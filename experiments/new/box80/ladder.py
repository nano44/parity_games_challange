#!/usr/bin/env python3
"""L-NEW box 80 (TASK 2, D18 on [P-WCHtau]): the RELAXATION obstruction. Builds ladder_k, a ONE-PLAYER (Even-only) parity game with
n = 2k + 2 vertices, and an explicit sequence of single improving switches (each step = the pointwise one-player optimum of the arena
sigma_t + one offered edge, R15 (a) Lemma A), found by exhaustive DP in the abstract model, then VERIFIES it with the fleet's valuation
engine (experiments/si/si.py Engine; with no Odd vertex, Engine.evaluate(sigma) is W = val(sigma, tau)):
  - each switched edge is W_t-improving at its vertex (W_t(w) > W_t(sigma_t v) in [S1-ord]); W_{t+1} >= W_t pointwise (every vertex monotone);
  - the cycle-node map lambda_W is constant (every play ends in the sink 0);
  - the top vertex T takes 2^k distinct W-values (2^k - 1 strict rises) in one tau-stretch with no fallback (a W-run of the relaxation).
Vertices: 0 sink (prio 0, self-loop); u(j,b) = 1 + 2(j-1) + b, j = 1..k, b = 0/1, prio 2(2(k-j)+b)+2 (all even; deeper = more relevant;
copy 1 above copy 0); level 1 -> sink; level j >= 2 -> {u(j-1,0), u(j-1,1)}; T = 2k+1, prio 1, -> {u(k,0), u(k,1)}.
Usage: ladder.py K [--write]   (writes inst/ladder_K.pg and inst/ladder_K.seq with --write)"""
import sys, os, functools
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
for p in ("experiments/si", "experiments/harness"): sys.path.insert(0, os.path.join(ROOT, p))
import pg
from si import Engine
sys.setrecursionlimit(100000)
k = int(sys.argv[1]); n = 2 * k + 2
def u(j, b): return 1 + 2 * (j - 1) + b
T = 2 * k + 1
prio = [0] * n; succ = [[0]] * n
succ = [None] * n; succ[0] = [0]
for j in range(1, k + 1):
    for b in (0, 1):
        prio[u(j, b)] = 2 * (2 * (k - j) + b) + 2
        succ[u(j, b)] = [0] if j == 1 else [u(j - 1, 0), u(j - 1, 1)]
prio[T] = 1; succ[T] = [u(k, 0), u(k, 1)]
g = pg.Game(prio, [0] * n, succ)
# ---- abstract DP (state = copy choice of every choice vertex) to find a longest sequence of T-value changes
chooser = [u(j, b) for j in range(2, k + 1) for b in (0, 1)] + [T]
def child_level(v): return k if v == T else (v - 1) // 2 + 1 - 1
def aval(st, v):                       # abstract value: copy bits from the deepest level up, then v's own copy bit
    bits = []; x = v
    while x != 0:
        if x != T: bits.append((x - 1) % 2)
        if x == T or (x - 1) // 2 + 1 >= 2: x = u(child_level(x), st[chooser.index(x)])
        else: x = 0
    return tuple(reversed(bits))
@functools.lru_cache(None)
def best(st):
    res = (0, None)
    for i, v in enumerate(chooser):
        cl = child_level(v); cur, alt = st[i], 1 - st[i]
        if aval(st, u(cl, alt)) > aval(st, u(cl, cur)):
            ns = st[:i] + (alt,) + st[i + 1:]
            r = best(ns)[0] + (aval(ns, T) != aval(st, T))
            if r > res[0]: res = (r, (i, alt))
    return res
st = tuple([0] * len(chooser)); seq = []
while best(st)[1] is not None:
    i, alt = best(st)[1]; v = chooser[i]; seq.append((v, u(child_level(v), alt))); st = st[:i] + (alt,) + st[i + 1:]
# ---- real verification with the fleet engine
E = Engine(g)
sigma = [0] * n
for v in range(n): sigma[v] = succ[v][0]
def W(sig): return E.evaluate(tuple(sig))[0]
w = W(sigma); tv = [w[T]]; viol = 0; nonimp = 0; lam = {x[0] for x in w}
for (v, tgt) in seq:
    if not E.key(w[tgt]) > E.key(w[sigma[v]]): nonimp += 1
    sigma[v] = tgt; w2 = W(sigma)
    viol += sum(1 for x in range(n) if E.key(w2[x]) < E.key(w[x]))
    lam |= {x[0] for x in w2}
    if w2[T] != w[T]: tv.append(w2[T])
    w = w2
rises = len(tv) - 1; strict = all(E.key(tv[i + 1]) > E.key(tv[i]) for i in range(rises))
print(f"LADDER k {k} n {n} switches {len(seq)} T-rises {rises} (2^k-1 = {2 ** k - 1}) distinct-T {len(set(tv))} strict {strict} "
      f"non-improving-switches {nonimp} monotonicity-violations {viol} cycle-nodes {sorted(lam)}")
if "--write" in sys.argv:
    with open(os.path.join(HERE, "inst", f"ladder_{k}.pg"), "w") as f:
        f.write(f"parity {n - 1};\n" + "".join(f"{v} {prio[v]} 0 {','.join(map(str, succ[v]))};\n" for v in range(n)))
    with open(os.path.join(HERE, "inst", f"ladder_{k}.seq"), "w") as f:
        f.write("% start: every vertex takes its first successor; then one W-improving switch per line: vertex target\n")
        f.write("".join(f"{v} {t}\n" for v, t in seq))
