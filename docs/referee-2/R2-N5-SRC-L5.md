# R2-N5-SRC-L5: word-diff of the P-N5-SRC line, revision L-5 (REFEREE-2 successor 24, Opus 5.5, D15)
- Object: docs/red/P-N5-SRC-line-L5.txt @ l-red a5340f2d, sha1 2b39581d367687ec41067d690e448541f2ac7678 (re-hashed: match).
- Compared with L-4 (1edc2f0e, sha1 ec2c7139; R2-N5-SRC-L4.md, 5e81fc5c). Written without opening REFEREE's verdict.

## 1. Diff (difflib over whitespace tokens, 744 → 756 tokens): three changes, nothing else
| change | item | check |
| --- | --- | --- |
| «DATA: they are not O(1) per W-run» → «DATA: they repeat within one W-run» | SRC-L5 | ✓ my fix verbatim. The asymptotic claim is gone |
| «(pins xcn4_n12, cn3_n9);» → «(xcn4_n12: 4 σ̄-flips at one own Ξ-cycle node; cn3_n9: 3 switches at one c ∈ C);» | SRC-L5 | ✓ the counts, see §2 |
| «entries 1-4)» → «entries 1-5)» | bookkeeping | ✓ |
This equals the Lead's tr/diff list.

## 2. The two counts, recounted with my own code
- Tool: docs/referee-2/R2-N5-SRC/pincount.py, my LATEP state loop; lane xcn.py is not imported. Pins are taken from 0521fb82.
- cn3_n9: one W-run F = [0, 3], |F| 3, CN {1: 3}. «3 switches at one c ∈ C» ✓, equal to the lane's «CN {1: 3}».
- xcn4_n12: one W-run F = [0, 4], |F| 4. Odd vertex 0 has σ̄(0) = 6, 3, 10, 6, 3 at states 0-4, so it flips at all 4 transitions.
  λ_Ξ(0) = 7 at state 0 and 0 at states 1-4.
  - Counting flips with λ_Ξ(o) = o at k OR at k + 1 (the lane's XCN, xcn.py @ a5340f2d l. 5) gives 4, equal to the lane's «XCN {0: 4}». ✓
  - Counting flips with λ_Ξ(o) = o at k AND at k + 1 (packet F2's form, and my first count) gives 3. The first flip (0 → 1) is the one at
    which 0 becomes its own node.
- «they repeat within one W-run» holds under both readings (3 or 4 ≥ 2).
- P-1 (precision, optional). The line does not define «own Ξ-cycle node» for a flip, and the number 4 depends on the reading. Two
  options:
  - «xcn4_n12: 4 σ̄-flips at one Odd vertex, its own Ξ-cycle node at one end of each»;
  - or «3 σ̄-flips at one own Ξ-cycle node» (F2's form).
  Either is exact. As written, 4 is right under the lane's stated definition.

## 3. Remaining overclaims (scope tail and claims, re-read in full)
- «no count is bounded here; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim»: ✓, consistent with the claims.
- «… are not source events (unless they change Ξ at a source)»: definitional. ✓
- The EQUIVALENCE is stated with «for every family of games … over all W-runs F», as proved. ✓
- «m_C … (≤ m_E)»: trivially true. ✓
- No other asymptotic or data word (O(·), unbounded, linear, «not O(1)») remains. None found.

## Verdict
L-5 (2b39581d): **MATCHES** (Opus 5.5, D15). No required change. SRC-L5 is CLOSED. P-1 is optional.
