'use strict';
(async () => {
  const byId = id => document.getElementById(id);
  const status = byId('status');
  const language = (document.documentElement && document.documentElement.dataset && document.documentElement.dataset.language) || 'pt';
  const messages = {
    pt: { copied: 'Comando copiado.', manual: 'Selecione e copie o texto manualmente.', unavailable: 'Personalização indisponível. Copie o comando padrão ou baixe o procedimento completo.' },
    en: { copied: 'Command copied.', manual: 'Select and copy the text manually.', unavailable: 'Customization unavailable. Copy the default command or download the full procedure.' },
    es: { copied: 'Comando copiado.', manual: 'Seleccione y copie el texto manualmente.', unavailable: 'Personalización no disponible. Copie el comando predeterminado o descargue el procedimiento completo.' }
  }[language] || {};
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
    status.textContent = messages.unavailable;
  }
  byId('copy').addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(byId('output').value);
      status.textContent = messages.copied;
    } catch (_) {
      byId('output').focus();
      byId('output').select();
      status.textContent = messages.manual;
    }
  });
})();
