# Packet P-N5-VILB (box 44): every in-phase fallback of N5 is at least one round of value iteration on the min-max reachability game of each honest class (Lemma VI-LB, every game)
L-NEW successor 23 (Opus 5.5), D14 / D18, Lead reading L40; Lead's order 03:07Z (Lead's stamp): "packet it as its own small packet,
P-N5-VILB, frozen, self-contained … VI-LB is a lower bound, so state exactly what it does NOT give." Written 2026-10-26 03:05Z (date -u).
FROZEN at push: later text goes into a fixes file. Source: docs/new/N5-FBF-box44.md §7.1 (working doc; this packet governs).
Labels: PROVED (L-NEW 23, unrefereed) / READING / OPEN. Not a TARGET.md claim; nothing here bounds N5's running time on any class.
G-N5-TIME stays open.

## To sign, and what is not to sign
| § | statement | label |
| --- | --- | --- |
| §1 | facts (Aκ), (M1κ), (M2κ) and Lemma κ-FB-ROUND (restated with proofs; = P-N5-FBRED §1.1, R48's κ-FB-ROUND per class) | PROVED |
| §2 | Lemma VI-LB | PROVED |
| §3 | what VI-LB does NOT give | READING (not to sign) |
| §4 | the cross-field reading ([BGHM]) and the obstruction | READING / OPEN (not to sign) |
- Premises (landed): (V1) (R17 (a)); R15 (a) (Ξ_{k+1} ⊵ Ξ_k at every transition); SPEC S1 (valuation order), S2 (gates), S4c (FIX 3);
  KEY (R38 (a)). No (P), no class hypothesis, no (h_D), no hypothesis on τ or c_w.
- Cross-field source (opened; notebook "Sources opened", sha256 there): [BGHM] T. Brihaye, G. Geeraerts, A. Haddad, B. Monmege, "To
  Reach or not to Reach? Efficient Algorithms for Total-Payoff Games", arXiv:1407.5030v4: §3, Algorithm 1 and the operator F; Theorem 1
  item 4; the Figure 2(a) example. Used only in the READING §4; the lemma does not depend on it.

## 0. Setting (every game)
- N5 = SPEC S1-S5 of docs/new/N5-ssi-global.md. A PHASE: a maximal run of consecutive states with (λ, τ) constant, λ := λ_Ξ (the honest
  cycle-node map); by R38 (a) it is a joint λ-phase. An in-phase transition has both ends in the phase; it is an S4a step or an Even S4c
  fallback (an Odd fallback changes τ). g_1 < g_2 < … are the in-phase fallbacks (transitions g_j → g_j + 1); "t > g_0" means every state.
- Honest play: next_t(v) := σ_t(v) for Even v, σ̄_t(v) for Odd v (σ̄_t = S1's optimal Odd counterstrategy to σ_t); Ξ_t(v) is the value
  (c, P, ℓ) of v's honest play.
- For a cycle node c of the phase: U_c := λ^{-1}(c) (constant on the phase). wt_c(v) := sgn(v)·2^rank(v) if rank(v) > rank(c), else 0
  (sgn = +1 for even Ω, −1 for odd); s_c := +1 if Ω(c) is odd, −1 if even; κwt_c(v) := (wt_c(v), s_c); for z ∈ U_c, κ_t(z) := (signed
  weight of P(Ξ_t z), s_c·ℓ(Ξ_t z)); pairs are added componentwise and ordered lexicographically.
- The game Γ_c (per phase and c): vertices U_c; at an Even vertex the maximiser, at EVERY Odd vertex (choice or not) the minimiser,
  chooses a successor inside U_c; c is the target, with value (0, 0); a play pays the sum of κwt_c over its vertices before c, and
  −∞ if it never reaches c. Val^{≤0}_c(c) := (0, 0), Val^{≤0}_c(z) := −∞ (z ≠ c); for j ≥ 1:
  Val^{≤j}_c(c) := (0, 0); Val^{≤j}_c(z) := κwt_c(z) + max_{x ∈ succ(z) ∩ U_c} Val^{≤j−1}_c(x) for Even z ≠ c, and with min for Odd z ≠ c
  (max / min over an empty set: −∞ / +∞; −∞ + a = −∞). Val^{≤j}_c(z) is the j-step value: the best payoff Even can force from z while
  reaching c within j steps.

## 1. Facts and κ-FB-ROUND (PROVED; restated from P-N5-FBRED §1.1 / RESULTS R48 with c for c_θ)
- (Aκ) For z ∈ U_c ∖ {c} and every state t of the phase: next_t(z) ∈ U_c and κ_t(z) = κwt_c(z) + κ_t(next_t z).
  Proof. λ_t(z) = c ≠ z, so (V1) gives Ξ_t(z) = z ⊕ Ξ_t(next_t z), with the same cycle node c; so next_t(z) ∈ U_c. ⊕ adds z to P iff
  rank(z) > rank(c) and adds 1 to ℓ. z is not counted twice: if z ∈ P(Ξ_t next_t z), z lies on its own play's cycle, whose top is c, so
  rank(z) < rank(c) and wt_c(z) = 0. □
- (M1κ) For values x, x′ with cycle node c: x ⊴ x′ iff κ(x) ≤ κ(x′) (S1's order with equal cycle-node rewards).
- (M2κ) For z ∈ U_c and every in-phase transition t → t+1: κ_t(z) ≤ κ_{t+1}(z). Proof: R15 (a) and (M1κ), as λ_{t+1}(z) = λ_t(z) = c. □
- κ-FB-ROUND. At an in-phase fallback k → k+1, for every Even v ∈ U_c ∖ {c} and every successor x ∈ U_c of v:
  κ_{k+1}(v) ≥ κwt_c(v) + κ_k(x).
  Proof. If Ξ_k(x) ⊴ Ξ_k(σ_k v): κ_k(x) ≤ κ_k(σ_k v) ((M1κ); both in U_c), so κwt_c(v) + κ_k(x) ≤ κ_k(v) ≤ κ_{k+1}(v) ((Aκ), (M2κ)).
  Otherwise (v, x) is a gate edge (S2), so S4c sets σ_{k+1}(v) = x* with Ξ_k(x*) ⊵ Ξ_k(x) (best key). λ_{k+1}(v) = c ≠ v, so (Aκ) at
  k+1 gives x* ∈ U_c and κ_{k+1}(v) = κwt_c(v) + κ_{k+1}(x*) ≥ κwt_c(v) + κ_k(x*) ≥ κwt_c(v) + κ_k(x) ((M2κ), (M1κ)). □

## 2. Lemma VI-LB (PROVED, every game)
For every phase, every cycle node c of it, every j ≥ 0, every state t of the phase with t > g_j, and every z ∈ U_c:
κ_t(z) ≥ Val^{≤j}_c(z).
Proof. Induction on j. j = 0: Val^{≤0} is −∞ off c, and κ_t(c) = (0, 0) (c's own value is (c, ∅, 0)). Step j − 1 → j, at a state
t > g_j:
- z = c: both sides are (0, 0).
- Even z ≠ c: let k := g_j < t. For every successor x ∈ U_c, κ-FB-ROUND gives κ_{k+1}(z) ≥ κwt_c(z) + κ_k(x); the hypothesis at k (k >
  g_{j−1}) gives κ_k(x) ≥ Val^{≤j−1}_c(x); (M2κ) from k+1 to t gives κ_t(z) ≥ κ_{k+1}(z). Take the max over x.
- Odd z ≠ c: by (Aκ), κ_t(z) = κwt_c(z) + κ_t(σ̄_t z) with σ̄_t(z) ∈ succ(z) ∩ U_c, so κ_t(z) ≥ κwt_c(z) + min_{x ∈ succ(z) ∩ U_c} κ_t(x)
  ≥ κwt_c(z) + min_x Val^{≤j−1}_c(x) (hypothesis at t > g_{j−1}). ∎
- Relation to R48's κ-HAT-FREEZE (a) (READING): HAT-FREEZE (a) is the special case of the one-player relaxation in which the Odd choice
  vertices are deleted (only forced Odd vertices remain on the paths). VI-LB keeps them as minimisers, so it is the two-player form.

## 3. What VI-LB does NOT give (READING, not to sign)
- No upper bound: VI-LB does not say κ_t ≤ Val^{≤j}_c or κ_t ≤ Val_c (the limit). In Γ_c the minimiser may avoid c (payoff −∞ for Even);
  in G that play has a different cycle node, not a lower κ, so Lemma S (a) does not give κ_t ≤ Val_c. Without an upper bound there is
  no freeze, hence no FREEZE-EXIT and no count of fallbacks.
- No count: VI-LB bounds no number of fallbacks, S4a steps, crossings, Q-runs or phases. In particular it does not make f polynomial;
  the only count it implies is by contradiction with a ceiling (§4, last bullet), and that count can be exponential.
- No claim that N5 performs only one VI round per fallback, or that the S4a steps between fallbacks do no VI work: S4a steps also raise κ
  (by (M2κ)), and VI-LB simply ignores them. It is a LOWER bound on progress, not a description of N5.
- Walks vs simple paths: Val^{≤j}_c is a value over j-step walks (vertices may repeat); N5's honest values are values of simple paths.
- Classes only: VI-LB is per class U_c of the current phase; it says nothing across a λ- or τ-change.
- DATA: none specific. The regime where VI-LB could matter (many fallbacks in one phase) is not reached in any sample (the most in-phase
  fallbacks seen: 33 at n 48 on 𝒞^1O, 17 at n 32 and 21 at n 64 on the frontier; never ≥ n), so no data test it beyond the lane's
  checks of κ-FB-ROUND inside FB-POLY / FB-RED.

## 4. Cross-field reading and obstruction (READING / OPEN, not to sign)
- Integer form: ω(v) := (2n + 1)·wt_c(v) + s_c is order-preserving on sums of ≤ |U_c| terms (|Σ s_c| < 2n + 1). Negating (Even ↦ Min,
  every Odd vertex ↦ Max, κ ↦ −κ), Γ_c is a min-cost reachability (MCR) game of [BGHM] §3 with target c, and Val^{≤j}_c is, up to sign,
  the j-th iterate x_j of [BGHM]'s Algorithm 1 (operator F; x_i = Val^{≤i}). So VI-LB says: after j in-phase fallbacks, N5's honest
  values in U_c are at least the j-th value-iteration iterate of that game.
- [BGHM] Theorem 1 item 4 bounds value iteration by O(|V|²W) iterations (W the largest absolute weight); here W ≈ (2n + 1)·2^{rank range
  above c}, so this is exponential in n. The [BGHM] Figure 2(a) example needs 2W iterations.
- Obstruction shape (OPEN): mirror Figure 2(a) into U_c (an Even vertex and an Odd choice vertex on a 2-cycle with a low even-rank r, an
  exit through a high even-rank R). Val^{≤j}_c rises by about 2^r per two rounds, while N5's simple-path values stay below a ceiling of
  about 2^{R+1}; VI-LB then forces the phase to end before about 2^{R+1−r} fallbacks, which is exponential when R − r is large. Whether N5
  ever performs that many fallbacks in one phase, or escapes the gadget, is open (routed to L-RED by the Lead, 03:07Z).
