#!/usr/bin/env python3
"""REFEREE-2 successor 42: two small checks for Addendum 4 of R2-P-N5-EXP.md (fixes entries 6-8 and line L-3 at l-red-b 10dfedb6).
r2exp.py / r2lem.py lineage (my generator, my lane's model); nothing of the lane is imported.
  r3      fixes entry 7.1: clause (R3) of LEMMA′ with its range. Per k, over the windows (j, a, t) of the recursion with j ≥ 2:
          r3win  [window]: s_τ(E(j)) ≠ a for some τ with t − 1 ≤ τ < last, or E(j) not at c under s_last        must 0
          literal [window]: s_τ(E(j)) ≠ a for some τ < t − 1 (the wording WITHOUT a lower end fails there)      CONTROL: must be
          2^(k−1) − k (every window of a unit j ≥ 2 but that unit's first); litdiff = [literal ≠ 2^(k−1) − k]   must 0
  gloss   line L-3's words «β-ranks by Ξ-depth with ties broken by β-id», read as a definition: br := the rank of the pair
          (−Ξ-depth, β-id) (the local δ of the rule's table dropped). T_gloss = the length of the IDEAL run of that genome;
          glossdiff = [T_gloss = 2^k − 2] must be 0 for the finding to stand (the genome so described is NOT G_k and its run is
          not the theorem's); samebr = [its br equals G_k's] must 0. Second variant «depth, then δ, then β-id» (the rule, entry
          5.1): rulediff = [its br ≠ G_k's] must 0.
Usage: r2add4.py r3 K... | r2add4.py gloss K..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE, os.path.join(HERE, "..", "R2-key"), os.path.join(HERE, "..", "R2-P-N5-END")]
import r2exp as X
import r2unit217 as U
import r2lem as L


def r3(k):
    cx = L.Ctx(k); T = 2 ** k - 2; S, reach = cx.traj(tuple(cx.G["start"]), T + 2); win = bad = lit = 0
    for t in range(1, T + 1):
        for j in range(2, k):
            for a in (0, 1):
                if not (cx.h1(S[t - 1], j, a) and cx.Cb(S[t], j - 1) == 1 - a): continue
                win += 1; last = t + cx.last_off(j); e = cx.Ef[j]
                if any(S[tau][e] != a for tau in range(t - 1, last)) or S[last][e] != 1 - a: bad += 1
                if any(S[tau][e] != a for tau in range(0, t - 1)): lit += 1
    exp = 2 ** (k - 1) - k
    print(f"k {k} T {T} windows2 {win} r3win {bad} literal {lit} expected {exp} litdiff {int(lit != exp)}")


def gloss(k):
    G, names, ix, _ = X.build(k); R = X.rows(k); M = 2 * G["N"]
    dep = [2 * k + 5 if r[6] == "wire" else r[6] for r in R]; dl = [r[7] for r in R]
    def br_of(keyf):
        order = sorted(range(M), key=keyf); br = [0] * M
        for r, b in enumerate(order): br[b] = r
        return br
    g1 = dict(G); g1["br"] = br_of(lambda b: (-dep[b // 2], b))                       # «by Ξ-depth with ties broken by β-id», literally
    g2 = dict(G); g2["br"] = br_of(lambda b: (-dep[b // 2], dl[b // 2][b % 2], b))    # the rule (entry 5.1): depth, δ, β-id
    T1 = len(U.M1P(g1).run(cap=10 ** 6)) - 1
    print(f"k {k} N {G['N']} T_rule {len(U.M1P(G).run(cap=10 ** 6)) - 1} T_gloss {T1} target {2 ** k - 2} glossdiff {int(T1 == 2 ** k - 2)} "
          f"samebr {int(g1['br'] == G['br'])} rulediff {int(g2['br'] != G['br'])}")


if __name__ == "__main__":
    for k in sys.argv[2:]: (r3 if sys.argv[1] == "r3" else gloss)(int(k))
