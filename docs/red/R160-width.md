# R160: depth × width does not multiply in anything built or climbed. Inner width > 1 while an outer level is held EXISTS (w_re3_1, n 32: two level-3 stretches of widths 9 and 6 inside ONE level-2 stretch, level 1 held; xeng, Oink OK), so there is no «width ≤ 1» lemma. But the two inner waves run over DISJOINT vertex sets, so they add. Climbing for REUSE (the same Even vertex switching in two sibling level-3 stretches) finds reuse only through mass multi-vertex switches, with narrow stretches (w_ru_2: reuse 14, widths 6 and 2). Every climbed W-run is ≤ 25 transitions at n 32. Re-armed waves are known only at depth 2 (fbg / obs: R2 = 32 reused reactors). Also: h^V = 40 on hd_H40, so CONJECTURE HV3 is dead
L-RED successor 37 (Opus 5.5; D1/D18). Lead 2026-10-31 10:11Z: «GO R160 = depth × width … Make each release of gate i+1 re-arm gate i's wave from scratch … If width at an inner level cannot exceed 1 while an outer level is held, that is the width lemma we need: state the exact obstruction … with the instance.» Lead 10:58Z: run box 107's hier2.py on hd_H (h^V); box 110 RESET-RED / resets2.py. Written 2026-10-31 from 11:00Z (date -u).
- Labels: DATA / READING. Not a TARGET.md claim. G-N5-TIME stays OPEN.
- Sources opened:
  - l-new 23770680: experiments/new/box107/hier2.py and box110/resets2.py (run unchanged from a git archive);
  - box107/hier.py (re-implemented as hd/hierx.py);
  - NOT opened: docs/new/N5-WIDTH-box110.md and L-SI box 56 (Lead summaries only).

## 1. Tools (experiments/red/hd/)
- hierx.py re-implements hier.py's level hierarchy independently, on n5b SPEC traces. It agrees with hier.py on hit_b6a_1 (18/19/1),
  hd_H10 (1 per level) and fbg_K4_m6_m24 (depth 2). It adds:
  - per-level stretch widths (transitions paid at level d inside one parent stretch);
  - REUSE R_d: Even vertices that switch inside ≥ 2 distinct sibling level-d stretches of one parent stretch, i.e. a re-armed inner wave.
- wclimb.py: hill-climb (retarget / add / drop an edge, change a priority, change a start choice), with three objectives:
  - the widest level-3 stretch;
  - REARM=1: the second-widest level-3 stretch;
  - REARM=2: R_3 first.

## 2. DATA
| instance | n | WT | depth | NLEV | widest stretch per level | R2 / R3 | longest W-run | E^S | longest source-free block | xeng / Oink |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hit_b6a_1 (l-new seed) | 32 | 38 | 3 | 18 / 19 / 1 | 9 / 19 / 1 | 0 / 0 | 23 | 11 | 10 | OK |
| w_hit_3 (climb: widest L3) | 32 | 20 | 3 | 4 / 2 / 14 | 3 / 2 / 14 | 0 / 0 | 19 | 5 | 9 | OK |
| w_re3_1 (climb: second L3 stretch) | 32 | 25 | 3 | 7 / 3 / 15 | 4 / 3 / 9 (L3 stretches 9, 6) | 0 / 0 | 21 | 8 | 4 | OK |
| w_ru_2 (climb: reuse) | 32 | 15 | 3 | 5 / 2 / 8 | 5 / 2 / 6 (L3 stretches 6, 2) | 0 / 14 | 15 | 7 | 5 | OK |
| fbg_K4_m6_m24 (R158) | 178 | 139 | 2 | 16 / 123 | 16 / 30 (four L2 stretches of 30) | 32 / – | 139 | – | – | OK |
| hd_H40 (R159) | 122 | 40 | 40 | 1 each | 1 each | 0 | 40 | 40 | 0 | OK |

- Climbs: 4 seeds per objective, ≤ 8,000 steps each, n 32, seeds hit_b6a_1, hd_H10 and the climbed instances.
  - Widest L3 stretch: 14 / 11 / 8 / 4, always with NLEV3 = widest, i.e. one wide stretch.
  - Second-widest L3 stretch: 6 / 6 / 4 / 0.
  - Reuse: R3 14 / 14 / 12 / 10, with second-widest stretch ≤ 3.
- w_re3_1 in detail (level-3 stretches inside the level-2 stretch 7–24, level 1 held):
  - k 8–13: 7, 24, 26, then 16, 28, 27, 17, 14, one per step;
  - k 15–23: 13, 3, 20, 10, 1, 21, 5, 31, 12, one per step.
  - Disjoint vertex sets: two different waves, not one re-armed wave.
- w_ru_2: the 14 reused vertices switch in multi-vertex transitions (k 0–5: 5–13 switches each). Its stretches are narrow.
- L-NEW tools on R-instances (l-new 23770680, unchanged):
  - hier2.py: hd_H10 DEPTHV 10, hd_H40 DEPTHV 40 (NOV 0); hit_b6a_1 and w_re3_1 DEPTHV 2; fbg DEPTHV 2. So h^V grows linearly on hd_H,
    and CONJECTURE HV3 (h^V ≤ 3) is dead there.
  - resets2.py:
    - hd_H10 / hd_H40: TD 0, RT 0 (depth without resets, as box 110 says);
    - hit_b6a_1: TD 540, RT 34, TDRANK 224, RTRANK 33;
    - w_re3_1: TD 466, RT 25, TDRANK 227, RTRANK 25;
    - fbg_K4_m6_m24: TD 19,157, RT 139 = |F|, TDRANK 9,012, RTRANK 139.

## 3. READING (what blocks the product, as far as the data go)
- No «width ≤ 1 while held» lemma exists: w_re3_1 has widths 9 and 6 under one held level-2 stretch.
- A product needs REUSE: the same wave vertices re-switching in each sibling stretch, i.e. a re-armed inner wave (box 110: trade-down
  switches re-enabled by fresh Ξ-overtakes).
  - At depth 2 this exists and is where the quadratic families come from: in obs / fbg the reactors are re-armed by the alternating
    roots h / hp.
  - At depth 3 neither the designs (R158: one shared line binds once per phase; R159: depth without resets) nor the climbs found a wave
    that is both wide and reused. Width and reuse appear separately.
- This is DATA plus a reading, not a lemma. The candidate statement for the proof side: inside one level-2 stretch, the Even vertices
  that switch in two sibling level-3 stretches make o(width) switches per stretch. No proof is offered, and none is known to me.
- The re-arm mechanism at depth 2 (two alternating roots) needs, one level up, alternating roots whose own alternation is re-armed.
  That is R156/R157's two-level leapfrog. The obstruction found there (passive selectors capped by |F|; R158 (A): a shared line carries
  the new root) is where the next attempt has to start.

## 4. Pins (experiments/red/check.sh «R160»)
- hd/pins.sha1 (adds w_hit_3, w_re3_1, w_ru_2); xeng and Oink on w_re3_1 and w_ru_2; hierx stretch widths of w_re3_1.

## DONE / FINDINGS / NEEDS
- DONE: this note; hd/hierx.py (stretch widths, REUSE), hd/wclimb.py, hd/instances w_*, pins, check.sh «R160». SHA: see the commit.
- FINDINGS:
  - DATA: inner width > 1 under a held outer level exists (w_re3_1: L3 stretches 9 and 6 under one L2 stretch), so there is no
    width-1 lemma. But the waves are disjoint. Reuse appears only with narrow stretches (w_ru_2: R3 14, widths 6 and 2). Every climbed
    W-run is ≤ 25 at n 32.
  - DATA: h^V = 40 on hd_H40 (hier2.py), so HV3 is dead; hd_H has 0 resets.
  - READING: the missing piece is a re-armed wave at depth 3. Re-arming is known only at depth 2 (alternating roots).
- NEEDS: none.
