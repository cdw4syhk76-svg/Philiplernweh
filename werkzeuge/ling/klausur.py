"""Erzeugt inhalte/ling/klausur.json: Probeklausur im Aufbau des Arbeitsblatts (Key Concepts in Linguistics).
1 Dichotomies (Richtig/Falsch + Korrektur) · 2.1 Strukturalismus (Lücken + Zeichen) · 2.2 Formalismus Chomsky (Lücken) · 2.3 Jakobson (Aufzählen).
Aufruf: python3 werkzeuge/ling/klausur.py"""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
IN = ROOT / 'inhalte' / 'ling'


def T(label, p, z=3): return dict(typ='text', label=label, p=p, zeilen=z)
def W(label, loesung, p=1): return dict(typ='wort', label=label, loesung=loesung, p=p)
def V(id, unter, text, felder, loesung): return dict(id=id, unter=unter, text=text, felder=felder, loesung=loesung)
def UL(*x): return '<ul>' + ''.join(f'<li>{i}</li>' for i in x) + '</ul>'


KORR = {
 'ff': 'Form refers to the structure of language (sounds, word forms, sentence patterns); function refers to what a form is used for in communication (its purpose).',
 'at': 'Applied linguistics uses linguistic findings to solve practical, real-life problems (e.g. language teaching, translation, speech therapy); not applied (theoretical) linguistics studies language for its own sake to describe and explain it.',
 'sd': 'Synchronic describes language at one specific point in time; diachronic describes language change through time.',
}
# je Variante 3 Aussagen (Text, richtig, Korrektur-Schlüssel)
RF = [
 [('The term synchronic describes a specific point in time, while diachronic describes language change through time.', True, None),
  ('Function denotes a speaker’s ability to only be able to convey basic messages, while form denotes a mastery over the language.', False, 'ff'),
  ('Applied linguistics refers to studies that still have real-life applications, ‘not applied’ refers to studies in the past that are not in use anymore.', False, 'at')],
 [('Diachronic linguistics describes a language at one specific point in time, while synchronic linguistics studies how it changes.', False, 'sd'),
  ('Form refers to the structure of language, while function refers to what this structure is used for in communication.', True, None),
  ('Theoretical linguistics studies language for its own sake, while applied linguistics uses its findings to solve real-life problems.', True, None)],
 [('A description of Old English grammar around the year 1000 is diachronic because Old English is no longer spoken.', False, 'sd'),
  ('Form describes how fluently a speaker can use a language, function describes how many words he knows.', False, 'ff'),
  ('Speech therapy and language teaching are examples of applied linguistics.', True, None)],
 [('Synchronic linguistics studies language at one specific point in time.', True, None),
  ('One linguistic form, e.g. a question, can have several functions, e.g. a request or a complaint.', True, None),
  ('‘Not applied’ linguistics refers to old theories that nobody uses anymore.', False, 'at')],
]
a1 = []
for k, aus in enumerate(RF):
    falsch = [s for s, r, key in aus if not r]
    p_korr = 3
    loes = '<br>'.join(f"<b>{k2 + 1}.</b> {'TRUE' if r else 'FALSE'}" + (f' – correct answer: <i>{KORR[key]}</i>' if key else '') for k2, (s, r, key) in enumerate(aus))
    a1.append(V(f'rf-{k + 1}', ['synchronic-diachronic', 'form-function', 'applied-theoretical', 'dichotomies'][k], '<p>Decide: true or false? If false, write the correct answer below.</p>',
                [dict(typ='rf', aussagen=[[s, r] for s, r, _ in aus], p=3, einzeln=True), T('Correct answer(s) for every false statement', p_korr, 4)], loes))
A1 = dict(titel='Dichotomies – true or false?', punkte=6, intro='Tick true or false. For every false statement write the correct answer.', teile=[dict(punkte=6, varianten=a1)])

# 2.1 Structuralism: gap text + sign (5 P)
SAUS = ['Ferdinand de Saussure', 'Saussure', 'de Saussure']
G21 = [
 ('gap-struk-1', 'This is a school of thought that stems from the work of <b>(1)</b> ______ (~1900). In structuralism, linguists are primarily concerned with the abstract language system shared by all members of a speech community, called <b>(2)</b> ______, and less so about <b>(3)</b> ______, which is about the concrete usage of language by the individual.'),
 ('gap-struk-2', 'The Swiss linguist <b>(1)</b> ______ is seen as the founder of structuralism. He distinguished between the system that all members of a speech community share, <b>(2)</b> ______, and the concrete language use of an individual speaker, <b>(3)</b> ______.'),
 ('gap-struk-3', 'Structuralists like <b>(1)</b> ______ focus on <b>(2)</b> ______ (the shared abstract system) rather than on <b>(3)</b> ______ (what a single person actually says or writes).'),
]
ZEICHEN = '<p>Figure: a circle divided in two – top half: a frog (the idea), bottom half: /frɒg/.<br><b>(4)</b> signifié (signified) = ______<br><b>(5)</b> ______ = the sound image, i.e. that which signifies</p>'
a21 = [V(i, 'structuralism', f'<p>{t}</p>{ZEICHEN}',
         [W('(1)', SAUS), W('(2)', ['langue']), W('(3)', ['parole']), W('(4) signifié =', ['concept', 'the concept', 'mental concept', 'idea', 'mental idea', 'that which is signified']), W('(5)', ['signifiant', 'signifier', 'signifiant (signifier)'])],
         '(1) Ferdinand de Saussure · (2) langue · (3) parole · (4) the concept / mental idea, i.e. that which is signified · (5) signifiant (signifier)') for i, t in G21]
A21 = dict(titel='2.1 Structuralism', punkte=5, teile=[dict(punkte=5, varianten=a21)])

# 2.2 Formalism (Chomsky): gap text (3 P)
CH = ["Chomsky's", 'Chomsky', "Noam Chomsky's", 'Noam Chomsky', 'Chomskys']
G22 = [
 ('gap-chom-1', 'This school of thought is widely associated with <b>(1)</b> ______ work in the 1950s and 1960s. He views every human as being born with a <b>(2)</b> ______, i.e. humans are viewed as genetically predisposed to learn language. This is based on the theory of <b>(3)</b> ______ which consists of syntactic structures and constraints that are thought to be universal in human languages and, thus, innate.'),
 ('gap-chom-2', 'According to <b>(1)</b> ______ (1950s/60s), children acquire their mother tongue so quickly because they are born with a <b>(2)</b> ______. It contains <b>(3)</b> ______: syntactic structures and constraints shared by all human languages.'),
 ('gap-chom-3', 'Formalism in the 1950s and 1960s: <b>(1)</b> ______ claims that humans are genetically predisposed to learn language, because every human is born with a <b>(2)</b> ______ (LAD). The innate, universal syntactic structures are called <b>(3)</b> ______.'),
]
a22 = [V(i, 'formalism-chomsky', f'<p>{t}</p>', [W('(1)', CH), W('(2)', ['language acquisition device', 'language acquisition device (LAD)', 'LAD']), W('(3)', ['Universal Grammar', 'UG'])],
         '(1) Chomsky(’s) · (2) language acquisition device (LAD) · (3) Universal Grammar') for i, t in G22]
A22 = dict(titel='2.2 Formalism', punkte=3, teile=[dict(punkte=3, varianten=a22)])

# 2.3 Jakobson (3 P)
L23 = [('list-jak-1', 'Formalism (Roman Jakobson 1920s): Name three linguistic disciplines that formalism heavily influenced.'),
       ('list-jak-2', 'Roman Jakobson (1920s) and the Prague Linguistic Circle shaped modern linguistics. Name three linguistic disciplines that formalism heavily influenced and say in a few words what each studies.')]
a23 = [V(i, 'formalism-jakobson', f'<p>{t}</p>', [T('1. / 2. / 3.', 3, 3)], UL('phonology (sound system)', 'morphology (structure of words)', 'syntax (structure of sentences)') + '<p>Also accepted: semantics, stylistics/poetics.</p>') for i, t in L23]
A23 = dict(titel='2.3 Formalism (Jakobson)', punkte=3, teile=[dict(punkte=3, varianten=a23)])

KL = dict(deckblatt=dict(fach='Introduction to English Linguistics – Key Concepts', pruefer='JLU Gießen', hilfsmittel='none',
                         bemerkungen='Structure like the worksheet “Key Concepts in Linguistics”. Answer in English.'),
          aufgaben=[A1, A21, A22, A23])
ids = {t['id'] for k in json.loads((IN / 'fach.json').read_text())['kapitel'] for t in k['themen']}
for A in KL['aufgaben']:
    assert sum(t['punkte'] for t in A['teile']) == A['punkte'], A['titel']
    for t in A['teile']:
        for v in t['varianten']:
            assert sum(f['p'] for f in v['felder']) == t['punkte'], v['id']
            for u in ([v['unter']] if isinstance(v['unter'], str) else v['unter']):
                assert u in ids, u
(IN / 'klausur.json').write_text(json.dumps(KL, ensure_ascii=False, indent=1))
print('ling: Probeklausur', sum(A['punkte'] for A in KL['aufgaben']), 'Punkte,', sum(len(t['varianten']) for A in KL['aufgaben'] for t in A['teile']), 'Varianten')
