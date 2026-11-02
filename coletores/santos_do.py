"""Vigia do Diário Oficial de Santos (diariooficial.santos.sp.gov.br).

Baixa a edição de cada dia (PDF), extrai o texto e separa as **leis, leis complementares e
decretos** publicados, gravando em `municipais/SP/santos/diario-oficial/AAAA/MM/DD/`. É a camada
"do dia": o LEGIS da Prefeitura (coletores/santos.py) recebe o mesmo ato depois, já catalogado.
"""
from __future__ import annotations

import datetime as dt
import re
import subprocess
import tempfile

from comum import (Pausa, data_extenso, gravar, ler_estado, montar_md, registrar_falha, salvar_estado,
                   sessao, texto_pdf)

NOME = "santos_do"
EDICAO = "https://diariooficial.santos.sp.gov.br/edicoes/inicio/download/{data}"
EPIGRAFE = re.compile(r"^\s*(LEI\s+COMPLEMENTAR|LEI|DECRETO)\s+N[º°.oO]*\s*([\d.]+)\s*(.*)$", re.M)
PASTA = {"LEI COMPLEMENTAR": ("lei-complementar", "Lei Complementar"), "LEI": ("lei", "Lei Ordinária"),
         "DECRETO": ("decreto", "Decreto")}


def texto(pdf: bytes) -> str:
    """pdftotext (lê colunas em ordem) quando existe; senão pypdf."""
    try:
        with tempfile.NamedTemporaryFile(suffix=".pdf") as f:
            f.write(pdf)
            f.flush()
            r = subprocess.run(["pdftotext", "-enc", "UTF-8", f.name, "-"], capture_output=True, timeout=300)
            if r.returncode == 0 and len(r.stdout) > 500:
                return r.stdout.decode("utf-8", "replace")
    except FileNotFoundError:
        pass
    return texto_pdf(pdf)


def atos(txt: str):
    marcas = list(EPIGRAFE.finditer(txt))
    for i, m in enumerate(marcas):
        fim = marcas[i + 1].start() if i + 1 < len(marcas) else len(txt)
        trecho = txt[m.start():min(fim, m.start() + 30000)].strip()
        # descarta citações e republicações parciais: o ato publicado traz a data logo após a epígrafe
        # ("LEI Nº 4.813 / DE 23 DE OUTUBRO DE 2026") e a promulgação/decretação em seguida
        data = data_extenso(trecho[:160])
        if not data or not re.search(r"fa[çc]o saber|DECRETA|decreta:|promulgo|sanciono", trecho[:1500], re.I):
            continue
        rotulo = " ".join(m.group(1).upper().split())
        yield rotulo, m.group(2).replace(".", ""), trecho, data


def ementa_de(trecho: str) -> str:
    """Bloco em maiúsculas entre a epígrafe/data/(projeto e autor) e a fórmula de promulgação."""
    linhas = [l.strip() for l in trecho.splitlines()[1:30] if l.strip()]
    bloco, parenteses = [], 0
    for l in linhas:
        if re.search(r"Prefeit|faço saber|DECRETA|C[ÂA]MARA MUNICIPAL APROVOU|usando das atribui", l, re.I):
            break
        abre, fecha = l.count("("), l.count(")")
        if parenteses or abre:  # pula "(PROJETO DE LEI ... – AUTOR: ...)" mesmo quebrado em linhas
            parenteses = max(0, parenteses + abre - fecha)
            continue
        if re.match(r"^DE\s+\d", l, re.I) and not bloco:
            continue
        if l.upper() == l and len(l) > 3:
            bloco.append(l)
        elif bloco:
            break
    return " ".join(bloco)[:600]


def main(dias: int = 10):
    est = ler_estado(NOME)
    hoje = dt.date.today()
    dia = dt.date.fromisoformat(est["ultimo"]) + dt.timedelta(days=1) if est.get("ultimo") \
        else hoje - dt.timedelta(days=dias)
    s, pausa, total = sessao(), Pausa(2.0), 0
    while dia <= hoje:
        url = EDICAO.format(data=dia.isoformat())
        try:
            pausa()
            r = s.get(url, timeout=180)
            r.raise_for_status()
            if r.content[:4] != b"%PDF":  # "Não foi encontrada nenhuma edição no dia ..."
                print(f"[santos_do] {dia}: sem edição")
                if dia < hoje:
                    salvar_estado(NOME, {"ultimo": dia.isoformat()})
                dia += dt.timedelta(days=1)
                continue
            txt, achados = texto(r.content), 0
            vistos = set()
            for rotulo, numero, trecho, data in atos(txt):
                pasta, tipo = PASTA[rotulo]
                if data < (dia - dt.timedelta(days=120)).isoformat():
                    continue  # menção a norma antiga quebrada em linha própria, não publicação do ato
                if (pasta, numero) in vistos:
                    continue
                vistos.add((pasta, numero))
                ementa = ementa_de(trecho)
                titulo = f"{tipo} nº {numero}, de {data[8:]}/{data[5:7]}/{data[:4]} – Município de Santos"
                meta = {"titulo": titulo, "uf": "SP", "municipio": "Santos", "tipo": tipo, "numero": numero,
                        "data": data,
                        "ementa": ementa, "publicacao": f"Diário Oficial de Santos de {dia:%d/%m/%Y}",
                        "data_publicacao": dia.isoformat(),
                        "versao_texto": "texto extraído do PDF do Diário Oficial (original da publicação)",
                        "fonte": url}
                total += gravar(f"municipais/SP/santos/diario-oficial/{dia:%Y/%m/%d}/{pasta}-{numero}.md",
                                montar_md(meta, titulo, trecho), NOME,
                                {"municipio": "Santos", "tipo": tipo, "numero": numero,
                                 "data": data, "ementa": ementa[:300]})
                achados += 1
            print(f"[santos_do] {dia}: {achados} leis/decretos")
            salvar_estado(NOME, {"ultimo": dia.isoformat()})
        except Exception as e:
            registrar_falha(NOME, dia.isoformat(), repr(e))
            break
        dia += dt.timedelta(days=1)
    print(f"[santos_do] {total} atos gravados")


if __name__ == "__main__":
    main()
