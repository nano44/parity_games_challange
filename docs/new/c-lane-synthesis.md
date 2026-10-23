# (c) lane synthesis after N1-N10 (L-NEW successor 7, Opus 5.5, D15; box 20, writing only)
Lead brief 2026-10-23 21:33Z (date -u). Sources: the lane's files and RESULTS DE22-DE33; no new code, no new runs.
Labels: DATA (a committed run), PROVED (an argument in a lane file), READING (my interpretation). No running-time claim.

## 1. Three structural lessons, with the instances that taught them
- L1. Local-improvement potentials get lapped by counters with delay lanes. A method that moves one strategy (or label vector)
  forward by local steps, ranked by a potential, can be driven through a base-n counter. Delay lanes make the counter survive
  randomisation.
  - DATA: N8a (DE28) on L_k = 15-node core + k high even self-loops: 3·n^(k+1) pivots (global) and 4·n^(k+1) (switch-all);
    levels_3.pg = 314,929 / 419,904. L-RED R53: F_k = klcount_n16 + 2k self-loops, dual pivots 4·n^L + 3.
  - DATA: N8d-R1 (DE29): switchallexp dual ≈ 9·2^N.
  - DATA: N8d-R2, random node (DE30, R56 §4): HLg_k = H_k + two z-separated delay lanes; mean pivots 630, 32,201, 2,759,578,
    388,769,332 for k = 0..3. It stops only if a lane-length run of frontier picks beats every rescuer, which costs ε(L) ≤ (r+1)^-L.
  - Earlier forms, same mechanism (DATA): N1 deep-trap switchallexp, one phase = Friedmann's counter (DE22). N2 padded switchallexp,
    largest stage 604 at N = 7 (DE23). The DTL attacks (L-RED; listed among the lapped methods in the Lead brief of 16:16Z; files not re-read for this box).
- L2. A relaxation must be exact on one-player games. One-player parity is polynomial, so a relaxation that fails there spends its
  levels on the easy part.
  - DATA: N9a (DE31) on circ(n,1,2) (all Even, all priorities 1, Odd wins everywhere): least exact Sherali-Adams level
    k* = ceil(n/3) for n = 3..11. circ12_n7.pg is wrong at k = 2; circ12_n10.pg is wrong at k = 3.
  - PROVED (N10-screen.md Lemma B): a min-cut family of escape cuts (ESC1) makes level-0 ACYC exact on one-player games of either
    owner. So L2 is cheap to satisfy.
- L3. LP and cut relaxations cannot supply Odd's strategy τ. Once one-player exactness is bought, every remaining gap is a two-player
  game where the cut that would refute it needs Odd's winning strategy on an Even-closed set, and no LP-guided τ finds it.
  - DATA: N10a has 15 gaps in 800 two-player queries; 12 of the 15 runs never violate a cut.
  - DATA: N10b (τ from the rounded Odd-side LP) fails on esc_gap_r1794_Q1.pg (n = 8, cuts = 0) and on counter_symsi N = 2, 3.
  - DATA: N10c (conditioning, one-sided) is STUCK on cond_stuck_r1569_YE.pg (n = 14). Its first wrong accept is an N10b gap
    (esc_gap_from_r1569.pg). It is also STUCK on cond_stuck_symsi3_YE.pg (n = 32).
  - Same lesson on the rounding side (DATA): N9b r26 (DE32). The LP value is exact (|W_O| = 6), yet the rounded strategy wins
    nowhere: the optimum is a mixture.

## 2. What the three lessons rule out, and what they do not touch (all READING unless marked)
Ruled out as lines for this lane (no theorem: each kill is a family, and B8-B11 bound only named rules):
- (a) by L1: single-trajectory improvement with a local potential, over any value domain (VJ valuations, discounted values, tree
  labels) and any pivot choice, deterministic or uniformly random. Exact best replies inside a step do not rescue it either:
  N8a's global rule (one-sided optimum) still fell to L_k.
- (b) by L2: relaxation hierarchies on encodings that already fail on one-player games (SA+ of ACYC: DE31). This says nothing
  about hierarchies on better encodings.
- (c) by L3: "relax, then round or cut using an LP-guided τ": N9b, N10b and N10c. It also covers any variant whose two-player
  step is a guess of τ from the same LP.
Not touched:
- (d) Methods whose progress is not a single trajectory: recursive decomposition (the Zielonka family; B4 gap, B5 families
  only), and attractor/dominion methods with a completeness argument.
- (e) Separator / automaton approaches (weak separators; L-STRUCT) and the structural-parameter results (M3 only).
- (f) Relaxation hierarchies (SA, SOS) on encodings that are one-player exact (ACYC + ESC1 is one). L3 was observed at level 0
  and level 1 only. Whether a fixed lift of ACYC + ESC1 closes the τ gap is OPEN: untested, and not ruled out by DE31.
- (g) Symmetric methods where Odd's τ is part of the state rather than guessed. N5 (SSI-GLOBAL) is one. It is the lane's only
  gauntlet-step-2 survivor, but it is a local-improvement method on both strategies, so L1 predicts it falls. No delay-lane
  counter has been tried against it: R53/R56 postdate N5's killer attempts (boxes 3-11).

## 3. Recommendation for the next box
Pause new (c) design for one box. Spend that box on the cheapest decisive test the lessons point to: L1 applied to N5.
- What: L-RED builds an R56-style counter for N5 (SSI-GLOBAL), meaning a base-n lapping core plus z-separated delay lanes on the
  fatal moves. The core is adapted to N5's best-reply gate (docs/new/N5-ssi-global.md; box 11's toggle instances in
  experiments/new/instances/br11b as seeds).
- Falsification test: super-polynomial growth of N5 iterations along the family, every run verified (Zielonka/Oink zlk plus
  harness/verify.py on both strategies).
- Owner of the work: L-RED, not L-NEW. It is an adversary task against a named candidate, and L-RED wrote R53/R56.
- Why this and not another design: it settles G-N5-TIME's direction (the lane's last open item) at low cost, and it tests L1 on
  the one method that survived everything else. If N5 survives a serious delay-lane attack, that is evidence against L1's scope
  and the most useful thing the fleet could learn.
- If the Lead prefers a design box instead: the one approach in (f). SA+_1 or SA+_2 of ACYC + ESC1 + ESC-τ, a lift of a
  one-player-exact encoding. Falsification test: the N10 gap instances (esc_gap_r1794_Q1, esc_gap_from_r1569,
  counter_symsi N = 2, 3) and the 2,000-game random corpus; kill = a gap at level 2. It meets L1 (one LP) and L2 (Lemma B), and
  it is the only cheap way to test whether L3 is a level-0/level-1 artefact. My estimate that it survives: low (about 0.05).
