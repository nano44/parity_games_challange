#!/usr/bin/env python3
"""L-NEW box 81 (R1-POLY), part 2: the GATED ladder gl_k under R1. R1 = the relaxation R0 (box 80) plus N5's offer FORM: at state t the
offers are Of_t = {(v, w) : X_t(w) > X_t(sigma_t v)} for a potential X_t with X_t <= W_t pointwise and X_t non-decreasing in t, and
sigma_{t+1} is the one-player optimum of sigma_t + Of_t. X is otherwise free (N5's Xi is X with the extra law X = val(sigma, sigmabar)).
gl_k = ladder_k with every choice edge v -> u(j, b) subdivided by a PRIVATE gate vertex g(v, b) (Even, one successor u(j, b)). Gates sit
below every ladder vertex in relevance, so path comparisons are decided by the ladder part as in ladder_k.
The script replays box 80's DP-optimal lead-follow schedule (v -> u(j,b) becomes v -> g(v,b)), builds the X schedule
  X_t(g) := W_s(g), s the last state <= t at which g was v's current successor or the offered target (BOTTOM if never),
  X_t(x) := W_t(x) for every non-gate vertex,
and VERIFIES with the fleet engine: (i) X_t <= W_t; (ii) X non-decreasing; (iii) at every step Of_t is EXACTLY the one scheduled edge;
(iv) the scheduled edge is W-improving, so sigma_{t+1} is the one-player optimum of sigma_t + Of_t; (v) W pointwise non-decreasing;
(vi) W(T) takes 2^k values. Usage: gladder.py K [--write]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
for p in ("experiments/si", "experiments/harness"): sys.path.insert(0, os.path.join(ROOT, p))
import pg, subprocess
from si import Engine
k = int(sys.argv[1])
# box80 schedule on ladder_k (ids: 0 sink, u(j,b) = 1+2(j-1)+b, T = 2k+1)
out = subprocess.run([sys.executable, "-I", os.path.join(HERE, "..", "box80", "ladder.py"), str(k), "--write"], capture_output=True, text=True).stdout
seq = [tuple(map(int, l.split())) for l in open(os.path.join(HERE, "..", "box80", "inst", f"ladder_{k}.seq")) if l[0] != "%"]
def u(j, b): return 1 + 2 * (j - 1) + b
T = 2 * k + 1; n0 = 2 * k + 2
choosers = [u(j, b) for j in range(2, k + 1) for b in (0, 1)] + [T]
gate = {}; prio = [0] * n0; succ = [None] * n0; succ[0] = [0]
nxt = n0; gp = 1
for j in range(1, k + 1):
    for b in (0, 1):
        prio[u(j, b)] = 2 * (2 * (k - j) + b) + 2 + 4 * k          # ladder above every gate
        succ[u(j, b)] = [0] if j == 1 else None
prio[T] = 1
for v in choosers:
    j = k if v == T else (v - 1) // 2          # level read by v (ladder index of v is (v-1)//2 + 1)
    succ[v] = []
    for b in (0, 1):
        gate[(v, b)] = nxt; prio.append(gp + 1); gp += 1; succ.append([u(j, b)]); succ[v].append(nxt); nxt += 1
n = nxt
assert len(prio) == n and all(s is not None for s in succ) and max(prio[n0:]) < min(prio[1:2 * k + 1])
g = pg.Game(prio, [0] * n, succ); E = Engine(g)
child2gate = {(v, w): gate[(v, (w - 1) % 2)] for v in choosers for w in (u(k if v == T else (v - 1) // 2, 0), u(k if v == T else (v - 1) // 2, 1))}
sigma = [s[0] for s in succ]
def W(sig): return E.evaluate(tuple(sig))[0]
BOT = None                                      # a value below every value
def le(a, b): return a is BOT or (b is not BOT and E.key(a) <= E.key(b))
def gt(a, b): return not le(a, b)
w = W(sigma); last = {}                         # gate -> value frozen at its last current/target state
for v in choosers: last[sigma[v]] = w[sigma[v]]
def Xof(wv):
    return [last.get(x, BOT) if x in last or x >= n0 else wv[x] for x in range(n)]
X = Xof(w); bad = {"X>W": 0, "X-decrease": 0, "offer-mismatch": 0, "non-improving": 0, "W-decrease": 0}
tv = [w[T]]
for (v, c) in seq:
    tg = child2gate[(v, c)]
    last[tg] = w[tg]                            # raise X of the target gate to its current W
    Xn = Xof(w)
    for x in range(n):
        if not le(Xn[x], w[x]): bad["X>W"] += 1
        if gt(X[x], Xn[x]): bad["X-decrease"] += 1
    offers = {(y, z) for y in choosers for z in succ[y] if z != sigma[y] and gt(Xn[z], Xn[sigma[y]])}
    if offers != {(v, tg)}: bad["offer-mismatch"] += 1
    if not E.key(w[tg]) > E.key(w[sigma[v]]): bad["non-improving"] += 1
    sigma[v] = tg; w2 = W(sigma)
    bad["W-decrease"] += sum(1 for x in range(n) if E.key(w2[x]) < E.key(w[x]))
    w = w2; last[tg] = w[tg]
    for y in choosers: last[sigma[y]] = w[sigma[y]]   # current gates track their W (monotone, = W)
    X = Xof(w)
    if w[T] != tv[-1]: tv.append(w[T])
print(f"GLADDER k {k} n {n} steps {len(seq)} T-values {len(tv)} (2^k = {2 ** k}) {bad}")
if "--write" in sys.argv:
    with open(os.path.join(HERE, "inst", f"gl_{k}.pg"), "w") as f:
        f.write(f"parity {n - 1};\n" + "".join(f"{x} {prio[x]} 0 {','.join(map(str, succ[x]))};\n" for x in range(n)))
