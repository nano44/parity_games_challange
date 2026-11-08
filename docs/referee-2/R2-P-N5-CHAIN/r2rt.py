#!/usr/bin/env python3
"""REFEREE-2 successor 35: RT_n1's state-0 option values on Γ3 (own engine r2end.py). Usage: r2rt.py RT_n1.json"""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2-P-N5-END"))
import r2end as R
G = json.load(open(sys.argv[1])); g = R.build(G, "lev"); n, pr, ow, E, V = g["n"], g["pr"], g["ow"], g["E"], g["V"]
od = R.Order(pr); st = R.s3(g); sig = [st[v] if ow[v] == 0 else None for v in range(n)]
val, sbar = R.s1(pr, ow, E, sig, od); inv = {i: k for k, i in V.items()}
for k in range(3):
    m = V[("m", (0, k))]; c, P, l = val[m]
    print(f"option {k}: m pad {m}, value (Λ {inv[c]}, Π {sorted(str(inv[u]) for u in P)}, k {l}); chosen at state 0: {sig[V[('x', 0)]] == m}")
print("options 1, 2 equal:", val[V[("m", (0, 1))]] == val[V[("m", (0, 2))]], "; both strictly above option 0:",
      od.cmp(val[V[("m", (0, 1))]], val[V[("m", (0, 0))]]) > 0)
