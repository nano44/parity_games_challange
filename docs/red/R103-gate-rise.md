# R103: FB-LIN, the gate-rise gadget box. No kill: carries (isolated stalls) track the gate's path-set changes, and those walk the gate's top down the ranks; ISO climbs plateau at 0.33n
L-RED successor 24 (Opus 5.5; D14/D15/D18; Lead 2026-10-29 04:28Z: "NEXT box: the gate-rise gadget (R102 §5) ... a gate whose Ξ rises Θ(n)
times in one phase, each rise ending in a stall ... Make the P-changes your knob."). Written 2026-10-29 from 04:55Z (date -u).
Labels: DATA / READING / OPEN. Context: L-SI docs/si/N5-GRUN-box25.md §5 (l-si 07f19760): a gate's Ξ rises in P-blocks, XR(gate) ≤ PCH +
(PCH + 1)(n − 1), PCH data max 0.66n.

## 1. Measure
ISO (fbphase.reuse mode 5) = in-phase fallbacks preceded by an in-phase non-fallback transition: the isolated stalls, i.e. carries; each
maximal run of consecutive in-phase fallbacks (a wave, R100) starts at one. So f = Σ over the phase's fallback runs of their lengths, and
the number of runs is ISO (plus one if the phase opens with a fallback).

## 2. DATA
- Survey (experiments/red, 348 games, r1survey.py with M2 = 5): max ISO 15 (n5inj/instances/returns_ph64, n 64, f 15); returns_rt64 14,
  returns_rt48 13 (n 48), best_7 12 (n 40), pl130_n40 11 (n 40). Max ISO / n = 0.28 (pl130_n40).
- Climbs (fbclimb.py --iso, own start, fitness 100 f + 1000 ISO + total fallbacks, 40 min each):
  | seed | n | ISO at seed → best | f at best |
  | --- | --- | --- | --- |
  | pl130_n40 | 40 | 11 → 13 | 13 |
  | best_7 (S3) | 40 | 9 → 12 | 14 |
  | long121_n40 | 40 | 7 → 12 | 13 |
  | returns_rt48 (S3) | 48 | 13 → 15 | 15 |
  Plateau at ISO ≤ 0.33n. In the best games f ≈ ISO: the carries are isolated (waves of length 1-2), so no wave rides on the carries.
- Anatomy of the best pl130 climb (gate 0, one of Q = {0, 1, 6}): the 13 isolated stalls at t = 5, 12, 14, 18, 21, 25, 30, 32, 36, 39, 41,
  43, 45. Gate 0's path-set weight changes at 9 of them (new values at t = 12, 18, 21, 25, 30, 32, 36, 39), and its top element walks DOWN
  the ranks: bit length of the weight 39 → 35 → 35 → 35 → 32 → 31 → 31 → 30 → 30. Six distinct tops; three P-changes keep the top and change
  lower elements only (the low-digit changes a counter would need). The last four carries (t = 39-45) come at a constant P.

## 3. READING (design obstruction, not a theorem)
- A rise inside a P-block (length only) happens inside an S4a run and cannot end in a stall: each step of the run is an S4a step (W- and
  Ξ-improving). A stall comes only where the run ends. So stall-ending rises ≤ number of S4a runs = ISO, and the length rises add nothing
  to f.
- Carries therefore need P-changes of the gate (or of the alternatives they detach to), one or two per carry in the data. In every instance
  examined (long121 R98 §3; the pl130 climb above) the gate's top P element walks monotonically down the ranks. A walk is ≤ n steps, and
  each step consumed one high-rank vertex: about 6-9 carries per 40 vertices.
- Θ(n) carries per vertex budget needs P-changes that REUSE ranks: low-digit changes under a fixed top, repeated, i.e. a counter on the
  gate's path set. The data show three such changes per phase at most. A counter of this kind needs each digit's reset to be Ξ-improving for
  every vertex reading the gate (Ξ is monotone, so a reset must be paid for by a higher digit), and the higher digit's change is again one
  rank. This is the same budget, so I see no way to get more than about one carry per rank from it. Not a proof; not built.
- Several gates sharing a phase do not add stalls either. A stall is global (S4c fires only when S4a and S4b change nothing anywhere), so
  stalls of independent gates synchronise (as L-NEW noted for fallbacks in N5-READER §8).

## 3a. CORRECTION (2026-10-29 05:20Z): §3's "each reset costs a rank" is wrong; binary counting is Ξ-monotone and low-digit resets are
abundant (133 in one pl130 phase). See R104 §1-§2. The carry count (ISO) data of §2 stand.

## 4. OPEN
- A gate whose path set counts (low digits reset and re-rise under a fixed top) with a stall at each count. This is the only shape left for
  carries to beat one per rank.
- FB-LIN remains a CONJECTURE (data max 38 = 0.79n, fb38_n48; ISO max 0.33n).

## DONE / FINDINGS / NEEDS
- DONE: R103 (this file); ISO measure (fbphase mode 5), fbclimb --iso, r1survey M2 / SHOW.
- FINDINGS:
  - ISO (carries) data max 0.28n; climbs plateau at 0.33n; f ≈ ISO in the best carry games.
  - Carries track the gate's P-changes, and the gate's top walks down the ranks: about one carry per rank.
  - Length rises sit inside S4a runs and cannot end in stalls; several gates do not add stalls (stalls are global).
  - FB-LIN unkilled after four boxes.
- NEEDS: none from the owner.
