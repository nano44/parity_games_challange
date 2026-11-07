# R2-N5-STAIR-L3: word-diff of P-N5-STAIR line L-3 (REFEREE-2 successor 25, Opus 5.5, D15; written 2026-10-31 20:28Z by date -u)
- Object: claude/l-new 7dc1eb7c, docs/new/P-N5-STAIR-line-L3.txt, sha1 9db0b169aadcbc5f81b2c0157f124946bbf74ad9 (re-hashed: match).
  - Base: L-2 (l-new 6903f1b3, sha1 44f56e96…, re-hashed), MATCHED by my predecessor (R2-N5-L2-confirm.md, cf5157fe).
  - 852 → 865 words. Asked by CHECKER C109; the fixes are in entry 7 of docs/new/P-N5-STAIR-fixes-box112.md at 7dc1eb7c.

## Token diff L-2 → L-3: exactly four replacements, nothing else (byte test True; each source phrase occurs once in L-2)
1. «the one-player arena H_k);» → «S4a's one-player arena at k);».
   - H_k occurred only here in L-2, so dropping the name leaves no free symbol.
   - S4a's arena at k is defined by SPEC, as in R91 / R93.
2. «DESC-LIN (DESC_F ≤ c·n) DEAD (L-RED R162, claude/l-red 54832628: passive observers, cp_K); » is removed.
   - This is consistent with Lead ruling L43, as relayed 20:29Z: a lane DEAD of an asymptotic statement enters a RESULTS line as DATA or
     not at all. No DESC-LIN or R162 text remains in L-3.
3. «TARGET.md claim)» → «TARGET.md claim; the proof of DESC-COPY uses COPY's converse, whose proof is referee-originated (G-ST-1 = P-1,
   written independently by REFEREE and REFEREE-2; docs/new/P-N5-STAIR-fixes-box112.md entry 1))».
4. «entries 1-6)» → «entries 1-7)».

## The attribution of P-1 (REFEREE-2's side)
- My predecessor's report docs/referee-2/R2-N5-STAIR.md (claude/referee-2 f92b278a, committed 13:06:38Z) proves COPY's converse in its
  COPY item, l. 69-78.
  - It gives both constancy facts: «v's own rank bit is constant: v ∉ P(z)» and «The one bit of z with no image is constant too:
    [sl(z) ≥ n] = 0 when ℓ(z) ≤ n − 1, and [sl(z) ≥ −n] = 1».
  - It concludes «the non-constant bits of v and z correspond bijectively and in order».
  - P-1 (l. 79-81) points to this as DESC-COPY's converse.
- REFEREE's G-ST-1 (claude/referee a61a258b, 13:41:23Z) came later, and my predecessor's notebook rule kept docs/referee/ STAIR closed
  until both reports were pushed.
- So «written independently by REFEREE and REFEREE-2» is right for my side. «referee-originated» is right as well, under L41.
  - It is a proof text supplied by the referees.
  - Each referee signed it: REFEREE in a61a258b, and my predecessor by writing it.
  - The other independently signed it: entry 1 quotes both; my predecessor's f92b278a covers REFEREE's argument in substance.
- Precision, optional: P-1 itself is the «precision» bullet. The PROOF is in the COPY item just above it, so «P-1 (with the COPY item of
  R2-N5-STAIR.md)» would point more exactly. This is not required.

## Verdict
**MATCHES** (Opus 5.5, D15). Nothing REQUIRED from me.

## DONE / FINDINGS / NEEDS
- DONE: this file; the token diff and byte test; the attribution check against f92b278a / a61a258b commit times and text.
- FINDINGS: STAIR L-3 = L-2 + exactly the four stated changes. MATCHES. The P-1 attribution «written independently» holds for REFEREE-2.
- NEEDS: none.
