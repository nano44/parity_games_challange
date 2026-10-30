# P-N5-WCH fixes (box 79): answers to REFEREE 19 (claude/referee d71d6e55, docs/referee/R-N5-WCH.md) and REFEREE-2 22 (claude/referee-2 24f32388, docs/referee-2/R2-N5-WCH.md)
L-NEW successor 37 (Opus 5.5). APPEND-ONLY. The frozen packet docs/new/P-N5-WCH-box79.md (sha1 31caa72e5265b7373218ce64e38d253112189506,
l-new 2ad78f51) is NOT edited; where this file and the packet differ, this file governs. Both referees: every item SIGNED, no gap, nothing
false (Lead 10:32Z). Written 2026-10-30 from 10:35Z (date -u). Classes: WORDING / TAGS / LINE PRECISION / FINDING / DATA.

## W1-1 (TAGS) WCH-N1 = REFEREE-2 N-2: four SPEC line tags one line low
- Correct tags (text unchanged, verbatim at quote base aefb71a3): [S1-rank] [Q SPEC:27] (packet says 26); [S1-val] [Q SPEC:28-29] (27-28);
  [S1-ord] [Q SPEC:30-31] (29-30); [S1-Xi] [Q SPEC:32] (31). [S2] 47, [S4a] 51-53, [S4c] 56-57 are right.
- Quote check added: experiments/new/box79/quotecheck.py (every «…» SPEC quote of the packet, whitespace-normalised, must occur inside the
  lines of its CORRECTED tag in docs/new/N5-ssi-global.md). Result: 7 / 7 OK, QUOTECHECK PASS; with the packet's original tags it reports
  4 NOT FOUND (the check bites). Pinned in experiments/new/check.sh "box 79".

## W1-2 (WORDING) WCH-N2 = REFEREE-2 N-1: the case split by position of v on π
- Lemma TIE (§3). Read (a2) as «π reaches its cycle node c* before v (v lies on π's cycle)» and (a3) as «π reaches v before its cycle
  node c* (v lies on π's path part)». (a1) is «π never visits v». The three cases are exhaustive and the proofs are unchanged.
- Theorem RET-WCH (§4.2) Step 2: read (ii) as «π reaches the cycle node c before v» and (iii) as «π reaches v before the cycle node c».
  Proofs unchanged.

## W1-3 (LINE PRECISION) REFEREE-2 L-1 to L-4: one corrected line, docs/new/P-N5-WCH-box79-line-W1.txt (sha1 00f9e375c448153f19b7620037a2723f6d10a0b1)
- L-1: NZ_P's «at k or k + 1»: k is now bound in that clause («NZ_P the Z-flat in-phase fallbacks k → k + 1 of P …»).
- L-2: w declared: «if, for a function w : ℕ → ℕ, every τ-stretch S …».
- L-3: N5-LZC's σ′ defined directly (packet §7.1 verbatim in content): «which, with W* the [S1-val] valuation of the (σ*, τ_t)-plays, keeps
  σ_t(v) at every Even v whose W*(v) has length at least 1 and satisfies v ⊕ W*(σ_t v) = W*(v), and at every Even v with W*(v) = (v, ∅, 0)
  for which W*(σ_t v) has cycle node v and empty path set, and takes σ*(v) at every other Even v».
- L-4: «R84 (a) (Fact DELTA)» added to the premise list.
- Word diff against 9ac6fdba (git diff --no-index --word-diff=plain; complete):
  - {+R84 (a) (Fact DELTA),+}
  - {+k → k + 1+}
  - [-if-] {+if, for a function w : ℕ → ℕ,+}
  - [-which keeps σ_t(v) at every Even v where it is consistent-] {+which,+}
  - [-W*,-] {+W*+}
  - [-in the sense of Lemma TIE's two forms-] {+keeps σ_t(v) at every Even v whose W*(v) has length at least 1 and satisfies
    v ⊕ W*(σ_t v) = W*(v), and at every Even v with W*(v) = (v, ∅, 0) for which W*(σ_t v) has cycle node v and empty path set,+}
  - [-elsewhere;-] {+at every other Even v;+}
  Nothing else changed.
- Strict symbol test re-run (experiments/new/box79/symtest.py, output symtest_W1.out): W1 186 symbols, 0 failures, SYMTEST PASS. The test
  now also extracts ℕ and ∅ and binds w by its declaration. Under the updated table the OLD line 9ac6fdba fails 4 (NZ_P, W*, σ′: their
  binding phrases were reworded in W1; w: undeclared, = L-2). Pinned on W1 in check.sh "box 79".

## W1-4 (FINDING) WCH-N3: OPT-ONLY
- Both referees checked ASSUMPTION OPT-ONLY against R90's proofs and find it TRUE, so Corollary LZ-NOSIL holds (REFEREE 19 WCH-N3: «OPT-ONLY
  is true (§7); LZ-NOSIL can be stated without the assumption»). Recorded only; the signed text is not changed.

## W1-5 (DATA) WCH-N4: NC / NT not exhibited
- REFEREE 19 WCH-N4: NC_R = NT_R = 0 on the referee's whole corpus; SIL-Z (b)'s own-Ξ-cycle exclusion and the NT term are never exercised
  by data. Recorded: NC_R and NT_R are residuals with no instance; the statements are unaffected.
