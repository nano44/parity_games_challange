# P-N5-LATEP fixes (append-only; the frozen packet docs/si/P-N5-LATEP-box53.md, sha1 b15223e5…, is never edited)
L-SI successor 32 (Opus 5.5; D15 / D18). Written from 2026-10-30 06:50Z (date -u).
- Sources: REFEREE 19, claude/referee 5bdd5d6d, docs/referee/R-N5-LATEP.md; REFEREE-2 22, claude/referee-2 e7b538a9,
  docs/referee-2/R2-N5-LATEP.md.
- Both referees SIGNED every PROVED item (§3-§7) with no gap. The Lead's routing (06:49Z): LINE items required before landing; DATA defects
  D1 / D2; notes N4, N5, N-1, N-4, N-6.
- The corrected line: docs/si/P-N5-LATEP-line-F1.txt (F0 below). The original line file (sha1 4a68934d…) is kept unchanged as the record.
- Classes:
  - LINE-REQ: the line must change before landing;
  - LINE-PREC: a precision in the line;
  - DATA: the tool or a data statement was wrong, no proof affected;
  - NOTE-ACC: the note is accepted as a clarification of the packet's text, with no change to any signed statement;
  - NOTE-READ: concerns the §8 READING, not signed.

## F0. The corrected line (docs/si/P-N5-LATEP-line-F1.txt, sha1 a85759a26b38b8bb6e3958bb19745d2aa9fd397c)
- Word changes against the frozen line (4a68934d), and nothing else:
  1. «In every W-run F of N5 (SPEC S1-S5) on any game, under the standing SPEC premise of RESULTS R57 (» → «In every W-run F = [a, b] of N5
     (SPEC S1-S5) on any game, under the standing SPEC premise of RESULTS R57, with RESULTS R15, R17 (a), R47 (a), R88 (Lemmas W-MON, XW,
     GP*, Corollary FW-R*), R89 (Lemmas GP*-RUN, LATE-RISE) and R90 (Lemmas OPT-OFF (ii), W-SUCC) (» (F3: names a, b and the premises).
  2. «(any t of F if none)» → «(a ≤ t < u if there is none)» (F1).
  3. «and t a blocked state as in the definition of LATE′,» → «and t the earliest blocked state as in the definition of LATE′,» (F4).
  4. «GXC_F the GXC events (v, s) of L-NEW box 70 §3 (docs/new/N5-SC-box70.md) with s, s + 1 in F,» → «GXC_F the pairs (v, s) with v Even,
     σ_{s+1}(v) ≠ σ_s(v), λ_Ξ unchanged at s → s + 1, v ∈ Z_s, Ξ_{s+1}(v) ▷ Ξ_s(v) and W_{s+1}(v) ⊴ W_s(v),» (F2). The pairs range over
     «the transitions s → s + 1 of F (s, s + 1 in F)», as the sentence already says. τ_{s+1} = τ_s holds on F, so L-NEW's τ-clause is
     automatic.
  5. «(Lemma LATE-SPLIT′) R*′_T» → «(Lemma LATE-SPLIT′, Corollary CIRCLE′) R*′_T» (F3).
- Strict symbol test of the new line: §F-SYM at the end of this file.

## F1. REFEREE-2 L-1 (LINE-REQ): «(any t of F if none)» drops t < u
- Accepted. The packet's §2 has t ∈ [max(a, p + 1), τ) with τ the adoption transition. The line now reads «(a ≤ t < u if there is
  none)», with a bound by «F = [a, b]» (F0 change 1).

## F2. REFEREE LATEP-L1 = REFEREE-2 L-2 (LINE-REQ): GXC_F cites an unlanded, unpinned file
- Accepted. The definition is inlined as REFEREE gives it (F0 change 4). The packet's §6 quote of box 70 l. 48-49 @ 170e5316 is the
  source; the inlined text drops only the τ-clause, which is automatic on F. The packet's §9 row «GXC_F … landed» was wrong: box 70 is
  not landed (RESULTS R91 excludes boxes 70-71).

## F3. REFEREE LATEP-L3 / LATEP-N3 = REFEREE-2 L-3 (LINE-PREC): name the landed premises; label CIRCLE′
- Accepted (F0 changes 1 and 5).
- The premises named are exactly those §1 of the packet lists and §3-§7 use: R15 (Ξ monotone), R17 (a) ([V1], [V2]), R47 (a) (Σ LCT ≤
  n(n − 1)), R88 (W-MON, XW, GP*, FW-R* and its proof), R89 (GP*-RUN, LATE-RISE), R90 (OPT-OFF (ii), W-SUCC).
- R89's SUCC-MON is listed in the packet's §1 but used by no proof of §3-§7: W-SUCC (R90) carries the W chain. It is therefore not named.

## F4. REFEREE LATEP-N2 / LATEP-L2 = REFEREE-2 L-4 (LINE-PREC): fix the blocked state t in X′_F
- Accepted, with the choice REFEREE proposes: the EARLIEST blocked state of [max(a, p + 1), u) (F0 change 3).
- CIRCLE′'s inequality REP′_F ≤ X′_F + Σ_z d_E(z)·WCH_F(z) holds for every fixed choice, because the chain uses only off-cycle on
  [k + 1, t] for the t used (REFEREE §4). The earliest t gives the smallest window and the smallest X′.
- By REFEREE-2 N-2 every LATE′ block t satisfies t ≥ k + 1, so [k + 1, t] is never empty. Reading the packet's §4 with this choice
  changes no signed statement.

## F5. REFEREE LATEP-D1 = REFEREE-2 N-7 (DATA): txcd.py read W with the old τ after a τ-change
- Accepted.
- The defect: experiments/si/odd/txcd.py set w0 := W(σ_{s+1}, τ_OLD) at the end of a τ-changing step, so the first transition of the
  next W-run was judged in a wrong frame.
- The fix, in a new commit: «if nt != t: w1, wk1 = W(ns, nt)» before the state update.
- Counts after the fix:
  - so_th_n32: TXC 73, gates 16 (was 63, 15);
  - tiedmut_so_th_n32_11: TXC 77, gates 10 (was 66, 9);
  - wdepth_K4_m16: unchanged, TXC 184, gates 93.
  - Corpus (odd/out/txcd_corpus_f1.txt; the old file txcd_corpus.txt is kept as the record): TXC 14,739; terminals T1 292, T2 (GXC) 306,
    T3 14,136, T4 5; GXC events 191; descent failures 0.
  - These equal REFEREE-2's counts exactly (TXC 14,739; T1 292, T2 306, T3 14,136, T4 5).
- Record of the old figures:
  - box 52 §4 / packet §10: TXC 14,526; T1 356, T2 292, T3 13,878, GXC events 227;
  - the old «box 52» pin «TXC 63 … GATE 15».
- The pin is re-derived in si/check.sh «box 52»: so_th «TXC 73 … T4 0 … GATE 16 CNW 0 MULT 13»; wdepth with the new fields.
- The READING «gates carry the descent» stands: 14,136 / 14,739 = 95.9 %.

## F6. REFEREE LATEP-D2 = REFEREE-2 N-8 (DATA): no T4 test; «0 T4» and «CNW is 0 in all data» are false
- Accepted.
- txcd.py now tests T4 (λ_W(x) = x, after T1-T3) and counts CNW (TXC events at own W-cycle nodes).
- Corpus: CNW 71; T4 terminals that are not T1-T3: 5 (all in tcR4_N6).
- REFEREE-2's instance n5-exhaustive/instances/b5_o11.pg (S3) shows CNW 1. Its own W-cycle node 7 is also a gate there, so the terminal
  is T3. It is pinned in «box 52» as «CNW 1».
- Box 52 §2 / §4's inference «a T4 vertex … would appear as a failure» was unsound: the old tool walked through T4 vertices, and the next
  vertex was a TXC event in all 5 cases. Withdrawn.
- §10's «0 T4» is corrected to «5 T4 terminals, CNW 71». REFEREE's own engine reports 36 T4 terminals and CNW 110 on its subset (n ≤ 120,
  given starts). The count depends on the T3 / T4 precedence and the run set.

## F7. REFEREE LATEP-N4 (NOTE-READ): §8 «REP′* ≤ REP* ≤ T»
- Accepted. P-N5-CUT K1 gives REP* ≤ n·T (≤ n_E adoptions per transition), not REP* ≤ T. Read «REP′* ≤ REP* ≤ n·T». The conclusion (the
  converse is unaffected) stands.

## F8. REFEREE LATEP-N5 (NOTE-ACC): T4 is used by the proof but not exhibited by REFEREE's MUT 4
- Accepted as stated. [V1] for W fails at an own W-cycle node, so T4 is needed in the proof.
- F6's tcR4_N6 has 5 descents whose first terminal is T4. Whether dropping T4 ever makes the descent fail is a separate question (REFEREE
  MUT 4: never; REFEREE-2: X_noT4 0 / 5). No instance shows T4 is necessary for the conclusion; it is necessary for the proof as written.

## F9. REFEREE-2 N-1 (NOTE-ACC): «verbatim» in §3
- Accepted. FW-R*′'s proof is R88's proof plus one added choice, τ := the first adoption after t, used twice (p ∉ (t, τ); k − τ ≤ i). Read
  «verbatim up to the choice of τ».

## F10. REFEREE-2 N-2 (NOTE-ACC): uniqueness of the leave in §4 (ii)
- Accepted. Between the previous adoption p and u there is no adoption of (y, z), so y leaves z exactly once in (p, u), at k. Hence every
  LATE′ block t ∈ [p + 1, u) has t ≥ k + 1 (also REFEREE §4).

## F11. REFEREE-2 N-3 (NOTE-ACC): GAP-CLIMB refines R89's R*-RISE
- Accepted as the packet's §5 last bullet says. Same LATE-RISE mechanism; the climb is located at a gap state; the disjointness comes from
  LATE′ itself (REFEREE MUT 5 confirms it bites without LATE′).

## F12. REFEREE-2 N-4 (NOTE-ACC): cross-reference
- Accepted. Packet §6 last bullet «(§8 DATA)» should read «(§10 DATA)».

## F13. REFEREE-2 N-5 (NOTE-ACC): termination in §7
- Accepted. «before any repetition» holds because the cycle node c lies on the play's cycle, so the simple prefix from z reaches c before
  any vertex repeats.

## F14. REFEREE-2 N-6 (NOTE-READ): §8's box-40 remark needs j − 2 in the same W-run
- Accepted. «LATE re-entries are LATE′» holds when j − 2, j − 1, j lie in one W-run, i.e. when the transition j − 2 → j − 1 keeps λ_W (and
  is not a fallback). Box 41 §4 already charges the other case to the λ_W-change (≤ Λ). Not signed; a future packet would carry that
  hypothesis.

## F15. REFEREE-2 N-9 (NOTE-ACC, wording)
- Accepted. λ_W is constant on F, so «y not off-cycle for τ at some state of [k + 1, t]» is the same as «λ_W(y) = y». The line keeps
  P-N5-CUT's wording; the two readings agree on F.

## F-SYM. Strict symbol test of the corrected line (docs/si/P-N5-LATEP-line-F1.txt)
| symbol / term | bound by (in the line, SPEC, or a named RESULTS entry) |
| --- | --- |
| F, a, b, W-run | «W-run F = [a, b]»; «W-run … as in RESULTS R89: τ and λ_W constant on F, no S4c fallback» |
| N5, SPEC S1-S5, S4c | named, landed |
| R15, R17 (a), R47 (a), R88, R89, R90 lemma names | named, landed (RESULTS) |
| W_t, λ_W, τ | «as in RESULTS R89»; τ is F's constant τ |
| Ξ_t, σ̄_t, Iσ_t, ⊴, ▷ | «as in SPEC S1-S2» |
| λ_Ξ | «the cycle-node map of Ξ_t» |
| BLOCKED | «as in RESULTS R88» |
| n, n_E, m_E, d_E(z) | in the line |
| adoption, y, z, u | «an adoption of (y, z) at u: σ_{u+1}(y) = z ≠ σ_u(y)» |
| LATE′, t, p | «blocked at some state t of F with p + 1 ≤ t < u, p its previous adoption in F (a ≤ t < u if there is none)» |
| REPEAT′, R*′_T, REP′_F | in the line |
| X′_F, k, t (second use), off-cycle | «k the last k < u with σ_k(y) = z ≠ σ_{k+1}(y) and t the earliest blocked state as in the definition of LATE′»; «off-cycle for τ (P-N5-CUT §2)» = R90's object |
| WCH_F, WCH_F(z) | in the line |
| Z_s, D_s, o | in the line |
| s, transitions of F | «the transitions s → s + 1 of F (s, s + 1 in F)» |
| ZXC_F(z), TXC_F(z), WZ_F(z) | in the line |
| GXC_F, v | inlined: «the pairs (v, s) with v Even, σ_{s+1}(v) ≠ σ_s(v), λ_Ξ unchanged at s → s + 1, v ∈ Z_s, Ξ_{s+1}(v) ▷ Ξ_s(v) and W_{s+1}(v) ⊴ W_s(v)» |
| GATE_F, CNW_F, x, LCT_F | in the line |
| TXC_F, ZXC_F (sets); a set as a number | in the line |
| Lemma / Corollary / Proposition names | the packet's §3-§7 names; CIRCLE′ now labelled (F3) |
- Result: no free symbol. Every symbol is bound in the line or by SPEC / a named landed RESULTS entry. No unlanded source remains (box 70
  is gone from the line).

## DONE / FINDINGS / NEEDS
- DONE: F0-F15 and F-SYM; new line docs/si/P-N5-LATEP-line-F1.txt; txcd.py fixed (D1, D2); odd/out/txcd_corpus_f1.txt; si/check.sh «box 52»
  re-derived.
- FINDINGS: every referee note is accepted. LINE-REQ: F1, F2. LINE-PREC: F3, F4. DATA: F5, F6. NOTE-READ: F7, F14. NOTE-ACC: F8-F13, F15.
  No signed statement changes.
- NEEDS: both referees' §C and their word-diff of the new line (F0); then the Lead's landing. Owner: none.
