/* Progressive enhancement only. The complete narrative remains readable without JS. */
(() => {
  'use strict';
  const body = document.body;
  const rail = document.getElementById('rail');
  const menu = document.querySelector('.menu');
  const toast = document.getElementById('toast');
  let toastTimer;
  const notify = text => { if (!toast) return; toast.textContent = text; toast.classList.add('visible'); clearTimeout(toastTimer); toastTimer = setTimeout(() => toast.classList.remove('visible'), 3500); };
  const close = () => { rail?.classList.remove('open'); menu?.setAttribute('aria-expanded', 'false'); };
  menu?.addEventListener('click', () => { const open = rail?.classList.toggle('open'); menu.setAttribute('aria-expanded', String(Boolean(open))); });
  document.addEventListener('keydown', e => { if (e.key === 'Escape') { close(); menu?.focus(); } });
  document.addEventListener('click', e => { if (rail && menu && !rail.contains(e.target) && !menu.contains(e.target)) close(); });
  document.querySelectorAll('.toc a').forEach(a => a.addEventListener('click', close));
  document.querySelectorAll('[data-copy-target]').forEach(button => button.addEventListener('click', async () => {
    const target = document.getElementById(button.dataset.copyTarget);
    if (!target) return;
    try { if (!navigator.clipboard?.writeText) throw new Error('clipboard unavailable'); await navigator.clipboard.writeText(target.textContent.trim()); notify(body.dataset.copied); }
    catch { const selection = window.getSelection(); const range = document.createRange(); range.selectNodeContents(target); selection?.removeAllRanges(); selection?.addRange(range); notify(body.dataset.copyError); }
  }));
  const input = document.getElementById('prompt-search');
  const rows = Array.from(document.querySelectorAll('#prompt-library tbody tr'));
  const count = document.getElementById('prompt-count');
  const normalize = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLocaleLowerCase();
  input?.addEventListener('input', () => { const term = normalize(input.value.trim()); let visible = 0; rows.forEach(row => { row.hidden = !normalize(row.textContent).includes(term); if (!row.hidden) visible++; }); if (count) count.textContent = `${visible} / ${rows.length} ${body.dataset.countLabel}`; });
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => { entries.forEach(entry => { if (!entry.isIntersecting) return; document.querySelectorAll('.toc a').forEach(a => a.classList.toggle('active', a.getAttribute('href') === '#' + entry.target.id)); }); }, { rootMargin: '-12% 0px -65% 0px' });
    document.querySelectorAll('section.chapter').forEach(section => observer.observe(section));
  }
})();
