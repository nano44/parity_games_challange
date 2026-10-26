#!/usr/bin/env python3
"""Box 48 DATA (N5-NCONF §10): Lemma RESTRICT_H on its widest instance, the USED-EDGE game of a whole phase. For a phase P = (i, ..., j):
G^P := G with every Odd v cut to {tau(v)} union {sigma-bar_k(v) : k in P} (Even keeps its edges). Checks (as box45 RESTRICT_E, fsrestrict.py):
XI_V (Xi on G^P != Xi on G at a state of P), REP_V (N5^tau on G^P from (sigma_i, tau) does not reproduce sigma, tau and the fallback flag at
every in-phase transition i -> i+1, ..., j-1 -> j). Counts phases with >= 2 states, QP := #{Odd v with >= 2 kept edges in G^P} (max, and
phases with QP >= 2, which no epoch / u-run / frozen-side stretch restriction covers in one piece), XDEG := sum over Odd v of (kept - 1).
MUT=1: at the phase's first state i pick an Odd v with sigma-bar_i(v) != tau(v) and drop the edge (v, sigma-bar_i(v)) from G^P (must bite).
Usage: phrestrict.py STARTS SEED (--list FILE | files) [--nmax N] [--start F]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
for p in ("../box45", "../box43", "../box21"): sys.path.insert(0, os.path.join(HERE, p))
from eprestrict import step_tau
from multi import load, step, start_pair, Engine, dual
from n5x import pg, readstart
C = {}
def inc(k, v=1): C[k] = C.get(k, 0) + v
def mx(k, v): C[k] = max(C.get(k, v), v)
MUT = os.environ.get("MUT") == "1"
def run(g, start, nm, cap=4000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []
    while len(rows) <= cap:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        rows.append(dict(lam=tuple(x[0] for x in vs), t=tuple(t), s=tuple(s), vs=tuple(vs), sb=tuple(sb), fb=r[4] if r else 0))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and (rows[j + 1]["lam"], rows[j + 1]["t"]) == (rows[i]["lam"], rows[i]["t"]): j += 1
        if j > i: phase(g, rows, i, j, nm)
        i = j + 1
def phase(g, rows, i, j, nm):
    tau = rows[i]["t"]; odd = [v for v in range(g.n) if g.owner[v] == 1]
    used = {v: sorted({tau[v]} | {rows[k]["sb"][v] for k in range(i, j + 1)}) for v in odd}
    qp = sum(1 for v in odd if len(used[v]) >= 2)
    inc("phases"); inc("phase_transitions", j - i); mx("max_QP", qp); mx("max_XDEG", sum(len(used[v]) - 1 for v in odd))
    if qp >= 2: inc("phases_QP_ge2"); inc("transitions_QP_ge2", j - i)
    if MUT:
        cand = [v for v in odd if rows[i]["sb"][v] != tau[v]]
        if not cand: return
        v0 = cand[0]; used[v0] = [w for w in used[v0] if w != rows[i]["sb"][v0]]; inc("mutated")
    succ = [used[v] if g.owner[v] == 1 else list(g.succ[v]) for v in range(g.n)]
    gp = pg.Game(list(g.prio), list(g.owner), succ); Ep, Edp = Engine(gp), Engine(dual(gp))
    if any(tuple(Ep.evaluate(rows[k]["s"])[0]) != rows[k]["vs"] for k in range(i, j + 1)): inc("XI_V")
    s, t = list(rows[i]["s"]), list(tau)
    for k in range(i, j):
        r = step_tau(gp, Ep, Edp, s, t)
        if r is None or tuple(r[0]) != rows[k + 1]["s"] or tuple(r[1]) != tau or r[2] != rows[k]["fb"]:
            inc("REP_V"); break
        s, t = r[0], r[1]
if __name__ == "__main__":
    a = sys.argv[1:]; nmax = 34; fixed = None
    if "--nmax" in a: i = a.index("--nmax"); nmax = int(a[i + 1]); del a[i:i + 2]
    if "--start" in a: i = a.index("--start"); fixed = readstart(a[i + 1]); del a[i:i + 2]
    K = int(a[0]); RNG = random.Random(int(a[1])); a = a[2:]
    if a[0] == "--list":
        R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        gs = [(l.split()[0], load(os.path.join(R0, l.split()[0]))) for l in open(a[1]) if l.strip() and not l.startswith("#")]
    else: gs = [(f, load(f)) for f in a]
    for nm, g in gs:
        if g.n > nmax: continue
        sts = [fixed] if fixed else [None] + [({v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                                {v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) for _ in range(K)]
        for st in sts:
            try: run(g, st, nm)
            except RecursionError: inc("RECERR")
    print(" ".join(f"{k} {v}" for k, v in sorted(C.items())))
