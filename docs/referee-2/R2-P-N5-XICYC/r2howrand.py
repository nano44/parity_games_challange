#!/usr/bin/env python3
"""REFEREE-2 succ. 30: r2howcyc.howard on random genomes WITH Ξ-cycles (my predecessor's R2-N5-REALIZE rand_genome, acyclic=False),
sums every check counter; ONEP=1 also asserts R = 0. Usage: r2howrand.py SEED COUNT NMAX DMAX"""
import sys, random, json
import r2howcyc as H
seed, cnt, Nmax, dmax = map(int, sys.argv[1:5]); rng = random.Random(seed)
S = dict(genomes=0, cyclic=0, steps=0, C=0, R=0, P=0, maxp_over_N=0.0, maxT=0, BRSEG_viol=0, CYC_viol=0, TCYC_viol=0)
for k in 'F1 F6 STRICT DOM LEVEL0 K2'.split(): S[k] = 0
for _ in range(cnt):
    G = H.R.rand_genome(rng, Nmax, dmax, acyclic=False); o = H.howard(G); S['genomes'] += 1
    S['cyclic'] += not H.R.acyclic(G)
    S['steps'] += o['T']; S['C'] += o['C']; S['R'] += o['R']; S['P'] += o['P']; S['maxT'] = max(S['maxT'], o['T'])
    S['maxp_over_N'] = max(S['maxp_over_N'], o['longest_p'] / o['N'])
    S['BRSEG_viol'] += not o['BRSEG_ok']; S['CYC_viol'] += not o['CYC_ok']; S['TCYC_viol'] += not o['TCYC_ok']
    for k in 'F1 F6 STRICT DOM LEVEL0 K2'.split(): S[k] += o[k]
print('seed', seed, 'count', cnt, 'Nmax', Nmax, 'dmax', dmax, 'ONEP', H.ONEP, json.dumps(S))
