# Packet P-IDEAL-SEG (box 157): stretches without low-level moves (SEG, SEG-ONCE) and the level-product bound T + 1 ≤ Π_l (n_l + 1) at degree ≤ 2 (LEVEL-PRODUCT); DEAD: REPLAY
L-NEW successor 51 (Opus 5.5), D14 / D18; Lead 2026-11-04 11:49Z: «(a) freeze P-IDEAL-SEG for both referees, in the same form as
P-IDEAL-M2». Written 2026-11-04 (date -u: see the commit). FROZEN at push: later text goes into docs/new/P-IDEAL-SEG-fixes.md
(append-only). Source: docs/new/N5-SEG-box157.md §1 (box 157). This packet governs: every proof below is written out in full here and is
checked against this text only. Labels: PROVED (L-NEW 51, unrefereed) / DEAD / DATA / READING (not to sign). Not a TARGET.md claim.
Every statement is about the IDEAL-ACYC model only. No polynomial bound is claimed anywhere: LEVEL-PRODUCT is an EXPONENTIAL bound.
G-N5-TIME stays OPEN.

## To sign, and what is not to sign
| § | statement | label | kind |
| --- | --- | --- | --- |
| §1 | Lemma SEG (any degree) | PROVED | restriction of a stretch to a smaller genome |
| §2 | Lemma SEG-ONCE (degree ≤ 2) | PROVED | per-stretch move bound |
| §3 | Corollary LEVEL-PRODUCT (degree ≤ 2), with the 2-wide-ladder form T ≤ 3^d − 1 | PROVED | exponential count bound |
| §4 | DEAD: REPLAY (lane conjecture, precise form), instance max_d5_L15 | DEAD (instance) | refutation of a lane conjecture |
| §5 | machine check, excluded parts, TARGET diff | DATA / READING (not to sign) | |

- Premises (both LANDED).
  - RESULTS R104 (P-N5-REALIZE): ONLY its definition of the IDEAL model and of the Ξ-graph, restated in §0. No theorem of R104 is used.
  - RESULTS R105 (P-IDEAL-RED): only item LOCAL, key half, quoted verbatim from the R105 statement where it is used. No other R105 item
    is used. U, CHAIN-BACK and the CHAINED binder (R105 Erratum E-2, at CHECKER C119) are not used.
  - Not used: RESULTS R106, R107, docs/lit, docs/sources, any other lane file. No outside source is cited.
- Each statement lists its hypotheses (model, degree, width) and a line «does NOT claim».

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

## 1. Lemma SEG (PROVED)
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

## 2. Lemma SEG-ONCE (PROVED)
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

## 3. Corollary LEVEL-PRODUCT (PROVED)
- Statement (IDEAL-ACYC, degree ≤ 2, any width).
  - Definitions: C_(−1) := 0; for l ≥ 0, C_l := |{t ∈ [1, T] : Mv_t contains a mover of level ≤ l}|; n_l := the number of degree-2
    movers of level l.
  - Then C_(l+1) + 1 ≤ (C_l + 1)(n_(l+1) + 1) for every l ≥ −1. Hence T + 1 ≤ Π_(l = 0..top) (n_l + 1), with top the largest level.
  - On a d-level 2-wide ladder: T ≤ 3^d − 1.
- Proof.
  - Fix l ≥ −1. The set of steps counted by C_l splits [1, T] into at most C_l + 1 maximal intervals of steps not counted by C_l.
  - Every step counted by C_(l+1) but not by C_l lies in one of these intervals and moves some mover of level l + 1. That mover has
    degree 2 (degree-1 movers never move).
  - By SEG-ONCE (applied to the interval, which satisfies SEG's hypothesis), each of the n_(l+1) degree-2 movers of level l + 1 moves
    at most once per interval. So each interval holds at most n_(l+1) such steps.
  - Hence C_(l+1) ≤ C_l + (C_l + 1) n_(l+1), i.e. C_(l+1) + 1 ≤ (C_l + 1)(n_(l+1) + 1).
  - Every step moves some mover, so T = C_top. Induction from C_(−1) + 1 = 1 gives T + 1 ≤ Π_l (n_l + 1).
  - Ladder: n_l = 2 for l = 0, …, d − 1, so T + 1 ≤ 3^d. ∎
- Remark (not to sign, arithmetic): Π_l (n_l + 1) ≤ 2^(Σ_l n_l), with equality iff every n_l ≤ 1. So at degree ≤ 2 the bound is never
  above 2^(number of degree-2 movers).
- Does NOT claim: any polynomial bound (the bound is exponential in the number of levels holding a degree-2 mover); tightness; anything
  at degree ≥ 3.

## 4. DEAD: REPLAY (precise lane form; instance max_d5_L15)
- The statement killed. CONJECTURE REPLAY (lane), the precise form of the box 157 proposal («after a level-0 reset the next segment is a
  sub-run of a segment already seen (no new states above)»):
  - For every degree-≤-2 IDEAL-ACYC run and every maximal interval [a, b] of steps none of which moves a level-0 mover, with a ≥ 2
    (so step a − 1 moves a level-0 mover):
  - every state s_t with t ∈ [a, b] agrees, on every mover of level ≥ 1, with some state s_j with j < a.
- Instance: L-RED R202's max_d5_L15 (claude/l-red 05c48415, experiments/red/r202/max_d5_L15.json; pinned there as max_d5_L15_n96).
  Copy: experiments/new/box157/max_d5_L15.json, sha1 ba963aceabeb35d95f9c47d80d1d0e87b87baf21. It is a 5-level 2-wide ladder (N 10,
  degree 2). Run from its stored start [0, 0, 1, 1, 0, 0, 0, 0, 1, 0] with the box 150 simulator: T = 15.
- States s_0 … s_15 (option per mover 0..9; levels [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]):
  - s_0 (0 0 1 1 0 0 0 0 1 0), s_1 (0 0 1 1 0 1 0 0 1 0), s_2 (0 0 1 1 0 1 0 0 1 1), s_3 (0 0 1 1 0 1 0 1 1 1);
  - s_4 (0 0 1 1 0 1 1 1 0 1), s_5 (0 0 1 1 0 1 1 1 0 0), s_6 (0 0 1 1 1 1 1 1 0 0), s_7 (1 0 0 0 1 1 1 1 0 0);
  - s_8 (1 1 0 0 1 1 1 1 0 0), s_9 (1 1 0 0 0 1 1 1 0 0), s_10 (1 1 0 0 0 1 0 0 1 1), s_11 (1 1 0 0 0 0 0 0 1 1);
  - s_12 (1 1 0 1 0 0 0 0 1 1), s_13 (1 1 0 1 0 0 0 1 1 1), s_14 (1 1 0 1 0 0 1 1 1 0), s_15 (1 1 0 1 1 0 1 1 1 0).
- The level-0 movers 0 and 1 move only at steps 7 and 8. So [9, 15] is a maximal interval with no level-0 move, and a = 9 ≥ 2.
- s_9 restricted to movers 2..9 is (0 0 0 1 1 1 0 0). No s_j with j ≤ 8 has it: s_0 … s_6 have (1 1 …) on movers 2, 3; s_7 and s_8
  have (0 0 1 1 1 1 0 0). So REPLAY fails at t = 9.
  - In fact every one of s_9 … s_15 is new above level 0 (box157/seg.py: NEWSTATES 7).
- So REPLAY is DEAD.
- Also on the same run: the interval [9, 15] has length 7, longer than the only earlier such interval [1, 6] (length 6).
- Does NOT claim: anything about other «replay» readings (e.g. repetition of mover sets, which does occur in max_d4_L13).

## 5. Machine check, excluded parts, TARGET diff (not to sign)
- Machine checks, wired into experiments/new/check.sh (block «P-IDEAL-SEG»; the box 157 block w106 runs the same checker), with the
  frozen files and the instance pinned by sha1:
  - experiments/new/box157/segcheck.py. It uses the box 150 simulator and builds H with box150/check.py restrict(). For every level
    l ∈ {−1, …, top − 1} and every maximal interval without a level-≤-l move, it checks:
    - SEG: H's run reproduces the interval;
    - ONCE: each level-(l + 1) mover moves at most once inside (degree ≤ 2);
    - COUNT: C_(l+1) + 1 ≤ (C_l + 1)(n_(l+1) + 1);
    - PROD: T + 1 ≤ Π (n_l + 1).
  - DATA: 0 violations on 59 corpus runs (652 intervals).
    - Boxes 140-153, box156/ext (max_d4_L13, dbl_d3_F6, dbl_d4_F10), box157/max_d5_L15 and the degree-3 genomes of box139/genomes. At
      degree 3 only SEG is checked.
  - DATA: 0 violations on 34,934 random runs: box150/out/rand, every start for N ≤ 8, the genome start otherwise; 57,755 intervals.
  - Negative control BADLEV=2 (ONCE tested at level l + 2): ONCE 112 on the corpus.
  - Largest (T + 1) / Π (n_l + 1): 1/3 on the corpus, 1 on the random runs (reached only by genomes with one degree-2 mover).
  - experiments/new/box157/seg.py on max_d5_L15 prints the §4 segment data (cuts [7, 8]; segment t9-15, NEWSTATES 7).
- EXCLUDED (lane statements, not to sign):
  - the slot-filling reading and the L-RED target (R203);
  - the «pattern replay» observations on max_d4_L13 / g4_L12 / x3_L8;
  - every READING of docs/new/N5-SEG-box157.md.
- Diff against TARGET.md (statement by statement).
  - No statement mentions a parity game, a winning region, an algorithm's running time or a complexity class. Each is about the step
    sequence of the IDEAL model of RESULTS R104's definition.
  - None is an M4 or M3 claim, none bounds anything polynomially, and none is a gauntlet step.
  - The link to the fleet question is R104's statement (landed, not used here), not this packet's. G-N5-TIME stays OPEN.
- READING (value): LEVEL-PRODUCT locates all super-linear room of degree-2 runs in the «reset slots» C_(l+1) − C_l ≤ (C_l + 1) n_(l+1).
  A polynomial bound needs most slots to stay empty; an exponential family must fill them level after level. Neither is claimed.
