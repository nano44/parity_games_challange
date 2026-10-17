# C7: landing gate for RESULTS R7 (packet 4: S0, PREFIX-MONO, POS-FALL, ROOT-BOUND, §22e reduction, bit cost) — CHECKER, 2026-10-17

Target: docs/agents/R7-draft.md at trunk 0eba38b (not edited). Branch: origin/claude/checker confirmed an ancestor of the
local branch, then trunk 0eba38b merged by merge commit.
Sources:
- GAP-A-M.md §22c/§22e at the pin 44d1428 (lines 1853-2010).
- docs/referee/R-P4.md: f74857c 12:04:21Z; §C at e0cb163, 12:15:17Z, compared against 352da6e.
- docs/referee-2/R2-P4.md: 352da6e 12:08:36Z; §8 at 69b38ab, 12:14:27Z, compared against f74857c.
- Code: Oink 8fbf0a7.

## Verdict: PASS (no required fix; recommended N-1..N-3, notes N-4, N-5)
| check | verdict |
| --- | --- |
| 1 statement diff (a)-(f), the four named points | PASS (N-1) |
| 2 verdict quotes and independence | PASS |
| 3 gap union; "closed" only for G-R7-1..3 | PASS on the header; two items not carried (N-2, N-3) |
| 4 re-run, REFEREE-2 P4 probe, corpus part | PASS: identical to probe4_results.txt (N-5) |

## 1. Statement diff
| item | §22 at 44d1428 / signed | draft | |
| --- | --- | --- | --- |
| (a) (S0) | §22c line 1929: "(S0) For every processed τ, P(τ) ⊆ Cl_{pr τ}(P(τ⁺) ∪ {τ})". Both SIGN, with Cl_q the triggered closure (REFEREE R-a1/R-b1, REFEREE-2 R-Cl) | Cl_q = "the TRIGGERED closure of the code (dtl_ideal.lfp ...)" | OK |
| (b) PREFIX-MONO + C1-C4 | §22c lines 1934-1950; both SIGN WITH GAPS, closed | as stated | OK |
| (c) POS-FALL | §22c line 1951; REFEREE SIGN; REFEREE-2 SIGN "(given FDL (ii)'s conclusion; see G-STR)", and §3: "it rests on (STR-DET) for the alignment" | "for clean transitions with e* in the root call ... Φ_top falls strictly" | OK. Unconditional only through REFEREE §C1's root-call exemption, which G-R7-7 discloses as one signature |
| (d) ROOT-BOUND | §22c lines 1960-1970; H = (n(n+1)+1)((n+1)(d+2)n+1)((n+1)n²+1); both SIGN WITH GAPS, closed | identical H and per-phase bound | OK |
| (e) reduction | §22e (two named statements at the pin); with additions: REFEREE (DOM-e*), G-e2 +1, G-STR; REFEREE-2 §8 corrected bound "S − 1 ≤ Σ_{R ∈ C_bv} (D_R+1)(H+1) + n·\|C_T\| + #(Dom-e* transitions) + 1, under (STR-DET-w)" | identical bound, +1 and Dom term included; "GAP-A ⇐ (CTX) ∧ (DIRTY) ∧ (DOM-e*) ∧ (STR-DET-w)" | OK. N-1 on who signed the (STR-DET-w) wording |
| (f) bit cost | both SIGN, conditional | "with S polynomial ... holds at bit cost" | OK |
The Lead's named points:
- (c) and (d) are root-call statements: yes ("with e* in the root call"; "whose e* is in the root call"; Scope "(a)-(d) are
  root-call statements"). (a) and (b) in fact hold per round at any fixed context (REFEREE (e) third bullet; REFEREE-2 §5
  (3)), so the Scope wording is narrower than signed, not broader.
- (e) is a reduction with four OPEN hypotheses, and the bound has the +1 and the Dom term: yes. Scope says "(e) is a
  reduction with four OPEN hypotheses, not a bound".
- (STR-DET-w) is worded as REFEREE-2 §8 has it. §8: "s+1 creates no tangle before its first set-level difference, and none
  at all if there is no set-level difference". The draft says the same with "from s" added.
- G-R7-7 ("the exemption has one signature; REFEREE-2 did not address it") is accurate. REFEREE-2 §8 (12:14:27Z) compares
  with f74857c and predates REFEREE §C (12:15:17Z), where the exemption first appears (C1, "One exception (my addition,
  checked)"). REFEREE-2 signs (c) "given FDL (ii)'s conclusion" and says in §3 that POS-FALL "rests on (STR-DET) for the
  alignment".
- N-1 (recommended; the same pattern as G-R7-7). The (STR-DET-w) wording of (e)'s hypothesis also has one explicit
  signature.
  - REFEREE §C, written against 352da6e, never saw §8. It signs the reduction "GAP-A ⇐ (CTX) ∧ (DIRTY) ∧ (DOM-e*) ∧
    (STR-DET)" with the weak form "s+1 creates no tangle before its first set difference, and one exists". That form
    implies (STR-DET-w), so it is the stronger hypothesis.
  - In substance REFEREE also covers (STR-DET-w):
    - REFEREE's main count covers the transitions that have a set difference (first clause).
    - REFEREE's G-e2 covers the barren transition: no differing tattr, s+1 re-finds only duplicates, last search, +1.
      (STR-DET-w)'s second clause supplies exactly its premise.
  - Suggest one sentence in G-R7-7 or G-R7-5: "(STR-DET-w) is REFEREE-2's §8 wording; REFEREE §C signs (STR-DET) in the
    stronger weak form, and the +1 by G-e2."

## 2. Verdict quotes and independence: PASS
- REFEREE (table, revised in §C2):
  - (a) SIGN; (b) SIGN WITH GAPS (R-b1 closed); (c) SIGN; (d) SIGN WITH GAPS (G-d1 closed);
  - (e) SIGN WITH GAPS, with G-e1 OPEN, G-e2 closed, and in §C2 "two OPEN gaps: G-e1/G-DOM and G-STR";
  - (f) SIGN, conditional.
  This equals the draft. Commits f74857c and e0cb163 are as cited.
- REFEREE-2: (a) SIGN; (b) SIGN WITH GAPS (G-Ψ, closed); (c) SIGN "(given FDL (ii)'s conclusion; see G-STR)"; (d) SIGN WITH
  GAPS (G-Ψ, closed); (e) SIGN WITH GAPS, G-DOM and G-STR OPEN; (f) SIGN (conditional). This equals the draft. Commits
  352da6e and 69b38ab are as cited.
- Independence: REFEREE "docs/referee-2/R2-P4.md was not read"; REFEREE-2 §8 "read after 352da6e was pushed". No REJECT in
  either report.

## 3. Gap union
| referee item | draft |
| --- | --- |
| REFEREE R-a1/R-b1 = REFEREE-2 R-Cl (triggered closure) | G-R7-1 |
| REFEREE G-d1 = REFEREE-2 G-Ψ | G-R7-2 |
| REFEREE G-e2 (+1), agreed REFEREE-2 §8 | G-R7-3 |
| REFEREE G-e1 = REFEREE-2 G-DOM, as (DOM-e*) | G-R7-4 |
| REFEREE-2 G-STR (§0), confirmed by REFEREE §C1; effect on R5 (h) (both) and on REFEREE-2's R2-PROVED2 §13.1 | G-R7-5 ("It also conditions RESULTS R5 (h) except for root-call first differences") |
| (CTX), (DIRTY) | G-R7-6 |
| REFEREE §C1 root-call exemption; FDL; O1; 1.2b; DTL-proof §3(e) | G-R7-7 |
| REFEREE §C2: "R-P3 (d), GAP-A first step: unaffected if 'root call' means the first best_vertices call. If it means any best_vertices call of the depth-0 search_rec, it needs (STR-DET) for calls after the first sptl." | **not carried** (N-2) |
| REFEREE open point 3 = REFEREE-2 §8 union: "PI-RISE on dirty transitions (§22d), DATA only" | **not carried** (N-3) |
- "Closed" applies only to G-R7-1..3: "G-R7-1..3 are closed in the reports and to be imported into the author's text; G-R7-4..6
  are OPEN and are hypotheses of (e); G-R7-7 lists dependencies". Correct.
- N-2 (recommended). REFEREE §C2 qualifies a LANDED result: R-P3 (d) is RESULTS R6 (e). Add to G-R7-5: "RESULTS R6 (e) holds
  without (STR-DET) only if its 'root call' is the first best_vertices call of the search (REFEREE §C2)". The Lead should
  note the same on R6.
- N-3 (recommended). Add to G-R7-6: "PI-RISE on dirty transitions (§22d): DATA only (REFEREE open point 3; REFEREE-2 §8)".

## 4. Re-run (REFEREE-2 docs/referee-2/R2-P4/ @ 352da6e, corpus part)
- Build: dtl_probe4_full.patch on Oink 8fbf0a7. Its removed lines are the same counter-only rewrites as R2-PROVED2/R2-P3.
  Release build.
- Corpus: the 254-file list that REFEREE-2 used. The corpus at 352da6e has 257 files; the three newer ones are
  kin_viol_n29, meet_viol_n17 and meet_viol_n29.
- run2.sh (both in-orders × labellings 0-1; R2FDLSUM): 1,014 runs; pairs 4,214, nodiff 0, newbefore 0. REFEREE-2's 4,290
  pairs are corpus + random. The corpus part is consistent: 0 / 0 as reported.
- run3.sh (labelling 0; R2EST): region 282, rescue level 766, −1 attractor 43, Dom 0. Identical to probe4_results.txt.
- Not re-run: the random part (6,000 runs).
- N-5 (data label). run3.sh greps R2EST only in its rev=1 branch (the rev=0 branch greps R2FDLSUM). So the 1,091 first
  differences come from ONE in-order, although R2-P4 says "corpus × 2 in-orders". I re-ran with both branches grepping
  R2EST: rev=0 gives the same 282 / 766 / 43 / 0. So the claim "0 in Dom" holds for both in-orders (0 of 2,182). The
  draft's "0 of 1,091" is exact for one in-order and conservative. No change needed.

## Notes
- N-4. G-R7-7 says FDL (R5 (h)) is a dependency "for (c)-(e)". After REFEREE §C2, R5 (h) is itself SIGN WITH GAPS (G-STR
  open) except for root-call first differences. That is consistent with G-R7-5.

## Fix list (none required)
Recommended: N-1 (STR-DET-w signature status), N-2 (R6 (e) qualification), N-3 (PI-RISE). The draft may land as written;
if edited, I re-diff the text only.

## Addendum: re-diff at trunk 1e4babe (Lead 12:32Z; REFEREE-2 R2-P4 §9 at 5ae9747)
History: 0eba38b is an ancestor of 1e4babe, and 5ae9747 (12:26:33Z) is an ancestor of 1e4babe. R2-P4.md is identical at
5ae9747 and at 1e4babe. docs/referee/ is unchanged since 0eba38b. Trunk 1e4babe was merged into claude/checker by merge
commit.

### Verdict: PASS (unchanged; N-1..N-3 still open as recommended)
- R7-draft.md, 0eba38b → 1e4babe: the diff touches only the header stamp and G-R7-7, as the Lead said. (a)-(f), the
  Signatures line, G-R7-1..6 and Scope are byte-identical.
- New G-R7-7 against §9:
  | draft | R2-P4 §9 | |
  | --- | --- | --- |
  | "For root-call first differences G-STR cannot arise (no extraction before e*; ...)" | "Claim: G-STR cannot arise when e* lies in the root best_vertices call"; "Nothing runs before it in the search: no sptl, no extraction, no Dom" | OK |
  | "inside best_vertices no set test reads str: 73 tests only '== -1'" | "Inside best_vertices no set test reads str: 73 tests only `str[from] == −1` and writes str" | OK |
  | "signed by REFEREE §C (e0cb163) and REFEREE-2 §9 (5ae9747)" | §9 heading: "SIGN (Opus 5.5, D12)"; "So I sign the exemption" | OK. Two signatures; the G-R7-7 claim of one signature is now correctly withdrawn |
  | "so (c) and (d) are independent of (STR-DET-w), which affects only non-root first differences" | "POS-FALL and ROOT-BOUND (§3, §4) hold as signed, with no dependence on (STR-DET). G-STR affects only first differences after the root call" | OK. §9 names (STR-DET), the draft (STR-DET-w). §9's argument uses no str fact at all ("Their classification needs no str argument"), so it covers both |
- Code anchors of §9, checked on Oink 8fbf0a7 dtl.cpp (anchors only, not the argument):
  - best_vertices is 644-779. It calls attracts (41), attractVertices (66) and attractTangles (198)/attractTangle (110).
  - In 41-209 and 644-779 the only non-logging read of str is 73 (`str[from] == -1`). 89, 171 and 694 are writes.
  - The other reads (268, 316-317 in extractTangles; 515 in sptl) are outside the root call.
  - search_rec (835) runs no computation before its first best_vertices call (853): only declarations and trace output.
- REFEREE-2 §0/§3 ("POS-FALL rests on (STR-DET) for the alignment") is superseded for root-call e* by §9. The draft's
  Signatures line still says REFEREE-2 signs (c) "given FDL (ii)'s conclusion". That stays accurate: §9 shows that
  conclusion holds at a root e* without (STR-DET).
- Independence: §9 reviews REFEREE's §C claim, so it is written after reading it by design. This is a cross-signature, not
  an independent derivation. The independence of the main reports (§2 above) is unaffected.
- RESULTS R5 (h), touched by the same Lead commit: "an exemption signed by both referees (REFEREE-2 R2-P4 §9, 5ae9747)" is
  accurate.
- Not applied at 1e4babe (still recommended): N-1 ((STR-DET-w) wording has one explicit signature), N-2 (REFEREE §C2
  qualification of R6 (e)), N-3 (PI-RISE on dirty transitions).
- N-6 (note, outside the draft). GAP-A-M §22h at 1e4babe (L-ALG, unrefereed) states the weak form as "s+1 creates no tangle
  before its first set difference, and every transition but the last has a set difference". This is not REFEREE-2 §8's
  (STR-DET-w). §22h also writes the reduction with (FALL) for (DIRTY). R7 (e) pins §22e at 44d1428 and §8's wording, so R7
  is unaffected. Any later result citing §22h needs its own diff.

## Addendum 2: text re-diff at trunk 86502cd (Lead 12:39Z): PASS
History: 1e4babe is an ancestor of 86502cd. R7-draft.md has the same blob at 6a4003d and 1e4babe; 6a4003d touched only
LEAD-STATE.md, and the Lead noted its message overstated it. Text only, no re-runs.
- 0eba38b → 1e4babe (G-R7-7, two signatures): checked in Addendum 1. PASS.
- 1e4babe → 86502cd: the diff is the header stamp, G-R7-5 (+3 lines) and G-R7-6 (+1 line). Nothing else moved.
  - N-1 applied in G-R7-5: "The (STR-DET-w) wording is REFEREE-2 §8's; REFEREE §C signs the stronger form (STR-DET) and
    covers the no-difference case through G-e2, so both cover (STR-DET-w) in substance". This matches N-1. OK.
  - N-2 applied in G-R7-5: "RESULTS R6 (e) holds without it only if 'root call' means the first best_vertices call of the
    search (REFEREE §C2)". This matches §C2 ("unaffected if 'root call' means the first best_vertices call"). OK. The Lead
    adds the same reading to R6 (e) at landing; that will need its own text check.
  - N-3 applied in G-R7-6: "Π rising on dirty transitions that do not lower RV (GAP-A-M §22d; REFEREE open point 3,
    REFEREE-2 §8)". At 44d1428, §22d's open part is "dirty transitions where RV does not fall" (PI-RISE, line 1999:
    "whose root RV does not fall raises Π strictly"). REFEREE open point 3 (R-P4 line 138) and R2-P4 §8 (line 197) say
    "PI-RISE on dirty transitions". The draft's restriction to transitions that do not lower RV is §22d's own scope. OK.
- No open recommendations remain. R7 may land as at 86502cd.
