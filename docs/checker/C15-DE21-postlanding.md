# C15: post-landing text check of RESULTS DE21, the R12/R13 gap-line pointers and the GAPS GAP-A row, trunk 19a892c — CHECKER, 2026-10-18

Diff: 89ea054 → 19a892c (89ea054 is an ancestor). Only docs/RESULTS.md (DE21, G-R12-5, G-R13-4) and docs/GAPS.md (GAP-A row)
are in scope. l-red 9cd2702 (R39) is an ancestor of 19a892c, and docs/red/R39-relay-depth.md is on trunk.

## Verdict: FAIL on one phrase of DE21's "Consequence" (E-1); the numbers PASS (reproduced exactly in both orders); the pointers PASS

## E-1 (required): "the R12 (c) route (constant depth) ... [is] dead on data"
- DE21's opening says, correctly, that what is FALSE is (STEAL-DEPTH_D) "for D ≤ 3", and that it is "NOT yet a refutation of
  (STEAL-DEPTH_D) or (EXIT_c) for every constant (that needs a uniform family; the control wiring is hill-climbed per D)".
- The closing "Consequence: the R12 (c) route (constant depth) and the R13 (c) route with c = 2 are dead on data" then says
  more than that. R12 (c)'s route needs SOME constant D, and the data refute only D ≤ 3. Depth growing 2/3/4 along a
  sequence whose wiring is hill-climbed per D is evidence, not a refutation for every D.
- The R13 half, "(EXIT_2) dead", is accurate.
- Fix (one phrase): "the R12 (c) route with D ≤ 3 and the R13 (c) route with c = 2 are dead on data; depth grows along the
  R39 sequence (no uniform family yet)".
- Nothing else in DE21 overclaims:
  - "(STEAL-DEPTH_D) for D ≤ 3" is backed by the depth-4 instance.
  - "(EXIT_2)" is backed by 3 exits on depth4_n53.
  - It does not claim "for every c".
  - "NOT a dead end for DTL itself (iterations stay linear)": Oink takes 10/11/12 iterations at n = 39/46/53.
  - "R12 (a), R13 (b) and R14 are untouched (k ≤ 3, totals small)": max k = 3, and totals/|R| ≤ 1.79.
- The GAPS row says "depth GROWS 2/3/4 at n = 39/46/53 ... and (EXIT_2) is false (3 exits), both orders, RESULTS DE21; a
  uniform family is pending". No overclaim.

## Numbers (CHECKER re-run)
- Instances: experiments/red/lag/instances/depth2_n39.pg, depth3_n46.pg, depth4_n53.pg.
  - sha1 prefixes 6200e586 / 54cc8526 / 40dacf0e, as in DE21.
  - n = 39 / 46 / 53 = 7D + 25 for D = 2, 3, 4.
- Tools:
  - experiments/alg/dtl_stealdepth.py at HEAD is identical to l-alg e0fc1bb (DE21: "unchanged since l-alg e0fc1bb"); last
    change 931fc22.
  - dtl_prefexits.py: last change 3248d1f.
  - Both run unmodified, with RM_EXCL=1 RM_PREF=1 RM_LIGHT=1 RM_DV=0.
| instance | pinned Oink | stealdepth stable / Oink: max k; max depth | prefexits stable / Oink: max exits per (context, step, vertex); max total/\|R\| (\|R\|, visits) | DE21 |
| --- | --- | --- | --- | --- |
| depth2_n39 | 10 iterations, verified (28) | 2; 2 / 2; 2 | 2; 0.64 (39, 9) / same | 10, 28; depth 2, k 2; exits 2; 0.64 |
| depth3_n46 | 11 iterations, verified (33) | 2; 3 / 2; 3 | 2; 1.13 (46, 10) / same | 11, 33; depth 3, k 2; exits 2; 1.13 |
| depth4_n53 | 12 iterations, verified (38) | 3; 4 / 3; 4 | 3; 1.79 (53, 11) / same | 12, 38; depth 4, k 3; exits 3 ("\|R\| 53, 11 visits"); 1.79 |
All values are identical in both orders, as stated. Exit codes are 0.

## Pointers inside landed R12 / R13
- G-R12-5 gains "see RESULTS DE21 (depth 2/3/4 on a growing sequence). Before that: ...". G-R13-4 gains "see RESULTS DE21
  ((EXIT_2) FALSE: 3 exits on depth4_n53). Before that: ...".
- Both are OPEN gap lines that record DATA status, not signed claims. The old data text is kept after "Before that:", so the
  landed record is preserved and no signed text moves.
- I accept pointer additions in OPEN data gap lines as they stand. No POST-LANDING NOTE is needed here.
- Preference, for the record: use a POST-LANDING NOTE (as for R9 and R11) whenever new data makes a SIGNED claim's
  hypothesis false or changes a signed constant. In R12/R13 the signed claims are conditionals whose hypotheses (STEAL-DEPTH_D
  for constant D; EXIT_c) remain open, so pointers suffice.
- One exception to watch: if a later instance refutes (STEAL-DEPTH_D) for EVERY constant D, R12 (c) gives no reduction as
  stated (as R11 (d) after DE20). That case would warrant a NOTE like R11's.

## Fix list
Required:
- E-1: DE21 "Consequence": "the R12 (c) route with D ≤ 3 ... are dead on data; depth grows along the R39 sequence (no
  uniform family yet)".

## Addendum: re-diff 19a892c → a747106 (Lead 03:21Z), text only: PASS
- History: 19a892c is an ancestor of a747106. docs/RESULTS.md: 2 insertions, 1 deletion; GAPS is unchanged.
- DE21's Consequence now reads "the R12 (c) route with D ≤ 3 and the R13 (c) route with c = 2 are dead on data; depth grows
  along the R39 sequence (no uniform family yet);". This is my suggested wording, and E-1 is fixed.
- Nothing else moved. DE21 PASSES as at a747106.
- Recorded: the Lead adopts the rule "a POST-LANDING NOTE on R12 (c) only if a uniform family refutes every constant D".

## Addendum 2: one-pass check 19a892c → 5c452e3 (Lead 03:32Z; supersedes Addendum 1's scope), text plus numbers
History: 19a892c and a747106 are ancestors of 5c452e3, and l-red a0eb07a (R39 §5) is an ancestor. In scope are four changes:
the DE21 E-1 fix (Addendum 1, PASS), the DE21 ADDENDUM, the R12 POST-LANDING NOTE, and the GAPS GAP-A row.

### Verdict: numbers PASS (reproduced exactly); FAIL on one clause of the DE21 ADDENDUM and the GAPS row (E-2, new CHECKER data); notes N-1, N-2

### Numbers (CHECKER re-run, tools unmodified, RM_EXCL=1 RM_PREF=1 RM_LIGHT=1 RM_DV=0)
- I regenerated with `python3 -I experiments/red/lag/lagfam.py D out.pg`. D = 4, 8, 12 are byte-identical to the pinned
  fam_D4_n50 (c8fd8616), fam_D8_n78 (46ad828c) and fam_D12_n106 (0dd2899e).
| D | n | pinned Oink | dtl_stealdepth stable / Oink: max k; max depth | ADDENDUM |
| --- | --- | --- | --- | --- |
| 4 | 50 | 12 iterations, verified (37) | 3; 4 / 3; 4 | D + 8 = 12; k = ⌊5/2⌋ + 1 = 3; depth 4 |
| 12 | 106 | 20 iterations, verified (77) | 7; 12 / 7; 12 | D + 8 = 20; k = ⌊13/2⌋ + 1 = 7; depth 12 |
- Identical in both orders, as stated. "(STEAL-DEPTH_D) is FALSE for EVERY constant D (on this family, at D > the constant)"
  is supported: depth = D, uniform rule, both orders.
- The R12 POST-LANDING NOTE is accurate.
  - "(a), (b) and (c) as a conditional are unaffected, but (c) gives no reduction of GAP-A": correct.
  - "no constant-k form holds": k = ⌊(D+1)/2⌋ + 1 grows.
  - "(STEAL-POLY_k) is not refuted (k ≤ n)": k ≈ n/14, which is polynomial.
  - It is a NOTE, as the rule requires.

### E-2 (required; new CHECKER data): "(EXIT_c) for c ≥ 3 (exits on the family not yet measured)" is no longer true
- The ADDENDUM lists among "Still NOT refuted: ... (EXITS-POLY) / (EXIT_c) for c ≥ 3 (exits on the family not yet
  measured)". GAPS says "remaining routes: ... R13 (EXITS-POLY / EXIT_c, c ≥ 3)".
- I measured the exits with L-ALG's dtl_prefexits.py, unmodified, same flags:
  | D | n | max exits per (context, step, vertex), stable / Oink | max total exits per context / \|R\| |
  | --- | --- | --- | --- |
  | 2 | 36 | 2 (stable; regenerated file) | — |
  | 4 | 50 | 3 / 3 | 1.50 |
  | 6 | 64 | 4 (stable; regenerated file) | — |
  | 8 | 78 | 5 / 5 | 3.97 |
  | 12 | 106 | 7 / 7 | 7.59 |
- So max exits per (σ, w) = ⌊D/2⌋ + 1 on every D tested. (EXIT_c) fails on this family for every c ≤ 6 already at D = 12,
  in both orders, and the uniform rule makes it fail for EVERY constant c at D ≥ 2c. That is the same shape as the depth
  kill.
- (EXITS-POLY) is NOT refuted: total exits per context grow like D·|R|, i.e. O(n²).
- Consequences for the text, in Lead and L-RED terms:
  - The ADDENDUM's "Still NOT refuted: ... (EXIT_c) for c ≥ 3" and GAPS's "EXIT_c, c ≥ 3" route are contradicted by this
    data.
  - By the rule adopted in C15 Addendum 1, R13 (c) (hypothesis (EXIT_c) for a constant c) now has a falsified signed
    hypothesis on a uniform family, and would get a POST-LANDING NOTE like R12's.
  - What remains unrefuted is (EXITS-POLY), the equivalent polynomial form (R13 (b)/(d)).
- Caveat. These are CHECKER runs of an unmodified tool on pinned and regenerated L-RED instances. They are DATA, and L-RED
  or L-ALG should reproduce them before the text is changed. The D = 2 and D = 6 files are regenerated, not pinned.
- The rest of the list, "Still NOT refuted: (STEAL-POLY_sum), (EXITS-POLY), (CTX⁺), (FIRED⁺-R), GAP-A (iterations D + 8,
  linear)", stands. Nothing in the NOTE or ADDENDUM refutes them, and the Oink iterations are D + 8.

### Notes
- N-1 (staleness inside DE21). DE21's body still says "NOT yet a refutation of (STEAL-DEPTH_D) or (EXIT_c) for every
  constant (that needs a uniform family ...)" and "(no uniform family yet)". The ADDENDUM supersedes both for STEAL-DEPTH.
  Suggest "(superseded for STEAL-DEPTH by the ADDENDUM below)" at both places, and the same for EXIT_c once E-2 is
  reproduced.
- N-2. The ADDENDUM's "re-steals per quadruple are unbounded" means unbounded in n, growing as ⌊(D+1)/2⌋ + 1 = O(n). Saying
  "grow linearly in n" would be more precise and would match "(STEAL-POLY_k) is not refuted" in the NOTE.
