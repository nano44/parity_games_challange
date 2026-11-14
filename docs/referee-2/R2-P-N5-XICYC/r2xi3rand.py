#!/usr/bin/env python3
"""REFEREE-2 succ. 30: r2xi3.check on random Ξ-cyclic genomes (rand_genome acyclic=False). Usage: r2xi3rand.py SEED COUNT NMAX DMAX"""
import sys, random, json
import r2xi3 as X
seed, cnt, Nmax, dmax = map(int, sys.argv[1:5]); rng = random.Random(seed)
S = dict(mover_transitions=0, nonstd=0, nonhoward=0, badstop=0, nofb=0, genomes=0, cyclic=0, transitions=0, howard3_equal=0, standard=0, no_fb_before=0, fb_at=0, xi_T3=0, gamma_eq_gamma3=0)
for _ in range(cnt):
    G = X.R.rand_genome(rng, Nmax, dmax, acyclic=False); o = X.check(G); S['genomes'] += 1; S['cyclic'] += not X.R.acyclic(G)
    S['transitions'] += o['T_howard3']; S['howard3_equal'] += o['movers_equal_howard3']; S['standard'] += o['standard_0_T33']
    S['no_fb_before'] += o['no_fb_before_T33']; S['fb_at'] += o['fb_at_T33plus1']; S['xi_T3'] += o['xi_eq_T33_plus3']
    S['gamma_eq_gamma3'] += o['gamma_equals_gamma3']
    d = o['direct']; S['mover_transitions'] += d['mover_transitions']; S['nonstd'] += d['nonstd']; S['nonhoward'] += d['nonhoward']
    S['badstop'] += d['badstop']; S['nofb'] += not d['fb_found']
print('seed', seed, 'count', cnt, 'Nmax', Nmax, 'dmax', dmax, json.dumps(S))
