#!/usr/bin/env python3
"""Probe: is there a weak (n,d)-separator with k states having an odd simple cycle whose maximum is <= pmax (odd)?
Usage: probe_oddcycles.py n d conv k pmax"""
import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from wsep.graphs import maximal_graphs
from wsep.encode import Encoder
from wsep.automata import check_separator
n, d, conv, k, pmax = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], int(sys.argv[4]), int(sys.argv[5])
evens = maximal_graphs(n, d, conv, 0, verify=False); odds = maximal_graphs(n, d, conv, 1, verify=False)
enc = Encoder(n, d, k, False); enc.require_odd_cycle_max_at_most(pmax)
ae, ao = set(), set(); rounds = 0
while True:
    rounds += 1
    aut = enc.solve()
    if aut is None:
        print(f"n={n} d={d} {conv} k={k} pmax={pmax}: UNSAT ({rounds} rounds)"); break
    bad = check_separator(aut, evens, odds, False)
    if not bad:
        print(f"n={n} d={d} {conv} k={k} pmax={pmax}: SAT {aut['delta']}"); break
    c = 0
    for kind, g in bad:
        if kind == 'W1' and evens.index(g) not in ae: enc.add_even(g); ae.add(evens.index(g)); c += 1
        if kind == 'W2' and odds.index(g) not in ao: enc.add_odd(g); ao.add(odds.index(g)); c += 1
        if c >= 3: break
