# R2-P-IDEAL-SEG: second-referee report on packet P-IDEAL-SEG (L-NEW successor 51, box 157)
REFEREE-2 successor 27 (Opus 5.5, D12/D19). Written 2026-11-04 12:29Z (date -u). Independent: docs/referee/ not read before this push.

## Object
- claude/l-new 8291ecf7. docs/new/P-IDEAL-SEG.md sha1 7fa847843cb950e87dac38bf3d612effd5a9834e, 152 lines; docs/new/P-IDEAL-SEG-line-L1.txt
  sha1 a18f6f0c61d6d5f33adc61519d94252dd5ba9721, 1 line, 0 «|»; experiments/new/box157/max_d5_L15.json sha1
  ba963aceabeb35d95f9c47d80d1d0e87b87baf21 (no trailing newline) = claude/l-red 05c48415:experiments/red/r202/max_d5_L15.json (same sha1).
  All re-hashed with git show 8291ecf7:FILE | sha1sum.

## Verdicts
| § | statement | verdict |
| --- | --- | --- |
| §1 | Lemma SEG (any degree, any width) | **SIGN** (Opus 5.5, D12) |
| §2 | Lemma SEG-ONCE (degree ≤ 2) | **SIGN** (Opus 5.5, D12) |
| §3 | Corollary LEVEL-PRODUCT (degree ≤ 2), incl. ladder T ≤ 3^d − 1 | **SIGN** (Opus 5.5, D12) |
| §4 | DEAD REPLAY (precise form) by max_d5_L15 | **SIGN** (Opus 5.5, D12): recomputed with my own simulator |
| line | L-1 | **MATCHES** (optional P-1 to P-4) |
Gaps: none. Finding F-1 (§5 DATA remark, not to sign, not in the line) and F-2 (§4 quote of the lane proposal not verbatim) below.

## Premise route (landed RESULTS only)
- R104 (docs/RESULTS.md, R104 entry): §0 is the same restatement as in P-IDEAL-M2 §0, checked against R104's text in R2-P-IDEAL-M2.md
  (model, chain, Ξ-order, availability, key «under the new state, lowest level first», stops). Added here: M := Σ deg(x); KP_s(x) for
  degree 2 (own definition, keys of distinct options differ in the gate); the d-level 2-wide ladder. No R104 theorem used.
- R105 LOCAL, key half: «a key only on the states below its level»: grepped verbatim in the landed R105 statement (1 hit). It is used at
  SEG (iii) and SEG-ONCE; the key half is exactly what is needed there (keys of x read only s at levels < lev(x); this also follows from
  §0's recursive key definition). No other R105 item, no U / CHAIN-BACK / E-2, no R106 / R107, no docs/lit: confirmed by reading every
  proof step.

## Proof check, step by step
### SEG (hyp.: IDEAL-ACYC, any degree; l ≥ −1; [a, b] ⊆ [1, T] with no level-≤-l mover in Mv_t, t ∈ [a, b])
- H is an IDEAL-ACYC genome: options of H are options of G (ranks, gates distinct; W-targets one level down; Ξ-graph a subgraph). ✓
  Its start is s_(a−1) (frozen movers at their only option). ✓
- Induction: at s = s_(t−1) every frozen mover is at its frozen option (no level-≤-l move in [a, t − 1]). ✓
- (i) For non-frozen x, the chain of (x, k) under s is the same option sequence in H and G (a frozen y contributes (y, s(y)), its only
  H-option), so the β-sets and A_s(x) agree. ✓ (ii) A^H_s is a singleton for frozen movers. ✓
- (iii) Level by level: equal states below lev(x) ⇒ equal keys (LOCAL key half; H's options carry the same W-targets and gates). A
  frozen x keeps its option = s_t(x) (t ∈ [a, b]); a non-frozen x picks the key-least of the same A under the same keys = s_t(x). ✓
- (iv) Stop tests: Mv_t ≠ ∅ contains no frozen mover, and a mover that moves has |A^G_s| ≥ 2, so some non-frozen mover has
  |A^G_s| ≥ 2 = |A^H_s| by (i): H passes the singleton test. H's new state = s′ ≠ s: H passes the no-change test. ✓ (The packet's
  «some non-frozen mover has |A^G_s| ≥ 2» is justified by exactly this.)
- Holds for ANY interval satisfying the hypothesis (not only maximal ones): my tool checks every sub-interval.
### SEG-ONCE (hyp.: degree ≤ 2)
- Two consecutive moves t1 < t2 of x (level l + 1) in [a, b]: degree 2, b′ → a′ → b′. x ∈ Mv_t ⇒ A_(s_(t−1))(x) = both options ⇒
  s_t(x) = KP_(s_t)(x) (§0; the step uses keys under s_t). ✓ s_(t1) and s_(t2) agree on all levels ≤ l (steps t1 + 1, …, t2 ∈ [a, b]),
  so KP equal (LOCAL key half), a′ = b′: contradiction. ✓ l = −1: level-0 keys are single gates, constant: each level-0 mover moves at
  most once. ✓
### LEVEL-PRODUCT (hyp.: degree ≤ 2)
- Steps counted by C_l cut [1, T] into ≤ C_l + 1 maximal intervals, each satisfying SEG's hypothesis for l. ✓ A step counted by
  C_(l+1) and not C_l moves a level-(l + 1) mover, of degree 2. ✓ Each interval holds ≤ n_(l+1) such steps (each moves ≥ 1 of the
  n_(l+1) movers, each mover ≤ once by SEG-ONCE). ✓ C_(l+1) ≤ C_l + (C_l + 1) n_(l+1). ✓ Levels are contiguous (W-targets one level
  down), T = C_top, C_(−1) + 1 = 1: T + 1 ≤ Π (n_l + 1). ✓ Ladder: 3^d. ✓ Remark (not to sign): n + 1 ≤ 2^n with equality iff n ≤ 1. ✓
### DEAD REPLAY
- Precise form (§4) checked as a statement: maximal interval [a, b] with no level-0 move and a ≥ 2; every s_t, t ∈ [a, b], equal above
  level 0 to some s_j, j < a. It is implied by the proposal «the next segment is a sub-run of a segment already seen» when states are
  compared above level 0, so killing it kills the proposal in that reading. ✓
- Instance checks (own code): acyclic; 5-level 2-wide ladder, N 10, every mover degree 2.
- My simulator (written from R104's text, β-SETS) from the stored start [0, 0, 1, 1, 0, 0, 0, 0, 1, 0]: T 15 and states s_0 … s_15
  IDENTICAL to packet §4 (all 16 compared); Mv: [5], [9], [7], [6, 8], [9], [4], [0, 2, 3], [1], [4], [6, 7, 8, 9], [5], [3], [7], [6, 9],
  [4]. Level-0 moves only at 7, 8; interval [9, 15]; new above level 0 at t = 9, 10, …, 15 (7 of 7) = lane «NEWSTATES 7». s_9 above
  level 0 = (0 0 0 1 1 1 0 0), not among s_0 … s_8. REPLAY FAILS at t = 9. ✓ [1, 6] has a = 1 and is outside REPLAY (packet correct).
- §4 «Does NOT claim» parenthetical: «repetition of mover sets, which does occur in max_d4_L13»: TRUE (my run: (3,) ×2, (6,) ×4, (4, 7)
  ×2, (2,) ×2; the block (3), (6), (4, 7), (6), (2) recurs at steps 9-13).

## Machine checks
- Lane blocks re-run at 8291ecf7 (worktree, experiments/new, check.sh lines 873-887 = w106, w107, pin107), 12:16Z: both PASS, exit 0.
  Output: «SEGCHECK runs 59 steps 650 intervals 652 SEG 0 ONCE 0 COUNT 0 PROD 0 maxratio 0.3333», «… runs 34934 steps 38676 intervals
  57755 … maxratio 1.0», BADLEV=2 «ONCE 112», seg.py «N 10 T 15 L 0 cuts [7, 8]», «seg t9-15 len 7 NEWSTATES 7 REPLAY False», pins
  7fa84784 / a18f6f0c.
- Own tool docs/referee-2/R2-P-IDEAL-SEG/seg_check.py (my simulator; H built by my own freeze(); lane restrict()/segcheck not imported).
  Checks SEG on EVERY sub-interval of every maximal interval (lane: maximal only), ONCE, COUNT, PROD, the ladder bound, T = C_top and
  #intervals ≤ C_l + 1.
  - Corpus (the same 59 files): runs 59, steps 650, intervals 652 (= lane), 12,175 sub-intervals; 0 violations. BADLEV=2: ONCE 112 (= lane).
  - box150/out/rand, every start for N ≤ 8 (maximal intervals): runs 34,934, steps 38,676, intervals 57,755 (= lane); 0 violations.
  - Random ladder genomes degree 2 (all starts N ≤ 7; 3,000 more N ≤ 12): 18,584 runs, 694 2-wide ladders; degree 3 (SEG only):
    55,964 runs, 91,682 sub-intervals; climbs on 60 degree-3/4 genomes: 18,060 runs; climbs of T on the 55 degree-2 box-14x/15x corpus genomes (4 seeds × 150
    mutations, maximal intervals): 33,220 runs, 240,850 intervals, max T 27, ladder ratio (T + 1) / 3^d at most 0.4545. All 0 violations.
- F-1 (packet §5 DATA remark, not to sign, not in the line): «Largest (T + 1) / Π (n_l + 1): … 1 on the random runs (reached only by
  genomes with one degree-2 mover)» is not exact: box150/out/rand/r150_049.json has degree ≤ 2 and NO degree-2 mover (T 0, Π 1, ratio
  1). My max ratio on box150 rand by number of degree-2 movers: {0: 1.0, 1: 1.0, 2: 0.6667, …}. (In my own random sets ratio 1 also
  occurs with 2 degree-2 movers on different levels: n = (1, 1), T 3.) A fixes-file correction suffices.
- F-2 (packet §4, not in the line): the quoted proposal «after a level-0 reset the next segment is a sub-run of a segment already seen
  (no new states above)» is not verbatim to its stated source docs/new/N5-SEG-box157.md l. 24 («after a level-0 reset, the next segment
  is a sub-run of a segment already seen»): comma missing and «(no new states above)» added inside the guillemets. The killed statement
  is the explicit precise form, so nothing changes.

## TARGET.md diff
- TARGET §2 (M4): a deterministic algorithm solving every parity game within p(n + m) steps. No statement here mentions a parity game,
  an algorithm or running time; all concern IDEAL-model step sequences. LEVEL-PRODUCT is an exponential bound inside the model, not a
  claim about any algorithm. No M4 / M3 claim, no gauntlet step. G-N5-TIME OPEN. The packet's §5 diff is correct.

## Line L-1: clause by clause, every definition against the packet
- Premise: «R104's definition of the model only, no theorem of R104 used; and RESULTS R105's LOCAL, key half only» = packet premises. ✓
- «on acyclic Ξ-graphs, any number of movers per level» = IDEAL-ACYC, no width hypothesis. ✓
- Definitions: «N movers» ✓; «T the number of steps of a run from a given start» = §0 T ✓; «Mv_t the movers of step t» = §0 ✓;
  «C_l the number of steps whose movers include one of level at most l (C_(−1) := 0)» = §3 C_l (steps of [1, T]) ✓; «n_l the number of
  movers of level l with two options» = §3 n_l (degree-2 movers) ✓.
- SEG «at any degree, if no step of an interval [a, b] of steps moves a mover of level at most l, then the genome in which every mover
  of level at most l keeps only its option at s_(a−1) runs from s_(a−1) through exactly the states s_(a−1), …, s_b first» = §1 ✓ (l ≥ −1
  implicit; any l works).
- SEG-ONCE (degree ≤ 2) «on such an interval every mover of level l + 1 moves at most once, so every level-0 mover moves at most once in
  a whole run» = §2 ✓.
- LEVEL-PRODUCT «C_(l+1) + 1 ≤ (C_l + 1)(n_(l+1) + 1) for every l ≥ −1, hence T + 1 ≤ the product over all levels l of (n_l + 1), and
  T ≤ 3^d − 1 on a d-level ladder with two movers of degree 2 per level» = §3 ✓; ladder definition: P-1.
- DEAD «REPLAY («in every degree-≤-2 IDEAL-ACYC run, every state inside a maximal interval of steps without a level-0 move that follows
  a level-0 move agrees on all movers of level ≥ 1 with some state before that interval») is false, by L-RED R202's 5-level 2-wide
  ladder max_d5_L15 from its stored start (N 10, T 15; level-0 moves only at steps 7 and 8; s_9 is new above level 0; sha1 ba963ace…)»
  = §4 precise form («follows a level-0 move» = a ≥ 2 with step a − 1 a level-0 move; «before that interval» = j < a) and numbers ✓.
  L43: universal finite statement killed by an explicit instance with its numbers. ✓
- Scope tail = §1-§5 «Does NOT claim» and §5 ✓. DATA «59 corpus runs with 652 intervals», «34,934 random runs (every start for N ≤ 8,
  the genome start otherwise) with 57,755 intervals», segcheck.py ✓ (reproduced). Provenance ✓.
### Optional
- P-1: ladder «with two movers of degree 2 per level» → «with exactly two movers per level, both of degree 2» (packet §0 definition;
  the line's wording also admits extra degree-1 movers, for which the bound still holds since n_l = 2, so this is precision only).
- P-2: SEG «of level at most l» → add «(l ≥ −1)» once.
- P-3: the REPLAY text in «…» is the line's own paraphrase of §4's precise form, not a quote; guillemets could be dropped.
- P-4: DATA: «0 violations … (at degree 3 only SEG is checked)», as packet §5 says.

## Signatures
All four statements: SIGN (Opus 5.5, D12), REFEREE-2 successor 27, 2026-11-04 (date -u stamp in the header). Gaps: none. Line L-1: MATCHES.
