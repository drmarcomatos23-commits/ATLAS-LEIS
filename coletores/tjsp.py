"""TJ-SP: súmulas, enunciados (inclusive do Grupo de Câmaras Empresariais) e temas de IRDR.

- Súmulas: PDF oficial da Biblioteca do TJ-SP, separado em um arquivo por súmula.
- Enunciados: PDFs listados na página de Enunciados + Grupo de Câmaras Empresariais.
- IRDR: página do NUGEP com a lista de temas; cada tema em um arquivo.
Tudo é revisitado a cada execução; só grava o que mudou.
"""
from __future__ import annotations

import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from comum import (Pausa, gravar, html_para_md, montar_md, registrar_falha, sessao, slug,
                   texto_arquivo)

NOME = "tjsp"
SUMULAS = "https://www.tjsp.jus.br/Download/Portal/Biblioteca/Biblioteca/Legislacao/SumulasTJSP.pdf"
EMPRESARIAIS = "https://www.tjsp.jus.br/Download/Rodape/GrupoCamarasEmpresariaisEnunciados.pdf"
ENUNCIADOS = "https://www.tjsp.jus.br/Enunciados"
IRDR = "https://www.tjsp.jus.br/NugepNac/Irdr"


def dividir(texto: str, rotulo: str):
    """Separa um compêndio em itens numerados ('Súmula 1', 'Enunciado I' ...)."""
    padrao = re.compile(rf"^\s*{rotulo}\s+(?:n[º°o.]*\s*)?([0-9]+|[IVXLC]+)\b\s*[:.–-]?", re.I | re.M)
    marcas = list(padrao.finditer(texto))
    for i, m in enumerate(marcas):
        fim = marcas[i + 1].start() if i + 1 < len(marcas) else len(texto)
        yield m.group(1), texto[m.start():fim].strip()


def compendio(s, pausa, url, rotulo, pasta, nome_doc, tipo):
    pausa()
    r = s.get(url, timeout=120)
    r.raise_for_status()
    texto = texto_arquivo(r.content, url, r.headers.get("content-type", ""))
    base = {"tribunal": "TJSP", "tipo": tipo, "versao_texto": "compêndio oficial em PDF do TJ-SP",
            "fonte": url}
    n = gravar(f"jurisprudencia/tjsp/{pasta}/{slug(nome_doc)}-compendio.md",
               montar_md({**base, "titulo": nome_doc}, nome_doc, texto), NOME,
               {"tribunal": "TJSP", "tipo": tipo, "ementa": nome_doc})
    vistos = set()
    for numero, trecho in dividir(texto, rotulo):
        if numero in vistos or len(trecho) < 30:
            continue
        vistos.add(numero)
        titulo = f"{tipo} {numero} do TJ-SP" + (f" – {nome_doc}" if "Empresar" in nome_doc else "")
        corpo = " ".join(trecho.split())
        n += gravar(f"jurisprudencia/tjsp/{pasta}/{slug(nome_doc)}-{slug(numero)}.md",
                    montar_md({**base, "titulo": titulo, "numero": numero}, titulo, corpo), NOME,
                    {"tribunal": "TJSP", "tipo": tipo, "numero": numero, "ementa": corpo[:300]})
    print(f"[tjsp] {nome_doc}: {len(vistos)} itens")
    return n


def irdr(s, pausa):
    pausa()
    r = s.get(IRDR, timeout=90)
    r.raise_for_status()
    sopa = BeautifulSoup(r.text, "html.parser")
    temas = {}
    for a in sopa.find_all("a", href=True):
        t = " ".join(a.get_text(" ").split())
        m = re.match(r"Tema\s+0*(\d+)\s*[-–]\s*IRDR\s*[-–]\s*(.+)", t, re.I)
        if m and "DetalheTema" in a["href"]:
            temas[m.group(1)] = (m.group(2), urljoin(IRDR, a["href"]))
    n = 0
    for numero, (assunto, url) in sorted(temas.items(), key=lambda x: int(x[0])):
        try:
            pausa()
            rd = s.get(url, timeout=90)
            rd.raise_for_status()
            sd = BeautifulSoup(rd.text, "html.parser")
            corpo = sd.select_one("#conteudo, .conteudo, main, article") or sd.body
            situacao = re.search(r"\(([^()]*)\)\s*$", assunto)
            titulo = f"Tema {numero} de IRDR do TJ-SP"
            meta = {"titulo": titulo, "tribunal": "TJSP", "tipo": "Tema de IRDR", "numero": numero,
                    "ementa": assunto, "situacao": situacao.group(1) if situacao else "",
                    "versao_texto": "página do NUGEP/TJ-SP", "fonte": url}
            n += gravar(f"jurisprudencia/tjsp/irdr/tema-{numero}.md",
                        montar_md(meta, titulo, html_para_md(str(corpo))), NOME,
                        {"tribunal": "TJSP", "tipo": "Tema de IRDR", "numero": numero, "ementa": assunto})
        except Exception as e:
            registrar_falha(NOME, url, repr(e))
    print(f"[tjsp] IRDR: {len(temas)} temas")
    return n


def enunciados(s, pausa):
    pausa()
    r = s.get(ENUNCIADOS, timeout=90)
    r.raise_for_status()
    sopa = BeautifulSoup(r.text, "html.parser")
    n = 0
    for a in sopa.find_all("a", href=True):
        url = urljoin(ENUNCIADOS, a["href"])
        nome = " ".join(a.get_text(" ").split())
        if url.lower().endswith(".pdf") and nome and "Enunciad" in (nome + url) and url != EMPRESARIAIS:
            try:
                n += compendio(s, pausa, url, "Enunciado", "enunciados", nome, "Enunciado")
            except Exception as e:
                registrar_falha(NOME, url, repr(e))
    return n


def main():
    s, pausa, total = sessao(), Pausa(1.5), 0
    for nome, f in [("súmulas", lambda: compendio(s, pausa, SUMULAS, "S[úu]mula", "sumulas",
                                                    "Súmulas do TJ-SP", "Súmula")),
                    ("câmaras empresariais", lambda: compendio(s, pausa, EMPRESARIAIS, "Enunciado",
                                                               "enunciados", "Enunciados do Grupo de Câmaras Empresariais",
                                                               "Enunciado")),
                    ("enunciados", lambda: enunciados(s, pausa)),
                    ("irdr", lambda: irdr(s, pausa))]:
        try:
            total += f()
        except Exception as e:
            print(f"[tjsp] {nome}: falhou — {e!r}")
            registrar_falha(NOME, nome, repr(e))
    print(f"[tjsp] {total} arquivos gravados")


if __name__ == "__main__":
    main()
