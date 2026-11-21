# Intercultural Management (Script, Kersten-Frisch). Jeder Stichpunkt „fehlt vielleicht“ einzeln geprüft (13.11.2026).
# F = 'ikm' (vom Lader gesetzt). Stellen: sk/<PDF-Seite>.
DECKNAME[F] = {'sk': 'Script'}
kein(F, 'sk/4', 'Literature')                                   # Inhaltsverzeichnis
ok(F, 'sk/5', 'Introduction')                                   # Kapitelüberschrift; Inhalt der Einleitung steht in what-is-icm
kein(F, 'sk/13', 'Multikulturalität', 'Mehrsprachigkeit')       # Fußnote: Quelle des Beispiels (Projekt MuMiS)
ok(F, 'sk/28', 'parent-child', 'medium-sized')                  # Länderprofil China–Deutschland steht vollständig in china-germany (small families, family-owned SMEs)
kein(F, 'sk/29', 'Kowalski')                                    # Quelle der Übung
kein(F, 'sk/37', 'Hotslede', 'Tromenaars')                      # Tippfehler der Mitschrift (Hofstede, Trompenaars)
kein(F, 'sk/47', 'Blackboard', 'Spotlight')                     # Quelle/Organisatorisches der Aufgabe
kein(F, 'sk/52', 'Oshould'); kein(F, 'sk/54', 'Behavorial'); kein(F, 'sk/74', 'Clow-context')   # Schreibfehler der Mitschrift
ok(F, 'sk/55', 'Remember')                                      # Satzanfang; „nobody can be put into a box“ steht in strategies
ok(F, 'sk/63', 'open-access', 'Offering')                       # Maßnahmen zu social background stehen in diversity-measures
kein(F, 'sk/68', 'Publishing', 'Brealey')
for s_ in ('sk/82', 'sk/83', 'sk/84'): kein(F, s_, 'Brealey')   # Literaturangabe (Gibson 2021)
kein(F, 'sk/86', 'Smileys')                                     # Bildnachweise
