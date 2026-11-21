import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from z import *

# Durchgehendes Beispiel in diesem Oberthema: das englische Wort „nice“ und ein Satz im Klassenzimmer
R = lambda x, y, w, h, art: f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" style="{art}" stroke-width="1.3"/>'

# ---------------------------------------------------------------- 0 What is a dichotomy?
fig_dicho = svg(360, 210,
    T(180, 18, 'One object – two ways of looking at it', 'Ein Gegenstand – zwei Blickwinkel', 13, 800)
    + box(120, 80, 120, 52, 'LANGUAGE', 'SPRACHE', tip=('The object is always the same: language. A dichotomy only changes the perspective.', 'Der Gegenstand ist immer derselbe: Sprache. Eine Dichotomie ändert nur den Blickwinkel.'), art='hl', size=14)
    + box(4, 36, 104, 44, 'synchronic', 'synchron', tip=('Look at language at ONE point in time.', 'Sprache zu EINEM Zeitpunkt ansehen.'))
    + box(252, 36, 104, 44, 'diachronic', 'diachron', tip=('Look at how language CHANGES over time.', 'Ansehen, wie Sprache sich über die Zeit VERÄNDERT.'))
    + box(4, 92, 104, 44, 'form', 'Form', tip=('What a linguistic unit looks / sounds like: its structure.', 'Wie eine sprachliche Einheit aussieht / klingt: ihre Struktur.'))
    + box(252, 92, 104, 44, 'function', 'Funktion', tip=('What the unit is used for in communication.', 'Wofür die Einheit in der Kommunikation verwendet wird.'))
    + box(4, 148, 104, 44, 'theoretical', 'theoretisch', tip=('Study language for its own sake: describe and explain the system.', 'Sprache um ihrer selbst willen untersuchen: das System beschreiben und erklären.'))
    + box(252, 148, 104, 44, 'applied', 'angewandt', tip=('Use linguistic findings to solve real-life problems (teaching, translation …).', 'Erkenntnisse nutzen, um praktische Probleme zu lösen (Unterricht, Übersetzen …).'))
    + pfeil(108, 58, 128, 86) + pfeil(252, 58, 232, 86) + pfeil(108, 114, 120, 110) + pfeil(252, 114, 240, 110)
    + pfeil(108, 170, 128, 128) + pfeil(252, 170, 232, 128),
    'Dichotomies as pairs of perspectives on language', maxw=420)

t_dicho = thema('dichotomies', ('What is a dichotomy?', 'Was ist eine Dichotomie?'),
    kern=('A dichotomy is a pair of opposite but complementary perspectives on language. The two sides do not compete – they are two ways of looking at the same object. The worksheet tests three of them: synchronic/diachronic, form/function and applied/theoretical.',
          'Eine Dichotomie ist ein Paar gegensätzlicher, aber sich ergänzender Blickwinkel auf Sprache. Die beiden Seiten konkurrieren nicht – sie sind zwei Arten, denselben Gegenstand anzusehen. Das Arbeitsblatt fragt drei davon ab: synchron/diachron, Form/Funktion und angewandt/theoretisch.'),
    kurz=('<p>Imagine a photo and a video of the same football match. The photo shows the exact positions of all players at one second. The video shows how the game develops. Neither is “better” – you need both to understand the match.</p><p>Linguistics works the same way. It uses <b>dichotomies</b>: pairs of terms that split language into two perspectives. Simply put: one object, two lenses.</p><p>In the exam, dichotomies usually come as <b>true-or-false statements</b>. If a statement is false, you must write the <b>correct answer</b>. So you need to know both sides of every pair exactly.</p>',
          '<p>Stell dir ein Foto und ein Video desselben Fußballspiels vor. Das Foto zeigt die genaue Position aller Spieler in einer Sekunde. Das Video zeigt, wie sich das Spiel entwickelt. Keins ist „besser“ – man braucht beide, um das Spiel zu verstehen.</p><p>Die Sprachwissenschaft arbeitet genauso. Sie nutzt <b>Dichotomien</b>: Begriffspaare, die Sprache in zwei Blickwinkel teilen. Einfach gesagt: ein Gegenstand, zwei Brillen.</p><p>In der Klausur kommen Dichotomien meist als <b>Richtig-oder-falsch-Aussagen</b>. Ist eine Aussage falsch, musst du die <b>richtige Antwort</b> hinschreiben. Du musst also beide Seiten jedes Paars genau kennen.</p>'),
    fig=fw('Three pairs of perspectives on the same object. Tap the boxes.', 'Drei Paare von Blickwinkeln auf denselben Gegenstand. Tippe auf die Kästen.') + bild(fig_dicho),
    figcap=('after the worksheet, task 1', 'nach dem Arbeitsblatt, Aufgabe 1'),
    article=h3('Dichotomy – the word', 'Dichotomie – das Wort')
        + p('The word comes from Greek <i>dicha</i> (“in two”) and <i>temnein</i> (“to cut”). A <b>dichotomy</b> cuts a topic into two parts. ' + eg('a pair of opposite terms that belong together.', 'ein Paar gegensätzlicher Begriffe, die zusammengehören.'),
            'Das Wort kommt aus dem Griechischen: <i>dicha</i> („zweigeteilt“) und <i>temnein</i> („schneiden“). Eine <b>Dichotomie</b> schneidet ein Thema in zwei Teile. ' + eg('a pair of opposite terms that belong together.', 'ein Paar gegensätzlicher Begriffe, die zusammengehören.'))
        + p('Important: the two sides are <b>not</b> right and wrong, good and bad, or old and new. They are two different questions you can ask about language.',
            'Wichtig: Die beiden Seiten sind <b>nicht</b> richtig und falsch, gut und schlecht oder alt und neu. Es sind zwei verschiedene Fragen, die man an Sprache stellen kann.')
        + weiter('Here are the three pairs from the worksheet at one glance. Each gets its own page afterwards.', 'Hier die drei Paare des Arbeitsblatts auf einen Blick. Jedes bekommt danach eine eigene Seite.')
        + h3('The three dichotomies of the worksheet', 'Die drei Dichotomien des Arbeitsblatts')
        + tabelle([('Pair', 'Paar'), ('Side 1', 'Seite 1'), ('Side 2', 'Seite 2')], [
            [('synchronic / diachronic', 'synchron / diachron'), ('language at <b>one point in time</b> (a snapshot)', 'Sprache zu <b>einem Zeitpunkt</b> (Momentaufnahme)'), ('language <b>change through time</b> (a film)', 'Sprach<b>wandel über die Zeit</b> (ein Film)')],
            [('form / function', 'Form / Funktion'), ('the <b>structure</b>: sounds, words, sentences – <i>how</i> something is said', 'die <b>Struktur</b>: Laute, Wörter, Sätze – <i>wie</i> etwas gesagt wird'), ('the <b>purpose</b> in communication – <i>what for</i> it is said', 'der <b>Zweck</b> in der Kommunikation – <i>wozu</i> es gesagt wird')],
            [('theoretical / applied', 'theoretisch / angewandt'), ('language studied <b>for its own sake</b> (“not applied”)', 'Sprache <b>um ihrer selbst willen</b> erforscht („nicht angewandt“)'), ('findings used to solve <b>real-life problems</b>', 'Erkenntnisse zur Lösung <b>praktischer Probleme</b>')]])
        + zusatz('Other famous dichotomies: <b>langue / parole</b> (Saussure, see “Structuralism”), <b>competence / performance</b> (Chomsky, see “Formalism”), <b>descriptive / prescriptive</b> (describe how people really speak vs. tell them how they should speak).',
                 'Weitere bekannte Dichotomien: <b>langue / parole</b> (Saussure, siehe „Strukturalismus“), <b>competence / performance</b> (Chomsky, siehe „Formalismus“), <b>deskriptiv / präskriptiv</b> (beschreiben, wie Menschen wirklich sprechen, statt vorzuschreiben, wie sie sprechen sollen).')
        + weiter('Because the exam asks “true or false?”, it helps to have a fixed method for these tasks.', 'Weil die Klausur „richtig oder falsch?“ fragt, hilft eine feste Methode für diese Aufgaben.')
        + h3('How to solve “True or false? → correct answer”', 'So löst du „Richtig oder falsch? → richtige Antwort“')
        + bsp('worksheet task 1.2', 'Arbeitsblatt Aufgabe 1.2', ('“Function denotes a speaker’s ability to only convey basic messages, while form denotes a mastery over the language.”', '„Funktion bezeichnet die Fähigkeit, nur einfache Botschaften zu übermitteln, Form die Beherrschung der Sprache.“'), [
            ('Find the two key terms of the statement.', 'Finde die zwei Schlüsselbegriffe der Aussage.', 'form, function', 'Form, Funktion'),
            ('Recall your definition of each term.', 'Rufe deine Definition jedes Begriffs ab.', 'form = structure · function = purpose', 'Form = Struktur · Funktion = Zweck'),
            ('Compare: does the statement match?', 'Vergleiche: passt die Aussage?', 'no → false', 'nein → falsch'),
            ('Write one full, correct sentence for BOTH terms.', 'Schreibe einen ganzen, richtigen Satz zu BEIDEN Begriffen.', '“Form = …, function = …”', '„Form = …, Funktion = …“')],
            ('A correction only scores if it defines both sides. “Form is not mastery” is not enough.', 'Eine Korrektur gibt nur Punkte, wenn sie beide Seiten definiert. „Form ist keine Beherrschung“ reicht nicht.'))
        + falle('Ticking “false” and leaving the line empty. Without the correct answer you lose most of the points.', '„Falsch“ ankreuzen und die Linie leer lassen. Ohne richtige Antwort verlierst du die meisten Punkte.')
        + klausur_hinweis('Every false statement needs a correction in full sentences, written in English.', 'Jede falsche Aussage braucht eine Korrektur in ganzen Sätzen, auf Englisch.'),
    merk=('A dichotomy = two complementary perspectives on the same object (language). Worksheet pairs: synchronic/diachronic, form/function, theoretical/applied.',
          'Dichotomie = zwei sich ergänzende Blickwinkel auf denselben Gegenstand (Sprache). Paare des Arbeitsblatts: synchron/diachron, Form/Funktion, theoretisch/angewandt.'),
    exam=('True/false statements on dichotomies; if false, write the correct definition of both terms.', 'Richtig/Falsch-Aussagen zu Dichotomien; wenn falsch, die richtige Definition beider Begriffe hinschreiben.'),
    fehler=[('Treating the two sides as “correct” vs. “wrong” or “old” vs. “new”.', 'Die beiden Seiten als „richtig“ vs. „falsch“ oder „alt“ vs. „neu“ deuten.'),
            ('Ticking “false” without writing the correct answer.', '„Falsch“ ankreuzen, ohne die richtige Antwort hinzuschreiben.')],
    src='Worksheet, task 1')

# ---------------------------------------------------------------- 1 synchronic / diachronic
fig_sd = svg(360, 236,
    T(180, 16, 'The word “nice” – snapshots and film', 'Das Wort „nice“ – Momentaufnahmen und Film', 13, 800)
    + f'<line x1="30" y1="200" x2="340" y2="200" style="stroke:var(--axis2)" stroke-width="2"/>'
    + pfeil(30, 200, 345, 200)
    + T(330, 186, 'time', 'Zeit', 12, 700)
    + ''.join(f'<line x1="{x}" y1="194" x2="{x}" y2="206" style="stroke:var(--axis2)" stroke-width="2"/>' + T(x, 222, j, {'today': 'heute'}.get(j, j), 12, 700) for x, j in ((70, '1300'), (180, '1600'), (290, 'today')))
    + box(22, 120, 96, 52, '“foolish,\nsilly”', '„dumm,\nalbern“', tip=('Synchronic snapshot around 1300: in Middle English “nice” meant foolish or silly (from Latin nescius, “not knowing”).', 'Synchrone Momentaufnahme um 1300: Im Mittelenglischen hieß „nice“ dumm oder albern (von lateinisch nescius, „unwissend“).'))
    + box(132, 120, 96, 52, '“precise,\nfussy”', '„genau,\npingelig”', tip=('Synchronic snapshot around 1600: “nice” meant precise or fussy (“a nice distinction”).', 'Synchrone Momentaufnahme um 1600: „nice“ hieß genau oder pingelig („a nice distinction“).'))
    + box(242, 120, 96, 52, '“pleasant,\nkind”', '„angenehm,\nfreundlich“', tip=('Synchronic snapshot today: “nice” means pleasant or kind.', 'Synchrone Momentaufnahme heute: „nice“ heißt angenehm oder freundlich.'))
    + tpg(f'<path d="M70 108 C 120 50, 240 50, 290 108" style="fill:none;stroke:var(--primary)" stroke-width="2.5"/>' + pfeil(282, 98, 290, 110, 'var(--primary)', 2.5)
          + T(180, 52, 'diachronic: the change', 'diachron: der Wandel', 13, 800, fill='var(--primary)'),
          ('Diachronic view: follow the same word through time and describe HOW its meaning changed.', 'Diachrone Sicht: dasselbe Wort durch die Zeit verfolgen und beschreiben, WIE sich die Bedeutung verändert hat.')),
    'Synchronic snapshots and the diachronic change of the word nice', maxw=420)

fig_schach = svg(360, 200,
    R(4, 30, 170, 160, 'fill:var(--pale);stroke:var(--line)') + R(186, 30, 170, 160, 'fill:var(--pale);stroke:var(--line)')
    + T(89, 16, 'synchronic', 'synchron', 13, 800) + T(271, 16, 'diachronic', 'diachron', 13, 800, fill='var(--primary)')
    + ''.join(f'<rect x="{24 + (i % 4) * 32}" y="{48 + (i // 4) * 32}" width="32" height="32" style="fill:{"var(--card)" if (i + i // 4) % 2 else "var(--line)"}"/>' for i in range(16))
    + T(89, 178, 'the board right now', 'das Brett jetzt', 12, 700)
    + T(271, 60, '1. e4  e5', '1. e4  e5', 12, 700) + T(271, 84, '2. Nf3  Nc6', '2. Sf3  Sc6', 12, 700) + T(271, 108, '3. Bb5 …', '3. Lb5 …', 12, 700)
    + pfeil(271, 120, 271, 150, 'var(--primary)') + T(271, 178, 'the moves over time', 'die Züge über die Zeit', 12, 700),
    'Saussure’s chess comparison', maxw=420)

t_sd = thema('synchronic-diachronic', ('Synchronic vs. diachronic', 'Synchron vs. diachron'), star=True,
    kern=('Synchronic linguistics studies a language at one specific point in time, like a snapshot. Diachronic linguistics studies how a language changes through time, like a film. Statement 1.1 of the worksheet is therefore TRUE.',
          'Synchrone Sprachwissenschaft untersucht eine Sprache zu einem bestimmten Zeitpunkt, wie eine Momentaufnahme. Diachrone Sprachwissenschaft untersucht, wie sich eine Sprache über die Zeit verändert, wie ein Film. Aussage 1.1 des Arbeitsblatts ist deshalb RICHTIG.'),
    kurz=('<p>Today, if someone calls you <i>nice</i>, it is a compliment. Around 1300 it was an insult: <i>nice</i> meant “foolish”.</p><p>You can ask two different questions about this word. <b>What does “nice” mean in English today?</b> That is a <b>synchronic</b> question – you look at one moment, like a photo. <b>How did “nice” get from “foolish” to “pleasant”?</b> That is a <b>diachronic</b> question – you follow the word through time, like a film.</p><p>Memory hook: <b>syn</b> = “together” (everything at the same time), <b>dia</b> = “through” (through time). Both contain <b>chronos</b> = time.</p>',
          '<p>Wenn dich heute jemand <i>nice</i> nennt, ist das ein Kompliment. Um 1300 war es eine Beleidigung: <i>nice</i> hieß „dumm“.</p><p>Zu diesem Wort kann man zwei verschiedene Fragen stellen. <b>Was bedeutet „nice“ im heutigen Englisch?</b> Das ist eine <b>synchrone</b> Frage – du siehst dir einen Moment an, wie ein Foto. <b>Wie kam „nice“ von „dumm“ zu „angenehm“?</b> Das ist eine <b>diachrone</b> Frage – du verfolgst das Wort durch die Zeit, wie in einem Film.</p><p>Eselsbrücke: <b>syn</b> = „zusammen“ (alles gleichzeitig), <b>dia</b> = „durch“ (durch die Zeit). Beide enthalten <b>chronos</b> = Zeit.</p>'),
    fig=fw('Each box is a synchronic snapshot; the arrow is the diachronic view. Tap them.', 'Jeder Kasten ist eine synchrone Momentaufnahme; der Pfeil ist die diachrone Sicht. Tippe darauf.') + bild(fig_sd),
    figcap=('example word “nice”; distinction after Saussure', 'Beispielwort „nice“; Unterscheidung nach Saussure'),
    article=h3('Synchronic: one point in time', 'Synchron: ein Zeitpunkt')
        + p('<b>Synchronic</b> linguistics describes a language as a system at <b>one specific point in time</b>. ' + eg('freeze the language and look at how it works at that moment.', 'die Sprache einfrieren und ansehen, wie sie in diesem Moment funktioniert.'),
            '<b>Synchrone</b> Sprachwissenschaft beschreibt eine Sprache als System zu <b>einem bestimmten Zeitpunkt</b>. ' + eg('freeze the language and look at how it works at that moment.', 'die Sprache einfrieren und ansehen, wie sie in diesem Moment funktioniert.'))
        + p('Examples: the sound system of present-day British English; how questions are formed in English today; the grammar of Old English around the year 1000.',
            'Beispiele: das Lautsystem des heutigen britischen Englisch; wie man heute im Englischen Fragen bildet; die Grammatik des Altenglischen um das Jahr 1000.')
        + falle('Thinking “synchronic = present day”. A study of Old English around 1000 is also synchronic – it looks at one moment, just an old one.', 'Denken „synchron = heute“. Eine Untersuchung des Altenglischen um 1000 ist auch synchron – sie betrachtet einen Moment, nur einen alten.')
        + weiter('The opposite question is not “when?” but “how did it change?”.', 'Die Gegenfrage lautet nicht „wann?“, sondern „wie hat es sich verändert?“.')
        + h3('Diachronic: change through time', 'Diachron: Wandel über die Zeit')
        + p('<b>Diachronic</b> (also: historical) linguistics studies <b>language change through time</b>. ' + eg('compare several snapshots and explain the development.', 'mehrere Momentaufnahmen vergleichen und die Entwicklung erklären.'),
            '<b>Diachrone</b> (auch: historische) Sprachwissenschaft untersucht den <b>Sprachwandel über die Zeit</b>. ' + eg('compare several snapshots and explain the development.', 'mehrere Momentaufnahmen vergleichen und die Entwicklung erklären.'))
        + cards([('Meaning', 'Bedeutung', '<i>nice</i>: “foolish” → “pleasant”; <i>girl</i>: once any young person, today a young female', '<i>nice</i>: „dumm“ → „angenehm“; <i>girl</i>: früher jedes Kind, heute ein Mädchen'),
                 ('Grammar', 'Grammatik', '<i>thou art</i> → <i>you are</i>', '<i>thou art</i> → <i>you are</i>'),
                 ('Sounds', 'Laute', 'Great Vowel Shift: <i>time</i> was once pronounced like German “Tiem”', 'Große Vokalverschiebung: <i>time</i> klang früher wie deutsch „Tiem“')])
        + weiter('Saussure, who made this distinction famous, explained it with a game of chess.', 'Saussure, der diese Unterscheidung bekannt gemacht hat, erklärte sie mit einer Schachpartie.')
        + h3('Saussure’s chess comparison', 'Saussures Schach-Vergleich')
        + p('To understand a position on a chessboard, you do not need to know the moves that led to it – the current state is a complete system. That is the synchronic view. The list of moves over the whole game is the diachronic view.',
            'Um eine Stellung auf dem Schachbrett zu verstehen, musst du die Züge davor nicht kennen – der jetzige Zustand ist ein vollständiges System. Das ist die synchrone Sicht. Die Liste der Züge über die ganze Partie ist die diachrone Sicht.')
        + mfig('Chess: the board vs. the moves', 'Schach: das Brett vs. die Züge', fig_schach, 'after Saussure (1916)')
        + gegen(('Synchronic', 'Synchron', 'one point in time · snapshot · “How does it work now / then?”', 'ein Zeitpunkt · Momentaufnahme · „Wie funktioniert es jetzt / damals?“'),
                ('Diachronic', 'Diachron', 'through time · film · “How did it change?”', 'über die Zeit · Film · „Wie hat es sich verändert?“'))
        + klausur_hinweis('Statement 1.1 (“synchronic describes a specific point in time, while diachronic describes language change through time”) is TRUE. Tick a – nothing to correct.', 'Aussage 1.1 („synchronic describes a specific point in time, while diachronic describes language change through time“) ist RICHTIG. a ankreuzen – nichts zu korrigieren.')
        + wahr('w-sd', [
            ('A study of how teenagers in London speak in 2026 is synchronic.', 'Eine Studie, wie Jugendliche in London 2026 sprechen, ist synchron.', True, 'One point in time.', 'Ein Zeitpunkt.'),
            ('A description of Old English grammar around 1000 is diachronic because it is old.', 'Eine Beschreibung der altenglischen Grammatik um 1000 ist diachron, weil sie alt ist.', False, 'Still one point in time → synchronic.', 'Trotzdem ein Zeitpunkt → synchron.'),
            ('Explaining how “nice” changed from “foolish” to “pleasant” is diachronic.', 'Zu erklären, wie „nice“ sich von „dumm“ zu „angenehm“ wandelte, ist diachron.', True, 'Change through time.', 'Wandel über die Zeit.'),
            ('Diachronic means “at the same time”.', 'Diachron heißt „zur gleichen Zeit“.', False, 'dia = through; at the same time = synchronic.', 'dia = durch; zur gleichen Zeit = synchron.')]),
    merk=('Synchronic = language at ONE specific point in time (snapshot). Diachronic = language CHANGE through time (film).', 'Synchron = Sprache zu EINEM bestimmten Zeitpunkt (Momentaufnahme). Diachron = Sprach-WANDEL über die Zeit (Film).'),
    exam=('Worksheet 1.1: TRUE. Be able to define both terms and classify examples.', 'Arbeitsblatt 1.1: RICHTIG. Beide Begriffe definieren und Beispiele zuordnen können.'),
    fehler=[('“Synchronic = today” – old language at one moment is synchronic too.', '„Synchron = heute“ – auch alte Sprache zu einem Zeitpunkt ist synchron.'),
            ('Mixing up the prefixes: syn = together/same time, dia = through.', 'Die Vorsilben verwechseln: syn = zusammen/gleiche Zeit, dia = durch.')],
    src='Worksheet 1.1')

# ---------------------------------------------------------------- 2 form / function
fig_ff = svg(360, 236,
    T(180, 16, 'One form – many functions', 'Eine Form – viele Funktionen', 13, 800)
    + box(70, 30, 220, 50, '“Can you open the window?”', '„Can you open the window?“', tip=('FORM: an interrogative sentence (a question) with the modal verb “can”. This is its structure.', 'FORM: ein Fragesatz (Interrogativsatz) mit dem Modalverb „can“. Das ist seine Struktur.'), art='hl', size=13)
    + T(180, 96, 'form = structure: a yes/no question', 'Form = Struktur: eine Ja/Nein-Frage', 12, 700)
    + pfeil(120, 104, 64, 140) + pfeil(180, 104, 180, 140) + pfeil(240, 104, 296, 140)
    + box(4, 144, 116, 64, 'request\n(please do it)', 'Bitte\n(mach es bitte)', tip=('FUNCTION 1: a polite request. Most of the time this is what the question is used for.', 'FUNKTION 1: eine höfliche Bitte. Meist wird die Frage genau dafür verwendet.'))
    + box(122, 144, 116, 64, 'question about\nability', 'Frage nach\nFähigkeit', tip=('FUNCTION 2: a real question – e.g. a doctor asks a patient with a hurt arm whether he is able to open it.', 'FUNKTION 2: eine echte Frage – z. B. fragt eine Ärztin einen Patienten mit verletztem Arm, ob er es schafft.'))
    + box(240, 144, 116, 64, 'complaint\n(it is hot!)', 'Beschwerde\n(es ist heiß!)', tip=('FUNCTION 3: an indirect complaint about the heat in the room.', 'FUNKTION 3: eine indirekte Beschwerde über die Hitze im Raum.'))
    + T(180, 226, 'function = purpose in communication', 'Funktion = Zweck in der Kommunikation', 12, 700),
    'One form with several functions', maxw=420)

fig_ff2 = svg(360, 220,
    T(180, 16, 'One function – many forms', 'Eine Funktion – viele Formen', 13, 800)
    + box(110, 30, 140, 44, 'request', 'Bitte', tip=('One function: you want someone to open the window.', 'Eine Funktion: Jemand soll das Fenster öffnen.'), art='hl', size=13)
    + pfeil(150, 74, 70, 104) + pfeil(180, 74, 180, 104) + pfeil(210, 74, 290, 104)
    + box(4, 108, 116, 60, 'imperative\n“Open the\nwindow!”', 'Imperativ\n„Open the\nwindow!“', tip=('Form: imperative sentence.', 'Form: Aufforderungssatz.'))
    + box(122, 108, 116, 60, 'question\n“Could you …?”', 'Frage\n„Could you …?“', tip=('Form: interrogative sentence.', 'Form: Fragesatz.'))
    + box(240, 108, 116, 60, 'statement\n“It’s hot in\nhere.”', 'Aussage\n„It’s hot in\nhere.“', tip=('Form: declarative sentence – still works as a request.', 'Form: Aussagesatz – funktioniert trotzdem als Bitte.'))
    + T(180, 196, 'same purpose, different structures', 'gleicher Zweck, verschiedene Strukturen', 12, 700),
    'One function with several forms', maxw=420)

t_ff = thema('form-function', ('Form vs. function', 'Form vs. Funktion'), star=True,
    kern=('Form is the structure of language: its sounds, word forms and sentence patterns – how something is said. Function is what this form is used for in communication – its purpose or meaning in a situation. Statement 1.2 of the worksheet is FALSE: the pair has nothing to do with basic messages vs. mastery.',
          'Form ist die Struktur der Sprache: Laute, Wortformen und Satzmuster – wie etwas gesagt wird. Funktion ist, wofür diese Form in der Kommunikation verwendet wird – ihr Zweck oder ihre Bedeutung in einer Situation. Aussage 1.2 des Arbeitsblatts ist FALSCH: Das Paar hat nichts mit einfachen Botschaften vs. Sprachbeherrschung zu tun.'),
    kurz=('<p>Your teacher says: “Can you open the window?” Grammatically this is a <b>question</b> – that is its <b>form</b>. But nobody answers “Yes, I can” and stays seated. Everybody understands it as a <b>request</b> – that is its <b>function</b>.</p><p>So: <b>form</b> = what it looks like (the structure). <b>Function</b> = what it does (the purpose).</p><p>The worksheet statement claims that form means “mastery of the language” and function means “only basic messages”. That mixes the pair up with how <i>well</i> someone speaks. Wrong – both terms describe language itself, not the speaker’s skill.</p>',
          '<p>Deine Lehrerin sagt: „Can you open the window?“ Grammatisch ist das eine <b>Frage</b> – das ist die <b>Form</b>. Aber niemand antwortet „Ja, kann ich“ und bleibt sitzen. Alle verstehen es als <b>Bitte</b> – das ist die <b>Funktion</b>.</p><p>Also: <b>Form</b> = wie es aussieht (die Struktur). <b>Funktion</b> = was es bewirkt (der Zweck).</p><p>Die Aussage im Arbeitsblatt behauptet, Form heiße „Beherrschung der Sprache“ und Funktion „nur einfache Botschaften“. Das verwechselt das Paar damit, wie <i>gut</i> jemand spricht. Falsch – beide Begriffe beschreiben die Sprache selbst, nicht das Können des Sprechers.</p>'),
    fig=fw('The same question can do very different jobs. Tap the boxes.', 'Dieselbe Frage kann ganz verschiedene Aufgaben erfüllen. Tippe auf die Kästen.') + bild(fig_ff),
    figcap=('classroom example', 'Beispiel aus dem Unterricht'),
    article=h3('Form: the structure', 'Form: die Struktur')
        + p('<b>Form</b> refers to the <b>structure of linguistic units</b>: how they sound, how words are built and how sentences are put together. ' + eg('what you can see and hear – the “shape” of language.', 'was man sehen und hören kann – die „Gestalt“ der Sprache.'),
            '<b>Form</b> bezeichnet die <b>Struktur sprachlicher Einheiten</b>: wie sie klingen, wie Wörter gebaut sind und wie Sätze zusammengesetzt werden. ' + eg('what you can see and hear – the “shape” of language.', 'was man sehen und hören kann – die „Gestalt“ der Sprache.'))
        + cards([('Sound', 'Laut', '/frɒg/ – three consonants and a vowel', '/frɒg/ – drei Konsonanten und ein Vokal'),
                 ('Word', 'Wort', '<i>walk-ed</i>: stem + past tense ending', '<i>walk-ed</i>: Stamm + Vergangenheitsendung'),
                 ('Sentence', 'Satz', '“Can you …?” – inverted word order = question', '„Can you …?“ – umgestellte Wortstellung = Frage')])
        + weiter('Form alone does not tell you what a speaker wants. For that you need the second side.', 'Die Form allein verrät nicht, was ein Sprecher will. Dafür braucht man die zweite Seite.')
        + h3('Function: the purpose', 'Funktion: der Zweck')
        + p('<b>Function</b> refers to <b>what a form is used for</b> in communication: to ask, to request, to warn, to greet, to complain … ' + eg('the job a piece of language does in a real situation.', 'die Aufgabe, die ein Stück Sprache in einer echten Situation erfüllt.'),
            '<b>Funktion</b> bezeichnet, <b>wofür eine Form</b> in der Kommunikation <b>verwendet wird</b>: fragen, bitten, warnen, grüßen, sich beschweren … ' + eg('the job a piece of language does in a real situation.', 'die Aufgabe, die ein Stück Sprache in einer echten Situation erfüllt.'))
        + p('Form and function do not match one to one. One form can have many functions (see the figure above), and one function can be expressed by many forms:',
            'Form und Funktion passen nicht eins zu eins zusammen. Eine Form kann viele Funktionen haben (siehe Schaubild oben), und eine Funktion kann durch viele Formen ausgedrückt werden:')
        + mfig('One function – many forms', 'Eine Funktion – viele Formen', fig_ff2)
        + weiter('Now to the statement in the worksheet and why it is false.', 'Jetzt zur Aussage im Arbeitsblatt und warum sie falsch ist.')
        + h3('Worksheet 1.2: what is wrong?', 'Arbeitsblatt 1.2: Was ist falsch?')
        + gegen(('The statement says', 'Die Aussage sagt', 'function = only basic messages · form = mastery of the language', 'Funktion = nur einfache Botschaften · Form = Beherrschung der Sprache'),
                ('Correct is', 'Richtig ist', 'form = the structure of language · function = its purpose/use in communication', 'Form = die Struktur der Sprache · Funktion = ihr Zweck/Gebrauch in der Kommunikation'))
        + klausur_hinweis('Tick b (false). Correct answer: “Form refers to the structure of language (sounds, words, sentences), function refers to what the form is used for in communication (its purpose).”', 'b (falsch) ankreuzen. Richtige Antwort: „Form refers to the structure of language (sounds, words, sentences), function refers to what the form is used for in communication (its purpose).“')
        + einfacher('Form = the packaging. Function = what is inside and why you send it. The same box (a question) can contain a request, a real question or a complaint.', 'Form = die Verpackung. Funktion = was drin ist und wozu man es schickt. Dieselbe Schachtel (eine Frage) kann eine Bitte, eine echte Frage oder eine Beschwerde enthalten.')
        + wahr('w-ff', [
            ('“Can you pass the salt?” has the form of a question and the function of a request.', '„Can you pass the salt?“ hat die Form einer Frage und die Funktion einer Bitte.', True, 'Classic example.', 'Klassisches Beispiel.'),
            ('Form describes how well a speaker masters a language.', 'Form beschreibt, wie gut ein Sprecher eine Sprache beherrscht.', False, 'Form = structure of language.', 'Form = Struktur der Sprache.'),
            ('One function can be expressed by several different forms.', 'Eine Funktion kann durch mehrere verschiedene Formen ausgedrückt werden.', True, 'e.g. imperative, question, statement as request.', 'z. B. Imperativ, Frage, Aussage als Bitte.'),
            ('The past tense ending -ed is an example of function.', 'Die Vergangenheitsendung -ed ist ein Beispiel für Funktion.', False, 'It is part of the form (word structure).', 'Sie gehört zur Form (Wortstruktur).')]),
    merk=('Form = the structure of language (sounds, words, sentences: HOW it is said). Function = the purpose/use in communication (WHAT FOR it is said).', 'Form = die Struktur der Sprache (Laute, Wörter, Sätze: WIE es gesagt wird). Funktion = der Zweck/Gebrauch in der Kommunikation (WOZU es gesagt wird).'),
    exam=('Worksheet 1.2: FALSE. Correct answer: form = structure, function = purpose/use in communication.', 'Arbeitsblatt 1.2: FALSCH. Richtige Antwort: Form = Struktur, Funktion = Zweck/Gebrauch in der Kommunikation.'),
    fehler=[('Linking form/function to the speaker’s skill level.', 'Form/Funktion mit dem Sprachniveau des Sprechers verbinden.'),
            ('Thinking every question is used to ask for information.', 'Denken, jede Frage diene dazu, nach Informationen zu fragen.')],
    src='Worksheet 1.2')

# ---------------------------------------------------------------- 3 applied / theoretical
fig_at = svg(360, 250,
    box(120, 6, 120, 40, 'Linguistics', 'Sprachwissenschaft', art='hl', size=13, tip=('The scientific study of language.', 'Die wissenschaftliche Erforschung der Sprache.'))
    + pfeil(160, 46, 92, 70) + pfeil(200, 46, 268, 70)
    + punktkasten(4, 72, 174, 172, ('Theoretical (“not applied”)', 'Theoretisch („nicht angewandt“)'),
                  [('phonetics & phonology (sounds)', 'Phonetik & Phonologie (Laute)'), ('morphology (words)', 'Morphologie (Wörter)'), ('syntax (sentences)', 'Syntax (Sätze)'), ('semantics (meaning)', 'Semantik (Bedeutung)')],
                  tip=('Studies language for its own sake: How is the system built? Why does it work like this? Not old, not out of use!', 'Erforscht Sprache um ihrer selbst willen: Wie ist das System gebaut? Warum funktioniert es so? Nicht alt, nicht veraltet!'))
    + punktkasten(182, 72, 174, 172, ('Applied', 'Angewandt'),
                  [('language teaching (e.g. English as a foreign language)', 'Sprachunterricht (z. B. Englisch als Fremdsprache)'), ('translation & interpreting', 'Übersetzen & Dolmetschen'), ('speech therapy', 'Sprachtherapie'), ('forensic linguistics, dictionaries', 'forensische Linguistik, Wörterbücher')],
                  tip=('Uses linguistic findings to solve practical, real-life problems.', 'Nutzt sprachwissenschaftliche Erkenntnisse, um praktische Probleme zu lösen.')),
    'Theoretical and applied linguistics', maxw=420)

t_at = thema('applied-theoretical', ('Applied vs. theoretical linguistics', 'Angewandte vs. theoretische Sprachwissenschaft'), star=True,
    kern=('Theoretical (“not applied”) linguistics studies language for its own sake: it describes and explains how the language system works. Applied linguistics uses these findings to solve real-life problems such as language teaching, translation or speech therapy. Statement 1.3 is FALSE: the pair has nothing to do with past vs. present.',
          'Theoretische („nicht angewandte“) Sprachwissenschaft erforscht Sprache um ihrer selbst willen: Sie beschreibt und erklärt, wie das Sprachsystem funktioniert. Angewandte Sprachwissenschaft nutzt diese Erkenntnisse, um praktische Probleme zu lösen, etwa im Sprachunterricht, beim Übersetzen oder in der Sprachtherapie. Aussage 1.3 ist FALSCH: Das Paar hat nichts mit Vergangenheit vs. Gegenwart zu tun.'),
    kurz=('<p>Think of medicine. Some researchers study <b>how the heart works</b> – that is basic research. Doctors <b>use</b> this knowledge to treat a patient – that is application.</p><p>Linguistics is the same. <b>Theoretical</b> linguists ask: How are English sentences built? Which sounds does English use? <b>Applied</b> linguists take these answers and use them for a real problem: How do I teach German pupils the English “th”? How do I help a child who cannot pronounce /r/?</p><p>The worksheet claims that “not applied” means old studies that are no longer in use. That is wrong. Theoretical linguistics is alive and modern – it is simply not aimed at a practical problem.</p>',
          '<p>Denk an die Medizin. Manche Forscher untersuchen, <b>wie das Herz funktioniert</b> – das ist Grundlagenforschung. Ärzte <b>nutzen</b> dieses Wissen, um Patienten zu behandeln – das ist Anwendung.</p><p>In der Sprachwissenschaft ist es genauso. <b>Theoretische</b> Linguisten fragen: Wie sind englische Sätze gebaut? Welche Laute nutzt das Englische? <b>Angewandte</b> Linguisten nehmen diese Antworten und nutzen sie für ein echtes Problem: Wie bringe ich deutschen Schülern das englische „th“ bei? Wie helfe ich einem Kind, das kein /r/ sprechen kann?</p><p>Das Arbeitsblatt behauptet, „nicht angewandt“ heiße: alte Studien, die nicht mehr genutzt werden. Das ist falsch. Theoretische Sprachwissenschaft ist lebendig und modern – sie zielt nur nicht auf ein praktisches Problem.</p>'),
    fig=fw('Two branches of linguistics. Tap the two boxes.', 'Zwei Zweige der Sprachwissenschaft. Tippe auf die beiden Kästen.') + bild(fig_at),
    figcap=('overview', 'Überblick'),
    article=h3('Theoretical linguistics', 'Theoretische Sprachwissenschaft')
        + p('<b>Theoretical</b> (also: general, pure, “not applied”) linguistics studies <b>language for its own sake</b>. It <b>describes and explains</b> how the language system works – sounds, words, sentences, meaning. ' + eg('research to understand language, without a practical goal.', 'Forschung, um Sprache zu verstehen, ohne praktisches Ziel.'),
            '<b>Theoretische</b> (auch: allgemeine, reine, „nicht angewandte“) Sprachwissenschaft erforscht <b>Sprache um ihrer selbst willen</b>. Sie <b>beschreibt und erklärt</b>, wie das Sprachsystem funktioniert – Laute, Wörter, Sätze, Bedeutung. ' + eg('research to understand language, without a practical goal.', 'Forschung, um Sprache zu verstehen, ohne praktisches Ziel.'))
        + weiter('Applied linguistics starts where a real person has a real language problem.', 'Angewandte Sprachwissenschaft beginnt dort, wo ein echter Mensch ein echtes Sprachproblem hat.')
        + h3('Applied linguistics', 'Angewandte Sprachwissenschaft')
        + p('<b>Applied linguistics</b> uses the findings of linguistics to <b>solve practical, real-life problems</b> in which language plays a role.',
            '<b>Angewandte Sprachwissenschaft</b> nutzt die Erkenntnisse der Linguistik, um <b>praktische Probleme</b> zu lösen, in denen Sprache eine Rolle spielt.')
        + tabelle([('Field', 'Bereich'), ('Real-life problem', 'Praktisches Problem')], [
            [('language teaching', 'Sprachunterricht'), ('How do German pupils best learn the English present perfect?', 'Wie lernen deutsche Schüler am besten das englische Present Perfect?')],
            [('translation', 'Übersetzen'), ('How do I translate a pun into another language?', 'Wie übersetze ich ein Wortspiel in eine andere Sprache?')],
            [('speech therapy', 'Sprachtherapie'), ('A child after a stroke cannot find words – what helps?', 'Ein Kind findet nach einem Schlaganfall keine Wörter – was hilft?')],
            [('forensic linguistics', 'forensische Linguistik'), ('Who wrote this anonymous letter?', 'Wer hat diesen anonymen Brief geschrieben?')],
            [('lexicography', 'Lexikografie'), ('Which words belong in a new learner’s dictionary?', 'Welche Wörter gehören in ein neues Lernwörterbuch?')]])
        + weiter('Now to the statement in the worksheet.', 'Jetzt zur Aussage im Arbeitsblatt.')
        + h3('Worksheet 1.3: what is wrong?', 'Arbeitsblatt 1.3: Was ist falsch?')
        + gegen(('The statement says', 'Die Aussage sagt', 'applied = still has real-life uses · not applied = past studies no longer in use', 'angewandt = noch praktisch nutzbar · nicht angewandt = frühere Studien, nicht mehr genutzt'),
                ('Correct is', 'Richtig ist', 'applied = uses linguistic findings to solve practical problems · not applied (theoretical) = studies language for its own sake to describe and explain it', 'angewandt = nutzt Erkenntnisse zur Lösung praktischer Probleme · nicht angewandt (theoretisch) = erforscht Sprache um ihrer selbst willen, um sie zu beschreiben und zu erklären'))
        + falle('Thinking the difference is about time (old vs. current). It is about the GOAL: understanding language vs. solving a practical problem.', 'Denken, es gehe um die Zeit (alt vs. aktuell). Es geht um das ZIEL: Sprache verstehen vs. ein praktisches Problem lösen.')
        + klausur_hinweis('Tick b (false). Correct answer: “Applied linguistics uses linguistic findings to solve practical, real-life problems (e.g. language teaching, translation, speech therapy); ‘not applied’ (theoretical) linguistics studies language for its own sake to describe and explain how it works.”', 'b (falsch) ankreuzen. Richtige Antwort: „Applied linguistics uses linguistic findings to solve practical, real-life problems (e.g. language teaching, translation, speech therapy); ‘not applied’ (theoretical) linguistics studies language for its own sake to describe and explain how it works.“')
        + wahr('w-at', [
            ('Developing a method to teach English pronunciation is applied linguistics.', 'Eine Methode für den englischen Ausspracheunterricht zu entwickeln, ist angewandte Linguistik.', True, 'Practical problem: teaching.', 'Praktisches Problem: Unterricht.'),
            ('Theoretical linguistics only studies dead languages.', 'Theoretische Linguistik untersucht nur tote Sprachen.', False, 'It studies any language for its own sake.', 'Sie untersucht jede Sprache um ihrer selbst willen.'),
            ('Describing the rules of English word order is theoretical linguistics.', 'Die Regeln der englischen Wortstellung zu beschreiben, ist theoretische Linguistik.', True, 'Describing the system itself.', 'Das System selbst beschreiben.'),
            ('Speech therapy is an example of theoretical linguistics.', 'Sprachtherapie ist ein Beispiel für theoretische Linguistik.', False, 'It solves a real-life problem → applied.', 'Sie löst ein praktisches Problem → angewandt.')]),
    merk=('Theoretical (“not applied”) = language studied for its own sake (describe and explain the system). Applied = linguistic findings used to solve real-life problems (teaching, translation, speech therapy).', 'Theoretisch („nicht angewandt“) = Sprache um ihrer selbst willen erforscht (System beschreiben und erklären). Angewandt = Erkenntnisse zur Lösung praktischer Probleme (Unterricht, Übersetzen, Sprachtherapie).'),
    exam=('Worksheet 1.3: FALSE. Correct answer with both definitions plus one example.', 'Arbeitsblatt 1.3: FALSCH. Richtige Antwort mit beiden Definitionen und einem Beispiel.'),
    fehler=[('Explaining the pair with time (old/new) instead of goal.', 'Das Paar mit Zeit (alt/neu) statt mit dem Ziel erklären.'),
            ('Not naming an example of applied linguistics.', 'Kein Beispiel für angewandte Linguistik nennen.')],
    src='Worksheet 1.3')

KAPITEL = kapitel('k1', ('Dichotomies', 'Dichotomien'),
    ('Three pairs of terms that look at language from two sides: synchronic/diachronic, form/function and theoretical/applied. In the exam they come as true-or-false statements with a correction. Running example: the English word “nice”.',
     'Drei Begriffspaare, die Sprache von zwei Seiten betrachten: synchron/diachron, Form/Funktion und theoretisch/angewandt. In der Klausur kommen sie als Richtig-oder-falsch-Aussagen mit Korrektur. Durchgehendes Beispiel: das englische Wort „nice“.'),
    ['Dichotomy', 'Synchronic/diachronic', 'Form/function', 'Applied/theoretical'], [t_dicho, t_sd, t_ff, t_at])
