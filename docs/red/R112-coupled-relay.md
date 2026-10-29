# R112: the first COUPLED family. A mutual relay chain in which every σ-change is caused by a τ-change and every τ-change by a σ-change, all inside ONE joint λ-run: 4L + 1 iterations, 2L σ-changes and 2L + 1 τ-changes at n = 8L + 4 (also from the S3 start via s3embed). Linear, NM = 0. Plus three READINGs on why coupling is hard: the stall-support rule, the direction rule, and why a re-usable coupled clock needs a graph cycle. DATA + READING
L-RED successor 27 (Opus 5.5; D1/D15/D18; Lead 13:47Z STEP 1: «the COUPLED family. σ-changes and τ-changes per joint λ-run must
both grow, each caused by the other; a disjoint union does not count»). Labels: DATA / READING / OPEN. Not a TARGET.md claim.
G-N5-TIME stays OPEN: everything here is linear.

## Summary
| item | label |
| --- | --- |
| cpl/chain.py L: four vertices per level (d_i, a_i, f_i, o_i), a DAG into one odd sink z. From the designed start N5 makes 4L + 1 iterations, 0 fallbacks, ONE joint λ-run (λ and λ^U constant: every Ξ- and U-play ends at z), 2L σ-changes and 2L + 1 τ-changes, strictly alternating in pairs (L = 2..40 exact). | DATA |
| Causation (trace, §2): o_{i−1} (τ) → d_i (τ, U-menu opens) → a_i (σ, W-release by d_i) → f_i (σ, Ξ-menu opens) → o_i (τ, W-release by f_i) → d_{i+1} … Each σ-step is released by the τ-step just before it and conversely (§1 lists the condition at each vertex; the trace shows one vertex per transition, in this order). | DATA |
| S3 default start: relay_L10_s3 (s3embed of relay_L10, n 209) makes the same 41 iterations, 1 joint λ-run, 20 σ- / 21 τ-changes. The S3 start of relay_L10 itself (no embedding) gives 2 iterations. | DATA |
| Engines: n5b SPEC and n5.py (si.py) state sequences identical (relay_L10); Oink zlk OK, both strategies verified, both engines' outputs, explicit and S3 pins. | DATA |
| Carries: NM = 0 and PCH ≤ 2 per vertex per λ-run (nm.py unmodified per phase; nmrun.py per λ-run and per joint run). Odd side on G^d (mirror check True): NM^U = 0, PCH^U ≤ 2. | DATA |
| Random hill climb (cpl/search.py, fitness min(σ-changes, τ-changes) in one joint λ-run; n 12-24, 16 runs × ≤ 20,000 steps, explicit and S3 starts): best 12 at n 20 (explicit) and 11 at n 24 (S3). Nothing beyond n/2 (bests not pinned; logs not kept). | DATA |
| Stall-support, direction and cycle rules (§3). | READING |

## 1. Construction (experiments/red/cpl/chain.py)
- z: Even self-loop, odd priority Z above every structural vertex; every marker (D_i, A_i, F_i, O_i, K0, O0) is an even priority above Z
  with one successor z. So every play is a DAG path into z, and a valuation is the marker on the path (then length).
- Level i = 1..L, start in brackets:
  - d_i (Odd): [D_i] | o_{i−1};
  - a_i (Even): [d_i] | A_i;
  - f_i (Even): [F_i] | a_i;
  - o_i (Odd): [f_i] | O_i.
  - Base: o_0 (Odd): [K0] | O0.
- Even-scale order (markers are even, so "higher priority" = "better for Even"):
  O0 < F_1 < O_1 < F_2 < O_2 < … < F_L < O_L < A_L < D_L < A_{L−1} < D_{L−1} < … < A_1 < D_1 < K0.
- Why each step waits (all checked in the trace):
  - o_i: its U-menu (O_i) is open from the start (U(f_i) = max(F_i, U(a_i)) ≥ A_i > O_i), but W keeps f_i while σ(f_i) = F_i < O_i.
    It switches the step after f_i moves to a_i (then W(f_i) = W(a_i) = A_i > O_i).
  - d_i: its U-menu opens only when U(o_{i−1}) drops below D_i. Before o_{i−1} switches, U(o_{i−1}) ≥ A_{i−1} > D_i; after, U = O_{i−1}.
    (A first version with A_i below the D's let the d's cascade by U alone, Odd to Odd; the interleaved ladder A_{i−1} > D_i fixes it.)
  - a_i: A_i is Ξ-improving from the start (Ξ(d_i) ≤ O_{i−1} < A_i), but W keeps d_i while τ(d_i) = D_i > A_i. It switches the step
    after d_i moves to o_{i−1} (then W(d_i) = O_{i−1} < A_i).
  - f_i: a_i is Ξ-improving only after a_i switched (before: Ξ(a_i) ≤ O_{i−1} < F_i).

## 2. DATA
| pin (experiments/red/cpl/instances/) | sha1 game / start | n | start | iterations | fb | joint λ-runs | σ-changes | τ-changes | engines | Oink |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| relay_L3 (check.sh gate) | 4e5e02b8936e… / 18980d20158f… | 28 | explicit | 13 | 0 | 1 | 6 | 7 | n5b = n5.py | OK |
| relay_L10 | fb0da4fdfd65… / b00305860e05… | 84 | explicit | 41 | 0 | 1 | 20 | 21 | n5b = n5.py states | OK |
| relay_L10_s3 | d43bee14a6da… / none | 209 | S3 | 41 | 0 | 1 | 20 | 21 | n5b, n5.py 41 | OK |
- chain.py L = 2, 5, 10, 20, 40: n = 20, 44, 84, 164, 324; iterations 9, 21, 41, 81, 161 = 4L + 1; σ-changes 2L, τ-changes 2L + 1;
  0 fallbacks; one joint λ-run each.
- Trace relay_L3 (trn.py), all 13 transitions: t0 o0 (τ); t1 d1 (τ); t2 a1 (σ); t3 f1 (σ); t4 o1 (τ); t5 d2; t6 a2; t7 f2; t8 o2;
  t9 d3; t10 a3; t11 f3; t12 o3. Exactly one vertex switches per transition.
- Carries (relay_L10): nm.py (key r38, per phase) nm_max 0, pch_max 1; nmrun.py per λ-run: NM 0, PCH 2 (one vertex); per joint run the
  same. G^d (ctl/dualize.py) mirrors G at all 42 states (ctl/mirror.py True); nmrun.py on G^d: NM^U 0, PCH^U 2.
- Tools (experiments/red/cpl/): cpl.py (per joint λ-run σ-/τ-changes; λ from Ξ_σ on G, λ^U from Ξ_τ on G^d), nmrun.py (NM per λ-run /
  joint run with nm.py's matched() and wmap() imported unchanged; nm.py itself cuts per phase, key (λ_Ξ, τ), so it resets at every
  τ-change), trn.py (named trace), vcpl.sh (two engines, Oink, counts), build.py, chain.py, search.py.

## 3. READING: what coupling requires (from SPEC S4a/S4b; checked against the traces, not proved here)
- (S) Stall-support rule. Write W for the valuation of the joint play (σ, τ), Ξ for σ against Odd's best reply, U for τ against Even's
  best reply. For Even, Ξ ≤ W ≤ U pointwise.
  - An Odd vertex b with a U-improving switch y keeps τ(b) = x only if W(y) ≥ W(x) (Even scale). Since U(y) < U(x) and W ≤ U, this needs
    W(x) < U(x): some Even vertex on x's W-play is not Even's best reply to τ. If x's play has no Even choice, b cannot stall.
  - Dually, an Even vertex a with a Ξ-improving switch keeps its edge only if some Odd vertex on its keep play is not Odd's best reply to σ.
- (D) Direction rule. Odd's S4b step alone (σ fixed) lowers W at every vertex (keep is allowed everywhere and the step is Odd's joint
  optimum); Even's S4a step alone raises W everywhere. So:
  - a τ-change can release an Even stall only by lowering W on its KEEP play (as d_i does for a_i);
  - a σ-change can release an Odd stall only by raising W on its keep play (f_i for o_i), and then W at the released Odd vertex still
    rises net (Odd moves to the smaller of two rises).
  - Consequence for chains: an Odd vertex released by an Even rise cannot, by its own move, release an Even vertex whose keep runs
    through it (W there only rises). The chain has to pass through a U-cascade step (o_{i−1} → d_i: U depends on τ only), which is why
    each level has four vertices.
- (C) Cycle rule. In a DAG every support chain of (S) ends at a vertex with no support, which moves at once; the chain unravels from
  there, one level per few steps, and each gate fires once (here: 4 steps per level, every vertex switches at most once). A clock whose
  gates fire again needs information to return to a vertex it came from, i.e. a cycle in the game graph (mkr has one: h → C → w → T →
  G → r_m → … → h). In a coupled clock each such cycle crosses both sides, and keeping λ and λ^U constant then needs every graph cycle to
  be avoided by Ξ-plays (Odd can exit and prefers to) and by U-plays (Even can exit and prefers to). Example of the conflict: an even-top
  cycle is avoided by Odd in Ξ but closed by Even in U unless some τ-edge on it exits.
- So the next family must have (i) flip-flops that re-fire (two sources whose values leapfrog, as mkr's reactors) on BOTH sides, and
  (ii) Odd breakers whose τ exits every cycle stably in U. OPEN; §4.

## 4. Next (OPEN)
- Two-sided clock: Even pivots h, h′ with Even reactors (mkr) and Odd pivots g, g′ with Odd reactors (dual mkr); h's and h′'s steps
  released by Odd holders whose U-menu opens when the Odd reactor wave arrives (rule (D): via the holder's keep), g's and g′'s steps
  released by Even holders whose Ξ-menu opens when the Even wave arrives. Target: Θ(Km) σ-changes and Θ(Km) τ-changes in one joint λ-run.
- Then nesting toward the Lead's first measurable target (super-quadratic NM* or NM*^U in one joint λ-run).

## DONE / FINDINGS / NEEDS
- DONE: cpl/ tools and pins above; check.sh gate (relay_L3: 13 iterations, 6/7 changes, 1 joint run).
- FINDINGS:
  1. DATA: a coupled family exists: 2L σ- and 2L + 1 τ-changes in ONE joint λ-run, each caused by the other (relay chain, n = 8L + 4;
     explicit and S3 starts; two engines; Oink). Linear; NM = NM^U = 0.
  2. READING (S): an Odd stall needs a not-best-reply Even vertex on its keep play (W < U there), and dually.
  3. READING (D): τ-changes only lower W, σ-changes only raise W; a coupled chain must route Even → Odd through W-rises and Odd → Even
     through U-cascades and W-drops.
  4. READING (C): in a DAG every gate fires once; a re-usable coupled clock needs graph cycles crossing both sides, with Odd breakers to
     keep λ^U constant.
- NEEDS: none from the owner.
