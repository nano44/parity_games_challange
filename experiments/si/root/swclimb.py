#!/usr/bin/env python3
"""L-SI box 23 (successor 19): climb for CONJECTURE SW-LIN (docs/si/N5-ALT-box23.md §9): the most switches of ONE Even vertex in ONE phase
of N5, relative to n. Score = (max_w SW(w) - n, phase length, -n). Mutations: experiments/new/box43/climb.mutate (Odd choice set fixed).
RUN=1: the same per fallback-free run (CONJECTURE SW-RUN, §10).
Usage: swclimb.py SEED.pg [SEED.start|-] STEPS RNGSEED NMAX OUTPREFIX"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box43"))
from common import rows, phases, load, readstart
import climb
climb.DEG2 = False
from multi import odd_choices

def score(g, st):
    try: E, R = rows(g, st, cap=800)
    except (RecursionError, RuntimeError): return None
    n = g.n; best = None
    for i, j in phases(R):
        segs = [(i, j)]
        if os.environ.get("RUN") == "1":                 # SW-RUN: score per fallback-free run instead of per phase
            segs, s0 = [], i
            for k in range(i, j + 1):
                if k == j or R[k]["fb"]: segs.append((s0, k)); s0 = k + 1
        for a, b in segs:
            sw = Counter()
            for k in range(a, b):
                for w in range(n):
                    if g.owner[w] == 0 and R[k]["s"][w] != R[k + 1]["s"][w]: sw[w] += 1
            if sw:
                sc = (max(sw.values()) - n, b - a, -n)
                if best is None or sc > best: best = sc
    return best

def mkst(g, st):
    if not st: return None
    return ({v: st[v] for v in range(g.n) if g.owner[v] == 0}, {v: st[v] for v in range(g.n) if g.owner[v] == 1})

def save(out, g, st):
    with open(out + ".pg", "w") as f:
        f.write("parity %d;\n" % (g.n - 1))
        for v in range(g.n): f.write("%d %d %d %s;\n" % (v, g.prio[v], g.owner[v], ",".join(map(str, g.succ[v]))))
    if st:
        with open(out + ".start", "w") as f:
            f.write("SIGMA0 " + " ".join("%d:%d" % (v, st[v]) for v in range(g.n) if g.owner[v] == 0) + "\n")
            f.write("TAU0 " + " ".join("%d:%d" % (v, st[v]) for v in range(g.n) if g.owner[v] == 1) + "\n")

def main():
    gp, sp, steps, seed, nmax, out = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
    rng = random.Random(seed); g = load(gp); O = sorted(odd_choices(g))
    st = None
    if sp != "-":
        s, t = readstart(sp); st = [s.get(v, t.get(v)) for v in range(g.n)]
    cur = score(g, mkst(g, st)); print("seed score", cur, "k", len(O), "n", g.n, flush=True)
    for it in range(steps):
        r = climb.mutate(rng, g, O, nmax, st)
        if r is None: continue
        g2, O2, st2 = r
        sc = score(g2, mkst(g2, st2))
        if sc is not None and (cur is None or sc[0] >= cur[0]):
            if cur is None or sc[0] > cur[0]: print("step", it, "score", sc, "n", g2.n, flush=True); save(out, g2, st2)
            g, O, st, cur = g2, O2, st2, sc
    print("final", cur)

if __name__ == "__main__":
    main()
