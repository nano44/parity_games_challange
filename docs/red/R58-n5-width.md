# R58: improving-set width bounds every N5 run; what a kill must look like (box 26, L-RED successor 13; Opus 5.5, D15 / L37)
Status: one statement PROVED, conditional on the premise named in §2 (unrefereed). The rest is DATA and READING, each labelled.
Box 26 GO from the Lead at 2026-10-23 23:06Z (date -u).
Object: N5 = docs/new/N5-ssi-global.md SPEC S1-S5. The code is experiments/new/n5.py, run read-only and unmodified.
Target: R57 §6, a game that meets (R-a) and (R-b) at once.
Result: NOT KILLED. §2 proves that a run is polynomial unless the moving player usually has many improving edges at once. So R57's
(R-b) has to hold at wide improving sets, against ω(1) simultaneous honest improving edges, which sharpens O4 to O5 (§5).

## 1. First step as planned: N5's jump-ahead switches on the n = 32 seed, by edge class (DATA)
Tool: experiments/red/n5inj/jumpclass.py.
- A jump-ahead switch is an N5 switch that SSI would not make at the same state (n5tr's `*`).
- Edge classes come from SSI's own run from the same start: COUNTER = a choice edge that some SSI strategy uses; THREAT = a
  choice edge that no SSI strategy uses.

| game | SSI / N5 iterations | jump-ahead switches: COUNTER (of which re-used by N5) / THREAT | SSI-type switches: COUNTER / THREAT |
| --- | --- | --- | --- |
| sym_h16_s1 (n 32) | 29 / 55 | 14 (6) / 3 | 74 / 3 |
| sym_h12_s1 (n 24) | 24 / 34 | 16 (6) / 3 | 45 / 1 |
| DLM family 1, n = 8 (n 18; DLM start pair) | 509 / 8 | 38 (24) / 0 | 16 / 0 |

- 14 of the 17 jump-ahead switches on sym_h16_s1, and every one of DLM's 38, use counter edges. This extends R57 §6 C2 from DLM
  to the climbed symmetric games: a lane can guard (R-b) only on non-counter edges, and almost no jump-ahead switch uses one.
- On the climbed games N5 is SLOWER than SSI (55 vs 29 iterations), so a long N5 run does not need a long SSI run.
- Trace (n5tr.py) of sym_h16_s1: every jump-ahead switch occurs by iteration 22, except iterations 50-51. Iterations 29-55 are a
  ping-pong tail in which the mover has 1-2 improving edges and the other player waits. §2 shows why such a tail stays short.

## 2. Theorem W (PROVED, conditional on premise (P)): moves at narrow improving sets are polynomially few
Notation:
- Iσ is Even's improving-edge set (S2); Ξσ is Even's valuation vector (S1).
- m_E is the number of edges leaving Even vertices that have at least 2 successors; m_O is the same for Odd.
- N_k(m) = Σ_{j ≤ k} C(m, j).
- Odd's side is the same statement on G^d.

Premise (P), VJ00 "no improvement ⇒ maximum":
- Statement: let H be G with some edges leaving Even vertices deleted (every Even vertex keeps at least one). If σ has no
  improving edge in H, then Ξσ ⊵ Ξσ′ componentwise for every Even strategy σ′ of H.
- Source: VJ00 Lemma 5.8, direction "1 ⇒ 2". Per RESULTS R15 (G-N5T-3) this rests on VJ00's unproved Lemma 5.9 and
  Prop. 5.10, and both referees left it outside their packet. Every N5 output in the fleet depends on the same premise, and each
  output is verified separately.
- I did not open VJ00 myself. The citation is through RESULTS R15, whose referees opened the pdf (sha256 485a12de…).

Lemma 1 (same I ⇒ same valuation; PROVED given (P)).
- Statement: if Iσ1 = Iσ2 then Ξσ1 = Ξσ2.
- Proof:
  1. Let I = Iσ1 = Iσ2, and let H = G minus the edges of I.
  2. σ1 and σ2 are strategies of H, since (v, σi(v)) ∉ Iσi by S2. Every Even vertex keeps at least one edge.
  3. Ξσ in H equals Ξσ in G, because Ξσ depends only on σ and on Odd's edges, and H keeps all of Odd's edges.
  4. So the improving set of σi in H is Iσi minus I, which is empty.
  5. By (P), Ξσ1 ⊵ Ξσ2 and Ξσ2 ⊵ Ξσ1.
  6. ⊴ is a total order on valuations at each vertex, so Ξσ1 = Ξσ2. □
- DATA: the lemma has to cope with ties. With SPEC's valuations two successors often share a valuation (e.g. (10, ∅, 3) twice on
  sym_h8_s1), so the map σ ↦ Iσ is far from injective: 562 collisions among 1,152 Even strategies of sym_h8_s1.
- DATA: no collision ever had different valuation vectors.
  - Exhaustive check: sym_h8_s1, both players, 2 × 1,152 strategies: 0.
  - 2,000 random games (n 3-9, both players, every strategy): 41,111 strategies, 3,345 collisions, 0 with different
    valuations.
  - Tools: experiments/red/n5inj/injcheck.py and injbatch.py.

Lemma 2 (flat stretches; from RESULTS R15).
- Statement: along an N5 run, the distinct strategies σ that Even visits with one fixed valuation vector Ξ form one contiguous
  stretch of at most 2n(n−1)+1 strategies.
- Proof:
  1. Ξ never decreases along Even's sequence (R15 (a)), and ⊴ is antisymmetric. So if σ_a and σ_c have the same Ξ and a < b < c,
     then σ_b has that Ξ too.
  2. Within the stretch every change is Ω-flat, so φ rises strictly (R15 (b), (c)).
  3. φ is an integer with |φ| ≤ n(n−1). □

Theorem W (PROVED given (P); fleet-new as far as I know, L-LIT not asked).
- Statement: in every N5 run, and for every k, the number of iterations in which Even's strategy changes while |Iσ| ≤ k is at most
  (2n(n−1)+1)·N_k(m_E). The same holds for Odd with m_O.
- Proof:
  1. R15 (c): no strategy repeats, and every Even change (S4a or the S4c fallback) leaves from a distinct σ.
  2. Map each such iteration to Iσ. Every set in the image has at most k elements and is a set of choice edges, so the image has
     at most N_k(m_E) members.
  3. All strategies in one preimage have the same Ξ (Lemma 1), so they lie in one flat stretch (Lemma 2): at most 2n(n−1)+1 of
     them. □
- Nothing in the proof uses N5's selection. It holds for every run that applies a nonempty subset of Iσ, or of Iτ, at each step:
  SSI, any single-player SI rule, and N5.

Corollary W1 (width).
- Define the width w of a run as the largest |I| of the moving player over all its moves.
- Every iteration changes σ or τ (R15 (d)), so: #iterations ≤ (2n(n−1)+1)·(N_w(m_E) + N_w(m_O)).
- Consequences:
  - Width O(1) gives polynomially many iterations.
  - Width O(log n) gives n^{O(log n)} iterations.
  - A run of length T must spend all but 4n²·N_k(m) of its moves at width > k. So it has width at least about
    log(T/8n²) / log m. For T = 2^{n^ε}, that is Ω(n^ε / log n).

DATA, showing that the shape is tight on an exponential symmetric run (experiments/red/n5inj/ssiwidth.py).
- SSI on DLM family 1 from DLM's start pair (2^(n+1) − 3 iterations).
- Odd's moves by |It| at n = 8 (509 iterations) are exactly C(8, k): 8 / 28 / 56 / 70 / 56 / 28 / 8 / 1 for k = 1..8.
  Even's are 8 / 35 / 77 / 105 / 91 / 49 / 15 / 2.
- Every visited improving set is visited once. The exponential run is a walk through the improving-set classes, and most of its
  moves sit at width about n/2.

## 3. N5 runs measured by width (DATA; experiments/red/n5inj/movehist.py and declines.py; n5tr replica, counts asserted = n5.run)
| game | N5 iterations | Even moves by |Iσ| (k:count) | Odd moves by |Iτ| | max visited strategies per I |
| --- | --- | --- | --- | --- |
| sym_h8_s1 (n 16) | 25 | 1:6 2:3 3:1 4:4 5:2 | 1:6 2:3 4:4 6:2 7:1 | 1 / 1 |
| sym_h12_s1 (n 24) | 34 | 1:3 2:5 3:3 4:2 5:3 6:2 7:2 10:3 | 1:1 2:4 3:6 4:1 5:4 6:1 7:2 8:1 10:1 | 1 / 1 |
| sym_h16_s1 (n 32) | 55 | 1:9 2:6 3:5 4:3 5:3 8:1 11:2 12:1 15:2 | 1:9 2:6 3:6 4:3 5:2 6:1 7:1 10:1 11:2 14:1 15:1 | 1 / 1 |
| DLM fam. 1, n 8 (n 18) | 8 | 1:1 2:3 4:3 8:1 | 1:1 2:3 4:3 8:1 | 1 / 1 |
| DLM fam. 2, n 7 (n 72) | 13 | 1:3 2:2 3:3 4:1 5:2 7:2 | 1:2 2:2 3:5 4:1 7:2 | 1 / 1 |

- N5 on DLM takes ALL of a wide improving set at once: 8 of 8 at n = 8, and 7 of 7 at DLM2 n = 7. That is the failure of (R-b)
  in counting form.
- Every move on the climbed games takes 1-6 switches, even at width 15. Most moves sit at width ≤ 3 (41 of 65 on sym_h16_s1),
  and Theorem W caps those at O(n²·m³).
- Declined improving edges, counted per iteration, so an edge declined over several iterations counts several times:
  - Most are deferred and later taken: Even 80 / 133 and Odd 99 / 147 on sym_h16_s1, longest deferral 21 iterations.
  - The rest stop being improving: 53 / 48.
  - DLM: 4 declines in total.
- So the climbs' alternation (R-a) works by deferral. The opponent holds an honest improving edge off for a few iterations,
  then releases it.
- Fixed optimal opponent (experiments/red/n5inj/frozen.py): N5 from a random σ with τ = an optimal Odd strategy (then
  It = ∅ for good) took at most 5 iterations on 400 random games (n 4-12, 20 starts each), and at most 6 / 8 / 11 on
  sym_h8 / h12 / h16 (50 starts each). Random only: climbed frozen runs reach 43-86 (L-NEW box 21; see (K2), withdrawn).
- Output checks: N5 outputs on dlm1_8 and dlm2_7 pass Oink zlk + verify.py (check_sol2.py). The sym_* instances were verified
  in R57 §6b.

## 4. What Theorem W does and does not do (READING)
- It does not bound N5. Exponential SI runs exist at width about n/2 (DLM-SSI, §2). The theorem says WHERE a long run has to
  live, not that none exists.
- It explains R57 §6b's linear growth: the climbs' long tails are ping-pong at width 1-3, a budget of O(n²·m³) moves.
- It turns (R-b) into a quantitative demand. At almost every move the mover has at least log(T)/log m honest improving edges.
  N5's joint optimum against the opponent's current strategy must refuse all but the few it takes.
- Every refusal of an edge (v, w) ∈ Iσ needs a "bribe" (R-b mechanism):
  - Let Ψ be the valuation against τ (one-player, Odd fixed to τ). Then Ψ ⊵ Ξ at every vertex, since σ̄ is Odd's optimal reply.
  - N5's optimum σ′ keeps v off w, so Ψσ′(σ′(v)) ⊵ Ψσ′(w) while Ξ prefers w. Hence τ differs from Odd's best reply to σ′ on the
    (σ′, τ) play from σ′(v).
  - This forces τ to be generous on Even's current path.
  - One generous Odd vertex can bribe many refusals, so this gives no counting bound. Not proved further.

## 5. O5: O4 sharpened (Theorem W PROVED given (P); the rest READING)
A super-polynomial N5 family (length T) must have all of the following.
- (K1) PROVED given (P), Theorem W: all but 4n²·N_k(m) of each player's moves happen at |I| > k, for every k. Hence width
  ≥ log(T/8n²)/log m.
- (K2) WITHDRAWN 2026-10-24 00:08Z (date -u); the original text is in git at 685174fb. It read: "both players move about T/poly
  times; with the opponent fixed at its optimum, runs are short".
  - That held on random games only (§3: ≤ 5 iterations; ≤ 11 on the sym seeds).
  - It fails on climbed instances, all frozen-τ* runs:
    - L-NEW fts_g29: 66 steps;
    - fts_best24: 43 steps;
    - an 86-step climb at n 33 (docs/new/N5-time-box21.md §0, §3.7).
  - L-NEW's Theorem B (c) makes the frozen run a complete kill route. So "both players move" is NOT necessary, and a kill may
    have τ frozen at τ* (§7).
  - (K1) is unaffected and applies to frozen runs as Corollary W2.
- (K3) READING, from (K1) and N5's definition: at those wide moves N5's joint optimum against the current opponent refuses
  nearly all honest improving edges (R-b at width ω(1)). Each refusal needs the opponent to be generous on the mover's current
  path (§4).
- (K4) DATA, §1: the refused jump-ahead edges are counter edges (DLM 38/38; sym_h16 14/17). So lanes cannot be the mechanism
  for (K3). On the two-player branch, the generosity must come from the opponent's own counter state (R-a). On the frozen branch
  (§7) it comes from an optimal τ*, which is generous to a suboptimal σ for free (bribe_cex_n15); there R-a is not needed.

Partial incompatibility (PROVED given (P)): (R-a) + (R-b) at bounded width cannot give a super-polynomial run, whatever the
mechanism. Every construction the fleet has tried is of that kind: DLM jumps at full width, and the symmetric climbs sit at
width ≤ 3 for most moves.

Conjecture BRIBE (tested and FALSE in this box, DATA).
- Statement tested: a mover that refuses r honest improving edges faces an opponent with at least r / poly(n) improving edges of
  its own.
- Climbed games: consistent, worst ratio refused / opponent |I| = 11 / 5 (sym_h16_s1, iteration 9; experiments/red/n5inj/bribe.py).
- Random games: FALSE.
  - 3,000 random games, n 6-16 (bribebatch.py 3000 6 16 1): 740 moves refuse edges while the opponent has NO improving edge.
  - Instance experiments/red/n5inj/instances/bribe_cex_n15.pg (sha1 392af465e390…). Iteration 1: Even has 15 improving edges and
    takes 5; Odd has none (It = ∅). The output is verified (Oink zlk + verify.py), and the run is 1 iteration.
  - Obstruction: an OPTIMAL opponent τ* is still not the best reply to the mover's current suboptimal σ. So τ* is generous on
    σ's paths, and the refusals cost the opponent nothing.
- Lesson: refusals alone do not couple the two improving sets. They slow N5 only when the generosity comes from a NON-optimal
  opponent that later withdraws it (the deferrals of §3).

Remaining open form (READING; the target for L-NEW's incompatibility attempt and for my next box).
- (STRETCH) If the opponent's strategy stays fixed, the mover makes at most poly(n) consecutive moves.
- DATA:
  - Longest one-sided stretch: 6 on 3,000 random games (n 6-16; stretch.py), and 5 / 3 / 4 on sym_h8 / h12 / h16.
  - L-NEW's box-10 instance vc_g25 had 26 value-changing Even moves in one segment-phase (GAPS G-N5-TIME). So stretches are not
    O(1) in general.
- (STRETCH) together with (K1) still does not bound N5. A kill needs a family in which wide improving sets (K1) are held off by
  generosity that the opponent withdraws, at polynomially spaced moves, super-polynomially often (K3, K4).
- No construction attempted in this box meets that. Neither does any instance in the fleet's record (DLM: full-width jumps;
  climbs: width ≤ 3).

## 7. Theorem W against L-NEW's frozen-τ* branch (Lead 23:28Z; docs/new/N5-time-box21.md §2.4, §3; 2026-10-23 ~23:35Z, date -u)
Context:
- L-NEW's Theorem B (PROVED, unrefereed) gives: N5 ≤ (C_τ+1)(F_E+1).
- From (σ_0, τ*) with τ* honest-optimal, N5 IS the frozen run F_τ*.
- So a kill needs no (R-a): one Even counter would do.
- The proposed throttle: keep jump-ahead heads EXPLOITABLE, so that jump-ahead edges stay OUT of the honest gate Iσ (H1 false).

Corollary W2 (PROVED given (P); Theorem W restricted to a frozen run).
- Statement: an F_τ* run whose gate never exceeds k edges at a move has at most (2n(n−1)+1)·N_k(m_E) iterations. This counts
  arena and fallback steps alike, since every step changes σ and applies a nonempty subset of Iσ.
- Reason: the frozen run is an Even SI-type run with gate Iσ. Theorem W uses only that.
- So a super-polynomial F_τ* family needs gates of width ≥ log(T/4n²)/log m_E at all but polynomially many moves.

What this does to the design lead (READING).
- Two throttles exist, and they act differently:
  - Exclusion (L-NEW §3.1): the jump-ahead edge (x, z) is profitable against τ* but kept OUT of Iσ while z is exploitable.
    Exclusion makes the gate NARROWER.
  - Refusal (R58 §4-§5): the edge is IN Iσ but not profitable against τ*, because σ(x)'s side is exploitable and τ* is
    generous there (bribe_cex_n15: an optimal τ* refuses 10 of 15 at no cost).
- Exclusion alone (narrow gate, one edge opened per repair) gives at most (2n(n−1)+1)·N_k(m_E) iterations, by W2.
  - DATA, fts_ph16 frozen run (22 iterations, n 16): 12 of 22 moves at gate width 1, the rest at width ≤ 5. Iterations 11-22 are
    a width-1 repair chain: 4>11, 14>13, 0>14, 2>0, 7>2, …
  - Such chains are capped by W2 at (2n²)(m_E + 1): polynomial.
  - h1_hand: 2 moves, both at width 1.
- So a frozen kill must keep the gate WIDE: ω(1) honest-improving edges at almost every move.
  - Nearly all of them must be REFUSED against τ*. Refusal needs σ(x)'s head exploitable, with τ* generous there.
  - The jump-ahead edges may be excluded or refused; the width has to come from refused edges.
- Requirement for a CDAG_n + threat-gadget design: besides throttling the jumps, each counter state must present about
  log T / log m honest improving edges that τ* does not reward. CDAG's 2^n − n − 1 Ω-strict single-switch improvements
  (N5-K9-Pstrict-counter.md) are candidates for that supply only if they are honest-improving in the two-player game AND
  τ*-unprofitable. Not built here.

## 6. Files (experiments/red/n5inj/, all read-only on experiments/new/n5.py, experiments/si/si.py, experiments/red/n5/n5tr.py)
- injcheck.py G even|odd [SAMPLE SEED]: exhaustive (or sampled) check of the collisions σ ↦ Iσ and of Lemma 1's premise; |I|
  histogram.
- injbatch.py COUNT NMIN NMAX SEED: injcheck on random games, both players.
- movehist.py G [START]: N5 moves and waits by the mover's |I|; switches per move; max visited strategies per I.
- declines.py G [START]: fate of declined improving edges (deferred and taken later, or dropped).
- ssiwidth.py G START: the same for SSI (DLM tightness).
- frozen.py: N5 from (random σ, optimal τ*).
- jumpclass.py G [START]: jump-ahead switches by edge class (§1).
- bribe.py G [START] and bribebatch.py COUNT NMIN NMAX SEED: Conjecture BRIBE (§5).
- stretch.py G [START] | random ...: longest one-sided stretch (§5).
- widthclimb.py h SECONDS SEED OUT [KMIN] [--from G]: symmetric climb, fitness = wide refused moves, then iterations (results §8).
- frozenclimb.py n SECONDS SEED OUT len|wide [KMIN]: frozen-τ* climb (§8b). phaselen.py G [START]: iterations per joint λ-phase.
- instances/wide_h16.pg, frz24/32/40.pg + .start (§8).
- instances/bribe_cex_n15.pg: the BRIBE counterexample (sha1 392af465e390d3fb83003d1dc06163da891bdac9).
- DLM games come from experiments/new/dlm_gen.py 1|2 n, with the start pair on stderr.

## 8. Climbs (DATA; 2026-10-23 23:20Z to 2026-10-24 01:36Z, date -u). Every best is checked: Oink zlk OK, strategies verified
### 8a. widthclimb.py: symmetric games, n = 32
Fitness: W = moves with mover |I| ≥ 4 that refuse ≥ 2 edges while the opponent has |I| ≥ 1; then iterations. 3,600 s per seed.

| run | W | N5 iterations | longest joint λ-phase | instance |
| --- | --- | --- | --- | --- |
| from sym_h16_s1 (seed 1) | 72 (start 24) | 44 (start 55) | 23 | instances/wide_h16.pg (sha1 990ecbcf15ae…) |
| random (seed 2) | 34 | 24 | — | not kept |

- wide_h16: most moves sit at width 4-9; 245 / 238 declined-edge events (Even / Odd); longest one-sided stretch 2.
- Raising width did NOT raise length: the climb traded iterations for W.
- READING: on symmetric two-player games, holding wide refused sets is easy, but it does not lengthen runs.

### 8b. frozenclimb.py: frozen-τ* runs, free games
Start: σ_0 = S3 best-reward; τ* = Odd's switch-all SI optimum; Iτ* = ∅ is asserted. By L-NEW Theorem B (c), N5 is then the
F_τ* run.
- Mode 'len' fitness: iterations, then wide moves (|I| ≥ 3, ≥ 2 refused).
- The n = 32 / 40 runs were cut at about 1,890 s of their 2,400 s, when a background-task limit stopped my session's wrapper
  (not the program). The bests written by then are used.

| n | budget | iterations (fallbacks) | longest joint λ-phase | Odd choice vertices | moves at gate width ≥ 3 | instance (sha1) |
| --- | --- | --- | --- | --- | --- | --- |
| 24 | 2,700 s | 39 (4) | 11 | 1 | 39 / 39 | instances/frz24.pg + .start (f50c434b731a…) |
| 24 'wide' mode | 2,700 s | 28 (0) | — | — | 26 at ≥ 4 | not kept |
| 32 | ~1,870 s | 66 (8) | 28 | 3 | 60 / 66 | instances/frz32.pg + .start (b251897c9db0…) |
| 40 | ~1,900 s | 90 (7) | 36 | 4 | 85 / 90 | instances/frz40.pg + .start (934e6dfa9965…) |

Observations:
- Iterations grow about 1.6n to 2.25n, linear at these budgets.
- The longest λ-phase is 11 / 28 / 36, i.e. ≈ 0.9n. L-NEW's fts_g29 reaches 65 at n 29 in one phase, with a fitness aimed at
  phases.
- Frozen runs found by length alone live at WIDE gates: every move of frz24 refuses edges, with Odd's |I| = 0 throughout. So
  Corollary W2's requirement is easy to meet; the hard part is length within one phase.
- frz24 (one Odd choice vertex 19, so the game is in L-NEW's class 𝒞^1O):
  - The 10-step backward propagation chain 4>16, 22>4, 6>22 + 7>6, 13>6, 5>13, 3>5, 8>3, 20>8, 14>20, 2>14 runs TWICE, at
    iterations 2-11 and again at 29-38.
  - σ̄(19) toggles 10 → 9 → 10 → 9.
  - BUT the two laps lie in DIFFERENT joint λ-phases (cycle-node changes at iterations 12, 13, 26, 31; phase list
    [1, 11, 1, 1, 8, 2, 2, 1, 1, 3, 8]).
  - READING: lapping that needs a λ-phase change per lap is bounded by Lemma Φ (≤ 2n(n−1)+1 phases). So a kill must be
    super-polynomial INSIDE one joint λ-phase, which is L-NEW's (SEG-1O)/(CH-1O) target, not across phases.
- No kill. No instance shows growth beyond linear.

## 9. Proposition X: on 𝒞^1O, the part of the game that cannot reach o is a one-player N5 run (PROVED, unrefereed; Lead routing 01:47Z)
Setting:
- 𝒞^1O: o is the only Odd vertex with out-degree > 1 (L-NEW box 21 §3.4). Any start pair.
- X := {v : no path from v to o in the game graph}. X is closed under successors, o ∉ X, and every Odd vertex in X has one
  successor. So G[X] is a game with no Odd choice, i.e. a one-player game in RESULTS R17's sense.

Proposition X.
- Statement: along N5's run on G, the sequence of DISTINCT restrictions σ|X (Even vertices of X) is N5's run on G[X] from
  σ_0|X. Hence σ|X changes fewer than (|X|² − |X| + 1)(|X| + m_X) times (RESULTS R17).
- Proof (from SPEC S1-S4):
  1. Locality of valuations.
     - Plays from x ∈ X stay in X, so the valuations Ξσ(x) and W(x) depend only on σ|X.
     - In S1's procedure for a cycle node v ∈ X, the vertices of Y = V \ X never affect an X vertex:
       - the cycle tests and the cycle-node DFS use successors only;
       - for an Even-liked u ∈ Y, every X vertex of R reaches v without passing u, so it lies in M and loses no edge;
       - for an Odd-liked u ∈ Y, no X vertex reaches u;
       - in the BFS over predecessors, X vertices are discovered only from X vertices, so their relative FIFO order and their
         choices are those of the BFS on G[X];
       - a cycle node in Y kills no X vertex (X cannot reach it).
     - So Ξσ, the gate Iσ and the W-optimum over A(σ), restricted to X, are those of G[X].
     - S3's best-reward start is local.
  2. Steps.
     - An S4a step restricted to X is G[X]'s S4a step from σ|X.
     - If that step is null, σ|X stays fixed: it waits, possibly while Y moves. It can then change only through a global S4c
       fallback. That fallback is a switch-all on Iσ by the rule (Ξσ(w), w), whose X-part is G[X]'s own fallback. G[X] would
       fall back at that state too, since its step depends on σ|X alone.
  3. So every change of σ|X is G[X]'s next N5 step. R17 bounds the number of steps. □
- DATA: experiments/red/n5inj/xlocal.py, 3,000 random 𝒞^1O games (n 5-14). In the 676 with o on no cycle, the sequence of
  distinct σ|X equals the canonical N5 run of G[X] in all 676 cases, with no mismatch. The other 2,324 were skipped (o on a
  cycle).

Corollary X1, (CH-1O) on o-acyclic games.
- Statement: if every successor of o lies in X, i.e. o lies on no cycle of the game graph, then:
  - θ = Ξ(o), the minimum of o ⊕ Ξ(e) over o's exits e ∈ X, changes fewer than (|X|² − |X| + 1)(|X| + m_X) times;
  - so does w = W(o) = o ⊕ W(τ(o)) between τ changes (at most d − 1 of those).
- Consequence: by L-NEW's decomposition (N5-time-box21.md §3.6), N5 on o-acyclic 𝒞^1O is polynomial ⇐ (SEG-1O) alone.
- READING: a 𝒞^1O kill must put o on a cycle of the game graph. The θ throttle must be fed by exits whose regions can route
  back through o.
- On the instances (checked): in fts_best16 (o = 5) and frz24 (o = 19) EVERY exit of o reaches o, and X = ∅. Both lie wholly
  outside Corollary X1, as the corollary predicts for long runs.
- Scope: Proposition X uses R17 as signed (N5 on games where Odd has out-degree 1 everywhere). The locality argument in step 1 is
  mine and unrefereed.

## 10. Box 27: 𝒞^1O climbs (DATA; GO 2026-10-24 01:52Z, date -u). Every best is checked: Oink zlk OK, strategies verified
Target (Lead): a 𝒞^1O family with super-linearly many canonical N5 iterations inside ONE joint λ-phase.
Two routes:
- (a) o on a cycle: θ = Ξ(o) changes often (Corollary X1 requires the cycle).
- (b) o-acyclic: a long pure-Y block, i.e. a stretch with σ|X and τ fixed (L-NEW box 22 §6-§7, static problem (STAT)).

### 10a. θ-changes inside one λ-phase (thetaclimb.py; canonical start; 3,000 s per seed)
| seed | n | θ-changes in one phase (total) | iterations | longest λ-phase | instance (sha1) |
| --- | --- | --- | --- | --- | --- |
| fts_best16 (start: 8 in one phase) | 16 | 13 (15) | 20 | 18 | instances/theta_thf16.pg (90ed13cf9e2c…) |
| oneodd_c24 (start: θ-changes 5) | 24 | 16 (19) | 29 | 18 | instances/theta_thc24.pg (12a303c9a778…) |
| random, n 20 / 28 (stopped at ~8 min) | 20 / 28 | 8 / 6 | 15 / 21 | — | not kept |

- θ-changes per phase stay below n.
- Mechanism seen in fts_best16, READING:
  - o's exits sit on one σ-path that returns to o (a "ring"), and σ̄(o) walks along it as the path improves.
  - Each lap needs the ring's entry value to improve.
  - A super-linear count would need nested rings, with each outer improvement re-arming an inner lap more than once. Not built.

### 10b. Pure-Y blocks on o-acyclic 𝒞^1O (blockclimb.py; o's exits are 3 self-loop sinks = X; canonical start)
Tool: blockcheck.py recomputes X, o-acyclicity and the blocks by L-NEW's definition.

| |Y| (incl. o) | n | pure-Y block | longest stretch inside block ∩ one λ-phase | λ-phases in the block | instance (sha1) |
| --- | --- | --- | --- | --- | --- |
| 21 | 24 | 27 | 10 | 11 | instances/block_bk20.pg (98dc1d8bced1…) |
| 33 | 36 | 49 | 22 | 28 | instances/block_bk32.pg (439bff4eb16e…) |

- FINDING (DATA): L-NEW's data bound "every pure-Y block ≤ |Y|" (575 random games; climbY best = |Y|) is FALSE: 27 > 21 and
  49 > 33.
  - Both runs: no Odd move, no fallback, τ fixed, X fixed. The whole run is ONE pure-Y block.
- But each block crosses many λ-phases. Inside one phase the stretch is 10 / 22, below |Y|.
- READING: (STAT) blocks can exceed |Y| only through λ-phase changes, i.e. cycle-node changes inside Y, at most 2n(n−1)+1 of them.
  So the per-(block ∩ phase) quantity is the one to bound, or to break.
- A follow-up climb with fitness "longest stretch inside block ∩ one λ-phase" (blockclimb.py --phase) runs from both instances
  to ~04:13Z; results in §10c.

### 10c. Longest stretch inside one pure-Y block AND one λ-phase (blockclimb.py --phase, 2,400 s, seeded from 10b; date -u 03:33-04:10Z)
| |Y| (incl. o) | n | longest stretch in block ∩ one phase | block (= whole run) | phases | instance (sha1) |
| --- | --- | --- | --- | --- | --- | --- |
| 21 | 24 | 20 (start 10) | 25 | [1, 20, 1, 3] | instances/blockph_bp20.pg (see sha1 below) |
| 33 | 36 | 31 (start 22) | 39 | [1, 31, 1, 1, 1, 1, 1, 1, 1] | instances/blockph_bp32.pg (see sha1 below) |

- Both runs are o-acyclic, with no Odd move and no fallback. Oink zlk OK, strategies verified.
- The climbs pushed the in-phase stretch to |Y| − 1 = 20 and to |Y| − 2 = 31, and not beyond.
- Conjecture STAT-PH (READING, DATA only): inside one joint λ-phase, a pure-Y block of an o-acyclic 𝒞^1O run has at most
  |Y| − 1 iterations. This is R17's n − 1 shape, with |Y| in place of n.
- With Lemma Φ (≤ 2n(n−1)+1 phases), Proposition X and L-NEW's reduction (C_X + d)(B_Y + 1), STAT-PH would make N5 polynomial
  on o-acyclic 𝒞^1O. No proof route is offered here; L-NEW's I1-I4 failures (box 22) show the per-path R17 template breaks.
- Box 27 result: NO KILL on 𝒞^1O. Route (a) gives θ-changes < n per phase; route (b) gives blocks > |Y| but ≤ |Y| − 1 per phase.
- blockph_bp20.pg sha1 c0cb90699c1e7eb042af61c4bdee9b762477ef43
- blockph_bp32.pg sha1 66c134cffcc92d1f63b8c3f4377c87ce8d84ca38

## 11. Box 28: o-cyclic 𝒞^1O and the 2-choice fallback (DATA and READING; GO 2026-10-24 04:31Z, end ~06:20Z, date -u)
Target (Lead): an N5 kill on o-cyclic 𝒞^1O, i.e. super-linearly many canonical iterations inside ONE joint λ-phase.
- The o-acyclic case is settled: L-NEW's refereed theorem (docs/new/N5-1Oacyc-box24.md) plus Prop X, landing as RESULTS R18.
  STAT-PH (§10c) is recorded only as a data conjecture.
- Every instance below passes Oink zlk and verify.py. Each was re-run with n5.py from the canonical start.

### 11a. θ-change climbs, padded (thetaclimb.py --from, padding with inert self-loop vertices; 3,600 s each)
| seed | n | θ-changes in one phase (total) | iterations | longest λ-phase | max trust events per phase (L-NEW trustcount.py) | instance (sha1) |
| --- | --- | --- | --- | --- | --- | --- |
| theta_thf16 → | 32 | 16 (20) | 45 | 41 | 4 | instances/theta_tp32.pg (f3c241884b34…) |
| theta_thc24 → | 40 | 16 (20) | 41 | 20 | — | instances/theta_tp40.pg (45b2bfd61427…) |
| (box 27) theta_thf16 | 16 | 13 (15) | 20 | 18 | 2 | |
| (box 27) theta_thc24 | 24 | 16 (19) | 29 | 18 | 0 | |

- θ-changes per phase PLATEAU at 16 from n 24 to n 40.
- theta_tp32 has a 41-iteration λ-phase at n 32 with one Odd choice vertex: above n − 1 = 31 but linear, about 1.3n.

### 11b. Ring templates (ringsearch.py; fixed topology, random priorities, 2,000 trials each)
- Template: a chain c_L → … → c_1 → o, with bail edges and o's exits on the chain.
- Results: one lap only. The θ-changes in one phase are 4 / 2 at L 6 and 5 / 4 at L 10 (exits all / odd), about L/2.
- READING: the plain absorbing ring reproduces the single lap of fts_best16 (exits absorbed into R one per step, σ̄(o) walking
  along the chain).
  - The second lap in fts_best16 / theta_thf16 needs a RESET WAVE: chain vertices switch away (iterations 9-11) and back (12-18),
    one return each.
  - No template here produces more than one lap.
  - Nested rings, where each outer reset re-arms an inner lap more than once, were NOT built.

### 11c. Fallback: at most 2 Odd choice vertices (phaseclimb.py K = 2; fitness = longest joint λ-phase; 3,000 s each)
| n | longest λ-phase | iterations (fallbacks) | Odd choice vertices | instance (sha1) |
| --- | --- | --- | --- | --- |
| 32 | 53 | 56 (6) | 14, 28 | instances/phase2_pk32.pg (2db943015cd9…) |
| 48 | 50 | 72 (8) | 14, 27 | instances/phase2_pk48.pg (83dead9bc3cd…) |

- In-phase length is about 1.6n at n 32 and about 1.0n at n 48 (budget-limited), so linear.
- L-NEW's frozen fts_g43, with 8 Odd choice vertices, remains the longest known: 121 iterations at n 43, about 2.8n.

### 11d. Result
- NO KILL on o-cyclic 𝒞^1O or with 2 Odd choice vertices.
- Every measured in-phase quantity is linear or plateaus, for θ-changes, phase length and trust events alike.
- The Lead's (TRUST) target: my instances have ≤ 4 trust events per phase. L-NEW's trustclimb reaches 29 at n 20 (box 25).
- READING, what a kill still needs: a reset wave that re-arms the absorbing ring more than once per outer event, i.e. returns at
  ring vertices that grow with depth. The only return mechanisms known are σ̄ lapping (one return per lap) and L-NEW's W-dropping
  fallbacks (one peel each). Neither has been composed.

## 12. Box 29: composing a reset wave with the absorbing ring (GO 2026-10-24 06:30Z; written 08:15Z, date -u)
Target (Lead): a COMPOSED reset wave that re-arms the absorbing ring more than once per outer event, inside ONE joint λ-phase.
- Success would be a family whose in-phase count grows super-linearly over ≥ 3 verified members.
- Every instance below passes Oink zlk and verify.py (check_sol2.py), re-run with n5.py from the canonical start.

### 12a. Re-rooted ring template (rootsearch.py --climb; chain c_L..c_1 → hub h → roots r_1..r_k → o; 1,200 s per run)
| L | k roots | longest in-phase count |
| --- | --- | --- |
| 8 | 1 | 9 |
| 8 | 4 | 10 |

- The k = 4 trace: the hub chooses one root once (18 → 19); the chain then propagates once (2>18, 3>2, …, 9>8); no re-root.
- WHY (READING, from L-NEW's Lemma G (c), box 21 §3.5):
  - Between two routes that both run through o, the gate and the selection compare the same quantity, π_y vs π_z, independent
    of θ and w.
  - So a hub's re-root is a one-player move. The chain keeps its edges, its values rise along them, and no chain vertex switches.
  - A re-root therefore re-arms nothing.
- Replaying the chain needs chain vertices to RETURN through o-free routes (R → F → R).

### 12b. Returns inside one phase (phasereturns.py, retcheck.py)
| instance | n | Odd choice vertices | longest phase | max switches / returns at one vertex | R→F leaves in the phase | re-entries (θ overtook old w / route improved) |
| --- | --- | --- | --- | --- | --- | --- |
| fts_best16 | 16 | 1 | 26 | 6 / 3 | 4 | 0 / 2 |
| theta_tp32 | 32 | 1 | 41 | 6 / 4 | 3 | 0 / 3 |
| fts_best39 | 39 | 4 | 77 | 8 / 5 | — | — |
| fts_g43 | 43 | 8 | 120 | 16 / 13 | — | — |
| returns_rt48 (new) | 48 | 1 | 78 | 14 / 12 | 34 | 0 / 15 |
| returns_rt64 (new) | 64 | 2 | 88 | 14 / 12 | — | — |
| returns_ph64 (new) | 64 | 1 | 103 | 10 / 8 | — | — |

- Instances: experiments/red/n5inj/instances/returns_rt48.pg (7e7ee1b354ad…), returns_rt64.pg (04c2f308ec50…),
  returns_ph64.pg (562f3e36dba5…), returns_rt32.pg (307240c5b8a9…).
- rt48 and ph64 are o-cyclic 𝒞^1O (one Odd choice vertex o = 14). rt64 kept a second Odd choice vertex.
- Per-vertex resets DO grow under a climb aimed at them: 12 returns at one vertex and 34 R→F leaves in one phase of rt48, against
  ≤ 5 and ≤ 4 on every earlier 𝒞^1O instance.
- No re-entry into R ever came from θ overtaking the w at the leave: 0 of 20. All came from a route improvement inside R.

### 12c. The in-phase count stays linear
On o-cyclic 𝒞^1O the longest phase is:

| instance | n | longest phase | per n |
| --- | --- | --- | --- |
| fts_best16 | 16 | 26 | 1.6n |
| theta_tp32 | 32 | 41 | 1.3n |
| returns_rt48 | 48 | 78 | 1.63n |
| returns_ph64 | 64 | 103 | 1.61n |

- Local exponent from 48 to 64: log(103/78)/log(64/48) = 0.97.
- With 2 Odd choice vertices: 53 at n 32, 50 at n 48 (§11c), 88 at n 64.
- These are climbs, not a family. There is no growth law, and no member is above about 1.65n.

### 12d. Why the composition fails (READING, with the data of 12a-12c; for the stand-down note)
- (i) A re-root does not re-arm. Routes through o are compared independently of θ and w (Lemma G (c)), so re-rooting is a
  one-player move along unchanged chain edges. Smallest instance: rootsearch L 8, k 4 (n 27, regenerated by `rootsearch.py 8 4
  all 1200 22 OUT --climb`): 10 in-phase iterations against 9 for k = 1.
- (ii) Re-arming needs returns R → F → R. A leave needs the o-free value above π ⊕ w; a re-entry along the same successor needs
  π' ⊕ θ above that o-free value. Since θ, w and o-free values only rise inside a τ-fixed phase, each re-entry needs either θ to
  overtake the old w, or a strictly better route π' inside R.
  - The data show only the second: 20 / 20 re-entries.
  - Route improvements inside R are one-player moves (Lemma G (c)), so each re-arm consumes one-player progress inside R. A phase
    holds polynomially much of that, but not in any proved per-phase form here.
- (iii) Resets per vertex can be made large (12 at n 48), but the climbs that make them large do not lengthen the phase beyond
  about 1.6n. The resets come from S4c fallbacks (14 in rt48 and in rt64) and from leaves, each followed by a short re-propagation,
  not by a full ring replay.
- Statement for the stand-down note: on o-cyclic 𝒞^1O the only re-arming mechanism observed is "route improvement inside R",
  which is a one-player resource. A re-root via θ was never observed, and a re-root via the hub is θ-independent. No in-phase count
  above about 1.65n was found up to n 64.

### 12e. Correction to §12d (ii) (2026-10-24 13:20Z, date -u; from L-NEW box 26 checkpoint 1, relayed by the Lead)
- retcheck.py's class A ("θ at re-entry ▷ w at the leave") cannot occur while w is constant, because θ ⊴ w (Lemma S). Class B
  was the fall-through, so "20 / 20 re-entries by route improvement" is WRONG.
- With L-NEW's classifier (experiments/new/box25/reentry.py), THETA re-entries are common. These are re-entries where w is
  unchanged, the route is the same, and only θ rose:

  | instance | ROUTE re-entries | THETA re-entries |
  | --- | --- | --- |
  | fts_best16 | 2 | 2 |
  | theta_tp32 | 0 | 4 |
  | rt48 | 21 | 21 |
  | ph64 | 30 | 23 |

  The smallest partial release is thetare_min.pg (n 15).
- §12d (ii) should therefore read: a re-entry along the same successor needs θ to rise past the leave threshold (THETA), or a
  better route inside R (ROUTE). Both occur.
- L-NEW proves (lane, unrefereed) that THETA re-entries per phase are at most n × (θ-changes in the phase). So the decisive
  quantity is the number of θ-changes per phase (§11a: plateau at 16 for n 24-40).
- §12d (i) and (iii) stand.
