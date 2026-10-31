# R157: k-SOURCE's degree factor IS realised in data, at one level, and it then hits |F|. rcl_K24 (n 321): an Even selector h2 with 24 options, option j riding (through a fixed even marker) on the j-th reactor of obs_K12_m24, re-climbs ALL 24 options in every wave. It switches 289 = 24 · 12 + 1 times in ONE 324-transition W-run, while the root pivot h changes W only 12 times: switches(h2) = K · WCH(h) + 1 (rcl_K8: 97 = 8 · 12 + 1; rcl_K16: 193). No gates are needed: each option has its own source, and the reactors rise in order within each wave. But the selector is passive (no in-edges), so its count is capped by |F|. At K = 24 it is 0.89 |F|. A second level cannot compound unless the selector feeds back and lengthens the W-run. That is the exact obstruction, with this instance: switches ≤ |F| (trivial), |F| unchanged by passive gadgets, and lengthening |F| needs source events (P-N5-SRC). No super-quadratic W-run
L-RED successor 36 (Opus 5.5; D1/D18), un-parked by the Lead 06:43Z: «ONE more box, R157, the attack half of your resume point: Build the
two-level counter whose upper selector re-climbs ≥ 2 options per source rise … Score switches(h2) against WCH(u_b), and max XICH / |F|
against n. Even one level that realises the (deg + 1) factor in data would be new. If the matching Ξ supply cannot be built, give the exact
obstruction (which premise of which lemma blocks it) with the instance.» Written 2026-10-31 from 06:45Z (date -u).
- Labels: PROVED (lane) / DATA / READING. Not a TARGET.md claim. G-N5-TIME stays OPEN.
- Sources opened:
  - red/span/mkrw.py docstring (reactor chain: «r_j: a_j → r_(j−1) (r_0 = h), or b_j → h′. An h-rise runs down the chain one reactor per
    step; an h′-rise flips all reactors back at once»);
  - docs/red/R156-twosource.md (k-SOURCE);
  - red/xcn/instances/xich obs_K12_m24 (traced, see §1).

## 1. The supply (DATA, obs_K12_m24, n5b SPEC, one W-run 0-324)
- Pivot h (vertex 3) changes W at 1, 28, 55, …, 298 (12 times, period 27). Pivot h′ (vertex 4) changes W at 26, 53, …, 323 (12 times).
  W(h) and W(h′) swap order 24 times.
- Reactor r_j (j = 1 … 24) changes W 24 times: at 1 + j + 27e (the h-wave reaches it) and at 27 + 27e (h′ flips all reactors back).
  Within each wave the reactors rise strictly in order r_1, r_2, …, r_24.
- So the reactors are K = 24 distinct sources that rise once each, in order, per root rise. This is exactly the per-epoch supply that
  GATE-r^dyn / k-SOURCE say a re-climb needs. Each reactor is itself a 2-option two-source selector (a_j via h, b_j via h′), and its 24
  switches meet k-SOURCE's 1 · (1 + 12) + 1 · (1 + 12) = 26 up to 2.

## 2. The re-climbing selector (DATA)
- wlev/mksrc2.py with EVEN=1 (even dynamic markers 4x + 2; priorities rescaled p → 4p + (p mod 2)): Even h2 (priority 0) with options
  d_j (Odd, priority 0) → md_j → r_j. md_j has an even priority of rescaled level x_j = 560 + 2j. It is above every a-marker (511-557),
  so a later reactor's extra odd a-markers lose to md_j, and below the pivot ladder (G, Gp ≥ 658), so the root level dominates.
- So option j is the W-best (and Ξ-best) exactly from the moment r_j rises in the current wave. The first option rides above the last
  option of the previous wave, because the root level dominates.
- wlev/src2trace.py:
  | instance | n | K | switches(h2) in the W-run | K · WCH(h) + 1 | k-SOURCE bound Σ (1 + WCH(r_j)) | descents without source rise | \|F\| |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | rcl_K8 | 289 | 8 | 97 | 97 | 200 | 0 | 324 |
  | rcl_K16 (not pinned) | 305 | 16 | 193 | 193 | 400 | 0 | 324 |
  | rcl_K24 | 321 | 24 | 289 | 289 | 600 | 0 | 324 |
- Landings: d8, d1, d2, …, d8, d1, … (rcl_K8): one full re-climb per wave. Every re-entry at a lower option is paid by a rise of its
  source, as k-SOURCE (iv) requires.
- xeng: state sequences identical on rcl_K8 and rcl_K24. Oink 8fbf0a7: OK on both.
- So per root rise h2 re-climbs K options. W(h2) changes about K · WCH(h) times. This is the (deg + 1)-type factor of R156's composition
  corollary, measured against the root.

## 3. The exact obstruction to compounding (PROVED, lane, trivial, and READING)
- (P1) For every vertex v and W-run F: switches_F(v), WCH_F(v) and XICH_F(v) are ≤ |F|. One change per transition at most.
- (P2) h2 and its options have no in-edges from the engine, so the original run is unchanged: |F| = 324 with and without the selector
  (iterations 324, one W-run, 0 τ-changes in every instance). A passive selector cannot lengthen F.
- So the measured factor saturates: rcl_K24 reaches 289 = 0.89 |F|. A second level riding on K′ copies of h2 can add at most
  |F| − (its own start) switches. The compounding the brief asks for must LENGTHEN F.
- Lengthening F means feeding the selector's rises back into the engine. By P-N5-SRC (Corollary SRC-COUNT, line L-5), |F| ≤ E^S_F +
  (E^S_F + 1)(n − 1 + m_C). So more transitions need more SOURCE EVENTS (Ξ-changes at Odd deviators D or at W-cycle nodes C), and the
  feedback must pass through an Odd deviator whose Ξ the selector raises.
- That is the premise that blocks: the selector here is Even and off every play. Its W-changes are not source events, and they reach no
  source. This is R148's dichotomy again: event-rich engines have short blocks.
- Which premise of which lemma: k-SOURCE's bound is in terms of WCH(u_b) ≤ |F|. It cannot exceed |F| whatever the degree. The open quantity
  is |F| itself, i.e. HXS-POLY / XI-CH-POLY (R95, P-N5-SRC).

## 4. Pins (experiments/red/check.sh «R157»)
- wlev/pins.sha1 (adds rcl_K8, rcl_K24); src2trace on rcl_K8 (97 switches; ~1 min); xeng and Oink on rcl_K8 and rcl_K24.

## Addendum 1 (2026-10-31, date -u in the commit): the CEIL-ACC score (Lead 07:04Z, from l-si 6ca54248 docs/si/N5-SBF-box53.md §8, Lemma CEIL-ACC; NOT opened, Lead summary only)
- L-SI's experiments/si/sb53/ceilpot.py @ l-si 6ca54248, run unchanged from a git archive (PYTHONPATH new/box21:harness:new:si):
  | game | n | W-run transitions | AUP | ANDN | ADN | AINC | AMAX |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | obs_K12_m24 (base) | 272 | 324 | 1 | 1 | 323 | 57,812 | 74,528 |
  | rcl_K8 | 289 | 324 | 1 | 1 | 323 | 66,397 | 84,099 |
  | rcl_K24 | 321 | 324 | 1 | 1 | 323 | 84,125 | 103,683 |
- A falls at 323 of 324 transitions in all three. The re-climbing selector does not change A's behaviour (AUP and ANDN stay 1). It only
  raises A's scale (AMAX grows with the added vertices).
- So R157's degree factor lives entirely inside the A-descent. It is consistent with CEIL-ACC's |F| ≤ (1 + AUP)·n(n + 2) + ANDN and gives
  no evidence of AUP or ANDN growth. A multiplying counter would need A to rise or stay flat often. Neither happens in any build here.

## DONE / FINDINGS / NEEDS
- DONE: this note; wlev/mksrc2.py EVEN=1; wlev/instances/rcl_K8, rcl_K24; check.sh «R157». SHA: see the commit.
- FINDINGS:
  - DATA (new): one level realises k-SOURCE's degree factor. rcl_K24: switches(h2) = 24 · WCH(h) + 1 = 289 in one W-run, re-climbing all
    24 options per root rise (xeng, Oink OK).
  - Obstruction to compounding: passive selectors are capped by |F| (0.89 |F| at K = 24). Lengthening F needs source events
    (SRC-COUNT), and the selector's W-changes are not source events.
- NEEDS: none.
