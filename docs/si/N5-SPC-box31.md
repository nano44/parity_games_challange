# N5-SPC (box 31): the same-pair core of a frozen W-phase — the gap-step Lemma P is DEAD (runfam_K100); Lemma GP (timely Lemma P) and GP+ PROVED (lane); Corollary FW-R: WCH ≤ (n − 1)(R + 1), R = late adoptions, so FW-BF holds whenever R = 0
L-SI successor 27 (Opus 5.5; D18, Lead reading L40). Lead's brief 2026-10-29 15:19Z, STEP 1: «the SAME-PAIR CORE ... Every gate has
λ_Ξ(d) = λ_W(d), so Ξ ⊴ W are two valuations under ONE order, differing only by the gates' tails; the arena is by Ξ and the choice by W ...
The untried idea: a W-frame Lemma P that charges one extra "gap step" per basin change. Target: FW-BF (WCH ≤ n − 1), or any polynomial bound
per frozen W-phase in the same-pair core. Otherwise a kill with an instance. Data first.» Working note, unrefereed, not frozen. Not a
TARGET.md claim. Nothing here bounds N5's running time; G-N5-TIME stays OPEN. Labels (D18 / L40): PROVED (lane) / CONJECTURE / OPEN / DATA /
DEAD. Counts are TRANSITIONS. Setting and lemmas used: docs/si/N5-FRZ-box29.md §0-§2, §7 (W-MON, XW, frozen W-phase, EPOCH-U);
docs/si/N5-TORD-box30.md §1, §11 (prefix form, GATE-FORM, SAME-NODE); RESULTS R17 (b) (Lemma P, cases A1/A2/B1/B2) and R17 (a) ((V1), (V2),
(F1)). Tools: experiments/si/core/ (sp.py, gp.py, mono.py, look.py, diag.py); outputs core/out/.

## Summary
| § | item | label |
| --- | --- | --- |
| §1 | the same-pair core in the corpora: 1,754 frozen W-phases (1,243 with \|D\| = 1, 511 with \|D\| ≥ 2); in every one L = WCH (no W-silent transition), L ≤ 0.87(n − 1), TC ≤ WCH; S is monotone (≤ 1 direction segment) in 1,722 of them | DATA |
| §2 | gap-step Lemma P («W_k ⊵ value(r) for simple G_τ paths of ≤ k − a − (basin changes so far) edges»), and the Ξ-frame, mixed and admitted-graph forms | DEAD (runfam_K100: lag 113 with 2 basin changes) |
| §3 | Lemma GP (timely Lemma P): W_k ⊵ value(r) for every simple path r whose i-th Even edge was ALLOWED (ρ, arena, or into U) at state k − 1 − i; any frozen W-phase | PROVED (lane); DATA 0 violations, control bites |
| §3 | Lemma GP+: also allowed: an edge inside one basin S_d whose gate is same-pair and tail-disjoint (G3*) | PROVED (lane); DATA 0 violations |
| §4 | Corollary FW-R: WCH ≤ (n − 1)(R + 1), R := adoptions of edges that were not allowed at an earlier state of the phase («late adoptions»); R = 0 ⇒ FW-BF; D = ∅ ⇒ R = 0 (R17 / FW-D0 recovered) | PROVED (lane), a REDUCTION |
| §4 | the same with R_T := transitions containing a late adoption: WCH ≤ (n − 1)(R_T + 1) | PROVED (lane) |
| §4 | R = 0 (⟺ R_T = 0) in 1,441 of the 1,754 same-pair frozen W-phases (FW-BF proved for each of them by FW-R); max R 40 (grow_K40_n373, WCH 45, n 373) | DATA |
| §5 | CONJECTURE R-LIN (R ≤ n − 1, R counted per adoption) | DEAD (core/instances/rlin_cex_n40: R = 129 in 10 transitions, n 40) |
| §6 | Lemma GP* (only BLOCKED edges, W-better but Ξ-refused, are excluded; contains GP, GP+) and Corollary FW-R*: WCH ≤ (n − 1)(R*_T + 1) | PROVED (lane); DATA 0 violations; R*_T = 0 in 1,499 / 1,754 |
| §5 | open: bound R_T polynomially (R_T ≤ L, so this is FW-BF's own difficulty); the late adoption is the precise residue of the obstruction F1 | OPEN |

## 0. Setting
A frozen W-phase F = [a, b] (box 29 §0): no fallback, τ, σ̄, D = {Odd u : σ̄(u) ≠ τ(u)}, λ_Ξ, λ_W constant. ρ_k := σ at state k;
W_k = val(ρ_k, τ), Ξ_k = val(ρ_k, σ̄). H_k := the arena (Even v keeps {ρ_k(v)} ∪ Iσ_k(v), Iσ_k = VJ00 improving edges of Ξ_k; Odd v keeps
τ(v)); ρ_{k+1} is a pointwise W-optimum of H_k ((F1) in G_τ, box 29 W-MON's proof). U_k := vertices whose (ρ_k, τ)-play avoids D (there
Ξ_k = W_k, Lemma XW's consequence); S_d,k := vertices whose play meets D first at d. SAME-PAIR CORE: λ_Ξ(d) = λ_W(d) for every d ∈ D (then
λ_Ξ = λ_W everywhere, Lemma SAME-NODE). G3* at state k for gate d: neither the (ρ_k, τ)- nor the (ρ_k, σ̄)-play from d meets S_d,k after d
(for |D| = 1 this is TD). TC := basin-changing transitions (some vertex changes its first gate or enters / leaves U).

## 1. DATA: the same-pair core (core/sp.py, core/mono.py; three corpora as in box 30: alt_all pinned starts (START=1), lib41, experiments/si (START=1))
| corpus | \|D\| = 1 | \|D\| ≥ 2 | control D = ∅ | blocked edge at some state | TC > 0 | ≤ 1 S-segment |
| --- | --- | --- | --- | --- | --- | --- |
| alt_all | 445 | 310 | 184 | 410 / 300 | 257 / 162 | 443 / 305 |
| lib41 | 519 | 30 | 164 | 486 / 30 | 305 / 11 | 509 / 29 |
| experiments/si | 279 | 171 | 133 | 241 / 157 | 150 / 97 | 271 / 165 |
- In every one of the 1,754 same-pair frozen W-phases: L = WCH (every transition changes W), TC ≤ WCH, L ≤ 0.87(n − 1): largest
  L/(n − 1) 0.870 (n5-epoch/instances/gci3_n24, |D| = 1, 20 at n 24), |D| ≥ 2: 0.800 (n5-epoch/instances/lend13_n16, 12 at n 16). So FW-BF holds
  there with room, and no same-pair frozen W-phase reaches n − 1 transitions.
- Blocked edges (W-improving in G_τ but not in Iσ, i.e. the arena refuses them: F1) occur in 92% of the same-pair phases; in the control
  (D = ∅) never (one frame).
- S := ∪_d S_d changes in one direction only (entries only or exits only) in 1,722 of 1,754 phases; at most 4 direction segments
  (red/xing/instances/x31_re24, 4 transitions). Long phases are monotone waves (box 30 §10.1).

## 2. DEAD: the gap-step Lemma P (one extra step per basin change), and its three variants
Statement tested (the Lead's untried idea in its natural form; core/sp.py): in a same-pair frozen W-phase, W_k(x) ⊵ value(r) for every simple
G_τ path r from x to a cycle node of state a with |r| ≤ k − a − TC_k edges (TC_k := basin-changing transitions before k), i.e. the W-frame
Lemma P of R17 (b) lags by at most one step per basin change. Measure: DEF := max_k (min(k − a, J) − e_k), e_k := the largest j with
W_k ⊵ BF_j pointwise (BF_j := best simple G_τ path of ≤ j edges found by a path-tracking Bellman-Ford; every BF value is the value of a real
simple path, so a lag is a genuine failure of the statement). Control: DEF = 0 on all 481 D = ∅ frozen W-phases (R17).
- KILL: experiments/si/runlin/instances/runfam_K100.pg (sha1 86cf1884919b223c18f982eed6a00a4256a501dd), start runfam_K100.start (sha1
  843b9f4e83a21d8ee5bd56df97f7b43f59edc394); frozen W-phase [52, 167], n = 139, D = {5}, c₁ = c₂ = 20: DEF = 113 with TC = 2 (WCH 115).
  n5b (L-COMP's implementation, SPEC mode) gives the identical state sequence (root/n5bcmp.py: 293 states, identical: True).
- The variants die on the same phase: Ξ-frame (Ξ_k vs simple G_σ̄ paths) DEF 109; mixed (W_k vs G_σ̄ paths) 108; W_k vs paths in the graph of
  edges admitted at SOME state of the phase 108.
- Obstruction (core/diag.py, core/look.py): the lag is not caused by basin changes but by a LONG-LIVED REFUSAL. Vertex 26 (in U) has the path
  26 → 27 → 10 → 5 → 7 → 20 (5 edges, through the gate 5) which is W-better than its play from state 69 on (diag at k = 69); the arena refuses
  (26, 27) (27 is trapped, Ξ(27) pessimistic) until the trapped wave (one Even vertex per transition along a chain of S, TORD (i)'s regime)
  has passed; 26 adopts (26, 27) only at 164 → 165. Meanwhile W never changes at 26, so a Lemma P in any single frame lags by ~100 steps,
  while WCH stays below n − 1. A Lemma P can only hold for paths whose edges were AVAILABLE in time; that is §3.

## 3. PROVED (lane): Lemma GP (timely Lemma P) and Lemma GP+
Definitions. Fix F = [a, b]. ALLOWED(x, t), for Even x and a ≤ t < b: ρ_t(x), every z with (x, z) ∈ Iσ_t, and every successor z ∈ U_t.
ALLOWED⁺(x, t): additionally every successor z with z, x ∈ S_d,t for a gate d with λ_Ξ(d) = λ_W(d) satisfying G3* at t. For Odd x:
τ(x). A path r = (x = r_0, …, r_L = u) is TIMELY AT STATE k (k ≥ a + L) if it is simple, u is a cycle node of state a (λ(u) = u), and
r_{i+1} ∈ ALLOWED(r_i, k − 1 − i) for every i < L. value(r) := (u, P(r), L) as in R17 (b).
Lemma GP. For every k ∈ [a, b] and every path r timely at state k: W_k(r_0) ⊵ value(r). The same with ALLOWED⁺ (Lemma GP+).
Proof. Induction on k; k = a: L = 0, r = (u), W_a(u) = (u, ∅, 0). Step k → k + 1: r = x → z → r′, r′ timely at state k, x ∉ r′; IH
W_k(z) ⊵ value(r′). By W-MON, W_{k+1} ⊵ W_k pointwise.
- z = ρ_k(x) (this covers Odd x, z = τ(x)): value(r′) ⊴ W_k(ρ_k(x)); R17 (b)'s Case A (A1, A2) verbatim with W_k in place of Ω_k gives
  value(r) ⊴ W_k(x) ⊴ W_{k+1}(x). (A1 uses (V1) W_k(x) = x ⊕ W_k(ρ_k x) and (V2); A2 is x its own cycle node.)
- z ∈ U_k, (x, z) ∉ Iσ_k: Ξ_k(z) ⊴ Ξ_k(ρ_k(x)) (not improving, VJ00 §4.4 (2)), W_k(z) = Ξ_k(z) (z's (ρ_k, τ)- and (ρ_k, σ̄)-plays coincide: they
  avoid D) and Ξ_k ⊴ W_k (Lemma XW). So value(r′) ⊴ W_k(z) ⊴ W_k(ρ_k(x)): Case A as above.
- GP+ only: z, x ∈ S_d,k, d same-pair and G3* at k, (x, z) ∉ Iσ_k. Then ρ_k(x) ∈ S_d,k, and by GATE-FORM (box 30 §11; G3* makes the
  continuation of d disjoint from S_d,k) Ξ_k(y) = pre_k(y) ⊕ Ξ_k(d), W_k(y) = pre_k(y) ⊕ W_k(d) for y ∈ {z, ρ_k(x)}, with the same cycle node
  c_d in both frames (same pair). Two values with the same tail compare as their prefixes (the symmetric difference of the P-sets lies in the
  prefixes, the length difference is the prefix length difference), so Ξ_k(z) ⊴ Ξ_k(ρ_k(x)) gives W_k(z) ⊴ W_k(ρ_k(x)): Case A as above.
- (x, z) ∈ Iσ_k: ρ̂ := ρ_k[x → z] is a strategy of H_k, so by (F1) W_{k+1}(x) ⊵ val_τ(ρ̂)(x). Let c := λ(z), π := the ρ_k-path (in G_τ) from z
  to c. This is R17 (b)'s Case B in the W frame, EXCEPT that (x, z) need not be W-improving; the cases where R17 used improvement are closed
  differently:
  B1 (x ∉ π, x not on c's cycle): val_τ(ρ̂)(x) = x ⊕ W_k(z) ⊵ x ⊕ value(r′) = value(r) by (V2).
  B1′ (x ∉ π, x on c's ρ_k-cycle; then W_k(x) = (c, ∅, ℓ)): the ρ̂-play from x is the cycle Z = x, π, arc to x, top(Z) = top of P(π) ∪ {c}.
      P(π) = ∅: val_τ(ρ̂)(x) = (c, ∅, |π| + 1) = x ⊕ W_k(z) ⊵ value(r). P(π) ≠ ∅ with even top: top(Z) is better than c, so by (F1) λ_W(x)
      changes at k + 1: not in F. P(π) ≠ ∅ with odd top: W_k(z) = (c, P(π), |π|) has a worse P-set than every (c, ∅, ·); value(r′) ⊴ W_k(z)
      then gives (cycle node u = c) P(r′) worse than ∅, or (u ≠ c) reward(u) < reward(c); x is less relevant than c, so in both cases
      value(r) = x ⊕ value(r′) ◁ (c, ∅, ℓ) = W_k(x) ⊴ W_{k+1}(x).
  B2 (x ∈ π): Z = x, z, π[z..x), λ(x) = c, and with D′ := P(π[z..x)) ∪ ({x} if x is more relevant than c) (R17's symmetric difference of the
      P-sets of W_k(z) and W_k(ρ_k(x))): D′ ≠ ∅ with even top ⇒ λ change (as R17). D′ ≠ ∅ with odd top ⇒ W_k(z) ◁ W_k(ρ_k(x)). D′ = ∅ and
      top(Z) ≠ c: if c is odd, top(Z) has a better reward ⇒ λ change; if c is even, W_k(z) is longer with the same P-set, so W_k(z) ◁
      W_k(ρ_k(x)). In both «◁» cases value(r′) ⊴ W_k(z) ◁ W_k(ρ_k(x)) and Case A gives value(r) ⊴ W_k(x) ⊴ W_{k+1}(x). D′ = ∅, top(Z) = c:
      c = x (π is simple and ends at c), x is its own cycle node, and R17's last paragraph applies verbatim (u = x is excluded since r′
      avoids x; u ≠ x: value(r′) ⊴ W_k(z), whose cycle node is x, so reward(u) < reward(x) and value(r) ◁ (x, ∅, 0) = W_k(x)).
  In every case W_{k+1}(x) ⊵ value(r); paths of fewer edges are covered by W-MON. □
- Remarks. (1) GP needs neither same-pair nor TD; it holds in every frozen W-phase (σ̄ fixed is used only for «Iσ_t is the arena» at each
  state). (2) For D = ∅ every successor is ALLOWED (U = V): GP is R17 (b) on G_τ (FW-D0). (3) What the arena refuses and GP does not cover is
  exactly an edge (x, z) with z trapped in a basin other than x's (or in a non-G3* basin), not in Iσ: the F1 edges of box 30 §9.
- DATA (core/gp.py, PLUS=1 for GP+ with G3 tested at each state): 0 violations on all 2,235 frozen W-phases of the three corpora (1,754
  same-pair + 481 control), for GP and for GP+. Control that bites: MUT=all (every successor ALLOWED, i.e. the plain W-frame Lemma P) fails
  (runfam_K100 phase [8, 33]; xing/instances/ccl_w48_n48). GP+ with the tail condition dropped fails on
  new/box28/instances/oc24_s4_final (gate 2 with both tails inside S_2): the tail condition is needed.

## 4. PROVED (lane): Corollary FW-R (a reduction of FW-BF to late adoptions)
Definition. A LATE ADOPTION in F is a pair (x, τ) with x Even, a ≤ τ < b, ρ_{τ+1}(x) = z ≠ ρ_τ(x), such that z ∉ ALLOWED⁺(x, t) at some
state t ∈ [a, τ) (necessarily t < τ: an adopted edge is in Iσ_τ). R := the number of late adoptions in F.
Corollary FW-R. Every frozen W-phase in which the ALLOWED⁺ notion applies (any frozen W-phase with ALLOWED; same-pair gates with G3* get
the larger ALLOWED⁺) has WCH ≤ (n − 1)(R + 1). In particular R = 0 ⇒ WCH ≤ n − 1 (FW-BF for F).
Proof. At most n − 1 W-changing transitions have k < a + n − 1. Let k ≥ a + n − 1 with W_{k+1}(x) ≠ W_k(x) for some x, and let π = (y_0 = x,
…, y_L = u) be the ρ_{k+1}-play from x to its cycle node u = λ(x) (a cycle node of state a: λ is constant on F); π is simple, L ≤ n − 1
≤ k − a, and value(π) = W_{k+1}(x). If π were timely at state k, Lemma GP+ would give W_k(x) ⊵ value(π) = W_{k+1}(x) ⊵ W_k(x) (W-MON), so
W_{k+1}(x) = W_k(x) (VJ keys are injective on values): contradiction. So some Even y_i has y_{i+1} = ρ_{k+1}(y_i) ∉ ALLOWED⁺(y_i, t) at
t := k − 1 − i ≥ a. Since ρ_{k+1}(y_i) = y_{i+1} ≠ ρ_t(y_i) (ρ_t(y_i) is allowed at t), y_i adopts y_{i+1} at some τ ∈ (t, k]: a late
adoption (y_i, τ) with k − τ ≤ k − t − 1 = i ≤ n − 2. Charge k to it. A late adoption at τ is charged only by transitions k ∈ [τ, τ + n − 2],
at most n − 1 of them. So the W-changing transitions with k ≥ a + n − 1 number at most (n − 1)R. □
- Variant FW-R′ (same proof, charge k to the TRANSITION τ instead of the pair (y_i, τ)): WCH ≤ (n − 1)(R_T + 1), R_T := the number of
  transitions τ → τ + 1 of F containing at least one late adoption. R_T ≤ min(R, L); R_T = 0 ⟺ R = 0. PROVED (lane).
- READING. FW-R isolates the residue of the obstruction F1 (box 30 §9, §11 SAME-NODE): R counts the refusals that are LATER RESOLVED
  (the refused edge is eventually adopted); permanent refusals and refusals inside a G3* same-pair basin cost nothing. For D = ∅, R = 0 and
  FW-R is FW-D0. A polynomial bound on R gives a polynomial bound per frozen W-phase.
- DATA (core/gp.py PLUS=1; check RED_V := WCH > n − 1 + nR never fires): R = 0 in 1,441 of the 1,754 same-pair frozen W-phases
  (alt_all 611 of 755, lib41 456 of 549, experiments/si 374 of 450), so FW-BF is PROVED for each of these 1,441 phases by FW-R (the hypothesis
  R = 0 is checked on the run). Largest R: 40 (red/usplit/instances/grow_K40_n373, |D| = 4, WCH 45, n 373), 12 (xing/instances/ccl_w48_n48,
  |D| = 1, WCH 3: several late adoptions in one transition), 9 (rund/instances/offalt_K10, |D| = 2, WCH 23). runfam_K100 [52, 167]: R = 1 (the
  adoption (26, 27) of §2).

## 5. OPEN, next
- DATA (core/late.py, outputs core/out/late_*.txt; the 687 late adoptions of the three corpora): x enters a basin (U → S) 468, x changes
  basin (S → S′) 125, no basin change of x 94; never S → U; the transition changes W at every late adoption. One vertex can make many: 40 late adoptions by one vertex, each to a different edge (red/usplit/instances/grow_K40_n373); an
  edge can be re-adopted 5 times in 23 transitions (si/rund/instances/offalt_K10, n 182, D = {4, 32}: vertex 181 alternates 179 ↔ 180
  between the basins of the two same-pair gates every two transitions, each switch Ξ-improving; core/lateshow.py). So no per-vertex or
  per-edge bound on late adoptions holds by itself.
- DEAD: CONJECTURE R-LIN (R ≤ n − 1 with R counted per adoption; it was stated in the first push of this note, l-si 76c83301). Killed by
  experiments/si/core/instances/rlin_cex_n40.pg (sha1 670ba1ffc22c8f9b170e11ca3e43c33cee9329ca), start rlin_cex_n40.start (sha1
  e488c00fe1359818b9a665a415cc7b2962015318); found by core/spclimb.py SCORE=r from lend13_n16 within ~1 minute. Frozen W-phase [1, 11], n 40,
  |D| = 1 (gate NOT tail-disjoint, so GP+'s basin allowance is unavailable): R = 129 late adoptions in 10 transitions (R_T = 9), WCH = 10.
  n5b identical (13 iterations). Obstruction: R counts several vertices per transition; FW-R′ (R_T) is the right count. FW-R itself holds
  there (WCH 10 ≤ 39).
- OPEN (the same-pair core after FW-R′): bound R_T. R_T ≤ L, so «R_T ≤ n − 1» is implied by FW-BF and implies only WCH ≤ n(n − 1); a
  polynomial bound on R_T would already give a polynomial bound per frozen W-phase. FW-BF itself needs the sharper amortisation the data
  show (WCH ≤ 0.87(n − 1) even with R up to 40).
- Next steps (lane): (i) bound late adoptions per edge (an edge adopted, left and re-adopted needs Ξ(x) to rise past it twice); (ii) a kill
  search maximising R/(n − 1) and WCH/(n − 1) in the same-pair core (seeds grow_K40_n373, ccl_w48_n48, runfam_K100); (iii) the non-G3* gates.

## 6. PROVED (lane): the sharp form — Lemma GP* (only BLOCKED edges are excluded) and Corollary FW-R* (written 2026-10-29T16:2xZ by date -u, see commit)
Definition. An Even edge (x, z) is BLOCKED at state t of F if W_t(z) ▷ W_t(ρ_t(x)) and (x, z) ∉ Iσ_t (W-better than x's current choice,
refused by the Ξ-arena: exactly the F1 edges of box 30 §9). A path r = (r_0, …, r_L = u) is UNBLOCKED AT STATE k if it is simple, u is a
cycle node of state a, L ≤ k − a, and no Even edge (r_i, r_{i+1}) is blocked at state k − 1 − i. A LATE ADOPTION* is an Even x switching at
τ → τ + 1 to an edge that was blocked at some earlier state of F; R*_T := the transitions of F containing a late adoption*.
Lemma GP*. In every frozen W-phase F (any game, any D): W_k(r_0) ⊵ value(r) for every path r unblocked at state k.
Proof. As §3, with one change: for an edge (x, z) ∉ Iσ_k that is not blocked, W_k(z) ⊴ W_k(ρ_k(x)) by definition, so value(r′) ⊴ W_k(z) ⊴
W_k(ρ_k(x)) and R17 (b)'s Case A (A1, A2) applies verbatim in the W frame; Case A never used anything else. Edges in Iσ_k are §3's arena
case (B1, B1′, B2), which does not use improvement; z = ρ_k(x) and Odd x are Case A. □
- GP and GP+ are special cases: an edge into U_k that is not in Iσ_k has W_k(z) = Ξ_k(z) ⊴ Ξ_k(ρ_k x) ⊴ W_k(ρ_k x); an edge inside a
  same-pair tail-disjoint basin compares as prefixes (§3). So the only edges a W-frame Lemma P must give up are the blocked ones.
Corollary FW-R*. Every frozen W-phase F has at most (n − 1)(R*_T + 1) W-changing transitions; R*_T = 0 ⇒ WCH ≤ n − 1 (FW-BF for F).
Proof. §4's proof with «unblocked» for «timely»: a W-change at k ≥ a + n − 1 forces an Even edge of x's new play, blocked at t = k − 1 − i
and held at k + 1, hence adopted at some τ ∈ (t, k] (a blocked edge is not ρ_t(y_i)); charge k to the transition τ, k − τ ≤ i ≤ n − 2. □
- DATA (core/gp.py STAR=1, outputs core/out/gpstar_*.txt): GP* 0 violations on all 2,235 frozen W-phases; RED (both forms) never fires.
  R*_T = 0 in 1,499 of the 1,754 same-pair frozen W-phases (alt_all 635 of 755, lib41 462 of 549, experiments/si 402 of 450): FW-BF is
  proved for each of these by FW-R*. Largest R*_T: 40 (grow_K40_n373, |D| = 4, WCH 45; R*_T/(n − 1) = 0.11); |D| = 1: R*_T/(n − 1) ≤ 0.11
  (red/so/instances/xrun8_n10, 1 at n 10). rlin_cex_n40 has R* = 0 (FW-BF proved there); ccl_w48_n48 has R* = 12 in R*_T = 1 transition.
- DATA (core/late.py STAR=1, outputs core/out/latestar_*.txt): R*_T ≤ TC in every one of the 1,754 same-pair frozen W-phases. Of the 348
  late-adoption* transitions, 340 change some basin; the other 8 (all with tail-disjoint gates) do not, so the inequality is not a
  per-transition fact. CONJECTURE R*-TC: R*_T ≤ TC in every frozen W-phase. With FW-R* it gives WCH ≤ (n − 1)(TC + 1), i.e. the epoch count
  again (box 30 TORD (i) + EPOCH-U give the same for |D| = 1, TD); the frontier stays TC (CONJECTURE TRAP-LIN and its multi-gate form).
- PACKET: docs/si/P-N5-GP-box31.md (GP*, GP, GP+, FW-R*, with W-MON and XW), FROZEN at l-si d072bb28, sha1 cd4866df18b55f44b3ef3d52de65943eeffe9140
  (Lead 16:24Z / 16:31Z).
- READING. FW-R* is the cleanest form of the reduction: the W-frame Bellman-Ford of R17 runs undisturbed except across F1 refusals, and
  every W-changing transition beyond n − 1 is paid for by a resolved F1 refusal within the last n − 1 transitions. The open quantity is
  R*_T, the number of transitions in which a previously blocked edge is taken. A polynomial bound on R*_T gives a polynomial bound on WCH per
  frozen W-phase (and only that: see the Lead's question (b), answered in the 16:17Z message: FW-R* feeds box 29's W-SPLIT, not R86's NM*).

## DONE / FINDINGS / NEEDS
- DONE: this note; tools experiments/si/core/ (sp.py, gp.py, mono.py, look.py, diag.py, late.py, lateshow.py, spclimb.py); outputs core/out/,
  climb logs core/climb/; check.sh «box 31» block.
- FINDINGS: (1) DEAD: the gap-step Lemma P charged per basin change (and its Ξ, mixed, admitted-graph forms): runfam_K100, lag 113 with 2
  basin changes; the lag comes from a long-lived refusal, not from basin changes. (2) PROVED (lane): Lemma GP / GP+ (timely Lemma P), any
  frozen W-phase. (3) PROVED (lane): Corollary FW-R, WCH ≤ (n − 1)(R + 1); R = 0 ⇒ FW-BF; R = 0 on 1,441 / 1,754 same-pair phases.
  (4) DATA: every same-pair frozen W-phase has L = WCH ≤ 0.87(n − 1). (5) DEAD: CONJECTURE R-LIN
  (rlin_cex_n40, R = 129 in 10 transitions). (6) PROVED (lane): the sharp
  form GP* / FW-R* (§6): only blocked edges are excluded; R*_T = 0 in 1,499 / 1,754. (7) OPEN: a polynomial bound on R*_T.
- NEEDS: none from the owner.
