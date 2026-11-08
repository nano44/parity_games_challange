#!/usr/bin/env python3
"""L-RED 59 R225: L-LOWER / L-COMP 2-wide degree-2 ladder text (d / xt / br / bp / gate / start; sim6.py format) -> own.py JSON.
Convention (as sim6.okeys reads it): mover x has level x // 2; option k of a mover at level l >= 1 has W-target mover 2(l-1) + k;
level-0 options have W-target c_W (-1). Xi-target xt[2x + k] (-1 = X). Gate index = gate[2x + k], beta rank br, parity bp.
Usage: lad2json.py in.txt out.json"""
import sys, json
D = {}
for ln in open(sys.argv[1]):
    w = ln.split()
    if w and w[0] in ('d', 'xt', 'br', 'bp', 'gate', 'start'): D[w[0]] = list(map(int, w[1:]))
d = D['d'][0]; N = 2 * d
lev = [x // 2 for x in range(N)]
opts = [[[(2 * (lev[x] - 1) + k) if lev[x] else -1, D['xt'][2 * x + k], 2 * x + k] for k in (0, 1)] for x in range(N)]
gate = [[D['gate'][2 * x + k] for k in (0, 1)] for x in range(N)]
G = {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": D['br'], "bp": D['bp'], "start": D['start'], "deg": 2}
json.dump(G, open(sys.argv[2], "w"))
U = sum(1 for x in range(N) for o in opts[x] if o[1] >= 0 and lev[o[1]] > lev[x])
print(sys.argv[1].split('/')[-1], "N", N, "M", 2 * N, "U(G)", U, "X-exits", sum(1 for x in D['xt'] if x < 0))
