#!/usr/bin/env python3
"""L-NEW: search for an N1 killer by per-edge delays. Base game G (priorities shifted by +2); each Even choice edge e gets
a chain of D_e >= 0 fresh single-successor Odd vertices of priority 0 (winners unchanged: every cycle keeps an original
vertex). Hill climb over the vector D (entries 0..--dmax) maximising N1's total Even iterations (anneal.solve, no merging).
Usage: delay_search.py game.pg [--dmax 8] [--steps 200] [--seed 0] [--out best.pg]"""
import sys, os, random, argparse, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "harness")); sys.path.insert(0, HERE)
import pg, zielonka, verify, anneal
anneal.COMPRESS = False
ap = argparse.ArgumentParser(); ap.add_argument("game"); ap.add_argument("--dmax", type=int, default=8)
ap.add_argument("--steps", type=int, default=200); ap.add_argument("--seed", type=int, default=0); ap.add_argument("--out", default="")
a = ap.parse_args(); rng = random.Random(a.seed)
g = pg.parse("".join(l for l in open(a.game) if not l.lstrip().startswith("%")))
edges = [(v, w) for v in range(g.n) if g.owner[v] == 0 and len(set(g.succ[v])) >= 2 for w in sorted(set(g.succ[v]))]
def build(D):
    prio = [p + 2 for p in g.prio]; owner = list(g.owner); succ = [sorted(set(s)) for s in g.succ]
    for (v, w), d in zip(edges, D):
        if d == 0: continue
        first = len(prio)
        for i in range(d):
            prio.append(0); owner.append(1); succ.append([first + i + 1] if i < d - 1 else [w])
        succ[v] = [first if x == w else x for x in succ[v]]
    return pg.Game(prio, owner, succ)
def score(D):
    (win, strat), J, E, O, per = anneal.solve(build(D)); return E
D = [0] * len(edges); s = score(D); best = (s, list(D)); t0 = time.time()
print(f"edges={len(edges)} start={s}", flush=True)
for t in range(a.steps):
    D2 = list(D)
    for _ in range(rng.randint(1, 3)):
        D2[rng.randrange(len(D2))] = rng.randint(0, a.dmax)
    s2 = score(D2)
    if s2 >= s: D, s = D2, s2
    if s > best[0]: best = (s, list(D)); print(f"  step {t}: {s}  ({time.time()-t0:.0f}s)", flush=True)
h = build(best[1]); (win, strat), J, E, O, per = anneal.solve(h)
ok = win == zielonka.solve(h) and not verify.check(h, win, strat)
print(f"RESULT best={best[0]} n={h.n} plain_vj_base=see vjfast check={'OK' if ok else 'FAIL'} D={best[1]}")
if a.out: pg.write(h, a.out)
