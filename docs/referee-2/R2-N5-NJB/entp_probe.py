#!/usr/bin/env python3
"""REFEREE-2 succ. 7, for §C on NJB-2 / N-NJB-1: at in-scope fallbacks k0 of level L >= 0 with (h) at k0+1, list Even edges (y, z) with
z in R_{k0} and not in Rbar_{k0+1} (evicted at the fallback), lev(Xi_{k0} z, Xi_{k0+1} z) = L with a rise, y unswitched, and (y, z) a
level-L gate at k0+1 but not a gate at k0 (REFEREE's local configuration). Own N5 (../R2-N5-FRZ). Usage: entp_probe.py game.pg runs [--rand]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FRZ"))
import frz_check as FC, njb_check as NJ
RC = FC.RC
args = [a for a in sys.argv[1:] if a != "--rand"]; rand = "--rand" in sys.argv
g = RC.parse(open(args[0]).read()); o = FC.odd_vertex(g); rng = random.Random(7); cnt = 0
for r in range(int(args[1])):
    s0, t0 = FC.s3_start(g) if r == 0 else RC.rand_start(rng, g)
    A, fbs = FC.run_n5(g, o, s0, t0, rng, rand)
    for (a, b_) in NJ.scope_runs(A, fbs, o):
        for k in range(a, b_):
            if not fbs[k] or not A[k + 1].hh: continue
            L = NJ.M_of(A[k])
            if L < 0: continue
            for (y, z), lv in A[k + 1].gates.items():
                if lv != L or (y, z) in A[k].gates or A[k].sg[y] != A[k + 1].sg[y]: continue
                if z in A[k].Rr and z not in A[k + 1].Rbar and FC.lev(g, A[k].Xi[z], A[k + 1].Xi[z]) == L and g.key(A[k + 1].Xi[z]) > g.key(A[k].Xi[z]):
                    cnt += 1
                    if cnt <= 3: print(f"run {r}: fallback {k} level {L}: y={y} z={z}, z in R_k0 -> F_k0+1, Xi(z) {A[k].Xi[z][0]},{A[k].Xi[z][2]} -> {A[k+1].Xi[z][0]},{A[k+1].Xi[z][2]}")
print("configurations", cnt)
