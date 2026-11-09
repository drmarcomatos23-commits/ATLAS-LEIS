---
titulo: "Portaria CAT 12 de 2006"
uf: "SP"
orgao: "Secretaria da Fazenda e Planejamento de SP"
tipo: "Portaria"
numero: "12"
data:
versao_texto: "texto do Portal de Legislação Tributária da SEFAZ-SP (pode estar consolidado)"
fonte: "https://legislacao.fazenda.sp.gov.br/Paginas/pcat122006.aspx"
id_fonte: "sefazsp-1505619"
baixado_em: 2026-11-09
modificado_na_fonte: "2022-05-06T19:41:28Z"
---

# Portaria CAT 12 de 2006

Portaria CAT-12 de 02-03-2006

Portaria CAT - 12, de 02-03-2006

(DOE de 03-03-2006)

Altera a Portaria
[CAT - 117/05](/Paginas/pcat1172005.aspx), de 16-12-2005, que estabelece disciplina para a prévia
autorização do deferimento do lançamento do imposto incidente na operação interna ou
interestadual que destinar Álcool Etílico Anidro Combustível - AEAC a estabelecimento
do distribuidor de combustíveis, e dispõe sobre procedimentos correlatos

NOTA - V. PORTARIA
[CAT-126/05](/Paginas/pcat1262005.aspx).
               PORTARIA
[CAT-24/07](/Paginas/pcat242007.aspx).

Alteram o conteúdo da Portaria [CAT-117/05](/Paginas/pcat1172005.aspx), de 16-12-2005 (DOE 17-12-2005), que estabelece disciplina para a prévia autorização do diferimento do lançamento do imposto incidente na operação interna ou interestadual que destinar Álcool Etílico Anidro Combustível - AEAC a estabelecimento do distribuidor de combustíveis, e dispõe sobre procedimentos correlatos.

NOTA - V. PORTARIA
[CAT-91/06](/Paginas/pcat912006.aspx), de 17-11-2006 (DOE 18-11-2006), alterada pelas Portarias [CAT-97/06](/Paginas/pcat972006.aspx) e [CAT-23/07](/Paginas/pcat232007.aspx) - Dispõe sobre o registro prévio de operação relativa à circulação de álcool etílico, gasolina automotiva e óleo diesel dos tipos B e D e altera a Portaria CAT 117/05.

O Coordenador da Administração
Tributária, considerando o disposto no artigo [419](/Paginas/art419.aspx) do Regulamento do Imposto sobre
Operações Relativas à Circulação de Mercadorias e sobre Prestações de Serviços de
Transporte Interestadual e Intermunicipal e de Comunicação - RICMS - aprovado pelo
Decreto nº 45.490, de 30 de novembro de 2000, expede a seguinte portaria:

**Artigo 1º** - Passam a vigorar com a
redação que se segue os dispositivos adiante indicados da Portaria [CAT - 117/05](/Paginas/pcat1172005.aspx), de 16 de
dezembro de 2005:

I - o § 3º do artigo 9º:

"§ 3° - Os procedimentos previstos
nos itens 2 a 4 do § 1º poderão ser efetivados por meio de transmissão eletrônica de
dados em lotes de até 250 (duzentas e cinqüenta) operações, observadas as instruções
contidas no Guia do Usuário, que poderá se encontrado no endereço eletrônico
www.fazenda.sp.gov.br/CODIF, e no Anexo único desta portaria." (NR);

II - o Anexo único:

**"Sistema
Combustível – Álcool - Estrutura do arquivo XML**

**Estrutura do arquivo XML de Entrada**

O arquivo XML de entrada possui as
informações que devem ser fornecidas pelos remetentes. Este arquivo será utilizado nos
3 casos identificados abaixo:
> Requisição de autorização:
>
> Utilizado quando o remetente encaminha as
> solicitações de autorização. Neste caso, o conteúdo das "tags" (elementos)
> relativas às autorizações e aos dados de Nota Fiscal estarão vazios.
>
> Quando o sistema receber o arquivo XML com
> este tipo de dado será feito o processamento das informações e será disponibilizado o
> arquivo de saída com o resultado das solicitações. Para cada situação será devolvido
> o código de autorização ou uma mensagem de erro para cada requisição quando for o
> caso.
>
> Registro de Nota Fiscal:
>
> Em um momento posterior à solicitação da
> autorização, o remetente deverá informar as Notas Fiscais relacionadas a cada
> operação autorizada. Na operação em lote deverá ser encaminhado o arquivo que terá a
> mesma formação. A alteração observada é a existência de informação nos campos
> relacionado às Notas Fiscais emitidas.
>
> Requisição de autorização com Nota Fiscal:

> Caso não tenha sido possível gerar o
> arquivo de solicitação de autorização nos casos previstos na legislação, o usuário
> poderá enviar um arquivo solicitando a autorização juntamente com os dados relativos
> às Notas Fiscais de cada item. Estruturalmente, o arquivo encaminhado é o mesmo. Mais
> uma vez, a diferença é que os campos destinados a todas estas informações deverão
> estar preenchidos.

A recepção de um arquivo fora do formato
indicado ou sem as informações necessárias acarretará a recusa do mesmo.

**Schema do arquivo XML de Entrada**

<?xml version="1.0" encoding="utf-8" ?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
xmlns="xsdRequisicao" targetNamespace="xsdRequisicao"
elementFormDefault="qualified">
<xs:element name="requisicaoXml" type="requisicoesXml">
</xs:element>
<xs:complexType name="requisicoesXml" id="requisicoesXml">
<xs:sequence minOccurs="1" maxOccurs="1">
<xs:element name="requisicoes" type="requisicoes" />
</xs:sequence>
</xs:complexType>
<xs:complexType name="requisicoes" id="requisicoes">
<xs:sequence minOccurs="1" maxOccurs="unbounded">
<xs:element name="requisicao" type="requisicao" />
</xs:sequence>
</xs:complexType>
<xs:complexType name="requisicao" id="requisicao">
<xs:sequence minOccurs="1" maxOccurs="1">
<xs:element name="dadosSolicitacao" type="dadosSolicitacao" />
<xs:element name="dadosNF" type="dadosNF" />
</xs:sequence>
<xs:attribute name="idRequisicao" type="idRequisicao"
use="required"></xs:attribute>
</xs:complexType>
<xs:complexType name="dadosSolicitacao" id="dadosSolicitacao">
<xs:sequence>
<xs:element name="dataRequisicao" type="dataRequisicao"
minOccurs="1" maxOccurs="1" />
<xs:element name="remetente" type="cnpj" minOccurs="1"
maxOccurs="1" />
<xs:element name="destinatario" type="cnpj" minOccurs="1"
maxOccurs="1" />
<xs:element name="ufDestinatario" type="uf" minOccurs="1"
maxOccurs="1" />
<xs:element name="codAutorizacao" type="codAutorizacao"
minOccurs="1" maxOccurs="1" />
<xs:element name="volume" type="xs:string" minOccurs="1"
maxOccurs="1" />
</xs:sequence>
</xs:complexType>
<xs:complexType name="dadosNF" id="dadosNF">
<xs:sequence>
<xs:element name="numero" type="nroNF" minOccurs="1"
maxOccurs="1" />
<xs:element name="serie" type="xs:string" minOccurs="1"
maxOccurs="1" />
<xs:element name="dataEmissao" type="dataNF"
minOccurs="1" maxOccurs="1" />
<xs:element name="volumeNF" type="xs:string"
minOccurs="1" maxOccurs="1" />
<xs:element name="valor" type="xs:string" minOccurs="1"
maxOccurs="1" />
</xs:sequence>
</xs:complexType>
<xs:simpleType name="idRequisicao">
<xs:restriction base="xs:positiveInteger">
<xs:pattern value="\d{1,6}" />
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="dataRequisicao">
<xs:restriction base="xs:positiveInteger">
<xs:pattern value="\d{12}" />
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="cnpj">
<xs:restriction base="xs:positiveInteger">
<xs:pattern value="\d{14}" />
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="uf" id="uf">
<xs:restriction base="xs:string">
<xs:enumeration value="AC"></xs:enumeration>
<xs:enumeration value="AL"></xs:enumeration>
<xs:enumeration value="AM"></xs:enumeration>
<xs:enumeration value="AP"></xs:enumeration>
<xs:enumeration value="BA"></xs:enumeration>
<xs:enumeration value="CE"></xs:enumeration>
<xs:enumeration value="DF"></xs:enumeration>
<xs:enumeration value="ES"></xs:enumeration>
<xs:enumeration value="GO"></xs:enumeration>
<xs:enumeration value="MA"></xs:enumeration>
<xs:enumeration value="MG"></xs:enumeration>
<xs:enumeration value="MS"></xs:enumeration>
<xs:enumeration value="MT"></xs:enumeration>
<xs:enumeration value="PA"></xs:enumeration>
<xs:enumeration value="PB"></xs:enumeration>
<xs:enumeration value="PE"></xs:enumeration>
<xs:enumeration value="PI"></xs:enumeration>
<xs:enumeration value="PR"></xs:enumeration>
<xs:enumeration value="RJ"></xs:enumeration>
<xs:enumeration value="RN"></xs:enumeration>
<xs:enumeration value="RO"></xs:enumeration>
<xs:enumeration value="RR"></xs:enumeration>
<xs:enumeration value="RS"></xs:enumeration>
<xs:enumeration value="SC"></xs:enumeration>
<xs:enumeration value="SE"></xs:enumeration>
<xs:enumeration value="SP"></xs:enumeration>
<xs:enumeration value="TO"></xs:enumeration>
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="codAutorizacao" id="codAutorizacao">
<xs:restriction base="xs:string">
<xs:pattern value="\d{0,20}" />
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="nroNF">
<xs:restriction base="xs:string">
<xs:pattern value="\d{0,9}" />
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="dataNF">
<xs:restriction base="xs:string">
<xs:pattern value="\d{0,8}" />
</xs:restriction>
</xs:simpleType>
</xs:schema>

**Estrutura do arquivo XML de Entrada**

|  |  |  |
| --- | --- | --- |
| **Campo** | **Descrição** | **Obrigatório** |
| xmlns | Este atributo identifica o schema associado ao arquivo XML. O valor deste campo é xsdRequisicao. | Sim |
| idRequisicao | Este atributo identifica a requisição de autorização unicamente, não podendo assumir um mesmo valor na mesma data (dd/mm/aaaa). O intervalo de valores que este atributo pode assumir varia entre 1 e 999.999. | Sim |
| dataRequisicao | Este elemento identifica a data na qual a requisição está sendo feita (data atual). O formato deste campo é aaaammddhhMM, onde: - aaaa: ano;  - mm: mês;  - dd: dia;  - hh: horas;  - MM: minutos. | Sim |
| remetente | Este elemento identifica o CNPJ do remetente da requisição. O valor deste campo deve ser informado sem pontuação, apenas os 14 dígitos que compõem o CNPJ. | Sim |
| destinatario | Este elemento identifica o CNPJ do destinatário da requisição. O valor deste campo deve ser informado sem pontuação, apenas os 14 dígitos que compõem o CNPJ. | Sim |
| ufDestinatario | Este elemento identifica a UF na qual o destinatário da requisição está localizado. Os possíveis valores para este campo são: AC, AL, AM, AP, BA, CE, DF, ES, GO, MA, MG, MS, MT, PA, PB, PE, PI, PR, RJ, RN, RO, RR, RS, SC, SE, SP, TO. | Sim |
| codAutorizacao | Este elemento identifica o Código de Autorização, recebido previamente, ao quais as informações da nota fiscal estão associadas. O valor deste campo é um número formado por 1 a 20 dígitos. | Não\* |
| volume | Este elemento identifica o volume "seta" a ser autorizado. O valor deste campo deverá ser informado desprezando-se os valores centesimais e sem qualquer pontuação. | Sim |
| numero | Este elemento identifica o número da nota fiscal associada a esta operação. O intervalo de valores que este campo pode assumir varia entre 1 e 999.999.999, devendo ser informado sem qualquer pontuação. | Não\* |
| serie | Este elemento identifica a série da nota fiscal associada a esta operação. | Não\* |
| dataEmissao | Este elemento identifica a data na qual a nota fiscal foi emitida. O formato deste campo é aaaammdd, onde: - aaaa: ano;  - mm: mês;  - dd: dia; | Não\* |
| volumeNF | Este elemento identifica o volume do produto medido a 20º C no caminhão. O valor deste campo deverá ser informado desprezando-se os valores centesimais e sem qualquer pontuação. | Não\* |
| valor | Este elemento identifica o valor da operação, conforme descrito na nota fiscal. O formato deste campo será o valor da operação sem qualquer pontuação, desprezados os centavos caso existam. | Não\* |

\* No caso da transmissão posterior dos dados da nota fiscal, os campos
codAutorizacao, numero, serie, dataEmissao, volumeNF e valor deverão estar
necessariamente preenchidos para a complementação.**Exemplo da Estrutura do arquivo XML de Entrada**

<requisicaoXml
xmlns="xsdRequisicao">
<requisicoes>
<requisicao idRequisicao="0001">
<dadosSolicitacao>
<dataRequisicao>200512091100</dataRequisicao>
<remetente>12345678901345</remetente>
<destinatario>43210987654321</destinatario>
<ufDestinatario>SP</ufDestinatario>
<codAutorizacao></codAutorizacao>
<volume>100000</volume>
</dadosSolicitacao>
<dadosNF>
<numero>123456789</numero>
<serie>1</serie>
<dataEmissao>20051010</dataEmissao>
<volumeNF>99000</volumeNF>
<valor>50000</valor>
</dadosNF>
</requisicao>
<requisicao idRequisicao="0002">
<dadosSolicitacao>
<dataRequisicao>200512091100</dataRequisicao>
<remetente>12345678901345</remetente>
<destinatario>43210987654321</destinatario>
<ufDestinatario>MG</ufDestinatario>
<codAutorizacao>9999999999</codAutorizacao>
<volume>100000</volume>
</dadosSolicitacao>
<dadosNF>
<numero>123456789</numero>
<serie>1</serie>
<dataEmissao>20051010</dataEmissao>
<volumeNF>50000</volumeNF>
<valor>25000</valor>
</dadosNF>
</requisicao>
</requisicoes>
</requisicaoXml>

**Schema do arquivo XML de Retorno**

<?xml version="1.0"
encoding="utf-8"?>

<xs:schema
xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns="xsdAutorizacao"
targetNamespace="xsdAutorizacao" elementFormDefault="qualified">

<xs:element name="autorizacaoXml"
type="autorizacoesXml">
</xs:element>
<xs:complexType name="autorizacoesXml" id="autorizacoesXml">
<xs:sequence minOccurs="1" maxOccurs="1">
<xs:element name="nrAutorizacoes" type="xs:integer" />
<xs:element name="autorizacoes" type="autorizacoes" />
</xs:sequence>
</xs:complexType>
<xs:complexType name="autorizacoes" id="autorizacoes">
<xs:sequence minOccurs="0" maxOccurs="unbounded">
<xs:element name="autorizacao" type="autorizacao" />
</xs:sequence>
</xs:complexType>
<xs:complexType name="autorizacao" id="autorizacao">
<xs:sequence minOccurs="1" maxOccurs="1">
<xs:element name="dadosAutorizacao" type="dadosAutorizacao" />
</xs:sequence>
<xs:attribute name="idRequisicao" type="idRequisicao"
use="required">
</xs:attribute>
</xs:complexType>
<xs:complexType name="dadosAutorizacao" id="dadosAutorizacao">
<xs:sequence minOccurs="1" maxOccurs="1">
<xs:element name="dataRequisicao" type="dataRequisicao"
minOccurs="1" maxOccurs="1" />
<xs:element name="remetente" type="cnpj" minOccurs="1"
maxOccurs="1" />
<xs:element name="destinatario" type="cnpj" minOccurs="1"
maxOccurs="1" />
<xs:element name="ufDestinatario" type="uf" minOccurs="1"
maxOccurs="1" />
<xs:element name="codAutorizacao" type="codAutorizacao"
minOccurs="1" maxOccurs="1" />
<xs:element name="mensagemRetorno" type="xs:string"
minOccurs="1" maxOccurs="1" />
</xs:sequence>
</xs:complexType>
<xs:simpleType name="idRequisicao" id="idRequisicao">
<xs:restriction base="xs:positiveInteger">
<xs:pattern value="\d{1,6}" />
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="dataRequisicao" id="dataRequisicao">
<xs:restriction base="xs:positiveInteger">
<xs:pattern value="\d{12}" />
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="cnpj" id="cnpj">
<xs:restriction base="xs:positiveInteger">
<xs:pattern value="\d{14}" />
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="uf" id="uf">
<xs:restriction base="xs:string">
<xs:enumeration value="AC"></xs:enumeration>
<xs:enumeration value="AL"></xs:enumeration>
<xs:enumeration value="AM"></xs:enumeration>
<xs:enumeration value="AP"></xs:enumeration>
<xs:enumeration value="BA"></xs:enumeration>
<xs:enumeration value="CE"></xs:enumeration>
<xs:enumeration value="DF"></xs:enumeration>
<xs:enumeration value="ES"></xs:enumeration>
<xs:enumeration value="GO"></xs:enumeration>
<xs:enumeration value="MA"></xs:enumeration>
<xs:enumeration value="MG"></xs:enumeration>
<xs:enumeration value="MS"></xs:enumeration>
<xs:enumeration value="MT"></xs:enumeration>
<xs:enumeration value="PA"></xs:enumeration>
<xs:enumeration value="PB"></xs:enumeration>
<xs:enumeration value="PE"></xs:enumeration>
<xs:enumeration value="PI"></xs:enumeration>
<xs:enumeration value="PR"></xs:enumeration>
<xs:enumeration value="RJ"></xs:enumeration>
<xs:enumeration value="RN"></xs:enumeration>
<xs:enumeration value="RO"></xs:enumeration>
<xs:enumeration value="RR"></xs:enumeration>
<xs:enumeration value="RS"></xs:enumeration>
<xs:enumeration value="SC"></xs:enumeration>
<xs:enumeration value="SE"></xs:enumeration>
<xs:enumeration value="SP"></xs:enumeration>
<xs:enumeration value="TO"></xs:enumeration>
</xs:restriction>
</xs:simpleType>
<xs:simpleType name="codAutorizacao" id="codAutorizacao">
<xs:restriction base="xs:string">
<xs:pattern value="\d{0,20}" />
</xs:restriction>
</xs:simpleType>

</xs:schema>

**Estrutura do arquivo XML de Retorno**

O arquivo XML de Retorno possui as informações que serão retornadas
após o processamento de cada requisição.

|  |  |  |
| --- | --- | --- |
| **Campo** | **Descrição** | **Obrigatório** |
| xmlns | Este atributo identifica o schema associado ao arquivo XML. O valor deste campo é xsdAutorizacao. | Sim |
| idRequisicao | Este atributo identifica a requisição de autorização unicamente, não podendo assumir um mesmo valor na mesma data (dd/mm/aaaa). O intervalo de valores que este atributo pode assumir varia entre 1 e 999.999. | Sim |
| dataRequisicao | Este elemento identifica a data na qual a requisição está sendo feita (data atual). O formato deste campo é aaaammddhhMM, onde: - aaaa: ano;  - mm: mês;  - dd: dia;  - hh: horas;  - MM: minutos. | Sim |
| remetente | Este elemento identifica o CNPJ do remetente da requisição. O valor deste campo deve ser informado sem pontuação, apenas os 14 dígitos que compõem o CNPJ. | Sim |
| destinatario | Este elemento identifica o CNPJ do destinatário da requisição. O valor deste campo deve ser informado sem pontuação, apenas os 14 dígitos que compõem o CNPJ. | Sim |
| ufDestinatario | Este elemento identifica a UF na qual o destinatário da requisição está localizado. Os possíveis valores para este campo são: AC, AL, AM, AP, BA, CE, DF, ES, GO, MA, MG, MS, MT, PA, PB, PE, PI, PR, RJ, RN, RO, RR, RS, SC, SE, SP, TO. | Sim |
| codAutorizacao | Este elemento identifica o Código de Autorização, caso a requisição tenha sido corretamente processada e autorizada. O valor deste campo é um número formado por 1 a 20 dígitos. | Não |
| mensagemRetorno | Este elemento identifica a mensagem de erro retornada pelo sistema no caso da impossibilidade de processamento ou da não autorização de uma requisição. O valor deste campo é um número formado por 1 a 20 dígitos. | Não |

**Exemplo da Estrutura do arquivo XML de Retorno**

<autorizacaoXml
xmlns="xsdAutorizacao">
<nrAutorizacoes>2</nrAutorizacoes>
<autorizacoes>
<autorizacao idRequisicao="0001">
<dadosAutorizacao>
<dataRequisicao>200601021100</dataRequisicao>
<remetente>12345678901234</remetente>
<destinatario>43210987654321</destinatario>
<ufDestinatario>SP</ufDestinatario>
<codAutorizacao>100000</codAutorizacao>
<mensagemRetorno></mensagemRetorno>
</dadosAutorizacao>
</autorizacao>
<autorizacao idRequisicao="0002">
<dadosAutorizacao>
<dataRequisicao>200601021100</dataRequisicao>
<remetente>12345678901234</remetente>
<destinatario>01234567890123</destinatario>
<ufDestinatario>MG</ufDestinatario>
<codAutorizacao></codAutorizacao>
<mensagemRetorno>DESTINATÁRIO NÃO ESTÁ VINCULADO AO
REMENTENTE</mensagemRetorno>
</dadosAutorizacao>
</autorizacao>
</autorizacoes>
</autorizacaoXml>
**Schema do arquivo XML de Erro**

<?xml version="1.0"
encoding="utf-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
xmlns="xsdErro" targetNamespace="xsdErro"
elementFormDefault="qualified">
<xs:element name="erroXml" type="erroXml">
</xs:element>
<xs:complexType name="erroXml" id="erroXml">
<xs:sequence minOccurs="1" maxOccurs="1">
<xs:element name="erros" type="erros" minOccurs="1"
maxOccurs="1">
</xs:element>
</xs:sequence>
</xs:complexType>
<xs:complexType name="erros" id="erros">
<xs:sequence minOccurs="1">
<xs:element name="erro" type="erro" minOccurs="1" />
</xs:sequence>
</xs:complexType>
<xs:complexType name="erro" id="erro">
<xs:sequence minOccurs="1" maxOccurs="1">
<xs:element name="codigo" id="codigo" minOccurs="0"
maxOccurs="1" type="xs:string">
</xs:element>
<xs:element name="mensagem" id="mensagem" minOccurs="1"
maxOccurs="1" type="xs:string">
</xs:element>
</xs:sequence>
</xs:complexType>
</xs:schema>

**Estrutura do arquivo XML de Erro**

O arquivo XML de Erro possui as informações dos erros detectados
durante o processamento de uma requisição.

|  |  |  |
| --- | --- | --- |
| **Campo** | **Descrição** | **Obrigatório** |
| xmlns | Este atributo identifica o schema associado ao arquivo XML. O valor deste campo é xsdErro. | Sim |
| codigo | Este elemento identifica o código associado ao erro, caso exista. | Não |
| mensagem | Este elemento contém a mensagem do erro ocorrido no sistema quando do processamento da requisição. | Sim |

**Exemplo da Estrutura do arquivo XML de Erro**

<erroXml xmlns="xsdErro">
<erros>
<erro>
<codigo />
<mensagem>O formato ou valor da data informada - 05/20/2005 - não é válido. O
formato correto da data é dd/mm/aaaa.</mensagem>
</erro>
</erros>
</erroXml>" (NR).
****Artigo 2º -** Esta portaria entra em vigor na data de
sua publicação.**
