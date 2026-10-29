# R104: FB-LIN, the counting-gate box (last FB-LIN box). No kill. The rank-per-reset inequality asked for does NOT hold (R103 §3 corrected): gate path sets reset under a fixed top all the time; the scarce resource is stalls, not ranks
L-RED successor 24 (Opus 5.5; D14/D15/D18; Lead 2026-10-29 04:57Z: "ONE last box on FB-LIN: the counting gate (R103 §4) ... Report a
kill, or the exact obstruction, ideally the inequality that forces a rank increase per reset."). Written 2026-10-29 05:20Z (date -u).
Labels: DATA / READING / OPEN.

## 1. Correction to R103 §3 (READING withdrawn)
R103 §3 said: "A counter of this kind needs each digit's reset to be Ξ-improving ... the higher digit's change is again one rank. This is
the same budget, so I see no way to get more than about one carry per rank from it." The ranks part is WRONG:
- Ξ-monotonicity does not force a new rank per reset. In S1's order a path set with a new even element at rank j beats every set that
  differs only below j. So a binary count (bit j turns on, every lower bit turns off) is Ξ-increasing and REUSES the low ranks. With k
  digits that gives 2^k increasing sets.
- DATA (§2) shows such resets constantly inside one phase. What is rare is a reset that coincides with a STALL.
So there is no inequality of the form "one rank per reset". The obstruction to a counting gate is not in the valuation order.

## 2. DATA (experiments/red/fb/gatep.py)
For each Odd choice vertex q, P_t(q) = the path set of the (σ_t, σ̄_t)-play from q (S1's P). Per phase: PCH = changes of some P(q), RESET =
changes that remove an element while the top element is unchanged (a low-digit reset), RESET_STALL = resets whose next transition is an
in-phase fallback (a stall).
| instance | n | f | PCH | RESET | RESET_STALL |
| --- | --- | --- | --- | --- | --- |
| pl130_n40 (own start) | 40 | 11 | 157 | 133 | 8 |
| long121_n40 (own start) | 40 | 8 | 116 | 93 | 0 |
| pftheta34_n32 (S3) | 32 | 0 | 10 | 9 | 0 |
| fb38_n48 (pinned start) | 48 | 38 | 12 | 9 | 0 |
| pl130 ISO climb (R103) | 40 | 13 | 64 | 33 | 4 |
- Climbs with fitness 1000·RESET_STALL + 30·RESET + 10·f (fbclimb.py --rs, own start, 20 min, 4 seeds) raise RESET_STALL to 30-32 while f
  stays at 7-14 (pl130 climb: RESET 192, RESET_STALL 30, f 11; best_7 climb: RESET 114, RESET_STALL 32, f 7). One stall resets the path
  sets of several gates at once, so RESET_STALL counts gate-transitions and is not bounded by f. It is gamed and says nothing about f.
- So in every instance and climb, counting (resets) is abundant and stalls are scarce: f ≤ 0.79n (fb38_n48), ISO ≤ 0.33n (R103).

## 3. READING: where the counting gate actually stops (not a theorem)
- f counts stalls. A stall needs every Ξ-improving switch in the whole game to be W-rejected (S4a idle) at once. A counter whose counts each
  end in a stall needs that, Θ(n) times or more in one phase. R100-R103 show the two ways stalls come, and why neither multiplied:
  - waves (consecutive stalls), whose reuse is blocked by the reader-prefix pair (R100 §3, R101 §4);
  - carries (isolated stalls), one per gate P-change in the data (R103), whose count the climbs keep at ≤ 0.33n.
- τ does not close the gate here. Every construction used the TAUSTAR start or an own start with I_τ = ∅, so S4b never fires (the BOX 16
  closure is avoided). Gates close instead when σ realises their escape (R100 §1). A counting gate needs its gap (σ̄ ≠ τ) to survive every
  count. Each count raises Ξ(gate) toward W(gate) ≤ the game value at the gate, and W rises only when σ improves on τ's branch. I did not
  build a gadget that keeps the gap open across counts and stalls at each count.
- The inequality the Lead asked for, if it exists, must be about stalls, not ranks: something like "between two stalls at which the
  gate's P resets under the same top, some Even vertex is fixed for the rest of the phase". It is not proposed; no data test was set up.

## 4. OPEN
- FB-LIN remains a CONJECTURE: data max f 38 = 0.79n (fb38_n48), ISO ≤ 0.33n, five boxes (R100-R104) without a kill.
- A gadget whose path-set counts each end in a stall, with the gate kept in D across counts.

## DONE / FINDINGS / NEEDS
- DONE: R104 (this file); gatep.py (PCH, RESET, RESET_STALL); fbclimb --rs.
- FINDINGS:
  - R103 §3's "one rank per reset" is wrong: low-digit resets under a fixed top are abundant (133 in one pl130 phase) and Ξ-monotone
    (binary counting).
  - The scarce resource is stalls: resets at stalls ≤ 8 in the library; the climbs only game the count (several gates per stall); f did
    not grow.
  - No kill, and no rank inequality: the counting-gate obstruction is a stall obstruction, open.
- NEEDS: none from the owner.
