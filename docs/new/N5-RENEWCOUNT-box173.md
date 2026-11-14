# Box 173 N5-RENEWCOUNT: CONJECTURE RENEW-COUNT is DEAD as stated (unbounded width: an alternating Ξ-chain has d = 2 and N/2 renewing lower steps); on 2-wide ladders it survives — the best d 5 witness has I = 2 (not ≈ L/2), and the only proved bound is I ≤ 2 + 2F(d − 2), exponential
L-NEW successor 55, 2026-11-05 (from 23:04Z, date -u: see the commit). Lead brief BOX 173: CONJECTURE RENEW-COUNT (box 171) — a lane
proof, or a kill / growth reading with instances; decisive data I vs L vs d + 1 on the T^R(5) / T*(5) maxima. Labels: PROVED (lane,
unrefereed) / DATA / CONJECTURE / DEAD (instance) / READING. Model: RESULTS R104's definition (P-IDEAL-KEYS §0). Not a TARGET.md claim.
G-N5-TIME and SLOT-TRADE stay OPEN.

## 0. Answer
- Definitions (box 171, P-IDEAL-KEYS §0): τ := the top level; a step is TOP-ONLY if all its movers have level τ, LOWER otherwise;
  I := the number of maximal top-only intervals; L := the number of lower steps; a RENEWING lower step is a lower step t − 1 followed by a
  top-only step t (t ≥ 2), i.e. the step RENEW (P-IDEAL-KEYS §5 (a)) is about. #renewing = I, or I − 1 if an interval starts at step 1.
- (1) DEAD: CONJECTURE RENEW-COUNT as stated in box 171 («on every IDEAL-ACYC run, the lower steps that renew a top mover (RENEW's step
  t − 1) number O(d) (or poly(d), for the polynomial version of SLOT-TRADE)»).
  - Instance family C_m (m even; experiments/new/box173/chain.py; files box173/out/chain_C8.json sha1 6c9962ba…, chain_C20.json sha1
    e5e65ab3…): d = 2 levels, N = m, T = m, pattern LTLT…LT, I = m/2 renewing lower steps. Unbounded at fixed d.
  - Proof (§1, by hand) and machine replay: chain.py (run = one mover per step, a_m down to a_1) and box150/check.py on C_8 and C_20
    (XSIM 0, every R105 check 0).
  - What dies is only the width-free form. C_m has m/2 movers per level. SLOT-TRADE lives on 2-wide ladders (R109's 𝓛_d, R110's 𝓛^R_d).
- (2) What survives: CONJECTURE RENEW-COUNT_2 (restricted): on 𝓛^R_d (and on R109's 𝓛_d), I ≤ poly(d) (strong form: I = O(d)).
  - DATA on the maxima (box171/frozen.py; files copied from claude/l-red into experiments/new/box172/inst/, sha1s in P-IDEAL-KEYS §8):
    | genome | d | T | L | I | d + 1 | pattern |
    | --- | --- | --- | --- | --- | --- | --- |
    | max_d4_L13 (T = T^R(4) = 13, L-RED R197) | 4 | 13 | 9 | 4 | 5 | LTLTLLLLLTLTL |
    | max_d5_L15 (best known d 5 witness, L-RED R202; T^R(5) ≥ 15, T ≥ 16 not decided) | 5 | 15 | 13 | 2 | 6 | LTLLTLLLLLLLLLL |
    | dd_d5_F14 (L-RED R197 lag) | 5 | 14 | 14 | 0 | 6 | all L |
  - So the box 171 reading «I ≈ L/2 on the T^R-type maxima» does NOT continue to d 5: I/L = 4/9 at d 4, 2/13 at d 5. Over the 163
    distinct (𝓛^R genome, stored start) pairs in the in-tree boxes 150-173 and in claude/l-red 5e98e81e experiments/red, max I by d =
    1, 2, 3, 4, 5, 6, 8 is 1, 2, 4 (fix3_8), 4 (max_d4_L13), 3 (tri_d5_L12), 2, 2: I ≤ d + 1 everywhere, I ≤ d except at d 3 (box 171's
    larger d 5 value 6 is g5_a, not an R197 ladder). No growth with d is visible. DATA only; d ≤ 5 is small and T^R(5) is not known.
  - Climbs (box173/climbR.py on 𝓛^R_d maximizing (I, T); logs box173/log/): from max_d4_L13 (4 × 30,000 steps): I stays 4; from
    max_d5_L15 (4 × 30,000): I stays 2; d 6 from random (6 × 20,000): I ≤ 2. Weak (local search, same plateau as box 171).
- (3) PROVED (lane; from P-IDEAL-KEYS PAIR-MOVES, i.e. R105 KEYFLIP + PAIR-KF): on 𝓛^R_d (d ≥ 2), I ≤ (number of top-only steps) ≤
  moves(2d − 2) + moves(2d − 1) ≤ 2 + 2F(d − 2), F(l) := flips(2l, 2l + 1); with P-IDEAL-KEYS LADDER, I ≤ 2 + 2 min(T, 3^(d−1) − 1).
  Exponential in d. Proof: every top-only step moves a top mover; PAIR-MOVES bounds each top mover's moves by 1 + F(d − 2). ∎
  - On max_d4_L13 the bound is 2 + 2·4 = 10 against I = 4; top movers 6, 7 move 4 + 3 = 7 times, 4 of them in top-only steps.
- (4) Why the chain does not port to 2-wide ladders (READING): in C_m every top-only interval is a DIFFERENT top mover, each moving once.
  On 𝓛^R_d there are two top movers, so I > 2 needs a top mover to move again; between two moves of one top mover its key preference
  must flip (R105 KEYFLIP), i.e. pair d − 2 must flip at a lower step, and the next top-only interval also needs a Ξ-rise of the option
  it takes at the lower step just before (RENEW). A 2-wide RENEW-COUNT proof has to bound how often both can coincide; the only bound
  we have is the key side (F(d − 2)), which is the SLOT-TRADE quantity again. No proof; no kill.
- Verdict: RENEW-COUNT DEAD as stated (width); RENEW-COUNT_2 OPEN, DATA I ≤ d + 1 on all R197 ladders seen, I = 2 on the best d 5
  witness. G-N5-TIME OPEN.

## 1. Proof that C_m runs as claimed (PROVED (lane); R104 definition and R105 ENC only)
- C_m: movers a_1, …, a_m (index i − 1), m even; lev(a_i) = 1 for odd i, 0 for even i. Option 0 of a_i: Ξ-target a_(i+1) (X for i = m),
  β even of rank 2i, gate 2(i − 1); option 1: Ξ-target X, β odd of rank 2i + 1, gate 2i − 1. Both options of a level-1 mover W-point to
  a_m (level 0, since m is even). Distinct gates and ranks; Ξ-edges a_i → a_(i+1) only (acyclic). Start: all on option 1.
- Values (ENC): v(a_i, 1) = −2^(2i+1); v(a_i, 0) = 2^(2i) + cv(a_(i+1)) (i < m), v(a_m, 0) = 2^(2m).
- Claim: s_t (t = 0, …, m) has a_j on option 0 iff j > m − t. Induction. At s_t: for j > m − t, cv(a_j) = Σ_(k=j..m) 2^(2k) > 0; for
  j ≤ m − t, cv(a_j) = −2^(2j+1).
  - i < m − t: v(a_i, 0) = 2^(2i) − 2^(2i+3) = −7·2^(2i) < −2·2^(2i) = v(a_i, 1): A = {1}.
  - i = m − t ≥ 1: v(a_i, 0) = 2^(2i) + (a positive sum, or nothing if t = 0) > 0 > v(a_i, 1): A = {1, 0}.
  - i > m − t: current option 0 with positive value, option 1 negative: A = {0}.
  - So a_(m−t) is the only mover with two available options. Its keys: at level 0, (gate); at level 1, (g(a_m, s(a_m)), gate) with
    the same prefix for both options. Either way option 0 (smaller gate) has the smaller key, so step t + 1 moves exactly a_(m−t) to
    option 0. At s_m every A-set is a singleton and the run stops: T = m.
- a_(m−t) has level 1 iff m − t is odd iff t is odd (m even): steps 1, 3, … are LOWER (a level-0 mover alone), steps 2, 4, … TOP-ONLY.
  I = m/2; every interval starts at an even step a ≥ 2 after the lower step a − 1, so all m/2 lower steps at odd positions are renewing.
  d = 2 for every m. ∎
- Consistency with RENEW: at step a = 2j the top mover a_(m−a+1) takes option 0, whose value rose at step a − 1 when its Ξ-target
  a_(m−a+2) moved: exactly RENEW (a) (ii), (iii).

## 2. Files (experiments/new/box173/)
- chain.py (C_m generator + run check), climbR.py (𝓛^R_d climb on (I, T)); out/chain_C8.json, out/chain_C20.json, out/climbR_d6_s61.json
  (best d 6 climb, I 2); log/climbR_*.log.

## 3. Next (Lead decides)
- RENEW-COUNT_2 needs exact data: max I over 𝓛^R_d (d 3, 4) by SAT (L-RED's xcnf with a top-only-interval counter), and I on any T^R(5)
  witness with T ≥ 16 if L-RED's cubes find one. A proof route would charge each re-move of a top mover to a pair-(d − 2) flip that is
  also a Ξ-rise step (RENEW + KEYFLIP); no such charging lemma is known.
