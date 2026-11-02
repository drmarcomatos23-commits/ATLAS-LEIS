"""Sondagem das fontes oficiais: testa endereços candidatos e registra o que cada um devolve.

Roda no GitHub Actions (que alcança os sites públicos) e grava `_relatorios/sondagem.md`,
usado para calibrar os coletores. Não grava nada no acervo.
"""
from __future__ import annotations

import json
import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from comum import RAIZ, sessao

BAIXADA = ["santos", "praiagrande", "guaruja", "cubatao", "saovicente", "bertioga", "mongagua",
           "itanhaem", "peruibe"]

ALVOS = [
    # Santos
    "https://egov.santos.sp.gov.br/legis/",
    "https://egov.santos.sp.gov.br/legis/documents",
    "https://egov.santos.sp.gov.br/legis/documents/2864",
    "https://egov.santos.sp.gov.br/legis/documents/2864/view",
    "https://egov.santos.sp.gov.br/legis/documents/1/view",
    "https://egov.santos.sp.gov.br/legis/api/documents",
    "https://diariooficial.santos.sp.gov.br/edicoes/inicio/download/2026-10-30",
    "https://www.santos.sp.gov.br/?q=portal/legislacao",
    "https://www.camarasantos.sp.gov.br/",
    # Baixada: portais das prefeituras
    "https://www.praiagrande.sp.gov.br/",
    "https://www.guaruja.sp.gov.br/legislacao/",
    "https://www.cubatao.sp.gov.br/legislacao/",
    "https://www.bertioga.sp.gov.br/legislacao/",
    "https://www.mongagua.sp.gov.br/legislacao",
    "https://www.itanhaem.sp.gov.br/legislacao-municipal/",
    "https://www.peruibe.sp.gov.br/legislacao",
    # Tributário administrativo
    "https://legislacao.fazenda.sp.gov.br/",
    "https://legislacao.fazenda.sp.gov.br/_api/web/lists?$select=Title,ItemCount",
    "https://legislacao.fazenda.sp.gov.br/Paginas/RespostasConsultas.aspx",
    "https://normas.receita.fazenda.gov.br/sijut2consulta/consulta.action",
    "https://carf.economia.gov.br/jurisprudencia/sumulas-carf",
    "https://www.gov.br/carf/pt-br/assuntos/sumulas",
    "https://www.in.gov.br/leiturajornal?secao=do1&data=30-10-2026",
    # Cartórios e registro
    "https://atos.cnj.jus.br/atos/detalhar/5243",
    "https://atos.cnj.jus.br/atos/detalhar/6300",
    "https://atos.cnj.jus.br/atos/pesquisar",
    "https://www.tjsp.jus.br/Corregedoria/Comunicados/NormasServico",
    "https://www.tjsp.jus.br/Corregedoria",
    "https://www.gov.br/empresas-e-negocios/pt-br/drei/legislacao",
    "https://www.institucional.jucesp.sp.gov.br/",
    # TJ-SP
    "https://www.tjsp.jus.br/Jurisprudencia/Sumulas",
    "https://www.tjsp.jus.br/Download/Portal/Jurisprudencia/Sumulas.pdf",
    "https://www.tjsp.jus.br/NugepNac/Irdr",
    "https://esaj.tjsp.jus.br/cjsg/consultaCompleta.do",
    # Precedentes (BNP/CNJ, usado pelo ctresb/leis)
    "https://pangeabnp.pdpj.jus.br/api/v1/precedentes?orgaos=TJSP&tipos=IRDR&pagina=1",
]
# Rodada 2: páginas guardadas na íntegra (_relatorios/bruto/) para calibrar os analisadores
BRUTOS = [
    "https://legislacao.fazenda.sp.gov.br/_api/web/lists/getbytitle('P%C3%A1ginas')/items?$top=3&$orderby=Modified%20desc",
    "https://legislacao.fazenda.sp.gov.br/_api/web/lists/getbytitle('P%C3%A1ginas')/items?$top=3&$filter=substringof('RC',FileLeafRef)",
    "https://legislacao.fazenda.sp.gov.br/_api/web/lists/getbytitle('RCTema')/items?$top=5",
    "https://www.in.gov.br/leiturajornal?secao=do1&data=27-10-2026",
    "https://www.tjsp.jus.br/Enunciados",
]
ALVOS = BRUTOS


def sondar(s, url):
    out = {"url": url}
    try:
        hdr = {"Accept": "application/json;odata=nometadata"} if "/_api/" in url else {}
        r = s.get(url, timeout=45, allow_redirects=True, headers=hdr)
        if url in BRUTOS:
            b = RAIZ / "_relatorios" / "bruto"
            b.mkdir(parents=True, exist_ok=True)
            nome = re.sub(r"[^a-zA-Z0-9]+", "_", url.split("//", 1)[1])[:120]
            (b / nome).write_bytes(r.content[:2_000_000])
        out.update(status=r.status_code, final=r.url, tipo=r.headers.get("content-type", ""),
                   bytes=len(r.content))
        if r.content[:4] == b"%PDF":
            out["amostra"] = "[PDF]"
        elif "json" in out["tipo"]:
            out["amostra"] = r.text[:1500]
        else:
            sopa = BeautifulSoup(r.text, "html.parser")
            out["titulo"] = (sopa.title.get_text(strip=True) if sopa.title else "")[:150]
            texto = re.sub(r"\s+", " ", sopa.get_text(" "))
            out["amostra"] = texto[:900]
            links = []
            for a in sopa.find_all("a", href=True):
                h = urljoin(r.url, a["href"])
                if h.startswith("http") and h not in links:
                    links.append(h)
            out["links"] = links[:60]
            out["forms"] = [{"action": f.get("action"), "campos": [i.get("name") for i in f.find_all(["input", "select"]) if i.get("name")][:25]}
                            for f in sopa.find_all("form")][:5]
    except Exception as e:
        out["erro"] = repr(e)[:300]
    return out


def main():
    s = sessao()
    res = [sondar(s, u) for u in ALVOS]
    d = RAIZ / "_relatorios"
    d.mkdir(exist_ok=True)
    (d / "sondagem.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    md = ["# Sondagem das fontes", ""]
    for r in res:
        md.append(f"## {r['url']}")
        md.append(f"- status: {r.get('status')} · tipo: {r.get('tipo')} · bytes: {r.get('bytes')} · final: {r.get('final')}")
        if r.get("erro"):
            md.append(f"- ERRO: {r['erro']}")
        if r.get("titulo"):
            md.append(f"- título: {r['titulo']}")
        if r.get("amostra"):
            md.append(f"- amostra: {r['amostra'][:600]}")
        md.append("")
    (d / "sondagem.md").write_text("\n".join(md), encoding="utf-8")
    for r in res:
        print(r.get("status"), r.get("bytes"), r["url"], r.get("erro", "")[:80])


if __name__ == "__main__":
    main()
