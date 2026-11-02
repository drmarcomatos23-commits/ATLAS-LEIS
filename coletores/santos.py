"""Legislação do Município de Santos — portal LEGIS da Prefeitura (egov.santos.sp.gov.br/legis).

Cada norma tem endereço sequencial `documents/<id>/view`, que devolve o arquivo (em geral PDF).
O coletor percorre os IDs em ordem, retoma de onde parou e, depois de alcançar o fim,
passa a verificar só os IDs novos. Tipo, número e data são lidos do próprio texto.
"""
from __future__ import annotations

import re

from comum import (Pausa, Prazo, data_br, data_extenso, gravar, ler_estado, minutos_env, montar_md,
                   registrar_falha, salvar_estado, sessao, slug, texto_arquivo)

BASE = "https://egov.santos.sp.gov.br/legis/documents/{id}/view"
NOME = "santos_legis"
FIM_APOS_VAZIOS = 400  # IDs seguidos inexistentes = fim da série

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


FICHA = "https://egov.santos.sp.gov.br/legis/documents/{id}"


def ficha(s, pausa, i):
    """Metadados da página do documento: título, ementa, publicação, etiquetas e nome do arquivo."""
    from bs4 import BeautifulSoup
    pausa()
    r = s.get(FICHA.format(id=i), timeout=60)
    if r.status_code in (404, 410):
        return None
    r.raise_for_status()
    sopa = BeautifulSoup(r.text, "html.parser")
    h1 = sopa.find("h1")
    if not h1:
        return None
    t = lambda sel: (sopa.select_one(sel).get_text(" ", strip=True) if sopa.select_one(sel) else "")
    arquivo = ""
    item = sopa.select_one("ul.list-group li div")
    if item:
        arquivo = item.find(string=True, recursive=False) or ""
    return {"h1": " ".join(h1.get_text(" ").split()), "ementa": t("p.descricao"), "info": t("p.info"),
            "tags": [b.get_text(strip=True) for b in sopa.select("p.tags .badge")],
            "arquivo": arquivo.strip()}


def ler_cabecalho(h1: str):
    """'2009 » Lei Complementar n.º 667, de 29 de dezembro' -> tipo, número, data."""
    ano, _, resto = h1.partition("»")
    ano = ano.strip() if re.fullmatch(r"\d{4}", ano.strip()) else ""
    resto = resto.strip() or h1
    m = re.match(r"(.+?)\s+n\.?\s*[ºo°]*\s*([\d.]+)(?:\s*,?\s*de\s+(.+))?$", resto, re.I)
    rotulo, numero, quando = (m.group(1), m.group(2).replace(".", ""), m.group(3) or "") if m else (resto, "", "")
    pasta, tipo = "outros", rotulo.strip()
    for padrao, p_, t_ in TIPOS:
        if re.fullmatch(padrao, rotulo.strip().upper()):
            pasta, tipo = p_, t_
            break
    data = data_extenso(f"{quando} de {ano}") if quando and ano else None
    return {"pasta": pasta if numero else "consolidacoes-e-outros", "tipo": tipo, "numero": numero,
            "data": data or "", "ano": ano or "sem-ano", "titulo": resto + (f" de {ano}" if ano and ano not in resto else "")}


def main():
    est = ler_estado(NOME)
    proximo, vazios = est.get("proximo", 1), est.get("vazios", 0)
    s, pausa, prazo = sessao(), Pausa(1.0), Prazo(minutos_env(40))
    gravados = 0
    while not prazo.esgotado() and vazios < FIM_APOS_VAZIOS:
        try:
            f = ficha(s, pausa, proximo)
            if f is None:
                vazios += 1
            else:
                vazios = 0
                c = ler_cabecalho(f["h1"])
                pausa()
                r = s.get(BASE.format(id=proximo), timeout=120)
                texto = texto_arquivo(r.content, f["arquivo"], r.headers.get("content-type", "")) if r.ok else ""
                if not texto.strip():
                    texto = "> Arquivo sem camada de texto (provavelmente digitalizado). Consulte a `fonte`."
                pub = data_br(f["info"]) or ""
                meta = {"titulo": c["titulo"], "uf": "SP", "municipio": "Santos", "tipo": c["tipo"],
                        "numero": c["numero"], "data": c["data"], "ementa": f["ementa"],
                        "versao_texto": "arquivo publicado no LEGIS (Prefeitura de Santos); conferir a compilação",
                        "publicacao": f["info"], "data_publicacao": pub, "fonte": FICHA.format(id=proximo),
                        "arquivo": BASE.format(id=proximo), "id_fonte": f"santos-legis-{proximo}",
                        "etiquetas": ", ".join(f["tags"])}
                nome = (f"{c['pasta']}-{c['numero']}-{c['ano']}-legis-{proximo}.md" if c["numero"]
                        else f"{slug(c['titulo'])[:80]}-legis-{proximo}.md")
                caminho = f"municipais/SP/santos/{c['pasta']}/{c['ano']}/{nome}"
                gravados += gravar(caminho, montar_md(meta, c["titulo"], texto), "santos",
                                   {"municipio": "Santos", "tipo": c["tipo"], "numero": c["numero"],
                                    "data": c["data"], "ementa": f["ementa"][:300]})
        except Exception as e:
            registrar_falha(NOME, proximo, repr(e))
        proximo += 1
        if proximo % 50 == 0:
            salvar_estado(NOME, {"proximo": proximo, "vazios": vazios})
    if vazios >= FIM_APOS_VAZIOS:  # chegou ao fim: volta e passa a vigiar os IDs novos
        proximo, vazios = proximo - FIM_APOS_VAZIOS, 0
    salvar_estado(NOME, {"proximo": proximo, "vazios": vazios})
    print(f"[santos] {gravados} documentos gravados; próximo ID {proximo}")


if __name__ == "__main__":
    main()
