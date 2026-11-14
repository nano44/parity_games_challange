#!/usr/bin/env python3
"""L-NEW box 147: hill-climb the unchained RANK (rank.py) on 2-wide deg-2 IDEAL-ACYC ladders (box143/dclimb.py rand / mut: R188
genome format, acyclic Xi forward in a mutable xorder). SCORE = (max RANK over unchained steps, U) or with ALL=1 (max RANK over all
steps, steps). RW=1: RANKW (count only key-ready unstable movers above y: Xi-better option = key-preferred
option under the keys of state t-1). Usage: rclimb.py d iters seed out.json"""
import sys, os, json, random
HERE = os.path.dirname(os.path.abspath(__file__))
s1 = os.path.join(HERE, "..", "box143", "dclimb.py"); n1 = {"__file__": s1}; exec(open(s1).read().split("def score(G):")[0], n1)
P = os.path.join(HERE, "stat.py"); ns = {"__file__": P}; exec(open(P).read().split('\nif __name__')[0], ns)
run, fc, topo, label = ns["run"], ns["fc"], ns["topo"], ns["label"]
ALL = os.environ.get("ALL"); RW = os.environ.get("RW"); feats = ns["feats"]
def unst(G, s):
    N, opts = G["N"], G["opts"]; val, idx, _, M = fc.values(G, s)
    return [int(any(val(N + idx[(v, k)]) > val(N + idx[(v, s[v])]) for k in range(len(opts[v])))) for v in range(N)]
def score(G):
    S, CUR, KEY, why = run(G, cap=3000); n = G["N"]; pos = {v: i for i, v in enumerate(topo(G))}; lab, least = label(G, S)
    if RW:
        FF = [feats(G, list(s), pos) for s in S]; US = [[int(F["UNST"][x] and F["KP"][x] == F["B"][x]) for x in range(n)] for F in FF]
    else: US = [unst(G, list(s)) for s in S]
    rk = {}
    for t in range(1, len(S)):
        y = max((x for x in range(n) if S[t][x] != S[t - 1][x]), key=lambda x: pos[x])
        rk[t] = 1 + sum(1 for x in range(n) if US[t - 1][x] and pos[x] > pos[y])
    U = sum(1 for c in lab.values() if not c)
    if ALL: return (max(rk.values(), default=0), len(S) - 1)
    return (max((rk[t] for t in lab if not lab[t]), default=0), U)
if __name__ == "__main__":
    d, iters, seed, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(seed); random.seed(seed)
    G = n1["rand"](d, rng); bs = score(G); best = (bs, G)
    for it in range(iters):
        H = n1["mut"](G, rng); hs = score(H)
        if hs >= bs:
            G, bs = H, hs
            if bs > best[0]: best = (bs, G); print("IT", it, "SCORE", bs, flush=True); json.dump(G, open(out, "w"))
        if it % 4000 == 3999 and bs < best[0]: G, bs = json.loads(json.dumps(best[1])), best[0]
    print("BEST", best[0], flush=True)
