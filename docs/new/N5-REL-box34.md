# N5 on o-cyclic 𝒞^1O, box 34: a coarse freeze that survives θ-changes, w-changes and fallbacks, and what it does to REL and X_SN
L-NEW successor 14 (Opus 5.5, D15/D18). Box 34 GO by the Lead 04:52Z (Lead's stamp). Written 2026-10-25 05:22Z onward by date -u.
- Setting and notation: P-N5-SN (docs/new/P-N5-SN-box33.md §0, pinned 2c70ef6) and its fixes file (frozen at §10): phase (λ_Ξ and τ
  constant), R_k (o's basin under (σ_k, τ)), F_k, θ, w, c_θ, c_w, H1-H3, (h), r_k := lev(θ_k, w_k), relevant changes, ε-transitions,
  absorptions, REL, X_SN, SN prefix (Corollary SN-PREFIX). Levels, COARSE_L, (C1)-(C7): RESULTS R25 / P-N5-FB §1 (P is the rank set;
  lev = top rank of P(x) Δ P(y), −1 = lengths only, ⊥ = equal). R20 (packet P-N5-XA, docs/new/P-N5-XA-box27.md §1-§6) for Lemma C,
  P^c, CR, XA, FBL, FBF. 𝒞^1O: exactly one Odd vertex o with out-degree > 1; every script here asserts it. d_o := |succ(o)|.
  G_τ := the one-player game "Even against the fixed τ" (o forced to t0 := τ(o)); W_k is σ_k's valuation in G_τ.
- Labels (D18/L40): PROVED (L-NEW succ. 14, unrefereed), CONJECTURE, OPEN, DATA, READING. Nothing here is a running-time bound for N5,
  a TARGET.md claim or a step-4 pass. G-N5-TIME stays OPEN.

## Summary
1. **Corollary NL-MF (PROVED; from R29 Lemma NL).** At an S4a step with (h), if r_j exceeds MF_j (the top level of the gates into F_j),
   no vertex leaves R and MF does not rise. So every release needs a gate into F of level ≥ r. DATA: all 46 library releases have one,
   always with a tail in R.
2. **Theorem FREEZE (PROVED).** Inside a phase, if n consecutive states k0, …, k0 + n − 1 all have (h) and r ≤ ℓ, then COARSE_ℓ(Ξ) is
   constant from k0 + n − 1 to the phase's last H2 state, and COARSE_ℓ(W) is constant at those of them with H2. This holds through
   θ-changes, w-changes and fallbacks. It is R20's coarse R17 (P^c / CR) with "θ constant" replaced by "r ≤ ℓ on a window", plus a
   one-line "forever" argument from XW (Ξ ⊴ W) and R15 (Ξ monotone).
3. **Corollary RATCHET (PROVED).** After such a freeze every later H2 state has c_w = c_θ, and (with H1) r ≤ ℓ. COARSE_{ℓ−1}(θ) then
   takes at most 2d_o values and COARSE_{ℓ−1}(w) at most 2, so the later (h) ∧ H1 states fall into ≤ 2d_o + 1 intervals with both
   constant. On an interval where they differ, r = ℓ exactly.
4. **Lemma BLOCK (PROVED).** On such an r = ℓ interval (ℓ ≥ 0), a vertex that leaves R at an S4a step never re-enters R in that
   interval. So in a fallback-free part of the interval each vertex crosses at most twice, and each exit is released at most once.
5. **Theorem X-RUN (PROVED).** In a fallback-free run of a phase whose SN prefix has H1 at every state, the SN prefix has O((d_o + 1)·n³)
   crossing transitions (P-N5-FRZ §6: ≤ 13 (d_o + 1) n³). Hence REL_run, ε_{H1} per run and X_SN per run are polynomial,
   and per phase X ≤ (f + 1)·poly(n) + f on that part. This answers the brief's "bound X_SN or REL" PER FALLBACK-FREE RUN.
6. **What stays open (OPEN, sharpened).** R28's f ≤ n_E(2n − 1)(X + 1) + X and item 5's X ≤ (f + 1)·poly(n) make f and X
   polynomially equivalent per phase. The loop of box 33 §4 is still open, but now it is localized (§6). Theorem FREEZE survives
   fallbacks, so the only crossings not yet bounded at (h) states are re-entries after FALLBACK evictions of level < r inside
   frozen r = ℓ blocks, together with the ¬(h) interruptions of (h)-runs.
7. **Theorem SUB (PROVED) and a refutation (DATA).** R20's Lemma C, P^c, CR and XA hold verbatim on (w, r)-subruns (w and r
   constant, θ free). R20's Lemma FBF does NOT transfer: there are 1,442 entries into R after a fallback inside such subruns (first
   instance b6_xl2_n32). That is the loop in item 6 seen in data.
8. **Climbs (DATA).** Re-release climbs from so_th_n32 (n 32): at most 2 releases of one exit per fallback-free run (24 exits
   re-released), never 3, as item 4 requires. The first REL climb maximised raw REL and hit a degenerate optimum (47 exits leaving R
   together at a phase start): raw REL is ≤ d_o per transition and is not the right fitness.

## 1. Corollary NL-MF (PROVED, L-NEW succ. 14; from R29 Lemma NL)
Statement. Let j → j+1 be an in-phase S4a transition with (h) at j. Put MF_j := the maximal level of a gate (y, z) at j with
z ∈ F_j (MF_j := ⊥ if there is none). If r_j > MF_j, then R_j ⊆ R̄_{j+1} (no vertex leaves R) and MF_{j+1} ≤ MF_j.
Proof. (A_j) of Lemma NL holds for L := MF_j by definition, and r_j > L. NL (ii) gives the first claim. NL (iii) gives (A_{j+1}) for
L, i.e. MF_{j+1} ≤ MF_j. (If MF_j = ⊥ there are no gates into F_j, and (A_j) holds for L = ⊥ < r_j unless r_j = ⊥.) □
- So a release at an (h) S4a step needs r_j ≤ MF_j: some gate into F_j has level ≥ r_j. By OFFGATE (R29), MF_j ≤ M_{j−1}.
- DATA (box34/relfr.py; LIB = box33/lib.txt plus exitr_cex_n48, epsseg_cex_n48 and exitr_cex_n16; data/relfr_lib.txt): 4,084 (h) S4a
  steps, 1,894 with r > MF; there, 0 leaves and 0 MF rises. 46 exit releases: 45 at (h), 1 under ¬(h). Every (h) release has a gate
  into F of level ≥ r with its tail in R (27 with R tails only, 19 with R and F tails). 34 of the 46 are at θ = w (r = ⊥).

## 2. The SN regime as value iteration in G_τ (PROVED, L-NEW succ. 14)
**Fact 0.** At every (h) state of a phase, W's cycle-node map is λ (the phase's honest map). On F, Ξ = W (R19 (a)). On R, c_w = c_θ =
λ(v) (H3; P-N5-SN §3 preamble). So a run of consecutive (h) states is a λ-phase of the one-player game G_τ.
**Lemma ARENA.** At an S4a step from an (h) state k, the arena contains every W-improving edge of G_τ except possibly WITHHELD edges:
(y, z) with y ∈ F_k, z ∈ R̄_k, W_k(z) ▷ W_k(σ_k y), that are not gates. A withheld edge has W-gain level lev(W_k(σ_k y), W_k(z)) ≤ r_k.
Proof. R → R: same order in both frames (R19 (a), (C7)). F → F: Ξ = W. R → F: W_k(z) ▷ π ⊕ w_k ⊵ π ⊕ θ_k, so the edge is a gate.
F → R̄: π_z ⊕ θ_k ⊴ W_k(σ_k y) ◁ π_z ⊕ w_k for a withheld edge, so by (C5), (C6) and (C7) its gain level is ≤ lev(π_z ⊕ θ_k, π_z ⊕ w_k) = r_k. □
- So at θ = w (r = ⊥) nothing is withheld, and the step is a switch-best step of G_τ (R17).
- DATA (box34/snvi.py): in 469 SN prefixes with H1, 3,186 of 4,247 steps have a withheld edge. In the 84 prefixes without one, the
  W-changing steps never exceed |U| − 1 (U := λ^{-1}(c_θ)). The maximum, 55 at n 64 (x32_rand64), sits close to that bound.

## 3. Theorem FREEZE (PROVED, L-NEW succ. 14)
Statement. Fix a phase and a level ℓ ∈ {⊥, −1, 0, 1, …}. Suppose the states k0, …, k0 + n − 1 of the phase all have (h) and r_k ≤ ℓ
(r = ⊥ counts as ≤ ℓ). Put F := k0 + n − 1. Then for every state t ≥ F of the phase up to its last state with H2:
(a) COARSE_ℓ(Ξ_t(x)) = COARSE_ℓ(Ξ_F(x)) for every x;
(b) if t has H2, COARSE_ℓ(W_t(x)) = COARSE_ℓ(W_F(x)) = COARSE_ℓ(Ξ_F(x)) for every x.
Fallbacks are allowed anywhere, both in [k0, F] and after F.
Proof.
- Step 1, Lemma C at level ℓ (statewise). At an (h) state k with r_k ≤ ℓ: COARSE_ℓ(Ξ_k(v)) = COARSE_ℓ(W_k(v)) for all v. On F_k this is
  Ξ = W (R19 (a)). On R̄_k, Ξ_k(v) = π_v ⊕ θ_k and W_k(v) = π_v ⊕ w_k (R19 (a) under (h)), and (C7) gives lev(Ξ_k v, W_k v) = r_k ≤ ℓ,
  i.e. (C2) equality.
- Step 2, Lemma P^c on [k0, F]. This is R20's Lemma P^c (P-N5-XA §5) with COARSE := COARSE_ℓ, and it says: for j ≤ n − 1, every x and
  every simple path r of G_τ with ≤ j edges from x to a vertex u with λ(u) = u, COARSE_ℓ(W_{k0+j}(x)) ⪰ COARSE_ℓ(value(r)). R20's proof
  uses the following facts about consecutive states k, k+1 of the window, and each holds here.
  - (i) Lemma C at k: Step 1.
  - (ii) Monotonicity COARSE_ℓ(W_{k+1}) ⪰ COARSE_ℓ(W_k). At an S4a step this is WM (R23 (g)) with (C1). At a fallback it follows from
    Step 1 at k and at k+1 and Ξ_{k+1} ⊵ Ξ_k (R15 (a)).
  - (iii) Case B_c: a coarse-strict W-improvement (x, z) is a gate. By Step 1, COARSE_ℓ(Ξ_k z) ≻ COARSE_ℓ(Ξ_k σ_k x), so Ξ_k(z) ▷
    Ξ_k(σ_k x) by (C1), (C3). It is also W-improving, so at an S4a step it lies in the arena and (F1) applies (R17).
  - (iv) At a fallback, case B_c is vacuous (R20 N-XA-1). S4a returned σ_k, so σ_k is arena-optimal, and a W-improving arena edge
    would contradict that.
  - (v) The cycle-closing cases B1 (α) and B2 of R17 / R20 need W's cycle-node map constant from k to k+1: Fact 0 at k and k+1.
  - (vi) Base: W_{k0}(u) = (u, ∅, 0) for every honest cycle node u. Under (h), λ(v) = c_θ ∈ F for v ∈ R̄, so u ∈ F, where W = Ξ.
  The coarse facts (Cmono), (Cstrict), (V1c) and (V2c) for COARSE_ℓ are (C1)-(C4) of R25.
- Step 3, upper bound at t. Let t ≥ F have H2. Every vertex's W-play in G_τ ends at its W-cycle node. That node is an honest cycle
  node: on F because W = Ξ there; on R̄ it is c_w, which under H2 lies in F (o's W-play leaves to τ(o) ∈ F and stays in F). So W_t(x)
  is value(r_t) for a simple path r_t of G_τ to an honest cycle node, and Step 2 at j = n − 1 gives
  COARSE_ℓ(W_t(x)) ⪯ COARSE_ℓ(W_F(x)).
- Step 4, sandwich. XW (R21 (a)) gives Ξ_t ⊴ W_t, and R15 (a) gives Ξ_F ⊴ Ξ_t (fallbacks included). So at every H2 state t ≥ F:
  COARSE_ℓ(Ξ_F x) ⪯ COARSE_ℓ(Ξ_t x) ⪯ COARSE_ℓ(W_t x) ⪯ COARSE_ℓ(W_F x) = COARSE_ℓ(Ξ_F x), the last by Step 1 at F. All are equal,
  which is (b) and, at H2 states, (a). At a state t without H2 but before a later H2 state t2 of the phase, monotonicity of Ξ squeezes
  COARSE_ℓ(Ξ_t) between the equal values at F and at t2. □
- Remark. The only new ingredients beyond R20 are: the window hypothesis "r ≤ ℓ" replaces "θ constant" (Step 1 is statewise), and
  Steps 3-4 extend the freeze past the window. Steps 3-4 do not need WM, so they cross fallbacks and w-changes.
- DATA (box34/freeze.py; LIB + experiments/red/*/instances + experiments/si/coarse/instances; data/freeze_lib.txt): 183 freezes,
  3,532 later states checked, 0 failures of (a), (b) or §4's counts. Random C^1O games almost never contain n consecutive (h) states
  (0 freezes in 200 random games at n 5-10). The data is thin; the proof carries the claim.

## 4. Corollary RATCHET and Lemma BLOCK (PROVED, L-NEW succ. 14)
**Corollary RATCHET.** Under Theorem FREEZE's hypothesis, at every H2 state t ≥ F of the phase:
- (a) COARSE_ℓ(θ_t) = COARSE_ℓ(w_t), so c_w = c_θ (H3). With H1, (h) holds and r_t ≤ ℓ.
- (b) If ℓ ≥ 0 and H1 holds at t: COARSE_{ℓ−1}(θ_t) lies in a fixed set of at most 2d_o values, and over all such t it changes at most
  2d_o − 1 times. COARSE_{ℓ−1}(w_t) changes at most once.
- (c) So the H1 ∧ H2 states t ≥ F split into at most 2d_o + 1 maximal intervals (of the time order) on which (COARSE_{ℓ−1}θ,
  COARSE_{ℓ−1}w) is constant. On an interval where the two differ, r = ℓ. On the others, r ≤ ℓ − 1.
Proof.
- (a) is FREEZE (b) at x = o, together with (C2), plus H3H2 (P-N5-SN §4) for (h).
- (b), θ. Under H1, σ̄_t(o) ∈ F_t, its honest path avoids o, and θ_t = o ⊕ Ξ_t(σ̄_t(o)) ((P2) at o). So COARSE_{ℓ−1}(θ_t) =
  o ⊕ COARSE_{ℓ−1}(Ξ_t(x)) with x = σ̄_t(o) ∈ succ(o) ((C4)). For each exit x, COARSE_ℓ(Ξ(x)) is frozen (FREEZE (a)). Then
  COARSE_{ℓ−1}(Ξ(x)) is decided by one more rank, ℓ, so it takes 2 values, and it is monotone (R15 (a), (C1)); it takes them in order.
  That gives ≤ 2d_o candidate values for COARSE_{ℓ−1}(θ). θ is monotone, so COARSE_{ℓ−1}(θ) changes at most 2d_o − 1 times.
- (b), w. Under H2, τ(o) ∈ F, so w_t = o ⊕ Ξ_t(τ(o)) (R19 Lemma Wo; τ is fixed in the phase). Ξ_t(τ(o)) is monotone with frozen
  COARSE_ℓ, so COARSE_{ℓ−1}(w) changes at most once.
- (c) follows from (a) and (b): the pair determines whether lev(θ, w) ≥ ℓ, and (a) caps it at ℓ. □
**Lemma BLOCK.** Let ℓ ≥ 0 and let I be an interval of (c) on which the pair differs (r = ℓ), consisting of consecutive (h) states.
If v leaves R at an S4a step s → s+1 inside I, then v ∉ R_t for every later t ∈ I.
Proof.
- Write A_v := COARSE_ℓ(W(v)) (frozen by FREEZE (b)), and u_ℓ for the rank-ℓ vertex. u_ℓ ∈ P(θ) Δ P(w) and θ ◁ w, so w is on the good
  side at u_ℓ. u_ℓ lies on no route π_v (R19 (a); REFEREE's note on Lemma G (b)).
- For v ∈ R_t at t ∈ I: Ξ_t(v) = π_v ⊕ θ_t, with COARSE_ℓ equal to A_v (it equals COARSE_ℓ(π_v ⊕ w_t) by (C7)). Its rank-ℓ bit is
  θ_t's, the bad one, so COARSE_{ℓ−1}(Ξ_t v) = (A_v, bad).
- At the leave: Ξ_{s+1}(v) = W_{s+1}(v) (R19 (a)) ⊵ W_s(v) = π_v ⊕ w_s (WM). Its COARSE_ℓ is A_v (frozen), so its rank-ℓ bit is w's, the
  good one: COARSE_{ℓ−1}(Ξ_{s+1} v) = (A_v, good).
- A re-entry at t > s in I would give COARSE_{ℓ−1}(Ξ_t v) = (A_v, bad) ≺ (A_v, good), against R15 (a). □
- Consequences on a fallback-free part of I: every vertex crosses R at most twice (at most one entry before its one S4a leave), so
  there are ≤ 2n crossing transitions. Every exit of o is released at most once, so the part contributes ≤ d_o to REL.
- With fallbacks inside I, a FALLBACK eviction of v at level < ℓ (CLU: levels ≤ r = ℓ) keeps v's bit bad, and v may come back. That
  is the residue of §6.
- ℓ = −1: COARSE_{−1} = (c, P), and after its freeze θ, w and every Ξ(x) can still change only in their length. Ξ(x) then takes ≤ n
  values in order, so θ takes ≤ d_o·n values and w ≤ n. A re-entry after an S4a leave is a strict Ξ(v) increase (Ξ_{E+1}(v) ⊵
  Ξ_{s+1}(v) ⊵ π_v ⊕ w ▷ π_v ⊕ θ_s = Ξ_s(v)), so each vertex re-enters ≤ n − 1 times after its freeze.
- ℓ = ⊥ (θ = w on the window): FREEZE freezes Ξ and W completely. A later S4a step at θ = w with a gate would strictly raise W at the
  switched vertex (R17 (F1)), so there is none: no Even switch, no crossing, until θ ≠ w.

## 5. Theorem X-RUN (PROVED, L-NEW succ. 14)
Statement. Let Q be a fallback-free run of a phase. Suppose its SN prefix P (Corollary SN-PREFIX) has H1 at every state. Then the
crossing transitions inside P number O((d_o + 1) n³) (≤ 13 (d_o + 1) n³). Packet P-N5-FRZ §6 governs; there the ℓ = −1
and ⊥ levels cost n³, and the count below is superseded. In particular:
- REL_Q ≤ d_o times that (every release is in P: R-STICK);
- ε_{H1}(Q) ≤ d_o + REL_Q (ABS-COUNT in its signed form; d_o − 1 + REL_Q when Q's last H1 ε-transition has O ≥ 0, ABS-COUNT′);
- by SN-PREFIX, Q has at most n − 1 more crossings after P.
Proof. Every state of P has (h) (H3H2). Write ℓ_0 := max_{k ∈ P} r_k. The first n − 1 transitions of P are a window at ℓ_0, which
gives F(ℓ_0) := k_P + n − 1 (FREEZE). Induct downward on the level ℓ, with F(ℓ) the first freeze time at ℓ:
- After F(ℓ), the states of P fall into ≤ 2d_o + 1 intervals (RATCHET (c)).
- r = ℓ intervals: ≤ 2n crossing transitions each (BLOCK; Q is fallback-free).
- r ≤ ℓ − 1 intervals: all those of length < n − 1 before the first one of length ≥ n − 1 have < n − 1 transitions each. The first
  long one gives F(ℓ − 1) after n − 1 transitions, and from then on the analysis at ℓ − 1 covers the rest of P.
- So [F(ℓ), F(ℓ − 1)) contains ≤ (2d_o + 1)·2n + (2d_o + 2)(n − 1) ≤ 6(d_o + 1)n crossing transitions.
- Levels range over ranks and −1: ≤ n + 1 of them, bounded by 2n + 2 above.
- Below ℓ = 0: the ℓ = −1 analysis of §4 gives ≤ 2n(n + 1) vertex crossings after F(−1) at r = −1 states. The ≤ d_o·n + n intervals
  with θ = w before F(⊥) are short (< n − 1 transitions each). After F(⊥) there is no crossing (§4, ℓ = ⊥).
- If some F(ℓ) never happens, the remaining states lie in ≤ 2d_o + 1 intervals of the level above, and the same counts apply. □
- Reading against the brief. X_SN per fallback-free run (on its H1 part) and REL per run are now polynomial. Per phase they are
  (f + 1)·O((d_o + 1)n³) and d_o·(f + 1)·O((d_o + 1)n³). The ¬H1 SN states (329 steps in the library, prefix_nonh_steps) are not
  covered: LEAVE and H3H2 need H1.
- Phase-level corollary (READING, from R27 Corollary LP′ / R28 Corollary OX): on o-cyclic 𝒞^1O with H1 on every SN prefix, a phase
  makes poly(n)·(1 + f + K) transitions. Here f is the number of fallbacks of the phase and K the number of wakes.

## 6. What is still open, localized (OPEN; READING where marked)
- The loop. R28: f ≤ n_E(2n − 1)(X + 1) + X. §5: X ≤ (f + 1)·poly(n) + f on the H1 part. So per phase f and X are polynomially
  equivalent, and neither is bounded. Box 33 §4's loop (absorb, fall back, release) is exactly this.
- Where it lives (READING, from FREEZE's survival across fallbacks). At (h) states, every crossing outside the two mechanisms below
  is already polynomial per maximal (h)-run (§5's count with fallbacks allowed: RATCHET and FREEZE hold through fallbacks; BLOCK
  covers S4a leaves).
  - (L1) Re-entries after FALLBACK evictions of level < ℓ inside frozen r = ℓ blocks (BLOCK's residue). R20's FBF forbids them only
    for θ constant; with θ moving below ℓ they occur (§7).
  - (L2) Interruptions of (h)-runs by ¬(h) states. Each one can restart a short window. After a freeze, every H1 ∧ H2 state is (h)
    (RATCHET (a)), so after the first freeze the only interruptions are ¬H1 or ¬H2 states.
- What would close (L1) (OPEN): a count of fallback evictions at levels < r inside one frozen block that does not go through
  re-entries. CLS1 (R29) gives monotone fallback levels along a scope run. L-SI's open per-level count (CL-S, second half) is that
  count.

## 7. Theorem SUB (PROVED) and the failure of FBF with θ moving (DATA)
- (w, r)-SUBRUN: a maximal run of states of one phase with (h), w and r = lev(θ, w) constant; θ may change.
- **Theorem SUB (PROVED, L-NEW succ. 14).** On a (w, r)-subrun with r = ρ ≥ 0, R20's Lemma C, P^c, CR (coarse values constant from n − 1
  transitions on) and Theorem XA (a re-entry after an S4a leave is a strict coarse increase; ≤ n(n − 1) such re-entries) hold with
  θ_k in place of θ. The proof is R20 §2, §5, §6 verbatim. There u* = the rank-ρ vertex is the same at every state, since lev(θ_k, w) = ρ
  for all k, and every use of θ is statewise:
  - Lemma C: P(θ_k) and P(w) agree above ρ;
  - XA step 4: u* is the top of P(θ_{E+1}) Δ P(w) and w is better there.
  For ρ = −1: C, P^c and CR hold (R20 remark), and a re-entry after an S4a leave is a strict Ξ increase. SUB is the special case
  ℓ = ρ of FREEZE on windows inside one subrun.
- **FBF does not transfer (DATA, box34/rsubfb.py, out/ log in this commit's data list).** R20's FBF proof step 2 uses "same path, same
  θ ⇒ same Ξ". With θ rising below ρ, entries after a fallback occur: 1,442 entries after the subrun's first fallback, over 368
  throttled subruns. First example: experiments/n5-exhaustive/instances/b6_xl2_n32.pg (sha1 909c7371…), subrun from state 4, first
  fallback 18, one entry after it.
- Same data: 0 failures of CR (coarse changes after transition n − 2 of a subrun) and of XA′ (123 re-entries checked). θ changes up to
  48 times inside one subrun (x31_rx32, n 32, sha1 4fe9ec0e…, r = 30 throughout states 2-53, with 3 fallbacks); non-flat fallbacks up
  to 33 in one subrun (ccl_w48_n48).

## 8. Data and climbs (DATA; experiments/new/box34; out/ is gitignored)
- Logs: data/relfr_lib.txt, data/snvi_lib.txt, data/rsub_lib.txt, data/rsubfb_lib.txt, data/freeze_lib.txt, data/rerel_lib.txt.
- relfr.py (NL-MF, §1); snvi.py (withheld edges, §2); rsub.py, rsubfb.py (SUB, FBF, §7); freeze.py (FREEZE, RATCHET counts, BLOCK
  on fallback-free intervals: 26 intervals, 0 failures); exittrace.py (per-transition exit trace); rerel.py (releases per exit per
  run / phase; library maximum 2, so_th_n32, 4 cases).
- Climbs (relclimb.py; 4 × ≤ 50 min, seeds so_th_n32 / exitr_cex_n48 / epsseg_cex_n48 / lev_l_n28):
  - fitness "max releases of one exit in one fallback-free run": stays at 2, with up to 24 re-releases in total at n 32;
  - fitness "raw REL per phase": degenerate optimum, 47 exits leaving at one transition at a phase start (≤ d_o per transition).
- wsnclimb.py (w-changes between (h) states in one phase, seeds sc24 / sc32): 21 at n 24 (sc24 starts at 20: an unthrottled, R17-type
  run with R mostly empty) and 17 at n 32. Both are below n.
- Every named instance above has exactly one Odd vertex with out-degree > 1; the scripts assert it.

## 9. The loop inside a scope run: drain and refill (DATA, READING; written 05:47Z by date -u)
- Mechanism (DATA, box34/fbclus.py). x48_rt48_final.pg (experiments/new/box28/instances, sha1 cff46249…, n 48, d_o 3) has one scope run,
  states 2-111, with r = 47 until 99:
  - Refill: R grows one vertex per S4a step (states 2-18, 63-82).
  - Drain: fallbacks at one level evict R in pieces, with no entry in between (level 45 at 19, 25, 31, 41, 46, 53, 55, 59, 61; level
    44 at 83-97).
  - Then θ rises at exactly the drain level (45 at 62, 44 at 98), R refills, and the next drain is one level lower (CLS1).
  - At 99 θ jumps to level 47 = r: the run's θ catches w.
  b6_xw_n56.pg (sha1 in data/fbentry_lib.txt) shows the same pattern with levels 43, 42, 41, 41, 41, 40, 39, 39, 36.
- So "≤ 1 fallback cluster per level per scope run" (CL1) is FALSE: 47 scope runs violate it, up to 9 clusters at one level
  (x48_rt48_final). But the repeated clusters at one level are drains: R only shrinks between them, so one drain has ≤ |R| ≤ n
  non-flat fallbacks.
- E1 (PROVED, it is R20's FBF): inside a scope run, no vertex enters R after a fallback until θ changes. w is fixed in a scope run, so
  the stretch after the fallback is a (θ, w)-stretch until θ moves, and FBF applies. DATA: 1,874 entries after fallbacks in scope
  runs, each preceded by a θ-change since the last fallback (box34/fbenter.py).
- READING (FBL needs u* ≠ none, i.e. r ≥ 0): per scope run, non-flat fallbacks ≤ n·(1 + number of θ-changes in the run). Between two θ-changes, after the first fallback R only shrinks (E1), and each non-flat THR fallback evicts a vertex (FBL). With item 6 of the
  Summary, per scope run the open count is the θ-changes after fallbacks (L-SI's "θ per scope run", P-N5-CLS §7). In the data they come
  at the drain level (93 of the 394 transitions right after a cluster change θ at exactly the cluster level; the other 301 do not; data/fbclus_lib.txt).

## 10. (L2): how (h)-runs end and restart; ¬H1 SN states (written 06:05Z onward by date -u)
**Lemma H3-CONST (PROVED, L-NEW succ. 14).** In a phase, at every H2 state c_w = λ(τ(o)). So H3 holds at all H2 states of the phase or at
none. If the phase has one (h) state, then at every state of it (h) ⟺ H1 ∧ H2.
Proof. Under H2, τ(o) ∈ F, and o's W-play continues along τ(o)'s W-play, which stays in F, where W = Ξ (R19 (a)). So c_w = τ(o)'s W-cycle
node = λ(τ(o)). τ and λ are constant in a phase, and so is c_θ = λ(o). □
- This gives RATCHET (a)'s "c_w = c_θ at H2 states" without a freeze.
**Lemma H2-STICK (PROVED, L-NEW succ. 14).** At an S4a transition s → s+1 of a phase with H1 and ¬H2 at s, ¬H2 holds at s+1.
Proof.
- ¬H2: τ(o) ∈ R_s. Its W-cycle node is c_w(s), the top of o's W-cycle, which passes o, so c_w(s) ∈ R̄_s.
- λ(τ(o)) = c_θ: τ(o)'s honest play agrees with its (σ, τ)-play up to o. Under H1, c_θ ∈ F_s (Fact 0's argument uses only H1).
- So the two cycle nodes differ, and R30 (c) R-STICK keeps τ(o) in R_{s+1}. □
- So inside a phase with H1 throughout, the (h) states of each fallback-free run form a prefix of the run. An (h)-run can restart only
  at a fallback, or after a state without H1.
**CONJECTURE ONE-H ("the (h) states of a phase are consecutive"): FALSE.**
- Instance: experiments/new/box34/instances/oneh_cex_n32.pg (sha1 51dab08664031c9d34b38de04ba99f255926e14b; n 32, o = 27, d_o 4; climb
  hrclimb.py from u1flat_best_n32).
  - Verified: n5.py n5 gives 3 iterations, 1 fallback; check_sol2.py gives "zielonka(oink zlk) OK strategies verified"; exactly one
    Odd vertex with out-degree > 1.
  - The phase is states 1-3. State 1 is (h), with R = {19}. State 2 is ¬H1 ∧ ¬H2 ∧ H3: R̄ is everything, both cycles pass o, and
    their common top is c_θ = c_w = 13. The fallback 2 → 3 returns to (h), with R = {19}.
- Also a random game (seed 3461, game 2863 of 30,000 at n 5-14) has 2 (h)-runs in one phase. Library: max 1 (h)-run in each of
  1,272 phases (data/hruns_lib.txt).
- The interruptions seen: 36 in the library, 107 in the random sample. All are ¬H2 (with ¬H3 or with ¬H1); none is ¬H1 with H2.
**Lemma G′ (PROVED, L-NEW succ. 14): the frames at an H3 state without H1.** Let k be a phase state with H3 and ¬H1, and put c := c_θ = c_w.
- Then ¬H2, and c ∈ R̄_k: o lies on its honest cycle, whose vertices all reach o; H2 would put c_w in F.
- For v ∈ R̄_k, call v c-FIRST if its (σ_k, τ)-play reaches c before o, and o-FIRST otherwise (o itself is o-first).
- c-first v: Ξ_k(v) = W_k(v), the value of the same path v ⇝ c.
- o-first v: Ξ_k(v) = π_v ⊕ θ_k and W_k(v) = π_v ⊕ w_k. Here π_v is v's route to o. It is disjoint from both paths of o and from c:
  meeting σ̄(o)'s or τ(o)'s path to c would make v c-first.
- On F_k, Ξ = W (R19 (a)). Hence lev(Ξ_k v, W_k v) ≤ r_k := lev(θ_k, w_k) for all v, by (C7).
**Theorem FREEZE′ (PROVED, L-NEW succ. 14; no data, see below).** Theorem FREEZE (P-N5-FRZ §3) holds with "(h)" replaced by "H3" in the
window, and "H2" replaced by "H2 or H3" in (b) and in its range.
Proof. Read P-N5-FRZ §3 with these changes.
- Step 1 at H3 states without H1 is Lemma G′.
- Fact 0 at H3 states: the W-cycle node of v ∈ R̄ is c_w = c_θ = λ(v). Honest cycle nodes are in F, or (¬H1) equal c, whose W-value
  is (c, ∅, 0) because c tops its W-cycle. That covers the base and the cases of P^c that use Fact 0.
- Step 2: WM and R15 (a) as before.
- Step 3 needs c_w to be an honest cycle node. That holds under H2 (c_w ∈ F) and under H3 (c_w = c_θ = λ(o)). □
- DATA: none. No window of n consecutive H3 states containing a ¬H1 state occurs in the library (MODE=H3 freeze.py gives the same 183
  freezes, all (h) windows; data/freezeH3_lib.txt) or in 20,000 random games at n 4-9.
- OPEN: RATCHET and BLOCK at ¬H1 SN states. A c-first vertex has Ξ = W, so BLOCK's "BAD bit in R" fails for it; re-entries as c-first
  vertices are not excluded. Under ¬H1, θ = o ⊕ Ξ(σ̄(o)) with σ̄(o) c-first (if c ≠ o), so RATCHET (b)'s counting of θ still applies.
- So for (L2) the restart mechanisms are: (i) a fallback at a ¬H2 state that takes τ(o) out of R; (ii) a passage through ¬H1 ∧ ¬H2 ∧ H3
  states (oneh_cex_n32). FREEZE′ already covers windows through (ii). (i) remains OPEN.
- (Superseded by §11: at ¬H1 states R̄ is a phase constant, so the c-first re-entry concern above does not arise between ¬H1 states.)

## 11. ¬H1 states: R is constant there, and they sit in one interval (written 06:15Z onward by date -u)
**Lemma R-CONST (PROVED, L-NEW succ. 14).** Let U := λ^{-1}(c_θ), a phase constant. At every ¬H1 state k of the phase, R̄_k = U.
Proof.
- (⊆) For v ∈ R̄_k, v's honest play agrees with its (σ_k, τ)-play up to o (on 𝒞^1O the graphs differ only at o). Then it follows o's
  honest play, so λ(v) = λ(o) = c_θ.
- (⊇) Let λ(v) = c_θ. In the functional graph H_k, the cycle that contains c_θ is unique. Under ¬H1 it is o's honest cycle, since o
  lies on its own honest cycle and that cycle's top is λ(o) = c_θ.
  - So v's honest play enters that cycle and passes o.
  - Up to that first visit of o it equals the (σ_k, τ)-play, so v ∈ R̄_k. □
- Corollary: a transition between two ¬H1 states of a phase is never a crossing. In the SN regime the ¬H1 states cost crossings only
  at the transitions where H1 changes. (This answers §10's OPEN item on BLOCK at ¬H1 SN states: no BLOCK is needed there.)
**Lemma H1-INT (PROVED, L-NEW succ. 14).** In a phase, the states with P(θ) = ∅ form one interval I_∅ (in time). Every ¬H1 state, and
every state k with H1 at k and ¬H1 at k+1, lies in I_∅. On I_∅, θ = (c_θ, ∅, ℓ_k) changes only in its length, so it changes at most n − 1
times there.
Proof.
- Interval. θ is non-decreasing (R15 (a)) with constant cycle node. VJ00's order compares path sets before lengths, by the signed
  weight Σ ±2^rank, which is injective, with weight(∅) = 0.
  - So for a < k < b with P(θ_a) = P(θ_b) = ∅: 0 ≤ weight P(θ_k) ≤ 0, hence P(θ_k) = ∅.
- ¬H1 states. θ is o's value on its own honest cycle: the path from o to the top c_θ along the cycle. Every vertex of that cycle
  other than c_θ is less relevant than c_θ, so P(θ) = ∅ (also if c_θ = o).
- States before a drop: R30 (f) H1-DROP gives P(θ_k) = ∅.
- Lengths. A length lies in [0, n − 1], and θ is monotone, so its length moves in one direction. □
**Theorem X-RUN′ (PROVED, L-NEW succ. 14): X-RUN without the H1 hypothesis.** Let Q be a fallback-free run of a phase and P its SN prefix.
Let t_Q be the number of transitions of P at which H1 changes. Then P has at most 13 (d_o + 1) n³ (t_Q + 1) + t_Q crossing transitions.
Proof.
- Split P into maximal runs of H1 states and of ¬H1 states. There are ≤ t_Q + 1 runs of each kind.
- Inside a ¬H1 run there is no crossing (R-CONST). The H1-changing transitions contribute ≤ t_Q.
- An H1 run of P consists of consecutive (h) states of a fallback-free run (H1 ∧ H3 ⇒ (h), R30 (d)). The proof of X-RUN (P-N5-FRZ §6)
  uses only that: its windows, RATCHET, BLOCK and the level count all take place inside a run of consecutive (h) states without
  fallbacks. So it gives ≤ 13 (d_o + 1) n³ per H1 run. □
- So X_SN per fallback-free run is polynomial in n and the H1-toggles of its SN prefix. All ¬H1 states of the phase, and every state
  just before a drop, lie in the single interval I_∅ (H1-INT).
**CONJECTURE ONE-DROP (OPEN; DATA).** In a phase there is at most one transition from H1 to ¬H1.
- DATA (box34/h1tog.py):
  - library + experiments/red + experiments/si/coarse + oneh_cex_n32: 1,274 phases, 1,043 ¬H1 states, max 1 drop and max 2 H1-toggles
    per phase (b4_n5_other_0, n 5);
  - random: 20,000 games at n 4-14 (seed 3481), 40,037 phases, 23,308 ¬H1 states, max 1 drop, max 1 toggle per phase;
  - R-CONST and the I_∅ interval: 0 failures in all of it (data/h1tog_lib.txt).
- With ONE-DROP, t_Q ≤ 2 per phase, and X-RUN′ gives X_SN ≤ (f + 1)·poly(n) per phase with no hypothesis on H1.

## 12. What remains open of (L2) if ONE-DROP holds (for the Lead's next packet; written 06:58Z by date -u)
Assume CONJECTURE ONE-DROP (§11) together with X-RUN′ (§11, lane PROVED). Then:
- Settled, per fallback-free run Q:
  - P (Q's SN prefix) has at most 3 H1-runs: one drop, at most one regain before it and one after it.
  - So X_SN(Q) ≤ 3·13(d_o + 1)n³ + 2, and REL_Q ≤ d_o(X_SN(Q) + 1) (FRZ-3), with no H1 hypothesis.
  - Per phase: X ≤ (f + 1)(39(d_o + 1)n³ + n + 2) + f.
- What is left of (L2), as a list:
  1. ONE-DROP itself (CONJECTURE). DATA:
     - library, experiments/red and experiments/si/coarse (1,274 phases): max 1 drop per phase, max 2 H1-toggles;
     - random (40,037 phases): max 1 drop per phase, max 1 H1-toggle;
     - climbs dropclimb.py: max 1 drop per phase, up to 3 H1-toggles (result line below).
     Known facts that a proof can use (all lane PROVED, §11): every drop starts in the P(θ) = ∅ interval I_∅ (R30 H1-DROP + H1-INT); on
     I_∅, θ = (c_θ, ∅, ℓ) changes only in length; at ¬H1 states R̄ = λ^{-1}(c_θ) (R-CONST).
  2. Restart mechanism (i): a fallback at an H1 ∧ ¬H2 state that moves τ(o) out of R, after which (h) returns by H3-CONST. OPEN, never seen
     (0 cases in the library, the random sample and the hrclimb.py climbs). H2-STICK rules it out at S4a steps.
  3. Restart mechanism (ii): (h) → ¬H1 ∧ ¬H2 ∧ H3 → (h). It costs no crossing inside the ¬H1 part (R-CONST). Under ONE-DROP it happens at
     most once per phase. Both observed restarts are of this kind: oneh_cex_n32 (back through a fallback) and the random game seed 3461 /
     2863 (n 12, states 0-2, back through S4a steps).
  4. Short (h)-runs (fewer than n states) never contain a FREEZE window. They cost ≤ n transitions each, so ≤ n per restart. Items 2-3
     bound how many there are.
- Not part of (L2), and still the real core (OPEN): the f-dependence. X-RUN′ is per fallback-free run. Across fallbacks, FREEZE and
  RATCHET survive, but BLOCK covers only S4a leaves. What remains is (L1): re-entries after fallback evictions below r inside frozen
  r = ℓ blocks. Inside a scope run these equal the θ-changes after fallbacks (§9). With (L1) bounded and items 1-2 settled, per phase X
  would be poly(n), and then f and J are poly(n) as well (R28 Corollary OX). Together with K, that would make a phase polynomial
  (R27 Corollary LP′).

## 13. ONE-DROP is FALSE; what survives (written 07:31Z by date -u)
- DEAD END: CONJECTURE ONE-DROP (§11) is FALSE.
  - Instance: experiments/new/box34/instances/onedrop_cex_n32.pg (sha1 5793d5a3303fd8c180dd7d0b8105e2d6961af1cd; n 32, o = 27,
    succ(o) = {3, 17}; climb dropclimb.py seed 3502 from oneh_cex_n32).
  - Verified: n5.py n5 gives 6 iterations, 1 fallback; check_sol2.py gives "zielonka(oink zlk) OK strategies verified"; exactly one
    Odd vertex with out-degree > 1.
  - The phase is states 2-6, with c_θ = 13. H1 at 2, ¬H1 at 3 (|R| 31), H1 at 4-5, ¬H1 at 6. The drops are 2 → 3 (an S4a step) and
    5 → 6 (an S4c fallback).
  - θ = (13, ∅, 10) at 2-3 and (13, ∅, 8) at 4-6: θ changes in length between the two drops, inside I_∅ (H1-INT).
- What survives (CONJECTURE DROP-LEN, OPEN): between two drops of a phase, θ changes. With H1-INT (θ changes ≤ n − 1 times on I_∅), that
  would give ≤ n drops per phase, ≤ 2n + 1 H1-toggles, and, via X-RUN′, X_SN ≤ (f + 1)(2n + 2)·13(d_o + 1)n³ + 2n + 1 per phase with no
  H1 hypothesis. A weaker form that is also open: at most one drop per fallback-free run (here the second drop is at a fallback).
- §12's item 1 now reads "DROP-LEN (or one drop per fallback-free run)", and its per-phase bound "3 H1-runs" reads "≤ 2(drops) + 1".
  Item 3 (restarts through ¬H1 states) becomes ≤ the number of drops per phase. DATA: climbs dc4 (b4_n5_other_0, 10.9M steps) and dc6
  (so_th_n32): max 1 drop per phase; dc5: 2.
