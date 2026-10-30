#!/usr/bin/env python3
"""L-SI box 51: LATE' (forget a block at each adoption). An adoption of (y, z) at transition u of a W-run F is LATE' if (y, z) was BLOCKED
(R88 §3) at some state t of F with t >= p + 1, p the previous adoption transition of (y, z) in F (t >= a if none), and t < u.
Per W-run: WCH (W-changing transitions), RT (R88 late transitions), RTP (transitions with a LATE' adoption), REPP (LATE' adoptions of an
edge adopted before in F), XP (REPP with no W(z)-change on [k + 1, u - 1], k = y's last leave of z), FWV (W-runs with
WCH > (n - 1)(RTP + 1): FW-R* for LATE', must be 0), RSUB_V (LATE' adoptions that are not R88-late: must be 0).
Box 51 GAP-CLIMB: LP = LATE' adoptions (sum); GAPV = LATE' adoptions whose first Xi(z)-change after the last blocked state t_b is not a
strict rise at a state with z in Z (Xi(z) != W(z)) (must be 0); GTOKV = repeated (edge, climb) tokens (must be 0); TIEDG = those climbs
with W(z) unchanged.
Output: maxima over W-runs of WCH, RT, RTP, REPP; sums of XP, FWV, RSUB_V. Usage: latep.py GAME.pg [START]"""
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
    ev = [v for v in range(n) if g.owner[v] == 0]
    def blocked(s, wk):
        vx, _ = E.evaluate(s); Is = set(E.improving(s, vx))
        return {(v, x) for v in ev for x in g.succ[v] if x != s[v] and wk[x] > wk[s[v]] and (v, x) not in Is}, [E.key(x) for x in vx]
    c = dict(WCH=0, RT=0, RTP=0, REPP=0, XP=0, FWV=0, RSUB_V=0, LP=0, GAPV=0, GTOKV=0, TIEDG=0)
    def reset(s, t):
        w, wk = W(s, t); b, xk = blocked(s, wk)
        return dict(WV=w, WK=[wk], XK=[xk], tok=set(), ever=set(b), lastbl={e: 0 for e in b}, adopt={}, leave={}, wch=0, rt=0, rtp=0, repp=0)
    def close(R):
        for k in ('WCH', 'RT', 'RTP', 'REPP'): c[k] = max(c[k], R[k.lower()])
        if R['wch'] > (n - 1) * (R['rtp'] + 1): c['FWV'] += 1
    R = reset(s, t)
    while True:
        r = step(g, E, Ed, list(s), list(t))
        if r is None: break
        ns, nt, _, _, fb, _, _ = r; ns, nt = tuple(ns), tuple(nt)
        w2, wk2 = W(ns, t)
        if nt != t or ns == s or fb or any(w2[x][0] != R['WV'][x][0] for x in range(n)):
            close(R); s, t = ns, nt; R = reset(s, t); continue
        u = len(R['WK']) - 1; b2, xk2 = blocked(ns, wk2); WK = R['WK'] + [wk2]; XK = R['XK'] + [xk2]; late = latep = False
        for y in ev:
            if ns[y] == s[y]: continue
            R['leave'][(y, s[y])] = u; z = ns[y]; e = (y, z); p = R['adopt'].get(e)
            if e in R['ever']: late = True
            if e in R['lastbl'] and R['lastbl'][e] >= (p + 1 if p is not None else 0):
                latep = True; c['LP'] += 1
                if e not in R['ever']: c['RSUB_V'] += 1
                tb = R['lastbl'][e]                                  # GAP-CLIMB: first Xi(z)-change on [tb, u - 1], z in Z there
                sc = [x for x in range(tb, u) if XK[x + 1][z] != XK[x][z]]
                if not sc or not (XK[sc[0] + 1][z] > XK[sc[0]][z] and XK[sc[0]][z] != WK[sc[0]][z]): c['GAPV'] += 1
                else:
                    if (e, sc[0]) in R['tok']: c['GTOKV'] += 1
                    R['tok'].add((e, sc[0])); c['TIEDG'] += WK[sc[0] + 1][z] == WK[sc[0]][z]
                if p is not None:
                    R['repp'] += 1; k = R['leave'][e]
                    if not any(WK[x + 1][z] != WK[x][z] for x in range(k + 1, u)): c['XP'] += 1
            R['adopt'][e] = u
        R['rt'] += late; R['rtp'] += latep; R['wch'] += wk2 != R['WK'][-1]
        for e in b2: R['lastbl'][e] = u + 1; R['ever'].add(e)
        R['WK'].append(wk2); R['XK'].append(xk2); R['WV'] = w2; s = ns
    close(R); return c
if __name__ == '__main__':
    args = sys.argv[1:]; g = load(args[0]); c = run(g, readstart(args[1]) if len(args) > 1 else None)
    print(f"LATEP {os.path.basename(args[0])} n {g.n} " + " ".join(f"{k} {v}" for k, v in c.items()))
