# T40: policy / strategy iteration with the improving set and the selection rule in DIFFERENT valuations (N5's FRAME SPLIT)
L-LIT successor 2 (Opus 5.5), D18, Lead reading L40. Lead's STEP 2 (message 12:22Z): «Find published analyses of policy / strategy
iteration where the improving set and the selection rule use DIFFERENT valuations ... For each, say whether it bounds the number of
iterations or switches per variable, under what hypothesis, and whether N5's piece (σ̄ and τ fixed, D = {σ̄ ≠ τ} fixed) satisfies it.»
Written 2026-10-29 from 12:45Z (date -u). Working note, unrefereed, not frozen. Not a TARGET.md claim; G-N5-TIME stays OPEN.
Labels (D18): PROVED (L-LIT, unrefereed) / DATA / READING / OPEN / CONJECTURE. Every source is opened (notebook "Sources opened", sha256).

## Summary
| # | source (opened) | frame split | bound on iterations / switches | hypothesis | N5's piece satisfies it? |
| --- | --- | --- | --- | --- | --- |
| 1 | Schewe-Trivedi-Varghese, symmetric SI (arXiv 1501.06484, Alg. 3, 5, Lemma 3.1, Thm 3.7) | improving set Prof(σ) (own valuation, vs Odd's best reply) ∩ the best response σ^c_τ to the CURRENT τ | none (termination only) | — | — . But: with τ fixed, STV's Even step switches each vertex at most ONCE (§1, PROVED); N5's switches one vertex 15 times in runquad's phase (DATA). The split alone is not the obstruction; N5's MOVING target is |
| 2 | Condon (via STV p.2); Pollatschek-Avi-Itzhak, van der Wal (via Bertsekas arXiv 2107.10406 §2) | selection by the joint value W only, no improving-set filter | none: it can CYCLE | — | N5 has the Ξ filter, so it never cycles (R15). Fixes in the literature are asymptotic (contraction), no count |
| 3 | Howard PI and Scherrer's Lemma 8 (arXiv 1306.0386, Lemma 1, 2, 8; Post-Ye Lemma 3.4 there) | none (one frame) — included as the bound-giving template | ≤ n iterations between new cycles (deterministic MDP); γ-contraction | selection greedy in the EVALUATION frame over all actions | NO, twice: the max is over the arena only (L-SI §14 Case A) and in W, not Ξ (Case B). The weaker "A-dominance" (contraction only) fails at 262 of 263 transitions of runquad's phase, 47-55% in the libraries (§3, DATA) |
| 4 | Feinberg-Huang-Scherrer, MPI / optimistic PI / λ-PI not strongly polynomial (ORL 2014, DOI 10.1016/j.orl.2014.07.006, Thm 1, Cor. 2) | greedy w.r.t. a STALE value (partial evaluation), not the policy's own | none: iterations grow arbitrarily with the rewards (3 states, 4 actions) | P{N_j < ∞} > 0 (truncated evaluation) | Not applicable: N5's W is an exact value; VJ valuations are combinatorial, so the numeric mechanism has no analogue |
| 5 | Schewe's optimal improvement = best strategy in the improvement arena (via Friedmann 1106.0778 §4, Thm 8.4; T20) | none (one frame, Ξ) | exponential in two-player games (Friedmann Thm 8.4); one player: R17 | — | N5 = the same arena, other frame; Friedmann's family is left by N5 (T20, T34) |
| 6 | Efroni-Dalal-Scherrer-Mannor, multiple-step greedy (arXiv 1805.07956, Thm 1) | selection by an h-step / κ lookahead operator, evaluation one-step | none (convergence rates in γ) | soft update with stepsize above a threshold, else improvement can FAIL | N5 moves fully to the selected strategy, so the Thm 1 obstruction is absent; no count transfers |
| 7 | Safe policy improvement: SPIBB (arXiv 1712.06924, Thm 1, 2); Petrik-Chow-Ghavamzadeh (arXiv 1607.03842, Def. 2, Thm 6) | arena from a pessimistic / uncertainty criterion, objective from the nominal model | Thm 1: classical PI convergence in a FIXED restricted policy class | the arena does not depend on the current policy | NO: N5's arena Iσ_t moves with σ_t. Robust form is NP-hard (Petrik Thm 6); one-shot, no iteration count |
**Finding.** No opened source bounds iterations or per-variable switches when the improving set and the selection use different
valuations. The bound-giving analyses (3, 5-one-player = R17) need ONE frame; the frame-split analyses (1, 2, 4, 6, 7) give
termination or convergence only, or negative results. Two PROVED facts and one DATA table sharpen what a two-frame theorem would have
to use (§8): W rises at every S4a transition (as does Ξ); S4a dominates Howard's step in W always and in Ξ only half the time.

## 0. The piece (setting)
- N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md). In a phase τ is fixed; on runquad_K8_m30_n192's phase σ̄ is constant too (L-SI box 28 §14).
  So, with G_ρ := the one-player game "Odd fixed to ρ": Ξ_t = val_{G_σ̄}(σ_t) (the IMPROVING frame A) and W_t = val_{G_τ}(σ_t) (the
  SELECTION frame B). They differ only through D = {Odd u : σ̄(u) ≠ τ(u)}.
- S4a: arena H_t = {σ_t(v)} ∪ {w : (v, w) ∈ Iσ_t} at Even v (Iσ_t improving in A); σ_{t+1} = Even's optimal strategy in H_t against τ,
  i.e. the B-optimum over the arena, at every vertex at once. S4c (fallback) is a switch-all step in A.
- The question for each source: does it bound the number of steps of "A-improving arena, B-greedy selection", or the switches of one
  variable, and under what hypothesis?

## 1. Schewe-Trivedi-Varghese, symmetric strategy improvement (arXiv 1501.06484 v1, ICALP 2015)
- What it is. Algorithm 3 (p.2): «update σ using Prof(σ) ∩ σ^c_τ», Prof(σ) the profitable updates of σ (Def. 2.7: against Odd's optimal
  counter strategy, i.e. frame A) and σ^c_τ «the optimal counter strategy to the respective other's strategy» (frame B). Algorithm 5
  (p.6): σ_{i+1} := σ_i^P for P ⊆ Prof(σ) ∩ σ^c_{τ_i}. This is the frame split in intersection form.
- What it proves. Lemma 3.1 (p.6): termination «for all classes of games that are good for strategy improvement», by monotonicity in
  frame A only («the number of values that can be taken is finite»). Theorems 3.4-3.5: correctness. Theorem 3.7 (p.7): the two stopping
  rules differ by at most a linear number of iterations. §4.1 (p.9-10): Friedmann's switch-best traps are escaped, by an argument on that
  family. No iteration bound in general; the authors expect none to be provable easily (p.10: a proof that no traps exist «would imply a
  proof that symmetric strategy improvement solves parity ... games in polynomial time»). DLM (arXiv 2309.02223, Thm 1, Thm 13; T20)
  later give an exponential lower bound for every improvement rule inside this form.
- PROVED (L-LIT, unrefereed). On any stretch of iterations with τ_i = τ fixed, STV's Even step changes each Even vertex at most once,
  provided σ^c_τ is computed by a deterministic procedure from τ (as in every implementation; Algorithm 5 only says "determine"). So
  there are at most |V_0| iterations with an Even change per τ-fixed stretch. Proof: σ^c_{τ} is the same strategy at every iteration of
  the stretch; a switch at v sets σ(v) := σ^c_τ(v), since P ⊆ σ^c_τ; a later switch at v would need an edge of σ^c_τ at v other than
  σ(v) = σ^c_τ(v), and there is none. □
- READING. DLM's Proposition 7 (p.10) proves its 2^(n+1) − 3 count by iterations whose steps 1 and 5 switch a- and d-vertices (both
  players) together, and whose steps 2-4 alternate single switches of the two players. So DLM's exponential count comes from τ moving;
  it says nothing about a τ-fixed stretch, where the bound above holds.
- N5's piece. N5's S4a is NOT this form: its target, the B-optimum over the CURRENT arena, moves as the arena moves. DATA (this note,
  runquad_K8_m30_n192 phase [0, 263], via L-SI's rows()): 481 Even switches by 47 vertices, 32 of them switch ≥ 2 times, one switches
  15 times. So the frame split by itself does not force long τ-fixed stretches (STV's version has ≤ |V_0|); what N5 adds is the moving
  target. A bound for the piece must control how often the arena optimum changes at a vertex.

## 2. The naive W-only selection cycles (Condon; Pollatschek-Avi-Itzhak; van der Wal)
- STV p.2, Algorithm 2 «Naïve symmetric strategy improvement» (σ' = σ^c_τ, τ' = τ^c_σ, no improving filter): «This algorithm has earlier
  been suggested by Condon [5] where it was shown that a repeated application of this update can lead to cycles» ([5] = Condon, "On
  algorithms for simple stochastic games", 1993; primary NOT opened).
- Bertsekas, arXiv 2107.10406 v4 §2 (p.10-13), on Markov games: the Pollatschek-Avi-Itzhak algorithm [PoA69] (evaluate the pair
  (µ_t, ν_t), then both players take the saddle point of the one-step game at J_{µt,νt}, i.e. selection in the joint frame W) is Newton's
  method on Bellman's equation; «a two-state example where the Pollatschek and Avi-Itzhak algorithm does not converge to J* was given by
  van der Wal [Van76] ... the algorithm oscillates» (p.13). (The bibliography lists only [Van78], JOTA 25 (1978) 125-138; [Van76] is not
  in it. Primary not opened.) Hoffman-Karp (one player best-responds, i.e. one frame) «is not subject to the convergence difficulties».
  Bertsekas's fix (§3-4) drops policy improvement and uses a uniform sup-norm contraction: convergence, no iteration count.
- Bound: none; cycling. N5's piece: never cycles (each S4a transition strictly improves σ in frame A; R15), because N5 filters the
  selection by the A-improving arena. This literature only shows the filter is necessary, not that it gives a count.

## 3. The one-frame template: Howard PI, Scherrer's Lemma 8, Post-Ye (arXiv 1306.0386 v4)
- Lemma 1 (p.2): switching any non-empty subset of states with positive advantage gives v_{π′} ≥ v_π. Lemma 2 (p.6, proof §5 p.8):
  Howard's PI contracts with coefficient γ; the proof uses «T_{π*} v_{πk−1} ≤ T_{πk} v_{πk−1}» (π_k greedy for the value of π_{k−1}) and
  Lemma 1. Lemma 8 (p.6, proof p.17): «If the MDP is deterministic, after at most n iterations, either Howard's PI finishes or a new cycle
  appears»; its proof uses «T_{πl} v_{πk−1} ≤ T_{πk} v_{πk−1}» for every k ≤ l and Lemma 1. Lemma 4 = Post-Ye Lemma 3.4 (p.5): the same for
  Simplex-PI with O(n² m log n).
- These are R17's mechanism in MDP form (R17's Lemma P: "the step's objective dominates every path in the arena"). The hypothesis is
  the same: the selection maximises, over ALL actions, the valuation in which progress is measured.
- N5's piece violates it twice, exactly as L-SI box 28 §14 found: (i) S4a maximises only over the arena H_t, so π_l's switches need not
  be available at step k (Case A); (ii) it maximises W, while progress (Lemma 1's role) is in Ξ (Case B).
- A weaker hypothesis that suffices for the CONTRACTION (not for Lemma 8): "A-dominance", v_{πk} ≥ v_{π^H_k} with π^H_k Howard's step from
  π_{k−1}. PROVED (L-LIT, unrefereed, from Scherrer's p.8 proof): then v* − v_{πk} ≤ v* − v_{π^H_k} ≤ γP_{π*}(v* − v_{πk−1}). (In the
  parity setting the discount of the standard reduction is exponentially close to 1, so this alone gives nothing polynomial; Lemma 8,
  which is γ-free, needs the full greedy property.)
- DATA (this note; docs/lit/T40-dominance-check.py, L-SI's rows() and n5x engine read-only): Howard's step σ^H_t = switch-all on Iσ_t with
  S4c's choice (best Ξ_t value, larger index). A-dom: Ξ(σ_{t+1}) ⊵ Ξ(σ^H_t) at every vertex. B-dom: W(σ_{t+1}) ⊵ W(σ^H_t).
  | corpus | games | in-phase transitions | of them fallback | A-dom violated (transitions / (t, v) pairs) | B-dom violated | W-monotone violated at non-fallback transitions |
  | --- | --- | --- | --- | --- | --- | --- |
  | runquad_K8_m30_n192 (L-RED R106 pin) | 1 | 263 | 0 | 262 / 34,583 | 0 | 0 |
  | alt_all (experiments/si/root/logs/alt_all.lst, pinned starts) | 413 | 8,084 | 731 | 4,421 / 46,840 (54.7%) | 0 | 0 (702 at fallbacks) |
  | lib41 (experiments/n5-box18/results/lib41_n48.lst) | 349 | 6,104 | 673 | 2,895 / 23,694 (47.4%) | 0 | 0 (650 at fallbacks) |
  The first A-dom violation on runquad is t = 0, v = 3 (σ_0(3) = 0, σ_1(3) = 9, σ^H_0(3) = 31): L-SI's B-fail witness vertex. Of the
  transitions with D_t = ∅ (σ̄_t = τ at state t), 9 (alt_all) and 4 (lib41), all non-fallback, still violate A-dom (σ̄_{t+1} ≠ τ there);
  Corollary R17-D0 needs D = ∅ on the whole phase.
- So N5's piece does not satisfy even the contraction hypothesis: S4a's step is often Ξ-worse than Howard's at some vertex.

## 4. Stale evaluation: modified / optimistic / λ-policy iteration (Feinberg, Huang, Scherrer, ORL 42 (2014) 429-431)
- Opened: inria.hal.science/hal-01091370 (author copy of DOI 10.1016/j.orl.2014.07.006). Abstract: «the number of arithmetic operations
  required by any member of a broad class of optimistic policy iteration algorithms to solve a deterministic discounted dynamic
  programming problem with three states and four actions may grow arbitrarily». Theorem 1 (p.3): if P{N_j < +∞} > 0 for each j (the
  evaluation is truncated after N_j steps with positive probability), the number of iterations of generalized optimistic PI may grow
  arbitrarily with the data; Corollary 2 (p.4): VI, MPI, λ-PI, OPI are not strongly polynomial. Howard's PI (N_j = ∞) is excluded.
- Frame split: selection greedy w.r.t. a stale estimate V_j, not the current policy's value. Mechanism (Example 1): a reward R close to
  β/(1 − β) keeps a suboptimal action greedy for arbitrarily many truncated evaluations.
- N5's piece: not applicable. W is an exact value (of the pair (σ_t, τ)), and VJ valuations are combinatorial (no magnitudes to tune),
  so the "arbitrarily many iterations for a fixed size" mechanism has no analogue; the piece's length is ≤ the number of strategies.
  Nothing positive transfers either: the AMPI analysis (Scherrer et al., arXiv 1205.3054; abstract opened 2026-10-29: "error propagation analyses",
  finite-sample analysis) bounds errors, not iteration counts.

## 5. One frame, the same arena: Schewe's optimal strategy improvement (via Friedmann; T20)
- Schewe's rule (CSL 2008; definition read in Friedmann arXiv 1106.0778 v2 §4, lower bound Thm 8.4; T20 §0, §3) takes the best strategy
  in the improvement arena against Odd's OPTIMAL reply: arena and objective both in frame A. Friedmann Thm 8.4: exponential.
- In one-player games (σ̄ = τ throughout, D = ∅) N5's S4a is this rule, and R17 / Corollary R17-D0 give < n + m transitions per phase.
  N5 two-player = the same arena with the objective moved to frame B. Friedmann's family is left by N5 (T20; T34 Lemma GATE-SHUT).
- So both "one frame" (Schewe, exponential in two players) and "split frame" (N5) are possible ways to use the arena; only the one-player
  one-frame case has a polynomial phase bound in the literature, and that is R17 (fleet result, not external).

## 6. Selection by a lookahead operator: multiple-step greedy policies (Efroni, Dalal, Scherrer, Mannor; arXiv 1805.07956 v2)
- Theorem 1 (p.3): for π_κ ∈ G_κ(v^π) (κ-greedy) or π_h ∈ G_h(v^π) (h-step greedy) and the soft update (1 − α)π + απ_κ, monotone
  improvement holds only for α above a threshold; below it the value can decrease (the "Tightrope Walking" MDP, Fig. 1). Abstract:
  «monotonic policy improvement is not guaranteed unless the update stepsize is sufficiently large». Theorems 3, 5, 6: convergence and
  error bounds in γ; no iteration counts.
- Frame split: selection by a lookahead operator, evaluation by the policy's own value.
- N5's piece: S4a moves fully to the selected strategy (α = 1), and the arena guarantees frame-A improvement, so the Theorem 1 obstruction
  is absent. No count transfers.

## 7. Arena from one criterion, objective from another: safe policy improvement (cross-field, D18)
- SPIBB (Laroche, Trichelair, Tachet des Combes; arXiv 1712.06924 v5): Π_b = policies that copy the baseline on state-action pairs with
  few samples; Π_b-SPIBB = PI in the MLE model restricted to Π_b. Theorem 1 (p.3): convergence to a Π_b-optimal policy, «a direct
  application of the classical policy iteration theorem»; Theorem 2: safe improvement with high probability.
- Petrik, Chow, Ghavamzadeh (arXiv 1607.03842 v1): Definition 2 (robust policy improvement: maximise the worst-case gain over the baseline
  across an uncertainty set); Theorem 6 (p.5): «Both optimization problems (2) and (3) are NP-hard». One-shot, no iteration analysis.
- Frame split: the allowed set comes from a pessimistic / uncertainty criterion, the objective from the nominal model. This is the
  same shape as N5's piece (Ξ is the pessimistic value: Ξ_t ⊴ W_t pointwise, since σ̄ is Odd's best reply), but SPIBB's arena is FIXED
  (independent of the current policy), which is what makes Theorem 1 classical. N5's arena Iσ_t moves with σ_t.
- READING. If N5's arena were frozen during a phase, S4a would reach the arena's W-optimum in one step and stop; every further W-change
  in the piece is caused by the arena changing. So the piece's length is at most 1 + the number of transitions at which H_t changes
  (trivial: S1's procedure is deterministic, so an unchanged arena and τ give the same output; it moves the question to arena changes).

## 8. What a two-frame theorem would have to use (synthesis)
- PROVED (L-LIT, unrefereed). (W-MONO) At every in-phase non-fallback transition, W(σ_{t+1})(v) ⊵ W(σ_t)(v) at every v. (B-DOM) And
  W(σ_{t+1})(v) ⊵ W(σ′)(v) for every σ′ inside the arena H_t, in particular Howard's σ^H_t. Proof: τ is constant on the phase; σ_t and
  σ^H_t are strategies of the arena H_t (H_t keeps σ_t(v) and every Iσ_t edge); S4a's σ_{t+1} is Even's optimal strategy of H_t against τ,
  computed by S1's procedure, which is optimal at every vertex at once [S1; VJ one-player]; the (σ′, τ)-plays of G and of H_t coincide for
  σ′ in H_t. □ DATA: 0 violations of either at non-fallback transitions (table §3); W-MONO fails only at S4c fallbacks (1,352 of 1,404).
- So on S4a transitions BOTH valuations are monotone (Ξ strictly, R15; W weakly), the step dominates every arena strategy in W, and it
  dominates Howard's step in Ξ only about half the time. Every bound-giving argument opened (Howard contraction, Scherrer Lemma 8,
  Post-Ye Lemma 3.4, R17 Lemma P) needs domination in the PROGRESS frame over all actions. None uses a pair of monotone valuations with
  domination in the other frame. OPEN: a counting argument for "Ξ strictly rising, W weakly rising, W-greedy over the Ξ-arena".
- The STV contrast (§1) isolates one usable ingredient: with τ fixed, a selection with a FIXED target gives ≤ |V_0| steps. N5's target is
  the W-optimum over a moving arena. A candidate to measure (for L-SI, not claimed): the number of transitions at which the W-optimum
  over the full G_τ (= σ^c_τ, fixed in the phase) and S4a's choice disagree at a switching vertex, against the phase length.

## DONE / FINDINGS / NEEDS
- DONE: this note; docs/lit/T40-dominance-check.py (sha1 in the push message; reads experiments/si/root/common.py and
  experiments/new/box21/n5x.py read-only; ~3 s on runquad, minutes per corpus). 9 sources opened (notebook).
- FINDINGS:
  - No published analysis bounds iterations or per-variable switches when the improving set and the selection use different valuations.
    Frame-split methods in the literature (STV symmetric SI, naive symmetric / Pollatschek-Avi-Itzhak, MPI/OPI/λ-PI, multi-step greedy,
    safe policy improvement) have termination, convergence, or negative results (cycling, not strongly polynomial, NP-hard) only.
  - PROVED (unrefereed): with τ fixed, STV's symmetric SI changes each Even vertex at most once (≤ |V_0| steps); N5 switches one vertex 15
    times in runquad's τ-fixed phase. The obstruction is N5's moving arena-optimum, not the split as such.
  - PROVED (unrefereed): W rises weakly at every S4a transition and S4a dominates Howard's step in W; DATA: in Ξ it fails to dominate
    Howard's step at 262/263 runquad transitions and ~half of library transitions, so the HMZ/Scherrer contraction hypothesis fails.
  - The one-frame bounds (Scherrer Lemma 8, Post-Ye Lemma 3.4) are R17's mechanism in MDP form, and fail on N5 for the two reasons
    L-SI §14 found (arena-restricted max; max in W, progress in Ξ).
- NEEDS: none from the owner. Lead: route §8's candidate measurement to L-SI if useful.
