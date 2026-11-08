# Box 84: HUB PAIR «MIRROR», milestone 1 (L-SI successor 44; Lead GO 01:54Z 2026-11-08, design (c) of box83-ladder.md §0)
Written 2026-11-08T02:26Z (date -u). Labels: PROVED (lane) / CONJECTURE / DATA (unit, set, scope, counter) / DEAD (instance) / READING.
Nothing here is a TARGET.md claim. G-N5-TIME stays OPEN. N5′-xi stays a CANDIDATE (D1).
Tools: experiments/si/box84/ (pair84.py builder; gen83.py is a byte copy of box 83's DSL; check84.sh, wired). Measured with box 83's
meas83 / lock83 and the pinned box 81 / 82 tools (census81, anal82, real81, xchk81).

## 0. Answer (milestone 1)
- Design MIRROR (§1). It breaks LOCK-UP's hypothesis «every option of B other than S has its Ξ-target in Y ∪ {X} ∪ Z ∪ {u}».
  - SET_l's continuation goes into the mirror M_(l+1); B_l's UP and lanes go into the real B_(l+1).
  - M_(l+1)'s play never passes B_(l+1), so the alternatives reach e's the continuation does not have. lock83 (which takes X = B_(l+1)) finds HYP in 0 states, as it must: the
    continuation never reaches B_(l+1).
- Result (DATA, §2), with mirror UP into the next mirror (MUP = 1):
  - Bit 1 now resets TWICE inside one Λ-interval (box 83: once).
  - At h = 3 the hub's e-set walks through 8 = 2^3 values, all lex-increasing.
  - But growth stays LINEAR: hubH 4 / 8 / 11 / 15 and R 4 / 9 / 13 / 17 for h = 2 / 3 / 4 / 5. RF(1) = 5 at every h ≥ 3.
  - Max adoptions per bit per Λ-interval 3 and max resets 2 (h = 3, 4, 5).
- NOT a counter. The obstruction (READING from the traces, not proved):
  - Bit l's SET condition is {e_l} ∪ m_(l+1) ▷ r_(l+1), where r_(l+1) := E(B_(l+1)) and m_(l+1) := E(M_(l+1)) are the real and mirror
    e-sets one level up.
  - That condition reads only the bits ABOVE l. So a carry starts ONE ripple wave down the bits: each B_l re-sets as soon as the
    mirror catches up, without waiting for the lower bits to count.
  - B_l's re-set does reset and re-set B_(l−1) (2 toggles), but B_l's reset triggers nothing below. Doubling would need both.
- The deeper reason: by R218 PLAY-BLIND, B_l's value can react to a lower bit only if B_l's play passes a mover that switches. The
  MIRROR plays only go up, so a bit is blind to the lower counter. Making a bit wait for the lower bits needs a route from B_l DOWN into
  them. That is [F09]'s s-hub (H1), which leaks with access (LEAK-ARCH) and was DEAD without access in R218 §6 (t4).
  So the next question is a downward route without H1's leak. OPEN.

## 1. The build (pair84.py; R104 IDEAL format)
- Real bits B_1..B_h (B_l at level l); mirrors M_2..M_h (M_l at level l); top T = B_(h+1) = M_(h+1); dummies D_l as in box 83.
- Every bit and mirror x of level l has:
  - UP (β → B_(l+1); with MUP = 1, a mirror's UP goes to M_(l+1));
  - an RS2 delay lane of length L_l (B) or LM_l (M), with exits → B_(l+1);
  - SET (W-target w at level l − 1 with one option β → M_(l+1); Ξ-target x; even β).
- The mirror's e lies above the real e at the same level (gate key (9, 1, l) > (9, 0, l)).
- H (level 0): β → B_1. Start: every bit on UP; lanes on EXIT.
- Intended mechanism: after a carry into l + 1, r_(l+1) holds e_(l+1) while m_(l+1) lags, so B_l's alternatives win and B_l resets.
  Once M_(l+1) sets, its mirror e outranks e_(l+1), so B_l re-sets.

| instance | args (h; L; LM; MUP) | sha1 (.json) |
| --- | --- | --- |
| HP2_mup | 2; 1,4; 8; 1 | b7964d561d92c316261d145b52bce66026ea00af |
| HP3_mup | 3; 1,3,6; 6,12; 1 | 3766033c28302e00db5427d74b7f7a06d8f5adee |
| HP3_mup0 | 3; 1,3,6; 6,12; 0 | e99c9ef6ea31da8638f85cce01daf3ab463c87f1 |
| HP4_mup | 4; 1,3,9,19; 7,10,30; 1 | d7ebbea0c3f21ce76b4304756387f6c067090737 |
| HP5_mup | 5; 2,4,12,17,22; 5,17,20,34; 1 | 39bce9f76d5ad06830d225c66e3835cde55fb9ef |
(sha1 of the working-tree files at the commit that adds them; re-take with `git show <that commit>:path | sha1sum`.)

## 2. DATA (outputs in experiments/si/box84/out/)
Unit: one Howard run per frozen instance (IDEAL-CYC, stored start). Set: the 5 instances above. Scope: box81/ref idealcyc. Counters as
in box83-ladder.md §3 (RF, hubH, SumD = Σ_v D^tot_E(v), bits, premature resets); lock83: adoptions and resets per bit per Λ-interval.

| instance | N | n | T | R | C | RF (levels 0..h) | hubH | SumD | adoptions / resets per bit (max) | N5′-xi on Γ3 (iters / fb / T3) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| HP2_mup | 40 | 253 | 11 | 4 | 0 | 0 3 2 | 4 | 291 | 2 / 1 | 14 / 1 / 11 |
| HP3_mup | 77 | 497 | 17 | 9 | 0 | 0 5 4 2 | 8 | 710 | 3 / 2 | 20 / 1 / 17 |
| HP3_mup0 | 77 | 497 | 15 | 6 | 0 | 0 3 4 2 | 5 | 685 | 2 / 1 | not run |
| HP4_mup | 186 | 1,245 | 37 | 13 | 0 | 0 5 7 4 2 | 11 | 1,991 | 3 / 2 | 40 / 1 / 37 |
| HP5_mup | 301 | 2,035 | 43 | 17 | 0 | 0 5 7 7 4 2 | 15 | 4,349 | 3 / 2 | not run |
- Premature resets 0 everywhere. N5′-xi = T + 3 with one fallback and mover phase = Howard (real81) on HP2-HP4. xchk81: game, states,
  values and labels SAME on HP2-HP4.
- Hub walk at h = 3 (HP3_mup, meas83 -v), 8 values: ∅ < {e_B1} < {e_B1, e_M2} < {e_B3} < {e_B1, e_B3} < {e_B1, e_M3} < {e_B2, e_M3}
  < {e_B1, e_M2, e_M3}. At h = 4 there are 11 values; the first lane phase sets several bits at once (0001 → 0111), so the low part is
  skipped.
- MUP = 0 (a mirror's UP goes to the real B_(l+1)): an unset mirror then shows r_(l+2)'s real e's, so a carry two levels up never
  resets B_l. h = 3: hubH 5, RF(1) 3, the box 83 picture.
- Lane scan (scratch, 25 random lane-length draws per h, seeded): best hubH 8 / 11 / 15 and R 9 / 13 / 17 at h = 3 / 4 / 5; RF(1) = 5 in
  every best run. So the linear growth is not a tuning artefact of the frozen choices.
- Trace of HP5_mup (meas83 bits, steps 24-43): the carry into bit 5 at t 24 gives one wave, B4 ↓ (25); B3 ↓↑ (26, 27); B2 ↓↑ (28, 29);
  B1 ↓↑ (30, 31). M5 sets at t 36 and gives a second wave, B4 ↑ (37), B3 ↓↑, B2 ↓↑, B1 ↓↑. Each bit toggles twice per wave, but the
  waves do not nest.

## 2b. Where MIRROR sits against L-RED's Lemma PRIV-FLIP (R222 §3, claude/l-red 3d9e788d; Lead 02:30Z)
- PRIV-FLIP (PROVED lane, L-RED): on a Λ-interval with Λ(B) ∈ {K1, K2}, if no play from SET's W-target or from B's other gates passes
  B (PRIV), then #changes of [σ(B) = S] ≤ 1 + (D_E,I(w) − 1) + Σ_(o ≠ S) (D_E,I(g_o) − 1). With HUB-ASC-G / UP-B this is polynomial
  for bounded U(G).
- Which of the three ways out MIRROR takes:
  - PRIV holds: every play from B_l's options goes up and never returns to B_l.
  - Λ is constant: C = 0 in every run.
  - U(G) grows with h. Every UP, carry and lane exit is an upward Ξ-edge, so U(G) = Θ(N); census81 gives U 20 / 39 / 94 / 152 for
    HP2 / HP3 / HP4 / HP5.
  So PRIV-FLIP does not forbid MIRROR. But it explains the DATA quantitatively.
- B_1's flips are at most 1 + Σ(D_E − 1) over w_1 (whose play is M_2's) and B_1's other gates (whose plays are B_2's).
  - A counter needs B_1 to flip about 2^h times. So E(M_2) or E(B_2) must take about 2^(h−1) values: the same hub-pair question one
    level up.
  - MIRROR's hub e-set heights grow linearly (maxD 4 / 8 / 11 / 15), so B_1's flips stay bounded (RF(1) = 5).
- FINDING (READING with PRIV-FLIP): a PRIV SET counter is a recursion on e-set heights, D(l) ≳ 2·D(l + 1) for the hubs that a level-l
  bit reads. Nothing in MIRROR makes a level-(l + 1) hub's height double. The way out is not U(G) alone.
  - Under PRIV, one needs higher hubs that themselves count (heights 2^(h−l)).
  - Without PRIV, a play from the bit's own options must return to the bit (the R218 §4 branch (c) cycle).

## 3. Next (proposal)
- A bit must WAIT for the lower counter before re-setting: its SET (or its lane) must be beaten until the bits below are full. By
  PLAY-BLIND that needs a route from B_l down into the lower bits, without H1's access leak. Candidate: the downward route enters only
  the lower MIRRORS (which lag), never a real bit's gate. LEAK-ARCH's H1 is about the real hub route, so this may avoid its proof; R218
  §4's branch (c) cycle must be checked first. Not built.
