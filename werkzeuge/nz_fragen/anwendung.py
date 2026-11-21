"""Ersetzt Folienstoff-Fragen (:nz-), die eine Folien-Definition ein zweites Mal abgefragt hätten (je Begriff nur eine
Definitionsfrage, nämlich df-). Statt „Was ist X?“ fragen sie dann Anwendung, Beispiel oder Abgrenzung. Gilt vor den Einträgen in <fach>.py."""
from dsl import mc, mm, bl, zu, ku

UEBER = {}
