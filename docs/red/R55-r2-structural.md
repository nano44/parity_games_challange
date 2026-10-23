# R55: toward a structural lower bound for N8d-R2 (random node, best arc), box 23 (L-RED successor 11; produced on Opus 5.5, D15 / L37)
Status: DATA plus readings, unrefereed. Started 2026-10-23 07:41Z (date -u) on the Lead's wake for box 23. Object as R54: kl_single.py
--rule r2 at l-new d7fadfb, unmodified (KL_DIR read-only extract); kl.py = l-new 4fd179c8. Every instance below verified as in R53/R54.

## 1. Literature (Lead item 2)
- Opened: Friedmann, PhD thesis LMU 2011 (edoc 13294, sha256 68748f53…, see R54 §0). It reproduces the Friedmann-Hansen-Zwick parity-game
  constructions: Random-Edge (Table 4.4, Thm 4.76 p. 187: ≥ 2^n expected improvement steps on G_n; "Con. Lower Bound 2^Ω(n^{1/4})
  (Friedmann, Hansen, Zwick)" in Table 4.4) and Random-Facet. The rules it lists are Random-Edge ("among all improving switches chooses
  one uniformly at random"), Random-Facet, Switch-Half, Least-Entered; NO random-NODE rule and no random-node lower bound.
- NOT opened: the FHZ STOC 2011 paper itself (DOI 10.1145/1993636.1993675): the ACM full text returns an HTML access page, and the
  author-page URLs tried return no PDF. Its parity-game content is cited here only through the thesis.
- Why the Random-Edge mechanism does not port verbatim (reading): (a) Random-Edge weights a node by its number of improving EDGES, and FHZ
  tune probabilities with parallel edges / lane lengths; under R2 every candidate node has weight 1 whatever its out-degree, so only
  node counts (lanes of nodes that must switch in sequence) can tune probabilities. (b) A delay lane in tree-SI does not reset: once its
  nodes have switched, µ keeps their raised labels (forced increase), so the lane delays only the FIRST lap unless every lane node also
  switches back each lap, and each switch-back is itself a move that R2 may make at the wrong time.

## 2. The R2 failure points of the H_0 period (traces, experiments/red/kl/ktrace_r2.py)
- Switch-all period of H_0 (dual, R53 §5): phase A = {3, 4, 8 → 6}, B = {7: 2 → 3}, C = {3: 6 → 11, 7: 3 → 2, 8: 6 → 1}, D = {4: 6 → 8}.
- Fatal early moves seen under R2: (i) 7's lap move B before A is complete (seed 1: after 3 alone, candidates {4, 7, 8}, 7 picked, all
  labels → ⊤); (ii) 4's move D before C is complete (seed 2 of the joined game, iteration 17).
- AND-join attempt (instances/r2join_h0E_n14.pg): 7's arc to 3 rerouted through a new dual-Even vertex E (dual priority 2) with arcs to 3,
  4, 8 (E's label = the minimum, i.e. "all three raised"). Switch-all still counts (56 = 4·14 dual pivots); R2 is unchanged (mean 13.56
  over 100 seeds vs 14.70 for H_0). Reason (trace): 4 and 8 already carry the top-component value of the NEW lap from their phase-D / start
  labels (1.0.0.0…), and A only raises them in a LOWER component (to 1.0.0.1…); 7's threshold is its own previous-lap label (0.0.1…), so
  min(3, 4, 8) passes it as soon as 3 alone moves. A min-gate cannot separate "switched in this period" from "switched in an earlier
  period", because the ratchet keeps every earlier raise.
