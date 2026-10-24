# Draft RESULTS DE30 (Lead, 2026-10-23 15:40Z by date -u) — LANDED in RESULTS Dead ends (CHECKER C23 Addendum 1 PASS, checker 77a8ede; lines 3-32 verbatim); was: awaits CHECKER C23 re-diff (rev. 15:57Z: C23 E-1, N-1..N-3; rev. 17:06Z: E-2; checker b356554)

- DE30 (2026-10-23): N8d-R2 = Koh-Loho strategy iteration over the perfect (n, d/2)-universal tree (arXiv 2108.13338v5, Algorithm 1) with
  the single-switch rule R2 (a uniformly random Odd node with an admissible arc, drawn by random.Random(seed), takes its largest-Tighten
  admissible arc; docs/new/N8d-single.md §0 frozen at l-new d7fadfb, pins §0b/§0c: compressed priorities canonical) is a DEAD END at
  gauntlet step 2 (runtime growth, DATA): a family whose verified members run the full lap counter, about (4L+2)·n^{k+1} pivots, on all but one of 17 runs
  (L-RED successor 12, box 24, docs/red/R56-r2-vj-switchsets.md §2-§4; l-red 29f74b1, 3bc170d, c5e3abb, b088440).
  Family HLg_k = experiments/red/kl24/hlgen.sh k L L: R53's H_k (DE28) plus two z-separated delay lanes (lanegen.py) on the two moves
  by which R2 escaped H_k, with L = 5, 6, 8, 10 for k = 0..3, n = 9 + 2k + 4L = 29, 35, 45, 55 (sha1 d2b96b45…, 2366cbad…, 1c3c7889…,
  9918e9b8463507401cf73a73a2945aa9bf5f23ac). R2 dual pivots (primal 0 on every row), every output with regions = Oink zlk @ 8fbf0a7 and
  both strategies passing experiments/harness/verify.py, code experiments/n8d-second/kl2fast.py (= L-NEW's kl_single.py seed for seed,
  checked on HL88_0 seeds 1-3 and HL88_1 seed 1): k = 0: 633, 623, 639, 643, 611 (mean 630); k = 1: 32,170, 32,232, 32,156, 32,214,
  32,232 (mean 32,201); k = 2: 3,139,182, 3,139,646, 1,230,538, 3,138,968, 3,139,556 (mean 2,757,578; one early stop, seed 3); k = 3: 388,766,970 and
  388,771,694 (seeds 1-2 only, runtime; mean 388,769,332). Steps ×51, ×86, ×141 per +1 of k. Lead re-runs: k = 0 and k = 1 seeds 1-5
  (kl2fast, all = lane, all verified; hlgen sha1s reproduced), k = 2 seeds 1 and 3 (= lane, verified, as HL88_2: same sha1), k = 3:
  lane rows only (results/hlg_k3.csv, solvecheck.py); not re-run by the Lead or CHECKER (a Lead re-run of seed 1 was lost to a container restart).
  Per-lap failure probability ε(L) of the lap counter (DATA: exact absorbing-chain computation, experiments/red/kl24/exactlap.py, from
  kl2fast's own candidate sets and least fixed point): steady per-lap ε = 6.2e-3, 5.75e-4, 3.92e-5, 2.1e-6, 1.0e-7 at L = 4..8, ratios
  ×10.8, ×14.7, ×18.3, ×21 per +1 of L (ratios growing; reading, R56 §3c: not a power law on this range). Lead re-run of the one-lap chain: L = 5 3.90822e-4,
  L = 6 2.75358e-5 (= lane). Coverage caveats: one snapshot lap per L for the multi-lap chain; every lap start scanned only at L = 4, 5
  (R56 §3b'); L ≥ 9 one-lap or extrapolated.
  Mechanism (READING, R56 §1, §4d): on Friedmann's Random-Edge game G_ζ (faithful: VJ Random-Edge counts on it, R55) R2's admissible
  sets differ from VJ's improving sets from state 0 (M1: label truncation hides odd costs; M2: truncation is idempotent, so delay lanes
  do not unwind), which is why G_ζ does not kill R2; the z-separated lanes repair M2, and a lap fails only if a run of L frontier picks
  beats every rescuer, so ε(L) ≲ 2^{−L}; with L(k) = Θ(k log k) the size stays polynomial in k and the expected pivot count is
  exp(Θ(n)) (READING beyond k = 3).
  Status: PROVED nothing new about R2's running time; DATA the table and the exact chains; READING the mechanism, the at-least-
  exponential decay of ε beyond L = 8 and the asymptotic schedule. Gaps for a proof: (G1) an ε bound for every lap type reachable in
  HLg_k; (G2) lap failures are the only exit from the counter. Not touched: correctness (N8d-proofs.md §2, PROVED by L-NEW, unrefereed:
  any single admissible switch rule is correct and terminates within n·n^h pivots); gauntlet steps 2 (two independent implementations,
  ~83,000 runs, 0 incorrect; L-COMP experiments/n8d-second/; passed by Lead reading 08:35Z) and 3 (L-LIT T26, SIGN WITH CAVEATS) had been passed; on Friedmann's
  switch-all/switch-best families and 10,000 random games R2's means stay about n^2 (DATA), which this family overturns.
