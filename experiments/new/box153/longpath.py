#!/usr/bin/env python3
"""L-NEW box 153 Step 3a: longest improving path (single switches, any order) in the decomposable AUSO of a degree-2 IDEAL-ACYC genome,
against its IDEAL run length from the same start. The orientation is acyclic, so the longest directed path from the start is a DP.
Also: random hill-climb over small genomes (CLIMB=n iterations) maximising the longest path from the start, to see whether the Xi side
alone (no W gating) realises Klee-Minty-length paths 2^n - 1. Usage: longpath.py genome.json ... | CLIMB=n SEED=s NM=n longpath.py"""
import sys, os, json, itertools, random, functools
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": os.path.abspath(P)}; exec(open(P).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
def analyse(G):
    g = Gen(G); D2 = [x for x in range(g.N) if len(g.opts[x]) == 2]; base = list(G["start"])
    def C(bits):
        s = list(base)
        for i, x in enumerate(D2): s[x] = bits[i]
        return tuple(1 if g.face(s, x, 1) > g.face(s, x, 0) else 0 for x in D2)
    @functools.lru_cache(maxsize=None)
    def LP(bits):
        c = C(bits); best = 0
        for i in range(len(D2)):
            if bits[i] != c[i]:
                nb = list(bits); nb[i] = c[i]; best = max(best, 1 + LP(tuple(nb)))
        return best
    start = tuple(base[x] for x in D2); T = len(g.run(base)[0]) - 1
    return len(D2), LP(start), T
if os.environ.get("CLIMB"):
    rng = random.Random(int(os.environ.get("SEED", "1"))); NM = int(os.environ.get("NM", "6")); best = None
    def rand():
        N = NM; order = list(range(N)); opts = []; M = 0
        for x in range(N):
            o = []
            for k in (0, 1):
                later = list(range(x + 1, N)); xt = rng.choice(later + [-1]) if later else -1; o.append([-1, xt, M]); M += 1
            opts.append(o)
        return {"N": N, "lev": [0] * N, "opts": opts, "gate": [[2 * x, 2 * x + 1] for x in range(N)], "br": rng.sample(range(M), M),
                "bp": [rng.randint(0, 1) for _ in range(M)], "start": [rng.randint(0, 1) for _ in range(N)], "xorder": order}
    G = rand(); sc = analyse(G)[1]
    for it in range(int(os.environ["CLIMB"])):
        H2 = json.loads(json.dumps(G)); r = rng.random(); x = rng.randrange(NM); k = rng.randrange(2)
        if r < 0.3: later = list(range(x + 1, NM)); H2["opts"][x][k][1] = rng.choice(later + [-1]) if later else -1
        elif r < 0.6: i, j = rng.sample(range(2 * NM), 2); H2["br"][i], H2["br"][j] = H2["br"][j], H2["br"][i]
        elif r < 0.8: H2["bp"][rng.randrange(2 * NM)] ^= 1
        else: H2["start"][x] ^= 1
        s2 = analyse(H2)[1]
        if s2 >= sc: G, sc = H2, s2
    print(f"CLIMB NM {NM} longest improving path {sc} (2^n - 1 = {2 ** NM - 1})"); json.dump(G, open(f"/tmp/claude-0/lp_climb_{NM}.json", "w"))
else:
    for p in sys.argv[1:]:
        G = json.load(open(p))
        if max(len(o) for o in G["opts"]) > 2 or sum(len(o) == 2 for o in G["opts"]) > 16: continue
        n, lp, T = analyse(G); print(f"LONGPATH {os.path.basename(p)} n2 {n} longest {lp} ideal_T {T}")
