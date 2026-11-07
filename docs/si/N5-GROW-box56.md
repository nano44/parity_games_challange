# N5-GROW (box 56): what makes a deviator's first segment re-grow. On the quadratic pins re-growth is a self-sustaining loop inside ONE level (flip → source-free settle → fresh overtake → flip), fuelled by a strictly descending staircase at the selector's targets; the conjectured width law «fuel descends between resets» (FUEL-DESC) is DEAD on nep56_n32
L-SI successor 36 (Opus 5.5; D18). Lead 2026-10-31 10:34Z: «BOX 56 = your option (a), aimed at width: what forces a deviator's first
segment to RE-GROW after a source event? … If re-growth needs a fresh Even switch whose own cause is charged to a different (outer)
level, and each outer event allows at most poly re-growths, widths add … If you find re-growth can be driven from WITHIN the same level,
i.e. self-sustaining, give the mechanism.» Written 2026-10-31 from 10:4xZ (date -u; see commit).
- Labels: PROVED (lane) / CONJECTURE / DEAD / DATA / READING. Not a TARGET.md claim. G-N5-TIME stays OPEN.
- Setting: boxes 54-55 (FS_k(o), FS-selectors, SRC-ROOT with NO-RET) and L-NEW box 108 (claude/l-new 2d791480: NEW-EDGE, OVERTAKE-W).
  H_k := S4a's arena at k. A RE-ROUTE at (o, k): FS_k(o) ≠ FS_(k+1)(o) and the first difference sits right after an Even y ∈ FS_k(o) that
  switches at k (class ESW of grow.py). A FUEL RE-ROUTE: an FS-selector switch y → z at k with k − 1 in the W-run, (y, z) ∉ H_(k−1) (a
  new arena edge) and Ξ(z) rising at k − 1 → k (by OVERTAKE-W such a rise is forced whenever the edge is new). Its KEY is the key of
  that rise: (2, 0) cycle node, (1, r) top rank r of the path-set difference, (0, 0) length.
- Sources opened: box 54, box 55 notes; claude/l-new docs/new/N5-HDEPTH-box108.md §2 (NEW-EDGE, OVERTAKE-W).

## 1. How first segments change (DATA, grow.py)
- Classes of a change FS_k(o) → FS_(k+1)(o) for o ∈ D_k ∩ D_(k+1), at the first differing position: CHOICE (σ̄(o) changed), ESW (re-route at
  an Even switch on the segment), OSW (an Odd on the segment re-chooses), ENDX (the end vertex left D or a segment vertex entered D ∪ C).
- Corpus (1,132 games, 1,692 W-runs): CHOICE 3,065, ESW 1,088, ENDX 357, OSW 0. ESW: all 1,088 at source events; 784 through new arena
  edges, every one with the target's Ξ rising one step earlier (OVERTAKE-W, 0 exceptions); 304 through old edges; before the re-route the
  transition k − 1 was a source event 610 times, source-free 176, outside the run 302.
- Quadratic pins: obs_K12_m24 ESW 529 (all new-edge, all preceded by a SOURCE-FREE transition, CHOICE 0); sbq2_K8_m16 ESW 241 (105 after
  a source-free transition, 136 right after a source event), CHOICE 112; hit_b6a_1 ESW 7, CHOICE 3.

## 2. The mechanism on obs_K12_m24: self-sustaining inside one level (DATA / READING)
- Every deviator's first segment passes the Even selector 244 (successors 245, 246; both Odd). 244 switches at k = 24, 26, 51, 53, …, 321,
  323 (24 switches, two per round of 27 transitions; |F| = 324 = 12 · 27).
- Each switch is a fuel re-route at a source event. Its trigger (OVERTAKE-W) is the rise of the new target's Ξ at the previous
  transition, and that transition is source-free: it is the last step of the settling block (R97 SRC-SETTLE, ≤ n − 1 + m_C) that the
  previous switch of 244 started.
- So the loop is: switch of 244 (source event) → source-free settling → Ξ-rise at the other target → fresh overtake → switch of 244.
  Nothing from an outer level is needed. This is the «self-sustaining» answer the Lead asked about.
- What stops it is the FUEL. Ξ(245) changes 24 times and Ξ(246) 13 times, at top ranks 222, 220, 218, …, 178 (245) and 222, 218, …,
  178 (246), plus one last change each at rank 271 at k = 323: each staircase change replaces the top odd vertex of the Odd escape path by the next lower one. The fuel keys of the re-routes
  244 → 245 are (1, 222), (1, 218), …, (1, 178), strictly descending (12 events). So the width at this level is linear because its fuel
  is a monotone staircase, not because an outer level is charged.
- Same picture on sbq2_K8_m16 (pairs (161, 162), (164, 165), (164, 166): keys (1, 227), (1, 223), …, (1, 199)) and latew_K16_m32 (pairs
  (324, 325), (324, 326): (1, 416), (1, 412), …, (1, 356)): every multi-event fuel sequence on the pins is strictly descending.

## 3. Source events by what carries them (DATA, srcfuel.py)
- Classes (first that applies): FUEL (some FS-selector switch at k is a fuel re-route), OLDE (an FS-selector switch through an old edge),
  FIRST (first transition of the W-run), CSW (an Even C-node switches), OTHER.
- Pins: obs, src2, rcl 24 = FUEL 24; sbq2 144 = FUEL 136 + OLDE 7 + FIRST 1; latew 528 = FUEL 512 + OLDE 15 + FIRST 1; hit_b6a_1 11 =
  FUEL 9 + FIRST 2. OTHER 0.
- Corpus: 4,570 = FUEL 3,862 + OLDE 6 + FIRST 686 + CSW 16 + OTHER 0.
- So a source event is, in data, a fuel re-route, an old-edge FS switch, a C-node switch, or the run's first transition. A per-pair bound
  on fuel re-routes would therefore bound E^S_F up to OLDE and CSW (via R97 SRC-COUNT).

## 4. The width laws tried (DEAD)
- FUEL-MONO (strict: per W-run and pair (y, z), the fuel keys are strictly monotone, so ≤ n + 2 fuel re-routes per pair): DEAD on
  experiments/red/so/instances/so_th_n32 (default start): pair (12, 6) is re-routed twice with the same key (1, 29). Corpus: 82 repeats,
  12 reversals. A monotone Ξ(6) can repeat a top rank only after a more significant change in between.
- CONJECTURE FUEL-DESC (consecutive fuel keys a, b of a pair: b < a, or Ξ(z) changed at a key ≥ a in between, a RESET; it would give
  ≤ (n + 2)(1 + resets) fuel re-routes per pair, i.e. «width ≤ n + 2 per outer event»): DEAD on experiments/n5-epoch/instances/nep56_n32
  (+ .start), pair (28, 2):
  - k 8 → 9: Ξ(2) rises at rank 22; k 9: 28 switches 5 → 2 (fuel key (1, 22));
  - k 11: 28 switches back 2 → 5; Ξ(2) does not change at k 9, 10, 11;
  - k 12 → 13: Ξ(2) rises at the MORE significant rank 25; k 13: 28 switches 5 → 2 again (fuel key (1, 25)), with no reset in between.
  - n5b agrees (xeng: state sequences identical); Oink zlk OK, strategies verified. Corpus: this is the only violation (DESCV 1; resets
    112, max 3 fuel re-routes per pair). Random search (fuelsearch.py; 60,000 games at n 16 and 20,000 at n 24): DESCV 0, but random W-runs
    carry almost no repeated fuel (max 1 per pair), so the search says little.
- READING. The ascending pair on nep56_n32 is the «inner climb» shape (sbq2's Odd root climbs 136, 137, … the same way): a pair can be
  re-armed by a MORE significant rise of its target with no outer reset. So the fuel of a single pair is not one-directional in general,
  and the width of a selector is not capped by n per outer event from the fuel order alone. Per pair the fuel sequence is a chain of Ξ(z)
  values; what is still open is whether that chain can be a counter (reversals that are not paid by resets). That is exactly the
  multiplication shape for L-RED: a selector y re-routed to the same target z by rises of Ξ(z) whose keys go down, up, down, … with no
  more significant change of Ξ(z) at the turns.

## 5. Tools and pins
- experiments/si/grow56/: grow.py (segment-change classes, fuel per pair, -v O traces), srcfuel.py (source-event classes, FUEL-DESC
  check), fuelsearch.py (random search, in-process), rungrow.sh, runfuel.sh; outputs grow_*.txt, fuel_*.txt, fs_out_a.txt, fs_out_b.txt.
- check.sh «box 55»'s pins are reused (si/src54/inst, si/fseg55/inst); nep56_n32 and so_th_n32 are trunk instances (n5-epoch/, red/so/).

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/si/grow56/; DEAD.md «box 56»; check.sh «box 56». SHAs: see the commit and the message to the Lead.
- FINDINGS:
  1. DATA / READING: on obs re-growth is self-sustaining inside one level. A switch of selector 244 starts a source-free settling block,
     whose last step raises the other target's Ξ, which forces the next switch (OVERTAKE-W). The loop is capped by a strictly descending
     staircase at the targets (12 fuel events per pair), not by an outer level.
  2. DATA: source events = fuel re-routes (3,862) + old-edge FS switches (6) + C-node switches (16) + first transitions (686), OTHER 0.
  3. DEAD: FUEL-MONO (so_th_n32) and FUEL-DESC (nep56_n32): a pair can be re-armed by a more significant rise of its target without a reset.
  4. READING: the width question becomes «can the fuel chain of one pair (y, z) be a counter?», which is the multiplication shape for L-RED.
- NEEDS: none from the owner.
