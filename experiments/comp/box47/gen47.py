#!/usr/bin/env python3
"""L-COMP box 47: JSON genome (box 46 / L-NEW format: N, lev, opts[x] = [[wt, xt, b], ...], gate[x][k], br[b], bp[b], start[x], optional
eperm = e-slot of the i-th option in GATE order) <-> gen47.h text («N M / lev / x wt xt gt br bp er per option in canonical order / st»).
gate and br are re-ranked to permutations 0..M-1 (order kept); er[option] = eperm[gate rank of the option] (identity = box 189's numbering).
Usage: gen47.py j2t in.json out.txt | t2j in.txt out.json"""
import sys, json
def rerank(v):
    o = sorted(range(len(v)), key=lambda i: v[i]); r = [0] * len(v)
    for j, i in enumerate(o): r[i] = j
    return r
def j2t(G):
    G = G.get("genome", G) if "N" not in G else G; N = G["N"]; O = [(x, k) for x in range(N) for k in range(len(G["opts"][x]))]; M = len(O)
    gt = rerank([G["gate"][x][k] for x, k in O]); br = rerank([G["br"][G["opts"][x][k][2]] for x, k in O]); bp = [G["bp"][G["opts"][x][k][2]] for x, k in O]
    ep = G.get("eperm", list(range(M))); er = [ep[gt[i]] for i in range(M)]
    s = "%d %d\n%s\n" % (N, M, " ".join(map(str, G["lev"])))
    s += "".join("%d %d %d %d %d %d %d\n" % (x, G["opts"][x][k][0], G["opts"][x][k][1], gt[i], br[i], bp[i], er[i]) for i, (x, k) in enumerate(O))
    return s + " ".join(map(str, G["start"])) + "\n"
def t2j(s):
    w = list(map(int, s.split())); N, M = w[0], w[1]; lev = w[2:2 + N]; p = 2 + N; R = [w[p + 7 * i:p + 7 * i + 7] for i in range(M)]; st = w[p + 7 * M:p + 7 * M + N]
    opts = [[] for _ in range(N)]; gate = [[] for _ in range(N)]; br, bp = [0] * M, [0] * M; ep = [0] * M
    for i, (x, wt, xt, gt, b, q, e) in enumerate(R): opts[x].append([wt, xt, i]); gate[x].append(gt); br[i] = b; bp[i] = q; ep[gt] = e
    G = dict(N=N, lev=lev, opts=opts, gate=gate, br=br, bp=bp, start=st)
    if ep != list(range(M)): G["eperm"] = ep
    return G
if __name__ == "__main__":
    if sys.argv[1] == "j2t": open(sys.argv[3], "w").write(j2t(json.load(open(sys.argv[2]))))
    else: json.dump(t2j(open(sys.argv[2]).read()), open(sys.argv[3], "w"), sort_keys=True)
