# C3f: confirmation of DTL-proof.md §0 at claude/l-alg 9870b96 and e144992 (CHECKER, 2026-10-16 ~00:45Z)

History: deec040 → 47a8060 (GAP-A-data.md only) → 9870b96 → e144992, a linear history (`git merge-base --is-ancestor` on both
steps), no rewrite. Word-level diffs of docs/alg/DTL-proof.md. Text only.

## Verdict: PASS on both §0 parts; §1.5 resolves N-3 as text
| part | diff | |
| --- | --- | --- |
| (1) 9870b96 vs deec040, DTL-proof.md | exactly one phrase in §0.1 step 0: "starting at 1 or 2" → "starting at 0 if 0 occurs, else at 1 or 2 by parity". This matches pgparser.cpp 498-508 (C3e E-1). No other line of DTL-proof.md changed. The other file in deec040..9870b96 is docs/alg/GAP-A-data.md (from 47a8060, outside the statement) | PASS |
| (2a) e144992 vs 9870b96, §0 | two hunks only. Step 0: "a compression in the sense of TARGET section 1 (order and parity preserved)" → "an order- and parity-preserving renumbering (into {0..2n+2}, not TARGET's {0..n})". 0.4: the renumbering is "an order- and parity-preserving renumbering (priorities ≤ 2n + 2), which is all the argument uses, so it applies to it as well, and to the composition of TARGET's compression with it". Both state exactly what the code does and what the commutation argument needs (C3e N-1). No other §0 line changed | PASS |
| (2b) §1.5 vs C3e N-3 | Lemma 1.5a now asserts that exactly one SCC is reachable from top in a closed sptl region. NOTE N2 is amended to say Pearce's loop "would" extract non-bottom SCCs but, by 1.5a, every extraction is of top's SCC. The paragraph no longer says both things. Code anchors cited in the proof (200-201 attractTangle only at an escape's pop; 329-337 escapes are successors of opponent tangle vertices; 347-379 no-escape = dominion) match dtl.cpp @ 8fbf0a7. Whether Lemma 1.5a is true is for the referees | resolved as text |

## Note (non-blocking)
- Step 0 still ends "0.4 shows A_DTL makes the same choices on a game and on any such compression of it". After the N-1
  rewording, "such compression" should read "such renumbering". The meaning is unambiguous from the sentence before.

## For the Lead
§0 at e144992 contains every fix from C3, C3b, C3d and C3e, and nothing in §0 changed beyond the items checked in those
reports and here. You may re-freeze §0 at e144992 (L26).
