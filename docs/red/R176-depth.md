# R176 Time depth D at ODIFF ≥ 1: the topfix family from its written starts has single ODIFF-1 TWO-FIX windows with charge depth D = 6k − 1 at n = 21k (k = 6..12; 71 at n 252), so D grows linearly in n at ODIFF 1 and GATE-REC's roots·(F + … + F^D) is not polynomial there; no padding needed (L-RED successor 41)
Started 2026-11-01 09:50Z (Lead queued box R176, date -u). Brief: «pad topfix_n10 so the window has ODIFF ≥ 1, and see whether time depth D
stays large … add one idle ODIFF vertex (or the cheapest structure …) and measure D, fan-in and PHNF per λ_W-phase. Then try a family
with D growing in n at ODIFF ≥ 1.» Labels: DATA, READING. Not a TARGET.md claim. G-N5-TIME stays OPEN. Nothing here is a kill: ODIFF-1
windows are polynomial (R170 FREEZE + RESULTS R51), and the family's runs are linear in n.

## 0. Answer
- No padding was needed.
  - L-NEW box 129 ran topfix_n10 from N5's default S3 start: ODIFF-0 window [6, 64], depth 52; its ODIFF ≥ 1 window has depth 1.
  - The same game from its own written start (new/box52/out/topfix_n10.start, a valid start: startck OK) is different. Every long window
    has ODIFF 1, and the charge depth grows window by window: 16, 22, 28, 34, 40, 46, 52, 59.
  - The last of these is window [303, 365] (L 62, ODIFF 1, 0 fallbacks): depth 59, fan-in 8, 564 charged moves.
- The family new/box52/out/topfix_nk (n = 21k, written starts) gives a size-indexed ODIFF-1 family with D growing linearly in n (DATA):

| k | n | longest-depth ODIFF ≥ 1 window | ODIFF | depth D | fan-in | charged moves | best PHNF (window L) | run K |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 63 | [4, 19] | 1 | 12 | 18 | 80 | 18 (20) | 61 |
| 4 | 84 | [4, 19] | 1 | 12 | 25 | 113 | 24 (26) | 95 |
| 6 | 126 | [107, 145] | 1 | 35 | 4 | 200 | 36 (38) | 181 |
| 8 | 168 | [193, 243] | 1 | 47 | 6 | 358 | 48 (50) | 291 |
| 10 | 210 | [303, 365] | 1 | 59 | 8 | 564 | 60 (62) | 425 |
| 12 | 252 | [437, 511] | 1 | 71 | 10 | 818 | 72 (74) | 583 |

  - D = 6k − 1 for k ≥ 6 (n/D → 3.5).
  - Fan-in stays ≤ 10 in the deep windows. The large fan-ins (18, 25, 67 on n10) sit in the shallow window [4, 19].
  - PHNF: per window, from r172 climb172.phnf_windows, the port of L-NEW box 122 windows.py. The best ODIFF ≥ 1 window has PHNF = L − 2,
    below n − 1. PHNF per λ_W-phase is at most the per-window value (phases inside the windows were not split here).
- Consequence for GATE-REC (READING):
  - At ODIFF 1, D is Θ(n) on this family while F ≥ 2. So the bound roots·(F + … + F^D) is exponential even where the true count is
    polynomial (ODIFF 1: FREEZE + R51) and here linear.
  - So D = O(1) is false at ODIFF ≥ 1, and a polynomial charge argument must use additivity (F = 1 along chains) or bound the chains
    another way.
  - The obstruction box 129 §4 describes (a cyclic vertex-level charge with time depth) is present at ODIFF 1. Box 129's table read D ≤ 4
    at ODIFF ≥ 1 only because its corpus runs topfix from the S3 start.

## 1. Checks (experiments/red/r176/out/pins.txt)
| pin | sha1 game / start | startck | Oink 8fbf0a7 zlk + verify | Oink --tl -v | xeng | FREEZE |
| --- | --- | --- | --- | --- | --- | --- |
| topfix_n10 | 4b65d3dc2735… / 35a45d49540d… | OK | OINK OK | verified (121 strategies) | identical | [303, 365] L 62 ODIFF 1, FFSEG 62, REPLAY True |
| topfix_n12 | a08c2c1dec86… / 37ed67b2db76… | OK | OINK OK | verified (145 strategies) | identical | [437, 511] L 74 ODIFF 1, FFSEG 74, REPLAY True |
- The pins are copies of new/box52/out/topfix_n10 / n12 and their starts (L-NEW box 52 outputs on trunk). The game sha1 for n10 equals
  box 129's pin (4b65d3dc2735). Only the start differs.
- No corpus counts in this box, so E-1 de-duplication does not arise.

## 2. Not done
- The idle-ODIFF padding of the S3-start window [6, 64]: superseded, since the written start already gives ODIFF-1 windows of larger
  depth.
- PHNF per λ_W-phase measured phase by phase: only per-window PHNF (an upper bound) is given.
- The topfix family is linear (run K ≈ 2.3n). D growing faster than n at ODIFF ≥ 1 is OPEN.

## 3. Tools (experiments/red/r176/)
- gatechg.py: a COPY of claude/l-new 1ebdae81 experiments/new/box129/gatechg.py. The box21 path line is adapted; an env VERB=1 per-stretch
  line was added; otherwise unchanged.
- fam.sh (out/fam.txt): the family table.
- check.sh block «R176»: depth 59 on topfix_n10's window [303, 365].

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/red/r176/*; check.sh block R176; notebook. SHAs in the push / message.
- FINDINGS:
  - topfix_nk from its written starts: ODIFF-1 windows with D = 6k − 1 at n = 21k (71 at n 252), fan-in ≤ 10, 0 fallbacks.
  - D = O(1) fails at ODIFF ≥ 1, so GATE-REC's geometric bound is exponential on a linear family. Box 129's «ODIFF ≥ 1: D ≤ 4» is a
    start effect (S3 start versus the written start).
- NEEDS: Lead: route to L-NEW 45 (box 129 / GATE-REC). The charge bound needs additivity or another chain bound; D = O(1) cannot hold.
