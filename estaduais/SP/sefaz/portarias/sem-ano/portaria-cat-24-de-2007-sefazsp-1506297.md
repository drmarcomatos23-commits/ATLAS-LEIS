---
titulo: "Portaria CAT 24 de 2007"
uf: "SP"
orgao: "Secretaria da Fazenda e Planejamento de SP"
tipo: "Portaria"
numero: "24"
data:
versao_texto: "texto do Portal de Legislação Tributária da SEFAZ-SP (pode estar consolidado)"
fonte: "https://legislacao.fazenda.sp.gov.br/Paginas/pcat242007.aspx"
id_fonte: "sefazsp-1506297"
baixado_em: 2026-11-09
modificado_na_fonte: "2022-05-06T19:54:00Z"
---

# Portaria CAT 24 de 2007

PORTARIA CAT- 24, de 12-3-2007

PORTARIA CAT- 24, de 12-3-2007

(DOE de 13-03-2007)

Altera a Portaria [CAT-117/05](/Paginas/pcat1172005.aspx), de
16-12-2005, que estabelece disciplina para a prévia autorização do diferimento do
lançamento do imposto incidente na operação interna ou interestadual que destinar
Álcool Etílico Anidro Combustível - AEAC a estabelecimento do distribuidor de
combustíveis, e dispõe sobre procedimentos correlatos.

NOTA - V. PORTARIA
[CAT-126/05](/Paginas/pcat1262005.aspx).
               PORTARIA
[CAT-12/06](/Paginas/pcat122006.aspx).

Alteram o conteúdo da Portaria [CAT-117/05](/Paginas/pcat1172005.aspx), de 16-12-2005 (DOE 17-12-2005), que estabelece disciplina para a prévia autorização do diferimento do lançamento do imposto incidente na operação interna ou interestadual que destinar Álcool Etílico Anidro Combustível - AEAC a estabelecimento do distribuidor de combustíveis, e dispõe sobre procedimentos correlatos.

NOTA - V. PORTARIA
[CAT-91/06](/Paginas/pcat912006.aspx), de 17-11-2006 (DOE 18-11-2006), alterada pelas Portarias [CAT-97/06](/Paginas/pcat972006.aspx) e [CAT-23/07](/Paginas/pcat232007.aspx) - Dispõe sobre o registro prévio de operação relativa à circulação de álcool etílico, gasolina automotiva e óleo diesel dos tipos B e D e altera a Portaria CAT 117/05.

O Coordenador da Administração Tributária, tendo em vista o disposto
no artigo 419 do Regulamento do Imposto sobre Operações Relativas à Circulação de
Mercadorias e sobre Prestações de Serviços de Transporte Interestadual e Intermunicipal
e de Comunicação - RICMS, aprovado pelo Decreto n° 45.490, de 30 de novembro de 2000,
expede a seguinte portaria:

**Artigo 1° -** O Anexo único da Portaria [CAT-117/05](/Paginas/pcat1172005.aspx), de 16 de dezembro
de 2005, passa a denominar-se Anexo I e a vigorar com a redação que se segue:

“**ANEXO I

CODIF – Webservice operacoes.asmx**

O sistema CODIF apresenta uma interface para integração de sistemas
via webservices para aqueles usuários cadastrados no sistema. Através deste webservice
os usuários poderão realizar as seguintes operações:

> > · Solicitar Autorizações: solicitar autorizações para as operações de venda de
> > álcool. O método que possibilita esta operação é o SolicitarAutorizações, recebendo
> > como parâmetro um documento xml em conformidade com o schema SolicitacaoAutorizacao.xsd.
> > É retornado por este método um outro documento xml em conformidade com o schema
> > Autorização.xsd, caso a requisição tenha sido processada com sucesso. No caso da
> > impossibilidade de processamento da requisição, a mensagem de erro estará em
> > conformidade com o schema Erro.xsd.
>
> > · Consultar operações próprias por dia: consultar todas as autorizações
> > concedidas ao contribuinte em uma determinada data. O método que possibilita esta
> > operação é o ConsultarOperacoesPropriasPorDia, recebendo como parâmetro uma data no
> > formato dd/mm/aaaa. É retornado por este método um outro documento xml em conformidade
> > com o schema Autorização.xsd, caso a requisição tenha sido processada com sucesso. No
> > caso da impossibilidade de processamento da requisição, a mensagem de erro estará em
> > conformidade com o schema Erro.xsd.
>
> > · Criar Passe Fiscal: solicitar a emissão de um Passe Fiscal para acompanhar o
> > transporte nas operações interestaduais. O método que possibilita esta operação é o
> > CriarPasseFiscal, recebendo como parâmetros um documento xml em conformidade com o schema
> > SolicitacaoPasseFiscal.xsd e um parâmetro de retorno que indica se houve sucesso na
> > geração do Passe Fiscal. Caso a solicitação tenha sido processada com sucesso, é
> > retornado um array de bytes com o conteúdo do Passe Fiscal em formato PDF. Caso
> > contrário, o array de bytes será a mensagem de erro (em conformidade com o schema
> > Erro.xsd) codificada em UTF-8.
>
> > · Obter Passe Fiscal: recuperar o Passe Fiscal gerado previamente. Este método recebe
> > como parâmetro o código de Autorização para o qual se deseja recuperar o Passe Fiscal
> > e também um parâmetro de retorno que indica se houve sucesso na recuperação dos dados
> > do Passe Fiscal. Caso a solicitação tenha sido processada com sucesso, é retornado um
> > array de bytes com o conteúdo do Passe Fiscal em formato PDF. Caso contrário, o array de
> > bytes será a mensagem de erro (em conformidade com o schema Erro.xsd) codificada em
> > UTF-8.
>
> > · Validar mensagens: este método auxiliar realiza a validação de uma mensagem
> > qualquer contra os schemas definidos pelo sistema. Pode ser utilizado durante a etapa de
> > testes para validação das mensagens geradas pelos sistemas que irão utilizar o
> > webservice do CODIF.

**Schema Tipos.xsd**

<?xml version="1.0" encoding="utf-8"?>

<xs:schema id="Tipos"
targetNamespace="https://www.fazenda.sp.gov.br/codif/ws"
elementFormDefault="qualified"
xmlns="https://www.fazenda.sp.gov.br/codif/ws"
xmlns:mstns="https://www.fazenda.sp.gov.br/codif/ws"
xmlns:xs="http://www.w3.org/2001/XMLSchema" version="1.0">

<xs:simpleType name="nroNFType" id="nroNFType">

<xs:restriction base="xs:string">

<xs:pattern value="\d{0,9}" />

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="cnpjType" id="cnpjType">

<xs:restriction base="xs:string">

<xs:pattern value="\d{14}" />

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="dataNFType" id="dataNFType">

<xs:restriction base="xs:string">

<xs:pattern value="\d{0,8}" />

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="codAutorizacaoType"
id="codAutorizacaoType">

<xs:restriction base="xs:string">

<xs:pattern value="\d{0,20}" />

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="idRequisicaoType" id="idRequisicaoType">

<xs:restriction base="xs:positiveInteger">

<xs:pattern value="\d{1,6}" />

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="tipoCombustivelType"
id="tipoCombustivelType">

<xs:restriction base="xs:integer">

<xs:pattern value="\d{9}" />

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="diferimentoType">

<xs:restriction base="xs:string">

<xs:enumeration value="S" />

<xs:enumeration value="N" />

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="cpfCnpjType" id="cpfCnpjType">

<xs:restriction base="xs:string">

<xs:pattern value="\d{11}|\d{14}" />

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="valorType" id="valorType">

<xs:restriction base="xs:string">

<xs:pattern value="\d+(,\d{2})?" />

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="cfopType">

<xs:restriction base="xs:integer">

<xs:pattern value="\d{4}" />

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="ufType" id="ufType">

<xs:restriction base="xs:string">

<xs:enumeration value="AC" />

<xs:enumeration value="AL" />

<xs:enumeration value="AM" />

<xs:enumeration value="AP" />

<xs:enumeration value="BA" />

<xs:enumeration value="CE" />

<xs:enumeration value="DF" />

<xs:enumeration value="ES" />

<xs:enumeration value="GO" />

<xs:enumeration value="MA" />

<xs:enumeration value="MG" />

<xs:enumeration value="MS" />

<xs:enumeration value="MT" />

<xs:enumeration value="PA" />

<xs:enumeration value="PB" />

<xs:enumeration value="PE" />

<xs:enumeration value="PI" />

<xs:enumeration value="PR" />

<xs:enumeration value="RJ" />

<xs:enumeration value="RN" />

<xs:enumeration value="RO" />

<xs:enumeration value="RR" />

<xs:enumeration value="RS" />

<xs:enumeration value="SC" />

<xs:enumeration value="SE" />

<xs:enumeration value="SP" />

<xs:enumeration value="TO" />

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="unidadeMedidaType"
id="unidadeMedidaType">

<xs:restriction base="xs:string">

<!-- 1: litros -->

<xs:pattern value="\d{1}" />

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="dataRequisicaoType"
id="dataRequisicaoType">

<xs:restriction base="xs:string">

<xs:pattern value="\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}" />

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="cpfType" id="cpfType">

<xs:restriction base="xs:string">

<xs:pattern value="\d{11}" />

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="placaType" id="placaType">

<xs:restriction base="xs:string">

<xs:pattern value="[A-Z]{2,3}\d{4}" />

</xs:restriction>

</xs:simpleType>

<xs:simpleType name="nomeType" id="nomeType">

<xs:restriction base="xs:string">

<xs:maxLength value="50" />

</xs:restriction>

</xs:simpleType>

</xs:schema>**Schema Autorizacao.xsd**

<?xml version="1.0" encoding="utf-8"?>

<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
xmlns="https://www.fazenda.sp.gov.br/codif/ws"
targetNamespace="https://www.fazenda.sp.gov.br/codif/ws"
elementFormDefault="qualified" version="1.2">

<xs:include schemaLocation="Tipos.xsd" />

<xs:complexType name="autorizacoesType"
id="autorizacoesType">

<xs:sequence minOccurs="0" maxOccurs="unbounded">

<xs:sequence minOccurs="1" maxOccurs="250">

<xs:element name="autorizacao" type="autorizacaoType" />

</xs:sequence>

</xs:sequence>

</xs:complexType>

<xs:complexType name="autorizacaoType" id="autorizacao">

<xs:sequence minOccurs="1" maxOccurs="1">

<xs:element name="dadosAutorizacao" type="dadosAutorizacaoType"
/>

</xs:sequence>

<xs:attribute name="idRequisicao" type="idRequisicaoType"
use="optional">

</xs:attribute>

</xs:complexType>

<xs:complexType name="dadosAutorizacaoType"
id="dadosAutorizacaoType">

<xs:sequence minOccurs="1" maxOccurs="1">

<xs:element name="dataRequisicao" type="dataRequisicaoType"
minOccurs="1" maxOccurs="1" />

<xs:element name="cnpjRemetente" type="cnpjType"
minOccurs="1" maxOccurs="1" />

<xs:element name="cpfCnpjDestinatario" type="cpfCnpjType"
minOccurs="1" maxOccurs="1" />

<xs:element name="ufDestinatario" type="ufType"
minOccurs="1" maxOccurs="1" />

<xs:element name="codAutorizacao" type="codAutorizacaoType"
minOccurs="1" maxOccurs="1" />

<xs:element name="mensagemRetorno" type="xs:string"
minOccurs="1" maxOccurs="1" />

</xs:sequence>

</xs:complexType>

<xs:element name="root">

<xs:complexType>

<xs:sequence>

<xs:element name="nrAutorizacoes" type="xs:integer"
minOccurs="1" maxOccurs="1" />

<xs:element name="autorizacoes" minOccurs="1"
maxOccurs="1" type="autorizacoesType" />

</xs:sequence>

</xs:complexType>

</xs:element>

</xs:schema>**Campos do schema Autorizacao.xsd**

|  |  |  |
| --- | --- | --- |
| **Campo** | **Descrição** | **Opcional** |
| idRequisicao | Este atributo identifica a requisição de autorização unicamente, não podendo assumir um mesmo valor na mesma data. O intervalo de valores que este atributo pode assumir varia entre 1 e 999.999. | Sim |
|  |  |  |
| dataRequisicao | Este elemento identifica a data na qual a requisição foi processada. O formato deste campo será dd/mm/aaaa hh:MM:ss, onde: - dd: dia;  - aaaa: ano;  - mm: mês;  - hh: hora;  - MM: minuto;  - ss: segundo. | Não |
|  |  |  |
| cnpjRemetente | Este elemento identifica o CNPJ do remetente da requisição. O valor deste campo serão os 14 dígitos que compõem o CNPJ, sem qualquer pontuação. | Não |
|  |  |  |
| cpfCnpjDestinatario | Este elemento identifica o CPF/CNPJ do destinatário da requisição. O valor deste campo serão os 11 dígitos que compõem o CPF ou os 14 dígitos que compõem o CNPJ, sem qualquer pontuação. | Não |
|  |  |  |
| ufDestinatario | Este elemento identifica a UF do destinatário da requisição. Este campo poderá assumir os seguintes valores: AC, AL, AM, AP, BA, CE, DF, ES, GO, MA, MG, MS, MT, PA, PB, PE, PI, PR, RJ, RN, RO, RR, RS, SC, SE, SP, TO. | Não |
|  |  |  |
| codAutorizacao | Este elemento identifica o código de autorização concedido para a requisição. O valor deste campo será um identificador numérico formado por até 20 dígitos. | Não |
|  |  |  |
| mensagemRetorno | Este elemento identifica a mensagem de erro retornada para uma solicitação de autorização. | Não1 |

**Exemplo de mensagem para o schema Autorizacao.xsd**

<?xml version="1.0" encoding="utf-8" ?>

<root xmlns="https://www.fazenda.sp.gov.br/codif/ws">

<nrAutorizacoes>2</nrAutorizacoes>

<autorizacoes>

<autorizacao idRequisicao="001">

<dadosAutorizacao>

<dataRequisicao>01/03/2007 10:00:00</dataRequisicao>

<cnpjRemetente>01234567890123</cnpjRemetente>

<cpfCnpjDestinatario>32109876543210</cpfCnpjDestinatario>

<ufDestinatario>SP</ufDestinatario>

<codAutorizacao>01234567890123456789</codAutorizacao>

<mensagemRetorno></mensagemRetorno>

</dadosAutorizacao>

</autorizacao>

<autorizacao idRequisicao="002">

<dadosAutorizacao>

<dataRequisicao>01/03/2007 10:00:00</dataRequisicao>

<cnpjRemetente>01234567890123</cnpjRemetente>

<cpfCnpjDestinatario>12345678901234</cpfCnpjDestinatario>

<ufDestinatario>MG</ufDestinatario>

<codAutorizacao></codAutorizacao>

<mensagemRetorno>DESTINATÁRIO NÃO ESTÁ VINCULADO AO
REMETENTE</mensagemRetorno>

</dadosAutorizacao>

</autorizacao>

</autorizacoes>

</root>**Schema Erro.xsd**

<?xml version="1.0" encoding="utf-8"?>

<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
xmlns="https://www.fazenda.sp.gov.br/codif/ws"
targetNamespace="https://www.fazenda.sp.gov.br/codif/ws"
elementFormDefault="qualified" version="1.2">

<xs:complexType name="errosType" id="erros">

<xs:sequence minOccurs="1">

<xs:element name="erro" type="erroType" minOccurs="1"
/>

</xs:sequence>

</xs:complexType>

<xs:complexType name="erroType" id="erro">

<xs:sequence minOccurs="1" maxOccurs="1">

<xs:element name="codigo" id="codigo" minOccurs="0"
maxOccurs="1" type="xs:string">

</xs:element>

<xs:element name="mensagem" id="mensagem"
minOccurs="1" maxOccurs="1" type="xs:string">

</xs:element>

</xs:sequence>

</xs:complexType>

<xs:element name="root">

<xs:complexType>

<xs:sequence>

<xs:element name="erros" type="errosType"
minOccurs="1" maxOccurs="10" />

</xs:sequence>

</xs:complexType>

</xs:element>

</xs:schema>**Campos do schema Erro.xsd**

|  |  |  |
| --- | --- | --- |
| **Campo** | **Descrição** | **Opcional** |
| codigo | Este elemento identifica o código associado ao erro, caso exista. | Sim |
|  |  |  |
| mensagem | Este elemento identifica a mensagem associada ao erro. | Não |

**Exemplo de mensagem para o schema Erro.xsd**

<?xml version="1.0" encoding="utf-8" ?>

<root xmlns="https://www.fazenda.sp.gov.br/codif/ws">

<erros>

<erro>

<codigo />

<mensagem>O formato ou valor da data informada - 03/20/2007 - não é válido. O
formato correto da data é dd/mm/aaaa.</mensagem>

</erro>

</erros>

</root>**Schema SolicitacaoAutorizacao.xsd**

<?xml version="1.0" encoding="utf-8"?>

<xs:schema id="requisicao"
targetNamespace="https://www.fazenda.sp.gov.br/codif/ws"
elementFormDefault="qualified"
xmlns="https://www.fazenda.sp.gov.br/codif/ws"
xmlns:mstns="https://www.fazenda.sp.gov.br/codif/ws"
xmlns:xs="http://www.w3.org/2001/XMLSchema" version="1.2">

<xs:include schemaLocation="Tipos.xsd" />

<xs:complexType name="dadosNFType" id="dadosNFType">

<xs:sequence>

<xs:element name="numero" type="nroNFType"
minOccurs="1" maxOccurs="1" />

<xs:element name="serie" type="xs:string"
minOccurs="0" maxOccurs="1" />

<xs:element name="dataEmissao" type="dataNFType"
minOccurs="1" maxOccurs="1" />

<xs:element name="cfop" type="cfopType" minOccurs="1"
maxOccurs="1" />

<xs:element name="volumeNF" type="xs:string"
minOccurs="1" maxOccurs="1" />

<xs:element name="valor" type="valorType"
minOccurs="1" maxOccurs="1" />

</xs:sequence>

</xs:complexType>

<xs:complexType name="dadosSolicitacaoType"
id="dadosSolicitacaoType">

<xs:sequence>

<xs:element name="cnpjRemetente" type="cnpjType"
minOccurs="1" maxOccurs="1" />

<xs:element name="cpfCnpjDestinatario" type="cpfCnpjType"
minOccurs="1" maxOccurs="1" />

<xs:element name="razaoSocialDestinatario" type="xs:string"
minOccurs="1" maxOccurs="1" />

<xs:element name="ufDestinatario" type="ufType"
minOccurs="1" maxOccurs="1" />

<xs:element name="volume" type="xs:string"
minOccurs="1" maxOccurs="1" />

<xs:element name="codUnidadeMedida" type="unidadeMedidaType"
minOccurs="1" maxOccurs="1" />

<xs:element name="tipoCombustivel" type="tipoCombustivelType"
minOccurs="1" maxOccurs="1" />

<xs:element name="diferimento" type="diferimentoType"
maxOccurs="1" minOccurs="1" />

</xs:sequence>

</xs:complexType>

<xs:complexType name="requisicaoType">

<xs:sequence>

<xs:choice minOccurs="1" maxOccurs="1">

<xs:sequence>

<xs:element name="dadosSolicitacao" type="dadosSolicitacaoType"
minOccurs="1" maxOccurs="1" />

<xs:element name="dadosNF" type="dadosNFType"
minOccurs="0" maxOccurs="1" />

</xs:sequence>

<xs:sequence>

<xs:element name="codAutorizacao" type="codAutorizacaoType"
minOccurs="1" maxOccurs="1" />

<xs:element name="dadosNFCompl" type="dadosNFType"
minOccurs="1" maxOccurs="1" />

</xs:sequence>

</xs:choice>

</xs:sequence>

<xs:attribute name="idRequisicao" type="idRequisicaoType"
use="required" />

</xs:complexType>

<xs:complexType name="requisicoesType">

<xs:sequence>

<xs:sequence>

<xs:element name="requisicao" type="requisicaoType"
minOccurs="1" maxOccurs="250" />

</xs:sequence>

</xs:sequence>

</xs:complexType>

<xs:element name="root">

<xs:complexType>

<xs:sequence>

<xs:element name="requisicoes" type="requisicoesType" />

</xs:sequence>

</xs:complexType>

</xs:element>

</xs:schema>**Campos do schema SolicitacaoAutorizacao.xsd**

|  |  |  |
| --- | --- | --- |
| **Campo** | **Descrição** | **Opcional** |
| idRequisicao | Este atributo identifica a requisição de autorização unicamente, não podendo assumir um mesmo valor na mesma data. O intervalo de valores que este atributo pode assumir varia entre 1 e 999.999. | Não |
|  |  |  |
| cnpjRemetente | Este elemento identifica o CNPJ do remetente da requisição. O valor deste campo serão os 14 dígitos que compõem o CNPJ, sem qualquer pontuação. | Não |
|  |  |  |
| cpfCnpjDestinatario | Este elemento identifica o CPF/CNPJ do destinatário da requisição. O valor deste campo serão os 11 dígitos que compõem o CPF ou os 14 dígitos que compõem o CNPJ, sem qualquer pontuação. | Não |
|  |  |  |
| razaoSocialDestinatario | Este elemento identifica a razão social do destinatário da requisição. | Não |
|  |  |  |
| ufDestinatario | Este elemento identifica a UF do destinatário da requisição. Este campo poderá assumir os seguintes valores: AC, AL, AM, AP, BA, CE, DF, ES, GO, MA, MG, MS, MT, PA, PB, PE, PI, PR, RJ, RN, RO, RR, RS, SC, SE, SP, TO. | Não |
|  |  |  |
| volume | Este elemento identifica o volume “seta” a ser autorizado. O valor deste campo deverá ser informado desprezando-se os valores centesimais e sem qualquer pontuação. | Não |
|  |  |  |
| codUnidadeMedida | O código da unidade de medida do volume identificado no campo anterior. Os possíveis códigos aceitos por este campo são:  - 1: litros. | Não |
|  |  |  |
| tipoCombustivel | Este elemento identifica o tipo de combustível da transação. Utiliza-se como valor deste campo o código correspondente ao produto conforme Tabela do ANEXO II da Potaria CAT nº 117, de 16-12-2005. | Não |
|  |  |  |
| diferimento | Este elemento indicará se a operação está sendo realizada com o diferimento do imposto ou não. O valor deste campo será:  - S: operação realizada com diferimento do imposto;  - N: operação realizada sem diferimento do imposto | Não |
|  |  |  |
| codAutorizacao | Este elemento identifica o código de autorização concedido para a requisição. O valor deste campo será um identificador numérico formado por até 20 dígitos. | Sim |
|  |  |  |
| numero | Este elemento identifica o número da nota fiscal associada a esta operação. O intervalo de valores que este campo pode assumir varia entre 1 e 999.999.999, devendo ser informado sem qualquer pontuação. | Não |
|  |  |  |
| serie | Este elemento identifica a série da nota fiscal associada a esta operação. | Sim |
|  |  |  |
| dataEmissao | Este elemento identifica a data na qual a nota fiscal foi emitida. O formato deste campo será ddmmaaaa, onde:  - dd: dia;  - mm: mês;  - aaaa: ano. | Não3 |
|  |  |  |
| cfop | Este elemento identifica o Código Fiscal de Operações e Prestações – CFOP – da operação. | Não3 |
|  |  |  |
| volumeNF | Este elemento identifica o volume do produto medido a 20º C no caminhão. O valor deste campo deverá ser informado desprezando-se os valores centesimais e sem qualquer pontuação. | Não3 |
|  |  |  |
| valor | Este elemento identifica o valor da operação, conforme descrito na nota fiscal. O formato deste campo será o valor da operação incluindo os centavos, caso existam, separados por vírgula. | Não3 |

**Exemplos de mensagens para o schema SolicitacaoAutorizacao.xsd**

> · Exemplo de solicitação de autorização acompanhada dos dados da Nota Fiscal:

<?xml version="1.0" encoding="utf-8" ?>

<root xmlns="https://www.fazenda.sp.gov.br/codif/ws">

<requisicoes>

<requisicao idRequisicao="1">

<dadosSolicitacao>

<cnpjRemetente>12345678901234</cnpjRemetente>

<cpfCnpjDestinatario>09876543210987</cpfCnpjDestinatario>

<razaoSocialDestinatario>Teste</razaoSocialDestinatario>

<ufDestinatario>RJ</ufDestinatario>

<volume>1200</volume>

<codUnidadeMedida>1</codUnidadeMedida>

<tipoCombustivel>320102001</tipoCombustivel>

<diferimento>N</diferimento>

</dadosSolicitacao>

<dadosNF>

<numero>572</numero>

<dataEmissao>01032007</dataEmissao>

<cfop>0000</cfop>

<volumeNF>1200</volumeNF>

<valor>1200,00</valor>

</dadosNF>

</requisicao>

</requisicoes>

</root>

> · Exemplo de solicitação de autorização não acompanhada dos dados da Nota Fiscal:

<?xml version="1.0" encoding="utf-8" ?>

<root xmlns="https://www.fazenda.sp.gov.br/codif/ws">

<requisicoes>

<requisicao idRequisicao="2">

<dadosSolicitacao>

<cnpjRemetente>12345678901234</cnpjRemetente>

<cpfCnpjDestinatario>09876543210987</cpfCnpjDestinatario>

<razaoSocialDestinatario>Teste</razaoSocialDestinatario>

<ufDestinatario>RJ</ufDestinatario>

<volume>1200</volume>

<codUnidadeMedida>1</codUnidadeMedida>

<tipoCombustivel>320102001</tipoCombustivel>

<diferimento>N</diferimento>

</dadosSolicitacao>

</requisicao>

</requisicoes>

</root>

> · Exemplo de complementação dos dados da Nota Fiscal para uma solicitação de
> autorização:

<?xml version="1.0" encoding="utf-8" ?>

<root xmlns="https://www.fazenda.sp.gov.br/codif/ws">

<requisicoes>

<requisicao idRequisicao="3">

<codAutorizacao>12345678901234567890</codAutorizacao>

<dadosNFCompl>

<numero>572</numero>

<dataEmissao>01032007</dataEmissao>

<cfop>0000</cfop>

<volumeNF>1200</volumeNF>

<valor>1200,00</valor>

</dadosNFCompl>

</requisicao>

</requisicoes>

</root>**Schema SolicitacaoPasseFiscal.xsd**

<?xml version="1.0" encoding="utf-8"?>

<xs:schema id="SolicitacaoPasseFiscal"
targetNamespace="https://www.fazenda.sp.gov.br/codif/ws"
elementFormDefault="qualified"
xmlns="https://www.fazenda.sp.gov.br/codif/ws"
xmlns:mstns="https://www.fazenda.sp.gov.br/codif/ws"
xmlns:xs="http://www.w3.org/2001/XMLSchema" version="1.1">

<xs:include schemaLocation="Tipos.xsd" />

<xs:complexType name="dadosTransporteType"
id="dadosTransporteType">

<xs:sequence>

<xs:element name="transporta" type="dadosTransportadorType"
minOccurs="1" maxOccurs="1" />

<xs:element name="motorista" type="dadosMotoristaType"
minOccurs="1" maxOccurs="1" />

<xs:element name="veic" type="dadosVeiculoType"
minOccurs="1" maxOccurs="1" />

</xs:sequence>

</xs:complexType>

<xs:complexType name="dadosTransportadorType"
id="dadosTransportadorType">

<xs:sequence>

<xs:element name="cpfCnpj" type="cpfCnpjType"
minOccurs="1" maxOccurs="1" />

<xs:element name="xNome" type="nomeType" minOccurs="1"
maxOccurs="1" />

<xs:element name="uf" type="ufType" minOccurs="1"
maxOccurs="1" />

</xs:sequence>

</xs:complexType>

<xs:complexType name="dadosVeiculoType"
id="dadosVeiculoType">

<xs:sequence>

<xs:element name="placaPrincipal" type="placaType"
minOccurs="1" maxOccurs="1" />

<xs:element name="ufPlacaPrincipal" type="ufType"
minOccurs="1" maxOccurs="1" />

<xs:element name="placaSecundaria" type="placaType"
minOccurs="0" maxOccurs="1" />

<xs:element name="ufPlacaSecundaria" type="ufType"
minOccurs="0" maxOccurs="1" />

<xs:element name="placaTerceira" type="placaType"
minOccurs="0" maxOccurs="1" />

<xs:element name="ufPlacaTerceira" type="ufType"
minOccurs="0" maxOccurs="1" />

</xs:sequence>

</xs:complexType>

<xs:complexType name="dadosMotoristaType"
id="dadosMotoristaType">

<xs:sequence>

<xs:element name="cpf" type="cpfType" minOccurs="1"
maxOccurs="1" />

<xs:element name="xNome" type="nomeType" minOccurs="1"
maxOccurs="1" />

</xs:sequence>

</xs:complexType>

<xs:complexType name="requisicaoType">

<xs:sequence>

<xs:element name="codAutorizacao" type="codAutorizacaoType"
maxOccurs="1" minOccurs="1" />

<xs:element name="dadosTransporte" type="dadosTransporteType"
maxOccurs="1" minOccurs="1" />

</xs:sequence>

</xs:complexType>

<xs:element name="root">

<xs:complexType>

<xs:sequence>

<xs:element name="requisicao" type="requisicaoType"
maxOccurs="1" minOccurs="1" />

</xs:sequence>

</xs:complexType>

</xs:element>

</xs:schema>**Campos do schema SolicitacaoPasseFiscal.xsd**

|  |  |  |
| --- | --- | --- |
| **Campo** | **Descrição** | **Opcional** |
| codAutorizacao | Este elemento identifica o código associado ao erro, caso exista. | Não |
|  |  |  |
| cpfCnpj | Este elemento identifica o CPF/CNPJ do remetente da requisição, seja transportador autônomo ou empresa. O valor deste campo serão os 11 dígitos que compõem o CPF ou os 14 dígitos que compõem o CNPJ, sem qualquer pontuação. | Não |
|  |  |  |
| transporta - xNome | Este elemento identifica o nome do transportador autônomo ou razão social da empresa que irá realizar o transporte. | Não |
|  |  |  |
| uf | Este elemento identifica a UF da empresa/transportador autônomo que irá realizar o transporte do produto. Este campo poderá assumir os seguintes valores: AC, AL, AM, AP, BA, CE, DF, ES, GO, MA, MG, MS, MT, PA, PB, PE, PI, PR, RJ, RN, RO, RR, RS, SC, SE, SP, TO. | Não |
|  |  |  |
| cpf | Este elemento identifica o CPF do motorista do veículo. O valor deste campo serão os 11 dígitos que compõem o CPF sem qualquer pontuação. | Não |
|  |  |  |
| motorista - xNome | Este elemento identifica o nome do motorista do veículo. | Não |
|  |  |  |
| placaPrincipal | Este elemento identifica a placa principal do veículo utilizado para o transporte. O formato deste campo será CCCNNNN ou CCNNNN, onde:  - C: é uma letra maiúscula;  - N: é um número. | Não |
|  |  |  |
| ufPlacaPrincipal | Este elemento identifica a UF da placa principal do veículo utilizado para o transporte. Este campo poderá assumir os seguintes valores: AC, AL, AM, AP, BA, CE, DF, ES, GO, MA, MG, MS, MT, PA, PB, PE, PI, PR, RJ, RN, RO, RR, RS, SC, SE, SP, TO. | Não |
|  |  |  |
| placaSecundaria | Este elemento identifica a placa secundária do veículo utilizado para o transporte. O formato deste campo será CCCNNNN ou CCNNNN, onde:  - C: é uma letra maiúscula;  - N: é um número. | Sim |
|  |  |  |
| ufPlacaSecundaria | Este elemento identifica a UF da placa secundária do veículo utilizado para o transporte. Este campo poderá assumir os seguintes valores: AC, AL, AM, AP, BA, CE, DF, ES, GO, MA, MG, MS, MT, PA, PB, PE, PI, PR, RJ, RN, RO, RR, RS, SC, SE, SP, TO. | Sim |
|  |  |  |
| placaTerceira | Este elemento identifica a placa terceira do veículo utilizado para o transporte. O formato deste campo será CCCNNNN ou CCNNNN, onde:  - C: é uma letra maiúscula;  - N: é um número. | Sim |
|  |  |  |
| ufPlacaTerceira | Este elemento identifica a UF da placa terceira do veículo utilizado para o transporte. Este campo poderá assumir os seguintes valores: AC, AL, AM, AP, BA, CE, DF, ES, GO, MA, MG, MS, MT, PA, PB, PE, PI, PR, RJ, RN, RO, RR, RS, SC, SE, SP, TO. | Sim |

**Exemplo de mensagem para o schema SolicitacaoPasseFiscal.xsd**

<?xml version="1.0" encoding="utf-8" ?>

<root xmlns="https://www.fazenda.sp.gov.br/codif/ws">

<requisicao>

<codAutorizacao></codAutorizacao>

<dadosTransporte>

<transporta>

<cpfCnpj>01234567890123</cpfCnpj>

<xNome>Teste Transportes LTDA.</xNome>

<uf>BA</uf>

</transporta>

<motorista>

<cpf>01234567890</cpf>

<xNome>Teste Jr.</xNome>

</motorista>

<veic>

<placaPrincipal>BAH2007</placaPrincipal>

<ufPlacaPrincipal>BA</ufPlacaPrincipal>

</veic>

</dadosTransporte>

</requisicao>

</root>

” (NR).

****Artigo 2°** -** Fica acrescentado o Anexo II à Portaria [CAT-117/05](/Paginas/pcat1172005.aspx), de
16 de dezembro de 2005, com a redação que se segue:

“**ANEXO II

Tabela de Código de Produtos**

|  |  |
| --- | --- |
| **Produto** | **Código** |
| Gasolina A Comum | 320101001 |
| Gasolina A Premium | 320101002 |
| Gasolina A fora de especificação | 320101003 |
| Gasolina C Comum | 320102001 |
| Gasolina C Aditivada | 320102002 |
| Gasolina C Premium | 320102003 |
| Gasolina C fora de especificação | 320102004 |
| Gasolina Automotiva Padrão | 320103001 |
| Outras Gasolinas Automotivas | 320103002 |
| Óleo Diesel Interior (B) Comum | 420101001 |
| Óleo Diesel Interior (B) Aditivado | 420101002 |
| Óleo Diesel Interior (B) fora de especificação | 420101003 |
| Óleo Diesel Interior fora de especificação | 420101003 |
| Óleo Diesel Interior Comum - Enxofre 2000 ppm | 420101004 |
| Óleo Diesel Interior Aditivado - Enxofre 2000 ppm | 420101005 |
| Óleo Diesel Metropolitano (D) Comum | 420102001 |
| Óleo Diesel Metropolitano (D) Aditivado | 420102002 |
| Óleo Diesel Metropolitano (D) fora de especificação | 420102003 |
| Óleo Diesel Metropolitano fora de especificação | 420102003 |
| Óleo Diesel Metropolitano Comum - Enxofre 500 ppm | 420102004 |
| Óleo Diesel Metropolitano Aditivado - Enxofre 500 ppm | 420102005 |
| Óleo Diesel S500 Comum | 420103001 |
| Óleo Diesel S500 Aditivado | 420103002 |
| Óleo Diesel S500 fora de especificação | 420103003 |
| Álcool Etílico Hidratado Comum Combustível - AEHC | 810101001 |
| Álcool Etílico Hidratado Combustível - AEHC Aditivado | 810101002 |
| Álcool Etílico Hidratado Combustível - AEHC fora da especificação | 810101003 |
| Álcool Etílico Hidratado para outros fins | 810101004 |
| Álcool Etílico Anidro Combustível - AEAC | 810102001 |
| Álcool Etílico Anidro Combustível - AEAC fora de especificação | 810102002 |
| Álcool Etílico Anidro Combustível - AEAC Padrão | 810102003 |
| Álcool Etílico Anidro Combustível - AEAC com corante | 810102004 |
| Álcool Etílico Anidro para outros fins | 810102005 |

” (NR).

**Artigo 3° -** Esta portaria entra em vigor na data de sua
publicação, produzindo efeitos a partir de 1° de abril de 2007.
