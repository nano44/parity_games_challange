# R145: CONJECTURE FLIP-EV (L-SI box 52) is DEAD. flipev_n10: an EXI σ̄-flip at a non-cycle-node Odd vertex in a W-run, at a transition with NO Ξ-change at any upward head; it is caused by an ENT flip elsewhere through a BFS tie. Repair candidate FLIP-EV′. (b) The head-feedback clock is not built; its exact shape (nested two-head leapfrog oscillators with a W-shortcut-free carry) is stated
L-RED successor 34 (Opus 5.5; D1/D18). Lead 2026-10-30 18:14Z, R145: «(a) CONJECTURE FLIP-EV … FLIP-CAUSE″ is already DEAD
(heads52/inst/flipnone_n14, flipnonex_a_n10); start from those … (b) L-SI's §4 target, the head-feedback clock … Build one, or name the
exact obstruction.» Written 2026-10-30 from 18:15Z (date -u). Labels: PROVED (lane) / DEAD / CONJECTURE / DATA / READING. Not a TARGET.md
claim. G-N5-TIME OPEN.
Source opened: L-SI box 52 (l-si 71d1d0ac, docs/si/N5-HEADS-box52.md §1-§4; experiments/si/heads52/flipc.py and inst/). Quoted, §3:
«CONJECTURE FLIP-EV (the form the count needs). Every EXI or MOV flip at an Odd o that is not its own Ξ-cycle node (at k or k + 1) occurs at
a transition with an event (iii).» Event (iii) (R143 §0): «Ξ changes at some vertex of U_k ∪ U_(k+1)».

## 1. (a) FLIP-EV is DEAD (DATA, exact; two engines, two counters, Oink)
- Instance experiments/red/flipev/instances/flipev_n10.pg (L-SI's flipnonex_a_n10 game, unchanged) with flipev_n10.start. The start
  is flipnonex_a's state 1, except τ(9) = 0 instead of 6:
  - σ_0 = {0:3, 1:9, 2:4, 4:6, 5:8};
  - τ = {3:5, 6:3, 7:3, 8:4, 9:0}.
- Transition 0 → 1 is a W-run transition (τ fixed, λ_W map constant, no fallback, σ moves). Every Ξ value has cycle node 5 (priority 9,
  odd) and empty path set, so only lengths matter (BFS branch; Odd prefers shorter).
  - Even 0 switches 3 → 4, and Ξ(0) rises in length 2 → 4.
  - 0 = τ(9) is NOT a head: 9 did not deviate at state 0 (σ̄_0(9) = 0 = τ(9)). So Odd 9 makes an ENT flip, 0 → 6. Ξ(6) has length 2, so
    Ξ(9) stays at length 3.
  - Odd 8 (τ(8) = 4) deviated to 9 at state 0, and Ξ(4) = Ξ(9) = length 3 is a tie. 9's new BFS parent re-orders the discovery, and 8
    flips 9 → 4 = τ(8): an EXI flip. 8 is not its own Ξ-cycle node (cycle node 5).
  - Heads: U_0 = {9} ∪ {Ξ-successors of W-cycle nodes} and U_1 = {6} ∪ … No Ξ value of U_0 ∪ U_1 changes (Ξ(9) 3 → 3, Ξ(6) 2 → 2).
    So no event (iii).
- Checks:
  - red/flipev/flipev.py on L-COMP's n5b SPEC: candidates 1, VIOL 1, witness (k, o, old, new) = (0, 8, 9, 4).
  - L-SI's own counter flipc.py on n5x (run unchanged from an archive of l-si 71d1d0ac): EVX 1. Control on flipnonex_a_n10 itself: EVX 0,
    as box 52 reports.
  - xeng: state sequences identical. Oink zlk + verify: OK.
- Second, independent instance: flipev/instances/flipevr_n10 (random hill-climb, rand:10 seed 1, 131,119 tries; the default S3 start is
  written to .start).
  - Transition 1 → 2: EXI flip at Odd 9 (3 → 0), with no head event. An ENT flip occurs in the same transition.
  - Checks: n5b VIOL 1 = L-SI flipc EVX 1; xeng identical; Oink OK. So the kill does not depend on a hand-made start.
- Mechanism, in one line: a non-head Ξ-rise makes an ENT flip whose own Ξ stays fixed (a tie), and the tie re-orders S1's BFS
  discovery, which moves a deviating Odd vertex back to τ. L-SI's flipnonex_a had the same chain, but with 9 already deviating, so its old
  target 0 was a head.
- Consequence for Corollary FLIP-RED: its premise fails. EXI flips are not charged to event (iii) alone. In the instance the EXI flip is
  charged to the ENT flip at 9. FLIP-RED's ENT ≤ EXI + 1 per vertex then charges back, so the charging can cycle, and SB-POLY does NOT
  reduce to XCN-POLY by this route.
- CONJECTURE FLIP-EV′ (repair candidate, R145): every EXI or MOV flip at a non-own-node Odd vertex occurs at a transition with an event
  (iii), or with an ENT flip at another Odd vertex.
  - flipev_n10: VIOL2 0.
  - Corpus (red/flipev/run.sh: box 50b's lists, 1132 runs, 300 s each): 4,962 candidate flips, VIOL 0 (agrees with box 52's EVX 0),
    VIOL2 0. The two alt entries n3cov_lean and n3cov_phi have partial starts (R99 erratum) and are not counted.
  - A search aimed at FLIP-EV′ (SCORE2=1, rand:12) found no violation, nor any VIOL instance, before it was stopped at about 30 min of
    its planned 1800 s.
  - For FLIP-RED, FLIP-EV′ needs a charging rule that is acyclic: ENT flips caused by non-head rises must be charged to the Even switch
    that caused them. Not done.
- Searches (flipev.py --search, hill-climbing on games with the default S3 start, 900 s each): only rand:10 seed 1 found a violation, flipevr_n10 at try 131,119. rand:12 (354,647 tries), the flipnonex_a seed
  (459,690) and the flipnonex_b seed (474,314) ended at MINHC 1, one head change at best. The pattern is rare at random, which fits box 52's
  500k-game zero.

## 2. (b) The head-feedback clock: not built. What it must look like (PROVED parts lane; the rest READING)
- Lemma SAME-HEAD (PROVED, lane, elementary).
  - Let Even v have two options a, b whose Ξ-plays reach the same next head u, before any other head, with the same cycle node, and
    with segments that do not meet u's play.
  - Then the ⊴-order of Ξ(a) and Ξ(b) does not depend on Ξ(u): Ξ(a) = seg_a ⊕ Ξ(u), and the VJ comparison is decided on seg_a Δ seg_b
    and the segment lengths.
  - So a head event at u re-opens a choice only where the options lead to DIFFERENT heads, or where u's cycle node changes.
- Hence a carry that a head event re-opens is a FLIP of the order of two heads u1, u2 as seen from v. Every such flip needs a strict
  Ξ-rise of u1 or u2 (Ξ is monotone).
- A reusable delay line (latew's reactors, R144 §1) is exactly this: m layers, each comparing "via the previous layer to u1" against
  "direct to u2". Each order flip of (u1, u2) sends one wave of length m through the line. So |F| ≈ (flips of (u1, u2)) × m, and RUN-SETTLE
  allows that.
- Feedback (READING). To get a clock, the end of each wave must raise the other head: forward wave ⇒ u2 rises above u1; backward wave
  ⇒ u1 rises above u2.
  - Ξ is monotone. If the line and everything else returned to the same configuration, u1's value would repeat. So every round must
    change some state permanently. The number of rounds is at most the number of distinct configurations of "the rest".
  - With fresh rungs (latew's pivot ladders) this gives (rungs) × m = Θ(n²).
  - Beyond that, "the rest" must itself be such an oscillator one level up, changing once per lower round: nested leapfrog
    oscillators, i.e. a binary counter whose state is the Ξ path set of the heads.
- Exact obstruction (READING, no lemma). Monotonicity does not forbid the nested counter: path sets can encode the counter value. The
  only known blocker is S4a. ARENA-MAX takes the W-optimum of the offered edges, and R140 found that it closes every bit cycle of a
  Friedmann counter at iteration 1. A head-feedback clock therefore needs carries whose W-shortcut is never offered, i.e. offered only in
  Ξ (σ̄-dependent) while W (τ-dependent) does not see them. That is R140 §3's Ξ-deceleration lane, still untried at depth ≥ 2.
- Not attempted this box: L-NEW box 93's elimination-window target (runfam_K40).

## DONE / FINDINGS / NEEDS
- DONE: red/flipev/ (flipev.py with --search, run.sh, corpus outputs, pin flipev_n10 + pins.sha1); check.sh "R145"; this note;
  notes/L-RED.md.
- FINDINGS:
  1. DEAD: CONJECTURE FLIP-EV (flipev_n10, transition 0 → 1, o = 8; n5b VIOL 1 = L-SI flipc EVX 1; xeng identical; Oink OK). Corollary
     FLIP-RED loses its premise.
  2. CONJECTURE FLIP-EV′ (an event (iii), or an ENT flip at another Odd vertex): flipev_n10 and flipevr_n10 satisfy it; corpus 4,962 candidates, 0 violations.
  3. PROVED (lane, elementary): Lemma SAME-HEAD. Head events re-open only choices between different heads.
  4. READING: the head-feedback clock must be a nested two-head leapfrog (a counter in Ξ path sets) whose carries S4a's W-optimum cannot
     shortcut. Not built.
- NEEDS: none from the owner.
