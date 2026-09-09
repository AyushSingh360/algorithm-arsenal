/**
 * Algorithm Arsenal — app.js
 * Full SPA logic: data loading, stats, galaxy, search/filter, detail panel.
 */

(function () {
  'use strict';

  /* ── Config ─────────────────────────────────────────────── */
  const GH_USER   = 'AyushSingh360';
  const GH_REPO   = 'algorithm-arsenal';
  const GH_BRANCH = 'main';
  const RAW_BASE  = `https://raw.githubusercontent.com/${GH_USER}/${GH_REPO}/${GH_BRANCH}/leetcode`;
  const LC_BASE   = 'https://leetcode.com/problems';

  const LANG_EXT = {
    '.py': 'python', '.cpp': 'cpp',   '.c': 'c',
    '.java': 'java', '.js': 'javascript', '.ts': 'typescript',
    '.go': 'go',     '.rs': 'rust',   '.cs': 'csharp',
    '.rb': 'ruby',   '.swift': 'swift',  '.sql': 'sql',
    '.sh': 'bash',   '.kt': 'kotlin', '.scala': 'scala',
  };

  /* ── State ──────────────────────────────────────────────── */
  let allProblems      = [];
  let filteredProblems = [];
  let currentProblem   = null;
  let activeTab        = 'problem';
  let activeSolLang    = null;          // index into currentProblem.files
  let solContents      = {};            // cached fetched code {filename: code}

  /* ── DOM refs ───────────────────────────────────────────── */
  const $ = id => document.getElementById(id);
  const el = {
    grid:          $('problems-grid'),
    galaxy:        $('galaxy-grid'),
    galaxyTooltip: $('galaxy-tooltip'),
    search:        $('search-input'),
    filterDiff:    $('filter-difficulty'),
    filterTopic:   $('filter-topic'),
    filterLang:    $('filter-language'),
    clearFilters:  $('clear-filters'),
    emptyClear:    $('empty-clear'),
    resultsCount:  $('results-count'),
    loadingState:  $('loading-state'),
    emptyState:    $('empty-state'),
    overlay:       $('detail-overlay'),
    panel:         $('detail-panel'),
    detailNum:     $('detail-number'),
    detailTitle:   $('detail-title'),
    detailBadges:  $('detail-badges'),
    detailBody:    $('detail-body'),
    detailClose:   $('detail-close'),
    statTotal:     $('stat-total'),
    statEasy:      $('stat-easy'),
    statMedium:    $('stat-medium'),
    statHard:      $('stat-hard'),
    diffBars:      $('diff-bars'),
    topicBars:     $('topic-bars'),
    langGrid:      $('lang-grid'),
  };

  /* ─────────────────────────────────────────────────────────
     Init
  ──────────────────────────────────────────────────────── */
  async function init() {
    setupEventListeners();
    await loadData();
  }

  /* ── Data loading ───────────────────────────────────────── */
  async function loadData() {
    try {
      const resp = await fetch('data/problems.json');
      if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
      allProblems = await resp.json();
      filteredProblems = [...allProblems];
      el.loadingState.hidden = true;
      onDataReady();
    } catch (err) {
      console.error('Failed to load problems.json:', err);
      el.loadingState.innerHTML = `
        <p style="color:var(--red)">⚠ Failed to load solutions data.</p>
        <p style="font-size:13px;color:var(--text-3)">
          Run <code style="font-family:var(--font-mono)">python .scripts/build_site_data.py</code>
          then push to trigger GitHub Pages rebuild.
        </p>`;
    }
  }

  function onDataReady() {
    populateFilterOptions();
    renderStats();
    renderGalaxy();
    renderGrid();
    animateCounters();
  }

  /* ── Filter options ─────────────────────────────────────── */
  function populateFilterOptions() {
    // Topics
    const topicSet = new Set();
    allProblems.forEach(p => p.topics?.forEach(t => topicSet.add(t)));
    const topics = [...topicSet].sort();
    topics.forEach(t => {
      const opt = document.createElement('option');
      opt.value = t; opt.textContent = t;
      el.filterTopic.appendChild(opt);
    });

    // Languages
    const langSet = new Set();
    allProblems.forEach(p => p.languages?.forEach(l => langSet.add(l)));
    [...langSet].sort().forEach(l => {
      const opt = document.createElement('option');
      opt.value = l; opt.textContent = l;
      el.filterLang.appendChild(opt);
    });
  }

  /* ── Stats ──────────────────────────────────────────────── */
  function renderStats() {
    const total  = allProblems.length;
    const easy   = allProblems.filter(p => p.difficulty === 'Easy').length;
    const medium = allProblems.filter(p => p.difficulty === 'Medium').length;
    const hard   = allProblems.filter(p => p.difficulty === 'Hard').length;

    // Difficulty bars
    el.diffBars.innerHTML = [
      { label: 'Easy',   count: easy,   cls: 'easy',   fill: 'easy-fill'   },
      { label: 'Medium', count: medium, cls: 'medium', fill: 'medium-fill' },
      { label: 'Hard',   count: hard,   cls: 'hard',   fill: 'hard-fill'   },
    ].map(({ label, count, cls, fill }) => `
      <div class="diff-bar-row">
        <span class="diff-bar-label" style="color:var(--${cls === 'easy' ? 'green' : cls === 'medium' ? 'amber' : 'red'})">${label}</span>
        <div class="diff-bar-track">
          <div class="diff-bar-fill ${fill}" data-pct="${total ? (count / total * 100).toFixed(1) : 0}"></div>
        </div>
        <span class="diff-bar-count">${count}</span>
      </div>`).join('');

    // Topic bars (top 12)
    const topicCount = {};
    allProblems.forEach(p => p.topics?.forEach(t => topicCount[t] = (topicCount[t] || 0) + 1));
    const sorted = Object.entries(topicCount).sort((a, b) => b[1] - a[1]).slice(0, 5);
    const maxTopic = sorted[0]?.[1] || 1;
    el.topicBars.innerHTML = sorted.map(([name, count]) => `
      <div class="topic-bar-row">
        <div class="topic-bar-inner">
          <span class="topic-name" title="${name}">${name}</span>
          <div class="topic-track">
            <div class="topic-fill" data-pct="${(count / maxTopic * 100).toFixed(1)}"></div>
          </div>
        </div>
        <span class="topic-count">${count}</span>
      </div>`).join('');

    // Language chips
    const langCount = {};
    allProblems.forEach(p => p.languages?.forEach(l => langCount[l] = (langCount[l] || 0) + 1));
    const langs = Object.entries(langCount).sort((a, b) => b[1] - a[1]);
    el.langGrid.innerHTML = langs.map(([lang, count]) => `
      <div class="lang-chip">
        <span>${lang}</span>
        <span class="lang-chip-count">${count}</span>
      </div>`).join('');

    // Animate bars after a short delay (allow DOM paint)
    setTimeout(() => {
      document.querySelectorAll('.diff-bar-fill, .topic-fill').forEach(bar => {
        bar.style.width = bar.dataset.pct + '%';
      });
    }, 200);
  }

  /* ── Animated counters ──────────────────────────────────── */
  function animateCounters() {
    const total  = allProblems.length;
    const easy   = allProblems.filter(p => p.difficulty === 'Easy').length;
    const medium = allProblems.filter(p => p.difficulty === 'Medium').length;
    const hard   = allProblems.filter(p => p.difficulty === 'Hard').length;

    const countTo = (el, target, duration = 1800) => {
      const start = performance.now();
      const tick = now => {
        const t = Math.min((now - start) / duration, 1);
        const eased = 1 - Math.pow(1 - t, 4); // ease-out quartic
        el.textContent = Math.round(eased * target).toLocaleString();
        if (t < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    };

    // Use IntersectionObserver to trigger when hero is visible
    const hero = document.querySelector('.hero-counters');
    const observer = new IntersectionObserver(entries => {
      if (entries[0].isIntersecting) {
        countTo(el.statTotal,  total,  1800);
        countTo(el.statEasy,   easy,   1600);
        countTo(el.statMedium, medium, 1700);
        countTo(el.statHard,   hard,   1500);
        observer.disconnect();
      }
    }, { threshold: 0.5 });
    observer.observe(hero);
  }

  /* ── Galaxy ─────────────────────────────────────────────── */
  function renderGalaxy() {
    const sorted = [...allProblems].sort((a, b) => a.id - b.id);
    const frag   = document.createDocumentFragment();

    sorted.forEach(p => {
      const dot = document.createElement('div');
      dot.className = `galaxy-dot ${(p.difficulty || 'unknown').toLowerCase()}`;
      dot.setAttribute('role', 'listitem');
      dot.dataset.id = p.id;
      dot.dataset.title  = `#${p.id} ${p.title}`;
      dot.dataset.diff   = p.difficulty || 'Unknown';
      dot.setAttribute('aria-label', `#${p.id} ${p.title} – ${p.difficulty || 'Unknown'}`);
      dot.tabIndex = 0;

      dot.addEventListener('click', () => openPanel(p));
      dot.addEventListener('keydown', e => { if (e.key === 'Enter') openPanel(p); });
      dot.addEventListener('mouseenter', showGalaxyTooltip);
      dot.addEventListener('mousemove',  moveGalaxyTooltip);
      dot.addEventListener('mouseleave', hideGalaxyTooltip);
      frag.appendChild(dot);
    });

    el.galaxy.appendChild(frag);
  }

  function showGalaxyTooltip(e) {
    const dot = e.currentTarget;
    el.galaxyTooltip.textContent = `${dot.dataset.title}  ·  ${dot.dataset.diff}`;
    el.galaxyTooltip.classList.add('visible');
    el.galaxyTooltip.removeAttribute('aria-hidden');
    moveGalaxyTooltip(e);
  }
  function moveGalaxyTooltip(e) {
    const x = e.clientX + 14, y = e.clientY - 32;
    el.galaxyTooltip.style.left = `${x}px`;
    el.galaxyTooltip.style.top  = `${y}px`;
  }
  function hideGalaxyTooltip() {
    el.galaxyTooltip.classList.remove('visible');
    el.galaxyTooltip.setAttribute('aria-hidden', 'true');
  }

  /* ── Problem Grid ───────────────────────────────────────── */
  function renderGrid() {
    el.grid.innerHTML = '';
    el.emptyState.hidden = true;

    if (filteredProblems.length === 0) {
      el.emptyState.hidden = false;
      el.resultsCount.textContent = '';
      return;
    }

    el.resultsCount.textContent =
      filteredProblems.length === allProblems.length
        ? `${allProblems.length} problems`
        : `${filteredProblems.length} of ${allProblems.length}`;

    const frag = document.createDocumentFragment();
    filteredProblems.forEach(p => frag.appendChild(buildCard(p)));
    el.grid.appendChild(frag);
  }

  function buildCard(p) {
    const diff     = p.difficulty || 'Unknown';
    const diffCls  = diff.toLowerCase();
    const topics   = (p.topics || []).slice(0, 3);
    const langs    = p.languages || [];

    const card = document.createElement('div');
    card.className = 'problem-card';
    card.setAttribute('role', 'listitem');
    card.dataset.diff = diff;
    card.tabIndex = 0;
    card.setAttribute('aria-label', `Problem ${p.id}: ${p.title}, ${diff}`);

    card.innerHTML = `
      <div class="card-top">
        <span class="card-num">#${String(p.id).padStart(4, '0')}</span>
        <span class="card-diff ${diffCls}">${diff}</span>
      </div>
      <h3 class="card-title">${escHtml(p.title)}</h3>
      ${topics.length ? `<div class="card-topics">${topics.map(t => `<span class="card-topic">${escHtml(t)}</span>`).join('')}${p.topics?.length > 3 ? `<span class="card-topic">+${p.topics.length - 3}</span>` : ''}</div>` : ''}
      <div class="card-bottom">${langs.map(l => `<span class="card-lang">${escHtml(l)}</span>`).join('')}</div>`;

    card.addEventListener('click', () => openPanel(p));
    card.addEventListener('keydown', e => { if (e.key === 'Enter') openPanel(p); });
    return card;
  }

  /* ── Filters & Search ───────────────────────────────────── */
  function applyFilters() {
    const query = el.search.value.trim().toLowerCase();
    const diff  = el.filterDiff.value;
    const topic = el.filterTopic.value;
    const lang  = el.filterLang.value;

    filteredProblems = allProblems.filter(p => {
      if (diff  !== 'all' && p.difficulty !== diff) return false;
      if (topic !== 'all' && !(p.topics || []).includes(topic)) return false;
      if (lang  !== 'all' && !(p.languages || []).includes(lang)) return false;
      if (query) {
        const haystack = `${p.id} ${p.title} ${(p.topics || []).join(' ')}`.toLowerCase();
        if (!haystack.includes(query)) return false;
      }
      return true;
    });

    renderGrid();
  }

  function clearFilters() {
    el.search.value       = '';
    el.filterDiff.value   = 'all';
    el.filterTopic.value  = 'all';
    el.filterLang.value   = 'all';
    filteredProblems = [...allProblems];
    renderGrid();
  }

  /* ── Detail Panel ───────────────────────────────────────── */
  function openPanel(p) {
    currentProblem = p;
    solContents    = {};
    activeSolLang  = p.files?.[0] ?? null;
    activeTab      = 'problem';

    // Header
    el.detailNum.textContent   = `#${p.id}`;
    el.detailTitle.textContent = p.title;
    const diff    = p.difficulty || 'Unknown';
    const diffCls = diff.toLowerCase();
    el.detailBadges.innerHTML = `
      <span class="card-diff ${diffCls}" style="font-size:12px">${diff}</span>
      ${(p.topics || []).slice(0, 4).map(t => `<span class="detail-topic-chip">${escHtml(t)}</span>`).join('')}`;

    // Tab state
    syncTabUI();
    renderPanelContent();

    el.overlay.hidden = false;
    document.body.style.overflow = 'hidden';

    // Focus close button for a11y
    setTimeout(() => el.detailClose.focus(), 350);
  }

  function closePanel() {
    el.overlay.hidden = true;
    document.body.style.overflow = '';
    currentProblem = null;
  }

  function syncTabUI() {
    document.querySelectorAll('.detail-tab').forEach(btn => {
      const active = btn.dataset.tab === activeTab;
      btn.classList.toggle('active', active);
      btn.setAttribute('aria-selected', active);
    });
  }

  function switchTab(tab) {
    activeTab = tab;
    syncTabUI();
    renderPanelContent();
  }

  async function renderPanelContent() {
    if (activeTab === 'problem') {
      await renderProblemTab();
    } else {
      await renderSolutionTab();
    }
  }

  async function renderProblemTab() {
    if (!currentProblem) return;
    const p = currentProblem;

    el.detailBody.innerHTML = `<div class="solution-loading"><div class="spinner"></div><p>Loading problem…</p></div>`;

    let html = '';
    if (p.hasReadme) {
      try {
        const url  = `${RAW_BASE}/${encodeURIComponent(p.folder)}/README.md`;
        const resp = await fetch(url);
        if (resp.ok) html = await resp.text();
      } catch (_) { /* fall through */ }
    }

    if (!html) {
      html = `<p style="color:var(--text-3)">Problem statement not available. 
        <a href="${LC_BASE}/${p.slug}/" target="_blank" rel="noopener" style="color:var(--cyan)">View on LeetCode ↗</a></p>`;
    }

    // Sanitise: strip <script> and <style> tags before injecting
    const clean = html
      .replace(/<script[\s\S]*?<\/script>/gi, '')
      .replace(/<style[\s\S]*?<\/style>/gi, '');

    el.detailBody.innerHTML = `
      <a class="leetcode-link" href="${LC_BASE}/${p.slug}/" target="_blank" rel="noopener">
        View on LeetCode ↗
      </a>
      <div class="problem-html">${clean}</div>`;
  }

  async function renderSolutionTab() {
    if (!currentProblem) return;
    const p = currentProblem;
    const files = p.files || [];

    if (files.length === 0) {
      el.detailBody.innerHTML = `<p style="color:var(--text-3);padding:40px 0;text-align:center">No solution files found.</p>`;
      return;
    }

    el.detailBody.innerHTML = `<div class="solution-loading"><div class="spinner"></div><p>Loading solution…</p></div>`;

    // Fetch current file
    const file = activeSolLang || files[0];
    if (!solContents[file]) {
      try {
        const url  = `${RAW_BASE}/${encodeURIComponent(p.folder)}/${encodeURIComponent(file)}`;
        const resp = await fetch(url);
        solContents[file] = resp.ok ? await resp.text() : '// Could not load file.';
      } catch (_) {
        solContents[file] = '// Network error loading file.';
      }
    }

    const ext      = file.slice(file.lastIndexOf('.'));
    const hlLang   = LANG_EXT[ext] || 'plaintext';
    const code     = solContents[file];
    const langName = p.languages[files.indexOf(file)] || file;

    let highlighted = '';
    try {
      highlighted = hljs.highlight(code, { language: hlLang }).value;
    } catch (_) {
      highlighted = escHtml(code);
    }

    el.detailBody.innerHTML = `
      <div class="solution-header">
        <div class="solution-lang-tabs">
          ${files.map((f, i) => `
            <button class="solution-lang-tab${f === file ? ' active' : ''}"
              data-file="${escHtml(f)}" data-idx="${i}">
              ${escHtml(p.languages[i] || f)}
            </button>`).join('')}
        </div>
        <button class="copy-btn" id="copy-btn" aria-label="Copy code">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
          Copy
        </button>
      </div>
      <div class="code-wrap">
        <pre><code class="language-${hlLang}" id="code-block">${highlighted}</code></pre>
      </div>`;

    // Lang tab switching
    el.detailBody.querySelectorAll('.solution-lang-tab').forEach(btn => {
      btn.addEventListener('click', async () => {
        activeSolLang = btn.dataset.file;
        await renderSolutionTab();
      });
    });

    // Copy button
    const copyBtn = $('copy-btn');
    copyBtn?.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(code);
        copyBtn.innerHTML = `<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg> Copied!`;
        copyBtn.classList.add('copied');
        setTimeout(() => {
          copyBtn.innerHTML = `<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg> Copy`;
          copyBtn.classList.remove('copied');
        }, 2000);
      } catch (_) { /* Clipboard API may not be available */ }
    });
  }

  /* ── Utility ────────────────────────────────────────────── */
  function escHtml(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  /* ── Event listeners ────────────────────────────────────── */
  function setupEventListeners() {
    // Search (debounced)
    let searchTimer;
    el.search?.addEventListener('input', () => {
      clearTimeout(searchTimer);
      searchTimer = setTimeout(applyFilters, 200);
    });

    // Filters
    el.filterDiff?.addEventListener('change',  applyFilters);
    el.filterTopic?.addEventListener('change', applyFilters);
    el.filterLang?.addEventListener('change',  applyFilters);

    // Clear buttons
    el.clearFilters?.addEventListener('click', clearFilters);
    el.emptyClear?.addEventListener('click',   clearFilters);

    // Detail panel close
    el.detailClose?.addEventListener('click', closePanel);
    el.overlay?.addEventListener('click', e => {
      if (e.target === el.overlay) closePanel();
    });

    // Detail tabs
    document.querySelectorAll('.detail-tab').forEach(btn => {
      btn.addEventListener('click', () => switchTab(btn.dataset.tab));
    });

    // Keyboard shortcuts
    document.addEventListener('keydown', e => {
      // '/' focuses search
      if (e.key === '/' && document.activeElement !== el.search) {
        e.preventDefault();
        el.search?.focus();
      }
      // Esc closes panel
      if (e.key === 'Escape' && !el.overlay.hidden) {
        closePanel();
      }
    });
  }

  /* ── Kick off ───────────────────────────────────────────── */
  document.addEventListener('DOMContentLoaded', init);
})();
