#!/usr/bin/env python3
"""Box 6: frequency of the K8 flip-back (b_k = b_{k+2} ≠ b_{k+1}) at changes of Odd's best reply along switch-best runs on random
games (n5_lock.rgame), and, separately, whether N5 then follows switch-best's run to the end (follow = full).
Usage: sb_flip_rand.py games seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from n5_lock import rgame, step
from n5 import pg, Engine, dual
games, seed = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed)
tot_ch = tot_flip = full = runs = longest_full = 0; wit = None
for _ in range(games):
    g = rgame(rng.randint(5, 20), 3, rng); E, Ed = Engine(g), Engine(dual(g)); O = [v for v in range(g.n) if g.owner[v] == 1]
    def sbstep(s):
        vs, _ = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs)
        if not Is: return None
        A = {v: {s[v]} | {w for x, w in Is if x == v} for v in range(g.n) if g.owner[v] == 0}
        h = pg.Game(list(g.prio), list(g.owner), [sorted(A[v]) if g.owner[v] == 0 else list(g.succ[v]) for v in range(g.n)])
        Eh = Engine(h); sb, _ = Eh.run(Eh.rule_switch_all, tuple(s)); return list(sb)
    sig = [list(E.initial("best"))]
    while len(sig) < 200:
        nx = sbstep(sig[-1])
        if nx is None: break
        sig.append(nx)
    b = [tuple(E.evaluate(tuple(s))[1][v] for v in O) for s in sig]
    for k in range(len(b) - 2):
        if b[k + 1] != b[k + 2]:
            tot_ch += 1
            if b[k] == b[k + 2]: tot_flip += 1; wit = wit or (g.prio, g.owner, g.succ, k)
    s, t = list(E.initial("best")), list(Ed.initial("best")); k = 0
    while k + 1 < len(sig):
        r = step(g, E, Ed, s, t)
        if r is None or r[0] != sig[k + 1]: break
        s, t = r[0], r[1]; k += 1
    runs += 1
    if k == len(sig) - 1: full += 1; longest_full = max(longest_full, k)
print(f"games={games} seed={seed}: changes of Odd's best reply {tot_ch}; flip-backs {tot_flip}; N5 follows switch-best fully in {full}/{runs} runs (longest fully followed run {longest_full})")
print("first flip-back witness:", wit)
