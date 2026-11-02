# ATLAS-LEIS

Complemento do acervo [ctresb/leis](https://github.com/ctresb/leis), a legislação brasileira em Markdown,
mantido para o ATLAS LAW, o copiloto jurídico do escritório Marco Matos Advogado (Santos/SP).

O ctresb/leis já cobre a Constituição, as leis federais e estaduais, os atos de reguladores e os precedentes vinculantes. **Este repositório coleta o que falta lá**,
no mesmo formato (cabeçalho YAML + texto) e na mesma estrutura de pastas, para que os dois acervos se somem:

| Frente | Fonte | Pasta |
|---|---|---|
| Santos | LEGIS – Prefeitura de Santos; Diário Oficial de Santos (vigia diária) | `municipais/SP/santos/`, `municipais/SP/santos/diario-oficial/` |
| Baixada Santista | SAPL das Câmaras de Praia Grande e Bertioga; DOM-E de Peruíbe | `municipais/SP/<municipio>/` |
| Cartórios e registro | Atos do CNJ / Corregedoria Nacional; instruções normativas e manuais do DREI | `reguladores/cnj/`, `reguladores/drei/` |
| Tributário administrativo | SEFAZ-SP (respostas a consultas, decisões normativas, portarias CAT) | `estaduais/SP/sefaz/` |
| TJ-SP | Súmulas, enunciados (inclusive Câmaras Empresariais), temas de IRDR | `jurisprudencia/tjsp/` |
| Trabalhista | TRT-2 (súmulas, OJs, precedentes normativos, teses prevalecentes); precedentes do TST e TRT-2 no BNP/CNJ (IRR, IAC); Normas Regulamentadoras do MTE | `jurisprudencia/trt2/`, `jurisprudencia/tst/precedentes/`, `reguladores/mte/normas-regulamentadoras/` |
| Federal (novidades) | DOU Seção 1 filtrado pelas áreas do escritório | `dou/` |

## Como funciona
- **Coleta diária** (`.github/workflows/coleta.yml`, 05:17 de Brasília): cada coletor retoma de onde parou
  (`estado/`) e grava as normas novas ou alteradas.
- **Novidades**: tudo o que entra ou muda é registrado em `_novidades/AAAA-MM-DD.jsonl`, base do boletim semanal.
- **Sondagem** (`coletores/sondagem.py`): testa as fontes oficiais e calibra os coletores.

## Aviso
Textos convertidos automaticamente de fontes oficiais, com caráter informativo. **Não substituem a publicação
oficial.** Confira sempre o link do campo `fonte` antes de citar.

Scripts sob licença MIT. Textos normativos não são objeto de proteção autoral (Lei 9.610/1998, art. 8º, IV).
