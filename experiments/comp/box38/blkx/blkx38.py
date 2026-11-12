#!/usr/bin/env python3
"""L-COMP box 38 (Lead 04:03Z preempting check): L-NEW 70's BLKX23_n48 (claude/l-new d3fc2d21 experiments/new/box206/inst, sha1 3275991e)
on MY IDEAL-CYC engine box37/ideal37.py (text engine; tie rule stated there; = L-NEW gfc203.hist_ideal on 41 genomes in BOX 37).
Counters (unit: one run of IDEAL-CYC(G), states 0..T; scope R118 (a)):
  T = number of Howard steps (len(H) - 1); D^tot(v) = #distinct (Lambda_t(v), E_t(v)), E_t = e-vertices of Pi_t(v) (P-N5-QN l. 71-72);
  D_mov = max over movers. k = Xi-feedback number (box36 own36.kfvs, brute force).
  Top block (box 206 Addendum B text, block206.py header): the e-vertices of the gates of the movers of the highest level L; Dtop(x) =
  #distinct E_t(x) ∩ block over the run (Lambda ignored). Integer reading: bit i = the block element of relevance rank i (rank 0 = least
  relevant = smallest priority; e-priorities are distinct). Usage: blkx38.py G.json [mover]"""
import sys, os, json
H0 = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H0, "..", "..", "box37"), os.path.join(H0, "..", "..", "box36")]
import ideal37, own36
G = json.load(open(sys.argv[1])); X = int(sys.argv[2]) if len(sys.argv) > 2 else None
g, V, H = ideal37.run(G); T = len(H) - 1; N = G["N"]
ev = {V[k] for k in V if isinstance(k, tuple) and k[0] == "e"}
L = max(G["lev"]); block = sorted((V[("e", (x, k))] for x in range(N) if G["lev"][x] == L for k in range(len(G["opts"][x]))), key=lambda v: g.prio[v])
rank = {v: i for i, v in enumerate(block)}; bset = set(block)
name = {v: k for k, v in V.items()}
Dtot = {x: len({(H[t][0][V[("x", x)]][0], frozenset(set(H[t][0][V[("x", x)]][1]) & ev)) for t in range(T + 1)}) for x in range(N)}
Dtop = {x: len({frozenset(set(H[t][0][V[("x", x)]][1]) & bset) for t in range(T + 1)}) for x in range(N)}
dm = max(Dtot.values())
print(f"T {T} k {own36.kfvs(G, 3)} N {N} M {sum(len(o) for o in G['opts'])} L {L} b {len(block)} D_mov {dm} argmax {[x for x in Dtot if Dtot[x] == dm]}")
print("block (rank: vertex, prio, gate):", [(rank[v], v, g.prio[v], name[v][1]) for v in block])
print("Dtop max", max(Dtop.values()), "argmax", [x for x in Dtop if Dtop[x] == max(Dtop.values())], "F0(b)", 1 + len(block) * (len(block) + 1) // 2)
print("D^tot per mover:", json.dumps(Dtot))
print("Dtop per mover:", json.dumps(Dtop))
if X is not None:
    v = V[("x", X)]; seq = []
    for t in range(T + 1):
        lam = H[t][0][v][0]; s = set(H[t][0][v][1]) & bset; val = sum(1 << rank[u] for u in s)
        seq.append(val)
        print(f"t {t:3d} Lambda {lam} ({name.get(lam)}) block {sorted(rank[u] for u in s)} int {val} sigma(x) -> {name[H[t][2][v]]}")
    print("mover", X, "block-integer sequence:", seq, "distinct", len(set(seq)))
