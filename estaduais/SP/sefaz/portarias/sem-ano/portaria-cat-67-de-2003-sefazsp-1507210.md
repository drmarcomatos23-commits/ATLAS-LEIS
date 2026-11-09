---
titulo: "Portaria CAT 67 de 2003"
uf: "SP"
orgao: "Secretaria da Fazenda e Planejamento de SP"
tipo: "Portaria"
numero: "67"
data:
versao_texto: "texto do Portal de Legislação Tributária da SEFAZ-SP (pode estar consolidado)"
fonte: "https://legislacao.fazenda.sp.gov.br/Paginas/pcat672003.aspx"
id_fonte: "sefazsp-1507210"
baixado_em: 2026-11-09
modificado_na_fonte: "2022-05-06T20:10:57Z"
---

# Portaria CAT 67 de 2003

Portaria CAT-67 de 04-08-03

PORTARIA CAT-67 de 04-08-2003

(DOE de 05-08-2003)

Dá nova redação ao parágrafo único do artigo 47 da Portaria CAT-27 de 16-3-95 e aos Anexos X, XVIII-A e XVIII-B de
que tratam os artigos 47 e 58 dessa portaria, na redação da Portaria CAT-27 de 15-4-2002

O Coordenador da Administração Tributária, considerando a necessidade de incluir novo campo de valor informativo na transação STR-020,
do Sistema de Pagamentos Brasileiro - SPB, relativo ao repasse das multas por infração à legislação de trânsito lavradas pelo Departamento Nacional
de Infra-Estrutura de Transportes - DNIT, que serão inseridas no Sistema do Licenciamento Eletrônico de Veículos, para fins de cobrança, conforme
convênio de cooperação técnica, administrativa e financeira firmado com esse órgão federal, expede a seguinte portaria:

**Artigo 1º** - Passam a vigorar com a redação
que se segue os dispositivos adiante enumerados da Portaria CAT-27 de 16 de março
de 1995:

I - o parágrafo único do artigo 47:
"Parágrafo Único - O Banco Nossa Caixa S/A, quando do recebimentoda
mensagem de repasse da Multa Por Infração à Legislação de Trânsito - MILT,
efetuará a consistência, sendo que: o Valor Informativo indicado no campo -
Tipo Valor Informativo "14" - Multas de Trânsito Total deverá ser
igual a somatória do Valor do Lançamento (Valor do Repasse) mais os Valores
Informativos indicados nos campos - Tipos Valores Informativos "16"-
MILT parcela FUNSET; - Tipos Valores Informativos "24" MILT valor da
Polícia Rodoviária Federal e Tipos Valores Informativos "26" - MILT
parcela DNIT". (NR)";

II - os anexos X, XVIII-A e XVIII-B de que
tratam os artigos 47 e 58 da Portaria CAT-27 de 16 de março de 1995, na redação
da Portaria CAT-27 de 15 de abril de 2002:

"ANEXO X

STR-0020 - MILT
Nome do Campo Conteúdo
Tipo Receita 5 (Multas Por Infração à Legislação de Trânsito)
Tipo Recolhimento N=Normal; I=Internet ou P=Papel
Data de Arrecadação AAAAMMDD
Valor lançamento Valor a ser repassado (valor a ser debitado do banco)
Tipo Valor Informativo 14 (Multas de Trânsito Total)
Valor Informativo Preencher com o valor total das Multas de Trânsito
Arrecadadas
Tipo Valor Informativo 16 (Multas de Trânsito - parcela do FUNSET)
Valor Informativo Preencher com o valor referente a parcela do FUNSET
Tipo Valor Informativo 24 (Multas de Trânsito - parcela da Polícia Rodoviária
Federal)
Valor Informativo Preencher com o valor total da Polícia Rodoviária Federal
Tipo Valor Informativo 26 (Multas de Trânsito - parcela do DNIT)
Valor Informativo Preencher com o valor total do DNIT (NR)";

"ANEXO XVIII-A

REGISTRO DETALHE - RESUMO DE RECEITA - MILT
Nome do Campo Posição Formato/Tamanho Conteúdo
Tipo de Registro 001-002 X(002) "03" = MILT
Identificação Registro 003-003 X(001) "1" (constante) = Resumo de
Receita
Data do Depósito 004-011 9(008) AAAAMMDD - Data Repasse à Sefaz
Banco Depositário 012-019 9(008) Configuração: BBBAAAAD Código CAR
Número do Resumo 020-023 9(004) Nº Sequencial, reiniciando anualmente
Número de Controle 024-027 9(004) Código do banco + Número do Resumo
Quantidade Depósitos 028-030 9(003) Quantidade de registros tipo 2
(comprovantes de depósito) existentes no arquivo
Valor Total Arrecadado 031-047 9(015)v99 MILT - Valor Total Arrecadado
1º Desdobramento Valor 048-064 9(015)v99 MILT -Valor Sefaz-Conta Única (código
300)
2º Desdobramento Valor 065-081 9(015)V99 MILT - Valor FUNSET (código 305)
3º Desdobramento Valor 082-098 9(015)v99 MILT - Valor P. Rod. Federal (código
400)
4º Desdobramento Valor 099-113 9(015)v99 MILT - Valor DNIT
Filler 114-144 X(031) Reservado para o futuro
Número Sequencial 145-152 9(008) "2" (constante) = nº de ordem do
registro no Arquivo (NR)";

"ANEXO XVIII-B

REGISTRO DETALHE - COMPROVANTE DE DEPÓSITO -
MILT
Nome do Campo Posição Formato/Tamanho Conteúdo
Tipo de Registro 001-002 X(002) "03" = MILT
Identificação do Registro 003-003 X(001) "2"(constante)= Comprovante
Depósito
Data do Depósito 004-011 9(008) AAAAMMDD = Data Repasse à Sefaz
Banco Arrecadador 012-019 9(008) Configuração: BBBAAAAD-Código CAR
Número do Depósito 020-023 9(004) nº sequencial, reiniciando anualmente
Número de Controle 024-027 9(004) Código do Banco+Número do Depósito
Quantidade Borderôs 028-030 9(002) "001" (constante)
Tipo de Guia 031-032 9(002) 03-GARE-MILT
Meio Prestação de Contas 033-033 X(001) M - meio magnético
F - meio físico (papel)
A - ambiente de pagamentos
Data da Arrecadação 034-041 9(008) AAAAMMDD - data do pagamento da guia
Valor Total Arrecadado 042-058 9(015)v99 MILT - Valor Arrecadado
1º Desdobramento Valor 059-075 9(015)v99 MILT -Valor Sefaz-Conta Única (código
300)
2º Desdobramento Valor 076-092 9(015)V99 MILT - Valor FUNSET (código 305)
3º Desdobramento Valor 093-109 9(015)v99 MILT - Valor P. Rod. Federal (código
400)
4º Desdobramento Valor 110-124 9(015)v99 MILT - Valor DNIT
Filler 125-144 X(020) Resevado para o futuro
Número Sequencial 145-152 9(008) Número de ordem do registro no arquivo
(NR)".

**Artigo 2º** - Esta portaria entrará em
vigor na data de sua publicação.
