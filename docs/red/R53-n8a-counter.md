# R53: a super-polynomial pivot family for N8a under switch-all (Koh-Loho SI, perfect universal tree) (box 21; L-RED successor 11; produced on Opus 5.5, D15 / L37)
Status: DATA plus a stated law, unrefereed. 2026-10-23 02:26Z (date -u). Target (Lead, 02:08Z): N8a = Koh-Loho strategy iteration over the
perfect (n, d/2)-universal tree (arXiv 2108.13338, PDF sha256 21ee0e4336252f7e6e1fcba7cb305b03f0950799610f324235eed5ecba15c9a9, opened
2026-10-23), as implemented by L-NEW in experiments/new/kl/kl.py at l-new 4fd179c8, run UNMODIFIED, rules frozen in docs/new/N8a-kohloho.md §2.
Fidelity: I re-read kl.py against the paper §2.1 (p-truncation lengths), §2.2 (feasibility, violated / tight, Tighten, lift), Algorithm 1
(µ ← min L(T); τ1; least fixed point above µ after each pivot; admissible = violated arc of an Odd node). No issue found; L-NEW's own check
(Algorithm 3 = naive least fixed point on 850 calls) stands. The counter below uses only Tighten's base-n successor, which is the paper's
perfect tree (Section 2.1: M = {0, …, ℓ−1}, ℓ = n leaves per branching).

## 1. The instances (experiments/red/kl/instances/; every row: kl.py --sol, then experiments/new/check_sol2.py = Oink zlk OK, strategies verified)
| instance | sha1 | n | d (kl) | switch-all: primal / dual pivots | global: primal / dual pivots |
| --- | --- | --- | --- | --- | --- |
| klcount_n16 (climb, 02:21Z) | b5269084cdc44a51c9f9f370dea4832fff3de45d | 16 | 18 | 4 / 16,387 = 4·16^3 + 3 | 3 / 8 |
| klcount_n18_base = n16 + 2 isolated self-loops, priorities 10, 11 (no new value) | a57b23ce0d07f4beb99d658895fef5181562e691 | 18 | 18 | 4 / 23,331 = 4·18^3 + 3 | 3 / 8 |
| klcount_n18_lvl = n16 + 2 isolated self-loops, priorities 33, 34 (two new top values) | 9ffdb16158b70547ac05d4ad0944254a55fabe0a | 18 | 20 | 4 / 419,907 = 4·18^4 + 3 | 3 / 8 |
| klglobal_n16 (climb, global rule) | 179b2cd059a54c3afe6a461c2dfb6c369537b416 | 16 | 20 | 6 / 81 | 11 / 134 |
- Both padded counts were PREDICTED from the law below before the runs and matched exactly.

## 2. The mechanism (trace: logs/klcount_n16_dual_all_trace_head_tail.txt, from experiments/red/kl/ktrace.py, which calls only kl.py's own
functions and asserts the same iteration count as kl.solve)
- Dual side (Odd of the dual = Even of the game pivots), switch-all. After 7 set-up pivots, a period of 4 pivots repeats forever:
  (1: 4→3, 4: 9→13, 6: 4→14, 11: 6→3), (4: 13→1, 11: 3→6), (4: 1→9), (1: 3→4, 6: 14→4) on dual nodes 1, 4, 6, 11.
- Each period raises the labels of the cycle nodes by ONE in label component 2 (ξ_15 of the dual, h = 10): the Tighten at the dual's
  odd-priority node 14 (priority 15) is the base-n successor of the 3-component prefix (ξ_19, ξ_17, ξ_15), with carry. The labels run
  0.0.0 → 0.0.15 → 0.1.0 → … → 15.15.15 (base 16) and then overflow to ⊤ (iterations 16,385-16,387).
- Why the least fixed point does not shortcut it: the lapping cycle is never entirely in G_τ. Under switch-all each pivot moves an Odd node
  to the admissible arc with the LARGEST Tighten value, which leaves the cycle open, and the ratchet (µ only increases, Theorem 3.1's proof)
  keeps the previous lap's labels. The strategy τ repeats with period 4 while µ climbs (the paper's own remark that τ may recur).

## 3. The law and the family
- Law (DATA on 3 instances, 2 of them predicted): dual pivots under switch-all = 4·n^L + 3, where n = number of vertices (= the branching ℓ
  of the perfect (n, d/2)-universal tree) and L = number of tree levels from the top down to the counting priority (L = 3 on klcount_n16).
  - Adding vertices that create no new priority value raises only the base: 4·16^3 → 4·18^3 (klcount_n18_base).
  - Adding two vertices with two new top priority values adds one level: 4·18^3 → 4·18^4 (klcount_n18_lvl).
- Family F_k := klcount_n16 + 2k isolated self-loop vertices with priorities 33, 34, …, 32 + 2k: n = 16 + 2k, L = 3 + k, and by the law
  pivots(F_k) = 4·(16 + 2k)^{3+k} + 3 = n^{Θ(n)}: SUPER-POLYNOMIAL in n (and in the input size). Verified members: k = 0, 1 (above).
  k = 2 would be 4·20^5 + 3 = 12.8 M pivots (about 3.5 h of kl.py at ~1 ms per pivot); not run in this box.
- What it kills: N8a with the switch-all rule ('all', the control rule of N8a-kohloho.md §2) on the perfect universal tree. It does NOT
  touch the 'global' rule: 8 dual pivots on all three counter instances (the one-sided optimum closes the lapping cycle at once).
- What it says about the paper: nothing against its theorems. The paper bounds the iterations by n·|L(T)| = n·n^{d/2} and leaves pivot
  rules open; this family shows the perfect-tree bound is nearly attained (n^{L}, L ≈ d/2 − const) by a natural rule.

## 4. The global rule is killed too (2026-10-23 02:33Z, date -u)
| instance | sha1 | n | d (kl) | global: primal / dual pivots | switch-all: primal / dual |
| --- | --- | --- | --- | --- | --- |
| klglobal_n16 (climb, global rule, 02:21Z) | 179b2cd059a54c3afe6a461c2dfb6c369537b416 | 16 | 20 | 11 / 134 = 8·16 + 6 | 6 / 81 |
| klglobal_n18_lvl = n16 + 2 isolated self-loops, priorities 29, 30 (new top values) | cb9004b7af4bbac31e4c9443229ac25bc241a7bc | 18 | 22 | 11 / 2,598 = 8·18^2 + 6 | see logs below |
| klglobal_n20_lvl2 = n16 + 4 isolated self-loops, priorities 29-32 | 0ffbeaf10ccfba071c5db9c07c4c56ae417a01b9 | 20 | 24 | 11 / 64,006 = 8·20^3 + 6 | see logs below |
- All rows: kl.py --sol, check_sol2.py = Oink zlk OK, strategies verified. Both padded counts were PREDICTED and matched exactly.
- Mechanism (logs/klglobal_n16_dual_global_trace_head_tail.txt): after 8 set-up pivots, a period of 8 pivots on dual Odd nodes 4, 5, 7, 8,
  10, 11 repeats; each period raises the TOP label component by one (0 … 15, then ⊤): L = 1 on klglobal_n16. The global rule solves Odd's
  one-player game against Even's counterstrategy σ read off µ, but σ itself moves with µ, so the one-sided optimum is re-taken every
  period and the cycle stays open across periods.
- Family G_k := klglobal_n16 + 2k isolated self-loops with new top priorities: n = 16 + 2k, L = 1 + k, dual pivots = 8·(16 + 2k)^{1+k} + 6
  = n^{Θ(n)}: SUPER-POLYNOMIAL. Verified members k = 0, 1, 2.
- So BOTH frozen rules of N8a-kohloho.md §2 have super-polynomial pivot families on the perfect universal tree. The common cause is the
  perfect tree's base-n Tighten: a lapping cycle that the rule keeps open counts through every leaf of the tree's top L levels, and every
  extra priority value on any vertex, even an isolated one, adds a level.
