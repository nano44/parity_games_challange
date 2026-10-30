# N5-FBENERGY (box 67): a Lyapunov energy for in-phase fallbacks (FB-LIN). The gap set never grows at a fallback; no energy drops at every one
L-NEW successor 35 (Opus 5.5), D14 / D18, Lead reading L40. Lead's brief 2026-10-30 00:23Z (BOX 67: ρ-POLY / FB-LIN by an import matching
"fallback = σ abandons its current best response and reverts"; candidates: a Lyapunov energy, no-regret switching, a Monderer-Shapley
potential). Written from ~00:45Z (date -u). Working note, unrefereed, not a TARGET.md claim. G-N5-TIME OPEN.
Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING.
- FB-LIN's statement (L-RED R100 §0, as briefed 2026-10-29 00:28Z; docs/lit/T36-n5-reduction-map.md l. 62): CONJECTURE FB-LIN, at most
  n in-phase (Even S4c) fallbacks in one phase (phase = RESULTS R38 (a), (λ_Ξ, τ) constant). Status OPEN; DATA max 0.79n; L-RED R100-R104
  (5 boxes, no kill). Best landed lemmas: RESULTS R56 FB-RED (≤ 1 + (n − 1)(2 + ρ) per phase, a reduction in ρ); RESULTS R81 / P-N5-FBCK
  (f ≤ n_K·|𝒞^K_f|, per K-configuration). My box 50 (N5-FBLIN-box50.md): a fallback forces neither a path-set change nor a carry (DEAD).
- Tool: experiments/new/box67/energy.py; corpus experiments/si/root/logs/alt_all.lst (413 games, 94 with pinned starts) via box67/run.sh;
  L-RED's FB instances red/fb/instances/fb38_n48, red/sel/instances/pl130_n40, red/n3/instances/long121_n40 with their starts.
- Sources: the import is used only as a TEMPLATE (a bounded integer energy that drops at every fallback and never rises elsewhere would
  bound fallbacks by its range). No theorem from discrete dynamical systems, online learning or potential games is cited, so none was
  opened. The notebook records this.

## 1. The energies tested (DATA, energy.py)
W := val(σ, τ) on G_τ. D := {Odd u : σ̄(u) ≠ τ(u)} (open gates). For each candidate: FBUP = in-phase fallbacks at which E does NOT strictly
drop; SAUP = in-phase non-fallback transitions at which E rises. An energy with FBUP = SAUP = 0 would prove FB-LIN with its range.
| candidate | FBUP (of 731 fallbacks, 413 games) | SAUP |
| --- | --- | --- |
| E1 = #Even v with Iσ(v) ≠ ∅ (the Lead's "Ξ-suboptimal σ-edges") | 537 | 1220 |
| E2 = Σ (rank + 1) over those v | 414 | 2947 |
| E3 = |Z|, Z := {v : Ξ(v) ≠ W(v)} (the GAP set) | 56 | 2440 |
| E4 = |D| | 685 | 469 |
| E5 = #v whose (σ, τ)-play meets D | 55 | 2429 |
| E6 = #blocked Even edges (R88) | 304 | 1111 |
- DEAD: every candidate as a Lyapunov energy. None drops at every fallback, and all rise at S4a steps.
- Smallest killing instance, for the two best ones (E3, E5): experiments/n5-epoch/instances/lend9_n8.pg with its .start (n 8). It has 3
  in-phase fallbacks in one phase, and E3 drops at none of them (FBUP 3).
- On L-RED's record, E3 drops at every fallback but rises at S4a steps (energy_red.txt). fb38_n48: f 38, |Z| at phase start 34, rises
  of |Z| in the phase 55. So the amortised form "f ≤ |Z_start| + rises" gives 89 > n = 48 there.

## 2. What survives: Lemma GAP-MON (PROVED, lane)
Let k → k + 1 be an Even S4c fallback with τ_{k+1} = τ_k = τ (every in-phase fallback is one). Write Z_t := {v : Ξ_t(v) ≠ W_t(v)}. Then
Z_{k+1} ⊆ Z_k, and every v ∉ Z_k keeps both values: Ξ_{k+1}(v) = Ξ_k(v) and W_{k+1}(v) = W_k(v).
Proof.
- (i) Ξ_{k+1} ⊵ Ξ_k pointwise. σ_{k+1} = Switch_I(σ_k) with ∅ ≠ I ⊆ Iσ_k (RESULTS R15 (d)), then R15 (a).
- (ii) W_{k+1} ⊴ W_k pointwise (box 21 Lemma W). S4c fires only when S4a returned σ_new = σ_k. So σ_k is the optimum of the one-player
  arena H_k = σ_k ∪ Iσ_k against τ. S4c's σ_{k+1} uses only edges of H_k, and the optimum dominates every strategy of H_k pointwise
  (RESULTS R17 (a) F1). The (σ, τ)-plays of H_k and G_τ coincide for strategies inside H_k.
- (iii) Ξ_t ⊴ W_t pointwise (R88 §2 Lemma XW: σ̄ minimises at every vertex at once, τ is one Odd strategy).
- If v ∉ Z_k: W_{k+1}(v) ⊴ W_k(v) = Ξ_k(v) ⊴ Ξ_{k+1}(v) ⊴ W_{k+1}(v). So all four are equal. □
DATA: Z grows at 0 of the 731 alt_all fallbacks and at 0 on L-RED's three instances (ZGROW 0).
Reading of GAP-MON. A fallback acts only inside the gap Z: outside it, Ξ and W are frozen. A fallback is the "revert" the brief describes.
Even abandons its W-best response and takes Ξ-best edges, and the only vertices that move are those where the honest frame and the
τ-frame disagree. So "f ≤ |Z| at phase start" would follow from "every fallback closes a gap vertex", which is false (§1, lend9_n8).
The obstruction is twofold:
- (a) a fallback can leave |Z| unchanged (it changes values inside Z without equalising any);
- (b) S4a steps re-open gaps (SAUP of E3 is 2440; up to 2.48n per phase, n5-exhaustive/instances/b6_xw_n48).

## 3. The other two imports (READING)
- Monderer-Shapley potential. In the "local game" of Even against the two frames, Ξ is an ordinal potential for both move types: R15 (a)
  for S4a and S4c alike. That is the termination potential, and its range is exponential. Its polynomial-range part is the cycle-node
  map λ_Ξ, which is CONSTANT in a phase by definition. So a potential of this kind cannot count in-phase fallbacks. Structural
  obstruction, no instance needed.
- No-regret ⇒ few switches. That argument bounds switches of a LAZY learner, one that switches only when the cumulative gain exceeds a
  threshold. N5's fallback rule is not lazy. It switches every improving vertex at once, whatever the size of the gain. The import
  would need a threshold that N5 does not have. Not pursued.

## 4. What it gives toward FB-LIN (READING)
- With GAP-MON, FB-LIN reduces to two counts per phase:
  - (a) fallbacks that close no gap vertex ("Z-flat" fallbacks, FBUP of E3: 56 in 413 games, at most 10 in one game: n5-epoch/instances/nep22f_n64, n 64);
  - (b) gap re-openings at S4a steps.
- Then f ≤ |Z_start| + (Z-flat fallbacks) + (re-openings) ≤ n + (a) + (b).
- Neither (a) nor (b) is bounded here. CONJECTURE (b)-type bounds are not proposed: re-openings reach 2.48n per phase.

## DONE / FINDINGS / NEEDS
- DONE: box67/energy.py, run.sh; energy_alt.txt (413 games), energy_red.txt (fb38_n48, pl130_n40, long121_n40); check.sh "box 67"; this note.
- FINDINGS:
  (1) DEAD: all six Lyapunov candidates, including the Lead's E1. None drops at every fallback; the best two fail 55-56 times. Smallest
  killing instance lend9_n8 (3 fallbacks, no drop of E3).
  (2) PROVED (lane): Lemma GAP-MON. At an Even fallback with τ fixed, the gap set Z = {Ξ ≠ W} never grows, and Ξ, W are frozen outside
  it. DATA 0 / 731.
  (3) READING: the Monderer-Shapley potential is λ_Ξ-blind in a phase; no-regret needs laziness that N5 lacks.
  (4) READING: FB-LIN ⇐ few Z-flat fallbacks ∧ few S4a gap re-openings per phase.
- NEEDS: none from the owner.
