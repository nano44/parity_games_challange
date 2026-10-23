# S4: structure of minimal deterministic weak separators, what holds on data (L-STRUCT, 2026-10-14)

Purpose: the record of the facts found while T3 (docs/struct/S3-statement.md) was attacked, each labelled by its
status. Everything below is DATA, UNPROVED unless marked otherwise; "all cells" means the enumerated cells listed with
each item. Code and results: experiments/weak-sep/ (commits 42dbbc2 table; 6614060, 6985a5a, 4237657 enumeration;
69a4938 rules; 283ebbc, a3c9c1c, 6c5e5e8 lemma tests). Vocabulary: S1 D1-D5; conventions E (edge multigraphs, the
literature's), S (one label per pair), V (vertex priorities = TARGET games, letters pr+2, 0 removed by S1 Lemma 2(b-V)).

## 1. Sizes
F1 (data, unproved beyond the cells; REFEREE-checked at (2,6) = C1). Table experiments/weak-sep/results/table.md.
 - w = s on every cell with d ≤ n+1: V (1,1), (1,2), (2,2), (2,3), (3,3), (3,4), (4,4) = 7, (4,5) = 10; E likewise
   through (4,4) = 8; S through (3,4). L-COMP (LRAT) agrees on (2,2), (2,3), (3,3), (3,4), (4,4) and on the TARGET
   alphabet n = 2, 3, 4 (2, 5, 7 = w^V(n,n)).
 - w < s only at d ≥ n+2: (2,5), (2,6) = 3 vs 4 (E, S, V; C1 refereed); (2,8) = 4 vs 5; (2,10) = 4 vs 5 (L-COMP, DE2);
   V (3,5), (3,6) = 6 vs 7; V (3,8) = 7 vs s(3,8) (strong open, ≥ 8). Fixed-n: w^V(2,d) = 4 for 7 ≤ d ≤ 12; w^V(3,d) =
   6, 7, 8 at d = 6, 8, 10.
 - Vertex priorities are cheaper for strong separators: s^V(4,4) = 7 < 8 = s^E(4,4); s^V(4,6) = 10 < 13 = s^E(4,6).
F2 (theorem, refereed-only, first referee 9bf5301): L4, s^V(n,n) ≥ (√n/(2 lg n))^{⌊½ lg n⌋−2} = n^{Ω(lg n)}
 (docs/struct/L4-proof.md: transfer lemma L4.1 + CDFJLP Thm 5.1). Awaits the second referee as part of the T3 package.

## 2. Odd cycles of weak separators (the refereed lasso condition S1 Q3 and its data)
F3 (refereed OK, T4 §3(c) as sharpened): every reachable odd simple cycle C and every path P from q0 give an accepted
 word π(P)·π(C)^ω that no odd X-graph with ≤ n vertices realises.
F4 (data): for every minimal weak witness with odd cycles at n ≤ 3 and (4,4), the least odd V-graph realising a lasso
 word has exactly n+1 vertices, except (3,6) V (n+2): tolerated cycles sit at W2's edge (results/lasso_analysis.md).
F5 (data): weak separators with odd cycles exist at d ≤ n+1 in E and V, at minimum size and above (E (2,3) k=3; V
 (2,3) k=3, (3,3) k=5, (3,4) k=5); so weak ≠ strong as objects even where w = s; T3 is a size statement only.
F6 (data): all-odd cycles occur (single odd self-loops, V (2,3) k=3), so any "even return edge" lemma needs a case split.

## 3. Rewiring weak to strong on the same states (results/sl8/)
F7 (data, exhaustive per cell up to BFS numbering, k = 6 cells capped at 5000): SL8-t holds with t ≤ 4 on E/V (2,2) k ≤ 4,
 (2,3) k ≤ 4, (3,3) k ≤ 6, (3,4) k ≤ 6; at MINIMUM size t ≤ 1 (E) and t ≤ 2 (V) (SL8-min). No weak separator without a
 strong rewire within the budget (which only re-checks T3 on these cells). t_max per cell: E 1, 3, 1, 1; V 2, 4, 4, 2.
F8 (data, 72 non-strong minimal witnesses, 106 odd simple cycles): one deleted even-letter transition kills ALL odd
 simple cycles in 71 of 72 automata (exception: the all-odd case); 104 of 106 cycles have an even "return edge" below
 their maximum whose deletion breaks every cycle through the cycle's maximal letter.
F9 (data, 58 even-letter working single rewires): necessary rule NR holds on all: with rank = CDFJLP's resistance tuple
 on A − R (smaller = deeper), rank(q) ≤ rank(new) < rank(old) or new = q. No sufficient deterministic rule: shallowest
 interval state 40/49, deepest 8/41, source 16/57, successor 6, predecessor and others 42 of 64 overall. The rewired
 letter is the smallest even letter of the cycle in 57 of 64.
F10 (data, refuted hypothesis): the D-tree of A − τ0 is NOT (n, ⌈d/2⌉)-universal in general (E (2,3) 2 of 3 fail;
 V (3,3) 8 of 11; V (3,4) 30 of 42; control on strong E witnesses passes); the even part of a minimal weak separator does
 not carry the universal tree.

## 4. The n = 2 mechanism (Fact M0 and its instance; elementary, proof in S3 §3, not refereed)
F11: in a word of OddCycles_n every window of n letters contains a factor with odd maximum, dually for Even; for n = 2:
 no two consecutive odd letters in even words, no two consecutive even letters in odd words (verified on the maximal
 graphs). The 4-state witnesses at (2,8), (2,10) tolerate only odd cycles with maximum d−1 whose lasso words need 3
 vertices ((9 4 8)^ω). This is why n = 2 says nothing about the diagonal.

## 5. Dead ends (instances in notes/L-STRUCT.md): T1 (S2, refuted at (2,10), DE2); restriction lemma; pruning lemma
(L5); L5'; SL5/SL5'; naive rewiring rule; D-A; D-C1; D-C2; D-HB2.
