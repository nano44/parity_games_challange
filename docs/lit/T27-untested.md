# T27: untested approaches to solving parity games in polynomial time, screened (L-LIT, 2026-10-24)

Asked by the Lead at 12:58Z (date -u), under D16 / Lead reading L38 (2)c. Scope:
- a source-checked scan;
- no runs and no contact.

Every source cited was opened by L-LIT in this session; sha256 values are in notes/L-LIT.md "Sources opened". Page conventions:
- Ohlmann's thesis: printed page = PDF page − 2.
- Ohlmann 2603.07555: printed page = PDF page.

"L-LIT reading" marks interpretation. Priors are L-LIT estimates, not results.

**Recommendation: C1, Ohlmann's symmetric recursive algorithm (arXiv 2603.07555), run on the parity-induced mean-payoff game.**
- It is new (8 March 2026, v1 only, no citers).
- It is untested by the fleet.
- It is not a single-trajectory improvement method, so lesson L1 (c-lane-synthesis.md) does not apply.
- Its author conjectures subexponential and gives no analysis (§7 p.19).
- A one-page pseudocode exists (§5 p.11), so the kill test fits in 2 h.
- Prior that it survives step 2: about 0.15.

## 0. Exclusion list (built first; nothing below re-proposes it)
| source | excluded approaches |
| --- | --- |
| docs/RESULTS.md R1-R18 | strong separators with vertex priorities (R1); psolB class (R2); original Random-Facet (R3); A_DTL / DTL and its GAP-A, GAP-C lemma packets (R4-R14, R16); N5 SSI-GLOBAL (R15, R17, R18) |
| docs/RESULTS.md DE1-DE34 | 2511.03752 attractor claim (DE1); weak-separator target T1 (DE2); psolC (DE3); SI single-switch rules MSF, LSF, steepest, most-improved, RAR / Random-Facet, subgame-optimal start (DE4, DE6-DE8); nested fatal attractors C1-C3 (DE5); DTL proof-route potentials and hypotheses (DE9-DE21, DE24, DE27); IncreasingDiscountPI (DE22); priority annealing (DE23); IPM on the JS LCP (DE25); entropic homotopy (DE26); Koh-Loho tree SI, all rules (DE28-DE30); Sherali-Adams lifts of ACYC (DE31); LP-guided peeling (DE32); ACYC + escape cuts (DE33); N5-HT (DE34) |
| docs/lit/BARRIERS.md B1-B21 | every framework there; in particular all VJ, discounted and LCP pivoting rules (B8-B13, B18, B20), IPMs (B15, B21), value iteration over universal trees/graphs (B1, B2), non-adaptive universal attractor decomposition (B3) |
| docs/new/ N1-N11 + README | N0-S5, N0-S6 (Zadeh, Cunningham under renumbering); N3 Blackwell path; N4 / N9d tropical shadow-vertex simplex; X1 scaled energy VI; N8b SA of strategy + potential MIP; N8c N5 with hysteresis; N9c simulation pruning; N8-screen S1-S5 (Schewe's LP, least-recently-considered SI, Schewe's optimal SI, adaptive progress-measure trees, discounted variants); N9-screen §5 (max-atom k-consistency, bounded registers); c-lane-synthesis (f): SA / SOS on ACYC + ESC1 (proposed there, so not re-proposed here) |
| docs/si/DEAD.md | S1-S7 as above |

Found during the scan and excluded, with the reason:
- **Lahlou-Truffet, "A polynomial time algorithm to solve the max-atom problem", arXiv 2106.08854.**
  - v2 (27 Aug 2024) is WITHDRAWN; the comment credits T. van Dijk with finding the errors.
  - The successor, arXiv 2408.14256 (abstract opened), claims no P result. For positive MAPs, "looking for all solutions requires
    the enumeration of all elementary circuits".
  - Not an audit target.
- **Di Stasio-Vardi, "Rabin games revisited", arXiv 2610.15495, §5 Theorem 5.3 (PDF p.13) and the comparison table (PDF p.14); GandALF 2026, EPTCS 454.8.** The memoized recursion
  costs 2^O(n)·poly(n, M, k). It is exponential by its own bound, and Zielonka-like for parity (B5).
- **Żyndul, "Lasso games", arXiv 2610.15480 (GandALF 2026).** Abstract: "lasso parity games are equivalent to weak parity games"
  and polynomial. That is a different game, not a method for parity games.
- **Piedeleu, "The algebra of parity games", arXiv 2501.18499.** An equational axiomatisation (Thm IV.1, IV.6), with no complexity
  bound. Compositional solving costs grow with interface width.
- **Hausmann, arXiv 2404.13687 (DAG fixpoint acceleration).** Speeds up acyclic substructures only; not a general bound.
- **Lapauw-Bruynooghe-Denecker, arXiv 2102.01440 (justifications).** Reconstructs Zielonka, priority promotion and tangle-style
  algorithms. All are known and exponential (abstract and §1).
- **Ohlmann thesis Ch. 11 (bi-progress measures, p.201 ff.).** = the Jurdziński-Morvan universal attractor decomposition (Thm 11.1, 11.2); B3.

## 1. C1 (rank 1): Ohlmann's ReduceGame on the parity-induced mean-payoff game
**(i) Object.**
- **Source.** P. Ohlmann, "A symmetric recursive algorithm for mean-payoff games", arXiv 2603.07555 v1 (sha256 292bde19…):
  - §3 p.5-7 (informal and formal presentation);
  - §5 p.11-12 (Algorithm 1 ReduceGame, plus ComputeZones, Reduced, PotentialReduction, BacktrackAllPaths, AttractMaxAndReduce;
    each subprocedure O(m));
  - Lemmas 4-7 (§4, correctness);
  - variants: §6.4 remembered potentials, §6.5 lazy version.
- **Input.** A game with integer edge weights and no zero cycles (§5: "All games are assumed without zero cycles").
- **Output.** (G−, G+, ϕ): the winning regions and a reducing potential.
- **One call ReduceGame(G):**
  1. Compute the zones. N = Min vertices with a negative edge, plus Max vertices with only negative edges; P is the dual. Stop if
     G is reduced.
  2. If |N| ≤ |P|, set F := N, with supΣ_N = 0 on N. Otherwise run the dual.
  3. Loop:
     - backtrack all paths into F;
     - H := G \ F;
     - (H−, H+, ϕ_H) := ReduceGame(H);
     - if H+ ≠ ∅ and a Min edge leaves H+ into F: add the escape vv′ minimising w(vv′) + supΣ_N(v′) − ϕ_H(v) to F (Lemma 5a);
     - if H+ ≠ ∅ and no Min edge leaves H+: Max-attract A ⊇ H+, recurse on G \ A and glue the potentials (Lemma 4);
     - if H+ = ∅ and H− ≠ ∅: add the maximising Max escape (Lemma 5b);
     - if H = ∅: apply the potential reduction by supΣ_N, then recurse on G′. Here N_{G′} and P_{G′} are both contained in N_G,
       and both are smaller than min(|N_G|, |P_G|) unless G′ is reduced (Lemma 7).
- **Parity instance.** Jurdziński's reduction (IPL 68(3) 1998, Thm 4, already verified in BARRIERS's table).
  - Compress priorities (order- and parity-preserving).
  - Give every edge out of v weight (−n)^{π(v)}, with Even = Max.
  - Every cycle's weight has the sign of its top-priority term, since n^p > (n−1)·n^(p−1). So there are no zero cycles, as §5
    requires.
- **Strategies (for verify.py).** In a reduced game:
  - Max on G+ takes a non-negative reduced edge staying in G+;
  - Min on G− takes a negative one (§2 zones; L-LIT reading, to be checked in the fidelity step).
- **Bit cost (TARGET §3).**
  - Weights have ≤ d·log2 n + 1 bits.
  - supΣ values and potentials are sums of at most n weights, so ≤ (d+1)·log2 n + O(1) bits.
  - Every operation is addition or comparison on such numbers. No big-number blow-up.

**(ii) Barriers.** L-LIT reading: outside every row, with B4/B5 the real risk.
- **B1-B3.** No automaton product and no value iteration. The values are computed by backtracking and escapes, never by walking
  a value domain. So the mean-payoff universal-graph bounds (CFGO 2104.05262 v8 Thm 7.5-7.6: size ≈ n·N) do not bound it.
  It is not a fixed-tree nested-fixpoint recursion (B3).
- **B8-B14, B18-B21.** Not strategy improvement, not pivoting, not discounted, not an IPM.
- **L1 (c-lane-synthesis, DATA reading).** Does not apply: progress is recursive, not one trajectory. This is c-lane-synthesis's
  "not touched (d)".
- **B4/B5, the risk.** It is a recursive attractor-style algorithm. §7 p.19: "One may be tempted to call it a mean-payoff analogue
  of Zielonka's algorithm ... however ours is more involved and differs from Zielonka's when executed on a parity game".
  - No theorem covers attractor recursions (B4).
  - The Zielonka families (B5: recursiveladder; B6: tc) are the natural killers.
  - The naive recursion bound is exponential: up to n calls on smaller games per level.
- **Literature status.** No upper or lower bound.
  - §1 p.2: "We believe that our algorithm is a candidate for a subexponential runtime, but we leave such an upper bound to
    future work".
  - §7 p.19: "So far, we haven't been able to analyse the algorithm in a meaningful way".
  - Semantic Scholar: 0 citers. arXiv: v1 only (checked 2026-10-24).

**(iii) Cheapest falsification test (< 2 h; L-NEW).**
1. Implement §5 Algorithm 1 and its subprocedures verbatim, with exact Python integers.
2. Freeze the variant before any run: base algorithm first, then §6.4 (remembered potentials) as a second run.
3. Fidelity: 300 random games (n ≤ 10), regions equal to Oink zlk, strategies verified by harness/verify.py.
4. Bench, counting total ReduceGame calls and total backtracking work:
   - tc N = 1..10 and recursiveladder (the Zielonka killers);
   - counter_qpt, switchallexp, switchbestexp;
   - the counter_* set.
5. Kill: growth in calls that is super-polynomial in n on any family, or any wrong region or strategy.

**(iv) Prior that it survives step 2: about 0.15.**
- Against: it is Zielonka-shaped, and tc / recursiveladder exploit exactly that shape.
- For: escapes are chosen by potential comparisons, which is information Zielonka discards.

## 2. C2 (rank 2): the GKK potential-reduction algorithm on the parity-induced game
**(i) Object.** Gurvich-Karzanov-Khachiyan 1988, in Ohlmann's symmetric presentation (thesis, Université Paris Cité 2021, sha256
a5c909cb…, Ch. 10 §3 p.179).
- Each iteration applies "the largest constant bi-safe potential" (§6.2 p.194).
- It stops when the arena is reduced (Fig. 10.4 p.179).
- Each iteration costs O(m) (§3 p.179).
- Thm 10.2 (p.179): iterations ≤ N + E⁺ + E⁻ + 1 ≤ nN + 1 and O(2^(n/2)), N = largest absolute weight. The O(2^(n/2)) bound is
  proved via alternating layers, Thm 10.4 and the proof on p.189.
- On the parity instance of C1, N = n^d, so the pseudo-polynomial bound is exponential. The question is the actual count.

**(ii) Barriers.**
- No barrier row covers GKK. It is symmetric and potential-based; Ohlmann calls it attractor-based (§3, p.179-180).
- The fleet has never run it: grep of docs, notes and experiments finds only binary hits.
- The literature has only empirical data on random games. Beffara-Vorobyov (LICS 2002 short presentation, title only, NOT opened)
  is reported in search results as ≈ (π/2)·n^(3/4) steps on random games. Thesis §6.3 p.194-196 compares GKK, ESL and AESL on
  random arenas only.
- Risk: L1. GKK is one trajectory of potentials. Each step moves by one constant δ, so a counter that forces small δ against
  weights of size n^d could make it climb. This is the X1 / small-progress-measure failure mode (docs/new README X1).

**(iii) Test.** Same harness as C1 (the potential-reduction subroutine is shared). Run tc, recursiveladder, counter_qpt and the
counter_* set; count iterations and the sizes of δ. Kill: super-polynomial iterations on any family.

**(iv) Prior: about 0.05.**

## 3. C3 (rank 3): alternating ESL (AESL), Ohlmann thesis Ch. 10 §6.2
**(i) Object.**
- ESL is Schewe's algorithm (Schewe CSL 2008, as presented in Lut08) recast as accelerated energy value iteration. Each iteration
  computes the SU⁺ update by a game version of Dijkstra (Thm 10.6, O(m + n log n), §6.1 p.190).
- AESL alternates SU⁺ and its dual SU⁻. It terminates when the potential takes only ±∞ values (§6.2 p.194).

**(ii) Barriers.**
- Asymmetric ESL is Schewe's globally optimal improvement in other words. Friedmann 0901.2731 §6 covers Schewe's variants (B8),
  so ESL alone is excluded.
- AESL is symmetric. It is not STV symmetric SI (footnote 9, p.194: "completely different"), so B11 does not apply, and no
  opened source gives a lower bound.
- Fatal for the gauntlet: §6.2 p.194: "we are not able to establish its termination ... (even over parity games)". Survival at
  step 2 would still leave step 4 open at its first lemma.
- L1 risk as in C2.

**(iii) Test.**
- Run AESL with a step cap of 10·n² and cycle detection on the potential vector.
- Kill: non-termination, a cap hit, or super-polynomial growth on the bench.
- Ohlmann's Python code is public (github.com/PierreOhl/parity_games_solving, thesis §6.3 p.194). It can serve as a reference
  after a fidelity check. NOT opened by L-LIT: reading only, no contact.

**(iv) Prior: about 0.04.**

## 4. C4 (rank 4, mathematical object, not an algorithm yet): priority-compressing parity separators
**(i) Object.**
- A deterministic parity automaton A over Σ_d with poly(n, d) states and k = O(log n) priorities, such that
  EvenCycles_{n,d} ⊆ L(A) and L(A) ∩ OddCycles_{n,d} = ∅.
- Then G ⊗ A is a parity game with k priorities and poly size. Jurdziński-Lazić (BARRIERS re-verification table: d = O(log n) is
  polynomial) would solve it in polynomial time.
- Correctness of the product reduction needs the separator to be good-for-games / deterministic, as in CDFJLP Prop. 3.2 for
  safety (L-LIT reading).

**(ii) Barriers.**
- Outside B1/B2 by acceptance type (B1 detail (ii): "acceptance beyond safety (parity separators with few priorities, open per
  §6)").
- R1 and B16 are about safety / DFA separators only.
- Neither CFGO 2104.05262 nor Colcombet-Fijalkow 1810.05106 v2 (opened; Thm 1-2 are for safety via universal graphs/trees) states
  a parity-acceptance bound.
- No opened source rules it out. L-LIT reading: the existence of such A would put parity games in P. That is evidence against
  existence, not a barrier.

**(iii) Test.**
- SAT search for the smallest deterministic k-priority separator, k = 2 (Büchi / co-Büchi), n ≤ 5, d ≤ 6.
- Compare its size growth with the safety separators of experiments/weak-sep/.
- This is L-STRUCT's lane: experiments/weak-sep/ owns the search code.

**(iv) Prior: about 0.02.**

## 5. Ranking
| rank | candidate | prior (step 2) | leverage | cost of kill test | main risk |
| --- | --- | --- | --- | --- | --- |
| 1 | C1 Ohlmann ReduceGame (2603.07555) | 0.15 | high: new, recursive, symmetric, unanalysed, poly bit size | ~1.5 h (one-page pseudocode) | Zielonka-type blow-up on tc / recursiveladder |
| 2 | C2 GKK on parity weights | 0.05 | medium | ~1 h (shares C1's potential code) | L1 small-δ climb |
| 3 | C3 AESL | 0.04 | low (no termination proof) | ~1 h | non-termination; L1 |
| 4 | C4 k-priority separators | 0.02 | very high if found | > 2 h (SAT); L-STRUCT | probably do not exist |

## Sign-off
- L-LIT recommends C1 for L-NEW's falsification box.
- No runs were made. No running-time claim is made (D1).
