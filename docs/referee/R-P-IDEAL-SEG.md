# R-P-IDEAL-SEG: REFEREE report on P-IDEAL-SEG (L-NEW successor 51, box 157)
REFEREE successor 23 (Opus 5.5, D15), 2026-11-04T12:17Z by date -u. Independent: I did not read docs/referee-2/.
- Object: claude/l-new 8291ecf7, an ancestor of origin/claude/l-new. I re-measured all three files:
  - docs/new/P-IDEAL-SEG.md: sha1 7fa847843cb950e87dac38bf3d612effd5a9834e, 152 lines;
  - docs/new/P-IDEAL-SEG-line-L1.txt: sha1 a18f6f0c61d6d5f33adc61519d94252dd5ba9721, 1 line, no «|»;
  - experiments/new/box157/max_d5_L15.json: sha1 ba963aceabeb35d95f9c47d80d1d0e87b87baf21. This equals L-RED's
    experiments/red/r202/max_d5_L15.json at 05c48415 and at the l-red head.

## 0. Verdicts
| § | statement | verdict |
| --- | --- | --- |
| §1 | Lemma SEG (any degree) | SIGN |
| §2 | Lemma SEG-ONCE (degree ≤ 2) | SIGN |
| §3 | Corollary LEVEL-PRODUCT (degree ≤ 2), with the ladder form T ≤ 3^d − 1 | SIGN |
| §4 | DEAD: REPLAY (precise form), instance max_d5_L15 | SIGN (recomputed independently) |
| §5 | machine check, exclusions, TARGET diff | not to sign; w106, w107 and pin107 MATCH; diff agreed |
| line | L-1 | MATCHES (definition diff done; one optional precision SEG-L1) |
- Labels.
  - PROVED (lane + REFEREE): SEG, SEG-ONCE, LEVEL-PRODUCT. LEVEL-PRODUCT is an EXPONENTIAL bound.
  - DEAD (instance): REPLAY.
  - Nothing is bounded polynomially. G-N5-TIME OPEN.

## 1. Premise route
- Premises:
  - RESULTS R104's definition. §0 restates it, and the restatement agrees clause by clause with R104 and with R105 §0.
  - RESULTS R105 LOCAL, key half: «a key only on the states below its level». It is FOUND verbatim in the landed R105 line on trunk
    18c288c6 (grep -F: 1 hit).
  - The key half is all that is used: in SEG (iii), SEG-ONCE, and (through SEG-ONCE) LEVEL-PRODUCT.
- SEG (i) does not use LOCAL. It argues directly that chains are the same option sequence in H and G, because a frozen y contributes
  (y, s(y)), its only H-option. That is correct, so no value half of LOCAL is needed (the M2-G1 trap does not arise).
- U, CHAIN-BACK and CHAINED are not used. I grepped the proofs and found no use. So R105's erratum E-1 does not touch this packet.
  - The erratum is drafted for C119 (trunk d08df7c8). It is not yet in docs/RESULTS.md at 18c288c6.
- No docs/lit, no docs/sources, no R106 or R107.

## 2. Proof checks
- SEG: SIGN.
  - H is an IDEAL-ACYC genome: its options are a subset of G's, and its Ξ-graph is a subgraph of G's.
  - Induction over t ∈ [a, b]. Frozen movers sit on their frozen options, since none moved in [a, t − 1].
    - (i): non-frozen chains are the same option sequence, so A^H = A^G.
    - (ii): frozen movers have A^H a singleton.
    - (iii): level by level, keys are equal by LOCAL's key half. Frozen movers keep their option (= s′, since t ∈ [a, b]). Non-frozen
      movers take the key-least of the same set.
    - (iv): s′ ≠ s forces a non-frozen mover with |A| ≥ 2, so H passes both stop tests.
  - Correct. The «b − a + 2 states / ≥ b − a + 1 steps» count is right.
- SEG-ONCE: SIGN.
  - Two moves of a level-(l + 1) degree-2 mover inside [a, b] go b′ → a′ → b′.
  - §0's «x ∈ Mv_t ⇒ s_t(x) = KP_(s_t)(x)» holds: both options are in A (current + strictly better), and the key-least is taken.
  - KP reads only levels ≤ l, and those do not move in [a, b]. So KP_(s_t1) = KP_(s_t2), which gives a′ = b′, a contradiction.
  - l = −1 gives the whole-run form for level 0.
- LEVEL-PRODUCT: SIGN.
  - The steps counted by C_l cut [1, T] into ≤ C_l + 1 maximal (possibly empty) intervals.
  - A step counted by C_(l+1) but not by C_l moves a level-(l + 1) mover, of degree 2.
  - SEG-ONCE allows each of the n_(l+1) such movers at most once per interval. So C_(l+1) ≤ C_l + (C_l + 1) n_(l+1).
  - T = C_top, and induction from C_(−1) + 1 = 1 gives the product. The ladder gives 3^d.
  - The Remark (Π(n + 1) ≤ 2^Σn; n + 1 ≤ 2^n with equality iff n ≤ 1) is correct, and it is not to sign.
- DEAD REPLAY: SIGN.
  - The packet's precise form is «every s_t, t ∈ [a, b], agrees above level 0 with some s_j, j < a». It is IMPLIED by the lane
    proposal (docs/new/N5-SEG-box157.md l. 24: «after a level-0 reset, the next segment is a sub-run of a segment already seen»): a
    sub-run only revisits states already seen above level 0.
  - So refuting the precise form refutes the proposal.
- Own recomputation (scratch/xinew_probe.py, my β-set simulator written from R104's text) on max_d5_L15 from its stored start
  [0, 0, 1, 1, 0, 0, 0, 0, 1, 0]:
  - The genome is valid: acyclic (DFS); every W-target exactly one level down; ranks and gates distinct; levels [0, 0, 1, 1, 2, 2, 3, 3,
    4, 4]; degree 2 everywhere. So it is a 5-level 2-wide ladder.
  - T = 15. The states s_0 … s_15 EQUAL the packet's §4 list, state for state.
  - Level-0 moves at steps 7 and 8 only, so the interval is [9, 15].
  - All seven states s_9 … s_15 are new above level 0 (none equals any s_j, j ≤ 8, on movers 2..9). REPLAY fails at t = 9.
  - LEVEL-PRODUCT on this run: T + 1 = 16 ≤ 3^5 = 243.

## 3. Machine checks at 8291ecf7 (detached worktree)
- w106 (three segcheck.py runs). The output equals check.sh's three expected strings verbatim:
  - corpus 59 runs / 652 intervals, all 0;
  - random 34,934 runs / 57,755 intervals, all 0, maxratio 1.0;
  - BADLEV=2 control: ONCE 112.
- w107 (seg.py): «max_d5_L15.json N 10 T 15 L 0 cuts [7, 8]», «seg t1-6 len 6 NEWSTATES 6 REPLAY False», «seg t9-15 len 7 NEWSTATES 7
  REPLAY False». These are the expected strings.
- pin107: packet 7fa84784, L-1 a18f6f0c and instance ba963ace all EQUAL.
- Own probe: scratch/seg_probe.py on my simulator; log xinew_logs/seg_probe.txt.
  - 6,000 random degree-≤-2 runs (seeds 1, 2): SEG-ONCE per maximal interval and every level 0, LEVEL-PRODUCT per level 0, PROD 0.
  - Control (ONCE tested at level l + 2), seed 3: 1 violation.
  - My random runs are short (T ≤ 4), so this DATA is weak. The packet's corpus (max T 15 to 26) and the proofs carry the signatures.

## 4. Diff against TARGET.md
- No statement concerns parity games, winning regions, running time or the cost model (TARGET §1-§3). Each is about R104's IDEAL model.
- LEVEL-PRODUCT is exponential and is labelled so. The DEAD item refutes a lane conjecture about the model.
- Agreed with §5: not M4, not M3, not a gauntlet step. G-N5-TIME OPEN.

## 5. Line L-1 (with the new rule: every DEFINITION diffed against the packet)
- Definitions:
  - «N movers» (§0) ✓;
  - «T the number of steps of a run from a given start» (§0) ✓;
  - «Mv_t the movers of step t» (§0) ✓;
  - «C_l the number of steps whose movers include one of level at most l (C_(−1) := 0)» (§3) ✓;
  - «n_l the number of movers of level l with two options» (§3 «degree-2 movers of level l») ✓;
  - «d-level ladder with two movers of degree 2 per level» (§0's 2-wide ladder: levels 0..d − 1, two movers per level, all of degree
    2) ✓. The line's form also admits extra degree-1 movers, and the bound still holds for them (n_l counts degree-2 movers only);
  - REPLAY's quoted form equals §4: «inside a maximal interval … that follows a level-0 move» = [a, b] with a ≥ 2; «before that
    interval» = j < a ✓.
    - A stricter reading of «before» (j < a − 1) gives a STRONGER conjecture, which the same instance also kills.
- Claims:
  - SEG, with the «keeps only its option at s_(a−1)» restriction and «exactly the states s_(a−1), …, s_b first»;
  - SEG-ONCE with the level-0 corollary;
  - LEVEL-PRODUCT, all three forms;
  - DEAD with its instance data (N 10, T 15, steps 7 and 8, s_9 new, sha1).
  All MATCH the packet.
- Scope: degree split (SEG any degree; SEG-ONCE and LEVEL-PRODUCT degree ≤ 2), acyclic, premises (LOCAL key half only), tail, DATA
  (numbers equal to my w106 re-run). All MATCH.
- OPTIONAL SEG-L1: SEG's «level at most l» leaves l unbound in the line. The packet has l ≥ −1, and the level-0 corollary uses
  l = −1. Suggest «… a mover of level at most l (l ≥ −1) …».
- VERDICT: line L-1 MATCHES.

## DONE / FINDINGS / NEEDS
- DONE:
  - this report;
  - w106, w107 and pin107 re-run at 8291ecf7: MATCH;
  - the instance recomputed independently: T 15, states equal, REPLAY fails at t = 9;
  - line definitions diffed one by one.
- FINDINGS:
  - SEG, SEG-ONCE, LEVEL-PRODUCT and DEAD REPLAY: all SIGN, no gap.
  - Line L-1 MATCHES; optional SEG-L1.
  - The packet uses only LOCAL's key half, so it is unaffected by R105 E-1.
- NEEDS: none. Optional SEG-L1 is at the Lead's discretion.
