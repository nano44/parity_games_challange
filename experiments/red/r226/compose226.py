#!/usr/bin/env python3
"""L-RED 60 R226: compose genomes (disjoint union, then rewires) for the DEPTH-2 race build.
union(A, B, gmode, lshift): B's movers get index offset N_A; B's levels += lshift; gate ranks / beta ranks of B placed
  gmode = "above" (B's gates after A's), "below", or "inter" (interleaved alternately); beta ranks likewise.
  W-targets / Xi-targets of B are offset (−1 stays −1).
rewire(G, x, k, field, target): field 0 = W-target, 1 = Xi-target (b-node successor); target −1 = cW / K0.
add_opt(G, x, wt, xt, gate_pos, beta_pos, bp): append a new option to mover x (gate rank / beta rank inserted at the given position).
measure(G): T, maxD, best X (comp225), and the hub."""
import sys, os, json, copy
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r225"), os.path.join(H, "..", "r221")]
import comp225
def _ranks(ra, rb, mode):
    # ra, rb: lists of ranks (permutations of 0..len-1 each); return combined ranks
    na, nb = len(ra), len(rb)
    if mode == "above": return list(ra), [r + na for r in rb]
    if mode == "below": return [r + nb for r in ra], list(rb)
    # interleave: merged order a0 b0 a1 b1 ...
    order = []; i = j = 0
    while i < na or j < nb:
        if i < na: order.append(("a", i)); i += 1
        if j < nb: order.append(("b", j)); j += 1
    pos = {k: p for p, k in enumerate(order)}
    return [pos[("a", r)] for r in ra], [pos[("b", r)] for r in rb]
def union(A, B, gmode="above", lshift=0, bmode=None):
    bmode = bmode or gmode; NA = A["N"]; MA = sum(len(o) for o in A["opts"])
    off = lambda y: -1 if y < 0 else y + NA
    opts = [list(map(list, o)) for o in A["opts"]] + [[[off(w), off(t), b + MA] for (w, t, b) in o] for o in B["opts"]]
    ga = [r for g in A["gate"] for r in g]; gb = [r for g in B["gate"] for r in g]
    ga2, gb2 = _ranks(ga, gb, gmode)
    gate = []; i = j = 0
    for o in A["opts"]: gate.append(ga2[i:i + len(o)]); i += len(o)
    for o in B["opts"]: gate.append(gb2[j:j + len(o)]); j += len(o)
    bra, brb = _ranks(A["br"], B["br"], bmode)
    return dict(N=NA + B["N"], lev=A["lev"] + [l + lshift for l in B["lev"]], opts=opts, gate=gate, br=bra + brb,
                bp=A["bp"] + B["bp"], start=A["start"] + B["start"])
def rewire(G, x, k, field, target):
    G = copy.deepcopy(G); G["opts"][x][k][field] = target; return G
def add_opt(G, x, wt, xt, gate_pos, beta_pos, bp=0):
    G = copy.deepcopy(G); M = len(G["br"])
    G["gate"] = [[r + (r >= gate_pos) for r in g] for g in G["gate"]]; G["gate"][x].append(gate_pos)
    G["br"] = [r + (r >= beta_pos) for r in G["br"]] + [beta_pos]; G["bp"] = G["bp"] + [bp]
    G["opts"][x].append([wt, xt, M]); return G
def check(G):
    N = G["N"]; M = sum(len(o) for o in G["opts"])
    assert sorted(r for g in G["gate"] for r in g) == list(range(M)), "gate ranks"
    assert sorted(G["br"]) == list(range(M)) and len(G["bp"]) == M
    assert sorted(o[2] for oo in G["opts"] for o in oo) == list(range(M))
    for x in range(N):
        for (w, t, b) in G["opts"][x]:
            assert (w == -1) if G["lev"][x] == 0 else (w >= 0 and G["lev"][w] == G["lev"][x] - 1), ("W", x, w)
            assert -1 <= t < N
    return True
def measure(G):
    check(G); c = comp225.comp(G); return dict(N=G["N"], T=c["T"], maxD=c["maxD"], X=c["best"]["X"], D=c["best"]["D"], Hn=c["best"]["Hn"], Ln=c["best"]["Ln"], hub=c["best"]["v"], vid=c["best"]["vid"])
if __name__ == "__main__":
    for f in sys.argv[1:]: print(f, measure(json.load(open(f))))
