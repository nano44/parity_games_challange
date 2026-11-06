# R213 RISE-2D under attack: DEAD at d 5 and d 6; exact at d 3 (L-RED successor 51)
Started 2026-11-06 12:1xZ (date -u). Lead BOX R213 (12:04Z), seed message 12:43Z. Object: L-NEW box 180 (claude/l-new 53318932,
docs/new/N5-RISES-box180.md) CONJECTURE RISE-2D «on 𝓛^R_d every option value rises at most 2d times in every run» (⇒ T^R(d) ≤ 8d² + 1
with RISE-EQUIV), and box 181 (29d41314) MOVES-2D «every Ξ-target mover moves at most 2d times» (implied by RISE-2D via MOVE-RISE).
Model: RESULTS R104 IDEAL, 𝓛^R_d of RESULTS R110. R(x, k) = number of strict rises of cv(xt(x, k)) along the run (box 180 §1).
Labels: DEAD (verified instance), EXACT-SAT (CaDiCaL 1.9.5 via pysat, one solver, no proof file), DATA, READING. Not a TARGET.md claim.
G-N5-TIME stays OPEN; the kill bounds nothing.

## 0. Answers
- **RISE-2D is DEAD** at d 5 and d 6:
  - r213/keep/rise_d5_R13.json (sha1 a45d7689…): d 5, start 1110110001, T 16; option (0, 0) (Ξ-target mover 8) rises 13 > 2d = 10 times.
  - r213/keep/rise_d6_R14.json (sha1 80d75c06…): d 6, start 101101011010, T 16; option (2, 1) (target mover 11) rises 14 > 12 times.
  - Checks (both): r187/ideal.py replay, T = max over all starts; L-NEW box 150 checker VIOL 0, XSIM 0; r189/lemck.py L 16, 0
    violations; R counted twice, by r213/rises.py (own: cv = signed 2^rank sums along the current Ξ-chain) and by L-NEW's own
    box180/rises.py (copied unmodified from claude/l-new 53318932, run on box 150's Gen): maxR 13 / 14, «maxR>2d 2», FALL 0, REDUCE 0.
  - Found by r212/fl.c with SCORE=R (max over options and all starts of the rises, memoised along the run graph), seeded from the R212
    records TR_d5_T16 and TRL_d6_22. fl agrees with rises.py on dd_d5_F14 (10), TR_d6_T22 (9 over all starts; 8 from the stored start),
    TR_d5_T16 (8).
- **RISE-2D at d 3 (EXACT-SAT):** R ≥ 7 is UNSAT for each of the six movers z, horizon 8 = T^R(3) (R197 exact), so max R(3) ≤ 6.
  R ≥ 6 is SAT (z 2, 110 s): r213/keep/rise_d3_R6.json, d 3, T 7, option (1, 1) rises 6 times (own rises.py and L-NEW box180
  rises.py agree; box 150 VIOL 0; lemck L 7, 0 violations). So **max R at d 3 = 6 = 2d EXACTLY** (EXACT-SAT): RISE-2D is tight at d 3
  (climbs had 5). z 0 and z 1: UNSAT at r 6 (2,061-2,077 s); z 3-5 not run after the SAT.
- **MOVES-2D at d 3 (EXACT-SAT, r213/move.py, env MOVEZ / MOVEMIN in xcnf; horizon 8):** max moves of a Ξ-target mover = 1 at level 0
  (r 2 UNSAT, r 1 SAT; consistent with R109 SEG-ONCE at l = −1), 3 at level 1 (r 4 UNSAT, r 3 SAT, replayed), 4 at level 2 (r 5 UNSAT,
  113-115 s; r 4 SAT, replayed); partners z 1, 3, 5 UNSAT at r 5. So MOVES-2D holds at d 3 with room: 4 < 2d = 6.
- **MOVES-2D: not killed.** The RISE-2D kills have Ξ-target movers moving ≤ 5 / 6 times (dd_d5_F14: 7); their rises come from chain changes
  below, not from own moves. SCORE=M climbs (d 5 from dd_d5_F14 and rise_d5_R13; d 6) reach 8 at d 5 (2d = 10). DATA only.
- READING: the kill removes the 8d² + 1 route only. In both kills R/T = 13/16, 14/16: one option rises at almost every step, so
  RISE-EQUIV (b) R ≤ T is nearly tight; max R tracks T, which stays linear in the data (R212).

## 1. The encoding (r200/xcnf.py, env RISEZ = z, RISEMIN = r)
- IN[(t, u, f)] (face f on mover u's current Ξ-chain at state t) is defined for t = 0..L when RISEZ is set (default runs unchanged).
- chg(t) = OR_f (IN[t − 1, z, f] XOR IN[t, z, f]), t = 1..L; constraint Σ chg ≥ r (sequential counter); plus «z is the Ξ-target of some
  option». A change of z's chain is a strict rise of cv(z): by R105 MONO cv(z) never falls, and distinct ranks give distinct values to
  distinct face sets.
- TMIN = 0 (runs of any length ≤ horizon). Horizon = T^R(d) makes the query cover every run.
- Driver r213/rise.py: SAT → decode, replay (ideal.py), recount (rises.py), «OK» iff the replay has ≥ r rises of z.
- Sanity: d 3, r 5, z 0: SAT in 6 s, replay 5 rises.

## 2. Exact queries
| d | horizon | r | z | answer | time |
| --- | --- | --- | --- | --- | --- |
| 3 | 8 | 7 | 0, 1, 2, 3, 4, 5 | UNSAT (all six) | 453-701 s each |
| 3 | 8 | 6 | 0, 1 / 2 | UNSAT, UNSAT / SAT (replayed, 6 rises) | 2,077, 2,061 / 110 s |
| 4 | 13 | 9 | 0, 2, 4, 6 (σ_l swaps 2l, 2l + 1 and preserves R) | STOPPED 14:10Z (Lead: low value after the kill); root cube split twice, no answer; state r213/cubes/ resumable (r213/run_d4.sh) | |

## 3. Climbs (r212/fl.c SCORE=R / SCORE=M, r212/out/L0_m*_r6xx / r7xx logs)
| d | 2d | best max R | best max moves of a Ξ-target |
| --- | --- | --- | --- |
| 4 | 8 | 8 | — |
| 5 | 10 | 13 (kill) | 8 |
| 6 | 12 | 14 (kill) | 8 |
| 7 | 14 | 14 (= 2d, no kill) | — |
