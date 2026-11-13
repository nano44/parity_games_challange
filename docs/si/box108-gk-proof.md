# Box 108 (D18 / D25; item 1 of the Lead's 2026-11-13 brief to successor 56): an INDEPENDENT proof that L(G_k) = 2^k − 2 on RESULTS R104's IDEAL model — Theorem GK, by an explicit closed form of the run
L-SI successor 56 (session_01V5yGRWzAPTWfgNSJqHbXjx), D1 / D18 / D25. Lead brief (quoted): «an INDEPENDENT PROOF that L(G_k) = 2^k − 2
for every k ≥ 3 (or the exact k and step at which the rule breaks), written from the rule above and R104's definition of the IDEAL
step ONLY»; «find the invariant (the «window» of a level, T(k + 1) = 2·T(k) + 2 from T(3) = 6, which mover moves at which step and why
no other mover can), check it by script on k = 3..12 with a firing control BEFORE writing the induction»; «write the induction with
every «nothing else moves» clause proved …, and say exactly where the start and each ε / rank order is used».
Labels: PROVED (L-SI lane, unrefereed) / DATA (counter, unit, set, scope) / OPEN.
**SCOPE LINE: nothing here is a TARGET.md claim, M3 or M4, or a gauntlet step. G-N5-TIME stays OPEN. Every statement is about the
IDEAL model of RESULTS R104 (docs/red/P-N5-REALIZE.md §2) on the genomes G_k. What L(G_k) means for N5 itself is the business of the
landed RESULTS R104 / R117 and of the referees of packet P-N5-EXP; no statement about N5 on a parity game is made or used here.**
D1 (owner, verbatim): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the
fleet's own, as wrong until it passes the gauntlet below.» Applied in mirror form: the kill candidate is treated as unproved until a
second derivation exists; this file is that second derivation.
INDEPENDENCE: written from the Lead's rule (§1.2) and R104's definition (§1.1) only. NOT READ before this file was committed:
claude/l-red-b (its proof, its B6b files, P-N5-EXP), docs/referee*/ on G_k, docs/red/R245. Tools read: L-NEW's one217.py (claude/l-new
a143d4060, the simulator named in the brief), used as a second engine only.

## 0. Result
- **Theorem GK (PROVED, lane).** For every k ≥ 3: L(G_k) = 2^k − 2, where L is R104's «L(G) := the number of IDEAL steps from s_0»
  (§1.1) and G_k is the genome of §1.2. The state after t IDEAL steps is the closed form c_k(t) of §3 (0 ≤ t ≤ 2^k − 2). The run stops
  by R104's clause «If s' = s, the run STOPS («stuck»)», with exactly v_1, …, v_(k−1) unstable and held.
- **Corollary SW (PROVED, lane).** v0 and the four movers u_1, v_1, y_1, yb_1 switch once; each of the seven movers of a middle
  level i (2 ≤ i ≤ k − 2) switches 2^(i−1) times; each of the four top movers u_(k−1), v_(k−1), y_(k−1), yb_(k−1) switches 2^(k−2)
  times; u0 and the wires never switch. Total 11·2^(k−2) − 9 switches; max_x sw(x) = 2^(k−2). With N = 9k − 16: L = 2^((N+16)/9) − 2.
- The proof is NOT an induction on k. It verifies that c_k(t + 1) satisfies the defining equations of the IDEAL step at c_k(t), mover
  by mover (§5, §6); the step is determined level by level, so this identifies the run. The verification is finite because each level's
  inputs are functions of its own phase (Lemma INPUT): 8 + 17 + 7 = 32 transition classes with one parameter h.
- DATA (§9): `experiments/si/box108/check108.py`, k = 3..12: the closed form equals the simulated run at every t; every static lemma
  is checked against the definition on all run states and on 200 random states per k; 19 controls fire as predicted.

## 1. Setting
### 1.1 The IDEAL model (RESULTS R104; docs/red/P-N5-REALIZE.md §2, quoted)
«movers x = 0, …, N − 1, each with a level lev(x) … and options k = 0, …, deg(x) − 1»; «per option (x, k): a W-target wt(x, k),
which is a mover of level lev(x) − 1 if lev(x) ≥ 1 and «none» if lev(x) = 0 (GRADED); a Ξ-target xt(x, k) ∈ {movers} ∪ {X}; a β-id
b(x, k)»; «a gate index gate(x, k), a bijection of the options onto 0..M − 1»; «per β-id b: a rank br(b) (a bijection onto 0..M − 1)
and a parity bp(b) ∈ {0, 1}»; «a start s_0».
«The X-CHAIN of a face (x, k) is the sequence of options (x, k) = (x_0, k_0), (x_1, k_1), … with x_(i+1) := xt(x_i, k_i) and
k_(i+1) := s(x_(i+1)), ending at the first option whose Ξ-target is X … B_s(x, k) := the set of β-ids of the chain.»
«(x, k) ▷_s (x, k') iff the β-id of LARGEST rank in B_s(x, k) Δ B_s(x, k') has parity 0 and lies in B_s(x, k), or has parity 1 and lies
in B_s(x, k').»
«IDEAL step from s. Availability A_s(x) := {s(x)} ∪ {k : (x, k) ▷_s (x, s(x))}. … If |A_s(x)| = 1 for every x, the run STOPS («opt»).
… Otherwise s' is defined level by level, lev = 0, 1, …: key(x, k) := (gate(x, k)) if lev(x) = 0, and key_(s')(wt(x, k), s'(wt(x, k)))
followed by gate(x, k) otherwise (a tuple of length lev(x) + 1); s'(x) := the k ∈ A_s(x) with the lexicographically least key. … If
s' = s, the run STOPS («stuck»). … Otherwise s → s' is one IDEAL step. L(G) := the number of IDEAL steps from s_0».
(The quotes of this subsection are compared with docs/red/P-N5-REALIZE.md by `experiments/si/box108/quotes108.py`; «…» marks an omission.)
Notation here: B_s(x, o) as quoted; val_s(z) := B_s(z, s(z)); key_s(x, o) as quoted with s in place of s′; key_s(x) := key_s(x, s(x)).
For two β-sets A ≠ B write A ▷ B iff the largest-rank element of A Δ B lies in A (all parities are 0 in G_k).

### 1.2 The family G_k, k ≥ 3 (the Lead's rule, restated; builder `experiments/si/box108/gk108.py`)
Movers (N = 9k − 16), with level lev, class number dep, and per option o ∈ {0, 1}: W-target, Ξ-target (X = exit), ε, dl; start.
The gate index is 100·lev + ε, the β-rank is the position of (2k + 5 − dep, dl, β-id) in increasing lexicographic order (so a SMALLER
dep is a HIGHER rank class, and inside a class a larger dl is a higher rank); every parity is 0.

| mover | range | lev | dep | W-target (o = 0, 1) | Ξ-target (o = 0, 1) | ε | dl | start |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| u_0 | | 0 | 0 | none | X, X | 2, 5 | 2, 0 | 0 |
| v_0 | | 0 | 0 | none | X, X | 3, 1 | 1, 3 | 0 |
| u_j | 1 ≤ j ≤ k−1 | j | 2j | u_(j−1), v_(j−1) | yb_j, y_j | 2, 3 | 1, 0 | 0 |
| v_j | 1 ≤ j ≤ k−1 | j | 2j | u_(j−1), v_(j−1) | y_j, yb_j | 4, 5 | 3, 2 | 0 |
| e_j | 2 ≤ j ≤ k−2 | j | 2j+1 | u_(j−1), v_(j−1) | ypb_j, yp_j | 0, 1 | 4, 5 | 0 |
| wv_j | 1 ≤ j ≤ k−2 | j+1 | 2k+5 | v_j, v_j | X, X | 6, 7 | 1, 0 | 0 |
| wu_j | 2 ≤ j ≤ k−2 | j+1 | 2k+5 | u_j, u_j | X, X | 8, 9 | 3, 2 | 0 |
| y_j | 1 ≤ j ≤ k−2 | j+2 | 2j−1 | wv_j, E(j+1) | u_(j−1), v_(j−1) | 10, 11 | 1, 3 | 0 |
| yb_j | 1 ≤ j ≤ k−2 | j+2 | 2j−1 | wv_j, E(j+1) | v_(j−1), u_(j−1) | 12, 13 | 0, 2 | 1 |
| y_(k−1) | | k | 2k−3 | u_(k−1), v_(k−1) | u_(k−2), v_(k−2) | 20, 21 | 1, 3 | 0 |
| yb_(k−1) | | k | 2k−3 | u_(k−1), v_(k−1) | v_(k−2), u_(k−2) | 22, 23 | 0, 2 | 1 |
| yp_j | 2 ≤ j ≤ k−2 | j+2 | 2j | wu_j, E(j+1) | yb_j, y_j | 14, 15 | 5, 7 | 0 |
| ypb_j | 2 ≤ j ≤ k−2 | j+2 | 2j | wu_j, E(j+1) | y_j, yb_j | 16, 17 | 4, 6 | 1 |

E(j) := e_j for 2 ≤ j ≤ k − 2 and E(k − 1) := u_(k−1). Names: B_j := (u_j, v_j) the BLOCK PAIR of index j; Y_j := (y_j, yb_j);
Y′_j := (yp_j, ypb_j); wv_j, wu_j the WIRES. «Level i» below means the GADGET of index i: B_i, Y_i and (for 2 ≤ i ≤ k − 2) Y′_i, e_i;
its movers sit on W-levels i and i + 2 (top: k − 1 and k). Level 1 is the BOTTOM gadget (B_1, Y_1), level k − 1 the TOP gadget
(B_(k−1), Y_(k−1)), levels 2..k − 2 the MIDDLE gadgets (none for k = 3).
Rebuild check (sha1 of json.dumps of the genome, keys N, lev, deg, opts, gate, br, bp, start): G_3 cd3cd7e3…, G_4 7a2218bf…,
G_8 d3ad8e2e…, G_10 da29d33e… (all four equal the Lead's values; `check108.py`, counter SHA).
**Well-formed (R104's conditions).** GRADED: every W-target has level lev − 1 (u_j, v_j, e_j: j − 1; wv_j, wu_j: j; y_j, yb_j, yp_j, ypb_j
with j ≤ k − 2: wv_j, wu_j, E(j + 1) all have level j + 1; top latches: k − 1). Gate indices are distinct: on W-level ℓ the movers
present have the ε-pairs {2,3} / {2,5} (u), {4,5} / {3,1} (v), {0,1} (e_ℓ), {6,7} (wv_(ℓ−1)), {8,9} (wu_(ℓ−1)), {10,11}, {12,13}
(Y_(ℓ−2)), {14,15}, {16,17} (Y′_(ℓ−2)), {20..23} (top latches, ℓ = k), pairwise disjoint; R104 wants a bijection onto 0..M − 1, and the
order-preserving renumbering changes no comparison. Ranks are distinct by construction.
**Fact DEP (Ξ-acyclic, ranks rise along chains).** Every Ξ-edge x → z has dep(z) < dep(x): B_j (2j) → Y_j (2j − 1) → B_(j−1) (2j − 2);
Y′_j (2j) → Y_j (2j − 1); e_j (2j + 1) → Y′_j (2j). Hence the Ξ-graph is acyclic (G_k ∈ IDEAL-ACYC), and for every mover z every β in
val_s(z) belongs to a mover of dep ≤ dep(z), with equality only for β(z, s(z)).

## 2. Static lemmas (every state s; no run is involved)
**Lemma LATCH (two-input latch form; uses: degree 2, R104's step).** For a mover x let pref_s(x) be the option o with
B_s(x, o) ▷ B_s(x, 1 − o), and kmin_s′(x) the option with the lexicographically smaller key under s′. Both are well defined (R104's
Fact X: the two β-sets differ; the two keys have equal length and distinct last entries). Let s′ be the state given by R104's
level-by-level rule at s (read also when every |A_s(x)| = 1, where it gives s′ = s). A state c equals s′ iff for every mover x
  (EQ)  c(x) = s(x) if pref_s(x) = s(x), and c(x) = kmin_c(x) otherwise.
*Proof.* A_s(x) = {s(x)} if pref_s(x) = s(x) and {0, 1} otherwise. s′ satisfies (EQ) by definition. Conversely let c satisfy (EQ);
by induction on the W-level ℓ, c = s′ on all movers of level < ℓ implies key_c(x, o) = key_s′(x, o) for x of level ℓ (a key reads
the state only on lower levels), hence c(x) = s′(x). ∎
A mover with pref_s(x) = s(x) is STABLE; otherwise it is UNSTABLE, and it is HELD if kmin_s′(x) = s(x) and MOVES if not.

**Lemma CMP (uses: Fact DEP).** (a) Let x have the two Ξ-targets z_0 ≠ z_1 (movers) with dep(z_0) = dep(z_1) < dep(x). Then
val_s(z_0) ≠ val_s(z_1), and pref_s(x) = o iff val_s(z_o) ▷ val_s(z_(1−o)). (b) Let z_0 ≠ z_1 be movers of equal dep whose current
options have Ξ-targets t_0, t_1. If t_0 = t_1 (or both are X) then val_s(z_0) ▷ val_s(z_1) iff β(z_0, s(z_0)) has the larger dl.
If t_0 ≠ t_1 are movers of equal dep then val_s(z_0) ▷ val_s(z_1) iff val_s(t_0) ▷ val_s(t_1).
*Proof.* (a) B_s(x, o) = {β(x, o)} ⊔ val_s(z_o). By DEP, β(z_0, s(z_0)) ∈ val_s(z_0) ∖ val_s(z_1) (the other elements of val_s(z_1)
have dep < dep(z_1) or are β(z_1, ·)), and neither β(x, ·) lies in val_s(z_0) ∪ val_s(z_1). So B_s(x, 0) Δ B_s(x, 1) =
{β(x, 0), β(x, 1)} ⊔ (val_s(z_0) Δ val_s(z_1)), the second part is non-empty and every element of it has dep < dep(x), i.e. outranks
both β(x, ·). (b) val_s(z_i) = {β(z_i, s(z_i))} ⊔ val_s(t_i). If t_0 = t_1 the difference is the two first elements, of equal dep,
ordered by dl. If t_0 ≠ t_1, as in (a) the largest element of the difference lies in val_s(t_0) Δ val_s(t_1). ∎

Signals of a state s (letters): P_j ∈ {u, v}: P_j = u iff val_s(u_j) ▷ val_s(v_j). K_j ∈ {u, v}: K_j = u iff key_s(u_j) < key_s(v_j).
Q_j ∈ {y, yb}: Q_j = y iff val_s(y_j) ▷ val_s(yb_j). R_j ∈ {yp, ypb}: R_j = yp iff val_s(yp_j) ▷ val_s(ypb_j). (The compared sets and
keys always differ: CMP (a)'s first claim; gate indices of one level are distinct.) Bits: X_0 := [s(v_0) = 1], X_j := [s(u_j) ≠ s(v_j)]
(j ≥ 1), E(j)(s) := s(E(j)).

**Ξ side (Lemmas X0–X7; all from CMP).** Below (a, b) := (s(y_j), s(yb_j)), (c, d) := (s(yp_j), s(ypb_j)).
- X0 (uses dl(u_0,0) > dl(u_0,1); dl(v_0,1) > dl(u_0,0) > dl(v_0,0)). pref(u_0) = 0, pref(v_0) = 1. If s(u_0) = 0: P_0 = u iff s(v_0) = 0.
- X1 (uses dl(yb_j,1) > dl(y_j,0), dl(y_j,1) > dl(yb_j,0); DEP). y_j points at u_(j−1) iff a = 0; yb_j points at u_(j−1) iff b = 1. So
  (a, b) = (0, 1): Q_j = yb. (1, 0): Q_j = y. (0, 0): Q_j = y iff P_(j−1) = u. (1, 1): Q_j = y iff P_(j−1) = v.
- X2. pref(y_j) = 0 iff P_(j−1) = u. pref(yb_j) = 0 iff P_(j−1) = v.
- X3. pref(u_j) = 0 iff Q_j = yb. pref(v_j) = 0 iff Q_j = y. (j ≥ 1.)
- X4 (uses dl(v_j,·) > dl(u_j,·)). If s(u_j) ≠ s(v_j) (both point at the same latch): P_j = v. If s(u_j) = s(v_j) = 0: P_j = u iff
  Q_j = yb. If s(u_j) = s(v_j) = 1: P_j = u iff Q_j = y.
- X5 (uses dl(ypb_j,1) > dl(yp_j,0), dl(yp_j,1) > dl(ypb_j,0)). pref(yp_j) = 0 iff Q_j = yb; pref(ypb_j) = 0 iff Q_j = y. yp_j points at
  yb_j iff c = 0; ypb_j points at yb_j iff d = 1. So (c, d) = (0, 1): R_j = ypb. (1, 0): R_j = yp. (0, 0): R_j = yp iff Q_j = yb.
  (1, 1): R_j = yp iff Q_j = y.
- X6. pref(e_j) = 0 iff R_j = ypb.
- X7 (uses dl(w,0) > dl(w,1) for the wires). pref(wv_j) = pref(wu_j) = 0.
*Proofs.* X0, X7: both options have Ξ-target X, so the β-sets are singletons of one class, ordered by dl. X2, X3, X6, first half of
X5: CMP (a) with (z_0, z_1) the two Ξ-targets (a pair B_(j−1), Y_j or Y′_j of equal dep below dep(x)). X1, X4, second half of X5:
CMP (b) for the pair; the «same target» cases are (a, b) ∈ {(0,1), (1,0)}, s(u_j) ≠ s(v_j), (c, d) ∈ {(0,1), (1,0)}, decided by dl
(yb_j,1 : 2 > y_j,0 : 1; y_j,1 : 3 > yb_j,0 : 0; v_j : {3,2} > u_j : {1,0}; ypb_j,1 : 6 > yp_j,0 : 5; yp_j,1 : 7 > ypb_j,0 : 4); the
«different targets» cases reduce to the pair below (P_(j−1) for Y_j, Q_j for B_j and Y′_j). ∎

**Key side (Lemmas K0–K6; n denotes the state under which keys are read, the NEW state in a step).**
- K0 (uses ε(v_0,1) < ε(u_0,0) < ε(v_0,0)). kmin(v_0) = 1 (ε 1 < 3; kmin(u_0) = 0 is not needed). If n(u_0) = 0: K_0 = u iff n(v_0) = 0.
- K1. For x ∈ {u_j, v_j, e_j} (j ≥ 1): kmin_n(x) = 0 iff K_(j−1)(n) = u.
- K2 (uses ε(u_j,·) < ε(v_j,·)). If n(u_j) = n(v_j): K_j = u. If (n(u_j), n(v_j)) = (0, 1): K_j = K_(j−1). If (1, 0): K_j = u iff K_(j−1) = v.
- K3. If the wires are at option 0: key_n(wv_j) = key_n(v_j)·(100(j+1) + 6), key_n(wu_j) = key_n(u_j)·(100(j+1) + 8).
- K4 (uses ε(E(j+1),1) < ε(wv_j,0): 1 or 3 < 6; wires at 0). For j ≤ k − 2: kmin_n(y_j) = kmin_n(yb_j) = 1 iff [E(j+1)(n) = 1 or K_j(n) = u].
- K5 (uses ε(E(j+1),0) < ε(wu_j,0): 0 or 2 < 8; wires at 0). For 2 ≤ j ≤ k − 2: kmin_n(yp_j) = kmin_n(ypb_j) = 1 iff [E(j+1)(n) = 0 or K_j(n) = v].
- K6. kmin_n(y_(k−1)) = kmin_n(yb_(k−1)) = 0 iff K_(k−1)(n) = u.
*Proofs.* K0: keys of level 0 are the single gate indices. K1: key_n(x, o) = key_n(m_o)·gate(x, o) with (m_0, m_1) = (u_(j−1), v_(j−1));
the two prefixes are different tuples of equal length, so they decide. K2: key_n(u_j) = key_n(m)·(100j + 2 or 3), key_n(v_j) =
key_n(m′)·(100j + 4 or 5) with m, m′ the current W-targets; if m = m′ the last entry decides (u smaller); if not, the prefixes
key_n(u_(j−1)), key_n(v_(j−1)) decide, and u_j's W-target is u_(j−1) iff n(u_j) = 0. K3: both options of a wire have the same
W-target. K4: key(·, 0) = key_n(v_j)·(100(j+1) + 6)·g and key(·, 1) = key_n(m)·gate(E(j+1), n(E(j+1)))·g′ with m = u_j if
n(E(j+1)) = 0 and m = v_j if n(E(j+1)) = 1 (E(j+1) ∈ {e_(j+1), u_(k−1)} has the W-targets (u_j, v_j)). If m = v_j the first j + 1
entries agree and entry j + 2 is 100(j+1) + (1 or 3) < 100(j+1) + 6: option 1. If m = u_j the first j + 1 entries are key_n(u_j) and
key_n(v_j): option 1 iff K_j = u. K5: the same with wu_j → u_j: if m = u_j, entry j + 2 is 100(j+1) + (0 or 2) < 100(j+1) + 8: option 1;
if m = v_j: option 1 iff key_n(v_j) < key_n(u_j). K6: the two W-targets are u_(k−1), v_(k−1). ∎
The latches' own ε (10..17, 20..23) never decide: their two keys differ at an earlier entry.

## 3. The closed form c_k(t)
H_i := 2^(k−i+1) − 1 for 1 ≤ i ≤ k − 1; so H_(k−1) = 3 and H_i = 2·H_(i+1) + 1. T_k := 2^k − 2 = 2·H_2 = H_1 − 1.
PHASES of a time t ∈ [0, T_k]: τ_1(t) := t and τ_(i+1)(t) := τ_i(t) mod H_i for 1 ≤ i ≤ k − 2. So τ_2(t) = t (as t < H_1) and
0 ≤ τ_i(t) ≤ 2·H_i for every i ≥ 2 (τ_(i+1) ≤ H_i − 1 = 2·H_(i+1)).
POSITIONS (local states written u v | y yb | yp ypb | e):

| pos | S0 | S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8 | S9 | S10 | S11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| state | 00 01 01 0 | 01 01 01 0 | 01 00 01 0 | 01 10 01 0 | 11 10 00 0 | 11 10 10 0 | 11 10 10 1 | 10 10 10 1 | 10 00 10 1 | 10 01 10 1 | 00 01 00 1 | 00 01 01 1 |
| moved | (e↓) | v↑ | yb↓ | y↑ | u↑ ypb↓ | yp↑ | e↑ | v↓ | y↓ | yb↑ | u↓ yp↓ | ypb↑ |

pos(τ; h), for h ≥ 3 and 0 ≤ τ ≤ 4h + 2: S0 at τ ∈ {0, 4h + 2}; S1 at 1; S2 on [2, h − 1]; S3 at h; S4 on [h + 1, 2h − 1]; S5 at 2h;
S6 at 2h + 1; S7 at 2h + 2; S8 on [2h + 3, 3h]; S9 at 3h + 1; S10 on [3h + 2, 4h]; S11 at 4h + 1.
Top positions (u v | y yb): T0 = 00 01, T1 = 01 01, T2 = 01 11, T3 = 11 10, T4 = 10 10, T5 = 10 11, T6 := T0.
**Definition of c_k(t)** (0 ≤ t ≤ T_k): u_0 = 0, v_0 = [t ≥ 1]; every wire at 0; level 1: (u_1, v_1, y_1, yb_1) := the first four
entries of pos(t; H_2) (only S0..S5 occur since t ≤ 2·H_2; S4 and S5 agree on these entries; call them A0..A4, A4 on [H_2 + 1, 2·H_2]);
middle level i (2 ≤ i ≤ k − 2): its seven movers are at pos(τ_i(t); H_(i+1)); top level: (u, v, y, yb)_(k−1) at T_(τ_(k−1)(t)).
c_k(0) is the start of G_k: all phases are 0, so every level is at S0 / T0 = (u, v, y, yb, yp, ypb, e) = (0, 0, 0, 1, 0, 1, 0),
v_0 = 0, wires 0. **This is the only use of the start** (each of its bits).

## 4. Phase lemmas
**Lemma PHASE.** For 0 ≤ t < T_k and 2 ≤ i ≤ k − 1 exactly one holds: (a) τ_i(t + 1) = τ_i(t) + 1 ≤ 2·H_i; (b) τ_i(t) = 2·H_i and
τ_i(t + 1) = 0; (c) τ_i(t) = τ_i(t + 1) = 0. Level 2 is always in case (a). If level i is in case (a) then level i + 1 is in case (a),
or τ_i(t) ∈ {H_i − 1, 2·H_i − 1} and level i + 1 is in case (b). If level i is in case (b) or (c), level i + 1 is in case (c).
*Proof.* τ_2 = t. If τ_i(t + 1) = τ_i(t) + 1 then τ_(i+1)(t + 1) = (τ_i(t) + 1) mod H_i, which is τ_(i+1)(t) + 1 unless
τ_i(t) + 1 ∈ {H_i, 2·H_i}, where τ_(i+1)(t) = H_i − 1 = 2·H_(i+1) and τ_(i+1)(t + 1) = 0. If τ_i(t) ∈ {0, 2·H_i} and τ_i(t + 1) = 0
then τ_(i+1)(t) = τ_(i+1)(t + 1) = 0. ∎
In cases (b) and (c) the level is at S0 (T0) before and after: pos(2·H_i) = pos(0) (2·H_i = 4h + 2 with h = H_(i+1); top: T6 = T0).

**Lemma INPUT (a level's inputs are functions of its own phase).** At c_k(t), with h := H_(i+1) where i ≤ k − 2:
 (i) for 2 ≤ i ≤ k − 1: X_(i−1) = 1 iff τ_i(t) ∈ [1, H_i]; for i = 1: X_0 = 1 iff t ≥ 1;
 (ii) for 1 ≤ i ≤ k − 2: E(i + 1) = 1 iff τ_i(t) mod H_i ∈ [h, 2h − 1], i.e. iff τ_i(t) ∈ [h, 2h − 1] ∪ [3h + 1, 4h] (for i = 1: t ∈ [h, 2h − 1]);
 (iii) X_i = 1 iff τ_i(t) ∈ [1, h] ∪ [2h + 2, 3h + 1] (middle), τ_(k−1)(t) ∈ {1, 2, 4, 5} (top), t ∈ [1, H_2] (level 1).
*Proof.* (iii): u ≠ v exactly at S1, S2, S3, S7, S8, S9, at T1, T2, T4, T5. (i): for i = 2, τ_2 = t and (iii) for level 1. For i ≥ 3,
level i − 1 is a middle level with its own parameter H_i: by (iii) X_(i−1) = 1 iff τ_(i−1) ∈ [1, H_i] ∪ [H_(i−1) + 1, H_(i−1) + H_i]
(2·H_i + 2 = H_(i−1) + 1); and τ_i = τ_(i−1) on [0, H_(i−1) − 1], τ_i = τ_(i−1) − H_(i−1) on [H_(i−1), 2·H_(i−1) − 1], τ_i = 0 at
2·H_(i−1). (ii): the phase of level i + 1 is τ_(i+1) = τ_i mod H_i ∈ [0, 2h]. If i + 1 ≤ k − 2: e_(i+1) = 1 exactly at S6..S11, i.e.
(with h′ := H_(i+2), h = 2h′ + 1) for τ_(i+1) ∈ [2h′ + 1, 4h′ + 1] = [h, 2h − 1]. If i + 1 = k − 1: u_(k−1) = 1 exactly at T3, T4, T5,
τ_(k−1) ∈ [3, 5] = [h, 2h − 1] with h = 3. ∎

**Lemma SIG (one bit per level).** At every c_k(t) and for every 0 ≤ j ≤ k − 1: P_j = K_j = v if X_j = 1, and P_j = K_j = u if X_j = 0.
*Proof.* j = 0: X0, K0 (u_0 = 0). j ≥ 1, K_j by K2 and induction on j: if u_j = v_j then K_j = u. (u_j, v_j) = (0, 1) occurs at S1..S3,
T1, T2, A1..A3, i.e. τ_j ∈ [1, h], {1, 2}, t ∈ [1, H_2], all inside [1, H_j] (resp. t ≥ 1), where X_(j−1) = 1 by INPUT (i), so
K_j = K_(j−1) = v. (1, 0) occurs at S7..S9, T4, T5, i.e. τ_j ∈ [H_j + 1, H_j + h], {4, 5}, outside [1, H_j], where X_(j−1) = 0 and
K_j = v since K_(j−1) = u. P_j by X4 and X1: if u_j ≠ v_j then P_j = v. u_j = v_j = 0 occurs at S0, S10, S11, T0, A0, where
(y_j, yb_j) = (0, 1), so Q_j = yb and P_j = u. u_j = v_j = 1 occurs at S4, S5, S6, T3, A4, where (y_j, yb_j) = (1, 0), Q_j = y, P_j = u. ∎

**Phase tables** (the signals each mover reads, at c_k(t); from the positions, INPUT, SIG, X1, X5; Xb := X_(i−1), E := E(i+1), Xi := X_i).
Middle level i, τ = τ_i(t), h = H_(i+1) ≥ 3:

| τ | pos | u v y yb yp ypb e | Q_i | R_i | Xb | E | Xi |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0, 4h+2 | S0 | 0 0 0 1 0 1 0 | yb | ypb | 0 | 0 | 0 |
| 1 | S1 | 0 1 0 1 0 1 0 | yb | ypb | 1 | 0 | 1 |
| [2, h−1] | S2 | 0 1 0 0 0 1 0 | yb (∗) | ypb | 1 | 0 | 1 |
| h | S3 | 0 1 1 0 0 1 0 | y | ypb | 1 | 1 | 1 |
| [h+1, 2h−1] | S4 | 1 1 1 0 0 0 0 | y | ypb (∗∗) | 1 | 1 | 0 |
| 2h | S5 | 1 1 1 0 1 0 0 | y | yp | 1 | 0 | 0 |
| 2h+1 | S6 | 1 1 1 0 1 0 1 | y | yp | 1 | 0 | 0 |
| 2h+2 | S7 | 1 0 1 0 1 0 1 | y | yp | 0 | 0 | 1 |
| [2h+3, 3h] | S8 | 1 0 0 0 1 0 1 | y (∗) | yp | 0 | 0 | 1 |
| 3h+1 | S9 | 1 0 0 1 1 0 1 | yb | yp | 0 | 1 | 1 |
| [3h+2, 4h] | S10 | 0 0 0 1 0 0 1 | yb | yp (∗∗) | 0 | 1 | 0 |
| 4h+1 | S11 | 0 0 0 1 0 1 1 | yb | ypb | 0 | 0 | 0 |

(∗) (y, yb) = (0, 0): Q_i = y iff P_(i−1) = u iff Xb = 0 (X1, SIG). (∗∗) (yp, ypb) = (0, 0): R_i = yp iff Q_i = yb (X5). Xb = 1 iff
τ ∈ [1, 2h + 1]; E = 1 iff τ mod (2h + 1) ∈ [h, 2h − 1]; both by INPUT.
Top level, τ = τ_(k−1)(t) (Xb = X_(k−2), Xi = X_(k−1); Xb = 1 iff τ ∈ [1, 3]):

| τ | pos | u v y yb | Q | Xb | Xi |
| --- | --- | --- | --- | --- | --- |
| 0, 6 | T0 | 0 0 0 1 | yb | 0 | 0 |
| 1 | T1 | 0 1 0 1 | yb | 1 | 1 |
| 2 | T2 | 0 1 1 1 | y (∗) | 1 | 1 |
| 3 | T3 | 1 1 1 0 | y | 1 | 0 |
| 4 | T4 | 1 0 1 0 | y | 0 | 1 |
| 5 | T5 | 1 0 1 1 | yb (∗) | 0 | 1 |

(∗) (y, yb) = (1, 1): Q = y iff P_(k−2) = v iff Xb = 1 (X1, SIG).
Level 1, phase t, h = H_2 (Xb = X_0 = [t ≥ 1], E = E(2) = 1 iff t ∈ [h, 2h − 1], Xi = X_1):

| t | pos | u v y yb | Q_1 | Xb | E | Xi |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | A0 | 0 0 0 1 | yb | 0 | 0 | 0 |
| 1 | A1 | 0 1 0 1 | yb | 1 | 0 | 1 |
| [2, h−1] | A2 | 0 1 0 0 | yb (∗) | 1 | 0 | 1 |
| h | A3 | 0 1 1 0 | y | 1 | 1 | 1 |
| [h+1, 2h−1] | A4 | 1 1 1 0 | y | 1 | 1 | 0 |
| 2h | A4 | 1 1 1 0 | y | 1 | 0 | 0 |

(∗) (y, yb) = (0, 0): Q_1 = y iff P_0 = u iff Xb = 0.

## 5. The transition tables and Lemma STEP
For a step from s := c_k(t) to n := c_k(t + 1) (and for the STOP step: t = T_k, n := s) every mover's two latch inputs follow from
§2 and SIG, read off the phase tables (old row for pref, new row for kmin):
 (F1) pref_s: u_i: 0 iff Q_i = yb. v_i: 0 iff Q_i = y. e_i: 0 iff R_i = ypb. yp_i: 0 iff Q_i = yb. ypb_i: 0 iff Q_i = y.
      y_i: = Xb(old). yb_i: = 1 − Xb(old).     (X3, X6, X5, X2 with P_(i−1) = v iff Xb = 1)
 (F2) kmin_n: u_i, v_i, e_i: = Xb(new). y_i, yb_i: = [E(new) = 1 or Xi(new) = 0] for i ≤ k − 2, and = Xi(new) for i = k − 1.
      yp_i, ypb_i: = [E(new) = 0 or Xi(new) = 1].     (K1, K4, K6, K5 with K_j = v iff X_j = 1; the wires are at 0 in every c_k(t))
Cell format: `m:c pP -` = mover m is at option c, pref = P = c: STABLE. `m:c pP kK hold` = unstable (P ≠ c), kmin = K = c: HELD.
`m:c pP kK ->K` = unstable and kmin = K ≠ c: MOVES to K. By LATCH these three cases are exhaustive and give the new option.
The rows below are machine-generated (`check108.py --table`, one row per class over all k = 3..12, all levels, all t) and each cell
can be recomputed by hand from (F1), (F2) and the phase tables; the hand recomputation is the proof, the script is the typo guard.

```
bot A0->A1         | old Q=yb Xb=0 | new Xb=1 E=0 Xi=1 | u:0 p0 - | v:0 p1 k1 ->1 | y:0 p0 - | yb:1 p1 -
bot A1->A2         | old Q=yb Xb=1 | new Xb=1 E=0 Xi=1 | u:0 p0 - | v:1 p1 - | y:0 p1 k0 hold | yb:1 p0 k0 ->0
bot A2 stay        | old Q=yb Xb=1 | new Xb=1 E=0 Xi=1 | u:0 p0 - | v:1 p1 - | y:0 p1 k0 hold | yb:0 p0 -
bot A2->A3         | old Q=yb Xb=1 | new Xb=1 E=1 Xi=1 | u:0 p0 - | v:1 p1 - | y:0 p1 k1 ->1 | yb:0 p0 -
bot A3->A4         | old Q=y Xb=1 | new Xb=1 E=1 Xi=0 | u:0 p1 k1 ->1 | v:1 p0 k1 hold | y:1 p1 - | yb:0 p0 -
bot A4 stay (E=1)  | old Q=y Xb=1 | new Xb=1 E=1 Xi=0 | u:1 p1 - | v:1 p0 k1 hold | y:1 p1 - | yb:0 p0 -
bot A4 stay (E=0)  | old Q=y Xb=1 | new Xb=1 E=0 Xi=0 | u:1 p1 - | v:1 p0 k1 hold | y:1 p1 - | yb:0 p0 -
bot A4 stay (stop) | old Q=y Xb=1 | new Xb=1 E=0 Xi=0 | u:1 p1 - | v:1 p0 k1 hold | y:1 p1 - | yb:0 p0 -
mid S0->S1         | old Q=yb R=ypb Xb=0 | new Xb=1 E=0 Xi=1 | u:0 p0 - | v:0 p1 k1 ->1 | y:0 p0 - | yb:1 p1 - | yp:0 p0 - | ypb:1 p1 - | e:0 p0 -
mid S1->S2         | old Q=yb R=ypb Xb=1 | new Xb=1 E=0 Xi=1 | u:0 p0 - | v:1 p1 - | y:0 p1 k0 hold | yb:1 p0 k0 ->0 | yp:0 p0 - | ypb:1 p1 - | e:0 p0 -
mid S2 stay        | old Q=yb R=ypb Xb=1 | new Xb=1 E=0 Xi=1 | u:0 p0 - | v:1 p1 - | y:0 p1 k0 hold | yb:0 p0 - | yp:0 p0 - | ypb:1 p1 - | e:0 p0 -
mid S2->S3         | old Q=yb R=ypb Xb=1 | new Xb=1 E=1 Xi=1 | u:0 p0 - | v:1 p1 - | y:0 p1 k1 ->1 | yb:0 p0 - | yp:0 p0 - | ypb:1 p1 - | e:0 p0 -
mid S3->S4         | old Q=y R=ypb Xb=1 | new Xb=1 E=1 Xi=0 | u:0 p1 k1 ->1 | v:1 p0 k1 hold | y:1 p1 - | yb:0 p0 - | yp:0 p1 k0 hold | ypb:1 p0 k0 ->0 | e:0 p0 -
mid S4 stay        | old Q=y R=ypb Xb=1 | new Xb=1 E=1 Xi=0 | u:1 p1 - | v:1 p0 k1 hold | y:1 p1 - | yb:0 p0 - | yp:0 p1 k0 hold | ypb:0 p0 - | e:0 p0 -
mid S4->S5         | old Q=y R=ypb Xb=1 | new Xb=1 E=0 Xi=0 | u:1 p1 - | v:1 p0 k1 hold | y:1 p1 - | yb:0 p0 - | yp:0 p1 k1 ->1 | ypb:0 p0 - | e:0 p0 -
mid S5->S6         | old Q=y R=yp Xb=1 | new Xb=1 E=0 Xi=0 | u:1 p1 - | v:1 p0 k1 hold | y:1 p1 - | yb:0 p0 - | yp:1 p1 - | ypb:0 p0 - | e:0 p1 k1 ->1
mid S6->S7         | old Q=y R=yp Xb=1 | new Xb=0 E=0 Xi=1 | u:1 p1 - | v:1 p0 k0 ->0 | y:1 p1 - | yb:0 p0 - | yp:1 p1 - | ypb:0 p0 - | e:1 p1 -
mid S7->S8         | old Q=y R=yp Xb=0 | new Xb=0 E=0 Xi=1 | u:1 p1 - | v:0 p0 - | y:1 p0 k0 ->0 | yb:0 p1 k0 hold | yp:1 p1 - | ypb:0 p0 - | e:1 p1 -
mid S8 stay        | old Q=y R=yp Xb=0 | new Xb=0 E=0 Xi=1 | u:1 p1 - | v:0 p0 - | y:0 p0 - | yb:0 p1 k0 hold | yp:1 p1 - | ypb:0 p0 - | e:1 p1 -
mid S8->S9         | old Q=y R=yp Xb=0 | new Xb=0 E=1 Xi=1 | u:1 p1 - | v:0 p0 - | y:0 p0 - | yb:0 p1 k1 ->1 | yp:1 p1 - | ypb:0 p0 - | e:1 p1 -
mid S9->S10        | old Q=yb R=yp Xb=0 | new Xb=0 E=1 Xi=0 | u:1 p0 k0 ->0 | v:0 p1 k0 hold | y:0 p0 - | yb:1 p1 - | yp:1 p0 k0 ->0 | ypb:0 p1 k0 hold | e:1 p1 -
mid S10 stay       | old Q=yb R=yp Xb=0 | new Xb=0 E=1 Xi=0 | u:0 p0 - | v:0 p1 k0 hold | y:0 p0 - | yb:1 p1 - | yp:0 p0 - | ypb:0 p1 k0 hold | e:1 p1 -
mid S10->S11       | old Q=yb R=yp Xb=0 | new Xb=0 E=0 Xi=0 | u:0 p0 - | v:0 p1 k0 hold | y:0 p0 - | yb:1 p1 - | yp:0 p0 - | ypb:0 p1 k1 ->1 | e:1 p1 -
mid S11->S0        | old Q=yb R=ypb Xb=0 | new Xb=0 E=0 Xi=0 | u:0 p0 - | v:0 p1 k0 hold | y:0 p0 - | yb:1 p1 - | yp:0 p0 - | ypb:1 p1 - | e:1 p0 k0 ->0
mid S0 idle        | old Q=yb R=ypb Xb=0 | new Xb=0 E=0 Xi=0 | u:0 p0 - | v:0 p1 k0 hold | y:0 p0 - | yb:1 p1 - | yp:0 p0 - | ypb:1 p1 - | e:0 p0 -
top T0->T1         | old Q=yb Xb=0 | new Xb=1 Xi=1 | u:0 p0 - | v:0 p1 k1 ->1 | y:0 p0 - | yb:1 p1 -
top T1->T2         | old Q=yb Xb=1 | new Xb=1 Xi=1 | u:0 p0 - | v:1 p1 - | y:0 p1 k1 ->1 | yb:1 p0 k1 hold
top T2->T3         | old Q=y Xb=1 | new Xb=1 Xi=0 | u:0 p1 k1 ->1 | v:1 p0 k1 hold | y:1 p1 - | yb:1 p0 k0 ->0
top T3->T4         | old Q=y Xb=1 | new Xb=0 Xi=1 | u:1 p1 - | v:1 p0 k0 ->0 | y:1 p1 - | yb:0 p0 -
top T4->T5         | old Q=y Xb=0 | new Xb=0 Xi=1 | u:1 p1 - | v:0 p0 - | y:1 p0 k1 hold | yb:0 p1 k1 ->1
top T5->T0         | old Q=yb Xb=0 | new Xb=0 Xi=0 | u:1 p0 k0 ->0 | v:0 p1 k0 hold | y:1 p0 k0 ->0 | yb:1 p1 -
top T0 idle        | old Q=yb Xb=0 | new Xb=0 Xi=0 | u:0 p0 - | v:0 p1 k0 hold | y:0 p0 - | yb:1 p1 -
```

Which class a level is in at a step (PHASE): case (a) with τ → τ + 1 gives, by the position function, `S0->S1` (τ = 0), `S1->S2` (1),
`S2 stay` (τ, τ + 1 ∈ [2, h − 1]), `S2->S3` (h − 1), `S3->S4` (h), `S4 stay`, `S4->S5` (2h − 1), `S5->S6` (2h), `S6->S7` (2h + 1), `S7->S8`
(2h + 2), `S8 stay`, `S8->S9` (3h), `S9->S10` (3h + 1), `S10 stay`, `S10->S11` (4h), `S11->S0` (4h + 1; pos(4h + 2) = S0); top: `Tτ->T(τ+1)`
for τ = 0..5. Cases (b), (c) and the STOP step give `S0 idle` / `T0 idle`: the level is at S0 / T0 in s and in n, its old inputs are
those of S0 (Xb = 0 at τ ∈ {0, 2·H_i} by INPUT (i)), and its new inputs are those of phase 0 (in the STOP step n = s = c_k(T_k), where
τ_2 = 2·H_2 and τ_i = 0 for i ≥ 3). Level 1: t → t + 1 for t = 0, 1, [2, h − 2], h − 1, h, [h + 1, 2h − 2] (`E=1`), 2h − 1 (`E=0`), and
the STOP step t = 2h (h = H_2). In every row the old columns are the phase-table row of the old phase and the new columns the row of
the new phase (Lemma INPUT at t and at t + 1).

**Lemma STEP.** For 0 ≤ t ≤ T_k let s := c_k(t) and n := c_k(t + 1) (n := s if t = T_k). Then n satisfies (EQ) of Lemma LATCH at s.
*Proof.* u_0: pref = 0 = s(u_0) (X0), stable, n(u_0) = 0. v_0: pref = 1 (X0); at t = 0 it is unstable and kmin = 1 = n(v_0) (K0); at
t ≥ 1 it is stable with n(v_0) = 1. Wires: pref = 0 = s(w) (X7), stable, n(w) = 0. Every other mover belongs to a level gadget, and
its row is the row of the class of that level at this step: in each cell marked `-` the mover is stable and its option in the new
position equals its old one; in each `hold` cell likewise; in each `->K` cell the new position has option K. (Compare each row with
the two positions it names: e.g. `S3->S4` moves exactly u (0 → 1) and ypb (1 → 0), and S3 = 01 10 01 0, S4 = 11 10 00 0.) ∎
So «nothing else moves» is, for every mover and every step, one of two facts: the mover is STABLE (its current option is the
Ξ-better one in the old state), or it is HELD (the key order of its two W-chains in the new state favours its current option).

**The two inputs of each mover, and the orders of the rule behind each cell.** (i = the mover's gadget; Xb = X_(i−1), Xi = X_i.)

| mover | Ξ input, OLD state (p in the cell) | lemma and orders used | key input, NEW state (k in the cell) | lemma and orders used |
| --- | --- | --- | --- | --- |
| u_i, v_i (i ≥ 1) | Q_i: which of y_i, yb_i is Ξ-better | X3; Q_i by X1 (dl inside Y_i; class B_(i−1) above Y_i above B_i) and Xb(old) | K_(i−1) = Xb(new): which of u_(i−1), v_(i−1) has the smaller key | K1; K_(i−1) = X_(i−1) by SIG (K2: ε(u_j,·) < ε(v_j,·); K0: ε(v_0,1) < ε(u_0,0) < ε(v_0,0)) |
| e_i | R_i: which of yp_i, ypb_i is Ξ-better | X6; R_i by X5 (dl inside Y′_i; class Y_i above Y′_i above e_i) and Q_i | K_(i−1) = Xb(new) | K1; SIG |
| y_i, yb_i (i ≤ k − 2) | P_(i−1) = Xb(old): which of u_(i−1), v_(i−1) is Ξ-better | X2 (class B_(i−1) above Y_i); P_(i−1) = X_(i−1) by SIG (X4: dl(v_j,·) > dl(u_j,·); X1; X0: dl(v_0,1) > dl(u_0,0) > dl(v_0,0)) | E(i+1)(new) and K_i = Xi(new): key of «E(i+1)» against key of the wire wv_i | K4 (ε(E(i+1),1) < ε(wv_i,0)); SIG |
| y_(k−1), yb_(k−1) | P_(k−2) = Xb(old) | X2; SIG | K_(k−1) = Xi(new): which of u_(k−1), v_(k−1) has the smaller key | K6; SIG |
| yp_i, ypb_i | Q_i | X5 (class Y_i above Y′_i) | E(i+1)(new) and K_i = Xi(new): key of «E(i+1)» against key of the wire wu_i | K5 (ε(E(i+1),0) < ε(wu_i,0)); SIG |
| v_0 | constant: option 1 is Ξ-better | X0 (dl(v_0,1) > dl(v_0,0)) | constant: option 1 has the smaller key | K0 (ε(v_0,1) < ε(v_0,0)) |
| u_0, wires | constant: option 0 is Ξ-better = current | X0, X7 | not read (stable) | — |

The start enters only through c_k(0) = s_0 (§3); no cell uses a start value otherwise.

**Order of evaluation: no circularity; where simultaneity matters.** R104 defines s′ by increasing W-level, and key_(s′)(x, ·) reads
s′ only on W-levels below lev(x). (EQ) is the same system, and the uniqueness half of Lemma LATCH is exactly the induction on the
W-level. In the tables every NEW-state input of a mover is a function of n on strictly lower W-levels:
- u_i, v_i, e_i (W-level i) read K_(i−1)(n), a function of n(u_j), n(v_j) for j ≤ i − 1 (W-levels ≤ i − 1; K2, K0);
- y_i, yb_i, yp_i, ypb_i with i ≤ k − 2 (W-level i + 2) read E(i+1)(n) = n(e_(i+1)) or n(u_(k−1)) (W-level i + 1) and K_i(n) (W-levels ≤ i);
- y_(k−1), yb_(k−1) (W-level k) read K_(k−1)(n) (W-levels ≤ k − 1).
So the verification can be read constructively: go up the W-levels; at W-level ℓ the new options below are already known to be those
of c_k(t + 1), and they fix the «new» columns of every row used on W-level ℓ. OLD-state inputs (pref) need no order.
Simultaneous events, each read in the NEW state from a lower W-level:
 (1) Chains of block movers. X_i rises in `S0->S1` and `S6->S7` of level i (v_i moves; `A0->A1` for i = 1) and falls in `S3->S4`
     and `S9->S10` (u_i moves; `A3->A4`). In the same step level i + 1 makes `S0->S1` / `T0->T1` (X_i rises) or `S6->S7` / `T3->T4`
     (X_i falls): these are its rows whose new Xb differs from the old one, and v_(i+1) (W-level i + 1) reads the move of v_i or u_i
     (W-level i) through K_i(n). At step 1 this runs through all levels: v_0, v_1, …, v_(k−1) move together.
 (2) (u_i↑, ypb_i↓) in `S3->S4` and (u_i↓, yp_i↓) in `S9->S10`. Both observers are unstable at S3 (Q_i has just become y): in `S3->S4` yp_i (at 0,
     pref 1) and ypb_i (at 1, pref 0) have kmin = [E(new) = 0 or Xi(new) = 1] = 0 because u_i's move makes Xi(new) = 0: ypb_i moves and
     yp_i is held. Read with the OLD Xi = 1 the key input would be 1 and the roles would be exchanged; the new-state reading is what
     R104 prescribes (u_i is on W-level i, the observers on W-level i + 2). `S9->S10` is the mirror image (yp_i moves, ypb_i is held).
 (3) Top: (u↑, yb↓) in `T2->T3` and (u↓, y↓) in `T5->T0`: yb_(k−1) resp. y_(k−1) (W-level k) have kmin = Xi(new) = 0 because u_(k−1)
     (W-level k − 1) moves in the same step; with the old Xi = 1 they would be held.
 (4) A latch and its E. y_i↑ in `S2->S3` (`A2->A3`), yb_i↑ in `S8->S9`: E(i+1)(new) = 1 because e_(i+1) (or u_(k−1)), on W-level i + 1,
     moves to 1 in that step (its row `S5->S6`, resp. `T2->T3`). yp_i↑ in `S4->S5`, ypb_i↑ in `S10->S11`: E(i+1)(new) = 0 because
     E(i+1) moves to 0 in that step (`S11->S0`, resp. `T5->T0`).
The tables never use more than Lemma INPUT at t (old columns) and at t + 1 (new columns).

## 6. Theorem GK and corollaries
**Lemma MOVE.** c_k(t + 1) ≠ c_k(t) for 0 ≤ t < T_k.
*Proof.* Let i ≥ 2 be largest with levels 2..i all in case (a) of PHASE. If i = k − 1, the top moves from T_τ to T_(τ+1) with
τ ≤ 5, and consecutive top positions differ. If i < k − 1, level i + 1 is in case (b), so τ_i(t) ∈ {H_i − 1, 2·H_i − 1} = {2h, 4h + 1}
(h = H_(i+1)): level i makes `S5->S6` or `S11->S0`, and e_i moves. ∎
**Proof of Theorem GK.** By induction on t, the state s_t of the run equals c_k(t) for 0 ≤ t ≤ T_k: s_0 = c_k(0) (§3). If
s_t = c_k(t) and t < T_k, then by STEP and LATCH the state s′ of R104's step at s_t is c_k(t + 1); it differs from s_t (MOVE), so
neither stop applies (if every |A_s(x)| were 1, the only solution of (EQ) would be s itself) and s_(t+1) = c_k(t + 1). At t = T_k,
STEP with n = s and LATCH give s′ = s: the run STOPS («stuck»). So L(G_k) = T_k = 2^k − 2. At the stop the unstable movers are those
with an `hold` cell in the rows `A4 stay (stop)`, `S0 idle`, `T0 idle`: exactly v_1, …, v_(k−1) (v_1 held by X_0 = 1, v_j held by
X_(j−1) = 0 for j ≥ 2). ∎
**Boundary cases, written out.**
- t = 0 → 1 (every k). All phases go 0 → 1: rows `A0->A1`, `S0->S1`, `T0->T1`. v_0 moves (X0, K0), and v_1, …, v_(k−1) move, each
  reading K_(j−1)(n) = v, i.e. the move of v_(j−1) in the same step. No latch moves: its Ξ input is Xb(old) = 0, so it is stable.
- k = 3 (no middle level; movers u_0, v_0, u_1, v_1, u_2, v_2, wv_1, y_1, yb_1, y_2, yb_2; no e, Y′, wu). H_1 = 7, H_2 = 3, T_3 = 6,
  τ_2 = t. The whole run, written u_1 v_1 y_1 yb_1 ‖ u_2 v_2 y_2 yb_2, with v_0 = [t ≥ 1]:
  t = 0: 0001 ‖ 0001; 1: 0101 ‖ 0101 (v_0, v_1, v_2); 2: 0100 ‖ 0111 (yb_1, y_2); 3: 0110 ‖ 1110 (y_1, u_2, yb_2); 4: 1110 ‖ 1010 (u_1, v_2);
  5: 1110 ‖ 1011 (yb_2); 6: 1110 ‖ 0001 (u_2, y_2). Classes: level 1 (h = 3): `A0->A1`, `A1->A2`, `A2->A3` (no `A2 stay`: [2, h − 2] is
  empty), `A3->A4`, `A4 stay (E=1)`, `A4 stay (E=0)`, then the stop row; top: `T0->T1`, …, `T5->T0`, then `T0 idle`. Level 1 reads
  E(2) = u_2: K4 uses ε(u_2,1) = 3 < 6 = ε(wv_1,0).
- k = 4 (one middle level, i = 2, with h = H_3 = 3, H_2 = 7; T_4 = 14). Level 2 reads E(3) = u_3 (the top): K4 uses ε(u_3,1) = 3 < 6,
  K5 uses ε(u_3,0) = 2 < 8. Its classes for t = 0..13: `S0->S1`, `S1->S2`, `S2->S3` (no `S2 stay`: [2, h − 1] = {2}), `S3->S4`, `S4 stay`
  (τ: 4 → 5), `S4->S5`, `S5->S6`, `S6->S7`, `S7->S8`, `S8->S9` (no `S8 stay`), `S9->S10`, `S10 stay` (τ: 11 → 12), `S10->S11`, `S11->S0`; at
  the stop `S0 idle`. The top has τ_3 = t mod 7: `T0->T1`..`T5->T0` for t = 0..5, `T0 idle` at t = 6 (case (b) of PHASE: τ_3 = 6 → 0),
  again `T0->T1`..`T5->T0` for t = 7..12, `T0 idle` at t = 13 and at the stop. Level 1 (h = 7): `A0->A1`, `A1->A2`, `A2 stay` (t = 2..5),
  `A2->A3` (t = 6), `A3->A4` (t = 7), `A4 stay (E=1)` (t = 8..12), `A4 stay (E=0)` (t = 13), stop row.
- Level 1 (every k). It has no Y′, e, wu; y_1, yb_1 sit on W-level 3 and read E(2) (e_2; u_2 for k = 3) and K_1. X_0 never falls, so
  after `A3->A4` (step H_2 + 1 = 2^(k−1)) level 1 is frozen: v_1 stays unstable (pref 0 since Q_1 = y) and held by Xb(new) = X_0 = 1.
- Level k − 2 (k ≥ 4) reads E(k − 1) = u_(k−1) with ε(u_(k−1),·) = (2, 3): K4 needs 3 < 6, K5 needs 2 < 8; INPUT (ii) holds with
  h = H_(k−1) = 3 because u_(k−1) = 1 exactly at T3, T4, T5.
- t = L = T_k (STOP). The equations (EQ) hold with n = s (rows `A4 stay (stop)`, `S0 idle`, `T0 idle`), so s′ = s and R104's clause
  applies: «If s' = s, the run STOPS («stuck»).» The other clause, «If |A_s(x)| = 1 for every x, the run STOPS («opt»).», does not apply:
  A_s(v_1) = {0, 1}.
**Proof of Corollary SW.** By PHASE, τ_2 runs once through [0, 2·H_2], and while τ_i runs once through [0, 2·H_i] the phase
τ_(i+1) = τ_i mod H_i runs twice through [0, 2·H_(i+1)] (on [0, H_i − 1] and on [H_i, 2·H_i − 1]) and is 0 at 2·H_i. So level i ≥ 2
walks its cycle 2^(i−2) times. In one cycle every mover of a middle level switches exactly twice (once up, once down: the «moved»
row of §3), and every top mover twice (T0..T6). Level 1 walks A0..A4 once (v_1, yb_1, y_1, u_1 once each), v_0 switches at step 1.
Total 1 + 4 + Σ_(i=2..k−2) 7·2^(i−1) + 4·2^(k−2) = 11·2^(k−2) − 9. ∎
**The window recursion.** H_i = 2·H_(i+1) + 1: a half cycle of level i (S0 → S6 or S6 → S0) lasts as long as one FULL cycle of level
i + 1 plus the one step in which e_i moves alone. With T(k) := L(G_k) = 2·H_2 this is the Lead's T(k + 1) = 2·T(k) + 2, T(3) = 6.

## 7. Where the start and each order of the rule is used; what is not used
| fact of the rule | used in | role |
| --- | --- | --- |
| start (every bit) | §3, c_k(0) = s_0 | the run starts at phase 0 of every level |
| dep(Ξ-target) < dep(mover) on every Ξ-edge | DEP, CMP | a chain's later β's outrank its earlier ones: a reader copies the order of the pair it reads |
| dl(u_0,0) > dl(u_0,1) | X0 | u_0 is STABLE (if violated, u_0 is unstable but HELD by ε(u_0,0) < ε(u_0,1): no state of the run changes, control dl-u0) |
| dl(v_0,1) > dl(u_0,0) > dl(v_0,0) | X0 | v_0 unstable at the start; P_0 flips when v_0 moves |
| dl(v_j,·) > dl(u_j,·), 1 ≤ j ≤ k − 2 | X4 | P_j = v while u_j ≠ v_j (for j = k − 1 the order has no reader) |
| dl(yb_j,1) > dl(y_j,0), dl(y_j,1) > dl(yb_j,0) | X1 | Q_j when both latches point at the same block mover |
| dl(ypb_j,1) > dl(yp_j,0), dl(yp_j,1) > dl(ypb_j,0) | X5 | R_j when both observers point at the same latch |
| dl(w,0) > dl(w,1), w a wire | X7 | wires are STABLE (if violated, a wire is unstable but HELD by ε(w,0) < ε(w,1): no state of the run changes, control dl-w) |
| ε(v_0,1) < ε(u_0,0) < ε(v_0,0) | K0 | v_0 moves at step 1; K_0 flips with it |
| ε(u_j,·) < ε(v_j,·), j ≥ 1 | K2 | K_j = u while u_j, v_j share the W-target |
| ε(E(j+1),1) < ε(wv_j,0) | K4 | y_j, yb_j go «fwd» as soon as E(j+1) = 1 |
| ε(E(j+1),0) < ε(wu_j,0) | K5 | yp_j, ypb_j go «fwd» as soon as E(j+1) = 0 |
| gate indices distinct per W-level | LATCH, K1, K2 | keys of two movers of one level differ |

NOT used (any values keeping ranks and gate indices distinct give the same run): the ε of the eight latch kinds (10..17, 20..23); ε(u_0,1);
ε(w,1) of the wires; the order between ε(e_j,·) and ε(u_j,·), ε(v_j,·); the dl of e_j; the dl order between different pairs of one class
(Y′_j against B_j; e_j against Y_(j+1)); the dl order of the top block pair; the tie rule by β-id; the value 2k + 5 of the wires' class.
**Remark ROBUST (PROVED by the same proof, lane).** Theorem GK and Corollary SW hold for every degree-2 genome with G_k's movers,
levels, W-targets, Ξ-targets and start, all parities 0, whose ranks and gate indices satisfy the rows above in this form: every β of
a mover of class dep D outranks every β of a mover of class dep D′ > D whenever both classes are ≤ 2k − 1 (the wires' β's are free),
the listed dl inequalities hold as rank inequalities, and the listed ε inequalities hold as gate-index inequalities on the same
W-level. No other property of the numbers enters §2–§6.
DATA for the table (controls of §9, k = 4..6): the mutations of the rows start (yb, ypb), dep, dl(v_0 / u_0), dl(v_j / u_j) at
level k − 2, both dl rows of Y_j and of Y′_j, and all four ε rows each change L; the mutations dl-u0 and dl-w leave every state
unchanged (only the held set grows, as the table says); the mutation of the TOP pair's dl order leaves the run unchanged (it fails
only the formula for P_(k−1), which no mover reads).

## 8. The mechanism in words
Every mover is a two-input latch (LATCH): it switches to an option only when BOTH the value order of its two Ξ-targets (old state) and
the key order of its two W-chains (new state) favour it. Level j shows the world one bit X_j = [u_j ≠ v_j], and both orders of its
block pair copy that bit (SIG). A level reads the bit of the level below twice: its block movers and e_i read it as a KEY order (so
they react in the same step), its latches read it as a VALUE order (one step later). Upward a level learns «the levels above have
finished a full cycle» from the single bit E(i + 1), read by its latches and observers as the key order «E(i + 1) against a wire»
(K4, K5): y / yb wait for E(i + 1) = 1 at S2 and S8, yp / ypb wait for E(i + 1) = 0 at S4 and S10. So between two flips of X_i the
level above walks half its cycle, and between two flips of e_i it walks the whole cycle: each level runs at twice the rate of the
level below, and the top runs a 6-step cycle 2^(k−3) times. No mover enumerates anything: the count is exponential because the levels
are nested «do everything above twice», with a constant number of movers (nine) per level.

## 9. Check (DATA; `experiments/si/box108/`, block in `experiments/si/check.sh`)
- `gk108.py` (builder from §1.2), `ideal108.py` (own simulator, written from §1.1; β-sets and tuple keys, no shortcut),
  `abs108.py` (the abstract latch network: Lemma LATCH with the inputs given by the signal formulas of §2, no chains and no keys),
  `quotes108.py` (the R104 quotes of §1.1 and of the STOP bullet against docs/red/P-N5-REALIZE.md, with a control),
  `check108.py` (counters below), `check108.sh` (the pinned block: fresh run against the frozen outputs `out/`; the 32 table rows of
  §5 are compared line by line with this file, and `--doc` parses the position row of §3 and the three phase tables of §4 out of
  this file and compares them with the signals computed from chains and keys on every run state: counter DOC).
- Counters, k = 3..12 (unit: failures; set: every t ∈ [0, 2^k − 2] of the run of G_k, every mover; scope: IDEAL model, own simulator):
  SHA 0 (four sha1); RUN 0 (L = 2^k − 2; stop «stuck» with held set v_1..v_(k−1)); CLOSED 0 (s_t = c_k(t)); LATCH 0 ((EQ) from the
  definition); STATIC 0 (X0–X7, K0–K6 and the signal formulas against chains and keys, on all run states and 200 random states per
  k with u_0 and the wires at 0); SIG 0; SW 0 (Corollary SW); TABLE: 32 classes, each with exactly one row, none missing; DOC 0
  (23 positions: per position the set of observed (state, Q, R, Xb, E, Xi) equals the set of this file's rows).
- Second engine: L-NEW's `one217.OneP` (claude/l-new a143d4060, rule «key»): the same state sequence as `ideal108` for k = 3..10
  (`check108.sh`, frozen `out/one217.out`).
- Controls (`--ctrl NAME`, k = 4..6, frozen `out/ctrl108.out`; each must make the check FAIL on every k; the line also prints L):
  H-off (closed form with H_i − 1: CLOSED fails). Genome mutations that change L (unmutated 14, 30, 62): eps-wv (3, 3, 3), eps-wu
  (3, 3, 3), eps-uv (11, 23, 47), eps-v0 (0, 0, 0), dl-y (6, 12, 24), dl-y2 (9, 14, 26), dl-yp (5, 11, 23), dl-yp2 (6, 6, 6), dl-uv at
  level k − 2 (2, 2, 2), dl-v0 (3, 4, 5), dep-yb (13, 28, 58), start-yb (6, 12, 24), start-ypb (5, 8, 19). Genome mutations that keep
  every state (L unchanged; only RUN's held-set test and STATIC fail): dl-u0, dl-w. Mutation with no effect on the run (STATIC only):
  dl-uvtop. Formula mutations (STATIC only): form-kmin-yp, form-Q. All 19 fire.
- Run lengths (DATA): L(G_k) = 6, 14, 30, 62, 126, 254, 510, 1022, 2046, 4094 for k = 3..12; N = 9k − 16.
- Abstract network (`abs108.py`; DATA; counter: states differing from c_k(t), set: every t of its run, scope: the latch network of
  §2's formulas, whose agreement with the definition is the counter STATIC for k ≤ 12): 0 for k = 3..17, with run lengths 2^k − 2
  (k = 3..11 re-run by `check108.sh`; k = 12..17 frozen in `out/abs108_long.out`: 4094, 8190, 16382, 32766, 65534, 131070).
- Other rules on the same genomes (DATA; counter: steps of `one217.OneP.run`, set k = 3..10, scope: L-NEW's model 1P(G_k), rules as
  defined in one217.py; NOT statements about the IDEAL step or about N5): «howard» (every mover to its Ξ-best option) 3, 4, 4, 4, 4, 4,
  4, 4; «seq» (the key step applied at one mover at a time) 10, 25, 51, 73, 96, 118, 140, 162. So on G_k the exponential length belongs
  to the simultaneous key step; this is an observation, no lemma.

## 10. Honest limits
- PROVED here (lane, unrefereed): Theorem GK, Corollary SW, Remark ROBUST, for R104's IDEAL model with the key and value definitions
  quoted in §1.1. The proof rests on the hand-checkable tables of §4–§5; the script guards them against typos but is not the proof.
- NOT claimed: anything about N5 on Γ(G_k) or Γ3(G_k) (that transfer is RESULTS R104 / R117, not re-derived here); anything about
  Howard's rule or other improvement rules on G_k; minimality of G_k; the «enumeration depth» of G_k.
- OPEN for the referee of record: the comparison of this derivation with L-RED-B's (not read by me); on the Lead's word I can align
  the two step for step.
