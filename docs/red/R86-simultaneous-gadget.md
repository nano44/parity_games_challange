# R86: the "simultaneous" gadget (σ̄-alternation forcing τ-alternation): an exact obstruction, polynomial on 𝒞^kO for fixed k, and a linear construction with Θ(n) phases (L-RED successor 20, box 53; Lead 11:27Z, date -u)
Target: the Lead's (c): a gadget where σ̄-alternation forces τ-alternation across phases, so that W alternates too, "Report the exponent,
or the exact obstruction", and "Check whether your gadget needs ≥ 2 Odd choice vertices per class, and say why". Labels per L40:
PROVED (lane, unrefereed; short derivations from landed results), DATA, READING. Not a TARGET.md claim. G-N5-TIME stays open.

## 0. Result
- **Obstruction 1 (PROVED from RESULTS R15 (c), (d)):** in any N5 run, the number of τ changes is at most the number of Odd positional
  strategies, Π_{q ∈ Q} deg(q) ≤ Δ^k, where k = |Q| is the number of Odd choice vertices.
  - Proof. R15 (c), (d): every N5 iteration that changes τ applies a non-empty switch of improvements to τ on G^d. Such a switch goes
    strictly up in the strict partial order ≺_{G^d}, so no τ repeats in a run. □
  - Consequence: on 𝒞^kO with k fixed, a τ-driven counter has polynomially many τ changes (≤ n^k). The phases it can cut are at most
    (τ changes + 1) × (λ-changes per constant τ).
  - So the Lead's "many PHASES" form of a counter needs k·log Δ = ω(log n): the number of Odd choice vertices must grow with n. No
    fixed-k family can do it through τ.
- **Obstruction 2 (PROVED, every game): alternation of τ at one Odd vertex q needs another Odd choice vertex that q can reach.**
  - Statement: suppose no play from a successor of q, under any pair of strategies, meets an Odd choice vertex other than q. Then τ(q)
    changes at most deg(q) − 1 times in a run.
  - Proof. Odd's honest value of each option y of q is computed on the subgame reachable from y. It contains no Odd choice vertex
    other than q, so it is a function of τ(q) alone (Even's best response there depends only on τ(q)). By R15 (c) applied on G^d to
    this subgame's strategy (τ(q) alone), τ(q) never returns to a value it left. □
  - This is the τ-side analogue of R47 (a) (τ changes ≤ d_o − 1 on 𝒞^1O).
  - So yes: a τ-alternating gadget needs ≥ 2 Odd choice vertices, and they must be in each other's reach. That is the dual-frame
    version of "≥ 2 Odd choice vertices per class". The class here is taken in G^d's honest frame (Even's best response to τ), not in
    σ's λ-classes.
- **The symmetric half (READING, from R15 (d)):** Iσ depends on σ alone and Iτ on τ alone. So σ̄'s alternation (a function of σ) can
  influence τ's moves only through S4b's W-optimal CHOICE among Iτ-edges. It can never make a τ-edge available. A "simultaneous"
  counter therefore needs Odd's own honest valuation (against Even's best response to τ) to keep improving, and that pays content per
  change by the mirror of RULER, exactly as on Even's side (R82, R83).
- **DATA (linear construction):** N5 on the DUAL of mkpp (n5.dual: owners swapped, priorities + 1, same start vector; dualrun.py). By
  Lemma DUAL (P-N5-DUAL) this is the mirror of N5^OF on mkpp; mkpp has no fallbacks, so the dynamics are mkpp's own. Every iteration
  changes τ, so every iteration is a new phase:

| K | n | iterations | τ changes | phases | fallbacks | Odd choice vertices | OUT / Oink |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 6 | 113 | 13 | 13 | 14 | 0 | — | OK / OK |
| 12 | 161 | 19 | 19 | 20 | 0 | — | OK / OK |
| 24 | 257 | 31 | 31 | 32 | 0 | — | OK / OK |
| 48 | 449 | 55 | 55 | 56 | 0 | 365 | OK / OK |

  - Phases grow linearly (exponent 1), with k ≈ 0.8 n Odd choice vertices, consistent with Obstruction 1.
  - Pins: pp_K12_n161_dual.pg (sha1 f967a43d2834ef6f73a2a821ab587f227114205f) and pp_K48_n449_dual.pg (sha1
    c764dd643eeb85798f5c66f858a512c4c43cee22), each with .start.json (the same start vectors as the primal pins).

## 1. What remains (READING)
- A super-polynomial N5 run needs one of:
  - super-polynomially many τ changes, which needs k = ω(1) Odd choice vertices (Obstruction 1);
  - super-polynomially long phases, which needs route (i), (ii) or (iii) of R83 §2.
- In both cases each "event" must be paid without fresh content: a ruler or binary-counter pattern in the scores of BOTH players. In
  [STV]'s words (arXiv 1501.06484 §4.1, R85): traps "need to trap them simultaneously". I have no gadget that does it.
- For the proof side, Obstruction 1 is a cheap but real handle. On 𝒞^kO, a phase-count bound reduces to bounding the λ-changes between
  consecutive τ changes (R47 (b) does this on 𝒞^1O).
