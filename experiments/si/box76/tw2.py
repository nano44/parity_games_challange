#!/usr/bin/env python3
"""L-SI box 76: Xi-DAG (tropical) increments. For every mover x of the corpus runs (tw.py corpus and simulator):
PF_x (pi changes), moves(x), D(x) = strict Xi-descendants (Xi-graph over ALL options), MD(x) = max moves over D(x) (0 if empty).
Prints per d the max of moves(x) - MD(x), PF_x - MD(x), PF_x - SD(x) (SD = sum of moves over D(x)), moves(x) - 1 - PF_x (must be <= 0,
AND-GATE (b)), and the max Xi-depth; witnesses."""
import sys, os, itertools, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tw import load_corpus, is_lr, Sim, analyse
def desc(G):
    N = G["N"]; ch = [{G["opts"][x][k][1] for k in range(2)} - {-1} for x in range(N)]; D = [None] * N
    def f(x):
        if D[x] is None:
            s = set()
            for y in ch[x]: s |= {y} | f(y)
            D[x] = s
        return D[x]
    for x in range(N): f(x)
    dep = [0] * N
    def h(x): return 0 if not ch[x] else 1 + max(h(y) for y in ch[x])
    return D, [h(x) for x in range(N)]
def main():
    R = collections.defaultdict(lambda: [-99, None]); C = collections.Counter()
    def upd(k, v, w):
        if v > R[k][0]: R[k] = [v, w]
    for path, G in load_corpus():
        if not is_lr(G): continue
        sim = Sim(G); N = G["N"]; d = N // 2; D, H = desc(G)
        Z = {G["opts"][x][k][1] for x in range(N) for k in range(2)} - {-1}
        for s0 in (itertools.product((0, 1), repeat=N) if N <= 10 else [tuple(G["start"])]):
            S = sim.run(s0); a = analyse(sim, S); T = a["T"]
            mv = [sum(1 for t in range(1, T + 1) if x in a["Mv"][t]) for x in range(N)]
            PF = [sum(1 for t in range(1, T + 1) if a["pi"][t][x] != a["pi"][t - 1][x]) for x in range(N)]
            for x in range(N):
                if mv[x] > 1 + PF[x]: C["AGB_VIOL"] += 1
                MD = max([mv[y] for y in D[x]] or [0]); SD = sum(mv[y] for y in D[x])
                w = (path, "".join(map(str, s0)), x, G["lev"][x], x in Z, mv[x], PF[x], MD, H[x])
                upd((d, "mv-MD"), mv[x] - MD, w); upd((d, "PF-MD"), PF[x] - MD, w); upd((d, "PF-SD"), PF[x] - SD, w)
                upd((d, "mv-1-PF"), mv[x] - 1 - PF[x], w); upd((d, "depth"), H[x], w)
                if x in Z and G["lev"][x] >= 1: upd((d, "Z:mv-MD"), mv[x] - MD, w); upd((d, "Z:PF"), PF[x], w)
                C["movers"] += 1
                if mv[x] == 1 + PF[x]: C["mv=1+PF"] += 1
    print("INFO", dict(C))
    for k in sorted(R): print(k, R[k][0], "witness(path,start,x,lev,inZ,moves,PF,MD,depth)", R[k][1])
if __name__ == "__main__":
    main()
