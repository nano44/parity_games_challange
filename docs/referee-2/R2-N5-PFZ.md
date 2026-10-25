# R2-N5-PFZ: second-referee check of packet P-N5-PFZ (L-NEW box 39: FB-ROUND, P-FREEZE, LEN-TAIL, NO-CROSS-A, RISE′, BRK-POLY). REFEREE-2 (successor 9), written 2026-10-25 15:4xZ-16:03Z (date -u)
Signature: (Opus 5.5, D15). Packet P-N5-PFZ (Lead queue 15:34Z by the Lead's stamp). Object docs/new/P-N5-PFZ-box39.md, sha1
3c617e06f7b9c67d5d9cd865acd134f3a8aed071. I checked the sha1 three ways: `git show 283bcb6:<file> | sha1sum`,
`git show origin/claude/l-new:<file> | sha1sum`, and on my tree. All three agree. The pin is trunk 283bcb6. The file has one commit,
c9f9caa1.
Background read: SPEC S1-S5; RESULTS R15 (a), (d), R17 (a) (V1), R21 (c), R23 (b), R38 (a), R39 (a), (c) (SPLIT, F-FLAT, which I
signed as P-N5-OUT); my R2-N5-NEB §2 (RISE, of which RISE′ is a re-proof).
Independence: nothing in docs/referee/ read for this packet (`ls docs/referee | grep -i pfz` is empty). No lane script (pfreeze.py,
pfzdata.py, pfzclimb.py) was run or imported.
Tools: docs/referee-2/R2-N5-PFZ/ (own code on R2-N5-OUT/out_check.py):
- pfz_check.py, pfz_climb.py;
- files.lst, run_all.sh, run_climbs.sh, totals.py, logs/, climb/, totals_logs.txt, totals_climb.txt.
Traces own / rand / spec. One Odd vertex with out-degree > 1 is asserted on every game.
Labels: PROVED (L-NEW succ. 18); no (P). Not a running-time bound, a TARGET.md claim or a step-4 pass. G-N5-TIME stays OPEN, and θ_S is a
parameter.

## Verdicts (Opus 5.5, D15)
| statement | verdict | gaps / notes |
| --- | --- | --- |
| §1 facts (A), (M1′), (M2′) | correct | N-PFZ-1 (wording): (A)'s "(filled in)" case "z ∈ P(Ξ next z)" cannot occur. z then lies on its own cycle after c_θ, while next(z)'s pre-c path ends at c_θ. The filled-in conclusion (wt(z) = 0, z in neither P) is still correct |
| §1 Lemma FB-ROUND | SIGN | — |
| §2 Theorem P-FREEZE (a)-(c) | SIGN | — |
| §3 Corollary LEN-TAIL | SIGN | — |
| §4 Corollary NO-CROSS-A | SIGN | — |
| P-N5-PFZ-ext (companion file) | see §X: P-FREEZE′, θ-LEN SIGN; BRK-POLY′ (i) NOT SIGNED as stated, (i′) SIGN | G-PFX-1 (successor 10) |
| §5 Lemma RISE′ | SIGN | It agrees with P-N5-NEB's RISE (R2-N5-NEB §2), stated with the break window and with "θ-change or rise" in one statement |
| §6 Theorem BRK-POLY (i), (ii) | SIGN | N-PFZ-2 (precision): the window here is [last eviction before the entry, entry], whereas P-N5-NEB uses the first eviction after the previous entry. Both give disjoint windows. The packet's choice is what makes RISE′'s "no entry in [a, k)" hold, and I checked that it does |
| §6 Consequences | correct as a READING with R39 (b) EPOCH | — |
| §7 | not signed (as briefed) | — |
Reachability (lesson N-ENT-2).
- FB-ROUND, the facts and P-FREEZE (a), (b) are exercised heavily: library 174,030 / 145,123 / 177,971 FB-ROUND checks, and 6,767,387 in
  the climbs.
- The post-freeze hypothesis "t > f_{|U|−1}" is reached only with |U| ≤ 2. That is 107 / 104 / 107 library θ-runs with |U| = 1, and
  955,321 climb θ-runs with |U| = 2. It is NEVER reached with |U| ≥ 3, not even by climbs aimed at it (max over θ-runs of
  #fallbacks − (|U| − 1) with |U| ≥ 3: 0 in batch and climbs).
- So P-FREEZE (c), LEN-TAIL, NO-CROSS-A and BRK-POLY's late kind-2 branch rest on their proofs. The packet's §8 says the same for the
  library.
No statement is NOT SIGNED, and no gap is open. No counterexample turned up in 66,655 batch runs or in 4,653,840 climb runs (4 climbs).

## 1. FB-ROUND: SIGN
- (A): for z ∈ U ∖ {c_θ}, λ(z) = c_θ ≠ z. (V1) gives Ξ(z) = z ⊕ Ξ(next z) with the same cycle node, so next z ∈ U. ⊕ adds z iff
  rank z > rank c_θ.
  - z is never already in P(Ξ next z): z's successor is next(z), so on a cycle through z the vertex c_θ comes before z (N-PFZ-1). ✓
- (M1′): on U the cycle node is c_θ for every value, so ⊴ compares the signed weights first. ✓
- (M2′): R15 (a), with λ constant in the phase. ✓
- Case 1 (Ξ_k x ⊴ Ξ_k σ_k v): (M1′) on x, σ_k v ∈ U, then (A), then (M2′). ✓
- Case 2: (v, x) is a gate. S4c's choice x* has Ξ_k(x*) ⊵ Ξ_k(x). In-phase gives λ_{k+1}(v) = c_θ ≠ v, and (A) at k+1 puts x* ∈ U. Then
  (M2′) and (M1′). ✓
- The Remark is right: the proof is "switch-all-to-best" plus monotonicity. It uses neither θ, nor H1, nor H2.

## 2. P-FREEZE: SIGN
- (b):
  - z's honest play reaches c_θ, which lies on its cycle, before any repetition. So the part up to the first terminal is a simple path.
  - Its edges are G_U edges. Even vertices follow σ into U by (A). Odd vertices other than o are forced.
  - (A) along it, with M_t(o) = wt(P(θ)) = M_Θ(o) and M_t(c_θ) = 0, gives M_t(z) = wt(p ∖ end) + M_Θ(end) ≤ Mopt_Θ(z). ✓
- (a): induction on j.
  - Odd z: (A) at t, and the hypothesis at t > f_j > f_{j−1}.
  - Even z: the hypothesis at k = f_j (k > f_{j−1}, or k ≥ a when j = 1), FB-ROUND at k (x ∈ U is a successor of z in G_U), then
    (M2′) from k+1 ≤ t.
  - p simple means z ∉ p′, so wt(z) is added once.
  - A θ-run with fewer than j fallbacks makes the claim vacuous. ✓
- (c): simple paths in G_U have ≤ |U| − 1 edges, so (a) at j = |U| − 1 gives ≥ Mopt and (b) gives ≤. The weight is injective on subsets
  of V_{>c_θ}. ✓
- The "no positive-cycle issue" remark is right. Mopt is a maximum over simple paths; (a) only quantifies over them, and (b) bounds
  above by an actual simple path.

## 3. LEN-TAIL and NO-CROSS-A: SIGN
- LEN-TAIL.
  - After f_{|U|−1}, P is frozen on U and the cycle node is fixed, so a U-rise is a length rise.
  - s_θ·ℓ is non-decreasing in each coordinate (R15 (a)), and strictly increasing at each rise.
  - ℓ ∈ [0, |U| − 1]: the path to c_θ lies in U and is simple.
  - So Ψ takes ≤ |U|(|U| − 1) + 1 values. ✓
- NO-CROSS-A.
  - At an H1 state, R̄ = {z ∈ U : o ∈ P(Ξ z)}: route form and SEP-o (re-proved in the packet, correctly) on R̄; F-plays avoid o.
  - o itself is in R̄ ∩ U with o ∈ P(θ) (case A).
  - P frozen on U gives R̄_{t+1} = R̄_t. ✓

## 4. RISE′ and BRK-POLY: SIGN
- RISE′: Step 0 (FBL-N (iii) plus the target-o step), Step 1 (ACT (i) and R15 (d)) and Steps 2-3 are R2-N5-NEB §2's argument.
  - The θ-change alternative is placed at t ∈ [a+1, k] by F-FLAT at a. ✓
  - The case split y ∈ F_t ∪ R_t uses SPLIT (a) at t ∈ S, which holds since t + 1 ≤ k and S is a run. ✓
- BRK-POLY.
  - Windows. a := the last eviction before the entry. Then no transition of [a, k) is an entry, so RISE′ applies.
  - Disjointness: break 2's last eviction lies after break 1's entry. ✓
  - Kind 1: a θ-change inside the window, so distinct windows give distinct changes. ✓
  - Kind 2, early (j ≤ |U| − 1): distinct breaks have distinct evictions, which are fallbacks of the same θ-run Θ. ✓
  - Kind 2, late (j ≥ |U|): the rise is a U-rise (R̄ ⊆ U under H1), after f_{|U|−1}, inside Θ; LEN-TAIL bounds these transitions. ✓
  - In case A, a late kind 2 is impossible: its eviction a → a+1 is a crossing between H1 states inside Θ after f_{|U|−1}, against
    NO-CROSS-A. ✓
  - ≤ θ_S + 1 θ-runs meet S, and |U|² − 1 ≤ n² − 1. ✓

## 5. Data (DATA, not proof)
- Batch (run_all.sh, logs/, totals_logs.txt): 295 𝒞^1O library files × 3 traces × 3 starts = 2,655 runs, 50,667 states; random 𝒞^1O
  64,000 runs. 893 / 893 logs end "RESULT OK violations=0".
- Library (own / rand / spec):
  - (A): every state of every phase (16,977 / 16,452 / 17,238), plus (M2′) at every in-phase transition.
  - FB-ROUND: 1,492 / 1,275 / 1,559 in-phase Even fallbacks, 174,030 / 145,123 / 177,971 (v, x) checks.
  - θ-runs: 7,821 / 7,506 / 7,859. P-FREEZE (b) (exact simple-path maximum by DFS) checked on the 1,525 / 1,518 / 1,524 runs with
    |U| ≤ 12; 6,296 / 5,988 / 6,335 runs with |U| > 12 were skipped, and that count is reported, not hidden.
  - P-FREEZE (a): 1,541 / 1,146 / 1,655 (j, t, z) checks.
  - NO-CROSS-A's identity R̄ = {z ∈ U : o ∈ P}: 7,611 / 7,502 / 7,699 case-A H1 states.
  - Breaks 22 / 20 / 22: kind 1 15 / 15 / 15, early kind 2 7 / 5 / 7, late kind 2 0. Every break was charged, and BRK-POLY (i), (ii)
    held.
  - Max fallbacks in one θ-run: 37.
- Climbs (run_climbs.sh, climb/, totals_climb.txt), four 1200 s climbs with FIT pfz:
  - seeds: random n 6-10 and 6-9, wd16_s2, b5_os_n16; own and rand traces;
  - totals: 1,163,460 evaluations, 4,653,840 runs, 11,155,049 states, 0 violations;
  - FB-ROUND 6,767,387 checks, P-FREEZE (a) 2,318,732, (b) 8,253,626 θ-runs (385,087 skipped, |U| > 12);
  - post-freeze θ-runs 419,630 (|U| = 1) and 955,321 (|U| = 2), with 102,305 post-freeze transitions and 0 U-rises after a freeze;
  - 5,254 breaks, all kind 1;
  - every climb plateaued at |U| = 2 freezes.

## 6. Notes for the lane (none blocks a signature)
- N-PFZ-1: §1 (A)'s filled-in case cannot occur (see §1); keep the conclusion, drop or reword the case.
- N-PFZ-2: §6's window convention (last eviction) differs from P-N5-NEB's (first eviction after the previous entry). Both are correct for
  their proofs. Say so if the RESULTS entries are merged.
- N-PFZ-3 (DATA): "t > f_{|U|−1}" with |U| ≥ 3 is not reached by the library or by my targeted climbs. θ-runs with large U end after far
  fewer than |U| − 1 fallbacks (max 37 at large |U|). This is what makes P-FREEZE a bound rather than a description of runs: it is worth
  stating that the freeze point is an upper bound that data never approaches.

## X. Companion packet P-N5-PFZ-ext (REFEREE-2 successor 10, written 2026-10-25 16:5xZ-17:2xZ by date -u; Lead GO 16:32Z, Lead's stamp)
Signature: (Opus 5.5, D15). Object: docs/new/P-N5-PFZ-ext-box39.md, sha1 b3702b1ba1849c6aa19cebd2c8fa57e02a318d2a. The same at the pin
c61ecc4 and on my tree (trunk 7d505e6). It is reviewed with P-N5-PFZ (§1-§6 above, successor 9's, all SIGN), as the Lead asked: one
report for both files.
Independence: nothing in docs/referee/ read for either file. REFEREE's R-N5-PFZ (referee 8595343, per the Lead) is not opened. No lane
script (pfreeze.py, pfzdata.py with PFZ_KEY=P) run or imported.
Tools (own code, in R2-N5-PFZ/):
- pfzx_check.py: successor 9's pfz_check.py with the θ-run replaced by the P-epoch, plus θ-LEN and BRK-POLY′ per HN stretch;
- pfzx_climb.py; filesx.lst (files.lst ∪ ../R2-N5-LV2/files_new.lst, 453 files), run_allx.sh, run_climbsx.sh, totalsx.py, logs_x/,
  climb/brki_*, totals_x.txt, totals_climbx.txt.

### X.1 Verdicts (Opus 5.5, D15)
| statement | verdict | gaps / notes |
| --- | --- | --- |
| §1 Theorem P-FREEZE′ (with LEN-TAIL′, NO-CROSS-A′) | SIGN | — |
| §2 Lemma θ-LEN | SIGN | — |
| §3 Theorem BRK-POLY′ (i) | NOT SIGNED as stated; SIGN corrected (i′) θ_S ≤ ρ_S + (ρ_S + 1)·max(\|U\| − 2, 0) | G-PFX-1 (proof gap, data below) |
| §3 Theorem BRK-POLY′ (ii) | SIGN its first inequality B_S ≤ θ_S + (ρ_S + 1)(\|U\| − 1 + \|U\|(\|U\| − 1)), and the end bound (ρ_S + 1)(2n² − 1); the middle bound needs + ρ_S | G-PFX-1 |
| §3 Theorem BRK-POLY′ (iii) | SIGN B_S ≤ θ_S + (ρ_S + 1)(\|U\| − 1); the end bound becomes (ρ_S + 1)(2n − 2) | G-PFX-1 |
| §3 Consequence O(n³·K·(ρ_S + 1)) | SIGN (unchanged by G-PFX-1) | — |
| §4, §5 | not signed (as briefed) | — |

### X.2 P-FREEZE′: SIGN
I re-read every use of "θ constant" in P-N5-PFZ §1-§4 (successor 9 signed those proofs).
- FB-ROUND: no θ.
- §2 (b): the terminal value M_t(o) = Σ_{u ∈ P(θ_t)} sgn(u)2^rank(u) = wt(P(θ_t)), since P(θ) ⊆ V_{>c_θ}. It depends on P(θ_t) only, so it is
  constant on a P-epoch. (V1) along the honest play and the G_U path are unchanged. ✓
- §2 (a): the base uses the terminal values. The induction uses FB-ROUND at f_j and (M2′) from f_j + 1 to t, all inside Π. ✓ (c): ✓
- LEN-TAIL′: after f_{|U|−1}, P is constant on all of U, o included. Each U-rise is then a length rise. Ψ is non-decreasing (R15 (a), same
  cycle node and same P), and ℓ ∈ [0, |U| − 1]. A length rise of θ itself is a U-rise at o, as the packet says. ✓
- NO-CROSS-A′: the route form and SEP-o are per state, with θ_s at s. Then R̄_s = {z ∈ U : o ∈ P(Ξ_s z)}, frozen by (c). ✓

### X.3 θ-LEN: SIGN
- If o ≠ c_θ: in Π the cycle node c_θ (phase) and P are fixed. So R15 (a) makes ℓ(θ) strictly monotone at each θ-change inside Π.
- ℓ(θ) is the number of edges of o's honest play to its first visit of c_θ. That is a simple path in U (λ = c_θ along it), with ≥ 1 edge
  since o ≠ c_θ, so ℓ ∈ [1, |U| − 1]. This holds with H1 or without it.
- So at most |U| − 2 changes. The bound counts θ-changes with both ends in Π. ✓

### X.4 BRK-POLY′: G-PFX-1
- (i) as written: θ_S ≤ (ρ_S + 1)·max(|U| − 2, 0). The proof is "S meets at most ρ_S + 1 P-epochs; apply θ-LEN to each".
- The gap: θ-LEN counts the θ-changes INSIDE a P-epoch, i.e. transitions with both ends in Π. The ρ_S transitions at which P(θ) changes
  join two P-epochs. They are θ-changes of S (θ_S counts every transition with θ_{k+1} ≠ θ_k), and no epoch counts them.
- So the proof gives (i′) θ_S ≤ ρ_S + (ρ_S + 1)·max(|U| − 2, 0). Nothing in the packet bounds the ρ_S extra changes by the epochs'
  slack. (i) as written fails exactly when every P-epoch of S nearly saturates its |U| − 2 length moves.
- Data: (i) as written held on every HN stretch I ran, batch and climbs; in 8,415 batch stretches and 269,211 climb stretches, including 50,167 with ρ_S ≥ 1 and up to ρ_S = 16, θ_S − (ρ_S + 1)·max(|U| − 2, 0) was never positive (max 0 in the climbs that pushed toward it, FIT brki). So G-PFX-1 is a gap in the proof, not a
  refutation. I sign (i′).
- Consequences of G-PFX-1:
  - (ii): the kind-1 / kind-2 charging is right. Kind 2 lies inside one θ-run and so inside one P-epoch Π. Its eviction is a fallback f_j
    of Π; early breaks are ≤ |U| − 1 per epoch; late ones fall under LEN-TAIL′. So B_S ≤ θ_S + (ρ_S + 1)(|U| − 1 + |U|(|U| − 1)) is
    signed.
  - With (i′), the middle bound becomes ρ_S + (ρ_S + 1)(|U|² + |U| − 3) ≤ (ρ_S + 1)(|U|² + |U| − 2). That is still ≤ (ρ_S + 1)(2n² − 1),
    since n² + n − 2 ≤ 2n² − 1. So the end bound stands.
  - (iii) case A: B_S ≤ θ_S + (ρ_S + 1)(|U| − 1) is signed (NO-CROSS-A′ removes the late kind-2 breaks). With (i′) the end bound is
    ρ_S + (ρ_S + 1)(2|U| − 3) ≤ (ρ_S + 1)(2n − 2), not (2n − 3).
  - The Consequence O(n³·K·(ρ_S + 1)) is unchanged.
- Fix for the lane: state (i) as (i′), and the end bound of (iii) as (ρ_S + 1)(2n − 2). Or prove that the P-change transitions are paid
  by the epochs' slack. I see no such argument.

### X.5 Data (DATA, not proof)
- Batch (run_allx.sh, logs_x/, totals_x.txt): 453 𝒞^1O files × 3 traces × 3 starts = 4,077 runs; random 𝒞^1O 64,000 runs. 1,367 /
  1,367 logs end "RESULT OK violations=0".
  - P-epochs (library, all traces): 27,786. θ-LEN: 3,564 θ-changes in 2,097 epochs, all length-only and within max(|U| − 2, 0); at most
    11 in one epoch. Random: 1,488 θ-changes, at most 2 per epoch.
  - P-FREEZE′: (a) 7,677 DFS checks (|U| ≤ 12; larger |U| skipped and counted), (b) on 6,947 library epochs; FB-ROUND at 7,256 fallbacks
    (library) + 876 (random).
  - Post-freeze regime: P-epochs that pass f_{|U|−1} have |U| = 1 (486 library, 15,805 random) or |U| = 2 (5 library, 51 random), none
    with |U| ≥ 3. So LEN-TAIL′ and NO-CROSS-A′ are exercised only trivially, as the packet's §5 says.
  - HN stretches: 1,791 (library; 222 with ρ_S ≥ 1, max ρ_S 16) and 6,624 (random; 11 with ρ_S ≥ 1).
  - Breaks: library 85: 57 kind 1, 28 kind 2 early, 0 kind 2 late. BRK-POLY′ (ii) / (iii) first inequalities and (i′): 0 failures.
    The records for (i) as written and for the middle / end bounds: 0.
- Climbs (run_climbsx.sh, climb/brki_*, totals_climbx.txt), FIT brki toward θ_S > (ρ_S + 1)·max(|U| − 2, 0):
  - 9601 (n 6-10 random) and 9602 (seeded with my lane's R2-N5-SN/climb/stick_a_best.pg, n 48), 1,200 s each;
  - 101,961 evaluations, 407,844 runs, 0 violations;
  - 269,211 HN stretches, 49,934 with ρ_S ≥ 1 (max ρ_S 5 and 13); 7,480 breaks, all kind 1;
  - the excess θ_S − (ρ_S + 1)·max(|U| − 2, 0) never exceeded 0, so no counterexample to (i) as written was found.
- Thin spots:
  - G-PFX-1 is a proof gap. The data neither refute (i) nor come close in a non-trivial way.
  - The post-freeze parts (LEN-TAIL′, NO-CROSS-A′, late kind-2 breaks) are vacuous beyond |U| ≤ 2, as for P-N5-PFZ (N-PFZ-3).
