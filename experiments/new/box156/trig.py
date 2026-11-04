#!/usr/bin/env python3
"""box 156: Lemma TRIGGER check (deg <= 2). For z in Mv_t, t >= 2, o = s_(t-1)(z), o' the other option:
 XiT(z,t): sign of face(o') - face(o) differs between s_(t-2) and s_(t-1);  WT(z,t): order of key(o'), key(o) differs between the
 keys of s_(t-1) and of s_t (keys of options read from the lower-level movers' states). Claim: every z in Mv_t (t >= 2) has XiT or WT.
Also: every WT(z,t) has a lower-level mover in Mv_t; every XiT(z,t) has a Xi-descendant (on z's chains under s_(t-2)) in Mv_(t-1).
Counts multi-steps by type: a step t >= 2 with >= 2 movers of which >= 1 is W-triggered only (WREL), or all Xi-triggered (XIBR).
ALL=1: all starts. Usage: trig.py genome.json ..."""
import sys, os, json, itertools
from val import ns
Gen = ns["Gen"]; tot = dict(runs=0, moves=0, NEITHER=0, WNOLOW=0, XNODESC=0, XiT=0, WT=0, BOTH=0, multi=0, WREL=0, XIBR=0)
def keysof(g, st): return g.keys(st)
for f in sys.argv[1:]:
    G = json.load(open(f)); g = Gen(G); N = g.N
    if max(len(o) for o in G["opts"]) > 2: continue
    starts = [G["start"]]
    if os.environ.get("ALL") and N <= 12: starts = [list(s) for s in itertools.product(*[range(len(o)) for o in G["opts"]])]
    for st0 in starts:
        S, _ = g.run(st0); T = len(S) - 1; tot["runs"] += 1
        K = [keysof(g, s) for s in S]
        for t in range(2, T + 1):
            mv = [v for v in range(N) if S[t][v] != S[t - 1][v]]; typ = []
            for z in mv:
                o = S[t - 1][z]; p = 1 - o; tot["moves"] += 1
                d2 = g.face(S[t - 2], z, p) - g.face(S[t - 2], z, o); d1 = g.face(S[t - 1], z, p) - g.face(S[t - 1], z, o)
                xi = (d2 > 0) != (d1 > 0)
                k1 = g.optkey(K[t - 1], z, p) < g.optkey(K[t - 1], z, o); k0 = g.optkey(K[t], z, p) < g.optkey(K[t], z, o)
                w = k1 != k0
                tot["XiT"] += xi; tot["WT"] += w; tot["BOTH"] += xi and w; tot["NEITHER"] += not xi and not w
                if w and not any(g.lev[y] < g.lev[z] for y in mv): tot["WNOLOW"] += 1
                if xi:
                    desc = set(g.play(S[t - 2], z, o)) | set(g.play(S[t - 2], z, p))
                    if not any(S[t - 1][y] != S[t - 2][y] for y in desc): tot["XNODESC"] += 1
                typ.append("W" if w and not xi else "X")
            if len(mv) >= 2:
                tot["multi"] += 1
                if "W" in typ: tot["WREL"] += 1
                else: tot["XIBR"] += 1
print("TRIG", " ".join(f"{k} {v}" for k, v in tot.items()))
