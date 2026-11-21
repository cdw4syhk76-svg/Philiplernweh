"""Zerlegt ein Skript in seine Anweisungen auf oberster Ebene (für die Schaubild-Laufzeit in bau.py)."""
import re, sys, pathlib


def stmts(js):
    """Top-level-Anweisungen eines Skripts (Klammern und Strings beachtet, grob)."""
    out = []; i = 0; n = len(js); start = 0; depth = 0; st = None
    while i < n:
        c = js[i]
        if st:
            if c == '\\':
                i += 2; continue
            if c == st:
                st = None
            i += 1; continue
        if c in '"\'`':
            st = c
        elif js.startswith('//', i):
            j = js.find('\n', i); i = n if j < 0 else j; continue
        elif js.startswith('/*', i):
            i = js.find('*/', i) + 2; continue
        elif c in '({[':
            depth += 1
        elif c in ')}]':
            depth -= 1
        elif c == '\n' and depth == 0:
            s = js[start:i].strip()
            if s:
                out.append(s)
            start = i + 1
        i += 1
    s = js[start:].strip()
    if s:
        out.append(s)
    return out


def name(s):
    m = re.match(r'(?:async\s+)?function\s+(\w+)', s) or re.match(r'(?:const|let|var)\s+(\w+)', s)
    return m.group(1) if m else None


