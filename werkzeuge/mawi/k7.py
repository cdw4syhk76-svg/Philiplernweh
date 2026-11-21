import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / 'fachbau'))
from bausteine_de import *
from fig import *

# ---------------------------------------------------------------- 1 Early Involvement
def ei_svg():
    X = lambda i: 50 + i * 60
    Y = lambda p: 210 - p * 1.8
    phasen = ['Entwick-\nlung', 'Planung', 'Produk-\ntion', 'Material', 'Vertrieb']
    gesetzt = [0, 70, 88, 95, 98, 100]
    angefallen = [0, 5, 12, 40, 85, 100]
    s = achsen(50, 210, 352, 14, '', 'Produktkosten (kumuliert, %)')
    for v in (50, 100):
        s += strich(50, Y(v), 350, Y(v), 'var(--line)', 1, True) + T(46, Y(v) + 4, f'{v}', 12, 400, 'end', 'var(--muted)')
    s += tpg(linie([(X(i), Y(p)) for i, p in enumerate(gesetzt)], 'var(--primary)', 2.8), 'Festgelegte Kosten (costs set): Nach der Entwicklungsphase sind schon rund 70 % der Produktkosten festgelegt.')
    s += tpg(linie([(X(i), Y(p)) for i, p in enumerate(angefallen)], 'var(--muted)', 2.4, True), 'Angefallene Kosten (costs incurred): Sie entstehen vor allem später, in Produktion und beim Material.')
    s += tpg(punkt(X(1), Y(70), 'var(--primary)', 6) + T(X(1) + 8, Y(70) + 4, 'ca. 70 % festgelegt', 12, 700, 'start', 'var(--primary)'), 'Ungefähr 70 % der Produktkosten werden in der Phase Design/Entwicklung festgelegt. Danach besteht nur noch geringer Einfluss.')
    s += T(X(2) + 4, Y(88) + 18, 'festgelegt', 12, 700, 'start', 'var(--primary)') + T(X(4) - 8, Y(60), 'angefallen', 12, 700, 'end', 'var(--muted)')
    for i, ph in enumerate(phasen):
        s += T(X(i) + 30, 228, ph, 12, 400, fill='var(--muted)')
    return svg(360, 262, s, 'Festgelegte und angefallene Kosten über die Phasen (schematisch)', maxw=420)

t_ei = thema('early-involvement', 'Early Involvement: den Einkauf früh einbinden',
    kern='Early Involvement ist die rechtzeitige, frühe Zusammenarbeit und gegenseitige Information zwischen Fachabteilung und Einkauf über Projekt, Zeitachse und geplante Mengen. Rund 70 % der Produktkosten werden in Design und Entwicklung festgelegt, aber erst später verursacht. Je früher der Einkauf eingebunden ist und je neutraler die Spezifikation, desto größer das Einsparpotenzial (über 10 %); bei spätem Einbezug und vorausgewähltem Lieferanten bleibt kaum etwas.',
    kurz=p('Die Entwicklung der Neckarrad GmbH konstruiert einen neuen Motorhalter und schreibt gleich hinein: „Teil von Firma X“. Kommt der Einkauf erst danach dazu, kann er kaum noch verhandeln. Der Lieferant steht ja schon fest.')
        + p('Merksatz der Vorlesung: <b>Je früher der Einkauf einbezogen wird, desto größer der Kostenhebel.</b> Denn rund 70 % der Produktkosten werden schon in der Entwicklung festgelegt.'),
    fig=fw('Kosten werden früh festgelegt, aber spät verursacht. Tippe auf die Linien.') + bild(ei_svg()),
    figcap='schematisch nach Folie „Einfluss der Entwicklung (Engineering) auf die Kosten“',
    article=h3('Definition')
        + p('<b>Early Involvement: rechtzeitige und frühe Zusammenarbeit und gegenseitige Information zwischen der Fachabteilung und dem Einkauf hinsichtlich des Projekts, der Zeitachse und der geplanten Mengen, mit dem Ziel, die Ansprüche beider Partner im Sinne des Unternehmens optimal umzusetzen.</b> Es ist interdisziplinäre Zusammenarbeit in der frühen Phase der Produktentwicklung und ein wirksamer Hebel zur Kostensenkung.')
        + h3('Warum früh?')
        + liste(['Zeitpunkt der Kostenfestlegung („costs set“) und des tatsächlichen Kostenanfalls („costs incurred“) sind unterschiedlich.', '<b>Ungefähr 70 % der Produktkosten werden in der Phase Design/Entwicklung festgelegt.</b> Ist das Produktdesign festgelegt, besteht nur noch geringer Einfluss auf die Kosten.',
                 'Wertanalysen (135 Analysen in 35 Unternehmen) ergaben im Schnitt rund ein Drittel unnötiger Kosten; davon gehen 65 % auf Design und Entwicklung, 19 % auf die Produktionsplanung und 15 % auf den Einkauf zurück. Fazit: Kooperation mit dem Einkauf ist essenziell.'])
        + h3('Einsparpotenzial nach Spezifikation und Zeitpunkt')
        + tabelle(['', 'späte Einbindung', 'frühe Einbindung'], [['neutrale Spezifikation', 'mittel (3–5 %)', '<b>hoch (über 10 %)</b>'], ['nicht neutral (Lieferant vorausgewählt)', 'keins oder gering', 'mittel (3–5 %)']])
        + p('<b>Wenn die Spezifikation neutral, d. h. unabhängig vom Anbieter formuliert ist und die Einbindung des Einkaufs rechtzeitig erfolgt, ist das Einsparpotenzial am größten.</b> Hat die Fachabteilung den Lieferanten über die Spezifikation schon „vorausgewählt“ und wird der Einkauf spät eingebunden, bestehen kaum noch Einsparpotenziale.')
        + h3('Wann im Produktentstehungsprozess (PEP)?')
        + p('Der PEP läuft über Innovation, Projektvorbereitung, Konzeptentwicklung, Produkt- und Prozessentwicklung, Vorserie und Serienfertigung (oft 1–4 Jahre). Der Einkauf sollte idealerweise schon in der <b>Projektvorbereitung</b> eingebunden sein: Marktpotenziale erheben, Kundenanforderungen detaillieren, Rahmenbedingungen (Zeit, Kosten, Ressourcen) klären, entscheiden, ob die Anforderungen auch unter Kostengesichtspunkten erfüllbar sind; Bestandteile: Projektteam, Kick-off, Informationszusammenstellung, Lastenheft.')
        + p('Status quo: Die Einbindung ist nach wie vor unzureichend, am besten noch bei Produktionsmaterial; der Einkauf muss sich und seine Leistungen intern besser verkaufen.'),
    merk='Early Involvement = frühe Zusammenarbeit Fachabteilung–Einkauf (Projekt, Zeitachse, Mengen). Ca. 70 % der Kosten werden in Design/Entwicklung festgelegt (costs set ≠ costs incurred). Neutrale Spezifikation + frühe Einbindung: > 10 % Einsparung; vorausgewählter Lieferant + späte Einbindung: kaum Potenzial. Ideal: Einbindung in der Projektvorbereitung. Je früher, desto größer der Kostenhebel.',
    exam='Begriff, Begründung (70 % Kostenfestlegung), Einsparmatrix Spezifikation × Zeitpunkt.',
    fehler=['Verwechseln: Die meisten Kosten fallen spät an, werden aber früh festgelegt.'],
    src='Folien 211–221')

# ---------------------------------------------------------------- 2 Bündelung und RFx
fig_rfx = svg(360, 258,
    achsen(56, 210, 350, 14, '', 'Konkretheit, Verbindlichkeit')
    + box(250, 24, 96, 46, 'RFQ', size=14, art='hl', tip='Request for Quotation: hohe Verbindlichkeit; an wenige Lieferanten; Angebot mit Preisen auf Basis einer detaillierten Spezifikation; Basis der Auswahl im Wettbewerb und für Verhandlungen.')
    + box(160, 92, 96, 46, 'RFP', size=14, tip='Request for Proposal: an weniger Lieferanten als ein RFI; Lieferanten sollen Vorschläge und innovative Lösungen machen; keine Weitergabe der Ideen an Wettbewerber (NDA).')
    + box(70, 152, 96, 46, 'RFI', size=14, tip='Request for Information: früh im MGM-Prozess; Lieferanten kennenlernen (Fähigkeiten, Produkte, Organisation, Standorte, Kapazitäten); niedrige Verbindlichkeit.')
    + T(66, 230, 'viele', 12, 400, 'start', 'var(--muted)') + T(346, 230, 'wenige', 12, 400, 'end', 'var(--muted)') + T(206, 248, 'Anzahl der angefragten Lieferanten', 12, 700),
    'RFI, RFP und RFQ', maxw=420)

t_rfx = thema('buendelung-rfx', 'Bündelung und Anfragen: RFI, RFP, RFQ',
    kern='Bündelung lohnt sich bei ähnlichen Beschaffungsobjekten und -prozessen, hohem gemeinsamem Volumen, geringer Spezifität und Komplexität, niedrigen Wechselkosten und geringem Versorgungsrisiko (Multiple Sourcing, unkritische Teile). Vom Bedarf zum Rahmenvertrag: Bedarfe → Vorauswahl → RFP/RFQ → Angebotsklärung → systematischer Angebotsvergleich (CoQ) → Verhandlung → Entscheidung → Rahmenvertrag. RFI: informieren, früh, viele Lieferanten, unverbindlich; RFP: Lösungsvorschläge; RFQ: verbindliches Preisangebot, wenige Lieferanten.',
    kurz=p('Drei Werke der Neckarrad GmbH kaufen dieselben Schrauben bei drei Händlern. <b>Bündeln</b> bringt einen besseren Preis. Dann fragt der Einkauf an, Schritt für Schritt immer verbindlicher: erst <b>RFI</b> (Wer kann was?), dann <b>RFP</b> (Macht uns Vorschläge!), dann <b>RFQ</b> (Euer verbindlicher Preis bitte!).')
        + p('Tipp aus der Vorlesung: Nicht zu oft konkrete Angebote anfragen, wenn man sie ohnehin nicht annimmt. Das macht Lieferanten müde.'),
    fig=fw('Je weniger Lieferanten, desto verbindlicher. Tippe auf die Kästen.') + bild(fig_rfx),
    figcap='nach Folien „Varianten von Anfragen“',
    article=h3('Wann lohnt sich Bündeln?')
        + tabelle(['Kriterium', 'hohe Bündelungsfähigkeit', 'geringe Bündelungsfähigkeit'], [
            ['Beschaffungsobjekt', 'identisch/ähnlich', 'heterogen'], ['gemeinsames Beschaffungsvolumen', 'hoch', 'gering'], ['Beschaffungsprozesse', 'identisch/ähnlich', 'verschieden'],
            ['Grad der Spezifität', 'gering', 'hoch'], ['Komplexität', 'gering', 'hoch'], ['Sourcing-Konzept', 'Multiple Sourcing', 'Single Sourcing'], ['Lieferantenwechselkosten', 'gering', 'hoch'],
            ['Versorgungsrisiko', 'gering', 'hoch'], ['Klassifizierung', 'unkritisches Bauteil', 'kritisch'], ['Nachfragemacht durch Bündelung', 'hoch', 'gering']])
        + h3('Vom Bedarf bis zum Rahmenvertrag')
        + fluss([('Bedarfe', 'erheben und bündeln'), ('Vorauswahl', 'Lieferanten'), ('RFP, RFQ', 'Anfrage'), ('Angebotsklärung', 'Präsentationen'), ('Angebotsvergleich', 'systematisch (CoQ)'), ('Verhandlung', ''), ('Entscheidung', ''), ('Rahmenvertrag', 'Abschluss')], hl=7)
        + h3('Varianten von Anfragen')
        + tabelle(['Anfrage', 'Merkmale', 'Verbindlichkeit'], [
            ['RFI (Request for Information)', 'früh im MGM-Prozess; Lieferanten kennenlernen: Fähigkeiten, Produkte, Organisation und Standorte, Kapazitäten; unterstützt die Datenbeschaffung', 'niedrig'],
            ['RFP (Request for Proposal)', 'an weniger Lieferanten als ein RFI; basiert auf deren Erfahrung; Lieferanten machen Vorschläge, innovative Lösungen möglich; keine Weitergabe an Wettbewerber (NDA)', 'mittel'],
            ['RFQ (Request for Quotation)', 'an wenige Lieferanten; Angebot mit kommerziellen Angaben und Preisen auf Basis einer detaillierten Spezifikation; Basis für die Lieferantenauswahl im Wettbewerb und für Verhandlungen mit mehreren Lieferanten', 'hoch']])
        + p('Angebote werden mit einer strukturierten Vergleichsmatrix verglichen (CoQ-Tool/Template).')
        + spiel('sp-rfx', 'RFI, RFP oder RFQ?', ['RFI', 'RFP', 'RFQ'], [
            ('„Welche Kapazitäten und Standorte haben Sie?“ an 30 Anbieter', 0, 'Informationsabfrage.'), ('„Schlagen Sie uns eine leichtere Gepäckträgerlösung vor.“', 1, 'Lösungsvorschlag.'),
            ('„Ihr Preis für 20.000 Stück nach Zeichnung 4711, gültig bis 30.6.“ an 3 Anbieter', 2, 'Verbindliches Preisangebot.')]),
    merk='Bündeln lohnt bei ähnlichen Objekten/Prozessen, hohem Volumen, geringer Spezifität und Komplexität, Multiple Sourcing, geringen Wechselkosten und Risiken (unkritische Teile). Prozess: Bedarfe → Vorauswahl → RFP/RFQ → Angebotsklärung → Vergleich (CoQ) → Verhandlung → Entscheidung → Rahmenvertrag. RFI (Info, viele, unverbindlich) → RFP (Vorschläge, NDA) → RFQ (Preise, wenige, verbindlich).',
    exam='RFI/RFP/RFQ unterscheiden; Bündelungskriterien.',
    fehler=['RFQ an sehr viele Lieferanten: Dafür ist der RFI da.'],
    src='Folien 225–230')

# ---------------------------------------------------------------- 3 Rahmenvertrag
fig_rv = svg(360, 250,
    f'<ellipse cx="180" cy="125" rx="174" ry="118" style="fill:var(--pale);stroke:var(--line)" stroke-width="1.3"/>'
    + f'<ellipse cx="180" cy="150" rx="128" ry="86" style="fill:var(--card);stroke:var(--primary-2)" stroke-width="1.3"/>'
    + f'<ellipse cx="180" cy="176" rx="82" ry="52" style="fill:var(--primary);stroke:var(--primary)" stroke-width="1.3"/>'
    + tpg(T(180, 32, 'Rahmenvertrag', 14, 800), 'Rahmenvertrag: individuell ausgehandelte Geschäftsbedingungen für zukünftige Geschäfte. Begründet keine eigenen Rechte und Pflichten (relativ unverbindlich).')
    + tpg(T(180, 90, 'Jahresabschluss /\nPreisabschluss', 12, 700), 'Jahresabschluss/Preisabschluss: bezieht sich auf den Rahmenvertrag und legt Preise für Produkte und Leistungen fest. Begründet (noch) keine eigenen Rechte und Pflichten.')
    + tpg(T(180, 166, 'B+A-Plan,\nEinzelbestellung', 12, 800, fill='var(--on-primary)'), 'Einzelbestellung (bzw. Bedarfs- und Abrufplan): bezieht sich auf den Jahresabschluss und verpflichtet zur Lieferung und Bezahlung. Erst hier entsteht Verbindlichkeit.')
    + T(180, 208, 'verbindlich', 12, 400, fill='var(--on-primary)'),
    'Rahmenvertrag, Jahresabschluss, Einzelbestellung', maxw=420)

t_rv = thema('rahmenvertrag', 'Rahmenvertrag als zentrales Instrument des MGM',
    kern='Ein Rahmenvertrag enthält individuell ausgehandelte Geschäftsbedingungen für künftige Aufträge (Abrufe), unterliegt normalerweise keiner AGB-Kontrolle und begründet keine eigenen Rechte und Pflichten; Verbindlichkeit entsteht erst durch die Bestellung bzw. den Lieferabruf. Hierarchie: Rahmenvertrag → Jahres-/Preisabschluss → B+A-Plan/Einzelbestellung (verpflichtet zu Lieferung und Zahlung). Prinzip im MGM: zentrale Bündelung und Rahmenverträge, dezentrale Abrufe.',
    kurz=p('Die Zentrale der Neckarrad GmbH verhandelt mit einem Schraubenhändler einen <b>Rahmenvertrag</b>: Qualität, Gewährleistung, Gerichtsstand. Darauf folgt ein <b>Jahresabschluss</b> mit den Preisen. Bestellen tun die Werke dann selbst mit <b>Einzelbestellungen</b>, immer mit Bezug auf den Rahmenvertrag.')
        + p('Wichtig: Der Rahmenvertrag allein verpflichtet niemanden zu liefern oder abzunehmen, außer das ist ausdrücklich vereinbart.'),
    fig=fw('Drei Ebenen der Verbindlichkeit. Tippe auf die Ringe.') + bild(fig_rv),
    figcap='nach Folien „Rahmenvertrag – Zusammenhänge“ und „Rahmenvertrag als zentrales Instrument des MGM“',
    article=h3('Prinzip im MGM')
        + p('<b>(Zentrale) Bündelung und Rahmenverträge sind Voraussetzung für die Umsetzung des MGM.</b> Der Lieferant hat einen strategischen Vertragspartner (MGM): Das MGM bündelt Bedarfe, führt den RFQ-Prozess und schließt Rahmenverträge ab; der dezentrale (operative) Einkauf erhebt lokale Bedarfe, meldet sie an das MGM und ruft dezentral unter Bezug auf die Rahmenverträge ab.')
        + p('Organisationsvarianten zur Hebung von Bündelungspotenzialen: konzernübergreifendes MGM, Lead-Buyer-Organisation, zentrale Bündelungseinkäufe auf Konzern-, Bereichs-, Regionen- und Länderebene, internationale Einkaufsbüros, Einkauf als Shared-Service-Abteilung.')
        + h3('Regelungen und Inhalte')
        + liste(['individuell ausgehandelte Geschäftsbedingungen für alle künftigen Aufträge (Abrufe)', 'unterliegt normalerweise nicht der AGB-Kontrolle (ausgehandelt)',
                 '<b>begründet keine eigenen Rechte und Pflichten</b>: Der Einkäufer kann keine Lieferung verlangen, wenn nicht Kapazitätsvorhaltung, Mindestbevorratung im Konsignationslager, Durchlaufzeiten oder Serviceleistungen ausdrücklich vereinbart sind; der Lieferant kann keine Abnahme verlangen, wenn nicht Mindestabnahme oder Lieferquote vereinbart sind',
                 'wichtig ist die Bezugnahme: Jahresabschluss auf Grundlage des Rahmenvertrags, B+A-Plan auf Grundlage des Jahresabschlusses, Einzelbestellung auf Grundlage des Rahmenvertrags'])
        + h3('Wichtige Regelungstatbestände')
        + liste(['Gültigkeit von Qualitätsvereinbarungen bzw. Verpflichtungen zu Zertifizierungen', 'Gewährleistungs- und Versicherungsfragen', 'Gültigkeit von Nebendokumenten (Anlieferungs-, Verpackungsvorschriften, Informationspflichten)',
                 'Stornierung von Bestellungen, Produktabkündigungen', 'Gültigkeit der eigenen Einkaufsbedingungen', 'Kapazitätsbereitstellung und Lieferfähigkeit', 'Vertragsstrafen bei Leistungsstörungen',
                 'konzernweite Gültigkeit', 'Gerichtsstand und anwendbares Recht', 'salvatorische Klausel'])
        + p('<b>Praxistipps:</b> Gerichtsstand am deutschen Firmensitz und deutsches Recht vereinbaren, UN-Kaufrecht ausschließen. <b>Bestellungen müssen sich immer auf den Rahmenvertrag beziehen!</b>')
        + h3('Vertragsmanagement im MGM')
        + tabelle(['Phase', 'Inhalt'], [['Vertragsplanung', 'Vertragsarten: Bestellung (PO), Rahmenvertrag, Preisabschluss, Non-Disclosure Agreement (NDA, Vertraulichkeit), ausformulierter spezifischer Vertrag'],
                                        ['Vertragsdurchführung', ''], ['Vertragsausstiegsplanung', 'Bedingungen der Beendigung, Vertragsstrafen, nachvertragliche Pflichten'],
                                        ['Vertragsmanagement', 'Fortschreibung, Erneuerung mit neuen Konditionen, Ausweitung/Einschränkung, Beenden/Auslaufen, Vertragscontrolling'], ['Claim-Management', 'Reklamation bei Schäden der gelieferten Produkte']])
        + p('<b>Wichtige KPIs aus der Praxis:</b> die <b>Rahmenvertragsquote</b> (Anteil des Einkaufsvolumens, der über Rahmenverträge läuft) und die <b>Cash-Out-Quote</b> (Anteil des Einkaufsvolumens, der tatsächlich über die vereinbarten Verträge abgerechnet wird). Einfach gesagt: Je höher beide sind, desto besser greift die Bündelung des MGM.'),
    merk='Rahmenvertrag: individuelle Bedingungen für künftige Abrufe, keine AGB-Kontrolle, keine eigenen Rechte und Pflichten (keine Liefer-/Abnahmepflicht ohne ausdrückliche Vereinbarung). Ebenen: Rahmenvertrag → Jahres-/Preisabschluss (Preise) → B+A-Plan/Einzelbestellung (verpflichtet zu Lieferung und Zahlung). MGM: zentral bündeln und abschließen, dezentral abrufen. Tipps: deutsches Recht, Gerichtsstand Firmensitz, UN-Kaufrecht ausschließen, Bestellungen immer mit Bezug auf den Rahmenvertrag.',
    exam='Verbindlichkeit der Ebenen; Inhalte eines Rahmenvertrags; Rolle im MGM.',
    fehler=['Glauben, ein Rahmenvertrag verpflichte zur Abnahme.'],
    src='Folien 226–234, 243–245')

# ---------------------------------------------------------------- 4 Vertragsrecht
fig_rang = svg(360, 220,
    box(60, 8, 240, 56, '1. individuell ausgehandelte\nRegelungen', size=12, art='hl', tip='Vorrang haben individuell ausgehandelte Regelungen: Vertragsgegenstand, Preis, Liefertermin.')
    + box(36, 76, 288, 56, '2. Allgemeine Geschäfts-\nbedingungen (AGB)', size=12, tip='Danach gelten AGB, soweit anerkannt bzw. nicht widersprochen.')
    + box(12, 144, 336, 56, '3. gesetzliche Regelungen\n(Kaufrecht, Mietrecht …)', size=12, tip='Auffanglösung für alle Punkte, für die keine individuelle Regelung vereinbart wurde.'),
    'Rangfolge der Vertragsinhalte', maxw=420)

t_recht = thema('vertragsrecht', 'Verträge im Einkauf: Abschluss, Rangfolge, Vertragsarten',
    kern='Ein Vertrag entsteht durch zwei Willenserklärungen: Angebot (ausreichend bestimmt) und Annahme (bedingungslos); „ja, aber“ ist Ablehnung mit neuem Angebot. Verträge sind grundsätzlich formfrei (mündlich, E-Mail, konkludent), Schriftform dient Beweis und Nachvollziehbarkeit. Rangfolge: individuelle Regelungen vor AGB vor Gesetz. Kaufvertrag (§ 433 BGB: Eigentum verschaffen), Werkvertrag (§ 631: Erfolg geschuldet), Dienstvertrag (§ 611: Tätigkeit, ergebnisunabhängig). Für Kaufleute: Wareneingangsprüfung mit unverzüglicher Rüge (§ 377 HGB) und kaufmännisches Bestätigungsschreiben.',
    kurz=p('Der Einkäufer der Neckarrad GmbH sagt am Telefon „Ja, wir nehmen die 500 Sättel“: Der Vertrag ist geschlossen, auch ohne Unterschrift. Sagt er „Ja, aber 5 % billiger“, ist das eine <b>Ablehnung mit neuem Angebot</b>.')
        + p('Und wenn die Sättel ankommen, muss er sie <b>sofort prüfen</b>: Rügt er offensichtliche Mängel nicht unverzüglich, gilt die Ware als ordnungsgemäß geliefert (§ 377 HGB).'),
    fig=fw('Was gilt, wenn sich Regelungen widersprechen? Tippe auf die Stufen.') + bild(fig_rang),
    figcap='nach Folien „Exkurs: Wichtige Verträge im Einkauf“',
    article=p('„Wenn man einem Menschen trauen kann, erübrigt sich ein Vertrag. Wenn man ihm nicht trauen kann, ist ein Vertrag nutzlos.“ (J. Paul Getty) – trotzdem gilt: Gute Verträge helfen, Gerichtsprozesse zu vermeiden.')
        + h3('Abschluss und Form')
        + liste(['<b>Abschluss durch zwei Willenserklärungen</b>: 1. Angebot mit ausreichend bestimmtem Inhalt, 2. Annahme: bedingungslos „ja, ich will“.', '„Ja, aber“ ist Ablehnung verbunden mit einem Gegenangebot.',
                 'Ausnahme: Bei Widerspruch gegen AGB gilt die gesetzliche Regelung, aber nur, wenn die Abwicklung tatsächlich erfolgt.',
                 '<b>Formfreiheit</b>: Verträge sind grundsätzlich formfrei, wenn keine besondere Form gesetzlich vorgeschrieben ist (z. B. Grundstückskauf beim Notar): mündlich (Handschlag), Fax/E-Mail, konkludentes (schlüssiges) Verhalten (z. B. Cola-Automat).',
                 'Schriftliche Dokumentation ist trotzdem wichtig: Missverständnisse vermeiden, spätere Nachvollziehbarkeit (auch durch Dritte), Beweisführung im Streitfall.'])
        + h3('Vertretung')
        + p('Verträge schließen Organe oder Bevollmächtigte (z. B. Prokura „ppa.“, Handlungsvollmacht „i. V.“); Unterschriftsregelungen legen Berechtigungen nach Art des Geschäfts und Wertgrenzen fest. <b>Vertretung ohne Vertretungsmacht</b>: Der Vertrag kommt nur mit dem Vertreter zustande; nachträgliche Genehmigung ist ausdrücklich oder konkludent möglich. Anscheins- und Duldungsvollmacht: Das Verhalten des Vertretenen legt eine Vollmacht nahe bzw. er duldet den falschen Anschein.')
        + h3('Rangfolge der Inhalte')
        + p('1. individuell ausgehandelte Regelungen (Vertragsgegenstand, Preis, Liefertermin), 2. AGB (anerkannt bzw. nicht widersprochen), 3. gesetzliche Regelungen als Auffanglösung.')
        + h3('Vertragsarten')
        + tabelle(['Vertrag', 'Gegenstand', 'Beispiel'], [['Kaufvertrag (§§ 433 ff. BGB)', 'Verschaffung von Eigentum an einer beweglichen Sache (neu, gebraucht oder noch herzustellen)', 'Kauf von Akkus'],
                                                     ['Werkvertrag (§§ 631 ff. BGB)', 'Herstellung bzw. Durchführung eines Werks; ein Erfolg ist geschuldet', 'Bauleistungen, Software, Wartung, Umbau, Reparatur'],
                                                     ['Dienstvertrag (§§ 611 ff. BGB)', 'Bereitstellung von Arbeitskraft; ergebnisunabhängig', 'Beratung, Arbeitnehmer']])
        + p('Hauptleistungspflichten bei Kauf- bzw. Werkvertrag: Lieferant: Übergabe und Eigentumsverschaffung bzw. Herstellung des Werks, Freiheit von Sach- und Rechtsmängeln; Kunde: Abnahme und Zahlung der vereinbarten Vergütung.')
        + h3('Sonderregelungen für Kaufleute')
        + liste(['<b>Wareneingangsprüfung (§ 377 HGB)</b> zwingend: Untersuchung bei Anlieferung auf Menge und Identität, Transportschäden, offenkundige Mängel. Werden Mängel nicht unverzüglich gerügt, wird der Käufer so behandelt, als sei die Ware ordnungsgemäß geliefert. Ausschluss nur zulässig, wenn mindestens gleichwertige Qualitätssicherung erfolgt (Zertifizierung, Audit, regelmäßige Kontrolle).',
                 '<b>Kaufmännisches Bestätigungsschreiben</b>: Wird der Inhalt einer mündlichen Vereinbarung schriftlich bestätigt, ist der Empfänger Kaufmann und widerspricht er nicht unverzüglich, wird der Inhalt zum Vertragsinhalt, selbst wenn etwas anderes besprochen wurde. Ausnahme: bewusst falsche Wiedergabe. Anwendung: mündliche Vereinbarungen jeder Art (Bestellungen, Spezifikationen, Änderungen). Keine Gegenzeichnung fordern! Nicht in allen Rechtsordnungen bekannt.'])
        + spiel('sp-vertrag', 'Kauf-, Werk- oder Dienstvertrag?', ['Kauf', 'Werk', 'Dienst'], [
            ('500 Sättel ab Lager', 0, 'Eigentum an beweglichen Sachen.'), ('Reparatur der Lackieranlage', 1, 'Erfolg geschuldet.'), ('Programmierung einer Lagersoftware', 1, 'Unkörperliches Werk.'),
            ('Beratertage für ein Einkaufsprojekt', 2, 'Tätigkeit, ergebnisunabhängig.')]),
    merk='Vertrag = Angebot + Annahme; „ja, aber“ = Ablehnung + Gegenangebot. Formfrei (mündlich, E-Mail, konkludent), Schriftform für Beweis. Rangfolge: individuell > AGB > Gesetz. Kauf § 433 (Eigentum), Werk § 631 (Erfolg), Dienst § 611 (Tätigkeit). § 377 HGB: Ware sofort prüfen und rügen, sonst genehmigt. Kfm. Bestätigungsschreiben: Schweigen = Zustimmung.',
    exam='Vertragsschluss, Rangfolge, Vertragsarten, § 377 HGB, kaufmännisches Bestätigungsschreiben (Multiple Choice).',
    fehler=['Glauben, Verträge bräuchten immer Schriftform.', 'Werk- und Dienstvertrag verwechseln: Werk = Erfolg, Dienst = Tätigkeit.'],
    src='Folien 237–251')

# ---------------------------------------------------------------- 5 TCO und Einstandspreis
EP = [('Nettoangebotspreis', 1200.00, 'start'), ('+ Zuschläge (z. B. Mindermenge)', 52.00, '+'), ('− Rabatte (2 % Kundenrabatt)', -25.04, '−'), ('= bereinigter Einkaufspreis', 1226.96, '='),
      ('− Skonto (3 %)', -36.81, '−'), ('+ Fracht', 26.00, '+'), ('+ Verpackung', 12.50, '+'), ('+ Versicherung', 5.20, '+'), ('+ Zoll', 0.00, '+'), ('= Einstandspreis', 1233.85, '=')]
assert round((1200 + 52) * 0.02, 2) == 25.04 and round(1226.96 * 0.03, 2) == 36.81
assert round(1226.96 - 36.81 + 26 + 12.5 + 5.2, 2) == 1233.85

t_tco = thema('tco', 'Total Cost of Ownership und Einstandspreis',
    kern='TCO betrachtet neben den direkten Kosten auch alle indirekten Kosten über die gesamte Besitzphase (Beschaffung, Nutzung, Betrieb). Basis des Angebotsvergleichs ist der Einstandspreis = Nettolistenpreis − Preisnachlässe + Bezugsnebenkosten. „Landed Cost“ umfasst Teilepreis, Werkzeug- und Nebenkosten, Währung, Verpackung, Versicherung, Transport, Zölle und Zahlungsbedingungen; dazu kommen Qualitätskosten, Kapitalbindung, Bezugsrisiken und Kosten der Lieferantensuche und -entwicklung. Entscheidung: TCO und Risiko gemeinsam bewerten.',
    kurz=p('Ein Lieferant in China bietet den Gepäckträger für 17,72 € statt 21,50 € aus Deutschland an. Billiger? Erst wenn Fracht, Zoll, Wechselkurs, längere Lieferzeit, Kapitalbindung, Qualitätsrisiken und Reisekosten fürs Audit dazukommen, sieht man die <b>Total Cost of Ownership</b>.')
        + p('Merksätze der Folie: „Wer billig kauft, kauft zweimal.“ „Billig ist nicht günstig.“'),
    fig=fw('Vom Angebotspreis zum Einstandspreis (Folienbeispiel). Tippe auf die Zeilen.')
        + bild(svg(360, 300, ''.join(box(4, 4 + i * 29, 224, 25, k, size=12, art='hl' if k.startswith('= Ein') else ('pale' if k.startswith('=') else 'card'),
                                         tip={'start': 'Nettoangebotspreis des Lieferanten.', '+': 'Bezugsnebenkosten bzw. Zuschläge erhöhen den Preis.', '−': 'Preisnachlässe: Rabatt (sofort), Bonus (nachträglich), Skonto (bei Zahlung innerhalb einer Frist).', '=': 'Zwischensumme.'}[o])
                                     + T(352, 21 + i * 29, f'{v:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.'), 13, 700, 'end') for i, (k, v, o) in enumerate(EP)),
                       'Einstandspreis', maxw=420)),
    figcap='nach Folie „Einstandspreis – Ausgangsbasis für den Angebotsvergleich“',
    article=h3('Begriff')
        + p('<b>Total Cost of Ownership: Neben den direkten Kosten für die Güter werden auch alle indirekten Kosten betrachtet.</b> „Total“ bezeichnet eine vollständige Sichtweise und zielt auf die Erfassung aller Kosten; „Ownership“ zielt auf die gesamte Besitzphase (Beschaffungs-, Nutzungs- und Betriebsphase; alternativ Entwicklung, Vermarktung, Service, Entsorgung). Produktpreis ist nicht gleich Gesamtkosten.')
        + h3('Einstandspreis')
        + fx('Einstandspreis', r'\text{Einstandspreis} = \text{Nettolistenpreis} - \text{Preisnachlässe} + \text{Bezugsnebenkosten}', 'Rabatte, Boni, Skonti abziehen; Fracht, Verpackung, Versicherung, Zoll addieren', '1.233,85 €')
        + bsp('Folienbeispiel', 'Angebot 1.200 €, Mindermengenzuschlag 52 €, 2 % Kundenrabatt, 3 % Skonto, Fracht 26 €, Verpackung 12,50 €, Versicherung 5,20 €, Zoll 0 €', [
            ('bereinigter Einkaufspreis', '(1.200 + 52) − 2 % = 1.252 − 25,04 = 1.226,96 €'), ('Skonto', '3 % von 1.226,96 = 36,81 €'), ('Einstandspreis', '1.226,96 − 36,81 + 26 + 12,50 + 5,20 + 0 = 1.233,85 €')],
            'Rabatt: sofortiger Preisnachlass (z. B. Mengenrabatt); Bonus: nachträglich gewährt; Skonto: Abzug bei Zahlung innerhalb einer bestimmten Frist.')
        + h3('Vom Teilepreis zu den TCO')
        + tabelle(['Kostenblock', 'Bestandteile'], [
            ['„Landed Cost“', 'Teilepreis (in lokaler Währung), Werkzeug- und Nebenkosten, Währungs-/Währungssicherungskosten, Verpackung, Versicherungen, Transport, Zölle und Abgaben, Zahlungsbedingungen'],
            ['Lieferantenentwicklung', 'Lieferantensuche, -bewertung, -auswahl, -auditierung/-freigabe'],
            ['weitere', 'Wareneingangsprüfung, Lagerung und Handling, Qualitätskosten, Kommunikations- und Reisekosten, Kapitalbindung, Bezugsrisiken']])
        + p('Qualifizierter Vergleich der Landed Cost: Teilepreis ggf. in alternativer Währung anfragen; Werkzeug- und Nebenkosten über strukturierte RFQ-Formulare bzw. einheitliches Lastenheft; konzernweit einheitliche Referenzkurse; Transport, Versicherung und Zoll nach den vereinbarten <b>Incoterms</b>; Zahlungsbedingungen normiert anfragen bzw. vergleichbar rechnen.')
        + h3('Problembereiche')
        + liste(['<b>(Auslands-)Bezugsrisiko</b>: politische Handelshemmnisse, Naturkatastrophen, innere Unruhen, Krieg, Streiks, Rohstoff- und Arbeitskräfteverfügbarkeit, Zahlungs- und Währungsrisiken, rechtliche Risiken, Transportrisiken, nicht-tarifäre Hemmnisse, Kommunikationsrisiken. In Relation zu lokalen Bezügen setzen, z. T. über einen Ländermultiplikator.',
                 '<b>Qualitätskosten</b>: Bestandteile genau definieren, von benachbarten TCO-Bestandteilen abgrenzen, Kennzahlen (z. B. PPM-Rate = parts per million) und Bonus-/Malus-Multiplikatoren festlegen; schwer quantifizierbar. Praxistipp: Kosten des Lieferantenmanagements separat erfassen.'])
        + h3('TCO in der Vergabeentscheidung')
        + p('TCO ist in den Einkaufsgrundsätzen als Entscheidungskriterium verankert; systematischer Vergleich mit normierten Angebotsvergleichsblättern und standardisierten Tools (zentral gepflegte Werte wie Frachten, Wechselkurse, Stundensätze); multipersonelle Entscheidung im Buying-Center (Einkauf, Technik, Entwicklung, Qualität, Projektmanagement).')
        + bsp('Beispiel aus der Vorlesung: Reduzierhülse aus drei Regionen', 'Teilepreis Jahr 1 (je 100 Stück): Deutschland 23,70 €, Portugal 20,35 €, China 19,20 €', [
            ('Schritt 1: TCO-Vergleich', 'mit Werkzeugkosten, Fracht, Zoll, Währung: A 24,27 €, B 20,98 €, C 22,56 €'), ('Schritt 2: Kosten und Risiken relational vergleichen', 'China hat den niedrigsten Teilepreis, aber höhere TCO als Portugal und das höchste Qualitäts- und Lieferrisiko (nicht bewertet, Länderrisiko C)'),
            ('Schritt 3: ganzheitliche Entscheidung', 'Kosten-/Risikomatrix, Scoring-Modell: hier spricht viel für Portugal')], 'Der billigste Teilepreis ist nicht automatisch die beste Vergabe.'),
    merk='TCO = direkte + indirekte Kosten über die ganze Besitzphase. Einstandspreis = Nettolistenpreis − Nachlässe (Rabatt, Bonus, Skonto) + Bezugsnebenkosten (Fracht, Verpackung, Versicherung, Zoll); Beispiel 1.233,85 €. Landed Cost: Teilepreis, Werkzeug, Währung, Verpackung, Versicherung, Transport, Zoll, Zahlungsbedingungen. Problembereiche: Bezugsrisiken, Qualitätskosten. Entscheidung: TCO + Risiko, Buying-Center.',
    exam='Einstandspreis berechnen; TCO-Bestandteile nennen; billigster Teilepreis vs. TCO begründen.',
    fehler=['Skonto vom Nettoangebotspreis statt vom bereinigten Einkaufspreis rechnen.', 'TCO mit Einstandspreis gleichsetzen: TCO ist umfassender.'],
    src='Folien 254–266')

# ---------------------------------------------------------------- 6 Incoterms
grp = [('E', 'EXW', 'Abholklausel: Käufer holt ab Werk ab, trägt alle Kosten und Risiken.'),
       ('F', 'FCA FAS FOB', 'Absendeklauseln ohne Übernahme der Haupttransportkosten durch den Verkäufer.'),
       ('C', 'CFR CIF CPT CIP', 'Absendeklauseln mit Übernahme der Haupttransportkosten durch den Verkäufer (Gefahr geht trotzdem früh über).'),
       ('D', 'DAP DAT DDP', 'Ankunftsklauseln: Verkäufer liefert bis zum Bestimmungsort; DDP ist die Maximalverpflichtung.')]
fig_inco = svg(360, 250,
    ''.join(box(4 + i * 89, 60, 82, 90, f'{g}\n{k.replace(" ", chr(10))}', size=12, art='hl' if g == 'D' else 'card', tip=f'Gruppe {g}: {t}') for i, (g, k, t) in enumerate(grp))
    + pfeil(8, 180, 352, 180) + T(8, 200, 'Verkäufer trägt wenig', 12, 600, 'start', 'var(--muted)') + T(352, 200, 'Verkäufer trägt viel', 12, 600, 'end', 'var(--muted)')
    + T(180, 30, 'Pflichten und Kosten des Verkäufers', 13, 800)
    + T(180, 232, 'EXW: Käufer trägt alles · DDP: Verkäufer trägt alles', 12, 400, fill='var(--muted)'),
    'Incoterms-Gruppen', maxw=420)

t_inco = thema('incoterms', 'Incoterms im TCO-Vergleich',
    kern='Incoterms regeln, wer Transport, Versicherung, Zoll und Gefahr trägt, und bestimmen damit die Landed Cost. Gruppen: E (EXW, Abholklausel), F (FCA, FAS, FOB: Absendeklauseln ohne Haupttransport), C (CFR, CIF, CPT, CIP: Absendeklauseln mit Haupttransportkosten durch den Verkäufer), D (Ankunftsklauseln, DAP, DDP). FAS, FOB, CFR, CIF nur für See- und Binnenschifffahrt. Empfehlung der Folie: FCA (gut für Container, alle Transportarten) und DDP (Maximalverpflichtung des Verkäufers).',
    kurz=p('Zwei Angebote für Gepäckträger: 18 € „EXW Shanghai“ und 21 € „DDP Mannheim“. Beim ersten muss die Neckarrad GmbH Transport, Versicherung und Zoll selbst bezahlen und organisieren, beim zweiten liefert der Lieferant verzollt vor die Tür. Ohne Incoterms kann man Angebote gar nicht vergleichen.'),
    fig=fw('Vier Gruppen, von „Käufer trägt alles“ bis „Verkäufer trägt alles“. Tippe auf die Gruppen.') + bild(fig_inco),
    figcap='nach Folien „TCO-Vergleich auf Basis von INCOTERMS“',
    article=tabelle(['Gruppe', 'Klauseln', 'Bedeutung'], [
            ['E – Abholklausel', 'EXW (Ex Works, ab Werk)', 'Käufer holt ab und trägt alle Kosten und Risiken'],
            ['F – Absendeklauseln ohne Haupttransport', 'FCA (Free Carrier), FAS (Free Alongside Ship), FOB (Free On Board)', 'Verkäufer liefert an den Frachtführer bzw. ans/aufs Schiff; Haupttransport zahlt der Käufer'],
            ['C – Absendeklauseln mit Haupttransport', 'CFR (Cost and Freight), CIF (Cost, Insurance, Freight), CPT (Carriage Paid To), CIP (Carriage and Insurance Paid To)', 'Verkäufer zahlt den Haupttransport (CIF/CIP auch Versicherung)'],
            ['D – Ankunftsklauseln', 'DAP (Delivered At Place), DAT (Delivered At Terminal; seit 2020 DPU), DDP (Delivered Duty Paid)', 'Verkäufer liefert bis zum Bestimmungsort; DDP inklusive Einfuhrverzollung']])
        + p('Für alle Transportarten (auch kombiniert): EXW, FCA, CPT, CIP, DAP, DAT, DDP. Nur See- und Binnenschifffahrt: FAS, FOB, CFR, CIF.')
        + h3('Empfehlungen der Folie')
        + liste(['<b>FCA (Frei Frachtführer, benannter Übergabeort)</b>: Der Verkäufer bringt die Ware zum vom Käufer bestimmten Lieferort, sorgt auf seine Kosten für Verpackung, Warenprüfung und Ausfuhrfreimachung und belädt ggf.; Haupttransport, Durchfuhr und Einfuhr verantwortet der Käufer. Für alle Transportarten, sehr gut für Container.',
                 '<b>DDP (Geliefert verzollt)</b>: Maximalverpflichtung des Verkäufers. Er macht die Ware zur Aus- und Einfuhr frei, liefert unentladen am benannten Bestimmungsort und trägt alle Kosten und die Gefahr bis dahin.'])
        + spiel('sp-inco', 'Welche Gruppe?', ['E', 'F', 'C', 'D'], [('EXW', 0, 'Abholklausel.'), ('FOB', 1, 'Frei an Bord: ohne Haupttransport.'), ('CIF', 2, 'Kosten, Versicherung, Fracht bezahlt.'), ('DDP', 3, 'Geliefert verzollt.'), ('FCA', 1, 'Frei Frachtführer.'), ('CPT', 2, 'Frachtfrei.')]),
    merk='Incoterms bestimmen Transport-, Versicherungs-, Zollkosten und Gefahrübergang → nötig für den TCO-Vergleich. E: EXW (Käufer trägt alles). F: FCA, FAS, FOB (ohne Haupttransport). C: CFR, CIF, CPT, CIP (Verkäufer zahlt Haupttransport). D: DAP, DAT, DDP (bis Bestimmungsort; DDP = Maximum). FAS/FOB/CFR/CIF nur Schiff. Empfehlung: FCA, DDP.',
    exam='Incoterms Gruppen zuordnen; EXW vs. DDP; Bedeutung für den TCO-Vergleich.',
    fehler=['Bei C-Klauseln annehmen, die Gefahr gehe erst am Ziel über: Der Verkäufer zahlt zwar den Transport, die Gefahr geht aber schon beim Versand über.'],
    src='Folien 261–262')

# ---------------------------------------------------------------- 7 KSA
ZK = [('Materialeinzelkosten', 50.00), ('+ Materialgemeinkosten (8 %)', 4.00), ('= Materialkosten', 54.00), ('Fertigungslohn Kst 1', 5.00), ('+ 100 % FGK', 5.00), ('Fertigungslohn Kst 2', 6.00),
      ('+ 150 % FGK', 9.00), ('= Fertigungskosten', 25.00), ('= Herstellkosten', 79.00), ('+ Verwaltungs-GK 9 % auf HK', 7.11), ('+ Vertriebs-GK 6 % auf HK', 4.74), ('+ Wagnis 1 % auf HK', 0.79),
      ('= Selbstkosten', 91.64), ('+ Gewinn 10 %', 9.16), ('= Verkaufspreis ab Werk netto', 100.80)]
assert round(79 * .09, 2) == 7.11 and round(79 * .06, 2) == 4.74 and round(79 * .01, 2) == 0.79 and round(91.64 * .1, 2) == 9.16

t_ksa = thema('ksa', 'Kostenstrukturanalyse (KSA) und Zuschlagskalkulation',
    kern='Die Kostenstrukturanalyse zerlegt den Preis eines Teils in seine Kostenbestandteile (Cost Break Down), um Kostentreiber zu erkennen und Material- und Prozesskosten zu senken. Grundlage ist die Kostenrechnung: Kostenartenrechnung (welche Kosten?), Kostenstellenrechnung (wo?), Kostenträgerrechnung (wofür?) – Eselsbrücke AST. Kalkulation per Zuschlagskalkulation (Materialkosten + Fertigungskosten = Herstellkosten; + Verwaltungs- und Vertriebs-GK = Selbstkosten; + Gewinn = Verkaufspreis) oder mit Maschinenstundensätzen.',
    kurz=p('Ein IKEA-Beistelltisch kostet 9,99 €. Ohne Mehrwertsteuer, Gewinn und Vertriebskosten bleiben gut 6,60 € Herstellkosten. Wie geht das? Die Tischplatte ist innen hohl, mit einer Wabenstruktur aus Karton: leicht, billig, nachhaltig, nur nicht schalldicht.')
        + p('Genau so denkt die <b>KSA</b>: Woraus besteht der Preis, und wo sind die Kostentreiber? Mit einer <b>Zuschlagskalkulation</b> rechnet der Einkauf nach, was ein Teil kosten dürfte, und hat Argumente für die Verhandlung.'),
    fig=fw('Zuschlagskalkulation auf Basis Fertigungslohn (Folienbeispiel). Tippe auf die Zeilen.')
        + bild(svg(360, 15 * 22 + 8, ''.join(box(4, 4 + i * 22, 236, 19, k, size=12, bold=700 if k.startswith('=') else 400, rx=5,
                                                art='hl' if k.startswith('= Verk') else ('pale' if k.startswith('=') else 'card'),
                                                tip={'Materialeinzelkosten': 'Direkt zurechenbares Fertigungsmaterial.', '+ Materialgemeinkosten (8 %)': 'Zuschlag auf die Materialeinzelkosten: 8 % von 50 = 4 €.',
                                                     '+ 100 % FGK': 'Fertigungsgemeinkosten der Kostenstelle 1: 100 % auf deren Fertigungslohn.', '+ 150 % FGK': 'Fertigungsgemeinkosten der Kostenstelle 2: 150 % von 6 € = 9 €.',
                                                     '= Herstellkosten': 'Materialkosten + Fertigungskosten = 54 + 25 = 79 €.', '+ Verwaltungs-GK 9 % auf HK': '9 % von 79 = 7,11 €.',
                                                     '+ Vertriebs-GK 6 % auf HK': '6 % von 79 = 4,74 €.', '+ Wagnis 1 % auf HK': '1 % von 79 = 0,79 €.', '= Selbstkosten': '79 + 7,11 + 4,74 + 0,79 = 91,64 €.',
                                                     '+ Gewinn 10 %': '10 % auf die Selbstkosten = 9,16 €.', '= Verkaufspreis ab Werk netto': '91,64 + 9,16 = 100,80 €.'}.get(k, k))
                                            + T(352, 18 + i * 22, f'{v:.2f}'.replace('.', ','), 12, 700 if k.startswith('=') else 400, 'end') for i, (k, v) in enumerate(ZK)),
                       'Zuschlagskalkulation', maxw=420)),
    figcap='nach Folie „Zuschlagskalkulation auf Basis Fertigungslohn“',
    article=h3('Motivation')
        + p('„It is not the employer who pays the wages … It is the customer who pays the wages.“ (Henry Ford) Der Kunde kauft nur Produkte, die seine Bedürfnisse unter besonderer Berücksichtigung des Preises erfüllen. Daher Kostenmanagement: <b>Kostentreiber im MGM identifizieren, Material- und Prozesskosten senken.</b>')
        + p('Wesentliche Kostentreiber der Herstellkosten nach Funktion: Forschung und Entwicklung (Design/Layout, Materialwahl, Spezifikationen, Technologie, Entwicklungsdauer, Investitionen), Fertigung (Prozessgestaltung, Rüstkosten, Auslastung, Zykluszeit, Ausschuss), Einkauf (Einkaufspreis, Lieferantenqualität, Prozesse, Logistik).')
        + h3('Aufbau der Kostenrechnung (AST)')
        + tabelle(['Stufe', 'Frage'], [['Kostenartenrechnung', 'Welche Kosten sind angefallen? Einzelkosten (direkt zurechenbar: Material, Fertigungslöhne) und Gemeinkosten (indirekt: Werbung, Entwicklung)'],
                                       ['Kostenstellenrechnung', 'Wo sind die Kosten angefallen? (Betriebsabrechnungsbogen, BAB)'], ['Kostenträgerstückrechnung (Kalkulation)', 'Wofür sind die Kosten angefallen?'],
                                       ['Kostenträgerzeitrechnung (Betriebsergebnisrechnung)', 'Wie hoch waren Kosten und Erfolg der Periode?']])
        + p('<b>Sechs originäre Kostenarten:</b> Materialkosten, Maschinen-/Anlagenkosten (Abschreibungen), Personalkosten, Kapitalkosten (kalkulatorische Zinsen), Fremdleistungskosten, kalkulatorische Wagniskosten. Materialkosten = Materialeinzelkosten (Rohstoffe, Einzelteile, Baugruppen) + Materialgemeinkosten (Disposition, Einkauf, Wareneingang und Kontrolle, Werkstoffprüfung, innerbetrieblicher Transport, Eingangslagerung).')
        + p('Fix oder variabel? Variabel: direktes Material, Fertigungslöhne, Energie (z. T.); fix (unabhängig von der Menge): Gebäude/Miete, Abschreibungen und Kapitalkosten der Anlagen, Planung/Verwaltung, Meister, Wartung.')
        + h3('Zuschlagskalkulation')
        + p('Die Gemeinkosten werden über den BAB den Kostenstellen zugerechnet und als prozentuale Zuschläge auf die Einzelkosten verteilt (abgeleitet vom Branchendurchschnitt bzw. aus Kalkulationssoftware).')
        + fluss([('Materialkosten', 'Fertigungsmaterial + Materialgemeinkosten'), ('+ Fertigungskosten', 'Fertigungslöhne + Fertigungsgemeinkosten + Sondereinzelkosten der Fertigung'), ('= Herstellkosten', ''),
                 ('+ Verwaltungs- und Vertriebs-GK', '% auf Herstellkosten'), ('= Selbstkosten', ''), ('+ Gewinn', '% auf Selbstkosten'), ('= Barverkaufspreis → + Erlösschmälerungen (Skonto) = Nettoverkaufspreis', '')], hl=2)
        + tabelle(['Zuschlag (Erfahrungswerte)', 'Größenordnung', 'Bezugsbasis'], [['Materialgemeinkosten', '5–10 %', 'Material-EK'], ['Fertigungs-GK bei Maschinenstundensatz', '10–20 %', 'Fertigungs-EK'],
                                                                            ['Fertigungs-GK bei mechanischer Bearbeitung', '80–110 %', 'Fertigungslöhne'], ['Verwaltungs-/Vertriebs-GK', '10–35 %', 'Herstellkosten'],
                                                                            ['Wagnis Material und Fertigung', '0,5–2 %', 'Herstellkosten'], ['Entwicklungs-GK', '10–15 %', 'Herstellkosten'], ['Gewinn', '5–10 %', 'Herstellkosten']])
        + h3('Kalkulation mit Maschinenstundensätzen')
        + p('Statt Fertigungslohn + FGK werden Maschinenkosten je Fertigungsschritt (inkl. Löhne) angesetzt: Maschinenstundensatz × Taktzeit + Lohnkosten + Restfertigungsgemeinkosten. Bestandteile des Maschinenstundensatzes: Abschreibung (Investitionssumme / Gesamtstundenleistung; meist der größte Brocken), Instandhaltung (Pauschale in % der Investition), kalkulatorische Zinsen (z. B. 6 % auf die halbe Investitionssumme / Jahresstunden), Raumkosten (Fläche × kalk. Miete / Stunden), Energie (kWh/h × €/kWh), Lohnkosten (Mitarbeiter × Stundenlohn).')
        + h3('KSA in der Einkaufspraxis: Schritte zur Einführung')
        + liste(['einheitliches Anfrageschema für den strukturierten Angebotsvergleich', 'firmeninterne Kalkulationsrichtlinien', 'Materialgruppenexperten und Know-how-Netzwerk', 'Wissensdatenbank', 'Kalkulationsprogramm', 'Einsatz beim Lieferanten'])
        + h3('Kostentransparenz durch KSA – Lessons Learned')
        + tabelle(['Erkenntnis', 'Was folgt daraus?'], [
            ['Kostentreiber identifizieren und verstehen', 'Ansatzpunkte für Verhandlung und technisches Ratio (Rationalisierung)'],
            ['Kostentreiber als Ansatzpunkte für <b>Design-to-Cost</b>', '<b>Early Involvement</b>: Kosten bereits in der Entwicklungsphase beeinflussen und senken'],
            ['Ansatzpunkte für Innovationen von Lieferantenseite und aus anderen Branchen aufnehmen', '<b>Querdenken!</b>']])
        + p('Einfach gesagt: Wer weiß, woraus der Preis besteht, kann besser verhandeln, das Teil schon in der Entwicklung billiger konstruieren lassen (Design-to-Cost: das Produkt wird auf einen Zielkostenrahmen hin entwickelt) und Ideen von außen übernehmen.')
        + zusatz('Die Folien zu den einzelnen Einführungsschritten (strukturiertes Anfrageschema, Kalkulationsrichtlinien, Experten-Netzwerk, Wissensdatenbank) und zu den Kostentreibern Material, Maschine und Personal (Börsenpreise, Maschinenstundensatz, Tarifverträge als Datenquelle) wurden in der Vorlesung ausgeklammert. Zur Einordnung: Bei Materialkosten helfen Börsenpreise, Recyclat und Konvoi-Verhandlung (Mengenbündelung), bei Maschinenkosten realistische Abschreibungs- und Instandhaltungsansätze, bei Personalkosten Mehrmaschinenbedienung und Aufteilung nach Qualifikationsniveau.')
        + falle('Den Gewinnzuschlag auf die Herstellkosten statt auf die Selbstkosten rechnen (im Schema: % auf Selbstkosten).'),
    merk='KSA = Cost Break Down: Kostentreiber finden, Material- und Prozesskosten senken. Lessons Learned: Kostentreiber verstehen (Verhandlung, technisches Ratio), Design-to-Cost/Early Involvement, Querdenken (Innovationen von Lieferanten und anderen Branchen). Kostenrechnung AST: Arten (welche), Stellen (wo, BAB), Träger (wofür). 6 Kostenarten: Material, Anlagen, Personal, Kapital, Fremdleistung, Wagnis. Zuschlagskalkulation: MEK + MGK = MK; FL + FGK = FK; MK + FK = HK (79); + VwGK, VtGK, Wagnis = SK (91,64); + Gewinn = VK (100,80). Alternativ Maschinenstundensätze.',
    exam='Kostenrechnungsstufen und Kostenarten; Zuschlagskalkulation durchrechnen oder ergänzen.',
    fehler=['Gemeinkostenzuschläge auf die falsche Basis rechnen.', 'Herstellkosten und Selbstkosten verwechseln.'],
    src='Folien 267–294, 302')

# ---------------------------------------------------------------- 8 LPP
PUNKTE = [(1.0, 2.1), (1.5, 2.4), (2.0, 3.6), (2.4, 2.9), (3.0, 3.4), (3.2, 4.6), (3.8, 3.9), (4.2, 4.3), (4.5, 5.9), (5.0, 4.8), (5.5, 5.1), (6.0, 6.9), (6.3, 5.6), (7.0, 6.2), (7.4, 7.9), (8.0, 6.8)]
n = len(PUNKTE); mx = sum(x for x, _ in PUNKTE) / n; my = sum(y for _, y in PUNKTE) / n
B = sum((x - mx) * (y - my) for x, y in PUNKTE) / sum((x - mx) ** 2 for x, _ in PUNKTE); A = my - B * mx
RES = sorted(PUNKTE, key=lambda p: p[1] - (A + B * p[0]))[:max(4, n // 5)]
m2x = sum(x for x, _ in RES) / len(RES); m2y = sum(y for _, y in RES) / len(RES)
B2 = sum((x - m2x) * (y - m2y) for x, y in RES) / sum((x - m2x) ** 2 for x, _ in RES); A2 = m2y - B2 * m2x

def lpp_svg():
    X = lambda x: 50 + x * 36
    Y = lambda y: 214 - y * 23
    s = achsen(50, 214, 352, 14, 'Kostentreiber (z. B. Gewicht)', '') + T(58, 16, 'Preis', 12, 600, 'start', 'var(--muted)')
    for x, y in PUNKTE:
        teuer = y - (A + B * x) > 0.6
        s += tpg(punkt(X(x), Y(y), 'var(--primary-2)' if teuer else 'var(--muted)', 4.5), f'Teil mit Kostentreiber {x:.1f} und Preis {y:.1f}' + (': deutlich über der Durchschnittslinie, Kandidat für Nachverhandlung.' if teuer else '.'))
    s += tpg(linie([(X(0.6), Y(A + B * 0.6)), (X(8.2), Y(A + B * 8.2))], 'var(--primary)', 2.4), f'Durchschnittspreislinie (lineare Regression über alle Teile): y = {A:.2f} + {B:.2f}·x.')
    s += tpg(linie([(X(0.6), Y(A2 + B2 * 0.6)), (X(8.2), Y(A2 + B2 * 8.2))], 'var(--axis)', 2.2, True), 'Best-Practice-Linie: Regression über die besten 20 % der Preis-Kostentreiber-Relationen; liegt immer unterhalb der Durchschnittslinie. Benchmark und Zielpreis.')
    s += linie([(64, 36), (90, 36)], 'var(--primary)', 2.4) + T(96, 40, 'Durchschnittslinie', 12, 700, 'start', 'var(--primary)') + linie([(64, 56), (90, 56)], 'var(--axis)', 2.2, True) + T(96, 60, 'Best-Practice-Linie', 12, 700, 'start')
    return svg(360, 240, s, 'LPP: Durchschnitts- und Best-Practice-Linie', maxw=420)

t_lpp = thema('lpp', 'Linear Performance Pricing (LPP)',
    kern='LPP ist ein datengetriebener, statistischer Ansatz, um Teile mit (zu) hohen Preisen zu identifizieren. Grundannahme: linearer Zusammenhang zwischen dem Hauptkostentreiber (z. B. Gewicht) und dem Preis; per linearer Regression y = a + b·x entsteht die Durchschnittspreislinie, aus den besten 20 % die Best-Practice-Linie als Benchmark. Teile weit über der Linie sind Kandidaten für Nachverhandlungen. Empfehlung: LPP als erstes Screening, KSA zur Detailanalyse ausgewählter Teile.',
    kurz=p('Die Neckarrad GmbH kauft 80 verschiedene Kunststoffteile. Je schwerer ein Teil, desto teurer, im Großen und Ganzen. Trägt man Preis über Gewicht auf und legt eine <b>Regressionsgerade</b> durch die Punktewolke, fallen Teile auf, die deutlich <b>über der Linie</b> liegen: zu teuer für ihr Gewicht.')
        + p('Mit der <b>Best-Practice-Linie</b> (die besten 20 %) hat der Einkauf sogar einen Zielpreis für die Verhandlung, ohne jedes Teil im Detail kalkulieren zu müssen.'),
    fig=fw('Preis über Kostentreiber. Tippe auf Punkte und Linien.') + bild(lpp_svg()),
    figcap='nach Folien „Durchschnitts-Preis-Linie“ und „Best-Practice-Linie als Benchmark“ (eigene Beispieldaten)',
    article=h3('Was ist LPP?')
        + liste(['datengetriebene Methode, um Einsparpotenziale zu identifizieren; Grundlage ist die statistische Regressionsanalyse', 'Grundannahme: linearer Zusammenhang zwischen dem (Haupt-)Kostentreiber und der Wertgröße, i. d. R. dem Preis',
                 'Einsatz: statistische Analyse vieler ähnlicher Teile, Identifizierung von Teilen mit Einsparpotenzial auf Teilenummernebene, Referenzgröße zur Bewertung von Angeboten, Vergleich von Anbietern und Regionen'])
        + h3('Lineare Regression')
        + fx('Regressionsgerade', r'y = a + b \cdot x', 'x = unabhängige Variable (Kostentreiber), y = abhängige Variable (Preis), a = Achsenabschnitt, b = Steigung', 'Methode der kleinsten Quadrate')
        + p('Die Regression legt die Gerade mit dem geringstmöglichen Abstand zu allen Punkten: Die vertikalen Abweichungen werden quadriert und summiert (positive und negative heben sich so nicht auf) und diese Summe wird minimiert.')
        + h3('Durchschnitts- und Best-Practice-Linie')
        + gegen(('Durchschnittspreislinie', 'Regression über alle Teile; bei positiver Korrelation gilt: je größer der Kostentreiber, desto höher der Preis'),
                ('Best-Practice-Linie', 'Regression über die besten 20 % der Preis-Kostentreiber-Relationen; liegt immer unterhalb der Durchschnittslinie; Benchmark'))
        + h3('Schritte')
        + fluss([('Produktgruppe definieren', 'ähnliche Funktionen oder Herstellungsprozesse'), ('Treiber identifizieren', 'Performance-Parameter'), ('Daten erheben', 'technische Daten (unabhängig) und Preise (abhängig)'),
                 ('Daten analysieren', 'Regression, kritische Prüfung, ggf. Rekursionen, tiefergehende Analysen'), ('Maßnahmen ableiten', '')], hl=4)
        + p('<b>Anforderungen:</b> Der Hauptkostentreiber muss für alle analysierten Teile gleich, leicht verfügbar und messbar sein (z. B. Gewicht bei Kunststoff-, Sinter-, Aluminiumteilen, Volumen bei Kühlmodulen, Druck bei Pumpen, Länge bei Stahlstäben) und positiv mit den Kostenelementen korrelieren (mehr Gewicht → längere Zykluszeit, höherer Maschinenstundensatz, mehr Handling, mehr Lagerkosten). Daten: verlässlich, vergleichbar, vollständig, mindestens 20 Teile je Cluster.')
        + p('Analyse: Unterscheiden sich die Teile über der Linie erheblich? Wenn nicht, warum sind sie teurer? → Argumente für Neuverhandlungen. Auswertung nach Lieferanten (wettbewerbsfähige für Verhandlungen, neue aufbauen), Business Units/Regionen, Teilefamilien und Ländern. <b>Basis für Sourcing- und Verhandlungsstrategien.</b>')
        + h3('Vorteile von LPP')
        + liste(['intuitiver Top-down-Ansatz, Zusammenhang Preis–Kostentreiber wird sichtbar', 'einfacher Vergleich ähnlicher Teile, schnelle Identifikation zu teurer Teile', 'Preisanalysen ohne detaillierte Kenntnis der Fertigungsprozesse',
                 'Plausibilitätscheck von Angeboten, einfache Berechnung von Zielpreisen', 'zusätzliche Argumente für Verhandlungen, transparente Ziele'])
        + h3('KSA oder LPP?')
        + tabelle(['', 'KSA', 'LPP'], [['Ansatz', 'detaillierter Cost Break Down je Teil', 'umfangreicher Preisvergleich innerhalb einer Materialgruppe'], ['Stärke', 'Besonderheiten einzelner Teile werden berücksichtigt', 'hoher Automatisierungsgrad, geringer Aufwand je Teil'],
                                       ['Schwäche', 'sehr hoher Aufwand je Teil, hohe Anforderungen an Know-how', 'Datenverfügbarkeit u. U. kritisch; verallgemeinernd']])
        + p('<b>Empfehlung: LPP als erstes Screening und KSA zur Detailanalyse bei ausgesuchten Bezugsteilen.</b> Nicht-lineares Performance Pricing (NLPP) bildet nichtlineare Zusammenhänge ab, ist aber sehr anspruchsvoll und schwer vermittelbar. Methodeneinsatz im MGM (Umfrage unter Einkäufern): Standardansätze sind weit verbreitet; schwach eingesetzt werden elektronische Ausschreibungen und Auktionen, LPP und Reverse Engineering; Cost Break Down wird von über 30 % noch unzureichend eingesetzt; Verbrauchsoptimierungen sind ausbaufähig. <b>Großes Potenzial bei LPP und Methoden zur Verbrauchsreduzierung.</b>')
        + h3('Fallstudie: LPP als Basis für eine Materialgruppenstrategie')
        + p('In der Vorlesung wird LPP in einer Gruppenarbeit angewendet: <b>Analyse einer Materialgruppe und Vorschläge für eine MG-Strategie sowie Maßnahmen zur Umsetzung.</b> Grundlage ist ein LPP-Diagramm (Preis je 100 Stück über dem Kostentreiber) mit Durchschnitts- und Best-Practice-Linie.')
        + fluss([('1', 'Analysieren Sie zunächst die Materialgruppe (LPP-Diagramm deuten: Ausreißer, Lieferanten, Regionen)'), ('2', 'Definieren Sie strategische Ziele für die Materialgruppe'),
                 ('3', 'Stellen Sie Maßnahmen auf, mit denen Sie Ihre Ziele erreichen wollen, und bewerten Sie die Maßnahmen'), ('4', 'Bereiten Sie eine kurze Präsentation Ihrer Ergebnisse vor')], hl=1)
        + p('Das Vorgehen folgt dem Kreislauf der Materialgruppenstrategie: Analyse der Ausgangssituation → MG-Strategie → operative Umsetzung/Maßnahmen → MGM-Ziele → Controlling/Strategieüberprüfung. Eine durchgerechnete Fallstudie findest du bei den großen Aufgaben.'),
    merk='LPP: statistisch (lineare Regression y = a + b·x, x = Kostentreiber, y = Preis), Teile über der Durchschnittslinie = zu teuer; Best-Practice-Linie aus den besten 20 % = Benchmark/Zielpreis. Schritte: Produktgruppe, Treiber, Daten, Analyse, Maßnahmen. Treiber gleich, messbar, positiv korreliert; ≥ 20 Teile je Cluster. LPP = Screening, KSA = Detail.',
    exam='LPP erklären, Linien deuten, Vor- und Nachteile gegenüber KSA.',
    fehler=['x und y vertauschen: Der Preis ist die abhängige Variable.', 'Best-Practice-Linie über der Durchschnittslinie zeichnen.'],
    src='Folien 303–323, 306')

KAPITEL = kapitel('k7', 'Instrumente zur Strategieumsetzung',
    'Mit welchen Werkzeugen setzt der Einkauf die Strategie um? Early Involvement, Bündelung und Anfragen, Rahmenverträge und Vertragsrecht, TCO mit Incoterms, Kostenstrukturanalyse und Linear Performance Pricing.',
    ['Early Involvement', 'RFI/RFP/RFQ', 'Rahmenvertrag', 'Vertragsrecht', 'TCO', 'Incoterms', 'KSA', 'LPP'],
    [t_ei, t_rfx, t_rv, t_recht, t_tco, t_inco, t_ksa, t_lpp])
