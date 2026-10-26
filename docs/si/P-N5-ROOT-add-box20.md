# P-N5-ROOT-add-box20: inside a D-direct gate region the honest Bellman-Ford step holds up to the gate's offset, the W-step is exact and freezes, and relays of the gate then move ≤ deg − 1 times (GATE-SHIFT, FREEZE-G, RELAY-PIECE)
Addendum packet for both referees, to be reviewed together with P-N5-ROOT-box20 (docs/si/P-N5-ROOT-box20.md, sha1
d3788bc0ce0e3da2d54298c58e227e437242419a, frozen at l-si ced5cf27). Author: L-SI successor 16 (Opus 5.5; D18, L40). Source: lane note
docs/si/N5-ROOT-box20.md §8.3, §9 (not frozen; this addendum is). Written at the Lead's request of 15:02Z (Lead's stamp: "freeze the addendum now
as docs/si/P-N5-ROOT-add-box20.md. It must be self-contained"). Stamp of the freeze: the commit (date -u).
Scope (D1): lemmas inside one phase of N5 on EVERY game. RELAY-PIECE bounds relay path-weight changes per G-interval; the number of G-intervals
(resets of a gate's offset or region) is NOT bounded here. Nothing here bounds N5's running time, ρ, N_ep or f. Not a TARGET.md claim.
G-N5-TIME stays OPEN.
Quotes: every «…» is verbatim from the tagged source; [Q path@commit:lines] is checked by
`python3 -I experiments/si/rund/quotecheck.py docs/si/P-N5-ROOT-add-box20.md` (QUOTES PASS; whitespace normalised; "…" separates parts).
Pinned in experiments/si/check.sh.

## 0. What to sign
- §2 Lemma GATE-SHIFT (a), (b); §3 Theorem FREEZE-G (a)-(c); §4 Corollary RELAY-PIECE.
- Not to sign: §5 (DATA), §6 (READING).

## 1. Setting, premises and cited text
### 1.1 Objects (as in P-N5-ROOT-box20 §1, restated)
- N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md, FIX 1-4) with the standing premise 1E-N3, as in RESULTS R55-R69. A PHASE: a maximal run of
  states with λ_Ξ and τ constant (RESULTS R38 (a) KEY). Every in-phase transition is an S4a step (σ_{t+1} is Even's optimum of the arena H_t
  against τ: every Even v keeps σ_t(v) and its edges in Iσ_t, every Odd v keeps τ(v)) or an Even S4c fallback.
- [Q docs/RESULTS.md@a7c141b8:2786-2787] «D_k := {Odd u : σ̄_k(u) ≠ τ_k(u)}; u(v) := the first vertex of D_k on v's (σ_k, τ_k)-play (v
  included), if any; R_D := {v : u(v) exists}, F_D := V ∖ R_D». W_t(v): the value of the (σ_t, τ)-play from v.
- [Q docs/RESULTS.md@a7c141b8:2839-2841] «for c ∈ C the honest class U_c := λ^{-1}(c). κ_t(z) := (signed weight of P(Ξ_t z), s_c·ℓ(Ξ_t z)) for
  z ∈ U_c, s_c := +1 if Ω(c) is odd, −1 if even; κwt_c(v) := (wt_c(v), s_c), wt_c(v) := sgn(v)·2^rank(v) if rank(v) > rank(c), else 0.»
- Fix a phase, a cycle node c, U := U_c (constant on the phase), wt := wt_c, wt(Z) := Σ_{v∈Z} wt(v). M_t(z) := wt(P(Ξ_t z)) for z ∈ U. For a
  valuation x with cycle node c, Mx := wt(P(x)); MW_t(z) := wt(P(W_t z)) when W_t(z) has cycle node c.
- A_t := F_D(t) ∩ U. An Odd u ∈ U is a D-DIRECT GATE at t (u ∈ DD_t) if u ∈ D_t, σ̄_t(u) ∈ A_t and τ(u) ∈ A_t. Its OFFSET is
  Δ_t(u) := M_t(τ u) − M_t(σ̄_t u). R_u(t) := {z ∈ U : the first D_t-vertex of z's (σ_t, τ)-play is u}; E_t := A_t ∪ R_u(t);
  off_t(z) := 0 on A_t and Δ_t(u) on R_u(t); N_t(z) := MW_t(z) for z ∈ E_t.
- G′[E]: the graph on E in which every A-vertex keeps its edges into A (Even) or its τ-edge if it lies in A (Odd); every R_u-vertex keeps its
  edges into E (Even) or its τ-edge if it lies in E (Odd, u included); c is a sink. MoptG′[E](z) := the best wt-weight of a simple G′[E]-path
  from z to c (−∞ if none).
- A G-INTERVAL for u: states [s, e] of the phase such that every transition t → t+1 (s ≤ t < e) is an S4a step, u ∈ DD_t for all t ∈ [s, e],
  A_{t+1} ⊆ A_t, R_u(t+1) ⊆ R_u(t), and Δ_t(u) = Δ is constant.
- A positional play is a lasso, and every vertex of its cycle is visited before the first repetition. For a play that ends on c's cycle, its
  path weight (the wt-sum over its vertex set P) is the wt-sum over all its distinct vertices: a vertex of nonzero wt has rank > rank(c) and
  is not on the cycle, whose top is c.
### 1.2 Premises (LANDED RESULTS entries, every game)
- (Aκ), (A0κ), (M1κ), (M2κ): [Q docs/RESULTS.md@a7c141b8:2851] «(a) Facts (Aκ), (A0κ), (M1κ), (M2κ), (INJ), (SP′) per honest class», with
  (Aκ) as stated in its packet [Q docs/new/P-N5-FBRED-box44.md@3732ab55:49-50] «(Aκ): for z ∈ U_c ∖ {c}: λ_t(z) = c ≠ z, so (V1) gives Ξ_t(z) =
  z ⊕ Ξ_t(next_t z) with cycle node c; next_t(z) ∈ U_c, and κ_t(z) = κwt_c(z) + κ_t(next_t z)». Used in the forms: M_t(z) = wt(z) +
  M_t(next_t z) for z ∈ U ∖ {c} (next_t := σ_t at Even, σ̄_t at Odd vertices); M_t(c) = 0; (M1κ) for valuations x, x′ with cycle node c:
  x ⊴ x′ ⇔ (Mx, s_c·ℓ(x)) ≤ (Mx′, s_c·ℓ(x′)) lexicographically (a fact about valuations, used for W-values too); (M2κ) M_{t+1}(z) ≥ M_t(z) at
  in-phase transitions.
- (F1) [Q docs/RESULTS.md@a7c141b8:738-739] «(F1)/(F2) (the optimum of a one-player game dominates every strategy of that game pointwise»,
  on S4a's arena H_t in G_τ; (V1) is RESULTS R17 (a) as well. XW [Q docs/RESULTS.md@a7c141b8:933] «(a) Lemma XW: Ξ_k ⊴ W_k pointwise at every
  state». Both are game-general by [Q docs/RESULTS.md@a7c141b8:2792-2794] «R17 (a)-(c), R18 (c) flat case, R18 (d) Lemma S (c) in its landed
  "⇒" form, R21 (a) XW, R21 (c) FBL-N (i), each signed under a 𝒞^1O setting line, whose proofs both referees read and CONFIRM use no one-Odd
  step (R17 and R18's flat case are one-player statements, applied to G_τ, its arenas and 𝓕, which are one-player on every game; XW is VJ00
  (11) on G_σ)».
- G_D (a) [Q docs/RESULTS.md@a7c141b8:2798] «(a) Lemma G_D (a) (no hypothesis): for every state k and every v ∈ F_D, Ξ_k(v) = W_k(v).»
- κ-Y-FORM_D [Q docs/RESULTS.md@a7c141b8:2858-2859] «(d) κ-Y-FORM_D (per q ∈ Q ∩ U_c, q ≠ c, at a state t where q lies on no honest cycle):
  κ_t(q) = κwt_c(q) + min over y ∈ Y^q_t of κ_t(y), with Y^q_t := {y ∈ succ(q) ∩ U_c : y's honest play at t avoids q}».
- WM-G (RESULTS R62 (d)), with its setting [Q docs/RESULTS.md@a7c141b8:3276] «Ω_k := W_k, the valuation of σ_k in the fixed one-player game G_τ»
  and [Q docs/RESULTS.md@a7c141b8:3286] «(d) Lemma WM-G: for every transition k → k+1 of a run S, Ω_{k+1} ⊵ Ω_k pointwise.» (S: a run of
  in-phase S4a transitions.)
- Rewards are injective (SPEC S1), and values with different cycle nodes are ordered by the rewards of their cycle nodes first.
### 1.3 Items of P-N5-ROOT-box20 used (by name; sha1 d3788bc0)
- Lemma BF-F_D (its §2) and Theorem FREEZE-A (a)-(c) with its hypothesis "every transition of [s, e] is an S4a step and A_{t+1} ⊆ A_t" (its §3),
  in FREEZE-G (a) (A-vertices) and in RELAY-PIECE. Lemma DL-SPLIT is not used.

## 2. Lemma GATE-SHIFT
Statement.
- (a) At a state t, for z ∈ U whose first D_t-vertex u := u(z) lies in DD_t: W_t(z) has cycle node c, Δ_t(u) ≥ 0, and M_t(z) = MW_t(z) − Δ_t(u).
- (b) At an in-phase S4a transition t → t+1, for Even z ∈ U, z ≠ c, whose first D_{t+1}-vertex u lies in DD_{t+1}, and every successor x ∈ U of z
  whose (σ_t, τ)-play avoids z: MW_{t+1}(z) ≥ wt(z) + M_t(x); hence M_{t+1}(z) ≥ wt(z) + M_t(x) − Δ_{t+1}(u).
Proof.
- (a) Let π be z's (σ_t, τ)-path before u. Its Odd vertices are not in D_t, so σ̄_t = τ there: z's honest play is π, u, then σ̄_t(u)'s play; its
  W-play is π, u, then τ(u)'s play. Both continuations lie in A_t ⊆ F_D(t): they avoid D_t, hence avoid u, and are disjoint from π, whose
  vertices lie in R_D(t). τ(u)'s play is its honest play and W = Ξ on it (G_D (a)), with cycle node c (τ(u) ∈ U). So both plays end on c's
  cycle, z is on neither cycle, and by §1.1's last item M_t(z) = wt(π) + wt(u) + M_t(σ̄_t u) and MW_t(z) = wt(π) + wt(u) + M_t(τ u).
  τ(u)'s honest play avoids D_t ∋ u, so τ(u) ∈ Y^u_t; u lies on no honest cycle (σ̄_t(u)'s play avoids u); by κ-Y-FORM_D and (Aκ), the minimum
  of κ_t over Y^u_t is attained at σ̄_t(u), and κ compares M first: M_t(σ̄_t u) ≤ M_t(τ u), i.e. Δ_t(u) ≥ 0.
- (b) By (a) at t + 1, W_{t+1}(z) has cycle node c and M_{t+1}(z) = MW_{t+1}(z) − Δ_{t+1}(u). It remains to show MW_{t+1}(z) ≥ wt(z) + M_t(x).
  - Case 1, M_t(x) ≤ M_t(σ_t z). (Aκ): wt(z) + M_t(x) ≤ M_t(z). XW: Ξ_t(z) ⊴ W_t(z); WM-G: W_t(z) ⊴ W_{t+1}(z), which has cycle node c. If W_t(z)
    had a cycle node other than c, its reward would exceed reward(c) (it dominates Ξ_t(z), cycle node c), and so would W_{t+1}(z)'s: impossible.
    So all three have cycle node c and (M1κ) gives M_t(z) ≤ MW_t(z) ≤ MW_{t+1}(z).
  - Case 2, M_t(x) > M_t(σ_t z). σ_t(z) = next_t(z) ∈ U by (Aκ), so (M1κ) gives Ξ_t(x) ▷ Ξ_t(σ_t z): (z, x) ∈ Iσ_t and σ″ := σ_t[z ↦ x] is a
    strategy of H_t. (F1): W_{t+1}(z) ⊵ W_{σ″}(z). x's (σ_t, τ)-play avoids z, so it is also x's (σ″, τ)-play and (V1) gives W_{σ″}(z) =
    z ⊕ W_t(x). XW: W_t(x) ⊵ Ξ_t(x) (cycle node c); a cycle node other than c would have larger reward and pass to W_{σ″}(z) and W_{t+1}(z),
    impossible. So W_t(x) has cycle node c, MW_t(x) ≥ M_t(x) (M1κ), z ∉ P(W_t x), and (M1κ) on W_{t+1}(z) ⊵ z ⊕ W_t(x): MW_{t+1}(z) ≥
    wt(z) + MW_t(x) ≥ wt(z) + M_t(x). □

## 3. Theorem FREEZE-G
Statement. Let [s, e] be a G-interval for u (§1.1) and L := |E_s| − 1.
- (a) For t ∈ [s, e], z ∈ E_t and every simple path p of G′[E_t] from z to c with ≤ t − s edges: N_t(z) ≥ wt(p ∖ {c}).
- (b) For t ∈ [s, e] and z ∈ E_t: N_t(z) ≤ MoptG′[E_t](z). Hence for s + L ≤ t ≤ t′ ≤ e and z ∈ E_{t′}: N_{t′}(z) = N_t(z) and M_{t′}(z) =
  M_t(z).
- (c) For every Odd q ∈ U ∖ {u, c}: over the states t ∈ [s + L, e] with σ̄_t(q) ∈ E_t, M_t(q) lies in {wt(q) + M_{s+L}(y) : y ∈ succ(q) ∩
  E_{s+L}} (≤ deg(q) values), non-decreasingly; so ≤ deg(q) − 1 transitions t → t+1 in [s + L, e) with σ̄(q) ∈ E at both ends change M(q).
Proof.
- Facts on the interval. For z ∈ R_u(t): by GATE-SHIFT (a), W_t(z) has cycle node c and M_t(z) = N_t(z) − Δ, i.e. M_t = N_t − off_t on E_t (on
  A_t, N = M by G_D (a)). z's W-play is π_z, u, τ(u)'s play in A_t; for z ∈ R_u(t) ∖ {u}, the next vertex on it (σ_t(z) or τ(z)) lies in R_u(t),
  and N_t(z) = wt(z) + N_t(next) (§1.1's last item); N_t(u) = wt(u) + M_t(τ u). N is non-decreasing along the interval on R_u (z ∈ R_u(t+1) ⊆
  R_u(t); WM-G; both values have cycle node c) and on A ((M2κ)).
- (a) Induction on t − s; base: N_t(c) = 0. Step t → t+1: z ∈ E_{t+1}, z ≠ c, p = z · p′ with p′ from x, ≤ t − s edges. G′[E_{t+1}] ⊆ G′[E_t]
  (A and R_u non-increasing; the edge rule depends only on membership), so by induction N_t(x) ≥ wt(p′ ∖ {c}), and wt(p ∖ {c}) = wt(z) +
  wt(p′ ∖ {c}).
  - z ∈ A_{t+1}: x ∈ A_{t+1}, and the step of P-N5-ROOT FREEZE-A (a) applies verbatim (BF-F_D for Even z, the τ-edge and (Aκ), (M2κ) for Odd z).
  - z = u: x = τ(u) ∈ A_{t+1}; N_{t+1}(u) = wt(u) + M_{t+1}(τ u) ≥ wt(u) + M_t(τ u) = wt(u) + N_t(x).
  - z ∈ R_u(t+1) Odd, z ≠ u: z ∉ D_{t+1}, x = τ(z) is the next vertex, N_{t+1}(z) = wt(z) + N_{t+1}(x) ≥ wt(z) + N_t(x).
  - z ∈ R_u(t+1) Even: z ∈ R_u(t) and σ_t(z) ∈ R_u(t), so off_t(σ_t z) = Δ ≥ off_t(x) for x ∈ E_t.
    - Case 1, M_t(x) ≤ M_t(σ_t z): N_t(x) − off_t(x) ≤ N_t(σ_t z) − Δ, so N_t(x) ≤ N_t(σ_t z), and wt(z) + N_t(x) ≤ N_t(z) ≤ N_{t+1}(z).
    - Case 2, (z, x) ∈ Iσ_t: σ″ := σ_t[z ↦ x] lies in H_t, and (F1) gives W_{t+1}(z) ⊵ W_{σ″}(z). If x's (σ_t, τ)-play avoids z, GATE-SHIFT (b)'s
      Case 2 argument with MW_t(x) = N_t(x) gives N_{t+1}(z) ≥ wt(z) + N_t(x). If it passes z, it is q · z · (z's play), with z ∉ q, and N_t(x) =
      wt(q) + N_t(z) (§1.1's last item; a vertex of q on z's play lies on z's cycle and has wt 0). Under σ″, z's play is the cycle Z := z → x →
      q → z. If wt(Z) > 0, Z's top is even of rank > rank(c), W_{σ″}(z) has that cycle node, and W_{t+1}(z) ⊵ W_{σ″}(z) contradicts W_{t+1}(z)'s
      cycle node c. So wt(Z) = wt(z) + wt(q) ≤ 0 and wt(z) + N_t(x) = wt(Z) + N_t(z) ≤ N_t(z) ≤ N_{t+1}(z).
- (b) z ∈ E_t: z's W-play up to c is a simple path of G′[E_t] (inside R_u: σ_t- and τ-edges into R_u; u's τ-edge into A; inside A: edges into A),
  so N_t(z) = its weight ≤ MoptG′[E_t](z). Simple paths of G′[E_t] have ≤ |E_t| − 1 ≤ L edges, so for t ≥ s + L (a) gives equality; for
  s + L ≤ t ≤ t′ and z ∈ E_{t′} ⊆ E_t: N_{t′}(z) = MoptG′[E_{t′}](z) ≤ MoptG′[E_t](z) = N_t(z) ≤ N_{t′}(z). M = N − off, and off is constant
  on the interval (0 on A, Δ on R_u).
- (c) Let t ∈ [s + L, e] with y := σ̄_t(q) ∈ E_t.
  - q ∉ D_t: q's honest play and its W-play agree up to their first D_t-vertex and are q followed by y's, so q ∈ E_t ⊆ E_{s+L} and M_t(q) =
    M_{s+L}(q) by (b); and q ∉ D_{s+L} (q ∈ E_{s+L} ∖ {u}), so (Aκ) gives M_{s+L}(q) = wt(q) + M_{s+L}(τ q) with τ q on q's play, τ q ∈ E_{s+L}.
  - q ∈ D_t: q's honest play is q then y's play, which does not return to q (y ∈ A_t: it avoids D_t ∋ q; y ∈ R_u(t): it is π_y, u, σ̄_t(u)'s
    play in A_t, and π_y has no D_t-vertex). So q is on no honest cycle, and (Aκ) gives M_t(q) = wt(q) + M_t(y) = wt(q) + M_{s+L}(y) by (b)
    (y ∈ E_t ⊆ E_{s+L}).
  - M(q) is non-decreasing on the phase ((M2κ)). □

## 4. Corollary RELAY-PIECE
Statement. Let [s, e] satisfy P-N5-ROOT FREEZE-A's hypothesis, L_A := |A_s| − 1, and let u ∈ DD_t for every t ∈ [s, e] with R_u(t+1) ⊆ R_u(t)
for s ≤ t < e. Then:
- (i) over the states t ∈ [s + L_A, e], Δ_t(u) takes ≤ deg(u) values, so [s + L_A, e] is the union of ≤ deg(u) G-intervals for u (consecutive
  ones sharing a transition at which Δ changes);
- (ii) for every Odd q ∈ U ∖ {u, c}, the transitions t → t+1 in [s + L_A, e) with σ̄(q) ∈ E at both ends that change M(q) number ≤ deg(u)·(|U| − 1
  + deg(q)).
Proof.
- (i) For t ∈ [s + L_A, e]: τ(u) ∈ A_t, so M_t(τ u) = M_{s+L_A}(τ u) by FREEZE-A (b); u ∈ D_t with σ̄_t(u) ∈ A_t, so M_t(σ̄_t u) = M_{s+L_A}(σ̄_t u)
  ∈ {M_{s+L_A}(y) : y ∈ succ(u) ∩ A_{s+L_A}} by FREEZE-A (b). So Δ_t(u) takes ≤ deg(u) values; M(u) = wt(u) + M(σ̄ u) is non-decreasing (M2κ),
  so M(σ̄ u) and hence Δ(u) move monotonically (Δ non-increasing), and each value is taken on one block of consecutive states. Each block is a
  G-interval (the other conditions hold on all of [s, e]).
- (ii) In each of the ≤ deg(u) G-intervals [s′, e′], ≤ |E_{s′}| − 1 ≤ |U| − 1 transitions lie before s′ + |E_{s′}| − 1, and ≤ deg(q) − 1 counted
  ones after it (FREEZE-G (c)); the ≤ deg(u) − 1 boundary transitions count once each. Sum: ≤ deg(u)(|U| − 1 + deg(q) − 1) + deg(u) − 1 ≤
  deg(u)(|U| − 1 + deg(q)). □

## 5. DATA (not to sign; experiments/si/root/bfgate.py, freezeg.py; logs experiments/si/root/logs/)
- GATE-SHIFT (bfgate.py, GS_A_V / GS_B_V): (a) 684 / 404 / 4,366 / 5,420 checks and (b) 943 / 661 / 5,868 / 7,044 checks on nep90 / nep76 /
  lib2o (KMIN 2, S3 + 4) / lib41 (KMIN 2, S3 + 4), 0 failures. Control: (b) with Δ := 0 (column BFG_fail): 188 / 138 / 387 / 568 failures.
- FREEZE-G (a) (freezeg.py, walk Bellman-Ford on G′[E_t] with ≤ t − s edges, simple witness by DFS when it exceeds N_t(z)):
  | set | G-intervals | checks (binding) | failures |
  | --- | --- | --- | --- |
  | nep90_n40 phase@4 / nep76_n40 phase@9 | 22 / 25 | 2,531 (332) / 2,386 (214) | 0 / 0 |
  | lib2o (KMIN 2), S3 + 4 | 120 | 15,878 (3,555) | 0 |
  | lib41 (KMIN 1), S3 + 4 | 729 | 95,488 (21,311) | 0 |
  Control MUT=1 (one more edge than (a) allows): bites on lib41 (11 failures, first so_sor5_n24); does NOT bite on nep90, nep76, lib2o.
- FREEZE-G (b), (c) and RELAY-PIECE are VACUOUS in the data: no G-interval is longer than |E_s| − 1 (0 of 22 / 25 / 120 / 729).

## 6. READING (not to sign)
- GATE-SHIFT (b) with Δ > 0 is where "Fact B across gates" fails (P-N5-ROOT §6): an Even z behind a gate with a large offset keeps a W-better
  route through the gate while a Ξ-improving direct option exists, so its honest value lags by up to Δ (GATE-LAG; nep90 phase@4, the root 0,
  gap rank 36-39 of 40, 188 lagging pairs). FREEZE-G shows the W-frame step is nevertheless exact on the gate region, so the lag is a constant
  shift while Δ is constant.
- RELAY-PIECE bounds a relay's re-routings between consecutive resets of its gate (offset changes, region gains). The open count is the number
  of such resets inside one fallback-free run; for the root it is ρ at the root plus the ping-pong entries into its region.
