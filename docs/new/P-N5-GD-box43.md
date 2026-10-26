# Packet P-N5-GD (box 43): set-form Lemma G, F1° and Wo on every game (the disagreement set D_k replaces o)
L-NEW successor 23 (Opus 5.5), D14 / D18, Lead reading L40; Lead's order 01:05Z (Lead's stamp). Written 2026-10-26 01:06Z-01:10Z (date -u).
FROZEN at push: later text goes into a fixes file. Source: docs/new/N5-MULTI-box43.md §4.4 (l-new fe3b0527, b2b88ea9; written by
successor 22; working doc, this packet governs). Successor 23 re-checked every step below against the cited landed texts.
Labels: PROVED (L-NEW 22, re-checked by L-NEW 23; unrefereed) / CONJECTURE / OPEN / DATA / READING. Not a TARGET.md claim: nothing
here bounds N5's running time on any class. G-N5-TIME stays open. Conjecture Δ1, Δ-RT and the R20 coarse port are NOT to sign (§3).

## 0. Setting (every game; no class hypothesis)
- N5 = SPEC S1-S5 of docs/new/N5-ssi-global.md (with FIX 1-4). Game G = (V, E, Ω, owner), n = |V|. State k = (σ_k, τ_k). σ̄_k = SPEC
  S1's optimal Odd counterstrategy to σ_k (with its tie-breaks). Ξ_k(v) := the VJ00 value of the (σ_k, σ̄_k)-play from v (the honest
  value). G_τ := G with every Odd vertex fixed to τ_k (a one-player game). W_k(v) := the value of the (σ_k, τ_k)-play from v (σ_k's
  valuation in G_τ). λ_Ξ, λ_W := the cycle-node maps of Ξ_k, W_k. Values x = (c, P, ℓ) and their order ⊴ as in VJ00 (RESULTS R15).
- PHASE: a maximal run of states with (λ, τ) constant (= joint λ-phase, RESULTS R38 (a) KEY, every game). A transition of a run I
  of states is k → k+1 with k, k+1 ∈ I.
- Disagreement set D_k := {Odd u : σ̄_k(u) ≠ τ_k(u)}. For v ∈ V, u(v) := the first vertex of D_k on v's (σ_k, τ_k)-play (v itself
  included), if any. R_D := {v : u(v) exists}, F_D := V ∖ R_D. For v ∈ R_D, π_v := the (σ_k, τ_k)-path from v to u(v), u(v)
  excluded. (All of D_k, u(·), R_D, F_D, π depend on k; the index is dropped when k is fixed.)
- On 𝒞^1O (one Odd choice vertex o): D_k ⊆ {o}; if D_k = {o}, R_D = R (vertices whose play reaches o) and F_D = F; if D_k = ∅,
  then σ̄_k = τ_k and R_D = ∅.
- Hypotheses, assumed ONLY where a statement names them:
  - (h_D) at k: for every u ∈ D_k, neither the honest play (σ_k, σ̄_k) nor the W-play (σ_k, τ_k) from u visits D_k after
    leaving u (in particular neither returns to u). On 𝒞^1O with D_k = {o}: (h_D) = H1 ∧ H2 of R19's (h).
  - (h3_D) at k: for every u ∈ D_k, λ_Ξ(u) = λ_W(u). On 𝒞^1O with D_k = {o}: (h3_D) = H3. (h) of R19 = (h_D) ∧ (h3_D).
- lev, COARSE_L, ranks and (C1)-(C4) as in RESULTS R25 (P-N5-FB §1): lev(x, y) := ∞ if the cycle nodes differ, else the top rank of
  P(x) Δ P(y), else −1 if only the lengths differ, ⊥ if x = y; COARSE_L(x) := (c, P ∩ V_{>L}) for −1 ≤ L < ∞, COARSE_⊥(x) := x;
  (C2) COARSE_L x = COARSE_L y ⟺ lev(x, y) ≤ L; (C4) COARSE_L(u ⊕ x) is a function of u and COARSE_L(x). Order ⊥ < −1 < 0 < … < ∞.
  M_D := max over u ∈ D_k of lev(Ξ_k(u), W_k(u)); M_D := ⊥ if D_k = ∅. Under (h3_D), M_D < ∞.
- Roots (names from N5-MULTI §2, READING): (FO) "Odd vertices other than o are forced"; (HP) "the honest play is the
  (σ, τ)-play until the first visit of o", i.e. σ̄ = τ off o. In set form (HP_D) "σ̄_k = τ_k off D_k" holds on EVERY game by the
  definition of D_k. Every proof below uses (HP_D) where the landed 𝒞^1O proof used FO or HP; §2 lists each replacement.
- Premises (landed; each proof below uses only these):
  - R17 (a): (V1) (prefix equation), (V2) (prefix monotonicity), (F1) (in a one-player game the optimum dominates every strategy of
    the arena pointwise); R17 (b), (c): Lemma P, Theorem PH (one-player games).
  - R15 (a): Ξ_{k+1} ⊵ Ξ_k at every N5 transition (every game; as used in P-N5-RE §2 = R19 (b)).
  - R18 (d) Lemma S (c): S4a returns σ_k iff σ_k is a pointwise optimum of its arena; R18 (c), flat case (R17's single-switch case
    analysis in a one-player arena): at a pointwise arena optimum, every arena edge (x, z) improving for the valuation is flat
    (x = λ(x), z in x's region, the switch changes no value). R21 (a) Lemma XW: Ξ_k ⊴ W_k. R21 (c) FBL-N (i).
  - Class of the premises (READING, ledger rows of N5-MULTI §2; referees to confirm): R15 (a), R17, R18 (c) flat case and (d) Lemma
    S, R21 XW and FBL-N (i) are signed under a 𝒞^1O setting line but their proofs use no one-Odd property (R17 and R18's flat case are
    one-player statements, applied here to G_τ and its arenas, which are one-player on every game; XW is VJ00 (11) on G_{σ_k};
    FBL-N (i) uses only SPEC S4c's "Even first" and τ_{k+1} = τ_k).

## 1. To sign
### Lemma G_D (a) (PROVED, every game; no hypothesis)
For every state k and every v ∈ F_D: Ξ_k(v) = W_k(v).
Proof. Along v's (σ_k, τ_k)-play every vertex lies outside D_k (v ∈ F_D), so at every Odd vertex x of it σ̄_k(x) = τ_k(x) (HP_D);
Even vertices use σ_k in both plays. By induction along the play, the (σ_k, σ̄_k)-play and the (σ_k, τ_k)-play from v are equal, so
their values are equal. ∎

### Lemma G_D (b) (PROVED, every game, under (h_D) at k)
For v ∈ R_D with u := u(v): Ξ_k(v) = π_v ⊕ Ξ_k(u) and W_k(v) = π_v ⊕ W_k(u) (⊕ along a path = iterated (V1)); and the honest and the
W-play from u avoid π_v.
Proof.
- Both plays from v follow π_v to u: the Odd vertices of π_v are outside D_k (u is the first vertex of D_k), so σ̄_k = τ_k there
  (HP_D).
- Continuation avoids π_v. Let x ∈ π_v. x's (σ_k, τ_k)-play is the suffix of π_v from x, then u; it meets D_k first at u, so by
  (HP_D) x's honest play is the same path to u. If u's honest play (resp. W-play) met x after leaving u, it would then follow x's
  play back to u ∈ D_k, against (h_D) at u.
- So each play from v is π_v followed by u's play, whose cycle lies off π_v; (V1) along π_v gives both equations. ∎

### Lemma G_D (c) (PROVED, every game, under (h_D) and (h3_D) at k)
- (c1) Same terminal. If y, z ∈ R_D and u(y) = u(z) = u, then π_y ⊕ Ξ_k(u) ⊴ π_z ⊕ Ξ_k(u) iff π_y ⊕ W_k(u) ⊴ π_z ⊕ W_k(u).
- (c2) Coarse form, any terminals. For every L with M_D ≤ L < ∞ (L = ⊥ allowed when M_D = ⊥) and every v ∈ V:
  COARSE_L(Ξ_k(v)) = COARSE_L(W_k(v)). Hence the COARSE_L-orders of Ξ_k and of W_k coincide on all of V.
Proof of (c1). By (h3_D), Ξ_k(u) and W_k(u) have the same cycle node c. For T ∈ {Ξ_k(u), W_k(u)}, π_v ⊕ T = (c, A_v ∪ P(T),
|π_v| + ℓ(T)) for v ∈ {y, z}, with A_v := {x ∈ π_v : x more relevant than c}, and A_v ∩ P(T) = ∅ (G_D (b): T's play avoids π_v).
So the symmetric difference of the two path sets is A_y Δ A_z and the length difference is |π_y| − |π_z|, whichever T is used;
VJ00's order on two values with the same cycle node depends only on these. ∎
Proof of (c2).
- v ∈ F_D: Ξ_k(v) = W_k(v) (G_D (a)).
- v ∈ R_D, u := u(v): by G_D (b), Ξ_k(v) = π_v ⊕ Ξ_k(u) and W_k(v) = π_v ⊕ W_k(u). lev(Ξ_k(u), W_k(u)) ≤ M_D ≤ L, so
  COARSE_L(Ξ_k(u)) = COARSE_L(W_k(u)) by (C2) (for L = ⊥: M_D = ⊥ means Ξ_k(u) = W_k(u)). By (C4) along π_v (both plays from u
  avoid π_v, so each ⊕ step is a (V1) step), COARSE_L(π_v ⊕ a) is a function of π_v and COARSE_L(a). So the two coarse values at v
  are equal.
- The order statement: equal coarse values pointwise give equal coarse orders. ∎
Remark (what (c) does NOT give; OPEN, Δ-RT in §3). For y, z with different terminals u(y) ≠ u(z) and a route difference at a level
≤ M_D, π_y ⊕ Ξ(u(y)) vs π_z ⊕ Ξ(u(z)) and π_y ⊕ W(u(y)) vs π_z ⊕ W(u(z)) can be ordered differently. (c1) and (c2) are all that
is claimed.

### Lemma F1°_D (PROVED, every game; no (h_D), no (h3_D))
Let I be a D-CROSSING-FREE INTERVAL: a maximal run of states of one phase on which (D_k, R_D) is constant (so F_D is constant; write
F_D for it). Then the transitions of I at which Ξ changes at some vertex of F_D number at most max(0, |F_D| − 1).
Proof (the six steps of R22 (a) = P-N5-NH-box30 §1, in set form).
1. At every state k of I: Ξ_k = W_k on F_D (G_D (a)). F_D is closed under σ_k and under τ (a successor of x ∈ F_D along x's play
   has the tail of x's play, which avoids D_k). Let 𝓕 := G_τ[F_D]: Even vertices of F_D keep their edges into F_D, Odd vertices
   keep τ. 𝓕 is a one-player game (every vertex has a successor in F_D, by closure).
2. For x, z ∈ F_D: (x, z) ∈ Iσ_k iff it is 𝓕-improving at σ_k|F_D (step 1 at both endpoints: Ξ_k = W_k = 𝓕's valuation on F_D,
   because plays from F_D under σ_k, τ stay in F_D).
3. S4a steps k → k+1 of I. F_D at k+1 is F_D, closed under σ_{k+1}, so σ_{k+1}|F_D is a strategy of 𝓕's arena
   A^𝓕_k := {σ_k(x)} ∪ (𝓕-improving edges at x) (step 2: its switched edges from F_D are gate edges into F_D). Any strategy ρ of
   A^𝓕_k, extended by σ_{k+1} off F_D, is a strategy of S4a's arena in G_τ (step 2), and its plays from F_D stay in F_D. By (F1)
   in G_τ, W_{k+1} dominates its valuation pointwise; on F_D both are 𝓕-valuations. So σ_{k+1}|F_D is a pointwise optimum of
   A^𝓕_k: R17's switch-best step on 𝓕.
4. S4c steps k → k+1 of I. τ_{k+1} = τ_k (one phase), so the fallback is Even's and σ_k is a pointwise optimum of the S4a arena in
   G_τ (FBL-N (i); R18 (d) Lemma S (c)). FBL-N (ii) in set form: let (x, z) be a gate edge with x ∈ F_D. Then σ_k(x) ∈ F_D (step 1)
   and Ξ_k(σ_k x) = W_k(σ_k x) (G_D (a)); Ξ_k(z) ▷ Ξ_k(σ_k x) (gate edge); XW gives W_k(z) ⊵ Ξ_k(z); so W_k(z) ▷ W_k(σ_k x), and by
   R18 (c)'s flat case at the arena optimum the edge is flat for W_k (x = λ_W(x), λ_W(z) = x). Since k+1 ∈ I, z ∈ F_D. The switched
   vertices of F_D are cycle nodes of distinct cycles (one cycle node per cycle), with disjoint regions, and each flat switch changes
   no value (R18 (c); as in R21 (d)'s proof, P-N5-X §4). Switches of R_D vertices do not affect 𝓕 (plays from F_D avoid R_D). So
   the F_D-values do not change at S4c steps, and R17 Lemma P's invariant on 𝓕 (a statement about current values) carries over.
5. λ on F_D is λ_Ξ (= λ_W there), constant on the phase; so the 𝓕-run is inside one λ-phase of 𝓕.
6. R17 Lemma P and Theorem PH on the one-player game 𝓕 (its Odd vertices have one successor) give ≤ max(0, |F_D| − 1)
   value-changing steps. By step 1 these are exactly the transitions of I with a Ξ-change on F_D. ∎

### Lemma Wo_D (PROVED, every game, under (h_D) at k and at k+1)
Let k → k+1 be an N5 transition with τ_{k+1} = τ_k, and u ∈ D_k ∩ D_{k+1}. Then W_{k+1}(u) ⊵ W_k(u).
Proof (P-N5-RE §2 = R19 (b), with u for o). Let b := τ(u) (= τ_k(u) = τ_{k+1}(u)). Fix j ∈ {k, k+1}. By (h_D) at j, u's W-play does
not return to D_j after leaving u; so u is not its own W-cycle node, and b's W-play (the tail of u's after u, b included) avoids
D_j: b ∈ F_D at j. By G_D (a), W_j(b) = Ξ_j(b), and b's honest play is its W-play, which avoids u. By (V1), W_j(u) = u ⊕ W_j(b) =
u ⊕ Ξ_j(b). By R15 (a), Ξ_{k+1}(b) ⊵ Ξ_k(b); both plays avoid u, so (V2) gives W_{k+1}(u) ⊵ W_k(u). ∎
(No (h3_D) and no phase hypothesis are used; the honest-side statement Ξ(u) is not claimed.)

## 2. Port table: the landed 𝒞^1O step, and what replaces FO / HP
| this packet | landed step (𝒞^1O) | the one-Odd use there | replaced by |
| --- | --- | --- | --- |
| G_D (a) | R19 (a) Lemma G (a) = P-N5-RE §1 (a): "the σ_k-path from v meets no Odd vertex with a choice before it closes (it never reaches o), so the plays under σ̄_k and τ_k coincide" | FO (the only Odd choice is at o, and v's play avoids o) | (HP_D) on F_D: σ̄ = τ at every vertex of v's play, by the definition of D_k and F_D; FO not needed |
| G_D (b) | R19 (a) Lemma G (b) = P-N5-RE §1 (b): "both plays follow π_v to o"; "any vertex of π_v reaches o, so meeting one would return the play to o" | HP (σ̄ = τ off o) | (HP_D): σ̄ = τ on π_v (u(v) is the first D_k vertex); the return argument uses (h_D) at u(v) in place of (h)'s H1, H2 |
| G_D (c1) | R19 (a) Lemma G (c) = P-N5-RE §1 (c), verbatim with u for o | (h)'s H3 (common cycle node c of θ, w) | (h3_D) at u |
| G_D (c2) | R20 (a) Lemma C (P-N5-XA §2): COARSE(Ξ) = COARSE(W) above u* := top of P(θ) Δ P(w) | RT (one terminal o, Ξ = π ⊕ θ, W = π ⊕ w on R) | several terminals u ∈ D_k; threshold M_D = max_u lev(Ξ(u), W(u)); (C2), (C4) of R25 at each terminal. Only the pointwise equality is ported, NOT C's monotonicity along a stretch (that is the R20 coarse port, §3) |
| F1°_D | R22 (a) Lemma F1° = P-N5-NH-box30 §1 steps 1-6, with R21 (c) FBL-N (ii) = P-N5-X §3 (ii) | step 1: "F contains no vertex with an Odd choice (o ∉ F)" (FO); FBL-N (ii): "x's play avoids o, so σ_k(x) ∈ F and Lemma G (a)" (HP) | step 1: 𝓕 := G_τ[F_D] is one-player because Odd is fixed to τ in G_τ (no FO needed); FBL-N (ii): σ_k(x) ∈ F_D by closure and G_D (a). "Crossing" := a change of (D_k, R_D) |
| Wo_D | R19 (b) Lemma Wo = P-N5-RE §2 | (h)'s H2 (τ(o) ∉ R), Lemma G (a) | (h_D) at k and k+1 at u (gives τ(u) ∈ F_D, the ledger's "H2_i strengthened to τ(o_i) ∈ F_D"), G_D (a) |

## 3. Not to sign (stated for context only)
- Conjecture Δ1 (CONJECTURE, every game; the Lead's form): inside one phase of an N5 run, the transitions at which (D_k, R_D) changes
  number at most poly(n). With F1°_D, F_D-side value changes per phase would then be poly(n). DATA: lib41 frontier ≤ 5 D-changes
  per phase; best climbed dch16_n44 (experiments/new/box43/instances/dch16_n44.pg: 16 D-changes, 27 R_D-changes in one phase of 44
  transitions).
- Δ-RT (OPEN): the fine route order on R_D for routes to different terminals below level M_D (Remark after G_D (c)). The R_D side
  of PIECE (R19 (f)) and every R-side count of the ledger rest on it.
- The R20 coarse port (CONJECTURE): R20's C (monotonicity), FBL, FBF, CR, XA with u* → M_D and "θ, w constant" → "Ξ(u), W(u)
  constant for every u ∈ D_k".
- docs/new/N5-MULTI-box43.md §2-§4 otherwise (ledger READING; frontier DATA; routes).

## 4. Data (DATA, not proof) and reproduce
experiments/new/box43/f1d.py (L-NEW 22; re-run by L-NEW 23 at 2026-10-26 01:07Z-01:09Z by date -u, from experiments/new/box43). It
checks G_D (a) at every state, G_D (c2) at every state with (h_D) and (h3_D) (at L = max(M_D, −1): the script's path-set masks drop
lengths, so for M_D = ⊥ it checks the weaker L = −1), Wo_D at every qualifying transition, and F1°_D on every D-crossing-free interval
of every phase. G_D (b), (c1) are not checked separately ((c2) on R_D uses (b)).
Every run starts at SPEC S3's start pair. The F1°_D check counts, per maximal run of consecutive states with (λ_Ξ, τ, D_k, R_D)
constant, the transitions with a Ξ-change on F_D, against max(0, |F_D| − 1).
| sample | runs | transitions | G_D (a) viol. | F1°_D viol. | G_D (c2) states / viol. | Wo_D checks / viol. |
| --- | --- | --- | --- | --- | --- | --- |
| `--list experiments/new/box41/lib41.txt` (canonical library) | 412 | 8,477 | 0 | 0 | 6,310 / 0 | 4,421 / 0 |
| `--rand 2000 5 14 21` (random 𝒞^kO, k 2-4, n 5-14) | 2,000 | 2,487 | 0 | 0 | 2,902 / 0 | 29 / 0 |
| `--rand 2000 5 14 22` | 2,000 | 2,453 | 0 | 0 | 2,910 / 0 | 21 / 0 |
| `instances/*.pg` (box-43 instances: dch16_n44, retf_n6, ret2_n7, tj17_n19, tx2_n8) | 5 | 87 | 0 | 0 | 39 / 0 | 13 / 0 |
Each line prints as "runs N, transitions T: G_D(a) violations 0; F1_D violations 0; G_D(c2) states checked …, violations 0; Wo_D
checks …, violations 0". Runtime: about 2 min for the lib41 line, less for the others. Thin spots: Wo_D is nearly vacuous on random
games (50 checks); (c2) is checked only at L = max(M_D, −1), not at every L ≥ M_D (larger L is implied by (C2) and is not data).
