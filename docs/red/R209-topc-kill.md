# R209 TOP-C is DEAD (L-NEW box 175 kills confirmed under R208's exact gain′); co-designed re-arm attack: no growth (L-RED successor 50)
Started 2026-11-06 01:5xZ (date -u). Lead R209 (01:27Z: co-designed attack on CONJECTURE TOP-C, R208) and 01:46Z (check L-NEW box 175's
kill seeds under R208's exact gain′; then (a) weak forms, (b) iteration). Model: IDEAL-ACYC (RESULTS R104), degree ≤ 2.
Labels: DATA (replayed), DEAD, PROVED (lane), READING. Not a TARGET.md claim. G-N5-TIME stays OPEN.

## 0. Answers
- TOP-C (gain′ ≤ 2 + C, R208): DEAD. The four L-NEW box 175 seeds (claude/l-new 06d4238d) were checked with my own exact tool
  r208/gainx.py.
  - Tool: top = max level, any indexing; exhaustive over all acyclic re-routings of the couplings (X or any non-top mover); the same
    start. A second variant also takes the max over ALL starts of the re-routed lower genome.
  - Every seed has C = 1, so 2 + C = 3.

  | instance (sha1) | d | T | best re-routing, same start | gain′ | best re-routing, all starts | gain (all starts) |
  | --- | --- | --- | --- | --- | --- | --- |
  | fa_d2_k2_W2 (6451b7c7) | 2 | 4 | 0 (X) | 4 | 0 | 4 |
  | iso_d4_st9 (7ca1e68c) | 4 | 11 | 3 | 8 | 4 | 7 |
  | g4_L12 (7d9c1025) | 4 | 12 | 5 | 7 | 6 | 6 |
  | tri_d5_L12 (9d419424) | 5 | 12 | 8 | 4 | 8 | 4 |

  - Every instance is in 𝓛^R-shape: two two-option movers per level, degree 2.
  - Replays:
    - ideal.py.
    - box166 verify_kill: well-formed, acyclic.
    - box150 check: XSIM 0, VIOL 0.
    - r189/lemck: 0 on every check, so these are real FL runs of N5 «from the stated start pairs». iso_d4_st9 needed an
      order-preserving renumbering of its 2000+ gates first: r209/seeds/iso_d4_st9_rn.json gives the same T and gain′.
  - Why R208 missed them: its bases were fixed near-extremal genomes, for which the best re-routing is already ≈ T(base).
- Weak form «T(G) ≤ T*(d − 1) + 2 + C» (what the recursion would need): also false at d 4, conditional on T*(3) = 8. g4_L12 has T 12 >
  8 + 3. T*(3) = 8 is exact on ladders (R202 / R197); with helpers it is DATA. It is no growth signal, since T*(4) = 13 = 8 + 5 anyway.
- (b) Does per-top-move re-arming iterate, so that gain′ grows with T(d − 1) at C = 1? Co-designed climbs (r209/coclimb.py: the WHOLE
  genome mutated, exactly one coupling, score gain′ or R = re-armed lower steps after the first top move) found NO growth (DATA):

  | file | d | T | m (top-moving steps) | lower steps per TOP-SPLIT segment | gain′ (same start) | gain (all starts) |
  | --- | --- | --- | --- | --- | --- | --- |
  | cc4_s1 | 4 | 11 | 6 | 1, 0, 2, 0, 2, 0, 1 | 9 | 7 |
  | cc5_s2 | 5 | 9 | 3 | 1, 1, 5 | 7 | 3 |
  | ra5_s3 | 5 | 14 | 7 | 1, 1, 0, 3, 2, 2, 0 | 7 | 7 |
  | ra6_s4 | 6 | 16 | 6 | 1, 2, 3, 2, 3, 3 | 15 | 3 |
  | ra6L_s5 | 6 | 21 | 8 | 1, 2, 3, 0, 8, 1, 2, 0 | 4 | — |
  | ra7L_s6 | 7 | 28 | 9 | 1, 4, 2, 3, 3, 5, 2, 3, 2 | 3 | — |

  - The all-starts gain at C = 1 stays ≤ 7 from d 2 to d 6. The re-armed segments stay short (≤ 9 lower steps; most ≤ 3), and m
    stays at 3-9.
  - The same-start gain′ is start-sensitive. ra6_s4 has gain′ 15 only because its lower part runs 1 step from that start; over all
    starts its gain is 3. So the robust measure is the all-starts gain, and it does not grow.
- (a) Weak forms.
  - «gain′ ≤ 2 + C·(1 + m)» fails on cc4_s1 (9 > 8).
  - What holds is TOP-SPLIT (PROVED, R208): T ≤ (m + 1)·T*(d − 1) + m.
  - In all data, gain (all starts) ≤ 7 at C = 1 and ≤ m + 1. I state no new conjecture: the data are small and the same-start
    variant is fragile.

## 1. Mechanism (DATA, iso_d4_st9 / cc4_s1)
- The run has m = 6 top-moving steps.
- TOP-SPLIT segments carry 1, 0, 2, 0, 2, 0, 1 lower steps. Each re-armed segment moves the coupled mover once: the top move changes
  the coupled option's value, the mover takes it, and one Ξ-ancestor follows.
- So the gain is «top moves + one short re-arm per top move», not a re-armed long run.
- READING: a long re-armed run would need the coupled mover's value change to feed a deep Ξ-chain of ancestors. In every climb the
  re-arm dies within ≤ 3 steps, except one segment of 8-9 steps in the lifted seeds, which is inherited from the base run, not
  iterated.

## 2. Files (experiments/red/r209/)
- seeds/ (L-NEW box 175 copies + iso_d4_st9_rn).
- keep/ (cc4_s1, cc5_s2, ra5_s3, ra6_s4, ra6L_s5, ra7L_s6; all replayed: verify_kill well-formed, box150 VIOL 0, lemck 0).
- coclimb.py (SCORE=gain | rearm | excess); segs.py (TOP-SPLIT anatomy).
- r208/gainx.py (exact gain′, any indexing; same-start and all-starts).
