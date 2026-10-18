# Box 1 (i): S5 (Zadeh, index tie-break) and S6 (Cunningham, index order) as a fast kill test (L-NEW, 2026-10-18)

Rules exactly as L-SI's S5.md / S6.md (engine: experiments/new/renum.cpp, which runs a verbatim copy of L-SI's vjfast.cpp;
best-reward start; identity counts equal vjfast on 5 pinned instances, check.sh pins zadehexp_N5 = 271).
Adversary: a hill climb over vertex renumberings (1-3 random swaps per step, sideways moves allowed; identity, reversal and
3 random restarts, 400 steps each). A renumbering moves (a) the priority-rank ties, (b) the best-reward start ties,
(c) the zadeh tie-break / the cunningham cyclic order. Earlier work on the same question: L-RED R4, R6, R7 (docs/red/),
which found no super-polynomial scheme and showed DFH's and Avis-Friedmann's orders are not index orders.

## Verdict so far: NOT KILLED (neither rule). No numbering with super-polynomial growth found.
Iterations, identity numbering -> best numbering found (experiments/new/out/renum/summary.csv; sweep still running for
gated_*, switchallexp, switchbestexp, recursiveladder; Oink hard bench not yet included):
| family (N = 2..6) | zadeh identity | zadeh best | cunningham identity | cunningham best |
| --- | --- | --- | --- | --- |
| zadehexp | 19, 71, 155, 271, 419 | 39, 111, 189, 323, 469 | 15, 41, 53, 73, 85 | 37, 81, 149, 213, 323 |
| cunninghamexp | 3, 6, 9, 12, 15 | 7, 30, 63, 104, 155 | 3, 6, 9, 12, 15 | 7, 24, 49, 76, 101 |
| randomfacetsubexp (n = 20, 68, 90, 207, 248) | 8, 71, 99, 320, 389 | 13, 136, 219, 759, >=1162 (timeout) | 4, 59, 88, 280, 354 | 13, 110, 186, 623, >=798 (timeout) |
| dlmm_ML | 6, 10, 14, 18, 22 | same | 2, 2, 2, 2, 2 | 6, 10, 18, 22, 24 |
| dlmm_bland | 1, 2, 5, 8, 13 | same | 1, 2, 5, 6, 9 | 1, 2, 5, 8, 11 |
| gated_bland | 3, 5, 7, 9, 11 | same | 3, 5, 9, 11, 15 | 3, 5, 9, 13, 17 |
| fhz_padded (n = 64..322) | 16, 36, 64, 100, 144 | 22, 45, 74, 112, 161 | 16, 32, 48, 64, 80 | 23, 40, 67, 83, 113 |
Growth of the best-found counts is at most quadratic in N on every family (e.g. zadehexp/zadeh second differences 0..+70
over N; cunninghamexp/zadeh 23, 33, 41, 51 first differences). randomfacetsubexp grows with n (n jumps 90 -> 207 at N = 5);
per vertex it is not faster than the identity.

## Why the rules might still fall (honest)
- A hill climb over n! numberings is weak evidence; R7 showed the best-found Zadeh numberings on zadehexp fall to 13% of the
  published tie-break's count by N = 7 while still growing by 1.5-1.9 per level at N <= 6. A counter built for a FIXED order
  (R7 section 5: one cycle per level or a fixed cycle order, escape records separating closed from open levels) is the open
  design problem for S5; a block-order (contiguous per vertex) round-robin counter is the one for S6 (R4).
- Neither rule is covered by a published lower bound (L-SI S5.md, S6.md; L-RED R4, R7).
Not recorded as dead ends. Status in docs/new/README.md: "not killed (fast test), not defended".
