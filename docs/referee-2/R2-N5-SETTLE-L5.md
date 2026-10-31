# R2-N5-SETTLE-L5: word-diff of the P-N5-SETTLE line, revision L-5 (REFEREE-2 successor 24, Opus 5.5, D15)
- Object: docs/si/P-N5-SETTLE-line-L5.txt @ l-si ce7bdc3b, sha1 39e44fe2b8b4cced9133270de0896e7652cc859c (re-hashed: match).
- Compared with L-4 (b04a1bbb, sha1 6ed61d84; R2-N5-SETTLE-L4.md, b441f3da).
- Token diff (844 → 868 tokens) has four changes and nothing else.

| change | item | check |
| --- | --- | --- |
| R57 gloss «for S4a, σ_new is …» → «for S4a at a transition t → t + 1, σ_(t+1) is …» | my P-1 / REFEREE SETTLE-L6 | ✓ t is now bound by the transition, and σ_(t+1) is a line symbol |
| ONE-STEP citation + «, which closes gap G-SRC-1 (REFEREE R-N5-SRC §3, claude/referee 81f6b89c)» | G-SRC-1 naming | ✓ the right file, section and commit, the same as SRC L-3 |
| scope tail «… XCN-POLY)» → «… XCN-POLY; Lemma ONE-STEP (Cases 2, 2b) is referee-originated)» | SET-L4-1 (REQUIRED) | ✓ L41's scope-tail clause |
| «entries 1-4)» → «entries 1-5)» | bookkeeping | ✓ |
- Strict symbol test of the changed text:
  - t is bound by «at a transition t → t + 1»;
  - H_t, σ_t, Iσ_t and τ_t are read at that t;
  - G-SRC-1 is a cited label with its source.
  No free symbol.
- Left optional: the second half of my P-1, «Even keeps σ_t ∪ Iσ_t» (a strategy united with an edge set; the line's own H_k reads
  «{σ_k(v)} ∪ Iσ_k(v)»). It is a precision only, and the reading is unambiguous.

## Verdict
L-5 (39e44fe2): **MATCHES** (Opus 5.5, D15). No required change. SET-L4-1 is CLOSED. All SETTLE line items on my side are closed.
