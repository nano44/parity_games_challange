#!/usr/bin/env python3
"""Lift a renumbering from instance N to N+1 of a labelled family: vertices whose label exists in both keep the RELATIVE order
of their new indices; new vertices are appended (renum --init fills gaps). Usage: lift.py small.pg small.perm big.pg > big.perm"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
import pg
gs, gb = pg.read(sys.argv[1]), pg.read(sys.argv[3])
perm = dict(map(int, l.split()) for l in open(sys.argv[2]))
lb = {gb.labels[v]: v for v in range(gb.n)}
common = sorted((perm[v], lb[gs.labels[v]]) for v in range(gs.n) if gs.labels[v] in lb)
for new, (_, vb) in enumerate(common):
    print(vb, new)
