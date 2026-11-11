#!/usr/bin/env python3
"""L-COMP box 38 item 2(a) SAMPLED: random genomes of (N, M), T3 by U(G). Sampler (stated): lev = a uniformly random nondecreasing
level vector from 0 with steps 0/1 (gen36.levvecs); D = uniform composition of M into N parts >= 1 (rejection); xt uniform in {-1} +
movers; gate, br uniform permutations; bp uniform bits; start uniform; wt = a UNIFORM mover of level lev - 1 (box 33/36 used the first:
this sampler is wider). Counter: T3 (fast36 bin/k, [E-LEV] and FAST36_NOELEV; N5'-xi from S3 on Gamma3 to the first fallback; total).
Out: one JSON line per (N, M, U) at the end + checkpoint every 2,000 genomes (OUT.ck; resume continues at the saved index; genome i is
drawn from Random(f"{SEED}-{N}-{M}-{i}") so a resume is exact). Argmax genomes -> out/argmax/S_N<N>M<M>_U<u>_<mode>.json.
Usage: samp38.py N M COUNT SEED OUT"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "box36")]
import fast36, gen36, u38
N, M, CNT, SEED, OUT = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
LEVS = gen36.levvecs(N)


def draw(i):
    r = random.Random(f"{SEED}-{N}-{M}-{i}"); lev = list(r.choice(LEVS))
    while True:
        D = [r.randint(1, M) for _ in range(N)]
        if sum(D) == M: break
    gate = list(range(M)); r.shuffle(gate); br = list(range(M)); r.shuffle(br)
    opts, g, b = [], [], 0
    for x in range(N):
        oo, gg = [], []
        for _ in range(D[x]):
            lower = [y for y in range(N) if lev[y] == lev[x] - 1]
            oo.append([-1 if lev[x] == 0 else r.choice(lower), r.randrange(-1, N), b]); gg.append(gate[b]); b += 1
        opts.append(oo); g.append(gg)
    return {"N": N, "lev": lev, "opts": opts, "gate": g, "br": br, "bp": [r.randrange(2) for _ in range(M)], "start": [r.randrange(d) for d in D]}


ck = OUT + ".ck"; st = json.load(open(ck)) if os.path.exists(ck) else dict(i=0, T={})
while st["i"] < CNT:
    G = draw(st["i"]); U = str(u38.U(G)); t = st["T"].setdefault(U, dict(n=0, e=-1, ne=-1, ie=None, ine=None))
    te, tn = fast36.one(G, bindir="bin/k")[0], fast36.one(G, noelev=True, bindir="bin/k")[0]
    t["n"] += 1
    if te > t["e"]: t["e"], t["ie"] = te, st["i"]
    if tn > t["ne"]: t["ne"], t["ine"] = tn, st["i"]
    st["i"] += 1
    if st["i"] % 2000 == 0 or st["i"] == CNT:
        json.dump(st, open(ck + ".tmp", "w")); os.replace(ck + ".tmp", ck)
for U, t in sorted(st["T"].items(), key=lambda z: int(z[0])):
    for mode, i in (("elev", t["ie"]), ("noelev", t["ine"])):
        json.dump(draw(i), open(os.path.join(H, "out", "argmax", f"S_N{N}M{M}_U{U}_{mode}.json"), "w"), sort_keys=True)
with open(OUT, "a") as f:
    for U, t in sorted(st["T"].items(), key=lambda z: int(z[0])):
        f.write(json.dumps(dict(N=N, M=M, NM=N + M, U=int(U), genomes=t["n"], T3e=t["e"], T3n=t["ne"], seed=SEED)) + "\n")
