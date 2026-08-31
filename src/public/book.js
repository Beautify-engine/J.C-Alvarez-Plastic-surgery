/* ============================================================================
   book.js — the consultation request.

   Panels ship visible in the markup; this script hides all but the current one.
   With scripting off the page is one long form with a single submit, and every
   question is reachable. Nothing is gated behind JS.

   Procedure is a checkbox group, not a radio group: combination cases are the
   norm in this practice, and a form that cannot say "tummy tuck and lipo"
   makes her pick one and explain the other in the note, or leave.
   ========================================================================= */
(function () {
  'use strict';
  var form = document.getElementById('bookForm');
  if (!form) return;

  var B      = window.BookBrief || null;
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
  var hint   = document.getElementById('bProcHint');
  var resume = document.getElementById('bResume');
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
  var procs = function () { return [].slice.call(form.querySelectorAll('input[name="procedure"]')); };
  var picked = function () { return procs().filter(function (i) { return i.checked; }); };
  /* Two shapes of option now carry a label: the image cards on step 01 (.pcard__t)
     and the hairline rows everywhere else (.bopt__t). firstChild skips the trailing
     <small>, which is a hint, not part of the answer. */
  var labelOf = function (input) {
    var t = input.parentNode.querySelector('.pcard__t, .bopt__t');
    return t ? t.firstChild.textContent.trim() : input.value;
  };

  var LABEL = { procedure: 'Procedure', timing: 'Timing', name: 'Name',
                email: 'Email', phone: 'Phone', language: 'Language', note: 'Note' };
  var STEP_OF = { procedure: 0, timing: 1, name: 2, email: 2, phone: 2, language: 2, note: 2 };
  var LANG = { en: 'English', es: 'Español', ru: 'Русский' };

  /* ---- procedure group --------------------------------------------------- */

  /* "I'm not sure yet" is an answer, not an addition. It clears the rest and the
     rest clear it, so the two can never be sent together. */
  form.addEventListener('change', function (e) {
    if (e.target.name === 'procedure') {
      if (e.target.checked) {
        var exclusive = e.target.hasAttribute('data-exclusive');
        picked().forEach(function (i) {
          if (i !== e.target && (exclusive || i.hasAttribute('data-exclusive'))) i.checked = false;
        });
      }
      if (e.target.checked) lastPick = e.target.value;
      hintProcedures();
      showVoice();
      err('e-procedure', false);
    }
    sync();
  });
  form.addEventListener('input', sync);

  /* Proof at the point of action: the review that matches what she just picked.
     Keyed to the most recent selection rather than to DOM order — pick a tummy tuck
     and then a rhinoplasty and it is the nose she is thinking about, so that is the
     quote to answer. Falls back to the general quote about his care; never to a
     review of a different procedure dressed up as hers. */
  var voice = document.getElementById('bVoiceQ');
  var quotes = voice ? [].slice.call(voice.querySelectorAll('.bvoice__q')) : [];
  var lastPick = null;
  function quoteFor(slug) {
    for (var i = 0; i < quotes.length; i++) {
      if (quotes[i].getAttribute('data-for').split(' ').indexOf(slug) > -1) return quotes[i];
    }
    return null;
  }
  function showVoice() {
    if (!quotes.length) return;
    var chosen = picked().map(function (i) { return i.value; });
    var hit = chosen.indexOf(lastPick) > -1 ? quoteFor(lastPick) : null;
    for (var i = 0; !hit && i < chosen.length; i++) hit = quoteFor(chosen[i]);
    var show = hit || quotes[quotes.length - 1];
    quotes.forEach(function (q) { q.hidden = q !== show; });
  }

  function hintProcedures() {
    var n = picked().filter(function (i) { return !i.hasAttribute('data-exclusive'); }).length;
    hint.textContent = n < 2 ? '' : n + ' selected.';
  }

  /* ---- state ------------------------------------------------------------- */

  function values() {
    var v = {};
    v.procedure = picked().map(labelOf);
    v.procedureIds = picked().map(function (i) { return i.value; });
    var t = form.querySelector('input[name="timing"]:checked');
    if (t) { v.timing = labelOf(t); v.timingId = t.value; }
    v.name = el('name').value.trim();
    v.email = el('email').value.trim();
    if (el('phone').value.trim()) v.phone = el('phone').value.trim();
    v.languageId = el('language').value;
    v.language = LANG[v.languageId] || v.languageId;
    if (el('note').value.trim()) v.note = el('note').value.trim();
    return v;
  }

  function sync() {
    var v = values();
    if (!B) return;
    B.paint(v);
    B.save({ procedure: v.procedureIds, timing: v.timingId, name: v.name, email: v.email,
             phone: v.phone || '', language: v.languageId, note: v.note || '' });
  }

  function restore(s) {
    if (!s) return false;
    var any = false;
    procs().forEach(function (i) {
      if ((s.procedure || []).indexOf(i.value) > -1) { i.checked = true; any = true; }
    });
    if (s.timing) {
      var t = form.querySelector('input[name="timing"][value="' + s.timing + '"]');
      if (t) { t.checked = true; any = true; }
    }
    ['name', 'email', 'phone', 'note'].forEach(function (k) {
      if (s[k]) { el(k).value = s[k]; any = true; }
    });
    if (s.language) el('language').value = s.language;
    return any;
  }

  /* The procedure can arrive pre-selected from a procedure page. That beats a
     restored draft, because it is what she just clicked. */
  (function init() {
    var restored = B && restore(B.load());
    var m = /[?&]procedure=([\w-]+)/.exec(location.search);
    var want = m && m[1];
    var input = want && form.querySelector('input[name="procedure"][value="' + want + '"]');
    if (input) { picked().forEach(function (i) { i.checked = false; }); input.checked = true; }
    else if (restored && resume) resume.hidden = false;
    if (B) document.getElementById('fSource').value = JSON.stringify(B.source());
    hintProcedures();
    showVoice();
    sync();
  })();

  if (resume) document.getElementById('bClear').addEventListener('click', function () {
    if (B) B.clear();
    form.reset();
    resume.hidden = true;
    hintProcedures(); showVoice(); sync(); show(0);
  });

  /* ---- stepping ---------------------------------------------------------- */

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
      panels[at].setAttribute('tabindex', '-1');
      panels[at].focus();
    }
  }

  function err(id, on, msg) {
    var node = document.getElementById(id);
    if (!node) return;
    node.hidden = !on;
    if (msg) node.textContent = msg;
    var field = document.getElementById('f-' + id.slice(2));
    if (field) field.setAttribute('aria-invalid', on ? 'true' : 'false');
  }

  function emailOk(v) { return /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v); }

  function validate(step) {
    var ok = true;
    if (step === 0) { ok = picked().length > 0; err('e-procedure', !ok); }
    if (step === 1) { ok = !!form.querySelector('input[name="timing"]:checked'); err('e-timing', !ok); }
    if (step === 2) {
      var n = el('name').value.trim(), e = el('email').value.trim();
      err('e-name', !n); err('e-email', !emailOk(e));
      ok = !!n && emailOk(e);
      if (!ok) (!n ? el('name') : el('email')).focus();
    }
    if (!ok) live.textContent = 'Check the highlighted answer';
    return ok;
  }

  /* ---- review ------------------------------------------------------------ */

  /* Every row carries its own way back to the question that produced it. A
     correction at the last moment is the most likely reason to abandon here. */
  function fillReview() {
    var v = values();
    review.textContent = '';
    Object.keys(LABEL).forEach(function (k) {
      var val = k === 'procedure' ? v.procedure.join(', ') : v[k];
      if (!val) return;
      var row = document.createElement('div');
      var dt = document.createElement('dt'); dt.textContent = LABEL[k];
      /* The button lives inside the <dd>. A <div> in a <dl> may hold only <dt>
         and <dd>, so a sibling <button> there is a spec violation — axe calls it,
         and a screen reader loses the row's structure. */
      var dd = document.createElement('dd');
      var txt = document.createElement('span'); txt.className = 'breview__v'; txt.textContent = val;
      var ed = document.createElement('button');
      ed.type = 'button'; ed.className = 'breview__edit'; ed.textContent = 'Edit';
      ed.setAttribute('aria-label', 'Edit ' + LABEL[k].toLowerCase());
      ed.addEventListener('click', function () { show(STEP_OF[k]); });
      dd.appendChild(txt); dd.appendChild(ed);
      row.appendChild(dt); row.appendChild(dd);
      review.appendChild(row);
    });
    if (!form.dataset.endpoint) {
      notice.hidden = false;
      notice.innerHTML = '<b>No destination is connected yet.</b> This preview has nowhere ' +
        'to deliver a request. Pressing send will show you exactly what would be sent, ' +
        'and nothing will leave your browser.';
    }
  }

  /* ---- navigation and submit --------------------------------------------- */

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
    if (el('company').value || (Date.now() - started) < 3000) { live.textContent = ''; return; }

    var v = values();
    v.source = B ? B.source() : {};
    v.elapsed = Math.round((Date.now() - started) / 1000);

    if (!form.dataset.endpoint) {
      finish('Nothing was sent, because no destination is connected to this preview yet. ' +
             'This is what would have gone: ' + flat(v) + '.');
      return;
    }
    send.disabled = true;
    live.textContent = 'Sending…';
    fetch(form.dataset.endpoint, {
      method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(v)
    }).then(function (r) {
      if (r.ok) {
        if (B) B.clear();
        finish('Sent. His office replies to every request, usually within a working day. ' +
               'A copy is on its way to ' + v.email + '.');
        return;
      }
      /* 503 means the endpoint is live but has no mailer configured yet — true of
         every preview build until his sending domain exists. Say that, rather than
         blaming her connection, and never claim a request was sent when it was not. */
      if (r.status === 503) {
        finish('Nothing was sent: this build has no mail destination connected yet. ' +
               'This is what would have gone: ' + flat(v) + '.');
        return;
      }
      throw new Error(r.status);
    }).catch(function () {
      send.disabled = false;
      live.textContent = '';
      notice.hidden = false;
      notice.innerHTML = '<b>That did not send.</b> Please call 786 795 2113 rather than ' +
        'trying again — it is faster, and someone answers.';
    });
  });

  function flat(v) {
    return Object.keys(LABEL)
      .map(function (k) { return [k, k === 'procedure' ? v.procedure.join(', ') : v[k]]; })
      .filter(function (p) { return p[1]; })
      .map(function (p) { return LABEL[p[0]] + ': ' + p[1]; }).join(' · ');
  }

  function finish(msg) {
    form.hidden = true;
    var brief = document.getElementById('bBrief');
    if (brief) brief.hidden = true;
    done.hidden = false;
    doneMsg.textContent = msg;
    done.focus();
  }

  show(0, false);
})();
