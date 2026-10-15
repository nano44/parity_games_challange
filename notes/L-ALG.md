# L-ALG notebook (algorithm design loop; lane started 2026-10-15 09:55Z, 12 h box)

## Resume point
- C1 DEAD (DEAD.md). Live: C2 = NE'(k) (candidates/C2.md; ne.py --mode h). Hunting NE'(1) failures with walk.py/cross.py
  (out/walk_h_*.log, out/cross_h_*.log); tc growth run out/families_c1_tc_growth.log. See "Log".
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

## Sources opened (this session)
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

## Log (UTC)
- 10:00 read CLAUDE/TARGET/NOW/DECISIONS/RESULTS/RANKING/BARRIERS/A3/TA1; Oink built (setup_oink.sh); branch fast-forwarded to trunk dc8e41b (D5).
- 10:25 C1.md written (pseudocode, soundness sketch, running time n^{O(k)} m) before any test.
- 10:45 ne.py: NE(0) == psolC on all 34 library games; NE(1) solves all 11 psolC-partial library games, strategies verified.
- 10:55 random n=5..12, 2,500 per n, kmax 3: all sound; k=0 on all but a handful, k=1 on the rest (out/random_c1_s1.log).
- 11:00 tc N=2..5: NE(1) complete, verified strategies; time 0.0/0.2/1.9/7.6 s (n = 22/42/68/100).
- 11:20 n=4: all 1,380 psolC-partial games solved by NE(1), strategies verified. tc N=6 solved (27 s); N=8 timeout 120 s.
- 11:40 walk.py (mutation walk inside the psolC-failure region): NE(1) fails at n=7 (10 shrunk instances); NE(2) solves all.
- 12:00 C2 = NE'(k) (recursion on the full product game H, Good sinks only): solves all NE(1) killers at k=1; C2.md written.
- 12:30 walk at base 1: NE(2) fails at n=11 (NE(3) solves; C2(1) solves). C1 recorded DEAD (fixed k). C2(1): no failure yet
  after ~10^6 accepted walk steps (n <= 20) and crossover trials; hunts continue.
