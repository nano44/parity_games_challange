#!/usr/bin/env python3
"""L-SI box 50 (second series; docs/si/N5-FL-box50b.md): FL_F, the W-FLAT transitions of a W-run F (R89 STRETCH-RED: «transitions with
sigma_{t+1} != sigma_t and W_{t+1} = W_t»; every transition of a W-run moves sigma). W-runs as in latep.py (tau constant, no S4c fallback,
lambda_W constant). For every switch v: d -> e at a W-flat transition t -> t+1:
 NOTZ_V: v not in Z_t (Xi_t(v) = W_t(v)); NOCL_V: Xi(v) does not strictly rise; WCH_V: W(v) changes (must be 0 at a flat transition);
 GXC: lambda_Xi unchanged at t (so (v, t) is a GXC event); NEW: (v, e) not in H_{t-1} (t-1 in F); OLDIN: (v, e) in H_{t-1}; IDXDN: e < d.
Per W-constant interval I of F (a maximal run of states of F with equal W): FLV = most flat switches of one vertex in I; FLI = most flat
transitions in I; and FLVD_V counts (v, I) with more flat switches than d_out(v) - 1.
Box 50b GAP route: ZFL = flat transitions with Z unchanged (max per W-run); ZA = |Z_a| (max); ZSHR_V flat transitions where Z does
not shrink weakly (must be 0); ZIN_V entries into Z without a W-change of the vertex (must be 0); FLGAP_V W-runs with
FL_F > |Z_a| + sum_v WCH_F(v) + ZFL_F (must be 0).
Output maxima over W-runs: FL (max FL_F), FLI, FLV, LCTFL (flat transitions with a lambda_Xi change); sums: SW (flat switches), the _V
counters, GXC, NEW, OLDIN, IDXDN, FLVD_V. Usage: flat.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
def run(g, start=None):
    n = g.n; E, Ed = Engine(g), Engine(dual(g))
    s, t = start_pair(g, E, Ed, start); s, t = tuple(s), tuple(t)
    WE = {}
    def W(s, t):
        if t not in WE: WE[t] = Engine(pg.Game(list(g.prio), list(g.owner), [[t[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(n)]))
        e = WE[t]; w = e.evaluate(s)[0]; return w, [e.key(x) for x in w]
    def X(s):
        vx, _ = E.evaluate(s); return vx, [E.key(x) for x in vx], set(E.improving(s, vx))
    c = dict(ZFL=0, ZA=0, ZSHR_V=0, ZIN_V=0, FLGAP_V=0, FL=0, FLI=0, FLV=0, LCTFL=0, SW=0, NOTZ_V=0, NOCL_V=0, WCH_V=0, GXC=0, NEW=0, OLDIN=0, IDXDN=0, FLVD_V=0)
    def newrun(s, t):
        w, wk = W(s, t); x = X(s); Z = {v for v in range(n) if x[1][v] != wk[v]}
        return dict(w=w, wk=wk, x=x, Hprev=None, fl=0, fli=0, flv={}, lct=0, Z=Z, za=len(Z), zfl=0, wchv=0)
    def close(R):
        c['FL'] = max(c['FL'], R['fl']); c['LCTFL'] = max(c['LCTFL'], R['lct']); c['ZFL'] = max(c['ZFL'], R['zfl']); c['ZA'] = max(c['ZA'], R['za'])
        if R['fl'] > R['za'] + R['wchv'] + R['zfl']: c['FLGAP_V'] += 1
    R = newrun(s, t)
    while True:
        r = step(g, E, Ed, list(s), list(t))
        if r is None: break
        ns, nt, _, _, fb, _, _ = r; ns, nt = tuple(ns), tuple(nt)
        w1, wk1 = W(ns, t)
        if nt != t or ns == s or fb or any(w1[x][0] != R['w'][x][0] for x in range(n)):
            close(R); s, t = ns, nt; R = newrun(s, t); continue
        x1 = X(ns); (v0, k0, I0) = R['x']; (v1, k1, I1) = x1
        H0 = {(v, s[v]) for v in range(n) if g.owner[v] == 0} | I0
        Z1 = {v for v in range(n) if k1[v] != wk1[v]}
        for v in Z1 - R['Z']:
            if wk1[v] == R['wk'][v]: c['ZIN_V'] += 1                 # REOPEN-W: entry into Z needs a W-change of v
        R['wchv'] += sum(1 for v in range(n) if wk1[v] != R['wk'][v])
        if wk1 == R['wk']:                                          # W-flat transition
            if not Z1 <= R['Z']: c['ZSHR_V'] += 1                     # Z shrinks at a flat transition
            R['zfl'] += Z1 == R['Z']
            R['fl'] += 1; R['fli'] += 1; c['FLI'] = max(c['FLI'], R['fli'])
            lamfix = all(v0[x][0] == v1[x][0] for x in range(n)); R['lct'] += not lamfix
            for v in range(n):
                if g.owner[v] != 0 or ns[v] == s[v]: continue
                c['SW'] += 1; d, e = s[v], ns[v]
                if k0[v] == R['wk'][v]: c['NOTZ_V'] += 1
                if not k1[v] > k0[v]: c['NOCL_V'] += 1
                if wk1[v] != R['wk'][v]: c['WCH_V'] += 1
                c['GXC'] += lamfix
                if R['Hprev'] is not None:
                    if (v, e) in R['Hprev']: c['OLDIN'] += 1
                    else: c['NEW'] += 1
                c['IDXDN'] += e < d
                R['flv'][v] = R['flv'].get(v, 0) + 1; c['FLV'] = max(c['FLV'], R['flv'][v])
                if R['flv'][v] > len(g.succ[v]) - 1: c['FLVD_V'] += 1
        else:
            R['fli'] = 0; R['flv'] = {}
        R['Hprev'] = H0; R['w'], R['wk'], R['x'], R['Z'] = w1, wk1, x1, Z1; s = ns
    close(R); return c
if __name__ == '__main__':
    args = sys.argv[1:]; g = load(args[0]); c = run(g, readstart(args[1]) if len(args) > 1 else None)
    print(f"FLAT {os.path.basename(args[0])} n {g.n} " + " ".join(f"{k} {v}" for k, v in c.items()))
