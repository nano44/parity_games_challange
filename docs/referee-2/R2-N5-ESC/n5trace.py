#!/usr/bin/env python3
"""REFEREE-2 (own code): trace N5 (docs/new/N5-ssi-global.md pseudocode, steps 1-5) on DLM family 1 (Table 1, 2309.02223)
with brute-force sink-game play values (paper §2: Θ counts priorities on the path to the sink; ±inf for cycles) and the
order ⊴ (highest differing priority decides; even: more is better, odd: fewer is better). Valuations by enumeration of all
opponent strategies; τ̄(v) as the SET of choices of all pointwise-optimal Even responses to τ; Jσ(τ) as in Alg. 3.
Usage: n5trace.py n"""
import sys, itertools
import subprocess, re
fam, n = int(sys.argv[1]), int(sys.argv[2])
gen = sys.argv[3]
out = subprocess.run([sys.executable, '-I', gen, str(fam), str(n)], capture_output=True, text=True)
name = {}; raw = {}
for l in out.stdout.splitlines():
    m = re.match(r'^(\d+) (\d+) (\d+) ([\d,]+) "(\w+)";', l)
    if m: name[int(m.group(1))] = m.group(5); raw[m.group(5)] = (int(m.group(3)), int(m.group(2)), [int(x) for x in m.group(4).split(',')])
V = {x: (o, p, [name[y] for y in s]) for x, (o, p, s) in raw.items()}
start = {}
for l in out.stderr.splitlines():
    k, *pairs = l.split()
    start[k] = {name[int(a)]: name[int(b)] for a, b in (q.split(':') for q in pairs)}
SINK = f"a{n+1}"; P = sorted({p for _, p, _ in V.values()}, reverse=True)
V0 = [v for v in V if V[v][0] == 0]; V1 = [v for v in V if V[v][0] == 1]
INF = (2,); NINF = (-2,)
def theta(st, v):
    seen = []; x = v
    while x != SINK and x not in seen: seen.append(x); x = st[x]
    if x != SINK:
        cyc = seen[seen.index(x):]; top = max(V[y][1] for y in cyc)
        return INF if top % 2 == 0 else NINF
    cnt = {}
    for y in seen: cnt[V[y][1]] = cnt.get(V[y][1], 0) + 1
    return (0,) + tuple(cnt.get(p, 0) if p % 2 == 0 else -cnt.get(p, 0) for p in P)
def allstrats(owner, allowed=None):
    vs = V0 if owner == 0 else V1
    choices = [allowed[v] if allowed else V[v][2] for v in vs]
    for c in itertools.product(*choices): yield dict(zip(vs, c))
def evaluate(fixed, owner_fixed, allowed=None):
    """owner_fixed's strategy fixed; the other player optimizes pointwise (Odd: min, Even: max) over allowed choices.
    Returns (valuation dict, list of all pointwise-optimal responses)."""
    best = None; opts = []
    other = 1 - owner_fixed
    for r in allstrats(other, allowed):
        st = dict(fixed); st.update(r); val = {v: theta(st, v) for v in V}
        if best is None: best = dict(val)
        else:
            for v in V: best[v] = min(best[v], val[v]) if other == 1 else max(best[v], val[v])
    for r in allstrats(other, allowed):
        st = dict(fixed); st.update(r)
        if all(theta(st, v) == best[v] for v in V): opts.append(r)
    return best, opts
sigma = dict(start["SIGMA0"]); tau = dict(start["TAU0"])
it = 0
while True:
    Xs, sbar = evaluate(sigma, 0)          # Ξσ, optimal Odd counterstrategies σ̄
    Xt, tbar = evaluate(tau, 1)            # Ξτ, optimal Even responses τ̄
    Is = [(v, w) for v in V0 for w in V[v][2] if Xs[w] > Xs[sigma[v]]]
    It = [(v, w) for v in V1 for w in V[v][2] if Xt[w] < Xt[tau[v]]]
    if not Is and not It: print(f"STOP after {it} iterations; sigma={sigma} tau={tau}"); break
    As = {v: sorted({sigma[v]} | {w for (u, w) in Is if u == v}) for v in V0}
    _, sopts = evaluate(tau, 1, As)        # Even's optimum vs fixed τ in the restricted arena
    At = {v: sorted({tau[v]} | {w for (u, w) in It if u == v}) for v in V1}
    _, topts = evaluate(sigma, 0, At)      # Odd's optimum vs σ in the restricted arena
    it += 1
    print(f"--- iteration {it}: Iσ={Is} Iτ={It}  #optimal σ'={len(sopts)} #optimal τ'={len(topts)}")
    s2, t2 = sopts[0], topts[0]
    if len({tuple(sorted(o.items())) for o in sopts}) > 1 or len(topts) > 1: print("   NOTE: optimum not unique; taking the first")
    tbar_sets = {v: {o[v] for o in tbar} for v in V0}
    for v in V0:
        if s2[v] != sigma[v]:
            w = s2[v]; inJ = Xt[w] >= Xt[sigma[v]]
            print(f"   Even switch ({v},{w}): τ̄({v}) ∈ {sorted(tbar_sets[v])} -> {'w = τ̄(v) possible' if w in tbar_sets[v] else 'w ≠ τ̄(v) for EVERY optimal τ̄'};"
                  f" (v,w) {'∈' if inJ else '∉'} Jσ(τ) [Ξτ(w) {'⊵' if inJ else '◁'} Ξτ(σ(v))]; in Iσ: {(v, w) in Is}")
    for v in V1:
        if t2[v] != tau[v]:
            w = t2[v]; sb = {o[v] for o in sbar}; inJ = Xs[w] <= Xs[tau[v]]
            print(f"   Odd switch ({v},{w}): σ̄({v}) ∈ {sorted(sb)}; (v,w) {'∈' if inJ else '∉'} Jτ(σ)")
    if s2 == {v: sigma[v] for v in V0} and t2 == {v: tau[v] for v in V1}: print("   FALLBACK needed (not implemented)"); break
    sigma.update(s2); tau.update(t2)
