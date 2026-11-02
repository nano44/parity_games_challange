#!/usr/bin/env python3
"""L-NEW box 147: per-step trace in pi order. Columns: step, option bits, unstable marks (W = unstable and key-preferred = Xi-better,
w = unstable but key prefers the current option, . = stable), movers (*), chained flag of the step. Usage: trace.py genome.json ..."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(HERE, "stat.py")
ns = {"__file__": P}; exec(open(P).read().split('\nif __name__')[0], ns); analyse = ns["analyse"]
for g in sys.argv[1:]:
    G = json.load(open(g)); R = analyse(G); pos = R['pos']; order = sorted(pos, key=pos.get)
    print(os.path.basename(g), 'pi order', order, 'lev', [G['lev'][x] for x in order])
    for t, s in enumerate(R['S']):
        F = R['FS'][t]
        st = ''.join(str(s[x]) for x in order)
        un = ''.join(('W' if F['KP'][x] == F['B'][x] else 'w') if F['UNST'][x] else '.' for x in order)
        mv = ''.join('*' if t > 0 and s[x] != R['S'][t - 1][x] else ' ' for x in order)
        lab = R['lab'].get(t); print(f"{t:3d} {st} {un} {mv} {'' if lab is None else ('ch' if lab else 'UNCH')}")
