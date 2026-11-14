# Packet P-IDEAL-RISE (box 182): on 2-wide R197 ladders the weighted count Φ_K of key-misaligned movers falls at every step (PHIK-DESCENT), and no potential linear in the key-misalignment bits has a smaller range (OPT-K); option values never fall, every move raises its mover's value, and the largest number of rises of one option is polynomial iff the run length is (RISE-EQUIV, MOVE-RISE); two exact LP certificates bound the range of richer potentials from below
L-NEW successor 56 (Opus 5.5), D14 / D18 / D20; Lead brief BOX 182 (2026-11-06 12:43Z): «freeze a landable packet P-IDEAL-RISE from
your lane-proved boxes 179-181: PHIK-DESCENT, OPT-K (machine-checked range d ≤ 8; state it exactly), RISE-EQUIV, MOVE-RISE. Add DEAD
items with exact certificates if they are signable». Written 2026-11-06 from 12:52Z (date -u: see the commit). FROZEN at push: later
text goes into docs/new/P-IDEAL-RISE-fixes.md (append-only). Sources: docs/new/N5-LPOT-box179.md §0, §2, §3, §5b;
docs/new/N5-RISES-box180.md §1; docs/new/N5-RISEPROOF-box181.md §0 (all successor 56). This packet carries every proof in full and is
checked against this text only; no other file carries a proof of a statement below. Labels: PROVED (L-NEW 56, unrefereed) / CERTIFIED
(machine, exact rational arithmetic; not a hand proof) / DATA / READING (not to sign). Not a TARGET.md claim. Every statement is about
the IDEAL model of RESULTS R104 only. No statement bounds T polynomially. CONJECTURE RISE-2D, MOVES-2D, DBL-O(1), PAIR-LIN and G-N5-TIME
stay OPEN.

## To sign, and what is not to sign
| § | statement | label | hypotheses |
| --- | --- | --- | --- |
| §1 | Lemma KEY (a), (b), (c) | PROVED | (a), (c): 𝓛^R_d; (b): IDEAL-ACYC, a mover of degree 2 |
| §2 | Theorem PHIK-DESCENT; Corollary PHIK-T | PROVED | 𝓛^R_d |
| §3 | Theorem OPT-K | PROVED | 𝓛^R_d, d ≥ 1 |
| §4 | Lemma RISE-EQUIV (a), (b), (c); Lemma MOVE-RISE; Corollary MOVE-RISE-R | PROVED | IDEAL-ACYC, any degree, any width |
| §5 | Certificate items C-PHX3, C-PBG | CERTIFIED (machine) | 𝓛^R_d, d = 2, 3, 4; the feature classes of §5 |
| §6 | DATA, machine checks, excluded parts, TARGET diff | DATA / READING (not to sign) | |

- Premises (LANDED only), quoted verbatim from the RESULTS statements on trunk c8fefddb.
  - RESULTS R104 (P-N5-REALIZE): ONLY its definition of the IDEAL model and of the Ξ-graph, restated in §0. No theorem of R104 is used.
  - RESULTS R105 (P-IDEAL-RED), four items, used in §4 only: «(ENC) the Ξ-order of β-sets is the order of the integers Σ ±2^rank (+
    for even parity), so, with ε(x, k) := ±2^rank(x, k) (+ for even parity), the value of option (x, k) is ε(x, k) plus the current
    value of its Ξ-target (ε(x, k) alone if the Ξ-target is the exit X)»; «(MONO) the current Ξ-value of every mover never decreases
    along a run»; «(XI-NEW) for t ≥ 2 every least-level mover h of step t moves to an option w ∉ A_(s_(t−2))(h) (A_s(h): h's current
    option under s and its options strictly better under s)»; «(RISE) that option's value rose strictly at step t − 1, and some strict
    Ξ-descendant of h on its chain under s_(t−2) moved at step t − 1». RESULTS Erratum E-2 corrects R105's CHAINED binder (E2a),
    TOP-MONO's RANK_t (E2b) and KEYFLIP's moves(x) (E2c); none of these items is used here (moves(x) is defined in §0 with the E-2
    (E2c) binder anyway).
  - RESULTS R110 (P-IDEAL-FLIP): ONLY its definition of 𝓛^R_d: «the 2-wide degree-2 ladders in L-RED's R197 convention (movers 2l and
    2l + 1 on level l, all of degree 2, no other movers, option k of a mover of level l ≥ 1 W-pointing to mover 2(l − 1) + k)», levels
    0, …, d − 1.
  - RESULTS R111 (P-IDEAL-KEYS), one item, used in §2 and §3: «(CASCADE) at any degree, at every step at which two distinct movers p, q
    of one level l flip, p or q moves, or l ≥ 1, neither moves, their current W-targets w_p ≠ w_q and (w_p, w_q) flips at the same
    step, and flips(p, q) ≤ T». R111's «flip» is the one of §0 below.
  - Not used: R105 KEYFLIP, LOCAL and every other R105 item; R106-R110 theorems; R111 PAIR-KF, LOCAL-KP and its other items (§1
    re-proves the key facts needed); R112; the signed but not landed packet P-IDEAL-ALIGN (its ALIGN (a)-(c) and KP-MOVE are re-proved as
    Lemma KEY in §1; PAIR-DOUBLE and PATH-RISE are not used); docs/lit, docs/sources, any other lane file. The §5 items use a machine
    premise (the tool of §5); no other signed item does.
- Each statement lists its hypotheses and a paragraph «does NOT claim».

## 0. The model (RESULTS R104's definition, as restated in P-IDEAL-FLIP §0) and the notation of this packet
- A genome G has N ≥ 1 movers x, each with a level lev(x) ∈ {0, 1, …} and deg(x) ≥ 1 options (x, k). Each option has a W-target
  wt(x, k) (a mover of level lev(x) − 1; none at level 0), a Ξ-target xt(x, k) (a mover or the exit X), a β with a rank (distinct over
  all options) and a parity, and a gate index g(x, k) (distinct over all options). There is a start s_0. A state s picks one option
  s(x) per mover.
- Ξ-graph: an edge x → xt(x, k) for every option whose Ξ-target is a mover. IDEAL-ACYC: it is acyclic.
- Under s, the chain of (x, k) is (x, k), (y_1, s(y_1)), (y_2, s(y_2)), … with y_1 = xt(x, k), y_(j+1) = xt(y_j, s(y_j)), up to the
  first option whose Ξ-target is X. Its Ξ-value Ξ_s(x, k) is the set of β's on it. Two sets P ≠ Q are compared by the β of largest
  rank in P △ Q: the set containing it is better (P ▷ Q) if that β's parity is even, worse if odd.
- A_s(x) := {s(x)} ∪ {k : Ξ_s(x, k) ▷ Ξ_s(x, s(x))}.
- key_s(x, k) := (g(x, k)) if lev(x) = 0, else key_s(wt(x, k), s(wt(x, k))) followed by g(x, k); compared lexicographically.
- Step. If every A_(s_(t−1))(x) is a singleton, the run stops. Otherwise s_t is defined level by level, lowest level first:
  s_t(x) := the option in A_(s_(t−1))(x) with the least key_(s_t)(x, ·) (keys under the NEW state). If s_t = s_(t−1), the run stops
  without that step. T := the number of steps. Mv_t := {x : s_t(x) ≠ s_(t−1)(x)} for t ∈ [1, T] (nonempty for every such t). For a
  state s, step(s) denotes s_1 of the run started at s_0 = s (defined when that run has T ≥ 1).
- Facts immediate from the definition. (F1) key_s(x, k) is a tuple of length lev(x) + 1 whose last entry is g(x, k); so the keys of
  two distinct options of the same level differ, and the least key over any set of options of one mover is attained by exactly one
  option. (F2) If x ∈ Mv_t, then s_t(x) ∈ A_(s_(t−1))(x) \ {s_(t−1)(x)}, so Ξ_(s_(t−1))(x, s_t(x)) ▷ Ξ_(s_(t−1))(x, s_(t−1)(x)); if
  moreover deg(x) = 2, then A_(s_(t−1))(x) contains both options and s_(t−1)(x) is the other option of x. (F3) key_s(x, k) depends only
  on the options under s of movers of level < lev(x).
- Notation (all derived from the definition):
  - moves(x) := #{t ∈ [1, T] : x ∈ Mv_t} (the binder of Erratum E-2 (E2c)).
  - KP_s(x) := the option k of x with the least key_s(x, k) (unique by (F1)); k_s(x) := [s(x) ≠ KP_s(x)] (x is KEY-MISALIGNED at s).
  - For two distinct movers u, w of one level: ord_s(u, w) := [key_s(u, s(u)) < key_s(w, s(w))]; a FLIP of (u, w) at step t means
    ord_(s_t)(u, w) ≠ ord_(s_(t−1))(u, w); flips(u, w) := the number of steps at which (u, w) flips (as in R111).
  - On 𝓛^R_d (d ≥ 1): for 0 ≤ l ≤ d − 1, ord_l(s) := ord_s(2l, 2l + 1). For 1 ≤ l ≤ d − 1: c_l(s) := 0 if ord_(l−1)(s) is true, else 1
    (the option index that W-points to the lower mover whose current option has the smaller key); γ_l(j) := [g(2l, j) < g(2l + 1, j)].
  - v_s(x, k) := the integer Σ_(β ∈ Ξ_s(x, k)) ±2^rank(β) (+ for even parity); cv_s(x) := v_s(x, s(x)). R(x, k) := #{t ∈ [1, T] :
    v_(s_t)(x, k) > v_(s_(t−1))(x, k)} (the RISES of option (x, k)); M := the number of options.
  - w_l := 2^(d−l) − 1 for 0 ≤ l ≤ d − 1, and w_d := 0 (so w_l = 2w_(l+1) + 1 for l ≤ d − 1). Φ_K(s) := Σ_x w_lev(x) k_s(x).

## 1. Lemma KEY (PROVED)
- (a) Hypotheses: G ∈ 𝓛^R_d, s any state. For y ∈ {0, 1}, KP_s(y) is the same option for every s. For 1 ≤ l ≤ d − 1 and x ∈ {2l,
  2l + 1}, KP_s(x) = c_l(s). Hence, for x of level l ≥ 1, KP_(s′)(x) ≠ KP_s(x) iff ord_(l−1)(s′) ≠ ord_(l−1)(s), for any two states s, s′.
- (b) Hypotheses: G IDEAL-ACYC; x a mover with deg(x) = 2; any run. If x ∈ Mv_t, then s_t(x) = KP_(s_t)(x) and s_(t−1)(x) ≠ KP_(s_t)(x).
- (c) Hypotheses: G ∈ 𝓛^R_d; 1 ≤ l ≤ d − 1 or l = 0; s any state. If s(2l) = s(2l + 1) = j and l ≥ 1, then ord_l(s) = γ_l(j).
- Proof. (a) Level 0: key_s(y, k) = (g(y, k)) for every s. Level l ≥ 1: wt(x, k) = 2(l − 1) + k (R110's wiring), so key_s(x, k) is
  key_s(2l − 2 + k, s(2l − 2 + k)) followed by g(x, k). The two prefixes are keys of options of the two distinct movers 2l − 2, 2l − 1 of
  one level; by (F1) they have equal length and differ, so they decide: key_s(x, 0) < key_s(x, 1) iff ord_(l−1)(s). So KP_s(x) = 0 iff
  ord_(l−1)(s), i.e. KP_s(x) = c_l(s). The last sentence follows. (b) By (F2), both options lie in A_(s_(t−1))(x) and the step gives x
  the one with the least key_(s_t)(x, ·), i.e. KP_(s_t)(x); since x moves, s_(t−1)(x) is the other option. (c) Both current options
  W-point to the same mover 2l − 2 + j, so the keys share the prefix and the gates g(2l, j), g(2l + 1, j) decide. ∎
- Does NOT claim: (a), (c) outside 𝓛^R_d; anything about A-sets in (a), (c); (b) at degree ≥ 3. (These are P-IDEAL-ALIGN's ALIGN (a),
  (c) and KP-MOVE (a), re-proved here because that packet is not landed; (a) is also R111 PAIR-KF's last clause read on 𝓛^R_d.)

## 2. Theorem PHIK-DESCENT and Corollary PHIK-T (PROVED)
- Hypotheses: G ∈ 𝓛^R_d (d ≥ 1); any run; t ∈ [1, T] any step; s := s_(t−1), s′ := s_t.
- Theorem PHIK-DESCENT. Φ_K(s′) ≤ Φ_K(s) − 1.
- Corollary PHIK-T. Every run from s_0 has T ≤ Φ_K(s_0) ≤ Σ_x w_lev(x) = 2 Σ_(l=0..d−1) (2^(d−l) − 1) = 2^(d+2) − 2d − 4. In
  particular a start with k_(s_0)(x) = 0 for every x has T = 0.
- Proof. For 0 ≤ l ≤ d − 1 put f_l := [ord_l(s′) ≠ ord_l(s)] (the level-l pair flips at step t), f_(−1) := 0, m_l := #(Mv_t ∩ {2l,
  2l + 1}), Δ_l := w_l Σ_(x ∈ {2l, 2l+1}) (k_(s′)(x) − k_s(x)), and S_l := Σ_(j=l..d−1) Δ_j (S_d := 0). So Φ_K(s′) − Φ_K(s) = S_0.
  - Per-level facts. For x of level l: KP_(s′)(x) = KP_s(x) iff f_(l−1) = 0 (KEY (a); at level 0 always). A non-moving x keeps s(x), so
    k_(s′)(x) = k_s(x) if f_(l−1) = 0 and k_(s′)(x) = 1 − k_s(x) if f_(l−1) = 1. A moving x has k_(s′)(x) = 0 and s(x) ≠ KP_(s′)(x)
    (KEY (b)); so k_s(x) = 1 if f_(l−1) = 0, and k_s(x) = 0 if f_(l−1) = 1 (then KP_(s′)(x) = 1 − KP_s(x) by KEY (a), and s(x) is the
    other option of x, i.e. KP_s(x)). By CASCADE: if f_l = 1, then m_l ≥ 1, or l ≥ 1 and f_(l−1) = 1 (on 𝓛^R_d two movers of one level
    on different options have the two distinct W-targets 2l − 2, 2l − 1).
  - Hence, with f := f_(l−1): (i) f = 0, m_l = 0: Δ_l = 0 and f_l = 0. (ii) f = 0, m_l ≥ 1: Δ_l = −m_l w_l ≤ −w_l. (iii) f = 1, m_l = 0:
    both k toggle; if k_s = 0 at both (then s(2l) = s(2l + 1) = c_l(s) =: j), Δ_l = +2w_l, and s′ = s at level l with both on j, so
    ord_l(s′) = γ_l(j) = ord_l(s) (KEY (c); case (iii) needs l ≥ 1, since f_(−1) = 0) and f_l = 0; if k_s = 1 at
    both, Δ_l = −2w_l; otherwise Δ_l = 0. (iv) f = 1, m_l = 1: the mover contributes 0, the other toggles: Δ_l = ±w_l. (v) f = 1, m_l =
    2: Δ_l = 0.
  - Claim: for 0 ≤ l ≤ d, S_l ≤ 0 if f_(l−1) = 0, S_l ≤ −1 if f_(l−1) = 0 and m_l ≥ 1 (l ≤ d − 1), and S_l ≤ 2w_l if f_(l−1) = 1. By
    downward induction (S_d = 0 = 2w_d). Since S_(l+1) ≤ 2w_(l+1) = w_l − 1 in every case: (i) S_l = S_(l+1) ≤ 0 (f_l = 0). (ii) S_l ≤
    −w_l + w_l − 1 = −1. (iii) S_l ≤ max(2w_l + 0, −2w_l + w_l − 1, 0 + w_l − 1) = 2w_l (the +2w_l case has f_l = 0). (iv) S_l ≤ w_l +
    w_l − 1 < 2w_l. (v) S_l ≤ w_l − 1 < 2w_l.
  - Step. Mv_t ≠ ∅; let l_0 be the least level with m_(l_0) ≥ 1. For l < l_0: m_l = 0, so by induction from l = 0 (f_(−1) = 0 and case
    (i)), f_l = 0 and Δ_l = 0. So S_0 = S_(l_0) with f_(l_0−1) = 0 and m_(l_0) ≥ 1: S_0 ≤ −1. ∎
  - Corollary: Φ_K ≥ 0 and falls by ≥ 1 per step, so T ≤ Φ_K(s_0) ≤ Σ_x w_lev(x) = 2 Σ_(l<d) (2^(d−l) − 1) = 2(2^(d+1) − 2) − 2d. ∎
- Does NOT claim: a polynomial bound (the bound is P-IDEAL-ALIGN's T-BOUND value, here as one potential); that Φ_K(s_0) is attained
  (DATA §6: never on the champions); anything outside 𝓛^R_d.

## 3. Theorem OPT-K (PROVED)
- Hypotheses: d ≥ 1; real numbers a and w_x (x = 0, …, 2d − 1), independent of the genome; Φ(G, s) := a + Σ_x w_x k_s(x) for G ∈
  𝓛^R_d and states s of G. Suppose Φ(G, s) − Φ(G, step(s)) ≥ 1 for every G ∈ 𝓛^R_d and every state s of G with step(s) defined.
- Then w_x ≥ 2^(d−lev(x)) − 1 for every x, and for every G ∈ 𝓛^R_d, max_s Φ(G, s) − min_s Φ(G, s) ≥ Σ_x w_x ≥ 2^(d+2) − 2d − 4.
  Φ_K (a = 0, w_x = w_lev(x)) attains equality in both (PHIK-DESCENT; its range on every G is exactly 2^(d+2) − 2d − 4, by the two
  extreme states below).
- Forcing genome τ(l, p) for 0 ≤ l ≤ d − 1 and p ∈ {2l, 2l + 1}, q := the other mover of level l (wiring of 𝓛^R_d):
  - Every Ξ-target is the exit X (so IDEAL-ACYC holds); every parity is even; Ξ_s(x, k) = {β(x, k)}, so the option of x with the larger
    rank is the better one at every state. A state s and the ranks are chosen as follows, the gates are distinct and otherwise free.
  - Levels < l: any options. Level l, l ≥ 1: s(q) := c_l(s), s(p) := 1 − c_l(s) (c_l(s) is fixed by the levels below). Level 0 (l = 0):
    gates with g(p, s(p)) > g(q, s(q)) > g(p, 1 − s(p)), and g(q, 1 − s(q)) > g(q, s(q)); then KP(p) = 1 − s(p) and KP(q) = s(q).
    For l ≥ 1 the gates of the level-l pair are chosen with γ_l(c_l(s)) ≠ ord_l(s) (ord_l(s) = [s(2l) = c_l(s)] is fixed by the levels
    below, by the proof of KEY (a): the two current options W-point to different lower movers).
  - Level l + 1 (if l ≤ d − 2): s(2l + 2) = s(2l + 3) := c_(l+1)(s) (fixed by levels ≤ l). Levels > l + 1: any options.
  - Ranks: at every x ≠ p the option s(x) gets the larger rank of x's two options; at p the option 1 − s(p) does.
- Lemma (the forcing step). In τ(l, p) from s: Mv_1 = {p}; k(p) goes 1 → 0; if l ≤ d − 2, both level-(l + 1) movers go k 0 → 1; every
  other k bit is unchanged.
  - Proof. A_s(x) = {s(x)} for x ≠ p (s(x) is Ξ-better) and A_s(p) = {0, 1}. So only p can move, and by the step rule and (F3) it takes
    KP_(s_1)(p) = KP_s(p) (levels < l are unchanged, and for l = 0 KP is constant), which is 1 − s(p) by construction: p moves, k(p): 1 → 0.
    At level l, q is unchanged, s_1(p) = s_1(q) = c_l(s) (l ≥ 1) and ord_l(s_1) = γ_l(c_l(s)) ≠ ord_l(s) (KEY (c)); at l = 0 the gate of
    p's new option is below g(q, s(q)) and the old one above, so ord_0 changes too. So f_l = 1 and KP at level l + 1 flips (KEY (a)): both
    level-(l + 1) movers, aligned and not moving, become misaligned; their options stay equal, so ord_(l+1) is unchanged (KEY (c)). Above
    l + 1, nothing moves and the pair below does not flip, so by CASCADE (inductively) no pair flips, and no KP changes (KEY (a)); below
    l and at q, nothing changes. ∎
- Proof of OPT-K. τ(l, p) with l ≤ d − 2 gives w_p − w_(2l+2) − w_(2l+3) ≥ 1, and τ(d − 1, p) gives w_p ≥ 1. With W_l := min(w_(2l),
  w_(2l+1)): W_(d−1) ≥ 1 and W_l ≥ 2W_(l+1) + 1, so W_l ≥ 2^(d−l) − 1 and every w_x > 0. In every G ∈ 𝓛^R_d the state with k = 1 at
  every mover exists (choose s(x) := 1 − KP_s(x) level by level, lowest first; KP_s(x) depends on lower levels only by (F3)), and so does
  the state with k = 0 everywhere; Φ differs between them by Σ_x w_x ≥ 2 Σ_l (2^(d−l) − 1) = 2^(d+2) − 2d − 4. ∎
- Does NOT claim: anything about potentials using other features (§5 for two classes); that the τ genomes have long runs (each has every
  Ξ-target X, so every mover moves at most once: after a move it is on its Ξ-better option); anything outside 𝓛^R_d.
- READING (not to sign): the exponential range is forced on genomes whose runs have T ≤ 2d; it measures what key bits cannot see (whether
  a misaligned mover will ever become Ξ-unhappy), not the length of runs.

## 4. Lemma RISE-EQUIV, Lemma MOVE-RISE, Corollary MOVE-RISE-R (PROVED; premises R105 ENC, MONO, XI-NEW, RISE)
- Hypotheses: G IDEAL-ACYC, any degree, any width; any run.
- RISE-EQUIV. (a) For every option (x, k) and t ∈ [1, T], v_(s_t)(x, k) ≥ v_(s_(t−1))(x, k); and R(x, k) = the number of rises of
  cv(xt(x, k)) if xt(x, k) is a mover, R(x, k) = 0 if it is X. (b) R(x, k) ≤ T. (c) T ≤ 1 + #{t ∈ [1, T − 1] : some option value rises at
  step t} ≤ 1 + Σ_(x,k) R(x, k). Hence T ≤ 1 + M · max_(x,k) R(x, k), and on any family of genomes and runs, max_(x,k) R(x, k) is bounded
  by a polynomial in N + M iff T is.
  - Proof. (a) By ENC, v_s(x, k) = ε(x, k) + cv_s(xt(x, k)) if the Ξ-target is a mover and ε(x, k) otherwise; by MONO (read through ENC's
    order-preserving integers), cv_s(z) never decreases along a run. (b) A value changes at most once per step. (c) If T ≥ 2: for every t
    ∈ [2, T], step t has a least-level mover h; by XI-NEW it moves to an option w, and by RISE «that option's value rose strictly at step
    t − 1». So every step t − 1 ∈ [1, T − 1] has a rising option value, and T − 1 ≤ #{t ≤ T − 1 with a rise} ≤ Σ R. If T ≤ 1 the
    inequality is trivial. ∎
- MOVE-RISE. If z ∈ Mv_t, then cv_(s_t)(z) > cv_(s_(t−1))(z).
  - Proof. By (F2), w := s_t(z) satisfies Ξ_(s_(t−1))(z, w) ▷ Ξ_(s_(t−1))(z, s_(t−1)(z)), i.e. v_(s_(t−1))(z, w) > cv_(s_(t−1))(z) (ENC).
    By RISE-EQUIV (a), cv_(s_t)(z) = v_(s_t)(z, w) ≥ v_(s_(t−1))(z, w). ∎
- Corollary MOVE-RISE-R. If xt(x, k) = z is a mover, then R(x, k) ≥ moves(z). (By RISE-EQUIV (a) and MOVE-RISE.)
- Does NOT claim: any bound on R (RISE-EQUIV only transfers bounds between R and T); CONJECTURE RISE-2D («on 𝓛^R_d every option rises at
  most 2d times in every run») or MOVES-2D; anything for Ξ-cyclic genomes.

## 5. Certificate items (CERTIFIED: machine, exact rational arithmetic; not hand proofs)
- Feature classes, for G ∈ 𝓛^R_d and a state s (x ranges over movers, l over levels; z_s(x) := [Ξ_s(x, 1 − s(x)) ▷ Ξ_s(x, s(x))];
  u := z·k; h(x) := the number of movers on the longest Ξ-path from x (1 + the largest h of a mover Ξ-target of x, with X counting 0);
  PV(x) := the sorted list of the integers (ENC) of the β-sets of the P(x) maximal Ξ-paths from x; ic(x), io(x) := the positions in PV(x) of
  cv_s(x) and of v_s(x, 1 − s(x)); P(x) := |PV(x)|):
  - BASE (in every class): z_s(x), k_s(x), u_s(x) for every x.
  - P: for every l, the indicator of each value of (k(2l), k(2l + 1), z(2l), z(2l + 1)) ∈ {0, 1}^4, and ord_l(s).
  - H: for every l and every height value η, #{x of level l : h(x) = η, z_s(x) = 1} and #{… : u_s(x) = 1}.
  - X: for l ≤ d − 2, a ∈ {2l, 2l + 1}, b ∈ {2l + 2, 2l + 3}: z(a)k(b) and k(a)z(b).
  - B: for every x, P(x) − 1 − ic(x) and (P(x) − 1 − ic(x)) / max(1, P(x) − 1); for every l, the sum of P(x) − 1 − ic(x) over level l.
  - G: for every x, io(x) − ic(x), max(0, io(x) − ic(x)), max(0, io(x) − ic(x)) / max(1, P(x) − 1), and k(x) · max(0, io(x) − ic(x)).
  - Class PHX := BASE + P + H + X. Class PBG := BASE + P + B + G. A class potential is Φ(G, s) := a + Σ_f w_f f(G, s) with real a, w_f,
    one weight per feature name (the names carry the mover / level / height / value index above), independent of G.
- Item C-PHX3. Every PHX potential Φ with Φ(G, s) − Φ(G, step(s)) ≥ 1 at every transition of every G ∈ 𝓛^R_3 satisfies
  sup_(G,s) Φ − inf_(G,s) Φ ≥ 22 (over G ∈ 𝓛^R_3 and their states). Since Φ_K is a PHX potential (a = 0, weight w_lev(x) on k(x), 0
  elsewhere) with range 22 on every G (PHIK-DESCENT, OPT-K), the least such range is exactly 22 = 2^(3+2) − 2·3 − 4.
- Item C-PBG. Every PBG potential with the same decrease property on 𝓛^R_d has sup − inf ≥ β_d with β_2 = 8, β_3 = 18.8596… (an exact
  rational with 67-digit numerator, printed by the tool) and β_4 = 35.5535… (an exact rational with 122-digit numerator, printed by the tool).
- Certificate. A certificate is a finite list of transitions (G_i, s_i → step(s_i)) with multipliers y_i ≥ 0 and two finite lists of
  states (G_j, s_j) with multipliers a_j ≥ 0, b_j ≥ 0 such that Σ_i y_i (f(G_i, s_i) − f(G_i, step(s_i))) + Σ_j a_j f(G_j, s_j) − Σ_j b_j
  f(G_j, s_j) = 0 for every feature f, Σ_j a_j = Σ_j b_j = 1. Then for every class potential with the decrease property, Σ_i y_i ≤ Σ_i
  y_i (Φ(s_i) − Φ(step(s_i))) = Σ_j b_j Φ(G_j, s_j) − Σ_j a_j Φ(G_j, s_j) ≤ sup Φ − inf Φ (the constant a cancels). The bound is Σ_i y_i.
- Machine premise: experiments/new/box182/risecheck.py (block CERT) re-checks the four certificates experiments/new/box182/cert/
  cert_PHX_d3_s1793.json, cert_PBG_d2_s179.json, cert_PBG_d3_s1793.json, cert_PBG_d4_s1794.json: it checks every genome is in 𝓛^R_d and
  Ξ-acyclic, recomputes every transition with the box150 simulator and every feature in exact rational arithmetic, re-solves the
  multipliers exactly on the certificate's support (Gaussian elimination over the rationals; the solution is unique, 0 free variables),
  and checks y, a, b ≥ 0 and the equalities. Output (one line per certificate): «bound 22.000000 (= 22) CERTIFIED», «bound 8.000000 (= 8) CERTIFIED», «bound 18.859681
  (= p/q) CERTIFIED» and «bound 35.553557 (= p/q) CERTIFIED», with the exact p/q printed in full. The certificates came from a floating-point LP (box179/lpot.py, HiGHS); only the
  exact re-check is the premise.
- Does NOT claim: that the PBG bounds grow exponentially in d (three values; READING §6); anything for d ≥ 5 or for other classes;
  anything about T (these are statements about potentials).

## 6. DATA, machine checks, excluded parts, TARGET diff (not to sign)
- Tool: experiments/new/box182/risecheck.py (deterministic, seed 182; simulator box150/check.py's Gen; no numpy / scipy). Output frozen
  in experiments/new/box182/risecheck.out and checked by block «P-IDEAL-RISE» of experiments/new/check.sh, which also pins the sha1s of
  this packet, its line L-1, the tool, its output and the four certificates.
- Scope and counts (each count covers ONLY the statement named; counter names as in the tool):
  - PHIK (PHIK-DESCENT): every state of 200 random 𝓛^R_d genomes (d 1-4; box162 rand_lr, seed 182) and every step of the stored-start runs
    of the 201 in-tree 𝓛^R_d genome files of experiments/new/box150 to box181: 14,384 steps, 0 violations, drop exactly 1 on 1,772.
  - OPTK (the forcing-step Lemma and the two extreme states): the τ(l, p) of §3 built by the tool for d = 1, …, 8, every l and both p:
    72 genomes, 0 failures. This is the machine-checked range d ≤ 8; the Theorem itself is proved for every d.
  - RISE_A, RISE_B, RISE_C (RISE-EQUIV (a), (b), (c)) and MOVERISE (MOVE-RISE): 401 runs (the 201 files and the 200 random genomes, stored
    starts), 1,968 moves; 0 violations each.
  - CERT: 4 certificates, all CERTIFIED (§5).
- Earlier DATA (box 179-181 logs; not re-run by the tool): Φ_K 0 violations on 38,902 transitions (box179/log/phik.txt); per-genome LP and
  the full LP table (docs/new/N5-LPOT-box179.md §0, §5b); value rises on 40 champion runs, max R ≤ 2d (box180/log/rises_champions.txt).
- EXCLUDED (not to sign): CONJECTURE RISE-2D and MOVES-2D; the PHX / PHXV / PHXVD / PHXVDBG lower bounds at d ≥ 4 (sampling-limited); the
  obstruction READINGs (free Ξ-renewal ping-pong; «a move spends one rank»); the «O(1) flips between rises» DEAD (box 181, DATA only);
  everything about the ALIGN 8-state automaton beyond Lemma KEY.
- READING (C-PBG): 8, 18.86, ≥ 35.55 against T^R(d) = 4, 8, 13 for d = 2, 3, 4: adding the value budget lowers the constant of the
  base-2 bound but, on three values, not its doubling.
- Diff against TARGET.md: no statement mentions a parity game, a winning region, an algorithm's running time or a complexity class. Each
  is about the step sequence of the IDEAL model of RESULTS R104's definition, or about potentials on it. None is an M4 or M3 claim, none
  bounds anything polynomially (PHIK-T is exponential; RISE-EQUIV is an equivalence), none is a gauntlet step. G-N5-TIME stays OPEN.
