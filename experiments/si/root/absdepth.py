#!/usr/bin/env python3
"""L-SI box 22 (successor 18): DATA for docs/si/N5-ABSCYC-box22.md, Theorem ABS-DEPTH in the cyclic abstract model of abscyc.py
(docs/si/N5-GCX-box21.md §8). For every run and every non-terminal v, with d*(v) := the number of non-terminals on v's FINAL play:
  DEPTH_V   v's play at some state t >= d*(v) differs from its final play (the theorem says 0 under GEN);
  NDEPTH_V  N_t(v) != N*(v) at some t >= d*(v);
  N_DROP / M_DROP  N or M falls along the run (Facts MONO and N-MONO say 0).
Runs where GEN fails (two different plays from one vertex with equal N among the run's strategies) are counted apart (suffix _nogen).
SMALL=1: weights and terminal values in {-2..2} (ties frequent). MUT=1: d*(v) - 1 in place of d*(v) (must bite).
--tie: the GEN-failure instance (note §3): vertex 2 keeps an N-tied non-final play one step past d*(2) = 1.
Usage: absdepth.py COUNT NLIST SEED   (NLIST like 4,5,6) | --tie"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import abscyc as A
SMALL = os.environ.get("SMALL") == "1"; MUT = os.environ.get("MUT") == "1"; C = Counter()

def rg(rng, n, nt):
    g = A.rgame(rng, n, nt)
    if not SMALL: return g
    n_, succ, w, h, T = g
    w = [rng.randint(-2, 2) for _ in range(n)]; h = [rng.randint(-2, 2) for _ in range(nt)]; T = [x + rng.randint(0, 2) for x in h]
    return (n, succ, w, h, T)

def full(s, v, n):
    p = A.play(s, v, n); return tuple(p) + (s[p[-1]],)

def gen_ok(g, tr):
    n = g[0]; seen = {}
    for s in tr:
        M, N = A.plays(g, s)
        for v in range(n):
            if seen.setdefault((v, N[v]), full(s, v, n)) != full(s, v, n): return False
    return True

TIE = ((3, [[1, 3], [0, 2, 5], [0, 4, 5]], [-1, 1, 1], [-1, 1, -1], [0, 1, 1]), [3, 5, 0])

def main():
    if sys.argv[1] == "--tie":
        tr = A.trace(*TIE); n = 3; fin = tr[-1]
        ok = tr == [[3, 5, 0], [1, 5, 0], [1, 2, 4]] and len(A.play(fin, 2, n)) == 1 and full(tr[1], 2, n) != full(fin, 2, n) \
            and A.plays(TIE[0], tr[1])[1][2] == A.plays(TIE[0], fin)[1][2]
        print("TIE trace", tr); print("TIE REPRODUCED" if ok else "TIE DIFFERS"); return
    cnt, ns, seed = int(sys.argv[1]), [int(x) for x in sys.argv[2].split(",")], int(sys.argv[3])
    for n in ns:
        rng = random.Random(seed * 1000 + n)
        for _ in range(cnt):
            g = rg(rng, n, rng.randint(2, 3)); s = A.valid_start(rng, g)
            if s is None: continue
            tr = A.trace(g, s)
            if tr is None: C["NOPT"] += 1; continue
            C["runs"] += 1; C["steps_max"] = max(C["steps_max"], len(tr) - 1)
            fin = tr[-1]; ok = gen_ok(g, tr); suf = "" if ok else "_nogen"; C["runs_nogen"] += not ok
            V = [A.plays(g, x) for x in tr]
            dmax = max(len(A.play(fin, v, n)) for v in range(n)); C["steps_gt_maxfinaldepth"] += (len(tr) - 1) > dmax
            for k in range(len(tr) - 1):
                if any(a > b for a, b in zip(V[k][1], V[k + 1][1])): C["N_DROP"] += 1
                if any(a > b for a, b in zip(V[k][0], V[k + 1][0])): C["M_DROP"] += 1
            for v in range(n):
                d = len(A.play(fin, v, n)) - (1 if MUT else 0); C["vertices"] += 1
                if any(full(tr[j], v, n) != full(fin, v, n) for j in range(d, len(tr))): C["DEPTH_V" + suf] += 1
                if any(V[j][1][v] != V[-1][1][v] for j in range(d, len(tr))): C["NDEPTH_V" + suf] += 1
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    print("ABSDEPTH PASS" if not any(k in C for k in ("DEPTH_V", "NDEPTH_V", "N_DROP", "M_DROP")) else "ABSDEPTH FAIL")

if __name__ == "__main__":
    main()
