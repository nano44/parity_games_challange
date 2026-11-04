# R2-P-IDEAL-SLOT: second-referee report on packet P-IDEAL-SLOT (L-NEW successor 51, box 158)
REFEREE-2 successor 27 (Opus 5.5, D12/D19). Written 2026-11-04 13:16Z (date -u). Independent: docs/referee/ not read for this packet
before this push.

## Object
- claude/l-new e46e98a4. docs/new/P-IDEAL-SLOT.md sha1 62901b5f951598fb44426942b0fb1d999325625a, 192 lines;
  docs/new/P-IDEAL-SLOT-line-L1.txt sha1 17236fb18d70c1e2968689108a74a1acac938bd5, 1 line, 0 «|»;
  experiments/new/box158/lift_max_d4_L13.json sha1 33fec48f1a8f1c57891b7574d87cc6bbe5e3bd38 (no trailing newline). Re-hashed with
  git show e46e98a4:FILE | sha1sum: all match.

## Verdicts
| § | statement | verdict |
| --- | --- | --- |
| §1-§2 | SEG, SEG-ONCE (copies) | **SIGN** (Opus 5.5, D12): byte-identical to P-IDEAL-SEG 8291ecf7 §1-§2 (signed in R2-P-IDEAL-SEG.md) |
| §3 | Lemma SHIFT (any degree) | **SIGN** (Opus 5.5, D12) |
| §4 | Corollary SEG-CAP (𝓛_d, d ≥ 2) | **SIGN** (Opus 5.5, D12) |
| §5 | Lemma LIFT (any degree) | **SIGN** (Opus 5.5, D12) (precision N-1) |
| §5 | Corollary SANDWICH | **SIGN** (Opus 5.5, D12) |
| §6 | DEAD SEG1-2D by lift_max_d4_L13 | **SIGN** (Opus 5.5, D12): recomputed with my own simulator |
| line | L-1 | **REQUIRED** SL-L1 (LIFT construction), SL-L2 (scope of the SANDWICH remark in the DEAD clause); optional P-1 to P-3 |
Gaps: none.

## Premise route
- R104: §0 is byte-identical to P-IDEAL-SEG §0 (diffed: equal, 1,997 chars), which I checked against R104's text in R2-P-IDEAL-M2.md /
  R2-P-IDEAL-SEG.md. No R104 theorem used.
- R105 LOCAL key half «a key only on the states below its level»: verbatim in the landed R105 statement. Used only inside the copied
  SEG / SEG-ONCE. SHIFT and LIFT compute keys directly from §0's recursive key definition (no premise needed).
- P-IDEAL-SEG is not a premise (copied, so no landing dependency): correct. No R106 / R107, no docs/lit.
- §1-§2 copies: the SEG statement+proof block (2,061 chars) and the SEG-ONCE block (1,061 chars) are byte-identical to P-IDEAL-SEG
  (8291ecf7) §1-§2. My signatures there carry over.

## Proof check
### SHIFT (hyp.: every level-0 mover has degree 1; any degree, any width)
- Gates: g′ = g(w, k_w)·Γ + g(x, k) with 0 ≤ g(x, k) < Γ: injective in (g(w, k_w), g(x, k)); g(x, k) distinct over options ⇒ new gates
  distinct; new gate ≥ Γ if g(w, k_w) ≥ 1, else = own old gate, which no unchanged gate equals. ✓
- W-targets: old level-1 options none (new level 0), others still one level down; old level-0 movers stay at level 0 with no W-target. ✓
  Ξ-data unchanged ⇒ same Ξ-graph, values, A-sets. ✓
- Keys: for an option at old level l ≥ 1 the W-chain is o_0, …, o_l with o_0 the ONLY option of its mover (degree 1), so key^G =
  (g(o_0), g(o_1), …), key^(G↓) = (g′(o_1), g(o_2), …); same length for options of one mover; g′ order = lexicographic order of
  (g(o_0), g(o_1)). ✓ Old level-0 movers never move in either genome; old level-1 movers now at level 0 read no state for keys, so the
  level-by-level evaluation order is immaterial. Same choices, same stop tests. ✓
### SEG-CAP (𝓛_d, d ≥ 2)
- At most 2 level-0 steps (SEG-ONCE, l = −1; degree-1 movers never move); T = seg1 + mid + tail + #level-0 steps: checked in all three
  cases (0, 1, 2 level-0 steps). ✓
- Each count is an interval with no level-0 move; SEG (l = 0) gives H; H's level-0 movers all have degree 1 ⇒ SHIFT; H↓ ∈ 𝓛_(d−1)
  (old level 1 → level 0 with its two degree-2 movers; frozen old level-0 movers now degree 1 at level 0; levels 0..d − 2). ✓ Its run
  from s_(a−1) has ≥ b − a + 1 steps ⇒ ≤ T*(d − 1). ✓
- T* finite: T*(1) ≤ 2 (SEG-ONCE l = −1), then the SANDWICH upper bound, whose proof uses SEG-CAP at d, which needs only T*(d − 1). No
  circularity. ✓ (So «largest» in the line is a maximum.)
### LIFT (any degree)
- Validity ✓ (new ranks / gates above all; old level-0 options → A at level 0; A, B isolated in the Ξ-graph). A: Ξ(A, 0) ▷ Ξ(A, 1)
  (larger rank, even), so from option 0 A_s(A) = {0}: by induction from the start A, B stay at 0. ✓ Old chains never pass A, B. ✓
- Keys: every old option's W-chain ends at (A, s(A)); the first entry g(A, s(A)) is COMMON to all old keys under any state, so the
  order is G's. ✓
- N-1 (precision, not a gap): the packet says «under any state, the W-chain of an old option ends at (A, 0)»; that holds for states
  with s(A) = 0, which is every state of the run (A never moves). The argument needs only the common first entry, true under any state.
- The condition «every option of a mover of old level 0 gets W-target A» (one common new mover) is essential: with the old level-0
  movers split between A and B, A and B still never move, but the runs change (control below; explicit instance lift_split_ctrl.json).
### SANDWICH
- Upper: SEG-CAP + ≤ 2 level-0 steps. ✓ Lower: G ∈ 𝓛_(d−1) ⇒ G^ ∈ 𝓛_d (A, B the two degree-2 movers of the new level 0; old levels
  shift up with their movers and degrees). No level-0 step ⇒ seg1 = T(G^) = T(G). ✓ sup seg1 = T*(d − 1) by SEG-CAP. ✓ Remark: the
  upper recursion gives T*(d) + 1 ≤ 3 (T*(d − 1) + 1), T*(1) ≤ 2 ⇒ T*(d) ≤ 3^d − 1. ✓
### DEAD SEG1-2D
- Instance (own code): N 10, levels 0-4 with exactly 2 movers each, all degree 2 (a 2-wide degree-2 ladder, no degree-1 mover, in
  𝓛_5). Its fields are exactly LIFT's construction applied to max_d4_L13 (sha1 f0735b61): old movers 0-7 with identical Ξ-targets, β,
  ranks, parities, gates; old level-0 options → mover 8 (A); A = 8 and B = 9 with ranks (17, 16) / (19, 18), all even, larger on option 0,
  gates 16-19 above 15; start [1, 1, 0, 0, 0, 1, 0, 1, 0, 0].
- My simulator: T 13, no level-0 step, seg1 13 > 2·5 − 1 = 9; run on movers 0-7 = max_d4_L13's run state for state; my own LIFT of
  max_d4_L13 gives the same. SEG1-2D FALSE. ✓
- §6 DATA «largest seg1 3, 5, 6, 9, 10 at d = 3, 4, 5, 6, 8» on the genome-start corpus: reproduced exactly (54 𝓛_d files without box158;
  also d = 2: 1, d = 7: 5, d = 10: 0, d = 12: 1; all ≤ 2d − 1). ✓
- Negative remarks (§3-§6 «Does NOT claim») checked: all are non-claims or correct arithmetic.

## Machine checks
- Lane blocks re-run at e46e98a4 (worktree, experiments/new, check.sh l. 888-902: w108, w109, pin109), 13:13Z: both PASS, exit 0
  («LIFT … SAME True» ×3; lift_max_d4_L13 «d 5 T 13 cuts [] seg1 13»; box150 check «XSIM 0 TOPO 0 … VIOL 0»; pins 62901b5f / 17236fb1 /
  33fec48f).
- Own tool docs/referee-2/R2-P-IDEAL-SLOT/slot_check.py (my simulator; SHIFT, LIFT, freeze, 𝓛_d generator all my own):
  - SHIFT: 18,948 runs (random genomes with level 0 frozen to degree 1, degree ≤ 2 and ≤ 3, 4 starts each): 0 violations. Control
    (gate g(w) + g instead of g(w)·Γ + g): runs differ 1,766 times.
  - LIFT: 28,000 runs: 0 violations (old movers' run identical, A and B fixed). Control (old level-0 movers' W-targets split A / B, A and B
    still fixed): runs differ 4,984 times.
  - SEG-CAP chain (for every segment: freeze level 0 → H, SHIFT → H↓, check H↓ ∈ 𝓛_(d−1) and that its run reproduces the segment), T
    decomposition, ≤ 2 level-0 steps: random 𝓛_d (d ≤ 8, with 0-4 extra degree-1 movers, all starts for d ≤ 3) and the 57 𝓛_d corpus files
    (all starts N ≤ 8) plus T-climbs (2 seeds × 150): 38,444 runs, 37,312 segments, 0 violations. Largest seg1 seen at d = 5, 6: 13, 15
    (the lifted champions).
- Explicit LIFT control instance: docs/referee-2/R2-P-IDEAL-SLOT/lift_split_orig.json (sha1 14d8510e…), N 3, lev [0, 0, 1], T 0 from
  start [1, 0, 1]; lift_split_ctrl.json (sha1 3ab62fd8…): mover 0 → A, mover 1 → B: run [1,0,1,0,0] → [1,0,0,0,0], T 1 (mover 2's
  key order flips: (5, 3, 1) < (7, 0, 2)), A and B never move. The packet's LIFT (both → A) gives T 0.

## TARGET.md diff
- No statement mentions a parity game, an algorithm or running time; all concern IDEAL-model step sequences. SANDWICH is an exponential
  recursion inside the model. No M4 / M3 claim, no gauntlet step. G-N5-TIME OPEN. The packet's §7 diff is correct.

## Line L-1: clause by clause, every definition against the packet
- Premise ✓. «on acyclic Ξ-graphs» ✓. T ✓. 𝓛_d «the genomes with levels 0, …, d − 1, exactly two movers with two options on every
  level, any number of movers with one option and none with more than two» = §4 ✓. T*(d) «the largest T over 𝓛_d and all starts» = §4
  supremum, finite ✓.
- SEG / SEG-ONCE: = §1-§2 in substance (P-1).
- SHIFT: hypothesis «every level-0 mover has one option» ✓; «removing one level» = levels ≥ 1 lowered by 1 (P-2); «the former level-1
  options get no W-target and the gate g(w) · Γ + g, with w their old W-target's option and Γ above every gate» = §3 g′ ✓; «gives a
  genome with the same run from every start» ✓.
- SEG-CAP: three counts, d ≥ 2, ≤ T*(d − 1) = §4 ✓.
- LIFT: SL-L1. SANDWICH ✓ («largest number of steps before the first level-0 step over 𝓛_d equals T*(d − 1)» ✓, maxima exist).
- DEAD: SEG1-2D text in «» vs §6: drops «d ≥ 2» and «(no degree-1 movers)»; the latter is implied by «2-wide degree-2 ladder» (§0),
  the former is harmless (at d = 1 seg1 = 0). Instance data ✓. SL-L2 for the remark.
- Scope tail and DATA ✓ (lift.py / three.py on three lifted champions; segcheck 59 / 34,934 runs).
### REQUIRED
- SL-L1 (LIFT, the clause is false as worded under a natural reading). «(LIFT) at any degree, adding two never-moving level-0 movers with
  two options below a genome, one level up, gives the same run on the old movers» does not say that every old level-0 option gets the
  SAME new mover as W-target (nor how the new movers are made never-moving). With the old level-0 movers split between the two new
  movers, both new movers still never move but the run changes (lift_split_ctrl.json above: T 0 → 1). Replace by
  «(LIFT) at any degree, raising every level by one and adding two level-0 movers A, B with two options each (Ξ-target the exit, new
  even β-ranks above all, the larger on option 0, new gates above all, start at option 0), with A the W-target of every option of a
  former level-0 mover, gives a genome in which A and B never move and the run on the old movers is the same».
- SL-L2 (DEAD clause, scope). «and by SANDWICH any bound on that number in terms of d is a bound on T*(d − 1)»: «that number» is bound
  in the line to 2-wide degree-2 ladders (SEG1-2D's class), but SANDWICH gives the implication only for bounds over 𝓛_d (packet §6:
  «any bound seg1 ≤ f(d) on 𝓛_d implies T*(d − 1) ≤ f(d)»); a bound over degree-1-free ladders bounds only their own (d − 1)-sup,
  which is not known to equal T*(d − 1). Replace by «and by SANDWICH any bound on that number over 𝓛_d in terms of d is a bound on
  T*(d − 1)».
### Optional
- P-1: SEG «reproduces the interval» → «run from the state before the interval reproduces it» (the freeze is the same at s_(a−1) and s_a,
  but the start of the reproducing run is not stated).
- P-2: SHIFT «removing one level» → «lowering every level ≥ 1 by one (level-0 movers stay at level 0)».
- P-3: SEG1-2D «with d levels» → «with d ≥ 2 levels», as in §6.

## Signatures
All seven items (SEG, SEG-ONCE, SHIFT, SEG-CAP, LIFT, SANDWICH, DEAD SEG1-2D): SIGN (Opus 5.5, D12), REFEREE-2 successor 27,
2026-11-04 13:16Z (date -u). Gaps: none. Line L-1: REQUIRED SL-L1, SL-L2.
