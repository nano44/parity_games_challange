# P-N5-TOG fixes file 2 (box 35; answers REFEREE succ. 7)
L-NEW successor 16 (Opus 5.5, D15/D18), session_01LLCK4ctQmkMq2huT44SU7d. Written 2026-10-25 10:3xZ by date -u (clock 10:33:39Z), at the
Lead's GO (10:34Z, Lead's stamp). A new file because docs/new/P-N5-TOG-fixes-box35.md (sha1 f15b58dddf232d810fab277010e29ae5187d382d)
is cited, so it is frozen. Neither the packet docs/new/P-N5-TOG-box35.md (pinned trunk d3daae1, sha1 7dfda8c88a0e9b752156f4faec726d8dccc20ccb)
nor fixes f15b58dd is edited. These lines extend those two files.
- REFEREE: docs/referee/R-N5-TOG.md (referee fff6e624). It signs L-MONO, Z-COUNT, TOGGLE, TOGGLE-COUNT and RESTARTS. It signs X-SN-PHASE
  WITH GAPS TOG-1 and TOG-2.
- REFEREE-2: docs/referee-2/R2-N5-TOG.md (referee-2 faabe716) and its Addendum A (16d27d1c).
- Labels (D18/L40): PROVED (by whom) / CONJECTURE / OPEN / DATA. Nothing here is a running-time bound for N5 or a TARGET.md claim. G-N5-TIME
  stays OPEN.

## 1. Map of REFEREE's gaps to the existing fixes rows (both already repaired in f15b58dd §1)
| REFEREE item | = REFEREE-2 item | repaired in | the two fixes lines compared |
| --- | --- | --- | --- |
| TOG-1 (§5, accounting: the crossing out of P(Q)'s last state) | G-TOG-1 | f15b58dd §1, "Corrected accounting (replaces the second bullet of §5)" | same argument (below) |
| TOG-2 (§0 table and §5, citation) | N-TOG-1 | f15b58dd §1, N-TOG-1 row | same correction; REFEREE's wording is fuller (below) |

- TOG-1, compared line by line.
  - Per-H1-run count. Both use (n − 1) + 6(d_o + 1)n² + 6(d_o + 1)n³ ≤ 13(d_o + 1)n³ − 1, from Lemma X-RUN° (P-N5-L2-fixes2 §2) and
    P-N5-FRZ §6. The slack 7(d_o + 1)n³ − 6(d_o + 1)n² − n + 1 ≥ 1 is the same.
  - Per run Q. Both write (t_Q + 1)(13(d_o + 1)n³ − 1) + t_Q + 1.
    - REFEREE closes this as ≤ 13(d_o + 1)n³(t_Q + 1). It is in fact an equality: (t + 1)(A − 1) + t + 1 = (t + 1)A.
    - f15b58dd closes it as ≤ 13(d_o + 1)n³(t_Q + 1) + t_Q. That is true but looser by t_Q.
  - Per phase. Summing REFEREE's form over ≤ f + 1 runs gives X_SN ≤ 13(d_o + 1)n³(f + 1 + T). f15b58dd gives 13(d_o + 1)n³(f + 1 + T) + T.
    - Both are within the packet's stated bound. f15b58dd §1 says so ("This is the packet's bound, unchanged").
    - REFEREE's tighter per-run form is ADOPTED as the record line. The f15b58dd line stays true; no verdict changes.
- TOG-2. Adopted text, REFEREE's: "P-N5-L2 §11" → "P-N5-L2 §7 (X-RUN′; Lemma X-RUN° in P-N5-L2-fixes2 §2)". This is f15b58dd's N-TOG-1
  correction plus the X-RUN° pointer.

## 2. G-TOG-1 / TOG-1 DATA attribution (replaces the "DATA (REFEREE-2)" sub-bullet of f15b58dd §1)
- f15b58dd §1's DATA line reads as if the boundary crossings were counted on the SPEC trace. REFEREE-2's Addendum A (16d27d1c) says that
  its counts (310 batch / 246,038 climb, and the example b6_xl2_n32 28 → 29) come from REFEREE-2's own N5, whose S4a takes another arena
  optimum. On b6_xl2_n32 the SPEC trace has 0 such crossings: L-RED 16 reports 87 iterations / 10 fallbacks, and REFEREE-2 reproduces it.
- Corrected DATA line (replaces f15b58dd's): "The gap OCCURS on the SPEC trace. Counts:
  - REFEREE-2 (xsn_exit_spec.py): 19 of 238 TOG batch files, one crossing per file. Named witness
    experiments/n5-exhaustive/instances/b4_cyc6_0.pg (sha1 748e7d51…), S4a 0 → 1.
  - L-RED 16 (experiments/red/so/rx16.py, data16/rx16_lib.txt, l-red 6ba0cf75): 26 files, ≤ 1 per file. Example so_sor5_n24 21 → 22.
  - REFEREE succ. 7 (R-N5-TOG §5): 26 library and 62 + 26 = 88 random.
  In REFEREE-2's own N5 there are also 310 batch and 246,038 climb crossings."
- How L-RED's 26 is counted (my reading of the committed log, DATA). data16/rx16_lib.txt has 303 file rows in 4 shards. 33 rows have
  exitx = 1 and none has more. These are 26 distinct basenames, because 7 instances sit in two directories (epsseg_cex_n16, epsseg_cex_n48,
  exitr_cex_n16, exitr_cex_n48, so_k2_n32, so_sor5_n24, so_th_n32). The shard TOTAL lines sum to 7 + 11 + 8 + 7 = 33.
- This lane's check (L-NEW succ. 16, DATA):
  - Both witnesses are re-run with experiments/new/n5.py (SPEC) and experiments/new/check_sol2.py, with one Odd choice vertex asserted.
    - b4_cyc6_0: n 11, 2 iterations, 0 fallbacks; Oink zlk OK, strategies verified.
    - so_sor5_n24: sha1 42f9fa79…, n 24, 23 iterations, 0 fallbacks; Oink zlk OK, strategies verified.
  - experiments/new/box35/d35trace.py:
    - b4_cyc6_0: state 0 is H1 ∧ H2 with θ = w = (3, 96, 3) and |R| = 4. State 1 is H1 ∧ ¬H2 with w = (6, 0, 0) and |R| = 8. The step is
      S4a, Even 5: 3 → 8. That is 4 vertices entering R, as in Addendum A ({2, 4, 5, 10}).
    - so_sor5_n24: state 21 is H1 ∧ H2 with θ = w = (5, 0, 2) and |R| = 21. State 22 is H1 ∧ ¬H2 with |R| = 22.

## 3. §7's DROP-LEN line is out of date (not a gap in a signed statement)
- P-N5-TOG §7 lists DROP-LEN as a CONJECTURE that "holds in every instance seen". That is out of date. DROP-LEN is FALSE:
  docs/referee/R-N5-L2/droplen_cex_n12.pg (REFEREE succ. 7, R-N5-L2 §8; this lane's record N5-DROP-box35.md §4 and P-N5-L2 fixes 7a110bca §2).
- The weak form "≤ 1 drop per fallback-free run" is also FALSE: onerun_cex_n32 (sha1 70832fcb…, N5-DROP-box35.md §3) and droplen_cex_n12.
- §7 was not to be signed, and REFEREE did not sign it (R-N5-TOG §7).

## 4. Labels after both reports (D18/L40)
- PROVED (L-NEW succ. 15), on 𝒞^1O inside a (λ_Ξ, τ)-phase:
  - L-MONO, Z-COUNT, TOGGLE, TOGGLE-COUNT and RESTARTS: signed by REFEREE-2 (faabe716) and REFEREE succ. 7 (fff6e624). (F) is
    signed by REFEREE-2; REFEREE uses it in its §0 as VJ00 (V1) plus "c is the top of its own cycle" and gives no separate row;
  - X-SN-PHASE: signed with gaps by both; G-TOG-1 = TOG-1 and N-TOG-1 = TOG-2 are closed by f15b58dd §1 with §1-§2 above.
- X-SN-PHASE and RESTARTS inherit their P-N5-L2 premises (both referees; R33 drafted, not landed).
- FALSE (DATA): DROP-LEN, "≤ 1 drop per fallback-free run", "a fallback at H1 ∧ ¬H2 never takes τ(o) out of R".
- OPEN: (L1), f ↔ X, K, G-N5-TIME. The TARGET.md diff is empty.
