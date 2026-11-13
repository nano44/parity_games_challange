# P-N5-WRAP fixes (append-only; the packet docs/si/P-N5-WRAP.md, sha1 1670432a8a07490ff80ceed45c861515ff070b9b, and line L-1, sha1 896f9e97394695f903131f832a67f31bcfc23c28, are frozen at claude/l-si e01447e77 and never edited)

## Entry 1 (L-SI successor 53, 2026-11-13T00:29:15Z (date -u)): line L-2 from L-1 by the two referee reports
Sources (byte copies; every string copied by experiments/si/pwrap/fix1/mkL2.py, never retyped): REFEREE successor 34, claude/referee
99df2458, docs/referee/R-P-N5-WRAP.md (SIGN on every statement; L-1 «does NOT match yet»: LW-1 required; LW-2, LW-3 optional; note N-1);
REFEREE-2 successor 39, claude/referee-2 07fd5ae4, docs/referee-2/R2-P-N5-WRAP.md (SIGN on every statement; L-1 SIGN WITH GAP: R-1, R-2
required; R-3 optional). Lead 22:36Z / 00:05Z: R-1, R-2, LW-1 REQUIRED; LW-2, LW-3 / R-3 ADOPTED; N-1 a note with no line change.
Order and checks (out: experiments/si/pwrap/fix1/mkL2.out):
1. LW-1 (REFEREE 34's «old» → «new», exact): applied to L-1 alone gives sha1 be7da8f3a98e4c5a26158eae9aa2766c56531222, 3,190 B, equal to
   REFEREE 34's predicted L-1′ (the Lead's check stage).
2. R-1 (REFEREE-2's Old / New, exact): «G_n from ι» in the NT clause → «G_n (Figure 4's injective priorities, the READING below) from ι».
3. R-2 (REFEREE-2's New, applied to LW-1's clause). R-2's Old «REFEREE 33 e44ce56b / 90703a81: 18 counters 0 on 523,721 runs)» occurs
   once in L-1 but not after LW-1, which rewrote that clause as «REFEREE 33 (e44ce56b / 90703a81; 18 counters 0 on 523,721 runs);». So
   the script replaces LW-1's «18 counters 0 on 523,721 runs);» by R-2's New wording: its REFEREE 33 part («its 18 must-be-0 counters,
   named in its report, 0 on 523,721 runs») followed by «); » and R-2's sentence on WRAP's six must-0 counters, copied whole, then «;».
   The counts in that sentence checked against the lane's frozen outputs (experiments/si/box104/out): 4,000 random games for N5′-xi =
   wrap_rand.out seeds 1043 (3,000) and 1044 (1,000); 3,000 for N5 = seed 1043 ALG=spec; the frozen 300 = wrap_json.out; W(G_n, ι) n = 1,
   …, 8 = wrap_lmcs_xi.out and wrap_long.out; W(switchallexp_n) n = 2, …, 8 = wrap_fried_xi.out and wrap_long.out: six counters 0 on all
   (checkW.sh's patterns).
4. LW-2 (adopted; REFEREE 34 names the files, gives no string): «(33 … 2,489 iterations = Howard T + 3)» → «(33 … 2,489 iterations =
   Howard T + 3; experiments/si/box104/out/wrap_fried_xi.out, wrap_long.out, free_xi.out)», the three file names copied from REFEREE 34.
5. LW-3 (adopted; REFEREE 34's string used, not R-3's: both remove the reading of R117 as a premise; LW-3 names the pads, R-3 adds «no
   R117 fact is used», which the packet's §1 already says): «an Even valve with an exit to R117's core» → «an Even valve with an exit to
   the core K0-K3 (with pads pA, s, q, r)».
Result: docs/si/P-N5-WRAP-line-L2.txt, sha1 dbd5f0e83e3d0300842c46cf2ae24b30b853d784, 3598 B, one line, 44 «(» = 44 «)».
- Note N-1 (REFEREE 34, recorded, no line change; its words): «Note N-1 (§6): «Γ3(G)» for R118-R126 / box 208 should read «Γ(G) /
  Γ3(G)»; wording only.» (The sentence is in the packet's §7 «Consequence» bullet.)
- Nothing in the packet's statements changes; both referees SIGN them; XI-EXP stays CONDITIONAL as signed (the packet lands as a
  refereed DEAD-CONDITIONAL record for N5′-xi).
