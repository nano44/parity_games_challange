# P-IDEAL-ALIGN fixes (append-only; the packet docs/new/P-IDEAL-ALIGN.md, sha1 d8acdece…, stays frozen)

## Entry 1 (2026-11-06 from 05:3xZ by date -u; L-NEW successor 55; Lead relay 05:32Z of fix round 1)
- Reports answered: REFEREE 24, claude/referee 6f0daf60, docs/referee/R-P-IDEAL-ALIGN.md (AL-L1 required; AL-L2, AL-P1 optional);
  REFEREE-2 28, claude/referee-2 ea08029d, docs/referee-2/R2-P-IDEAL-ALIGN.md (P-1, P-2 optional). Both sign all seven statements; no
  statement, proof or hypothesis changes here. This entry carries no proof.

### F-a (AL-L1): the two DATA ranges of the line, checked against the counter code
- experiments/new/box178/aligncheck.py (unchanged, sha1 9335dee7…): LAND (ALIGN (b)) is counted under «if t and …» (l. 52), i.e. only
  at states with t ≥ 1; KPEQ (ALIGN (a)) and ORD (ALIGN (c)) on every (state, level ≥ 1) pair. aligncheck.out (unchanged, sha1
  b653b01b…): «statelevels 22472», «runlevels 10648» (one start state per (run, level)), so (b) covers 22,472 − 10,648 = 11,824 pairs.
- KFF (KF_x = F(l − 1)) is counted under «if l >= 1 and …» (l. 67), MOV (the moves bound) on every (run, mover) pair: «runmovers 32620»,
  «runs 5662» with 2 level-0 movers each, so KF_x = F(l − 1) covers 32,620 − 2·5,662 = 21,296 pairs.
- Packet §7 reads accordingly: «ALIGN (a) and (c): 22,472 (state, level ≥ 1) pairs, 0 violations each; ALIGN (b): checked at every
  step of the same runs, 0» stands (the step-wise wording is correct); «Corollary MOVES (…): 32,620 (run, mover) pairs, 0 violations
  each» is to be read: the moves bound on 32,620 pairs, KF_x = F(l − 1) on the 21,296 with level ≥ 1.

### F-b (AL-P1): §5 «Does NOT claim» of Corollary T-BOUND, the T^R values are lane DATA
- Replace «(T^R(d) = 2, 4, 8, 13 for d = 1-4 by L-RED's exact data, against 2^(d+2) − 2d − 4 = 2, 8, 22, 52; equal at d = 1 only)» by
  «(lane DATA, not landed and not used by any statement: T^R(1) = 2 and T^R(2) = 4 lane-exact, T^R(3) = 8 = packet P-TR3 (signed, not
  yet landed), T^R(4) = 13 L-RED's machine result under lane side constraints (REFEREE AL-P1: notes/L-RED.md l. 406,
  docs/red/R197-alt.md l. 34), against 2^(d+2) − 2d − 4 = 2, 8, 22, 52; equal at d = 1 only)». The line L-1 / L-2 quotes none of these
  values.

### F-c (P-1, P-2 = AL-L2): line only
- P-1 defines g in γ_l; P-2 / AL-L2 qualifies «improving»: at d = 1, 2 the bounds 3^d − 1 and 2^(d+2) − 2d − 4 are both 2 and 8; from
  d = 3 the new one is strictly smaller (22 < 26). The packet's §5 needs no change for P-1 (§0 defines g(x, k) as the gate index).

### Line L-2 (docs/new/P-IDEAL-ALIGN-line-L2.txt, sha1 cb5f0398431cc1a5122e13327e7bbae9f9985e51, 1 line, 3,330 bytes, 0 «|», 76 «(» =
  76 «)», depth never negative)
- L-2 = L-1 (e46b0417) with exactly these five replacements, applied by script; R1 and R2 copied from REFEREE §5 «Fix: «…»», R3 and R4
  from REFEREE-2's P-1 / P-2 «→ «…»» (wrapped lines joined by single spaces); each old string occurs exactly once in L-1:
  - R1 (AL-L1 (i), REFEREE §5): «ALIGN 0 violations on 22,472 (state, level ≥ 1) pairs» → «ALIGN (a) and (c) 0 violations on 22,472 (state, level ≥ 1) pairs and (b) on the 11,824 of them with t ≥ 1»
  - R2 (AL-L1 (ii), REFEREE §5): «MOVES 0 on 32,620 (run, mover) pairs» → «MOVES 0 on 32,620 (run, mover) pairs for the moves bound and on the 21,296 with level ≥ 1 for KF_x = F(l − 1)»
  - R3 (REFEREE-2 P-1): «γ_l(j) := [g(2l, j) < g(2l + 1, j)]» → «γ_l(j) := [g(2l, j) < g(2l + 1, j)] with g(x, k) the gate index of option (x, k)»
  - R4 (REFEREE-2 P-2 = REFEREE AL-L2): «improving RESULTS R108's bound T ≤ 3^d − 1 to T ≤ 2^(d+2) − 2d − 4 on 𝓛^R_d» → «improving RESULTS R108's bound T ≤ 3^d − 1 to T ≤ 2^(d+2) − 2d − 4 on 𝓛^R_d (strictly for d ≥ 3; equal at d = 1, 2)»
  - R5 (source note names the fixes file): «(P-IDEAL-ALIGN, docs/new/P-IDEAL-ALIGN.md; L-NEW successor 55)» → «(P-IDEAL-ALIGN, docs/new/P-IDEAL-ALIGN.md with its fixes entry 1, docs/new/P-IDEAL-ALIGN-fixes.md; L-NEW successor 55)»
- Word diff L-1 → L-2 (git diff --no-index --word-diff=plain; [-removed-] {+added+}):
  [-j)],-]
  {+j)] with g(x, k) the gate index of option (x, k),+}
  [-𝓛^R_d;-]
  {+𝓛^R_d (strictly for d ≥ 3; equal at d = 1, 2);+}
  {+(a) and (c)+}
  [-pairs;-]
  {+pairs and (b) on the 11,824 of them with t ≥ 1;+}
  [-pairs;-]
  {+pairs for the moves bound and on the 21,296 with level ≥ 1 for KF_x = F(l − 1);+}
  [-docs/new/P-IDEAL-ALIGN.md;-]
  {+docs/new/P-IDEAL-ALIGN.md with its fixes entry 1, docs/new/P-IDEAL-ALIGN-fixes.md;+}
