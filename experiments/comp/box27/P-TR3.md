# Packet P-TR3 (L-COMP box 27): T^R(3) ≤ 8, so T^R(3) = 8 — no genome of 𝓛^R_3 has a run of 9 or more IDEAL steps from any start (EXACT-SAT, own encoding, 16 cubes; every cube CERTIFIED by a Glucose 4 DRUP proof checked by my own RUP checker, §4)
L-COMP successor 9, 2026-11-05 (date -u: see the commit). Labels: EXACT-SAT (solver UNSAT, machine-checked, not Lean, not refereed),
CERT (a solver proof checked by my own RUP checker), PROVED (lane: a short argument written out here), DATA. Not a TARGET.md claim.
No polynomial bound. G-N5-TIME stays OPEN. Every statement is about the IDEAL-ACYC model only.

## 1. Statement
- Model: the IDEAL model of RESULTS R104 (definition only; no theorem of R104 used), acyclic Ξ-graphs. R104's wording (RESULTS R104,
  docs/RESULTS.md): «an IDEAL genome G has N movers x with levels lev(x), M := Σ deg(x) options (x, k), each with a W-target of level
  lev(x) − 1 (none at level 0), a Ξ-target xt(x, k), a mover or the exit X, a distinct β-rank with a parity, a distinct gate index, and
  a start; under a state s the Ξ-value of option (x, k) is the set of β's on its chain (x, k), (xt, s(xt)), … up to the first
  Ξ-target X, compared by the β of largest rank in the symmetric difference: the option whose set contains that β is the better one if
  its parity is even and the worse one if odd; an IDEAL step moves every mover to the lexicographically least key (gate indices of the
  chain of W-targets under the new state, lowest level first) among its current option and the options with a strictly better
  Ξ-value, and the run stops when nothing is available or nothing changes, L(G) := its number of steps».
- Class and quantity (not landed terms; quoted from L-NEW's packet P-IDEAL-FLIP §1, claude/l-new 9effea1f, docs/new/P-IDEAL-FLIP.md
  l. 54-56): «𝓛^R_d (d ≥ 1; L-RED's R197 convention): N = 2d movers 0, …, 2d − 1, lev(x) = ⌊x/2⌋, every mover of degree 2, and
  wt(x, k) = 2(lev(x) − 1) + k for lev(x) ≥ 1 (option k of a level-l mover W-points to the k-th mover of level l − 1); Ξ-data, β's,
  gates and start arbitrary.» «T^R(d) := the largest T over 𝓛^R_d and all starts.» (= RESULTS R110 once landed; P-IDEAL-FLIP is CHECKER C122s item.) Here T = R104's L(G) from the given start, and
  «Ξ-data arbitrary» includes Ξ-targets at level-0 movers (ISO is NOT assumed).
- KEEP APART: R109's 𝓛_d / T*(d) (any W-targets one level down, degree-1 movers allowed). Nothing here is about 𝓛_d.
- STATEMENT P-TR3: for every genome G ∈ 𝓛^R_3 and every start s_0, the IDEAL run of G from s_0 has at most 8 steps: T^R(3) ≤ 8.
  With the witness of §5, T^R(3) = 8.

## 2. Method
- Query Q(L): «there are a genome of 𝓛^R_3 and a start whose run has at least L steps», as CNF, built by
  experiments/comp/box27/cnf.py (sha1 fd882af16648b82c014754cadcdaf9b85ae8296d at l-comp 557b045b), with d = 3, W = R, no padding.
  Clause-by-clause map to R104's wording: experiments/comp/box27/ENCODING.md §2-§3 (variables; ranks and gates as strict total
  orders; acyclicity by a strict total order on movers over ALL options; chains unrolled hop by hop; the comparison «largest-rank β of
  the symmetric difference, parity decides»; A-sets read at the OLD state; keys lexicographic under the NEW state, lowest level first;
  «T ≥ L» as «each of the first L steps changes the state», which excludes both stop reasons).
- Encoding facts used (PROVED, lane; ENCODING.md §3): (E1) Δ = chain(x,0) △ chain(x,1) is never empty, so «not 1 ▷ 0» = «0 ▷ 1»;
  (E2) keys of one level have equal length and position j holds a level-j gate, so only the order of gates INSIDE a level matters
  (per-level strict total orders are complete); (E3) two movers of one level: different W-targets → compare the targets' keys,
  same W-target → compare their gates (this is the lexicographic order, since distinct movers end in distinct gates).
- Symmetry break (the ONLY one): SYM, s_0(u_0) = s_0(v_0) = 0, u_0 = mover 0, v_0 = mover 1. PROVED (lane): for a level-0 mover x,
  relabel its two options (swap (x,0) and (x,1) with their Ξ-targets, β's (rank, parity) and gates; flip bit x of every state). The
  relabelled genome is in 𝓛^R_3 (level-0 options have no W-target; the wiring wt(y,k) = 2(lev(y)−1)+k refers to MOVERS, so it is
  untouched; ranks and gates stay distinct), and its run from the relabelled start is the old run state for state with bit x flipped
  (Ξ-chains through x use s(x)'s option, i.e. the same option object; key(x) is the gate of that same option; A-sets compare the same
  sets). Applying it to x = 0 and/or x = 1 maps every start to one with s_0(0) = s_0(1) = 0 and the same T.
- Cubes: CUBE fixes s_0(x) for x = 2, 3, 4, 5; cube c (0..15) sets s_0(2 + i) = bit i of c. The 16 cubes are all 2^4 assignments, so
  SYM × cubes covers every start up to the relabelling. Q(9) is UNSAT iff all 16 cube formulas are UNSAT.

## 3. Evidence
- Solver for the result: CaDiCaL 1.9.5 via pysat 1.9.dev15 (Solver(name="cadical195")), one process per cube, 2026-11-05.
- Q(9), per cube (seconds): 0 287.1; 1 158.8; 2 140.7; 3 312.3; 4 287.6; 5 154.2; 6 146.4; 7 280.5; 8 344.0; 9 309.1; 10 300.1;
  11 479.5; 12 611.8; 13 307.0; 14 336.8; 15 490.3 (total 4,946 s); all UNSAT. Logs: experiments/comp/box27/log/R_d3_L9/<c>.log (the
  build line names the cube; 58,896 vars, 204,036 clauses each), RESULT lines log/R_d3_L9_cubes.txt.
- CNF identity: DIMACS text «p cnf V C» + one line per clause in cnf.py's order, sha1 per cube (built by cnf.py at 557b045b and by the
  current cnf.py: byte-identical): 0 7e70b9e100155d8da2e7712469a6c1e145ac4850; 1 40412c7b6a8db5b8c87f9673499fcb233f519145; 2 d8cadc0ce70965077f8cb8a01fc0ef0357a9512c; 3 df5ecf8c3f31b1ce1671cbd6d71a4a445af71fd1; 4 57e654b424153eb7542734a7616bca0d60ae204e; 5 2701cae6e1025ef02c98c9d9b81b7fb181c68367; 6 e4886b4716f5fe07039fd62d9e2de787c780f83d; 7 f87b694607906e572841ca29ff7bca3023051385; 8 7fd44a80cc886adb701e5f9069d02b69d62676cf; 9 01a9488a18b51267dd6010802c7f4c9a3425d936; 10 924ae0118e1b142a8d762d03d314d4a0c9be1af2; 11 2ba36f3dc819868a75c8b6d3917d9298ee59065f; 12 7215704a0707adbbd7b2d367c750d2dda00ed1e1; 13 873e2eecd0e87c85d4ece243d47cb06d63a3cbb0; 14 c663d746f9c77edfaefb9fcfd4622b5b83eda04d; 15 44fb279663b37e55c7c5f3d78f58470ce6208f71
- Q(8) SAT: experiments/comp/box27/out/R_d3_L8.json, replayed by sim.py (my simulator from R104's text) and by L-RED's r187/ideal.py
  (claude/l-red 6f347876): T = 8, identical states, stop «opt».
- Semantic checks of the encoding (DATA): pinck.py pins a whole genome and start by unit clauses; the CNF is SAT at L = T and UNSAT at
  L = T + 1 with T from sim.py: 0 disagreements on 300 random d 2 and 150 random d 3 genomes of 𝓛^R and on all 64 starts of each of
  the 2 distinct length-8 genomes ext/dbl_d3_F6.json (L-RED R197) and ext/own_R_d3_L8.json (= the genome of out/R_d3_L8.json)
  (128 runs, T 0..8). At d 2 the same encoder gives Q(5) UNSAT and the
  exhaustive C enumeration bf2.c (no SAT) gives max T = 4 over all of 𝓛^R_2 and all starts. sim.py = ideal.py on 198,085 runs.

## 4. Certificate
- Route (REFEREE 24 gap T3-G1): drat-trim could not be fetched or built here (auto-mode classifier: «Code from External»; the same
  happened at the referee). Instead: Glucose 4 (pysat 1.9.dev15, Solver(name="glucose4", with_proof=True)) produces a textual DRUP
  proof per cube, and my own checker experiments/comp/box27/drup.c (sha1 2d4b8eab8fe9e9035c396733bb400d9d6e7d2366, l-comp 07cec839;
  98 lines of C, built with gcc -O2) checks it. CERT = this check; it is an own tool, not drat-trim.
- Checker semantics (summary of the drup.c header; the source is the reference):
  - Input: the DIMACS file of the cube (written by mkproof.py from exactly the clause list cnf.py builds) and the proof (lines «l1 … lk 0»
    = an added lemma; «d l1 … lk 0» = a deletion).
  - Forward RUP: for each added lemma C (duplicates removed; tautologies skipped), assign the negation of every literal of C on top of
    the current top-level assignment and unit-propagate over the current clause DB; the lemma is accepted iff a conflict arises (or a
    literal of C is already true at top level). Accepted lemmas join the DB. A lemma that fails stops the check: «s NOT VERIFIED:
    lemma i is not RUP». No RAT step is accepted.
  - Deletions: default mode APPLIES them (the DB clause with the same literal set is removed; literals already assigned at top level
    stay assigned). Mode IGNDEL=1 ignores them (the DB only grows). Both are sound: every clause ever in the DB is implied by the input
    formula, so RUP against any subset of it is a sound step; deletion can only make a check fail.
  - Verdict: «s VERIFIED (n lemmas RUP-checked)» iff the input plus the accepted lemmas reach a top-level conflict (empty clause /
    unit-propagation refutation) before the proof ends; otherwise «s NOT VERIFIED: no refutation reached».
- Negative tests (d 2, cnf.py d 2 L 5 / L 4 cube 0; files in the scratchpad, reproducible with mkproof.py): the d 2 L 5 UNSAT proof
  is VERIFIED in both modes (5,730 lemmas); the satisfiable d 2 L 4 formula with its solver «proof» is NOT VERIFIED (no refutation);
  the L 5 proof truncated to its first 3,000 lines is NOT VERIFIED (no refutation); the L 5 proof with deletion lines dropped and every
  7th remaining line removed is NOT VERIFIED («lemma 10 is not RUP»).
- Per cube (Q(9), d 3, SYM, CUBE as §2): DIMACS sha1 (= the §3 table, which equals cnf.py at 557b045b and now), Glucose time (s), proof
  sha1, proof size (bytes), lemmas RUP-checked, drup wall time (s), verdict; all in deletion-applying mode:
| cube | DIMACS sha1 | Glucose s | proof sha1 | proof bytes | lemmas | drup s | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 7e70b9e100155d8da2e7712469a6c1e145ac4850 | 488.7 | 0e98a96c3530a9f6da53234f17de00f3575094b2 | 1,460,488,502 | 807,459 | 1237 | s VERIFIED |
| 1 | 40412c7b6a8db5b8c87f9673499fcb233f519145 | 209.3 | e7f8d3880415937598a78fc1e8aeec8d1064554b | 970,002,355 | 567,712 | 853 | s VERIFIED |
| 2 | d8cadc0ce70965077f8cb8a01fc0ef0357a9512c | 258.9 | 41f973883c3b72755c54d84a15dabefd8e4b5f2f | 921,350,684 | 533,419 | 648 | s VERIFIED |
| 3 | df5ecf8c3f31b1ce1671cbd6d71a4a445af71fd1 | 295.7 | 4cb7024e7cab26b89fed834eb718862f8e093fe0 | 1,419,744,096 | 803,571 | 1086 | s VERIFIED |
| 4 | 57e654b424153eb7542734a7616bca0d60ae204e | 359.0 | e6c7527f3f925fb9b459ef1f4c4fead6463aa5e8 | 1,661,515,605 | 939,707 | 1378 | s VERIFIED |
| 5 | 2701cae6e1025ef02c98c9d9b81b7fb181c68367 | 184.9 | e45c0dd108e48fb8eddeb51ffcb4fe5787833baa | 913,302,433 | 544,619 | 654 | s VERIFIED |
| 6 | e4886b4716f5fe07039fd62d9e2de787c780f83d | 194.0 | ff59ee2cd3a9268d371022895e4509793f5f545b | 941,098,907 | 561,107 | 714 | s VERIFIED |
| 7 | f87b694607906e572841ca29ff7bca3023051385 | 431.6 | 657258c11459e2cb951efcb7cec890c736a6eba6 | 1,623,733,639 | 930,211 | 1453 | s VERIFIED |
| 8 | 7fd44a80cc886adb701e5f9069d02b69d62676cf | 345.1 | 2192cf5c5d051b976d5fad2dbe06c864a7c320dd | 1,598,046,419 | 931,580 | 1378 | s VERIFIED |
| 9 | 01a9488a18b51267dd6010802c7f4c9a3425d936 | 177.5 | 942334eb3905ff3aa887e37db72d1df84433b804 | 894,105,785 | 526,970 | 641 | s VERIFIED |
| 10 | 924ae0118e1b142a8d762d03d314d4a0c9be1af2 | 190.9 | cae6998bd94b78005931ee2faff7eaffc3c122fc | 851,461,087 | 485,366 | 709 | s VERIFIED |
| 11 | 2ba36f3dc819868a75c8b6d3917d9298ee59065f | 357.3 | a8ede7f045be25665eb98844a38c47f3b25accac | 1,585,527,511 | 915,729 | 1411 | s VERIFIED |
| 12 | 7215704a0707adbbd7b2d367c750d2dda00ed1e1 | 324.4 | cb63a3197c11ca175ccb1b9ae27ee627d7cc6e89 | 1,500,256,933 | 885,374 | 1418 | s VERIFIED |
| 13 | 873e2eecd0e87c85d4ece243d47cb06d63a3cbb0 | 199.2 | b2cf489ac74bbd8d84330ab0d39bf49a03f195c3 | 860,468,273 | 528,362 | 719 | s VERIFIED |
| 14 | c663d746f9c77edfaefb9fcfd4622b5b83eda04d | 204.7 | 77052f059eb2c02dcaa8c1d83dfd5d1bb4406aa3 | 926,008,396 | 551,347 | 741 | s VERIFIED |
| 15 | 44fb279663b37e55c7c5f3d78f58470ce6208f71 | 331.9 | 142821525d1130b7f11c324fc38be03a43d17655 | 1,567,848,549 | 841,457 | 1201 | s VERIFIED |
- Totals: 16/16 VERIFIED; 11,353,990 lemmas; 19,694,959,174 proof bytes. Each cube: 58,896 variables, 204,036 clauses (§3).
- Determinism: cube 1 was proved twice (2026-11-05 ~14:39Z and ~01:0xZ on 11-06): both proofs have sha1 e7f8d388…, so a referee who
  re-runs mkproof.py gets byte-identical proofs. Cube 1 was first checked in IGNDEL mode (567,711 lemmas, VERIFIED; record
  log/R_d3_L9_c1_igndel.chk); the table row is the deletion-applying re-check (567,712 lemmas: with deletions ignored the larger DB
  reached the refutation one lemma earlier).
- Storage: the proofs (0.9-1.7 GB each, 19.7 GB in total) are NOT committed (too large for git); each was deleted after its check,
  sha1 and size recorded. Re-run: python3 mkproof.py 3 9 <cube> DIR glucose4; ./drup DIR/d3_L9_c<cube>.cnf DIR/d3_L9_c<cube>.glucose4.proof
  (or PDIR=DIR PAR=1 ./proofs.sh for all 16; records via certtab.py). Records: log/R_d3_L9_cert.txt.
- Limits (stated plainly): drup.c is my own, unaudited tool (no drat-trim / LRAT cross-check); its correctness is a premise of CERT.
  It checks only RUP, so it can wrongly REJECT, never (if correct) wrongly accept. The DIMACS files are produced by the same cnf.py
  whose encoding §2 / ENCODING.md maps to R104; CERT certifies the UNSAT of those formulas, not the encoding.

## 5. What is proven, and what rests on the solver
- PROVED (lane, written out above / in ENCODING.md): E1-E3, the soundness of SYM, the cube cover, «Q(9) UNSAT ⇔ P-TR3» given that the
  CNF encodes R104 for 𝓛^R_3 (ENCODING.md §3, which is the item a referee must check against R104's text).
- Rests on the machine: the UNSAT of the 16 cube formulas, now CERTIFIED (§4): every cube has a Glucose proof accepted by drup.c.
  What remains trusted: (i) drup.c (own forward RUP checker, §4 limits); (ii) cnf.py's DIMACS output being the encoding of §2 (checked
  by two referee audits of ENCODING.md and by pinck.py, not by a proof). The original CaDiCaL 1.9.5 UNSAT results (§3) and Glucose 4's
  16/16 UNSAT agree.
- DATA only (not part of the claim): pinck, bf2, the replays.

## 6. EXCLUDED
- 𝓛_d and T*(d) (free W-targets, padding); d ≠ 3; Ξ-cyclic genomes; real N5 runs (no use of R104's REALIZE); any bound for d ≥ 4.

## 7. TARGET.md diff
- Not a TARGET.md claim: a statement inside the IDEAL model; G-N5-TIME stays OPEN; not M3, not a step-4 pass.
