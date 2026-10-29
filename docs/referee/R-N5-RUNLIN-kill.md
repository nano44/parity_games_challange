# R-N5-RUNLIN-kill: REFEREE confirmation of the RUN-LIN kill (L-SI, docs/si/N5-RUNLIN-box24.md §7 at l-si 90bcc50c)
Referee: REFEREE (successor 17), Opus 5.5 (owner ruling D15). Task: Lead message of 2026-10-29 00:20Z (date -u), a dead-end confirmation,
not a packet review. Runs 2026-10-29T00:23Z-00:25Z; written 00:25Z-00:26Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Inputs copied by `git show 90bcc50c:experiments/si/runlin/instances/<f>` into scratch/runlin_inputs/ (data files only): runfam_K10.pg
  sha1 faf218f125d1516d4677393991d53a08a9f4f3bb, .start 56e4dec67323e6f5b832ac2d95ef832d6ce3a013 (both = the Lead's pins); runfam_K40.pg
  287a185d…, .start bcbfeed3… (= §6's pins); runfam_K20, K60, K100 as committed. 90bcc50c is an ancestor of origin/claude/l-si.
- No lane code run or imported (mkrunfam.py, keeper.py, anatomy.py, allruns.py, n5x / n5b / n5.py, check_sol2 untouched).
- Tool: scratch/runlin_check.py (sha1 c30fd52d…): own engine rl_engine (SPEC S1-S5 + FIX 1-4), start parsing from scratch/core_probe.py;
  Oink 8fbf0a7 (tools/oink/build/oink, --zlk and --tl); an own winning-strategy check (closure + no cycle of the wrong parity in the
  strategy-restricted graph). Logs scratch/runlin_logs/ (k10_k40.txt, k10_wave.txt with the per-transition trace, k20_k60_k100.txt).

## Verdict
| item | verdict (Opus 5.5, D15) |
| --- | --- |
| (a) runfam_K10 reproduced: 101 states (100 iterations), phases [0, 0] and [1, 100], 0 fallbacks, one fallback-free run of 99 transitions > 2n = 98, I_τ = ∅ at every state, one Odd choice vertex (𝒞^1O) | REPRODUCED, every figure |
| (a) runfam_K40: 173 states, phases [0, 0], [1, 172], 0 fallbacks, run 171 = 2n + 13, I_τ = ∅ throughout | REPRODUCED |
| (b) Oink regions | AGREE with zlk AND tl on K10, K20, K40, K60, K100; N5's output strategies verified by my own check |
| (c) §7's obstruction description | FAIR as a READING, with two precisions (§3) |
| CONJECTURES RUN-LIN and RUN-LIN-OPT | DEAD, confirmed. Linearity is not touched (RUN-LIN′ open), as §7 says |

## 1. (a) The runs (scratch/runlin_logs/k10_k40.txt, k20_k60_k100.txt)
| instance | n | states | phases | fallbacks | longest fallback-free run | 2n | run − 2n | I_τ = ∅ at every state | σ̄ changes G | D ≠ ∅ (phase states) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| runfam_K10 | 49 | 101 | [0, 0], [1, 100] | 0 | 99 (states 1-100) | 98 | +1 | yes | 9 (at 1, 2, 4, 9, 30, 36, 39, 65, 66) | 65 of 100 |
| runfam_K20 | 59 | 126 | [0, 0], [1, 125] | 0 | 124 | 118 | +6 | yes | 9 | — |
| runfam_K40 | 79 | 173 | [0, 0], [1, 172] | 0 | 171 | 158 | +13 | yes | 9 | 107 of 172 |
| runfam_K60 | 99 | 213 | [0, 0], [1, 212] | 0 | 211 | 198 | +13 | yes | 9 | — |
| runfam_K100 | 139 | 293 | [0, 0], [1, 292] | 0 | 291 | 278 | +13 | yes | 9 | — |
- Every figure equals §7's table and text (K10: "[1, 100]", "D ≠ ∅ at 65 of the 100 states"; K40 run 171; K20 / K60 / K100 runs 124 / 211 / 291).
- Q = {5} (Odd, successors 2, 7, 9, 14, 18, 28; τ0(5) = 7), so every instance is in 𝒞^1O. The whole phase is fallback-free, so the 99
  transitions are one fallback-free run of one phase: RUN-LIN ("every fallback-free run of a phase has ≤ 2n transitions") is false at n = 49,
  and RUN-LIN-OPT with it (I_τ = ∅ throughout).
- σ̄-constant pieces (transitions strictly between σ̄ changes; §7 counts each piece together with the σ̄ change that closes it, so its
  numbers are mine + 1 except the last piece; both sum to the run): K10 0, 0, 1, 4, 20, 5, 2, 25, 0, 33 (+ 9 changes = 99) against §7's
  1, 1, 2, 5, 21, 6, 3, 26, 1, 33; K40 0, 0, 1, 4, 32, 5, 2, 55, 0, 63 against 1, 1, 2, 5, 33, 6, 3, 56, 1, 63. Same pieces.
- Growth: from K60 to K100 (+40 vertices) the two last pieces grow 75 → 115 and 83 → 123 (+40 each) and the third long piece stays 32, so
  run grows by 2 per vertex and run − 2n stays 13, as §7 says. Every piece is ≤ n − 1 (max 123 at n = 139).

## 2. (b) Correctness of the output
- Oink --zlk and --tl regions equal N5's S5 regions on all five instances (no zlk abort here; the counter_m trap does not apply).
- On every instance Even wins every vertex (W_Odd = ∅). σ on W_Even passes my check: W_Even closed under all Odd moves, and no cycle of the
  σ-restricted graph has an odd maximum priority. σ̄'s check is vacuous (W_Odd = ∅). This does not weaken the kill: RUN-LIN is about N5's
  run length on every game, and these runs are long whatever the winner is.

## 3. (c) The obstruction in §7, against my trace (runlin_logs/k10_wave.txt)
- The corridor: 28 ↔ 34 ↔ 37 ↔ 38 ↔ … ↔ 48 ↔ 25 is a two-way Even corridor (34, 37-48 are Even, priority 0, out-degree 2, one edge to each
  neighbour; 28 and 25 are its ends).
- The trace: inside each long σ̄-constant piece one Even vertex switches per transition (or two), and the switch moves one step along a chain.
  The corridor is walked four times, in alternating directions: t = 2-8 (37 → 34, 38 → 37, …, 43 → 42; partial), t = 22-29 (43 → 44, 42 → 43, …,
  34 → 37), t = 40-53 (34 → 28, 37 → 34, …, 48 → 47, 25 → 48; full) and t = 82-95 (25 → 21 at 82, then 48 → 25, 47 → 48, …, 34 → 37; full).
  The long pieces start right after gate changes (after 9, after 39, after 66), and the waves end at or just before the next one.
- So "run = Σ over σ̄-constant pieces, a piece is a wave along a corridor, and a σ̄ change restarts the wave" is a FAIR description, with two
  precisions:
  1. "one Odd gate whose options are the two ends of a two-way Even corridor" is not literal. Gate 5 has six options. Only 28 is a corridor
     end; the other end 25 is reached in one Even step from the options 2 and 9 (2 → 25, 9 → 25). The other options (7, 14, 18) are not at the
     corridor.
  2. The waves are not confined to the corridor. Pieces also run along other Even chains (t = 10-21: 26 → 14, 3 → 26, 36 → 3, 27 → 36,
     22 → 27, 16 → 22, 11 → 16, 4 → 11, 0 → 4, 33 → 0, 1 → 33, 21 → 1; t = 54-64 and 67-81 similarly). So a long piece is a wave along a
     path of Even chains, of which the corridor is the part that the family stretches.
- §7's conclusion follows from the trace as a READING: two long waves cover the stretched corridor (+1 transition per added vertex each)
  and a third piece is bounded, so the run is ≈ 2n + const; nothing here shows a number of long pieces growing with n (RUN-LIN′ open).

## DONE / FINDINGS / NEEDS
- DONE: this file; scratch/runlin_check.py; scratch/runlin_inputs/ (5 instances), scratch/runlin_logs/.
- FINDINGS: RUN-LIN and RUN-LIN-OPT DEAD, confirmed on my own engine (runfam_K10: one fallback-free phase of 99 > 98 transitions, I_τ = ∅,
  𝒞^1O; K40 171 = 2n + 13); Oink zlk / tl agree and the strategies verify; §7's wave reading is fair, but the gate's options are not literally
  the corridor's two ends (28 is one end, 25 is one Even step from options 2 and 9), and the waves also travel non-corridor Even chains. Even
  wins every vertex on the family (remark).
- NEEDS: none.
