/* ATLAS LAW no Atlas Contencioso — leis, precedentes e tarefas jurídicas do processo.
   Custo zero: lê o acervo público (ATLAS-LEIS + ctresb/leis) pela ponte /api/leis e monta os pedidos
   do ATLAS LAW no navegador, para colar no Claude. Nada é enviado a serviço pago. */
(function () {
  'use strict';
  const SUPABASE_URL = 'https://oorpvbxxpbxoaaykrtcf.supabase.co';
  const SUPABASE_KEY = 'sb_publishable_5261il-Rwu1wPQG_sTBb5g_tE52L_DQ';
  const sb = window.supabase.createClient(SUPABASE_URL, SUPABASE_KEY);
  const $ = (s) => document.querySelector(s);
  const esc = (t) => String(t == null ? '' : t).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const norm = (t) => String(t || '').normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
  const REPO_CHAVE = { 'drmarcomatos23-commits/ATLAS-LEIS': 'atlas', 'ctresb/leis': 'ctresb' };
  const githubUrl = (repo, path) => `https://github.com/${repo}/${path.endsWith('/') ? 'tree' : 'blob'}/main/${path}`;

  const estado = { token: null, processos: [], atual: null, ctx: null, indices: {}, normas: null, novidades: null, tarefa: null };

  function toast(msg) { const t = $('#toast'); t.textContent = msg; t.style.display = 'block'; clearTimeout(toast.h); toast.h = setTimeout(() => (t.style.display = 'none'), 2600); }

  /* ---------- acervo ---------- */
  async function api(repo, path) {
    const r = await fetch(`/api/leis?repo=${repo}&path=${encodeURIComponent(path)}`, { headers: { authorization: `Bearer ${estado.token}` } });
    if (!r.ok) throw new Error((await r.json().catch(() => ({}))).error || `Erro ${r.status}`);
    return r.json();
  }
  async function indice(nome) {
    if (!estado.indices[nome]) estado.indices[nome] = api('atlas', `indices/${nome}.json`).then(preparar);
    return estado.indices[nome];
  }
  const STOP = new Set('a o e de da do das dos em no na nos nas por para com sem que se ao aos as os um uma ou nao sim sob sobre pela pelo pelas pelos seu sua seus suas art lei n nº no. ser e/ou ainda este esta isso mesmo quando como mais menos entre ate apos desde outros outras demais etc'.split(' '));
  function tokens(t) {
    return norm(t).replace(/[^a-z0-9§ ]+/g, ' ').split(/\s+/).filter((w) => w.length > 2 && !STOP.has(w)).map((w) => (w.length > 4 && w.endsWith('s') ? w.slice(0, -1) : w));
  }
  function preparar(lista) {
    for (const it of lista) { it._tok = new Set(tokens(`${it.tit} ${it.txt}`)); it._norm = norm(`${it.tit} ${it.txt}`); }
    const df = new Map();
    for (const it of lista) for (const w of it._tok) df.set(w, (df.get(w) || 0) + 1);
    lista._idf = (w) => Math.log((lista.length + 1) / ((df.get(w) || 0) + 1));
    return lista;
  }

  // Sinônimos e expansões para os assuntos mais comuns da carteira (TPU/CNJ)
  const EXPANSOES = [
    [/hora.{0,3}extra|sobrejornada/, 'horas extras jornada sobrejornada compensacao 59 banco horas'],
    [/insalubri/, 'insalubridade insalubre adicional insalubridade 189 192 nr-15 laudo pericia'],
    [/periculosi/, 'periculosidade perigoso adicional periculosidade 193 nr-16 inflamavel eletricidade'],
    [/aviso previo/, 'aviso previo indenizado proporcional 487 12506'],
    [/rescisao indireta/, 'rescisao indireta falta grave empregador 483'],
    [/verbas rescisorias|rescisao do contrato|integracao em verbas/, 'verbas rescisorias rescisao 477 multa 467 ferias 13º'],
    [/relacao de emprego|vinculo/, 'vinculo emprego relacao emprego subordinacao pessoalidade pejotizacao autonomo 3º'],
    [/dano moral/, 'dano moral indenizacao extrapatrimonial 223'],
    [/\bfgts\b/, 'fgts deposito multa 40% 8036 prescricao'],
    [/acumulo de funcao/, 'acumulo funcao desvio funcao plus salarial 456'],
    [/intrajornada/, 'intervalo intrajornada 71 refeicao descanso supressao'],
    [/adicional noturno/, 'adicional noturno hora noturna 73 prorrogacao'],
    [/subsidiaria|solidaria/, 'responsabilidade subsidiaria solidaria terceirizacao tomador 331 6019 grupo economico'],
    [/justa causa/, 'justa causa falta grave 482 reversao'],
    [/comisso/, 'comissoes percentuais comissionista 466 integracao'],
    [/honorario/, 'honorarios sucumbencia 791-a advocaticios'],
    [/execucao provisoria|cumprimento provisorio/, 'execucao provisoria cumprimento provisorio sentenca 520 caucao penhora'],
    [/liquidacao|cumprimento|execucao/, 'execucao liquidacao penhora correcao monetaria juros ipca selic'],
    [/divida ativa|execucao fiscal/, 'execucao fiscal divida ativa prescricao intercorrente redirecionamento socio cda 6830 excecao pre-executividade'],
    [/\biss\b|imposto sobre servico/, 'iss imposto servicos municipal base calculo lista servicos local'],
    [/expurgo|planos economicos/, 'expurgos inflacionarios planos economicos poupanca bresser verao collor'],
    [/locacao/, 'locacao aluguel despejo fianca 8245 locatario locador'],
    [/condominio/, 'condominio cotas condominiais taxa inadimplemento'],
    [/inventario|partilha/, 'inventario partilha heranca sucessao itcmd colacao'],
    [/rescisao do contrato e devolucao|devolucao do dinheiro/, 'rescisao compromisso compra venda imovel devolucao parcelas retencao'],
    [/prestacao de servico/, 'prestacao servicos contrato inadimplemento'],
    [/\bctps\b/, 'ctps anotacao carteira trabalho'],
  ];

  // termos genéricos de classe processual não servem para escolher precedente
  const GENERICOS = new Set(tokens('acao trabalhista rito ordinario sumarissimo sumario procedimento comum civel processo conhecimento recurso ordinario agravo peticao'));
  function consulta(ctx) {
    const assunto = String(ctx.assunto || '');
    let extra = '';
    for (const [re, add] of EXPANSOES) if (re.test(norm(`${assunto} ${ctx.classe || ''}`))) extra += ' ' + add;
    const pubs = (ctx.publicacoes || []).slice(0, 3).map((p) => p.texto).join(' ');
    const forte = new Set(tokens(assunto + extra).filter((w) => !GENERICOS.has(w)));
    const fraco = new Set(tokens(`${ctx.classe || ''} ${pubs}`).filter((w) => !GENERICOS.has(w)));
    return { forte, fraco, trabalho: /^TRT|^TST/.test(String(ctx.tribunal || '')) };
  }

  function pontuar(lista, q, limite = 12) {
    const res = [];
    for (const it of lista) {
      let s = 0; const hits = [];
      for (const w of q.forte) if (it._tok.has(w)) { s += 2 * lista._idf(w); hits.push(w); }
      for (const w of q.fraco) if (it._tok.has(w) && !q.forte.has(w)) s += 0.25 * lista._idf(w);
      if (!s || hits.length < 1) continue;
      if (/repetitivo|IRR|repercussao|vinculante|IRDR|Tema/i.test(it.tipo)) s *= 1.25;
      if (q.trabalho && /^(TST|TRT2|MTE)$/.test(it.trib)) s *= 1.4;   // na Justiça do Trabalho, TST/TRT-2 primeiro
      if (it.trib === 'STF' && hits.length < 2) s *= 0.5;             // tema do STF só com mais de um termo em comum
      if (/cancelad|revogad|nao admitido|inadmitido/i.test(norm(it.sit + ' ' + it.txt.slice(0, 120)))) s *= 0.3;
      res.push({ it, s, hits });
    }
    return res.sort((a, b) => b.s - a.s).slice(0, limite);
  }

  function destacar(txt, hits) {
    let h = esc(txt);
    for (const w of hits.slice(0, 8)) {
      const re = new RegExp(`(${w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}\\w*)`, 'gi');
      h = h.replace(re, '<mark>$1</mark>');
    }
    return h;
  }

  function cartao(it, opts = {}) {
    const vinculado = (estado.ctx?.vinculos || []).some((v) => v.item_id === it.id);
    const sit = it.sit ? `<span class="tag cinza">${esc(it.sit)}</span>` : '';
    return `<div class="item" data-id="${esc(it.id)}">
      <div class="t">${esc(it.tit)}</div>
      <div><span class="tag">${esc(it.trib)}</span><span class="tag ouro">${esc(it.tipo)}</span>${sit}</div>
      <div class="x">${opts.hits ? destacar(it.txt, opts.hits) : esc(it.txt)}</div>
      <div class="acoes">
        <button data-ver="${esc(it.repo)}|${esc(it.path)}|${esc(it.tit)}">Ler texto</button>
        ${vinculado ? `<button data-desvincular="${esc(it.id)}">Remover do processo</button>` : `<button class="prim" data-vincular="${esc(it.id)}">Vincular ao processo</button>`}
      </div></div>`;
  }

  function areaDo(ctx) {
    const t = String(ctx.tribunal || '');
    if (/^TRT|^TST/.test(t)) return 'trabalho';
    if (/divida ativa|execucao fiscal|tribut|iss|icms|iptu|itbi|itcmd/.test(norm(`${ctx.assunto} ${ctx.classe}`))) return 'tributario';
    return 'civel';
  }

  async function renderPrecedentes() {
    const ctx = estado.ctx; const area = areaDo(ctx);
    const nomes = area === 'trabalho' ? ['trabalho', 'geral'] : ['civel', 'geral'];
    try {
      const listas = await Promise.all(nomes.map(indice));
      const q = consulta(ctx);
      const res = listas.flatMap((l) => pontuar(l, q, 10)).sort((a, b) => b.s - a.s).slice(0, 14);
      estado.sugeridos = res.map((r) => r.it);
      $('#sugeridos').innerHTML = res.length ? res.map((r) => cartao(r.it, { hits: r.hits })).join('')
        : '<div class="vazio">Nenhuma sugestão automática: o processo não tem assunto cadastrado ou o tema não aparece no acervo. Use a busca ao lado.</div>';
    } catch (e) {
      $('#sugeridos').innerHTML = `<div class="vazio">Não foi possível carregar o acervo: ${esc(e.message)}</div>`;
    }
    renderVinculados();
    renderNormas(area);
  }

  function renderVinculados() {
    const v = estado.ctx?.vinculos || [];
    $('#n-vinc').textContent = v.length;
    $('#vinculados').innerHTML = v.length ? v.map((x) => `<div class="item">
        <div class="t">${esc(x.titulo)}</div><div><span class="tag">${esc(x.tribunal || '')}</span><span class="tag ouro">${esc(x.tipo || '')}</span></div>
        ${x.resumo ? `<div class="x">${esc(x.resumo.slice(0, 300))}${x.resumo.length > 300 ? '…' : ''}</div>` : ''}
        <div class="acoes"><button data-ver="${esc(x.repo)}|${esc(x.path)}|${esc(x.titulo)}">Ler texto</button><button data-desvincular="${esc(x.item_id)}">Remover</button></div></div>`).join('')
      : '<div class="vazio">Nenhum precedente ou norma vinculado ainda. Os vinculados entram automaticamente nas tarefas do ATLAS LAW.</div>';
  }

  async function renderNormas(area) {
    try {
      if (!estado.normas) estado.normas = await api('atlas', 'indices/normas.json');
      const lista = [...(estado.normas[area] || []), ...(estado.normas.geral || [])];
      $('#normas').innerHTML = lista.map((n) => `<div class="item" style="padding:9px 12px"><div class="t" style="font-size:13px">${esc(n.tit)}</div>
        <div class="acoes">${n.path.endsWith('/') ? '' : `<button data-ver="${esc(n.repo)}|${esc(n.path)}|${esc(n.tit)}">Ler texto</button>`}
        <a href="${githubUrl(n.repo, n.path)}" target="_blank" rel="noopener">Abrir no acervo</a>
        ${n.path.endsWith('/') ? '' : `<button data-vincular-norma="${esc(n.repo)}|${esc(n.path)}|${esc(n.tit)}">Vincular</button>`}</div></div>`).join('');
    } catch (e) { $('#normas').innerHTML = `<div class="vazio">${esc(e.message)}</div>`; }
  }

  let buscaT;
  function buscarAcervo() {
    clearTimeout(buscaT);
    buscaT = setTimeout(async () => {
      const termo = $('#busca-acervo').value.trim();
      if (termo.length < 3) { $('#resultado-busca').innerHTML = ''; return; }
      const listas = await Promise.all(['trabalho', 'civel', 'geral'].map(indice));
      const tn = norm(termo); const q = { forte: new Set(tokens(termo)), fraco: new Set() };
      let res = listas.flatMap((l) => pontuar(l, q, 15));
      const exato = listas.flat().filter((it) => it._norm.includes(tn)).slice(0, 10).map((it) => ({ it, s: 999, hits: [...q.forte] }));
      const vistos = new Set(); res = [...exato, ...res].filter((r) => !vistos.has(r.it.id) && vistos.add(r.it.id)).slice(0, 12);
      $('#resultado-busca').innerHTML = res.length ? res.map((r) => cartao(r.it, { hits: r.hits })).join('') : '<div class="vazio">Nada encontrado.</div>';
    }, 300);
  }

  async function vincular(it, nota) {
    try {
      await sb.rpc('atlas_contencioso_law_vincular', { p: { cnj: estado.atual.cnj, item_id: it.id, repo: it.repo, path: it.path, titulo: it.tit, tipo: it.tipo, tribunal: it.trib, resumo: it.txt, nota } }).then(r => { if (r.error) throw r.error; });
      await recarregarCtx(); toast('Vinculado ao processo'); renderPrecedentes(); montarPrompt();
    } catch (e) { toast(`Não foi possível vincular: ${e.message}`); }
  }
  async function desvincular(id) {
    const r = await sb.rpc('atlas_contencioso_law_vincular', { p: { cnj: estado.atual.cnj, item_id: id, acao: 'remover' } });
    if (r.error) return toast(r.error.message);
    await recarregarCtx(); toast('Removido'); renderPrecedentes(); montarPrompt();
  }

  async function verTexto(repoNome, path, titulo) {
    const chave = REPO_CHAVE[repoNome] || repoNome;
    $('#m-tit').textContent = titulo; $('#m-txt').textContent = 'Carregando…';
    $('#m-link').href = githubUrl(repoNome, path); $('#modal').style.display = 'flex';
    try {
      const d = await api(chave, path);
      const fonte = (d.texto.match(/^fonte:\s*"?([^"\n]+)"?/m) || [])[1];
      $('#m-txt').textContent = (fonte ? `Fonte oficial: ${fonte}\n\n` : '') + d.texto.replace(/^---[\s\S]*?---\s*/, '');
    } catch (e) { $('#m-txt').textContent = e.message; }
  }

  /* ---------- novidades ---------- */
  async function renderNovidades() {
    try {
      if (!estado.novidades) estado.novidades = preparar(await api('atlas', 'indices/novidades.json'));
      const q = consulta(estado.ctx);
      const rel = pontuar(estado.novidades, q, 10);
      $('#novidades-proc').innerHTML = rel.length ? rel.map((r) => novidade(r.it, r.hits)).join('') : '<div class="vazio">Nenhuma novidade dos últimos 30 dias ligada ao assunto deste processo.</div>';
      $('#novidades-todas').innerHTML = estado.novidades.slice(-25).reverse().map((n) => novidade(n)).join('');
    } catch (e) { $('#novidades-proc').innerHTML = `<div class="vazio">${esc(e.message)}</div>`; }
  }
  function novidade(n, hits) {
    return `<div class="item"><div class="t">${esc(n.tit || n.tipo)}</div><div><span class="tag">${esc(n.trib || n.col)}</span><span class="tag cinza">${esc(n.dia)}</span></div>
      ${n.txt ? `<div class="x">${hits ? destacar(n.txt, hits) : esc(n.txt)}</div>` : ''}
      <div class="acoes"><button data-ver="${esc(n.repo)}|${esc(n.path)}|${esc(n.tit || n.tipo)}">Ler texto</button></div></div>`;
  }

  /* ---------- tarefas ATLAS LAW ---------- */
  const SUGERIDAS = ['LAW-LIT-01', 'LAW-LIT-03', 'LAW-LIT-04', 'LAW-LIT-05', 'LAW-LIT-06', 'LAW-LIT-07', 'LAW-LIT-08', 'LAW-LIT-09',
    'LAW-JUR-01', 'LAW-JUR-09', 'LAW-AUD-01', 'LAW-AUD-06', 'LAW-PAR-09', 'LAW-EMP-09'];
  function renderTarefas() {
    const termo = norm($('#busca-tarefa').value);
    const mods = window.ATLAS_LAW_MODULOS || [];
    const todas = mods.flatMap((m) => m.tarefas.map((t) => ({ ...t, mod: m })));
    const filtro = (t) => !termo || norm(`${t.id} ${t.titulo} ${t.tarefa} ${t.mod.nome}`).includes(termo);
    const sug = SUGERIDAS.map((id) => todas.find((t) => t.id === id)).filter(Boolean).filter(filtro);
    let html = sug.length ? `<div class="mod-t">Sugeridas para processos</div>${sug.map(linhaTarefa).join('')}` : '';
    for (const m of mods) {
      const ts = m.tarefas.map((t) => ({ ...t, mod: m })).filter(filtro);
      if (ts.length) html += `<div class="mod-t">${esc(m.nome)} · ${esc(m.cmd)}</div>${ts.map(linhaTarefa).join('')}`;
    }
    $('#lista-tarefas').innerHTML = html || '<div class="pad vazio">Nenhuma tarefa encontrada.</div>';
  }
  function linhaTarefa(t) {
    return `<div class="tar${estado.tarefa?.id === t.id ? ' sel' : ''}" data-tarefa="${esc(t.id)}"><b>${esc(t.id)}</b> ${esc(t.titulo)}<small>${esc(t.formato)}</small></div>`;
  }
  function escolherTarefa(id) {
    for (const m of window.ATLAS_LAW_MODULOS) { const t = m.tarefas.find((x) => x.id === id); if (t) estado.tarefa = { ...t, mod: m }; }
    const t = estado.tarefa;
    $('#tarefa-info').innerHTML = `<b>${esc(t.id)} — ${esc(t.titulo)}</b><br><span class="vazio">${esc(t.tarefa)}</span>`;
    renderTarefas(); montarPrompt();
  }

  function anon(texto, ctx) {
    let t = String(texto || '');
    const subs = [[ctx.polo_ativo, '[POLO ATIVO]'], [ctx.polo_passivo, '[POLO PASSIVO]'], [ctx.cliente_nome, '[CLIENTE]'], [ctx.parte_contraria, '[PARTE CONTRÁRIA]']];
    for (const [nomes, rot] of subs) {
      for (const n of String(nomes || '').split(/,\s*| × /)) if (n && n.trim().length > 4) t = t.split(n.trim()).join(rot);
    }
    return t.replace(/\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b/g, '[CPF]').replace(/\b\d{2}\.?\d{3}\.?\d{3}\/?\d{4}-?\d{2}\b/g, '[CNPJ]');
  }

  function montarPrompt() {
    const t = estado.tarefa; const c = estado.ctx;
    if (!t || !c) { $('#prompt').value = ''; $('#btn-copiar').disabled = true; return; }
    const A = $('#opt-anon').checked; const f = (x) => (A ? anon(x, c) : String(x || ''));
    const vinc = (c.vinculos || []);
    const linhas = [];
    linhas.push(`ATLAS LAW — ${t.id} | ${t.titulo}`, '');
    linhas.push(`PAPEL: Atue como ${t.mod.papel}, no direito brasileiro, como assistente jurídico sênior do escritório Marco Matos Advogado. A decisão profissional, a assinatura e o protocolo são do advogado.`);
    linhas.push(`FOCO TÉCNICO: ${t.mod.foco}`);
    linhas.push(`TAREFA: ${t.tarefa}`);
    const instr = $('#instrucao').value.trim(); if (instr) linhas.push(`INSTRUÇÃO DO ADVOGADO: ${instr}`);
    linhas.push('', '=== DADOS DO PROCESSO (extraídos do Atlas Contencioso — DataJud/DJEN) ===');
    linhas.push(`Processo: ${c.numero} — ${c.tribunal || ''} — ${c.orgao || ''}`);
    linhas.push(`Classe: ${c.classe || '[DADO PENDENTE]'} | Assunto: ${c.assunto || '[DADO PENDENTE]'} | Valor da causa: ${c.valor_causa ? 'R$ ' + c.valor_causa : '[DADO PENDENTE]'}`);
    if (c.data_ajuizamento) linhas.push(`Ajuizamento: ${c.data_ajuizamento} | Situação no sistema: ${c.situacao || '—'}`);
    linhas.push(`Polo ativo: ${f(c.polo_ativo) || '[DADO PENDENTE]'}`);
    linhas.push(`Polo passivo: ${f(c.polo_passivo) || '[DADO PENDENTE]'}`);
    if (c.cliente_nome) linhas.push(`Cliente representado: ${f(c.cliente_nome)}`);
    if (c.segredo_justica) linhas.push('ATENÇÃO: processo em segredo de justiça — redobrar sigilo.');
    if ($('#opt-movs').checked && (c.movimentacoes || []).length) {
      linhas.push('', 'Últimas movimentações:');
      for (const m of c.movimentacoes) linhas.push(`- ${String(m.data || '').slice(0, 10)}: ${m.nome || ''}${m.complemento ? ' — ' + f(m.complemento) : ''}`);
    }
    if ($('#opt-pubs').checked && (c.publicacoes || []).length) {
      linhas.push('', 'Publicações recentes (texto do DJEN, pode estar truncado):');
      for (const p of c.publicacoes.slice(0, 4)) linhas.push(`- [${p.data || ''}] ${f(p.texto).replace(/\s+/g, ' ').slice(0, 1400)}`);
    }
    if ((c.prazos_sugeridos || []).length) {
      linhas.push('', 'Prazos sugeridos pelo sistema — PRAZO NÃO CONFIRMADO (exigem validação humana):');
      for (const p of c.prazos_sugeridos) linhas.push(`- ${p.dias || '?'} ${p.unidade || ''} (${p.situacao || ''}${p.vencimento ? ', vencimento sugerido ' + String(p.vencimento).slice(0, 10) : ''}): ${f(p.trecho)}`);
    }
    linhas.push('', '=== FONTES VINCULADAS PELO ADVOGADO (acervo de leis) ===');
    if (vinc.length) for (const v of vinc) linhas.push(`- ${v.titulo} (${v.tribunal || ''} · ${v.tipo || ''}) — texto: https://raw.githubusercontent.com/${v.repo}/main/${v.path}${v.nota ? ' — nota: ' + v.nota : ''}`);
    else linhas.push('- (nenhuma vinculada; pesquise no acervo abaixo)');
    const sug = (estado.sugeridos || []).slice(0, 6).filter((s) => !vinc.some((v) => v.item_id === s.id));
    if (sug.length) { linhas.push('', 'Precedentes sugeridos automaticamente (aplicabilidade NÃO verificada — confira antes de usar):'); for (const s of sug) linhas.push(`- ${s.tit} — https://raw.githubusercontent.com/${s.repo}/main/${s.path}`); }
    linhas.push('', '=== ACERVO DE LEIS ===');
    linhas.push('Leia o texto integral das normas antes de citar: https://github.com/ctresb/leis (CF, leis federais e estaduais, súmulas e OJs do TST, STF, STJ) e https://github.com/drmarcomatos23-commits/ATLAS-LEIS (Santos e Baixada, SEFAZ-SP, CNJ, DREI, TJ-SP, TRT-2, temas repetitivos do TST, NRs). Confirme sempre no link oficial do campo "fonte".');
    linhas.push('', `MÉTODO: (1) extraia e cite fatos dos dados acima; (2) separe confirmado de faltante; (3) confronte legislação vigente e jurisprudência oficial; (4) melhor abordagem e melhor argumento contrário; (5) redija a entrega completa; (6) audite coerência, números, remissões e prova.`);
    linhas.push(`FORMATO DE SAÍDA: ${t.formato} Inclua conclusão executiva e pendências críticas no fim, fora do corpo da minuta.`);
    linhas.push('LIMITES: Não invente normas, decisões, números de processo, qualificações ou fatos. Precedente sem fonte oficial verificada = "PRECEDENTE NÃO VERIFICADO" e fica fora da peça. Prazos sempre "PRAZO NÃO CONFIRMADO" até validação humana; não registre nem ajuste prazos em sistema. Use [DADO PENDENTE] para o que faltar. Não prometa resultado e proteja os dados do cliente (LGPD, sigilo, ética OAB).');
    const txt = linhas.join('\n');
    $('#prompt').value = txt; $('#btn-copiar').disabled = false;
    $('#tam').textContent = `${txt.length.toLocaleString('pt-BR')} caracteres`;
  }

  /* ---------- processos ---------- */
  function renderLista() {
    const termo = norm($('#busca-proc').value);
    const lst = estado.processos.filter((p) => !termo || norm(`${p.numero} ${p.cnj} ${p.partes} ${p.assunto} ${p.classe} ${p.tribunal}`).includes(termo)).slice(0, 300);
    $('#lista-proc').innerHTML = lst.length ? lst.map((p) => `<div class="proc${estado.atual?.cnj === p.cnj ? ' ativo' : ''}" data-cnj="${esc(p.cnj)}">
      <div class="n">${esc(p.numero || p.cnj)}</div>
      <div class="m">${esc(p.partes || '')}</div>
      <div class="m"><span class="tag">${esc(p.tribunal || '')}</span>${esc(p.assunto || p.classe || 'Sem assunto cadastrado')}${p.vinculos ? ` <span class="tag ouro">${p.vinculos} fonte(s)</span>` : ''}</div></div>`).join('')
      : '<div class="pad vazio">Nenhum processo encontrado.</div>';
  }

  async function recarregarCtx() {
    const r = await sb.rpc('atlas_contencioso_law_contexto', { p_cnj: estado.atual.cnj });
    if (r.error) throw r.error;
    estado.ctx = r.data;
    const p = estado.processos.find((x) => x.cnj === estado.atual.cnj); if (p) p.vinculos = (r.data?.vinculos || []).length;
  }

  async function abrirProcesso(cnj) {
    estado.atual = estado.processos.find((p) => p.cnj === cnj);
    if (!estado.atual) return;
    history.replaceState(null, '', `?cnj=${cnj}`);
    renderLista();
    $('#sem-proc').style.display = 'none'; $('#proc').style.display = 'block';
    $('#p-num').textContent = estado.atual.numero || cnj;
    $('#p-tags').innerHTML = `<span class="tag">${esc(estado.atual.tribunal)}</span>${estado.atual.situacao ? `<span class="tag cinza">${esc(estado.atual.situacao)}</span>` : ''}`;
    $('#sugeridos').innerHTML = '<div class="vazio">Carregando o acervo…</div>';
    try { await recarregarCtx(); } catch (e) { toast(e.message); return; }
    const c = estado.ctx;
    $('#p-desc').textContent = `${c.classe || ''} · ${c.assunto || 'sem assunto cadastrado'} · ${c.orgao || ''}`;
    renderPrecedentes(); renderNovidades(); montarPrompt();
  }

  /* ---------- eventos ---------- */
  function ligarEventos() {
    $('#busca-proc').addEventListener('input', renderLista);
    $('#lista-proc').addEventListener('click', (e) => { const el = e.target.closest('[data-cnj]'); if (el) abrirProcesso(el.dataset.cnj); });
    document.querySelectorAll('.aba').forEach((a) => a.addEventListener('click', () => {
      document.querySelectorAll('.aba').forEach((x) => x.classList.toggle('ativa', x === a));
      document.querySelectorAll('.painel').forEach((p) => p.classList.toggle('ativo', p.id === `aba-${a.dataset.aba}`));
    }));
    $('#busca-acervo').addEventListener('input', buscarAcervo);
    $('#busca-tarefa').addEventListener('input', renderTarefas);
    $('#lista-tarefas').addEventListener('click', (e) => { const el = e.target.closest('[data-tarefa]'); if (el) escolherTarefa(el.dataset.tarefa); });
    ['#opt-anon', '#opt-pubs', '#opt-movs'].forEach((s) => $(s).addEventListener('change', montarPrompt));
    $('#instrucao').addEventListener('input', montarPrompt);
    $('#btn-copiar').addEventListener('click', async () => {
      try { await navigator.clipboard.writeText($('#prompt').value); toast('Copiado. Cole no Claude.'); }
      catch { $('#prompt').select(); document.execCommand('copy'); toast('Copiado.'); }
    });
    $('#btn-abrir').addEventListener('click', () => window.open('https://claude.ai/new', '_blank', 'noopener'));
    $('#m-fechar').addEventListener('click', () => ($('#modal').style.display = 'none'));
    $('#modal').addEventListener('click', (e) => { if (e.target.id === 'modal') $('#modal').style.display = 'none'; });
    document.body.addEventListener('click', async (e) => {
      const b = e.target.closest('button'); if (!b) return;
      if (b.dataset.ver) { const [repo, path, tit] = b.dataset.ver.split('|'); verTexto(repo, path, tit); }
      if (b.dataset.vincular) {
        const listas = await Promise.all(['trabalho', 'civel', 'geral'].map(indice));
        const it = listas.flat().find((x) => x.id === b.dataset.vincular); if (it) vincular(it);
      }
      if (b.dataset.vincularNorma) {
        const [repo, path, tit] = b.dataset.vincularNorma.split('|');
        vincular({ id: `norma-${path}`, repo, path, tit, tipo: 'Legislação', trib: '', txt: '' });
      }
      if (b.dataset.desvincular) desvincular(b.dataset.desvincular);
    });
  }

  /* ---------- sessão ---------- */
  async function iniciar(sessao) {
    estado.token = sessao.access_token;
    $('#login').style.display = 'none'; $('#app').style.display = 'grid';
    $('#usuario').textContent = sessao.user?.email || '';
    const r = await sb.rpc('atlas_contencioso_law_processos');
    if (r.error) { $('#lista-proc').innerHTML = `<div class="pad vazio">${esc(r.error.message)}</div>`; return; }
    estado.processos = r.data || [];
    renderLista(); renderTarefas();
    const cnj = new URLSearchParams(location.search).get('cnj');
    if (cnj) abrirProcesso(cnj.replace(/\D/g, ''));
  }

  document.addEventListener('DOMContentLoaded', async () => {
    ligarEventos();
    sb.auth.onAuthStateChange((_ev, s) => { if (s) estado.token = s.access_token; });
    const { data } = await sb.auth.getSession();
    if (data.session) return iniciar(data.session);
    $('#login').style.display = 'block';
    $('#lg-btn').addEventListener('click', async () => {
      $('#lg-msg').textContent = 'Entrando…';
      const { data: d, error } = await sb.auth.signInWithPassword({ email: $('#lg-email').value.trim(), password: $('#lg-senha').value });
      if (error) { $('#lg-msg').textContent = 'E-mail ou senha inválidos.'; return; }
      iniciar(d.session);
    });
  });
})();
