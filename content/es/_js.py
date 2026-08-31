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

"main.js": [
  ("f.title='Map showing 8400 SW 8th St, 4th Floor, Miami, Florida';",
   "f.title='Mapa que muestra 8400 SW 8th St, 4th Floor, Miami, Florida';"),
],

"book.js": [
  ("""  var LABEL = { procedure: 'Procedure', timing: 'Timing', name: 'Name',
                email: 'Email', phone: 'Phone', language: 'Language', note: 'Note' };""",
   """  var LABEL = { procedure: 'Procedimiento', timing: 'Fechas', name: 'Nombre',
                email: 'Correo', phone: 'Tel\\u00e9fono', language: 'Idioma', note: 'Nota' };"""),

  # Announced to screen readers on every step change.
  ("live.textContent = 'Step ' + (at + 1) + ' of ' + panels.length;",
   "live.textContent = 'Paso ' + (at + 1) + ' de ' + panels.length;"),

  ("if (!ok) live.textContent = 'Check the highlighted answer';",
   "if (!ok) live.textContent = 'Revise la respuesta se\\u00f1alada';"),

  ("ed.textContent = 'Edit';",
   "ed.textContent = 'Editar';"),

  # 'Edit ' + LABEL[k].toLowerCase() -> 'Editar ' + ... reads correctly in Spanish
  # for all seven labels ("editar procedimiento", "editar correo").
  ("ed.setAttribute('aria-label', 'Edit ' + LABEL[k].toLowerCase());",
   "ed.setAttribute('aria-label', 'Editar ' + LABEL[k].toLowerCase());"),

  ("live.textContent = 'Sending…';",
   "live.textContent = 'Enviando…';"),
],

"book-brief.js": [
  ("cell.el.textContent = text || 'Not yet';",
   "cell.el.textContent = text || 'Todav\\u00eda no';"),
],
}
