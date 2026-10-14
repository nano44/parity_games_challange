# T-A1: the class of parity games that psolB solves completely (L-ATTR; proof draft, revised 2026-10-14 23:55Z after REFEREE-2's report docs/referee-2/R2-TA1.md; first referee pending)
Vocabulary: TARGET.md section 1 (max-parity; G = (V, V_E, V_O, E, pr)). Solvers: psolB (HKP Fig. 3) and psolQ (HKP Fig. 5),
HKP = Huth, Kuo, Piterman, arXiv 1405.0386v2, implemented in experiments/attr/psolb.py and psolq.py (pseudocode with line
numbers in notes/L-ATTR.md). HKP work in min-parity; every HKP notion is restated here in max-parity (colour = M - priority;
"colour >= c" becomes "priority <= d"). Data: docs/attr/A1-results.md section 3. Gaps are listed in section 6.

## 1. Definitions
Players p, q = the opponent of p. For R ⊆ V, G ∩ R is the structure induced on R; it is a *subgame* if every vertex of R has a
successor in R. All notions below for a subgame G ∩ R use only edges inside R.
- Trap. S ⊆ R is a *trap for q in R* if every q-vertex of S has all its R-successors in S and every p-vertex of S has some
  R-successor in S (DJT, arXiv 2003.08627 v2 section 2). A trap for q is a subgame.
- Attractor. Attr_p^R(X) = least Z ⊇ X ∩ R such that a p-vertex of R with an R-successor in Z, or a q-vertex of R with all its
  R-successors in Z, is in Z. Fact A1: R \ Attr_p^R(X) is a trap for p in R, hence a subgame (HKP Thm 1).
- Monotone attractor (HKP Def. 3, max-parity). For d >= 0 and X ⊆ R: MAttr_p^R(X, d) = least Z ⊆ R such that a vertex v ∈ R
  with pr(v) <= d is in Z as soon as (v ∈ V_p and some R-successor of v is in Z ∪ X) or (v ∈ V_q and all R-successors of v are
  in Z ∪ X). X is kept external: x ∈ X is in Z only if attracted to X in >= 1 move.
- Recurrent set. X ⊆ R is *(p,d)-recurrent in R* if X ≠ ∅ and X ⊆ MAttr_p^R(X, d): from every x ∈ X, p forces a revisit of X
  while every vertex visited (x included) has priority <= d. (HKP: "MAttr(X) is fatal".)
- Peelable (the predicate PA** of A1-results.md). Let d >= 0 with d ≡ p (mod 2), and R ⊆ V with G ∩ R a subgame and
  pr(R) <= d. R is *(p,d)-peelable* if R = ∅, or there is a non-empty F ⊆ R such that R \ F is (p,d)-peelable and
  (a) F = Attr_p^R(MAttr_p^R(X, d)) for some (p,d)-recurrent X ⊆ pr^{-1}(d) ∩ R, or
  (b) F = Attr_p^R(S) for some non-empty trap S for q in R with pr(S) <= d-2 that is (p,d-2)-peelable.
  (R \ F is a subgame by Fact A1; S is a subgame as a trap. Recursion on (d, |R|).)
- d_p(G) = the least d ≡ p (mod 2) with d >= max pr(V). PA**(G): W_E(G) is (E, d_E)-peelable and W_O(G) is (O, d_O)-peelable.
  (W_p is a trap for q in G, hence a subgame.)
- "P solves G completely" (HKP's class Solved, Def. 8): the residual game returned by P is empty.

Lemma 0 (choice of d). If R is (p,d)-peelable then it is (p,d+2)-peelable. Proof: at level d+2 take option (b) with S = R
(a trap for q in R trivially, pr(R) <= d, (p,d)-peelable); F = Attr_p^R(R) = R; R \ F = ∅. So PA** does not depend on
taking the least admissible d. (The converse direction is not needed.)

## 2. Statement
Theorem T-A1. For every parity game G: psolB solves G completely if and only if PA**(G).
Theorem T-A1' (psolQ). If PA**(G) then psolQ solves G completely. The converse fails (HKP Fig. 4(a): psolQ solves it, psolB
does not, so by T-A1 it is not in PA**).
Corollary 1 (HKP's classes). Büchi games (HKP Thm 7), games whose SCCs have constant priority (HKP Thm 8) and
deterministic games (HKP Lemma 5) are contained in PA**: HKP prove that psolB solves them completely, and the "only if"
direction of T-A1 turns that into PA**. This is a consequence of HKP's three theorems, not a derivation of them (REFEREE-2
F4; the lane's earlier wording "they follow from T-A1" was reversed). A direct proof that these classes are PA** would make
HKP's three theorems corollaries of the "if" direction; it is not attempted here. See G10.
Corollary 2 (membership). PA**(G) is decidable in time O(|V|^2 |E|) (HKP Thm 5(1): run psolB and test the residual). This is
not a solver-free procedure; two natural canonical rules are sound but incomplete (A1-results.md section 3).
Remark 3 (order independence; REFEREE-2 F2, agreed). Neither direction of the proof uses the order in which psolB visits the
colours: section 4 shows that in every subgame reached by sound removals with W_p(G') ≠ ∅ some colour of G' has a non-empty
fatal greatest fixpoint, and section 5 works for any sequence of removals. Hence, for every stable colour order π in the sense
of HKP Thm 6 (every colour of the current game is tried before the solver returns, and the loop restarts after a removal),
psolB(π) solves G completely iff PA**(G). This re-proves the completeness half of HKP Thm 6 without HKP's Lemmas 2-4.
REFEREE-2's empirical check: psolB's residual is identical for descending, ascending and random colour orders on all 490,944
games searched (R2-TA1.md section 4).
Remark 4 (hierarchy; data, not part of the claim). A1-results.md section 3 defines two stronger predicates: PA (a DJT
decomposition all of whose traps are traps for the opponent in the whole subgame of their level) and PA* (traps peeled
before the level's top set). On all data PA ⊆ PA* ⊆ PA**, with both inclusions strict (instances/llit_witness_buchi_n3.pg is
PA* and not PA; the game 0 3 0 0; 1 1 0 0; 2 1 0 0,2 is PA** and not PA*); PA* ⊆ PA** was re-derived by REFEREE-2 (F6);
PA ⊆ PA* is data only. Only T-A1, T-A1', Corollary 1-2 and Remark 3 are claimed.

## 3. Facts used (all standard or HKP's)
- F1 (soundness, HKP Thm 2 in max-parity): if X ⊆ W = MAttr_p^{G'}(X, d) with X ≠ ∅ then p wins every vertex of W and of
  Attr_p^{G'}(W) in G'. HKP's proof (tex:575-590) is a sketch; written out in G9.
- F2 (residual regions): if D = Attr_p^{G'}(Y) with Y ⊆ W_p(G'), then G' \ D is a subgame, W_p(G' \ D) = W_p(G') \ D and
  W_q(G' \ D) = W_q(G'). (Zielonka's standard argument: q's winning strategy on W_q never enters D ⊆ W_p; p's winning strategy
  on W_p \ D restricted to G' \ D still wins, as q's moves in G' \ D are a subset of q's moves in G' and p's vertices outside D
  have no edge into D.)
- F3 (monotonicity): X ⊆ X' implies MAttr_p^R(X, d) ⊆ MAttr_p^R(X', d), and likewise PMAttr_p^R(T, d) ⊆ PMAttr_p^R(T', d) for
  targets T ⊆ T' (least fixpoints of operators monotone in the set variable and in the target). Also
  MAttr_p^R(X, d) ⊆ PMAttr_p^R(X, d) (the permissive eligibility condition "pr(v) <= d or v ∈ T" is weaker). Nothing about
  layeredAttr as a whole is claimed (REFEREE-2 F3); T-A1' uses only the last layer, see section 4.
- F4 (psolB's run, HKP Fig. 3): psolB is a sequence of removals D_1, ..., D_m from G_0 = G, G_k = G_{k-1} \ D_k, where
  D_k = Attr_{p_k}^{G_{k-1}}(W_k), W_k = MAttr_{p_k}^{G_{k-1}}(X_k, d_k), X_k ⊆ pr^{-1}(d_k) ∩ V(G_{k-1}) is the greatest
  fixpoint of X ↦ X ∩ MAttr(X, d_k) started from all vertices of priority d_k, and X_k ≠ ∅ (p_k = parity of d_k). After each
  removal the colour loop restarts on G_k. psolB stops when, for every priority d occurring in G_k, the greatest fixpoint is
  empty; the residual is G_m. By F3 the greatest fixpoint at priority d contains every (p,d)-recurrent subset of
  pr^{-1}(d) ∩ V(G_k) (the union of recurrent sets is recurrent, and the iteration never drops a recurrent subset).
- F5 (psolQ's run, HKP Fig. 5): the same with W_k = layeredAttr(G_{k-1}, p_k, X_k), X_k the greatest fixpoint of
  X ↦ X ∩ layeredAttr(X) started from all vertices of parity p_k and priority >= d_k (colour <= b), and the fatal test X ⊆ W.
- F6 (restriction): if R is a trap for q in a subgame G' and X ⊆ R, then MAttr_p^{G'}(X, d) ⊇ MAttr_p^R(X, d) and
  Attr_p^{G'}(X) ⊇ Attr_p^R(X) (p's witnesses inside R are witnesses in G'; q's vertices of R have no G'-successor outside R).
  If moreover R = W_p(G') then equality holds in both (a vertex of W_q(G') cannot force reaching X ⊆ W_p against q, who can
  stay in W_q forever), and the witness successors of p-vertices of R lie in R.

## 4. Proof of "if" (PA** implies psolB, and psolQ, solve G completely)
Fix a player p and a certificate of (p,d_p)-peelability of W_p = W_p(G): a tree of steps. A *level* is a pair (R, d) that is
peeled: the root level (W_p, d_p), and for each (b)-step with trap S at a level of bound d, the level (S, d-2). The steps
of a level (R, d) produce pieces F^1, F^2, ..., F^m with R^0 = R, R^k = R^{k-1} \ F^k, R^m = ∅. Define the *list* of a level
recursively: list(R, d) = seg(F^1) ++ ... ++ seg(F^m), where seg(F) = [F] if F is an (a)-piece, and
seg(F) = list(S, d-2) ++ [F \ S] if F is a (b)-piece with trap S. Let L = list(W_p, d_p). The members of L are pairwise
disjoint and their union is W_p (induction on the recursion; empty members allowed). For a member P write Before(P) for the
union of the members listed before P.

Invariant I. For every level (R, d) and every q-vertex u ∈ R, all successors of u in G lie in R ∪ Before(first member of
list(R, d)). Proof by induction on depth: for (W_p, d_p), u's successors lie in W_p (a trap for q in G). For a level (S, d-2)
created by a (b)-step at level (R', d') after pieces F^1..F^{k-1}: S is a trap for q in R'^{k-1} = R' \ (F^1 ∪ ... ∪ F^{k-1}),
so u ∈ S has all R'^{k-1}-successors in S; its other successors lie in V \ R' (by induction inside R' ∪ Before(list(R')) and
hence, as u ∈ S ⊆ R' is a q-vertex of R', in Before(list(R'))), or in F^1 ∪ ... ∪ F^{k-1}, all of which are listed before
list(S, d-2) begins. ∎
Consequence I'. If F = F^k is a piece of level (R, d) and u is a q-vertex of R^{k-1}, all successors of u lie in R^{k-1} ∪ Before(F)
(as above, with F^1..F^{k-1} ⊆ Before(F)).

Setting. Let G' be any subgame reached from G by removals as in F2 (by either player, in any order), Rem = V \ V(G'), so
W_p(G') = W_p \ Rem by F2 applied repeatedly. Note that every vertex of W_p ∩ Rem was removed by a p-removal
D = Attr_p^{G''}(Y) with Y ⊆ W_p(G'') (q-removals lie in W_q).

Observation O. If v ∈ W_p ∩ V(G') is a p-vertex, no successor of v lies in Rem ∩ W_p: a successor w removed by the p-removal
D = Attr_p^{G''}(Y) at a time when v ∈ V(G'') would have put v into D (p-vertex with an edge into the attractor). Likewise a
q-vertex v ∈ V(G') has at least one successor in V(G') (G' is a subgame).

Lemma L1 (the first surviving member is an (a)-piece whose target is still recurrent). Suppose W_p(G') ≠ ∅ and let P be the
first member of L with P ⊄ Rem. Then P is an (a)-piece F of some level (R, d), step k, with recurrent target X and
W = MAttr_p^{R^{k-1}}(X, d), and X' = X ∩ V(G') is (p,d)-recurrent in G'.
Proof. (i) P is not a member of the form F \ S. Suppose it were, with F = Attr_p^{R^{k-1}}(S) at level (R, d) and S ⊆ Rem
(all members of list(S) precede P). Let v ∈ (F \ S) \ Rem have the least attractor rank r >= 1. If v ∈ V_p, its witness
successor has rank r-1, so it lies in S ∪ {rank < r} ⊆ Rem ∩ W_p, contradicting O. If v ∈ V_q, all its R^{k-1}-successors have
rank < r, hence lie in Rem; its other successors lie in Before(F) ⊆ Rem by I'; so v has no successor in G', contradicting O.
(ii) So P = F is an (a)-piece: F = Attr_p^{R^{k-1}}(W), W = MAttr_p^{R^{k-1}}(X, d). Write W' = W ∩ V(G'), X' = X ∩ V(G').
Claim: W' ⊆ MAttr_p^{G'}(X', d). Induction on the rank of w ∈ W' in the least-fixpoint computation of W (rank i: added at
stage i, with witnesses of rank < i or in X). pr(w) <= d. If w ∈ V_p: its witness w' ∈ X ∪ (rank < i) lies in W_p; by O it is
not in Rem, so w' ∈ X' ∪ (MAttr_p^{G'}(X', d) by induction), and w is eligible. If w ∈ V_q: its R^{k-1}-successors lie in
X ∪ (rank < i); its other successors lie in Before(F) ⊆ Rem (I'); so all its G'-successors lie in X' ∪ MAttr_p^{G'}(X', d), and
it has at least one (O). This proves the claim. Since X ⊆ W (X is recurrent in R^{k-1}), X' ⊆ W' ⊆ MAttr_p^{G'}(X', d).
(iii) X' ≠ ∅. Otherwise MAttr_p^{G'}(∅, d) = ∅ gives W' = ∅, and then the rank argument of (i) applied to the attractor
F = Attr_p^{R^{k-1}}(W) (with W in place of S) gives F ∩ V(G') = ∅, contradicting P ⊄ Rem. ∎

Proof of T-A1 "if". Run psolB (F4). Suppose it stops with residual G_m ≠ ∅. Then W_p(G_m) ≠ ∅ for some p. By L1 there is a
priority d occurring in G_m (the priority of X' ⊆ pr^{-1}(d)) at which some (p,d)-recurrent set X' ⊆ pr^{-1}(d) ∩ V(G_m)
exists, so by F4 the greatest fixpoint at d is non-empty and psolB would have made a further removal: contradiction. ∎
Proof of T-A1'. Run psolQ (F5). At the bound b of priority d (which occurs in G_m since X' ≠ ∅), the start set
X_0 = {v : pr(v) >= d, pr(v) ≡ p} contains X'; all its vertices have parity p, so Fig. 5's pre-condition holds. The iteration
X ↦ X ∩ layeredAttr(X) starts from X_0; we show it never drops X'. Let X ⊇ X' be the current set and write the last layer of
layeredAttr(G_m, p, X) as A_b = PMAttr_p(A_{b-2} ∪ Y_b, d) with Y_b = {v ∈ X : pr(v) >= d} = X ⊇ X' (every vertex of X has
priority >= d; in HKP's colours, colour <= b). By F3, A_b ⊇ PMAttr_p(X', d) ⊇ MAttr_p^{G_m}(X', d) ⊇ X'. So X' ⊆ layeredAttr(X)
and X' ⊆ X ∩ layeredAttr(X). Hence the iteration ends in a non-empty fatal set and psolQ makes a further removal:
contradiction as before. (Only the monotonicity of one PMAttr layer in its target is used; the increase of the layer chain
A_{d'} ⊆ A_{d'+2} is not needed.) ∎

## 5. Proof of "only if" (psolB solves G completely implies PA**)
Let psolB's run be D_1, ..., D_m with G_m = ∅ (F4). Fix p. We show by downward induction on k that W_p(G_k) is
(p, d_p)-peelable (note d_p >= max pr(V) >= max pr(V(G_k)), so d_p is admissible at every stage). Base k = m: ∅.
Step: assume W_p(G_k) is (p,d_p)-peelable and consider D_k (so G_k = G_{k-1} \ D_k).
- If D_k is a q-removal: W_p(G_k) = W_p(G_{k-1}) by F2, and the subgame G ∩ W_p(G_{k-1}) is the same in G_{k-1} and G_k (D_k ⊆ W_q
  and peelability uses only edges inside W_p). Done.
- If D_k is a p-removal: R = W_p(G_{k-1}), X = X_k ⊆ pr^{-1}(d_k) ∩ V(G_{k-1}), W = MAttr_p^{G_{k-1}}(X, d_k), D_k = Attr_p^{G_{k-1}}(W).
  By F1, W ⊆ R, so by F6 (with R = W_p(G_{k-1})) W = MAttr_p^R(X, d_k) and D_k = Attr_p^R(W), and R \ D_k = W_p(G_k) is
  (p,d_p)-peelable by the induction hypothesis. Two cases.
  (1) d_k = d_p: option (a) with the recurrent set X (X ⊆ W by the fatal test): F = D_k. Done.
  (2) d_k < d_p (then d_k <= d_p - 2, same parity): option (b) with S = W. S is a trap for q in R (every q-vertex of W has all
  its successors in W ∪ X = W by the MAttr condition, with X ⊆ W; every p-vertex of W has a witness successor in W),
  pr(W) <= d_k <= d_p - 2, and S is (p, d_p - 2)-peelable: by Lemma 0 it suffices that W is (p, d_k)-peelable, which holds by
  option (a) with X: MAttr_p^W(X, d_k) = W (F6 with R = W, a trap for q in G_{k-1}: the witnesses of p-vertices of W lie in
  W ∪ X = W), so X is recurrent in W and F = Attr_p^W(W) = W, leaving ∅. Finally F = Attr_p^R(S) = D_k. Done.
  (d_k > d_p is impossible as X ⊆ R has priority d_k <= max pr(V) <= d_p.)
So W_p(G_0) = W_p(G) is (p,d_p)-peelable for both p, i.e. PA**(G). ∎

## 6. Gaps and what the referee should check (status after REFEREE-2, docs/referee-2/R2-TA1.md)
- G1. F2 is used as "standard". REFEREE-2 wrote it out (R2 section 2: q's winning strategy keeps the play in the trap W_q(G'),
  disjoint from D ⊆ W_p(G'); p's positional strategy on W_p(G') never leaves W_p(G') and never enters D from outside D); may be
  cited as Zielonka 1998 section 3. Closed by R2's text.
- G2. The proof of L1(ii) treats X external in MAttr (HKP's convention, tex:532-535): a vertex of X ∩ W has rank >= 1 and
  witnesses of lower rank or in X; nothing needs rank 0. Closed by R2.
- G3. F6's equality "MAttr^{G'} = MAttr^R for R = W_p(G')": R2's cleaner argument: by F1, Z = MAttr_p^{G'}(X,d) ⊆ W_p(G') = R;
  induction on attraction rank gives Z ⊆ MAttr_p^R(X,d) (a p-witness lies in Z ∪ X ⊆ R; a q-vertex of Z has all G'-successors
  in Z ∪ X ⊆ R, so its R-successors are the same set, and it has one). Same for Attr. Closed by R2; section 5 as written uses
  only W ⊆ R and "witnesses lie in R".
- G4. psolB's colour loop: the proof needs only that every occurring colour is examined before psolB returns and that psolB
  restarts after each removal (HKP Fig. 3). Covered by Remark 3.
- G5. Choice of d: Lemma 0 lifts certificates to larger d; the "only if" direction produces certificates at d_p directly. R2's
  side check: PA** at d_p, d_p+2, d_p+4 identical on 4,000 random games (the converse of Lemma 0, unproved, is not needed).
- G6. Members of the list L may be empty (a (b)-step's F \ S); the choice "first member not inside Rem" skips them.
- G7. Finite games, every vertex has a successor (TARGET section 1); self-loops are ordinary edges.
- G8. T-A1' uses F3 only for one PMAttr layer (section 4, revised after R2 F3). The monotonicity of layeredAttr as a whole
  (layer chain A_d ⊆ A_{d+2}, which rests on the external target, plus the monotone layer count) is NOT claimed.
- G9 (R2 F1). F1 rests on HKP Thm 2, whose proof in the source is a one-paragraph sketch (tex:575-590). Written out (R2):
  the attractor strategy on MAttr(X) reaches X in >= 1 move through priorities <= d (colours >= c); X ⊆ MAttr(X) lets it
  repeat; so the play stays in MAttr(X), visits priority d (colour c) infinitely often and sees no priority > d (colour < c);
  the top priority seen infinitely often is d, of p's parity. Closed by this text.
- G10 (R2 F4). Corollary 1 inherits HKP's proofs of Thm 7, Thm 8 and Lemma 5. HKP's proof of Thm 7 invokes Thm 6 (robustness),
  whose proof rests on Lemmas 2-4, given as sketches. R2 checked that Thm 7 goes through without Thm 6 (every colour is tried
  before returning: with W_0(G') ≠ ∅ colour 0 has a non-empty fixpoint, else colour 1 does), and likewise Lemma 5 and Thm 8
  (the sink SCC's colour always yields a fatal attractor containing the SCC; SCCs of a subgame refine the SCCs). Remark 3
  gives the same independence of the order. Open until a second signature.
Evidence: PA** ⟺ psolB-complete on all 41,440 canonical 3-vertex games and on 20,000 + 20,000 random 4-vertex and 1,500 + 3,000
random 5-vertex games; PA** false on all 75,856 psolQ failures among the 27,331,200 canonical 4-vertex games
(experiments/attr/results/pa2_*.txt). REFEREE-2's independent code: 490,944 games (exhaustive n <= 3 without canonicalisation,
random n = 4, 5, 6), both directions hold, psolQ-complete does not imply PA** (6 of 324 at n = 2), R2-TA1.md section 4.
