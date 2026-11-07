# Packet P-IDEAL-KEYS (box 172): the key side of the IDEAL-ACYC model — a mover's key preference depends only on its W-closure (LOCAL-KP); at degree 2 its key flips are the order flips of its two W-targets (PAIR-KF); every order flip of a same-level pair is its own move or one flip of the pair below (CASCADE); a top-only interval starting at t ≥ 2 follows a lower step that strictly raised the moving top mover's chosen option value (RENEW); MERGE and RETURN on the Ξ side; DEAD: PM, PMV and the doubling-tower step
L-NEW successor 55 (Opus 5.5), D14 / D18 / D20; Lead brief BOX 172 (2026-11-05): «freeze packet P-IDEAL-KEYS for the referees».
Written 2026-11-05 from 22:57Z (date -u: see the commit). FROZEN at push: later text goes into docs/new/P-IDEAL-KEYS-fixes.md
(append-only). Sources: docs/new/N5-PERMOVER-box165.md §1 (MERGE), N5-PMKILL-box166.md §0-§1 (PM kill, RETURN, PMV),
N5-PMPRIME-box167.md §0 (LOCAL-KP), N5-CLOCK-box168.md §0 (PAIR-KF), N5-PAIRLIN-box169.md §0 (CASCADE), N5-TOWER-box170.md §0 (F ≤ T,
tower), N5-FROZEN-box171.md §0 (RENEW), all by successor 54. This packet governs: every proof is written out in full HERE and is
checked against this text only; no other file carries a proof of a statement below. Labels: PROVED (L-NEW 54/55, unrefereed) / DEAD /
DATA / READING (not to sign). Not a TARGET.md claim. Every statement is about the IDEAL-ACYC model only. No polynomial bound is claimed.
PAIR-LIN, RENEW-COUNT, PM′_S, SLOT-TRADE and G-N5-TIME stay OPEN.

## To sign, and what is not to sign
| § | statement | label | hypotheses |
| --- | --- | --- | --- |
| §2 | Lemma LOCAL-KP (a) keys depend only on W(x); (b) KF_x ≤ WE_x | PROVED | IDEAL-ACYC, any degree |
| §3 | Lemma PAIR-KF (a), (b); Corollary PAIR-MOVES | PROVED | deg(x) = 2, lev(x) ≥ 1; the corollary: every mover of degree ≤ 2 |
| §4 | Lemma CASCADE (a), (b); Corollary F ≤ T; Corollary LADDER (𝓛^R_d) | PROVED | IDEAL-ACYC, any degree; LADDER: 𝓛^R_d |
| §5 | Lemma RENEW (a), (b) | PROVED | IDEAL-ACYC, any degree |
| §6 | Lemma MERGE (a), (b); Lemma RETURN; Corollary RETURN-COUNT | PROVED | IDEAL-ACYC; MERGE any degree; RETURN: deg(x) = 2 |
| §7 | DEAD: CONJECTURE PM; CONJECTURE PMV; the doubling-tower step | DEAD (instances; tower by Corollary F ≤ T) | refutations of lane statements |
| §8 | DATA, machine checks, excluded parts, TARGET diff | DATA / READING (not to sign) | |

- Premises (LANDED only).
  - RESULTS R104 (P-N5-REALIZE): ONLY its definition of the IDEAL model and of the Ξ-graph, restated in §0. No theorem of R104 is used.
  - RESULTS R105 (P-IDEAL-RED), these items only, quoted verbatim from the R105 statement (RESULTS l. 10155 on trunk b5d154ad):
    - «(ENC) the Ξ-order of β-sets is the order of the integers Σ ±2^rank (+ for even parity), so, with ε(x, k) := ±2^rank(x, k) (+ for
      even parity), the value of option (x, k) is ε(x, k) plus the current value of its Ξ-target (ε(x, k) alone if the Ξ-target is the
      exit X)» — used in §6.
    - «(MONO) the current Ξ-value of every mover never decreases along a run» — used in §6 (RETURN).
    - «(XI-NEW) for t ≥ 2 every least-level mover h of step t moves to an option w ∉ A_(s_(t−2))(h) (A_s(h): h's current option under
      s and its options strictly better under s)» and «(RISE) that option's value rose strictly at step t − 1, and some strict
      Ξ-descendant of h on its chain under s_(t−2) moved at step t − 1», in the signed form of R105's body item (e): «(a) v_(s_(t−1))(h,
      w) > v_(s_(t−2))(h, w): the value of option (h, w) rose strictly at step t − 1;»; «(b) the set Z_t of movers z ≠ h on the chain of
      (h, w) under s_(t−2) with z ∈ Mv_(t−1) is nonempty;»; «(c) every z ∈ Z_t is a strict Ξ-descendant of h, so π(z) > π(h).» — used in
      §5 (RENEW) only.
    - At degree ≤ 2 only: «(KEYFLIP) moves(x) ≤ 1 + KF_x with KF_x the number of steps at which KP(x) changes, so T ≤ N + KF and KF ≤
      N T (T polynomial iff KF is)», with «KP_s(x) the key-preferred option under the keys of s» — used in §3 (Corollary PAIR-MOVES)
      and §4 (Corollary LADDER) only.
  - RESULTS Erratum E-2 to R105, checked item by item. (E2c) bears on KEYFLIP: «(E2c) KEYFLIP's «moves(x)» is used without its binder;
    the packet defines moves(x) as the number of steps t with x ∈ Mv_t (§0 l. 59).» This packet uses exactly that binder (§0). (E2a)
    (CHAIN-BACK's «chained») and (E2b) (TOP-MONO's RANK_t) concern items not used here, so they do not bear.
  - RESULTS R110 (P-IDEAL-FLIP): ONLY its definition of 𝓛^R_d, restated in §0; used by Corollary LADDER only. No theorem of R110 is used.
  - Not used: R105's LOCAL, CHAIN-BACK, U-EQ, DECREMENT, EXACT-ENERGY, TOP-MONO, RANK-BOUND, INTERVAL-RESTRICT, INTERVAL-CHARGE,
    RECURSION; R106-R109; docs/lit, docs/sources; any other lane file; no outside source. No machine premise is used by any signed item.
- Each statement lists its hypotheses and a paragraph «does NOT claim».

## 0. The model (RESULTS R104's definition, as restated in P-IDEAL-FLIP §0) and the notation of this packet
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
  - KP_s(x) := the option k of x with the least key_s(x, k) (unique by (F1)); KF_x := #{t ∈ [1, T] : KP_(s_t)(x) ≠ KP_(s_(t−1))(x)}
    (R105's «number of steps at which KP(x) changes», read with the keys of s_t against those of s_(t−1)).
  - W(x) := the set of movers reachable from x by following W-targets of options (of any option, at every mover on the way), x
    excluded. Every mover of W(x) has level < lev(x); W(x) = ∅ at level 0; W(y) ⊆ W(x) for y ∈ W(x).
  - WE_x := #{t ∈ [1, T] : Mv_t ∩ W(x) ≠ ∅}.
  - D(x) := the set of strict Ξ-descendants of x (movers reachable from x along Ξ-edges of any options, x excluded); desc(x) := |D(x)|.
  - For two distinct movers p, q of one level: ord_s(p, q) := [key_s(p, s(p)) < key_s(q, s(q))] (a truth value); a FLIP of (p, q) at
    step t ∈ [1, T] means ord_(s_t)(p, q) ≠ ord_(s_(t−1))(p, q); flips(p, q) := the number of steps t ∈ [1, T] at which (p, q) flips.
  - v_s(x, k) := the integer Σ_(β ∈ Ξ_s(x, k)) ±2^rank(β) (+ for even parity), so by ENC, for distinct sets, P ▷ Q iff the integer of P
    is larger; cv_s(x) := v_s(x, s(x)) (the current value); cv_s(X) := 0 by convention. By ENC, v_s(x, k) = ε(x, k) + cv_s(xt(x, k)).
  - 𝓛^R_d (RESULTS R110's definition, verbatim from its statement: «the 2-wide degree-2 ladders in L-RED's R197 convention (movers 2l
    and 2l + 1 on level l, all of degree 2, no other movers, option k of a mover of level l ≥ 1 W-pointing to mover 2(l − 1) + k)»),
    levels 0, …, d − 1. On 𝓛^R_d, F(l) := flips(2l, 2l + 1).
  - Top level τ := max_x lev(x). A step t is TOP-ONLY if every mover of Mv_t has level τ, LOWER otherwise. A TOP-ONLY INTERVAL is a
    maximal interval [a, b] ⊆ [1, T] of consecutive top-only steps.

## 2. Lemma LOCAL-KP (PROVED)
- Hypotheses: G IDEAL-ACYC, any degree; s, s′ any two states; x any mover.
- (a) If s(y) = s′(y) for every y ∈ W(x), then key_s(x, k) = key_(s′)(x, k) for every option k of x; hence KP_s(x) = KP_(s′)(x).
- (b) For every run, KF_x ≤ WE_x.
- Proof of (a), by induction on lev(x). lev(x) = 0: key_s(x, k) = (g(x, k)) = key_(s′)(x, k). lev(x) ≥ 1: let y := wt(x, k). Then y ∈
  W(x), so s(y) = s′(y) =: j, and W(y) ⊆ W(x), so s, s′ agree on W(y); by the induction hypothesis (lev(y) = lev(x) − 1) key_s(y, j) =
  key_(s′)(y, j). Hence key_s(x, k) = key_s(y, j) followed by g(x, k) = key_(s′)(y, j) followed by g(x, k) = key_(s′)(x, k). All keys of
  x agree, so their unique minimum (F1) is the same option. ∎
- Proof of (b). If Mv_t ∩ W(x) = ∅, then s_t and s_(t−1) agree on W(x), so KP_(s_t)(x) = KP_(s_(t−1))(x) by (a). So every step counted
  in KF_x is counted in WE_x. ∎
- Does NOT claim: that KP depends on all of W(x) (only an upper bound on what it reads); any bound on WE_x or KF_x; anything about the
  A-sets (LOCAL-KP is about keys only; R105's LOCAL is not used).

## 3. Lemma PAIR-KF (PROVED) and Corollary PAIR-MOVES
- Hypotheses: G IDEAL-ACYC (any degree elsewhere); x a mover with deg(x) = 2 and lev(x) ≥ 1; options 0, 1; a := wt(x, 0), b := wt(x, 1).
- (a) If a = b, KP_s(x) is the option of x with the smaller gate, for every state s; so KF_x = 0 in every run.
- (b) If a ≠ b, then for every state s: KP_s(x) = 0 iff ord_s(a, b) is true; so KF_x = flips(a, b) in every run.
- Proof. key_s(x, k) = key_s(wt(x, k), s(wt(x, k))) followed by g(x, k), the prefix having length lev(x) (F1).
  - (a): both prefixes equal key_s(a, s(a)); the tuples differ only in the last entries g(x, 0) ≠ g(x, 1), which decide.
  - (b): the prefixes are the keys of the options (a, s(a)) and (b, s(b)), two distinct options of level lev(x) − 1, so they differ by
    (F1). Lexicographic comparison of two tuples of equal length decides at the first differing entry, which lies in the prefix; so
    key_s(x, 0) < key_s(x, 1) iff key_s(a, s(a)) < key_s(b, s(b)), i.e. KP_s(x) = 0 iff ord_s(a, b). Then KP_(s_t)(x) ≠ KP_(s_(t−1))(x)
    iff ord_(s_t)(a, b) ≠ ord_(s_(t−1))(a, b), and the two counts are equal. ∎
- Corollary PAIR-MOVES (PROVED; premise R105 KEYFLIP). If every mover of G has degree ≤ 2, then in every run, for every mover x:
  moves(x) ≤ 1 + flips(wt(x, 0), wt(x, 1)) if deg(x) = 2, lev(x) ≥ 1 and wt(x, 0) ≠ wt(x, 1); moves(x) ≤ 1 otherwise. Hence
  T ≤ Σ_x moves(x) ≤ N + Σ_x flips(wt(x, 0), wt(x, 1)), the sum over the movers of the first kind.
  - Proof. KEYFLIP gives moves(x) ≤ 1 + KF_x. First kind: KF_x = flips(…) by (b). Otherwise: deg(x) = 1 gives moves(x) = 0
    (A-sets are {s(x)}); deg(x) = 2 with lev(x) ≥ 1 and equal W-targets gives KF_x = 0 by (a); deg(x) = 2 with lev(x) = 0 gives
    key_s(x, k) = (g(x, k)) for every s, so KP is constant and KF_x = 0. Every step t ∈ [1, T] has Mv_t ≠ ∅, so T ≤ Σ_x moves(x). ∎
- Does NOT claim: any bound on flips(a, b) (CONJECTURE PAIR-LIN, flips ≤ c · |{a, b} ∪ W(a) ∪ W(b)|, is OPEN and is not stated for
  signing); PAIR-MOVES at degree ≥ 3 (KEYFLIP is degree ≤ 2 only); that moves(x) = 1 + KF_x ever holds beyond the instances of §8.

## 4. Lemma CASCADE (PROVED), Corollary F ≤ T, Corollary LADDER
- Hypotheses: G IDEAL-ACYC, any degree; p ≠ q two movers of one level l; t ∈ [1, T] a step at which (p, q) flips.
- (a) If l = 0, then p ∈ Mv_t or q ∈ Mv_t.
- (b) If l ≥ 1, exactly one of the following holds:
  - (own) p ∈ Mv_t or q ∈ Mv_t;
  - (below) p, q ∉ Mv_t, the current W-targets w_p := wt(p, s_t(p)) and w_q := wt(q, s_t(q)) are distinct movers (of level l − 1), and
    (w_p, w_q) flips at step t.
- Proof. (own) and (below) exclude each other by definition. Suppose p, q ∉ Mv_t, so s_t(p) = s_(t−1)(p) and s_t(q) = s_(t−1)(q). If l = 0,
  key_s(p, s(p)) = (g(p, s(p))) and the same for q, so both keys are the same under s_(t−1) and s_t and (p, q) does not flip:
  contradiction, which proves (a). Let l ≥ 1. Under s ∈ {s_(t−1), s_t}, key_s(p, s(p)) = key_s(w_p, s(w_p)) followed by g(p, s_t(p)),
  with the same w_p for both states, and the same for q. If w_p = w_q, the two prefixes are equal under each s and the order is decided
  by the constant gates g(p, s_t(p)) ≠ g(q, s_t(q)): no flip, contradiction. So w_p ≠ w_q; then the prefixes are keys of two distinct
  options of level l − 1, they differ (F1), and as in §3 (b) ord_s(p, q) = ord_s(w_p, w_q) for both s. A flip of (p, q) is then a flip
  of (w_p, w_q). ∎
- Corollary F ≤ T (PROVED; immediate from the definition). flips(p, q) ≤ T for every pair and every run: flips counts steps, and a
  pair flips at most once per step. (Listed because box 169's recursion counted flip EVENTS; with CASCADE, every flip of a pair at a
  step is one step, whatever happens below.)
- Corollary LADDER (PROVED; premises: R110's definition of 𝓛^R_d; R105 KEYFLIP). Let G ∈ 𝓛^R_d (d ≥ 1) and any run. Then
  - F(0) ≤ moves(0) + moves(1) ≤ 2, and F(l) ≤ moves(2l) + moves(2l + 1) + F(l − 1) for 1 ≤ l ≤ d − 1;
  - moves(x) ≤ 1 + F(lev(x) − 1) for lev(x) ≥ 1, so F(l) ≤ 2 + 3 F(l − 1) and F(l) ≤ 3^(l+1) − 1; and F(l) ≤ T for every l.
  - Proof. F(0): (a) — each flip step of (0, 1) moves 0 or 1, and level-0 movers of degree 2 move at most once (PAIR-MOVES, «otherwise»
    case). Level l ≥ 1: by (b), each flip step of (2l, 2l + 1) is an own step (at most moves(2l) + moves(2l + 1) of them) or a below
    step; at a below step the distinct current W-targets are movers of level l − 1, i.e. {2l − 2, 2l − 1}, and they flip at t; distinct
    steps, so the below steps are at most F(l − 1). Every mover x of level l ≥ 1 has wt(x, k) = 2(l − 1) + k, distinct, so PAIR-MOVES
    gives moves(x) ≤ 1 + F(l − 1). Hence F(l) ≤ 2(1 + F(l − 1)) + F(l − 1); with F(0) ≤ 2, F(l) + 1 ≤ 3 (F(l − 1) + 1) gives
    F(l) ≤ 3^(l+1) − 1. F(l) ≤ T is Corollary F ≤ T. ∎
- Does NOT claim: a polynomial bound on any F(l) (3^(l+1) − 1 is exponential; PAIR-LIN is OPEN); that either inequality of LADDER is
  tight in general (it is tight at level 3 of one instance, §7 (c)); anything outside 𝓛^R_d for LADDER; that a cascade cannot be wide
  (one low move may flip many pairs at the same step; only «at most once per pair per step» is claimed).

## 5. Lemma RENEW (PROVED; premises R105 XI-NEW, RISE; LOCAL-KP)
- Hypotheses: G IDEAL-ACYC, any degree; τ its top level; a run; [a, b] a top-only interval.
- (a) If a ≥ 2, then step a − 1 is a LOWER step, and for every h ∈ Mv_a, with w := s_a(h):
  - (i) w ∉ A_(s_(a−2))(h);
  - (ii) v_(s_(a−1))(h, w) > v_(s_(a−2))(h, w): step a − 1 strictly raised the value of the option that h takes at a;
  - (iii) some mover z ≠ h on the chain of (h, w) under s_(a−2) lies in Mv_(a−1), and every such z lies in D(h).
  The same (i)-(iii) hold, with a replaced by t, for every top-only step t ≥ 2 (for t > a inside the interval, step t − 1 is top-only).
- (b) For every top mover h and every option k of h, key_(s_u)(h, k) is the same for all u ∈ [a − 1, b]; so KP_(s_u)(h) is constant on
  [a − 1, b].
- Proof of (a). a − 1 ≥ 1 is a step, and it is not top-only, since [a, b] is maximal: so it is a LOWER step. Every mover of Mv_t
  (t = a, or any top-only t ≥ 2) has level τ, the largest level, so every h ∈ Mv_t is a least-level mover of step t. R105 XI-NEW
  («for t ≥ 2 every least-level mover h of step t moves to an option w ∉ A_(s_(t−2))(h)») gives (i), and RISE in its signed form (body
  item (e) (a), (b), (c), quoted above) gives (ii) and (iii). ∎
- Proof of (b). Every mover of Mv_u, u ∈ [a, b], has level τ; W(h) contains only movers of level < τ; so s_(a−1), s_a, …, s_b agree on
  W(h), and LOCAL-KP (a) gives equal keys and equal KP. ∎
- Reading of (a)+(b), as the box 171 statement «a top-only interval starting at t ≥ 2 follows a lower step that strictly raised the
  moving top mover's chosen option value»: the interval's first move of h is to an option that was not available two states earlier and
  whose value rose at the lower step just before; the keys of the top movers do not change inside the interval (b). Part (iii) does
  not say that z is below the top: z may be a top mover moving together with lower movers at step a − 1.
- Does NOT claim: any bound on the number of top-only intervals (CONJECTURE RENEW-COUNT, «the lower steps that renew a top mover number
  O(d)», is OPEN and not stated for signing); that the key change at a − 1 plays no role in which option h takes (the choice among A
  is still by keys); anything for t = 1 (an interval starting at a = 1 has no step before it); that z is unique.

## 6. Lemma MERGE, Lemma RETURN, Corollary RETURN-COUNT (PROVED; premises R105 ENC, MONO)
- Lemma MERGE. Hypotheses: G IDEAL-ACYC, any degree; x a mover with two distinct options a, b (x may have more); s a state. Let y_1,
  …, y_p be the movers of the chain of (x, a) under s after (x, a) (y_1 = xt(x, a), y_(i+1) = xt(y_i, s(y_i)); p = 0 if xt(x, a) = X),
  and z_1, …, z_q those of (x, b). Let m be the first y_i that equals some z_j, at positions i and j (if none, m := X, i := p + 1,
  j := q + 1). Pre_a := {y_1, …, y_(i−1)}, Pre_b := {z_1, …, z_(j−1)}.
  - (a) v_s(x, a) − v_s(x, b) = (ε(x, a) + Σ_(i′ < i) ε(y_(i′), s(y_(i′)))) − (ε(x, b) + Σ_(j′ < j) ε(z_(j′), s(z_(j′)))).
  - (b) If a state s′ agrees with s on Pre_a ∪ Pre_b, then v_(s′)(x, a) − v_(s′)(x, b) = v_s(x, a) − v_s(x, b); in particular the
    Ξ-order of (x, a) and (x, b) is the same under s′ as under s.
  - Proof. ENC unrolled along a chain: if c_1 = xt(x, a), c_2, … is the chain's mover sequence under a state r, then for every
    position i with c_i a mover, v_r(x, a) = ε(x, a) + Σ_(i′ < i) ε(c_(i′), r(c_(i′))) + cv_r(c_i) (induction on i, ENC at each
    step), and the same with cv_r(X) = 0 when the chain ends. (a): apply this at y_i = m = z_j (or at the ends, m = X) for both options
    under s; the terms cv_s(m) are the same and cancel. (b): under s′ the chain of (x, a) starts at y_1 = xt(x, a) and, since s′ = s on
    y_1, …, y_(i−1), visits y_1, …, y_(i−1) and then m (each next mover is xt of the current mover's s′-option); the same for (x, b)
    up to m. Apply the unrolled identity under s′ at m: the prefix sums are the ones of (a), and cv_(s′)(m) cancels. The Ξ-order is
    the sign of the difference, by ENC (the two Ξ-sets differ: β(x, a) lies only in the first, since x does not recur on an acyclic
    chain). ∎
  - Does NOT claim: that Pre_a ∪ Pre_b is the same set under s′ beyond the merge point (it is the same up to m only); anything about
    keys.
- Lemma RETURN. Hypotheses: G IDEAL-ACYC, any degree elsewhere; x a mover with deg(x) = 2 and options o, o′; a run; steps t_1 < t_2
  with x ∈ Mv_(t_1), s_(t_1)(x) = o, x ∉ Mv_u for t_1 < u < t_2, and x ∈ Mv_(t_2). Then z := xt(x, o′) is a mover (not X), and
  cv_(s_(t_2 − 1))(z) > cv_(s_(t_1 − 1))(z).
  - Proof. By (F2) at t_1: s_(t_1 − 1)(x) = o′ and v_(s_(t_1 − 1))(x, o) > v_(s_(t_1 − 1))(x, o′). Between t_1 and t_2 x stays at o, so
    s_(t_2 − 1)(x) = o and s_(t_2)(x) = o′; by (F2) at t_2: v_(s_(t_2 − 1))(x, o′) > v_(s_(t_2 − 1))(x, o). For every option k of x,
    v_r(x, k) = ε(x, k) + cv_r(xt(x, k)) (ENC; cv_r(X) = 0), and cv_r(y) never decreases along the run (MONO, read through ENC's
    integer order), so v_r(x, o) is non-decreasing along the run. Hence v_(s_(t_2 − 1))(x, o′) > v_(s_(t_2 − 1))(x, o) ≥
    v_(s_(t_1 − 1))(x, o) > v_(s_(t_1 − 1))(x, o′). If z = X, v(x, o′) = ε(x, o′) would be constant: contradiction. So z is a mover and
    cv(z) = v(x, o′) − ε(x, o′) rose strictly. ∎
- Corollary RETURN-COUNT. For x as in RETURN (deg(x) = 2), with R(x, k) := #{u ∈ [1, T] : cv_(s_u)(xt(x, k)) > cv_(s_(u−1))(xt(x, k))}
  (R(x, k) := 0 if xt(x, k) = X): moves(x) ≤ 1 + R(x, 0) + R(x, 1).
  - Proof. Let t_1 < … < t_M be the steps moving x. For i ∈ [2, M], RETURN applied to t_(i−1), t_i gives a mover z_i = xt(x, k_i) (k_i
    := s_(t_i)(x)) whose current value at s_(t_i − 1) exceeds that at s_(t_(i−1) − 1); so at some step u_i ∈ [t_(i−1), t_i − 1] it
    rises (telescoping). The intervals [t_(i−1), t_i − 1] are pairwise disjoint, so i ↦ (u_i, k_i) is injective into the set of pairs
    (u, k) with cv(xt(x, k)) rising at u, which has R(x, 0) + R(x, 1) elements. So M − 1 ≤ R(x, 0) + R(x, 1). ∎
- Does NOT claim (RETURN, RETURN-COUNT): any bound on R(x, k) in terms of desc (PMV is DEAD, §7 (b)); anything at deg(x) ≥ 3; that the
  rise of cv(z) happens at a step where z itself moves (it may come from z's own descendants).

## 7. DEAD items (lane statements refuted; each with its instance and the exact check)
- (a) CONJECTURE PM (box 165): «for every IDEAL-ACYC genome and every start, moves(x) ≤ (deg(x) − 1)(1 + desc(x)) for every mover x».
  - Instance: experiments/new/box166/out/KILL_PM_compose_dd_d5_F14.json (sha1 c025a4b6…, full in §8), IDEAL-ACYC, every mover of degree
    2, N = 15, levels 0-4, from its stored start T = 14. Mover 12: D(12) = {10, 11, 13, 14} (desc 4), moves at steps 1, 2, 5, 8, 9, 10:
    moves(12) = 6 > (2 − 1)(1 + 4) = 5.
  - Option fields (W-target, Ξ-target, gate, β rank, β parity): mover 0 (lev 0): (−, 4, 4, 7, even), (−, 3, 17, 12, odd); 1 (lev 0):
    (−, 9, 3, 6, odd), (−, X, 9, 10, even); 2 (lev 1): (0, 8, 18, 1, odd), (1, 1, 15, 4, odd); 3 (lev 1): (0, X, 11, 19, even), (1, X,
    16, 9, odd); 4 (lev 2): (2, 6, 6, 16, odd), (3, 9, 2, 15, odd); 5 (lev 2): (2, 8, 19, 13, odd), (3, 3, 8, 8, odd); 6 (lev 3): (4, 7,
    0, 14, even), (5, 5, 5, 11, odd); 7 (lev 3): (4, 5, 7, 3, even), (5, 2, 10, 2, odd); 8 (lev 4): (6, 9, 12, 17, even), (7, 3, 14, 18,
    odd); 9 (lev 4): (6, 3, 13, 5, odd), (7, X, 1, 0, even); 10 (lev 1): (0, X, 21, 26, odd), (0, X, 20, 28, even); 11 (lev 1): (1, X,
    22, 22, odd), (0, 10, 23, 29, even); 12 (lev 4): (6, 14, 24, 25, even), (7, 13, 25, 21, even); 13 (lev 4): (6, 11, 26, 24, even), (7,
    10, 27, 23, odd); 14 (lev 1): (0, 10, 28, 20, even), (1, 11, 29, 27, even). Start 110111111000000 (movers 0..14).
  - Run (states s_0, …, s_14): 110111111000000, 111111101110101, 111111000110001, 111110010110011, 111110110110011, 111100100110111,
    010000000111110, 010001011111110, 010001111011000, 000011101011101, 001011000011001, 001010010011001, 001010110011001,
    001000100011001, 001000000011001.
  - Check: experiments/new/box172/keycheck.py line «DEAD PM …» (well-formed: W-targets exactly one level down, distinct gates and
    ranks, acyclic Ξ-graph; desc and moves recomputed); experiments/new/box150/check.py on the file: XSIM 0 (two simulators agree state
    for state) and 0 violations of every R105 check. L-RED replayed the instance independently (reported in the Lead brief of BOX 172;
    not re-checked here).
  - Does NOT claim: that T is long (T = 14 is dd_d5_F14's T; the extra moves happen inside its steps); anything about PM restricted to
    𝓛^R_d or to R109's 𝓛_d (the instance is in neither: levels 1 and 4 have more than two movers).
- (b) CONJECTURE PMV (box 166 §1, hypothesis (H-values)): «VR(z) ≤ 1 + desc(z) for every mover z», VR(z) := #{t ∈ [1, T] : cv_(s_t)(z)
  > cv_(s_(t−1))(z)}.
  - Instance: experiments/new/box172/inst/dd_d5_F14.json (sha1 06f0e501…; L-RED's claude/l-red experiments/red/r197/lag/dd_d5_F14.json,
    copied byte for byte), a genome of 𝓛^R_5, from its stored start T = 14. Mover 6: D(6) = {1, 2, 3, 5, 7, 8, 9} (desc 7); cv(6)
    rises at steps 2, 3, 4, 6, 7, 8, 10, 11, 12, 14: VR(6) = 10 > 1 + 7 = 8.
  - Option fields: identical to movers 0-9 of the instance in (a) (the composition of (a) is dd_d5_F14 plus movers 10-14). Start
    1101111110. Run: 1101111110, 1111111011, 1111110001, 1111100101, 1111101101, 1111001001, 0100000001, 0100010111, 0100011110,
    0000111010, 0010110000, 0010100100, 0010101100, 0010001000, 0010000000.
  - Check: keycheck.py line «DEAD PMV …»; box150/check.py on the file: XSIM 0, all R105 checks 0.
  - Does NOT claim: anything about moves(6) (it is 7 = 1 + desc(6)); a growth rate of VR.
- (c) The doubling-tower step (box 169 §0, «Predicted: F(l) = 2^(l+1) − 2, N = O(l²), and T ≥ F(l)», by iterating «F(l) = 2(1 + F(l − 1))»
  level by level over a fixed clock). DEAD as a route by Corollary F ≤ T: in one run every pair flips at most T times, so F(l) =
  2^(l+1) − 2 at level l needs T ≥ 2^(l+1) − 2 in the same run; the tower produces no exponential flip count without an exponential T,
  which is the open question itself.
  - Instance (the step is attained once, then blocked): dd_d5_F14 as in (b): pair flips by level F(0..4) = 2, 3, 6, 14, 7 and T = 14;
    F(3) = 14 = 2(1 + F(2)) (the doubling step attained, KEYFLIP tight at movers 6, 7: 7 moves each, KF 6); the next step needs 2(1 +
    F(3)) = 30 > 14 = T flips in this run. Compositions over this clock: KILL_PM_compose_dd_d5_F14.json (N 15) and
    experiments/new/box170/out/T1_dd_top8.json (sha1 9aead80e…, N 18, a desc-6 gadget on a reader of pair (6, 7), top mover with 8
    moves): both have T = 14 and largest pair flip count 14 = T.
  - Check: keycheck.py lines «DEAD TOWER …» and «TOWER composition …»; box150/check.py on T1_dd_top8.json: XSIM 0, all R105 checks 0.
  - Does NOT claim: that no IDEAL-ACYC family has exponential T (G-N5-TIME is OPEN); that a gadget can never add steps (DATA only: in
    the two compositions T stays 14); anything about R104's real games.

## 8. DATA, machine checks, excluded parts, TARGET diff (not to sign)
- Tool: experiments/new/box172/keycheck.py (deterministic, seed 172; simulator: box150/check.py's Gen, the R104 step). Output pinned
  in experiments/new/box172/keycheck.out and checked by block «P-IDEAL-KEYS» of experiments/new/check.sh, which also pins the sha1s of
  this packet, its line L-1 and the instances.
- Scope: 413 in-tree genome files (every JSON genome under experiments/new/box150 to box172 that parses, is well-formed, has a start and
  N ≤ 30; one run each, from its stored start) and 400 random IDEAL-ACYC genomes (levels 1-4, 1-3 movers per level, degree 2 or 3 with
  some degree-1 movers; every start if there are at most 64, else the genome start and 63 random ones): 13,813 runs, 14,027 steps.
  Each count covers ONLY the statement named:
  - LOCAL-KP (a): 27,102 (random state pair, mover) checks, 0 violations; control (change one mover of W(x)): fires 48,435 times.
  - LOCAL-KP (b) KF_x ≤ WE_x: 90,811 (run, mover) pairs, 0 violations.
  - PAIR-KF (a), (b): 34,113 (run, degree-2 mover of level ≥ 1) pairs, 0 violations.
  - CASCADE (a), (b): 15,614 pair flips (13,393 own, 2,221 below), 0 unclassified. Corollary F ≤ T: 0 violations on the same runs.
  - Corollary LADDER, first inequality only (F(l) ≤ moves(2l) + moves(2l + 1) + F(l − 1)): 231 runs of 𝓛^R genomes, 0 violations.
  - RENEW (a) (i)-(iii): 520 (step, mover) pairs at the first step of a top-only interval starting at t ≥ 2 (516 such steps), 0
    violations; the extension to every top-only step t ≥ 2: 573 pairs (these 520 included), 0 violations. RENEW (b): 2,704 top-only intervals, 0 violations.
  - MERGE (b): 19,932 (random state, degree-2 mover) checks, 0 violations; control (change one pre-merge mover): fires 23,272 times.
  - RETURN: 722 consecutive move pairs of degree-2 movers, 0 violations. RETURN-COUNT: 50,260 (run, degree-2 mover) pairs, 0 violations.
  - PAIR-MOVES (through R105 KEYFLIP): KEYFLIP itself on 51,431 (run, mover) pairs of degree-≤-2 genomes, 0 violations; PAIR-MOVES as
    stated: no separate DATA (it is PAIR-KF + KEYFLIP).
  - No DATA: Corollary LADDER's second and third bullets; RENEW's «reading» paragraph.
- The DEAD instances: keycheck.py lines «DEAD PM …», «DEAD PMV …», «DEAD TOWER …», «TOWER composition …» (exact values in §7);
  box150/check.py on KILL_PM_compose_dd_d5_F14.json, box172/inst/dd_d5_F14.json and box170/out/T1_dd_top8.json: «TOTAL genomes 1 runs 1
  steps 14 XSIM 0 … VIOL 0» each.
- Pins (sha1, full in check.sh): KILL_PM_compose_dd_d5_F14.json c025a4b6…, box172/inst/dd_d5_F14.json 06f0e501…,
  box170/out/T1_dd_top8.json 9aead80e…; box172/inst/max_d4_L13.json f0735b61… and max_d5_L15.json ba963ace… are copies of L-RED's
  files for box 173, used by no statement here.
- EXCLUDED (not to sign): CONJECTURES PAIR-LIN, PAIR-POLY, PM′_S, RENEW-COUNT, SLOT-TRADE; FREE-KP and the B-bit counts (box 166 §1-§2);
  the dynamic κ forms and LEVEL-PRODUCT reading (box 167); every DATA table and READING of boxes 165-171; the box 170 csp.py results.
- Diff against TARGET.md: no statement mentions a parity game, a winning region, an algorithm's running time or a complexity class.
  Each is about the step sequence of the IDEAL model of RESULTS R104's definition. None is an M4 or M3 claim, none bounds anything
  polynomially (LADDER's bound is exponential), none is a gauntlet step. G-N5-TIME stays OPEN.
- READING (value): the key side is now local and exact: a degree-2 mover's key preference is one bit, the order of its two W-targets'
  current keys (PAIR-KF), and that bit flips only by an own move of the pair or by one flip of the pair below (CASCADE). So T is
  polynomial at degree ≤ 2 iff the pair flip counts are (PAIR-MOVES with F ≤ T), and every bound on them must come through the moves
  of the pair's own movers, i.e. through the Ξ side (RETURN, RENEW). PM and PMV show that Ξ-only per-mover bounds fail.
