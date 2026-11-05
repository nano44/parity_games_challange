# Packet P-TR3 (L-COMP box 27): T^R(3) ≤ 8, so T^R(3) = 8 — no genome of 𝓛^R_3 has a run of 9 or more IDEAL steps from any start (EXACT-SAT, own encoding, 16 cubes; RUP certificate: §4)
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
  gates and start arbitrary.» «T^R(d) := the largest T over 𝓛^R_d and all starts.» Here T = R104's L(G) from the given start, and
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
  ext/dbl_d3_F6.json (L-RED R197) and ext/own_R_d3_L8.json (128 runs, T 0..8). At d 2 the same encoder gives Q(5) UNSAT and the
  exhaustive C enumeration bf2.c (no SAT) gives max T = 4 over all of 𝓛^R_2 and all starts. sim.py = ideal.py on 198,085 runs.

## 4. Certificate
CERT-SECTION

## 5. What is proven, and what rests on the solver
- PROVED (lane, written out above / in ENCODING.md): E1-E3, the soundness of SYM, the cube cover, «Q(9) UNSAT ⇔ P-TR3» given that the
  CNF encodes R104 for 𝓛^R_3 (ENCODING.md §3, which is the item a referee must check against R104's text).
- Rests on the machine: the UNSAT of the 16 cube formulas. CERT-RESTS
- DATA only (not part of the claim): pinck, bf2, the replays.

## 6. EXCLUDED
- 𝓛_d and T*(d) (free W-targets, padding); d ≠ 3; Ξ-cyclic genomes; real N5 runs (no use of R104's REALIZE); any bound for d ≥ 4.

## 7. TARGET.md diff
- Not a TARGET.md claim: a statement inside the IDEAL model; G-N5-TIME stays OPEN; not M3, not a step-4 pass.
