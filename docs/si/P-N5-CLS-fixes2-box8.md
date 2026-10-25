# Fixes to packet P-N5-CLS, part 2: REFEREE's §C (packet docs/si/P-N5-CLS-box8.md, sha1 5bbfd872; never edited)
L-SI successor 3 (Opus 5.5, D18/L40). Written 2026-10-25 03:1xZ (date -u).
- Part 1: docs/si/P-N5-CLS-fixes-box8.md, sha1 92f79dc9, l-si 2c5e57ce. It holds rows 1-5 (CLS-1, CLS-2, CLS-3 = G-CLS-1, CLS-4,
  N-CLS-1). Its sha1 was already sent, so it is not edited; this file completes it.
- Source: REFEREE docs/referee/R-N5-CLS.md §C (8af6347), as relayed by the Lead at 03:08Z. No verdict differs from REFEREE-2's §C.

## The six rows (the joint map)
| # | row | where | fix |
| --- | --- | --- | --- |
| 1 | CLS-1 | §3 (and §5) | part 1: M_k ≥ −1 at every in-phase transition (no gate ⇒ σ unchanged ⇒ τ changes ⇒ the phase is left) |
| 2 | CLS-2 | §4 CN | part 1: "an Even y with λ_k(y) = y" |
| 3 | CLS-3 = G-CLS-1 | §6 CLS1 (and §0) | part 1: FBL (R20 (b)) in its u* ≠ none strong gate form at the single state k1 (no F → R, no R → R gate edge); replaces "a single fallback state … is a throttled stretch of length 1". REFEREE adopts this form. |
| 4 | CLS-4 | §6 Corollary | part 1: drop "evicting" |
| 5 | N-CLS-1 | §3 OFFGATE | part 1, with REFEREE's citation: R̄ is as in R25's OFF (P-N5-FB l. 48-49: on 𝒞^1O, (σ, τ)-reachability of o = honest reachability of o) |
| 6 | N-CLS-2 | §6 (β) | NEW, wording: under (h), θ = w ⟺ EQ (Lemma G: Ξ = π ⊕ θ and W = π ⊕ w on R, Ξ = W off R̄). So every in-scope fallback is THR or EQ, and case (β) ("EQ or u* = none") covers all in-scope fallbacks that are not THR with u* ≠ none. |

## Status
- No statement of the packet changes. All six rows are wording or explicit dependencies.
- The packet is signed by both referees.
