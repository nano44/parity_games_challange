# R-N5-NHN: REFEREE report on packet P-N5-NHN (box 40: T0U, EV2-FB, SG-EV, T0-PIN, NHN-BOUND, H3-IN-HN, Corollary HN-POLY-ALL)
Referee: REFEREE (successor 10, session_01J4kmfDqtZdanh3RSCxChyD), Opus 5.5 (owner ruling D15, Lead reading L37).
- Routing: the Lead's message of 17:34Z (Lead's stamp): review it after RHO.
- Object: docs/new/P-N5-NHN-box40.md at trunk 0bb175d, sha1 da7d09ec6cb27ee8f7d94b857bc13fb2946aff1a (checked with
  `git show 0bb175d:docs/new/P-N5-NHN-box40.md | sha1sum`; identical on my tree), 166 lines. Author: L-NEW successor 19.
- Written 2026-10-25T17:55Z-18:34Z by date -u. Every verdict is labelled (Opus 5.5, D15).
- Independent of REFEREE-2: I did not read any docs/referee-2/R2-N5-NHN* file. D1: each statement treated as wrong until its proof was
  checked. Tools: my own N5 engine (scratch/rl_engine.py) and new probes; no lane code (nhn.py, nhnclimb.py, qsurvey.py not run).

## Verdicts
| § | statement | label | verdict (Opus 5.5, D15) |
| --- | --- | --- | --- |
| §1 | Lemma T0U (a), (b) | PROVED | SIGNED |
| §2 | Lemma EV2-FB | PROVED | SIGNED |
| §3 | Lemma SG-EV | PROVED | SIGNED |
| §4 | Lemma T0-PIN | PROVED (uses P-N5-RHO §2) | SIGNED, conditional on P-N5-RHO's HAT-FREEZE (signed by me in R-N5-RHO; REFEREE-2 pending) |
| §5 | Theorem NHN-BOUND (a), (b) | PROVED (uses P-N5-RHO §2 via §4) | SIGNED, same condition; note NHN-N1 |
| §6 | Remark H3-IN-HN, and its bookkeeping Consequence | PROVED | SIGNED; note NHN-N2 (wording) |
| §7 | Corollary HN-POLY-ALL | PROVED, CONDITIONAL on P-N5-PFZ, P-N5-PFZ-ext BRK-POLY′ (i′)/(ii), P-N5-RHO | SIGNED with exactly those conditions; note NHN-N1. Its "What this closes" line is a GAPS reading for the Lead, not signed |
| §8, §9 | OPEN items, data | not to sign | not signed |
- No (P). The conditional labels are exact.
  - §1-§3 and §6 use landed results only: (V1), R15 (a), (d), SPLIT (a) (R39 (a)), H2-STICK and H3-CONST (R33 (b), (a)), and (A), (M1′),
    (M2′), (INJ), (HP), (SP) (restated in P-N5-RHO §0, checked in R-N5-RHO §0).
  - §4 and §5 use HAT-FREEZE (a)-(c).
  - §7 adds RHO-HN, HN-POLY, BRK-POLY′ (i′), (ii), EPOCH and TOGGLE-COUNT.
- Conditions:
  - P-N5-PFZ: signed by both referees.
  - P-N5-PFZ-ext: (i′) and (ii) signed by both. REFEREE-2 signs (i′), not (i), so (i′) is the form to use. See my §C-ext in R-N5-PFZ.
  - P-N5-RHO: signed by me (R-N5-RHO), REFEREE-2 pending.
- No gaps. Notes NHN-N1 (citation), NHN-N2 (wording), NHN-N3 (data).
- VACUOUS OR THIN IN DATA (lesson N-ENT-2; file sets in §8): T0-PIN and NHN-BOUND (a)'s second branch (EV2 ends at g_j, j ≥ |U| − 1).
  EV2-FB and SG-EV are thin. DROPs that end an HN stretch: 0 in the library,
  35 in my climbs (so (b)'s DROP branch is now exercised).

## 1. T0U: checked
- (a): o's (σ, τ)-play is o · (t0's play). o lies on its W-cycle iff that play returns to o, i.e. iff t0 ∈ R̄; since t0 ≠ o, iff t0 ∈ R.
  Correct.
- (b):
  - At an HN state s, (HP)'s route form gives R_s ⊆ U, and c_θ ∈ F_s, so t0 ∈ U ∖ {c_θ}.
  - λ is a phase constant, so λ(t0) = c_θ at every state, and t0 ∈ U ∖ {o, c_θ} throughout. Hence |U| ≥ 3. Correct.

## 2. EV2-FB: checked
- T0U (a) at k and k + 1 gives t0 ∈ R_k ∖ R_{k+1}, so R_k ⊄ R_{k+1}.
- SPLIT (a) (HN at k, in-phase): a non-fallback has R_k ⊆ R_{k+1}. So k → k + 1 is an S4c fallback, and it is Even's because τ is a
  phase constant. Correct.
- H2-STICK (R33 (b)) is a valid second source.

## 3. SG-EV: checked
- κ:
  - (M1′) applies because all four valuations have cycle node c_θ.
  - (A) gives κ_t(z) = (wt(z), s_θ) + κ_t(next_t z) for z ∈ U ∖ {c_θ}: M by (A), and ℓ = 1 + ℓ(next), so s_θ·ℓ gains s_θ.
- The route π_{t0}^k lies in R_k ⊆ U ∖ {c_θ}. This uses H1 at k through (HP).
- For route vertices, next is the same for the honest play and the (σ, τ)-play. Odd vertices other than o are forced, and σ̄ = τ there.
  So if no route vertex changed next, the same path would lead t0 to o at k + 1. Hence there is a first changed vertex y. It is Even,
  and R15 (d) makes its new edge a gate.
- z = σ_{k+1}(y) ∈ U by (A) at k + 1 (λ(y) = c_θ ≠ y).
- κ_k(z) > κ_k(σ_k y) by the gate and (M1′). κ_{k+1}(z) ≥ κ_k(z) by (M2′) and the length part of R15 (a), via (M1′).
- The prefix before y is unchanged and avoids c_θ, so the difference at t0 equals the difference at y, which is > 0.
- Correct. The remark is right too: R19 (d)'s step (SG) assumed (h), and this proof uses only H1 at k and the phase.

## 4. T0-PIN: checked
- k = g_j with j ≥ |U| − 1, so both k and k + 1 are > g_{|U|−2}. Also |U| ≥ 3 (T0U (b)), so g_{|U|−2} is a real fallback.
- At k + 1: H2 gives t0 ∉ R_{k+1} (T0U (a)), so t0 ∈ F_{k+1} ∩ Û. HAT-FREEZE (b), (c) give "defined" and the equality.
- At k: HAT-FREEZE (a) with j′ = |U| − 2 covers all simple paths of G_Û. So M_k(t0) ≥ MoptÛ(t0).
- (M2′) closes the sandwich. Correct.

## 5. NHN-BOUND: checked
- (b):
  - A stretch that is not the last of its phase has a later HN state in the phase, so it ends at an in-phase transition with HN at k
    and ¬HN at k + 1. That transition is a DROP (¬H1 at k + 1) or an EV2 end (H1 ∧ H2 at k + 1).
  - The last stretch adds 1. Drops ≤ ⌈T/2⌉ (R34 (e), every phase). With |U| ≤ n: 1 + 2(|U| − 2) ≤ 2n − 3.
  - Correct.
- (a), early ends: the EV2 ends are distinct Even fallbacks g_j (EV2-FB), and at most |U| − 2 of them have j ≤ |U| − 2.
- (a), late ends:
  - By T0-PIN, M(t0) = m* at both ends of each late end. M(t0) is non-decreasing on the phase (M2′), so the states with M = m* form an
    interval I that contains both ends of each such end.
  - On I, P(Ξ t0) is constant ((INJ)), so ⊴ on Ξ_t(t0) is the order of s_θ·ℓ. Each late end is a strict rise (SG-EV) inside I.
  - ℓ ∈ [1, |U| − 1] ((SP), t0 ≠ c_θ), so at most |U| − 2 strict rises.
  - Correct.
- NHN-N1 (citation, no gap; same as RHO-N2 in R-N5-RHO):
  - For τ(o) = o, the remark in §5 and the first line of §7 cite R39 (f) (c), which is signed for τ(o) = o in case A only.
  - (b)'s own argument covers τ(o) = o in both cases. o's W-play is its loop, so ¬H2 holds at every state, there is no EV2 end, and
    N_HN ≤ 1 + #DROPs ≤ ⌈T/2⌉ + 1. (R34 (e) holds on every phase, and so does the per-phase form ⌊T_ph/2⌋ + 1.)
  - Suggested citation: "§5 (b)'s argument with no EV2 end (or R34 (e) with HN = H1)", in place of R39 (f) (c) alone.
  - Data: §8.

## 6. H3-IN-HN: checked
- H3-CONST (R33 (a)): at every H2 state c_w = λ(τ(o)) = λ(t0). T0U (b): λ(t0) = c_θ. So H3 holds at every H2 state. Correct.
- The Consequence is correct as bookkeeping. A phase with a Q state (H1 ∧ H2 ∧ ¬H3) has no HN state:
  - with τ(o) = o, there are no H2 states;
  - with τ(o) ≠ o and an HN state, there is no Q state, by the Remark.
- NHN-N2 (wording): in "(there H3 fails at every H2 state, and every ¬H2 state is ¬H1)", the word "there" must mean "in a phase that
  contains a Q state". H3-CONST makes H3 constant over the H2 states of a phase. A phase with no HN state may still have H3 at every H2
  state (then it has no Q state). Read as "in a phase containing a Q state", the sentence is right.

## 7. HN-POLY-ALL: checked
- The orders:
  - N_HN = O(n²);
  - ρ_HN ≤ (N_HN + n)(2n) + n = O(n³);
  - Σ θ_S ≤ ρ_HN + (ρ_HN + N_HN)·n = O(n⁴);
  - Σ B_S ≤ (ρ_HN + N_HN)(2n² − 1) = O(n⁵);
  - Σ X_S = O(n⁶);
  - fallbacks ≤ K(Σ X_S + N_HN) + Σ X_S + N_HN = O(n⁸), with K = O(n²).
  Correct.
- The proof is HN-POLY (signed by me in R-N5-RHO §6) with §5's bound. The conditions are named correctly. BRK-POLY′ is used in the weak
  form (i′), which both referees sign.
- "What this closes" is a reading of GAPS G-N5-TIME. That belongs to the Lead and is not signed. In substance:
  - the open list item "HN stretches for τ(o) ≠ o" is bounded, conditionally on PFZ (+ ext (i′), (ii)) and RHO;
  - §8's items stay OPEN, including Q-state fallbacks, f in SCOPE-COUNT, (h)-state fallbacks, quiet S4a steps and the number of phases.
- Nothing here is a running-time bound for N5, a TARGET.md claim or a step-4 pass. G-N5-TIME stays OPEN.

## 8. Data (DATA, not proof)
Tools (docs/referee/scratch/, own code on rl_engine.py, `python3 -I`; logs docs/referee/scratch/nhn_logs/):
- nhn_probe.py: T0U (a), (b), EV2-FB, SG-EV (at every in-phase H1 transition where t0 leaves R, not only at EV2 ends), T0-PIN against
  the exact MoptÛ(t0), NHN-BOUND (a), (b) and N_HN ≤ 1 + #DROPs + #EV2, τ(o) = o (no EV2 end, N_HN ≤ ⌈T/2⌉ + 1), H3-IN-HN, and "no Q
  state in an HN phase".
- nhn_climb.py: score pulls toward late EV2 ends (j ≥ |U| − 1, i.e. T0-PIN), then more EV2 ends.
### 8.1 Library and lane climbs
- (L) is P-N5-RHO's 412-file list: 253 𝒞^1O games, 990 phases, 0 failures (nhn_logs/lib.log).
  - 918 phases with t0 ≠ o, 76 of them with an HN state; 30 τ(o) = o phases with HN states (case A 17, case B 13; NHN-N1 data); 165
    phases with Q states, none of them an HN phase.
  - T0U (a): 6,414 states; T0U (b): 604. H3-IN-HN: 385 H2 states. EV2 ends: 3 (EV2-FB and SG-EV hold at each). N_HN 76 in total, max 1.
- (C) is experiments/new/box40/out/*.pg, 8 files, including nhc_tauw_B_cex_n24_23.pg (sha1 e7bae7dd…) and nhc_band_base_cex_24.pg
  (da60633b…). 28 phases, 8 with t0 ≠ o and HN, 0 failures (nhn_logs/climbC.log).
  - EV2 ends 5; N_HN 13 in total, max 4 with 3 EV2 ends (nhc_tauw_B_cex_n24_23); H3 10 checks; 4 phases with Q states.
- Together, my engine reproduces the packet's §9 totals exactly: 84 phases, 8 EV2 ends, 395 H3 checks, N_HN 89 with max 4, 165 Q
  phases, 0 DROPs ending a stretch. No T0-PIN case.
### 8.2 My climbs (40 min each; seeds from (C))
- Seeds: nhc_fbrestart_cex_n12_11.pg (rngseed 11), nhc_tauw_B_cex_n24_23.pg (12), nhc_band_base_cex_24.pg (13). Logs
  nhn_logs/climb_{11,12,13}.log.
- 1,882,532 candidates, of which 922,373 have an EV2 end. Each of those was fully checked with nhn_probe.run.
- Checks: 1,022,295 EV2 ends (EV2-FB and SG-EV), 1,200,988 H3 checks. 0 failures.
- New relative to the lane's data: 35 DROPs ending an HN stretch (31 from the tauw_B seed), so NHN-BOUND (b)'s DROP branch is
  exercised. Max N_HN 4; max EV2 ends per phase 3.
- T0-PIN NOT reached. Best score 22: 3 EV2 ends in a phase, the latest at g_j with j = |U| − 9. No EV2 end at a fallback g_j with
  j ≥ |U| − 1 was found, so T0-PIN and NHN-BOUND (a)'s second branch stay VACUOUS in my data as well.
- NHN-N3 (data): T0-PIN and (a)'s late branch rest on their proofs. I checked those line by line (§4, §5). The bound of §5 is far from
  approached (max N_HN 4 against ⌈T/2⌉ + 2|U| − 3 in the hundreds).
