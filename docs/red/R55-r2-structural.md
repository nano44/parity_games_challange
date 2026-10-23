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

## 3. Friedmann's Random-Edge parity game G_zeta under R2 (Lead 07:49Z / 08:00Z, first priority; experiments/red/gzeta/)
- Generator gzeta.py, transcribed node by node from thesis §4.7.2: node sets V0, V1 (printed p. 185) and Table 4.19 (successors and
  priorities of t, w_{n+1}, u_{n+1}, w_i, u_i, A_i, a_{i,1}, a_{i,j+1}, x_i, r, s, d_i, y_i, B_i, b_{i,1}, b_{i,j+1}, c_{i,1}, c_{i,j+1});
  parameters h = 8n, g = 22n, l_k = 25k^2 n (T26 C6). Every player-0 node has out-degree ≤ 2 (checked by construction).
  Sizes / sha1: n 1: 67 vertices (c29864c792e0), n 2: 389 (d502e9eebc3e), n 3: 1346 (7ab7a133ae3c).
- Port steps: (i) DUAL run = Friedmann's improver (player 0) switching: kl_single.py's dual pivots; (ii) start: each player-0 node lists its
  "0" edge first (σ(u) = 1 iff u moves into its level, thesis §4.7.2), so kl's first-successor τ_1 is the all-0 strategy, our READING of
  Lemma 4.74's "σ(w*) = σ(s*) = 0" (the thesis does not list the other nodes); NOT a code deviation. (--order table gives the printed order.)
- R2 dual pivots (kl_single.py --rule r2, seeds 1-5, every run check_sol2 = Oink zlk OK, strategies verified; r2_gz{1,2,3}.txt):
  n 1: 63, 61, 60, 61, 60 (mean 61.0); n 2: 405, 421, 389, 408, 404 (mean 405.4); n 3: see §3b.
- Per-node switching (gzswitch.py): n 1 seed 1: 57 nodes switch, 51 once and 6 twice, 6 switches back to a 0-edge (first at iteration 57,
  c1,11); n 2 seed 1: 374 nodes switch, 354 once, max 5, 22 back-switches (first at iteration 5, w1). All 250 b-nodes and 88 c-nodes switch
  into their cycles. So the pivot count ≈ the number of cycle vertices (h + l_i + g summed: 55 at n 1, 370 at n 2): R2 closes the cycles
  essentially once and terminates; the B / C cycles never re-open as the binary counter of Table 4.17 requires (2^n increments through
  seven phases each).
- Item (iii) (admissible sets vs Table 4.17 state by state): NOT done as a formal check. Table 4.17's cells did not survive text
  extraction, and I did not transcribe the phase definitions by hand in this box. What the data shows: the run never reaches counter
  value 1 (cycles open at most a handful of times, no node switches more than 5 times), so the admissible sets have departed from Table
  4.17's by the end of the first increment at the latest. The exact first departing state is open.

### 3b. n = 3 and the faithfulness check (Lead 08:39Z; 2026-10-23 09:59Z by date -u)
- R2 dual pivots at n 3 (1346 vertices; kl_single.py, seeds 1-5; r2_gz3.txt; all check_sol2-verified): 1432, 1490, 1491, 1469, 1493 (mean 1475.0).
- Faithfulness of gzeta.py and the start: classic strategy improvement for player 0 with Vöge-Jurdziński valuations under Random-Edge
  (vj_re.py: L-SI's experiments/si/si.py Engine and its rule_random_edge, imported read-only; same all-0 start; regions vs Oink zlk;
  vj_random_edge.txt):
| n | vertices | VJ Random-Edge iterations, seeds 1-5 | VJ back-switches (cycle openings) | R2 dual pivots, seeds 1-5 (mean) |
| --- | --- | --- | --- | --- |
| 1 | 67 | 57, 57, 57, 57, 57 | 0 each | 63, 61, 60, 61, 60 (61.0) |
| 2 | 389 | 824, 782, 828, 842, 854 | 225, 204, 227, 234, 240 | 405, 421, 389, 408, 404 (405.4) |
| 3 | 1346 | 5420, 5192, 5270, 5214, 5218 | 2047, 1933, 1972, 1944, 1946 | 1432, 1490, 1491, 1469, 1493 (1475.0) |
- Under VJ / Random-Edge the cycles open and close thousands of times and the count multiplies by ×14.5 then ×6.3 per bit: the generator
  and start reproduce Friedmann's counter (in the reachable range; Thm 4.76's 2^n regime needs larger n). Under R2 on the same games the
  pivots stay ≈ the number of cycle vertices (55 / 370 / 1320) with few openings (≤ 22 at n 2): R2 does not follow the counter.

## 4. Status at box end (reading)
- No kill of N8d-R2. On Friedmann's own Random-Edge game, R2 closes each cycle about once and stops (pivots ≈ |cycle vertices|, linear in
  the game size), while VJ Random-Edge counts on the identical games. The transfer fails exactly where L-LIT T26 placed it (Lemma 4.75):
  tree-label admissible sets do not track VJ improving-switch sets. The first departing state is NOT located; it is now checkable by
  running VJ and R2 from the same strategy and comparing the switch sets step by step (Table 4.17 not needed).
- Forced-chain gadgets: an AND-join gate fails because the ratchet lets earlier raises pass it (§2); lap-count climbs reached 6 laps at
  n 22 (min over 5 seeds) against ~21 needed. Reason it blocks every gadget class tried (reading): a lapping counter needs a period whose
  every R2-reachable order keeps the cycle open; in all gadgets seen, some node's lap move becomes admissible before its prerequisites,
  and µ's history dependence makes min-gates useless for ordering within a period. Not a proof.
