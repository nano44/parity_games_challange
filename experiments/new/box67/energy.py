#!/usr/bin/env python3
"""L-NEW box 67: candidate Lyapunov energies for N5's in-phase Even fallbacks (S4c). Phase = maximal run with (lambda_Xi, tau)
constant (RESULTS R38 (a)); an in-phase fallback is an S4c transition with both states in the phase. For each candidate E, counts
  FBUP:  in-phase fallbacks at which E does NOT strictly decrease (must be 0 for "E drops at every fallback");
  SAUP:  in-phase non-fallback transitions at which E increases (must be 0 for "E never rises in a phase").
A candidate with FBUP = SAUP = 0 and range <= R bounds in-phase fallbacks per phase by R.
Candidates (W = val(sigma, tau) on G_tau, D = {Odd u : sbar(u) != tau(u)}):
  E1 = #Even v with I_sigma(v) nonempty;          E2 = sum of (rank(v) + 1) over those v;
  E3 = #vertices v with Xi(v) != W(v);            E4 = |D| (open gates);
  E5 = #vertices whose (sigma, tau)-play meets D;  E6 = #blocked Even edges (W-better than sigma's choice, not in I_sigma).
ZGROW: Even fallbacks with tau unchanged at which Z = {v : Xi(v) != W(v)} gains a vertex (Lemma GAP-MON: must be 0).
Plain N5 (box21/n5x.step). Usage: energy.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
p = sys.argv[1]; g = load(p); n = g.n
start = readstart(sys.argv[2]) if len(sys.argv) > 2 else None
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); s, t = tuple(s), tuple(t)
bad = [(v, w) for d in (start or ({}, {})) for v, w in d.items() if w not in g.succ[v]]
if bad:                                   # P-N5-GAP fixes H8 (REFEREE-2 N-GAP-7): a start pair must use edges of G
    print(f"INVALID-START {os.path.basename(p)} non-edges {bad}"); sys.exit(2)
rank = {v: r for r, v in enumerate(sorted(range(n), key=lambda v: (g.prio[v], v)))}
Wc = {}
def W(s, t):
    if t not in Wc: Wc[t] = Engine(pg.Game(list(g.prio), list(g.owner), [[t[v]] if g.owner[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[t].evaluate(s)[0], Wc[t]
def energies(s, t):
    vx, sb = E.evaluate(s); Is = E.improving(s, vx); w, Ew = W(s, t)
    imp = {v for v, _ in Is}; Iset = set(Is)
    D = {u for u in range(n) if g.owner[u] == 1 and sb[u] != t[u]}
    def meets(v):
        seen = set(); x = v
        while x not in seen:
            if x in D: return True
            seen.add(x); x = s[x] if g.owner[x] == 0 else t[x]
        return False
    bl = sum(1 for v in range(n) if g.owner[v] == 0 for x in g.succ[v]
             if x != s[v] and Ew.key(w[x]) > Ew.key(w[s[v]]) and (v, x) not in Iset)
    e = (len(imp), sum(rank[v] + 1 for v in imp), sum(1 for v in range(n) if vx[v] != w[v]), len(D),
         sum(1 for v in range(n) if meets(v)), bl)
    return e, tuple(vx[x][0] for x in range(n)), frozenset(v for v in range(n) if vx[v] != w[v])
K = 6; FBUP = [0] * K; SAUP = [0] * K; fbn = 0; fmax = 0; f = 0
cur, lx, Z = energies(s, t); ZGROW = 0
ph = dict(e3s=cur[2], up3=0, drop3=0); worst = dict(f=0, e3s=0, up3=0, drop3=0)
while True:
    r = step(g, E, Ed, list(s), list(t))
    if r is None: break
    ns, nt, _, _, fb, _, _ = r; ns, nt = tuple(ns), tuple(nt)
    nxt, nlx, nZ = energies(ns, nt)
    if fb and nt == t and not nZ <= Z: ZGROW += 1
    inphase = nt == t and nlx == lx
    if not inphase:
        f = 0; ph = dict(e3s=nxt[2], up3=0, drop3=0)
    elif fb:
        fbn += 1; f += 1; fmax = max(fmax, f); ph['drop3'] += cur[2] - nxt[2]
        if f > worst['f']: worst = dict(f=f, e3s=ph['e3s'], up3=ph['up3'], drop3=ph['drop3'])
        for i in range(K):
            if not nxt[i] < cur[i]: FBUP[i] += 1
    else:
        ph['up3'] += max(0, nxt[2] - cur[2])
        for i in range(K):
            if nxt[i] > cur[i]: SAUP[i] += 1
    s, t, cur, lx, Z = ns, nt, nxt, nlx, nZ
print(f"ENERGY {os.path.basename(p)} n {n} inphase-fb {fbn} fmax {fmax} FBUP {FBUP} SAUP {SAUP} worst-phase {worst} ZGROW {ZGROW}")
