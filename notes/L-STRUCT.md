# L-STRUCT notebook (handover-grade, rewritten 2026-10-14 ~22:00Z UTC; earlier timestamps in messages ran ahead of UTC)
Overwrite the top sections; append to "Sources opened" and "Dead ends".

## Resume point
PARKED (Lead 2026-10-22 13:59Z). Cap reached 2026-10-23 01:30Z; no job running. Outcome of the n = 5 box:
s^V(5,5) >= 11 (LRAT), w^V(5,5) >= 11 (SOLVER-ONLY), strong (5,5) k=11 undecided (ran >= 8h24m from 07:58Z, lost at a
container restart before the cap, no result). T3 at n = 5 untested; a gap needs s >= 12 and a weak 11-state separator.
Checkpoints in out/ (gitignored) may be lost with the container; regenerate with n5.py. Next: the Lead chooses T6, the
n = 2 o(d) family, or a full park.
- Lane files: docs/struct/S1-statement.md (definitions; refereed), S2-lower-bound-statement.md (T1 dead, DE2; T2 parked),
  S3-statement.md (T3 data conjecture), L4-proof.md (RESULTS R1, GAPS G1 closed: signatures 9bf5301, d76c9e1; G-L4-1 =
  CDFJLP Thm 5.1 black box), T3-proof-attempt.md (gaps and dead ends), S4-structure-note.md (facts on data).
- Experiments: experiments/weak-sep/ (README; check.sh is in scripts/verify.sh; results/table.md, results/sl8/,
  results/lasso_analysis.md, results/external/).
- Live conjecture: T3: w^V(n,d) = s^V(n,d) for d ≤ n+1 (data through (4,5) V; also (4,6) V equal, d = n+2).
- n = 5 bounds before this box (L-COMP, experiments/sat-hard/results.md 47-57, LRAT): w^V(5,5) >= 10, s^V(5,5) >= 10
  (>= 11 CEGAR only), s^V(5,6) >= 10; no upper bound.

## Box log 2026-10-22 (date -u)
- 07:34Z P0: strong (5,5) V k=10 UNSAT (30 graphs, 420 s), LRAT VERIFIED (3417924 RUP) -> s^V(5,5) >= 11 (f6ce465).
- Upper side (SAT) is NOT cheap at n = 5: weak (5,6) k=14 needed ~20 min per CEGAR round after 67 rounds (paused,
  checkpoint out/ckpt_weak_V_n5_d6_k14.json: 181+37 graphs); strong (5,6) k=13 stuck > 30 min in round 5 (stopped).
- Pattern in all computed s^V: s^V(n,2h-1) = s^V(n,2h) = n + (h-1)(n-1) (n <= 4, h <= 3; DATA, no proof). Predicts
  s^V(5,5) = s^V(5,6) = 13.
- 09:47Z switched to the LOCKSTEP ladder: once strong UNSAT at k is proved (s >= k+1), weak SAT at k certifies a gap
  by itself (Lemma P), so weak and strong climb together from k = 10: weak (5,5) k=10 running beside strong (5,5) k=11.
- 13:18Z box end: strong (5,5) k=11 still in ONE solve after 5h20m (PID 5687; not resumable, no checkpoint gain);
  weak (5,5) k=10 in round 7 after 3h33m (PID 12501; round 6 took 4255 s; checkpoint out/ckpt_weak_V_n5_d5_k10.json).
  Both left running pending the Lead's decision. Paused: weak (5,6) k=14 checkpoint (181+37 graphs, 67 rounds).
- 13:25Z theory box GO (to ~16:30Z; jobs PIDs 5687/12501 kept until ~01:30Z Oct 23). Output docs/struct/S5-weak-strong.md:
  CDFJLP needs strongness only in Lemma 5.2 (quote); Lemma TD (tree-decomposable <=> strong) PROVED; Prop. W PROVED
  (weak W with U_G(W) odd-cycle-free obeys Thm 5.1's bound) but its hypothesis UG is DEAD on data; same-even-partition
  hypothesis DEAD; Lemma SL (lasso > n) PROVED (elementary); s^V formula: DATA range + false for n >= 2 240 572 at d = n
  by L4 (l4_vs_formula.py). 13:50Z: S5 §8 Lemma CL (EvenCycles_{n,d} is closed, König) => closure DFA is strong and
  huge (c^V(3,6) = 140; closure_dfa.py) and common-suffix fooling sets are void for weak and strong (Remark F); T6 restated.
  13:50Z UG_alpha (runs on the CDFJLP words themselves) DEAD at minimum size too (cf9ec7d). Box ended early 13:55Z:
  T5/T6 are research targets, not box items. Next if woken: T6 (fold numbers of tolerated cycles vs the run structure)
  or a provable o(d) weak family at n = 2 (w^V(2,d): 3 for d = 3..6, 4 for 7..12, >= 5 at d = 14 E; s(2,d) = ceil(d/2)+1).

## Queue
0. At ~01:30Z Oct 23 (Lead cap): stop PIDs 5687, 12501; record bounds + cost obstruction in S3 §2 (LRAT via lrat.sh
   if 5687 ends UNSAT and the proof fits; PID 12501 SAT = gap: report at once with sha1, re-verification, LRAT path).
1. The box above. A gap at d <= n+1: report at once (LRAT path, witness sha1), then lasso_analysis / family (T3-pos).
2. Theory targets after S5: T5 (a thinner universal word family whose runs avoid the tolerated odd cycles) and T6
   (fooling sets with the safety-correct notion, S5 §7). The state-by-state comparison (old item 2) is DONE: DEAD (S5 §4).

## Things only I know
- Timestamps in my messages of 2026-10-14 ran ahead of UTC by up to 90 min until ~20:35Z; SHAs are authoritative.
- 2026-10-22: make_table.py skipped every '_k<j>' file, which hid the exact w^V(4,6) = 10 for a week; it now accepts a
  partial run when k_start <= the monotone lower bound (S1 Lemma 2(a)) and prints it.
- Kill long jobs only by PID file (out/<cell>.pid), never pkill -f. Take the PID from `ps -C python3 -o pid=,args=`
  (pgrep -f matches the calling shell, and `$!` after a chained `... && nohup X &` is the subshell's PID; both bit on 2026-10-22).
- Encoding traps: BFS symmetry breaking forces all states reachable, so search k upward and stop at the first SAT; the
  (W2) rank clauses are the UNSAT bottleneck (~20x per state at n = 4); the rank range N = n·k is needed for completeness.
- Enumeration (enumerate_weak.py) is per BFS numbering, not per isomorphism class (over-counts); fine for existence.
- Convention E = multigraphs is the literature's (CDFJLP §5 G_t has parallel self-loops; CFGO E ⊆ V×C×V); E and S agree
  on every computed cell; V differs (Parys-Wiącek effect, s^V(4,6) = 10 vs 13).
- The neutral letter 0 and the top even letter never changed a value in the data.
- pkill/pgrep -f with a pattern that appears in your own command line kills your shell (lost two jobs that way);
  make_table.py and selfcheck.py skip slow families (S with d ≥ 5, V with d ≥ 9, n ≥ 5, (4, ≥5)) to keep the gate fast.
- L-COMP's independent pipeline (LRAT) agrees with every value it recomputed; the REFEREE's tools reproduced n ≤ 3.
- Lemma 2(b-V) (vertex version of the neutral-letter lemma) is the REFEREE's proof; Claim R (L4.1) is L-LIT's.

## Sources opened
| source (arXiv id / DOI) | result used (theorem / section) | opened on | note |
| --- | --- | --- | --- |
| arXiv 1807.10546v2 (CDFJLP, SODA 2019) | §2.1 graph conventions; §3.1 Σ_d, LimsupEven/Odd, EvenCycles/OddCycles; §3.2 safety automata; §3.3 (n,d)-separator vs strong, Prop. 3.1; Prop. 3.2 + proof; §4.1 Thm 4.1; §5 Lemma 5.1, 5.2 (resistance, tree decomposition Conditions 1-3), 5.3, Claim 5.1, Thm 5.1, G_t and α_t constructions; §6 open question | 2026-10-14 | PDF via arxiv.org/pdf; pdftotext |
| arXiv 2104.05262v8 (CFGO, LMCS 18(3:29) 2022) | §2.1 graphs E ⊆ Q×C×Q; Def. 3.3; Thm 3.4; Thm 4.1; §6 colours [0,d], Lemma 6.1, Thm 6.2, §6.2 trees and G(T), Lemma 6.8, Thm 6.9, Props 6.10/6.11 | 2026-10-14 | |
| Colcombet, Fijalkow, FoSSaCS 2019, author PDF (irif.fr) | footnote 5 p.14 ("nothing is known about this notion"); Def. 9 / Thm 9 strong only | 2026-10-14 | arXiv 1810.05106v2 lacks the footnote |
| Parys, CSL 2020, LIPIcs.CSL.2020.32 | p.2 intro sentence; Def. 3.2 (PG separator weak / strong PG separator); remark after Def. 3.2 | 2026-10-14 | cited in S2 to pre-empt a misreading |
| arXiv 2305.00308v1 (Parys-Wiącek) | p.2 vertex-splitting remark (verbatim in L4-proof.md); p.8 §4 "necessity proof does not apply"; Thm 3.1, recursion (1) | 2026-10-14 | L4 attribution |
| arXiv 1902.07175v3 (Kozachinskiy-Vyalyi) | §1.2-1.3 alphabet, "in time t", qn-time remark (App. A), p.6 quote; Thm 2 | 2026-10-14 | their intro describes CDFJLP's bound with reversed roles |
| arXiv 1807.10546v2 (CDFJLP), re-opened | §5.1 Lemma 5.2 proof (the LimsupOdd sentence, quoted in S5 §1), §5.2 Lemma 5.3, G_t, α_t, Prop. 5.1, Claim 5.1; §6 open question (quoted S5 §0) | 2026-10-22 | arxiv.org/pdf/1807.10546v2, pdftotext; scratch copy not committed |

## Dead ends
| date | idea | obstruction (exact) | instance |
| --- | --- | --- | --- |
| 2026-10-14 | S2 target T1: w^X(n,d) ≥ s^X(n,d−2) | REFUTED (DE2, REFEREE 92846bf): w(2,10) = 4 < 5 = s(2,8) in E, S, V; s(2,2h) = h+1 grows while w(2,d) = 4 for 7 ≤ d ≤ 12 | L-COMP's 4-state weak (2,10)-separator (l-comp 3e44d2c); my re-check experiments/weak-sep/results/external/lcomp_weak_E_n2_d10_k4.json |
| 2026-10-14 | Restriction lemma: a weak (n,d)-separator restricted to Σ_{d−2} is a strong (n,d−2)-separator | weak separators with an odd cycle of maximum ≤ d−3 exist, even at minimum size | results/automata/deadend_restriction_V_n3_d6_k6.json |
| 2026-10-14 | Pruning lemma: the even-used transitions of a weak V-separator contain no odd cycle (d ≤ n+1) | false at (3,3) V, d = n | results/automata/weak_V_n3_d3.json (wsep/analyze.py) |
| 2026-10-14 | L5': at d ≤ n+1 every lasso word of a reachable odd cycle folds into ≤ n vertices (would make weak = strong) | false at (3,3) V: lasso words need 4 vertices | weak_V_n3_d3.json; results/lasso_analysis.md |
| 2026-10-14 | SL5/SL5': at d ≤ n+1 every (minimal) weak separator is strong / has no odd cycle | false in E and V at minimum size | probe_oddcycles.py outputs (S3 §4c) |
| 2026-10-14 | Naive rewiring rule: smallest-even-letter transition of an odd cycle → self-loop | breaks (W1) in 7 of 8 instances | probe_rule.py |
| 2026-10-14 | D-A: every odd simple cycle has an even return edge below its maximum | false for all-odd cycles (odd self-loops); 104/106 hold | V (2,3) k=3, δ = [[1,0,1],[⊥,2,⊥],[2,2,⊥]] (test_lemmas.py) |
| 2026-10-14 | D-C1: rewire target "next state of the cycle or source" | wrong in 42 of 64 working rewires | V (3,3) k=5, δ = [[1,0,1],[2,3,2],[⊥,3,⊥],[4,3,⊥],[2,0,⊥]], δ(4,2): 0 → 3 |
| 2026-10-14 | D-C2: any deterministic target rule (shallowest/deepest interval state, source, successor, predecessor) | none holds on all 57 groups; only NR (necessary) does | same instance, interval {1,3,4}, only 3 works (target_rule2.py) |
| 2026-10-14 | D-HB2: the D-tree of A − τ0 of a minimal weak separator at d ≤ n+1 is (n,⌈d/2⌉)-universal | false on 2/3 (E (2,3)), 8/11 (V (3,3)), 30/42 (V (3,4)); control on strong E witnesses passes | E (2,3) k=3, δ = [[1,0,1],[⊥,2,⊥],[1,0,⊥]], τ0 = (1,2), leaves {(0,0),(1,0)} (test_HB2.py) |
| 2026-10-22 | Same even-prefix partition: every minimal weak W at d ≤ n+1 has a minimal strong S with R(W,S) a bijection | false: 1/16 (V (2,3)), 0/3 (E (2,3)), 1/11 (V (3,3)), 2/42 (V (3,4)) | V (2,3) W = [[1,1,1],[2,1,⊥],[⊥,0,⊥]], least |R| = 5 (prefix_partition.py, results/partition/) |
| 2026-10-22 | UG: the CDFJLP graphs G_t drive no odd cycle of a weak separator (would give Thm 5.1's bound by S5 Prop. W) | false on almost all non-strong weak separators, also at d = n+1 | E (2,4) k=3 δ = [[1,0,1,0],[⊥,2,⊥,0],[1,0,⊥,0]] (ug_test.py) |
