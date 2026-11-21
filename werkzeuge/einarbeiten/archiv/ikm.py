"""Intercultural Management: Script-Wortlaut, der auf den Lernseiten fehlte, in den normalen Text eingearbeitet (Runde b1, 13.11.2026).
Format und Regeln: werkzeuge/einarbeiten.py. [[…]] = neu. Zweisprachig: englischer Text (l-en) im Wortlaut des Scripts, deutscher (l-de) sinngemäß."""
STAND = 'b1'
def zw(en, de): return f'<div class="zw2"><div class="l-en" lang="en">{en}</div><div class="l-de" lang="de">{de}</div></div>'
E = [
 # ---- Iceberg ----
 dict(t='iceberg', nach='<div class="zw2"><div class="l-en" lang="en"><h3>Above and below the water</h3></div><div class="l-de" lang="de"><h3>Über und unter Wasser</h3></div></div>',
      block=zw('<p><b>Culture</b> is a <b>complex and multilayered system</b>. It is often described with the help of the <b>iceberg model</b>. Above the water is what is visible, below the water is what is invisible.</p>',
               '<p><b>Kultur</b> ist ein <b>komplexes, vielschichtiges System</b>. Man beschreibt sie oft mit dem <b>Eisbergmodell</b>: Über Wasser liegt das Sichtbare, unter Wasser das Unsichtbare.</p>')),
]
