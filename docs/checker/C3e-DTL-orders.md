# C3e: re-diff of DTL-proof.md §0 at claude/l-alg deec040 (CHECKER, 2026-10-16 ~00:40Z)

Diff: §0 at deec040 against 37bbe2f (the C3d target), word-level. History: 37bbe2f is an ancestor of deec040; the
commits after it are f2704d7 (GAP-A, outside §0), 4cd8ca4 (C3d fixes) and deec040 (two "1125" → "1126"). No rewrite.
Code: Oink 8fbf0a7. Statement text only, no re-runs.

## Verdict: FAIL, one factual error (a one-phrase fix); everything else PASS
| C3d item | at deec040 | |
| --- | --- | --- |
| F-1 D1 for every ω | 0.2: "every order datum ω (0.1)" in the A_DTL sentence and "for every order datum ω" in the A_IDTL sentence | FIXED |
| O3 citation | "pgparser.cpp 441-457, the parser the pinned command uses, solve.cpp:263". The `for (;;)` successor loop of `parse_pgsolver_renumber` starts at 441 | FIXED |
| O4 | "(sorted, dtl.cpp 389)" | FIXED |
| O8 | "(1111, 1119; idtl 1126)" and 0.3(d) "(1126, ...)" | FIXED |
| O7 | "the tin iteration order O7" listed among the free data | FIXED |
| NF-1 renumbering named in step 0 | named, cited 492-511, "whatever the flags", O(n log n) charged in D2(e), and a composition sentence added to 0.4 | FIXED, except **E-1** below |
| N-2 §1.5 | §1.5 now says the SCCs are processed "in the order O3'" (Oink: Pearce, reverse topological) and that no argument uses the order | TAKEN (note N-3) |
| nothing else in §0 moved | the word diff shows only the places above, plus the threshold bound in D2(e) "≤ 2n + 2 after step 0's renumbering" (was "≤ n + 1 after compression"), which follows from NF-1 | CONFIRMED |

## E-1 (FAIL): "starting at 1 or 2" is false for games containing priority 0
§0.1 step 0 says the distinct priorities are mapped "in increasing order to consecutive integers starting at 1 or 2".
The code (pgparser.cpp 498-508):
- `counter = 0; previous = 0;`
- for each distinct priority p, increasing: `if (previous != p) { counter++; if ((counter&1) != (p&1)) counter++; previous = p; }`, then `map[p] = counter`.
- When the least priority is 0, `previous != p` is false, so 0 maps to 0. Otherwise the least priority maps to 1 (odd)
  or 2 (even).

A transcription of these lines (CHECKER scratch, not committed) gives:
- {0,1,2} → {0,1,2};
- {0,2,4} → {0,2,4};
- {3,5,7} → {1,3,5};
- {4} → {2};
- {0,3} → {0,1}.

Fix: "starting at 0 (if 0 occurs), else 1 or 2 by parity".
- The stated bound "≤ 2d ≤ 2n + 2" still holds: the first value is ≤ 2 and each next one adds 1 or 2.
- Nothing else in §0 depends on the starting value.
- TARGET priorities lie in {0..n}, so priority 0 is the common case. The sentence is wrong exactly in the usual
  situation, which is why I do not pass it as a note.

## Notes (non-blocking)
- N-1. "this is a compression in the sense of TARGET section 1 (order and parity preserved)". TARGET §1's compression
  maps into {0..n}; the parser's map goes into {0..2n+2}. The parenthesis gives the property the argument uses (order
  and parity), so 0.4's commutation applies, but "in the sense of TARGET" slightly overstates. Suggest "an order- and
  parity-preserving relabelling (TARGET §1's compression is another)".
- N-2. 0.1's leftover range citation "(1125-1138)" for the interleaved block is correct: 1125 is the `while (true) {`
  that opens it. The two counter citations are now 1126.
- N-3 (§1.5, outside §0). The new sentence "in a closed region every vertex reaches top, so the reachable SCCs are exactly
  one, the SCC of top" contradicts NOTE N2 in the same paragraph ("non-bottom SCCs are extracted too"). If the new
  sentence holds, N2 is vacuous; if N2 can happen, the new sentence is false.
  - This is a proof claim, not a statement claim. I do not judge which is right.
  - The paragraph must not say both. Route it to L-ALG before referees read §1.5.

## For the Lead
- With E-1 fixed (one phrase), §0 at deec040 + that fix passes. Nothing else in §0 needs to change for an L26 re-freeze.
- If the fix lands as a single commit touching only that phrase, a blob-level diff is enough for me to confirm.
