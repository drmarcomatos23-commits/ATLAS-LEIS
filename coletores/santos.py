"""Legislação do Município de Santos — portal LEGIS da Prefeitura (egov.santos.sp.gov.br/legis).

Cada norma tem endereço sequencial `documents/<id>/view`, que devolve o arquivo (em geral PDF).
O coletor percorre os IDs em ordem, retoma de onde parou e, depois de alcançar o fim,
passa a verificar só os IDs novos. Tipo, número e data são lidos do próprio texto.
"""
from __future__ import annotations

import re

from comum import (Pausa, Prazo, data_extenso, gravar, html_para_md, ler_estado, minutos_env,
                   montar_md, registrar_falha, salvar_estado, sessao, slug, texto_pdf)

BASE = "https://egov.santos.sp.gov.br/legis/documents/{id}/view"
NOME = "santos_legis"
FIM_APOS_VAZIOS = 300  # IDs seguidos inexistentes = fim da série

TIPOS = [
    (r"EMENDA\s+[ÀA]\s+LEI\s+ORG[ÂA]NICA", "emendas-lei-organica", "Emenda à Lei Orgânica"),
    (r"LEI\s+ORG[ÂA]NICA", "lei-organica", "Lei Orgânica"),
    (r"LEI\s+COMPLEMENTAR", "leis-complementares", "Lei Complementar"),
    (r"DECRETO\s+LEGISLATIVO", "decretos-legislativos", "Decreto Legislativo"),
    (r"DECRETO", "decretos", "Decreto"),
    (r"RESOLU[ÇC][ÃA]O", "resolucoes", "Resolução"),
    (r"PORTARIA", "portarias", "Portaria"),
    (r"LEI", "leis-ordinarias", "Lei Ordinária"),
]
EPIGRAFE = re.compile(
    r"^\s*(" + "|".join(t[0] for t in TIPOS) + r")\s*(?:MUNICIPAL\s*)?N\s*[.ºo°]*\s*([\d.]+)"
    r"(?:\s*/\s*(\d{2,4}))?(.{0,80})", re.I | re.M)


def classificar(texto: str):
    m = EPIGRAFE.search(texto[:4000])
    if not m:
        return None
    rotulo = re.sub(r"\s+", " ", m.group(1).upper())
    for padrao, pasta, tipo in TIPOS:
        if re.fullmatch(padrao, rotulo, re.I):
            break
    numero = m.group(2).replace(".", "")
    data = data_extenso(m.group(4) or "") or data_extenso(texto[:3000])
    ano = (data or "")[:4] or (m.group(3) if m.group(3) and len(m.group(3)) == 4 else "")
    ementa = ""
    depois = texto[m.end():m.end() + 1500].strip().split("\n\n")
    for bloco in depois[:4]:
        b = " ".join(bloco.split())
        if len(b) > 25 and b.upper() == b and not b.startswith(("ROG", "PAULO", "JO")):
            ementa = b
            break
    return {"pasta": pasta, "tipo": tipo, "numero": numero, "data": data, "ano": ano or "sem-ano",
            "ementa": ementa, "epigrafe": " ".join(m.group(0).split())}


def baixar(s, pausa, i):
    pausa()
    r = s.get(BASE.format(id=i), timeout=90, allow_redirects=True)
    if r.status_code in (404, 410) or not r.content:
        return None
    r.raise_for_status()
    ct = r.headers.get("content-type", "")
    if r.content[:4] == b"%PDF" or "pdf" in ct:
        return texto_pdf(r.content)
    if "html" in ct:
        if re.search(r"n[ãa]o encontrad|not found", r.text[:3000], re.I):
            return None
        return html_para_md(r.text)
    return ""


def main():
    est = ler_estado(NOME)
    proximo, vazios = est.get("proximo", 1), est.get("vazios", 0)
    s, pausa, prazo = sessao(), Pausa(1.2), Prazo(minutos_env(40))
    gravados = 0
    while not prazo.esgotado() and vazios < FIM_APOS_VAZIOS:
        try:
            texto = baixar(s, pausa, proximo)
        except Exception as e:
            registrar_falha(NOME, proximo, repr(e))
            texto = None
        if texto is None:
            vazios += 1
        else:
            vazios = 0
            info = classificar(texto) or {"pasta": "_nao-classificados", "tipo": "Não classificado",
                                          "numero": "", "data": "", "ano": "sem-ano", "ementa": "",
                                          "epigrafe": f"Documento {proximo} do LEGIS Santos"}
            titulo = info["epigrafe"].title() if info["numero"] else info["epigrafe"]
            meta = {"titulo": titulo, "uf": "SP", "municipio": "Santos", "tipo": info["tipo"],
                    "numero": info["numero"], "data": info["data"], "ementa": info["ementa"],
                    "versao_texto": "arquivo publicado no LEGIS (Prefeitura de Santos); conferir compilação",
                    "fonte": BASE.format(id=proximo), "id_fonte": f"santos-legis-{proximo}"}
            nome_arq = (f"{info['pasta']}-{slug(info['numero'])}-{info['ano']}-legis-{proximo}.md"
                        if info["numero"] else f"legis-{proximo}.md")
            caminho = f"municipais/SP/santos/{info['pasta']}/{info['ano']}/{nome_arq}"
            gravados += gravar(caminho, montar_md(meta, titulo, texto), "santos",
                               {"municipio": "Santos", "tipo": info["tipo"], "numero": info["numero"],
                                "data": info["data"], "ementa": info["ementa"][:300]})
        proximo += 1
        if proximo % 50 == 0:
            salvar_estado(NOME, {"proximo": proximo, "vazios": vazios})
    if vazios >= FIM_APOS_VAZIOS:  # chegou ao fim: volta para o último ID existente e vigia os novos
        proximo, vazios = proximo - FIM_APOS_VAZIOS, 0
    salvar_estado(NOME, {"proximo": proximo, "vazios": vazios})
    print(f"[santos] {gravados} documentos gravados; próximo ID {proximo}")


if __name__ == "__main__":
    main()
