# L17: build the base AROUND the f6 cascade (BOX L17; L-LOWER successor 14)
Labels: PROVED (lane) / CONJECTURE / DATA / DEAD. Lead approval 07:37Z 2026-11-12. Every DATA clause names its counter (unit, set, scope).
Model: R104's IDEAL model at degree ≤ 2 (sim6; fenc for replays). Target core8 (c6e19673). Tools experiments/lower/l16/ and l17/.

## 0. The box and what success would mean
- Box (Lead 07:37Z, quoted): «build the base AROUND the cascade. Freeze the f6 pair (ekr2_f6_k1_P510, 4fee0495) first, then search the readers'
  wiring.» «Milestone: a full realized design past P 18 (rows 0..18), replayed by sim6 = fenc on two engines. Stretch: P 32.» «Stop and write
  the obstruction if three consecutive capped runs give no answer at the same P.»
- What a success would show (stated before any run). A genome whose free run follows core8's rows 0..P for P ≥ 18 would be DATA: one more
  realized prefix of the level-8 target in the IDEAL model, beyond the walls 17 / 14 / 15 of L13-L14, built with a one-pair XOR gadget for the
  cluster sink. It would NOT show: a lower bound for N5 (a realized prefix is an upper-bound construction attempt, not an iteration count on a
  game); that the level-8 tower exists (rows 0..510 are needed); that d grows linearly (one level only); or anything about N5 on real games
  unless the full-horizon replay also holds on the real N5 run (R104's IDEAL model vs the N5 implementation; L-RED / L-COMP own that check).
- What a failure would show: only that this frame (frozen f6 pair, annealed / SAT-searched readers on the C12 wiring) did not find one within
  the caps; nothing about other frames.

## 1. Why the frozen pair does not stay correct by itself (DATA, exact; l16/f6check.py)
- Counter: free pre-states of f6 (13) on rows 0..P where its better in the genome's CLAMPED run (core forced to core8) differs from its required
  value. C12 itself: 16 / 129 (P 510). C12 + the P 510 design grafted at level 8 (l16/run/C12_F6k1_P510.txt): 42 / 129: the graft changes
  o(8), hence every helper above, hence the chains f6 reads.
- Redesign with o(8) kept (ekr2 KEEPO) and inputs widened to all 34 movers avoiding f6 / the slots: SAT at P 32 (C12_f6_k1_P32_keepwide.txt,
  replayed by sim2), but after grafting (l16/run/B2.txt) 5 / 10 mismatches at P 32: movers reading f6's chain or slot 16 (18, 46) change and
  feed back through keys. Keeping all their base betters too (KEEPR) is UNSAT at P 18 (solver only; core over 12, 14, 15, 18, 19, 22, 24, …):
  the readers must CHANGE (they should read f6's new information), so the frame has to re-search them, as the Lead's box says.
- Cluster structure (DATA, exact; counter = free pre-states over rows 0..510 where the required value differs from the formula): f6 =
  XNOR(q6, q7) 0 errors; q7 = copy f7 0; f7 = NOT q7 0; q7 = XOR(q6, f6) 1; f7 = XNOR(q6, f6) 1; f5 = XNOR(q5, q7) 2. The cluster's lists are
  copies and XORs of each other; any Ξ order leaves one member needing an XOR from outside (CLUSTER-SINK, L16 §2).

## 2. Search runs (filled in as they end)
- A1: l14/ann3.c from C12 + the P 510 design (l17/run/A1_start.txt), frozen options 26, 27 (f6) and 32-35 (the pair), C12's three cuts,
  seed 17, 2,700 s, T 0.8. Start score 1,106 (unit = violated constraint of the full target; C12's own run started at 284, ended 137).
  End: best 489 (A1.txt 77fc18ff; ranks re-solved by l14/rsolve.py → A1_solved.txt 087269f5). ann3 re-solves ALL ranks, so the design's ranks are
  not kept: f6 mismatches 7 / 18 free pre-states on rows 0..64 of A1's clamped run (l16/f6check.py). Exact prefix (l13/sweep1.sh, pgad3, XS 8,
  G {63}): UNSAT already at prefix 2 (solver only). A1: DEAD start (frozen wiring without frozen ranks breaks f6 at row 2).
- A2: same, from B2 (C12 + the o(8)-keeping P 32 design, l17/run/A2_start.txt a6c646f6), seed 18. Start 909, end best 161 (A2.txt d9aa4f7e).
  Ranks re-solved (l14/rsolve.py → A2_solved.txt 2eae1e1f; score 161 of 12,556 constraints). Unlike A1, the re-solved ranks KEEP f6 correct
  (DATA, l16/f6check.py; counter = free pre-states of f6 in the clamped run where its better differs from its required value): 0 / 18 on rows
  0..64, 0 / 129 on rows 0..510. Free run (l13/prefcheck.py, sim6 = fenc): fixed point at T 6, rows 0..6 followed; at row 7 movers 11, 13, 15
  must flip and 11 does not want to (l16/diag.py).
  Exact prefix (pgad3, G {63}, 600 s per question; l17/sweep.sh; l17/sweepA2/): XS 8: SAT for every prefix 2..12, UNSAT at 13 (296 s);
  XS 11: SAT 2..12, UNSAT at 13 (379 s). Every SAT decode (22) replayed sim6 = fenc, each following at least rows 0..P (sweepA2/replay.txt,
  SHA1SUMS). DATA (unit = prefix length in core8 rows, scope A2_solved with one helper 63 and one rewired client): best realized prefix rows
  0..12 (A2x8_P11_dec follows 0..12 as well). A2 does NOT pass P 18. P 13 UNSAT for XS 8 DRUP VERIFIED (l17/sweepA2/drup.txt: 880,002 clauses, Glucose4 proof, l8/sat/drup.c «s VERIFIED»); XS 11 at P 13 solver-only (DRUP pending).
- Reading of the stop rule used here: a «run» is one capped search plus its exact prefix measurement; three consecutive runs that do not pass
  P 18 end the box with the obstruction. Count so far: A1 failed (prefix < 2); A2 failed (prefix 12, UNSAT at 13 for XS 8 and XS 11); A3 running (pgad5, below).

- A3 (frame that keeps the design's ranks): l16/pgad5.py on A2_solved, all ranks of fixed options kept, the f6 pair's signs / gates / starts
  fixed (FIXC 16, 17; f6 = mover 13 not in XS), clients XS = {8, 11, 12, 14, 15} free to read ANY mover compatible with the order
  XORD 8 < 11 < 12 < 15 < 14 (the base wiring's reach order among XS, computed on A2_solved), G empty; ascending from P 10, 2,900 s per
  question (l17/sweep5.sh). SAT at P 10 (99 s), 11 (626), 12 (496), 13 (812), 14 (765), 15 (2,680 s); P 16 running.
  Every decode replayed sim6 = fenc (l17/sweepA3/replay.txt, SHA1SUMS). DATA (unit = core8 rows followed by the free run, scope this frame
  on A2_solved): A3x5_P15_dec (27ac152d) follows rows 0..15, T 16, the lane's longest realized prefix so far (L14-L16 best: rows 0..14).
  DATA (f6check rows 0..510, same counter as §1): every A3 decode breaks f6 beyond its prefix, 47-62 / 129 mismatching free pre-states,
  first at row 14-18 (l17/sweepA3/f6check.txt): re-searched readers change the chains f6 reads (the L16 coupling, seen from the reader side);
  the prefix constraints repair f6 only on the rows they cover.
- A2 XS 11 P 13 UNSAT: DRUP check hit its 2,900 s cap (proof 1.56 GB; exit 124): solver-only, NOT cited.

## 9. Diff against TARGET.md
No statement mentions a parity game, a winning region, an algorithm's running time or a complexity class. All statements are about the IDEAL
model's step sequence (R104's definition) on degree-≤-2 genomes and core8's rows. Not M3, not a gauntlet step-4 pass, not a TARGET.md claim.
