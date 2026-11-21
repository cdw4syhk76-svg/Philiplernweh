"""Erzeugt inhalte/mawi/fragen.json. Aufruf: python3 werkzeuge/mawi/fragen.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import fragen_1, fragen_2, fragen_3
from fr_basis import schreibe
schreibe()
