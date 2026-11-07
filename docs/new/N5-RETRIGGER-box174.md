# Box 174 N5-RETRIGGER: the lane proof attempt of RENEW-COUNT_2 — every top-only block that is not the last needs a LOWER Ξ-ANCESTOR of a top mover to move right after it (RE-TRIGGER, PROVED), so I ≤ 1 + (moves of the lower Ξ-ancestors of the top); on 2-wide ladders this gives I ≤ 3^(k+1) when those ancestors sit at levels ≤ k, i.e. poly(d) if k = O(log d); the attempt breaks when a top mover has Ξ-ancestors near the top, whose moves are bounded only by the SLOT-TRADE quantity F(τ − 2); the ping-pong kill candidate was not realized
L-NEW successor 55, 2026-11-05 (from 23:47Z, date -u: see the commit). Lead brief BOX 174 (23:46Z): lane proof attempt of
RENEW-COUNT_2 on 2-wide 𝓛^R_d / 𝓛_d (I ≤ d + 1, or poly(d)); if it breaks, build the configuration as a kill candidate, XSIM 0.
Labels: PROVED (lane, unrefereed) / DATA / CONJECTURE / READING. Model: RESULTS R104's definition (P-IDEAL-KEYS §0 notation);
premises R105 XI-NEW and RISE (landed); P-IDEAL-KEYS PAIR-MOVES / LADDER (frozen, unrefereed: results using them are lane-only).
Not a TARGET.md claim. G-N5-TIME, SLOT-TRADE and RENEW-COUNT_2 stay OPEN.

## 0. Answer
- Notation: τ = top level; a BLOCK is a maximal interval [a, b] of top-only steps (I = number of blocks); A_top := the LOWER movers
  (level < τ) that have some top mover as a strict Ξ-descendant; D_top := the movers (any level) that are a strict Ξ-descendant of some
  top mover.
- PROVED (lane) Lemma RE-TRIGGER (IDEAL-ACYC, any degree, any width). If [a, b] is a block with b < T, then step b + 1 is lower, and every
  least-level mover h of step b + 1, moving to w, has on the chain of (h, w) under s_(b−1) a top mover z ∈ Mv_b with z ∈ D(h). In
  particular h ∈ A_top.
  - Proof. b + 1 ≥ 2 is a step that is not top-only (maximality), so its least level is < τ and h is a lower mover. R105 XI-NEW / RISE
    (signed form, body item (e) (b), (c)) at t = b + 1: the set Z_(b+1) of movers z ≠ h on the chain of (h, w) under s_(b−1) with
    z ∈ Mv_b is nonempty and every such z is a strict Ξ-descendant of h. Mv_b contains only top movers (b is top-only). ∎
- PROVED (lane) Corollary TOP-SINK. If A_top = ∅ (no lower mover Ξ-reaches a top mover), every block ends at T, so I ≤ 1.
- PROVED (lane) Corollary CHARGE-I (any degree, any width).
  - #{blocks with b < T} ≤ #{lower steps that move a mover of A_top} (block ↦ step b + 1, injective: distinct blocks have distinct b).
  - #{blocks with a ≥ 2} ≤ #{lower steps that move a mover of D_top} (block ↦ step a − 1; RENEW (a) (iii): the renewing z ∈ Mv_(a−1) is a
    strict Ξ-descendant of the moving top mover — z may itself be a top mover, which is why D_top is taken over all levels).
  - Hence I ≤ 1 + min(Σ_(x ∈ A_top) moves(x), #{lower steps moving D_top}) (the «1» is the last block, resp. a block at a = 1).
  - A first version of the second bullet restricted D_top to lower movers; it FAILED on 31 runs (DATA, box174/retrig.py before the fix):
    the renewing descendant can be a top mover moving together with lower movers.
- PROVED (lane) on 𝓛^R_d (premises add P-IDEAL-KEYS PAIR-MOVES and LADDER, unrefereed). If every mover of A_top has level ≤ k, then
  I ≤ 1 + Σ_(l=0..k) 2 (1 + F(l − 1)) ≤ 1 + 2 Σ_(l=0..k) 3^l ≤ 3^(k+1) (F(−1) := 0; level-0 movers move ≤ 1; F(l) ≤ 3^(l+1) − 1).
  So RENEW-COUNT_2 in its poly(d) form holds on every ladder family whose top movers have Ξ-ancestors only at levels ≤ c·log_3 d, and
  I ≤ 1 + 2(k + 1)(1 + max_(l<k) F(l)) in general.
- Where the attempt breaks (exact): CHARGE-I is tight-type, not lossy: on fix3_8 (d 3, T 8, pattern TLTLLTLT, A_top at levels 0, 1)
  I = 4 = 1 + #{lower steps moving A_top}. The only bound on how often an A_top mover x at level l moves is 1 + F(l − 1) (PAIR-MOVES), and
  F(l − 1) for l near τ is exactly the quantity SLOT-TRADE / PAIR-LIN must bound. On the maxima A_top reaches high levels: max_d4_L13
  levels 0, 1, 1, 2 (= τ − 1); max_d5_L15 levels 0, 1, 2, 2, 3, 3 (= τ − 1); g5_a (d 5, I 6) one A_top mover on each level 0-3. So a
  proof of I ≤ poly(d) through CHARGE-I needs moves(x) ≤ poly(d) for high-level A_top movers, i.e. polynomial pair flips — circular.
- Kill candidate (READING; NOT realized): PING-PONG on 𝓛^R_d. Top movers u, v; a mover q of level τ − 1 with v ∈ D(q) (q ∈ A_top), a lower
  mover p ∈ D(u); each round: top move (raises cv(v)) → q re-triggered → lower block flips pair τ − 2 (u's key bit, PAIR-KF) and raises
  cv(p) → u renewed → … . It gives I ≈ moves(q) ≈ 1 + F(τ − 2) if the lower block can settle between rounds. Not built: random and seeded
  climbs (below) never exceeded the seeds; the hard part is that the lower block must STOP (all lower movers settled) after each flip of
  pair τ − 2, while the clocks that flip pair τ − 2 often (dd_d5_F14: 14 flips) never pause (pattern all L).
- Verdict: no proof, no kill. RENEW-COUNT_2 is reduced (lane) to «lower Ξ-ancestors of the top move poly(d) times», which is implied by
  PAIR-POLY / polynomial T and holds unconditionally when those ancestors are low (levels O(log d)). OPEN.

## 1. DATA (experiments/new/box174/retrig.py; corpus = in-tree boxes 150-174 + claude/l-red 5e98e81e experiments/red JSON genomes,
   stored starts; plus 400 random genomes (box172 generator, seed 174), every start when ≤ 64)
- 5,846 runs (3 files skipped: Ξ-cyclic): 1,291 blocks, 295 re-triggers. RETRIG (RE-TRIGGER) 0 violations; BOUNDA (first bullet of
  CHARGE-I) 0; BOUNDD (second bullet, D_top over all levels) 0; TOPSINK 0 on the 1,707 runs with A_top = ∅.
- Per-file detail (retrig.py -v): max_d4_L13 I 4, #lower steps moving A_top (nA) 8, nD 5; max_d5_L15 I 2, nA 12, nD 4; fix3_8 I 4, nA 3,
  nD 4; g5_a I 6, nA 11, nD 6; big_d4_k3_W3 (degree 3) I 6, nA 25.
- Searches (all on 𝓛^R_d unless noted; logs box174/log/, best genomes box174/out/): climbI2.py random restarts (d 3, 4, 5; 20 × 40,000
  steps; and R109-style general W-targets at d 4): best I 3 (T ≤ 7); sampleI.py d 2, 20,000 random genomes × all 16 starts: max I 2
  (pattern TLT); pingclimb.py (mutating only the top two levels' fields and Ξ-targets, seeded with max_d4_L13, max_d5_L15, dd_d5_F14,
  6 × 40,000 steps, annealing 0.03): best I 4 (the seed max_d4_L13), 3 from the d 5 seeds (at T 6). No I above d + 1 anywhere.

## 2. Files (experiments/new/box174/)
- retrig.py (RE-TRIGGER, CHARGE-I, TOP-SINK checks; -v per-file table), climbI2.py, sampleI.py, pingclimb.py; out/*.json (best climb
  genomes, I ≤ 4), log/*.log.

## 3. Next (Lead decides)
- RE-TRIGGER and CHARGE-I are short and self-contained (premises R105 XI-NEW / RISE only): candidates for a packet with the box 173 kill
  if the Lead wants them signed.
- Exact side: max I on 𝓛^R_d with A_top restricted to level τ − 1 (the ping-pong shape) by SAT would decide the kill candidate at d ≤ 5.
