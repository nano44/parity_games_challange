#!/usr/bin/env python3
"""L-SI box 47 (docs/si/N5-READ-box47.md): reader chains of W-changes inside W-runs (plain N5, S3 start or START; W-run as in L-NEW's
box64/late.py: tau constant, no S4c fallback, lambda_W constant). For a W-change of c at transition t (W_{t+1}(c) != W_t(c)), its CAUSES are
the Even x on c's new or old (sigma, tau)-play that switch at t (Lemma READ-CHARGE: there is at least one; RC_V counts W-changes without
a cause, must be 0). For a cause x -> w (sigma_{t+1}(x) = w), its SOURCE is the last W-change of w at a transition t' < t of the same W-run
(none: the switch is a ROOT, driven by an arena entry or by the start state). DEPTH(c, t) := 1 + max over causes of DEPTH(source), roots
count 0. Counters: wchg (W-changes, vertex-transition pairs), roots, maxdepth (over the run), maxdepthW (max over W-runs of the max depth),
WRUN (W-runs), RC_V; FANOUT = the most W-changes having one source W-change (w, t') as a source; FANOUTW = the same over
the sources of one W-run summed per transition t' (the breadth one transition's W-changes feed). Usage: readch.py GAME.pg [START]"""
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
def play(s, t, z):
    seen, out, x = set(), [], z
    while x not in seen: seen.add(x); out.append(x); x = s[x] if g.owner[x] == 0 else t[x]
    return out
c = dict(wchg=0, roots=0, maxdepth=0, WRUN=1, RC_V=0, FANOUT=0, FANOUTW=0)
fan = {}; fant = {}
w0, wk = W(s, t); last = {}; dep = {}          # last[v] = (transition index, depth) of v's last W-change in the current W-run
u = 0
while True:
    r = step(g, E, Ed, list(s), list(t))
    if r is None: break
    ns, nt, _, _, fb, _, _ = r; ns, nt = tuple(ns), tuple(nt)
    w2, wk2 = W(ns, t)
    if nt != t or ns == s or fb or any(w2[x][0] != w0[x][0] for x in range(n)):
        s, t = ns, nt; w0, wk = W(s, t); last = {}; fan = {}; fant = {}; c["WRUN"] += 1; u += 1; continue
    sw = {x for x in range(n) if g.owner[x] == 0 and ns[x] != s[x]}
    new = {}
    for z in range(n):
        if wk2[z] == wk[z]: continue
        c["wchg"] += 1
        causes = [x for x in set(play(ns, t, z)) | set(play(s, t, z)) if x in sw]
        if not causes: c["RC_V"] += 1; continue
        d = 0
        for x in causes:
            src = last.get(ns[x])
            if src is None: c["roots"] += 1
            else:
                d = max(d, src[1]); key = (ns[x], src[0]); fan[key] = fan.get(key, 0) + 1; fant[src[0]] = fant.get(src[0], 0) + 1
                c['FANOUT'] = max(c['FANOUT'], fan[key]); c['FANOUTW'] = max(c['FANOUTW'], fant[src[0]])
        new[z] = (u, d + 1); c["maxdepth"] = max(c["maxdepth"], d + 1)
    last.update(new); s, w0, wk = ns, w2, wk2; u += 1
print(f"READCH {os.path.basename(args[0])} n {n} " + " ".join(f"{k} {v}" for k, v in c.items()))
