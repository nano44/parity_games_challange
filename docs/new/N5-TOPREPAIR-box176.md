# Box 176 N5-TOPREPAIR: the repaired TOP-C — the data support gain′ ≤ n₂ + 3·m_c (m_c = steps moving a coupled top mover = proxy changes), which reproduces TOP-ADD at m_c = 0; but m_c is bounded only through the flips of the pair just below the top, so summed over levels it gives O(3^d), no better than LEVEL-PRODUCT; dd_d5_F14 forces the per-move term (its lower part runs ≤ 1 step under all 266 re-routings, the genome runs 14)
L-NEW successor 55, 2026-11-06 (from 01:59Z, date -u: see the commit). Lead brief BOX 176 (01:57Z): repair TOP-C with the right
resource (top moves m, or distinct proxy states), test on all files incl. L-RED R207 / R208, check TOP-ADD and the level sum; if every
repaired form sums to LEVEL-PRODUCT, say so with the instance that forces it. Labels: PROVED (lane, unrefereed) / DATA / CONJECTURE /
DEAD / READING. Model: RESULTS R104's definition (P-IDEAL-KEYS §0). Not a TARGET.md claim. G-N5-TIME and SLOT-TRADE stay OPEN.

## 0. Answer
- R208 opened (claude/l-red 16ae702d, docs/red/R208-topcouple.md, now on origin). Its definition: «Robust gain: gain′(G) := T(G) − max
  over all re-routings r of T(G^-_r), where r sends each coupling to X or to any lower mover (keeping acyclicity) and G^-_r deletes U.»
  This is the definition box 175 used (same start, as TOP-ADD), so box 175's kill of TOP-C at C = 1 stands as stated.
- Resources (box176/repair.py; stored starts): n₂ := #two-option top movers (TOP-ADD's constant); m := #steps moving a top mover;
  m_c := #steps moving a COUPLED top mover (the Ξ-target of some coupling) = #changes of R208's TOP-SPLIT proxies (a proxy copies its top
  mover's current option, so it changes exactly when that mover moves); p_c := #distinct proxy tuples visited.
- (1) Forms tested on 372 genome files (in-tree boxes 150-175 and claude/l-red 16ae702d experiments/red, incl. R207 keep/ and R208 keep/;
  degree ≤ 2; 341 distinct (file, T, gain′, C) rows; box176/forms.py, log/forms_all.txt):
  | form | violations / 372 | worst instance |
  | --- | --- | --- |
  | FA = TOP-C with TOP-ADD's constant: gain′ ≤ n₂ + C | 53 | dd_d5_F14: gain′ 13, C 4 |
  | FB (one step per proxy change): gain′ ≤ n₂ + m_c | 34 | iso_d4_st9: 8 > 2 + 3 |
  | FD (per coupling, one step per move of its target): gain′ ≤ n₂ + Σ_couplings (1 + moves(target)) | 2 | iso_d4_st9 8 > 6; pm_d5_w2_s3 8 > 7 |
  | FC: gain′ ≤ n₂ + c·m_c, smallest c fitting all files | c = 3 fits (0 violations) | (gain′ − n₂)/m_c = 3.0 on pm_d5_w2_s3 (C 2, m_c 2, gain′ 8), ISO_1_d4_t11 (C 4, m_c 2, gain′ 8), climbI2_d3_LR_s103 (C 5, m_c 1, gain′ 5); 2.2 on dd_d5_F14 (m_c 5, gain′ 13) |
  - L-RED's R208 keep files (top extensions of R207 champions): gain′ 2-4 at m_c 3-11, (gain′ − n₂)/m_c ≤ 0.29: the climbs that build long runs do
    NOT use the per-move gain; the 2-wide small genomes do.
  - CONJECTURE TOP-M (sharpest form the data support): gain′ ≤ n₂ + 3·m_c. DATA only (0 violations on 372 files); no proof.
- TOP-ADD check: at C = 0 there is no coupled top mover, m_c = 0, and TOP-M reads gain′ ≤ n₂, which is TOP-ADD (R207 §1, with its exact
  constant #two-option top movers). DATA: on the 186 rows with m_c = 0 the largest gain′ is 3 (gate_K3_m2, n₂ = 6).
- (2) Level sum (READING with the bounds that are proved in the lane). TOP-M gives T(G) ≤ T*(d − 1) + n₂ + 3 m_c, since every re-routed
  G^-_r is a (d − 1)-level genome of the same class. m_c ≤ Σ_(coupled u) moves(u) ≤ 2 (1 + F(τ − 1)) (P-IDEAL-KEYS PAIR-MOVES on 𝓛^R_d;
  F(τ − 1) := flips of the level-(τ − 1) pair in G's run). The only bounds on F(τ − 1) are F ≤ T(G) (circular) and LADDER's
  F(τ − 1) ≤ 3^τ − 1. So T*(d) ≤ T*(d − 1) + 2 + 6·3^(d−1), i.e. T*(d) = O(3^d): the same order as LEVEL-PRODUCT (T + 1 ≤ 3^d on
  a 2-wide ladder). Every form tested is linear in a top-move resource (m, m_c, p_c ≤ 1 + m_c, or moves of targets), so every one sums
  the same way: no repaired TOP-C is a polynomial route unless the top-move resource is itself bounded by poly(d) — which is PAIR-LIN /
  SLOT-TRADE.
- The instance that forces the per-move term (DATA, two simulators): dd_d5_F14 (box172/inst/dd_d5_F14.json, sha1 06f0e501…; 𝓛^R_5;
  C = 4 couplings (1, 0), (2, 0), (4, 1), (5, 0)). T(G) = 14, while T(G^-_r) ≤ 1 under every one of its 266 acyclic re-routings (box175/
  xgain.py, L-RED's r187/ideal.py; the same with box175/gain.py): gain′ = 13 = 14 − 1. So 13 of the 14 steps exist only through the
  top level; any additive bound needs a term that grows with the top's activity (here m_c = 5). The top movers 8, 9 read the pair
  (6, 7), whose flip count F(3) = 14 = T (P-IDEAL-KEYS §8 DATA): the resource is as large as the quantity to be bounded.
- Verdict: DEAD as a route (READING, with the instance): TOP-C repaired by any top-move resource sums to O(3^d), no better than
  LEVEL-PRODUCT. TOP-M itself survives as DATA (0 violations) but carries no polynomial consequence on its own.

## 1. Files (experiments/new/box176/)
- repair.py (per-file T, C, gain′, m, m_c, p_c, lowph; also a «rearm» count whose stuck-test reads only A-sets, not keys, so it is
  NOT used anywhere here), forms.py (FA, FB, FD violations, FC ratios); log/repair_all.txt, log/forms_all.txt.

## 2. Next (Lead decides)
- A polynomial route through the top level needs m_c ≤ poly(d) for coupled top movers on 2-wide genomes, i.e. a bound on how often the
  pair below the top flips while the top is Ξ-coupled — PAIR-LIN at the top pair. That is where L-RED's R209 bases should push (their
  climbs keep (gain′ − n₂)/m_c ≤ 0.29; the small 2-wide genomes reach 3).
