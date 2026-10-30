#!/usr/bin/env python3
"""L-RED successor 32 (R131): importable re-implementation of L-SI box 50 tied.py (l-si 4fb0bfba) counters, written from the box 50 §6
definitions, on L-NEW's n5x step (SPEC S1-S5). W-run = tau constant, sigma moves, no fallback, W cycle-node map constant. (v, x) BLOCKED at a
state: x W-better than sigma(v) and (v, x) not Xi-improving. LATE adoption: adoption of an edge blocked at an earlier state of the W-run.
REPEAT: a late adoption of an edge late-adopted before in the W-run. k = y's last leave of z; RE-BLOCKED: blocked at a state of [k+1, u];
TIED: some s in [k, u-1] with Xi_(s+1)(z) > Xi_s(z) and W_(s+1)(z) = W_s(z). stats() also returns the REPEAT list for tree analysis."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg

def stats(g, start=None, cap=5000):
    n = g.n; E, Ed = Engine(g), Engine(dual(g))
    s, t = start_pair(g, E, Ed, start); s, t = tuple(s), tuple(t)
    WE = {}
    def W(s, t):
        if t not in WE: WE[t] = Engine(pg.Game(list(g.prio), list(g.owner), [[t[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(n)]))
        e = WE[t]; w = e.evaluate(s)[0]; return w, [e.key(x) for x in w]
    ev = [v for v in range(n) if g.owner[v] == 0]
    def xi(s):
        vx, _ = E.evaluate(s); return [E.key(x) for x in vx], set(E.improving(s, vx))
    def blocked(s, wk, Is):
        return {(v, x) for v in ev for x in g.succ[v] if x != s[v] and wk[x] > wk[s[v]] and (v, x) not in Is}
    c = dict(it=0, runs=1, rep=0, tied=0, untied=0, reblk=0, untied_reblk=0)
    reps = []
    def reset(s, t):
        w, wk = W(s, t); xk, Is = xi(s); b = blocked(s, wk, Is)
        return dict(WV=w, WK=[wk], XK=[xk], BL=[b], bl=set(b), adopt={}, leave={}, t0=c['it'])
    R = reset(s, t)
    while c['it'] < cap:
        r = step(g, E, Ed, list(s), list(t))
        if r is None: break
        c['it'] += 1
        ns, nt, _, _, fb, _, _ = r; ns, nt = tuple(ns), tuple(nt)
        w2, wk2 = W(ns, t)
        if nt != t or ns == s or fb or any(w2[x][0] != R['WV'][x][0] for x in range(n)):
            s, t = ns, nt; R = reset(s, t); c['runs'] += 1; continue
        u = len(R['WK']) - 1
        xk2, Is2 = xi(ns); b2 = blocked(ns, wk2, Is2)
        WK = R['WK'] + [wk2]; XK = R['XK'] + [xk2]; BL = R['BL'] + [b2]
        for y in ev:
            if ns[y] == s[y]: continue
            R['leave'][(y, s[y])] = u; z = ns[y]
            if (y, z) in R['bl']:
                if R['adopt'].get((y, z)):
                    c['rep'] += 1; k = R['leave'][(y, z)]
                    ss = [x for x in range(k, u) if XK[x + 1][z] > XK[x][z] and WK[x + 1][z] == WK[x][z]]
                    rb = any((y, z) in BL[x] for x in range(k + 1, u + 1))
                    c['reblk'] += rb
                    if ss: c['tied'] += 1
                    else: c['untied'] += 1; c['untied_reblk'] += rb
                    reps.append(dict(y=y, z=z, u=R['t0'] + u, k=R['t0'] + k, reblk=rb, tied=bool(ss)))
                R['adopt'][(y, z)] = 1
        R['bl'] |= b2; R['WK'].append(wk2); R['XK'].append(xk2); R['BL'].append(b2); R['WV'] = w2; s = ns
    return c, reps

if __name__ == "__main__":
    g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 else None
    c, reps = stats(g, st, cap=10 ** 6)
    print(f"TIEDLIB {os.path.basename(sys.argv[1])} n {g.n} " + " ".join(f"{k} {v}" for k, v in c.items()))
