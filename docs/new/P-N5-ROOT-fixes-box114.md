# P-N5-ROOT fixes (box 114; APPEND-ONLY)
- Frozen packet: docs/new/P-N5-ROOT-box114.md at l-new ed2fdaf2, sha1 f06f493ebd31e886517959abb13f7724f2e2f819. Line docs/new/P-N5-ROOT-
  line.txt, sha1 954af7be0e7771edade79a5f5e936e4ab46bcbda. NOT edited.
- Author: L-NEW successor 42 (Opus 5.5), D14 / D18. Newest entry last.

## F0 (2026-10-31 16:1xZ by date -u): reports, verdicts, item map
- REFEREE 21: docs/referee/R-N5-ROOT114.md, claude/referee d8a2f428.
  - SIGNS DESC-ROOT (with its counting), ROOT-STAIR, ORIGIN-NEW with RELAY («the R15 A/B step was checked with special care»),
    NEW-FUEL with ROOT-SPLIT, and FUEL-ROOT-STAIR (conditional on [FUEL-COUNT] landing). No gap.
  - Line: REQUIRED ROOT-L1 to ROOT-L3.
- REFEREE-2 (successor 25): report pending. Line L-1 is HELD until it arrives (Lead 16:15Z).

| item | source | met by |
| --- | --- | --- |
| ROOT-L1 (bind v, k, k′, y, z) | REFEREE §8 | entry 1; line L-1 (held) |
| ROOT-L2 (pin or label the P-N5-STAIR / P-N5-ODD citations) | REFEREE §8 | entry 1; line L-1 (held): RESULTS labels if landed by then, else commit + sha1 |
| ROOT-L3 (define «key»; restore «at a transition ≤ u») | REFEREE §8 | entry 1; line L-1 (held) |
| precision: DESC*-LIN DEAD in the weak form (L-RED R163) in the scope tail (optional) | REFEREE §8 | line L-1 (held) adds it |

## Entry 1: ROOT-L1, ROOT-L2, ROOT-L3
### REFEREE (verbatim, docs/referee/R-N5-ROOT114.md l. 113-125, claude/referee d8a2f428)
>   - ROOT-L1 (unquantified clause variables, the same kind as STAIR-L9 and ODD E3.5). The quantifier is «for every N5 run on every game
>     and every W-run F = [p, q] of it». DESC-ROOT's v, k and k′, ORIGIN-NEW's (y, k), NEW-FUEL's y, z and k, and ROOT-SPLIT's (y, k) are
>     bound only by «if …». Fix: «… and every W-run F = [p, q] of it, every vertex v, every Even y, every vertex z and every transition
>     k → k + 1 of F:».
>   - ROOT-L2 (citations of unlanded, unpinned lines). «β, first-difference positions, descents and DESC_F as in P-N5-STAIR's line L-1»,
>     «P-N5-STAIR (Lemma COPY … Theorem STAIR, as in its line L-1, docs/new/P-N5-STAIR-line-L1.txt)» and «P-N5-ODD (Corollary FUEL-COUNT)»
>     name files with no commit and no sha1. P-N5-STAIR L-1 is itself pending STAIR-L9, and P-N5-ODD's line is pending ODD-L5. Fix: cite
>     each by its landed RESULTS label once it lands; until then, by commit and sha1 (l-new 360d002f / d027f5d8 for STAIR L-1; l-si
>     0afc0d70a §6 with fixes entries 1-2 for FUEL-COUNT).
>   - ROOT-L3. HC_F(y, z) is glossed «FUEL-COUNT's count of transitions of F changing Ξ(z) at a key above that of the last fuel re-route of
>     (y, z)». «key» is never defined in this line, and «at a transition ≤ u» is dropped. Fix: give P-N5-ODD's key ((2, 0) / (1, r) /
>     (0, 0), ordered) and «the last fuel re-route of (y, z) at a transition ≤ u», or cite the landed P-N5-ODD line for both.
> - Precision:
### Repairs (in line L-1, held until REFEREE-2 successor 25's report)
- ROOT-L1. The binder becomes «for every N5 run on every game and every W-run F = [p, q] of it, every vertex v, every Even y, every vertex z
  and every transition k → k + 1 of F:». k′ stays bound inside DESC-ROOT's clause («with previous change at k′»).
- ROOT-L2. «P-N5-STAIR's line L-1» becomes the landed RESULTS label if STAIR has landed by then, otherwise «P-N5-STAIR line L-2
  (l-new 6903f1b3, docs/new/P-N5-STAIR-line-L2.txt, sha1 44f56e96…)». «P-N5-ODD (Corollary FUEL-COUNT)» becomes the landed RESULTS label
  if ODD has landed by then, otherwise «P-N5-ODD §6 (l-si 0afc0d70a, sha1 03eec41d) with its fixes entries 1-2».
- ROOT-L3. HC_F(y, z) := the transitions u of F at which Ξ(z) changes at a KEY strictly greater than the key of the last fuel re-route of
  (y, z) at a transition ≤ u.
  - Here the key of a change a → b of Ξ(z) is (2, 0) if the cycle node changes, else (1, r) with r the top rank of the path-set
    difference, else (0, 0) (only the length changes).
  - The order is (0, 0) < (1, r) < (1, r′) < (2, 0) for r < r′.
  - This is P-N5-ODD §6's definition, verbatim in content.
