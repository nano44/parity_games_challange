#!/usr/bin/env python3
"""L-LOWER 14: write a genome's gsolve ranks/signs (the «_solved» form of L10 §3d) and print its score.
Core target read from the frozen core file (TARGET, e.g. ../l10/out/core8_HIT7.txt) instead of rebuilding it from HIT7.
Usage: rsolve.py GENOME TARGET OUT"""
import sys, os, hashlib
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(here, '..', 'l10'))
from build import *
from gsolve import gsolve
D = fixgates(rd(sys.argv[1]))
T = open(sys.argv[2]).read().split(); CT = [tuple(int(c) for c in T[2 + i]) for i in range(int(T[0]))]
S, E = fulltraj(D, CT); cons = constraints(E, S); v, br, bp = gsolve(cons, 4 * D['d'])
G = dict(E); G['start'] = D['start']; G['br'], G['bp'] = br, bp; wr(G, sys.argv[3])
print('score', v, 'constraints', len(cons), '->', sys.argv[3], hashlib.sha1(open(sys.argv[3], 'rb').read()).hexdigest())
