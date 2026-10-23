# Draft RESULTS DE28-DE29 (Lead, 2026-10-23 04:35Z by date -u) — awaits CHECKER C22 re-diff (rev. 04:52Z: C22 E-1..E-3, N-1..N-3; checker 2e60ce3; rev. 05:08Z: C22 Addendum 1 E-4, checker 476ca61)

- DE28 (2026-10-23): N8a = Koh-Loho strategy iteration over the perfect (n, d/2)-universal tree (Koh & Loho arXiv 2108.13338, Algorithm 1;
  pdf sha256 21ee0e43…), with either frozen rule "global" or "switch-all" (L-NEW, (c) lane under D14/D15; docs/new/N8a-kohloho.md §2
  frozen, §7 dead-end record, l-new 30b8a6c), is a DEAD END at gauntlet step 2 (runtime growth, DATA): under both rules, pivot families
  whose verified members follow laws that are super-polynomial in n (laws DATA: H_k k ≤ 3, F_k k ≤ 1, G_k k ≤ 2, L_k k ≤ 3; R53 §6b G2) (L-RED box 21, docs/red/R53-n8a-counter.md §1-§6; l-red 9fa1067, 4035ab5, 1c19da3, 866615f). Every row below: kl.py
  --sol, then experiments/new/check_sol2.py = Oink zlk OK, strategies verified.
  Canonical family H_k = klmin_n13 (13 vertices, 18 edges, sha1 b8a5b1bdb2f130adee4a20e70b5b5382932f1b4e) + 2k isolated self-loops
  with new top priorities (experiments/red/kl/gen_gk.py or famgen.py H k), n = 13 + 2k: dual pivots 52, 900, 19,652, 521,284 for
  k = 0..3 = 4·n^{k+1} under BOTH rules (runs identical for k ≤ 2 as below, traces logged for k = 0; equal counts for k = 3) (H_1 889e8e1d…, H_2 c8a9fdffd5c74781f803a47da950829985457820,
  H_3 7b7b2ecc…); law DATA for k ≤ 3, i.e. n^{(n−11)/2}. Further families: F_k (klcount_n16 b5269084…, switch-all 4·n^{3+k}+3, k = 0, 1),
  G_k (klglobal_n16 179b2cd0…, global 8·n^{1+k}+6 and switch-all 5·n^{1+k}+1, k = 0..2); independently L-NEW's L_k (15-node core
  40dde127…, primal, global 3·n^{k+1}+1, switch-all 4·n^{k+1}; levels_2 3c0092c4…, levels_3 9ce17076…). Lead re-runs (trunk kl.py, both
  rules where listed): klcount_n16 and klcount_n18_lvl (switch-all), klglobal_n18_lvl and klglobal_n20_lvl2 (global), H_2 from famgen.py
  (both, 19,652 each); all verified. gen_gk.py reproduces every pinned F/G/H sha1 (L-RED R53 §6a; CHECKER C22 re-run).
  Mechanism (R53 §2-§5, reading from traces): Tighten on the perfect tree carries in base n; a lapping cycle that the rule keeps open
  climbs one leaf per period through all leaves of the top L levels, and each extra priority value (even on an isolated vertex) adds a
  level. R53 §6b: PROVED Tighten = leftmost leaf below the successor (any ordered tree); PROVED the top L levels of an (ℓ, h)-universal
  tree are (ℓ, L)-universal; COMPUTED (kadmiss.py: at most one admissible arc per Odd node at every iteration on H_0..H_2), hence
  PROVED by induction: every rule in SA (switch every Odd node that has an admissible arc, to an admissible arc; R53 §6b
  item 3) gives the identical run on H_0..H_2; transfer to every
  universal tree for SA rules is a READING with gaps G1 (succinct trees: local offsets), G2 (law DATA for k ≤ 3), G3 (rules outside SA not
  covered). REFUTED (computed, ksubset.py) for 'every pivot rule': four single-switch rules (lowest index, highest index, random seeds
  1, 2) solve H_0..H_2 in 9, 5, 5, 17 iterations (this led to N8d). Not touched: the paper's theorems
  (iterations ≤ n·|L(T)|; the family shows the perfect-tree bound is nearly attained). Random corpus (10,000 games, both rules) all
  verified: the kill is on running time, not correctness.
- DE29 (2026-10-23): N8d-R1 = Koh-Loho tree SI over the perfect tree with the single-switch rule R1 (lowest-index Odd node with an
  admissible arc takes its largest-Tighten arc; rules frozen in docs/new/N8d-single.md §0 at l-new d7fadfb before any run; code
  experiments/new/kl/kl_single.py --rule r1) is a DEAD END at gauntlet step 2 (runtime growth): on Friedmann's switch-all family
  (experiments/hard-families/pgsolver_port.py switchallexp N, n = 14N + 7) dual pivots 14, 39, 84, 165, 318, 615, 1,200, 2,361, 4,674,
  9,291 for N = 1..10 (ratio 1.93-1.99 per N from N = 5; DATA fit ≈ 9·2^N = 2^{Θ(n)}); switchbestexp N = 1..8: 28 … 2,297 (×1.8 per N at the top);
  every output verified and = Oink zlk (results/switchallexp.r1.csv, switchbestexp.r1.csv; l-new c79dd24). Lead re-run (03:50Z, trunk
  kl_single.py): N = 6 (sha1 5dc850b156c6…) 615 and N = 7 (ff46e32f1d93…) 1,200 dual pivots, check_sol2 verified, = lane CSV.
  Reading (lane, N8d §3): the lowest-index single switch falls to Friedmann's families as single-switch rules do on VJ valuations
  (BARRIERS B8); the tree labels do not help there. Not a kill of N8d-R2 (random node), which is under attack (L-RED box 22).
