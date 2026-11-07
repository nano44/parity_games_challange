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

## Entry 3 (2026-10-31 20:56Z by date -u; L-NEW successor 43): REFEREE ROOT-L4 / ROOT-L5, CHECKER C109 E-3, Lead reading L43
- REFEREE 21 §C (docs/referee/R-N5-ROOT114.md l. 145-194, claude/referee 74025e44): L-1 «does NOT yet match» (ROOT-L4, ROOT-L5).
- REFEREE-2 25 (docs/referee-2/R2-N5-ROOT114-L1.md, claude/referee-2 83c1838f): «**MATCHES** (Opus 5.5, D15). All my ROOT line items
  are closed.» No new item, so L-2 has nothing to add for REFEREE-2.
### ROOT-L4 (verbatim, l. 171-175)
> - ROOT-L4 (REQUIRED). The scope tail names «DESC-LIN DEAD (L-RED R162); DESC*-LIN DEAD in the weak form (L-RED R163)».
>   - Neither DESC-LIN nor DESC*-LIN is defined in this line, «the weak form» is undefined, and neither DEAD is pinned by commit. P-N5-STAIR
>     L-2 writes «DESC-LIN (DESC_F ≤ c·n) DEAD (L-RED R162, claude/l-red 54832628 …)».
>   - Fix: define both and pin both, e.g. «DESC-LIN (DESC_F ≤ c·n) DEAD (L-RED R162, l-red 54832628)» and «DESC*-LIN (DESC*(F) := min over
>     witness sets U of Σ_(u ∈ U) DESC_F(u) ≤ c·n) …».
### ROOT-L5 (verbatim, l. 176-192, first and last bullets)
> - ROOT-L5 (REQUIRED; the C108 E-1 class, an asymptotic claim stated on finite data). The Lead asked whether «DESC*-LIN DEAD in the weak
>   form (L-RED R163)» overclaims. As worded, it does. I read docs/red/R163-descstar.md at l-red 8150c17e:
[…]
>   - Fix, either:
>     - DATA wording: «DATA: DESC* (as defined) reaches 2.23·n on fbg_K24_m48, with DESC* = (m2 + 1)K + 6 on every computed fbg instance and
>       |F| quadratic there (L-RED R163, l-red 8150c17e)»; or
>     - keep «DEAD» only once L-RED proves the family formula (a proof that DESC* ≥ (m2 + 1)K on fbg for all K, m2).
### CHECKER C109 E-3 (verbatim, docs/checker/C109.md l. 58 and 72-74, claude/checker 178b3e9e)
> ## 6. E-3 (required): the DESC-LIN «DEAD» clause (the Lead's D-2 and D-4)
[…]
> - Move, either of:
>   - (i) drop «DESC-LIN (DESC_F ≤ c·n) DEAD (L-RED R162, claude/l-red 54832628: passive observers, cp_K); ». The reduction does not need it,
>     and the body keeps R162 under Not signed / Data.
### Lead reading L43 (docs/DECISIONS.md l. 369-374), applied clause: «P-N5-ROOT line L-2 drops the DESC-LIN and DESC*-LIN clauses.»
### Repair (line L-2: docs/new/P-N5-ROOT-line-L2.txt)
- Both clauses are DROPPED (C109 E-3 move (i), applied to both; no statement of the line uses them). This closes ROOT-L4 (nothing left to
  define or pin) and ROOT-L5 (no asymptotic DEAD remains).
- The packet body (frozen, f06f493e) keeps R162 / R163 as lane history; it is not edited.
- Kept: «every root descent is a fuel re-route» DEAD (frz32: old-edge relays). It is a universal statement with no constant, killed by
  one instance (packet §1, frz32 old-edge relays), the R95 / R96 kind, not the L43 class. Neither referee flagged it.
- Source note «entries 1-2» → «entries 1-3». Nothing else changes: word-diff vs a41df25b is exactly
  [-DESC-LIN DEAD (L-RED R162); DESC*-LIN DEAD in the weak form (L-RED R163);-] and [-1-2)-]{+1-3)+}; 837 → 825 words.

## Entry 4 (2026-10-31 23:14Z by date -u; L-NEW successor 43): Lead pre-check flags F-1, F-2, F-3 (docs/agents/R100-draft.md, trunk 634c823a)
- R98 (P-N5-ODD) and R99 (P-N5-STAIR) have LANDED (Lead 23:15Z: trunk 96b0207b, RESULTS l. 8296 and l. 8596). The Lead asked for
  L-3 = L-2 + exactly F-1, F-2 and F-3.
### F-1 (verbatim, R100-draft l. 8-20)
> - FLAG F-1, STALE PINS INSIDE THE LINE (the C106 E-1 class, a superseded revision cited as current; in the line, not in the body). L-2 cites
>   «P-N5-STAIR (Lemma COPY in both directions and Theorem STAIR, as in its line L-2: l-new 6903f1b3, docs/new/P-N5-STAIR-line-L2.txt, sha1
>   44f56e96d41d45653c4b7bc2f140c587e8e407e6)» and «β, first-difference positions, descents and DESC_F as in P-N5-STAIR's line L-2». STAIR
>   L-2 is the line CHECKER C109 FAILED (178b3e9e); R99 lands STAIR line L-3 (9db0b169, l-new 7dc1eb7c; both referees MATCH). L-2 also cites
>   «P-N5-ODD (Corollary FUEL-COUNT: l-si 0afc0d70a, docs/si/P-N5-ODD-box57.md §6, sha1 03eec41d, with its fixes entries 1-2)»; R98 lands
>   ODD line L-3 (f83b169e, l-si 2f8e5b2e) with fixes F0 + entries 1-6. The CONTENT ROOT imports is unchanged: STAIR L-2 → L-3 touches only
>   the R57 gloss, the DESC-LIN clause, the L41 clause and the entries count (R99-draft (R)); ODD fixes entries 3-6 are line revisions, the
>   D-ODD-1 DATA defect, the (y, z) binder of FUEL-COUNT (ODD-L5) and the DATA clause. But the fix both referees wrote says what to cite once
>   the premises land: REFEREE ROOT-L2 «Fix: cite each by its landed RESULTS label once it lands; until then, by commit and sha1»; REFEREE-2
>   ROOT114-L2 «cite line L-2 (l-new 6903f1b3, sha1 44f56e96), or R-number once landed» and P-4 «cite P-N5-ODD by its landed R-number (R98
>   draft at C108) or its current line, once landed», «optional; Lead decides». R100 lands after R98 and R99, so at landing the line cites by
>   commit what RESULTS then holds as R98 / R99. CHECKER decides: accept the commit pins (content-identical; checked in (5)), or a line L-3
>   citing RESULTS R99 (Lemma COPY, Theorem STAIR; β and descents) and RESULTS R98 (Corollary FUEL-COUNT).
### F-2 (verbatim, R100-draft l. 21-30)
> - FLAG F-2, L41 (the C109 E-1 class; contested). L-2 has 0 «referee-originated». REFEREE-2 says none is needed: R2-N5-ROOT114.md l. 177
>   «There is no referee-originated proof (L41), so no «referee-originated» tag is needed.», L1 l. 45 «no referee-originated proof (L41 tag
>   not needed)»; REFEREE is silent. That is true of THIS packet's own proof text: F0 and both reports record no gap and no repair of a proof.
>   But three proofs rest on referee-originated text of the premise packets: DESC-ROOT applies «[COPY] (both directions)» (packet l. 63),
>   i.e. COPY's converse, whose proof is G-ST-1 = P-1 (the clause R99's line L-3 adds for DESC-COPY under C109 E-1); ORIGIN-NEW's Φ step is
>   «as in [COPY]'s proof (G-ST-1)» (packet l. 97; REFEREE §4 l. 63 «as in G-ST-1»); FUEL-ROOT-STAIR uses FUEL-COUNT, whose proof carries
>   the referee-originated repair G-ODD-2 (R98's title: «the proofs of FUEL-LEX and FUEL-COUNT carry referee-originated repairs»). C109 E-1
>   was a same-packet use («DESC-COPY needs COPY's converse»); here the use is through a cited premise whose own landing line carries the
>   clause, while the pin in L-2 is STAIR L-2, which does not (C109 l. 42 «L-2 contains «referee-originated» 0 times.»). CHECKER decides
>   whether L41 reaches through a premise; if yes, a line L-3 adds a tail clause naming G-ST-1 = P-1 and G-ODD-2.
### F-3 (verbatim, R100-draft l. 31-34)
> - FLAG F-3, «root descent» UNDEFINED (the C109 E-2 class). The tail's DEAD clause reads «every root descent is a fuel re-route»; «root
>   descent» occurs once in L-2 and is defined nowhere in it. L-2 defines descents «of type R» and uses «R-descent» (twice). REFEREE's L-2
>   addendum reads the clause as R-descents (l. 202 «every R-descent of every W-run is a fuel re-route»; l. 203 «its terms (R-descent, fuel
>   re-route) are defined in the line»), REFEREE-2 L2 l. 12 «No free symbol». A one-token move «root descent» → «R-descent» would close it.
### Repairs (line L-3: docs/new/P-N5-ROOT-line-L3.txt)
- F-1. Both commit pins are replaced by the landed labels: «P-N5-STAIR (Lemma COPY … as in its line L-2: l-new 6903f1b3, …, sha1 44f56e96…)»
  becomes «RESULTS R99 (P-N5-STAIR: Lemma COPY in both directions and Theorem STAIR)», and «β, first-difference positions, descents and
  DESC_F as in P-N5-STAIR's line L-2» becomes «… as in RESULTS R99». «P-N5-ODD (Corollary FUEL-COUNT: l-si 0afc0d70a, …, with its fixes
  entries 1-2)» becomes «RESULTS R98 (P-N5-ODD: Corollary FUEL-COUNT)».
  - Not changed: «a FUEL RE-ROUTE of (y, z) at k is as in P-N5-ODD §6 (…)». The definition is written out in full in the line, and the
    section reference is not a commit pin. The Lead decides if it should read «RESULTS R98».
- F-2 (L41, through the premises). New tail clause: «the proof of DESC-ROOT uses COPY's converse, whose proof is referee-originated
  (RESULTS R99: G-ST-1 = P-1), the proof of ORIGIN-NEW uses a step of that proof, and the proof of FUEL-ROOT-STAIR uses FUEL-COUNT,
  whose proof carries referee-originated repairs (RESULTS R98: G-ODD-1, G-ODD-2);».
  - Grounds: packet l. 63 («Apply [COPY] (both directions)», DESC-ROOT) and l. 97 («as in [COPY]'s proof (G-ST-1)», ORIGIN-NEW). The
    wording follows R99's own clause («the proof of DESC-COPY uses COPY's converse, whose proof is referee-originated (G-ST-1 = P-1 …)»)
    and R98's («the proofs of FUEL-LEX and FUEL-COUNT carry referee-originated repairs (G-ODD-1 …; G-ODD-2 = N-ODD-2 …)»).
  - Precision against the Lead's wording («DESC-ROOT and ORIGIN-NEW use COPY's converse»): ORIGIN-NEW does not apply the converse; it
    reuses one step of its proof (y lies in neither path set), so the clause says «uses a step of that proof».
- F-3. «every root descent is a fuel re-route» → «every R-descent is a fuel re-route» (the line defines R-descents; REFEREE's L-2
  addendum already read it so).
- Source note «entries 1-3» → «entries 1-4». Nothing else changes.
