#!/usr/bin/env python3
"""L-NEW box 153 Step 1 check: the improvement orientation of a degree-2 IDEAL-ACYC genome is a decomposable acyclic USO.
Cube = states of the degree-2 movers (degree-1 movers fixed). Edge s -- s xor e_x is oriented toward the option C_s(x) (the strictly
better face of x at s; it does not depend on s(x)). Checks by brute force (N2 <= NMAX degree-2 movers):
 USO     every face (choice of fixed coordinates) has exactly one sink [Weber-Widmer arXiv 2207.05985 Def. 4]
 COMB    every face of dimension >= 1 has a combed dimension (all its edges in that dimension point the same way) [ibid. §2.2:
         «each face is combed» = decomposable]
 ORDER   in every face the free mover of largest pi is combed (the combing order of Lemma DECOMP)
 ACYC    E(s) = sum_x [s(x) != C_s(x)] 2^pi(x) strictly decreases along every edge (so the orientation is acyclic)
 JUMP    switch-all (JumpAntipodal) from every vertex reaches the sink in <= N2 jumps
Usage: decomp.py genome.json ...   (NMAX env, default 10)"""
import sys, os, json, itertools
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": os.path.abspath(P)}; exec(open(P).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]; topo = ns["topo"]
NMAX = int(os.environ.get("NMAX", "10")); TOT = dict(genomes=0, faces=0, USO=0, COMB=0, ORDER=0, ACYC=0, JUMP=0, maxjump=0)
for p in sys.argv[1:]:
    G = json.load(open(p)); g = Gen(G)
    if max(len(o) for o in g.opts) > 2: continue
    D2 = [x for x in range(g.N) if len(g.opts[x]) == 2]
    if len(D2) > NMAX or not D2: continue
    TOT["genomes"] += 1; pi = topo(G); pos = {v: i for i, v in enumerate(pi)}; n = len(D2); base = list(G["start"])
    def st(bits):
        s = list(base)
        for i, x in enumerate(D2): s[x] = bits[i]
        return s
    Cb = {}
    for bits in itertools.product((0, 1), repeat=n):
        s = st(bits); Cb[bits] = tuple(1 if g.face(s, x, 1) > g.face(s, x, 0) else 0 for x in D2)
    def E(bits): return sum((1 << pos[x]) for i, x in enumerate(D2) if bits[i] != Cb[bits][i])
    for bits in Cb:
        for i in range(n):
            if bits[i] != Cb[bits][i]:
                nb = list(bits); nb[i] = Cb[bits][i]; nb = tuple(nb)
                if not E(nb) < E(bits): TOT["ACYC"] += 1
        cur, j = bits, 0
        while any(cur[i] != Cb[cur][i] for i in range(n)):
            cur = Cb[cur]; j += 1
            if j > n: TOT["JUMP"] += 1; break
        TOT["maxjump"] = max(TOT["maxjump"], j)
    for face in itertools.product((0, 1, None), repeat=n):
        free = [i for i in range(n) if face[i] is None]; TOT["faces"] += 1
        verts = [tuple(face[i] if face[i] is not None else b[free.index(i)] for i in range(n)) for b in itertools.product((0, 1), repeat=len(free))]
        sinks = [v for v in verts if all(v[i] == Cb[v][i] for i in free)]
        if len(sinks) != 1: TOT["USO"] += 1
        if free:
            combed = [i for i in free if len({Cb[v][i] for v in verts}) == 1]
            if not combed: TOT["COMB"] += 1
            top = max(free, key=lambda i: pos[D2[i]])
            if top not in combed: TOT["ORDER"] += 1
print("DECOMP", " ".join(f"{k} {v}" for k, v in TOT.items()))
