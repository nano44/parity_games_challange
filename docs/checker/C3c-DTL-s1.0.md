# C3c: re-read of DTL-proof.md §1.0 (and the dependent rewordings) at claude/l-alg e916b24 (CHECKER, 2026-10-15 ~18:10Z)

Scope (Lead 18:08Z):
- §1.0 against C3b's R-1..R-3 (checker cf3e0d2).
- Whether the reworded §1.2 start-site list, §1.6 candidate note and §2.3 K5(ii)/K6 follow from the corrected §1.0.

§0 is frozen at ccff864 (L24) and was not re-read. Code: Oink 8fbf0a7, dtl.cpp. Text only, no re-runs. No judgement on
the mathematics beyond what the code shows.

## Verdict: PASS (notes N-1..N-4, none blocking)
| item | verdict |
| --- | --- |
| R-1 (s3) self-loop of a candidate | FIXED |
| R-2 (s4) str self-assignment outside sptl | FIXED (N-2) |
| R-3 (s2) singleton extraction | FIXED |
| §1.2 start sites | follows from (s4) |
| §1.6 candidate note | follows from (s3) (N-1) |
| §2.3 K5(ii) looped opponent top | follows from (s2) for the extraction. "So it is productive" needs one more sentence (N-3) |
| §2.3 K6 looped τ_k | follows from (s2), (s3) |

## R-1..R-3
- R-1, (s3). Now reads: every vertex of V lies in Reg ⊆ A_t, so a candidate's self-loop is a successor in Z.
  - Checked against attracts (40-57) and best_vertices 690-716: every V-vertex is a region top (`CurZ[top] = true`) or
    already in Z (`!Z[top]`), and `Z |= CurZ`.
  - A p-owned V-vertex with a loop is never a candidate (43-46).
  - An opponent-owned V-vertex with a loop is a candidate iff it has a successor in R \ Z (49-55).
  FIXED.
- R-2, (s4). Now distinguishes inside and outside sptl.
  - Inside sptl (481-496), str is set per region at the push (89 or 171), or at the top's own pop through 73 when the
    top has a loop.
  - Outside sptl, the search_rec scan at 899-911 sets str = -1 (908), and line 73 gives str[u] = u for p-owned u with
    a loop. The same holds at 881/965/694.
  - Checked:
    - extractTangles is called only from sptl (539).
    - Every vertex of an sptl region is pushed in that region, so its str is written there before 539.
    - dom_vector records str at extraction (364-367).
    - The removal attractor (1032-1038) writes str only through 89 and 171.
  - So the outside-sptl self-assignments are never read by extraction and never output. FIXED (N-2).
- R-3, (s2). Now: {u} is extracted by 317 iff u has no successor in Z other than itself; otherwise u's SCC in the
  restricted graph (234-266) contains that successor. Matches 234-266 and 315-317. FIXED.

## Dependent rewordings
- §1.2 "Strategy assignment" now lists 908 (search_rec's -1 branch, either owner) with the self-loop case. Consistent
  with (s4) and with lines 73 and 905-911.
- §1.6: "a self-loop of v counts as a successor in Reg because v ∈ Reg, 1.0 (s3)". Consistent.
- §2.3 K6: "with all other successors in X it is pruned unless it has a self-loop (1.0 (s3)), and then {τ_k} is extracted
  by 317 with escapes in X — covered by (β') below or new".
  - (s3): X vertices are removed from R (885/920/969), so attracts ignores them. With the loop, hasZ is true and no
    successor lies in R \ Z, so τ_k is not a candidate and survives.
  - (s2): the region is closed with no other successor in Z, so 317 applies.
  - The duplicate case is routed to (β'). Consistent.
- §2.3 K5(ii): "with a self-loop it is not attracted (1.0 (s2)) but then its closed region {τ} is extracted by 317 (1.0
  (s2)), so it is productive".
  - The extraction follows from (s2): all other successors are in higher regions, so none lie in Z, and the region is
    closed (519-525).
  - "Productive" does not follow from §1.0 alone. An extracted SCC can be a duplicate of a stored tangle and be
    discarded (385-424, §1.5), and extraction happens only if `!W[top]` (528).
  - See N-3.

## Notes
- N-1. (s3) says an opponent-owned looped candidate "is cleared at threshold t iff it has no successor in R \ A_t".
  The code also requires t < pr(u) (737 breaks at the first candidate with pr(u) ≤ t). §1.6 states this correctly; add
  "for some t < pr(u)" to (s3) for consistency.
- N-2. (s4)'s "solved vertices get str at 1027 and 89 on the removal attractor" omits 171: attractTangles at 1037 writes
  tangle strategies. Those strategies were written in sptl regions, so the conclusion (no outside-sptl value is output)
  stands. Add 171.
- N-3. K5(ii)'s "so it is productive" needs the duplicate case excluded. A stored singleton tangle {τ} with all escapes
  in higher regions might already have been pulled into a higher region by rule (T).
  - Rule (T) needs: one escape in the current Z, the others in Z or outside Gx = the consumed copy (152-158), and
    tpr ≤ threshold (140).
  - In that case τ would have no region. State that sentence, or route the duplicate to (β') as K6 does.
  - This is a proof step, not a reading error; I do not judge it.
- N-4. (s2) "contains that successor's reachable part" is loose. The SCC contains the successor because the successor
  reaches u inside Z (it was attracted toward u), not "its reachable part". Wording only.

## Conclusion
§1.0 now matches dtl.cpp @ 8fbf0a7 at every cited line I checked (40-57, 73, 78-90, 171, 234-266, 315-317, 481-496,
519-529, 539, 690-716, 737, 899-911, 1023-1038). The three C3b reading errors are corrected. The dependent rewordings
follow from it, except the one-sentence gap N-3 in K5(ii).
