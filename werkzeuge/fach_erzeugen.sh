#!/bin/bash
# Erzeugt alle Inhaltsdateien eines Fachs neu, in der festen Reihenfolge (docs/update-2026-11-09/UPDATE.md, Teil B):
# Lernseite → Glossar → Fragen → Karten → Aufgaben → Probeklausur → Merklisten-Fragen → Klausurstil → Verständnis → Zeichnen → Aufräumen → Wichtig.
# Aufruf: bash werkzeuge/fach_erzeugen.sh <fach> [--nur-fach]
# Danach immer git diff --stat inhalte/<fach> prüfen: große Änderungen an fragen.json/karten.json heißen, dass ein Generator den Bestand umbaut.
set -e
f=$1; cd "$(dirname "$0")/.."
[ -f werkzeuge/$f/glossar.py ] && python3 werkzeuge/$f/glossar.py   # zuerst: „Weitere Begriffe“ im Bau braucht die ergänzten Begriffe
python3 werkzeuge/fachbau/bauen.py $f
for s in glossar fragen karten aufgaben klausur; do [ -f werkzeuge/$f/$s.py ] && python3 werkzeuge/$f/$s.py; done
python3 werkzeuge/begriffs_fragen.py $f
[ "$2" = "--nur-fach" ] && exit 0   # igt, ikm: nur die Fach-Skripte (die allgemeinen Generatoren verändern dort den Bestand)
python3 werkzeuge/merklisten_fragen.py $f
python3 werkzeuge/klausurstil.py $f
python3 werkzeuge/verstehen.py $f
python3 werkzeuge/zeichnen.py $f
python3 werkzeuge/fehler_fix.py $f
python3 werkzeuge/mc_kuerzen.py
python3 werkzeuge/wichtig.py $f
python3 werkzeuge/zielgroessen.py $f --kurz
python3 werkzeuge/abdeckung.py $f
