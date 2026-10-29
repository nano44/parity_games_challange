#!/usr/bin/env python3
"""T44: independent re-check of an sfw ("arena by W") run. Replays sfw's steps (pieces of T44-sf-variants.py) and checks each step
against a separate valuation computed by SIMULATING the deterministic (sigma, tau) play (no si.py Engine): (1) the arena equals the set
of edges that are W-improving by simulation, for both players; (2) the selected strategy is optimal in its arena (no arena edge is
W-improving at the new strategy vs the opponent's old one; one-player local = global optimality); (3) every switched edge is strictly
W-improving. Prints the switches per step and "== state k" when a state repeats.
Run from the repo root: python3 -I docs/lit/T44-sfw-cycle-check.py game.pg startfile steps   (startfile may have empty SIGMA0/TAU0 lines)"""
import sys, os, importlib.util
sys.path[:0] = [os.path.join(os.getcwd(), p) for p in ("experiments/new", "experiments/si", "experiments/harness")]
spec = importlib.util.spec_from_file_location("v", "docs/lit/T44-sf-variants.py"); V = importlib.util.module_from_spec(spec); spec.loader.exec_module(V)
import pg, n5
from si import Engine
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); st = V.readstart(sys.argv[2]); n = g.n
names = {}
for l in open(sys.argv[1]):
    t = l.split()
    if len(t) > 4: names[int(t[0])] = t[4].strip('";')
# independent valuation by simulation of the deterministic (sigma, tau) play
order = sorted(range(n), key=lambda v: (g.prio[v], v)); rank = {v: r for r, v in enumerate(order)}
def val(v, s, t):
    path = []; pos = {}
    x = v
    while x not in pos:
        pos[x] = len(path); path.append(x); x = s[x] if g.owner[x] == 0 else t[x]
    cyc = path[pos[x]:]; c = max(cyc, key=lambda u: rank[u]); k = path.index(c)
    P = [u for u in path[:k] if rank[u] > rank[c]]
    wsum = sum((1 if g.prio[u] % 2 == 0 else -1) * 2 ** rank[u] for u in P)
    rc = (2 * rank[c] + g.prio[c] % 2); rew = rc if g.prio[c] % 2 == 0 else -rc
    return (rew, wsum, k if g.prio[c] % 2 == 1 else -k)   # larger = better for Even
E, Ed = Engine(g), Engine(n5.dual(g))
s, t = list(E.initial("best")), list(Ed.initial("best"))
for v, w in st[0].items(): s[v] = w
for v, w in st[1].items(): t[v] = w
states = [(tuple(s), tuple(t))]
for it in range(int(sys.argv[3])):
    # replicate sfw step via the module's pieces
    gt = V.restricted(g, [g.succ[v] if g.owner[v] == 0 else [t[v]] for v in range(n)])
    Ew = Engine(gt); vw, _ = Ew.evaluate(tuple(s)); Isw = Ew.improving(tuple(s), vw)
    gs = V.restricted(g, [g.succ[v] if g.owner[v] == 1 else [s[v]] for v in range(n)])
    Ewd = Engine(n5.dual(gs)); vwd, _ = Ewd.evaluate(tuple(t)); Itw = Ewd.improving(tuple(t), vwd)
    ar = {v: {s[v]} | {w for x, w in Isw if x == v} for v in range(n) if g.owner[v] == 0}
    ns = V.sel_vs(g, ar, t) if Isw else list(s)
    ar2 = {v: {t[v]} | {w for x, w in Itw if x == v} for v in range(n) if g.owner[v] == 1}
    nt = V.sel_vs_odd(g, ar2, s) if Itw else list(t)
    ch = []
    simE = {(v, w) for v in range(n) if g.owner[v] == 0 for w in g.succ[v] if w != s[v] and val(w, s, t) > val(s[v], s, t)}
    simO = {(v, w) for v in range(n) if g.owner[v] == 1 for w in g.succ[v] if w != t[v] and val(w, s, t) < val(t[v], s, t)}
    assert simE == set(Isw) and simO == set(Itw), "arena mismatch"
    for v in range(n):
        if g.owner[v] == 0:
            assert all(not (val(w, ns, t) > val(ns[v], ns, t)) for w in ar[v]), ("Even not optimal in arena", v)
        if g.owner[v] == 1:
            assert all(not (val(w, s, nt) < val(nt[v], s, nt)) for w in ar2[v]), ("Odd not optimal in arena", v)
    for v in range(n):
        if g.owner[v] == 0 and ns[v] != s[v]:
            ok = val(ns[v], s, t) > val(s[v], s, t); ch.append(f"E {names[v]}->{names[ns[v]]}{'' if ok else '!NOTW'}")
        if g.owner[v] == 1 and nt[v] != t[v]:
            ok = val(nt[v], s, t) < val(t[v], s, t); ch.append(f"O {names[v]}->{names[nt[v]]}{'' if ok else '!NOTW'}")
    s, t = [ns[v] if g.owner[v] == 0 else -1 for v in range(n)], [nt[v] if g.owner[v] == 1 else -1 for v in range(n)]
    key = (tuple(s), tuple(t)); rep = states.index(key) if key in states else None; states.append(key)
    print(it + 1, " ".join(ch), "" if rep is None else f"== state {rep}")
