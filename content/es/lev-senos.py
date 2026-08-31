# -*- coding: utf-8 -*-
"""/procedimientos/levantamiento-de-senos — Spanish copy.

Two statements carry the page and both are refusals to flatter.

  "Un levantamiento cambia una cicatriz por una forma."
  An augmentation hides its incision in a fold. A lift cannot. The page says the
  bargain out loud instead of burying it under the risks list.

  "Un levantamiento la deja más levantada, no más grande."
  The commonest disappointment after this operation, and entirely avoidable by
  saying it first. Keep "no más grande" blunt; the whole section exists for it.

WHAT THIS PAGE REFUSES TO CLAIM — do not "fix" it in review. It has its own
Evidence section saying two things plainly: his before-and-afters for this are
filed under breast augmentation and are not shown here as though they were lifts,
and no week-by-week recovery timeline exists for a lift alone, so none is
invented. That section is the most valuable thing on the page and the easiest for
somebody to delete as an oddity.

Terms: "mastopexia" appears once as the clinical name; everywhere else it is
"levantamiento de senos", which is what patients say. "Pedículo" is the right
word for the tissue column and is what he uses.
"""

# Split across a <br>.
# One title node here, not two: the source is "Breast&nbsp;Lift" followed by
# the clinical name in a <span>. A two-item list ate the subtitle.
H1 = ["Levantamiento de&nbsp;senos"]

T = {
"Breast Lift (Mastopexy) in Miami — Julio Clavijo Alvarez, MD":
  "Levantamiento de senos (mastopexia) en Miami — Julio Clavijo Alvarez, MD",
"Breast lift with Dr. Julio Clavijo Alvarez, board-certified plastic surgeon in Miami. Raising what is already there, the scar it costs, and why it will not make you bigger.":
  "Levantamiento de senos con el Dr. Julio Clavijo Alvarez, cirujano plástico certificado en Miami. Elevar lo que ya está, la cicatriz que cuesta, y por qué no la va a dejar más grande.",
"Mastopexy": "Mastopexia",
"Raising what is already there. Nothing is added, so nothing gets bigger &mdash; and that surprises people who did not ask.":
  "Elevar lo que ya está. No se añade nada, así que nada se hace más grande &mdash; y eso sorprende a quien no lo preguntó.",
"How it is done &darr;": "Cómo se hace &darr;",
"1h30 &ndash; 3h": "1h30 &ndash; 3h",
"Depends on the pattern": "Según el patrón",
"His own published guidance": "Sus propias indicaciones publicadas",
"Permanent": "Permanente",
"Around and below the areola": "Alrededor y por debajo de la areola",

# ---- the evidence section: what the page will not claim ----
"Evidence": "Evidencia",
"Two things this page does not claim.": "Dos cosas que esta página no afirma.",
"His before-and-after records for this are filed under breast augmentation. A lift is a different operation and none of them are shown here as though they were.":
  "Sus registros de antes y después para esto están archivados bajo aumento de senos. Un levantamiento es otra operación, y aquí no se muestra ninguno como si lo fuera.",
"On recovery he publishes one figure &mdash; one to two weeks before normal activity &mdash; which is in the fact rail above. A full week-by-week timeline for a lift alone is not sourced, so none is invented here. The augmentation timeline is the nearest documented one.":
  "Sobre la recuperación él publica una sola cifra &mdash; de una a dos semanas antes de la actividad normal &mdash; y está en la ficha de arriba. No hay una fuente para un calendario semana a semana solo del levantamiento, así que aquí no se inventa ninguno. El calendario del aumento es el más cercano que sí está documentado.",
"See the augmentation timeline": "Ver el calendario del aumento",

# ---- the operation ----
"A mastopexy under general anaesthesia. Nothing is added &mdash; the whole result comes from moving what is already there.":
  "Una mastopexia bajo anestesia general. No se añade nada &mdash; todo el resultado viene de mover lo que ya está.",
"Types, scars, real results": "Tipos, cicatrices y resultados reales",
"Lift, or implant?": "¿Levantamiento, o implante?",
"How he decides &middot; English": "Cómo lo decide &middot; English",

"The new position is marked, standing": "La nueva posición se marca de pie",
"Sitting or standing upright, because that is where gravity will hold it. This one measurement decides most of the result &mdash; a nipple set a centimetre too high cannot be moved back down afterwards.":
  "Sentada o de pie, erguida, porque ahí es donde la gravedad la va a sostener. Esa sola medida decide la mayor parte del resultado &mdash; un pezón colocado un centímetro demasiado alto no se puede bajar después.",
"The nipple is raised on its own blood supply": "El pezón se eleva con su propia irrigación",
"It is not detached and re-sited. It stays attached to a column of tissue that carries its blood and nerve supply, and that column is moved up with it &mdash; which is why smoking matters here more than on any other breast operation.":
  "No se desprende para recolocarlo. Queda unido a un pedículo de tejido que lleva su irrigación y su inervación, y ese pedículo sube con él &mdash; por eso fumar importa aquí más que en cualquier otra operación de senos.",
"Excess skin is removed": "Se retira el exceso de piel",
"The envelope is tightened around the tissue inside it. How much has to come out decides the scar pattern: around the areola alone, or with a vertical line running down from it, or with a horizontal one along the fold as well.":
  "La envoltura se ajusta alrededor del tejido que contiene. Cuánta piel haya que sacar decide el patrón de la cicatriz: solo alrededor de la areola, o con una línea vertical que baja desde ella, o además con una horizontal a lo largo del surco.",
"The breast tissue is reshaped, then checked sitting up":
  "Se remodela el tejido y se comprueba sentada",
"The tissue is gathered and narrowed rather than simply pulled tight, so the shape holds. He sits you up on the table to judge it, because a breast that looks right lying down does not necessarily look right standing.":
  "El tejido se recoge y se estrecha en vez de solo tensarse, para que la forma aguante. La sienta en la mesa para valorarlo, porque un seno que se ve bien acostada no necesariamente se ve bien de pie.",
"Closed in layers, supported": "Cerrado por capas, con sujeción",
"Self-dissolving sutures and tape, then a surgical bra to hold the tissue on its new position while it heals into place. The support is doing real work, not comforting you.":
  "Suturas reabsorbibles y cinta, después un sostén quirúrgico que mantiene el tejido en su nueva posición mientras cicatriza ahí. La sujeción está haciendo un trabajo real, no consolándola.",

# ---- the three statements ----
"A lift trades a": "Un levantamiento cambia una",
"scar": "cicatriz",
"for a shape.": "por una forma.",
"That is the whole bargain, and it is the part people are not told plainly. An augmentation hides its incision in a fold. A lift cannot &mdash; skin has to come out, and the scar runs around the areola and usually down from it. It fades substantially, it does not disappear, and if that trade is not worth it to you then an implant alone is the honest answer even if the result is lower.":
  "Ese es todo el trato, y es la parte que no se dice con claridad. Un aumento esconde su incisión en un surco. Un levantamiento no puede &mdash; hay que sacar piel, y la cicatriz rodea la areola y normalmente baja desde ella. Se aclara bastante, no desaparece, y si ese trato no le compensa, entonces un implante solo es la respuesta honesta aunque el resultado quede más bajo.",
"Where your": "Dónde está su",
"nipple": "pezón",
"sits decides which operation you need.": "decide qué operación necesita.",
"Not what you ask for, and not what a photograph shows. Above the crease beneath the breast, an implant alone can work. Below it, no implant will raise it &mdash; a bigger one just makes a heavier breast in the same place. He will measure it and show you, which takes about a minute.":
  "No lo que usted pida, ni lo que muestre una fotografía. Por encima del surco debajo del seno, un implante solo puede servir. Por debajo, ningún implante lo va a subir &mdash; uno más grande solo hace un seno más pesado en el mismo sitio. Se lo mide y se lo enseña, y eso lleva como un minuto.",
"A lift makes you": "Un levantamiento la deja más",
"perkier": "levantada",
", not bigger.": ", no más grande.",
"It is the single most common disappointment after this operation, and it is entirely avoidable by being told first. Nothing is added, so the volume you have is the volume you keep &mdash; and once it has been gathered into a higher, tighter shape, some people read that as smaller. If fullness at the top is what you are actually after, the operation you want has an implant in it.":
  "Es, con diferencia, la decepción más común después de esta operación, y se evita por completo con que se lo digan antes. No se añade nada, así que el volumen que tiene es el volumen que conserva &mdash; y una vez recogido en una forma más alta y más firme, hay quien lo lee como más pequeño. Si lo que busca de verdad es volumen en la parte alta, la operación que quiere lleva un implante.",

# ---- candidacy ----
"A nipple that sits below the fold": "Un pezón que queda por debajo del surco",
"The objective test. If the nipple has dropped below the crease beneath the breast, an implant alone will not raise it and a lift is the only operation that raises it.":
  "La prueba objetiva. Si el pezón ha caído por debajo del surco que hay debajo del seno, un implante solo no lo va a subir y el levantamiento es la única operación que lo eleva.",
"If it still sits above the fold. An augmentation may do what you want with a scar hidden in the crease, and no scar on the front of the breast at all.":
  "Si todavía queda por encima del surco. Un aumento puede darle lo que quiere con una cicatriz escondida en el pliegue, y sin ninguna cicatriz en la parte delantera del seno.",
"Enough tissue left to reshape": "Tejido suficiente para remodelar",
"Position has changed more than volume has. There is breast to work with, and repositioning it gives a fuller, higher shape without adding anything.":
  "Ha cambiado más la posición que el volumen. Hay seno con el que trabajar, y recolocarlo da una forma más llena y más alta sin añadir nada.",
"If the breast is empty as well as low, which is common after breastfeeding. Lifting an empty breast gives a higher empty breast, and he will say that in the room rather than let you find it out afterwards.":
  "Si el seno está vacío además de bajo, algo común después de la lactancia. Levantar un seno vacío da un seno vacío más alto, y se lo va a decir en la consulta en vez de dejar que lo descubra después.",
"The scar is a trade you accept": "La cicatriz es un trato que usted acepta",
"Around the areola, usually with a line running down from it. It fades substantially over a year and it never disappears.":
  "Alrededor de la areola, normalmente con una línea que baja desde ella. Se aclara bastante en un año y nunca desaparece.",
"If the scar is unacceptable to you. That is a legitimate answer, not a failure of nerve, and it is better said now than regretted later.":
  "Si la cicatriz le resulta inaceptable. Esa es una respuesta legítima, no una falta de valor, y es mejor decirlo ahora que lamentarlo después.",
"Or certain that you are. Pregnancy and breastfeeding stretch the envelope and drop the position again, which is exactly what this operation just corrected.":
  "O segura de que ya terminó. El embarazo y la lactancia estiran la envoltura y vuelven a bajar la posición, que es justo lo que esta operación acaba de corregir.",
"If a pregnancy is close. Everything this operation corrects can be undone by one.":
  "Si hay un embarazo cerca. Todo lo que corrige esta operación lo puede deshacer uno.",
"Not smoking, not vaping. This operation moves the nipple on its own blood supply. Nicotine narrows exactly those vessels.":
  "Sin fumar, sin vapear. Esta operación mueve el pezón con su propia irrigación. La nicotina estrecha justo esos vasos.",
"If you are still smoking. Of all the breast operations, this is the one where nicotine does the most visible damage &mdash; and the damage lands at the nipple.":
  "Si todavía fuma. De todas las operaciones de senos, esta es en la que la nicotina hace el daño más visible &mdash; y el daño cae en el pezón.",
"A doctorate in surgery, years of laboratory work in cell biology, and hyperbaric oxygen therapy in his own practice. It is why he is unusually specific about healing &mdash; and why he will turn you down if you are not prepared to do your half of it.":
  "Un doctorado en cirugía, años de trabajo de laboratorio en biología celular, y oxigenoterapia hiperbárica en su propia consulta. Por eso es inusualmente específico con la cicatrización &mdash; y por eso la va a rechazar si no está dispuesta a poner su mitad.",

# ---- risks ----
"A shorter list than most breast operations, because nothing is being implanted. The ones that remain are worth reading properly.":
  "Una lista más corta que la de la mayoría de operaciones de senos, porque no se implanta nada. Las que quedan vale la pena leerlas bien.",
"Around the areola, usually with a vertical line beneath it and sometimes a horizontal one along the fold. It fades substantially over a year. It does not go away, and no technique makes it go away.":
  "Alrededor de la areola, normalmente con una línea vertical debajo y a veces una horizontal a lo largo del surco. Se aclara bastante en un año. No desaparece, y ninguna técnica hace que desaparezca.",
"Loss of nipple sensation": "Pérdida de sensibilidad en el pezón",
"The nipple is moved on its own nerve supply, so some change is common. Usually partial and usually temporary; occasionally permanent, in either direction &mdash; numb or oversensitive.":
  "El pezón se mueve con su propia inervación, así que algún cambio es común. Normalmente parcial y normalmente temporal; en ocasiones permanente, en cualquiera de los dos sentidos &mdash; adormecido o demasiado sensible.",
"Nipple healing problems": "Problemas de cicatrización del pezón",
"Rare and serious. The nipple survives on the column of tissue it travels with, and anything that narrows those vessels &mdash; nicotine above all &mdash; puts it at risk.":
  "Poco frecuentes y graves. El pezón sobrevive gracias al pedículo con el que viaja, y cualquier cosa que estreche esos vasos &mdash; la nicotina sobre todo &mdash; lo pone en riesgo.",
"Delayed healing where the scars meet": "Cicatrización lenta donde se juntan las cicatrices",
"The junction of the vertical and horizontal scars is under the most tension and is the commonest place to see slow healing. It is managed with dressings and time, and it can widen the scar.":
  "La unión de la cicatriz vertical con la horizontal es la que más tensión soporta y el sitio donde más se ve una cicatrización lenta. Se maneja con curaciones y tiempo, y puede ensanchar la cicatriz.",
"Breasts are not symmetrical before surgery and will not be afterwards. He aims to reduce the difference, not to erase it, and small differences in nipple height are the usual residue.":
  "Los senos no son simétricos antes de la cirugía y no lo serán después. Su objetivo es reducir la diferencia, no borrarla, y pequeñas diferencias en la altura del pezón son lo que suele quedar.",
"Recurrent drooping": "Caída que vuelve",
"The operation resets position. It does not stop gravity, weight change, or time, and heavier breasts descend sooner.":
  "La operación reinicia la posición. No detiene la gravedad, ni los cambios de peso, ni el tiempo, y los senos más pesados bajan antes.",
"The tissue around the nipple is moved, so it may be affected. It often still works. It cannot be guaranteed either way, and anyone who guarantees it is guessing.":
  "El tejido alrededor del pezón se mueve, así que puede verse afectada. Muchas veces sigue funcionando. No se puede garantizar en ningún sentido, y quien lo garantice está adivinando.",

# ---- cost ----
"Every quote is built from the same things. A lift is priced on how much work the pattern takes, not on a cup size &mdash; so two people quoted differently are usually being quoted for different operations.":
  "Todo presupuesto se arma con las mismas cosas. Un levantamiento se cotiza por el trabajo que exige el patrón, no por una talla de copa &mdash; así que dos personas con presupuestos distintos normalmente están recibiendo presupuestos de operaciones distintas.",
"Which lift pattern is needed &mdash; scar length tracks the work involved":
  "Qué patrón de levantamiento hace falta &mdash; la longitud de la cicatriz sigue al trabajo que implica",
"Whether tissue is being removed as well as repositioned":
  "Si además de recolocar tejido se va a retirar",
"Facility fee, garments and follow-up": "Costo del quirófano, prendas y seguimiento",
"Whether revisions are included, and for how long":
  "Si las revisiones están incluidas, y por cuánto tiempo",

# ---- FAQ ----
"Will a lift make me bigger?": "¿Un levantamiento me va a dejar más grande?",
"No, and this is the thing worth being certain about before you book. Nothing is added. The breast is raised, narrowed and tightened, which reads as fuller in a bra and can read as slightly smaller out of one. If upper-pole fullness is the goal, you want an implant in the plan.":
  "No, y esto es lo que conviene tener claro antes de reservar. No se añade nada. El seno se eleva, se estrecha y se tensa, lo que se lee como más lleno dentro de un sostén y puede leerse como algo más pequeño fuera de él. Si el objetivo es volumen en la parte alta, lo que quiere lleva un implante en el plan.",
"How long is the scar?": "¿De qué largo es la cicatriz?",
"It depends on how much skin has to come out. Around the areola alone for a small correction; with a vertical line below it for most; with a horizontal line along the fold as well where there is a lot. More skin removed means more scar and a better shape &mdash; that is the whole trade.":
  "Depende de cuánta piel haya que sacar. Solo alrededor de la areola en una corrección pequeña; con una línea vertical debajo en la mayoría; y además con una horizontal a lo largo del surco cuando hay mucha. Más piel retirada significa más cicatriz y mejor forma &mdash; ese es todo el trato.",
"Could I add an implant later instead?": "¿Podría añadir un implante más adelante?",
"Yes, and for some people staging it that way is the better plan. The lift settles first and the implant is then chosen against a shape that already exists. It is two recoveries and two costs, so it is a genuine conversation rather than a default.":
  "Sí, y para algunas personas hacerlo por etapas es el mejor plan. Primero se asienta el levantamiento y después se elige el implante contra una forma que ya existe. Son dos recuperaciones y dos costos, así que es una conversación de verdad y no una opción por defecto.",
"Will it droop again?": "¿Volverá a caer?",
"Eventually, to some extent. The operation resets position; it does not stop time or gravity. Stable weight, good support and not smoking all slow it down.":
  "Con el tiempo, en alguna medida. La operación reinicia la posición; no detiene el tiempo ni la gravedad. Un peso estable, buena sujeción y no fumar lo frenan.",
"Can I still breastfeed afterwards?": "¿Puedo seguir amamantando después?",
"Often, yes &mdash; the ducts and the nipple stay connected to the tissue beneath. But the tissue around the nipple is moved, so it may be affected, and nobody can promise you either outcome. Say at the consultation if it matters; it changes how he plans the pedicle.":
  "Muchas veces sí &mdash; los conductos y el pezón siguen conectados al tejido de debajo. Pero el tejido alrededor del pezón se mueve, así que puede verse afectada, y nadie le puede prometer ningún resultado. Dígalo en la consulta si le importa; cambia cómo planifica el pedículo.",
"Why is my nipple position marked while I am standing?":
  "¿Por qué me marcan la posición del pezón estando de pie?",
"Because that is where gravity holds it. Marked lying down, a nipple ends up too high once you stand &mdash; and a nipple set too high is the one error in this operation that cannot be corrected afterwards.":
  "Porque ahí es donde la gravedad lo sostiene. Marcado acostada, el pezón acaba demasiado alto en cuanto se pone de pie &mdash; y un pezón colocado demasiado alto es el único error de esta operación que no se puede corregir después.",

# ---- booking ----
"Breast lift, pre-filled from this page.":
  "Levantamiento de senos, ya rellenado desde esta página.",

# ---- JSON-LD ----
"Performed under general anaesthesia. The new nipple position is marked with the patient upright. The nipple-areola complex is raised on a pedicle carrying its own blood and nerve supply. Excess skin is excised, the pattern depending on how much must be removed, and the breast tissue is reshaped and assessed with the patient sitting up. Closure is in layers, followed by a supportive garment.":
  "Se realiza bajo anestesia general. La nueva posición del pezón se marca con la paciente erguida. El complejo areola-pezón se eleva sobre un pedículo que lleva su propia irrigación e inervación. Se reseca el exceso de piel, con un patrón que depende de cuánta haya que retirar, y el tejido mamario se remodela y se valora con la paciente sentada. El cierre es por capas, seguido de una prenda de sujeción.",
"Nipple position below the inframammary fold, sufficient breast tissue to reshape, acceptance of a permanent scar, completed childbearing, and nicotine-free.":
  "Posición del pezón por debajo del surco submamario, tejido mamario suficiente para remodelar, aceptación de una cicatriz permanente, maternidad terminada, y sin nicotina.",
"Supportive bra full-time for approximately one month. One to two weeks before returning to normal activity.":
  "Sostén de sujeción a tiempo completo durante aproximadamente un mes. De una a dos semanas antes de volver a la actividad normal.",
"It depends on how much skin has to come out. Around the areola alone for a small correction; with a vertical line below it for most; with a horizontal line along the fold as well where there is a lot. More skin removed means more scar and a better shape — that is the whole trade.":
  "Depende de cuánta piel haya que sacar. Solo alrededor de la areola en una corrección pequeña; con una línea vertical debajo en la mayoría; y además con una horizontal a lo largo del surco cuando hay mucha. Más piel retirada significa más cicatriz y mejor forma — ese es todo el trato.",
"Often, yes — the ducts and the nipple stay connected to the tissue beneath. But the tissue around the nipple is moved, so it may be affected, and nobody can promise you either outcome. Say at the consultation if it matters; it changes how he plans the pedicle.":
  "Muchas veces sí — los conductos y el pezón siguen conectados al tejido de debajo. Pero el tejido alrededor del pezón se mueve, así que puede verse afectada, y nadie le puede prometer ningún resultado. Dígalo en la consulta si le importa; cambia cómo planifica el pedículo.",
"Because that is where gravity holds it. Marked lying down, a nipple ends up too high once you stand — and a nipple set too high is the one error in this operation that cannot be corrected afterwards.":
  "Porque ahí es donde la gravedad lo sostiene. Marcado acostada, el pezón acaba demasiado alto en cuanto se pone de pie — y un pezón colocado demasiado alto es el único error de esta operación que no se puede corregir después.",
}
