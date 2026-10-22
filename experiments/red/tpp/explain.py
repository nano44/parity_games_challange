"""Explain each (TREE-PIECE⁺) violation of a game (b12_ident.run / treepieces, unmodified): the two call sequences side by side
(depth, |R|, res, e, |V|, piece), and for every vertex of the later search the earlier searches that held its keys.
Usage: [LALG_DIR=..] DTL_ORDER=.. explain.py G.pg"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tpclimb as T
I, pg = T.I, T.pg
sys.setrecursionlimit(100000); order = os.environ.get("DTL_ORDER", "stable"); g = pg.read(sys.argv[1]); n = g.n
d = I.run(g, order); L = [(ph, d.allc.get(id(c), [])) for ph, c in d.log]


def pieces(A):
    out = []
    for i, (dep, R, res, e, V) in enumerate(A):
        nx = next((k for k in range(i + 1, len(A)) if A[k][0] <= dep), None)
        out.append(R - (A[nx][1] if nx is not None and A[nx][0] == dep else frozenset()))
    return out


for s in range(1, len(L)):
    (pa, A), (pb, Bc) = L[s - 1], L[s]
    if pa != pb or A == Bc: continue
    seen = set()
    for t in range(s):
        if L[t][0] == pb: seen |= I.treepieces(L[t][1], n)
    k = I.treepieces(Bc, n)
    if k - seen: continue
    print(f"VIOLATION order {order}: phase {pb}, searches {s-1} -> {s}")
    PA, PB = pieces(A), pieces(Bc)
    for j in range(max(len(A), len(Bc))):
        f = lambda C, P, j: "-" if j >= len(C) else f"d{C[j][0]} |R|{len(C[j][1])} res{C[j][2]} e{C[j][3]} V{sorted(C[j][4])} piece{sorted(P[j])}"
        same = j < len(A) and j < len(Bc) and A[j] == Bc[j] and PA[j] == PB[j]
        print(f"  {j:2d} {'=' if same else '*'} s{s-1}: {f(A, PA, j)}")
        if not same: print(f"       s{s}: {f(Bc, PB, j)}")
    for v in sorted({x[0] for x in k}):
        for x in sorted(y for y in k if y[0] == v):
            held = [t for t in range(s) if L[t][0] == pb and x in I.treepieces(L[t][1], n)]
            if s - 1 not in held: print(f"  key {x} of vertex {v} not held at s{s-1}; held at searches {held}")
