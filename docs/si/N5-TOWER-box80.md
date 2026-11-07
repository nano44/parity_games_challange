# N5-TOWER box 80: pulse nesting, autonomous zones, and the stretch obstruction to extending capped towers
L-SI successor 42 (Opus 5.5), D14 / D18 / D20; Lead brief BOX 80 (2026-11-07 ~07:05Z): the proof side of the tower question.
Written 2026-11-07 from 07:25Z (date -u: see the commits). Labels: PROVED (lane, unrefereed) / DEAD (instance) / CONJECTURE /
DATA / READING. Not a TARGET.md claim; no statement bounds T polynomially; G-N5-TIME stays OPEN. The towers H5, H6 stay CANDIDATE.

## 0. Premises, notation
- LANDED (trunk docs/RESULTS.md): R104 definition of the IDEAL model (step rule: A-sets under the old state, keys level by level
  under the new state); R105 ENC, LOCAL; R110 definition of 𝓛^R_d; R113 ALIGN and its notation c_l(s), γ_l(j), F(l).
- Lane (this lane, unrefereed; packet P-IDEAL-DBL, draft at 2c396f6f, §2): DBL-EQ (a), (b): if level j is doubling (F(j) = 2F(j − 1) +
  2) then the flip steps of the pair j are exactly the steps that move 2j or 2j + 1, no step moves both, and each of them moves exactly
  once in every j-window. (L-LOWER 4's DOUBLE-EQ′ (E3), (E4), docs/lower/L4-tower.md §3 at claude/l-lower f55b98e3, is the same
  statement from ALIGN only; either serves.)
- Notation as in P-IDEAL-DBL §0: j-window = maximal set of consecutive steps [a, e] with no j-b-step (flip step of the pair j − 1) in
  [a + 1, e]. For a doubling level j and a j-window W, u_1(W) < u_2(W) are the two steps of W that move a member of the pair j, and
  PULSE(W) := u_2(W) − u_1(W) (the length of the pulse of the key bit b_j: by DBL-EQ the order of the pair j flips at u_1 and back at
  u_2). P_j(run) := min over j-windows of PULSE. Levels 0, …, h − 1 CAPPED: F(l) = 2^(l+2) − 2 for l < h (so F(0) = 2 and levels 1, …,
  h − 1 doubling). SLACK_j := P_j − (h − j) for a run with exactly h capped levels.

## 1. Lemma PULSE-NEST (PROVED, lane; DBL-EQ (a), (b))
- Hypotheses: G ∈ 𝓛^R_d, any run, j ≥ 1, k ≥ 0, j + k ≤ d − 1, levels j, j + 1, …, j + k all doubling.
- Claim: every j-window W has PULSE(W) ≥ k + 1, hence length ≥ k + 2.
- Proof. Induction on k. k = 0: u_1 < u_2 (DBL-EQ (b): two moves; (a): at distinct steps). k ≥ 1: by DBL-EQ (a) at level j the flip
  steps of the pair j are exactly its move steps, so the (j + 1)-b-steps are exactly the steps u_1(W), u_2(W) over all j-windows W. Hence
  W′ := [u_1(W), u_2(W) − 1] is a (j + 1)-window (it starts at a (j + 1)-b-step, contains none in its interior part, and u_2(W) is the
  next one). Level j + 1 is doubling, so by DBL-EQ (b), (a) both members of the pair j + 1 move in W′, at steps u_1(W′) < u_2(W′) ≤ u_2(W)
  − 1, with u_1(W′) ≥ u_1(W). So PULSE(W) ≥ PULSE(W′) + 1, and by the induction hypothesis (levels j + 1, …, j + k doubling) PULSE(W′) ≥
  k. A window contains both steps, so its length is ≥ PULSE + 1. ∎
- Corollary CAP-PULSE. If levels 0, …, h − 1 are capped, then P_j ≥ h − j for 1 ≤ j ≤ h − 1 (k = h − 1 − j).
- Note: k = 1 is L-LOWER 4's LATE-PREF (i) (u_2 ≥ u_1 + 2); PULSE-NEST iterates it. The bound is attained (DATA §5: PN_T).

## 2. Lemma ZONE (PROVED, lane; R104 definition, R105 ENC and LOCAL)
- Hypotheses: G′ an IDEAL genome (any degree, any width), Ξ-acyclic; Z a set of its movers closed under the W-targets and the
  Ξ-targets of all options of its members (X allowed); G′|Z the genome with movers Z and the same options, W-targets, Ξ-targets, ENC
  integers ε, gates; s′ the run of G′ from s′_0, z the run of G′|Z from s′_0|Z, T′, T_Z their lengths.
- Claim: T′ ≥ T_Z and s′_t|Z = z_(min(t, T_Z)) for every t ≤ T′. In particular, if G is a genome containing Z as a closed set with the
  same data (e.g. G = G′ minus some movers outside Z), the runs of G and G′ from starts that agree on Z agree on Z, step for step,
  until the shorter of the Z-run ends, and then the Z-part stays constant.
- Proof. By ENC/LOCAL the value of an option of x ∈ Z is ε along its chain, which lies in Z ∪ {X} (Ξ-closure); so the A-set of x under
  s is a function of s|Z, the same in G′ and G′|Z. The key of an option is the lexicographic tuple of gates along its W-chain, which lies
  in Z (W-closure); so the key-least choice of x under the new state is a function of the new state on Z. Hence the new option of every x
  ∈ Z at each step is the same function f_Z(s|Z) in G′ and in G′|Z, and s′_t|Z = f_Z^t(s′_0|Z) as long as these differ. If f_Z(z) = z,
  the Z-part is constant from then on. A step of G′|Z that changes its state changes s′, so G′ does not stop earlier: T′ ≥ T_Z. ∎

## 2b. Lemma INSERT-PASS (PROVED, lane; R104 definition, R105 ENC, R113 ALIGN)
- Construction: G ∈ 𝓛^R_d, 1 ≤ L ≤ d − 1. G^(+L) ∈ 𝓛^R_(d+1): levels ≥ L shifted up by one (every index renumbered), and a new pair (a,
  b) = (2L, 2L + 1) at level L: all four options Ξ-target X, ε of the start option +2^(r+1), of the other −2^r (new ranks), a starts on
  0 and b on 1 (split), new gates. Nobody targets a or b.
- Claim: from every start (old start + a, b on 0, 1), the run of G^(+L) restricted to the old movers equals the run of G, state for
  state, a and b never move, F_new(L) = F(L − 1), and the other F values are G's (shifted).
- Proof. a, b: by ENC their option values are the constants ε, the other option is strictly worse, so they never move (R104). Under any
  state, a's key is K(2L − 2) followed by its gate and b's is K(2L − 1) followed by its gate, so the order bit of (a, b) equals the order
  bit b_(L−1) of the pair L − 1, and its flips are those of the pair L − 1. Hence c_(L+1) under G^(+L) is c_L under G, and by ALIGN (the
  order of a pair is a function of its states, its c and its gates) every higher c and order bit agrees with G's, by induction on the
  level. A-sets agree because no old chain meets a, b (ENC). So every step agrees. ∎
- Use: a capped tower can get a level inserted directly above its top capped pair for free (same run). The inserted pair then reads
  the top pair's clock, and a climb may turn it into the new top pair. Machine check: check80.py «INSERT» (§5).

## 3. Corollary STRETCH-NEED and DEAD-RIGID (PROVED, lane; §1, §2) — the obstruction to (a) in its rigid / local form
- STRETCH-NEED. Let G ∈ 𝓛^R_d with h capped levels (any run) and 1 ≤ j ≤ h − 1 with SLACK_j = 0, i.e. some j-window has PULSE = h −
  j. Let G′ ∈ 𝓛^R_(d′) contain the closure Z_j of the pair j of G (W- and Ξ-closure) with the same data, as a closed set, from a start
  that agrees with G's on Z_j. Then G′ does not have h + 1 capped levels.
  - Proof. Z_j ⊇ the pairs 0, …, j (W-closure). By ZONE the Z_j-parts of the two runs agree, so F(0), …, F(j) and the j-windows (they are
    delimited by the flips of the pair j − 1 ⊆ Z_j) with their move steps of the pair j are the same in G′ as in G. If G′ had h + 1 capped
    levels, CAP-PULSE (with h + 1) would give PULSE ≥ h + 1 − j on every j-window. ∎
- Family form. For a sequence (G_h) where G_h has at least h capped levels, and any fixed j ≥ 1: P_j(G_h) ≥ h − j → ∞, so the pair j's
  run changes infinitely often, and (by ZONE) so does the closed set Z_j(G_h) with its start. No construction that keeps, for some j,
  the closure of the pair j and its start fixed can add more than (max SLACK_j over its runs) further capped levels.
- DEAD-RIGID (instances; machine-checked, experiments/si/box80/check80.py «SLACK»):
  - H6_d24_F126 (L-LOWER 4, claude/l-lower 10cac3d9, sha1 fb37fec9…; byte copy experiments/si/box79/inst/H6_d24_F126.json): 6 capped
    levels, SLACK_4 = 0 (15 of its 31 4-windows have PULSE 2 = 6 − 4) and SLACK_5 = 0 (all 63 5-windows have PULSE 1). Every 𝓛^R genome
    with 7 capped levels must differ from H6 on Z_4(H6) (or its start there), and must lengthen those 15 + 63 pulses. Z_4(H6) is all 48
    movers of H6 (re-entry everywhere: every Z_j of H6 and of H5 is the whole genome, DATA §5), so ZONE gives no smaller fixed core.
  - H5_d20_F62 (claude/l-lower c45cf2f3, sha1 2204079d…): SLACK_4 = 0 (16 of 31 4-windows have PULSE 1). So H5 → H6 had to change the
    run of the pair 4: the «global» H5 → H6 diff (L-LOWER 4, diffg.py) is forced in this sense, not an accident of the climb.
- What this says about question (a). An extension lemma «h → h + 1 capped levels with O(1) more levels, interface preserved» cannot
  keep any closed core below a fixed level fixed: its interface must contain a STRETCH: every pair j with SLACK_j = 0 must get longer
  pulses. In the best case (every pair at zero slack, as in H6 for j = 4, 5) one extension lengthens a pulse of every level j ≥ some j_0.
  The interface property that a proof needs is therefore of the form «the pulse of the pair j can be lengthened by one step by a local
  change of the delay structure feeding the second mover of the pair j» (DATA §4: in H6 these are delay lines through block movers).
  No such lemma is proved here; none is claimed.

## 4. DATA / READING: how H6 realises its pulses (delay lines, key clocks)
- Trigger lines (experiments/si/box80/delay80.py → delay80.out; for a move of x, the step v at which π(x) last became x's new option,
  and the movers of x's chains (under s_(v−1)) that moved at v; followed back while unique, stopping at a lower pair; trig80.py prints
  the raw table): in H6 the second mover of the pair 4 is mover 9 in all 31 4-windows, and its trigger is a DELAY LINE from the b-step
  (a move of the pair 3): 9 ← 12 ← 7 (PULSE 2; 13 windows, 2 more with the second link ambiguous 7/25) and 9 ← 14 ← 13 ← 6 (PULSE 3;
  10 windows, 6 more variants of length ≥ 3). Each arrow: «moves one step after, because the earlier mover is on its chain». Movers 12, 13
  (level 6) and 14 (level 7) are block movers moving 31-32 times (the pair 4's rate). In H5 the same mover 9 is triggered DIRECTLY by
  the pair 3 in 15 windows (9 ← 6, PULSE 1) and through one delay mover in 15 (9 ← 12 ← …, PULSE 2): H5 → H6 replaced the direct
  trigger by delay lines of length 2-3, which is the stretch STRETCH-NEED requires. H6's pair 3 (x2 = 6 in all 15 windows) uses
  lines 6 ← 19 ← 5 (PULSE 5, 7 windows) and longer ones through 23, 24, 25 (PULSE 6). The top pair 5: mover 10 has options targeting 11
  (its partner) and 8, and moves one step after 11 in every window (PULSE 1).
- Same pattern one level up, in the climb snapshot (§5, CANDIDATE DATA; delay80.py on out/climb_s2_snapshot.json). The old top pair
  5 (x2 = 10 in all 63 5-windows) is no longer triggered by its partner. It now uses delay lines through block movers: 10 ← 12 ← 9/11 and
  10 ← 14 ← 8 (PULSE 2), and 10 ← 21 ← 12 (PULSE 3). The pair 4 (x2 = 9) uses 9 ← 15 ← 6 (PULSE 3, 15 windows) and longer ones (PULSE
  4-5).
- READING (not to sign; candidate interface for an extension lemma): when a capped pair stops being the top pair, its second mover's
  direct trigger (the partner, one step) is replaced by a delay line of 1-2 block movers. The lines of the pairs below get one link
  longer only where their slack is 0. Seen twice (H5 → H6, H6 → snapshot); not proved, and nothing shows the block movers can be
  added O(1) per level.
- READING (BIT-CHAIN, RESULTS R115): on 𝓛^R the key bits satisfy b_l = b_(l−1) or its negation while the pair l is split and b_l =
  γ_l(k) while both members are on k, and c_l = 1 − b_(l−1). So a block mover at level L can move to a given option only when the bits
  between the highest «together» pair below L and L give the right c_L. Above a tower whose top pair is split only during its pulses,
  c_L of a block level reads the top pulses through any frozen split pairs (PASS-FREEZE): the block movers are clocked by the fastest pair.
  This is why the delay movers sit just above the top capped pair, and why lengthening a delay line needs a mover at a level with a fast
  key clock, not just one more mover anywhere.

## 5. DATA (experiments/si/box80/check80.py → check80.out; own simulators sim80.py and box76 tw.py, compared on every run)
- CORPUS (208 𝓛^R_d genomes of the frozen P-IDEAL-MOVES corpus, every start for N ≤ 10, the stored start otherwise): 63,223 runs,
  140,395 steps; XS 0 (sim80 = tw.py on every run). PULSE-NEST: 0 violations on 32 (run, level j, j-window) units with k ≥ 1; the bound
  PULSE = k + 1 attained on 30 of them (PN_T).
- EXTRA (box79/inst: RECF4_d20_F60, DBL4_d20_F30, H5_d20_F62, H6_d24_F126, stored start): 4 runs, 442 steps, XS 0; PULSE-NEST 0 on 102
  units, attained on 22.
- ZONE: 0 violations on 3,180 (random top extension by 1-3 levels, start) units over the corpus and EXTRA genomes (new movers with
  uniform Ξ-targets among all movers of smaller index or X, new ranks interleaved with the old ones, random signs, gates, starts).
  Control ZONE_NEG: re-targeting one old option to a new mover changes the old part of the run in 218 of 479 cases.
- INSERT-PASS: 0 violations on 2,037 (genome, level L ∈ 1..d − 1, start) units (corpus + EXTRA; stored start and two random starts):
  the old part of the run is unchanged, the inserted pair never moves, F_new(L) = F(L − 1), other F unchanged. Control INSERT_NEG: the
  pair split the other way round (a on 1, b on 0, still never moving; it inverts the bit) changes the old run on 1,841 of them.
- SLACK table (P_j / bound h − j / SLACK_j): H5 (h 5, T 136): j 1: 8/4/4; j 2: 7/3/4; j 3: 3/2/1; j 4: 1/1/0. H6 (h 6, T 209): j 1:
  21/5/16; j 2: 7/4/3; j 3: 5/3/2; j 4: 2/2/0; j 5: 1/1/0. RECF4 (h 4): j 1: 8/3/5; j 2: 4/2/2; j 3: 2/1/1.
- Climb snapshot (CANDIDATE DATA, not a record; experiments/si/box80/out/climb_s2_snapshot.json, sha1 2a3bde938a7a3d48c554a0aa68dc9d956de19add;
  pclimb.c seed 2, H 7, from H6 + 4 frozen top levels, d 28): T 312, F 2 6 14 30 62 126 222 223 …; levels 0-5 capped and the PULSE-NEST
  requirement for 7 capped levels already met (pair 4 pulses 3-5, pair 5 pulses 2-3), but F(6) = 222 < 254. The stretch STRETCH-NEED
  asks for is reachable while keeping six capped levels; the seventh is not reached.
- Why the snapshot stops at F(6) = 222 (experiments/si/box80/lvl6_80.py → lvl6_80.out; DATA). In 111 of the 127 6-windows each
  member of the pair 6 moves once. In the other 16 (window indices ≡ 4 mod 8) neither moves: π never reaches c there, and the next
  window then starts already on c. Each such window loses 2 flips, so F(6) = 254 − 2·16 = 222 exactly. All 16 have LENGTH 1. They are
  one-step gaps between consecutive pulses of the pair 5, at a step where the pair 4's b-step lets the next first mover of the pair 5
  move at once. PULSE-NEST's second clause (every j-window has length ≥ k + 2) forbids them for 7 capped levels. The climb's score
  counted only pulses (u_2 − u_1), not the gap windows, so it could not see this obstruction. pclimb.c now has WIN=1 (every j-window of
  length ≥ H − j + 1 for j = 1..H − 1); on the snapshot it scores exactly these 16 deficits. Climbs with WIN=1 run from the snapshot.
- Closures: every Z_j of H5 and of H6 (j = 0..6) is the whole genome (40 resp. 48 movers).

## 6. Question (b): a lower bound on the levels per capped level — what is and is not proved
- PROVED (lane, from landed + lane items): a pair of a capped level l has both Ξ-targets movers with R ≥ 2^l − 3/2 (TOWER-NEED) and P(x)
  ≥ 2^(l+1) (TOWER-NEED + PATH-RISE), so the Ξ-DAG has a path through ≥ h movers when h levels are capped (P(x) ≤ 2^(path length)). This
  gives only d ≥ h/2 + O(1): no S(h) lower bound beyond the trivial one is proved here.
- READING (not to sign): the O(1)-per-level question is stronger than N5 needs. If each extension costs q(h) levels with q a polynomial,
  then d(h) = Σ q = poly(h) and T ≥ F(h − 1) = 2^(h+1) − 2 = 2^(Ω(d^ε)), which is super-polynomial in d; under the Lead's reading that
  R104 + R117 transfer T^R(d) to N5 on Γ3(G) with polynomial size, any polynomial S(h) would make N5 super-polynomial. CAP-PULSE asks for
  Σ_j (h − j) = Θ(h²) units of pulse length in all; even one new mover per unit of stretch per extension is polynomial.
- OPEN (no conjecture added): whether one extension can lengthen all zero-slack pulses with O(1), O(h) or poly(h) new movers.
