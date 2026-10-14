# REFEREE-2 notebook (independent second referee)
Rule: do not read docs/referee/ or notes/REFEREE.md before my own report on a claim is pushed.

## Resume point
2026-10-14 23:52Z. R2-L4 report docs/referee-2/R2-L4.md written (verdict OK with minor CHANGES F1-F3; CDFJLP Thm 5.1
hypotheses checked; PW quote verified). Pushed; Lead messaged. May now read docs/referee/ (Lead 23:40Z) once this is pushed.
Earlier: R2-TA1 report pushed (3ea0c97) and landed by the Lead (trunk 58b5c72). Lead's reply 23:40Z (quoted):
"P2 grading: CAUGHT. The F5 sentence was the planted error ... F4 was not a plant ... it is a real finding. Proposition 3 is
not part of the signed claim ... L-ATTR is revising for F1, F3, F4, F7 and possibly F2; I'll route the revision to you for a
re-check. You may now read docs/referee/ if useful. Next queued for you, after the T-A1 re-check: the second-referee check of
L4 (claude/l-struct 50dc28b, docs/struct/L4-proof.md). Do your own report before reading the first referee's
(docs/referee/2026-10-14-L4-proof-check.md). Idle until routed." Idle now.

## Queue
1. T-A1 revision re-check when routed: G8/F3 text, gap rows for F1/F4, corrected n = 2 row, F2 if taken up.
2. L4: compare with the first referee's report (docs/referee/2026-10-14-L4-proof-check.md) after my push; note disagreements.

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
| arXiv 1807.10546 v2 (CDFJLP, e-print tex) | §3.1 languages, §3.2 safety automata, §3.3 (strong) separators; §5 Thm 5.1 (binomial only), Lemma 5.1 (injection into non-rejecting states), Lemma 5.2 proof (resistance), Lemma 5.3 structure (G_t with parallel self-loops, α_t); §4 universal-tree lower bound theorem (binomial unconditional; 2h ≤ ℓ only for the closed form) | 2026-10-14 | the "because d ≤ n" remark concerns only the n^{lg(d/lg n)-2} form |
| arXiv 2305.00308 v1 (Parys-Wiącek, e-print tex) | p.2 vertex-splitting remark (lines 85-87), §4 "necessity proof does not apply" (lines 367-368) | 2026-10-14 | quotes in L4-proof.md verified verbatim |
| TARGET.md v1.0 | section 1 vocabulary (max-parity, successor condition, priorities 0..n) | 2026-10-14 | T-A1 uses nothing about the priority range |

## Dead ends
- R2-L4: my first brute-force test of L4.1(a) on finite prefixes "failed" on 90 graphs; cause was my test (sinks make finite prefixes of dead-end paths), not the lemma, which is about infinite paths; fixed by pruning sinks (0 failures).
- None otherwise (no counterexample to T-A1 / T-A1' in 490,944 games; the search code is kept for the next revision).
