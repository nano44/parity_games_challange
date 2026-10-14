# L-STRUCT notebook
Overwrite the top sections; append to "Sources opened" and "Dead ends".

## Resume point
2026-10-14 20:10Z: S1 done and refereed (C1 OK, Lemmas 1-3 OK after patches). Lead direction (19:26Z): (a) lower-bound
line is mine, (b) hard SAT cells go to L-COMP, (c) constructions only if the gap at (4,6) or n=5 exceeds 1.
- docs/struct/S2-lower-bound-statement.md: T1 w^X(n,d) ≥ s^X(n,d−2), T2 w^X(n,d) ≥ s^X(⌊n/c⌋,d); sent to the Lead
  20:05Z for L-LIT novelty + REFEREE statement check. Proof work on T1 starts only after the Lead's go.
- Latest data: w^V(4,6) ≤ 11 (checker-verified); s^V(4,6) computing (background: compute.py 4 6 V strong, log
  experiments/weak-sep/out/strong_V_n4_d6.log); weak V (4,6) k=10 search and weak E (4,6) k=12 search under caps.
  Any finished results/automata/*.json must be committed (make_table.py, then verify.sh && git push).
- Probe result: weak separators can have odd simple cycles below the top odd letter (probe_oddcycles.py).

## Queue
1. Lead's go on T1 (after L-LIT/REFEREE); then proof attempt along S2 §4 (even-realisable resistance).
2. L-COMP has the hard cells; cheapest decisive one for T1: weak E (4,6) with ≤ 7 states (SAT refutes T1).
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
| date | idea | obstruction (exact) | instance |
| --- | --- | --- | --- |
| 2026-10-14 | Restriction lemma: "a deterministic weak (n,d)-separator restricted to Σ_{d−2} is a strong (n,d−2)-separator" (would give T1 at once) | weak separators with an odd simple cycle whose maximum is ≤ d−3 exist, even at minimum size, so the restriction keeps an odd cycle and is not strong | (3,6) convention V, k = 6 = w^V(3,6): `experiments/weak-sep/probe_oddcycles.py 3 6 V 6 3` returns a 6-state weak separator with an odd cycle of maximum 3; also (2,6) E with k = 4 and (2,4) V with k = 3 |
