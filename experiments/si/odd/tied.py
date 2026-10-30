#!/usr/bin/env python3
"""L-SI box 50 §5 probe: is every REPEAT late adoption of (y, z) (windag.py / repchain.py definitions) paid by a TIED Xi-climb of z, i.e. a
transition s in [k, u - 1] of the W-run (k = y's last leave of z, u the REPEAT's transition) with Xi_{s+1}(z) > Xi_s(z) and W_{s+1}(z) =
W_s(z)? Counters: rep; tied (yes); untied; reblk = REPEATs with (y, z) blocked at some state of [k + 1, u]; untied_reblk; tsh = most
REPEATs paid by one (z, s) (taking the last tied s). Usage: tied.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
def run(g, start=None, bad=None):
    n = g.n; E, Ed = Engine(g), Engine(dual(g))
    s, t = start_pair(g, E, Ed, start); s, t = tuple(s), tuple(t)
    WE = {}
    def W(s, t):
        if t not in WE: WE[t] = Engine(pg.Game(list(g.prio), list(g.owner), [[t[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(n)]))
        e = WE[t]; w = e.evaluate(s)[0]; return w, [e.key(x) for x in w]
    ev = [v for v in range(n) if g.owner[v] == 0]
    def xi(s):
        vx, _ = E.evaluate(s); return vx, [E.key(x) for x in vx], set(E.improving(s, vx))
    def blocked(s, wk, Is):
        return {(v, x) for v in ev for x in g.succ[v] if x != s[v] and wk[x] > wk[s[v]] and (v, x) not in Is}
    c = dict(rep=0, tied=0, untied=0, reblk=0, untied_reblk=0, tsh=0)
    def reset(s, t):
        w, wk = W(s, t); vx, xk, Is = xi(s); b = blocked(s, wk, Is)
        return dict(WV=w, WK=[wk], XK=[xk], BL=[b], bl=set(b), adopt={}, leave={}, tok={})
    R = reset(s, t)
    while True:
        r = step(g, E, Ed, list(s), list(t))
        if r is None: break
        ns, nt, _, _, fb, _, _ = r; ns, nt = tuple(ns), tuple(nt)
        w2, wk2 = W(ns, t)
        if nt != t or ns == s or fb or any(w2[x][0] != R['WV'][x][0] for x in range(n)):
            s, t = ns, nt; R = reset(s, t); continue
        u = len(R['WK']) - 1
        vx2, xk2, Is2 = xi(ns); b2 = blocked(ns, wk2, Is2)
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
                    if ss:
                        c['tied'] += 1; key = (z, ss[-1]); R['tok'][key] = R['tok'].get(key, 0) + 1; c['tsh'] = max(c['tsh'], R['tok'][key])
                    else:
                        c['untied'] += 1; c['untied_reblk'] += rb
                        if rb and bad is not None: bad.append((y, z, k, u))
                R['adopt'][(y, z)] = 1
        R['bl'] |= b2; R['WK'].append(wk2); R['XK'].append(xk2); R['BL'].append(b2); R['WV'] = w2; s = ns
    return c
if __name__ == '__main__':
    args = sys.argv[1:]; g = load(args[0])
    c = run(g, readstart(args[1]) if len(args) > 1 else None)
    print(f"TIED {os.path.basename(args[0])} n {g.n} " + " ".join(f"{k} {v}" for k, v in c.items()))
