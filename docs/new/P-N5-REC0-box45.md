# Packet P-N5-REC0 (box 45): in every phase of N5, the epochs in which Odd's best reply agrees with τ (D = ∅) number at most (f + 1)(n + 1) + 4n(n − 1) + 1 (Lemma REC-0) — every game
L-NEW successor 24 (Opus 5.5), D14 / D18, Lead reading L40; Lead's PICK 08:03Z (Lead's stamp): "(a). Freeze packet P-N5-REC0-box45 from §5 …
the exact statement; the premise list, with the R17 (b) use flagged as a question for the referees …; the data, and the climbs labelled DATA."
Written 2026-10-26 08:03Z (date -u). FROZEN at push: later text goes into a fixes file.
Source: docs/new/N5-NEP-box45.md §5 (working doc, l-new 40659d50; this packet governs). Labels: PROVED (L-NEW 24, unrefereed) / READING / DATA.
Not a TARGET.md claim. REC-0 is a REDUCTION: it bounds the D = ∅ epochs of a phase in terms of the phase's fallbacks f; it does not bound f,
and nothing here bounds N5's running time on any class beyond 𝒞^1O ∪ 𝒞^1E. G-N5-TIME stays open.

## To sign, and what is not to sign
| § | statement | label |
| --- | --- | --- |
| §1 | Lemma REC-0, with the corollary on transitions | PROVED (to sign) |
| §2 | what REC-0 does not give; consequences with R56 and FB-kT | READING (not to sign) |
| §3 | data and climbs | DATA (not to sign) |
- Premises (LANDED unless marked):
  - SPEC S1-S5 of docs/new/N5-ssi-global.md (FIX 1-4, Q1-Q4); S4a (arena: Even v restricted to {σ(v)} ∪ Iσ(v), Odd to τ).
  - RESULTS R17 (b) Lemma P (its INDUCTION STEP only) and R17 (F1)/(F2), (d) ("the bound holds for every pointwise-optimal choice").
    QUESTION FOR THE REFEREES (Q-R17): REC-0 applies the induction step of Lemma P at a state k of an N5 run, not inside a run of switch-best
    from a phase start. As I read docs/new/N5-phase-bound-box10.md §2, the step from k to k + 1 uses only: the hypothesis at k (W_k ⪰ value(r)
    for paths with ≤ j edges), that the step is an optimum of the switch-best arena H_k (every improving edge available), (F1)/(F2), and that
    no vertex changes its cycle node from k to k + 1 (its cases B1/B2 end in "the phase ended at step k + 1, contrary to the assumption"). Please
    confirm that nothing else (in particular nothing about earlier steps or the phase start) is used.
  - RESULTS R18 (d) Lemma S (c) (S4a's output is an optimum of its arena against τ).
  - RESULTS R23 (g) Lemma WM (W_{k+1} ⊵ W_k at an in-phase non-fallback transition); game-general (P-N5-XEP fixes, XEP-N2, both referees).
  - RESULTS R21 (a) Lemma XW (Ξ_k ⊴ W_k); game-general (= (VJ) at τ′ := τ_k, RESULTS R57).
  - RESULTS R15 (a) (Ξ non-decreasing along a run) and R15 (d) (at most 4n(n − 1) consecutive iterations leave both Ωσ and Ωτ unchanged).
  - P-N5-XEP §2 Corollary SN-PREFIX_D (a) (signed by both referees; fixes file P-N5-XEP-fixes-box44): along a run of consecutive in-phase S4a
    transitions, each vertex's unsplit states form a prefix of the run.
  - RESULTS R64 (P-N5-EPR, landed) Corollary EP-0, for the corollary on transitions only.

## 0. Setting (every game)
- N5 = SPEC S1-S5. State k = (σ_k, τ_k); σ̄_k = S1's Odd counterstrategy; Ξ_k = V_{σ_k,σ̄_k}; W_k := V_{σ_k,τ_k}, σ_k's valuation in G_τ (Odd fixed to
  τ_k); λ := Ξ's cycle-node map, λ_W := W's. A PHASE P: a maximal run of consecutive states with (λ, τ) constant; f := its in-phase S4c
  fallbacks. Q := the Odd vertices of out-degree ≥ 2. An EPOCH: a maximal run of consecutive states of P with σ̄|Q constant;
  D_E := {q ∈ Q : σ̄_E(q) ≠ τ(q)}.
- A state of P is D = ∅ if σ̄_k(q) = τ(q) for all q ∈ Q; then σ̄_k = τ (Odd vertices outside Q have one successor) and Ξ_k = W_k. A state is
  ALL-UNSPLIT if λ_W = λ there; D = ∅ states are all-unsplit.
- The W-frame of P is the FIXED one-player game G_τ (τ is constant on P).
- LEVEL. For j ≥ 0, a state k has LEVEL j if W_k(x) ⪰ value(r) for every vertex x and every simple path r of G_τ with ≤ j edges from x to a cycle
  node u of λ (u = λ(u)), where value(r) := (u, P(r), |r|), P(r) = the vertices of r before u more relevant than u (as in R17 Lemma P).
  B(x) := the maximum of value(r) over all such simple paths r from x (≤ n − 1 edges).

## 1. Lemma REC-0 (PROVED, every game)
Statement. In every phase P of N5, the number N_0 of epochs E of P with D_E = ∅ satisfies
    N_0 ≤ (f + 1)(n + 1) + 4n(n − 1) + 1.
Corollary. With EP-0 (RESULTS R64: len(E) ≤ n + m when D_E = ∅), the in-phase transitions of P whose source lies in a D = ∅ epoch number at most
((f + 1)(n + 1) + 4n(n − 1) + 1)·(n + m).
Proof.
1. (Level step.) Let k be a D = ∅ state of P with level j, let k → k + 1 be an S4a step, and let k + 1 be all-unsplit. Then k + 1 has level j + 1.
   At k, Ξ_k = W_k, so the gates Iσ_k (S2: Ξ-improving edges) are exactly the W-improving edges of G_τ at σ_k, and S4a's arena is the
   switch-best arena H_k of G_τ; S4a's output is an optimum of it (R18 (d) S (c)). λ_W = λ at k and at k + 1, so no vertex changes its W-cycle
   node. The induction step of R17 Lemma P, with Ω := W, ρ_k := σ_k, ρ_{k+1} := σ_{k+1} and u a cycle node of λ, gives level j + 1 at k + 1 (Q-R17).
2. (Persistence and base.) Every all-unsplit state has level 0 (for a cycle node u of λ = λ_W, W(u) = (u, ∅, 0) = value of the empty path). If k → k + 1
   is an S4a step and k, k + 1 are all-unsplit, level j at k gives level j at k + 1: W_{k+1} ⊵ W_k (WM), and the cycle nodes of λ are unchanged.
3. (Runs.) The f fallback transitions split P into ≤ f + 1 maximal runs R of consecutive in-phase S4a transitions (fallback-free runs). By
   SN-PREFIX_D (a) applied to every vertex, the all-unsplit states of R form a prefix U(R) of R. By 1 and 2, inside U(R) the level never decreases,
   and it rises by one at every S4a step from a D = ∅ state of U(R) to a state of U(R).
4. (Saturation.) At an all-unsplit state t, W_t(x) = value(r_x) for the simple path r_x from x to λ_W(x) = λ(x) along x's play, so W_t ⊴ B.
   Hence a D = ∅ state with level n − 1 has W_t = B; call such a D = ∅ state SATURATED. Let t be the first saturated D = ∅ state of P (if any) and
   t* the last D = ∅ state of P. For every D = ∅ state t′ ≥ t: Ξ_{t′} = W_{t′} ⊴ B = W_t = Ξ_t ⊴ Ξ_{t′} (R15 (a)), so Ξ_{t′} = B. By R15 (a), Ξ is
   constant (= B) on the states t, …, t*. τ is constant on P, so every transition among these states leaves Ωσ = Ξ and Ωτ unchanged, and R15 (d)
   gives t* − t ≤ 4n(n − 1). So at most 4n(n − 1) + 1 epochs with D = ∅ have a state in [t, t*].
5. (Before saturation.) Consider the D = ∅ epochs E = (x, …, y) with y < t (all D = ∅ epochs, if no D = ∅ state is saturated). Except possibly the
   last epoch of P, each has an in-phase last transition y → y + 1 with source the D = ∅ state y, and distinct epochs have distinct last
   transitions. Such a transition is one of:
   (i) an S4c fallback: at most f;
   (ii) an S4a step from y ∈ U(R) to a state outside U(R) (y is all-unsplit, so y ∈ U(R) for its run R): at most one per run, ≤ f + 1;
   (iii) an S4a step from y into U(R).
   In a run R, after n − 1 steps of kind (iii) (each from a D = ∅ state of U(R) into U(R), so each raises the level by one, by 3), every later
   D = ∅ state of U(R) has level ≥ n − 1, hence is saturated (4), hence is ≥ t. So steps of kind (iii) with source < t number ≤ n − 1 per run,
   ≤ (n − 1)(f + 1) in all. Total before t: ≤ f + (f + 1) + (n − 1)(f + 1) + 1 = (f + 1)(n + 1).
6. Sum of 4 and 5: N_0 ≤ (f + 1)(n + 1) + 4n(n − 1) + 1. The corollary multiplies by EP-0's n + m. □

## 2. Not to sign: what REC-0 does not give (READING)
- It is not free of f. The level of step 3 lives in W and is lost at a fallback (W can drop there) and at a split. The permanent progress measure
  Ξ grows only at D = ∅ → D = ∅ steps, so single-state D = ∅ epochs (epoch exit at once) are charged to W-progress, hence to f.
- Consequences: with RESULTS R56 (f ≤ 1 + (n − 1)(2 + ρ)), N_0 = O(n²(1 + ρ)); on 𝒞^kO with FB-kT (P-N5-FBK, signed by both referees, conditional on
  R56 and P-N5-2T), f = O(n^{k+1}) and N_0 = O(n^{k+2}). So the conjecture REC (docs/new/N5-NEP-box45.md §2) for the configuration C = τ|Q is
  REDUCED to fallbacks per phase; it is not proved outright.
- Not addressed: configurations with |D| ≥ 1 (lane queue: |D| = 1 next), and an f-free form via a permanent Ξ-level.

## 3. DATA (not to sign; experiments/new/box45/)
- rec0.py checks REC-0's inequality per phase and records N_0, f, and the kind-(iii) steps per fallback-free run.
| sample | runs | phases | REC-0 violations | max N_0 (n) | max N_0 / (f + 1) | max kind-(iii) steps in one run | max f |
| --- | --- | --- | --- | --- | --- | --- | --- |
| lib41 (n ≤ 64), S3 + 2 random starts, seed 7 | 1,101 | 5,377 | 0 | 5 (24) | 5.0 | 4 | 33 |
| 3,000 random 𝒞^kO (k 2-4, n 5-18, games seed 111), S3 + 4 random, seed 8 | 15,000 | 40,203 | 0 | 2 (17) | 2.0 | 1 | 1 |
- Climbs (DATA; recclimb.py --d0, hill climbs on (N_0, N_ep) with box43 climb.mutate, S3 start): seeded from experiments/red/so/instances/so_th_n32.pg
  (sha1 ae9126ad…), 1,500 steps, seed 41: (5, 31), no growth; 𝒞^3O, n ≤ 20, 4,000 steps, seed 42: (2, 7); 𝒞^2O, n ≤ 16, 4,000 steps, seed 43: (2, 3);
  𝒞^2O, n ≤ 12, 3,000 steps, seed 33: (1, 4). No instance beyond the library's N_0 = 5. The bound is far above every observed N_0.
- Context (DATA, docs/new/N5-NEP-box45.md §1): the epoch configurations recur inside phases (up to 10 times, lev_l_x.pg), and N_ep is not bounded by the
  number of distinct one-player optima (so_th_n32.pg: 31 epochs, 1 optimum); this packet treats only the configuration τ|Q.
- Reproduce (from experiments/new/box45): `python3 rec0.py 2 7 --list ../box41/lib41.txt`; `python3 rec0.py 4 8 --rand 3000 5 18 111`;
  `python3 recclimb.py 2 32 1500 41 out/climb --d0 --seed ../../red/so/instances/so_th_n32.pg` (and seeds 42, 43, 33 as listed in the README).
