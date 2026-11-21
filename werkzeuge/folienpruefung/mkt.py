# Marketing (Chammout). Jeder Stichpunkt „fehlt vielleicht“ einzeln geprüft (13.11.2026). Echte Lücken: werkzeuge/einarbeiten/mkt.py
# (Sinus-Milieus 1995/2010/2021 mit Wein-Segmentierung, Kundenorientierung, Wahrnehmungsmodell, Milka-Assoziationsnetz, SOR-Theorien).
DECKNAME[F] = {'vl': 'Folien'}
for st in ('vl/12', 'vl/13', 'vl/14', 'vl/19', 'vl/34', 'vl/277', 'vl/278', 'vl/279', 'vl/281', 'vl/291'): kein(F, st, '*')   # Organisatorisches, Lernhinweise, Klausurhinweise
for st in ('vl/280', 'vl/282', 'vl/283'): kein(F, st, '*')   # Beispiel-Wissensfragen zur Marktforschung (Fragetypen zeigen; Marktforschung ist nicht Stoff dieser Vorlesung)
for st in ('vl/284', 'vl/285', 'vl/286', 'vl/287', 'vl/288', 'vl/289', 'vl/290'): ok(F, st, '*')   # Beispielaufgabe Club „Exil“: Aufgabe in LernWeh und Lernseiten marktabgrenzung/segment
ok(F, 'vl/7', 'Eckpunkte'); kein(F, 'vl/8', 'Murdoch'); ok(F, 'vl/22', 'Zielauswahl'); ok(F, 'vl/26', 'Zeitangaben')
kein(F, 'vl/28', 'Kunden-Junde', 'Personalwahl'); ok(F, 'vl/29', 'Kundenabwanderung')
ok(F, 'vl/37', 'Finanzierungsmarketing'); ok(F, 'vl/38', 'Intranet'); ok(F, 'vl/39', 'Herstellermarketing'); ok(F, 'vl/40', 'Investitionsgütermarketing')
ok(F, 'vl/41', 'Einpersonenentscheidungen'); kein(F, 'vl/41', 'Burmann', 'Kirchgeorg', 'Meffert'); ok(F, 'vl/45', 'Marketing-Hype'); kein(F, 'vl/49', 'Filialennetz')
ok(F, 'vl/57', 'Bauanleitung', 'Bausatz'); kein(F, 'vl/62', 'Aupfiff', 'Hochschulen', 'Lidl-App'); kein(F, 'vl/64', 'BWL-Professorin', 'Buchtitel', 'Hartmann')
ok(F, 'vl/69', 'Arztbesuch', 'Friseurbesuch'); kein(F, 'vl/70', 'Anleitung', 'Transportmittel'); ok(F, 'vl/76', 'Gewerbetreibende', 'Herstellerperspektive')
kein(F, 'vl/89', 'Lobbyismus'); ok(F, 'vl/89', 'Verkaufsförderungsaktionen'); ok(F, 'vl/91', 'Handelsunternehmen'); ok(F, 'vl/92', 'Produktinnovationen')
kein(F, 'vl/97', 'Fair-Trade-Kaffee'); ok(F, 'vl/103', 'Abgrenzungsdimension'); kein(F, 'vl/103', 'Pharmazeutiles'); ok(F, 'vl/120', 'After-Sales-Bereich')
ok(F, 'vl/123', 'Arbeitermilieu'); ok(F, 'vl/130', 'Arbeitermilieu'); kein(F, 'vl/187', '*')   # Quellenhinweis Sinus-Institut
ok(F, 'vl/190', 'Angebotsoligopol'); kein(F, 'vl/195', 'Fragestellungen'); kein(F, 'vl/196', 'Annährung'); ok(F, 'vl/199', 'Erkenntnisgewinnung')
ok(F, 'vl/201', 'Konsumentinnen'); ok(F, 'vl/202', 'Konsumentinnen'); kein(F, 'vl/204', 'Aktiviertheit', 'Leistungsvermögen')   # handschriftliche Randnotiz
ok(F, 'vl/229', 'Forschungszweig'); kein(F, 'vl/231', 'Frodukt'); ok(F, 'vl/232', 'Bio-Eiern', 'Matratzen', 'Vermarktungsaktivitäten'); kein(F, 'vl/232', 'Chemikalien', 'LabortetsPsychologische', 'Leseeche')
ok(F, 'vl/247', 'Gesamtvertrauen'); kein(F, 'vl/260', 'Kneipenbesitzer'); ok(F, 'vl/264', 'Lebensdauer')

# neuer Foliensatz 16.11.2026 (handschriftliche Randnotizen): Texterkennungsreste und sinngemäß Vorhandenes
kein(F, 'vl/89', 'Handelskammertbündeln'); kein(F, 'vl/101', 'ZSeiten'); ok(F, 'vl/106', 'Prävention'); ok(F, 'vl/204', 'Steinzeit')

# Sinus-Milieus im Einzelnen: laut Folie „Alles Sinus nicht im Detail relevant!“ (nur wissen, worum es geht) – kein Lernstoff im Detail
for st in ('vl/122', 'vl/123', 'vl/124', 'vl/125', 'vl/126', 'vl/127', 'vl/130', 'vl/132'): kein(F, st, '*')
