'use strict';
// Dependency-free progressive enhancement. No tracking, remote accounts or executable prompts.
(() => {
  const $ = (s, root = document) => root.querySelector(s);
  const $$ = (s, root = document) => [...root.querySelectorAll(s)];
  const normalize = value => String(value || '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  let toastTimer;
  function notify(text) {
    const el = $('#toast'); if (!el) return;
    el.textContent = text; el.classList.add('visible');
    clearTimeout(toastTimer); toastTimer = setTimeout(() => el.classList.remove('visible'), 2300);
  }
  async function copyText(text) {
    try {
      if (navigator.clipboard && window.isSecureContext) await navigator.clipboard.writeText(text);
      else {
        const field = document.createElement('textarea'); field.value = text; field.setAttribute('readonly', '');
        field.style.position = 'fixed'; field.style.opacity = '0'; document.body.appendChild(field);
        field.select(); const ok = document.execCommand('copy'); field.remove();
        if (!ok) throw new Error('clipboard unavailable');
      }
      notify('Copiado. Cole na conversa do agente.'); return true;
    } catch (_) {
      notify('Não foi possível copiar. Selecione e copie o texto visível.'); return false;
    }
  }
  document.addEventListener('click', async event => {
    const button = event.target.closest('[data-copy], [data-copy-target]'); if (!button) return;
    const target = button.dataset.copyTarget ? document.getElementById(button.dataset.copyTarget) : null;
    const text = target ? target.textContent : button.dataset.copy;
    if (!text) { notify('Texto indisponível. Abra o arquivo do procedimento.'); return; }
    if (await copyText(text.trim())) {
      const original = button.textContent; button.textContent = 'Copiado';
      setTimeout(() => { button.textContent = original; }, 1600);
    }
  });
  const menu = $('.menu-toggle'), sidebar = $('#sidebar');
  function setMenu(open) { if (!menu || !sidebar) return; sidebar.classList.toggle('open', open); menu.setAttribute('aria-expanded', String(open)); menu.setAttribute('aria-label', open ? 'Fechar navegação' : 'Abrir navegação'); }
  if (menu) menu.addEventListener('click', () => setMenu(menu.getAttribute('aria-expanded') !== 'true'));
  $$('.sidebar a').forEach(a => a.addEventListener('click', () => setMenu(false)));
  document.addEventListener('click', event => { if (sidebar && menu && !sidebar.contains(event.target) && !menu.contains(event.target)) setMenu(false); });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape') setMenu(false);
    if (event.key === '/' && !['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) {
      const search = $('#prompt-search'); if (search) { event.preventDefault(); search.focus(); }
    }
  });
  // Prompt cards are pre-rendered and remain accessible without JavaScript.
  let currentFilter = 'all';
  const search = $('#prompt-search'), cards = $$('[data-prompt-card]');
  function filterPrompts() {
    const q = normalize(search ? search.value : ''); let count = 0;
    cards.forEach(card => {
      const show = (currentFilter === 'all' || card.dataset.group === currentFilter) && normalize(card.dataset.search).includes(q);
      card.hidden = !show; if (show) count++;
    });
    if ($('#prompt-count')) $('#prompt-count').textContent = `${count} ${count === 1 ? 'procedimento encontrado' : 'procedimentos disponíveis'}`;
    if ($('#prompt-empty')) $('#prompt-empty').hidden = count > 0;
  }
  if (search) search.addEventListener('input', filterPrompts);
  $$('[data-filter]').forEach(button => button.addEventListener('click', () => {
    currentFilter = button.dataset.filter;
    $$('[data-filter]').forEach(x => { const selected = x === button; x.classList.toggle('active', selected); x.setAttribute('aria-pressed', String(selected)); });
    filterPrompts();
  }));
  // Private originals and scripts are never requested by this catalog.
  const capGrid = $('#cap-grid');
  if (capGrid) {
    let data = {skills: [], staff: []}, kind = 'skills', limit = 12;
    const capSearch = $('#cap-search'), more = $('#cap-more');
    function renderCatalog() {
      const q = normalize(capSearch.value);
      const results = data[kind].filter(x => normalize(`${x.name} ${x.category} ${x.description}`).includes(q));
      capGrid.replaceChildren();
      results.slice(0, limit).forEach(item => {
        const card = document.createElement('article'); card.className = 'cap-card';
        const category = document.createElement('small'); category.textContent = item.category.replace(/^\d+-/, '').replaceAll('-', ' ');
        const title = document.createElement('h3'); title.textContent = item.name;
        const description = document.createElement('p'); description.textContent = item.description;
        const state = document.createElement('span'); state.className = 'cap-state'; state.textContent = item.state;
        card.append(category, title, description, state); capGrid.appendChild(card);
      });
      $('#cap-count').textContent = results.length ? `${Math.min(limit, results.length)} de ${results.length} registros · sem instalação automática` : 'Nenhuma capacidade encontrada.';
      more.hidden = limit >= results.length;
    }
    capSearch.addEventListener('input', () => { limit = 12; renderCatalog(); });
    more.addEventListener('click', () => { limit += 12; renderCatalog(); });
    $$('[data-cap]').forEach(button => button.addEventListener('click', () => {
      kind = button.dataset.cap; limit = 12;
      $$('[data-cap]').forEach(x => { const selected = x === button; x.classList.toggle('active', selected); x.setAttribute('aria-pressed', String(selected)); });
      renderCatalog();
    }));
    fetch('assets/catalog.json').then(response => { if (!response.ok) throw new Error('catalog'); return response.json(); }).then(result => {
      if (!Array.isArray(result.skills) || !Array.isArray(result.staff)) throw new Error('schema'); data = result; renderCatalog();
    }).catch(() => { $('#cap-count').textContent = 'Não foi possível carregar o catálogo. Consulte os arquivos no GitHub.'; more.hidden = true; });
  }
})();
