"""Índices compactos (JSON) para uso direto no navegador — usados pelo módulo ATLAS LAW do Atlas Contencioso.

Juntam o ATLAS-LEIS e o ctresb/leis (clonado parcialmente em CTRESB) em arquivos pequenos:
- indices/trabalho.json  súmulas e OJs do TST, temas de IRR/IAC/IRDR do TST, jurisprudência do TRT-2
- indices/civel.json     súmulas e repetitivos do STJ, súmulas/IRDR/enunciados do TJ-SP
- indices/geral.json     súmulas vinculantes e temas de repercussão geral do STF
- indices/normas.json    legislação-base por área, com caminho no acervo
- indices/novidades.json o que entrou/mudou nos últimos 30 dias
Cada item: id, trib, tipo, num, tit, txt (≤ 600 caracteres), sit, repo, path.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CTRESB = Path(os.environ.get("CTRESB", "/tmp/ctresb"))
SAIDA = RAIZ / "indices"
REPO_ATLAS = "drmarcomatos23-commits/ATLAS-LEIS"
REPO_CTRESB = "ctresb/leis"


def ler_md(p: Path):
    t = p.read_text(encoding="utf-8", errors="replace")
    meta, corpo = {}, t
    if t.startswith("---"):
        partes = t.split("---", 2)
        if len(partes) == 3:
            for linha in partes[1].splitlines():
                m = re.match(r"^(\w+):\s*(.*)$", linha)
                if m:
                    v = m.group(2).strip()
                    if v.startswith('"') and v.endswith('"'):
                        try:
                            v = json.loads(v)
                        except Exception:
                            v = v.strip('"')
                    meta[m.group(1)] = v
            corpo = partes[2]
    return meta, corpo


def resumo(corpo: str, n: int = 450) -> str:
    corpo = re.sub(r"```.*?```", " ", corpo, flags=re.S)           # JSON bruto do CNJ
    corpo = re.sub(r"^#.*$", " ", corpo, flags=re.M)                # títulos
    corpo = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", corpo)          # links markdown
    corpo = re.sub(r"<br\s*/?>|\*\*|__", " ", corpo)
    corpo = re.sub(r"-\n(\w)", r"\1", corpo)                        # hifenização do PDF
    corpo = " ".join(corpo.split())
    corpo = re.sub(r"^\d+\s+Tema\s+\d+\s+(?:\d{4}-\d{2}-\d{2}\s+)+", "", corpo)  # cabeçalho numérico do STJ
    return corpo[:n]


def item(p: Path, base: Path, repo: str, trib: str, tipo: str):
    meta, corpo = ler_md(p)
    num = str(meta.get("numero", "")).strip()
    sit = str(meta.get("situacao", "") or ("revogada" if str(meta.get("revogada")) == "true" else ""))
    txt = resumo(corpo)
    if re.search(r"cancelad", txt[:250], re.I) and not sit:
        sit = "cancelada"
    rel = p.relative_to(base).as_posix()
    tipo = tipo or meta.get("tipo", "")
    return {"id": f"{trib}-{p.parent.name}-{p.stem}".lower(), "trib": trib, "tipo": tipo, "num": num,
            "tit": meta.get("titulo", p.stem), "txt": txt, "sit": sit[:80], "repo": repo, "path": rel}


def coletar(base: Path, repo: str, padrao: str, trib: str, tipo: str, excluir: str = r"compendio"):
    out = []
    for p in sorted(base.glob(padrao)):
        if p.suffix == ".md" and not re.search(excluir, p.name):
            try:
                out.append(item(p, base, repo, trib, tipo))
            except Exception as e:
                print("falha", p, e, file=sys.stderr)
    return out


NORMAS = {  # legislação-base por área (caminhos conferidos no ctresb/leis)
    "geral": [("Constituição Federal", "constituicao.md"),
              ("CPC – Lei 13.105/2015", "federal/leis-ordinarias/2015/lei-13105-2015-03-16.md"),
              ("Código Civil – Lei 10.406/2002", "federal/leis-ordinarias/2002/lei-10406-2002-01-10.md")],
    "trabalho": [("CLT – Decreto-Lei 5.452/1943", "federal/decretos-lei/1943/del-5452-1943-05-01.md"),
                 ("Reforma trabalhista – Lei 13.467/2017", "federal/leis-ordinarias/2017/lei-13467-2017-07-13.md"),
                 ("Terceirização – Lei 6.019/1974", "federal/leis-ordinarias/1974/lei-6019-1974-01-03.md"),
                 ("FGTS – Lei 8.036/1990", "federal/leis-ordinarias/1990/lei-8036-1990-05-11.md"),
                 ("Repouso semanal – Lei 605/1949", "federal/leis-ordinarias/1949/lei-605-1949-01-05.md"),
                 ("Benefícios da Previdência – Lei 8.213/1991", "federal/leis-ordinarias/1991/lei-8213-1991-07-24.md")],
    "civel": [("CDC – Lei 8.078/1990", "federal/leis-ordinarias/1990/lei-8078-1990-09-11.md"),
              ("Locações – Lei 8.245/1991", "federal/leis-ordinarias/1991/lei-8245-1991-10-18.md"),
              ("Registros Públicos – Lei 6.015/1973", "federal/leis-ordinarias/1973/lei-6015-1973-12-31.md"),
              ("Recuperação e falência – Lei 11.101/2005", "federal/leis-ordinarias/2005/lei-11101-2005-02-09.md"),
              ("Sociedades anônimas – Lei 6.404/1976", "federal/leis-ordinarias/1976/lei-6404-1976-12-15.md"),
              ("Mandado de segurança – Lei 12.016/2009", "federal/leis-ordinarias/2009/lei-12016-2009-08-07.md"),
              ("Ação civil pública – Lei 7.347/1985", "federal/leis-ordinarias/1985/lei-7347-1985-07-24.md")],
    "tributario": [("CTN – Lei 5.172/1966", "federal/leis-ordinarias/1966/lei-5172-1966-10-25.md"),
                   ("Execução fiscal – Lei 6.830/1980", "federal/leis-ordinarias/1980/lei-6830-1980-09-22.md"),
                   ("Simples Nacional – LC 123/2006", "federal/leis-complementares/2006/lcp-123-2006-12-14.md"),
                   ("IBS/CBS – LC 214/2025", "federal/leis-complementares/2025/lcp-214-2025-01-16.md"),
                   ("ITCMD-SP – Lei 10.705/2000", "estaduais/SP/leis-ordinarias/2000/lei-10705-2000-12-28-id4368.md")],
}


def gravar(nome: str, dados):
    SAIDA.mkdir(exist_ok=True)
    (SAIDA / nome).write_text(json.dumps(dados, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"[indices] {nome}: {len(dados) if isinstance(dados, list) else 'ok'}")


def main():
    if not (CTRESB / "jurisprudencia").exists():
        sys.exit(f"ctresb/leis não encontrado em {CTRESB}")
    A, C = RAIZ, CTRESB
    trabalho = (coletar(C, REPO_CTRESB, "jurisprudencia/tst/sumulas/*.md", "TST", "Súmula")
                + coletar(C, REPO_CTRESB, "jurisprudencia/tst/orientacoes-jurisprudenciais/*.md", "TST", "OJ")
                + coletar(A, REPO_ATLAS, "jurisprudencia/tst/precedentes/*.md", "TST", "")
                + coletar(A, REPO_ATLAS, "jurisprudencia/trt2/sumulas/*.md", "TRT2", "Súmula")
                + coletar(A, REPO_ATLAS, "jurisprudencia/trt2/teses-juridicas-prevalecentes/*.md", "TRT2", "Tese prevalecente")
                + coletar(A, REPO_ATLAS, "jurisprudencia/trt2/orientacoes-jurisprudenciais/*.md", "TRT2", "OJ")
                + coletar(A, REPO_ATLAS, "jurisprudencia/trt2/precedentes-normativos/*.md", "TRT2", "Precedente normativo")
                + coletar(A, REPO_ATLAS, "jurisprudencia/trt2/precedentes/*.md", "TRT2", "")
                + coletar(A, REPO_ATLAS, "reguladores/mte/normas-regulamentadoras/*.md", "MTE", "NR"))
    civel = (coletar(C, REPO_CTRESB, "jurisprudencia/stj/sumulas/*.md", "STJ", "Súmula")
             + coletar(C, REPO_CTRESB, "jurisprudencia/stj/repetitivos/*.md", "STJ", "Tema repetitivo")
             + coletar(A, REPO_ATLAS, "jurisprudencia/tjsp/sumulas/*.md", "TJSP", "Súmula")
             + coletar(A, REPO_ATLAS, "jurisprudencia/tjsp/irdr/*.md", "TJSP", "Tema de IRDR")
             + coletar(A, REPO_ATLAS, "jurisprudencia/tjsp/enunciados/*.md", "TJSP", "Enunciado"))
    geral = (coletar(C, REPO_CTRESB, "jurisprudencia/stf/sumulas-vinculantes/*.md", "STF", "Súmula vinculante")
             + coletar(C, REPO_CTRESB, "jurisprudencia/stf/repercussao-geral/*.md", "STF", "Tema de repercussão geral"))
    gravar("trabalho.json", trabalho)
    gravar("civel.json", civel)
    gravar("geral.json", geral)
    normas = {area: [{"tit": t, "repo": REPO_CTRESB, "path": p} for t, p in lst]  # caminhos conferidos
              for area, lst in NORMAS.items()}
    normas["trabalho"].append({"tit": "Normas Regulamentadoras (NRs)", "repo": REPO_ATLAS,
                               "path": "reguladores/mte/normas-regulamentadoras/"})
    gravar("normas.json", normas)
    limite = (dt.date.today() - dt.timedelta(days=30)).isoformat()
    recente = (dt.date.today() - dt.timedelta(days=120)).isoformat()  # a carga inicial de acervo antigo não é novidade
    novidades = []
    for p in sorted((A / "_novidades").glob("*.jsonl")):
        if p.name[:10] < limite:
            continue
        for linha in p.read_text(encoding="utf-8").splitlines():
            try:
                n = json.loads(linha)
            except Exception:
                continue
            if not (A / n["arquivo"]).exists():
                continue
            if n.get("coletor") in ("dou", "santos_do", "peruibe_do") or (n.get("data") or "") >= recente:
                novidades.append({"dia": p.name[:10], "col": n.get("coletor"), "tipo": n.get("tipo", ""),
                                  "num": n.get("numero", ""), "tit": n.get("titulo") or n.get("tipo", ""),
                                  "txt": (n.get("ementa") or "")[:300], "trib": n.get("tribunal") or n.get("orgao") or n.get("municipio", ""),
                                  "repo": REPO_ATLAS, "path": n["arquivo"]})
    gravar("novidades.json", novidades[-1500:])


if __name__ == "__main__":
    main()
