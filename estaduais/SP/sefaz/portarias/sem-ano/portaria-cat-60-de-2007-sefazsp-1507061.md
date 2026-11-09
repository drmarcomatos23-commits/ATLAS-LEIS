---
titulo: "Portaria CAT 60 de 2007"
uf: "SP"
orgao: "Secretaria da Fazenda e Planejamento de SP"
tipo: "Portaria"
numero: "60"
data:
versao_texto: "texto do Portal de Legislação Tributária da SEFAZ-SP (pode estar consolidado)"
fonte: "https://legislacao.fazenda.sp.gov.br/Paginas/pcat602007.aspx"
id_fonte: "sefazsp-1507061"
baixado_em: 2026-11-09
modificado_na_fonte: "2022-05-06T20:08:19Z"
---

# Portaria CAT 60 de 2007

PORTARIA CAT- 60, de 28-6-2007

PORTARIA CAT- 60, de 28-6-2007

(DOE 29/06/2007)

Altera a Portaria [CAT-52/07](/Paginas/pcat522007.aspx), de 6-6-2007, que dispõe sobre geração e guarda de arquivo digital por contribuinte usuário de equipamento Emissor de Cupom Fiscal - ECF.

O Coordenador da Administração Tributária, tendo em vista o disposto
no artigo 251 do Regulamento do Imposto sobre Operações Relativas à Circulação de
Mercadorias e sobre Prestações de Serviços de Transporte Interestadual e Intermunicipal
e de Comunicação - RICMS, aprovado pelo Decreto n° 45.490, de 30 de novembro de 2000,
expede a seguinte portaria:

**Artigo 1° -** Passam a vigorar com a redação que se segue os
dispositivos adiante indicados da Portaria [CAT-52/07](/Paginas/pcat522007.aspx), de 6 de junho de 2007:

**I** - o item 3 do parágrafo único do artigo 2°:

“3 - deverá ser aplicada a função unidirecional MD5 - Message
Digest n° 5, uma única vez, em todo o arquivo digital, com exceção do registro EAD,
para fins de gerar um código que garanta a integridade do arquivo, o qual deverá ser
assinado digitalmente, mediante uso do algoritmo RSA de chave pública de 1024 bits, e
informado no registro EAD;” (NR);

**II** - o Anexo I:

ANEXO I (da Portaria [CAT-52/07](/Paginas/pcat522007.aspx) - versão 01.00.00)

1 - REGISTROS:

1.1 - Tipo: texto não delimitado;

1.2 - Tamanho: variável, acrescidos de CR/LF (Carriage Return/Line
feed) ao final de cada registro;

1.3 - Organização: seqüencial;

1.4 - Codificação: ASCII;

2 - FORMATO DOS CAMPOS:

2.1 - Numérico (N): sem sinal, não compactado, alinhado à direita,
suprimidos a vírgula e os pontos decimais, com as posições não significativas zeradas;

2.2 - Alfanumérico (X): alinhado à esquerda, com as posições não
significativas em branco;

2.3 - Data (D): somente os algarismos da data, no formato (AAAAMMDD);

2.4 - Hora (H): somente os algarismos da hora, no formato (HHMMSS);

3 - PREENCHIMENTOS DOS CAMPOS

3.1 - Numérico: na ausência de informação, os campos deverão ser preenchidos com
zeros;

3.2 - Alfanumérico: na ausência de informação, os campos deverão ser preenchidos
com brancos;

3.3 - Origem do dado: Memória Fiscal (MF), Memória de Fita-detalhe (MFD), Memória de
Trabalho (MT), Redução Z (imagem de dados codificados impressa de acordo com o disposto
na alínea "d" do inciso II da cláusula terceira do Convênio ICMS 85/01 de 28
de setembro de 2001);

3.4 - Data: na ausência de informação, os campos deverão ser preenchidos com
brancos;

3.5 - Hora: na ausência de informação, os campos deverão ser preenchidos com
brancos.

4 - ESTRUTURA DO ARQUIVO:

4.1 - O arquivo compõe-se dos seguintes tipos de registros:

4.1.1- Registro tipo E00 – Identificação da Software House.

4.1.2 - Registro tipo E01 – Identificação do ECF;

4.1.3 - Registro tipo E02 – Identificação do atual contribuinte usuário do ECF;

4.1.4 - Registro tipo E12 – Relação de reduções Z;

4.1.5 - Registro tipo E13 – Detalhe da Redução Z;

4.1.6 - Registro tipo E14 – Cupom Fiscal, Nota Fiscal de Venda a Consumidor ou
Bilhete de Passagem;

4.1.7 - Registro tipo E15 – Detalhe do Cupom Fiscal, da Nota Fiscal de Venda a
Consumidor ou do Bilhete de Passagem;

4.1.8 - Registro tipo E16 – Demais documentos emitidos pelo ECF.

4.1.9 - Registro tipo E21 – Detalhe do Cupom Fiscal e Documento Não Fiscal –
Meio de Pagamento

4.1.10 - Registro EAD – Assinatura digital.

5 - MONTAGEM DO ARQUIVO:

5.1 - O conjunto de registros que compõem o arquivo obedecerá a ordem
indicada no campo “Tipo de Registro” da tabela abaixo, e serão classificados de
acordo com o campo “Classificação” da referida tabela.

|  |  |  |  |
| --- | --- | --- | --- |
| Tipo de Registro | Nome do Registro | Classificação | |
| Denominação dos Campos de Classificação | A/D \* |
| E00 | Identificação da Software House | 1º registro (único) | - |
| E01 | Identificação do ECF | 2º registro (único) | ---------- |
| E02 | Identificação do atual contribuinte usuário do ECF | 3º registro (único) | ---------- |
| E12 | Relação de Reduções Z | Nº de fabricação Modelo  Nº do usuário  CRZ  CRO | A  A  A  A  A |
| E13 | Detalhe da Redução Z | Nº de fabricação Modelo  Nº do usuário  CRZ  Totalizador | A  A  A  A  A |
| E14 | Cupom Fiscal, Nota Fiscal de Venda a Consumidor ou Bilhete de Passagem | Nº de fabricação Modelo  Nº do usuário  CCF, CVC ou CBP | A  A  A  A |
| E15 | Detalhe do Cupom Fiscal, Nota Fiscal de Venda a Consumidor ou Bilhete de Passagem | Nº de fabricação Modelo  Nº do usuário  CCF, CVC ou CBP  Nº do item | A  A  A  A  A |
| E16 | Demais documentos emitidos pelo ECF | Nº de fabricação Modelo  Nº do usuário  COO | A  A  A  A |
| E21 | Detalhe do Cupom Fiscal e Documento Não Fiscal – Meio de Pagamento | Nº de fabricação Modelo  Nº do usuário  COO, GNF ou CCF  Meio de Pagamento | A  A  A  A  A |
| EAD | Assinatura digital | Último registro (único) | - |

\* A indicação “A/D” significa ascendente/descendente

6 - ESTRUTURA DOS REGISTROS:

6.1 - REGISTRO TIPO E00 – IDENTIFICAÇÃO DA SOFTWARE HOUSE

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Nº | Denominação do Campo | Conteúdo | Tamanho | Posição | | Formato |
| 1 | Tipo | "E00" | 3 | 1 | 3 | X |
| 2 | Número de fabricação | Número de fabricação do ECF | 20 | 4 | 23 | X |
| 3 | MF adicional | Letra indicativa de MF adicional | 1 | 24 | 24 | X |
| 4 | Número do usuário | Número de ordem do usuário do ECF | 2 | 25 | 26 | N |
| 5 | Tipo de ECF | Tipo de ECF | 7 | 27 | 33 | X |
| 6 | Marca do ECF | Marca do ECF | 20 | 34 | 53 | X |
| 7 | Modelo | Modelo do ECF | 20 | 54 | 73 | X |
| 8 | COO | Nº do Contador de Ordem de Operação relativo à troca de Aplicativo | 6 | 74 | 79 | N |
| 9 | Número do Aplicativo | Número de Ordem do Aplicativo | 2 | 80 | 81 | N |
| 10 | CNPJ/CPF: | CNPJ/CPF da Software House ou Desenvolvedor Autônomo | 14 | 82 | 95 | N |
| 11 | I.E: | I.E: da Software House | 14 | 96 | 109 | N |
| 12 | I.M: | I.M: da Software House | 14 | 110 | 123 | N |
| 13 | Nome da Software House | Nome comercial (razão social / denominação) do Software House | 40 | 124 | 163 | X |
| 14 | Nome do Aplicativo | Nome do Aplicativo | 40 | 164 | 203 | X |
| 15 | Versão do Aplicativo | Versão do Aplicativo | 10 | 204 | 213 | X |
| 16 | Linha 01 | Dados do Programa Aplicativo | 42 | 214 | 255 | X |
| 17 | Linha 02 | Dados do Programa Aplicativo | 42 | 256 | 297 | X |

6.1.1 - Observações

6.1.1.1 - Campo 04: O número do usuário deverá ser iniciado por 01 para o primeiro
usuário cadastrado na MF, incrementado de uma unidade para os demais usuários, se for o
caso.

6.1.1.2 - Campo 10: Deverá ser informado o número do CNPJ caso o desenvolvedor do
PAF-ECF seja pessoa jurídica, ou número do CPF no caso de desenvolvedor autônomo.

6.1.1.3 - Campos 8, 9, 16 e 17 devem ser informados em branco ou zerados, conforme seu
formato.

6.2 - REGISTRO TIPO E01 - IDENTIFICAÇÃO DO ECF

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Nº | Denominação do Campo | Conteúdo | Tamanho | Posição | | Formato |
| 01 | Tipo do registro | "E01" | 03 | 1 | 3 | X |
| 02 | Número de fabricação | Nº de fabricação do ECF | 20 | 4 | 23 | X |
| 03 | MF adicional | Letra indicativa de MF adicional | 01 | 24 | 24 | X |
| 04 | Tipo do ECF | Tipo do ECF | 07 | 25 | 31 | X |
| 05 | Marca | Marca do ECF | 20 | 32 | 51 | X |
| 06 | Modelo | Modelo do ECF | 20 | 52 | 71 | X |
| 07 | Versão do SB | Versão atual do Software Básico do ECF gravada na MF | 10 | 72 | 81 | X |
| 08 | Data da gravação do SB | Data da gravação na MF da versão do SB a que se refere o campo 07 | 08 | 82 | 89 | D |
| 09 | Hora da gravação do SB | Hora da gravação na MF da versão do SB a que se refere o campo 07 | 06 | 90 | 95 | H |
| 10 | Número Seqüencial do ECF | Nº de ordem seqüencial do ECF no estabelecimento usuário | 03 | 96 | 98 | N |
| 11 | CNPJ do usuário | CNPJ do estabelecimento usuário do ECF | 14 | 99 | 112 | N |
| 12 | Comando de geração | Código do comando utilizado para gerar o arquivo, conforme tabela abaixo | 03 | 113 | 115 | X |
| 13 | CRZ inicial | Contador de Reduções Z do início do período a ser capturado | 06 | 116 | 121 | N |
| 14 | CRZ final | Contador de Reduções Z do final do período a ser capturado | 06 | 122 | 127 | N |
| 15 | Data Inicial | Data do Início do período a ser capturado | 08 | 128 | 135 | D |
| 16 | Data final | Data do fim do período a ser capturado | 08 | 136 | 143 | D |
| 17 | Versão da biblioteca | Versão da biblioteca do fabricante do ECF geradora deste arquivo | 08 | 144 | 151 | X |
| 18 | Versão do Ato/COTEPE | Versão do Ato/COTEPE | 15 | 152 | 166 | X |

6.2.1 - OBSERVAÇÕES:

6.2.1.1 - Deve ser criado somente um registro tipo E01 para cada
arquivo;

6.2.1.2 - Campo 11: Informar somente os caracteres relativos aos
dígitos do número, sem máscaras de edição;

6.2.1.5 - Campo 12: Informar o código do comando a partir do qual o
programa aplicativo gerou o arquivo, conforme a tabela abaixo:

|  |  |
| --- | --- |
| Função/Comando | Código |
| Geração do arquivo a partir de biblioteca de comandos do fabricante de ECF | RFD |
| Geração do arquivo a partir de PAF-ECF | APL |
| Geração do arquivo por outro meio que não os especificados anteriormente | ALT |

6.2.1.6 - Campo 13 ao Campo 16: Deverão ser informados valores
gravados nas memórias, dentro do intervalo mencionado.

6.2.1.7 - Campo 17: Deve ser preenchido com o formato NN.NN.NN, sendo:

a) o primeiro e o segundo dígitos devem ser incrementados de uma
unidade, a partir do valor inicial 01 (zero um), sempre que houver atualização da
versão por motivo de mudança na legislação;

b) o terceiro e o quarto dígitos devem ser incrementados de uma
unidade, a partir do valor inicial 00 (zero zero), sempre que houver atualização da
versão por motivo de correção de defeito;

c) os dois últimos dígitos podem ser utilizados livremente, a partir
do valor inicial 00 (zero zero), excluídas as situações previstas nas alíneas
anteriores;

6.2.1.8 - Campo 18: Deve ser preenchido com o formato PC5207 NN.NN.NN,
onde NN.NN.NN é o número indicado na Portaria CAT de alteração da Portaria CAT 52/07,
em razão de:

a) o primeiro e o segundo dígitos devem ser incrementados de uma
unidade, a partir do valor inicial 01 (zero um), sempre que houver atualização da
versão por motivo de mudança na legislação;

b) o terceiro e o quarto dígitos devem ser incrementados de uma
unidade, a partir do valor inicial 00 (zero zero), sempre que houver atualização da
versão por motivo de correção de defeito;

c) os dois últimos dígitos podem ser utilizados livremente, a partir
do valor inicial 00 (zero zero), excluídas as situações previstas nas alíneas
anteriores;

6.3 - REGISTRO TIPO E02 – IDENTIFICAÇÃO DO ATUAL CONTRIBUINTE USUÁRIO DO ECF

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Nº | Denominação do Campo | Conteúdo | Tamanho | Posição | | Formato |
| 01 | Tipo | "E02" | 03 | 1 | 3 | X |
| 02 | Número de fabricação | Nº de fabricação do ECF | 20 | 4 | 23 | X |
| 03 | MF adicional | Letra indicativa de MF adicional | 01 | 24 | 24 | X |
| 04 | Modelo | Modelo do ECF | 20 | 25 | 44 | X |
| 05 | CNPJ | CNPJ do estabelecimento usuário do ECF | 14 | 45 | 58 | N |
| 06 | Inscrição Estadual | Inscrição Estadual do estabelecimento usuário | 14 | 59 | 72 | X |
| 07 | Nome do Contribuinte | Nome comercial (razão social / denominação) do contribuinte usuário do ECF | 40 | 73 | 112 | X |
| 08 | Endereço | Endereço do estabelecimento usuário do ECF | 120 | 113 | 232 | X |
| 09 | Data do cadastro | Data do cadastro do usuário no ECF | 08 | 233 | 240 | D |
| 10 | Hora do cadastro | Hora do cadastro do usuário no ECF | 06 | 241 | 246 | H |
| 11 | CRO (Contador de Reinício de Operação) | Valor do CRO relativo ao cadastro do usuário no ECF | 06 | 247 | 252 | N |
| 12 | GT (Totalizador Geral) | Valor acumulado no GT, com duas casas decimais. | 18 | 253 | 270 | N |
| 13 | Número do usuário | Nº de ordem do usuário do ECF | 02 | 271 | 272 | N |

6.3.1 - OBSERVAÇÕES:

6.3.1.1 - Deve ser criado somente um registro tipo E02 para cada
arquivo, contendo os dados relativos ao atual estabelecimento usuário do ECF;

6.3.1.2 - Campos 05 e 06: Informar somente os caracteres relativos aos
dígitos do número, sem máscaras de edição;

6.3.1.3 - Campo 07: Deverá conter os primeiros 40 (quarenta)
caracteres do nome do contribuinte usuário do ECF;

6.3.1.4 - Campo 08: Deverá conter os primeiros 120 (cento e vinte)
caracteres do endereço do estabelecimento usuário do ECF;

6.3.1.6 - Campo 13: O número do usuário deverá ser iniciado por 01
para o primeiro usuário cadastrado na MF, incrementado de uma unidade para os demais
usuários, se for o caso.

6.4 - REGISTRO TIPO E12 - RELAÇÃO DE REDUÇÕES Z

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Nº | Denominação do Campo | Conteúdo | Tamanho | Posição | | Formato |
| 01 | Tipo | "E12" | 03 | 1 | 3 | X |
| 02 | Número de fabricação | Nº de fabricação do ECF | 20 | 4 | 23 | X |
| 03 | MF adicional | Letra indicativa de MF adicional | 01 | 24 | 24 | X |
| 04 | Modelo | Modelo do ECF | 20 | 25 | 44 | X |
| 05 | Número do usuário | Nº de ordem do usuário do ECF relativo à respectiva Redução Z | 02 | 45 | 46 | N |
| 06 | CRZ | Nº do Contador de Redução Z relativo à respectiva redução | 06 | 47 | 52 | N |
| 07 | COO | Nº do Contador de Ordem de Operação relativo à respectiva Redução Z | 06 | 53 | 58 | N |
| 08 | CRO | Nº do Contador de Reinício de Operação relativo à respectiva Redução Z | 06 | 59 | 64 | N |
| 09 | Data do movimento | Data das operações relativas à respectiva Redução Z | 08 | 65 | 72 | D |
| 10 | Data de emissão | Data de emissão da Redução Z | 08 | 73 | 80 | D |
| 11 | Hora de emissão | Hora de emissão da Redução Z | 06 | 81 | 86 | H |
| 12 | Venda Bruta Diária | Valor acumulado neste totalizador relativo à respectiva Redução Z, com duas casas decimais. | 14 | 87 | 100 | N |
| 13 | Incidência de Desconto ISSQN | Informar "S" ou "N", conforme tenha ocorrido ou não,a parametrização para o desconto em ISSQN | 01 | 101 | 101 | X |

6.4.1 - OBSERVAÇÕES:

6.4.1.1 - Deve ser criado um registro tipo E12 para cada Redução Z emitida pelo ECF;

6.4.1.2 - CAMPO 07: informar somente no caso de ECF homologado ou registrado com base
nos Convênios ICMS 50/00 ou 85/01; nos demais casos, preencher com zeros;

6.4.1.3 - Campo 08: o CRO informado deve refletir a posição deste contador no momento
da emissão da respectiva Redução Z.

6.4.1.4 - Campo 13: Deverá ser preenchido com "S", no caso de incidir
desconto no totalizador de ISSQN ou "N", no caso se não incidir.

6.5 - REGISTRO TIPO E13 - DETALHE DA REDUÇÃO Z

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Nº | Denominação do Campo | Conteúdo | Tamanho | Posição | | Formato |
| 01 | Tipo | "E13" | 03 | 1 | 3 | X |
| 02 | Número de fabricação | Nº de fabricação do ECF | 20 | 4 | 23 | X |
| 03 | MF adicional | Letra indicativa de MF adicional | 01 | 24 | 24 | X |
| 04 | Modelo | Modelo do ECF | 20 | 25 | 44 | X |
| 05 | Número do usuário | Nº de ordem do usuário do ECF | 02 | 45 | 46 | N |
| 06 | CRZ | Nº do Contador de Redução Z relativo à respectiva redução | 06 | 47 | 52 | N |
| 07 | Totalizador Parcial | Código do totalizador conforme tabela abaixo | 07 | 53 | 59 | X |
| 08 | Valor acumulado | Valor acumulado no totalizador, relativo à respectiva Redução Z, com duas casas decimais. | 13 | 60 | 72 | N |

6.5.1 - OBSERVAÇÕES:

6.5.1.1 - Deve ser criado um registro tipo E13 para cada totalizador
parcial identificado na tabela abaixo e constante na Redução Z emitida pelo ECF;

6.5.1.2 - Campo 07: Tabela de Códigos dos Totalizadores Parciais:

|  |  |  |
| --- | --- | --- |
| Código | Nome do Totalizador | Conteúdo do Totalizador |
| xxT*nnnn* | Tributado ICMS | Valores de operações tributadas pelo ICMS, onde “xx” representa o número seqüencial do totalizador cadastrado no ECF e “*nnnn”* representa a alíquota efetiva do imposto com duas casas decimais. Exemplo: 01T1800 (totalizador 01 com alíquota de18,00% de ICMS) |
| xxS*nnnn* | Tributado ISSQN | Valores de operações tributadas pelo ISSQN, onde “xx” representa o número seqüencial do totalizador cadastrado no ECF e “*nnnn”* representa a alíquota efetiva do imposto com duas casas decimais. Exemplo: 02S0500 (totalizador 02 com alíquota de 5,00% de ISSQN) |
| F*n* | Substituição Tributária – ICMS | Valores de operações sujeitas ao ICMS, tributadas por Substituição Tributária, onde “*n”* representa o número do totalizador. |
| I*n* | Isento – ICMS | Valores de operações Isentas do ICMS, onde “*n”* representa o número do totalizador. |
| N*n* | Não-incidência – ICMS | Valores de operações com Não Incidência do ICMS, onde “*n”* representa o número do totalizador. |
| FS*n* | Substituição Tributária – ISSQN | Valores de operações sujeitas ao ISSQN, tributadas por Substituição Tributária, onde “*n”* representa o número do totalizador. |
| Is*n* | Isento – ISSQN | Valores de operações Isentas do ISSQN, onde “*n”* representa o número do totalizador. |
| NS*n* | Não-incidência – ISSQN | Valores de operações com Não Incidência do ISSQN, onde “*n”* representa o número do totalizador. |
| OPNF | Operações Não Fiscais | Somatório dos valores acumulados nos totalizadores relativos às Operações Não Fiscais registradas no ECF. |
| DT | Desconto – ICMS | Valores relativos a descontos incidentes sobre operações sujeitas ao ICMS |
| DS | Desconto – ISSQN | Valores relativos a descontos incidentes sobre operações sujeitas ao ISSQN |
| AT | Acréscimo – ICMS | Valores relativos a acréscimos incidentes sobre operações sujeitas ao ICMS |
| AS | Acréscimo – ISSQN | Valores relativos a acréscimos incidentes sobre operações sujeitas ao ISSQN |
| Can-T | Cancelamento – ICMS | Valores das operações sujeitas ao ICMS, canceladas. |
| Can-S | Cancelamento – ISSQN | Valores das operações sujeitas ao ISSQN, canceladas. |

6.6 - REGISTRO TIPO E14 - CUPOM FISCAL, NOTA FISCAL DE VENDA A CONSUMIDOR E BILHETE DE
PASSAGEM

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Nº | Denominação do Campo | Conteúdo | Tamanho | Posição | | Formato |
| 01 | Tipo | "E14" | 03 | 1 | 3 | X |
| 02 | Número de fabricação | Nº de fabricação do ECF | 20 | 4 | 23 | X |
| 03 | MF adicional | Letra indicativa de MF adicional | 01 | 24 | 24 | X |
| 04 | Modelo | Modelo do ECF | 20 | 25 | 44 | X |
| 05 | Número do usuário | Nº de ordem do usuário do ECF | 02 | 45 | 46 | N |
| 06 | CCF, CVC ou CBP, conforme o documento emitido | Nº do contador do respectivo documento emitido | 06 | 47 | 52 | N |
| 07 | COO (Contador de Ordem de Operação) | Nº do COO relativo ao respectivo documento | 06 | 53 | 58 | N |
| 08 | Data de início da emissão | Data de início da emissão do documento | 08 | 59 | 66 | D |
| 09 | Subtotal do Documento | Valor total do documento, com duas casas decimais. | 14 | 67 | 80 | N |
| 10 | Desconto sobre subtotal | Valor do desconto ou Percentual aplicado sobre o valor do subtotal do documento, com duas casas decimais. | 13 | 81 | 93 | N |
| 11 | Indicador do Tipo de Desconto sobre subtotal | Informar “V” para valor monetário ou “P” para percentual | 1 | 94 | 94 | X |
| 12 | Acréscimo sobre subtotal | Valor do acréscimo ou Percentual aplicado sobre o valor do subtotal do documento, com duas casas decimais. | 13 | 95 | 107 | N |
| 13 | Indicador do Tipo de Acréscimo sobre subtotal | Informar “V” para valor monetário ou “P” para percentual | 1 | 108 | 108 | X |
| 14 | Valor Total Líquido | Valor total do Cupom Fiscal após desconto/acréscimo, com duas casas decimais. | 14 | 109 | 122 | N |
| 15 | Indicador de Cancelamento | Informar "S" ou "N", conforme tenha ocorrido ou não, o cancelamento do documento. | 01 | 123 | 123 | X |
| 16 | Cancelamento de Acréscimo no Subtotal | Valor do cancelamento de acréscimo no subtotal | 13 | 124 | 136 | N |
| 17 | Ordem de aplicação de Desconto e Acréscimo | Indicador de ordem de aplicação de desconto/acréscimo em Subtotal. ‘D’ ou ‘A’ caso tenha ocorrido primeiro desconto ou acréscimo, respectivamente | 01 | 137 | 137 | X |
| 18 | Nome do adquirente | Nome do Cliente | 40 | 138 | 177 | X |
| 19 | CPF/CNPJ do adquirente | CPF ou CNPJ do cliente (somente números) | 14 | 178 | 191 | N |

6.6.1 - OBSERVAÇÕES:

6.6.1.1 - Deve ser criado um registro tipo E14 para cada Cupom Fiscal, Nota Fiscal de
Venda a Consumidor ou Bilhete de Passagem emitido pelo ECF; não deve ser criado registro
relativo a documento para cancelamento de documento anterior (vide item 6.14.1.4);

6.6.1.2 - Campo 09: Não informar este campo caso ocorra o cancelamento do Cupom Fiscal
em emissão antes da impressão da totalização do documento.

6.6.1.3 - Campo 14: Não informar este campo caso ocorra o cancelamento do Cupom Fiscal
em emissão antes da impressão da totalização do documento.

6.6.1.4 - Campo 15: caso tenha ocorrido o cancelamento do documento durante sua
emissão ou imediatamente após por meio da emissão de documento para cancelamento de
documento anterior, informar "S", caso contrário, informar "N".

6.7 - REGISTRO TIPO E15 - DETALHE DO CUPOM FISCAL, DA NOTA FISCAL DE VENDA A CONSUMIDOR
OU DO BILHETE DE PASSAGEM

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Nº | Denominação do Campo | Conteúdo | Tamanho | Posição | | Formato |
| 01 | Tipo | "E15" | 03 | 1 | 3 | X |
| 02 | Número de fabricação | Número de fabricação do ECF | 20 | 4 | 23 | X |
| 03 | MF adicional | Letra indicativa de MF adicional | 01 | 24 | 24 | X |
| 04 | Modelo | Modelo do ECF | 20 | 25 | 44 | X |
| 05 | Número do usuário | Número de ordem do usuário do ECF | 02 | 45 | 46 | N |
| 06 | COO (Contador de Ordem de Operação) | Número do COO relativo ao respectivo documento | 06 | 47 | 52 | N |
| 07 | CCF, CVC ou CBP, conforme o documento emitido | Número do contador do respectivo documento emitido | 06 | 53 | 58 | N |
| 08 | Número do item | Número do item registrado no documento | 03 | 59 | 61 | N |
| 09 | Código do Produto ou Serviço | Código do produto ou serviço registrado no documento. | 14 | 62 | 75 | X |
| 10 | Descrição | Descrição do produto ou serviço constante no Cupom Fiscal | 100 | 76 | 175 | X |
| 11 | Quantidade | Quantidade comercializada, sem a separação das casas decimais. | 07 | 176 | 182 | N |
| 12 | Unidade | Unidade de medida | 03 | 183 | 185 | X |
| 13 | Valor unitário | Valor unitário do produto ou serviço, sem a separação das casas decimais. | 08 | 186 | 193 | N |
| 14 | Desconto sobre item | Valor do desconto incidente sobre o valor do item, com duas casas decimais. | 08 | 194 | 201 | N |
| 15 | Acréscimo sobre item | Valor do acréscimo incidente sobre o valor do item, com duas casas decimais. | 08 | 202 | 209 | N |
| 16 | Valor total líquido | Valor total líquido do item, com duas casas decimais. | 14 | 210 | 223 | N |
| 17 | Totalizador parcial | Código do totalizador relativo ao produto ou serviço conforme tabela abaixo. | 07 | 224 | 230 | X |
| 18 | Indicador de cancelamento | Informar "S" ou "N", conforme tenha ocorrido ou não, o cancelamento total do item no documento. Informar "P" quando ocorrer o cancelamento parcial do item. | 01 | 231 | 231 | X |
| 19 | Quantidade cancelada | Quantidade cancelada, no caso de cancelamento parcial de item, sem a separação das casas decimais. | 07 | 232 | 238 | N |
| 20 | Valor cancelado | Valor cancelado, no caso de cancelamento parcial de item. | 13 | 239 | 251 | N |
| 21 | Cancelamento de acréscimo no item | Valor do cancelamento de acréscimo no item | 13 | 252 | 264 | N |
| 22 | Indicador de Arredondamento ou Truncamento (IAT) | Indicador de Arredondamento ou Truncamento relativo à regra de cálculo do valor total líquido do item, sendo‘T’ para truncamento ou ‘A’ para arredondamento. | 01 | 265 | 265 | X |
| 23 | Casas decimais da quantidade | Parâmetro de número de casas decimais da quantidade | 01 | 266 | 266 | N |
| 24 | Casas decimais de valor unitário | Parâmetro de número de casas decimais de valor unitário | 01 | 267 | 267 | N |

6.7.1 - OBSERVAÇÕES:

6.7.1.1 - Deve ser criado um registro tipo E15 para cada item (produto
ou serviço) registrado no documento emitido pelo ECF;

6.7.1.3 - Campo 10 - Deve conter os primeiros cem caracteres da
descrição do produto ou serviço constante no documento;

6.7.1.4 - Campo 17 - Vide tabela do subitem 6.5.1.2;

6.7.1.5 - Campo 19 - Informar a quantidade cancelada somente quando
ocorrer o cancelamento parcial do item;

6.7.1.6 - Campo 20 - Informar o valor cancelado somente quando ocorrer
o cancelamento parcial do item;

6.7.1.7 - Campo 23: Informar o número de casas decimais da quantidade
comercializada;

6.7.1.8 - Campo 24: Informar o número de casas decimais do valor
unitário do produto ou serviço.

6.8 - REGISTRO TIPO E16 - DEMAIS DOCUMENTOS EMITIDOS PELO ECF

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Nº | Denominação do Campo | Conteúdo | Tamanho | Posição | | Formato |
| 01 | Tipo | “E16” | 03 | 1 | 3 | X |
| 02 | Número de fabricação | Número de fabricação do ECF | 20 | 4 | 23 | X |
| 03 | MF Adicional | Letra indicativa de MF adicional | 01 | 24 | 24 | X |
| 04 | Modelo | Modelo do ECF | 20 | 25 | 44 | X |
| 05 | Número do usuário | Número de ordem do usuário do ECF | 02 | 45 | 46 | N |
| 06 | COO (Contador de Ordem de Operação) | Número do COO relativo ao respectivo documento | 06 | 47 | 52 | N |
| 07 | GNF (Contador Geral de Operação Não Fiscal) | Número do GNF relativo ao respectivo documento, quando houver | 06 | 53 | 58 | N |
| 08 | GRG (Contador Geral de Relatório Gerencial) | Número do GRG relativo ao respectivo documento (vide item 6.16.1.4) | 06 | 59 | 64 | N |
| 09 | CDC (Contador de Comprovante de Crédito ou Débito) | Número do CDC relativo ao respectivo documento (vide item 6.16.1.5) | 04 | 65 | 68 | N |
| 10 | CRZ (Contador de Redução Z) | Número do CRZ relativo ao respectivo documento (vide item 6.16.1.6) | 06 | 69 | 74 | N |
| 11 | Denominação | Símbolo referente à denominação do documento fiscal, conforme tabela abaixo | 02 | 75 | 76 | X |
| 12 | Data final de emissão | Data final de emissão | 08 | 77 | 84 | D |
| 13 | Hora final de emissão | Hora final de emissão, no formato hh:mm:ss | 06 | 85 | 90 | H |

6.8.1 - OBSERVAÇÕES:

6.8.1.1 - Deve ser criado um registro tipo E16 para cada documento
emitido, exceto para os documentos fiscais informados no registro tipo E14;

6.8.1.2 - Campo 08 - Informar apenas no caso de Relatório Gerencial;

6.8.1.3 - Campo 09 - Informar apenas no caso de Comprovante Crédito ou
Débito;

6.8.1.4 - Campo 10 - Informar apenas no caso de Redução Z;

6.8.1.5 - Campo 11 - Tabela de símbolos dos demais documentos emitidos
pelo ECF:

|  |  |
| --- | --- |
| Documento | Símbolo |
| Leitura da Memória Fiscal | MF |
| Redução Z | RZ |
| Leitura X | LX |
| Conferência de Mesa | CM |
| Registro de Venda | RV |
| Comprovante de Crédito ou Débito | CC |
| Comprovante Não-Fiscal | CN |
| Comprovante Não-Fiscal Cancelamento | NC |
| Relatório Gerencial | RG |

6.9 - REGISTRO TIPO E21 – DETALHE DO CUPOM FISCAL E DOCUMENTO NÃO FISCAL - MEIO
DE PAGAMENTO

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Nº | Denominação do Campo | Conteúdo | Tamanho | Posição | | Formato |
| 01 | Tipo | "E21" | 03 | 1 | 3 | X |
| 02 | Número de fabricação | Número de fabricação do ECF | 20 | 4 | 23 | X |
| 03 | MF adicional | Letra indicativa de MF adicional | 01 | 24 | 24 | X |
| 04 | Modelo | Modelo do ECF | 20 | 25 | 44 | X |
| 05 | Número do usuário | Número de ordem do usuário do ECF | 02 | 45 | 46 | N |
| 06 | COO (Contador de Ordem de Operação) | Número do COO relativo ao respectivo Cupom Fiscal ou Comprovante Não Fiscal | 06 | 47 | 52 | N |
| 07 | CCF | Número do Contador de Cupom Fiscal relativo ao respectivo Cupom Fiscal emitido | 06 | 53 | 58 | N |
| 08 | GNF | Número do Contador Geral Não Fiscal relativo ao respectivo Comprovante Não Fiscal emitido | 06 | 59 | 64 | N |
| 09 | Meio de pagamento | Descrição do totalizador parcial de meio de pagamento | 15 | 65 | 79 | X |
| 10 | Valor pago | Valor do pagamento efetuado, com duas casas decimais | 13 | 80 | 92 | N |
| 11 | Indicador de estorno | Informar "S" ou "N", conforme tenha ocorrido ou não, o estorno do pagamento, ou “P” para estorno parcial do pagamento | 01 | 93 | 93 | X |
| 12 | Valor estornado | Valor do estorno efetuado, com duas casas decimais | 13 | 94 | 106 | N |

6.9.1 - OBSERVAÇÕES:

6.9.1.1 - Deve ser criado um registro tipo E21 para cada pagamento
efetuado no respectivo Cupom Fiscal ou Comprovante Não Fiscal, inclusive quando houver
posterior estorno do mesmo, podendo resultar em novo registro E21 com o meio de pagamento
efetivado em substituição.

6.10 - REGISTRO TIPO EAD - ASSINATURA DIGITAL

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Nº | Denominação do Campo | Conteúdo | Tamanho | Posição | | Formato |
| 01 | Tipo do registro | "EAD" | 03 | 1 | 3 | X |
| 02 | Assinatura digital | Assinatura do Hash | 256 | 4 | 259 | X |

6.10.1 - OBSERVAÇÕES:

6.10.1.1 - Os seguintes passos devem ser seguidos para gerar a
Assinatura digital:

6.10.1.1.1 - Aplicar a função unidirecional MD5 uma única vez em
todo o arquivo, com exceção do registro EAD. O resultado será um código de 128 bits,
ou 16 caracteres ASCII, correspondendo a um número hexadecimal de 32 dígitos. Deverá
ser utilizado nos cálculos o número hexadecimal, considerando-o como um único bloco.

6.10.1.1.2 - Criar uma chave privada de 1024 bits, equivalente a um
número hexadecimal de 256 dígitos.

6.10.1.1.3 - Criptografar o código hexadecimal gerado no item
6.10.1.1.1, utilizando a chave do item 6.10.1.1.2, pelo algoritmo RSA de chave pública. O
resultado dessa critptografia, um número hexadecimal com até 256 dígitos, deverá ser
informado no campo Assinatura digital.

**III** - o Anexo III:

ANEXO III

|  |  |  |
| --- | --- | --- |
| Marca | Modelo | Código (M) |
| AOKI | AOKI 1E | 1 |
| ASTICK | ASTICK 100 | 1 |
| ASTICK | ASTICK L | 2 |
| BEMATECH | ECF-IF MP-20 FI | 1 |
| BEMATECH | ECF-IF MP-20 FI R | 2 |
| BEMATECH | ECF-IF MP-40 FI | 3 |
| BEMATECH | KIT ECF-IF MP-30 FI | 4 |
| BEMATECH | MP-20 FI DUAL ECF-IF | 5 |
| BEMATECH | MP-20 FI II ECF-IF | 6 |
| BEMATECH | MP-20 FI II R ECF-IF | 7 |
| BEMATECH | MP-40 FI II ECF-IF | 8 |
| BEMATECH | MP-40 FI II R ECF-IF | 9 |
| BEMATECH | MP/20 FI II ECF-IF | A |
| BETHA | BETHA 2E | 1 |
| CHRONOS | CHRONOS-250 1E | 1 |
| CHRONOS | CHRONOS-270 2E | 2 |
| CHRONOS | MULTI-50110 | 3 |
| CORISCO | ECF-IF CT7000-V1 | 1 |
| CORISCO | ECF-IF CT7000V3 | 2 |
| DARUMA AUTOMACAO | ECF-IF FS 500 | 1 |
| DARUMA AUTOMACAO | ECF-IF FS2000 | 2 |
| DARUMA AUTOMACAO | FS-318 | 3 |
| DARUMA AUTOMACAO | FS-345 | 4 |
| DARUMA AUTOMACAO | PRINT PLUS FS-335 | 5 |
| DATAREGIS | 1Q | 1 |
| DATAREGIS | 300-EP | 2 |
| DATAREGIS | 375-EP | 3 |
| DATAREGIS | 950-EP | 4 |
| DATAREGIS | DT-4000 | 5 |
| DATAREGIS | IF/1 | 6 |
| DATAREGIS | IF/1N | 7 |
| DATAREGIS | IF/2 | 8 |
| DIGIARTE | DIGIARTE 1 | 1 |
| DIGIARTE | DIGIARTE 1E | 2 |
| DIGISAT | 1E | 1 |
| DISMAC | 2001-II | 1 |
| EAGLE | PRINTER 2000 ECF-IF | 1 |
| EAGLE | PRINTER 2000 II ECF-IF | 2 |
| EAGLE | PRINTER 2000 II R ECF-IF | 3 |
| EAGLE | PRINTER 2001 ECF-IF | 4 |
| EAGLE | PRINTER 2002 II | 5 |
| EAGLE | PRINTER 2002 II ECF-IF | 6 |
| ELGIN | ECF IF 400 2E | 1 |
| ELGIN | ECF IF 500 1E | 2 |
| GENERAL | ECF-IF GP-2000 | 1 |
| IBM | 4679 3BM | 1 |
| IBM | 4679 3BS | 2 |
| IBM | ECF-IF 4679-3FB | 3 |
| IBM | IB 20 FI II ECF-IF | 4 |
| IBM | IB 40 FI II ECF-IF | 5 |
| IBM | IB-20 FI II R ECF-IF | 6 |
| IONICS | IONICS 1E | 1 |
| ITAUTEC | KIT ECF-IF/1E | 1 |
| ITAUTEC | KIT POS 4000 ECF-IF/1E | 2 |
| ITAUTEC | KIT POS 4000 ECF-IF/3E | 3 |
| ITAUTEC | POS 4000 1E | 4 |
| ITAUTEC | POS 4000 3E | 5 |
| ITAUTEC | POS 4000 ECF-IF/1E | 6 |
| ITAUTEC | POS 4000 ECF-IF/1E BR | 7 |
| ITAUTEC | POS 4000 ECF-IF/3E | 8 |
| ITAUTEC | POS 4000 ECF-IF/3E BR | 9 |
| ITAUTEC | POS ECF IF/2E M | A |
| ITAUTEC | POS4000 ECF-IF/1E II | B |
| ITAUTEC | POS4000 ECF-IF/3E II | C |
| MECAF | ECF 1E-3001 | 1 |
| MECAF | ECF-4002 | 2 |
| MECAF | MECAF COMPACT FCR | 3 |
| NCR | ECF-IF 72EPS-01 | 1 |
| NCR | ECF-IF 72EPS-02 | 2 |
| NCR | ECF-IF-02-01 | 3 |
| NCR | ECF-IF-03-02 | 4 |
| NCR | ECF-IF-7141 | 5 |
| NCR | ECF-IF-7424E2i | 6 |
| PROCOMP | ECF 2001 | 1 |
| PROCOMP | ECF 2002 | 2 |
| PROCOMP | ECF 2011 | 3 |
| PROCOMP | ECF 2023 | 4 |
| QUALID | CASH TOP ECF-IF | 1 |
| QUATRO | EASY APF | 1 |
| QUATRO | EASY IIF | 2 |
| QUATRO | ECF-IF EASY APF | 3 |
| ROBOMARKET | RM 1 | 1 |
| ROR | IF ROR 1E | 1 |
| SCHALTER | D PRINT | 1 |
| SCHALTER | D PRINT ECF | 2 |
| SCHALTER | ECF IF SCFI 1E | 3 |
| SCHALTER | S PRINT | 4 |
| SCHALTER | T PRINT | 5 |
| SCHALTER | T PRINT-ECF | 6 |
| SID | 6417 | 1 |
| SID | SID 6459 | 2 |
| SID | SID 6460 | 3 |
| SIGTRON | FS-318 | 1 |
| SIGTRON | FS-345 | 2 |
| SIGTRON | FS367 | 3 |
| SIGTRON | PRINT PLUS- FS 210 | 4 |
| SIGTRON | PRINT PLUS-FS 100 | 5 |
| SIGTRON | PRINT PLUS-FS 200 | 6 |
| SIGTRON | PRINT PLUS-FS 200 G | 7 |
| SIGTRON | PRINT PLUS-FS 215 | 8 |
| SIGTRON | PRINT PLUS-FS 220 | 9 |
| SIGTRON | PRINT PLUS-FS 300 | A |
| SIGTRON | PRINT PLUS-FS 315 | B |
| SIGTRON | PRINT PLUS-FS 320 | C |
| SIGTRON | PRINT PLUS-FS 335 | D |
| SIGTRON | PRINT PLUS-FS 350 | E |
| SIGTRON | PRINT PLUS-FS 365 | F |
| SIGTRON | PRINT PLUS-FS 370 | G |
| SIGTRON | PRINT PLUS-FS 395 | H |
| SWEDA | IF S-7000 III | 1 |
| SWEDA | IF S-7000I | 2 |
| SWEDA | IF S-7000IE | 3 |
| SWEDA | IF S-7000II | 4 |
| SWEDA | IF S-9000I | 5 |
| SWEDA | IF S-9000IE | 6 |
| SWEDA | IF S-9000II | 7 |
| SWEDA | IF S-9000IIE | 8 |
| SWEDA | IF S-9000IIIE | 9 |
| TRENDS | TRENDS 1.0 E | 1 |
| UNIGRAPH | UN-FI | 1 |
| UNIGRAPH | UN-FI 2E | 2 |
| UNISYS | BR 1002-ECF | 1 |
| UNISYS | BR-20 IF2 ECF-IF | 2 |
| UNISYS | BR-40 IF2 ECF-IF | 3 |
| UNISYS | BR400-IF ECF-IF | 4 |
| UNISYS | BRB 375 ECF-IF | 5 |
| UNISYS | ECF-IF BR401-IF | 6 |
| URANO | ECF-IF URANO/1EFREST | 1 |
| URANO | ECF-IF URANO/2EFCR | 2 |
| URANO | KIT URANO/2EFC | 3 |
| URANO | URANO/1EFC | 4 |
| URANO | URANO/2EFC | 5 |
| URANO | URANO/2EFE | 6 |
| URANO | ZPM/1EF | 7 |
| YANCO | ECF-IF YANCO 8000 | 1 |
| YANCO | ECF-IF YANCO8500 | 2 |
| ZANTHUS | 1e | 1 |
| ZANTHUS | 2E-ECF | 2 |
| ZANTHUS | ECF-IF QZ1000 | 3 |
| ZANTHUS | IZ 11-ECF | 4 |
| ZANTHUS | IZ 21-ECF | 5 |
| ZANTHUS | IZ10-ECF | 6 |
| ZANTHUS | IZ20-ECF | 7 |
| ZANTHUS | IZ22 | 8 |
| ZANTHUS | IZ41-ECF | 9 |
| ZANTHUS | IZ51 | A |
| ZANTHUS | QZ 1001 | B |
| ZANTHUS | QZ1000 | C |
| ZANTHUS | QZ2000 | D |
| ZPM | ZPM/1EF | 1 |
| ZPM | ZPM/2EFC | 2 |

**Artigo 2° -** Esta portaria entra em vigor na data de sua
publicação.
