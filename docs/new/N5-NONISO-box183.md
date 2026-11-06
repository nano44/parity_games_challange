# Box 183 N5-NONISO: where W-ONLY uses ISO (the Ξ side only), the non-ISO frame lemma (≤ 3 frozen segments separated by ≤ 2 switch steps), and the obstruction — non-ISO 𝓛^R_3 runs move the upper ladder MORE often than any ISO E-run with the same number of key flips (now1_d3_5: 5 > T_0(2) = 4 with no key flip; dbl_d3_F6: 8 > T_2(2) = 7); so FLIP-ADD on the ISO frame T_k cannot reach T^R
L-NEW successor 56, 2026-11-06 (from 13:41Z by date -u; see the commits). Lead brief BOX 183 (13:43Z; Lead reading L49): (1) find
exactly where R110's W-ONLY uses ISO; (2) prove a non-ISO version or give the obstruction with an instance. Premises: R110 (W-ONLY, the
definitions of 𝓛^R_d, ISO, b_0, the c-step and T_k(m)); P-IDEAL-ALIGN F0 (signed, R113 pending) for «each level-0 mover moves at most
once». Labels: PROVED (lane, unrefereed) / DATA / CONJECTURE / DEAD / READING. Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Answer
- (1) Where ISO is used. R110 W-ONLY reads: «on 𝓦_d every step of a run equals, on the levels ≥ 1, the c-step with c = b_0 of the new
  state; under ISO the A-sets of the levels ≥ 1 do not depend on the options of 0 and 1, and freezing 0 and 1 at options q gives an
  IDEAL genome whose run from any state with q at 0 and 1 is the iterated b_0(q)-step; hence every run of an ISO genome of 𝓛^R_d (d ≥ 2)
  has T ≤ T_2(d − 1) + 2». The first clause is ISO-free: it is the key side, and level-0 options enter the keys of level ≥ 1 only through
  b_0. ISO enters only in the second clause, on the Ξ side. Under ISO no option has Ξ-target 0 or 1, so no chain of a level-≥1 option
  passes through 0 or 1, and A-sets above level 0 are functions of the upper state alone. That is what makes «the c-step of u» a map
  on upper states and lets T_k(m) be defined over ISO genomes with an external bit sequence. The Lead's guess is right: the gap is
  exactly the Ξ-targets 0 and 1 of upper options.
- (2a) PROVED (lane) Lemma NONISO-FRAME. On 𝓛^R_d with any acyclic Ξ-graph, every run is ≤ 3 FROZEN SEGMENTS separated by ≤ 2 SWITCH
  steps. A switch step is a step moving 0 or 1; there are at most 2, since each level-0 mover moves at most once (F0). In a segment,
  (s(0), s(1)) = q is constant and the run coincides, state for state, with the run of the frozen genome G_q (0 and 1 restricted to their
  options q). A switch step can do two things to the levels ≥ 1, and only these: flip b_0, which is R110's c-change, and raise the
  values of the upper options whose current chains pass through the mover that moved (R105 MONO + ENC). Hence T ≤ U + 2, where U :=
  #{steps changing a level-≥1 mover} is bounded by the largest upper count over frozen non-ISO frames with ≤ 2 switches.
  - Proof. Within a segment, at every step 0 and 1 keep q. Their A-sets in G are irrelevant to the other movers' choices, which depend on
    A-sets computed from the old state, and on keys under the new state that agree with G_q's, because q is unchanged. G_q gives 0 and 1
    singleton A-sets and every other mover the same A-set (same old state, same chains) and the same keys. So the steps agree. The
    switch count is F0. Every step either
    changes a level-≥1 mover (counted in U) or moves only level-0 movers (a switch step, ≤ 2). ∎
- (2b) DEAD (instances; premise the exact values T_0(2) = 4, T_1(2) = 5, T_2(2) = 7, SAT, L-COMP 27 / box 160 table, lane DATA, not landed):
  the ISO-frame inequality «U ≤ T_C(d − 1), with C the number of b_0 changes along the run» is FALSE for non-ISO genomes. Here U is the
  count in T_k: steps changing the levels ≥ 1. For ISO genomes it holds by W-ONLY: the levels ≥ 1 follow a c-step sequence with C changes.
  - now1_d3_5 (experiments/new/box160/out/now1_d3_5.json, sha1 1454119a…) from start 001110: T 5, U 5, C 0, one switch step (mover 0
    at step 1, b_0 unchanged): U = 5 > T_0(2) = 4. Mechanism: options (2, 0), (4, 0), (5, 0) have Ξ-target 0. The move of 0 at step 1
    raises their values; mover 2 becomes Ξ-unhappy and moves at step 2, and the chain 3, 5, 4 follows. The extra step is a Ξ-renewal
    through a level-0 mover, invisible to the key bit.
  - one_d3_6 (box160/out/one_d3_6.json, sha1 9f8b7c7c…) from start 110110: U 6, C 1 > T_1(2) = 5.
  - dbl_d3_F6 (box156/ext/dbl_d3_F6.json, sha1 ef787bf4…) from start 111101: T 8, U 8, C 2, two switch steps (mover 1 at step 4, mover 0 at step 6): U = 8 > T_2(2) =
    7. Every one of the 8 steps changes the upper ladder, more than any ISO E-run with 2 external flips. This is the T^R(3) = 8 value.
  - Sanity (ISO genomes, same tool): the corpus maxima are exactly U = 4, 5, 7 at C = 0, 1, 2 (nol0_d3_4, iso1_d3_5, iso_d3_7) = T_0, T_1,
    T_2(2): ISO runs reach the frame values and never exceed them.
- Consequence (READING, the Lead's question). FLIP-ADD stated on the ISO frame (T_k(m) ≤ T^R(m) + O(m)) can at best bound T^R_ISO(d).
  It cannot reach T^R(d) through W-ONLY, because the non-ISO coupling feeds the upper ladder through a second channel (Ξ-renewal
  through 0, 1) that T_k does not model. The right frame is T^N_k(m): the largest upper count over 𝓛^R_(m+1) genomes, any Ξ, with ≤ k
  switch steps, each moving 0 or 1 once (key bit and Ξ inputs together). NONISO-FRAME gives T^R(d) ≤ T^N_2(d − 1) + 2 (PROVED, lane;
  T^N_2 is a supremum, finite at each d). DATA: T^N_0(2) ≥ 5, T^N_1(2) ≥ 6, T^N_2(2) ≥ 8, against T_k(2) = 4, 5, 7. The gain is +1 at
  each k here; at d 4 the corpus has U 9 at C 0 (NOW_1_d4_t10), U 13 at C 2 (max_d4_L13), against T_0(3) ≥ 8 and T_2(3) ≥ 12 (lower
  bounds only, no exact values: not a kill at d 4).
- DATA (frozen frames without switches, box183/frozen.py climbs): relays alone, i.e. upper options pointing to frozen 0 and 1, gave no
  gain over ISO frames in my climbs (d 3: max 4 both = T_0(2)). The climbs are weak, though (d 4 frozen: 5; full d 3 ISO: 3), so this
  is not evidence of equality. The gain in (2b) comes from the SWITCH (the value rise at the moment 0 or 1 moves), not from static
  relays.
- CONJECTURE N-FLIP-ADD (the non-ISO replacement, lane): T^N_2(m) ≤ T^R(m) + O(m). With NONISO-FRAME it would give T^R(d) ≤ T^R(d − 1)
  + O(d), so T^R(d) = O(d²). DATA: m = 2: T^N_2(2) ≥ 8 = T^R(2) + 4. Kill: a family with T^N_2(m) − T^R(m) superlinear.

## 1. Files (experiments/new/box183/)
- upper.py (U, C, Z per run over every start for d ≤ 4; log/upper.txt: corpus + L-RED R212 keep); frozen.py (frozen-frame and full-ladder
  climbs, ISO vs non-ISO; log/fz_*, log/full_*; out/*.json).
- The non-ISO instances are existing in-tree files (box156, box160); no new genome JSON under box150-181 (risecheck corpus rule).

## 2. Next (Lead decides)
- Exact T^N_k(2) by SAT (L-COMP's T_k encoding with level-0 movers as real movers, each allowed one move): settles the +1 per k.
- Proof side: bound the extra Ξ-renewals of one switch. A switch raises the values of the options whose chains pass through 0 or 1;
  by MOVE-RISE and RISE-EQUIV (P-IDEAL-RISE) each renewed mover moves to a strictly better option. The question is whether one switch can
  renew more than O(1) movers per level.
