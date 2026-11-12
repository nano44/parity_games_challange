# L-COMP BOX 42 (successor 18; Lead 11:54Z 2026-11-12): fixed-family Deep_3 test on the C6G8 line. All DATA.
Nothing here is a TARGET.md claim. CONJECTURE DEEP3 stays OPEN (this family is consistent with it); G-N5-TIME stays OPEN.

## Item 1: the family (trace -> growth rule), clone42.py
- Trace (box41 per-gate census, scope all SCCs, one N5′-xi run from S3 on Γ3): on C6G8_n54 -> its growth to 281 -> the D300b best
  (sha1 79f3cd11), the deep internal flips (depth 4-5) sit at a few steps (t = 6, 7, 9, 12); each deep change fans out to the internal
  gates of several level-1 movers. Mover 10 carries the most (gate (10, 0): 3 deep flips); its only in-edge is option (18, 0) (Ξ-target 10).
- Growth rule CL(k): the D300b best plus k clones of mover 10 (copies of its 5 options, gate / β rank placed just after the original's)
  plus one copy of its in-edge option retargeted to each clone: +7 to N + M per clone. CL(0) = the D300b best byte for byte (sha1 79f3cd11).
  Built at k = 0, 8, 16, 30, 45, 90, 131: N + M = 285, 341, 397, 495, 600, 915, 1202 (inst/, SHA1SUMS). No search, so equal effort per size.

## Item 2: measurements (two engines on every point; out/meas42_mine.out = box41/deep41.py on own34; out/meas42_cross.out = L-SI cross100.py
on L-RED how3_232, CMAX 3)
| k | N + M | T3 | Deep_3 (Σ_C, internal, after t0, depth > 3) | per-gate max | dmaxInt | whole-run deep (mine / cross100) | dmax (both) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 285 | 14 | 10 | 3 | 5 | 10 / 10 | 5 |
| 8 | 341 | 14 | 42 | 3 | 5 | 42 / 42 | 5 |
| 16 | 397 | 14 | 74 | 3 | 5 | 74 / 74 | 5 |
| 30 | 495 | 14 | 130 | 3 | 5 | 130 / 130 | 5 |
| 45 | 600 | 14 | 190 | 3 | 5 | 190 / 190 | 5 |
| 90 | 915 | 14 | 370 | 3 | 5 | 370 / 370 | 5 |
| 131 | 1202 | 14 | 534 | 3 | 5 | 534 / 534 | 5 |
T3 equal on both engines at every k; unm 0 on both. cross100 has no internal / after-t0 split and no per-gate deep count; on every CL(k)
my whole-run deep equals my Deep_3, so cross100's equal whole-run deep confirms the Deep_3 column; the per-gate max (3) is mine only.

## Item 3: fit (fit42.py, out/fit42.out), within the family only
- Deep_3 = 10 + 4k EXACTLY = (4/7)(N + M) − 152.9: **polynomial, exponent 1 (linear)**, max residual 1e-13 on 7 sizes over 285-1202.
  (A log-log slope of 1.94 over k >= 8 is the affine offset, not curvature.)
- Per-gate maximum of deep internal flips: **3 at every size** (constant). dmax at internal gates: **5 at every size**: dmax does NOT grow
  with size in this family (the quantity L-RED 66's one-gate climb targets). T3 = 14 at every size.
- READING: each clone is one more gate on the same deep changes; the deep flips pile up in parallel at the same few steps (T3 constant),
  so Deep_3 here is bounded by (#internal gates) x (a constant per gate). Nothing faster than polynomial; nothing sent as an alert.
  BOX 41's cross-family slope 2.45 was a cross-family artefact for this line.
