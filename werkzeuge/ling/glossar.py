"""Erzeugt inhalte/ling/glossar.json. Aufruf: python3 werkzeuge/ling/glossar.py"""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
G = [
    ('Dichotomy', '[Dd]ichotom(?:y|ies)', 'dichotomies', 'Dichotomy (Dichotomie): a pair of opposite but complementary perspectives on language.'),
    ('Synchronic', '[Ss]ynchronic', 'synchronic-diachronic', 'Synchronic (synchron): studying language at one specific point in time.'),
    ('Diachronic', '[Dd]iachronic', 'synchronic-diachronic', 'Diachronic (diachron): studying language change through time; also historical linguistics.'),
    ('Form', '\\b[Ff]orm\\b', 'form-function', 'Form (Form): the structure of language – sounds, word forms, sentence patterns.'),
    ('Function', '\\b[Ff]unction\\b', 'form-function', 'Function (Funktion): what a form is used for in communication; its purpose.'),
    ('Applied linguistics', '[Aa]pplied linguistics', 'applied-theoretical', 'Applied linguistics (angewandte Sprachwissenschaft): uses linguistic findings to solve real-life problems such as language teaching, translation or speech therapy.'),
    ('Theoretical linguistics', '[Tt]heoretical(?: linguistics)?', 'applied-theoretical', 'Theoretical linguistics (theoretische Sprachwissenschaft): studies language for its own sake to describe and explain the language system.'),
    ('Structuralism', '[Ss]tructuralism', 'structuralism', 'Structuralism (Strukturalismus): school of thought going back to Ferdinand de Saussure (~1900); language as a system of signs.'),
    ('Langue', '\\blangue\\b', 'structuralism', 'Langue: the abstract language system shared by all members of a speech community (Saussure).'),
    ('Parole', '\\bparole\\b', 'structuralism', 'Parole: the concrete usage of language by the individual (Saussure).'),
    ('Speech community', '[Ss]peech community', 'structuralism', 'Speech community (Sprachgemeinschaft): all people who share the same language system.'),
    ('Signifié', 'signifié', 'linguistic-sign', 'Signifié / signified (das Bezeichnete): the concept or mental idea of a sign.'),
    ('Signifiant', 'signifiant', 'linguistic-sign', 'Signifiant / signifier (das Bezeichnende): the sound image of a sign, e.g. /frɒg/.'),
    ('Arbitrary', '[Aa]rbitrar(?:y|iness)', 'linguistic-sign', 'Arbitrary (arbiträr): there is no natural link between the sound image and the concept; it is a convention.'),
    ('Formalism', '[Ff]ormalism', 'formalism-chomsky', 'Formalism (Formalismus): studies language by its form and structure; Jakobson (1920s), Chomsky (1950s/60s).'),
    ('Language acquisition device', '[Ll]anguage acquisition device|LAD', 'formalism-chomsky', 'Language acquisition device, LAD (Spracherwerbsapparat): innate ability to learn language every human is born with (Chomsky).'),
    ('Universal Grammar', '[Uu]niversal [Gg]rammar', 'formalism-chomsky', 'Universal Grammar (Universalgrammatik): syntactic structures and constraints thought to be universal in human languages and thus innate.'),
    ('Innate', '\\binnate\\b', 'formalism-chomsky', 'Innate (angeboren): present from birth.'),
    ('Competence', '\\b[Cc]ompetence\\b', 'formalism-chomsky', 'Competence (Kompetenz): a speaker’s unconscious knowledge of the grammar of their language (Chomsky).'),
    ('Performance', '\\b[Pp]erformance\\b', 'formalism-chomsky', 'Performance (Performanz): the actual use of language in real situations (Chomsky).'),
    ('Phonology', '[Pp]honology', 'formalism-jakobson', 'Phonology (Phonologie): the study of the sound system of a language – which sounds distinguish meaning.'),
    ('Morphology', '[Mm]orphology', 'formalism-jakobson', 'Morphology (Morphologie): the study of the structure of words.'),
    ('Syntax', '\\b[Ss]yntax\\b', 'formalism-jakobson', 'Syntax (Syntax): the study of the structure of sentences.'),
    ('Distinctive features', '[Dd]istinctive features?', 'formalism-jakobson', 'Distinctive features (distinktive Merkmale): properties that distinguish sounds, e.g. voiced vs. voiceless (Jakobson).'),
    ('Prague Linguistic Circle', 'Prague Linguistic Circle', 'formalism-jakobson', 'Prague Linguistic Circle (Prager Linguistikkreis): group founded in 1926 by Jakobson, Trubetzkoy and others.'),
]
ids = {t['id'] for k in json.loads((ROOT / 'inhalte/ling/fach.json').read_text())['kapitel'] for t in k['themen']}
for b, m, h, t in G:
    assert h in ids, (b, h)
out = {'begriffe': [{'begriff': b, 'muster': m, 'heimat': h, 'text': t} for b, m, h, t in G], 'nicht_markieren': ['language', 'linguistics', 'school of thought']}
(ROOT / 'inhalte/ling/glossar.json').write_text(json.dumps(out, ensure_ascii=False, indent=1))
print(f'ling: {len(G)} Glossarbegriffe')
