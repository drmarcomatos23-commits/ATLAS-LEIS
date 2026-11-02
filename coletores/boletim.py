"""Boletim semanal e alertas a partir de `_novidades/`.

- `python coletores/boletim.py semanal`  -> boletins/AAAA-Wnn.md (últimos 7 dias, por frente e tipo)
- `python coletores/boletim.py alertas`  -> _alertas/AAAA-MM-DD.md com o que bate nos temas
  prioritários do escritório (o workflow abre uma Issue, que o GitHub notifica por e-mail/app).
"""
from __future__ import annotations

import datetime as dt
import json
import re
import sys
from collections import defaultdict

from comum import NOVIDADES, RAIZ

PRIORIDADE = re.compile(
    r"ITBI|ITCMD|holding|integraliza[çc][ãa]o de capital|planejamento sucess|heran[çc]a|doa[çc][ãa]o|"
    r"invent[áa]rio|usufruto|sociedade limitada|registro de im[óo]veis|cart[óo]rio|tabeli|"
    r"incorpora[çc][ãa]o imobili|loca[çc][ãa]o|IPTU|Tema 1348|C[óo]digo Tribut[áa]rio|"
    r"IBS|CBS|reforma tribut|lucros e dividendos|ganho de capital|transa[çc][ãa]o tribut", re.I)
FRENTES = {"santos": "Santos", "sapl": "Baixada Santista (Câmaras)", "cnj": "CNJ / Corregedoria Nacional",
           "tjsp": "TJ-SP", "sefaz_sp": "SEFAZ-SP", "dou": "Diário Oficial da União"}


def ler(dias: int):
    hoje = dt.date.today()
    itens = []
    for i in range(dias):
        for p in sorted(NOVIDADES.glob(f"{hoje - dt.timedelta(days=i)}*.jsonl")):
            itens += [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
    return [n for n in itens if (RAIZ / n["arquivo"]).exists()]  # ignora o que foi depurado


def linha(n: dict) -> str:
    rotulo = n.get("titulo") or " ".join(x for x in [n.get("tipo", ""), n.get("numero", "") and f"nº {n['numero']}",
                                                     n.get("municipio", "")] if x)
    ementa = (n.get("ementa") or "").strip()
    link = f"https://github.com/drmarcomatos23-commits/ATLAS-LEIS/blob/main/{n['arquivo']}"
    return f"- [{rotulo}]({link})" + (f" — {ementa[:220]}" if ementa else "") + \
        (" *(alterada)*" if n.get("evento") == "alterada" else "")


def semanal():
    itens = ler(7)
    hoje = dt.date.today()
    ano, semana, _ = hoje.isocalendar()
    por = defaultdict(lambda: defaultdict(list))
    for n in itens:
        por[n.get("coletor", "outros")][n.get("tipo") or "Outros"].append(n)
    md = [f"# Boletim semanal ATLAS-LEIS — semana {semana}/{ano}", "",
          f"Período: {hoje - dt.timedelta(days=6):%d/%m/%Y} a {hoje:%d/%m/%Y}. "
          f"{len(itens)} normas novas ou alteradas.", ""]
    prio = [n for n in itens if PRIORIDADE.search(json.dumps(n, ensure_ascii=False))]
    if prio:
        md += ["## Destaques para o escritório", ""] + [linha(n) for n in prio[:60]] + [""]
    for col, tipos in por.items():
        md += [f"## {FRENTES.get(col, col)}", ""]
        for tipo, lst in sorted(tipos.items(), key=lambda x: -len(x[1])):
            md += [f"### {tipo} ({len(lst)})", ""] + [linha(n) for n in lst[:40]]
            if len(lst) > 40:
                md.append(f"- … e mais {len(lst) - 40}")
            md.append("")
    md.append("> Textos informativos, convertidos automaticamente. Confira sempre a fonte oficial antes de citar.")
    destino = RAIZ / "boletins" / f"{ano}-S{semana:02d}.md"
    destino.parent.mkdir(exist_ok=True)
    destino.write_text("\n".join(md), encoding="utf-8")
    print(destino)


def alertas():
    # a carga inicial de acervo antigo não é "novidade": só alerta o que tem data recente
    limite = (dt.date.today() - dt.timedelta(days=45)).isoformat()
    itens = [n for n in ler(1) if PRIORIDADE.search(json.dumps(n, ensure_ascii=False))
             and (n.get("data") or "") >= limite]
    if not itens:
        print("sem alertas")
        return
    destino = RAIZ / "_alertas" / f"{dt.date.today()}.md"
    destino.parent.mkdir(exist_ok=True)
    destino.write_text("\n".join([f"Novidades nos temas prioritários ({len(itens)}):", ""] +
                                 [linha(n) for n in itens[:50]]), encoding="utf-8")
    print(destino)


if __name__ == "__main__":
    {"semanal": semanal, "alertas": alertas}[sys.argv[1] if len(sys.argv) > 1 else "semanal"]()
