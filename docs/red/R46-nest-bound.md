# R46: on 𝒞^1P a phase is polynomial unless the nesting depth NEST is unbounded (L-RED box 15; produced on Opus 5.5)
Status: READING. One combinatorial lemma is PROVED for d = 1 and CONJECTURED for d ≥ 2, with brute-force data; unrefereed.
Written 2026-10-19 00:55Z (date -u). Target: Lead box-15 order (2): the exact obstruction to a compounding counter on 𝒞^1P.
Inputs:
- Lemma LEX and the outcome order of OUTCOME-MONO-1P (L-ALG GAP-A-M §35b, §28e: readings, unrefereed, LEX mechanically checked
  by b12_lexchk.py);
- NEST as defined in experiments/red/tcpert/carryclimb.py nest() (R41 §1);
- EMPTY-REC (R42 §2).

## 1. The DTL side: the K-constraint (reading, from LEX)
Fix a q-phase of G ∈ 𝒞^1P. Let P = (p_1, …, p_{S−1}) be the first changed depth-0 positions of its transitions.
Claim (K): for every position p, among the transitions lying strictly between two consecutive transitions at positions < p (or
before the first, or after the last), at most K have position p. Here K is the length of the longest chain of the per-context
state order: K ≤ (n + 2)²(n + 1) = O(n³).
Proof.
- A transition whose first changed position is p0 leaves states 0 … p0−1 unchanged. So inside such a window, the states at
  positions < p never change, and R_p (= G′ minus the pieces at positions < p) is one fixed set.
- A transition at p has its first difference at p. By LEX its state at the common context R_p strictly rises in the per-context
  order. Transitions at positions > p do not touch state_p.
- So inside the window, state_p goes through a strictly increasing chain in the per-context order: at most K steps.
- That order is: the outcome (−1 with rising emptying round e ≤ n + 1; for equal e, prevV ⊆; then stable with V* ⊆), then the
  piece ⊆ for an equal outcome. Its longest chain is at most (n + 2)·(n + 2)·(n + 1). □

## 2. The combinatorial side: sequences with bounded NEST
Lemma L-NEST(d). Let P be a sequence over positions {0, …, m−1} that satisfies the K-constraint and has NEST(P) ≤ d. Then
|P| ≤ F(m, d, K), where F is polynomial in m and K for every fixed d. Conjectured form: F ≤ (2Km)^d.
- PROVED for d = 1: |P| ≤ 2Km (the brute force gives exactly K(2m − 1)).
  - NEST 1 means that, for every q, two consecutive occurrences of q have only shallower positions between them.
  - (Retirement) If some position deeper than q follows an occurrence of q, then q never occurs again. Otherwise that deeper
    position would lie between two consecutive occurrences of q.
  - Group the occurrences of each symbol q into RUNS: maximal blocks of occurrences of q with nothing between them. By the
    K-constraint a run has length ≤ K, because nothing shallower separates the occurrences inside it.
  - Two consecutive runs of q are separated by a nonempty GAP, and every element of the gap is shallower than q.
  - Map each gap to the index of its first element y. This map is injective: an index is the first element of at most one gap,
    namely the gap of the symbol at the preceding index.
  - y is shallower than q, and q occurs after y. So y retires, and the occurrence of y at that index is y's LAST occurrence.
  - Hence #gaps ≤ #last occurrences ≤ m, so the number of runs is at most #symbols + #gaps ≤ 2m, and |P| ≤ 2Km.
  - The brute force below gives exactly K(2m − 1) for K = 1, 2, 3. □
- d ≥ 2: CONJECTURED. Exhaustive search (experiments/red/xctx/comb/nestK.py: all sequences satisfying the K-constraint with NEST ≤ d, DFS,
  sequence-length cap above every reported value) gives maximum lengths:

| K | d | m = 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 1 | 3 | 5 | 7 | 9 | 11 |
| 2 | 1 | 2 | 6 | 10 | 14 | 18 | |
| 3 | 1 | 3 | 9 | 15 | 21 | | |
| 1 | 2 | 1 | 3 | 7 | 13 | 21 | |
| 2 | 2 | 2 | 8 | 24 | | | |
| 1 | 3 | 1 | 3 | 7 | 15 | 29 | |
| 1 | 4 | 1 | 3 | 7 | 15 | 31 | |

  - d = 1 is exactly K(2m − 1). d = 2 with K = 1 is m² − m + 1, quadratic.
  - Once d ≥ m − 1 the maximum is 2^m − 1: the binary counter, whose position sequence has NEST m − 1.
  - The growth is polynomial of degree d in m for fixed d, and exponential only when d grows with m. These are data on small m,
    not a proof.

## 3. Consequence (reading, conditional on L-NEST(d) for d ≥ 2)
On 𝒞^1P, every q-phase satisfies S − 1 ≤ F(n, NEST, K) with K = O(n³). With the conjectured form this gives
S ≤ (2Kn)^NEST + 1 = n^{O(NEST)}.
- NEST 1 phases are PROVED (reading) to have S ≤ 2K(n + 1) + 1 = O(n⁴): a chain has at most n + 1 positions, so m ≤ n + 1.
- Hence a super-polynomial family on 𝒞^1P must have UNBOUNDED NEST, that is, the binary-counter signature. Each counter level must
  re-rise at a fixed context with deeper re-rises in between: (N1) of R45 at depth NEST.
- Known values: the class best is NEST 3 (nest3_n20, nest3_n24, R45). The two-player best is NEST 4 (nest4_n80, R41), but LEX
  fails in two-player games (L-ALG §36b), so §1 and this bound do not apply there.
- What this does NOT give: a polynomial bound for 𝒞^1P. A family whose NEST grows like log n would escape it.
- Exact obstruction statement for the counter: (NEST-BOUNDED) "NEST is bounded by a constant on 𝒞^1P" would imply GAP-A on
  𝒞^1P, given LEX and L-NEST. A counter must violate it.

## 4. Box-15 climb data on R45's (N3b) events (experiments/red/xctx/resetclass.py)
- A PRODUCTIVE RELEASE is an outcome rise at position l (fixed R_l) that returns vertices to lower positions, after which a tangle
  containing a returned vertex is learned below l before the next change at ≤ l. It is a reset that is not plain extension.
- By SAME-CTX (iii), a release (a vertex leaving piece_l at a fixed R_l) requires an outcome rise at l.
- Corpus: 0-2 productive releases per phase (vrall_viol_n20 1, nest3_n24 2).
- Climbs on (#productive releases, NEST, S), with growth to n ≤ 50, ran 00:12-00:50Z (date -u): best 6 productive releases at
  n 23 (stable order) and 4 at n 24-26. NEST stays 3, S 12-17. No growth with n was seen.
