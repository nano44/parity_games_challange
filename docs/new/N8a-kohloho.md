# N8a: Koh-Loho strategy iteration over the perfect universal tree, kill test (L-NEW successor 5, Opus 5.5; box 14)
Lead GO 01:51Z 2026-10-23 (date -u): fidelity first, then pivot rules switch-all and global, bench on tc N = 1..8, counter_qpt, the rest.
Source: Z. K. Koh, G. Loho, "Beyond value iteration for parity games: strategy iteration with universal trees", arXiv 2108.13338
(LMCS 21(2) 2025, 24:1-24:35), PDF sha256 21ee0e4336252f7e (opened 2026-10-23). Code: experiments/new/kl/kl.py.
Status: STEP-2 SURVIVOR ON THE HARD BENCH (DATA, Lead's box-14 criterion, 2026-10-23 ~01:57Z): all 13 hard families, both pivot rules,
all outputs verified; iterations ≤ 2N+O(1)-type on every family (§3). Random-game part of step 2 pending (§4). D1 applies: this is data, not a claim.

## 0. Fidelity: code function ↔ paper
| kl.py | paper | note |
| --- | --- | --- |
| `Game` | §2 instance (G, π), π: V → [d], d even | priorities compressed order- and parity-preserving into [d] with min ≥ 1; d rounded up to even |
| tuple of length h = d/2 over {0..n−1}; `None` = ⊤ | §2.1 perfect (ℓ, h)-universal tree, M = {0..ℓ−1}, ℓ = n; leaf ξ = (ξ_{2h−1}, …, ξ_1); §2.2 L̄(T) = L(T) ∪ {⊤} | (n, d/2)-universal (Def. 2.2, "perfect universal tree") as Theorem 2.3 requires |
| `klen`, `trunc` | §2.1 p-truncation ξ|_p (odd p keeps indices ≥ p, even p keeps ≥ p+1); ⊤|_p = ⊤ | |
| `violated` | §2.2 feasibility condition per arc (even π(v): µ(v)|_π ≥ µ(w)|_π; odd: > or both ⊤) | |
| `tighten` | §2.2 Tighten(µ, vw); γ(T) = O(d) for the perfect tree | smallest non-violating ξ: prefix (even) or prefix successor in base n (odd; ⊤ on overflow), padded with 0s |
| `lift` | §2.2 lift(µ, vw) = Tighten if violated, else µ(v) | = max(µ(v), Tighten) |
| `drop` | §3.1 drop(ν, vw) = Tighten if loose, else ν(v) | = min(ν(v), Tighten) |
| `edges_tau` | §2 strategy subgraph G_τ | |
| `base_nodes` | Definition 3.3 B(G_τ); reduction in the proof of Thm 3.4 (v ∈ B iff π(v) even and the min-bottleneck cycle through v costs π(v)) | implemented as: v on a cycle of G_τ[π ≤ π(v)]; O(d·m) instead of O(m log d) |
| `dijkstra` | Algorithm 2 (lines 2-11); H = G_τ \ ∪_{v∈B} δ⁺(v); Φ_p (three properties, §4); Φ_ν interlaced potential (§4) | Φ_p via Tarjan SCC order (sinks get the smallest number); argmin by linear scan (O(n²) per call, not Fibonacci heaps) |
| `label_setting` | Algorithm 3 (Line 4 lifts on base nodes, then Dijkstra); Theorem 4.5 | Remark 4.6 says Line 4 is skippable inside Algorithm 1; kept |
| `naive_lfp` | Proposition 2.5 (i): apply G_τ↑ = {Lift_v (v ∈ V0), Lift_vw (v ∈ V1)} until convergence | fidelity oracle only (exponential in general, §3 "Running time") |
| `strategy_iteration` | Algorithm 1 (µ ← min L(T); τ ← τ_1; µ ← µ^{G_τ1↑}; loop while an admissible arc exists) | τ_1 = first successor; admissible = violated arc of an Odd node (§3) |
| `even_strategy` | Theorem 2.3 (Even wins iff µ*(v) ≠ ⊤); progress-measure strategy: a non-violated arc | Odd's strategy = Even's of the DUAL game (owners swapped, priorities +1), solved by the same algorithm |
Checks (experiments/new/kl/fidelity.txt): 300 random games (gen.py n = 3..8, d = 2..6, out-degree 1-3, seeds 7001-7300), both rules, `--check`:
Algorithm 3's output equals the naive least fixed point at EVERY call (850 calls; 167 games pivot at least once, max 3 pivots), µ is
pointwise non-decreasing at every iteration (Theorem 3.1's proof), primal and dual regions agree, and all 600 solutions agree with Oink
zlk with both strategies verified by harness/verify.py. 0 failures.
Iteration bound: Theorem 3.1's proof (µ strictly increases, finite lattice) gives ≤ n·|L(T)| = n·n^{d/2} iterations; the code asserts
monotonicity each iteration. Per-iteration cost: Theorem 4.5 gives O(d(m + n log n)) with Fibonacci heaps; kl.py uses a linear-scan
argmin and recomputes base nodes and Φ_p from scratch: O(d·(n² + m·d)) per iteration in Python; polynomial, which is all the kill test
needs (the measure is the NUMBER of iterations). Bit cost: labels are h-tuples of integers < n, i.e. O(d log n) bits; no big numbers.

## 1. Measure
Iterations of Algorithm 1 (pivots), primal (Odd pivots) and dual (Even pivots in the dual game), against N and n, per rule.

## 2. Pivot rules (stated before the bench runs; the smoke tests on hij 6, tc 1, tc 2 and the fidelity corpus came first)
- `all` (control, switch-all): every Odd node with at least one admissible arc switches to its admissible arc with the LARGEST
  Tighten(µ, vw) (⊤ largest; ties by the smallest successor index).
- `global` (N5-style one-sided optimum): let σ be Even's counterstrategy read off µ (at each Even node the non-violated arc with the
  smallest head label, ties by index; if none, the smallest head label). In the arena A where every Odd node may use τ(v) or any
  admissible arc and Even is fixed to σ, solve Odd's one-player game exactly: Odd wins from v iff v can reach a cycle of A whose top
  priority is odd; on that set take the cycle/attractor strategy (BFS inside each odd-topped SCC of A[π ≤ p] toward one top node,
  then backward attractor). Every other Odd node with an admissible arc takes the switch-all choice. If nothing changes, switch-all.

## 3. Bench
| family | N: n / pivots global (dual) / pivots switch-all (dual) | all outputs |
| --- | --- | --- |
| tc | 1: 8 / 0 (0) / 0 (0); 2: 22 / 3 (3) / 3 (3); 3: 42 / 4 (4) / 4 (4); 4: 68 / 5 (5) / 5 (5); 5: 100 / 7 (6) / 6 (6); 6: 138 / 7 (7) / 7 (7); 7: 182 / 11 (10) / 8 (8); 8: 232 / 12 (13) / 9 (9); 10: 350 / 12 (14) / 11 (11); 12: 492 / 14 (18) / 13 (13); 14: 658 / 15 (24) / 15 (15) | verified (verify.py) and = Oink zlk |
| tc+ | 1: 8 / 0 (0) / 0 (0); 2: 24 / 2 (2) / 2 (2); 3: 54 / 3 (3) / 3 (3); 4: 104 / 4 (4) / 4 (4); 5: 180 / 5 (5) / 5 (5); 6: 288 / 6 (6) / 6 (6) | verified (verify.py) and = Oink zlk |
| counter_qpt | 1: 2 / 0 (0) / 0 (0); 2: 4 / 0 (0) / 0 (0); 3: 6 / 0 (0) / 0 (0); 4: 8 / 0 (0) / 0 (0); 6: 12 / 0 (0) / 0 (0); 8: 16 / 0 (0) / 0 (0); 10: 20 / 0 (0) / 0 (0); 12: 24 / 0 (0) / 0 (0) | verified (verify.py) and = Oink zlk |
| counter_m | 2: 9 / 1 (1) / 1 (1); 4: 15 / 1 (1) / 1 (1); 8: 27 / 1 (1) / 1 (1); 12: 39 / 1 (1) / 1 (1); 16: 51 / 1 (1) / 1 (1); 20: 63 / 1 (1) / 1 (1) | verified (verify.py) and = Oink zlk |
| counter_rr | 2: 8 / 0 (2) / 0 (2); 4: 16 / 2 (2) / 2 (2); 8: 32 / 2 (2) / 2 (2); 12: 48 / 2 (2) / 2 (2); 16: 64 / 2 (2) / 2 (2); 20: 80 / 2 (2) / 2 (2) | verified (verify.py) and = Oink zlk |
| counter_dp | 2: 12 / 2 (1) / 2 (1); 4: 20 / 2 (1) / 2 (1); 8: 36 / 2 (1) / 2 (1); 12: 52 / 2 (1) / 2 (1); 16: 68 / 2 (1) / 2 (1) | verified (verify.py) and = Oink zlk |
| counter_core | 2: 15 / 2 (1) / 2 (1); 4: 27 / 2 (1) / 2 (1); 6: 39 / 2 (1) / 2 (1); 8: 51 / 2 (1) / 2 (1); 10: 63 / 2 (1) / 2 (1) | verified (verify.py) and = Oink zlk |
| counter_ortl | 2: 11 / 0 (1) / 0 (1); 4: 21 / 0 (1) / 0 (1); 6: 31 / 0 (1) / 0 (1); 8: 41 / 0 (1) / 0 (1); 10: 51 / 0 (1) / 0 (1) | verified (verify.py) and = Oink zlk |
| counter_rob | 1: 14 / 3 (3) / 4 (3); 2: 31 / 6 (5) / 6 (5); 3: 54 / 7 (5) / 8 (5); 4: 83 / 13 (10) / 10 (5); 5: 118 / 14 (10) / 12 (5) | verified (verify.py) and = Oink zlk |
| counter_symsi | 1: 12 / 2 (3) / 2 (3); 2: 22 / 5 (3) / 5 (3); 3: 32 / 7 (5) / 7 (5); 4: 42 / 10 (10) / 10 (8); 6: 62 / 16 (16) / 16 (14) | verified (verify.py) and = Oink zlk |
| switchallexp | 1: 21 / 1 (4) / 1 (7); 2: 35 / 1 (6) / 1 (7); 3: 49 / 1 (9) / 1 (8); 4: 63 / 1 (11) / 1 (10); 5: 77 / 1 (13) / 1 (12) | verified (verify.py) and = Oink zlk |
| switchbestexp | 1: 35 / 1 (13) / 1 (20); 2: 60 / 1 (34) / 1 (21); 3: 85 / 1 (27) / 1 (54); 4: 110 / 1 (33) / 1 (60) | verified (verify.py) and = Oink zlk |
| recursiveladder | 2: 10 / 3 (0) / 3 (0); 4: 20 / 3 (3) / 3 (3); 6: 30 / 3 (3) / 3 (3); 8: 40 / 3 (3) / 3 (3); 10: 50 / 3 (3) / 3 (3) | verified (verify.py) and = Oink zlk |
Initial-strategy robustness (kl_init.py, τ_1 = last successor or uniform random, seeds 1-3; both rules; all verified, all = Oink):
tc 4: 4-10 pivots; tc 8: 11-17 pivots; counter_qpt 4, 8: 0 pivots for every τ_1.
Reading: the iteration counts are small and grow at most linearly in N on every hard family, including tc (exponential for the
progress-measure algorithms on the SAME perfect tree, BARRIERS B6) and counter_qpt (built against the quasi-polynomial algorithms).
Sizes reached: n ≤ 658 (tc 14), d ≤ 126. NOT yet done: gauntlet step 2's 10,000 random games, larger N, adversarial search.

## 4. Random part of gauntlet step 2 (2026-10-23 ~02:02Z by date -u)
Corpus: `gen.py corpus experiments/new/out/kl/rand10k 10000 20261023 --nmin 1 --nmax 120` (gitignored; regenerable; manifest.csv sha1
c2b19244e676). Driver experiments/new/kl/randrun.py; results experiments/new/kl/results/rand10k.global.part{0-3}.csv (one row per game).
Global rule: 10,000 / 10,000 games verified (harness/verify.py, both players' strategies) and regions = Oink zlk (no tl fallback needed);
max 11 pivots primal, 11 dual.
