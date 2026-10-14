# Referee report: L-STRUCT claim C1 (w(2,6) = 3 < 4 = s(2,6)), S1 Lemmas 1–3, and the E/S/V conventions

Referee: REFEREE. Date: 2026-10-14. Routed by the Lead 2026-10-14 19:26Z. Source: claude/l-struct 42dbbc2,
docs/struct/S1-statement.md and experiments/weak-sep/ (README.md, results/table.md, results/automata/*.json).

## Verdicts
| item | verdict |
| --- | --- |
| 1a. C1: a 3-state deterministic weak (2,6)-separator exists; no deterministic strong (2,6)-separator has < 4 states; so w(2,6) = 3 < 4 = s(2,6) in conventions E, S and V | **OK** (independently re-derived, section 1) |
| 1b. Side claim: the same 3-state automaton is a weak (3,6)-separator | **BROKEN** (two 3-vertex counterexamples, section 1.4; it also contradicts L-STRUCT's own table, w^V(3,6) = 6) |
| 1c. w^V(3,6) = 6 < 7 = s^V(3,6) | **OK** (section 1.5) |
| 2. Lemma 1 (regions) | **OK** (section 2.1) |
| 2. Lemma 2 (invariances, neutral letter) | **CHANGES**: (b)'s sketch misses the words with finitely many non-zero letters and needs d ≥ 2 (section 2.2, finding 1) |
| 2. Lemma 3 (shift) and the comparison with KV | **OK** as stated, with one note on the alphabet (section 2.3, finding 2) |
| 3. E/S/V definitions against CDFJLP, CFGO, KV | **OK**, one wording note (section 3, finding 3) |

## 1. C1 and the side claim: independent computation
Tools (mine, independent of L-STRUCT's wsep/ package; in docs/referee/scratch/): `wsepref.py` enumerates ALL graphs
with 1..n vertices (not maximal ones) in the three conventions, classifies each by brute force (a cycle with maximum
exactly p exists iff some p-edge (u,p,v) has a path v → u using labels ≤ p), prunes vertices without an infinite
continuation, and checks (W1) by product reachability, (W2) by acyclicity of the reachable non-sink product, and (S2)
on the automaton's reachable transition graph. `wsepsat.py` is my own SAT encoding (python-sat, CaDiCaL 1.5.3;
one-hot transitions, closure variables per graph, order-encoded ranks for (W2) and for (S2)), over inclusion-maximal
even/odd graphs computed by brute force; every SAT answer is re-checked by `wsepref.py` against all graphs.
`wsepE2.py` is a single pass over all 64⁴ = 16,777,216 edge-labelled multigraphs on 2 vertices (convention E).

### 1.1 The witness is a weak (2,6)-separator in every convention
δ(0,·) = [1,0,1,0,2,0], δ(1,·) = [2,1,⊥,0,⊥,0], δ(2,·) = [⊥,1,⊥,1,⊥,0] (letters 1..6, state 0 initial).
| convention | graphs with ≤ 2 vertices (even / odd / neither) | (W1) | (W2) |
| --- | --- | --- | --- |
| V | 126 / 114 / 90 | holds | holds |
| S | 534 / 438 / 1436 | holds | holds |
| E (all 16,777,216 multigraphs on 2 vertices, 15 s) | 28,545 / 16,257 / 16,732,414 | holds | holds |
(S2) fails: the reachable cycle 0 →5 2 →4 1 →4 0 has odd maximum, so the automaton is not strong (as L-STRUCT says).

### 1.2 No 2-state weak (2,6)-separator (so w = 3)
- Exhaustive: all 3¹² = 531,441 two-state automata over Σ_6 tested against every even and odd graph with ≤ 2 vertices
  in convention V: none is a weak separator. Since V-graphs ⊆ S-graphs ⊆ E-graphs (as word languages, Words(H) for a
  V-graph is the Words of the same graph read as an S- or E-graph), a weak separator in S or E is one in V, so w^S,
  w^E ≥ 3 too; with the witness, w^V = w^S = w^E = 3.
- My SAT encoding agrees: k = 2 weak V: UNSAT; k = 3 weak V: SAT, and the automaton it returns re-verifies.

### 1.3 No 3-state strong (2,6)-separator; a 4-state one exists (so s = 4)
- My SAT: k = 3 strong V: UNSAT; k = 3 strong S: UNSAT; k = 4 strong V: SAT (re-verified). As above, s^E ≥ s^S ≥ s^V ≥ 4.
- Universal-tree cross-check (the Lead's ask): by CFGO Thm 4.1 (smallest separating automaton = smallest universal
  graph, for positional, prefix-independent objectives with a neutral letter) + Lemma 6.8 (smallest
  (n, Parity(2h))-universal graph = smallest (n,h)-universal tree) + Thm 6.2 (parity qualifies) + S1 Lemma 2(b) (the
  neutral letter 0 can be dropped), s^E(2,6) = least size of a (2,3)-universal tree. CFGO's recursions (Prop. 6.10
  upper f, Prop. 6.11 lower g) give f(2,3) = g(2,3) = 4 (my re-computation; also (3,3): 7, (4,3): 13, matching
  L-STRUCT's table). Hand argument that 3 leaves do not suffice: a tree with 3 leaves ℓ1 < ℓ2 < ℓ3 has split levels
  s12, s23 and s13 = min(s12, s23), at most two distinct values, but the three 2-leaf trees of height 3 need splits at
  levels 1, 2 and 3; 4 leaves with splits 1, 2, 3 in a row suffice. So s^E(2,6) = 4.
- Upper bound 4 by witness: L-STRUCT's `strong_E_n2_d6.json` and `strong_S_n2_d6.json` (4 states each) pass (W1) in
  convention S over all graphs and (S2); `strong_V_n2_d6.json` passes in V; `strong_E_n2_d6.json` also passes (W1) and (S2)
  over all 16,777,216 E-multigraphs (so s^E(2,6) ≤ 4 by an automaton I verified myself). `weak_E_n2_d6.json` (the same
  3-state witness) passes (W1), (W2) over all E-multigraphs. `strong_S_n2_d6.json` fails (W1) in E on a graph with parallel
  edges, as expected for an S-only automaton (not a claim).
- Hence s^V = s^S = s^E = 4 and C1 holds in all three conventions. ✓

### 1.4 Side claim BROKEN: the witness is not a weak (3,6)-separator
Checked against all 74,088 vertex-labelled graphs with 3 vertices (convention V; V ⊆ S ⊆ E, so the counterexamples
refute the claim in every convention):
- (W1) fails: the even graph 0 →1 1 →1 2 →2 0 (a 3-cycle with labels 1, 1, 2; maximum 2). Its word (1 1 2)^ω: run
  0 →1 1 →1 2 →2 1 →1 ⊥ (δ(2,1) = ⊥). Rejected after four letters.
- (W2) fails: the odd graph 0 →2 1 →4 2 →5 0 (labels 2, 4, 5; maximum 5). Its word (2 4 5)^ω: run 0 →2 0 →4 0 →5 2
  →2 1 →4 0 →5 2 …, cycling through 0, 2, 1 for ever. Accepted.
This agrees with L-STRUCT's own table (w^V(3,6) = 6): no 3-state automaton can be a weak (3,6)-separator. The side
claim as routed is false; whichever text asserted it must be corrected.

### 1.5 w^V(3,6) = 6 < 7 = s^V(3,6): OK
- L-STRUCT's `weak_V_n3_d6.json` (6 states) and `strong_V_n3_d6.json` (7 states) pass my checker against all 74,088
  three-vertex and all smaller V-graphs ((W1), (W2), resp. (W1), (S2)).
- My SAT: k = 5 weak V (n ≤ 3): UNSAT (1.03M clauses, 15 s); k = 6 weak V: SAT, re-verified against all graphs;
  k = 6 strong V: UNSAT (9 s). Universal tree (3,3): f = g = 7, consistent with s^E(3,6) = 7 in the table.

## 2. Lemmas 1–3 of S1 §4
### 2.1 Lemma 1 (regions): OK
Statement: for a TARGET game G (max-parity, pr : V → {0..n}), edge letters π(u,v) = pr(u) + 2 ∈ {2..n+2} ⊆ Σ_{n+2},
and a deterministic weak (n, n+2)-separator A of convention V: v ∈ W_E(G) iff Even wins the chained-product safety
game G ⊳ A from (v, q0).
Re-derivation. (⇒) Let σ be a positional winning strategy for Even on W_E (TARGET §3 allows positional determinacy).
W_E is closed under σ and under all Odd moves, so the σ-subgraph on W_E is a vertex-labelled graph with ≤ n vertices
(labels pr+2) all of whose cycles have even maximum (otherwise Odd could follow that cycle forever and win). Every play
from v ∈ W_E consistent with σ has its word in EvenCycles^V_{n,n+2} ⊆ L(A), so the run never reaches ⊥: σ (with the
automaton's deterministic transitions) wins G ⊳ A from (v, q0). (⇐) If v ∈ W_O, Odd's positional winning strategy τ
on W_O gives an odd vertex-labelled subgraph with ≤ n vertices; every play consistent with τ from v stays in W_O and
its word is in OddCycles^V_{n,n+2}, hence rejected: the run reaches ⊥, Odd wins the safety game from (v, q0). By
determinacy the two cases are exhaustive. ✓ The chained product used is CDFJLP's (dynamics and ownership from G, the
automaton fed the letter of each move, safety condition = never ⊥), and the V convention suffices because the letter
of an edge depends only on its source. The letters {2..n+2} ⊆ Σ_{n+2}: correct (TARGET priorities are ≤ n).

### 2.2 Lemma 2 (invariances): CHANGES on (b)
(a) Monotone in n (more graphs to satisfy) and in d (a separator for Σ_{d+1} restricted to Σ_d is one for Σ_d, since
Σ_d-graphs are Σ_{d+1}-graphs with the same cycle parities). ✓
(b) Dropping the neutral letter 0 (CFGO alphabet [0,d]) changes neither w^E nor s^E. The direction [0,d] → Σ_d
(restrict the automaton; even/odd Σ_d-graphs are even/odd [0,d]-graphs) is immediate. The direction Σ_d → [0,d]
(extend by δ(q,0) = q): L-STRUCT's sketch "contracting 0-edges maps paths of even/odd [0,d]-graphs with ≤ n vertices
to paths of even/odd Σ_d-graphs with ≤ n vertices" covers the paths with infinitely many non-zero letters: contract
0-paths into the following non-zero edge; cycles keep their non-zero maximum; a 0-only cycle has limsup 0, i.e. is
even, so odd graphs have none and even graphs lose only even cycles; vertex count does not grow. It does NOT cover a
path of an even [0,d]-graph that is eventually all 0 (word u 0^ω, u finite): the extended automaton must not reach ⊥
on u, and u need not be a prefix of an infinite path of the contracted graph (the path may end in a 0-only cycle).
Repair: at the vertex x where the non-zero part of the path ends, add to the contracted graph a self-loop labelled 2
(even; it creates only the cycle consisting of itself); then u 2^ω is the word of an even Σ_d-graph with ≤ n vertices,
so A does not reach ⊥ on u. This needs an even letter, i.e. d ≥ 2 (CFGO has d even anyway). Odd [0,d]-graphs have no
eventually-0 paths. For strong separators (S2) over [0,d]: a word with infinitely many non-zero letters has the limsup
of its projection (0 is neutral) and the projection is accepted by A; an eventually-0 word has limsup 0, even. ✓ with
the repair.
(c) follows from (b). ✓

### 2.3 Lemma 3 (shift) and F5: OK, one note
Replacing every label p by p+1 flips the parity of every cycle's maximum, so it swaps even and odd graphs and maps
Σ_d-graphs to graphs with labels in {2..d+1}; the identity on automata (with letters renamed) gives the stated
equality between "accept OddCycles, reject EvenCycles over Σ_d" and "accept EvenCycles, reject OddCycles over
{2..d+1}". ✓ Comparison with KV (F5), checked against arXiv 1902.07175v3 §1.2 and §2.1: KV's automaton reads
(vertex, priority) pairs; "separates A from B" = eventually always in q_accept on A and never on B; KV's EvenCycles is
over game graphs with no parallel edges, loops allowed, every vertex with an out-edge, i.e. L-STRUCT's convention S;
Thm 2 is for "in time t" only. Taking ⊥ := q_accept (absorbing without loss of generality, since "eventually always"
and "ever reaches an absorbing state" coincide) turns a KV separator into a safety automaton that accepts
OddCycles and rejects EvenCycles: roles swapped, as F5 says. A Σ_d-automaton induces a pair-alphabet automaton of the
same size (ignore the vertex), so a KV-type lower bound would transfer to our setting through the shift; note the
shifted labels live in {2..d+1} ⊆ Σ_{d+1}, so the transferred bound is on separators over an alphabet of size d+1
(F5/Lemma 3 should say so).

## 3. The E/S/V conventions against the sources
- CFGO (arXiv 2104.05262v8, §2.1, read in the source): graphs are "edge labelled directed graphs", E ⊆ Q × C × Q a
  set of triples, so parallel edges with distinct colours are allowed; sinks allowed, paths are infinite for L;
  an automaton is a graph, deterministic = at most one c-edge per (q,c), missing edges reject, size = number of
  vertices (no sink state). Separating automaton: Ω^{|n} ⊆ L(A) ⊆ Ω (Def. in §3.3 of the source's reductions
  section), i.e. STRONG. Universal graphs §3.5, Thm 4.1 (smallest sizes coincide, under the three assumptions),
  parity §6: colours [0,d], d even, Lemma 6.1 (even cycles), Thm 6.2 (assumptions hold), Lemma 6.8 (trees = graphs),
  Thm 6.9, Props 6.10/6.11. All of L-STRUCT's citations check out; convention E and D4 (⊥ not counted) match CFGO.
- CDFJLP (arXiv 1807.10546v2, read in the source): alphabet Σ_d = {1..d}; "a (parity game) graph is called even if
  every cycle in it is even (i.e., the highest priority that occurs on the cycle is even)"; EvenCycles_{n,d} = words
  of infinite paths of even graphs with at most n vertices and d priorities; OddCycles analogous; (n,d)-separator and
  strong (n,d)-separator verbatim as in D5. The text says "directed graph" with "positive integers that label all
  edges" and nowhere fixes whether two edges between the same ordered pair may carry different priorities. D1's
  sentence "CDFJLP §2.1 give one priority per edge and E a set of edges, which is a sub-case" is a reading, not a
  quote; it is a safe one because C1's witness is checked in E anyway (finding 3).
- KV: convention S exactly (no parallel edges, loops allowed, out-degree ≥ 1), alphabet with vertex names (above).
- V = TARGET games with π(u,v) = pr(u)+2: correct, and V ⊆ S ⊆ E as classes of word languages, which L-STRUCT's F1
  uses (w^V ≤ w^E). ✓

## Findings
1. Lemma 2(b): the proof sketch omits eventually-zero paths; add the self-loop repair above (needs d ≥ 2).
2. Lemma 3 / F5: say that the shifted problem lives over {2..d+1} ⊆ Σ_{d+1}, so KV-type bounds transfer to alphabet
   size d+1.
3. D1: mark the CDFJLP multiplicity sentence as L-STRUCT's reading (the paper does not state it); harmless for C1.
4. The side claim (3-state automaton is a weak (3,6)-separator) is false; remove it wherever it appears.

## Gaps
- All three conventions are checked exhaustively for n ≤ 2 (V: 330 graphs, S: 2,408, E: 16,777,216); the lower bounds
  are exhaustive/SAT in V (the weakest class), which suffices for S and E.
- My SAT encoding has no formal proof; its UNSAT answers agree with the exhaustive 2-state enumeration (k = 2) and with
  the universal-tree value (k = 3 strong), and its SAT answers re-verify. L-STRUCT's UNSAT answers and mine come from
  two different encodings and graph enumerations.
- Nothing here is machine-checked beyond these runs; Lemmas 1–3 are refereed-only.
