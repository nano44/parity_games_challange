# R33: box-7 data for GAP-A after R32: (CTX⁺), (RELSTEAL)/(STEAL-ONCE), (FIRED-R), (DIRTY) (L-RED box 7; produced on Opus 5.5)
Written by 16:52Z (date -u, taken at commit time). Status: DATA, unrefereed. Every instance
below was re-run with pinned Oink 8fbf0a7 (`--dtl --no-single --no-wcwc --no-loops -v`, solution verified) and is pinned in
experiments/red/check.sh unless marked "scratch only". Judges: L-ALG's experiments/alg/dtl_rootmono.py UNMODIFIED, via
experiments/red/root/rootfit.py (it parses the tool's printed lines), or a read-only wrapper that imports dtl_rootmono.RM.

## 1. (CTX⁺): distinct first-difference contexts per phase (dtl_rootmono, both orders identical)
| instance | n | contexts | transitions | |G'| |
| --- | --- | --- | --- | --- |
| spp25_oink_n40 (L-RED box 6) | 40 | 10 | 24 | 38 |
| ctx11_n40 | 40 | 11 | 20 | 40 |
| ctx12_n40 | 40 | 12 | 21 | 40 |
| ctx13_n40 | 40 | 13 | 24 | 40 |
| n48 climb best (scratch only) | 48 | 13 | 23 | 48 |
Climb: dtl_search --fitness root, ROOTFIT=ctx, seed 13001, Oink order, from spp22_oink_n40 (8 contexts), about 840 steps to 13,
then flat for about 1.5 h. Growing ctx13_n40 by 8 random vertices (best of 30) dropped it to 8; the n48 climb rebuilt 13 in 9
steps and stayed there. No n-trend yet: 13 at n = 40 and n = 48.

## 2. (RELSTEAL) and (STEAL-ONCE) (dtl_rootmono RM_EXCL=1, l-alg 473edc4b; rootfit ROOTFIT=steal)
| instance | n | relevant new-steal visits at one context | max new steals per (context, round, top, tangle) |
| --- | --- | --- | --- |
| fallv_viol_n28 | 28 | 2 | 1 |
| f1_twofall_n48 | 48 | 2 | 1 |
| fall3_n76 | 76 | 3 | 1 |
| fall4_n116 | 116 | 4 | 1 |
Both orders identical. Relevant steals grow with the chained parts (R31), linearly. (STEAL-ONCE): 0 failures; the steal
climb (seed 19001, Oink, from fallv_viol_n28, about 2,700 steps) stayed at 2 relevant steals, max 1 per quadruple.

## 3. (FIRED-R): distinct tangles fired at one context over a phase (dtl_rootmono RM_EXCL=1 "max tangles")
| instance | n | max fired at one context (Oink / stable) | max fired/|R| |
| --- | --- | --- | --- |
| fallv_viol_n28 | 28 | 4 / 4 | 0.20 |
| f1_twofall_n48 | 48 | 7 / 7 | 0.15 |
| fall3_n76 | 76 | 13 / 14 | 0.17 / 0.18 |
| fall4_n116 | 116 | 17 / 17 | 0.17 |
| ctx13_n40 | 40 | 5 / 5 | 0.17 |
| spp25_oink_n40 | 40 | 6 / 6 | 0.22 |
| fired10_n20 | 20 | 10 / 8 at |R| = 12 | 0.83 / 0.67 |
- fired10_n20 (sha1 a12fe45d): climb ROOTFIT=fired, seed 20001, Oink, from L-ALG's climbs_1016/a_best_s31. 10 distinct tangles
  fire at one context of |R| 12 over 2 visits (1 transition). Above L-ALG's 0.5·|R| data line, but SHORT phase: per the Lead
  (16:22Z, L-ALG §22w) (FIRED-R) has content only on long phases (S ≥ 2|R|), where it is open.
- LONG phases (root/firedlong.py: same model and fired-set union as L-ALG dtl_firedclimb.fitness, only phases with S >= 2|R|,
  contexts visited >= 2 times): spp_chain_up_n43 0 (no long-phase context visited twice), spp25_oink_n40 2 fired at |R| 9
  (S 25), ctx13_n40 0. Climbs 21001/21002 (from spp25, both orders) and 21003 (from ctx13), about 250 steps each by 16:52Z:
  no improvement (2 / 9, 0). Slow: about 7 s per step at n = 40.

## 4. (DIRTY) (dtl_rootmono, l-alg 8a2a149; superseded by (FALL) at 13:04Z)
Max dirty root transitions per phase: 12 / 9 (Oink / stable) at n 28 (h4_def11), 9 / 9 at n 44 (h4_def8); two-copy union of
h4_def11 with random cross edges (compose.py): 13 / 13 at n 56 (keep_d13_n56, scratch only; pinned Oink 16 iterations
verified); growth chain (best-of-40 growths): 12 at n 32. Note: #DIRTY per phase <= searches per phase (<= |G'| on all data).

## 5. Dead or discharged this box, with the instance (for the record)
(MEET) DE15 meet_viol_n17; (FALL-V) R32 fallv_viol_n28; FALL <= 2 per context: R31 fall3_n76 / fall4_n116; Dom e* and STR-DET
discharged by L-ALG/referees (my searches found none: corpus 0 / 1,062 transitions for both).
