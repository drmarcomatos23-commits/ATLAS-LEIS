"""Base comum dos coletores do ATLAS-LEIS.

Formato de saída idêntico ao do acervo ctresb/leis: cabeçalho YAML + título em `#` + texto.
Cada coletor é incremental: guarda o ponto em que parou em `estado/<coletor>.json`
e registra o que entrou de novo em `_novidades/AAAA-MM-DD.jsonl`.
"""
from __future__ import annotations

import datetime as dt
import io
import json
import os
import re
import time
import unicodedata
from pathlib import Path

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

RAIZ = Path(__file__).resolve().parent.parent
ESTADO = RAIZ / "estado"
NOVIDADES = RAIZ / "_novidades"
HOJE = dt.date.today().isoformat()
UA = "ATLAS-LEIS/1.0 (+https://github.com/drmarcomatos23-commits/ATLAS-LEIS; coleta de legislacao publica)"

ORDEM_CAMPOS = [
    "titulo", "uf", "municipio", "orgao", "tribunal", "tipo", "numero", "data", "ano", "ementa",
    "situacao", "revogada", "versao_texto", "publicacao", "data_publicacao", "urn", "fonte",
    "arquivo", "id_fonte", "baixado_em",
]

MESES = {m: i for i, m in enumerate(
    ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto",
     "setembro", "outubro", "novembro", "dezembro"], start=1)}


def sessao() -> requests.Session:
    s = requests.Session()
    retry = Retry(total=4, backoff_factor=1.5, status_forcelist=(429, 500, 502, 503, 504),
                  allowed_methods=("GET", "HEAD"), respect_retry_after_header=True)
    s.mount("https://", HTTPAdapter(max_retries=retry))
    s.mount("http://", HTTPAdapter(max_retries=retry))
    s.headers.update({"User-Agent": UA, "Accept-Language": "pt-BR,pt;q=0.9"})
    return s


class Pausa:
    """Limita o ritmo de requisições por fonte (respeito aos servidores públicos)."""

    def __init__(self, segundos: float = 1.0):
        self.segundos = segundos
        self._ultimo = 0.0

    def __call__(self):
        falta = self.segundos - (time.monotonic() - self._ultimo)
        if falta > 0:
            time.sleep(falta)
        self._ultimo = time.monotonic()


class Prazo:
    """Orçamento de tempo de um coletor dentro do job do GitHub Actions."""

    def __init__(self, minutos: float):
        self.fim = time.monotonic() + minutos * 60

    def esgotado(self) -> bool:
        return time.monotonic() >= self.fim


def slug(txt: str) -> str:
    txt = unicodedata.normalize("NFKD", txt or "").encode("ascii", "ignore").decode()
    txt = re.sub(r"[^a-zA-Z0-9]+", "-", txt.lower()).strip("-")
    return txt or "sem-nome"


def so_digitos(txt) -> str:
    return re.sub(r"\D", "", str(txt or ""))


def data_extenso(txt: str) -> str | None:
    """'21 de dezembro de 2009' -> '2009-12-21'."""
    t = unicodedata.normalize("NFKD", txt or "").encode("ascii", "ignore").decode().lower()
    m = re.search(r"(\d{1,2})\s*(?:o|º)?\s+de\s+([a-z]+)\s+de\s+(\d{4})", t)
    if not m or m.group(2) not in MESES:
        return None
    try:
        return dt.date(int(m.group(3)), MESES[m.group(2)], int(m.group(1))).isoformat()
    except ValueError:
        return None


def data_br(txt: str) -> str | None:
    """'16/04/2024' -> '2024-04-16'."""
    m = re.search(r"(\d{1,2})/(\d{1,2})/(\d{4})", txt or "")
    if not m:
        return None
    try:
        return dt.date(int(m.group(3)), int(m.group(2)), int(m.group(1))).isoformat()
    except ValueError:
        return None


def _yaml_valor(v) -> str:
    if v is None:
        return ""
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return f'"{v}"'
    v = str(v)
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", v):
        return v
    return json.dumps(v, ensure_ascii=False)


def montar_md(meta: dict, titulo: str, corpo: str) -> str:
    meta = dict(meta)
    meta.setdefault("titulo", titulo)
    meta.setdefault("baixado_em", HOJE)
    linhas = ["---"]
    for k in ORDEM_CAMPOS + sorted(set(meta) - set(ORDEM_CAMPOS)):
        if k in meta and meta[k] not in (None, ""):
            linhas.append(f"{k}: {_yaml_valor(meta[k])}")
        elif k == "data":
            linhas.append("data:")
    linhas += ["---", "", f"# {titulo}", "", limpar_texto(corpo), ""]
    return "\n".join(linhas)


def limpar_texto(t: str) -> str:
    t = (t or "").replace("\r", "").replace("\x00", "")
    t = re.sub(r"[ \t]+\n", "\n", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


def texto_pdf(conteudo: bytes) -> str:
    """Extrai a camada de texto do PDF. PDFs só com imagem voltam vazios (OCR fica para a fila)."""
    try:
        from pypdf import PdfReader
        leitor = PdfReader(io.BytesIO(conteudo))
        return "\n\n".join((p.extract_text() or "") for p in leitor.pages)
    except Exception as e:  # PDF corrompido ou protegido
        return f"[texto não extraído: {type(e).__name__}]"


def texto_arquivo(conteudo: bytes, nome: str = "", tipo: str = "") -> str:
    """Texto de PDF, DOC (antiword), DOCX, RTF ou HTML, conforme assinatura do arquivo."""
    import subprocess
    import tempfile
    nome, tipo = (nome or "").lower(), (tipo or "").lower()
    if conteudo[:4] == b"%PDF":
        return texto_pdf(conteudo)
    if conteudo[:4] == b"PK\x03\x04":  # docx / odt
        try:
            import docx2txt
            with tempfile.NamedTemporaryFile(suffix=".docx") as f:
                f.write(conteudo); f.flush()
                return docx2txt.process(f.name) or ""
        except Exception as e:
            return f"[texto não extraído: {type(e).__name__}]"
    if conteudo[:8] == b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1":  # .doc (OLE)
        with tempfile.NamedTemporaryFile(suffix=".doc") as f:
            f.write(conteudo); f.flush()
            for cmd in (["antiword", "-w", "0", f.name], ["catdoc", "-w", f.name]):
                try:
                    r = subprocess.run(cmd, capture_output=True, timeout=120)
                    if r.returncode == 0 and r.stdout.strip():
                        return r.stdout.decode("utf-8", "replace")
                except FileNotFoundError:
                    continue
        return "[texto não extraído: .doc sem conversor disponível]"
    if conteudo[:5] == b"{\\rtf":
        from striprtf.striprtf import rtf_to_text
        return rtf_to_text(conteudo.decode("latin-1", "replace"))
    if "html" in tipo or conteudo[:200].lstrip().lower().startswith((b"<!doctype", b"<html")):
        return html_para_md(conteudo.decode("utf-8", "replace"))
    try:
        return conteudo.decode("utf-8")
    except UnicodeDecodeError:
        return conteudo.decode("latin-1", "replace")


def html_para_md(html: str) -> str:
    from bs4 import BeautifulSoup
    from markdownify import markdownify
    sopa = BeautifulSoup(html, "html.parser")
    for tag in sopa(["script", "style", "nav", "header", "footer", "form", "noscript"]):
        tag.decompose()
    return markdownify(str(sopa), heading_style="ATX", strip=["img"])


def gravar(caminho_rel: str, conteudo: str, coletor: str, resumo: dict) -> bool:
    """Grava o arquivo; registra novidade se for novo ou se o texto mudou. Retorna True se gravou."""
    destino = RAIZ / caminho_rel
    destino.parent.mkdir(parents=True, exist_ok=True)
    novo = not destino.exists()
    if not novo:
        antigo = re.sub(r"\nbaixado_em: .*", "", destino.read_text(encoding="utf-8"))
        if antigo == re.sub(r"\nbaixado_em: .*", "", conteudo):
            return False
    destino.write_text(conteudo, encoding="utf-8")
    NOVIDADES.mkdir(exist_ok=True)
    with open(NOVIDADES / f"{HOJE}-{coletor}.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps({"coletor": coletor, "evento": "nova" if novo else "alterada",
                            "arquivo": caminho_rel, **resumo}, ensure_ascii=False) + "\n")
    return True


def ler_estado(nome: str) -> dict:
    p = ESTADO / f"{nome}.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def salvar_estado(nome: str, estado: dict):
    ESTADO.mkdir(exist_ok=True)
    (ESTADO / f"{nome}.json").write_text(json.dumps(estado, ensure_ascii=False, indent=2), encoding="utf-8")


def registrar_falha(nome: str, item, erro: str):
    ESTADO.mkdir(exist_ok=True)
    with open(ESTADO / f"{nome}_falhas.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps({"data": HOJE, "item": item, "erro": erro[:300]}, ensure_ascii=False) + "\n")


def minutos_env(padrao: float) -> float:
    return float(os.environ.get("ATLAS_MINUTOS", padrao))
