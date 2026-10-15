# Packet for a human expert: an exact characterisation of the games psolB solves completely (RESULTS R2, T-A1)
Maintained by HUMAN-DESK. Prepared 2026-10-15 at trunk cb5bc6d. Whether this packet goes to anyone, and to whom, is the
owner's decision alone. Nobody outside the fleet has been contacted.

**Read this first.** The authors, both referees, the CHECKER and the literature check are all AI-model sessions in one
research fleet. **No human has checked any step.** Nothing is machine-checked in a proof assistant. "Signed" below means that
two independent AI referee sessions re-derived the proof in prose and ran their own exhaustive and random searches. The fleet
classes the result as a modest partial result ("a tighter analysis of a known algorithm"). It says nothing about whether
parity games can be solved in polynomial time.

Sources. HKP = Huth, Kuo, Piterman, "Fatal Attractors in Parity Games: Building Blocks for Partial Solvers", arXiv 1405.0386v2.
Theorem numbers are by order of appearance in that file, as the referee who indexed them read them (docs/referee-2/R2-TA1.md
header). HKP work in min-parity colours; everything below is in max-parity with priorities on vertices.
Full proof: docs/attr/TA1-proof.md, the version both referees signed (l-attr 57a1515, blob f58968f; identical on trunk).

## 1. The claim, as signed
**Conventions.** G = (V, V_E, V_O, E, pr), V finite, every vertex has a successor, self-loops allowed, pr : V → ℕ.
*Max-parity*: Even wins a play iff the largest priority seen infinitely often is even. p is a player and q is the opponent.
W_p(G) is p's winning region. For R ⊆ V, G ∩ R is a *subgame* if every vertex of R has a successor in R. All notions
relative to R use only edges inside R.

**Definitions** (TA1-proof.md §1).
- *Trap.* S ⊆ R is a trap for q in R if every q-vertex of S has all its R-successors in S, and every p-vertex of S has some
  R-successor in S.
- *Attractor.* Attr_p^R(X) is the usual p-attractor to X ∩ R inside R.
- *Monotone attractor* (HKP Def. 3, in max-parity). For d ≥ 0 and X ⊆ R, MAttr_p^R(X, d) is the least Z ⊆ R such that a
  vertex v ∈ R with pr(v) ≤ d is in Z as soon as (v ∈ V_p and some R-successor of v is in Z ∪ X) or (v ∈ V_q and all
  R-successors of v are in Z ∪ X). The target X is *external*: x ∈ X is in Z only if it is attracted in ≥ 1 move.
- *Recurrent set.* X ⊆ R is (p,d)-recurrent in R if X ≠ ∅ and X ⊆ MAttr_p^R(X, d). From every x ∈ X, p forces a revisit of
  X while seeing only priorities ≤ d. HKP call such X with X ⊆ pr^{-1}(d), d ≡ p, *fatal*.
- *psolB* (HKP Fig. 3, restated in max-parity). On the current game G', for each priority d occurring in G' (HKP: descending
  colours), with p = d mod 2: set X := pr^{-1}(d) ∩ V(G'). Repeat: if X ⊆ MAttr_p^{G'}(X, d), declare Attr_p^{G'}(MAttr_p^{G'}(X, d))
  won by p, remove it, and restart on the smaller game. Otherwise set X := X ∩ MAttr_p^{G'}(X, d), until X = ∅. psolB
  returns the residual game when every priority of G' yields X = ∅. HKP Thm 5(1) gives O(|V|² |E|) time.
- *psolQ* (HKP Fig. 5, stated in HKP's min-parity colours c(v) = M − pr(v), M even ≥ max pr). It is the same loop over colours b,
  ascending, with p = b mod 2. The start set is X := {v : c(v) ≤ b, c(v) ≡ b mod 2}, and MAttr(X) is replaced by the *layered
  attractor*: A := ∅; for d = p, p+2, …, ≤ max c(X): A := PMAttr_p(A ∪ {x ∈ X : c(x) ≤ d}, d). The permissive attractor
  PMAttr_p(T, d) (HKP Def. 6) is MAttr with eligibility "c(v) ≥ d or v ∈ T" and target T external. The fatal test is X ⊆ A;
  on success Attr_p(A) is removed, otherwise X := X ∩ A. Implementation: experiments/attr/psolq.py (l-attr).
- *Solves completely* (HKP Def. 8, class "Solved"): the residual game returned is empty.
- *(p,d)-peelable.* Let d ≡ p (mod 2), G ∩ R a subgame and pr(R) ≤ d. R is (p,d)-peelable if R = ∅, or there is a non-empty
  F ⊆ R such that R \ F is (p,d)-peelable and either
  (a) F = Attr_p^R(MAttr_p^R(X, d)) for some (p,d)-recurrent X ⊆ pr^{-1}(d) ∩ R, or
  (b) F = Attr_p^R(S) for some non-empty trap S for q in R with pr(S) ≤ d − 2 that is itself (p, d−2)-peelable.
  The recursion is on (d, |R|). R \ F is a subgame because it is the complement of an attractor.
- *PA\*\*(G)*: W_E(G) is (E, d_E)-peelable and W_O(G) is (O, d_O)-peelable, where d_p is the least d ≡ p with d ≥ max pr(V).
  Lemma 0: peelable at d implies peelable at d + 2, so the choice of d_p does not matter upward.

In words: each winning region can be emptied by repeatedly removing either (a) the attractor of a self-returning set of
top-priority vertices, or (b) the attractor of a closed sub-trap of lower priority that can recursively be emptied the same
way. Clause (b) is what an attractor decomposition (Zielonka; Daviaud-Jurdziński-Thejaswini, arXiv 2003.08627) allows and
fatal attractors miss, *unless the trap is closed in the current subgame*. Note that PA\*\* is defined in terms of the winning
regions, so stating it presupposes knowing W_E and W_O.

**Theorem T-A1.** For every finite parity game G, psolB solves G completely if and only if PA\*\*(G).

**Theorem T-A1'.** If PA\*\*(G), then psolQ solves G completely. The converse is false. One witness is HKP Fig. 4(a). The
smallest witness has 2 vertices: v0 has priority 0, belongs to Odd and has edges to v0 and v1; v1 has priority 2, belongs to
Even and has an edge to v0. Even wins both vertices. psolQ solves it and psolB does not, so by T-A1 it is not PA\*\*.

**Corollary 1.** HKP's Büchi games (Thm 7), games whose maximal SCCs each have constant priority (Thm 8) and deterministic games
(Lemma 5) all satisfy PA\*\*. This follows from HKP's completeness theorems plus the "only if" direction of T-A1. It is
a consequence of HKP's theorems, not a new proof of them. The Büchi class is HKP's only up to an order- and parity-preserving
recolouring, under which psolB is invariant.

**Corollary 2.** PA\*\*(G) is decidable in O(|V|² |E|) time: run psolB and test whether the residual is empty (HKP Thm 5(1)).
This is **not** a solver-free test (see Q2).

**Remark 3 (order independence).** For every colour sequence π that is stable in HKP's sense (Thm 6: appending any colour to
π does not change the output), psolB(π) solves G completely iff PA\*\*(G). This re-proves the completeness half of HKP Thm 6
without HKP's Lemmas 2–4.

**Not claimed.** Remark 4 of the proof file covers two stronger predicates PA ⊆ PA\* ⊆ PA\*\*, with strict inclusions on the
data. It is data only and was not signed.

## 2. Proof summary (details: TA1-proof.md §§3–5)
**Facts used.**
- F1, soundness of fatal attractors (HKP Thm 2). If d ≡ p, ∅ ≠ X ⊆ pr^{-1}(d) and X ⊆ W = MAttr_p(X, d), then p wins W
  and Attr_p(W). The hypothesis X ⊆ pr^{-1}(d) is necessary.
- F1', soundness of psolQ's removals (HKP Thm 4; see §3, G11).
- F2, residual regions. If D = Attr_p^{G'}(Y) with Y ⊆ W_p(G'), then W_p(G' \ D) = W_p(G') \ D and W_q(G' \ D) = W_q(G').
  This is Zielonka's standard argument.
- F3, monotonicity of MAttr and PMAttr in the target set.
- F6, restriction. For R = W_p(G'), MAttr_p^{G'}(X, d) = MAttr_p^R(X, d) for X ⊆ R, and likewise for Attr.

**"Only if": psolB complete ⟹ PA\*\*** (§5). Take psolB's run D_1, …, D_m with empty residual G_m. By downward induction on k,
W_p(G_k) is (p, d_p)-peelable.
- A q-removal leaves W_p unchanged (F2).
- A p-removal D_k = Attr(MAttr(X_k, d_k)) lies inside R = W_p(G_{k−1}) by F1, and F6 lets it be computed inside R.
  - If d_k = d_p, it is an (a)-step.
  - If d_k < d_p, then S = MAttr(X_k, d_k) is a trap for q in R. S is (p, d_k)-peelable by one (a)-step and hence
    (p, d_p − 2)-peelable by Lemma 0, so D_k = Attr_p^R(S) is a (b)-step.
- In short, psolB's run read backwards is a certificate.

**"If": PA\*\* ⟹ psolB (and psolQ) complete** (§4). Fix a certificate for W_p.
- *List.* Flatten the certificate tree into a list L of disjoint members covering W_p: an (a)-piece is one member, and a
  (b)-piece is the list of its sub-trap followed by F \ S.
- *Invariant I.* For every level (R, d) of the certificate, each q-vertex of R has all its G-successors in R or in members
  listed earlier.
- *Observation O.* In any subgame G' reached from G by sound removals (in any order, by either player), a p-vertex of W_p ∩ V(G')
  has no successor among the removed vertices of W_p.
- *Lemma L1, the key lemma.* If W_p(G') ≠ ∅, let P be the first member of L not entirely removed. Then P is an (a)-piece
  whose recurrent target X satisfies: X ∩ V(G') is still (p,d)-recurrent in G'.
  - The proof is a rank argument on the attractors.
  - Members of the form F \ S cannot be first. Their minimal-rank surviving vertex would lose all its successors (q-vertex,
    by I) or have its witness removed (p-vertex, contradicting O).
  - For (a)-pieces, the monotone attractor computation transfers rank by rank to G'.
- So any residual with W_p ≠ ∅ still contains a non-empty recurrent set at some occurring priority d. psolB's greatest-fixpoint
  loop at d keeps every recurrent subset of pr^{-1}(d) (F3), so psolB would not have stopped.
- For psolQ (T-A1'): its removals are sound (F1'), so L1 applies. The start set at the colour of d contains X'. The last
  layer of the layered attractor is a PMAttr whose target contains X', hence contains MAttr(X', d) ⊇ X'. So psolQ's
  iteration never drops X' either.
- Neither direction uses the order of psolB's colour loop, which gives Remark 3.

## 3. Gaps (union of both referees' lists; status at the signed commit plus the first referee's later answer)
| gap | content | status, and who closed it |
| --- | --- | --- |
| G1 | F2 (residual regions) used as standard | closed: written out by REFEREE-2 (R2-TA1 §2) and by the first referee (its §2); citable as Zielonka 1998 §3 |
| G2 | external target in MAttr; rank of X-vertices in L1(ii) | closed by both referees (nothing needs rank 0) |
| G3 | F6 equality MAttr^{G'} = MAttr^{W_p(G')} | closed: REFEREE-2's derivation from F1; first referee machine-checked it for every X ⊆ W_p on 324 + 40,000 + 1,500 games |
| G4 | psolB's colour loop order | closed by Remark 3 (only "every colour tried, restart after removal" is used) |
| G5 | choice of d (Lemma 0) | closed; the converse of Lemma 0 is unproved and unused (REFEREE-2 side check on 4,000 games) |
| G6 | empty members of the list L | closed (skipped by the "first member not removed" choice) |
| G7 | scope: finite games, successors everywhere, self-loops | closed |
| G8 | monotonicity of layeredAttr used in T-A1' | closed: only one PMAttr layer's target monotonicity is used; monotonicity of layeredAttr as a whole is not claimed |
| G9 | HKP Thm 2 (F1): its proof in HKP is a one-paragraph sketch | closed by REFEREE-2's written argument (agreed by the lane and the first referee) |
| G10 | Corollary 1 depends on HKP's proofs of Thm 7, Thm 8, Lemma 5 | **open**: a dependency on published proofs. Both referees re-derived them informally, without HKP Thm 6, whose proof rests on Lemmas 2–4, given as sketches. HKP Thm 7's Büchi fixpoint correspondence itself is taken from the source |
| G11 | HKP Thm 4 (F1'), used only by T-A1': HKP's proof is a sketch | **closed at referee level only with a correction to HKP's proof** (below). REFEREE-2 found the defect and the repair; the first referee confirmed both in writing (referee 5ff8edb) and re-derived Thm 4 with the repair |
| black box | HKP Thm 5(1) running time (Corollary 2) | used as stated, not re-derived |
| prose only | Invariant I, O, L1, the "only if" induction, Lemma 0, G9–G11 | prose re-derivations by two AI referees; machine checks cover the theorem's extension on searched games only |
| source | DJT §2 (trap definition) not opened by the first referee | the definition is stated in full in TA1-proof §1 and matches HKP Def. 2 |

**The HKP Thm 4 strategy issue** (docs/referee-2/R2-TA1/hkp_thm4_strategy.py; reproduced by the first referee and by the
CHECKER). HKP's proof of Thm 4 (fatal layered attractors are winning) defines p's strategy as "select the successor with
minimal rank r" (arXiv tex lines 1085–1088, as cited by the referees). In HKP's min-parity colours, take player 0 = p and:
- w has colour 0; v and u have colour 1; all three belong to player 0;
- edges v → {w, u}, u → {w, v}, w → v; X = {w}.

PMAttr_0({w}, 0) adds v and u at stage 1 and w at stage 2. So r(v) = r(u) = (0,1) < r(w) = (0,2), and X ⊆ layeredAttr is
fatal. Player 0 wins every vertex. But the minimal-rank rule moves v → u and u → v, and the play v u v u … has minimal
colour 1 infinitely often, so player 0 loses it.
- Repair: move to a *witness* successor, one in X_d ∪ A_{d−2} ∪ A_{d,i−1} for r(v) = (d,i). With this choice HKP's
  induction goes through (R2-TA1 §8; first referee's G11 answer).
- The statement of Thm 4 is unaffected, and T-A1' uses only the statement. The lane's psolq.py records witness successors.
- No fleet member has checked whether this issue is known (Q3).

## 4. Evidence
**Referee signatures.** Both referees signed the same commit, l-attr 57a1515 (TA1-proof.md blob f58968f).
- REFEREE (first): OK, docs/referee/2026-10-14-TA1-proof-check.md, signature at referee d1e065b; G11 answer and
  reconfirmation at referee 5ff8edb (append-only).
- REFEREE-2 (independent; wrote its report without reading the first): OK, docs/referee-2/R2-TA1.md §8, at referee-2 2eb1a2d.
- Earlier rounds found and fixed real defects:
  - a missing hypothesis in F1;
  - an unlisted dependency on HKP Thm 4;
  - a circular routing of Corollary 1;
  - a false "psolQ iff" claim, refuted by the 2-vertex game in §1.

**Machine searches** (each side used its own code).
| who | games | result |
| --- | --- | --- |
| REFEREE-2 (own code, docs/referee-2/R2-TA1/) | exhaustive n = 1, 2, 3 with priorities 0..n, all owners, all successor sets: 4 + 324 + 175,616; random n = 4: 250,000; n = 5: 60,000; n = 6: 5,000. Total 490,944 | T-A1 both directions and T-A1' hold on all. "psolQ complete ⟹ PA\*\*" fails (e.g. 6 of 324 at n = 2). psolB's residual is the same for descending, ascending and random colour orders. psolB is sound against Zielonka |
| REFEREE (own code, docs/referee/scratch/) | all 3-vertex games, plus probes of F6/Lemma 0 | agrees |
| L-ATTR (lane, experiments/attr/) | all 41,440 canonical 3-vertex games; 2 × 20,000 random n = 4; 1,500 + 3,000 random n = 5 | PA\*\* ⟺ psolB-complete holds |
| L-ATTR | all 27,331,200 canonical 4-vertex games, psolQ-failure side only | PA\*\* is false on all 75,856 psolQ failures, consistent with T-A1'. This covers all 4-vertex games only under relabelling invariance of PA\*\*, which itself follows from T-A1 |
| REFEREE-2 compare_lane.py | lane vs referee code on 324 + 175,616 exhaustive and 23,000 random games | psolB residual, psolQ residual and PA\*\* identical |

**CHECKER** (docs/checker/C1-report.md, checker 62cf1c4). The first pass FAILED on two points:
- missing gap entries in the RESULTS text;
- the two referees' G11 closures differed.

After the RESULTS edit and the first referee's written G11 answer, the re-check PASSED at trunk 4b9cb6e:
- blob identity of every signed file;
- statement diff against the signed text;
- vocabulary;
- re-runs of 9 of 9 listed computations on the exact signed commits, with identical output;
- the gap list.

The CHECKER makes no mathematical judgement.

**Novelty (L-LIT, docs/lit/T8-TA1.md).** Verdict "NEW": no source found that states this class or an equivalent one.
Sources opened:
- HKP;
- Ah-Fat and Huth, "Partial Solvers for Parity Games: Effective Polynomial-Time Composition", arXiv 1609.04085 (GandALF 2016),
  whose Conclusions say "we do not, at present, have a good understanding of what types of parity games are solved completely
  for certain partial solvers. More powerful versions of Theorem 1, which extend to classes of 2-player games, would be a
  first step in addressing that weakness";
- Vester, "Winning Cores in Parity Games", arXiv 1602.01963;
- Bruyère, Pérez, Raskin, Tamines, arXiv 1907.06913;
- arXiv keyword and author searches.

**Limits of the novelty check.**
- **T8 checked an earlier, stronger predicate, PA (l-attr fdb5092), not PA\*\*.** Nobody has re-run a novelty check
  specifically for PA\*\* or for the exact "iff". The sources searched are the same.
- T8's finding that PA misses HKP's Büchi and SCC-constant classes does not apply to PA\*\*, which contains them (Corollary 1).
- Not checked: citers of HKP beyond the arXiv hits, and HKP's FoSSaCS 2013 conference version.
- L-LIT's own assessment of the value, made for PA: "low-medium".

## 5. Open questions for the expert
1. **Is the characterisation known?** Is PA\*\*, or the statement "psolB solves G completely iff PA\*\*(G)", or an equivalent
   characterisation of HKP's class Solved, already in the literature (papers citing HKP, Vester's winning cores, the FoSSaCS
   2013 version, theses)?
2. **Is there a solver-free polynomial membership test?** Can PA\*\*(G) be decided in polynomial time without running psolB?
   What the fleet has tried:
   - PA\*\* is stated in terms of W_E and W_O, so even its statement needs the winning regions.
   - Two greedy canonical rules are sound but incomplete: at n = 3 they miss 4,266 and 48 games (docs/attr/A1-results.md §3).
   - The fleet's Lead reading L8 counts the class as "a new polynomial class" only if such a test exists, and records T-A1 as
     "a tighter analysis of a known algorithm".
3. **Is the HKP Thm 4 strategy issue known?** Has the minimal-rank strategy in the proof of HKP Thm 4 been noted or corrected
   elsewhere (an erratum, a journal version, follow-up work)? Is the witness-successor repair the intended reading?
4. **Is the result interesting?**
   - The "only if" direction reads a certificate straight off psolB's run. Is the characterisation more than a restatement of
     psolB's behaviour?
   - Does it say anything new about which games defeat fatal-attractor solvers? The fleet's reading is that a level of every
     decomposition has no piece that can go first, a "mutual escape" between the top attractor and a sub-trap.
   - Is it worth writing up in any form?
5. (Secondary.) Is there a natural exact characterisation of psolQ's complete class? The fleet only notes that the analogue of
   PA\*\* with layered attractors in clause (a) would be close to definitional.
6. (Secondary.) Do the 2-vertex counterexample to "psolQ complete ⟹ PA\*\*" and the order independence of Remark 3 match the
   expert's understanding of HKP Fig. 4(a) and Thm 6?

## Reviewer Q&A (verbatim)
Each entry: date (UTC), who asked, question verbatim, answer verbatim, who answered. Empty: no reviewer has been engaged.
