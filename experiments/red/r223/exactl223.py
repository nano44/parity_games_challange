#!/usr/bin/env python3
"""L-RED 58 R223 item 1: EXACT-L (P-N5-END §6, claude/l-new 131b4c1c) on IDEAL-ACYC genomes whose Xi-edges follow a RANDOM topological
order (pi), not «smaller index» (L-NEW's acyc family and R222's selfl222 only use smaller indices; vertex indices drive SPEC's ties).
Also an exhaustive part: every N <= 2 genome of exh223 whose Xi-graph is acyclic (no self-loop).
Per genome: L = len(r187 ideal.traj) - 1; N5 (frozen n5v spec) run on Gamma3 from S3 via end222.check: F, T.
Counter: mismatches of F = L + 1 or T = L + 3 (unit: IDEAL-ACYC genome). Usage: exactl223.py SEED COUNT (env WT = WT3)"""
import sys, os, random, json
here = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [here, os.path.join(here, "../r222"), os.path.join(here, "../r187")]
import end222, ideal, exh223
def acyclic(G):
    N = G["N"]; ed = {x: {o[1] for o in G["opts"][x] if o[1] >= 0} for x in range(N)}; col = [0] * N
    def dfs(x):
        col[x] = 1
        for y in ed[x]:
            if col[y] == 1 or (col[y] == 0 and not dfs(y)): return False
        col[x] = 2; return True
    return all(col[x] or dfs(x) for x in range(N))
def test(G, tag, st):
    S, why = ideal.traj(G); L = len(S) - 1; c, T, F = end222.check(G, "spec"); st["n"] += 1; st["maxL"] = max(st["maxL"], L)
    if F != L + 1 or T != L + 3 or any(c.values()):
        st["mis"] += 1; print("MISMATCH", tag, "L", L, why, "F", F, "T", T, c, json.dumps(G), flush=True)
seed, cnt = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed)
st = dict(n=0, mis=0, maxL=0)
for t in exh223.genomes():
    G = exh223.mk(*t)
    if acyclic(G): test(G, "exh", st)
print(f"EXACTL223 exhaustive N<=2 acyclic genomes {st['n']} mismatches {st['mis']} maxL {st['maxL']}", flush=True)
st = dict(n=0, mis=0, maxL=0)
for i in range(cnt):
    d = rng.randint(1, 5); w = rng.randint(1, 3); D = rng.choice([2, 3]); lev = [x // w for x in range(d * w)]; N = len(lev)
    pi = list(range(N)); rng.shuffle(pi); pos = {x: i for i, x in enumerate(pi)}; opts = []
    for x in range(N):
        later = [y for y in range(N) if pos[y] > pos[x]]
        opts.append([[rng.choice([y for y in range(N) if lev[y] == lev[x] - 1]) if lev[x] else -1,
                      rng.choice(later + [-1]) if later else -1, 0] for _ in range(D)])
    M = sum(len(o) for o in opts); perm = list(range(M)); rng.shuffle(perm); gate = []; j = 0
    for x in range(N):
        gate.append([])
        for o in opts[x]: o[2] = j; gate[x].append(perm[j]); j += 1
    br = list(range(M)); rng.shuffle(br)
    G = {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": [rng.randrange(2) for _ in range(M)], "start": [rng.randrange(len(o)) for o in opts]}
    assert acyclic(G); test(G, f"pi_{seed}_{i}", st)
print(f"EXACTL223 random-topological-order seed {seed} genomes {st['n']} mismatches {st['mis']} maxL {st['maxL']}", flush=True)
