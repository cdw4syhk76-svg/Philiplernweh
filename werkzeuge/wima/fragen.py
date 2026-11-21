"""Erzeugt inhalte/wima/fragen.json. Aufruf: python3 werkzeuge/wima/fragen.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import fragen_1
try:
    import fragen_2
except ImportError:
    pass
from fr_basis import schreibe
schreibe()
