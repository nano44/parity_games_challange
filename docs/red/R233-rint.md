# R233: adversary on L-NEW 71 BOX 207 (Q2) / CONJECTURE R-INT: growing CFI3's clock lane (L-RED successor 65)
Written 2026-11-12 (date -u in the commit). Target: claude/l-new 2d599a09, docs/new/N5-RLOCAL-box207.md (Lemma R-LOCAL, CONJECTURE R-INT:
«at k = 1, λ_max (the most loud steps inside one window of constant class(R)) is polynomial in N + M»). Lead 06:32Z / 07:59Z: «Grow that
clock lane: can the loud steps per R-window be made super-linear? Use at most 2 hand-built designs at 3+ sizes, or give the exact
obstruction.» Engine: experiments/red/r221q/own.py (IDEAL-CYC); tools experiments/red/r233/window233.py, lane233.py; no L-NEW code run.
Labels: DATA (unit, set, scope) / DEAD / READING. Frozen: experiments/red/r233/inst/ (SHA1SUMS; CFI3_n48 d55b20b8 and RINT_n48 35b48913
= L-NEW's sha1s).

## 1. Reproduction: AGREEMENT (window233.py; out/window233.out)
- Unit: windows of constant class(R) = (Λ(R), E(R)); loud = some vertex of Γ(G) changes class; R = the feedback vertex box 207 names.
  Box 207's convention: the step that changes class(R) is counted in the window it ENDS (WCONV=start gives the other convention;
  out/window233_startconv.out).
- Every number of box 207's §4 table that I re-ran matches exactly:
  | genome | T | R | D^tot(R) | λ_max | window | cint | flipint |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | CFI3_n48 | 24 | 29 | 3 | 11 | [4, 18] | 4 | 3 |
  | RINT_n48 | 24 | 29 | 2 | 22 | [2, 24] | 7 | 3 |
  | MWR8_2 | 54 | 83 | 18 | 8 | [1, 8] | 2 | 2 |
  | CWRR8_n | 52 | 83 | 3 | 43 | [9, 52] | 2 | 1 |
  | K1L10_n48 | 31 | 28 | 15 | 7 | [9, 15] | 2 | 2 |
## 2. Two hand-built growths (lane233.py, own builder; k = 1 on every instance)
- Design 1 LONG(L): L new lane movers (options [Ξ next, X], start X) inserted between 16 and 17 of CFI3's lane 9 → … → 16 → 17 → 33.
- Design 2 NEST(L): a second lane B of L movers ending at lane A's middle mover 12, plus an option of A's head 9 into B's first mover.
- DATA (unit as §1; set LONG(L), NEST(L); scope all vertices):
  | design | L | N | M | T | D^tot(R) | λ_max | cint | flipint |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | LONG | 0 (= CFI3) / 8 / 16 / 32 | 48 / 56 / 64 / 80 | 97 / 113 / 129 / 161 | 24 / 24 / 32 / 48 | 3 | 11 / 9 / 17 / 33 | 4 / 3 / 3 / 3 | 3 |
  | NEST | 4 / 8 / 16 / 32 | 52 / 56 / 64 / 80 | 106 / 114 / 130 / 162 | 9 / 13 / 21 / 37 | 2 | 5 / 9 / 17 / 33 | 2 | 2 |
- λ_max = L + 1 for L ≥ 16 in both designs: LINEAR in the lane length. cint (most class changes of one vertex inside one window) stays
  2-4 and flipint 2-3, constant in L. NEST also kills CFI3's original window (T 9 at L = 4).
## 3. DEAD and the obstruction
- DEAD «a longer or nested clock lane makes λ_max super-linear» for these two designs (killing instances inst/LONG_32.json, sha1 3dbfee5e,
  λ_max 33 = L + 1; inst/NEST_32.json, sha1 92854dc9, λ_max 33).
- Obstruction (DATA): inside one window every vertex changes class at most cint ≤ 4 times on these instances (≤ 7 on RINT_n48). The lane is
  one pass: each lane mover switches X → next once, and nothing re-arms it while class(R) is constant. A nested lane B only adds its own
  single pass (NEST: λ_max = L + 1, not (L + 1)·|A|).
- Remark (trivial, PROVED): λ(W) ≤ Σ_v (class changes of v inside W) ≤ n · cint(W), n = |Γ(G)| = N + 3M + 6. So R-INT follows from «the per-vertex class changes
  inside one R-window are polynomial». Every set measured has cint ≤ 7. A super-linear λ_max needs a vertex that changes class
  super-polynomially often with class(R) frozen: a re-armed lane inside one window. That is the same missing resource as the re-armed carry
  (R231-cwr, R231-rearm2, ONE-CROSS).
- READING: inside a window R behaves like a terminal of fixed class, so the window looks like the Ξ-acyclic case (R122 ACYC-LIN, T ≤ N)
  with one non-standard terminal. Box 207 §5 shows ACYC-LIN's hypothesis fails, but the lanes measured here still run one pass, linear in
  the lane length. This adds no proof.
