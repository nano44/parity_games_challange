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
3. **EXIT-R: FALSE (L-RED exitr_cex_n48, §13); it was a CONJECTURE with 0 failures on the 279 library ε-transitions.** Survivor: ABS-COUNT (§13).
   Original statement: An exit absorbed at an ε-transition stays in R until the next fallback
   transition or the end of the phase. With Lemma OR it gives ε ≤ (d_o − 1)(f + 1) per phase (under H1), hence J ≤ ε ≤ (d_o − 1)(f + 1).
   Absorbed exits that do leave R leave only at (tame) fallbacks: 37 of 37.
4. **The loop that remains (OPEN).** R25 Theorem FB gives f ≤ n_E(2n − 1)(J + 1) + J, and EXIT-R gives J ≤ (d_o − 1)(f + 1). The two are
   circular. A bound on either side per phase, from something other than the other, closes the X-charged carries.
5. **Lemma WK (PROVED, L-NEW succ. 13, from RESULTS R24 Lemma R / TB).** At a wake y: a → z whose W-cycle node is odd and y is not its own
   W-cycle node, W changes at a or at z (both in R) at the same transition. So in the odd mode every wake is a transition with a W-change
   on R; wakes with W unchanged at a and z exist only in the BFS (even) mode.
6. **Lemma R-STICK, Corollary SN-PREFIX, Lemma SN-ORDER (PROVED, L-NEW succ. 13; §8).** At an S4a step R can lose a vertex only
   when c_w = c_θ; in a run without fallbacks those states form a prefix, so after it R only grows (≤ n − 1 crossings). The crossing
   problem lives in the SN regime c_w = c_θ, where (under H1) both frames order R-vertices identically. This proves EXIT-R for the 30
   ε-transitions with c_w(k+1) ≠ c_θ; 249 remain conjectural.
7. **K data, and the K-chain family (§11).** The library has 1 wake. Climbs reached K = 2. The explicit family kchain.py K (n = 11K + 14,
   verified with Oink) has K − 1 wakes in ONE phase at consecutive transitions with rising levels: K per phase is Θ(n), not O(1). N5
   stays fast there (K + 2 iterations). Every wake seen is U3 / U23, length-only band, BFS mode.
8. **Refuted (§10).** H-RE (re-absorbing the same exit needs r to drop): FALSE on b6_xl_n48.
9. **Tool bug (§11).** mono.py's lev() uses 99 for ∞: wrong on n ≥ 100 (library unaffected). box33/biglev.py patches it.

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

## 2. CONJECTURE EXIT-R and its consequence (EXIT-R FALSE: §13)
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
  K = 1 in random and library data. "Wakes per phase stay O(1)" is FALSE: the K-chain family (§11) has K − 1 wakes in one phase at n = 11K + 14.
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

## 8. R never shrinks at an S4a step unless c_w = c_θ (PROVED, L-NEW succ. 13; written 02:41Z by date -u)
Notation: c_θ := λ_Ξ(o) (fixed in the phase), c_w(s) := λ_W(o) at state s. For x ∈ R_s, λ_Ξ(x) = c_θ and λ_W(x) = c_w(s): x's
(σ_s, τ)-play reaches o, its H_s-play agrees with it up to o (on 𝒞^1O the two graphs differ only at o), and both then follow o's play.
Distinct cycle nodes compare by rew alone, and rew is injective (si.py l.42-44: pp = 2·rank + parity; rew = ±pp), as is Even's order
on cycle nodes in VJ00.

**Lemma R-STICK.** At an S4a transition s → s+1 (no fallback) of a phase, every x ∈ R_s with λ_W(x) ≠ λ_Ξ(x) lies in R_{s+1}. Hence if
c_w(s) ≠ c_θ, then R_s ⊆ R_{s+1}.
Proof. Suppose x ∈ R_s ∩ F_{s+1}. Off R, Ξ = W (RESULTS R19 (a) Lemma G (a)), so W_{s+1}(x) = Ξ_{s+1}(x), of cycle node λ_Ξ(x) =: c (fixed in
the phase). W_s(x) has cycle node c′ := λ_W(x) ≠ c. At an S4a step W_{s+1} ⊵ W_s (the arena contains σ_s; R24 TB step 1, R17 (F1)), so
rew(c) > rew(c′). But Ξ_s(x) (cycle node c) ⊴ W_s(x) (cycle node c′) by (XW) (VJ00 (11)), so rew(c) < rew(c′). Contradiction. □

**Corollary SN-PREFIX.** In a run of consecutive non-fallback transitions of a phase, the states with c_w = c_θ form a prefix of the run,
and after that prefix R never loses a vertex until the run ends. So every crossing after the prefix adds a vertex to R: at most n − 1
of them per such run, and the crossings of a phase number at most (f + 1)(n − 1) + f + X_SN, where X_SN counts the S4a crossings at
states with c_w = c_θ.
Proof. W(o) is non-decreasing along the run (as above), so rew(c_w) is non-decreasing; and rew(c_w) ≥ rew(c_θ) at every state by (XW) at
o, with equality iff c_w = c_θ (rew injective). So c_w = c_θ holds on an initial part of the run only. After it, R-STICK at every step. □
- Consequence for §2: EXIT-R is PROVED for every ε-transition k with c_w(k+1) ≠ c_θ (x0 ∈ R_{k+1} by Lemma OR (a), then R-STICK to the end
  of the run). It stays a CONJECTURE when c_w(k+1) = c_θ (249 of the 279 ε-transitions; the other 30 are covered).
- DATA (box33/sn.py; 0 failures of R-STICK and of the prefix property): library 894 fallback-free runs, crossings at S4a steps 2,473 at
  c_w = c_θ states vs 61 after the prefix (max 12 per run, jcl_zcl_cu_n48 at n 48; max 55 in the prefix, x32_rand64 at n 64); random
  (sn.py --rand 2000 8 24 3302) 172 vs 0. Every S4a exit release of §2's data is at c_w = c_θ (45 of 45).

**Lemma SN-ORDER (the order part is RESULTS R19 (a) under (h); mine is only H1 ∧ H3 ⇒ H2, P-N5-SN §4).** Under H1 at a state with c_w = c_θ =: c, both frames are in route form, and for x, y ∈ R
lev(Ξ(x), Ξ(y)) = lev(W(x), W(y)) with the same direction: the two frames order R-vertices identically. They can disagree only when an
R-vertex is compared with an F-vertex.
Proof. Under H1, c ∈ F (o is on no honest cycle). o's W-play ends on the cycle of c ⊆ F, so o is not on its W-cycle (H2). In route form
(R22 / R24 (R1)) Ξ(x) = π_x ⊕ θ and W(x) = π_x ⊕ w, where π_x ⊆ R \ {o} is x's route and the paths of θ and w lie in F ∪ {o}. So
P(Ξ(x)) = (π_x ∩ V_{>c}) ⊔ P(θ) and P(W(x)) = (π_x ∩ V_{>c}) ⊔ P(w), with lengths |π_x| + |θ| and |π_x| + |w|. For x, y ∈ R the symmetric
differences of the path sets are (π_x Δ π_y) ∩ V_{>c} in both frames, the length differences are equal, and the cycle node (which fixes
the length direction) is c in both. □
- Reading: the crossing problem of a phase (X, hence the X-charged carries) lives entirely in the SN regime c_w = c_θ, where the two
  frames agree on R and differ only by the terminal values θ ⊴ w at o. There Lemma BAND's band (rank c_θ, rank c_w) is empty, so route-form
  wakes cannot occur. Leaving R at p needs an F-option ⊵ π_q ⊕ w (the optimistic value); joining R needs only π_r ⊕ θ ▷ the F-value (the
  pessimistic one). An absorption (§1) is Even closing a loop p → r → … → o → x0 → … → p whose top above c is good for Even in the honest
  frame; Odd leaves the loop at o.

## 9. θ-changes are Even-driven or absorptions; the link to L-SI's CLS1 (Lead question 02:42Z; written 02:50Z by date -u)
**Lemma TC-SPLIT (PROVED, L-NEW succ. 13; 𝒞^1O, inside a phase).** At every phase transition k → k+1 with θ_{k+1} ≠ θ_k: either
lev(θ_k, θ_{k+1}) ≤ E_k, or k is an ε-transition and lev(θ_k, θ_{k+1}) = O_k (Lemma OR (c)).
Proof. If λ(o) = o, θ = (o, ∅, 0) never changes. Else let x0 := σ̄_k(o), x1 := σ̄_{k+1}(o); θ_k = o ⊕ Ξ_k(x0), θ_{k+1} = o ⊕ Ξ_{k+1}(x1), and o
lies on neither path (functional graph, as in Lemma OE step 2), so lev(θ_k, θ_{k+1}) = lev(Ξ_k(x0), Ξ_{k+1}(x1)) (L-SI (C7)). x1's
H_{k+1}-path avoids o, so its relevant changes are Even ones of level ≤ E_k, and U-loc gives lev(Ξ_k(x1), Ξ_{k+1}(x1)) ≤ E_k. If x0 = x1 that
is the claim. Otherwise lev(Ξ_k(x0), Ξ_k(x1)) = O_k, and by (C6) lev(θ_k, θ_{k+1}) ≤ max(O_k, E_k): ≤ E_k if O_k ≤ E_k, and = O_k if
O_k > E_k (Lemma OR (c)). □
- DATA (box33/scopecov.py, library): 1,573 θ-changes in phases, 0 failures; 279 are ε-transitions, 1,294 have level ≤ E_k.

**Lemma ABS-L (PROVED, L-NEW succ. 13, from L-SI's Lemma NL (P-N5-CLS §5; unrefereed) and CAP-1).** Let S be a scope run (P-N5-CLS §0),
k0 < k fallbacks of S with no fallback between them, L := M_{k0}, and r_j := lev(θ_j, w_j) > L for j ∈ [k0+1, k] (CLS1's case 2; there
(A_j) holds for L at every j ∈ [k0+1, k], CLS1's proof). Then at every transition j ∈ [k0+1, k−1] with lev(θ_j, θ_{j+1}) > L:
- (i) σ̄(o) changes, x0 := σ̄_j(o) → x1, and lev(θ_j, θ_{j+1}) = lev(Ξ_j(x0), Ξ_j(x1)) = O_j > L;
- (ii) x0 ∈ F_j ∩ R̄_{j+1} (an absorption);
- (iii) x0 ∈ R̄_t for every t ∈ [j+1, k].
Hence there are at most d_o − 1 θ-changes above L in (k0, k).
Proof.
- (h) holds at j and j+1, so H1: σ̄(o) ∈ F at both (Lemma OR (b)'s argument). If σ̄(o) did not change, x0 ∉ R̄_{j+1} and NL (i) freezes
  COARSE_L(Ξ(x0)), so lev(θ_j, θ_{j+1}) ≤ L by (C7). So it changes. x1 ∉ R̄_{j+1}, so NL (i) freezes COARSE_L(Ξ(x1)).
- If x0 ∉ R̄_{j+1}, both are frozen above L. CAP-1 at j and j+1 (Ξ_j(x0) ⊴ Ξ_j(x1), Ξ_{j+1}(x1) ⊴ Ξ_{j+1}(x0)) then forces
  lev(Ξ_j(x0), Ξ_j(x1)) ≤ L (a strict order above L would persist, (C1)-(C3)), and (C6) gives lev(θ_j, θ_{j+1}) ≤ L. So x0 ∈ R̄_{j+1}.
  x0 ∈ F_j by H1. (i): Ξ_{j+1}(x1) agrees with Ξ_j(x1) above L, so the level > L is lev(Ξ_j(x0), Ξ_j(x1)).
- (iii): NL (ii) at each S4a step of [j+1, k−1]: R_t ⊆ R̄_{t+1}.
- Count: each such j absorbs the current minimiser, a distinct exit (absorbed exits stay in R̄ and σ̄(o) ∈ F under H1), and one exit
  is in F at every state. □
- So EXIT-R is PROVED on CLS1 case-2 intervals (for all absorptions there, not only ε-transitions). Coverage of the 279 library
  ε-transitions: 30 by R-STICK (c_w ≠ c_θ), 64 in case-2 intervals (ABS-L), 45 in scope runs before their first fallback, 139 in scope
  runs where r ≤ L somewhere in the interval, 1 outside scope runs. 185 remain CONJECTURE.
- Note: once r_j ≤ L, θ has no change above L for the rest of the scope run: θ_j ⊴ θ_{j+1} ⊴ w with lev(θ_j, w) ≤ L gives
  lev(θ_j, θ_{j+1}) ≤ L ((C5)).
- Answers to the Lead's questions (READING):
  - (a) Segmentation: EXIT-R is per fallback-free run; CLS1 is per scope run ((h) and w constant), which contains fallbacks. A scope run
    lies in the SN regime (H3: c_w = c_θ), exactly where R-STICK is silent; L-SI's NL (ii) is the SN / THR / (A) analogue of R-STICK. Inside
    a scope run, EXIT-R's segments are the gaps between its fallbacks; on case-2 gaps ABS-L proves it.
  - (b) Yes, on case-2 gaps: every θ-change above L is an absorption of the current minimiser exit (ABS-L (i)-(ii)); in general
    (TC-SPLIT) θ-changes above Even's own level E_k are exactly the ε-absorptions. So L-SI's per-level count becomes: between consecutive
    fallbacks at level M, at most d_o − 1 θ-changes above M, each an absorption. It does not close by itself: fallbacks release absorbed
    exits (FBL: THR fallbacks switch R → F edges), and a released exit can be absorbed again in the same scope run. DATA: 673 absorptions
    (σ̄(o) changes with x0 entering R) in scope runs; the same exit up to 5 times in one scope run (b6_xl_n48, exit 28). The open count
    per level is now: releases of absorbed exits at level-M fallbacks (OPEN).

## 10. Refuted: H-RE (FALSE, DATA)
- H-RE "inside a scope run, between two absorptions of the same exit, r = lev(θ, w) strictly drops": FALSE. b6_xl_n48
  (experiments/n5-exhaustive/instances/b6_xl_n48.pg; in the library): exit 28 is absorbed at transitions 70 (θ-level 38) and 88 (θ-level 33)
  with r = 39 at both. 25 failures in the library (box33/hre.py), 161 re-absorptions in scope runs in all.
- Also false at phase level: "between two absorptions of the same exit, θ changes above the first absorption's level" (9 failures; the
  same pair). Re-absorption at a LOWER level needs no higher θ-change.
- The b6_xl_n48 scope run shows the counter shape: after each fallback θ rises at level r (so r drops by 1: 43 → 39), and exit 28 is
  re-absorbed once per such epoch, at level 33 (transitions 3, 25, 48, 70, 88). Absorptions per exit per scope run: up to 5 in the
  library. Climb (box33/reabsclimb.py, seed b6_xl_n48, fitness = max absorptions of one exit in one phase): 5 → 5 after ~1.6·10⁴
  candidates (max absorptions in one phase 9 → 12). No growth found.

## 11. K is linear per phase: the K-chain family (DATA, verified; L-NEW succ. 13, written 03:08Z by date -u)
- FINDING: wakes per phase are not O(1). experiments/new/box33/kchain.py K builds a 𝒞^1O game of n = 11K + 14 vertices on which N5,
  from the canonical start, has ONE phase with K − 1 wakes at consecutive transitions 1, …, K − 1, with rising wake levels.
- Construction (U3, the length-only band of Lemma KW-LEN, BFS mode): a top vertex T (even) on o's W-cycle o → t_1 → … → t_6 → T → o, and
  every route passes T, so W compares lengths only. Odd's honest reply at o is x (cycle o → x → o, c_θ = x); x has a dormant edge to r,
  whose short route (Ξ-worse) keeps Odd's τ(o) honest-optimal (no S4b switch). Gadget i: y_i chooses between A_i (short, Ξ-poor) and
  Z_i → h_i → p_i (long, with the even vertex h_i of rank ℓ_i); p_i has a shortcut to y_{i−1}. When y_{i−1} wakes (Ξ rises at level
  ℓ_{i−1}), the shortcut (p_i, y_{i−1}) becomes an honest gate; the next S4a step takes it (shorter), which makes Z_i shorter than A_i,
  and y_i switches to Z_i at level ℓ_i > ℓ_{i−1} = L_{previous}: a wake. Lengths: a_i = D_{i−1} + 3, q_i = D_{i−1}, D_i = D_{i−1} + 4.
- Mechanism in words: a distance improvement propagates one layer per S4a step through honest gates, and each layer releases one
  dormant high edge. The honest frame sees each h_i all along; W (lengths to T) sees it only when the route catches up.
- Verified (instances in experiments/new/box33/instances/, out/ is gitignored):
| instance | sha1 | n | N5 iterations / fallbacks | wakes in one phase | Oink | one Odd choice vertex |
| --- | --- | --- | --- | --- | --- | --- |
| kchain4.pg | 2be32f30… | 58 | 6 / 1 | 3 | zlk OK, strategies verified | yes (o = 18) |
| kchain10.pg | 4af3726f… | 124 | 12 / 1 | 9 | zlk OK, strategies verified | yes (o = 42) |
| kchain32.pg | 63c5b0dd… | 366 | 34 / 1 | 31 | zlk OK, strategies verified | yes (o = 130) |
  - n5.py run equals the box21 trace and the box32 rows (asserted state by state). check_sol2.py with Oink built at 8fbf0a7.
  - lcheck.py (through box33/biglev.py, see below) on kchain10 / kchain32: 0 failures of Lemma U, HI, UL, GR, Theorem LP; in the phase
    T = 32, f = 0, X = 0, ρ = 31, all 31 rises caused by wakes (kchain32). So Corollary OX (iii)'s K term is the whole of ρ here.
  - Every wake is BFS mode, U3 / U23 by the box32 classifier, length-only band, with W changing at z (Lemma WK's odd-mode statement is
    not exercised).
- What it does NOT show: N5 is fast on this family (iterations = K + 2). K = Θ(n) per phase is still polynomial; the open question for
  G-N5-TIME is whether K, X and the fallbacks can multiply, not whether one of them is linear.
- TOOL BUG FOUND (inherited, not mine to fix in place): experiments/si/coarse/mono.py lev() returns 99 for ∞, so on games with n ≥ 100
  a rank ≥ 99 reads as ∞ (lcheck.py reported 42 false "L = ∞" failures on kchain10 / kchain32). All library data (n ≤ 64) is unaffected.
  box33/biglev.py runs any box32 / box33 tool with ∞ = 10⁶; the numbers above for n ≥ 100 use it. The si/coarse owner (L-SI) may want
  the same fix in mono.py.

## 12. Who can leave R at an S4a step (PROVED, L-NEW succ. 13; written 03:27Z by date -u)
Under H1, "c_w = c_θ" is H3, and H1 ∧ H3 gives H2 (Lemma SN-ORDER's proof: o's W-play ends on the cycle of c_θ ⊆ F). So the SN regime
under H1 is exactly the (h) regime of RESULTS R19-R25.
**Lemma LEAVE.** Let s → s+1 be an S4a transition (no fallback) of a phase with H1 at s, and let q ∈ R_s leave (q ∉ R̄_{s+1}). Then (h)
holds at s, and q's H_{s+1}-path before its cycle node carries a relevant change of level ≥ r_s := lev(θ_s, w_s); in particular L_s ≥ r_s.
Proof.
- If c_w(s) ≠ c_θ, Lemma R-STICK forbids the leave. So H3, hence (h).
- R19 (b) Lemma G: Ξ_s(q) = π_q ⊕ θ_s, W_s(q) = π_q ⊕ w_s, and π_q avoids the paths of θ_s and w_s (H1, H2); by L-SI's (C7)
  lev(Ξ_s(q), W_s(q)) = r_s and Ξ_s(q) ◁ W_s(q) (Ξ ⊴ W, and they differ when r_s ≠ ⊥).
- q ∉ R̄_{s+1}: W_{s+1}(q) = Ξ_{s+1}(q) (Lemma G (a)); R23 (g) WM: W_{s+1}(q) ⊵ W_s(q). So Ξ_s(q) ◁ W_s(q) ⊴ Ξ_{s+1}(q), and L-SI's (C5) gives
  lev(Ξ_s(q), Ξ_{s+1}(q)) ≥ r_s.
- If every relevant change on q's H_{s+1}-path had level < r_s, Lemma U-loc with L = r_s − 1 (L = ⊥ if r_s = −1) would give
  lev(Ξ_s(q), Ξ_{s+1}(q)) ≤ r_s − 1. Contradiction. (If r_s = ⊥, i.e. θ = w, the claim is empty.) □
- This is L-SI's Lemma NL key step (K*) without hypothesis (A), stated through U-loc: a leave needs an F-ward relevant change at a level
  at least the θ / w gap. With (A) for L < r it is impossible (NL (ii)); with R-STICK it is impossible off (h).
- DATA (box33/leave.py): library 616 S4a leaves under H1, all at (h) states, all with a relevant change of level ≥ r on the new path;
  random (--rand 3000 8 32 3404) 561, same, 0 failures. Leaves under ¬H1 (library 4, random 702) are outside the lemma; by R-STICK
  they are at c_w = c_θ states.
- Random robustness of §8-§9 (seeds 3401-3403, 4,800 games, n 8-48; out/randcheck.txt): R-STICK and SN-PREFIX 0 failures (552
  crossings in SN prefixes, 1 after); TC-SPLIT 0 failures on 371 θ-changes (2 ε); Lemma OR 0 failures (1 O-rise).

## 13. EXIT-R is FALSE (L-RED box 37); what survives (written 03:31Z by date -u)
- DEAD END: CONJECTURE EXIT-R (ε form) and ORX are FALSE. experiments/red/so/instances/exitr_cex_n48.pg (L-RED, l-red 9783ab7; sha1
  7a663df25ba44e15022ad94fe5f0709662dbca8d; n 48, o = 0, d_o 18; Lead re-run n5 22/1, Oink OK verified, one Odd choice vertex). Phase =
  transitions 4-20, no fallback. ε-transition 4 absorbs x0 = 13; at the S4a step 5 → 6 Even 13 switches 8 → 17 and leaves R; exit 13 is
  absorbed again at 9. box33/orx.py (EPS=1): EXITR_FAIL (4, 5, 13), ORX_FAIL (4, 9, 13). States 3-7 are (h) / SN (c_w = c_θ = 2), r = 47,
  45, 44, 43, then θ = w at 7, c_w ≠ c_θ from 8. The leave is in an (h) state before any fallback of its scope run (not a CLS1 case-2 gap),
  and it obeys Lemma LEAVE (a relevant change of level ≥ r = 44 on 13's new path; leave.py 0 failures). The O-rise restriction of
  EXIT-R has no counterexample yet; ε ≤ (d_o − 1)(f + 1) holds there (16 ≤ 17).
- What survives, PROVED (L-NEW succ. 13): **Corollary ABS-COUNT.** In a fallback-free run of a phase, the ε-transitions under H1 number
  at most (d_o − 1) + REL_run, where REL_run := the exits leaving R at S4a steps of the run; and every such release happens at an (h)
  state of the run's SN prefix via a relevant change of level ≥ r (Lemmas LEAVE, R-STICK, SN-PREFIX). Per phase:
  ε_{H1} ≤ (d_o − 1)(f + 1) + REL, REL := exit releases at S4a steps.
  Proof. Under H1 σ̄(o) ∈ F, so at most d_o − 1 exits are in R at any state. Each H1 ε-transition moves the current minimiser exit from F
  to R (Lemma OR (a)-(b)). The number of exits in R starts ≥ 0, ends ≤ d_o − 1, rises by ≥ 1 at each H1 ε-transition, and falls only when
  exits leave R, which inside the run happens only at S4a steps. □ (ε under ¬H1: 0 in all data; not covered.)
- DEAD END (L-RED box 37 interim 2, l-red fdd801b): the per-phase form "ε_{H1} ≤ (d_o − 1)(f + 1)" is FALSE.
  experiments/red/so/instances/epsseg_cex_n48.pg (sha1 b4c7dcb04fc2a156905fbe9ba2739e70e04c5c8c; n 48, o = 0, d_o 17; Lead re-run n5 26/1,
  Oink OK verified, one Odd choice vertex): phase 7-24, f = 0, 17 ε-transitions under H1 > 16. Exit 33 absorbed at 7, leaves R at the S4a
  step 8 → 9, re-absorbed at 14 (corrected 2026-10-25 05:31Z by date -u; CHECKER C39: at 13 σ̄(o) goes 47 → 33 with 33 still in F). ABS-COUNT holds with equality there (17 ≤ 16 + REL, REL = 1); LEAVE holds (1 leave, at (h)). Smaller
  EXIT-R counterexample: exitr_cex_n16.pg (sha1 6971211e…; n 16, d_o 6; ε 5 ≤ 5 + 1). So REL is the whole question for ε.
- So the form I pursue now: bound REL, the exit releases inside SN prefixes. In the data REL is tiny (library: 45 exit releases at S4a
  steps in all; exitr_cex_n48: 1).

## 14. REL data (DATA; written 03:44Z by date -u)
- Exit releases (an exit of o leaving R) at S4a steps, library + exitr_cex_n48: 46. Under H1 all 44 are at (h) states (Lemma LEAVE);
  2 under ¬H1 (b4_n5_other_0). 7 release an exit that was absorbed (σ̄(o) left it as it entered R) earlier in the same fallback-free run
  (e.g. lev_l_n28 transition 12, exit 16; all at (h)); 37 release exits not absorbed in the run. 13 of the 46 are at transitions that
  change w. So REL is small in all data; ABS-COUNT's bound ε_{H1} ≤ (d_o − 1)(f + 1) + REL is far from tight there.
- OPEN: a bound on REL per phase. LEAVE says each release needs an F-ward relevant change of level ≥ r = lev(θ, w); in a scope run r is
  non-increasing (L-SI Fact R), and after a fallback with level L, ABS-L / NL exclude releases while r > L.
- Where the 44 H1 releases sit (same data): 13 at transitions that change w (not scope-run transitions), 31 in scope runs before the
  run's first fallback (25 of them in scope runs that start at the phase start), 0 after a fallback (consistent with NL: none with r > L,
  and none with r ≤ L either). So REL ≤ (releases at w-changes) + Σ over scope runs of (releases before the first fallback), and
  only these two terms are non-empty in the data. OPEN: an (A)-type freeze at the start of a scope run (OFFGATE gives gates into F
  ≤ M of the previous transition, which does not exist at a phase start).
