#!/usr/bin/env python3
"""Box 33: CONJECTURE ORX (docs/new/N5-K-box33.md): inside a fallback-free segment of a phase, each exit of o is the old exit x0 of at
most one O-rise. Also checks the stronger EXIT-R: after an O-rise with old exit x0, x0 stays in R until the next fallback or phase end.
With env EPS=1 the same for every ε-transition (O_k > E_k; ε of Theorem LP). Usage: orx.py game.pg ... | --rand N lo hi seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box32"))
from dormant import *

EPS = os.environ.get("EPS") == "1"   # EPS=1: every ε-transition (O_k > E_k), not only O-rises

def check(g, acc, name):
    rows, o = rows_w(g); E = Engine(g); ev = [E.evaluate(tuple(r["s"])) for r in rows]
    Ls = [relL(g, ev, rows, k) if rows[k]["ph"] == rows[k + 1]["ph"] else None for k in range(len(rows) - 1)]
    prev = None; seg = 0; seen = {}; watch = {}
    for k in range(len(Ls)):
        if Ls[k] is None or rows[k]["fb"]: seg += 1; watch = {}
        if Ls[k] is None: prev = None; continue
        for x in list(watch):
            if x not in set(rows[k + 1]["R"]) | {o}:
                acc["EXITR_FAIL"] = acc.get("EXITR_FAIL", 0) + 1; acc.setdefault("ex_EXITR", (name, watch[x], k, x)); del watch[x]
        if Ls[k] == -2: continue
        isrise = prev is not None and Ls[k] > Ls[prev] and not any(rows[j]["fb"] for j in range(prev, k + 1))
        if isrise or EPS:
            sb0, sb1, X0 = ev[k][1], ev[k + 1][1], ev[k][0]
            Ev = max([lev(X0[rows[k]["s"][y]], X0[rows[k + 1]["s"][y]]) for y in range(g.n) if g.owner[y] == 0 and rows[k]["s"][y] != rows[k + 1]["s"][y] and X0[y][0] != y] + [-2])
            if sb0[o] != sb1[o] and X0[o][0] != o and lev(X0[sb0[o]], X0[sb1[o]]) == Ls[k] and (isrise or lev(X0[sb0[o]], X0[sb1[o]]) > Ev):
                x0 = sb0[o]; acc["orise"] = acc.get("orise", 0) + 1; key = (seg, x0)
                if key in seen: acc["ORX_FAIL"] = acc.get("ORX_FAIL", 0) + 1; acc.setdefault("ex_ORX", (name, seen[key], k, x0))
                seen[key] = k; watch[x0] = k
        prev = k

if __name__ == "__main__":
    acc = {}; a = sys.argv[1:]
    if a and a[0] == "--rand":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); d = 0
        while d < N:
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            check(g, acc, f"rand{seed}_{d}"); d += 1
    else:
        for f in a:
            g = load(f)
            if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) != 1: continue
            check(g, acc, os.path.basename(f))
    acc.setdefault("orise", 0)
    for k in sorted(acc): print(k, acc[k])
