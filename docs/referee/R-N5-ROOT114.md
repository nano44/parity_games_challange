# R-N5-ROOT114: REFEREE report on packet P-N5-ROOT (L-NEW box 114): DESC-ROOT, ROOT-STAIR, ORIGIN-NEW (+ RELAY), NEW-FUEL + ROOT-SPLIT, FUEL-ROOT-STAIR
Referee: REFEREE (successor 21), Opus 5.5 (D15). Lead brief 2026-10-31 15:17Z. REFEREE-2 reviews independently.
- Object and pin: docs/new/P-N5-ROOT-box114.md at claude/l-new ed2fdaf2. `git show ed2fdaf2:<path> | sha1sum` =
  f06f493ebd31e886517959abb13f7724f2e2f819 (158 lines). The line docs/new/P-N5-ROOT-line.txt has sha1
  954af7be0e7771edade79a5f5e936e4ab46bcbda. Both equal the Lead's figures.
- File name: docs/referee/R-N5-ROOT.md is my predecessors' report on an EARLIER packet also called P-N5-ROOT (619fccf2), so this report
  is R-N5-ROOT114.md (box 114). Its tools are root114_probe.py and root114_logs/.
- Independence: I opened no docs/referee-2/ file for this packet.
- Scope (D1): REDUCTIONS and EQUIVALENCES inside W-runs. No count is bounded. G-N5-TIME stays OPEN. Not a TARGET.md claim.
- Premise status: [COPY], [STAIR] (P-N5-STAIR) and [FUEL-COUNT] (P-N5-ODD) are signed by both referees, but neither line has landed.
  P-N5-STAIR L-1 still needs STAIR-L9 and P-N5-ODD L-1 still needs ODD-L5 (my §Cs). So this packet's results are conditional on those
  two landings.
- Every verdict below is labelled (Opus 5.5, D15).

## Verdicts
| § | item | verdict |
| --- | --- | --- |
| 1 | premises | CHECKED: R15 (a), (b), (d) at l. 624 (Lemma B's text is «every (v, w) ∈ I is a length-only switch at a cycle node: Λσ(v) = v»); R57 1E-N3; R91 W-MON; R93 (a) LEX; [COPY] / [STAIR] as signed; [FUEL-COUNT] as signed with fixes entries 1-2 |
| 2 | Lemma DESC-ROOT, with its counting (DESC_F ≤ n(R + T + S), T_F ≤ TS_F) | SIGNED |
| 3 | Theorem ROOT-STAIR (equivalence) | SIGNED |
| 4 | Lemma ORIGIN-NEW; Corollary RELAY | SIGNED. The R15 A/B step was checked with special care (§4) |
| 5 | Lemma NEW-FUEL; Corollary ROOT-SPLIT | SIGNED |
| 6 | Corollary FUEL-ROOT-STAIR | SIGNED (conditional on [FUEL-COUNT] landing) |
| 7-8 | DEADs, DATA, READING | not to sign. The pins re-run and agree (§7) |
| — | RESULTS line (954af7be) | REQUIRED CHANGES ROOT-L1 to ROOT-L3 (§8) |

## 2. DESC-ROOT
- The walk follows v's (σ_(k+1), τ)-play. v changes, so v ∉ C. The play reaches λ_W(v) ∈ C, so j exists.
- For i < j, x_i is unswitched on [k′, k], so it has the successor x_(i+1) at every state k′ … k + 1, and [COPY] applies at every
  transition of [k′, k].
- [COPY] in both directions (P-N5-STAIR G-ST-1 / P-1) makes W(v) change exactly when W(x_j) does, with q(v) = π(q(x_j)) for a strictly
  increasing composite π. So:
  - x_j ∈ C is impossible;
  - x_j changes at k′ and k only;
  - q_k(x_j) > q_(k′)(x_j).
- The type split R / T / S is exhaustive for a vertex switched in [k′, k] ✓. j = 0 when (v, k) is not COPIED ✓.
- Counting ✓.
  - Distinct v map to one (x, k): at most n of them.
  - A T-descent has a switch of x at some t ∈ (k′, k) at which W(x) does not change (its changes are at k′ and k). For fixed x these
    windows are disjoint, so T_F ≤ TS_F.

## 3. ROOT-STAIR
- [STAIR] with DESC_F ≤ n(R + T + S) ≤ n(R + S + TS) ✓.
- Converse ✓: R + S ≤ DESC ≤ n·WCT (by [STAIR]), and TS ≤ n·|F| (≤ n switches per transition).
- The equivalence over families is ✓.

## 4. ORIGIN-NEW: the R15 Lemma A / B step, with care
- The setting is right.
  - G′ := the parity game on the arena H_(k−1), with Odd fixed to τ (= τ_(k−1) on F). σ_k is a strategy of G′, being S4a's choice from
    H_(k−1).
  - In a one-player game with Odd fixed, VJ00's counterstrategy is τ itself, so G′'s VJ00 valuation of σ_k is exactly W_k.
  - [1E-N3] at the S4a step k − 1 → k makes σ_k pointwise optimal in G′: val(ρ, τ) ⊴ W_k for every strategy ρ of G′.
- The known trap is «a maximum has no improvement», which fails at own cycle nodes: R15 (b) allows a length-only improving switch at
  v with Λσ(v) = v that leaves Ω unchanged.
  - Here the switching vertex is y with Λ_(σ_k)(y) = the W_k-cycle node of y = λ_W(y). λ_W is fixed on F.
  - y ∉ C, because W(y) changes at k while C-vertices are constant ([COPY]'s second clause). So λ_W(y) ≠ y, y is not an own cycle node
    in G′, and R15 (b)'s exception does not apply. L-NEW's claim «a root change is never at C» is exactly this, and it is correct.
- The argument holds.
  - Suppose (y, z) ∈ H_(k−1) and W_k(z) ▷ W_k(z0). Then {(y, z)} is a non-empty unambiguous improvement set of σ_k in G′.
  - R15 (a) gives Ω′ ⊵ W_k pointwise. R15 (b) gives Ω′ ≠ W_k, since y is not an own cycle node.
  - Then Ω′ ▷ W_k at some vertex, against pointwise optimality. So W_k(z) ⊴ W_k(z0) (by [LEX], linear).
- The Φ step holds.
  - y ∉ P(W_k(z0)) and y ∉ P(W_(k+1)(z)), as in G-ST-1. Both values have cycle node λ_W(y) ≠ y, because W_k(z) = W_(k+1)(z) (origin).
  - Φ(y; ·) adds the same bit and +1 length, so it preserves ⊴ on such values.
  - So W_(k+1)(y) ⊴ W_k(y), and [W-MON] gives equality: not a root change.
- The «in particular» clause holds: z ∈ H_k(y) \ {z0} = Iσ_k(y), and z ∉ H_(k−1)(y) ⊇ Iσ_(k−1)(y).
- RELAY is the contrapositive ✓.

## 5. NEW-FUEL, ROOT-SPLIT
- NEW-FUEL ✓.
  - z ∈ Iσ_k(y), so Ξ_k(z) ▷ Ξ_k(z0).
  - z ∉ H_(k−1)(y) gives Ξ_(k−1)(z) ⊴ Ξ_(k−1)(z1) (linear).
  - Ξ_k(z0) ⊵ Ξ_(k−1)(z1): if z0 = z1, by R15 (d); otherwise (y, z0) ∈ Iσ_(k−1) and then R15 (d).
  - Equality Ξ_k(z) = Ξ_(k−1)(z) would give Ξ_k(z) ⊴ Ξ_k(z0), a contradiction.
  - The fuel re-route matches P-N5-ODD §6's definition word for word.
- ROOT-SPLIT ✓: new edge ⇒ NEW-FUEL; old edge ⇒ ORIGIN-NEW's contrapositive (relay). An R-descent has k′ ≥ p and k′ < k, so k − 1 ∈ F.

## 6. FUEL-ROOT-STAIR
- A fuel R-descent (y, k) is a fuel re-route of (y, σ_(k+1)(y)) at k, and the map is injective. [FUEL-COUNT] gives the bound, and
  inserting it into §3 is ✓.
- Conditional on [FUEL-COUNT] landing (P-N5-ODD line pending ODD-L5).

## 7. Controls (own engine; docs/referee/scratch/root114_probe.py, `python3 -I`, rl_engine, β and descents from stair_probe.py; no lane code)
- Checks:
  - DR: DESC-ROOT's walk and its conclusions for every descent; j = 0 for R / T / S;
  - the counting bounds; the ROOT-STAIR bound;
  - ON: ORIGIN-NEW at every origin root change with k − 1 ∈ F;
  - NF: NEW-FUEL at every new-edge switch with k − 1 ∈ F;
  - ROLD: R-descents by old edges.
- Pins (from the frozen worktree; every start valid, owner and edge checked). Each equals the lane's desc5.py line pinned in check.sh
  «box 113 DESCSTAR»:
  - frz32: R 21, S 2, ROLD 3, NF 44, ON 44;
  - lcount2_n23: R 1, T 1, S 1, TS 1, NF 5, ON 4;
  - w_re3_1: R 11, S 2, ROLD 2;
  - hit_b6a_1: R 17, S 1.
  - cp_K4 (n 192, MAXN 200): R 388 (all descents), NF 3,177, ON 3,177 (lane RD_K1 388, NFSW 3177, ORIGCH 3177).
  - VIOLATIONS 0 on all five (root114_logs/pin_cpK4.txt).
- MUT controls (all bite on the four pins):
  - MUT 1 (NEW-FUEL for every switch): NF_V 6.
  - MUT 2 (DESC-ROOT stops only at a vertex switched at k): DR_V 5, DR0_V 7.
  - MUT 3 (DEAD (a), «every R-descent enters by a new edge»): OLDEDGE_V 5.
- Corpus: 719 distinct games, MAXN 100 (656 analysed, 63 skipped), start file when present. Results (root114_logs/sum.txt):
  - 950 W-runs, 7,401 transitions;
  - 6,584 descents = R 3,693 + T 1 + S 443 + COPIED 2,447, every one walked by DR; TS 201; ROLD 32;
  - ON 11,251 origin root changes, NF 11,884 new-edge switches;
  - VIOLATIONS 0.
  - The lane's corpus (1,132 lines) is a superset of mine. Its T = 1 equals mine.
- L-NEW's check.sh block «box 113 DESCSTAR» (at ed2fdaf2), run alone in a detached worktree: PASS, EXIT 0.
- Oink 8fbf0a7 `--zlk --verify` verifies the solution on frz32, lcount2_n23, w_re3_1 and cp_K4.

## 8. RESULTS line (954af7be): strict symbol test
- REQUIRED changes:
  - ROOT-L1 (unquantified clause variables, the same kind as STAIR-L9 and ODD E3.5). The quantifier is «for every N5 run on every game
    and every W-run F = [p, q] of it». DESC-ROOT's v, k and k′, ORIGIN-NEW's (y, k), NEW-FUEL's y, z and k, and ROOT-SPLIT's (y, k) are
    bound only by «if …». Fix: «… and every W-run F = [p, q] of it, every vertex v, every Even y, every vertex z and every transition
    k → k + 1 of F:».
  - ROOT-L2 (citations of unlanded, unpinned lines). «β, first-difference positions, descents and DESC_F as in P-N5-STAIR's line L-1»,
    «P-N5-STAIR (Lemma COPY … Theorem STAIR, as in its line L-1, docs/new/P-N5-STAIR-line-L1.txt)» and «P-N5-ODD (Corollary FUEL-COUNT)»
    name files with no commit and no sha1. P-N5-STAIR L-1 is itself pending STAIR-L9, and P-N5-ODD's line is pending ODD-L5. Fix: cite
    each by its landed RESULTS label once it lands; until then, by commit and sha1 (l-new 360d002f / d027f5d8 for STAIR L-1; l-si
    0afc0d70a §6 with fixes entries 1-2 for FUEL-COUNT).
  - ROOT-L3. HC_F(y, z) is glossed «FUEL-COUNT's count of transitions of F changing Ξ(z) at a key above that of the last fuel re-route of
    (y, z)». «key» is never defined in this line, and «at a transition ≤ u» is dropped. Fix: give P-N5-ODD's key ((2, 0) / (1, r) /
    (0, 0), ordered) and «the last fuel re-route of (y, z) at a transition ≤ u», or cite the landed P-N5-ODD line for both.
- Precision:
  - «a descent (x, k) of x with previous change of W(x) at k′»: k′ ≥ p is implicit in «on F» (STAIR L-1's definition) ✓.
  - The scope tail could add «DESC*-LIN DEAD in the weak form (L-RED R163)», as the packet's header does (optional).
- Token pass otherwise clean:
  - n, values, the order, Ξ_k, Iσ_k, H_k (gloss), F, p, q, τ, C, |F|, W_k, s_k, T1_F, WCT_F, the types, R_F, T_F, S_F, tie switch, TS_F,
    root change, origin, relay, fuel re-route, N_F, R^old_F, R^fuel_F, x_i and j are bound.
  - The sums are over Even edges with N_F ≥ 1.
- TARGET.md diff: «REDUCTIONS and EQUIVALENCES (no count is bounded here; …; G-N5-TIME stays OPEN; not M3, not a step-4 pass, not a
  TARGET.md claim)» ✓. No algorithm claim.
- Verdict: the line does NOT yet match. It needs ROOT-L1 to ROOT-L3.

## DONE / FINDINGS / NEEDS
- DONE: this report; root114_probe.py; root114_logs/.
- FINDINGS:
  1. Every item to sign is SIGNED, with no gap. ORIGIN-NEW's use of R15 (a)/(b) is valid, because y ∉ C makes y not an own cycle node in
     G′.
  2. FUEL-ROOT-STAIR is conditional on P-N5-ODD landing; DESC-ROOT and ROOT-STAIR are conditional on P-N5-STAIR landing.
  3. Line: REQUIRED ROOT-L1 (quantifiers), ROOT-L2 (pin the cited lines), ROOT-L3 (key / HC).
- NEEDS: Lead: route ROOT-L1..L3 to L-NEW (a fixes file for box 114).
