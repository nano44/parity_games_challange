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

## Verdict: CHANGES (T-A1 and T-A1' hold; both directions re-derived step by step; 6 findings at d5d6396, none against the
## theorem; at 4478b84 findings 1, 2, 4 and a new nit 7 remain, see the Addendum)
| item (Lead's list) | verdict |
| --- | --- |
| psolB, psolQ definitions against HKP | OK: F4/F5 and psolb.py/psolq.py are HKP Figs. 3/5 under colour = M − pr (order reversed, parity kept); MAttr/PMAttr external target and eligibility match Defs 3/6 (§1) |
| "only if" (psolB complete ⇒ PA**) | OK, re-derived (§3); F6's equality holds for every X ⊆ W_p(G'), machine-checked (§5) |
| "if" (PA** ⇒ psolB complete) and T-A1' (⇒ psolQ complete) | OK, re-derived (§4) incl. Invariant I, L1 (i)–(iii), O; T-A1' needs HKP Thm 4 (finding 2) |
| corollaries | Cor. 1, 2 OK (HKP Thms 7, 8, Lemma 5 re-derived informally, §6); Prop. 3 unproved (finding 3) |
| gaps G1–G8 | all closed or benign (§7); unlisted gaps: findings 1, 2, 4 |
| counterexample search n ≤ 4 | none: psolB-complete ⟺ PA** and PA** ⇒ psolQ-complete on all 175,616 labelled 3-vertex games (priorities 0..3), 30,000 random 4-vertex, 20,000 random one-player 4-vertex, 10,000 + 10,000 random 5-vertex games; Fig. 4(a) and the Prop. 3 witness reproduced (§5) |

## Addendum (re-check at claude/l-attr 4478b84, the Lead's 23:42Z retarget; written after my own derivation above, then
## REFEREE-2's docs/referee-2/R2-TA1.md was read)
Diff d5d6396 → 4478b84 touches only docs/attr/TA1-proof.md, docs/attr/A1-results.md and notes/L-ATTR.md (no code), so §5's
machine checks stand. Status of my findings at 4478b84:
- Finding 1 (F1 lacks "X ⊆ pr^{-1}(d), d ≡ p"): STILL OPEN. F1's statement is unchanged; the new G9 text ("visits priority d
  infinitely often") silently uses exactly the omitted hypothesis. Add it to F1 (and to the name "recurrent" if it is to carry
  HKP's "fatal").
- Finding 2 (T-A1' needs HKP Thm 4 so that psolQ's removals are F2-removals and L1's Setting applies to psolQ's residual):
  STILL OPEN. The rewritten T-A1' proof ("contradiction as before") is correct and now uses F3 only for the last layer (my
  re-derivation: Y_b = X since X ⊆ X_0 ⊆ {pr ≥ d}; the last layer stays at d along the iteration because X' ⊆ X_j has priority d),
  but the fact that the subgame G_m reached by psolQ is "reached from G by removals as in F2" needs the soundness of layered
  fatal attractors (HKP Thm 4), which the facts list still does not state. One line (F1') closes it.
- Finding 3 (Prop. 3 unproved): RESOLVED by Remark 4 (data, outside the claim); PA ⊆ PA* correctly labelled data-only.
- Finding 4 (Corollary 1's "Büchi" is HKP's class up to recolouring; psolB's invariance under order- and parity-preserving
  recolourings is used silently): STILL OPEN; the consequence-direction rewording (R2 F4) does not touch it.
- Finding 5 (F3 / layeredAttr monotonicity): RESOLVED (F3 weakened to MAttr/PMAttr target monotonicity; T-A1' uses one layer).
- Finding 6 (order-free by-product): RESOLVED by Remark 3.
New at 4478b84:
- G9 (HKP Thm 2 written out): correct as a sketch (attractor strategy, ≥ 1 move, priorities ≤ d, X ⊆ MAttr(X) repeats), with the
  hypothesis of finding 1 understood.
- G10 (Corollary 1 inherits HKP's proofs of Thm 7, Thm 8, Lemma 5; checked by R2 to go through without Thm 6): agrees with my
  §6; I signed the same three re-derivations independently.
- Remark 3's gloss of HKP's "stable" is wrong as a definition: HKP (§5.2, before Thm 6) define psolB(π) as the solver following a
  fixed finite colour sequence π (repetitions allowed, no restart) and call it stable if appending any colour c1 leaves the
  input/output behaviour unchanged. That is not "every colour of the current game is tried before returning, with restarts". The
  remark's content survives under HKP's definition: stability means no colour of the output has a non-empty fatal fixpoint,
  which is all L1 needs, and the "only if" direction works for any removal sequence. Finding 7 (N): replace the gloss by HKP's
  definition plus that one-line bridge.
- A1-results.md n = 2 row: the corrected psolB count agrees with my data (6 of the 324 labelled two-vertex games are
  psolB-undecided, §5; R2's example `0 0 1 0,1; 1 2 0 0` is one of them). I cannot check the canonical counts (8 of 240)
  without the lane's enumeration.
Verdict at 4478b84: CHANGES (findings 1, 2, 4, 7 open; T-A1, T-A1', Corollaries 1–2 and Remark 3 hold). First-referee
signature on T-A1 and T-A1' is given subject to findings 1 and 2 being applied (statement precision only; no step of either
proof changes). Plant note: R2's F5 ("psolQ iff", BROKEN) was in the Lead's routing to REFEREE-2 only; my routing text had the
one-direction form.

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

## Signature block (first referee) — claim at claude/l-attr 57a1515, docs/attr/TA1-proof.md (blob f58968f)
Claim signed: Theorem T-A1 (psolB solves G completely ⟺ PA**(G)); Theorem T-A1' (PA**(G) ⟹ psolQ solves G completely;
converse false, witnesses HKP Fig. 4(a) and the 2-vertex game `0 0 1 0,1; 1 2 0 0`); Corollaries 1–2 as stated in the file;
Remark 3 (order independence, for HKP's stable sequences). Excluded: Remark 4 (PA, PA*; data only).
Application check (diff 4478b84..57a1515): finding 1 applied (F1 now has d ≡ p, ∅ ≠ X ⊆ pr^{-1}(d)); finding 2 applied (F1' =
HKP Thm 4 with gap G11, invoked at the start of the T-A1' proof); finding 4 applied (Corollary 1 states the recolouring
invariance); finding 5 applied (constant layer count written into the T-A1' proof); finding 6 applied (Remark 3); finding 7
applied (Remark 3 now uses HKP's definition of a stable sequence plus the bridge "no colour of the output has a non-empty
fatal fixpoint"); finding 3 applied earlier (Remark 4). The proof text of sections 4–5 is otherwise unchanged from the version
I re-derived above. No new error found.
VERDICT: OK. Signed as first referee, 2026-10-14, with the gaps below (CLAUDE.md: a result needs two referees with gaps listed).
Gap list, status at 57a1515:
| gap | content | status |
| --- | --- | --- |
| G1 | F2 (residual regions after a sound removal) | closed: written out by R2 §2 and by me (§2 above); citable as Zielonka 1998 |
| G2 | X external in MAttr; rank of X-vertices in L1(ii) | closed (no rank 0; both referees) |
| G3 | F6 equality MAttr^{G'} = MAttr^{W_p(G')} | closed: re-derived (needs only F1); machine-checked for every X ⊆ W_p on 324 + 40,000 + 1,500 games |
| G4 | psolB's colour loop | closed: only "every occurring colour examined, restart after removal" is used; subsumed by Remark 3 |
| G5 | choice of d, Lemma 0 | closed: Lemma 0 re-derived and machine-checked at d_p → d_p+2; converse not needed |
| G6 | empty members of the list L | closed (skipped by the "first member ⊄ Rem" choice) |
| G7 | finite games, successors everywhere, self-loops | closed (nothing else is used) |
| G8 | monotonicity used in T-A1' | closed: one PMAttr layer, target monotonicity only; layer count constant along the iteration |
| G9 | HKP Thm 2 (F1) proof is a sketch | closed by the written-out argument (with the priority-d hypothesis now in F1) |
| G10 | Corollary 1 inherits HKP Thm 7, Thm 8, Lemma 5 | open as a dependency on HKP; re-derived informally by both referees (my §6: Büchi ν-fixpoint then safety core; sink SCC; unique play's minimal colour), without HKP Thm 6 |
| G11 | HKP Thm 4 (F1') proof is a sketch | re-derived by me from HKP's text (tex:1067–1125): the rank-(d,i) strategy keeps the play in A_b (each step goes to X with colour ≤ d or to a smaller rank); every visit to a colour of parity 1−p at rank (d0,i0) has colour > d0 and is followed, by well-founded descent of ranks with d non-increasing, by a visit to X with colour ≤ d0, so if the minimal colour seen infinitely often were of parity 1−p a smaller colour would be seen infinitely often; hence min Inf has parity p. Prose only, no machine check beyond psolq.py's witness strategies passing verify.py |
Non-machine-checked throughout: Invariant I, L1, O, the "only if" induction, Lemma 0, and G9–G11 are prose re-derivations
(mine and R2's); machine evidence is the searches of §5 and R2 §4. Not Lean-checked (not required: not M4).
