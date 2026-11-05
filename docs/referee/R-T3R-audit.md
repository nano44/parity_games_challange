# R-T3R-audit: REFEREE audit of the machine premise T^R(3) ≤ 8 (gap FL-G1 of R-P-IDEAL-FLIP)
REFEREE successor 24 (Opus 5.5, D15), written 2026-11-05 (date -u in the commit). Independent second audit under D1: I did not
open or list anything in docs/referee-2/ before this report was pushed.
- Object: claude/l-comp 6f19564f (an ancestor of origin/claude/l-comp), experiments/comp/box27/. Read from a detached worktree.
  - cnf.py sha1 fd882af1…; cubes.sh d941b617…; sim.py f494b4e6…; pinck.py 9dc3c503…; ENCODING.md, README.md; log/R_d3_L9/ (16 logs).
- Definition audited against:
  - RESULTS R104's model text (trunk 61a1175c, RESULTS l. 9864);
  - P-IDEAL-FLIP §0 and §1 (claude/l-new 9effea1f): 𝓛^R_d and T^R(d).
  - NOTE: T^R(d) and 𝓛^R_d are NOT defined in RESULTS R105-R109 (grep on trunk 61a1175c finds no hit for «T^R» or «𝓛^R»). The only
    definition of record is P-IDEAL-FLIP §1: «N = 2d movers 0, …, 2d − 1, lev(x) = ⌊x/2⌋, every mover of degree 2, and wt(x, k) =
    2(lev(x) − 1) + k for lev(x) ≥ 1 …; Ξ-data, β's, gates and start arbitrary. … T^R(d) := the largest T over 𝓛^R_d and all starts.»
    A RESULTS entry for the premise must restate this definition.

## 0. Verdict
| item | verdict |
| --- | --- |
| cnf.py as an encoding of «some genome of 𝓛^R_3 and some start give T ≥ L» | FAITHFUL WITH GAPS (T3-G1, T3-G2; neither is an error) |
| scope: full 𝓛^R_3, ISO not imposed, every start | FAITHFUL |
| symmetry break SYM=1 and the 16 cubes | SOUND; the cubes cover every start |
| T^R(3) ≥ 8 | PROVED by an explicit instance (R_d3_L8, T 8 under my own simulator) |
| T^R(3) ≤ 8 | holds IF the solvers' UNSAT answers are correct: 16/16 UNSAT under CaDiCaL 1.9.5 and under Kissat 4.0.4 (no certificate) |

- Gaps (listed, as D1 / CLAUDE.md require for a refereed machine claim):
  - T3-G1 (solver trust). No UNSAT certificate (DRAT/LRAT) was produced or checked, by L-COMP or by me (§4 says why). The upper
    bound rests on the UNSAT answers of SAT solvers, not on a checked proof.
  - T3-G2 (definition home). The class is defined only in a lane packet (P-IDEAL-FLIP §1), not in RESULTS (see the note above).

## 1. Clause map: cnf.py → R104 / P-IDEAL-FLIP §0-§1 (W=R, d = 3, no padding, SYM=1, CUBE)
Every definition was diffed against the source text (trap R105-E1), not only the target.
| R104 / §0-§1 text | cnf.py | check |
| --- | --- | --- |
| movers 0..2d−1, lev = ⌊x/2⌋, degree 2, no other movers | `build`: two movers per level, deg 2, P = [0]*d | MATCH |
| wt(x, k) = 2(lev − 1) + k (level ≥ 1), none at level 0 | `Wv` constants under wiring "R" (`w == 2*(lev[x]-1)+k`) | MATCH |
| Ξ-target: a mover or X, «arbitrary» | `Xv[(x,k)]`: exactly one of {every mover y ≠ x} ∪ {exit}; ISO off (level-0 targets allowed) | MATCH (full scope) |
| IDEAL-ACYC: the Ξ-graph over ALL options is acyclic | `Xv=y → pi(x<y)`, pi a strict total order on movers (transitivity clauses) | MATCH (acyclic ⇔ a topological order exists) |
| distinct ranks; parities free | `rk` strict total order on all 12 options; `par` free | MATCH |
| distinct gates | `gord[l]` strict total order per level | MATCH: only same-level gates are ever compared (see note K) |
| chain of (x, k) under s; value = set of β's | `chains(t)`: N hop-unrolled layers, cm_(h+1)(x,k) = {(x,k)} ∪ [xt = y]·cm_h(y, s_t(y)) | MATCH (an acyclic chain has ≤ N options) |
| P ▷ Q: largest-rank β of P △ Q in P and even, or in Q and odd | `better1`: OR_o [o ∈ Δ, all other Δ-members have smaller rank, (o ∈ chain(x,1)) XOR odd(o)] | MATCH (Δ ≠ ∅: (x,0) only on chain(x,0) by acyclicity) |
| A_s(x) = {s(x)} ∪ strictly better options, at the OLD state | `Bx = better1(t) XOR S[t][x]` with chains of S[t] | MATCH |
| least key in A, keys under the NEW state, lowest level first | `nx = ITE(Bx, kp1(t+1), S[t][x])`, `keys_lt(t+1)` from S[t+1] level by level | MATCH |
| key = key(wt, s(wt)) + (g) / (g) at level 0; lexicographic | `keys_lt`: different W-targets → compare the targets' keys; same target → compare the two gates; level 0 → gates | MATCH (note K) |
| stop when all A singleton or nothing changes; T = #steps | for t < L: S[t+1] = step(S[t]) AND OR_x (S[t+1][x] ≠ S[t][x]) | MATCH: T ≥ L ⇔ SAT (both stop reasons give S[t+1] = S[t]) |
- Note K (keys). Two movers of one level have keys of equal length (one gate per level below). If their W-targets differ, the
  prefixes end in the gates of two distinct options, so they differ and decide; if equal, the prefixes are equal and the own gates
  decide. This is exactly cnf.py's rule. Gates of different levels never meet at one tuple position, so a per-level total order
  loses no generality (any family of per-level orders extends to distinct global integers).
- Constant folding. `CNF.AND/OR/XOR` fold Python booleans. An `[]` clause would make every instance trivially UNSAT: I counted
  0 empty clauses in all 16 cube CNFs (t3r_dimacs.py), and the pinned tests below reach SAT at every length 1..8.
- What the map does NOT cover by itself: pysat's CNF hand-over to the solver and the solver's internals (T3-G1).

## 2. Symmetry break and cubes
- SYM=1 forces s_0(0) = s_0(1) = 0. Sound: swapping the two option LABELS of a level-0 mover x, with each option's Ξ-target, β (rank,
  parity) and gate, and flipping bit x in every state, maps 𝓛^R_3 to itself and a run to the same run (T equal).
  - Level-0 options have no W-target.
  - Every other option refers to x only as a MOVER: as W-target (the wiring 2(l−1)+k names movers of level l − 1, never options of
    x) or as Ξ-target; chains use x's current option and keys read g(x, s(x)).
  - Ranks and gates stay distinct; acyclicity is about movers, so it is unchanged.
  - The same swap is NOT available at levels ≥ 1 (option k's W-target is fixed by k), and cnf.py does not use it there. CORRECT.
- CUBE fixes s_0(x) for x = 2..5; the 16 cubes are all 2^4 assignments. With SYM, every start is covered up to the relabelling.
- No other symmetry break, no lane lemma, no ENC (R105) is used.
- Scope matches the use: SC-ISO's bound T^R(d − 1) is over all of 𝓛^R_(d−1) (ISO is a hypothesis on the d-level genome only), and
  cnf.py imposes no ISO.

## 3. Own independent checks (docs/referee/scratch/; `python3 -I`)
- t3r_sim.py: my simulator, written from R104's text and P-IDEAL-FLIP §0 only (β-SETS, literal key tuples under the new state).
  No L-COMP, L-RED or L-NEW code was read for it. It has MUT controls (oldkeys, parity, minrank).
  - out/R_d3_L8.json (L-COMP's SAT witness): in 𝓛^R_3, T = 8 from its start, max over all 64 starts 8. So T^R(3) ≥ 8 is PROVED
    by this instance (a run of the R104 model, recomputed independently).
  - ext/dbl_d3_F6.json (L-RED R197): in 𝓛^R_3, max over starts 8. ext/own_R_d3_L8.json is the SAME genome as out/R_d3_L8.json
    (all genome fields equal; only «states» differs), so there are two distinct length-8 champions, not three.
  - The MUT controls change the run on both champions (T from start 8 → 6 / 1 / 1).
- t3r_pin.py: my pinning code (pinck.py not used). For a genome G and start s0, with T from MY simulator:
  - CNF(3, T) + pins (Ξ-targets, parities, all rank pairs, all gate pairs, start) is SAT, and the decoded states S[0..T] EQUAL my
    simulator's states, state for state (a stronger test than lengths);
  - CNF(3, T + 1) + pins is UNSAT;
  - genome-only (start free): CNF(3, Tmax + 1) UNSAT and CNF(3, Tmax) SAT, Tmax my maximum over all 64 starts.
- Results (logs t3r_logs/):
  | batch | runs (genome × start) | T histogram | run disagreements | genome-only tests / disagreements |
  | --- | --- | --- | --- | --- |
  | champions R_d3_L8, dbl_d3_F6, own_R_d3_L8 (= R_d3_L8), bf2_wit0, bf2_wit1 (d 2), all starts | 224 | 0..8 (T 8: 3 runs) | 0 | 5 / 0 |
  | 40 single-field mutants of R_d3_L8, all 64 starts | 2,560 | 0..8 | 0 | 40 / 0 |
  | 40 mutants of dbl_d3_F6, all starts | 2,560 | 0..8 | 0 | 40 / 0 |
  | 40 mutants of own_R_d3_L8 (same genome and seed as row 2: a repeat, not new coverage) | 2,560 | 0..8 | 0 | 40 / 0 |
  | 60 random 𝓛^R_3 genomes (Ξ-targets anywhere, incl. level 0 and lower levels), half hill-climbed, all starts | 3,840 | 0..5 | 0 | 60 / 0 |
  | 200 random 𝓛^R_2 genomes, half climbed, all starts | 3,200 | 0..4 | 0 | 200 / 0 |
  - Distinct coverage: 12,384 runs (repeat batch excluded), 345 genome-only tests; 0 disagreements. Mutations: rank swap, parity
    flip, gate swap (also across levels), Ξ-target change (kept acyclic). Every genome-only test is SAT at its Tmax and UNSAT at Tmax + 1,
    as my simulator predicts; for the two champions and the 24 mutants with Tmax 8, Tmax + 1 = 9.
- Mutation controls on the encoding (copies of cnf.py with one change each; t3r_pin.py files on the two champions, 128 runs):
  - keys under the OLD state (2 lines): 112 disagreements;
  - parity rule reversed (1 line): 126;
  - chains truncated to one hop (1 line): 100;
  - same-W-target gate comparison reversed (1 line): 94.
  - So the pin test detects each of these encoding errors.
- Falsification search (t3r_climb.py, my simulator, DATA): 40 restarts × 400 hill-climb steps over 𝓛^R_3; best max-over-starts T
  6. Weak (it does not reach the known 8); it neither supports nor weakens the bound, and is reported only for completeness.

## 4. Re-run of the 16 T ≥ 9 cubes at 6f19564f
- Same CNFs as L-COMP's: every cube 58,896 vars, 204,036 clauses (L-COMP's 16 logs show the same numbers), 69 unit clauses, 0 empty
  clauses; DIMACS sha1 per cube in t3r_logs/dimacs_sha1.txt (so any solver can re-check the exact formula).
- CaDiCaL 1.9.5 (pysat 1.9.dev15, solver name cadical195), cubes.sh unchanged, PAR 2; Kissat 4.0.4 (pysat kissat404), t3r_cube.py:
  | cube | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | CaDiCaL 1.9.5 (s) | 358 | 159 | 240 | 596 | 537 | 221 | 214 | 340 | 376 | 227 | 223 | 364 | 457 | 230 | 255 | 492 |
  | Kissat 4.0.4 (s) | 517 | 369 | 345 | 532 | 540 | 309 | 276 | 440 | 430 | 303 | 257 | 500 | 441 | 344 | 429 | 601 |
  - CaDiCaL: 16/16 UNSAT, 5,289 s solver time (2026-11-05 14:13Z-15:00Z, PAR 2; t3r_logs/cadical195_ref24.txt). Same verdicts as
    L-COMP's log/R_d3_L9_cubes.txt (times differ by load).
  - Kissat: 16/16 UNSAT, 6,633 s (t3r_logs/kissat/<c>.txt). Each log's DIMACS sha1 equals t3r_logs/dimacs_sha1.txt (checked), so
    both solvers saw byte-identical formulas.
  - Third solver, Glucose 4 (pysat glucose4, MiniSat lineage, different authors): cube 1 UNSAT 278.5 s (t3r_logs/glucose4/1.txt).
    The remaining 15 cubes are running; results go into an addendum. Not needed for the verdict.
- DRAT/LRAT: NOT done. Why:
  - pysat's cadical195 returned no proof (with_proof=True gives an empty proof in this build) and pysat refuses proof logging for
    kissat404 («Proof logging is not supported by Kissat in PySAT»);
  - building the standalone cadical / kissat / drat-trim binaries from their source repositories was refused by this session's
    permission policy (external code), so no proof could be emitted to a file or checked;
  - lingeling under pysat can emit DRUP, but with no checker available a proof cannot be checked, and a Python RUP checker over
    204k clauses and a proof of a multi-minute solve is out of reach here.
  - A certificate route (cadical --lrat or kissat proof + drat-trim / cake_lpr on the 16 recorded DIMACS files) needs a session
    allowed to build those tools; I list it as NEEDS.

## 5. What is proven by this audit, and what rests on the solver
- PROVED (by an instance re-run with my own simulator): T^R(3) ≥ 8.
- AUDITED (by reading and by tests; not a proof): cnf.py encodes exactly «some genome of 𝓛^R_3 and some start give T ≥ L», for the
  full class, every start; SYM and the cubes are sound. Tests: pinned genomes (state-for-state), genome-only maxima, four mutation
  controls that bite.
- RESTS ON THE SOLVERS: «no genome of 𝓛^R_3 and no start give T ≥ 9», i.e. T^R(3) ≤ 8. Evidence: 16/16 UNSAT under CaDiCaL 1.9.5
  (L-COMP's run and mine), 16/16 UNSAT under Kissat 4.0.4 (mine), cube 1 under Glucose 4; and L-RED's separate
  xcnf encoding (UNSAT at d 3, T 9; not audited by me). No checked certificate.
- My ruling on FL-G1: the premise is now refereed as «T^R(3) = 8: lower bound by instance, upper bound by an audited encoding and
  solver UNSAT (two solvers), no certificate». Whether that is «established» enough to drop CONDITIONAL from DEAD SC-ISO is the
  Lead's L42/L43 call once REFEREE-2's audit is compared (§C). My recommendation: land it as its own RESULTS entry labelled with
  gap T3-G1 («machine, uncertified»), and keep the DEAD line's dependence on it explicit; a DRAT/LRAT check would close T3-G1.

- NOT CHECKED here (out of the brief's scope): box 27's other results (bf2.c / bfk.c, T^R(2) = 4, the T_k(m) table, padded
  T*(d), the running d 4 cubes), L-RED's xcnf.py, and L-COMP's sim.py / pinck.py beyond reading them.

## 6. Diff against TARGET.md
- The statement is about the IDEAL model of R104 only (a combinatorial run length on a finite class). It concerns no parity game,
  no running time of a solver and no cost model. Not M3, not M4, not a gauntlet step. G-N5-TIME stays OPEN.

## §C. Comparison with REFEREE-2's audit (2026-11-05, after my report was pushed at 776d0fdf; Lead 16:55Z)
- Read only after my push: docs/referee-2/R2-T3R-audit.md at claude/referee-2 d1c4a530 (an ancestor of origin; file sha1 75197995…).
- AGREE (independently reached, the same on every point):
  - clause map: every R104 element MATCHES in both (wiring, Ξ-targets over all movers + exit, acyclicity via a strict mover order,
    ranks, per-level gate orders with the same «only same-level gates meet» argument, hop-unrolled chains, the Δ rule with Δ ≠ ∅, A-sets
    at the old state, keys under the new state, the T ≥ L target with both stop rules);
  - SYM SOUND by the same level-0 relabelling argument, and both note it would be unsound at levels ≥ 1;
  - the 16 cubes cover every start; both re-ran the 16 cubes under CaDiCaL 1.9.5 (16/16 UNSAT, 58,896 / 204,036 per cube);
  - both state the missing DRAT/LRAT certificate.
- REFEREE-2 HAS, I DID NOT:
  - an explicit proof that ISO was OFF in the lane's logged runs, by counts: ISO=1 gives 30,994 vars / 103,952 clauses, ISO=0 gives
    58,896 / 204,036, and every lane log reads 58,896 / 204,036. I RE-MEASURED both counts on cube 0 at 6f19564f: EQUAL. My own
    check was the same counts on my rebuild with ISO unset, which shows my re-run was ISO-free but not, by itself, the lane's;
    REFEREE-2's comparison closes that. CONCUR.
  - pinned runs on the 50 𝓛^R genomes of box160/out and box162/out, including d = 4 (T up to 12). These exercise cnf.py at d = 4,
    which my checks (d 2, 3 only) do not. Not needed for d = 3, but a real extra.
- I HAVE, REFEREE-2 DID NOT:
  - state-for-state comparison of the pinned CNF with my simulator (REFEREE-2 compares lengths, T SAT / T + 1 UNSAT);
  - four mutation controls on the encoding, each caught (94-126 disagreements), so the pin test is shown to bite;
  - scale: 12,384 distinct pinned runs + 345 genome-only tests (REFEREE-2: 414 pairs);
  - a second SOLVER on byte-identical DIMACS: Kissat 4.0.4, 16/16 UNSAT (REFEREE-2 relies on CaDiCaL only, plus L-RED's second
    ENCODING, also solved with CaDiCaL); DIMACS sha1 per cube recorded;
  - 0 empty clauses in all 16 cube CNFs (a trivial-UNSAT check);
  - T3-G2: 𝓛^R_d / T^R are not defined in RESULTS (only in P-IDEAL-FLIP §1).
- DIFFER (labelling, not substance):
  - REFEREE-2 calls the missing certificate a «residual caveat … not a gap» and writes «G-FLIP-1 CLOSES on my side … The DEAD SC-ISO
    may drop CONDITIONAL», premise cited «not as a theorem». I list it as gap T3-G1 and leave dropping CONDITIONAL to the Lead's L42/L43
    reading. Both of us say the upper bound rests on solver correctness and must be cited as a machine result; the difference is only
    whether that suffices for «established». Under the Lead's 16:55Z plan the difference disappears if T3-G1 closes by an audited
    in-fleet RUP check (L-COMP drup.c on Glucose 4 proofs); I will audit drup.c inside P-TR3.
  - REFEREE-2 counts L-RED's xcnf.py as an independent encoding (from its FLIP report). I did not audit xcnf.py, so I do not rely on it.
- No disagreement on any fact. Joint position: cnf.py is a faithful encoding for the full 𝓛^R_3; T^R(3) ≥ 8 by instance; T^R(3) ≤ 8 by
  solver UNSAT, uncertified until P-TR3's RUP check is audited.

## Addendum 1 (2026-11-05, successor 24): Glucose 4 pass complete
- Glucose 4 (pysat glucose4) on the same 16 cube CNFs (t3r_cube.py; DIMACS sha1 equal to t3r_logs/dimacs_sha1.txt): 16/16 UNSAT, 5,640 s
  in total (t3r_logs/glucose4/<c>.txt). Cubes 13-15 were relaunched after a container restart killed them (the first attempt left
  13.txt.part / 14.txt.part in commit bfeca123; they are removed here).
- So three solvers of two lineages (CaDiCaL 1.9.5 and Kissat 4.0.4; Glucose 4, MiniSat lineage) agree: 16/16 UNSAT each. Still no
  checked certificate: T3-G1 stays open until P-TR3's RUP check (L-COMP drup.c on Glucose 4 proofs) is audited.
