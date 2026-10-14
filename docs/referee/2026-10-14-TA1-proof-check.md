# Referee report (first referee): T-A1, the class psolB solves completely (L-ATTR, docs/attr/TA1-proof.md at claude/l-attr d5d6396)

Referee: REFEREE (first of two independent referees; no coordination with the second). Date: 2026-10-14 (routed by the Lead
23:22Z). Source: claude/l-attr d5d6396, docs/attr/TA1-proof.md (§1–6), context docs/attr/A1-results.md §3–4, code
experiments/attr/psolb.py, psolq.py, peeling.py, strahler.py (Strahler.attr, is_trap_for_opponent), a1lib.py, check.sh.
Primary source opened by me: Huth–Kuo–Piterman arXiv 1405.0386v2 (HKP), LaTeX archiv.tex + PDF: §2 (games, colours,
MIN-parity: player 0 wins iff min Inf is even), Defs 1–4 (attractor, trap, monotone attractor with external target,
fatal), Thm 1, Thm 2 and proof, Lemma 1, Fig. 3 (psolB, tex:728–747), Example 5 and Fig. 4(a) (png in the source),
Def. 6 (pmpre/PMAttr, tex:942–948), Def. 7, Fig. 5 (layeredAttr/psolQ, tex:970–997), Thm 4 and proof, Thm 5, Thm 6
(statement), Def. 8 (class S "Solved"), Thm 7 and proof, Lemma 5 and proof, Thm 8 and proof, the external-target
remark tex:528–536. Not opened by me: DJT arXiv 2003.08627 (the trap definition is quoted from the lane; it is the standard
one and matches HKP Def. 2 with the roles swapped).
Machine checks (mine, independent of experiments/attr): docs/referee/scratch/ta1check.py (my own psolB and psolQ written
from HKP Figs. 3/5 in HKP's min-parity colours, fed colour = M − pr; my own PA** in max-parity from §1, exhaustive over X
and S; Zielonka reference) and ta1probe.py (F2, F6, Lemma 0 on all small games).

## Verdict: CHANGES (T-A1 and T-A1' hold; both directions re-derived step by step; 6 findings, none against the theorem;
## Proposition 3 is not proved in the document)
| item (Lead's list) | verdict |
| --- | --- |
| psolB, psolQ definitions against HKP | OK: F4/F5 and psolb.py/psolq.py are HKP Figs. 3/5 under colour = M − pr (order reversed, parity kept); MAttr/PMAttr external target and eligibility match Defs 3/6 (§1) |
| "only if" (psolB complete ⇒ PA**) | OK, re-derived (§3); F6's equality holds for every X ⊆ W_p(G'), machine-checked (§5) |
| "if" (PA** ⇒ psolB complete) and T-A1' (⇒ psolQ complete) | OK, re-derived (§4) incl. Invariant I, L1 (i)–(iii), O; T-A1' needs HKP Thm 4 (finding 2) |
| corollaries | Cor. 1, 2 OK (HKP Thms 7, 8, Lemma 5 re-derived informally, §6); Prop. 3 unproved (finding 3) |
| gaps G1–G8 | all closed or benign (§7); unlisted gaps: findings 1, 2, 4 |
| counterexample search n ≤ 4 | none: psolB-complete ⟺ PA** and PA** ⇒ psolQ-complete on all 175,616 labelled 3-vertex games (priorities 0..3), 30,000 random 4-vertex, 20,000 random one-player 4-vertex, 10,000 + 10,000 random 5-vertex games; Fig. 4(a) and the Prop. 3 witness reproduced (§5) |

## 1. Definitions against HKP
HKP colours c with min-parity; the lane's map c = M − pr, M even ≥ max pr, reverses the order and keeps parity, so
"colour ≥ c" = "priority ≤ d", descending colours = ascending priorities, player 0 = Even. Def. 3 (mpre: colour ≥ c and a
successor in A ∪ X for p's vertices, all successors in A ∪ X for q's; MAttr = μZ.mpre(Z, X, c); X external, tex:528–536)
is §1's MAttr_p^R(X, d) with R-successors; Def. 4 "fatal" = §1 "recurrent" (with X ⊆ pr^{-1}(d), see finding 1). Def. 6
adds the eligibility "or v ∈ X" (permissive) = psolq.py line "c[v] >= d or v in T". Fig. 3 = psolb.py run(): colours of the
current game in descending order, X = vertices of colour d, cache loop, fatal ⇒ remove Attr_{d%2}(MA(X)) and restart;
the while loop exits only with X = ∅ or a removal (after the else branch X shrinks strictly). Fig. 5 = psolq.py: bounds b
ascending, X = {c ≤ b, c ≡ b}, layeredAttr with layers d = p, p+2, …, b and Y = {v ∈ X : c(v) ≤ d}. Both
implementations' worklists count alive successors for the opponent's vertices and pop every target once: faithful. My
independent fixpoint implementations give the same completeness verdicts on every game run (§5), and HKP Example 5 is
reproduced (Fig. 4(a): v0:3 ○, v1:2 □, v2:0 ○, v3:2 □, v4:3 ○; edges v0↔v1, v1↔v2, v2↔v3, v3↔v4; psolB decides nothing,
psolQ solves it at b = 2 with W = all five vertices, Even wins all).
Trap (DJT): q's vertices keep all R-edges inside S, p's keep one; strahler.py is_trap_for_opponent(S, R, p) implements
exactly that (owner == p ⇒ s & S; else s ⊆ S). Attr, MAttr in peeling.py (mattr: pr ≤ d, R-successors, X external) match §1.

## 2. Facts F1–F6
F1: TRUE only with the hypothesis of HKP Def. 4/Thm 2, X ⊆ pr^{-1}(d) with d ≡ p, which F1 omits (finding 1); every use
(F4, "only if", L1) satisfies it. F2: re-derived: G' \ D is a subgame (complement of a p-attractor is a trap for p);
W_q(G') ⊆ W_q(G' \ D) because q's winning strategy never leaves W_q ∩ D = ∅ and p's moves in G' \ D are fewer;
W_p(G') \ D ⊆ W_p(G' \ D) because p's vertices outside D = Attr_p(Y) have no edge into D, so p's winning strategy on W_p
restricted to G' \ D is total and every consistent play is a play of G'; determinacy gives equality (closes G1).
F3: MAttr, PMAttr are least fixpoints of operators monotone in Z and in the target (eligibility "or v ∈ X" is monotone in X);
layeredAttr(X) at a FIXED number of layers is a composition of monotone maps; when X ⊆ X₂ have different b, the extra
layers of X₂ only enlarge A because A ⊆ PMAttr_p(A ∪ Y, d') (a vertex of A is eligible as a target and its witnesses lie in
the previous Z ∪ T ⊆ A ∪ Y; induction over layers). In T-A1' the iterates X_j all contain X' of priority d and lie in
{pr ≥ d}, so b is constant and only the fixed-layer case is used (closes G8, with the two lines above to be written in).
F4, F5: as in §1. F6: the inclusions hold for every trap R for q (p's witnesses in R are witnesses in G'; q's vertices of R
have no G'-successor outside R). The equality for R = W_p(G'): MAttr_p^{G'}(X, d) ⊆ W_p(G') for X ⊆ W_p (q keeps the play
in W_q), then induction on rank (every witness lies in Z ∪ X ⊆ R, every q-vertex's G'-successors are R-successors);
machine-checked for EVERY X ⊆ W_p and every d on all 324 two-vertex games, 40,000 three-vertex games and 1,500
random four-vertex games (ta1probe.py: 0 failures), also Attr^{G'}(X) = Attr^R(X) and F2. In the "only if" only W ⊆ R
(F1) and X ⊆ W are needed for both equalities, as the lane's G3 says (closes G3).

## 3. "Only if" (§5 of the document), re-derived
Downward induction on k. q-removal: W_p unchanged (F2) and peelability uses only G ∩ W_p. p-removal with X = X_k fatal at
d_k: W ⊆ R = W_p(G_{k−1}) (F1), W = MAttr_p^R(X, d_k) and D_k = Attr_p^R(W) (F6, needs only F1), R \ D_k = W_p(G_k) (F2),
pr(W) ≤ d_k. Case d_k = d_p: option (a). Case d_k ≤ d_p − 2: S = W is a trap for q in R (q's vertices of W have all
successors in Z ∪ X = W; p's have a witness in W), pr(W) ≤ d_p − 2, and W is (p, d_k)-peelable by option (a) with X since
MAttr_p^W(X, d_k) = W (rank induction inside the trap W), then (p, d_p − 2)-peelable by Lemma 0 iterated; F = Attr_p^R(W)
= D_k. d_k ≡ p and d_k ≤ max pr(V) ≤ d_p. Lemma 0 re-derived (option (b) with S = R; machine-checked at d_p → d_p + 2 on
all probed games). Base: ∅. OK.

## 4. "If" (§4) and T-A1', re-derived
List L, Before(P): members disjoint with union W_p (seg of a (b)-piece is list(S) ++ [F \ S], S ⊆ F = Attr(S); empty
members harmless, G6). Invariant I by induction on the level depth: root W_p is a trap for q in G; at a level (S, d − 2)
created after pieces F¹..F^{k−1} of (R', d'), a q-vertex of S keeps its R'^{k−1}-successors in S, its successors outside R'
are in Before(list(R')) by the induction hypothesis and those in F¹ ∪ … ∪ F^{k−1} are listed before seg(F^k) ⊇ list(S).
I' follows. Setting: W_p(G') = W_p \ Rem by F2 iterated (q-removals lie in W_q(G'') ⊆ W_q(G)). O: a successor w ∈ Rem ∩ W_p
of an alive p-vertex v ∈ W_p was removed by a p-removal D = Attr_p^{G''}(Y) with v ∈ V(G''), which would contain v.
L1 (i): the first surviving member cannot be F \ S: least attractor rank r ≥ 1 of a surviving v; p-vertex: witness of rank
r − 1 in Rem ∩ W_p, against O; q-vertex: R^{k−1}-successors of rank < r in Rem, others in Before(seg(F)) ⊆ Rem by I', no
successor alive, against "G' is a subgame". (ii): W ∩ V(G') ⊆ MAttr_p^{G'}(X', d) by induction on the MAttr rank in
R^{k−1}; p-vertex: witness in X ∪ (lower rank) ⊆ W_p, alive by O; q-vertex: R^{k−1}-successors in X ∪ (lower rank), others
in Before(seg(F)) ⊆ Rem; X ⊆ W gives X' ⊆ MAttr_p^{G'}(X', d). G2: there is no rank 0 in a MAttr computation (X external,
Z starts empty), vertices of X' are ordinary members of W' with rank ≥ 1 and the induction covers them (closes G2).
(iii): X' = ∅ forces W' = ∅ and then F ∩ V(G') = ∅ by the rank argument of (i). Conclusion: at the priority d of X' the
gfp of psolB on G_m contains X' (F3/F4: the iteration never drops a recurrent subset), is fatal and non-empty, so psolB
removes more: contradiction. The argument does not use the colour order, so T-A1 holds for psolB with ANY colour order
(consistent with HKP Thm 6). T-A1': at bound b = colour of d the start set contains X', the last layer is PMAttr_p(A ∪
X_0, d) ⊇ MAttr_p^{G_m}(X', d) ⊇ X' (F3), the gfp keeps X', a removal follows. This needs psolQ's removals to be
F2-removals, i.e. HKP Thm 4 (layered fatal attractors are winning), which the document never states (finding 2).
Strictness: Fig. 4(a) as in §1 (psolQ complete, psolB decides nothing, hence not PA** by T-A1; my PA** = False). OK.

## 5. Machine checks (docs/referee/scratch/ta1check.py, ta1probe.py; `python3 -I ta1check.py`, 2 min)
| games | psolB-complete | psolQ-complete | PA** | problems |
| --- | --- | --- | --- | --- |
| all 4 one-vertex, 324 two-vertex, 175,616 three-vertex games (priorities 0..n, all owners, all successor sets) | 4 / 318 / 168,080 | 4 / 324 / 175,376 | 4 / 318 / 168,080 | 0 |
| 30,000 random 4-vertex (priorities 0..4); 20,000 random one-player | 27,608; 19,230 | 29,881; 19,960 | 27,608; 19,230 | 0 |
| 10,000 random 5-vertex (0..5); 10,000 (0..2) | 9,110; 9,274 | 9,955; 9,948 | 9,110; 9,274 | 0 |
"Problems" counts: psolB-complete ≠ PA**, PA** with psolQ incomplete, psolB-complete with psolQ incomplete, a Büchi /
SCC-constant / deterministic game outside PA**, psolB residual differing between descending and ascending colour order
(HKP Thm 6), or an unsound decision (assertion). All zero. Fig. 4(a): psolB residual = all, psolQ residual = ∅, PA** false.
Prop. 3's SCC witness "0 3 0 0; 1 1 0 0; 2 1 0 0,2": Odd wins all, psolB complete, PA** true, SCC-constant (hand check in
my notebook: PA* fails because no trap for Even with priorities ≤ 1 exists and Attr_O({v0}) = {v0, v1} ≠ V).

## 6. Corollaries
Cor. 1: logically "HKP's theorem + only-if" (OK). HKP Thm 7 (colours {0,1}): re-derived, psolB at colour 0 computes the
Büchi ν-fixpoint and removes W_0, then at colour 1 the gfp contains the safety core νY.(P_1 ∩ cpre_1(Y)) of W_1, non-empty
whenever W_1 ≠ ∅; iterate. Thm 8: a sink SCC C of constant colour satisfies C ⊆ MA(X_j) whenever C ⊆ X_j, so the gfp ⊇ C
and the residual is again SCC-constant. Lemma 5: the unique play from v ends in a cycle whose minimal colour k sits at a
vertex v' that survives the gfp at k. The lane's class "Büchi" (one priority value, or two of different parity) is HKP's
class up to an order- and parity-preserving recolouring, under which psolB is invariant (it only compares colours and
reads parity); this invariance is used silently (finding 4). Cor. 2: HKP Thm 5(1) O(|V|²|E|) for psolB, OK.
Prop. 3: no proof in the document; PA* ⊆ PA** is short (the final piece R_l = Attr_p^{R_l}(pr^{-1}(d) ∩ R_l) is an
(a)-piece with X = pr^{-1}(d) ∩ R_l, recurrent because every vertex of the subgame R_l is attracted to X through
priorities ≤ d), PA ⊆ PA* is not obvious (DJT removes the top attractor first; Attr_p^R(S_1) and Attr_p^{G_1}(S_1) can
differ in both directions), and both strictness witnesses are data (finding 3).

## 7. The lane's gaps G1–G8
G1 closed by the F2 argument in §2 (to be written into the document or cited: Zielonka 1998 / DJT §2). G2 closed (§4).
G3 closed (§2): equality holds generally for R = W_p(G'); the "only if" uses only F1. G4: benign; the proof needs only that
every colour occurring in the residual is examined and that psolB restarts after a removal; both true for Fig. 3 under
either reading of "colors". G5: Lemma 0 verified; the certificate at d_p exists whenever one at any admissible d does.
G6: benign (§4). G7: all games finite with successors everywhere, self-loops allowed; nothing in the proof needs more.
G8: closed (§2), two lines to add. Unlisted: findings 1–4.

## Findings
1. (S) F1 is false as stated: "X ⊆ W = MAttr_p^{G'}(X, d), X ≠ ∅ ⇒ p wins W" needs X ⊆ pr^{-1}(d) and d ≡ p (HKP Def. 4);
   e.g. p = Even, X = {x} with pr(x) odd and x on its own loop, d ≥ pr(x): X ⊆ MAttr but Odd wins x. Add the hypothesis
   (every use satisfies it). Same for the name "recurrent" if it is meant to carry HKP's "fatal".
2. (S) T-A1' uses that psolQ's removals are F2-removals, i.e. HKP Thm 4 (fatal layered attractors are winning for p). Add it
   to §3 as F1' with its citation.
3. (S) Proposition 3 is stated as a proposition with no proof: give the PA* ⊆ PA** argument (one paragraph), prove or
   downgrade PA ⊆ PA* (data-only at present), and label the strictness witnesses as checked instances.
4. (N) Corollary 1's "Büchi" class is HKP's only up to recolouring; state psolB's invariance under order- and
   parity-preserving recolourings (one line) or restrict the class to two consecutive priorities with the even one on top.
5. (N) Write the two lines for F3's layeredAttr monotonicity (A ⊆ PMAttr(A ∪ Y, d')) or note that T-A1' only needs the
   fixed-layer case (b constant along the iteration).
6. (N) Record the by-product: the "if" proof never uses the colour order, so T-A1 characterises psolB under every order,
   which re-proves the completeness half of HKP Thm 6 without Lemmas 2–4.

## Gaps (steps not machine-checked)
- Invariant I, L1 (i)–(iii), O, the "only if" induction and Lemma 0 are prose re-derivations (mine and the lane's); the
  machine checks cover the theorem's extension on the games listed in §5 and F2/F6/Lemma 0 on the probed games only.
- HKP Thm 2 (F1), Thm 4 (T-A1'), Thm 5(1) (Cor. 2) are black boxes from the paper; Thms 7, 8, Lemma 5 re-derived informally in §6.
- DJT §2 (trap definition) not opened by me.
- PA ⊆ PA* (Prop. 3) rests on data only.
