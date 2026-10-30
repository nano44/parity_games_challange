#!/usr/bin/env python3
"""L-SI box 50 (docs/si/N5-ADD-box50.md): the WINDOW DAG of a W-run, for an additive count of REPEAT late adoptions.
Same W-runs, BLOCKED, late adoptions, FIRST / REPEAT, t* and windows as repchain.py (box 48): a REPEAT rho of (y, z) at transition u
(previous late adoption of (y, z) at u1, y's last leave of z at k) is CHAINED if W(z) changes at some transition of [k + 1, u - 1]; t*(rho)
is the last one; P(rho) := the window of t* (the last late transition <= t*, or INIT). The DAG has one node per window (INIT and one per
late transition) and an arc P(rho) -> u for every chained REPEAT rho at u. Per W-run (maxima over W-runs, except sums marked S):
 RT = late transitions; REP = REPEATs (chained + exceptional); NWIN = windows; BETA = most distinct children of one window;
 INDEG = most distinct parents of one window; NPATH = most root-to-window paths of one window (roots: windows with no parent);
 LONG = longest DAG path (arcs); TOK = distinct (z, t*) pairs over chained REPEATs, TOKSH = most chained REPEATs sharing one (z, t*);
 ETOK = distinct (y, z, t*) triples (must equal the chained REPEATs: the box 42 injectivity);
 SELFL (S) = chained REPEATs rho of e whose P(rho) is the window opened by e's own previous late adoption (u1);
 CHREP (S) = chained REPEATs rho of e whose P(rho) is reachable by >= 1 arc from the window of some earlier late adoption of e;
 EPATH = most REPEATs of one edge on one root-to-window path (DP over the DAG; 1 = no edge twice on a chain).
Usage: windag.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
args = sys.argv[1:]; g = load(args[0]); n = g.n
E, Ed = Engine(g), Engine(dual(g))
s, t = start_pair(g, E, Ed, readstart(args[1]) if len(args) > 1 else None); s, t = tuple(s), tuple(t)
WE = {}
def W(s, t):
    if t not in WE: WE[t] = Engine(pg.Game(list(g.prio), list(g.owner), [[t[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(n)]))
    e = WE[t]; w = e.evaluate(s)[0]; return w, [e.key(x) for x in w]
ev = [v for v in range(n) if g.owner[v] == 0]
def blocked(s, wk):
    vx, _ = E.evaluate(s); Is = set(E.improving(s, vx))
    return {(v, x) for v in ev for x in g.succ[v] if x != s[v] and wk[x] > wk[s[v]] and (v, x) not in Is}
c = dict(runs=0, RT=0, REP=0, X=0, NWIN=0, BETA=0, INDEG=0, NPATH=0, LONG=0, TOK=0, TOKSH=0, ETOK_V=0, SELFL=0, CHREP=0, EPATH=0)
def reset(s, t):
    w, wk = W(s, t); return dict(WV=w, WK=[wk], bl=set(blocked(s, wk)), adopt={}, leave={}, lastlate=None, win=[], late=[], arcs=[], reps=[])
def close(R):
    c['runs'] += 1
    nodes = [None] + R['late']; kids = {x: set() for x in nodes}; par = {x: set() for x in nodes}
    for p, ch in R['arcs']: kids[p].add(ch); par[ch].add(p)
    c['RT'] = max(c['RT'], len(R['late'])); c['NWIN'] = max(c['NWIN'], len(nodes))
    c['REP'] = max(c['REP'], len(R['reps']) + R.get('x', 0))
    if nodes: c['BETA'] = max(c['BETA'], max(len(kids[x]) for x in nodes)); c['INDEG'] = max(c['INDEG'], max(len(par[x]) for x in nodes))
    order = sorted(nodes, key=lambda x: -1 if x is None else x)    # arcs go forward in time
    npath, lon = {}, {}
    for x in order:
        npath[x] = sum(npath[p] for p in par[x]) if par[x] else 1; lon[x] = max([lon[p] + 1 for p in par[x]] + [0])
    c['NPATH'] = max(c['NPATH'], max(npath.values())); c['LONG'] = max(c['LONG'], max(lon.values()))
    tok = {}
    for (y, z, ts, u, p, u1) in R['reps']: tok[(z, ts)] = tok.get((z, ts), 0) + 1
    if R['reps']:
        c['TOK'] = max(c['TOK'], len(tok)); c['TOKSH'] = max(c['TOKSH'], max(tok.values()))
        if len({(y, z, ts) for (y, z, ts, u, p, u1) in R['reps']}) != len(R['reps']): c['ETOK_V'] += 1
    reach = {}
    def rch(a):                                                    # windows reachable from a by >= 1 arc
        if a not in reach:
            out, st = set(), list(kids[a])
            while st:
                b = st.pop()
                if b not in out: out.add(b); st.extend(kids[b])
            reach[a] = out
        return reach[a]
    ep = {}                                                        # EPATH: per window, the most repeats of each edge on a path into it
    arcs_by_child = {}
    for (y, z, ts, u, p, u1) in R['reps']: arcs_by_child.setdefault(u, []).append((p, (y, z)))
    for x in order:
        best = {}
        for p, e in arcs_by_child.get(x, []):
            d = dict(ep.get(p, {})); d[e] = d.get(e, 0) + 1
            for k, v in d.items(): best[k] = max(best.get(k, 0), v)
        ep[x] = best
        if best: c['EPATH'] = max(c['EPATH'], max(best.values()))
    for (y, z, ts, u, p, u1s) in R['reps']:
        if p == u1s[-1]: c['SELFL'] += 1
        if any(p in rch(a) for a in u1s): c['CHREP'] += 1
R = reset(s, t)
while True:
    r = step(g, E, Ed, list(s), list(t))
    if r is None: break
    ns, nt, _, _, fb, _, _ = r; ns, nt = tuple(ns), tuple(nt)
    w2, wk2 = W(ns, t)
    if nt != t or ns == s or fb or any(w2[x][0] != R['WV'][x][0] for x in range(n)):
        close(R); s, t = ns, nt; R = reset(s, t); continue
    u = len(R['WK']) - 1
    anylate = False
    WK = R['WK'] + [wk2]
    for y in ev:
        if ns[y] == s[y]: continue
        R['leave'][(y, s[y])] = u
        z = ns[y]
        if (y, z) in R['bl']:
            anylate = True; prev = R['adopt'].get((y, z), [])
            if prev:
                kl = R['leave'][(y, z)]
                ts = [x for x in range(kl + 1, u) if WK[x + 1][z] != WK[x][z]]
                if not ts: R['x'] = R.get('x', 0) + 1; c['X'] += 1
                else:
                    tt = ts[-1]; p = R['win'][tt]
                    R['reps'].append((y, z, tt, u, p, list(prev))); R['arcs'].append((p, u))
            R['adopt'][(y, z)] = prev + [u]
    if anylate: R['lastlate'] = u; R['late'].append(u)
    R['win'].append(R['lastlate'])
    R['bl'] |= blocked(ns, wk2); R['WK'].append(wk2); R['WV'] = w2; s = ns
close(R)
print(f"WINDAG {os.path.basename(args[0])} n {n} " + " ".join(f"{k} {v}" for k, v in c.items()))
