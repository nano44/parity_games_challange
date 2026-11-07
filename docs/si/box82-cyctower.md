# Box 82 CYCLIC TOWERS: can the tower doubling be carried by Odd (R > 0) under N5′-xi? (milestone 1)
L-SI successor 43 (Opus 5.5), under D18 / D14 / D1. Lead brief 2026-11-07 22:35Z (BOX 82). Written from 23:57Z (date -u; see the
commits). Labels: PROVED (lane, unrefereed) / CONJECTURE / DATA (counter: unit, set, scope) / DEAD / READING (not to sign). Not a
TARGET.md claim. G-N5-TIME stays OPEN. N5′-xi stays a CANDIDATE (D1). Tools: experiments/si/box82/ (check82.sh, wired); the runners are
box 81's (experiments/si/box81/, L-NEW byte copies in ref/).

## 0. Answer so far
- PROVED (§1, Corollary CAP-R): under Howard / N5′-xi, h capped levels force R ≥ (2^(h+1) − 1)/(N + 1) − C − 1, with C ≤ n(2M + 2)
  (R118 CYC-COUNT). So a tower family whose height grows faster than log of a polynomial is, for N5′-xi, exactly an Odd counter with R
  exponential in h. That is L-RED's open «third bit» / LADDER question, and no shortcut via the tie rule exists. On Ξ-acyclic genomes
  (R = C = 0, P-ACYC) the height is at most log₂(N + 2) − 1.
- DATA, h = 2 baseline (§2): adding Ξ-cycles to L-LOWER 8's HS2_d3 by 1 or 2 Ξ-target edits never carries the doubling under Howard.
  - The baseline has IDEAL T 6, F 2, 6, 2 (two capped levels). Its Howard run has T 4, R 0.
  - 956 Ξ-cyclic variants. Max R 2, max Howard T 5. Key flips at level 1 ≤ 3, against the 6 that the cap needs.
  - So with ≤ 2 edits the doubling breaks, and Odd does not take it over.
- DATA, climbs on 𝓛^R_d with Ξ-cycles allowed (§3):
  - max R grows slowly with d: 2, 5, 7, 9, 10 at d = 2, …, 6;
  - the Howard capped height is 2 for d = 3, 4, 5 and 3 at d = 6 (one seed of three);
  - the d = 6 genome with 3 capped levels (key flips 2, 6, 14) has T 20, C 7, R 6. The real N5′-xi mover phase equals Howard there, and
    N5 (spec) makes only 5 iterations on it.
  - At this size every capped profile fits inside the linear-in-N budget of CAP-R. Nothing here shows R doubling with h.
- Side product (for L-NEW's RECUR(2), via the Lead): best_R_d5_s3 (N 10, M 20) has plays with 2 ascents: 5 plays at state 9, from
  e-vertices of levels 1 and 2, each ascent through one or more upward Ξ-edges (§3). It is the smallest ≥ 2-ascent IDEAL-CYC instance
  in the lane's files.

## 1. Corollary CAP-R (PROVED, lane)
Setting:
- any genome G; IDEAL-CYC(G) Howard, R118 (a).
- For a pair (2l, 2l + 1) of movers on the same level (𝓛^R_d layout, R104 / R110), the key order of a state is R104's: gate indices
  along the W-chain, lowest level first.
- F_H(l) counts the steps of the Howard run at which the pair's key order changes. «h capped levels» means F_H(l) = 2^(l+2) − 2 for
  l < h (R104 / R113's cap read on the Howard run).

Statement: if the run has h ≥ 1 capped levels, then 2^(h+1) − 2 ≤ T_CYC ≤ C + R + (C + R + 1)·N. Hence
R ≥ (2^(h+1) − 1)/(N + 1) − C − 1.

Proof:
- F_H(h − 1) counts distinct steps, so F_H(h − 1) ≤ T_CYC.
- The second inequality is R118 (f) T-CYC: «T_CYC ≤ C + R + (C + R + 1)·N ≤ (C + R + 1)(N + 1)».
- Rearrange. ∎

Corollaries:
- With C ≤ n(2M + 2) (R118 (e)), a family with h ≥ c·log₂(N·M·n) for large c forces R ≥ 2^(h+1)/(N + 1) − poly. So a super-polynomial
  height function S(h) under N5′-xi is impossible unless R is exponential in h.
- On Ξ-acyclic genomes (P-ACYC: C = R = 0, T_CYC ≤ N): 2^(h+1) − 2 ≤ N, so h ≤ log₂(N + 2) − 1.
- READING: the Lead's question «can the doubling be carried by Odd's choices» therefore has a precise form. Under N5′-xi, every capped
  level beyond log₂ of a polynomial must be paid for by a doubling of R, i.e. by a binary counter in σ̄. That is the open counter question
  of L-RED (LEAK-ARCH, third bit), now with a tower interface. Box 193's UP-B adds that the plays must have growing ascents.

## 2. h = 2 baseline: HS2_d3 with Ξ-cycles (DATA)
- Instance:
  - HS2_d3.txt: claude/l-lower da105498, experiments/lower/l8/rec/HS2_d3.txt, sha1 8ddebddc55e255843bde61f4026a2f448e6b136d, the Lead's
    figure.
  - Mapped by box80/j2t.py (t2j) to inst/HS2_d3.json, sha1 8ce59c3f….
  - sim80.py: d 3, T 6, capped 2, F 2, 6, 2.
  - IDEAL-CYC Howard: T 4, C 0, R 0, 0 ascents (Ξ-acyclic, so P-ACYC applies).
- Scan (scan82.py):
  - every variant with K changed Ξ-targets (K = 1: 60 variants, 20 Ξ-cyclic; K = 2: 1,650 variants, 936 Ξ-cyclic), new target any
    mover other than the option's own mover, or X;
  - unit: Ξ-cyclic variants; set: all of them; scope: the stored start.
- Results:
  - K = 1: R 0 / 1 / 2 in 15 / 4 / 1 variants; Howard T ≤ 5; F_H(1) ≤ 3; max ascents ≤ 1.
  - K = 2: R 0 / 1 / 2 in 685 / 219 / 32; Howard T 2-5 (5 in 54 variants); max ascents 0 or 1.
- The exact obstruction at h = 2 is the step budget, not Odd:
  - the cap at level 1 needs 6 key flips, hence T ≥ 6 (CAP-R's first inequality);
  - the Howard runs of all 956 Ξ-cyclic variants have T ≤ 5;
  - Odd contributes R ≤ 2, and C ≤ 3.
  - So both the S4a mechanism and the doubling disappear under Howard, and the Odd steps that appear are too few to rebuild them.
- N5 (spec) on the same variants from S3 on Γ3: T3 ≤ 6. Each cycle edit also shortens the N5 run, so no variant is longer than the
  baseline under N5.

## 3. Climbs on 𝓛^R_d with Ξ-cycles (DATA)
- climb82.py: hill-climb on 𝓛^R_d genomes (2 movers per level, degree 2, R104 / R110 layout, any Ξ-targets including cycles).
  - Mutations: one Ξ-target, a β-rank swap, a parity bit, a gate swap, a start bit.
  - Accept if the score does not decrease. 20,000 mutations, seeds 1-3.
  - OBJ=R: score (R, T). OBJ=kf: score (capped height under Howard, flips of the next level (cut at its cap), R, T).
- Unit: the best genome of each climb. Set: 3 seeds per d. Scope: the stored start, IDEAL-CYC Howard.

| d | N | best R (seeds 1-3) | its T | kf: capped height (seeds 1-3) | kf: next-level flips / cap | kf: T |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | 4 | 2, 2, 1 | 6 | - | - | - |
| 3 | 6 | 3, 5, 3 | 9 | 2, 2, 2 | 7, 7, 6 / 14 | 9, 9, 8 |
| 4 | 8 | 6, 7, 7 | 11, 8, 11 | 2, 2, 2 | 8, 9, 8 / 14 | 9, 11, 8 |
| 5 | 10 | 6, 8, 9 | 15, 17, 12 | 2, 2, 2 | 8, 11, 9 / 14 | 14, 15, 11 |
| 6 | 12 | 10, 10, 9 | 18, 14, 15 | 3, 2, 2 | 12 / 30, 11 / 14, 12 / 14 | 20, 15, 17 |

- Anatomy of four best genomes (anal82.py; per level l: GF = σ̄ changes at level-l gates, RF = R-steps changing a level-l gate, MV =
  mover moves, KF = key flips):
  - best_kf_d6_s1: T 20, labels CCCCRRCRCppppRpRRCpp, R 6, C 7, KF 2, 6, 14, 12, 3, 6, GF 0, 12, 6, 12, 5, 11, 12 simple Ξ-cycles,
    U(G) 10, max ascents 1.
  - best_R_d6_s1: R 10, T 18, KF 5, 3, 5, 3, 5, 3 (no capped level), max ascents 2.
  - best_R_d6_s2: R 10, T 14, max ascents 2.
  - best_R_d5_s3: R 9, T 12, max ascents 2.
  - GF(0) = 0 in all four: R118's LEVEL0 («σ̄ takes the β-face at every gate of a level-0 mover»). Odd's activity starts at level 1.
- Real runners (box81/real81.py on Γ3 from S3): N5′-xi's mover phase equals Howard on best_kf_d6_s1 and best_R_d6_s2, with T3 = 20 and
  14. N5 (spec) makes 5 and 6 iterations there.
  - So on these Ξ-cyclic genomes N5′-xi is the slower of the two: the reverse of the towers.
- ≥ 2-ascent plays (box81/census81.py --loc on best_R_d5_s3; unit play, set all plays, scope stored start):
  - 5 plays at state 9 have 2 ascents; all start at e-vertices (levels 1-2).
  - Each ascent's segment contains an upward Ξ-edge: (lev 0 → lev 2), (lev 1 → lev 3), or (lev 1 → lev 4) (UP-JUMP holds).
  - UP-B: max 2 ≤ U(G) 8. HUB-ASC-G, OVT-DV, R-SPLIT: 0 failures.
- READING: at d ≤ 6 the climbs reach R ≈ 2d − 2 and a Howard capped height ≤ 3. Both are within what CAP-R allows with C + R linear in
  N. No climb shows R doubling per level. Climbs are weak evidence: they do not exclude a hand-built counter.

## 4. Next (proposal)
1. Hand design, following the reduction: a 2-level gadget where one Odd R-step at level l + 1 re-arms two R-steps at level l, the
   counter form of the doubling. Start from best_kf_d6_s1's level-1/2 block (RF 5, 2) and L-RED's RS2 (2-bit, R 4). Read L-RED 56's
   LADDER item first (the Lead has routed the reduction there).
2. A lemma bounding R per level by the activity one level up (the obstruction side), if the gadget fails in a way that generalises.
3. Hand best_R_d5_s3 to L-NEW as a RECUR(2) test instance (frozen in experiments/si/box82/out/climbR/, pins.sha1).
