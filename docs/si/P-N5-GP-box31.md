# P-N5-GP (box 31): in every frozen W-phase of N5, the W-frame Lemma P holds for every path that avoids BLOCKED edges (Lemma GP*), so a frozen W-phase has at most (n − 1)(R*_T + 1) W-changing transitions, R*_T the transitions that adopt a previously blocked edge (Corollary FW-R*)
L-SI successor 27 (Opus 5.5; D18, Lead reading L40). Packet for the referees, FROZEN at its push; the sha1 goes to the Lead; repairs go in a
NEW file docs/si/P-N5-GP-fixes-box31.md. Lead 2026-10-29 16:24Z: «Freeze it as a packet (docs/si/P-N5-GP-box31.md or your naming) with these
contents: definitions from SPEC/RESULTS and N5-FRZ-box29 §0, restated in the packet; the proofs of W-MON and XW included, as you propose;
premises named: SPEC S1-S5, R17 (a) (V1)/(V2)/(F1) and (b); the pinned check core/gp.py on ccl_w48_n48 and rlin_cex_n40 with the MUT=all
control; a quote check of R17 (b) Case A/B.» Lead 16:31Z: «Yes, freeze the GP* form ... Include GP and GP+ as stated corollaries of GP*, so a
referee can sign the special cases even if GP* gets a gap.» Working note with data: docs/si/N5-SPC-box31.md §3-§6. Labels (D18 / L40): PROVED (lane,
unrefereed) / DATA / READING.
SCOPE (D1): a REDUCTION, per frozen W-phase only, not a bound on the run. Not a TARGET.md claim, not an algorithm claim, no running-time
bound (R*_T is NOT bounded here; FW-BF and G-N5-TIME stay OPEN). Every [Q path@commit:lines] «…» below is verbatim, checked by
experiments/si/rund/quotecheck.py (pinned in experiments/si/check.sh with a shifted-line control that must fail).

## 0. What to sign, and what not
| § | statement | label |
| --- | --- | --- |
| §2 | Lemma W-MON (W rises at every non-fallback in-phase transition) and Lemma XW (Ξ ⊴ W), any game | PROVED (to sign) |
| §3 | Lemma GP* (W-frame Lemma P for unblocked paths, every frozen W-phase of every game) | PROVED (to sign) |
| §3a | Corollaries GP and GP+ (the special cases: paths whose Even edges are σ's choice, Ξ-improving, into U, or inside one same-pair tail-disjoint basin); each also follows from §3's Case A / Case B directly | PROVED (to sign separately) |
| §4 | Corollary FW-R* (WCH ≤ (n − 1)(R*_T + 1) per frozen W-phase) | PROVED (to sign) |
| §5 | special cases and what is not claimed | READING (NOT to sign) |
| §6 | data and pinned check | DATA (NOT to sign) |

## 1. Setting, symbols, premises
- N5 = SPEC S1-S5 of docs/new/N5-ssi-global.md (FIX 1-4 as in RESULTS); any parity game G = (V, E, Ω, owner), n = |V|. A run is the sequence of
  states (σ_t, τ_t); a TRANSITION is t → t + 1.
- [S1-val] [Q docs/new/N5-ssi-global.md@2a435f8f4:28-29] «valuation of v under (σ, σ̄): (c, P, ℓ), c = the most relevant (max p') vertex of
  the cycle the play from v ends in, P = set of vertices on the play before reaching c with p' > p'(c), ℓ = number of steps to reach c.»
  The same definition applied to the (σ, τ)-play gives W below.
- [S1-ord] [Q docs/new/N5-ssi-global.md@2a435f8f4:30-31] «order (better for Even): compare reward of c (p'(c) if even, −p'(c) if odd); then P
  by the signed weight Σ_{u∈P} (+2^rank(u) if Ω(u) even else −2^rank(u)); then ℓ: if c is odd, longer is better for Even; if c even, shorter
  is better.» ⊴ / ◁ denote this order (◁ strict), ⊵ / ▷ the reverse. Distinct values are distinct in the order (rewards of distinct
  vertices differ; distinct rank sets have distinct signed weights, RESULTS R84 (a) Fact DELTA).
- [S1-Xi] [Q docs/new/N5-ssi-global.md@2a435f8f4:32] «Ξσ = valuation of every vertex under σ and Odd's OPTIMAL counterstrategy σ̄ (minimising
  this order at every vertex at once).» Ξ_t := Ξ_{σ_t}, σ̄_t := that counterstrategy.
- [S2] [Q docs/new/N5-ssi-global.md@2a435f8f4:47] «Improving edges: Iσ = {(v, w) : owner(v) = Even, w ≠ σ(v), Ξσ(w) strictly better than
  Ξσ(σ(v))}; Iτ the same on G^d for τ.»
- [S4a] [Q docs/new/N5-ssi-global.md@2a435f8f4:51-54] «a. If Iσ ≠ ∅: A(v) = {σ(v)} ∪ {w : (v, w) ∈ Iσ} for Even v. Arena H: Even v keeps only
  edges to A(v); Odd v keeps only the edge to τ(v). σ_new = Odd's optimal counterstrategy (S1 procedure) in the dual of H to the dual-Even
  strategy τ, read as an Even strategy of G. (Even's one-player optimum against τ among "keep or take an improving edge".) Else σ_new = σ.»
- [S4c] [Q docs/new/N5-ssi-global.md@2a435f8f4:56] «c. FALLBACK, if σ_new = σ and τ_new = τ:»
- [STEP] RESULTS R15 (d): [Q docs/RESULTS.md@2a435f8f4:640-642] «(d) N5: every iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ (on G)
  and/or with ∅ ≠ I ⊆ Iτ to Odd's τ (on G^d), and changes at least one of them».
- R17's facts, as signed (RESULTS R17 (a)) and as stated in its object docs/new/N5-phase-bound-box10.md §1 (H a one-player game, ρ a strategy
  of the player who moves, Ω_ρ the VJ00 valuation of ρ's plays):
  [F1] [Q docs/new/N5-phase-bound-box10.md@2a435f8f4:16] «(F1) the optimum of a one-player game dominates every strategy of that game pointwise»
  [PRE] [Q docs/new/N5-phase-bound-box10.md@2a435f8f4:13-14] «Prefix: x ⊕ (c, P, ℓ) := (c, P ∪ {x if x more relevant than c}, ℓ + 1); this is
  the value of a play that steps from x to a vertex of value (c, P, ℓ) whose path to c avoids x.»
  [V1] [Q docs/new/N5-phase-bound-box10.md@2a435f8f4:20-21] «(V1) if x is not its own cycle node then Ω_ρ(x) = x ⊕ Ω_ρ(ρ(x)) and the ρ-path from
  ρ(x) to λ(x) avoids x.»
  [V2] [Q docs/new/N5-phase-bound-box10.md@2a435f8f4:21-22] «(V2) PREFIX MONOTONICITY: if a ⪯ b are values whose paths both avoid x (or whose
  cycle nodes differ), then x ⊕ a ⪯ x ⊕ b, and strictly if a ≺ b.»
  [VAL] [Q docs/new/N5-phase-bound-box10.md@2a435f8f4:27-28] «For a simple path r = (x = r_0, r_1, …, r_L = u) in H with L ≤ k edges let
  value(r) := (u, P(r), L), P(r) = {r_i : i < L, r_i more relevant than u}»
  [CASE-A] R17 (b)'s Case A, used verbatim in §3 (with Ω_k := W_k and I_k replaced by the hypothesis «W_k(z) ⊴ W_k(ρ_k(x))»):
  [Q docs/new/N5-phase-bound-box10.md@2a435f8f4:32-37] «Case A: (x, z) ∉ I_k, i.e. Ω_k(z) ⪯ Ω_k(ρ_k(x)). So value(r') ⪯ Ω_k(ρ_k(x))
  (transitivity). A1: x is not its own cycle node. By (V1) and (V2) (both paths avoid x; or cycle nodes differ): value(r) = x ⊕ value(r') ⪯ x
  ⊕ Ω_k(ρ_k(x)) = Ω_k(x) ⪯ Ω_{k+1}(x) by (F2).… A2: x = λ_k(x) (its own cycle node), so Ω_k(x) = (x, ∅, 0). If x is better than u, Ω_k(x) ≻
  value(r). If x is worse than u: Ω_k(ρ_k(x)) has cycle node x and value(r') has cycle node u, so value(r') ≻ Ω_k(ρ_k(x)), contradicting
  value(r') ⪯ Ω_k(ρ_k(x)).»
  [CASE-B] R17 (b)'s Case B, whose sub-case structure §3 follows: [Q docs/new/N5-phase-bound-box10.md@2a435f8f4:38-39] «Case B: (x, z) ∈ I_k,
  i.e. Ω_k(z) ≻ Ω_k(ρ_k(x)). Then ρ̂ := ρ_k[x → z] is a strategy of the arena H_k, so by (F1) Ω_{k+1}(x) ⪰ val_ρ̂(x). Let c := λ_k(z) and π :=
  the ρ_k-path from z to c (simple, z first, c last).» Case A of R17 uses only «Ω_k(z) ⪯ Ω_k(ρ_k(x))» and (V1), (V2), (F2); §3 re-proves
  every Case B sub-case without the improvement «Ω_k(z) ≻ Ω_k(ρ_k(x))».
- [FRZ] A FROZEN W-PHASE (docs/si/N5-FRZ-box29.md §0, restated): W_t := the valuation [S1-val] of the (σ_t, τ_t)-plays, λ_W its cycle-node
  map, λ_t := Ξ_t's cycle-node map. A PHASE is a maximal run of states with (λ_t, τ_t) constant (RESULTS R38 (a)). A frozen W-phase F = [a, b]
  is a maximal run of consecutive states of one phase such that no transition t → t + 1 with a ≤ t < b is an S4c fallback, changes λ_W, or
  changes σ̄. On F: τ := τ_t, σ̄ := σ̄_t, D := {Odd u : σ̄(u) ≠ τ(u)}, λ_Ξ and λ_W are constant. ρ_t := σ_t. G_τ := G with Odd fixed to τ (a
  one-player game of Even); W_t = Ω_{ρ_t} in G_τ.
- [H] For t ∈ [a, b): H_t := the arena of [S4a] at state t (Even v keeps {ρ_t(v)} ∪ Iσ_t(v), Odd v keeps τ(v)), a one-player game.

## 2. Lemma W-MON and Lemma XW (proofs included, as the Lead asked)
Lemma W-MON. Let t → t + 1 be a transition inside a phase that is not an S4c fallback. Then ρ_{t+1} is an optimal strategy of H_t in G_τ's
valuation, and W_{t+1}(v) ⊵ W_t(v) for every v.
Proof. τ_{t+1} = τ_t = τ (phase). By [STEP] the transition changes σ or τ, so σ_{t+1} ≠ σ_t; it is not a fallback, so σ_{t+1} = [S4a]'s σ_new
with Iσ_t ≠ ∅ (if Iσ_t = ∅, σ_new = σ_t). By [S4a], σ_new is Even's one-player optimum in H_t against τ: the optimal strategy of the
one-player game H_t. The (σ, τ)-plays of G and of H_t coincide for every σ whose edges lie in H_t, in particular for ρ_t (ρ_t(v) ∈ A(v)) and
for ρ_{t+1}. By [F1] applied to H_t: W_{t+1} = Ω_{ρ_{t+1}} ⊵ Ω_{ρ_t} = W_t pointwise. □
Lemma XW. Ξ_t(v) ⊴ W_t(v) for every v and t; and Ξ_t(v) = W_t(v) whenever the (σ_t, τ_t)-play from v meets no vertex of D_t := {Odd u :
σ̄_t(u) ≠ τ_t(u)}.
Proof. Ξ_t is the valuation under σ_t and σ̄_t, which minimises the order at every vertex at once [S1-Xi]; τ_t is one Odd strategy, so
Ξ_t(v) ⊴ W_t(v). If the (σ_t, τ_t)-play from v meets no u with σ̄_t(u) ≠ τ_t(u), the (σ_t, σ̄_t)-play from v is the same play, so the
valuations are equal. □

## 3. Lemma GP* (W-frame Lemma P for unblocked paths)
Definitions (F = [a, b] a frozen W-phase). An edge (x, z) of G with x Even is BLOCKED at state t ∈ [a, b) if W_t(z) ▷ W_t(ρ_t(x)) and (x, z) ∉
Iσ_t. A path r = (x = r_0, r_1, …, r_L = u) of G_τ (Odd r_i: r_{i+1} = τ(r_i)) is UNBLOCKED AT STATE k (a ≤ k ≤ b) if it is simple, u is a
cycle node of state a (λ_W(u) = u), L ≤ k − a, and for every i < L with r_i Even the edge (r_i, r_{i+1}) is not blocked at state k − 1 − i.
value(r) := (u, P(r), L) as in [VAL].
Lemma GP*. For every k ∈ [a, b] and every path r unblocked at state k: W_k(r_0) ⊵ value(r).
Proof. Induction on k. k = a: L = 0, r = (u), W_a(u) = (u, ∅, 0) = value(r) (u is its own W cycle node; nothing on its path is more relevant).
Step k → k + 1 (k + 1 ≤ b): let r be unblocked at state k + 1, L ≥ 1 (L = 0 as in the base: λ_W is constant on F, so W_{k+1}(u) = (u, ∅, 0)).
Write r = x → z → r′. Then r′ is simple, avoids x, has ≤ k − a edges, and its i-th Even edge is not blocked at state k − 1 − i (it is edge
i + 1 of r): r′ is unblocked at state k, so by induction W_k(z) ⊵ value(r′). The first edge (x, z) is not blocked at state k (or x is Odd).
By W-MON, W_{k+1} ⊵ W_k pointwise (the transition k → k + 1 lies in F, so it is not a fallback).
Case A: x Odd (z = τ(x) = ρ_k(x) in G_τ), or z = ρ_k(x), or (x, z) ∉ Iσ_k. In each, W_k(z) ⊴ W_k(ρ_k(x)) (trivially for z = ρ_k(x); for
  (x, z) ∉ Iσ_k because (x, z) is not blocked), so value(r′) ⊴ W_k(ρ_k(x)), and [CASE-A] (A1, A2) read with Ω := W gives value(r) ⊴ W_k(x) ⊴
  W_{k+1}(x). ([CASE-A] uses only this inequality, [V1], [V2] and W_{k+1} ⊵ W_k.)
Case B: x Even, (x, z) ∈ Iσ_k. ρ̂ := ρ_k[x → z] is a strategy of H_k ([H]), so by W-MON's first part and [F1] in H_k: W_{k+1}(x) ⊵ val_ρ̂(x)
  (the value of the ρ̂-play in G_τ). Let c := λ_W(z) and π := the ρ_k-path from z to c in G_τ (simple, z first, c last). The improvement of
  (x, z) is in Ξ, not in W; it is NOT used below.
  B1: x ∉ π and x not on c's ρ_k-cycle. The ρ̂-play from x is x, π, then c's unchanged cycle, so val_ρ̂(x) = x ⊕ W_k(z) ⊵ x ⊕ value(r′) =
      value(r) by [V2] (π and r′ avoid x; or the cycle nodes differ).
  B1′: x ∉ π, x on c's ρ_k-cycle (so λ_W(x) = c, every vertex of that cycle other than c is less relevant than c, and W_k(x) = (c, ∅, ℓ_x)).
      The ρ̂-play from x is the cycle Z = x, π, then the arc of c's old cycle from c back to x; the vertices of Z more relevant than c are
      exactly P(π). (i) P(π) = ∅: top(Z) = c and val_ρ̂(x) = (c, ∅, |π| + 1) = x ⊕ W_k(z) ⊵ value(r) by [V2]. (ii) P(π) ≠ ∅ with its most
      relevant vertex even: top(Z) is that vertex, its reward exceeds c's, so W_{k+1}(x) ⊵ val_ρ̂(x) has a cycle node better than c, i.e.
      λ_W(x) changes at k + 1: impossible in F. (iii) P(π) ≠ ∅ with its most relevant vertex odd: W_k(z) = (c, P(π), |π|) is worse than every
      value (c, ∅, ·) (its P-set has negative signed weight relative to ∅ at the top differing rank). value(r′) ⊴ W_k(z) gives: if value(r′)
      has cycle node u = c, its P-set compares below ∅ in the same way; if u ≠ c, reward(u) < reward(c). x is less relevant than c, so in
      both cases value(r) = x ⊕ value(r′) ◁ (c, ∅, ℓ_x) = W_k(x) ⊴ W_{k+1}(x).
  B2: x ∈ π. Then λ_W(x) = c and the ρ̂-play from x is the cycle Z = x, z, π[z..x) (π up to but excluding x).
      B2a, x = c (x is its own W cycle node, W_k(x) = (x, ∅, 0)): r′ avoids x, so its end u ≠ x; value(r′) ⊴ W_k(z), whose cycle node is x,
      so reward(u) < reward(x) (distinct vertices have distinct rewards), and value(r) = x ⊕ value(r′) has cycle node u: value(r) ◁ (x, ∅, 0)
      = W_k(x) ⊴ W_{k+1}(x).
      B2b, x ≠ c: W_k(x) = x ⊕ W_k(ρ_k(x)) [V1], W_k(z) = π[z..x) ⊕ W_k(x) (prefix by prefix), and c ∉ Z (c is the last vertex of the simple
      path π, after x). Let D′ := P(π[z..x)) ∪ ({x} if x is more relevant than c): the symmetric difference of the P-sets of W_k(z) and
      W_k(ρ_k(x)) (π[z..x) and x's path to c are disjoint parts of π), and the set of vertices of Z more relevant than c. (i) D′ ≠ ∅, top even:
      top(Z) is that vertex, with a better reward than c, so W_{k+1}(x) ⊵ val_ρ̂(x) forces a cycle node other than c at k + 1: λ_W(x) changes,
      impossible in F. (ii) D′ ≠ ∅, top odd: W_k(z) ◁ W_k(ρ_k(x)). (iii) D′ = ∅: every vertex of Z is less relevant than c; if c is odd, every
      less relevant vertex has a better reward than c, so λ_W(x) changes as in (i): impossible; if c is even, W_k(z) has the same P-set as
      W_k(ρ_k(x)) and a longer path, so W_k(z) ◁ W_k(ρ_k(x)). In (ii) and (iii) value(r′) ⊴ W_k(z) ◁ W_k(ρ_k(x)), and Case A's argument (A1,
      x not its own cycle node) gives value(r) ⊴ W_k(x) ⊴ W_{k+1}(x).
  In every case W_{k+1}(x) ⊵ value(r). □

## 3a. Corollaries GP and GP+ (the special cases, stated separately so that each can be signed on its own)
Definitions (F = [a, b], state t ∈ [a, b)). U_t := the vertices whose (ρ_t, τ)-play meets no vertex of D. For d ∈ D, S_{d,t} := the vertices
whose (ρ_t, τ)-play meets D first at d (d ∈ S_{d,t}). A gate d is SAME-PAIR if λ_Ξ(d) = λ_W(d) (constant on F), and TAIL-DISJOINT at t if
neither the (ρ_t, τ)-play nor the (ρ_t, σ̄)-play from d meets S_{d,t} again after d. For Even x: ALLOWED(x, t) := {ρ_t(x)} ∪ Iσ_t(x) ∪ (x's
successors in U_t); ALLOWED⁺(x, t) := ALLOWED(x, t) ∪ {z successor of x : x, z ∈ S_{d,t} for a same-pair gate d tail-disjoint at t}. A path r
is TIMELY (TIMELY⁺) AT STATE k if it is as in §3's «unblocked» with «not blocked at state k − 1 − i» replaced by «r_{i+1} ∈ ALLOWED(r_i,
k − 1 − i)» (ALLOWED⁺).
Corollary GP. W_k(r_0) ⊵ value(r) for every path r timely at state k.  Corollary GP+. The same for every path timely⁺ at state k.
Proof. By Lemma GP* it suffices that no z ∈ ALLOWED⁺(x, t) is blocked at t. z = ρ_t(x): blocked needs W_t(z) ▷ W_t(ρ_t(x)), false.
(x, z) ∈ Iσ_t: blocked needs (x, z) ∉ Iσ_t, false. z ∈ U_t, (x, z) ∉ Iσ_t: W_t(z) = Ξ_t(z) (Lemma XW, second part) ⊴ Ξ_t(ρ_t(x)) ([S2], not
improving) ⊴ W_t(ρ_t(x)) (Lemma XW): not blocked. x, z ∈ S_{d,t}, d same-pair and tail-disjoint at t, (x, z) ∉ Iσ_t: ρ_t(x) ∈ S_{d,t} (x is
Even, d Odd, so x ≠ d, and x's play continues as ρ_t(x)'s). For y ∈ S_{d,t} let p(y) := the (ρ_t, τ)-play from y up to and excluding d; it
avoids D, so it is also the (ρ_t, σ̄)-play from y up to d, and by tail-disjointness it is disjoint from both continuations of d. Applying
[V1] / [PRE] vertex by vertex: W_t(y) = p(y) ⊕ W_t(d) and Ξ_t(y) = p(y) ⊕ Ξ_t(d), where W_t(d) and Ξ_t(d) have the same cycle node c
(same pair). For two such prefixes p, q and any value A with cycle node c whose path avoids p and q, p ⊕ A vs q ⊕ A is decided by the
symmetric difference of {v ∈ p : v more relevant than c} and {v ∈ q : v more relevant than c}, and then by |p| vs |q| ([S1-ord]): it does
not depend on A. So Ξ_t(z) ⊴ Ξ_t(ρ_t(x)) (not improving) gives W_t(z) ⊴ W_t(ρ_t(x)): not blocked. □

## 4. Corollary FW-R*
Definition. A LATE ADOPTION in F is a transition τ → τ + 1 of F (a ≤ τ < b) at which some Even y switches, ρ_{τ+1}(y) = z ≠ ρ_τ(y), to an
edge (y, z) that was blocked at some state t ∈ [a, τ). R*_T := the number of transitions of F containing at least one late adoption.
WCH := the number of transitions t → t + 1 of F with W_{t+1} ≠ W_t.
Corollary FW-R*. Every frozen W-phase F of N5 on every game has WCH ≤ (n − 1)(R*_T + 1). In particular, if no previously blocked edge is ever
adopted in F (R*_T = 0), then WCH ≤ n − 1.
Proof. The transitions k → k + 1 with a ≤ k < a + n − 1 are at most n − 1. Let k ≥ a + n − 1, k < b, and W_{k+1}(x) ≠ W_k(x). Let π = (y_0 =
x, …, y_L = u) be the ρ_{k+1}-play from x in G_τ up to its cycle node u = λ_W(x) (constant on F, so u is a cycle node of state a). π is simple,
L ≤ n − 1 ≤ k − a, and value(π) = W_{k+1}(x) ([S1-val]). If π were unblocked at state k, Lemma GP* would give W_k(x) ⊵ value(π) = W_{k+1}(x) ⊵
W_k(x) (W-MON), so W_{k+1}(x) = W_k(x) (distinct values are distinct in the order): contradiction. So for some i < L, y_i is Even and
(y_i, y_{i+1}) is blocked at t := k − 1 − i ≥ k − n + 1 ≥ a. A blocked edge is not ρ_t(y_i) and not in Iσ_t, so ρ_{t+1}(y_i) ≠ y_{i+1}
(ρ_{t+1}(y_i) ∈ {ρ_t(y_i)} ∪ Iσ_t(y_i), [S4a]); since ρ_{k+1}(y_i) = y_{i+1}, y_i adopts (y_i, y_{i+1}) at some transition τ → τ + 1 with
t < τ ≤ k: a late adoption, and k − τ ≤ k − t − 1 = i ≤ n − 2. Charge k to τ. A transition τ is charged only by k ∈ [τ, τ + n − 2], at most
n − 1 of them. So at most (n − 1)·R*_T transitions with k ≥ a + n − 1 change W. □

## 5. READING (not to sign): special cases, and what is not claimed
- D = ∅: every edge outside Iσ_k has W_k(z) = Ξ_k(z) ⊴ Ξ_k(ρ_k x) = W_k(ρ_k x) (Lemma XW), so nothing is blocked, R*_T = 0, and FW-R* gives ≤ n − 1
  W-changing transitions: R17 (b)-(c) on G_τ (box 29 Corollary FW-D0).
- Edges into U_k := {v : the (ρ_k, τ)-play from v avoids D} are never blocked (Lemma XW), and neither are edges inside one basin S_d of a gate d
  with λ_Ξ(d) = λ_W(d) whose continuations avoid S_d (prefix comparison; N5-SPC-box31 §3, GP+). So the blocked edges are the F1 refusals of
  docs/si/N5-TORD-box30.md §9: W-better edges refused by the Ξ-arena, into a vertex whose play meets D.
- Not claimed: any bound on R*_T; FW-BF (≤ n − 1 per frozen W-phase) in general; any bound on |F| (W-silent transitions) or on the number of
  frozen W-phases (fallbacks FB, σ̄-changes SBCH′: box 29 W-SPLIT); anything about the whole run. FW-R* feeds box 29's W-SPLIT per frozen
  W-phase, not R86 COMPOSE's NM*/P*.

## 6. DATA (NOT to sign) and pinned check
- core/gp.py STAR=1 (lists as box 30: alt_all pinned starts, lib41, experiments/si; outputs experiments/si/core/out/gpstar_*.txt): Lemma GP* 0
  violations on all 2,235 frozen W-phases tested (1,754 with D ≠ ∅ and every gate λ_Ξ(d) = λ_W(d), 481 with D = ∅); the FW-R* inequality never
  fails; R*_T = 0 in 1,499 of the 1,754 (FW-BF for each of them by FW-R*); largest R*_T 40 (red/usplit/instances/grow_K40_n373, n 373, WCH 45).
  Control that bites: MUT=all (every successor allowed, i.e. the plain W-frame Lemma P) fails on xing/instances/ccl_w48_n48 and on
  runlin/instances/runfam_K100.
- Pinned in experiments/si/check.sh «box 31 §6»: ccl_w48_n48 (sha1 a7056dea01cd9c6398e054ef6edaaa40f60dabb1; R* = 12 in R*_T = 1 transition,
  GP* PASS, MUT=all FAIL) and core/instances/rlin_cex_n40 (sha1 670ba1ffc22c8f9b170e11ca3e43c33cee9329ca, start sha1
  e488c00fe1359818b9a665a415cc7b2962015318; R* = 0, so FW-BF holds there by FW-R*; n5b identical). Quote check: «box 31 packet» block
  (rund/quotecheck.py PASS, --mut FAIL).
