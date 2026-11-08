---
titulo: "Portaria CAT 99 de 2005"
uf: "SP"
orgao: "Secretaria da Fazenda e Planejamento de SP"
tipo: "Portaria"
numero: "99"
data:
versao_texto: "texto do Portal de Legislação Tributária da SEFAZ-SP (pode estar consolidado)"
fonte: "https://legislacao.fazenda.sp.gov.br/Paginas/pcat992005.aspx"
id_fonte: "sefazsp-1507810"
baixado_em: 2026-11-08
modificado_na_fonte: "2022-05-06T20:21:48Z"
---

# Portaria CAT 99 de 2005

Portaria CAT-99 de 25-10-2005

Portaria CAT - 99, de 25-10-2005

(DOE 26-10-2005)

Altera disposições da Portaria [CAT-17/99](/Paginas/pcat171999.aspx),
de 5/3/1999, que dispõe sobre os procedimentos relacionados com o complemento e o
ressarcimento do imposto retido por sujeição passiva por substituição, e dispõe sobre
procedimentos correlatos

O Coordenador da Administração Tributária, objetivando aperfeiçoar a disciplina
sobre o complemento e o ressarcimento do imposto retido por sujeição passiva por
substituição, prevista nos artigos 263, 269 e 270 do Regulamento do ICMS, aprovado pelo
Decreto 45.490, de 30 de novembro de 2000, e considerando o disposto no Convênio SINIEF
s/nº, de 15-12-70, e na Portaria [CAT-32/96](/Paginas/pcat321996.aspx),
de 28-03-96, expede a seguinte portaria:

**Artigo 1º** - Passa a vigorar com a seguinte redação o "caput" do
artigo 13, da Portaria [CAT-17/99](/Paginas/pcat171999.aspx),
de 5 de março de 1999:

"Artigo 13 - O arquivo magnético do controle de estoque previsto nos artigos 4º
e 5º será gerado e armazenado em conformidade com o gabarito de registro
("layout") e disciplina prevista no Manual de Orientação, anexo a esta
Portaria, vigente na data de entrega do arquivo." (NR).

**Artigo 2º** - Passam a vigorar com a redação que se segue os seguintes itens e
subitens do Manual de Orientação anexo à Portaria [CAT-17/99](/Paginas/pcat171999.aspx),
de 5 de março de 1999:

**I -** o item 6:

"6. REGISTRO TIPO 01: Mestre do Estabelecimento

MESTRE DO ESTABELECIMENTO

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Nº** | **DENOMINAÇÃO DO CAMPO** | **CONTEÚDO** | **TAMANHO** | **POSIÇÃO** |  | **FORMATO** |
| 01 | TIPO | "01" | 2 | 1 | 2 | N |
| 02 | CNPJ | CNPJ DO ESTABELECIMENTO INFORMANTE | 14 | 3 | 16 | N |
| 03 | INSCRIÇÃO ESTADUAL | INSCRIÇÃO ESTADUAL DO ESTABELECIMENTO INFORMANTE | 14 | 17 | 30 | X |
| 04 | CNAE FISCAL | CÓDIGO NACIONAL DE ATIVIDADES ECONÔMICAS - FISCAL | 7 | 31 | 37 | N |
| 05 | NOME DO CONTRIBUINTE | RAZÃO SOCIAL DO CONTRIBUINTE | 35 | 38 | 72 | X |
| 06 | MUNICÍPIO | MUNICÍPIO ONDE ESTÁ DOMICILIADO O ESTABELECIMENTO INFORMANTE | 30 | 73 | 102 | X |
| 07 | UNIDADE DA FEDERAÇÃO | UNIDADE DA FEDERAÇÃO REFERENTE AO MUNICÍPIO | 2 | 103 | 104 | X |
| 08 | DATA INICIAL | A DATA DO INICIO DO PERÍODO REFERENTE ÀS INFORMAÇÕES PRESTADAS | 8 | 105 | 112 | D |
| 09 | DATA FINAL | A DATA DO FIM DO PERÍODO REFERENTE AS INFORMAÇÕES PRESTADAS | 8 | 113 | 120 | D |
| 10 | LOGRADOURO | NOME DO LOGRADOURO | 34 | 121 | 154 | X |
| 11 | NUMERO | NUMERO | 5 | 155 | 159 | N |
| 12 | COMPLEMENTO | COMPLEMENTO (CONJUNTO, SALA, ANDAR ETC) | 22 | 160 | 181 | X |
| 13 | BAIRRO | BAIRRO | 15 | 182 | 196 | X |
| 14 | CEP | CÓDIGO DE ENDEREÇAMENTO POSTAL | 8 | 197 | 204 | N |
| 15 | NOME DO CONTATO | PESSOA RESPONSÁVEL PARA CONTATOS | 28 | 205 | 232 | X |
| 16 | FAX | NUMERO DO FAX DO ESTABELECIMENTO INFORMANTE | 10 | 233 | 242 | N |
| 17 | TELEFONE | NUMERO DO TELEFONE PARA CONTATO | 12 | 243 | 254 | N |
| 18 | E-MAIL | ENDEREÇO ELETRONICO DO CONTRIBUINTE | 50 | 255 | 304 | X |
| 19 | ENDEREÇO WWW | SITE OFICIAL DA EMPRESA (CASO EXISTA) | 40 | 305 | 344 | X |

6.1 - OBSERVAÇÕES

6.1.1 - O arquivo magnético deverá conter apenas um registro deste tipo, e
obrigatoriamente na primeira linha;

6.1.2 - CAMPO 04 - CNAE Fiscal - Deve ser preenchido conforme Código Nacional de
Atividades Econômicas - Fiscal constante na DECA - Declaração Cadastral."(NR);

**II -** o Item 7:

"7. REGISTRO TIPO 02: Movimentação de mercadorias por Nota Fiscal

REGISTRO DE MOVIMENTAÇÃO DE MERCADORIAS POR NOTA FISCAL

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Nº** | **DENOMINAÇÃO DO CAMPO** | **CONTEÚDO** | **TAMANHO** | **POSIÇÃO** |  | **FORMATO** |
| 01 | TIPO | "02" | 02 | 1 | 2 | N |
| 02 | CNPJ | CNPJ DO REMETENTE NAS ENTRADAS E DO DESTINATÁRIO NAS SAIDAS | 14 | 3 | 16 | N |
| 03 | INSCRIÇÃO ESTADUAL | INSCRIÇÃO ESTADUAL DO REMETENTE NAS ENTRADAS E DO DESTINATÁRIO NAS SAÍDAS | 14 | 17 | 30 | N |
| 04 | UNIDADE DA FEDERAÇÃO | SIGLA DA UNIDADE DA FEDERAÇÃO DO REMETENTE NAS ENTRADAS E DO DESTINATÁRIO NAS SAÍDAS | 2 | 31 | 32 | X |
| 05 | DATA DE EMISSÃO/ RECEBIMENTO | DATA DE EMISSÃO NA SAIDA OU RECEBIMENTO NA ENTRADA (DATA CONSTANTE NO DOCUMENTO FISCAL) | 8 | 33 | 40 | D |
| 06 | SÉRIE | SÉRIE DA NOTA FISCAL | 2 | 41 | 42 | X |
| 07 | NUMERO | NUMERO DA NOTA FISCAL | 6 | 43 | 48 | N |
| 08 | CFOP | CÓDIGO FISCAL DA OPERAÇÃO E PRESTAÇÃO | 4 | 49 | 52 | N |
| 09 | CÓDIGO COMPLEMENTAR DA OPERAÇÃO | CÓDIGO COMPLEMENTAR DA OPERAÇÃO CONFORME TABELAS NO SUBITEM 7.1.16 | 2 | 53 | 54 | N |
| 10 | QUANTIDADE | QUANTIDADE DA MERCADORIA (COM 3 DECIMAIS), DE ACORDO COM A UNIDADE DE MEDIDA ESPECIFICADA NO REGISTRO TIPO 04 | 13 | 55 | 67 | N |
| 11 | VALOR TOTAL DA BASE DE CALCULO DA RETENÇÃO | VALOR TOTAL DA BASE DE CALCULO DO ICMS DE RETENÇÃO NA SUBSTITUIÇÃO TRIBUTARIA (COM 2 DECIMAIS) | 13 | 68 | 80 | N |
| 12 | VALOR DE CONFRONTO | BASE DE CALCULO EFETIVA NA SAIDA CONSUMIDOR OU USUÁRIO FINAL OU NA ENTRADA NAS DEMAIS HIPÓTESES (COM 2 DECIMAIS) | 13 | 81 | 93 | N |
| 13 | CÓDIGO DA MERCADORIA | CÓDIGO DA MERCADORIA DO ESTABELECIMENTO INFORMANTE | 14 | 94 | 107 | X |
| 14 | CHASSI | NUMERO DE CHASSI DO VEICULO | 22 | 108 | 129 | X |
| 15 | BASE DE CALCULO DO SUBSTITUTO NAS OPERAÇÕES COM VEÍCULOS OU MOTOS | BASE DE CALCULO DA OPERAÇÃO PRÓPRIA DO SUBSTITUTO (COM 2 DECIMAIS) | 13 | 130 | 142 | N |

**III -** o subitem 7.1.7:

"7.1.7 - CAMPO 09 - Código complementar para identificação do CFOP. Códigos
conforme tabela no subitem 7.1.16"(NR);

**IV -** o subitem 7.1.13.2.7:

"7.1.13.2.7 - CAMPO 08 - Assumirá o valor numérico 2"(NR);

**V -** o subitem 7.1.14.5:

"7.1.14.5 - CAMPO 08 - Assumirá o valor numérico 1"(NR);

**VI -** o subitem 7.1.15:

"7.1.15 - Tabela de CFOPs:

TABELA DE CFOP

(Códigos Fiscais de Operação ou Prestação válidos para substituição tributária
e aplicáveis às finalidades desta Portaria)

7.1.15.1 - Aplicável às operações realizadas até 31/12/2002:

ENTRADAS

CODIGO DESCRIÇÃO DA OPERAÇÃO OU PRESTAÇÃO

1.72 / 2.72 Compra para comercialização em operação sujeita ao regime de
substituição tributária (Convênio de 15.12.70 - SINIEF, Anexo, na redação do Ajuste
SINIEF-6/98, cláusula segunda, II e III). A entrada por compra de mercadoria a ser
comercializada, decorrente de operação sujeita ao regime de substituição tributária.
Também será classificada neste código a entrada de mercadoria em estabelecimento de
cooperativa, quando recebida de cooperado ou de estabelecimento de outra cooperativa.

1.76 / 2.76 Transferência para comercialização em operação sujeita ao regime de
substituição tributária (Convênio de 15.12.70 - SINIEF, Anexo, na redação do Ajuste
SINIEF-6/98, cláusula segunda, II e III). Entrada por transferência de mercadoria a ser
comercializada, decorrente de operação sujeita ao regime de substituição tributária.

1.78 / 2.78 Devolução de venda de mercadoria adquirida e/ou recebida de terceiros em
operação sujeita ao regime de substituição tributária (Convênio de 15.12.70 -
SINIEF, Anexo, na redação do Ajuste SINIEF-6/98, cláusula segunda, II e III). Referente
a venda de mercadoria, cuja saída tenha sido classificada no código 5.73 ou 6.73 - Venda
de mercadoria adquirida e ou recebida de terceiros em operação sujeita ao regime de
substituição tributária, quando destinada a comercialização ou industrialização
subseqüente, ou 5.74 ou 6.74 - Venda de mercadoria adquirida e/ou recebida de terceiros
em operação sujeita ao regime de substituição tributária, quando destinada a
consumidor ou usuário final.

1.99/2.99 Outras entradas ou aquisições de serviços não especificadas. Entrada de
mercadoria, bem ou serviço, não compreendida nos códigos anteriores, qualquer que seja
a natureza jurídica ou econômica da operação ou prestação (não deve ser informado o
subcódigo existente neste item).

SAÍDAS

CODIGO DESCRIÇÃO DA OPERAÇÃO OU PRESTAÇÃO

5.73 / 6.73 Venda de mercadoria adquirida e/ou recebida de terceiros em operação
sujeita ao regime de substituição tributária, quando destinada a comercialização ou
industrialização subseqüente (Convênio de 15.12.70 - SINIEF, Anexo, na redação do
Ajuste SINIEF-6/98, cláusula segunda, II e III). Saída por venda de mercadoria entrada
para industrialização e/ou comercialização, que não tenha sido objeto de qualquer
processo industrial no estabelecimento, em operação sujeita ao regime de substituição
tributária, quando destinada a comercialização ou industrialização subseqüente.
Também será classificada neste código a saída de mercadoria de estabelecimento de
cooperativa, quando destinada a cooperado ou estabelecimento de outra cooperativa.

5.74 / 6.74 Venda de mercadoria adquirida e/ou recebida de terceiros em operação
sujeita ao regime de substituição tributária, quando destinada a consumidor ou usuário
final (Convênio de 15.12.70 - SINIEF, Anexo, na redação do Ajuste SINIEF-6/98,
cláusula segunda, II e III). Saída por venda de mercadoria entrada para
industrialização e/ou comercialização, que não tenha sido objeto de qualquer processo
industrial no estabelecimento, em operação sujeita ao regime de substituição
tributária, quando destinada a consumidor ou usuário final. Também será classificada
neste código a saída de mercadoria de estabelecimento de cooperativa, quando destinada a
cooperado ou estabelecimento de outra cooperativa.

5.76 / 6.76 Transferência de mercadoria adquirida e/ou recebida de terceiros em
operação sujeita ao regime de substituição tributária (Convênio de 15.12.70 -
SINIEF, Anexo, na redação do Ajuste SINIEF-6/98, cláusula segunda, II e III). Saída
por transferência de mercadoria entrada para industrialização e/ou comercialização,
que não tenha sido objeto de qualquer processo industrial no estabelecimento, decorrente
de operação sujeita ao regime de substituição tributária.

5.78 / 6.78 Devolução de compra para comercialização em operação sujeita ao
regime de substituição tributária (Convênio de 15.12.70 - SINIEF, Anexo, na redação
do Ajuste SINIEF-6/98, cláusula segunda, II e III). Referente a mercadoria comprada para
ser comercializada, cuja entrada tenha sido classificada no código 1.72 ou 2.72 - Compra
para comercialização em operação sujeita ao regime de substituição tributária.

5.99/6.99 Outras saídas ou aquisições de serviços não especificadas Saída de
mercadoria, bem ou serviço, não compreendida nos códigos anteriores, qualquer que seja
a natureza jurídica ou econômica da operação ou prestação (não deve ser informado o
subcódigo existente neste item).

7.1.15.2 Aplicável às operações realizadas a partir de 01/01/2003

ENTRADAS

CODIGO DESCRIÇÃO DA OPERAÇÃO OU PRESTAÇÃO

1.403 / 2.403 Compra para comercialização em operação com mercadoria sujeita ao
regime de substituição tributária Classificam-se neste código as compras de
mercadorias a serem comercializadas, decorrentes de operações com mercadorias sujeitas
ao regime de substituição tributária. Também serão classificadas neste código as
compras de mercadorias sujeitas ao regime de substituição tributária em estabelecimento
comercial de cooperativa.

1.409 / 2.409 Transferência para comercialização em operação com mercadoria
sujeita ao regime de substituição tributária Classificam-se neste código as
mercadorias recebidas em transferência de outro estabelecimento da mesma empresa, para
serem comercializadas, decorrentes de operações sujeitas ao regime de substituição
tributária.

1.411 / 2.411 Devolução de venda de mercadoria adquirida ou recebida de terceiros em
operação com mercadoria sujeita ao regime de substituição tributária

Classificam-se neste código as devoluções de vendas de mercadorias adquiridas ou
recebidas de terceiros, cujas saídas tenham sido classificadas como "Venda de
mercadoria adquirida ou recebida de terceiros em operação com mercadoria sujeita ao
regime de substituição tributária".

1.949 /2.949 Outra entrada de mercadoria ou prestação de serviço não especificada
Classificam-se neste código as outras entradas de mercadorias ou prestações de
serviços que não tenham sido especificadas nos códigos anteriores.

SAÍDAS

CODIGO DESCRIÇÃO DA OPERAÇÃO OU PRESTAÇÃO

6.404 Venda de mercadoria sujeita ao regime de substituição tributária, cujo imposto
já tenha sido retido anteriormente. Classificam-se neste código as vendas de mercadorias
sujeitas ao regime de substituição tributária, na condição de substituto tributário,
exclusivamente nas hipóteses em que o imposto já tenha sido retido anteriormente.

5.405 Venda de mercadoria adquirida ou recebida de terceiros em operação com
mercadoria sujeita ao regime de substituição tributária, na condição de contribuinte
substituído. Classificam-se neste código as vendas de mercadorias adquiridas ou
recebidas de terceiros em operação com mercadorias sujeitas ao regime de substituição
tributária, na condição de contribuinte substituído.

5.409 / 6.409 Transferência de mercadoria adquirida ou recebida de terceiros em
operação com mercadoria sujeita ao regime de substituição tributária.

Classificam-se neste código as transferências para outro estabelecimento da mesma
empresa, de mercadorias adquiridas ou recebidas de terceiros que não tenham sido objeto
de qualquer processo industrial no estabelecimento, em operações com mercadorias
sujeitas ao regime de substituição tributária.

5.411 / 6.411 Devolução de compra para comercialização em operação com mercadoria
sujeita ao regime de substituição tributária. Classificam-se neste código as
devoluções de mercadorias adquiridas para serem comercializadas, cujas entradas tenham
sido classificadas como "Compra para comercialização em operação com mercadoria
sujeita ao regime de substituição tributária".

5.929 Lançamento efetuado em decorrência de emissão de documento fiscal relativo a
operação ou prestação também registrada em equipamento Emissor de Cupom Fiscal - ECF.
5.949 / 6.949 Outra saída de mercadoria ou prestação de serviço não especificado.
Classificam-se neste código as outras saídas de mercadorias ou prestações de serviços
que não tenham sido especificados nos códigos anteriores.

7.1.15.3 Aplicável às operações com combustível ou lubrificante realizadas a
partir de 01/01/2004,:

ENTRADAS

CODIGO DESCRIÇÃO DA OPERAÇÃO OU PRESTAÇÃO

1.652 / 2.652 Compra de combustível ou lubrificante para comercialização.
Classificam-se neste código as compras de combustíveis ou lubrificantes a serem
comercializados

1.659 / 2.659 Transferência de combustível e lubrificante para comercialização.
Classificam-se neste código as entradas de combustíveis e lubrificantes recebidas em
transferência de outro estabelecimento da mesma empresa para serem comercializados.

1.661 / 2.661 Devolução de venda de combustível ou lubrificante destinado à
comercialização. Classificam-se neste código as devoluções de vendas de combustíveis
ou lubrificantes, cujas saídas tenham sido classificadas como "Venda de
combustíveis ou lubrificantes para comercialização".

1.662 / 2.662 Devolução de venda de combustível ou lubrificante destinado a
consumidor ou usuário final. Classificam-se neste código as devoluções de  vendas
de combustíveis ou lubrificantes, cujas saídas tenham sido classificadas como
"Venda de combustíveis ou lubrificantes por consumidor ou usuário final".

SAÍDAS

CODIGO DESCRIÇÃO DA OPERAÇÃO OU PRESTAÇÃO

5.655 / 6.655 Venda de combustível ou lubrificante adquirido ou recebido de terceiros
destinado à comercialização. Classificam-se neste código as vendas de combustíveis ou
lubrificantes adquiridos ou recebidos de terceiros destinados à comercialização,
inclusive aquelas decorrentes de encomenda para entrega futura, cujo faturamento tenha
sido classificado no código 5.922 - "Lançamento efetuado a título de simples
faturamento decorrente de venda para entrega futura".

5.656 / 6.656 Venda de combustível ou lubrificante adquirido ou recebido de terceiros
destinado a consumidor ou usuário final. Classificam-se neste código as vendas de
combustíveis ou lubrificantes adquiridos ou recebidos de terceiros destinados a consumo
em processo de industrialização de outros produtos, à prestação de serviços ou a
usuário final, inclusive aquelas decorrentes de encomenda para entrega futura, cujo
faturamento tenha sido classificado no código 5.922 - "Lançamento efetuado a
título de simples faturamento decorrente de venda para entrega futura" .

5.659 / 6.659 Transferência de combustível ou lubrificante adquirido ou recebido de
terceiro. Classificam-se neste código as transferências de combustíveis ou
lubrificantes, adquiridos ou recebidos de terceiros, para outro estabelecimento da mesma
empresa.

5.661 / 6.661 Devolução de compra de combustível ou lubrificante adquirido para
comercialização. Classificam-se neste código as devoluções de compras de
combustíveis ou lubrificantes adquiridos para comercialização, cujas entradas tenham
sido classificadas como "Compra de combustível ou lubrificante para
comercialização".

5.662 / 6.662 Devolução de compra de combustível ou lubrificante adquirido por
consumidor ou usuário final. Classificam-se neste código as devoluções de compras de
combustíveis ou lubrificantes adquiridos para consumo em processo de industrialização
de outros produtos, na prestação de serviços ou por usuário final, cujas entradas
tenham sido classificadas como "Compra de combustível ou lubrificante por consumidor
ou usuário final".

" (NR);

**VII -** o subitem 7.1.16:

"7.1.16 - A tabela abaixo disciplina a utilização de códigos complementares
para cobrir os desdobramentos de CFOPs para as operações:

7.1.16.1 - Aplicável às operações realizadas até 31/12/2002:

TABELA DE CÓDIGOS COMPLEMENTARES DAS OPERAÇÕES

CODIGO DESCRIÇÃO DA OPERAÇÃO OU PRESTAÇÃO

00 O campo assumirá o conteúdo "00" para todas as operações que não as
especificadas a seguir.

01 Deve complementar as operações de devolução de venda (ref. CFOP 1.78), cuja
saída tenha sido classificada no código 5.73.

02 Deve complementar as operações de devolução de venda (ref. CFOP 1.78), cuja
saída tenha sido classificada no código 5.74.

03 Deve complementar as operações de venda destinada a comercialização subseqüente
(ref. CFOP 5.73), venda destinada a consumidor ou usuário final (ref. CFOP 5.74) ou
transferência de mercadoria (ref. CFOP 5.76), quando essas operações próprias
estiverem amparadas por isenção ou não incidência. Este código complementar deve ser
utilizado também nas correspondentes devoluções de venda (ref. CFOP 1.78).

04 Deve complementar as operações de venda destinada a comercialização subseqüente
(ref. CFOP 5.73) ou transferência de mercadoria (ref. CFOP 5.76), quando a operação
subseqüente estiver amparada por isenção ou não incidência, exceto a isenção da
microempresa. Este código complementar deve ser utilizado também nas correspondentes
devoluções de venda (ref. CFOP 1.78).

7.1.16.2 - Aplicável às operações realizadas a partir de 01/01/2003:

TABELA DE CÓDIGOS COMPLEMENTARES DAS OPERAÇÕES

CODIGO DESCRIÇÃO DA OPERAÇÃO OU PRESTAÇÃO

00 O campo assumirá o conteúdo "00" para todas as operações que não as
especificadas a seguir.

01 Deve complementar as operações de devolução de venda, cuja saída tenha sido
para comercialização subseqüente.

02 Deve complementar as operações de devolução de venda, cuja saída tenha sido
destinada a usuário ou consumidor final.

03 Deve complementar as operações de saída destinada a comercialização
subseqüente ou transferência de mercadoria, quando essas operações próprias estiverem
amparadas por isenção ou não incidência. Este código complementar deve ser utilizado
também nas correspondentes devoluções de venda.

04 Deve complementar as operações de saída destinada a consumidor ou usuário final,
quando essas operações próprias estiverem amparadas por isenção ou não incidência.
Este código complementar deve ser utilizado também nas correspondentes devoluções de
venda.

05 Deve complementar as saídas de mercadorias adquiridas ou recebidas de terceiros em
operação sujeita ao regime de substituição tributária, na condição de contribuinte
substituído, cuja saída tenha sido destinada à comercialização subseqüente ou
transferência de mercadoria, quando a operação subseqüente estiver amparada por
isenção ou não incidência, exceto a isenção da microempresa. Este código
complementar deve ser utilizado também nas correspondentes devoluções de venda.

06 Deve complementar as operações de saída de mercadorias adquiridas ou recebidas de
terceiros em operação sujeita ao regime de substituição tributária, na condição de
contribuinte substituído, cuja saída tenha sido destinada à comercialização
subseqüente.

07 Deve complementar o lançamento efetuado em decorrência de emissão de documento
fiscal relativo à operação ou prestação também registrada em equipamento Emissor de
Cupom Fiscal - ECF, quando a saída destinar-se a contribuintes do imposto e a
comercialização subseqüente. "(NR);

**VIII -** o subitem 8.3.1.6:

"8.3.1.6 - CAMPO 08 - Deve ser preenchido com o código da mercadoria, em
conformidade com o Registro Tipo 04"(NR);

**IX -** o subitem 9.1.5:

"9.1.5 - Deve haver, obrigatoriamente, total correspondência entre os códigos de
mercadorias aqui informados com os apresentados nos registros "Tipo 02" e
"Tipo 03 - Mercadoria" desta portaria bem como com o código de
mercadoria\*produto informado no arquivo magnético regido pela Portaria [CAT-32/96](/Paginas/pcat321996.aspx),
de 28 de março de 1996."(NR);

**Artigo 3º** - Fica acrescentado o subitem 7.1.17 ao Manual de Orientação anexo
à Portaria [CAT-17/99](/Paginas/pcat171999.aspx),
de 5 de março de 1999, com a seguinte redação:

"7.1.17 - Toda Nota Fiscal emitida em substituição a um ou mais Cupons Fiscais
(conforme autorizado pela legislação) deve ser informada nos registros "Tipo
2" com os valores que nela constem, devendo ser gerado, no mínimo, um registro
"Tipo 2" para cada tipo de mercadoria."

**Artigo 4º** - Esta portaria entra em vigor na data de sua publicação.
