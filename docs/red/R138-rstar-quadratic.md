# R138: R*_F is QUADRATIC in one W-run. R127's one-world mkr with late adopters (span/mkrw.py LATE=1) has R*_F = K·m on L-NEW's own counter (640 = 1.19n at n 538; 512 at n 482). But R*_F ≤ |F| always, so R*-POLY is EQUIVALENT to "|F| polynomial" (given FL): no reduction, and no kill
L-RED successor 33 (Opus 5.5; D1/D18). Lead 2026-10-30 13:06Z: "R138, an adversary against R*-POLY. In real N5 ... build a family with R*_F
super-linear in n inside ONE W-run. Targets in order: (1) R*_F ≥ c·n^{1+ε}, or quadratic; (2) failing that, FL_F growing unboundedly;
(3) failing both, the exact obstruction ... Start from gate_K64 (where does 64 come from ...)". Written 2026-10-30 from 13:08Z (date -u).
Labels: PROVED (lane) / DATA / READING. Not a TARGET.md claim. G-N5-TIME OPEN.
Definitions: R*_F and FL_F as in RESULTS R88 / R89, read on a W-run F as in l-new 893b9346 docs/new/N5-FREE-box85.md §0 and its
experiments/new/box85/xirise.py:
- R*_F: the transitions of F at which some Even y adopts an edge (y, z) that was BLOCKED at an earlier state q of F, i.e.
  W_q(z) ▷ W_q(σ_q y) and (y, z) ∉ Iσ_q.
- FL_F: the transitions with W unchanged.

## 1. Where gate_K64's 64 comes from
- gate_K64_n581 is L-RED successor 20's R84 instance (experiments/red/usplit/mkgate.py K LG, docs/red/R84-gate-reentry.md). K
  leapfrogging risers drive one Odd gate. Each rise ends in one first adoption of a blocked edge, so R*_F = K by design, with n = 9K + 5.
- It is linear: 64 at K 64, n 581 (box 85 §2: "all 64 are first adoptions of blocked edges").

## 2. Target (1) met: R*_F = K·m in one W-run (DATA)
- Family. R127's span/mkrw.py K m with LATE=1 (L-RED successor 31; R128 REP-LIN kill). It is mkr in one W-world. Each reactor J ≥ 2 gets a
  re-blockable late adopter v_J → {d_J, c_J}, c_J (Odd) → {r_J, yh_J (τ)}. n = 14K + 8m + 2.
- Counted with L-NEW's own xirise.py (l-new 893b9346, run unchanged from a worktree):

  | K | m | n | W-runs | |F| | R*_F | R*_F / n | FL_F | FREE-RED violations |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | 4 | 8 | 122 | 1 | 44 | 32 | 0.26 | 0 | 0 |
  | 4 | 16 | 186 | 1 | 76 | 64 | 0.34 | 0 | 0 |
  | 8 | 16 | 242 | 1 | 152 | 128 | 0.53 | 0 | 0 |
  | 12 | 24 | 362 | 1 | 324 | 288 | 0.80 | 0 | 0 |
  | 16 | 32 (pin rstar/latew_K16_m32) | 482 | 1 | 560 | 512 | 1.06 | 0 | 0 |
  | 20 | 32 (pin span/latew_K20_m32, R128) | 538 | 1 | 700 | 640 | 1.19 | 0 | 0 |

- R*_F = K·m exactly. With m = 2K that is 2K² ≈ n²/450: quadratic, super-linear from K ≥ 16.
- Second counter: L-RED's span/latec.py (R127, on n5b) prints the same R* (64 at K 4 m 16; 512 on the K 16 pin).
- Pins: xeng identical; Oink zlk OK with strategies verified (§5).
- Box 85's corpus maximum (64, gate_K64) did not include this family.

## 3. The obstruction behind every R*-amplification: R*_F ≤ |F| (PROVED, lane; immediate)
- R*_F counts transitions of F, so R*_F ≤ |F|.
- With FREE-RED (box 85, from landed R88 FW-R* and R89 GP*-RUN): R*_F ≤ |F| ≤ (n − 1)(R*_F + 1) + FL_F.
- So R*-POLY ∧ FL-POLY ⇔ |F| ≤ poly on every W-run: an EQUIVALENCE, not a reduction. The "hard residual" R*_F is the W-run length up to a
  factor n − 1 (plus FL).
- Hence a super-quadratic R*_F needs a super-quadratic W-run. That is the wall of the Successor 32 PARK: a third factor beyond clock ×
  chain, which R124 / R127 / R135-R137 have not produced.
- So target (1) is met at the quadratic level, and the step beyond quadratic is exactly G-N5-TIME on W-runs.

## 4. Target (2): FL_F (not attempted beyond a READING)
- FL = 0 on every W-run above. An FL transition needs a σ-change that leaves every W value unchanged: an offered edge that is W-tied with
  the current choice and taken by S4a's tie rule.
- A star X → {o_1, …, o_L} (all W-tied, Ξ increasing in index) would give L − 1 such transitions, which is linear. Its Odd escapes need
  stable W/Ξ gaps under τ̄, as R135 §1 requires. Not built.

## 5. Pins and checks
- rstar/instances/latew_K16_m32 (new; = span/mkrw.py LATE=1 16 32): latec R* 512; xeng identical; Oink zlk OK with strategies verified
  (sha1 in check.sh).
- span/instances/latew_K20_m32 (R128 pin, unchanged): xirise R*_F 640, |F| 700.

## DONE / FINDINGS / NEEDS
- DONE: this note; pin rstar/instances/latew_K16_m32; check.sh "R138" (regenerates the pin, latec R* = K·m at K 4 m 8).
- FINDINGS:
  1. DATA: R*_F = K·m in ONE W-run on mkrw LATE=1 (L-NEW's xirise.py; latec.py agrees). The maximum is 640 = 1.19n at n 538: quadratic,
     target (1). FL_F = 0.
  2. DATA: gate_K64's 64 is K (R84 mkgate, n = 9K + 5): linear by design.
  3. PROVED (lane, immediate) R*_F ≤ |F|: with FREE-RED, R*-POLY ∧ FL-POLY ⇔ polynomial W-runs. R*_F is not a smaller residual. A
     super-quadratic R*_F needs a super-quadratic W-run (the same wall). No kill.
- NEEDS: none from the owner. Lead: tell L-NEW 38 (box 86) that R*_F is already quadratic (mkrw LATE=1), and that R*-POLY is equivalent to
  W-run length, not easier.
