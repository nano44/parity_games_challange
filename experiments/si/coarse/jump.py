#!/usr/bin/env python3
"""L-SI box 7: DATA for §5-§6 of docs/si/N5-C-box7.md, inside joint λ-phases of one-Odd-choice games:
  (J1) at a non-tame transition, a = σ̄_k(o) != b = σ̄_{k+1}(o) and lev(Ξ_k(a), Ξ_k(b)) > M_k (Lemma TAME, contrapositive);
  (J2) at every transition, a vertex whose (σ_{k+1}, τ)-play avoids o keeps COARSE_{M_k}(Ξ) (Lemma OFF);
  (J3) at a non-tame transition, every exit e with lev(Ξ_k(a), Ξ_k(e)) <= M_k lies in R_{k+1} (Corollary CAP);
  (J4) at each in-phase evicting fallback: leaver carry level L (box 5 definition) vs M_k (is L = M_k?).
Usage: jump.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tame import *

def scan_j(g):
    E, out = states(g); n = g.n; o = odd_choice(g); assert o is not None
    Ed = n5.Engine(n5.dual(g)); ex = []
    for a in out:
        gl = [lev(a["Xi"][a["s"][y]], a["Xi"][z]) for y, z in a["Is"]]; a["M"] = max(gl) if gl else -3
        a["key"] = (tuple(x[0] for x in a["Xi"]), a["t"], tuple(x[0] for x in Ed.evaluate(tuple(a["t"]))[0]))
        a["R"] = reach(g, a["s"], a["t"], o)
    c = dict(J=0, J1=0, J2chk=0, J2viol=0, J3chk=0, J3viol=0, carries=0, L_eq_M=0, L_lt_M=0, L_gt_M=0)
    for i in range(len(out) - 1):
        a, b = out[i], out[i + 1]
        if a["key"] != b["key"]: continue
        M = a["M"]; tame = all(coarse(b["Xi"][v], M) == coarse(a["Xi"][v], M) for v in range(n))
        for v in range(n):
            if v != o and v not in b["R"]:
                c["J2chk"] += 1
                if coarse(b["Xi"][v], M) != coarse(a["Xi"][v], M): c["J2viol"] += 1; ex.append(("J2", i, v))
        if not tame:
            c["J"] += 1; ea, eb = a["sb"][o], b["sb"][o]
            if ea != eb and lev(a["Xi"][ea], a["Xi"][eb]) > M: c["J1"] += 1
            else: ex.append(("J1", i))
            for e in set(g.succ[o]):
                if lev(a["Xi"][ea], a["Xi"][e]) <= M:
                    c["J3chk"] += 1
                    if e not in b["R"] and e != o: c["J3viol"] += 1; ex.append(("J3", i, e))
        if a["fb"]:
            lv = [lev(a["Xi"][y], b["Xi"][y]) for y in range(n) if g.owner[y] == 0 and b["s"][y] != a["s"][y]
                  and y in a["R"] and b["s"][y] not in a["R"] and b["s"][y] != o]
            if lv:
                c["carries"] += 1; L = max(lv)
                c["L_eq_M" if L == M else ("L_lt_M" if L < M else "L_gt_M")] += 1
    return c, ex

if __name__ == "__main__":
    T = {}
    for p in sys.argv[1:]:
        g = load(p); c, ex = scan_j(g)
        for kk, v in c.items(): T[kk] = T.get(kk, 0) + v
        if ex or c["J"]: print(f"{os.path.basename(p):22s}", c, ex[:4])
    print("TOTAL", T)
