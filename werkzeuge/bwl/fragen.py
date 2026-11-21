"""Erzeugt inhalte/bwl/fragen.json aus fragen_1.py und fragen_2.py. Aufruf: python3 werkzeuge/bwl/fragen.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import fr_basis
import fragen_1  # noqa: F401
try:
    import fragen_2  # noqa: F401
except ModuleNotFoundError:
    pass
fr_basis.schreibe()
