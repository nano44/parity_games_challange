#!/usr/bin/env python3
"""Box 48 climber (DATA, N5-NCONF §12): long phases with many disagreeing Odd vertices in ONE class. Genome: game + start pair (seeded from a
long-phase instance and its .start). Mutations: box43 climb.mutate (O fixed) with prob. 0.85; with prob. 0.15 an O-move: turn a forced Odd vertex
into an Odd choice vertex (add an edge), or an Odd choice vertex into a forced one (keep its start edge). Score per phase:
QP_c := max over cycle nodes c of |union of D_k inside lambda^-1(c)|; objective (max over phases of QP_c * len, then len).
Usage: qpcclimb.py NMAX STEPS SEED OUTDIR --seed GAME.pg --start GAME.start"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
for p in ("../box43", "../box21"): sys.path.insert(0, os.path.join(HERE, p))
import climb
from multi import odd_choices
from n5x import load, step, start_pair, Engine, dual, pg, readstart
climb.DEG2 = False
def score(g, st, cap=3000):
    sp = ({v: st[v] for v in range(g.n) if g.owner[v] == 0}, {v: st[v] for v in range(g.n) if g.owner[v] == 1})
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, sp); rows = []
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2]
    while len(rows) <= cap:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        rows.append((tuple(x[0] for x in vs), tuple(t), tuple(sb[q] for q in Q)))
        if r is None: break
        s, t = r[0], r[1]
    best, info, i = (0, 0), None, 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and rows[j + 1][:2] == rows[i][:2]: j += 1
        tau, lam = rows[i][1], rows[i][0]
        U = {q for k in range(i, j + 1) for a, q in enumerate(Q) if rows[k][2][a] != tau[q]}
        byc = {}
        for q in U: byc[lam[q]] = byc.get(lam[q], 0) + 1
        qpc = max(byc.values(), default=0); L = j - i; sc = (qpc * L, L)
        if sc > best: best = sc; info = dict(QPc=qpc, QP=len(U), len=L, Q=len(Q), classes=len(byc))
        i = j + 1
    return best, info
def omove(rng, g, O, st):
    prio, owner, succ = list(g.prio), list(g.owner), [list(x) for x in g.succ]; O = list(O); st = list(st)
    forced = [v for v in range(g.n) if owner[v] == 1 and v not in O]
    if forced and (rng.random() < 0.6 or len(O) <= 1):
        v = rng.choice(forced); succ[v] = sorted(set(succ[v]) | {rng.randrange(g.n)})
        if len(succ[v]) < 2: return None
        O.append(v)
    elif len(O) > 1:
        v = rng.choice(O); succ[v] = [st[v]]; O.remove(v)
    else: return None
    h = pg.Game(prio, owner, succ)
    if sorted(odd_choices(h)) != sorted(O): return None
    return h, O, st
if __name__ == "__main__":
    NMAX, STEPS, SEED = map(int, sys.argv[1:4]); OUT = sys.argv[4]; os.makedirs(OUT, exist_ok=True); rng = random.Random(SEED)
    g = load(sys.argv[sys.argv.index("--seed") + 1]); sp = readstart(sys.argv[sys.argv.index("--start") + 1])
    st = [sp[0][v] if g.owner[v] == 0 else sp[1][v] for v in range(g.n)]
    NMAX = max(NMAX, g.n); O = odd_choices(g); tag = os.path.basename(sys.argv[sys.argv.index("--seed") + 1])[:-3]
    best, info = score(g, st); print("start", best, info, "n", g.n, flush=True)
    for t in range(STEPS):
        r = omove(rng, g, O, st) if rng.random() < 0.15 else climb.mutate(rng, g, O, NMAX, st)
        if r is None: continue
        h, O2, st2 = r
        try: sc, inf = score(h, st2)
        except RecursionError: continue
        if sc >= best:
            if sc > best:
                print(t, sc, inf, "n", h.n, flush=True)
                climb.save(os.path.join(OUT, f"best_qpc_{tag}_s{SEED}.pg"), h, st2, inf)
            g, O, st, best, info = h, O2, st2, sc, inf
    print("done", best, info, flush=True)
