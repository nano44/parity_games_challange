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

## G6-G11. REFEREE-2 20's notes N-GP-1..6 (report docs/referee-2/R2-N5-GP.md, referee-2 4835eb3d; SIGNED all, no gap). Appended at the Lead's 17:17Z request
- G6 (N-GP-1, quote form): agreed; the elision in [CASE-A] is faithful. The elided text is A1's closing parenthetical, in full
  (docs/new/N5-phase-bound-box10.md lines 34-35 at 2a435f8f4): «(If the cycle node c of Ω_k(ρ_k(x)) differs from u, then value(r') ⪯ Ω_k(ρ_k(x))
  forces c better than u, and the prefixed values are ordered the same way.)» GP*'s Case A uses it in the same way, through [V2]'s «(or whose
  cycle nodes differ)».
- G7 (N-GP-2, standing premises): agreed; this complements G1 (GP-N1) and does not repeat it. W-MON reads S4a's σ_new (S1 on the dual of H_t)
  as Even's pointwise optimum of H_t. This needs the exact order reversal between G^d and G and the SPEC-conformance premise (R57 (b)); together
  these are G1's [OPT-H]. XW's first part is R57 (a)'s (VJ) premise: σ̄ minimises S1's order at every vertex at once (G1's [OPT-σ̄], optimality
  half).
- G8 (N-GP-3): agreed; see G5 (GP-N5). B1′ (i) covers both parities of c in one formula because [V2] needs no parity. This is the one place
  where GP*'s Case B is strictly more general than R17's (R17 had P(π) = ∅ only with c odd, forced by improvement).
- G9 (N-GP-4, cycle shape in B1′): agreed. Z = x, π, then the arc of c's ρ_k-cycle from c back to x, is a simple cycle. Since x ∉ π, π's
  part on c's cycle (from the vertex where π enters it, up to c) does not contain x. Going around the cycle from c, x therefore comes before
  that entry vertex, so the arc c → x and π meet only at c.
- G10 (N-GP-5, §3a wording): agreed. In the §0 table, «each also follows from §3's Case A / Case B directly» means: run §3's induction with
  «timely (timely⁺) at state k», i.e. «r_{i+1} ∈ ALLOWED(⁺)(r_i, k − 1 − i)», in place of «unblocked at state k». The non-blocked cases of
  §3a alone do not conclude without that induction. §3a's proof (reduction to GP*) is the one to sign.
- G11 (N-GP-6, R*_T): agreed; G0 already uses R*_T. R_T (FW-R′ of docs/si/N5-SPC-box31.md §4, adoptions of edges not in ALLOWED⁺) satisfies
  R_T ≥ R*_T, because every blocked edge is outside ALLOWED⁺ (§3a). So a line stated with R_T would be implied by FW-R*, but weaker.

## G12. REFEREE-2 20's N-GP-7 (report docs/referee-2/R2-N5-GP.md at referee-2 894a1971, §2.6 and §4): the FINAL RESULTS line, verbatim; supersedes G0's line
Lead 2026-10-29 17:23Z (brief to successor 28): «G12 records the FINAL RESULTS line verbatim, superseding G0's line.» Final line:
"In every frozen W-phase F = [a, b] of N5 on any game (N5-FRZ-box29 §0: no S4c fallback; τ, σ̄, λ_Ξ, λ_W constant; W = val(σ, τ)), (Lemma GP*) for every k ∈ [a, b], W_k(x) ⊵ value(r) for every simple path r of G_τ (Odd steps follow τ) with at most k − a edges from x to a W-cycle node u of F's first state a (λ_W(u) = u), none of whose Even edges (r_i, r_{i+1}) was BLOCKED at state k−1−i (W-better than σ's choice at r_i but not a VJ00-improving edge of Ξ); (Corollary FW-R*) F has at most (n−1)(R*_T+1) W-changing transitions, R*_T := the transitions of F at which some Even vertex adopts an edge blocked at an earlier state of F; so R*_T = 0 ⇒ ≤ n−1 — a REDUCTION (R*_T is not bounded here; FW-BF, G-N5-TIME open; per frozen W-phase only, not a bound on the run)."
- N-GP-7 agreed. (a) «at most k − a edges» was already restored in G0 (GP-E1); the referee's instances b4_theta_n7.pg (x = 1, z = 6), canonA_0.pg
  (x = 3, z = 4), b5_os_n28.pg (x = 1, z = 7), from docs/referee-2/R2-N5-GP/line_probe.py, are one-edge paths at k = a and are excluded by it
  (at k = a only L = 0 is allowed). (b) G0 said «a cycle node of F's first state»; the final line says «a W-cycle node u … (λ_W(u) = u)». This
  matters: λ_Ξ and λ_W are both constant on F but differ when D ≠ ∅, and GP* (base case W_a(u) = (u, ∅, 0)) needs u to be W's cycle node.
- Word-by-word check against the packet's §3 (docs/si/P-N5-GP-box31.md lines 85-89, sha1 cd4866df) and §1 [FRZ] (line 67):
  | packet §3 / §1 | final line | match |
  | --- | --- | --- |
  | F = [a, b] a frozen W-phase; k ∈ [a, b] | «frozen W-phase F = [a, b]», «for every k ∈ [a, b]» | yes |
  | path of G_τ (Odd r_i: r_{i+1} = τ(r_i)) | «path r of G_τ (Odd steps follow τ)» | yes |
  | simple | «simple» | yes |
  | u a cycle node of state a (λ_W(u) = u) | «a W-cycle node u of F's first state a (λ_W(u) = u)» | yes |
  | L ≤ k − a | «with at most k − a edges» | yes |
  | for every i < L with r_i Even, (r_i, r_{i+1}) not blocked at state k − 1 − i | «none of whose Even edges (r_i, r_{i+1}) was BLOCKED at state k−1−i» | yes, reading «Even edge» as «edge whose tail r_i is Even» (the packet's «with x Even» in BLOCKED) |
  | BLOCKED at t ∈ [a, b): W_t(z) ▷ W_t(ρ_t(x)) and (x, z) ∉ Iσ_t; ρ_t := σ_t (§1 [FRZ]); Iσ_t = [S2]'s improving edges of Ξ_{σ_t} | «W-better than σ's choice at r_i but not a VJ00-improving edge of Ξ» | yes (strict; W, σ, Ξ read at that state t = k − 1 − i; t ∈ [a, k − 1] ⊆ [a, b) because i < L ≤ k − a) |
  | Lemma GP*: W_k(r_0) ⊵ value(r), value(r) := (u, P(r), L) [VAL] | «W_k(x) ⊵ value(r)», x = r_0 | yes (value(r) is the packet's [VAL]; the line does not restate it) |
  | §4 FW-R*: WCH ≤ (n − 1)(R*_T + 1), R*_T as defined | as G0, unchanged; REFEREE-2 §2.6: «matches §4» | yes |
  Nothing else differs. Two readings the line leaves implicit, both forced by the packet: «Even edges» = edges with an Even tail, and the
  state at which W, σ and Ξ are read in the parenthetical is the state k − 1 − i named just before it.
- Packet unchanged (sha1 cd4866df re-measured at this commit). Label: the line is a wording of PROVED (lane) content, signed by REFEREE-2 20.

## DONE / FINDINGS / NEEDS
- DONE: G0-G5 above (REFEREE 18), G6-G11 (REFEREE-2 20), G12 (REFEREE-2 20's N-GP-7: final RESULTS line, word-by-word against §3).
  FINDINGS: GP-E1 is a RESULTS-line wording error (mine, approved at 16:26Z), not a packet error; GP-N1-N5 and N-GP-1..7 accepted, no change
  to any proof; the final line matches §3 word by word (G12 table). NEEDS: none from the owner.
