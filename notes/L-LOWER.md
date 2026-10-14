# L-LOWER notebook
Overwrite the top sections; append to "Sources opened" and "Dead ends".

## Resume point
2026-10-14 23:20Z. Task L1 (24h box from 23:01Z). Statement written: docs/lower/L1-statement.md (model Def. 1.3-1.4,
Lemma 2.1 direct Ω(n), Transfer 2.2 CDHL, Lemma 2.3 n^2 upper bound, Transfer 2.4 ANP with the CAUTION that ANP's
n^{lg(d/lg n)} bound is adaptive; target T-L1 = B_1(n) = ω(n)). Next: experiments/lower (evaluator, unfolded Büchi SLP,
ANP SLP vs Zielonka n ≤ 4; exhaustive minimum-cost search on the bisimulation quotient for n ≤ 3, then 4), then the report.

## Queue
1. experiments/lower/slp.py: SLP evaluator on pg.Game; unfolded Büchi SLP; ANP symmetric SLP with S_{n,h} trees.
2. check vs zielonka.brute_force on all games n ≤ 4 (Büchi, one- and two-player) and parity {0,1,2} n ≤ 3.
3. bisimulation quotient Q_n of all one-player Büchi pointed games with ≤ n vertices; exact B_1(n) for n ≤ 3 by search; n = 4 by SAT if feasible.
4. report: data, statement, proof route / obstruction. DONE/FINDINGS/NEEDS to the Lead.

## Things only I know
- The ANP asymmetric algorithm (Lemma 3.6) is a worklist, hence adaptive; the T7 reading "C(n,d) ≤ n^{lg(d/lg n)+O(1)}"
  for SLPs is not established by ANP's text. The symmetric recursion (Lemma 3.2) IS straight-line: |U|·|V| queries.
- With the "successor priority" query f'(x) = Cpre_E(∪_p P_p ∩ x_p) each ANP query is one Cpre gate; with the vertex-priority
  form g(x) = ∪_p P_p ∩ Cpre_E(x_p) it is d+1 gates. Exponent unchanged. Equivalence of the two nested fixpoints with W_E
  is standard but no primary source opened yet.
- Bisimulation invariance (L1 Lemma 1.5) lets the exact search run on the bisimulation quotient of all ≤ n-vertex games.

## Sources opened
| source (arXiv id / DOI) | result used (theorem / section) | opened on | note |
| --- | --- | --- | --- |
| Chatterjee-Dvořák-Henzinger-Loitzenbauer, arXiv 1711.09148 v1 (SODA 2018) | §1 p.1-2 model and the "2n one-step operations" remark; §2 Preliminaries (Pre/Post, Set Disjointness, Thm 2.1); Reduction 3.1; Lemma 3.4 (O(1) bits per one-step op); Reduction 3.9 (p.7); Thm 3.10 (p.7) and its proof (p.13); Thm 3.11; §4 upper bounds (Büchi O(min(SCC+D, |T|·D))) | 2026-10-14 | pdftotext of arXiv v1 PDF; Reduction 3.9 graph has out-degree ≥ 1 everywhere |
| Arnold-Niwiński-Parys, LIPIcs.CSL.2021.9 (DOI 10.4230/LIPIcs.CSL.2021.9) | §2 fixed-point expressions, f_{A,B}, trees, Prop. 2.5 (S_{n,h} universal, width n^{lg(h/lg n)+O(1)}); §3.1 definition of ‖F‖_{U,V} (cases (1)-(3)), Lemma 3.1, Lemma 3.2 (|U|·|V| queries), Remark 3.3; §3.2 Algorithm 1, Lemma 3.4, 3.5, 3.6 (worklist, |V| to |V|(1+nd) queries), Cor. 3.7; Thm 5.1; Remark 5.5 | 2026-10-14 | DROPS PDF; intro p.9:2 states the symmetric bound n^{2·lg(d/lg n)+O(1)} explicitly |

## Dead ends
(none)
