# L-STRUCT notebook
Overwrite the top sections; append to "Sources opened" and "Dead ends".

## Resume point
2026-10-14 22:45Z: SL8 exhaustive test nearly complete (results/sl8/; S3 §4c table). Finding: at minimum size t ≤ 2 (E: ≤ 1); above minimum t reaches 4. Working statement SL8-min (t = 2 at minimum size). Lead approved the proof attempt 21:40Z; proof not started; next: read the rule off the t = 1 rewires at minimum size (E first).
2026-10-14 22:20Z: w^V(4,5) = 10 = s^V(4,5): T3 holds at (4,5) V with equality (SAT + checker, unrefereed).
2026-10-14 22:15Z: S3 §4c written: sub-lemma SL8 (same-states rewiring weak → strong at d ≤ n+1) with probe data (t = 1 rewire in 9/9 instances; naive rule dead). Sent to the Lead; no proof started. Next data step: enumerate ALL t=1 rewires per instance (E first) to read off the rule.
2026-10-14 21:50Z: docs/struct/L4-proof.md written (Claim R transfer + CDFJLP Thm 5.1 ⇒ S(n) = n^{Ω(lg n)}); sent to the Lead for the two referees. Next: T3 via R2 size argument (no sub-lemma yet).
2026-10-14 21:30Z: new cells s^V(4,5) = 10, w^V(4,5) ∈ {9,10} (k=8 refuted, k=9 running: equality here is T3's first real test at n=4), w^V(3,10) = 8 (fixed-n growth 6,7,8 at d = 6,8,10), s^S(3,6) landed.
2026-10-14 ~20:55Z: Lead confirmed L4 first (R1), T3 second (R2). R2 data step done: L5' dead (see Dead ends). Waiting for L-LIT T6 (L4 known or open) before R1. Background (caps): weak/strong V (4,5), weak V (3,10) k=8, strong V (3,8) k=8, weak V (4,6) k=9, weak E (4,6) k=12.
2026-10-14 21:55Z: S2 T1 dead (DE2). S2 patched per REFEREE (T2 n ≥ c; V barrier conditional on L4; algorithmic
quantity w^V(n,n); dead-end automaton committed). S3-statement.md written (diagonal W(n) = w^V(n,n) vs S(n) =
s^V(n,n); T3-neg / T3-pos / L4 / H1) and sent to the Lead for L-LIT + REFEREE. No proof or construction work until
their verdicts. Background (caps): weak V (3,10); weak E (2,12); strong V (3,8); weak V (4,6) k=9; weak E (4,6) k=12.
Any finished results/automata/*.json: make_table.py, then verify.sh && git push.

## Queue
1. Lead's go on S3 (after L-LIT/REFEREE); then: if T3-neg is the line, study why the diagonal shows no gain; if T3-pos, try to generalise the fixed-n witnesses to the diagonal (unlikely per S3 §5).
2. H1 tests at n = 3 (d = 10, 12, 14) are mine (cheap); W(5), S(5) are L-COMP's.
3. Structural study of minimal weak separators that beat s: which odd lassos they tolerate (Q3); try to generalise the
   (2,6) 3-state automaton and the (3,6) V 6-state automaton to a family and compute its size against s.
4. Write proofs of Lemmas 1-3 of S1-statement.md (S1-notes) and send to the REFEREE through the Lead.

## Things only I know
- Conventions matter for small n: EvenCycles over multigraphs (CFGO E ⊆ V×C×V; CDFJLP §5 G_t has several self-loops with
  different even priorities on one vertex, so they use multigraphs too) is strictly larger than over simple graphs.
  s^V(4,4) = 7 < 8 = s^E(4,4): the Parys-Wiącek vertex-priority effect shows up already here.
- The neutral letter 0 of CFGO changes nothing (Lemma 2(b)); the top even letter also seems irrelevant in the data:
  every computed value at odd d equals the value at d+1.
- Encoding trap: with BFS symmetry breaking all states are reachable, so SAT at k does not imply SAT at k+1; the
  search must go upward from k = 1 (or from a proven lower bound) and stop at the first SAT. Also "unreachable states
  padded" is NOT the model: k is the exact number of reachable states.
- UNSAT cost grows ~20x per state at n = 4 (k=7: 6 s, k=8: 118 s, k=9: >1 h); the (W2) rank clauses are the bulk
  (|E(H)|·k²·N per odd graph, N = nk). Ideas not tried: binary ranks, cube-and-conquer on delta(q0,·), clique lower
  bounds from pairwise-inconsistent prefixes, a C++ DFA-identification solver.
- `pkill -f <pattern>` kills the calling shell if the pattern is in its own command line (lost one job that way).

## Sources opened
| source (arXiv id / DOI) | result used (theorem / section) | opened on | note |
| --- | --- | --- | --- |
| arXiv 1807.10546v2 (CDFJLP, SODA 2019) | §2.1 graph conventions (edge priorities, every vertex has a successor, even graph); §3.1 Σ_d, LimsupEven/Odd, EvenCycles/OddCycles; §3.2 safety automata; §3.3 (n,d)-separator vs strong, Prop. 3.1 (C_{n,d}); Prop. 3.2 + proof; §4.1 Thm 4.1 (U_{n,d}); §5 Lemma 5.1, Thm 5.1 (C(⌊lg n⌋+d/2−1, ⌊lg n⌋)), G_t construction (parallel self-loops), remark after Lemma 5.2 on OddCycles; §6 open question | 2026-10-14 | PDF via arxiv.org/pdf; text extracted with pdftotext |
| arXiv 2104.05262v8 (CFGO, LMCS 18(3:29) 2022) | §2.1 graphs E ⊆ Q×C×Q, size = vertices, L(A); Def. 3.3 separating automaton (deterministic, Ω|n ⊆ L(A) ⊆ Ω); Thm 3.4; Thm 4.1; §6 colours [0,d], Parity(d), Lemma 6.1, Thm 6.2 (neutral letter 0), §6.2 trees T ⊂ Z^h and G(T), Lemma 6.8, Thm 6.9, Prop. 6.10 (f), Prop. 6.11 (g) | 2026-10-14 | |
| Colcombet, Fijalkow, FoSSaCS 2019, author PDF www.irif.fr/~colcombe/Publications/FOSSACS19-colcombet-fijalkow.pdf | footnote 5 p.14 ("nothing is known about this notion" = weak separation); Thm 9 / Def. 9 strong only | 2026-10-14 | the arXiv version 1810.05106v2 does not contain the footnote |
| Parys, CSL 2020, LIPIcs.CSL.2020.32 (drops.dagstuhl.de PDF) | p.2 intro sentence on "quasi-polynomial lower bound for the size of a PG separator"; Def. 3.2 (PG separator = weak, strong PG separator); remark after Def. 3.2 | 2026-10-14 | cited in S2 §1 to pre-empt a misreading |
| arXiv 2305.00308v1 (Parys-Wiącek) | p.2 vertex-splitting conversion remark (verbatim in L4-proof.md); p.8 §4 "necessity proof does not apply"; Thm 3.1, recursion (1) for f(n,h) | 2026-10-14 | used for L4 attribution |
| arXiv 1902.07175v3 (Kozachinskiy-Vyalyi) | §1.2-1.3: alphabet {1..n}×{1..d}, separation = reach q_accept, "in time t" definition, qn-time remark (App. A), p.6 "Even super-linear lower bounds ... are not known"; Thm 2 | 2026-10-14 | their intro describes CDFJLP's bound as LimSupEven vs OddCycles (reversed roles); CDFJLP Thm 5.1 is EvenCycles vs LimsupOdd |

## Dead ends
| date | idea | obstruction (exact) | instance |
| --- | --- | --- | --- |
| 2026-10-14 | S2 target T1: w^X(n,d) ≥ s^X(n,d−2) (one tree level is all a weak separator saves) | REFUTED (DE2, REFEREE 92846bf): w(2,10) = 4 < 5 = s(2,8) in E, S, V; s(2,2h) = h+1 grows while w(2,d) = 4 for 7 ≤ d ≤ 12 (V) and d = 8, 10 (E) | L-COMP's 4-state weak (2,10)-separator, l-comp 3e44d2c experiments/sat-hard/results/weak_E_n2_d10_k4.json; my re-check experiments/weak-sep/results/external/lcomp_weak_E_n2_d10_k4.json (checker: no violation in E, S, V; not strong) |
| 2026-10-14 | SL5/SL5' for T3: "at d ≤ n+1 every (minimal) deterministic weak separator is strong / has no reachable odd cycle" (E or V) | false: weak separators with odd cycles exist at d ≤ n+1 in E and V, at minimum size ((2,3) E k=3, (2,3) V k=3, (3,3) V k=5, (3,4) V k=5) and above | probe_oddcycles.py outputs listed in S3 §4c |
| 2026-10-14 | Naive rewiring rule for SL8: smallest-even-letter transition of an odd cycle → self-loop | removes the odd cycles but breaks (W1) in 7 of 8 instances; the SAT-found one-transition rewire uses a different transition or target | probe_rule.py |
| 2026-10-14 | L5' for T3 (R2): "for d ≤ n+1 every lasso word of a reachable odd cycle of a deterministic weak V-separator folds into an odd V-graph with ≤ n vertices" (would make every weak separator at d ≤ n+1 strong) | false at (3,3) V, d = n: the minimal 5-state weak witness has a reachable odd simple cycle whose lasso words need 4 vertices (exact DFS, lasso_analysis.py); weak ≠ strong as objects even when w = s | experiments/weak-sep/results/automata/weak_V_n3_d3.json; table experiments/weak-sep/results/lasso_analysis.md |
| 2026-10-14 | Pruning lemma for T3 at d ≤ n+1: "the even-used transitions of a deterministic weak V-separator contain no odd cycle, so it prunes to a strong one of the same size" | false already at (3,3) V, d = n: a minimal 5-state weak witness has an odd cycle inside its even-used part (wsep/analyze.py live_has_no_odd_cycle = False) although w^V(3,3) = s^V(3,3) = 5; T3 cannot be proved by pruning | experiments/weak-sep/results/automata/weak_V_n3_d3.json |
| 2026-10-14 | Restriction lemma: "a deterministic weak (n,d)-separator restricted to Σ_{d−2} is a strong (n,d−2)-separator" (would give T1 at once) | weak separators with an odd simple cycle whose maximum is ≤ d−3 exist, even at minimum size, so the restriction keeps an odd cycle and is not strong | (3,6) convention V, k = 6 = w^V(3,6): `experiments/weak-sep/probe_oddcycles.py 3 6 V 6 3` returns a 6-state weak separator with an odd cycle of maximum 3; also (2,6) E with k = 4 and (2,4) V with k = 3 |
