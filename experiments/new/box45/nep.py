#!/usr/bin/env python3
"""Box 45 DATA for N_ep (Lead 07:11Z item (3)): per phase of N5, the number of epochs N_ep, the number of distinct sigma-bar|Q
configurations (CONF), the max number of epochs sharing one configuration (MULT), and the number of distinct one-player optima OPT
(Even's optimal valuation in G_{sigma-bar_E}, Odd fixed to sigma-bar_E: the one-player game behind the epoch's honest frame).
Reports: phases, ALL1 (phases whose epochs all have |D| <= 1) with their max N_ep / MULT / CONF, phases with N_ep > CONF (a configuration recurs), max N_ep, max MULT, max N_ep / OPT, and the per-|D| configuration counts.
Usage: nep.py STARTS SEED (--list FILE | --rand C LO HI GSEED | files)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "box43")); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from multi import rand_ckO
from n5x import load, step, start_pair, Engine, dual, pg
C = dict(runs=0, phases=0, REC=0, NEPMAX=0, NEPMAX_n=0, CONFMAX=0, MULTMAX=0, MULTMAX_n=0, OPTMAX=0, NEP_OVER_OPT=0.0, MULT_D1MAX=0, MULT_D0MAX=0, ALL1=0, ALL1_NEPMAX=0, ALL1_MULTMAX=0, ALL1_CONFMAX=0)
def opt(g, sbE):
    succ = [[sbE[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(g.n)]
    gg = pg.Game(list(g.prio), list(g.owner), succ); Ed = Engine(dual(gg))
    vals, _ = Ed.evaluate(tuple(sbE[v] if g.owner[v] == 1 else -1 for v in range(g.n)))
    return tuple(vals)
def check(g, start, cap=4000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []; C["runs"] += 1
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2]
    while len(rows) <= cap:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        rows.append((tuple(x[0] for x in vs), tuple(t), tuple(sb[q] for q in Q), tuple(sb)))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and rows[j + 1][:2] == rows[i][:2]: j += 1
        phase(g, rows, i, j, Q); i = j + 1
def phase(g, rows, a, b, Q):
    C["phases"] += 1; eps = []; k = a
    while k <= b:
        e = k
        while e + 1 <= b and rows[e + 1][2] == rows[k][2]: e += 1
        eps.append(k); k = e + 1
    confs = [rows[x][2] for x in eps]; tau = rows[a][1]
    cnt = {}
    for c in confs: cnt[c] = cnt.get(c, 0) + 1
    nd = lambda c: sum(1 for q, w in zip(Q, c) if w != tau[q])
    if len(eps) > len(cnt): C["REC"] += 1
    if len(eps) > C["NEPMAX"]: C["NEPMAX"], C["NEPMAX_n"] = len(eps), g.n
    C["CONFMAX"] = max(C["CONFMAX"], len(cnt))
    m = max(cnt.values())
    if m > C["MULTMAX"]: C["MULTMAX"], C["MULTMAX_n"] = m, g.n
    for c, v in cnt.items():
        if nd(c) == 1: C["MULT_D1MAX"] = max(C["MULT_D1MAX"], v)
        if nd(c) == 0: C["MULT_D0MAX"] = max(C["MULT_D0MAX"], v)
    if all(nd(c) <= 1 for c in confs):
        C["ALL1"] += 1; C["ALL1_NEPMAX"] = max(C["ALL1_NEPMAX"], len(eps)); C["ALL1_MULTMAX"] = max(C["ALL1_MULTMAX"], m)
        C["ALL1_CONFMAX"] = max(C["ALL1_CONFMAX"], len(cnt))
    if len(eps) > 1:
        opts = {opt(g, rows[x][3]) for x in eps}
        C["OPTMAX"] = max(C["OPTMAX"], len(opts)); C["NEP_OVER_OPT"] = max(C["NEP_OVER_OPT"], round(len(eps) / len(opts), 2))
if __name__ == "__main__":
    a = sys.argv[1:]; K = int(a[0]); RNG = random.Random(int(a[1])); a = a[2:]
    if a[0] == "--list":
        R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        gs = [load(os.path.join(R0, l.split()[0])) for l in open(a[1]) if l.strip() and not l.startswith("#")]
    elif a[0] == "--rand":
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        gs = [g for g in (rand_ckO(rng, lo, hi, rng.randint(2, 4)) for _ in range(cnt)) if g is not None]
    else: gs = [load(f) for f in a]
    for g in gs:
        if g.n > 64: continue
        for st in [None] + [({v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                             {v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) for _ in range(K)]:
            try: check(g, st)
            except RecursionError: pass
    print(", ".join(f"{k} {v}" for k, v in C.items()))
