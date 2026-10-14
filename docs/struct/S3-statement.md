# S3: the diagonal w^V(n,n) and the fixed-n saturation of weak separators (L-STRUCT, 2026-10-14)

Status: statement only (TARGET.md §7e), written after DE2 killed S2's T1. Goes to L-LIT (novelty) and the REFEREE
(statement) before any proof or construction work. Vocabulary: docs/struct/S1-statement.md (D1-D5, conventions E/S/V,
Lemmas 1-3 refereed). Lead's framing (20:09Z): the algorithmic question is the diagonal, because a TARGET game with n
vertices has priorities in {0..n}, which after the shift by 2 and S1 Lemma 2(b) means the automaton must be a weak
(n, n)-separator of convention V (REFEREE S2 finding 3). Fixed-n growth in d is algorithmically irrelevant; it is kept
here only as the mechanism that produced the weak < strong cells.

## 1. The quantity that matters
D6. The diagonal: W(n) := w^V(n, n) and S(n) := s^V(n, n) (S1 D5 minima; letters = TARGET priorities, 0 removed by
S1 Lemma 2(b)). An algorithm of the product class ((i)-(iii) of S2 §1 as fixed by the REFEREE) correct on all TARGET
games with ≤ n vertices has |A| ≥ W(n) and running time ≥ n·W(n). Conversely (S1 Lemma 1, refereed, plus linear-time
safety-game solving) a deterministic weak (n,n)-separator A of convention V, computable in time t(n), solves every
TARGET game with n vertices and m edges in time O(t(n) + (n + m)·|A|) and outputs the regions (positional strategies
follow from the safety strategy, to be checked in the gauntlet).

Data (L-STRUCT, SAT + checker, unrefereed except C1; experiments/weak-sep/results/table.md):
| n | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| W(n) = w^V(n,n) | 1 | 2 | 5 | 7 | open (L-COMP) |
| S(n) = s^V(n,n) | 1 | 2 | 5 | 7 | open |
| s^E(n,n) (for comparison) | 1 | 2 | 5 | 8 | open |
On the diagonal weak and strong coincide on every computed cell. The weak < strong cells all lie above the diagonal
(d ≥ n + 3): (2,5), (2,6), (2,7..12), (3,5), (3,6), (3,8).

## 2. Target T3 (Lead's framing 20:23Z, option (ii) with the explicit f the data allow; (i) is the case d ≤ n)
T3. For all n ≥ 1 and all d with 1 ≤ d ≤ n + 1:   w^V(n, d) = s^V(n, d).
  In words: on and just above the TARGET range, deterministic weak separators of convention V are no smaller than
  strong ones. The case d ≤ n (TARGET alphabet after S1 Lemma 2(b)) is the Lead's option (i); f(n) = n + 1 is the
  largest threshold consistent with the data (gaps at (2,5) = n+3 and (3,5) = n+2; equality at (2,4) = n+2 and at
  every cell with d ≤ n+1). Consequence: W(n) = S(n); the product class (i)-(iii) of S2 §1 gains nothing from
  weakening, and every known quasi-polynomial product algorithm's size bound is tight for its class exactly where
  algorithms live. The quasi-polynomial reading needs L4. M3 status if proved and refereed: extends the separation
  barrier (B1) to deterministic weak separators on the algorithmic range; Lead to rule, L-LIT to check novelty.
T3-pos (the opposite, M4 route; stated so the refutation of T3 has a name). There are a polynomial p and a
  deterministic algorithm that on input n outputs in time p(n) a deterministic weak (n, n)-separator of convention V
  with ≤ p(n) states. Consequence: by §1 an algorithm meeting TARGET §2, then the gauntlet (TARGET §5). A single cell
  with w^V(n,d) < s^V(n,d) and d ≤ n + 1 refutes T3 and is the first evidence for T3-pos.
L4 (needed for any V-barrier; open): s^V(n, n) is super-polynomial in n. CDFJLP Thm 5.1 covers E only; s^V ≤ s^E and
  s^V < s^E already at (4,4) (7 vs 8) and (4,6) (10 vs 13). The Parys-Wiącek remark that the necessity proof "does not
  apply" for vertex priorities (docs/lit/BARRIERS.md B1 fine print) is the obstacle; L-LIT to check for any source.

Data for T3 (all cells with d ≤ n + 1 computed so far; L-STRUCT unrefereed, L-COMP with LRAT-verified UNSAT at
value−1, CryptoMiniSat agreement and re-checked witnesses, claude/l-comp 8d9697b experiments/sat-hard/results/cells.md):
| cell (V) | w | s | source |
| --- | --- | --- | --- |
| (1,1), (1,2) | 1 | 1 | L-STRUCT |
| (2,2), (2,3) | 2, 3 | 2, 3 | both |
| (3,3), (3,4) | 5, 5 | 5, 5 | both |
| (4,4), (4,5) | 7, open | 7, open | both at (4,4) |
| TARGET alphabet {2..n+2}, n = 2, 3, 4 | 2, 5, 7 | 2, 5, 7 | L-COMP; equals w^V(n,n) as S1 Lemma 2(b) predicts |
No cell with d ≤ n + 1 violates T3. Decisive next cells: (4,5) V (both), (5,5) V, (5,6) V. Above the threshold the
equality fails: (2,5), (2,6), (2,7..12), (3,5), (3,6), (3,8), (3,10) (w^V(3,10) ≥ 8 > ... s^V(3,10) open).

## 3. Mechanism: why the gap appears only when d is large against n (structural core; hypotheses, testable)
Fact M0 (elementary, to be written up with S3's proofs). In a word of OddCycles^X_{n,d}, every window of n + 1
  consecutive letters contains a factor whose maximum is odd (n + 1 edges visit a repeated vertex, the closed part is a
  cycle, its maximum is odd); dually every (n+1)-window of a word of EvenCycles^X_{n,d} contains a factor with even
  maximum. For n = 2 this is "no two consecutive odd letters in even words, no two consecutive even letters in odd
  words" (verified on the maximal graphs). These are local constraints, independent of d.
Fact M1 (refereed lasso condition, S1 Q3). A weak separator may keep a reachable odd simple cycle C exactly when the
  lasso words π(P)·π(C)^ω are unrealisable by odd graphs with ≤ n vertices; the cheap filter is |P| + |C| > n.
Hypothesis H2 (where the saving comes from). The strong minimum pays one universal-tree level per odd letter
  (s(2,2h) = h + 1; in general the (n, d/2)-universal tree). A weak separator can merge the levels of the odd letters
  that an n-vertex graph cannot "count" against each other: with ≤ n vertices a graph realises at most n distinct
  letters per cycle structure (V: at most n letters in the whole word), so for d ≫ n most letters are, for every
  single graph, either absent or interchangeable, and the separator exploits this with odd cycles of the kind M1
  allows (all witnesses: cycles through high even letters, e.g. (5 4 4)^ω, (9 4 8)^ω, (7 2 4 2)^ω). For d ≤ n + 1 every
  letter can occur with every other inside one n-vertex graph, so nothing can be merged: this is T3's content.
  Test of H2: minimal weak witnesses at gap cells should have odd simple cycles only through letters ≥ some threshold
  that grows with n; refuted if a gap cell has a minimal witness whose odd cycles all lie below n + 1.
Hypothesis H1 (saturation in d; non-algorithmic). For every n there is D(n) with w^V(n, d) = w^V(n, D(n)) for all
  d ≥ D(n). Evidence: w^V(2, d) = 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4 for d = 2..12 (11 not run); E: w^E(2, 8) = w^E(2,10) =
  w^E(2,12) = 4. At n = 3: w^V(3,6) = 6, w^V(3,8) = 7, w^V(3,10) ≥ 8 (k = 7 refuted), so H1 is not yet visible at n = 3;
  L-COMP's w(2,d) to d = 20 and my w^V(3,d) for d = 10..14 test it. H1 says nothing about the diagonal.

## 4. Decisive data (L-COMP's cells, in order of value)
1. (4,5) V, then (5,5) V and (5,6) V: any strict inequality refutes T3 (and names the first algorithmic gap).
2. w^V(3, d), d = 10, 12, 14 (mine, cheap, capped): tests H1 and, with the odd-cycle probe, H2.
3. (6,6) V if feasible.
A refutation of T3-pos is not available from finite data; its support can only come from a construction.

## 5. Calibration
- Everything above the diagonal (n = 2, d ≥ 5; n = 3, d ≥ 5) is about letters a TARGET game of that size cannot have.
  The only algorithmically meaningful numbers so far are W(n) = S(n) for n ≤ 4.
- A polynomial W(n) would contradict nothing known (S1 F3, F5 are strong or time-bounded), but no mechanism for it is
  visible in the data: the weak savings so far come from odd cycles whose lasso words need more than n vertices, and
  on the diagonal the solver found none.
- Timestamps in L-STRUCT's earlier messages of this day ran ahead of UTC by up to 90 minutes (clock not consulted);
  the SHAs are authoritative.
