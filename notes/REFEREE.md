# REFEREE notebook
Overwrite the top sections; append to "Sources opened" and "Dead ends".

## Resume point
R1 (audit of arXiv 2511.03752 v1): report written, verdict BROKEN: docs/referee/2026-10-14-arxiv-2511.03752.md.
Counterexamples cex1 (4 vertices) and cex2 (4 vertices, solitaire) in docs/referee/scratch/, with max-parity twins for Oink
and Oink's .sol files. Faithful implementation of Alg. 1 with all 16 readings: docs/referee/scratch/aiayn.py (run with python3 -I).
M2 closed as BROKEN by the Lead (trunk fa543a3). R1 step 3 done: AM1-AM9 verdicts in section 10 of the report (all faithful).
PGSolver generator ports checked: docs/referee/2026-10-14-pgsolver-ports.md (OK, two cosmetic citation findings).
Theorem numbering: the paper's shared counter (Theorem 2 = dominion, Lemma 3 = minimal dominion, Lemma 4 = progress); my
first two messages to the Lead were off by one. Idle until the Lead routes the next item.

## Queue
- (empty) Possible follow-ups if routed: output diff of the ports against real PGSolver binaries (needs Q4); L-COMP's
  pgsolver_si.py (switch-all strategy improvement port) was not in scope and is unchecked.

## Things only I know
- Paper is MIN-parity (lowest priority seen infinitely often decides). PGSolver/Oink are MAX-parity. Convert p -> M - p, M even >= max p.
  On cex1 the max-parity reading of the SAME priorities happens to give Odd everywhere, which coincides with the algorithm's
  (wrong) output: anyone who runs the paper's algorithm with min-parity but checks it against Oink on the unconverted file
  will see false agreement. Use the converted twin file for Oink.
- The paper's PDF (sha256 61060b71...) and e-print tarball (4dc6c4b9...) are in my scratchpad only (untrusted downloads, not committed).

## Sources opened
| source (arXiv id / DOI) | result used (theorem / section) | opened on | note |
| --- | --- | --- | --- |
| github.com/tcsprojects/pgsolver d3cd624 | recursiveladder.ml 13-46; policyiter/generators/switchallexp.ml 30-66, switchbestexp.ml 34-74; policyiter/stratimprgenerators.ml 7-47; paritygame.ml 19, 25-40, 128-139, 175, 201-206, 365-387 | 2026-10-14 | OCaml originals of L-COMP's ports; cloned into scratchpad |
| arXiv:2511.03752v1 | whole paper: Sec. 2 defs, Sec. 3 (A*, A', A^k, Thm 1, Lemma 2, Alg. 1, Lemma 3, Thm 4, 5, 6) | 2026-10-14 | PDF + LaTeX source (main.tex); 4 pages; only v1 exists |

## Dead ends
(none)
