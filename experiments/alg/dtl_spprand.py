"""L-ALG succ. 5 (produced on Opus 5.5, 2026-10-17 box 5): (SPP) on random games. For seeds a..b and n in [nmin, nmax]:
gen.random_game(n, d, 1, dmax, seed) with d = n (one priority per vertex possible) or SPPR_D; reports the max of S - |G'|,
the max of S - (|G'| - 1) over phases with |G'| >= 2, and the max S - P (P = p-parity vertices of G'), with witnesses.
DTL_ORDER=oink | stable. Usage: dtl_spprand.py nmin nmax seed0 count"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import gen, dtl_spp as P
sys.setrecursionlimit(100000)
nmin, nmax, s0, cnt = map(int, sys.argv[1:5]); dmax = int(os.environ.get("SPPR_DMAX", "3"))
best = {"G": (-99,), "G1": (-99,), "P": (-99,), "S": (0,)}
for k in range(cnt):
    seed = s0 + k; n = nmin + k % (nmax - nmin + 1)
    g = gen.random_game(n, int(os.environ.get("SPPR_D", n)), 1, dmax, seed)
    d = P.build(g); d.run()
    for r in P.phases(d):
        best["G"] = max(best["G"], (r["S"] - r["G"], seed, n, r["S"], r["G"]))
        if r["G"] >= 2: best["G1"] = max(best["G1"], (r["S"] - r["G"] + 1, seed, n, r["S"], r["G"]))
        best["P"] = max(best["P"], (r["S"] - r["P"], seed, n, r["S"], r["P"]))
        best["S"] = max(best["S"], (r["S"], seed, n, r["G"]))
print(f"order={os.environ.get('DTL_ORDER', 'stable')} n={nmin}..{nmax} seeds {s0}..{s0 + cnt - 1} dmax={dmax}:", best)
