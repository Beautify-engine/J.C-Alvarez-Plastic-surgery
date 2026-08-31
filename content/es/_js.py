# -*- coding: utf-8 -*-
"""Copy that lives in JavaScript rather than in markup.

The builder copied *.js across untouched, so every string the page writes at
runtime stayed English on the Spanish site: the gallery's result count, the
booking form's step announcements and its review screen, the "watch on YouTube"
link. None of it appears in the HTML, so no amount of checking the built pages
would have found it.

These are exact source-to-source edits rather than a text map, because several
are built by concatenation and Spanish does not take the same word order. The
gallery count is the clearest case: 'Showing ' + n + ' ' + name + ' cases'
cannot be translated string by string — it has to become
'Mostrando ' + n + ' casos de ' + name.

Every replacement is asserted to match exactly once, so a change to the English
source fails the build instead of silently shipping English.
"""

EDITS = {

"results.js": [
  # 'Showing 5 Rinoplastia cases' is not a Spanish sentence. Restructured.
  ("""    count.textContent = filter === 'all'
      ? 'Showing all ' + total + ' cases'
      : 'Showing ' + shown + ' ' + name + (shown === 1 ? ' case' : ' cases');""",
   """    count.textContent = filter === 'all'
      ? 'Mostrando los ' + total + ' casos'
      : 'Mostrando ' + shown + (shown === 1 ? ' caso de ' : ' casos de ') + name;"""),

  ("""    lbT.textContent = btn.querySelector('.gal__proc').textContent + ' · case '
                    + btn.querySelector('.gal__n').textContent;""",
   """    lbT.textContent = btn.querySelector('.gal__proc').textContent + ' · caso '
                    + btn.querySelector('.gal__n').textContent;"""),
],

"videos.js": [
  # The build now writes aria-label="Reproducir: …". Left as it was, this strips
  # nothing and every embedded player would be titled "Reproducir: <title>".
  ("f.title=btn.getAttribute('aria-label').replace(/^Play: /,'');",
   "f.title=btn.getAttribute('aria-label').replace(/^Reproducir: /,'');"),
],

"procedure.js": [
  ("f.title = row.dataset.label || 'Video';",
   "f.title = row.dataset.label || 'Video';"),
  ("src.textContent = 'Watch on YouTube \\u2197';",
   "src.textContent = 'Ver en YouTube \\u2197';"),
],


"book.js": [
  # NOTE: book.js is being rewritten by the client-side lead as this is written.
  # These edits are asserted against the file, so the build fails loudly if the
  # source moves again rather than shipping English. Expect one more pass here
  # once the form settles.
  ("live.textContent = 'Step ' + (at + 1) + ' of ' + panels.length;",
   "live.textContent = 'Paso ' + (at + 1) + ' de ' + panels.length;"),

  ("if (!ok) live.textContent = 'Check the highlighted answer';",
   "if (!ok) live.textContent = 'Revise la respuesta se\u00f1alada';"),

  ("live.textContent = 'Sending\u2026';",
   "live.textContent = 'Enviando\u2026';"),

  ("hint.textContent = n < 2 ? '' : n + ' selected.';",
   "hint.textContent = n < 2 ? '' : n + ' seleccionados.';"),

  ("if (h && v && v.name) h.textContent = 'Thank you, ' + v.name.split(' ')[0] + '.';",
   "if (h && v && v.name) h.textContent = 'Gracias, ' + v.name.split(' ')[0] + '.';"),

  # The confirmation's summary labels are built at runtime, so they shipped English on
  # the Spanish page with nothing in the markup to catch it. Terms match the ones already
  # on this page: "Fechas" as on the step rail, "Responder a" as in the brief.
  ("""      [['Considering', (v.procedure || []).join(', ')],
       ['Timing', v.timing],
       ['Replying to', v.email]].forEach(function (row) {""",
   """      [['Le interesa', (v.procedure || []).join(', ')],
       ['Fechas', v.timing],
       ['Responder a', v.email]].forEach(function (row) {"""),

  # The confirmation. It appears three times in the source with the same wording,
  # which is deliberate — one promise, not three.
  ("""      finish('His office reads every request and replies, usually within a working day.', v);
      return;""",
   """      finish('Su consulta lee todas las solicitudes y responde, normalmente en un d\u00eda h\u00e1bil.', v);
      return;"""),
  ("""        finish('His office reads every request and replies, usually within a working day. ' +
               'A copy is on its way to ' + v.email + '.', v);""",
   """        finish('Su consulta lee todas las solicitudes y responde, normalmente en un d\u00eda h\u00e1bil. ' +
               'Va una copia en camino a ' + v.email + '.', v);"""),
  ("""    finish('His office reads every request and replies, usually within a working day.',
           values());""",
   """    finish('Su consulta lee todas las solicitudes y responde, normalmente en un d\u00eda h\u00e1bil.',
           values());"""),

  # Both notices say plainly that nothing was or will be sent. Keep the negation
  # first in Spanish too: a preview must never read as though it delivered a
  # request it did not.
  ("""    notice.innerHTML = '<b>No destination is connected yet.</b> This preview has nowhere ' +
      'to deliver a request. Pressing send will show you exactly what would be sent, ' +
      'and nothing will leave your browser.';""",
   """    notice.innerHTML = '<b>Todav\u00eda no hay un destino conectado.</b> Esta vista previa no tiene ' +
      'a d\u00f3nde entregar una solicitud. Al pulsar enviar ver\u00e1 exactamente lo que se enviar\u00eda, ' +
      'y nada saldr\u00e1 de su navegador.';"""),

  ("""      notice.innerHTML = '<b>That did not send.</b> Please call 786 795 2113 rather than ' +
        'trying again — it is faster, and someone answers.';""",
   """      notice.innerHTML = '<b>Eso no se envi\u00f3.</b> Por favor llame al 786 795 2113 en vez de ' +
        'volver a intentarlo — es m\u00e1s r\u00e1pido, y alguien contesta.';"""),
],

"book-brief.js": [
  ("cell.el.textContent = text || 'Not yet';",
   "cell.el.textContent = text || 'Todav\\u00eda no';"),
],
}
