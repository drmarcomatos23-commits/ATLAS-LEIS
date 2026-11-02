"""SEFAZ-SP — Portal de Legislação Tributária (legislacao.fazenda.sp.gov.br), via API REST do SharePoint.

A biblioteca "Páginas" guarda cada ato (leis, decretos, RICMS, portarias CAT/SRE, decisões
normativas) e cada **Resposta à Consulta Tributária** como uma página com o HTML integral em
`PublishingPageContent`. O coletor lista os itens em ordem de ID (o firewall do portal recusa
filtros), baixa o conteúdo dos novos e alterados e grava em `estaduais/SP/sefaz/<tipo>/`.
"""
from __future__ import annotations

import re

from comum import (Pausa, Prazo, data_br, data_extenso, gravar, html_para_md, ler_estado,
                   minutos_env, montar_md, registrar_falha, salvar_estado, sessao, slug)

NOME = "sefaz_sp"
API = "https://legislacao.fazenda.sp.gov.br/_api/web/lists/getbytitle('P%C3%A1ginas')"
LISTA = API + "/items?$select=Id,Title,FileRef,Modified&$orderby=Id&$top=500"
ITEM = API + "/items({id})?$select=Id,Title,FileRef,Modified,Created,PublishingPageContent"
JSON = {"Accept": "application/json;odata=nometadata"}

CLASSES = [
    (r"Resposta\s+(?:[àa]\s+)?Consulta|^RC\s", "respostas-consultas", "Resposta à Consulta Tributária"),
    (r"Decis[ãa]o\s+Normativa", "decisoes-normativas", "Decisão Normativa"),
    (r"Lei\s+Complementar", "leis-complementares", "Lei Complementar"),
    (r"^Lei\b", "leis-ordinarias", "Lei"),
    (r"^Decreto", "decretos", "Decreto"),
    (r"Portaria", "portarias", "Portaria"),
    (r"Resolu[çc][ãa]o", "resolucoes", "Resolução"),
    (r"Comunicado", "comunicados", "Comunicado"),
    (r"RICMS|Regulamento", "regulamentos", "Regulamento"),
]


def classificar(titulo: str):
    for padrao, pasta, tipo in CLASSES:
        if re.search(padrao, titulo, re.I):
            return pasta, tipo
    return "outros-atos", "Ato normativo"


def main():
    est = ler_estado(NOME)
    conhecidos: dict = est.get("modificado", {})  # id -> Modified já gravado
    s, pausa, prazo = sessao(), Pausa(0.8), Prazo(minutos_env(40))
    url, pendentes = LISTA, []
    while url and not prazo.esgotado():  # 1) índice completo (leve)
        pausa()
        r = s.get(url, headers=JSON, timeout=90)
        r.raise_for_status()
        d = r.json()
        for it in d.get("value", []):
            if conhecidos.get(str(it["Id"])) != it.get("Modified"):
                pendentes.append(it)
        url = d.get("odata.nextLink")
    # respostas a consultas primeiro, depois o resto; mais recentes antes
    pendentes.sort(key=lambda it: (classificar(it.get("Title") or "")[0] != "respostas-consultas",
                                   -(it["Id"])))
    gravados = 0
    for it in pendentes:  # 2) conteúdo integral dos novos/alterados
        if prazo.esgotado():
            break
        try:
            pausa()
            r = s.get(ITEM.format(id=it["Id"]), headers=JSON, timeout=120)
            r.raise_for_status()
            d = r.json()
            titulo = " ".join((d.get("Title") or f"Página {it['Id']}").split())
            html = d.get("PublishingPageContent") or ""
            if len(html) < 50:
                conhecidos[str(it["Id"])] = it.get("Modified")
                continue
            pasta, tipo = classificar(titulo)
            num = re.search(r"n?[º°.]?\s*([\d.]+)\s*(?:/|,?\s*de\s+)", titulo)
            numero = num.group(1).replace(".", "") if num else ""
            data = data_br(titulo) or data_extenso(titulo) or ""
            ano = data[:4] or (re.search(r"/(\d{4})\b", titulo).group(1) if re.search(r"/(\d{4})\b", titulo) else "sem-ano")
            pagina = "https://legislacao.fazenda.sp.gov.br" + (d.get("FileRef") or "")
            meta = {"titulo": titulo, "uf": "SP", "orgao": "Secretaria da Fazenda e Planejamento de SP",
                    "tipo": tipo, "numero": numero, "data": data,
                    "versao_texto": "texto do Portal de Legislação Tributária da SEFAZ-SP (pode estar consolidado)",
                    "fonte": pagina, "id_fonte": f"sefazsp-{it['Id']}", "modificado_na_fonte": d.get("Modified")}
            nome = f"{slug(titulo)[:90]}-sefazsp-{it['Id']}.md"
            gravados += gravar(f"estaduais/SP/sefaz/{pasta}/{ano}/{nome}",
                               montar_md(meta, titulo, html_para_md(html)), NOME,
                               {"orgao": "SEFAZ-SP", "tipo": tipo, "numero": numero, "data": data,
                                "titulo": titulo})
            conhecidos[str(it["Id"])] = it.get("Modified")
        except Exception as e:
            registrar_falha(NOME, it["Id"], repr(e))
        if gravados and gravados % 100 == 0:
            salvar_estado(NOME, {"modificado": conhecidos})
    salvar_estado(NOME, {"modificado": conhecidos})
    print(f"[sefaz_sp] {len(pendentes)} pendentes, {gravados} gravados; {len(conhecidos)} conhecidos")


if __name__ == "__main__":
    main()
