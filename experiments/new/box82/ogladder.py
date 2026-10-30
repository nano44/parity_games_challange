#!/usr/bin/env python3
"""L-NEW box 82 (R2-POLY): the ODD-gated ladder ogl_k under R2, verified with the fleet engine.
R2 = R1 (box 81) with X_t := the [S1-val] valuation of the (sigma_t, rho_t)-plays for SOME Odd strategy rho_t (consistency), X_t <= W_t,
X non-decreasing; offers {(v, w) : X_t(w) > X_t(sigma_t v)}; sigma_{t+1} = the one-player W-optimum of sigma_t + offers (W against tau).
ogl_k: ladder_k (box 80) with every choice edge v -> u(j, c) replaced by v -> o(v, c), o(v, c) an ODD gate with successors
{u(j, c) = tau(o), u(j, 1 - c)}. Gates are less relevant than the sink cycle node (priority 2, self-loop), so they never enter path sets,
and all plays from one vertex have equal length; ladder priorities as in box 80, shifted above the sink.
rho schedule (box 82 note §2): rho(o(v, c)) := u(j, 1 - c) (ROUTED) iff v currently holds o(v, 1 - c), the scheduled switch at this state is
not (v -> o(v, c)), and W(u(j, c)) > W(u(j, 1 - c)); otherwise rho(o) := tau(o) (HONEST).
Checks with the engine: X <= W; X non-decreasing; offers = exactly the scheduled edge; it is W-improving; W non-decreasing; W(T) 2^k values.
Usage: ogladder.py K [--write]"""
import sys, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
for p in ("experiments/si", "experiments/harness"): sys.path.insert(0, os.path.join(ROOT, p))
import pg
from si import Engine
k = int(sys.argv[1])
subprocess.run([sys.executable, "-I", os.path.join(HERE, "..", "box80", "ladder.py"), str(k), "--write"], capture_output=True)
seq0 = [tuple(map(int, l.split())) for l in open(os.path.join(HERE, "..", "box80", "inst", f"ladder_{k}.seq")) if l[0] != "%"]
def u(j, b): return 1 + 2 * (j - 1) + b
T = 2 * k + 1; n0 = 2 * k + 2
choosers = [u(j, b) for j in range(2, k + 1) for b in (0, 1)] + [T]
def rl(v): return k if v == T else (v - 1) // 2
prio = [0] * n0; owner = [0] * n0; succ = [None] * n0
prio[0] = 2; succ[0] = [0]
for j in range(1, k + 1):
    for b in (0, 1):
        prio[u(j, b)] = 2 * (2 * (k - j) + b) + 4
        succ[u(j, b)] = [0] if j == 1 else None
prio[T] = 3
gate = {}; nxt = n0
for v in choosers:
    succ[v] = []
    for c in (0, 1):
        gate[(v, c)] = nxt; prio.append(c % 2); owner.append(1); succ.append([u(rl(v), c), u(rl(v), 1 - c)]); succ[v].append(nxt); nxt += 1
n = nxt; g = pg.Game(prio, owner, succ)
Ec = {}
def W_of(sig, tau):
    key = tuple(tau)
    if key not in Ec: Ec[key] = Engine(pg.Game(prio, owner, [[tau[x]] if owner[x] == 1 else succ[x] for x in range(n)]))
    return Ec[key].evaluate(tuple(sig))[0], Ec[key]
sig = [s[0] if owner[x] == 0 else -1 for x, s in enumerate(succ)]
tau = [succ[x][0] if owner[x] == 1 else -1 for x in range(n)]
seq = [(v, gate[(v, (c - 1) % 2)]) for v, c in seq0]
def rho_for(sig, W, sched):
    r = list(tau)
    for v in choosers:
        cur = 0 if sig[v] == gate[(v, 0)] else 1
        for c in (0, 1):
            if c == cur or sched == (v, gate[(v, c)]): continue
            j = rl(v)
            if E0.key(W[u(j, c)]) > E0.key(W[u(j, 1 - c)]): r[gate[(v, c)]] = u(j, 1 - c)
    return r
W, E0 = W_of(sig, tau)
bad = dict.fromkeys(["X>W", "X-decrease", "offer-mismatch", "non-improving", "W-decrease"], 0)
Xprev = None; tv = [W[T]]
for step in seq + [None]:
    rho = rho_for(sig, W, step); X, EX = W_of(sig, rho)
    bad["X>W"] += sum(1 for x in range(n) if E0.key(X[x]) > E0.key(W[x]))
    if Xprev is not None: bad["X-decrease"] += sum(1 for x in range(n) if E0.key(X[x]) < E0.key(Xprev[x]))
    Xprev = X
    if step is None: break
    offers = {(v, z) for v in choosers for z in succ[v] if z != sig[v] and E0.key(X[z]) > E0.key(X[sig[v]])}
    if offers != {step}: bad["offer-mismatch"] += 1
    v, z = step
    if not E0.key(W[z]) > E0.key(W[sig[v]]): bad["non-improving"] += 1
    sig[v] = z; W2, _ = W_of(sig, tau)
    bad["W-decrease"] += sum(1 for x in range(n) if E0.key(W2[x]) < E0.key(W[x]))
    W = W2
    if W[T] != tv[-1]: tv.append(W[T])
lam = {W[x][0] for x in range(n)}
print(f"OGLADDER k {k} n {n} odd-gates {n - n0} steps {len(seq)} T-values {len(tv)} (2^k = {2 ** k}) cycle-nodes {sorted(lam)} {bad}")
if "--write" in sys.argv:
    with open(os.path.join(HERE, "inst", f"ogl_{k}.pg"), "w") as f:
        f.write(f"parity {n - 1};\n" + "".join(f"{x} {prio[x]} {owner[x]} {','.join(map(str, succ[x]))};\n" for x in range(n)))
