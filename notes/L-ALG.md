# L-ALG notebook (algorithm design loop; lane started 2026-10-15 09:55Z, 12 h box)

## Resume point
- C1, C2, C3 DEAD (DEAD.md). T-ALG1 deferred by the Lead (11:20Z). Next: design C4 against the two obstructions (register depth;
  partial-solver blindness composes). Lead rulings 11:20Z: ZP no gauntlet; T-ALG1 deferred; GA instances go to L-SI (keep pushing them).
- Lead session for messages: session_014FBi6o334DvwT5Uw2kDfoN. Branch claude/l-alg. Push: scripts/verify.sh && git push -u origin claude/l-alg.

## Brief (Lead, 2026-10-15 09:55Z, quoted in substance)
Aim M4 / M4-R (TARGET.md section 2 / 4b). Falsification-driven loop: exact pseudocode + running-time argument before any
test (docs/alg/candidates/C<k>.md); implement in experiments/alg/ with positional strategies verified by harness verify.py;
falsify cheapest first: (a) instance library, (b) all n <= 3 and the exhaustive n = 4 corpus, (c) random n = 5..12,
(d) 13 M1 families at growing size with runtime growth. Dead candidates to docs/alg/DEAD.md with the smallest failing
instance and the exact obstruction. A candidate passing (a)-(d): STOP and message the Lead (gauntlet steps 2-5 are not mine).
D5 (owner, verbatim in docs/DECISIONS.md): M4 is the primary aim; D1 unchanged: every claim is wrong until it passes the gauntlet.

## Queue
1. C1 steps (b) n = 4 psolC-partial list (1,380 games), (c) random, (d) families: smallest k per family and size; time growth.
2. If some fixed k survives everything: stop, message the Lead; the completeness proof is the open question (say so).
3. Else: record in DEAD.md the instance with the largest needed k / the family where k grows; design C2 against it.

## Conjecture T-ALG1 (data, 10:25Z; not a claim)
NE'(k) (C2) decides every vertex of every parity game of Strahler number <= k + 1 (DJT 2003.08627v2 p.5 definition:
the maximum over the two players of the smallest Strahler number of an attractor decomposition of that player's largest
dominion). k = 0: psolC is complete on Strahler-1 games. Evidence: every psolC failure found (1,389) has Str = 2, every
NE'(1) failure found (45) has Str = 3; strtest.py (walk, Str computed per game) running. Consequence if true: NE'(floor(lg n))
is complete (Prop. 3: Str <= floor(lg n) + 1) in time n^{O(log n)}: quasi-polynomial, no better than known (Thm 32);
the fixed-k candidates C1, C2 are incomplete for every k (games of Strahler k+2 exist for every k: perfect binary trees of
decompositions). Reading: the nesting depth of prefix-maximum memories IS the register number (DJT Thm 8 = Lehtinen 2018):
each level of NE' adds one register. This is the exact obstruction of the whole fatal-attractor nesting family.

## Sources opened (this session)
- Daviaud, Jurdzinski, Thejaswini, "The Strahler number of a parity game", arXiv 2003.08627v2 (ICALP 2020), opened 10:23Z
  (pdftotext of the arXiv PDF, scratchpad djt/djt.txt): p.4-5 definitions (attractor decomposition, tree, Strahler number of
  a tree and of a game), Proposition 3 (Str(T) <= h and <= floor(lg n) + 1 for (n,h)-small trees), Lemma 7 + Theorem 8
  (Strahler number = Lehtinen (defensive) register number), Theorem 32 (algorithm n^{O(1)} (d/2k)^k for Strahler k).
  Strahler numbers here are computed with L-ATTR's experiments/attr/strahler.py (DP over subsets; A1 validated it against
  brute force over all decompositions on small games, per experiments/attr/README.md).
- Huth, Kuo, Piterman, "Static analysis of parity games: alternating reachability under parity", Imperial DTR 2015/4
  (LNCS 9560 pp. 159-177, DOI 10.1007/978-3-319-27810-0_8): NOT re-opened by me; used through L-ATTR's implementation
  experiments/attr/psolc.py (REFEREE-checked FAITHFUL, referee 1600917) and docs/attr/A3-psolC-results.md section 1
  (Def. 1-2, Thm 1-2, Fig. 5). NE(0) is cross-checked against psolc.py on every test game instead of against the text.
- No other external source cited so far. (Barrier reading in C1.md section 4 is against docs/lit/BARRIERS.md, a fleet
  document, not a source; L-LIT signs off barrier statements.)

## Things only I know
- A decided region of NE(k) (and of psolC) is NOT closed in general: p's winning plays from the greatest fixpoint X may run
  through undecided vertices (the product attractor and the escape tails). Decisions stay sound (p wins from each decided
  vertex; the remainder A \ Attr_p(X) is a p-trap, so q's later decisions transfer; p's later decisions transfer because
  the strategies from decided vertices win from scratch). Consequence: positional strategies are extracted on each
  player's FINAL region (closed when the game is solved), not per decision. psolc.py's per-decision Zielonka fallback
  asserts closure; it never fired on L-ATTR's runs because they produced strategies only on completely solved games.
- Implementation trap caught by verify.py: the start vertex x of a segment must not count as a "later visit to X"
  (DTR Def. 1 says later); with the start counted, every p-parity vertex is trivially in W and the solver is UNSOUND.
  ne.py uses a START marker (as psolc.py uses ⊥).
- Random games (gen.py mix) almost never need k >= 1 (psolC solves 99.9 %); the informative tests are the n = 4
  psolC-partial list and the families tc, tc+, counter_symsi, counter_rr.

## Dead ends (lane-level; the fleet list is docs/alg/DEAD.md)
- C1 NE(k): k = 1 dies at n = 7 (c1_k1_min_n7_m10.pg), k = 2 at n = 11 (c1_k2_min_n11_m15.pg); obstruction: BOT sink = bad visit treated as loss. See DEAD.md.
- C2 NE'(k): dies on the sibling-trap family S_s (strfam.py): NE'(k) solves S_s iff k >= s-1; depth = Strahler number = registers. DEAD.md.

## Log (UTC; clock checked with `date -u`: box start 09:55Z)
- 09:55-10:00 read CLAUDE/TARGET/NOW/DECISIONS/RESULTS/RANKING/BARRIERS/A3/TA1; Oink built; branch fast-forwarded to trunk dc8e41b (D5).
- 09:59 C1.md written (pseudocode, soundness sketch, running time n^{O(k)} m) before any test.
- 10:02 ne.py: NE(0) == psolC on all 34 library games; NE(1) solves all 11 psolC-partial library games, strategies verified.
  Random n=5..12, 2,500 per n: all sound; k=0 on all but 4 games, k=1 on those (out/random_c1_s1.log).
- 10:05 n=4 list regenerated (1,380 psolC-partial games, 518 s, agrees with A3's count); all solved by NE(1), strategies verified.
  tc N=2..6: NE(1) complete, strategies verified; 0.0/0.2/1.9/7.6/26.9 s at n=22/42/68/100/138; N=8 > 120 s.
- 10:09 walk.py (mutation walk inside the psolC-failure region): NE(1) fails at n=7 (10 shrunk instances); NE(2) solves all.
- 10:12 C2 = NE'(k) (recursion on the full product game H, Good sinks only): solves all NE(1) killers at k=1; C2.md written.
- 10:17 walk at base 1: NE(2) fails at n=11 (NE(3) solves; C2(1) solves). C1 recorded DEAD (fixed k). Pushed 9eaa870.
- 10:19 cross.py (glue two NE(1) killers, mutate, shrink): 45 distinct NE'(1) failures, n=10..15; NE'(2) solves all tested.
- 10:22 Strahler numbers (experiments/attr/strahler.py): ALL 1,380 + 9 psolC failures have Str = 2 (none with Str 1);
  all 45 NE'(1) failures have Str = 3; C1 killers (k=1 and k=2) have Str = 2. No n=4 game has Str 3 (A3 summary: 26,632,540
  with Str 1, 698,660 with Str 2). Conjecture T-ALG1 below. Source DJT opened (scratchpad, arXiv 2003.08627v2).
- 10:31 strtest: 84,571 Strahler-2 games (walk, two seeds, n <= 11), all solved by NE'(1), none by psolC. tc N=8: NE(1) 365 s (n=232).
- 10:33 T-ALG1.md: proof that psolC is complete on Strahler-1 games (chain decompositions: every opponent exit goes upward into
  a region whose top even priority dominates the segment). Sharp: Strahler-2 killer n=4.
- 10:35 strfam.py: sibling-trap family S_s (n = 3*2^(s-1)-2, Strahler s): NE'(k) solves S_s iff k >= s-1 for s <= 4 (S_4 n=22:
  NE'(2) nothing, NE'(3) 13 s); S_5 (n=46) running. C2 recorded DEAD with the family. check.sh extended (13 s).
- 10:40 C3 = ZP (Zielonka + psolC pruning at every call; zp.py, C3.md): == Zielonka with verified strategies on 107 library/instance
  games and the 1,380 n=4 games. Families: tc N=2..14: 5 calls at every size (plain Zielonka 65 -> 140,699); counter_dp/m/core:
  1 call (psolC solves the whole game). Hill-climb for call growth at n <= 12: best calls ~ n-1 (linear). Larger searches running.
- 10:45-11:05 C3 ZP on families: tc N<=14, tc+ N<=12: 5 calls at every size; counter_dp/m/core/rob: 1 call (psolC solves);
  plain Zielonka exponential on all of them. ZP call-count searches: hill-climb at n<=12 and n<=60: ~linear (weak);
  block-structured random games (K copies of S_2, shifted priorities, random inter-block edges): max calls 248 at K=13,
  936 at K=23; GA over block genomes (zp_ga.py): best calls 129/247/659/1485+ at K=6/8/10/12 (n=4K), and 6248+ at K=16
  when seeded with two tiled copies of the K=8 best (zp_ga.py --double). Exponent between successive points rises
  (~2.3 -> ~4.8): superpolynomial-looking, not a proof; no explicit family extracted yet (genomes look unstructured).
- 11:00 S_5 (n=46): NE'(3) did not finish in 1700 s (Python); the S_4 point stands as the measured limit for C2.
- 11:17 interim message to the Lead (a5164a4): ZP passes (a)-(d) as data, running time unproven, GA growth. Lead 11:20Z: wait, no
  gauntlet; T-ALG1 deferred; state the register obstruction citably (done, DEAD.md); GA instances to L-SI.
- 11:45 explicit ZP killer: tiling the GA K=8 unit (zp_ladder2.py template search, zp_curve.py): 247 / 7,273 / 234,133 calls at
  R = 1/2/3 tiles (n = 32/64/96), x30 per tile; second unit (K=10) 659 / 10,795 / 132,507. GA table to n=64: 12,255 calls.
  C3 recorded DEAD. R=4 (n=128) running.

