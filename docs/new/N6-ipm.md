# N6: interior-point method on the P-matrix LCP of the discounted game (L-NEW successor 5, Opus 5.5; box 12)
Lead GO 07:18Z 2026-10-22 (date -u): screen first, with an opened source for each item; code only if the screen leaves a live question.
Status: DEAD END (§8). Proof route dead at the screen (§2, §5); on data the implemented path-following IPM (central mode) gives NO ANSWER on 7 of 13
hard families at small N and on every random game with n >= 23 (§7), from loss of the central path where the kappa effect collapses
Newton's convergence region (§6). Every answer that WAS produced is correct (Oink zlk regions, verify.py strategies).

## 0. The approach
parity game G (n vertices, priorities ≤ d) → mean-payoff game (weights (−n)^p, Jurdziński) → discounted game with γ ≥ β_G →
binary 2TBSG (every state two actions; out-degree > 2 split into binary trees, out-degree 1 doubled) → LCP (M, q) of Jurdziński-Savani
→ primal-dual path-following IPM (wide neighbourhood, Kojima-type) at counted bit precision → round (w, z) to a positional profile
(at state i keep the action whose slack is the smaller) → strategies checked by experiments/harness/verify.py, regions against Oink.

## 1. Sources opened (all in this session, 2026-10-22; PDFs in the scratchpad, sha256 prefixes)
- HIJ: T. D. Hansen, R. Ibsen-Jensen, "The complexity of interior point methods for solving discounted turn-based stochastic games",
  arXiv 1304.1888 v2 (CiE 2013), sha256 01e4cde9b47f90cb. §2.3 (JS reduction, Definition 16, Theorem 18), §3 Theorem 19, Theorem 21,
  §4 Theorems 22-25, §1.1.
- ABGJ: X. Allamigeon, P. Benchimol, S. Gaubert, M. Joswig, "Log-barrier interior point methods are not strongly polynomial",
  arXiv 1708.01544, sha256 9608058cb6fa98a3. Theorem A (= Thm 25), Theorem B (= Corollary 31), Remark 32, introduction p.2-3.
- dKN: E. de Klerk, M. E.-Nagy, "On the complexity of computing the handicap of a sufficient matrix", Math. Program. 129(2) 2011;
  preprint optimization-online 2010/02/2555, sha256 726c92b99e80dae6. Abstract, Definition 1, §3.
- Friedmann, "An exponential lower bound for the latest deterministic strategy iteration algorithms", arXiv 1106.0778 (LMCS 7(3:19)),
  sha256 46c96f44775aa2b0. §9: definition of β_G and Theorem 9.3 (Zwick-Paterson).
- HMZ: T. D. Hansen, P. B. Miltersen, U. Zwick, "Strategy iteration is strongly polynomial for 2-player turn-based stochastic games
  with a constant discount factor", arXiv 1008.0530 v1, sha256 f53a6b5127d95078. Theorem 6.5.
- FJS: Fearnley, Jurdziński, Savani, arXiv 0909.5653 v1 (sha256 9fbd86643615f000): opened for B13 only (pivoting).

## 2. (a)+(b) What is known about IPMs on exactly these LCPs: HIJ, and why the κ route is dead
- The reduction is known and analysed. HIJ Definition 16: for a 2TBSG with two actions per state, split into profiles σ, τ,
  M_{G,σ,τ} = I(I − γP_σ)(I − γP_τ)^{-1}I and q = I(I − γP_σ)(I − γP_τ)^{-1}c_τ − Ic_σ (I = diag(±1) by owner). Theorem 18: M is a
  P-matrix and the LCP solves G. M does NOT depend on the costs c (only q does).
- HIJ Theorem 19: M is P*(κ) for κ = n/(1−γ)². Theorem 21: for the one-player arena G_n (states 1, 2 self-loops, every i > 2 has one
  edge to 1 and one to 2), M is not P*(κ) for any κ < γ²(n−2)/(8(1−γ)²) − 1/4. So κ = Θ(n/(1−γ)²) in the worst case, and the
  Kojima-Megiddo-Noma-Yoshise bound O((1+κ)n^3.5 L) is O(n^4.5 L/(1−γ)²) and cannot be improved by bounding κ (HIJ §3, first para).
  Theorems 22-25: the same for the potential-reduction method of Kojima-Megiddo-Ye: −δ/θ = Θ(n^1.5/(1−γ)³) in the worst case.
  HIJ §1.1 note these bounds are WORSE than value iteration's O(n² L/(1−γ) log(1/(1−γ))), and leave open whether the true running
  time is smaller.
- dKN abstract: the handicap of a sufficient matrix may be exponential in its bit size, so the known IPM bounds are not polynomial
  in the input size in general. HIJ makes this concrete for game matrices: κ is polynomial iff 1/(1−γ) is.
- The discount parity needs. Friedmann 1106.0778 §9: β_G = 1 − 1/(4|V|³·max|r|) with Theorem 9.3 (Zwick-Paterson): optimal
  strategies of the discounted game at β_G are optimal for the mean-payoff game. With Jurdziński weights max|r| = n^d, so
  1/(1−γ) = 4n^{d+3}: κ = Θ(n^{2d+7}) on G_n-shaped arenas, exponential when d = Θ(n). Since M ignores the costs, ANY parity game
  whose binary arena is G_n (priorities arbitrary) has this κ at this γ.
- Why no cleverer γ rescues the κ route (L-NEW reading, not a theorem): HMZ Theorem 6.5: strategy iteration on a 2TBSG terminates in
  (m+1)(1 + log_{1/γ}(n²/(1−γ))) = O(m/(1−γ)·log(n/(1−γ))) iterations. So ANY reduction parity → 2TBSG with poly size and 1/(1−γ) =
  poly(n) would already put parity games in P via strategy iteration, with no IPM. Whenever the KMNY/KMY bound for N6 is polynomial,
  HMZ's bound for SI is polynomial too: the κ route can never give more than SI already gives. A polynomial N6 needs a NEW
  analysis of the IPM that is independent of κ, θ and δ (the open question HIJ §1.1 states).
  Sketch of why the standard schemes need 1/(1−γ) ≥ n^{Ω(d)}: a priority-to-weight scheme correct on mean-payoff cycles needs
  |w_{p+1}| > (n−1)|w_p| (a cycle with one (p+1)-vertex and n−2 p-vertices), and on the lasso "Even chooses between a self-loop of
  priority 1, or one step through a vertex of odd priority d−1 followed by a self-loop of priority 2" the discounted values are
  w_1/(1−γ) vs γw_{d−1} + γ²w_2/(1−γ); parity says take the lasso, which needs 1/(1−γ) ≳ |w_{d−1}|/(|w_1| + |w_2|) ≥ (n−1)^{d−3}.
- Transfer of ABGJ (Lead item (a)). Statement (Theorem B = Cor. 31): every log-barrier primal-dual path-following IPM that stays in
  the wide neighbourhood N^{−∞}_{θ,t} of the central path of the LP LW_r(t) (2r variables, 3r+1 constraints) needs ≥ 2^{r−1}
  iterations to reduce the duality measure from t² to 1, provided t satisfies their condition (36); p.3: "It is doubly exponential in
  r, implying that the bitlength of t is exponential in r, which is consistent with the polynomial time character of interior point
  methods in the bit model." Transfer to our LCPs: NOT as stated. (i) LW_r(t) is an LP (a monotone LCP, P*(0)); our M is a P-matrix
  with κ up to Θ(n/(1−γ)²), not an LP. (ii) Their bound needs bitlength exponential in r; our (M, q) has polynomial bitlength
  (§3). (iii) ABGJ do not mention games (`grep -i game` on the text: no hit outside references). The tropical mechanism is still
  RELEVANT: our data are Puiseux-like in the base n (γ = 1 − n^{−(d+3)}/4, costs ±n^p), so a long-and-winding central path with
  poly-bounded exponents is not excluded; RANKING.md row 7's question (do the LW LPs tropicalize to parity games?) stays open and is
  the natural route to a lower bound for N6, not to an upper bound.

## 3. (c) Bit costs (TARGET.md §3)
- γ: 1 − γ = 1/(4n'^{d+3}) with n' the binary arena's size: O(d log n) bits. Costs (−n')^p: O(d log n) bits.
- M and q: entries are rationals whose numerators and denominators are minors of (I − γP), integer after scaling by 4n'^{d+3}:
  O(n·d log n) bits each (Hadamard). Polynomial.
- IPM precision: each Newton step solves (ZM + W)Δz = rhs. Rounding to an exact optimal profile needs the duality gap below the
  separation of reduced costs, which are rationals with denominators bounded by the same minors: log(1/ε) = O(n d log n) bits.
  Kojima-type IPMs carry O(L) bits per iteration (standard). So per-iteration cost is polynomial; the ONLY non-polynomial term in
  the known bound is the iteration count through κ (§2).
- Verdict on (c): no exponential precision is needed; the method is dead at the screen only through κ (§2), i.e. as a PROOF route.

## 4. (d) BARRIERS and the dead-end record
- B13 (Lemke, Cottle-Dantzig on the same LCPs, 0909.5653 Thm 18-19): pivoting methods; N6 is not a pivoting method: outside.
- B15 (log-barrier and self-concordant IPMs are not strongly polynomial): about strong polynomiality on LPs with exponential
  bitlength; N6's inputs have polynomial bitlength: does not apply in the bit model (§2, ABGJ transfer).
- B18 (Howard / discounted PI exponential at one γ): N6 is not policy iteration; same γ regime (§2), so the discount itself is not
  the barrier for N6, only for its κ-based analysis.
- B19 (LDT weight compression, 2503.17294): N6 does not compress weights; it pays their bits (§3): outside.
- B8-B12, B14, B16, B17: not applicable (no switching rule, no cube, no automaton).
- MISSING ROW (for L-LIT, finding): HIJ 1304.1888 (κ = Θ(n/(1−γ)²), −δ/θ = Θ(n^1.5/(1−γ)³) for the JS LCPs of 2TBSGs) is the
  directly relevant known result for any IPM-on-game claim and is not in BARRIERS.md or RANKING.md row 7.
- Dead-end record: X1 SCALE-VI (bit-scaled value iteration, dead by argument: pseudo-polynomial per phase) and N1 (discount
  schedules, killed) are different methods; no IPM was ever run in the fleet (RANKING row 7; N4 tropical simplex proposed, not run).

## 5. Screen verdict
- As a PROOF route N6 is DEAD AT THE SCREEN: the only known analyses (KMNY, KMY) go through κ or −δ/θ, which are Θ(n/(1−γ)²) /
  Θ(n^1.5/(1−γ)³) (HIJ Thm 19/21/22-25), exponential at the discount parity needs (Friedmann β_G); and a reduction with polynomial
  1/(1−γ) would make SI polynomial already (HMZ Thm 6.5), so the κ route can never beat SI.
- LIVE QUESTION (HIJ §1.1 states it open): is the ACTUAL iteration count of a standard wide-neighbourhood path-following IPM on
  these LCPs polynomial in n and L? Cheap to measure: §7. A polynomial-looking count would still need a κ-free proof (gauntlet
  step 4); an exponential-looking count kills N6 on data.

## 6. The obstruction on data: path following loses the path (counter_ortl N = 3, n = 16)
Instance experiments/new/instances/n6/counter_ortl-3.pg (Oink counter_ortl 3; sha1 c8bc349942b32305edee56ba8fb7d6504ed86622), 18 binary
states, d = 13, 1/(1−γ) = 4·18³·19^13 ≈ 1.0·10^21 (70 bits), so HIJ's κ scale n/(1−γ)² ≈ 10^43.
- M is a P-matrix: all 262,143 principal minors positive (arb, rigorous; scratch pminors.py). So the central path exists and K = W + ZM is
  nonsingular everywhere (the stall is not a modelling error).
- Central-path mode (centring by target following, 141 steps, then 36 μ-reductions) stalls at μ = 3.1911583…·10^−26 (scaled costs): with
  the μ-factor allowed to approach 1 (1 − 10^−6, 1 − 10^−12, 1 − 10^−30) the run stalls at the SAME μ (2,147 / 3,467 / 7,147 Newton steps);
  with neighbourhood 0.5, 0.1, 0.01 the same; with precision 8, 16, 32 × bits (704, 1264, 2384 bits) identical counts. Precision is not
  the cause: the Newton direction is certified by an arb ball (dz_7 = 2.4850·10^5 ± 0.03 at Newton step 1559, residual 10^−189).
- What happens (N6LIM diagnostic): state 7 (Even, edges to 0 and 14) has BOTH slacks tiny (z_7 ≈ 0.05, w_7 ≈ 10^−25) while the path point
  needs z_7 ≈ 2.5·10^5. The iterate satisfied the product neighbourhood (every w_i z_i within 50% / 1% of μ) yet sat far from the path in
  coordinate space: with κ ≈ 10^43 the inverse of z ↦ (q + Mz)∘z is so distorted that a product-space neighbourhood does not localise the
  point. Every Newton step then wants z_7 up by ~5·10^6× and w_7 below zero; the fraction-to-boundary step is 10^−7…10^−22 and the
  iterate never re-enters the neighbourhood. This is the mechanism behind HIJ's κ factor (short-step theory shrinks the neighbourhood and
  the μ-step by ~1/(1+κ)), seen on a 16-vertex game.

## 7. Bench (gauntlet step 2 in miniature; experiments/new/ipm/results/*.csv, every produced solution checked by check_sol2.py)
Method: n6.py track() (default, "central"): natural strictly feasible start y = 2/(1−γ)·sign (no big-M; w, z ≥ 1 after scaling), centring
by target following (targets move ≤ ×2 per step), adaptive long-step μ-targets (factor f, success f ← f², failure f ← √f), Newton with
fraction-to-boundary 0.99, proximity max_i |w_i z_i/μ − 1| ≤ 0.5; rounding certified with verify.py after every μ-step. Variant
"weighted" (N6PATH=weighted): follow the weighted path w∘z = t·p0 on which the start lies exactly, t → 0, no centring. Count = Newton
steps (each O(n³) at O(bits) precision). Earlier variants (infeasible start with KMM residual control, big-M embedding, Armijo on the
max-norm proximity, log-coordinate Newton) were worse; all are in n6.py (ipm(), env switches) and recorded in the notebook.
| family | N tried | central: Newton steps to a certified answer | weighted | no answer (both modes) from |
| --- | --- | --- | --- | --- |
| tc | 1-5 | 134, 269, 302, -, - | 62, -, -, -, - | central N = 4 (n = 68), weighted N = 2 |
| tc+ | 1-3 | 74, -, - | 0, -, - | N = 2 (n = 24) |
| counter_m | 1,2,3,4,6,8,10 | 69 … 373 (N = 8), 919 (N = 10) | 29 … 375 (N = 6), -, - | weighted N = 8 |
| counter_rr | 1,2,3,4,6,8 | 0, 42, 66, 90, 145, 203 (≈ 25N) | 0 … 93 | none |
| counter_dp | 1,2,3,4,6,8 | 124 … 646 (N = 6), - (N = 8) | 2 each | central N = 8 |
| counter_qpt | 1-8 | 1-2 | 0 | none |
| counter_core | 1,2,3,4,6 | 151, 345, 799, -, - | 2 each | central N = 4 |
| counter_ortl | 1,2,3,4,6 | 108, 249, -, -, - | 22, 82, -, -, - | N = 3 (n = 16), BOTH modes |
| counter_symsi | 1-3 | -, -, - | 222, -, - | central N = 1, weighted N = 2 |
| counter_rob | 1-2 | 412, - | -, - | central N = 2 (n = 31), weighted N = 1 (n = 14) |
| recursiveladder | 1-5 | 16 … 221 | 0 … 503 | none |
| switchallexp / switchbestexp | 1-3 / 1-2 | centring fails; the final rounding is nevertheless certified (225-305 steps) | 0 (start rounding already optimal) | none |
| hij (HIJ's G_n arena, d = n) | 4, 8, 16, 32 | 17, 36, 80, 180 (≈ 5.6n) | 0 | none |
Random games (gen.py n, d = n, out-degree 1-4, seeds 20261023-20261062, n = 5..30; random.central.csv): 27 certified answers (all n ≤ 22),
13 without an answer: every game with n ≥ 23 (8 of 8) and 5 of 32 below; 30 produced solutions all correct.
Where the method converges, step counts grow mildly (counter_rr ≈ 25N, hij ≈ 5.6n, tc2 ≈ 5.5 steps per decimal digit of 1/(1−γ) in a
γ-sweep), so the iteration count itself never looked exponential; the failure mode is loss of the path (§6), which a theory-backed
short-step method would replace by μ-steps of relative size ~1/κ = n^{−Θ(d)}, i.e. the exponential count of §2.

## 8. Verdict: DEAD END (recorded in notes/L-NEW.md "Dead ends")
- Proof route: dead at the screen (κ = Θ(n/(1−γ)²), HIJ Thm 19/21; parity forces 1/(1−γ) = n^{Θ(d)}, Friedmann β_G; HMZ Thm 6.5 makes SI
  polynomial whenever the κ bound is).
- Gauntlet step 2: FAILED: no answer on tc (N = 4 central), tc+ (2), counter_ortl (3, both modes), counter_symsi, counter_rob (2) and on every
  random game with n ≥ 23; all produced answers correct. Exact obstruction: §6 (path lost where the product-space neighbourhood stops
  localising the iterate; Newton direction certified; M certified P). Killing instance: counter_ortl-3.pg (sha1 c8bc3499…), 16 vertices.
- Not shown: a super-polynomial ITERATION COUNT for a convergent IPM. Whether some IPM variant is polynomial on these LCPs stays the open
  question HIJ §1.1 states; nothing here answers it, and the κ route cannot (§2).
