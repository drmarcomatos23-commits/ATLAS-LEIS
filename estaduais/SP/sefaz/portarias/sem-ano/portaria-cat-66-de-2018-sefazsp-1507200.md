---
titulo: "Portaria CAT 66 de 2018"
uf: "SP"
orgao: "Secretaria da Fazenda e Planejamento de SP"
tipo: "Portaria"
numero: "66"
data:
versao_texto: "texto do Portal de Legislação Tributária da SEFAZ-SP (pode estar consolidado)"
fonte: "https://legislacao.fazenda.sp.gov.br/Paginas/pcat662018.aspx"
id_fonte: "sefazsp-1507200"
baixado_em: 2026-11-09
modificado_na_fonte: "2022-05-06T20:10:49Z"
---

# Portaria CAT 66 de 2018

Portaria CAT nº 66, de 25-07-2018

Portaria CAT nº 66, de 25-07-2018

(DOE 26-07-2018)

Altera a Portaria [CAT-147/09](/Paginas/pcat1472009.aspx), de 27-07-2009, que disciplina os procedimentos a serem adotados para fins da Escrituração Fiscal Digital - EFD pelos contribuintes do ICMS

O Coordenador da Administração Tributária, tendo em vista o disposto no
artigo 250-A do Regulamento do ICMS - RICMS, aprovado pelo Decreto 45.490, de
30-11-2000, expede a seguinte portaria:

**Artigo 1º** - Ficam acrescentados, com a redação que se segue, os
dispositivos adiante indicados ao Anexo VIII da Portaria [CAT-147/09](/Paginas/pcat1472009.aspx), de
27-07-2009:

I - os códigos SP90090104 e SP90090278 à Tabela 5.3:

“SP90090104 - Valor correspondente à coluna Isentas/Não tributadas e Outras
(artigos 214 e 215 do RICMS/00).

SP90090278 - Valor correspondente ao ICMS ST na condição de substituído
(artigo 278, § 1º, do RICMS/00).” (NR);

II - os itens 5 e 6 às Orientações:

“5. Para o cumprimento do disposto nos artigos 214 e 215 do RICMS, o código
de ajuste SP90090104, no registro C197/D197, será utilizado conforme segue:

DESCR\_COMPL\_AJ CFOP utilizado no registro C190/D190 que corresponde às
colunas Isentas/Não trib. e Outras

VL\_ICMS Valor da coluna Isentas/Não
tributadas (RICMS, artigo 214, § 3º, 7, “a” e artigo 215, § 3º, 5, “a”)

VL\_OUTROS Valor da coluna Outras (RICMS, artigo 214, § 3º, 7, “b” e artigo 215,
§ 3º, 5, “b”), de acordo com o CST

5.1 A escrituração dos valores da coluna Isentas/Não tributadas (RICMS,
artigo 214, § 3º, 7, “a” e artigo 215, § 3º, 5, “a”) deverá ser efetuada através
do campo VL\_ICMS, para cada CFOP que conste dos registros C190/D190 do documento
fiscal, de forma sumarizada para todos os códigos CST e alíquotas informadas.

5.2 Na ausência de preenchimento do campo VL\_ICMS ou de informação no campo
DESCR\_COMPL\_AJ do registro C197, com CFOP informado em um registro C190, ou na
falta de entrega do registro C197, o valor da coluna Isentas/Não tributadas
resultará da apuração:

Valor da coluna Isentas/Não tributadas (CFOP) = função1 (CFOP) + função2
(CFOP), sendo que:

função1 (CFOP) é o valor calculado, para um determinado CFOP informado nos
registros C190, correspondente a VL\_OPR - VL\_BC\_ICMS - VL\_ICMS\_ST - VL\_RED\_BC -
VL\_IPI calculado a partir dos registros C190 com CST 30 (Isenta ou não tributada
e com cobrança do ICMS por substituição tributária), 40 (Isenta) ou 41 (Não
tributada);

função2 (CFOP) corresponde à soma de todos os campos VL\_RED\_BC para um
determinado CFOP informado nos registros C190;

Se a função1 (CFOP) resultar em valor negativo, será atribuído valor 0 (zero)
ao seu resultado.

5.3 Na ausência de preenchimento do campo VL\_ICMS ou de informação no campo
DESCR\_COMPL\_AJ do registro D197, com CFOP informado em um registro D190, ou na
falta de entrega do registro D197, o valor da coluna Isentas/Não tributadas
resultará da apuração:

Valor da coluna Isentas/Não tributadas (CFOP) = função3 (CFOP) + função4
(CFOP), sendo que:

função3 (CFOP) é o valor calculado, para um determinado CFOP informado nos
registros D190, correspondente a VL\_OPR - VL\_BC\_ICMS - VL\_RED\_BC calculado a
partir dos registros D190 com CST 30 (Isenta ou não tributada e com cobrança do
ICMS por substituição tributária), 40 (Isenta) ou 41 (Não tributada);

função4 (CFOP) corresponde à soma de todos os campos VL\_RED\_BC para um
determinado CFOP informado nos registros D190;

Se a função3 (CFOP) resultar em valor negativo, será atribuído valor 0 (zero)
ao seu resultado.

5.4 A escrituração dos valores da coluna Outras (RICMS, artigo 214, § 3º, 7,
“b” e artigo 215, § 3º, 5, “b”) deverá ser efetuada através do campo VL\_OUTROS,
para cada CFOP que conste dos registros C190/D190 do documento fiscal, de forma
sumarizada para todos os códigos CST e alíquotas informadas.

5.5 Na ausência de preenchimento do campo VL\_ OUTROS ou de informação no
campo DESCR\_COMPL\_AJ do registro C197, com CFOP informado em um registro C190,
ou na falta de entrega do registro C197, o valor da coluna Outras resultará da
apuração:

Valor da coluna Outras (CFOP) = função5 (CFOP), sendo que:

função5 (CFOP) é o valor calculado, para um determinado CFOP informado nos
registros C190, correspondente a VL\_OPR - VL\_BC\_ICMS - VL\_ICMS\_ST - VL\_RED\_BC -
VL\_IPI - ICMS ST (substituído) calculado a partir dos registros C190 com CST
diferente de: 30 (Isenta ou não tributada e com cobrança do ICMS por
substituição tributária), 40 (Isenta) ou 41 (Não tributada) e, para o ICMS ST
(substituído), obtido a partir de registro C197, com código de ajuste
SP90090278, com o CFOP correspondente;

Se a função5 (CFOP) resultar em valor negativo, será atribuído valor 0 (zero)
ao seu resultado.

5.6 Na ausência de preenchimento do campo VL\_OUTROS ou de informação no campo
DESCR\_COMPL\_AJ do registro D197, com CFOP informado em um registro D190, ou na
falta de entrega do registro D197, o valor da coluna Outras resultará da
apuração:

Valor da coluna Outras (CFOP) = função6 (CFOP), sendo que:

Função6 (CFOP) é o valor calculado, para um determinado CFOP informado nos
registros D190, correspondente a VL\_OPR - VL\_BC\_ICMS - VL\_RED\_BC - ICMS ST
(substituído) calculado a partir dos registros D190 com CST diferente de: 30
(Isenta ou não tributada e com cobrança do ICMS por substituição tributária), 40
(Isenta) ou 41 (Não tributada) e, para o ICMS ST (substituído), obtido a partir
de registro D197, com código de ajuste SP90090278, com o CFOP correspondente;

Se a função6 (CFOP) resultar em valor negativo, será atribuído valor 0 (zero)
ao seu resultado.

6. Para o cumprimento do disposto no artigo 278 do RICMS, o código de ajuste
SP90090278, nos registros C197 e D197, será utilizado conforme segue:

DESCR\_COMPL\_AJ CFOP utilizado nos registros C190 e D190, que corresponde ao
valor do ICMS ST na condição de substituído

VL\_ICMS ICMS ST correspondente ao
valor, ou à parcela, de imposto retido considerando o valor da operação (RICMS,
artigo 278, § 1º, 2)

6.1 Para os registros C100 e D100, o valor do ICMS ST na
condição de substituído correspondente às operações dos CFOPs encontrados nos
registros C190 e D190, será considerado 0 (zero) em quaisquer das seguintes
situações:

> 6.1.1 registros C197 ou D197, com o código de ajuste SP90090278, em que se
> constate a ausência de preenchimento do campo VL\_ICMS;
>
> 6.1.2 registros C197 ou D197, com o código de ajuste SP90090278, em que se
> constate a ausência de informação no campo DESCR\_COMPL\_AJ ou sem a
> correspondência com CFOPs informados em registros C190 ou D190;
>
> 6.1.3 falta de entrega do registro C197 ou D197.” (NR).

**Artigo 2º** - Esta portaria entra em vigor na data de sua publicação,
produzindo efeitos para a Escrituração Fiscal Digital - EFD correspondente ao
mês de referência julho/2018 e seguintes.
