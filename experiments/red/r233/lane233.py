#!/usr/bin/env python3
"""L-RED 65 R233 (vs box 207 (Q2), R-INT): two hand-built growths of CFI3_n48's clock lane (box 207 §4.1: movers 9 -> 10 -> ... -> 16 -> 17
-> 33, options [Xi next, X], hooked onto mover 33 whose gate lies on R's play).
Design 1 LONG(L): L new level-0 lane movers inserted between 16 and 17 (each: options [Xi next, X], start X).
Design 2 NEST(L): a second lane B of L movers (options [Xi next, X], start X) whose last mover's Xi-target is lane A's mover 12 (the middle),
and lane A's mover 9 gets one more option with Xi-target B's first mover (so B's progress feeds A's tail and A's head observes B).
Usage: lane233.py IN.json OUT.json DESIGN L"""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r230"))
import mut230
G = json.load(open(sys.argv[1])); design, L = sys.argv[3], int(sys.argv[4])
def add(xt):
    x = G["N"]; G["N"] += 1; G["lev"].append(0); G["opts"].append([[-1, xt, 0], [-1, -1, 0]]); G["gate"].append([10 ** 6 + 2 * x, 10 ** 6 + 2 * x + 1])
    G["start"].append(1); G["br"] += [len(G["br"]) + 10 ** 5, len(G["br"]) + 10 ** 5 + 1]; G["bp"] += [0, 0]; return x
if design == "long":
    nxt = 17
    for _ in range(L): nxt = add(nxt)
    G["opts"][16][0][1] = nxt
elif design == "nest":
    nxt = 12
    for _ in range(L): nxt = add(nxt)
    G["opts"][9].append([-1, nxt, 0]); G["gate"][9].append(10 ** 7)
    G["br"].append(len(G["br"]) + 10 ** 6); G["bp"].append(0)
json.dump(mut230.renum(G), open(sys.argv[2], "w"))
