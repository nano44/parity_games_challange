# P-N5-SDPRIME fixes (box 25): repairs only, after both reports on P-N5-SDPRIME-box25 (no gap; joint gap map EMPTY)
L-SI successor 21 (Opus 5.5; D18, Lead reading L40). Object: the frozen packet docs/si/P-N5-SDPRIME-box25.md, sha1
54678c38a04842bd936a9bf4b241d47ad8ab90a3 (l-si edc14c51), UNCHANGED (sha1 pinned in experiments/si/check.sh). This file changes NO signed
statement: it records the referees' notes and the lane's repairs of citations and wording, as the Lead's message of 2026-10-29 04:51Z asked
(«Please write docs/si/P-N5-SDPRIME-fixes-box25.md (repairs only, quotes pinned)»). Reports: REFEREE docs/referee/R-N5-SDPRIME.md (report
573d2695, §C d693a6fe); REFEREE-2 docs/referee-2/R2-N5-SDPRIME.md (report bf48b8f4, §C 9784229a). Every [Q path@commit:lines] «…» below is
verbatim (experiments/si/rund/quotecheck.py, pinned with a shifted-line control); every quote here is a contiguous span of the source.
Scope (D1) unchanged: structural lemmas inside one phase; no running-time bound; G-N5-TIME stays OPEN.

## Joint list (Lead 04:51Z) and repairs
| fix | note(s) | kind | repair |
| --- | --- | --- | --- |
| F1 | SDP-N2 (= REFEREE-2 §1 "Premises", N-SD-5) | citation; a SIGNED proof step | W-MONO and Ξ-SUCC are proved at every in-phase S4a transition, λ_W not used; listed among the proof facts |
| F2 | SDP-N3 = N-SD-1 | quote | the (SW) quote's "…" marks only a line break |
| F3 | SDP-N4 = N-SD-2 | wording | "GEN_W at every epoch end" is redundant: GEN_W is a property of (G, τ) |
| F4 | SDP-N1 = N-SD-7 | §4 data (not signed) | the piece notion and the starts used, and the recount |
| F5 | SDP-N5 ⊇ N-SD-3; N-SD-4 | thin spots; (H4′) not vacuous | recorded |
| F6 | N-SD-6 | proof remark | R77's (CV) step is not used; item 1 replaces it |

## F1 (SDP-N2; N-SD-5). W-MONO and Ξ-SUCC where λ_W changes: a signed proof step
- The packet §1 cites W-MONO and Ξ-SUCC as R77 (c)'s signed proof steps "on in-phase S4a transitions (R77's (H1); neither step uses
  (H2)-(H4))". R77's (H1) includes λ_W constant, and STATIC-DEPTH′'s intervals may change λ_W. REFEREE: [Q docs/referee/R-N5-SDPRIME.md@d693a6fe7:94-96]
  «SDP-N2 (premise scope). W-MONO and Ξ-SUCC are landed inside R77 (c) under (H1), which includes λ_W constancy. The packet uses them on
  (H1′) intervals where λ_W may change. Both facts hold there (§1, first bullet; one line each), so this is a citation point: say "W-MONO
  (P2 at an S4a step) and Ξ-SUCC (R15 (a), (d), (SW)) hold at every in-phase S4a transition; λ_W is not used".»
- Settled in §C as a signed step: [Q docs/referee/R-N5-SDPRIME.md@d693a6fe7:117-118] «SDP-N2 SETTLED (Lead's question): the extension of W-MONO and
  Ξ-SUCC to in-phase S4a transitions at which λ_W changes is a SIGNED PROOF STEP of this entry, not a note.»
- REPAIR (citation; the proof text is unchanged). Read the packet §1's W-MONO / Ξ-SUCC bullet as: "Facts used as proof steps (signed by both
  referees for this entry): (W-MONO) W_{t+1} ⊵ W_t at every in-phase S4a transition t → t + 1: σ_t uses only its own choices, which are arena
  edges, and σ_{t+1} is pointwise W-optimal over strategies using arena edges (P2; R18 (d) Lemma S (a)). (Ξ-SUCC) Ξ_t(σ_t v) is non-decreasing
  along in-phase S4a transitions: if v keeps, Ξ_{t+1}(σ_t v) ⊵ Ξ_t(σ_t v) by R15 (a), (d) (pointwise monotonicity of Ξ under N5's S4a
  Switch_I); if v switches, (SW) gives Ξ_t(σ_{t+1} v) ▷ Ξ_t(σ_t v) and R15 (a), (d) give Ξ_{t+1}(σ_{t+1} v) ⊵ Ξ_t(σ_{t+1} v). λ_W is not used."
  R15 (a), (d) and (SW) are LANDED; the quotes for them are in P-N5-REL-box25's premise list ([Q docs/RESULTS.md@b28123a58:631] «(a) Lemma A: for any
  non-empty unambiguous set I of improvements of σ (VJ00 §4.4), Ωσ ⊴ Ω_{Switch_I(σ)}.» and [Q docs/RESULTS.md@b28123a58:640] «(d) N5: every iteration
  applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ (on G)»).
- N-SD-5 (same point): [Q docs/referee-2/R2-N5-SDPRIME.md@9784229a2:117-118] «N-SD-5 (premise use). Ξ-SUCC needs only (SW) and pointwise
  Ξ-monotonicity (R15 (a), (d)). The (M2κ) citation inherited from R77 is fine but stronger than needed.» ACCEPTED: the (M2κ) citation is
  replaced by R15 (a), (d) as above.

## F2 (SDP-N3 = N-SD-1). The (SW) quote
- REFEREE-2: [Q docs/referee-2/R2-N5-SDPRIME.md@9784229a2:105-106] «The source reads "(SW): every Even switch of N5 is to an edge" / "of Iσ" over a line break.»
  The packet's ellipsis marks an omission that does not exist; content identical (REFEREE-2 l. 107, REFEREE SDP-N3 l. 97-98).
- REPAIR: the quote reads, strictly verbatim, [Q docs/RESULTS.md@55e0bcbda:3768-3769] «(SW): every Even switch of N5 is to an edge of Iσ». The other 11
  quotes were verbatim for both referees. (Our quotecheck.py treats "…" as a separator, so it passed; from this file on, quotes that span a line
  break are written without "…".)

## F3 (SDP-N4 = N-SD-2). GEN_W in Corollary EPOCH
- [Q docs/referee-2/R2-N5-SDPRIME.md@9784229a2:110-111] «GEN_W as defined in R77 (c) is a property of (G, τ), and τ is fixed on the phase. So "GEN_W at every
  epoch end" in EPOCH is either redundant or means the used form per epoch.»
- REPAIR (wording): EPOCH's hypothesis reads "if (H4′) holds at every epoch end, and GEN_W holds". GEN_W is the property of (G, τ) quoted in the
  packet §1. Both referees checked the used form (the plays compared in step (C)) and found the conclusion intact where it fails.

## F4 (SDP-N1 = N-SD-7). The piece counts of §4 (DATA, not signed)
- [Q docs/referee/R-N5-SDPRIME.md@d693a6fe7:90-92] «SDP-N1 (§4 coverage, not signed). On my alt_all pieces with ≥ 1 transition, STATIC-DEPTH′'s hypotheses hold on 1,098 of 1,132 (97.0 %; (H3′)
  fails 25, (H4′) 2, GEN_W(used) 7) and R77's on 918 (81.1 %). §4: 844 of 872 (96.8 %) and 708 (81.2 %). The RATIOS agree; the piece COUNTS
  differ (1,132 vs 872)»
- Cause found: §4's corpus run used the DEFAULT S3 start for every file. The list runlin/out/alt_all_root.lst has a second column (a pinned
  .start file) on 94 of its 413 lines, and piece/sdprime.py --list (like root/staticdepth.py --list) read only the first column.
- Piece notion (unchanged): a maximal stretch of ≥ 2 states (≥ 1 transition) of a fallback-free run of one phase ((λ_Ξ, τ) constant) on which
  σ̄ is constant on every Odd vertex; games without an Odd vertex of out-degree ≥ 2 included (9 alt_all games, 9 pieces).
- Recount with the pinned starts (piece/sdprime.py now takes env START=1; log piece/sdprime_alt_start.txt): 1,140 pieces (1,131 without the 9
  no-choice games), (H3′) fails 25, (H4′) 2, STATIC-DEPTH′'s hypotheses hold on 1,113 (97.6 %; GEN_W failures counted, not excluded: 9
  pieces), 0 violations. REFEREE's 1,132 and REFEREE-2's 1,133 are within 1-9 of 1,140 / 1,131; the remaining difference is not determined
  (start-file handling, cf. REFEREE's CORE-N5, or the no-choice games). The default-start counts of the packet §4 stay as stated, now labelled
  "default S3 starts".
- lib41: §4's 943 pieces are the default starts of the 412 files; REFEREE-2's 1,812 × 3 are its own start sets.

## F5 (SDP-N5 ⊇ N-SD-3; N-SD-4). Thin spots, recorded
- [Q docs/referee-2/R2-N5-SDPRIME.md@9784229a2:113] «N-SD-3 (thin spot). The packet's "cycles other than the end state's may come and go" is exercised in only 3 + 0 + 3 intervals.»
  The other new freedoms are well exercised (T_W ≠ T_H, λ_W moving; REFEREE-2 l. 114). EPOCH with CF ≥ 1 is exercised on few pieces (REFEREE:
  25 / 41 / 137 / 438; REFEREE-2: 24 + 50), and the bound (CF + 1)n − 1 is far from reached. MUT=1 bites only where the bound is sharp.
- [Q docs/referee-2/R2-N5-SDPRIME.md@9784229a2:116] «N-SD-4 ((H4′) is not vacuous). It fails at 4 + 28 (H3′)-intervals.» Recorded: (H4′) is a real
  hypothesis (also in the lane's data: 4 + 2 (H4′) failures, N5-PIECE-box25 §2).

## F6 (N-SD-6). R77's (CV) is not used
- [Q docs/referee-2/R2-N5-SDPRIME.md@9784229a2:119-120] «N-SD-6 (R77's (CV) step). STATIC-DEPTH′'s proof does not use R77's (CV) (cycle vertices constant). It uses item 1, which holds only for the
  end-state cycles.» ACCEPTED; this is the step that lets other cycles come and go (F5's thin spot).

## DONE / FINDINGS / NEEDS
- DONE: this fixes file (repairs only); piece/sdprime.py START=1 and its log; check.sh pins this file's quotes.
- FINDINGS: no signed statement changes; the §4 count difference was the start column (default vs pinned starts). The same (SW) "…" and the
  same W-MONO / Ξ-SUCC citation occur in the frozen P-N5-REL-box25 (§2 item 4 and premises); they will be repaired there in its own fixes
  file after its reports.
- NEEDS: none from the owner.
