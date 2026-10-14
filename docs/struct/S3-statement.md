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

## 2. Targets (mutually exclusive; the data cannot yet tell them apart)
T3-neg (no diagonal gain). For all n ≥ 1: w^V(n, n) = s^V(n, n). Consequence: deterministic weak separators give no
  algorithmic advantage over strong ones on TARGET games; the product class (i)-(iii) is bounded below by s^V(n,n). A
  barrier in TARGET terms needs in addition L4 below.
T3-pos (polynomial diagonal). There are a polynomial p and a deterministic algorithm that on input n outputs in time
  p(n) a deterministic weak (n, n)-separator of convention V with ≤ p(n) states. Consequence: by §1 an algorithm meeting
  TARGET §2 (then the gauntlet, TARGET §5). Weaker intermediate: w^V(n,n) ≤ p(n) without a construction (existence only;
  not an algorithm).
T3-mid (sub-quasi-polynomial but super-polynomial) is the remaining possibility; a statement there is premature.
L4 (needed for any V-barrier; open): s^V(n, n) is super-polynomial in n. CDFJLP Thm 5.1 covers E only; s^V ≤ s^E and
  s^V < s^E already at (4,4). The Parys-Wiącek remark that the necessity proof "does not apply" for vertex priorities
  (docs/lit/BARRIERS.md B1 fine print) is the obstacle; L-LIT to check whether any source bounds s^V from below.

## 3. The fixed-n mechanism (structural, non-algorithmic), stated so it can be tested and refuted
H1 (saturation in d). For every n there is D(n) such that w^V(n, d) = w^V(n, D(n)) for all d ≥ D(n); write F(n) for
  this value. Evidence: w^V(2, d) = 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4 for d = 2..12 (d = 11 not run), so D(2) ≤ 7,
  F(2) = 4 if H1 holds, while s^V(2, 2h) = h + 1 → ∞ (REFEREE S2 §0). In E: w^E(2,8) = w^E(2,10) = 4.
  Test: w^V(3, d) for d = 8, 10, 12, 14 (w^V(3,6) = 6, w^V(3,8) = 7; d = 10 running). H1 is refuted at n = 3 if
  w^V(3,d) keeps growing; L-COMP's w(2,d) up to d = 20 tests it at n = 2.
Why n = 2 is degenerate (verified on the maximal graphs, experiments/weak-sep): in an even 2-vertex graph no two
  consecutive letters are odd (two consecutive odd edges form a 2-cycle or a loop with odd maximum), and in an odd
  2-vertex graph no two consecutive letters are even. Every word of EvenCycles_{2,d} has each odd letter immediately
  followed by a larger even letter, and dually for OddCycles. The 4-state witnesses (2,8), (2,10) exploit this: their
  only odd simple cycles have maximum d−1 and lasso words such as (9 4 8)^ω that no 2-vertex odd graph realises. Even
  if H1 holds for all n, F(n) ≥ W(n), so it says nothing about the diagonal unless F(n) is also computed.
H1 is NOT an algorithmic statement: for TARGET games d ≤ n + 1 < D(n) is the expected regime.

## 4. Decisive data (L-COMP's cells, in order of value)
1. W(5) and S(5): a strict inequality refutes T3-neg; equality extends the diagonal pattern to n = 5.
2. w^V(3, d), d = 10, 12, 14: tests H1 at n = 3 (my cheap runs, caps).
3. W(6), S(6) if feasible.
A refutation of T3-pos is not available from finite data; its support can only come from a construction.

## 5. Calibration
- Everything above the diagonal (n = 2, d ≥ 5; n = 3, d ≥ 5) is about letters a TARGET game of that size cannot have.
  The only algorithmically meaningful numbers so far are W(n) = S(n) for n ≤ 4.
- A polynomial W(n) would contradict nothing known (S1 F3, F5 are strong or time-bounded), but no mechanism for it is
  visible in the data: the weak savings so far come from odd cycles whose lasso words need more than n vertices, and
  on the diagonal the solver found none.
