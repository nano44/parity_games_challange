#!/usr/bin/env python3
"""Turn a 'witness T .. xt .. rank .. par .. gate .. start s' line of bf2 / bfk into a genome JSON (R197 wiring).
Usage: wit2json.py d 'witness line' out.json   (d levels, two movers per level, option o = 2x+k, beta id = o)."""
import sys, json
d = int(sys.argv[1]); w = sys.argv[2].split(); out = sys.argv[3]
def grab(tag, n): i = w.index(tag); return [int(v) for v in w[i + 1:i + 1 + n]]
N = 2 * d; M = 2 * N
xt, rk, par, gate = grab("xt", M), grab("rank", M), grab("par", M), grab("gate", M); st = grab("start", 1)[0]
lev = [x // 2 for x in range(N)]
opts = [[[-1 if lev[x] == 0 else 2 * (lev[x] - 1) + k, xt[2 * x + k], 2 * x + k] for k in range(2)] for x in range(N)]
G = {"N": N, "lev": lev, "deg": 2, "opts": opts, "gate": [[gate[2 * x], gate[2 * x + 1]] for x in range(N)], "br": rk, "bp": par,
     "start": [(st >> x) & 1 for x in range(N)], "T": int(w[w.index("T") + 1])}
json.dump(G, open(out, "w")); print(out)
