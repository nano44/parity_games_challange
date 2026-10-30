#!/usr/bin/env python3
"""L-SI box 42 (from L-NEW box64/late.py, read-only copy): per W-run, late adoptions split FIRST (first late adoption of the edge in the W-run) / REPEAT; for a REPEAT, RV counts the cases where W(z) did not rise between y's last leave of z and the adoption and y is off-cycle (Lemma LATE-REPEAT says 0). MAXE = most late adoptions of one edge in one W-run. Orig doc: L-NEW box 65: late adoptions in W-runs (box 64 §1.8; fallback-free, tau and lambda_W constant) of plain N5, S3 start
(--start: GAME.start). For each adoption at transition u of an edge (y, z) that was blocked at an earlier state t of the W-run
(W_t(z) > W_t(rho_t y), (y, z) not in I_sigma_t), take t = the LATEST such state and test:
  XI: Xi_u(z) strictly above Xi_t(z) (box 64 §5.2 READING);  W: W_u(z) strictly above W_t(z) (the §5.3 (b) question).
Usage: late.py GAME.pg [--start]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
p = sys.argv[1]; g = load(p); n = g.n
start = readstart(p[:-3] + ".start") if "--start" in sys.argv and os.path.exists(p[:-3] + ".start") else None
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); s, t = tuple(s), tuple(t)
Wc = {}
def W(s, t):
    if t not in Wc: Wc[t] = Engine(pg.Game(list(g.prio), list(g.owner), [[t[v]] if g.owner[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[t].evaluate(s)[0], Wc[t]
def info(s, t):
    vx, _ = E.evaluate(s); Is = set(E.improving(s, vx)); w, Ew = W(s, t)
    bl = {(v, x) for v in range(n) if g.owner[v] == 0 for x in g.succ[v]
          if x != s[v] and Ew.key(w[x]) > Ew.key(w[s[v]]) and (v, x) not in Is}
    return vx, w, Ew, bl
c = dict(late=0, xi_rise=0, w_rise=0, neither=0, first=0, repeat=0, RV=0, cyc=0, MAXE=0)
seen = {}; leftW = {}
vx, w, Ew, bl = info(s, t); last = {e: (vx, w) for e in bl}
while True:
    r = step(g, E, Ed, list(s), list(t))
    if r is None: break
    ns, nt, _, _, fb, _, _ = r; ns, nt = tuple(ns), tuple(nt)
    if nt != t or ns == s:
        s, t = ns, nt; vx, w, Ew, bl = info(s, t); last = {e: (vx, w) for e in bl}; seen = {}; leftW = {}; continue
    vx2, w2, Ew2, bl2 = info(ns, t)
    if fb or any(w2[x][0] != w[x][0] for x in range(n)):
        last = {}; seen = {}; leftW = {}
    else:
        for y in range(n):
            if g.owner[y] == 0 and ns[y] != s[y]: leftW[(y, s[y])] = Ew.key(w2[s[y]])   # W of the left target at the state after the leave
        for y in range(n):
            if g.owner[y] == 0 and ns[y] != s[y] and (y, ns[y]) in last:
                z = ns[y]; vt, wt = last[(y, z)]; c["late"] += 1
                xr = E.key(vx2[z]) > E.key(vt[z]); wr = Ew.key(w2[z]) > Ew.key(wt[z])
                c["xi_rise"] += xr; c["w_rise"] += wr; c["neither"] += (not xr and not wr)
                k = seen.get((y, z), 0); seen[(y, z)] = k + 1; c["MAXE"] = max(c["MAXE"], k + 1)
                if k == 0: c["first"] += 1
                else:
                    c["repeat"] += 1
                    if (y, z) in leftW and not Ew.key(w2[z]) > leftW[(y, z)]:
                        if w2[y][0] == y or w[y][0] == y: c["cyc"] += 1
                        else: c["RV"] += 1
    for e in bl2: last[e] = (vx2, w2)
    s, vx, w, Ew, bl = ns, vx2, w2, Ew2, bl2
print(f"LATE {os.path.basename(p)} n {n} {c}")
