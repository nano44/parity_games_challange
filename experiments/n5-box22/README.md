# Box 22: independent reproduction of L-RED's fcN (R115) under N5-SF and N5 (L-COMP successor 7)
Lead brief 2026-10-29 17:49Z (D18). Subject: L-RED R115 (claude/l-red docs/red/R115-sf-quadratic-sbc.md). fcN = PGSolver switchbestexp N
minus the N edges CycleNode1(i) → CycleAccessDistributer (f_i → c); n = 25N + 10. Start: SPEC S3 (best reward) for both players.
All numbers are DATA. SF-POLY stays OPEN, and G-N5-TIME is not touched beyond the N5 column.

## Independent build and engine
- fcgen.py builds fcN from MY switchbestexp port (hard-families/pgsolver_port.py, byte-identical to the PGSolver d3cd624 binary,
  pgsolver-binary-diff.md). It removes exactly the edges "f<i>" → "c" and asserts that there are N of them. L-RED's sbev.py was NOT
  used or opened.
- Diff vs L-RED's pins: sha1 prefixes fc3 9af7ca12ace1, fc6 2fbe13a615f6 and fc10 53a8f01c3bfa are IDENTICAL to R115 §1.
- sfb.py: N5-SF on L-COMP's engine n5b (SPEC). It is box17.Eng.step with S4a's opponent τ replaced by σ̄ and S4b's opponent σ replaced
  by τ̄, written from docs/new/N5-SF-box54.md §1. This is a second implementation besides L-NEW's n5sf.py (n5x engine).
- sfxcheck.py: sfb.py's full state sequences and SBC_σ, SBC_τ equal n5sf.py's on fc3-fc6, fc8 and on 1,000 random games (n ≤ 9, S3 or a
  random start): 0 mismatches.

## Results (run22.py; results/run22_S3.log). Every row: N5-SF regions = Oink zlk @ 8fbf0a7, N5 regions = Oink, 0 fallbacks in both.
| N | n | sha1 | N5-SF it (sfb) | L-RED's it | SBC_σ | SBC_σ − N² | SBC_τ | N5 it (n5b) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 85 | 9af7ca12ace1 | 121 | 121 | 9 | 0 | 3 | 41 |
| 4 | 110 | 3562ec4d15eb | 215 | 215 | 16 | 0 | 4 | 47 |
| 5 | 135 | 6e9163038da7 | 346 | | 25 | 0 | 5 | 55 |
| 6 | 160 | 2fbe13a615f6 | 520 | 520 | 36 | 0 | 6 | 62 |
| 7 | 185 | 24bb76ffa168 | 743 | | 49 | 0 | 7 | 68 |
| 8 | 210 | a7cde7101dcf | 1,021 | 1,021 | 64 | 0 | 8 | 77 |
| 9 | 235 | 34aac6c8b4ac | 1,360 | | 81 | 0 | 9 | 83 |
| 10 | 260 | 53a8f01c3bfa | 1,753 | 1,753 | 100 | 0 | 10 | 89 |
| 11 | 285 | dfcb525e2ee5 | 2,219 | | 121 | 0 | 11 | 98 |
| 12 | 310 | c690a56dd72e | 2,764 | 2,764 | 144 | 0 | 12 | 104 |
| 13 | 335 | c55f3f85605e | 3,394 | | 169 | 0 | 13 | 110 |
| 14 | 360 | 33edd935ad71 | 4,115 | | 196 | 0 | 14 | 117 |
| 15 | 385 | 94e32943f176 | 4,945 | | 227 | **+2** | 15 | 123 |
| 16 | 410 | 249de4dfaf85 | 5,847 | 5,847 | 257 | +1 | 16 | 129 |
- L-RED's iteration counts are reproduced at every N it reported (3, 4, 6, 8, 10, 12, 16) by an independent build on an independent
  engine. So is SBC_σ = N² for N ≤ 14, and 257 at N = 16. New: N = 15 has SBC_σ = 227 = N² + 2, so "SBC_σ = N² exactly" fails
  from N = 15 (N² + 2 at 15, N² + 1 at 16). SBC_τ = N exactly.
- N5-SF iterations are cubic in N, as R115 says (e.g. 4,115 at N 14 vs 0.79N³ + 9.7N² = 4,069).
- N5 ITSELF on fcN is LINEAR: 41, 47, …, 129 for N = 3..16 (increments 6-9, ≈ 6.3N + 22), with 0 fallbacks. So fcN does nothing to
  N5's running time; the cubic count belongs to the single-frame variant only (G-N5-TIME: DATA, not a bound).

## DONE / FINDINGS / NEEDS
- DONE: fcgen.py, sfb.py, sfxcheck.py, run22.py; instances/fc3-fc16.pg; results/run22_S3.log.
- FINDINGS:
  1. R115 is independently reproduced (generator sha1s, N5-SF iteration counts, SBC_σ = N² for N ≤ 14).
  2. SBC_σ = N² + 2 at N = 15 and N² + 1 at N = 16, so "exactly N²" holds only for N ≤ 14.
  3. N5 on fcN is linear, ≈ 6.3N + 22, with no fallbacks.
- NEEDS: none.
