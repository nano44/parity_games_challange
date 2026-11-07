# R2-T3R-audit: audit of L-COMP box 27's encoding of «T^R(3) = 8» (G-FLIP-1 part (b))
REFEREE-2 successor 27 (Opus 5.5, D12/D19). Written 2026-11-05 12:49Z (date -u). Asked by the Lead 12:31Z (its stamp).

## Object
- claude/l-comp 6f19564f, experiments/comp/box27/: ENCODING.md sha1 2ba6b1a0aeb4ef7079878f98b52acacc2404741f (64 lines); cnf.py sha1
  fd882af16648b82c014754cadcdaf9b85ae8296d (215 lines; the file's only commit is 557b045b, so every cube ran this file); pinck.py
  9dc3c503…; cubes.sh; log/R_d3_L9/0..15.log and log/R_d3_L9_cubes.txt.
- Claim audited: «some genome of 𝓛^R_3 (R197 wiring, 2 movers per level, degree 2, no padding; Ξ-targets (acyclic), ranks, parities,
  gates and start free; ISO not imposed) and some start give T ≥ 9» is UNSAT. With the SAT witness at T = 8, T^R(3) = 8.

## 1. cnf.py against R104's definition, clause by clause
| R104 element | cnf.py | verdict |
| --- | --- | --- |
| movers, levels, degree 2, R197 W-targets | movers 2l, 2l + 1; Wv constants w = 2(l − 1) + k (W=R); level 0 none | ✓ |
| Ξ-target: exit or a mover, Ξ-graph acyclic over ALL options | Xv exactly-one over {X} ∪ {y ≠ x} (level-0 movers included unless ISO); Xv = y ⇒ π(x < y), π a strict total order (transitivity clauses) | ✓ acyclic ⇔ some topological order: sound and complete |
| distinct β-rank per option, parity | rk strict total order on the 12 options; par free | ✓ |
| distinct gates | strict total order per level (gord) | ✓ only same-level gates are ever compared (key position j holds a level-j gate; keys of one level have equal length); per-level orders extend to distinct global gates (decode uses 100·l + rank) |
| chain and Ξ-value | cm_(h+1)(x, k) = {(x, k)} ∪ ⋃_y [Xv = y] · cm_h(y, s(y)), N iterations | ✓ acyclic chains have ≤ N movers; one β per option, so «set of β's» = set of options |
| comparison: largest rank in the symmetric difference, even = better | better1: decisive o ∈ Δ with all other Δ-ranks below; result = (o ∈ chain(x, 1)) XOR odd(o) | ✓ (four cases checked); Δ ≠ ∅ since (x, k) lies only on its own chain (acyclic), so no ties |
| A-set (current + strictly better), at the OLD state | B_t(x) = better1(t) XOR S[t][x] | ✓ |
| step: key-least in A under the NEW state, lowest level first | S[t+1][x] = ITE(B_t(x), KP_(t+1)(x), S[t][x]); KP from lt(t + 1) of the level below (R197: the two options' W-targets differ) or the gate at level 0 | ✓ lt reads only S[t+1] at lower levels, so the simultaneous constraints have exactly the level-by-level solution |
| keys, lexicographic, lowest level first | lt(y, y′): different W-targets ⇒ lt of the targets; same target ⇒ own gates; level 0 ⇒ gates | ✓ distinct movers of one level have distinct keys (last entries are distinct gates), so a differing prefix decides |
| stop rules and T | for t < L: S[t+1] = step(S[t]) and S[t+1] ≠ S[t] | ✓ both stops (all A singletons ⇒ step = identity; no change) are excluded on the first L steps; every run with T ≥ L satisfies the clauses |
- Padding (P), W=free, FREE0, ISO and KF are off for this claim: verified below.

## 2. Symmetry break SYM (s_0(u_0) = s_0(v_0) = 0): SOUND
- Relabelling the two options of a level-0 mover x (moving Ξ-target, β (rank, parity) and gate with the label, and flipping bit x in
  every state) maps 𝓛^R_3 to itself: level-0 options have no W-target; other options refer to x only as a mover (W-target, Ξ-target);
  chains through x use the option s(x) names, x's key reads gate(x, s(x)); x's own A-set and KP are label-symmetric; ranks and gates stay
  distinct. The run maps state for state with bit x flipped, so T is unchanged. Applied to u_0 and/or v_0, every start reduces to
  s_0(u_0) = s_0(v_0) = 0. (It would NOT be sound at levels ≥ 1, where option k's W-target is fixed by the wiring; cnf.py applies it to
  movers 0 and 1 only.) ✓

## 3. Cube coverage: COMPLETE
- cubes.sh: cube c fixes s_0(i + 2) = bit i of c, i = 0..3, c = 0..15: all 2^4 assignments of movers 2-5. With SYM: every start up to
  the relabelling. The 16 log build lines name the 16 distinct cubes. ✓
- ISO off in the lane's runs: the build line does not print ISO, but cnf.py with ISO=1 gives 30,994 variables / 103,952 clauses, and
  without ISO 58,896 / 204,036; every lane log reads 58,896 / 204,036. So the logged runs had ISO, FREE0 and padding off. ✓

## 4. Re-run of all 16 cubes (REFEREE-2, this container)
- cnf.py extracted from 6f19564f (sha1 fd882af1 re-checked), driver docs/referee-2/R2-T3R-audit/cubes_r2.sh with ISO, FREE0, P, W, KF
  explicitly unset, SYM=1; pysat 1.9.dev15, cadical195; 12:31-12:48Z, 4 parallel.
- Result: all 16 cubes «RESULT d 3 T >= 9 P None W R: UNSAT», 128-341 s each (lane: 141-612 s); every build line 58,896 vars / 204,036
  clauses (= lane). Summary file R2-T3R-audit/cubes_r2_results.txt. ✓ (A re-run, not an independent encoding.)

## 5. Semantic checks
- Lane pinck.py (read): pins a whole genome + start, SAT at L = T and UNSAT at L = T + 1 with T from the lane's sim.py. Its random genomes
  give mostly T 0-2; its long runs are all 64 starts of two T = 8 genomes.
- Mine, docs/referee-2/R2-T3R-audit/pin_mine.py: the same pin test, but T from MY simulator (R2-P-IDEAL-M2/m2_check.py, written from
  R104's text) and my own pinning code (no lane simulator):
  - all 64 starts of the lane's T = 8 witness (from my FLIP re-run of L-RED's encoding): T 0-8;
  - the 50 𝓛^R genomes of box160/out and box162/out (d = 2, 3, 4; ISO and non-ISO), stored starts: T 1-12;
  - 150 random 𝓛^R_3 and 150 random 𝓛^R_2 genomes (70 % non-ISO): T 0-2.
  - 414 (genome, start) pairs, 0 disagreements (R2-T3R-audit/pin_mine_results.txt). This also covers d = 4 encodings (T up to 12).
- Cross-encoding: L-RED's xcnf.py (a different author and encoding; my FLIP report) also gives T ≥ 9 UNSAT and T ≥ 8 SAT on 𝓛^R_3, and
  bf2.c (exhaustive, no SAT) agrees at d = 2 (T^R(2) = 4; lane DATA, not re-run by me).

## 6. Verdict
- The encoding is faithful to R104's definition on every clause; the symmetry break is sound; the cubes cover every start; ISO was off;
  the UNSAT result reproduces here; the pin test against my independent simulator has 0 disagreements, including runs of length 8-12.
- Residual caveat (stated, not a gap in the sense of G-FLIP-1): no DRAT/LRAT certificate; the UNSAT rests on CaDiCaL 1.9.5's
  correctness. It is reported by two independent encodings (L-RED xcnf.py, L-COMP cnf.py) and re-run by me.
- **G-FLIP-1 CLOSES on my side**: part (a) (independent encoding, UNSAT over all of 𝓛^R_3, every start, ISO or not) and part (b) (referee
  check of that encoding against R104) both hold. The DEAD SC-ISO may drop «CONDITIONAL». Its premise should then be cited as «T^R(3) ≤ 8
  (two independent CNF encodings, CaDiCaL UNSAT, no DRAT certificate; encoding audited by REFEREE-2, R2-T3R-audit.md)», not as a
  theorem. Under D1's two-referee rule the other referee's audit is still needed before the change lands.
