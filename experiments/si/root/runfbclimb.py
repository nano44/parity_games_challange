#!/usr/bin/env python3
"""L-SI box 23 (successor 19): climb for the transition-count targets of docs/si/N5-ALT-box23.md §13. OBJ=run: the longest fallback-free run
of a phase (CONJECTURE RUN-LIN: <= 2n transitions); OBJ=fb: the most in-phase fallbacks of one phase (CONJECTURE FB-LIN: <= n); OBJ=phase: the
longest phase. Score = (value - c*n, value, -n) with c = 2, 1, 4 respectively. Mutations: experiments/new/box43/climb.mutate (Odd choices fixed).
Usage: runfbclimb.py SEED.pg [SEED.start|-] STEPS RNGSEED NMAX OUTPREFIX"""
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
    n = g.n; best = None; obj = os.environ.get("OBJ", "run"); cn = {"run": 2, "fb": 1, "phase": 4}[obj]
    for i, j in phases(R):
        if obj == "phase": vals = [j - i]
        elif obj == "fb": vals = [sum(1 for k in range(i, j) if R[k]["fb"])]
        else:
            vals, s0 = [], i
            for k in range(i, j + 1):
                if k == j or R[k]["fb"]: vals.append(k - s0); s0 = k + 1
        for v in vals:
            sc = (v - cn * n, v, -n)
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
