# R2-N5-FBPOLY: second-referee check of packet P-N5-FBPOLY (L-NEW box 41: κ-FB-ROUND, κ-HAT-FREEZE, κ-PFZ, κ-Y-FORM, EXIT-SWITCH, FREEZE-EXIT, CN-ONLY, THETA-AFTER, Theorem FB-POLY). REFEREE-2 (successor 11), written 2026-10-25 19:0xZ-20:0xZ (date -u)
Signature: (Opus 5.5, D15). Lead queue addition 18:51Z (Lead's stamp). I put it ahead of NHN / NEEDB, as the Lead allowed.
Object: docs/new/P-N5-FBPOLY-box41.md, sha1 de244dcd3592b04eca2080a0efe10a7c0b2e5301, the same at the pin 42d8c3a9 and on my tree
(`git show 42d8c3a9:<file> | sha1sum`, `sha1sum`). Author: L-NEW successor 20.
Background read: SPEC S1-S5 (as restated in the packet's §0.1); RESULTS R15 (a), (d), R17 (a) (V1), R18 (d) Lemma S (a), R19 (a) G (a),
R21 (c) FBL-N, R38 (a) KEY, R38 (f) CN-LAST (text checked: "(every game): if k → k+1 is an S4c fallback at which Even switches
(Iσ_k ≠ ∅), and every gate (y, z) ∈ Iσ_k has λ_k(y) = y and lev(Ξ_k(σ_k y), Ξ_k(z)) = −1, then Ξ_{k+1} = Ξ_k, Iσ_{k+1} = ∅, and k + 1 is
the last state of its phase"). FBL-N (ii) appears in RESULTS as "every gate edge from F is flat for W". The packet reads it as
x = λ_W(x), λ_W(z) = x, which is the reading in docs/new/N5-NH-box28.md l. 85 and in P-N5-OUT / P-N5-NEB, both signed by both referees.
I accept it.
Also read: P-N5-PFZ §0-§6, P-N5-PFZ-ext and P-N5-RHO §0-§3 (this lane signed them: R2-N5-PFZ, R2-N5-RHO). The packet restates what it
uses from them, with proofs, and I checked the restated proofs on their own.
Independence: nothing in docs/referee/ was read for this packet (`ls docs/referee | grep -i fbpoly` -> empty). No lane script
(experiments/new/box41/fbpoly.py, which is not on my tree) was run or imported.
Tools (own code, docs/referee-2/R2-N5-FBPOLY/): fbpoly_check.py (on R2-N5-OUT/out_check.py: traces own / rand / spec; exact κ-path
optima by DFS for |U| ≤ 12), fbpoly_climb.py, files.lst (../R2-N5-PFZ/filesx.lst 453 + files_new.lst 39 = 492 tracked 𝒞^1O files,
n ≤ 64), run_all.sh, run_fx.sh, run_climbs.sh, totals.py, logs/, logs_fx/, logs_mut/, climb/, totals_logs.txt.
Labels: PROVED (L-NEW succ. 20). This is not a running-time bound, not a TARGET.md claim and not a step-4 pass. G-N5-TIME stays OPEN:
crossings outside SN prefixes / OUT stretches, OTHER-touching transitions, S4a steps and phases are not bounded here.

## Verdicts (Opus 5.5, D15)
| statement | verdict | gaps / notes |
| --- | --- | --- |
| §0.3 facts (Aκ), (A0κ), (M1κ), (M2κ), (INJ), (HP), (SP′), (YB) | correct | — |
| §1 Lemma κ-FB-ROUND | SIGN | — |
| §1 Lemma κ-HAT-FREEZE (a)-(c) | SIGN | — |
| §1 Lemma κ-PFZ | SIGN | — |
| §1 Lemma κ-Y-FORM | SIGN | — |
| §2 Lemma EXIT-SWITCH | SIGN | — |
| §3 Lemma FREEZE-EXIT | SIGN | — |
| §4 Lemma CN-ONLY | SIGN | — |
| §5 Lemma THETA-AFTER | SIGN | — |
| §6 Theorem FB-POLY (a)-(d) | SIGN | N-FBP-1 (proof of (b) covers only o ≠ c_θ; the claim holds for o = c_θ too); N-FBP-2 ((a)'s end bound uses deg_U(o) ≤ n − 1, false when o has a self-loop; the end bound still holds) |
| §7 (FB-CAP, FB-CAP-1/2, the EXIT branch question), §8 | not signed (as briefed) | N-FBP-4 (DATA): the EXIT branch occurs for SOME switched vertex (witness, §9) |
No statement is NOT SIGNED, and no gap is open. No (P). The only premises outside the packet are landed results (list above).
Thin spots (DATA, lesson N-ENT-2; my data agree with the packet's caveats):
- The hypotheses of FREEZE-EXIT and THETA-AFTER at |U| ≥ 3 (a fallback g_j with j ≥ |U| − 1) are NEVER reached, in my batch or my
  climbs (§9). FB-POLY (a) beyond FB-CAP rests on the proofs, which I checked line by line (§1-§6).
- FREEZE-EXIT's per-vertex bounds: the batch comes no closer than 2 below them. My climbs reach the kind-c_θ bound with equality,
  never past it (§9). The FX mutation could not be shown to bite on any saved instance.
- κ-HAT-FREEZE (c) is checked 27 times, all in the 63 phases with |U| ≥ 3 and f = |U| − 2 (no phase has f > |U| − 2).

## 0. The facts (§0.3)
- (Aκ): λ_t(z) = c_θ ≠ z, so (V1) gives Ξ_t(z) = z ⊕ Ξ_t(next z), with the same cycle node, so next_t(z) ∈ U. ⊕ adds z to P iff
  rank z > rank c_θ (wt(z)) and adds 1 to ℓ (s_θ). The double-count case is impossible: z ∈ P(Ξ next z) would put z on its own cycle,
  below c_θ. The κ components add, because the order inside a fixed cycle node is lexicographic in (signed weight, s_θ·ℓ) and both are
  additive. ✓
- (A0κ): c_θ's value is (c_θ, ∅, 0). next(c_θ) lies on c_θ's cycle, whose top is c_θ, so its P is empty. ✓
- (M1κ): S1 with equal rewards: first the signed weight, then ℓ, longer better for Even iff Ω(c) odd, i.e. s_θ = +1. ✓
  (M2κ): R15 (a) with λ constant on the phase. ✓ (INJ): distinct powers of 2. ✓
- (HP): on 𝒞^1O only o differs between the honest frame and (σ, τ). (i) and (ii) follow. ✓
- (SP′): the play stays in U by (Aκ). Its cycle has cycle node c_θ, so it contains c_θ. A lasso's vertices are distinct before the
  first repetition, which comes after the cycle has been traversed once, so after c_θ. ✓
- (YB): at ¬H1, o lies on its honest cycle, whose top is c_θ. The P-vertices would lie on that cycle above c_θ, so there are none.
  ℓ ∈ [1, |U| − 1] by (SP′). ✓

## 1. κ-freeze lemmas: SIGN
- κ-FB-ROUND: this is P-N5-PFZ's FB-ROUND with lengths carried along.
  - Case 1: (M1κ), (Aκ), (M2κ).
  - Case 2: S4c's maximiser x* ⊵ x, then (Aκ) at k + 1 (λ_{k+1}(v) = c_θ ≠ v) and (M2κ), (M1κ).
  - No hypothesis on H1, H2, θ. ✓
- κ-HAT-FREEZE (a), induction on j:
  - The base is z = c_θ.
  - Odd z ∈ Û ∖ {c_θ}: forced, so x = next_t(z), and the hypothesis at t (t > g_j > g_{j−1}).
  - Even z: the hypothesis at k = g_j (k > g_{j−1}), then κ-FB-ROUND at k (x ∈ Û ⊆ U), then (M2κ) from k + 1 to t.
  - wt adds over the simple path. ✓
- κ-HAT-FREEZE (b): z ∈ F_t ∩ U, so z ≠ o, z's honest play avoids o ((HP)), and its prefix to the first T-vertex, which is c_θ, is
  simple ((SP′)). It uses σ_t-edges into Û and forced edges, so it is a path of G_Û. ✓
- κ-HAT-FREEZE (c): simple paths of G_Û have ≤ |U| − 2 edges. (a) at j = |U| − 2 gives ≥ the maximum, (b) gives ≤. ✓
- κ-PFZ:
  - The base j = 0 is z = o.
  - Odd z ≠ o: forced, (Aκ).
  - Even z: k = f^Θ_j ∈ Θ with k > f^Θ_{j−1}. The hypothesis at k uses κ_k(o) = κ(θ_Θ) = κ_t(o). Then κ-FB-ROUND at k (x ∈ U ∖ {c_θ})
    and (M2κ).
  - G_U^o keeps Even edges into U ∖ {c_θ} and makes o a sink, matching the path class. ✓
- κ-Y-FORM: the Y-FORM argument signed in R2-N5-RHO §1, with lengths. V_{σ,τ′}(o) = o ⊕ Ξ_t(y) adds 1 to ℓ, and o ∉ P(Ξ_t y) (y's
  play avoids o). Lemma S (a) and (M1κ) apply; y ∈ F_t ∩ U, so y's value has cycle node c_θ. ✓

## 2. EXIT-SWITCH: SIGN
- The dichotomy is complete. For u ∈ S_U, x*_u ∈ U ((Aκ) at k + 1). If x*_u ∈ T, the play meets T first. Otherwise (SP′) at k gives a
  visit of c_θ, so the k-play from x*_u meets T, and either u comes first or T does.
- The contradiction:
  - The k + 1-play from v ∈ S_U stays in U ((Aκ) at k + 1). It must visit c_θ ((SP′) at k + 1, λ_{k+1}(v) = c_θ).
  - At u ∈ S_U it moves to x*_u.
  - On U ∖ (S_U ∪ T) it takes the k-step: an unswitched Even vertex keeps σ (S4c switches only gate sources), and an Odd vertex in
    U ∖ T is ≠ o, so it is forced.
  - Under the hypothesis, the k-play from x*_u reaches some u′ ∈ S_U before T. So the k + 1-play runs from S_U-vertex to S_U-vertex
    and never meets T. Contradiction. ✓
- The path p_u:
  - It is simple: the prefix to the first T-vertex by (SP′), and it avoids u by the choice of u.
  - Its first edge u → x*_u is an Even edge into Û (e = c_θ forces x*_u ≠ o) or into U ∖ {c_θ} (e = o forces x*_u ≠ c_θ). The other
    edges are σ_k / forced edges inside U.
  - The κ identity is (Aκ) along it. ✓

## 3. FREEZE-EXIT: SIGN
- Both graphs have |U| − 1 vertices, so p_u has ≤ |U| − 2 edges.
- The gate (u, x*_u) gives κ_k(x*_u) > κ_k(σ_k u) by (M1κ): both lie in U at the same state.
- e = c_θ: k = g_j with j ≥ |U| − 1, so k > g_{|U|−2}, and κ-HAT-FREEZE (a) with j = |U| − 2 applies to p_u. That gives
  κ_k(u) ≥ κwt(u) + κ_k(x*_u).
- e = o: k = f^Θ_i with i ≥ |U| − 1, so k > f^Θ_{|U|−2}, and κ-PFZ applies to p_u (a path of G_U^o) at the state k ∈ Θ.
- Both cases contradict (Aκ) at u: κ_k(σ_k u) = κ_k(u) − κwt(u). ✓
- The proof gives slightly more: per switched u of kind c_θ, j ≤ |U| − 2; per switched u of kind o, i ≤ |U| − 2. My checker tests
  these per-vertex forms (FX).

## 4. CN-ONLY: SIGN
- (1) Switched y:
  - U ∖ T is excluded by S_U = ∅. o is Odd. c_θ is a cycle node.
  - y ∉ U: y's honest play misses o ((HP) (ii)), so y ∈ F_k ((HP) (i)). Then FBL-N (ii) (flat: y = λ_W(y)) and G (a) (Ξ = W off R)
    give y = λ_k(y). ✓
- (2) Both ends have empty P:
  - σ_k(y) lies on y's cycle, whose top is y. ✓
  - y ≠ c_θ: λ_k^{-1}(y) avoids o, so it lies in F_k ∖ U. The k-play from x*_y stays in λ_k^{-1}(y). Its non-y vertices are not cycle
    nodes, so by (1)'s argument they are not gate sources, and its Odd vertices are forced. So the k + 1-cycle of y is y · (that path),
    with top y. ✓
  - y = c_θ, play meets c_θ first: same argument with S_U = ∅. ✓
  - y = c_θ, play meets o first:
    - π is unchanged at k + 1, so c_θ's k + 1-cycle contains π and o. So ¬H1 at k + 1, and (YB) gives M_{k+1}(o) = 0.
    - π's vertices lie below c_θ, so (Aκ) gives M_k(x*_y) = M_k(o) ≤ M_{k+1}(o) = 0 ((M2κ), first component of the lexicographic order).
    - The gate gives M_k(x*_y) ≥ M_k(σ_k c_θ) = 0 ((A0κ), (M1κ)).
    - So P = ∅ (INJ). ✓
- (3) Every gate is pinned between the two ends:
  - The reward is injective, so the cycle node is y. The signed weight lies between 0 and 0, so P = ∅. The gate is strict, so it is a
    length change: lev = −1.
  - CN-LAST (R38 (f)) applies, since Iσ_k ≠ ∅. At most one per phase: a second such fallback k′ < k would need k′ + 1 to be the
    phase's last state. ✓

## 5. THETA-AFTER: SIGN
- θ is determined by κ(o) (cycle node c_θ fixed, (INJ)), and κ(o) is non-decreasing (M2κ).
- After g_{|U|−2}:
  - At H1 states, κ(o) ∈ V_H (κ-Y-FORM plus κ-HAT-FREEZE (c) on Y_t ⊆ F_t ∩ U).
  - At ¬H1 states, κ(o) ∈ V_N ((YB)).
- A non-decreasing sequence with values in a set of size ≤ deg_U(o) + |U| − 1 changes at most deg_U(o) + |U| − 2 times.
- The suffix {t > g_{|U|−2}} is contiguous, so the θ-runs meeting it number at most 1 + that count. ✓
- Sharper: y ∈ V_H ranges over succ(o) ∩ Û (κoptÛ is defined on Û), so |V_H| ≤ |succ(o) ∩ Û| ≤ |U| − 1. See N-FBP-2.

## 6. FB-POLY: SIGN (N-FBP-1, N-FBP-2)
- (d) = CN-ONLY. ✓
- (a) The three classes:
  - S_U = ∅: ≤ 1.
  - S_U ≠ ∅, j ≤ |U| − 2: ≤ |U| − 2.
  - S_U ≠ ∅, j ≥ |U| − 1: FREEZE-EXIT's contrapositive gives i ≤ |U| − 2. The θ-run contains g_j > g_{|U|−2}. THETA-AFTER applies
    (≥ |U| − 1 ≥ |U| − 2 fallbacks) and bounds those θ-runs by deg_U(o) + |U| − 1, with ≤ |U| − 2 fallbacks each.
  - The sum is 1 + (|U| − 2)(deg_U(o) + |U|). ✓
- (c) o = c_θ, T = {o}:
  - θ = (o, ∅, 0) throughout, so there is one θ-run.
  - EXIT-SWITCH's proof needs only that the k + 1-play from a switched vertex visits o ((SP′) with c_θ = o).
  - κ-PFZ in G_U, with κ(θ) = (0, 0).
  - Paths have ≤ |U| − 1 edges, so i ≥ |U| gives S_U = ∅. That gives ≤ |U| − 1 + 1. ✓
- N-FBP-1 (wording): the proof of (b) says "U = {o, c_θ}", which assumes o ≠ c_θ. When o = c_θ and |U| = 2 (U = {o, x}; 293 library
  and 7,064 random phases in my data), (c) alone gives only f ≤ 2.
  - The claim f ≤ 1 still holds. If x is Even and switches at k, then both σ_k(x) = next_k(x) and x*_x = next_{k+1}(x) lie in
    U ∖ {x} = {o} ((Aκ) at k and k + 1). Neither can be x, since x ≠ λ(x). So σ_k(x) = x*_x: no switch. So S_U = ∅ at every fallback,
    and (d) applies.
  - Data: max f = 1 in those phases (max_f_o=c_U=2).
  - Suggested proof line: "If o ≠ c_θ, U ∖ T = ∅. If o = c_θ, U = {o, x} and x's successor lies in {o} at every state, so x never
    switches. Either way S_U = ∅."
- N-FBP-2 (precision): (a)'s last step uses "deg_U(o) ≤ n − 1". With a self-loop at o, o ∈ succ(o) ∩ U, and deg_U(o) can reach n.
  - In my file set, 84 of 492 games have a self-loop at o, and 3 have succ(o) = V.
  - The end bound 1 + (n − 2)(2n − 1) still holds: THETA-AFTER's V_H only uses y ∈ succ(o) ∩ Û, so the proof gives
    f ≤ 1 + (|U| − 2)(|succ(o) ∩ Û| + |U|) ≤ 1 + (|U| − 2)(2|U| − 1).
  - Suggested fix: define deg_U(o) := |succ(o) ∩ Û|, or keep the middle bound and derive the end bound from |succ(o) ∩ Û| ≤ |U| − 1.

## 7. Consequence and reading (not signed)
- With FB-POLY, f per phase is polynomial without hypothesis, so X_SN per phase (R34 (f)) is polynomial. Crossings outside SN /
  OUT stretches, OTHER states, S4a steps and phases stay open. G-N5-TIME stays OPEN.
- This is the first per-phase fallback bound that has no hypothesis. The packet's remarks list the earlier conditional ones correctly
  (FB-INT, NH1-FB, EPOCH, PL-S″, LV-PL, OUT-1).

## 9. Data (DATA, not proof)
- Batch (run_all.sh, logs/, totals_logs.txt): 492 𝒞^1O files × own / rand / spec × 3 starts = 4,428 runs; random 𝒞^1O 64,000 runs
  (n 4-14 and 15-30). 1,484 / 1,484 logs "RESULT OK violations=0".
  - Phases: 159,383, of which 47,760 have o = c_θ, and 7,357 of those have |U| = 2 (max f there 1, N-FBP-1).
  - In-phase Even fallbacks 8,643 (library 7,764, random 879). CN-ONLY (S_U = ∅) 973, each followed by the phase's last state and
    at most one per phase. EXIT 7,670. Switched vertices of U ∖ T: kind c_θ 13,085, kind o 270, kind loop 0.
  - SW: the switched set equals the gate sources at every fallback.
  - (Aκ) 3,001,987; (YB) 87,503; κ-Y-FORM 139,928 H1 states; κ-HAT-FREEZE (a) 5,048, (b) 286,906, (c) 27; κ-PFZ 104,199 checks
    (exact DFS, |U| ≤ 12; 26,613 larger phases skipped for these, and counted).
  - THETA-AFTER phases 6,190 (63 with |U| ≥ 3); θ-changes after g_{|U|−2}: max 0.
  - FB-POLY: max f per phase 37 (|U| 48). FB-CAP excess ≤ 0. f = |U| − 2 in 63 phases with |U| ≥ 3; never f ≥ |U| − 1 at |U| ≥ 3.
  - So the FREEZE-EXIT / THETA-AFTER hypotheses are NEVER reached (RECORD_fallbacks_j>=|U|-1_U>=3 = 0), as the packet's §8 says.
  - Note: the counter max_f_minus_U_plus_2_U>=3 was added while the batch ran. It is a maximum only, no check changed, and later
    logs have it. The RECORD counter, present from the start, carries the claim.
- FX slack (run_fx.sh, logs_fx/: the 209 files with EXIT fallbacks, 3 traces, + random 10,000 × 3): the closest kind-c_θ switch has
  j = |U| − 4 (slack 2); the closest kind-o switch has i ≤ |U| − 12.
- Mutation controls (logs_mut/): FBP_MUT=fx on 60 EXIT files (own), on the 8 files with |U| = 3 fallback phases (spec), and on random
  seed 412 (spec): 0 violations, because no data come within 1 of FREEZE-EXIT's per-vertex bounds. So I could not show the FX check
  biting. No mutation of the CN or TA checks was run.
- Climbs (run_climbs.sh, FIT frz toward |U| ≥ 3 phases with f ≥ |U| − 1; 1,500 s each):
  - The first run of 4101 STOPPED at a bug in MY checker: for o = c_θ it tested p_u against Û instead of G_U (packet (c)). That is a
    checker bug, not a finding (climb/frz_4101_checker_bug.txt, climb/viol_frz_4101.pg). Fixed in fbpoly_check.py (line marked);
    the climb's own evaluation of that game then gives 0 violations, with 2 kind-o switches at o = c_θ checked by FX(c). The batch
    never met that case (it could only produce violations, and the batch had none).
  - 4101 re-run (random n 6-10) and 4102 (seed R2-N5-RHO/climb/best_rho_9701.pg, a |U| = 3 post-freeze climb output): 480,528
    evaluations, 1,922,112 runs, 0 violations.
    - Fallbacks: EXIT 694k (275,897 + 418,465 per run), CN 151,052. Switched U ∖ T: kind c_θ 758,578, kind o 10,149, kind LOOP 31.
    - κ-HAT-FREEZE (c) 16,008 checks.
    - max f per phase 3. f − (|U| − 2) ≤ 0 at |U| ≥ 3. A kind-c_θ switch reached j = |U| − 2 (FX slack 0) in 4101; it was not saved,
      so the mutation could not be re-run on it. THETA-AFTER changes 0.
  - The hypotheses of FREEZE-EXIT / THETA-AFTER were not reached by either climb.
- NEW DATA on §7's OPEN question (not a signed item): EXIT-SWITCH's excluded branch DOES occur for SOME switched vertex.
  - The packet says "it never occurs in data (0 of 1,544 switched vertices of U ∖ T)". My climbs found 31 kind-loop switched vertices,
    each at a fallback where another switched vertex was of kind c_θ or o, as EXIT-SWITCH proves.
  - Witness climb/loop_4102.pg (sha1 016473b411a63c62260845015025876eba9816af, n 8, o = 2, succ(o) = {0, 1, 7}). The event is in
    climb/loop_4102_event.txt: the climb's evaluation with seed 4102, trace 2 (mode rand), start σ0 = [3, 1, 1, 2, 5, 1, 2, 1],
    τ0 = [3, 1, 0, 5, 5, 1, 2, 0]; fallback k = 1, c_θ = 1, U = V, H1.
    - u = 3 switches to x* = 7, and the k-play 7 → 0 → 3 returns to u: kind LOOP.
    - u = 7 switches to x* = 4, and 4 → 5 → 1 = c_θ: kind c_θ.
  - So "impossible for some switched vertex" is FALSE. "Impossible for all" (EXIT-SWITCH) stands. This matters for (FB-CAP-1)-type
    arguments that would want every switched vertex to exit.

## 10. Notes for the lane (none blocks a signature)
- N-FBP-1 (wording): FB-POLY (b)'s proof for o = c_θ, |U| = 2 (§6).
- N-FBP-2 (precision): deg_U(o) ≤ n − 1 fails with a self-loop at o; use |succ(o) ∩ Û| (§6).
- N-FBP-4 (DATA, for §7): EXIT-SWITCH's excluded branch occurs for SOME switched vertex. Witness climb/loop_4102.pg (§9). The §7
  sentence "it never occurs in data" no longer holds.
- N-FBP-3 (DATA): FREEZE-EXIT / THETA-AFTER at |U| ≥ 3 stay unreached in my batch and climbs as well (§9). This is a target for L-RED.
  FB-CAP's (f ≤ max(1, |U| − 2)) excess is ≤ 0 in all my data. It is 0 (f = |U| − 2) in 63 phases with |U| ≥ 3.

## §C. Comparison with REFEREE: docs/referee/R-N5-FBPOLY.md (REFEREE successor 10; report referee 3de7cab7, §C d6248f7b; sha1 e4389a59 on my tree)
REFEREE-2 successor 12, written 2026-10-25 22:1xZ (date -u). Opened only after this report (2fef7c4a) was pushed. (Opus 5.5, D15).
- Verdicts: identical in substance. Both referees sign κ-FB-ROUND, κ-HAT-FREEZE (a)-(c), κ-PFZ, κ-Y-FORM, EXIT-SWITCH, FREEZE-EXIT, CN-ONLY,
  THETA-AFTER and FB-POLY (a)-(d); neither signs §7, §8 or the §6 Remarks. No (P) on either side.
- The two §6 defects were found independently, with the same repairs:
  - REFEREE FBP-1 (+ FBP-N1) = my N-FBP-2: a self-loop at o makes deg_U(o) = |succ(o) ∩ U| reach n. THETA-AFTER's V_H is indexed by
    succ(o) ∩ Û, so f ≤ 1 + (|U| − 2)(|succ(o) ∩ Û| + |U|) ≤ 1 + (n − 2)(2n − 1). Same line as mine.
  - REFEREE FBP-2 = my N-FBP-1: at o = c_θ, |U| = 2, U = {o, v}, next(v) = o at every state (a self-loop would make v its own cycle
    node), so v never switches, S_U = ∅, and (d) gives f ≤ 1. Same argument as mine (§6), checked again: a switch at k needs x*_v ∈ U ∖
    {σ_k v} by (Aκ) at k + 1, i.e. x*_v = v, a self-loop, against λ_{k+1}(v) = o (in phase).
  - REFEREE's data attribution is right: 84 of my 492 games have a self-loop at o, 3 have succ(o) = V; 293 + 7,064 = 7,357 phases with
    o = c_θ, |U| = 2, max f 1.
- Labels: REFEREE wrote "SIGNED WITH GAP" for (a)'s end bound and (b), and signs without a gap once the two one-line repairs are in the
  fixes file. I wrote SIGN with notes, because the statements are true and the repairs are one line each. I accept REFEREE's form: the
  two lines go into the L-NEW fixes file; with them, both referees sign FB-POLY (a)-(d) unconditionally. Until then the joint form is
  REFEREE's (a)'s middle bound and (c), (d) as written; (a)'s end bound and (b) with the stated one-line proofs.
- FBP-N2 (wording, (YB) from z = o): ACCEPTED. My §0 checked (YB) with "ℓ ∈ [1, |U| − 1] by (SP′)"; what (YB) uses is the lasso part of
  (SP′)'s proof (o's honest path to c_θ is simple), as REFEREE says. The lane should say so.
- FBP-N3 (scope): identical to my header (G-N5-TIME open; the §6 Remarks' consequences are readings).
- FBP-N4 and N-FBP-4: REFEREE re-ran my witness climb/loop_4102.pg (sha1 016473b4) on its engine from my start pair (1 fallback, kinds
  c_θ 1 + loop 1, EXIT-SWITCH holds) and with 300 random starts (loop kind 24 of 35 fallbacks). ACCEPTED: the packet's §7 line "the loop
  branch never occurs in data" is out of date for single switched vertices; EXIT-SWITCH's "some u exits" is what holds.
- N-FBP-3 = REFEREE's untested-regime line: FREEZE-EXIT / THETA-AFTER at |U| ≥ 3 with j ≥ |U| − 1 is unreached in both referees' data
  (mine: batch + climbs; REFEREE: 3.82 M climb candidates, best one fallback short). Both rest on the proofs; a target for L-RED.
- REFEREE's mention of my checker bug (o = c_θ tested against Û instead of G_U, caught in a climb, fixed before the batch) is accurate.

| item | REFEREE-2 | REFEREE | outcome |
| --- | --- | --- | --- |
| (a) end bound, self-loop at o | N-FBP-2 | GAP FBP-1 + FBP-N1 | same finding, same repair; fixes-file line |
| (b) at o = c_θ, \|U\| = 2 | N-FBP-1 | GAP FBP-2 | same finding, same repair; fixes-file line |
| (YB) from z = o | §0 via (SP′) | FBP-N2 (wording) | ACCEPTED |
| EXIT-SWITCH loop branch for some vertex | N-FBP-4 (witness loop_4102.pg) | re-run: confirmed | agreed; §7 sentence out of date |
| FREEZE-EXIT / THETA-AFTER regime | N-FBP-3 unreached | unreached | agreed; L-RED target |
| scope / consequences | reading | FBP-N3 | agreed |
No disagreement remains. Joint gap map: one row (FBP-1 = N-FBP-2, FBP-2 = N-FBP-1), closed by the agreed repairs. No verdict of mine
changes. (Opus 5.5, D15)
