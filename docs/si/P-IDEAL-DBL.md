# Packet P-IDEAL-DBL (box 79, DRAFT): window and doubling structure of 2-wide ladders; max-plus routes, the doubling gap, pass-through decay and fuel separation are dead
L-SI successor 41 (Opus 5.5), D14 / D18 / D20; Lead brief BOX 79 (2026-11-07 03:58Z). DRAFT, written 2026-11-07 from 04:05Z (date
-u: see the commit). It is NOT frozen: it freezes only after RESULTS R116 (packet P-IDEAL-MOVES) lands; the premises marked «R116
(pending landing)» are then re-quoted from the landed text. Sources: docs/si/N5-TROPICAL-box76.md §1-§12 (this lane). This packet
carries every proof in full and is checked against this text only. Labels: PROVED (L-SI 41, unrefereed) / DEAD (instance,
machine-checked) / CONDITIONAL (not to sign) / DATA / READING (not to sign). Not a TARGET.md claim. Every statement is about the
IDEAL model of RESULTS R104's definition only. No statement bounds T polynomially; G-N5-TIME stays OPEN.

## To sign, and what is not to sign
| § | statement | label | premises |
| --- | --- | --- | --- |
| §1 | Fact MP-LIN | PROVED | none (max-plus algebra) |
| §2 | Lemma WINDOW-ONCE | PROVED | R113 ALIGN |
| §2 | Lemma DBL-EQ (a), (b), (c) | PROVED | R113 ALIGN; WINDOW-ONCE |
| §2 | Lemma PASS-FREEZE | PROVED | R104 definition; R113 ALIGN |
| §3 | Lemma HIT; Corollary FUEL-EXACT (= FUEL (ii)) | PROVED | R104 definition; R105 ENC, MONO, LOCAL |
| §4 | Lemma ALT-MIN (a)-(d) | PROVED | R105 ENC, MONO; R116 AND-GATE (pending landing) |
| §4 | Lemma TOWER-NEED | PROVED | DBL-EQ, HIT, ALT-MIN, R113 PATH-RISE |
| §5 | FUEL-NEED; FUEL (i) | CONDITIONAL (not to sign) | L-LOWER's FEEDBACK (b), not landed, not refereed |
| §6 | DEAD-MAXPLUS, DEAD-DBLGAP, DEAD-DECAY, DEAD-REENTRY | DEAD (instances) | |
| §7 | DATA, machine checks, TARGET diff | DATA / READING (not to sign) | |

## 0. Premises and notation
- LANDED (quoted from trunk docs/RESULTS.md at 2ccd037b9):
  - R104: ONLY the definition of the IDEAL model and of the Ξ-graph (as restated in P-IDEAL-MOVES §0); no theorem of R104.
  - R105, three items «at any degree»: «(ENC) … the value of option (x, k) is ε(x, k) plus the current value of its Ξ-target (ε(x, k)
    alone if the Ξ-target is the exit X)»; «(LOCAL) an option's value depends only on the states on its chain, a key only on the states
    below its level»; «(MONO) the current Ξ-value of every mover never decreases along a run».
  - R110: ONLY the definition of 𝓛^R_d (movers 2l, 2l + 1 on level l, all of degree 2, no other movers, option k of a mover of level
    l ≥ 1 W-pointing to mover 2(l − 1) + k), levels 0, …, d − 1.
  - R113: (ALIGN) «on 𝓛^R_d, for 1 ≤ l ≤ d − 1 and every state s of a run, both movers 2l and 2l + 1 have KP_s = c_l(s), each of them
    that moves at step t moves to option c_l(s_t), and the order of their keys under s is [s(2l) = c_l(s)] if s(2l) ≠ s(2l + 1) and
    γ_l(j) if both are on option j»; (F0) «on 𝓛^R_d each level-0 mover moves at most once and F(0) ≤ 2»; (PATH-RISE) «Then the number
    of steps at which cv(z) rises is at most P(z) − 1.» [IDEAL-ACYC, any degree, any width]; with R113's notation c_l(s), γ_l(j), F(l).
- R116 (pending landing) = packet P-IDEAL-MOVES (claude/l-new d86adc86; fixes at 9995f5a2; signed by both referees; at CHECKER C129):
  Lemma AND-GATE (a) «x ∈ Mv_t iff s_(t−1)(x) ≠ π_(s_(t−1))(x) and π_(s_(t−1))(x) = KP_(s_t)(x)», (b) «If x moves at steps t < t′ and at no
  step strictly between, then π(x) changes at some step of [t, t′ − 1] … Hence moves(x) ≤ 1 + min(KF_x, PF_x).», (c) «If π_(s_t)(x) = b ≠
  π_(s_(t−1))(x), then v_(s_t)(x, b) > v_(s_(t−1))(x, b).» [IDEAL-ACYC, x of degree 2]; its notation π_s(x), PF_x. Used ONLY by §4.
- Not used: every other RESULTS item; WINDOW-DOUBLE and SEG-WINDOW of P-IDEAL-MOVES (the facts needed are re-proved in §2); L-LOWER's
  lane lemmas except in §5 (CONDITIONAL); docs/lit, docs/sources.
- Notation. T, s_t, Mv_t := {x : s_t(x) ≠ s_(t−1)(x)}, moves(x) := #{t ∈ [1, T] : x ∈ Mv_t}. On 𝓛^R_d: the pair l is (2l, 2l + 1); a
  flip of the pair l at t is a change of its key order between s_(t−1) and s_t; F(l) the number of such t; an l-b-step (l ≥ 1) is a flip
  step of the pair l − 1; Φ_l(s) := #{x ∈ {2l, 2l + 1} : s(x) ≠ c_l(s)}. An l-WINDOW is a maximal set [t_0, e] ⊆ [1, T] of consecutive
  steps such that no step of [t_0 + 1, e] is an l-b-step. A level l ≥ 1 is DOUBLING in a run if F(l) = 2F(l − 1) + 2. cv_s(y) :=
  v_s(y, s(y)) (R105 ENC integers); R(y) := #{t : cv_(s_t)(y) > cv_(s_(t−1))(y)}; R_k(x) := #{t : v_(s_t)(x, k) > v_(s_(t−1))(x, k)}.
  The OLD CHAIN of y at t is the chain of (y, s_(t−1)(y)) under s_(t−1) (y included). P(x) the number of maximal Ξ-paths from x (R113).
  Upward option: an option (x, k) with xt(x, k) a mover of level > lev(x). U_l := the Ξ-targets of upward options of movers of level ≤
  l; E_l := {t : cv_(s_t)(y) ≠ cv_(s_(t−1))(y) for some y ∈ U_l}.

## 1. Fact MP-LIN (PROVED; no premise)
- Statement. Let A be a k × k matrix over ℝ ∪ {−∞}, b ∈ ℝ^k, x_0 ∈ ℝ^k, and x_(j+1) ≤ (A ⊗ x_j) ⊕ b for j ≥ 0, where (A ⊗ x)(τ) :=
  max_σ (A(τ, σ) + x(σ)) and ⊕ is the componentwise max. With λ the maximum cycle mean of A (−∞ if A has no cycle) and a the largest
  finite entry of A (0 if none): max_τ x_j(τ) ≤ max(λ, 0)·j + C for every j, where C depends on A, b and x_0 but not on j.
- Proof. By induction, x_j ≤ (A^⊗j ⊗ x_0) ⊕ max_(i<j) (A^⊗i ⊗ b). A^⊗i(τ, σ) is the largest weight of a length-i path σ → τ in the
  weighted digraph of A. Remove cycles from such a path until a path with no repeated vertex remains, of length r ≤ k − 1; each removed
  cycle of length L has weight ≤ λL. So the weight is ≤ max(λ, 0)·(i − r) + r·max(a, 0) ≤ max(λ, 0)·i + (k − 1)·max(a, 0). ∎
- Does NOT claim: any recursion of this form for a quantity of the IDEAL model (§6 DEAD-MAXPLUS kills the two natural ones).
- READING: a maximum cycle mean 0 gives a bounded quantity, not a linear one; every finite max-plus recursion gives at most linear
  growth, so such a route stands or falls on the validity of an additive transfer.

## 2. Window and doubling lemmas on 𝓛^R_d (PROVED; R113 ALIGN; R104 definition)
- Lemma WINDOW-ONCE. Hypotheses: G ∈ 𝓛^R_d, 1 ≤ l ≤ d − 1, any run, ω = [t_0, e] an l-window. Then c_l(s_t) is the same for every t
  ∈ ω, and each of 2l, 2l + 1 moves at most once in ω, to that option.
  - Proof. c_l(s) is a function of the key order of the pair l − 1 under s (R113's definition of c_l), which changes between s_(t−1) and
    s_t exactly at the l-b-steps t; none lies in [t_0 + 1, e]. By ALIGN a member that moves at t ∈ ω moves to c_l(s_t) = c; after it is
    on c, and a second move in ω would again go to c, but a move of a degree-2 mover changes its option. ∎
- Lemma DBL-EQ. Hypotheses: G ∈ 𝓛^R_d, 1 ≤ l ≤ d − 1, any run, p := 2l, q := 2l + 1, Φ := Φ_l.
  - (a) Level l is doubling iff all of: Φ(s_0) = 2; Φ(s_T) = 0; Φ(s_(t−1)) = 0 at every l-b-step t; no step moves both p and q; the
    flip steps of the pair l are exactly the steps that move p or q.
  - (b) If level l is doubling, each of p, q moves exactly once in every l-window; so moves(p) = moves(q) = F(l − 1) + 1.
  - (c) If level l is doubling, γ_l(0) = γ_l(1) =: γ, and in every l-window the first of p, q to move is p iff γ is false.
  - Proof. Write c_t := c_l(s_t), Φ(t) := Φ(s_t), m_t := #(Mv_t ∩ {p, q}), B := the set of l-b-steps (|B| = F(l − 1)).
    - (i) Φ(t) = Φ(t − 1) − m_t if t ∉ B, and Φ(t) = 2 − Φ(t − 1) − m_t if t ∈ B. Indeed c_t = c_(t−1) off B and c_t = 1 − c_(t−1) on B
      (options in {0, 1}); a member that moves at t moves to c_t (ALIGN), so it was off c_t before; a member that does not move keeps
      its option. Summing over t ∈ [1, T]: Σ_t m_t = Φ(0) − Φ(T) + Σ_(t ∈ B) (2 − 2Φ(t − 1)).
    - (ii) A flip of the pair l at a step t with m_t = 0 needs t ∈ B and Φ(t − 1) = 1. Indeed, by ALIGN the order is [s(p) = c_l(s)] if
      s(p) ≠ s(q) and γ_l(j) if both are on j; with no move, both on one option j gives the order γ_l(j) before and after; so they are
      split, exactly one is on c_(t−1), Φ(t − 1) = 1; and off B, c_t = c_(t−1), the order [s(p) = c] is unchanged.
    - (iii) So F(l) ≤ M + B1 with M := #{t : m_t ≥ 1} and B1 := #{t ∈ B : Φ(t − 1) = 1}, and M ≤ Σ_t m_t. With (i): F(l) ≤ Φ(0) − Φ(T) +
      Σ_(t ∈ B) h(Φ(t − 1)), h(0) = 2, h(1) = 0 + 1 = 1, h(2) = −2; and Φ(0) ≤ 2, Φ(T) ≥ 0, h ≤ 2. So F(l) ≤ 2 + 2F(l − 1) (this is R113
      PAIR-DOUBLE, re-proved), with equality iff every inequality is tight: Φ(0) = 2, Φ(T) = 0, h(Φ(t − 1)) = 2 i.e. Φ(t − 1) = 0 at every
      t ∈ B (then B1 = 0), M = Σ m_t (no step moves both), F(l) = M + B1 = M (every flip is at a moving step by (ii) and B1 = 0, and every
      moving step flips). Conversely the five conditions make every inequality an equality. This is (a).
    - (iv) (b): at the first state of every l-window Φ = 2 (for the window starting at 1, Φ(0) = 2; for a window starting at t ∈ B,
      Φ(t − 1) = 0 and c changes at t, so both members are off c_t; a move at t itself is inside the window), and at its end Φ = 0 (at the
      state before the next l-b-step, or at s_T). A member moves only to c (ALIGN), so both members move in the window; by WINDOW-ONCE each
      at most once. There are F(l − 1) + 1 windows.
    - (v) (c): in a window both members start on one option i (off c, so i = 1 − c); their order is γ_l(i) (ALIGN). The first mover A
      goes to c, and the order becomes [s(p) = c] = [A = p]; the second brings both to c, order γ_l(c). By (a) both moving steps flip:
      γ_l(i) ≠ [A = p] ≠ γ_l(c). So γ_l(0) = γ_l(1) and A = p iff ¬γ. ∎
  - Does NOT claim: anything about two consecutive doubling levels (§6 DEAD-DBLGAP); a bound on F.
- Lemma PASS-FREEZE. Hypotheses: G ∈ 𝓛^R_d, 1 ≤ l ≤ d − 2, any run. If neither member of the pair l + 1 moves in the run and they start
  on different options, then F(l + 1) = F(l). Sufficient for «never moves»: for each member x and every state s of the run, every
  option of x other than s_0(x) is not strictly better than (x, s_0(x)) under s (e.g. both options of x have Ξ-target X and ε(x,
  s_0(x)) > ε(x, 1 − s_0(x))).
  - Proof. The members keep distinct options, so by ALIGN the order of their keys under s is [s(2l + 2) = c_(l+1)(s)], with s(2l + 2)
    constant; c_(l+1)(s) is a function of the key order of the pair l, and changes exactly at its flips. Sufficient condition: by R104's
    definition a mover x moves at a step only to an option of A_(s_(t−1))(x) other than its current one, i.e. a strictly better one; if
    s_(t−1)(x) = s_0(x) and no other option is strictly better, x does not move at t; induction on t. With Ξ-targets X the values are the
    constants ε (R105 ENC). ∎
  - Does NOT claim: that freezing a pair of a given run preserves the rest of that run (§7 DATA: it does not in general).

## 3. Lemma HIT and Corollary FUEL-EXACT (PROVED; R104 definition; R105 ENC, MONO, LOCAL)
- Lemma HIT. Hypotheses: IDEAL-ACYC, any degree, any width; y a mover; any run. For every t ∈ [1, T]: cv_(s_t)(y) > cv_(s_(t−1))(y) iff
  some mover of the old chain of y at t moves at t. Hence R(y) = #{t : Mv_t meets the old chain of y} ≥ moves(y).
  - Proof. (⇐) Let z be the first mover of the old chain that moves at t. The movers before z keep their options, so the new chain of
    y has the same prefix up to z, and by ENC cv(y) = (the sum of ε over that prefix) + cv(z) at s_(t−1) and at s_t. z moves to an option
    of A_(s_(t−1))(z) other than its current one (R104), so v_(s_(t−1))(z, s_t(z)) > cv_(s_(t−1))(z); and v(z, k) = ε(z, k) + cv(xt(z,
    k)) is non-decreasing along the run (ENC + MONO; ε(z, k) alone if xt(z, k) = X), so cv_(s_t)(z) = v_(s_t)(z, s_t(z)) ≥ v_(s_(t−1))(z,
    s_t(z)) > cv_(s_(t−1))(z). (⇒) By LOCAL the value of y's option depends only on the states on its chain; if no mover of the old chain
    moves, chain and value are unchanged (and y keeps its option). A move of y itself is the case z = y, so every move of y is a rise. ∎
- Corollary FUEL-EXACT (= FUEL (ii) of the source note). Hypotheses: G ∈ 𝓛^R_d, Ξ-acyclic, 0 ≤ l ≤ d − 1, any run. Then E_l = {t :
  some mover of the old chain at t of some y ∈ U_l moves at t}, and |E_l| ≤ Σ_(y ∈ U_l) R(y).
  - Proof. By MONO a change of cv(y) is a rise; by HIT a rise at t is exactly a move at t on y's old chain. The union over y ∈ U_l gives
    the set; its size is at most the sum of the sizes. ∎

## 4. Lemma ALT-MIN and Lemma TOWER-NEED (PROVED; R105 ENC, MONO; R116 AND-GATE (pending landing); R113 PATH-RISE)
- Lemma ALT-MIN. Hypotheses: IDEAL-ACYC, any degree elsewhere, x a mover of degree 2, any run; y_k := xt(x, k).
  - (a) #{t : π(x) changes at t to k} ≤ R_k(x) for k = 0, 1.
  - (b) PF_x ≤ 2·min(R_0(x), R_1(x)) + 1.
  - (c) moves(x) ≤ 2 + 2·min(R_0(x), R_1(x)).
  - (d) R_k(x) = R(y_k) if y_k is a mover, and R_k(x) = 0 if y_k = X; so if an option of x has Ξ-target X, moves(x) ≤ 2.
  - Proof. (a) By AND-GATE (c) a change of π(x) to b at t has v(x, b) rising strictly at t; distinct changes are at distinct steps. (b)
    π(x) ∈ {0, 1}, so its changes alternate in value and the numbers of changes to 0 and to 1 differ by at most 1: PF_x ≤ 2·min + 1;
    then (a). (c) AND-GATE (b): moves(x) ≤ 1 + PF_x. (d) ENC: v(x, k) = ε(x, k) + cv(y_k) (ε(x, k) alone if y_k = X), ε constant. ∎
  - Does NOT claim: a bound on R (§6 cites L-RED's RISE-2D kill as context); anything at degree ≥ 3.
- Lemma TOWER-NEED. Hypotheses: G ∈ 𝓛^R_d, Ξ-acyclic, 1 ≤ l ≤ d − 1, any run in which level l is doubling, f := F(l − 1), x ∈ {2l,
  2l + 1}. Then moves(x) = f + 1, P(x) ≥ f + 2, and if f ≥ 2 both Ξ-targets of x are movers y with R(y) ≥ (f − 1)/2.
  - Proof. moves(x) = f + 1 by DBL-EQ (b). HIT: moves(x) ≤ R(x); PATH-RISE: R(x) ≤ P(x) − 1. ALT-MIN (c), (d): f + 1 ≤ 2 + 2 min_k R(y_k)
    with R(X) := 0; for f ≥ 2 this forces min_k R(y_k) ≥ (f − 1)/2 > 0, so neither target is X. ∎
  - Does NOT claim: that these necessary conditions are sufficient; a bound on the number of doubling levels.

## 5. CONDITIONAL (not to sign): FUEL-NEED and FUEL (i) depend on L-LOWER's FEEDBACK (b)
- Premise not landed, not refereed, not checked by this lane: Lemma FEEDBACK (b) of docs/lower/L3-families.md §4 (claude/l-lower
  4d747490): on 𝓛^R_d, «a mover of level l ≥ 1 moves at most 2l times in [a, b]» for every [a, b] with [a, b − 1] ∩ E_l = ∅, hence «moves(x)
  ≤ 2·lev(x)·(1 + |E_lev(x)|)».
- FUEL (i): Σ over movers of levels ≤ l of moves ≤ 4l(l + 1)(1 + |E_l|) (F0 at level 0; FEEDBACK (b) at levels 1..l; E_j ⊆ E_l).
- FUEL-NEED: if level h is doubling with f := F(h − 1), then |E_h| ≥ (f + 1)/(2h) − 1 (DBL-EQ (b) and FEEDBACK (b)), and some y ∈ U_h has
  P(y) ≥ 1 + ((f + 1)/(2h) − 1)/|U_h| with |U_h| ≤ 4h (FUEL-EXACT, PATH-RISE, pigeonhole).
- These items are listed so that the dependency is visible; they are NOT to sign until FEEDBACK (b) is refereed.

## 6. DEAD items (instances; machine-replayed by experiments/si/box79/dead79.py, own simulator and, with XCHK, L-NEW's box150 Gen)
- DEAD-MAXPLUS. Both scalar max-plus transfers are false for every constant c ≤ 5: (LEV-ADD c) «in every run on 𝓛^R_d a Ξ-target mover
  of level j ≥ 1 moves at most c times more than the largest number of moves of a mover of level < j»; (DAG-ADD c) «moves(x) ≤ c + max
  over strict Ξ-descendants y of x of moves(y)». Instance experiments/si/box76/inst/dense_d5_l3_H10.json (sha1
  a449d7719000b8f60a3fb41087449c4f79f02abe; byte copy of claude/l-red experiments/red/r214/out/dense_d5_l3_H10.json, commit 36d340c7),
  𝓛^R_5, start 1100110110, T 10: mover 6 (level 3, a Ξ-target) moves 10 times; levels 0-2 and the strict Ξ-descendants of 6 move at most
  4 times each. Check: dead79.py line D1.
- DEAD-DBLGAP. «If levels l and l + 1 are both doubling in a run, then F(l − 1) = 0» is false: experiments/si/box76/inst/lower/
  REC_d10_tower_mu30.json (sha1 cc94dc9c46ef63f7a3a54b536d9d3b38fdee5255; byte copy of claude/l-lower 4d747490
  experiments/lower/l3/kill/REC_d10_tower_mu30.json), 𝓛^R_10, stored start, T 35: F(0..3) = 2, 6, 14, 30, so levels 1, 2, 3 are
  doubling with F(0) = 2. Check: dead79.py line D2.
- DEAD-DECAY. «If level l is doubling and the level l + 1 has no upward option, then F(l + 1) ≤ F(l) − c», for every c ≥ 1, is false:
  experiments/si/box76/inst/passfreeze77_d5.json (sha1 56436bc05a5c35fc1ea33357c3d51290fa43a9f4; built by experiments/si/box76/append77.py from L-NEW's
  climbR_d4_s6, l-new 9995f5a2 experiments/new/box180/out/climbR_d4_s6.json, start 11011111, plus a frozen top pair), 𝓛^R_5, stored
  start 1101111101, T 10: F = 2, 2, 2, 6, 6; level 3 doubling; the pair 4 never moves, has no upward option (top level), and F(4) = F(3).
  Check: dead79.py line D3.
- DEAD-REENTRY. «The movers on the chains of the fuel targets U_l lie at levels > l» is false (static Ξ-graph): REC_d10_tower_mu30 (as
  above): mover 11 (level 5) is the Ξ-target of an upward option of mover 1 (level 0) and has an option with Ξ-target 3 (level 1);
  experiments/si/box76/inst/lower/KILL_M2D_d6_mu13.json (sha1 5301c716f68f219bda2806f29b317c94e0ed5df0, byte copy of claude/l-lower
  4d747490): mover 5 (level 2) is the Ξ-target of an upward option of a mover of level ≤ 1 and has an option with Ξ-target 3 (level 1).
  Check: dead79.py line D4.
- Context, not this packet's kill: «R(y) ≤ 2d for every mover» is L-RED R213's RISE-2D kill (claude/l-red 9eac6d70,
  keep/rise_d5_R13.json); it is why ALT-MIN alone gives no linear bound.

## 7. DATA, machine checks, excluded parts, TARGET diff (not to sign)
- Tool: experiments/si/box79/dblcheck.py (own simulator experiments/si/box76/tw.py Sim). Output frozen in dblcheck.out; control run
  dblcheck_neg2.out; replays dead79.py → dead79.out; all checked by experiments/si/box79/check79.sh (pins --strict).
- Scopes. CORPUS: the 208 𝓛^R_d genomes of the frozen P-IDEAL-MOVES corpus (l-new 9995f5a2, box150-box187; stored in
  experiments/si/box76/corpus_lr.json.gz with git blob sha1s re-hashed at load), every start for N ≤ 10, the stored start otherwise:
  63,223 runs, 140,395 steps. LOWER: L-LOWER 3's nine kill genomes, stored start: 9 runs, 270 steps. Each count covers ONLY the
  statement named; every unit is the one printed by dblcheck.py:
  - WINDOW-ONCE: (run, level, window, member) 577,908 CORPUS / 1,736 LOWER, 0 violations (counter WO); control WO_T (a member moving
    exactly once in a window) 220,641 / 984.
  - DBL-EQ (a): (run, level ≥ 1) 225,647 / 72, 0 (DBLa: doubling iff the five conditions, both directions); doubling (run, level) 4,534 /
    12. (b): (run, doubling level, window, member) 11,052 / 176, 0 (DBLb). (c): every doubling (run, level), 0 (DBLc).
  - PASS-FREEZE: (run, level l ∈ 1..d − 2) with the pair l + 1 never moving and split at s_0: 23,317 CORPUS, 0 (PF); none in LOWER. The
    sufficient condition: no separate DATA.
  - HIT: (run, mover, step) 1,298,948 / 5,216, 0 (HIT); control: under NEG=2 (key-least option ignoring availability) 238,546 violations.
  - FUEL-EXACT: (run, level) 288,870 / 81, 0 (FU2, the set equality; the inequality: no separate DATA); control FU2_T ((run, level) with
    E_l ≠ ∅) 222,089 / 81.
  - ALT-MIN: (run, mover) 577,740 / 162: (a) and (d) per (run, mover, k), 0 (ALTa, ALTd); (b), (c) 0 (ALTb, ALTc); controls: the bounds
    minus 1 fail ALTb_T 112,372 / 43 and ALTc_T 7,085 / 13 times; under NEG=2, ALTa 86,709.
  - TOWER-NEED: (run, doubling level, member) 9,068 / 24, 0 (TN).
  - MP-LIN: no separate DATA (algebra). FUEL-NEED, FUEL (i): CONDITIONAL, no DATA claimed here.
- Lane DATA (not to sign; docs/si/N5-TROPICAL-box76.md §8-§12): L-LOWER's nine genomes replayed by two simulators (MOVES-2D dead);
  freezing an untargeted pair above a doubling level in REC_d12_mu42 / REC_d11_mu40 collapses those runs; |E_l| ≥ 0.77·T for l ≥ 2 on
  the records; R105's RANK grows 3 → 7 with d on the records; annealing found no F(4) = 62 tower.
- EXCLUDED (not to sign): every READING of the source note; FUEL-NEED and FUEL (i) (§5).
- Diff against TARGET.md: no statement mentions a parity game, a winning region, an algorithm's running time or a complexity class.
  Each is about the step sequence of R104's IDEAL model (MP-LIN about max-plus recursions). None is an M3/M4 claim, a gauntlet step, or
  a polynomial bound. G-N5-TIME stays OPEN.

## Freeze steps (after R116 lands)
1. Re-quote AND-GATE (a)-(c) from the landed R116 text in §0; if the landed wording differs, update the quotes only.
2. Re-run experiments/si/box79/check79.sh; commit the frozen packet with its line L-1; from then on changes go to a fixes file only.
