# R46: on 𝒞^1P a phase is polynomial unless the nesting depth NEST* is unbounded (L-RED box 15; produced on Opus 5.5)
Status: READING, unrefereed.
- PROVED (reading): S ≤ n^{O(NEST*)} on 𝒞^1P (§2b), given L-ALG's readings LEX and OUTCOME-MONO-1P.
- The variant L-NEST with the consecutive-pair NEST is PROVED for d = 1 and CONJECTURED for d ≥ 2 (§2).
Written 2026-10-19 00:55Z, §2b-§3 rewritten 01:03Z (date -u). TARGET.md diff: a statement about A_DTL's search count (gauntlet
step 4 objects) on a subclass; no definition changed; no M4 claim. Target: Lead box-15 order (2): the exact obstruction to a compounding counter on 𝒞^1P.
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

## 2b. L-NEST* (PROVED, reading): the monotone version
Definition. NEST*(Q) is defined like NEST, but over ANY two occurrences of p rather than consecutive ones. By monotonicity it is
enough to take the first and the last occurrence:
NEST*(Q) = 0 if Q is empty; otherwise max(1, max over p with first occurrence i0 < last occurrence i1 of 1 + NEST*(Q(i0, i1)|>p)).
- (M) NEST* is monotone under taking subsequences. Induction: a witness pair in the subsequence is a pair in Q whose gap contains
  the subsequence's gap.
- NEST ≤ NEST*, since a consecutive pair's gap is inside the first-last gap.
- NEST is NOT monotone under deletion: 412 counterexamples in 200,000 random single deletions; for example deleting the eighth
  element of [3,0,3,3,1,0,2,1,3,3,2,1] raises NEST from 2 to 3. That is why the induction below uses NEST*.
Lemma L-NEST*. Let P satisfy the K-constraint over m symbols. Let Q be a subsequence of P that is a concatenation of at most r
intervals of P, with NEST*(Q) ≤ d. Then |Q| ≤ F_r(m, d), where F_r(m, 0) = 0 and
F_r(m, d) ≤ m(r + m)K·(1 + F_{r+m}(m, d − 1)). Hence |P| ≤ (2(d + 2)m²K)^d.
Proof.
- Unroll the shallowest symbol. Let a_1 be the shallowest symbol of Q_0 := Q.
  - Each of the ≤ r intervals of P that make up Q_0 contains no symbol smaller than a_1, because Q_0 contains none and each interval
    is kept whole. So within one interval, the occurrences of a_1 lie in one window of a_1 in P, and there are ≤ K of them. In
    total a_1 occurs o_1 ≤ rK times.
  - Every inner segment I between consecutive occurrences of a_1 consists of symbols > a_1. By (M) and the definition,
    NEST*(Q_0) ≥ 1 + NEST*(I), so NEST*(I) ≤ d − 1. I is a contiguous piece of Q_0, hence a union of ≤ r intervals of P.
  - Delete the chunk from the first to the last occurrence of a_1 to get Q_1. It is a union of ≤ r + 1 intervals of P, it has no
    a_1, and by (M) NEST*(Q_1) ≤ d.
- Repeat with the shallowest symbol a_j of Q_{j−1}: o_j ≤ (r + j − 1)K, and the inner segments are unions of ≤ r + j − 1 intervals
  with NEST* ≤ d − 1. Each step removes one symbol, so after at most m steps the sequence is empty.
- Summing: |Q| ≤ Σ_{j≤m} o_j·(1 + F_{r+m}(m, d − 1)) ≤ m(r + m)K(1 + F_{r+m}(m, d − 1)).
- At depth i of the recursion, r ≤ 1 + i·m ≤ (d + 1)m. So each level contributes at most a factor 2(d + 2)m²K, and
  |P| ≤ (2(d + 2)m²K)^d. □
Brute-force sanity check: experiments/red/xctx/comb/neststar.py, K ≤ 2, d ≤ 2, m ≤ 5. Every maximum is far below the bound; for
example K = 1, d = 2 gives 1, 3, 7, 13, 19.

## 3. Consequence (reading; PROVED given L-ALG's LEX and OUTCOME-MONO-1P)
THEOREM (NEST*-BOUND). On 𝒞^1P, every q-phase with first-difference sequence P satisfies
S − 1 = |P| ≤ (2(d + 2)(n + 1)²K)^d, where d = NEST*(P) and K ≤ (n + 2)²(n + 1). So S ≤ n^{O(NEST*)}.
- The K-constraint is §1. A chain has at most n + 1 positions, so m ≤ n + 1.
- A super-polynomial family on 𝒞^1P must therefore have UNBOUNDED NEST*: NEST* = ω(1), since n^{O(d)} has to exceed every
  polynomial.
- This is exactly the binary-counter signature: the k-bit counter sequence has NEST* = k − 1 (for k = 3, [2,1,2,0,2,1,2] has
  NEST* 2).
- Measured NEST* (stable order): nest3_n20 3, nest3_n24 3 (= NEST), onep_fdkey_n20 2, vrall_viol_n20 1, onep_lagdist_D8 1.
  The class best is NEST* 3.
- The two-player best is NEST 4 (nest4_n80, R41). LEX fails in two-player games (L-ALG §36b), so §1 and the theorem do not apply
  there.
- What this does NOT give: a polynomial bound for 𝒞^1P. A family with NEST* = Θ(log n) would give n^{Θ(log n)}.
- Exact obstruction statement for the counter question on 𝒞^1P: (NEST*-BOUNDED) "NEST* ≤ c on 𝒞^1P for a constant c"
  IMPLIES polynomially many searches per q-phase on 𝒞^1P. With phases ≤ dominions + 2 (GAP-A-M §21c) and CTRL for the
  controller's searches, that is GAP-A (a polynomial search count) on 𝒞^1P. The converse is not claimed.
  - So a counter on 𝒞^1P must be a family with unbounded NEST*, and a proof of GAP-A on 𝒞^1P may go through bounding NEST*.

## 4. Box-15 climb data on R45's (N3b) events (experiments/red/xctx/resetclass.py)
- A PRODUCTIVE RELEASE is an outcome rise at position l (fixed R_l) that returns vertices to lower positions, after which a tangle
  containing a returned vertex is learned below l before the next change at ≤ l. It is a reset that is not plain extension.
- By SAME-CTX (iii), a release (a vertex leaving piece_l at a fixed R_l) requires an outcome rise at l.
- Corpus: 0-2 productive releases per phase (vrall_viol_n20 1, nest3_n24 2).
- Climbs on (#productive releases, NEST, S), with growth to n ≤ 50, ran 00:12-01:00Z (date -u): best 6 productive releases at
  n 23 (stable order) and 4 at n 24-27. NEST stays 3, S 12-20. No growth with n was seen.

## 1b. Post-pin notes on §1 (NOT signed; appended 2026-10-19 by L-RED successor 10, after the P-C1P pin 01d63d7)
§1 and §3 above are the exact pinned text (01d63d7) that both referees signed, with K ≤ (n + 2)²(n + 1). l-red 938cea58 had changed
the K line in §1 and §3 and the last sentence of §1's proof after the pin; CHECKER C19 flagged it, and that edit is reverted here.
The material it added is kept below, unsigned.
- Alternative count (successor 9, post-pin): ranks take ≤ n + 3 values (0, the emptying rounds 1 … n + 1, and stable n + 2); for a
  fixed rank V grows ≤ n + 1 times, and for a fixed outcome the piece grows ≤ n + 1 times; so the longest chain is ≤ (n + 3)(n + 1)².
- Referee counts (for the record, not new claims):
  - REFEREE-2 (docs/referee-2/R2-C1P.md §6): K ≤ (n² + n)·n ≤ (n + 2)²(n + 1).
  - REFEREE's correction note (docs/referee/R-C1P.md "Correction note (02:47Z ...)", referee 89fee50): its own earlier count was
    wrong in arithmetic; the correct count is REFEREE-2's, ≤ (n² + n + 1)·n ≤ (n + 2)²(n + 1) (result-0 outcome included); the
    verdict on §1 (SIGN) is unchanged; the post-pin value (n + 3)(n + 1)² is also a valid K, and neither value affects the theorem.
- Adversarial check of the input LEX (experiments/red/xctx/lexrand.py, the b12_lexchk.py test re-stated), 2026-10-19 01:09-01:15Z
  (date -u), successor 9:
  - 200,000 random class games per order (n 4-14): 1,741 and 1,734 pairs, 0 LEX violations.
  - All 230 class instances saved by box 15's climbs (long, nested phases): 12,940 pairs (stable) and 13,255 (oink), 0 violations.
  - L-ALG's own b12_lexchk.py on experiments/red/xctx/instances/: 245 pairs per order, 0 violations.
