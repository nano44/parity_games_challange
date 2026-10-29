#!/usr/bin/env python3
"""L-RED (R106 addendum): the whole N5 execution on a game, from a given start or from the S3 default start ("S3"): iterations,
fallbacks, phases (maximal tau-constant stretches), runs (KEY = (lambda_Xi, tau) constant, no fallback), the longest run, the maximal REL
segment length (segchk.py's cut), and per-vertex switch counts (max over Even vertices in the whole execution and inside the longest run).
Usage: whole.py GAME.pg START|S3"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "n5-second")); sys.path.insert(0, HERE)
import n5b, segchk
g = n5b.pg.read(sys.argv[1]); N = n5b.N5(g); N.mode = "spec"
if sys.argv[2] == "S3": s0, t0 = N.SG.initial_strategy_by_best_reward(), N.SD.initial_strategy_by_best_reward()
else: s0, t0 = n5b.read_start(sys.argv[2], g)
tr, fb = [], []; N.run(list(s0), list(t0), trace=tr, fbtrace=fb)
S = [s for s, _ in tr]; T = [t for _, t in tr]; K = len(tr)
LAM = [tuple(N.opt(N.SG, [S[k][v] if g.owner[v] == 0 else -1 for v in range(g.n)])[0][v][0] for v in range(g.n)) for k in range(K)]
phases = 1 + sum(1 for k in range(1, K) if T[k] != T[k - 1])
runs, r0 = [], 0
for k in range(1, K + 1):
    if k == K or fb[k - 1] or T[k] != T[k - 1] or LAM[k] != LAM[k - 1]: runs.append((r0, k - 1)); r0 = k
lr = max(runs, key=lambda r: r[1] - r[0])
EV = [v for v in range(g.n) if g.owner[v] == 0]
sw = lambda a, b: max(sum(1 for t in range(a, b) if S[t][v] != S[t + 1][v]) for v in EV)
res, _, _ = segchk.analyse(g, list(s0), list(t0), out=lambda *x: None)
print(f"n {g.n} start {sys.argv[2].split('/')[-1]} iterations {K - 1} fallbacks {sum(fb)} phases {phases} runs {len(runs)} "
      f"longest run {lr} len {lr[1] - lr[0]} max REL segment {max(r['L'] for r in res)} max per-vertex switches: whole {sw(0, K - 1)} "
      f"in longest run {sw(*lr)}")
