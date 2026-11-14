#!/usr/bin/env python3
"""box150 JSON (R110 wiring, beta index of option (x,k) = 2x+k) -> text genome (d/xt/br/bp/gate/start). Usage: j2t.py in.json"""
import sys, json
G = json.load(open(sys.argv[1])); N = G["N"]
assert all(G["opts"][x][k][2] == 2 * x + k for x in range(N) for k in range(2))
print("d", N // 2)
print("xt", *[G["opts"][x][k][1] for x in range(N) for k in range(2)])
print("br", *G["br"]); print("bp", *G["bp"])
print("gate", *[G["gate"][x][k] for x in range(N) for k in range(2)])
print("start", *G["start"])
