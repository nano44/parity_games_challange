# T50: the quasi-polynomial side: Koh-Loho universal-tree SI, parametric dimension (coherence) of a run, and DLM's locks vs the one-sided F
L-LIT successor 4 (Opus 5.5), D18. Lead's brief 2026-10-29 16:54Z (T50 (1)-(3)). Written 2026-10-29 from 16:58Z (date -u). Working note,
unrefereed, not a TARGET.md claim. CONJECTURE SF-POLY and CONJECTURE SF-QP stay OPEN. Symbols as in docs/lit/T48-sbc-neighbours.md,
T49-tropical-simplex.md and P-N5-SF §0. Labels: PROVED-in-source / PROVED (L-LIT, unrefereed) / READING / CONJECTURE / OPEN / DEAD / DATA.
All sources here were opened by me (no subagents). sha256 and pages are in the notebook; page numbers are PDF pages unless "printed".

## Summary
- (1) Koh-Loho: universal-tree labels make the improver's run quasi-polynomial for ANY pivot rule. The reason is a potential: labels in
  the finite lattice L(T)^V are forced to increase, n·|L(T)| steps in all (p.3). The opponent's best reply is never counted; it changes
  at most once per iteration.
  - The price is that strategies may repeat (Ohlmann's impossibility is sidestepped, not refuted).
  - READING: an "N5-SF with tree labels" would be quasi-polynomial by the same potential. The open SF-POLY question is exactly whether
    VJ00's Ξ (2^n values in its P component, T48 / L-NEW (M4)) can be replaced by such a lattice without losing F.
- (2) "Parametric dimension 1" of a run has a name in the literature: COHERENT (Billera-Sturmfels 1992, via Black-Xue 2607.11628 p.2).
  - Black-Xue Thm 1.1 (2026): there are polytopes on which EVERY coherent monotone path is exponentially long. So low parametric dimension
    alone gives nothing on general polytopes.
  - For path polytopes, d parameters give n^O(d log n) (Chillara-Gajjar-Raja Thm 2-4).
  - F's runs are not coherent on the joint-play polytope (SEGRET, T48). They need at least PIECES ≈ SBC/2 coherent pieces (T49).
  - No literature found bounds the parametric dimension of an iterative algorithm's run beyond d = 1.
- (3) DLM's mechanism cannot be adapted to F (PROVED (L-LIT) from DECOUPLE + Friedmann thesis Lemma 4.2).
  - DLM's locks work through Odd's CURRENT τ (Even switches only along τ̄(τ)). F's arena and opponent are functions of σ alone.
  - DLM's "for every rule" has no one-sided analogue: one-sided SI always has a rule with ≤ |V| iterations (Friedmann thesis Lemma 4.2,
    printed p.74; DLM p.2 contrast it with SSI). Any super-polynomial lower bound for F must be F-specific, like Friedmann's families.

## 1. (1) Koh-Loho, «Beyond value iteration for parity games: strategy iteration with universal trees»
Source: arXiv 2108.13338 (LMCS 21(2:24), 2025; this file v5 per the LMCS header), sha256 21ee0e4336252f7e. Opened 2026-10-29.
- PROVED-in-source / stated.
  - Framework (p.2-3): «one fixes a suitable value domain V and associates a valuation µ : V → V to each strategy for Odd. The valuation
    of a strategy τ can be thought of as an evaluation of the best counterstrategy for Even … a fixed point of a set of operators
    associated with the 1-player game (Gτ, π) for Even.»
  - Contribution (p.3): «After pivoting to a strategy τ′ in an iteration, we update the current node labeling µ to the least fixed point
    of (Gτ′, π) that is pointwise at least µ. In other words, we force µ to increase … this means that we may encounter a strategy more
    than once». They cite [Ohl21]: «a valuation that is fit for strategy iteration cannot be defined using L(T) for the aforementioned
    trees».
  - Algorithm 1 (p.9): «while ∃ an admissible arc in G with respect to µ do: Pivot to a strategy τ′ by selecting admissible arc(s)
    ▷ requires a pivot rule; τ ← τ′, µ ← µ↑Gτ′». Invariants: «every arc in Gτ is either tight (usable by Even in her counterstrategy σ)
    or violated».
  - Thm 3.1 (p.9): correctness (the pointwise minimal feasible labeling); «The node labeling µ is monotone increasing in every iteration.»
  - p.3: «The total number of strategy iterations is trivially bounded by n|L(T)|, the same bound for the progress measure algorithm …
    Identifying a pivot rule that may provide strictly improved (and possibly even polynomial) running time is left for future research.»
  - Per-iteration cost: O(d(m + n log n)) (perfect tree, Thm 4.5); O(mn² log n log d) (JL17 tree); O(mn² log³ n log d) (Strahler tree)
    (abstract, p.4). The motivation is tropical (Appendix A).
- READING (mechanism and the opponent).
  - Roles are mirrored w.r.t. N5-SF: Odd improves, Even best-responds through tight arcs.
  - The iteration bound uses no rule property and no opponent property. It is the height of a monotone potential: Σ_v rank of µ(v) in
    L(T), at most n|L(T)|, quasi-polynomial for JL17 / DJT20 trees.
  - The opponent's best reply changes at most once per iteration, hence at most n|L(T)| times, again by the potential alone.
  - The price: µ is a least fixed point ≥ the previous µ, not a function of τ, so τ may repeat. This is the step that escapes Ohlmann's
    impossibility.
- READING (what it means for SF-POLY).
  - F's potential is Ξ (VJ00), monotone (MONO-XI). Its P component has up to 2^n values, so "potential height" gives only an exponential
    bound. L-NEW's (M4) is the data: 290 distinct Ξ values at one vertex, n = 260.
  - Two design routes, both CONJECTURE / design hints for L-NEW, not results:
    - (KL-SF) Run F's step with tree labels: Even's one-player optimum in the improving arena (switch-best), evaluated by least fixed points
      in L(T). Termination and the quasi-polynomial bound then come free from Koh-Loho's potential. Correctness needs their Prop. 2.5 /
      Thm 3.1 framework with Even and Odd swapped.
    - (POLY-POT) A polynomial-height lattice with the same "forced increase" property. Czerwiński et al. (CDFJLP, opened 2026-10-14) prove
      universal trees have quasi-polynomial size, so a lattice of the L(T) kind cannot be polynomial. A polynomial-height potential must
      therefore be of a different kind (not a universal-tree label). This is the same barrier the fleet records for progress measures.

## 2. (2) Parametric dimension of a run; Chillara-Gajjar-Raja; the obstruction for F
### 2.1 Sources (PROVED-in-source)
- Chillara-Gajjar-Raja, «Shortest Paths with Linear Edge Weights», arXiv 2607.21055 v1 (23 Jul 2026), sha256 32ee94e1aab6eecd.
  - Definition 1 (p.3-4): for a directed graph with special vertices s, t and wt(e) = a_{e,1}λ_1 + … + a_{e,d}λ_d + a_{e,d+1} (a_{e,i} ∈ ℝ),
    MSPC(G) is «a minimum-sized subset of [the s-t paths] such that for every x ∈ ℝ^d, there is a path P ∈ [it] which is a shortest path
    in G at λ = x».
  - Theorem 2: «Let G = (V, E) be an n-vertex directed acyclic graph with edge weights of the form a_{e,1}λ_1 + … + a_{e,d+1}. Then,
    |MSPC(G)| ∈ n^O(d log n).»
  - Theorem 3: the same for «an n-vertex directed graph without negative-weight cycles».
  - Theorem 4: the same for undirected graphs «without negative-weight edges».
  - Abstract: the matching n^Ω(d log n) «can be obtained by trivially extending existing lower bound constructions for d = 1». History in
    the abstract: Carstensen (d = 1), Gajjar-Radhakrishnan (d = 2), Barth-Funke-Proissl (n^O_d(log^d n)).
  - Assumptions, exactly: affine weights in d real parameters, one fixed s-t pair, the whole of ℝ^d. The graph class is per theorem
    (DAG / no negative cycles / undirected non-negative). The count is of paths, not trees.
- Black-Xue, «Any proof of polynomial Hirsch must be completely incoherent», arXiv 2607.11628 v1 (13 Jul 2026), sha256 26ed159192e9e6e6.
  - p.2: «the coherent monotone paths are precisely those that arise from a parametric linear optimization problem … max((w + λc)ᵀx) s.t.
    Ax ≤ b … A monotone path is called coherent if it arises in this way.»
  - Thm 1.1: «For each d ≥ 3, there exists a d + 1 dimensional polytope P with (2d + 1)(d + 1) + 1 facets and a linear objective function
    such that any coherent monotone path on P with respect to that objective function is of length at least 2^(d−1) − 1.»
  - Cor. 1.5: «… for any choice of c linearly independent from w the parametric optimization problem w + λc has at least 2^(d−1) many
    solutions.»
  - Cor. 1.3: the same for semi-random shadows.
  - They note (p.2) that an exponential coherent path already follows from Zadeh 1973 (network flows), Murty, Goldfarb and Amenta-Ziegler.
- Black-De Loera-Lütjeharms-Sanyal, arXiv 2201.05134 v1 (opened by my T49 subagent, sha256 aa1e5e36f30e5572).
  - p.1: «The vertices of monotone path polytopes are in bijection to special monotone paths, called coherent» (Billera-Sturmfels,
    Ann. Math. 135 (1992), NOT OPENED).
  - The max-slope pivot rule generalises shadow vertex. Its pivot-rule polytopes refine monotone path polytopes (abstract). No polynomial
    bound.
- Search (arXiv API, 2026-10-29): abs:"coherent monotone path"; abs:"coherent" AND abs:"simplex method"; abs:"strategy improvement" AND
  abs:parametric; abs:"policy iteration" AND abs:"shadow"; abs:"parametric complexity" AND abs:algorithm. The relevant hits are the two
  above. No paper bounds the parametric dimension (d ≥ 2) of the run of an iterative algorithm, or defines it.

### 2.2 The obstruction for F (PROVED (L-LIT) + DATA)
- Definition used here (READING). A run has parametric dimension ≤ d on a polytope P if there is an affine map ℝ^d → objectives under
  which every solution of the run is optimal somewhere. A run is coherent in Billera-Sturmfels' sense if moreover d = 1 and the run is
  traced in λ-order.
- PROVED (L-LIT, T48 §1.4). A run of joint plays with a segment return (SEGRET > 0) is not coherent on the joint-play (path) polytope.
  - Witness switchbestexp_1, pair (15, 5).
  - Minimum number of coherent pieces ≥ PIECES (T49 §4): switchbestexp N = 1..6 → 2, 4, 9, 16, 24, 29 (SBC 1, 4, 11, 26, 49, 56).
- READING (the exact obstruction). F's run is a monotone walk in Even's improvement order on a product of per-vertex choices. Even's
  multi-switch leaps revisit sub-paths (an Even vertex returns to an edge with the same continuation), and a coherent run never revisits
  a strictly optimal sub-path. More dimensions do not obviously help:
  - with d ≥ 2 a curve may re-enter a cone, so PIECES gives no lower bound on d;
  - even d = 1 (coherent) paths can be exponential on general polytopes (Black-Xue);
  - only on the path / flow polytope does small d give n^O(d log n) (Chillara-Gajjar-Raja).
  So a route "SF-QP from small parametric dimension" would need BOTH (i) F's runs having d = O(1) on the joint-play polytope (OPEN; no
  test available, since counting shadow vertices is NP-hard, Disser-Skutella Cor. 4), AND (ii) the overlay count over n vertices
  (crude n^O(d² log n), T49 §4, READING).
- DEAD for d = 1 (coherent): SEGRET > 0 from switchbestexp_1.

## 3. (3) van Dijk-Loho-Maat (CSL 2024) and the one-sided F
Source: arXiv 2309.02223 v1 (= LIPIcs.CSL.2024.24), sha256 10e6794d82aba465, re-opened 2026-10-29. Fleet background: T43
(docs/lit/T43-dlm-coupled-counter.md: N5 sets every level's final edge in iteration 1).
- PROVED-in-source.
  - Thm 1 (p.2): «In the worst case, the number of iterations of symmetric strategy improvement in parity games, mean payoff games and
    discounted payoff games is exponential in the number of nodes and edges in the graph independently of the improvement rule.»
  - p.2: «This is different from regular strategy improvement, where the existence of a (theoretical) improvement rule for which the
    algorithm terminates in a linear number of iterations is guaranteed, see [15, Lemma 4.2].»
  - p.3: «the two players are both distracted by the other player's strategy. The key insight here is that the optimal counterstrategy
    to a bad strategy can also be a bad strategy itself. Hence restricting to moves from the optimal counterstrategy prevents them from
    making the crucial switches».
  - p.3: «It requires the algorithm to solve a subgame first, and then after the important switches are made, solve the same subgame
    again».
  - SSI (Algorithm 2, p.8): «It uses an optimal counterstrategy τ̄ to τ to select improving moves for σ».
  - Thm 13: the same for generalized SSI.
- PROVED-in-source, [15] = Friedmann PhD thesis (LMU 2011, sha256 68748f5388a94151), Lemma 4.2 (printed p.74): «Let G be an infinitary
  payoff game. There is an improvement rule SWITCH-LIN s.t. policy iteration requires at most |V| many iterations.» (SWITCH-LIN switches
  each v to σ*(v) whenever (v, σ*(v)) is improving.)
- PROVED (L-LIT, unrefereed; from DECOUPLE, P-N5-SF §2).
  - (a) No DLM lock acts on F. In SSI, Even's candidate set at σ is Iσ ∩ τ̄(τ), which depends on Odd's current τ. In N5-SF, Even's
    arena (Iσ) and opponent (σ̄(σ)) are functions of σ alone, and the distinct-σ sequence is the F-orbit of σ_0 for every τ_0. So any
    family whose slowness comes from τ gating σ, which is DLM's «both distracted by the other player's strategy», has no effect on F's
    σ-run. The mirror holds for τ.
  - (b) No "every rule" lower bound exists for one-sided SI. By Lemma 4.2, from every σ_0 some improvement rule reaches the optimum in
    ≤ |V| steps; DLM themselves state the contrast. A lower bound for F must therefore be rule-specific: it must use F's switch-best
    choice against the stale σ̄ (T46 §1 (a)), as Friedmann's families do for their rules.
- READING (what of DLM can still be used).
  - DLM's self-similar recursion («solve a subgame first, then … solve the same subgame again») is a generic counter skeleton.
  - DLM's distraction («the optimal counterstrategy to a bad strategy can also be a bad strategy itself») has a one-sided analogue only
    inside F's own frame: Even's choice is evaluated against σ̄(σ), the best reply to Even's OLD strategy. A bad old σ makes σ̄(σ) a
    misleading frame for the arena optimum. This is the stale-frame gap of T46 §1 (a) (val(σ′, σ̄(σ)) ⊵ val(σ′, σ̄(σ′))).
  - The design target for L-RED (T43's coupled-N5 target transposed to F; not a construction): put every lock into Even's own stale frame.
    A level's final Even edge must look non-improving (or non-optimal in the arena) against σ̄(σ) until the lower levels finish, and then
    become the arena optimum. With NO-TRANSFER this must be done with Odd strategies that are BEST REPLIES, not with a slow Odd counter.
  - DATA (existing): F is short on dlm1/dlm2 (L-NEW box 54; N5-SF-gauntlet-box55 row 3), consistent with (a).

## 4. What this means for SF-POLY / N5
- PROVED-in-source:
  - Koh-Loho: quasi-polynomial iterations for any pivot rule, via a forced-increase potential on universal-tree labels (repeats allowed).
  - Black-Xue Thm 1.1 / Cor. 1.5: coherent (one-parameter) paths can be forced exponential.
  - Chillara-Gajjar-Raja Thm 2-4: n^O(d log n) for d-parameter shortest paths.
  - DLM Thm 1 (SSI, every rule).
  - Friedmann Lemma 4.2 (one-sided SI has a linear rule).
- PROVED (L-LIT, unrefereed):
  - F's run is not coherent (SEGRET).
  - DLM's τ-gated locks cannot affect F's σ-run (DECOUPLE).
  - No rule-independent lower bound exists for F (Lemma 4.2).
- READING:
  - Quasi-polynomial SI bounds come from potential height (Koh-Loho), not from counting best-reply changes. SF-POLY needs a
    polynomial-height potential for F, and universal-tree lattices cannot supply one (CDFJLP quasi-polynomial lower bound).
  - The parametric-dimension route needs F-specific structure on the path polytope; it has no general backing (Black-Xue).
- CONJECTURE (design, offered to L-NEW): KL-SF, F with Koh-Loho tree labels, is quasi-polynomial by construction. Whether it keeps
  N5-SF's behaviour on the fleet corpus is DATA to be measured.
- OPEN:
  - SF-POLY; SF-QP.
  - Parametric dimension of F's runs.
  - Whether a rule-specific F family exists (L-RED's question; §3 states the design target).
- DEAD:
  - "Adapt DLM's mutual locks to F" (DECOUPLE).
  - "A DLM-style all-rules lower bound for F" (Lemma 4.2).
  - "Coherent F-runs" (SEGRET).

## DONE / FINDINGS / NEEDS
- DONE: this note; notebook rows (Koh-Loho, Chillara-Gajjar-Raja Thm 2-4, Black-Xue, DLM re-open, Friedmann Lemma 4.2).
- FINDINGS:
  1. Koh-Loho's quasi-polynomial bound is a potential-height bound (n|L(T)|, any pivot rule, repeats allowed). The opponent's best reply is
     never counted. KL-SF is a design hint.
  2. "Parametric dimension 1" = coherent (Billera-Sturmfels). Black-Xue 2026 make coherent paths exponential on some polytopes. F's runs are
     not coherent (SEGRET), and no literature bounds the d ≥ 2 case.
  3. DLM's locks cannot transfer to F (DECOUPLE). No rule-independent lower bound exists for one-sided SI (Friedmann Lemma 4.2). A lower
     bound for F must exploit F's stale frame, whose design target is in §3.
- NEEDS: none from the owner.
