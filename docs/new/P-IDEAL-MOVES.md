# Packet P-IDEAL-MOVES (box 187): every step but the last moves a Ξ-target mover, so a per-mover move bound on the Ξ-targets of 2-wide ladders is polynomial iff the run length is (REDUCE-XI); a degree-2 mover moves exactly when its Ξ-preference and its key preference agree against its position (AND-GATE); a metronome segment forces a flip of the pair below at every inner step and is bounded through the flips two levels down (SEG-WINDOW, WINDOW-DOUBLE); two conjectured bounds are false
L-NEW successor 57 (Opus 5.5), D14 / D18 / D20; Lead brief BOX 187 (2026-11-06 21:07Z): «freeze packet P-IDEAL-MOVES with your
lane-proved lemmas: REDUCE-XI, AND-GATE, SEG-WINDOW (a)-(e); DEAD items, each with an instance and checks: the segment lemma «D ≤ 2·LM +
O(1)» (pass_d4_D4, pass_d3_D3) and «moves ≤ 2(l + 1)» (L-RED m4_z4_r7)». Written 2026-11-06 from 21:08Z (date -u: see the commit).
FROZEN at push: later text goes into docs/new/P-IDEAL-MOVES-fixes.md (append-only). Sources: docs/new/N5-MOVES-box185.md §1, §2 and
docs/new/N5-METRONOME-box186.md §0, §1 (both successor 57). This packet carries every proof in full and is checked against this text
only; no other file carries a proof of a statement below. Labels: PROVED (L-NEW 57, unrefereed) / DEAD (instance, machine-checked) /
DATA / READING (not to sign). Not a TARGET.md claim. Every statement is about the IDEAL model of RESULTS R104 only. No statement bounds T
polynomially. CONJECTURE MOVES-2D and G-N5-TIME stay OPEN.

## To sign, and what is not to sign
| § | statement | label | hypotheses |
| --- | --- | --- | --- |
| §1 | Lemma REDUCE-XI; Corollary MOVES-EQUIV | PROVED | REDUCE-XI: IDEAL-ACYC, any degree, any width; MOVES-EQUIV: 𝓛^R_d |
| §2 | Lemma AND-GATE (a), (b), (c) | PROVED | IDEAL-ACYC, a mover of degree 2 |
| §3 | Lemma WINDOW-DOUBLE (a), (b) | PROVED | 𝓛^R_d, a level j ≥ 1, any window |
| §4 | Lemma SEG-WINDOW (a)-(e) | PROVED | 𝓛^R_d, a mover of level l ≥ 1, a metronome segment |
| §5 | DEAD-SEG; DEAD-LEV | DEAD (instances) | 𝓛^R_3, 𝓛^R_4, 𝓛^R_5 |
| §6 | DATA, machine checks, excluded parts, TARGET diff | DATA / READING (not to sign) | |

- Premises (LANDED only), quoted verbatim from the RESULTS statements on trunk b876c884.
  - RESULTS R104 (P-N5-REALIZE): ONLY its definition of the IDEAL model and of the Ξ-graph, restated in §0. No theorem of R104 is used.
  - RESULTS R105 (P-IDEAL-RED), five items, from its statement «at any degree»: «(ENC) the Ξ-order of β-sets is the order of the
    integers Σ ±2^rank (+ for even parity), so, with ε(x, k) := ±2^rank(x, k) (+ for even parity), the value of option (x, k) is ε(x, k)
    plus the current value of its Ξ-target (ε(x, k) alone if the Ξ-target is the exit X)»; «(LOCAL) an option's value depends only on the
    states on its chain, a key only on the states below its level»; «(MONO) the current Ξ-value of every mover never decreases along a
    run»; «(XI-NEW) for t ≥ 2 every least-level mover h of step t moves to an option w ∉ A_(s_(t−2))(h) (A_s(h): h's current option under
    s and its options strictly better under s)»; «(RISE) that option's value rose strictly at step t − 1, and some strict Ξ-descendant of h
    on its chain under s_(t−2) moved at step t − 1». ENC, MONO: §2 (c); LOCAL: §4 (e); XI-NEW, RISE: §1. RESULTS Erratum E-2 corrects
    R105's CHAINED binder (E2a), TOP-MONO's RANK_t (E2b) and KEYFLIP's moves(x) (E2c); none of these items is used here (moves(x) is
    defined in §0 with the E-2 (E2c) binder anyway).
  - RESULTS R110 (P-IDEAL-FLIP): ONLY its definition of 𝓛^R_d: «the 2-wide degree-2 ladders in L-RED's R197 convention (movers 2l and
    2l + 1 on level l, all of degree 2, no other movers, option k of a mover of level l ≥ 1 W-pointing to mover 2(l − 1) + k)», levels
    0, …, d − 1.
  - RESULTS R113 (P-IDEAL-ALIGN), two items: «(ALIGN) on 𝓛^R_d, for 1 ≤ l ≤ d − 1 and every state s of a run, both movers 2l and 2l + 1
    have KP_s = c_l(s), each of them that moves at step t moves to option c_l(s_t), and the order of their keys under s is [s(2l) =
    c_l(s)] if s(2l) ≠ s(2l + 1) and γ_l(j) if both are on option j»; «(F0) on 𝓛^R_d each level-0 mover moves at most once and F(0) ≤ 2»,
    with R113's notation «KP_s(x) the option of x with the least key under s», «c_l(s) the option index k for which mover 2(l − 1) + k
    has the smaller current key under s», «γ_l(j) := [g(2l, j) < g(2l + 1, j)] with g(x, k) the gate index of option (x, k)» and «F(l)
    the number of steps at which the pair (2l, 2l + 1) flips». ALIGN: §3, §4; F0: §1, §3, §4.
  - Not used: every other R105 item; R106-R112; R111 (CASCADE is not needed: §3 (a) re-proves the pass-through fact from ALIGN); R113's
    KP-MOVE, PAIR-DOUBLE, MOVES, T-BOUND, PATH-RISE (§2 re-proves what is needed of KP-MOVE; §3 re-proves PAIR-DOUBLE's argument on a
    window); the signed but not landed packet P-IDEAL-RISE (R114 draft: its MOVE-RISE is not used); docs/lit, docs/sources, any other
    lane file. No machine premise is used by any signed item; the DEAD items rest on machine computations (§5).
- Each statement lists its hypotheses and a paragraph «does NOT claim».

## 0. The model (RESULTS R104's definition, as restated in P-IDEAL-ALIGN §0) and the notation of this packet
- A genome G has N ≥ 1 movers x, each with a level lev(x) ∈ {0, 1, …} and deg(x) ≥ 1 options (x, k). Each option has a W-target wt(x,
  k) (a mover of level lev(x) − 1; none at level 0), a Ξ-target xt(x, k) (a mover or the exit X), a β with a rank (distinct over all
  options) and a parity, and a gate index g(x, k) (distinct over all options). There is a start s_0. A state s picks one option s(x) per
  mover.
- Ξ-graph: an edge x → xt(x, k) for every option whose Ξ-target is a mover. IDEAL-ACYC: it is acyclic. A strict Ξ-descendant of h is a
  mover reached from h by a path of ≥ 1 Ξ-graph edges.
- Under s, the chain of (x, k) is (x, k), (y_1, s(y_1)), (y_2, s(y_2)), … with y_1 = xt(x, k), y_(j+1) = xt(y_j, s(y_j)), up to the
  first option whose Ξ-target is X. Its Ξ-value Ξ_s(x, k) is the set of β's on it; two sets P ≠ Q are compared by the β of largest rank
  in P △ Q: the set containing it is better (P ▷ Q) if that β's parity is even, worse if odd.
- A_s(x) := {s(x)} ∪ {k : Ξ_s(x, k) ▷ Ξ_s(x, s(x))}. key_s(x, k) := (g(x, k)) if lev(x) = 0, else key_s(wt(x, k), s(wt(x, k))) followed
  by g(x, k); compared lexicographically.
- Step. If every A_(s_(t−1))(x) is a singleton, the run stops. Otherwise s_t is defined level by level, lowest level first: s_t(x) :=
  the option in A_(s_(t−1))(x) with the least key_(s_t)(x, ·) (keys under the NEW state). If s_t = s_(t−1), the run stops without that
  step. T := the number of steps. Mv_t := {x : s_t(x) ≠ s_(t−1)(x)} for t ∈ [1, T] (nonempty for every such t).
- Notation.
  - moves(x) := #{t ∈ [1, T] : x ∈ Mv_t} (the binder of Erratum E-2 (E2c)). Z := {xt(x, k) : (x, k) an option, xt(x, k) ≠ X} (the
    Ξ-target movers).
  - KP_s(x) as in R113; KF_x := #{t ∈ [1, T] : KP_(s_t)(x) ≠ KP_(s_(t−1))(x)}.
  - v_s(x, k) := the integer of Ξ_s(x, k) (R105 ENC: Σ ±2^rank over its β's). For deg(x) = 2, π_s(x) := the option k of x with the larger
    v_s(x, k) (well defined: the chains of (x, 0) and (x, 1) contain β(x, 0) and β(x, 1) respectively and, by acyclicity, not the other
    one, so the two β-sets differ and are strictly ordered). PF_x := #{t ∈ [1, T] : π_(s_t)(x) ≠ π_(s_(t−1))(x)}.
  - A flip of two distinct movers u, w of one level at step t: a change between s_(t−1) and s_t of the order of key_s(u, s(u)) and
    key_s(w, s(w)) (R113's flip). On 𝓛^R_d, for a set W of steps and a level j, F_W(j) := #{t ∈ W : the pair (2j, 2j + 1) flips at t};
    F(j) := F_[1,T](j).
  - On 𝓛^R_d, for a level j ≥ 1 and a state s: Φ_j(s) := #{x ∈ {2j, 2j + 1} : s(x) ≠ c_j(s)} ∈ {0, 1, 2}. A step t is a j-b-step if the
    pair (2j − 2, 2j − 1) flips at t.
  - A METRONOME SEGMENT of a mover x is a set [a, b] ⊆ [1, T] of consecutive steps with x ∈ Mv_t for every t ∈ [a, b]; D := b − a + 1.
    For x of level l ≥ 1: u := 2l − 2, w := 2l − 1; LM := Σ_(t ∈ [a, b]) #(Mv_t ∩ {u, w}); LS := #{t ∈ [a + 1, b] : Mv_t ∩ {u, w} ≠ ∅};
    PT := #{t ∈ [a + 1, b] : (u, w) flips at t and Mv_t ∩ {u, w} = ∅}.
  - T^R(d) := the largest T over all genomes of 𝓛^R_d with acyclic Ξ-graph and all starts (R110's T^R(d)). CONJECTURE MOVES-2D (lane,
    box 181, OPEN): on 𝓛^R_d every z ∈ Z moves at most 2d times in every run.

## 1. Lemma REDUCE-XI and Corollary MOVES-EQUIV (PROVED; premises R105 XI-NEW, RISE; R113 F0)
- Lemma REDUCE-XI. Hypotheses: G IDEAL-ACYC, any degree, any number of movers per level; any run. Then Mv_(t−1) ∩ Z ≠ ∅ for every t
  with 2 ≤ t ≤ T. Hence T ≤ 1 + #{t ∈ [1, T − 1] : Mv_t ∩ Z ≠ ∅} ≤ 1 + Σ_(z ∈ Z) moves(z).
  - Proof. Let 2 ≤ t ≤ T. Mv_t ≠ ∅, so a least-level mover h of step t exists. By R105 XI-NEW and RISE (stated «at any degree»), «some
    strict Ξ-descendant of h on its chain under s_(t−2) moved at step t − 1». A strict Ξ-descendant y of h is reached by a Ξ-graph path
    of ≥ 1 edges; its last edge is x′ → xt(x′, k′) = y for some option (x′, k′), so y ∈ Z, and y ∈ Mv_(t−1). The map t ↦ t − 1 is
    injective from [2, T] into [1, T − 1], so T − 1 ≤ #{t ∈ [1, T − 1] : Mv_t ∩ Z ≠ ∅}; each such t moves some z ∈ Z and is counted in
    moves(z). If T ≤ 1 the bound is trivial. ∎
  - Does NOT claim: that the moving Ξ-target is a least-level mover; any bound on moves; anything about Ξ-cyclic genomes.
- Corollary MOVES-EQUIV. Hypotheses: 𝓛^R_d (2d movers, levels 0, …, d − 1), acyclic Ξ-graph. Let μ(d) := the largest moves(z) over
  all such genomes, all starts and all z ∈ Z of level ≥ 1 (μ(1) := 0). Then μ(d) ≤ T^R(d) ≤ 3 + (2d − 2)·μ(d). In particular MOVES-2D
  implies T^R(d) ≤ 4d² − 4d + 3, and μ is bounded by a polynomial in d iff T^R is.
  - Proof. moves(z) ≤ T ≤ T^R(d) for every z. By REDUCE-XI and F0 (each level-0 mover moves at most once): T ≤ 1 + moves(0) + moves(1)
    + Σ_(z ∈ Z, lev(z) ≥ 1) moves(z) ≤ 3 + (2d − 2)·μ(d), with 2d − 2 movers of level ≥ 1. Under MOVES-2D, μ(d) ≤ 2d. ∎
  - Does NOT claim: MOVES-2D; that movers outside Z are bounded (they need not be, and REDUCE-XI does not need them).

## 2. Lemma AND-GATE (PROVED; R104 definition; (c) uses R105 ENC, MONO)
- Hypotheses: G IDEAL-ACYC (any degree elsewhere); x a mover with deg(x) = 2; any run.
- (a) For t ∈ [1, T]: x ∈ Mv_t iff s_(t−1)(x) ≠ π_(s_(t−1))(x) and π_(s_(t−1))(x) = KP_(s_t)(x). If x ∈ Mv_t then s_t(x) = π_(s_(t−1))(x) =
  KP_(s_t)(x).
- (b) If x moves at steps t < t′ and at no step strictly between, then π(x) changes at some step of [t, t′ − 1] (i.e. π_(s_r)(x) ≠
  π_(s_(r−1))(x) for some r ∈ [t, t′ − 1]) and KP(x) changes at some step of [t + 1, t′]. Hence moves(x) ≤ 1 + min(KF_x, PF_x).
- (c) If π_(s_t)(x) = b ≠ π_(s_(t−1))(x), then v_(s_t)(x, b) > v_(s_(t−1))(x, b).
- Proof. (a) Deg 2: A_(s_(t−1))(x) = {s_(t−1)(x)} if π_(s_(t−1))(x) = s_(t−1)(x), and both options otherwise (the other option is in A iff
  its Ξ-value is strictly better, i.e. iff it is π). The step gives x the option of A with the least key_(s_t)(x, ·) (§0). So x moves
  iff |A| = 2 and the key-least of the two options under s_t, KP_(s_t)(x), is the other option, which is π_(s_(t−1))(x); then s_t(x) is
  that option. (b) By (a), s_t(x) = π_(s_(t−1))(x) = KP_(s_t)(x), s_(t′)(x) = π_(s_(t′−1))(x) = KP_(s_(t′))(x), and s_(t′)(x) ≠ s_t(x)
  because x keeps s_t(x) on [t, t′ − 1] and moves at t′ (deg 2). So π(x) differs at s_(t−1) and s_(t′−1), and KP(x) at s_t and s_(t′).
  Over the moves t_1 < … < t_M of x the windows [t_i, t_(i+1) − 1] are pairwise disjoint, and so are [t_i + 1, t_(i+1)]; so PF_x ≥ M − 1
  and KF_x ≥ M − 1. (c) Let a := π_(s_(t−1))(x). By ENC the values are the integers v, and by ENC + MONO v(x, a) = ε(x, a) + (the current
  value of xt(x, a), or 0 if it is X) is non-decreasing along the run. So v_(s_t)(x, b) > v_(s_t)(x, a) ≥ v_(s_(t−1))(x, a) >
  v_(s_(t−1))(x, b). ∎
- Does NOT claim: a bound on PF_x or KF_x; anything at deg(x) ≥ 3.

## 3. Lemma WINDOW-DOUBLE (PROVED; R104 definition, R113 ALIGN, F0)
- Hypotheses: G ∈ 𝓛^R_d; 1 ≤ j ≤ d − 1; p := 2j, q := 2j + 1; any run; 0 ≤ a < b ≤ T; W := [a + 1, b].
- (a) If (p, q) flips at a step t with Mv_t ∩ {p, q} = ∅, then t is a j-b-step, s_(t−1)(p) ≠ s_(t−1)(q) and Φ_j(s_(t−1)) = 1.
- (b) F_W(j) ≤ 2 + 2·F_W(j − 1). In particular (BURST-2) if F_W(j − 1) = 0 then F_W(j) ≤ 2.
- Proof. Write c_t := c_j(s_t), Φ(t) := Φ_j(s_t).
  - (a) By ALIGN the order of the keys of p, q under s is [s(p) = c_j(s)] if s(p) ≠ s(q) and γ_j(i) if both are on option i. If neither
    moves at t, then s_t(p) = s_(t−1)(p), s_t(q) = s_(t−1)(q). If both are on one option i, the order is γ_j(i) before and after: no flip.
    So s_(t−1)(p) ≠ s_(t−1)(q); then exactly one of them is on c_(t−1), so Φ(t − 1) = 1. If t were not a j-b-step, then c_t = c_(t−1)
    (c_j(s) is a function of the order of the pair (2j − 2, 2j − 1) under s, which changes exactly at its flips), and the order [s(p) =
    c] would not change: no flip. So t is a j-b-step.
  - (b) Put Φ′(t) := #{x ∈ {p, q} : s_(t−1)(x) ≠ c_t}. If t is not a j-b-step, c_t = c_(t−1) and Φ′(t) = Φ(t − 1); if it is, c_t = 1 −
    c_(t−1) and Φ′(t) = 2 − Φ(t − 1) (options in {0, 1}). By ALIGN, a mover of {p, q} that moves at t moves to c_t, so it had s_(t−1)(x) ≠
    c_t and is counted in Φ′(t); a mover that does not move keeps its option. So Φ(t) = Φ′(t) − #(Mv_t ∩ {p, q}).
  - By (a), every flip of (p, q) at a step t ∈ W is at a step with Mv_t ∩ {p, q} ≠ ∅ or at a j-b-step with Φ(t − 1) = 1. So F_W(j) ≤ M_W +
    B1_W with M_W := #{t ∈ W : Mv_t ∩ {p, q} ≠ ∅} and B1_W := #{j-b-steps t ∈ W with Φ(t − 1) = 1}.
  - Summing Φ(t) − Φ(t − 1) over t ∈ W: Φ(b) − Φ(a) = Σ_(j-b-steps t ∈ W) (2 − 2Φ(t − 1)) − Σ_(t ∈ W) #(Mv_t ∩ {p, q}). As Φ(b) ≥ 0, Φ(a)
    ≤ 2 and #(Mv_t ∩ {p, q}) ≥ 1 at the M_W steps: M_W ≤ 2 + Σ_(j-b-steps t ∈ W) (2 − 2Φ(t − 1)).
  - So F_W(j) ≤ 2 + Σ_(j-b-steps t ∈ W) h(Φ(t − 1)) with h(0) = 2, h(1) = 0 + 1 = 1, h(2) = −2; h ≤ 2, and the j-b-steps in W are F_W(j − 1)
    many. ∎
- Does NOT claim: anything beyond R113 PAIR-DOUBLE on the whole run (W = [1, T] is PAIR-DOUBLE itself); a polynomial bound.

## 4. Lemma SEG-WINDOW (PROVED; R104 definition, R105 LOCAL, R113 ALIGN, F0; §2, §3)
- Hypotheses: G ∈ 𝓛^R_d; x a mover of level l ≥ 1 (so d ≥ 2); any run; [a, b] a metronome segment of x; D, u, w, LM, LS, PT as in §0.
- (a) The pair (u, w) flips at every step of [a + 1, b]; so D − 1 ≤ F_[a+1,b](l − 1).
- (b) D ≤ 1 + LS + PT, and every step of [a + 1, b] moves some mover of level < l.
- (c) If l ≥ 2: D ≤ 3 + 2·F_[a+1,b](l − 2). If l = 1: D ≤ 3.
- (d) (BURST-2 for the pair below) If l ≥ 2, every window W ⊆ [a + 1, b] of consecutive steps with F_W(l − 2) = 0 has |W| ≤ 2; so every 3
  consecutive steps of [a + 1, b] contain a flip of the pair l − 2.
- (e) For every t ∈ [a, b − 1], π(x) changes at step t and the value of x's option s_(t+1)(x) rises strictly at t; some mover of the
  chain of (x, s_(t+1)(x)) under s_(t−1), other than x, moves at t.
- Proof.
  - (a) For t ∈ [a + 1, b], x moves at t − 1 and at t; by AND-GATE (b) applied to these consecutive moves, KP(x) changes at a step of
    [t, t], i.e. at t. By ALIGN, KP_s(x) = c_l(s), and c_l(s) changes between s_(t−1) and s_t exactly when (u, w) flips at t (§3 proof of
    (a)). Each of the D − 1 steps is counted in F_[a+1,b](l − 1).
  - (b) Each t ∈ [a + 1, b] is a flip step of (u, w) by (a), so it is counted in LS or in PT: D − 1 ≤ LS + PT. If Mv_t ∩ {u, w} ≠ ∅, t moves
    a mover of level l − 1. Otherwise (u, w) flips with no move of u, w: if l − 1 = 0 this is impossible (the keys of 0 and 1 are their
    gates (g(y, s(y))), which change only when y moves); if l − 1 ≥ 1, by §3 (a) the pair l − 2 flips at t. Repeat with that pair: the
    descent stops at a level whose pair has a mover moving at t (at level 0 at the latest), a level < l.
  - (c) l ≥ 2: by (a) and §3 (b) with j = l − 1, W = [a + 1, b]: D − 1 ≤ F_W(l − 1) ≤ 2 + 2·F_W(l − 2). l = 1: D − 1 ≤ F(0) ≤ 2 (F0).
  - (d) By (a), the pair l − 1 flips at every step of W; by §3 (b) (BURST-2, j = l − 1, applied to the window W) it flips at most twice
    on W; so |W| ≤ 2.
  - (e) x moves at t and t + 1; by AND-GATE (b) π(x) changes at a step of [t, t], i.e. at t, to b := π_(s_t)(x) = s_(t+1)(x) (AND-GATE (a)),
    and by AND-GATE (c) v(x, b) rises strictly at t. By R105 LOCAL «an option's value depends only on the states on its chain»: the chain
    of (x, b) under s_(t−1) is (x, b), (y_1, s_(t−1)(y_1)), …; if no y_i moved at t, the chain and its β-set would be the same under s_t,
    and v(x, b) would not change. So some y_i ≠ x (acyclic) moves at t. ∎
- Does NOT claim: that the movers of (b) or (e) are u or w; a bound on D polynomial in l (iterated, (c) gives 2^l-type bounds only).

## 5. DEAD items (instances; machine-checked by experiments/new/box187/movescheck.py)
- DEAD-SEG: «for a metronome segment of a mover of level l ≥ 1, D ≤ 2·LM + c» is FALSE for every c ≤ 4. Instances (all 𝓛^R_d, Ξ-acyclic;
  the mover is a Ξ-target in each):
  - experiments/new/box186/out/pass_d3_D3.json (sha1 8bca976438ca184bb8b8e4d5ecf3455f51809ff4), start 110100: mover 5 (level 2) moves at
    steps 1, 2, 3 (D 3), LM 0: false for c ≤ 2.
  - experiments/new/box186/out/pass_d4_D4.json (sha1 3bf6a4a48bc2df9fb8809306f8347ee280965b07), start 01010111: mover 7 (level 3) moves
    at steps 1-4 (D 4), LM 0: false for c ≤ 3.
  - experiments/new/box186/out/pass_d5_D5.json (sha1 16be2e594732ad0b21e2c84aa4cdbc62d143e7c4), start 0101010110: mover 9 (level 4) moves
    at steps 1-5 (D 5), LM 0: false for c ≤ 4.
  - Checks: movescheck.py lines «DEAD-SEG …» (box150 Gen; the stored start of the .json is not used, the start is given explicitly;
    each line also prints whether the mover is a Ξ-target).
  - Does NOT claim: that D − 2·LM is unbounded in d (DATA only: 3, 4, 5 at d = 3, 4, 5); anything about c ≥ 5.
- DEAD-LEV: «on 𝓛^R_d every mover of level l moves at most 2(l + 1) times» is FALSE (even for Ξ-target movers). Instance:
  experiments/new/box187/inst/m4_z4_r7.json (sha1 7c158e2f806df2d1984418902548cfc2cb243d75; a byte copy of L-RED's claude/l-red
  experiments/red/r213/out/m4_z4_r7.json, l-red commit 4b61200d, same sha1), stored start 10111010, 𝓛^R_4: mover 4 (level 2, a Ξ-target)
  moves 7 > 6 = 2(2 + 1) times in a run of T 8. Check: movescheck.py line «DEAD-LEV …».
  - Does NOT claim: anything about MOVES-2D (7 ≤ 2d = 8).

## 6. DATA, machine checks, excluded parts, TARGET diff (not to sign)
- Tool: experiments/new/box187/movescheck.py (numpy-free, deterministic; simulator box150/check.py Gen). Output frozen in
  experiments/new/box187/movescheck.out, checked by block «P-IDEAL-MOVES» of experiments/new/check.sh, which pins the sha1s of this
  packet, its line L-1, the tool, its output and the four instance files.
- Scope (FROZEN corpus): every 𝓛^R_d genome JSON under experiments/new/box150 to box187 (208 files, d 1-8), every start for d ≤ 5, the
  stored start for d ≥ 6: 63,223 runs, 140,395 steps. Each count covers ONLY the statement named:
  - REDUCE-XI (both inequalities and the per-step form): 63,223 runs, 0 violations (counter RX); equality T = 1 + #{t ≤ T − 1 : Mv_t ∩ Z
    ≠ ∅} on 59,502 runs.
  - AND-GATE (a): every (run, step, mover) triple, 0 (AGA); (b): every pair of consecutive moves of every mover, 0 (AGB); (c): every
    π-change, 0 (AGC).
  - WINDOW-DOUBLE (b): every window [a + 1, b] of every run and every level j ≥ 1, 1,288,162 (window, level) pairs, 0 (WPD); BURST-2:
    every maximal window without flips of the pair j − 1, 0 (SWD). WINDOW-DOUBLE (a): no separate DATA.
  - SEG-WINDOW (a), (b), (c), (e): every metronome segment (every [a, b] of consecutive steps all moving one mover of level ≥ 1),
    225,917 segments, 0 each (SWA, SWB, SWC, SWE; max D 9). SEG-WINDOW (d): no separate DATA (it is (a) with BURST-2).
  - Corollary MOVES-EQUIV: no separate DATA (it is REDUCE-XI with F0).
- Lane DATA (not to sign; from L-RED, not landed, «one solver, no proof file»): exact maxima of moves of a Ξ-target by level (L-RED R213,
  CaDiCaL via pysat): d 3: 1, 3, 4; d 4: 1, ≤ 8 (≤ 3 by R113 MOVES), 7, 7 or 8. d 5: a Ξ-target of level 4 moves 9 times
  (experiments/new/box186/out/dense_d5_D9.json, L-NEW climb, in the corpus above); L-RED's DENSE(5, 3, 10) SAT (10 = 2d) as relayed by the Lead at 21:07Z
  (not opened by me; not used).
- EXCLUDED (not to sign): CONJECTURE MOVES-2D; the halving-tower and LEVEL-PRODUCT readings of box 186; every READING of
  docs/new/N5-MOVES-box185.md and docs/new/N5-METRONOME-box186.md.
- Diff against TARGET.md: no statement mentions a parity game, a winning region, an algorithm's running time or a complexity class.
  Each is about the step sequence of the IDEAL model of RESULTS R104's definition. None is an M4 or M3 claim, none bounds anything
  polynomially, none is a gauntlet step. MOVES-EQUIV is an equivalence of two open bounds, not a bound. G-N5-TIME stays OPEN.
