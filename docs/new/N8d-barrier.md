# N8d-R2: gauntlet step 3, barrier statement (L-NEW successor 5, Opus 5.5; box 16; draft for L-LIT sign-off)
Lead 07:42Z 2026-10-23 (date -u). Object: N8d-R2 = Koh-Loho strategy iteration with tree labels (arXiv 2108.13338, Algorithm 1 + Algorithm 3)
on the PERFECT (n, d/2)-universal tree, pivot rule R2 frozen at d7fadfbf (docs/new/N8d-single.md §0): each iteration, a uniformly random Odd
node among those with an admissible arc (an Odd arc violated w.r.t. µ) switches to its admissible arc with the largest Tighten(µ, vw).
No running-time claim is made here (D1). BARRIERS.md (B1-B21) and L-LIT T25 (step 3 for N8a, the same method with multi-switch rules) are
the starting point; rows they already settle are cited, not re-opened.

## 0. Sources opened in this box (2026-10-23)
- O. Friedmann, "Exponential Lower Bounds for Solving Infinitary Payoff Games and Linear Programs", PhD thesis, LMU Munich 2011,
  edoc.ub.uni-muenchen.de/13294, PDF sha256 68748f5388a94151… (same file as L-RED R54 cites): §4.7.2 (Random-Edge definition: "among all
  improving switches chooses one uniformly at random"; Table 4.4: single-switching, probabilistic, oblivious; concrete lower bound
  2^{Ω(n^{1/4})} attributed to Friedmann-Hansen-Zwick; abstract lower bound 2^{Ω(n^{1/3})} Matoušek-Szabó on AUSOs), Lemma 4.75 and
  Theorem 4.76 (p.187: "Parity game strategy iteration with RANDOM-EDGE-rule requires at least 2^n expected improvement steps on G_n";
  Lemma 4.75: "The improving switches from strategies in the parity game that belong to the phases are exactly those specified in
  Table 4.17", justified because "the valuations of the parity game nodes are essentially the same as the potentials in the MDP").
- Opened earlier in this session and reused: Koh-Loho arXiv 2108.13338 (sha256 21ee0e4336252f7e; §1 p.24:3, §3 Algorithm 1 and Theorem
  3.1, "a strategy τ may occur more than once"); HMZ arXiv 1008.0530 v1 (sha256 f53a6b5127d95078; Theorem 6.5); Avis-Friedmann arXiv
  1305.3944 (sha256 d1fafb8b5d0b822c; Theorem 4); Canavoi-Grädel-Rabinovich arXiv 1210.2459 (sha256 02fca6a45515f2ec; abstract).
- Settled elsewhere and cited: BARRIERS.md rows B1-B21 (L-LIT, sources and sha256 in notes/L-LIT.md); L-LIT T25 (docs/lit/T25-N8a-step3.md:
  no published lower bound for Koh-Loho SI under any pivot rule; its two citers checked; Ohlmann thesis Thm 9.1); L-RED R53 (docs/red/
  R53-n8a-counter.md) and R54 (claude/l-red, docs/red/R54-n8d-r2.md).

## 1. Framework by framework
| framework | R2 inside? | exact reason | source |
| --- | --- | --- | --- |
| B8 deterministic SI rules (switch-all, switch-best, Zadeh, Cunningham, Friedmann's locally/globally optimal) | **outside** (by model and by kind) | R2 is randomized; every B8 bound is for a deterministic rule on VJ (or discounted / MDP) valuations from a fixed start. The fleet's own data confirm the danger is real for deterministic single switch on tree labels: N8d-R1 (lowest index) is exponential on Friedmann's switchallexp (≈ 9·2^N, N8d §3) | BARRIERS B8; Friedmann 1106.0778 Thm 6.14, 8.4; Avis-Friedmann 1305.3944 Thm 4; N8d-single.md §3 |
| B9 index-based single-switch rules (DLMM) | **outside** | B9 covers deterministic rules ranking edges by a global index with o(m/log m) memory. R2 draws the node at random and picks the arc by a LABEL comparison (largest Tighten), not by an index | BARRIERS B9 (arXiv 2512.16684 v2 Thm 4.3) |
| B10 Random-Edge on VJ valuations (Friedmann thesis Thm 4.76) | **outside as a theorem; nearest framework** | Two differences. (i) Selection: Random-Edge draws a uniformly random improving EDGE; R2 draws a uniformly random improvable NODE and takes its best-Tighten arc. On Odd nodes of out-degree 2 (one admissible arc at most besides τ(v)) the two distributions coincide; with larger out-degree they differ. (ii) Valuation, the decisive one: Thm 4.76's proof transfers the MDP counter to parity games through Lemma 4.75, i.e. the improving-switch sets of the phases are those of Table 4.17 BECAUSE the VJ valuations equal the MDP potentials up to O(1) terms. R2's admissible arcs are violations w.r.t. a least fixed point µ over the tree that is forced to increase and depends on the history (strategies may recur, Koh-Loho §3), so Lemma 4.75 has no counterpart. Whether G_n (or a port of it) produces the same switch sets under tree labels is UNKNOWN: G_n is not in the fleet bench, and R54 did not port it (L-RED box 23 is attempting a structural random-node lower bound) | Friedmann thesis §4.7.2, Lemma 4.75, Thm 4.76 p.187; R54 lines 12-14 |
| B10 Friedmann-Hansen-Zwick randomized rules: Random-Edge 2^{Ω(n^{1/4})} on LPs/MDPs; Random-Facet (parity bound WITHDRAWN, errata 1410.7871); Random-Facet* | **outside** | Random-Edge (FHZ): same two differences as the row above (it is the MDP/LP form of the same construction, thesis §4.7.2). Random-Facet / Random-Facet*: different rule (recursive facet choice); R2 is not facet-based | BARRIERS B10; Friedmann thesis Table 4.4, §4.7.2 |
| B11 symmetric SI (DLM) | **outside** | only Odd's strategy is maintained; Even's counterstrategy is read off µ; one-sided | BARRIERS B11; T25 §3 |
| B12 PSPACE-completeness of all-switches path prediction | **outside** | proved for VJ all-switches SI; R2 is single-switch, randomized, tree-labelled; not an iteration bound anyway | BARRIERS B12 |
| B13 LCP pivoting, B14 AUSO walks | **outside** | no LCP; Koh-Loho runs are not walks in a unique-sink orientation of the strategy cube (a strategy may recur with a larger µ), so AUSO bounds (incl. Matoušek-Szabó for Random-Edge, thesis Table 4.4) do not even have a model to transfer to; B14 already says they do not transfer to games | BARRIERS B13, B14; Koh-Loho §3 |
| B1/B2 separating automata, universal trees / graphs (CDFJLP 1807.10546 Thm 5.1; CFGO) | **outside, by model** | these bound the SIZE of the value domain (|L(T)| ≥ quasi-polynomial for any universal tree) and hence value iteration over it. Koh-Loho SI uses the tree only as a value domain; each pivot jumps to a least fixed point, so |L(T)| bounds iterations only from ABOVE (n·|L(T)|, Theorem 3.1's proof), not from below. Here the tree is the perfect one, |L(T)| = n^{d/2}: the only proven upper bound is exponential | BARRIERS B1, B2; T25 §3 row B1/B2; Koh-Loho p.24:3 |
| B3 ANP tree-driven nested fixpoints | **outside** | Koh-Loho reads the explicit graph (SCCs, base nodes, Dijkstra, strategies), not a black-box monotone f with fixed trees | BARRIERS B3; T25 §3 |
| B4-B7 attractor / dominion families | **outside the class** | R2 is SI; completeness is Theorem 3.1; the B5/B6 families are in the bench (all verified, polynomial-looking, N8d §5) | BARRIERS B4-B7; N8d-single.md §5 |
| HMZ 1008.0530 Theorem 6.5 (strongly polynomial SI for fixed discount) | **does not apply** (it is an upper bound, not a barrier, and its hypotheses fail) | It concerns Strategy-Iteration (switch-all) on DISCOUNTED 2TBSGs, with values a FUNCTION of the strategy profile and a bound O(m/(1−γ)·log(n/(1−γ))). R2 has no discount, is single-switch, and its µ is history-dependent (not a function of τ), so neither the hypothesis nor the potential argument (Lemmas 6.1-6.4 compare values of strategy profiles) carries over. The lane's screening principle derived from it (N6/N7: discounted-reduction methods need a γ-free argument) is irrelevant here: R2 uses no discount | HMZ Thm 6.5, Lemmas 6.1-6.4; notebook screening principle |
| B15-B21 (IPM, weak separators, complexity classes, Howard/discount, LDT, deep traps, JS-LCP IPM) | **outside / not applicable** | no LP path, automaton, discount, weight compression (labels are O(d log n)-bit tuples, compared lexicographically) or IPM | BARRIERS B15-B21 |
| Lower bounds for Koh-Loho / SI on universal trees | **none for R2** | Published: none for any pivot rule (T25 §1: paper, MFCS version, both citers, authors' list, web search). Fleet: R53's F_k/G_k/H_k and N8a's L_k are exponential for the MULTI-switch rules (switch-all, global) on the perfect tree; R54: under R2 the H_k counter dies (≈ 14.7 pivots over 200 seeds, flat in k); N8d-R1 (deterministic single switch) is exponential on switchallexp. No family is known on which R2's expected pivot count is super-polynomial | T25 §1; R53 §1-§5; N8a §6; R54; N8d §3 |

## 2. Positioning sentence (strongest honest form)
N8d-R2 lies outside every proved lower-bound framework we know of, because all proved strategy-iteration lower bounds (B8-B12, including
Friedmann's Random-Edge bound, thesis Thm 4.76) are for valuations that are a function of the current strategy (VJ, discounted or MDP
values), whose improving-switch sets the constructions control (Lemma 4.75), whereas R2's switches are violations of a history-dependent,
forced-increase least fixed point over a universal tree; and the universal-tree / separator lower bounds (B1-B3) bound the size of the
value domain or tree-driven fixpoint recursions, which bound Koh-Loho's pivots only from above. Its nearest framework is Random-Edge
(B10): on Odd nodes of out-degree two R2 selects exactly as Random-Edge would, so the open question is precisely whether Friedmann's
G_n (or a port of it) forces the same switch sets under tree labels; that is unknown and is L-RED's box-23 target.

## 3. What is unknown (stated, not hidden)
- U1. Friedmann's Random-Edge family G_n has not been run under R2 (not in the bench; R54 did not port it). It is the first instance to
  try; a structural port must reproduce Lemma 4.75's switch sets under tree labels.
- U2. No upper bound beyond n·n^{d/2} (perfect tree) is known for R2's expected pivots; with the JL/Strahler trees the bound would be
  quasi-polynomial by construction (not implemented, Lead: do not start).
- U3. The perfect tree's width n makes a lexicographic crawl cost up to n per tree level (N8a §5-§6): R2 escapes the known crawl
  gadgets because a single switch closes the odd cycle (R54); whether some gadget keeps an odd cycle open under EVERY single
  admissible switch is open.
- U4. Data caveat (T25 C1): the bench families were built against other algorithms; the evidence is not adversarial for tree labels
  beyond R53/R54's families.

## 4. T26 corrections (L-LIT T26 SIGN WITH CAVEATS, claude/l-lit docs/lit/T26-N8d-step3.md; applied 08:02Z by date -u; §0-§3 unchanged)
- **C4, page fix.** Lemma 4.75 and Theorem 4.76 are on printed p.186 (PDF p.202) of the thesis, not p.187 (§0 and §1 say p.187; the same
  slip is in R54 §0). Checked in L-NEW's copy (sha256 68748f5388a94151…): PDF p.202 carries both and is headed "186".
- **C1, Theorem 4.78 added (the B10 row of §1 should be read with it).** Thesis §4.7.3 ("Switch Half and all that", printed p.187-189,
  PDF p.203-205), Theorem 4.78 (printed p.189): "Policy iteration with oblivious randomized improvement rules for infinitary payoff games
  requires expected subexponential time". The rules are Improve_P for a probabilistic positive integer selector P = (p_n), "for
  simplicity, we assume binary out-degree here"; Random-Edge is p_n(1) = 1 (Algorithm 11, item 1). On binary out-degree games R2 IS this
  Random-Edge instance (an improvable node has exactly one admissible arc, so node-uniform = edge-uniform and the largest-Tighten choice
  is vacuous); off binary games R2 is node-uniform, not edge-uniform, and is not an Improve_P rule. Theorem 4.78's proof is a sketch
  (p.187-188: the bound "transfers to all randomized multi-switch improvement rules due to the fact that the two kinds of competitions ...
  are won with even higher probability").
- **C2/C3, status of B10's parity side: "theorem, transfer sketched".** Theorem 4.76's parity transfer rests on Lemma 4.75, justified in
  one sentence ("the valuations of the parity game nodes are essentially the same as the potentials in the MDP by dropping unimportant
  O(1) terms") with no proof in Appendix A; its MDP twin Lemma 4.68 is proved (pp. 259-263, per T26). The MDP/LP rows (Thm 4.71, 4.73)
  are proved. A port of G_n to R2 needs three steps (T26 §2(b)): (i) dualize (Friedmann's improver is player 0, Koh-Loho's is Odd: the
  test is R2's DUAL run); (ii) use Lemma 4.74's start strategy as τ_1 (kl_single.py's default, first successor, is not it); (iii) a
  Lemma-4.75 analogue for EVERY reachable (τ, µ) in each phase, since Koh-Loho's admissible set depends on µ, not only on τ. (i) and (ii)
  are mechanical; (iii) is the substantive open step. (The structural test, C6, is L-RED box 23's; not run here.)
- **C5, B14 row.** Add Hansen-Zwick, "Random-Edge Is Slower Than Random-Facet on Abstract Cubes", ICALP 2016, LIPIcs.ICALP.2016.51
  (PDF sha256 ac500016f9d73aed…, opened 2026-10-23), abstract: AUSOs of the n-cube "on which Random-Edge performs an expected number of
  2^{Ω(√(n log n))} steps", improving Matoušek-Szabó's 2^{Ω(n^{1/3})}. Still abstract cubes: not transferable to Koh-Loho runs (not cube
  walks; strategies recur with larger µ, Koh-Loho §3).
- **Positioning sentence: L-LIT's stronger form ADOPTED (replaces §2's sentence; §2 kept for the record).** I agree with T26 §3: the
  selection rule is not the escape, only the valuation is.
  > N8d-R2 lies outside every proved lower-bound framework we know of, for two reasons. First, every proved strategy-iteration lower
  > bound fixes valuations that are a function of the current strategy (VJ, discounted or MDP values), and the construction controls
  > their improving-switch sets; this covers B8-B12, Friedmann's Random-Edge bound (thesis Thm 4.76) and its oblivious-randomized
  > extension (Thm 4.78). R2's switches are instead violations of a history-dependent, forced-increase least fixed point over a
  > universal tree. Second, the universal-tree and separator bounds (B1-B3) bound only the value domain or tree-driven recursions,
  > which bound Koh-Loho's pivots only from above. The selection rule itself is not the escape: on Friedmann's Random-Edge game G_n
  > every improver node has out-degree 2 (T26 §2(a), Table 4.19), so R2 chooses exactly as Random-Edge does there. Hence Thm 4.76
  > would apply to R2 if, on the dual of G_n from Lemma 4.74's start strategy, the admissible arcs at every reachable (τ, µ) were those
  > of Table 4.17. That is Lemma 4.75 for tree labels, and it is open; Thm 4.76's own parity transfer rests on Lemma 4.75, which the
  > thesis justifies in one sentence.
- Unchanged and still applying: T25 C1 / T26 C7 (bench not built against tree labels beyond R53/R54; the switchbestexp ~n² fit is DATA).
