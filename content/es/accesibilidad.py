# -*- coding: utf-8 -*-
"""/accesibilidad — Spanish copy.

The page's credibility comes entirely from "Lo que todavía no está bien". Any
accessibility statement can claim conformance; this one names four things that
fail, and that is the part worth protecting in review. Do not soften them, do
not move them above the tested list, and do not let anyone add a claim to the
tested list that is not actually measured.

Two of the four gaps are the same media problems flagged elsewhere: the
before-and-after images carry burned-in English text, and the talks have only
automatic captions. Both are recorded here as accessibility failures rather than
as nice-to-haves, which is what they are.

"WCAG 2.2 Level AA" stays in English — it is the name of a standard, and the
Spanish reader looking it up needs the string that finds it.

Dates: "27 de agosto de 2026". If the page is edited, this date moves with it.
"""

T = {
# ---- head ----
"Accessibility — J.C. Alvarez Plastic Surgery":
  "Accesibilidad — J.C. Alvarez Plastic Surgery",
"How this site is built to be usable, what has been tested, and what is still not good enough.":
  "Cómo está construido este sitio para que se pueda usar, qué se ha probado, y qué todavía no está bien.",

# ---- hero ----
"A lot of people read a site like this one-handed, at night, on a phone, worried. Some read it at 200% zoom, or with a screen reader, or without using a mouse at all. It should work for all of them.":
  "Mucha gente lee un sitio como este con una sola mano, de noche, en el teléfono, preocupada. Algunas lo leen con el zoom al 200%, o con un lector de pantalla, o sin usar el ratón en absoluto. Debería funcionar para todas.",
"Last updated 27 August 2026": "Última actualización: 27 de agosto de 2026",

# ---- the standard ----
"The standard": "El estándar",
"This site targets": "Este sitio apunta a",
"WCAG 2.2 Level AA": "WCAG 2.2 nivel AA",
". That is a measurable bar, not a statement of intent, and the checks below are run against every page rather than a sample.":
  ". Es un listón medible, no una declaración de intenciones, y las comprobaciones de abajo se ejecutan sobre todas las páginas, no sobre una muestra.",

# ---- what has been tested ----
"What has been tested": "Qué se ha probado",
"Automated checks on every page": "Comprobaciones automáticas en todas las páginas",
", at 1440px and 390px, using axe-core against the WCAG 2.0, 2.1 and 2.2 A and AA rule sets. Every page currently reports zero violations.":
  ", a 1440px y a 390px, con axe-core sobre los conjuntos de reglas A y AA de WCAG 2.0, 2.1 y 2.2. Ahora mismo todas las páginas dan cero incidencias.",
"Keyboard only.": "Solo teclado.",
"Every control can be reached and operated without a mouse, including the results filters, the case viewer and the carousels. Focus is always visible.":
  "Se puede llegar a todos los controles y usarlos sin ratón, incluidos los filtros de resultados, el visor de casos y los carruseles. El foco siempre se ve.",
"Text over video.": "Texto sobre video.",
"The homepage headline sits over moving footage, which automated tools cannot evaluate at all. The contrast was measured by sampling the actual composited pixels behind the text across the whole loop and taking the brightest frame as the worst case. It passes at that frame, not just on average.":
  "El titular del inicio va sobre imágenes en movimiento, algo que las herramientas automáticas no pueden evaluar. El contraste se midió muestreando los píxeles reales que quedan detrás del texto a lo largo de todo el bucle y tomando el fotograma más claro como el peor caso. Pasa en ese fotograma, no solo de media.",
"Reduced motion.": "Movimiento reducido.",
"If your system asks for less movement, the hero video does not load, carousels do not animate, and transitions are removed.":
  "Si su sistema pide menos movimiento, el video de portada no se carga, los carruseles no se animan, y las transiciones se eliminan.",
"320px and 200% zoom.": "320px y zoom al 200%.",
"No horizontal scrolling, no clipped text.": "Sin desplazamiento horizontal, sin texto cortado.",
"Structure.": "Estructura.",
"One": "Un",
"per page, no skipped heading levels, real landmarks, and a skip link.":
  "por página, sin saltarse niveles de encabezado, con regiones semánticas reales y un enlace para saltar al contenido.",

# ---- what is not good enough ----
"What is not good enough yet": "Lo que todavía no está bien",
"Every site claiming to be accessible has gaps. These are ours.":
  "Todo sitio que se dice accesible tiene carencias. Estas son las nuestras.",
"The before-and-after images carry text inside the picture.":
  "Las imágenes de antes y después llevan texto dentro de la propia foto.",
"The procedure name and the &ldquo;Before&rdquo; and &ldquo;After&rdquo; labels are part of the photograph rather than real text, so they cannot be resized or restyled. Each image has alt text carrying the same information, but that is a workaround.":
  "El nombre del procedimiento y las etiquetas «Before» y «After» son parte de la fotografía y no texto real, así que no se pueden redimensionar ni cambiar de estilo. Cada imagen lleva un texto alternativo con la misma información, pero eso es un apaño.",
"The video talks are in Spanish with automatic captions only.":
  "Las charlas en video están en español y solo tienen subtítulos automáticos.",
"They have not been captioned by a person in either language, and automatic captions of medical vocabulary are unreliable.":
  "Nadie las ha subtitulado a mano en ninguno de los dos idiomas, y los subtítulos automáticos de vocabulario médico no son fiables.",
"The hero video has no captions or audio description.":
  "El video de portada no tiene subtítulos ni audiodescripción.",
"It carries no speech and no information that is not repeated in the text beside it, but it has not been described.":
  "No lleva voz ni información que no esté repetida en el texto que tiene al lado, pero no se ha descrito.",
"Nothing here has been tested with real assistive technology by someone who depends on it.":
  "Nada de esto lo ha probado con tecnología de asistencia real alguien que dependa de ella.",
"Automated checks and keyboard testing catch a great deal and are not the same thing.":
  "Las comprobaciones automáticas y las pruebas con teclado detectan muchísimo, y no son lo mismo.",

# ---- if something does not work ----
"If something does not work": "Si algo no funciona",
"Tell us and it will be fixed. Please say what page you were on and what you were using &mdash; that is usually enough to reproduce it.":
  "Díganoslo y se arregla. Por favor indique en qué página estaba y qué estaba usando &mdash; con eso suele bastar para reproducirlo.",
"If you need any information on this site in another format, ask and it will be sent to you.":
  "Si necesita cualquier información de este sitio en otro formato, pídala y se la enviamos.",
}
