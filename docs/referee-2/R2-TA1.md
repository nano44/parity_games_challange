# R2-TA1: second-referee report on T-A1 (psolB-complete ⟺ PA**) — REFEREE-2, 2026-10-14 23:36Z
Claim refereed: claude/l-attr d5d6396, docs/attr/TA1-proof.md (blob 8691267), context docs/attr/A1-results.md (blob 1076c23)
sections 3-4, code experiments/attr/ at the same commit. Written without reading docs/referee/ or notes/REFEREE.md.
Primary source opened by me: HKP = Huth, Kuo, Piterman, arXiv 1405.0386v2 (e-print archiv.tex; line numbers below are its
lines). Theorem/definition numbers are by order of appearance in that file: Def. 1 attractor (tex:407), Def. 2 trap (487),
Def. 3 monotone attractor (506), Def. 4 fatal (551), Thm 2 fatal is winning (567), Fig. 3 psolB (728-747), Def. 6 permissive
attractor (936), Fig. 5 layeredAttr/psolQ (970-997), Def. 7 (1033), Thm 4 (1060), Thm 5 complexity (1214), Thm 6 robustness
(1346), Lemmas 2-4 (1355-1524), Def. 8 Solved/Kernel (1632), Thm 7 Büchi (1651), Lemma 5 deterministic (1784), Thm 8
SCC-constant (1811). My code: docs/referee-2/R2-TA1/ (r2lib.py, validate.py, search.py, compare_lane.py, lemma0_converse.py;
outputs in results/). Nothing in it is taken from experiments/attr/; the lane's code was run only in compare_lane.py.

## Verdict
| item | verdict |
| --- | --- |
| T-A1 (psolB solves G completely ⟺ PA**(G)), both directions | **OK** with CHANGES F1-F3 (gap list), no error found |
| T-A1' (PA**(G) ⟹ psolQ solves G completely) | **OK** with CHANGES F3 (gap G8 incomplete as written) |
| Corollary 1 as written in TA1-proof.md (HKP's three classes ⊆ PA**) | **OK** (vacuous direction; see F4) |
| Corollary 1 as routed ("HKP Thm 7, Thm 8 and Lemma 5 follow" from T-A1) | **BROKEN** as a derivation: circular (F4) |
| Corollary 2 (PA** decidable in O(\|V\|^2 \|E\|)) | **OK** (= T-A1 + HKP Thm 5(1); not a solver-free procedure) |
| "By the same proof, psolQ solves G completely iff PA**(G)" (routed) | **BROKEN**: 2-vertex counterexample (F5) |
| Proposition 3 (PA ⊊ PA* ⊊ PA**) | not in the routed claim; PA* ⊆ PA** re-derived, both witnesses confirmed, PA not checked (F6) |
| Evidence tables in A1-results.md section 2-3 | one wrong row (F7); everything else I re-ran agrees |
Overall: **CHANGES** (findings F1-F7 below). The theorem T-A1 and T-A1' survive re-derivation and a search of 490,944 games.

## 1. Definitions against HKP (task item 1)
- psolB. TA1-proof.md F4 and experiments/attr/psolb.py restate HKP Fig. 3 (tex:731-744) exactly: descending colours of the
  current game; X = all nodes of colour d; loop `while X ≠ ∅ and X ≠ cache`; fatal test X ⊆ MAttr(X); on success remove
  Attr_{d%2}(MAttr(X)) and recurse (colour loop restarts); else X := X ∩ MAttr(X). The loop can only exit with X = ∅ (if
  X ⊄ MAttr(X) then X ∩ MAttr(X) ⊊ X), so "psolB returns G" is exactly "the greatest fixpoint is empty at every colour of G",
  as F4 says. MAttr is Def. 3 (tex:506-521) with the target external (tex:532-535); the max-parity restatement
  "colour ≥ c" = "priority ≤ d" is the correct order reversal with parity kept. Checked.
- psolQ. F5 and psolq.py restate Fig. 5 (tex:970-997): ascending colours b, X = {v : c(v) ≤ b, c(v) ≡ b}, layeredAttr with
  PMAttr of Def. 6 (eligibility "c(v) ≥ d or v ∈ T", target external), fatal test of Def. 7. Checked.
- PA**. Section 1 of the proof defines (p,d)-peelable with options (a) (recurrent top set X ⊆ pr^{-1}(d), piece
  Attr(MAttr(X,d))) and (b) (closed sub-trap S, pr(S) ≤ d-2, (p,d-2)-peelable, piece Attr(S)), and PA**(G) at d_p. The proof
  uses exactly this definition (section 4 builds the list from (a)/(b) steps, section 5 produces (a)-steps at d_p and
  (b)-steps for lower fatal attractors). experiments/attr/peeling.py `peelable(exact=True)` computes the same predicate
  (every X, every S). My independent implementation (r2lib.make_peelable) agrees with it on 198,940 games (section 4).
- Validation of my implementations against the paper (validate.py, 24 checks, all pass): Fig. 1 regions (Example 1), MAttr(4),
  MAttr(8), v11 ∈ MAttr(11) (Example 2), psolB's two removals and residual {v3,v5,v7} (Example 4), psolQ fatal at b = 4 then
  b = 19 (psolQ example), Fig. 4(a)/(b) (Example 5), Fig. 6 untouched by psolB and psolQ. Games transcribed by me from the tikz
  source (circle = V_0 = Even, square = V_1 = Odd), not from the lane's files.

## 2. Re-derivation (task item 2)
"Only if" (section 5). Downward induction on the removal index k. I re-derived every step; the only non-trivial ones:
- F6 equality (gap G3). Cleaner than the proof's argument and without the "q stays in W_q forever" remark: by F1 (HKP Thm 2)
  Z = MAttr_p^{G'}(X,d) ⊆ W_p(G') = R; then induction on attraction rank shows Z ⊆ MAttr_p^R(X,d): a p-witness lies in
  Z ∪ X ⊆ R, a q-vertex of Z has all G'-successors in Z ∪ X ⊆ R so its R-successors are the same set, and it has one because
  R is a subgame. Same for Attr. The witness claim for p-vertices of X (G3) holds for the same reason. G3 can be closed.
- Case (2) (d_k < d_p): S = W is a trap for q in R (q-vertices of W have all successors in W ∪ X = W since X ⊆ W by the fatal
  test; p-vertices have a witness in W); W is (p,d_k)-peelable by one (a)-step because MAttr_p^R(X,d_k) ⊆ MAttr_p^W(X,d_k)
  (witnesses lie in W); Lemma 0 lifts d_k to d_p - 2. All correct.
"If" (section 4). Invariant I and I' (induction on the certificate tree), Observation O, Lemma L1 (i)-(iii) and the final
argument are correct as written; I checked in particular: (i) the rank argument needs S ⊆ Rem and Before(F) ⊆ Rem, both
given by the choice of P as the first member not inside Rem; (ii) the induction on the rank of w in the least-fixpoint
computation of W is sound with X external (G2: a vertex of X ∩ W has rank ≥ 1 and witnesses of lower rank or in X; nothing
needs rank 0; G2 can be closed); (iii) MAttr(∅,d) = ∅ because every vertex of a subgame has a successor. The step from L1 to
psolB uses only that psolB examines every colour of G_m before returning (G4) and that the greatest fixpoint at priority d
contains every (p,d)-recurrent subset of pr^{-1}(d) (F3, correct: Y ⊆ MAttr(Y) ⊆ MAttr(X) for Y ⊆ X).
T-A1'. Correct, but the written argument needs less than F3 claims and G8 lists more than two lines: see F3.
Gaps G1-G8, one line each: G1 F2 is standard and I wrote it out (q's winning strategy keeps the play in the trap W_q(G'),
disjoint from D ⊆ W_p(G'); p's positional strategy on W_p(G') never leaves W_p(G') and never enters D from outside D) — can be
cited as Zielonka 1998 §3 or closed by that text. G2 closed (above). G3 closed (above). G4 correct; stronger remark in F2.
G5 correct; side check in F2. G6 correct (empty members are skipped by the "first member ⊄ Rem" choice). G7 correct (nothing
in the proof uses the priority range of TARGET; self-loops are ordinary edges throughout). G8 see F3.

## 3. Findings (CHANGES)
- F1 (gap list, major for the record, not for the truth of the theorem). The gap list G1-G8 omits that F1 (soundness of fatal
  attractors) rests on HKP Thm 2, whose proof in the source is a one-paragraph sketch (tex:575-590). Re-derived by me: the
  attractor strategy on MAttr(X) reaches X in ≥ 1 move through colours ≥ c, X ⊆ MAttr(X) lets it repeat, so the play stays in
  MAttr(X), visits colour c infinitely often and sees no colour < c: min Inf = c. Add as G9 (closed by this text).
- F2 (order independence, remark that strengthens the claim). The proof never uses the colour order: section 4 shows that in
  ANY subgame reached by sound removals with W_p(G') ≠ ∅ some colour of G' has a non-empty fatal greatest fixpoint, and
  section 5 works for any removal sequence. Hence "psolB(π) solves G completely ⟺ PA**(G)" for every stable colour order π,
  which re-proves the completeness half of HKP Thm 6 without Lemmas 2-4 (whose proofs in HKP are sketches). Suggest stating
  it; it also answers G4 and G5 fully. Empirical side checks (search.py): residual of psolB with descending, ascending and
  random colour orders identical on all 490,944 games; PA** at d_p, d_p + 2, d_p + 4 identical on 4,000 random games
  (lemma0_converse.py), consistent with the converse of Lemma 0 (unproved, unneeded).
- F3 (G8 is incomplete as written; minor). F3 claims layeredAttr(G,p,X) is monotone in X. That needs, besides the monotonicity
  of each PMAttr layer in its target, (i) that the layer sequence is increasing, A_d ⊆ A_{d+2}, which holds only because every
  v ∈ A_d is eligible in layer d+2 as a member of the target and its witness successors lie in A_d ∪ Y_d ⊆ A_d ∪ Y_{d+2}
  (the target is external, so this is a real step), and (ii) that the number of layers b = max c(X) is monotone in X. Neither
  is in G8's "two lines". However the proof of T-A1' only needs: for X' ⊆ X ⊆ X_0 all of colour ≤ b with X' of colour b, the
  LAST layer is PMAttr(A_{b-2} ∪ X, b) ⊇ MAttr(X', b) ⊇ X' (monotone in the target only). Either write (i)-(ii) out or weaken
  F3 to what is used. Also record: all vertices of X_0 have parity p, so Fig. 5's PRE-CONDITION holds.
- F4 (Corollary 1, direction). TA1-proof.md says HKP's three classes are in PA** "by HKP's theorems and the 'only if'
  direction; no new proof needed". That is correct but is a consequence of HKP's Thm 7, Thm 8, Lemma 5, not a derivation of
  them. The routed text "Corollaries: HKP Thm 7, Thm 8 and Lemma 5 follow" reverses this and is circular. If the lane wants
  the corollary to carry weight, it must show Büchi / SCC-constant / deterministic games are PA** directly (then HKP's three
  theorems follow from the "if" direction). As it stands Corollary 1 also inherits HKP's proofs: Thm 7's proof invokes Thm 6
  "for convenience"; I checked that the argument goes through without Thm 6 (the for-loop tries every colour before
  returning: with W_0(G') ≠ ∅ colour 0 has a non-empty fixpoint, else colour 1 does); Lemma 5 and Thm 8 likewise need only
  that every colour is tried (the sink SCC's colour always yields a fatal attractor containing the SCC, and SCCs of a subgame
  refine the SCCs). Add this dependency as a gap row (G10).
- F5 (routed psolQ "iff": BROKEN). "psolQ solves G completely ⟹ PA**(G)" is false. Smallest counterexample (n = 2, max-parity,
  TARGET format): `0 0 1 0,1; 1 2 0 0;` (v0: priority 0, Odd, edges to v0 and v1; v1: priority 2, Even, edge to v0). Even
  wins both vertices (both cycles have even top priority). psolB (HKP Fig. 3, min-parity colours 2 and 0): at d = 2, X = {v0},
  MAttr = ∅ since v0 is Odd with the successor v1 of colour 0 < 2; at d = 0, X = {v1}, MAttr = ∅ since v1's successor v0 is
  not yet in Z ∪ X and v0 needs both successors in Z ∪ X; psolB returns G. psolQ: b = 0 gives nothing; at b = 2, X = {v0,v1},
  last layer PMAttr({v0,v1}, 2) contains v1 (Even, successor v0 ∈ X) and v0 (both successors in Z ∪ X): fatal, solved. PA**
  is false (W_E = V at d_E = 2: the only top set {v1} is not recurrent, the only lower trap candidate {v0} is not a trap for
  Odd since v0 can leave to v1). Counts: 6 of the 324 games with n = 2, 7,296 of the 175,616 with n = 3 (exhaustive, no
  canonicalisation), 8,667 of 100,000 random n = 4. HKP Fig. 4(a) is another witness (validated). The lane's own T-A1' remark
  says the same ("the converse fails"); the routed sentence contradicts it. T-A1' (the one direction) holds on every game tried.
- F6 (Proposition 3, outside the routed claim). PA* ⊆ PA**: re-derived (if R_l = Attr_p^{R_l}(T) for T = pr^{-1}(d) ∩ R_l
  then T ⊆ MAttr_p^{R_l}(T,d), so the final PA* condition is an (a)-step). Witnesses confirmed with my code:
  llit_witness_buchi_n3 (`0 1 0 0; 1 2 1 0; 2 1 0 2,1`) is PA* and PA**; `0 3 0 0; 1 1 0 0; 2 1 0 0,2` is PA** and not PA*
  (and psolB solves it). PA ⊆ PA* and "PA ⊊ PA*" not checked: PA is defined only in experiments/attr/hypotheses.py, not in the
  proof text; if Proposition 3 is to be a result its definition must be in the document.
- F7 (data row wrong in A1-results.md section 2). The table says at n = 2: psolB undecided 0. The lane's own
  `peeling.py --pa2 2` (run by me on d5d6396) reports psolB undecided on 8 of the 240 canonical games; my exhaustive run finds
  6 of 324 games (e.g. the F5 game). psolQ undecided 0 at n = 2 is right. Also the row n = 3 psolB value (3,060) could not
  be cross-checked without the lane's canonical enumeration; my exhaustive count is 7,536 of 175,616 (non-canonical).

## 4. Counterexample search (task item 4; my code only, results/)
| run | games | PA** ⟹ psolB | psolB ⟹ PA** | PA** ⟹ psolQ | psolQ ⟹ PA** |
| --- | --- | --- | --- | --- | --- |
| exhaustive n = 1, 2, 3 (priorities 0..n, all owners, all successor sets) | 4 + 324 + 175,616 | holds | holds | holds | fails 0 / 6 / 7,296 |
| random n = 4, seeds 41 (any degree), 42 (degree 1-2), 43 (priorities 0..9) | 100,000 + 100,000 + 50,000 | holds | holds | holds | fails 8,667 / 4,731 / 5,044 |
| random n = 5, seeds 51, 52 (degree 1-2); n = 6 seed 61 | 30,000 + 30,000 + 5,000 | holds | holds | holds | fails 2,834 / 1,589 / 302 |
Also on every game: psolB sound against Zielonka; literal min-parity psolB = line-by-line max-parity psolB; psolB residual
independent of the colour order (descending, ascending, random); psolQ solves every game psolB solves.
Comparison with the lane's code (compare_lane.py, not used for the verdict): psolB residual, psolQ residual and PA** identical
on all 324 (n = 2) and 175,616 (n = 3) games and on 20,000 random n = 4 and 3,000 random n = 5 games.
Exhaustive n = 4 was not run (506 M games without canonicalisation; the lane's 27.3 M canonical run covers it only under the
unproved relabelling invariance of PA**, which follows from T-A1 itself).

## 5. Routed-text errors found (for the Lead's grading)
- "By the same proof, psolQ solves G completely if and only if PA**(G)": false (F5); the proof file itself says the converse fails.
- "Corollaries: HKP Thm 7, Thm 8 and Lemma 5 follow": reversed/circular (F4).
No error found in the proof file beyond the gap-list findings F1, F3 and the data row F7 in the context document.

## 6. What is and is not machine-checked
Nothing is Lean-checked (not required: not M4). Machine evidence: the searches above. Everything in sections 2-3 is my
hand re-derivation and is a gap in the fleet's sense until a second signature or Lean. Under CLAUDE.md the claim becomes a
result only with the first referee's independent report; I have not read it.

## 7. Re-check of the revision (claude/l-attr 4478b84, TA1-proof.md blob b1e1118, A1-results.md blob c0d62df; 2026-10-15 00:05Z)
Only the changed parts were re-checked (diff d5d6396..4478b84), as routed by the Lead.
| changed item | verdict |
| --- | --- |
| Corollary 1 (direction: HKP's classes ⊆ PA** by HKP's theorems + "only if"; not a derivation of HKP) | **OK** (F4 applied) |
| Corollary 2 (note "not a solver-free procedure") | **OK** |
| F3 weakened to MAttr/PMAttr monotone in the set variable and the target, MAttr ⊆ PMAttr; nothing on layeredAttr | **OK** (F3 applied) |
| Proof of T-A1' rewritten: last layer A_b = PMAttr_p(A_{b-2} ∪ X, d) with X ⊇ X', since X ⊆ X_0 has colours ≤ b and X' has colour b so max c(X) = b; A_b ⊇ PMAttr(X',d) ⊇ MAttr(X',d) ⊇ X' | **OK**: re-derived; uses only one layer's target monotonicity, as F3 asked; pre-condition of Fig. 5 noted |
| G9 (F1 soundness of fatal attractors written out) | **OK**: matches my derivation |
| G10 (Corollary 1 inherits HKP's proofs; Thm 7/8/Lemma 5 without Thm 6) | **OK** as a gap row; "open until a second signature" is the right status |
| G1-G8 status lines | **OK**: G1-G3 closed by the quoted text, G4 by Remark 3, G5-G8 restated correctly |
| Remark 3 (order independence; F2) | **OK** in substance; one wording nit, N1 below |
| Remark 4 (former Proposition 3, now data; PA ⊆ PA* data only) | **OK** |
| A1-results.md section 2: n = 2 psolB 8 / psol 10 of 240 canonical, n = 3 psolB 3,060 with my 7,536 of 175,616 noted | **OK**: the n = 2 figures equal the output of the lane's peeling.py --pa2 2 that I ran; my counts quoted correctly; psol not checked by me (not implemented) |
| Evidence line (490,944 games, 6 of 324 at n = 2) | **OK**: quotes my section 4 correctly |
- N1 (wording, Remark 3). The parenthetical "stable colour order π in the sense of HKP Thm 6 (every colour of the current game
  is tried before the solver returns, and the loop restarts after a removal)" is not HKP's definition: HKP call π stable when
  psolB(π) and psolB(π·c) have the same input/output behaviour for every colour c, with π a fixed sequence (repetitions
  allowed, no restart). The remark is true for HKP's notion as well, and more simply: stability of π means that no colour of
  the output game has a non-empty fatal fixpoint, which is all the "if" direction uses, and the "only if" direction works for
  any removal sequence. Suggest replacing the parenthetical by "(HKP: appending any colour to π does not change the output;
  equivalently no colour of the output game has a non-empty fatal fixpoint)".
Verdict on the revision: **OK** (N1 is wording). Second-referee position on T-A1 at l-attr 4478b84: T-A1 and T-A1' as
stated in section 2, Corollaries 1-2 and Remark 3 are correct, with gaps G1-G10 as listed there (G1-G3, G9 closed by
written text; G10 open until a second signature; nothing Lean-checked). The first referee's independent report is still
required for this to become a result (CLAUDE.md).

## 8. Second-referee signature (claude/l-attr 57a1515, TA1-proof.md blob f58968f; 2026-10-15 00:25Z)
Diff 4478b84..57a1515 checked (first referee's six items plus my N1):
- F1 now carries HKP Def. 4's hypothesis (∅ ≠ X ⊆ pr^{-1}(d), d ≡ p): correct and necessary; every use (F4, L1, section 5) has
  it. OK.
- F1' (HKP Thm 4) added for psolQ's removals, with gap G11: correct; my first report used "removals as in F2" for psolQ
  without naming this dependency, so G11 is a genuine addition by the first referee. See the G11 status below.
- Büchi class up to order- and parity-preserving recolouring: correct (psolB reads colours only through ≥, = and parity).
- T-A1': the layer count b is constant along the iteration (every X contains X' of priority d and lies in {pr ≥ d}): correct.
- Remark 3 wording (N1) applied as suggested; Remark 4 credits: fine, Remark 4 is excluded from the claim.
Signed claim (Lead's wording, 23:51Z) at l-attr 57a1515: Theorem T-A1; Theorem T-A1' (with "the converse fails");
Corollaries 1-2 as stated; Remark 3. Remark 4 excluded. Verdict as second referee: **OK**.
Gap list G1-G11 with status:
| gap | status |
| --- | --- |
| G1 (F2 standard) | closed: written out by both referees; citable as Zielonka 1998 §3 |
| G2 (external target, rank of X-vertices in L1(ii)) | closed by both referees |
| G3 (F6 equality) | closed: R2's soundness-based derivation; first referee machine-checked it on all n ≤ 3 games |
| G4 (colour loop order) | closed by Remark 3 (proof uses only "every colour tried before returning" and the restart) |
| G5 (choice of d; Lemma 0) | closed: not needed; converse of Lemma 0 unproved, unused (R2 side check on 4,000 games) |
| G6 (empty list members) | closed (the "first member ⊄ Rem" choice skips them) |
| G7 (scope: finite games, successors, self-loops) | closed |
| G8 (layeredAttr monotonicity) | closed: F3 weakened, T-A1' uses one PMAttr layer; layer-chain inclusion not claimed |
| G9 (HKP Thm 2 sketch) | closed by written text (R2, agreed by the lane) |
| G10 (Corollary 1 inherits HKP Thm 7/8/Lemma 5) | open as a dependency on published proofs; R2 re-derived Lemma 5 and Thm 8 in full and checked that Thm 7's proof needs no Thm 6; HKP Thm 7's Büchi fixpoint correspondence itself is taken from the source |
| G11 (HKP Thm 4, F1') | closed at referee level by R2's re-derivation below, WITH A CORRECTION to HKP's proof: as written (tex:1085-1088) the strategy "select the successor with minimal rank r" is unsound. Instance (R2-TA1/hkp_thm4_strategy.py): X = {w}, c(w) = 0; v, u of colour 1 owned by player 0, v → {w,u}, u → {w,v}, w → v. Layer 0 adds v, u at stage 1 and w at stage 2, so r(v) = r(u) = (0,1) < r(w) = (0,2); the minimal-rank strategy plays v u v u ... and loses, although X ⊆ layeredAttr is fatal. Repair: choose a WITNESS successor (one in X_{d} ∪ A_{d-2} ∪ A_{d,i-1} for r(v) = (d,i)); psolq.py records exactly this witness. With the witness strategy HKP's induction goes through: from v with r(v) = (d,i) and c(v) odd (so c(v) > d, since v ∉ X and v ∉ A_{d-2} by minimality), the next vertex is in X_d (even colour ≤ d < c(v)) or has smaller rank, and the play stays in ∪_d A_d = A_b (the layer chain A_d ⊆ A_{d+2} holds by one lfp step: a vertex of A_d is eligible in layer d+2 as a member of the target, with witnesses in A_d ∪ Y_d); ranks decrease until X_d is hit, so every odd colour is followed by a smaller even colour and min Inf is even. V_1-vertices have all successors in the witness set. T-A1' is unaffected (it uses only the statement of Thm 4). |
Nothing is Lean-checked (not required at M3). The claim becomes a result with the first referee's signature on the same
commit; my signature is for 57a1515 only.
