# R230 item 5: is HYPOTHESIS [E-LEV] needed for N5′-xi's polynomial count at bounded U(G)? (counter side)
L-RED successor 64, D1 / D18 / D14. Lead routing 2026-11-12 00:00Z. Written 2026-11-12T02:03Z (date -u).
Object: trunk RESULTS R125 (origin/claude/vibrant-johnson-nxvvxo 4c2f407d2, docs/RESULTS.md l. 15595), Theorem CHAIN3, «PROVED under
HYPOTHESIS [E-LEV] and CONDITIONAL on P-N5-END's Theorem ENDGAME-3 … and P-N5-ASC §4»; [E-LEV] = «lev(x) < lev(x′) implies
pr(e_(x,k)) < pr(e_(x′,k′))», used «for UP-JUMP3, UP-B3 and CHAIN3 only». Labels: PROVED (lane) / CONJECTURE / DATA / DEAD / READING.

## 0. Verdict
- No super-linear growth found. Over three size caps (N ≤ 12, 24, 48) at U(G) = 2 with [E-LEV] violated (inv > 0), the climbs' best
  T3 is 23, 31, 39: +8 per doubling of N, and T3 / (N + M) falls 0.49, 0.42, 0.29 (DATA, §2). Nothing to freeze as a major finding.
- Every run (8 seeds, 3 bests, 90,000 climb evals) has exactly one fallback and total = T3 + 3, and nstd = 0: CHAIN3's «T3 + 3» shape
  and REACH3-ALL's standard-state run hold with permuted e-priorities too (DATA). REACH3-ALL itself does not use [E-LEV] (R125's premise
  list), so this is a consistency check, not news.
- Permuting does lengthen runs at small N: the same best genome in [E-LEV] order has T3 15 (c12) and 20 (c24) against 23 and 31
  permuted; at N 48 the two coincide (39). The longest run seen (T3 52, seed MWR8_2, N 84) is below R125's own max T3 129 (LEAP_k64)
  under [E-LEV].
- READING (not a result): the data say nothing about whether [E-LEV] is needed in the PROOF. R121 already records that it is necessary
  for UP-JUMP / NOUP on IDEAL-CYC (REFEREE-2 CTRL=elevrev; L-RED NOUPC_1-3, claude/l-red 68a1f609), so without [E-LEV] UP-B3's ascent
  bound is lost and CHAIN3's route has no replacement; the question «polynomial without [E-LEV] at U ≤ B» stays OPEN. A climb on
  T3 is weak evidence: its reach is bounded by mutation and size (§3).
- I did not read L-SI 50's BOX 98 or L-COMP 17's U(G) census outputs; not cited.

## 1. Set-up (experiments/red/r230/elev230.py, climbel230.py)
- Genome → Γ3(G) by L-NEW gamma3.build (l-new fcba92fc, via env LNEW), then the e-vertices' priorities PERMUTED: the same SET of
  priorities gamma3 assigns, re-assigned to the options in the order of a per-option key G["ekey"] (instead of (lev, gate)).
- Run: L-NEW n5v (N5′-xi, mode "xi") from start_pair (S3) to the end, cap 20,000 iterations (never reached).
- Counters (unit: per genome, one run): U = #options whose Ξ-target has a higher level; inv = #option pairs (q, q′) with
  lev(q) < lev(q′) and pr(e_q) > pr(e_q′) ([E-LEV] iff inv = 0); T3 = index of the first fallback − 1; total = iterations to the end;
  fb = #fallbacks; nstd = non-standard states before the first fallback (as std230).
- Climb: move = ekey swap / re-draw (p 0.35) or mut230.mutate (structure, size ≤ NMAX, degree ≤ 3); reject U > 2 or inv = 0; accept
  score (T3, total) ≥ current. Seeds repaired to U = 2 by elev230 repair (re-points upward Ξ-targets).

## 2. DATA
| run | seed (start) | evals | N | M | U | inv | T3 | total | fb | nstd | T3 in [E-LEV] order |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| c12 (seed 2315, N ≤ 12) | seed_r12 (T3 10) | 30,000 | 12 | 35 | 2 | 234 | 23 | 26 | 1 | 0 | 15 |
| c24 (seed 2312, N ≤ 24) | seed_C (T3 7) | 40,000 | 24 | 50 | 2 | 412 | 31 | 34 | 1 | 0 | 20 |
| c48 (seed 2313, N ≤ 48) | seed_MWR4_2 (T3 30) | 20,000 | 48 | 89 | 2 | 360 | 39 | 42 | 1 | 0 | 39 |
| seeds (no climb): r12 / C / MWR4_2 / MWR8_2 / B | | | 12 / 24 / 48 / 84 / 64 | 36 / 55 / 97 / 177 / 127 | 2 | 290 / 536 / 130 / 882 / 2020 | 10 / 7 / 30 / 52 / 4 | T3 + 3 | 1 | 0 | 7 / 7 / 30 / 52 / 4 |
- Rejected mutants (U > 2 or inv = 0): c12 1,556, c24 2,258, c48 253. nstd-fails 0 in all 90,000 evals (unit: evaluated genomes with
  nstd > 0).
- c12 / c24 bests were last improved at evals 20,833 / 37,344; c48's at eval 9,813 of 20,000 (logs in out/elev/).

## 3. Reach and limits
- Sizes N ≤ 48 (climbs), N ≤ 84 (seed); degree ≤ 3; U = 2 only. U = 0, 1 and larger U are not run.
- Hill climb, single chain per cap; T3 is the only target. A construction that needs coordinated priority + structure changes (e.g. a
  binary counter) could be out of reach. No tightness claim and no upper bound follow.
- One engine (L-NEW gamma3 / n5v); no second engine on the permuted games.

## 4. Frozen instances
experiments/red/r230/inst/elev_best_c12.json, elev_best_c24.json, elev_best_c48.json (the climbs' bests, _evals removed); sha1 from
`git show <SHA>:path | sha1sum` in the commit message / notebook.

## 5. Sources opened
docs/RESULTS.md R121 (l. 14320) and R125 (l. 15595) at trunk 4c2f407d2; L-NEW gamma3.py / n5v.py at l-new fcba92fc (code, as engine).
- sha1 at claude/l-red fabfe38e1: elev_best_c12 afaf9e8a…, elev_best_c24 50d82fe6…, elev_best_c48 6606feaa….
