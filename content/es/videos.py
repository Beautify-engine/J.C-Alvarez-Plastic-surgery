# -*- coding: utf-8 -*-
"""/videos — the talk library. Spanish copy.

THE TITLES ARE NOT TRANSLATED, AND MUST NOT BE.

All 42 are real published works with real titles. The English strings on the
English page are YouTube's machine translations, recorded as such in
content/youtube-catalog.md — the originals are Spanish. Every card already
carries its true Spanish title in .vid__es, so on this site the .vid__en line is
a gloss for an English reader sitting under a Spanish headline they can already
read. It is dropped, not translated: translating it would invent a second title
for a video that has one.

The per-card "Español" chip goes with it. It marks the spoken language, which is
useful on the English site where it warns you what you are about to hear. All 42
say Español, so on the Spanish site it is 42 identical chips telling a Spanish
reader that Spanish videos are in Spanish.

Both are removed by rule rather than by editing src/public/videos.html, so the
English page keeps them.

If English talks are added later, restore the chip — the moment the set is mixed
it carries information again.
"""

DROP = [
  r'\s*<p class="vid__en">[^<]*</p>',
  r'\s*<span class="vid__lang">[^<]*</span>',
]

T = {
# ---- head ----
"Video Library — Dr. Julio Clavijo Alvarez":
  "Videoteca — Dr. Julio Clavijo Alvarez",
"Dr. Julio Clavijo Alvarez answers the questions patients actually ask — recovery, planning, and what each procedure really involves.":
  "El Dr. Julio Clavijo Alvarez responde las preguntas que los pacientes realmente hacen — recuperación, planificación, y en qué consiste de verdad cada procedimiento.",

# ---- hero ----
"He answers the questions before you have to ask.":
  "Responde las preguntas antes de que usted tenga que hacerlas.",
"42 videos, from ninety-second answers to a thirty-six minute patient story. Every one began as a question someone asked in consultation &mdash; how long until I can work, whether the gym undoes a BBL, what happens when a liposuction doesn&rsquo;t go to plan.":
  "42 videos, desde respuestas de noventa segundos hasta la historia de una paciente de treinta y seis minutos. Todos empezaron como una pregunta que alguien hizo en consulta &mdash; cuánto falta para volver al trabajo, si el gimnasio deshace un BBL, qué pasa cuando una liposucción no sale como estaba previsto.",
# The English page warns you the talks are in Spanish. Here that is the default,
# so the line becomes about the subtitles, which is the part still missing.
"Published in Spanish &middot; English subtitles in progress":
  "En su canal &middot; subtítulos automáticos, todavía sin revisar",

# ---- filters ----
"Filter videos by topic": "Filtrar videos por tema",
"All": "Todos",
"Planning & philosophy": "Planificación y filosofía",
"Recovery": "Recuperación",
"Liposuction": "Liposucción",
"Breast": "Senos",
"Face": "Rostro",
"Patient story": "Historia de una paciente",
}
