/* Only thirty metadata cards enter the DOM. All catalog content is literal text. */
(async () => {
  'use strict';
  const PAGE_SIZE = 30;
  const byId = id => document.getElementById(id);
  const status = byId('result-count');
  const labels = status.dataset;
  const records = byId('records');
  const controls = ['search', 'category', 'state', 'source'].map(byId);
  const normalize = value => String(value).normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  // Upstreams in this audited inventory are GitHub URLs; other hosts need review.
  function canonicalURL(value) {
    if (typeof value !== 'string' || /[\s\\\x00-\x1f\x7f]/.test(value)) return '';
    try {
      const url = new URL(value);
      return url.protocol === 'https:' && url.hostname === 'github.com' &&
        !url.username && !url.password && !url.port ? url.href : '';
    } catch { return ''; }
  }
  function element(tag, text, className) {
    const node = document.createElement(tag);
    if (text !== undefined) node.textContent = String(text);
    if (className) node.className = className;
    return node;
  }
  function card(entry) {
    const article = element('article', undefined, 'pathway record');
    article.append(element('h3', entry.name), element('p', entry.category), element('p', entry.state, 'small'));
    const source = element('p');
    const url = canonicalURL(entry.source);
    if (url) {
      const link = element('a', labels.upstream);
      link.href = url;
      link.rel = 'noopener noreferrer';
      source.append(link);
    } else source.textContent = labels.missing;
    const details = element('details');
    details.append(element('summary', `Metadata · ${entry.id}`), element('pre', JSON.stringify(entry, null, 2)));
    article.append(source, element('p', labels.rights, 'small'), details);
    return article;
  }
  status.textContent = labels.loading;
  records.setAttribute('aria-busy', 'true');
  try {
    const response = await fetch('metadata.json', {credentials: 'omit'});
    if (!response.ok) throw new Error('Catalog HTTP error');
    const data = await response.json();
    if (!Array.isArray(data.entries) || !data.entries.every(entry => entry && typeof entry === 'object')) throw new Error('Invalid catalog');
    const rows = data.entries.map(entry => ({entry, text: normalize(JSON.stringify(entry))}));
    let filtered = rows;
    let page = 0;
    function render() {
      const pages = Math.max(1, Math.ceil(filtered.length / PAGE_SIZE));
      page = Math.max(0, Math.min(page, pages - 1));
      records.replaceChildren(...filtered.slice(page * PAGE_SIZE, (page + 1) * PAGE_SIZE).map(row => card(row.entry)));
      status.textContent = `${filtered.length} / ${rows.length} ${labels.results} · ${labels.page} ${page + 1} / ${pages}`;
      byId('empty').hidden = filtered.length !== 0;
      byId('previous').disabled = page === 0;
      byId('next').disabled = page >= pages - 1;
    }
    function filter() {
      const [query, category, state, source] = controls.map(control => control.value);
      const words = normalize(query).trim().split(/\s+/).filter(Boolean);
      filtered = rows.filter(({entry, text}) => words.every(word => text.includes(word)) &&
        (!category || entry.category === category) && (!state || entry.state === state) &&
        (!source || entry.source_group === source));
      page = 0;
      render();
    }
    for (const control of controls) control.addEventListener(control.id === 'search' ? 'input' : 'change', filter);
    byId('reset').addEventListener('click', () => { controls.forEach(control => { control.value = ''; }); filter(); byId('search').focus(); });
    byId('previous').addEventListener('click', () => { page--; render(); });
    byId('next').addEventListener('click', () => { page++; render(); });
    render();
    byId('filters').hidden = false;
    byId('pagination').hidden = false;
  } catch {
    status.textContent = labels.error;
  } finally {
    records.setAttribute('aria-busy', 'false');
  }
})();
