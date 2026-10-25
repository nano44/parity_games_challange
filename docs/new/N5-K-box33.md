# N5 on o-cyclic 𝒞^1O, box 33: what the X-charged carries and the wakes are made of
L-NEW successor 13 (Opus 5.5, D15/D18). Box 33 GO by the Lead 02:06Z (Lead's stamp). Written 2026-10-25 02:28Z onward by date -u.
- Setting and notation: P-N5-LP §0-§1 (phase = λ_Ξ and τ constant; relevant changes; used level L_k; rises; wakes; K), P-N5-OE (E_k, O_k,
  Lemma U-loc, Lemma OE, Corollary OX) with its fixes file docs/new/P-N5-OE-fixes-box32.md. 𝒞^1O: exactly one Odd vertex o with
  out-degree > 1; every 𝒞^1O instance below was checked for that. d_o := |succ(o)|. An ε-TRANSITION is a phase transition with O_k > E_k
  (Theorem LP's ε; on 𝒞^1O exactly the transitions whose used level is attained only by σ̄(o)).
- Labels (D18/L40): PROVED (by whom; unrefereed unless said), CONJECTURE, OPEN, DATA, READING. Nothing here is a running-time bound, a
  TARGET.md claim or a step-4 pass. G-N5-TIME stays OPEN.

## Summary
1. **Lemma OR (PROVED, L-NEW succ. 13).** At every ε-transition the old exit x0 = σ̄_k(o) is rerouted through o (x0 ∈ R_{k+1}); under H1
   it was in F_k, so the transition is a crossing that ABSORBS the current minimiser exit into R; and θ rises at exactly the level O_k.
2. **What X is charged for (DATA, 234-file library).** All non-tame transitions (235) and 146 of the 148 rises with a crossing in their
   interval are ε-transitions (O-rises); the other 2 are Even-attained R → R rises. Every one is an H1 → H1 S4a step. So the "weaker X
   target" of the Lead's brief is, in the data, the count of exit absorptions plus 2 rises.
3. **CONJECTURE EXIT-R (0 failures on 279 ε-transitions).** An exit absorbed at an ε-transition stays in R until the next fallback
   transition or the end of the phase. With Lemma OR it gives ε ≤ (d_o − 1)(f + 1) per phase (under H1), hence J ≤ ε ≤ (d_o − 1)(f + 1).
   Absorbed exits that do leave R leave only at (tame) fallbacks: 37 of 37.
4. **The loop that remains (OPEN).** R25 Theorem FB gives f ≤ n_E(2n − 1)(J + 1) + J, and EXIT-R gives J ≤ (d_o − 1)(f + 1). The two are
   circular. A bound on either side per phase, from something other than the other, closes the X-charged carries.
5. **Lemma WK (PROVED, L-NEW succ. 13, from RESULTS R24 Lemma R / TB).** At a wake y: a → z whose W-cycle node is odd and y is not its own
   W-cycle node, W changes at a or at z (both in R) at the same transition. So in the odd mode every wake is a transition with a W-change
   on R; wakes with W unchanged at a and z exist only in the BFS (even) mode.
6. **K data.** The library (234 files) has 1 wake (nowake_cex_n32). Three wake climbs (box33/kclimb.py, ~9·10⁴ candidates each so far)
   reach K = 2 in one phase (consecutive transitions, rising wake levels 26 → 29), never more. Every wake seen is in U3 / U23 with
   c_w the top-rank vertex (the length-only band of Lemma KW-LEN), BFS mode.

## 1. Lemma OR (PROVED, L-NEW succ. 13; 𝒞^1O; inside a phase)
Statement. Let k → k+1 be a phase transition with O_k > E_k. Put c := λ(o) (≠ o: O_k is defined only then), x0 := σ̄_k(o),
x1 := σ̄_{k+1}(o), ℓ := O_k = lev(Ξ_k(x0), Ξ_k(x1)). Then
- (a) x0's H_{k+1}-path to c visits o; hence x0 ∈ R_{k+1};
- (b) under H1 at k, x0 ∈ F_k: k is a crossing at which x0 joins R;
- (c) lev(θ_k, θ_{k+1}) = ℓ and θ_{k+1} ▷ θ_k.
Proof.
- (a) Suppose x0's H_{k+1}-path before c avoids o. Its vertices other than Even ones are forced Odd vertices (𝒞^1O), so every relevant
  change on it is Even, of level ≤ E_k. Lemma U-loc with L = E_k: COARSE_{E_k}(Ξ_{k+1}(x0)) = COARSE_{E_k}(Ξ_k(x0)). x1's H_{k+1}-path avoids
  o (Lemma OE step 2: H_{k+1} is functional and x1 = σ̄_{k+1}(o), so a visit of o would return to x1 before c), so likewise
  COARSE_{E_k}(Ξ_{k+1}(x1)) = COARSE_{E_k}(Ξ_k(x1)). By CAP-1 (full minimiser when λ(o) ≠ o; R-N5-FB §4.2, R2-N5-FB §C.3) Ξ_k(x0) ◁ Ξ_k(x1),
  and lev = ℓ > E_k, so by (C2), (C1) their COARSE_{E_k} values differ in the same strict order; these are the values at k+1, so by (C1),
  (C3) Ξ_{k+1}(x0) ◁ Ξ_{k+1}(x1), against CAP-1 at k+1 (x1 is a full minimiser). Hence the path visits o. On 𝒞^1O the H_{k+1}-graph and the
  (σ_{k+1}, τ)-graph agree everywhere except at o, so x0's (σ_{k+1}, τ)-play follows the same path up to o: x0 ∈ R_{k+1}.
- (b) H1 at k: o lies on no honest cycle. x0's H_k-play is the tail of o's (x0 = σ̄_k(o)); a visit of o would put o on its own honest
  cycle. So x0's (σ_k, τ)-play equals its H_k-play and avoids o: x0 ∈ F_k (P-N5-OE-fixes §4).
- (c) θ_k = o ⊕ Ξ_k(x0), θ_{k+1} = o ⊕ Ξ_{k+1}(x1) ((P2) at o, λ(o) ≠ o). Ξ_{k+1}(x1) has the COARSE_{E_k} of Ξ_k(x1) ((a)), and for two
  values of cycle node c the level and direction of a difference above E_k are functions of their COARSE_{E_k} values (P-N5-LP Lemma HI,
  second bullet). So lev(Ξ_k(x0), Ξ_{k+1}(x1)) = ℓ and Ξ_{k+1}(x1) ▷ Ξ_k(x0). Prefixing o keeps level and direction: o lies on neither
  path (x1's H_{k+1}-path avoids o by (a)'s argument; x0's H_k-path to c avoids o, under H1 by (b) and under ¬H1 because x0 lies on o's
  honest cycle after o and reaches c before returning to o), so o is added to both path sets or to neither, and both lengths grow by 1. □
- Remarks. (a) and (c) do not use H1. Under ¬H1 at k, x0 ∈ R_k already, and k is a crossing by Lemma OE. ℓ = −1 is allowed in (c) (then
  E_k = ⊥ and only lengths differ).
- Reading: an ε-transition is an ABSORPTION: Even's S4a step routes the current minimiser exit through o (data: by a switch on x0's new
  route, at an S4a step, in all 279 cases), so Odd's honest reply moves to the next exit, and θ = Ξ(o) rises at that exit's level.
  jcl_zcl_cu_n48 (J 17 = X 17 = ε 17) is this, cleanly: in its long phase σ̄(o) walks through 17 of its 18 exits, absorbing each into R;
  R grows from 1 to 41 vertices, and no exit ever leaves R.

## 2. CONJECTURE EXIT-R and its consequence
Statement (CONJECTURE). If k is an ε-transition with old exit x0, then x0 ∈ R_t for every t from k+1 up to the next fallback transition
of the phase (or the end of the phase).
Consequence (PROVED from EXIT-R, L-NEW succ. 13). Under H1 every σ̄(o) lies in F ((b)'s argument at every state), so an exit in R is not
σ̄(o). Between two fallbacks, each ε-transition under H1 absorbs a distinct exit (EXIT-R), and one exit stays in F; so there are
≤ d_o − 1 of them per fallback-free segment, and ε_{H1} ≤ (d_o − 1)(f + 1) per phase. With Corollary OX's proof of (ii), J ≤ ε.
DATA (box33/orx.py, EPS=1 for all ε-transitions; the 234-file library = box32/c1o_list.py 64 without box33/out):
- ε-transitions 279 (all H1, all S4a), O-rises 146: 0 failures of EXIT-R, 0 of "each exit at most once per fallback-free segment" (ORX).
- When an absorbed exit leaves R later in the phase, it leaves at a fallback, always a tame one: 37 of 37 (17 at the first fallback
  after the absorption, 20 later).
- Max ε-type O-rises in one fallback-free segment: 8 (jcl_zcl_cu_n48, d_o 18). Random 𝒞^1O games (EPS=1 orx.py --rand 400 8 24 3301: 400 games, 763
  transitions): no ε-transition at all (random games are thin on crossings).
- Climb against EXIT-R / ORX (box33/orxclimb.py, seed jcl_zcl_cu_n48, fitness failures then O-rises per segment): 0 failures; O-rises per
  segment 9 at n 48.

## 3. What the X-charged carries are (DATA; box33/xclass.py, riseclass.py, orise2.py on the library)
- Crossings in phases: 3,170. By direction / H1 / tameness / rise interval / step type:
  - GROW (R gains vertices), H1 → H1, S4a: 1,766 tame not in a rise interval; 73 tame in one; 60 non-tame not in one; 175 non-tame in one.
  - SHRINK, H1 → H1: 420 S4a + 630 fallback, all tame, none in a rise interval. BOTH: 38 (tame, S4a, no rise). Type changes: 8.
- So every non-tame crossing and every crossing inside a rise interval is a GROW crossing under H1 → H1 at an S4a step.
- Rises with a crossing in [k, k′] and no fallback: 148 = 146 attained by σ̄(o) at k′ (115 with crossings at k and k′, 14 at k′ only;
  129 non-tame, 17 tame) + 2 attained by an Even R → R switch (tame, crossings at k and k′). Rises with no fallback and no crossing: 1
  (the wake of nowake_cex_n32).
- Lemma OR checked at all 146 O-rises (orise2.py: (a) path through o and x0 ∈ R_{k+1}; (b) x0 ∈ F_k under H1; (c) θ's level = L_{k′}
  and θ rises): 0 failures.
- Reading: per phase, the X-charged part of Corollary OX (ε, J, and the crossing part of ρ) is, in all data, exit absorptions plus a few
  Even R → R rises. A crossing in general (R oscillating, e.g. x31_re24: R of size 22, 2, 17, 5, 22 in five steps) is not charged to
  anything new: it is a relevant transition inside an L-run and is counted by Theorem LP.

## 4. The loop f ↔ ε (OPEN)
- R25 Theorem FB: fallbacks per phase ≤ n_E(2n − 1)(J + 1) + J (tame runs have ≤ n_E(2n − 1) fallbacks).
- EXIT-R: ε ≤ (d_o − 1)(f + 1), and J ≤ ε.
- Together they bound nothing: alternating "one absorption, one fallback that releases it" is consistent with both. j7_n48 has an exit
  absorbed twice in one phase, with fallbacks between (transitions ~40-67).
- What would close it (each OPEN): (i) a fallback releases an absorbed exit only if something else monotone moves (data: releases are at
  tame fallbacks only); (ii) a bound on fallbacks per phase not through J; (iii) a potential on θ: every ε-transition raises θ at level
  O_k (Lemma OR (c)), but θ is one monotone value and its increases can in principle run like a binary counter, so a bound needs more
  than monotonicity.

## 5. Wakes
**Lemma WK (PROVED, L-NEW succ. 13, from RESULTS R24 Lemma R and Lemma TB's choice rule).** Let y: a → z be a wake at k′ (P-N5-LP §3), y not
its own W-cycle node. If W_{k′+1} = W_{k′} at a and at z, then the W-cycle node of y has even priority (BFS mode).
Proof.
- By Lemma WAKE's proof, (y, z) is an edge of the arenas H_{k′−1} and H_{k′}; (y, a) is in both (a = σ_{k′}(y) was chosen from H_{k′−1} and
  is current at k′). k′ − 1 → k′ and k′ → k′+1 are S4a steps (no fallback in [k, k′]).
- In the odd mode the S4a choice at y (R24 Lemma TB step 4 with Lemma R; SPEC S1 (iv) / FIX 4) is the smallest index among the arena
  successors x that are fully optimal for the new valuation, i.e. W'(x) ⊕ y = W'(y).
- At k′ − 1 the choice is a: so W_{k′}(z) ◁ W_{k′}(a), or W_{k′}(z) = W_{k′}(a) and a < z. With the values at a and z unchanged at k′ + 1,
  in the first case z is not fully optimal at k′ while a is available; in the second both are fully optimal and a < z. Either way the
  choice at k′ is not z. The mode (parity of the cycle node of the optimal class at y) is the same at both steps, because it is the cycle
  node of W(a) = W(z) or of the strictly better a. □
- Consequence: in the odd mode every wake transition is a transition with a W-change on R (a, z ∈ R by Lemma WAKE), so K_odd ≤ the
  number of transitions with a W-change on R: in route-form pieces R24 counts them; in U2 / U3 / U23 stretches they are (K_W). In the BFS
  mode a wake with W unchanged at a and z is a TB-even key move or comes with a W-change on y's play.
- DATA (box33/wakes.py): 1 wake in the library (nowake_cex_n32: BFS mode, W changes at z, a W-tie switch). Climb products: 5 more (BFS
  mode, length-only band, U3 or U23); 4 with a W-change at a or z, 1 (U23, climb from nr_u23_n32) with W unchanged at a and z.
- K per phase (box33/kclimb.py, fitness = max K in one phase, total K, finite dormant R → R edges; seeds nowake_cex_n32, nr_u23_n32,
  u1flat_best_n32, n 32): best K = 2 per phase (two consecutive transitions, wake levels rising 26 → 29 and 18 → 19). REFEREE-2's
  K = 1 in all its data stands as the norm. CONJECTURE-level only: wakes per phase stay O(1) in reachable data; no statement.
- READING: with Lemma KW-LEN, in the length-only band (c_w above every vertex of R, which is where every wake so far lives) the odd-mode
  wakes are ≤ (f + 1)·|R|·(n − 1) per stretch; the BFS-mode ones are W-flat switches of CASC-U3 sub-runs (≤ 2|R| − 4 steps each) or ride on
  W-changes. So in that band K is bounded given f and the events (E). (E) stays OPEN.

## 6. Where this leaves the open cores per phase of o-cyclic 𝒞^1O (READING)
- The used-level carries (Theorem LP's ρ, ε) come from: fallbacks (R25 FB), exit absorptions (Lemma OR; ≤ (d_o − 1) per fallback-free
  segment if EXIT-R holds), 2 Even R → R rises in all data, and wakes (odd mode: W-changes on R; BFS mode: W-flat key moves).
- So the per-phase question is now three counts: fallbacks ↔ absorptions (the loop of §4), W-changes on R in U2 / U3 (K_W) and events
  in U3 (E). X itself (all crossings) is not needed beyond these.

## 7. Files (experiments/new/box33; out/ is gitignored)
- wakes.py (per-wake description), kclimb.py (K climb), xclass.py (crossing classes), xgrow.py, xjoin.py (grow/shrink, joins per vertex),
  riseclass.py (X-rises by attainer), orise2.py (Lemma OR checks), orx.py (EXIT-R / ORX; EPS=1 for all ε-transitions), orxclimb.py.
  lib.txt = the 234-file library list used here.
- Instances re-used: nowake_cex_n32 (sha1 3a56e3fb…), jcl_zcl_cu_n48 (sha1 53c69d2d…). No new named instance in this note.
