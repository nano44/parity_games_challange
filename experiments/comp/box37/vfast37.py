#!/usr/bin/env python3
"""L-COMP box 37: validate fast37 (Gamma3 N5'-xi run, mover class changes) against ideal37 (IDEAL-CYC text engine) on D_mov, T and
max flips. Usage: vfast37.py G.json ... | vfast37.py --rand COUNT SEED (random genomes: box36 gen36 space, N 2-6, M N..2N+2, k any)."""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "box36")]
import fast37, ideal37
def check(G, name):
    a = fast37.one(G); b = ideal37.heights(G)
    mf = max([f for q, f, l in a["rows"]] or [0])
    ok = a["Dmov"] == b["Dmov"] and a["T3"] == b["T"] and mf == b["maxflip"]
    return ok, f"{name} fast37 T3 {a['T3']} Dmov {a['Dmov']} maxflip {mf} | ideal37 T {b['T']} Dmov {b['Dmov']} maxflip {b['maxflip']} {'OK' if ok else 'MISMATCH'}"
bad = n = 0
if sys.argv[1] == "--rand":
    import gen36
    cnt, seed = int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed)
    for i in range(cnt):
        N = rng.randint(2, 6); M = rng.randint(N, 2 * N + 2)
        lev = rng.choice(gen36.levvecs(N)); D = [1] * N
        for _ in range(M - N): D[rng.randrange(N)] += 1
        xts = [rng.randrange(-1, N) for _ in range(M)]; gate = rng.sample(range(M), M); br = rng.sample(range(M), M)
        bp = [rng.randrange(2) for _ in range(M)]; st = [rng.randrange(d) for d in D]
        G = gen36.make(N, lev, D, xts, gate, br, bp, st)
        ok, s = check(G, f"rand{i}"); n += 1; bad += not ok
        if not ok: print(s, json.dumps(G), flush=True)
else:
    for f in sys.argv[1:]:
        ok, s = check(json.load(open(f)), os.path.basename(f)); n += 1; bad += not ok; print(s, flush=True)
print("genomes", n, "mismatches", bad)
