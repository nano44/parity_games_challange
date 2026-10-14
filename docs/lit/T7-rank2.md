# T7: barrier/novelty check for RANKING rank 2 (straight-line symbolic programs) (L-LIT, 2026-10-14)

Asked by the Lead 21:59Z. Sources opened for T7 are listed in notes/L-LIT.md (new: Parys RAIRO 2013 author copy;
Chatterjee-Dvořák-Henzinger-Loitzenbauer arXiv 1711.09148 v1; Chatterjee-Dvořák-Henzinger-Loitzenbauer arXiv 1706.04889 v1;
Jung-Kołodziejski arXiv 2406.01497 v1; Hella-Vilander arXiv 1912.08715 v1; plus T3 sources ANP, CDHS 1909.04983, JMT 2001.04333).

**Verdict: OPEN and not covered**, with one caution about the model. Straight-line programs are covered by no proven
lower bound beyond LINEAR, and that linear bound comes from a model much stronger than straight-line programs.
The super-polynomial question is open (ANP p.16; CDHS p.19). Super-polynomial bounds are impossible in the usual adaptive
symbolic model, so the rank-2 lane MUST use a restricted model like the one in §2.

## (a) What the existing frameworks cover (exact definitions)
1. **Arnold-Niwiński-Parys, CSL 2021 (LIPIcs.CSL.2021.9), Thm 5.1.** The model is the value ‖F‖_{U,V}, defined by recursion over two
   trees U, V that are fixed for all f. The function f: ({0,1}^n)^d -> {0,1}^n is monotone and is queried as a black box. Thm 5.1 (verbatim): "Let U, V be equitable trees of
   height h. (1) If ‖F‖_{U,V} = ‖F‖ for all fixed-point expressions over B^n of the form F = (Θ, f, (0, 1)), where |Θ|µ =
   |Θ|ν = h, then U and V are (n, h)-universal." Remark 5.5: the bound already holds when every output bit of f is an AND or OR of
   input bits, i.e. for game-induced f. Intro p.2: "While this is not an absolute lower bound for the black-box complexity
   like, e.g., in Parys [24], we show that any algorithm of the considered form must involve a universal tree".
   **Coverage:** only straight-line programs whose shape is the ‖·‖_{U,V} recursion with some trees U, V. Arbitrary DAGs of
   Boolean operations and Cpre calls are NOT covered.
2. **Parys, "Some results on complexity of µ-calculus evaluation in the black-box model", RAIRO-TIA 47(1):97-109, 2013**
   (DOI 10.1051/ita/2012030; author copy mimuw.edu.pl/~parys, "journal version"). The model is decision trees, i.e. ADAPTIVE
   algorithms, that query a monotone f: {0,1}^{nd} -> {0,1}^n given by an oracle. Thm 1.3: "For any natural n it holds
   num(2, {0,1}^n) = Ω(n^2 / log n)". The paper notes that allowing an arbitrary monotone f "weakens" the lower bound.
   Thm 1.1: for fixed lattice size the problem is polynomial in d. **Coverage:** adaptive, arbitrary monotone f with d = 2. It does
   not follow that the bound holds for game-induced f (AND/OR), and so it does not follow for symbolic programs on games.
3. **Chatterjee-Dvořák-Henzinger-Svozil, LPAR 2018 (arXiv 1909.04983 v1).** Set-based symbolic model: "the allowed symbolic
   operations are: (a) basic set operations such as union, intersection, complement, and inclusion; and (b) one step
   predecessor (Pre) operations". Upper bounds only (Thm 2, 3: quasi-polynomially many symbolic operations). p.19: "whether
   lower bounds can be established for symbolic algorithms for parity games is another interesting direction for future work."
4. **Jurdziński-Morvan-Thejaswini (arXiv 2001.04333 v2), "Symbolic algorithms" section (p.15-16).** Adopts CDHS's model:
   "any standard computational operations on any standard data structures are allowed, but there are also the following
   symbolic resources available: symbolic set variables ...; basic set-theoretic operations ...; the controllable
   predecessors operations". The resource is symbolic space, O(lg d) set variables, and there is no lower bound.
5. **Chatterjee-Dvořák-Henzinger-Loitzenbauer, SODA 2018 (arXiv 1711.09148 v1): the only symbolic lower bounds.** Model (§2):
   Pre/Post on arbitrary sets plus basic set operations, ADAPTIVE, with unbounded free computation; only one-step operations
   are counted. Thm 3.10: any symbolic algorithm solving Büchi(T) on graphs needs "(1) Ω(n) [one-step operations] even for
   instances with constant D". Thm 3.11 gives the same for safety and co-Büchi. The method is communication complexity (set
   disjointness). **Why this model cannot give more** (their p.2, verbatim): "every computable graph-algorithmic question can be
   solved with 2n symbolic one-step operations when storing O(n) many sets ... : For every vertex v perform a Pre and a Post
   operation, store the results, which represent the full graph, and then compute the solution on this graph". So in the
   adaptive model with arbitrary sets, parity games take O(n) one-step operations, and no super-linear lower bound is possible there.
6. **Modal-logic succinctness** (adjacent, NOT covering). Jung-Kołodziejski 2406.01497, Prop. 3, and Hella-Vilander 1912.08715
   (formula-size games; Remark 4.12 on DAG size) give lower bounds on formula size for equivalence over ALL structures. No source
   found addresses equivalence on structures with at most n states, which is what §2 needs.

L-LIT reading of the gap: rank 2 is meaningful only for programs that cannot name individual vertices. These are
programs built from the priority classes and the owner sets by Boolean operations and Cpre. They are exactly the DAG-shaped
modal formulas over ◇/□ and the propositions P_i, V_E, V_O. Such programs are automorphism-invariant, so the "learn the
whole graph" escape of item 5 is unavailable. Item 5's lower bounds DO transfer to them: a straight-line program is a
symbolic algorithm in that paper's sense, Cpre costs at most 2 Pre, and deciding s ∈ output costs nothing. So the known
picture is: lower bound Ω(n) (from item 5) and upper bound n^{lg(d/lg n)+O(1)} (from item 1's algorithms; see §2).

## (b) Model in TARGET vocabulary, and the first problem
**Definition (SLP).** Fix n >= 1 and d with 0 <= d <= n. A straight-line symbolic program over (n,d) is a finite sequence
X_1, ..., X_L. Each X_i is one of:
- a base set: P_0, ..., P_d (P_p = {v : pr(v) = p}), V_E, ∅;
- X_j ∪ X_k, X_j ∩ X_k or V \ X_j, with j, k < i;
- Cpre_E(X_j), with j < i, where Cpre_E(X) = {v ∈ V_E : E(v) ∩ X ≠ ∅} ∪ {v ∈ V_O : E(v) ⊆ X}.
(Cpre_O(X) = V \ Cpre_E(V \ X), so it needs no separate gate.) P solves (n,d) if for every parity game G of TARGET §1 with at most n
vertices and priorities in {0..d}, the value of X_L on G equals W_E(G). Cost c(P) = number of Cpre gates.
C(n,d) := min over programs solving (n,d). Boolean gates are free, as in item 5.
Known bounds (L-LIT readings; to be refereed as part of the lane's statement):
- Upper: C(n,d) <= n^{lg(d/lg n)+O(1)}. ANP's non-adaptive algorithm uses a number of queries proportional to the width of a
  universal tree (ANP abstract, Lemma 3.2/3.6). Each query to the game-induced f is one Cpre applied to a Boolean combination of
  the P_i, so it is an SLP. write B(n) for C restricted to Büchi games (priorities in {1,2} only, max-parity: Even wins iff 2 occurs
  infinitely often). B(n) <= O(n^2) by unfolding νZ.µY.((P_2 ∩ Cpre_E(Z)) ∪ (P_1 ∩ Cpre_E(Y))) with n iterations per
  fixpoint. (Priorities {0,1,2} would be a three-priority condition with three nested fixpoints, not Büchi.)
- Lower: B(n) = Ω(n), via item 5's Thm 3.10 on one-player games (V_O = ∅, T = P_2). Check before use: their graphs have
  out-degree >= 1 as TARGET requires.

**First problem (M3-sized; new as far as L-LIT found).**
Theorem target T7-1. B(n) = Ω(n^2 / polylog n). That is, every straight-line symbolic program that computes Even's winning
region on all Büchi parity games (priorities in {1,2}) with at most n vertices uses n^{2-o(1)} Cpre gates.
Fallback T7-1'. B(n) = ω(n), already on one-player games (V_O = ∅). Even n^{1+ε} would be the first super-linear
symbolic lower bound for any ω-regular objective. It would separate straight-line programs from the adaptive model, where
one-player liveness takes O(n) (item 5 p.2: the SCC-based O(n) algorithm of [GPP08]).
Why it is a sensible first step: it is the d = 2 case of the full question; Parys 2013 proves Ω(n^2/log n) for d = 2 in
an adaptive black-box model with arbitrary monotone f. T7-1 asks for the same order in a non-adaptive model with game-induced f.
Neither result implies the other. The method can be tried: adversary arguments as in Parys 2013 §§4-6, restricted to the
automorphism-invariant sets an SLP can compute.
The general goal it opens the way to (the real rank-2 result): C(n,d) >= n^{lg(d/lg n) - O(1)}, i.e. ANP Thm 5.1 for arbitrary SLPs.

**Small cases a search can check (L-COMP).**
- B(2) and B(3) exactly over chain programs: each Cpre argument is a Boolean combination of the previous Cpre output and the base
  sets. Program values are functions from (games with <= n vertices) to subsets of V. Quotient by graph isomorphism
  (at n = 3 there are about 2.2·10^4 games before symmetry reduction). Unrestricted SLPs are out of reach beyond n = 2:
  the free Boolean closure makes the branching doubly exponential. The data would be weak evidence, a sanity check only.
- Cheaper and more useful: implement the unfolded Büchi SLP and ANP's universal-tree SLP. Check them against Zielonka on all
  games with n <= 4. Search for any program with fewer Cpre gates that agrees on all of them, by local
  search / SAT over chain programs at n = 3, 4. A strictly smaller program found this way is real information.

## (c) Promise / cost versus rank 3 and rank 4 (L-LIT judgement, opinion)
| | rank 2 (SLP lower bounds) | rank 3 (Strahler threshold for psolQ / 2511.03752) | rank 4 (original Random-Facet) |
| --- | --- | --- | --- |
| contributes to M4? | no (negative evidence only) | no (explains a failure) | no (negative evidence) |
| M3 value if done | high for the general target (ANP Thm 5.1 for all SLPs), medium for T7-1 / T7-1' | low-medium ("tighter analysis of a known algorithm"; a characterisation of a partial solver) | high: closes a gap the field reopened (errata 1410.7871) |
| chance of a result in a few days | T7-1' (super-linear): low-medium; T7-1 (quadratic): low; general: very low | high: computational search plus a construction; the minimal undecided game is near-certain to exist (HKP Fig. 6 already defeats psolQ) | low: FHZ needed a long construction and still erred; Hansen's thesis (needed first) is 404 |
| compute cost | small (chain-program search at n <= 4) | small-medium (Strahler number + psolQ on all small games) | medium (simulation of Random-Facet on candidate games for evidence) |
| dependence | none | strongest if M2 shows 2511.03752 incomplete (then it explains why) | Hansen thesis / FHZ STOC text (not opened) |
| risk | proof technique may not exist; even linear-to-super-linear has no known method in this model | result may be judged minor | high: errors are easy (cf. the errata) |
Recommendation (L-LIT opinion): if M2 has a counterexample to 2511.03752 in hand, open rank 3 first: it is cheap and
near-certain, and it turns the M2 refutation into a statement about a whole family. If the second lane must be a barrier
lane, open rank 2 with the fallback T7-1' (one-player, super-linear) as the first target, and keep the quadratic and
general forms as stretch goals. Rank 4 last: it is highest-value but needs the unopened Hansen thesis and carries the most error risk.

## DONE / FINDINGS / NEEDS
- FINDINGS: rank 2 is uncovered: only ANP (tree-shaped) and the 2018 linear bounds apply. The adaptive symbolic model admits
  O(n) one-step algorithms (CDHL p.2), so the lane must use non-adaptive, vertex-anonymous programs. In that model the
  known bounds are Ω(n) <= C(n,d) <= n^{lg(d/lg n)+O(1)}, and for Büchi games the gap is n versus n^2.
- NEEDS: Lead: choose between rank 3 (if M2 has a counterexample) and rank 2 with T7-1'. REFEREE: the SLP definition and the
  two transfer readings (CDHL lower bound and ANP upper bound into SLPs) before a lane relies on them.
