# Box 23: true maxima of R*_F and FL_F per W-run of plain N5 (L-COMP successor 8)
Lead brief 2026-10-30 13:09Z (D18): "a measurement beats an inference". FRONTIER: inside one W-run of plain N5, R3-POLY ⇐ R*-POLY ∧ FL-POLY
(l-new 893b9346, docs/new/N5-FREE-box85.md §3, Theorem FREE-RED, lane-PROVED: |F| ≤ (n − 1)(R*_F + 1) + FL_F). Work done 2026-10-30
13:10Z-22:xxZ (date -u). Every number here is DATA unless labelled. Labels: DATA, PROVED (mine, unrefereed), CONJECTURE, DEAD, READING.
Not a TARGET.md claim. G-N5-TIME stays open.

## Summary
- (a) My counter = L-NEW's xirise.py on the whole box-83 corpus (1,132 / 1,132 games).
- HEADLINE (DATA): R*_F is Θ(n²) per W-run on L-RED's latew family (R127/R128, mkrw.py LATE=1). Exactly R*_F = K·m and |F| = K(m + 3)
  in ONE W-run, with n = 14K + 8m + 2 (7 sizes, n 186-778; K28_m48 was predicted 1,344 before it ran and gave 1,344). Balanced K, m give R*_F ≈ n²/448.
  At latew_K20_m32: R*_F 640 > n = 538, confirmed by xirise.py. The brief's "corpus max 64" (gate_K64_n581) is 10× below this.
- PROVED (mine, trivial): R*_F ≤ |F| and FL_F ≤ |F|. With FREE-RED this gives R*-POLY ∧ FL-POLY ⟺ "every W-run has polynomial length".
  The reduction restates the open core; it does not narrow it. In the latew family that length is Θ(n²): polynomial.
- (b) Exhaustive, all start pairs:
  - n ≤ 3: max R*_F 0.
  - C(4): max R*_F 1, FL_F 1, |F| 3.
  - Random n 5: same maxima. Random n 6: FL_F 2 (see the table).
- (c) Local search finds R*_F ≈ 0.7-1.0 n (best 42 at n 60). That is far below the latew construction, and the climbs are budget-limited.
  So the growth fitted from climbs is not the true growth.
- FL_F: max 1 at n ≤ 5 exhaustive/random, 2 at random n 6, 6 by climbs (n 20); corpus max 8 (u23sw64_n32). No instance with FL_F
  growing with n was found; FL_F is 0 in every latew run.

## Definitions (from the text: RESULTS R88, R89; box 85 §3). Implementation rstar.py, on L-COMP's engine n5b (SPEC mode)
- State t = (σ_t, τ_t); transitions = n5b.N5.run's loop body (box17.Eng.step); fb_t = S4c fallback flag of t → t + 1.
- Ξ_t := VJ valuation of σ_t (Odd best reply); Iσ_t := Even edges (y, z) with Ξ_t(z) strictly better than Ξ_t(σ_t y) (SPEC S2).
- W_t := VJ valuation of σ_t in the game with Odd restricted to τ_t (the (σ_t, τ_t)-plays); λ_W := its cycle-node map.
- W-run (R89): maximal run of consecutive states of one τ-stretch none of whose transitions is an S4c fallback or changes λ_W.
- BLOCKED at state q (R88): y Even, z ∈ succ(y), z ≠ σ_q(y), W_q(z) ▷ W_q(σ_q y) and (y, z) ∉ Iσ_q.
- R*_F (R88's R*_T on F): transitions t → t + 1 of F at which some Even y adopts (σ_{t+1}(y) = z ≠ σ_t(y)) an edge BLOCKED at an
  earlier state q of F. Headline reading "strict" q < t (Lead reading 13:22Z; = xirise.py); "incl" q ≤ t also computed.
  PROVED (mine, one line): incl = strict on every run. S4a moves y only to σ_t(y) or along Iσ_t (its arena), and S4c only to a
  Ξ_t-best, hence improving, successor; an edge blocked at t is not in Iσ_t, so it is never adopted at t → t + 1. Checked: 0 W-runs
  with incl ≠ strict anywhere below (so no instance differs by more than 1, the Lead's flag condition).
- FL_F (R89's FL_S on F): transitions of F with σ_{t+1} ≠ σ_t and W_{t+1} = W_t.
- Also per W-run: |F|, la = max late adoptions of one edge, sig0 = transitions with σ unchanged (box 84 §4: always 0; 0 everywhere here).
- Start files: S3 overridden by every VALID entry (owner matches, edge exists), as L-RED R99's fullstart2.py (rstar.overlay).

## (a) Cross-check against L-NEW's xirise.py (read only, l-new 893b9346), box-83 corpus (1,132 runs): 0 disagreements
- xcheck.py: per game, (number of W-runs, max R*_F, max FL_F, max |F|, FREE-RED violations) from rstar.py vs L-NEW's committed
  new/box85/xirise_{sbcg,alt}.txt; and xirise.py re-run (unmodified, own process) on the first 15 games of each list: 30/30 print exactly
  the committed line. Result (results/xcheck.txt): 1,132 / 1,132 agree, 0 disagree, 0 failures. Corpus max R*_F 64 (gate_K64_n581),
  max FL_F 8 (u23sw64_n32): L-NEW's maxima reproduced.
- One disagreement found and resolved on the way: red/n3/instances/n3cov_lean.start is INVALID (L-RED R99 erratum: wrong-owner entries).
  n5x drops wrong-owner entries implicitly; my first reader did not (run of 20 iterations instead of 35). With the R99 overlay, and with
  n3cov_lean_fixed.start, both tools give R*_F 4, |F| 30 (n3cov_phi_fixed: 5, 9). The corpus line for n3cov_lean is a faithful run.
- Every pinned witness below is also counted by xirise.py: equal (R*_F, FL_F) on all 15.
- Limitation: the corpus comparison is per game (maxima and run count), not per W-run.

## (b) Exhaustive and random small-n tables (exh23.py; all start pairs; model C(n) of box 17)
- Model: ids in rank order, distinct minimal priorities per parity pattern, owners free, every nonempty successor set (self-loops
  allowed). Priorities matter only through (Ω, id)-rank and parity (box 17 privar.py). All (σ0, τ0) pairs. The maxima over all start pairs equal
  the maxima over maximal ok-chains from HEADS: a suffix of a W-run has subsets of its blocked sets and adoptions.
- n = 5 exhaustive is out of reach: |C(5)| ≈ 2.9·10^10 games; even out-degree ≤ 2 gives 7.8·10^8. n 5, 6 are uniform random samples.

| table | games | states (= start pairs) | W-run chains (heads) | max R*_F | chains with R* = 1 | max FL_F | max |F| | FREE-RED viol. | incl ≠ strict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C(1) exhaustive | 4 | 4 | 0 | - | - | - | - | 0 | 0 |
| C(2) exhaustive | 144 | 256 | 6 | 0 | 0 | 1 | 1 | 0 | 0 |
| C(3) exhaustive | 21,952 | 110,592 | 6,242 | 0 | 0 | 1 | 2 | 0 | 0 |
| C(4) EXHAUSTIVE (8 parts, results/C4_all.json, 25,101 CPU-s) | 12,960,000 | 268,435,456 | 13,131,476 | 1 | 9,512 | 1 | 3 | 0 | 0 |
| random C(5), seed 23, all starts | 20,000 | 4,866,523 | 110,270 | 1 | 437 | 1 | 3 | 0 | 0 |
| random C(6), seed 23, games with ≤ 4,096 start pairs, all starts | 20,000 | 19,320,173 | 274,550 | 1 | 2,583 | 2 | 4 | 0 | 0 |

- Witnesses (pin23.py: n5.py = n5b state by state, Oink zlk regions, verify.py, L-RED xeng.py state by state, rstar = xirise; ALL OK):
  - C4_rs1 (sha1 35785879…): R*_F 1 at n 4, the least n with R*_F > 0. Prio 0,1,3,4; owners O,E,E,E; |F| 2.
  - C4_fl1 (f3735200…): FL_F 1, all-Even.
  - R6_rs1 (d9410c60…): R*_F 1 at n 6.
  - R6_fl2 (c40352ea…): FL_F 2 at n 6, the only table with FL_F > 1 (exhaustive n ≤ 4 and random n 5 have FL_F ≤ 1).

## (c) Climbs maximising R*_F at n = 10..60 (climb23.py; engine n5b; one core, 900 s fresh / 1,800 s seeded)
- Mutations as box 12's climb.py. Fitness (max R*_F, Σ R*_F, |F|). Families:
  - fresh: random start game, start pair mutated.
  - chain: seeded from the previous n's best, padded with Even self-loops; seed-dominated, so a lower bound only.
  - s3: start = SPEC S3 of the current game, never mutated (plain N5 from its own start).
  - F: fitness = longest W-run.
  - fl: fitness = FL_F.
- Every END line is in results/climbs_end.txt; plot results/rstar_vs_n.svg (plot23.py).

| n | R*_F fresh | R*_F chain | R*_F S3 fresh | R*_F S3 chain | longest |F| (any climb) | FL_F (fl climb) | steps (fresh) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10 | 8 (|F| 10) | | 4 | | 10 | 3 | 159k |
| 15 | 13 (14) | | 5 | | 20 | | 63k |
| 20 | 17 (21) | | 12 | | 24 | 6 | 44k |
| 30 | 16 (27) | 31 (34) | 10 | 24 | 34 | 1 | 25k |
| 40 | 13 (15) | 36 (39) | | 31 | 39 | | 30k |
| 60 | 12 (13) | 42 (44) | | 34 | 44 | | 7k |

- Envelope fits (best per n, n 10-60): free start R*_F ≈ 0.93 n^0.97 (linear slope 0.71); S3 ≈ 0.17 n^1.36 (slope 0.67); longest
  |F| ≈ 2.0 n^0.80. On n 10-30 the exponents are 1.21 / 1.72 / 1.08. The curves bend down at n ≥ 40, where steps per climb fall
  from 159k (n 10) to 7k (n 60). READING: these are budget-limited lower bounds. They show only that random local search finds
  R*_F ≈ n. They say nothing about the true growth: the latew construction is quadratic.
- Start-pair inflation (DATA): at n 10 / 15 the S3-only climbs reach 4 / 5, against 8 / 13 with a free start. By n 30-60 both families
  find ~0.6-1.0 n.
- Mechanism (rs_fresh_n15, rs31_n30): the start state carries many BLOCKED edges (14 at n 15). The W-run drains them, nearly one late
  adoption per transition, mostly one switching vertex per step. Blocked edges are replenished mid-run (rs31_n30: 7-11 blocked at
  states 16-21). Max late adoptions of one edge: 2 in every climb witness.
- Pinned climb witnesses (pin23.py ALL OK):
  - rs8_n10 (278520ea…, R*_F 8, FL 1)
  - rs17_n20 (e7b77982…)
  - rs31_n30 (7d8665c6…, R*_F 31 > n)
  - rs36_n40 (234b6218…)
  - rs42_n60 (d3c0ca31…)
  - s3rs12_n20 (039d3e4a…, S3 start)
  - s3rs31_n40 (c44a2df4…, S3 start)
  - F24_n20 (4c4fab7e…, |F| 24 with R*_F 11; it 28, 1 fallback)
  - fl6_n20 (fb8b1397…, FL_F 6, R*_F 9)

## (d) The construction: R*_F on L-RED's latew family (mkrw.py LATE=1, R127/R128; regenerated, read only)
- Regenerated with `LATE=1 python3 red/span/mkrw.py K m OUT.pg OUT.start`. K8_m32 and K20_m32 are byte-identical to L-RED's pins
  (sha1 3498a23d…, 063d173c…). Counted with rstar.py (results/latew_rstar.txt); K20_m32 also with xirise.py:
  R*_F 640, |F| 700, FL 0, one W-run, returns 2,418.

| K | m | n = 14K + 8m + 2 | iterations | W-runs | R*_F | K·m | |F| = K(m + 3) | FL_F | max late adoptions of one edge | R*_F / n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | 16 | 186 | 76 | 1 | 64 | 64 | 76 | 0 | 4 | 0.34 |
| 8 | 32 | 370 | 280 | 1 | 256 | 256 | 280 | 0 | 8 | 0.69 |
| 12 | 24 | 362 | 324 | 1 | 288 | 288 | 324 | 0 | 12 | 0.80 |
| 16 | 28 | 450 | 496 | 1 | 448 | 448 | 496 | 0 | 16 | 1.00 |
| 20 | 32 | 538 | 700 | 1 | 640 | 640 | 700 | 0 | 20 | 1.19 |
| 24 | 40 | 658 | 1,032 | 1 | 960 | 960 | 1,032 | 0 | 24 | 1.46 |
| 28 | 48 | 778 | 1,428 | 1 | 1,344 | 1,344 | 1,428 | 0 | 28 | 1.73 |

- DATA: R*_F = K·m and |F| = K(m + 3) exactly on every row. The whole run is one W-run; each of the K pivot cycles has m transitions
  with a late adoption (R128 §1: every late-adopter edge is re-adopted once per pivot cycle) plus 3 without.
- Hence with K = ⌊n/28⌋, m = ⌊n/16⌋ (balanced): R*_F ≈ n²/448 = Θ(n²) per W-run, and the W-run length is Θ(n²) too.
- DEAD (any reading "R*_F = O(n)" or "R*_F ≤ n per W-run"): latew_K20_m32, R*_F 640 > n = 538 (xirise.py agrees).
  Not a kill of R*-POLY: n² is polynomial.
- Pins: latew_K8_m32, latew_K20_m32 through pin23.py: both ALL OK (n5.py = n5b over 280 / 700 iterations, Oink zlk, verify.py, xeng.py state by state, rstar = xirise (256, 0) / (640, 0)).

## What this means for the frontier (READING)
- R3-POLY ⇐ R*-POLY ∧ FL-POLY is, by R*_F, FL_F ≤ |F|, the same as "every W-run has polynomial length".
- The known extremes:
  - quadratic W-runs, with R*_F = Θ(n²) (latew);
  - FL_F ≤ 8 everywhere measured.
- The open question is whether a W-run can be superpolynomially long. A linear bound on R*_F is not available, and is false.
- Local search does not reach the constructed extremes. Exhaustive small n (R*_F ≤ 1 at n ≤ 4) gives no growth information.

## Files
- rstar.py (counter), xcheck.py (a), exh23.py + run_parts.sh + merge23.py (b), climb23.py + climbs.sh + seedchain.sh + fit23.py +
  plot23.py (c), pin23.py (pins), check.sh (fast self-check run by verify.sh).
- results/: xcheck.txt, C1-C4 (C4_all.json merged from parts/), R5_all_s23.json, R6_all_s23.json, climbs_end.txt,
  rstar_vs_n.svg, latew_rstar.txt.
- instances/: pinned witnesses (.pg + .start); climbs/: every climb's best (.pg + .start).
