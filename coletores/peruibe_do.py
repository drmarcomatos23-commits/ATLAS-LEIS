"""Peruíbe — Diário Oficial do Município (DOM-E), publicado como posts no site da Prefeitura.

O portal de legislação da Câmara bloqueia acesso automatizado (desafio do Cloudflare); o DOM-E
não. Cada edição é um post com o PDF anexado. O coletor lê as edições novas (e, aos poucos, as
antigas), extrai leis, leis complementares e decretos e grava em
`municipais/SP/peruibe/diario-oficial/AAAA/MM/edicao-N/`.
"""
from __future__ import annotations

import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from comum import (Pausa, Prazo, gravar, ler_estado, minutos_env, montar_md, registrar_falha,
                   salvar_estado, sessao)
from santos_do import PASTA, atos, texto

NOME = "peruibe_do"
LISTA = "https://www.peruibe.sp.gov.br/diario-oficial-do-municipio-dom-e/"
POST = re.compile(r"/(\d{4})/(\d{2})/diario-oficial-do-municipio-dom-e-edicao-(\d+)[^/]*/?$")


def edicoes(s, pausa, pagina: int):
    pausa()
    url = LISTA if pagina == 1 else f"{LISTA}page/{pagina}/"
    r = s.get(url, timeout=90)
    if r.status_code == 404:
        return []
    r.raise_for_status()
    sopa = BeautifulSoup(r.text, "html.parser")
    achadas = {}
    for a in sopa.find_all("a", href=True):
        h = urljoin(url, a["href"])
        m = POST.search(h)
        if m:
            achadas[h] = (m.group(1), m.group(2), m.group(3), "extra" in h)
    return list(achadas.items())


def processar(s, pausa, url, ano, mes, numero, extra) -> int:
    pausa()
    r = s.get(url, timeout=90)
    r.raise_for_status()
    sopa = BeautifulSoup(r.text, "html.parser")
    pdfs = [urljoin(url, a["href"]) for a in sopa.find_all("a", href=True) if ".pdf" in a["href"].lower()]
    if not pdfs:
        return 0
    pausa()
    rp = s.get(pdfs[0], timeout=180)
    rp.raise_for_status()
    txt, n, vistos = texto(rp.content), 0, set()
    ed = f"{numero}{'-extra' if extra else ''}"
    for rotulo, num, trecho in atos(txt):
        pasta, tipo = PASTA[rotulo]
        if (pasta, num) in vistos:
            continue
        vistos.add((pasta, num))
        linhas = [l.strip() for l in trecho.splitlines() if l.strip()]
        ementa = next((l for l in linhas[1:6] if len(l) > 25 and l.upper() == l), "")
        titulo = f"{tipo} nº {num} – Município de Peruíbe (DOM-E ed. {ed})"
        meta = {"titulo": titulo, "uf": "SP", "municipio": "Peruíbe", "tipo": tipo, "numero": num,
                "ementa": ementa, "publicacao": f"DOM-E Peruíbe, edição {ed} ({mes}/{ano})",
                "versao_texto": "texto extraído do PDF do Diário Oficial (original da publicação)",
                "fonte": url, "arquivo": pdfs[0]}
        n += gravar(f"municipais/SP/peruibe/diario-oficial/{ano}/{mes}/edicao-{ed}/{pasta}-{num}.md",
                    montar_md(meta, titulo, trecho), NOME,
                    {"municipio": "Peruíbe", "tipo": tipo, "numero": num, "data": f"{ano}-{mes}-01",
                     "ementa": ementa[:300]})
    return n


def main():
    est = ler_estado(NOME)
    feitas = set(est.get("feitas", []))
    proxima_antiga = est.get("pagina_antiga", 2)
    s, pausa, prazo, total = sessao(), Pausa(1.5), Prazo(minutos_env(40)), 0
    paginas = [1] + list(range(proxima_antiga, proxima_antiga + 40))  # novas + carga das antigas
    for p in paginas:
        if prazo.esgotado():
            break
        try:
            lst = edicoes(s, pausa, p)
        except Exception as e:
            registrar_falha(NOME, f"pagina-{p}", repr(e))
            break
        if not lst and p > 1:
            proxima_antiga = p  # chegou ao fim do arquivo histórico
            break
        for url, (ano, mes, num, extra) in lst:
            if url in feitas or prazo.esgotado():
                continue
            try:
                total += processar(s, pausa, url, ano, mes, num, extra)
                feitas.add(url)
            except Exception as e:
                registrar_falha(NOME, url, repr(e))
        if p > 1:
            proxima_antiga = p + 1
        salvar_estado(NOME, {"feitas": sorted(feitas), "pagina_antiga": proxima_antiga})
    print(f"[peruibe_do] {len(feitas)} edições lidas; {total} atos gravados")


if __name__ == "__main__":
    main()
