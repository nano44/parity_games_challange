# N5-GATE (box 118): inside a τ-stretch N5's climb is R17's one-player switch-best except at «inconsistent» steps; on every attack build those are almost all steps, and the ungated one-player climb would finish in 2 to 7
L-NEW successor 43, 2026-10-31 (date -u: after 22:19Z). Lead brief 22:19Z (BOX 118): Even's climb inside a τ-stretch below a fixed HI. Is
the number of S4a steps inside one τ-stretch polynomial, in the one-player world G_τ with S4a's arena rule? Connect to known one-player
results only where a source is opened; generalise L-RED R167 (a driver's restart is W-better but not Ξ-improving).
Labels: PROVED (lane), DEAD, DATA, READING, OPEN. No count is bounded here. G-N5-TIME stays OPEN. This is not M3 and not a TARGET.md claim.

## 0. Answer
- Setting: a τ-stretch is a maximal window of transitions with τ constant. G_τ is the one-player game with Odd fixed to τ, and W_k is
  σ_k's valuation in G_τ. IW_k := G_τ's improving edges of σ_k (W-improving); Is_k := N5's improving edges (Ξ-improving, SPEC S2).
  A transition of the stretch is CONSISTENT if Is_k = IW_k and it is not a fallback; otherwise it is INCONSISTENT. INC := their number.
- PROVED (lane) Lemma CONSISTENT-RED (§1): a run of consecutive consistent transitions inside a τ-stretch is a sequence of switch-best steps on
  G_τ, so it has < B := (n² − n + 1)(n + m) transitions (RESULTS R17). Hence a τ-stretch has at most (INC + 1)(B − 1) + INC transitions.
  - EQUIVALENCE (INC ≤ stretch length): τ-stretch lengths are polynomial ⟺ their INC counts are.
  - In words, the only source of super-polynomial length inside a τ-stretch would be steps where the gate (Ξ) and the objective (W)
    disagree. R167's restart (W-better, not Ξ-improving) is one such disagreement: an edge of IW_k outside Is_k.
- DATA (§2, faithful): on every L-RED build the gate is the whole cost.
  - Without the gate, switch-best on G_τ from the stretch's first σ finishes in 2 to 7 steps (20 on fb3).
  - N5's gated climb takes 44 to 403 steps.
  - INC ≈ the stretch length: 43 of 44 on cp_K4, 263 of 264 on s3quad_K8_m30, 395 of 403 on fbg_K12_m6_m24. The longest consistent run
    is 1 to 8 steps (17 on fb3).
  - On switchbestexp_2..6, INC is 6 / 8 / 7 / 8 / 8, flat in N, and the stretch has about the length of the ungated one-player run (ratio ≤ 1.2).
- DEAD (§3, explicit bound): R17's phase theorem does not transfer to N5's climb inside a τ-stretch.
  - Statement killed: «a λ_W-phase of a τ-stretch has at most n − 1 W-changing transitions» (Theorem PH's bound for switch-best on G_τ).
  - Instance: fbg_K12_m6_m24 (n 290, repaired start of box 116b, 0 fallbacks): 403 W-changing transitions in ONE λ_W-phase of one τ-stretch,
    403 > 289.
  - Also lend107_n32: 107 > 31; 118 corpus runs exceed n − 1.
  - Faithful: n5b = n5x state by state, Oink --zlk and --tl verified, N5's regions agree.
  - RESULTS R17's honest limit (ii) (box 10 §5) had already reported a small-margin failure (vc_g25: 26 > 24). This box gives a factor of 1.39 at n = 290 and 3.45 at n = 32.
- DATA (§4): natural potentials of the gate fail. The gap set {v : W(v) ≠ Ξ(v)} GROWS inside stretches (cp_K4: 152 → 168), and box 107's
  A = Σ_v lcp(Ξ, W) drops at 43 of 44 transitions on cp_K4.
- So the τ-stretch question reduces exactly to counting inconsistent steps. On the attack builds that count is the iteration count; the
  one-player world (R17) is fast there, and the slowness is entirely Ξ certifying W's moves late.

## 1. Lemma CONSISTENT-RED — PROVED (lane)
- Premises:
  - [1E-N3-S1] (standing SPEC premise of RESULTS R57): S1's procedure realises the pointwise optimum; so S4a's σ_(k+1) is a pointwise
    optimum of the one-player arena H_k (Even y keeps {σ_k(y)} ∪ Is_k(y), Odd follows τ_k).
  - RESULTS R17 (b)-(d): switch-best on a one-player game (ρ_(j+1) := a pointwise-optimal strategy of the arena {ρ_j(x)} ∪ I_j(x), with
    I_j VJ00's improving edges of ρ_j) makes fewer than B steps. This holds for every pointwise-optimal choice (R17 (d)) and from any start
    (R18 (c): «R17 Corollary 2, which both referees confirmed holds from any start»).
  - SPEC S4 / FIX 3: in a transition with τ_(k+1) = τ_k that is not a fallback, σ_(k+1) is S4a's σ_new, and σ_new ≠ σ_k. Otherwise
    σ_new = σ_k and τ_new = τ_k, which is the fallback condition S4c.
- Statement. Let k0 < k1 be states of one N5 run with τ_k = τ for k0 ≤ k ≤ k1, and let every transition k → k + 1, k0 ≤ k < k1, be
  consistent: no fallback and Is_k = IW_k, where IW_k is the set of VJ00 improving edges of σ_k in G_τ. Then σ_(k0), …, σ_(k1) is a
  sequence of k1 − k0 switch-best steps on G_τ, so k1 − k0 < B.
- Proof.
  - Fix k in [k0, k1). The transition is not a fallback and τ is constant, so σ_(k+1) = σ_new of S4a and σ_new ≠ σ_k (premise 3). In
    particular Is_k ≠ ∅.
  - S4a's arena H_k is the one-player arena on G_τ (Odd follows τ_k = τ) in which Even y may use {σ_k(y)} ∪ Is_k(y) = {σ_k(y)} ∪ IW_k(y).
    By [1E-N3-S1], σ_(k+1) is a pointwise optimum of that arena, i.e. one switch-best step of R17 on G_τ from σ_k.
  - Consecutive steps chain (σ_(k+1) is the next step's start), so the window is a sequence of k1 − k0 switch-best steps on G_τ from σ_(k0).
    R17 (d) with the any-start reading bounds their number by B. □
- Corollary. A τ-stretch with INC inconsistent transitions has at most (INC + 1)(B − 1) + INC transitions. So stretch length is polynomial
  ⟺ INC is polynomial (INC ≤ length).
- Remark. R18 (c) Lemma 3 is the special case Ξ = W (pure transitions on o-acyclic 𝒞^1O), where every transition is consistent. The lemma
  needs only Is = IW, not Ξ = W.
- What it does not give: no bound on INC. The τ-side is untouched too: the number of τ-stretches is G-N5-TIME by TAU-EQ (box 116).

## 2. DATA: the gate is the cost (box118/gate.py, runred.sh, rungate.sh; N5 = n5x.step)
- Per run: τ-stretches; climb steps (τ-constant transitions); INC; «gated» := transitions where R17's ungated step (arena {σ_k} ∪ IW_k
  in G_τ) gives a strictly better W at some vertex than N5's σ_(k+1); onep := the length of R17's switch-best run on G_τ from the longest
  stretch's first σ; maxConsistentWindow.

| instance | n | longest stretch | onep (ungated) | INC in stretches | gated | max consistent run |
| --- | --- | --- | --- | --- | --- | --- |
| cp_K4 / suf_K4 / fbA_K4_m8_m8 | 192 / 103 / 136 | 44 | 2 | 43 | 43 | 1 |
| fbA_K8_m8_m8 / suf_K8 | 192 / 199 | 88 / 152 | 2 | 87 / 151 | 87 / 151 | 1 |
| fbg_K4_m6_m24 / K4_m6_m48 | 178 / 250 | 139 / 235 | 7 | 131 / 227 | 131 / 227 | 8 |
| fbg_K8_m6_m24 / K12_m6_m24 | 234 / 290 | 271 / 403 | 7 | 263 / 395 | 263 / 395 | 8 |
| s3quad_K8_m30 | 479 | 264 | 2 | 263 | 263 | 1 |
| fb3_K4_m6_m12_m12 (R165) | 215 | 158 | 20 | 140 | 140 | 17 |
| topfix_n10 | 210 | 64 | 64 | 0 | 0 | 64 |
| switchbestexp_2..6 | 60..160 | 18 / 26 / 31 / 38 / 44 | 16 / 22 / 28 / 34 / 40 | 6 / 8 / 7 / 8 / 8 | 6 / 8 / 7 / 8 / 8 | 12 / 14 / 20 / 26 / 32 |

- Lag of a gated step (vertices where the ungated step is strictly better): up to 33 (cp_K4), 145 (s3quad), 182 (fbg_K12).
- topfix_n10's 64 steps are a pure one-player switch-best run (INC 0): within R17.
- Corpus (L-SI box 53's 1,132 runs; box 113's repaired starts): 17,841 climb steps, INC 12,433, fallbacks 1,450. 575 runs have INC 0.
  Max INC / n = 3.375 (lend107_n32, INC 108); the longest consistent run is 49 (block_bk32, n 36).
  - Largest ratio stretch / |onep| = 132 (s3quad_K8_m30: 264 vs 2).
  - R17's run stalls (arena optimum = σ with IW ≠ ∅, the own-cycle-node case of R15's side finding) on 58 runs; there onep is the
    pre-stall length and the ratio uses it.
- READING:
  - L-RED's builds are N5-specific in a precise sense: the same stretch without the Ξ-gate (R17 on G_τ) is 2 to 7 steps, and ARSB, which
    keeps the gate but optimises against σ̄, takes 2 to 23 (box 117 §4).
  - The slowness is the MISMATCH: the gate certifies by Ξ (against σ̄), the objective is W (against τ). Each inconsistent step moves W as far
    as Ξ certifies, so W advances along a front one gate at a time.
  - R167's UNSAT is the statement that the front cannot be re-run inside one phase by a W-better restart, because the gate refuses it.

## 3. DEAD: R17's phase bound inside a τ-stretch (explicit bound n − 1)
- Statement killed (never claimed by the fleet for two players; RESULTS R17's honest limit (ii) already reported a small-margin failure, vc_g25 26 > 24): «in a
  τ-stretch, every λ_W-phase (maximal window with W's cycle-node map constant) has at most n − 1 W-changing transitions».
- Instance: experiments/new/box116/inst/fbg_K12_m6_m24.pg (L-RED's fbg family; repaired start fbg_K12_m6_m24_fixed.start of box 116b).
  - n 290, 404 iterations, 0 fallbacks.
  - One τ-stretch of 403 transitions, one λ_W-phase, 403 W-changing transitions > 289.
- Second instance: n5-epoch/instances/lend107_n32 (with its start): 107 W-changing transitions in one λ_W-phase > 31 (10 fallbacks in
  the run). 118 of 1,132 corpus runs exceed n − 1.
- Faithfulness (box118/pincheck.sh, pincheck.txt):
  - n5b = n5x «identical state sequences: True» (404 and 112 iterations);
  - Oink 8fbf0a7 --zlk and --tl «solution verified» on both;
  - N5's regions agree with Oink's (pinwin AGREE True).
- The obstruction: Lemma P's induction (R17 (b)) needs every edge of a k-edge path to a cycle node to be AVAILABLE in the arena at the step
  where it is used. In N5 the edge must also be Ξ-improving. On fbg the gate lets the front advance about one vertex per step, and the
  front is re-entered by fbg's gates (L-RED R158 / R165).

## 4. DATA: two candidate potentials of the gate fail (box118/gapset.py)
- GAP_k := {v : W_k(v) ≠ Ξ_k(v)}. Every blocked edge (y, z) ∈ IW_k minus Is_k has z ∈ GAP_k, because
  Ξ(z) ⊴ Ξ(σ(y)) ⊴ W(σ(y)) ◁ W(z) (R18 (d) Lemma S (b)). So an empty gap set forces Is ⊇ IW.
- But GAP grows inside the stretches: cp_K4 152 → 168 (8 growths, 1 shrink, 44 transitions); fbg_K4_m6_m24 138 → 154 (7 growths, 2 shrinks).
- A_k := Σ_v lcp(cs Ξ_k(v), cs W_k(v)) (box 107 / T63's A-potential) drops at 43 of 44 transitions on cp_K4 and at 130 of 139 on
  fbg_K4_m6_m24.
- READING: W runs ahead of Ξ as the climb proceeds. Neither the gap set nor A measures progress; both measure the mismatch, which grows.

## 5. What this means (READING)
- Inside a τ-stretch, the one-player world is fast (R17; DATA: 2 to 7 steps on every build). The open quantity is INC, the steps where
  Ξ's gate and W's objective disagree.
- Any bound on INC must use Ξ's two-player structure: Is is computed against σ̄, so the gate moves with Odd's BEST reply while W is
  measured against τ. That is the XI-CH core again, now localised to the gate's mismatch.
- R167's UNSAT model is the strongest data that INC is constrained: a W-better restart is never Ξ-improving, so a front cannot be
  re-run inside one phase. A lemma in that direction would be: a blocked edge (y, z) ∈ IW minus Is can become Ξ-improving only after a
  Ξ-change of z at a key above the key that blocked it.
  - That is FUEL-COUNT's HC (P-N5-ODD §6) on the gate side.
  - Not stated as a conjecture: the gap set data (§4) show the blocked edges multiply.
- Possible next target (untested): count, per τ-stretch, the DISTINCT blocked edges that are later used (unblocked and switched to), and
  test whether INC ≤ c·(their number + fallbacks). If yes, INC is charged to edges × unblock events, i.e. to Ξ-changes of targets
  (FUEL-COUNT's form).

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/new/box118/ (gate.py, gapset.py, rungate.sh, runred.sh, pincheck.sh; outputs g_sbcg.txt, g_alt.txt
  (final), g1_*.txt (first pass, without INC), g_red.txt, pincheck.txt); check.sh pin «box 118 GATE»; box 117 erratum (SQUEEZE = landed
  R18 (d) Lemma S (b)).
- FINDINGS:
  - PROVED (lane) CONSISTENT-RED: τ-stretch length ≤ (INC + 1)(B − 1) + INC, with B from R17; an equivalence.
  - DATA: on every L-RED build the ungated one-player climb takes 2 to 7 steps (20 on fb3), N5 takes 44 to 403, and INC ≈ the stretch
    length. On switchbestexp INC stays at 6 to 8.
  - DEAD (explicit bound): R17's n − 1 per λ-phase fails inside a τ-stretch: fbg_K12_m6_m24 403 > 289 (faithful, Oink OK).
  - DATA: the gap set and the A-potential grow / drop. Not potentials.
- NEEDS: Lead: next box. Candidate: blocked-edge unblock charging (§5).
