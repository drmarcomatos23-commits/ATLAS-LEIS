"""Vigia diária do Diário Oficial da União (Seção 1) — atos novos nas áreas do escritório.

A página "Leitura do Jornal" traz, embutido, o índice JSON de todos os atos do dia. O coletor
filtra pelos órgãos e temas de interesse (tributário, societário/registro, sucessões,
imobiliário, cartórios, reforma tributária), baixa o texto integral dos selecionados e grava em
`dou/AAAA/MM/DD/`. É a fonte mais rápida de novidade federal: o ctresb/leis incorpora depois.
"""
from __future__ import annotations

import datetime as dt
import json
import re

from bs4 import BeautifulSoup

from comum import (Pausa, data_br, gravar, html_para_md, ler_estado, montar_md, registrar_falha,
                   salvar_estado, sessao, slug)

NOME = "dou"
INDICE = "https://www.in.gov.br/leiturajornal?secao={secao}&data={data}"
ATO = "https://www.in.gov.br/web/dou/-/{url}"

ORGAOS = re.compile(
    r"Presid[êe]ncia da Rep[úu]blica|Atos do Poder Legislativo|Congresso Nacional|Receita Federal|"
    r"Conselho Administrativo de Recursos Fiscais|Procuradoria-Geral da Fazenda|Comit[êe] Gestor|"
    r"Registro Empresarial|DREI|Conselho Nacional de Justi[çc]a|Comiss[ãa]o de Valores Mobili[áa]rios|"
    r"Conselho Monet[áa]rio|Banco Central|Conselho Nacional de Pol[íi]tica Fazend[áa]ria|CONFAZ|"
    r"Minist[ée]rio da Fazenda/Gabinete|Secretaria do Patrim[ôo]nio da Uni[ãa]o|Supremo Tribunal|"
    r"Superior Tribunal de Justi[çc]a", re.I)
TIPOS = re.compile(r"^(Lei|Lei Complementar|Decreto|Medida Provis[óo]ria|Emenda Constitucional|"
                   r"Instru[çc][ãa]o Normativa|Solu[çc][ãa]o de Consulta|Ato Declarat[óo]rio|"
                   r"Parecer Normativo|Resolu[çc][ãa]o|Portaria Normativa|S[úu]mula|Conv[êe]nio|"
                   r"Ajuste|Ato Normativo|Provimento|Ac[óo]rd[ãa]o)", re.I)
TEMAS = re.compile(
    r"ITBI|ITCMD|holding|sociedade limitada|sociedades? an[ôo]nima|registro empresarial|junta comercial|"
    r"integraliza[çc][ãa]o|ganho de capital|lucro presumido|lucro real|distribui[çc][ãa]o de lucros|"
    r"dividendos|juros sobre (o )?capital|heran[çc]a|sucess[ãa]o|doa[çc][ãa]o|invent[áa]rio|"
    r"registro de im[óo]veis|registros p[úu]blicos|cart[óo]rio|notari|incorpora[çc][ãa]o imobili|"
    r"IBS|CBS|Imposto Seletivo|reforma tribut|Simples Nacional|transa[çc][ãa]o tribut|"
    r"planejamento tribut|IRPF|IRPJ|CSLL|PIS|Cofins|patrim[ôo]nio de afeta", re.I)


def relevante(a: dict) -> bool:
    hier, tipo = a.get("hierarchyStr", ""), a.get("artType", "")
    texto = " ".join(str(a.get(k, "")) for k in ("title", "titulo", "content", "subTitulo"))
    if TIPOS.match(tipo or "") and ORGAOS.search(hier):
        return True
    return bool(TEMAS.search(texto)) and bool(TIPOS.match(tipo or ""))


def atos_do_dia(s, pausa, data: dt.date):
    pausa()
    r = s.get(INDICE.format(secao="do1", data=data.strftime("%d-%m-%Y")), timeout=90)
    r.raise_for_status()
    m = re.search(r'<script[^>]*id="params"[^>]*>(.*?)</script>', r.text, re.S)
    return json.loads(m.group(1)).get("jsonArray", []) if m else []


def texto_ato(s, pausa, url_title: str):
    pausa()
    r = s.get(ATO.format(url=url_title), timeout=90)
    r.raise_for_status()
    sopa = BeautifulSoup(r.text, "html.parser")
    el = sopa.select_one("div.texto-dou") or sopa.select_one("article") or sopa.body
    return html_para_md(str(el))


def main(dias_atras: int = 7):
    est = ler_estado(NOME)
    hoje = dt.date.today()
    inicio = dt.date.fromisoformat(est["ultimo"]) + dt.timedelta(days=1) if est.get("ultimo") \
        else hoje - dt.timedelta(days=dias_atras)
    s, pausa = sessao(), Pausa(1.0)
    dia, total = inicio, 0
    while dia <= hoje:
        try:
            atos = atos_do_dia(s, pausa, dia)
        except Exception as e:
            registrar_falha(NOME, dia.isoformat(), repr(e))
            break  # tenta de novo amanhã a partir deste dia
        escolhidos = [a for a in atos if relevante(a)]
        for a in escolhidos:
            try:
                titulo = " ".join((a.get("title") or a.get("titulo") or "Ato do DOU").split())
                corpo = texto_ato(s, pausa, a["urlTitle"])
                meta = {"titulo": titulo, "orgao": a.get("hierarchyStr", ""), "tipo": a.get("artType", ""),
                        "data_publicacao": data_br(a.get("pubDate", "")) or dia.isoformat(),
                        "ementa": " ".join(str(a.get("content", "")).split())[:600],
                        "publicacao": f"DOU Seção 1, ed. {a.get('editionNumber', '')}, p. {a.get('numberPage', '')}",
                        "versao_texto": "texto publicado no DOU (original)",
                        "fonte": ATO.format(url=a["urlTitle"]), "id_fonte": f"dou-{a.get('urlTitle')}"}
                caminho = f"dou/{dia:%Y/%m/%d}/{slug(a.get('artType', 'ato'))}-{slug(a['urlTitle'])[:90]}.md"
                total += gravar(caminho, montar_md(meta, titulo, corpo), NOME,
                                {"orgao": meta["orgao"], "tipo": meta["tipo"], "titulo": titulo,
                                 "data": meta["data_publicacao"], "ementa": meta["ementa"][:300]})
            except Exception as e:
                registrar_falha(NOME, a.get("urlTitle"), repr(e))
        print(f"[dou] {dia}: {len(atos)} atos, {len(escolhidos)} relevantes")
        if atos or dia < hoje:  # edição de hoje ainda não saiu: refaz amanhã
            salvar_estado(NOME, {"ultimo": dia.isoformat()})
        dia += dt.timedelta(days=1)
    print(f"[dou] {total} atos gravados")


if __name__ == "__main__":
    main()
