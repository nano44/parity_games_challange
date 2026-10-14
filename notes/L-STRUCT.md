# L-STRUCT notebook (handover-grade, rewritten 2026-10-14 ~22:00Z UTC; earlier timestamps in messages ran ahead of UTC)
Overwrite the top sections; append to "Sources opened" and "Dead ends".

## Resume point
PARKED by the Lead (21:59Z, option 1). Branch claude/l-struct; all work pushed. The Lead wakes this lane if the n = 5
diagonal cells (w^V(5,5), s^V(5,5), (5,6); L-COMP's successor) show a gap (then T3-pos, constructions) or if a new proof
idea for T3 appears.
- Lane files: docs/struct/S1-statement.md (definitions; refereed), S2-lower-bound-statement.md (T1 dead, DE2; T2 parked),
  S3-statement.md (T3 parked, data conjecture; H1/H2 hypotheses), L4-proof.md (signed by first referee 9bf5301; second
  referee pending with T3), T3-proof-attempt.md (record of gaps and dead ends), S4-structure-note.md (facts on data).
- Experiments: experiments/weak-sep/ (README has the how-to; check.sh is in scripts/verify.sh; results/table.md,
  results/sl8/, results/lasso_analysis.md, results/external/ (L-COMP's (2,10) witness re-checked)).
- Live conjecture: T3: w^V(n,d) = s^V(n,d) for d ≤ n+1 (data through (4,5) V; REFEREE-checked statement; NEW per L-LIT).
  Supporting unproved facts: S4 F7-F9. Refuted routes: notebook Dead ends.

## Queue (if woken)
1. If a diagonal gap at n = 5 appears: analyse the witness with lasso_analysis.py / probe_rules_min.py style tools;
   try to generalise it into a family (T3-pos route); S3 §2 has the consequence for algorithms.
2. If T3 is to be attacked again: the open core is a SIZE argument; both "rewire to strong" (needs a target rule; none
   deterministic, F9) and "hidden universal tree" (F10, false) are dead. An untried idea: compare the weak separator with
   the minimal STRONG one found by the solver on the same cell state-by-state (bisimulation up to even-realisable words)
   to see whether minimal weak and strong separators are always related by a bijection of states.
3. Second referee for L4 (+ T3 package) when the Lead schedules it; L4-proof.md is ready.

## Things only I know
- Timestamps in my messages of 2026-10-14 ran ahead of UTC by up to 90 min until ~20:35Z; SHAs are authoritative.
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
