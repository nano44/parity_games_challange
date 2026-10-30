# R2-N5-WRUN-L4: word-diff of the P-N5-WRUN line, revision L-4 (REFEREE-2 successor 23, Opus 5.5, D15)
Object: docs/new/P-N5-WRUN-box92-line-L4.txt @ l-new 5462315f, sha1 98d9a50c0268e82754b87f2c6db9b14e49f22d34 (re-hashed: match), against
L-3 (fb976deb, cbba7a1b). Token diff L-3 → L-4 (difflib over whitespace tokens), every change mapped:
| change | item | check |
| --- | --- | --- |
| «Σ_v SW_R(v)» → «Σ_{v′} SW_R(v′)» (XI-RUN) | my optional (summation index) | ✓ no shadowing of the global v |
| «Σ RET_F … Σ_{(X, g)} REG_F(X, g) + Σ_{(X, g)} FREE_F(X, g)» → «Σ_{(X′, g′)} RET_F(X′, g′) … Σ_{(X′, g′)} REG_F(X′, g′) + Σ_{(X′, g′)} FREE_F(X′, g′)» (TRIPLE-RED) | my optional | ✓ |
| PREFIX-MON «fixed over states t of F» → «fixed over consecutive states t of the run» | my optional (§7.2's range) | ✓ now exactly §7.2 |
| «(Theorem BIP-RED, with [SUB])» → «(Lemma SUB, signed by both referees: REFEREE-2 docs/referee-2/SUB-check.md, claude/referee-2 a11c2868, and REFEREE R-N5-WRUN §9.1, claude/referee 8c0b2e69) [SUB] holds, and (Theorem BIP-RED)» | WRUN-L5 (a), REQUIRED | ✓ verbatim my text; the citations are the right files, sections and commits; [SUB] as defined in the parenthesis is the statement both of us signed |
| WRUN-EQ «and, under [SUB], ⇔ SB-POLY ∧ R°-POLY ∧ FL-POLY» → «and ⇔ SB-POLY ∧ R°-POLY ∧ FL-POLY» | WRUN-L5 (a) | ✓ E8 now unconditional, consistent with Lemma SUB |
| the header «### R?? [proposed, P-N5-WRUN, revision L-3]» is removed (L-4 starts «N5 on EVERY game (…») | — | not a content change; the Lead adds the R-number heading at landing (note only) |
Nothing else changed. WRUN-L5 is CLOSED. All line items of both referees (G-WRUN-1, WRUN-L1..L5, my L-1..L-5) are closed.
Symbol test of the changed text: X′, g′ and v′ are bound by their sums; t ranges over the run's states; no new symbol is free.

## Verdict
L-4 (98d9a50c): **MATCHES** (Opus 5.5, D15). No required change.
