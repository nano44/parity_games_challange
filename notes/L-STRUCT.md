# L-STRUCT notebook
Overwrite the top sections; append to "Sources opened" and "Dead ends".

## Resume point
2026-10-14: task S1 steps 1-2 done, step 3 (direction) awaiting the Lead's answer to my report.
- docs/struct/S1-statement.md: definitions (conventions E/S/V), facts F1-F5 with sources, lemmas 1-3 (sketched, not
  refereed), questions Q1-Q3, candidate theorems S1-A (M4 route) / S1-B (barrier).
- experiments/weak-sep/: SAT computation; results/table.md; check.sh is in scripts/verify.sh.
- Finding (data, not a result): w < s at (2,5),(2,6) [E,S,V] and (3,5),(3,6) [V]; w = s elsewhere computed.
- Open cells: (4,5),(4,6) all conventions, n = 5 beyond d = 2 (E) / 2 (V): UNSAT side too slow (see README timings).
  Background jobs may still be running: compute.py 4 6 E weak --k-start 12; compute.py 5 3 E weak; S (3,5),(3,6).

## Queue
1. Lead's direction (construct vs lower bound). My proposal is in the report (notes below).
2. If engineering goes to L-COMP: spec = README "Re-run" + encode.py docstring; the hard cells are (4,5),(4,6),(5,>=3).
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
| arXiv 1902.07175v3 (Kozachinskiy-Vyalyi) | §1.2-1.3: alphabet {1..n}×{1..d}, separation = reach q_accept, "in time t" definition, qn-time remark (App. A), p.6 "Even super-linear lower bounds ... are not known"; Thm 2 | 2026-10-14 | their intro describes CDFJLP's bound as LimSupEven vs OddCycles (reversed roles); CDFJLP Thm 5.1 is EvenCycles vs LimsupOdd |

## Dead ends
(none yet)
