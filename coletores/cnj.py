"""Atos normativos do CNJ e da Corregedoria Nacional (atos.cnj.jus.br).

Provimentos (inclusive o Código Nacional de Normas – Foro Extrajudicial, base dos cartórios),
resoluções, recomendações, instruções normativas e portarias. Endereço sequencial
`/atos/detalhar/<id>`; o coletor percorre os IDs e depois vigia os novos.
Para cada ato guarda o **texto compilado** quando houver (senão o original).
"""
from __future__ import annotations

import re

from bs4 import BeautifulSoup

from comum import (Pausa, Prazo, data_br, gravar, html_para_md, texto_arquivo, ler_estado, minutos_env,
                   montar_md, registrar_falha, salvar_estado, sessao, slug)

BASE = "https://atos.cnj.jus.br/atos/detalhar/{id}"
NOME = "cnj_atos"
FIM_APOS_VAZIOS = 150


def campos(sopa: BeautifulSoup) -> dict:
    """Pares rótulo → elemento da ficha (div.identificacao / div.dsc_conteudo)."""
    out = {}
    for rot in sopa.select("div.identificacao"):
        val = rot.find_next_sibling("div", class_="dsc_conteudo")
        if val is not None:
            out.setdefault(rot.get_text(" ", strip=True), val)
    return out


def txt(el) -> str:
    return " ".join(el.get_text(" ").split()) if el is not None else ""


def texto_principal(f: dict) -> tuple[str, str]:
    """(texto em Markdown, link do PDF original/compilado)."""
    el = f.get("Texto")
    if el is None:
        return "", ""
    pdfs = [a for a in el.find_all("a", href=True) if a["href"].lower().endswith(".pdf")]
    compilado = next((a for a in el.find_all("a", href=True) if "Compilado" in a.get_text()
                      and a["href"].lower().endswith(".pdf")), None)
    link = (compilado or (pdfs[0] if pdfs else None))
    link = ("https://atos.cnj.jus.br/files/" + link["href"].split("files/", 1)[1]) if link else ""
    corpo = el.find("div", class_="col-12")
    return (html_para_md(str(corpo)) if corpo else ""), link


def main():
    est = ler_estado(NOME)
    proximo, vazios = est.get("proximo", 1), est.get("vazios", 0)
    s, pausa, prazo = sessao(retry_500=False), Pausa(1.0), Prazo(minutos_env(30))
    gravados = 0
    while not prazo.esgotado() and vazios < FIM_APOS_VAZIOS:
        try:
            pausa()
            r = s.get(BASE.format(id=proximo), timeout=60)
            if r.status_code in (404, 500) or "identificacao" not in r.text:
                vazios += 1
            else:
                vazios = 0
                sopa = BeautifulSoup(r.text, "html.parser")
                f = campos(sopa)
                ident = txt(f.get("Identificação")) or f"Ato CNJ {proximo}"
                m = re.match(r"(.+?)\s+N[ºo°.]*\s*([\d.]+)\s+de\s+(\d{1,2}/\d{1,2}/\d{4})", ident, re.I)
                tipo = (m.group(1) if m else ident.split(" N")[0]).strip()
                numero = m.group(2).replace(".", "") if m else ""
                data = data_br(m.group(3)) if m else data_br(ident)
                ano = (data or "")[:4] or "sem-ano"
                situacao = txt(f.get("Situação"))
                meta = {"titulo": ident, "orgao": f"CNJ – {txt(f.get('Origem'))}".strip(" –"),
                        "tipo": tipo, "numero": numero, "data": data, "ementa": txt(f.get("Ementa")),
                        "situacao": situacao, "revogada": bool(re.search(r"revogad", situacao, re.I)),
                        "versao_texto": "texto do portal Atos do CNJ (compilado quando disponível)",
                        "publicacao": txt(f.get("Fonte")), "fonte": BASE.format(id=proximo),
                        "alteracao": txt(f.get("Alteração")), "apelido": txt(f.get("Apelido")).strip("- "),
                        "id_fonte": f"cnj-{proximo}"}
                pasta = slug(tipo) + ("s" if not slug(tipo).endswith("s") else "")
                caminho = (f"reguladores/cnj/{pasta}/{ano}/{slug(tipo)}-{numero or 'sn'}-{data or ano}"
                           f"-cnj-{proximo}.md")
                corpo, pdf = texto_principal(f)
                meta["arquivo"] = pdf
                if len(corpo) < 300 and pdf:  # texto só no PDF
                    pausa()
                    rp = s.get(pdf, timeout=120)
                    if rp.ok:
                        corpo = texto_arquivo(rp.content, pdf, rp.headers.get("content-type", ""))
                gravados += gravar(caminho, montar_md(meta, ident, corpo), "cnj",
                                   {"orgao": meta["orgao"], "tipo": tipo, "numero": numero, "data": data,
                                    "ementa": meta["ementa"][:300], "situacao": situacao})
        except Exception as e:
            registrar_falha(NOME, proximo, repr(e))
        proximo += 1
        if proximo % 50 == 0:
            salvar_estado(NOME, {"proximo": proximo, "vazios": vazios})
    if vazios >= FIM_APOS_VAZIOS:
        proximo, vazios = proximo - FIM_APOS_VAZIOS, 0
    salvar_estado(NOME, {"proximo": proximo, "vazios": vazios})
    print(f"[cnj] {gravados} atos gravados; próximo ID {proximo}")


if __name__ == "__main__":
    main()
