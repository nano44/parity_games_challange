# P-N5-NEB fixes (box 38 packet): REFEREE NEB-R1, NEB-N1..N5, NEB-B1; REFEREE-2 N-NEB-1..3; §8 status (CONJECTURE BAND FALSE in three forms)
L-NEW successor 19 (Opus 5.5, D15/D18), session_011reTXakSJCcwLhC4i9ZpkB. Written 2026-10-25 16:52Z by date -u, at the Lead's request
(16:37Z, Lead's stamp). Repairs only. Frozen at its commit; any later item goes to a fixes2 file.
- Object: docs/new/P-N5-NEB-box38.md, sha1 ba15e51fb02471207b11ecd64e9687a23fe8a744, pinned trunk 314d220 (L-NEW successor 17). Unchanged.
- Reports (all on trunk f7b6e68):
  - REFEREE (succ. 9), docs/referee/R-N5-NEB.md at 40adbf1c, §C at 46a80300: RISE, HIGH-RISE, NO-ENTRY-A′, CASE-B-LEN′, LOW-RISE′, BRK,
    OUT-1 SIGNED, no gap; notes NEB-R1, NEB-N1..N5; record NEB-B1 (§8, not to sign).
  - REFEREE-2 (succ. 9), docs/referee-2/R2-N5-NEB.md at a4516df9, §C at a769ff54: all SIGN; notes N-NEB-1..3.
  - Both §Cs: identical verdicts, joint gap map EMPTY. REFEREE's §C accepts N-NEB-2, which it had missed. Union for this file:
    NEB-R1 = N-NEB-1, N-NEB-2, N-NEB-3 + NEB-N4, NEB-N1, NEB-N2, NEB-N3, NEB-N5, NEB-B1.
- No verdict or statement changes. No proof step changes, except the citations and the one added line in §1-§3 below.

## Map
| item | packet place | repair | kind |
| --- | --- | --- | --- |
| NEB-R1 = N-NEB-1 | §3 BASE (ii) of NO-ENTRY-A′; §4 CASE-B-LEN′ | cite FBL-N (i) (R21 (c)) + F1 (R17 (a)) for "no arena edge raises W at v at a", instead of Step (K) (R23 (a), "inside a phase") | citation; covers a phase-exiting fallback a → a+1 |
| NEB-N1 | §6 BRK proof, first line | "SPLIT (b): an S4a step does not evict" → "SPLIT (a)" | citation |
| NEB-N2 | §6 BRK proof, choice of t+1 | add: "a itself has no gate F → R̄ (FBL-N (iii) with (iii+), as in §3 BASE (i) and §5 INV_B(a) (i))", so §1's hypothesis holds on [a, t] | one missing line, no gap |
| NEB-N3 | §6 LR_S | "Values in C_θ belong to vertices z ∉ {o, c_θ}" → "low rises are at vertices z ∉ {o, c_θ}" | wording |
| N-NEB-2 | §5 LOW-RISE′ (b) | optional sharpening: (b) holds without (i) at t+1 | precision (optional) |
| N-NEB-3 + NEB-N4 | §0 dependency table and the "To sign" table header | stale statuses → RESULTS R38 (KEY, FB-INT) and RESULTS R39 (SPLIT, F-FLAT, EPOCH, NE-COUNT (c)) | status wording |
| NEB-N5 | §9 base totals | the printed totals are not those of the stated command; the stated command gives 75 / 9 / 4 / 20 / 8 | data note |
| NEB-B1 | §8 (not to sign), CONJECTURE BAND | FALSE in the rises form, in the gates form at a later state, and in the gates form at the base state | status (record) |

## 1. NEB-R1 = N-NEB-1: the Step (K) citation at the base
- REFEREE (NEB-R1, remark, no gap): the setting allows a phase-exiting fallback a → a+1 (then b = a), while (K) is stated "at an S4c
  fallback inside a phase". (K)'s proof uses only FBL-N (i) at a and does not look at a+1. Data: one such base occurs
  (experiments/red/n5inj/instances/frz24.pg, case A, c_w ≠ o; outside §3's class).
- REFEREE-2 (N-NEB-1, citation): "against Step (K)" in §3 BASE (ii) and §4; R23 (a) is stated "inside a phase" and a+1 may leave S.
  FBL-N (i) + F1 is what is used. (= OUT-R1 / N-OUT-2 on P-N5-OUT; docs/new/P-N5-OUT-fixes-box37.md §1 already forwards it to NEB.)
- Repair. In §3 BASE (ii) and in §4, read "against Step (K) (RESULTS R23 (a))" as:
  - at the Even fallback a → a+1 with τ unchanged, σ_a is a pointwise arena optimum in G_τ (FBL-N (i), RESULTS R21 (c));
  - the one-player optimum dominates every arena strategy pointwise (F1, RESULTS R17 (a));
  - so no single switch along an arena edge (v, z) raises W at v.
  - This uses only τ_{a+1} = τ_a, true at every Even fallback (SPEC S4c, FIX 3). It is Step (K)'s own proof. In every use inside the
    packet (§6: an eviction is a crossing, hence in-phase) a+1 ∈ S holds anyway.
- §0's sentence "The W-arguments use Step (K) (RESULTS R23 (a)), which rests on FBL-N (i) (R21 (c)) and F1 (R17 (a))" stays true; with
  this repair the packet cites the two premises directly.

## 2. NEB-N1, NEB-N2, NEB-N3: §6 (Theorem BRK) proof text
- NEB-N1 (citation). §6 proof, first line: "The eviction a → a+1 is a fallback (SPLIT (b): an S4a step does not evict)". The part used
  is SPLIT (a) (an S4a step from an HN state has R_k ⊆ R_{k+1}). Read "SPLIT (a)". (SPLIT (b) is "an Even fallback does not enter".)
- NEB-N2 (one missing line, no gap). §6 defines t+1 as "the first state after a with a gate F → R̄" and applies §1, whose hypothesis is
  "no state of [a, t] has a gate F → R̄", a itself included. Add after the definition of t+1:
  - "The state a has no gate F → R̄: FBL-N (iii) (RESULTS R21 (c)) under ¬H2 excludes gates F → R, and (iii+) (the target-o step, §0)
    excludes F → o (§0, l. 99); as in §3 BASE (i) and §5 INV_B(a) (i). So §1's hypothesis holds on [a, t]."
  - REFEREE's probe FBLN0: 0 failures at 117 HN Even-fallback states. REFEREE-2's report states the same line in its §6 ("since a has
    none").
- NEB-N3 (wording). §6, LR_S, second sub-bullet: "Values in C_θ belong to vertices z ∉ {o, c_θ}" is false as written (θ itself lies in
  C_θ). Read: "Low rises are at vertices z ∉ {o, c_θ} (z ≠ o by the definition of an R̄-rise; c_θ ∈ F), with lengths in [1, n − 1]."
  The count that follows ((n − 2)² transitions per θ-constant run) is unchanged.

## 3. N-NEB-2 (optional): LOW-RISE′ (b)
- REFEREE-2 (precision, optional): the proof of §5 (b) uses the value claim and (ii_B) at t, not (i) at t+1, so (b) holds even at the
  first failure of (i). BRK uses (b) only at states where (i) holds, so nothing depends on it.
- REFEREE's §C: missed it, ACCEPTED ("(b) needs only the value claim and (ii_B) at t, and the no-entry at t → t+1 uses (i) at t only").
- Repair (optional sharpening; no statement used elsewhere changes): §5 (b) may be read "for every t in the run up to and including the
  first state t+1 at which (i) fails".

## 4. N-NEB-3 + NEB-N4: stale statuses
- "To sign" table header: "uses P-N5-OUT (pinned 719ce66, in review)" → "uses RESULTS R39 (P-N5-OUT, LANDED 15:09Z; CHECKER C48)";
  "uses P-N5-SCOPE (signed, landing)" → "uses RESULTS R38 (P-N5-SCOPE, LANDED 14:16Z; CHECKER C47)".
- §0 dependency table:
  | row | old status | new status |
  | --- | --- | --- |
  | KEY | signed by both referees; landing (R36) | LANDED: RESULTS R38 (a) |
  | FB-INT | signed by both referees; landing (R36) | LANDED: RESULTS R38 (d) |
  | SPLIT | IN REVIEW (P-N5-OUT §1) | LANDED: RESULTS R39 (a) |
  | F-FLAT | IN REVIEW (P-N5-OUT §3) | LANDED: RESULTS R39 (c) |
  | EPOCH | IN REVIEW (P-N5-OUT §2) | LANDED: RESULTS R39 (b) (corrected form) |
  | NE-COUNT (c) | IN REVIEW | LANDED: RESULTS R39 (f) (c) |
- "landing (R36)" was wrong at the pin: RESULTS R36 is P-N5-P1, R37 is P-N5-RL, R38 is P-N5-SCOPE. P-N5-OUT's fixes file is
  docs/new/P-N5-OUT-fixes-box37.md (sha1 640a5db2…), on trunk.

## 5. NEB-N5: §9 base totals (data note)
- §9 prints, from data/inv2_all.txt, the bases by class 75 + 13 (case A, c_w = o; τ(o) = o / ≠ o), 34 (case B, τ(o) = o), 6 (case A,
  c_w ≠ o), 27 (case B, c_w ≠ o), with the "Reproduce" line `python3 experiments/new/box38/inv2.py $(cat experiments/new/box37/lib37.txt)
  experiments/new/box38/instances/*.pg`.
- REFEREE (own engine and the lane's inv2.py per file): that command gives 75 / 9 / 4 / 20 / 8 (A c_w = o τ(o) = o / A c_w = o τ(o) ≠ o /
  A c_w ≠ o / B τ(o) = o / B c_w ≠ o), plus 1 phase-exiting base (frz24) that inv2.py does not count.
- Lane re-run (L-NEW succ. 19, 16:51Z, this container, l-new 3e9fe5c2): the stated command gives exactly 75 / 9 / 4 / 20 / 8, with 0
  failures of every FAIL counter (NO-ENTRY violations outside the proved class: 9 / 10 / 1, as expected; none in the proved class).
- So data/inv2_all.txt came from an input set larger than its Reproduce line names. The most likely extra input is successor 17's box-38
  climb outputs (experiments/new/out/box38/, gitignored and lost with its container); this cannot be checked now. Repair: §9's totals
  read "75 / 9 / 4 / 20 / 8 on the stated command (lib37 + box-38 instances/*.pg)"; the larger totals of data/inv2_all.txt are from an
  unnamed input set and are withdrawn as evidence. Every statement's 0-failure record stands on the stated set and on both referees' sets.

## 6. NEB-B1: CONJECTURE BAND is FALSE (record for §8; not a signed item)
CONJECTURE BAND (§8): "after a c_w ≠ o fallback in case A, R → R̄ gates and R̄-rises have levels below rank(c_w)". FALSE in three forms.
- (1) Rises form (lane, successor 17, post-pin commit 1d934feb, 13:29Z; reproduced by REFEREE): experiments/new/box38/instances/
  tauw_A_cex_n24.pg (sha1 e29908d5…), canonical start. Base a = 4: case A, c_w(4) = 7 of rank 21, rank(o) 17. The θ-constant HN run is
  [4, 13]. S4a 12 → 13 raises Ξ(11) and Ξ(16) at level 23 > 21.
- (2) Gates form at a later state (REFEREE, new): same run, state 13 has R → R̄ gates 3 → 11 and 7 → 16 at level 23 > 21. The same two
  rises and gates repeat from base a = 10.
- (3) Gates form AT the base state (REFEREE, new): docs/referee/R-N5-NEB/band_base_cex.pg, sha1
  468edac825a19ef73823a684c288ee01abaad94b (re-measured here). n 24, 𝒞^1O, o = 19 (rank 17), τ(o) = 16; canonical start, 6 iterations,
  1 fallback; Oink 8fbf0a7 --zlk solves it and verify accepts (REFEREE; Lead re-run OK, 15:59Z). Base a = 2 is an in-phase Even fallback
  at an HN state, case A (rank c_θ 14 < 17), c_w(2) = 2 of rank 19; its R → R̄ gate 5 → 14 has level 19 = rank(c_w(2)) (the top
  difference is c_w itself). This breaks the strict "below rank(c_w)" at the boundary.
- A "≤ rank(c_w)" form AT THE BASE: no counterexample in REFEREE's 458,960-step search (DATA only). It fails after the base anyway: the
  later-state gates of (2) are strictly above rank(c_w).
- Obstruction (both): c_w(a) is read at the base, and W-improving R → R̄ gates are not bounded by c_w.
- §8 status lines therefore read: "CONJECTURE BAND: FALSE (rises form: tauw_A_cex_n24; gates form later: tauw_A_cex_n24 state 13; gates
  form at the base: band_base_cex.pg, level = rank(c_w))". The OPEN item RW_S (R̄-rises after c_w ≠ o evictions) is unchanged by
  this record. (Since the pin, P-N5-PFZ BRK-POLY bounds breaks per HN stretch for every c_w without BAND; P-N5-PFZ is in review.)
