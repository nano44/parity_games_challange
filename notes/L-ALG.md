# L-ALG notebook (algorithm design loop; lane started 2026-10-15 09:55Z, 12 h box)

## Resume point
- 13:50Z: box deliverables complete (DEAD.md C1-C4, T-ALG1, C5-DTL.md, REPORT-2026-10-15.md); lane idle unless the
  Lead redirects. Everything on claude/l-alg; out/ logs are gitignored (regenerable by the scripts named in the report).
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

## C5-DTL provenance (Lead 12:47Z item 1; recorded 13:05Z)
- Oink clone (tools/oink/src, pinned 8fbf0a7 = upstream master, 322 commits): `git log -- src/solvers/dtl.cpp src/dtl.cpp`:
  e67cb4c 2019-09-14 Tom van Dijk "New experimental solver distraction-free tangle learning"; 7798285 2019-10-27 "New version
  of distraction-free tangle learning."; 2d12471 2019-11-05 "Fix bugs in Distraction-free Tangle Learning"; 0c2fab6 2020-03-27
  "Major update to Oink" (dtl.cpp 891 lines changed); 2024 refactors only. README: 39254fe 2021-06-25 "Updated README.md"
  renames the row to "Distraction-free Tangle Learning (research variant)" and ADDS the line "counter_dtl | Counterexample to
  the DTL solver"; 1ba8b0a 2021-07-02 "Rename the DTL solver": README row becomes "Distance Tangle Learning (research variant
  based on 'good path length')", solvers.cpp registers "distance tangle learning". `git log --all -S counter_dtl` and a search
  of every added file name: NO commit ever contained a counter_dtl source; the README line is the only trace. All commits by
  Tom van Dijk.
- Web (opened 13:00Z): (a) van Dijk, GandALF 2019 talk slides "Fixed-points, Tangles, Distractions in Parity Games"
  (tvandijk.nl/pdf/2019gandalf_talk.pdf, scratchpad dtl/gandalf2019.txt), slide 42: "'Recursive tangle learning' and
  'progressive tangle learning' (unpublished) use this method [play to the best path, not just the best endpoint] to identify
  distractions ... BUT VULNERABLE! (to a different version of the TC game)!"; slide 43: quasi-polynomial algorithms look at
  "how many times alpha dominates beyond this vertex", "Similar to 'distance to opponent region'", "Also a path-progressive
  measure, but stronger". (b) van Dijk, "Avoiding Distractions in Parity Games", ISoLA 2024, LNCS 15221 pp. 330-352, DOI
  10.1007/978-3-031-75380-0_19 (author PDF tvandijk.nl/pdf/2024isola_rtl.pdf, scratchpad dtl/isola2024.txt): defines and
  evaluates rtl and ortl, gives exponential lower bounds for both (its Fig. 6 = counter_ortl, Fig. 7 = tc+), section 4 explains
  the "good path" / progress-measure view of distractions; it does not mention dtl, distance tangle learning or counter_dtl;
  its evaluation runs tl, pp, zlk, fpi, fpj. (c) "Solving Parity Games, Very Slowly" (van Dijk, 2024, Springer chapter
  10.1007/978-3-031-75778-5_21): not opened (paywall); search snippet says the author's work "focused on designing various
  variations of tangle learning and subsequently exploring examples that maximally distract and delay these ... variations".
  Reading: DTL is an unpublished 2019-2021 research variant of van Dijk's; the author's own README asserts a counterexample
  exists; no published definition, no running-time claim, and the author's slides say the path-based variants are vulnerable to
  a modified Two Counters game. The fleet has no published source for DTL beyond the C++; C5-DTL.md transcribes the code.

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
- 12:00-12:20 C4 = tangle learning (Oink tl) on the prefix-max product with the C2 outer fixpoint (c4_product.py): correct on
  all 33 library games, S_2..5, T_1..3 (0-244 tangles), but tc: 131 / 3,070 / 37,372 / 333,132 / 2,493,190 tangles at
  N = 2..10: DEAD (DEAD.md C4). First version without the outer loop was WRONG on 7/30 games: the fixpoint is needed even
  with a complete inner solver (good visits must land on vertices p wins from).
- Oink T_R table (RESULTS.md): T_R hard only for uzlk/fpi/zlkq/qpt/tspm (all already beaten by published families);
  tl/ptl/dtl/spptl/psi/pp linear. Oink-fitness GA (rich pool, 80 gens, pop 40): Oink zlk explodes (308 / 968 / 10,587 at
  n = 66/88/132: Zielonka's known exponential behaviour rediscovered); tl 21/26/77, ptl 29/30/49, spptl 32/35/54, dtl 89/110/92,
  psi 36/59, rtl 71/146 at K = 6/8/12(/16): no blow-up found for the tangle-learning family in the S_2/S_3/tc-core gadget
  space. Calibration run started: pool = whole tc N=2 game as a block (can the GA rediscover tc's hardness for tl?).
  Oink README lists counter_dtl, but no such generator source exists at commit 8fbf0a7.
- 12:30 GA calibration (pool = whole tc N=2 games as blocks, fitness = Oink tl tangles): best 25/38/54/77 at n = 66/88/132/176,
  while tc itself gives tl 126 at n=138 and 510 at n=232: the GA cannot rediscover the two-counter hardness; its silence on
  ptl/spptl/dtl is NOT evidence. The GA is validated only against Zielonka-type recursion (ZP, Oink zlk: it finds x30/tile).
  ptl/spptl on tc: 6/12/20/42/72 and 5/9/14/27/44 tangles at N = 2/3/4/6/8 (polynomial-looking, as Oink's README says).
  Upstream Oink master == pinned 8fbf0a7; no counter_dtl source anywhere (README mention only). ptl_sweep.py running:
  ptl/spptl/tl/dtl on all 13 families, S_s, T_R.
- 12:47-13:50 Lead redirect to DTL: provenance (git + GandALF 2019 slides + ISoLA 2024 paper), C5-DTL.md transcription,
  dtl_check.py (all ok on 67,000+ games with verified strategies), growth sweeps (tangles linear on every family; tc wall
  time ~n^2.5; tc+ N=16 exceeded 900 s). Report finalised; end-of-box message sent.
- 13:56Z Lead: attack DTL with tc variants (rest of box). 14:00-14:40Z:
  - tcvar.py: Python port of tc.cpp, validated (identical tl/dtl/uzlk work at N = 2..6). Knobs tried (tcvar_sweep.py, N = 2..10):
    DOUBLEDISTRACTION (the author's own compile-time variant), lanes of 1-3 extra vertices on the A/B -> input edges (prio 0 or 1),
    2-3 gates in series, Z priority +2/+4 (destroys the counter: tl becomes linear too), T priority 3, high-priority gap 4,
    combinations: DTL stays at exactly 2N+1 tangles on every one (idtl identical); tl stays 2^(N+1)-2 except with zshift.
  - tc_local.py (hill-climb from tc N=3/4, mutations on edges/priorities/owners/splits, fitness = dtl tangles): best 26 (N=3,
    n=70) and 28 (N=4, n=100) vs 7 and 9: a 3x constant, then stalls.
  - tc_template_ga.py (uniform per-bit templates with two extra vertices per bit and a 17-edge menu, fitness = dtl at N=5):
    all three seeds converge to the same family (T<->E1, E2->T, A->E1 with prZ = lopr+2): dtl = 10, 18, 32, 41, 52, 62, 74, 85
    at N = 2..9, i.e. ~10N, LINEAR. Lesson: single-size fitness rewards constants, not growth. Relaunched with a 27-edge menu
    (cross-counter couplings) and growth fitness (work at N=7, tie-break N=7/N=4 ratio): out/tc_template_ga_growth_s1{1,2,3}.log.
  - DTL trace reading (oink --dtl -t -t on tc 2): pruning removes the priority-0 vertices of the odd counter first ("distance 1"),
    then gates/selectors, leaving {Even-1-T, Even-0-H} stable after 5 rounds; one tangle per search; 2 dominions in 5 iterations.
    The pruning is a greatest fixpoint ("p-vertices with a good path, through priorities below their own, to the regions of the
    surviving p-vertices"), computed in <= n rounds: a single weak condition, like psolC's, with tangle learning handling siblings.
- 14:20 growth-fitness template GA seed 13: best family quadratic (11..183 at N = 2..10, ~1.8 N^2); seeds 11/12 pending.
