// =================================================================
// Slide presentation layer
//
// Auto-paginates each module's <section> elements into slides.
// Adds prev/next navigation, slide counter, dots, keyboard shortcuts,
// progress bar, slide-title overlay, and an opt-out "scroll mode".
// =================================================================

(function () {
  // Wait until DOM ready
  function init() {
    const sections = Array.from(document.querySelectorAll('.wrap > section'));
    if (sections.length <= 1) return; // nothing to paginate

    // Storage helpers that work on file:// and opaque origins
    function safeGet(k) {
      try { return localStorage.getItem(k); } catch (_) { return null; }
    }
    function safeSet(k, v) {
      try { localStorage.setItem(k, v); } catch (_) {}
    }

    // Read persisted mode (default: paginated)
    const PREF_KEY = 'cc_presentation_mode';
    let mode = safeGet(PREF_KEY) || 'slides';

    // Read slide index from URL hash if present (#slide=3) or localStorage per-page
    const PAGE_KEY = 'cc_slide_' + location.pathname;
    let current = parseInt(safeGet(PAGE_KEY), 10) || 0;
    if (location.hash.match(/^#slide=(\d+)/)) {
      current = Math.max(0, Math.min(sections.length - 1, parseInt(RegExp.$1, 10) - 1));
    }
    if (current >= sections.length) current = 0;

    // ---- Title detection ----
    function titleFor(section, idx) {
      const h2 = section.querySelector('h2');
      if (h2) return h2.textContent.trim();
      const h3 = section.querySelector('h3');
      if (h3) return h3.textContent.trim();
      return 'Slide ' + (idx + 1);
    }

    // ---- Build UI ----
    function buildUI() {
      // Progress bar (top)
      const prog = document.createElement('div');
      prog.id = 'slide-progress';
      prog.innerHTML = '<div id="slide-progress-fill"></div>';
      document.body.appendChild(prog);

      // Slide title overlay (top-right)
      const overlay = document.createElement('div');
      overlay.id = 'slide-title-overlay';
      overlay.textContent = 'slide 1';
      document.body.appendChild(overlay);

      // Bottom nav bar
      const nav = document.createElement('div');
      nav.id = 'slide-nav';
      nav.innerHTML = `
        <button id="slide-prev" aria-label="Previous slide">← Prev</button>
        <div id="slide-dots" role="tablist"></div>
        <span id="slide-counter">1 / ${sections.length}</span>
        <button id="slide-mode" aria-label="Toggle slide/scroll mode" title="Toggle slide / scroll mode" style="background: var(--paper); color: var(--accent); border: 1px solid var(--rule-strong); min-width: 90px;">⤓ Scroll</button>
        <button id="slide-next" aria-label="Next slide">Next →</button>
      `;
      document.body.appendChild(nav);

      // Dots
      const dots = document.getElementById('slide-dots');
      for (let i = 0; i < sections.length; i++) {
        const d = document.createElement('div');
        d.className = 'dot';
        d.title = titleFor(sections[i], i);
        d.onclick = () => goTo(i);
        dots.appendChild(d);
      }

      // Buttons
      document.getElementById('slide-prev').onclick = prev;
      document.getElementById('slide-next').onclick = next;
      document.getElementById('slide-mode').onclick = toggleMode;

      // Keyboard
      document.addEventListener('keydown', (e) => {
        if (mode !== 'slides') return;
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA' || e.target.tagName === 'SELECT') return;
        if (e.key === 'ArrowLeft' || e.key === 'PageUp') { e.preventDefault(); prev(); }
        else if (e.key === 'ArrowRight' || e.key === 'PageDown' || e.key === ' ') { e.preventDefault(); next(); }
        else if (e.key === 'Home') { e.preventDefault(); goTo(0); }
        else if (e.key === 'End') { e.preventDefault(); goTo(sections.length - 1); }
        else if (e.key === 'Escape') { e.preventDefault(); toggleMode(); }
      });

      // Short keyboard hint
      const hint = document.createElement('div');
      hint.id = 'slide-hint';
      hint.textContent = '← → for slides · Esc for scroll mode';
      document.body.appendChild(hint);
      setTimeout(() => hint.classList.add('show'), 800);
      setTimeout(() => hint.classList.remove('show'), 4500);
    }

    function prev() { if (current > 0) goTo(current - 1); }
    function next() { if (current < sections.length - 1) goTo(current + 1); }

    function goTo(idx) {
      if (idx < 0 || idx >= sections.length) return;
      current = idx;
      applyState();
    }

    function applyState() {
      if (mode === 'slides') {
        document.body.classList.add('paginated');
        sections.forEach((s, i) => {
          s.classList.toggle('slide-active', i === current);
          // Add a slide-badge if not yet present
          if (!s.querySelector('.slide-badge')) {
            const badge = document.createElement('div');
            badge.className = 'slide-badge';
            badge.textContent = 'Slide ' + (i + 1) + ' of ' + sections.length;
            s.insertBefore(badge, s.firstChild);
          }
        });

        // Counter & dots
        document.getElementById('slide-counter').textContent = (current + 1) + ' / ' + sections.length;
        Array.from(document.querySelectorAll('#slide-dots .dot')).forEach((d, i) => {
          d.classList.toggle('active', i === current);
        });
        // Progress bar
        const fill = document.getElementById('slide-progress-fill');
        if (fill) fill.style.width = ((current + 1) / sections.length * 100) + '%';
        // Title overlay
        const ov = document.getElementById('slide-title-overlay');
        if (ov) ov.textContent = titleFor(sections[current], current);
        // Buttons
        document.getElementById('slide-prev').disabled = (current === 0);
        document.getElementById('slide-next').disabled = (current === sections.length - 1);
        document.getElementById('slide-mode').textContent = '⤓ Scroll';

        // Scroll to top of active slide
        try { window.scrollTo({ top: 0, behavior: 'smooth' }); } catch (_) {}

        // Persist
        safeSet(PAGE_KEY, String(current));
        try { history.replaceState(null, '', '#slide=' + (current + 1)); } catch (_) {}
      } else {
        // Scroll mode: show everything
        document.body.classList.remove('paginated');
        sections.forEach(s => s.classList.remove('slide-active'));
        document.getElementById('slide-mode').textContent = '▤ Slides';
        history.replaceState(null, '', location.pathname);
      }
    }

    function toggleMode() {
      mode = (mode === 'slides') ? 'scroll' : 'slides';
      localStorage.setItem(PREF_KEY, mode);
      applyState();
    }

    buildUI();
    applyState();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
