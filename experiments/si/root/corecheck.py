#!/usr/bin/env python3
"""L-SI box 23 (successor 19): DATA for docs/si/P-N5-CORE-box23.md. At every in-phase transition: C1_V (sigma unchanged), C3_V (an Even
switcher off honest cycles at t and t+1 whose Xi does not rise strictly), C4 (every CLEAN sigma-bar change at u in Q, u != c, off honest cycles:
y2 in Y^u_t, y1 in Y^u_t+1; C4_V if Xi(y1) does not rise and is not tied with y2 at t+1). C4_clean / C4_unclean count the cases.
MUT=1 (control): C3 demands a rise of the switcher's NEW successor's Xi from t to t+1 instead (must bite).
Usage: corecheck.py --list FILE (env NMAX) | --one GAME [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from common import rows, phases, load, readstart
C = Counter(); MUT = os.environ.get("MUT") == "1"

def oncyc(nx, v):
    x, seen = nx[v], set()
    while x not in seen and x != v: seen.add(x); x = nx[x]
    return x == v

def avoids(nx, y, u):
    x, seen = y, set()
    while x not in seen:
        if x == u: return False
        seen.add(x); x = nx[x]
    return True

def run(g, name, st=None):
    E, R = rows(g, st); n = g.n; Q = {v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2}
    for i, j in phases(R):
        for k in range(i, j):
            a, b = R[k], R[k + 1]; C["trans"] += 1
            if a["s"] == b["s"]: C["C1_V"] += 1; print("C1_V", name, k)
            for w in range(n):
                if g.owner[w] != 0 or a["s"][w] == b["s"][w]: continue
                if oncyc(a["nxt"], w) or oncyc(b["nxt"], w): C["C3_skip_cycle"] += 1; continue
                C["C3"] += 1
                lhs, rhs = (b["vs"][b["s"][w]], a["vs"][b["s"][w]]) if MUT else (b["vs"][w], a["vs"][w])
                if not E.key(lhs) > E.key(rhs): C["C3_V"] += 1
            for u in Q:
                y1, y2 = a["sb"][u], b["sb"][u]
                if y1 == y2 or a["vs"][u][0] == u or oncyc(a["nxt"], u) or oncyc(b["nxt"], u): continue
                if avoids(a["nxt"], y2, u) and avoids(b["nxt"], y1, u):
                    C["C4_clean"] += 1
                    if not (E.key(b["vs"][y1]) > E.key(a["vs"][y1]) or E.key(b["vs"][y1]) == E.key(b["vs"][y2])): C["C4_V"] += 1; print("C4_V", name, k, u)
                    if E.key(b["vs"][y1]) == E.key(b["vs"][y2]) and E.key(b["vs"][y1]) == E.key(a["vs"][y1]): C["C4_tie"] += 1
                else: C["C4_unclean"] += 1

def main():
    a = sys.argv[1:]; ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
    if a[0] == "--one": run(load(a[1]), a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        for line in open(a[1]):
            tk = line.split() if line.strip() and not line.startswith("#") else []
            if not tk: continue
            P = lambda x: os.path.join(ROOT, x) if os.path.exists(os.path.join(ROOT, x)) else os.path.join(ROOT, "experiments", x)
            g = load(P(tk[0]))
            if g.n > int(os.environ.get("NMAX", "48")): continue
            run(g, tk[0], readstart(P(tk[1])) if len(tk) > 1 else None)
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    print("CORE PASS" if not any(k in C for k in ("C1_V", "C3_V", "C4_V")) else "CORE FAIL")

if __name__ == "__main__":
    main()
