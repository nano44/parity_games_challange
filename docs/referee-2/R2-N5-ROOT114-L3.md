# R2-N5-ROOT114-L3: word-diff of P-N5-ROOT line L-3 (REFEREE-2 successor 25, Opus 5.5, D15; written 2026-10-31 23:39Z by date -u)
- Object: claude/l-new 4cac9dc5, docs/new/P-N5-ROOT-line-L3.txt, sha1 7b0916921c39cd6f11bde9c4d8f1eed6be1bf81d (re-hashed: match).
  - Base: L-2 (7988e2f4, c9c6b380), MATCHED in R2-N5-ROOT114-L2.md (3bb41a4c). 825 → 848 words.
- Premises: R98 (l. 8296) and R99 (l. 8596), read at trunk 96b0207b (origin/claude/vibrant-johnson-nxvvxo).

## Token diff L-2 → L-3: exactly these changes, nothing else
1. «P-N5-STAIR (Lemma COPY … STAIR, as in its line L-2: l-new 6903f1b3, …, sha1 44f56e96…)» → «RESULTS R99 (P-N5-STAIR: Lemma COPY …
   STAIR)».
2. «P-N5-ODD (Corollary FUEL-COUNT: l-si 0afc0d70a, …, sha1 03eec41d, with its fixes entries 1-2))» → «RESULTS R98 (P-N5-ODD: Corollary
   FUEL-COUNT))».
3. «β, … DESC_F as in P-N5-STAIR's line L-2;» → «… as in RESULTS R99;».
4. «every root descent is a fuel re-route» DEAD → «every R-descent is a fuel re-route» DEAD.
5. A new L41 clause in the scope tail (the text after the statements: DEAD notes, OPEN / not-M3 labels): «the proof of DESC-ROOT uses COPY's
   converse, whose proof is referee-originated (RESULTS R99: G-ST-1 = P-1), the proof of ORIGIN-NEW uses a step of that proof, and the
   proof of FUEL-ROOT-STAIR uses FUEL-COUNT, whose proof carries referee-originated repairs (RESULTS R98: G-ODD-1, G-ODD-2);».
6. «entries 1-3)» → «entries 1-4)».

## Checks
- **ROOT114-L2 is fully closed.** R99 and R98 have landed.
  - R99's line states Lemma COPY as «β(W(v)) and β(W(z)) have the same flips at k, in the same directions, through a strictly increasing
    position map» and «C-vertices keep the value (c, ∅, 0) on F». That is both directions, exactly the [COPY] the packet uses.
  - R99's line also defines β, descents and DESC_F, and states Theorem STAIR.
  - R98's line states FUEL-COUNT (with (y, z) bound, per L-2).
- Item 4: «R-descent» is the line's own defined term (type R), and frz32's 3 old-edge relays are R-descents (my pins.txt: R^old 3). It is
  more precise and remains a non-asymptotic, one-instance DEAD (L43).
- Item 5 is accurate, and it is about the premises:
  - DESC-ROOT uses [COPY] in both directions. The converse's proof is G-ST-1 = P-1, and R99's own tail labels it referee-originated.
  - ORIGIN-NEW's proof step «y is not in the path set of W_k(z0) … nor in that of W_(k+1)(z) …, as in [COPY]'s proof (G-ST-1)» (packet
    l. 97) is that proof's rank-bit constancy fact.
  - FUEL-ROOT-STAIR uses FUEL-COUNT, and R98's tail names G-ODD-1 and G-ODD-2.
  - ROOT's own proofs remain not referee-originated: my P-1 (NEW-FUEL via R15 (d)) was not taken, and nothing else was supplied.
- No free symbol, no new claim. The scope words are unchanged.

## The Lead's question: «a FUEL RE-ROUTE … as in P-N5-ODD §6» → «as in RESULTS R98»?
- **Yes, recommended.** R98's line defines «a fuel re-route of a pair (y, z) at k := Even y switches to z = σ_(k+1)(y) at k with k − 1 ∈ F,
  (y, z) ∉ H_(k−1) and Ξ_(k−1)(z) ≠ Ξ_k(z)». It also defines the key «(2, 0) … else (1, r) with r the top rank …». Both are identical in
  substance to L-3's parenthesis and KEY clause.
- L-3 dropped the 0afc0d70a / 03eec41d pin from the premise list. «P-N5-ODD §6» is therefore now the line's only unpinned packet citation,
  the kind REFEREE's ROOT-L2 asked to remove.
- Since L-3 restates the definition in full in the parenthesis, the line is unambiguous either way. So I rate this a precision, not a blocking
  item: «… is as in RESULTS R98 (y switches …)».

## Verdict
**MATCHES** (Opus 5.5, D15). Optional precision: «as in P-N5-ODD §6» → «as in RESULTS R98».

## DONE / FINDINGS / NEEDS
- DONE: this file; the token diff; R98 and R99 lines read at trunk 96b0207b.
- FINDINGS: ROOT L-3 MATCHES. The L41 premise clause is accurate. Changing the fuel re-route citation to R98 is recommended (a precision).
- NEEDS: none.
