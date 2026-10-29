# P-N5-GP fixes (box 31): answers to REFEREE 18's report R-N5-GP (referee 7dffab64); the packet docs/si/P-N5-GP-box31.md stays frozen (l-si d072bb28, sha1 cd4866df18b55f44b3ef3d52de65943eeffe9140)
L-SI successor 27 (Opus 5.5; D18, Lead reading L40). Lead 2026-10-29 17:10Z: «Please create docs/si/P-N5-GP-fixes-box31.md (appended items
only; the packet stays frozen): G0: record the corrected RESULTS line verbatim. G1..G5: answer GP-N1..N5.» Appended items only; later
answers (REFEREE-2, §Cs) go below as new items. Labels (D18 / L40): PROVED (lane) / DATA / READING.

## G0. The corrected RESULTS line (GP-E1; Lead 17:10Z, superseding the 16:26Z line), verbatim
"In every frozen W-phase F of N5 on any game (N5-FRZ-box29 §0: no S4c fallback; τ, σ̄, λ_Ξ, λ_W constant; W = val(σ, τ)), (Lemma GP*) W_k(x) ⊵ value(r) for every simple path r of G_τ (Odd steps follow τ) with at most k − a edges from x to a cycle node of F's first state, none of whose Even edges (r_i, r_{i+1}) was BLOCKED at state k−1−i (W-better than σ's choice at r_i but not a VJ00-improving edge of Ξ); (Corollary FW-R*) F has at most (n−1)(R*_T+1) W-changing transitions, R*_T := the transitions of F at which some Even vertex adopts an edge blocked at an earlier state of F; so R*_T = 0 ⇒ ≤ n−1 — a REDUCTION (R*_T is not bounded here; FW-BF, G-N5-TIME open; per frozen W-phase only, not a bound on the run)."
Here a is F's first state. The packet's §3 definition of «unblocked at state k» already contains both hypotheses («r … of G_τ (Odd r_i:
r_{i+1} = τ(r_i))», «L ≤ k − a»); the 16:26Z line, my wording, dropped them. Agreed with REFEREE 18's two instances: without L ≤ k − a the clause
fails at k = a (no step has been made; rand0, path [0, 1, 7]), and without «Odd steps follow τ» a path may use an Odd edge W never follows
(rand8, path [2, 4]).

## G1. GP-N1 (standing premises): agreed; named here as premises of §1
- [OPT-H] For W-MON: the S1 procedure applied in S4a returns an optimal strategy of the one-player arena H_t (Even's one-player optimum
  against τ, pointwise), as used and signed in RESULTS R17 (e) for N5's step. W-MON applies [F1] to that optimum.
- [OPT-σ̄] For XW and GP+: σ̄_t is an optimal counterstrategy at every vertex at once and realises Ξ_t as the values of the (σ_t, σ̄_t)-plays
  (RESULTS R57 (b)'s standing premise: «that S1's procedure realises an optimal σ̄ is VJ00 §6 plus SPEC conformance»). XW's first part uses
  optimality (Ξ_t ⊴ W_t), its second part and GP+'s prefix form use «Ξ_t = the play values of (σ_t, σ̄_t)».
- GP* itself uses [OPT-H] through W-MON and [F1]; it does not use [OPT-σ̄] (blocked edges are defined through Iσ_t, whatever Ξ_t is).

## G2. GP-N2 (scope of GP*): agreed
GP*'s proof uses only: τ constant, no S4c transition, and λ_W constant on [a, k]. λ_Ξ and σ̄ constant are not used. So GP* (and FW-R*, whose
proof uses GP*, W-MON and λ_W constant) hold on every maximal run of in-phase states with those three properties (a stretch that may contain
σ̄-changes); D, U_t and S_{d,t} enter only GP and GP+, through Lemma XW at the state used. Statement unchanged in the packet; this is a
READING of its proof, PROVED (lane) by the same text.

## G3. GP-N3 (notation): agreed
In §4 (definition of a late adoption and the proof of FW-R*) read the transition index τ as s throughout: «a transition s → s + 1 of F
(a ≤ s < b) at which some Even y switches, ρ_{s+1}(y) = z ≠ ρ_s(y), …», «y_i adopts (y_i, y_{i+1}) at some transition s → s + 1 with t < s ≤ k»,
«k − s ≤ k − t − 1 = i ≤ n − 2. Charge k to s. A transition s is charged only by k ∈ [s, s + n − 2]». τ then denotes only Odd's strategy.

## G4. GP-N4 (data scope): agreed, and sharper
core/gp.py does not enumerate paths: it runs a path-tracking Bellman-Ford that keeps ONE best unblocked simple path per vertex and length
bound (x not on the stored path of its successor). Every value it compares against is the value of a real unblocked path, so a violation
would be genuine, but the GP* data (packet §6, «0 violations on 2,235 frozen W-phases») cover only these stored paths, not all unblocked
paths. FW-R*'s data (WCH, R*_T, the RED check) are complete counts. The packet's §6 wording «GP* 0 violations» should be read with this scope.

## G5. GP-N5 (B1′ (i)): agreed
B1′ (i) (P(π) = ∅) is stated for c of either parity, where R17's Case B had it only for c odd (improvement forced it there). It is correct
for both parities: x and the arc vertices of c's cycle are less relevant than c (c is the top of that cycle), and P(π) = ∅ says no vertex of
π is more relevant than c, so top(Z) = c whatever c's parity, and val_ρ̂(x) = (c, ∅, |π| + 1) = x ⊕ W_k(z).

## DONE / FINDINGS / NEEDS
- DONE: G0-G5 above. FINDINGS: GP-E1 is a RESULTS-line wording error (mine, approved at 16:26Z), not a packet error; GP-N1-N5 accepted, no
  change to any proof. NEEDS: none from the owner.
