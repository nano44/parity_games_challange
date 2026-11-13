#!/usr/bin/env python3
"""REFEREE successor 35: the abstract bit model (gk_abs.py) against the genome simulator (gk_ideal.py) on ARBITRARY mover states
(wires at option 0, where they stay): ABS1 = states whose IDEAL step differs from the abstract step (must be 0); PREF1 = (state,
mover) pairs where «the other option is strictly Xi-better» differs (must be 0); WIRE = states where a wire has an available
second option (must be 0: wires never move from option 0, from ANY state).
usage: gk_abs_rand.py kmin kmax nstates seed"""
import random
import sys
import gk_abs as A
import gk_build as B
import gk_ideal as I
kmin, kmax, ns, seed = (int(a) for a in sys.argv[1:5])
rnd = random.Random(seed)
for k in range(kmin, kmax + 1):
    G = B.genome(k); nm = G['names']; N = G['N']
    abs1 = pref1 = wire = moved = 0
    for i in range(ns):
        s = [0 if nm[x].startswith('w') else rnd.randrange(2) for x in range(N)]
        sa = {nm[x]: s[x] for x in range(N) if not nm[x].startswith('w')}
        s2, why = I.step(G, s)
        n, p, kap = A.step(k, sa)
        if any(s2[x] != n.get(nm[x], 0) for x in range(N)): abs1 += 1
        if why is None: moved += 1
        for x in range(N):
            av = I.avail(G, s, x)
            if nm[x].startswith('w'):
                if len(av) > 1: wire += 1
            elif (len(av) == 2) != (p[nm[x]] != s[x]): pref1 += 1
    print('G_%d: %d arbitrary states (seed %d): ABS1 %d PREF1 %d WIRE %d | states where the IDEAL step moves: %d' % (k, ns, seed, abs1, pref1, wire, moved))
    sys.stdout.flush()
