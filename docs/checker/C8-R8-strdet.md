# C8: landing gate for RESULTS R8 (Lemma STR-DET) — CHECKER, 2026-10-17

Target: docs/agents/R8-draft.md at trunk 44af920 (not edited). Branch: origin/claude/checker confirmed an ancestor of the
local branch, then trunk 44af920 merged by merge commit.
Sources:
- GAP-A-M.md §22i at the pin f920dc2 (line 2156 ff.).
- docs/referee/R-P5.md at ca03021 (commit 12:36:22Z).
- docs/referee-2/R2-P5.md at 6d508da (commit 12:35:59Z).
- f920dc2, ca03021 and 6d508da are all ancestors of 44af920. Both reports are byte-identical at 44af920.
- Code: Oink 8fbf0a7. No re-runs, as instructed.

## Verdict: PASS (no required fix; recommended N-1..N-4; notes N-5..N-7)
| check | verdict |
| --- | --- |
| 1 statement diff (a)-(d) and the three named points | PASS (N-1, N-2, N-3) |
| 2 verdict quotes and independence | PASS (N-6) |
| 3 gap union | PASS |
| data line | PASS (N-4 citation) |

## 1. Statement diff
| item | §22i at f920dc2 | signed | draft | |
| --- | --- | --- | --- | --- |
| premise | "Align their reduced logs (§21d) up to a point π, and suppose every tattr before π has the same input and the same SET output" | both | "reduced logs ... aligned up to a point π with equal inputs and equal set outputs before π" | OK |
| (a) | "no tangle of T_{s+1} \ T_s^π fires in any sptl region computation before π" | REFEREE: SIGN WITH GAPS, W-a1: "state (a) for T_{s+1} \ T_s^ρ (ρ = the region's point)"; REFEREE-2: SIGN, table wording "T_{s+1} \ T_s^π" | "No tangle that s lacked when it computed a given sptl region before π (i.e. in T_{s+1} \ T_s^ρ for the region at point ρ < π) fires in that region in s+1" | OK, W-a1 form (N-1) |
| (b) | "every sptl region computation before π is step-identical in s and s+1, including str" | both SIGN | same | OK |
| (c) | "every SCC extracted before π is the same, s+1 creates no tangle before π, and the W bits agree" | both SIGN; `more`: REFEREE "the `more` flags agree except for s's repeated pass, which is pure"; REFEREE-2 "`more` (873) agrees" | adds "and the `more` flag agree before π" | OK with N-2 |
| (d) | "if no tattr differs at all, s+1 creates no tangle, returns false (1068) and is the last search of the phase (G-e2)" | both SIGN (1068, 1113/1120) | same, "(at most one per phase)" | OK |

The Lead's named points:
- (a) is worded with W-a1 (T_{s+1} \ T_s^ρ): yes.
- N-1 (recommended). REFEREE-2 signed (a) in the pin's T_s^π wording. W-a1 is stronger, since T_s^ρ ⊆ T_s^π, so it
  excludes more tangles. In substance REFEREE-2's proof covers it: its Case A is "t created by s in a later piece, at any
  depth", which includes a piece after the region but before π. That is the split REFEREE uses to justify W-a1. As in
  C7 N-1, the W-a1 wording has one explicit signature. Suggest a sentence in G-R8-1: "REFEREE-2 signs the T_s^π wording;
  its Case A (any later piece) covers W-a1 in substance."
- "Consequences signed by both" line:
  | draft clause | REFEREE R-P5 | REFEREE-2 R2-P5 | |
  | --- | --- | --- | --- |
  | G-STR CLOSED for every first-difference location (bv, −1 attractor, sptl, Dom) | "G-STR: CLOSED". (a) section: 171-vs-89 can still occur "in best_vertices regions and in −1/Dom attractors, but extraction never reads those str values" | "It closes them for every first-difference location (bv, −1 attractor, sptl, Dom)" | OK (N-5) |
  | str part of G-h1 closed | "The str part of G-h1 is closed" | "The str part of G-h1 (R2-PROVED2 §13.1): CLOSED" | OK |
  | R5 (h) holds without the (STR-DET) condition | "FDL R5 (h): SIGN WITH GAPS (Opus 5.5, D12), all closed. My R-P4 §C verdict 'conditional on (STR-DET)' is withdrawn" | "FDL (ii)/(iii) hold on the reduced log without the (STR-DET) condition, given this lemma" | OK |
  | R7 (e)'s (STR-DET-w) discharged | "§22e: the (STR-DET) term is discharged" (implies the weak form) | "(STR-DET-w) is discharged" | OK |
- G-R8-2 states REFEREE's corrected Case A argument. It does: the PREFIX-MONO absorbed case is replaced by the Dom
  closure D_τ under the threshold-pr(τ) triggered rules, which gives ⊇ Cl(P(τ⁺) ∪ {τ}) ⊇ Z_τ by (S0). It also notes
  REFEREE-2's D_{≥σ} argument.
  - N-3 (recommended, citations).
    - "Dom attracts into X (136)": Dom's target is X by the calls at 884-885 (attractVertices/attractTangles with Z = X;
      loop 877-890). Line 136 is `else if (Z[v]) continue; // already attracted`, i.e. Dom SKIPS vertices already in X.
      That is what lets X-straddling tangles fire (REFEREE: "Dom SKIPS every vertex already in X (136, target = X)").
      Suggest "Dom's target is X (877-890); attractTangle skips vertices in X (136)".
    - "Cl(" should read "Cl_{pr τ}(", as in both reports.
    - REFEREE's step "Dom runs after sptl, with T_s^{Dom} ⊇ T_s^{pass 1}" is not stated. REFEREE-2: "The Cl tangle set is
      s's pass-1 set, which is ⊆ Dom's". Optional.
- N-2 (recommended). REFEREE qualifies `more`: "agree except for s's repeated pass, which is pure". The draft's
  "(c) ... the `more` flag agree before π" is exact only on the reduced log, where repeated passes are deleted. The
  premise sets that frame, but suggest "(on the reduced log)" after "`more` flag".

## 2. Verdict quotes and independence: PASS
- REFEREE (table): (a) "SIGN WITH GAPS: W-a1 (wording, closed), G-a2 (Case A's justification replaced, closed)"; (b), (c),
  (d) SIGN. This equals the draft.
- REFEREE-2 (table): (a)-(d) **SIGN**. This equals the draft.
- Both use the "(Opus 5.5, D12)" labels.
- Independence: REFEREE "docs/referee-2/R2-P5.md was not read"; REFEREE-2 "docs/referee/R-P5.md was not read before this
  report was pushed". No REJECT.
- N-6 (label). R2-P5's header says "12:40Z (date -u)", but 6d508da is committed at 12:35:59Z. It is a stamp
  inconsistency only; the commit order (6d508da 23 s before ca03021) does not affect the independence statements.

## 3. Gap union
| referee item | draft |
| --- | --- |
| REFEREE W-a1 | G-R8-1 |
| REFEREE G-a2 = REFEREE-2 §2 D_{≥σ} argument | G-R8-2 |
| context chain (REFEREE "R-PROVED2 §C5"; REFEREE-2 "R-PROVED2 §13.2 and REFEREE §C5"), SCC1, (S0), O1, 1.2b; nothing Lean-checked | G-R8-3. "RESULTS R5 (b)" is right: the context chain is R5's G-R5-1 under (b) |
| both: G-DOM / (DOM-e*) untouched, stays OPEN | Scope ("the Dom term (RESULTS R7 (e); GAPS G-DOM)") |
| both: open terms (CTX), (DIRTY)/(FALL) | Scope |
| REFEREE-2: induction along the reduced log ("the statement needs and has") | not a gap; covered by the premise |
| REFEREE-2: extra firings in bv/−1/Dom not excluded "and need not be" | not a gap; consistent with N-5 |
- "all closed in the reports, to be imported into §22i": correct. G-R8-1 and G-R8-2 are closed in REFEREE. REFEREE-2 has
  no gap. G-R8-3 lists dependencies, which is correctly not a "closed" item, although the header lumps it in.

## Data line
- "1,065/1,065 (Oink) and 1,035/1,035 (stable) on the corpus plus 4 instances": §22i at f920dc2. OK.
- "0 of 4,290 same-phase pairs (REFEREE-2 R2-P4 probe)": R2-P5 header. The corpus part was re-run in C7. OK.
- N-4 (recommended). "3,377/3,377 on 600 cross unions (stable) (L-ALG)" is not at the pin: §22i there says "Union runs:
  pending at 12:26Z". The figure is in GAP-A-M at 44af920 line 2235 ("DATA, cross unions s11 (UM_CROSS = 3, 600 games,
  stable order): weak STR-DET 3,377 / 3,377"), added by l-alg 6d79ce8 (§22j). Cite "GAP-A-M §22j, l-alg 6d79ce8". It is
  evidence only, so not blocking.

## Notes
- N-5. "every first-difference location" is explicit in REFEREE-2 only. REFEREE's "G-STR: CLOSED" with its (a) paragraph
  (str differences outside sptl are never read by extraction, F3) covers the same ground. Consistent.
- N-7. R7's post-gate note cites RESULTS R8. Land R8 before or with R7 (C7 Addendum 3).

## Addendum: RESULTS R6 (e) note (Lead 12:49Z), text only: PASS
Proposed line: "Note (CHECKER C7 N-2; REFEREE R-P4 §C2): 'root call' here means the first best_vertices call of the search;
read that way, (e) holds without (STR-DET), which RESULTS R8 in any case discharges."
- REFEREE R-P4 §C2 (e0cb163): "R-P3 (d), GAP-A first step: unaffected if "root call" means the first best_vertices call.
  If it means any best_vertices call of the depth-0 search_rec, it needs (STR-DET) for calls after the first sptl."
- R-P3 (d) is R6 (e). The trunk text says so: "R6 (e) = reports' (d)", RESULTS at 44af920.
- R6 (e) at 44af920 uses the phrase "in the root call's threshold loop", so the note attaches to existing wording.
- The note matches §C2:
  - "first best_vertices call" is §C2's reading;
  - "holds without (STR-DET)" is §C2's "unaffected";
  - "RESULTS R8 in any case discharges" is accurate under the other reading too. Both R8 referees close G-STR "for every
    first-difference location" (R2-P5), "G-STR: CLOSED" (R-P5).
  - The last clause depends on R8 being landed, so land R8 before or with this note (as N-7).
- Cosmetic: the reference "CHECKER C7 N-2" is right (C7-R7-packet4.md N-2).

## Fix list (none required)
Recommended:
- N-1: W-a1 has one explicit signature.
- N-2: `more` on the reduced log.
- N-3: G-R8-2 citations: 136 vs 877-890, Cl_{pr τ}.
- N-4: cite §22j / 6d79ce8 for the union data.
The draft may land as written. If edited, I re-diff the text only.
