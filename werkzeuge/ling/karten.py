"""Erzeugt inhalte/ling/karten.json (Glossar und Merksätze kommen in der App automatisch dazu). Aufruf: python3 werkzeuge/ling/karten.py"""
import json, pathlib
from collections import Counter
ROOT = pathlib.Path(__file__).resolve().parents[2]
K = {
'dichotomies': [('Dichotomy – definition', 'a pair of opposite but complementary perspectives on the same object (language)'),
    ('The three dichotomies of the worksheet', 'synchronic / diachronic · form / function · theoretical / applied'),
    ('True/false task – what to do if false', 'tick b and write a full correct sentence defining BOTH terms'),
    ('Other dichotomies', 'langue / parole (Saussure) · competence / performance (Chomsky) · descriptive / prescriptive')],
'synchronic-diachronic': [('Synchronic', 'language at ONE specific point in time – a snapshot (e.g. English today, Old English around 1000)'),
    ('Diachronic', 'language CHANGE through time – a film (also: historical linguistics)'),
    ('Worksheet 1.1 – true or false?', 'TRUE: synchronic = specific point in time, diachronic = language change through time'),
    ('“nice” – a diachronic example', '“foolish” (~1300) → “precise, fussy” (~1600) → “pleasant, kind” (today)'),
    ('Is a study of Old English synchronic or diachronic?', 'synchronic, if it describes one point in time – old ≠ diachronic'),
    ('Saussure’s chess comparison', 'position on the board = synchronic; sequence of moves = diachronic')],
'form-function': [('Form', 'the structure of language: sounds, word forms, sentence patterns – HOW something is said'),
    ('Function', 'what a form is used for in communication – its purpose (WHAT FOR it is said)'),
    ('Worksheet 1.2 – true or false?', 'FALSE: form = structure of language, function = its purpose/use in communication (not basic messages vs. mastery)'),
    ('“Can you open the window?”', 'form: question (interrogative) · function: request'),
    ('One form – many functions?', 'yes: a question can be a request, a real question or a complaint'),
    ('One function – many forms?', 'yes: a request as imperative, question or statement (“It’s hot in here.”)')],
'applied-theoretical': [('Theoretical (“not applied”) linguistics', 'studies language for its own sake: describes and explains how the system works'),
    ('Applied linguistics', 'uses linguistic findings to solve practical, real-life problems'),
    ('Worksheet 1.3 – true or false?', 'FALSE: the difference is the goal (understand vs. solve problems), not past vs. present'),
    ('Fields of applied linguistics', 'language teaching · translation · speech therapy · forensic linguistics · lexicography')],
'structuralism': [('Founder of structuralism', 'Ferdinand de Saussure (~1900), Course in General Linguistics 1916'),
    ('Langue', 'the abstract language system shared by all members of a speech community'),
    ('Parole', 'the concrete usage of language by the individual'),
    ('Main interest of structuralism', 'langue (the system) – less so parole'),
    ('Gap text 2.1 – the three answers', 'Saussure · langue · parole'),
    ('Language as a system of differences', 'a sign gets its value from its differences to other signs (cat ≠ bat ≠ hat)')],
'linguistic-sign': [('Signifié (signified)', 'the concept / mental idea – that which is signified'),
    ('Signifiant (signifier)', 'the sound image, e.g. /frɒg/ – that which signifies'),
    ('Arbitrariness of the sign', 'no natural link between sound and concept: frog / Frosch / grenouille'),
    ('Is the signifié the real frog?', 'no – the real object is the referent; the signifié is the concept'),
    ('Sheet-of-paper comparison', 'signifié and signifiant are inseparable, like two sides of a sheet of paper')],
'formalism-chomsky': [('Formalism (Chomsky) – when?', '1950s and 1960s (Syntactic Structures 1957, Aspects 1965)'),
    ('Language acquisition device (LAD)', 'innate ability every human is born with – humans are genetically predisposed to learn language'),
    ('Universal Grammar', 'syntactic structures and constraints thought to be universal in human languages and thus innate'),
    ('Gap text 2.2 – the three answers', 'Chomsky’s · language acquisition device (LAD) · Universal Grammar'),
    ('Competence vs. performance', 'competence = unconscious knowledge of grammar; performance = actual use (with errors)'),
    ('Evidence for the LAD', 'children learn fast from limited input and create new forms (“I goed”)')],
'formalism-jakobson': [('Formalism (Jakobson) – when and where?', '1920s; Moscow Linguistic Circle → Prague Linguistic Circle (1926)'),
    ('Three disciplines formalism heavily influenced', 'phonology · morphology · syntax'),
    ('Phonology', 'the sound system: which sounds distinguish meaning (/p/ vs /b/)'),
    ('Morphology', 'the structure of words (un-friend-ly)'),
    ('Syntax', 'the structure of sentences'),
    ('Jakobson’s key contribution', 'distinctive features in phonology (with Trubetzkoy)')],
'schools-overview': [('Order of the three linguists', 'Saussure (~1900) → Jakobson (1920s) → Chomsky (1950s/60s)'),
    ('Structuralism vs. formalism', 'structuralism: Saussure, langue/parole, sign · formalism: Jakobson and Chomsky, form, LAD, Universal Grammar'),
    ('Langue vs. competence', 'langue = social, shared by the community · competence = mental, in each speaker’s head'),
    ('What connects the three schools?', 'all study the language system and its form rather than single conversations')],
}
fach = json.loads((ROOT / 'inhalte/ling/fach.json').read_text())
ids = [t['id'] for k in fach['kapitel'] for t in k['themen']]
assert set(K) == set(ids), (set(ids) - set(K), set(K) - set(ids))
karten = [{'t': t, 'v': v, 'r': r} for t in ids for v, r in K[t]]
vs = [k['v'] for k in karten]; assert len(vs) == len(set(vs)), [v for v in vs if vs.count(v) > 1]
(ROOT / 'inhalte/ling/karten.json').write_text('{\n "karten": [\n' + ',\n'.join('  ' + json.dumps(x, ensure_ascii=False) for x in karten) + '\n ]\n}\n')
print(f'ling: {len(karten)} Karten')
