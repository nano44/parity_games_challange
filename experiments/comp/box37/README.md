# L-COMP BOX 37 item 1: the family behind the k = 1 climb bests (L-COMP 16, 2026-11-09)
Labels: everything here is DATA (scope: N5'-xi from S3 on Gamma3 up to the first fallback, [E-LEV]; unit = one genome).
Counters: Qf = flips at gate (Q, 0) (per gate); maxflip = per-gate MAXIMUM of flips; C = max over (v, I) of #tops of one letter;
T3 = iterations up to the first fallback (total); k = Xi-feedback number (own36.kfvs). Engines: fast36 (bin/k build of box36/fast36.c,
plus a W = 96 build for n >= 18) and own36 (Python, box36/own36.py on box34/own34.py).

## Findings
1. The record gate (82, 0) of BEST_C300_r17..r34 is MWR8_2's mover **Q** (the race letter y), NOT qz (62). In MWR8_2 gate (Q, 0) has
   0 flips and qz has 17; along the C300 chain qz stays at 17 and Q goes 20, 24, 28, 32, 34 (align37.py chain MWR8_2 -> r17 -> ... -> r34,
   names in out/align/n_*.json). The climb opened a second flipping gate; it did not grow qz's.
2. The climb bests are **MWR8_2 plus inert decoration**. Ablation of r34 (ablate37/shrink37): reverting any single one of the 39 edit
   units leaves (Qf, C) = (34, 17) except the br order (-> 4, 9) and the bp bit of a47's option 1 (-> 32, 16); reverting all the others
   together leaves a core of N + M 261 (= MWR8_2's size) with Qf 34, C 17. The extra 28 units of size in r34 do nothing.
   brmin37 / movemin37 reduce the core's br permutation to 5 single-option relocations; of these, two carry the effect (scan37):
   (R, qz-option) raised anywhere into the hiX0 block (lane exits) and a lane option (a_i, 0) raised into the hiX0 block.
   With i = m (the last lane node) no bp edit is needed. Scan (out/align/scan*.txt): C = 9 + #{k : a_{51-6k} <= i}, i.e. one extra
   top of the low letter per qh_k lane entry passed.
3. BEST_B400_r34 (1694d52f) is a variant: core N + M 261, Qf 34, C 17 at gate (Q, 0); it shares a raised lane option ((a50, 0)) but
   leaves (R, qz-option) at its MWR place and instead edits qz (bp 1 -> 0, plus a 2nd option wt b8_1 xt qh8) and deletes a37's exit
   option (out/align/core_namedB.json). Same counts as gen37(8), different bytes.
4. **gen37(n)** (gen37.py) = MWR(n) (L-RED R229 genmw229.py @ claude/l-red 406ef2fd, WTGT=R, L = 2; verbatim copy genmw229_copy.py,
   sha1 ba1686db) with ONLY two br moves: (R, qz-option) and (a_m, 0), m = 6n + 4, moved to just above (a_1, 1).
   Byte-for-byte reproduction of the two bests: NOT possible as a family member (they carry inert decorations and ~150 inert br swaps);
   gen37(8) reproduces their counters (Qf 34, C 17, k 1, lamch 0) at N + M 261 < 289 / 297.
5. Measured n = 2..23 (fast36; N + M 87..696) and n = 2,3,4,5,6,8,10,12,14,16,18,20,23 (own36): the two engines agree on every column.
   EXACT (zero residual on every row): Qf = maxflip = 4n + 2, C = 2n + 1, T3 = 6n + 7, N + M = 29n + 29, lamch at Q = 0, k = 1.
   So Qf = (4/29)(N + M) - 2: LINEAR. Log-log p (fit37.py) is only the offset: see out/fit37.out.
   Per unit of size gen37 has the most flips at one gate of the k = 1 families seen so far (0.135 at n 23, against MWR's 0.067; MW(n)
   0.135 has k = 2).

## Files
align37.py (DP mover alignment, names), named37.py (named genome form), ablate37.py / shrink37.py (edit ablation), brmin37.py /
movemin37.py (br minimisation), scan37.py (anchor scans), gen37.py (family), meas37.py (measurement, both engines), fit37.py (fits).
inst/gen37_n<n>.json (sha1 in out/meas37_*.out); out/align (names, cores, scans, B400 alignment).
