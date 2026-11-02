"""Coletor genérico de "página oficial com lista de atos em PDF".

Configurado em `fontes.yml` (chave `paginas`): para cada página, segue os links que casam com
`padrao`, baixa o arquivo (ou, se o link for outra página, o primeiro PDF dentro dela),
extrai o texto e grava em `<pasta>/<slug-do-título>.md`. Serve para o DREI (instruções
normativas e manuais de registro), as Normas Regulamentadoras do MTE e afins.
"""
from __future__ import annotations

import re
import sys
from urllib.parse import urljoin

import yaml
from bs4 import BeautifulSoup

from comum import (RAIZ, Pausa, Prazo, gravar, minutos_env, montar_md, registrar_falha, sessao,
                   slug, texto_arquivo)

NOME = "paginas"


def pdf_de(s, pausa, url):
    """Devolve (bytes, url_final, content-type) do documento; resolve páginas intermediárias."""
    pausa()
    r = s.get(url, timeout=120)
    r.raise_for_status()
    ct = r.headers.get("content-type", "")
    if "html" not in ct or r.content[:4] == b"%PDF":
        return r.content, r.url, ct
    sopa = BeautifulSoup(r.text, "html.parser")
    for a in sopa.find_all("a", href=True):
        h = urljoin(r.url, a["href"])
        if re.search(r"\.pdf(/|$|\?|@@)", h, re.I):
            pausa()
            r2 = s.get(h, timeout=120)
            r2.raise_for_status()
            return r2.content, r2.url, r2.headers.get("content-type", "")
    return r.content, r.url, ct  # sem PDF: guarda a própria página


def coletar(s, pausa, cfg) -> int:
    pausa()
    r = s.get(cfg["url"], timeout=90)
    r.raise_for_status()
    sopa = BeautifulSoup(r.text, "html.parser")
    vistos, n = set(), 0
    for a in sopa.find_all("a", href=True):
        url = urljoin(r.url, a["href"]).split("#")[0]
        titulo = " ".join(a.get_text(" ").split())
        if not re.search(cfg["padrao"], url, re.I) or url in vistos or not titulo:
            continue
        if cfg.get("titulo_padrao") and not re.search(cfg["titulo_padrao"], titulo, re.I):
            continue
        vistos.add(url)
        try:
            conteudo, final, ct = pdf_de(s, pausa, url)
            texto = texto_arquivo(conteudo, final, ct)
            # título mais informativo: "Nº 81" sozinho vira "Instrução Normativa DREI nº 81"
            if cfg.get("prefixo_titulo") and re.match(r"^N\s*[º°o.]", titulo):
                titulo = f"{cfg['prefixo_titulo']} {titulo}"
            num = re.search(r"\b(?:N[ºo°.]*\s*|NR-?\s*)(\d+)", titulo, re.I)
            meta = {"titulo": titulo, "orgao": cfg.get("orgao", ""), "tipo": cfg.get("tipo", ""),
                    "numero": num.group(1) if num else "", "situacao": cfg.get("situacao", ""),
                    "revogada": bool(re.search(r"revogad", titulo, re.I)),
                    "versao_texto": cfg.get("versao_texto", "arquivo publicado na página oficial"),
                    "fonte": cfg["url"], "arquivo": final}
            n += gravar(f"{cfg['pasta']}/{slug(titulo)[:100]}.md", montar_md(meta, titulo, texto), NOME,
                        {"orgao": meta["orgao"], "tipo": meta["tipo"], "numero": meta["numero"],
                         "titulo": titulo})
        except Exception as e:
            registrar_falha(NOME, url, repr(e))
    print(f"[paginas] {cfg['nome']}: {len(vistos)} documentos, {n} gravados")
    return n


def main(filtro=None):
    fontes = yaml.safe_load((RAIZ / "fontes.yml").read_text(encoding="utf-8"))
    s, pausa, prazo = sessao(), Pausa(1.0), Prazo(minutos_env(40))
    for cfg in fontes.get("paginas", []):
        if prazo.esgotado() or (filtro and cfg["nome"] not in filtro):
            continue
        try:
            coletar(s, pausa, cfg)
        except Exception as e:
            print(f"[paginas] {cfg['nome']}: falhou — {e!r}")
            registrar_falha(NOME, cfg["nome"], repr(e))


if __name__ == "__main__":
    main(set(sys.argv[1:]) or None)
