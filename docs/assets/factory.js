'use strict';
(async () => {
  const byId = id => document.getElementById(id);
  const status = byId('status');
  try {
    const response = await fetch('routes.json');
    if (!response.ok) throw new Error('catalog unavailable');
    const catalog = await response.json();
    const update = () => {
      const mode = byId('mode').value;
      const route = catalog.routes[mode];
      const data = {
        projeto: byId('target').value.trim() || 'projeto aberto; confirmar raiz',
        pedido: byId('request').value.trim() || route.goal,
        estudo_anexado: byId('attachment').checked
      };
      byId('output').value = route.template.replace(JSON.stringify(catalog.dummy, null, 2), () => JSON.stringify(data, null, 2));
      status.textContent = '';
    };
    ['mode', 'target', 'request', 'attachment'].forEach(id => byId(id).addEventListener('input', update));
    document.querySelectorAll('[data-mode]').forEach(button => button.addEventListener('click', () => {
      byId('mode').value = button.dataset.mode;
      byId('mode').dispatchEvent(new Event('input', { bubbles: true }));
      byId('target').focus();
      window.scrollTo({ top: byId('mode').getBoundingClientRect().top + window.scrollY - 24, behavior: 'smooth' });
    }));
    update();
  } catch (_) {
    status.textContent = 'Personalização indisponível. Copie o comando padrão ou baixe o procedimento completo.';
  }
  byId('copy').addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(byId('output').value);
      status.textContent = 'Comando copiado.';
    } catch (_) {
      byId('output').focus();
      byId('output').select();
      status.textContent = 'Selecione e copie o texto manualmente.';
    }
  });
})();
