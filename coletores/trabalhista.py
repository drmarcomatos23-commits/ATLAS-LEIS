"""Frente trabalhista: o que o ctresb/leis ainda não cobre.

1. TRT-2 (abrange Santos e a Baixada): súmulas, orientações jurisprudenciais, precedentes
   normativos e teses jurídicas prevalecentes, das páginas de jurisprudência consolidada.
2. Precedentes qualificados do Banco Nacional de Precedentes do CNJ (pangeabnp): temas de
   recursos repetitivos (IRR), IAC e demais precedentes do TST e do TRT-2.
(CLT, reforma, súmulas e OJs do TST já estão no ctresb/leis; NRs vêm de coletores/paginas.py.)
"""
from __future__ import annotations

import json
import re

from bs4 import BeautifulSoup

from comum import (Pausa, gravar, html_para_md, montar_md, registrar_falha, salvar_estado, sessao,
                   slug)

NOME = "trabalhista"
BASE_TRT2 = "https://ww2.trt2.jus.br/jurisprudencia/jurisprudencia/trt2-jurisprudencia-consolidada/"
PAGINAS_TRT2 = [
    ("sumulas", "S[ÚU]MULA", "Súmula"),
    ("orientacoes-jurisprudenciais", "ORIENTA[ÇC][ÃA]O JURISPRUDENCIAL", "Orientação Jurisprudencial"),
    ("precedentes-normativos", "PRECEDENTE NORMATIVO", "Precedente Normativo"),
    ("teses-juridicas-prevalecentes", "TESE JUR[ÍI]DICA PREVALECENTE", "Tese Jurídica Prevalecente"),
]
BNP = "https://pangeabnp.pdpj.jus.br/api/v1/precedentes"
NOMES_BNP = {"IRR": "Tema de recurso repetitivo (IRR)", "IAC": "Incidente de assunção de competência",
             "IRDR": "Tema de IRDR", "SUM": "Súmula", "OJ": "Orientação jurisprudencial",
             "PN": "Precedente normativo", "TJP": "Tese jurídica prevalecente", "RR": "Recurso repetitivo"}


def trt2(s, pausa) -> int:
    n = 0
    for pagina, rotulo, tipo in PAGINAS_TRT2:
        try:
            pausa()
            r = s.get(BASE_TRT2 + pagina, timeout=90)
            r.raise_for_status()
            sopa = BeautifulSoup(r.text, "html.parser")
            corpo = sopa.select_one("main, #content, .content, article") or sopa.body
            md = html_para_md(str(corpo))
            itens = list(re.finditer(rf"^[#*\s]*{rotulo}\s*(?:N[º°o.]*\s*)?(\d+)", md, re.I | re.M)) \
                or list(re.finditer(r"^\*\*\s*(\d+)\s*[-.–]", md, re.M))  # formato "**12 - Título.**"
            base = {"tribunal": "TRT2", "tipo": tipo, "versao_texto": "página de jurisprudência consolidada do TRT-2",
                    "fonte": BASE_TRT2 + pagina}
            n += gravar(f"jurisprudencia/trt2/{pagina}/{pagina}-compendio.md",
                        montar_md({**base, "titulo": f"{tipo}s do TRT-2 (compêndio)"}, f"{tipo}s do TRT-2", md),
                        NOME, {"tribunal": "TRT2", "tipo": tipo, "titulo": f"{tipo}s do TRT-2"})
            vistos = set()
            for i, m in enumerate(itens):
                numero = m.group(1)
                if numero in vistos:
                    continue
                vistos.add(numero)
                fim = itens[i + 1].start() if i + 1 < len(itens) else len(md)
                trecho = md[m.start():fim].strip()
                titulo = f"{tipo} nº {numero} do TRT-2"
                situacao = "cancelada" if re.search(r"cancelad", trecho[:400], re.I) else ""
                n += gravar(f"jurisprudencia/trt2/{pagina}/{slug(tipo)}-{numero}.md",
                            montar_md({**base, "titulo": titulo, "numero": numero, "situacao": situacao},
                                      titulo, trecho), NOME,
                            {"tribunal": "TRT2", "tipo": tipo, "numero": numero,
                             "ementa": " ".join(trecho.split())[:300]})
            print(f"[trabalhista] TRT-2 {pagina}: {len(vistos)} itens")
        except Exception as e:
            print(f"[trabalhista] TRT-2 {pagina}: falhou — {e!r}")
            registrar_falha(NOME, pagina, repr(e))
    return n


# códigos aceitos pelo BNP com registros da Justiça do Trabalho (verificado em nov/2026)
TIPOS_CANDIDATOS = ["IRR", "RR", "IAC", "IRDR", "SIRDR"]


def bnp(s, pausa, orgao: str) -> int:
    """Precedentes do órgão no BNP, tipo a tipo (a API exige a lista de tipos e recusa códigos
    desconhecidos com HTTP 400 — assim descobrimos quais existem)."""
    n = 0
    for tipo in TIPOS_CANDIDATOS:
        try:
            n += bnp_tipo(s, pausa, orgao, [tipo])
        except Exception as e:
            print(f"[trabalhista] BNP {orgao}/{tipo}: {str(e)[:80]}")
    return n


def bnp_tipo(s, pausa, orgao: str, tipos: list) -> int:
    n, pagina, total, contagem = 0, 1, None, {}
    while True:
        filtro = {"buscaGeral": "", "todasPalavras": "", "quaisquerPalavras": "", "semPalavras": "",
                  "trechoExato": "", "atualizacaoDesde": "", "atualizacaoAte": "", "cancelados": True,
                  "ordenacao": "Text", "nr": "", "pagina": pagina, "tamanhoPagina": 50,
                  "orgaos": [orgao], "tipos": tipos}
        pausa()
        r = s.post(BNP, json={"filtro": filtro}, timeout=90, headers={"Accept": "application/json"})
        r.raise_for_status()
        d = r.json()
        total = d.get("total", total)
        res = d.get("resultados") or []
        if not res:
            break
        for reg in res:
            try:
                tipo, nr = reg.get("tipo", "OUTRO"), str(reg.get("nr", ""))
                contagem[tipo] = contagem.get(tipo, 0) + 1
                nome_tipo = NOMES_BNP.get(tipo, tipo)
                titulo = f"{nome_tipo} nº {nr} do {orgao}"
                corpo = []
                for campo, rot in (("questao", "Questão"), ("tese", "Tese"), ("situacao", "Situação")):
                    if reg.get(campo):
                        corpo += [f"## {rot}", "", str(reg[campo]), ""]
                corpo += ["## Registro original do CNJ", "", "```json",
                          json.dumps(reg, ensure_ascii=False, indent=2), "```"]
                meta = {"titulo": titulo, "tribunal": orgao, "tipo": nome_tipo, "numero": nr,
                        "situacao": reg.get("situacao", ""), "ementa": str(reg.get("questao", ""))[:600],
                        "versao_texto": "Banco Nacional de Precedentes do CNJ",
                        "atualizacao_fonte": reg.get("ultimaAtualizacao", ""), "fonte": BNP,
                        "id_fonte": reg.get("id", "")}
                n += gravar(f"jurisprudencia/{orgao.lower().replace('trt02', 'trt2')}/precedentes/{slug(tipo)}-{slug(nr)}.md",
                            montar_md(meta, titulo, "\n".join(corpo)), NOME,
                            {"tribunal": orgao, "tipo": nome_tipo, "numero": nr,
                             "ementa": meta["ementa"][:300], "situacao": meta["situacao"]})
            except Exception as e:
                registrar_falha(NOME, reg.get("id"), repr(e))
        pagina += 1
        if pagina > 400:
            break
    print(f"[trabalhista] BNP {orgao}/{tipos[0]}: total informado {total}; por tipo {contagem}")
    return n


def main():
    s, pausa, n = sessao(), Pausa(1.2), 0
    n += trt2(s, pausa)
    for orgao in ("TST", "TRT02", "TRT2"):  # o código do TRT-2 no BNP varia
        try:
            n += bnp(s, pausa, orgao)
        except Exception as e:
            print(f"[trabalhista] BNP {orgao}: falhou — {e!r}")
            registrar_falha(NOME, f"bnp-{orgao}", repr(e))
    salvar_estado(NOME, {"ultima_execucao_gravou": n})
    print(f"[trabalhista] {n} arquivos gravados")


if __name__ == "__main__":
    main()
