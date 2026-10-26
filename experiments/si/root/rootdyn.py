#!/usr/bin/env python3
"""L-SI box 20 (successor 16): DATA for note §29 (the root's dynamics). For the phase and Odd choice vertex r with the most rho events
(or the given ones), class c := lambda(r), U := lambda^-1(c), Q_c := Odd choice vertices of U other than c:
  Fr_k := {z in U : z's honest play at k meets no vertex of Q_c}   (the "direct" region of the class; r direct iff sigma-bar_k(r) in Fr_k)
Per transition k -> k+1: fb, r direct at k, |Fr|, the vertices entering / leaving Fr (IN / OUT) and, for IN at an S4a step, whether the
entering vertex z itself switched (SELF) or a vertex on its new play did (DOWN); c in D; Y-FORM_r (M(r) = wt(r) + min over
succ(r) cap Fr of M) at direct states (YFORM_V counts failures); rho at r. Per fallback-free run of direct states: rho_r and the
number of IN events. Usage: rootdyn.py GAME [START] [PHASE_START R]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from common import *

def honest_avoid(nxt, S, n):
    return avoid(nxt, S, n)

def main():
    g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and not sys.argv[2].isdigit() else None
    E, R = rows(g, st); Q = [v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2]
    best = None
    for i, j in phases(R):
        for q in Q:
            rq = sum(E.key(R[k]["vs"][q]) != E.key(R[k + 1]["vs"][q]) for k in range(i, j))
            if best is None or rq > best[0]: best = (rq, i, j, q)
    rq, i, j, r = best
    if len(sys.argv) > 4: i = int(sys.argv[-2]); r = int(sys.argv[-1]); j = max(jj for ii, jj in phases(R) if ii == i)
    c = R[i]["vs"][r][0]; U = {v for v in range(g.n) if R[i]["vs"][v][0] == c}; Qc = {q for q in Q if q in U and q != c}
    print(f"phase@{i} len={j - i} r={r} c={c} |U|={len(U)} Qc={sorted(Qc)} deg(r)={len(set(g.succ[r]))} c_owner={g.owner[c]} "
          f"c_in_Q={c in Q}")
    Cn = Counter(); runs = []; cur = None
    for k in range(i, j + 1):
        A = R[k]; D = Dset(g, A); Fr = honest_avoid(A["nxt"], Qc, g.n) & U
        direct = A["sb"][r] in Fr
        if direct:
            ys = [y for y in set(g.succ[r]) if y in Fr]
            if M(E, A["vs"][r]) != wt(E, r, c) + min(M(E, A["vs"][y]) for y in ys): Cn["YFORM_V"] += 1
            Cn["yform_checks"] += 1
        if k == j: break
        B = R[k + 1]; FrB = honest_avoid(B["nxt"], Qc, g.n) & U
        rho = E.key(A["vs"][r]) != E.key(B["vs"][r])
        IN, OUT = sorted(FrB - Fr), sorted(Fr - FrB)
        tags = []
        for z in IN:
            if A["fb"]: tags.append("fb"); continue
            tags.append("SELF" if A["s"][z] != B["s"][z] else "DOWN")
        Cn["IN_" + ("fb" if A["fb"] else "s4a")] += len(IN); Cn["OUT_" + ("fb" if A["fb"] else "s4a")] += len(OUT)
        Cn["c_in_D"] += c in D
        if A["fb"] or not direct:
            if cur: runs.append(cur)
            cur = None
        else:
            if cur is None: cur = dict(start=k - i, rho=0, IN=0, OUT=0, Fmax=0)
            cur["rho"] += rho; cur["IN"] += len(IN); cur["OUT"] += len(OUT); cur["Fmax"] = max(cur["Fmax"], len(Fr))
        spl = lambda X, z: "s" if X["W"][z][0] != c else "u"
        insp = [spl(A, z) for z in IN]; Cn["IN_split_at_k"] += insp.count("s")
        gates = " ".join(f"{q}{'*' if q in D else ''}{spl(A, q)}" for q in sorted(Qc))
        print(f"  t={k - i:3d} {'fb ' if A['fb'] else 's4a'} direct={int(direct)} |Fr|={len(Fr):2d} rho_r={int(rho)} "
              f"Qc[*=D,s/u=split]={gates} sbar(r)={A['sb'][r]} IN={list(zip(IN, tags, insp))} OUT={OUT}")
    if cur: runs.append(cur)
    print("RUNS (fallback-free, r direct):", [(x["start"], x["rho"], x["IN"], x["OUT"], x["Fmax"]) for x in runs])
    print(" ".join(f"{a}={b}" for a, b in sorted(Cn.items())))

if __name__ == "__main__":
    main()
