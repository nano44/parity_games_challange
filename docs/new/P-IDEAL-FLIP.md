# Packet P-IDEAL-FLIP (box 162): on R197-convention 2-wide ladders the bottom level acts on the levels above through one key bit b_0 (W-ONLY); with b_0 constant each level-1 mover moves once (NOW-ONCE); a flip of b_0 is a swap of the level-1 W-targets (SWAP); one level above an externally flipped bit makes at most 3 steps (FLIP-1); DEAD: the single-channel trade seg1 + tail ≤ T^R(d − 1)
L-NEW successor 53 (Opus 5.5), D14 / D18; Lead brief BOX 162 (2026-11-05): «freeze packet P-IDEAL-FLIP for the referees». Written
2026-11-05 (date -u: see the commit). FROZEN at push: later text goes into docs/new/P-IDEAL-FLIP-fixes.md (append-only). Sources:
docs/new/N5-SLOT-box160.md §1 and docs/new/N5-FLIPADD-box161.md §1 (successor 52). This packet governs: every proof is written out in
full here and is checked against this text only. Labels: PROVED (L-NEW 53, unrefereed) / DEAD / DATA / READING (not to sign). Not a
TARGET.md claim. Every statement is about the IDEAL-ACYC model only. No polynomial bound is claimed. FLIP-ADD, SLOT-TRADE and G-N5-TIME
stay OPEN.

## To sign, and what is not to sign
| § | statement | label | kind |
| --- | --- | --- | --- |
| §2 | Lemma W-ONLY (a)-(c) (class 𝓦_d) and Corollary W-ONLY (d) (𝓛^R_d, ISO): T ≤ T_2(d − 1) + 2 | PROVED | reduction to the external-flip model |
| §3 | Lemma NOW-ONCE (a) real runs, (b) forced runs (𝓛^R_d) | PROVED | per-stretch bound |
| §4 | Lemma SWAP (𝓛^R_d) and Corollary SWAP-RUN (ISO) | PROVED | structure of a flip |
| §5 | Proposition FLIP-1: T_0(1) = 2 and T_k(1) = 3 for every k ≥ 1 | PROVED (bounds by proof, values by two explicit instances) | exact one-level value |
| §6 | DEAD: the single-channel trade SC-ISO, instance iso_d4_st9 | DEAD (instance; one machine premise, listed) | refutation of a lane conjecture |
| §7 | DATA: T_k(m) table (m ≤ 3), machine checks, excluded parts, TARGET diff | DATA / READING (not to sign) | |

- Premises (LANDED only).
  - RESULTS R104 (P-N5-REALIZE): ONLY its definition of the IDEAL model and of the Ξ-graph, restated in §0. No theorem of R104 is used.
  - RESULTS R109 (P-IDEAL-SLOT): only SEG-ONCE at l = −1, quoted verbatim from the R109 statement: «(SEG, SEG-ONCE; restated in full
    from P-IDEAL-SEG) on an interval of steps without a move at levels ≤ l (l ≥ −1), freezing the movers of level ≤ l at their options
    at the state before the interval's first step (s_(a−1)) reproduces the interval, and at degree ≤ 2 every mover of level l + 1 moves
    at most once in it». Used in §2 (d) and §3 (c) only, with l = −1 and the interval = the whole run (no mover has level ≤ −1), for
    «each level-0 mover of a genome of degree ≤ 2 moves at most once in the whole run». R109's 𝓛_d and T*(d) are named in
    §1 and §4 only to keep them apart from 𝓛^R_d and T^R(d); no statement here uses a value or a bound of T*.
  - Not used: RESULTS R105 (so its Erratum E-2 does not bear on this packet), R106, R107, R108, docs/lit, docs/sources, any other
    lane file. No outside source is cited.
  - One machine premise, used ONLY by the DEAD item §6 and listed there as its gap: T^R(3) ≤ 8 (CaDiCaL UNSAT, §7).
- Each statement lists its hypotheses and a line «does NOT claim».

## 0. The model (RESULTS R104's definition, as restated in P-IDEAL-SLOT §0)
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
  without that step. T := the number of steps. Mv_t := {x : s_t(x) ≠ s_(t−1)(x)}.
- Two facts used below, immediate from the definition. (F1) Keys of two distinct options of the same level are tuples of the same
  length whose last entries are distinct gates, so they differ. (F2) If deg(x) = 2 and x ∈ Mv_t, then s_t(x) ∈ A_(s_(t−1))(x) \
  {s_(t−1)(x)}, so both options lie in A_(s_(t−1))(x), and s_t(x) is the one with the smaller key_(s_t)(x, ·).

## 1. Classes and the external-flip model (definitions)
- 𝓦_d (d ≥ 2): the IDEAL-ACYC genomes with levels 0, …, d − 1 whose level-0 movers are exactly two movers, named 0 and 1 (any degrees,
  any number of movers on the levels ≥ 1). U := the movers of level ≥ 1; s|U := the restriction of a state to U.
- 𝓛^R_d (d ≥ 1; L-RED's R197 convention): N = 2d movers 0, …, 2d − 1, lev(x) = ⌊x/2⌋, every mover of degree 2, and wt(x, k) = 2(lev(x)
  − 1) + k for lev(x) ≥ 1 (option k of a level-l mover W-points to the k-th mover of level l − 1); Ξ-data, β's, gates and start
  arbitrary. 𝓛^R_d ⊆ 𝓦_d for d ≥ 2. T^R(d) := the largest T over 𝓛^R_d and all starts.
  - KEEP APART: R109's 𝓛_d (two degree-2 movers per level with ANY W-targets one level down, degree-1 movers allowed) and T*(d) over
    𝓛_d. 𝓛^R_d ⊆ 𝓛_d, so T^R(d) ≤ T*(d); whether they are equal is not known and nothing here depends on it.
- ISO (a property of a genome of 𝓦_d): no option of any mover has Ξ-target 0 or 1.
- b_0(s) := 1 if g(0, s(0)) < g(1, s(1)), else 0. Since key_s(y, s(y)) = (g(y, s(y))) for y ∈ {0, 1}, b_0(s) = 1 iff the level-0
  mover 0 has the smaller key under s.
- The c-step. For c ∈ {0, 1} put κ^c_0 := 1 − c and κ^c_1 := c (so κ^c_0 < κ^c_1 iff c = 1). For G ∈ 𝓦_d and a state s, the state s′ =:
  Step^c_G(s) is: s′(y) := s(y) for y ∈ {0, 1}; for x ∈ U, level by level from level 1, s′(x) := the option in A_s(x) with the least
  key^c_(s′)(x, ·), where key^c_(s′)(x, k) := (κ^c_(wt(x, k)), g(x, k)) if lev(x) = 1, and key^c_(s′)(wt(x, k), s′(wt(x, k))) followed
  by g(x, k) if lev(x) ≥ 2. (F1) holds for key^c too, so the least option is unique.
- Forced run. Let m ≥ 1 and G ∈ 𝓛^R_(m+1) with ISO, a start s_0, L ≥ 0 and bits c_1, …, c_L. Put u_0 := s_0, u_t := Step^(c_t)_G(u_(t−1)).
  moves := #{t ∈ [1, L] : u_t|U ≠ u_(t−1)|U}; flips := #{t ∈ [2, L] : c_t ≠ c_(t−1)}.
- T_k(m) := the supremum of moves over all such G, s_0, L and c with flips ≤ k (a priori possibly ∞). T_k(m) is non-decreasing in k.
- seg1, tail (as in R109's SEG-CAP): for a run of a genome of 𝓦_d, a LEVEL-0 STEP is a step that moves mover 0 or 1; seg1 := the number
  of steps before the first level-0 step (T if none); tail := the number of steps after the last level-0 step (0 if none).

## 2. Lemma W-ONLY (PROVED)
- (a) [G ∈ 𝓦_d, d ≥ 2; no ISO needed] For every step t ∈ [1, T] of every run: s_t|U = Step^c_G(s_(t−1))|U with c := b_0(s_t).
- (b) [G ∈ 𝓦_d, ISO] For x ∈ U, every option k and states s, s̃ with s|U = s̃|U: Ξ_s(x, k) = Ξ_s̃(x, k), hence A_s(x) = A_s̃(x). So
  Step^c_G(s)|U is a function of s|U and c.
- (c) [G ∈ 𝓦_d, ISO, frozen form] Let q = (q(0), q(1)) be options of the movers 0, 1, and H_q the genome G in which 0 and 1 keep only the
  options q(0), q(1) (same W-target, Ξ-target, β, gate); identify a state of H_q with the state of G having q at 0 and 1. Then H_q is
  IDEAL-ACYC, and from every state s with s(0) = q(0), s(1) = q(1) the run of H_q is s, Step^c_G(s), Step^c_G(Step^c_G(s)), … with
  c := b_0(q), stopped at the first application of Step^c_G that changes nothing.
- (d) Corollary [G ∈ 𝓛^R_d, d ≥ 2, ISO]: T ≤ T_2(d − 1) + 2, for every start.
- Proof of (a). Fix t, write s := s_(t−1), s″ := s_t, c := b_0(s″), s′ := Step^c_G(s). Both s″(x) and s′(x), x ∈ U, are chosen from the
  same set A_s(x). Claim, by induction on l = 1, …, d − 1: s″ and s′ agree on level l, and for any two options o, o′ of movers of level
  l, key_(s″)(o) < key_(s″)(o′) iff key^c_(s′)(o) < key^c_(s′)(o′).
  - l = 1. Let o = (x, k), o′ = (x′, k′), w := wt(o), w′ := wt(o′) ∈ {0, 1}. key_(s″)(o) = (g(w, s″(w)), g(o)) and key^c_(s′)(o) =
    (κ^c_w, g(o)). If w = w′, both first entries tie in both systems and g(o) vs g(o′) decides in both. If w ≠ w′, say w = 0, w′ = 1:
    the first entries differ in both systems (distinct gates; κ^c_0 ≠ κ^c_1) and decide; key_(s″)(o) < key_(s″)(o′) iff g(0, s″(0)) <
    g(1, s″(1)) iff b_0(s″) = 1 iff c = 1 iff κ^c_0 < κ^c_1. So the two orders agree on level-1 options, and s″(x), s′(x) are the least
    of the same set A_s(x) in the same order: they agree on level 1.
  - l ≥ 2. key_(s″)(o) = key_(s″)(p) followed by g(o), with p := (wt(o), s″(wt(o))); key^c_(s′)(o) = key^c_(s′)(p) followed by g(o),
    with the same p since s″ and s′ agree on level l − 1. Same for o′ with p′. If p = p′, both prefixes tie and g(o) vs g(o′) decides in
    both. If p ≠ p′, the prefixes differ in both systems by (F1) and decide; their orders agree by the claim at l − 1. So the orders
    agree, and s″, s′ agree on level l as for l = 1. ∎
- Proof of (b). The chain of (x, k) visits (x, k) and then options (y_j, s(y_j)) with each y_j the Ξ-target of the previous option. By
  ISO no y_j is 0 or 1, so every y_j ∈ U, and s(y_j) = s̃(y_j). The chains are the same sequence of options, so the Ξ-values are equal,
  and so are the A-sets. key^c reads no option of 0 or 1. ∎
- Proof of (c). H_q is IDEAL-ACYC: its options are options of G (ranks and gates stay distinct, W-targets one level down) and its
  Ξ-graph is a subgraph of G's. For x ∈ U, A^(H_q)_s(x) = A^G_s(x) for every state s of H_q (by (b): the chains never pass 0 or 1).
  Movers 0, 1 have A-sets {q(0)}, {q(1)} in H_q. H_q ∈ 𝓦_d, and every state of H_q has b_0 = b_0(q) = c. So whenever H_q steps from s,
  its new state is Step^c_G(s) on U by (a) (applied to H_q, whose A-sets on U and keys are those of G at states with q at 0 and 1), and
  q at 0, 1. Stop rule: if every A-set is a singleton, Step^c_G(s) = s (each x ∈ U picks from {s(x)}); if not, H_q's new state is
  Step^c_G(s), and H_q stops exactly when that equals s. ∎
- Proof of (d). Let c_t := b_0(s_t) for t ∈ [1, T], and u_t the forced run of G from s_0 under c_1, …, c_T (G ∈ 𝓛^R_d = 𝓛^R_((d−1)+1)).
  By induction u_t|U = s_t|U: u_t|U = Step^(c_t)(u_(t−1))|U = Step^(c_t)(s_(t−1))|U by (b), = s_t|U by (a). So moves = #{t : s_t|U ≠
  s_(t−1)|U}. b_0(s_t) depends only on s_t(0), s_t(1), so c changes only at a step that moves 0 or 1. Every mover of G has degree 2, so
  by RESULTS R109 SEG-ONCE (l = −1) each of 0, 1 moves at most once in the run: at most 2 steps move a level-0 mover. Hence flips ≤ 2,
  so moves ≤ T_2(d − 1); and every step not counted in moves moves only level-0 movers, at most 2 of them. So T ≤ T_2(d − 1) + 2. ∎
- Does NOT claim: anything without ISO in (b)-(d); any bound on T_2; that T_2(d − 1) + 2 is reached; anything about b_0's own dynamics.

## 3. Lemma NOW-ONCE (PROVED)
- For G ∈ 𝓛^R_d (d ≥ 2) and a level-1 mover x: under key_s, x's option k has key (g(k, s(k)), g(x, k)); the first entries differ, so
  x's key-smaller option is KP_s(x) = 0 iff b_0(s) = 1. Under key^c, option k has key (κ^c_k, g(x, k)), so the key^c-smaller option is
  KP^c(x) = 0 iff c = 1.
- (a) [real runs, no ISO needed] If [a, b] ⊆ [1, T] and b_0(s_t) is the same for all t ∈ [a, b], every level-1 mover moves at most once
  in [a, b].
- (b) [forced runs, ISO] If c_t is the same for all t ∈ [a, b] ⊆ [1, L], every level-1 mover x has u_t(x) ≠ u_(t−1)(x) for at most one
  t ∈ [a, b].
- (c) Corollary [real runs]: if b_0(s_t) is the same for all t ∈ [1, T], each of the four movers of levels 0 and 1 moves at most once
  in the run (levels 0: RESULTS R109 SEG-ONCE, l = −1; level 1: (a) with [a, b] = [1, T]).
- Proof of (a). Suppose x moves at t1 < t2 in [a, b] and not in between. By (F2), s_(t1)(x) = KP_(s_(t1))(x) and s_(t2)(x) = KP_(s_(t2))(x),
  and s_(t2)(x) ≠ s_(t1)(x) (degree 2: x returns to the option it left). But KP_(s_(t1))(x) = KP_(s_(t2))(x) since b_0(s_(t1)) =
  b_0(s_(t2)). Contradiction. ∎
- Proof of (b). If x changes at frame t, its new option lies in A_(u_(t−1))(x) and differs from u_(t−1)(x); with degree 2 both options
  lie in that A-set, and the new option is the key^c-least, KP^(c_t)(x). Two consecutive changes at t1 < t2 in [a, b] would give
  u_(t2)(x) = KP^(c_(t2))(x) = KP^(c_(t1))(x) = u_(t1)(x), against u_(t2)(x) ≠ u_(t1)(x). ∎
- Does NOT claim: any bound on movers of level ≥ 2 in such an interval.

## 4. Lemma SWAP and Corollary SWAP-RUN (PROVED)
- Definition. For G ∈ 𝓛^R_d (d ≥ 2), G^swap is G with the W-targets of the two options of every level-1 mover exchanged: option k now
  W-points to mover 1 − k; its gate, Ξ-target and β, and every other field and the start are unchanged. G^swap is IDEAL-ACYC (W-targets
  still one level down, Ξ-data unchanged) and lies in 𝓦_d (also in R109's 𝓛_d), but not in 𝓛^R_d. G is ISO iff G^swap is.
- Lemma SWAP. For every state s and c ∈ {0, 1}: Step^(1−c)_G(s) = Step^c_(G^swap)(s).
- Proof. The Ξ-data are equal, so all A-sets are equal. Level-1 option (x, k): in G^swap, key^c(x, k) = (κ^c_(1−k), g(x, k)), and
  κ^c_(1−k) = κ^(1−c)_k (k = 0: κ^c_1 = c = 1 − (1 − c) = κ^(1−c)_0; k = 1: κ^c_0 = 1 − c = κ^(1−c)_1). So every level-1 key^c in
  G^swap equals the key^(1−c) of the same option in G; both steps choose the same options at level 1. At levels ≥ 2 the W-targets are
  the same in both genomes, so by induction on the level the keys, built from the same level-below options, are equal, and the same
  options are chosen. Levels 0 are kept in both. ∎
- Corollary SWAP-RUN (ISO). Let u_0, …, u_L be a forced run with flips ≤ k, and c* := c_1. Cut [1, L] into the maximal blocks of
  constant c (at most k + 1 blocks). In a block with c = c*, u_t = Step^(c*)_G(u_(t−1)); in a block with c = 1 − c*,
  u_t = Step^(c*)_(G^swap)(u_(t−1)) (SWAP). Fix any level-0 options q with b_0(q) = c* (b_0 is computed from the gates of 0, 1, which
  G and G^swap share). Setting the options of 0, 1 to q changes no c-step on U (W-ONLY (b)). By W-ONLY (c), applied to G and to G^swap
  (both in 𝓦_d, both ISO), each block [a, b] is a prefix of the run of the IDEAL genome H_q (resp. (G^swap)_q) from u_(a−1) (with q at
  0, 1), followed by frames that change nothing once that run has stopped.
  So a forced run with k flips is a concatenation of at most k + 1 runs of two FIXED genomes, H_q and (G^swap)_q, each started where the
  previous one was cut, and moves = the sum of the lengths of the pieces. ∎
  - If no q with b_0(q) = c* exists (b_0 is constant on all four level-0 configurations), the block statements still hold for the
    c-steps; only the reading «run of an IDEAL genome» needs such a q.
- Does NOT claim: any bound. The two genomes are in 𝓛_d, so T* (not T^R) caps each piece; no bound on T* is used or claimed.

## 5. Proposition FLIP-1 (PROVED): T_0(1) = 2 and T_k(1) = 3 for every k ≥ 1
- Upper bounds. Let G ∈ 𝓛^R_2 with ISO and u_0, …, u_L a forced run. U = {2, 3}, the two level-1 movers.
  - By ISO and since there are no levels ≥ 2, every Ξ-target of an option of 2 or 3 is X, 2 or 3; not its own mover (acyclic), and not
    both 2 → 3 and 3 → 2. Call v ∈ {2, 3} a mover none of whose options points to the other one, u the other: both options of v have
    Ξ-target X.
  - v: Ξ(v, 0) = {β(v, 0)}, Ξ(v, 1) = {β(v, 1)} for every state; one of them is strictly better, always the same. A change of v at
    frame t takes an option of A_(u_(t−1))(v) other than u_(t−1)(v), which is strictly better: v goes from the worse to the better
    option, after which its A-set is a singleton forever. So v changes at most once.
  - u: each Ξ(u, k) is {β(u, k)} or {β(u, k)} ∪ Ξ(v, ·) at v's current option, so it depends only on v's option; the two values always
    differ (β(u, k) lies on the chain of (u, k) and not on the chain of (u, 1 − k)), so exactly one option, better(u_(t)(v)), is
    strictly better. A change of u at frame t moves it to better(u_(t−1)(v)). If u changes at t1 < t2 and not in between, it moves to
    better(u_(t1−1)(v)) at t1 and away from it, to better(u_(t2−1)(v)), at t2; so v changed at some frame in [t1, t2 − 1]. Three changes
    of u would need two changes of v in disjoint frame sets. So u changes at most twice.
  - Every counted frame changes u or v: moves ≤ 1 + 2 = 3, whatever c is (the flips touch no Ξ-value; W-ONLY (b)). So T_k(1) ≤ 3.
  - k = 0: c is constant, so by NOW-ONCE (b) each of 2, 3 changes at most once: moves ≤ 2. So T_0(1) ≤ 2.
- Lower bounds: two explicit instances of 𝓛^R_2, ISO (option fields: W-target, Ξ-target, gate, β rank, β parity (0 = even); X = exit).
  - I-0 (experiments/new/box162/out/kf0_d2_t2.json): mover 0: (−, X, 0, 7, odd), (−, X, 2, 6, odd); mover 1: (−, X, 3, 5, odd),
    (−, X, 1, 4, odd); mover 2: (0, X, 2005, 2, odd), (1, 3, 2006, 0, odd); mover 3: (0, X, 2004, 3, odd), (1, X, 2007, 1, odd); start
    (0, 0) on (2, 3); c ≡ 0. Frame 1: Ξ(3, 0) = {r3 odd} is worse than {r1 odd}, A(3) = {0, 1}, KP^0 = option 1 (W-target 1, κ^0_1 = 0
    < 1): 3 → 1; A(2) = {0} (Ξ(2, 1) = {r0, r3} has r3 odd: worse). Frame 2: now Ξ(2, 1) = {r0, r1} vs {r2}: largest r2 odd lies in
    Ξ(2, 0), so option 1 is better; A(2) = {0, 1}, KP^0 = 1: 2 → 1. Frame 3: both A-sets singletons. moves = 2, flips = 0: T_0(1) ≥ 2.
  - I-1 (experiments/new/box162/out/kf1_d2_t3.json): mover 0: (−, X, 1, 7, even), (−, X, 3, 6, even); mover 1: (−, X, 2, 5, even),
    (−, X, 0, 4, even); mover 2: (0, X, 2004, 3, even), (1, X, 2007, 0, odd); mover 3: (0, 2, 2005, 2, odd), (1, X, 2006, 1, odd);
    start (1, 0) on (2, 3); c = (0, 1, 1) (one flip). Option 0 of 2 is always better. Ξ(3, 0) vs Ξ(3, 1) = {r1 odd}: with 2 at 1,
    {r2, r0} (largest r2 odd: worse); with 2 at 0, {r2, r3} (largest r3 even: better). Frame 1 (c = 0, KP^0 = option 1): A(2) = {1, 0}
    → 2 stays at 1; A(3) = {0, 1} → 3 → 1. Frame 2 (c = 1, KP^1 = option 0): 2 → 0; A(3) = {1}. Frame 3 (c = 1): A(2) = {0};
    A(3) = {1, 0} (2 is at 0) → 3 → 0. moves = 3, flips = 1: T_1(1) ≥ 3, so T_k(1) ≥ 3 for k ≥ 1 (monotone in k).
- Does NOT claim: anything for m ≥ 2.

## 6. DEAD: the single-channel trade SC-ISO (instance iso_d4_st9)
- The statement killed. CONJECTURE SC-ISO (lane, box 160 §0 READING: «The single-channel trade «seg1 + tail ≤ T^R(d − 1)» is EXACT at
  d = 3 for both channels»; the W-channel form): «for every d ≥ 3, in every run of every ISO genome of 𝓛^R_d, seg1 + tail ≤ T^R(d − 1)».
- Instance: experiments/new/box160/out/iso_d4_st9.json (sha1 in §7), a genome of 𝓛^R_4 with ISO (option fields: W-target, Ξ-target,
  gate, β rank, β parity):
  - mover 0: (−, 3, 0, 8, odd), (−, X, 2, 11, even); mover 1: (−, 3, 1, 9, odd), (−, X, 3, 4, odd);
  - mover 2: (0, 5, 2005, 10, even), (1, X, 2006, 14, odd); mover 3: (0, 6, 2004, 5, odd), (1, 2, 2007, 12, even);
  - mover 4: (2, 2, 2008, 13, even), (3, 5, 2011, 0, odd); mover 5: (2, X, 2009, 15, odd), (3, X, 2010, 7, even);
  - mover 6: (4, 7, 2012, 3, even), (5, 2, 2015, 1, even); mover 7: (4, 4, 2013, 2, even), (5, 5, 2014, 6, even);
  - start 11111011 (movers 0..7). The Ξ-graph is acyclic (topological order 1, 0, 3, 6, 7, 4, 2, 5); no Ξ-target is 0 or 1 (ISO).
  - Run (box 150 simulator, and L-RED's r187/ideal.py: same states): 11111011, 11110011, 11110010, 11110000, 11100100, 11001101,
    11001111, 10011111, 00010111, 00010110, 00010100, 00000100. T = 11; mover 1 moves at step 7, mover 0 at step 8, no other step moves
    0 or 1. So seg1 = 6, tail = 3, seg1 + tail = 9.
- Machine premise (the gap of this item): T^R(3) ≤ 8, CaDiCaL UNSAT of «some genome of 𝓛^R_3 and start with T ≥ 9» (box160/iso.py
  d 3 t 9, 14 s; L-RED's xcnf.py encoding, claude/l-red 5f3e89e1, read-only; not Lean, not refereed). With it, 9 > 8 ≥ T^R(3) and
  SC-ISO is DEAD at d = 4. Without it, the instance proves: SC-ISO at d = 4 implies T^R(3) ≥ 9.
- Does NOT claim: anything about the NOW channel at d = 4 (UNKNOWN; box 160 §0); anything about SLOT-TRADE or FLIP-ADD (both OPEN); that
  seg1 + tail can exceed T^R(d − 1) by more than 1.

## 7. DATA, machine checks, excluded parts, TARGET diff (not to sign)
- DATA: T_k(m) (EXACT = CaDiCaL via pysat on L-RED's xcnf.py with one added line (experiments/new/box160/xcnf_free0.py), driver
  box160/iso.py FREE0=1 ISO=1 KF=k at d = m + 1; logs experiments/new/box162/log/kf<k>_d<d>_t<t>.log; witnesses box162/out/; every SAT
  witness re-evaluated by box162/flipcheck.py, which computes the exact per-genome maximum V_k(G, s_0) of the §1 definition by search).
  Each count covers ONLY the statement «T_k(m) ≥ t» (SAT) or «T_k(m) ≤ t − 1» (UNSAT at t) on 𝓛^R_(m+1) with ISO:
  - m = 1: T_0 ≥ 2 SAT, ≥ 3 UNSAT; T_1, T_2, T_3, T_6: ≥ 3 SAT, ≥ 4 UNSAT (all < 1 s). Agrees with §5 (PROVED).
  - m = 2: T_0 = 4 (≥ 5 UNSAT 3.9 s), T_1 = 5 (≥ 6 UNSAT 88 s), T_2 = 7, T_3 = 8, T_4 = 8, T_8 = 9 (UNSAT times: see §7 table below).
  - m = 3: T_0(3) see table; T_1(3) ≥ 10 (box160/out/kf1_d4_t10.json, V_1 = 10; T_1(3) ≥ 11 UNKNOWN); T_2(3) ≥ 12
    (box160/out/ISO_1_d4_t12.json, V_2 = 12).
  - TABLE-PLACEHOLDER
  - Encoding vs definition (READING, not signed): the SAT model has free level-0 options q_t and a free order of the four level-0 gates,
    c_t = b_0(q_t), flips counted over q_0, …, q_L, and every frame must change U. These give the §1 supremum: q_0 can copy q_1; every bit
    sequence is some b_0(q_t) under the gate order g(0, 0) < g(1, 0) < g(1, 1) < g(0, 1) (b_0 = 1 iff q_t(0) = 0); deleting a frame that
    changes nothing leaves the later u_t and does not add flips. By W-ONLY (b) the level-0 options play no other role under ISO.
- T^R values (EXACT, same encoding, 𝓛^R only): T^R(2) = 4, T^R(3) = 8 (box160/iso.py d 3: T ≥ 8 SAT 13 s, T ≥ 9 UNSAT 14 s, re-run
  2026-11-05; L-RED R197), T^R(4) = 13 (L-RED R197 / R202, not re-run). T* over 𝓛_d: no value used.
- Machine checks (experiments/new/box162/flipcheck.py; block «P-IDEAL-FLIP» of experiments/new/check.sh, which also pins the sha1s of
  this packet, its line L-1, the instance and the two FLIP-1 instances):
  - 300 random 𝓛^R_d genomes (d = 2, 3, 4; 3 of 4 ISO) + every 𝓛^R genome in box160/out and box162/out, every start for d ≤ 4:
    WONLY (§2 (a)), ISOA (§2 (b)), FROZ (§2 (c)), CONS (§2 (d): b_0 changes ≤ 2 and moves ≤ V_2), SWAP (§4), NOWONCE (§3 (a)), FLIP1
    (§5 bounds, every start of every d = 2 ISO genome, k ≤ 6): 0 violations. Controls: SWAPNEG (G^swap at the SAME c) and NOWCTRL
    (level-1 movers moving twice somewhere) are nonzero; NEG=1 (c-step ignoring c) makes WONLY, FROZ, CONS and SWAP fire.
  - INST: iso_d4_st9 is in 𝓛^R_4, ISO, T 11, level-0 steps [7, 8], seg1 6, tail 3.
- EXCLUDED (not to sign): CONJECTURE FLIP-ADD (T_2(m) ≤ T^R(m) + O(m)); CONJECTURE SLOT-TRADE; every READING and every other DATA row
  of docs/new/N5-SLOT-box160.md and docs/new/N5-FLIPADD-box161.md (NOW / NOL0 / FRZ tables, adversarial level 0, jumps, potential
  probe Ψ).
- Diff against TARGET.md: no statement mentions a parity game, a winning region, an algorithm's running time or a complexity class. Each
  is about the step sequence of the IDEAL model of RESULTS R104's definition (or the forced run defined from it, §1). None is an M4 or M3
  claim, none bounds anything polynomially, none is a gauntlet step. G-N5-TIME stays OPEN.
- READING (value): W-ONLY + SWAP turn the W-channel part of SLOT-TRADE into a question about TWO fixed genomes alternating at most
  three times (k = 2): FLIP-ADD asks that such an alternation adds only O(m) steps to T^R(m). FLIP-1 settles m = 1 (+1 per flip, at most
  +1 in total); the DATA show the gain T_k(m) − T_0(m) = 1, 3 at k = 1, 2 for m = 2 and ≥ 2, ≥ 4 for m = 3.
