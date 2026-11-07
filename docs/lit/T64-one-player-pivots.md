# T64: pivot rules for policy / strategy iteration on ONE-PLAYER deterministic games, against L-NEW 44's Lemma TWO-FIX (improving set from G_σ̄, choice from G_τ)
L-LIT successor T59-T64 (Opus 5.5), D18; un-parked by the Lead 2026-11-01 02:52Z for this one box. Written 2026-11-01 02:52Z-03:15Z
(date -u). Working note, unrefereed, not a TARGET.md claim. G-N5-TIME stays OPEN.
Input: L-NEW 44 box 121, Lemma TWO-FIX (lane), as the Lead states it (claude/l-new 7965c774, docs/new/N5-BRTREE-box121.md; not re-read
here). Inside a window with τ and σ̄ both fixed:
- N5 is strategy improvement on the one-player game G_σ̄ (Odd fixed to σ̄): its improving set is G_σ̄'s;
- each step's CHOICE is the arena optimum in the one-player game G_τ (Odd fixed to τ);
- on L-RED's slow builds this window lasts 43-263 steps, while switch-best on G_σ̄ alone finishes in 2.
Labels as in T59.

## Summary
- (a) Post-Ye (arXiv 1208.5083): simplex with the highest-gain (Dantzig) single-switch rule on deterministic discounted MDPs.
  - Thm 3.7 p.9: O(n³m²log²n) iterations, uniform discount, independent of γ.
  - Thm 4.8 p.12: O(n⁵m³log²n), non-uniform discounts.
  - Hypotheses: one player, deterministic transitions, a discounted objective (γ arbitrary), one switch per step, the Dantzig choice.
  - Zhong-Ye 2609.40147 Thm 7.1 is the undiscounted (average-reward) form, O(N³M²log²(2N)).
- (b) Hansen-Kaplan-Zwick (SODA 2014, DOI 10.1137/1.9781611973402.63). ABSTRACT ONLY (CRIS record; full text paywalled, NOT OPENED).
  - Dantzig's rule: O(mn log n) for shortest paths, improving Orlin, and O(m²n²log²n) for deterministic MDPs with a common discount,
    improving Post-Ye by a factor n.
  - An Ω(n²) lower bound for Dantzig on shortest paths with m = Θ(n).
  - A strongly polynomial algorithm for minimum cost-to-time ratio cycles.
- (c) Exponential lower bounds on deterministic one-player games.
  - Howard's PI: Zhong-Ye 2609.40147 Thm 2.1 (discounted, 2 actions per state) and Thm 6.1 (average reward, M ≤ 4N).
  - Single-switch rules on MDPs: Melekopoglou-Condon 1994 (NOT OPENED; cited by Christ-Yannakakis 2212.00083 p.3 as «exponential lower
    bounds for several pivoting rules» for one-switch PI; I do not claim their instances are deterministic).
  - For Dantzig on deterministic games only quadratic lower bounds are known (HKZ Ω(n²), abstract).
- (d) No opened source studies a rule whose improving set comes from one game and whose choice comes from another.
  - Nearest known rules:
    - Schewe's I^glo / one-player switch-best: improving set and choice from the SAME game. On one-player parity games, RESULTS R17:
      ≤ n − 1 value-changing steps per λ-phase.
    - Auger et al.'s Opt-GSIA (2102.04922 Thm 30): the choice is the optimum of a MODIFIED game G[A, σ]. The modification is
      value-consistent (Lemma 12, Prop. 18), so a choice there is an improvement in G.
  - TWO-FIX's choice game G_τ is not value-consistent with G_σ̄ (W ≠ Ξ exactly where σ̄ ≠ τ, i.e. on D). So neither maps, and R17's and
    ABS's proofs do not transfer.
  - TWO-FIX's rule reduces to a known one exactly when D = ∅ in the window (G_τ = G_σ̄ on the play-relevant part). Then it is
    one-player switch-best and R17 applies. The 43-263-step windows are the cost of D ≠ ∅.

## 1. Sources
- OPENED:
  - Post-Ye arXiv 1208.5083 v2 (c51876eb…; earlier tasks; scratchpad t59/A): abstract p.1, «uniform and … nonuniform» (l.15-23), Thm 3.7
    p.9, Thm 4.8 p.12, p.2 «do not extend to policy iteration».
  - Zhong-Ye arXiv 2609.40147 v2 (dafeb818…): Table 1 p.2, Thm 2.1, Thm 6.1, Thm 7.1 + proof pp.31-32.
  - Christ-Yannakakis arXiv 2212.00083 (ab6b5251…, scratchpad t64): p.3 (MC94 remark); p.8 definitions of Simple / Topological /
    Difference PI («Simple policy iteration fixes an ordering over the states and switches the highest-numbered switchable state»).
  - Auger-Badin de Montjoye-Strozecki arXiv 2102.04922 (c992c3f4…): Def. 10, Lemma 12, Prop. 18, Thm 30.
  - Friedmann arXiv 1106.0778 v2 p.7 (I^glo). RESULTS R17 (landed).
- ABSTRACT ONLY: HKZ SODA 2014 via cris.iucc.ac.il (CRIS record; DOI 10.1137/1.9781611973402.63; pp.847-860).
- NOT OPENED: Melekopoglou-Condon 1994 (INFORMS 403, as T30); Orlin 1997 (shortest-path Dantzig bound, cited via the HKZ abstract).

## 2. Mapping to TWO-FIX (Lead-checkable)
| item | rule | improving set | choice | one player? | bound | transfers to TWO-FIX? |
| --- | --- | --- | --- | --- | --- | --- |
| Post-Ye Thm 3.7 / 4.8 | Dantzig single switch | G's | the max-gain edge in G | yes (DMDP) | O(n³m²log²n); O(n⁵m³log²n) | NO as stated: TWO-FIX switches SETS (arena optimum), and its gains are read in G_τ, not in G_σ̄. The contraction route is T59 DZ-W, which needs BLOCK-RATIO (false on fx) |
| Zhong-Ye Thm 7.1 | Dantzig, undiscounted | G's | max residual | yes | O(N³M²log²N) | same as above |
| HKZ (abstract) | Dantzig | G's | max reduced cost | yes | O(mn log n) SP; O(m²n²log²n) DMDP; Ω(n²) SP | same; the Ω(n²) shows quadratic is natural for single-switch on one player |
| Zhong-Ye Thm 2.1, 6.1 | Howard (switch-all greedy) | G's | the greedy edge at every vertex | yes | exp(Ω(N)) | rule differs (TWO-FIX is an arena optimum, which kills greedy lanes: R140 / T59) |
| MC94 (via CY p.3) | single-switch variants | G's | index-based | MDPs | exponential | not checked as deterministic; rule differs |
| I^glo / one-player switch-best; R17 | arena optimum in the SAME game | G's | optimum over G's arena | yes | R17: ≤ n − 1 value-changing steps per λ-phase | YES when D = ∅ in the window (G_τ = G_σ̄ on the plays); otherwise no |
| ABS Opt-GSIA Thm 30 | optimum in a modified game G[A, σ] | – | optimum of G[A, σ] | SSG | (r+k)!, (r+k)q^r | NO: needs value consistency (Lemma 12, Prop. 18); G_τ vs G_σ̄ differ exactly on D |
- READING (what TWO-FIX's rule is, in known terms). A STALE-MODEL arena optimum.
  - The step is the best strategy, among Ξ-improving switches, for a model G_τ that differs from the true improvement model G_σ̄ at the
    deviators D.
  - Termination comes from the restriction to G_σ̄'s improving set (R15), not from the choice. This is L-NEW box 57's Lemma STALE in
    one-player form.
  - The opened literature has no bound for such mixed rules: every opened polynomial bound needs the choice to be read in the same
    model that certifies improvement.

## DONE / FINDINGS / NEEDS
- DONE: this note; notes/L-LIT.md (sources, resume point; parked).
- FINDINGS:
  1. (a) Post-Ye: Dantzig single switch on deterministic MDPs, strongly polynomial for any γ (Thm 3.7 uniform O(n³m²log²n); Thm 4.8
     non-uniform O(n⁵m³log²n)). Zhong-Ye Thm 7.1 is the undiscounted form.
  2. (b) HKZ, abstract only: O(mn log n) shortest paths, O(m²n²log²n) DMDPs, Ω(n²) Dantzig lower bound on shortest paths.
  3. (c) On deterministic one-player games, Howard is exponential (Zhong-Ye Thm 2.1, 6.1). Single-switch exponential bounds (MC94) are
     for MDPs, not opened.
  4. (d) No opened rule takes its improving set from one game and its choice from another. TWO-FIX = one-player switch-best (R17: n − 1
     per λ-phase) exactly when D = ∅. With D ≠ ∅ it is a stale-model arena optimum, and neither R17 nor ABS's value-consistent
     modified-game argument transfers.
- NEEDS: none from the owner (optional: HKZ SODA 2014 full text; Melekopoglou-Condon 1994).
