# L-ATTR notebook
Overwrite the top sections; append to "Sources opened" and "Dead ends".

## Resume point
2026-10-15 08:20Z. Task A3-psolC (Lead 08:00Z, 6 h box to 14:00Z): psolC (HKP DTR15-4 Fig. 5) implemented in
experiments/attr/psolc.py, line map docs/attr/psolC-impl.md (ambiguity A1: start colour, literal reading used), validation
a3_validate.py PASS (DTR Ex. 1-3, Fig. 8). Running: a3_exhaustive.py 4 (out/a3_log_n4.txt, ~35 min), a3_families.py
(out/a3_families_log.txt), random runs done (out/a3_random_*.txt). Then: docs/attr/A3-psolC-results.md, push, message.
Findings so far: psolC solves ALL canonical n <= 3 games (psolQ misses 44); Thm 4 per node holds everywhere; smallest
psolC-partial game n = 4, m = 6 (prio [1,2,1,5], all Even, v0->v0,v1; v1->v2; v2->v2,v3; v3->v0; Odd wins all): the
weak-parity prefix minimum is spoiled by the even colour at v1 before Even parks on the v2 loop. tc: 0 % decided at all sizes.

## Queue
2. Answer referee questions on TA1-proof.md; G3 (F6 equality) and G2 (external target, rank of X-vertices) are the ones I
   would probe first.
3. Not done, optional: a solver-free polynomial decision procedure for PA** (the canonical rule greedy2 is sound but misses
   48 of 41,440 n=3 games); exact class of psolQ.

## Things only I know
- R2's n = 2 witness of "psolQ-complete does not imply PA**": 0 0 1 0,1; 1 2 0 0 (Even wins both; psolB stuck, psolQ solves at b = 2 via the permissive layer). psolQ's class is strictly larger than PA** already at n = 2.
- Lead decisions 2026-10-14 23:00Z (quoted): "1. T-A1: before paying for a proof, L-LIT checks novelty and whether PA is decidable
  in polynomial time (T8). Do not start the proof yet. If T8 says NEW and the value holds, I'll give you the go. 2. The 51 MB n=4
  jsonl stays gitignored. Record in experiments/attr/README.md the exact command that regenerates it (27 min), plus a sha256 of
  the file. 3. I've added your Alg1-vs-psolQ data to docs/decisions/M2-arxiv-2511.03752.md. The avh.py strategy finding goes to
  L-COMP's successor. 4. Until T8 lands, make notes/L-ATTR.md handover-grade, push, message me the SHA, and park."
- How to rerun everything (all from experiments/attr/): validate.py (2 min, full), exhaustive.py 3 --all-strahler (3 s),
  exhaustive.py 4 --workers 3 --all-strahler (27 min, 3 cores), hypotheses.py 3 (8 s; PD is slow from n = 5 on, use pa_sample.py
  for PA alone), pa_sample.py n K seed. Oink is needed only by scripts/verify.sh (setup_oink.sh, ~1 min).
- Conventions that bit me: HKP are MIN-parity, DJT and TARGET MAX-parity; all my code converts at the boundary (colour = M - pr).
  PMAttr's target is external (a target node is in the attractor only if attracted in >= 1 step); in the worklist implementation
  every node of Z ∪ T is popped exactly once, so opponent counters count all alive successors. DJT's trap: the opponent's
  vertices keep ALL edges inside, the owner's keep ONE (direction matters in is_trap_for_opponent).
- The machine clock was ~1 h behind what the Lead's message times suggested at first; all my timestamps are machine clock
  (trunk commit 209865a = 22:05Z).
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
| Imperial DTR 2015/4 (HKP, "Static analysis of parity games: alternating reachability under parity"; DTR15-4.pdf sha256 a7b61fe3...9cd6; = LNCS 9560 pp. 159-177 per L-LIT T11, unverified) | Def. 1 (reachability under parity, p.4), Def. 2 (G^p_X, p.5), Thm 1 (p.6), Cor. 1, Lemma 2-3 (p.7), Fig. 5 psolC (p.9), Thm 2 (p.8), Thm 3 (p.9), Ex. 2-3 and Fig. 4, 6 (pp.8-11), Fig. 7-8 and Thm 4 (p.12), section 6 experiments | 2026-10-15 | min-parity; figures read from rendered pages; Example 3 step (ii) contradicts Def. 1's inclusion of the start colour (psolC-impl.md A1) |
| arXiv 2511.03752 v1 (AVH, e-print main.tex sha256 9840db37...3f8b) | Algorithm 1 (main.tex:370-395) only, as the object implemented in experiments/m2/avh.py per notes/L-COMP.md "M2 pseudocode" (REFEREE: faithful) | 2026-10-14 | not re-refereed here |

## Dead ends
- 2026-10-14 23:25Z. Canonical polynomial rules: greedy (largest admissible trap first) for PA*: sound, misses 4,266 of 41,440 at n=3 (e.g. 0 3 0 0; 1 4 0 0; 2 1 0 0,2: the largest trap {v0,v2} is not PA*-peelable, {v0} then {v2} is). greedy2 (largest self-returning top set, else bottom SCCs of the largest trap) for PA**: sound, misses 48 at n=3 (e.g. results/pa2_n3.txt). Decidability of PA** in polynomial time therefore rests on T-A1 (run psolB), not on a solver-free rule.
- 2026-10-14 23:20Z. PA as the class containing HKP Thm 7/8: dead (L-LIT witness instances/llit_witness_buchi_n3.pg). PA* as the class containing Thm 8: dead (witness 0 3 0 0; 1 1 0 0; 2 1 0 0,2).
- 2026-10-14 22:25Z. "Strahler threshold k >= 1 for psolQ / Algorithm 1 of 2511.03752" (L-LIT rank-3 first problem as posed):
  dead, k = 0 for both. Instances: HKP Fig. 6 (Str 1, psolQ untouched; bench/hkp_fig6.pg); experiments/attr/instances/psolq_min_n3_m4.pg
  (n = 3, m = 4, Str 1, psolQ/psolB/psol undecided; exhaustive n <= 2 all solved); experiments/m2/counterexamples/ce1_4v.pg
  (n = 4, Str 1, Alg1 WRONG; exhaustive n <= 3: Alg1 regions always right). Obstruction: the solvers certify only forced returns
  to a target; a decomposition whose sub-trap and top attractor escape into each other (mutual escape) has no fatal attractor.
- 2026-10-14 22:35Z. PB ("S_i a trap in R \ A") as the completeness condition: dead, 44 counterexamples at n = 3
  (e.g. instances/psolq_min_n3_m4.pg satisfies PB). PD (acyclic piece-escape graph): dead, 8 counterexamples at n = 3:
  parity 2; 0 1 0 0,1; 1 5 1 2; 2 2 0 0 (v1 owned by Odd; A = {v1} is a sink of the escape graph, yet Odd cannot force a return
  to v1 and the return path from v1 to v0 crosses priority 2, excluded from v0's layer).
