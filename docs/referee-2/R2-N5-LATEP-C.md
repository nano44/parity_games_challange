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

## C.5 The fixes (l-si 17a3ecec, docs/si/P-N5-LATEP-fixes.md sha1 a690dc25…; new line docs/si/P-N5-LATEP-line-F1.txt sha1 a85759a2…)
Both re-hashed here from `git show 17a3ecec:<path> | sha1sum`: match. Pins re-run in a detached worktree at 17a3ecec (my extraction of
si/check.sh «box 51»-«box 53», set -euo pipefail): three PASS lines, exit 0, including the re-derived «box 52» strings and the new b5_o11 pin.

### C.5.1 Word-diff of the new line against the frozen line 4a68934d (my own: difflib over whitespace tokens, 486 → 529 tokens)
| # | frozen | new | fix | verdict |
| --- | --- | --- | --- | --- |
| 1 | «In every W-run F of N5» | «In every W-run F = [a, b] of N5» | F3 (binds a, b) | precision; needed by #3 |
| 2 | «premise of RESULTS R57 (W-run, …» | «premise of RESULTS R57, with RESULTS R15, R17 (a), R47 (a), R88 (Lemmas W-MON, XW, GP*, Corollary FW-R*), R89 (Lemmas GP*-RUN, LATE-RISE) and R90 (Lemmas OPT-OFF (ii), W-SUCC) (W-run, …» | F3 | precision; the list equals the premises §3-§7 use (I checked each proof: SPEC [S2] / [S4a] are SPEC; SUCC-MON is used by none, so its omission is right) |
| 3 | «(any t of F if none)» | «(a ≤ t < u if there is none)» | F1 = J-1 | the REQUIRED fix, as I asked; now equal to packet §2's window [max(a, p + 1), u) |
| 4 | «and t a blocked state as in the definition of LATE′» | «and t the earliest blocked state as in the definition of LATE′» | F4 = J-4 | precision; on F it changes nothing (λ_W constant, C.3), and it removes the existential ambiguity |
| 5 | «GXC_F the GXC events (v, s) of L-NEW box 70 §3 (docs/new/N5-SC-box70.md) with s, s + 1 in F,» | «GXC_F the pairs (v, s) with v Even, σ_{s+1}(v) ≠ σ_s(v), λ_Ξ unchanged at s → s + 1, v ∈ Z_s, Ξ_{s+1}(v) ▷ Ξ_s(v) and W_{s+1}(v) ⊴ W_s(v),» | F2 = J-2 | the REQUIRED fix; equal to box 70 @ 170e5316 l. 48-49 (packet §6's quote) minus «τ_{t+1} = τ_t», automatic on F; s ranges over «the transitions s → s + 1 of F (s, s + 1 in F)» (the clause it sits in), so «s, s + 1 in F» is kept in substance |
| 6 | «(Lemma LATE-SPLIT′) R*′_T ≤» | «(Lemma LATE-SPLIT′, Corollary CIRCLE′) R*′_T ≤» | F3 = J-3 | precision (label) |
- Nothing else changes: every displayed inequality, the date and the scope tail are token-identical. The diff equals F0's list of five
  changes (F0 counts #1 and #2 as one).

### C.5.2 My strict symbol test of the new line (every symbol and index)
- F, a, b: «W-run F = [a, b]». τ, W_t, λ_W, S4c: R89 / SPEC. Ξ_t, σ̄_t, Iσ_t, ⊴, ▷: SPEC S1-S2. λ_Ξ: in the line. BLOCKED: R88. n, n_E, m_E,
  d_E(z): in the line. σ_u (Even strategy of state u): SPEC's run states, as before (unchanged; acceptable). y, z, u: «adoption of (y, z) at
  u». LATE′'s t, p: «p + 1 ≤ t < u, p its previous adoption in F (a ≤ t < u if there is none)»: bound, with t < u in both branches (J-1 closed).
  REPEAT′, R*′_T, REP′_F: in the line. X′_F's k, t: «k the last k < u …», «t the earliest blocked state …»: bound (J-4 closed). off-cycle:
  P-N5-CUT §2 = R90's object. WCH_F, WCH_F(z), W(z): in the line. Z_s, D_s, o: in the line. s: «the transitions s → s + 1 of F». ZXC_F(z),
  TXC_F(z), WZ_F(z): in the line. GXC_F, v: inlined (J-2 closed; no unlanded source remains). GATE_F, CNW_F, x, LCT_F, the sets, «a set
  stands for its number»: in the line. Premise names: named landed RESULTS entries (J-3 closed).
- Result: no free symbol, no unlanded binder. The new line MATCHES the packet's §3-§7 (the statements are unchanged from the frozen line,
  which I diffed against §3-§7 in my report §4).

### C.5.3 Are F0-F15 clarifications or corrections only, with no widening?
- YES. Item by item:
  - F1, F2 (LINE-REQ): corrections of the line to the packet's own text. F1 NARROWS the literal frozen line back to §2; F2 is equivalent on F.
  - F3, F4 (LINE-PREC): bindings and labels; F4 fixes a choice that does not affect X′ on F.
  - F5, F6 (DATA): tool fixes; no signed statement mentions their counts.
  - F7, F14 (NOTE-READ): corrections inside the §8 READING, which is not signed. F14 adds a new claim, «Box 41 §4 already charges the
    other case to the λ_W-change (≤ Λ)». I did not check that claim. It is READING only and not to land.
  - F8-F13, F15 (NOTE-ACC): accepted notes; no statement text changes.
- No statement of §3-§7 is widened. No new hypothesis is dropped. The new line claims nothing the frozen line did not.

### C.5.4 F5 / F6 data against my N-7 / N-8
- F5 code (txcd.py l. 61 @ 17a3ecec): «if nt != t: w1, wk1 = W(ns, nt)» before the state update. This is exactly the defect I named (old
  l. 58) and the same repair as my scratch copy.
- The lane's new corpus file odd/out/txcd_corpus_f1.txt, summed by me: TXC 14,739; T1 292; T2 (GXC) 306; T2L 0; T3 14,136; T4 5; GXC events
  191; gate terminals 2,416; CNW 71; MULT 83; DESC_V / CYC_V / TERM_V 0. These equal my engine's corpus figures in every field (report §5,
  N-7, N-8).
- F6: the 5 T4 terminals all lie in tcR4_N6 (one CNW event there serves 5 descents). That is consistent with my counts (CNW 71 counts events,
  T4 counts descents). The b5_o11 pin (CNW 1, terminal T3) is the instance from my N-8.
- REFEREE's 36 / 110 come from a different run set (given start and S3, n ≤ 120); F6 says so.
- N-7 and N-8: CLOSED.

## DONE / FINDINGS / NEEDS
- DONE: this §C.
- FINDINGS: (1) joint proof-gap map EMPTY: every item of §2-§7 SIGNED by both referees; (2) the line needs TWO required fixes: J-1 (mine,
  the LATE′ window) and J-2 (REFEREE's, inline GXC); (3) J-3, J-4 precision; (4) DATA: both referees independently found the txcd.py frame bug
  (so_th TXC 73) and that T4 terminals exist; (5) X′_F is choice-free on a W-run (disagreement with REFEREE's N2, same fix).
  (6) C.5: the fixes at l-si 17a3ecec close J-1-J-4. The new line (a85759a2) is the frozen line plus exactly the six token changes in
  C.5.1. It has no free symbol and MATCHES §3-§7. F0-F15 are corrections and clarifications only, with no widening. F5 / F6 data equal mine
  exactly (N-7, N-8 CLOSED). Pins at 17a3ecec PASS, exit 0.
- NEEDS: Lead: none from REFEREE-2 for landing P-N5-LATEP on the new line a85759a2 (the CHECKER's exact-commit run is next). F14's new box-41
  claim is READING and unchecked: do not land it.
