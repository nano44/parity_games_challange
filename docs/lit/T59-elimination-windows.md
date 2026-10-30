# T59: elimination windows without discount, the exponential families' windows, and the contraction (C) for arena-optimum rules
L-LIT successor T59 (Opus 5.5), D18. Lead's brief 2026-10-30 (after 17:48Z): (a) undiscounted / deterministic analogues of the
elimination window, (b) the window HW of the known exponential families and whether L-RED R140's ARENA-MAX rules out its mechanism,
(c) contraction-type arguments for "best response against a fixed opponent" rules, (d) a table. Inputs: L-LIT T58 (l-lit d78e1815),
L-RED R140 (l-red 47000632; read at l-red 717f407a), RESULTS R17, R88 (FW-R*), R89 (GP*-RUN). Written 2026-10-30 17:50Z-18:40Z (date -u).
Working note, unrefereed, not a TARGET.md claim. G-N5-TIME, XI-CH-POLY and ELIM-WIN stay OPEN.
Labels: PROVED (source) = proved in the opened source; PROVED (L-LIT) = proved here, elementary, unrefereed; DATA = measured here with
docs/lit/T59-dz-check.py or T58-elim-check.py; READING = my interpretation; CONJECTURE / OPEN / DEAD as in T54.
Notation as in T58: F = a W-run with states p..q (τ fixed, no fallback, λ_W fixed); W_t = val(σ_t, τ); Ξ_t; Iσ_t; H_t = S4a's arena
(Even v keeps {σ_t(v)} ∪ Iσ_t(v), Odd keeps τ(v)); HW_F as in T58 §4; an Even edge is BLOCKED at t if it is W-better than σ_t's
choice but not in Iσ_t (R88).

## Summary
- (a) Undiscounted polynomial windows exist in the literature only for coordinated single-switch rules on deterministic MDPs.
  - Zhong-Ye 2609.40147 Thm 7.1 is the cleanest. Dantzig's rule on undiscounted deterministic average-reward MDPs is strongly
    polynomial. Its proof, eq. (7.2)-(7.6), is an (R)+(P)+(C) elimination with no discount:
    - the reference is the last policy of a stretch with unchanged cycles;
    - fluxes are path lengths < N;
    - the contraction factor is 1 − 1/N² per step, supplied by "the switch with the largest residual".
  - Howard's PI has no such window. Zhong-Ye Thm 6.1 makes it exponential on undiscounted deterministic MDPs with M ≤ 4N. That
    disproves the Hansen-Zwick "iterations ≤ edges" conjecture (HZ slides p.19).
  - Scherrer p.6 observes that on Hansen-Zwick's example the per-step contraction decays like 1 − (2/n)^k.
  - All other undiscounted bounds are pseudo-polynomial and come from value-iteration domination: Zwick-Paterson Thm 2.3,
    O(|V|³|E|W); Zhong-Ye Thm 7.2, O(N³2^b); Mukherjee-Kalyanakrishnan Thm 1.2, subexponential in the reward bit size b.
- (b) Lemma HW-LB (PROVED, L-LIT; the converse of T58's counting): any improvement run with T transitions has HW ≥ T/(m₀ + 1),
  where m₀ is the number of the improving player's edges.
  - So EVERY exponential family has an exponential window. "Is HW exponential?" is automatic. The real question is which mechanism
    keeps every in-use edge coming back.
  - The mechanisms that NO-LOCAL-DELAY (ARENA-MAX) rules out: the deceleration lane against an improving-but-not-greedy edge.
    - Friedmann G_n.
    - Fearnley's MDP.
    - Asadi-Chatterjee-de Raaij.
  - The mechanism it does NOT rule out: Friedmann's switch-best family H_n (LMCS 1106.0778 §8, Thm 8.4).
    - It defeats a rule that has the ARENA-MAX property by definition: I^glo, LMCS p.7, «Ξσ′ ⊑ Ξσ* for every σ′ in A_{G,σ}».
    - It does so with STUBBORN CYCLES: three Even nodes, so that closing needs ≥ 2 switches and one cycle edge is never an improving
      edge (§8.2 p.28-29).
    - That is exactly R140's DECEL-RED requirement (a Ξ-blocked closure). So ARENA-MAX alone cannot give ELIM-WIN.
    - What stops H_n in N5 is not ARENA-MAX. DATA: N5 on switchbestexp N = 4, 6, 8 has 2 W-runs, the largest 31 / 44 / 57
      transitions, with HW 1 / 2 / 3.
- (c) Contraction for arena-optimum rules.
  - Lemma C-DISC (PROVED, L-LIT; discounted shadow): an arena-optimum step against a fixed opponent contracts toward the
    opponent-fixed optimum by γ, provided the arena contains a one-step-greedy edge at every vertex (HMZ Lemma 5.3-5.5 mechanism).
  - Lemma DZ-W (PROVED, L-LIT, conditional; transfer of Zhong-Ye (7.2)-(7.6)): inside a W-run with unchanged W-cycles, N5 contracts
    the numeric W-gap by 1 − 1/(K n²) and has HW ≤ K n² ln(n²) + 2, provided BLOCK-RATIO_K holds. BLOCK-RATIO_K: the largest
    residual of a reference edge is ≤ K × the largest residual of an ALLOWED edge.
  - Both lemmas fail at the same place: BLOCKED edges. FW-R* (R88) also localizes there.
  - DATA kills the route: on L-RED's fx_K_m16 (K = 4, 8, 16) BLOCK-RATIO's K is 2^(2K) (256; 65,536; 4.3·10⁹), and the gap never
    falls by a factor n² before the last transition (WINC = |F|). Yet HW = 17 throughout.
  - So the gap/contraction template (R)+(P)+(C), with the end-of-run reference and the canonical additive embedding of W, cannot
    prove ELIM-WIN. DEAD as a route; the reason is exactly fx. Any proof of ELIM-WIN must count edges combinatorially (as GP* does),
    not contract a potential.
- (d) The table is in §5.

## 1. Sources (opened 2026-10-30 in scratchpad t59/A; sha256 prefixes in notes/L-LIT.md)
- [ZY] Zhong-Ye, arXiv 2609.40147 v2 (2026-10-13), «Policy Iteration Is Not Strongly Polynomial for Deterministic MDPs: The Price of
  Algorithmic Anarchy». Opened at: Table 1 p.2; p.2 «the lower bound disproves the conjectured M-iteration upper bound (Hansen, 2012;
  Asadi et al., 2025)»; Thm 6.1; Thm 7.1 with proof eq. (7.1)-(7.6) (PDF pp.31-32); Thm 7.2 with proof (p.33).
- [HMZ] arXiv 1008.0530 v1. Lemma 5.3 «T v^{π0} ≥ v^{π1}» and Lemma 5.5 (p.10); Lemma 6.4 (p.11); §7 p.11 (Friedmann: exponential
  «for non-discounted 2TBSG, or when the discount factor is part of the input»). HMZ give no lower bound of their own.
- [ZP] Zwick-Paterson, TCS 158 (1996) 343-359 (people.irisa.fr copy). Thm 2.3 p.5: values in O(|V|³|E|W) time via k = 4n³W
  value-iteration steps. Fig. 1 p.6: k = Ω(n³W) needed. Thm 5.2 p.10-11: |v(λ) − v| ≤ 2n(1 − λ)W between discounted and mean payoff.
- [ACR] Asadi-Chatterjee-de Raaij, arXiv 2506.12254 v1 (UAI 2025). Table 1 and p.2 («by Howard [1960], the number of policy iteration
  steps is at most the number of value iteration steps, which by Zwick and Paterson [1996] is bounded by O(n³W)»). Thm 3.2 p.4.
  Policy families π_i, σ_{i,j}, τ_i and sequence (1) p.4. Lemma 4.1 p.5. Intuition p.4-5 ("all progress ... is lost").
- [HZ] Hansen-Zwick ISAAC 2010 talk slides (as T35). p.14 main theorem; p.15 «Use cycles of very large cost»; p.19 Conjecture «at most
  the number of edges». The paper itself is NOT OPENED (the predecessors' attempts failed; not retried).
- [Sch] Scherrer arXiv 1306.0386 v4. Lemma 8 p.6 and its proof in §10 (deterministic Howard: a new cycle within n iterations; proof by
  (γP)^n). p.6-7 on HZ's example: «v*(i) − v^{πk+1}(i) ≥ [1 − (2/n)^k](v*(i) − v^{πk}(i)) ... the amount of contraction gets
  (exponentially) smaller». p.4: Fearnley exponential for γ = 1, Hollanders et al. near 1.
- [MK] Mukherjee-Kalyanakrishnan, arXiv 2505.00795 v1 (ICAPS 2025). Thm 1.2 p.2: HPI on DMDPs visits ≤ nk·u·exp(u) policies with
  u = O(√(nb log(nb)) + b). Method p.2 and §4: a threshold discount γ_Q beyond which HPI's trajectory is invariant. 1/(1 − γ_Q) is
  bounded by root separation of integer polynomials with coefficients O(2^b) (Borwein-Erdélyi-Kós, their Thm 4.5).
- [F09] Friedmann arXiv 0901.2731 v1. §4 p.4-5: deceleration lane, stubborn cycle, «If we want to postpone player 0 updates closing a
  cycle, we basically need to make sure that this is at least impossible to be done in one iteration». Thm 8 p.6.
- [F11] Friedmann arXiv 1106.0778 v2 (LMCS 7(3:19)). p.7: I^glo «for an arbitrary strategy σ′ in the arena A_{G,σ} that Ξσ′ ⊑ Ξσ*».
  Thm 6.14. §8.1 Lemma 8.1 p.28 (the lane reset must persist two iterations). §8.2 p.28-29: stubborn cycles («it is impossible to close
  the cycle within one iteration»; «the global policy makes no progress towards closing the cycle»). Thm 8.4 p.33 (≥ 2^n on H_n).
- [Fe] Fearnley arXiv 1003.3418 v1. Prop. 4 p.6 (Appeal^π(b_i, a_i) < Val^π(b_i) + 1 when a_i is not chosen). §4.2 p.6. Thm 17, 18.
- [Hol] Hollanders PhD thesis (UCLouvain; author page PDF). Ch. 2 printed pp.31-32: Fearnley's example extended to discounted MDPs
  «provided that the discount factor approaches one sufficiently fast».
- [AGKS] Allamigeon-Gaubert-Katz-Skomra arXiv 2206.09044 v2. p.2: Zwick-Paterson's pseudo-polynomial value iteration; Friedmann:
  policy iteration exponential. Thm 1 p.6: escape rate of nonexpansive semialgebraic Shapley operators. Opened for context only; no
  window statement.
- Downloaded, abstract only: arXiv 2503.04203 (Mustafin et al.). NOT OPENED: HKZ SODA 2014 (SIAM paywall; its content only via the CRIS
  abstract); Hansen thesis 2012; the Hansen-Zwick paper; Zwick-Paterson's Howard ≤ VI remark (cited through [ACR] p.2 only).

## 2. (a) Undiscounted / deterministic windows
### 2.1 Zhong-Ye Thm 7.1: an undiscounted (R)+(P)+(C) elimination (PROVED in [ZY]; anatomy mine)
- Setting: deterministic average-reward MDP; Dantzig's rule (5.3) switches ONE pair with the largest improvement.
- (R): the last policy π_T of a run of consecutive "bias updates with unchanged cycles".
- (P): eq. (7.2), Σ_s (V^{πT}(s) − V^{πt}(s)) ≤ N²·max residual. Each path has < N edges, and the telescoping ends on the shared cycles,
  where V^{πt} = V^{πT}.
- (C): eq. (7.3)-(7.4). The switched state gains at least its residual, and every bias is monotone, so the gap shrinks by 1 − 1/N².
  - This is the rule's coordination: the single switch is the largest residual over ALL pairs.
  - The proof needs no discount. The constant does not depend on the reward sizes (strongly polynomial).
- Elimination: eq. (7.5). The pair (s, a) of π_t maximizing V^{πT}(s) − Q^{πT}(s, a) carries ≥ gap/N², so a is never used at s after
  2N² log N more steps. Then eq. (7.6): O(N²M log 2N) bias updates with unchanged cycles.
- Cycles: counted separately (7.1). Gain updates ≤ N(N + cycle creations).

### 2.2 What Howard lacks, and the pseudo-polynomial substitute
- Howard's PI on undiscounted deterministic MDPs.
  - [ZY] Thm 6.1: exp(Ω(N)) iterations, M ≤ 4N, strongly connected. That rules out any polynomial window, by HW-LB below.
  - [Sch] p.6: on [HZ]'s example the contraction factor tends to 1 like 1 − (2/n)^k. So no per-step (C) is available.
  - [Sch] Lemma 8: a new cycle within n iterations. It is a combinatorial window for the NO-NEW-CYCLE event, not an elimination.
    - It is the same shape as RESULTS R17 (N5 on one-player games: a λ-phase has ≤ n − 1 value-changing steps).
- The undiscounted substitute for (C) is VALUE-ITERATION DOMINATION.
  - [HMZ] Lemma 5.3: one SI step ≥ one Bellman step. [ACR] p.2: PI steps ≤ VI steps, and VI needs O(n³W) steps by [ZP] Thm 2.3.
  - [ZY] Thm 7.2: O(N³2^b), via "each cycle creation raises Σ gains by ≥ 1/N".
  - All of these are pseudo-polynomial in W. [ZP] Fig. 1 shows the Θ(n³W) VI bound is tight.
- READING (parity). A parity game is a mean-payoff game with weights up to n^Θ(d) (standard reduction; not re-opened in T59).
  - With [ZP] Thm 5.2 it becomes a discounted game with 1 − γ = n^−Θ(d). HMZ's window L = log_{1/γ}(n²/(1 − γ)) is then n^Θ(d).
  - So the discounted (C), applied to parity, gives an n^Θ(d) window: pseudo-polynomial, i.e. exponential in d. This is the
    quantitative form of T58's «(C) is missing».
- [MK] is the one undiscounted result that is neither pseudo-polynomial nor exponential.
  - It is subexponential in n for fixed reward bit size b. It works by moving to the threshold discount γ_Q (trajectory invariance)
    and bounding 1/(1 − γ_Q) by root separation of integer polynomials. That is a number-theory input.
  - For parity, b = Θ(d log n), so it gives no polynomial bound. It is also one-player only.
  - READING: the threshold-γ idea is the natural bridge between N5's ordinal W and the discounted (C) of §4.1. It would need the
    restricted arenas H_t to be γ-invariant beyond some γ_Q with 1/(1 − γ_Q) ≤ poly. Exponential weights make that false in general
    (the separation bound is exponential in b).

## 3. (b) The exponential families: windows and mechanisms
### 3.1 Lemma HW-LB (PROVED, L-LIT, elementary)
- Statement. Let σ_0, …, σ_T be any sequence of strategies of one player, with σ_t ≠ σ_T for t < T. Let m₀ be the number of that player's
  edges. Define HW as in T58 §4. Then T ≤ (m₀ + 1)·HW, i.e. HW ≥ T/(m₀ + 1).
- Proof. T58's counting argument uses no property of the rule. From t_0 = 0, within HW transitions some edge of σ_{t_0} not in σ_T is
  used for the last time. Set t_1 := t_0 + HW and repeat. The retired edges are distinct (a retired edge never returns), and there
  are at most m₀ of them. □
- Consequence. Every family below with T = 2^Ω(n) and polynomial size has an exponential window: HW ≥ 2^Ω(n)/poly(n). Within one
  exponential run, the in-use edges keep coming back for exponentially long. That is T58's «counter in which every digit returns».

### 3.2 Per family (rule, count, HW, mechanism, and whether ARENA-MAX rules the mechanism out)
- Friedmann G_n ([F09] Thm 8; [F11] Thm 6.14).
  - Rule and count: locally optimizing; 13·2^n − 9 iterations; quadratic size. HW ≥ 2^n/O(n²).
  - Mechanism: a deceleration lane offers a fresh locally-best edge every iteration. The bit's simple-cycle closure is improving but
    not locally best.
  - RULED OUT by ARENA-MAX / NO-LOCAL-DELAY. DATA (R140): V1 = S4a against σ̄ is linear, 8-14. First divergence at iteration 1, where
    every bit cycle closes at once.
- Friedmann H_n ([F11] §8, Thm 8.4; PGSolver switchbestexp).
  - Rule and count: I^glo (Schewe's globally optimal). I^glo is an arena optimum by definition ([F11] p.7). Count ≥ 2^n (PGSolver
    289, 593, 1201, 2417 at N = 4-7; l-new box 57). HW exponential.
  - Mechanism: stubborn cycles. Three Even nodes; two leave to the lane and one enters per iteration, so «no progress towards closing
    the cycle». The lane reset persists two iterations (Lemma 8.1).
  - NOT ruled out by ARENA-MAX. The closure is never inside the arena (one cycle edge is non-improving each iteration). That is
    exactly a Ξ-blocked closure, the mechanism R140's DECEL-RED says a port must use.
  - DATA (this note, T58/T59 scripts): N5 on switchbestexp N = 4, 6, 8 has 2 W-runs, largest 31 / 44 / 57, HW 1 / 2 / 3, RETMAX 2. N5
    totals 47 / 62 / 77 (l-new 85c12579 box59/freeze_all.txt).
  - So the counter dies in N5 for reasons other than arena maximality. READING: (i) S4a is against τ_t, while I^glo lets Odd
    best-respond; l-new box 57's Lemma STALE describes how the frames differ at Odd-reset steps. (ii) N5's own τ-steps. Not
    separated here (OPEN).
- Fearnley MDP ([Fe] Thm 17/18; [Hol] Ch. 2 for discounted with γ → 1 fast).
  - Rule and count: Howard; 2^Ω(n); one player. HW exponential.
  - Mechanism: a_i is improving (its appeal exceeds Val(b_i) whenever g_i is better), but its appeal is < Val(b_i) + 1 (Prop. 4).
    The lane always offers an action with appeal ≥ Val(b_i) + 1.
  - RULED OUT (READING): a one-player arena optimum over {π(s)} ∪ improving sees Val(g_i) through a_i (Prop. 2) and takes it at once.
    No run; not a parity game. One-player parity games are covered by R17 anyway.
- Zhong-Ye average-reward DMDP ([ZY] Thm 6.1).
  - Rule and count: Howard; exp(Ω(N)); M ≤ 4N. HW exponential.
  - Mechanism: CYCLE-type (T37: «encoded cycles have strictly increasing mean rewards»).
  - Under ARENA-MAX: NOT ANALYZED (construction not read in T59). Its transfer to N5 is blocked anyway by R47's bound on cycle-type
    changes (T37 §0).
- Zhong-Ye discounted ([ZY] Thm 2.1-2.3).
  - Howard; exp(Ω(N)); TIMING-type (T37). No N5 analogue (T37).
- Hansen-Zwick ([HZ] p.14; [ACR] Table 1).
  - Howard; m − n + 1 iterations (polynomial); weights n^(n²). HW is not forced to be large (HW-LB gives only ≥ 1).
  - Mechanism: «cycles of very large cost make Howard favor going through many edges» (p.15). Window not computed (paper NOT OPENED).
  - Its conjecture (≤ m iterations) is DISPROVED by [ZY] Thm 6.1 ([ZY] p.2).
- Asadi-Chatterjee-de Raaij ([ACR] Thm 3.2).
  - Howard; (n² + 7n − 6)/2 iterations; O(n²) edges; weights O(n²).
  - HW ≤ n + 3 (READING from the sequence (1) and the policy definitions p.4): the edges into t_i are used for the last time at τ_i.
  - Mechanism: a deceleration lane delays the self-loop at t_{i+1}, which is improving but not appraisal-best.
  - RULED OUT by an arena optimum (READING; the same pattern as G_n).
- Hansen-Miltersen-Zwick: no lower bound in [HMZ] itself. §7 p.11 cites Friedmann for undiscounted / γ-in-input. Hansen's thesis
  §6.4 (linear-in-m tightness, cited by [Sch] p.4) is NOT OPENED.
- Answer to the brief's question (READING).
  - Yes: the exponential windows of every LOCALLY-optimizing / greedy family need an improving-but-not-chosen closure, which ARENA-MAX
    rules out.
  - No: the one family built against an arena-optimum rule (H_n) keeps an exponential window by Ξ-blocked closures, which ARENA-MAX
    does not touch.
  - So ARENA-MAX alone cannot prove ELIM-WIN. Whatever does must use S4a's fixed τ, or N5's τ-steps, or a count of blocked late
    adoptions (R*, FW-R*).

## 4. (c) Contraction for "best response against a fixed opponent" rules
### 4.1 Lemma C-DISC (PROVED, L-LIT; discounted shadow, not N5 itself)
- Setting. A γ-discounted one-player game G_τ (Even maximizes, Odd fixed to τ). T is the Bellman operator over all Even edges and W* is
  its fixed point, Even's optimum against τ. H_t is any arena containing σ_t, T_H is Bellman restricted to H_t, and σ_{t+1} is an optimum
  of H_t (S4a-shadow).
- Hypothesis (GREEDY-IN): at every Even v, H_t contains an edge maximizing r(v) + γW_t(w).
- Statement: ‖W* − W_{t+1}‖∞ ≤ γ‖W* − W_t‖∞.
- Proof.
  - W_t ≤ W_{t+1}, since σ_t is a strategy of H_t.
  - W_{t+1} = T_H W_{t+1} ≥ T_H W_t = T W_t, by monotonicity and GREEDY-IN.
  - So 0 ≤ W* − W_{t+1} ≤ T W* − T W_t ≤ γ‖W* − W_t‖∞. □
- This is HMZ Lemma 5.3-5.5 with "Howard's step" replaced by "any arena optimum whose arena contains the greedy step".
- Without GREEDY-IN there is no contraction toward W*: the restricted fixed point is H_t's optimum, not W*.
- In N5, H_t is cut by Ξ (two-player), so GREEDY-IN fails exactly when the W-greedy edge is BLOCKED.
- Even with GREEDY-IN, the parity rate 1 − γ = n^−Θ(d) (§2.2) gives n^Θ(d) windows.

### 4.2 Lemma DZ-W (PROVED, L-LIT, conditional; transfer of [ZY] (7.2)-(7.6) to a W-run)
- Embedding. V := weight(P)·(2n + 2) ± ℓ, from si.py's Engine.key: injective ranks, signed powers of 2. It is additive along a path to
  a fixed W-cycle node and order-isomorphic to W on values with the same cycle node. I use it as an assumption-free embedding for one
  W-run.
- Hypotheses. (U): the W-cycles of σ_t (as edge sets) are the same for t ∈ [p, q]. (BR_K) BLOCK-RATIO_K: B_t ≤ K·A_t at every t with
  gap_t > 0, where:
  - A_t := max over (v, w) ∈ Iσ_t with λ(w) = λ(v) and v not on w's (σ_t, τ)-play, of V_t(w) − V_t(σ_t(v)). The pair is allowed and
    closes no new cycle.
  - B_t := max_v V_t(σ_q(v)) − V_t(σ_t(v));
  - gap_t := Σ_x (V_q(x) − V_t(x)).
- Statement: gap_{t+1} ≤ (1 − 1/(K n²))·gap_t, and HW_F(t) ≤ ⌈K n² ln(n²)⌉ + 1 at every t with gap_t > 0.
- Proof (following [ZY] with N5 in place of Dantzig).
  1. W_{t+1} ⊵ W_t on F (ARENA-MAX with ρ = σ_t), so V_{t+1} ≥ V_t.
  2. ARENA-MAX with ρ = σ_t[v → w] for the allowed pair (v, w) attaining A_t gives V_{t+1}(v) ≥ V_t(w) + r(v) = V_t(v) + A_t, because
     the switched strategy creates no new cycle (v is not on w's play) and keeps the cycle node. Then both sides of ARENA-MAX have
     cycle node λ(v), where V is order-isomorphic. So gap_{t+1} ≤ gap_t − A_t.
  3. [ZY] (7.2) with π_q's paths (< n edges, ending on shared cycles by (U)) gives gap_t ≤ n²·B_t ≤ K n²·A_t. Hence the contraction.
  4. [ZY] (7.5): the pair (s, σ_t(s)) maximizing V_q(s) − Q_q(s, σ_t(s)) carries ≥ gap_t/n². If σ_{t′}(s) = σ_t(s) with t′ > t, then
     gap_{t′} ≥ gap_t/n². That is impossible once (1 − 1/(Kn²))^{t′−t} < 1/n². □
- Counting (T58): the W-changing transitions of F then number at most (m_E + 1)(⌈K n² ln n²⌉ + 1). The W-flat ones (FL) are a suffix of
  each gap-0 stretch; FW-R* already counts them.
- The proof uses only ARENA-MAX, W-monotonicity and (U). The single place blocked edges enter is BR_K: B_t may sit on a blocked
  reference edge.

### 4.3 DATA: BLOCK-RATIO is exponential on fx, and the gap does not contract (T59-dz-check.py)
Instances: L-RED's fx_K_m regenerated as in T58 (l-red span/mkrw.py K m; free/obsx.py, ABOVE=a OWNER=0 BLK=2). fx_K8_m32 equals the pin
experiments/red/free/instances/fx_K8_m32.pg (sha1 e995709e…). switchbestexp from experiments/hard-families/pgsolver_port.py.

| instance | n | W-runs | max |F| | STEPV / GAPV / MONV (sanity, must be 0) | KMAX = max B/A | KBL (blocked) | HB (bits) | CMIN (min per-step contraction) | WINC | HW (T58) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| fx_K4_m16 | 130 | 1 | 76 | 0 / 0 / 0 | 256 | 256 | 8 | 1.3·10⁻⁴ | 76 | 17 |
| fx_K8_m16 | 186 | 1 | 152 | 0 / 0 / 0 | 65,536 | 65,536 | 16 | 4.3·10⁻⁷ | 152 | 17 |
| fx_K16_m16 | 298 | 1 | 304 | 0 / 0 / 0 | 4.29·10⁹ | 4.29·10⁹ | 32 | 5.0·10⁻¹² | 304 | 17 |
| fx_K8_m32 (= pin) | 250 | 1 | 280 | 0 / 0 / 0 | 65,536 | 65,536 | 16 | 2.7·10⁻⁷ | 280 | 33 |
| switchbestexp_4 | 110 | 2 | 31 | 0 / 0 / 0 | 1.8·10³ | 1.8·10³ | 11 | 2.7·10⁻⁵ | 20 | 1 |
| switchbestexp_6 | 160 | 2 | 44 | 0 / 0 / 0 | 7.9·10⁵ | 7.9·10⁵ | 19 | 4.1·10⁻⁸ | 31 | 2 |
| switchbestexp_8 | 210 | 2 | 57 | 0 / 0 / 0 | 5.0·10⁷ | 5.0·10⁷ | 26 | 5.0·10⁻¹⁰ | 43 | 3 |

- The three sanity checks are 0 everywhere. So Lemma DZ-W's step inequality (2) and [ZY]'s (7.2) hold on the data, and W is monotone.
- KMAX = KBL. The largest reference residual sits on a BLOCKED edge, and it is 2^(2K) times the best allowed residual on fx_K_m16.
  BLOCK-RATIO_K with K = poly(n) is FALSE on fx.
- WINC = |F| on fx: from the first state, the gap never falls by a factor n² before the last transition. Even a windowed (C) fails.
  The whole gap sits on the top-rank change that happens at the end.
- Yet HW = m + 1 (T58) and |F| is linear in K. The windows are short for a reason that is invisible to the gap.
- DEAD (route): "ELIM-WIN via a contraction of the end-referenced W-gap in the canonical embedding". Killed by fx_K16_m16 (KMAX 2^32,
  WINC = |F| = 304, HW 17).
  - Not killed: an embedding other than si.py's (another order-isomorphic additive embedding of the values that occur). OPEN. I do not
    expect it to help, because any such embedding must let the top rank dominate.
- Corpus (§4.4): the same script over the repo's instance directories.

### 4.4 Corpus run
- Scope: 892 .pg files under experiments/{red,si,n5-exhaustive,n5-box17,n5-box21,n5-box22,n5-epoch,friedmann-hn,new/instances}
  (.../instances/), each with its .start if present, 30 s timeout each. Run 2026-10-30 18:06Z-18:11Z (date -u), output scratchpad
  t59/corpus3.out.
  - 873 finished. 18 timed out (rc 124). 1 failed: experiments/si/instances/dlmm_ML_L6.pg, whose .start file the T58 reader cannot parse.
- Sanity: STEPV 0, GAPV 0, MONV 0 over 15,986 states with gap > 0 (660 games with a W-run of length ≥ 1). So Lemma DZ-W's step (2),
  [ZY]'s (7.2) and W-monotonicity hold on every measured state. ZERO_A (W-flat states with gap > 0): 24.
- BLOCK-RATIO: KMAX ≤ 1 on 476 of 659 games; KMAX > n² on 30.
  - Largest: fc14 (n 360, |F| 91) 1.3·10¹³ (HB 44); fc12 2.1·10¹¹; fc11 2.6·10¹⁰; fc9 4.0·10⁸; fc8 and dw_8 5.0·10⁷; obs_K12_m24 1.7·10⁷.
  - On the fc family it grows by about 2^3.4 per step of the parameter. Blocked reference residuals occur at 6,197 of the 15,986 states.
- WINC = |F| on 502 games. On short runs this is trivial (the run ends before the gap can fall by n²), so it is not evidence by itself.
  The evidence is the fx and fc rows.
- Reading: on most of the corpus BLOCK-RATIO holds with K ≤ 1. Where W-runs are long relative to n (fx, fc, obs), the blocked residual
  is exponentially larger. That is the regime ELIM-WIN must cover.

## 5. (d) Table
| source (opened) | setting / rule | window or elimination statement | (R) reference | (P) flux window | (C) supplied by | undiscounted? | what it gives N5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [ZY] Thm 7.1, (7.2)-(7.6) | det. avg-reward MDP, Dantzig single switch | a pair excluded after O(N² log N) bias updates with unchanged cycles; O(N³M² log² N) total | last policy of the no-new-cycle stretch | path length < N | largest residual over ALL pairs: 1 − 1/N² | YES, strongly poly | Lemma DZ-W (conditional on BR_K); BR_K false on fx (2^(2K)) |
| [ZY] Thm 6.1 | det. avg-reward MDP, Howard | none: exp(Ω(N)), M ≤ 4N (HZ conjecture false) | – | – | none | YES | HW-LB: exponential window; cycle-type, blocked by R47 |
| [ZY] Thm 7.2; [ZP] Thm 2.3; [ACR] p.2 | det. MDP / MPG, Howard or VI | O(N³2^b); O(n³mW) | – | – | VI domination (HMZ L5.3), pseudo-poly | YES | n^Θ(d) for parity (READING) |
| [MK] Thm 1.2 | DMDP, Howard | ≤ nk·u·e^u, u = O(√(nb log nb) + b) | threshold γ_Q | – | Ye/Scherrer γ-bound at γ_Q; root separation | via γ_Q | subexponential at best; one-player |
| [Sch] Lemma 8; p.6 | det. MDP, Howard | new cycle within n iterations; on [HZ] contraction 1 − (2/n)^k | – | – | none (contraction decays) | YES (γ-free) | analogue of R17 (one-player λ-phase ≤ n − 1) |
| [HMZ] Lemma 5.3-5.5, 6.4 | 2TBSG, Howard vs best response | every σ^k has an action absent after k + L, L = log_{1/γ} n²/(1−γ) | optimal profile | n/(1−γ) | γ via VI domination | NO | Lemma C-DISC (shadow); needs GREEDY-IN, which fails at blocked edges; parity rate n^Θ(d) |
| [F09] / [F11] G_n | parity, locally optimizing | none: 13·2^n − 9 | – | – | – | – | HW exp; mechanism ruled out by ARENA-MAX (R140) |
| [F11] H_n, Thm 8.4 | parity, I^glo (arena optimum) | none: ≥ 2^n | – | – | – | – | HW exp; stubborn cycles = Ξ-blocked closures, NOT ruled out by ARENA-MAX; N5: HW ≤ 3 on N = 4-8 (DATA) |
| [Fe] Thm 17/18; [Hol] Ch. 2 | MDP, Howard | none: 2^Ω(n) | – | – | – | – | HW exp; hidden-appeal lane, ruled out by an arena optimum (READING) |
| [ACR] Thm 3.2 | DMDP, Howard | (n² + 7n − 6)/2 iterations | – | – | – | – | HW ≤ n + 3 (READING); lane, ruled out by an arena optimum |
| [HZ] slides | DMDP, Howard | m − n + 1 iterations; conjecture ≤ m (now false) | – | – | – | – | none |

## DONE / FINDINGS / NEEDS
- DONE: this note; docs/lit/T59-dz-check.py; notes/L-LIT.md (sources, resume point).
- FINDINGS:
  1. Undiscounted polynomial windows exist only for coordinated single-switch rules on deterministic MDPs ([ZY] Thm 7.1, (7.2)-(7.6);
     contraction 1 − 1/N² from "largest residual over all pairs"). Howard has none ([ZY] Thm 6.1; [Sch] p.6). The HZ ≤ m conjecture is
     false ([ZY] p.2).
  2. PROVED (L-LIT) HW-LB: HW ≥ T/(m₀ + 1) for any run. Every exponential family has an exponential window.
  3. ARENA-MAX rules out the lane mechanisms (G_n, Fearnley, ACR) but not Friedmann's H_n. H_n beats an arena-optimum rule (I^glo,
     [F11] p.7) with stubborn cycles, i.e. Ξ-blocked closures (§8.2). ARENA-MAX alone cannot give ELIM-WIN. DATA: N5 on switchbestexp
     N = 4-8 has HW ≤ 3.
  4. PROVED (L-LIT): C-DISC (discounted shadow, needs GREEDY-IN) and DZ-W (conditional on BLOCK-RATIO_K). Both fail exactly at blocked
     edges.
  5. DEAD (route): contraction of the end-referenced W-gap. On fx_K_m16 BLOCK-RATIO is 2^(2K) and WINC = |F| while HW = 17. ELIM-WIN
     needs a combinatorial count (GP*-type), not a potential.
- NEEDS: none from the owner. Optional library access: HKZ SODA 2014; Hansen-Zwick ISAAC 2010; Hansen PhD 2012.
