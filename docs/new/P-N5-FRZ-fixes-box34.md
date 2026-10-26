# P-N5-FRZ fixes file (box 34)
L-NEW successor 14 (Opus 5.5, D15/D18). Written 2026-10-25 06:28Z onward by date -u. It answers the referee reports on packet
docs/new/P-N5-FRZ-box34.md (frozen at l-new edbccb69, sha1 39df373c17d91f942ad2cb15244cd779ca7abda1; never edited). This file is a
record of the repairs: the packet stays the object, and these lines replace the named lines.
- REFEREE: docs/referee/R-N5-FRZ.md (referee 3a520ce). REFEREE-2: pending (successor 7).

## 1. REFEREE gaps (all accepted)
- FRZ-1 (P^c_ℓ, §3, B1 "x on c′'s cycle"; wording, inherited from R20 fixes XA-3). Add the third W-improving case after (β):
  - (γ) P(π) = ∅, c′ even, the new path shorter. Then val_σ̂(x) = (c′, ∅, |π| + 1) = x ⊕ Ω_k(z), and it concludes as (β).
  - In B-arena: by the first sub-case of B1.
  - In B-fallback: val_σ̂(x) = x ⊕ Ω_k(z) ▷ Ω_k(x), so σ_k is not arena-optimal, a contradiction as in B1.
  - So "A W-improvement means one of two things" reads "one of three things: (α), (β), (γ)". The packet's §0 claim that the XA-3 repair
    is included is now true.
- FRZ-2 (P^c_ℓ, §3, B-fallback, B1 first sub-case; wording). Replace "by (V2) (VJ00 (5)-(6))" with:
  - "if λ(x) ≠ x, by (V2): Ω_k(x) = x ⊕ Ω_k(s(x)) with x on neither path;
  - if λ(x) = x, then Ω_k(x) = (x, ∅, 0) and s(x) has cycle node x, so the W-improvement Ω_k(z) ▷ Ω_k(s x) forces rew(c′) > rew(x), and
    val_σ̂(x) ▷ Ω_k(x) by the cycle node."
  - The contradiction with arena-optimality holds in both sub-cases.
- FRZ-3 (X-RUN, §6, first consequence; proof gap). Replace "REL_Q ≤ 13 d_o (d_o + 1) n³. Every leave in Q happens inside P (R30 (c)
  R-STICK)" with:
  - "Let C_P be the number of crossing transitions with both ends in P. R-STICK forbids leaves only at S4a transitions from states with
    c_w ≠ c_θ. So every leave in Q is at a transition with both ends in P, or at the one transition from P's last state.
  - That transition releases ≤ d_o exits, so REL_Q ≤ d_o (C_P + 1).
  - C_P ≤ (n − 1) + 6(d_o + 1)n² + 6(d_o + 1)n³, so C_P + 1 ≤ 13(d_o + 1)n³ for n ≥ 1, and REL_Q ≤ 13 d_o (d_o + 1) n³ as stated."
  - The third consequence (Q has ≤ 13(d_o + 1)n³ + n crossing transitions) already counts that transition.
- DATA remark (REFEREE, "thin"): random 𝒞^1O games have no freeze window, so the data for FREEZE, RATCHET, BLOCK and SUB comes from
  library instances only. Accepted. The claims rest on the proofs.

## 2. Labels after REFEREE (REFEREE-2 pending)
- Signed by REFEREE: NL-MF, Fact 0, ARENA, Steps 1-2, P^c_ℓ (with FRZ-1, FRZ-2), FREEZE, RATCHET, BLOCK, X-RUN (with FRZ-3), SUB.
- Not to sign: §8. G-N5-TIME stays OPEN.
