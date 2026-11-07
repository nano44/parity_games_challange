# L-COMP box 30: parallel tower search (Lead 07:12Z) -- a seventh capped level from H6, and the least d for six. Label: DATA / CANDIDATE
L-COMP successor 10, 2026-11-07. Recipe = L-LOWER 4's (docs/lower/L4-tower.md §5 on claude/l-lower; «+4 TOP-ADD levels, then an LV climb»).
## Tools (copies in l-lower/, from claude/l-lower at the commit in l-lower/COMMIT)
- rclimb30.c = L-LOWER's rclimb.c with ONE change: the value type is a 192-bit signed integer instead of __int128 (rclimb's values are
  sums of ±2^rank; at d = 32 the 128 ranks reach 2^127, which overflows __int128). Check: on H6 lifted to d 26 (no overflow possible for
  the original), 20,000 proposals with the same seed give byte-identical best files and logs from the original and from rclimb30.
- lift.py (L-LOWER's l3/lift.py: k TOP-ADD levels), trunc.py (mine: drop the top k levels; removed Xi-targets -> X; ranks renumbered).
- lane30.sh: restart-proof lane: units of 2·10^7 proposals (ANNEAL 0.15 -> 0 within a unit) from the lane's best; seed = lane base + unit;
  HIT = F(l) = 2^(l+2) − 2 for l = 0..h (exact doubling over F(0) = 2) -> out/<lane>_HIT_u<u>.txt + out/HITS.txt. relaunch30.sh relaunches.
## Lanes (seed bases chosen to differ from L-LOWER's runs: 300000+, 310000+, 320000+)
| lane | start | d | score | hit = |
| --- | --- | --- | --- | --- |
| A_d28 | H6_d24_F126 + 4 TOP-ADD | 28 | LV 6, GUARD 5 (levels 1-5 kept exact, maximise F(6)) | F(0..6) = 2, 6, ..., 254 |
| B_d32 | H6 + 8 TOP-ADD | 32 | LV 6, GUARD 5 | F(0..6) = 2, ..., 254 |
| C_d23 | H6 minus its top level (trunc.py) | 23 | LV 5, GUARD 5 | F(0..5) = 2, ..., 126 (six capped levels at d 23) |
- A hit is a CANDIDATE until replayed by an independent simulator (box27/sim.py for T; F re-counted).
- 07:4xZ lane C restarted: removing the TOP level of H6 collapses its run (T 3; 10 units at d 23 never left the GUARD penalty; kept as
  out/C_d23_toptrunc.log). remlevel.py removes ONE level j (levels above shift down by one): for j = 6..23 the start profiles are in out/remlevel_profiles.txt
  ; j = 21 keeps T 101, F 0 2 6 14 30 62 47 … (levels 1-5 exact doubling over F(0) = 0), so lane C restarts from
  H6 minus level 21 (out/seed_d23_rm21.txt), seed base 320100.
- First units (DATA): A_d28 and B_d32 keep levels 0-5 exact (2 … 126) and reach F(6) = 160 after one unit each (target 254).
