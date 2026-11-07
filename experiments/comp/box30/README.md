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
## Lead 09:32Z changes
- A_d28 STOPPED (flat at F(6) = 160 for 6 units, seeds 300000-300005). B_d32 kept (F(6) = 190 after 4 units, levels 0-5 exact).
- NEW lane D_d32, seeds 330000+: L-LOWER 4's warm start rec/G7_best_d28.txt (claude/l-lower af9a73d8, experiments/lower/l4/rec/;
  copy l-lower/G7_best_d28.txt, sha1 b995fff2…) + 4 TOP-ADD (lift.py) -> out/seed_D_d32.txt. MEASURED before climbing, by rclimb30 and by
  replay30.py: T 270, F 2 6 14 30 62 126 222 158 126 80 32 28 20 8 8 8 8 7 7 6 5 2 2 1 2 1 2 2 (lifted: the same, + four 0s on the
  inert top levels).
- C_d23: one more hour, stopped at 10:35Z by stopC.sh; S(h) DATA = out/remlevel_profiles.txt (unit: the start profile T, F(0..22) per
  removed level j; set: the 18 single-level removals j = 6..23 of H6_d24_F126).
- replay30.py: independent replay of a climb genome with MY simulator box27/sim.py (R104 rules) and F(l) counted from R104 key orders;
  = rclimb30 on H6 (T 209), G7 (T 270) and B's best (T 257, F(6) 190). A HIT is reported only with this replay.
## Lead 10:23Z: targeted score for lane D (L-LOWER 5, claude/l-lower 13b2b4d8, docs/lower/L5-rule.md §4, experiments/lower/l5/slack.py)
- rclimb30.c now has env SLACKH = H: after the GUARD check (levels 1..5 exact over F(0) = 2) the score is −1000·v + F(LV), v = the
  violations of slack.py's counter at level j = H − 2 with need = H − j (PULSE < need, GAP < need; windows cut at level j−1's flips),
  ported to C (slack_viol); output files carry «slack_viol v good91 g» (g = (9,1)-type windows with PULSE, GAP ≥ need). Without SLACKH
  the binary's behaviour is unchanged (identical output on H6).
- Port check (H = 7), port = slack.py at every level j = 1..5: G7_best_d28 0 0 0 0 30; B_d32 best 0 0 0 0 48; D_d32 best (F(6) score)
  0 0 0 0 30. NOTE: slack.py itself gives 30 level-5 violations on G7_best (15 pulse + 14 gap in (9,1) windows + 1 pulse in the first
  window), not the 31 quoted in the 10:23Z message.
- Choice (mine, stated): the primary score minimises ALL level-5 violations (not only the (9,1)-type count): on G7 they coincide except
  the first window, and a move that only shifts violations to another window type earns nothing.
- Lane D_d32 restarted 10:3xZ from out/seed_D_d32.txt (G7 + 4 TOP-ADD; TOP-ADD adds levels above, so level indices are unchanged: port gives
  the same 30 there), seeds 340000+. Its earlier F(6)-score files: out/D_d32_fsix*.
