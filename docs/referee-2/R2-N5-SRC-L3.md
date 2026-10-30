# R2-N5-SRC-L3: word-diff of the P-N5-SRC line, revision L-3 (REFEREE-2 successor 24, Opus 5.5, D15)
- Object: docs/red/P-N5-SRC-line-L3.txt @ l-red 564bef5a, sha1 5736d8ab828d8244c6466abbc08d4fa8d8c03b41 (re-hashed: match).
- Compared with L-2 (sha1 9fcb5790, re-hashed) and with the frozen line (0521fb82, sha1 3101a0c0).

## 1. Frozen line → L-2 (not diffed by me before; checked here): five changes
| change | item | check |
| --- | --- | --- |
| «for S4a, σ_new … H_t)» → «for S4a at a transition k → k + 1, σ_(k+1) … H_k)» | SRC-L2 | ✓ H_k is the line's own («for a state k of F») |
| + «|F| := the number of transitions of F;» | SRC-L1 | ✓ |
| «not events,» → «not source events (unless they change Ξ at a source),» | N-1 | ✓ my wording |
| + «; fixes docs/red/P-N5-SRC-fixes.md entries 1-2» | bookkeeping | ✓ |

## 2. L-2 → L-3 (705 → 746 tokens): four changes, nothing else
| change | item | check |
| --- | --- | --- |
| «n := \|V\|,» → «n := \|V\| (V the vertex set of the game),» | REFEREE SRC-L3 precision | ✓ |
| source-block proof note + «with Case 2 and Case 2b's comparison step by (Lemma ONE-STEP, REFEREE-2 R2-N5-SRC §3.2, claude/referee-2 e8c1b62d; signed by REFEREE, claude/referee 8951ef7c), which closes gap G-SRC-1 (REFEREE R-N5-SRC §3, claude/referee 81f6b89c),» | SRC-L3 (Lead: REQUIRED) | ✓ the right file, section and commits. 8951ef7c holds REFEREE's ONE-STEP signature (R-N5-SETTLE.md Addendum 1 (2)); 81f6b89c holds REFEREE's G-SRC-1 statement and its own closing split (R-N5-SRC §3), which I SIGNED in R2-N5-SRC-C (824651dd) |
| scope tail «… cn3_n9)» → «… cn3_n9; Lemma ONE-STEP is referee-originated)» | L41 | ✓ |
| «entries 1-2)» → «entries 1-3)» | bookkeeping | ✓ |
- Strict symbol test of the changed text: V is now named, and ONE-STEP and G-SRC-1 are cited labels with sources. No free symbol.
- Precision, not required: «by (Lemma ONE-STEP, …)» would read better as «by Lemma ONE-STEP (…)».

## Verdict
L-3 (5736d8ab): **MATCHES** (Opus 5.5, D15). No required change. Every SRC line item of both referees (SRC-L1, SRC-L2, SRC-L3, N-1 and
REFEREE's V) is closed.
