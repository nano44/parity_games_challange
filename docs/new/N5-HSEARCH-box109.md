# Box 109 N5-HSEARCH: hill-climbing for W-digit depth (L-NEW successor 41; Lead 09:00Z / 09:22Z, 2026-10-31)
Started 09:00Z (date -u). Labels: PROVED (lane); CONJECTURE; DATA; DEAD. Box choice reported to the Lead at 09:00Z:
«next (b′) search, because (a)'s dominance half is already CARRIER (h ≤ #ranks) and HDEPTH is my own conjecture, rated false».
Lead 09:22Z split the work: L-NEW SEARCHES, L-RED DESIGNS (R159). Setting as in boxes 107-108.

## 1. DEAD: HDEPTH (h^W ≤ 2), my own box 107 conjecture
- Instance: experiments/new/box109/out/hit_b6a_1.pg (n 32) with hit_b6a_1.start (n5x default start).
  - Found after ~3 min of climb.py from n5-exhaustive/instances/b6_xl2_n32.pg (RNG seed 3, iteration 11,681).
- N5 runs 43 iterations with 2 fallbacks. The W-run spans transitions 20..42 (23 transitions) with h^W = 3 (NLEV 18 / 19 / 1).
  T1 0, T2 18, T3 12, T4 8. XDEC = WDEC = WOX = 0, so box 107's W-MON and O-ARENA hold here too.
- Faithfulness:
  - n5b (L-COMP's independent N5, si/root/n5bcmp.py) is identical state by state (43 iterations, 2 fallbacks).
  - Oink 8fbf0a7 --zlk and --tl are both "solution verified", and both equal N5's regions at its stop (pinwin.py).
- Carrier chain (trace3.py; box 108 CARRIER + GATE), carrier v = 5:
  - level 3: u9 (priority 17) fixed at k = 20, the first transition of the run;
  - level 2: u8 (priority 22) fixed at k = 36 via the new arena edge (5, 9), at a source event;
  - level 1: u18 (priority 29) fixed at k = 40 via the new edge (6, 0), at a source event.
  - The other carriers are 12 and 24. These are box 108 §4's three gates, released bottom-up at source events.
- Pinned in experiments/new/check.sh «box 109 HSEARCH».

## 2. A refinement: length repeats are degenerate depth (PROVED, lane) — h^U
- DATA first. climb2.py found h^W = 4 already at n 16: out/hit_n16_1.pg (13 iterations; W-run of 10 transitions; n5b identical;
  Oink zlk / tl verified, equal regions).
  - Its four pending digits are ALL the length coordinate. W's path length steps toward its final value, one level per step: the
    length-repeat exception of box 108 CARRIER.
- Unary length.
  - Replace CS's last coordinate (the signed length sl) by the threshold bits [sl ≥ j], j = −n..n. This map preserves the lex order,
    so SANDWICH, FROZEN and HIER-RED hold with R = n(2n + 3).
  - A move of sl toward the reference now raises lcp, so length progress is always paid at the current level. CARRIER's positions
    become strictly increasing with no exception.
- So h^U := the depth in this encoding counts only RANK-digit nesting, with h^U ≤ h^W. The bound HIER-RED(U) reads
  |F| ≤ T1_F + (n(2n + 3) + 1)^(h^U_F).
- hit_n16_1 has h^U = 1 (degenerate). hit_b6a_1 and the other n 32 / n 40 depth-3 games keep h^U = 3 (genuine).

## 3. DATA: climbing (climb2.py = h^W, climb4.py = h^U, climb3.py = joint h^V; n fixed per climber; 4-5 cores, 09:00Z-10:10Z; stopped at 10:10Z on the Lead's word)
- Score: (depth, transitions paid at the deepest level, W-run transitions). Moves: redirect / add / remove an edge, swap two
  priorities, flip an owner. Sideways moves are accepted.
- Max depth reached (best files in out/; all re-scored with box 107 hier2.py):

| n | max h^W | its h^U | max h^V | best W-run length | climbers (log) |
| --- | --- | --- | --- | --- | --- |
| 16 | 4 (length repeats only) | 2 (u16) | 2 (v16) | 10-20 | n16, u16, v16 |
| 24 | 1 | not run | 3 (cw11_n24 seed; not raised by 1 h of climbing) | 26 | v24 |
| 32 | 3 | 3 | 3 (v32, from best_u32) | 38-61 | b6a, d4a, d4b, u32, v32 |
| 40 | 3 | 3 | 2 | 49 | b6b, d4d |
| 48 | 2 | 2 | 2 | 49-70 | x31a, x31b, d4c, u48 |
| 64 | 2 | 2 | 1-2 | 31-44 | n64, u64 |

- Hold lengths (trace3.py; number of transitions in B_1 / B_2 / B_3 of the deepest chain):
  - hit_b6a_1: 23 / 20 / 1;
  - best_d4a: 24 / 20 / 19;
  - best_d4b: 33 / 30 / 10;
  - best_d4d: 26 / 22 / 17.
  So each level holds for 10-30 transitions, and the width per stretch is small (NLEV3 ≤ 20).
- Joint depth h^V:
  - It is 2 on every W-deep game found (all h^W = 3 / 4 instances).
  - It reached 3 only from the corpus seed cw11_n24 (h^W = 1) and on v32.
  - It never reached 4.
- Climbing never raised depth with n. Larger n climbs more slowly, and the n 48 / 64 climbers stayed at 2. This is a property of
  the search, not of N5: L-RED R159 (claude/l-red 599f9571, docs/red/R159-depth.md, as relayed by the Lead 10:12Z, not opened by
  me) DESIGNS hd_H with n = 3H + 2 and h^W = H (hd_H40: depth 40 at n 122).

## 4. CONJECTURES (with the evidence) and the obstruction I see
- HDEPTH is DEAD (§1), and depth is unbounded by design (R159 hd_H, h^W = H, |F| = H). HIER-RED's bound (R + 1)^h is
  therefore vacuous there: depth costs nothing in length. The climb data agree: deep games are short (|F| ≤ 61).
- No depth obstruction is claimed. My earlier hope «h^V ≤ 3 ⇒ |F| = O(n^6)» rests only on the search above (max h^V = 3, never 4).
  R159's hd_H has not been measured for h^V; if L-RED runs box 107 hier2.py on hd_H, that settles it. I label it CONJECTURE HV3,
  weak, and expect hd_H to kill it as well.
- READING (agreeing with the Lead / L-RED): the quantity that matters is WIDTH, i.e. how many times a level-i digit is re-fixed
  inside one hold of level i − 1. The climbers' widths are ≤ 20 per stretch. Box 110 takes it.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/new/box109/:
  - climb.py, climb2.py, climb3.py (joint V), climb4.py (unary length), trace3.py;
  - out/ (hit_*, best_*, log_*, seed_n16.pg; hit_b6a_1.start, hit_n16_1.start);
  - pins in experiments/new/check.sh «box 109 HSEARCH».
  - Interim commits 04696022 (pushed) and 3778dbcd. Final SHA: see the commit.
- FINDINGS:
  - DEAD: HDEPTH (hit_b6a_1, n 32, h^W = 3, faithful).
  - PROVED (lane): the unary-length refinement h^U (length repeats are degenerate depth; hit_n16_1 has h^W = 4 but h^U = 1).
  - DATA: per-n maxima above; each level holds 10-30 transitions; h^V ≤ 3 on everything searched.
  - CONJECTURE HV3: weak, expected false.
- NEEDS: L-RED (via Lead): measure h^U and h^V on hd_H (box 107 hier2.py; climb4.py's cs for h^U).
