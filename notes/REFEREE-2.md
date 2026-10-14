# REFEREE-2 notebook (independent second referee)
Rule: do not read docs/referee/ or notes/REFEREE.md before my own report on a claim is pushed.

## Resume point
2026-10-14 23:40Z. Task R2-TA1 done: report docs/referee-2/R2-TA1.md (verdict CHANGES F1-F7; T-A1 and T-A1' OK; routed
"psolQ iff PA**" BROKEN; routed corollary direction circular). Code and outputs in docs/referee-2/R2-TA1/. Next: wait for the
Lead (grading of P2, lane's answers to F1-F7).

## Queue
- On the lane's revision: re-check G8/F3 text, the new gap rows G9-G10, the corrected n = 2 row.

## Things only I know
- The Lead's LEAD-STATE.md records a plant P2 (sha256 2847e370…) targeting REFEREE-2; description held until verdict. My
  candidates: the routed "psolQ iff" sentence and the reversed corollary direction (report section 5).
- My implementations (docs/referee-2/R2-TA1/r2lib.py) are naive fixpoint loops; validate.py reproduces HKP's worked Examples
  1-5 and Figs. 1, 4(a), 4(b), 6 from the tikz source (circle = Even, square = Odd; min-parity colours c, pr = M - c, M even).
- Timing: exhaustive n = 3 (175,616 games) takes 30 s; 100,000 random n = 4 about 3 min; the lane's peeling.pa2 is ~10x slower.
- The 2-vertex psolB failure `0 0 1 0,1; 1 2 0 0;` contradicts the n = 2 row of A1-results.md; the lane's own code agrees with me.

## Sources opened
| source (arXiv id / DOI) | result used (theorem / section) | opened on | note |
| --- | --- | --- | --- |
| arXiv 1405.0386 v2 (HKP, e-print archiv.tex, 2014-05-20) | Defs 1-8, Thm 1-8, Lemmas 1-5, Figs 1-6, Examples 1-5 (tex lines in the report) | 2026-10-14 | min-parity (tex:366-367); Fig. 3 = psolB, Fig. 5 = psolQ; Thm 6 proof is a sketch |
| TARGET.md v1.0 | section 1 vocabulary (max-parity, successor condition, priorities 0..n) | 2026-10-14 | T-A1 uses nothing about the priority range |

## Dead ends
- None yet (no counterexample to T-A1 / T-A1' in 490,944 games; the search code is kept for the next revision).
