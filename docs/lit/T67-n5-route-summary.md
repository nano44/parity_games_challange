# T67: one-page summary for the Lead: the N5′-xi route on Γ3 against the literature (T65, T66)
L-LIT successor, 2026-11-12 (date -u in the commit). Unrefereed. Not a TARGET.md claim; G-N5-TIME stays OPEN; DEEP3 stays a CONJECTURE.
Details, quotes and locations: docs/lit/T65-lamgap-one-player-howard.md, docs/lit/T66-deep3-lower-bound-families.md.
Labels: KNOWN (source) / IMPLIED (source + argument) / NEW (searched where) / CONTRADICTS (source).

## 1. Verdicts
| claim | label | by what |
| --- | --- | --- |
| LAM-GAP / SHARP: one-player Howard under VJ, a window with every Λ constant has b − a ≤ \|Ch\| (L-SI box 101 §2; L-RED R234 §3) | KNOWN for additive weights and for mean payoff; STATED without proof for parity games; proved inside the fleet in three forms | Cochet-Terrasson–Gaubert, shortest-path policy iteration, Theorem 2.3 (≤ n − 1 steps, tight); Zhong–Ye arXiv 2609.40147 Thm 7.2's proof («every N consecutive updates create a new cycle»); Friedmann thesis p.101 and Thm 4.9; landed R118 (c)/(d)/(i), R17 (b)/(c) |
| the same on one-player 1-sink games | IMPLIED | Cochet-Terrasson–Gaubert Thm 2.3 + the weight map of T65 §5 |
| the tight constant \|Ch\| with cycle nodes allowed to switch (no H0) | NEW, weakly (an elementary variant) | searched: T65 §4-§5 |
| L1-POLY: Howard on one-player parity games makes O(n²·\|Ch\|) iterations | KNOWN as a statement, no published proof opened | VJ00 BRICS RS-00-48 Prop. 7.4 (O(n³)); Friedmann thesis Thm 4.9 ([Vög00], not opened) |
| LAM-GAP vs the lower bounds for Howard on deterministic MDPs | no CONTRADICTION | Hansen–Zwick, Asadi et al., Zhong–Ye count new cycles (gains); under VJ the gain is the top vertex Λ, ≤ n values per vertex |
| Hansen's Conjecture 6.1.1 (Howard ≤ #edges) | claimed REFUTED by an unrefereed preprint | Zhong–Ye Theorem 6.1 (p.23-24): exp(Ω(N)); proof not checked here |
| Friedmann's G_n (and every other published exponential family) lives in the genome class | NO | E-DOM: [F11] Table 4 has f_j, k_j odd above h_i (i < j), used in Lemma 6.6 (2); agrees with L-RED 54's DEAD port (R217 §7) |
| DEEP3 vs the known lower bounds | no CONTRADICTION; no literature test | on G_N itself Deep_c is exponential (DATA, N ≤ 8) while every other chain link holds |

## 2. For the chain table (L-SI box 101 Addendum A)
- The link «LAM-GAP» can be replaced by landed statements. On Γ3 no mover is a cycle node (R125 (e)), so H0 is automatic.
  - Option A: global windows. R118 (l) + R125 (c): T3 ≤ (C + R + 1)(N + 1). With TWO-CROSS and DEPTH-COUNT3 (lane; R234's D1 fix):
    polynomial T3 ⇐ «Deep_c over all gates and the whole run is polynomial». No SCC-RED, ONE-CROSS3, WINDOW, LAM-GAP.
  - Option B′: per SCC, R118 (d) + (l) on the sub-genome of Reach(C) (one unrefereed restriction paragraph): Gap(C) ≤ N.
  - Option B: LAM-GAP / SHARP + W1 as a new lane lemma: Gap(C) ≤ N_C.
- Box 101 §0-§1: «Hansen's conjecture is OPEN» → «a preprint (Zhong–Ye, 2026-10) claims a refutation; irrelevant to the VJ case».

## 3. For DEEP3 (L-SI box 102, L-RED 66)
- DEEP is the only chain link that fails on Friedmann's games. Its proof must use E-DOM (every e even and above every β) or another
  genome-only property. Test for a proof draft: run each step on G_N with docs/lit/T66-depth-check.py; the failing step is the one
  that must use the genome structure.
- The literature has no E-DOM-compatible counter (none found). The fleet's own abstract results point at the same place: ascents
  (L-NEW box 193 ASC-EXP; R125 CHAIN3 for U(G) ≤ B) and LEAK-ARCH (R217 §11).

## 4. Not opened (reported, not paraphrased)
Hansen–Zwick ISAAC 2010 (paper; slides opened), Hansen's thesis (Wayback snapshot exists, host unreachable here), Vöge's thesis (403),
Madani AAAI 2002 (403), the FHZ papers.

## DONE / FINDINGS / NEEDS
- DONE: T65, T66, docs/lit/T66-depth-check.py, this page.
- FINDINGS: §1-§3.
- NEEDS: Lead: choose A / B′ / B; relay §3 to L-SI and L-RED. Owner: nothing (optional library: the three theses / papers of §4).
