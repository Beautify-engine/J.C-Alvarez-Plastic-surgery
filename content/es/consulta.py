# -*- coding: utf-8 -*-
"""/consulta — the booking form. Spanish copy.

THE ONE RULE ON THIS PAGE: it must never read as though a request was sent when
it was not. The preview build has no destination connected, and the page says so
in three places. Every one of those keeps the negation first in Spanish —
"No se envió nada", "Todavía no hay un destino conectado" — because a sentence
that opens with reassurance and qualifies it later is read as reassurance. The
matching strings inside book.js are in content/es/_js.py and must agree with
these word for word; a patient who reads one thing on the page and another in
the confirmation stops trusting both.

Register: the form addresses her directly and briefly. "¿Qué le preocupa?",
"¿Más o menos cuándo?", "¿Cómo la contacta?" — questions, not field labels.
The English is deliberately short here and the Spanish must not pad it out.

"Tres preguntas" is a promise the form has to keep. It was "Four" across
thirteen pages until the form was rewritten to three; if the form changes again,
this number changes with it, on /contacto and every procedure page too.

The reviews are translated and labelled, matching /, /resultados and
/preparacion. Usernames and months are never translated.
"""

T = {
# ---- head ----
"Request a Consultation — Julio Clavijo Alvarez, MD, Miami":
  "Solicitar una consulta — Julio Clavijo Alvarez, MD, Miami",
"Request a consultation with Dr. Julio Clavijo Alvarez, board-certified plastic surgeon in Miami. Three questions, about a minute. No medical history, no photographs.":
  "Solicite una consulta con el Dr. Julio Clavijo Alvarez, cirujano plástico certificado en Miami. Tres preguntas, un minuto aproximadamente. Sin historial médico, sin fotografías.",

# ---- hero ----
"What bothers you, in your own words.": "Qué le molesta, con sus propias palabras.",
"Three questions, about a minute. His office replies to every request, usually within a working day.":
  "Tres preguntas, un minuto aproximadamente. Su consulta responde a todas las solicitudes, normalmente en un día hábil.",

# ---- restored draft ----
"We kept your answers from earlier. They are stored in this browser only.":
  "Guardamos sus respuestas de antes. Están solo en este navegador.",
"Start over": "Empezar de nuevo",

# ---- step 1 ----
"What are you considering?": "¿Qué está considerando?",
"Select as many as apply.": "Marque todas las que correspondan.",
"I&rsquo;m not sure yet": "Todavía no estoy segura",
"Choose at least one, or &ldquo;I&rsquo;m not sure yet&rdquo;.":
  "Elija al menos una, o «Todavía no estoy segura».",

# ---- step 2 ----
"Roughly when?": "¿Más o menos cuándo?",
"A window, not a date.": "Un margen, no una fecha.",
"As soon as possible": "Lo antes posible",
"In the next three months": "En los próximos tres meses",
"Three to six months": "De tres a seis meses",
"Just researching": "Solo estoy averiguando",

# ---- step 3 ----
"How should he reach you?": "¿Cómo la contacta?",
"So he can get back to you.": "Para poder responderle.",
"Your name": "Su nombre",
"Please give a name he can use.": "Indique un nombre que él pueda usar.",
"That does not look like an email address.": "Eso no parece una dirección de correo.",
"Anything he should know": "Algo que él deba saber",
"Please do not include medical history, medications or photographs here &mdash; this form is not a secure medical record.":
  "Por favor no incluya aquí historial médico, medicamentos ni fotografías &mdash; este formulario no es un expediente médico seguro.",
"Or call": "O llame al",

# ---- the brief rail ----
"Your request": "Su solicitud",
"Reply to": "Responder a",
"Nothing leaves this page until you press send.":
  "Nada sale de esta página hasta que usted pulse enviar.",

# ---- reviews ----
"In their words": "En sus palabras",
"Verbatim from": "Tomados de",

# ---- confirmation ----
"Nothing was sent &mdash; no destination is connected yet. This is the confirmation a real request produces.":
  "No se envió nada &mdash; todavía no hay un destino conectado. Esta es la confirmación que produce una solicitud real.",
"Thank you.": "Gracias.",
"His office will call you from": "Su consulta la llamará desde el",
"Usually within one working day. Save it now, so you know who is ringing &mdash; and if you miss the call, ring the same number back.":
  "Normalmente en un día hábil. Guárdelo ahora, para saber quién la llama &mdash; y si pierde la llamada, devuélvala a ese mismo número.",
"Save the number": "Guardar el número",
"people follow his work": "personas siguen su trabajo",

# ---- while you wait ----
"While you wait": "Mientras espera",
"See the results gallery": "Ver la galería de resultados",
"Cases by procedure, no form in the way.":
  "Casos por procedimiento, sin ningún formulario de por medio.",
"Read the preparation guide": "Leer la guía de preparación",
"What the ninety days before surgery actually involve.":
  "En qué consisten realmente los noventa días previos a la cirugía.",

# ---- the four reviews used only here, in their shortened form ----
"I was so scared to get my breast lift done due to seeing horrible results. I almost canceled &hellip; I&rsquo;m glad I went with it. The lining of the nipples look perfect, which was my biggest concern &hellip; I knew his work would speak for itself, how detailed he was during the pre-op drawing.":
  "Tenía mucho miedo de hacerme el levantamiento de senos porque había visto resultados horribles. Casi lo cancelo &hellip; Me alegra haber seguido adelante. El borde de los pezones quedó perfecto, que era lo que más me preocupaba &hellip; Sabía que su trabajo hablaría por sí solo, por lo detallado que fue al hacer el marcaje preoperatorio.",
"He gave me his number after surgery. When I texted him with my &ldquo;problem&rdquo;, he called INSTANTLY &hellip; I told him, I&rsquo;m a mother of four, I don&rsquo;t want too big, I don&rsquo;t want too small &hellip; He DEFINITELY understood the assignment.":
  "Me dio su número después de la cirugía. Cuando le escribí por mi «problema», me llamó AL INSTANTE &hellip; Le dije: soy madre de cuatro, no los quiero muy grandes ni muy pequeños &hellip; DEFINITIVAMENTE entendió la tarea.",
"My biggest concern with going under the knife was losing my uniqueness &hellip; From the beginning I expressed that I didn&rsquo;t want to look like a different person &hellip; I am simply blown away with how natural, and beautiful I look now.":
  "Lo que más me preocupaba de entrar al quirófano era perder lo que me hace única &hellip; Desde el principio dije que no quería parecer otra persona &hellip; Estoy simplemente maravillada de lo natural y lo bien que me veo ahora.",
"I asked about getting implants and he was like NO, you are young and you don&rsquo;t need it. Definitely the &ldquo;money&rdquo; is not his motor, he&rsquo;s thinking about you &hellip; He called me 3 hours after my surgery to check on me.":
  "Le pregunté por implantes y me dijo que NO, que era joven y no los necesitaba. El «dinero» definitivamente no es su motor, está pensando en ti &hellip; Me llamó 3 horas después de la cirugía para ver cómo seguía.",
"All of the pain and discomfort has been absolutely worth it. He called me a few hours after my surgery to check in on me and is always available to answer questions.":
  "Todo el dolor y la molestia valieron absolutamente la pena. Me llamó unas horas después de la cirugía para ver cómo estaba y siempre está disponible para responder preguntas.",
"Dr. Alvarez took a great amount of time with me to discuss what I wanted and how he would go about helping me achieve my goal &hellip; As usual he always calls you in the evening to check up on you.":
  "El Dr. Alvarez se tomó muchísimo tiempo conmigo para hablar de lo que yo quería y de cómo me iba a ayudar a lograrlo &hellip; Como siempre, llama por la noche para ver cómo sigues.",
", with the reviewer&rsquo;s handle and the month they posted it.":
  ", con el usuario de quien lo escribió y el mes en que lo publicó.",

# ---- form furniture and controls -------------------------------------------
# Every one of these was missed until tools/todo-es.py stopped guessing the
# language and started diffing against the English source. "Request a
# consultation." is the H1.
"Request a consultation.": "Solicite una consulta.",
"Consultation request": "Solicitud de consulta",
"Board-certified plastic surgeon &middot; Miami": "Cirujano plástico certificado &middot; Miami",
"Progress": "Progreso",
"Timing": "Fechas",
"Pick a rough window.": "Elija un margen aproximado.",
"Name": "Nombre",
"Phone": "Teléfono",
"optional": "opcional",
"Preferred language": "Idioma preferido",
"Back": "Atrás",
"Continue": "Continuar",
"Send request": "Enviar solicitud",
"Preview build.": "Versión de prueba.",
"Request received": "Solicitud recibida",
"Call now instead": "Mejor llame ahora",
"Previous review": "Reseña anterior",
"Next review": "Reseña siguiente",
"Patient reviews, horizontally scrollable": "Reseñas de pacientes, desplazables en horizontal",

# Verbatim by design, declared so they stop being reported as unfinished.
# "Company" is the honeypot field's label — it is never shown to a person, and
# renaming it would change what a bot sees, which is the whole trick.
"Company": None,
"English": None,
"Espa&ntilde;ol": None,
"Русский": None,
"Dr. Julio Clavijo Alvarez.": None,
"Julio Clavijo Alvarez, MD": None,
}
