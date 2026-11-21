import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from z import *

# Durchgehendes Beispiel in diesem Oberthema: der Frosch /frɒg/ vom Arbeitsblatt
R = lambda x, y, w, h, art: f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" style="{art}" stroke-width="1.3"/>'

# ---------------------------------------------------------------- 1 Structuralism: Saussure, langue, parole
fig_lp = svg(360, 236,
    T(180, 16, 'Langue and parole', 'Langue und parole', 13, 800)
    + tpg(R(70, 30, 220, 86, 'fill:var(--primary);stroke:var(--primary)')
          + T(180, 54, 'LANGUE', 'LANGUE', 14, 800, fill='var(--on-primary)')
          + T(180, 80, 'the abstract system', 'das abstrakte System', 12, 700, fill='var(--on-primary)')
          + T(180, 98, 'shared by the whole community', 'geteilt von der ganzen Gemeinschaft', 12, 600, fill='var(--on-primary)'),
          ('LANGUE: the abstract language system (rules, signs, sounds) shared by ALL members of a speech community. Main interest of structuralism.', 'LANGUE: das abstrakte Sprachsystem (Regeln, Zeichen, Laute), das ALLE Mitglieder einer Sprachgemeinschaft teilen. Hauptinteresse des Strukturalismus.'))
    + pfeil(110, 116, 60, 150) + pfeil(180, 116, 180, 150) + pfeil(250, 116, 300, 150)
    + box(4, 154, 112, 56, 'Anna says\n“Hi there!”', 'Anna sagt\n„Hi there!“', tip=('PAROLE: one concrete utterance by one individual.', 'PAROLE: eine konkrete Äußerung eines Einzelnen.'))
    + box(124, 154, 112, 56, 'Ben writes\n“Hey :)”', 'Ben schreibt\n„Hey :)“', tip=('PAROLE: another concrete use of the same system.', 'PAROLE: ein anderer konkreter Gebrauch desselben Systems.'))
    + box(244, 154, 112, 56, 'Cleo says\n“Hello!”', 'Cleo sagt\n„Hello!“', tip=('PAROLE: concrete, individual language use – always different.', 'PAROLE: konkreter, individueller Sprachgebrauch – immer anders.'))
    + T(180, 226, 'PAROLE = concrete usage by the individual', 'PAROLE = konkreter Gebrauch durch den Einzelnen', 12, 700),
    'Langue as shared system, parole as individual use', maxw=420)

t_struk = thema('structuralism', ('Structuralism: Saussure, langue and parole', 'Strukturalismus: Saussure, langue und parole'), star=True,
    kern=('Structuralism stems from the work of Ferdinand de Saussure (around 1900). Structuralists are mainly interested in the abstract language system shared by all members of a speech community – langue – and less in parole, the concrete use of language by the individual.',
          'Der Strukturalismus geht auf Ferdinand de Saussure zurück (um 1900). Strukturalisten interessieren sich vor allem für das abstrakte Sprachsystem, das alle Mitglieder einer Sprachgemeinschaft teilen – langue – und weniger für parole, den konkreten Sprachgebrauch des Einzelnen.'),
    kurz=('<p>Think of football. There are the <b>rules</b> of the game – the same for every player in the world. And there is <b>every single match</b> – each one different, with good and bad passes.</p><p>The Swiss linguist <b>Ferdinand de Saussure</b> (around 1900) saw language the same way. The rules and signs that everybody in a speech community shares he called <b>langue</b> (French: “language”). Each concrete thing a person says or writes he called <b>parole</b> (French: “speech”).</p><p>Saussure’s school is called <b>structuralism</b> because it sees language as a <b>structure</b>: a system in which every element gets its value from its relation to the others. Structuralists study mainly <b>langue</b>, the system – not the individual matches.</p>',
          '<p>Denk an Fußball. Es gibt die <b>Regeln</b> des Spiels – für jeden Spieler auf der Welt gleich. Und es gibt <b>jedes einzelne Spiel</b> – jedes anders, mit guten und schlechten Pässen.</p><p>Der Schweizer Sprachwissenschaftler <b>Ferdinand de Saussure</b> (um 1900) sah Sprache genauso. Die Regeln und Zeichen, die alle in einer Sprachgemeinschaft teilen, nannte er <b>langue</b> (franz. „Sprache“). Jede konkrete Äußerung eines Menschen nannte er <b>parole</b> (franz. „Rede“).</p><p>Saussures Schule heißt <b>Strukturalismus</b>, weil sie Sprache als <b>Struktur</b> sieht: ein System, in dem jedes Element seinen Wert aus der Beziehung zu den anderen bekommt. Strukturalisten untersuchen vor allem die <b>langue</b>, das System – nicht die einzelnen Spiele.</p>'),
    fig=fw('One shared system, many individual uses. Tap the boxes.', 'Ein gemeinsames System, viele individuelle Verwendungen. Tippe auf die Kästen.') + bild(fig_lp),
    figcap=('after the worksheet, task 2.1', 'nach dem Arbeitsblatt, Aufgabe 2.1'),
    article=h3('Who was Saussure?', 'Wer war Saussure?')
        + p('<b>Ferdinand de Saussure</b> (1857–1913) was a Swiss linguist who taught in Geneva. He is called the <b>father of modern linguistics</b>. His lectures (1906–1911) were published after his death by his students as the <i>Course in General Linguistics</i> (<i>Cours de linguistique générale</i>, 1916).',
            '<b>Ferdinand de Saussure</b> (1857–1913) war ein Schweizer Sprachwissenschaftler, der in Genf lehrte. Er gilt als <b>Vater der modernen Sprachwissenschaft</b>. Seine Vorlesungen (1906–1911) wurden nach seinem Tod von seinen Studenten als <i>Cours de linguistique générale</i> (1916) veröffentlicht.')
        + p('Before Saussure, linguistics was mostly <b>diachronic</b>: it compared old and new forms of words. Saussure put the <b>synchronic</b> study of the language system in the centre.',
            'Vor Saussure war die Sprachwissenschaft meist <b>diachron</b>: Sie verglich alte und neue Wortformen. Saussure stellte die <b>synchrone</b> Untersuchung des Sprachsystems in den Mittelpunkt.')
        + weiter('His most important idea is the difference between the system and its use.', 'Seine wichtigste Idee ist der Unterschied zwischen dem System und seinem Gebrauch.')
        + h3('Langue and parole', 'Langue und parole')
        + gegen(('langue', 'langue', 'the <b>abstract language system</b> shared by all members of a <b>speech community</b>: its signs and rules. Social, stable, in everybody’s head.', 'das <b>abstrakte Sprachsystem</b>, das alle Mitglieder einer <b>Sprachgemeinschaft</b> teilen: seine Zeichen und Regeln. Sozial, stabil, in allen Köpfen.'),
                ('parole', 'parole', 'the <b>concrete usage of language by the individual</b>: what one person actually says or writes in one situation. Individual, changing, observable.', 'der <b>konkrete Sprachgebrauch des Einzelnen</b>: was eine Person in einer Situation tatsächlich sagt oder schreibt. Individuell, wechselnd, beobachtbar.'))
        + p('Langue is like the <b>score</b> of a piece of music, parole like each <b>performance</b> of it. Structuralists are “primarily concerned” with langue and “less so” with parole – exactly as the worksheet says.',
            'Langue ist wie die <b>Partitur</b> eines Musikstücks, parole wie jede einzelne <b>Aufführung</b>. Strukturalisten beschäftigen sich „vor allem“ mit langue und „weniger“ mit parole – genau wie im Arbeitsblatt.')
        + falle('Swapping the two terms in the gap text. Order in task 2.1: first the shared system (langue), then the concrete individual use (parole).', 'Die beiden Begriffe im Lückentext vertauschen. Reihenfolge in Aufgabe 2.1: zuerst das gemeinsame System (langue), dann der konkrete individuelle Gebrauch (parole).')
        + weiter('Why “structure”? Because in the system each element is defined by what it is not.', 'Warum „Struktur“? Weil im System jedes Element dadurch bestimmt ist, was es nicht ist.')
        + h3('Language as a system of differences', 'Sprache als System von Unterschieden')
        + p('For Saussure, a sign has value only through its <b>relations and differences</b> to other signs. <i>cat</i> means “cat” because it is not <i>bat</i>, <i>hat</i> or <i>cap</i>. Change one sound and you get another word.',
            'Für Saussure hat ein Zeichen seinen Wert nur durch seine <b>Beziehungen und Unterschiede</b> zu anderen Zeichen. <i>cat</i> bedeutet „Katze“, weil es nicht <i>bat</i>, <i>hat</i> oder <i>cap</i> ist. Ändere einen Laut und du bekommst ein anderes Wort.')
        + merkliste(('Gap text 2.1 – the three gaps', 'Lückentext 2.1 – die drei Lücken'), ('fill in exactly these words', 'genau diese Wörter einsetzen'),
                    [('“stems from the work of <b>Ferdinand de Saussure</b> (~1900)”', '„stems from the work of <b>Ferdinand de Saussure</b> (~1900)“'),
                     ('“the abstract language system shared by all members of a speech community, called <b>langue</b>”', '„the abstract language system shared by all members of a speech community, called <b>langue</b>“'),
                     ('“and less so about <b>parole</b>, which is about the concrete usage of language by the individual”', '„and less so about <b>parole</b>, which is about the concrete usage of language by the individual“')],
                    ('<b>L</b>angue = <b>L</b>aw of the community (the rules). <b>P</b>arole = <b>P</b>erson speaking.', '<b>L</b>angue = <b>L</b>eitlinien der Gemeinschaft (Regeln). <b>P</b>arole = <b>P</b>erson, die spricht.'))
        + klausur_hinweis('Spell the terms correctly: Saussure, langue, parole (French words, no capital letters needed).', 'Begriffe richtig schreiben: Saussure, langue, parole (französische Wörter, kleingeschrieben).')
        + wahr('w-lp', [
            ('Langue is the language system shared by a speech community.', 'Langue ist das Sprachsystem, das eine Sprachgemeinschaft teilt.', True, 'Shared, abstract system.', 'Gemeinsames, abstraktes System.'),
            ('Parole is the main interest of structuralism.', 'Parole ist das Hauptinteresse des Strukturalismus.', False, 'Main interest: langue.', 'Hauptinteresse: langue.'),
            ('A text message you write to a friend is an example of parole.', 'Eine Nachricht an eine Freundin ist ein Beispiel für parole.', True, 'Concrete, individual usage.', 'Konkreter, individueller Gebrauch.'),
            ('Saussure wrote the Course in General Linguistics himself and published it in 1900.', 'Saussure schrieb den Cours selbst und veröffentlichte ihn 1900.', False, 'His students published it in 1916, after his death.', 'Seine Studenten veröffentlichten ihn 1916, nach seinem Tod.')]),
    merk=('Structuralism: Ferdinand de Saussure (~1900). Langue = abstract language system shared by all members of a speech community (main interest). Parole = concrete usage of language by the individual.', 'Strukturalismus: Ferdinand de Saussure (~1900). Langue = abstraktes Sprachsystem aller Mitglieder einer Sprachgemeinschaft (Hauptinteresse). Parole = konkreter Sprachgebrauch des Einzelnen.'),
    exam=('Gap text 2.1: Saussure – langue – parole.', 'Lückentext 2.1: Saussure – langue – parole.'),
    fehler=[('Swapping langue and parole.', 'Langue und parole vertauschen.'),
            ('Writing Chomsky instead of Saussure for structuralism.', 'Beim Strukturalismus Chomsky statt Saussure schreiben.')],
    src='Worksheet 2.1')

# ---------------------------------------------------------------- 2 the linguistic sign
def _frosch(cx, cy):
    """sehr einfacher Frosch aus Kreisen (Theme-Farben)"""
    return (f'<ellipse cx="{cx}" cy="{cy + 8}" rx="30" ry="20" style="fill:var(--pale);stroke:var(--ink)" stroke-width="1.6"/>'
            f'<circle cx="{cx - 14}" cy="{cy - 10}" r="9" style="fill:var(--card);stroke:var(--ink)" stroke-width="1.6"/>'
            f'<circle cx="{cx + 14}" cy="{cy - 10}" r="9" style="fill:var(--card);stroke:var(--ink)" stroke-width="1.6"/>'
            f'<circle cx="{cx - 14}" cy="{cy - 10}" r="3.2" style="fill:var(--ink)"/><circle cx="{cx + 14}" cy="{cy - 10}" r="3.2" style="fill:var(--ink)"/>'
            f'<path d="M{cx - 12} {cy + 10} Q {cx} {cy + 18} {cx + 12} {cy + 10}" style="fill:none;stroke:var(--ink)" stroke-width="1.6"/>')

fig_zeichen = svg(360, 250,
    tpg(f'<circle cx="100" cy="125" r="92" style="fill:var(--card);stroke:var(--ink)" stroke-width="2"/>'
        + f'<line x1="8" y1="125" x2="192" y2="125" style="stroke:var(--ink)" stroke-width="2"/>',
        ('The linguistic sign has two sides, like a sheet of paper: you cannot cut one side without the other.', 'Das sprachliche Zeichen hat zwei Seiten wie ein Blatt Papier: Man kann nicht eine Seite schneiden, ohne die andere.'))
    + tpg(_frosch(100, 80) + T(100, 112, 'concept', 'Konzept', 12, 700), ('SIGNIFIÉ (signified): the concept or mental idea of a frog – not a real frog in the pond!', 'SIGNIFIÉ (Bezeichnetes): das Konzept, die Vorstellung eines Frosches – kein echter Frosch im Teich!'))
    + tpg(T(100, 165, '/frɒg/', '/frɒg/', 22, 600) + T(100, 194, 'sound image', 'Lautbild', 12, 700), ('SIGNIFIANT (signifier): the sound image /frɒg/ – the mental picture of the sound sequence.', 'SIGNIFIANT (Bezeichnendes): das Lautbild /frɒg/ – die Vorstellung der Lautfolge.'))
    + pfeil(16, 150, 16, 100, 'var(--axis2)') + pfeil(184, 100, 184, 150, 'var(--axis2)')
    + f'<line x1="180" y1="70" x2="208" y2="56" style="stroke:var(--ink)" stroke-width="1.5"/><line x1="182" y1="170" x2="208" y2="184" style="stroke:var(--ink)" stroke-width="1.5"/>'
    + box(210, 26, 146, 62, 'signifié\n(signified)\n= the concept', 'signifié\n(Bezeichnetes)\n= das Konzept', tip=('Gap answer 2.1 (top line): the concept / mental image, i.e. that which is signified.', 'Lösung der oberen Linie in 2.1: das Konzept / die Vorstellung, also das Bezeichnete.'), art='hl', size=12)
    + box(210, 154, 146, 62, 'signifiant\n(signifier)\n= sound image', 'signifiant\n(Bezeichnendes)\n= Lautbild', tip=('Gap answer 2.1 (bottom line): signifiant (signifier) – the sound image, i.e. that which signifies.', 'Lösung der unteren Linie in 2.1: signifiant (Bezeichnendes) – das Lautbild, also das Bezeichnende.'), size=12)
    + T(180, 240, 'Saussure’s linguistic sign', 'Saussures sprachliches Zeichen', 12, 700),
    'Saussure’s linguistic sign with signifié and signifiant', maxw=420)

fig_arbi = svg(360, 170,
    box(120, 6, 120, 50, 'concept\nFROG', 'Konzept\nFROSCH', art='hl', size=13, tip=('One and the same concept …', 'Ein und dasselbe Konzept …'))
    + pfeil(150, 56, 60, 100) + pfeil(180, 56, 180, 100) + pfeil(210, 56, 300, 100)
    + box(4, 104, 112, 50, 'English\n/frɒg/', 'Englisch\n/frɒg/', tip=('… is called frog in English,', '… heißt im Englischen frog,'))
    + box(124, 104, 112, 50, 'German\n/frɔʃ/', 'Deutsch\n/frɔʃ/', tip=('… Frosch in German,', '… im Deutschen Frosch,'))
    + box(244, 104, 112, 50, 'French\n/ɡʁənuj/', 'Französisch\n/ɡʁənuj/', tip=('… and grenouille in French. Nothing in the animal forces any of these sounds: the link is arbitrary.', '… und im Französischen grenouille. Nichts am Tier erzwingt einen dieser Laute: Die Verbindung ist arbiträr.')),
    'The arbitrariness of the sign', maxw=420)

t_zeichen = thema('linguistic-sign', ('The linguistic sign: signifié and signifiant', 'Das sprachliche Zeichen: signifié und signifiant'), star=True,
    kern=('For Saussure, every linguistic sign has two inseparable sides: the signifié (signified) is the concept or mental idea, e.g. the idea of a frog; the signifiant (signifier) is the sound image, e.g. /frɒg/ – that which signifies. The link between them is arbitrary.',
          'Für Saussure hat jedes sprachliche Zeichen zwei untrennbare Seiten: Das signifié (Bezeichnetes) ist das Konzept oder die Vorstellung, z. B. die Idee eines Frosches; das signifiant (Bezeichnendes) ist das Lautbild, z. B. /frɒg/ – das, was bezeichnet. Die Verbindung zwischen beiden ist arbiträr (willkürlich).'),
    kurz=('<p>When you hear the sounds /frɒg/, a picture pops up in your head: a small green animal that jumps and croaks. Saussure says: a word is exactly this <b>pair</b>.</p><p>Side 1 is the <b>concept</b> in your head – the <b>signifié</b> (“the signified”, what is meant). Side 2 is the <b>sound image</b> /frɒg/ – the <b>signifiant</b> (“the signifier”, what does the meaning).</p><p>Like the two sides of a sheet of paper, they always belong together. And the connection is <b>arbitrary</b>: nothing about a frog sounds like /frɒg/. Germans say <i>Frosch</i>, the French <i>grenouille</i> – same concept, different sound image.</p>',
          '<p>Wenn du die Laute /frɒg/ hörst, erscheint ein Bild in deinem Kopf: ein kleines grünes Tier, das hüpft und quakt. Saussure sagt: Ein Wort ist genau dieses <b>Paar</b>.</p><p>Seite 1 ist das <b>Konzept</b> in deinem Kopf – das <b>signifié</b> („das Bezeichnete“, was gemeint ist). Seite 2 ist das <b>Lautbild</b> /frɒg/ – das <b>signifiant</b> („das Bezeichnende“, das, was die Bedeutung trägt).</p><p>Wie die zwei Seiten eines Blattes Papier gehören sie immer zusammen. Und die Verbindung ist <b>arbiträr</b>: Nichts an einem Frosch klingt nach /frɒg/. Deutsche sagen <i>Frosch</i>, Franzosen <i>grenouille</i> – gleiches Konzept, anderes Lautbild.</p>'),
    fig=fw('The frog from the worksheet: tap the two halves and the two labels.', 'Der Frosch vom Arbeitsblatt: Tippe auf die beiden Hälften und die zwei Beschriftungen.') + bild(fig_zeichen),
    figcap=('after the worksheet, task 2.1 (figure)', 'nach dem Arbeitsblatt, Aufgabe 2.1 (Abbildung)'),
    article=h3('Two sides of one sign', 'Zwei Seiten eines Zeichens')
        + tabelle([('Term', 'Begriff'), ('Meaning', 'Bedeutung'), ('Frog example', 'Frosch-Beispiel')], [
            [('<b>signifié</b> (signified)', '<b>signifié</b> (Bezeichnetes)'), ('the <b>concept</b>, the mental idea – that which is signified', 'das <b>Konzept</b>, die Vorstellung – das Bezeichnete'), ('the idea of a small green jumping animal', 'die Vorstellung eines kleinen grünen hüpfenden Tieres')],
            [('<b>signifiant</b> (signifier)', '<b>signifiant</b> (Bezeichnendes)'), ('the <b>sound image</b> – that which signifies', 'das <b>Lautbild</b> – das Bezeichnende'), ('/frɒg/', '/frɒg/')]])
        + p('Both sides are <b>mental</b>. The signifiant is not the physical sound wave, but the sound pattern stored in our head. The signifié is not the real animal, but our idea of it. ' + eg('a sign connects an idea with a sound pattern – both in the mind.', 'ein Zeichen verbindet eine Idee mit einem Lautmuster – beides im Kopf.'),
            'Beide Seiten sind <b>gedanklich</b>. Das signifiant ist nicht die physikalische Schallwelle, sondern das im Kopf gespeicherte Lautmuster. Das signifié ist nicht das echte Tier, sondern unsere Vorstellung davon. ' + eg('a sign connects an idea with a sound pattern – both in the mind.', 'ein Zeichen verbindet eine Idee mit einem Lautmuster – beides im Kopf.'))
        + falle('Writing “the real frog” for signifié. The real frog in the pond is the referent – Saussure’s signifié is the CONCEPT.', 'Beim signifié „der echte Frosch“ schreiben. Der echte Frosch im Teich ist der Referent – Saussures signifié ist das KONZEPT.')
        + einfacher('signifIÉ ends like “meant” in French grammar: what is meant. signifiANT is the active one: the sound that does the meaning.', 'signifIÉ ist die „erledigte“ Form: das Gemeinte. signifiANT ist die aktive Form: der Laut, der etwas bedeutet.')
        + weiter('Why do English speakers say /frɒg/ and not something else? There is no natural reason.', 'Warum sagen Englischsprecher /frɒg/ und nicht etwas anderes? Dafür gibt es keinen natürlichen Grund.')
        + h3('The sign is arbitrary', 'Das Zeichen ist arbiträr')
        + p('The link between signifiant and signifié is <b>arbitrary</b>: there is no natural connection between the sounds and the concept. ' + eg('it is a convention – the community simply agreed on it.', 'es ist eine Konvention – die Gemeinschaft hat sich einfach darauf geeinigt.'),
            'Die Verbindung zwischen signifiant und signifié ist <b>arbiträr</b> (willkürlich): Es gibt keine natürliche Verbindung zwischen den Lauten und dem Konzept. ' + eg('it is a convention – the community simply agreed on it.', 'es ist eine Konvention – die Gemeinschaft hat sich einfach darauf geeinigt.'))
        + mfig('One concept – different sound images', 'Ein Konzept – verschiedene Lautbilder', fig_arbi)
        + p('Because the sign is a convention of the whole community, it belongs to <b>langue</b>: one person alone cannot decide to call a frog “blib”.',
            'Weil das Zeichen eine Konvention der ganzen Gemeinschaft ist, gehört es zur <b>langue</b>: Ein Einzelner kann nicht beschließen, einen Frosch „blib“ zu nennen.')
        + zusatz('A small exception are onomatopoeic words like <i>cuckoo</i> or <i>splash</i>, which imitate sounds. But even they differ between languages (English <i>ribbit</i>, German <i>quak</i>).', 'Eine kleine Ausnahme sind lautmalerische Wörter wie <i>cuckoo</i> oder <i>splash</i>, die Geräusche nachahmen. Aber auch sie unterscheiden sich zwischen Sprachen (englisch <i>ribbit</i>, deutsch <i>quak</i>).')
        + klausur_hinweis('In the figure of task 2.1 the top line asks for the meaning of signifié: “the concept (the mental idea), i.e. that which is signified”. The bottom line asks for the term: “signifiant (signifier)”.', 'In der Abbildung von Aufgabe 2.1 fragt die obere Linie nach der Bedeutung von signifié: „the concept (the mental idea), i.e. that which is signified“. Die untere Linie fragt nach dem Begriff: „signifiant (signifier)“.')
        + wahr('w-zeichen', [
            ('The signifiant of “frog” is the sound image /frɒg/.', 'Das signifiant von „frog“ ist das Lautbild /frɒg/.', True, 'Sound image = signifier.', 'Lautbild = Bezeichnendes.'),
            ('The signifié is the real frog sitting in a pond.', 'Das signifié ist der echte Frosch im Teich.', False, 'It is the concept, not the real animal.', 'Es ist das Konzept, nicht das echte Tier.'),
            ('“Arbitrary” means that there is no natural link between sound and concept.', '„Arbiträr“ heißt: keine natürliche Verbindung zwischen Laut und Konzept.', True, 'It is a convention.', 'Es ist eine Konvention.'),
            ('Signifié and signifiant can exist separately.', 'Signifié und signifiant können getrennt existieren.', False, 'Two sides of one sheet of paper.', 'Zwei Seiten eines Blattes.')]),
    merk=('Linguistic sign (Saussure) = signifié (signified: the concept / mental idea, that which is signified) + signifiant (signifier: the sound image, that which signifies). The link is arbitrary.', 'Sprachliches Zeichen (Saussure) = signifié (Bezeichnetes: Konzept / Vorstellung) + signifiant (Bezeichnendes: Lautbild). Die Verbindung ist arbiträr.'),
    exam=('Label the sign model in 2.1: signifié = the concept; signifiant (signifier) = the sound image.', 'Zeichenmodell in 2.1 beschriften: signifié = das Konzept; signifiant (signifier) = das Lautbild.'),
    fehler=[('Signifié = real object (that is the referent).', 'Signifié = echter Gegenstand (das ist der Referent).'),
            ('Swapping signifié and signifiant.', 'Signifié und signifiant vertauschen.')],
    src='Worksheet 2.1 (figure)')

# ---------------------------------------------------------------- 3 Formalism: Chomsky, LAD, Universal Grammar
fig_lad = svg(360, 232,
    T(180, 16, 'Chomsky: how children acquire language', 'Chomsky: wie Kinder Sprache erwerben', 13, 800)
    + box(4, 40, 100, 70, 'input:\nthe English\nthey hear', 'Input:\ndas Englisch,\ndas es hört', tip=('Children hear limited, often incomplete language – yet they learn the full grammar. (“poverty of the stimulus”)', 'Kinder hören begrenzte, oft unvollständige Sprache – und lernen trotzdem die ganze Grammatik. („Armut des Stimulus“)'))
    + pfeil(104, 75, 124, 75)
    + tpg(R(126, 30, 112, 92, 'fill:var(--primary);stroke:var(--primary)')
          + T(182, 56, 'LAD', 'LAD', 16, 800, fill='var(--on-primary)')
          + T(182, 82, 'language', 'Sprach-', 12, 700, fill='var(--on-primary)') + T(182, 98, 'acquisition device', 'erwerbsapparat', 12, 700, fill='var(--on-primary)'),
          ('Language Acquisition Device: an innate mental ability every human is born with. Humans are genetically predisposed to learn language.', 'Language Acquisition Device (Spracherwerbsapparat): eine angeborene geistige Fähigkeit, mit der jeder Mensch geboren wird. Menschen sind genetisch dafür veranlagt, Sprache zu lernen.'))
    + pfeil(238, 75, 256, 75)
    + box(258, 40, 98, 70, 'output:\nEnglish\ngrammar', 'Output:\nenglische\nGrammatik', tip=('The result: the child knows the grammar of its mother tongue (competence).', 'Ergebnis: Das Kind kennt die Grammatik seiner Muttersprache (Kompetenz).'))
    + pfeil(182, 122, 182, 148)
    + box(70, 150, 224, 60, 'Universal Grammar (UG)\nsyntactic structures and constraints\nshared by all languages – innate', 'Universalgrammatik (UG)\nsyntaktische Strukturen und Regeln,\nallen Sprachen gemeinsam – angeboren', tip=('The LAD contains Universal Grammar: syntactic structures and constraints that are thought to be universal in human languages and thus innate.', 'Der LAD enthält die Universalgrammatik: syntaktische Strukturen und Beschränkungen, die als universell in menschlichen Sprachen und damit als angeboren gelten.'), size=12)
    + T(180, 226, 'Noam Chomsky, 1950s and 1960s', 'Noam Chomsky, 1950er und 1960er', 12, 700),
    'Language acquisition device and Universal Grammar', maxw=420)

t_chomsky = thema('formalism-chomsky', ('Formalism: Chomsky, LAD and Universal Grammar', 'Formalismus: Chomsky, LAD und Universalgrammatik'), star=True,
    kern=('Formalism is widely associated with Noam Chomsky’s work in the 1950s and 1960s. He views every human as being born with a language acquisition device (LAD): humans are genetically predisposed to learn language. This is based on the theory of Universal Grammar – syntactic structures and constraints thought to be universal in human languages and therefore innate.',
          'Der Formalismus wird vor allem mit Noam Chomskys Arbeiten der 1950er und 1960er Jahre verbunden. Er sieht jeden Menschen mit einem Spracherwerbsapparat (language acquisition device, LAD) geboren: Menschen sind genetisch dafür veranlagt, Sprache zu lernen. Grundlage ist die Theorie der Universalgrammatik – syntaktische Strukturen und Beschränkungen, die als universell in menschlichen Sprachen und damit als angeboren gelten.'),
    kurz=('<p>A three-year-old says “I goed to the park”. Nobody ever said <i>goed</i> to her. She invented it – by applying the rule “past = verb + -ed”. Children do not just copy; they <b>build grammar rules</b> by themselves, very fast, from little and messy input.</p><p>The American linguist <b>Noam Chomsky</b> asked: how is this possible? His answer (1950s/60s): every human is <b>born</b> with a special ability for language, a <b>language acquisition device (LAD)</b>. We are genetically prepared to learn language, like birds are prepared to fly.</p><p>Inside this “device” is <b>Universal Grammar</b>: basic syntactic structures and rules that all human languages share. That is why it is called <b>innate</b> – it is there from birth.</p>',
          '<p>Eine Dreijährige sagt „I goed to the park“. Niemand hat je <i>goed</i> zu ihr gesagt. Sie hat es erfunden – indem sie die Regel „Vergangenheit = Verb + -ed“ anwendet. Kinder kopieren nicht einfach; sie <b>bauen sich Grammatikregeln</b> selbst, sehr schnell, aus wenig und unordentlichem Input.</p><p>Der amerikanische Sprachwissenschaftler <b>Noam Chomsky</b> fragte: Wie ist das möglich? Seine Antwort (1950er/60er): Jeder Mensch wird mit einer besonderen Fähigkeit für Sprache <b>geboren</b>, einem <b>Spracherwerbsapparat (language acquisition device, LAD)</b>. Wir sind genetisch darauf vorbereitet, Sprache zu lernen, wie Vögel aufs Fliegen.</p><p>In diesem „Apparat“ steckt die <b>Universalgrammatik</b>: grundlegende syntaktische Strukturen und Regeln, die alle menschlichen Sprachen teilen. Deshalb heißt sie <b>angeboren</b> – sie ist von Geburt an da.</p>'),
    fig=fw('From input to grammar: tap the LAD and Universal Grammar.', 'Vom Input zur Grammatik: Tippe auf LAD und Universalgrammatik.') + bild(fig_lad),
    figcap=('after the worksheet, task 2.2', 'nach dem Arbeitsblatt, Aufgabe 2.2'),
    article=h3('Noam Chomsky', 'Noam Chomsky')
        + p('<b>Noam Chomsky</b> (born 1928) is an American linguist at MIT. His books <i>Syntactic Structures</i> (1957) and <i>Aspects of the Theory of Syntax</i> (1965) changed linguistics. That is why the worksheet says “Chomsky’s work in the 1950s and 1960s”.',
            '<b>Noam Chomsky</b> (geb. 1928) ist ein amerikanischer Sprachwissenschaftler am MIT. Seine Bücher <i>Syntactic Structures</i> (1957) und <i>Aspects of the Theory of Syntax</i> (1965) veränderten die Sprachwissenschaft. Deshalb steht im Arbeitsblatt „Chomsky’s work in the 1950s and 1960s“.')
        + p('Why “formalism”? Chomsky describes grammar like mathematics: with <b>formal rules</b> that generate all correct sentences of a language. The focus is on the <b>form</b> (the structure, especially syntax), not on how language is used.',
            'Warum „Formalismus“? Chomsky beschreibt Grammatik wie Mathematik: mit <b>formalen Regeln</b>, die alle korrekten Sätze einer Sprache erzeugen. Im Fokus steht die <b>Form</b> (die Struktur, vor allem Syntax), nicht der Sprachgebrauch.')
        + weiter('His central claim concerns how children learn their first language.', 'Seine zentrale These betrifft, wie Kinder ihre Erstsprache lernen.')
        + h3('The language acquisition device (LAD)', 'Der Spracherwerbsapparat (LAD)')
        + p('Every human is born with a <b>language acquisition device</b>. ' + eg('humans are genetically predisposed to learn language – the ability is in our biology.', 'Menschen sind genetisch dafür veranlagt, Sprache zu lernen – die Fähigkeit liegt in unserer Biologie.'),
            'Jeder Mensch wird mit einem <b>Spracherwerbsapparat</b> (language acquisition device) geboren. ' + eg('humans are genetically predisposed to learn language – the ability is in our biology.', 'Menschen sind genetisch dafür veranlagt, Sprache zu lernen – die Fähigkeit liegt in unserer Biologie.'))
        + cards([('Fast', 'Schnell', 'children master complex grammar in about 4–5 years', 'Kinder beherrschen komplexe Grammatik in etwa 4–5 Jahren'),
                 ('From little input', 'Aus wenig Input', 'they hear incomplete sentences and errors, yet learn the rules (“poverty of the stimulus”)', 'sie hören unvollständige Sätze und Fehler und lernen trotzdem die Regeln („poverty of the stimulus“)'),
                 ('Creative', 'Kreativ', 'they produce forms they never heard: “I goed”, “two mouses”', 'sie bilden Formen, die sie nie gehört haben: „I goed“, „two mouses“')])
        + weiter('What exactly is “built in”? Chomsky’s answer is Universal Grammar.', 'Was genau ist „eingebaut“? Chomskys Antwort ist die Universalgrammatik.')
        + h3('Universal Grammar (UG)', 'Universalgrammatik (UG)')
        + p('<b>Universal Grammar</b> consists of <b>syntactic structures and constraints</b> that are thought to be <b>universal</b> in human languages and thus <b>innate</b>. ' + eg('a basic grammar plan that all languages share and that every baby already has.', 'ein grundlegender Grammatikplan, den alle Sprachen teilen und den jedes Baby schon hat.'),
            'Die <b>Universalgrammatik</b> besteht aus <b>syntaktischen Strukturen und Beschränkungen</b>, die als <b>universell</b> in menschlichen Sprachen und damit als <b>angeboren</b> gelten. ' + eg('a basic grammar plan that all languages share and that every baby already has.', 'ein grundlegender Grammatikplan, den alle Sprachen teilen und den jedes Baby schon hat.'))
        + p('Example: all languages have nouns and verbs, and all build sentences from smaller phrases. A child only needs to find out which “settings” its language uses (e.g. verb before or after the object).',
            'Beispiel: Alle Sprachen haben Nomen und Verben, und alle bauen Sätze aus kleineren Phrasen. Ein Kind muss nur herausfinden, welche „Einstellungen“ seine Sprache nutzt (z. B. Verb vor oder nach dem Objekt).')
        + merkliste(('Gap text 2.2 – the three gaps', 'Lückentext 2.2 – die drei Lücken'), ('fill in exactly these words', 'genau diese Wörter einsetzen'),
                    [('“widely associated with <b>Chomsky’s</b> (Noam Chomsky’s) work in the 1950s and 1960s”', '„widely associated with <b>Chomsky’s</b> (Noam Chomsky’s) work in the 1950s and 1960s“'),
                     ('“born with a <b>language acquisition device (LAD)</b>”', '„born with a <b>language acquisition device (LAD)</b>“'),
                     ('“based on the theory of <b>Universal Grammar</b>”', '„based on the theory of <b>Universal Grammar</b>“')],
                    ('C – L – U: Chomsky gives every child a Language device with Universal rules.', 'C – L – U: Chomsky gibt jedem Kind einen Language device mit Universal-Regeln.'))
        + weiter('Chomsky also has his own version of Saussure’s langue/parole.', 'Chomsky hat auch eine eigene Version von Saussures langue/parole.')
        + h3('Competence and performance', 'Kompetenz und Performanz')
        + gegen(('competence', 'Kompetenz', 'the speaker’s unconscious knowledge of the grammar of their language (main interest of Chomsky)', 'das unbewusste Wissen des Sprechers über die Grammatik seiner Sprache (Hauptinteresse Chomskys)'),
                ('performance', 'Performanz', 'the actual use of language in real situations – with slips, pauses and errors', 'der tatsächliche Sprachgebrauch in echten Situationen – mit Versprechern, Pausen und Fehlern'))
        + p('Like Saussure with langue, Chomsky is mainly interested in the <b>system in the head</b>, not in real use. The difference: langue is <b>social</b> (shared by the community), competence is <b>individual and mental</b> (in each speaker’s mind).',
            'Wie Saussure bei der langue interessiert sich Chomsky vor allem für das <b>System im Kopf</b>, nicht für den echten Gebrauch. Der Unterschied: Langue ist <b>sozial</b> (von der Gemeinschaft geteilt), Kompetenz ist <b>individuell und geistig</b> (im Kopf jedes Sprechers).')
        + falle('Writing “Saussure” in 2.2. Saussure = structuralism (~1900); Chomsky = formalism (1950s/60s).', 'In 2.2 „Saussure“ schreiben. Saussure = Strukturalismus (~1900); Chomsky = Formalismus (1950er/60er).')
        + klausur_hinweis('The second gap needs the full term “language acquisition device” – the abbreviation LAD alone may not be enough.', 'Die zweite Lücke braucht den vollen Begriff „language acquisition device“ – die Abkürzung LAD allein reicht womöglich nicht.')
        + wahr('w-chomsky', [
            ('According to Chomsky, humans are genetically predisposed to learn language.', 'Laut Chomsky sind Menschen genetisch für das Sprachlernen veranlagt.', True, 'LAD = innate.', 'LAD = angeboren.'),
            ('Universal Grammar means that all languages have exactly the same grammar.', 'Universalgrammatik heißt: Alle Sprachen haben genau dieselbe Grammatik.', False, 'Only basic structures and constraints are shared.', 'Nur grundlegende Strukturen und Beschränkungen sind gemeinsam.'),
            ('Chomsky’s main work dates from the 1950s and 1960s.', 'Chomskys Hauptwerk stammt aus den 1950er und 1960er Jahren.', True, 'Syntactic Structures 1957, Aspects 1965.', 'Syntactic Structures 1957, Aspects 1965.'),
            ('Children learn language only by imitating their parents.', 'Kinder lernen Sprache nur durch Nachahmen ihrer Eltern.', False, '“I goed” shows they build rules themselves.', '„I goed“ zeigt: Sie bilden Regeln selbst.')]),
    merk=('Formalism (Chomsky, 1950s/60s): every human is born with a language acquisition device (LAD) = genetically predisposed to learn language; based on Universal Grammar = syntactic structures and constraints universal in human languages and thus innate.', 'Formalismus (Chomsky, 1950er/60er): Jeder Mensch hat einen angeborenen Spracherwerbsapparat (LAD) = genetische Veranlagung zum Sprachlernen; Grundlage: Universalgrammatik = syntaktische Strukturen und Beschränkungen, universell und angeboren.'),
    exam=('Gap text 2.2: Chomsky’s – language acquisition device (LAD) – Universal Grammar.', 'Lückentext 2.2: Chomsky’s – language acquisition device (LAD) – Universal Grammar.'),
    fehler=[('Writing Saussure or Jakobson instead of Chomsky.', 'Saussure oder Jakobson statt Chomsky schreiben.'),
            ('“Universal Grammar = all languages are the same”.', '„Universalgrammatik = alle Sprachen sind gleich“.')],
    src='Worksheet 2.2')

# ---------------------------------------------------------------- 4 Formalism: Jakobson, disciplines
fig_jak = svg(360, 236,
    T(180, 16, 'Roman Jakobson (1896–1982)', 'Roman Jakobson (1896–1982)', 13, 800)
    + box(4, 34, 168, 54, 'Moscow Linguistic\nCircle (1915)', 'Moskauer Linguistik-\nkreis (1915)', tip=('Russian Formalism: Jakobson and others studied the FORM of language and literature – sounds, structure, devices.', 'Russischer Formalismus: Jakobson und andere untersuchten die FORM von Sprache und Literatur – Laute, Aufbau, Stilmittel.'))
    + pfeil(172, 61, 186, 61)
    + box(188, 34, 168, 54, 'Prague Linguistic\nCircle (1926)', 'Prager Linguistik-\nkreis (1926)', tip=('In Prague, Jakobson and Trubetzkoy applied these ideas to linguistics – the 1920s work the worksheet refers to.', 'In Prag übertrugen Jakobson und Trubetzkoy diese Ideen auf die Sprachwissenschaft – die Arbeit der 1920er, auf die sich das Arbeitsblatt bezieht.'))
    + T(180, 108, 'heavily influenced:', 'stark beeinflusst:', 12, 700)
    + box(4, 120, 112, 58, '1. phonology\n(sound system)', '1. Phonologie\n(Lautsystem)', tip=('Phonology: phonemes and distinctive features (e.g. voiced/voiceless: /b/ vs /p/). Jakobson’s most important contribution.', 'Phonologie: Phoneme und distinktive Merkmale (z. B. stimmhaft/stimmlos: /b/ vs /p/). Jakobsons wichtigster Beitrag.'), art='hl')
    + box(124, 120, 112, 58, '2. morphology\n(word structure)', '2. Morphologie\n(Wortbau)', tip=('Morphology: how words are built from meaningful parts (walk-ed, un-happy).', 'Morphologie: wie Wörter aus bedeutungstragenden Teilen gebaut sind (walk-ed, un-happy).'))
    + box(244, 120, 112, 58, '3. syntax\n(sentence\nstructure)', '3. Syntax\n(Satzbau)', tip=('Syntax: how words are combined into sentences.', 'Syntax: wie Wörter zu Sätzen verbunden werden.'))
    + T(180, 204, 'also: semantics, stylistics / poetics', 'außerdem: Semantik, Stilistik / Poetik', 12, 600)
    + T(180, 224, 'Formalism → focus on form and structure', 'Formalismus → Fokus auf Form und Struktur', 12, 700),
    'Jakobson and the disciplines influenced by formalism', maxw=420)

t_jak = thema('formalism-jakobson', ('Formalism: Roman Jakobson (1920s)', 'Formalismus: Roman Jakobson (1920er)'), star=True,
    kern=('An earlier form of formalism goes back to Roman Jakobson in the 1920s (Russian Formalism, Moscow and Prague Linguistic Circles). It studies language by its form and structure and heavily influenced three linguistic disciplines: phonology, morphology and syntax (also semantics and stylistics/poetics).',
          'Eine frühere Form des Formalismus geht auf Roman Jakobson in den 1920er Jahren zurück (Russischer Formalismus, Moskauer und Prager Linguistikkreis). Er untersucht Sprache nach ihrer Form und Struktur und beeinflusste drei sprachwissenschaftliche Disziplinen stark: Phonologie, Morphologie und Syntax (außerdem Semantik und Stilistik/Poetik).'),
    kurz=('<p>Why are <i>pat</i> and <i>bat</i> two different words? Only one feature changes: with /b/ your vocal cords vibrate, with /p/ they do not. <b>Roman Jakobson</b>, a Russian linguist, made exactly such small <b>formal differences</b> the centre of his work in the 1920s.</p><p>He belonged to <b>Russian Formalism</b> (Moscow) and later founded the <b>Prague Linguistic Circle</b>. Formalists look at the <b>form</b> of language – its sounds and structures – not at the speaker’s intentions.</p><p>For the exam you need three disciplines that formalism heavily influenced. The safest answer: <b>phonology</b> (sound system), <b>morphology</b> (word structure) and <b>syntax</b> (sentence structure).</p>',
          '<p>Warum sind <i>pat</i> und <i>bat</i> zwei verschiedene Wörter? Nur ein Merkmal ändert sich: Bei /b/ schwingen die Stimmbänder, bei /p/ nicht. <b>Roman Jakobson</b>, ein russischer Sprachwissenschaftler, machte genau solche kleinen <b>formalen Unterschiede</b> in den 1920er Jahren zum Mittelpunkt seiner Arbeit.</p><p>Er gehörte zum <b>Russischen Formalismus</b> (Moskau) und gründete später den <b>Prager Linguistikkreis</b> mit. Formalisten betrachten die <b>Form</b> der Sprache – ihre Laute und Strukturen – nicht die Absichten des Sprechers.</p><p>Für die Klausur brauchst du drei Disziplinen, die der Formalismus stark beeinflusst hat. Die sicherste Antwort: <b>Phonologie</b> (Lautsystem), <b>Morphologie</b> (Wortbau) und <b>Syntax</b> (Satzbau).</p>'),
    fig=fw('Jakobson’s path and the three disciplines from task 2.3. Tap the boxes.', 'Jakobsons Weg und die drei Disziplinen aus Aufgabe 2.3. Tippe auf die Kästen.') + bild(fig_jak),
    figcap=('after the worksheet, task 2.3', 'nach dem Arbeitsblatt, Aufgabe 2.3'),
    article=h3('Roman Jakobson and Russian Formalism', 'Roman Jakobson und der Russische Formalismus')
        + p('<b>Roman Jakobson</b> (1896–1982) was born in Moscow. In 1915 he co-founded the <b>Moscow Linguistic Circle</b>, a centre of <b>Russian Formalism</b>. In 1920 he moved to Czechoslovakia and in 1926 helped found the <b>Prague Linguistic Circle</b> with Nikolai Trubetzkoy. Later he taught at Harvard and MIT – and influenced Chomsky.',
            '<b>Roman Jakobson</b> (1896–1982) wurde in Moskau geboren. 1915 gründete er den <b>Moskauer Linguistikkreis</b> mit, ein Zentrum des <b>Russischen Formalismus</b>. 1920 zog er in die Tschechoslowakei und gründete 1926 mit Nikolai Trubetzkoy den <b>Prager Linguistikkreis</b>. Später lehrte er in Harvard und am MIT – und beeinflusste Chomsky.')
        + p('Formalists analyse language (and literature) by its <b>form</b>: sounds, patterns, structures. ' + eg('look at HOW language is built, not at what the speaker wants.', 'ansehen, WIE Sprache gebaut ist, nicht, was der Sprecher will.'),
            'Formalisten analysieren Sprache (und Literatur) nach ihrer <b>Form</b>: Laute, Muster, Strukturen. ' + eg('look at HOW language is built, not at what the speaker wants.', 'ansehen, WIE Sprache gebaut ist, nicht, was der Sprecher will.'))
        + weiter('The exam asks which linguistic disciplines this way of thinking shaped.', 'Die Klausur fragt, welche sprachwissenschaftlichen Disziplinen diese Denkweise geprägt hat.')
        + h3('Three disciplines formalism heavily influenced', 'Drei Disziplinen, die der Formalismus stark beeinflusst hat')
        + tabelle([('Discipline', 'Disziplin'), ('Studies …', 'Untersucht …'), ('Example', 'Beispiel')], [
            [('<b>phonology</b>', '<b>Phonologie</b>'), ('the sound system: which sounds distinguish meaning (phonemes, distinctive features)', 'das Lautsystem: welche Laute Bedeutung unterscheiden (Phoneme, distinktive Merkmale)'), ('/p/ vs /b/: <i>pat</i> – <i>bat</i>', '/p/ vs /b/: <i>pat</i> – <i>bat</i>')],
            [('<b>morphology</b>', '<b>Morphologie</b>'), ('the structure of words: smallest meaningful units (morphemes)', 'den Bau der Wörter: kleinste bedeutungstragende Einheiten (Morpheme)'), ('<i>un-friend-ly</i>', '<i>un-friend-ly</i>')],
            [('<b>syntax</b>', '<b>Syntax</b>'), ('the structure of sentences: how words combine', 'den Bau der Sätze: wie Wörter sich verbinden'), ('<i>The frog sees the fly.</i> ≠ <i>The fly sees the frog.</i>', '<i>The frog sees the fly.</i> ≠ <i>The fly sees the frog.</i>')]])
        + p('Jakobson’s biggest contribution was in <b>phonology</b>: with Trubetzkoy he founded modern phonology and developed the theory of <b>distinctive features</b>. He then applied the same ideas to morphology and syntax.',
            'Jakobsons größter Beitrag lag in der <b>Phonologie</b>: Mit Trubetzkoy begründete er die moderne Phonologie und entwickelte die Theorie der <b>distinktiven Merkmale</b>. Danach übertrug er dieselben Ideen auf Morphologie und Syntax.')
        + zusatz('Formalism also shaped semantics (meaning) and, outside linguistics in the narrow sense, stylistics and poetics (the analysis of literary language). Should your lecture name these, they also count as answers.', 'Der Formalismus prägte auch die Semantik (Bedeutung) und, außerhalb der Sprachwissenschaft im engeren Sinn, Stilistik und Poetik (Analyse literarischer Sprache). Nennt deine Vorlesung diese, zählen sie ebenfalls.')
        + merkliste(('Task 2.3 – name three disciplines', 'Aufgabe 2.3 – drei Disziplinen nennen'), ('from small to big', 'vom Kleinen zum Großen'),
                    [('<b>phonology</b> – sounds', '<b>phonology</b> – Laute'), ('<b>morphology</b> – words', '<b>morphology</b> – Wörter'), ('<b>syntax</b> – sentences', '<b>syntax</b> – Sätze')],
                    ('P – M – S: sound → word → sentence, the building blocks get bigger.', 'P – M – S: Laut → Wort → Satz, die Bausteine werden größer.'))
        + falle('Naming “applied linguistics” or “sociolinguistics”. These are not shaped by formalism – formalism looks at form, not at use or society.', '„Angewandte Linguistik“ oder „Soziolinguistik“ nennen. Die sind nicht vom Formalismus geprägt – er betrachtet Form, nicht Gebrauch oder Gesellschaft.')
        + klausur_hinweis('Write the disciplines in English: phonology, morphology, syntax. One word each is enough.', 'Die Disziplinen auf Englisch schreiben: phonology, morphology, syntax. Je ein Wort genügt.')
        + wahr('w-jak', [
            ('Jakobson’s formalist work dates from the 1920s.', 'Jakobsons formalistische Arbeit stammt aus den 1920ern.', True, 'Moscow, then Prague (1926).', 'Moskau, dann Prag (1926).'),
            ('Phonology studies how sentences are built.', 'Phonologie untersucht, wie Sätze gebaut sind.', False, 'Phonology = sound system; sentences = syntax.', 'Phonologie = Lautsystem; Sätze = Syntax.'),
            ('Morphology studies the structure of words.', 'Morphologie untersucht den Bau von Wörtern.', True, 'e.g. un-friend-ly.', 'z. B. un-friend-ly.'),
            ('Jakobson founded the Language Acquisition Device theory.', 'Jakobson begründete die Theorie des Spracherwerbsapparats.', False, 'That was Chomsky.', 'Das war Chomsky.')]),
    merk=('Formalism (Roman Jakobson, 1920s; Moscow → Prague Linguistic Circle): focus on form and structure; heavily influenced phonology, morphology and syntax (also semantics, stylistics/poetics).', 'Formalismus (Roman Jakobson, 1920er; Moskau → Prager Linguistikkreis): Fokus auf Form und Struktur; prägte stark Phonologie, Morphologie und Syntax (außerdem Semantik, Stilistik/Poetik).'),
    exam=('Task 2.3: name three disciplines – phonology, morphology, syntax.', 'Aufgabe 2.3: drei Disziplinen nennen – phonology, morphology, syntax.'),
    fehler=[('Naming applied linguistics or sociolinguistics.', 'Angewandte Linguistik oder Soziolinguistik nennen.'),
            ('Confusing phonology (sound system) and syntax (sentences).', 'Phonologie (Lautsystem) und Syntax (Sätze) verwechseln.')],
    src='Worksheet 2.3')

# ---------------------------------------------------------------- 5 Overview: the schools on a timeline
fig_zeit = svg(360, 220,
    T(180, 16, 'Schools of thought on a timeline', 'Denkschulen auf einem Zeitstrahl', 13, 800)
    + f'<line x1="20" y1="110" x2="345" y2="110" style="stroke:var(--axis2)" stroke-width="2"/>' + pfeil(20, 110, 350, 110)
    + ''.join(f'<circle cx="{x}" cy="110" r="6" style="fill:var(--primary)"/>' + T(x, 134, j, j, 12, 800) for x, j in ((60, '~1900'), (175, '1920s'), (290, '1950s/60s')))
    + box(4, 30, 112, 62, 'Structuralism\nSaussure\nlangue / parole', 'Strukturalismus\nSaussure\nlangue / parole', tip=('Language as a system of signs (langue); signifié + signifiant.', 'Sprache als Zeichensystem (langue); signifié + signifiant.'))
    + box(124, 148, 112, 62, 'Formalism\nJakobson\nphonology …', 'Formalismus\nJakobson\nPhonologie …', tip=('Russian Formalism / Prague Circle: form and structure; phonology, morphology, syntax.', 'Russischer Formalismus / Prager Kreis: Form und Struktur; Phonologie, Morphologie, Syntax.'))
    + box(244, 30, 112, 62, 'Formalism\nChomsky\nLAD, UG', 'Formalismus\nChomsky\nLAD, UG', tip=('Innate language acquisition device and Universal Grammar.', 'Angeborener Spracherwerbsapparat und Universalgrammatik.'), art='hl'),
    'Timeline of structuralism and formalism', maxw=420)

t_ueber = thema('schools-overview', ('Overview: who, when, what?', 'Überblick: wer, wann, was?'),
    kern=('Three names, three key ideas: Saussure (~1900, structuralism: langue/parole, the sign), Jakobson (1920s, formalism: phonology, morphology, syntax), Chomsky (1950s/60s, formalism: LAD, Universal Grammar). All three focus on the language system and its form rather than on how people use language.',
          'Drei Namen, drei Kernideen: Saussure (~1900, Strukturalismus: langue/parole, das Zeichen), Jakobson (1920er, Formalismus: Phonologie, Morphologie, Syntax), Chomsky (1950er/60er, Formalismus: LAD, Universalgrammatik). Alle drei konzentrieren sich auf das Sprachsystem und seine Form, weniger darauf, wie Menschen Sprache gebrauchen.'),
    kurz=('<p>In the exam, the most common mistake is mixing up the names. So here is everything on one page.</p><p><b>Saussure</b> comes first (around 1900): language is a system of signs, <b>langue</b> vs. <b>parole</b>, <b>signifié</b> and <b>signifiant</b>. <b>Jakobson</b> follows in the 1920s: formalism, focus on form, influence on <b>phonology, morphology, syntax</b>. <b>Chomsky</b> comes last (1950s/60s): every human has an innate <b>language acquisition device</b> based on <b>Universal Grammar</b>.</p><p>What connects them: all three study the <b>system</b> behind language – not single conversations.</p>',
          '<p>In der Klausur ist der häufigste Fehler, die Namen zu verwechseln. Deshalb hier alles auf einer Seite.</p><p><b>Saussure</b> kommt zuerst (um 1900): Sprache ist ein Zeichensystem, <b>langue</b> vs. <b>parole</b>, <b>signifié</b> und <b>signifiant</b>. <b>Jakobson</b> folgt in den 1920ern: Formalismus, Fokus auf Form, Einfluss auf <b>Phonologie, Morphologie, Syntax</b>. <b>Chomsky</b> kommt zuletzt (1950er/60er): Jeder Mensch hat einen angeborenen <b>Spracherwerbsapparat</b>, der auf der <b>Universalgrammatik</b> beruht.</p><p>Was sie verbindet: Alle drei erforschen das <b>System</b> hinter der Sprache – nicht einzelne Gespräche.</p>'),
    fig=fw('Three names on one timeline. Tap the boxes.', 'Drei Namen auf einem Zeitstrahl. Tippe auf die Kästen.') + bild(fig_zeit),
    figcap=('summary of worksheet task 2', 'Zusammenfassung von Arbeitsblatt Aufgabe 2'),
    article=h3('Everything in one table', 'Alles in einer Tabelle')
        + tabelle([('School', 'Schule'), ('Who / when', 'Wer / wann'), ('Key terms', 'Schlüsselbegriffe')], [
            [('Structuralism', 'Strukturalismus'), ('Ferdinand de Saussure, ~1900 (Cours 1916)', 'Ferdinand de Saussure, ~1900 (Cours 1916)'), ('langue, parole, signifié, signifiant, arbitrary sign', 'langue, parole, signifié, signifiant, arbiträres Zeichen')],
            [('Formalism (early)', 'Formalismus (früh)'), ('Roman Jakobson, 1920s (Moscow, Prague)', 'Roman Jakobson, 1920er (Moskau, Prag)'), ('form, phonology, morphology, syntax, distinctive features', 'Form, Phonologie, Morphologie, Syntax, distinktive Merkmale')],
            [('Formalism (generative)', 'Formalismus (generativ)'), ('Noam Chomsky, 1950s/60s', 'Noam Chomsky, 1950er/60er'), ('language acquisition device (LAD), Universal Grammar, innate, competence/performance', 'Spracherwerbsapparat (LAD), Universalgrammatik, angeboren, Kompetenz/Performanz')]])
        + weiter('Two pairs of terms look alike – here is how they differ.', 'Zwei Begriffspaare sehen ähnlich aus – so unterscheiden sie sich.')
        + h3('Langue/parole vs. competence/performance', 'Langue/parole vs. Kompetenz/Performanz')
        + tabelle([('', ''), ('Saussure', 'Saussure'), ('Chomsky', 'Chomsky')], [
            [('the system', 'das System'), ('langue – social, shared by the community', 'langue – sozial, von der Gemeinschaft geteilt'), ('competence – mental, in each speaker’s head', 'Kompetenz – geistig, im Kopf jedes Sprechers')],
            [('the use', 'der Gebrauch'), ('parole – concrete individual usage', 'parole – konkreter individueller Gebrauch'), ('performance – actual use with errors', 'Performanz – tatsächlicher Gebrauch mit Fehlern')]])
        + weiter('Test yourself: which name belongs to which idea?', 'Teste dich: Welcher Name gehört zu welcher Idee?')
        + spiel('sp-schulen', ('Saussure, Jakobson or Chomsky?', 'Saussure, Jakobson oder Chomsky?'), [('Saussure', 'Saussure'), ('Jakobson', 'Jakobson'), ('Chomsky', 'Chomsky')], [
            ('langue and parole', 'langue und parole', 0, 'Structuralism, ~1900.', 'Strukturalismus, ~1900.'),
            ('language acquisition device', 'Spracherwerbsapparat', 2, 'Innate ability, 1950s/60s.', 'Angeborene Fähigkeit, 1950er/60er.'),
            ('Prague Linguistic Circle', 'Prager Linguistikkreis', 1, 'Founded 1926.', 'Gegründet 1926.'),
            ('signifié and signifiant', 'signifié und signifiant', 0, 'The two sides of the sign.', 'Die zwei Seiten des Zeichens.'),
            ('Universal Grammar', 'Universalgrammatik', 2, 'Innate syntactic structures.', 'Angeborene syntaktische Strukturen.'),
            ('distinctive features in phonology', 'distinktive Merkmale in der Phonologie', 1, 'e.g. voiced vs. voiceless.', 'z. B. stimmhaft vs. stimmlos.'),
            ('Course in General Linguistics (1916)', 'Cours de linguistique générale (1916)', 0, 'Published by his students.', 'Von seinen Studenten veröffentlicht.'),
            ('“humans are genetically predisposed to learn language”', '„Menschen sind genetisch zum Sprachlernen veranlagt“', 2, 'The LAD idea.', 'Die LAD-Idee.')])
        + zusatz('The counter-movement is <b>functionalism</b>: it explains language by its use and communicative functions (see form vs. function). It is not part of the worksheet.', 'Die Gegenbewegung ist der <b>Funktionalismus</b>: Er erklärt Sprache über ihren Gebrauch und ihre kommunikativen Funktionen (siehe Form vs. Funktion). Er ist nicht Teil des Arbeitsblatts.')
        + klausur_hinweis('Learn the order: Saussure (~1900) → Jakobson (1920s) → Chomsky (1950s/60s). Dates in the gap text help you pick the right name.', 'Lerne die Reihenfolge: Saussure (~1900) → Jakobson (1920er) → Chomsky (1950er/60er). Die Jahreszahlen im Lückentext helfen dir, den richtigen Namen zu wählen.'),
    merk=('Saussure (~1900, structuralism: langue/parole, sign) → Jakobson (1920s, formalism: phonology, morphology, syntax) → Chomsky (1950s/60s, formalism: LAD, Universal Grammar).', 'Saussure (~1900, Strukturalismus: langue/parole, Zeichen) → Jakobson (1920er, Formalismus: Phonologie, Morphologie, Syntax) → Chomsky (1950er/60er, Formalismus: LAD, Universalgrammatik).'),
    exam=('Assign names, dates and key terms correctly in the gap texts of task 2.', 'Namen, Jahreszahlen und Schlüsselbegriffe in den Lückentexten von Aufgabe 2 richtig zuordnen.'),
    fehler=[('Mixing up Saussure and Chomsky.', 'Saussure und Chomsky verwechseln.'),
            ('Equating langue with competence (social vs. mental).', 'Langue mit Kompetenz gleichsetzen (sozial vs. geistig).')],
    src='Worksheet 2')

KAPITEL = kapitel('k2', ('Schools of Thought in Linguistics', 'Denkschulen der Sprachwissenschaft'),
    ('Structuralism (Saussure: langue, parole and the linguistic sign) and formalism (Chomsky: language acquisition device and Universal Grammar; Jakobson: phonology, morphology, syntax). In the exam: gap texts, a labelled figure and a list. Running example: the frog /frɒg/ from the worksheet.',
     'Strukturalismus (Saussure: langue, parole und das sprachliche Zeichen) und Formalismus (Chomsky: Spracherwerbsapparat und Universalgrammatik; Jakobson: Phonologie, Morphologie, Syntax). In der Klausur: Lückentexte, ein beschriftetes Schaubild und eine Aufzählung. Durchgehendes Beispiel: der Frosch /frɒg/ vom Arbeitsblatt.'),
    ['Structuralism', 'Sign', 'Chomsky', 'Jakobson', 'Overview'], [t_struk, t_zeichen, t_chomsky, t_jak, t_ueber])
