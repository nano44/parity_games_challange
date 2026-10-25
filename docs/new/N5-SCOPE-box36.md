# N5 on o-cyclic 𝒞^1O, box 36: the cross-scope-run count (scope runs per phase, fallbacks outside scope runs, level −1 residue)
L-NEW successor 15 (Opus 5.5, D15/D18). Box 36 GO by the Lead 09:42Z (Lead's stamp). Written 2026-10-25 09:4xZ onward by date -u.
- Setting: P-N5-SN §0, P-N5-FBW §0, P-N5-TOG §0. SCOPE RUN (R29 §0): a maximal run of in-phase transitions k → k+1 with (h) at k, H2 at
  k+1 and w_{k+1} = w_k. T := #H1-toggles of the phase (P-N5-TOG §4: T ≤ |U|(n + 1) + n − 1). X := #crossing transitions. f := #fallback
  transitions. n_E := #Even vertices.
- Labels (D18/L40): PROVED (L-NEW succ. 15, unrefereed), CONJECTURE, OPEN, DATA. Nothing here is a running-time bound for N5, a TARGET.md
  claim or a step-4 pass. G-N5-TIME stays OPEN.

## Summary
1. **Remark KEY (PROVED, trivial).** λ_U, the cycle-node map of Odd's valuation of τ, is a function of τ alone. So a (λ_Ξ, τ)-phase IS a
   joint λ-phase (λ_Ξ, λ_U, τ). Every result signed under R21's joint key (R19-R29, e.g. F1°, TC, NL) holds on (λ_Ξ, τ)-phases verbatim. The
   case-by-case transfer arguments (REFEREE's NL note, N-OE-3, R30's WM) are therefore all instances of one line.
   DATA: scopecnt.py, 0 transitions with τ constant and λ_U changing, in 1,419 library phases and 39,777 random phases.
2. **Lemma WCH (PROVED).** In a phase, the transitions with H2 at both ends and w changing number ≤ (n − 2)(X + 1) + X.
3. **Corollary SCOPE-COUNT (PROVED).** Scope runs per phase ≤ #(h)-runs + WCH ≤ (1 + T + f) + (n − 2)(X + 1) + X.
4. **Lemma FB-INT (PROVED, from signed R25 (d), R25 (e) J1, R28 (b) OE).** Inside a phase, every maximal run of consecutive non-crossing
   transitions contains ≤ n_E(2n − 1) fallbacks.
5. **Corollary NH1-FB (PROVED).** Fallbacks at ¬H1 states of a phase ≤ n_E(2n − 1)(⌈T/2⌉ + 1) + T ≤ poly(n). No X and no f.
6. **The rest of the out-of-scope fallbacks (OPEN; obstruction named).** The other kinds are fallbacks at H1 ∧ ¬H2 states, at OTHER states
   (H1 ∧ H2 ∧ ¬H3), and at the end of a scope run.
   - Each kind lives outside the SN regime (c_w ≠ c_θ). There R only grows at S4a steps (R-STICK), and fallbacks evict.
   - So the f ↔ X loop of (L1) reappears without (h), where the scope-run machinery (NL, CLS1, MINSET, NJB) does not apply.
   - DATA: these are 113 of the library's 1,022 in-phase fallbacks, at most 12 in one phase (wd16_s2, n 16, τ(o) = o). In random games
     there are 29, all at scope ends.
7. **(iii) Level −1 residue: no short argument found (OPEN).** FB step (3) gives ≤ n_E(n − 1) level −1 fallbacks per tame run. CN-LAST
   handles the own-cycle-node case. A per-scope-run count of the non-own case needs that level −1 blocks are not re-entered across
   crossings, which is the same reset as in item 6.

## 1. Remark KEY (PROVED, L-NEW succ. 15)
- U := Ξ^d(τ), Odd's valuation of τ on the dual game, is computed from τ alone (SPEC S1, "Odd's side"; experiments/si/si.py evaluate on
  the dual strategy). So λ_U is constant on every run with τ constant.
- Hence "λ_Ξ and τ constant" (the phase of R27-R30, P-N5-SN onward) and "λ_Ξ, λ_U constant, τ constant" (R21's joint λ-phase) are the same
  runs.
- DATA: scopecnt.py checks λ_U at every transition with τ(o) unchanged. 0 changes in 1,419 library and 39,777 random phases.

## 2. Lemma WCH and Corollary SCOPE-COUNT (PROVED, L-NEW succ. 15)
**Lemma WCH.** Let k → k+1 be a transition of a phase with H2 at k and at k+1 and w_k ≠ w_{k+1}. Then it is a crossing, or it changes Ξ at
t0 := τ(o) ∈ F_k = F_{k+1}. Hence such transitions number ≤ (n − 2)(X + 1) + X per phase.
Proof.
- Under H2, o lies on no W-cycle, so (V1) at o gives w = W(o) = o ⊕ W(t0), and t0 ∈ F (TC (i): H2 ⟺ τ(o) ∈ F).
- Off R̄, W = Ξ (R19 (a), statewise). So w_k = o ⊕ Ξ_k(t0) and w_{k+1} = o ⊕ Ξ_{k+1}(t0), with t0 the same vertex (τ is constant in a phase).
- If w_k ≠ w_{k+1}, then Ξ_k(t0) ≠ Ξ_{k+1}(t0).
- Unless the transition is a crossing, it lies in a crossing-free interval I with t0 ∈ F. By R22 (a) F1° (on (λ_Ξ, τ)-phases by Remark
  KEY), at most |F| − 1 ≤ n − 2 transitions of I change Ξ on F. A phase has ≤ X + 1 crossing-free intervals. □
**Corollary SCOPE-COUNT.** The number of scope runs of a phase is ≤ #(h)-runs + WCH ≤ (1 + T + f) + (n − 2)(X + 1) + X.
Proof.
- Let a scope run start at transition k. Then (h) holds at k.
- Either k is the first state of its (h)-run, or (h) holds at k − 1, so H2 holds at both k − 1 and k, and the transition k − 1 → k is not in
  scope. That forces w_{k−1} ≠ w_k: a WCH transition.
- The (h)-runs are ≤ 1 + T + f by P-N5-TOG §6 (RESTARTS). □
- DATA (scopecnt.py; data/scopecnt_lib.txt, data/scopecnt_rand.txt). 0 failures of SCOPE-COUNT, WCH and RESTARTS.
  - Max per phase, library: 5 scope runs (so_th_n32), 4 (h)-runs (tog6a_n32), 20 WCH at n 24 with X = 2 (sc24), against the bound
    22·3 + 2 = 68.
  - Max per phase, random: 2 scope runs, 1 (h)-run, 2 WCH.

## 3. Lemma FB-INT and Corollary NH1-FB (PROVED, L-NEW succ. 15)
**Lemma FB-INT.** Inside a phase, a maximal run Q of consecutive transitions none of which is a crossing contains ≤ n_E(2n − 1) fallbacks.
Proof.
- Every non-tame transition is a crossing. By R25 (e) J1, a non-tame transition switches σ̄(o) at a level > M_k, and that change is relevant.
  By R28 (b) OE, a non-crossing transition has O_k ≤ E_k ≤ M_k. This is R28 (c) (ii)'s own proof (P-N5-OE §4 (ii)).
- So Q lies inside one tame run, and the proof of R25 (d) Theorem FB, steps (1)-(4), bounds the fallbacks of a tame run by n_E(2n − 1). □
**Corollary NH1-FB.** The fallbacks of a phase taken at ¬H1 states number ≤ n_E(2n − 1)(⌈T/2⌉ + 1) + T.
Proof.
- By R-CONST (P-N5-L2 §11, signed by both referees), R̄ = λ^{-1}(c_θ) at every ¬H1 state. So a transition with both ends ¬H1 is not a crossing.
- A maximal run of consecutive ¬H1 states therefore spans a crossing-free stretch, with ≤ n_E(2n − 1) fallbacks by FB-INT. There are
  ≤ ⌈T/2⌉ + 1 such runs.
- A fallback at a ¬H1 state whose next state has H1 is a toggle: ≤ T. □
- DATA: library 11 fallbacks at ¬H1 states, random 338. 0 cases above the bound.

## 4. The rest of the out-of-scope fallbacks (OPEN; the obstruction)
- Classification of in-phase fallbacks (scopecnt.py):
  | kind | library | random (20,000 games, n 4-14) |
  | --- | --- | --- |
  | IN (inside a scope run) | 898 | 334 |
  | ¬H1 at k (NH1, §3) | 11 | 338 |
  | H1 ∧ ¬H2 at k | 107 | 0 |
  | OTHER, H1 ∧ H2 ∧ ¬H3 | 2 | 0 |
  | END: (h) at k, ¬H2 at k+1 | 4 | 29 |
  | END: (h) at k, w changes | 0 | 0 |
- END fallbacks. Each ends a scope run or an (h)-run, so they are ≤ #scope runs ≤ SCOPE-COUNT (PROVED, as a count in T, f and X).
- H1 ∧ ¬H2 and OTHER fallbacks. In both, c_w ≠ c_θ:
  - under H1 ∧ ¬H2, c_w ∈ R̄ while c_θ ∈ F (the H2-STICK proof);
  - OTHER is ¬H3 by definition.
  So these states are outside the SN regime. R-STICK (R30 (c)) makes R only grow at S4a steps, and SN-PREFIX gives ≤ n − 1 crossings
  per fallback-free run there.
  - With FB-INT: such fallbacks ≤ n_E(2n − 1)(X_out + 1), and X_out ≤ (n − 1)(f_out + 1) + f_out. That is the same loop as (L1), with no
    (h), so no u*, NL, CLS1 or MINSET.
  - EXACT OBSTRUCTION: FB's per-tame-run count resets at every crossing, and in this regime crossings are only re-entries after fallback
    evictions. Nothing proved charges an eviction-then-re-entry pair to a monotone quantity.
  - Under τ(o) = o (91 of the 104 H1 ∧ ¬H2 fallbacks in box 35's survey), w = (o, ∅, 0) is constant. So the regime is a fixed-target
    "reach o" game in the W frame against "reach c_θ" in the honest frame. It is the cleanest test case for a new argument.
  - DATA: wd16_s2 (n 16, τ(o) = o): 12 such fallbacks in one phase with X = 12, T = 0. Random games: none.
- CONJECTURE OUT-POLY (DATA only): fallbacks at H1 ∧ ¬H2 and OTHER states are poly(n) per phase. Not attacked by any climb yet. The
  natural climb is fbtclimb-style fitness = #H1 ∧ ¬H2 fallbacks in one phase, seeded from wd16_s2 and wd12_s1.

## 5. (iii) Level −1 fallbacks with a non-cycle-node gate (OPEN; one look)
- What is proved:
  - R25 (d) step (3): a level −1 block has ≤ n_E(n − 1) fallbacks, so per tame run, and by FB-INT per crossing-free stretch.
  - CN-LAST (N5-DROP-box35 §7): the own-cycle-node case ends the phase.
- The only example, box28/out/oc12_s1 at k = 6:
  - states 5-7 have M = −1 with length-only gates at non-cycle nodes (0 → 7, then 7 → 8). Their cycle node 1 is odd, so longer is better;
  - at 8 the phase ends with M = 9;
  - all are ¬H1 states, so NH1-FB (§3) already counts them.
- A short argument for a per-scope-run count would need that a level −1 block is not re-entered after a crossing. The same reset as in §4
  blocks this. No short argument found.

## 6. Data and scripts (DATA; experiments/new/box35, where box-35 tools live)
- scopecnt.py (this box): SCOPE-COUNT, WCH, RESTARTS, Remark KEY, the fallback classes. Logs data/scopecnt_lib.txt (library +
  box34/box35 instances + experiments/red + experiments/si/coarse + docs/referee/R-N5-L2 instances) and data/scopecnt_rand.txt (seed 3561).
- Every script asserts exactly one Odd vertex of out-degree > 1.

## 7. OUT-POLY climbs (DATA)
- outclimb.py, 25 min each. Fitness = (max fallbacks at H1 ∧ ¬H2 or OTHER states in one phase, crossings in that phase).
  - seed 3631 from wd16_s2 (n 16): starts at (12, 12) and ends at (12, 21) after 386,754 mutations. Only the crossings grew; the fallback count
    did not.
  - seed 3632 from wd12_s1 (n 12): starts at (7, 7) and ends at (7, 13) after 683,765 mutations.
- So the count did not grow past the seed's value in either climb. It is below n in both cases, and the margin did not shrink. This is weak
  evidence for OUT-POLY with a linear constant. Climbs are local, and the obstruction (§4) is unchanged. The climb bests are in out/
  (gitignored); they were not copied, since they show no new maximum.

## 8. Note (added while parked, at the Lead's request 10:20Z): the linear PF-THETA is FALSE (DATA, verified)
- experiments/red/so/instances/pftheta_cex_n32.pg (sha1 9f526135e272fabcb38c1cc24a99a4418717f7ed; L-RED 15, climbed from pf_best_3621).
  - It has 33 θ-changes after its only fallback, inside one scope run, at n 32.
  - Re-run here: n5.py n5 38 / 1; check_sol2.py "zielonka(oink zlk) OK strategies verified"; pfclimb.fit (33, 1).
- Scope of the kill: all 33 are in ONE fallback-free run. There the per-run machinery already gives a poly(n) bound: X-RUN (crossings)
  plus R27 TH (≤ n θ-changes per crossing-free interval). So only the constant 1 dies. The poly form of PF-THETA (N5-DROP-box35 §8) is
  untouched.
