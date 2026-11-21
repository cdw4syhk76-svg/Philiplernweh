"""Linguistics-Fragen bauen: python3 werkzeuge/ling/fragen.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import fragen_1, fragen_2  # noqa: F401
from fr_basis import schreibe
schreibe()
