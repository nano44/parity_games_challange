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

## Rev. 18:42Z (Lead, by date -u): REFEREE-2 R2-N5-X §3.2 (referee-2 059f492), G-X-1
- REFEREE-2 finds the same gap independently, and sharper. If the R-part of R19 (f) is read as counting Ξ on R, the per-part bound
  "≤ |R| − 1 on R" is FALSE with θ free.
  - Instance: experiments/new/box28/instances/fbref_n48.pg (sha1 414231a2…), transition 56 → 57.
    - Same phase, (h) at both ends, no fallback, w = (27, ∅, 2) constant, R = {o} = {14}.
    - θ goes from (27, {28}, 9) to (27, {15, 28, 29}, 18).
    - Ξ changes at 14 ∈ R with budget 0, and also at F-vertices 3, 16 and 19.
  - Lead re-run, docs/referee-2/R2-N5-X/dump_tf.py at 059f492: exactly this output (same λ maps; Ξ changes [3, 14, 16, 19];
    W changes [3, 16, 19]; switched Even (3: 10→6), (16: 33→44)).
- Lemma TF (REFEREE-2, §3.2) is the same fact as REFEREE's X-1 closure: under (h) at both ends with R and τ constant, a θ-change is an
  F-value change.
- Lead reading (both referees agree on the substance): R19 (f) is TRUE when its R-part counts route changes (W on R, the route game
  against the frozen terminal w, which is what the 𝓡 / 𝓡* construction measures) and θ-changes are charged to the F-part (TF / X-1).
  Read with Ξ on R, the per-part split fails and only the total ≤ |R| − 1 + |F| − 1 holds.
- Clarified wording, to be carried as a clarification item in the RESULTS entry for P-N5-X (R19's landed text stays frozen):
  "θ constant not needed, provided the R-part counts route (W) changes on R; a θ-change under (h) at both ends is an F-change
  (Lemma TF = REFEREE X-1)."
- Status: REFEREE-2 proposed this wording; REFEREE's X-1 closure is the same argument. Both referees confirm the wording in their §C.
