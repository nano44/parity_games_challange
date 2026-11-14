# R2-P-IDEAL-CUBE-L2: REFEREE-2 word-diff of P-IDEAL-CUBE line L-2 against L-1, and fixes entries 1-2
Referee: REFEREE-2 successor 26, Opus 5.5 (D15). Written 2026-11-04 (date -u; see the commit). Verdict: **MATCHES**.

## 0. Object
- Commit: claude/l-new a0bb269499779a9dd766b6fe504f0fc6166d0b31, an ancestor of origin/claude/l-new. Re-hashed:
  - packet 366afedc (186 lines, unchanged);
  - L-1 99ae8fac (unchanged);
  - L-2 449421e4cfaedbef577f68720fab4924111cd170 (1 line, no «|»);
  - fixes 006274ec3f0aa82ceac8fa9b8f294f1f8d2e138e (30 lines).
  All equal the Lead's figures.
- RESULTS R105 is on trunk (claude/vibrant-johnson-nxvvxo bed56cba, RESULTS l. 10155), so «RESULTS R105» in L-2 is a landed citation.

## 1. Word-diff L-1 → L-2
- difflib gives 8 hunks. Byte test: L-1 with exactly the 6 replacements below, each old phrase occurring once, equals L-2: **True**.

| # | change | item | ✓ |
| --- | --- | --- | --- |
| 1 | «LOCAL (b), (c), signed, RESULTS R105 when landed;» → «LOCAL (b), RESULTS R105; π a topological order of the Ξ-graph;» | LC-P2 (drop unused (c)); R105 landed; LC-P1 (π bound at first use) | ✓ |
| 2 | «arXiv:2207.05985,» → «arXiv:2207.05985v1,» | LC-P3 | ✓ (the version I read) |
| 3 | «(π a topological order of the Ξ-graph)» deleted at the comb clause | LC-P1 (moved, not lost) | ✓ |
| 4 | L_K: + «(all movers of degree 2, distinct gate indices)» | REFEREE CUBE-L3 | ✓ (= packet §4) |
| 5 | «bound, and the W-key rule must carry any such bound;» → «bound (READING: a polynomial bound on T must use the W-key rule);» | REQUIRED LC-2 = REFEREE CUBE-L1 | ✓ verbatim as I asked |
| 6 | «(DATA: on L_K the IDEAL run» → «(DATA: on L_K with gate indices increasing in the option index, the IDEAL run» | REQUIRED LC-1 | ✓ verbatim as I asked |

- Nothing else differs. Entry 2's hunk list agrees with mine.
- Entry 2 says it follows ladder.py's gate order «g(x, k) = 2x + k». L-2 states only «increasing in the option index», which is all
  the DATA clause needs (my probe: increasing gives T = 0, decreasing gives T = 1). ✓

## 2. Fixes entry 1 (my P-1) ✓
- The new §0 text: face k's set contains β(x, k) and not β(x, 1 − k), because by acyclicity neither chain returns to x; ENC (R105)
  then orders them strictly.
- That is exactly the correction I asked for. «No proof in the packet changes» is correct.

## Verdict
**MATCHES.**
- L-2 (449421e4) = L-1 + the two REQUIRED changes (LC-1, LC-2) + the optional LC-P1 to LC-P3, CUBE-L3 and the R105 citation.
- Every clause is a signed statement with its exact hypotheses: acyclic, degree ≤ 2.
- Premises: R104's definition, P-IDEAL-RED ENC and LOCAL (b) (R105, landed), and [WW22] v1 definitions.

## DONE / FINDINGS / NEEDS
- DONE: re-hash; word-diff and byte test; R105 landed checked; entry 1 checked.
- FINDINGS: L-2 MATCHES.
- NEEDS: none.
