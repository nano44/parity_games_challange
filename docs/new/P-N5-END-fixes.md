# P-N5-END fixes (append-only; the packet docs/new/P-N5-END.md stays frozen at l-new 131b4c1c, sha1 5cae845b)

## Fixes entry 1 (L-NEW successor 64; Lead 05:56Z: L-RED 58 R223 items W-1 and T-1; written 06:17Z by date -u)
- Report answered: L-RED 58 R223 item 1, docs/red/R223-end.md at claude/l-red 143f0b4c. Every P-N5-END statement SURVIVES (L-RED's
  counters, cited, not re-run here: 8,100 family runs, 48,816 exhaustive N ≤ 2 genomes × 3 modes, 30,000 N = 3 genomes, 515
  second-implementation checks, 0 fails; 33 of 33 premise quotes verbatim in trunk). One wording gap (W-1) and one tool remark (T-1);
  neither changes a statement. Both ACCEPTED below.
- The packet is unchanged; where this entry and the packet differ, this entry governs.

### W-1 (R223 §1): the standing SPEC premise in the «To sign» table. ACCEPTED (L-RED's suggested line, verbatim).
- The gap: RESULTS carries 1E-N3 as a STANDING SPEC PREMISE (R57's heading «under the standing SPEC premise 1E-N3»; R104's and R117's
  headings the same way); the packet lists [1E-N3] in §1 and E0-E4, (H) and TERM-XI use it (E0 and TERM-XI through [TAU3] and through
  «τ̄ is Even's optimal counterstrategy»), but the «To sign» table gives the hypotheses of §3-§6 as «every genome» only.
- Fix (governs the «To sign» table): «Hypotheses of every row: under the standing SPEC premise 1E-N3 (RESULTS R57 (b)), as in RESULTS
  R104 / R117.» So the rows read «every genome, under 1E-N3» (E0-E4, TERM-XI, ENDGAME-3, ENDGAME-3-N5), «G ∈ IDEAL-ACYC, under 1E-N3;
  premise R117 (f)» (EXACT-L) and «on REACH3-CYC, under 1E-N3» (END-T3). No statement and no proof changes.

### T-1 (R223 §1): quotes_end.py read four of its five sources from the working tree. ACCEPTED; tool fixed, re-run, re-pinned.
- The remark: quotes_end.py took only docs/RESULTS.md from `git show TRUNK`; SPEC (docs/new/N5-ssi-global.md), XICYC, REACH and QFIX
  (docs/new/P-N5-QUIET-fixes.md) came from the working tree, i.e. from l-new's copies at the freeze.
- Fix: experiments/new/box195/quotes_end.py now reads EVERY source by `git show TRUNK:path`, and asserts the frozen packet's sha1
  (5cae845b…) before it extracts §1 and §6. Re-run against trunk claude/vibrant-johnson-nxvvxo c8f42538f: «quotes 33 missing 0 (every
  source from trunk c8f42538f)» (experiments/new/box195/quotes_end.out, re-pinned in box195/end.pins). This agrees with L-RED's own
  all-trunk re-run (33 of 33 at trunk 4aaba7d52). Unit: one «…»; set: §1 + §6 of the frozen packet. Note: at c8f42538f the trunk
  copies of SPEC, XICYC and REACH are byte-identical to l-new's (sha1 66fde9ef, 149e2414, b7bd6937); RESULTS and QFIX differ, and every
  quote is found in the trunk copies.

## Line L-1 (L-NEW successor 64; Lead brief: «write P-N5-END's line L-1 by script»; W-1 applied; written 06:17Z by date -u)
- docs/new/P-N5-END-line-L1.txt, one paragraph, no «|»; generator experiments/new/box195/mkl1_195.py (run from the repo root with
  `git show c8f42538f:docs/RESULTS.md` as its argument). It asserts the packet's sha1, the RESULTS quotes verbatim, and W-1's sentence
  verbatim (once in this file, once in the line). sha1 68a691764c57ef16bb8a8c294925954a3c71fb1b, 5903 B. Pinned in box195/end.pins.
- Labels in the line: PROVED (lane, unrefereed) for E0-E4, TERM-XI, ENDGAME-3, ENDGAME-3-N5, EXACT-L; PROVED-CONDITIONAL for END-T3, with
  its condition (R118 (k)'s REACH3-CYC and that theorem's own condition) in the line; DATA clauses with counters (unit, set, scope); a
  TARGET.md §2 / §4 scope clause.
