"""Legislação municipal das Câmaras que usam o SAPL (Interlegis), pela API REST pública.

API: /api/norma/tiponormajuridica/  e  /api/norma/normajuridica/?tipo=<id>&page_size=100&page=<n>
Saída: municipais/SP/<municipio>/<pasta-do-tipo>/<ano>/<pasta>-<numero>-<ano>-sapl-<id>.md
(mesmo padrão de nomes do ctresb/leis, para os dois acervos se somarem sem colisão).

Câmaras configuradas em `fontes.yml` (chave `sapl`). Municípios que o ctresb/leis já cobre
ficam marcados `upstream: true` e são pulados.
"""
from __future__ import annotations

import sys

import yaml

from comum import (RAIZ, Pausa, Prazo, gravar, ler_estado, minutos_env, montar_md, registrar_falha,
                   salvar_estado, sessao, slug, texto_pdf)

PASTAS = [  # (trecho da descrição do tipo no SAPL, pasta canônica, tipo canônico)
    ("emenda", "emendas-lei-organica", "Emenda à Lei Orgânica"),
    ("organica", "lei-organica", "Lei Orgânica"),
    ("complementar", "leis-complementares", "Lei Complementar"),
    ("decreto legislativo", "decretos-legislativos", "Decreto Legislativo"),
    ("decreto", "decretos", "Decreto"),
    ("resolu", "resolucoes", "Resolução"),
    ("lei", "leis-ordinarias", "Lei Ordinária"),
]


def canonico(descricao: str):
    d = slug(descricao).replace("-", " ")
    for trecho, pasta, tipo in PASTAS:
        if trecho in d:
            return pasta, tipo
    return slug(descricao), descricao


def api(s, pausa, base, caminho):
    pausa()
    r = s.get(f"{base}/api/{caminho}", timeout=60, headers={"Accept": "application/json"})
    r.raise_for_status()
    return r.json()


def coletar_camara(s, cfg, prazo):
    base = cfg["url"].rstrip("/")
    mun = cfg["municipio"]
    nome = f"sapl_{slug(mun)}"
    est = ler_estado(nome)
    vistos = set(est.get("ids", []))
    pausa = Pausa(cfg.get("pausa", 1.0))
    tipos, pag = {}, 1
    while True:
        d = api(s, pausa, base, f"norma/tiponormajuridica/?page_size=100&page={pag}")
        for t in d["results"]:
            tipos[t["id"]] = t.get("descricao") or t.get("sigla") or str(t["id"])
        if not d.get("pagination", {}).get("next_page"):
            break
        pag += 1
    novos = 0
    for tid, desc in tipos.items():
        pasta, tipo = canonico(desc)
        pag = 1
        while not prazo.esgotado():
            d = api(s, pausa, base, f"norma/normajuridica/?tipo={tid}&page_size=100&page={pag}")
            for n in d["results"]:
                if n["id"] in vistos or prazo.esgotado():
                    continue
                try:
                    novos += salvar_norma(s, pausa, base, cfg, n, pasta, tipo, desc)
                    vistos.add(n["id"])
                except Exception as e:
                    registrar_falha(nome, n["id"], repr(e))
            if not d.get("pagination", {}).get("next_page"):
                break
            pag += 1
        salvar_estado(nome, {"ids": sorted(vistos)})
    print(f"[sapl] {mun}: {len(vistos)} normas conhecidas, {novos} gravadas nesta execução")


def salvar_norma(s, pausa, base, cfg, n, pasta, tipo, desc) -> int:
    ano = str(n.get("ano") or (n.get("data") or "")[:4] or "sem-ano")
    numero = str(n.get("numero") or "sn").strip()
    data = n.get("data") or ""
    titulo = f"{desc} nº {numero}/{ano}" if numero != "sn" else f"{desc} de {ano}"
    texto, arquivo = "", (n.get("texto_integral") or "").replace("http://", "https://")
    if arquivo:
        pausa()
        r = s.get(arquivo, timeout=120)
        if r.ok and (arquivo.lower().endswith(".pdf") or r.content[:4] == b"%PDF"):
            texto = texto_pdf(r.content)
        elif r.ok and "html" in r.headers.get("content-type", ""):
            from comum import html_para_md
            texto = html_para_md(r.text)
    if not texto.strip():
        texto = "> Texto integral não disponível em camada de texto na fonte (PDF digitalizado ou ausente). " \
                "Consulte o arquivo indicado em `arquivo`."
    meta = {
        "titulo": titulo, "uf": cfg.get("uf", "SP"), "municipio": cfg["municipio"], "tipo": tipo,
        "tipo_na_fonte": desc, "numero": numero, "data": data, "ementa": (n.get("ementa") or "").strip(),
        "versao_texto": "texto integral anexado no SAPL municipal",
        "fonte": f"{base}/norma/{n['id']}", "arquivo": arquivo, "id_fonte": f"sapl-{n['id']}",
    }
    caminho = (f"municipais/{cfg.get('uf', 'SP')}/{slug(cfg['municipio'])}/{pasta}/{ano}/"
               f"{pasta}-{slug(numero)}-{ano}-sapl-{n['id']}.md")
    ok = gravar(caminho, montar_md(meta, titulo, texto), "sapl",
                {"municipio": cfg["municipio"], "tipo": tipo, "numero": numero, "data": data,
                 "ementa": meta["ementa"][:300]})
    return int(ok)


def main(filtro=None):
    fontes = yaml.safe_load((RAIZ / "fontes.yml").read_text(encoding="utf-8"))
    s = sessao()
    prazo = Prazo(minutos_env(40))
    for cfg in fontes.get("sapl", []):
        if cfg.get("upstream") or not cfg.get("ativo", True):
            continue
        if filtro and slug(cfg["municipio"]) not in filtro:
            continue
        if prazo.esgotado():
            break
        try:
            coletar_camara(s, cfg, prazo)
        except Exception as e:
            print(f"[sapl] {cfg['municipio']}: falhou — {e!r}")
            registrar_falha("sapl", cfg["municipio"], repr(e))


if __name__ == "__main__":
    main(set(sys.argv[1:]) or None)
