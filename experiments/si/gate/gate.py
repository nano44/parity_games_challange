#!/usr/bin/env python3
"""L-SI box 51b (docs/si/N5-GATE-box51b.md): gates of W-flat Xi-climbs in a W-run (W-runs and W-flat transitions as in
si/fl/flat.py, box 50b). State k: sigma_k, tau (fixed on F), sbar_k := Odd's optimal counterstrategy of Xi_k (si.Engine.evaluate),
D_k := {Odd o : sbar_k(o) != tau(o)}. Gate g_k(u) := the first vertex of D_k on the (sigma_k, tau)-play from u (u itself if u in D_k;
None if the play avoids D_k); pre_k(u) := the play's vertices before g. DEC_k(u): W_k(u) = pre_k(u) (+) W_k(g) and Xi_k(u) =
pre_k(u) (+) Xi_k(g) (prefix operation si.Engine.extend). SP_k(g): Xi_k(g) and W_k(g) have the same cycle node.
At every W-flat transition t -> t+1 of F, every u with Xi_{t+1}(u) |> Xi_t(u) (a CLIMB) is put in one class:
 GSELF: u in D_t and in D_{t+1} (u is its own gate);  NOG: no gate at t or t+1;  GCH: g_t(u) != g_{t+1}(u);
 NSP: same gate, not SP at t or t+1;  NDEC: same gate, SP at both, DEC fails at t or t+1;
 SPD: same gate, DEC, SP at both states. Lemma GATE (box 51b §2) says then Xi(g) strictly climbs: TRV_V counts failures.
 Climbs are also split EV (Even, switched) / ALL. ZZ_V: a climb at u not in Z_t (must be 0 by XW at a flat transition).
Potential (box 51b §3): LEV_k(u) := index of the first coordinate where Xi_k(u), W_k(u) differ in the coordinate sequence
(reward(cycle node), bit of rank n-1, ..., bit of rank 0 (signed), length (signed)); PHI_k(u) := (LEV, Xi's coordinate at LEV).
MONO_V: PHI falls at a flat transition for some u in Z (must be 0, Lemma LEV-FLAT). Per flat transition with Z fixed: PR if some u's
PHI rises, else SUB (all PHI fixed). Output maxima per W-run: ZFL, SUB, PR, WCI (W-constant intervals), FLAT; sums of classes.
Box 51b §1 (INTERVAL-SI): on a W-constant interval I (W fixed), OPT(v) := {e : v (+) W(e) = W(v)} (v not its own W-cycle node) or
{e : W(e) has cycle node v and empty path set} (v its own W-cycle node). TIGHT_V: some state of a W-run has sigma(v) not in OPT(v) for its
W (must be 0); IMP_V: a switch at a W-flat transition to an edge not in Isigma_t (must be 0). FLI: most W-flat transitions in one I.
XGRD / XNGRD: switches at W-flat transitions whose new edge is / is not Xi_t-best among the TIGHT arena edges of v (OPT(v) for W_t,
intersected with {sigma_t(v)} u Isigma_t(v)); LAZY: Even v not switched at a W-flat transition although some tight arena edge is
Xi_t-improving. DMAX: largest |D_k|. NSPW: flat NSP climbs at which u's W-cycle node lies on pre_t(u) or pre_{t+1}(u) (W ignores the gate). Over ALL transitions of a W-run (flat or not): TXC events (u, t) (Xi(u) strictly climbs, W(u) fixed; RESULTS R92):
TXC (max per W-run), TXV (max per W-run of one vertex's TXC events), XCV (max per W-run of one vertex's Xi-changes), TXC_<class> sums
with the gate classes above (state pair t, t+1). Usage: gate.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
def run(g, start=None):
    n = g.n; E, Ed = Engine(g), Engine(dual(g)); own = g.owner
    s, t = start_pair(g, E, Ed, start); s, t = tuple(s), tuple(t)
    WE = {}
    def W(s, t):
        if t not in WE: WE[t] = Engine(pg.Game(list(g.prio), list(g.owner), [[t[v]] if own[v] == 1 else list(g.succ[v]) for v in range(n)]))
        e = WE[t]; w = e.evaluate(s)[0]; return w, [e.key(x) for x in w]
    def coords(val):
        c, m, ln = val; out = [E.rew[c]]
        for r in range(n - 1, -1, -1):
            out.append(0 if not (m >> r) & 1 else (1 if E.rankpar[r] == 0 else -1))
        out.append(ln if E.par[c] == 1 else -ln); return out
    def phi(xv, wv):
        a, b = coords(xv), coords(wv)
        for i in range(len(a)):
            if a[i] != b[i]: return (i, a[i])
        return None
    def state(s, t):
        w, wk = W(s, t); xv, sb = E.evaluate(s); xk = [E.key(x) for x in xv]
        D = {o for o in range(n) if own[o] == 1 and sb[o] != t[o]}
        return dict(s=s, w=w, wk=wk, xv=xv, xk=xk, D=D, Z={v for v in range(n) if xk[v] != wk[v]})
    def gate(S, t, u):
        pre, x, seen = [], u, set()
        while x not in S['D']:
            if x in seen: return None, pre
            seen.add(x); pre.append(x); x = S['s'][x] if own[x] == 0 else t[x]
        return x, pre
    def dec(S, g0, pre):
        a, b = S['w'][g0], S['xv'][g0]
        for y in reversed(pre): a, b = E.extend(y, a), E.extend(y, b)
        return a == S['w'][pre[0]] and b == S['xv'][pre[0]] if pre else True
    cls = ['GSELF', 'NOG', 'GCH', 'NDEC', 'NSP', 'SPD']
    c = {k: 0 for k in ['ZFL', 'SUB', 'PR', 'WCI', 'FLAT', 'TRV_V', 'ZZ_V', 'MONO_V', 'XFL', 'TIGHT_V', 'IMP_V', 'FLI', 'DMAX', 'TXC', 'TXV', 'XCV', 'NSPW', 'XGRD', 'XNGRD', 'LAZY'] + ['TXC_' + k for k in cls] + ['EV_' + k for k in cls] + ['ALL_' + k for k in cls]}
    mx = ['ZFL', 'SUB', 'PR', 'WCI', 'FLAT', 'XFL', 'FLI', 'TXC', 'TXV', 'XCV']
    def newrun(S): return dict(ZFL=0, SUB=0, PR=0, WCI=1, FLAT=0, XFL=0, FLI=0, fli=0, TXC=0, TXV=0, XCV=0, tv={}, xv={})
    def classify(S, S1, u, chk=False):
        if u in S['D'] and u in S1['D']: return 'GSELF'
        g0, p0 = gate(S, t, u); g1, p1 = gate(S1, t, u)
        if g0 is None or g1 is None: return 'NOG'
        if g0 != g1: return 'GCH'
        if S['xv'][g0][0] != S['w'][g0][0] or S1['xv'][g0][0] != S1['w'][g0][0]:
            if chk and (S['w'][u][0] in p0 or S1['w'][u][0] in p1): c['NSPW'] += 1
            return 'NSP'
        if not (dec(S, g0, p0) and dec(S1, g1, p1)): return 'NDEC'
        if chk and not S1['xk'][g0] > S['xk'][g0]: c['TRV_V'] += 1
        return 'SPD'
    def txc(R, S, S1):
        for u in range(n):
            if S1['xk'][u] != S['xk'][u]:
                R['xv'][u] = R['xv'].get(u, 0) + 1; R['XCV'] = max(R['XCV'], R['xv'][u])
                if S1['xk'][u] > S['xk'][u] and S1['wk'][u] == S['wk'][u]:
                    R['TXC'] += 1; R['tv'][u] = R['tv'].get(u, 0) + 1; R['TXV'] = max(R['TXV'], R['tv'][u]); c['TXC_' + classify(S, S1, u)] += 1
    def tight(S):
        w = S['w']; bad = 0
        for v in range(n):
            if own[v] != 0: continue
            e = S['s'][v]
            if w[v][0] == v: bad += not (w[e][0] == v and w[e][1] == 0)
            else: bad += E.extend(v, w[e]) != w[v]
        return bad
    def close(R):
        for k in mx: c[k] = max(c[k], R[k])
    S = state(s, t); R = newrun(S)
    while True:
        c['TIGHT_V'] += tight(S); c['DMAX'] = max(c['DMAX'], len(S['D']))
        r = step(g, E, Ed, list(S['s']), list(t))
        if r is None: break
        ns, nt, Is, _, fb, _, _ = r; ns, nt = tuple(ns), tuple(nt); Is = set(Is)
        if nt != t or ns == S['s'] or fb:
            close(R); t = nt; S = state(ns, t); R = newrun(S); continue
        S1 = state(ns, t)
        if any(S1['w'][x][0] != S['w'][x][0] for x in range(n)):
            close(R); S = S1; R = newrun(S); continue
        txc(R, S, S1)
        if S1['wk'] != S['wk']:
            R['WCI'] += 1; R['fli'] = 0; S = S1; continue
        R['FLAT'] += 1; R['fli'] += 1; R['FLI'] = max(R['FLI'], R['fli'])
        c['IMP_V'] += sum(1 for v in range(n) if own[v] == 0 and ns[v] != S['s'][v] and (v, ns[v]) not in Is)
        for v in range(n):
            if own[v] != 0: continue
            w = S['w']; tg = [e for e in [S['s'][v]] + [e for (x, e) in Is if x == v]
                              if (E.extend(v, w[e]) == w[v] if w[v][0] != v else (w[e][0] == v and w[e][1] == 0))]
            best = max(S['xk'][e] for e in tg)
            if ns[v] != S['s'][v]: c['XGRD' if S['xk'][ns[v]] == best else 'XNGRD'] += 1
            elif best > S['xk'][S['s'][v]]: c['LAZY'] += 1
        climbs = [u for u in range(n) if S1['xk'][u] > S['xk'][u]]
        if not climbs: R['XFL'] += 1
        for u in climbs:
            if u not in S['Z']: c['ZZ_V'] += 1
            k = classify(S, S1, u, True); c['ALL_' + k] += 1
            if own[u] == 0 and ns[u] != S['s'][u]: c['EV_' + k] += 1
        if S1['Z'] == S['Z']:
            R['ZFL'] += 1; rise = False
            for u in S['Z']:
                p0, p1 = phi(S['xv'][u], S['w'][u]), phi(S1['xv'][u], S1['w'][u])
                if p1 < p0: c['MONO_V'] += 1
                if p1 > p0: rise = True
            R['PR' if rise else 'SUB'] += 1
        S = S1
    close(R); return c
if __name__ == '__main__':
    args = sys.argv[1:]; g = load(args[0]); c = run(g, readstart(args[1]) if len(args) > 1 else None)
    print(f"GATE {os.path.basename(args[0])} n {g.n} " + " ".join(f"{k} {v}" for k, v in c.items()))
