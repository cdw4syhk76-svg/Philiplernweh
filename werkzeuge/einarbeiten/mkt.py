"""Marketing: Folienstoff, der auf den Lernseiten fehlte (Runde b1, 13.11.2026). Format: werkzeuge/einarbeiten.py."""
STAND = 'b1'
KC = '<h3>Kurz-Check: richtig oder falsch?</h3>'
L = lambda *xs: ''.join(f'<li>{x}</li>' for x in xs)
E = [
 # ---- Kundenorientierung ----
 dict(t='kundenorientierung', alt='<p>Nicht jede gelungene Marketing-Aktivität ist Kundenorientierung.',
      neu='<p>[[Kundenorientierung ist <b>schwer zu fassen</b>; im Einzelfall ist es <b>Interpretationssache</b>, ob ein Verhalten Ausdruck besonderer Kundenorientierung ist. ]]Nicht jede gelungene Marketing-Aktivität ist Kundenorientierung.[[ Eine gelungene Kommunikationskampagne hat sicher damit zu tun, dass sich die Werbetreibenden gut in die Köpfe der Nachfrager versetzen konnten, aber ist das gleich Kundenorientierung?]]'),
 # ---- Wahrnehmung: Modell vollständig ----
 dict(t='wahrnehmung', vor='<p class="bruecke">Was heißt das fürs Marketing?</p>',
      block='<p>Im Modell (nach Steffenhagen) wirken auf diesen Ablauf die <b>Inhalte des Langzeitgedächtnisses</b> und die <b>Merkmale der Kontaktsituation</b> ein; Aktivierung, Aufmerksamkeit, (kognitive) Informationsverarbeitung und emotionales Erleben stehen in Wechselwirkung. Ergebnis sind die <b>momentanen Resultate eines Reizkontakts</b>.</p>'),
 # ---- Image: Assoziationsnetz Milka ----
 dict(t='risiko-vertrauen-image', vor=KC,
      block='<p><b>Beispiel Assoziationsnetzwerk der Marke Milka</b>: lila Verpackung, Tafelschokolade (rechteckige, flache Tafeln mit <b>eingestanzten Bruchstellen</b>), Alpenlandschaft (hohe Berge, grüne Landschaft, natürlich, heimelig), „Trau Dich zart zu sein“, schmeckt besonders gut, Genuss, sich etwas gönnen, Frustabbau, aber auch Kalorien und Karies. '
            'Unternehmen sind daran interessiert, dass das Assoziationsnetzwerk dichter bei den positiven Assoziationen ist.</p>'),
 dict(t='sr-sor', vor='<h3>Kurz-Check: richtig oder falsch?</h3>',
      block='<p>Den Organismus erklären verschiedene Theorien, auf deren Basis man Erkenntnisse gewinnt: <b>Wahrnehmungstheorie</b>, <b>Lern- und Gedächtnistheorie</b>, <b>Kognitionstheorie</b>, <b>Motivationstheorie</b>, <b>Entscheidungstheorie</b> und Persönlichkeitstheorie. Weitere Stimuli (Umweltreize usw.) wirken neben den Marketing-Reizen.</p>'),
]
