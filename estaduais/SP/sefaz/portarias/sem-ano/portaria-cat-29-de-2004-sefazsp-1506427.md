---
titulo: "Portaria CAT 29 de 2004"
uf: "SP"
orgao: "Secretaria da Fazenda e Planejamento de SP"
tipo: "Portaria"
numero: "29"
data:
versao_texto: "texto do Portal de Legislação Tributária da SEFAZ-SP (pode estar consolidado)"
fonte: "https://legislacao.fazenda.sp.gov.br/Paginas/pcat292004.aspx"
id_fonte: "sefazsp-1506427"
baixado_em: 2026-11-09
modificado_na_fonte: "2022-05-06T19:56:13Z"
---

# Portaria CAT 29 de 2004

Portaria CAT-29 de 07-05-04

PORTARIA CAT-29 de 07-05-2004

(DOE 08-05-2004; Republicação DOE 12-05-2004)

Altera dispositivos da Portaria [CAT-95/03](/Paginas/pcat952003.aspx), de 17-11-2003,
que dispõe sobre a prestação de informações fiscais pelos contribuintes do setor de combustíveis

O Coordenador da Administração Tributária, tendo em vista o disposto
no Decreto nº 48.139 de 8-1-2003, expede a seguinte portaria:

**Artigo 1º**  - Passam a vigorar com a redação que se segue os dispositivos
adiante indicados da Portaria [CAT-95/03](/Paginas/pcat952003.aspx) de 17 de novembro de 2003:

I - o § 2º do artigo 2º:

"§ 2º - Os contribuintes que adquirirem combustíveis para consumo
informarão apenas as aquisições:
1 - acobertadas por Nota Fiscal, modelo 1 ou 1-A ;
2 - que superarem no período a quantidade de 10.000 (dez mil) litros em relação
a cada tipo de combustível." (NR);

II - o subitem 3.1 do Anexo Único:

"3.1 O arquivo deverá ser composto pelos conjuntos de registros previstos
na Portaria CAT 32/96, Anexo 1, item 8, incluídos os registros discriminados e
classificados na ordem abaixo:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Tipos de Registros | Posições de Classificação | A/D | Denominação dos Campos de Classificação | Observações |
| 88 C | 4a 17 20 a 22 23 a 28 33 a 35 | A A A A | CNPJ Série Número CFOP Número do Item | Classificar o Registro 88 pela ordem dos subtipos: C,D,E e T |
| 88 D | 4a 45 46 a 53 | A A | Chave do registro Data de Emissão |
| 88 E | 4 a 45 | A | Chave do registro |
| 88 T | 4 a 17 26 a 39 | A A | 1ª Parte da chave do registro 2ª Parte da chave do registro |

III - o subitem 4.2 do Anexo Único:

"4.2 Registro tipo "88D" - Informações sobre a data de emissão
dos documentos ficais e locais de armazenagem.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Nº | Denominação do Campo | Conteúdo | Tamanho | Posição | | Formato |
| 01 | Tipo | "88" | 2 | 1 | 2 | N |
| 02 | Subtipo | "D" | 1 | 3 | 3 | X |
| 03 | CNPJ / CPF | CNPJ ou CPF do remetente nas entradas e do destinatário nas saídas | 14 | 4 | 17 | N |
| 04 | IE | Inscrição Estadual do remetente nas entradas e do destinatário nas saídas | 14 | 18 | 31 | X |
| 05 | UF | Unidade da federação do remetente nas entradas e do destinatário nas saídas | 2 | 32 | 33 | X |
| 06 | Modelo | Código do modelo do documento fiscal | 2 | 34 | 35 | N |
| 07 | Série | Série do Documento Fiscal | 3 | 36 | 38 | X |
| 08 | Número | Número do Documento Fiscal | 6 | 39 | 44 | N |
| 09 | Emitente | Emitente da Nota Fiscal (P-próprio/T-terceiros) | 1 | 45 | 45 | X |
| 10 | Data de Emissão | Data de emissão do documento fiscal | 8 | 46 | 53 | D |
| 11 | Data de Saída / Entrada | Data de saída / entrada dos produtos/mercadorias | 8 | 54 | 61 | D |
| 12 | CNPJ do local de saída | CNPJ do local de saída dos produtos/mercadorias | 14 | 62 | 75 | N |
| 13 | UF do local de saída | Unidade da federação do local de saída dos produtos/mercadorias | 2 | 76 | 77 | X |
| 14 | IE do local de saída | Inscrição Estadual do local de saída dos produtos/mercadorias | 14 | 78 | 91 | X |
| 15 | CNPJ do local de recebimento/entrega | CNPJ do local de recebimento/entrega dos produtos/mercadorias | 14 | 92 | 105 | N |
| 16 | UF do local de recebimento/entrega | Unidade da federação do local de recebimento/entrega dos produtos/mercadorias | 2 | 106 | 107 | X |
| 17 | IE do local de recebimento/entrega | Inscrição Estadual do local de recebimento/entrega dos produtos/mercadorias | 14 | 108 | 121 | X |
| 18 | Brancos | Complementação com espaços | 5 | 122 | 126 | X |

IV - o subitem 4.2.1.2 do Anexo Único:

"4.2.1.2 Deverá ser gerado um registro do tipo "88D" correspondente a cada registro do tipo 50 da Portaria CAT 32/96 (envolvendo operações de combustíveis / solventes) informado; se a operação descrita na Nota Fiscal não envolver a movimentação física da mercadoria, os campos 11 a 17 devem ser deixados em branco." (NR);

V - o subitem 4.2.1.5 do Anexo Único:

"4.2.1.5 Os campos 15, 16 e 17 serão preenchidos com as informações da identificação do contribuinte estabelecido no lugar de destino físico da mercadoria. Na hipótese do lugar de destino físico da mercadoria não estar obrigado a inscrição no Cadastro de Contribuintes do ICMS, os campos 15, 16 e 17 serão preenchidos com as informações referentes ao destinatário."(NR);

VI - o subitem 4.5 do Anexo Único:

"4.5 Registro tipo "88T" - Informação sobre a prestação de serviço de transporte

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Nº | Denominação do Campo | Conteúdo | Tamanho | Posição | | Formato |
| 01 | Tipo | "88" | 2 | 1 | 2 | N |
| 02 | Subtipo | "T" | 1 | 3 | 3 | X |
| 03 | CNPJ / CPF | CNPJ ou CPF do remetente nas entradas e do destinatário nas saídas | 14 | 4 | 17 | N |
| 04 | Data de Emissão / Recebimento | Data de Emissão na Saída ou Recebimento na Entrada | 8 | 18 | 25 | D |
| 05 | UF | Unidade da Federação do remetente nas entradas e do destinatário nas saídas | 2 | 26 | 27 | X |
| 06 | Modelo | Código do modelo do documento fiscal | 2 | 28 | 29 | N |
| 07 | Série | Série do Documento Fiscal | 3 | 30 | 32 | X |
| 08 | Número | Número do Documento Fiscal | 6 | 33 | 38 | N |
| 09 | Emitente | Emitente da Nota Fiscal (P-próprio/T-terceiros) | 1 | 39 | 39 | X |
| 10 | CIF / FOB | Modalidade do Frete – "1" – CIF / Emitente ou "2" – FOB / Destinatário | 1 | 40 | 40 | N |
| 11 | CNPJ/CPF Frete | CNPJ ou CPF do Transportador | 14 | 41 | 54 | N |
| 12 | UF Frete | Unidade da Federação de localização do transportador | 2 | 55 | 56 | X |
| 13 | IE Frete | Inscrição Estadual do transportador | 14 | 57 | 70 | X |
| 14 | Modal | Modal de Transporte | 1 | 71 | 71 | N |
| 15 | Placa 1 | Número da placa do veículo | 7 | 72 | 78 | X |
| 16 | UF 1 | Unidade da Federação correspondente a Placa 1 | 2 | 79 | 80 | X |
| 17 | Placa 2 | Número da placa do veículo | 7 | 81 | 87 | X |
| 18 | UF 2 | Unidade da Federação correspondente a Placa 2 | 2 | 88 | 89 | X |
| 19 | Placa 3 | Número da placa do veículo | 7 | 90 | 96 | X |
| 20 | UF 3 | Unidade da Federação correspondente a Placa 3 | 2 | 97 | 98 | X |
| 21 | Brancos | Complementação com espaços | 29 | 99 | 126 | X |

VII - o subitem 4.5.1.2 do Anexo Único:

"4.5.1.2 Deverá ser gerado um registro "88T" correspondente a
cada registro tipo 50 da Portaria CAT 32/96 (envolvendo operações de combustíveis
/ solventes) informado." (NR);

VIII - o subitem 4.5.1.4 do Anexo Único:

"4.5.1.4 DO campo 10 deverá ser preenchido com o número 1 quando o
responsável pelo pagamento do serviço de transporte for o remetente da
mercadoria (CIF) e com o número 2 quando o responsável pelo pagamento for o
destinatário da mercadoria (FOB)." (NR);

IX - o subitem 4.5.1.5 do Anexo Único:

"4.5.1.5 Os campos 11, 12 e 13 serão preenchidos com informações da
identificação do prestador de serviço de transporte; se a operação descrita
na Nota Fiscal não envolver a movimentação física da mercadoria o campo 11 (CNPJ/CPF
Frete) deve ser preenchido com a expressão "S/MOV.FISICA" e os campos
12 a 20 devem ser deixados em branco." (NR);

X - o subitem 4.5.1.6 do Anexo Único:

"4.5.1.6 O campo 14 deverá ser preenchido de acordo com a Tabela de
Modalidade de Transporte apresentada, abaixo, nas Tabelas Auxiliares."
(NR);

XI - o subitem 4.5.1.7 do Anexo Único:

"4.5.1.7 Os campos 15 a 19 deverão ser preenchidos quando a prestação do
serviço de transporte envolver a modalidade rodoviária." (NR);

XII - o subitem 4.5.1.8 do Anexo Único:

"4.5.1.8 Os campos 15 e 16 deverão conter as informações sobre o veículo
tracionador - caminhão de eixo simples, eixo duplo, trator, etc." (NR);

XIII - o subitem 4.5.1.9 do Anexo Único:

"4.5.1.9 Os campos 17 a 20 deverão conter as informações referentes ao
semi- reboque e/ou reboque(s). Não havendo esses tipos de veículos deixar o
campo em branco." (NR).

**Artigo 2º**  - Esta portaria entra em vigor na data de sua publicação,
retroagindo seus efeitos em relação às operações realizadas a partir de
janeiro de 2004.

(Republicada por ter saído com incorreções)
