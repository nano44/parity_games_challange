#!/usr/bin/env python3
"""L-SI box 88: CARRY test (docs/si/box88-nest.md §3). For each real bit B_l with threshold r = rank(e_S): run Howard on IDEAL-CYC
twice from the same start, (i) the real run (idealcyc.run's rule: largest full key, ties keep current, then larger index) and (ii) the
LOW-BLIND-r run: largest Pi_r key (cycle-node reward, path weight on ranks >= r), ties keep current, then larger index. Compare the
Pi_r-trajectories P_t = (Pi_r(val_t(v)))_v step by step. «same» = identical sequences (then data below rank r never steered the
dynamics at ranks >= r: no carry into level r); else the first step where they differ, and the run lengths.
Usage: blind88.py BOX81DIR GENOME.json ..."""
import sys, os, json
B81 = sys.argv[1]; sys.path[:0] = [B81, os.path.join(B81, "ref", "experiments", "new", "box191"), os.path.join(B81, "ref", "experiments", "new", "box189")]
import idealcyc, gamma3
def runk(h, E, s, movers, keyf, cap=3000):
    vs, _ = E.evaluate(s); out = [vs]
    while len(out) <= cap:
        ns = list(s)
        for x in movers: ns[x] = max(h.succ[x], key=lambda w: (keyf(vs[w]), w == s[x], w))
        ns = tuple(ns)
        if ns == s: break
        s = ns; vs, _ = E.evaluate(s); out.append(vs)
    return out
for f in sys.argv[2:]:
    G = json.load(open(f)); nm = json.load(open(f[:-5] + ".names.json")); h, s0, movers, inv = idealcyc.build(G); E = idealcyc.Engine(h)
    _, _, _, V = gamma3.build(G, set()); res = []
    bits = sorted((int(n[1:]), x) for x, n in enumerate(nm["movers"]) if n[0] == "B" and n[1:].isdigit())
    real = runk(h, E, s0, movers, E.key)
    for l, x in bits:
        r = E.rank[V[("e", (x, nm["opts"][x].index("SET")))]]; mask = ~((1 << r) - 1)
        P = lambda val: (E.rew[val[0]], E.weight(val[1] & mask))
        bl = runk(h, E, s0, movers, P)
        A = [tuple(P(v) for v in vs) for vs in real]; B = [tuple(P(v) for v in vs) for vs in bl]
        dA = [a for i, a in enumerate(A) if i == 0 or a != A[i - 1]]; dB = [b for i, b in enumerate(B) if i == 0 or b != B[i - 1]]
        first = next((i for i in range(min(len(A), len(B))) if A[i] != B[i]), None)
        res.append(f"B{l}:" + ("same" if A == B else f"diff@{first}") + f"(T {len(A) - 1}/{len(B) - 1}, distinct {len(dA)}/{len(dB)}, distinct-seq {'same' if dA == dB else 'diff'})")
    print(os.path.basename(f), " ".join(res))
