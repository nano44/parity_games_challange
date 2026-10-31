# R147: own-node σ̄-flips (XCN) and W-cycle-node switches (CN) drop out of the reduction. Theorem SRC-SETTLE (PROVED, lane): with the heads taken at the deviation SOURCES S_k := D_k ∪ D_(k+1) ∪ C instead of their targets, every block of a W-run with no Ξ-change on S_k has at most (n − 1) + m_C transitions (m_C := Σ_(c ∈ C Even) (|succ(c)| − 1)). So polynomial W-runs ⟺ polynomial Ξ-changes at D ∪ C. No σ̄-flip term, no XCN, no CN, and ROOT-FLIP is not needed. XCN and CN do repeat in one W-run (4 and 3 at one vertex, n ≤ 12). No super-linear family was built.
L-RED successor 35 (Opus 5.5; D1/D18). Lead 2026-10-30 ~20:42Z, FIRST BOX R147 (b): «Target HEAD-RED′'s smallest-looking term, XCN
(own-cycle-node σ̄-flips) … Build a family where XCN or CN grows super-linearly in one W-run. If both are provably O(n) per W-run, give the
exact reason; that is a proof-side lemma.» Written 2026-10-30 from 20:50Z (date -u).
- Labels: PROVED (lane) / DATA / READING. Not a TARGET.md claim. G-N5-TIME stays OPEN. This is not M3 and not a step-4 pass.
- Why (b) and not (a): (a) is predicted quadratic, and Lemma ADD (R144) already says that costs add, so (a) could not give a kill.
- Sources opened (no outside theorem is used):
  - l-si accd388a docs/si/N5-SBF-box53.md §1-§4 (HEAD-RED′, XCN, ROOT-FLIP);
  - l-si docs/si/P-N5-SETTLE-box52.md §1-§5 (definitions, PLAY-CAUSE, W-MON, PATH, RUN-SETTLE, RUN-COUNT, Claim RG′, quoted premises);
  - docs/red/R143-settle.md §0-§1;
  - experiments/n5-second/n5b.py SpecSI.evaluate_choice (the S1 DFS and the cycle-node choice).
- Object: N5 (SPEC S1-S5). Notation: P-N5-SETTLE §1 (Ξ_k, σ̄_k, W_k, ℓ_k, H_k, Iσ_k, W-run, C, D_k, [R57], [R15]).

## 0. Answer in one paragraph
- Own-node flips and cosmetic CN switches change no value.
  - An Odd o with λ_Ξ(o) = o has Ξ(o) = (o, ∅, 0) whatever σ̄(o) is.
  - An Even c ∈ C has W-values that end at c, so σ(c) does not enter any W-value.
- They are events in HEAD-RED′ only because R143 / P-N5-SETTLE read the heads at the TARGETS σ̄_k(g). A flip moves the target, so it has to
  count as an event.
- Read the heads at the SOURCES instead: the deviating Odd vertices D_k and the W-cycle nodes C.
  - Every vertex before the first source on a play follows τ or σ, so the play argument (PLAY-CAUSE) goes through unchanged.
  - The induction of RUN-SETTLE goes through without any σ̄ event and without the CN event. A C-only transition with no source event
    freezes Ξ, W and σ off C (§2.3). So the C-only transitions form a tail of the block, in which each c climbs strictly in a frozen Ξ.
- That is §2's Theorem SRC-SETTLE.
- XCN and CN are NOT O(1) per W-run (§3: 4 and 3 at one vertex). Whether they can be super-linear is not settled. After §2 it no longer
  matters for G-N5-TIME.

## 1. Definitions (a W-run F, τ and C fixed)
- D_k := {Odd o : σ̄_k(o) ≠ τ(o)} (P-N5-SETTLE §1).
- SOURCES S_k := D_k ∪ D_(k+1) ∪ C, for a transition k → k + 1.
- SOURCE EVENT: a transition k → k + 1 of F with Ξ_(k+1)(v) ≠ Ξ_k(v) for some v ∈ S_k. E^S_F := the number of source events.
- HXS_F(v) := the number of transitions of F with v ∈ S_k and Ξ_(k+1)(v) ≠ Ξ_k(v). So E^S_F ≤ Σ_v HXS_F(v).
- A transition is C-ONLY if every Even vertex that switches at it is in C. It is NORMAL otherwise.
- m_C := Σ over Even c ∈ C of (|succ(c)| − 1) ≤ m_E.

## 2. Theorem SRC-SETTLE (PROVED, lane; premises exactly those of RUN-SETTLE: [R57], [R15] (a), ARENA-MAX, Claim RG′, LEX-BFS / IDX-MONO)
- Statement.
  - Let k0 → … → k1 be consecutive transitions of a W-run F, none of them a source event (a SOURCE BLOCK). Put j := k − k0.
  - (S_j) Every Even y ∉ C that switches at k has ℓ_(k+1)(y) ≥ j + 1.
  - (X_j) Every x with Ξ_(k+1)(x) ≠ Ξ_k(x) has ℓ_(k+1)(x) ≥ j + 1.
  - (T) If the transition at k is C-only, so is every later transition of the block.
  - Hence k1 − k0 ≤ (n − 1) + m_C.
- Corollary SRC-COUNT. |F| ≤ E^S_F + (E^S_F + 1)(n − 1 + m_C).
  - So polynomial W-runs ⟺ Σ_v HXS_F(v) polynomial (⇐ by the corollary; ⇒ since HXS_F(v) ≤ |F|).
- Against HEAD-RED′ (L-SI box 53 §3, READING):
  - the terms CN_F, XCN_F, the σ̄-flip events (i) and ROOT-FLIP are not used;
  - the heads are D ∪ C (the sources) in place of U′ = U ∪ τ(Odd) (the targets).

### 2.1 Lemma PLAY-CAUSE^S
- Statement. If k → k + 1 is not a source event and Ξ_(k+1)(x) ≠ Ξ_k(x), then some Even y ∉ C switches at k and lies on x's
  (σ_(k+1), τ)-path to λ_W(x). In particular ℓ_(k+1)(x) ≥ ℓ_(k+1)(y).
- Proof.
  - Let x = y_0, y_1, … be the (σ_(k+1), σ̄_(k+1))-play, and i the least index with y_i ∈ S_k.
  - i exists. An Odd y_t ∉ D_(k+1) follows τ, so until S_k the play is the (σ_(k+1), τ)-path, which reaches λ_W(x) ∈ C ⊆ S_k.
  - Every VJ value on a play is (cycle node w, the relevant vertices of the path to w, the length of that path).
    - If w = y_j for some j < i, Ξ_(k+1)(x) is fixed by y_0 … y_j and the cycle node of Ξ_(k+1)(y_i).
    - Otherwise Ξ_(k+1)(x) = y_0 ⊕ … ⊕ y_(i−1) ⊕ Ξ_(k+1)(y_i).
    - Either way, Ξ_(k+1)(x) is a function of the segment y_0 … y_(i−1) and of Ξ_(k+1)(y_i).
  - Suppose no Even y_t with t < i switches at k.
    - The Odd y_t with t < i are not in D_k (D_k ⊆ S_k), so σ̄_k(y_t) = τ(y_t).
    - So the (σ_k, σ̄_k)-play from x is y_0 … y_i …, and the same function gives Ξ_k(x) from Ξ_k(y_i).
    - Ξ_k(y_i) = Ξ_(k+1)(y_i), since there is no source event. So Ξ_k(x) = Ξ_(k+1)(x), a contradiction.
  - So some Even y_t with t < i switches. It is not in C (C ⊆ S_k and t < i), and it lies on x's (σ_(k+1), τ)-path before λ_W(x). So
    ℓ_(k+1)(x) = t + ℓ_(k+1)(y_t). □
- Difference from PLAY-CAUSE (P-N5-SETTLE §4):
  - The stop set is S_k, not D_(k+1) ∪ C.
  - The value used is Ξ(y_i) at the source, not Ξ(y_(i+1)) at the target.
  - Neither «σ̄_k = σ̄_(k+1)» nor «C does not switch» is used.

### 2.2 (S_j), (X_j): the RUN-SETTLE induction, restricted to Even vertices outside C
- (X_j) follows from (S_j) by PLAY-CAUSE^S.
- (S_0) holds trivially: y ∉ C means ℓ_(k+1)(y) ≥ 1.
- For j ≥ 1, take P-N5-SETTLE §5's proof verbatim, with the following changes.
  - «switched Even y» → «switched Even y ∉ C».
  - (MIN) → «no Even u ∉ C with ℓ_(k+1)(u) < L switches at k».
  - (PATH) is read on the path from b up to c, c EXCLUDED.
    - A W-value (c, P, ℓ) of a vertex b ≠ c depends only on the path from b to its first visit of c, so σ(c) does not enter it.
    - Every vertex of that path except c is outside C (a W-path to c meets no other cycle node).
    - So (MIN) restricted to non-C vertices still gives W_k(b) = W_(k+1)(b), and gives the same path up to c.
  - Case 1 uses X_(j−1), now from PLAY-CAUSE^S.
  - Case 2a uses keys of (σ, τ)-paths up to c, c excluded (T54's key_σ(x) = (x_(ℓ−1), …, x_0)). They are unchanged by the restricted
    (MIN) / (PATH).
  - Case 2c: «u ∉ C» holds because u lies on a's path strictly before c. Some non-C vertex on that path must switch: if only c switched,
    a's (σ_(k+1), τ)-path to c would equal its (σ_k, τ)-path, which avoids y.
  - Cases 2b and 2c use ARENA-MAX and W-MON only. Both are unchanged.
- Nothing else in §5 uses events (i) or (ii). □

### 2.3 The bound on a C-only transition's successor
- (T0) Let k → k + 1 be a C-only transition of F that is not a source event. Then:
  - Ξ_(k+1) = Ξ_k, by PLAY-CAUSE^S (no Even outside C switches);
  - W_(k+1) = W_k on every vertex (σ changed only on C; a W-value does not depend on σ at its cycle node);
  - H_(k+1) ⊆ H_k.
    - Off C: σ_(k+1) = σ_k, and Iσ_(k+1) = Iσ_k because Ξ is unchanged.
    - At c ∈ C that switched from a to b: b ∈ Iσ_k(c), and Iσ_(k+1)(c) = {z : Ξ(z) ▷ Ξ(b)} ⊆ Iσ_k(c), since Ξ(b) ▷ Ξ(a).
- (T1) Then σ_(k+2) = σ_(k+1) off C, so k + 1 → k + 2 (if it is in F) is C-only.
  - W_(k+2) = W_(k+1).
    - ⊵ holds by ARENA-MAX at k + 1 with ρ = σ_(k+1) ∈ H_(k+1).
    - ⊴ holds by ARENA-MAX at k with ρ = σ_(k+2) ∈ H_(k+1) ⊆ H_k, which gives W_(k+1) ⊵ W_(k+2).
  - By Claim RG′ with LEX-BFS / IDX-MONO, σ_(k+2)(x) for x ∉ C is the ≺-least W_(k+2)-tight edge of x's arena.
    - The arenas off C, the tight sets and the branch (parity of λ_W(x)) are those of the step k → k + 1.
    - ≺ is either the static index order or the key order on σ_(k+2) at lower layers.
    - Induction on the layer ℓ, starting at layer 1, whose only tight successor is the cycle node: σ_(k+2) = σ_(k+1) off C.
- (T) follows by induction along the block.
- In the C-only tail of a block, Ξ is constant (T0). So each Even c ∈ C switches only to a successor that is strictly Ξ-better than its
  current one, under one fixed Ξ. That is at most |succ(c)| − 1 switches, so the tail has at most m_C transitions.
- The normal transitions all precede the tail. Each switches some y ∉ C with j + 1 ≤ ℓ_(k+1)(y) ≤ n − 1, so there are at most n − 1
  of them.
- So a block has k1 − k0 ≤ (n − 1) + m_C. □
- READING: a C-only tail also ends the W-run soon. When no c can climb any more, S4a returns σ unchanged, and with τ fixed that is an
  S4c fallback, or else τ changes.

### 2.4 The two small facts behind «cosmetic»
- (F1) A CN switch at an Even c ∈ C leaves Ξ(c) unchanged only if λ_Ξ(c) = c at k or at k + 1.
  - Proof. Let c switch a → b, so b ∈ Iσ_k(c) and Ξ_k(b) ▷ Ξ_k(a). If c is not a Ξ-cycle node at k or at k + 1, then
    Ξ_(k+1)(c) = c ⊕ Ξ_(k+1)(b) ⊵ c ⊕ Ξ_k(b) ▷ c ⊕ Ξ_k(a) = Ξ_k(c). Here ⊕ by c preserves ◁: it leaves the cycle node's reward unchanged
    and is monotone for one cycle node. □
  - (F1) is not used in §2. It explains why CN^own is the only part of CN that §2.3's tail has to absorb.
- (F2) A σ̄-flip at an Odd o with λ_Ξ(o) = o at k and at k + 1 changes no Ξ-value.
  - Ξ is a function of σ alone (S1), and Ξ(o) = (o, ∅, 0).
  - Every value whose play enters o is (o, path to o, length), so it does not depend on σ̄(o).

## 3. DATA (n5b SPEC; xeng = L-NEW's n5.py on L-SI's si.py; Oink 8fbf0a7 --zlk plus verify)
- Tools (experiments/red/xcn/):
  - xcn.py counts per W-run (R89's definition): CN, CN per c, XCN, XCN per o;
  - xsearch.py: random search;
  - xclimb.py: hill climb on one-vertex XCN / CN;
  - srcsettle.py checks §2 on a trace: VIOL = RUN-SETTLE's (S_j)/(X_j) with source events plus CN; VIOL2 = §2's (S_j)/(X_j) with source
    events only; TAILV = (T); BLKV = the block bound; CNOX = (F1);
  - srcrand.py: srcsettle on random games;
  - runsrc.sh: the corpus run.
- Random games, 12,000, n 5-12, random starts (xsearch, seeds 1-4):
  - 30,855 W-runs;
  - Σ CN = 115 and Σ XCN = 50;
  - never more than 1 of either in one W-run.
- Hill climb (xclimb.py, 4 runs of 25 min, n 9 and 12, 400 steps per restart; KEY = the one-vertex count in one W-run).
  - XCN at ONE own node: 4 in a W-run of length 4 (pin xcn/instances/xcn4_n12, Odd vertex 0, succ 3, 6, 10, 11).
    - An earlier climb state (n 12, XCN 3 at Odd vertex 2, succ 1, 4, 5, 6) shows the mechanism: flips 5 → 6 → 5 → 4.
    - The S1 DFS pushes all of o's successors and pops the highest index first, so σ̄(o) is the popped successor whose push-subtree
      first meets a predecessor of o.
    - Each flip is the popped successor leaving that subtree: σ(6) = 10 → 1, an already-marked sibling; then σ(5) = 2 → 11, priority
      21 > 17. σ(5) returns to 11 after Ξ(11) rose: its path set gained vertex 0, of priority 24.
  - CN at ONE W-cycle node: 3 in a W-run of length 3 (pin xcn/instances/cn3_n9, Even vertex 1).
    - All 3 switches are cosmetic: λ_Ξ(1) = 1, so CNO 3 of 3.
    - The W-run has NO source event (Es2 0). Its single source block of length 3 ends in a C-only tail of length 2. This is §2.3's
      tail; the bound there is n − 1 + m_C = 8 + 9.
  - Both pins: xeng state sequences identical; Oink --zlk winners equal and verify passes (rel2/oinkcmp.sh: OINK OK).
  - So XCN and CN are NOT O(1) per W-run. Nothing here shows them super-linear. Climb values 3-4 at n ≤ 12 are what a linear bound
    would also allow.
- Random games, 12,000 (xsearch.py seeds 1-4, n 5-12, random starts): 30,855 W-runs, Σ CN 115, Σ XCN 50, never more than 1 of either in
  one W-run.
- Corpus (box 50b: sbcg 719 + alt 413 = 1,132 games, 300 s each; xcn/runsrc.sh → xcn/src_corpus.txt).
  - 1,130 games analysed. 2 RUN-ERROR: n3cov_phi and n3cov_lean, the known invalid starts of R99.
  - VIOL 0, VIOL2 0, TAILV 0, BLKV 0, CNOX 0.
  - Events summed over all W-runs: E (R143 / P-N5-SETTLE events) 4,724; Esrc (source events plus CN) 4,554; Es2 (source events only,
    §2) 4,546.
  - FLIPONLY 513: transitions that are R143 events only through a σ̄-flip. §2 does not count them (most of them start a new source
    block anyway).
  - CN 37, of which cosmetic (CNO) 11.
  - Longest source block (maxblk2) 67 (gate_K64_n581, n 581). Longest C-only tail 1. Max HXS at one vertex 61 (gate_K64_n581).
- Random check (srcrand.py, seeds 11-14, 2,500 games each, n 6-14): see §3.1.

### 3.1 Final numbers
- srcrand.py, seeds 11-14, 2,500 games each, n 6-14 (xcn/srcrand_out.txt):
  - VIOL 0, VIOL2 0, TAILV 0, BLKV 0, CNOX 0;
  - CN 96, of which cosmetic 94.
- This is WEAK evidence. Random games have short W-runs (max |F| 3 here). The corpus above, with |F| up to 159, is the real test.
- check.sh «R147» pins: xcn4_n12, cn3_n9 (sha1, xcn.py / srcsettle.py outputs, xeng, Oink), and srcrand seed 1 (300 games).

## 4. What is open, exactly
- G-N5-TIME: OPEN. Theorem SRC-SETTLE is a REDUCTION. Its residual is HXS-POLY: Ξ-changes at the deviating Odd vertices and at the W-cycle
  nodes, per W-run, polynomial.
- Relation to L-SI's residual HX′-POLY (Ξ-changes at U ∪ τ(Odd)), READING:
  - At a non-own g ∈ D_k with σ̄(g) unchanged, Ξ(g) = g ⊕ Ξ(σ̄(g)), so a Ξ-change at g IS a Ξ-change at its target.
  - A Ξ-change at a target that Odd answers with a tie re-order does not change Ξ(g). §2 does not count it; HEAD-RED′ does.
  - On the corpus E^S ≈ E (§3), so the gain is in the proof (no ROOT-FLIP, no flip or CN terms), not in the counts.
- The kill target is unchanged, but now stated on sources:
  - make Ξ(g) rise super-polynomially often at one deviating Odd vertex g (or at a W-cycle node) inside one W-run;
  - Ξ(g) is Odd's optimal value at g, so each rise is a rise of the minimum over succ(g).
- Not done: a super-linear XCN or CN family. §2 makes both irrelevant to G-N5-TIME, so I did not build one.
