# PGSolver binary diff (Lead reading L15; L-COMP, 2026-10-15 23:15-23:30Z)
One attempt, as ruled: build the original PGSolver at github.com/tcsprojects/pgsolver d3cd624 and diff the Python ports
used for M1 (pgsolver_port.py, pgsolver_si.py) against its binaries. The permission classifier did NOT refuse this time; no
workaround was needed or used.

Build (fresh container; under out/pgsolver, gitignored): apt ocaml 4.14.1, ocaml-dune 3.14.0, ocaml-findlib,
libextlib-ocaml-dev, libnum-ocaml-dev; clones pgsolver d3cd624, tcslib 6778419, ocaml-sat-solvers 0264291,
c-cube/ocaml-minisat aeb7776 in one dune workspace; two local edits (every dune-project `(lang dune 3.x)` -> 3.14,
`maintenance_intent` line removed); `dune build ./pgsolver/src/apps`.

## Generators: byte-for-byte
`generator.exe -gen recursiveladder N` and `stratimprgen.exe -pg {switchallexp,switchbestexp} "N"` vs
`python3 pgsolver_port.py GEN N`, N = 1, 2, 3, 4, 5, 6, 8, 10, 16: IDENTICAL (cmp) for all 27 (family, N) pairs.
(friedmannsubexp and fearnleysubexp: ported 2026-10-29 (L-COMP box 21, experiments/n5-box21/README.md); NOT binary-diffed: the PGSolver build was refused by the permission classifier that day.)

## Strategy improvement loop: iteration counts and solutions
`pgsolver.exe -global policyiter -x "-sa"|"-sb" -dgo -dsd -dlo -dsg -v 3 GAME` (switchall / switchbest, all preprocessing
off) vs `python3 pgsolver_si.py GAME OUT [--switchbest]` on the binary-generated games. PGSolver logs "Iteration: i" for
i = 0..K-1; the port logs K.
| family | N = 1 | 2 | 3 | 4 | 5 | 6 | 8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| switchallexp, switchall: binary K / port K | 11/11 | 31/31 | 71/71 | 151/151 | 311/311 | 631/631 | 2487/2487 |
| switchbestexp, switchbest: binary K / port K | 23/23 | 61/61 | 137/137 | 289/289 | 593/593 | 1201/1201 | 4849/4849 |
Final solutions at N = 4 (`--printsolonly` vs the port's solution file): regions AND strategies identical on all 63 / 110
vertices.

## Verdict
The ports used for M1 (Lead reading L5) agree with the original binaries: generators byte-identical, SI iteration counts
identical, solutions identical. L5's port-based confirmation of switchallexp / switchbestexp / recursiveladder now also
rests on the original binaries. (A first switchbest attempt passed an empty -x flag by a scripting slip and ran a different
solver; the numbers above are from the corrected `-x "-sb"` run.)
