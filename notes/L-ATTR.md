# L-ATTR notebook
Overwrite the top sections; append to "Sources opened" and "Dead ends".

## Resume point
2026-10-14 22:42Z (machine clock; trunk commit 22:05Z). A1 answered: k(psolQ) = k(Alg1) = 0 (docs/attr/A1-results.md). Exhaustive n <= 3 done; n = 4 full
enumeration (27.3 M canonical games, experiments/attr/exhaustive.py 4 --all-strahler) and PA sampling at n = 5 were running
when this was written; their numbers go into A1-results.md section 2-3 (placeholders N4, Q4, W4, S4, B4, H4, N5Q, N5B if
still present means they did not finish). Then: instances/alg1_min_n4_m5.pg from out/fail_n4.jsonl, scripts/verify.sh, push,
message to the Lead (Q1-Q3, T-A1 judgement, NEEDS: L-LIT novelty of T-A1, REFEREE for L1-L4 if the Lead wants it).

## Queue
1. Fill the n = 4 and n = 5 numbers; write instances/alg1_min_n4_m5.pg (minimal m for Alg1 WRONG/stuck at n = 4).
2. verify.sh && push; message the Lead.
3. If the Lead wants T-A1 refereed: write the full proof of L1-L4 (docs/attr/T-A1-proof.md), with L3 stated carefully.
4. Optional: exact class of psolQ (dynamic/peeling version of PA); psolB vs psolQ inclusion on the n = 4 data.

## Things only I know
- Lead correction (22:08Z, read 22:42Z): the brief's sentence "polynomial partial solvers cannot be complete unless ... collapse" is withdrawn; a complete polynomial partial solver would put parity games in P (open, would be an M4 claim). Nothing in docs/attr/ relied on the withdrawn sentence.
- Hand computation BEFORE running code (recorded 22:15Z, statement section 4):
  HKP Fig. 6 in max-parity (bench/hkp_fig6.pg: v0:4 v1:3 v2:1 v3:1 v4:2 v5:3 v6:3 v7:4, all Odd): Even wins all; d = 4:
  A = Attr_E({v0,v7}) = {v0,v5,v6,v7}; G_1 = {v1,v2,v3,v4}; S_1 = {v2,v3,v4} (trap for Odd in G_1, pr <= 2); its
  2-decomposition: A' = Attr_E({v4}) = S_1, l = 0; A_1 = Attr_E(G_1, S_1) = G_1. Tree <<>>, Str_E = 1; W_O empty, Str_O = 1. Str = 1.
  psolQ by hand (min-parity colours 0,1,3,3,2,1,1,0): b=0: X={v0,v7}, A={v5,v6}, X -> {}; b=1: X={v1,v5,v6} -> {v1} -> {};
  b=2: X={v0,v4,v7}: A_0={v5,v6}, A_2={v2..v6}, X -> {v4} -> {}; b=3: X={v1,v2,v3,v5,v6} -> {v1,v2,v3} -> {v1} -> {}. Nothing decided.
  ce1_4v.pg (v0:1 v1:0 v2:2 v3:0, all Odd, Even wins all): d = 2: A = Attr_E({v2}) = {v2}; G_1 = {v0,v1,v3}, S_1 = {v1,v3},
  0-decomposition trivial, A_1 = G_1. Tree <<>>, Str = 1.
  Why psolQ misses Fig. 6 (my reading): the decomposition's second level is a TRAP (S_1 = {v2,v3,v4}, where Odd may stay forever on
  the even cycle v3v4); fatal attraction only knows "force a return to the target", not "or trap the opponent in a sub-dominion
  of the right parity". The vertex v1 (colour 1) is the obstruction: it must be crossed to return from v0/v7 to X but is permitted
  only in layer 0, whose attractor cannot pass the cycle v3v4.
- psolQ pseudocode as implemented (experiments/attr/psolq.py), HKP archiv.tex lines:
  Q1  colours b of the current G in ascending order                       (Fig. 5, tex:986; Thm 5(3) proof tex:1297-1298: loop on b <= |c|)
  Q2    X = {v : c(v) <= b, c(v) % 2 = b % 2}; cache = {}                   (tex:987-988)
  Q3    while X != {} and X != cache: cache = X                              (tex:989-990)
  Q4      W = layeredAttr(G, b % 2, X)                                       (tex:991)
  Q5      if X ⊆ W: decide Attr_{b%2}(G, W) for player b % 2; recurse on G \ Attr_{b%2}(G, W)   (tex:992)
  Q6      else X = X ∩ W                                                     (tex:993)
  Q7  return G                                                               (tex:996)
  L1  layeredAttr(G, p, X): A = {}; b = max c(X)                              (tex:970-972)
  L2    for d = p, p+2, ..., b: Y = {v in X : c(v) <= d}; A = PMAttr_p(A ∪ Y, d)   (tex:973-977)
  P1  PMpred_p(Z, T, d) = {v in V_p : (c(v) >= d or v in T) and v.E ∩ (Z ∪ T) != {}}
                        ∪ {v in V_{1-p} : (c(v) >= d or v in T) and v.E ⊆ Z ∪ T}   (Def. 6 eq. (5), tex:942-947)
  P2  PMAttr_p(T, d) = mu Z. PMpred_p(Z, T, d), target T external                    (Def. 6 eq. (6), tex:948; tex:532-535)
  S   strategy (mine, D3b): witness successor recorded when v enters PMAttr; attractor strategy on Attr(W) \ W.
  Attr_p(G, X) = Def. 1 (tex:407-418), standard attractor, X included.
- Strahler DP (strahler.py): f(R, d, p) for a p-trap R (subgame) with pr(R) <= d, d of p's parity: A = Attr_p(R, pr^{-1}(d));
  R_1 = R \ A; chain state (remaining set, current max m, count flag) -> minimal final Strahler; a step picks a non-empty
  opponent-trap S ⊆ remaining with pr(S) <= d-2 and f(S, d-2, p) finite, removes Attr_p(remaining, S). Final: 1 if no child,
  m if the max is unique, m+1 otherwise. Children never benefit from non-minimal decompositions (the tree rule is monotone).

## Sources opened
| source (arXiv id / DOI) | result used (theorem / section) | opened on | note |
| --- | --- | --- | --- |
| arXiv 2003.08627 v2 (DJT, e-print LaTeX; tuning.tex, coda.tex, prelude.tex, ballade.tex) | section 2 definitions (attractor decomposition, tree, Strahler number of tree/decomposition/game); Prop. 1, Thm 2, Prop. 3, Prop. 4; Lemma 7, Thm 8 (Strahler = Lehtinen number); Thm 32 (n^{O(1)} (d/2k)^k), Remark 33 | 2026-10-14 | max-parity ("even cycle" = highest priority even); shared counter, numbering checked against the source order |
| arXiv 1405.0386 v2 (HKP, e-print LaTeX archiv.tex) | Defs 1-7, Fig. 2 (psol), Fig. 3 (psolB), Fig. 5 (layeredAttr, psolQ), Thm 2 (fatal attractor winning), Thm 4 (layered fatal attractor winning, strategy by rank (d,i)), Thm 5 (complexity), Thm 6 (psolB order-independence), Thm 7 (Büchi), Thm 8 (SCC-constant colour), Lemma 5 (deterministic games), Ex. 5-6, Fig. 4(a)(b), Fig. 6 | 2026-10-14 | MIN-parity (tex:366-367); title "Fatal Attractors in Parity Games: Building Blocks for Partial Solvers" |
| arXiv 2511.03752 v1 (AVH, e-print main.tex sha256 9840db37...3f8b) | Algorithm 1 (main.tex:370-395) only, as the object implemented in experiments/m2/avh.py per notes/L-COMP.md "M2 pseudocode" (REFEREE: faithful) | 2026-10-14 | not re-refereed here |

## Dead ends
- 2026-10-14 22:25Z. "Strahler threshold k >= 1 for psolQ / Algorithm 1 of 2511.03752" (L-LIT rank-3 first problem as posed):
  dead, k = 0 for both. Instances: HKP Fig. 6 (Str 1, psolQ untouched; bench/hkp_fig6.pg); experiments/attr/instances/psolq_min_n3_m4.pg
  (n = 3, m = 4, Str 1, psolQ/psolB/psol undecided; exhaustive n <= 2 all solved); experiments/m2/counterexamples/ce1_4v.pg
  (n = 4, Str 1, Alg1 WRONG; exhaustive n <= 3: Alg1 regions always right). Obstruction: the solvers certify only forced returns
  to a target; a decomposition whose sub-trap and top attractor escape into each other (mutual escape) has no fatal attractor.
- 2026-10-14 22:35Z. PB ("S_i a trap in R \ A") as the completeness condition: dead, 44 counterexamples at n = 3
  (e.g. instances/psolq_min_n3_m4.pg satisfies PB). PD (acyclic piece-escape graph): dead, 8 counterexamples at n = 3:
  parity 2; 0 1 0 0,1; 1 5 1 2; 2 2 0 0 (v1 owned by Odd; A = {v1} is a sink of the escape graph, yet Odd cannot force a return
  to v1 and the return path from v1 to v0 crosses priority 2, excluded from v0's layer).
