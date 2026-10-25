#!/usr/bin/env python3
"""L-SI succ. 10: own reproduction of REFEREE-2's N-NEEDB-5 (R2-N5-NEEDB.md, referee-2 ef433d32): the CONJECTURE "in scope, THR => M >= 0"
(docs/si/N5-LV3-box12.md §4-§5) fails on docs/referee-2/R2-N5-LV2/climb/block_9501.pg from its saved start pair.
Independent of REFEREE-2's code: the N5 loop is experiments/new/n5.py's run() transcribed (SPEC S1-S5), valuations from L-SI's
experiments/si/si.py Engine; W (the (sigma, tau)-play value), H1/H2/H3, R, gates, levels, r = lev(theta, w), M = max gate level are
computed here from the definitions (P-N5-RE §0, P-N5-LP §0). Usage: repro.py game.pg "s0 s1 ..." "t0 t1 ..." [all]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..", "..", "..")
sys.path.insert(0, os.path.join(ROOT, "experiments", "si")); sys.path.insert(0, os.path.join(ROOT, "experiments", "harness"))
import pg
from si import Engine
def dual(h): return pg.Game([p + 1 for p in h.prio], [1 - o for o in h.owner], [list(s) for s in h.succ])

def n5_states(g, sigma, tau, cap=200):
    E, Ed = Engine(g), Engine(dual(g)); n = g.n; out = []
    while len(out) < cap:
        vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
        vt, tbar = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
        out.append((list(sigma), list(tau), vs, sbar, Is))
        if not Is and not It: return out, E
        ns, nt = list(sigma), list(tau); fb = False
        if Is:
            opt = {v: {sigma[v]} for v in range(n) if g.owner[v] == 0}
            for v, w in Is: opt[v].add(w)
            succ = [sorted(opt[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]
            _, best = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ))).evaluate(tuple(tau[v] if g.owner[v] == 1 else -1 for v in range(n)))
            for v in range(n):
                if g.owner[v] == 0: ns[v] = best[v]
        if It:
            opt = {v: {tau[v]} for v in range(n) if g.owner[v] == 1}
            for v, w in It: opt[v].add(w)
            succ = [sorted(opt[v]) if g.owner[v] == 1 else [sigma[v]] for v in range(n)]
            _, best = Engine(pg.Game(list(g.prio), list(g.owner), succ)).evaluate(tuple(sigma[v] if g.owner[v] == 0 else -1 for v in range(n)))
            for v in range(n):
                if g.owner[v] == 1: nt[v] = best[v]
        if ns == sigma and nt == tau:
            fb = True
            if Is:
                for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
            else:
                for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
        out[-1] = out[-1] + (fb,)
        sigma, tau = ns, nt
    return out, E

def play_val(E, f, v):
    seq, pos, x = [], {}, v
    while x not in pos: pos[x] = len(seq); seq.append(x); x = f[x]
    cyc = seq[pos[x]:]; c = max(cyc, key=lambda u: E.rank[u]); i = seq.index(c)
    mask = 0
    for u in seq[:i]:
        if E.rank[u] > E.rank[c]: mask |= E.bit[u]
    return (c, mask, i)

def returns(f, o):
    x, seen = f[o], set()
    while x not in seen:
        if x == o: return True
        seen.add(x); x = f[x]
    return False

def lev(E, a, b):
    if a == b: return None
    if a[0] != b[0]: return "inf"
    if a[1] != b[1]: return (a[1] ^ b[1]).bit_length() - 1
    return -1

def main():
    g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%")))
    s0 = [int(x) for x in sys.argv[2].split()]; t0 = [int(x) for x in sys.argv[3].split()]
    odds = [v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1]; assert len(odds) == 1, odds; o = odds[0]
    sigma = [s0[v] if g.owner[v] == 0 else -1 for v in range(g.n)]; tau = [t0[v] if g.owner[v] == 1 else -1 for v in range(g.n)]
    for v in range(g.n):
        if g.owner[v] == 1 and v != o: tau[v] = g.succ[v][0]
    states, E = n5_states(g, sigma, tau)
    print(f"o = {o}, n = {g.n}, states {len(states)}, fallbacks at {[k for k, s in enumerate(states) if len(s) > 5 and s[5]]}")
    for k, st in enumerate(states):
        sg, tu, Xi, sbar, Is = st[:5]
        f = [sg[v] if g.owner[v] == 0 else tu[v] for v in range(g.n)]
        fh = list(f); fh[o] = sbar[o]
        W = [play_val(E, f, v) for v in range(g.n)]
        R = {v for v in range(g.n) if any(True for _ in [0]) and (lambda v: (lambda seen: None)(set()))(v) is None}
        R = set()
        for v in range(g.n):
            x, seen = v, set()
            while x not in seen and x != o: seen.add(x); x = f[x]
            if x == o: R.add(v)
        H1, H2 = not returns(fh, o), not returns(f, o)
        th, w = Xi[o], W[o]; H3 = th[0] == w[0]; hh = H1 and H2 and H3
        r = lev(E, th, w) if H3 else "inf"
        gates = [(y, z, lev(E, Xi[sg[y]], Xi[z])) for y, z in Is]
        M = max((L for _, _, L in gates if L != "inf"), default=None)
        thr = hh and any(Xi[v] != W[v] for v in range(g.n))
        kinds = [("beta" if (y in R and z not in R) else "R->R" if y in R else "F->R" if z in R else "F->F") for y, z, _ in gates]
        print(f"state {k}: fb={st[5] if len(st) > 5 else '-'} (h)={hh} THR={thr} H1={H1} H2={H2} theta={th[0]},{bin(th[1])},{th[2]} "
              f"w={w[0]},{bin(w[1])},{w[2]} r={r} M={M} c_theta={th[0]} rank(o)={E.rank[o]} rank(c)={E.rank[th[0]]} R={sorted(R - {o})} "
              f"gates={[(y, z, L, kd) for (y, z, L), kd in zip(gates, kinds)]} lambda_key={tuple(x[0] for x in Xi)} tau(o)={tu[o]}")
if __name__ == "__main__": main()
