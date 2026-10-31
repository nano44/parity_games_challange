# R2-N5-SRC-L4: word-diff of the P-N5-SRC line, revision L-4 (REFEREE-2 successor 24, Opus 5.5, D15)
- Object: docs/red/P-N5-SRC-line-L4.txt @ l-red 1edc2f0e, sha1 ec2c713989eb3075060247b714eb49a5b2abf875 (re-hashed: match).
- Compared with L-3 (564bef5a, sha1 5736d8ab; MATCHES in R2-N5-SRC-L3.md, b441f3da). Fixes: docs/red/P-N5-SRC-fixes.md Entry 4 at
  1edc2f0e.
- Written without opening REFEREE's verdict on L-4.

## (1) Word-diff L-3 → L-4 (difflib over whitespace tokens, 746 → 744 tokens): five token changes, nothing else
| change | entry | check |
| --- | --- | --- |
| «RESULTS line L-2, l-si 86becaa0)» → «RESULTS R96)» | E4.1 | ✓ see (2) |
| «source), and» → «source); DATA: they» | E4.2 | ✓ see (3) |
| «W-run: pins» → «W-run (pins» | E4.2 | ✓ |
| «cn3_n9;» → «cn3_n9);» | E4.2 | ✓ |
| «entries 1-3)» → «entries 1-4)» | bookkeeping | ✓ |
These are exactly the token changes Entry 4 lists. No symbol is added or removed.

## (2) The R96 citation, against docs/RESULTS.md on trunk
- Trunk 38bb8320 is an ancestor of origin/claude/vibrant-johnson-nxvvxo. docs/RESULTS.md l. 7748 there is «### R96 [refereed-only] N5 on
  EVERY game …», the only R96 heading.
- With the heading «### R96 [refereed-only] » and the «, CHECKER PASS (…)» fill stripped, it equals the SETTLE line L-5 (l-si ce7bdc3b,
  sha1 39e44fe2, which I found MATCHES, 0f864f7a) token for token: 868 = 868 tokens, 0 differences.
- So R96 contains the RUN-SETTLE induction with «Cases 2, 2b via Lemma ONE-STEP», G-SRC-1, and «Lemma ONE-STEP (Cases 2, 2b) is
  referee-originated». It is the right object for «P-N5-SETTLE's RUN-SETTLE induction … signed; RESULTS R96».
- The landed entry carries the ONE-STEP repair that SRC's own clause also cites, so the citation is consistent. ✓

## (3) The DATA relabel
- The split is right. «σ̄-changes, switches at C and σ̄-changes at own Ξ-cycle nodes are not source events (unless they change Ξ at a
  source)» follows from the definition of a source event, so it stays a statement. Only the count claim is relabelled DATA. ✓
- **SRC-L5 (REQUIRED; present since the frozen line, missed by me in L-3).** The DATA clause reads «they are not O(1) per W-run (pins
  xcn4_n12, cn3_n9)».
  - «not O(1)» is an asymptotic claim: no constant bounds the count over all W-runs.
  - Two fixed instances, with counts 4 and 3, cannot support it. A constant-size pin is consistent with an O(1) bound.
  - The lane's own note says what was observed: R147-xcn.md @ 1edc2f0e l. 1 «XCN and CN do repeat in one W-run (4 and 3 at one vertex,
    n ≤ 12). No super-linear family was built.» It uses «not O(1)» to mean «more than one per vertex» (l. 25, 147).
  - A DATA label does not cure an overclaim.
  - Fix (minimal): «DATA: they repeat within one W-run (xcn4_n12: 4 σ̄-flips at one own Ξ-cycle node; cn3_n9: 3 switches at one c ∈ C)».
  - Or drop the clause. The reduction does not need it.

## Verdict (Opus 5.5, D15)
- L-4 (ec2c7139) applies Entry 4 exactly. The R96 citation is right, and the DATA split is right.
- **DOES NOT MATCH as a landing line: one REQUIRED change, SRC-L5** (the «not O(1)» wording, pre-existing).
- Correction (my side): my L-3 MATCHES (b441f3da) and my SRC report §6 passed this clause. I missed it there.
