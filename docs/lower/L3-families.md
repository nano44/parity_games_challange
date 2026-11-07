# L3: explicit families and obstructions for μ(d) on 2-wide ladders (L-LOWER successor 3, BOX L3, 2026-11-07)

Box: Lead BRIEF (L-LOWER successor 3, D1/D14/D18/D20), BOX L3 «EXPLICIT FAMILIES for μ(d), the per-mover move count in the
IDEAL-ACYC model». Labels: PROVED (lane, unrefereed) / CONJECTURE (with data) / DEAD (instance) / DATA. Nothing here is a result in
the sense of CLAUDE.md. Nothing here bounds T polynomially on 𝓛^R_d; MOVES-2D and G-N5-TIME stay OPEN. Not a TARGET.md claim: every
statement is about the step sequence of the IDEAL model only (diff in §8).

## 0. Premises (landed RESULTS only, plus one packet item «signed, not landed»), model, notation
- RESULTS R104 (P-N5-REALIZE): ONLY its definition of the IDEAL model (opened: docs/RESULTS.md l. 9864, «an IDEAL genome G has N
  movers x with levels lev(x), M := Σ deg(x) options (x, k), each with a W-target of level lev(x) − 1 (none at level 0), a Ξ-target
  xt(x, k), a mover or the exit X, a distinct β-rank with a parity, a distinct gate index, and a start; under a state s the Ξ-value of
  option (x, k) is the set of β's on its chain (x, k), (xt, s(xt)), … up to the first Ξ-target X, compared by the β of largest rank in
  the symmetric difference …; an IDEAL step moves every mover to the lexicographically least key (gate indices of the chain of
  W-targets under the new state, lowest level first) among its current option and the options with a strictly better Ξ-value, and the
  run stops when nothing is available or nothing changes»). As restated in P-IDEAL-MOVES §0: A_s(x) := {s(x)} ∪ {k : Ξ_s(x, k) ▷
  Ξ_s(x, s(x))}; s_t(x) := the option of A_(s_(t−1))(x) with the least key_(s_t)(x, ·), level by level, lowest level first.
- RESULTS R110: ONLY its definition of 𝓛^R_d («the 2-wide degree-2 ladders in L-RED's R197 convention (movers 2l and 2l + 1 on level
  l, all of degree 2, no other movers, option k of a mover of level l ≥ 1 W-pointing to mover 2(l − 1) + k)», levels 0, …, d − 1).
- RESULTS R113 (P-IDEAL-ALIGN), two items: «(ALIGN) on 𝓛^R_d, for 1 ≤ l ≤ d − 1 and every state s of a run, both movers 2l and 2l + 1
  have KP_s = c_l(s), each of them that moves at step t moves to option c_l(s_t), and the order of their keys under s is [s(2l) =
  c_l(s)] if s(2l) ≠ s(2l + 1) and γ_l(j) if both are on option j»; «(F0) on 𝓛^R_d each level-0 mover moves at most once and F(0) ≤
  2». Notation as in R113: KP_s(x), c_l(s), γ_l(j), F(l).
- Packet P-IDEAL-MOVES (L-NEW 57, claude/l-new d86adc86, signed by REFEREE and REFEREE-2 with W-1/W-2 required, NOT LANDED):
  «signed, not landed» Lemma AND-GATE (a): «For t ∈ [1, T]: x ∈ Mv_t iff s_(t−1)(x) ≠ π_(s_(t−1))(x) and π_(s_(t−1))(x) = KP_(s_t)(x).
  If x ∈ Mv_t then s_t(x) = π_(s_(t−1))(x) = KP_(s_t)(x).» Used only in §1 (the latch form, a reformulation used for intuition and for
  the family descriptions); no proof in §2-§5 uses it.
- Notation. T: number of steps; Mv_t: movers of step t; moves(x) := #{t ∈ [1, T] : x ∈ Mv_t}; Z: the Ξ-target movers; μ(d) as in
  P-IDEAL-MOVES §1 (the largest moves(z) over 𝓛^R_d, acyclic, all starts, z ∈ Z of level ≥ 1). cv_s(y) := the Ξ-value of y's current
  option under s. An option (x, k) is UPWARD if xt(x, k) is a mover y with lev(y) > lev(x), INNER if lev(y) = lev(x), DOWNWARD if
  lev(y) < lev(x). A genome is TRI if it has no upward option.

## 1. The latch form (PROVED from «signed, not landed» AND-GATE (a) and R113 ALIGN; a reformulation, not used in §2-§5)
- Statement. On 𝓛^R_d, for a mover x of level l ≥ 1 and t ∈ [1, T]: s_t(x) = c_l(s_t) if π_(s_(t−1))(x) = c_l(s_t), and s_t(x) =
  s_(t−1)(x) otherwise. For a level-0 mover, the same with c_l(s_t) replaced by the constant KP(x).
- Proof. If π_(s_(t−1))(x) = c_l(s_t) = KP_(s_t)(x) (ALIGN) and s_(t−1)(x) ≠ π, AND-GATE (a) moves x to π = c_l(s_t); if s_(t−1)(x) =
  π then x does not move and s_t(x) = π = c_l(s_t). If π ≠ c_l(s_t), AND-GATE (a) says x does not move. ∎
- Reading: every mover is a latch that copies the key signal c_l when its Ξ-preference agrees. With R113 ALIGN's key-order clause,
  c_(l+1)(s) = s(2l) ⊕ c_l(s) when s(2l) ≠ s(2l + 1) (the pair passes the signal through, flipped by s(2l)) and = 1 − γ_l(j) when both
  are on j (a constant). So the key side is a chain of 2-bit transducers driven from level 0; all the difficulty is the Ξ side.

## 2. Lemma TRI (PROVED; R104 definition only)
- Hypotheses: an IDEAL genome (any width, any degrees) whose Ξ-graph is acyclic and that is TRI (no upward option); levels 0, …, λ − 1.
  For a level L, D_L := the largest number of movers on a Ξ-path all of whose movers are on level L (D_L = 1 if level L has no inner
  option). For a run: T_L := the last step moving a mover of level < L (0 if none); T_0 := 0.
- Claim. T_(L+1) ≤ T_L + D_L for every L; hence T = T_λ ≤ D_0 + … + D_(λ−1) ≤ N. On 𝓛^R_d: D_L ≤ 2, so T ≤ 2d, and T ≤ d + (the number
  of levels with an inner option).
- Proof.
  - (i) Dependencies. Under TRI the Ξ-targets along a chain never rise in level, so the chain of an option of a level-L mover y visits,
    after (y, k), first movers of level L reached by inner options, then movers of levels < L. Its Ξ-value under s depends only on s at
    those movers. The key of (y, k) under s depends only on s at levels < L (W-targets are one level down). So A_(s_(t−1))(y) depends
    only on s_(t−1) at levels < L and at the level-L movers inner-reachable from y, and key_(s_t)(y, ·) only on s_t at levels < L.
  - (ii) For t ≥ T_L the states s_t agree on levels < L (no mover of level < L moves at a step > T_L). For a level-L mover y let e(y) :=
    the largest number of movers on a level-L Ξ-path starting at y (so e(y) ≤ D_L, and e(z) < e(y) for every z that y reaches by an
    inner option). Claim: y does not move at any step t > T_L + e(y). Induction on e(y). All level-L movers inner-reachable from y have
    e < e(y), so by induction they do not move after T_L + e(y) − 1: s_t agrees at them for all t ≥ T_L + e(y) − 1. By (i), for t ≥ T_L +
    e(y) the set A_(s_(t−1))(y) is the same set A* (t − 1 ≥ T_L + e(y) − 1), and the keys key_(s_t)(y, ·) are the same (t ≥ T_L), with
    distinct values (gate indices distinct). So s_t(y) = the key-least option of A*, the same option for every such t: y does not move
    at any step t ≥ T_L + e(y) + 1.
  - (iii) So no mover of level L moves after T_L + D_L, and T_(L+1) ≤ max(T_L, T_L + D_L). Every step moves some mover, so T = T_λ. ∎
- Does NOT claim: anything for genomes with an upward option (§4); that T ≤ 2d is attained (DATA §5: attained by family A for every
  tested d).

## 3. Corollary TRI-MU (PROVED; R104 definition, R113 ALIGN; §2)
- Hypotheses: G ∈ 𝓛^R_d, Ξ-acyclic, TRI; any start.
- Claim. moves(x) ≤ 1 for lev(x) = 0 and moves(x) ≤ 2·lev(x) for lev(x) ≥ 1. Hence every mover (Ξ-target or not) moves at most 2d − 2
  times (d ≥ 2): MOVES-2D holds on TRI genomes, with room 2, and «μ ≥ 2d» needs an upward option.
- Proof. Level 0: R113 F0. Level l ≥ 1: let t < t′ be consecutive moves of x. By ALIGN, s_t(x) = c_l(s_t) and s_(t′)(x) = c_l(s_(t′));
  x has degree 2 and keeps its option on [t, t′ − 1], so s_(t′)(x) ≠ s_t(x) and c_l(s_(t′)) ≠ c_l(s_t). c_l(s) is the key order of the
  pair (2l − 2, 2l − 1), a function of s at levels < l (keys depend only on lower levels), so some mover of level < l moves at a step of
  [t + 1, t′]. By §2, T_l ≤ 2l, so t′ ≤ 2l for every non-first move t′ of x, and the non-first moves of x lie in [2, 2l] (t ≥ 1 and t′ >
  t). So moves(x) ≤ 1 + (2l − 1) = 2l. ∎
- Does NOT claim: that 2l is attained (family A: 2⌊2l/3⌋ + 1 at the odd mover of level l, DATA).

## 4. Lemma FEEDBACK (PROVED; R104 definition; §2's argument)
- Hypotheses: an IDEAL genome with acyclic Ξ-graph, any width/degrees; any run. Up := the movers y that are the Ξ-target of an upward
  option. E := {t ∈ [1, T] : cv_(s_t)(y) ≠ cv_(s_(t−1))(y) for some y ∈ Up}. For a level l, Up_l := the Ξ-targets of the upward
  options of movers of level ≤ l, and E_l defined from Up_l the same way (E_l ⊆ E).
- (a) Every set [a, b] ⊆ [1, T] of consecutive steps with [a, b − 1] ∩ E = ∅ has b − a + 1 ≤ D_0 + … + D_(λ−1) ≤ N, D_L counted with
  inner options only. Hence T ≤ N·(1 + |E|); on 𝓛^R_d, T ≤ 2d(1 + |E|).
- (b) On 𝓛^R_d: on every [a, b] with [a, b − 1] ∩ E_l = ∅, no mover of level ≤ l moves after step a − 1 + 2(l + 1), and a mover of level
  l ≥ 1 moves at most 2l times in [a, b]. Hence moves(x) ≤ 2·lev(x)·(1 + |E_lev(x)|) for lev(x) ≥ 1, and μ(G) > 2d − 2 forces E_l ≠ ∅
  at the level l of the mover.
- Proof. (a) Cut the chain of an option of y at its first upward option (x′, k′) (its Ξ-target z ∈ Up): the β-set of the chain is
  the β's before z plus the β-set of z's current chain, and the order of two such sets is the order of the integers of RESULTS R105
  ENC — not needed: it suffices that the Ξ-value of (y, k) under s is a function of s at the movers before z on the chain (all of level
  ≤ lev(y), inner-reachable at level lev(y), as in §2 (i)) and of z's current chain's β-set Ξ_s(z, s(z)). For s ∈ {s_(a−1), …, s_(b−1)}
  these chain β-sets do not change for any z ∈ Up (no t ∈ [a, b − 1] is in E; a change of the set changes cv, a change of cv is a change
  of the set: cv_s(z) is the Ξ-value of z's current option, i.e. that set). Run §2 (ii)-(iii) on the steps a, …, b with T_0 := a − 1 and
  T_L := the last step of [a, b] moving a mover of level < L (a − 1 if none): every decision at a step t ∈ [a, b] reads s_(t−1) with
  t − 1 ∈ [a − 1, b − 1] and s_t, and the induction is word for word the same. So b ≤ T_λ ≤ a − 1 + Σ D_L. [1, T] is the union of at
  most |E| + 1 such sets (cut after every t ∈ E). (b) The first part is (a) for the levels ≤ l only: a chain from a mover of level ≤ l
  meets its first upward option at a mover of level ≤ l, so only Up_l matters. Second part: §3's argument on [a, b]: the non-first
  moves of x in [a, b] lie in [a + 1, a − 1 + 2l]. ∎
- Does NOT claim: any bound on |E| (it is at most the sum over Up of the numbers of rises of cv, which RESULTS R113 PATH-RISE bounds by
  P(y) − 1, exponential in general); that the intervals are long.
- Reading (the obstruction for compositions, §7): beating 2d − 2 moves needs a Ξ-target mover whose levels-≤-l subsystem is re-opened
  by a rise of an upward target after it has settled; one re-opening buys at most 2l more moves.

## 5. Family A (explicit, uniform, TRI; DATA, proof of the run: CONJECTURE A-RUN)
- Definition (explicit formula: experiments/lower/l3/genA.py; the same genomes as the template-search output
  experiments/lower/l3/fam/A_d<d>.json up to gate renumbering, same runs, checked d = 3..16). 𝓛^R_d, 4d options, for d ≥ 3:
  - Ξ-targets: (2l, 0) → 2l + 1 (inner), (2l, 1) → 2l − 1, (2l + 1, 0) → 2l − 2, (2l + 1, 1) → 2l − 4 (X if l = 1), for l ≥ 1;
    (0, 0) → X, (0, 1) → 1 (inner), (1, 0), (1, 1) → X. So A_d is TRI, with an inner option on every level.
  - Ranks: (2l, 0) has rank l − 1 (a low band, below everything else); with h(l) := (d − 1) + 3(d − 1 − l): (2l + 1, 0) → h(l),
    (2l, 1) → h(l) + 1, (2l + 1, 1) → h(l) + 2 (l ≥ 1); level 0: (0, 0) → 4(d − 1), (1, 1) → 4(d − 1) + 1, (0, 1) → 4(d − 1) + 2,
    (1, 0) → 4(d − 1) + 3. So the high band is ordered by level, level 0 highest (the Ξ order is decided lowest level first, like keys).
  - Parities: even for (2l + 1, ·) (l ≥ 1), (0, 1) and (1, 1); odd for (2l, ·) (l ≥ 1), (0, 0), (1, 0).
  - Gates: level 0: g(0, 0) = 2, g(0, 1) = 0, g(1, 0) = 3, g(1, 1) = 1; level l ≥ 1: g(2l, j) < g(2l + 1, j) for j = 0, 1 (γ_l(j) = 1).
  - Start: 00 at level 0, 11 at every level ≥ 1.
- DATA (own simulator sim.py, and L-NEW's box150 Gen with movescheck.py's counters via xcheck.py, 0 mismatches): T(A_d) = 2d and
  moves(2l + 1) = 2⌊2l/3⌋ + 1 for l ≥ 1, moves of every even mover and of both level-0 movers = 1, for d = 3, …, 40 from the stored
  start (l3check.py re-checks d = 3..20 at every verify). The run is regular: mover 1 moves at step 1, mover 0 at step 2, mover 2l
  (l ≥ 1) at step 2l + 2; the odd mover 2l + 1 moves at step 1 iff 3 | l and at a step t ∈ [2, 2l + 1] iff (l + t) mod 3 ≠ 0 (d = 10
  printed in notes/L-LOWER.md); so μ(A_d) = 2⌊2(d − 1)/3⌋ + 1 (3, 5, 5, 7, 9, 9, 11, 13, 13, 15, 17, 17, 19, 21 for d = 3..16). Every start for d = 3, 4
  (320 runs): movescheck counters 0.
- Status: the run is not yet proved for all d (CONJECTURE A-RUN: T(A_d) = 2d and μ(A_d) = 2⌊2(d − 1)/3⌋ + 1 for every d ≥ 3). If
  proved: an explicit TRI family meeting §2's T ≤ 2d with equality (so §2 is tight), and μ(d) ≥ 2⌊2(d − 1)/3⌋ + 1 for every d.

## 6. Searches (DATA; method distinct from L-RED's unrestricted SAT/climbs: uniform templates and lifts of the d = 5 witness)
- Simulator cross-check: experiments/lower/l3/sim.py (written from §0 only) vs L-NEW box150 Gen: 0 state-sequence mismatches on
  3,648 runs (every start of the box-186 instances dense_d5_D9, pass_d3_D3, pass_d4_D4, pass_d5_D5 and the box-187 instance m4_z4_r7,
  and L-RED's dense_d5_l3_H10 (μ 10)); movescheck.py counters RX, AGA, AGB, AGC, SWA-SWE, WPD all 0 on those runs.
- Uniform-template search (tsearch.c): every level ≥ L0 uses one of P local rules (Ξ-targets relative: down 1/2, inner, up 1/2, top pair,
  pairs 0/1; ranks by level bands; parities; γ bits; start bits). Best families found (from the template's start): A (μ ≈ 4d/3, TRI);
  slope-1 families (μ = d, T = d + 1); with upward/top-pair codes allowed, slope ≤ 1.6 up to d = 12 (μ(12) = 15 = A's). None reaches 2d
  at any d ≥ 6 tested (d ≤ 12).
- Lift search (lsearch.c): levels 0-4 fixed to L-RED's dense_d5_l3_H10 (μ 10 = 2d at d 5), one new top level from a template, with up to
  2 or 4 base options re-targeted to the new top pair (feedback): best μ(6) = 10 (no +1) in 2 × 2·10^7 candidates.
- Theorem-side consistency: tricheck.py (TRI, TRI-MU, FEEDBACK (a), (b) per level) 0 violations on 114,944 runs (the 220 𝓛^R genome
  JSONs under L-NEW's box150-187 (every start for N ≤ 10, the stored start otherwise), family A, the d = 5 witness, and 400 random
  𝓛^R_d genomes); 745 non-TRI runs have T > 2d (the hypothesis of §2 is needed).

## 7. Obstructions for compositions (goal (c))
- TOP-ADD (PROVED, from §2 (i)-(ii) applied to the new levels): if G′ ⊇ G adds k levels above G's top, no option of G Ξ-points into
  the new levels and no option of a new level is upward, then G's movers run exactly as in G (their A-sets and keys read only G's
  movers; once G's run has stopped they never move again), and from T(G) on the new levels settle within 2 steps per level (§2 (ii)
  with T_L := T(G) for the lowest new level): T(G′) ≤ T(G) + 2k and μ(G′) ≤ T(G′) ≤ T(G) + 2k. From the d = 5 witness (T 10) pure
  top-adds give at most T = μ = 2d (k = 1: the single new top level can have no upward option at all).
- TRI / FEEDBACK: «μ ≥ 2d» is impossible without an upward option (§3), and each extra 2l moves at level l needs one more step of E_l
  (§4 (b)). The d = 5 witness uses upward options at level 0 (movers 0, 1 Ξ-point to 8, 7, 6): its two level-0 moves re-open the levels
  above (c_1 changes at steps 4 and 6; the levels 1-3 repeat a 3-step cycle in steps 1-3 and 7-9).
- Substitution / Gray / Hanoi compositions (goal (b)): by §1 a Hanoi-type doubling needs F(l) ≈ 2F(l − 1) (key side, allowed by
  R113 PAIR-DOUBLE) and π alternating at every move of the pair below (Ξ side). With downward Ξ-options only, the Ξ order of a pair
  is a transducer chain like the key side and §2 gives T ≤ 2d; so the doubling needs |E| ≥ T/(2d) − 1 rises of upward targets (§4 (a)).
  No construction of such rises found (§6).

## 8. Diff against TARGET.md
No statement mentions a parity game, a winning region, an algorithm's running time or a complexity class; each is about the IDEAL
model's step sequence (R104's definition). §2-§4 bound T only on TRI genomes or in terms of |E|; nothing is polynomial on 𝓛^R_d.
Not M3, not a gauntlet step. G-N5-TIME stays OPEN; MOVES-2D stays OPEN.
