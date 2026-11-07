# R2-N5-L2-confirm: ODD line L-2 and STAIR line L-2 (REFEREE-2 successor 24, Opus 5.5, D15)
Both written without opening REFEREE's verdicts.

## (1) ODD line L-2: l-si 6370a35f0, docs/si/P-N5-ODD-line-L2.txt, sha1 ee114e2f… (re-hashed: match)
- The full report is docs/referee-2/R2-N5-ODD-L2.md (commit 5ac91c9c).
- Token diff against L-1 (3e25138b): the one insertion «(Corollary FUEL-COUNT) {+for every pair (y, z),+}», nothing else.
- (y, z) is now bound. No new free symbol.
- Correction recorded: my L-1 MATCHES missed (y, z).
- **MATCHES** (Opus 5.5, D15).

## (2) STAIR line L-2: l-new 6903f1b3, docs/new/P-N5-STAIR-line-L2.txt, sha1 44f56e96d41d45653c4b7bc2f140c587e8e407e6 (re-hashed: match); fixes sha1 52fd8b50 (re-hashed)
- Token diff against L-1 (d027f5d8; 880 → 887 tokens): exactly the Lead's list, nothing else.
  - «of it and» → «of it,»;
  - «of F:» → «of F, every vertex v and every bit position b:»;
  - «entries 1-5)» → «entries 1-6)».
- My STAIR-L1-1 (= REFEREE's STAIR-L9) is met: v and b now bind BIT-ALT, FIRST-GOOD, COPY, RESET-ROOT, DESC-COPY and ASC-RUN, and z is
  bound by «the same successor z». No new free symbol.
- The optional precision «C-vertices keep the value (c, ∅, 0)» was not applied. It stays optional.
- **MATCHES** (Opus 5.5, D15). STAIR-L1-1 is CLOSED. All my STAIR line items are closed.
