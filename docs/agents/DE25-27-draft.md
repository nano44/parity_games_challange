# Draft RESULTS DE25-DE27 (Lead, 2026-10-22 08:25Z by date -u) — LANDED in RESULTS Dead ends (CHECKER C21 PASS, Addendum 1 30a0919 + stamp fix 4105c4a); was: awaits CHECKER C21 re-diff (rev. 08:45Z: C21 E-1..E-4, N-1..N-3, N-6)

- DE25 (2026-10-22): N6 = path-following interior-point method on the Jurdziński-Savani P-matrix LCP of the discounted game obtained
  from a parity game (L-NEW successor 5, (c) lane under D14/D15; docs/new/N6-ipm.md §1-§8, l-new c0e8b57 + addendum 8ace011) is a DEAD
  END. (a) Proof route dead at the screen (sources opened by L-NEW; HIJ re-opened by L-LIT T24, docs/lit/T24-HIJ-barrier.md, BARRIERS
  B21): Hansen & Ibsen-Jensen arXiv 1304.1888 Thm 19 / Thm 21, κ = Θ(n/(1−γ)²) for these LCPs (lower bound on the arena G_n, M
  independent of the costs); Friedmann arXiv 1106.0778 §9: at β_G, 1/(1−γ) = 4n^{d+3}, so every κ-based IPM bound at that discount is
  n^Θ(d) (L-LIT / L-NEW reading, T24 §2, BARRIERS B21; no opened source gives a polynomial 1/(1−γ) that works for all parity games);
  and, by HMZ arXiv 1008.0530 Thm 6.5 (reading, T24), whenever such a bound is polynomial, strategy iteration is already polynomial. ABGJ arXiv 1708.01544 Thm B
  (Cor. 31) does not transfer as stated (LPs, doubly exponential data). (b) Gauntlet step 2 fails on data for the implementation
  experiments/new/ipm/n6.py in its default central mode (target-following, adaptive long step, fraction-to-boundary Newton, precision 8×bits): no answer on 7 of
  13 hard families at small N (tc N=4, tc+ N=2, counter_ortl N=3, counter_symsi N=1, counter_rob N=2, counter_core N=4, counter_dp N=8)
  and on 6 of the 8 random games with n ≥ 23 (n = 25-30; n = 23, 24 answered correctly after a centring failure; 10 of 40
  random games without a solution; gen.py, seeds 20261023-62); the weighted mode fails on tc, tc+, counter_ortl, counter_symsi and
  counter_rob from N ≤ 3 (N6 §7); every produced answer correct (check_sol2.py against Oink zlk).
  Obstruction instance experiments/new/instances/n6/counter_ortl-3.pg (sha1 c8bc349942b32305edee56ba8fb7d6504ed86622, n = 16): M
  certified P (all 262,143 principal minors positive, arb); the path is lost at μ = 3.19e-26 under every setting tried (HIJ's κ scale n/(1−γ)² ≈ 1e43: a
  neighbourhood on the products w_i z_i no longer pins the coordinates). Lead re-run (2026-10-22 08:20Z, trunk, python-flint):
  "stalled/c141/mu36, 3.1911607757279757e-26", no solution, identical to results/counter_ortl.central.csv. The step-2 failure is
  non-convergence of this implementation, not an incorrect answer; the generic method is killed by (a). Open and not claimed: the
  iteration count of a convergent IPM on these LCPs (HIJ §1.1).
- DE26 (2026-10-22): N7 = entropic temperature homotopy (soft log-sum-exp Bellman operator on the parity-induced discounted game at
  γ = β_G, temperature τ → 0, Newton / soft policy iteration; docs/new/N7-entropic.md, l-new 9d8846f) is a DEAD END. (a) Screen:
  known entropy-regularised rates are poly(1/(1−γ), 1/τ) (Cen et al. arXiv 2007.06558 Thm 1; Cen-Wei arXiv 2105.15186 Thm 3); both
  factors are exponential for parity (1/(1−γ) = n^Θ(d); τ below action gaps 2^−O(n d log n)); HMZ Thm 6.5 as in DE25. (b) Data
  (experiments/new/ipm/n7.py, results/*.n7.csv): stalls mid-path on counter_ortl N=3 (same instance as DE25; τ ≈ 2.83e-7) and tc+
  N=2; start-phase failures on tc N=4, counter_symsi N=1-2, counter_rob N=2; every produced answer correct. Lead re-run on
  counter_ortl-3 (08:22Z): no solution, τ = 2.8349e-07 at the 3,000-iteration cap (lane: 3,213 iterations, "stalled/tau38", same τ;
  CHECKER C21 with --maxit 20000 reproduced the lane row to every digit).
  Screen rule recorded by the lane (N7 §4): every method that works on the parity → discounted reduction and whose analysis is
  polynomial in 1/(1−γ) is no better than strategy iteration (HMZ Thm 6.5); such a candidate needs a γ-free argument before any bench.
- DE27 (2026-10-22): the k-pools attack on (NEST*-BOUNDED) (GAPS G-NEST; RESULTS R16) is CLOSED without a family (L-RED boxes 16-19,
  docs/red/R49-nest4-attempt.md, R50-kpools.md, R51-piecemap.md; l-red e1c3f2b, b575ae7, 4f73e7a, c6ac001). DATA: class best NEST* on
  𝒞^1P went 3 → 6 (nest4u_n46 ae7ed559 and nest4uu_n51 302c03a8 NEST* 4, nest5_n49 fe50a2c9 NEST* 5, nest6_n75 dc8b04cc NEST* 6; each
  re-run by the Lead in both orders with pinned Oink: even iterations = S, solutions verified); k = 4 parts: NEST* 6, no 7, in climbs
  (≥ 650 / ≥ 300 steps) and in 448 hand-built gate/return configurations (k4u_n101 sha1 37a45ff8a932bcc6e4a79d4848a0a57dbb82367a,
  NEST* 6, S 25; k4L72r_n101 e84a57b6f13e546811c203bf35b86a0ee8b69462, S 31, NEST* 5); S ≤ 31 at n = 101 throughout (about n/3).
  Obstruction (reading, one seed, R51 §4-§5): a seventh level needs a longer post-block stretch with no shallow first change inside it;
  no edge class tried gives both. False single-pool laws found on the way (R49 §6, §8): (G-NEXT) and (G-ADJ) (nest4u_n46 transition
  #3, nest4uu_n51 #16, nest5_n49 #2), (O-SEG) (oseg_n26, sha1 381b7b9d…), (W) (near4_n26, 6d7c5e38…). Closed by the Lead (decision 07:35Z under
  L37 (3); Lead reading): even a family refuting (NEST*-BOUNDED) would not give a super-polynomial family while S stays linear (S ≤ 31
  at n = 101, DATA). (NEST*-BOUNDED) stays OPEN.
