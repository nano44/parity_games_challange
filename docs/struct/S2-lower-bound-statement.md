# S2: lower bound for deterministic weak separators, exact statement (L-STRUCT, 2026-10-14)

Status: statement only (TARGET.md §7e), written before proof work, after the Lead's direction (a) of 19:26Z. Vocabulary
and conventions: docs/struct/S1-statement.md (D1-D5; E = edge-labelled multigraphs, S = one label per pair, V = vertex
labels; for a TARGET game the letters are pr + 2 ∈ {2..n+2} ⊆ Σ_{n+2}). s^E(n,d) for even d is the least number of
leaves of an (n, d/2)-universal tree (S1 F2). Nothing here is claimed; T1 is the target, T2 the fallback.

## 1. Target theorem T1 (one tree level is all a weak separator can save)
For all n ≥ 1 and all even d ≥ 4, and each convention X ∈ {E, S, V}:
    w^X(n, d) ≥ s^X(n, d − 2).
Equivalently: every deterministic safety automaton over Σ_d that accepts every word of EvenCycles^X_{n,d} and rejects
every word of OddCycles^X_{n,d} has at least as many states as the smallest deterministic strong (n, d−2)-separator.

Consequence (with CDFJLP 1807.10546 Thm 5.1 for X = E, which bounds non-deterministic strong separators and hence s^E):
    w^E(n, d) ≥ C(⌊lg n⌋ + d/2 − 2, ⌊lg n⌋),
quasi-polynomial in the same regime as the strong bound (n^{lg(d/lg n) − O(1)} for d = ω(lg n)). It would answer the
question left open in CDFJLP §6 for deterministic automata, and give the first super-linear bound for unrestricted
(not time-bounded) weak separators (KV 1902.07175 p.6: "Even super-linear lower bounds for unrestricted separation
automata are not known"). For X = V it is a barrier for every algorithm of the form "solve the safety game G ⊲ A for a
fixed deterministic automaton family A_{n,d}" on TARGET games, by S1 Lemma 1 (refereed).

## 2. Fallback theorem T2 (constant-factor loss in n)
There is a constant c ≥ 1 such that for all n ≥ c, even d ≥ 2 and X ∈ {E, S, V}: w^X(n, d) ≥ s^X(⌊n/c⌋, d).
Same consequence with n replaced by n/c. Weaker than T1 in the data (it is trivial for n ≤ c) but may be what the
proof gives.

## 3. What the data say (experiments/weak-sep/results/table.md, L-STRUCT data, unrefereed, l-struct 42dbbc2 and later)
- T1 holds with equality at (2,5), (2,6) in E, S, V: w = 3 = s(2,4) = s(2,3). It holds strictly at (2,4) V (3 > 2),
  (3,5), (3,6) V (6 > 5), (3,6) E (7 > 5), (4,6) V (w ≤ 11 vs s^V(4,4) = 7; w^V(4,6) itself is open from k = 10).
  No computed cell violates T1 or T2. REFEREE-checked cell: C1 (762c598).
- Refuting instance for T1 would be a cell with w^X(n,d) < s^X(n,d−2); the first candidates are the open cells
  (4,6) E (needs w^E(4,6) < 8) and n = 5 (L-COMP).
- The naive mechanism is FALSE: "a weak (n,d)-separator restricted to Σ_{d−2} is a strong (n,d−2)-separator" fails,
  because weak separators with an odd simple cycle of maximum ≤ d−3 exist, even at minimum size ((3,6) V, 6 states,
  cycle maximum 3; experiments/weak-sep/probe_oddcycles.py). So T1 needs an argument that re-uses states, not a
  restriction.

## 4. Proof route to be tried (not started)
- Input: A deterministic weak (n,d)-separator; by Q3 (refereed lasso condition) every reachable odd simple cycle C and
  every path P from q0 satisfy: the least odd X-graph generating π(P)·π(C)^ω has more than n vertices.
- Step 1: CDFJLP's Lemma 5.1 extracts an (n, d/2)-universal tree from a strong separator through the quasi-orders
  defined by "resistance" (maximal number of p-letters on paths inside the ≤p sub-automaton), which is finite only
  because no reachable cycle has odd maximum (Lemma 5.2). Replace resistance by a quantity that is finite for weak
  separators: the number of p-letters on paths that are prefixes of words of EvenCycles^X_{n,d} (even-realisable
  paths). Odd cycles are then invisible as long as no even graph with ≤ n vertices can traverse them; the lasso
  condition is what controls when an even graph can.
- Step 2: show the extracted ordered tree embeds every tree with n leaves and height d/2 − 1 (T1) or every tree with
  n/c leaves and height d/2 (T2). The loss (one level, or a factor in n) is where the odd cycles enter.
- Dead-end record: the restriction lemma (§3) is a dead end by the probe; obstruction instance: the 6-state weak
  (3,6)-separator of convention V with an odd 3-cycle (probe_oddcycles.py 3 6 V 6 3).

## 5. Novelty (for L-LIT) and refereeing (for the REFEREE)
- L-LIT: check T1/T2 against the map. Known: strong bounds only (B1, B2); KV time-bounded (B16); CDFJLP §6 open.
- REFEREE: the statement T1 as written in §1, including the definition of s^X(n, d−2) for X ∈ {S, V} (no universal-tree
  formula there; it is the SAT-defined minimum, S1 D5) and the pr + 2 mapping for TARGET games.
