#!/usr/bin/env python3
"""L-SI box 92 (correction to box 91, L-RED 62 F1): A*_all := max over ALL vertices v, maximal Lambda-intervals I of v and e-letters z of
#maximal runs of t in I with z in E_t(v) (a per-tuple MAXIMUM; the A* of box 91's Corollary A*-EQUIV). Also C := max c_y(v, I)
(per-tuple maximum) so that C <= A*_all can be read off (cfail: a tuple (v, I, y) with c_y > a_y(v, I); must be 0).
Engines: box91/mult91.py eng_own / eng_g3.  Usage: astar92.py own|g3 G.json ..."""
import sys, os, json, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box91"))
import mult91
def run(T, n, nx, lam, E, rk, evs, odd2, val):
    A = 0; C = 0; cfail = 0
    for v in range(n):
        t = 0
        while t <= T:
            u = t
            while u + 1 <= T and lam(u + 1, v) == lam(t, v): u += 1
            Es = [E(i, v) for i in range(t, u + 1)]; runs = collections.Counter(); tops = collections.Counter()
            for i, S in enumerate(Es):
                for z in S:
                    if i == 0 or z not in Es[i - 1]: runs[z] += 1
                if i and S != Es[i - 1]: tops[max(S ^ Es[i - 1], key=lambda e: rk[e])] += 1
            A = max([A] + list(runs.values())); C = max([C] + list(tops.values()))
            cfail += sum(1 for y, k in tops.items() if k > runs[y])
            t = u + 1
    return A, C, cfail
if __name__ == "__main__":
    eng = sys.argv[1]; print("engine", eng, "instance N+M T C Aall cfail", flush=True)
    for f in sys.argv[2:]:
        G = json.load(open(f)); G = G.get("genome", G); e = mult91.eng_own(G) if eng == "own" else mult91.eng_g3(G)
        a, c, cf = run(*e); print(eng, os.path.basename(f), G["N"] + sum(len(o) for o in G["opts"]), e[0], c, a, cf, flush=True)
