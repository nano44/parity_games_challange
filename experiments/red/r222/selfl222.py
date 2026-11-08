#!/usr/bin/env python3
"""L-RED 57 R222 item 3 (d): EXACT-L's scope. Genomes whose Xi-edges go to smaller indices (acyclic) or, with probability PSELF, to the
mover itself (a Xi self-loop: NOT in IDEAL-ACYC, R104 «self-loops count as cycles», but «acyclic» if self-loops are not counted).
Per genome: L = len(r187 ideal.traj) - 1, and the N5 (n5v spec) run on Gamma3 from S3 via end222.check: F and total T.
Prints mismatches of F = L + 1 / T = L + 3. Usage: selfl222.py SEED COUNT PSELF   (env WT, WT3)"""
import sys, os, json, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../r187"))
import end222, ideal
seed, cnt, ps = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]); rng = random.Random(seed); mis = 0; tot = 0; selfg = 0
for i in range(cnt):
    d = rng.randint(1, 4); w = rng.randint(1, 3); D = rng.choice([2, 3]); lev = [x // w for x in range(d * w)]; N = len(lev); opts = []
    for x in range(N):
        opts.append([[rng.choice([y for y in range(N) if lev[y] == lev[x] - 1]) if lev[x] else -1,
                      x if rng.random() < ps else rng.choice(list(range(x)) + [-1, -1]), 0] for _ in range(D)])
    M = sum(len(o) for o in opts); perm = list(range(M)); rng.shuffle(perm); gate = []; j = 0
    for x in range(N):
        gate.append([])
        for o in opts[x]: o[2] = j; gate[x].append(perm[j]); j += 1
    br = list(range(M)); rng.shuffle(br)
    G = {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": [rng.randrange(2) for _ in range(M)], "start": [rng.randrange(len(o)) for o in opts]}
    hasself = any(o[1] == x for x in range(N) for o in opts[x]); selfg += hasself
    S, why = ideal.traj(G); L = len(S) - 1
    c, T, F = end222.check(G, "spec"); tot += 1
    if F != L + 1 or T != L + 3:
        mis += 1; json.dump(G, open(f"out/selfl_{seed}_{i}.json", "w")); print("MISMATCH", i, "self" if hasself else "acyc", "L", L, why, "F", F, "T", T, flush=True)
print(f"SELFL222 seed {seed} genomes {tot} with-self {selfg} mismatches {mis} pself {ps}", flush=True)
