# Packet P-IDEAL-SLOT (box 158): one level less (SHIFT), segment caps (SEG-CAP), one level more (LIFT); T*(d−1) ≤ T*(d) ≤ 3 T*(d−1) + 2 and max seg1 = T*(d−1) on 2-wide degree-2 ladders; DEAD: the linear first-segment bound SEG1-2D
L-NEW successor 51 (Opus 5.5), D14 / D18; Lead 2026-11-04 12:46Z: «Freeze P-IDEAL-SLOT as a short packet with line L-1, same form as
before». Written 2026-11-04 (date -u: see the commit). FROZEN at push: later text goes into docs/new/P-IDEAL-SLOT-fixes.md
(append-only). Source: docs/new/N5-SLOT-box158.md §1 (box 158). This packet governs: every proof below is written out in full here and
is checked against this text only. Labels: PROVED (L-NEW 51, unrefereed) / DEAD / DATA / READING (not to sign). Not a TARGET.md claim.
Every statement is about the IDEAL-ACYC model only. No polynomial bound is claimed anywhere. G-N5-TIME stays OPEN.

## To sign, and what is not to sign
| § | statement | label | kind |
| --- | --- | --- | --- |
| §1-§2 | Lemma SEG, Lemma SEG-ONCE: carried verbatim from P-IDEAL-SEG §1-§2 (frozen 8291ecf7, sha1 7fa84784; not yet landed), so this packet does not depend on that packet's landing | PROVED (copy; sign as in P-IDEAL-SEG) | restriction / per-stretch bound |
| §3 | Lemma SHIFT (any degree) | PROVED | one level less |
| §4 | Corollary SEG-CAP (𝓛_d) | PROVED | segment caps |
| §5 | Lemma LIFT (any degree) and Corollary SANDWICH: T*(d − 1) ≤ T*(d) ≤ 3 T*(d − 1) + 2, max seg1 over 𝓛_d = T*(d − 1) | PROVED | one level more; two-sided recursion |
| §6 | DEAD: SEG1-2D (lane), instance lift_max_d4_L13 | DEAD (instance) | refutation of a lane conjecture |
| §7 | machine check, excluded parts, TARGET diff | DATA / READING (not to sign) | |

- Premises (LANDED only).
  - RESULTS R104 (P-N5-REALIZE): ONLY its definition of the IDEAL model and of the Ξ-graph, restated in §0. No theorem of R104 is used.
  - RESULTS R105 (P-IDEAL-RED): only item LOCAL, key half, quoted verbatim from the R105 statement («a key only on the states below its
    level»). U, CHAIN-BACK and the CHAINED binder (R105 Erratum E-2) are not used.
  - Not used: RESULTS R106, R107, docs/lit, docs/sources, any other lane file. No outside source is cited. P-IDEAL-SEG is NOT a
    premise: its §0-§2 are copied below.
- Each statement lists its hypotheses and a line «does NOT claim».

## 0. The model (RESULTS R104's definition)
- A genome G has N ≥ 1 movers x, each with a level lev(x) ∈ {0, 1, …} and deg(x) ≥ 1 options (x, k); M := Σ deg(x). Each option has a
  W-target wt(x, k) (a mover of level lev(x) − 1; none at level 0), a Ξ-target xt(x, k) (a mover or the exit X), a β with a rank
  (distinct over all options) and a parity, and a gate index g(x, k) (distinct over all options). There is a start s_0. A state s picks
  one option s(x) per mover.
- Ξ-graph: an edge x → xt(x, k) for every option whose Ξ-target is a mover. IDEAL-ACYC: it is acyclic.
- Under s, the chain of (x, k) is (x, k), (y_1, s(y_1)), (y_2, s(y_2)), … with y_1 = xt(x, k), y_(j+1) = xt(y_j, s(y_j)), up to the
  first option whose Ξ-target is X. Its Ξ-value Ξ_s(x, k) is the set of β's on it. Two sets P ≠ Q are compared by the β of largest
  rank in P △ Q: the set containing it is better (P ▷ Q) if that β's parity is even, worse if odd.
- A_s(x) := {s(x)} ∪ {k : Ξ_s(x, k) ▷ Ξ_s(x, s(x))}.
- key_s(x, k) := (g(x, k)) if lev(x) = 0, else key_s(wt(x, k), s(wt(x, k))) followed by g(x, k); compared lexicographically.
- Step. If every A_(s_(t−1))(x) is a singleton, the run stops. Otherwise s_t is defined level by level, lowest level first:
  s_t(x) := the option in A_(s_(t−1))(x) with the least key_(s_t)(x, ·) (keys under the NEW state). If s_t = s_(t−1), the run stops
  without that step. T := the number of steps.
- Mv_t := {x : s_t(x) ≠ s_(t−1)(x)} (nonempty for t ∈ [1, T]). A mover of degree 1 has A_s(x) = {s(x)} always and never moves.
- At degree ≤ 2, for deg(x) = 2 and a state s, KP_s(x) := the option of x with the smaller key_s(x, ·) (keys of distinct options differ
  in the last entry). If x ∈ Mv_t, both options lie in A_(s_(t−1))(x), and the step rule gives s_t(x) = KP_(s_t)(x).
- d-level 2-wide ladder: a genome with levels 0, …, d − 1, exactly two movers per level, all of degree 2 (N = 2d).
- No width hypothesis is made in §1-§3: every level may hold any number of movers.

## 1. Lemma SEG (carried verbatim from P-IDEAL-SEG §1)
- Statement (IDEAL-ACYC, any degree, any width).
  - Let l ≥ −1, and let [a, b] ⊆ [1, T] be an interval of steps such that Mv_t contains no mover of level ≤ l for every t ∈ [a, b].
  - Let H be the genome G in which every mover x of level ≤ l keeps only the option s_(a−1)(x), with the same W-target, Ξ-target, β
    and gate. Identify a state of H with the state of G that has s_(a−1)(x) at every such x.
  - Then the run of H from s_(a−1) has s_(a−1), s_a, …, s_b as its first b − a + 2 states (so H takes at least b − a + 1 steps).
- Proof.
  - H is an IDEAL genome: each option of H is an option of G, so ranks and gates stay distinct, W-targets still lie one level down,
    and the Ξ-graph of H is a subgraph of G's, hence acyclic.
  - Induction on t ∈ [a, b]. Assume H is at s := s_(t−1) (true for t = a). Every frozen mover is at its frozen option in s, since no
    step in [a, t − 1] moved it.
  - (i) Values. Let x be non-frozen and k an option of x. The chain of (x, k) under s is the same sequence of options in H and in G:
    each frozen mover y on it contributes (y, s(y)), which is its only H-option. So Ξ^H_s(x, k) = Ξ^G_s(x, k), and A^H_s(x) = A^G_s(x).
  - (ii) For a frozen mover, A^H_s is a singleton.
  - (iii) New state. Let s′ := s_t. The frozen movers satisfy s′(y) = s(y), since t ∈ [a, b]. Go level by level from level 0, and assume
    H's new state agrees with s′ below lev(x).
    - The keys of x's options under the two new states are then equal: RESULTS R105 (LOCAL), «a key only on the states below its
      level».
    - A frozen x keeps its only option, which is s′(x).
    - A non-frozen x takes the key-least option of the same set A_s(x) under the same keys, which is s′(x).
    - So H's new state is s′.
  - (iv) Stop rule. G performs step t, so s′ ≠ s. Then some non-frozen mover has |A^G_s| ≥ 2, so |A^H_s| ≥ 2 by (i), and H does not stop
    at the singleton test. H's new state is s′ ≠ s, so H does not stop at the no-change test either. ∎
- Does NOT claim: anything about H's run after state s_b; any count bound.

## 2. Lemma SEG-ONCE (carried verbatim from P-IDEAL-SEG §2)
- Statement (IDEAL-ACYC, degree ≤ 2, any width). With l and [a, b] as in SEG: every mover x of level l + 1 satisfies
  |{t ∈ [a, b] : x ∈ Mv_t}| ≤ 1. In particular (l = −1, [a, b] = [1, T]) every level-0 mover moves at most once in the whole run.
- Proof.
  - Suppose x moves at t1 < t2 in [a, b] and not in between. Then deg(x) = 2: x goes from b′ to a′ at t1 and from a′ back to b′ at
    t2, with {a′, b′} its two options.
  - By §0, a′ = s_(t1)(x) = KP_(s_(t1))(x) and b′ = s_(t2)(x) = KP_(s_(t2))(x).
  - KP_s(x) depends only on the keys of x's two options under s, which depend only on the states of movers of level < lev(x) = l + 1
    (RESULTS R105 (LOCAL), «a key only on the states below its level»).
  - No mover of level ≤ l moves at any step of [a, b], so s_(t1) and s_(t2) agree on all of them. So KP_(s_(t1))(x) = KP_(s_(t2))(x),
    that is a′ = b′. Contradiction. ∎
- Does NOT claim: anything at degree ≥ 3 (the proof uses that a mover with two options must return to the option it left); any bound
  on moves at levels ≥ l + 2 inside [a, b].

## 3. Lemma SHIFT (PROVED)
- Statement (IDEAL-ACYC, any degree, any width). Let G be a genome in which every level-0 mover has degree 1. Let Γ be an integer larger
  than every gate index of G. Define G↓:
  - every mover of level ≥ 1 has its level lowered by 1, and the level-0 movers stay at level 0;
  - every option (x, k) of a mover of old level 1 loses its W-target, and its gate becomes g′(x, k) := g(w, k_w) · Γ + g(x, k), where
    w := wt(x, k) and k_w is the only option of w;
  - every other field (all other W-targets and gates, all Ξ-targets, β's, degrees) and the start are unchanged.
  - Then G↓ is an IDEAL-ACYC genome, and from every start its run is G's run, state for state.
- Proof.
  - Validity.
    - New gates are distinct. g′(x, k) determines the pair (g(w, k_w), g(x, k)) as quotient and remainder by Γ, and distinct options
      have distinct g(x, k), so distinct new gates. A new gate with g(w, k_w) ≥ 1 is ≥ Γ, above every unchanged gate. A new gate with
      g(w, k_w) = 0 equals g(x, k), the option's own old gate, which no unchanged gate equals.
    - W-targets: old level-1 options have none (new level 0). Every other W-target pointed one level down and still does, since both
      ends moved down by one. No option points to an old level-0 mover any more.
    - The Ξ-data, hence the Ξ-graph, are unchanged, so G↓ is acyclic.
  - Ξ-values: identical in G and G↓ for every state, by the unchanged Ξ-data. So every A_s(x) is the same.
  - Keys. Take an option (x, k) of old level l ≥ 1 and a state s. Its W-chain in G under s passes options o_0, o_1, …, o_l = (x, k) at
    old levels 0, 1, …, l, with o_0 the only option of its mover.
    - key^G_s(x, k) = (g(o_0), g(o_1), g(o_2), …, g(o_l)).
    - key^(G↓)_s(x, k) = (g′(o_1), g(o_2), …, g(o_l)), with g′(o_1) = g(o_0) · Γ + g(o_1).
    - Since 0 ≤ g(o_1) < Γ, g′(o_1) < g′(o_1′) iff (g(o_0), g(o_1)) < (g(o_0′), g(o_1′)) lexicographically. So for any two options of
      the same mover the two key orders agree.
  - Level-0 movers (degree 1) never move in either genome. So at every step both genomes choose the same option at every mover, and
    their stop rules (singleton test, no-change test) agree. ∎
- Does NOT claim: anything when some level-0 mover has degree ≥ 2.

## 4. Corollary SEG-CAP (PROVED)
- Definitions. For d ≥ 1, 𝓛_d is the class of IDEAL-ACYC genomes with levels 0, …, d − 1 and exactly two degree-2 movers on every
  level; any number of degree-1 movers may be added at any level, and no mover has degree ≥ 3. T*(d) := the supremum of T over all
  genomes of 𝓛_d and all starts. It is finite, by induction on d: T*(1) ≤ 2 by SEG-ONCE with l = −1 (each of the two degree-2 movers
  moves at most once, and every step moves one of them), and the step from d − 1 to d is the upper bound of SANDWICH (§5), whose proof
  uses only SEG-CAP at d.
- For a run of a genome in 𝓛_d (d ≥ 2): a LEVEL-0 STEP is a step whose movers include a level-0 mover. By SEG-ONCE (l = −1) each of the
  two degree-2 level-0 movers moves at most once, and degree-1 movers never move, so there are at most 2 level-0 steps.
  - seg1 := the number of steps before the first level-0 step (T if there is none).
  - mid := the number of steps strictly between the first and the last level-0 step (0 if there are fewer than 2).
  - tail := the number of steps after the last level-0 step (0 if there is none).
  - So T = seg1 + mid + tail + (number of level-0 steps).
- Statement (d ≥ 2). In every run of every genome of 𝓛_d: seg1, mid and tail are each ≤ T*(d − 1).
- Proof.
  - Each of the three counts is the length of a (possibly empty) interval [a, b] of consecutive steps none of which moves a level-0
    mover. If it is empty there is nothing to prove.
  - By SEG (§1) with l = 0, the genome H in which every level-0 mover keeps only its option at s_(a−1) runs from s_(a−1) through
    s_(a−1), …, s_b. So H's run from s_(a−1) has at least b − a + 1 steps.
  - Every level-0 mover of H has degree 1, so SHIFT (§3) applies. H↓ has the same run.
  - H↓ ∈ 𝓛_(d−1): its levels are 0, …, d − 2. Its level 0 holds the two degree-2 movers of G's level 1, plus degree-1 movers. Its level
    l ≥ 1 holds G's level l + 1, with the same degrees.
  - So b − a + 1 ≤ T*(d − 1). ∎
- Does NOT claim: that the three counts can be ≈ T*(d − 1) at the same time (that is the open CONJECTURE SLOT-TRADE, not in this packet).

## 5. Lemma LIFT and Corollary SANDWICH (PROVED)
- Lemma LIFT (IDEAL-ACYC, any degree, any width). Let G have levels 0, …, d − 1. Build G^:
  - every mover of G has its level raised by 1;
  - two new movers A, B of level 0 and degree 2 are added. Each of their four options has Ξ-target X and no W-target. Their β's get four
    new ranks above all ranks of G, all with even parity, the larger one of each mover on its option 0. Their gates are four new
    indices above all gates of G;
  - every option of a mover of old level 0 gets W-target A;
  - the start is G's start with A and B at option 0.
  - Then G^ is IDEAL-ACYC, A and B never move, and the run of G^ is G's run on the old movers, state for state; in particular T(G^) =
    T(G).
- Proof.
  - Validity: ranks and gates are distinct; W-targets lie one level down (old level-0 options now point to A, of level 0); A and B are
    nobody's Ξ-target and their own options exit to X, so the Ξ-graph only gains two isolated vertices.
  - A and B: the Ξ-value of each of their options is the set of its own β. Option 0 carries the larger rank with even parity, so
    Ξ(A, 0) ▷ Ξ(A, 1) under every state; at option 0, A_s(A) = {0}, so A never moves. The same holds for B.
  - Old movers: their chains never pass A or B, so all Ξ-values and A-sets are as in G.
  - Keys: under any state, the W-chain of an old option ends at (A, 0). So its key in G^ is (g(A, 0)) followed by its key in G. A common
    first entry does not change the order of two keys.
  - Hence every step chooses the same options at the old movers, A and B stay put, and the stop rules agree. ∎
- Corollary SANDWICH (d ≥ 2).
  - T*(d − 1) ≤ T*(d) ≤ 3 T*(d − 1) + 2.
  - The supremum of seg1 over all runs of 𝓛_d equals T*(d − 1).
- Proof.
  - Upper bound: T = seg1 + mid + tail + (number of level-0 steps) ≤ 3 T*(d − 1) + 2, by SEG-CAP and the ≤ 2 level-0 steps.
  - Lower bound and seg1: for G ∈ 𝓛_(d−1) and any start, G^ ∈ 𝓛_d (two degree-2 movers on the new level 0; every old level gains one in
    index and keeps its movers and degrees). Its run has no level-0 step (A, B never move), so seg1 = T(G^) = T(G).
  - Taking suprema: T*(d) ≥ T*(d − 1) and sup seg1 ≥ T*(d − 1). SEG-CAP gives sup seg1 ≤ T*(d − 1). ∎
- Does NOT claim: any polynomial bound (the upper recursion gives 3^d − 1); that T* is strictly increasing; anything off 𝓛_d for SANDWICH
  (LIFT itself holds for every genome).

## 6. DEAD: SEG1-2D (instance lift_max_d4_L13)
- The statement killed. CONJECTURE SEG1-2D (lane; the precise form of the route «bound the first segments linearly in d», Lead brief box
  158): «in every run of every 2-wide degree-2 ladder with d ≥ 2 levels (no degree-1 movers), seg1 ≤ 2d − 1».
  - It holds on every genome-start run of the corpus (docs/new/N5-SLOT-box158.md §0 table: largest seg1 3, 5, 6, 9, 10 at d = 3, 4, 5,
    6, 8).
- Instance: experiments/new/box158/lift_max_d4_L13.json, built by box158/lift.py from L-RED R197's max_d4_L13
  (experiments/new/box156/ext/max_d4_L13.json, sha1 f0735b61…). sha1 of the instance: see §7.
  - It is a 2-wide degree-2 ladder with d = 5 levels and no degree-1 movers.
  - The box 150 simulator runs it from its stored start: T = 13, the same states as max_d4_L13 on the old movers (lift.py: SAME True),
    and no level-0 step. So seg1 = 13 > 2·5 − 1 = 9.
- So SEG1-2D is DEAD. More generally, by SANDWICH any bound seg1 ≤ f(d) on 𝓛_d implies T*(d − 1) ≤ f(d). A linear seg1 bound is
  therefore a linear bound on T* itself: the route is circular.
- Does NOT claim: anything about T*'s growth.

## 7. Machine check, excluded parts, TARGET diff (not to sign)
- Machine checks, wired into experiments/new/check.sh:
  - block w108: lift.py on max_d4_L13, max_d5_L15 and dd_d5_F14 (SAME True each: lifted run = original on the old movers, A and B
    fixed); three.py: lift_max_d4_L13 «d 5 T 13 cuts [] seg1 13», lift_max_d5_L15 «d 6 T 15 cuts [] seg1 15»;
  - block «P-IDEAL-SLOT»: sha1 pins of this packet, its line L-1 and the instance; the box 150 checker (check.py) on the instance gives
    XSIM 0, TOPO 0 and 0 violations.
  - SEG and SEG-ONCE: block w106 (segcheck.py; 59 corpus runs and 34,934 random runs, 0 violations; BADLEV=2 fires).
- EXCLUDED (not to sign): CONJECTURE SLOT-TRADE; the segment table and every READING of docs/new/N5-SLOT-box158.md.
- Diff against TARGET.md: no statement mentions a parity game, a winning region, an algorithm's running time or a complexity class. Each
  is about the step sequence of the IDEAL model of RESULTS R104's definition. None is an M4 or M3 claim, none bounds anything
  polynomially, none is a gauntlet step. The link to the fleet question is R104's statement (not used here). G-N5-TIME stays OPEN.
- READING (value): SANDWICH pins the ladder growth question to one trade-off: T*(d) − T*(d − 1) is the extra room that the mid segment
  and the tail can add beyond a seg1 that already uses a full (d − 1)-run.
