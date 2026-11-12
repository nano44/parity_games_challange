# R231 item 0: BLKX23_n48 re-run on L-RED's own engine (L-RED successor 65; written 2026-11-12T04:15Z by date -u)
Target: L-NEW 70 BOX 206 Addendum B (claude/l-new d3fc2d21), DEAD BLOCK-DESC witness BLKX23_n48, and the Lead's 04:05Z correction
(relayed from L-NEW 70): «two low bits (34, 46) count through the race; four high bits (30, 31, 32, 33) arrive one at a time (one-hot);
multi-high sets only at the end, through one nesting edge (41 → 42 → 33)».
Engine: experiments/red/r221q/own.py (L-RED 54, independent IDEAL-CYC Howard run; no L-NEW code). Only the genome JSON is read.
Labels: DATA (unit, set, scope) / READING. Frozen: experiments/red/r231/inst/BLKX23_n48.json, sha1 3275991e86fb590e35d3129ae7e9de36f4b85a0f
(= L-NEW's inst/SHA1SUMS line).

## Result: AGREEMENT on every number; the correction is right
- DATA (r231/blk231.py, out/blk231_BLKX23.out; unit: Howard steps / distinct values per mover; set: BLKX23_n48; scope: all movers):
  T 28; k 1 (min FVS of Ξ(G) over all options, brute force); levels {0, 1} (two levels); b 6; F_0(6) 22; D_mov 23 (movers 2, 3, 22, 23,
  24, 27, 28, 29, 46, 47); max Dtop 23 (same movers). Mover 47 (= 46 = 29) top-block sequence, deduplicated, bit i = e-position 91 + i:
  0, 1, …, 11, 16, 17, 18, 19, 33, 34, 36, 40, 41, 42, 43 — identical to L-NEW's. So 23 > 22: DEAD BLOCK-DESC reproduces.
- Cross-check of the engine against L-NEW's Addendum A/B numbers: K1L10_n48 T 31, max Dtop 14; K1L7_n48 T 37, max Dtop 18 (both as L-NEW).
- Bit map (blkmap231.py, out/blkmap231_BLKX23.out): bits 0, 1 = options of movers 46, 34 (low); bits 2, 3, 4, 5 = movers 30, 31, 32, 33
  (high). Both B2 (mover 30) and B3 (mover 31) have W-target 41.
- High part of mover 47's set (bits 2-5), deduplicated: {}, {B2}, {B3}, {B4}, {B5}, {B5, B2}, {B5, B3}: one-hot through the first five
  values; the two 2-bit values are the last ones (states 24-28 of 28).
- Plays (blkplay231.py, out/blkplay231_BLKX23.out; unit: segments of mover 47's play from a high-bit e-vertex to the next high-bit
  e-vertex, all 29 states): exactly two segments, B2 → x41 x42 x33 → B5 (state 24) and B3 → x41 x42 x33 → B5 (states 25-28). So every
  multi-high set uses the one nesting path 41 → 42 → 33. The low bits nest through 45 → 44 → 34 (B0 before B1) at every 2-low state.
- READING: Dtop = 4·(number of high values) − (missing low completions) = 4·7 − 5 = 23. The high values are one-hot plus one nesting
  edge, so this witness's Dtop grows linearly in the number of high bits, not as 2^b. DEAD BLOCK-DESC stands as a small-b fact
  (F_0(b) is not the bound); it is no evidence of a counter. The open question is L-NEW 70's carry-wired family CW(n) (next item).
