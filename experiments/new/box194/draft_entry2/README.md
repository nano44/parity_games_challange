# DRAFT, NOT ROUTED: P-N5-QUIET fixes entry 2 + line L-2 (L-NEW successor 63, 2026-11-08 ~05:2xZ)
Lead 05:20Z: «commit your prepared fixes entry 2 + L-2 as a DRAFT outside the packet files … clearly marked NOT ROUTED».
Nothing here is part of packet P-N5-QUIET, its fixes file, its pins or any check.sh block. Successor 64 finishes it AFTER REFEREE-2 33's
review of P-N5-QUIET, so that one fixes entry 2 answers both REFEREE 28 (claude/referee a233f356, docs/referee/R-P-N5-QUIET.md) and
REFEREE-2 33.

## Files
- L2_QT_only.txt: L-1 + REFEREE 28's QT-L1..QT-L6, made with REFEREE's own scratch/quiet_linefix.py (git show a233f356, run with -I):
  sha1 fed893462811ea10d0b99622dcbb31f7b50b6d47, 5,131 B: MATCHES REFEREE 28's predicted L-2 byte for byte.
- L2_QT_formB.txt: the same + Form B (Lead 03:37Z «take REFEREE's optional Form B»; Lead 04:10Z «The Form B difference from fed89346 is
  fine; say so in the entry»): one more string, in QUIET's DATA clause:
  old «rd3_d4, RS2_L32M6, 10 of the 13 instances (all but cR_d2_w8_R22, rd3_d7, rf_d5), the 1,000 random genomes); »
  new «rd3_d4, RS2_L32M6, the 13 instances, the 1,000 random genomes; tested against L, not L + 1); »
  sha1 56fb06989b00f5d746e3449a7930ba40d458b326, 5,116 B. (Successor: re-apply on top of REFEREE-2 33's strings; the sha1 will change.)
- quiet194_fixed.py / quiet194_fix.diff: the off-by-one fix (Lead 03:37Z): L = (M+1)(2M+1)(N+1) + N(n−1), not + 1 (code l. 19 and the
  docstring). To use: copy over experiments/new/box194/quiet194.py (its imports are relative to box194/), add the three instances to
  check194.sh's quiet194 call, regenerate check194.out, repin quiet194.py / check194.sh / check194.out in quiet.pins.
- formB_quiet.out: quiet194_fixed.py on all 13 P-N5-ASC instances + rd3_d4 + RS2_L32M6, and rand 1000 2: wfail 0, Tfail 0, crossflip 0
  everywhere (run in a mirror tree). Added instances: cR_d2_w8_R22 W 0 (N 16), rd3_d7 W 4 (N 14), rf_d5 W 0 (N 10) = REFEREE 28's replay.
  Every printed L is one less than in check194.out.

## Fixes entry 2 text (draft; append to docs/new/P-N5-QUIET-fixes.md only after REFEREE-2 33)
- Report: REFEREE 28: every statement SIGN; ASC-T, UP-T conditional on R121 landing first; UP-T under HYPOTHESIS [E-LEV]; L-1 NOT YET on
  QT-L1..QT-L6. All ACCEPTED as written (exact strings: REFEREE §5 and quiet_linefix.py).
- QT-L1 [OPT]: re-cited from R118's σ̄ as used in R118 (b) (XICYC l. 75 «σ̄_t is optimal at every vertex at once ([VJ])») and R21 (a);
  R57 (b) concerns SPEC's S1 output and is not used (Lead 03:37Z correction (1): the 00:36Z reading was wrong). Fixes entry 1's [OPT]
  paragraph is superseded.
- QT-L2: F2 added to the premise list. QT-L3: [E-LEV] is a HYPOTHESIS (R104 (vi) leaves the e-priorities to its packet as immaterial).
- QT-L4: the Γ3 scope sentence of fixes entry 1 OVERCLAIMS (Lead 03:37Z correction (2)); replaced by REFEREE's sentence (nothing is
  proved on Γ3; the Γ3 run can differ at exact VJ ties); the DIV witnesses stay. Note for box 195 / P-N5-END: they never used it.
- QT-L5: the random set's generator parameters (d 1-6, w 1-3, degree 2-3). QT-L6: CN2's DATA scope ((σ_t, σ̄_t) only).
- Form B + off-by-one: as above; the final L-2 differs from fed89346 by the Form B string (Lead 04:10Z: fine).
