/* ============================================================================
   book.js — the consultation request.

   Panels ship visible in the markup; this script hides all but the current one.
   With scripting off the page is one long form with a single submit, and every
   question is reachable. Nothing is gated behind JS.
   ========================================================================= */
(function () {
  'use strict';
  var form = document.getElementById('bookForm');
  if (!form) return;

  var panels = [].slice.call(form.querySelectorAll('.bpanel'));
  var steps  = [].slice.call(document.querySelectorAll('#bSteps li'));
  var live   = document.getElementById('bLive');
  var back   = document.getElementById('bBack');
  var next   = document.getElementById('bNext');
  var send   = document.getElementById('bSend');
  var review = document.getElementById('bReview');
  var notice = document.getElementById('bNotice');
  var done   = document.getElementById('bDone');
  var doneMsg= document.getElementById('bDoneMsg');
  var at = 0;
  var started = Date.now();

  /* The markup ships every panel visible and the submit button live, so without
     JavaScript the page is one long form that can actually be sent. Stepping is
     switched on only now that we are here to drive it. */
  next.hidden = false;

  /* form.name is HTMLFormElement's own IDL attribute (the form's name), NOT the
     control named "name" — reading el('name').value silently yields undefined and the
     validation never passes. Always go through form.elements. */
  var el = function (n) { return form.elements[n]; };

  var LABEL = { procedure: 'Procedure', timing: 'Timing', name: 'Name',
                email: 'Email', phone: 'Phone', language: 'Language', note: 'Note' };
  var LANG = { en: 'English', es: 'Español', ru: 'Русский' };

  /* the procedure can arrive pre-selected from a procedure page */
  (function preselect() {
    var m = /[?&]procedure=([\w-]+)/.exec(location.search);
    var want = m && m[1];
    var input = want && form.querySelector('input[name="procedure"][value="' + want + '"]');
    if (input) { input.checked = true; return; }
    var fallback = form.querySelector('input[name="procedure"][data-default]');
    if (fallback && !form.querySelector('input[name="procedure"]:checked')) fallback.checked = true;
  })();

  function show(i, announce) {
    at = Math.max(0, Math.min(panels.length - 1, i));
    panels.forEach(function (p, j) { p.hidden = j !== at; });
    steps.forEach(function (s, j) {
      s.classList.toggle('is-done', j < at);
      if (j === at) s.setAttribute('aria-current', 'step');
      else s.removeAttribute('aria-current');
    });
    back.hidden = at === 0;
    next.hidden = at === panels.length - 1;
    send.hidden = at !== panels.length - 1;
    if (at === panels.length - 1) fillReview();
    if (announce !== false) {
      live.textContent = 'Step ' + (at + 1) + ' of ' + panels.length;
      var legend = panels[at].querySelector('legend');
      if (legend) { panels[at].setAttribute('tabindex', '-1'); panels[at].focus(); }
    }
  }

  function err(id, on, msg) {
    var el = document.getElementById(id);
    if (!el) return;
    el.hidden = !on;
    if (msg) el.textContent = msg;
    var field = document.getElementById('f-' + id.slice(2));
    if (field) field.setAttribute('aria-invalid', on ? 'true' : 'false');
  }

  function emailOk(v) { return /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v); }

  function validate(step) {
    var ok = true;
    if (step === 0) {
      var chosen = !!form.querySelector('input[name="procedure"]:checked');
      err('e-procedure', !chosen); ok = chosen;
    }
    if (step === 1) {
      var t = !!form.querySelector('input[name="timing"]:checked');
      err('e-timing', !t); ok = t;
    }
    if (step === 2) {
      var n = el('name').value.trim(), e = el('email').value.trim();
      err('e-name', !n); err('e-email', !emailOk(e));
      ok = !!n && emailOk(e);
      if (!ok) (!n ? el('name') : el('email')).focus();
    }
    if (!ok) live.textContent = 'Check the highlighted answer';
    return ok;
  }

  function values() {
    var v = {};
    ['procedure', 'timing'].forEach(function (k) {
      var c = form.querySelector('input[name="' + k + '"]:checked');
      if (c) v[k] = c.parentNode.querySelector('.bopt__t').firstChild.textContent.trim();
    });
    v.name = el('name').value.trim();
    v.email = el('email').value.trim();
    if (el('phone').value.trim()) v.phone = el('phone').value.trim();
    v.language = LANG[el('language').value] || el('language').value;
    if (el('note').value.trim()) v.note = el('note').value.trim();
    return v;
  }

  function fillReview() {
    var v = values();
    review.innerHTML = '';
    Object.keys(LABEL).forEach(function (k) {
      if (!v[k]) return;
      var row = document.createElement('div');
      var dt = document.createElement('dt'); dt.textContent = LABEL[k];
      var dd = document.createElement('dd'); dd.textContent = v[k];
      row.appendChild(dt); row.appendChild(dd); review.appendChild(row);
    });
    if (!form.dataset.endpoint) {
      notice.hidden = false;
      notice.innerHTML = '<b>No destination is connected yet.</b> This preview has nowhere ' +
        'to deliver a request &mdash; his inbox or CRM has not been supplied. Pressing send ' +
        'will show you exactly what would be sent, and nothing will leave your browser.';
    }
  }

  next.addEventListener('click', function () { if (validate(at)) show(at + 1); });
  back.addEventListener('click', function () { show(at - 1); });

  /* advancing on Enter should not skip validation, and should not submit early */
  form.addEventListener('keydown', function (e) {
    if (e.key !== 'Enter') return;
    if (e.target.tagName === 'TEXTAREA') return;
    if (at < panels.length - 1) { e.preventDefault(); next.click(); }
  });

  ['name', 'email'].forEach(function (k) {
    el(k).addEventListener('blur', function () {
      if (k === 'name') err('e-name', !el('name').value.trim());
      else err('e-email', !!el('email').value.trim() && !emailOk(el('email').value.trim()));
    });
  });

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    for (var i = 0; i < panels.length - 1; i++) {
      if (!validate(i)) { show(i); return; }
    }
    /* honeypot, plus a time trap: a human does not complete this in three seconds */
    if (el('company').value || (Date.now() - started) < 3000) {
      live.textContent = '';
      return;
    }
    var v = values();
    if (form.dataset.endpoint) {
      send.disabled = true;
      live.textContent = 'Sending…';
      fetch(form.dataset.endpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(v)
      }).then(function (r) {
        if (!r.ok) throw new Error(r.status);
        finish('Sent. His office replies to every request, usually within a working day. ' +
               'A copy is on its way to ' + v.email + '.');
      }).catch(function () {
        send.disabled = false;
        live.textContent = '';
        notice.hidden = false;
        notice.innerHTML = '<b>That did not send.</b> Please call 786 795 2113 rather than ' +
          'trying again — it is faster, and someone answers.';
      });
    } else {
      finish('Nothing was sent, because no destination is connected to this preview yet. ' +
             'This is what would have gone: ' +
             Object.keys(LABEL).filter(function (k) { return v[k]; })
               .map(function (k) { return LABEL[k] + ': ' + v[k]; }).join(' · ') + '.');
    }
  });

  function finish(msg) {
    form.hidden = true;
    done.hidden = false;
    doneMsg.textContent = msg;
    done.focus();
  }

  show(0, false);
})();
