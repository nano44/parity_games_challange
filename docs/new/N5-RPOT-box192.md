# Box 192 R-POT: potentials for R on Γ3-Howard (IDEAL-CYC); TIE-restricted domination (L-NEW successor 60)
L-NEW successor 60, under D14 / D18 / D1. Lead GO 09:36Z (2026-11-07). Written from 09:40Z (date -u). Tools: experiments/new/box192/.
Labels: PROVED (lane, unrefereed) / PROVED-CONDITIONAL (on a named premise) / CONJECTURE / DATA (with counter: unit, set, scope) /
DEAD (instance) / READING (not to sign). Nothing here is a TARGET.md claim. G-N5-TIME stays OPEN. N5′-xi stays a CANDIDATE.

## 0. The question and the answer so far
- Question (handover 59, Lead brief): R := the number of R-steps of the Howard run on IDEAL-CYC(G), i.e. steps with no cycle-node
  change at which Odd's optimal counterstrategy σ̄ changes. By P-N5-XICYC Corollary T3 (PROVED-CONDITIONAL on [REACH-L]), «R polynomial for
  every genome» ⇔ «N5′-xi's FL run on Γ3(G) polynomial for every genome».
- Answer so far: R is NOT proved polynomial. Proved here (lane):
  - §2 EQ-FLIP: every R-flip happens at a gate whose two faces share one cycle node.
  - §2 MERGE: the order of the two face values is decided by the most relevant vertex on the two plays before they merge (a max-plus,
    i.e. tropical, comparison).
  - §2 X-GATE: a gate whose Ξ-target is the exit X flips at most 4M + 5 + L_g times in the whole run. L_g counts face ties; it is 0 in all
    data. So R is polynomial ⇔ the R-steps that flip a gate whose Ξ-target is a mover (R_mov) are polynomially many.
- DEAD potentials (§3): FLIP-H, HEAD-STEP, EXCH-1 (matroid single exchange), L♮-MODEL (discrete convexity, Murota–Shioura).
- TIE-restricted domination (§5): DOM-T PROVED (lane). The step from DOM-T to a segment bound (SEG-T) needs TIE-PERSIST, which is
  open. SEG-T has 0 violations in DATA, but those runs are short.

## 1. Setting and premises
- IDEAL-CYC(G), steps, labels C / R / p, n, M, N: as in P-N5-XICYC §2 (frozen packet docs/new/P-N5-XICYC.md, sha1 149e2414).
  Facts F1-F6 are from there: F1 monotonicity, F3 play extension, F4 ext monotone, F6 movers are never cycle nodes.
- [VJ]: the VJ00 / Friedmann 1106.0778 §3 value (Λ, Π, k) and its order ⊴, as in P-N5-XICYC §1. Π is the set of play vertices more
  relevant than Λ; vertices on the cycle other than Λ are less relevant than Λ.
- [LOC] local optimality of Odd's optimal counterstrategy: σ̄_t(v) is a ⊴-least successor value at every Odd v. The premise is used as in
  RESULTS R104, quoted: «with local optimality in a one-player game (RESULTS R36 (c) Lemma P1, applied on the dual game to Odd's one-player
  game against a fixed σ; VJ00's two-player Lemma 5.8 is not used)». Used only where marked.
  DATA: locfail 0. Unit: (gate, state) pairs. Set: 16 L-RED R-bests + 100 random genomes (seed 1). Scope: IDEAL-CYC. Tool: xgate192.py.
- Gate g of option (x, k): faces e_g (→ W-target y_g, or c_W at level 0) and β_g (frozen → Ξ-target xt_g, or → u = K0 when xt = X).
- RESULTS R95 (Lemmas LEX-SIGN, PREFIX-MON) already gives the monotone k-prefix of a path set while the cycle node is fixed. I use only its
  k = 1 case: the most relevant e-vertex of Π(v) does not decrease. That is not new here.

## 2. PROVED (lane)
**Lemma EQ-FLIP.** At an R-step t → t+1, every Odd vertex v with σ̄_t(v) ≠ σ̄_(t+1)(v) is a gate g with Λ_t(e_g) = Λ_t(β_g).
Proof.
- The Odd vertices are the gates and K2.
- K2: under σ̄(K2) = K2 the play is the K2 self-loop, so Λ(K2) = K2. Under σ̄(K2) = K1 it is K2 → K1 → K1 …, so Λ(K2) = K1. A change at K2
  therefore changes Λ(K2), and the step is a C-step.
- A gate g has priority 1, and every cycle through g passes a face of priority ≥ 6, so g is never a cycle node. F3 gives
  Λ_t(g) = Λ_t(σ̄_t(g)) and Λ_(t+1)(g) = Λ_(t+1)(σ̄_(t+1)(g)).
- At an R-step Λ_t = Λ_(t+1) =: Λ everywhere. If σ̄ changes at g from face f to the other face f′, then Λ(f) = Λ(g) = Λ(f′). ∎

**Lemma MERGE.** Fix a state and a gate g with Λ(e_g) = Λ(β_g) = w. Define:
- P_A and P_B: the plays from e_g and from β_g;
- m: the first vertex of P_A that lies on P_B;
- A′ and B′: the parts of P_A and P_B before m;
- U_w: the vertices more relevant than w.

Then A′ ∩ B′ = ∅, and Π(e_g) Δ Π(β_g) = (A′ ∪ B′) ∩ U_w, with A′ ∩ U_w ⊆ Π(e_g) and B′ ∩ U_w ⊆ Π(β_g). So:
- if (A′ ∪ B′) ∩ U_w ≠ ∅, let z be its most relevant vertex; the face whose part contains z is the ⊴-larger one (better for Even) iff z
  is even;
- otherwise the two values differ only in length (k_A − k_B = |A′| − |B′|), ordered by [VJ].

e_g ∈ A′ always.

Proof.
- Both plays are lassos ending in the play of w, so w lies on both and m exists.
- After m both plays coincide (positional strategies). Lasso vertices are pairwise distinct, so A′ and B′ are disjoint from the common
  suffix S. A′ ∩ P_B = ∅ by the choice of m, so A′ ∩ B′ = ∅.
- Π = (play vertices) ∩ U_w, by [VJ]. So Π(e_g) = (A′ ∪ S) ∩ U_w and Π(β_g) = (B′ ∪ S) ∩ U_w. The order is [VJ]'s order on the symmetric
  difference. ∎

READING: MERGE is a max-plus (tropical) statement. Odd's comparison at g is the sign of the most relevant vertex of a bounded union. It
is not a sum, so a weighted-shortest-path potential is the wrong lens.

**Corollary MERGE-CHOICE (PROVED-CONDITIONAL on [LOC]).** If Ω(e_g) ≠ Ω(β_g), σ̄(g) is the face that MERGE ranks lower for Even.

**Lemma X-GATE (PROVED-CONDITIONAL on [LOC]).** Let g be a gate with xt_g = X. Let L_g be the number of states with Ω(e_g) = Ω(β_g). Then
σ̄(g) changes at most 4M + 5 + L_g times along the whole run.

Proof.
- β_g → K0 → K3 → K2 are all frozen (K2 is Odd). At K2 the two options have values with cycle nodes K2 (reward −3) and K1 (reward −5). By
  [LOC] σ̄_t(K2) = K1 at every t.
- So Ω_t(β_g) is one fixed value B (cycle node K1) for all t. Ω_t(e_g) =: A_t is ⊴-non-decreasing (F1).
- Λ(e_g) changes at most 2M + 2 times (the argument of CYC-COUNT: rewards rise strictly, and there are ≤ 2M + 3 possible cycle nodes).
  So the run splits into at most 2M + 3 maximal intervals I with Λ(e_g) constant, plus at most 2M + 2 transitions between them.
- Inside I:
  - if Λ(e_g) ≠ K1, A ≠ B by reward, and [LOC] fixes σ̄(g);
  - if Λ(e_g) = K1, the states of I split, in order, into a block with A ◁ B, a block with A = B (L_I states) and a block with A ▷ B,
    because A is monotone and B is fixed. σ̄(g) = e is forced on the first block and β on the third, so it changes at most L_I + 1 times
    inside I.
- Total: (2M + 2) + Σ_I (L_I + 1) ≤ 4M + 5 + L_g. ∎

**Corollary R-SPLIT (PROVED-CONDITIONAL on [LOC]).** R ≤ R_mov + Σ_{g: xt_g = X} (4M + 5 + L_g) ≤ R_mov + M(4M + 5) + Σ_g L_g, where
R_mov is the number of R-steps that change σ̄ at some gate whose Ξ-target is a mover. So «R polynomial» ⇔ «R_mov + Σ_g L_g polynomial».
(⇐ by the bound; ⇒ since R_mov ≤ R. For Σ L_g, ⇒ is NOT claimed.)
- DATA, face ties: Σ_g L_g = 0. Unit: (gate, state) pairs. Set: 16 L-RED R-bests + 100 random genomes (seed 1) + the 300 of xgate192.py
  rand 300 1. Scope: IDEAL-CYC. Tool: xgate192.py.
- DATA, max σ̄-changes of one X-gate inside one interval of constant (Λ(e_g), Λ(β_g)) = 1. Unit: transitions. Same set and scope. Tool:
  xgate192.py.

## 3. DEAD potentials (each with its instance; instances in experiments/new/box192/inst/, copied from claude/l-red c81dd2d7
experiments/red/r215/out/, sha1 in inst/SHA1SUMS)
Head notation: head(v) := the most relevant e-vertex of Π(v).
- **DEAD FLIP-H** («every R-flip at g changes head(e_g) or head(β_g)»; it would bound flips by head changes, which are monotone per
  R95 k = 1). Killed by rd2_d9 (N 18): 15 of 55 R-flips change neither head. Also rd2_d10 8/51, rf_d5 5/19, rd3_d7 4/29. Tool:
  rpot192.py, column flipnoh.
- **DEAD HEAD-STEP** (the weaker «every R-step changes head(v) at some vertex v»; it would give R ≤ n·M·(2M + 3)). Killed by rd2_d9: 9 of
  18 R-steps (t = 11, 13, 14, 15, 17-21) change no head anywhere. Also rd2_d4 (t = 9), rd2_d6, rd2_d8, rd3_d5, rd3_d7, rf_d5. Tool:
  rpot192.py, column Rnohead.
- **DEAD EXCH-1** (matroid / basis exchange: «per step, the e-part of Π(v) at a vertex with fixed cycle node changes by one exchange
  (|Δ ∩ E| ≤ 2)». An exchange-graph argument would need it). Killed by rd2_d9 and rd3_d5: |Δ ∩ E| = 7 in one step. Tool: rpot192.py,
  column xsz.
- **DEAD L♮-MODEL** (discrete convex analysis: «the Howard run is a SteepestDescent run of some L♮-convex g on the option coordinates»).
  - Source opened: Murota–Shioura, «Exact bounds for steepest descent algorithms of L-convex function minimization», METR 2013-24
    (U. Tokyo) = Oper. Res. Lett. 42 (2014) 361-366, DOI 10.1016/j.orl.2014.06.005.
  - Its Algorithm SteepestDescent moves by ±χ_X. Its Theorem 1.2: it «terminates exactly in μ(p◦) + 1 iterations», where
    μ(p) = min over p* ∈ argmin g of ‖p* − p‖⁺∞ + ‖p − p*‖⁻∞.
  - On a box {0, …, K}^N, μ ≤ 2K, so there are at most 2K moves.
  - rd2_d3: every mover has 2 options, so K = 1, but T = 9 > 2. rd3_d4: degree ≤ 3, K = 2, T = 18 > 4. This holds under ANY injective
    encoding of the options as 0..K.
  - M♮ version (exchange moves change ≤ 2 coordinates): Howard switches up to 11 movers in one step (rd2_d9). So it is not an M♮
    exchange walk either.
  - Only the MODEL is dead. A discrete-convex potential that Howard merely increases is not excluded; I have no candidate.
- DATA (not DEAD), DEPTH: depth(t) := min over vertices v of the e-rank depth of the top of Δ(Π_t(v), Π_(t+1)(v)). A constant bound c at
  every R-step would give R ≤ n(2M + 3)(M + 1)^c (the R95-style k-prefix count). Unit: R-steps. Set: 16 L-RED R-bests + climb cD_d6_w2.
  Scope: IDEAL-CYC. Max depth: 5 at rd2_d8 (N 16), 2 at rd2_d9. The climb maximising depth (cD) reached 5 at N 12. So no constant c is in
  sight. Tool: depth192.py.

## 4. The requested fields: what each would need, and its status
- Matroid / submodular exchange: Π∩E would have to move by single exchanges in a matroid. DEAD as EXCH-1 (§3).
- Discrete convexity (M♮ / L♮): the run would have to be a steepest-descent / exchange walk. DEAD as a model (§3). A potential view stays
  open with no candidate.
- Tropical geometry of the Ξ-values: MERGE shows each local decision is a max-plus sign. What it needs: a bound on the number of sign
  changes of the tropical difference max(A′ ∪ B′) at a fixed gate g, as A′ and B′ move. The ingredients that are monotone are F1 (values)
  and R95 (k-prefixes). Neither controls the sign of a bounded union. Open; no claim.
- Amortised (splay-style) potential: Φ_1 := Σ_v rank(head(v)) is monotone between cycle-node changes and pays exactly for HEAD-STEP,
  which is DEAD. Φ_k (k-prefixes, R95) pays for depth ≤ k. That fails for every fixed k unless DEPTH is bounded (DATA: it grows to 5).
  So any amortised potential must charge R-steps to something other than path-set prefixes, e.g. to pairs (y_g, xt_g) of movers (next
  item).
- What remains: by X-GATE, only gates with a mover Ξ-target matter. At such a gate g (Ξ-target x′, W-target y) the choice is the order
  of the truncated values trunc_{>e_g}Ω(y) and trunc_{>e_g}Ω(x′) (MERGE). The equality case resolves to β (DATA: TRUNC-CHOICE 0 failures.
  Unit: (gate, state) pairs with equal face cycle nodes below e_g, decided by the truncation or by the equality rule. Set: 16 L-RED
  R-bests, 5,599 pairs. Scope: IDEAL-CYC. Tool: trunc192.py). So the open core is:
  - (OVT) for a fixed pair of movers (y, x′) and a fixed threshold, how often can two ⊴-monotone truncated value sequences overtake each
    other?
  - CONJECTURE OVT-POLY: polynomially often.
  - DATA: max σ̄-changes at one gate (all steps) = 10, at rd2_d9 and rf_d5. Unit: transitions. Set: 16 L-RED R-bests. Scope: IDEAL-CYC.
    Tool: climb192.py flipcount. This agrees with L-RED §53.1 («No gate flips more than 10 times»).

## 5. TIE-restricted domination for RED-XI (item 2 of the brief)
Setting: general game G; the N5′-xi run; S its σ-changing iterations (DECOMP-G). At a non-fallback σ-step σ_k → σ_(k+1), N5′-xi sets
σ_(k+1)(x) := the Ω_k-best element of TIE_k(x) at every Even x with |A_k(x)| ≥ 2, x not its own H-cycle node and TIE_k(x) ≠ ∅ (a «TIE
vertex»). Here A_k(x) = {σ_k(x)} ∪ Iσ_k(x). Source: n5v.py l. 34-37 (key E.key(vs[w]) = Ω_k), box 190 §2.1.

**Lemma DOM-T (PROVED, lane).** For a TIE vertex x of a non-fallback σ-step k → k+1 with Λ_(k+1)(x) ≠ x:
Ω_(k+1)(x) ⊵ ext(x, Ω_k(y)) for every y ∈ TIE_k(x).
Proof.
- Ω_(k+1)(x) = ext(x, Ω_(k+1)(σ_(k+1)(x))) by F3 (on G; Λ_(k+1)(x) ≠ x).
- This is ⊵ ext(x, Ω_k(σ_(k+1)(x))) by [R15a] and F4. The step switches only along edges of Iσ_k, one per vertex, so it is a non-empty
  unambiguous improvement set.
- That is ⊵ ext(x, Ω_k(y)) for y ∈ TIE_k(x), by the choice of σ_(k+1)(x) and F4.
- At a fallback σ-step, σ_new(v) is the Ω-best improving successor at every switched v, which is Howard's choice there. So plain DOM
  holds at those vertices. ∎

**Obstruction (why DOM-T does not yet give BR-SEG-T).** PATH needs, at every Even z_i of the final play π and every earlier step of the
window:
- z_i is a TIE vertex;
- z_(i+1) ∈ TIE(z_i).

Call this TIE-PERSIST. It is open: TIE sets are recomputed at every step from the arena H_k.

DATA SEG-T («every maximal run of p-steps along S has ≤ n_E steps»): 0 violations. Unit: games. Sets: 300 random games n 12 (seed 1),
200 random games n 24 (seed 2), switchallexp sae_2..5. Scope: general games, N5′-xi. Tool: tie192.py. WEAK: the longest p-run seen is 4
(sae_5), so the runs are short. A climb for long p-runs (tieclimb192.py) is queued. X1 fails on 67 of 314 and 159 of 378 σ-steps in the
random sets: Howard-faithfulness is not the route, which is why TIE-PERSIST is the right target.

## 6. Data runs in progress (growth of R)
R-scored climbs, climb192.py: «R (d, w)» = d levels of width w. Values at 09:4xZ (date -u; climbs still running, logs out/c*.log):

| climb | levels d | width w | N | best R | its T |
| --- | --- | --- | --- | --- | --- |
| cR_d2_w4 | 2 | 4 | 8 | 8 | 10 |
| cR_d2_w8 | 2 | 8 | 16 | 16 | 24 |
| cR_d3_w4 | 3 | 4 | 12 | 7 | 22 |

So even two levels give R ≈ N. That fits L-RED's R ≲ 2d ≈ N. DATA. Unit: R-steps. Set: climb bests. Scope: IDEAL-CYC.

## 7. Next
1. Two-level genomes (d = 2): only level-1 gates can flip (LEVEL0), and every e on a play is a level-1 e. Attempt OVT-POLY there first:
   the smallest case with R ≈ N.
2. SEG-T climb (tieclimb192.py); if it holds, look for a TIE-PERSIST proof on Γ3-like arenas.
3. L-LIT: is the «overtake count of two monotone sequences coupled through a positional game» bounded in any source on policy iteration
   for deterministic games (e.g. Hansen–Zwick-style Howard bounds for deterministic MDPs)? Not opened here.

## Addendum 1 (after milestone 1; date -u from 10:0xZ)
### A1.1 MERGE types of R-flips (DATA)
I classify every R-flip at a gate g by MERGE's first common vertex m, in the state after the flip:
- RET: m = e_g. The β-play runs back through g and then through e_g, so A′ = ∅. The comparison is the top of the loop segment
  B′ = β_g → … → g. Odd takes e to avoid closing the cycle g → β_g → … → g.
- BRET: m = β_g, the mirror case.
- DISJ: A′ and B′ are both non-empty.

PROVED (lane, immediate): a RET state has σ̄(g) = e, and a BRET state has σ̄(g) = β. The play from β_g passes g and continues with
σ̄(g), so e_g on P_B forces σ̄(g) = e, and symmetrically for BRET.

DATA (unit: R-flips; set: 16 L-RED R-bests + cR_d2_w8 best; scope: IDEAL-CYC; tool: mtype192.py):

| type | to e | to β |
| --- | --- | --- |
| RET | 143 | 0 |
| BRET | 0 | 34 |
| DISJ | 147 | 71 |

READING: about half the R-flips are «cycle avoidance». Even's switches complete a route from β_g back to g, and Odd answers by leaving
through e_g. This is L-RED §53.1's «Odd leaves an Even-won β-cycle», made exact by MERGE. A charging argument would charge each RET flip
to the switch that completed the return route. It is not proved, and it would need a per-route bound.

## Addendum 2: literature check (Lead 10:05Z; L-LIT parked). Sources opened, with what each bound needs, and whether Γ3 runs meet it
- Murota–Shioura, METR 2013-24 = ORL 42 (2014) 361-366, DOI 10.1016/j.orl.2014.06.005: Theorem 1.2. Opened. Covered in §3 (DEAD L♮-MODEL).
- **Post–Ye, arXiv 1208.5083 (v2; SODA 2013; Math. Oper. Res. 2015, DOI 10.1287/moor.2014.0699).** Opened: the abstract on arxiv.org.
  - Quoted: «the simplex method with the highest gain/most-negative-reduced cost pivoting rule converges in strongly polynomial time for
    deterministic Markov decision processes (MDPs) regardless of the discount factor»; «O(n^3m^2log^2 n) iterations if the discount
    factor is uniform and O(n^5m^3log^2 n) iterations if each action has a distinct discount factor».
  - Needs: ONE player (an MDP); deterministic transitions; discounted total cost; Dantzig's rule, i.e. one switch per iteration (the
    highest gain).
  - DOES NOT APPLY to Γ3-Howard, for three reasons: two players (Odd best-responds at the gates); Howard switches every improvable mover at
    once (up to 11 in one step, rd2_d9); the values are VJ parity values, not discounted costs.
  - The one-player variant is already polynomial by ONEP-POLY (P-N5-XICYC), so Post–Ye adds nothing there.
  - A possible use, NOT done: a Dantzig-rule variant of N5′-xi (one switch per step) on a parity-to-discounted reduction. The bound is
    independent of the discount, so the exponentially small 1 − γ of that reduction would not hurt. But Odd's best response still breaks
    the one-player hypothesis.
- **Hansen–Miltersen–Zwick, arXiv 1008.0530.** Opened: the abstract on arxiv.org; Lemmas 5.3 / 5.4 were opened by successor 59 (DOM =
  folklore).
  - Bound: Howard's policy iteration / strategy iteration for 2-player turn-based stochastic games with discount γ «terminates after at
    most O(m/(1−γ) log(n/(1−γ))) iterations».
  - Needs: a FIXED discount, 1/(1−γ) polynomially bounded. Two players and Howard are allowed, so this is the closest match to our setting.
  - DOES NOT APPLY: a parity game, or the VJ order, is captured by a discounted game only with 1 − γ exponentially small in the number of
    priorities. That is the standard parity → mean-payoff → discounted reduction; I did not re-open its source here. With such a γ the bound
    is exponential.
  - Its proof idea, action elimination («after O(1/(1−γ) log(n/(1−γ))) iterations some action is never used again»), does not carry over
    plainly. DATA: movers re-adopt options they left, up to 6 times per option (rd2_d9), and gate faces return up to 5 times (rd2_d9, rf_d5).
    Unit: re-adoptions per (mover, option) / per (gate, face). Set: 16 L-RED R-bests + cR_d2_w8. Scope: IDEAL-CYC. Tool: ret192.py.
    A VJ analogue would need «some action is never used again after poly steps». Untested.
- **Hansen–Kaplan–Zwick, «Dantzig's pivoting rule for shortest paths, deterministic MDPs, and minimum cost to time ratio cycles», SODA
  2014, pp. 847-860, DOI 10.1137/1.9781611973402.63.** NOT OPENED: epubs.siam.org returned 403, dblp blocked automated access, and the
  arXiv API title search returned no entry.
  - I therefore cite no theorem from it. The search-engine snippets (an O(mn log n) Dantzig bound for shortest paths, an Ω(n²) lower bound,
    and an improvement of Post–Ye) are secondary and are not used.
  - On the hypotheses those snippets name (Dantzig's rule, one player), it would not apply, for the same reasons as Post–Ye.
- Summary: none of the three bounds applies to Γ3-Howard. Each needs one player, a single switch per step (Dantzig), or a fixed discount.
  Γ3-Howard has two players, all-switch steps and parity (exponentially-small-discount) values. This is the expected gap: it is the gap
  between «strongly polynomial for fixed discount» (HMZ) and «parity games».

## Addendum 3: DEAD SEG-T (TIE item); final climb values
- **DEAD SEG-T** («along DECOMP-G's σ-steps S of N5′-xi on a general game, every maximal run of p-steps (Λ and σ̄ constant) has
  ≤ n_E steps»).
  - Instance: experiments/new/box192/inst/DEAD_SEGT_n20.json (sha1 02efd55e…, in inst/SHA1SUMS), a general game with n 20, n_E 6, 19
    iterations, 1 fallback. Found by tieclimb192.py (GAP=1, n 20, seed 7), climb log out/tieg_n20.log.
  - Its 18 σ-steps are ALL p-steps: p-run 18 > n_E = 6.
  - Replay with segt192.py (independent of the climb's scorer): every step is ⊴-monotone at every vertex, and every switch is improving.
    Most switches are improving but NOT ⊴-best (X1 fails). Steps 2, 11 and 18 switch vertex 2 while it is its own cycle node (H0 fails),
    and Ω does not change strictly there.
  - Even without those steps, steps 3-10 are 8 consecutive p-steps with no own-cycle-node switch, 8 > 6. So SEG-T is dead also under H0.
  - Consequence: DOM-T, the TIE-restricted domination of §5, stays PROVED (lane), but no segment bound follows from it alone.
    RED-XI's route on general games needs X1, or TIE-PERSIST plus TIE vertices at every switch; the latter is still unrefuted as stated.
    The Γ3 route (X1 holds there by REACH3-CYC) is unaffected.
- Final climb values (40-min slices ended; DATA; unit R-steps; set: climb bests; scope: IDEAL-CYC):

| climb | levels | width | N | best R | its T |
| --- | --- | --- | --- | --- | --- |
| cR_d2_w4 | 2 | 4 | 8 | 9 | 10 |
| cR_d2_w8 | 2 | 8 | 16 | 22 | 24 |
| cR_d3_w4 | 3 | 4 | 12 | 10 | 23 |

  The depth climb cD_d6_w2 (N 12) ended at R-depth 6.

## Addendum 4: erratum to A1.1; DEAD CHARGE-RET
- Erratum (A1.1 table): the row set «16 L-RED R-bests + cR_d2_w8 best» used the cR_d2_w8 genome as it stood at commit d52f9613 (R 21).
  The climb then improved it to R 22. That genome is frozen as inst/cR_d2_w8_R22.json (sha1 in inst/SHA1SUMS). Re-run with
  mtype192.py on the 16 + cR_d2_w8_R22 (unit R-flips):

| type | to e | to β |
| --- | --- | --- |
| RET | 144 | 0 |
| BRET | 0 | 29 |
| DISJ | 151 | 77 |

  The A1.1 statements (RET ⇒ e, BRET ⇒ β, about half the flips «to e» are RET) are unchanged.
- **DEAD CHARGE-RET** («every RET flip at g at step t → t+1 has a mover on the return segment B′ = β_g … g that switched at step t»; this
  would charge cycle-avoidance flips to the switch that completes the return route).
  - Killed by rf_d5: 3 of its 8 RET flips have no switched mover on B′. Also rd2_d4 (2 of 8), rd2_d9 (3 of 24), cR_d2_w8_R22 (3 of 14).
  - Total: 120 of 144 RET flips charged. Unit RET flips. Set 16 L-RED R-bests + cR_d2_w8_R22. Scope IDEAL-CYC. Tool charge192.py.
  - Even on the charged ones, one mover carries up to 9 charges over a run (rd2_d9). A per-mover bound would need a separate argument.
  - Obstruction (reading): the return route can already exist at t. The flip then comes from a change of the segment's most relevant
    vertex (MERGE), not from the route's completion.

## Addendum 5: DEAD SRC-DEC
- Definition: a «source» at a state is a gate whose faces have different cycle nodes. Its choice is fixed by the rewards ([LOC]) and
  changes only at C-steps.
- **DEAD SRC-DEC** («whenever an equal-Λ gate takes e, MERGE's decisive vertex is the e-vertex of a source gate»). If true, e-taking
  would be rooted in sources, whose choices change only polynomially often.
  - Killed by cR_d2_w8_R22: of its 119 such e-takings, 0 are decided by a source's e-vertex, 87 by the e-vertex of another equal-Λ
    gate, and 32 by a non-e vertex (the RET loop segment's top).
  - Total: 1,044 e-takings, 40 source-decided, 763 decided by an equal-Λ gate's e, 241 other. Unit: (state, gate) pairs. Set: 16 L-RED
    R-bests + cR_d2_w8_R22. Scope: IDEAL-CYC. Tool: src192.py.
- READING: e-taking chains sustain themselves among equal-Λ gates. Their roots are mostly RET loops, i.e. cycles Odd would close by
  taking β, not cycle-node differences. So a potential must see «virtual» cycles: the Even-won cycles that a β choice would close. A
  candidate for the next step: count, per gate g, the changes of the top vertex of the would-be cycle g → β_g → … → g.

## Addendum 6: erratum on the cR_d2_w8 numbers (Lead 11:12Z, L-RED §53.2 discrepancy); CI diagnostics
- Unit: my «R» in §6, A3 and my messages is the number of R-STEPS: rpot192.analyse's count of steps labelled R (no cycle-node change,
  σ̄ changes somewhere). «R-flips» (rpot192 «flips») = σ̄-changes at R-steps, summed over Odd vertices.
- Error: out/cR_d2_w8.json was rewritten by the running climb after each improvement, and I quoted log values for whatever version
  existed at the time. The versions and their counts (rpot192.py / xgate192.py / climb192 flipcount; unit as stated):

| version (sha1 of the genome file) | where | T | C | R-steps | R-flips | max flips at one gate (all steps) |
| --- | --- | --- | --- | --- | --- | --- |
| never committed | §6 table at 8c2a6678 («R 16, T 24», read from the climb log) | 24 | | 16 | | |
| 0952ef28 | committed in 8c2a6678 | 23 | 2 | 19 | 38 | 8 |
| 575c8683 | committed in d52f9613 (A1.1's set); my 10:02Z message «R 21» | 23 | 2 | 21 | 38 | 7 |
| b83785f6 | committed in 1da5317c / 05c5170b; frozen as inst/cR_d2_w8_R22.json; A3 «R 22» | 24 | 2 | 22 | 44 | 7 |

  On 0952ef28 these agree with L-RED's replay in §53.2 (T 23, C 2, R 19, max flips 8). §6's «R 16, T 24» row and the «R 21» in the
  10:02Z report are withdrawn as counts of a committed genome. Only inst/cR_d2_w8_R22.json (b83785f6) is a frozen instance; out/ files
  are live climb state, not instances.
- CI: GitHub «verify» failed on 8c2a6678, 1da5317c, 05c5170b and df108b05 inside the BOX 192 block with no message. In this container it
  passes on a clean worktree of e47d0203 with a fresh HOME, under python3.12 and python3.13 and with an 8 MB stack. The cause is not
  reproduced here. The block now never exits silently: it prints «BOX 192 R-POT check: FAILED (check192.sh exit …; python …)», the diff
  and the run's last 15 lines (control: an altered check192.out makes it fire).

## Addendum 7: DEAD VCYC-STEP (the A5 candidate)
- VCYC_t(g) := the most relevant vertex of the cycle closed by the play from β_g when g is forced to β (σ̄ elsewhere), or none if that
  play does not return to g.
- **DEAD VCYC-STEP** («every σ̄-change at a gate g coincides with a change of VCYC(g)»; with a per-gate bound on VCYC changes it would
  bound flips per gate).
  - Killed by rd2_d9: 48 of its 93 σ̄-changes at gates (all steps) leave VCYC(g) unchanged. Also cR_d2_w8_R22 (35 of 54), rf_d5 (16 of
    28), rd3_d5 (12 of 30).
  - Moreover VCYC itself changes up to 8 times per gate (rd2_d9), as often as the flips (max 10). So it is no cheaper a quantity.
  - Unit: σ̄-changes at gates over all steps. Set: the four instances named. Scope: IDEAL-CYC. Tool: vcyc192.py.
- Status of the open core after A1-A7: R (R-steps) on Γ3-Howard is NOT proved polynomial. Proved (lane): EQ-FLIP, MERGE, RET/BRET; X-GATE
  and R-SPLIT [LOC]; DOM-T. Dead: FLIP-H, HEAD-STEP, EXCH-1, L♮/M♮ models, SEG-T, CHARGE-RET, SRC-DEC, VCYC-STEP. Per-gate flips stay
  ≤ 10 in all data (L-RED §53.2: per-gate overtakes ≤ 15 on 37 instances), so CONJECTURE OVT-POLY is unrefuted.
