#!/usr/bin/env python3
"""Box 45 DATA: search for DIV (premise (Στ), docs/new/P-N5-EPR-box45.md §4): an in-phase state k of N5 on G with D_k = {u},
(u, sigma-bar_k(u)) in I_tau_k (so W_k = Xi_k, Lemma TIE-W), at which SPEC's own S4b on G'_E returns tau_new != tau.
Random games (rand_ckO, k Odd choice vertices), random start pairs. Prints counts and writes the first hits to out/div_*.pg.
tie1_cyc / DIV_cyc: those at which u is its own honest cycle node (lambda(u) = u).
Usage: divsearch.py COUNT NLO NHI K SEED STARTS"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "box43")); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from multi import rand_ckO
from n5x import step, Engine, dual, pg
from eprestrict import restrict, step_tau
cnt, lo, hi, K, seed, S = map(int, sys.argv[1:7]); rng = random.Random(seed)
C = dict(games=0, runs=0, tie1=0, tie1_cyc=0, DIV=0, DIV_cyc=0)
def save(g, s, t, tag):
    os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
    with open(os.path.join(HERE, "out", f"div_{tag}.pg"), "w") as f:
        f.write(f"parity {g.n - 1};\n")
        for v in range(g.n): f.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")
    with open(os.path.join(HERE, "out", f"div_{tag}.start"), "w") as f: f.write(f"sigma {list(s)}\ntau {list(t)}\n")
for gi in range(cnt):
    g = rand_ckO(rng, lo, hi, K)
    if g is None: continue
    C["games"] += 1; E, Ed = Engine(g), Engine(dual(g))
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2]
    for _ in range(S):
        s = [rng.choice(g.succ[v]) if g.owner[v] == 0 else -1 for v in range(g.n)]
        t = [rng.choice(g.succ[v]) if g.owner[v] == 1 else -1 for v in range(g.n)]; C["runs"] += 1
        for it in range(500):
            vs, sb = E.evaluate(tuple(s)); vt, _ = Ed.evaluate(tuple(t)); It = set(Ed.improving(tuple(t), vt))
            r = step(g, E, Ed, s, t)
            if r is None: break
            D = [q for q in Q if sb[q] != t[q]]
            if len(D) == 1 and (D[0], sb[D[0]]) in It and list(r[1]) == list(t):
                vs1, _ = E.evaluate(tuple(r[0]))
                if tuple(x[0] for x in vs1) == tuple(x[0] for x in vs):
                    C["tie1"] += 1; cyc = vs[D[0]][0] == D[0]; C["tie1_cyc"] += cyc
                    gp = restrict(g, set(D), t, sb); rs = step_tau(gp, Engine(gp), Engine(dual(gp)), s, t, spec=True)
                    if rs is not None and list(rs[1]) != list(t):
                        C["DIV"] += 1; C["DIV_cyc"] += cyc
                        if C["DIV"] <= 3: save(g, s, t, f"s{seed}_{C['DIV']}")
            s, t = r[0], r[1]
print(", ".join(f"{k} {v}" for k, v in C.items()))
