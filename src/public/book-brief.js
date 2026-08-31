/* ============================================================================
   book-brief.js — three things the form needs but the step machine should not own:

     1. the brief that assembles beside the form as she answers
     2. save-and-resume, so a phone call mid-form does not cost the request
     3. where the request came from, captured silently

   Exposes window.BookBrief. Loads before book.js; if it is missing, book.js
   degrades to a plain stepped form rather than failing.
   ========================================================================= */
(function () {
  'use strict';

  var KEY = 'jca.book.v1';
  var TTL = 1000 * 60 * 60 * 24 * 14; /* two weeks; a surgical decision is slow */

  var panel = document.getElementById('bBrief');
  var cells = {};
  if (panel) {
    [].forEach.call(panel.querySelectorAll('[data-brief]'), function (el) {
      cells[el.getAttribute('data-brief')] = { el: el, last: null };
    });
  }

  /* ---- the brief --------------------------------------------------------- */

  function paint(v) {
    if (!panel) return;
    panel.hidden = false;
    set('procedure', v.procedure && v.procedure.length ? v.procedure.join(', ') : '');
    set('timing', v.timing || '');
    set('name', v.name || '');
    set('contact', v.email || v.phone || '');
  }

  /* An unanswered row keeps its height and reads as a prompt, so the panel never
     reflows as it fills — the whole point of reserving the space. */
  function set(key, text) {
    var cell = cells[key];
    if (!cell || cell.last === text) return;
    var first = cell.last === null;
    cell.last = text;
    cell.el.textContent = text || 'Not yet';
    cell.el.classList.toggle('is-empty', !text);
    if (text && !first) {
      cell.el.classList.remove('is-new');
      void cell.el.offsetWidth; /* restart the animation on a re-answer */
      cell.el.classList.add('is-new');
    }
  }

  /* ---- save and resume --------------------------------------------------- */

  function save(state) {
    try {
      localStorage.setItem(KEY, JSON.stringify({ t: Date.now(), s: state }));
    } catch (e) { /* private mode, or full. Losing a draft is not worth an error. */ }
  }

  function load() {
    try {
      var raw = localStorage.getItem(KEY);
      if (!raw) return null;
      var box = JSON.parse(raw);
      if (!box || !box.s || Date.now() - box.t > TTL) { clear(); return null; }
      return box.s;
    } catch (e) { return null; }
  }

  function clear() {
    try { localStorage.removeItem(KEY); } catch (e) {}
  }

  /* ---- where the request came from --------------------------------------- */

  /* Referrer, campaign and the procedure page that sent her. He has never had
     this: today a request arrives with no idea which page earned it. Nothing
     here is typed by the patient and none of it is shown back to her. */
  function source() {
    var q = new URLSearchParams(location.search);
    var out = {};
    ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term', 'gclid', 'fbclid']
      .forEach(function (k) { if (q.get(k)) out[k] = q.get(k).slice(0, 120); });
    if (q.get('procedure')) out.from_page = q.get('procedure').slice(0, 60);
    var ref = document.referrer;
    if (ref) {
      try {
        var u = new URL(ref);
        if (u.host !== location.host) out.referrer = u.host + u.pathname.slice(0, 80);
        else if (!out.from_page) out.from_page = u.pathname.slice(0, 80);
      } catch (e) {}
    }
    out.viewport = window.innerWidth + 'x' + window.innerHeight;
    return out;
  }

  window.BookBrief = {
    paint: paint, save: save, load: load, clear: clear, source: source,
    hasPanel: !!panel
  };
})();
