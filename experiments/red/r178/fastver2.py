#!/usr/bin/env python3
"""L-RED R178: fastcyc <-> abs177 (si.py engine) on random cyclic genomes and given champions. Usage: fastver2.py trials seed [files]"""
import sys, os, random, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H); sys.path.insert(0, os.path.join(H, "..", "r177"))
import fastcyc as F, abs177 as A
def conv(G):
    N = G["N"]; deg = G["deg"]
    return dict(levels=[l + 1 for l in G["lev"]], opts=[[["W" if o[0] < 0 else o[0], "X" if o[1] < 0 else o[1]] for o in G["opts"][v]] for v in range(N)],
                perm=list(range(N)) + [N + G["gate"][v][k] for v in range(N) for k in range(deg)], brank=G["br"], bpar=G["bp"],
                start=G["start"], bper=True)
T, seed = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed); bad = 0; tot = 0
Gs = [F.randG(rng.randint(2, 4), rng.randint(2, 3), rng, rng.choice([1, 2, 3])) for _ in range(T)] + [json.load(open(p)) for p in sys.argv[3:]]
for G in Gs:
    try: b = A.simulate(conv(G))
    except RuntimeError as e: print("ENGINE", e); continue
    a = F.simulate(G); tot += 1
    if a[0] != b[0] or a[1] != b[2]: bad += 1; print("MISMATCH", a, b[:3])
print("FASTVER2", tot, "genomes, mismatches", bad)
