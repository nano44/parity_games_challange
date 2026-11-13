#!/usr/bin/env python3
"""L-RED 70 R244: text dump of a genome for the C tools: N; per mover: lev start, then per option: wt xt e gate (e = 2 br + bp).
Usage: dump244.py G.json OUT.txt"""
import sys, sim244
G = sim244.load(sys.argv[1])
with open(sys.argv[2], "w") as f:
    f.write(f"{G['N']}\n")
    for x in range(G["N"]):
        f.write(f"{G['lev'][x]} {G['start'][x]}\n")
        for k, o in enumerate(G["opts"][x]): f.write(f"{o[0]} {o[1]} {2 * G['br'][o[2]] + G['bp'][o[2]]} {G['gate'][x][k]}\n")
