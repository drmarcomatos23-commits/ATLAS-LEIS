# Módulo ATLAS LAW do Atlas Contencioso

Código-fonte do módulo que junta o ATLAS LAW (108 tarefas) e o acervo ATLAS-LEIS dentro do Atlas Contencioso.

- `atlas-law.js`, `atlas-law-tarefas.js` — carregados pela página `/atlas-law.html` do Contencioso via jsDelivr,
  **fixados por commit e com verificação de integridade (SRI)**: uma alteração aqui só entra no sistema quando a
  página do Contencioso é republicada apontando para o novo commit.
- `atlas-law.html` — cópia da página publicada no Contencioso.
- `api-leis.js` — cópia da função `/api/leis` (ponte de leitura do acervo; exige sessão do Atlas).

Banco (Supabase, esquema `atlas_contencioso`): tabela `law_vinculos` e funções `atlas_contencioso_law_processos`,
`atlas_contencioso_law_contexto`, `atlas_contencioso_law_vincular` — mesma regra de visibilidade de
`atlas_contencioso_meus_processos()`.

Custo zero: nenhuma API paga; a IA é usada colando o pedido no Claude.
