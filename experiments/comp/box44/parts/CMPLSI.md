- Against L-SI's replay (claude/l-si 925577fe experiments/si/box104/out/replay209_level.out, replay209_plat.out: L-NEW's counter code on L-RED
  65's HOW3 engine, L-SI's 26 frozen genomes; out/cmp44_lsi925577fe.out, one line per genome, all 26 listed): 26 of 26 EQUAL in (T3, number
  of Φ values, stalls, plateaus, longest plateau, tail); my must-0 sum 0 and L-SI's 9 + 9 counters sum 0 on all 26; largest T3 199
  (MW32_2). My rows come from my sets records (5), corpus (11) and mine (10: C98_* 7, Ku_4/8/16, Kprev_8 — box40/inst; 59 distinct genomes
  in «mine», must-0 sum 0; MWR4/8/16_2 occur in both box39/inst and box40/inst with equal sha1 and run once).
- The cross (L-NEW's own counter code, claude/l-new 311bbf81 box208/level208.py --hist (16 counters) and box209/plat209.py --hist (9
  counters), run unchanged with python3 -I on the history of MY builder + engine; run44c.sh; compared by cross44.py, whole line character for
  character after «plat3 hist » := «plat3 »; out/cross44.out): records 25, corpus 53, dead 3 — 0 differing lines against BOTH of L-NEW's
  engines (its n5v rows level3_* / plat3_* and its rows on L-RED 65's HOW3 engine own3_*), level and plat; mine 59 runs, of which the 26 of
  L-SI's replay (925577fe) compare: 0 differing lines, level and plat. L-NEW's 16 + 9 counters sum 0 on all 140 of my runs.
