# REFEREE notebook
Overwrite the top sections; append to "Sources opened" and "Dead ends".

## Resume point
R1 (audit of arXiv 2511.03752 v1) in progress, deadline 2026-10-16 18:30Z. Verdict so far: BROKEN.
Counterexample found and reported to the Lead (docs/referee/scratch/cex1-minparity.pg, max-parity twin cex1-maxparity.pg).
Faithful throwaway implementation: docs/referee/scratch/aiayn.py (min-parity, flags for the two ambiguous readings).
Next: full report docs/referee/2026-10-14-arxiv-2511.03752.md; then wait for the Lead to route L-COMP's pseudocode (R1 step 3).

## Queue
- R1 step 1: full report (in progress).
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
