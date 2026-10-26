#!/usr/bin/env python3
"""Box 48 DATA (N5-NCONF §9): the frozen-side u-run restriction. A FROZEN-SIDE u-STRETCH J = (x, ..., y) of a phase: a maximal run on which
sigma-bar is constant on Q - {u} (only u's best reply may change; u fixed by J's first change). D- := {v in Q - {u}: sigma-bar_J(v) != tau(v)}.
G^{u|J}: every Odd v in D- cut to {tau(v), sigma-bar_J(v)}, every other Odd v != u cut to tau(v), u keeps its edges. Checks (as box45 RESTRICT_E):
XI_V (Xi on G^{u|J} != Xi on G at a state of J), REP_V (N5^tau on G^{u|J} from x does not reproduce sigma, tau and the fallback flag through
J's last in-phase transition). Counts stretches with |D-| >= 1 (not covered by RESULTS R68's u-runs) and their epochs.
MUT=1: cut v in D- to tau(v) only (XI_V / REP_V must bite). Usage: fsrestrict.py STARTS SEED (--list FILE | files) [--nmax N] [--start F]"""
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
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2]
    while len(rows) <= cap:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        rows.append(dict(lam=tuple(x[0] for x in vs), t=tuple(t), s=tuple(s), vs=tuple(vs), sb=tuple(sb), fb=r[4] if r else 0))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and (rows[j + 1]["lam"], rows[j + 1]["t"]) == (rows[i]["lam"], rows[i]["t"]): j += 1
        x = i
        while x <= j:
            u = None; y = x
            while y < j:
                diff = [q for q in Q if rows[y + 1]["sb"][q] != rows[y]["sb"][q]]
                if not diff: y += 1; continue
                if len(diff) == 1 and (u is None or diff[0] == u): u = diff[0]; y += 1; continue
                break
            if u is not None: stretch(g, rows, x, y, j, Q, u, nm)
            x = y + 1 if y > x else x + 1
        i = j + 1
def stretch(g, rows, x, y, b, Q, u, nm):
    tau = rows[x]["t"]; sb = rows[x]["sb"]; Dm = {v for v in Q if v != u and sb[v] != tau[v]}
    eps = 1 + sum(1 for k in range(x, y) if rows[k + 1]["sb"][u] != rows[k]["sb"][u])
    inc("stretches"); inc("stretch_epochs", eps)
    if not Dm: inc("covered_by_R68_urun"); return
    inc("frozen_side"); inc("frozen_side_epochs", eps); mx("max_Dminus", len(Dm)); mx("max_fs_epochs", eps)
    succ = []
    for v in range(g.n):
        if g.owner[v] == 1 and v != u: succ.append(([tau[v]] if MUT else sorted({tau[v], sb[v]})) if v in Dm else [tau[v]])
        else: succ.append(list(g.succ[v]))
    gp = pg.Game(list(g.prio), list(g.owner), succ); Ep, Edp = Engine(gp), Engine(dual(gp))
    if any(tuple(Ep.evaluate(rows[k]["s"])[0]) != rows[k]["vs"] for k in range(x, y + 1)): inc("XI_V")
    s, t = list(rows[x]["s"]), list(tau)
    for k in range(x, y + 1 if y < b else y):
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
