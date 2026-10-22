#!/usr/bin/env python3
"""Box 10 (L-NEW): frozen-σ TAIL simulator and the gadgeted Odd-CDAG family.
Tail = N5's run from a pair (σ, τ0) in which σ is already Even-optimal (Iσ = ∅), so Even never moves (Iσ depends on σ only) and every
iteration is N5's Odd step (n5_lock.step = n5.py's loop, unmodified): τ' = Odd's optimum in G_σ over the arena {τ(o)} ∪ Iτ(o), where
Iτ = Odd's VJ00 improvements against Even's FRESH best reply τ̄(τ) (dual game). Family: Odd vertices 1..n form the dual CDAG (edges
x -> u for u < x, sink 0); every edge x -> u passes an Even gadget e[x,u] with σ(e[x,u]) = u and optional EXPLOIT edges to other
vertices. Even's exploits (used by τ̄, never by σ) are the masks of Odd's improvement gate.
Vertex ids: 0 = sink (Odd, prio 1, self-loop); v = 1..n Odd, prio 2(n+1-v)+1 (v = 1 most relevant); gadgets prio 0 (never in path sets)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..")); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import pg
from n5 import Engine, dual
from n5_lock import step

def build(n, exploits, gadget_prio=0, sink_prio=1):
    """exploits: dict (x,u) -> list of exploit targets; a target is an Odd vertex id (0..n) or a pair (x',u') naming gadget e[x',u'].
    Returns (game, sigma (full list, -1 at Odd), gid dict (x,u)->vertex id)."""
    prio = [sink_prio] + [2 * (n + 1 - v) + 1 for v in range(1, n + 1)]; owner = [1] * (n + 1); succ = [[0]] + [[] for _ in range(n)]
    gid = {}
    for x in range(1, n + 1):
        for u in range(x):
            gid[(x, u)] = len(prio); prio.append(gadget_prio); owner.append(0); succ.append([u])
            succ[x].append(gid[(x, u)])
    sigma = [-1] * len(prio)
    for (x, u), e in gid.items():
        sigma[e] = u
        for t in exploits.get((x, u), []):
            tv = gid[t] if isinstance(t, tuple) else t
            if tv not in succ[e]: succ[e].append(tv)
    g = pg.Game(prio, owner, [sorted(s) for s in succ])
    return g, sigma, gid

def tail(g, sigma, tau0, cap=100000, trace=False):
    """Run N5 (n5_lock.step) from (sigma, tau0). Returns dict: steps, even_moves, fallbacks, optimal_sigma (Iσ = ∅ at start), history of
    (switched Odd vertices with old->new target as (x, u_old, u_new) in CDAG terms when gadgets are used), and capped flag."""
    E, Ed = Engine(g), Engine(dual(g)); s, t = list(sigma), list(tau0)
    vs, _ = E.evaluate(tuple(s)); opt = not E.improving(tuple(s), vs)
    hist = []; em = fb = k = 0
    while k < cap:
        r = step(g, E, Ed, s, t)
        if r is None: break
        ns, nt, f = r[0], r[1], r[2]
        em += ns != s; fb += f
        sw = [(v, t[v], nt[v]) for v in range(g.n) if g.owner[v] == 1 and nt[v] != t[v]]
        hist.append((sw, f, r[3], r[4]))
        if trace: print(k, "switch", sw, "fb" if f else "", "|Iσ|", r[3], "|Iτ|", r[4])
        s, t = ns, nt; k += 1
    return dict(steps=k, even_moves=em, fallbacks=fb, optimal_sigma=opt, hist=hist, capped=k >= cap, sigma=s, tau=t)

def cdag_target(g, gid, t):
    """Map an Odd vertex's successor (a gadget id or the sink) to the CDAG target u."""
    inv = {e: u for (x, u), e in gid.items()}
    return inv.get(t, t)

def tau_all_sink(g, gid, n):
    t = [-1] * g.n; t[0] = 0
    for x in range(1, n + 1): t[x] = gid[(x, 0)]
    return t

if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    g, sigma, gid = build(n, {})
    r = tail(g, sigma, tau_all_sink(g, gid, n), trace=True)
    print({k: v for k, v in r.items() if k not in ("hist", "sigma", "tau")})
