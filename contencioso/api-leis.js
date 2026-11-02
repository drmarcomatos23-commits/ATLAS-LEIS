// Ponte de leitura do acervo de leis (ATLAS-LEIS e ctresb/leis no GitHub) para o módulo ATLAS LAW.
// Custo zero: só lê arquivos públicos do GitHub. Exige sessão válida do Atlas, como as demais APIs.
const SUPABASE_URL = process.env.SUPABASE_URL;
const SUPABASE_KEY = process.env.SUPABASE_PUBLISHABLE_KEY;

const REPOS = {
  'atlas': 'drmarcomatos23-commits/ATLAS-LEIS',
  'ctresb': 'ctresb/leis'
};

async function authorize(req) {
  const auth = String(req.headers.authorization || '');
  if (!auth.startsWith('Bearer ')) return { ok: false, status: 401, error: 'Sessão não informada' };
  if (!SUPABASE_URL || !SUPABASE_KEY) return { ok: false, status: 503, error: 'Autenticação do Atlas não configurada' };
  try {
    const r = await fetch(`${SUPABASE_URL}/auth/v1/user`, {
      headers: { authorization: auth, apikey: SUPABASE_KEY },
      signal: AbortSignal.timeout(8000)
    });
    if (!r.ok) return { ok: false, status: 401, error: 'Sessão inválida ou expirada' };
    return { ok: true };
  } catch {
    return { ok: false, status: 503, error: 'Falha temporária ao validar a sessão' };
  }
}

function caminhoValido(repo, path) {
  if (!REPOS[repo]) return false;
  if (!path || path.length > 400 || path.includes('..') || path.startsWith('/')) return false;
  if (repo === 'atlas' && /^indices\/[a-z]+\.json$/.test(path)) return true;
  return /^[\w\-./áéíóúâêôãõçÁÉÍÓÚÂÊÔÃÕÇ]+\.md$/.test(path);
}

module.exports = async (req, res) => {
  res.setHeader('Content-Type', 'application/json; charset=utf-8');
  if (req.method !== 'GET') { res.statusCode = 405; return res.end(JSON.stringify({ error: 'Método não permitido' })); }
  const a = await authorize(req);
  if (!a.ok) { res.statusCode = a.status; return res.end(JSON.stringify({ error: a.error })); }
  const url = new URL(req.url, 'http://local');
  const repo = url.searchParams.get('repo') || 'atlas';
  const path = url.searchParams.get('path') || '';
  if (!caminhoValido(repo, path)) { res.statusCode = 400; return res.end(JSON.stringify({ error: 'Caminho inválido' })); }
  try {
    const r = await fetch(`https://raw.githubusercontent.com/${REPOS[repo]}/main/${path.split('/').map(encodeURIComponent).join('/')}`,
      { signal: AbortSignal.timeout(20000) });
    if (!r.ok) { res.statusCode = r.status === 404 ? 404 : 502; return res.end(JSON.stringify({ error: 'Arquivo não encontrado no acervo' })); }
    const texto = await r.text();
    // índices mudam uma vez por dia; textos de normas raramente
    res.setHeader('Cache-Control', 'private, max-age=1800');
    if (path.endsWith('.json')) { res.statusCode = 200; return res.end(texto); }
    res.statusCode = 200;
    return res.end(JSON.stringify({ repo: REPOS[repo], path, texto }));
  } catch {
    res.statusCode = 504;
    return res.end(JSON.stringify({ error: 'O acervo não respondeu a tempo' }));
  }
};
