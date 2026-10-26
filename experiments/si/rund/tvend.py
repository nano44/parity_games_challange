#!/usr/bin/env python3
"""L-SI box 19 (successor 15): DATA for note §27 (Lemma TV-END). Per phase and honest class c with T := Q u {c} (Q = Odd vertices of
out-degree >= 2), Q_c-runs Theta = maximal runs of the phase with Xi(q) constant for every q in Q n U_c, q != c. A state t is FROZEN
for c when t comes after >= |U_c| - 1 fallbacks of the phase AND of its Q_c-run (RESULTS R56 (g) Lemma TV's hypothesis). Lemma TV-END:
from a frozen state to the end of the phase, no Even vertex of U_c minus T switches and Xi is constant on U_c (so the Q_c-run lasts to the
phase end). TVEND_V counts violations; frozen_states counts (class, state) pairs checked (vacuity); classes_frozen the classes reaching it.
MUT=1 control: count only the PHASE's fallbacks, not the run's (a weaker hypothesis; reported, may or may not bite).
Usage: tvend.py --one GAME [START] | --list FILE [KMIN] (env RS, NMAX)"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, HERE)
from n5x import step, start_pair, Engine, dual, load, readstart
C = Counter(); VIOL = []; MUT = os.environ.get("MUT") == "1"

def check(g, name, start=None):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2]
    while len(rows) <= 3000:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        rows.append(dict(key=(tuple(x[0] for x in vs), tuple(t)), vs=vs, s=list(s), fb=(r[4] if r else 0)))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and rows[j + 1]["key"] == rows[i]["key"]: j += 1
        if j > i: phase(g, name, rows, i, j, set(Q))
        i = j + 1

def phase(g, name, rows, i, j, Qs):
    lam = rows[i]["key"][0]
    for c in sorted(set(lam)):
        U = [v for v in range(g.n) if lam[v] == c]
        if len(U) < 2: continue
        Qc = [v for v in U if v in Qs and v != c]
        NT = [v for v in U if v != c and v not in Qs]
        fph = frun = 0; frozen = False
        for k in range(i, j):
            if frozen:
                C["frozen_transitions"] += 1
                sw = [v for v in NT if g.owner[v] == 0 and rows[k]["s"][v] != rows[k + 1]["s"][v]]
                ch = [v for v in U if tuple(rows[k]["vs"][v]) != tuple(rows[k + 1]["vs"][v])]
                if sw or ch: C["TVEND_V"] += 1; VIOL.append(("TVEND", name, i, c, k - i, sw[:4], ch[:4]))
            qev = any(tuple(rows[k]["vs"][q]) != tuple(rows[k + 1]["vs"][q]) for q in Qc)
            if rows[k]["fb"]: fph += 1; frun += 1
            if qev: frun = 0
            if not frozen and (fph if MUT else min(fph, frun)) >= len(U) - 1:
                frozen = True; C["classes_frozen"] += 1; C["frozen_multi" if len(Qc) >= 2 else "frozen_le1"] += 1

def main():
    a = sys.argv[1:]
    if a[0] == "--one":
        g = load(a[1]); check(g, a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        kmin = int(a[2]) if len(a) > 2 else 2
        for line in open(a[1]):
            f = line.strip()
            if not f: continue
            g = load(os.path.join(ROOT, f))
            if g.n > int(os.environ.get("NMAX", "48")) or sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2) < kmin:
                continue
            check(g, f); rng = random.Random(f)
            for _ in range(int(os.environ.get("RS", "0"))):
                check(g, f + " rs", ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                     {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}))
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for v in VIOL[:8]: print("VIOLATION", v)
    print("TVEND PASS" if not VIOL else "TVEND FAIL")

if __name__ == "__main__":
    main()
