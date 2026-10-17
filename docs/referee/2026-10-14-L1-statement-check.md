# Referee report R-L1: SLP model and first lower-bound target (L-LOWER, docs/lower/L1-statement.md at claude/l-lower 8fcc0f2)

Referee: REFEREE (successor session). Date: 2026-10-14 (routed by the Lead 23:15Z). Source: claude/l-lower 8fcc0f2,
docs/lower/L1-statement.md §1–3 (§4 read for context only), notes/L-LOWER.md at the same SHA. Primary sources opened by me
(LaTeX source / publisher PDF, not the landscape doc): Chatterjee–Dvořák–Henzinger–Loitzenbauer arXiv 1711.09148v1 (CDHL;
arxiv.tex: §2 model lines 466–517, Reduction red:buchi = Reduction 3.9 lines 759–765, Theorem thm:buchi = 3.10 lines 803–814,
Lemma lem:scc2 = 3.4 lines 615–665, proof of 3.10 lines 1223–1241, Prop. lem:objectives_ub §4.2 lines 1023–1044, the "2n
one-step operations" remark lines 284–286; numbering re-derived from the \declaretheorem/\newtheorem shared counter and
confirmed in the compiled PDF) and Arnold–Niwiński–Parys LIPIcs.CSL.2021.9 (ANP; DROPS PDF: §2 p.9:3–9:5 incl. f_{A,B},
trees, Prop. 2.5; §3.1 p.9:5–9:6 cases (1)–(3), Lemmas 3.1, 3.2, Remark 3.3; §3.2 p.9:6–9:8 Algorithm 1, Lemmas 3.4–3.6,
Cor. 3.7; §3.3 p.9:9; Thm 5.1 p.9:14; Remark 5.5 p.9:18; intro p.9:2–9:3 incl. the sentence citing [10] Emerson–Jutla for
"Expression (1) represents the winning region in a parity game").
Machine checks: docs/referee/scratch/slpcheck.py (mine, independent of the lane; run `python3 -I slpcheck.py`; the
`quick` run is reproduced in §3 below).

## Verdict: CHANGES (model well posed; every re-derived statement holds; 9 numbered findings, none BROKEN)
| item (Lead's list) | verdict |
| --- | --- |
| (1) SLP model Defs 1.1–1.4, R1–R6 well posed, non-adaptive, "solves (n,d)" = W_E on all games ≤ n | OK with CHANGES: the letter d clashes with TARGET.md (finding 1); the class of games is ambiguous at one corner (finding 2) |
| (2) Lemmas 1.5, 1.6, 2.1; Transfer 2.2 (CDHL Reduction 3.9 / Thm 3.10) | OK; all re-derived; one O(1)-bit step that CDHL only gestures at is re-derived here and must be written in (gap G3); page cites off (finding 8) |
| (3) Lemma 2.3, Transfer 2.4, the CAUTION on ANP Lemma 3.6 | OK in substance (machine-checked for small n; CAUTION confirmed verbatim); CHANGES: Lemma 2.3 rests on the unproved Remark 2.5 and cites a check that is not in the commit (findings 3, 4) |
| (4) T-L1 precise, non-vacuous, consistent with (2)–(3) | CHANGES: the gloss of ω(n) is a strictly weaker statement than ω(n) (finding 5); the "why it matters" sentence conflates three model differences (finding 6) |

## 1. The model (Defs 1.1–1.4, R1–R6)
Well-posedness. A gate sequence is a finite object; every gate has a value on every game (Cpre_E is total; "every vertex has a
successor" is not even needed for totality). The minimum in Def. 1.4 is attained because a solving program exists for every
(n, d): the Kleene unfolding of the standard nested fixpoint with n iterations per level (cost (d+1)·n^{d+1}, machine-checked
below) or Transfer 2.4. B_1(n) ≤ B_2(n) ≤ C(n,2) and C(n,d) ≤ C(n,d') for d ≤ d' are inclusions of game classes, OK.
Non-adaptive. The sequence is fixed before the game is seen; the only data dependence is through set values flowing along
gates, and no gate inspects a set (no ⊆, =, size). Boolean gates act pointwise, so information moves between vertices only
through Cpre gates: cost is the right measure. Dependence on (n, d) is a non-uniform family, stated in R1. OK.
R3's identities: Cpre_O(X) = V \ Cpre_E(V \ X) (duality, OK); Pre(X) = (V_E ∩ Cpre_E(X)) ∪ (V_O \ Cpre_E(V \ X)): for v ∈ V_O,
v ∉ Cpre_E(V \ X) iff E(v) ⊄ V \ X iff E(v) ∩ X ≠ ∅, OK, 2 gates. "Post is not expressible": by Lemma 1.5, since Post is not
bisimulation invariant (G_1: v_1 → v_2, v_2 ⟲, pr = (1, 2); G_2: v_2 ⟲, v_3 ⟲, both priority 2; (v_2, G_1) ~ (v_2, G_2) but
v_2 ∈ Post(P_1) only in G_1). OK.
"Solves (n, d)" is exactly "output = W_E(G) on every TARGET game with |V| ≤ n and pr(V) ⊆ {0..d}", including smaller games
(R6). W_O = V \ W_E is one free gate, so TARGET's pair (W_E, W_O) is covered. Two statement-drift points:
- Finding 1 (vocabulary). TARGET.md §1: "d = |pr(V)| ≤ n + 1" is the NUMBER of distinct priorities. L1 uses d for the MAXIMUM
  priority ("pr(V) ⊆ {0, ..., d}"), so a TARGET game with d_TARGET = k distinct priorities has L1-d up to n, and an L1 class
  (n, d) contains games with up to d + 1 distinct priorities. CLAUDE.md requires every statement to be diffed against TARGET.md;
  this one fails the diff. Fix: rename (e.g. "priorities bounded by d", written d_max or p_max) or state the translation once
  in Def. 1.3 and in every theorem that mentions d. The Büchi quantities are unaffected (both readings give 2).
- Finding 2 (corner of the game class). TARGET games have pr : V → {0, ..., |V|}. Read literally, "game of TARGET.md section 1
  with pr(V) ⊆ {1, 2}" excludes the one-vertex game with priority 2 (2 > |V| = 1), and C(n, d) for d > n equals C(n, n).
  Asymptotic targets do not care; the exact values B_1(n), B_2(n) for small n that the lane plans to compute
  (notes/L-LOWER.md queue item 3) do depend on the class. Fix: say explicitly whether the priority alphabet is {1, 2}
  regardless of |V| (deviating from TARGET's pr ≤ |V|, which is harmless for lower bounds since more games only raise the
  minimum) and note that C(n, d) = C(n, min(d, n)) under TARGET's convention.

## 2. Lemmas 1.5, 1.6, 2.1 and Transfer 2.2
Lemma 1.5 (bisimulation invariance). Re-derived. The induction must run over ALL pairs (u, u') of the bisimulation relation Z
simultaneously (not over the one pointed pair): base sets are label tests (Z respects pr and owner); ∪, ∩, complement are
pointwise; for Cpre_E, if u Z u' and u ∈ V_E then a successor w ∈ X_j of u has a Z-partner w' successor of u' with w' ∈ X_j
by IH, and symmetrically; if u ∈ V_O, every successor w' of u' has a Z-partner w successor of u, which is in X_j, so w' ∈ X_j.
Isomorphism is a bisimulation. OK. The parenthetical "W_E is also bisimulation invariant" is true (strategy transfer along Z, or
the μ-calculus characterisation) but unsourced: gap G1. The claim "this is what experiments/lower uses" refers to a directory
that does not exist at 8fcc0f2 (see finding 4).
Lemma 1.6 (locality). Re-derived: induction on k over the DAG; a Boolean gate's depth is the max of its inputs; Cpre_E(X_j) at
v is a function of owner(v) and {[w ∈ X_j] : w ∈ E(v)}, each determined by the depth-(k−1) unravelling of (w, G), a subtree of
the depth-k unravelling of (v, G). OK.
Lemma 2.1 (B_1(n) ≥ n − 1). G^+, G^− are TARGET games (successor everywhere; priorities ≤ 2 ≤ n for n ≥ 2; {1, 2} and {1}
are already compressed). W_E(G^+) = V, W_E(G^−) = ∅ (checked by my Zielonka for n = 2..5). Paths of length ≤ n − 2 from v_1
end in v_1..v_{n−1}, all priority 1, all Even's, so the depth-(n − 2) unravellings coincide and Lemma 1.6 forces equal answers
at v_1 for every program of depth ≤ n − 2; a solving program has δ ≥ n − 1, hence c ≥ δ ≥ n − 1. OK. The chain
C(n, d) ≥ C(n, 2) ≥ B_2(n) ≥ B_1(n) needs d ≥ 2 (stated in the lemma, dropped in the "Known picture" line: finding 7).
Transfer 2.2 (CDHL). Quotes verified verbatim against arxiv.tex: the model sentence (lines 471–479), Pre/Post, Theorem 3.10 (1)
"Ω(n) even for instances with constant D", Reduction 3.9 (vertices v_0..v_k, edges v_i → v_j for i < j, loop at v_k, loop at v_j
(j < k) iff x_j = y_j = 1), and the proof sentence "v_0 is winning for Büchi(T) iff there is a loop for one of the vertices in T
iff S_x ∩ S_y ≠ ∅" (line 1227). Theorem numbers: the shared counter gives Thm 2.1 (Set Disjointness), Reduction 3.1, Lemma 3.4,
Remark 3.5 (numbered, capital-R environment), Reduction 3.9, Thms 3.10, 3.11, as the lane cites. Checklist (i)–(iii) re-derived:
(i) out-degree ≥ 1 everywhere, V_O = ∅, P_2 = T, P_1 = {v_k}, n = k + 1 ≥ 2; (ii) Cpre_E = Pre on one-player games; (iii) an SLP
is a deterministic algorithm of CDHL's class using only Pre and set operations (a subclass; CDHL's bound is for the whole class,
Theorem 3.10 is stated for deterministic and bounded-error protocols). One step CDHL does not write out: the proof of Thm 3.10
says only "By the same argument as in the proof of Theorem 3.2 ... constant communication", and Lemma 3.4's two-possible-edges
argument is for the graph of Reduction 3.1, not 3.9. For Reduction 3.9 I re-derived it: with v_max the largest index in S,
Pre(S) ⊇ {v_i : i < max} definitely, v_max ∈ Pre(S) iff max = k or the loop at v_max is present, nothing else; dually Post(S)
⊇ {v_j : j > min}, v_min ∈ Post(S) iff its loop is present. One bit from each party per one-step operation. The transfer is
sound, with constant: deterministic CC of Set Disjointness on k elements is ≥ k (rank 2^k), two bits per Pre, so B_1(n) ≥
(n − 1)/2 from this route; Lemma 2.1's n − 1 is better, as the lane says. Gap G3: the lane must write the two-edge argument for
Reduction 3.9 into the document instead of attributing it to CDHL's text.

## 3. Lemma 2.3, Transfer 2.4 and the CAUTION
Lemma 2.3 (B_2(n) ≤ n²). The formula is the "successor-priority" (shifted) form νZ.μY.Cpre_E((P_2 ∩ Z) ∪ (P_1 ∩ Y)), not the
textbook νZ.μY.(P_2 ∩ Cpre_E(Z)) ∪ (P_1 ∩ Cpre_E(Y)). The document justifies it by "(standard; ... see Remark 2.5)", and Remark
2.5 says the shifted form "needs a source or a proof before use". So as written Lemma 2.3 is unproved (finding 3). I checked that
it is TRUE: (a) argument: the νZ-fixpoint Z* satisfies Z* = μY.Cpre((P_2 ∩ Z*) ∪ (P_1 ∩ Y)); from v ∈ Z* with least rank j,
Even forces the next vertex into (P_2 ∩ Z*) or (P_1 ∩ Y_{j−1}), so the play stays in Z* and ranks fall until a P_2 vertex,
infinitely often: Z* ⊆ W_E. Conversely W_E ⊆ μY.Cpre((P_2 ∩ W_E) ∪ (P_1 ∩ Y)) by ranking each u ∈ W_E with the maximal
number of steps a positional winning strategy needs before the next P_2 visit (finite, ≤ n, else a P_1-only cycle in the
strategy graph), so W_E is a post-fixpoint and W_E ⊆ Z*. The first vertex's priority never matters because the winner is a
limsup. (b) Machine check, slpcheck.py, the Lemma 2.3 program written gate by gate: 0 mismatches against Zielonka on all
games with ≤ 3 vertices and pr ⊆ {1, 2} (4 + 144 + 21,952 games), all 810,000 one-player games with 4 vertices, 300,000 random
two-player games with 4 vertices and 100,000 with 5; the n = 4 program is also right on all games with 2 and 3 vertices (R6).
Cost n·n and depth n·n as claimed; the textbook form costs n(n + 1). Chain-length argument (≤ n strict steps) OK.
Remark 2.5 (f'(x) = Cpre_E(∪_p P_p ∩ x_p)). Also TRUE on the data: the n-fold Kleene unfolding of θ_d x_d ... θ_0 x_0 . f'
agrees with Zielonka on all games with n ≤ 3 and priorities {0..d}, d = 2, 3 (324 + 74,088 + 175,616 games) and on random
n = 4 games with d = 3, 4 (30,000 + 20,000). It is the vertex-priority instance of the edge-priority characterisation (edge
(u, w) carries pr(w)); the source the lane asks for is the one ANP themselves cite for Expression (1) = winning region: ANP
p.9:3 "[10]" = Emerson–Jutla, FOCS 1991 (vertex form); the edge form needs its own citation or the one-paragraph proof above.
Gap G2.
Transfer 2.4 (ANP). Quotes verified: Lemma 3.2 verbatim; Lemma 3.1; Prop. 2.5 (S_{n,h} universal, n^{lg(h/lg n)+O(1)} leaves);
cases (1)–(3) of ‖F‖_{U,V}; Cor. 3.7; the Lemma 3.6 proof sentences "a standard worklist algorithm" and "re-evaluate right sides
only of those equations in which at least one variable was modified in the previous stage" (p.9:8), and "between |V| and
|V|·(1 + nd) queries". Straight-lineness of the symmetric recursion: re-derived from the definition (the query tree is fixed
by (Θ, U, V); computed sets enter only as arguments and as A, B of the restriction A + B ∗ f(·), which are ∪/∩ gates) and
machine-checked: slpcheck.py builds ‖(Θ, g, (∅, V))‖_{U,V} literally as a gate list with U = S_{n,h_μ}, V = S_{n,h_ν}
(S_{n,h} = S_{⌊n/2⌋,h} · ⟨S_{n,h−1}⟩ · S_{⌊n/2⌋,h}), outermost θ_d acting on the LAST argument x_d, and gets 0 mismatches on
all games with n ≤ 3, d ∈ {2, 3} and on random n = 4, d = 3, with cost exactly (d + 1)·|U|·|V| for g and |U|·|V| for f'
(45/15 at (2,2) and (3,2); 100/25 at (3,3); 1156/289 at (4,3)). Replacing V by a non-universal tree of width 1 gives 19,164
mismatches at (3,2): the harness detects wrong trees. Heights: |Θ|_ν = ⌊d/2⌋ + 1 and |Θ|_μ = ⌈d/2⌉, both ≤ ⌈(d + 1)/2⌉, OK;
universality for n' < n vertices follows from universality for n. Exponent: |S_{n,h}| ≤ n^{lg(d/lg n)+O(1)}, squared, times
d + 1 ≤ n + 1: n^{2·lg(d/lg n)+O(1)}, OK (ANP state this symmetric bound at p.9:2 and Remark 3.3).
The CAUTION. Confirmed. Lemma 3.6's algorithm decides which equations to re-evaluate from which variables changed; that is
adaptive, and nothing in ANP gives a straight-line schedule with |V|·poly(n, d) queries. The lane's non-adaptive fallback is
right: Jacobi-style rounds over the |V| equations of Algorithm 1 are monotone from ⊥ (the right-hand sides are monotone in
all variables), each round before stabilisation raises one of the n·|V| bits, so 1 + n·|V| rounds of |V| queries suffice,
n^{2·lg(d/lg n)+O(1)} again. L-LIT's T7 reading "C(n,d) ≤ n^{lg(d/lg n)+O(1)}" for SLPs is therefore unsupported by ANP's text,
as L-LOWER says; whether it is nevertheless true is open (ANP Remark 3.3 and CDHS 1909.04983 are both adaptive). Reading note
for the Lead's task text: "the best non-adaptive exponent is 2·lg(d/lg n)+O(1)" is the best exponent DERIVABLE FROM ANP
non-adaptively, not a proven optimum; the document's own wording ("the best SLP upper bound L-LOWER can currently derive")
is correct and should be kept. ANP Thm 5.1 / Remark 5.5 restricted to the shapes ‖·‖_{U,V}, ‖·‖_V: correct reading.

## 4. Target T-L1
Precision. "B_1(n) = ω(n)" means B_1(n)/n → ∞. The gloss "for every constant K there is n with B_1(n) > K·n" is the negation
of B_1(n) = O(n), i.e. limsup B_1(n)/n = ∞, which is strictly weaker even though B_1 is monotone in n (example: f(n) = n_k²
on [n_k, n_{k+1}) with n_{k+1} = n_k² is monotone, not O(n), not ω(n)). Finding 5: choose one; the strong form (∃ε > 0,
B_1(n) ≥ n^{1+ε} for all large n) is precise and should be the headline, with "B_1(n) ≠ O(n)" as the weak form if wanted.
Non-vacuity and consistency. n − 1 ≤ B_1(n) ≤ n² (Lemma 2.1, Lemma 2.3 via B_1 ≤ B_2), so the strong form needs ε ≤ 1 and is
not excluded by anything in §2; the weak form is consistent too. B_1 is monotone and ≥ 1 for n ≥ 2. Non-vacuous.
TARGET vocabulary. Max-parity, vertex priorities, successor everywhere, W_E as Even's region: OK (modulo findings 1 and 2).
"Why it would matter". CDHL Prop. 4.2 (lem:objectives_ub), verbatim "O(min(SCC + D, |T|·D))", with SCC = O(n) (Thm 4.1 /
GPP08), so one-player Büchi costs O(n) one-step operations in CDHL's model: OK. But CDHL's model differs from Def. 1.3 in THREE
ways at once: (a) adaptive, (b) vertex-naming (singleton sets are basic sets; their p.2 "for every vertex v perform a Pre and a
Post" learns the whole graph in 2n operations) and (c) Post available. The O(n) algorithm uses (b) and (c) (SCC decomposition
is forward/backward). T-L1 would show the SLP model is weaker than CDHL's, not that non-adaptivity is the cause (finding 6).
Note for the lane's own §4: with named singleton queries, n queries read the adjacency matrix, so no model with vertex naming
and unrestricted post-processing can give ω(n); super-linearity has to come from R2 (anonymity) plus pointwise Boolean
post-processing, which is what §4's "count × distance" intuition relies on.
Novelty. L-LIT T7 found nothing beyond linear for non-adaptive symbolic models; the modal-logic succinctness remark is right
(those are over all structures). One adjacent framework neither T7 nor L1 mentions: the matrix-vector query model (Sun, Woodruff,
Yang, Zhang, ICALP 2019, arXiv 1906.05736; Rashtchian–Woodruff–Zhu arXiv 2006.14015), where a graph is accessed through
products Ax (CDHL's own p.5 remark identifies one-step operations with Boolean matrix–vector products) and adaptive/non-adaptive
query counts for graph problems are studied, with lower bounds by two-party communication complexity. Because an SLP is an
adaptive Mv algorithm (its queries depend on earlier answers through fixed Boolean gates), any adaptive Boolean-Mv lower bound
for "reach a cycle through P_2" would transfer to B_1; none above Ω(n) can exist there (n basis queries read A). So I do not
expect T-L1 to be in that literature, but L-LIT should open it and say so (NEEDS). Not re-checked: whether any non-adaptive
Boolean-Mv paper treats anonymous (label-only) query vectors.

## Findings (numbered; severity: S = statement must change, N = nit)
1. (S) d means "maximum priority" in L1 and "number of distinct priorities" in TARGET.md §1. Rename or translate in Def. 1.3 and
   in every statement using d; the TARGET diff fails as written.
2. (S) Fix the game class at the corner pr > |V| (one-vertex Büchi game with priority 2; C(n, d) for d > n): say which games are
   in, since exact small-n values depend on it.
3. (S) Lemma 2.3 is stated with the shifted formula and justified only by Remark 2.5, which the document itself marks unproved.
   Either prove the shifted νμ identity in the document (the argument is short; my sketch in §3 is a check, not the lane's
   proof) or state Lemma 2.3 with the textbook form at cost n(n + 1) and keep n² as a corollary of Remark 2.5 once proved.
4. (S) "Checked against Zielonka for n ≤ 4 in experiments/lower, section 3" and "this is what experiments/lower uses" cite
   a directory that does not exist at 8fcc0f2 (the lane's queue says it is still to be written). A statement document may not
   cite a check that is not in the commit. Remove, or land the experiment first and cite its SHA.
5. (S) T-L1's gloss of ω(n) is the strictly weaker "not O(n)". Pick the quantifier (recommend headline = strong form n^{1+ε}).
6. (S) "Why it would matter": name the three differences between Def. 1.3 and CDHL's model (adaptivity, vertex naming, Post);
   T-L1 separates the models, it does not isolate adaptivity. The vertex-naming remark (n singleton queries read the graph)
   belongs here.
7. (N) "Known picture" drops the hypothesis d ≥ 2 of Lemma 2.1 (C(n, 0) = 0; C(n, 1) is not bounded below in the document).
8. (N) CDHL page cites (printed numbers): Reduction 3.9 p.7, Theorem 3.10 p.8 (not 7), proof p.13 (OK), §4.2 "Upper Bounds for
   Liveness" p.10 (not 14), model sentence p.4 (§2), "2n one-step operations" remark p.2 (OK). Theorem numbers all correct.
9. (N) Lemma 1.5's proof sketch should say the induction runs over all pairs of the bisimulation, and Def. 1.3's "over (n, d)"
   is a misnomer: the gate list depends on d (which P_p exist) but not on n; n enters only in Def. 1.4.

## Gaps (steps not machine-checked)
- G1 W_E is bisimulation invariant (Lemma 1.5 parenthetical): standard, unsourced.
- G2 Remark 2.5 / Lemma 2.3: the shifted nested fixpoint equals W_E for all d (checked exhaustively only for n ≤ 3, d ≤ 3, and
  by sampling at n = 4); needs a proof or the edge-priority citation; the vertex form's source is Emerson–Jutla 1991 ([10] in ANP).
- G3 Transfer 2.2: the O(1)-bits-per-operation step for Reduction 3.9 is not in CDHL's text (they say "same argument"); re-derived
  in §2 above, to be written into the document by the lane.
- G4 Transfer 2.4: ANP Lemma 3.1 (universal trees give the exact value) is used as a black box; only its consequence was
  machine-checked on small games. ANP Prop. 2.5 and the width estimate of S_{n,h} are black boxes.
- G5 The CAUTION's non-adaptive fallback bound |V|(1 + n|V|) is a prose argument (monotone rounds), not machine-checked.
- G6 Novelty of T-L1 rests on L-LIT T7 plus the search above; the matrix-vector query literature is not yet opened by L-LIT.
- Lemmas 1.5, 1.6, 2.1 and the two transfers are prose re-derivations by me; no Lean.

## Counterexample attempts
None of the claims in §1–3 admits a counterexample on the data (slpcheck.py, all cells above, 0 mismatches). Finding 5 is a
counterexample to the wording of T-L1, not to its content.
