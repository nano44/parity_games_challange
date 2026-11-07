# Packet P-IDEAL-ALIGN (box 178): on 2-wide R197 ladders both movers of a pair key-prefer the same option and every move lands on it (ALIGN); a pair flips at most 2F + 2 times when the pair below flips F times (PAIR-DOUBLE, tight), so T^R(d) ≤ 2^(d+2) − 2d − 4; and the current value of a mover rises at most (number of its maximal Ξ-paths) − 1 times (PATH-RISE)
L-NEW successor 55 (Opus 5.5), D14 / D18 / D20; Lead brief BOX 178 (2026-11-06 03:23Z): «freeze packet P-IDEAL-ALIGN with ALIGN +
PAIR-DOUBLE (a) + Corollary T^R(d) ≤ 2^(d+2) − 2d − 4 + PATH-RISE». Written 2026-11-06 from 03:22Z (date -u: see the commit). FROZEN
at push: later text goes into docs/new/P-IDEAL-ALIGN-fixes.md (append-only). Source: docs/new/N5-PAIRDOUBLE-box177.md §0 (successor 55);
this packet carries every proof in full and is checked against this text only; no other file carries a proof of a statement below.
Labels: PROVED (L-NEW 55, unrefereed) / DATA / READING (not to sign). Not a TARGET.md claim. Every statement is about the IDEAL model of
RESULTS R104 only. The bounds proved are exponential. PAIR-LIN, DBL-O(1), SLOT-TRADE and G-N5-TIME stay OPEN.

## To sign, and what is not to sign
| § | statement | label | hypotheses |
| --- | --- | --- | --- |
| §2 | Lemma ALIGN (a), (b), (c) | PROVED | 𝓛^R_d, a level l ≥ 1 |
| §3 | Lemma KP-MOVE (a), (b); Lemma F0 | PROVED | KP-MOVE: IDEAL-ACYC, a mover of degree 2; F0: 𝓛^R_d |
| §4 | Theorem PAIR-DOUBLE | PROVED | 𝓛^R_d, a level l ≥ 1 |
| §5 | Corollary MOVES; Corollary T-BOUND | PROVED | 𝓛^R_d |
| §6 | Lemma PATH-RISE | PROVED | IDEAL-ACYC, any degree |
| §7 | DATA, machine checks, excluded parts (incl. the γ(0) ≠ γ(1) bound), TARGET diff | DATA / READING (not to sign) | |

- Premises (LANDED only).
  - RESULTS R104 (P-N5-REALIZE): ONLY its definition of the IDEAL model and of the Ξ-graph, restated in §0. No theorem of R104 is used.
  - RESULTS R105 (P-IDEAL-RED), two items only, quoted verbatim from the R105 statement (RESULTS l. 10155 on trunk b5d154ad), used in
    §6 only: «(ENC) the Ξ-order of β-sets is the order of the integers Σ ±2^rank (+ for even parity), so, with ε(x, k) := ±2^rank(x, k)
    (+ for even parity), the value of option (x, k) is ε(x, k) plus the current value of its Ξ-target (ε(x, k) alone if the Ξ-target is
    the exit X)» and «(MONO) the current Ξ-value of every mover never decreases along a run». RESULTS Erratum E-2 corrects R105's
    CHAINED binder (E2a), TOP-MONO's RANK_t (E2b) and KEYFLIP's moves(x) (E2c); none of these three items is used here, so E-2 does not
    bear (moves(x) is defined in §0 with the E-2 (E2c) binder anyway).
  - RESULTS R110 (P-IDEAL-FLIP): ONLY its definition of 𝓛^R_d, quoted verbatim from its statement: «the 2-wide degree-2 ladders in
    L-RED's R197 convention (movers 2l and 2l + 1 on level l, all of degree 2, no other movers, option k of a mover of level l ≥ 1
    W-pointing to mover 2(l − 1) + k)», levels 0, …, d − 1. No theorem of R110 is used.
  - Not used: R105 KEYFLIP (its degree-2 argument is re-proved in §3 as KP-MOVE), R105 LOCAL and every other R105 item, R106-R109,
    the signed but not yet landed packet P-IDEAL-KEYS (R111; its PAIR-KF and LADDER are not used: §2 and §3 re-prove what is needed),
    docs/lit, docs/sources, any other lane file. No machine premise is used by any signed item.
- Each statement lists its hypotheses and a paragraph «does NOT claim».

## 0. The model (RESULTS R104's definition, as restated in P-IDEAL-FLIP §0 and P-IDEAL-KEYS §0) and the notation of this packet
- A genome G has N ≥ 1 movers x, each with a level lev(x) ∈ {0, 1, …} and deg(x) ≥ 1 options (x, k). Each option has a W-target
  wt(x, k) (a mover of level lev(x) − 1; none at level 0), a Ξ-target xt(x, k) (a mover or the exit X), a β with a rank (distinct over
  all options) and a parity, and a gate index g(x, k) (distinct over all options). There is a start s_0. A state s picks one option
  s(x) per mover.
- Ξ-graph: an edge x → xt(x, k) for every option whose Ξ-target is a mover. IDEAL-ACYC: it is acyclic (in particular no option has its
  own mover as Ξ-target).
- Under s, the chain of (x, k) is (x, k), (y_1, s(y_1)), (y_2, s(y_2)), … with y_1 = xt(x, k), y_(j+1) = xt(y_j, s(y_j)), up to the
  first option whose Ξ-target is X. Its Ξ-value Ξ_s(x, k) is the set of β's on it. Two sets P ≠ Q are compared by the β of largest
  rank in P △ Q: the set containing it is better (P ▷ Q) if that β's parity is even, worse if odd.
- A_s(x) := {s(x)} ∪ {k : Ξ_s(x, k) ▷ Ξ_s(x, s(x))}.
- key_s(x, k) := (g(x, k)) if lev(x) = 0, else key_s(wt(x, k), s(wt(x, k))) followed by g(x, k); compared lexicographically.
- Step. If every A_(s_(t−1))(x) is a singleton, the run stops. Otherwise s_t is defined level by level, lowest level first:
  s_t(x) := the option in A_(s_(t−1))(x) with the least key_(s_t)(x, ·) (keys under the NEW state). If s_t = s_(t−1), the run stops
  without that step. T := the number of steps. Mv_t := {x : s_t(x) ≠ s_(t−1)(x)} for t ∈ [1, T] (nonempty for every such t).
- Facts immediate from the definition. (F1) key_s(x, k) is a tuple of length lev(x) + 1 whose last entry is g(x, k); so the keys of
  two distinct options of the same level differ (equal length, distinct last entries), and the least key over any set of options of
  one mover is attained by exactly one option. (F2) If x ∈ Mv_t, then s_t(x) ∈ A_(s_(t−1))(x) \ {s_(t−1)(x)}, so Ξ_(s_(t−1))(x,
  s_t(x)) ▷ Ξ_(s_(t−1))(x, s_(t−1)(x)); if moreover deg(x) = 2, then s_(t−1)(x) is the other option of x.
- Notation of this packet (all derived from the definition):
  - moves(x) := #{t ∈ [1, T] : x ∈ Mv_t} (the binder of Erratum E-2 (E2c)).
  - KP_s(x) := the option k of x with the least key_s(x, k) (unique by (F1)); KF_x := #{t ∈ [1, T] : KP_(s_t)(x) ≠ KP_(s_(t−1))(x)}.
  - For two distinct movers u, w of one level: ord_s(u, w) := [key_s(u, s(u)) < key_s(w, s(w))]; a FLIP of (u, w) at step t ∈ [1, T]
    means ord_(s_t)(u, w) ≠ ord_(s_(t−1))(u, w); flips(u, w) := the number of steps t ∈ [1, T] at which (u, w) flips.
  - On 𝓛^R_d (d ≥ 1): for 0 ≤ l ≤ d − 1, F(l) := flips(2l, 2l + 1). For 1 ≤ l ≤ d − 1 and a state s: p := 2l, q := 2l + 1,
    b_l(s) := ord_s(2l − 2, 2l − 1) (the order of the pair below), c_l(s) := 0 if b_l(s) is true, else 1 (the option index that
    W-points to the lower mover whose current option has the smaller key); γ_l(j) := [g(p, j) < g(q, j)] for j ∈ {0, 1}.
  - v_s(x, k) := the integer Σ_(β ∈ Ξ_s(x, k)) ±2^rank(β) (+ for even parity); cv_s(x) := v_s(x, s(x)); a RISE of cv(z) at step t
    means cv_(s_t)(z) > cv_(s_(t−1))(z).
  - A maximal Ξ-path from a mover z: a sequence (y_0, k_0), (y_1, k_1), …, (y_r, k_r) of options with y_0 = z, y_(i+1) = xt(y_i, k_i)
    for i < r, and xt(y_r, k_r) = X (one option chosen at every mover on the way). P(z) := the number of maximal Ξ-paths from z. The
    chain of (z, s(z)) under s is one of them.

## 2. Lemma ALIGN (PROVED)
- Hypotheses: G ∈ 𝓛^R_d; 1 ≤ l ≤ d − 1; p = 2l, q = 2l + 1; any run; s any state of the run, t ∈ [1, T] any step.
- (a) KP_s(p) = KP_s(q) = c_l(s).
- (b) If x ∈ {p, q} and x ∈ Mv_t, then s_t(x) = c_l(s_t).
- (c) ord_s(p, q) = [s(p) = c_l(s)] if s(p) ≠ s(q), and ord_s(p, q) = γ_l(j) if s(p) = s(q) = j.
- Proof. (a) For x ∈ {p, q} and k ∈ {0, 1}, wt(x, k) = 2(l − 1) + k (R110's wiring), so key_s(x, k) = key_s(2l − 2 + k, s(2l − 2 + k))
  followed by g(x, k). The two prefixes are keys of options of the two distinct movers 2l − 2, 2l − 1 of level l − 1; by (F1) they are
  tuples of equal length that differ, so the lexicographic comparison of key_s(x, 0) and key_s(x, 1) is decided inside the prefixes:
  key_s(x, 0) < key_s(x, 1) iff b_l(s). So KP_s(x) = 0 iff b_l(s), i.e. KP_s(x) = c_l(s), for x = p and x = q.
  (b) By (F2), s_t(x) is the other option than s_(t−1)(x), and both options lie in A_(s_(t−1))(x); the step gives x the option of that
  set with the least key_(s_t)(x, ·), i.e. KP_(s_t)(x) = c_l(s_t) by (a).
  (c) key_s(p, s(p)) = key_s(w_p, s(w_p)) followed by g(p, s(p)) with w_p := 2l − 2 + s(p), and the same for q. If s(p) ≠ s(q), then
  {w_p, w_q} = {2l − 2, 2l − 1}, the prefixes differ (F1) and decide: ord_s(p, q) = [key of w_p's current option < key of w_q's] = [w_p
  is the lower mover with the smaller key] = [s(p) = c_l(s)]. If s(p) = s(q) = j, the prefixes are equal and the gates g(p, j), g(q, j)
  decide: ord_s(p, q) = γ_l(j). ∎
- Does NOT claim: anything outside 𝓛^R_d (in R109's 𝓛_d two movers of a level may W-point to different lower movers, and (a) fails
  in general); anything about which options are AVAILABLE (A-sets are Ξ-side and are not used by (a), (c)).

## 3. Lemma KP-MOVE and Lemma F0 (PROVED)
- Lemma KP-MOVE. Hypotheses: G IDEAL-ACYC (any degree elsewhere); x a mover with deg(x) = 2; any run.
  - (a) If x ∈ Mv_t, then s_t(x) = KP_(s_t)(x).
  - (b) moves(x) ≤ 1 + KF_x.
  - Proof. (a) As in ALIGN (b): by (F2) both options of x lie in A_(s_(t−1))(x) and the step takes the one with the least key_(s_t)(x,
    ·). (b) Let t_1 < … < t_M be the steps moving x. By (F2), consecutive moves go to different options: s_(t_i)(x) ≠ s_(t_(i+1))(x).
    By (a), KP_(s_(t_i))(x) ≠ KP_(s_(t_(i+1)))(x), so KP(x) changes at some step of [t_i + 1, t_(i+1)]. These intervals are pairwise
    disjoint, so KF_x ≥ M − 1. ∎
  - Does NOT claim: anything at deg(x) ≥ 3. (This is the argument of R105 KEYFLIP for one mover of degree 2; it is re-proved here so
    that no unlanded or non-quoted premise is needed.)
- Lemma F0. Hypotheses: G ∈ 𝓛^R_d (d ≥ 1); any run. Then moves(0) ≤ 1, moves(1) ≤ 1, and F(0) ≤ 2.
  - Proof. For y ∈ {0, 1}, key_s(y, k) = (g(y, k)) for every s, so KP_s(y) is the same option for every s and KF_y = 0; KP-MOVE (b)
    gives moves(y) ≤ 1. key_s(y, s(y)) = (g(y, s(y))) changes only at a step moving y, so a flip of (0, 1) happens only at a step moving
    0 or 1: F(0) ≤ #{steps moving 0 or 1} ≤ moves(0) + moves(1) ≤ 2. ∎
  - Does NOT claim: that F(0) = 2 is reached by every genome.

## 4. Theorem PAIR-DOUBLE (PROVED)
- Hypotheses: G ∈ 𝓛^R_d; 1 ≤ l ≤ d − 1; any run. Then F(l) ≤ 2 F(l − 1) + 2.
- Proof. Write p = 2l, q = 2l + 1, c_t := c_l(s_t), b_t := b_l(s_t). For x ∈ {p, q} put a_x(t) := [s_t(x) = c_t] (x is ALIGNED at s_t)
  and Φ(t) := #{x ∈ {p, q} : a_x(t) = 0} ∈ {0, 1, 2}.
  - By definition of F, b_t ≠ b_(t−1) holds at exactly F(l − 1) steps t (call them b-steps); at every other step c_t = c_(t−1).
  - At a step t, for x ∈ {p, q}: if x ∉ Mv_t, then s_t(x) = s_(t−1)(x), so a_x(t) = a_x(t − 1) if t is not a b-step and a_x(t) = 1 −
    a_x(t − 1) if it is (c changes, s(x) does not); if x ∈ Mv_t, then a_x(t) = 1 by ALIGN (b), and x was not aligned w.r.t. c_t before
    the step: s_(t−1)(x) ≠ s_t(x) = c_t.
  - Define, for a step t, Φ′(t) := #{x ∈ {p, q} : s_(t−1)(x) ≠ c_t} (misaligned w.r.t. the NEW c). Then Φ′(t) = Φ(t − 1) if t is not a
    b-step, Φ′(t) = 2 − Φ(t − 1) if it is, and Φ(t) = Φ′(t) − #(Mv_t ∩ {p, q}) (each mover of the pair that moves was among the Φ′(t)
    misaligned ones and becomes aligned; the others keep their alignment w.r.t. c_t).
  - By ALIGN (c), ord_(s_t)(p, q) is a function of (a_p(t), a_q(t), c_t): it equals a_p(t) when a_p(t) ≠ a_q(t) («D-states» 10 and 01),
    γ_l(c_t) when a_p(t) = a_q(t) = 1 (both on option c_t), and γ_l(1 − c_t) when a_p(t) = a_q(t) = 0 (both on option 1 − c_t).
  - Claim: if (p, q) flips at step t and Mv_t ∩ {p, q} = ∅, then t is a b-step and Φ(t − 1) = 1. Indeed, if t is not a b-step, nothing
    in (a_p, a_q, c) changes, so ord does not change. If t is a b-step, the alignments both toggle and c toggles: a D-state 10 becomes
    01 (ord changes from 1 to 0) and vice versa, while 11 under c becomes 00 under 1 − c, whose ord is γ_l(1 − (1 − c)) = γ_l(c), the
    same as before; likewise 00 under c (ord γ_l(1 − c)) becomes 11 under 1 − c (ord γ_l(1 − c)). So ord changes only from a D-state,
    where Φ(t − 1) = 1.
  - Hence F(l) ≤ M + B₁, with M := #{t : Mv_t ∩ {p, q} ≠ ∅} and B₁ := #{b-steps t with Φ(t − 1) = 1}.
  - Summing Φ(t) − Φ(t − 1) over the run: Φ(T) − Φ(0) = Σ_(b-steps t) (2 − 2Φ(t − 1)) − Σ_t #(Mv_t ∩ {p, q}). Since Φ(T) ≥ 0 and
    #(Mv_t ∩ {p, q}) ≥ 1 at the M steps counted by M: M ≤ Φ(0) + Σ_(b-steps t) (2 − 2Φ(t − 1)).
  - So F(l) ≤ Φ(0) + Σ_(b-steps t) h(Φ(t − 1)) with h(0) = 2, h(1) = 0 + 1 = 1, h(2) = −2 (the +1 for Φ = 1 from B₁). Since h ≤ 2
    and Φ(0) ≤ 2: F(l) ≤ 2 + 2 F(l − 1). ∎
- Does NOT claim: a polynomial bound on F(l) (iterated, the bound is 2^(l+2) − 2); anything outside 𝓛^R_d; that the stronger bound
  F(l) ≤ F(l − 1) + 1 holds when γ_l(0) ≠ γ_l(1) (§7: machine-checked range only, NOT stated for signing); anything about the Ξ side
  (whether the movers' moves are available is not used: the bound holds for every run).

## 5. Corollary MOVES and Corollary T-BOUND (PROVED)
- Hypotheses: G ∈ 𝓛^R_d (d ≥ 1); any run.
- Corollary MOVES. For every mover x of level l ≥ 1: KF_x = F(l − 1) and moves(x) ≤ 1 + F(l − 1). For x of level 0: moves(x) ≤ 1.
  - Proof. By ALIGN (a), KP_s(x) = c_l(s), which changes between s_(t−1) and s_t iff b_l changes, i.e. iff (2l − 2, 2l − 1) flips at t.
    So KF_x = F(l − 1). KP-MOVE (b) gives moves(x) ≤ 1 + F(l − 1). Level 0: Lemma F0. ∎
- Corollary T-BOUND. F(l) ≤ 2^(l+2) − 2 for 0 ≤ l ≤ d − 1, and T ≤ 2d + 2 Σ_(l=0..d−2) F(l) ≤ 2^(d+2) − 2d − 4.
  - Proof. F(0) + 2 ≤ 4 (Lemma F0) and F(l) + 2 ≤ 2 (F(l − 1) + 2) (PAIR-DOUBLE) give F(l) + 2 ≤ 2^(l+2). Every step moves at least
    one mover, so T ≤ Σ_x moves(x) ≤ 2 + Σ_(l=1..d−1) 2 (1 + F(l − 1)) = 2d + 2 Σ_(l=0..d−2) F(l) ≤ 2d + 2 Σ_(l=0..d−2) (2^(l+2) − 2)
    = 2d + 2 (2^(d+1) − 4) − 4 (d − 1) = 2^(d+2) − 2d − 4. ∎
- Does NOT claim: that the bound on T is attained for d ≥ 2 (T^R(d) = 2, 4, 8, 13 for d = 1-4 by L-RED's exact data, against 2^(d+2) − 2d − 4 = 2, 8,
  22, 52; equal at d = 1 only); anything about R109's 𝓛_d or T*(d); a polynomial bound.

## 6. Lemma PATH-RISE (PROVED; premises R105 ENC, MONO)
- Hypotheses: G IDEAL-ACYC, any degree, any width; z any mover; any run. Then the number of steps at which cv(z) rises is at most
  P(z) − 1.
- Proof. Under any state s, the chain of (z, s(z)) is a maximal Ξ-path from z (it follows the current option of every mover it meets
  until the first Ξ-target X; it is finite and has no repeated mover since the Ξ-graph is acyclic), and Ξ_s(z, s(z)) is the set of β's
  of its options. Two distinct maximal Ξ-paths from z first differ at some mover y that both visit, with different options k ≠ k′ there;
  each path visits y only once (acyclic), so one set contains β(y, k) and not β(y, k′), the other the reverse: their β-sets differ. By
  ENC, distinct β-sets have distinct integers (one is ▷ the other, i.e. its integer is larger). So cv(z) takes at most P(z) distinct
  values along the run. By MONO, cv_(s_t)(z) ≥ cv_(s_(t−1))(z) at every step (read through ENC's integer order); a non-decreasing
  sequence with at most P(z) distinct values rises at most P(z) − 1 times. ∎
- Does NOT claim: that P(z) is polynomial (it is exponential in desc(z) on diamond-shaped Ξ-graphs); any bound on moves from PATH-RISE
  alone; anything about keys.

## 7. DATA, machine checks, excluded parts, TARGET diff (not to sign)
- Tool: experiments/new/box178/aligncheck.py (deterministic, seed 178; simulator box150/check.py's Gen). Output frozen in
  experiments/new/box178/aligncheck.out and checked by block «P-IDEAL-ALIGN» of experiments/new/check.sh, which also pins the sha1s
  of this packet, its line L-1, the tool, its output and the instance dd_d5_F14.
- Scope: the 184 in-tree genome files of 𝓛^R_d (R110 wiring) under experiments/new/box150 to box177, from their stored starts, and 300
  random 𝓛^R_d genomes (d 2-5; every start for d ≤ 3, the genome start otherwise): 5,662 runs, 5,602 steps. Each count covers ONLY
  the statement named:
  - ALIGN (a) and (c): 22,472 (state, level ≥ 1) pairs, 0 violations each; ALIGN (b): checked at every step of the same runs, 0.
  - Lemma F0 (F(0) ≤ 2): 5,662 runs, 0 violations.
  - PAIR-DOUBLE: 10,648 (run, level ≥ 1) pairs, 0 violations; equality F(l) = 2F(l − 1) + 2 on 44 of them.
  - Corollary MOVES (KF_x = F(l − 1) at level ≥ 1, and the moves bound at every level): 32,620 (run, mover) pairs, 0 violations each.
  - Corollary T-BOUND (both inequalities): 5,662 runs, 0 violations.
  - PATH-RISE: 32,620 (run, mover) pairs, 0 violations.
  - Lemma KP-MOVE (b) at degree 2 outside 𝓛^R_d: no separate DATA here (on 𝓛^R_d it is checked through Corollary MOVES).
- Tightness instance: experiments/new/box172/inst/dd_d5_F14.json (sha1 06f0e501…; L-RED's claude/l-red experiments/red/r197/lag/
  dd_d5_F14.json, byte copy), in 𝓛^R_5, T 14, F(0..4) = 2, 3, 6, 14, 7: F(3) = 14 = 2F(2) + 2 (aligncheck.py line «TIGHT …»).
- EXCLUDED (not to sign):
  - The bound F(l) ≤ F(l − 1) + 1 when γ_l(0) ≠ γ_l(1): machine-checked only, by exhaustive DP over the 8-state automaton (a_p, a_q, b)
    for F(l − 1) ≤ 30 (experiments/new/box177/automaton.py: 2(k + 1) when γ_l(0) = γ_l(1), k + 1 otherwise); no hand proof; left out.
  - CONJECTURE DBL-O(1) and the doubling-persistence DATA (box 177: never 3 consecutive doubling levels in 190 runs); CONJECTURE PAIR-LIN;
    the slack table of box 177; every READING of docs/new/N5-PAIRDOUBLE-box177.md.
- Diff against TARGET.md: no statement mentions a parity game, a winning region, an algorithm's running time or a complexity class. Each
  is about the step sequence of the IDEAL model of RESULTS R104's definition. None is an M4 or M3 claim, none bounds anything
  polynomially (T-BOUND is exponential), none is a gauntlet step. G-N5-TIME stays OPEN.
- READING (value): on 𝓛^R the key side of every level is an exact 3-bit automaton; it allows doubling per level and no more (T^R(d) =
  O(2^d), improving R108's 3^d − 1 there), and equality needs every flip below to be taken with both movers aligned and then moved by both,
  which the Ξ side must permit (PATH-RISE bounds that permission only exponentially).
