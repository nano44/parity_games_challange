# REFEREE notebook
Overwrite the top sections; append to "Sources opened" and "Dead ends".

## Resume point (successor session, 2026-10-14 ~23:50Z)
I am the successor REFEREE (spawned 23:15Z, replacing the session parked at f179ae0). Lead: session_014FBi6o334DvwT5Uw2kDfoN
(send_message, first line "From REFEREE (<UTC from `date -u`>):"). Branch claude/referee, trunk merged in
(origin/claude/vibrant-johnson-nxvvxo). Push only via `scripts/verify.sh && git push -u origin claude/referee`; Oink built with
scripts/setup_oink.sh (~1 min; rebuild after every restart, tools/ is gitignored).
Tasks done: R-L1 (L-LOWER L1 at 8fcc0f2; CHANGES, 9 findings; report 2026-10-14-L1-statement-check.md, pushed 9b01cbb,
reported 23:43Z) and T-A1 first-referee check (L-ATTR TA1-proof.md at d5d6396, then re-checked at 4478b84 per the Lead's 23:42Z retarget;
then SIGNED OK at 57a1515 (signature block at the end of the report, gaps G1-G11); report 2026-10-14-TA1-proof-check.md; tools
ta1check.py, ta1probe.py). R2's report (docs/referee-2/R2-TA1.md) read only after my derivation; it agrees on every point. T-A1 signed OK at l-attr 57a1515 (G11 answer for the CHECKER appended). R-L1b (L-LOWER v2 + Lemma 2.1' + Theorem B at
l-lower b1abae0): CHANGES with one one-line finding; report 2026-10-15-L1b-check.md; tool l1bcheck.py (types over all
one-player Büchi games n <= 4, exhaustive B_1 lower bounds n <= 3, lane witnesses on my quotient). Nothing in flight.
Coming (per the Lead's brief): the L1 proof work / experiments/lower from L-LOWER; SL8-min / T3 from L-STRUCT; second referee
for the L4+T3 package is a SEPARATE session, not me.

## Resume point of the predecessor (kept for the record; HANDOVER, parked 2026-10-14 ~21:50Z on the Lead's instruction; context ~680k)
You are the successor REFEREE. Read CLAUDE.md, TARGET.md (v1.0 frozen), docs/NOW.md (Lead session id; it was
session_014FBi6o334DvwT5Uw2kDfoN), docs/agents/LANE-RESTART.md (the five handover-check questions), docs/referee/README.md,
then every report in docs/referee/ (eight so far). Branch claude/referee; push only via `scripts/verify.sh && git push -u
origin claude/referee`; messages to the Lead with the claude-code-remote send_message tool, first line "From REFEREE
(<UTC time from `date -u`>):" (my own first lines drifted ahead of UTC; use the clock). Build Oink first
(`scripts/setup_oink.sh`, ~1 min) so the gate's smoke step runs; `pip install python-sat` for wsepsat.py.
Last actions: L4 (docs/struct/L4-proof.md) signed OK as FIRST referee at claude/l-struct 50dc28b (referee 9bf5301);
handover written (this commit). No work in flight; nothing routed.

State of every claim I refereed (report file in docs/referee/, verdict, status):
| claim | report | verdict | status |
| --- | --- | --- | --- |
| arXiv 2511.03752 v1 (M2) | 2026-10-14-arxiv-2511.03752.md | BROKEN (Theorem 2 false; cex1, cex2) | M2 closed on trunk; AM1-AM9 faithfulness OK |
| L-COMP PGSolver ports (generators, pgsolver_si.py) | 2026-10-14-pgsolver-ports.md | OK; bare SI loop = PGSolver -dgo -dsd -dlo -dsg | done |
| L-LIT T4 §3(c) lasso observation | 2026-10-14-T4-3c-lasso.md | OK, 3 strengthenings, 1 citation nit | done |
| L-COMP gauntlet bench (experiments/) | 2026-10-14-harness-review.md | CHANGES then OK at l-comp e70a2a9 | landed |
| L-STRUCT S1 C1 (w(2,6)=3<4=s(2,6)) | 2026-10-14-S1-C1-weak-separators.md | OK; side claim BROKEN (= plant P1); Lemma 2(b) CHANGES | findings to L-STRUCT |
| L-STRUCT S2 (T1/T2) + L-COMP T1 refutation | 2026-10-14-S2-statement-check.md | T1 REFUTED at (2,10), verified; T2 CHANGES | findings 1-4 to L-STRUCT |
| L-STRUCT S3 (diagonal, T3, L4, H1) | 2026-10-14-S3-statement-check.md | CHANGES, all applied (a67bd78); delta OK | done; T3 proof not yet seen |
| L-STRUCT L4 proof | 2026-10-14-L4-proof-check.md | CHANGES then OK, first referee, at 50dc28b | awaits SECOND referee |
| L-LOWER L1 statement (SLP model, Lemmas 1.5/1.6/2.1/2.3, Transfers 2.2/2.4, T-L1) | 2026-10-14-L1-statement-check.md | CHANGES (9 findings: d vocabulary, game-class corner, Lemma 2.3 rests on unproved Remark 2.5, cited experiments/lower absent at 8fcc0f2, ω(n) gloss weaker than ω(n), 3 model differences, nits) | findings to L-LOWER via Lead; every re-derived claim holds |
| L-ATTR T-A1 (psolB complete <=> PA**; PA** => psolQ complete; Cor. 1-2, Prop. 3) | 2026-10-14-TA1-proof-check.md | CHANGES (theorem and both proofs hold; at 4478b84 open: F1 misstated, T-A1' needs HKP Thm 4, Büchi recolouring, 'stable' gloss); first referee | SIGNED OK as first referee at l-attr 57a1515 (all findings applied; G1-G11 listed, G10 open as HKP dependency) |
| L-LOWER L1 v2 + Lemma 2.1' + Theorem B (b1abae0) | 2026-10-15-L1b-check.md | CHANGES (findings 1-9 applied; Lemma 2.1' OK; Theorem B OK, Claim 3 misses the case t<t'<a; B_1(1..4) = 0,2,4,6 confirmed independently) | findings to L-LOWER |

## Queue / open items
- L4 second referee (not me; a second, independent referee): the gap list G1-G6 in the L4 report is the checklist. What
  the second referee must re-derive: Lemma L4.1 (a)-(d) (Parys-Wiacek conversion H', words p.w, cycle multisets,
  q1 = delta(q0,1) != bottom via 1.2^w, A' = (Q,q1,delta)), L4.2, the chain in Theorem L4, the constants of L4.3
  (d' = 2 floor(sqrt n /2), a0, b0; the fixed step uses floor >= ceil - 1), L4.4's class (i)-(iii) from S2 §3(c), and the
  black-box use of CDFJLP Thm 5.1 (E convention, non-rejecting states, deterministic ⊆ non-deterministic, binomial form
  needs no side condition). My S3 "delta" section records the alternative split-G_t route, not written up.
- Coming (per the Lead): SL8-t and T3 (S3 §2: w^V(n,d) = s^V(n,d) for 1 <= d <= n+1). For T3: cells I confirmed with my
  own SAT: (1,1), (2,2), (2,3), (3,3), (3,4), (4,4) all w = s; obstruction to "prune the even-used part": the committed
  weak_V_n3_d3.json has an odd cycle among its even-used transitions (my check, S3 delta); route R2's L5' must be about
  all paths P and all foldings (S3 §4b). A (4,5) V or (5,5) V cell with w < s would refute T3; my enumeration is too
  slow for n = 5 (use L-COMP's LRAT-checked cells, then verify any SAT witness with wsepref.py over all graphs).
- Minor, not routed: diff of the PGSolver ports against the real binary with -dgo -dsd -dlo -dsg (owner Q4);
  s^V(4,6) = 10 (L-STRUCT) and w^E(4,6) >= 8 (L-COMP, LRAT) are not re-verified by me.
- Findings I routed whose application I have not seen: S2 findings 1-4, S1 findings 1-3 (Lead said L-STRUCT has them),
  T4 finding 4 (CDFJLP multiplicity wording, to L-LIT), ports cosmetic nits (to L-COMP).

## My tools (docs/referee/scratch/; all throwaway, run with `python3 -I`; every SAT answer is re-checked by brute force)
- aiayn.py: faithful implementation of 2511.03752 Algorithm 1 under all 16 readings of its ambiguities, a min-parity
  Zielonka, .pg read/write with min<->max conversion, random counterexample search. `--pg FILE --trace`, `--all-readings`,
  `--search N`. cex1-/cex2-minparity.pg are the counterexamples (paper's convention); *-maxparity.pg are the twins for
  Oink/PGSolver; *.sol are Oink's verified answers (Even wins all four vertices on both).
- harness_faults.py: four planted-fault solvers (winner swap, strategy leaving region, in-region losing cycle, min-parity
  convention) run through L-COMP's compare.py; needs a checkout of experiments/harness.
- sitest_run.py: execution check of pgsolver_si.py / pgsolver_port.py against Oink (paths point at my scratchpad; adjust).
- wsepref.py: brute-force checker for weak/strong (n,d)-separators (S1 D1-D5) over ALL graphs: conventions V (any small n),
  S (n <= 2 cheap, n = 3 is 7^9), E (n = 2, d = 6 via graphs_E2); prune, cycle_class, accepts_all (W1), rejects_all (W2),
  strong_S2 (S2); CFGO universal-tree recursions f_upper/g_lower. CLI: `witness n conv [strong]`, `json FILE n conv`,
  `utrees`, `k2` (all 531,441 two-state automata, V, n <= 2, d = 6).
- wsepE2.py (d = 6: all 16,777,216 edge-labelled multigraphs on 2 vertices, several automata at once) and wsepE2d.py
  (any d: all (A,B) cross-label-set pairs with saturated same-parity loops; sound by monotonicity of W1/W2).
- wsepsat.py: my own SAT encoding (pysat CaDiCaL 1.5.3; one-hot transitions, closure variables per graph, thermometer
  ranks for W2 and for S2 on all states, no symmetry breaking) over inclusion-maximal even/odd graphs computed by brute
  force (V: one labelling per vertex-permutation orbit; S). `wsepsat.py n d V|S weak|strong k`. Timings: n <= 3 seconds;
  n = 4, d = 4: ~11 min per cell (enumeration dominates), weak k = 6 took 24 min; n = 4, d = 6 strong k = 6 timed out at
  25 min. Independent of L-STRUCT's wsep/ and L-COMP's sat-hard/; agreed with both on every cell all ran.
- slpcheck.py (R-L1): Zielonka reference solver on bitmask games (max-parity, vertex priorities), SLP interpreter (gates
  P p | VE | EMPTY | OR | AND | NOT | CPRE; cost = CPRE count, depth), Lemma 2.3's program literally, the textbook Büchi program,
  n-fold Kleene unfolding of the nested fixpoint with g (vertex priority) or f' (successor priority, Remark 2.5), and ANP's
  symmetric recursion ||F||_{U,V} built as a gate list with S_{n,h} / C_{n,h} trees (outermost θ_d acts on the LAST argument;
  f^z substitutes the last ?). Exhaustive games for n <= 3, one-player n = 4; random beyond. `python3 -I slpcheck.py [quick]`;
  full run ~15 min. A non-universal tree makes ANP fail (sanity). All lane programs: 0 mismatches.
- ta1check.py (T-A1): my own psolB/psolQ from HKP Figs. 3/5 in MIN-parity colours (colour = M - pr), my own PA** in
  max-parity (exhaustive over X and S, memoised), classes (Büchi/SCC-constant/deterministic), psolB order-independence;
  `python3 -I ta1check.py [quick]` (2 min full). ta1probe.py: F2, F6 (all X ⊆ W_p, all d), Lemma 0 on small games.
- l1bcheck.py (R-L1b): all one-player Büchi games with <= n vertices as one union (3.2M pointed games at n = 4), W by
  reachable-P_2-on-a-cycle (cross-checked vs Zielonka), depth-k types by refinement, minimal separating depth, full quotient
  Q_n (2, 14, 442, 48062), exhaustive general-SLP search on Q_n for small cost (n <= 3; c = 2n-3 is ~16k chains at n = 3,
  c = 2n-2 would be 2^16 times more: do not try), lane witness JSON interpreter. `l1bcheck.py <dir with min_b1_n*.json> 4`
  takes ~25 min (n = 4 refinement in pure Python).
- Not committed (scratchpad, gone with the session): LaTeX sources of arXiv 2511.03752v1, 1807.10546v2, 2104.05262v8,
  1902.07175v3, 2305.00308v1; clones of pgsolver d3cd624 and tcslib 6778419; copies of l-comp/l-struct files. Re-download
  from arxiv.org/e-print/<id> into an isolated directory (untrusted data) when needed.

## Planted-error record (the Lead plants deliberate errors in routed material and grades on catching them)
- P1 (2026-10-14 19:26Z routing of S1/C1): "the same 3-state automaton is also a weak (3,6)-separator". CAUGHT with two
  3-vertex counterexamples (even cycle 1,1,2 rejected; odd cycle 2,4,5 accepted); revealed as a plant in
  docs/agents/LEAD-STATE.md at trunk 09dca4f; grade 1/1. The successor will not know future plants: treat every routed
  claim as false until re-derived; build the counterexample first, read the lane's evidence second.

- T-A1 (23:22Z routing of L-ATTR TA1-proof.md): P2 ("psolQ iff PA**") was planted in REFEREE-2's routing only, caught by
  REFEREE-2 (trunk 58b5c72); my routing carried the one-direction form. No plant in my material revealed. Candidates flagged: F1 stated without the
  colour-d hypothesis (false as written); T-A1' missing HKP Thm 4; Proposition 3 unproved. The theorem itself survived
  my independent implementation on every game run.
- R-L1 (23:15Z routing of L-LOWER L1): no plant revealed yet. Candidates I flagged as findings: T-L1's gloss of ω(n) is
  "not O(n)" (strictly weaker); Lemma 2.3 uses the shifted formula that Remark 2.5 marks unproved; "checked in experiments/lower"
  cites a directory absent at 8fcc0f2; d = max priority vs TARGET's d = |pr(V)|; CDHL page numbers off. Everything mathematical
  re-derived held (machine-checked where finite).

## Things only I know
- R-L1b: minimal program depth on one-player Büchi is exactly 2n-2 for n <= 4 (my types), Theorem B gives 2n-1; B_1(4) = 6
  follows from Lemma 2.1' + the lane's witness without any SAT. The exhaustive chain search is fully general for SLPs.
- T-A1: F6's equality MAttr^{G'}(X,d) = MAttr^{W_p(G')}(X,d) holds for EVERY X ⊆ W_p (q keeps the play in W_q), not only
  fatal X; the "only if" needs only W ⊆ R from F1. L1's rank induction has no rank 0 (X external). T-A1' silently needs
  HKP Thm 4. The "if" proof is order-free, so T-A1 holds for psolB under any colour order. HKP Fig. 4(a) edges (from the
  png): v0↔v1, v1↔v2, v2↔v3, v3↔v4, colours 3,2,0,2,3, squares v1, v3. PA ⊆ PA* has no proof anywhere (data only).
- R-L1: ANP's recursion ||F||_{U,V} is straight-line; Lemma 3.6 (worklist) is adaptive; a Jacobi round-robin on Algorithm 1's
  |V| equations is non-adaptive at |V|(1 + n|V|) queries. CDHL's O(1)-bit step for Reduction 3.9 is NOT in their text (they
  say "same argument as Theorem 3.2"); it is one bit per party about the loop at v_max (Pre) / v_min (Post). CDHL printed
  page = physical page − 1. ANP cite Emerson–Jutla 1991 ([10]) for "Expression (1) = winning region". The shifted Büchi
  formula νZ.μY.Cpre((P_2∩Z) ∪ (P_1∩Y)) is correct (rank argument in the report §3) and exhaustively checked for n <= 3.
  The matrix-vector query model (Sun–Woodruff–Yang–Zhang ICALP 2019, arXiv 1906.05736) is the adjacent framework nobody in
  the fleet has opened; with named singleton queries n queries read the adjacency matrix, so ω(n) must come from anonymity.
- 2511.03752 is MIN-parity; PGSolver/Oink are MAX-parity; convert p -> M - p (M even >= max p). On cex1 the max-parity
  reading of the same numbers coincides with the algorithm's wrong output: never check a min-parity run against Oink on
  the unconverted file. The paper's theorem numbers follow a shared counter (Lemma 1 Zielonka, Theorem 2 dominion,
  Lemma 3 minimal dominion, Lemma 4 progress, Theorem 5 correctness); the false sentence is tex:332.
- L-COMP's strategy-improvement port is the bare loop = PGSolver with -dgo -dsd -dlo -dsg (pgsolver.ml:102-116), not the
  default binary with universal_solve preprocessing; any M1 sentence quoting PGSolver counts must say so.
- CDFJLP (1807.10546v2): Thm 5.1 is an E-convention theorem (G_t has one self-loop per even priority at each vertex),
  counts non-rejecting states (tree decomposition on non-rejecting states; leaves inject there), and its binomial form
  comes from Thm 2.3 "for all positive integers" with no side condition; the "d <= n" is only for the closed form. The
  embedding claim (§5) uses only a run on alpha_t avoiding rejecting states plus the tree decomposition from strongness.
  CDFJLP never fixes whether parallel edges may carry distinct priorities (T4 finding 4). CFGO (2104.05262v8): Thm 4.1 =
  saturation.tex thm:main; parity §6 lemma numbering: 6.1 (line 13), Thm 6.2, 6.3 (68), 6.4 (145), 6.5 (165), 6.6 (197),
  6.7 (225), 6.8 (266), Thm 6.9 (287), Prop 6.10 (304), Prop 6.11 (374); universal-tree sizes f = g: (2,3) 4, (2,4) 5,
  (3,3) 7, (4,2) 8, (4,3) 13. KV (1902.07175v3): alphabet (vertex, priority), eventually-always q_accept, graphs = S
  convention, Thm 2 time-bounded.
- S1 Lemma 2(b) repair differs by convention: E = self-loop labelled 2 at the end of the non-zero part; V = fresh vertex
  labelled 2 (a 0-vertex was removed), n >= 2.
- T1 (one tree level) died at (2,10): w = 4 < 5 = s(2,8) in E, S, V (my exhaustive checks); it held at (2,6), (2,8) and
  L-COMP's w^E(4,6) >= 8 supports it there. The weak < strong cells all have d >= n+3.
- The probe automaton that exhibits the restriction dead end for (3,6) V (6 states, odd cycle of maximum 3) is listed in
  the S2 report §5; the committed weak_V_n3_d6.json is NOT such an instance (its restriction to Sigma_4 is strong).
- My timestamps in messages to the Lead ran ahead of UTC (I estimated instead of reading the clock); the SHAs are the
  record. L-STRUCT had the same issue (S3 §5).
- The split-G_t observation (S3 delta, finding 8): one copy per out-letter gives c = d and monotonicity in d then gives
  L4; L-STRUCT used L-LIT's Claim R instead (same bound form). If a self-contained proof is ever wanted, that is the route;
  I did not write it (referees do not write proofs for lanes).

## Sources opened
| source (arXiv id / DOI) | result used (theorem / section) | opened on | note |
| --- | --- | --- | --- |
| arXiv:1405.0386v2 (HKP, Fatal Attractors) | archiv.tex/PDF: §2, Defs 1–8, Thm 1, Thm 2 + proof, Lemma 1, Fig. 3 (tex:728–747), Ex. 5 + Fig. 4(a) png, Def. 6 (tex:942–948), Fig. 5 (tex:970–997), Thm 4 + proof, Thm 5, Thm 6 statement, Thm 7/8 + proofs, Lemma 5 + proof, external-target remark tex:528–536 | 2026-10-14 | T-A1; MIN-parity |
| arXiv:1711.09148v1 (CDHL, SODA 2018) | arxiv.tex: §2 model 466–517 (Thm 2.1 th:lbdisj), Reduction 3.9 red:buchi 759–765, Thm 3.10 thm:buchi 803–814 and proof 1223–1241, Lemma 3.4 lem:scc2 615–665, Prop 4.2 lem:objectives_ub 1023–1044, intro 284–286 ("2n one-step operations"); theorem numbering from the shared counter, confirmed in the PDF | 2026-10-14 | R-L1; LaTeX source + PDF, isolated dir |
| LIPIcs.CSL.2021.9 (ANP, DOI 10.4230/LIPIcs.CSL.2021.9) | §2 (f_{A,B}, trees, Prop 2.5), §3.1 cases (1)–(3), Lemmas 3.1, 3.2, Remark 3.3; §3.2 Algorithm 1, Lemmas 3.4–3.6, Cor 3.7; §3.3; Thm 5.1; Remark 5.5; intro p.9:2–9:3 ([10] Emerson–Jutla for Expression (1) = winning region) | 2026-10-14 | R-L1; DROPS PDF via pdftotext |
| arXiv:2305.00308v1 (Parys–Wiącek) | improved-parity.tex lines 86-87 (edge-to-vertex priority conversion remark), 368 (necessity proof does not apply) | 2026-10-15 | LaTeX source; L4 attribution quotes |
| arXiv:2104.05262v8 (CFGO, LMCS 2022) | preliminaries (graphs, automata, neutral letter), reductions (separating automata, universal graphs), saturation Thm 4.1, parity §6: Lemma 6.1, Thm 6.2, Lemmas 6.4-6.8, Thm 6.9, Props 6.10/6.11 | 2026-10-14 | LaTeX source; S1 conventions and F2 |
| arXiv:1902.07175v3 (Kozachinskiy-Vyalyi) | §1.2 separation approach, §2.1 separation automata and game graphs, Thm 2 | 2026-10-14 | LaTeX source; S1 F5 / Lemma 3 |
| arXiv:1807.10546v2 (Czerwiński et al., universal trees inside separating automata) | the-separation-approach.tex (languages of play encodings; safety automata; (n,d)-separators, strong separators); intro.tex 161-166 (separator) | 2026-10-14 | definitions for the T4 §3(c) check; LaTeX source |
| github.com/tcsprojects/tcslib 6778419 | src/data/tcsgraph.ml 8-226, tcsset.ml 132-166/284-287/426, tcslist.ml 35-42, tcsarray.ml 48-52, tcsbasedata.ml 181-227 | 2026-10-14 | helpers used by stratimpralgs.ml |
| github.com/tcsprojects/pgsolver d3cd624 | solvers/stratimpralgs.ml 54-199, 441-669, 693-696; solvers/switch_globally_best.ml 1-119; paritygame/transformations.ml 271-320, 338-413; paritygame/univsolve.ml 23-66, 267-780; apps/pgsolver/pgsolver.ml 102-116 | 2026-10-14 | strategy improvement originals of pgsolver_si.py |
| github.com/tcsprojects/pgsolver d3cd624 | recursiveladder.ml 13-46; policyiter/generators/switchallexp.ml 30-66, switchbestexp.ml 34-74; policyiter/stratimprgenerators.ml 7-47; paritygame.ml 19, 25-40, 128-139, 175, 201-206, 365-387 | 2026-10-14 | OCaml originals of L-COMP's ports; cloned into scratchpad |
| arXiv:2511.03752v1 | whole paper: Sec. 2 defs, Sec. 3 (A*, A', A^k, Thm 1, Lemma 2, Alg. 1, Lemma 3, Thm 4, 5, 6) | 2026-10-14 | PDF + LaTeX source (main.tex); 4 pages; only v1 exists |

## Dead ends
(none)
