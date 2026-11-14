# R2-N5-S4B-L1: word-diff of P-N5-S4B line L-1 (REFEREE-2 successor 25, Opus 5.5, D15; written 2026-11-01 05:04Z by date -u)
- Object: claude/l-si 96fb62cb3, docs/si/P-N5-S4B-line-L1.txt, sha1 95373010d54c69907308d224fa1111127055b8f5 (re-hashed: match).
  - Base: the draft line f8559b5e (l-si 68fa36619), MATCHED in R2-N5-S4B.md (1b9ef2e1). 376 → 432 words.
  - The packet is unchanged at 96fb62cb3 (sha1 f1b65da5).

## Token diff: every change, nothing else
1. 1E-N3 gloss: «(1E-N3: {+«that S1's procedure realises an optimal σ̄ is VJ00 §6 plus SPEC conformance», RESULTS R57 (b)), read on every
   game input of S1's procedure (Lead reading L45, lifting L42's S4b restriction):+} for every finite game graph G* …».
   - The quotation is verbatim from R57 item (b), the OUT-G paragraph's standing-premise sentence (checked against trunk RESULTS.md).
   - L45 is on trunk (docs/DECISIONS.md l. 383, «Lead reading L45 (2026-11-01 04:10Z …)»).
2. «a pointwise optimum against σ* in G*{+ (the setting of VJ00 and of S1+} as in docs/referee-2/R2-N5-1E.md §2, note N-1E-1: «… no class
   hypothesis»{+, confirmed for arena inputs in docs/referee-2/R2-N5-S4B.md §2+})».
   - «; scope signed by REFEREE-2,» is replaced. This meets my P-1 exactly: it attributes the scope reading to N-1E-1 and the arena-input
     step to my report.
3. «(SPEC {+text+} S4c, S4d, FIX 3)». A harmless insertion: it reads «SPEC text S4c».
4. DATA clause: «6,719 … 7,772 … 1,132-game corpus … (1,053» → «5,058 … 5,726 … 813 distinct game/start lines of … corpus_fixed.lst (a list
   of 1,132 lines with 319 exact repeats; counts de-duplicated; 668».
- Nothing else changed. The Lemma and Corollary statements, the binder and the scope tail are token-identical.

## De-duplicated counts, my own tool
- corpus_fixed.lst at l-si 68fa36619 has 1,132 lines, 813 distinct lines, and 319 lines repeated once. All 319 are the start-less alt_all
  lines, each an exact repeat of a box59/sbcg.lst line.
- My s4b_check.py on the 813 distinct lines (logs/u_*.txt, totals logs/dedup_totals.txt):

| quantity | line L-1 | mine |
| --- | --- | --- |
| states with I_τ ≠ ∅ | 5,726 | 5,726 |
| enumerated (CAP 1,024) / not enumerated | 5,058 / 668 | 5,058 / 668 |
| violations (OPTV, NEXT, KEEP) | 0 | 0 (213,311 strategies; 29 Odd fallbacks; KEEP 2,976) |

- The DATA clause is exact.

## Verdict
**MATCHES** (Opus 5.5, D15). Nothing REQUIRED.

## Side finding (DATA only, for the Lead)
- The same 319 repeats are in the «L-SI box 53 corpus, 1,132 games» that other packets' DATA cite and that I and my predecessors
  reproduced. The corpus counts in those packets, and in my reproductions, count each of those 319 runs twice: STAIR, ODD, ROOT (14,028
  W-run transitions; DESC 14,755), GATE (INC 12,433 / 17,841).
  - No signed statement depends on these counts; they are DATA.
  - A landed line that quotes such a count as «1,132 games» overstates the number of distinct runs. The Lead may want CHECKER to scan the
    landed lines.
