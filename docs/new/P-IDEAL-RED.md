# Packet P-IDEAL-RED (box 150): reductions inside the IDEAL-ACYC model (MONO, XI-NEW, CHAIN-BACK, KEYFLIP, DECREMENT, TOP-MONO, RANK-BOUND, INTERVAL-RESTRICT, INTERVAL-CHARGE, RECURSION)
L-NEW successor 50 (Opus 5.5), D14 / D18; Lead brief BOX 150 (2026-11-03): «FREEZE packet P-IDEAL-RED for the two referees». Written
2026-11-03 (date -u: see the commit). FROZEN at push: later text goes into docs/new/P-IDEAL-RED-fixes.md (append-only).
Source: docs/new/N5-IDEAL-STATE.md §6 (synthesis, box 149) and the lane proofs of boxes 144, 147, 148, 149. This packet governs: every
proof below is written out in full here and is checked against this text only. Labels: PROVED (L-NEW 50, unrefereed) / DATA / READING.
Not a TARGET.md claim. Every statement is about the IDEAL-ACYC model only. No polynomial bound is claimed anywhere. G-N5-TIME stays OPEN.

## To sign, and what is not to sign
| § | statement | label | kind |
| --- | --- | --- | --- |
| §1 | Lemma ENC, Lemma LOCAL | PROVED | facts about the model |
| §2 | Lemma MONO | PROVED | monotonicity |
| §3 | Lemma XI-NEW, Corollary RISE | PROVED | structure of a step |
| §4 | Theorem CHAIN-BACK (steps ≤ N (1 + U)) and Corollary U-EQ | PROVED | REDUCTION / EQUIVALENCE of two counts |
| §5 | Lemma KEYFLIP (degree ≤ 2) and Corollary KF-EQ | PROVED | REDUCTION / EQUIVALENCE of two counts |
| §6 | Lemma DECREMENT, Corollary EXACT-ENERGY (any degree) | PROVED | exponential bound only |
| §7 | Corollary TOP-MONO, Corollary RANK-BOUND (degree ≤ 2) | PROVED | conditional count bound |
| §8 | Lemma INTERVAL-RESTRICT, Corollary INTERVAL-CHARGE, Corollary RECURSION (degree ≤ 2) | PROVED | recursive bounds |
| §9 | machine check, excluded parts, TARGET diff | DATA / READING (not to sign) | |

- Premises.
  - LANDED: RESULTS R104 (P-N5-REALIZE), ONLY its definition of the IDEAL model and of the Ξ-graph, restated in §0 below. No theorem
    of R104 (REALIZE, REAL-IDEAL) is used. No other RESULTS entry is used.
  - Not used: L-RED R178 (its Lemma XI-NEW is re-proved in full in §3; the lane text is not a premise), docs/lit, docs/sources, any
    other lane file. No outside source is cited.
- Each statement lists its hypotheses (model, degree, width) and a line «does NOT claim».

## 0. The model (RESULTS R104's definition, restated with notation)
- A genome G has N movers x (N ≥ 1), each with a level lev(x) ∈ {0, 1, …}, and deg(x) ≥ 1 options (x, k), k = 0, …, deg(x) − 1.
  M := Σ deg(x). Each option (x, k) has:
  - a W-target wt(x, k): a mover of level lev(x) − 1 (none if lev(x) = 0);
  - a Ξ-target xt(x, k): a mover or the exit X;
  - a β with a rank rk(x, k) ∈ ℕ and a parity par(x, k) ∈ {0, 1}; the ranks of distinct options are distinct;
  - a gate index g(x, k) ∈ ℕ; the gate indices of distinct options are distinct.
  - and a start s_0 (an option s_0(x) per mover).
- A state s picks one option s(x) of each mover.
- Ξ-graph: an edge x → xt(x, k) for every option whose Ξ-target is a mover. IDEAL-ACYC: the Ξ-graph is acyclic. Fix a topological
  order, written as positions π(x) ∈ {0, …, N − 1} (a bijection, π(x) < π(y) for every edge x → y). Every statement holds for every
  such π. A strict Ξ-descendant of x is a mover reachable from x by a nonempty Ξ-path.
- Chain and Ξ-value. Under s, the chain of (x, k) is (x, k), then (y_1, s(y_1)) with y_1 = xt(x, k), then (y_2, s(y_2)) with
  y_2 = xt(y_1, s(y_1)), …, up to the first option whose Ξ-target is X. (Acyclic: the movers x, y_1, y_2, … are distinct, so the chain
  is finite.) The Ξ-value Ξ_s(x, k) is the set of β's of the options on the chain. Two values P ≠ Q are compared by the β of largest
  rank in P △ Q: the value containing it is the better one if its parity is even (0), the worse one if odd (1). Write P ▷ Q for
  «P better than Q».
- Current value and availability. cur_s(x) := Ξ_s(x, s(x)). A_s(x) := {s(x)} ∪ {k : Ξ_s(x, k) ▷ cur_s(x)}.
  c_s(x) := |A_s(x)| − 1 (the number of options strictly better than the current one). x is UNSTABLE at s iff c_s(x) ≥ 1.
- Keys. For a state s, key_s(x, k) := (g(x, k)) if lev(x) = 0, and key_s(x, k) := key_s(y, s(y)) followed by g(x, k), with
  y = wt(x, k), if lev(x) ≥ 1. (The sequence of gate indices of the chain of W-targets under s, lowest level first.) It is a sequence
  of length lev(x) + 1, and it depends only on s at movers of level < lev(x). Keys of distinct options of x differ in the last entry
  at least, so they are distinct. Sequences are compared lexicographically.
- Step. From s_(t−1), if every A_(s_(t−1))(x) is a singleton, the run stops. Otherwise the new state s_t is defined level by level,
  lowest level first: s_t(x) := the option k ∈ A_(s_(t−1))(x) with the least key_(s_t)(x, k). (key_(s_t)(x, ·) reads s_t only at
  levels < lev(x), already defined, so this is well defined: «keys under the new state, root-first».) If s_t = s_(t−1), the run stops
  without that step. T := the number of steps (R104's L(G)). We consider runs with T < ∞ or the first T steps of any run; nothing
  below uses termination except where T appears as a number.
- So every step t ∈ {1, …, T} has a nonempty mover set Mv_t := {x : s_t(x) ≠ s_(t−1)(x)}, and every x ∈ Mv_t satisfies
  s_t(x) ∈ A_(s_(t−1))(x) \ {s_(t−1)(x)}, i.e. Ξ_(s_(t−1))(x, s_t(x)) ▷ cur_(s_(t−1))(x). Every mover outside Mv_t keeps its option.
- Notation for steps. h_t := a mover of least level in Mv_t (smallest index on a tie; any fixed tie rule works). y_t := the mover of
  largest π in Mv_t. moves(x) := |{t : x ∈ Mv_t}|. A mover with deg(x) = 1 never moves.
- Degree. «Degree ≤ 2» means deg(x) ≤ 2 for every mover. No width hypothesis is made anywhere: every level may hold any number of
  movers. The 2-wide ladder of N5-IDEAL-STATE §0 is a special case and is not used.

## 1. Lemma ENC and Lemma LOCAL (PROVED)
- Lemma ENC (any IDEAL genome, any degree). Put ε(x, k) := (−1)^par(x, k) · 2^rk(x, k) and, for a finite set P of β's,
  e(P) := Σ_(β ∈ P) ε(β). Then for P ≠ Q: P ▷ Q ⟺ e(P) > e(Q). Hence ▷ is a strict total order on finite sets of β's, compared as
  the integers e(·).
  - Proof. e(P) − e(Q) = Σ_(P \ Q) ε − Σ_(Q \ P) ε. Let β* be the element of largest rank r* in P △ Q. The other elements of P △ Q
    have distinct ranks < r*, so their total contribution has absolute value ≤ Σ_(r < r*) 2^r = 2^(r*) − 1 < 2^(r*). So the sign of
    e(P) − e(Q) is the sign of the β* term: positive iff (β* ∈ P and par even) or (β* ∈ Q and par odd), which is exactly «P ▷ Q» by
    the definition. ∎
  - Consequence used below: Ξ_s(x, k) is compared through v_s(x, k) := e(Ξ_s(x, k)) ∈ ℤ, and, since the options on a chain are
    distinct, v_s(x, k) = ε(x, k) if xt(x, k) = X, and v_s(x, k) = ε(x, k) + v_s(y, s(y)) with y = xt(x, k) otherwise. Write
    cv_s(x) := v_s(x, s(x)).
  - Does NOT claim: anything about the size of these integers in a real game (they are a proof device only).
- Lemma LOCAL (any IDEAL-ACYC genome, any degree).
  - (a) If two states s, s′ agree on every mover of the chain of (x, k) under s other than x, then the chains of (x, k) under s and s′
    are equal and Ξ_s(x, k) = Ξ_(s′)(x, k).
  - (b) If s, s′ agree on every strict Ξ-descendant of x, then Ξ_s(x, k) = Ξ_(s′)(x, k) for every k; if moreover s(x) = s′(x), then
    cur, A and c of x are the same under s and s′.
  - (c) key_s(x, k) = key_(s′)(x, k) whenever s and s′ agree on every mover of level < lev(x).
  - Proof. (a) Induction along the chain: its first option is (x, k) in both; if the j-th option is (y_j, s(y_j)) = (y_j, s′(y_j)),
    the next mover xt(y_j, s(y_j)) is the same, and its option is the same by hypothesis. The β-sets are then equal. (b) Every mover
    after x on any chain of an option of x is a strict Ξ-descendant of x; apply (a). (c) key_s(x, k) reads s only at levels < lev(x)
    (definition, by induction on the level). ∎
  - Does NOT claim: anything beyond the model.

## 2. Lemma MONO (PROVED)
- Statement (any IDEAL-ACYC genome, any degree, any width). For every step t and every mover x: cv_(s_t)(x) ≥ cv_(s_(t−1))(x), i.e.
  the current Ξ-value of every mover never gets worse along a run.
- Proof. Induction on x in decreasing π. Let k′ := s_t(x) ∈ A_(s_(t−1))(x), so v_(s_(t−1))(x, k′) ≥ cv_(s_(t−1))(x) (equality iff
  k′ = s_(t−1)(x)). If xt(x, k′) = X, then v_(s_t)(x, k′) = ε(x, k′) = v_(s_(t−1))(x, k′). Otherwise y := xt(x, k′) has π(y) > π(x),
  so by induction cv_(s_t)(y) ≥ cv_(s_(t−1))(y), and by ENC v_(s_t)(x, k′) = ε(x, k′) + cv_(s_t)(y) ≥ ε(x, k′) + cv_(s_(t−1))(y) =
  v_(s_(t−1))(x, k′). In both cases cv_(s_t)(x) = v_(s_t)(x, k′) ≥ v_(s_(t−1))(x, k′) ≥ cv_(s_(t−1))(x). ∎
- Does NOT claim: that any non-current option's value is monotone (it is not in general), or anything on Ξ-cyclic genomes.

## 3. Lemma XI-NEW and Corollary RISE (PROVED; re-proved here, the l-red R178 text is not a premise)
- Lemma XI-NEW (any IDEAL-ACYC genome, any degree, any width; in fact acyclicity is not used). Let 2 ≤ t ≤ T, let h be ANY mover of
  least level in Mv_t, and w := s_t(h). Then w ∉ A_(s_(t−2))(h).
- Proof.
  - (1) Every mover of level < lev(h) is outside Mv_t, so s_t and s_(t−1) agree on all levels < lev(h). By LOCAL (c),
    key_(s_t)(h, k) = key_(s_(t−1))(h, k) for every option k of h.
  - (2) Put o := s_(t−1)(h). Since h ∈ Mv_t, w ≠ o. By the step rule at step t − 1, o is the key_(s_(t−1))-least element of
    A_(s_(t−2))(h). Suppose w ∈ A_(s_(t−2))(h). Keys of distinct options are distinct, so key_(s_(t−1))(h, w) > key_(s_(t−1))(h, o).
  - (3) By (1), key_(s_t)(h, w) > key_(s_t)(h, o). But o = s_(t−1)(h) ∈ A_(s_(t−1))(h), and the step rule at step t chose w as the
    key_(s_t)-least element of A_(s_(t−1))(h), so key_(s_t)(h, w) < key_(s_t)(h, o). Contradiction. ∎
- Corollary RISE (IDEAL-ACYC, any degree, any width). With t, h, w as in XI-NEW:
  - (a) v_(s_(t−1))(h, w) > v_(s_(t−2))(h, w): the value of option (h, w) rose strictly at step t − 1;
  - (b) the set Z_t of movers z ≠ h on the chain of (h, w) under s_(t−2) with z ∈ Mv_(t−1) is nonempty;
  - (c) every z ∈ Z_t is a strict Ξ-descendant of h, so π(z) > π(h).
- Proof. w ∉ A_(s_(t−2))(h) gives w ≠ s_(t−2)(h) and v_(s_(t−2))(h, w) ≤ cv_(s_(t−2))(h). Since h moves to w at step t,
  w ∈ A_(s_(t−1))(h) \ {s_(t−1)(h)}, so v_(s_(t−1))(h, w) > cv_(s_(t−1))(h). By MONO cv_(s_(t−1))(h) ≥ cv_(s_(t−2))(h). Chaining:
  v_(s_(t−1))(h, w) > cv_(s_(t−1))(h) ≥ cv_(s_(t−2))(h) ≥ v_(s_(t−2))(h, w): (a). If Z_t were empty, s_(t−1) and s_(t−2) would agree
  on every mover of the chain of (h, w) under s_(t−2) other than h, and LOCAL (a) would give equal values, contradicting (a): (b).
  The movers after h on that chain are reached from h by Ξ-edges, and acyclicity excludes h itself: (c). ∎
- Does NOT claim: anything for real N5 runs (R178's real-game form of XI-NEW is EXCLUDED, §9), nor a bound on how often (b) happens.

## 4. Theorem CHAIN-BACK and Corollary U-EQ (PROVED)
- Definitions. For 2 ≤ t ≤ T, step t is CHAINED iff h_(t−1) lies on the chain of (h_t, s_t(h_t)) under s_(t−2) (as a mover other
  than h_t), and UNCHAINED otherwise. U := |{t ∈ [2, T] : t unchained}|.
- Theorem CHAIN-BACK (any IDEAL-ACYC genome, any degree, any width). (i) If step t is chained, then π(h_t) < π(h_(t−1)).
  (ii) T ≤ N (1 + U).
- Proof. (i) h_(t−1) ∈ Mv_(t−1) by definition, so a chained step has h_(t−1) ∈ Z_t (RISE (b), with h = h_t), and RISE (c) gives
  π(h_(t−1)) > π(h_t). (ii) Cut [1, T] into maximal blocks [a, b] of consecutive steps such that every t ∈ (a, b] is chained. Each
  block starts at a = 1 or at an unchained step, so there are ≤ 1 + U blocks. Inside a block π(h_a) > π(h_(a+1)) > … > π(h_b) by
  (i), so the h_t of a block are distinct movers and b − a + 1 ≤ N. Hence T ≤ N (1 + U). ∎
- Corollary U-EQ. U ≤ T − 1 and T ≤ N (1 + U). So for any family of IDEAL-ACYC runs: T is bounded by a polynomial in N + M iff U is.
- Does NOT claim: any bound on U (CONJECTURE U-LIN of N5-IDEAL-STATE §3 is NOT part of this packet), any bound on T, or anything on
  Ξ-cyclic genomes. It is a REDUCTION (T to U) and an EQUIVALENCE of the two growth classes, nothing more.

## 5. Lemma KEYFLIP and Corollary KF-EQ (PROVED)
- Definitions (degree ≤ 2). For a mover x with deg(x) = 2 and a state s, KP_s(x) := the option of x with the smaller key_s(x, ·)
  (keys under s, as in §0). KF_x := |{t ∈ [1, T] : KP_(s_t)(x) ≠ KP_(s_(t−1))(x)}| (KF_x := 0 if deg(x) = 1). KF := Σ_x KF_x.
- Lemma KEYFLIP (degree ≤ 2, any width; acyclicity not used). moves(x) ≤ 1 + KF_x for every mover x.
- Proof. Let t1 < t2 be consecutive moves of x (x ∈ Mv_(t1), x ∈ Mv_(t2), x ∉ Mv_t for t1 < t < t2). With two options, x moves from
  b to a at t1 and from a back to b at t2 (a ≠ b). At t1 both options lie in A_(s_(t1−1))(x) = {a, b}, and the step rule takes the
  one with the smaller key under s_(t1), so KP_(s_(t1))(x) = a. In the same way KP_(s_(t2))(x) = b. Hence KP flips at some
  t ∈ (t1, t2]. These windows (t1, t2] are disjoint for distinct consecutive pairs, so moves(x) − 1 ≤ KF_x when moves(x) ≥ 1. ∎
- Corollary KF-EQ (degree ≤ 2). T ≤ Σ_x moves(x) ≤ N + KF, and KF ≤ N · T (each KF_x ≤ T). So for any family: T is bounded by a
  polynomial in N + M iff KF is; with CHAIN-BACK, the same holds for U.
- Does NOT claim: any bound on KF; the ladder identity «KF_x = flips of level lev(x) − 1» (N5-IDEAL-STATE §5) is EXCLUDED (§9);
  nothing for degree ≥ 3 (there a mover may move twice without a key flip, to a key-smaller option that becomes available later).

## 6. Lemma DECREMENT and Corollary EXACT-ENERGY (PROVED)
- Lemma DECREMENT (any IDEAL-ACYC genome, any degree, any width). For every step t, with y := y_t:
  - (a) c_(s_(t−1))(y) ≥ 1; (b) c_(s_t)(y) < c_(s_(t−1))(y); (c) c_(s_t)(x) = c_(s_(t−1))(x) and s_t(x) = s_(t−1)(x) for every x
    with π(x) > π(y).
- Proof. (a) y ∈ Mv_t moves to k′ := s_t(y) with Ξ_(s_(t−1))(y, k′) ▷ cur_(s_(t−1))(y). (b) Every strict Ξ-descendant z of y has
  π(z) > π(y), so z ∉ Mv_t (y has the largest π in Mv_t), so s_t and s_(t−1) agree on them and by LOCAL (b) every option of y has the
  same value under both states; write v(k) for it. The options better than k′ are {k : v(k) > v(k′)} ⊆ {k : v(k) > v(k_old)} \ {k′},
  with k_old := s_(t−1)(y), since v(k′) > v(k_old) (ENC: a total order). So c strictly falls. (c) x ∉ Mv_t, and its strict
  Ξ-descendants have π > π(x) > π(y), so they are not in Mv_t either; LOCAL (b). ∎
- Corollary EXACT-ENERGY. Let D := max_x deg(x) ≥ 2 and E(s) := Σ_x c_s(x) · D^π(x). Then E(s_t) < E(s_(t−1)) at every step.
  Hence T ≤ E(s_0) ≤ D^N − 1.
- Proof. By DECREMENT the terms with π > π(y_t) are unchanged, the y_t term falls by at least D^π(y_t), and the terms below change
  by at most Σ_(p < π(y_t)) (D − 1) D^p = D^π(y_t) − 1 in total. Since 0 ≤ c ≤ D − 1, E < D^N. ∎
- Does NOT claim: any polynomial bound. It is an exponential bound and a structural fact (the unstable word in π order is a strictly
  decreasing counter). The truncations tested in box 147 (TOP_k for constant k, polynomial weights) are DEAD there and not claimed.

## 7. Corollaries TOP-MONO and RANK-BOUND (PROVED; degree ≤ 2)
- Definitions (degree ≤ 2). S(s) := {x : c_s(x) = 1}, the unstable set. For k ≥ 1, TOP_k(s) := the k largest values of π on S(s), in
  decreasing order, padded with −1 to length k; tuples are compared lexicographically. RANK_t := 1 + |{x ∈ S(s_(t−1)) : π(x) > π(y_t)}|.
- Corollary TOP-MONO. For every k ≥ 1 and step t: if RANK_t ≤ k then TOP_k(s_t) < TOP_k(s_(t−1)); if RANK_t > k then
  TOP_k(s_t) = TOP_k(s_(t−1)).
- Proof. Degree ≤ 2 gives c ∈ {0, 1}, so DECREMENT says y_t ∈ S(s_(t−1)) \ S(s_t) and S agrees on {π > π(y_t)} at both states; call
  that common part Hi (|Hi| = RANK_t − 1). If RANK_t > k, the first k entries of both tuples are the k largest elements of Hi: equal.
  If RANK_t ≤ k, the first RANK_t − 1 entries are Hi at both states; entry RANK_t is π(y_t) at s_(t−1), and at s_t it is either the
  largest π in S(s_t) below π(y_t) or the pad −1, smaller in both cases. ∎
- Corollary RANK-BOUND. For every k ≥ 1: |{t : RANK_t ≤ k}| ≤ Σ_(j=0..k) C(N, j) − 1. Hence for every set 𝒯 of steps with
  RANK_t ≤ R on 𝒯: |𝒯| ≤ Σ_(j=0..R) C(N, j) − 1; in particular U ≤ Σ_(j=0..R) C(N, j) − 1, with R := the largest RANK_t over the
  unchained steps (R := 0 if U = 0).
- Proof. TOP_k is non-increasing (TOP-MONO) and falls strictly at exactly the steps with RANK_t ≤ k. It is determined by the set of
  its non-pad entries, a subset of {0, …, N − 1} of size ≤ k, so it takes ≤ Σ_(j ≤ k) C(N, j) values, and a non-increasing sequence
  with that many values has at most one fewer strict falls. ∎
- Does NOT claim: R = O(1) (DEAD in box 147: R climbs to N − 1), nor any polynomial bound. It is a CONDITIONAL count bound.

## 8. Lemma INTERVAL-RESTRICT, Corollaries INTERVAL-CHARGE and RECURSION (PROVED; degree ≤ 2)
- Lemma INTERVAL-RESTRICT (degree ≤ 2, any width). Let k ≥ 1 and let [a, b) (0 ≤ a < b ≤ T + 1) be an interval of state indices with
  TOP_k(s_t) = TOP_k(s_a) for a ≤ t < b. Let p := the k-th entry of TOP_k(s_a) (possibly −1).
  - (i) For every step t with a < t < b, every mover x ∈ Mv_t has π(x) < p.
  - (ii) Let H be the genome G in which every mover x with π(x) ≥ p keeps only its option s_a(x) (same W-target, Ξ-target, β and
    gate), with start s_a. Then H is an IDEAL-ACYC genome of degree ≤ 2, and the first b − a states of H's run are s_a, …, s_(b−1).
  - (iii) For a + 2 ≤ t < b, step t of G's run is chained iff step t − a of H's run is chained.
- Proof.
  - (i) For a < t < b, TOP_k(s_t) = TOP_k(s_(t−1)), so RANK_t > k by TOP-MONO: at least k movers of S(s_(t−1)) have π > π(y_t).
    TOP_k(s_(t−1)) = TOP_k(s_a) lists the k largest π on S(s_(t−1)), so its k-th entry p satisfies p > π(y_t) ≥ π(x) for every
    x ∈ Mv_t. (If p = −1, S(s_(t−1)) has fewer than k elements, RANK_t ≤ |S(s_(t−1))| < k, so no such t exists.)
  - (ii) Validity: levels, W-targets and Ξ-targets of the kept options are unchanged; H's Ξ-graph is a subgraph of G's, so acyclic
    and π is still topological; ranks and gate indices remain distinct; every mover keeps ≥ 1 option; s_a is a state of H.
    - Induction on j with a + j < b: H's j-th state equals s_(a+j). For j = 0 by definition. Let s := s_(a+j) with a + j + 1 < b,
      put t := a + j + 1 and s′ := s_t.
    - Values: an option present in both genomes has the same chain and value under s in both (same targets and β's; the kept option
      of a trimmed mover is its option in s). So A^H_s(x) = A^G_s(x) when π(x) < p (all options kept), and A^H_s(x) = {s(x)} when
      π(x) ≥ p.
    - Keys under any state are the same in G and H (same gates, same W-targets).
    - By (i), s′(x) = s(x) for π(x) ≥ p, and Mv_t ≠ ∅ consists of movers with π < p, whose A^H = A^G has ≥ 2 elements; so H's run
      does not stop at s. Level by level, lowest first: a trimmed mover's H-choice is s(x) = s′(x); a mover with π(x) < p chooses the
      key-least option of A^H_s(x) = A^G_s(x) under keys that read H's new state at lower levels, which equals s′ there by induction
      on the level, so it chooses s′(x) as G does. H's new state is s′ ≠ s.
  - (iii) The label of step t reads Mv_t, Mv_(t−1) (hence h_t, h_(t−1), with the same levels and tie rule) and the chain of
    (h_t, s_t(h_t)) under s_(t−2), all from the states s_(t−2), s_(t−1), s_t with t − 2 ≥ a; by (ii) these are H's states
    t − a − 2, t − a − 1, t − a, and the chain is the same in H by the «Values» argument. ∎
- Corollary INTERVAL-CHARGE (degree ≤ 2). For every r ≥ 2:
  |{t : RANK_t = r}| ≤ (N − r + 1) · (1 + |{t : RANK_t ≤ r − 1}|).
- Proof. Cut the state indices 0..T into maximal intervals on which TOP_(r−1) is constant. By TOP-MONO a new interval starts exactly
  at the steps with RANK_t ≤ r − 1, so there are 1 + |{t : RANK_t ≤ r − 1}| intervals, and every step with RANK_t = r lies inside one
  (a < t < b). Let q(s) := the r-th entry of TOP_r(s). Inside an interval: at a step with RANK_t = r, TOP_r falls with its first r − 1
  entries fixed (TOP-MONO's proof), so q goes from π(y_t) to a smaller value; at a step with RANK_t > r, TOP_r is unchanged, so q is
  unchanged; steps with RANK_t < r do not occur inside. So the values π(y_t) at the rank-r steps of one interval strictly decrease,
  and each lies in {0, …, N − r} (r − 1 larger positions exist). So each interval holds ≤ N − r + 1 rank-r steps. ∎
- Corollary RECURSION (degree ≤ 2). Let [a_1, b_1), …, [a_m, b_m) be the maximal TOP_1-constant intervals (a_1 = 0, a_(i+1) = b_i,
  b_m = T + 1), p_i := the entry of TOP_1(s_(a_i)), and for p_i ≥ 0 let H_i be INTERVAL-RESTRICT's genome for k = 1 on [a_i, b_i).
  Then
  - U(G) ≤ (m − 1) + Σ_(i : p_i ≥ 0) (U(H_i) + 1), where U(H_i) is U of H_i's run from s_(a_i);
  - p_1 > p_2 > … (strictly, TOP-MONO with k = 1), the positions p_i ≥ 0 are positions of degree-2 movers, and H_i has degree-2
    movers only at positions < p_i.
  - So, with n := the number of degree-2 movers and U*(n) := the largest U over all degree-≤-2 IDEAL-ACYC genomes with at most n
    degree-2 movers and all their starts (finite by EXACT-ENERGY applied to the degree-2 movers alone: T < 2^n),
    U*(n) ≤ n + Σ_(p=0..n−1) (U*(p) + 1).
- Proof. An unchained step t ∈ [2, T] is (α) a boundary step t = a_i with i ≥ 2 (≤ m − 1 of them), or (β) the first step a_i + 1
  inside an interval (≤ 1 per interval with p_i ≥ 0; an interval with p_i = −1 has S = ∅, so no step leaves it, and it is the last
  one with no step inside), or (γ) a step a_i + 2 ≤ t < b_i, which by INTERVAL-RESTRICT (iii) is unchained iff step t − a_i ≥ 2 of
  H_i's run is unchained; distinct t give distinct t − a_i, and H_i's run has these steps by (ii). This gives the first line. Unstable
  movers have degree 2 (c ≤ deg − 1), so p_i ≥ 0 is a degree-2 position. In H_i every mover with π ≥ p_i has degree 1, so its
  degree-2 movers are among the degree-2 movers with π < p_i; their number is < n and strictly decreases with i. So m − 1 ≤ n and the
  sum runs over distinct values p < n. (EXACT-ENERGY with the positions renumbered among degree-2 movers only: degree-1 movers have
  c = 0 and never move, so the proof is unchanged.) ∎
  - Note (vs box 148): the lane form «U*(n) ≤ Σ_(p<n) (U*(p) + 1)» (docs/new/N5-INTERVAL-box148.md §1) omits the boundary steps (α);
    this packet proves only the form above. The box 148 form is not violated on the data (§9, REC148 0) but is NOT claimed.
- Does NOT claim: any polynomial bound (the recursion only gives an exponential bound); that the number of interval openings, or of
  «releases of frozen top movers», is equivalent to the run length (only one direction is trivial, N5-IDEAL-STATE §6).

## 9. Machine check, excluded parts, TARGET diff (not to sign)
- Machine check: experiments/new/box150/check.py, wired into experiments/new/check.sh (block w99).
  - It has its own simulator of §0 (Ξ-values through ENC's integers; keys under the new state, root-first) and cross-checks the state
    sequence against box139/paths.py run() (XSIM).
  - Per run it counts the violations of MONO, XI-NEW (every least-level mover, all ties), RISE (a)-(c), CHAIN-BACK (i)-(ii), KEYFLIP
    and KF-EQ, DECREMENT (a)-(c) and EXACT-ENERGY, TOP-MONO (every k), RANK-BOUND (every k, and U), INTERVAL-RESTRICT (i)-(iii) (every
    k, every maximal TOP_k-constant interval: it builds H and runs it), INTERVAL-CHARGE (every r), RECURSION (first line). It also
    reports REC148 (the box 148 form) for information.
  - DATA (2026-11-03): 0 violations of every check on the 46 corpus genomes of boxes 140-149 (with the R188 pins x3_L8 and g4_L12 and
    the R189 pins lag1, lag1u, lag2c_d4, nest_d3_L4 as IDEAL genomes; 386 steps), and on 75,518 runs = every start of 200 random
    IDEAL-ACYC genomes (box150/rand.py seed 150; width 1-3, depth 1-4, degree 1-4: 107 of them have a mover of degree 3 or 4; 93,963
    steps). REC148 0 everywhere.
  - Negative controls (NEG=1/2/3: key-greatest choice, availability ignored, keys of the OLD state): the checks fire (NEG=3 on the
    random genomes: XINEW 6, RISE 3, XSIM 8), so XI-NEW's dependence on «keys under the new state» is visible in the data.
- EXCLUDED from this packet (not to sign; they stay lane statements):
  - R178's real-N5 form of XI-NEW (needs the TWO-FIX window and the corner exclusion; not written here as a complete proof).
  - The 2-wide ladder identity KF_x = F_(lev(x)−1) and «IDEAL-ACYC-POLY ⟺ Σ_l F_l poly» (N5-IDEAL-STATE §5): needs the ladder's
    definition and a key-extension argument not written here in full.
  - Box 148's opening dichotomy (release or fresh Ξ-wake) and its ladder reading.
  - Box 147's degree-D TOP forms (TOP-MONO fails as stated when an unstable mover stays unstable after a move).
  - Every CONJECTURE of N5-IDEAL-STATE §3 (U-LIN, DELAY-LIN, DELSTEP-LIN, UP-LIN) and every DEAD item of §2.
- Diff against TARGET.md (statement by statement): TARGET.md's objects are parity games, winning regions, algorithms and their running
  time on the word RAM (§1-§3), milestone M4 (§2) and M3 (§4, §7e). No statement of this packet mentions a parity game, a winning
  region, an algorithm's running time, or a complexity class: each is about the step sequence of the IDEAL model of RESULTS R104 §0
  definition. None is an M4 or M3 claim, none bounds anything polynomially, and none is a gauntlet step for any algorithm. The only
  link to the fleet question is R104 (landed, not used here): a super-polynomial IDEAL-ACYC family would give real games with
  super-polynomially long FL runs of N5. That link is R104's statement, not this packet's. G-N5-TIME stays OPEN.
- READING (value): the packet fixes in one refereed place the three equivalent growth measures of IDEAL-ACYC runs (T, U, and KF at
  degree ≤ 2), plus the exponential counter (EXACT-ENERGY) that every attempted polynomial potential must coarsen. Later attempts can
  be scored against U or KF with a signed reduction.
