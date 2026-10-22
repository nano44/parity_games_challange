# T24: Hansen & Ibsen-Jensen (arXiv 1304.1888) as a barrier row (L-LIT, 2026-10-22)

Asked by the Lead at 08:02Z. Prompted by L-NEW's N6 screen (docs/new/N6-ipm.md §1–§5, claude/l-new), which found the row missing from BARRIERS.md. Added there as **B21** (BARRIERS.md is in docs/lit/, an L-LIT file).

**Source opened by L-LIT.** T. D. Hansen, R. Ibsen-Jensen, "The complexity of interior point methods for solving discounted turn-based stochastic games", arXiv 1304.1888 v2 (17 Dec 2014; CiE 2013).
- sha256 01e4cde9b47f90cb9fc22072d0df68e1cf4a8bfd125b971f25690cf89952e6aa (matches L-NEW's prefix).
- p. = PDF page. Page 3 was rendered and read as an image to fix the formulas.

## (1) Check of the statements L-NEW cites
| L-NEW's citation | opened text | check |
| --- | --- | --- |
| §2.3: JS reduction, Definition 16, Theorem 18 | Def. 16 (p.9): M_{G,σ,τ}, q_{G,σ,τ}. Theorem 18 (p.10): "Then the optimal value vector for G is v* = (I − γPτ)^{-1}(cτ + Iz), where (w, z) is a solution to the LCP (M_{G,σ,τ}, q_{G,σ,τ}). Furthermore, M_{G,σ,τ} is a P-matrix." | **correct**. M involves P, I, γ only; the costs enter q only (Def. 16) |
| Theorem 19: κ = n/(1−γ)² | Theorem 19 (p.11): "Let G be a 2TBSG with n states and discount factor γ, where 0 < γ < 1. … Then the matrix M_{G,σ,τ} is a P*(κ)-matrix for κ = n/(1−γ)²." | **correct** |
| Theorem 21: lower bound on G_n | Theorem 21 (p.13): "The matrix M_{Gn,σn,τn} is not a P*(κ)-matrix for κ < γ²(n−2)/(8(1−γ)²) − 1/4 = Ω(γ²n/(1−γ)²)." G_n (p.12): "n states that all belong to Player 2. Every state has two actions, and all actions are deterministic. The actions from states 1 and 2 form self-loops. The actions from state i, for i > 2, lead to state 1 and 2, respectively." | **correct**. Note the Ω has γ² in it, so it is Θ(n/(1−γ)²) for γ bounded away from 0, which covers the γ → 1 regime that matters |
| KMNY consequence | §1.1 (p.3): "Item (i) implies that the running time of the unified interior point method of Kojima et al. [12] for 2TBSGs is at most O((1 + κ)n^3.5 L) = O(n^4.5 L/(1−γ)²)." The intro (p.3) restates the KMNY method: P*(κ) LCP "in time O((1+κ)n^3.5 L)" | **correct** |
| Theorems 22–25 (Kojima-Megiddo-Ye potential reduction) | abstract: "in the worst case κ = Θ(n/(1−γ)²), −δ = Θ(√n/(1−γ)), and 1/θ = Θ(n/(1−γ)²)". §1.1: "O((−δ/θ) n^4 log ε^{-1}) = O(n^5.5 log ε^{-1}/(1−γ)³)". Theorem 24 (p.18): θ(M) ≥ (1−γ)²/((1+γ)²n). Theorems 23 and 25 (p.16, p.19) are the matching lower bounds on G_n | **correct**. L-NEW's −δ/θ = Θ(n^1.5/(1−γ)³) is the product of the two Θ's |
| §1.1 open question | p.3–4: "Note that the upper bounds we prove for the two algorithms are worse than the O((n²L/(1−γ)) log(1/(1−γ))) bound for the value iteration algorithm for the case where every state has two actions. Although our results for existing interior point methods for solving 2TBSGs are therefore negative, other interior point methods may solve 2TBSGs efficiently. It is also possible that the known bounds for the algorithms studied in this paper do not reflect their true running time. In fact, we believe that interior point methods are the key to solving 2TBSGs efficiently, and that the study of interior point methods in this context remains an important question for future research." | **correct**. The value-iteration bound read from the rendered p.3 is O((n²L/(1−γ)) log(1/(1−γ))), matching L-NEW |

## (2) The barrier row (B21) and what it rules out
**Statement.**
- For the Jurdziński-Savani P-matrix LCP (M, q) of a discounted 2TBSG with n states, the parameters satisfy, in the worst case:
  - κ = Θ(n/(1−γ)²) (Thm 19 upper; Thm 21 lower, on the one-player deterministic arena G_n);
  - −δ = Θ(√n/(1−γ)) (Thm 22, 23);
  - 1/θ = Θ(n/(1−γ)²) (Thm 24, 25).
- So the parameter-based running-time bounds are O(n^4.5 L/(1−γ)²) for the unified IPM of Kojima-Megiddo-Noma-Yoshise, and O(n^5.5 log ε^{-1}/(1−γ)³) for the potential reduction of Kojima-Megiddo-Ye. These are polynomial iff 1/(1−γ) is.

**What it rules out for parity games (L-LIT reading, from opened sources).**
- Parity → mean payoff → discounted (Friedmann 1106.0778 §9, p.35: r = (−|V|)^Ω and β_G = 1 − 1/(4|V|³·max|r(v)|); Thm 9.3 [ZP96]: optimal strategies at β_G are optimal for the mean-payoff and parity game). This needs 1/(1−γ) = 4n³·n^d = n^Θ(d).
- At that γ, Thm 21 gives κ = Ω(n·n^(2d+6)) on G_n-shaped arenas. Since M does not depend on the costs (Def. 16), the bound holds whatever priorities the arena carries.
- **Hence every κ-, δ- or θ-based running-time bound for these IPMs on the JS LCP of a parity game is n^Θ(d)**: polynomial only for d = O(1), and quasi-polynomial for d = O(log n).
- It does NOT rule out an IPM that solves these LCPs in polynomial time by an analysis independent of κ, δ and θ. HIJ themselves leave that open (§1.1 quote above).
- Fine print:
  - G_n is one-player and trivial as a parity game. The row is a worst-case statement about the parameter, not a hard parity instance.
  - A smaller γ than β_G might suffice for a particular game, but no opened source gives a polynomial 1/(1−γ) that works for all parity games. Friedmann §9 and Zwick-Paterson give n^Θ(d).

**Link to HMZ (1008.0530 v1, Thm 6.5).**
- HMZ: strategy iteration (switch-all against an optimal counter-strategy) terminates within (m+1)(1 + log_{1/γ}(n²/(1−γ))) = O((m/(1−γ)) log(n/(1−γ))) iterations from any start. This is polynomial whenever 1/(1−γ) is.
- So whenever B21's κ-based IPM bound is polynomial, HMZ already gives a polynomial bound for strategy iteration on the same game (L-NEW's observation, L-LIT agrees as a reading).
- The κ route can never beat what strategy iteration's discount-dependent bound gives.
- Both are n^Θ(d) on parity games at β_G. This is the same n^O(d) class as N1's ceiling (T18 §1, T19).

**Relation to other rows.**
- B15 (ABGJ 1708.01544, AGV 2201.02186): "no log-barrier / self-concordant IPM is strongly polynomial" for LPs. B21 is the game/LCP-side statement: polynomial in 1/(1−γ), and the dependence is tight for these parameters.
- B13 (Lemke, Cottle-Dantzig on the same JS LCPs, 0909.5653 Thm 18–19): pivoting, a different method on the same LCPs.

## DONE / FINDINGS / NEEDS
- FINDINGS:
  - Every HIJ statement L-NEW cites checks out (Def. 16, Thm 18, 19, 21, 22–25, §1.1 open question; sha256 matches).
  - B21 added to BARRIERS.md: κ, δ and θ for JS LCPs of discounted games are tight polynomials in 1/(1−γ), so κ-based IPM bounds for parity via discounting are n^Θ(d).
  - B21 is never better than HMZ Thm 6.5 for strategy iteration. An IPM analysis independent of κ remains open (HIJ §1.1).
- NEEDS: none (owner: nothing).
