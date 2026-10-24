# Justification note on RESULTS R19 (f) (Lead, 2026-10-24 18:28Z by date -u)
R19's landed text is frozen; this dated note adds a step and changes no statement.
- Statement concerned: RESULTS R19 (f) PIECE, signed "θ constant not needed (N-RE-4)" for the count of transitions at which Ξ or W changes.
- Gap (REFEREE R-N5-X X-1, docs/referee/R-N5-X.md §3.2, referee 53c0c68). N-RE-4's justification covers the GATES (Lemma G (c) at each
  state). The COUNT step (REFEREE R-N5-RE §5.2, "a value change on R is a change of (A_v, |π_v|)") assumes θ constant. A θ-change
  changes Ξ on all of R (Ξ = π ⊕ θ) with no route and no W-value on R changing.
- Missing step (REFEREE's closure, §3.2): inside a sub-block (τ, w, R constant, (h), one joint λ-phase), a transition that changes θ also
  changes W at a vertex of F.
  - Under H1, Odd's honest choice e_k = σ̄_k(o) lies in F, and θ_k = o ⊕ W_k(e_k).
  - If W is unchanged on F, then θ_{k+1} ⊴ o ⊕ W_{k+1}(e_k) = θ_k (Lemma S (a)), and θ_{k+1} ⊵ θ_k (R15 (a)).
  - So θ_{k+1} = θ_k.
  Hence every Ξ-or-W-changing transition changes an 𝓡*-value or an 𝓕-value, and the R19 (f) count stands with θ free.
- Status: R19 (f) as landed is TRUE (REFEREE, R-N5-X §3.2). This note is to be checked by REFEREE-2 (its §C on R-N5-X) and by CHECKER
  when the P-N5-X result is drafted. Until then it is "REFEREE-signed, REFEREE-2 pending".
