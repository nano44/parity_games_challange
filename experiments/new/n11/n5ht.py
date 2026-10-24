#!/usr/bin/env python3
"""N11 = N5-HT (docs/new/N11-proposal.md, section "FREEZE"): N5 (experiments/new/n5.py, SPEC S1-S5) with an honest override at
trust conflicts in S4a/S4b. Engine: L-SI's si.py (read-only), dual game as in n5.py.
S4a' (Even, only if Iσ ≠ ∅):
  1. σ_W := N5's S4a step (arena optimum against τ, exactly n5.py's code).
  2. C := {Even x with some (x, z) ∈ Iσ : key(Ξσ(σ_W(x))) < max_{(x,z) ∈ Iσ} key(Ξσ(z))}   (key = si.py Engine.key at the CURRENT σ)
  3. for x ∈ C: σ'(x) := argmax_{(x,z) ∈ Iσ} (key(Ξσ(z)), z); elsewhere σ'(x) := σ_W(x).
S4b' (Odd, only if Iτ ≠ ∅): the same on G^d with Ξτ, Iτ, Ed.key, from N5's S4b step τ_W.
S4c: unchanged from N5 (if σ' = σ and τ' = τ: one switch-all fallback, Even first, ties (key, w) by max).
Both steps from the same (σ, τ); stop when Iσ = Iτ = ∅; output Engine.regions(σ) as n5.py.
Usage: n5ht.py game.pg out.sol [--start "SIGMA0 ..." "TAU0 ..."] [--cap K]   (prints RESULT iterations=.. fallback=.. conflicts=..)"""
import sys, os, time
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
for p in ("experiments/new", "experiments/si", "experiments/harness"): sys.path.insert(0, os.path.join(ROOT, p))
import pg, n5
from si import Engine
dual = n5.dual

def override(owner_side, g, Eng, strat_W, I, val):
    """Steps 2-3 for one player. strat_W: list; I: improving edges; val: valuations at the CURRENT strategy. Returns (new, |C|)."""
    best = {}
    for v, w in I:
        k = (Eng.key(val[w]), w)
        if v not in best or k > best[v]: best[v] = k
    out = list(strat_W); c = 0
    for v, (kb, wb) in best.items():
        if Eng.key(val[strat_W[v]]) < kb:
            out[v] = wb; c += 1
    return out, c

def step(g, E, Ed, sigma, tau, ht=True):
    """One N5-HT iteration (ht=False: plain N5, identical to n5.py's loop). Returns None or (ns, nt, fb, cE, cO)."""
    n = g.n
    vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
    vt, tbar = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
    if not Is and not It: return None
    ns, nt = list(sigma), list(tau); cE = cO = 0
    if Is:
        opt = {v: {sigma[v]} for v in range(n) if g.owner[v] == 0}
        for v, w in Is: opt[v].add(w)
        succ = [sorted(opt[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]
        Er = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ)))
        _, best = Er.evaluate(tuple(tau[v] if g.owner[v] == 1 else -1 for v in range(n)))
        for v in range(n):
            if g.owner[v] == 0: ns[v] = best[v]
        if ht: ns, cE = override(0, g, E, ns, Is, vs)
    if It:
        opt = {v: {tau[v]} for v in range(n) if g.owner[v] == 1}
        for v, w in It: opt[v].add(w)
        succ = [sorted(opt[v]) if g.owner[v] == 1 else [sigma[v]] for v in range(n)]
        Er = Engine(pg.Game(list(g.prio), list(g.owner), succ))
        _, best = Er.evaluate(tuple(sigma[v] if g.owner[v] == 0 else -1 for v in range(n)))
        for v in range(n):
            if g.owner[v] == 1: nt[v] = best[v]
        if ht: nt, cO = override(1, g, Ed, nt, It, vt)
    fb = 0
    if ns == list(sigma) and nt == list(tau):
        fb = 1
        if Is:
            for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
        else:
            for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
    return ns, nt, fb, cE, cO

def run(g, start=None, cap=10 ** 6, ht=True, trace=False):
    E, Ed = Engine(g), Engine(dual(g))
    sigma, tau = list(E.initial("best")), list(Ed.initial("best"))
    if start:
        for v, w in start[0].items(): sigma[v] = w
        for v, w in start[1].items(): tau[v] = w
    it = fb = conf = 0; states = [(tuple(sigma), tuple(tau))]
    while it < cap:
        r = step(g, E, Ed, sigma, tau, ht)
        if r is None: break
        sigma, tau, f, cE, cO = r; it += 1; fb += f; conf += cE + cO
        if trace: states.append((tuple(sigma), tuple(tau)))
    win, ws = E.regions(tuple(sigma))
    return it, fb, conf, win, ws, states

if __name__ == "__main__":
    path, out = sys.argv[1], sys.argv[2]
    cap = int(sys.argv[sys.argv.index("--cap") + 1]) if "--cap" in sys.argv else 10 ** 6
    g = pg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%")))
    st = None
    if "--start" in sys.argv:
        k = sys.argv.index("--start")
        st = tuple(dict(map(int, t.split(":")) for t in sys.argv[k + j].split()[1:]) for j in (1, 2))
    t0 = time.time(); it, fb, conf, win, ws, _ = run(g, st, cap)
    with open(out, "w") as f:
        f.write(f"paritysol {g.n - 1};\n")
        for v in range(g.n): f.write(f"{v} {win[v]} {ws[v]};\n" if ws[v] is not None else f"{v} {win[v]};\n")
    print(f"RESULT mode=n5ht n={g.n} iterations={it} fallback={fb} conflicts={conf} capped={int(it >= cap)} secs={time.time() - t0:.2f}")
