# R2-N5-DW: REFEREE-2 independent reproduction of L-RED 29's dwN counts (N5-SF and plain N5), D1 (designer ≠ falsifier)
REFEREE-2 successor 20, Opus 5.5 (D15, L37). Lead brief 18:31Z (date -u). Written 2026-10-29 from 18:31Z. No verdict asked: reproduced counts only.

**What was reproduced.** L-RED 29 reports (DATA, unpushed at brief time) a family dwN on which N5-SF makes 134 / 286 / 590 / 1198 / 2414
iterations at N = 3..7 (= 19·2^N − 18), with SBC_σ = 2^(N+1) − N − 2 and LAM 0, from the S3 start.

**Built from the description only.** No L-RED file, generator or code was used or read.
- Builder: R2-N5-DW/dw_build.py.
- Base games: PGSolver's switchbestexp N as copied on trunk, experiments/new/box54/out/switchbestexp_N.pg (sha1s: N=3 e1cd8f13, 4 57b27b74,
  5 84913ba8, 6 7348edf1, 7 23241724), with vertex names.
- fcN := remove the N edges f_i → c.
- dwN := fcN plus one Even repeater u_i, i = 0..N−2. The edge v_i → r_(i+1) is replaced by v_i → u_i. u_i has the edges {r_(i+1), v_i's other
  successor}. That other successor is v_(i+1) for i < N − 2; for i = N − 2 it is p, because v_(N−1) does not exist.
- u_i gets an odd priority 1 + 2(i + 1). Every other vertex except q is shifted by 2(N − 1) + 2, keeping parity. q keeps 1.
- n = 26N + 9 (87 / 113 / 139 / 165 / 191). Files: R2-N5-DW/inst/dwN.pg, with sha1s:

| N | sha1 |
| --- | --- |
| 3 | ea07fb2f |
| 4 | ba13715f |
| 5 | 7ba1e1f7 |
| 6 | 0e4e6eb0 |
| 7 | c393e5ac |

**Description points I had to settle.** Each choice is stated, with how it was tested:
- The last repeater's second edge (v_(N−1) does not exist): settled by reading "repeater" as a copy of v_i's choice. Variants A and B are
  identical: for i < N − 2 the other successor is v_(i+1).
- The order of the repeaters' odd priorities: irrelevant. "up" (u_0 lowest) and "down" give identical runs at N = 3, 4, 5 (logs/dw_down.txt).
- Whether q is shifted: q kept at 1, per "just above q's 1". Shifting q too gives 121 at N = 3, not 134.
- To do: diff these files against L-RED's pinned sha1s when the Lead sends them. Vertex numbering and names may differ even if the games are
  isomorphic.

## Results (my engines: N5-SF = R2-N5-SF/sf_check.run_sf on si.py; N5 = R2-N5-DUAL/dual_check.Runner on si.py; S3 start both sides)
Script R2-N5-DW/dw_run.py, log R2-N5-DW/logs/dw_up.txt.
| N | n | N5-SF iterations | 19·2^N − 18 | σ-changes | SBC_σ | 2^(N+1) − N − 2 | LAM_σ | τ-changes / SBC_τ / LAM_τ | fallbacks | plain N5 iterations | N5 fallbacks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 87 | 134 | 134 | 134 | 11 | 11 | 0 | 3 / 3 / 3 | 0 | 41 | 0 |
| 4 | 113 | 286 | 286 | 286 | 26 | 26 | 0 | 4 / 4 / 4 | 0 | 47 | 0 |
| 5 | 139 | 590 | 590 | 590 | 57 | 57 | 0 | 5 / 5 / 5 | 0 | 55 | 0 |
| 6 | 165 | 1198 | 1198 | 1198 | 120 | 120 | 0 | 6 / 6 / 6 | 0 | 62 | 0 |
| 7 | 191 | 2414 | 2414 | 2414 | 247 | 247 | 0 | 7 / 7 / 7 | 0 | 68 | 0 |

- **N5-SF: REPRODUCED EXACTLY.**
  - Iterations 19·2^N − 18 and SBC_σ = 2^(N+1) − N − 2, both at every N = 3..7. LAM_σ = 0. Every iteration changes σ.
  - τ changes N times, each change with a σ̄ and λ^U change.
  - No fallbacks.
  - Exponential: the count doubles plus a constant per step of N, while n grows by 26.
- **Plain N5 (the number that matters for G-N5-TIME): 41, 47, 55, 62, 68.**
  - Differences 6, 8, 7, 6: linear in N on these five points (about 6.75 per step), far from N5-SF's doubling.
  - On this family the gap between N5-SF and N5 is the opponent argument alone (σ̄(σ) vs τ in S4a).
- **WIN against Oink:**
  - Oink 8fbf0a7 (built here by scripts/setup_oink.sh, exit 0), `oink --zlk -v`, "solution verified" at every N (logs/oink_dw*.txt).
  - Odd wins every vertex at every N.
  - N5-SF's and N5's final λ-parity regions both equal Oink's winner at every vertex (logs/win_oink.txt).
  - zlk is not near its known abort cases (counter_m N = 41, 42).

## What this does and does not show
- DATA, not proof. The N5-SF counts match L-RED 29's figures from an independent build and an independent engine.
- With P-N5-SF's signed SF-RED (c) (SBC ≤ 2I, and I polynomial iff SBC polynomial), exponential SBC on a family is exactly what makes
  N5-SF exponential there. If the closed forms hold for all N, CONJECTURE SF-POLY is false on dwN. The DEAD label is the Lead's to assign
  from L-RED's report, with this as the independent reproduction.
- Plain N5 is NOT exponential on dwN (N ≤ 7). This family does not touch G-N5-TIME.

## DONE / FINDINGS / NEEDS
- DONE: dw_build.py, dw_run.py, inst/dw3-7.pg, logs (dw_up, dw_down, win_oink, oink_dw3-7).
- FINDINGS:
  - N5-SF on dwN: 134 / 286 / 590 / 1198 / 2414 iterations, SBC_σ 11 / 26 / 57 / 120 / 247, LAM 0. EXACT reproduction of L-RED 29.
  - Plain N5: 41 / 47 / 55 / 62 / 68, linear.
  - WIN: all match Oink's verified solutions.
- NEEDS: Lead: L-RED's generator SHA and pinned sha1s, to diff my dwN files (isomorphism if the numbering differs).

## Addendum (18:5xZ by date -u): isomorphism with L-RED's pins (Lead 18:50Z)
- Pins: L-RED experiments/red/sf/instances/dw_3..8.pg at claude/l-red 6e7acb3b. sha1 prefixes measured: e5f94c800324 / eba759c1e811 /
  c03e3e00578a / 34ad93bc62d0 / 6b40922a7950 / 5a7fe1cc2d78, equal to the Lead's. Trunk 0b3abd0f was not yet on origin at my fetch, so I read
  them from 6e7acb3b.
- Check: R2-N5-DW/iso_check.py, log logs/iso.txt. Vertices are matched by name, and the repeaters (mine u_i, L-RED's u_i_0) by their unique
  priority.
- Result, N = 3..7: all vertices matched, with 0 priority, 0 owner and 0 edge-set mismatches. My dwN and L-RED's dw_N are the SAME GAME up to
  vertex numbering, with identical priority values.
- At N = 4 and 6 (injective priorities) the priority map alone confirms it independently.
- In particular the last repeater u_(N−2) has edges {p, r_(N−1)} in both: my settled reading of "v_(N−1)" (= v_(N−2)'s other successor, p) is
  L-RED's construction.
