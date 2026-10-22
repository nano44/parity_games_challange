#!/usr/bin/env python3
"""L-RED successor 3 (Opus 5.5), 2026-10-16: attack on L-ALG's (U-MONO_DTL) (relayed by the Lead 16:59Z): at a fixed context
and a fixed round input V, the region union U(V,T) is contained in U(V,T') for consecutive calls (T subset of T').
Repeats L-ALG's experiments/alg/dtl_steal.py measurement (read-only via LALG_DIR, l-alg >= 670a762) and adds a score:
U shrinks, survivors shrink, and as a gradient the number of carry rounds whose steal splits a stored tangle.
Usage: DTL_ORDER=oink LALG_DIR=.. umono.py G.pg ..."""
import sys, os

def _mods():
    ld = os.environ["LALG_DIR"]
    for q in (os.path.join(ld, "experiments", "alg"), os.path.join(ld, "experiments", "harness")):
        if q not in sys.path: sys.path.insert(0, q)
    import dtl_regvec as RV, dtl_ideal as I, pg
    return RV, I, pg

def measure(path):
    RV, I, pg = _mods(); g = pg.read(path); d = RV.build(g); d.run()
    tot = dict(carry=0, U_shrink=0, S_shrink=0, split=0, down=0); ex = []
    for key, occ in d.calls.items():
        p, R = key[0], set(key[1])
        for (s1, r1, v1, h1, t1), (s2, r2, v2, h2, t2) in zip(occ, occ[1:]):
            for r in range(min(len(r1), len(r2))):
                if r1[r] != r2[r] or not r1[r] or r >= len(v1) or r >= len(v2): continue
                A, B = v1[r], v2[r]
                if A == B: continue
                tot["carry"] += 1
                ra, rb = dict(A), dict(B)
                UA = set().union(*ra.values()); UB = set().union(*rb.values())
                # a tangle alive at T whose vertex set meets two different regions at T' (split by the steal)
                regof = {v: t for t, z in rb.items() for v in z}
                for t in t1:
                    vs = {w for w, _ in d.tv[t]} & UA
                    if len({regof.get(v) for v in vs}) > 1: tot["split"] += 1; break
                rega = {v: t for t, z in ra.items() for v in z}
                tot["down"] += sum(1 for v in UA & UB if regof[v] < rega[v])   # pushed into a lower-top region (near miss)
                if not UA <= UB:
                    tot["U_shrink"] += 1
                    if len(ex) < 5: ex.append(("U", len(R), s1, s2, r, sorted(d.idx[v] for v in UA - UB)))
                SA = I.survivors(d, p, r1[r], R, UA, t1); SB = I.survivors(d, p, r1[r], R, UB, t2)
                if not SA <= SB: tot["S_shrink"] += 1
    return tot, ex, d

def score(path):
    tot, _, d = measure(path)
    return 100000 * tot["U_shrink"] + 10000 * tot["S_shrink"] + 10 * tot["down"] + tot["split"] + tot["carry"] / 10.0 + len(d.trace) / 1000.0

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    for f in sys.argv[1:]:
        tot, ex, d = measure(f)
        print(f"== {os.path.basename(f)} order={os.environ.get('DTL_ORDER', 'stable')} searches={len(d.trace)} {tot} {ex}")
