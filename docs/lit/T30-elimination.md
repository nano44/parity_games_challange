# T30: "every k iterations eliminate an action" lemmas in policy iteration and simplex, against N5's (ELIM-n) (L-LIT, 2026-10-24)

Asked by the Lead at 14:01Z (date -u), under D18.
- **Target.** L-SI's CONJECTURE (ELIM-n) (docs/si/N5-OR-lens.md §5): every n consecutive transitions of a joint λ-phase contain an
  eliminating one.
- **What L-SI proved.**
  - (ELIM-n) ⇒ G-N5-TIME (§5 Proposition).
  - The HMZ 6.1-6.2 half in VJ valuations (§2, Lemmas U, E1-E6).
- **The correspondence used throughout** (N5-OR-lens §1):
  - action = Even edge;
  - potential = gap level g_k(v) = lev(T(v), Ξ_k(v));
  - reduced cost = slack level s(x, z) = lev(T(x), x ⊕ T(z));
  - levels are ultrametric (Lemma U).
- **Conventions.** No runs, no contact. Labels: PROVED (in the source, or here and elementary), CONJECTURE, READING, DATA (the lanes'
  data). PDF pages. sha256 values are in notes/L-LIT.md.

## 0. Result in one paragraph
- Every published elimination lemma found rests on one of two pillars:
  - **(A)** an ADDITIVE potential that contracts by a fixed factor:
    - HMZ Lemma 6.4 (γ);
    - Post-Ye Lemma 3.5-3.6 ((1 − 1/n) per new cycle);
    - Kitahara-Mizuno Lemma 3.2 / Thm 3.2 (ratio γ/δ of basic-solution entries);
    - Mei-Sun-Ye Lemma 6, 11;
    - Zhong-Ye Thm 7.1, via Post-Ye.
  - **(B)** a structural restriction that makes cycle creation monotone progress: one player (Post-Ye, Zhong-Ye, Scherrer Lemma 8);
    or no cycle containing actions of both players (Mei-Sun-Ye's "forward games").
- N5's open case violates both.
  - (A) has no analogue for VJ gap levels. L-SI Lemma D and §3, PROVED/DATA: levels are ultrametric, and only n(n + 1) level
    changes fit in a phase (E6). The flat transitions carry no additive progress.
  - (B): o-cyclic 𝒞^1O games have mixed-owner cycles through o.
- **New literature fact (19 Oct 2026; NOT in the fleet before T30):** Mei, arXiv 2610.27386. Simple strategy iteration with
  Dantzig's rule is exponential on turn-based deterministic games. The mechanism is exactly the obstruction: "make Player 1 create a
  mixed-player cycle and Player 2 cancel it through the optimal counter strategy at every iteration" (p.2). That is N5's σ̄-lap /
  trust mechanism in Dantzig form.
- **Structural match (READING, near-definitional):**
  - o-acyclic 𝒞^1O, with forced Odd vertices relabelled Even, is a turn-based deterministic forward game. There Mei-Sun-Ye prove
    strong polynomiality for Dantzig SSI, and R18 proves N5 polynomial (conditional on (P)).
  - o-cyclic 𝒞^1O is outside every theorem, and is where Mei's counterexample lives.
- Recommendation:
  - port Mei's G_h / Ĝ_h to parity and run N5 on it (L-RED). It is the first published family built on the exact mechanism;
  - the window shape a killer of (ELIM-n) must have is Fearnley's deceleration-lane reset (§7).

## 1. Hansen-Miltersen-Zwick, arXiv 1008.0530 v1 (sha256 f53a6b51…)
- **Lemma.** **Lemma 6.4 (p.11), PROVED:** with L = log_{1/γ}(n²/(1−γ)), "every strategy σ^k contains an action that does not appear
  in any strategy σ^ℓ, where k + L < ℓ ≤ N". It uses Lemmas 6.1-6.3 (reduced cost certifies a gap) and the contraction (Lemmas 4.8
  / 5.5).
- **Hypotheses.** Discounted 2TBSG; Howard (switch-all) strategy iteration; values a function of the profile; a γ-contraction.
- **N5.**
  - The 6.1-6.2 half is satisfied: L-SI E2-E5, PROVED.
  - The contraction is violated. L-SI Lemma D (PROVED) plus switchallexp (DATA): lexicographic value iteration is itself
    exponentially slow in one phase; Scherrer §2 (the 1/(1−γ) factor is irremovable for Howard).
  - HMZ's specific mechanism ("the argmax-slack action of σ_k is gone within L") is FALSE for N5 as DATA: returns_rt48, 77 of 78
    transitions (N5-OR-lens §4.1).
- **Transfer.** None (PROVED absence of the contraction ingredient, by L-SI).

## 2. Post-Ye, arXiv 1208.5083 v2 (sha256 c51876eb…)
- **Lemmas.**
  - **Lemma 3.6 (p.8), PROVED:** "after O(n log n) iterations in which a new cycle is created, some action in π is either
    eliminated from cycles for the remainder of the algorithm or entirely eliminated from policies".
  - **Lemma 3.5 (p.8):** a cycle-creating pivot shrinks (r*)ᵀx by a factor (1 − 1/n).
  - **Lemma 3.4:** no new cycle for O(n²m log n) iterations ⇒ terminate.
  - **Thm 3.7 (p.9):** O(n³m² log² n), for any uniform discount.
- **Hypotheses.** Deterministic ONE-player MDP; highest-gain single-switch simplex; an LP with flux x^π, where 1 ≤ x_a ≤ n on paths
  and 1/(1−γ) ≤ x_a ≤ n/(1−γ) on cycles; reduced costs r* ≤ 0.
- **N5 against the hypotheses.**
  - **Satisfied.** Determinism. An analogue of "pigeonhole: some action carries ≥ 1/n of the total gap": L-SI E5 is its ultrametric
    form, gap ≤ the largest slack on the play.
  - **Violated: one player.** N5's honest valuation uses Odd's best reply σ̄.
  - **Violated: an additive potential.** (r*)ᵀx sums reduced cost × flux. The ultrametric max has no factor (1 − 1/n), and a
    cycle-creating step in N5 can be level-flat.
- **Transfer.**
  - CONJECTURE (weak form): on one-player N5 phases, Lemma 3.6's conclusion holds with "new cycle" read as "λ-change". This is
    subsumed by R17 (n − 1 value-changing steps per phase), which is stronger.
  - No transfer for two players.

## 3. Mei-Sun-Ye, arXiv 2606.29568 v1 (sha256 8bbb42f6…), and Mei, arXiv 2610.27386 v1 (sha256 5b3265d3…)
**Mei-Sun-Ye.**
- **Definition 7 (p.6):** a TBDFG is a turn-based deterministic game whose graph "contains no directed cycle involving actions from
  both players".
- **Lemma 11 (p.15), PROVED:** on a TBDFG, after O(n log n) Player-1 cycle-creating rounds, some action of π ∩ A₁ is eliminated
  from cycles or from policies for the remainder.
- **Lemma 10 (p.15):** terminate or a new Player-1 cycle within O(n²m log n).
- **Thm 1 (p.16):** simple strategy iteration (Dantzig pivot for Player 1, exact best reply for Player 2) is O(n⁶m⁴ log⁴ n),
  strongly polynomial.

**Mei 2610.27386.**
- **Thm 1 (p.11), PROVED:** on G_h (n = 4h + 2, m = 8h + 2, unrestricted costs, discounted), the same method performs exactly
  2^h − 1 iterations.
- **Thm 4 (p.20):** the mean-payoff Dantzig counterpart on Ĝ_h also performs 2^h − 1 iterations (unrestricted costs).
- **Thm 5 (p.21):** with unit weights, it is O(n⁵).
- p.5 (§3), with the same point on p.2: "a mixed-player cycle created by a Player 1 pivot may be canceled by Player 2's optimal counter strategy ...
  This prevents the cycle-creation arguments used for deterministic MDPs and deterministic forward games from extending directly
  to general TBDGs."

**N5.**
- READING, near-definitional: relabelling a forced Odd vertex as Even changes no play. After that, 𝒞^1O is a TBDG with ONE
  Player-2 choice vertex o. It is a TBDFG iff no cycle uses an action of o together with an Even choice, i.e. iff o is on no cycle
  with Even choices. o-acyclic implies this.
- So R18 (N5 polynomial on o-acyclic 𝒞^1O) sits inside Mei-Sun-Ye's forward class.
- The open o-cyclic case is the non-forward case, and Mei's mechanism is the one that breaks Lemma 11 there.
- Parity weights (−n)^p are "unrestricted costs" in Mei's sense: exponential magnitudes with a lexicographic scale separation. Mei
  uses exactly such a separation: "Costs on actions to the next level determine the ordering of state values, while costs on
  return actions determine Dantzig's pivot selection" (p.5).
- Mei's unit-weight case (Thm 5, polynomial) does not cover parity.

**Transfer.**
- CONJECTURE (kill direction): a parity encoding of G_h or Ĝ_h (priorities chosen so that VJ order reproduces Mei's two cost
  scales) gives an N5 run with long non-eliminating windows.
- Obstacle: N5 is not Dantzig SSI. Its Even step is the arena optimum over the gate, and N5 is symmetric. So Mei's unique-pivot
  argument (Thm 1 (ii)) does not apply; the run must be checked.
- CONJECTURE (proof direction): Mei-Sun-Ye Lemma 11's cycle-elimination step holds for N5 on o-acyclic 𝒞^1O. This is redundant
  given R18.

## 4. Zhong-Ye, arXiv 2609.40147 v2 (sha256 dafeb818…)
- **Theorems, PROVED.**
  - **Thm 2.1 (p.3):** Howard's PI takes exp(Ω(N)) iterations on deterministic discounted MDPs with two actions per state. Thm
    2.2-2.3: exp(Ω(N^(1/4))) with small integer rewards.
  - **Thm 7.1 (p.31):** "On any deterministic average-reward MDP, Dantzig's rule (5.3) finds an optimal policy within
    O(N³M² log²(2N)) iterations from every initial policy".
  - Proof structure: gain updates ≤ N(N + #cycle creations) (eq. (7.1)), plus "the two action-elimination arguments of Post and
    Ye" for bias updates with unchanged cycles.
- **Hypotheses.** One player; undiscounted (average reward), so γ-free; a single coordinated switch (largest improvement).
- **N5.**
  - The split matches exactly (READING): gain ↔ cycle node (λ), bias ↔ (P, ℓ).
  - Eq. (7.1)'s gain count is N5's Lemma Φ.
  - The bias-update elimination is the in-phase part, which R17 already bounds on one-player games.
  - Violated: one player.
  - Lesson (PROVED in source): simultaneous switching (Howard) is exponential even on one-player deterministic games, while
    coordinated single-action selection is polynomial. N5's step is a coordinated arena optimum, consistent with R17.
- **Transfer.** The one-player part is subsumed by R17. None for two players.

## 5. Kitahara-Mizuno, arXiv 1101.3820 v1 (sha256 b5b02b5d…)
- **Lemma and theorem, PROVED.**
  - **Lemma 3.2 (p.6):** if x^t is not optimal, some basic j̄ has s*_j̄ ≥ (cᵀx^t − z*)/(m x^t_j̄), and then every later iterate has
    x^k_j̄ ≤ m(cᵀx^k − z*)/(cᵀx^t − z*) · x^t_j̄. This is the elimination.
  - **Thm 3.2 (p.8):** Dantzig / best improvement meets ≤ n⌈m(γ/δ) log(mγ/δ)⌉ distinct BFS, with γ/δ the ratio of the largest
    to the smallest positive BFS entry.
- **Hypotheses.** An LP. A bounded ratio γ/δ. Single pivots.
- **N5.**
  - No LP whose basic solutions are N5's strategies is known.
  - Via the discounted reduction, the flux ratio is n/(1−γ) = n^Θ(d) (BARRIERS B21, DE25). That is exponential.
  - In the ultrametric reading, a "ratio of levels" is meaningless.
- **Transfer.** None. The obstacle is bit size / ratio.

## 6. Scherrer, arXiv 1306.0386 (sha256 391b6481…): the n-window lemma
- **Lemma 8 (p.6), PROVED:** "If the MDP is deterministic, after at most n iterations, either Howard's PI finishes or a new cycle
  appears."
- Lemma 9 (structural τ_t): the same with polynomially many iterations.
- **N5.**
  - Lemma 8 is the closest published statement to the SHAPE of (ELIM-n): a window of length n in which a structural event must
    occur.
  - Its one-player N5 analogue is R17 Theorem PH (a phase has ≤ n − 1 value-changing steps).
  - For two players the analogue "n transitions ⇒ λ-change or finish" is FALSE (DATA: box 21 §3.2, fts_ph16, 22 value-changing
    steps in a phase at n = 16).
  - (ELIM-n) is the weaker event ("some edge retired") that the data still support (N5-OR-lens §4.2: longest non-eliminating run
    ≤ 17 at n ≤ 64).
- **Transfer.** None for two players.

## 7. Fearnley, arXiv 1003.3418 v1 (sha256 0964f029…), and Melekopoglou-Condon: what a long non-eliminating window looks like
**Fearnley, the deceleration lane.**
- **Proposition 8 and the reset paragraph (p.8), PROVED:** each b_i follows the lane, switching (b_i, d_k) "in the iteration
  immediately after it switches (d_k, d_{k−1})".
- When Val(x) > Val(y) + 6n + 1, policy iteration switches (d_k, x) for all k and (b_i, x), and later back to (d_k, y), (b_i, y).
- **Every lane edge abandoned before a reset is reused after it.** Inside one counter period no edge is eliminated, and the period
  grows with the bit index.
- Thm 17-18 (p.12): exponential for total and average reward.
- This is the anatomy of the switch-all control in N5-OR-lens §4.2, where the non-eliminating runs double on switchallexp
  (Friedmann's lane is the same device).

**Melekopoglou-Condon (1994; NOT opened; described in Christ-Yannakakis arXiv 2212.00083 v1 §5, p.30, sha256 ab6b5251…).**
- Reachability MDPs with random vertices, two actions per min-vertex.
- Under simple / topological / difference rules the policy string walks a binary counter, so every action is reused: zero
  permanent eliminations.
- Needs stochastic vertices. N5 is deterministic.

**READING for (ELIM-n).**
- A counterexample must contain a reset gadget that re-enables abandoned edges within n transitions, repeatedly, inside ONE joint
  λ-phase.
- In N5, returns exist: fts_g43 has 71 returns to T-tight edges (N5-OR-lens §4.2). But they are interleaved with eliminations.
- Mei's G_h (§3) supplies the reset through Player 2's cancellation of mixed cycles, which is the one ingredient Fearnley's
  one-player lane cannot use against an exact best reply.

## 8. Not opened
- Hansen-Kaplan-Zwick, SODA 2014, DOI 10.1137/1.9781611973402.63: the SIAM link returned HTML, paywalled. Dantzig: O(mn log n)
  for shortest paths and O(m²n² log² n) for deterministic MDPs, per the abstract text in search results only.
- Madani-Thorup-Zwick, TALG 6(2) 2010, DOI 10.1145/1721837.1721849: paywalled. It gives an O(mn) algorithm, not a PI analysis.
- Karczmarz arXiv 2110.15070 (sha256 693b744f…): downloaded, abstract only; algorithmic, no PI.
- Mukherjee-Kalyanakrishnan (cited by Zhong-Ye p.2) and Kitahara-Mizuno 1101.3821 (the arXiv link returned HTML).

## 9. Ranking for the Lead (expected value for (ELIM-n))
1. **Kill direction.** Port Mei 2610.27386 G_h / Ĝ_h to parity (L-RED). It is the only published family whose mechanism, a
   mixed-owner cycle cancelled by the best reply, is N5's open case. CONJECTURE that it produces long non-eliminating windows.
2. **Proof direction.** A Mei-Sun-Ye Lemma 11 analogue on o-cyclic 𝒞^1O needs a replacement for "cycle creation = progress" when the
   best reply cancels the cycle. Candidate fact, CONJECTURE (ELIM-CANCEL): when σ̄(o) cancels a mixed cycle created by an Even
   switch, the Even edge that closed it is retired in the phase, or o's exit is retired. This is checkable on data (L-SI's elim.py,
   with cancellations tagged).
3. Everything else in §1, §2, §4-§6 is subsumed by R17 (one player) or blocked by the additive-potential pillar (A).

No running-time claim is made (D1). G-N5-TIME stays OPEN.
