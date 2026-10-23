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
  sym_h8 / h12 / h16 (50 starts each).
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
- (K2) READING with DATA: both players move about T/poly times.
  - With the opponent fixed at its optimum, runs are short: ≤ 11 iterations in §3, and R17 on one-player games.
  - A fixed-opponent stretch bound is NOT proved for two-player games: G-N5-TIME, box-10 note vc_g25.
- (K3) READING, from (K1) and N5's definition: at those wide moves N5's joint optimum against the current opponent refuses
  nearly all honest improving edges (R-b at width ω(1)). Each refusal needs the opponent to be generous on the mover's current
  path (§4).
- (K4) DATA, §1: the refused jump-ahead edges are counter edges (DLM 38/38; sym_h16 14/17). So lanes cannot be the mechanism
  for (K3). The generosity must come from the opponent's own counter state, which is R-a.

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
- instances/bribe_cex_n15.pg: the BRIBE counterexample (sha1 392af465e390d3fb83003d1dc06163da891bdac9).
- DLM games come from experiments/new/dlm_gen.py 1|2 n, with the start pair on stderr.
