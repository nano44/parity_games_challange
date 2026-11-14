# R207 Lower bounds for T*(d) and T^R(d), d 5-10, by construction plus simulation; Lemma TOP-ADD (L-RED successor 50)
Started 2026-11-05 22:1xZ (date -u). Lead BOX R207 (brief to successor 50). Model: IDEAL-ACYC (RESULTS R104), degree ≤ 2.
- 𝓛_d (RESULTS R109): levels 0..d−1, exactly two two-option movers per level, any number of one-option ("aux") movers; T*(d) = max T.
- 𝓛^R_d (RESULTS R110): the R197 2-wide ladder; T^R(d) = max T, and T^R(d) ≤ T*(d).
Labels: DATA (replayed witnesses; lower bounds only, nothing exact), PROVED (lane, unrefereed), READING. Not a TARGET.md claim.
G-N5-TIME stays OPEN. No SAT is used in this file.

## 0. Answers
- Best lower bounds found (every row is a replayed witness, §2):

  | d | T^R(d) ≥ | T*(d) ≥ | T* witness (N = two-option + aux) | segments [seg1, mid, tail] | top-pair flips (F, |W|) | max pair flips (F, |W|) |
  | --- | --- | --- | --- | --- | --- | --- |
  | 4 | 13 (exact, R197) | 13 (2 aux climbs, no gain) | — | — | — | — |
  | 5 | 15 (R202) | **17** | Tstar_d5_T17 (10 + 10) | [6, 3, 6] | (4, 13) | (7, 9) |
  | 6 | 18 | **25** | Tstar_d6_T25 (12 + 12) | [12, 0, 11] | (4, 18) | (9, 13) |
  | 7 | 20 | **31** | Tstar_d7_T31 (14 + 14) | [16, 0, 13] | (11, 19) | (11, 18) |
  | 8 | — | **33** | Tstar_d8_T33 (16 + 16) | [9, 8, 14] | (5, 26) | (5, 18) |
  | 9 | — | **42** | Tstar_d9_T42 (18 + 18) | [12, 9, 19] | (7, 22) | (10, 20) |
  | 10 | — | **46** | Tstar_d10_T46 (20 + 20) | [13, 11, 20] | (5, 24) | (13, 20) (aux pair) |

  - Status of the bounds: they are lower bounds from hill climbs, not maxima.
  - T*(5) ≥ 17 is above the ladder bound T^R(5) ≥ 15, at the same depth.
  - In the data, therefore, the helper (one-option) movers separate T* from T^R from d 5 on. Whether T^R(d) = T*(d) is the open item in
    RESULTS R110. This is DATA, not a proof: T^R(5) = 15 is not proved, and the conditional d 5 T ≥ 16 cube run is still going.
  - With helpers, d 4 stays at 13 (two climbs, AUX 2 and 3). This is consistent with T*(4) = 13.
- Growth: T* rises by +4, +8, +6, +2, +9, +4 per added level (d 4 → 10), 33 over 6 levels, about 5.5 per level. The increments do not grow. T^R rises by +2, +3, +2 (d 5 → 7).
  - In both, growth is LINEAR or slower. There is no superlinear signal.
  - This supports SLOT-TRADE (T*(d) ≤ T*(d − 1) + O(d)), as DATA only.
  - The SANDWICH ceiling 3T*(d − 1) + 2 is never approached. The best ratio is 25 / 17 ≈ 1.47.
- Top-pair flips against |W| (L-NEW's box168/pairflips.py and my own diag.py agree on every file):
  - The run-length champions keep flips ≤ |W| at every level.
  - The only pair with flips > |W| is still the dd clock's level-3 pair: 14 flips at |W| 8 (dd_d5_F14).
  - A flip-maximising climb (SCORE=FL, ladders, d 6, seeded by dd_d5_F14) found no pair above 14. Its added levels flip ≤ 7.
  - So no slope > 2 appears and PAIR-LIN is not refuted. By CASCADE, F ≤ T, so flips cannot outgrow T.
- Where and why growth stops (§1, §3):
  - (a) TOP-ADD (PROVED, lane; §1). A new top level that no lower option's Ξ-chain reaches adds at most 2 steps. It adds no Ξ capacity
    to the old levels. Pure top extensions therefore saturate. In the data, even Ξ-coupled top extensions gain little (T*: 31 → 32 at d 8). Growth needs either Ξ-coupling
    of old options through the new movers, or re-routing the whole genome.
  - (b) Bottom insertion (R109 LIFT) keeps T. Gains then need the run to continue after the level-0 steps. Climbs that change only
    levels ≤ 1 of a lifted champion gain little (d 6: 17 → 20; d 7: 25 → 26). The second segment needs the frozen upper genome to run
    long under the other level-0 bit (R110 W-ONLY: T ≤ T_2(d − 1) + 2). That is a property of the whole upper genome, not of the
    bottom.
  - (c) The best witnesses replay. In Tstar_d6_T25 the 11 tail steps repeat seg1's steps 2-12 almost move for move (§3). At d 7 and
    d 8 the replay does not compound: seg1 + tail ≈ T*(d − 1) + a few.
  - READING: what limits these constructions is saturated steps (no step without a lower move can be added except at the ends, SEG-ONCE
    / TOP-ADD), not Ξ capacity. At d 6-8 the helper movers give Ξ capacity freely (12-16 aux movers), and T still grows linearly.

## 1. Lemma TOP-ADD (PROVED, lane; unrefereed)
Statement. Let G be an IDEAL-ACYC genome of degree ≤ 2 with top level d − 1. Let U be its level-(d − 1) movers. Assume no option of a
mover outside U has its Ξ-target in U. Let G − U be the genome on the other movers, with the same start. Then the steps 1..T(G − U)
of G's run move exactly the movers of the corresponding steps of the run of G − U, plus possibly movers of U. Hence
T(G) ≤ T(G − U) + #{two-option movers in U} (≤ T(G − U) + 2 in 𝓛_d).

Proof.
1. Outside movers depend only on outside movers:
   - The key of an outside mover x uses only the W-chain below x. That chain lies outside U, since W-targets point one level down.
   - The Ξ-value of an outside option is the β-set of its Ξ-chain. By assumption and induction along the chain, the chain stays
     outside U.
   - So availability A(x), and the key-least choice, depend only on the outside part of the state.
2. Matching phase. By induction on t, the outside part of G's state s_t equals G − U's state for t ≤ T(G − U). Each such step changes
   some outside mover, so G's run does not stop before T(G − U).
3. Tail.
   - After T(G − U), the outside part has stopped: either nothing is available, or the key-least choice is the current option. No
     outside mover moves again.
   - The remaining steps lie in an interval with no move at levels ≤ d − 2.
   - By R109 SEG-ONCE (degree ≤ 2; «on an interval of steps without a move at levels ≤ l … every mover of level l + 1 moves at most
     once in it»), each mover of U moves at most once there.
   - Every step moves at least one mover, so the tail has at most #{two-option movers in U} steps. ∎
DATA check (r207/topadd_ck.py): random genomes of 𝓛_d (AUX 2, free W) with the hypothesis forced (lower Ξ-targets into U redirected
to X), comparing G's run off U with the run of G − U. d 5: 500 genomes, 0 violations, gains {0: 475, 1: 25}. d 6: 300 genomes,
0 violations, gains {0: 292, 1: 8}.
CORRECTION (same session, before commit): the d 8 top extension (31 → 32) does NOT satisfy the hypothesis. Its genome has 2 lower
options with Ξ-target in the top level, and Tstar_d7_T31 has 3. So it is not an instance of the lemma. The climbs reach Ξ-coupling
anyway, and it still gave only +1.

## 2. Witnesses and replays (experiments/red/r207/keep/)
- Files: Tstar_d5_T17, Tstar_d6_T25, Tstar_d7_T31, Tstar_d8_T33, Tstar_d9_T42, Tstar_d10_T46 (𝓛_d: movers 2l, 2l + 1 are the two-option movers of level l; the
  aux movers follow); TR_d6_T18, TR_d7_T20 (𝓛^R_d, R197 convention checked).
- Replay of every file:
  - r187/ideal.py (reference) and r207/lscore.py.
  - L-NEW box150/check.py (own simulator plus box139/paths.py, XSIM 0; all 13 lemma counters 0).
  - L-NEW box166/verify_kill.py: well-formed (W-target exactly one level down, distinct gates, distinct ranks, acyclic Ξ).
  - r189/lemck.py on the realised N5 game (Theorem REALIZE: L-SBAR, L-TAU, L-ESC, L-W, L-AV, KEY, FB): 0 violations on d 5-8 and
    TR_d6. So these are real FL runs of N5 of length 17, 25, 31, 33 and 18, from the stated start pairs (R104 Corollary REAL-IDEAL: «from
    the stated start pairs», «nothing about N5's default start S3»).
  - r207/allstarts.py (all 2^(2d) starts): the stored starts are optimal for d 5 and 6 (max T 17, 25; TR_d6 18).

## 3. Mechanism note (DATA, Tstar_d6_T25)
Movers per step (mover@level):
- seg1, steps 1-12: 4@2 9@4 | 11@5 | 7@3 8@4 | 10@5 | 3@1 5@2 | 10@5 | 9@4 | 7@3 11@5 | 6@3 8@4 | 9@4 | 4@2 | 11@5.
- Level-0 steps 13-14: 0@0 2@1 3@1 | 1@0 5@2.
- Tail, steps 15-25: 4@2 6@3 | 7@3 8@4 | 10@5 | 3@1 5@2 | 10@5 | 9@4 | 7@3 11@5 | 6@3 8@4 | 9@4 | 4@2 | 11@5.
- Steps 18-25 equal steps 5-12 exactly. The replay is one copy, not a recursion: at d 7 the tail (13) is below seg1 (16).

## 4. Tools (experiments/red/r207/)
- gclimb.py: climber over 𝓛_d / 𝓛^R_d.
  - AUX: helpers per level. WFREE: free W-targets one level down. SEED: start genome. LIFT: R109 LIFT of the seed.
  - MAXLEV: option-local mutations only at levels ≤ MAXLEV.
  - SCORE: T, or FL / FTOP for flips.
- diag.py: segments, moves, C_l, pair flips vs |W|.
- lscore.py, allstarts.py, stage.sh.
- Climb logs are in r207/out/ (not committed).

## 5. Frozen intervals I / L (Lead 22:52Z add-on; L-NEW box 171 frozen.py @ claude/l-new 2afbb491, run read-only, unmodified)
- Definitions (box 171): a step is LOWER if some mover below the top level moves; otherwise it is TOP-ONLY. L = #lower steps.
  I = #maximal runs of top-only steps.

  | file | d | T | L | top-only | I | max run | I / L | pattern (L lower, T top-only) |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | dd_d5_F14 | 5 | 14 | 14 | 0 | 0 | 0 | 0 | all L |
  | max_d5_L15 | 5 | 15 | 13 | 2 | 2 | 1 | 0.15 | LTLLTLLLLLLLLLL |
  | Tstar_d5_T17 | 5 | 17 | 17 | 0 | 0 | 0 | 0 | all L |
  | TR_d6_T18 | 6 | 18 | 15 | 3 | 3 | 1 | 0.20 | LLLLLLLLTLTLLLLLLT |
  | Tstar_d6_T25 | 6 | 25 | 18 | 7 | 7 | 1 | 0.39 | LTLTLTLLLLLTLLLLTLTLLLLLT |
  | TR_d7_T20 | 7 | 20 | 17 | 3 | 3 | 1 | 0.18 | LLLLLLTLLLLLLLLTLLLT |
  | Tstar_d7_T31 | 7 | 31 | 25 | 6 | 3 | 2 | 0.12 | LLTTLLLLLLLLLLTTLLLLLLLLLLLLLTT |
  | Tstar_d8_T33 | 8 | 33 | 27 | 6 | 3 | 2 | 0.11 | LLTTLLLLLLLLLLLTTLLLLLLLLLLLLLLTT |
  | Tstar_d9_T42 | 9 | 42 | 34 | 8 | 4 | 2 | 0.12 | LLLLLTTLLLLLLLLLLLLTTLLLLLLTTLLLLLLLLLLLTT |
  | Tstar_d10_T46 | 10 | 46 | 44 | 2 | 2 | 1 | 0.05 | LLTL…LTL… (2 isolated top-only steps) |

- Where I sits against d + 1:
  - I ≤ d + 1 on every file.
  - The largest ratio is I / L = 0.39 (Tstar_d6_T25, I 7 = d + 1).
  - At d 7-10, I is 2-4 and stays well below L / 2.
- So no extremal file shows I ≈ L / 2 (DATA, lower-bound constructions only). The O(d) form of SLOT-TRADE survives these files.
- T(H) is «None» on every file. Every witness has a lower option whose Ξ-target lies in the top level, so none is autonomous. This
  matches §1: the top levels gain mainly through Ξ-coupling, not through top-only steps (top-only ≤ 8 of 42 at d 9).
