---
titulo: "Comunicado DEAT 1 de 2007"
uf: "SP"
orgao: "Secretaria da Fazenda e Planejamento de SP"
tipo: "Comunicado"
numero: "1"
data:
versao_texto: "texto do Portal de Legislação Tributária da SEFAZ-SP (pode estar consolidado)"
fonte: "https://legislacao.fazenda.sp.gov.br/Paginas/cdeat012007.aspx"
id_fonte: "sefazsp-1505010"
baixado_em: 2026-11-09
modificado_na_fonte: "2019-03-20T18:01:58Z"
---

# Comunicado DEAT 1 de 2007

Comunicado DEAT-1, de 5-1-2007

Comunicado DEAT-1, de 5-1-2007

(D.O.E. de 06-01-2007)

Dispõe sobre as especificações técnicas para geração do arquivo digital a que se refere a [CAT - 36/06](/Paginas/pcat362006.aspx)

O Diretor Executivo da Administração
Tributária, tendo em vista a necessidade de acompanhamento do serviço de relacração
determinado pela Portaria CAT 36/2006, torna público as especificações do arquivo
digital que deverá ser entregue à Secretaria da Fazenda do Estado de São Paulo no dia
10 de cada mês.

**1. REGISTROS:**

1.1. - Tipo: texto não delimitado;

1.2. - Tamanho: variável, acrescidos de CR/LF
(Carriage Return/Line feed) ao final de cada registro;

1.3. - Organização: seqüencial;

1.4. - Codificação: ASCII;

**2. FORMATO DOS CAMPOS:**

2.1. - Numérico (N): sem sinal, não
compactado, alinhado à direita.

2.2. - Alfanumérico (X): alinhado à
esquerda, com as posições não significativas em branco;

**3. PREENCHIMENTOS DOS CAMPOS**

3.1. Numérico: na ausência de
informação, os campos deverão ser preenchidos com zeros;

3.2. Alfanumérico: na ausência de
informação, os campos deverão ser preenchidos com brancos;

**4. ESTRUTURA DO ARQUIVO:**

> 4.1. O arquivo compõe-se dos seguintes tipos
> de registros:
>
> > 4.1.1. Registro tipo 1 - Identificação do
> > fabricante do ECF - registro único;
> >
> > 4.1.2. Registro tipo 2 - Identificação do
> > executante do serviço de relacração - um registro por executante;
> >
> > 4.1.3. Registro tipo 3 - Identificação do
> > contribuinte usuário do ECF - um registro por contribuinte e executante;
> >
> > 4.1.4. Registro tipo 4 - Dados do equipamento
> > relacrado;
> >
> > 4.1.5. Registro tipo 5 - Dados dos
> > dispositivos de segurança instalados no ECF;
> >
> > 4.1.6. Registro tipo 6 - Rodapé - usuário do
> > ECF - um registro para cada registro tipo 3 correspondente;
> >
> > 4.1.7. Registro tipo 7 - Rodapé - executante
> > do serviço de relacração - um registro para cada registro tipo 2 correspondente;
> >
> > 4.1.8. Registro tipo 8 - Rodapé - fabricante
> > do ECF - registro único;

**5. ESTRUTURA DOS REGISTROS:**

**7. TABELA TIPO-LOCAL DE DISPOSITIVO DE
SEGURANÇA**

7.1. 9.1 o campo Tipo-local deve especificar,
simultaneamente, o tipo de dispositivo de segurança utilizado e onde este foi colocado.

7.2. 9.2 Cada campo Tipo-local deve
especificar somente um dispositivo de segurança.

7.3. 9.1 Os campos Tipo-local do registro do
tipo 5, devem ter os seus 6 caracteres preenchidos exclusivamente com os valores da tabela
abaixo:

Valor - Tipo dispositivo

N - Nenhum

E - Etiqueta

L - Lacre

7.4. A contagem da posição deve se iniciar
pela esquerda e o significado de cada uma deve se basear na tabela abaixo

Posição - Local de aposição

> 1 - Software Básico
>
> 2 - Cabo PCF-MF lado PCF
>
> 3 - Cabo PCF-MF lado MF
>
> 4 - PCF-gabinete
>
> 5 - MFD
>
> 6 - Externo

**8. Observações**

8.1. Devem constar do arquivo todos os
equipamentos informados pela Secretaria da Fazenda do Estado de São Paulo no arquivo de
equipamentos autorizados, entregue ao fabricante, devendo os seus dados serem atualizados
a cada entrega.

8.2. Se o executante da relacração for o
próprio fabricante  (mesma Inscrição Estadual), os registros tipos 1 e 2 deverão
possuir os dados do mesmo, ainda que redundantes.

8.3. Todos os equipamentos que ainda não
foram relacrados deverão constar no arquivo com o código "XX", sob um registro
do tipo 2 em que conste a Inscrição Estadual do fabricante de ECF como executante. Neste
caso não deve ser informado o registro tipo 5.

8.4. Este Comunicado define com maior
detalhamento o leiaute previsto no Comunicado DEAT 29/2006, de 5/10/2006, publicado no
D.O. Em 06/10/2006.
