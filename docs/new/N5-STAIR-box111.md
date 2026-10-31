# Box 111 N5-STAIR: the staircase as a potential; resets reduce to DESCENTS (L-NEW successor 41; Lead 10:58Z, 2026-10-31)
Started 10:58Z, written ~11:4xZ (date -u). Labels: PROVED (lane); CONJECTURE; DATA; DEAD; READING.
- Setting as in boxes 107-110: F is a W-run, every CS coordinate is an oriented 0/1 bit (unary length), and position 0 is the most
  significant.
- For a vertex v, q_1(v), q_2(v), … are the first-difference positions of its successive W-changes on F.
- L-SI 36 box 56 (cecbf177a, «push pending» per the Lead) was NOT on claude/l-si at my fetch (10:58Z: tip bd4d0472, box 55). Not read;
  the staircase below is my own reading of obs. Coordination: L-SI works from the FS side, this note from the bit side.

## 0. Answer
- The staircase IS a potential. A vertex's W-change positions climb in significance between DESCENTS (a change strictly below
  the previous one).
- Ψ := Σ_v (index of v's last change position) falls at every descent-free W-changing transition and has range O(n²).
- So |F| ≤ T1_F + n(3n + 2) + (3n + 2)·DESC_F (Theorem STAIR, PROVED).
- DATA: the long families are almost descent-free.
  - sbq2_K8_m16 (quadratic, R145 / L-SI box 54) has 0 descents.
  - hd_H40 (depth 40, R159) has 0.
  - obs_K12_m24 has 12, all at its clock selector 247, one per round.
  - Corpus: 14,755 descents against 66,857 vertex W-changes, max 3.14·n in a game.
- CONJECTURE DESC-LIN (descents per W-run ≤ c·n) would give |F| = T1 + O(n²). The «counted set» is the descents, i.e. the carries.
- DEAD: «descents happen at source events» (obs: 12 of 12 source-free).

## 1. PROVED (lane)
- Lemma ASC-RUN. For every vertex v, WCH_F(v) ≤ (3n + 1)(1 + DESC_F(v)).
  - Proof. Between two descents the positions q_j strictly decrease (become more significant), and there are 3n + 1 positions. □
- Theorem STAIR. Let Ψ_k := Σ_v ψ_k(v), where ψ_k(v) is the position of v's last change before state k (3n + 1 if none yet).
  Then WCT_F ≤ n(3n + 2) + (3n + 2)·DESC_F, and so |F| ≤ T1_F + n(3n + 2) + (3n + 2)·DESC_F.
  Conversely DESC_F ≤ Σ_v WCH_F(v) ≤ n·WCT_F, so this is an EQUIVALENCE: WRUN-POLY ⟺ (T1 + DESC)-POLY.
  - Proof.
    - At a W-changing transition, every changed vertex either ascends (ψ falls by ≥ 1) or descends (ψ rises by ≤ 3n + 1).
    - A transition with no descent lowers Ψ by ≥ 1. Ψ ∈ [0, n(3n + 1)] and Ψ_0 = n(3n + 1).
    - So the descent-free W-changing transitions number ≤ n(3n + 1) + (3n + 1)·DESC_F. Each other W-changing transition contains a
      descent. □
- Corollary RESET-STAIR (relating to box 110). TD_F ≤ (3n + 1)·n·WCT_F ≤ poly·(n + DESC_F), so TD-POLY ⟸ DESC-POLY.
  - Resets that are NOT followed by a descent cost nothing: they belong to an ascending staircase. That is obs's selector 247
    resetting its previous target's bit at every inner switch.
  - Only the resets that a later descent re-fixes, the carries, can multiply.
- Lemma DESC-COPY (from box 110 COPY). If v did not switch at k or at its previous change, its descent at k is a descent of its
  successor at k. So descents, like resets, are born at switched vertices or at re-pointings.
  - Proof. COPY preserves first-difference positions (up to the unary-length shift, which preserves order). □

## 2. The obs staircase (DATA; tdtrace.py)
- Selector 247 makes 289 trade-down switches = 12 rounds × 24 + 1.
- Inside a round it walks its targets 248 → 249 → … → 271. Each switch improves at the new target's own bit (q = u249, u250, …,
  strictly MORE significant each time) and resets the previous one. That is the ascending staircase: no descent.
- At a round boundary (271 → 248, q = u10) the next inner switch (q = u249) is a DESCENT. That gives 12 descents in all, which are
  obs's whole DESC.
- This is the bit-side view of L-SI's staircase: «strictly descending staircase at the targets» is, on the selector, a strictly
  ASCENDING sequence of change positions.
- Re-growth inside one level is free (Ψ pays it). Only the round restart, a carry, needs an outer event.
- The descents are source-free here (DSRC_NOW 0, DSRC_SINCE 0). The outer event that restarts a round is a change at the high digit
  u10, not an R97 source event.

## 3. DATA (desc.py; corpus = box 53's 1,132 games; desc_sbcg.txt, desc_alt.txt, desc_pins.txt)
| instance | n | WT | Σ_v WCH | DESC | max WCH(v) | max DESC(v) | max ascending run |
| --- | --- | --- | --- | --- | --- | --- | --- |
| hd_H40 | 122 | 40 | 2,420 | 0 | 40 | 0 | 40 |
| sbq2_K8_m16 | 261 | 152 | 1,967 | 0 | 16 | 0 | 16 |
| obs_K12_m24 | 272 | 324 | 2,976 | 12 | 301 | 12 | 25 |
| hit_b6a_1 | 32 | 38 | 113 | 24 | 4 | 1 | 3 |
| x31_rx48 | 48 | 47 | 247 | 80 | 5 | 3 | 3 |
| runfam_K40 | 79 | 171 | 378 | 253 | 7 | 4 | 3 |

- Corpus:
  - WT 14,028, Σ WCH 66,857, DESC 14,755;
  - DSRC_NOW 7,911 (54 % of descents at a source event), DSRC_SINCE 9,907 (67 %);
  - ASC-RUN VIOL 0; 809 games have no descent;
  - max DESC/n = 3.14 (runfam_K40, 248 with the default start); nep92_n40 has 3.03.
- READING.
  - In every family with |F| ≫ n, the W-changes are long ascending staircases at many vertices (sbq2: max 16 per vertex, 1,967 in
    all, 0 descents).
  - Descents concentrate where |F| is small relative to n: runfam's many short staircases.

## 4. CONJECTURES and what L-RED would need
- CONJECTURE DESC-LIN: DESC_F ≤ c·n for every W-run (DATA: max 3.14·n). With STAIR this gives WCT_F = O(n²), and with T1 (INS face)
  |F| = T1_F + O(n²).
- Weaker CONJECTURE DESC-POLY: DESC_F is polynomial. STAIR makes it equivalent to WRUN-POLY modulo T1.
- DEAD: «every descent is at (or after) a source event since v's previous change» (obs_K12_m24: 12 descents, 0 at source events).
  So the outer events that pay carries are not R97 source events. On obs they are changes at a higher digit of the SAME selector
  (u10). That is a self-carry, possibly paid by the R95 / R97 outer level (the clock vertex's fresh ticks; L-NEW box 99
  FRESH-ROOT). Not proved.
- For L-RED (R160): a multiplying W-run must have DESC_F super-linear, and by STAIR at least |F| / (3n + 2) − n.
  - So a 3-level product w_1·w_2·w_3 needs w_1·w_2 descents: carries nested two deep at one selector, or spread over many.
  - The measurable target: a W-run with DESC_F ≫ n (desc.py).
- Why no proof (READING). A descent at v is a re-fix of a lower bit after a higher change. By DESC-COPY it is born at a switch. The
  switch needs a fresh Ξ-overtake (box 108), and nothing bounds how often the Ξ side re-arms one selector below a fixed higher digit.
  This is the box 110 §3 question, now restricted to carries.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/new/box111/:
  - tdtrace.py (trade-down roots), desc.py (descents, ASC-RUN, source flags), rundesc.sh;
  - desc_pins.txt, desc_sbcg.txt, desc_alt.txt;
  - pins in experiments/new/check.sh «box 111 STAIR».
- FINDINGS:
  - PROVED (lane): ASC-RUN, Theorem STAIR (|F| ≤ T1 + n(3n + 2) + (3n + 2)·DESC; an equivalence), RESET-STAIR (resets not re-fixed by a
    descent are free), DESC-COPY.
  - DATA: sbq2 and hd_H40 have 0 descents; obs has 12 (one per round, at selector 247); corpus DESC 14,755, max 3.14·n.
  - DEAD: descents charged to R97 source events (obs).
  - CONJECTURE: DESC-LIN (⇒ |F| = T1 + O(n²)).
- NEEDS: Lead: route DESC-LIN to L-RED R160 (target: a W-run with DESC ≫ n, measured by desc.py). L-SI box 56 not yet readable; I
  will read it when it lands.
