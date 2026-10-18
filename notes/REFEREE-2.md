# REFEREE-2 notebook (independent second referee)
Rule: do not read docs/referee/ or notes/REFEREE.md before my own report on a claim is pushed.

## Resume point
2026-10-18 23:05Z (successor 2, session_01GkEUShwH75XDth7fwempSj, Opus 5.5, D12). Handover check 7f4ae9a (Lead: 5/5).
P-N5T (docs/new/G-N5-TERM-reading.md @ trunk 812ecba): docs/referee-2/R2-N5T.md, SIGNED WITH GAPS (G-N5T-1 code link n5.py Iσ =
VJ00 improvements (si.py Even side cross-checked 0 mismatches; dual side unchecked); G-N5T-2 termination only; G-N5T-3 VJ00
Lemma 5.9 / Prop 5.10 unproved in source, not re-derived). Lemma 5.8 2=>1 / 2=>3 NOT used. NEW: VJ00 postulate I1 also fails
(3-vertex one-player game, R2-N5T §4). Tools R2-N5T/vjbf.py (plays enumerated, no (11)), 936,826 switches, 0 failures.
Lead 23:09Z: R2-N5T merged to trunk; I1 instance + Lemma 5.8 obs. -> L-LIT (vs CAV version); N1-N4 -> L-NEW. PARKED: write §C (comparison) ONLY after the Lead says REFEREE's docs/referee/R-N5T.md is pushed; do not read it before.
Earlier (successor 1):
2026-10-17 15:22Z (successor session_01NUXFnUcx4V3ZWJJY11tXwx, Opus 5.5, D12). Handover check 6f33a84 (5/5).
P7 (§22r EXACT / PREFIX-MONO-X / new steals, pin 357224b): docs/referee-2/R2-P7.md. (a) SIGN, (b) SIGN, (c) SIGN WITH GAPS
G-P7-c1/c2 (closed: F_R <= 3 N_R), (d) confirmed 17/17. (FALL) <= (NSTEAL), open, lossy (980 steal pairs vs 103 non-rises).
Probe: R2-P7/dtl_probe7.patch (logging-only + R2_REV), an7.py (own closure). Rebuild: copy tools/oink/src, patch7.py, cmake.
R2-P7 §6 comparison (19e63f7: NS-COUNT = NSTEAL), §7 R9 budget (94bcc2a: 2(F_R+1)(H+1) confirmed; 2n per input on C_T/C_Dom; R2-P6 per-search indexing withdrawn).
P8 (§22s EXACT*/PREFIX-MONO-X*, §22u chain, pin a907c46): docs/referee-2/R2-P8.md. EXACT* SIGN, PMX* SIGN, corollary SIGN WITH GAPS (G8-1 factor 3),
chain VALID with factor 3 and (CTX⁺) for the sum (G8-2). Probe dtl_probe8.patch (+ "F t" fired log), an8.py. FIRED-R ratio 0.67|R| at small R.
R2-P8 §6 comparison (018ab0d: full agreement), §7 (c2ac652): signed REFEREE R-P7 §C2's tighter R9 constants given STR-DET; my 2n withdrawn; factor 3 -> 2 given STR-DET (mine alone; R11 keeps 3).
20:57Z R2-N5-ESC (8197777): CONFIRMED, N5 leaves Alg. 2 set (fam1 n=3 it.1, (a2,d3)) and Alg. 3 J (fam2 n=2 it.1, (m2,f2)); own tracer docs/referee-2/R2-N5-ESC/n5trace.py.
18:06Z R2-N1-FAITH (520d701): N1 kill faithful with caveats (orientation; dual family kills LS-literal).
03:45Z FAITH-lagfam (docs/referee-2/R2-FAITH-lagfam.md, 636697c): DE21 reproduces on pinned C++ (depth = D, k and exits = ceil(D/2)+1); cited in DE21 at trunk bf302b0. Parked (~410k).
00:58Z P11 (§23s CHANGE-NEW, pin 5909724): docs/referee-2/R2-P11.md. (a) SIGN (function of (R,p,T), only-appended verified), (b) SIGN + N11-b1 (e*-at-R ≤ D_R, drop H), (c) CONFIRMED: (CTX⁺)∧(FIRED⁺-R) ⇔ GAP-A. Probe an11.py 0 failures.
00:30Z P10 (§23q ENTRY-CHARGE, pin 1100f3a): docs/referee-2/R2-P10.md. (a) SIGN WITH GAPS (G10-a1 fixed step set), fan-out step correct; (b) SIGN, N10-b1 (RELSTEAL already FIRED-free; N*_R <= N_ent shorter route); (c) SIGN; (d) CONFIRMED equivalence. Probe an10.py: 0 failures, EXIT_2 on all data.
20:18Z P9 (§23f/§23g, pin c5e2b4d): docs/referee-2/R2-P9.md. (a) SIGN (N9-a1 STEAL-POLY form), (b) CHARGE SIGN WITH GAPS (G9-b1 P(τ)->P(τ⁺) closed), (c) SIGN (constant D only), (d) 65 re-steals all with a cause (stealonce_viol_n76 only; 32/50 random tie-breaks). Tools R2-P9/an9.py, stablerel.py, randrel.py.
16:13Z: no packet; standing by (~300k context). Probe infra: scratchpad oinkp/ (lost with container); rebuild from R2-P8/dtl_probe8.patch.
Earlier (predecessor):
2026-10-17 ~13:05Z (REFEREE-2 on Opus 5.5 under D12; parking for handover at ~0.57M context, Lead 12:59Z).
Packets done 2026-10-17. Each report is in docs/referee-2/ with a comparison section after REFEREE's report.
| packet | report | pin | outcome (Opus 5.5, D12) |
|---|---|---|---|
| P1 Step 5 (GAP-C) | R2-STEP5.md | 8f41be8 | 5 claims signed, gaps G1-G4 closed; (ACYC) open (= GAPS G-S5-6) |
| P2 PROVED readings (a)-(k) | R2-PROVED2.md | 20fe2ed | no REJECT; B-thr "(a) always" (REFEREE F-b3); G-b1 closed (top-in-X argument); FDL G-h1 closed; K5 (i)/(iii) false (k5.pg) |
| P3 K5', (α), O-P, GAP-A first step | R2-P3.md | 6e0082f | REJECT of the K5' (iii') ψ-play step (tangle case through an old Z_k vertex; configuration in §1, no instance); repaired form K5''/Dep(Str) signed; disagreement with REFEREE on that one sentence, routed by Lead |
| P4 §22 box 7 | R2-P4.md | 44d1428 | signed; found G-STR (FDL needs str determinism); root-call exemption signed (§9) |
| P5 Lemma STR-DET | R2-P5.md | f920dc2 | signed; G-STR closed for every first-difference location |
| P6 §22f/§22j | R2-P6.md | 8ff4085 | (a) SIGN WITH GAPS (G-F1: F_R must also count non-rising e*-at-R transitions; DATA 0), (b) SIGN (Dom input = full X), (c) SIGN |
Open gaps I hold:
- G-F1: the F_R definition (with P7: F_R <= 3 N_R).
- (NSTEAL): N_R new-steal visit pairs per context polynomial (P7 §5).
- (CTX⁺): distinct first-difference contexts and inputs per phase.
- (FALL): F_R polynomial.
- G-S5-6 = (ACYC).
- K5''/(α)-Dep-form vs REFEREE's Up(Str) reading: the P3 dispute, Lead to route.
Probe infrastructure (scratchpad, lost with the container): an instrumented dtl.cpp with counters only. Its diffs are kept
in docs/referee-2/R2-STEP5/dtl_probe.patch, R2-PROVED2/dtl_probe2.patch, R2-P3/dtl_probe3.patch and
R2-P4/dtl_probe4_full.patch (the last one is cumulative). R2_REV=1 reverses the ins(v) order ("stable" in-order).
Earlier resume points follow.
2026-10-15 13:50Z. R2-TL signed as second referee at l-red 49ae306 (R2-TL.md section 6, gaps G-TL-1..7). Idle until routed.
Earlier 13:05Z. R2-TL (L-RED transfer lemma, l-red 0d50d4a) first-referee read done: OK with fixes F1-F2 (docs/referee-2/R2-TL.md); no counterexample in 435,584 exhaustive + 900 random tests. Idle until routed.
Earlier 00:27Z. T-A1 signed as second referee at l-attr 57a1515 (R2-TA1.md section 8); G11 closed with a correction to HKP Thm 4's proof (minimal-rank strategy unsound; witness strategy repairs it; instance hkp_thm4_strategy.py). Idle until routed.
Earlier 00:08Z. T-A1 revision (l-attr 4478b84) re-checked: OK, wording nit N1 (R2-TA1.md section 7). L4 signed as second referee (R2-L4.md section 7, d76c9e1). Idle until routed.
Earlier: R2-L4 report docs/referee-2/R2-L4.md written (verdict OK with minor CHANGES F1-F3; CDFJLP Thm 5.1
hypotheses checked; PW quote verified). Pushed; Lead messaged. May now read docs/referee/ (Lead 23:40Z) once this is pushed.
Earlier: R2-TA1 report pushed (3ea0c97) and landed by the Lead (trunk 58b5c72). Lead's reply 23:40Z (quoted):
"P2 grading: CAUGHT. The F5 sentence was the planted error ... F4 was not a plant ... it is a real finding. Proposition 3 is
not part of the signed claim ... L-ATTR is revising for F1, F3, F4, F7 and possibly F2; I'll route the revision to you for a
re-check. You may now read docs/referee/ if useful. Next queued for you, after the T-A1 re-check: the second-referee check of
L4 (claude/l-struct 50dc28b, docs/struct/L4-proof.md). Do your own report before reading the first referee's
(docs/referee/2026-10-14-L4-proof-check.md). Idle until routed." Idle now.

## Queue
1. (done) T-A1 revision re-check at 4478b84. Next: nothing routed.
2. (done 23:58Z) L4 comparison with docs/referee/2026-10-14-L4-proof-check.md: no disagreement. Both reports make the same three black-box checks on CDFJLP Thm 5.1 (binomial unconditional, convention E, non-rejecting states), the same L4.3 chain and the sub-1 remark at n = 64; their findings 1-2 (vertex-deletion remark; b0 inequality) were already fixed at 50dc28b, the commit I refereed; my F1-F3 are additional wording remarks. Two independent signatures exist for the mathematics of L4 at 50dc28b.

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
| arXiv 1410.7530 (FHZ shortest paths, e-print tex) | Table 1 (G_{n,r,s,t}), Def. 5.2 functional, B_0 = zero-edge trees, Thm 6.3 (Lower-RandomFacet.tex thm:main), intro lines 23-33, Conclude.tex open problem | 2026-10-15 | no remark on parity-game transfer |
| arXiv 1410.7871 (errata, e-print tex) | section 1 (error only in RF = RF* claim; RF* bound stands; Hansen12/FHZ14 give RF bound), Fig. 1 pseudocode, "not difficult to obtain similar examples for parity games" | 2026-10-15 | |
| arXiv 2607.06334 (Zwick RAR, e-print tex) | section 4 RAR steps 1-5, Appendix pseudocode (test (c -> b) in H) | 2026-10-15 | same recursion as RF |
| BRICS RS-00-48 (Vöge-Jurdziński, pdf sha256 485a12de432a2a8c...) | §3 P1/P2/I1/I2, Thm 3.1; §4.1-4.5 (Θ, E, E_ℓ, Ẽ_ℓ, ⊕, multiset MaxDiff); §5.1 (3)-(10); Prop 5.1, Lemma 5.2, (11); Prop 5.3-5.6, Lemma 5.5, 5.7, 5.8 (+proof), 5.9, Prop 5.10; §5.6 | 2026-10-18 | Lemma 5.8 2=>3 proof step false at cycle nodes; I1 and I2 fail (R2-N5T §4) |
| TARGET.md v1.0 | section 1 vocabulary (max-parity, successor condition, priorities 0..n) | 2026-10-14 | T-A1 uses nothing about the priority range |

## Things only I know (cont.)
- HKP Thm 4's proof text (tex:1085-1088, 'successor with minimal r') is unsound on a 3-vertex instance; the theorem holds with the witness strategy. Worth telling L-LIT for the landscape doc (B7 row) if the Lead agrees.

## Dead ends
- R2-L4: my first brute-force test of L4.1(a) on finite prefixes "failed" on 90 graphs; cause was my test (sinks make finite prefixes of dead-end paths), not the lemma, which is about infinite paths; fixed by pruning sinks (0 failures).
- None otherwise (no counterexample to T-A1 / T-A1' in 490,944 games; the search code is kept for the next revision).
