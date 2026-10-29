#!/usr/bin/env python3
"""L-NEW box 60 probe: PV-PLAY. A flip of Odd u at transition j counts only if u lies on a (sigma^(j), sbar_j)- or (sigma^(j+1),
sbar_(j+1))-play from some Even vertex with >= 2 successors. Prints n, max play-flips(u), and raw max flips. Usage: pvplay.py GAME.pg"""
import sys, os, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import flips
g, E, seq, ev = flips.run(sys.argv[1])
EB = [v for v in range(g.n) if g.owner[v] == 0 and len(set(g.succ[v])) > 1]
def onplay(j):
    s, sb = seq[j]["s"], seq[j]["sb"]; seen = set()
    for v in EB:
        while v not in seen:
            seen.add(v); v = s[v] if g.owner[v] == 0 else sb[v]
    return seen
cache = {}
P = lambda j: cache.setdefault(j, onplay(j))
raw = collections.Counter(e["u"] for e in ev)
pl = collections.Counter(e["u"] for e in ev if e["u"] in P(e["j"]) or e["u"] in P(e["j"] + 1))
mp = max(pl.values(), default=0)
print(f"PVPLAY {os.path.basename(sys.argv[1])} n {g.n} rawmax {max(raw.values(), default=0)} playmax {mp} playSBC {len({e['j'] for e in ev if e['u'] in P(e['j']) or e['u'] in P(e['j']+1)})} {'OK' if mp <= g.n else 'VIOL'}", flush=True)
