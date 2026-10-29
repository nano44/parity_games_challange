# N5-DEPTH (box 61): bounding I directly. CONJECTURE I-CUBIC (data), Lemma DEPTH-COUNT (proved), and the value-prefix potential is DEAD on switchbestexp
L-NEW successor 34 (Opus 5.5), D14 / D18, Lead reading L40. Lead's brief 2026-10-29 18:18Z (BOX 61 (a), (b)). Written 2026-10-29 from
18:34Z (date -u). Working note, unrefereed, not a TARGET.md claim. SF-POLY OPEN; G-N5-TIME untouched. Labels: PROVED (lane) / DATA /
READING / CONJECTURE / OPEN / DEAD.
Symbols as in N5-PV-box60.md §3:
- greedy one-player segments; SBC_G; Theorem SF-RED-G (PROVED, lane; no LOC needed).
- SF-RED-R is not used here. Where it is cited elsewhere, it carries ASSUMPTION LOC.
- I = N5-SF's two-sided iteration count.
- All runs from the SPEC S3 default start, NOT the corpus's pinned starts.
- Tool: experiments/new/box59/coarse.py. Logs: box59/depth_all.txt (the 719 games of sbcg.lst) and box59/depth_hard.txt (14 games:
  friedmannsubexp / fearnleysubexp N = 2..5 from L-LIT's T47 generator, switchbestexp 5..8, fc_9 / fc_10). 733 games, 0 timeouts.

## Summary
- (a) DATA. Over all 733 games: max I/n³ = 0.031 and max I/(n²(n + m)) = 0.011, both on n4_maxph_1, a 4-vertex game with I = 2.
  Over games with n ≥ 20: max I/n³ = 0.0021 and I/(n²(n + m)) = 0.00067 (red/n5inj/instances/theta_thc24.pg, n 24, I 29, sha1 12a303c9…).
  - fcN: I ≈ N³ with n = 25N + 10, so I/n³ → 1/15625. Measured: 1.0·10⁻⁴ at N = 9 and 10.
  - Max I/n = 4.86 (fc_8).
  - CONJECTURE I-CUBIC (OPEN): I ≤ n³/32 for every game and start. The constant comes from the tiny game; for n ≥ 20 the data say
    ≤ n³/476. fcN shows the degree 3 is attained.
- (b) The step-structure ingredient. By SF-RED-G, I < 2(1 + SBC_G)(n + m + 1)(n² − n + 1). So the question is a potential that rises at
  every F-relevant boundary and is poly(n)-bounded.
  - Lemma DEPTH-COUNT (PROVED, lane): records of depth ≤ K number at most n²(n + 1)^K over the whole run.
  - Theorem DEPTH-BOUND (PROVED, lane; conditional): if every F-relevant segment contains a transition of depth ≤ K, then
    SBC_G ≤ 2n²(n + 1)^K. K = O(1) would give SF-POLY; K = O(log n) a quasi-polynomial bound.
  - DATA:
    - fcN: needed depth 5 for N = 3..10, constant.
    - switchbestexp N = 5..8: 14, 17, 20, 23 (+3 per N, about n/9).
    - fearnleysubexp N = 2..5: 3, 6, 6, 12.
  - DEAD: any constant- or log-depth value-prefix potential (instance switchbestexp_8, sha1 7082e724…). This is where T48's barrier
    bites, now on the F-relevant changes themselves.

## 1. Depth, records, and the count (PROVED, lane)
- Path sets. Fix a vertex v. Along the distinct-σ sequence Ξ_j(v) is ⊴-non-decreasing (R15 (a), as in P-N5-SF SF-RED (b)). Within an
  epoch of constant cycle node, valuations compare by the path set P (SPEC S1: «then P by the signed weight») and then by length.
- The P-order is lexicographic on χ(P) ∈ {0, 1}^V. Coordinates are taken in relevance order (rank, descending), and each coordinate
  is oriented: for an even vertex 1 beats 0, for an odd vertex 0 beats 1. The signed weight Σ ±2^rank orders P exactly so.
- key_K(Ξ) := (cycle node, the K most relevant vertices of P), or all of P if |P| < K.
- Depth of a change Ξ → Ξ′:
  - 0 if the cycle node changes;
  - else 1 + #{common vertices of P, P′ more relevant than d}, where d := the most relevant vertex of P Δ P′;
  - n + 1 if P = P′ and only the length changes.
- The depth of a transition j is the minimum depth over all vertices v.
- A change of depth ℓ ≤ K changes key_K: d is the ℓ-th element of P or of P′.

Lemma DEPTH-COUNT. For every v and K ≥ 0, key_K(Ξ_j(v)) changes at most n · Σ_{i ≤ K} C(n, i) ≤ n(n + 1)^K times along the run. Hence
at most n²(n + 1)^K transitions have depth ≤ K.
Proof.
- The cycle node's reward strictly rises at each cycle-node change (SF-RED (b)'s argument), so there are at most n epochs.
- Within an epoch, fix a value κ of key_K and let S_κ be the set of path sets P with key_K(P) = κ.
  - If |κ| = K, then S_κ consists of the P that agree with κ on every coordinate of rank ≥ r, where r is the rank of κ's least relevant
    element. That is a fixed prefix of χ.
  - If |κ| < K, then S_κ = {κ}.
- Either way S_κ is convex in the lexicographic order: anything between two vectors sharing a prefix shares it.
- A non-decreasing sequence meets a convex set in a contiguous block of indices. So each κ occupies one block, and key_K changes at most
  (#κ) − 1 times per epoch. The number of κ is ≤ Σ_{i ≤ K} C(n, i).
- Sum over the ≤ n epochs, then over the n vertices. □
Theorem DEPTH-BOUND (conditional). Suppose every greedy segment ending at a boundary contains (including its boundary transition) a
transition of depth ≤ K. Then SBC_G ≤ 2n²(n + 1)^K. With SF-RED-G: I < 2(1 + 2n²(n + 1)^K)(n + m + 1)(n² − n + 1).
Proof. Assign each boundary a transition of depth ≤ K in its segment. Consecutive segments share only their common endpoint, so each
transition is assigned at most twice. Then apply DEPTH-COUNT. □
- The theorem uses MONO-XI and injective rewards. That is exactly the "coarse records with fine changes absorbed into stretch length"
  route of the brief, made exact: depth K = 1 is the coarse record (cycle node, top vertex).

## 2. DATA: the needed depth (coarse.py; the depth of a segment = the minimum over its transitions; DEPTH(game) = the maximum over segments)
| game | n | I | SBC_G | DEPTH |
| --- | --- | --- | --- | --- |
| fc_3 / fc_5 / fc_7 / fc_9 / fc_10 | 85 / 135 / 185 / 235 / 260 | 121 / 346 / 743 / 1360 / 1753 | 8 / 24 / 48 / 80 / 99 | 5 / 5 / 5 / 5 / 5 |
| fcobsP_3 | 90 | 121 | 8 | 5 |
| switchbestexp_5..8 | 135..210 | 364, 412, 456, 489 | 48, 55, 59, 74 | 14, 17, 20, 23 |
| fearnleysubexp_2..5 | 38..110 | 6, 9, 12, 15 | 3, 5, 6, 9 | 3, 6, 6, 12 |
| friedmannsubexp_2..5 | 44..170 | 8, 11, 14, 18 | 5, 9, 12, 16 | 3, 3, 3, 6 |
| so_sor5_n24 | 24 | 22 | 8 | 2 |
| corpus maximum ≤ n (719 games) | | | | 23 (switchbestexp_8) |
- Coarse records alone (K = 1) are DEAD as the potential. fc_5 has 24 F-relevant boundaries, but only 15 transitions change any
  vertex's (cycle node, top vertex); fc_7: 48 against 20. The top of most paths is the sink's p, which the low bits never move.
- In 8 games some segment has only length changes (depth n + 1). There no path-set potential rises at all; for example
  experiments/new/box59/out/rnd/r132_n80.pg.
- So DEPTH-BOUND with constant K is DEAD: on switchbestexp it would need K = 3N − 1 ≈ n/9, i.e. a bound n^{Θ(n)}. Its I is small
  (≈ 2.3n), so the obstruction is to the POTENTIAL, not to polynomiality.
- Obstruction:
  - switchbestexp_8 (sha1 7082e7242d82) has an F-relevant segment in which no vertex's top-22 path prefix moves.
  - Every function of the top-22 prefixes of all valuations is therefore constant across a step at which F's frame matters.
  - This is the binary counter's low bits (the box-55 leapfrog vertex), decided at depth Θ(N).

## 3. Where T48's barrier bites, and what lemma would be needed (READING)
- T48: monotone values plus an argmin allow argmin changes decided arbitrarily deep, n^Ω(log n) of them in parametric shortest paths.
  §2 shows the same depth growth on the F-RELEVANT changes of a real lower-bound family, not only on observers.
- Any potential built from per-vertex valuation prefixes, of any depth o(n), therefore fails, with switchbestexp as the instance.
- A polynomial proof needs a potential that is NOT a function of valuation prefixes. Two shapes remain, both OPEN:
  - (i) A potential on Even's strategy itself, read through LATENCY. Each F-relevant change must be paid for by an F-step that switches
    an edge whose head's value rose in the PREVIOUS step. Per vertex, the number of such "fresh-head" switches would need a bound;
    none is known.
  - (ii) A bound on SBC_G through the one-player runs G*_a. Each segment is a prefix of N5's run on G*_a. If successive G*_a are
    "nested" (each frame's run is a continuation of the last), a total-order argument on one-player optima could bound the number of
    frames. This needs a monotonicity of σ̄ across frames, and (M1) of box 55 says σ̄ is NOT monotone in R15's order. So (ii) needs a
    different order.
- The lemma that would close (a) given (b): CONJECTURE SBCG-QUAD (OPEN), SBC_G ≤ c·n² on every game. With F-relevant segments of
  length ≤ n + m, as on fcN, where LAM = 0 and R17's λ-phase bound applies to G*_a, this gives I = O(n²(n + m)), i.e. I-CUBIC up to
  the m factor.
  - DATA: max SBC_G/n² = 0.0295 (red/xing/instances/j10_n24.pg, n 24, SBC_G 17); fcN gives (N² − 1)/(25N + 10)² → 1/625.
  - Max SBC_G/n = 0.708, also j10_n24.

## DONE / FINDINGS / NEEDS
- DONE: box59/coarse.py; box59/hard61.lst, out/snare/ (T47 snare instances, switchbestexp 5..8 copies, fc_9 / 10); depth_all.txt,
  depth_hard.txt; this note; check.sh "Box 59" pins coarse.py on fc_3 (DEPTH 5).
- FINDINGS:
  (1) DATA: I/n³ ≤ 0.031 on 733 games (≤ 0.0021 for n ≥ 20). CONJECTURE I-CUBIC: I ≤ n³/32. fcN attains the degree.
  (2) PROVED (lane): Lemma DEPTH-COUNT and Theorem DEPTH-BOUND. A constant needed depth would give SF-POLY; O(log n) would give QP.
  (3) DEAD: coarse records (K = 1) on fcN; constant- and log-depth value-prefix potentials on switchbestexp (needed depth 14, 17, 20,
  23 for N = 5..8). That is the T48 barrier on F-relevant changes.
  (4) OPEN: a potential that is not a function of valuation prefixes, (i) or (ii); CONJECTURE SBCG-QUAD.
- NEEDS: none from the owner.
