---
titulo: "Portaria CAT 98 de 2007"
uf: "SP"
orgao: "Secretaria da Fazenda e Planejamento de SP"
tipo: "Portaria"
numero: "98"
data:
versao_texto: "texto do Portal de Legislação Tributária da SEFAZ-SP (pode estar consolidado)"
fonte: "https://legislacao.fazenda.sp.gov.br/Paginas/pcat982007.aspx"
id_fonte: "sefazsp-1507794"
baixado_em: 2026-11-08
modificado_na_fonte: "2022-05-06T20:21:34Z"
---

# Portaria CAT 98 de 2007

PORTARIA CAT-98, de 05-10-2007

PORTARIA CAT-98, de 05-10-2007

DOE 06/10/2007

Altera a Portaria [CAT-85/07](/Paginas/pcat852007.aspx), de 4-9-2007, que estabelece disciplina
relativa ao Registro Eletrônico de Documento Fiscal - REDF.

O Coordenador da Administração Tributária, tendo em vista o disposto
no artigo 212-P do Regulamento do Imposto sobre Operações Relativas à Circulação de
Mercadorias e sobre Prestações de Serviços de Transporte Interestadual e Intermunicipal
e de Comunicação, aprovado pelo Decreto 45.490, de 30 de novembro de 2000, expede a
seguinte portaria:

**Artigo 1°** - Passa a vigorar com a redação que se segue o Anexo
II da Portaria [CAT-85/07](/Paginas/pcat852007.aspx),
de 4 de setembro de 2007:

**"Anexo II**

Leiaute do arquivo digital da Nota Fiscal de Venda a Consumidor-NFVC,
modelo 2

(a que se refere o artigo 9º, II, "a", da Portaria CAT-85/07)

1. Cada arquivo digital deverá conter
informações relativas às NFVC emitidas por um único estabelecimento, no período
compreendido entre a data inicial e a data final indicadas no próprio arquivo, e deverá
observar a seguinte especificação técnica:

1.1 - Formato do arquivo: Texto (Text Encoding = UTF-8);

1.2 - Tamanho máximo: 500 KB;

1.3 - Divisão entre os campos de cada registro: utilizar o caractere
"|" (pipe);

1.4 - Finalização da linha de cada registro: proceder conforme
orientado no item 3;

1.5 - Formato dos campos: data, numérico e alfanumérico;

1.6 - Tamanho dos campos:

1.6.1 - fixo, com tamanho exato de preenchimento (ex.: campos do CPF ou
CNPJ); 1.6.2 - variável, com limite de tamanho máximo para preenchimento (ex.: campo do
nome do destinatário da Nota Fiscal de Venda a Consumidor).

2. Estrutura do arquivo:

2.1 - O arquivo deverá ser composto pelos seguintes tipos de
registros:

2.1.1 - Tipo 10 - Registro obrigatório, cabeçalho do arquivo,
identificador do estabelecimento emitente. Deve ser informado exatamente 1 (um) registro
por arquivo.

2.1.2 - Tipo 20 - Registro obrigatório, identificador da Nota Fiscal
de Venda a Consumidor - NFVC, modelo 2. Deve ser informado no mínimo 1 (um) registro por
arquivo.

2.1.3 - Tipo 21 - Registro obrigatório, discriminador dos itens das
mercadorias da NFVC, modelo 2. Deve ser informado no mínimo 1 (um) registro por NFVC,
modelo 2.

2.1.4 - Tipo 22 - Registro opcional, indicador de vendas a prazo.

2.1.5 - Tipo 90 - Registro obrigatório, rodapé totalizador da
quantidade de registros no arquivo. Deve ser informado exatamente 1 (um) registro por
arquivo.

2.2 - Os registros deverão ser classificados na seguinte ordem:

|  |  |  |  |
| --- | --- | --- | --- |
| RegistroTipo | Informação | Hierarquia | Quantidade obrigatória |
| 10 | Cabeçalho | 1 | =1 por arquivo |
| 20 | Identificador da NFVC, mod. 2 | 2 | >= 1 por arquivo |
| 21 | Discriminador dos itens da NFVC, mod.2 | 3 | >= 1 por NF |
| 22 | Vendas a prazo | 3 | >= 0 por NF |
| 90 | Rodapé totalizador dos registros | 1 | =1 por arquivo |

Modelo exemplificativo: após informado o registro tipo 20 relativo a
uma NFVC, devem ser informados todos os registros tipo 21 referentes a essa NFVC; somente
após informado o último registro tipo 21 referente a essa NFVC, devem ser informados
todos os registros tipo 22 (parcelas) referentes à mesma NFVC.

10 - Cabeçalho

    20 - NFVC (com 3 itens de mercadorias)

        21 - Item NFVC

        21 - Item NFVC

        21 - Item NFVC

    20 - NFVC (com 1 item de mercadoria e 2 parcelas de
pagamento a prazo)

        21 - Item NFVC

        22 - Parcela NFVC

        22 - Parcela NFVC

    20 - NFVC (com 1 item de mercadoria)

        21 - Item NFVC

90 - Rodapé totalizador

3.
Leiaute detalhado do arquivo:

Registro Tipo 10 - Cabeçalho (obrigatório um registro por arquivo)

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| No | Campo | Tamanho Fixo | Tamanho Máximo | Formato | Obrigatório | Observação |
| 1 | Tipo de registro | 2 | - | Numérico | Sim | Preencher com o valor "10" para indicar o tipo de registro |
| 2 | Versão do leiaute do arquivo | 4 | - | Alfanumérico | Sim | Indica a versão do leiaute do arquivo. Preencher com o número da versão atual : "1.00" |
| 3 | CNPJ completo do estabelecimento emitente | 14 | - | Numérico | Sim | Preencher com o CNPJ completo do estabelecimento. A informação será valida para todos os registros do arquivo. Demais dados do estabelecimento emitente serão inseridos pela SEFAZ/SP de acordo com aqueles constantes na base cadastral (DECA). Deve ser preenchido apenas com números. |
| 4 | Data de início do período transferido no arquivo | 10 | - | DD/MM/AAAA | Sim | Menor data de emissão das NFVC transmitidas. Preencher no formato : DD/MM/AAAA (dia, mês e ano separados por barras). |
| 5 | Data de fim do período transferido no arquivo | 10 | - | DD/MM/AAAA | Sim | Maior data de emissão das NFVC transmitidas. Preencher no formato: DD/MM/AAAA (dia, mês e ano separados por barras). |
| FINALIZAÇÃO DA LINHA DO REGISTRO: NÃO UTILIZAR O CARACTERE *PIPE* " | " NO FINAL DA LINHA | | | | | | |

3.2 Registro Tipo 20 - Registro da NFVC (obrigatório, no mínimo, um
registro por arquivo)

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| N | Informação | Tamanho Fixo | Tamanho Máximo | Formato | Obrigatório | Observação |
| 1 | Tipo de registro | 2 | - | Numérico | Sim | Preencher com o valor "20", para indicar o tipo de registro |
| 2 | Série da NFVC | 1 |  | Numérico | Sim | Preencher com os seguintes valores:  " 1 " – para série D  " 2 " – para série D única  " 3 " – para série Única |
| 3 | Subsérie da NFVC | - | 6 | Numérico | Não | Subsérie da NFVC |
| 4 | Número da NFVC | - | 9 | Numérico | Sim | Número da NFVC |
| 5 | Data de emissão | 10 | - | DD/MM/AAAA | Sim | Data de emissão da NFVC. Preencher no formato: DD/MM/AAAA (dia, mês e ano separados por barras). |
| 6 | Data da saída | 10 | - | DD/MM/AAAA | Não | Data de saída da mercadoria. Preencher no formato: DD/MM/AAAA (dia, mês e ano separados por barras). |
| 7 | CPF ou CNPJ do destinatário | 11 (CPF) ou  14 (CNPJ) | - | Numérico | Não | Indicar o número do CPF (11 dígitos) ou do CNPJ (14 dígitos) do destinatário da mercadoria. Preencher apenas com números. Caso o CPF ou CNPJ sejam desconhecidos, o campo não deverá ser preenchido |
| 8 | Nome do destinatário | - | 60 | Alfanumérico | Não |  |
| 9 | Logradouro | - | 60 | Alfanumérico | Não |  |
| 10 | Número | - | 60 | Alfanumérico | Não |  |
| 11 | Complemento | - | 60 | Alfanumérico | Não |  |
| 12 | Bairro / Distrito | - | 60 | Alfanumérico | Não |  |
| 13 | Município | - | 60 | Alfanumérico | Não |  |
| 14 | UF | 2 | - | Alfanumérico | Não |  |
| 15 | CEP | - | 8 | Alfanumérico | Não | Preencher apenas com números |
| 16 | Telefone | - | 10 | Numérico | Não | Preencher apenas com números |
| 17 | Valor total dos produtos | 2 (casas decimais) | 15 (antes da vírgula) | Numérico | Sim | Preencher SEMPRE com duas casas decimais, inclusive para valor zero. Ex.: "15,00", "16,85", "2435,05", "101000,00", "0,00". |
| 18 | Valor total do desconto | 2 (casas decimais) | 15 (antes da vírgula) | Numérico | Sim | Preencher SEMPRE com duas casas decimais, inclusive para valor zero. Ex.: "15,00", "16,85", "2435,05", "101000,00", "0,00". |
| 19 | Valor total do frete | Numérico | Sim |
| 20 | Valor total do seguro | Numérico | Sim |
| 21 | Outras despesas acessórias | Numérico | Sim |
| 22 | Descrição das outras despesas acessórias | - | 60 | Alfanumérico | Não | Texto livre |
| 23 | Valor total da NFVC | 2 (casas decimais) | 15 (antes da vírgula) |  | Sim | Deve corresponder ao resultado do cálculo: valores totais dos produtos + frete + seguro + outras despesas acessórias – descontos. Preencher SEMPRE com duas casas decimais, inclusive para valor zero. Ex.: "15,00", "16,85", "2435,05", "101000,00", "0,00". |
| 24 | Informações complementares do interesse do contribuinte | - | 5000 | Alfanumérico | Não | Texto livre |
| 25 | Informações complementares de interesse do fisco | - | 256 | Alfanumérico | Não | Texto livre |
| 26 | Realiza entrega em domicílio | 1 |  | Numérico | Sim | Preencher com valor "1" para resposta afirmativa ou valor "2" para resposta negativa |
| 27 | Logradouro do local de entrega | - | 60 | Alfanumérico | Não | Texto livre |
| 28 | Número do local de entrega | - | 60 | Alfanumérico | Não | Texto livre |
| 29 | Complemento do local de entrega | - | 60 | Alfanumérico | Não | Texto livre |
| 30 | Bairro / Distrito do local de entrega | - | 60 | Alfanumérico | Não | Texto livre |
| 31 | Município do local de entrega | - | 60 | Alfanumérico | Não | Texto livre |
| 32 | UF do local de entrega | - | 2 | Alfanumérico | Não |  |
| 33 | Realiza venda a prazo | 1 |  | Numérico | Sim | Preencher com valor "1" para resposta afirmativa ou valor "2" para resposta negativa |
| 34 | Preço à vista | 2 (casas decimais) | 15 (antes da vírgula) | Numérico | Não | Valor da venda à vista |
| 35 | Preço final | Numérico | Não | Valor do preço final na venda a prazo |
| 36 | Quantidade de parcelas nas vendas a prazo | - | 2 | Numérico | Não | Indicar a quantidade de parcelas. Preencher apenas com número INTEIRO, sem vírgula. |
| FINALIZAÇÃO DA LINHA DO REGISTRO: SE O CAMPO 36 TIVER SIDO PREENCHIDO, NÃO UTILIZAR O CARACTERE *PIPE* " | ". SE O CAMPO 36 NÃO TIVER SIDO PREENCHIDO, UTILIZAR O CARACTERE *PIPE* " | ". | | | | | | |

3.3 Registro Tipo 21 - Itens da NFVC, modelo 2 (obrigatório, no mínimo,
um registro por NFVC)

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| N | Informação | Tamanho Fixo | Tamanho Máximo | Formato | Obrigatório | Observação |
| 1 | Tipo de registro | 2 | - | Numérico | Sim | Preencher com o valor "21", para indicar o tipo de registro |
| 2 | Número do item | - | 3 | Numérico | Sim | Número seqüencial dos itens informados |
| 3 | Código do produto | - | 60 | Alfanumérico | Não | Código interno utilizado pelo emitente, quando existir |
| 4 | Tipo de receita | 1 | - | Numérico | Sim | Preencher com os seguintes valores:  " 1 " - para revenda de mercadorias;  " 2 " - para venda de mercadorias industrializadas pelo emitente;  " 3 " - para venda de mercadorias imunes ou sujeitas à substituição tributária. |
| 5 | Descrição da mercadoria | - | 120 | Alfanumérico | Sim | Texto livre |
| 6 | Unidade de comercialização | - | 6 | Alfanumérico | Não | Texto livre |
| 7 | Quantidade | - | 11 (antes da vírgula) 3 (casas decimais) | Numérico | Sim | Quantidade relativa à unidade de comercialização. Preencher com número inteiro ou com 3 casas decimais (a utilização da vírgula é opcional). Ex.: "12" ou "12,000" |
| 8 | Valor unitário | 2 (casas decimais) | 15 (antes da vírgula) | Numérico | Sim | Preencher SEMPRE com duas casas decimais, inclusive para valor zero. Ex.: "15,00", "16,85", "2435,05", "101000,00", "0,00". |
| 9 | Valor total | 2 (casas decimais) | 15 (antes da vírgula) | Numérico | Sim | Deve corresponder ao resultado do cálculo: Qtdd x valor unitário. Preencher SEMPRE com duas casas decimais, inclusive para valor zero. Ex.: "15,00", "16,85", "2435,05", "101000,00", "0,00". |
| FINALIZAÇÃO DA LINHA DO REGISTRO: NÃO UTILIZAR O CARACTERE *PIPE* " | " NO FINAL DA LINHA. | | | | | | |

3.4 Registro Tipo 22 - Vendas a prazo (registro opcional)

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| N | Informação | Tamanho Fixo | Tamanho Máximo | Formato | Obrigatório | Observação |
| 1 | Tipo de registro | 2 | - | Numérico | Sim | Preencher com o valor "22" para indicar o tipo de registro. |
| 2 | Valor da parcela | 2 (casas decimais) | 15 (antes da vírgula) | Numérico | Sim | Preencher SEMPRE com duas casas decimais, inclusive para valor zero. Ex.: "15,00", "16,85", "2435,05", "101000,00", "0,00". |
| 3 | Data de vencimento da parcela | 10 | - | DD/MM/AAAA | Sim | Preencher no formato : DD/MM/AAAA (dia, mês e ano separados por barras). |
| FINALIZAÇÃO DA LINHA DO REGISTRO: NÃO UTILIZAR O CARACTERE *PIPE* " | " NO FINAL DA LINHA | | | | | | |

3.5 Registro do Tipo 90 - Registro rodapé (obrigatório um registro por
arquivo)

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| N | Informação | Tamanho Fixo | Tamanho Máximo | Formato | Obrigatório | Observação |
| 1 | Tipo de registro | 2 | - | Numérico | Sim | Preencher com o valor "90" para indicar o tipo de registro |
| 2 | Quantidade de registros tipo 20 |  | 5 | Numérico | Sim | Indicar quantidade de registros tipo "20" no arquivo |
| 3 | Quantidade de registros tipo 21 |  | 5 | Numérico | Sim | Indicar quantidade de registros tipo "21" no arquivo |
| 4 | Quantidade de registros tipo 22 |  | 5 | Numérico | Sim | Indicar quantidade de registros tipo "22" no arquivo |
| 5 | Somatória dos valores totais das NFVC informadas no arquivo | 2 (casas decimais) | 15 (antes da vírgula) | Numérico | Sim | Somatória dos campos "Valor total da NFVC" informados nos registros tipo "20". Preencher SEMPRE com duas casas decimais, inclusive para valor zero. Ex.: "15,00", "16,85", "2435,05", "101000,00", "0,00". |
| FINALIZAÇÃO DA LINHA DO REGISTRO: NÃO UTILIZAR O CARACTERE *PIPE* " | " NO FINAL DA LINHA | | | | | | |

" (NR).

**Artigo 2°** - Esta portaria entra em vigor na data de sua
publicação.
