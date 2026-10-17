"""L-ALG (produced on Opus 5.5, 2026-10-16 box 4), GAP-A-M §18h. On ACTUAL A_DTL runs: for consecutive calls at one context
(T ⊆ T') and EVERY round r whose input V is the same in both calls, compare the region vectors on V (Lemma R): equal, or
carry at index k. For carries: does some later region (same top) lose vertices (a STEAL), does the union U shrink
(U(T) ⊄ U(T')), do survivors shrink (S(T) ⊄ S(T'))? (dtl_lexcounter.py shows all three on synthetic genuine tangles.)
Usage: DTL_ORDER=oink dtl_steal.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import dtl_regvec as RV, dtl_ideal as I, pg

if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    tot = {}; ex = []
    def inc(k): tot[k] = tot.get(k, 0) + 1
    for f in sys.argv[1:]:
        g = pg.read(f); d = RV.build(g); d.run(); name = os.path.basename(f)
        for key, occ in d.calls.items():
            p, R = key[0], set(key[1])
            for (s1, r1, v1, h1, t1), (s2, r2, v2, h2, t2) in zip(occ, occ[1:]):
                for r in range(min(len(r1), len(r2))):
                    if r1[r] != r2[r] or not r1[r]: continue
                    if r >= len(v1) or r >= len(v2): continue
                    A, B = v1[r], v2[r]
                    if A == B: inc("rounds_equal_regions"); continue
                    inc("carry_rounds")
                    ra = dict(A); rb = dict(B)
                    steal = any(t in rb and not ra[t] <= rb[t] for t in ra) or any(t not in rb for t in ra)
                    UA = set().union(*ra.values()); UB = set().union(*rb.values())
                    inc("steal" if steal else "no_steal"); inc("U_shrinks" if not UA <= UB else "U_grows_or_eq")
                    V = r1[r]
                    SA = I.survivors(d, p, V, R, UA, t1); SB = I.survivors(d, p, V, R, UB, t2)
                    inc("S_shrinks" if not SA <= SB else "S_mono")
                    if (not UA <= UB or not SA <= SB) and len(ex) < 5: ex.append((name, len(R), s1, s2, r))
    print(os.environ.get("DTL_ORDER", "stable"), tot); print("examples", ex)
