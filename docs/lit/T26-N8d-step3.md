# T26: gauntlet step 3 for N8d-R2, Koh-Loho tree SI with a uniformly random single switch (L-LIT, 2026-10-23)

Asked by the Lead at 07:49Z (date -u). The object:
- **Statement:** docs/new/N8d-barrier.md (L-NEW 264b38b, draft for sign-off).
- **Rule R2:** docs/new/N8d-single.md §0 (frozen at d7fadfb). Each iteration draws a uniformly random Odd node among those with an
  admissible arc; that node takes its largest-Tighten admissible arc.
- **Method:** Koh-Loho Algorithm 1 over the perfect (n, d/2)-universal tree.

Every source below was opened by L-LIT in this session; sha256 values are in notes/L-LIT.md. Page conventions:
- Friedmann thesis: "p." is the printed page; PDF page = printed + 16.
- Other sources: "p." is the printed page unless marked.
- "L-LIT reading" marks interpretation.
- L-NEW's file is not edited. Corrections are caveats to the Lead.

**Verdict (step 3): SIGN WITH CAVEATS 1-7 (§4).**
- No published lower bound covers R2.
- Nearest framework: Random-Edge (Friedmann thesis Thm 4.76) and its generalization, Thm 4.78 (oblivious randomized rules).
  - L-NEW's table misses Thm 4.78.
  - On Friedmann's own game G_n, R2's selection IS Random-Edge exactly.
  - So R2 stays outside only through the switch set, i.e. the valuation.
- L-NEW's claim (the transfer breaks only at Lemma 4.75) holds in substance, with three mechanical steps added (§2).

## 1. Row-by-row check of N8d-barrier.md §1
| L-NEW row | opened source | check |
| --- | --- | --- |
| B8 deterministic rules | Friedmann 1106.0778 Thm 6.14, 8.4 (re-opened T25); 0901.2731 Thm 8, §6; Avis-Friedmann 1305.3944 Thm 4: "The sequence Pn of improving switches followed by Algorithm 2 in Gn from the initial strategy ... has length at least 2^n" (sha256 d1fafb8b…) | **correct**. All deterministic, VJ valuations, fixed start. R2 is randomized |
| B9 DLMM index rules | 2512.16684 v2 Thm 4.3 (BARRIERS B9) | **correct**. R2 is not index-based |
| B10 Random-Edge, Thm 4.76 | Friedmann thesis (edoc.ub.uni-muenchen.de/13294/1/Friedmann_Oliver.pdf, sha256 68748f5388a94151… = L-NEW's and R54's). §4.7.2 p.168: "among all improving switches chooses one uniformly at random". Table 4.19 p.184. Lemma 4.74, 4.75, Thm 4.76 **p.186** | **correct in substance**: both halves verified in §2. Page wrong (caveat 4) |
| B10 FHZ Random-Edge / Random-Facet / Random-Facet* | thesis Table 4.4 p.96 (concrete Random-Edge lower bound 2^Ω(n^(1/4)), FHZ). Thm 4.71 p.183: MDPs with O(n^4) vertices and edges, Ω(2^n). Errata arXiv 1410.7871 v1 (sha256 d89ec8c3…) p.1: "The main result of [1] is thus flawed" (Random-Facet); p.2: the Random-Edge work "remains unaffected" | **correct**. R2 is not facet-based |
| B11 symmetric SI | BARRIERS B11; T25 §3 | **correct** |
| B12 PSPACE path prediction | BARRIERS B12 | **correct** |
| B13 LCP, B14 AUSO | BARRIERS B13, B14. Thm 4.76 table: abstract lower bound 2^Ω(n^(1/3)) (Matoušek-Szabó). **Newer:** Hansen-Zwick, ICALP 2016, LIPIcs.ICALP.2016.51 (sha256 ac500016…), abstract: AUSOs "on which Random-Edge performs an expected number of 2^Ω(√(n log n)) steps" | **correct**: KL runs are not cube walks, since strategies recur with larger µ (KL p.24:9). **Add** Hansen-Zwick to the row (caveat 5) |
| B1/B2, B3 | T25 §3 | **correct** (same method as N8a) |
| B4-B7 | T25 §3 | **correct** |
| HMZ 1008.0530 Thm 6.5 | v1 (sha256 f53a6b51…) Thm 6.5: "The Strategy-Iteration algorithm, starting from any initial strategy, terminates with an optimal strategy after at most (m + 1)(1 + log_{1/γ} n²/(1−γ)) = O(m/(1−γ) · log(n/(1−γ))) iterations" | **correct**. An upper bound for discounted switch-all. R2 has no discount, and µ is not a function of τ |
| B15-B21 | BARRIERS | **correct**, not applicable |
| KL lower bounds | T25 §1 (KL 2108.13338 v5 p.24:3; MFCS p.63:3; 2 citers; Loho's list; Ohlmann thesis Ch. 9 §2.3) | **correct**: none published. Fleet data (R53, R54, N8d-R1) are DATA |

## 2. The B10 claim, both halves
**(a) Selection coincides with Random-Edge: verified, and in fact on ALL of G_n.**
- Friedmann's parity game G_ζ (Table 4.19, p.184): every player-0 node (the improver) has out-degree at most 2.
  - w_i: {w_{i+1}, A_i}; u_i: {u_{i+1}, d_i};
  - a_{i,j}, b_{i,j}, c_{i,j}: 2 each;
  - d_i, y_i, x_i, r, s, t: 1 each.
  - Player-1 nodes are A_i (2) and B_i (3).
- At an out-degree-2 node, an improvable node has exactly one improving edge. Its current edge cannot be admissible, because µ is
  feasible in G_τ (KL §3).
- So "uniform node with an admissible arc" equals "uniform admissible edge", and the largest-Tighten choice is vacuous.
- R2 is then the Random-Edge instance of Friedmann's oblivious randomized rule Improve_P: p_n(1) = 1, §4.7.3 p.188-189. That
  family is stated for binary out-degree.
- Off binary games, R2 differs from Random-Edge (node-uniform, not edge-uniform) and is not an Improve_P rule.
- The coincidence is conditional: it holds only if R2 sees the SAME switch set. That is half (b).

**(b) The transfer fails only at Lemma 4.75: correct in substance. The thesis's own structure:**
- p.186: "All other proofs rely on Table 4.17 and Lemma 4.68, hence we transfer our main theorem to the parity game world".
- Lemma 4.75 restates the MDP Lemma 4.68 for the parity game. Its only justification: "the valuations of the parity game nodes are
  essentially the same as the potentials in the MDP by dropping unimportant O(1) terms".
- The probabilistic counter analysis (noise bounds, Table 4.18, p.180-182; Thm 4.71) uses only the switch sets of strategies in the
  phases. With a Lemma-4.75 analogue for tree labels, it would carry over verbatim.

L-LIT reading: a tree-label port must also do three mechanical steps.
- **(i) Dualize.** Friedmann's improver is player 0 = even ("Player 0 wins if this priority is even", p.45). KL's improver is Odd.
  So the port is the dual game (owners swapped, priorities +1), and R2's DUAL run is the test.
- **(ii) Fix the start.** Use Lemma 4.74's start, σ(w*) = σ(s*) = 0, as τ_1. KL's default (first successor) is not it.
- **(iii) State the analogue per state.** KL's admissible set depends on (τ, µ), not on τ: µ is forced to increase and strategies
  recur. So the Lemma-4.75 analogue must hold for every µ reachable with τ in a phase, not per strategy.
  - (i) and (ii) are mechanical. (iii) is the real gap, and it is exactly L-NEW's point.

## 3. Positioning sentence (N8d-barrier.md §2)
L-NEW's sentence is honest, but it is not the strongest form. It understates how close R2 is to Random-Edge, and it misses Thm 4.78.
Proposed replacement:

> N8d-R2 lies outside every proved lower-bound framework we know of, for two reasons.
> First, every proved strategy-iteration lower bound fixes valuations that are a function of the current strategy (VJ,
> discounted or MDP values), and the construction controls their improving-switch sets. This covers B8-B12, Friedmann's
> Random-Edge bound (thesis Thm 4.76) and its oblivious-randomized extension (Thm 4.78).
> R2's switches are instead violations of a history-dependent, forced-increase least fixed point over a universal tree.
> Second, the universal-tree and separator bounds (B1-B3) bound only the value domain or tree-driven recursions. These bound
> Koh-Loho's pivots only from above.
> The selection rule itself is not the escape. On Friedmann's Random-Edge game G_n every improver node has out-degree 2, so
> R2 chooses exactly as Random-Edge does there.
> Hence Thm 4.76 would apply to R2 if, on the dual of G_n from Lemma 4.74's start strategy, the admissible arcs at every
> reachable (τ, µ) were those of Table 4.17. That is Lemma 4.75 for tree labels, and it is open.
> Thm 4.76's own parity transfer rests on Lemma 4.75, which the thesis justifies in one sentence.

Missing frameworks checked:
- **Thm 4.78 (§4.7.3 p.189):** "Policy iteration with oblivious randomized improvement rules for infinitary payoff games requires
  expected subexponential time". Missing from L-NEW; add.
- **Hansen-Zwick ICALP 2016:** AUSO only; add to the B14 row.
- **Random-node / "Random-Vertex":** none found.
  - Not in thesis Table 4.4 (p.96: Random-Edge) or §4.7.2-4.7.3, nor in the FHZ errata.
  - Web search found no random-node rule.
  - The only "random vertex" hit is the Matoušek-Szabó AUSO random START vertex, which is B14.
- **Dorfman-Kaplan-Zwick, ESA 2026 (LIPIcs.ESA.2026.140, sha256 981235e8…):** upper bounds only. O(n·2^n) for Switch-All and
  O(poly(n)·2^n) expected for Random-Edge on energy games; p.2 says "Comparable results were known only for binary games".
  Context, no lower bound.

## 4. Caveats
1. **Thm 4.78 is missing** from N8d-barrier.md §1-§2. Use the positioning sentence of §3.
2. **The parity half of B10 rests on a sketch.** Thm 4.76's parity transfer rests on Lemma 4.75. Lemma 4.75 has a one-sentence
   justification and no proof in Appendix A; the MDP twin Lemma 4.68 is proved there (Lemma 4.67-4.68, p.259-263, potential tables A.1-A.2).
   - Thm 4.78 has only a sketch either (p.187-188: the lower bound "transfers to all randomized multi-switch improvement rules" because the competitions "are won with even higher probability").
   - Record B10's parity rows as "theorem, transfer sketched". The MDP/LP rows (Thm 4.71, 4.73) are proved.
3. **The transfer has three steps, not one** (§2 (b)): dualize; Lemma 4.74's start as τ_1; the Lemma-4.75 analogue per state
   (τ, µ). Only the third is substantive.
4. **Page.** Lemma 4.75 and Thm 4.76 are on printed p.186 (PDF p.202), not p.187. The same slip is in N8d-barrier.md §0 and R54 §0.
5. **B14 row:** add Hansen-Zwick ICALP 2016 (2^Ω(√(n log n)) for Random-Edge on AUSOs). Matoušek-Szabó is no longer the best
   abstract bound.
6. **U1 is the decisive test and is buildable** from Table 4.19: h = 8n, g = 22n, ℓ_k = 25k²n (p.183), O(n^4) vertices (Thm 4.71).
   - The right test is structural, not a pivot count. Do the admissible-arc sets under tree labels match Table 4.17 along a run?
   - Counts are uninformative: Ω(2^n) in bit count n means about 2^(n^(1/4)) in size, and small n already gives ~10^3 vertices.
   - Route to L-RED box 23 or L-NEW.
7. **T25 C1 still applies.** The bench families are not built against tree labels beyond R53/R54. The switchbestexp ~n² fit is
   DATA (D1).

## Sign-off
L-LIT signs step 3 for N8d-R2 WITH CAVEATS 1-7.
- R2 is outside every proved framework only through its valuation. Its selection equals Random-Edge on G_n.
- The open question is a precise lemma: Lemma 4.75 for history-dependent tree labels.
