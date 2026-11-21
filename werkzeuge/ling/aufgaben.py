"""Erzeugt inhalte/ling/aufgaben.json (große Aufgaben im Klausurstil, Englisch, mit Tipps und Lösungsweg). Aufruf: python3 werkzeuge/ling/aufgaben.py"""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
A = []


def L(*punkte): return '<ul>' + ''.join(f'<li>{p}</li>' for p in punkte) + '</ul>'
def teil(text, punkte, t1, t2, loesung): return dict(text=text, punkte=punkte, tipp1=t1, tipp2=t2, loesung=loesung)
def aufgabe(id, unter, stufe, titel, ausgang, teile, art='anwendung', klausur=True):
    A.append(dict(id='ling-' + id, unter=unter, art=art, stufe=stufe, klausur=klausur, titel=titel, quelle='exam style', ausgang=ausgang, teile=teile))


aufgabe('dicho-tf', ['dichotomies', 'synchronic-diachronic', 'form-function', 'applied-theoretical'], 2, 'Dichotomies – true or false?',
    '<p>Decide whether the statements are true or false. If false, write the correct answer.</p>', [
    teil('<b>1.1</b> The term <i>synchronic</i> describes a specific point in time, while <i>diachronic</i> describes language change through time.', 1, 'Think of snapshot vs. film.', 'syn = together, dia = through.',
         '<p><b>a) True.</b> Nothing to correct.</p>'),
    teil('<b>1.2</b> Function denotes a speaker’s ability to only be able to convey basic messages, while form denotes a mastery over the language.', 3, 'Is the pair about the speaker’s skill?', 'Form = structure, function = …',
         '<p><b>b) False.</b> Correct answer: <i>Form refers to the structure of language (sounds, word forms, sentence patterns), function refers to what a form is used for in communication, i.e. its purpose (e.g. “Can you open the window?” = question form, request function).</i></p>'),
    teil('<b>1.3</b> Applied linguistics refers to studies that still have real-life applications, ‘not applied’ refers to studies in the past that are not in use anymore.', 3, 'Is the difference about time or about the goal?', 'Theoretical linguistics studies language for its own sake.',
         '<p><b>b) False.</b> Correct answer: <i>Applied linguistics uses linguistic findings to solve practical, real-life problems (e.g. language teaching, translation, speech therapy). ‘Not applied’ (theoretical) linguistics studies language for its own sake to describe and explain how it works.</i></p>')])

aufgabe('schools-gaps', ['structuralism', 'linguistic-sign', 'formalism-chomsky', 'formalism-jakobson'], 2, 'Schools of thought – fill in the gaps',
    '<p>Complete the texts from the worksheet and label the model of the sign.</p>', [
    teil('<b>2.1 Structuralism:</b> This is a school of thought that stems from the work of ____ (~1900). In structuralism, linguists are primarily concerned with the abstract language system shared by all members of a speech community, called ____, and less so about ____, which is about the concrete usage of language by the individual.', 3, 'Swiss linguist, Geneva.', 'French terms: system vs. speech.',
         '<p>Ferdinand de <b>Saussure</b> · <b>langue</b> · <b>parole</b></p>'),
    teil('<b>2.1 (figure)</b> Label the sign /frɒg/: signifié (signified) = ____ ; ____ = the sound image, i.e. that which signifies.', 2, 'The upper half shows the frog idea.', 'The lower term ends in -ant.',
         '<p>signifié = <b>the concept / mental idea, i.e. that which is signified</b> · <b>signifiant (signifier)</b> = the sound image</p>'),
    teil('<b>2.2 Formalism:</b> This school of thought is widely associated with ____ work in the 1950s and 1960s. He views every human as being born with a ____, i.e. humans are viewed as genetically predisposed to learn language. This is based on the theory of ____ which consists of syntactic structures and constraints that are thought to be universal in human languages and, thus, innate.', 3, 'American linguist at MIT.', 'LAD …, UG …',
         '<p><b>Chomsky’s</b> · <b>language acquisition device (LAD)</b> · <b>Universal Grammar</b></p>'),
    teil('<b>2.3 Formalism (Roman Jakobson 1920s):</b> Name three linguistic disciplines that formalism heavily influenced.', 3, 'sound – word – sentence', 'P – M – S',
         L('phonology', 'morphology', 'syntax'))], art='transfer')

aufgabe('explain', ['form-function', 'linguistic-sign', 'structuralism', 'formalism-chomsky'], 3, 'Explaining with examples',
    '<p>A fellow student missed the session. Explain the key concepts to her in your own words – in English, with one example each.</p>', [
    teil('Explain form vs. function using a sentence of your choice.', 3, 'Choose a question that is not really a question.', '“Can you pass the salt?”',
         L('Form = structure: “Can you pass the salt?” is an interrogative sentence (yes/no question).', 'Function = purpose: it is used as a polite request.', 'One form can have several functions, one function several forms.')),
    teil('Explain Saussure’s linguistic sign using the word “tree”.', 3, 'Two sides of one sheet of paper.', 'concept + sound image; arbitrary.',
         L('signifié: the concept/idea of a tree', 'signifiant: the sound image /triː/', 'the link is arbitrary (German: Baum)')),
    teil('Compare langue/parole with competence/performance.', 4, 'Who? System or use?', 'social vs. mental.',
         L('Saussure: langue = shared abstract system (social), parole = concrete individual use.', 'Chomsky: competence = unconscious grammar knowledge (mental, individual), performance = actual use.', 'Both focus on the system (langue / competence).'))])

ids = {t['id'] for k in json.loads((ROOT / 'inhalte/ling/fach.json').read_text())['kapitel'] for t in k['themen']}
for a in A:
    for u in a['unter']:
        assert u in ids, (a['id'], u)
(ROOT / 'inhalte/ling/aufgaben.json').write_text(json.dumps({'hinweis': 'Große Aufgaben im Klausurstil (Englisch).', 'aufgaben': A}, ensure_ascii=False, indent=1) + '\n')
print(f'ling: {len(A)} Aufgaben')
