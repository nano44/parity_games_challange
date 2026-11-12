# L-COMP BOX 39 (successor 18; Lead «go» 06:21Z 2026-11-12): Q_(>c) counter, climb, fit. All DATA.
Nothing here is a TARGET.md claim. G-N5-TIME stays OPEN; N5′-xi stays a CANDIDATE (D1). CONJECTURE DEEP-k1 (box 206) is untouched:
nothing below is above linear.

## Counter (item 1): depth39.py
- MY IDEAL-CYC engine (box37/ideal37.py: Γ(G) build, Howard switch-best at the movers, my tie rule), with box 206's definitions written
  from its TEXT (claude/l-new 134adb53, docs/new/N5-DEPTH-box206.md l. 7, 12-16, 20, 74; quoted in the script header), not L-NEW code.
- Counters (unit; set; scope): Q = loud steps (unit: step of one IDEAL-CYC run from the start, total per run; scope all = every vertex
  of Γ(G)); Q_(>c) = loud steps of loud depth > c; maxdepth = largest change depth (unit: (vertex, step)); hist = loud steps by loud
  depth. Must-0: elfall [(vertex, step)] (R121 E-MON), ufail[c0] [(change, c0), c0 = 0, 1, 2] (DEPTH-COUNT). Relevance = e-priority;
  G["ekey"] (L-RED R230-elev §1) applied when present (ring3 only). D_mov from ideal37.heights.
- Cross-check (xcheck39.sh; out/xcheck39_all.out, _ctrl.out, _dmov.out; inputs inst/, sha1 in inst/SHA1SUMS): 27 genomes, **0 mismatches**
  against every published number:
  | genome | T | Q_(>1) | loud-depth histogram | source matched |
  | --- | --- | --- | --- | --- |
  | MWR4/8/16_2 | 30/54/102 | 0 | {0: T−1, 1: 1} | box 206 §3.1 |
  | K1F21_n48 / K1F34_n84 / K1C16_n400 / B400_r32 | 31/52/51/49 | 2/2/1/1 | §3.1 rows | box 206 §3.1 |
  | K1D4_n48 | 23 | 0 | {−1: 2, 0: 10}, maxdepth 5 | box 206 §3.1 |
  | K1L7_n48 / K1L10_n48 / BLKX23_n48 | 37/31/28 | 7/10/3 | Add. A1 / B1 / B | box 206; R231-box206 §2 |
  | CW4/8/16_n, CW32_own | 30/59/114/225 | 2/7/14/29 | {0: …, one step at each depth} | R231-box206 §3 (L-RED 65); D_mov 12/38/92/202 |
  | CWRR4/8/16, CWRQ4/8/16 | 28/52/100 | 0 | max loud depth 0 | Add. D; R231-cwr |
  | CLA25_n64 (L-RED) | 33 | 5 | {−1: 1, 0: 24, 3: 1, 4: 2, 5: 2} | R231-box206 §4 |
  | BLKX26_n48 | 33 | 6 | (no published Q) | — |
  | ring3A/B/C/D_k8_m12 | 12 | 0 | {0: 12} | (R231-stall3 publishes no Q: mine only) |
  elfall = ufail = 0 on all 27. Control DEP_CTRL=1 fires: K1L7 elfall 1,059 (= L-RED's DEP_CTRL=1 figure), MWR4_2 elfall 338.

## Climb (item 2): climb39.py, band39.sh (k = 1; score (Q_(>1), Q, T), raw; 1 restart x 200 proposals per stream; box 38 move set)
- Second engine: every new best re-run on L-NEW's depth206.py (worktree of claude/l-new 8d6c363b, DEP_ALL=1). depth206 prints loud
  depths >= 8 in one bucket «L8» (its l. 72: min(d + 1, 9)); agreement = same T and same histogram with mine capped at 8 (the first
  C600a log lines say «agree False» from the uncapped comparison; capped re-check below). Q_(>1) is unaffected by the cap.
- Seeds. Lead reading: of the brief's three seeds (CW(n) at the band, gen37 at the band, K1L7 grown), stream A = CW(n), stream B = the
  better of gen37 and grown K1L7 by Q_(>1). gen37_n9 (290): Q_(>1) 1; gen37_n19 (580): 1. K1L7 grown with growth-only moves (add option,
  add mover; k = 1; accept iff Q_(>1) does not fall): 281 (Q_(>1) 7, sha1 a58cbc0e), 580 (Q_(>1) 12, sha1 7b03650a). CW15 (597) built
  with L-RED's carry231.py on genmw229.py WTGT=R n 15 (same pipeline gives CW8 = L-NEW's sha1 da29577d).
- Results (frozen out/climb39/BEST_*.json; sha1 in the logs; all k = 1, all must-0 counters 0):
  | stream | seed (Q_(>1)) | best Q_(>1) | N + M | T | sha1 | L-NEW depth206 (capped) |
  | --- | --- | --- | --- | --- | --- | --- |
  | C300a | CW8_n (7) | 10 | 303 | 60 | 978ed2a7 | agrees (T 60, Q_(>1) 10) |
  | C300b | K1L7 grown 281 (7) | 7 (no gain) | 281 | 20 | a58cbc0e | agrees |
  | C600a | CW15 (14) | **18** | 612 | 53 | f6a910ce | agrees (T 53, Q_(>1) 18) |
  | C600b | K1L7 grown 580 (12) | 13 | 584 | 24 | 101ef1e3 | agrees |
  | D300a (Q_(>2), budget left) | C300a best (Q_(>2) 9) | 9 (no gain) | 303 | 60 | 978ed2a7 | agrees |
  12/12 frozen bests agree with depth206 (capped histogram, T and Q_(>1)).
- READING: the band maxima are CW(n) plus a few deep steps (C600a: 14 -> 18; C300a: 7 -> 10); T stays linear (53-60 at these sizes,
  C600a's best even lowered T from 108 to 53 while raising Q_(>1)). The grown K1L7 seeds (deep but short runs, T 20-24) do not beat CW.

## Fit (item 3): fit39.py, out/fit39.out
- BOX 37/38 points (pts39.py, out/pts39.jsonl): Q_(>1) on all 163 frozen BOX 37/38 climb bests (D_mov / T3 scores; k = 1 on 126): max
  Q_(>1) = 3 (N + M 244-582); must-0 counters 0. These climbs did not optimise Q_(>1), so they lie far below the envelope; they are
  points «where defined», not maxima.
- Envelope (max Q_(>1) per size, k = 1): (145, 10) K1L10, (303, 10) C300a, (612, 18) C600a, (1515, 29) CW32: log-log exponent
  0.49 +- 0.11; linear 0.0145 (N + M) + 7.4. CW(n) alone, n >= 8: 0.88 +- 0.02 (Q_(>1) = 2 / 7 / 14 / 29 at n = 4 / 8 / 16 / 32: n − 1 to
  n − 3, linear in n, sub-linear in N + M because M grows faster than n). Two band maxima only: 0.84.
- Verdict: exponent **NOT identified** as an asymptotic statement. Reasons: (a) unequal search effort per point (K1L10: 9,000 L-NEW
  iterations at N 48; my bands: 200 proposals; CW32: no climb); (b) the climbs' bests are CW(n) plus a constant-ish gain, so the fit
  measures the hand family more than the search; (c) 4 distinct sizes only. What the DATA does say: no point is above linear; Q_(>1) /
  (N + M) <= 0.07 (145), 0.033 (303), 0.029 (612), 0.019 (1515); nothing to send as «above linear».

## Files
depth39.py (counter), xcheck39.sh, climb39.py + mut39.py (box 38 move set) + band39.sh, pts39.py, fit39.py; inst/ (frozen inputs and
seeds, inst/SHA1SUMS; L-NEW's and L-RED's SHA1SUMS copied as SHA1SUMS.lnew206 / SHA1SUMS.lred231); out/. Resumable: climb39 OUT.state,
band39.sh flock + DONE skip, pts39 skips done genomes. band39.sh needs env LNEW = a worktree of claude/l-new.
