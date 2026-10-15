# docs/alg (L-ALG): algorithm design loop for M4 (TARGET.md section 2)
- candidates/C<k>.md: one file per candidate, written before its tests: exact pseudocode, soundness, running time in the
  TARGET section 3 model, barrier reading, falsification plan.
- DEAD.md: dead candidates, each with the smallest failing instance (experiments/alg/instances/), the exact obstruction,
  and which idea it kills.
- RESULTS.md: what the loop has measured (data, unrefereed).
Code: experiments/alg/ (ne.py solver for C1/C2, test drivers, instances/). Notebook: notes/L-ALG.md.
