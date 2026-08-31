/* ============================================================================
   procedure.js — shared behaviour for the 11 procedure pages.
   Every block guards on its own root node, so a page that omits a section
   costs nothing. No dependencies.
   ========================================================================= */
(function () {
  'use strict';
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var pad = function (n) { return String(n).padStart(2, '0'); };

  /* ---------- reveal on scroll: 12px, once, never on the way out ---------- */
  (function () {
    var els = [].slice.call(document.querySelectorAll('[data-reveal]'));
    if (!els.length) return;
    if (reduce || !('IntersectionObserver' in window)) {
      els.forEach(function (el) { el.classList.add('is-in'); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add('is-in');
        io.unobserve(e.target);
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.05 });
    els.forEach(function (el) { io.observe(el); });
  })();

  /* ---------- sticky page index: scrollspy ----------
     A section counts as current once its top passes just below the sticky bar,
     so the highlight changes at the moment the heading arrives, not late. */
  (function () {
    var idx = document.getElementById('pidx');
    if (!idx) return;
    var links = [].slice.call(idx.querySelectorAll('a[href^="#"]'));
    var sections = links.map(function (a) {
      return document.getElementById(a.getAttribute('href').slice(1));
    });
    if (sections.some(function (s) { return !s; })) return;

    var current = -1;
    function sync() {
      var line = idx.getBoundingClientRect().bottom + 8;
      var next = -1;
      for (var i = 0; i < sections.length; i++) {
        if (sections[i].getBoundingClientRect().top <= line) next = i;
      }
      if (next === current) return;
      current = next;
      links.forEach(function (a, i) {
        if (i === next) a.setAttribute('aria-current', 'true');
        else a.removeAttribute('aria-current');
      });
      // keep the active item visible in the horizontally scrolling rail
      if (next > -1 && idx.querySelector('ul').scrollWidth > idx.clientWidth) {
        links[next].scrollIntoView({ block: 'nearest', inline: 'center',
          behavior: reduce ? 'auto' : 'smooth' });
      }
    }
    // reading progress across the whole bar
    var prog = document.getElementById('pidxProg');
    function progress() {
      if (!prog) return;
      var h = document.documentElement.scrollHeight - innerHeight;
      prog.style.width = (h > 0 ? Math.min(100, Math.max(0, scrollY / h * 100)) : 0) + '%';
    }

    var ticking = false;
    addEventListener('scroll', function () {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function () { sync(); progress(); ticking = false; });
    }, { passive: true });
    addEventListener('resize', function () { sync(); progress(); });
    sync(); progress();
  })();

  /* ---------- case stage ----------
     One whole slide per case. The BEFORE/BOTH/AFTER control is gone with the split:
     each slide already carries both states, at matching scale, labelled. */
  (function () {
    var img = document.getElementById('caseImg');
    if (!img) return;
    var strip = document.getElementById('caseStrip');
    var num = document.getElementById('caseNum');
    var btns = [].slice.call(strip.querySelectorAll('button'));
    var total = btns.length;
    var at = 0;

    function show(i) {
      at = (i + total) % total;
      var thumb = btns[at].querySelector('img').getAttribute('src');
      img.src = thumb.replace(/-t\.jpg$/, '.jpg');
      img.alt = 'Case ' + (at + 1) + ' of ' + total + ', before and after';
      btns.forEach(function (b, j) {
        if (j === at) b.setAttribute('aria-current', 'true');
        else b.removeAttribute('aria-current');
      });
      if (num) num.textContent = pad(at + 1) + ' of ' + pad(total);
    }

    btns.forEach(function (b, i) {
      b.addEventListener('click', function () { show(i); });
    });
    var prev = document.getElementById('casePrev'), next = document.getElementById('caseNext');
    if (prev) prev.addEventListener('click', function () { show(at - 1); });
    if (next) next.addEventListener('click', function () { show(at + 1); });
    strip.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') { e.preventDefault(); show(at + 1); btns[at].focus(); }
      if (e.key === 'ArrowLeft') { e.preventDefault(); show(at - 1); btns[at].focus(); }
    });
    show(0);
  })();

  /* ---------- candidacy: five checks, one at a time ----------
     Same tablist contract as the recovery timeline: arrow keys, Home/End, roving
     tabindex, one visible panel. Prev/next are a convenience on top. */
  (function () {
    var dots = document.querySelector('.pchk__dots[role="tablist"]');
    if (!dots) return;
    var tabs = [].slice.call(dots.querySelectorAll('[role="tab"]'));
    var panels = tabs.map(function (t) {
      return document.getElementById(t.getAttribute('aria-controls'));
    });
    var posEl = document.getElementById('ckPos');
    var at = 0;

    function select(i, focus) {
      at = (i + tabs.length) % tabs.length;
      tabs.forEach(function (t, j) {
        t.setAttribute('aria-selected', String(j === at));
        t.tabIndex = j === at ? 0 : -1;
        panels[j].hidden = j !== at;
      });
      if (posEl) posEl.textContent = pad(at + 1) + ' / ' + pad(tabs.length);
      if (focus) tabs[at].focus();
    }

    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { select(i); });
      t.addEventListener('keydown', function (e) {
        var n = null;
        if (e.key === 'ArrowRight') n = i + 1;
        if (e.key === 'ArrowLeft') n = i - 1;
        if (e.key === 'Home') n = 0;
        if (e.key === 'End') n = tabs.length - 1;
        if (n === null) return;
        e.preventDefault();
        select(n, true);
      });
    });
    var prev = document.getElementById('ckPrev'), next = document.getElementById('ckNext');
    if (prev) prev.addEventListener('click', function () { select(at - 1); });
    if (next) next.addEventListener('click', function () { select(at + 1); });
    select(0);
  })();

  /* ---------- a filled testimonial slot: self-hosted, loads on click ---------- */
  (function () {
    var btn = document.querySelector('.pvt__frame--live');
    if (!btn) return;
    btn.addEventListener('click', function () {
      var v = document.createElement('video');
      v.src = btn.dataset.vid;
      v.controls = true; v.autoplay = true; v.loop = true; v.muted = true;
      v.playsInline = true; v.setAttribute('playsinline', '');
      btn.appendChild(v);
      var g = btn.querySelector('.pvt__glow'); if (g) g.remove();
      var p = v.play(); if (p && p.catch) p.catch(function () {});
    }, { once: true });
  })();

  /* ---------- recovery timeline ----------
     Real tab semantics underneath (arrow keys, Home/End, one visible panel), with a
     drag layer on top: the rail fills to the current milestone and the handle can be
     dragged, because a row of small circles did not read as operable. */
  (function () {
    var list = document.querySelector('.ptime__list[role="tablist"]');
    if (!list) return;
    var tabs = [].slice.call(list.querySelectorAll('[role="tab"]'));
    var panels = tabs.map(function (t) {
      return document.getElementById(t.getAttribute('aria-controls'));
    });
    var axis = document.getElementById('timeAxis');
    var fill = document.getElementById('timeFill');
    var thumb = document.getElementById('timeThumb');
    var at = 0;

    function tickCentre(i) {
      var d = tabs[i].querySelector('.ptime__tick') || tabs[i];
      var r = d.getBoundingClientRect(), a = axis.getBoundingClientRect();
      return r.left - a.left + r.width / 2;
    }
    function paint() {
      if (!axis || !fill || !thumb) return;
      var x = tickCentre(at);
      fill.style.width = x + 'px';
      thumb.style.left = x + 'px';
    }
    function select(i, focus) {
      at = i;
      tabs.forEach(function (t, j) {
        t.setAttribute('aria-selected', String(j === i));
        t.tabIndex = j === i ? 0 : -1;
        panels[j].hidden = j !== i;
      });
      paint();
      if (focus) tabs[i].focus();
    }

    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { select(i); });
      t.addEventListener('keydown', function (e) {
        var n = null;
        if (e.key === 'ArrowRight') n = (i + 1) % tabs.length;
        if (e.key === 'ArrowLeft') n = (i - 1 + tabs.length) % tabs.length;
        if (e.key === 'Home') n = 0;
        if (e.key === 'End') n = tabs.length - 1;
        if (n === null) return;
        e.preventDefault();
        select(n, true);
      });
    });

    if (axis) {
      var dragging = false;
      var nearest = function (clientX) {
        var a = axis.getBoundingClientRect(), x = clientX - a.left;
        var best = 0, bestD = Infinity;
        for (var i = 0; i < tabs.length; i++) {
          var d = Math.abs(tickCentre(i) - x);
          if (d < bestD) { bestD = d; best = i; }
        }
        return best;
      };
      axis.addEventListener('pointerdown', function (e) {
        if (e.button) return;
        dragging = true;
        axis.classList.add('is-drag');
        axis.setPointerCapture(e.pointerId);
        var n = nearest(e.clientX);
        if (n !== at) select(n);
      });
      axis.addEventListener('pointermove', function (e) {
        if (!dragging) return;
        e.preventDefault();
        var n = nearest(e.clientX);
        if (n !== at) select(n);
      });
      var stop = function (e) {
        if (!dragging) return;
        dragging = false;
        axis.classList.remove('is-drag');
        try { axis.releasePointerCapture(e.pointerId); } catch (err) {}
      };
      axis.addEventListener('pointerup', stop);
      axis.addEventListener('pointercancel', stop);
      addEventListener('resize', paint);
      list.addEventListener('scroll', paint, { passive: true });
    }

    select(0);
  })();

  /* ---------- the operation: five or six moves ----------
     The current step is the one whose centre sits nearest a reading line at 46% of
     the viewport. Activating a step plays its mark and advances the meter. */
  (function () {
    var list = document.getElementById('opSteps');
    if (!list) return;
    var bar = document.getElementById('opBar');
    var pos = document.getElementById('opPos');
    var steps = [].slice.call(list.children);
    var at = -1;

    function sync() {
      var line = innerHeight * 0.46, best = -1, bestD = Infinity;
      for (var i = 0; i < steps.length; i++) {
        var r = steps[i].getBoundingClientRect();
        if (r.bottom < 0 || r.top > innerHeight) continue;
        var d = Math.abs((r.top + r.height / 2) - line);
        if (d < bestD) { bestD = d; best = i; }
      }
      if (best === at) return;
      at = best;
      steps.forEach(function (s, i) { s.classList.toggle('is-active', i === best); });
      if (best > -1) {
        if (bar) bar.style.width = ((best + 1) / steps.length * 100) + '%';
        if (pos) pos.textContent = pad(best + 1) + ' / ' + pad(steps.length);
      }
    }

    var ticking = false;
    addEventListener('scroll', function () {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function () { sync(); ticking = false; });
    }, { passive: true });
    addEventListener('resize', sync);
    sync();
  })();

  /* ---------- talks: click-to-load, privacy-preserving YouTube ----------
     Nothing is fetched from Google until a row is pressed. youtube-nocookie
     keeps the tracking cookie off the page, and the video stays on his channel
     rather than being re-hosted here. */
  (function () {
    var box = document.getElementById('pvid');
    if (!box) return;
    box.addEventListener('click', function (e) {
      var row = e.target.closest('.pvid__row');
      if (!row) return;
      var id = row.dataset.yt;
      if (!id) return;

      var frame = document.createElement('div');
      frame.className = 'pvid__frame';
      var f = document.createElement('iframe');
      f.src = 'https://www.youtube-nocookie.com/embed/' + id +
              '?autoplay=1&rel=0&modestbranding=1';
      f.title = row.dataset.label || 'Video';
      f.allow = 'accelerometer; autoplay; encrypted-media; picture-in-picture';
      f.allowFullscreen = true;
      f.referrerPolicy = 'strict-origin-when-cross-origin';
      frame.appendChild(f);

      var src = document.createElement('a');
      src.className = 'pvid__src';
      src.href = 'https://www.youtube.com/watch?v=' + id;
      src.rel = 'noopener';
      src.target = '_blank';
      src.textContent = 'Watch on YouTube \u2197';

      box.replaceChildren(frame, src);
      f.focus();
    });
  })();
})();
