# -*- coding: utf-8 -*-
"""Copy that repeats across eight or more pages: the procedure-page template's
section headings, the recovery timeline, the candidacy control, the surgeon strip
and the booking summary.

Written once here and applied to every page before that page's own map, so the
nav, the CTAs and the shared furniture cannot drift between pages. A page map
that redefines one of these wins, which is the escape hatch for the odd page
that needs a different wording.

Register note: the site addresses the reader as *usted*, not *tú*. A surgical
consultation in Miami is a formal conversation, and *usted* also travels better
across the Cuban, Colombian, Venezuelan and Argentine Spanish his patients
speak. Keep it consistent — mixing the two reads as careless.
"""

T = {
# ---- page index / section names ----
"On this page": "En esta página",
"The operation": "La operación",
"Candidacy": "Candidatura",
"Recovery": "Recuperación",
"Your surgeon": "Su cirujano",
"Before you decide": "Antes de decidir",
"Before you decide.": "Antes de decidir.",
"Procedure": "Procedimiento",
"Result": "Resultado",
"Home": "Inicio",
"Breadcrumb": "Ruta de navegación",
"Next": "Siguiente",

# ---- the fact rail ----
"Operating time": "Duración de la cirugía",
"Back to desk work": "Vuelta al trabajo de oficina",
"Final result": "Resultado final",
"Cases on file": "Casos documentados",
"Most of it visible by 3": "La mayor parte visible a los 3",
"6 months": "6 meses",

# ---- operation section ----
"One operation, five moves.": "Una operación, cinco pasos.",
"Or hear him explain it": "O escúchelo explicarlo",

# ---- candidacy ----
"Five things he checks.": "Cinco cosas que revisa.",
"The same five he works through in the room. A surgeon who operates on everyone who asks is not selecting for results.":
  "Las mismas cinco que repasa en la consulta. Un cirujano que opera a todo el que se lo pide no está seleccionando por resultados.",
"Likely a candidate": "Probablemente es candidata",
"He&rsquo;ll ask you to wait": "Le pedirá que espere",
"Candidacy checks": "Criterios de candidatura",
"Previous check": "Criterio anterior",
"Next check": "Criterio siguiente",
"Nicotine-free": "Sin nicotina",
"Asymmetry": "Asimetría",

# ---- recovery timeline ----
"Recovery milestones": "Etapas de la recuperación",
"Drag the handle, or pick a milestone": "Arrastre el control, o elija una etapa",
"The first 24 hours": "Las primeras 24 horas",
"Day 1": "Día 1",
"Week 4": "Semana 4",
"Month 6": "Mes 6",
"Settled": "Estabilizado",
"Swelling": "Inflamación",
"Movement": "Movimiento",
"Moving again": "Volver a moverse",
"Driving": "Conducir",
"Exercise": "Ejercicio",
"Intimacy": "Intimidad",
"Work": "Trabajo",

# ---- surgeon strip ----
"The recovery is planned as carefully as the operation.":
  "La recuperación se planifica con el mismo cuidado que la operación.",
"A doctorate in surgery, years of laboratory work in cell biology, and hyperbaric oxygen therapy in his own practice. It is why the next section exists at all &mdash; and why he will turn you down if you are not prepared for it.":
  "Un doctorado en cirugía, años de trabajo de laboratorio en biología celular, y oxigenoterapia hiperbárica en su propia consulta. Por eso existe la siguiente sección &mdash; y por eso la rechazará si no está preparada para ella.",
"I&rsquo;m integrating all that knowledge to improve the quality of your healing after surgery.":
  "Estoy integrando todo ese conocimiento para mejorar la calidad de su recuperación después de la cirugía.",
"More about him": "Más sobre él",
"American Board of Plastic Surgery": "American Board of Plastic Surgery",
"Ph.D., Surgery": "Doctorado en Cirugía",

# ---- band ----
"At the consultation": "En la consulta",
"Every plan starts here &mdash; a conversation about proportion, yours, before anything is booked.":
  "Todo plan empieza aquí &mdash; una conversación sobre proporción, la suya, antes de reservar nada.",
"Dr. Alvarez in scrubs at his desk during a consultation":
  "El Dr. Alvarez, en uniforme quirúrgico, en su escritorio durante una consulta",
"Dr. Julio Clavijo Alvarez in his Miami office":
  "El Dr. Julio Clavijo Alvarez en su consulta de Miami",

# ---- costs and questions ----
"What it costs": "Lo que cuesta",
"Operating time and anaesthesia": "Tiempo de quirófano y anestesia",
"Still asked, often": "Lo que siguen preguntando",

# ---- related ----
"Often considered together": "Se suelen considerar juntos",

# ---- closing CTA and booking summary ----
"Ask him whether you&rsquo;re a candidate.": "Pregúntele si es candidata.",
"Four questions, about a minute. You are asking for an assessment, not committing to an operation &mdash; and if the answer is &ldquo;not yet,&rdquo; he will tell you that.":
  "Cuatro preguntas, un minuto aproximadamente. Está pidiendo una valoración, no comprometiéndose a una operación &mdash; y si la respuesta es «todavía no», se lo dirá.",
"Or call 786 795 2113": "O llame al 786 795 2113",
"What you&rsquo;re considering": "Lo que está considerando",
"Roughly when": "Más o menos cuándo",
"A window, not a date. Nothing is booked here.": "Un margen, no una fecha. Aquí no se reserva nada.",
"How to reach you": "Cómo contactarla",
"Name, email, phone, preferred language.": "Nombre, correo, teléfono e idioma preferido.",
"Review and send": "Revisar y enviar",
"You see everything before it goes.": "Usted lo ve todo antes de que se envíe.",
"We deliberately do not ask for medical history, medications, weight, or photographs. That belongs in the consultation with a surgeon, not in a marketing form.":
  "Deliberadamente no le pedimos historial médico, medicamentos, peso ni fotografías. Eso pertenece a la consulta con un cirujano, no a un formulario de marketing.",

# ---- brand / contact, unchanged ----
"J.C. Alvarez Plastic Surgery": "J.C. Alvarez Plastic Surgery",
}

# ---- site chrome: nav, footer, the sitewide CTA ----------------------------
# These were originally only in home.py, so every other page rendered an English
# nav under Spanish content. Chrome belongs here by definition — it is on all 22.
T.update({
"Skip to content": "Saltar al contenido",
"Request a Consultation": "Solicitar una consulta",
"Results": "Resultados",
"Procedures": "Procedimientos",
"Preparation": "Preparación",
"Videos": "Videoteca",
"About": "Sobre él",
"Contact": "Contacto",

# footer
"Explore": "Explorar",
"Preparation &amp; recovery": "Preparación y recuperación",
"Video library": "Videoteca",
"About Dr. Alvarez": "Sobre el Dr. Alvarez",
"Follow": "Síganos",
"His book": "Su libro",
"Privacy": "Privacidad",
"Accessibility": "Accesibilidad",
"Visit": "Visítenos",
"Address": "Dirección",
"Call us": "Llámenos",
"Email": "Correo",
"Consultations": "Consultas",
"Legal": "Legal",
"Primary": "Principal",
"Dr. JC Alvarez, Board Certified Plastic Surgeon": "Dr. JC Alvarez, cirujano plástico certificado",
"Individual results vary. Nothing on this site is medical advice or a guarantee of outcome. Surgery carries risk; every procedure is discussed in person before it is planned.":
  "Los resultados varían según la persona. Nada en este sitio constituye consejo médico ni garantía de resultado. Toda cirugía conlleva riesgos; cada procedimiento se conversa en persona antes de planificarse.",

# procedure names, used in nav, footers, related cards and breadcrumbs
"Brazilian Butt Lift": "Aumento de glúteos",
"Skinny BBL": "Skinny BBL",
"Breast Augmentation": "Aumento de senos",
"Breast Lift": "Levantamiento de senos",
"Breast Lift &amp; Augmentation": "Levantamiento y aumento de senos",
"Breast Lift & Augmentation": "Levantamiento y aumento de senos",
"Tummy Tuck": "Abdominoplastia",
"High-Definition Liposuction": "Liposucción de alta definición",
"HD Liposuction": "Liposucción de alta definición",
"Deep Facelift": "Levantamiento facial profundo",
"Deep Plane Facelift": "Levantamiento facial profundo",
"Rhinoplasty": "Rinoplastia",
"Eyelid Surgery": "Blefaroplastia",
"Scarless Eyelid Rejuvenation": "Párpados sin cicatrices",

# breadcrumb section names
"Body": "Cuerpo",
"Breast": "Senos",
"Face": "Rostro",
})
