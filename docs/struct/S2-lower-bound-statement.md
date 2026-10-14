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
question left open in CDFJLP §6 for deterministic automata, and give the first super-linear lower bound for unrestricted
deterministic weak separators over the priority alphabet; the vertex-alphabet question of KV p.6 stays open (KV's
sentence concerns automata over (vertex, priority) letters, which can simulate priority-only automata, not conversely).
Second source stating the question open: Colcombet, Fijalkow, FoSSaCS 2019 (author PDF, irif.fr), footnote 5, p.14,
verbatim: "Note that there is a natural, more symetric, notion of (W, n)-separating automata in which the requested
inclusions are W|n ⊆ L(A) ⊆ ((W^∁)|n)^∁. However, nothing is known about this notion." That symmetric notion is weak
separation (D5) for W = Parity.
Pre-empting a misreading: Parys, CSL 2020 (LIPIcs.CSL.2020.32), p.2, writes "Czerwiński et al. [9] show a
quasi-polynomial lower bound for the size of a PG separator", and his Def. 3.2 defines a PG separator as one that
"accepts all words from PosEven_{n,d}, and rejects all words from PosOdd_{n,d}" (weak form, over his alphabet Σ_{n,d}),
with "strong PG separator" for the additional rejection of LimsupOdd_{n,d}. The sentence is a summary of CDFJLP, whose
Thm 5.1 is stated and proved for strong separators only (CDFJLP §3.3, §6); Parys himself notes right after Def. 3.2
that the quasi-polynomial-time separators "are actually strong PG separators (cf. [9, Section 4])". So no weak-separator
lower bound is asserted there, and T1 is not pre-empted by it.
For X = V it is a barrier for every algorithm of the form "solve the safety game G ⊲ A for a fixed deterministic
automaton family A_{n,d} reading priorities" on TARGET games, by S1 Lemma 1 (refereed). M3 status: Lead reading L6
(docs/DECISIONS.md) on D1, based on L-LIT's T5 verdict NEW.

Scope of T1 (what it does not cover). Automata over alphabets carrying vertex names or edges (KV's (vertex, priority)
letters; Parys's Σ_{n,d}) are outside: with vertex names, non-deterministic weak separation is easy (KV p.5), so any
proof of T1 must use determinism or the priority-only alphabet, or both. Non-deterministic weak separators are outside.
At d = 4, T1 reads w(n,4) ≥ s(n,2) = n, the trivial level; T1 has content only from d = 6 on.

## 2. Fallback theorem T2 (constant-factor loss in n)
There is a constant c ≥ 1 such that for all n ≥ c, even d ≥ 2 and X ∈ {E, S, V}: w^X(n, d) ≥ s^X(⌊n/c⌋, d).
Same consequence with n replaced by n/c. Weaker than T1 in the data (it is trivial for n ≤ c) but may be what the
proof gives.

## 3. What the data say (experiments/weak-sep/results/table.md, L-STRUCT data, unrefereed, l-struct 42dbbc2 and later)
- T1 holds with equality at (2,5), (2,6) in E, S, V: w = 3 = s(2,4) = s(2,3). It holds strictly at (2,4) V (3 > 2),
  (3,5), (3,6) V (6 > 5), (3,6) E (7 > 5), (4,6) V (w ≤ 11 vs s^V(4,4) = 7; w^V(4,6) itself is open from k = 10).
  No computed cell violates T1 or T2. REFEREE-checked cell: C1 (762c598).
- Monotonicity (Lead, 20:04Z, from L-COMP): a weak (n,d)-separator restricted to Σ_{d−2} is a weak (n,d−2)-separator
  (S1 Lemma 2(a)), so w^X(n,d) ≥ w^X(n,d−2). Hence T1 is automatic at every cell where w^X(n,d−2) = s^X(n,d−2); in
  particular w^E(4,6) ≥ w^E(4,4) = 8 = s^E(4,4), which L-COMP also confirmed directly (no weak (4,6) E-separator with
  ≤ 7 states; LRAT-checked, l-comp d818c50). T1's content sits where weak is already below strong two letters down.
- Decisive test cells (L-COMP computing): (2,8), where T1 needs w(2,8) ≥ 4 = s(2,6) although w(2,6) = 3; and V (3,8),
  where T1 needs w^V(3,8) ≥ 7 = s^V(3,6) although w^V(3,6) = 6. A SAT answer below those values refutes T1. The proof
  attempt waits for (2,8) and the REFEREE's statement check.
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
