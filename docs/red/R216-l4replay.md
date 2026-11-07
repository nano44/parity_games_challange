# R216: replay of L-LOWER 4's CANDIDATE records (Lead 05:20Z / 05:34Z / 05:55Z / 06:12Z) — L-RED successor 53
Written 2026-11-07 07:2xZ (date -u). Labels: REPRODUCED = the claim's numbers re-computed with L-RED tools from the pinned file.
No claim about T^R beyond the certified lower bounds below; G-N5-TIME stays OPEN.

## 0. Answer: all four REPRODUCED
| file (claude/l-lower commit) | sha1 (checked) | d | T | F per level (levels 0-6) | per-mover moves, levels 0-6 |
| --- | --- | --- | --- | --- | --- |
| RECF4_d20_F60 (2f15c81a) | 354b7d44… | 20 | 67 | 2, 6, 14, 30, 60, 13, 9 | 1/1, 3/3, 7/7, 15/15, 30/30, 7/6, 6/3 |
| DBL4_d20_F30 (33eb8593) | 43704358… | 20 | 30 | 0, 2, 6, 14, 30, 7, 8 | 0/0, 1/1, 3/3, 7/7, 15/15, 2/5, 4/4 |
| H5_d20_F62 (c45cf2f3) | 2204079d… | 20 | 136 | 2, 6, 14, 30, 62, 62, 62 | 1/1, 3/3, 7/7, 15/15, 31/31, 31/31, 31/31 |
| H6_d24_F126 (10cac3d9) | fb37fec9… | 24 | 209 | 2, 6, 14, 30, 62, 126, 63 | 1/1, 3/3, 7/7, 15/15, 31/31, 63/63, 31/32 |
- DBL4: pairs 1-4 move 1/1, 3/3, 7/7, 15/15, F(l) = 2F(l−1) + 2 from F(0) = 0, as claimed.
- RECF4: F(4) = 60 (two short of 62), as claimed.
- H5: F = 2, 6, 14, 30, 62 on levels 0-4 (R113's cap 2^(l+2) − 2 attained on five levels), as claimed. Also, levels 5 and 6 each have F 62 (31/31).
- H6: F = 2, 6, 14, 30, 62, 126 on levels 0-5 (six capped levels), as claimed. Level 5's movers move 63 times each (> 2d = 48).
- Full per-mover lists: experiments/red/r216/out/lowrep.txt.

## 1. Checks (L-RED code; box 150 is L-NEW's checker, run as an extra)
- r214/memb.py (𝓛^R_d membership, C1-C9, Ξ-acyclic incl.): PASS, all 4 originals and renumbered copies.
- r187/ideal.py replay from the stored start (via r214/lowrep.py): T and moves as in the table. Every run ends «stuck», i.e. a fixed
  point: nothing changes. Original and renumbered copies agree.
- r189/lemck.py on the renumbered copies (r214/renum.py): viol SBAR 0, TAU 0, ESC 0, W 0, AV 0, KEY 0, FB 0, all 4.
- box 150 check.py: VIOL 0, XSIM 0, all 4 (out/box150.txt).
- Real game (r216/g3run.py): N5 (n5v.py spec @ acdbd28b) on Γ3(G) from S3 gives 33 / 70 / 139 / 212 iterations = T + 3 on all 4
  (n 610 / 610 / 610 / 730, 1 fallback each). The outputs are correct: regions = harness Zielonka and the strategies pass verify.
  For contrast, CANDIDATE N5′-xi runs 12 / 12 / 12 / 15 iterations on these games (correct), consistent with box 190's IDEAL-XI T ≤ H.
- Not run: fa (all starts) — its MAXN 28 limits it to d ≤ 14. So T is for the stored start only.
- Pins: experiments/red/r216/pins.sha1. Tool sha1: ideal.py 4a6a168a, lemck.py b2a5901d, memb.py 436522b2, box150 check.py 019de0f7.

## 2. Consequences (certified lower bounds, stored start; READING beyond that)
- T^R(20) ≥ 136 (H5) and T^R(24) ≥ 209 (H6). These are new table entries; the earlier certified d 15 bound was 114.
- READING: the per-level cap F(l) = 2^(l+2) − 2 is attained on 6 consecutive levels at d 24. Whether that continues with S(h) ≈ 4h
  levels per capped level (exponential T^R, hence an exponential N5 family on Γ3 under P-N5-REACH) is not decided by two points.
