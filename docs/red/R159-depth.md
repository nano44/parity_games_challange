# R159: W-run depth h^W is cheap. A designed family hd_H (a chain of self-referential gates) has ONE W-run of H transitions with hier.py DEPTH H = (n − 2)/3, so depth grows linearly with n (HDEPTH dead by design; box 109 found depth 3 by search). But |F| = H = depth: one transition per level. Depth alone is no lengthening, and HIER-RED's (n(n + 2) + 1)^(h^W) is vacuous on it. hit_b6a_1 reproduced (xeng identical, Oink OK). Its depth-3 shape avoids R158's obstruction (A) because y_1's alternative is an Odd vertex with an edge back into the carrier's own play: both sides of the gate comparison share the same suffix, and no root/phase level enters
L-RED successor 37 (Opus 5.5; D1/D18). Lead 2026-10-31 09:22Z: «GO R159 = the depth-3 build, with a seed … (1) Reproduce hit_b6a_1 … (2) Read its gate pattern. Explain how it avoids your obstruction (A) … (3) Turn it into a DESIGNED family where the depth h^W grows with n, or at least where level 3 holds for many transitions. Score |F|, |F|/n², h^W (hier.py), carriers (carrier.py), E^S and max XICH. If depth cannot grow, the obstruction should now be provable». Written 2026-10-31 from 09:35Z (date -u).
- Labels: PROVED (lane, elementary) / DATA / READING. Not a TARGET.md claim. G-N5-TIME stays OPEN.
- Sources opened:
  - l-new 04696022: experiments/new/box109/out/hit_b6a_1.pg / .start (sha1 ff1cd2f9 / 89ae7c5b);
  - box107/hier.py and box108/carrier.py source, run unchanged from a git archive;
  - l-si c7f00306 si/sb53/ceilpot.py.
  - NOT opened: docs/new/N5-HDEPTH-box108.md and the box-109 note (Lead summary only).

## 1. Reproduction (DATA)
- hit_b6a_1 (n 32, l-new start file):
  - n5b and n5.py on si.py make 43 iterations and 2 fallbacks, with identical state sequences (xeng); Oink OK.
  - W-runs (3, 12), (13, 19) and (20, 43), the longest |F| = 23.
  - hier.py: WT 38, DEPTH 3, NLEV 18 / 19 / 1. carrier.py: 23 carriers, all fixed by a new edge at a source event.
  - srcsettle: E^S 11, longest source-free block 10, VIOL 0. Max XICH 7. ceilpot: MAXAUP 5, MAXANDN 11.
  - The Lead's numbers match.

## 2. The gate pattern of hit_b6a_1 (DATA, fb/h3trace.py, carrier v = 5, W-run 20–43)
- k 20: 5 switches 9 → 21 (level 3, the single low fix).
- k 22–34: a source-free wave rebuilds a 14-vertex W-path backwards, one switch per step: 8→4, 24→8, 16→24, 28→16, 27→28, 17→27, 14→17,
  15→14, 3/31→15, 19→31, 20→19, 10→20, 1→10. Every vertex on it still carries the pending top digit u18 (prio 29) through the shared tail
  4 → 6 → 22 → 18, so the wave is flat at level 1.
- k 34–36: the wave's end is a source event (deviators 0 and 4). Then 9 → 7 (onto the new path), and 5 → 9 (new edge (5, 9), level 2:
  the mid digit u8).
- k 37–40: Odd 0's σ̄ moves 5 → 21. At k 40, 6 → 0 (new edge (6, 0), level 1: u18 leaves every play through 6).
- How (A) is avoided:
  - y_1 = 6 lies on the carrier's own W-play. Its alternative is the Odd vertex 0, whose successors {1, 5, 10, 11, 21, 27, 31} lead back
    into the carrier's structure (τ(0) = 11 is the exit).
  - So Ξ(0) is a min over values that share the carrier's current suffix, and the gate compares two values with the SAME tail. That is
    the level match R158's design A lacked (its delay line carried the new root while b_j carried hp's old level).
  - There is one wave and no phase or re-climb, so no root-dominance term appears.

## 3. A designed family with depth growing with n: hd_H (hd/mkhd.py)
- Construction:
  - Carrier v (Even, even priority E = 4) → y_H.
  - Gate y_i (Even, i = H … 1) has two edges: to c_i (odd digit marker m_i) → y_(i−1), and to o_i. o_i (Odd) → {y_(i−1) (τ), v}.
  - y_0 = z (sink, priority 3). Digits: m_H = 5 < m_(H−1) = 7 < … < m_1 = 2H + 3 (top digit nearest z). σ_0(y_i) = c_i.
  - n = 3H + 2.
- PROVED (lane, elementary; the SPEC S1 order on path sets):
  - Write R_i := Ξ(y_(i−1)) and Pref := the digits still on v's play above y_i.
  - Ξ(o_i) = min(R_i, Ξ(v)), and Ξ(v) = {E} ∪ {pending m_j} ∪ R-part.
  - Gate i is Ξ-improving (Ξ(o_i) ▷ m_i ⊕ R_i) iff the top of {E} ∪ {pending m_j : j > i} is E, i.e. iff every lower digit is already
    fixed. W prefers o_i at once (it skips m_i), so gate i switches at the first transition after gate i + 1. The digits are fixed
    bottom-up, one per transition.
  - Under τ̄ every back-edge value is E ⊕ (optimum) ▷ the τ-edge, so Iτ = ∅ and τ never moves. All plays end at z (λ_W constant), and
    no S4c fallback occurs, since one gate is improving at each state until the last.
  - So the run is ONE W-run with |F| = H.
  - Depth H by hier.py's definition: every vertex keeps the pending top digit m_1 on its play until the last transition. So level 1 pays
    only the last transition; inductively level d pays the fix of m_d.
- DATA (n5b; xeng identical; Oink OK):

  | instance | n | \|F\| | \|F\|/n² | h^W (hier DEPTH) | NLEV | E^S | longest source-free block | max XICH | carriers (carrier.py) | AUP / ANDN |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | hd_H10 | 32 | 10 | 0.0098 | 10 | 1 each | 10 | 0 | 10 (v) | 26, all fixed by a new edge at a source | 10 / 10 |
  | hd_H40 | 122 | 40 | 0.0027 | 40 | 1 each | 40 | 0 | 40 (v) | 116, ditto | 40 / 40 |
  | hit_b6a_1 | 32 | 23 | 0.022 | 3 | 18 / 19 / 1 | 11 | 10 | 7 | 23 | 5 / 11 |

- So CONJECTURE HDEPTH (h^W ≤ 2) is dead, and depth is not bounded by any constant: h^W = (n − 2)/3 on hd_H.
- And |F| = h^W. L-SI's A rises at EVERY transition of hd_H (AUP = |F|), which is consistent with CEIL-ACC, whose bound charges
  n(n + 2) per rise.

## 4. What this means for HIER-RED (READING)
- HIER-RED (|F| ≤ T1 + (n(n + 2) + 1)^(h^W)) is vacuous on hd_H: the right-hand side is (n²)^(n/3) while |F| = n/3. A polynomial bound
  cannot come from bounding depth.
- The quantity that would have to be large for a long W-run is the WIDTH: transitions paid per level, i.e. many fixes of the same digit
  position inside one parent stretch.
- In hd_H every level is paid once. In hit_b6a_1 the width sits at levels 1–2 (the 13-step wave), and level 3 is one transition.
- «Level 3 for many transitions» needs the low digit to be re-fixed, i.e. un-fixed and re-fixed, inside one level-2 stretch. In W that
  means the gate y_3 re-entering an option it left, which is the re-entry / re-climb question of R152 (O1 dead) and R155–R157 (k-SOURCE).
  So the open target, restated, is width per level, not depth. No lemma bounding width is proved here.
- Not built in this box: a private delay chain per gate (depth H, each level a source-free wave of length L). That gives |F| ≈ H·L at
  n ≈ H(L + 3), still linear. A shared delay line is R158's obstruction (A) again.

## 5. Pins (experiments/red/check.sh «R159»)
- hd/pins.sha1 (hd_H10, hd_H40, hit_b6a_1 copied from l-new 04696022); mkhd.py 40 reproduces hd_H40; wch |F| 40; xeng and Oink on hd_H40
  and hit_b6a_1.

## DONE / FINDINGS / NEEDS
- DONE: this note; hd/mkhd.py, fb/h3trace.py, hd/instances, hd/pins.sha1, check.sh «R159». SHA: see the commit.
- FINDINGS:
  - DATA: hit_b6a_1 reproduced (43 iterations, 2 fallbacks, DEPTH 3; xeng, Oink OK).
  - READING: it avoids (A) by self-reference. y_1's alternative is an Odd vertex with edges back into the carrier's own play, so both
    sides of the comparison share the same suffix.
  - PROVED (lane) + DATA: designed family hd_H, one W-run with h^W = |F| = (n − 2)/3 (hd_H40: n 122, depth 40). HDEPTH is dead with
    linear depth, and HIER-RED's exponent is vacuous there. The open quantity is the width per level.
- NEEDS: none.
