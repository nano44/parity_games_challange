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

L4 proof (l-struct 168d828), first referee: docs/referee/2026-10-14-L4-proof-check.md, CHANGES (two sentence fixes;
Theorem L4, L4.3, L4.4 hold; Thm 5.1 black box legitimate; PW quotes verbatim).
S3 delta (l-struct a67bd78): OK; M0 window-length nit; R1 observation: splitting v_i per out-letter gives c = d and with
monotonicity in d this already yields L4 (s^V(n,n) >= n^{Omega(lg n)}); appended to the S3 report.
S3 statement (l-struct ef95a93): docs/referee/2026-10-14-S3-statement-check.md, CHANGES (6 findings; diagonal W=S=1,2,5,7 for n<=4 confirmed by my SAT).
T1 REFUTED at (2,10) (l-comp 3e44d2c): witness verified by me in E (exhaustive 2-vertex), S, V; s(2,8) >= 5 and w(2,10) >= 4
by my own SAT in V/S; universal tree (2,4) = 5. Added as section 0 of the S2 report.
S2 statement (l-struct 616cf77): docs/referee/2026-10-14-S2-statement-check.md, CHANGES (T2 edge case; V barrier needs an s^V bound;
algorithm class; commit the probe automaton). (4,6) V SAT cells pending.
S1/C1 (l-struct 42dbbc2): docs/referee/2026-10-14-S1-C1-weak-separators.md: C1 OK (w(2,6)=3<4=s(2,6) in E,S,V, own checker
over all graphs + own SAT + universal trees), side claim (3-state weak (3,6)-separator) BROKEN (a Lead plant, revealed in docs/agents/LEAD-STATE.md at trunk 09dca4f; graded CAUGHT 1/1), w^V(3,6)=6<7 OK, Lemma 2(b) CHANGES.
Harness review (l-comp a3777f1..de7ea19, experiments/): docs/referee/2026-10-14-harness-review.md, CHANGES (2 self-test coverage findings; code correct); signed OK at l-comp e70a2a9 after re-running both faults.
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
| arXiv:2305.00308v1 (Parys–Wiącek) | improved-parity.tex lines 86-87 (edge-to-vertex priority conversion remark), 368 (necessity proof does not apply) | 2026-10-15 | LaTeX source; L4 attribution quotes |
| arXiv:2104.05262v8 (CFGO, LMCS 2022) | preliminaries (graphs, automata, neutral letter), reductions (separating automata, universal graphs), saturation Thm 4.1, parity §6: Lemma 6.1, Thm 6.2, Lemmas 6.4-6.8, Thm 6.9, Props 6.10/6.11 | 2026-10-14 | LaTeX source; S1 conventions and F2 |
| arXiv:1902.07175v3 (Kozachinskiy-Vyalyi) | §1.2 separation approach, §2.1 separation automata and game graphs, Thm 2 | 2026-10-14 | LaTeX source; S1 F5 / Lemma 3 |
| arXiv:1807.10546v2 (Czerwiński et al., universal trees inside separating automata) | the-separation-approach.tex (languages of play encodings; safety automata; (n,d)-separators, strong separators); intro.tex 161-166 (separator) | 2026-10-14 | definitions for the T4 §3(c) check; LaTeX source |
| github.com/tcsprojects/tcslib 6778419 | src/data/tcsgraph.ml 8-226, tcsset.ml 132-166/284-287/426, tcslist.ml 35-42, tcsarray.ml 48-52, tcsbasedata.ml 181-227 | 2026-10-14 | helpers used by stratimpralgs.ml |
| github.com/tcsprojects/pgsolver d3cd624 | solvers/stratimpralgs.ml 54-199, 441-669, 693-696; solvers/switch_globally_best.ml 1-119; paritygame/transformations.ml 271-320, 338-413; paritygame/univsolve.ml 23-66, 267-780; apps/pgsolver/pgsolver.ml 102-116 | 2026-10-14 | strategy improvement originals of pgsolver_si.py |
| github.com/tcsprojects/pgsolver d3cd624 | recursiveladder.ml 13-46; policyiter/generators/switchallexp.ml 30-66, switchbestexp.ml 34-74; policyiter/stratimprgenerators.ml 7-47; paritygame.ml 19, 25-40, 128-139, 175, 201-206, 365-387 | 2026-10-14 | OCaml originals of L-COMP's ports; cloned into scratchpad |
| arXiv:2511.03752v1 | whole paper: Sec. 2 defs, Sec. 3 (A*, A', A^k, Thm 1, Lemma 2, Alg. 1, Lemma 3, Thm 4, 5, 6) | 2026-10-14 | PDF + LaTeX source (main.tex); 4 pages; only v1 exists |

## Dead ends
(none)
