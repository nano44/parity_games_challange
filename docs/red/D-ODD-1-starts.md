# D-ODD-1 / F-1: invalid START files in experiments/red (L-RED successor 38; Lead 13:32Z relaying both P-N5-ODD referees)
Written ~14:0xZ (date -u), 2026-10-31. Label: DATA.
- Defect: sbq2_K8_m16.start sets τ(242) := 243, but succ(242) = 244…258. n5x.start_pair, n5b.read_start and n5.py accept a start
  entry without checking it.

## (1) Validation added (L-RED tools only; other lanes' engines are not mine to edit)
- New experiments/red/startck/startck.py. It checks, for each SIGMA0 / TAU0 entry v:w, that v has the right owner and that (v, w) ∈ E.
  Its `--repair` mode replaces a non-edge with min succ(v) and drops wrong-owner entries.
  trcmp.py compares two n5b runs from different starts.
- The following now REFUSE a bad start (exit with «BAD START …») unless ALLOW_BAD_START=1:
  - seg/xeng.py;
  - rel2/oinkcmp.sh;
  - desc/desc2.py, desc/descstar.py, desc/qtrace.py.
- check.sh sets ALLOW_BAD_START=1 only on the R158 history line (fbg_K4_m6_m48) and comments it. A new check.sh block «D-ODD-1»
  pins the exact list of bad start files, so a new bad one fails the gate.
- NOT done: the ~100 older single-purpose L-RED scripts (they read starts through n5b / n5x / own parsers) were not each patched. The
  scan in (2) covers their pinned inputs instead.

## (2) Scan: every experiments/red .start with a matching .pg (142 files)
| file | defect | claims that used it | effect of repair |
| --- | --- | --- | --- |
| flipev/instances/sbq2_K8_m16.start (98b0927a) | τ(242) = 243 non-edge (obs3.py keeps obs2's obs → y_1 start after obs lost y_1); persists the whole run | R145 §(c) (SB 128 at root, F 152); R153 keych (KEYCH 0); copied to L-NEW / L-SI | see (3) |
| fb/instances/fbg_K4_m6_m24, fbg_K4_m6_m48, fbg_K8_m6_m24 .start | 6 non-edge τ entries each (single-successor Odd vertices given τ = vertex 4; fbsearch.py build). One of them, τ(80) = 4, persists the whole run | R158 (|F| = K(m2 + c), fbg_K4_m6_m48 |F| 235); R162 §2 (fbg DESC_U 640); R163 (all fbg rows); desc/instances/fbg_K12_m6_m24 (R163 pin, now re-pinned with the repaired start) | n5b: same iterations; σ differs only at vertex 105, state 1; the rest is identical up to τ(80). Every fbg count is UNCHANGED (|F|, DESC, DESC*, \|U*\| at K4 m24/m48, K8, K12, K16 m24/m32, K24 m24; xeng + Oink OK on the repaired K4 m24 and K12) |
| n3/instances/comp54_n80.start, n3cov_lean.start | already found and repaired by R99 (successor 23; *_fixed.start valid) | R87, R88, R89 | R99 |
| n3/out/{c1,c2,ph1,ph2,ph7}/best_*.start | wrong-owner entries (climb outputs written for another owner assignment) | R101 table (ph7/best_7: f 23, RF 19, R1 0), R102 seed (S3: unaffected) | ph7/best_7 rerun with a valid start (r1survey): f 23, RF 19, R1 0, unchanged. The others are climb scratch outputs, not cited |
- All other 131 start files are valid. The 7 .start files without a same-name .pg (mei/*.pg.start, seg/*.image.start, the n3 *_fixed)
  are not scanned by name. The two n3 *_fixed files were checked by hand: OK.

## (3) R145 / flipev sbq2 rows, re-run with a repaired start (τ(242) := 244)
| K | m | n | maxSB at root, old → repaired | returns | W-run length, old → repaired |
| --- | --- | --- | --- | --- | --- |
| 4 | 8 | 133 | 32 → 32 | 31 → 31 | 44 → 43 |
| 8 | 16 | 261 (pin) | 128 → 128 | 127 → 127 | 152 → 151 |
| 12 | 24 | 389 | 288 → 288 | 287 → 287 | 324 → 323 |
| 16 | 32 | 517 | 512 → 512 | 511 → 511 | 560 → 559 |
- What changes:
  - The W-run is one transition shorter (the first transition is no longer W-flat with τ(260) changing). Iterations are unchanged
    (152 at the pin).
  - τ(260), the root, starts at 259 instead of 242.
- What does not: SB = K·m at ONE Odd vertex of out-degree 2 (R145 (c)) survives exactly. This matches the referees' «153 states,
  128 flips».
- Faithfulness: xeng identical and Oink OK on the repaired pin start (desc/instances/sbq2_K8_m16.rep.start).
- NOT re-run: R153's keych on sbq2 (KEYCH 0). It is a different tool with its own parser.

## DONE / FINDINGS / NEEDS
- DONE:
  - startck.py and trcmp.py;
  - validation in xeng / oinkcmp / desc2 / descstar / qtrace;
  - check.sh block D-ODD-1;
  - repaired starts desc/instances/{fbg_K4_m6_m24,sbq2_K8_m16}.rep.start; fbg_K12_m6_m24.start re-pinned (desc/pins.sha1).
- FINDINGS:
  - Bad starts: sbq2 (Lead's), plus the 3 fbg pins (6 non-edges each, a NEW find) and the old n3 climb outputs (wrong owners).
  - All re-runs reproduce the reported counts. The only change is that W-run lengths are 1 shorter on the sbq2 family.
- NEEDS: Lead: tell L-NEW / L-SI that their copies of sbq2_K8_m16.start carry the defect, and that R158's fbg starts carry 6 non-edges.
