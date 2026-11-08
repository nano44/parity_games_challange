#!/usr/bin/env python3
"""L-RED 61 R227 item 1: INDEPENDENT re-arming-DAG census for L-NEW 65 BOX 198 (claude/l-new fcba92fc) on R221 own.py (IDEAL-CYC Howard,
[E-LEV] unless EORD=rev). No L-NEW code. Per (v, maximal Lambda-interval I): tops; c_y = #tops equal to y; Dhi_y = #distinct values of
E_t(v) ∩ {e more relevant than y}; RA(y) = the most relevant top strictly between two consecutive y-tops (per gap); P(y) = 1 + Σ_{z∈RA(y)} P(z);
depth(y) = longest RA-chain from y (letters); fan-in = max |RA(y)|.
Counters (unit: (v, I, y) unless said): ph1 (c_y > Dhi_y), ph2 (A_xy > 2 Dhi_y + 1, unit pair), phc (Dhi_y != 1 + Σ_{z above y} c_z), raup (an RA letter
not above y), rp (c_y > P(y)), lexdec (a top not in the new set; unit change). Records: C, maxP, depth, fanin, A, T.
Usage: ra227.py G.json ..."""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r226"), os.path.join(H, "..", "r225"), os.path.join(H, "..", "r221")]
import own
from alth227 import altpair
def census(G, cap=3000):
    out, V, O, ow = own.run(G, cap); n, prio, o_, succ, _, _ = own.build(G); rk = own.VJ(prio).rk; evs = {V[("e", q)] for q in O}
    T = len(out) - 1; c = dict(ph1=0, ph2=0, phc=0, raup=0, rp=0, lexdec=0, C=0, maxP=0, depth=0, fanin=0, A=0, T=T)
    for v in range(n):
        t = 0
        while t <= T:
            u = t
            while u + 1 <= T and out[u + 1][1][v][0] == out[t][1][v][0]: u += 1
            Es = [frozenset(e for e in out[i][1][v][1] if e in evs) for i in range(t, u + 1)]
            tops = []
            for a, b in zip(Es, Es[1:]):
                if a != b:
                    z = max(a ^ b, key=lambda e: rk[e]); tops.append(z)
                    if z not in b: c["lexdec"] += 1
            t = u + 1
            if not tops: continue
            L = sorted(set(tops), key=lambda e: -rk[e])           # most relevant first
            cy = {y: tops.count(y) for y in L}
            RA = {}
            for y in L:
                idx = [i for i, z in enumerate(tops) if z == y]; RA[y] = set()
                for i, j in zip(idx, idx[1:]):
                    if j > i + 1: RA[y].add(max(tops[i + 1:j], key=lambda e: rk[e]))
                for z in RA[y]:
                    if rk[z] <= rk[y]: c["raup"] += 1
            P = {}; dep = {}
            for y in L:                                           # RA letters are above y, so already done
                P[y] = 1 + sum(P[z] for z in RA[y] if z in P); dep[y] = 1 + max((dep[z] for z in RA[y] if z in dep), default=0)
            for y in L:
                Dhi = len({frozenset(e for e in E if rk[e] > rk[y]) for E in Es})
                if cy[y] > Dhi: c["ph1"] += 1
                if Dhi != 1 + sum(cy[z] for z in L if rk[z] > rk[y]): c["phc"] += 1
                if cy[y] > P[y]: c["rp"] += 1
                for x in L:
                    if rk[x] < rk[y]:
                        a = max(altpair(tops, x, y), altpair(tops, y, x)); c["A"] = max(c["A"], a)
                        if a > 2 * Dhi + 1: c["ph2"] += 1
                c["C"] = max(c["C"], cy[y]); c["maxP"] = max(c["maxP"], P[y]); c["depth"] = max(c["depth"], dep[y]); c["fanin"] = max(c["fanin"], len(RA[y]))
            if len(L) == 1: c["A"] = max(c["A"], 1)
    return c
if __name__ == "__main__":
    K = ("T", "C", "maxP", "depth", "fanin", "A", "ph1", "ph2", "phc", "raup", "rp", "lexdec")
    print("instance", " ".join(K))
    for f in sys.argv[1:]:
        c = census(json.load(open(f))); print(os.path.basename(f), " ".join(str(c[k]) for k in K), flush=True)
