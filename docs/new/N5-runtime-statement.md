# What a running-time proof for N5 would have to show (L-NEW successor 2, 2026-10-18 23:34Z by date -u; for the owner's reassessment, Q16)
L-NEW's honest statement, not a claim (D1). What is known:
- The (Ω, φ) theorem (G-N5-TERM-reading.md; two referee signatures at 812ecba) shows that N5 terminates. Each iteration strictly
  raises Even's potential (Ωσ, φ) or Odd's (Ωτ, φ^d), and neither ever drops. So the iteration count is at most the sum of the
  HEIGHTS of the two orders.
- Those heights are the lengths of VJ00 improvement chains. They can be exponential: Friedmann's families realise exponential
  chains for switch-all and for switch-best.
- So a polynomial bound needs a DIFFERENT potential, one of polynomial height that N5's specific step (Even's optimum over its
  improving edges against Odd's CURRENT strategy, and symmetrically for Odd) raises every poly(n) iterations.
- The natural shape is an elimination argument, as in Hansen-Miltersen-Zwick's discounted bound (arXiv 1008.0530, Lemma 6.4): every
  p(n) iterations some edge becomes permanently non-improving (or some vertex's cycle node becomes final), giving ≤ m · p(n)
  iterations. VJ valuations are order-based and have no contraction factor, so HMZ's mechanism does not transfer, and the lane has
  no candidate for p(n).
- What the obstructions K1-K8 contribute:
  - They say what any super-polynomial family must look like: mutual blunders frozen through a counter (K1-K5); a local stall at
    every DLM-distracted vertex (K6); Odd's lagged step tracking every change of the arena reply (K7). Through the coincidence lemma, that
    means constant or 2-periodic Odd replies (K8; sufficient condition, matched by the data).
  - They also say that N5 coincides with switch-best whenever τ is Odd's arena-optimal reply (proved). So a proof must use the lag
    between the two players: on Friedmann's switch-best family, the lag is exactly what makes N5 leave the exponential path.
  - None of K1-K8 is a bound. Each is a necessary condition that the lane's attacks failed to meet.
Summary: termination is proved. A polynomial running-time proof would need a polynomial-height potential that the τ-steered step
raises every poly(n) iterations. None is in sight. The evidence for polynomial behaviour is data only (every bench family and every
adversarial search so far is linear or near-linear in n).
