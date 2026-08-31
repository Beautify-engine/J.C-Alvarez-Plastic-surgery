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
"Driving again": "Volver a conducir",
"Back to training": "Volver a entrenar",
"Light walking starts immediately, to keep circulation moving.":
  "Caminar suave desde el primer momento, para mantener la circulación.",
"Low-impact training can usually begin.": "Normalmente se puede empezar entrenamiento de bajo impacto.",
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

# ---- the click-to-load map facade (homepage + /contacto) --------------------
T.update({
"Load interactive map &rarr;": "Cargar mapa interactivo &rarr;",
"8400 SW 8th St, Miami": "8400 SW 8th St, Miami",
"Map showing 8400 SW 8th St, 4th Floor, Miami, Florida":
  "Mapa que muestra 8400 SW 8th St, 4th Floor, Miami, Florida",
})

# ---- procedure-page template: furniture shared by all eleven ---------------
T.update({
# breadcrumb / hero eyebrow
"Body &middot; Miami, Florida": "Cuerpo &middot; Miami, Florida",
"Breast &middot; Miami, Florida": "Senos &middot; Miami, Florida",
"Face &middot; Miami, Florida": "Rostro &middot; Miami, Florida",
"General anaesthesia": "Anestesia general",
"See his cases &rarr;": "Ver sus casos &rarr;",

# the case stage
"Case": "Caso",
"A result, in motion.": "Un resultado, en movimiento.",
"Private preview &mdash; these cases are not cleared for public display.":
  "Vista privada &mdash; estos casos no están autorizados para publicación.",

# recovery section
"Six months, told honestly.": "Seis meses, contados con honestidad.",
"Most of what people want to know is scheduling: when can I shower, drive, work, train, be seen.":
  "Casi todo lo que la gente quiere saber es calendario: cuándo puedo ducharme, conducir, trabajar, entrenar, dejarme ver.",
"Day 5": "Día 5",
"Week 2": "Semana 2",
"Week 6": "Semana 6",
"Week 8": "Semana 8",
"Month 3": "Mes 3",
"Washing": "Higiene",
"Sleeping": "Dormir",
"Support": "Sujeción",
"First shower": "Primera ducha",
"Back to a desk": "Vuelta al escritorio",
"Physical work": "Trabajo físico",
"Compression": "Compresión",
"Compression eases": "La compresión se reduce",
"Training": "Entrenamiento",
"What people see": "Lo que se nota",
"Numbness": "Adormecimiento",
"Scar": "Cicatriz",
"Still maturing. Scars continue to fade well past a year.":
  "Todavía madurando. Las cicatrices siguen aclarándose mucho después del año.",
"Sensation is still returning. This is normal and it is slow.":
  "La sensibilidad sigue volviendo. Es normal, y es lento.",

# risks that recur across procedures
"A permanent scar": "Una cicatriz permanente",
"Bleeding and infection": "Sangrado e infección",
"Managed with technique and monitoring, not eliminated.":
  "Se manejan con técnica y seguimiento; no se eliminan.",
"Deep vein thrombosis": "Trombosis venosa profunda",
"An outcome that needs revision": "Un resultado que necesita revisión",
"Some results need a second, smaller procedure. Ask what that costs before you book, not after.":
  "Algunos resultados necesitan un segundo procedimiento, más pequeño. Pregunte cuánto cuesta antes de reservar, no después.",
"Fluid collection (seroma)": "Acumulación de líquido (seroma)",

# cost block
"Every quote is built from the same six things. Ask for them itemised &mdash; a single number tells you nothing about what is in it.":
  "Todo presupuesto se arma con las mismas seis cosas. Pídalo desglosado &mdash; una cifra sola no le dice nada de lo que incluye.",
"Facility fee": "Costo del quirófano",
"Garments, drains and the follow-up schedule": "Prendas de compresión, drenajes y las citas de seguimiento",

# closing
"Dr. Julio Clavijo Alvarez": "Dr. Julio Clavijo Alvarez",
})

# ---- alt text and announced labels -----------------------------------------
# Alt text is the part of a page nobody screenshots, so it was the last English
# left on a finished Spanish page. A screen-reader user on the Spanish site was
# hearing every image described in English.
T.update({
"Choose a case": "Elija un caso",
"Previous case": "Caso anterior",
"Next case": "Caso siguiente",
"Gloved hands marking the incision plan for a breast lift with augmentation":
  "Manos con guantes marcando el plan de incisión para un levantamiento con aumento de senos",
"Hands assessing abdominal skin laxity before an abdominoplasty":
  "Manos evaluando la flacidez de la piel abdominal antes de una abdominoplastia",
"Profile view of a marked waist and hip before body contouring":
  "Vista de perfil de una cintura y una cadera marcadas antes de un contorno corporal",
"A surgeon holding two breast implants, one smooth and one textured":
  "Un cirujano sosteniendo dos implantes mamarios, uno liso y uno texturizado",
"A hand resting at the d&eacute;colletage before a breast lift consultation":
  "Una mano apoyada en el escote antes de una consulta de levantamiento de senos",
"A surgeon marking contour lines before a Brazilian butt lift":
  "Un cirujano marcando líneas de contorno antes de un aumento de glúteos",
"A surgeon marking contour lines for a Brazilian butt lift":
  "Un cirujano marcando líneas de contorno para un aumento de glúteos",
"A surgeon marking definition lines for high-definition liposuction":
  "Un cirujano marcando líneas de definición para una liposucción de alta definición",
"A surgeon marking muscle definition lines for high-definition liposuction":
  "Un cirujano marcando líneas de definición muscular para una liposucción de alta definición",
"A surgeon marking the upper eyelid crease before blepharoplasty":
  "Un cirujano marcando el pliegue del párpado superior antes de una blefaroplastia",
"A gloved hand steadying the brow above a closed eye before lower-eyelid surgery":
  "Una mano con guante sujetando la ceja sobre un ojo cerrado antes de una cirugía de párpado inferior",
"A surgeon assessing the profile of a nose before rhinoplasty":
  "Un cirujano evaluando el perfil de una nariz antes de una rinoplastia",
"Profile view of a nose, assessed in consultation":
  "Vista de perfil de una nariz, evaluada en consulta",
"Pre-operative facial markings drawn before surgery":
  "Marcas faciales preoperatorias dibujadas antes de la cirugía",
"Pre-operative facial markings drawn before a deep plane facelift":
  "Marcas faciales preoperatorias dibujadas antes de un levantamiento facial profundo",
"Dr. Julio Clavijo Alvarez, photographed against a plain background":
  "El Dr. Julio Clavijo Alvarez, fotografiado sobre un fondo liso",
"Dr. Alvarez at his desk during a consultation":
  "El Dr. Alvarez en su escritorio durante una consulta",
"Dr. Alvarez writing at his desk during a consultation":
  "El Dr. Alvarez escribiendo en su escritorio durante una consulta",
"Dr. Alvarez reviewing a chart before surgery":
  "El Dr. Alvarez revisando una historia clínica antes de una cirugía",
"Dr. Alvarez marking a patient before surgery":
  "El Dr. Alvarez marcando a una paciente antes de la cirugía",
"Certified by the American Board of Plastic Surgery":
  "Certificado por el American Board of Plastic Surgery",

# Society names are proper nouns and stay in English — a Spanish rendering would
# read as a different, non-existent body.
"American Society of Plastic Surgeons": None,
"American College of Surgeons": None,
})


# ---- patient reviews, TRANSLATED at the client-side lead's instruction ----
# Shared, not page-local: the same six quotes appear on / and on /resultados.
# Translated twice they would drift, and two Spanish versions of one real
# person's words is worse than one.
# These were previously left verbatim: they are real people's words, quoted from his
# RealSelf profile, and translating a quotation changes it. Translated here on request.
# Consequence handled: the section note no longer claims the quotes are "textual" —
# it now says they come from RealSelf and are translated from English, which is true.
T.update({
"Every quote below is verbatim from": "Cada testimonio proviene de",
"his RealSelf profile": "su perfil de RealSelf &middot; traducidos del inglés",

"I was so scared to get my breast lift done due to seeing horrible results. I almost canceled … I'm glad I went with it. My breasts aren't even healed and they look amazing. The lining of the nipples look perfect, which was my biggest concern … I knew his work would speak for itself, how detailed he was during the pre-op drawing.":
 "Tenía mucho miedo de hacerme el levantamiento de senos porque había visto resultados horribles. Casi lo cancelo … Me alegra haber seguido adelante. Mis senos ni siquiera han terminado de sanar y se ven increíbles. El borde de los pezones quedó perfecto, que era lo que más me preocupaba … Sabía que su trabajo hablaría por sí solo, por lo detallado que fue al hacer el marcaje preoperatorio.",

"He gave me his number after surgery. When I texted him with my \"problem\", he called INSTANTLY … I recovered so quickly; by day three I felt EXCELLENT. I told him, I'm a mother of four, I don't want too big, I don't want too small … He DEFINITELY understood the assignment.":
 "Me dio su número después de la cirugía. Cuando le escribí por mi «problema», me llamó AL INSTANTE … Me recuperé rapidísimo; al tercer día me sentía EXCELENTE. Le dije: soy madre de cuatro, no los quiero muy grandes ni muy pequeños … DEFINITIVAMENTE entendió la tarea.",

"The pain has been at a minimum and Tylenol is all I've been taking since surgery. I was really nervous about the pain at first but turns out it's totally manageable.":
 "El dolor ha sido mínimo y desde la cirugía solo he tomado Tylenol. Al principio estaba muy nerviosa por el dolor, pero resulta que es totalmente manejable.",

"My biggest concern with going under the knife was losing my uniqueness … From the beginning I expressed that I didn't want to look like a different person … I am simply blown away with how natural, and beautiful I look now.":
 "Lo que más me preocupaba de entrar al quirófano era perder lo que me hace única … Desde el principio dije que no quería parecer otra persona … Estoy simplemente maravillada de lo natural y lo bien que me veo ahora.",

"I asked about getting implants and he was like NO, you are young and you don't need it. Definitely the \"money\" is not his motor, he's thinking about you … He called me 3 hours after my surgery to check on me.":
 "Le pregunté por implantes y me dijo que NO, que era joven y no los necesitaba. El «dinero» definitivamente no es su motor, está pensando en ti … Me llamó 3 horas después de la cirugía para ver cómo seguía.",

"He took his time and explained the process, told me what to expect along the way and what the expected outcome would be … My arms look better at 59 years old than they did in my 20's.":
 "Se tomó su tiempo y me explicó el proceso, qué esperar en cada etapa y cuál sería el resultado … Mis brazos se ven mejor a los 59 años que a los 20.",

"Be prepared to feel uncomfortable, sore and swollen — all normal parts of recovery … All of the pain and discomfort has been absolutely worth it. He called me a few hours after my surgery to check in on me and is always available to answer questions.":
 "Prepárese para sentirse incómoda, adolorida e inflamada — todo eso es parte normal de la recuperación … Todo el dolor y la molestia valieron absolutamente la pena. Me llamó unas horas después de la cirugía para ver cómo estaba y siempre está disponible para responder preguntas.",

"He was very patient and kind regarding my surgical and anesthesia-related anxiety … I later learned that my nose was one of his most complex rhinoplasty cases, which required him to completely rebuild my nose internally and externally.":
 "Fue muy paciente y amable con mi ansiedad por la cirugía y la anestesia … Después supe que mi nariz fue uno de sus casos de rinoplastia más complejos, y tuvo que reconstruírmela por completo por dentro y por fuera.",

"I consider it a blessing to have gone on my breast cancer journey with Dr. Clavijo and his staff … His kindness, compassion, and sense of humor took the horribleness out of a devastating diagnosis.":
 "Considero una bendición haber pasado por mi proceso de cáncer de mama con el Dr. Clavijo y su equipo … Su amabilidad, su compasión y su sentido del humor le quitaron lo terrible a un diagnóstico devastador.",

"I worked out 6 days a week and could not get the body I wanted. Dr. Alvarez took a great amount of time with me to discuss what I wanted and how he would go about helping me achieve my goal … As usual he always calls you in the evening to check up on you.":
 "Entrenaba 6 días a la semana y aun así no lograba el cuerpo que quería. El Dr. Alvarez se tomó muchísimo tiempo conmigo para hablar de lo que yo quería y de cómo me iba a ayudar a lograrlo … Como siempre, llama por la noche para ver cómo sigues.",

"From the initial consultation to the procedure to all of the follow-up appointments and care — he takes his time, explains everything, and truly cares about his patients.":
 "Desde la consulta inicial hasta el procedimiento y todas las citas de seguimiento — se toma su tiempo, lo explica todo, y de verdad se preocupa por sus pacientes.",
})


# ---- review metadata and case labels, shared by / and /resultados -----------
# Both pages carry the same six quotes with the same month, procedure label and
# case numbering. Generated rather than listed so a case added to the gallery
# does not need a copy edit.
# ---- generated: 64 case alt strings, one pattern ----
PROC = {"Brazilian Butt Lift":"aumento de glúteos", "Breast Augmentation":"aumento de senos",
        "Tummy Tuck":"abdominoplastia", "Rhinoplasty":"rinoplastia",
        "Eyelid Surgery":"blefaroplastia", "Deep Facelift":"levantamiento facial profundo",
        "HD Liposuction":"liposucción de alta definición"}
for en, es in PROC.items():
    for i in range(1, 20):
        T["%s, case %d: before and after" % (en, i)] = "%s, caso %d: antes y después" % (es[0].upper()+es[1:], i)

# ---- verbatim: patient reviews stay in the language they were written in ----
KEEP_VERBATIM = True

# ---- review metadata: month names and the procedure label under each quote ----
MONTHS = {"January":"enero","February":"febrero","March":"marzo","April":"abril",
          "May":"mayo","June":"junio","July":"julio","August":"agosto",
          "September":"septiembre","October":"octubre","November":"noviembre","December":"diciembre"}
for en, es in MONTHS.items():
    for y in range(2018, 2027):
        T["%s %d" % (en, y)] = "%s de %d" % (es, y)

T.update({
"Breast lift + Lipo 360": "Levantamiento de senos + Lipo 360",
"Breast augmentation": "Aumento de senos",
"Consultation and surgery": "Consulta y cirugía",
"Consultation and follow-up": "Consulta y seguimiento",
"Rhinoplasty + otoplasty": "Rinoplastia + otoplastia",
"Breast lift": "Levantamiento de senos",
"Arm lift": "Braquioplastia",
"Septorhinoplasty": "Septorrinoplastia",
"Revision septorhinoplasty": "Septorrinoplastia de revisión",
"Breast reconstruction": "Reconstrucción mamaria",
"Liposuction": "Liposucción",
"BBL + Lipo 360": "BBL + Lipo 360",
"Tummy Tuck + BBL": "Abdominoplastia + BBL",
"BBL + Breast Lift": "BBL + levantamiento de senos",
"29 sec": "29 s",
"Julio Clavijo Alvarez MD": "Julio Clavijo Alvarez MD",
})

# ---- short case labels (aria/slide labels), generated from the same map ----
for en, es in PROC.items():
    for i in range(1, 20):
        T["%s, case %d" % (en, i)] = "%s, caso %d" % (es[0].upper()+es[1:], i)

