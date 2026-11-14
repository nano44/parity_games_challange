# Box 109 (design day 2026-11-14; D27 / D28 / D18 / D1; Lead brief 13:42Z, design lane B): the hybrids h1-h4 against both kill families, and ONE candidate inside the strategy-improvement scheme: S8 = RF (ROOT-FIRST)
L-SI successor 57 (session_01V5yGRZzMPHfvDam83kize6). Written 2026-11-14 (date -u in the commit). Labels: PROVED (L-SI lane, unrefereed) /
DATA (counter, unit, set, scope) / CONJECTURE / OPEN / READING.
**SCOPE LINE: nothing here is a TARGET.md claim, M3 or M4. RF is a CANDIDATE at gauntlet steps 1-2 (pseudocode, one implementation,
agreement with Zielonka on 10,000 random games, growth tables on the families named below); it has NOT been attacked by anyone but its
author, and no bound on its iteration count is proved beyond Lemma ACYC (§4.4). «Not killed in this box» is the strongest status any
rule has here.**
D1 (owner, verbatim): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the
fleet's own, as wrong until it passes the gauntlet below.» D27 (owner, verbatim, as relayed in the Lead's brief): «SO we have to look
for a new algorithm no? Do we have any promising lead or can convert our learning into a new promising algorithm?»

## 0. Result
1. **STALL (§2).** Both kill families share one mechanism: the core's improving edge (K0, K1) is in Iσ from the first state, and S4a
   holds it until the first fallback. **Lemma STALL-W (PROVED, lane, from P-N5-WRAP §4.8's computations):** on W(H, s0), for EVERY
   parity game H and start s0, every CORE-FAIR rule (one that never holds an improving edge at K0, K1, K3 or a valve) stops after
   exactly 3 iterations. DATA: the same 3 iterations on Γ3(G_k), k = 3..12, and on the disjoint unions. So «polynomial on both kill
   families» is cheap; the families that bind a design are the classical counters (Friedmann's G_n, PGSolver's switchallexp and
   switchbestexp), which the Lead's table did not list.
2. **Hybrids (§3).** h2 (run both, stop with the first) DIES on the disjoint union DU_a = Γ3(G_a) ⊔ W(G_a, ι): N5 2^a + 1, N5′-xi
   9·2^a − 7 (DATA a = 3..7). h3 (Ξσ-best first, key only among Ξσ-ties) and h4 (dependency-ordered Howard, static SCCs) are Howard's
   rule on a strongly connected game: they DIE on switchallexp from S3 (10, 30, …, 2486 at N = 1..8) and on Friedmann's G_n from ι
   (9·2^n − 10, n = 1..8; [F11] Theorem 6.14). My own hybrid NH (no-hold N5) DIES on switchbestexp (20, 58, 134, 286, 590, 1198, 2414
   at N = 1..7). **h1 (alternate the two tie rules) is NOT killed in this box**: 9 on Γ3(G_k) (k = 4..12), 11 on W(G_n, ι) (n = 3..8),
   11 on DU_a, and equal to N5 on the three classical families (no S4a tie arises there). Its killer would be a DE-TIED Γ3(G_k)
   (§3.3, OPEN): a family on which S4a's TIE sets are singletons kills every tie rule, every alternation and every dovetailing at once.
3. **Candidate S8 = RF (§4).** One-sided, memoryless, inside the Vöge-Jurdziński scheme: switch-best exactly at the improvable
   vertices whose inputs are settled, where «settled» is read off the play graph of (σ, σ̄) (the Lead's lesson L2 made exact, with
   the cyclic case resolved by sink strongly connected components). PROVED: it is a strategy-improvement run (terminates, correct);
   at most |V_E| iterations on games whose only cycles are self-loops of one-successor vertices (Lemma ACYC). DATA (iterations): Γ3(G_k)
   6, 6, 8, 8, 10, 10, 12, 12, 14, 14 (k = 3..12); W(G_n, ι) 8 (n = 1..8); Friedmann's G_n from ι 3n + 3 (n = 2..16; Howard 9·2^n − 10);
   switchallexp ≤ 79 (N ≤ 16; Howard 2486 at N = 8); switchbestexp ≤ 184 (N ≤ 14; Howard 2541 at N = 7); 10,000 random games: wrong 0,
   badstrat 0. My own attack (hill-climb, §4.7) reaches 16, 25, 22, 27, 40, 41 iterations at n = 6, 7, 8, 9, 10, 12: RF is slow in the
   single-switch sense, and superlinear growth is NOT excluded.
4. My best guess of what kills RF (§4.6): DEPENDENCY COLLAPSE (a Howard-exponential family in which the improvable vertices never
   lie on each other's option plays, e.g. through Odd mirror gates, so that RF's switching set is Howard's), or a LEAPFROG counter
   routed through cross edges.

## 1. Setting
- [SPEC] = docs/new/N5-ssi-global.md «SPEC (EXACT …)» (S1 valuations Ξσ and Odd's optimal counterstrategy σ̄; S2 improving edges Iσ; S3
  start; S4a/b/c; S5). N5 = SPEC. N5′-xi = RESULTS R118's rule ([N5XI] in docs/si/P-N5-WRAP.md §1). G^d = the dual game.
- Kill families. Γ3(G_k): the genome G_k (docs/si/box108-gk-proof.md §1.2; builder experiments/si/box108/gk108.py, gate numbers ranked
  onto 0..M − 1) realised by L-NEW's gamma3.build(G, eg195.PADS) + eg195.topg, the calls of L-RED-B's b6n5.py; n = 135k − 230. DATA
  (`fam109.py gkeq`, out/gkeq.out): for k = 3..12 this game equals, vertex by vertex, the one built from L-RED-B's gk.py (claude/l-red-b
  10dfedb6). W(G_n, ι): docs/si/P-N5-WRAP.md §2.1 with H = Friedmann's G_n ([F11] Figure 4's injective priorities, L-LIT's
  transcription T66 at claude/l-lit 5c53efbd) and s0 = ι. DU_a := the disjoint union Γ3(G_a) ⊔ W(G_a, ι) (W's vertices renumbered
  after Γ3's), a ≥ 3.
- Classical families. fr n = G_n itself, Even started at ι, Odd at S3. sae N / sbe N = PGSolver's switchallexp / switchbestexp
  (experiments/hard-families/pgsolver_port.py), start S3. Ports of experiments/si/gens.py (randomfacetsubexp, zadehexp, cunninghamexp,
  dlmm_bland), start S3.
- Engine (one, `experiments/si/box109/n6.py`): L-SI's si.Engine (S1, S2, S3) and, for the N5-shaped rules, L-NEW's n5v.step (box 190;
  modes spec, xi). Every rule applies in each iteration a non-empty set of improving switches (at most one per vertex) of σ on G and /
  or of τ on G^d, so RESULTS R15 (a), (c), (d) give termination, and the stop is S5's. COUNTERS (reading L43; one line per (family,
  size, rule) in out/*.out): **iterations** (unit: passes of the rule's own loop that change σ or τ; one-sided rules count Even's
  improvement steps), **fallbacks** (unit: S4c iterations), **switches** (unit: (Even vertex, iteration) pairs with a changed
  successor), **wrong** (unit: vertices whose winner differs from harness Zielonka), **badstrat** (unit: complaints of harness
  verify.check about the positional strategies, D2 change 5), **capped**. wrong, badstrat and capped are 0 on every row of this file.
- ENGINE FAITHFULNESS (the two known rows first; CLAUDE.md Traps): N5 on Γ3(G_k): 9, 17, 33, 65, 129, 257 at k = 3..8 (= 2^k + 1, the
  count of packet P-N5-EXP as relayed by the Lead), 1 fallback; N5′-xi on Γ3(G_k): 6 at k = 3 and 7 at k = 4..12 (the Lead's «7
  iterations (DATA, k = 4, 6)»); N5 on W(G_n, ι): 6 (n = 1..8) and N5′-xi: 11, 29, 65, 137, 281, 569 (n = 1..6), the rows of
  docs/si/P-N5-WRAP.md §9 (box 104's frozen rows continue with 1145, 2297 at n = 7, 8).

## 2. STALL: what the two kill families have in common
In the standard state of W(H, s0) the edge (K0, K1) is improving (P-N5-WRAP Lemma ESC-W: «Iσ ∋ (K0, K1)»), S4a's arena optimum keeps
K0 at pA (E1-W (b)), and the K-config changes only at a fallback (E1-W's corollary). The whole run before the first fallback is spent
on V_E while the escape is held. Call a rule CORE-FAIR on W(H, s0) if in every iteration every vertex of {K0, K1, K3} ∪ {valves}
that has an improving edge is switched to it (each of these vertices has two successors, so the edge is unique), and τ is changed
only by improving switches of Iτ.

**Lemma STALL-W (PROVED, lane; premises: docs/si/P-N5-WRAP.md Lemmas S3-W, TAU-W, E1-W (a), and the Iσ computations inside the proofs
of E3-W, E4-W (a), E4-W (b), each of which holds «for σ arbitrary at V_E and at the valves» (§4.8's first line)).** For every parity
game H and every positional Even strategy s0 of H, every core-fair rule started at S3 on W(H, s0) makes exactly 3 iterations.
*Proof.* S3 is the standard state of s0 (S3-W): K-config κ0, τ = τ0. Iτ0 = ∅ (TAU-W; Iτ depends on τ alone), so τ = τ0 throughout.
Iteration 1: at κ0 the improving edges out of the core's Even vertices are exactly {(K0, K1)} (E1-W (a)); core-fairness switches K0
and nothing else in the core: κ1. Iteration 2: at κ1 they are exactly {(K1, q)} (proof of E3-W: «(K1, q) ∈ Iσ», K0 «not improving»,
K3 «not improving»): κ2. Iteration 3: at κ2 they are exactly {(K3, K1)}, and at every valve (b, pb) ∈ Iσ where σ(b) = y and
(b, y) ∉ Iσ where σ(b) = pb (proof of E4-W (a)): the result has K-config κ3 and σ(b) = pb at every valve, whatever happened at the
valves and on V_E before. At such a state Iσ = ∅ (E4-W (b), «any σ* at V_E»), and Iτ = ∅: the run stops. Iterations 1-3 each changed
σ, so the count is exactly 3. ∎
- Core-fair rules of §3: howard, h3, nh (each switches EVERY improvable Even vertex in every iteration). DATA: 3 iterations on
  W(G_n, ι), n = 1..8 (out/wl.out), as the lemma says.
- DATA (not proved; the core of Γ3 is «exactly as in R117's Γ3», but I have not redone STALL-W's three steps on Γ3's valves): howard,
  h3 and nh make 3 iterations on Γ3(G_k) for k = 3..12 and on DU_a for a = 3..7 (out/gk.out, out/du.out). CONJECTURE STALL-Γ3: the same
  lemma holds on Γ3(G) for every R104 genome G.
- READING. (i) The Lead's lesson L1 («the kills are complementary») is confirmed and sharpened: the two families do not test a tie
  rule's quality, they test whether S4a's arena step is allowed to hold an escape for the length of a run that the tie rule makes
  long. (ii) A second, cheaper exit is in the same data: on Γ3(G_k), W(G_n, ι) and DU_a, Iτ = ∅ at the START (TAU-W for W; DATA for
  Γ3): τ0 is already optimal, and a stop rule «Iσ = ∅ OR Iτ = ∅» (row rf2 of §3) ends in 0 iterations. Neither exit is a defence of
  N5: an adversary removes both by putting the game next to its dual, or by building the escape into the counter. They only say
  that today's two families constrain a new rule very little.

## 3. The hybrids
### 3.1 Rules (exact; `n6.py` modes)
| id | mode | rule (Even's side; Odd's side in brackets) |
| --- | --- | --- |
| N5 | spec | SPEC S1-S5 |
| N5′-xi | xi | [N5XI] |
| h1 | h1 | iteration t odd: an N5 iteration; t even: an N5′-xi iteration (t counts iterations from 1) |
| h2 | (derived) | run N5 and N5′-xi side by side, one iteration of each per round, stop with the first that stops: 2·min(N5, N5′-xi) iterations |
| h3 | h3 | every improvable Even v moves to the Ξσ-best element of A(v) = {σ(v)} ∪ Iσ(v); among Ξσ-equal best elements: SPEC's S4a choice if it is one of them, then the larger index [Odd: S4b; S4c for Odd when Iσ = ∅] |
| Howard | howard | classical switch-best for Even only (ties: larger index); τ not used |
| h4 | h4 | dependency-ordered Howard, static: switch-best only at the improvable Even vertices of those strongly connected components of the GAME GRAPH from which no other component holding an improvable Even vertex is reachable; τ not used |
| NH | nh | no-hold N5 (mine): S4a's / S4b's choice where it moves; every improvable vertex that S4a (S4b) holds moves to its best improving edge (ties: larger index). S4c is kept as written but cannot fire: when Iσ ∪ Iτ ≠ ∅ some vertex moves (fallbacks 0 on every row) |
| RF | rf | §4 (candidate S8) |
| RF2 | rf2 | RF on both sides at once (Odd on G^d), stop when Iσ = ∅ OR Iτ = ∅; output read from the optimal side |

### 3.2 Iterations (DATA; generated rows: `tab109.py` from out/*.out; columns: family, rule, sizes, iterations, fallbacks summed, wrong + badstrat + capped summed)
| family | rule | sizes | iterations | fb | bad |
| --- | --- | --- | --- | --- | --- |
| gk | spec | 3, 4, 5, 6, 7, 8 | 9, 17, 33, 65, 129, 257 | 6 | 0 |
| gk | xi | 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 | 6, 7, 7, 7, 7, 7, 7, 7, 7, 7 | 10 | 0 |
| gk | h1 | 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 | 11, 9, 9, 9, 9, 9, 9, 9, 9, 9 | 10 | 0 |
| gk | h3 | 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 | 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 | 0 | 0 |
| gk | howard | 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 | 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 | 0 | 0 |
| gk | h4 | 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 | 5, 5, 5, 5, 5, 5, 5, 5, 5, 5 | 0 | 0 |
| gk | nh | 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 | 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 | 0 | 0 |
| gk | rf | 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 | 6, 6, 8, 8, 10, 10, 12, 12, 14, 14 | 0 | 0 |
| gk | rf2 | 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 | 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 | 0 | 0 |
| wl | spec | 1, 2, 3, 4, 5, 6, 7, 8 | 6, 6, 6, 6, 6, 6, 6, 6 | 8 | 0 |
| wl | xi | 1, 2, 3, 4, 5, 6 | 11, 29, 65, 137, 281, 569 | 6 | 0 |
| wl | h1 | 1, 2, 3, 4, 5, 6, 7, 8 | 7, 9, 11, 11, 11, 11, 11, 11 | 8 | 0 |
| wl | h3 | 1, 2, 3, 4, 5, 6, 7, 8 | 3, 3, 3, 3, 3, 3, 3, 3 | 0 | 0 |
| wl | howard | 1, 2, 3, 4, 5, 6, 7, 8 | 3, 3, 3, 3, 3, 3, 3, 3 | 0 | 0 |
| wl | h4 | 1, 2, 3, 4, 5, 6, 7, 8 | 8, 8, 8, 8, 8, 8, 8, 8 | 0 | 0 |
| wl | nh | 1, 2, 3, 4, 5, 6, 7, 8 | 3, 3, 3, 3, 3, 3, 3, 3 | 0 | 0 |
| wl | rf | 1, 2, 3, 4, 5, 6, 7, 8 | 8, 8, 8, 8, 8, 8, 8, 8 | 0 | 0 |
| wl | rf2 | 1, 2, 3, 4, 5, 6, 7, 8 | 0, 0, 0, 0, 0, 0, 0, 0 | 0 | 0 |
| du | spec | 3, 4, 5, 6, 7 | 9, 17, 33, 65, 129 | 5 | 0 |
| du | xi | 3, 4, 5, 6, 7 | 65, 137, 281, 569, 1145 | 5 | 0 |
| du | h1 | 3, 4, 5, 6, 7 | 11, 11, 11, 11, 11 | 5 | 0 |
| du | h3 | 3, 4, 5, 6, 7 | 3, 3, 3, 3, 3 | 0 | 0 |
| du | howard | 3, 4, 5, 6, 7 | 3, 3, 3, 3, 3 | 0 | 0 |
| du | h4 | 3, 4, 5, 6, 7 | 8, 8, 8, 8, 8 | 0 | 0 |
| du | nh | 3, 4, 5, 6, 7 | 3, 3, 3, 3, 3 | 0 | 0 |
| du | rf | 3, 4, 5, 6, 7 | 8, 8, 8, 8, 10 | 0 | 0 |
| du | rf2 | 3, 4, 5, 6, 7 | 0, 0, 0, 0, 0 | 0 | 0 |
| fr | spec | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16 | 3, 4, 5, 7, 9, 11, 13, 15, 17, 19, 23, 27, 31 | 0 | 0 |
| fr | xi | 1, 2, 3, 4, 5, 6, 7, 8 | 3, 4, 5, 7, 9, 11, 13, 15 | 0 | 0 |
| fr | h1 | 1, 2, 3, 4, 5, 6, 7, 8 | 3, 4, 5, 7, 9, 11, 13, 15 | 0 | 0 |
| fr | h3 | 1, 2, 3, 4, 5, 6, 7, 8 | 8, 26, 62, 134, 278, 566, 1142, 2294 | 0 | 0 |
| fr | howard | 1, 2, 3, 4, 5, 6, 7, 8 | 8, 26, 62, 134, 278, 566, 1142, 2294 | 0 | 0 |
| fr | h4 | 1, 2, 3, 4, 5, 6, 7, 8 | 8, 26, 62, 134, 278, 566, 1142, 2294 | 0 | 0 |
| fr | nh | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16 | 5, 7, 13, 17, 21, 26, 30, 35, 40, 45, 54, 65, 73 | 0 | 0 |
| fr | rf | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16 | 5, 9, 12, 15, 18, 21, 24, 27, 30, 33, 39, 45, 51 | 0 | 0 |
| fr | rf2 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16 | 0 | 0 |
| sae | spec | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16 | 5, 8, 7, 8, 10, 12, 14, 16, 18, 20, 24, 28, 32 | 0 | 0 |
| sae | xi | 1, 2, 3, 4, 5, 6, 7, 8 | 5, 8, 7, 8, 10, 12, 14, 16 | 0 | 0 |
| sae | h1 | 1, 2, 3, 4, 5, 6, 7, 8 | 5, 8, 7, 8, 10, 12, 14, 16 | 0 | 0 |
| sae | h3 | 1, 2, 3, 4, 5, 6, 7, 8 | 10, 30, 70, 150, 310, 630, 1243, 2486 | 0 | 0 |
| sae | howard | 1, 2, 3, 4, 5, 6, 7, 8 | 10, 30, 70, 150, 310, 630, 1243, 2486 | 0 | 0 |
| sae | h4 | 1, 2, 3, 4, 5, 6, 7, 8 | 10, 30, 70, 150, 310, 630, 1243, 2486 | 0 | 0 |
| sae | nh | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16 | 6, 13, 19, 25, 31, 37, 43, 49, 55, 61, 73, 85, 97 | 0 | 0 |
| sae | rf | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16 | 10, 21, 21, 27, 30, 40, 41, 65, 71, 71, 73, 76, 79 | 0 | 0 |
| sae | rf2 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16 | 0 | 0 |
| sbe | spec | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14 | 20, 32, 41, 47, 55, 62, 68, 77, 83, 89, 104, 117 | 0 | 0 |
| sbe | xi | 1, 2, 3, 4, 5, 6, 7 | 20, 32, 41, 47, 55, 62, 68 | 0 | 0 |
| sbe | h1 | 1, 2, 3, 4, 5, 6, 7 | 20, 32, 41, 47, 55, 62, 68 | 0 | 0 |
| sbe | h3 | 1, 2, 3, 4, 5, 6, 7 | 21, 61, 141, 301, 621, 1261, 2541 | 0 | 0 |
| sbe | howard | 1, 2, 3, 4, 5, 6, 7 | 21, 61, 141, 301, 621, 1261, 2541 | 0 | 0 |
| sbe | h4 | 1, 2, 3, 4, 5, 6, 7 | 21, 61, 141, 301, 621, 1261, 2541 | 0 | 0 |
| sbe | nh | 1, 2, 3, 4, 5, 6, 7 | 20, 58, 134, 286, 590, 1198, 2414 | 0 | 0 |
| sbe | rf | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14 | 17, 38, 43, 69, 74, 82, 93, 106, 117, 132, 158, 184 | 0 | 0 |
| sbe | rf2 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14 | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14 | 0 | 0 |
| cun | howard | 2, 3, 4, 5, 6, 7, 8 | 4, 4, 4, 4, 4, 4, 4 | 0 | 0 |
| cun | rf | 2, 3, 4, 5, 6, 7, 8 | 3, 4, 5, 6, 7, 8, 9 | 0 | 0 |
| cun | rf2 | 2, 3, 4, 5, 6, 7, 8 | 2, 3, 4, 5, 6, 7, 8 | 0 | 0 |
| dlb | howard | 2, 3, 4, 5, 6, 7, 8 | 1, 2, 3, 4, 5, 6, 7 | 0 | 0 |
| dlb | rf | 2, 3, 4, 5, 6, 7, 8 | 1, 2, 3, 4, 5, 6, 7 | 0 | 0 |
| dlb | rf2 | 2, 3, 4, 5, 6, 7, 8 | 1, 2, 3, 4, 5, 6, 7 | 0 | 0 |
| rfs | howard | 2, 3, 4, 5, 6, 7, 8 | 4, 6, 8, 10, 12, 14, 16 | 0 | 0 |
| rfs | rf | 2, 3, 4, 5, 6, 7, 8 | 4, 20, 26, 66, 78, 90, 102 | 0 | 0 |
| rfs | rf2 | 2, 3, 4, 5, 6, 7, 8 | 3, 4, 5, 6, 7, 8, 9 | 0 | 0 |
| zad | howard | 2, 3, 4, 5, 6, 7, 8 | 4, 6, 5, 6, 5, 6, 5 | 0 | 0 |
| zad | rf | 2, 3, 4, 5, 6, 7, 8 | 4, 7, 8, 9, 13, 11, 15 | 0 | 0 |
| zad | rf2 | 2, 3, 4, 5, 6, 7, 8 | 3, 5, 7, 9, 11, 11, 15 | 0 | 0 |

Derived row h2 (2·min of the spec and xi rows): Γ3(G_k) 12, 14, 14, … ; W(G_n, ι) 12; **DU_a 18, 34, 66, 130, 258 (a = 3..7)**.
Sizes: Γ3(G_k) n = 175, 310, …, 1390 (k = 3..12); W(G_n, ι) n = 211, 395, 600, 826, 1073, 1341, 1630, 1940 (n = 1..8); DU_a n = 775,
1136, 1518, 1921, 2345 (a = 3..7); fr n: 10n + 4 vertices; sae N: 14N + 7; sbe N: 25N + 10.

### 3.3 Verdicts
| rule | Γ3(G_k) | W(G_n, ι) | DU_a | fr / sae / sbe | verdict | killing instance |
| --- | --- | --- | --- | --- | --- | --- |
| N5 | 2^k + 1 | 6 | 2^a + 1 | linear | DEAD (packet P-N5-EXP) | Γ3(G_k) |
| N5′-xi | 7 | 9·2^n − 7 | 9·2^a − 7 | = N5 | DEAD (RESULTS R130) | W(G_n, ι) |
| h1 | 9 | 11 | 11 | = N5 | **not killed in this box** | none found; see below |
| h2 | 14 | 12 | 2·(2^a + 1) | = 2·N5 | **DEAD (DATA a = 3..7; argument below)** | DU_a |
| h3 | 3 | 3 | 3 | Howard's counts | **DEAD** | switchallexp_N from S3 (DATA N = 1..8: 10, 30, 70, 150, 310, 630, 1243, 2486); G_n from ι ([F11] Theorem 6.14 with Claim NT) |
| h4 | 5 | 8 | 8 | Howard's counts | **DEAD** | the same two (each is one strongly connected component as far as h4's order is concerned: h4's counts equal Howard's on every row) |
| NH | 3 | 3 | 3 | linear / linear / doubling | **DEAD (DATA N = 1..7)** | switchbestexp_N from S3: 20, 58, 134, 286, 590, 1198, 2414 |
| RF | 2⌊(k − 1)/2⌋ + 4 | 8 | 8, 10 | linear on fr, sbe; ≤ 79 on sae | not killed in this box (candidate, §4) | none found |
| RF2 | 0 | 0 | 0 | n, N, N | not killed in this box; not proposed (its gain is the stop rule of §2 READING (ii)) | none found |

- **h2 on DU_a (argument; DATA agrees).** In a disjoint union the S1 valuations, Iσ, Iτ, S4a's and S4b's arenas of the two parts do not
  interact (no edge joins them; the rank order inside each part is the part's own, since the renumbering keeps each part's index
  order), so every non-fallback iteration acts on each part as on the part alone. S4c fires only when BOTH parts stall. Under N5 the
  Γ3(G_a) part moves for L(G_a) = 2^a − 2 iterations (packet P-N5-EXP; box 108 Theorem GK for the model) while the W part stalls from
  its iteration 4 on; under N5′-xi the W part moves for Howard's T ≥ 2^a iterations (P-N5-WRAP WRAP (iii), XI-EXP). Measured:
  2^a + 1 and 9·2^a − 7. So h2 makes ≥ 2·(2^a + 1) iterations on DU_a, a game with 135a − 230 + |W(G_a, ι)| = O(a²) vertices. Status of
  the argument: READING on top of the two packets (the «parts do not interact» step is not written to referee standard here).
- **h3, h4.** On a game where no two successors of a vertex ever have equal Ξσ-values, h3's σ-run is Howard's (the tie clause is
  never used), and Iσ depends on σ alone (RESULTS R15 (d)), so Odd's side cannot shorten it. On G_n from ι that run is the I^loc run
  of [F11] Theorem 6.14 (no tie: P-N5-WRAP Claim NT): ≥ 2^n. From S3 (the rule's own start) the kill is DATA on switchallexp. h4's
  static components do not separate anything on either family (its counts equal Howard's row by row).
  The Lead's question «what does such a rule do on W(G_n, ι), where everything is one tied core?»: h3, h4 and Howard do NOT die
  there (3, 8, 3 iterations): the wrapper's own escape ends the run (STALL-W). They die on the unwrapped counter.
- **NH.** N5's own selections plus Howard's choice at every held vertex: on switchbestexp the held vertices carry the counter
  (doubling from N = 2). Obstruction: «never hold» makes the rule a switch-all rule, and Friedmann-type counters are built against
  exactly those.
- **h1 is not killed here**, by either family, by their union, or by the three classical families. What I expect to kill it, and
  with it the whole shape «N5 with another tie rule» (L3):
  **Fact SHAPE (PROVED, immediate from P-N5-WRAP Fact (H)).** Let ρ be any rule that picks σ_new(v) inside S4a's TIE(v). On a run in
  which every TIE(v) met is a singleton, N5 with ρ in place of SPEC's choice makes the same iterations as N5.
  Hence a family on which N5 is exponential WITHOUT ties kills every tie rule, every alternation (h1) and every dovetailing (h2) of
  tie rules at once. **OPEN (for the adversaries): DE-TIE Γ3(G_k)**, i.e. realise the root-first key order by strict arena values
  instead of by SPEC's breadth-first tie-break. Sketch (unverified): give the gate of option (x, o) an odd priority above c_W, the
  gates of W-level 0 above those of level 1 and so on, inside a level increasing with the gate index; then two arena plays to the
  root differ first at their root-most differing gate, and the play through the larger index is worse for Even, which is the key
  order. Not checked: that Ξσ, σ̄ and Iτ = ∅ survive these priorities (R104's [DEF] has every gate below c_W for a reason).
  h1's 11 on W(G_n, ι) is also fragile: the N5 iterations of the alternation stall as soon as every v ∈ V_E sits on the key-least
  element of A(v), and the key order is the adversary's (the index order of §2.1 of the packet).

## 4. The candidate S8 = RF (ROOT-FIRST strategy improvement)
### 4.1 Idea
RIPPLE is «a mover moves before its inputs have settled». In the Vöge-Jurdziński scheme the inputs of an improvable vertex v are the
values of its current successor and of its improving targets, and each of these values is carried by ONE play of (σ, σ̄). RF lets v
switch only when no other improvable vertex lies on those plays. Where improvable vertices block each other in a cycle, the blocked
set that depends on nothing outside itself moves together (so the rule is total). On an acyclic dependency structure this is the
one-pass evaluation in dependency order; nothing in the rule mentions τ, an arena, a tie between plays, or a vertex index (except
the tie among equal best valuations).

### 4.2 Exact pseudocode (implementation: experiments/si/box109/rf109.py; the notebook notes/L-SI.md carries the same text)
Input: a parity game G (TARGET.md §1). S1, S2, S3, S5 are [SPEC]'s.
```
sigma := S3's Even strategy (or a given one)
loop:
  1. (Xi, sbar) := S1(sigma)            # Xi = valuation of sigma against Odd's optimal counterstrategy sbar
     I := S2(sigma, Xi)                 # improving edges (v, w): v Even, w != sigma(v), Xi(w) strictly better than Xi(sigma(v))
     if I is empty: stop
  2. Imp := { v : (v, w) in I for some w };   T(v) := { w : (v, w) in I }
  3. nxt(x) := sigma(x) if x is Even's, sbar(x) if x is Odd's
     pi(x)  := the set of vertices on the play x, nxt(x), nxt(nxt(x)), ...          (finite path followed by its cycle)
  4. for v in Imp:  D(v) := ( pi(sigma(v))  ∪  ⋃_{w in T(v)} pi(w) )  ∩  Imp  \  {v}
     Delta := the digraph (Imp, { v -> u : u in D(v) })
  5. S := the union of the strongly connected components of Delta that have no edge into another component
  6. for v in S:  sigma(v) := the w in T(v) maximising (Xi(w), w)                   # best valuation; ties: larger index
output (S5): Even wins v iff the cycle node of Xi(v) has even priority; Even's strategy sigma on Even's region,
             Odd's strategy sbar (for the final sigma) on Odd's region
```
Cost of one iteration beyond S1 and S2: the play graph is a functional graph, so the sets π(x) ∩ Imp are computed for all x in O(n)
set operations on |Imp|-bit sets; D in O(m) such operations; the components of Delta (≤ n vertices, ≤ n² edges) by Tarjan. No number
larger than S1's own n-bit path sets is built (TARGET.md §3). One iteration is polynomial; the open quantity is the number of
iterations.

### 4.3 Correctness and termination (PROVED, lane; premises RESULTS R15 (a), (c) and the classical optimality of a strategy without improving edges, as S5 uses it)
If I ≠ ∅ then Imp ≠ ∅, the finite digraph Delta has a component without outgoing edges, so S ≠ ∅; each v ∈ S receives one improving
edge. So σ_new = Switch_J(σ) for a non-empty set J ⊆ Iσ with one edge per vertex («unambiguous»): by R15 (a) Ωσ ⊴ Ω_(σ_new), by R15
(c) no strategy repeats, and the run terminates. At the stop Iσ = ∅, which is S5's condition. No statement about τ is needed (the
rule is one-sided).

### 4.4 Lemma ACYC (PROVED, lane)
Call x CLOSED-FINAL at σ if no vertex reachable from x in G (x included) is improvable at σ.
(A) If x is closed-final at σ and σ′ = Switch_J(σ) for any J ⊆ Iσ, then Ξσ′ = Ξσ on R(x) := the vertices reachable from x, and x is
closed-final at σ′. *Proof.* R(x) is closed under successors, so G|R(x) is a parity game, every play from R(x) stays in it, and the S1
value of a vertex of R(x) is its value in G|R(x) (σ̄ is a pointwise optimum, [1E-N3] P1). J contains no edge out of R(x) (no vertex
there is improvable), so σ′ = σ on R(x). ∎
(B) **If the only cycles of G are self-loops at vertices with one successor, RF makes at most |{v ∈ V_E : v has ≥ 2 successors}|
iterations.** *Proof.* Let Iσ ≠ ∅. G without its self-loops is acyclic, so some improvable v has no improvable vertex among the
vertices reachable from its successors (v itself is not among them: v has ≥ 2 successors, hence no self-loop, and lies on no cycle).
Every play from a successor of v stays among those vertices, so D(v) = ∅, {v} is a sink component, and RF moves v to w := its
Ξσ-best improving target, which is a Ξσ-best successor of v (the non-improving ones are not better than σ(v)). Every successor y of v
is closed-final at σ, so by (A) Ξσ′(y) = Ξσ(y) and y stays closed-final; hence at σ′ no successor of v is strictly better than w: v is
not improvable, and v is closed-final at σ′. By (A) closed-final vertices stay closed-final, and an improvable vertex is not
closed-final: every iteration turns at least one Even vertex with ≥ 2 successors closed-final for good. ∎
READING. (B) is the one-pass statement of lesson L2 in the scheme's own terms. It covers the layered one-player counters built for
index- and level-ranked single-switch rules whenever their graph is acyclic (the port dlmm_ML is: levels l → l + 1 and a sink). It
says nothing about strongly connected games, where every known counter lives.

### 4.5 Measurements (DATA; out/*.out, regenerated by run109.sh; wrong 0, badstrat 0, capped 0 on every row)
- The rows «rf» of §3.2. Fits read off the rows (no claim beyond the listed sizes): Γ3(G_k): 2⌊(k − 1)/2⌋ + 4; fr n: 3n + 3 for
  n = 2..16; sbe N: ≤ 19N, about 13N for N ≥ 6; sae N: ≤ 79 at N ≤ 16 and flattening (65, 71, 71, 73, 76, 79 at N = 8, 9, 10, 12, 14, 16).
- Switching sets (out/sinks.out; unit: vertices): on fr n the largest S has 4 vertices while up to 4n vertices are improvable
  (n = 16: Σ|S| = 126 against Σ|Imp| = 1,270 over the 51 iterations); S = Imp (a Howard step) in 4 of the 3n + 3 iterations. RF's run
  is not Howard's run with pauses: at n = 16 it switches one improvable vertex in ten per iteration, and most of the postponed ones
  are no longer improvable when their turn would come (126 switches in all; the I^loc run has at least 2^16 iterations by [F11]
  Theorem 6.14).
- Ports (out/ports.out): randomfacetsubexp 4, 20, 26, 66, 78, 90, 102 (N = 2..8; Howard 2N); zadehexp ≤ 15; cunninghamexp N + 1;
  dlmm_bland N − 1.
- Random games (out/rand.out): 10,000 games, harness gen.random_game(n, P, 1, D, ·) with n uniform in [2, 40], P uniform in [1, n + 1],
  D uniform in [2, min(n, 6)], seed 109: wrong 0,
  badstrat 0, capped 0 for rf, rf2, nh, h3, h4, h1, howard; max iterations rf 21, howard 12. Control (out/rand_ctrl.out): flipping the
  winner of vertex 0 makes wrong = 100 of 100.
- NOT RUN: the Oink-generated M1 families (counter_*, tc, tc+, recursiveladder at scale): Oink is not built in this container
  (scripts/setup_oink.sh was not run while a push was in verify). L-COMP 23's battery is the place for them.

### 4.6 Barrier statement (first version; gauntlet step 3 is L-LIT's to sign; sources as opened in notes/L-SI.md «Sources opened»)
| framework | source (opened) | does it cover RF? |
| --- | --- | --- |
| locally optimizing policy I^loc (switch-best at every improvable vertex) | [F11] arXiv 1106.0778v2 Theorem 6.14 (G_n from ι: ≥ 2^n) | No as it stands: the theorem is about the I^loc run. DATA: RF's run on the same G_n from the same ι has 3n + 3 iterations (n = 2..16). |
| globally / locally optimal multi-switch rules on PGSolver's switchbestexp | [F11] §8 as cited in docs/si/README.md's map (Theorem 8.4) | No as it stands: RF is not a multi-switch optimum. DATA: ≤ 184 at N ≤ 14. |
| index-based single-switch rules, every numbering | Disser-Loho-Maat-Mosis arXiv 2512.16684v2 Theorem 1.1 | RF uses an index only among equal best valuations. The ported M_L is acyclic: Lemma ACYC. |
| history-based rules (Zadeh, Cunningham) | arXiv 1911.01074v2 (title page only opened); [AF13] arXiv 1305.3944 Theorem 8 | RF is memoryless. DATA on the ports: ≤ 15. |
| Random-Facet | arXiv 1410.7530 Theorem 6.3 | Randomised rules; not applicable. DATA on the port: ≤ 102 at N ≤ 8. |
| symmetric strategy improvement | van Dijk-Loho-Maat arXiv 2309.02223 Theorem 1 | RF is one-sided: its σ-run depends on σ alone. |
| the fleet's kill families | P-N5-EXP (Γ3(G_k)), RESULTS R130 (W(G_n, ι)) | No: 2⌊(k − 1)/2⌋ + 4 and 8 iterations (DATA). |
| «a memoryless single-switch rule ranks improving edges by a quantity the input steers» | L-RED's Lemmas T and D and Gate Lemma, as recorded in docs/si/README.md (unrefereed there) | **NOT shown outside.** Where Delta is a chain RF is a single-switch rule ordered by position on the play, and an Odd gate re-routes plays. This is the framework I expect to transfer. |
Why Friedmann's gates do not transfer as they stand (READING, unproved): a cycle gate keeps the closing edge of a bit's simple
cycle «improving but never best» while the lower bits are reset, and the resets are switches at vertices whose option plays run
through vertices that are improvable in the same iteration. RF postpones exactly those switches (out/sinks.out), and when their
turn comes the edge is usually no longer improving. A counter against RF must make its simultaneous switches pairwise
play-independent, or carry the information between bits through Odd's re-routing, which Delta does not see.

### 4.7 My own attack, and my best guess of what kills RF
- Hill-climb (`climb109.py`; moves: one priority, one owner, add / delete / redirect one edge; objective: RF's iterations from S3;
  out/climb.out). Best found, two-player: 16, 25, 22, 27, 40, 41 at n = 6, 7, 8, 9, 10, 12 (8 restarts × 30,000 steps) and 39 at
  n = 16 (6 × 4,000); one-player (every vertex Even's): 24 at n = 8, 33 at n = 12. On the same games Howard needs 4 to 13. The n = 10
  game (out/climb_rf_10.json) runs through five cycle nodes with a chain of single switches after each: «single-switch» behaviour,
  3 to 4 iterations per vertex, no doubling pattern seen. This is a weak search on tiny games; it neither supports nor refutes a
  polynomial bound. «At most 3n iterations» is false (25 at n = 7, 40 at n = 10).
- Random starts (`starts109.py`, out/starts.out; the start is the adversary's, a wrapper can force S3 to pick it): over 200 uniformly
  random Even strategies RF's maximum is 30 on fr 6 (21 from ι), 56 on sae 6 (40 from S3), 127 on sbe 4 (69 from S3). No blow-up; the
  start matters by a factor below 2 on these three games.
- Family search (`famrf109.py`, out/famsearch.out; gadget templates of G vertices chained k times with edges to the next AND the
  previous copy and a 1-sink; objective: growth between k = K − 2 and K): best templates G = 4 (12 restarts × 1,200 steps) and G = 3,
  descending priorities (16 × 1,500): RF 3, 5, 7, 26, 36, 39, 45, 50, 55, 60, 65 and 3, 3, 5, 8, 17, 24, 29, 36, 41, 48, 53 at
  k = 2..12: about 5 to 7 iterations per copy, linear. No doubling template found at this search size.
- Guess 1, DEPENDENCY COLLAPSE. RF = Howard whenever no improvable vertex lies on another's option plays, or all of them lie on
  each other's. A Friedmann-type counter in which every Even decision vertex is entered only through an Odd MIRROR GATE (the gate
  can also step to a pad chain that copies the vertex's current play up to the next decision vertex) would keep the values and
  remove the vertices from each other's plays. I have not built it; the difficulty is that the copy must follow the vertex's
  switches without itself being a decision vertex.
- Guess 2, LEAPFROG. Values only rise, so a vertex that switches 2^k times needs two options whose values overtake each other 2^k
  times; path sets have room for that. The cross edges that raise an option must come from vertices that are not on the plays of
  the vertex's options at that moment (else RF waits for them). G_k's own latches are of this kind on the key side; on the value
  side G_k is Ξ-acyclic and RF passes it in k + 2 iterations. A Ξ-cyclic latch ladder WITHOUT the escape core is the family I would
  try first.
- Guess 3 (cheap, for RF2 only): the game next to its dual defeats the stop rule «Iσ = ∅ or Iτ = ∅».

## 5. What is not here
No proof of a polynomial bound for RF; no attack by another lane; no second implementation (gauntlet step 2: «only if the first
survives»); no Oink families; no L-LIT signature on §4.6; the de-tied Γ3(G_k) of §3.3 is a sketch. Dead ends of this box are in
docs/si/DEAD.md (h2, h3, h4, NH) with their instances.

## 6. Against TARGET.md (READING)
RF takes a parity game in TARGET §1's form (priorities are ranked injectively by S1, a sort), outputs (W_E, W_O) and positional
strategies for both players (D2 change 5), and is deterministic. TARGET §2 asks for a polynomial bound on every game: none is
proved or claimed. §3: no number beyond n-bit path sets and their signed weights (compared at bit cost) is built. §4: Lemma ACYC is a
restricted-class statement and would count for nothing under §4 even if refereed.

## 7. Files and checks
experiments/si/box109/: rf109.py (the candidate, standalone: `python3 rf109.py GAME.pg OUT.sol [--trace]`), n6.py (all rules of §3.1;
`python3 n6.py GAME.pg MODE`), fam109.py (families and tables), rand109.py, climb109.py, starts109.py, famrf109.py, tab109.py,
run109.sh (regenerates the tables of out/; the climbs, the random starts and the family search are not re-run by it, their
commands are in its last comment lines), check109.sh (about 10 s: the frozen rows of §3.2 are in this file line by line; N5's,
RF's, Howard's, NH's and h1's rows on small sizes are re-run and compared with out/, with a control; rf109.py against n6.py's
mode rf and harness verify.py on one game; 300 random games with a control; pinned in experiments/si/check.sh).
