// Shared helper: auto-play, looping, speed-controlled animation for every interactive widget.
// Each widget that wants this behavior calls WidgetLoop.create(opts) with its own step/reset/atEnd functions.
window.WidgetLoop = (function () {
  function create(opts) {
    // opts = {
    //   runBtn:        DOM button (Play/Pause toggle) — required
    //   stepBtn:       DOM button — optional, pauses loop and does one step
    //   resetBtn:      DOM button — optional, pauses loop and resets state
    //   speedSlider:   DOM input[type=range] — optional
    //   speedLabel:    DOM element to show "1.5×" — optional
    //   doStep:        () => void  — perform one step of the animation
    //   atEnd:         () => boolean — true when the animation has completed
    //   doReset:       () => void  — restore initial state
    //   baseStepMs:    delay between steps at speed = 1× (default 2000)
    //   baseLoopMs:    pause after the animation ends before looping back (default 5000)
    //   autoStartMs:   ms after init before auto-play kicks in (default 1500). Pass false to disable auto-start.
    //   onPause:       optional callback when pausing
    //   onPlay:        optional callback when starting/resuming
    // }

    const baseStep = opts.baseStepMs ?? 2000;
    const baseLoop = opts.baseLoopMs ?? 5000;
    let runTimer = null, loopTimer = null, looping = false;

    function speed() {
      if (!opts.speedSlider) return 1;
      const v = parseFloat(opts.speedSlider.value);
      return v > 0 ? v : 1;
    }
    function clearTimers() {
      if (runTimer) clearTimeout(runTimer);
      if (loopTimer) clearTimeout(loopTimer);
      runTimer = null; loopTimer = null;
    }
    function setBtn() {
      if (opts.runBtn) opts.runBtn.textContent = looping ? '⏸ Pause' : '▶ Play';
    }
    function stop() {
      looping = false;
      clearTimers();
      setBtn();
      if (opts.onPause) try { opts.onPause(); } catch (_) {}
    }
    function start() {
      looping = true;
      clearTimers();
      setBtn();
      if (opts.onPlay) try { opts.onPlay(); } catch (_) {}
      if (opts.atEnd && opts.atEnd()) opts.doReset();
      const tick = () => {
        if (opts.atEnd && opts.atEnd()) {
          runTimer = null;
          if (looping) {
            loopTimer = setTimeout(() => {
              if (!looping) return;
              opts.doReset();
              start();
            }, baseLoop / speed());
          } else setBtn();
          return;
        }
        try { opts.doStep(); } catch (e) { stop(); return; }
        if (!looping) { setBtn(); return; }
        runTimer = setTimeout(tick, baseStep / speed());
      };
      runTimer = setTimeout(tick, Math.min(800, baseStep / speed()));
    }

    if (opts.runBtn) {
      opts.runBtn.onclick = () => { if (looping || runTimer) stop(); else start(); };
    }
    if (opts.stepBtn) {
      const orig = opts.stepBtn.onclick;
      opts.stepBtn.onclick = (ev) => { stop(); opts.doStep(); if (orig) orig(ev); };
    }
    if (opts.resetBtn) {
      const orig = opts.resetBtn.onclick;
      opts.resetBtn.onclick = (ev) => { stop(); opts.doReset(); if (orig) orig(ev); };
    }
    if (opts.speedSlider) {
      opts.speedSlider.addEventListener('input', () => {
        if (opts.speedLabel) {
          opts.speedLabel.textContent = speed().toFixed(2).replace(/\.?0+$/, '') + '×';
        }
      });
      // Initialize label
      if (opts.speedLabel) {
        opts.speedLabel.textContent = speed().toFixed(2).replace(/\.?0+$/, '') + '×';
      }
    }

    const autoStart = opts.autoStartMs ?? 1500;
    if (autoStart !== false) setTimeout(start, autoStart);

    return { start, stop, clearTimers, isLooping: () => looping };
  }

  // Helper to inject standard control HTML (speed slider + play/pause + step + reset).
  // Returns the elements created (for chaining).
  function controlsHTML(prefix, opts = {}) {
    const showStep = opts.showStep !== false;
    const showReset = opts.showReset !== false;
    return `
      <button class="btn play-btn" id="${prefix}-run">⏸ Pause</button>
      ${showStep ? `<button class="btn ghost" id="${prefix}-step">Step</button>` : ''}
      ${showReset ? `<button class="btn ghost" id="${prefix}-reset">Reset</button>` : ''}
      <label class="speed-control">Speed
        <input type="range" id="${prefix}-speed" min="0.25" max="3" step="0.25" value="1">
        <span id="${prefix}-speed-label" style="font-family: var(--mono); min-width: 28px;">1×</span>
      </label>
    `;
  }

  return { create, controlsHTML };
})();
