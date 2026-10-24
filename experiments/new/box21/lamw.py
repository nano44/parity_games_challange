#!/usr/bin/env python3
"""Box 21: for the N5 run from (sigma_0, tau*): W = play values vs tau* (one-player game G_tau*), λ_W-phases (cycle nodes of W),
W-changing steps per λ_W-phase, and the one-player Lemma P check in G_tau* (simple paths <= k edges to a cycle node of the phase start).
Writes the start file (n5.py --start format) next to the game. Usage: lamw.py game.pg"""
import sys
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))  # box21 -I: find sibling modules
from n5x import *
from h1 import wvals
def paths_ok(g, tau, sig_start, sig_k, k, Eg0):
    """Lemma P in H = G_tau: W_k(x) >= value(r) for every simple path r of <= k edges from x to a cycle node u of W_0. Returns violations."""
    n = g.n; W0 = wvals(g, sig_start, tau)[1]; Eg, Wk = wvals(g, sig_k, tau)
    cyc = [u for u in range(n) if W0[u][0] == u]
    succH = [g.succ[v] if g.owner[v] == 0 else [tau[v]] for v in range(n)]
    viol = []
    for u in cyc:
        # DFS backwards from u over simple paths of <= k edges: value(r) = (u, P(r), L)
        def rec(x, P, L, on):
            if L > 0 or x == u:
                val = (u, P, L)
                if Eg.key(Wk[x]) < Eg.key(val): viol.append((x, u, L))
            if L == k: return
            for y in range(n):
                if x in succH[y] and y not in on:
                    rec(y, P | (Eg.bit[y] if Eg.rank[y] > Eg.rank[u] else 0), L + 1, on | {y})
        rec(u, 0, 0, {u})
    return viol
def main(path):
    g = load(path); n = g.n
    states, _ = trace(g); s0, ts = states[0][0], states[-1][1]
    st = ({v: s0[v] for v in range(n) if g.owner[v] == 0}, {v: ts[v] for v in range(n) if g.owner[v] == 1})
    with open(path[:-3] + ".start", "w") as f:
        f.write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in sorted(st[0].items())) + "\n")
        f.write("TAU0 " + " ".join(f"{v}:{w}" for v, w in sorted(st[1].items())) + "\n")
    fs, _ = trace(g, st)
    Ws = [wvals(g, s, ts)[1] for s, _ in fs]
    lam = [tuple(w[0] for w in W) for W in Ws]
    phase_start = 0; cnt = 0; out = []
    for k in range(1, len(fs)):
        if lam[k] != lam[k - 1]:
            out.append(cnt); cnt = 0; phase_start = k
        cnt += Ws[k] != Ws[k - 1]
        v = paths_ok(g, ts, fs[phase_start][0], fs[k][0], k - phase_start, None)
        if v: print(f"Lemma P (G_tau*) violated at step {k} (phase step {k - phase_start}): {len(v)} violations, e.g. {v[:3]}")
    out.append(cnt)
    print(f"plain N5 iterations {len(states)-1}; from (sigma0, tau*): {len(fs)-1}; W-changing steps per λ_W-phase: {out}; n-1 = {n-1}")
if __name__ == "__main__": main(sys.argv[1])
