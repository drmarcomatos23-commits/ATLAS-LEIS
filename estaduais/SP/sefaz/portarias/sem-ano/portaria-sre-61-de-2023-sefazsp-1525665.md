---
titulo: "Portaria SRE 61 de 2023"
uf: "SP"
orgao: "Secretaria da Fazenda e Planejamento de SP"
tipo: "Portaria"
numero: "61"
data:
versao_texto: "texto do Portal de Legislação Tributária da SEFAZ-SP (pode estar consolidado)"
fonte: "https://legislacao.fazenda.sp.gov.br/Paginas/Portaria-SRE-61-de-2023.aspx"
id_fonte: "sefazsp-1525665"
baixado_em: 2026-11-08
modificado_na_fonte: "2023-09-19T07:00:25Z"
---

# Portaria SRE 61 de 2023

# ​​PORTARIA SRE 61, DE 12-09​-2023

(DOE 13-09-​​2023)

Altera a Portaria [CA​​T 147/09](/Paginas/pcat1472009.aspx), de 27 de julho de 2009, que
disciplina os procedimentos a serem adotados para fins da
Escrituração Fiscal Digital - EFD pelos contribuintes do ICMS.

​​O SUBSECRETÁRIO DA RECEITA ESTADUAL, tendo em vista
o disposto no artigo 250-A do Regulamento do Imposto sobre
Operações Relativas à Circulação de Mercadorias e sobre Prestações de Serviços de Transporte Interestadual e Intermunicipal
e de Comunicação - RICMS, aprovado pelo Decreto nº 45.490, de
30 de novembro de 2000, expede a seguinte portaria:

**Artigo 1º** - Passam a vigorar, com a redação que se segue,
os itens 5 e 6 das Orientações da Tabela 5.3 do Anexo VIII da
Portaria [CAT 147/09](/Paginas/pcat1472009.aspx)​, de 27 de julho de 2009:

​​“5. Para o cumprimento do disposto nos artigos 214 e 215
do RICMS, o código de ajuste SP90090104, no registro C197,
D197 e C597, será utilizado conforme segue:

DESCR\_COMPL\_AJ: CFOP utilizado no registro C190, D190
e C590 que corresponde às colunas Isentas/Não trib. e Outras;

VL\_ICMS: Valor da coluna Isentas/Não tributadas (RICMS,
artigo 214, § 3º, 7, “a” e artigo 215, § 3º, 5, “a”);

VL\_OUTROS: Valor da coluna Outras (RICMS, artigo 214,
§ 3º, 7, “b” e artigo 215, § 3º, 5, “b”), de acordo com o CST.

5.1 A escrituração dos valores da coluna Isentas/Não
tributadas (RICMS, artigo 214, § 3º, 7, “a” e artigo 215, § 3º,
5, “a”) deverá ser efetuada através do campo VL\_ICMS, para
cada CFOP que conste dos registros C190, D190 e C590 do
documento fiscal, de forma sumarizada para todos os códigos
CST e alíquotas informadas.

5.2 Na ausência de preenchimento do campo VL\_ICMS ou
de informação no campo DESCR\_COMPL\_AJ do registro C197/
C597, com CFOP informado em um registro C190/C590, ou na
falta de entrega do registro C197/C597, o valor da coluna Isentas/Não tributadas resultará da apuração:​​

Valor da coluna Isentas/Não tributadas (CFOP) = função1
(CFOP) + função2 (CFOP), sendo que:

Função1 (CFOP) é o valor calculado, para um determinado
CFOP informado nos registros C190/C590, correspondente a
VL\_OPR - VL\_BC\_ICMS - VL\_ICMS\_ST - VL\_RED\_BC - VL\_IPI
calculado a partir dos registros C190/C590 com CST 30 (Isenta
ou não tributada e com cobrança do ICMS por substituição
tributária), 40 (Isenta) ou 41 (Não tributada);

Função2 (CFOP) corresponde à soma de todos os campos
VL\_RED\_BC para um determinado CFOP informado nos registros
C190/C590;

Se a função1 (CFOP) resultar em valor negativo, será atribuído valor 0 (zero) ao seu resultado.

5.3 Na ausência de preenchimento do campo VL\_ICMS ou
de informação no campo DESCR\_COMPL\_AJ do registro D197,
com CFOP informado em um registro D190, ou na falta de entrega do registro D197, o valor da coluna Isentas/Não tributadas
resultará da apuração:​

Valor da coluna Isentas/Não tributadas (CFOP) = função3
(CFOP) + função4 (CFOP), sendo que:

Função3 (CFOP) é o valor calculado, para um determinado
CFOP informado nos registros D190, correspondente a VL\_OPR -
VL\_BC\_ICMS - VL\_RED\_BC calculado a partir dos registros D190
com CST 30 (Isenta ou não tributada e com cobrança do ICMS
por substituição tributária), 40 (Isenta) ou 41 (Não tributada);

Função4 (CFOP) corresponde à soma de todos os campos
VL\_RED\_BC para um determinado CFOP informado nos registros D190;
Se a função3 (CFOP) resultar em valor negativo, será atribuído valor 0 (zero) ao seu resultado.

​5.4 A escrituração dos valores da coluna Outras (RICMS,
artigo 214, § 3º, 7, “b” e artigo 215, § 3º, 5, “b”) deverá ser efetuada através do campo VL\_OUTROS, para cada CFOP que conste dos registros C190/D190/C590 do documento fiscal, de forma
sumarizada para todos os códigos CST e alíquotas informadas.

5.5 Na ausência de preenchimento do campo VL\_ OUTROS
ou de informação no campo DESCR\_COMPL\_AJ do registro
C197/C597, com CFOP informado em um registro C190/C590,
ou na falta de entrega do registro C197/C597, o valor da coluna
Outras resultará da apuração:​

Valor da coluna Outras (CFOP) = função5 (CFOP), sendo que:
Função5 (CFOP) é o valor calculado, para um determinado
CFOP informado nos registros C190/C590, correspondente a
VL\_OPR - VL\_BC\_ICMS - VL\_ICMS\_ST - VL\_RED\_BC - VL\_IPI
- ICMS ST (substituído) calculado a partir dos registros C190/
C590 com CST diferente de: 30 (Isenta ou não tributada e com
cobrança do ICMS por substituição tributária), 40 (Isenta) ou 41
(Não tributada) e, para o ICMS ST (substituído), obtido a partir
de registro C197/C597, com código de ajuste SP90090278, com
o CFOP correspondente;

​​Se a função5 (CFOP) resultar em valor negativo, será atribuído valor 0 (zero) ao seu resultado.

5.6 Na ausência de preenchimento do campo VL\_OUTROS
ou de informação no campo DESCR\_COMPL\_AJ do registro
D197, com CFOP informado em um registro D190, ou na falta
de entrega do registro D197, o valor da coluna Outras resultará
da apuração:​

Valor da coluna Outras (CFOP) = função6 (CFOP), sendo que:
Função6 (CFOP) é o valor calculado, para um determinado
CFOP informado nos registros D190, correspondente a VL\_OPR
- VL\_BC\_ICMS - VL\_RED\_BC - ICMS ST (substituído) calculado
a partir dos registros D190 com CST diferente de: 30 (Isenta
ou não tributada e com cobrança do ICMS por substituição
tributária), 40 (Isenta) ou 41 (Não tributada) e, para o ICMS ST
(substituído), obtido a partir de registro D197, com código de
ajuste SP90090278, com o CFOP correspondente;

Se a função6 (CFOP) resultar em valor negativo, será atribuído valor 0 (zero) ao seu resultado.

5.7 Uma observação de lançamento fiscal (registro C195/
D195/C595) não deve conter mais de um registro C197/D197/
C597 com código de ajuste SP90090104. Se um documento fiscal contiver dois ou mais CFOPs nos registros C190/D190/C590
que resultem em mais de um registro C197/D197/C597, estes
deverão ser declarados sob lançamentos fiscais individualizados
(C195/D195/C595), com os campos COD\_OBS e TXT\_COMPL
preenchidos com código e descrição, respectivamente, escolhidos pelo declarante.​

6. Para o cumprimento do disposto no artigo 278 do RICMS,
o código de ajuste SP90090278, nos registros C197, D197 e
C597, será utilizado conforme segue:

DESCR\_COMPL\_AJ: CFOP utilizado nos registros C190,
D190 e C590, que corresponde ao valor do ICMS ST na condição
de substituído;

VL\_ICMS: ICMS ST correspondente ao valor, ou à parcela,
de imposto retido considerando o valor da operação (RICMS,
artigo 278, § 1º, 2).

6.1 Para os registros C100, D100 e C500, o valor do ICMS
ST na condição de substituído correspondente às operações dos
CFOPs encontrados nos registros C190, D190 e C590, será considerado 0 (zero) em quaisquer das seguintes situações:

6.1.1 Registros C197, D197 ou C597, com o código de
ajuste SP90090278, em que se constate a ausência de preenchimento do campo VL\_ICMS;

6.1.2 Registros C197, D197 ou C597, com o código de ajuste SP90090278, em que se constate a ausência de informação
no campo DESCR\_COMPL\_AJ ou sem a correspondência com
CFOPs informados em registros C190, D190 ou C590;

6.1.3 Falta de entrega do registro C197, D197 ou C597.

6.2 Uma observação de lançamento fiscal (registro C195/
D195/C595) não deve conter mais de um registro C197/D197/
C597 com código de ajuste SP90090278. Se um documento fiscal contiver dois ou mais CFOPs nos registros C190/D190/C590
que resultem em mais de um registro C197/D197/C597, estes
deverão ser declarados sob lançamentos fiscais individualizados
(C195/D195/C595), com os campos COD\_OBS e TXT\_COMPL
preenchidos com código e descrição, respectivamente, escolhidos pelo declarante.” (NR).

**Artigo 2º** - Esta portaria entra em vigor na data de sua
publicação.​
