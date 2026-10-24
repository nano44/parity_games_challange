#!/usr/bin/env python3
"""Box 26: per (τ, joint-λ)-phase: re-entries by class (reentry.py), θ-changes, and the largest number of THETA re-entries that
follow one θ-change before the next (release batch). Usage: reperphase.py game.pg [start]"""
from common import *
from reentry import run
from collections import Counter
import reentry
if __name__ == "__main__":
    g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 else None
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); states, _ = trace(g, st)
    lam, th = [], []
    for s, t in states:
        Xi, _ = E.evaluate(s); U, _ = Ed.evaluate(t); lam.append((tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o])); th.append(E.key(Xi[o]))
    # capture verbose events
    import io, contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf): run(g, st, Counter(), verbose=True)
    ev = [l for l in buf.getvalue().splitlines() if l.startswith("x=")]
    phases = []; a = 0
    for i in range(1, len(states) + 1):
        if i == len(states) or lam[i] != lam[i - 1]: phases.append((a, i - 1)); a = i
    for a, b in phases:
        if b - a < 3: continue
        thc = sum(th[k] != th[k - 1] for k in range(a + 1, b + 1))
        es = [l for l in ev if a <= int(l.split("reenter@")[1].split()[0]) <= b]
        cls = Counter(l.rsplit(": ", 1)[1] for l in es)
        print(f"phase {a}..{b} ({b-a} it): θ-changes {thc}, re-entries {dict(cls)}")
