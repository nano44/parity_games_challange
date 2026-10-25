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
