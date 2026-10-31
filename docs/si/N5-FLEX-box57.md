# N5-FLEX (box 57): Lemma FUEL-LEX holds, by Ξ-monotonicity alone. So the fuel re-routes of one pair (y, z) number O(n²) per «higher-digit» change of Ξ(z); pair width becomes a recursion on Ξ(z)'s more significant changes, and whether it can cycle is the open question
L-SI successor 36 (Opus 5.5; D18). Lead 2026-10-31 11:23Z: «Take ONE more short box, 57, then park … Prove the corrected form, FUEL-LEX:
"between two fuel events of pair (y, z), either the fuel key strictly descends, or Ξ(z) has risen at a strictly more significant rank" …
If it holds, state what it gives: fuel events per pair ≤ (n + 2) × (1 + more-significant Ξ(z)-changes) … whether that recursion can cycle
(z's higher digit fed back by y's own fuel). If it fails, give the instance. Corpus + nep56_n32 + obs / sbq2 / latew; same rules.»
Written 2026-10-31 from 11:2xZ (date -u; see commit).
- Labels: PROVED (lane) / DATA / READING. Not a TARGET.md claim. G-N5-TIME stays OPEN.
- Setting: box 56 (docs/si/N5-GROW-box56.md): fuel re-route of a pair (y, z) at k (an FS-selector y switches to z at k through an edge
  not in H_(k−1), k − 1 in the W-run, Ξ(z) rising at k − 1 → k); its KEY is the key of that rise, in the order (0, 0) (length) <
  (1, r) (path-set change with top rank r; larger r = more significant) < (2, 0) (cycle node). The rise transition is t := k − 1.
- Premise: [R15a] (RESULTS R15 (a), (d)): Ξ_(k+1) ⊵ Ξ_k pointwise at every N5 transition. Value order: SPEC S1 and Q1 (cycle-node
  reward first; then the top rank of the path-set difference decides; then length).

## 1. Lemma FUEL-LEX (PROVED, lane; uses only [R15a])
- Statement. Let (y, z) be a pair with consecutive fuel re-routes at k < k′ in one W-run, keys a, b, rise transitions t = k − 1 < t′ = k′ − 1.
  If b ≥ a, then one of:
  - (ASC) b > a; the rise at t′ is itself a change of Ξ(z) at a key > a;
  - (EQHI) b = a, and Ξ(z) changes at some transition u with t < u < t′ at a key > a;
  - (REP) b = a ∈ {(2, 0), (0, 0)} (a repeated cycle-node or length key).
- Proof. Only the case b = a = (1, r) needs an argument. Suppose every change of Ξ(z) at transitions u with t < u < t′ has key < (1, r).
  - Then no such change touches the cycle node or any rank ≥ r. So Ξ_(t+1)(z) and Ξ_(t′)(z) have the same cycle node and agree at
    every rank ≥ r: write β for their common bit at r.
  - The rise at t has key (1, r): Ξ_t(z) and Ξ_(t+1)(z) agree above r and differ at r. By [R15a] the new bit β is the better one for
    Even (Q1: in Ξ_(t+1)(z) iff Ω(rank r) is even).
  - The rise at t′ has key (1, r) as well: Ξ_(t′)(z), with bit β at r, and Ξ_(t′+1)(z) agree above r and differ at r, so Ξ_(t′+1)(z) has
    the other bit at r. By Q1 that makes Ξ_(t′+1)(z) ◁ Ξ_(t′)(z), against [R15a]. □
- This is the Lead's statement, with the two repeat cases made explicit. It does not use N5's dynamics beyond monotonicity.

## 2. Corollary FUEL-COUNT (PROVED, lane)
- Notation, per W-run F and pair (y, z): N := the number of fuel re-routes of (y, z); HC := the number of transitions u of F at which
  Ξ(z) changes at a key strictly greater than the key of the last fuel re-route of (y, z) before u (the «higher-digit» changes).
- Statement. N ≤ (n + 2)(1 + HC + REP), with REP ≤ (n − 1) + n(1 + HC + n − 1); so N ≤ (n + 2)(n + 1)(HC + n + 1).
- Proof.
  - Split the fuel keys into maximal strictly descending runs. Keys take at most n + 2 values, so a run has ≤ n + 2 events.
  - Each run boundary is ASC, EQHI or REP (FUEL-LEX). An ASC or EQHI boundary between fuel events with rise transitions t < t′ is charged
    to a change of Ξ(z) at a key > a in (t, t′], a higher-digit change. The windows (t, t′] of different boundaries are disjoint, so the
    charged changes are distinct. Hence #runs ≤ 1 + HC + REP.
  - REP at (2, 0): the cycle-node reward of Ξ(z) rises strictly at each such change, so ≤ n − 1 of them.
  - REP at (0, 0): consecutive length-only fuel rises with no change of key > (0, 0) between them happen inside a stretch where Ξ(z)'s
    cycle node and path set are fixed, and there the length moves monotonically through ≤ n values. Such stretches are separated by
    higher-digit or cycle-node changes, so REP at (0, 0) ≤ n(1 + HC + n − 1).
  - Add up. □
- What it gives (READING). Pair width is polynomial in n times the higher-digit changes of Ξ(z): the width of a selector y towards z is
  paid by more significant changes of its target. Pair width is therefore a RECURSION on Ξ(z)'s higher digits. It is polynomial at the
  top if the recursion has polynomial depth and does not cycle.
- Can it cycle? A cycle needs z's higher digits to be fed by y's own fuel: y's switch must lie upstream of z's value. By OLD-PLAY (box 54)
  a change of Ξ(z) needs an Even switch on z's OLD Ξ-play; so y's switch can feed z's higher digit AT THE SAME TRANSITION only if y
  lies on z's Ξ-play (indirect feedback, through switches that y's switch causes later, is not covered by this remark). Measured as YONZ
  (y on z's (σ_k, σ̄_k)-play at the fuel re-route k) in §3. When YONZ holds, y's switch to z closes a cycle through y, so z's value after
  the switch is read off a cycle containing y. That is the feedback the Lead asks about; it is not excluded by anything proved here.

## 3. DATA (srcfuel.py, LEXV = violations of FUEL-LEX, expected 0)
- Pins:
  - obs_K12_m24: LEXV 0, ASC 0, EQHI 0, REP 0 (one strictly descending run per pair, max 12); YONZ 1 of 302 fuel re-routes.
  - sbq2_K8_m16: LEXV 0, one run per pair (max 8); YONZ 1 of 258.
  - latew_K16_m32: LEXV 0, one run per pair (max 16); YONZ 1 of 1,010.
  - nep56_n32 (FUEL-DESC's kill): LEXV 0, ASC 2 (the re-arms by a more significant rise), max 2 runs per pair; YONZ 11 of 56.
  - so_th_n32 (FUEL-MONO's kill): LEXV 0, EQHI 6 (every repeat has a more significant change between), max 2 runs; YONZ 5 of 21.
- Corpus: see «Corpus» below.

## DONE / FINDINGS / NEEDS
- DONE: this note; srcfuel.py fields LEXV / ASC / EQHI / REP / MAXRUNS / YONZ / FUELEV; corpus outputs fuel_*.txt rerun; check.sh «box 57».
- FINDINGS:
  1. PROVED (lane): FUEL-LEX (non-descents of a pair's fuel keys are paid by a more significant change of Ξ(z), or are cycle-node / length
     repeats). It needs only [R15a].
  2. PROVED (lane): FUEL-COUNT: N ≤ (n + 2)(n + 1)(HC + n + 1) per pair and W-run. Pair width is a recursion on Ξ(z)'s higher digits.
  3. DATA: LEXV 0 everywhere; on the quadratic pins every pair is one descending run (HC plays no role); feedback (y on z's Ξ-play)
     is rare on the pins (1 per run) and common on small corpus games (§3).
  4. READING: the recursion can cycle only through YONZ re-routes (y upstream of z); bounding the depth of the higher-digit recursion is
     the open core, now stated per pair.
- NEEDS: none from the owner.
