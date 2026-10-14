# REFEREE notebook
Overwrite the top sections; append to "Sources opened" and "Dead ends".

## Resume point
R1 (audit of arXiv 2511.03752 v1): report written, verdict BROKEN: docs/referee/2026-10-14-arxiv-2511.03752.md.
Counterexamples cex1 (4 vertices) and cex2 (4 vertices, solitaire) in docs/referee/scratch/, with max-parity twins for Oink
and Oink's .sol files. Faithful implementation of Alg. 1 with all 16 readings: docs/referee/scratch/aiayn.py (run with python3 -I).
M2 closed as BROKEN by the Lead (trunk fa543a3). R1 step 3 done: AM1-AM9 verdicts in section 10 of the report (all faithful).
PGSolver ports checked: docs/referee/2026-10-14-pgsolver-ports.md: Part A generators OK (two cosmetic citation findings);
Part B pgsolver_si.py (switchall, switchbest) OK, faithful to the bare SI loop = PGSolver with -dgo -dsd -dlo -dsg, not the
default binary (universal_solve preprocessing); regions match Oink on 150 random games; counts 10*2^n-9 and 19*2^n-15 (n<=6).
Theorem numbering: the paper's shared counter (Theorem 2 = dominion, Lemma 3 = minimal dominion, Lemma 4 = progress); my
first two messages to the Lead were off by one. Idle until the Lead routes the next item.

Harness review (l-comp a3777f1..de7ea19, experiments/): docs/referee/2026-10-14-harness-review.md, CHANGES (2 self-test coverage findings; code correct).
T4 §3(c) lasso observation checked: docs/referee/2026-10-14-T4-3c-lasso.md (OK; 3 strengthenings, 1 citation nit on §3(b)).

## Queue
- (empty) Possible follow-up if routed: diff of the ports' games and iteration counts against the real PGSolver binary
  with -dgo -dsd -dlo -dsg (needs owner Q4).

## Things only I know
- Paper is MIN-parity (lowest priority seen infinitely often decides). PGSolver/Oink are MAX-parity. Convert p -> M - p, M even >= max p.
  On cex1 the max-parity reading of the SAME priorities happens to give Odd everywhere, which coincides with the algorithm's
  (wrong) output: anyone who runs the paper's algorithm with min-parity but checks it against Oink on the unconverted file
  will see false agreement. Use the converted twin file for Oink.
- The paper's PDF (sha256 61060b71...) and e-print tarball (4dc6c4b9...) are in my scratchpad only (untrusted downloads, not committed).

## Sources opened
| source (arXiv id / DOI) | result used (theorem / section) | opened on | note |
| --- | --- | --- | --- |
| arXiv:1807.10546v2 (Czerwiński et al., universal trees inside separating automata) | the-separation-approach.tex (languages of play encodings; safety automata; (n,d)-separators, strong separators); intro.tex 161-166 (separator) | 2026-10-14 | definitions for the T4 §3(c) check; LaTeX source |
| github.com/tcsprojects/tcslib 6778419 | src/data/tcsgraph.ml 8-226, tcsset.ml 132-166/284-287/426, tcslist.ml 35-42, tcsarray.ml 48-52, tcsbasedata.ml 181-227 | 2026-10-14 | helpers used by stratimpralgs.ml |
| github.com/tcsprojects/pgsolver d3cd624 | solvers/stratimpralgs.ml 54-199, 441-669, 693-696; solvers/switch_globally_best.ml 1-119; paritygame/transformations.ml 271-320, 338-413; paritygame/univsolve.ml 23-66, 267-780; apps/pgsolver/pgsolver.ml 102-116 | 2026-10-14 | strategy improvement originals of pgsolver_si.py |
| github.com/tcsprojects/pgsolver d3cd624 | recursiveladder.ml 13-46; policyiter/generators/switchallexp.ml 30-66, switchbestexp.ml 34-74; policyiter/stratimprgenerators.ml 7-47; paritygame.ml 19, 25-40, 128-139, 175, 201-206, 365-387 | 2026-10-14 | OCaml originals of L-COMP's ports; cloned into scratchpad |
| arXiv:2511.03752v1 | whole paper: Sec. 2 defs, Sec. 3 (A*, A', A^k, Thm 1, Lemma 2, Alg. 1, Lemma 3, Thm 4, 5, 6) | 2026-10-14 | PDF + LaTeX source (main.tex); 4 pages; only v1 exists |

## Dead ends
(none)
