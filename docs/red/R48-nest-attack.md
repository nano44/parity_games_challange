# R48: attack on (NEST*-BOUNDED) on 𝒞^1P, box 15 data (L-RED; produced on Opus 5.5)
Status: DATA, no kill. Written 2026-10-19 02:25Z (date -u). Target: Lead 01:14Z and 02:04Z (date -u). If R47 signs, (NEST*-BOUNDED)
"NEST* ≤ c on 𝒞^1P" is the only open statement for GAP-A on 𝒞^1P (R46 §3, R47 §5). The attack: a class family whose NEST* grows with n.
Tools (experiments/red/xctx/): nestclass.py (STAR=1 ranks by NEST*), neststarscan.py, comb/neststar.py.

## 1. Library scan
neststarscan.py over L-ALG's class set: experiments/alg/instances, experiments/red/*/instances and tcpert/instances/prod, with
classgames DIST=1 (in-class files as given, others forced into 𝒞_C, 3 trials), stable order.
- 955 q-phases. NEST* histogram: 0: 540, 1: 397, 2: 16, 3: 2.
- The two NEST* 3 phases are this lane's climbed instances nest3_n24 (S 18) and nest3_n20 (S 11).
- Every forced conversion of a two-player family, including leanT, lagfam's depth3/4 and nest4_n80, has NEST* ≤ 2.
- nest4_n80 has NEST 4 as a two-player game (R41), but is ≤ 2 after forcing.

## 2. A parametrised family
lagfam.py D (R39), forced into 𝒞_C: D = 4, 8, 12, 16 (n = 50, 78, 106, 134). Best q-phase NEST* is 1 at every D, with S = 11, 15, 19, 23
(D + 7, linear). No growth of NEST* with n.

## 3. Climbs (this box)
- nestclass.py with NEST, then with NEST* (STAR=1), class moves, vertex insertions to n ≤ 50-60. Seeds nest3_n20 and nest3_n24,
  both orders, 00:59-02:25Z (date -u), interrupted by the ~01:45Z worker restart and then restarted.
- Plateau: NEST* = NEST = 3, S ≤ 21 at n 24 (about 0.9 n).
- In the NEST-3 instances inspected with tlog.py, carries are case-G absorptions into −1 pieces, from the last stable piece, which acts as the learning
  pool. A fourth level needs a middle position that re-rises twice with deeper rises in between (R45 (N1) one level deeper). The
  climbs never produce it.

## 4. Reading
Nothing found contradicts (NEST*-BOUNDED). There is no proof either. The structural reason the climbs stall is open: every observed
carry goes from the deepest stable piece to one −1 piece, so carries do not chain through intermediate levels. A construction that
makes a −1 piece's own outcome rise feed a second, shallower −1 piece is the concrete next target. A proof that a −1 piece's rise
can only be fed from the deepest stable piece would be the matching obstruction.
