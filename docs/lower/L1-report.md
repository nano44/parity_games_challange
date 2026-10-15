# L1 report: data, lemmas and the state of target T-L1 (L-LOWER, 2026-10-15; unrefereed)

Statement and model: docs/lower/L1-statement.md (Def. 1.3-1.4, restrictions R1-R6). Code: experiments/lower/ (README there).
Everything below is L-LOWER's own work unless a source is named; nothing is a result in the sense of CLAUDE.md.

## 1. Data (one-player Büchi, B_1(n) = minimal number of Cpre gates; exact)
| n | B_1(n) | minimal depth | 2n−2 | n^2 (Lemma 2.3) | method |
| --- | --- | --- | --- | --- | --- |
| 1 | 0 | 0 | 0 | 1 | SAT on Q_1 |
| 2 | 2 | 2 | 2 | 4 | SAT on Q_2; BFS over partitions agrees |
| 3 | 4 | 4 | 4 | 9 | SAT on Q_3 (UNSAT at 3 on the full quotient); BFS finds no program of depth ≤ 3 |
| 4 | 6 | 6 | 6 | 16 | SAT with CEGAR on Q_4 (48062 classes); UNSAT at 5 on a successor-closed subset; witness verified on all of Q_4 |
| 5 | see §4 | ≥ 8 (Lemma 2.1') | 8 | 25 | CEGAR against all 916·10^6 five-vertex games (experiments/lower/cegar5.py) |
Q_n = bisimulation quotient of all pointed one-player Büchi games with ≤ n vertices (L1 Lemma 1.5 makes this sound):
|Q_1..4| = 2, 14, 442, 48062. Two-player Büchi: minimal depth 2n−2 for n ≤ 3 as well (|Q| = 4, 76, 5164).
Restricted minima at n = 4: chain programs reading only (P_2, previous gate): 6; reading the two previous gates: 6;
complement-free (monotone) programs: 8 (n = 3: 5; n = 2: 2).
The reference programs: Lemma 2.3's unfolding agrees with Zielonka on every Büchi game with ≤ 4 vertices (two-player n = 4:
every 13th of 12.96·10^6) and on all 916·10^6 one-player games with 5 vertices (vectorized reference, itself checked against
Zielonka on all 810000 games with 4 vertices); ANP's symmetric SLP (Transfer 2.4, S trees, 357 Cpre gates at n = 4, d = 2)
agrees with Zielonka on all 74088 games with 3 vertices and priorities {0,1,2} and on 649604 of the 4-vertex ones.

## 2. The depth is Θ(n): two lemmas (proofs written out; to be refereed)
**Lemma A (= L1 Lemma 2.1').** Every program solving one-player Büchi on ≤ n vertices has depth ≥ 2n − 2 (n ≥ 2).
Witness pair: the n-cycle with one P_2 vertex rooted n − 2 steps before it, versus the same path ending in a P_1 self-loop.

**Theorem B (depth upper bound).** If (v, G) is winning and (v', G') losing, both one-player Büchi games with ≤ n vertices, then
their depth-(2n − 1) bisimulation types differ. Hence W_E is a union of depth-(2n − 1) types, and a program of depth 2n − 1
(and, a priori, exponential cost) exists. For n ≤ 4 depth 2n − 2 is exact (table).
Proof. Replace G by the bisimulation quotient of its part reachable from v (≤ n vertices, same types, same W_E), so distinct
vertices of G have distinct full types; since partition refinement on ≤ n vertices stabilises after ≤ n − 1 rounds, distinct
vertices of G already have distinct depth-(n − 1) types. (*)
Suppose the depth-D types of (v, G) and (v', G') agree for some D; we show D ≤ 2n − 2 (so the depth-(2n − 1) types differ).
Pick a P_2 vertex u on a cycle reachable from v, a shortest path v = x_0 → ... → x_a = u and a shortest cycle u = y_0 → y_1
→ ... → y_{ℓ−1} → y_0 (the y's distinct). Let π = x_0 ... x_{a−1} (y_0 ... y_{ℓ−1})^ω. By the forth condition of depth-D
bisimulation there is a path π' = x'_0 ... x'_D in G' with x'_t ≡_{D−t} π(t) for all t ≤ D.
Claim 1 (freshness; losing G'): if p is a P_2 position of π' then x'_s ≠ x'_t for all s < p ≤ t. Otherwise x'_s → ... → x'_p →
... → x'_t = x'_s is a closed walk through a P_2 vertex reachable from v', and repeating it gives an infinite path with
infinitely many P_2, contradicting that v' is losing.
Claim 2: if t < t' ≤ D − n + 1 and x'_t = x'_{t'} then π(t) = π(t'). Indeed both x'_t and x'_{t'} are ≡_{D−t'} to π(t) and π(t')
respectively, so π(t) ≡_{D−t'} π(t') with D − t' ≥ n − 1, and by (*) π(t) = π(t').
Claim 3: if t < t' and π(t) = π(t') then π has a P_2 position in (t, t']. The case t < t' < a is impossible (the stem is a
shortest path, so its vertices are distinct). Either both t, t' ≥ a, so t' − t is a positive multiple
of ℓ and the window (t, t'] contains a position ≡ a (mod ℓ), i.e. a visit to u; or t < a ≤ t' (a stem vertex equal to a cycle
vertex), and position a ∈ (t, t'] is the visit to u.
Claims 1-3 give: x'_0, ..., x'_{D−n+1} are pairwise distinct vertices of G', so D − n + 2 ≤ n, i.e. D ≤ 2n − 2. ∎
Consequence: no lower-bound argument for B_1 that only uses depth (Lemma 1.6, locality) can give more than 2n − 1. A super-
linear bound must count gates, not depth. Conversely Theorem B gives no program of small cost: the number of depth-(2n−1)
types is astronomically large.

## 3. What the minimal programs look like (n ≤ 4)
Every minimum is attained by a chain s_1, ..., s_{2n−2} with s_i = ◇ f_i(P_2, s_{i−1}) and an arbitrary output function of
(P_2, s_1, ..., s_{2n−2}). Example n = 4 (experiments/lower/min_window1_n4.json, printed by show.py):
s1 = ◇P2, s2 = ◇(P2 ∨ s1), s3 = ◇s2, s4 = ◇s3, s5 = ◇(P2 ∧ s4), s6 = ◇s5, out = a 19-term DNF over (P2, s1..s6).
Reading: s_1..s_4 = "a P_2 at distance 1 / ≤2 / 2..3 / 3..4"; s_5 = "a path with P_2 at position 1 and at position 4 or 5";
s_6 = the same one step later. The output combines distance-profile bits with two-visit bits; in a losing graph with ≤ 4
vertices every path visits P_2 vertices in pairwise fresh segments (Claim 1), so "P_2 at positions 1 and 4..5" forces 5
vertices. These are pigeonhole witnesses tuned to n = 4; L-LOWER has NOT found a uniform family of O(n)-gate programs.

## 4. n = 5 (in progress; exact statements only)
Method: experiments/lower/cegar5.py and cegar5b.py. SAT candidates on Q_3 plus counterexample games, verified on Q_4 and on
ALL 916·10^6 one-player Büchi games with 5 vertices (vec5.py reference, itself equal to Zielonka on all games with ≤ 4
vertices). UNSAT on a successor-closed subset is a proof of impossibility; a candidate counts only after the full sweep passes.
| program class | k = 8 | k = 9 | k = 10 | k = 11 |
| --- | --- | --- | --- | --- |
| window-1 chains (gate i reads P_2, s_{i−1}) | UNSAT (136 games, cegar5_k8_w1.json) | UNSAT (154 games) | UNSAT (562 games) | running |
| window-2 chains | running | | | |
| unrestricted | running | | | |
So chain programs, which attain the minimum 2n − 2 for n ≤ 4, need ≥ 11 gates at n = 5 (2n − 2 = 8): the chain family does
not extend linearly. B_1(5) itself (≥ 8 by Lemma A) is open until the unrestricted run ends.

## 5. State of T-L1 and proof routes
- The hoped-for lower bound T-L1 (B_1(n) = ω(n)) is NOT supported by the data: B_1(n) = 2n − 2 exactly for n ≤ 4, attained by
  chain programs. If B_1(5) = 8 the conjecture B_1(n) = 2n − 2 (linear; T-L1 false) becomes the working hypothesis and the
  lane's job turns into constructing the uniform O(n) program (which would be a positive separation result in the opposite
  direction: non-adaptive anonymous programs solve one-player Büchi with O(n) Cpre gates, matching the adaptive O(n)).
- If B_1(5) > 8, the first super-linear step appears at n = 5 and the witness subset (UNSAT core games) is the place to look
  for the obstruction family.
- Obstruction for the two standard methods: (i) depth/locality is capped at 2n − 1 by Theorem B; (ii) two-party
  communication (CDHL) is capped at Θ(n) bits on the Reduction 3.9 graphs (L1 §4).
