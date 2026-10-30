#!/usr/bin/env python3
"""L-NEW box 68: anatomy of in-phase Even fallbacks and S4a gap re-openings (plain N5, box21/n5x.step; START optional).
Z_t = {v : Xi_t(v) != W_t(v)}, W = val(sigma, tau) on G_tau. Per in-phase fallback: Z-FLAT iff Z_{k+1} = Z_k.
Checks (must be 0):
  SWOUT   a fallback switches an Even v off its own Xi-cycle with v not in Z_k (Lemma SW-IN);
  REOPNW  an in-phase S4a step puts v into Z with W(v) unchanged (Lemma REOPEN-W).
Reports for Z-flat fallbacks: how many change W somewhere (WCH), the number switched, |Z|; per phase the max of Z-flat fallbacks, and of
the number of distinct Xi cycle nodes / distinct W cycle nodes of Z at the phase's Z-flat fallbacks; re-openings per phase and the
per-phase sum over v of W(v)-changes at in-phase S4a steps (the charge of REOPEN-W).
Usage: zflat.py GAME.pg [START]"""
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
Wc = {}
def W(s, t):
    if t not in Wc: Wc[t] = Engine(pg.Game(list(g.prio), list(g.owner), [[t[v]] if g.owner[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[t].evaluate(s)[0]
def st(s, t):
    vx, _ = E.evaluate(s); w = W(s, t)
    return dict(x=vx, w=w, lx=tuple(vx[v][0] for v in range(n)), Z=frozenset(v for v in range(n) if vx[v] != w[v]))
cur = st(s, t)
C = dict(fb=0, zflat=0, zflat_wch=0, swout=0, reop=0, reopnw=0, sa=0)
ph = dict(zf=0, reop=0, wch=0); worst = dict(zf=0, reop=0, wch=0); zf_cn = []; maxcn = (0, 0)
def close():
    for k in ph: worst[k] = max(worst[k], ph[k])
while True:
    r = step(g, E, Ed, list(s), list(t))
    if r is None: break
    ns, nt, _, _, fb, _, _ = r; ns, nt = tuple(ns), tuple(nt)
    nx = st(ns, nt)
    inph = nt == t and nx["lx"] == cur["lx"]
    if not inph:
        close(); ph = dict(zf=0, reop=0, wch=0)
    elif fb:
        C["fb"] += 1
        sw = [v for v in range(n) if ns[v] != s[v]]
        for v in sw:
            if cur["x"][v][0] != v and v not in cur["Z"]: C["swout"] += 1
        if nx["Z"] == cur["Z"]:
            C["zflat"] += 1; ph["zf"] += 1
            if nx["w"] != cur["w"]: C["zflat_wch"] += 1
            Z = cur["Z"]
            maxcn = max(maxcn, (len({cur["x"][v][0] for v in Z}), len({cur["w"][v][0] for v in Z})))
    else:
        C["sa"] += 1
        for v in nx["Z"] - cur["Z"]:
            C["reop"] += 1; ph["reop"] += 1
            if nx["w"][v] == cur["w"][v]: C["reopnw"] += 1
        ph["wch"] += sum(1 for v in range(n) if nx["w"][v] != cur["w"][v])
    s, t, cur = ns, nt, nx
close()
print(f"ZFLAT {os.path.basename(p)} n {n} {C} worst-phase {worst} max-cyclenodes-of-Z-at-zflat {maxcn}")
