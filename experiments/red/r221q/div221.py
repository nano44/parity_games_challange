#!/usr/bin/env python3
"""L-RED 56 R221 (d): does IDEAL-CYC's T bound N5'-xi on Gamma3? For random Xi-cyclic genomes: own.py IDEAL-CYC run T (ties keep current,
then larger index) vs box 191 idealcyc (trajectory equality) vs N5'-xi on Gamma3(G) (box 190 n5v.py mode xi, iteration count, fallback flag).
Flags genomes with n5v xi != T + 3 (the R118 context relation) and saves them to out/div_*.json. Needs env WT, WT3 (r218/env.sh).
Usage: div221.py SEED COUNT"""
import sys, os, json, random
WT, WT3 = os.environ["WT"], os.environ["WT3"]
sys.path[:0] = [os.path.join(WT3, "experiments/new/box191"), os.path.join(WT, "experiments/new/box190"), os.path.join(WT, "experiments/harness")]
import idealcyc, gamma3, n5v, pg
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import own
from brute221 import rgen
if __name__ != "__main__": raise ImportError("div221 is a script")
seed, cnt = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed); bad = tr = 0
def topg(g): return f"parity {g.n - 1};\n" + "".join(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n" for v in range(g.n))
for i in range(cnt):
    d = rng.randint(1, 4); w = rng.randint(1, 3); G = rgen(rng, d, w, rng.choice([2, 3]))
    o, V, O, _ = own.run(G); T = len(o) - 1; a = idealcyc.run(G)
    inv = {V[("g", (x, k))]: k for x in range(G["N"]) for k in range(len(G["opts"][x]))}
    same = [tuple(inv[v] for v in s) for s, _, _ in o] == a
    g, sig, tau, _ = gamma3.build(G, {"K", "pe", "pb", "m"}); gp = pg.parse(topg(g))
    st, fb, E = n5v.run(gp, "xi", cap=100000); xi = len(st) - 1
    tr += not same
    if xi != T + 3 or not same:
        bad += 1; json.dump(G, open(f"out/div_{seed}_{i}.json", "w"))
        print(f"DIV genome {i} N {G['N']} own T {T} idealcyc T {len(a) - 1} same-traj {same} n5v xi {xi} fb {fb}", flush=True)
print(f"seed {seed} genomes {cnt}: n5v xi != T+3 or trajectory mismatch in {bad}; trajectory mismatches own vs idealcyc {tr}", flush=True)
