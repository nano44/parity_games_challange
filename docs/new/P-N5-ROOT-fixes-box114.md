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


## Entry 2 (2026-10-31 19:3xZ by date -u): REFEREE-2 successor 25 (docs/referee-2/R2-N5-ROOT114.md, claude/referee-2 d1c493fb)
- REFEREE-2 SIGNS every item, with no packet gap. ORIGIN-NEW's R15 A / B step is sound (it is landed R91 Lemma OPT-OFF).
- Line REQUIRED: ROOT114-L1 (bind k) and ROOT114-L2 (cite STAIR line L-2). Optional: P-1, P-2, P-3.
### ROOT114-L1 (verbatim, l. 41-61), with the boundary counterexample
> ### ROOT114-L1 (REQUIRED): bind k
> - Line text: «a ROOT CHANGE is a pair (y, k) with y switching at k and W(y) changing at k …; (Lemma ORIGIN-NEW) if (y, k) is an origin root change
>   and k − 1 ∈ F, then (y, σ_(k+1)(y)) ∉ H_(k−1); … (Corollary ROOT-SPLIT) every root change (y, k) with k − 1 ∈ F is a fuel re-route or a
>   relay entering by an edge of H_(k−1)».
> - Here F = [p, q] is a set of states. With k = q, the state k − 1 = q − 1 lies in F, but the transition q → q + 1 is not a transition of F.
>   It is the cut: an S4c fallback, a λ_W change, or a τ change.
> - The proof needs k → k + 1 in F three times: W-MON (W_(k+1) ⊵ W_k), C fixed at k + 1, and λ_W(y) fixed at k + 1.
> - Counterexample: experiments/new/box113/inst/w_re3_1.pg (sha1 c59735b4…) with its start w_re3_1.start (3614ad94…), at l-new ed2fdaf2.
>   - The W-run is F = [2, 6]. Transition 6 → 7 is an S4c fallback (τ unchanged, λ_W unchanged).
>   - k = 6, y = 12, z = 29: σ_5(12) = σ_6(12) = 22 and σ_7(12) = 29.
>   - W(12): (11, 201465856, 4) → (11, 218234880, 4), a change. W(29) = (11, 218103808, 3) at states 5, 6 and 7, so the root change is an origin.
>   - k − 1 = 5 ∈ F, and (12, 29) ∈ H_5.
>   - So ORIGIN-NEW as worded fails. ROOT-SPLIT as worded fails too: the change is not a fuel re-route (the edge is old) and not a relay.
>   - Evidence: docs/referee-2/R2-N5-ROOT114/bnd.py, logs/bnd_w_re3_1.txt, and pins.txt (lines «EX BND_ONEW_FAILS_fb … w_re3_1 …@6»).
> - Size of the problem: there are 2,977 such boundary origins with an old edge on the corpus (logs/corpus_totals.txt: BND_ONEW_FAILS_fb
>   2,394, BND_ONEW_FAILS_lamW 583) and 42 on the pins.
> - Fix (wording only; the packet's proofs are unchanged): define a root change as a pair (y, k) with k → k + 1 a transition of F, y switching at k
>   and W(y) changing at k. Equivalently, write «if k → k + 1 is a transition of F, k − 1 ∈ F and (y, k) is an origin root change» in
>   ORIGIN-NEW, and «every root change (y, k) at a transition k → k + 1 of F with k − 1 ∈ F» in ROOT-SPLIT.
> - The packet itself should say the same in §4. Its §1 («every transition is an S4a step») is the reading under which I sign.
> 
### Repairs in line L-1 (docs/new/P-N5-ROOT-line-L1.txt)
- ROOT114-L1 (= REFEREE ROOT-L1):
  - the binder quantifies «every transition k → k + 1 of F»;
  - a ROOT CHANGE is defined as a pair (y, k) «with k → k + 1 a transition of F»;
  - ROOT-SPLIT reads «if (y, k) is a root change and k − 1 ∈ F, then …», so k is not re-quantified.
  - The boundary case k = q (w_re3_1, F = [2, 6], 6 → 7 an S4c fallback; 2,977 corpus cases) is outside the line.
  - The packet's proofs are unchanged. Its §1 («every transition is an S4a step», k → k + 1 a transition of F) is the reading both
    referees signed. Packet §4 should be read with «k → k + 1 a transition of F», as REFEREE-2 asks.
- ROOT114-L2: the line cites «P-N5-STAIR … as in its line L-2: l-new 6903f1b3, docs/new/P-N5-STAIR-line-L2.txt, sha1 44f56e96…» and
  «… DESC_F as in P-N5-STAIR's line L-2». Neither STAIR nor ODD has landed, so the pins stay commit + sha1. ODD is cited as the packet
  (l-si 0afc0d70a, sha1 03eec41d) with its fixes entries 1-2.
- P-3 (= REFEREE ROOT-L3): «the last fuel re-route of (y, z) at a transition ≤ u» is restored, and the key is defined (entry 1).
- P-1: no change needed. NEW-FUEL is true even with k unbound, and the binder covers it either way.
- P-2 (cite R91 OPT-OFF for ORIGIN-NEW's first step): recorded here. The line's premise list cites R15 (a), (b) and [1E-N3], which give
  OPT-OFF's content.
