---
titulo: "Portaria CAT 110 de 2003"
uf: "SP"
orgao: "Secretaria da Fazenda e Planejamento de SP"
tipo: "Portaria"
numero: "110"
data:
versao_texto: "texto do Portal de Legislação Tributária da SEFAZ-SP (pode estar consolidado)"
fonte: "https://legislacao.fazenda.sp.gov.br/Paginas/pcat1102003.aspx"
id_fonte: "sefazsp-1505451"
baixado_em: 2026-11-09
modificado_na_fonte: "2022-05-06T19:37:33Z"
---

# Portaria CAT 110 de 2003

Portaria CAT-110 de 22-12-03

Portaria CAT-110, de 22-12-2003

(DOE de 24-12-2003)

Altera a Portaria [CAT-79/03,](/Paginas/pcat792003.aspx) de 10
de setembro de 2003, que uniformiza e disciplina a emissão, escrituração, manutenção
e prestação das informações dos documentos fiscais emitidos em via única por sistema
eletrônico de processamento de dados

O Coordenador da Administração Tributária, tendo em vista o disposto no Convênio
ICMS-115, de 12-12-2003, e nos artigos 146, § 4º, "e" e 250 do Regulamento do
Imposto sobre Circulação de Mercadorias e sobre Prestação de Serviços - RICMS,
aprovado pelo Decreto nº 45.490, de 30-11-2000, expede a seguinte portaria:

**Artigo 1º** - Passa a vigorar com a redação que se segue o item 2 do § 4º do
artigo 4º da Portaria CAT-79/03, de 10 de setembro de 2003:

"2 - 1 (hum) milhão de documentos fiscais, para os contribuintes com volume
mensal de emissão superior a 1 (hum) milhão de documentos fiscais;" (NR).

**Artigo 2º** - Passam a vigorar com a redação que se segue os itens e subitens
adiante indicados do Manual de Orientação (Anexo Único) da Portaria CAT-79/03, de 10 de
setembro de 2003:

**I** - o item 5:

"5. Arquivo tipo MESTRE DE DOCUMENTO FISCAL

5.1. O arquivo deverá ser composto por registros que contenham as seguintes
informações, classificadas pelo número do documento fiscal, em ordem crescente:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **n.º** | **Conteúdo** | **Tam.** | **posição** | | **formato** |
|  |  |  | **inicial** | **final** |  |
| 1 | CNPJ ou CPF | 14 | 1 | 14 | N |
| 2 | IE | 14 | 15 | 28 | X |
| 3 | Razão Social | 35 | 29 | 63 | X |
| 4 | UF | 2 | 64 | 65 | X |
| 5 | Classe de Consumo ou Tipo de Assinante | 1 | 66 | 66 | N |
| 6 | Fase ou Tipo de Utilização | 1 | 67 | 67 | N |
| 7 | Grupo de Tensão | 2 | 68 | 69 | N |
| 8 | Código de Identificação do consumidor ou assinante | 12 | 70 | 81 | X |
| 9 | Data de emissão | 8 | 82 | 89 | N |
| 10 | Modelo | 2 | 90 | 91 | N |
| 11 | Série | 3 | 92 | 94 | X |
| 12 | Número | 9 | 95 | 103 | N |
| 13 | Código de Autenticação Digital documento fiscal | 32 | 104 | 135 | X |
| 14 | Valor Total (com 2 decimais) | 12 | 136 | 147 | N |
| 15 | BC ICMS (com 2 decimais) | 12 | 148 | 159 | N |
| 16 | ICMS destacado (com 2 decimais) | 12 | 160 | 171 | N |
| 17 | Operações Isentas ou não tributadas (com 2 decimais) | 12 | 172 | 183 | N |
| 18 | Outros valores (com 2 decimais) | 12 | 184 | 195 | N |
| 19 | Situação do documento | 1 | 196 | 196 | X |
| 20 | Ano e Mês de referência de apuração | 4 | 197 | 200 | N |
| 21 | Referência ao item da NF | 9 | 201 | 209 | N |
| 22 | Número do terminal telefônico ou Número da conta de consumo | 10 | 210 | 219 | X |
| 23 | Brancos - reservado para uso futuro | 3 | 220 | 222 | X |
| 24 | Código de Autenticação Digital do registro | 32 | 223 | 254 | X |
|  | **Total** | **254** |  |  |  |

5.2. Observações:

5.2.1. Informações referentes aos dados cadastrais do consumidor da energia elétrica
ou tomador dos serviços de comunicação/telecomunicação

5.2.1.1. Campo 01 - Informar o CNPJ ou CPF. Em se tratando de pessoa não obrigada à
inscrição no CNPJ ou CPF, preencher o campo com zeros;

5.2.1.2. Campo 02 - Informar a Inscrição Estadual. Em se tratando de pessoa não
obrigada à inscrição estadual, preencher o campo com a expressão "ISENTO";

5.2.1.3. Campo 03 - Informar a razão social, denominação ou nome;

5.2.1.4. Campo 04 - Informar a sigla da UF da localização do consumidor da energia
elétrica ou tomador dos serviços de comunicação/telecomunicação. Em se tratando de
operações com exterior, preencher o campo com a expressão "EX";

5.2.1.5. Campo 05 - Informar o código da classe de consumo da energia elétrica ou
tipo de assinante de serviço de comunicação/telecomunicação, utilizando tabela de
item 11.1;

5.2.1.6. Campo 06 - Informar o código do tipo de ligação (Mono/Bi/Trifásico) ou
tipo de utilização, conforme tabela de item 11.2;

5.2.1.7. Campo 07 - Informar o código do Grupo de Tensão, conforme tabela de item
11.3;

5.2.1.8. Campo 08 - Informar o código de identificação do consumidor ou assinante
utilizado pelo contribuinte;

5.2.2. Informações referentes ao documento fiscal

5.2.2.1. Campo 09 - Informar a data de emissão do documento fiscal no formato
AAAAMMDD;

5.2.2.2. Campo 10 - Informar o modelo do documento fiscal, conforme código da tabela
de documentos fiscais, do item 11.4;

5.2.2.3. Campo 11 - Informar a série do documento fiscal, utilizar a letra
"U" para indicar série única;

5.2.2.4. Campo 12 - Informar o número seqüencial atribuído pelo sistema eletrônico
de processamento de dados ao documento fiscal (vide item 2.1.2). O campo deverá ser
alinhado à direita com as posições não significativas preenchidas com zeros;

5.2.2.5. Campo 13 - Informar o código de autenticação digital obtido através da
aplicação do algoritmo MD5 (Message Digest 5, vide item 11.7) de 128 bits na cadeia de
caracteres formada pelos campos 01, 12, 14, 15 e 16, respeitando o tamanho previsto do
campo, assim como os brancos e zeros de preenchimento.

5.2.3. Informações referentes aos valores do documento fiscal

5.2.3.1. Campo 14 - Informar o Valor Total do documento fiscal, com 2 decimais;

5.2.3.2. Campo 15 - Informar a Base de Cálculo do ICMS destacado no documento fiscal,
com 2 decimais;

5.2.3.3. Campo 16 - Informar o valor do ICMS destacado no documento fiscal, com 2
decimais;

5.2.3.4. Campo 17 - Informar o valor das operações ou serviços isentos ou não
tributados pelo ICMS, com 2 decimais;

5.2.3.5. Campo 18 - Informar os outros valores constantes do documento fiscal, com 2
decimais. Neste campo devem ser informados as multas e juros, tributos que não compõe a
BC do ICMS como o PIS e COFINS, cobrança de terceiros, mercadorias ou serviços com ICMS
diferido, etc.;

5.2.4. Informações de controle

5.2.4.1. Campo 19 - Informar a situação do documento. Este campo deve ser preenchido
com "S", em se tratando de documento fiscal cancelado ou com "N", caso
contrário;

5.2.4.2. Campo 20 - Informar o ano e mês de referência de apuração do ICMS do
documento fiscal, utilizando o formato "AAMM";5.2.4.3. Campo 21 - Informar o
número do registro do arquivo ITEM DO DOCUMENTO FISCAL, onde se encontra o primeiro item
do documento fiscal;

5.2.4.4. Campo 22 - Informar a localidade de registro e o número do terminal/aparelho
telefônico no formato "LLNNNNNNNN", onde "LL" é o código da
localidade e "NNNNNNNN", o número de identificação do terminal/aparelho
telefônico. Quando se tratar de Nota Fiscal/Conta de Energia Elétrica, informar o
número da conta de consumo e nos demais casos deixar em branco;

5.2.4.5. Campo 23 - Brancos, reservado para uso futuro;

5.2.4.6. Campo 24 - Informar o código de autenticação digital obtido através da
aplicação do algoritmo MD5 (Message Digest 5, vide item 11.7) de 128 bits na cadeia de
caracteres formada pelos campos 01 a 23.

5.2.5. Deverá ser criado um único registro fiscal mestre para cada documento fiscal
emitido." (NR);

**II** - o subitem 6.2.3.1:

"6.2.3.1. Campo 10 - Informar o CFOP do item do documento fiscal. Preencher o
campo com zeros, quando se tratar de item apenas financeiro, sem repercussão fiscal, tais
como a cobrança de terceiros, juros e multa de mora;" (NR);

**III** - o subitem 6.2.3.2:

"6.2.3.2. Campo 11 - Informar o número de ordem do item do documento fiscal. A
quantidade máxima de itens por documento fiscal é limitada em 990 (novecentos e
noventa), devendo ser iniciada em 001 (um). Não detalhar os serviços medidos para evitar
a identificação individual das chamadas (telefone chamado, localidade, data, hora e
duração), informar apenas o tipo de serviço prestado (chamadas locais a cobrar,
chamadas de longa distância, chamadas internacional, etc.) e o valor total cobrado pelo
serviço prestado. Na conta de energia elétrica a Base de Cálculo e o valor do ICMS
deverão ser informados de forma individualizada para cada item de fornecimento. Toda e
qualquer cobrança realizada no documento fiscal, tal como a cobrança de terceiros, juros
e multas de mora, contas de meses anteriores, etc., mesmo não sendo fato gerador do ICMS
deverá ser informada como um item do documento fiscal;" (NR);

**IV** - o subitem 6.2.3.4:

"6.2.3.4. Campo 13 - Informar a descrição do fornecimento ou serviço do item. A
descrição deverá ser sucinta e clara de forma que seja possível a correta
identificação do fornecimento ou serviço;" (NR);

**V** - o item 7:

"7. Arquivo tipo DADOS CADASTRAIS DO DESTINATÁRIO DO DOCUMENTO FISCAL

7.1. O arquivo deverá ser composto por registros que contenham as seguintes
informações, devendo ser apresentado um registro para cada documento fiscal contido no
Arquivo MESTRE DE DOCUMENTO FISCAL:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **n.º** | **Conteúdo** | **Tam.** | **posição** | | **formato** |
|  |  |  | **inicial** | **final** |  |
| 1 | CNPJ ou CPF | 14 | 1 | 14 | N |
| 2 | IE | 14 | 15 | 28 | X |
| 3 | Razão Social | 35 | 29 | 63 | X |
| 4 | Logradouro | 45 | 64 | 108 | X |
| 5 | Número | 5 | 109 | 113 | N |
| 6 | Complemento | 15 | 114 | 128 | X |
| 7 | CEP | 8 | 129 | 136 | N |
| 8 | Bairro | 15 | 137 | 151 | X |
| 9 | Município | 30 | 152 | 181 | X |
| 10 | UF | 2 | 182 | 183 | X |
| 11 | Telefone de contato | 10 | 184 | 193 | N |
| 12 | Código de Identificação do consumidor ou assinante | 12 | 194 | 205 | X |
| 13 | Número do terminal telefônico ou Número da conta de consumo | 10 | 206 | 215 | X |
| 14 | UF de habilitação do terminal telefônico | 2 | 216 | 217 | X |
| 15 | Brancos - reservado para uso futuro | 5 | 218 | 222 | X |
| 16 | Código de Autenticação Digital do registro | 32 | 223 | 254 | X |
|  | **Total** | **254** |  |  |  |

7.2. Observações:

7.2.1. Informações referentes ao consumidor da energia elétrica ou do tomador dos
serviços de comunicação/telecomunicação

7.2.1.1. Campo 01 -Informar o CNPJ ou CPF. Em se tratando de pessoa não obrigada à
inscrição no CNPJ ou CPF, preencher o campo com zeros;

7.2.1.2. Campo 02 - Informar a Inscrição Estadual. Em se tratando de pessoa não
obrigada à inscrição estadual, preencher o campo com a expressão "ISENTO";

7.2.1.3. Campo 03 - Informar a razão social, denominação ou nome;

7.2.1.4. Campo 04 - Informar o Logradouro do endereço;

7.2.1.5. Campo 05 - Informar o Número do endereço;

7.2.1.6. Campo 06 - Informar o Complemento do endereço;

7.2.1.7. Campo 07 - Informar o CEP do endereço;

7.2.1.8. Campo 08 - Informar o Bairro do endereço;

7.2.1.9. Campo 09 - Informar o Município do endereço;

7.2.1.10. Campo 10 - Informar a sigla da UF do endereço. Em se tratando de operações
com o exterior, preencher o campo com a expressão "EX";

7.2.1.11. Campo 11 - Informar a localidade de registro e o número do telefone de
contato no formato "LLNNNNNNNN", onde "LL" é o código da localidade
e "NNNNNNNN" o número de identificação do terminal/aparelho telefônico;

7.2.1.12. Campo 12- Informar o código de identificação do consumidor ou assinante
utilizado pelo contribuinte

7.2.1.13. Campo 13 - Informar a localidade de registro e o número do terminal/aparelho
telefônico no formato "LLNNNNNNNN", onde "LL" é o código da
localidade e "NNNNNNNN" o número de identificação do terminal/aparelho
telefônico. Quando se tratar de Nota Fiscal/Conta de Energia Elétrica, informar o
número da conta de consumo, nos demais casos deixar em branco;

7.2.1.14. Campo 14 - Informar a sigla da UF de habilitação do terminal/aparelho
telefônico, deixando em branco nos demais casos;

7.2.2. Informações de Controle

7.2.2.1. Campo 15 - Brancos, reservado para uso futuro;

7.2.2.2. Campo 16 - Informar o código de autenticação digital obtido através da
aplicação do algoritmo MD5 (Message Digest 5, vide item 11.7) de 128 bits na cadeia de
caracteres formada pelos campos 01 a 15." (NR);

**VI** - o item 11:

"11. Anexos

11.1. Tabelas de Classe de Consumo da Energia Elétrica e Tipo de Assinantes

11.1.1. Classe de Consumo de Energia Elétrica

|  |  |
| --- | --- |
| Classe de Consumo | Código |
| Comercial | 1 |
| Consumo Próprio | 2 |
| Iluminação Pública | 3 |
| Industrial | 4 |
| Poder Público | 5 |
| Residencial | 6 |
| Rural | 7 |
| Serviço Público | 8 |

11.1.2. Tipo de Assinante de Serviços de Telecomunicação

|  |  |
| --- | --- |
| Tipo de Assinante | Código |
| Comercial/Industrial | 1 |
| Poder Público | 2 |
| Residencial/Pessoa física | 3 |
| Público | 4 |
| Semi-Público | 5 |
| Outros | 6 |

11.2. Tabela de Tipo de Ligação e Tipo de Utilização

11.2.1. Tipo de Ligação - informar somente na Nota Fiscal/Conta de Energia Elétrica,
modelo 6

|  |  |
| --- | --- |
| Ligação | Código |
| Monofásico | 1 |
| Bifásico | 2 |
| Trifásico | 3 |

11.2.2. Tipo de utilização - informar apenas quando não se tratar de na Nota
Fiscal/Conta de Energia Elétrica, modelo 6

|  |  |
| --- | --- |
| Tipo de Utilização | Código |
| Telefonia | 1 |
| Comunicação de dados | 2 |
| TV por Assinatura | 3 |
| Provimento de acesso à Internet | 4 |
| Multimídia | 5 |
| Outros | 6 |

11.3. Tabela de Grupo de Tensão - informar apenas quando se tratar de Nota
Fiscal/Conta de Energia Elétrica, modelo 6. Nos demais caso deverá ser preenchido com
00;

|  |  |
| --- | --- |
| Subgrupo | Código |
| A1 – Alta Tensão (230kV ou mais) | 01 |
| A2 - Alta Tensão (88 a 138kV) | 02 |
| A3 – Alta Tensão (69kV) | 03 |
| A3a – Alta Tensão (30kV a 44kV) | 04 |
| A4 – Alta Tensão (2,3kV a 25kV) | 05 |
| AS – Alta Tensão Subterrâneo | 06 |
| B1 – Residencial | 07 |
| B1 – Residencial Baixa Renda | 08 |
| B2 – Rural | 09 |
| B2 – Cooperativa de Eletrificação Rural | 10 |
| B2 – Serviço Público de Irrigação | 11 |
| B3 – Demais Classes | 12 |
| B4a – Iluminação Pública – rede de distribuição | 13 |
| B4b – Iluminação Pública – bulbo de lâmpada | 14 |

11.4. Tabela de documentos fiscais

|  |  |
| --- | --- |
| Documento Fiscal | Código |
| Nota Fiscal de Serviço de Comunicação, modelo 21 | 21 |
| Nota Fiscal de Serviço de Telecomunicações, modelo 22 | 22 |
| Nota Fiscal/Conta de Energia Elétrica, modelo 6 | 06 |
| Nota Fiscal/Conta de Gás, modelo 1 | 01 |

11.5. Tabela de classificação do item de documento fiscal

|  |  |  |
| --- | --- | --- |
| Grupo | Código | Descrição |
| 01. Assinatura | 0101 | Assinatura de serviços de telefonia |
|  | 0102 | Assinatura de serviços de comunicação de dados |
|  | 0103 | Assinatura de serviços de TV por Assinatura |
|  | 0104 | Assinatura de serviços de provimento de acesso à internet |
|  | 0105 | Assinatura de serviços multimídia |
|  | 0199 | Assinatura de outros serviços |
| 02. Habilitação | 0201 | Habilitação de serviços de telefonia |
|  | 0202 | Habilitação de serviços de comunicação de dados |
|  | 0203 | Habilitação de serviços de TV por Assinatura |
|  | 0204 | Habilitação de serviços de provimento de acesso à internet |
|  | 0205 | Habilitação de serviços multimídia |
|  | 0299 | Habilitação de outros serviços |
| 03. Serviço Medido | 0301 | Serviço Medido - chamadas locais |
|  | 0302 | Serviço Medido - chamadas interurbanas no Estado |
|  | 0303 | Serviço Medido - chamadas interurbanas para fora do Estado |
|  | 0304 | Serviço Medido - chamadas internacionais |
|  | 0305 | Serviço Medido - Números Especiais (0300/0500/0600/0800/etc.) |
|  | 0306 | Serviço Medido - comunicação de dados |
|  | 0307 | Serviço Medido - chamadas originadas em Roaming |
|  | 0308 | Serviço Medido - chamadas recebidas em Roaming |
|  | 0309 | Serviço Medido - adicional de chamada |
|  | 0310 | Serviço Medido - provimento de acesso à Internet |
|  | 0311 | Serviço Medido - pay-per-view (programação TV) |
|  | 0312 | Serviço Medido - Mensagem SMS |
|  | 0313 | Serviço Medido - Mensagem MMS |
|  | 0314 | Serviço Medido - outras mensagens |
|  | 0315 | Serviço Medido - serviços multimídia |
|  | 0399 | Serviço Medido - outros serviços |
| 04. Serviço pré-pago | 0401 | Cartão Telefônico - Telefonia Fixa |
|  | 0402 | Cartão Telefônico - Telefonia Móvel |
|  | 0403 | Cartão de Provimento de acesso à internet |
|  | 0404 | Ficha Telefônica |
|  | 0405 | Recarga de Créditos - Telefonia Fixa |
|  | 0406 | Recarga de Créditos - Telefonia Móvel |
|  | 0407 | Recarga de Créditos - Provimento de acesso à internet |
|  | 0499 | Outras cobranças realizadas de assinantes de plano serviço pré-pago |
| 05. Outros Serviços | 0501 | Serviço Adicional (substituição de número, troca de aparelho, emissão de 2ª via de conta, conta detalhada, etc.) |
|  | 0502 | Serviço Facilidades (identificador de chamadas, caixa postal, transferência temporária, não-perturbe, etc.) |
|  | 0599 | Outros Serviços |
| 06. Energia Elétrica | 0601 | Energia Elétrica – Consumo |
|  | 0602 | Energia Elétrica – Demanda |
|  | 0603 | Energia Elétrica - Serviços (Vistoria de unidade consumidora, Aferição de Medidor, Ligação, Religação, Troca de medidor, etc.) |
|  | 0604 | Energia Elétrica - Encargos Emergenciais |
|  | 0699 | Energia Elétrica – Outros |
| 07. Locação | 0701 | Locação de Aparelho Telefônico |
|  | 0702 | Locação de Aparelho Identificador de Chamadas |
|  | 0703 | Locação de Modem |
|  | 0704 | Locação de Rack |
|  | 0705 | Locação de Sala/Recinto |
|  | 0706 | Locação de Roteador |
|  | 0707 | Locação de Servidor |
|  | 0708 | Locação de Multiplexador |
|  | 0709 | Locação de Decodificador/Conversor |
|  | 0799 | Outras Locações |
| 08. Cobranças | 0801 | Cobrança de Serviços de Terceiros |
|  | 0802 | Cobrança de Seguros |
|  | 0803 | Cobrança de Financiamento de Aparelho/Serviços |
|  | 0804 | Cobrança de Juros de Mora por atraso de pagamento |
|  | 0805 | Cobrança de Multa de Mora por atraso de pagamento |
|  | 0806 | Cobrança de Conta de meses anteriores |
|  | 0899 | Outras Cobranças |
| 09 – Créditos e Redutores | 0901 | Crédito relativo a impugnação de serviços |
|  | 0902 | Crédito referente ajuste de conta |
|  | 0903 | Redutor - Energia Elétrica - IN nº 306/2003 (PIS/COFINS/IRPJ/CSLL) |
|  | 0999 | Outros créditos |

11.6. Recibo de Entrega

11.7.    MD5 – Message Digest 5

11.7.1.    O MD5 é um algoritmo projetado por Ron Rivest da RSA Data
Security e é de domínio público. A função do algoritmo é produzir uma chave de
codificação digital (hash code) de 128 bits, para uma mensagem (cadeia de caracteres) de
entrada de qualquer tamanho. A idéia básica é que a chave de codificação digital
representa de forma compacta a cadeia inicial de forma unívoca. A chave de codificação
digital é utilizada basicamente para a validação da integridade dos dados e assinaturas
digitais."

**Artigo 3º** - A data de início de produção dos efeitos da Portaria CAT-79/03,
prevista para 1º de janeiro de 2004 em seu artigo 10, fica prorrogada para 1º de maio de
2004.

**Artigo 4º** - Esta portaria entra em vigor na data de sua publicação.
