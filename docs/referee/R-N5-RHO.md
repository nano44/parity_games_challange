# R-N5-RHO: REFEREE report on packet P-N5-RHO (box 40: Y-FORM, HAT-FREEZE, RHO-TAIL, BF-F, FREEZE-F, RHO-HN, Corollary HN-POLY)
Referee: REFEREE (successor 10, session_01J4kmfDqtZdanh3RSCxChyD), Opus 5.5 (owner ruling D15, Lead reading L37).
- Routing: the Lead's message of 16:54Z (Lead's stamp). It starts R-N5-RHO now; the PFZ-ext and LV2 §Cs wait for REFEREE-2 10's SHAs.
- Object: docs/new/P-N5-RHO-box40.md at trunk c814455 (added at 3e9fe5c2), sha1 cd5df65c2f3e6829f85739a57023fc3da6944baa (checked with
  `git show c814455:docs/new/P-N5-RHO-box40.md | sha1sum`), 269 lines. Author: L-NEW successor 19 (from successor 18's N5-RHO-box39.md).
- Written 2026-10-25T17:21Z-17:40Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: I did not read any docs/referee-2/R2-N5-RHO* file. D1: each statement treated as wrong until its proof was
  checked line by line. Tools: my own N5 engine (scratch/rl_engine.py, written from the SPEC text) and a new probe; no lane code.

## Verdicts
| packet § | statement | label | verdict (Opus 5.5, D15) |
| --- | --- | --- | --- |
| §0 | Facts (A), (A0), (M1′), (M2′), (INJ), FB-ROUND, (HP), (SP) as restated | used | checked (FB-ROUND re-proved here; its signature stays with P-N5-PFZ) |
| §1 | Lemma Y-FORM (a), (b) | PROVED | SIGNED |
| §2 | Lemma HAT-FREEZE (a)-(c) | PROVED | SIGNED (note RHO-N1) |
| §3 | Theorem RHO-TAIL | PROVED | SIGNED (note RHO-N1) |
| §4 | Lemma BF-F | PROVED | SIGNED |
| §5 | Theorem FREEZE-F (a)-(c) | PROVED | SIGNED |
| §6 | Theorem RHO-HN | PROVED | SIGNED |
| §6 | Corollary HN-POLY | PROVED, conditional on P-N5-PFZ-ext BRK-POLY′ | SIGNED, conditional as labelled: on BRK-POLY′ (i′) and (ii)'s window bound B_S ≤ θ_S + (ρ_S + 1)(|U|² − 1) (P-N5-PFZ-ext §3, in review). Its τ(o) = o line: note RHO-N2 (citation) |
| §7, §8 | N_HN for τ(o) ≠ o, OPEN items, data | not to sign | not signed |
- No (P). Labels are exact. Premises used: (V1), (F1) (R17 (a)); R15 (a), (d); Lemma S (a) (R18 (d); its gaps S1, S2 are citation
  items, "none open as mathematics") or XW (R21 (a)); G (a) (R19 (a)); KEY (R38 (a)); SPLIT, F-FLAT, EPOCH (R39 (a)-(c); EPOCH's premise
  FB-INT is R38 (d)); NE-COUNT (c) (R39 (f)) / TOGGLE-COUNT (R34 (e)). All landed. From P-N5-PFZ: (A), (M1′), (M2′), FB-ROUND, restated
  with proofs and checked here; from P-N5-PFZ-ext: BRK-POLY′ (i′), (ii) only, in HN-POLY.
- HN-POLY uses only the weak form (i′) θ_S ≤ ρ_S + (ρ_S + 1)·max(|U| − 2, 0). That is what P-N5-PFZ-ext's proof gives as written (my
  predecessor's R-N5-PFZ §3, GAP PFZ-1). So HN-POLY does not depend on PFZ-1's repair. Its algebra was checked: ρ_S + (ρ_S + 1)(|U| − 2) +
  (ρ_S + 1)(|U|² − 1) ≤ (ρ_S + 1)(|U|² + |U| − 2) ≤ (ρ_S + 1)(2n² − 1).
- No gaps. Notes RHO-N1 (wording), RHO-N2 (citation), RHO-N3 (data).
- VACUOUS OR THIN IN DATA (lesson N-ENT-2; my data, file sets in §8): FREEZE-F (b) is VACUOUS in the library (no fallback-free HN run is
  longer than |U| − 2 transitions). HAT-FREEZE (c) and RHO-TAIL past the hat freeze occur at |U| = 2 (library) and |U| = 3 (5 lane
  climb phases) only, with 0 P(θ)-changes there. BF-F's Case 2 sub-cases "x ∈ R̄_k" and "x's play passes v" never occur (proved
  impossible). My climbs toward these regimes: §8.2.

## 0. The restated facts
- (A), (M1′), (M2′), (INJ): as signed in R-N5-PFZ §1. (INJ): each rank > rank(c_θ) carries a fixed sign, so the highest differing
  vertex decides the sum; the signed weight is injective on such sets.
- (A0) is correct: next_t(c_θ) lies on c_θ's own cycle, whose top is c_θ, so its P is empty; wt(c_θ) = 0.
- FB-ROUND, re-checked:
  - First case: Ξ_k(σ_k v) has cycle node c_θ by (A), so (M1′) applies to the pair.
  - Second case: S4c switches every Even vertex with an improving edge to its best improving successor x*, so σ_{k+1}(v) = x*.
  - Correct. The signature belongs to P-N5-PFZ; this packet's use is self-contained.
- (HP) is correct. Every Odd vertex except o is forced, so the honest play and the (σ, τ)-play differ only at o. Under H1, c_θ lies on
  o's honest cycle, which avoids o, so c_θ ∈ F.
  - The route form: if o's honest play met π_z at some p, the (σ, τ)-play from p would reach o, and so would the honest play from p.
    That contradicts H1. So R̄ ⊆ U under H1.
- (SP) is correct. The honest play to c_θ is simple: c_θ is reached before any repetition, since the cycle contains c_θ.
- §0's classification is correct: an in-phase transition keeps τ, so it is an S4a step or an Even S4c fallback.
  - An S4b change or an Odd fallback changes τ.
  - Checked at 5,996 library transitions (CLS, §8).

## 1. Y-FORM: checked
- (a), Y_t:
  - σ̄_t(o)'s honest play is the tail of o's honest play. Under H1 it never visits o.
  - By (HP) its (σ, τ)-play is the same play, so σ̄_t(o) ∈ F_t. By (A), σ̄_t(o) ∈ U.
- (a), the bound M_t(o) ≤ wt(o) + M_t(y):
  - τ′ changes only o. Then y's (σ_t, τ′)-play avoids o, so V_{σ_t,τ′}(y) = W_t(y) = Ξ_t(y) (G (a)).
  - o's play under τ′ is o · (y's play), so V_{σ_t,τ′}(o) = o ⊕ Ξ_t(y), with cycle node c_θ, and o ∉ P(Ξ_t y).
  - Lemma S (a) gives Ξ_t(o) ⊴ V_{σ_t,τ′}(o). This is the pointwise minimum over every Odd strategy, not only the current τ. R21 (a)'s
    bracket gives the same.
  - (M1′) with ⊕'s rule, which adds o iff rank(o) > rank(c_θ), i.e. iff wt(o) ≠ 0, gives the inequality.
  - Correct.
- (b) is correct. o lies on its honest cycle, whose top is c_θ, so the path from o to c_θ runs inside the cycle and has no vertex above
  c_θ.
- Data: 6,335 H1 states and 651 ¬H1 states in the library, plus 25 + 2 on the lane climbs, all exact. 0 failures.

## 2. HAT-FREEZE: checked
- (a), induction on j:
  - Base: "t > g_0" means every state, and a 0-edge path is z = c_θ.
  - Even z: the level-(j − 1) hypothesis is applied at the state k = g_j. Since k ≥ g_{j−1} + 1, it applies there. FB-ROUND at k, then
    (M2′) from k + 1 to t.
  - Odd z ≠ o: z is forced, so next_t(z) = x. Apply (A) at t and the hypothesis at t.
  - p is simple, so z ∉ p′ and the weights add.
  - Neither branch uses θ, H1 or H2. Correct.
- (b) is correct. z ∈ F_t gives an honest play that avoids o ((HP)) and is simple up to c_θ ((SP)). Its vertices are in Û. Even
  vertices follow σ_t into U ∖ {o}; Odd vertices other than o are forced. So it is a path of G_Û, and (A), (A0) give its weight.
- (c) is correct. A simple path of G_Û has at most |Û| − 1 = |U| − 2 edges. Each y ∈ F_t ∩ U has y ≠ o, so y ∈ Û.
- RHO-N1 (wording, no gap): "If |U| = 1, o = c_θ" names only one case of o = c_θ.
  - o = c_θ with |U| ≥ 2 occurs: 89 of the 990 library phases.
  - Then c_θ ∉ Û, and G_Û's "c_θ is a sink" has no vertex to refer to.
  - All statements still hold, vacuously:
    - every z ∈ U ∖ {o} has an honest play that reaches o, so F_t ∩ U = ∅ ((HP)), and (b), (c) are empty;
    - H1 never holds, so M(o) = 0 throughout (Y-FORM (b)), and RHO-TAIL, RHO-HN hold with 0.
  - Suggested wording: "If o = c_θ (in particular if |U| = 1), H1 fails at every state of the phase and θ is constant."
- Data: (a) 1,127 + 22 checks against the exact best path of G_Û with ≤ j edges (|U| ≤ 14). (b) 2,517 + 84. (c) 38 at |U| = 2 and 10 at
  |U| = 3. 0 failures.

## 3. RHO-TAIL: checked
- Past g_{|U|−2}, M(o) takes values in {0} ∪ {wt(o) + MoptÛ(y) : y ∈ succ(o) ∩ U}, at most deg(o) + 1 numbers.
- M(o) is non-decreasing ((M2′) at o ∈ U), and (INJ) identifies its changes with the P(θ)-changes.
- Correct. The bound counts every in-phase transition after the freeze, at H1 states or not.

## 4. BF-F: checked
- F_{k+1} ⊆ F_k: SPLIT (R39 (a)) with HN at k, and o ∈ R̄ at both states.
- Case 1 is (A) at k plus (M2′).
- Case 2:
  - (M1′) turns the strict inequality of M into ▷ for two valuations with cycle node c_θ. So (v, x) ∈ Iσ_k, and σ″ is a strategy of
    the S4a arena H_k.
  - σ_{k+1} is H_k's optimum against τ. In-phase non-fallback ⇒ S4a really switched; the S4b part leaves τ unchanged.
  - So (F1) gives W_{k+1} ⊵ W_{σ″} pointwise.
- x ∈ R̄_k:
  - ¬H2 at k puts o on C_W, and C_W ⊆ R̄_k. x's play stays in R̄_k, so it avoids v ∈ F_k and is unchanged under σ″.
  - So W_{σ″}(v) has cycle node c_w. c_w ∈ R̄_k and c_θ ∈ F_k, so c_w ≠ c_θ.
  - XW at o gives θ ⊴ w. Rewards are distinct per vertex, so reward(c_θ) < reward(c_w): a contradiction with (F1).
  - Correct.
- x's play passes v:
  - It is x's honest play (it avoids o), so (A), (A0) apply along q · v. The A0 step is needed when q passes c_θ, which happens when v
    lies on c_θ's cycle.
  - The vertices of q are distinct (a lasso prefix up to the first v), so wt(q) is a set sum.
  - wt(q ∪ {v}) > 0 makes the top of A positive, i.e. even. The vertices of C ∖ A, including c_θ if it is on C, are below it, so it is
    C's top.
  - Its reward is +pp > ±pp(c_θ): a contradiction with (F1).
  - Correct.
- x's play avoids v: v ⊕ Ξ_k(x), with v ∉ P(Ξ_k x), and (M1′). Correct.
- The three sub-cases exhaust x ∈ U, and x = o falls under R̄_k. The hypothesis HN at k + 1 is indeed unused.
- Data: 28,394 + 10 checks. Case 1: 27,932 + 10; Case 2, play avoids v: 462; the two impossible sub-cases: 0. 0 failures. The setting
  "HN at k only" never occurs in my data.

## 5. FREEZE-F: checked
- (a):
  - F shrinks along the run (SPLIT) and c_θ ∈ F ((HP)), so a path of G[F_{t+1} ∩ U] is a path of G[F_t ∩ U].
  - Even step: BF-F. Odd step: (A) at t + 1 and (M2′). Correct.
- (b):
  - |F_t ∩ U| ≤ |U| − 1, because o ∉ F. So every simple path of G[F_t ∩ U] has ≤ |U| − 2 ≤ t − s edges.
  - The honest path of z lies in G[F_t ∩ U], because suffixes of an o-avoiding play avoid o.
  - So M_t = MoptF_t, and the sandwich across t ≤ t′ follows (F_{t′} ⊆ F_t means fewer paths). Correct.
- (c):
  - At t ≥ t*, Y-FORM (a) gives M_t(o) = wt(o) + min over Y_t of values that are fixed by (b).
  - Y_t shrinks and stays non-empty, since σ̄_t(o) ∈ Y_t. A minimum of fixed numbers over a shrinking set is non-decreasing and takes at
    most |Y_{t*}| ≤ deg(o) values.
  - Correct.
- Data: 212 maximal fallback-free HN runs, 91 with more than one state. (a): 310 checks against exact G[F_t ∩ U] paths. (c): at most 13
  changes in a run (epsseg_cex_n48, as the lane reports). 0 failures.
  - (b) is VACUOUS in the library. So the second term of (c) is never exercised there: 0 changes after s + |U| − 2.

## 6. RHO-HN and HN-POLY: checked
- RHO-HN's classification:
  - F-FLAT removes fallbacks; RHO-TAIL covers t > g_{|U|−2}.
  - Every other P(θ)-changing HN → HN transition is an S4a transition with t < g_{|U|−2}.
- Each lies in a maximal fallback-free HN run starting at an HN-stretch start or at g_j + 1 with j ≤ |U| − 3. So there are at most
  N_HN + max(|U| − 3, 0) runs. For |U| = 2 this class is empty, because g_0 = every state.
- FREEZE-F (c) gives |U| + deg(o) − 3 per run, for |U| ≥ 2. The sum is below the stated bound. Correct.
- HN-POLY:
  - Σ_S ρ_S ≤ ρ_HN.
  - The weak-form chain, checked above.
  - EPOCH summed over stretches.
  - "fallbacks at HN states ≤ Σ f_S + N_HN": a fallback from an HN state is inside its stretch or is its last transition.
  - Orders: ρ_HN = O(n²·N_HN) when N_HN ≥ 1, ρ_HN = 0 when N_HN = 0, Σ B_S = O(n⁴·N_HN), Σ X_S = O(n⁵·N_HN), fallbacks O(n⁷·N_HN).
  - Correct.
- RHO-N2 (citation, no gap): the τ(o) = o line cites NE-COUNT (c), RESULTS R39 (f). R39 (f) is signed for τ(o) = o in case A only, but
  the line is used for every τ(o) = o, case B included.
  - The bound holds in case B as well. τ(o) = o makes o's (σ, τ)-play the loop o → o, so ¬H2 holds at every state and HN = H1. An H1
    run that is not the phase's first starts with an H1-toggle, and the H1 runs alternate with the ¬H1 runs. So N_HN ≤ ⌊T_ph/2⌋ + 1,
    with T_ph ≤ T ≤ n² + 2n − 1 by TOGGLE-COUNT (RESULTS R34 (e), every phase).
  - Suggested citation: "R34 (e), with HN = H1 when τ(o) = o", in place of R39 (f) (c) alone.
  - Data: ¬H2 at every state of every τ(o) = o phase, and N_HN ≤ ⌊T_ph/2⌋ + 1 in every such phase, both cases (§8).

## 7. Not signed
- §7: N_HN for τ(o) ≠ o (docs/new/N5-NHN-box40.md, a separate packet per the Lead); the OPEN items; W-TIE and the block lemmas.
- Nothing here is a running-time bound for N5, a TARGET.md claim or a step-4 pass. G-N5-TIME stays OPEN.

## 8. Data (DATA, not proof)
Tools (docs/referee/scratch/, own code on rl_engine.py, `python3 -I`; logs docs/referee/scratch/rho_logs/):
- rho_probe.py runs every statement's check with its exact hypothesis (header lists them). It asserts one Odd vertex of out-degree > 1
  per game.
- rho_climb.py climbs with mutations from neb_climb.py. MODE tail: post-freeze with |U| ≥ 3 and P(θ)-changes there. MODE ffb:
  fallback-free HN runs longer than |U| − 2, with changes after s + |U| − 2.
### 8.1 Library and lane climbs
- (L) is the packet's 412-file list (lib37.txt existing files + box37/box38 instances): 253 games in 𝒞^1O, 159 skipped. 990 phases,
  106 with HN states. 0 failures (rho_logs/lib.log, lib2.log).
- My engine reproduces the packet's §8 counts exactly: Y-FORM 6,335 / 651, HAT-FREEZE (a) 1,127, (c) 38 at |U| = 2 in 29 post-freeze
  phases (22 with H1), BF-F 28,394 = 27,932 + 462, runs > 1 state 91, FREEZE-F (c) max 13, ρ_HN 87 with max 13.
- (C) is the six lane climb files experiments/new/box40/out/*.pg (sha1 2344518c…, cc459f93…, 77cc31b1…, 2a68bea3…, 25d15aac…, 98ba660a…;
  matching §8). 0 failures. 5 post-freeze phases at |U| = 3 with H1; HAT-FREEZE (c) 10 checks; RHO-TAIL 0 changes.
- RHO-N2 data (lib2.log): 30 phases with τ(o) = o and HN states, 17 in case A and 13 in case B. ¬H2 at every state of every
  τ(o) = o phase, and N_HN ≤ ⌊T_ph/2⌋ + 1 in all of them. 0 failures.
- Named: experiments/red/so/instances/beta2_n11.pg (L-RED, sha1 bdea2a23) and epsseg_cex_n48.pg: 0 failures.
### 8.2 My climbs (40 CPU-minutes each, 6 runs)
- MODE tail (rho_climb_out, logs climb_tail_{1,2,3}.log):
  - Seeds: experiments/new/box40/out/rhc_rhc_oneodd_c16_2_5.pg, rhc_pure_22_6.pg, rhc_rhc_block_bk20_3_4.pg.
  - 877,874 candidates, 685,042 qualifying: post-freeze phases at |U| = 3 (679,124 with an H1 state after g_1) and 13,933 at |U| = 2.
  - HAT-FREEZE (c): 1,164,482 checks at |U| = 3 against exact MoptÛ, and 3,736 at |U| = 2. Every qualifying candidate also got the full
    rho_probe check.
  - 0 failures.
  - RHO-TAIL: 0 P(θ)-changes after the freeze in every qualifying phase. The score (100 + 10·changes + |U|) never rose above 103:
    neither a change past the freeze nor |U| ≥ 4 past the freeze was reached.
- MODE ffb (logs climb_ffb_{4,5,6}.log):
  - Seeds: rhc_rhc_oneodd_c16_2_5.pg, experiments/red/so/instances/beta2_n11.pg, experiments/new/box40/out/nhc_fbrestart_cex_n12_11.pg.
  - 5,953,246 candidates, best score −1: no fallback-free HN run with |U| ≥ 3 longer than |U| − 3 transitions.
  - FREEZE-F (b) stays VACUOUS in my data as well.
- So the regimes the packet itself marks thin stay thin after about 4 CPU-hours: RHO-TAIL with a change past the freeze, |U| ≥ 4 past
  the freeze, and FREEZE-F (b) and the second term of (c). The lane's climbs plateau at the same place.
- RHO-N3 (data): what my data and the lane's do not reach is listed in the Verdicts' VACUOUS line. Those parts rest on their proofs,
  which I checked line by line.

## §C. Comparison with REFEREE-2: docs/referee-2/R2-N5-RHO.md at referee-2 269ae45a (sha1 89cd0a48…, the same on trunk 102f05a)
Written 2026-10-25T18:39Z by date -u, after the Lead's word of 18:15Z (Lead's stamp) that 269ae45a is final. I opened R2-N5-RHO only
after my report (59278313) was pushed. (Opus 5.5, D15).
- Verdicts: identical.
  - Both sign Y-FORM, HAT-FREEZE (a)-(c), RHO-TAIL, BF-F, FREEZE-F (a)-(c) and RHO-HN.
  - Both sign HN-POLY only through BRK-POLY′ (i′) and (ii)'s first inequality (θ_S form), the forms both referees sign in P-N5-PFZ-ext.
  - Neither signs §7-§8. No gap on either side.
- Joint gap map: EMPTY.

| item | REFEREE-2 | REFEREE | outcome |
| --- | --- | --- | --- |
| RHO-HN's run count | N-RHO-1: the proof gives (N_HN + \|U\| − 3)(…) + deg(o), sharper than stated | §6: "≤ (N_HN + \|U\| − 3)(\|U\| + deg(o) − 3) + deg(o), below the stated bound" | identical; wording note |
| o = c_θ with \|U\| ≥ 2 | — | RHO-N1 (wording): occurs in 89/990 library phases; covered vacuously; the text names only \|U\| = 1 | stands; R2's proofs (e.g. "\|U\| ≥ 2 under H1") are consistent with it |
| HN-POLY's τ(o) = o line, citing R39 (f) (c) | "For τ(o) = o they are polynomial via R39 (f) (c). ✓" | RHO-N2 (citation): R39 (f) is signed for τ(o) = o in case A only. The bound holds in case B too, because ¬H2 holds everywhere, so HN = H1, and R34 (e) applies (13 case-B phases in data) | REFEREE-2 MISSED the case restriction. The claim is unaffected. The lane should cite R34 (e) with HN = H1 (or P-N5-NHN §5 (b)'s argument) |
| post-freeze regime and FREEZE-F (b) | N-RHO-2: post-freeze only at \|U\| = 3 (133,889 phases), never \|U\| ≥ 4; FREEZE-F (b) 0 states; RHO-TAIL max 0 | §8: post-freeze at \|U\| ≤ 3 (679,124 climb phases at \|U\| = 3), never \|U\| ≥ 4; FREEZE-F (b) vacuous (5.95M ffb candidates, best run length \|U\| − 3); RHO-TAIL 0 changes | identical; both say: target for L-RED |
| mutation controls | hatall bites (701); frzb0 does not bite | none run | REFEREE-2's controls add to the evidence that the checks can fail |

- Data agree in kind. 0 failures on both sides. Both engines reach the same thin spots and none beyond them.
- No verdict of mine changes. (Opus 5.5, D15)
