# Box 177 N5-PAIRDOUBLE: the direct PAIR-LIN attempt — on 𝓛^R_d the key side of a pair is an 8-state automaton (ALIGN), which gives F(l) ≤ 2F(l − 1) + 2 (and F(l) ≤ F(l − 1) + 1 when the pair's two gate orders differ): doubling, not tripling, is the worst the keys allow, and it is attained (dd_d5_F14); so T^R(d) ≤ 2^(d+2) − 2d − 4; the brake that stops persistent doubling must be Ξ-side, and the Ξ capacity per option (PATH-RISE) is exponential, so no polynomial invariant is found
L-NEW successor 55, 2026-11-06 (from 02:48Z, date -u: see the commit). Lead brief BOX 177 (02:46Z): a direct PAIR-LIN attempt; find the
invariant that stops «every flip of the lower pair becomes a move of BOTH level-l movers» from persisting; candidates (i) Ξ-rises
consumed per own flip, (ii) a potential over pairs; state the strongest lemma provable and measure its slack. Labels: PROVED (lane,
unrefereed) / DATA / CONJECTURE / DEAD / READING. Model: RESULTS R104's definition (P-IDEAL-KEYS §0 notation); premises R105 KEYFLIP
(landed), P-IDEAL-KEYS PAIR-KF / CASCADE / RETURN-COUNT (signed, landing as R111). Not a TARGET.md claim. PAIR-LIN, SLOT-TRADE and
G-N5-TIME stay OPEN.

## 0. Answer
- Setting: 𝓛^R_d (R110's definition); for l ≥ 1 the pair p = 2l, q = 2l + 1; b_t := [key_(s_t)(2l − 2, ·) < key_(s_t)(2l − 1, ·)] (the
  order of the pair below, current options); c_t := 0 if b_t else 1 (the option index that W-points to the lower mover with the smaller
  key); γ(j) := [g(p, j) < g(q, j)] for j ∈ {0, 1} (gate constants of the pair). F(l) := flips(2l, 2l + 1) (P-IDEAL-KEYS §0).
- PROVED (lane) Lemma ALIGN. For every state s_t and every l ≥ 1:
  - (a) KP_(s_t)(p) = KP_(s_t)(q) = c_t;
  - (b) if p (or q) moves at step t, it moves to option c_t;
  - (c) ord_(s_t)(p, q) = [s_t(p) = c_t] if s_t(p) ≠ s_t(q), and = γ(s_t(p)) if s_t(p) = s_t(q).
  - Proof. (a) Option k of p and of q W-points to mover 2(l − 1) + k (R110's wiring), so by PAIR-KF (b) both key-prefer the option whose
    W-target has the smaller current key, i.e. c_t. (b) A moving degree-2 mover has both options in its A-set ((F2)) and takes the one
    with the least key under the new state: KP_(s_t), = c_t by (a). (c) If s_t(p) ≠ s_t(q), their current W-targets are the two distinct
    lower movers and (as in CASCADE's proof) ord(p, q) = ord of those targets, which is [p's target is the smaller-key one] = [s_t(p) =
    c_t]. If s_t(p) = s_t(q) = j the prefixes are equal and the gates g(p, j), g(q, j) decide. ∎
- PROVED (lane) Theorem PAIR-DOUBLE. On 𝓛^R_d, in every run, for every 1 ≤ l ≤ d − 1:
  - (a) F(l) ≤ 2 F(l − 1) + 2;
  - (b) if γ(0) ≠ γ(1), then F(l) ≤ F(l − 1) + 1 (status below: machine-proved for F(l − 1) ≤ 30).
  - Hence (with F(0) ≤ 2, P-IDEAL-KEYS LADDER) F(l) ≤ 2^(l+2) − 2, and by PAIR-MOVES T ≤ 2d + 2 Σ_(l=0..d−2) F(l) ≤ 2^(d+2) − 2d − 4.
    This improves the 𝓛^R bounds 3^(l+1) − 1 (LADDER) and T ≤ 3^d − 1 (R108 LEVEL-PRODUCT) to base 2. Still exponential.
  - Proof of (a). Put a_x := [s(x) = c] for x ∈ {p, q} (x is ALIGNED) and Φ := #misaligned ∈ {0, 1, 2}. By ALIGN, along the run:
    a b-change (a flip of the pair below; at most one per step, b being a bit) changes c, so it toggles a_x of every x that does not
    move; a move of x at step t makes a_x = 1 w.r.t. c_t, and happens only if x was misaligned w.r.t. c_t (a move is a change and
    lands on c_t). By ALIGN (c), ord is a_p when a_p ≠ a_q («D-states» 10, 01) and γ(j) when a_p = a_q («S-states» 11 with j = c,
    00 with j = 1 − c). A b-change without a move maps 10 ↔ 01 (ord changes) and 11 ↔ 00 (j is unchanged: 11 under c becomes 00 under
    1 − c, both with j = c; so ord is unchanged). Therefore a step that changes ord either contains a move of p or q, or is a b-change
    step without such a move taken from a D-state (Φ = 1). Let M be the number of steps moving p or q: each removes ≥ 1 from Φ, and a
    b-change taken at Φ_f (before the step's moves) adds 2 − 2Φ_f. So M ≤ Φ_0 + Σ_f (2 − 2Φ_f) (Φ ≥ 0 at the end), and
    F(l) ≤ M + #{b-changes with Φ_f = 1} ≤ Φ_0 + Σ_f h(Φ_f), with h(0) = 2, h(1) = 0 + 1, h(2) = −2. So F(l) ≤ 2 + 2·#{b-changes} =
    2 + 2F(l − 1). ∎
  - Status of (b): PROVED for F(l − 1) ≤ 30 by exhaustive machine case check; CONJECTURE beyond (DATA 0 violations). The dynamics above
    is a path in the 8-state automaton (a_p, a_q, b) with the stated moves; experiments/new/box177/automaton.py computes, for each of the
    four (γ(0), γ(1)), the largest number of ord changes over all paths with exactly k b-changes (DP over ≤ 4k + 6 steps, which covers
    every path: without b-changes each mover moves at most once, so a path has ≤ 3k + 2 steps), k ≤ 30: 2(k + 1) when γ(0) = γ(1) (so (a)
    is tight for the automaton), k + 1 when γ(0) ≠ γ(1). Hand-proof sketch (not checked): with γ(0) ≠ γ(1), ord is ¬u on 00, u on 11
    (u := γ(c), which flips at every b-change) and 1, 0 on 10, 01, so a b-constant segment changes ord at most once; what is missing is
    the charge of the b-change steps.
  - Tightness (DATA): (a) holds with equality on dd_d5_F14 level 3 (F(3) = 14 = 2·6 + 2) and on 60 (run, level) pairs; (b) on 1,183.
- READING (what the theorem says about the doubling): equality in (a) needs Φ_0 = 2 and every b-change taken at Φ = 0 (both aligned)
  followed by moves of BOTH movers before the next b-change — exactly the Lead's «every flip of the lower pair becomes a move of both
  level-l movers», and only on pairs with γ(0) = γ(1) (one mover's gates both below the other's). The key side allows this at every
  level. So the brake that the data show (doubling never runs for 3 consecutive levels, below) is not on the key side.
- PROVED (lane) Lemma PATH-RISE (Ξ side, candidate (i)). For every mover z and every run, the number of steps at which cv(z) rises is
  at most P(z) − 1, P(z) := the number of maximal Ξ-paths from z (choose an option at every mover on the way; P(X) := 1).
  - Proof. cv_s(z) is the integer of the β-set of z's current chain, which is one of the P(z) paths; distinct paths have distinct β-sets
    (distinct options carry distinct β's), hence distinct integers (ENC). By MONO cv(z) never decreases, so it visits each value at most
    once and rises at most P(z) − 1 times. ∎
  - Corollary (with KEYFLIP and RETURN-COUNT): for a degree-2 mover x, moves(x) ≤ 1 + min(KF_x, R(x, 0) + R(x, 1)) and R(x, k) ≤
    P(xt(x, k)) − 1 (R := 0 at X).
  - Why (i) is not polynomial: P(z) is exponential in desc(z) on diamond Ξ-graphs, and box 165 §4 / box 166 §2 showed that the
    key-free (and the 2-key-bit) dynamics realize exponentially many moves there. So the Ξ capacity alone does not give PAIR-LIN; the
    invariant must couple the two sides (a window needs a key flip AND a Ξ-rise; DATA: every inter-move window has both, 304 movers).
- (ii) Potential over pairs: none found. The natural one (Σ_l Φ_l of PAIR-DOUBLE) is exactly what gives base 2; any further gain must
  charge Ξ-rises, and the Ξ-rises of a level-l option come from moves of its Ξ-descendants at ANY level (above included), which breaks
  a level induction.
- DATA (doubling persistence, box177 one-off script in the log): over 190 distinct 2-wide (𝓛^R-convention) runs, the largest number of
  consecutive levels with F(l) ≥ 2F(l − 1) is 2 (7 runs: c4x_d5_F12 [2, 6, 12, 9, 2], dd_d5_F14 [2, 3, 6, 14, 7], nd2_d5_F12, …); 0 in
  118, 1 in 65. Never 3. Weak (no targeted climb).
- Slack (box177/slack.py on the 24 champion files: dd_d5_F14, max_d4_L13, max_d5_L15, L-RED R207 keep (Tstar_d5-d10, TR_d6, TR_d7),
  R208 keep, the box 175 seeds, iso_d4_st9): 304 two-option movers; moves ≤ min(1 + KF, 1 + R0 + R1) with 0 violations, equality on 168;
  the key bound is the tight one on 66 movers with ≥ 2 moves, the Ξ bound on 24; PATH-RISE 0 violations; the path bound is loose (up to
  65 against 3 moves). Typical shape (dd_d5_F14): levels 1-3 key-tight (moves = 1 + KF: 3, 7, 7), level 4 Ξ-tight (KF bound 15, RET
  bound 4 and 2, moves 3 and 2).
- Verdict: PAIR-LIN not proved. Proved: ALIGN, PAIR-DOUBLE (base 2 on 𝓛^R, tight), PATH-RISE. The open step is now exactly: on 𝓛^R,
  a pair with γ(0) = γ(1) cannot have both movers Ξ-renewed after every flip of the pair below for more than O(1) consecutive levels
  (CONJECTURE DBL-O(1); DATA max 2). PAIR-DOUBLE would then give F(l) ≤ poly(l) only if the doubling levels are O(log) many, so even
  DBL-O(1) needs a counting of the non-doubling levels (where (b) or slack applies) to give polynomial F.

## 1. Files (experiments/new/box177/)
- align.py (ALIGN (a)-(c) and PAIR-DOUBLE (a), (b) on runs: all 𝓛^R files of the in-tree boxes 150-176 and claude/l-red 16ae702d, plus
  300 random 𝓛^R genomes, seed 177, every start for d ≤ 3): 6,214 runs, 24,730 (state, level) checks, KPEQ 0, LAND 0, ORD 0; 11,478
  (run, level) pairs, PAIR-DOUBLE (a) 0 violations (60 tight), (b) 0 (1,183 tight), F(0) ≤ 2: 0 violations (log/align.txt).
- automaton.py (the 8-state DP of PAIR-DOUBLE (b)); slack.py (per-mover bounds; log/slack_champions.txt).

## 2. Next (Lead decides)
- Packet candidate: ALIGN + PAIR-DOUBLE (short, premises PAIR-KF / KEYFLIP only; improves R108's 𝓛^R bound to 2^(d+2)). The hand proof
  of (b) would have to be written first.
- Kill side for L-RED: a 2-wide ladder with 3 consecutive doubling levels (γ(0) = γ(1) at each), the configuration the data never show.
