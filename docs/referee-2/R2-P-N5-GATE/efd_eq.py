#!/usr/bin/env python3
# REFEREE-2 successor 38: probe for line L-5's E-2 clause «per-gate flips … = 2·ch_D + 1 … with lamch 0 …, where E-FACE-PAYS (d)
# holds with equality». Own engines only (r2gate.run_g3 / run_cyc of R2-P-N5-GATE/r2gate.py; no lane code). For every gate o with
# faces p_e, p_b and D = succ(e_o): flips(o), ch(p_e), ch(p_b), ch(D), lamch(o) (states where Λ(p_e) or Λ(p_b) changes), recounted
# here from the states. Prints the gates attaining the largest flip count and whether flips = 2·min(ch_pe, ch_pb) + 1 = 2·ch_D + 1.
# Usage: efd_eq.py ENGINE(g3|cyc) FILE.json ...
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import r2gate as RG
eng = sys.argv[1]
for fn in sys.argv[2:]:
    G = RG.load(fn); R = RG.run_g3(G) if eng == "g3" else RG.run_cyc(G)
    S = R["states"]; T = len(S) - 1; f = [s[0] for s in S]; val = [s[1] for s in S]; rows = []
    for (o, pe, pb, eo) in R["gates"]:
        D = R["succ"][eo][0]; fl = cpe = cpb = cD = lam = 0
        for t in range(1, T + 1):
            fl += f[t][o] != f[t - 1][o]; cpe += val[t][pe] != val[t - 1][pe]; cpb += val[t][pb] != val[t - 1][pb]
            cD += val[t][D] != val[t - 1][D]; lam += val[t][pe][0] != val[t - 1][pe][0] or val[t][pb][0] != val[t - 1][pb][0]
        rows.append((fl, cpe, cpb, cD, lam))
    mx = max(r[0] for r in rows); top = sorted(set(r for r in rows if r[0] == mx))
    viol = sum(1 for r in rows if r[0] > 2 * min(r[1], r[2]) + 1)
    eqd = all(r[0] == 2 * min(r[1], r[2]) + 1 for r in top); eqD = all(r[0] == 2 * r[3] + 1 for r in top); l0 = all(r[4] == 0 for r in top)
    print(os.path.basename(fn), eng, "T", T, "gates", len(rows), "maxflips", mx, "at-max (flips, ch_pe, ch_pb, ch_D, lamch):", top,
          "| (d) equality at every max gate:", eqd, "| flips = 2·ch_D + 1:", eqD, "| lamch 0:", l0, "| (d) violations over all gates:", viol, flush=True)
