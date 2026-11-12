# R231 item (a): L-NEW 70's re-armed carry CWR(n) (box 206 Addendum D, claude/l-new 134adb53) on L-RED's own engine (L-RED successor 65)
Written 2026-11-12 (date -u in the commit). Engine: experiments/red/r221q/own.py; builder: my experiments/red/r231/carry231.py (env
CW_REARM, written from Addendum D's prose and carry206.py's documented option order); no L-NEW code run. Labels: DATA / READING / DEAD.

## 1. Reproduction: AGREEMENT
- My builder's CWRR4/8/16 and CWRQ4/8/16 are JSON-equal to L-NEW's frozen files (sha1 6970f1b9 / c11bc1c2 / 4cd707c7, f863afd2 / b0fcba01 /
  2cf7b336); copies in r231/inst (CWRR4/8/16, CWRQ8).
- DATA (cw231.py, out/cw231_CWR.out; set CWRR4/8/16, CWRQ8; scope movers): k 1; N + M 160 / 310 / 658; b 6 / 10 / 18; Dtop = D_mov 3; T 28 /
  52 / 100; max ascents 1; max loud depth 0; BOX 206 must-0 counters 0. All equal to Addendum D's table.
- DATA (eface231.py, out/eface231_CW8_CWRR8.out; unit: states; set CW8_n, CWRR8_n): e-face of qh_1..qh_7 (movers 54-60) taken at 0 / 53
  states on CWRR8 (qh_8: 3), against 39, 31, 27, 24, 21, 18, 14 (qh_8: 9) of 60 on CW8. = L-NEW's «0 states against 14-39».

## 2. The obstruction on the trace: the collapse is real, the stated mechanism is not what the trace shows
- Addendum D: «The re-arm edge c_k → R closes a Γ-cycle qh_k → e_qh_k → c_k → … → R → … → qh_k THROUGH the e-vertex e_qh_k. On IDEAL-CYC,
  Odd never takes such an e-face».
- DATA (eface231.py, same sets; unit: states): the number of states at which the play from e_qh_k, with qh_k's gate forced onto its e-face
  and every other vertex on the state's strategy pair, returns to e_qh_k is 0 for every k, on CWRR8 and on CW8. So at no state of the run
  does such a cycle close under the strategies actually played.
- What the trace shows (ediag231.py, out/ediag231_CWRR8_qh3.out vs out/ediag231_CW8_qh3.out; qh_3, c_3 = mover 86):
  - c_3 switches to the re-arm option (Ξ-target R) by t = 5 and keeps it to the end.
  - From t ≈ 10, at Q's gate Odd takes the β-face (the e-face of Q leads hv → v → qh → e → c → R, back into R). The race cycle R → Q → R through
    the β's closes. Its top is β_(R,0), priority 218 (even), so every play that reaches R ends there.
  - At qh_3's gate both faces end in that cycle: val(e) = (β_R, |Π| 2), val(β) = (β_R, |Π| 0). The e-face only adds the e-vertex to Π
    (good for Even), so Odd takes β. On CW8 instead, c_3 picks its qh_j or X options, Λ stays K1, and Odd uses the e-face at 30 of 60 states.
- READING (corrected mechanism): the re-arm edge makes every exit of the race component lead back to R. So Odd can no longer escape the race
  to K1 and must close the R ↔ Q cycle, whose top β_R is even. That cycle absorbs every re-armed carry: one class for all movers, D_mov 3.
  Addendum D's «a cycle through e_qh_k» is the counterfactual that Odd blocks at Q's gate, not a cycle that closes. DEAD CWR stands, with
  this obstruction: «a re-arm route back into the race traps the race cycle (top even β_R), and every carry is absorbed».

## 3. The variant that avoids R: re-arm through any other single vertex (DEAD as a family of variants, at n = 4, 8)
- rearm231.py: for EVERY mover t of MWR(n) (51 at n = 4, 91 at n = 8), CW(n) plus one re-arm option per c_k with Ξ-target t (even β, before X),
  own engine. DATA (out/rearm231_n4.out, out/rearm231_n8.out; unit: genomes; scope movers):
  - k = 1 for every t.
  - D_mov ≤ CW's (12 at n = 4, 38 at n = 8) for every t; T ≤ CW's (30, 59) for every t.
  - Every race-component target collapses: R, Q, v, hv → D_mov 3; u, qz → D_mov 4 (T 28 / 52).
  - The lane and sink targets (a_i, b_i, D, W, qh_k) leave CW unchanged or lower it (D_mov 9-12 at n = 4).
- READING: a single extra Ξ-target either feeds the race component (then the race cycle traps and the carries collapse) or does not see
  the race (then nothing is re-armed). With one re-arm option per c_k there is no third case. A re-armed carry at k = 1 would need re-arming
  that sees the race's state without giving Odd's race exits a route back into R. Not found; open.
