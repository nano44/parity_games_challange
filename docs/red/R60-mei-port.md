# R60: Mei's Ĝ_h ported to parity, and N5 on it (L-RED successor 14, box 31; written 2026-10-24 14:56Z, date -u)
Target (Lead GO 14:48Z): T31 checklist (i)-(iv) (docs/lit/T31-mei-port.md, L-LIT). Labels per D18 / L40: PROVED (who checked),
CONJECTURE (data), OPEN, plus DATA and READING. No running-time claim (D1). G-N5-TIME stays OPEN.

## 0. Source (opened by me)
- S. Mei, "Simple Strategy-Iteration with Dantzig's Rule is not Strongly Polynomial on Turn-Based Deterministic Games", arXiv
  2610.27386 v1 (19 Oct 2026). PDF fetched 14:54Z, sha256 5b3265d3eb1c5b8ae79f…, the same file as T31's.
- Read: §3.1 p.5 (construction, eq. (3), Table 1); eq. (4) p.6 (start σ_0(a_i) = (a_i, p_i)); Theorem 1 p.11 (exactly 2^h − 1
  iterations, h ≥ 2); §5.1 p.20 (Ĝ_h, eq. (35)) and Theorem 4 p.20 (Algorithm 2 from (4): exactly 2^h − 1 iterations).
- The graph, owners and start of my port match Table 1 and eq. (4) line by line.

## 1. The port (T31 (iii) exactly)
- Generator: experiments/red/mei/meigen.py h out.pg. It writes out.pg.start (SIGMA0 = eq. (4); TAU0 = Odd's best reply σ̄_0
  computed by si.py). Vertices are labelled a_i, b_i, p_i, q_i, wp_i, wq_i, kp_i, kq_i, r. n = 8h + 3. Priorities as in T31's table.
- Instances, experiments/red/mei/instances/ (sha1):

  | h | n | sha1 |
  | --- | --- | --- |
  | 2 | 19 | eef6418f… |
  | 3 | 27 | 8e819ddf… |
  | 4 | 35 | c971b1df… |
  | 5 | 43 | def85e63… |
  | 6 | 51 | b30d5e72… |
  | 8 | 67 | 6d1537da… |

- h = 1 is NOT built: T31's priority table (like Mei's construction) is for h ≥ 2.

## 2. Checklist results (DATA; experiments/red/mei/meirun.py, n5.py and elim.py unmodified)
| h | n | Dantzig-SSI from σ_0 | its longest non-eliminating run | N5 from (σ_0, σ̄_0) | N5 canonical | N5 phases (start / canon) | N5 longest phase / non-elim run |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 19 | 3 | 1 | 3 | 1 | 2 / 1 | 1 / 0 |
| 3 | 27 | 7 | 3 | 4 | 2 | 2 / 1 | 2 / 0 |
| 4 | 35 | 15 | 7 | 5 | 3 | 2 / 1 | 3 / 0 |
| 5 | 43 | 31 | 15 | 6 | 4 | 2 / 1 | 4 / 0 |
| 6 | 51 | 63 | 31 | 7 | 5 | 2 / 1 | 5 / 0 |
| 8 | 67 | 255 | 127 | 9 | 7 | 2 / 1 | 7 / 0 |

- (i) Every N5 output (both starts, h = 2..6 and 8) passes Oink zlk + verify.py (check_sol2.py). No fallbacks.
- (ii) Dantzig-SSI control = si.py rule_single_level (MSF: the single switch at the most significant valuation difference; Odd =
  σ̄). It makes exactly 2^h − 1 iterations, as Theorem 4 says. The port is faithful for the rule Mei analyses, and T31's PROVED-S
  row "Lemma 7 / Thm 4" is CONFIRMED by run for h ≤ 8.
- (iii) N5: h + 1 iterations from Mei's start pair, h − 1 from the canonical start. L-COMP's n5b.py (SPEC and orig modes) gives
  the same counts on every instance, from both starts.
- T31's CONJECTURE (iv) holds on the data:
  - experiments/red/mei/meitrace.py, h = 4, Mei start. In iteration 0, N5's gate is {a_j > q_j : j = 1..4} and Even's arena
    optimum takes all four. Odd's arena step leaves τ unchanged (against σ_0 the q_j are off the play).
  - In iteration 1, Odd cancels all four return cycles (q_j > wq_j) and fixes b_1, b_3. Then one level resolves per iteration,
    top-down. Iterations: 5.
- Correction to T31 (ELIM-n READING): Dantzig-SSI's longest non-eliminating run is 2^(h−1) − 1, not 2^h − O(h). Level h pivots
  only once, at the midpoint, and that move abandons (a_h, p_h) for good, so it is eliminating. Still exponential: 127 at n 67.
  So (ELIM-n) is false for Dantzig-SSI on the port (DATA h ≤ 8; PROVED-S by Mei Lemma 7 plus this midpoint argument).

## 3. T31 (iv), "redesign so that N5's gate is a singleton", cannot give a kill (PROVED given (P); lane, unrefereed)
- Claim: on any family, the N5 iterations at which Even's gate has |Iσ| ≤ 1 number at most (2n(n−1)+1)·(1 + m_E). Likewise for
  Odd with m_O.
- Proof: Theorem W of R58 §2 with k = 1. It holds for every SI-type run, N5 included; premise (P) = VJ00 Lemma 5.8, cited via
  RESULTS R15. □
- So a family on which N5's gate is a singleton at every iteration has polynomially many iterations. The redesign target must be:
  a WIDE gate of which N5's arena optimum takes only a small part (refusals), as in R58 §7 (Corollary W2: exclusion-only
  throttles are polynomial).
- The port shows why. gatecensus.py over all 2^h Even strategies (h = 2..6, 8):
  - |Iσ| has the binomial histogram C(h, k). So |Iσ| = the number of levels with ∆_j > 0 (Mei's counter popcount).
  - Valuations are all distinct, and σ ↦ set of improving vertices is injective (a strict cube USO; Szabó-Welzl outmap
    bijection). Only h strategies have a singleton gate.
  - Mei's Dantzig run visits all 2^h strategies, at mean gate width h/2. Its exponential length comes from Dantzig's narrow TAKE,
    not from narrow gates.
- READING, the kill requirement on this family: at a state with gate {a_j > s_j : ∆_j > 0}, N5's arena optimum against τ_k must
  take only the lowest level.
  - On the plain port it takes all of them: against τ_k = σ̄_k every gate edge closes an Even-won return cycle (top k^s_j, even),
    and the levels do not interact in Even's one-player optimum.
  - A refusal of (a_j, s_j) for j above the lowest needs τ_k to differ from σ̄_k at s_j: Odd must already go forward at s_j, while
    σ̄_k returns. N5's Odd step is the one that creates such lags. The construction has to keep Odd's τ "ahead" at higher levels
    while Even's honest gate still contains them. That is the trust mode of R57 §6 / R58 §5, and no construction is known.
  - OPEN.

## 4. Files (experiments/red/mei/)
- meigen.py (port + start file), meirun.py (Dantzig control with its elimination window; N5 both starts; elim.py rows; writes
  .sol files), meitrace.py (per-iteration gate, switches and σ̄-τ mismatch), gatecensus.py (|I| census over all Even strategies).
- Reproduce: `python3 experiments/red/mei/meirun.py experiments/red/mei/instances/mei_h6.pg` (start file next to it), then
  `python3 experiments/new/check_sol2.py experiments/red/mei/instances/mei_h6.pg experiments/red/mei/instances/mei_h6.pg.mei-start.sol`.
