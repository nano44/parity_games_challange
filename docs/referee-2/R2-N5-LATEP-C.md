# R2-N5-LATEP-C: §C cross-map of the two referee reports on P-N5-LATEP (REFEREE-2 successor 22, Opus 5.5, D15)
Reports mapped: mine, docs/referee-2/R2-N5-LATEP.md (claude/referee-2 e7b538a9, pushed before any docs/referee/ file was opened), and REFEREE
successor 19's docs/referee/R-N5-LATEP.md (claude/referee 5bdd5d6d, opened after the Lead's word at 06:49Z). Object: docs/si/P-N5-LATEP-box53.md
@ l-si b63f2554 (sha1 b15223e5…), line docs/si/P-N5-LATEP-line.txt (sha1 4a68934d…), the same object in both reports.

## C.1 Verdicts side by side
| item | REFEREE 19 | REFEREE-2 22 | joint |
| --- | --- | --- | --- |
| §2 LATE′ diff vs R88 §4 | CHECKED, exact | CHECKED, exact | agree |
| §3 FW-R*′ | SIGNED | SIGNED | agree (same argument: τ := first adoption after t, p ≠ t, p ∉ (t, τ)) |
| §4 LATE-SPLIT′ (i), (ii) | SIGNED | SIGNED | agree (both note the leave is unique in (p, u): their §4, my N-2) |
| §4 CIRCLE′ | SIGNED (+ N2 on X′) | SIGNED | agree on the verdict; N2 discussed in C.3 |
| §5 GAP-CLIMB | SIGNED | SIGNED | agree |
| §6 CHAIN | SIGNED | SIGNED | agree |
| §7 TXC-DESCENT (termination) | SIGNED | SIGNED | agree (same termination argument: the lasso's cycle node c is reached on the simple prefix; a non-T1 c cannot climb) |
| §7 TXC-RED, LCT sum | SIGNED | SIGNED | agree |
| §7 closing sentence (l. 145) | SIGNED | SIGNED | agree |
| §8 READING | not signed; N4 | not signed; N-6 | both not signed; notes differ (C.3) |
| line 4a68934d | MATCHES after L1 (REQUIRED) | MATCHES after L-1 (REQUIRED) | MATCHES after BOTH required fixes (C.2) |

## C.2 Joint gap map
- Proof gaps: NONE in either report. Joint gap map for §2-§7: EMPTY.
- Required line fixes (the union; each referee found one the other did not rate as required):
  - J-1 = my L-1, not in REFEREE's report (REFEREE MISSED it). The line's «(any t of F if none)» drops the bound t < u when the edge has no
    previous adoption in F; packet §2 keeps t ∈ [max(a, p + 1), τ). Fix: «(a ≤ t < u if there is none)». REFEREE's §9 lists «LATE′ (t, p)» as
    bound in the line; it is bound, but to the wrong set.
  - J-2 = REFEREE's LATEP-L1 = my L-2. Both found that GXC_F is defined only by citing docs/new/N5-SC-box70.md without a commit. REFEREE rates it
    REQUIRED because box 70 is NOT landed (RESULTS R91 excludes boxes 70-71); I rated it precision and did not check whether box 70 had landed
    (I MISSED that). I accept REQUIRED: the every-symbol rule needs a landed or inline binder. Fix as REFEREE gives it: inline the definition.
- Precision fixes (agreed, either may apply): J-3 = REFEREE L3 + N3 = my L-3 (label the three inequalities «(Lemma LATE-SPLIT′, Corollary
  CIRCLE′)»; REFEREE also asks to name the landed premises R15, R17 (a), R47 (a), R88, R89, R90 in the line, as K15 / H18 do; I agree);
  J-4 = REFEREE L2 + N2 = my L-4 («some blocked state t»; see C.3 on whether the choice matters).

## C.3 Notes mapping
| REFEREE 19 | REFEREE-2 22 | joint reading |
| --- | --- | --- |
| LATEP-N1 (standing premise R57; OPT-OFF (i) chain inherited from R90 K2) | — | accepted; no counterpart in mine |
| LATEP-N2 (X′_F depends on the choice of the blocked state t) | N-9 (λ_W is constant on F, so «off-cycle at some state of [k + 1, t]» is «λ_W(y) = y» for every t) | DISAGREE in substance, agree on the fix. On a W-run λ_W is constant (R89), and P-N5-CUT §2's off-cycle is «v is not the cycle node of its W^τ-value», so it does not depend on the state, hence not on t: X′_F is choice-free. REFEREE's fix (fix one t) is harmless; mine (say «λ_W(y) = y») removes t from X′ altogether. Either closes J-4. |
| LATEP-N3 (lemma name in the line) | L-3 | same (J-3) |
| LATEP-N4 (§8: «REP′* ≤ REP* ≤ T» should be «≤ n·T») | — | REFEREE right; I MISSED it. REP* counts adoptions, up to n_E per transition, so REP* ≤ n_E·T, not ≤ T. The converse (K1) still holds. READING only. |
| LATEP-N5 (T4 used by the proof, never exhibited: MUT 4 never bites) | §5 controls (X_noT4 0 / 5) and N-8 | same finding on two engines |
| LATEP-D1 (txcd.py keeps W(σ, τ_OLD) after a τ-change; so_th TXC 73 not 63; 10 missing events at s = 1) | N-7 (same line, l. 58; so_th 73 / 16, tiedmut 77 / 10, corpus 14,739; a patched copy reproduces mine) | same defect, same true count on so_th (73) on two engines; the «box 52» pins must be re-derived |
| LATEP-D2 (§10 «0 T4» a tool artifact; 36 T4 terminals, CNW 110) | N-8 (5 T4-only terminals, CNW 71; instance b5_o11 [5, 6]) | same finding; the counts differ by data set, not by definition: REFEREE ran 672 games with given start AND S3 (767 runs, n ≤ 120), I ran 719 games from S3 only (TXC 23,975 vs 14,739 shows the different run sets). Both > 0, so «0 T4» is false. |
| — (TXC-RED's n² is weaker than needed: REFEREE §7 remark) | — | agreed (both sign; n·LCT_F suffices) |
| — | N-1 (FW-R*′ «verbatim» except the choice of τ) | REFEREE's §2-3 makes the same observation; accepted |
| — | N-3 (GAP-CLIMB refines R89 R*-RISE) | context only |
| — | N-4 (§6 l. 111 «§8 DATA» → §10) | REFEREE has no counterpart; editorial |
| — | N-5 (termination spelled out) | REFEREE's §7 gives the same argument |
| — | N-6 (§8: box-40 LATE re-entries are LATE′ only if j − 2 lies in the W-run of j − 1) | REFEREE has no counterpart; READING only, not signed |
| — | REP′ data: frozen REP′ corpus 4 (max 3) vs the tool's REPP 40 (max 9) | REFEREE: «REPEAT′s are rare: 2» on its run set; consistent (both small, both ≪ the tool's REPP) |

## C.4 What I missed, and what REFEREE missed
- I MISSED: that box 70 is not landed (J-2 is REQUIRED, not precision); §8's «≤ T» slip (LATEP-N4); naming the landed premises in the line
  (part of J-3).
- REFEREE MISSED: J-1 (the line's LATE′ parenthetical drops t < u). REFEREE's LATEP-N2 claims a choice-dependence that λ_W-constancy on F
  rules out (C.3).

## DONE / FINDINGS / NEEDS
- DONE: this §C.
- FINDINGS: (1) joint proof-gap map EMPTY: every item of §2-§7 SIGNED by both referees; (2) the line needs TWO required fixes: J-1 (mine,
  the LATE′ window) and J-2 (REFEREE's, inline GXC); (3) J-3, J-4 precision; (4) DATA: both referees independently found the txcd.py frame bug
  (so_th TXC 73) and that T4 terminals exist; (5) X′_F is choice-free on a W-run (disagreement with REFEREE's N2, same fix).
- NEEDS: Lead: route J-1 and J-2 (both REQUIRED) plus J-3, J-4, N-4, LATEP-N4 and the «box 52» re-pin to L-SI; send the fixes SHA for the
  word-diff and the new line's strict symbol test.
