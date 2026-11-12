# L-COMP BOX 38 (L-COMP 17, 2026-11-11/12): item 2 U(G) AXIS (for L-SI 50 BOX 98) and item 1 SIZE-BAND CLIMB
Labels: everything here is DATA. Scope of every T3: N5'-xi from S3 on Gamma3 (P-N5-REACH §3 / R117) up to the FIRST FALLBACK, a TOTAL
over that run (not per gate); Ttot = N5'-xi's TOTAL iterations to the end (SPEC passes through steps 2-5, n5b reading A8); F = fallback
passes. Unit: one genome (one run). [E-LEV] = e-priorities ordered by (level, gate); "no E-LEV" = by gate only (FAST36_NOELEV /
own34 --noelev / lnew38 --noelev patch). Nothing here is a theorem; CHAIN3's bound is quoted, not re-proved.

## U(G) (implemented in u38.py from the text)
P-N5-ASC §6 l. 179 (Corollary UP-B; landed RESULTS R121 (g), docs/RESULTS.md l. 14320 / 14505-14506 on trunk 86f62c26): «Let U(G) :=
the number of options (x, k) whose Ξ-target is a mover of level > lev(x).» xt = -1 (K0) is not a mover. Cross-check: = L-NEW
ug193.py (check193.out l. 59-71) on the 8 box 193 pins it lists (U 21, 4, 6, 17, 4, 7, 6, 1); L-NEW qt3_196.py uses the same formula.

## Engines
- fast36 / fast38 (box36 C engine, validated in BOX 36; fast38 = + T3 argmax in block mode, diff in fast38.c header): T3 only.
- full38.py = MY engine (box34/own34.py, text engine) + SPEC step-4 fallback (n5b A7), run to the end: T3, Ttot, F.
- lnew38.py = L-NEW's n5v mode "xi" (box 190) on gamma3.build (box 189) from n5x.start_pair, claude/l-new 1478886e: T3, Ttot, F.
- fullval38.py: all three on a genome, both modes. out/fullval38.jsonl: 188 genomes (every argmax below + both ends of every ladder),
  N + M 4-486, U 0-216, x 2 modes = 376 runs: 376/376 AGREE (fast36 T3 = mine = L-NEW; Ttot and F equal) and 376/376 have
  F = 1 and Ttot = T3 + 3 (ENDGAME-3's prediction; P-N5-END, lane-proved). So below, "Ttot" = T3 + 3 on every genome checked.

## (a) EXHAUSTIVE: max T3 per (N, M, U), ALL genomes of (N, M) (box 33/36 space, gen36.py; sweep38.py; out/sw_N<N>M<M>.jsonl)
U is constant on a gen36 block (it depends on lev, D, xts only). Genome totals equal BOX 33/36's ((2,4) 14,929,920; (3,4) 56,623,104;
(4,4) 46,080,000). Argmax genomes: out/argmax/T3_N<N>M<M>_U<u>_<mode>.json. Table: out/table38.md.
RESULT: at N + M <= 8, max T3 is 0-2 on every U, identical with and without [E-LEV]; T3 does not grow with U at these sizes.

## (a') SAMPLED: 20,000 random genomes per (N, M), 13 pairs, N + M 12-48 (samp38.py, sampler stated in its header; out/samp38.jsonl)
max T3 [E-LEV] / no E-LEV per U: <= 12 everywhere; e.g. (12, 36): U 0 -> 5/5, U 4-20 -> 10-12, U 26-27 -> 3-4; (16, 32): U 1 -> 4,
U 8-17 -> 9-11, U 24 -> 5. N = M (one option per mover): T3 = 0. The two modes differ by <= 3. Random genomes have small T3; the sample
says little about worst cases.

## (b) STRUCTURED: U-LADDERS at FIXED N + M (ladder38.py; only Xi-targets move; out/lad/*.out, rung genomes out/lad/g/)
down = one upward option per rung -> K0 (all paths end at the same U = 0 genome); greedy = keep T3 largest; rand1/2 = random order.
| base | N + M | U base | T3 base | T3 at U = 0 | min T3 on the ladder |
| --- | --- | --- | --- | --- | --- |
| gen37(n), n = 2,3,4,5,6,8,10,12 | 29n + 29 | 3n + 3 | 6n + 7 | 6n + 4 | 6n + 4 (monotone) |
| gen37(n) no E-LEV, n = 2, 4, 8 | same | same | 6n + 7 | 6n + 4 | 6n + 4 |
| L-SI 85 TC2 | 173 | 34 | 12 | 10 | 7 |
| TC3 | 335 | 64 | 18 | 14 | 8 |
| CL2_22 | 460 | 85 | 28 | 28 | 12 |
| CL3_32 | 486 | 90 | 24 | 23 | 11 |
up (random) from the U = 0 ends of gen37(4), gen37(8), TC3: T3 falls to 2-4 at U 91 / 167 / 216 (random upward edges destroy the
structure). READING (not a claim): on every structured family here, removing ALL upward Xi-edges lowers T3 by at most 4; the linear
growth of gen37's T3 survives at U = 0 (T3 = 6n + 4 at N + M = 29n + 29).

## (c) U-CONSTRAINED T3 CLIMB at fixed N + M band (climb38.py SCORE T3, KONE 0; cl38.sh; out/climb38_L*.log, bests out/climb38/)
Band [140, 160], seed = gen37(4)'s U = 0 form (T3 28), 6 restarts x 1,500 proposals, same seed and RNG stream for every B:
best T3: U <= 0: 33; U <= 2: 32; no U constraint: 34 (at U 6). (gen37(4) itself: U 15, T3 31, N + M 145.)
Band [280, 300] (seed gen37(9) U = 0 form, N + M 290): see below when finished.

## CHAIN3's bound against the data (chainb38.py; formula quoted from P-N5-CHAIN L3 / box 196 §5 and P-N5-ASC §5)
log10 of the bound on T3 + 3: gen37(2) U 0: 13.3, U 9: 4,361; gen37(4) U 0: 14.8, U 15: 3.2e5; gen37(12) U 0: 17.7, U 39: 6.5e12;
CL2_22 U 0: 18.3, U 85: 4.7e26. Data: T3 + 3 <= 82 on all of them. The bound's dependence on U (F'_U doubly exponential in U) is not
visible in any family here: the U = 0 bound alone exceeds the data by > 10^11.
