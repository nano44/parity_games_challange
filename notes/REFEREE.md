# REFEREE notebook
Overwrite the top sections; append to "Sources opened" and "Dead ends".

## Resume point
R1 (audit of arXiv 2511.03752 v1): report written, verdict BROKEN: docs/referee/2026-10-14-arxiv-2511.03752.md.
Counterexamples cex1 (4 vertices) and cex2 (4 vertices, solitaire) in docs/referee/scratch/, with max-parity twins for Oink
and Oink's .sol files. Faithful implementation of Alg. 1 with all 16 readings: docs/referee/scratch/aiayn.py (run with python3 -I).
Lead informed (interim message 18:40Z, DONE message after the push). Waiting for the Lead to route L-COMP's pseudocode (R1 step 3).

## Queue
- R1 step 1: done (report pushed).
- R1 step 3: line-by-line faithfulness check of L-COMP's pseudocode (notes/L-COMP.md, branch claude/l-comp) when routed.
- Later: PGSolver generator ports (recursiveladder, switchallexp, switchbestexp) vs OCaml source, when routed.

## Things only I know
- Paper is MIN-parity (lowest priority seen infinitely often decides). PGSolver/Oink are MAX-parity. Convert p -> M - p, M even >= max p.
  On cex1 the max-parity reading of the SAME priorities happens to give Odd everywhere, which coincides with the algorithm's
  (wrong) output: anyone who runs the paper's algorithm with min-parity but checks it against Oink on the unconverted file
  will see false agreement. Use the converted twin file for Oink.
- The paper's PDF (sha256 61060b71...) and e-print tarball (4dc6c4b9...) are in my scratchpad only (untrusted downloads, not committed).

## Sources opened
| source (arXiv id / DOI) | result used (theorem / section) | opened on | note |
| --- | --- | --- | --- |
| arXiv:2511.03752v1 | whole paper: Sec. 2 defs, Sec. 3 (A*, A', A^k, Thm 1, Lemma 2, Alg. 1, Lemma 3, Thm 4, 5, 6) | 2026-10-14 | PDF + LaTeX source (main.tex); 4 pages; only v1 exists |

## Dead ends
(none)
