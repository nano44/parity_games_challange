#!/usr/bin/env python3
"""L-NEW box 55: check of Proposition NO-TRANSFER (docs/new/N5-SBC-box55.md §1). Runs N5-SF from the start, takes the final tau (I_tau = empty),
reruns from (sigma_0, tau_final) and checks: tau never changes, every iteration changes sigma (I = #sigma - 1), and the distinct-sigma
sequence is the first run's. Prints NT PASS / NT FAIL. Usage: ntcheck.py GAME [START] | --list FILE"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box54")); sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
import n5sf
from pcheck import distinct
from n5x import Engine, dual, load, readstart, start_pair

def one(g, st):
    E, T = n5sf.trace(g, st); T = [x for x in T if "lam" in x]
    s0, _ = start_pair(g, Engine(g), Engine(dual(g)), st); tf = T[-1]["t"]
    d = lambda s, t: ({v: s[v] for v in range(g.n) if g.owner[v] == 0}, {v: t[v] for v in range(g.n) if g.owner[v] == 1})
    _, U = n5sf.trace(g, d(s0, tf)); U = [x for x in U if "lam" in x]
    A = distinct([x["s"] for x in T], g, 0); B = distinct([x["s"] for x in U], g, 0)
    ok = A == B and len(distinct([x["t"] for x in U], g, 1)) == 1 and len(U) - 1 == len(B) - 1
    return ok, len(T) - 1, len(U) - 1

if __name__ == "__main__":
    a = sys.argv[1:]; bad = tot = 0
    L = [l.split() for l in open(a[1]) if l.strip() and not l.startswith("#")] if a[0] == "--list" else [a]
    for p in L:
        X = lambda q: q if os.path.exists(q) else (os.path.join(ROOT, q) if os.path.exists(os.path.join(ROOT, q)) else os.path.join(ROOT, "experiments", q))
        ok, i1, i2 = one(load(X(p[0])), readstart(X(p[1])) if len(p) > 1 else None); tot += 1; bad += not ok
        if not ok or len(L) == 1: print("GAME", p[0], "I", i1, "I_from_tau_final", i2, "ok" if ok else "BAD")
    print(f"games={tot} bad={bad}"); print("NT PASS" if not bad else "NT FAIL")
