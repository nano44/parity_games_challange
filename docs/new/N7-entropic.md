# N7: entropic temperature homotopy (soft Bellman + Newton path following) on the parity-induced discounted game (L-NEW successor 5, Opus 5.5; box 12, second half)
Lead 08:02Z (date -u): next untested approach, screened first; park with the screen results if nothing survives by ~09:30Z.
Status: DEAD END (§4). Proof route dead at the screen (§2); on data the Newton path-follower stalls on the same 16-vertex instance that
killed N6 (counter_ortl N = 3) and its step counts grow fast where it converges (§3). All produced answers correct.

## 0. The approach and why it is not already covered
Binary discounted game from N6's pipeline (compressed priorities, weights (−B)^p scaled to max 1, γ = β_G). For temperature τ > 0 the soft
Bellman operator T_τ(v)_i = s_i·τ·log Σ_a exp(s_i(c_i + γ v_{succ_a(i)})/τ) (s_i = +1 for Even/max, −1 for Odd/min) is a γ-contraction in
the sup norm (log-sum-exp is 1-Lipschitz), so its fixed point v_τ is unique and smooth in τ; v_τ → the discounted values as τ → 0.
N7 follows τ ↦ v_τ from τ_0 = 4/(1−γ) down, by Newton on F(v) = v − T_τ(v) (Jacobian I − γP_π with π the soft policy, always invertible),
with adaptive τ-steps, and certifies the hard rounding (argmax/argmin of Q) with verify.py after every τ-step.
Not covered, because:
- Not strategy improvement (BARRIERS B8-B12): no switching rule over positional strategies; the iterates are values of SOFT (mixed)
  policies, and Newton on the soft operator is not a policy-iteration step until τ = 0.
- Not N3 (Blackwell path, discount homotopy: the path of optimal PURE pairs as γ varies, killed by one degenerate breakpoint) and not N1
  (discount schedules): γ is fixed at β_G; the homotopy parameter is the temperature and the path is a smooth curve of unique fixed points.
- Not N6: N6 follows the log-barrier central path of the LCP. The other standard smoothing of an LCP, Chen-Harker-Kanzow-Smale,
  φ_μ(a, b) = a + b − √((a − b)² + 4μ) = 0 ⟺ a, b > 0 and ab = μ (square both sides), IS the central path, so it is covered by N6. Entropic
  smoothing acts in value space and is a different curve.
- RANKING.md rows 4 and 7 and the dead-end record list no regularisation / smoothing method; no fleet lane ran one (grep "entrop",
  "soft" in docs/ and experiments/: N6 only).

## 1. Sources opened (2026-10-22; PDFs in the scratchpad)
- Cen, Cheng, Chen, Wei, Chi, "Fast global convergence of natural policy gradient methods with entropy regularization", arXiv 2007.06558
  v5, sha256 23fddbc3f493d02e: Theorem 1 (linear rate (1 − ητ)^t for any η ≤ (1−γ)/τ; MDPs).
- Cen, Wei, "Fast policy extragradient methods for competitive games with entropy regularization", arXiv 2105.15186 v3, sha256
  a2da0da3164be410: Theorem 3 (two-player zero-sum Markov games, total iterations O((log|A| + 1/τ)/(1−γ)² · log²(log|A|/((1−γ)ε)))).
- HMZ arXiv 1008.0530 Thm 6.5 and Friedmann arXiv 1106.0778 §9 (β_G), as opened for N6 (docs/new/N6-ipm.md §1).

## 2. Screen
- (a) Known analyses of entropy-regularised MDPs and games are polynomial in 1/(1−γ) and 1/τ (Cen et al. Thm 1: with η = (1−γ)/τ the
  rate is γ^t, i.e. O(1/(1−γ)·log) iterations; Cen-Wei Thm 3: O((log|A| + 1/τ)/(1−γ)²) up to logs). For parity both factors are
  exponential: 1/(1−γ) = 4n'^{d+3} (β_G), and recovering the exact positional optimum needs τ below the smallest action gap divided by
  log 2, a gap that can be 2^{−O(n d log n)} (the same separation as N6 §3).
- (b) The HMZ principle (N6 §2) applies verbatim: any analysis polynomial in 1/(1−γ) would make strategy iteration on the same discounted
  game polynomial already (HMZ Thm 6.5). So a polynomial N7 needs an analysis independent of γ: proof route DEAD AT THE SCREEN.
- (c) Heuristic for Newton path following (L-NEW reading, not a theorem): the Jacobian's inverse is bounded by 1/(1−γ) and its Lipschitz
  constant is ~γ/τ, so Newton's guaranteed radius is ~τ(1−γ); the path moves by up to ~τ·log 2/(1−γ) when τ halves. Guaranteed steps per
  halving ~1/(1−γ)²: the same Θ(1/(1−γ)²) as HIJ's κ for N6. Live question: whether actual damped-Newton counts follow (bench §3).
- (d) Bit costs: as N6 §3 (γ, costs O(d log n) bits; exp/log at O(bits) precision); polynomial per Newton step.
- BARRIERS: B8-B14 not applicable (no rule over pure strategies, no pivoting, no cube); B15 (IPM strong polynomiality) not applicable;
  B18 (Howard at one discount): N7's τ → 0 limit is Newton on the hard operator, which for one player IS Howard; N7 avoids Howard's
  fixed start only through the path. B19: weights paid at bit cost.

## 3. Bench (experiments/new/ipm/n7.py; bench.sh with SOLVER=n7; results/*.n7.csv; every produced solution checked by check_sol2.py)
See the CSVs for exact rows (Newton steps to a certified answer; "-" = no answer):
| family | N (n): Newton steps to a certified answer, or the failure | all produced answers vs Oink |
| --- | --- | --- |
| tc | 1 (8): 57; 2 (22): 193; 3 (42): 772; 4 (68): - (start-fail) | all correct |
| tc+ | 1 (8): 2; 2 (24): - (stalled) | all correct |
| counter_m | 1 (6): 16; 2 (9): 26; 4 (15): 65; 6 (21): 89; 8 (27): 113 | all correct |
| counter_rr | 1 (4): 1; 2 (8): 54; 4 (16): 401; 6 (24): 911; 8 (32): 3098 | all correct |
| counter_dp | 1 (8): 64; 2 (12): 154; 4 (20): 475; 6 (28): 1482 | all correct |
| counter_qpt | 2 (4): 1; 4 (8): 1; 8 (16): 1 | all correct |
| counter_core | 1 (9): 102; 2 (15): 634; 3 (21): 1567; 4 (27): 4779 | all correct |
| counter_ortl | 1 (6): 47; 2 (11): 603; 3 (16): - (stalled) | all correct |
| counter_symsi | 1 (12): - (start-fail); 2 (22): - (start-fail) | all correct |
| counter_rob | 1 (14): 449; 2 (31): - (start-fail) | all correct |
| recursiveladder | 1 (5): 1; 2 (10): 26; 3 (15): 3; 4 (20): 899 | all correct |
| switchallexp | 1 (21): 97 (start-fail, final rounding certified); 2 (35): 179 (start-fail, final rounding certified) | all correct |
| hij | 4 (4): 200 (start-fail, final rounding certified); 8 (8): 200 (start-fail, final rounding certified); 16 (16): 1 (start-fail, final rounding certified) | all correct |
'start-fail' = Newton at τ_0 did not reach |F| ≤ 10^−3·τ_0 in 200 steps (a start-phase weakness of this implementation, like N6's early
variants); 'stalled' = the τ-step factor reached 1 − 10^−12 mid-path (the N6 §6 mechanism).

## 4. Verdict: DEAD END
- Proof route dead at the screen (§2 (a)-(b): known rates poly(1/(1−γ), 1/τ), both exponential for parity; HMZ principle).
- On data: no answer on counter_ortl N = 3 (experiments/new/instances/n6/counter_ortl-3.pg, sha1 c8bc349942b32305edee56ba8fb7d6504ed86622;
  stalls at τ ≈ 2.8·10^−7 after 38 τ-steps and 3,213 Newton steps), i.e. the instance that kills N6 also kills N7, and tc+ N = 2 (stalled mid-path, 51 τ-steps); start-phase failures on tc N = 4, counter_symsi N = 1-2, counter_rob N = 2.
  Where it converges, step counts grow fast (counter_rr 1, 54, 401, 911, 3,098 at N = 1, 2, 4, 6, 8, i.e. n = 4..32, about n^3 at the top; counter_core 102, 634, 1,567, 4,779
  at N = 1-4); these curves alone are polynomial-looking and are NOT claimed as super-polynomial.
  No incorrect answer.
- Screening principle recorded for the lane (both N6 and N7): every method that works on the parity → discounted reduction and whose
  analysis is polynomial in 1/(1−γ) is no better than strategy iteration (HMZ Thm 6.5); such a candidate needs a γ-free argument before
  any bench.
- Scope of the kill (same framing as the Lead's N6 addendum): the generic method is killed by the SCREEN (§2); the bench failures are
  non-convergence of THIS implementation (stated parameters: τ_0 = 4/(1−γ), tolerance 10^−3·τ, adaptive τ-factor, Armijo on |F|_inf),
  with no incorrect answer. Whether some Newton/continuation scheme on the entropic path has a γ-free polynomial count is not claimed.
