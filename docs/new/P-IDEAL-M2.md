# Packet P-IDEAL-M2 (box 156): multi-mover steps measure IDEAL-ACYC run length (MULTI-CHARGE both directions, SINGLE-SHORT, TRIGGER, XIFLIP, MIN-FLIP); DEAD: LIN-156
L-NEW successor 51 (Opus 5.5), D14 / D18; Lead GO 2026-11-04 07:00Z («P-M2 packet: GO. Freeze docs/new/P-IDEAL-M2.md, self-contained,
in the P-IDEAL-RED form»). Written 2026-11-04 (date -u: see the commit). FROZEN at push: later text goes into
docs/new/P-IDEAL-M2-fixes.md (append-only). Source: docs/new/N5-GATE-box155.md §1 (MULTI-CHARGE, box 155) and docs/new/N5-M2-box156.md
§1 (box 156). This packet governs: every proof below is written out in full here and is checked against this text only.
Labels: PROVED (L-NEW 51, unrefereed) / DEAD / DATA / READING / CONJECTURE (not to sign). Not a TARGET.md claim. Every statement is
about the IDEAL-ACYC model only. No polynomial bound is claimed anywhere. G-N5-TIME stays OPEN.

## To sign, and what is not to sign
| § | statement | label | kind |
| --- | --- | --- | --- |
| §1 | Lemma MULTI-CHARGE, Corollary M2-EQ, Corollary SINGLE-SHORT (any degree) | PROVED | REDUCTION / EQUIVALENCE of two counts |
| §2 | Lemma TRIGGER (degree ≤ 2) | PROVED | structure of a step |
| §3 | Lemma XIFLIP, Corollary MIN-FLIP (degree ≤ 2) | PROVED | per-mover count bound by flips |
| §4 | DEAD: «LIN-156: T ≤ ⌊3N/2⌋ on degree-≤-2 IDEAL-ACYC» | DEAD (instance) | refutation of a lane conjecture |
| §5 | machine check, excluded parts, TARGET diff | DATA / READING (not to sign) | |

- Premises (both LANDED).
  - RESULTS R104 (P-N5-REALIZE): ONLY its definition of the IDEAL model and of the Ξ-graph, restated in §0. No theorem of R104 is used.
  - RESULTS R105 (P-IDEAL-RED), by item name: ENC, LOCAL, XI-NEW, RISE, CHAIN-BACK, KEYFLIP (MONO and the other items are not used). Each is
    quoted where it is used, verbatim from the RESULTS R105 statement.
  - Not used: RESULTS R106 (P-IDEAL-CUBE), docs/lit, docs/sources, any other lane file. No outside source is cited.
- Each statement lists its hypotheses (model, degree, width) and a line «does NOT claim».

## 0. The model (RESULTS R104's definition; notation of RESULTS R105)
- A genome G has N ≥ 1 movers x, each with a level lev(x) ∈ {0, 1, …} and deg(x) ≥ 1 options (x, k). Each option has a W-target
  wt(x, k) (a mover of level lev(x) − 1; none at level 0), a Ξ-target xt(x, k) (a mover or the exit X), a β with a rank (distinct over
  all options) and a parity, and a gate index g(x, k) (distinct over all options). There is a start s_0. A state s picks one option
  s(x) per mover.
- Ξ-graph: an edge x → xt(x, k) for every option whose Ξ-target is a mover. IDEAL-ACYC: it is acyclic. π is a fixed topological order
  (π(x) < π(y) on every edge). A strict Ξ-descendant of x is a mover reachable from x by a nonempty Ξ-path.
- Under s, the chain of (x, k) is (x, k), (y_1, s(y_1)), (y_2, s(y_2)), … with y_1 = xt(x, k), y_(j+1) = xt(y_j, s(y_j)), up to the
  first option whose Ξ-target is X. Its Ξ-value Ξ_s(x, k) is the set of β's on it. Two sets P ≠ Q are compared by the β of largest rank
  in P △ Q: the set containing it is better (P ▷ Q) if that β's parity is even, worse if odd.
- A_s(x) := {s(x)} ∪ {k : Ξ_s(x, k) ▷ Ξ_s(x, s(x))}. x is unstable at s iff |A_s(x)| ≥ 2.
- key_s(x, k) := (g(x, k)) if lev(x) = 0, else key_s(wt(x, k), s(wt(x, k))) followed by g(x, k); compared lexicographically.
- Step. If every A_(s_(t−1))(x) is a singleton, the run stops. Otherwise s_t is defined level by level, lowest level first:
  s_t(x) := the option in A_(s_(t−1))(x) with the least key_(s_t)(x, ·) (keys under the NEW state; well defined since key_(s_t)(x, ·)
  reads s_t only below lev(x)). If s_t = s_(t−1), the run stops without that step. T := the number of steps.
- Mv_t := {x : s_t(x) ≠ s_(t−1)(x)} (nonempty for t ∈ [1, T]); moves(x) := |{t : x ∈ Mv_t}|; h_t := a least-level mover of Mv_t
  (smallest index on a tie). Step t ∈ [2, T] is CHAINED iff h_(t−1) lies on the chain of (h_t, s_t(h_t)) under s_(t−2) (as a mover
  other than h_t), and UNCHAINED otherwise; U := the number of unchained steps (RESULTS R105).
- M₂ := |{t ∈ [1, T − 1] : |Mv_t| ≥ 2}| (the number of multi-mover steps, the last step excluded).
- Degree 2, used in §2-§3. If deg(x) = 2, write o′ for the option of x other than o. For a state s: x is unstable at s iff
  Ξ_s(x, o′) ▷ Ξ_s(x, o) with o = s(x), and then A_s(x) = {o, o′}. So at degree 2 the step rule reads: x ∈ Mv_t iff, with
  o = s_(t−1)(x), (i) Ξ_(s_(t−1))(x, o′) ▷ Ξ_(s_(t−1))(x, o) and (ii) key_(s_t)(x, o′) < key_(s_t)(x, o). A mover of degree 1 never moves.
- No width hypothesis is made anywhere: every level may hold any number of movers.

## 1. Lemma MULTI-CHARGE, Corollaries M2-EQ and SINGLE-SHORT (PROVED)
- Lemma MULTI-CHARGE (IDEAL-ACYC, any degree, any width). Every unchained step t ∈ [2, T] has |Mv_(t−1)| ≥ 2. Hence U ≤ M₂ and
  T ≤ N (1 + M₂).
- Proof.
  - Let t ∈ [2, T] and w := s_t(h_t). RESULTS R105 (XI-NEW) + (RISE), applied with h = h_t: «for t ≥ 2 every least-level mover h of
    step t moves to an option w ∉ A_(s_(t−2))(h)»; «that option's value rose strictly at step t − 1, and some strict Ξ-descendant of
    h on its chain under s_(t−2) moved at step t − 1».
  - So the set Z_t of movers z ≠ h_t on the chain of (h_t, w) under s_(t−2) with z ∈ Mv_(t−1) is nonempty.
  - Suppose Mv_(t−1) = {h_(t−1)}. Then Z_t ⊆ Mv_(t−1) gives Z_t = {h_(t−1)}. So h_(t−1) lies on the chain of (h_t, w) under s_(t−2), as
    a mover other than h_t: step t is chained.
  - Contrapositive: an unchained step t ≥ 2 has |Mv_(t−1)| ≥ 2, and t − 1 ∈ [1, T − 1]. Distinct t give distinct t − 1, so U ≤ M₂.
  - RESULTS R105 (CHAIN-BACK): «T ≤ N (1 + U) with U the number of unchained steps t ∈ [2, T]». With U ≤ M₂: T ≤ N (1 + M₂). ∎
- Corollary M2-EQ (IDEAL-ACYC, any degree, any width).
  - M₂ ≤ max(T − 1, 0) (M₂ counts steps of [1, T − 1]) and T ≤ N (1 + M₂).
  - So for any family 𝓕 of IDEAL-ACYC runs (genome and start): T is bounded on 𝓕 by a polynomial in N + M iff M₂ is.
    - (⇒) M₂ ≤ T.
    - (⇐) if M₂ ≤ p(N + M), then T ≤ N (1 + p(N + M)).
- Corollary SINGLE-SHORT (IDEAL-ACYC, any degree). If |Mv_t| = 1 for every t ∈ [1, T − 1], then T ≤ N. (M₂ = 0.) ∎
- Does NOT claim: any bound on M₂ or on T; anything on Ξ-cyclic genomes. It is a REDUCTION (T to M₂) and an EQUIVALENCE of the two
  growth classes, nothing more.

## 2. Lemma TRIGGER (PROVED)
- Statement (IDEAL-ACYC, degree ≤ 2, any width). Let t ∈ [2, T], z ∈ Mv_t, o := s_(t−1)(z), o′ the other option of z. Define:
  - XiT(z, t): [Ξ(z, o′) ▷ Ξ(z, o)] has different truth values under s_(t−2) and under s_(t−1);
  - WT(z, t): [key(z, o′) < key(z, o)] has different truth values under the keys of s_(t−1) and under the keys of s_t.
  - Then:
    - (a) XiT(z, t) or WT(z, t);
    - (b) XiT(z, t) implies that some mover y ≠ z on the chain of (z, o) or of (z, o′) under s_(t−2) is in Mv_(t−1), and every such y
      is a strict Ξ-descendant of z;
    - (c) WT(z, t) implies that some mover of level < lev(z) is in Mv_t.
- Proof.
  - deg(z) = 2, since z moves.
  - (a) Suppose neither holds. Since z ∈ Mv_t, the step rule (§0, degree 2) gives Ξ_(s_(t−1))(z, o′) ▷ Ξ_(s_(t−1))(z, o) and
    key_(s_t)(z, o′) < key_(s_t)(z, o). With no flip, also Ξ_(s_(t−2))(z, o′) ▷ Ξ_(s_(t−2))(z, o) and key_(s_(t−1))(z, o′) <
    key_(s_(t−1))(z, o).
    - Case s_(t−2)(z) = o. Then z is unstable at s_(t−2) with A_(s_(t−2))(z) = {o, o′}. The step rule of step t − 1 takes the option
      with the least key under the keys of s_(t−1), which is o′. So s_(t−1)(z) = o′ ≠ o. Contradiction.
    - Case s_(t−2)(z) = o′. Then s_(t−1)(z) = o ≠ o′, so z ∈ Mv_(t−1) moved from o′ to o. The step rule of step t − 1 requires
      Ξ_(s_(t−2))(z, o) ▷ Ξ_(s_(t−2))(z, o′). But ▷ is a strict order (RESULTS R105 ENC: «the Ξ-order of β-sets is the order of the
      integers Σ ±2^rank»), and Ξ_(s_(t−2))(z, o′) ▷ Ξ_(s_(t−2))(z, o) holds. Contradiction.
    - Both cases are impossible, which proves (a).
  - (b) RESULTS R105 LOCAL: «an option's value depends only on the states on its chain».
    - Suppose no mover y ≠ z on the chains of (z, o) and (z, o′) under s_(t−2) is in Mv_(t−1). Then s_(t−1) agrees with s_(t−2) on
      those movers, so both chains and both values are unchanged from s_(t−2) to s_(t−1). Then XiT(z, t) fails.
    - The movers after z on these chains are reached from z by Ξ-edges, and acyclicity excludes z. So they are strict Ξ-descendants.
  - (c) RESULTS R105 LOCAL: «a key only on the states below its level».
    - If no mover of level < lev(z) is in Mv_t, then s_t and s_(t−1) agree below lev(z). So key_(s_t)(z, ·) = key_(s_(t−1))(z, ·), and
      WT(z, t) fails. ∎
- Does NOT claim: any count of XiT or WT events; that a step with a W-triggered mover is a multi-mover step for a reason other than (c)
  (it is one: (c) gives a second mover of lower level in Mv_t, so |Mv_t| ≥ 2); anything at degree ≥ 3.

## 3. Lemma XIFLIP and Corollary MIN-FLIP (PROVED)
- Definitions (degree ≤ 2). For deg(x) = 2, with the two options 0 and 1: σ_s(x) := [Ξ_s(x, 1) ▷ Ξ_s(x, 0)]. XF_x := |{j ∈ [1, T] :
  σ_(s_j)(x) ≠ σ_(s_(j−1))(x)}|. XF_x := 0 if deg(x) = 1. KF_x is RESULTS R105's: «KF_x the number of steps at which KP(x) changes»
  (KP_s(x) the key-preferred option under the keys of s).
- Lemma XIFLIP (IDEAL-ACYC, degree ≤ 2, any width). moves(x) ≤ 1 + XF_x for every mover x.
- Proof.
  - If moves(x) ≤ 1 there is nothing to prove. Let a < b be consecutive moves of x. With two options, x moves from o to o′ at a and
    from o′ back to o at b.
  - At a, the step rule needs Ξ_(s_(a−1))(x, o′) ▷ Ξ_(s_(a−1))(x, o). At b, it needs Ξ_(s_(b−1))(x, o) ▷ Ξ_(s_(b−1))(x, o′).
  - ▷ is a strict order (ENC), so σ(x) takes different values at s_(a−1) and s_(b−1). Hence some j ∈ [a, b − 1] has
    σ_(s_j)(x) ≠ σ_(s_(j−1))(x).
  - The ranges [a, b − 1] of distinct consecutive pairs are disjoint. So moves(x) − 1 ≤ XF_x. ∎
- Corollary MIN-FLIP (IDEAL-ACYC, degree ≤ 2).
  - moves(x) ≤ 1 + min(KF_x, XF_x). Proof: XIFLIP and RESULTS R105 (KEYFLIP): «moves(x) ≤ 1 + KF_x with KF_x the number of steps
    at which KP(x) changes».
  - XF_x ≤ |{j : some strict Ξ-descendant of x is in Mv_j}|. Proof: if no strict Ξ-descendant of x moves at step j, then s_j and
    s_(j−1) agree on every strict Ξ-descendant. By LOCAL, both values of x are unchanged, so σ(x) is unchanged.
  - KF_x ≤ |{j : some mover of level < lev(x) is in Mv_j}|. Proof: by LOCAL the keys of x read only levels < lev(x). ∎
- Does NOT claim: any bound on XF_x or KF_x. Both right-hand sides can be large; no polynomial bound follows.

## 4. DEAD: LIN-156 (instance; not a theorem to sign beyond the computation)
- The statement killed. CONJECTURE LIN-156 (docs/new/N5-M2-box156.md, first version, 4047aacf): «for every IDEAL-ACYC genome of degree
  ≤ 2 with N movers and every start, T ≤ ⌊3N/2⌋ and M₂ ≤ N + 1». Its T part is FALSE.
- Instance: L-RED R197's exact d = 4 witness max_d4_L13 (claude/l-red 46588929, experiments/red/r197/lag/max_d4_L13.json; pinned there
  as max_d4_L13_n78). Copy: experiments/new/box156/ext/max_d4_L13.json, sha1 f0735b61312bdbfe1bb553496d7e9ee38681dcee. Inline
  (JSON of the box 139-150 format; option = [W-target, Ξ-target (−1 = X), β index]; br / bp: rank / parity of β index; gate per option):
  - N 8; lev [0, 0, 1, 1, 2, 2, 3, 3]; every mover has degree 2.
  - opts: 0: [[−1, 2, 0], [−1, 3, 1]]; 1: [[−1, 5, 2], [−1, −1, 3]]; 2: [[0, 3, 4], [1, 4, 5]]; 3: [[0, 7, 6], [1, 1, 7]];
    4: [[2, 7, 8], [3, 6, 9]]; 5: [[2, −1, 10], [3, −1, 11]]; 6: [[4, 7, 12], [5, 3, 13]]; 7: [[4, 1, 14], [5, 5, 15]].
  - gate: [[13, 15], [4, 14], [0, 9], [6, 1], [10, 11], [7, 12], [3, 8], [5, 2]].
  - br: [9, 2, 11, 12, 5, 8, 0, 10, 1, 6, 14, 15, 4, 7, 3, 13]; bp: [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1].
  - start [1, 1, 0, 0, 0, 1, 0, 1]; topological order (xorder) [0, 2, 4, 6, 3, 7, 1, 5].
- Recomputed by the box 150 simulator (experiments/new/box150/check.py, own simulator of §0; XSIM against box139/paths.py; TOPO checks
  acyclicity):
  - T = 13 > ⌊3·8/2⌋ = 12; M₂ = 5, U = 4.
  - |Mv_t| for t = 1..13: 1, 1, 2, 1, 1, 2, 3, 2, 1, 1, 2, 1, 1.
  - XSIM 0, TOPO 0, and 0 violations of every RESULTS R105 check on this run.
  - Also box156/val.py: «N 8 T 13 M2 5 U 4».
- So LIN-156 is DEAD. The M₂ part (M₂ ≤ N + 1) is not killed by this instance (M₂ = 5).
- Does NOT claim: anything about the CONJECTURE LIN-2 (T ≤ 2N), which stays a CONJECTURE (not to sign); any growth rate.

## 5. Machine check, excluded parts, TARGET diff (not to sign)
- Machine checks, wired into experiments/new/check.sh (block «P-IDEAL-M2»), with the frozen files pinned by sha1 in the same block:
  - experiments/new/box155/mcharge.py (MULTI-CHARGE; own counts on the box 150 simulator).
    - DATA: VIOL 0, BOUND 0 on 54 corpus runs (boxes 140-153 and box156/ext: 468 steps, M₂ total 300).
    - DATA: VIOL 0, BOUND 0 on 34,934 runs of the 200 random genomes of box150/out/rand (every start of each genome with N ≤ 8, the
      genome start of the others; ALL=1 ALLN=8).
    - The 6,114 single-mover runs among them have T / N ≤ 1.0 (SINGLE-SHORT).
  - experiments/new/box156/trig.py (TRIGGER (a)-(c) and XIFLIP, degree-≤-2 runs).
    - DATA: NEITHER 0 (a), XNODESC 0 (b), WNOLOW 0 (c), XIFLIP 0, on the same 54 corpus runs (919 moves; XiT 707, WT 333, both 121;
      multi-mover steps 270, of which 162 contain a W-triggered-only mover).
    - DATA: the same zeros on 3,981 runs: every start of each degree-≤-2 random genome of box150/out/rand (all have N ≤ 12; ALL=1).
    - Negative control NEG=3 (keys of the OLD state) on the corpus: NEITHER 141. So (a) visibly depends on «keys under the new state».
  - experiments/new/box156/val.py: max_d4_L13 gives «N 8 T 13 M2 5 U 4» (§4).
- EXCLUDED (lane statements, not to sign):
  - the exact z3 small-N table (max T = 1, 2, 3, 4 for N = 1..4, etc.);
  - DEAD «M₂ ≤ N − 2» (dd_d5_F14);
  - CONJECTURE LIN-2 and the M₂ part of LIN-156;
  - the 2-wide-ladder trend reading;
  - every READING of docs/new/N5-M2-box156.md.
- Diff against TARGET.md (statement by statement).
  - TARGET.md's objects are parity games, winning regions, algorithms and their running time on the word RAM (§1-§3), milestone M4
    (§2) and M3 (§4, §7e).
  - No statement of this packet mentions a parity game, a winning region, an algorithm's running time, or a complexity class. Each is
    about the step sequence of the IDEAL model of RESULTS R104's definition.
  - None is an M4 or M3 claim, none bounds anything polynomially, and none is a gauntlet step for any algorithm.
  - The only link to the fleet question is R104 (landed, its theorem not used here). That link is R104's statement, not this packet's.
  - G-N5-TIME stays OPEN.
- READING (value): M₂ joins T, U and KF as a fourth equivalent growth measure of IDEAL-ACYC runs, and the one easiest to observe.
  TRIGGER says what a multi-mover step is made of: a W-release (a lower-level mover in the same step) or a Ξ-branching. MIN-FLIP caps
  each mover by the smaller of its key flips and its Ξ flips. A polynomial bound would follow from a polynomial bound on M₂, or on
  Σ_x min(KF_x, XF_x). Neither is claimed.
