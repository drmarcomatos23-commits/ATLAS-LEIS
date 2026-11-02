"""Atos normativos do CNJ e da Corregedoria Nacional (atos.cnj.jus.br).

Provimentos (inclusive o Código Nacional de Normas – Foro Extrajudicial, base dos cartórios),
resoluções, recomendações, instruções normativas e portarias. Endereço sequencial
`/atos/detalhar/<id>`; o coletor percorre os IDs e depois vigia os novos.
Para cada ato guarda o **texto compilado** quando houver (senão o original).
"""
from __future__ import annotations

import re

from bs4 import BeautifulSoup

from comum import (Pausa, Prazo, data_br, gravar, html_para_md, ler_estado, minutos_env,
                   montar_md, registrar_falha, salvar_estado, sessao, slug)

BASE = "https://atos.cnj.jus.br/atos/detalhar/{id}"
NOME = "cnj_atos"
FIM_APOS_VAZIOS = 150
ROTULOS = ("Identificação", "Apelido", "Temas", "Ementa", "Situação", "Situação STF", "Origem",
           "Fonte", "Alteração", "Legislação Correlata")


def campos(sopa: BeautifulSoup) -> dict:
    """Lê pares rótulo → valor da ficha, tolerando tabela, <dl> ou blocos soltos."""
    linhas = [l.strip() for l in sopa.get_text("\n").split("\n") if l.strip()]
    out = {}
    for i, l in enumerate(linhas):
        if l in ROTULOS and i + 1 < len(linhas) and linhas[i + 1] not in ROTULOS:
            out.setdefault(l, linhas[i + 1])
    return out


def texto_principal(sopa: BeautifulSoup) -> str:
    for seletor in ("#textoCompilado", "#texto-compilado", ".texto-compilado", "#textoOriginal",
                    "#texto-original", ".texto-original", "#conteudo", "main", "article"):
        el = sopa.select_one(seletor)
        if el and len(el.get_text(strip=True)) > 200:
            return html_para_md(str(el))
    return html_para_md(str(sopa.body or sopa))


def main():
    est = ler_estado(NOME)
    proximo, vazios = est.get("proximo", 1), est.get("vazios", 0)
    s, pausa, prazo = sessao(), Pausa(1.0), Prazo(minutos_env(30))
    gravados = 0
    while not prazo.esgotado() and vazios < FIM_APOS_VAZIOS:
        try:
            pausa()
            r = s.get(BASE.format(id=proximo), timeout=60)
            if r.status_code == 404 or "Identificação" not in r.text:
                vazios += 1
            else:
                vazios = 0
                sopa = BeautifulSoup(r.text, "html.parser")
                f = campos(sopa)
                ident = f.get("Identificação", f"Ato CNJ {proximo}")
                m = re.match(r"(.+?)\s+N[ºo°.]*\s*([\d.]+)\s+de\s+(\d{1,2}/\d{1,2}/\d{4})", ident, re.I)
                tipo = (m.group(1) if m else ident.split(" N")[0]).strip()
                numero = m.group(2).replace(".", "") if m else ""
                data = data_br(m.group(3)) if m else data_br(ident)
                ano = (data or "")[:4] or "sem-ano"
                situacao = f.get("Situação", "")
                meta = {"titulo": ident, "orgao": f"CNJ – {f.get('Origem', '')}".strip(" –"),
                        "tipo": tipo, "numero": numero, "data": data, "ementa": f.get("Ementa", ""),
                        "situacao": situacao, "revogada": bool(re.search(r"revogad", situacao, re.I)),
                        "versao_texto": "texto do portal Atos do CNJ (compilado quando disponível)",
                        "publicacao": f.get("Fonte", ""), "fonte": BASE.format(id=proximo),
                        "id_fonte": f"cnj-{proximo}"}
                pasta = slug(tipo) + ("s" if not slug(tipo).endswith("s") else "")
                caminho = (f"reguladores/cnj/{pasta}/{ano}/{slug(tipo)}-{numero or 'sn'}-{data or ano}"
                           f"-cnj-{proximo}.md")
                gravados += gravar(caminho, montar_md(meta, ident, texto_principal(sopa)), "cnj",
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
