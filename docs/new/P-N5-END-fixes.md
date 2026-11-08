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

## Fixes entry 2 (L-NEW successor 64; Lead 06:33Z: REFEREE 29 R-P-N5-END, «Line requirements LN-1..LN-8 … follow them exactly»; written 06:58Z by date -u)
- Report: REFEREE 29, docs/referee/R-P-N5-END.md at claude/referee e4cb208a: every row SIGN; END-T3 SIGN as PROVED-CONDITIONAL on
  REACH3-CYC (R118 (k), itself PROVED-CONDITIONAL on [REACH-L]); [OPT] = [1E-N3] for SPEC runs; optional EN-1..EN-4; line requirements
  LN-1..LN-8 (§7, written when no line existed). The packet is unchanged; entry 1 is unchanged; where they differ, this entry governs.
- Order of events: line L-1 (sha1 68a69176…, 5,903 B) was written and pushed (l-new a60733b8) before REFEREE 29's report reached this
  lane. L-1 is SUPERSEDED by L-2 below; it is not edited (history).

### EN-1 (taken, Lead 06:33Z «take it with W-1»): EXACT-L's dependence on SPEC's tie-breaks. Packet wording governed by this entry.
- Added after Corollary EXACT-L: «EXACT-L uses SPEC's S1 tie-breaks (through REACH3's [RULE] choice); with another pointwise-optimal
  S4a choice the identity can fail (REFEREE R-P-N5-END §4 (C): F = 1 on 382 of 382 IDEAL-ACYC genomes with L ≥ 1).» The packet's «N5
  (SPEC S1-S5)» already includes FIX 1-4, so EXACT-L is unchanged; ENDGAME-3-N5 does not depend on the tie-break (EN-2).
### EN-2 (taken): ENDGAME-3-N5 uses only (H), so it holds for every rule whose S4a output is a pointwise optimum of H (REFEREE 29's n5w
  DATA, §4 (A), cited, not re-run). No statement change; a reading of the proof the referee checked.
### EN-3 (taken): Consequence after EXACT-L: «a polynomial bound on L(G) would bound N5 on them» → «… would bound N5's iteration count on
  them» (the cost per iteration at bit cost is a separate gauntlet step-4 item).
### EN-4 (taken): (H) in §2: «not its own H-cycle node» → «the cycle node of W*(v) is not v». Same meaning, stated on the value.

### Line L-2 (LN-1..LN-8 applied; written by script)
- docs/new/P-N5-END-line-L2.txt = L-1 + R1-R16, by experiments/new/box195/mkl2_195.py: asserts L-1's sha1, each old string exactly once
  in L-1, the LN-4 quote verbatim in trunk docs/new/P-N5-XICYC.md (git show c8f42538f), one line, no «|», «(» = «)». Result: sha1
  e8a8ac51cc79c9de4000749899e7f0b860eeebe5, 6988 B. Map of requirements to replacements:
  - LN-1: R2 (each PROVED, every genome), R4 (EXACT-L PROVED for G ∈ IDEAL-ACYC in REFEREE's words + R104's quote), R6 (END-T3 on
    REACH3-CYC, itself on [REACH-L]).
  - LN-2: R1 (N5 = SPEC S1-S5 with FIX 1-4), R3 (ENDGAME-3's form «exactly one fallback, at an iteration F ≥ 1, and exactly F + 2
    iterations»). Γ3(G), n = N + 7M + 10, N5′-xi = R118's [N5XI], start S3, iterations (SPEC S4): already in L-1.
  - LN-3: R4 («N5 (SPEC S1-S5 with its FIX 1-4 tie-breaks)» and EN-1 in substance, with REFEREE's 382 / 382 cited as REFEREE's counter).
  - LN-4: R7 (T3 quoted from P-N5-XICYC §7, the frozen packet R118 (k) lands; RESULTS' own text gives T3 + 1 as the first fallback).
  - LN-5: R8 ([TAU3] = RESULTS R117 / P-N5-REACH §6.4), R9 ([OPT] = [1E-N3] for SPEC runs; R118 (b)'s [OPT] not used); [1E-N3], R15 (c),
    R117 (f), R118 (k) already named in L-1 (with W-1).
  - LN-6: R10 (sets: 24,000 + 24,000, the 14 corpus genomes in spec mode, check195's set), R11 (units for nofb, capped: runs; late:
    iterations after F + 2), R12 (EXACT-L spec runs only; RECT_d11_T59_norm 62 iterations; «record only (not re-run by check.sh, which
    leaves LRED unset)»), R13 (controls with their counters and units, as in check195.out), R14 (other groups' counts removed from the
    line: they are not in this lane's pinned outputs; the replays are cited by commit). 4,283 and 3,000 are sums of sweep195.out's columns
    (REFEREE 29 §5: EQUAL).
  - LN-7: R15 («(OPEN)» after L(G)); not M3, not M4, not a step-4 pass, G-N5-TIME OPEN, CANDIDATE (D1): already in L-1.
  - LN-8: R16 (fixes entries 1-2); L-NEW successors 63-64 and credit L-RED 56: already in L-1.
  - EN-3: R5.
- end.pins: this file re-pinned; L-2 and mkl2_195.py added. check.sh block «P-N5-END» unchanged.

## Fixes entry 3 (L-NEW successor 65; line-only; written 10:18Z by date -u)
- Sources: REFEREE-2 34 second review, claude/referee-2 9b3cc9b6, docs/referee-2/R2-P-N5-END.md «Line L-2» (+ Addendum 1 0f82f03b:
  verdicts equal to REFEREE 29's); REFEREE 29 R-P-N5-END.md §C (claude/referee e4cb208a / 407f4a21) optional EL-1, EL-2. Both referees
  SIGN every statement (END-T3 PROVED-CONDITIONAL on REACH3-CYC). No statement and no proof changes; the packet stays frozen.
- Lead 09:52Z routed the round; Lead ruling 10:18Z: «P-N5-END L-3: take S1-S5, DROP S6» (a line-only fixes entry need not be named in
  the source note).
| item | from | kind | change in the line (old → new, each old string once in L-2) |
| --- | --- | --- | --- |
| S1 L-R1 | REFEREE-2 34 | REQUIRED | «so the K-config changes only at a fallback …» → «so the K-config leaves κ0 only at a fallback …» (E3 and E4 are S4a steps that change the K-config; ENDGAME-3's proof uses exactly this reading) |
| S2 N-1 | REFEREE-2 34 | optional, taken | after SELFL_n3's «has L(G) = 1» insert «(IDEAL run read with B_s the set of β-ids on its eventually periodic X-chain; R104's IDEAL run is defined on IDEAL-ACYC)» |
| S3 N-2 | REFEREE-2 34 | optional, taken | «ctrl2 e0fail 200 and e1fail 200 (unit: states)» → «ctrl2 e0fail 200 (unit: states) and e1fail 200 (unit: iterations before the first fallback)» |
| S4 EL-1 | REFEREE 29 | optional, taken | «their transfer to the Γ3 run (equal runs at exact VJ ties) is NOT proved» → «their transfer to the Γ3 run is NOT proved (the Γ3 run can differ from the IDEAL-CYC run at exact VJ ties, R118's DATA)» (REFEREE 29's parenthesis; lane placement) |
| S5 EL-2 | REFEREE 29 | optional, taken | «REFEREE 29 R-P-N5-END §4 (claude/referee e4cb208a)» → «REFEREE 29 R-P-N5-END §4 (A), (B) (claude/referee e4cb208a)» |
### Line L-3 (written by script)
- docs/new/P-N5-END-line-L3.txt = L-2 + S1-S5, by experiments/new/box195/mkl3_195.py (from the repo root): asserts the packet's sha1
  (5cae845b…), L-2's sha1 (e8a8ac51…), each old string exactly once in L-2, one line, no «|», «(» = «)». Result: sha1
  d6afe92ae0d2c0021743c99d2bd10f16cad27c73, 7,215 B, 105 «(» = 105 «)». L-2 kept (superseded).
- end.pins: this file re-pinned; L-3 and mkl3_195.py added. check.sh block «P-N5-END» unchanged.
