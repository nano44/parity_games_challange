# R140: Friedmann's locally-optimizing counter (arXiv 0901.2731, PGSolver switchallexp) dies in N5 by S4a's ARENA OPTIMUM alone. τ-fixing is irrelevant. First divergence: iteration 1, where every bit cycle closes at once. Lemma ARENA-MAX: a lane that is only "locally not best" delays nothing, so a port into one W-run needs Ξ-BLOCKED closures (R*_F ≥ 2^N/(n − 1)). No kill
L-RED successor 33 (Opus 5.5; D1/D18). Lead 2026-10-30 13:57Z: "R140 = port Friedmann's mechanism into ONE W-run of real N5 ... (1) Run N5 on
Friedmann's G_n ... Record which of (i)–(iii) breaks the counter, at the first bit flip where it breaks. (2) Design a gadget that defeats
that feature ... (3) If (ii) is the true blocker, state it as an exact lemma candidate". Written 2026-10-30 from 14:00Z (date -u). Labels:
PROVED (lane) / DATA / READING. Not a TARGET.md claim. G-N5-TIME OPEN.

## 0. Sources and family
- L-LIT T53 (l-lit 60bb9a56, docs/lit/T53-arv-friedmann-levels.md) row (2): Friedmann arXiv 0901.2731 Thm 8 (PDF p.9), «13·2^n − 9 iterations
  on G_n using the locally optimizing improvement policy», with the cycle node and the length component fixed. T53 §2 uses PGSolver's
  switchallexp as this family.
- Generator: experiments/hard-families/pgsolver_port.py switchallexp N. It is L-COMP's port of PGSolver d3cd624 switchallexp.ml,
  byte-identical to the original binaries (pgsolver-binary-diff.md).
- Switch-all reference: hard-families/pgsolver_si.py ("switchall" = improvement_policy_optimize_all_locally with
  initial_strategy_by_best_reward, stratimpralgs.ml:659-669, 694-696). Its start is the best-reward start, the same as N5's SPEC S3.

## 1. Step (1): N5 and three controlled hybrids (DATA)
- fried/hybrid.py runs one-sided Even loops on L-SI's si.py Engine (as experiments/new/n5.py does), from the best-reward start:
  - V0: switch-all. Each Even v takes its Ξ-best improving successor.
  - V1: S4a's step with Odd fixed to σ̄_t. That is feature (ii) alone.
  - V2: S4a's step against τ_0 fixed forever. That is (i) + (ii).

  | N | n | PGSolver switchall | V0 | V1 (ii) | V2 (i)+(ii) | N5 (n5b = n5.py, xeng) |
  | --- | --- | --- | --- | --- | --- | --- |
  | 3 | 49 | 71 | 70 | 8 | stalls at 6 | 7 |
  | 4 | 63 | 151 | 150 | 8 | stalls at 8 | 8 |
  | 5 | 77 | 311 | 310 | 10 | stalls | 10 |
  | 6 | 91 | 631 | 630 | 12 | stalls | 12 |
  | 7 | 105 | – | – | 14 | stalls | – |

- V0 reproduces PGSolver's count minus its final check iteration, so the port is faithful. V1 is linear, 2N + O(1).
- So feature (ii), the arena optimum, kills the counter by itself; (i) is not needed. N5 itself also changes τ on this family (iterations
  2-5: h_i → m_i), so its run is not one W-run.
- First divergence, at iteration 1 (sa4, fried/hybrid.py TRACE=1):
  - V0 sends every bit entry e_i into the deceleration lane (e_i → g_i), the locally Ξ-best improving edge.
  - V1 sends every e_i → h_i, closing ALL bit cycles at once. The cycle edge was improving but not locally best, and S4a's one-player
    optimum takes it because it is W-better within the arena.
  - The counter never starts: after 2N + O(1) iterations V1 / N5 are optimal.
- Pins fried/instances/switchallexp_4 and _6 (with best-reward .start): xeng identical (8 and 12 iterations); Oink zlk OK with strategies
  verified.

## 2. Step (3): the exact lemma (PROVED, lane; immediate from SPEC S4a)
- Lemma ARENA-MAX. Let H_t be the arena of S4a at state t: Even v restricted to {σ_t(v)} ∪ Iσ_t(v), Odd fixed to τ_t. Then for every
  vertex v and every Even strategy ρ of H_t:
  W_(t+1)(v) ⊵ val(ρ, τ_t)(v), with W_(t+1) := val(σ_(t+1), τ_t).
  - Proof. σ_(t+1) is Even's pointwise optimal strategy in the one-player game H_t (SPEC S4a: Odd's optimal counterstrategy on the dual of
    H_t, i.e. VJ00's simultaneous optimum). □
- Corollary NO-LOCAL-DELAY.
  - Let an Even edge (v, w) be in Iσ_t, and let some strategy of H_t that uses it give v a W-value strictly above every strategy of H_t
    that does not. Then σ_(t+1)(v) = w, regardless of which improving edge at v is locally Ξ-best.
  - Friedmann's deceleration lane delays the cycle edge only by not being locally best, so in N5 it delays nothing.
- Corollary DECEL-RED (with landed RESULTS R88 FW-R* and R89 GP*-RUN).
  - Inside one W-run F, a closure that the counter needs to delay must be W-better but not adopted. By ARENA-MAX it must therefore be
    outside Iσ (Ξ-blocked) until its time, and its adoption is a late adoption of a blocked edge, counted in R*_F.
  - FW-R* gives |F| ≤ (n − 1)(R*_F + 1) + FL_F. So a Friedmann-type counter with 2^N W-changing steps inside one W-run needs
    R*_F ≥ 2^N/(n − 1) − 1 blocked late adoptions (with FL_F small).
  - The deceleration has to be rebuilt from W/Ξ gaps (R135's gates, R138's late adopters). The lane mechanism of 0901.2731 cannot be
    transplanted.

## 3. Step (2): a gadget against (ii) (READING; not built)
- The required gadget is a "Ξ-deceleration lane":
  - Each bit's cycle edge is Ξ-blocked, W-better, with τ fixed.
  - It is released exactly when the counter reaches that bit.
- Release must be per bit and depend on the lower bits' state. That is R135's waiting gate (lateral or upward), plus a fresh pattern per
  wait (R136 PAT-SW: one switch on the route per release). R135-R139 have not produced such a gate beyond quadratic totals.
- The Lead's suggestion (a lane whose W-value is EQUAL, not better) does not help as stated.
  - A tied closure is not progress.
  - A closure that becomes W-better later needs its target's W to rise first. That is a GP* climb (LAT), paid at most n − 1 per R*-epoch
    by FW-R*, so without blocked edges the run stays ≤ (n − 1) + FL_F.

## DONE / FINDINGS / NEEDS
- DONE: fried/hybrid.py (V0 / V1 / V2, TRACE=1); pins fried/instances/switchallexp_4, _6 (+ .start); check.sh "R140".
- FINDINGS:
  1. DATA: switch-all 70 / 150 / 310 / 630 (N 3-6, faithful). The S4a arena optimum against σ̄ gives 8 / 8 / 10 / 12 / 14 (linear). N5
     gives 7-12 (xeng identical). The blocker is (ii) alone. It breaks at iteration 1, where all bit cycles close at once (e_i → h_i, not
     the lane's e_i → g_i).
  2. PROVED (lane) Lemma ARENA-MAX and Corollary NO-LOCAL-DELAY. With landed FW-R* (Corollary DECEL-RED): a Friedmann counter inside one
     W-run needs R*_F ≥ 2^N/(n − 1) − 1 Ξ-blocked late adoptions. Deceleration must be built from W/Ξ gaps.
  3. READING: a Ξ-deceleration lane is the build target. It is the R135 waiting gate with fresh patterns (R136). Not built.
- NEEDS: none from the owner. Lead: give ARENA-MAX / DECEL-RED to the proof side if useful (it is immediate from the SPEC). Say whether to
  attempt the Ξ-deceleration lane next.
