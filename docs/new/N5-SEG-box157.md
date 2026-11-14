# Box 157 N5-SEG: Lemma SEG and Lemma SEG-ONCE (PROVED, lane) give Corollary LEVEL-PRODUCT: T + 1 ≤ Π_l (n_l + 1) at degree ≤ 2 (3^d − 1 on 2-wide ladders, below EXACT-ENERGY's 4^d − 1); REPLAY DEAD on R202's max_d5_L15 (the post-reset segment is longer and all-new)
L-NEW successor 51, 2026-11-04 (date -u: see the commit). Lead GO 11:24Z (BOX 157 SEGMENT / REPLAY, with my kill test). Labels:
PROVED (lane), DATA, DEAD, CONJECTURE, READING. Model: P-IDEAL-RED §0 = RESULTS R104's definition, with RESULTS R105's notation.
Not a TARGET.md claim. LEVEL-PRODUCT is an EXPONENTIAL bound. IDEAL-ACYC-POLY and G-N5-TIME stay OPEN.

## 0. Answer
- PROVED (lane), §1:
  - Lemma SEG (any degree, any width). Freeze every mover of level ≤ l at its option at s_(a−1). On a stretch of steps [a, b] with no
    move at level ≤ l, the frozen genome reproduces the run exactly.
  - Lemma SEG-ONCE (degree ≤ 2). On such a stretch, every mover of level l + 1 moves at most once. For l = −1: every level-0 mover moves
    at most once in the whole run.
  - Corollary LEVEL-PRODUCT (degree ≤ 2). With C_l the number of steps that move some mover of level ≤ l, and n_l the number of
    degree-2 movers on level l:
    - C_(l+1) + 1 ≤ (C_l + 1)(n_(l+1) + 1);
    - hence T + 1 ≤ Π_l (n_l + 1).
  - On the 2-wide ladder (n_l = 2, d levels) this gives T ≤ 3^d − 1. EXACT-ENERGY (RESULTS R105) gives 2^N − 1 = 4^d − 1 there.
  - In general Π_l (n_l + 1) ≤ 2^(number of degree-2 movers), so LEVEL-PRODUCT is never worse than EXACT-ENERGY at degree 2.
- DATA (box157/segcheck.py): 0 violations of SEG, SEG-ONCE, COUNT and PRODUCT.
  - Corpus: 59 runs, 652 intervals, including the champions max_d4_L13, max_d5_L15, dd_d5_F14 and the degree-3 genomes of box 139
    (SEG only at degree 3).
  - Random: 34,934 runs of the box 150 random genomes (every start for N ≤ 8), 57,755 intervals.
  - Negative control BADLEV=2 (ONCE tested one level too high): 112 violations on the corpus. So the level index in SEG-ONCE matters.
  - Max (T + 1) / Π (n_l + 1): 1/3 on the corpus. It reaches 1 only on trivial random genomes (one degree-2 mover).
- DEAD: REPLAY (my box 157 proposal: «after a level-0 reset, the next segment is a sub-run of a segment already seen»).
  - Killed by L-RED R202's max_d5_L15 (claude/l-red 05c48415, experiments/red/r202/max_d5_L15.json; copy box157/max_d5_L15.json, sha1
    ba963ace…; N 10, 2-wide ladder d 5, degree 2, from its stored start T 15).
  - Segments at its level-0 moves (box157/seg.py, L = 0):
    - t1-6: length 6, mover sets (5) (9) (7) (6 8) (9) (4);
    - t7 and t8: level-0 steps, movers {0, 2, 3} and {1};
    - t9-15: length 7, mover sets (4) (6 7 8 9) (5) (3) (7) (6 9) (4).
  - So the post-reset segment is LONGER than every earlier segment (7 > 6), visits 7 states (above level 0) never seen before, and its
    mover pattern is no replay of the first.
  - On the smaller champions the later segment is a pattern replay (max_d4_L13, g4_L12, x3_L8) or shorter (dbl_*, dd_d5_F14,
    c4x_d5_F12). Even there it visits new states (NEWSTATES = length in every case). So «state replay» is false on every one of them.
- L-RED target (nested doubling via resets; this shape is the one that killed REPLAY):
  - Wanted: a ladder in which every level-0 reset (≤ 2 per run: SEG-ONCE) is followed by a segment longer than the one before it.
  - Recursively, the same at level 1 inside each segment (≤ 2 level-1 moves per level-0 segment, SEG-ONCE with l = 0).
  - LEVEL-PRODUCT says this is the ONLY way to beat linear: the 3^d room comes exactly from (C_l + 1)(n_(l+1) + 1).
  - Concrete seed: max_d5_L15 (above). Its level-1 cuts (seg.py, L = 1) are t7, t8, t12. So the second level-0 segment is itself cut once
    at level 1 (t12), into 3 + 3 steps. The first segment has no level-1 cut.
- READING:
  - LEVEL-PRODUCT turns «T/N unbounded on ladders?» into a counting question about resets: how many of the (C_l + 1)(n_(l+1) + 1)
    slots the run actually fills.
  - In the exact champions the fill is tiny. max_d5_L15 has C_0 = 2 of 2 possible, and C_1 = 3 of up to 8.
  - A linear bound needs «most slots stay empty». An exponential family needs the slots filled level after level.

## 1. Proofs (deg as stated; notation of P-IDEAL-RED §0)
- Lemma SEG (IDEAL-ACYC, any degree, any width).
  - Setting. Let l ≥ −1. Let [a, b] ⊆ [1, T] be an interval of steps such that no step t ∈ [a, b] moves a mover of level ≤ l. Let H be
    the genome G with every mover x of level ≤ l given the single option s_(a−1)(x) (same W-target, Ξ-target, β and gate).
  - Identify a state of H with the state of G that has s_(a−1)(x) at every frozen mover.
  - Claim: the run of H from s_(a−1) has s_(a−1), s_a, …, s_b as its first b − a + 2 states.
- Proof.
  - H is an IDEAL-ACYC genome: its options are a subset of G's, so ranks and gates stay distinct, W-targets still lie one level down,
    and the Ξ-graph has fewer edges.
  - Induction on t ∈ [a, b]: assume H is at s := s_(t−1). Every frozen mover has its frozen option at s, because no step in [a, t − 1]
    moved it.
  - (i) For a non-frozen mover x and any of its options k, the chain of (x, k) under s is the same in H and in G: each frozen mover
    passed is at its only H-option, which is its G-option at s. So Ξ^H_s(x, k) = Ξ^G_s(x, k), and A^H_s(x) = A^G_s(x).
  - (ii) For a frozen mover, A^H_s is a singleton.
  - (iii) Keys. Let s′ := s_t. The frozen movers keep their options (t ∈ [a, b]). So, level by level from level 0, H's new state agrees
    with s′: the frozen movers by (ii); a non-frozen x by (i) and because its key_(s′) reads only levels < lev(x), already equal. Both
    genomes then take the key-least option of the same set.
  - (iv) Stop rule. G performs step t, so s′ ≠ s and some non-frozen mover has |A| ≥ 2. So H does not stop either, and its new state
    is s′. ∎
- Lemma SEG-ONCE (IDEAL-ACYC, degree ≤ 2, any width). With l, [a, b] as in SEG, every mover x of level l + 1 has
  |{t ∈ [a, b] : x ∈ Mv_t}| ≤ 1.
- Proof.
  - Suppose x moves at t1 < t2 in [a, b], consecutively (no move of x in between). Then deg(x) = 2, and x goes b′ → a′ at t1 and
    a′ → b′ at t2.
  - At t1 both options are available and x takes the key-smaller one under the keys of s_(t1). So KP_(s_(t1))(x) = a′. Likewise
    KP_(s_(t2))(x) = b′.
  - The keys of x's options read only movers of level ≤ l (RESULTS R105 LOCAL, «a key only on the states below its level»; the body
    form «(c) key_s(x, k) = key_(s′)(x, k) whenever s and s′ agree on every mover of level < lev(x).»).
  - Those movers do not move in [a, b], so s_(t1) and s_(t2) agree on them, and KP_(s_(t1))(x) = KP_(s_(t2))(x). Contradiction.
  - (This is the KEYFLIP argument of RESULTS R105 with KF = 0 on the stretch.) ∎
- Corollary LEVEL-PRODUCT (IDEAL-ACYC, degree ≤ 2, any width).
  - Statement. C_(−1) := 0, C_l := |{t ∈ [1, T] : Mv_t contains a mover of level ≤ l}|, n_l := the number of degree-2 movers of
    level l. Then C_(l+1) + 1 ≤ (C_l + 1)(n_(l+1) + 1) for every l ≥ −1, hence T + 1 ≤ Π_l (n_l + 1).
  - Proof.
    - The steps counted by C_(l+1) but not by C_l lie in the maximal intervals of [1, T] that avoid the C_l steps. There are at most
      C_l + 1 such intervals.
    - In each such interval, each such step moves some mover of level l + 1. That mover has degree 2 (degree-1 movers never move), and
      by SEG-ONCE it moves at most once in the interval. So each interval contains at most n_(l+1) such steps.
    - Hence C_(l+1) ≤ C_l + (C_l + 1) n_(l+1), which is the first claim.
    - Every step moves some mover, so T = C_top with top the largest level. Induction from C_(−1) + 1 = 1 gives the product. ∎
  - Lemma SEG is not needed for LEVEL-PRODUCT. It is stated because it lets every stretch be studied as a run of a smaller genome:
    levels ≤ l become fixed context.
- Does NOT claim: any polynomial bound. LEVEL-PRODUCT is exponential in the number of levels with ≥ 1 degree-2 mover. No claim at
  degree ≥ 3 for SEG-ONCE or LEVEL-PRODUCT (SEG holds at any degree).

## 2. Files and status
- experiments/new/box157/:
  - seg.py: segments and REPLAY test (env L);
  - segcheck.py: SEG / ONCE / COUNT / PROD checker; ALL=1 for all starts; BADLEV=2 negative control;
  - max_d5_L15.json: R202 copy.
- PROVED (lane): SEG, SEG-ONCE, LEVEL-PRODUCT. DEAD: REPLAY (max_d5_L15). OPEN: IDEAL-ACYC-POLY, G-N5-TIME.
