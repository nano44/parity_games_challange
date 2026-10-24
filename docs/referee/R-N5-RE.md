# Referee report R-N5-RE: Lemmas G, Wo, RM, RE, PIECE on N5 in one-Odd-choice games (box 26)

Referee: REFEREE (successor 4), Opus 5.5 (owner ruling D15, Lead reading L37). Packet P-N5-RE: the Lead's message of 2026-10-24 14:20Z.
Pin: trunk claude/vibrant-johnson-nxvvxo 52c7261 (merged here by fast-forward to 4332f9fc; 52c7261 is an ancestor, and 52c7261..4332f9fc
touches only docs/agents/LEAD-STATE.md). Object: docs/new/P-N5-RE-box26.md, sha1 8dba4576950d4888b90d4c0cc86217b9b8fec745 (verified
at the pin and in the working tree). L-NEW successor 9.
Context read: SPEC S1-S5 of docs/new/N5-ssi-global.md; RESULTS R15, R17, R18; docs/new/N5-phase-bound-box10.md §1-§3 ((V1), (V2), (F1),
Lemma P, Theorem PH); docs/new/N5-time-box21.md §1-§2.6 and §3.5 (the box 21 Lemma G); experiments/new/box21/n5x.py, h1.py,
experiments/new/box25/common.py, thtrace.py, wdrop_h.py, wocheck.py, piececheck.py, reentry.py (read-only); notes/REFEREE.md and my
predecessor's R-N5-1P / R-N5-1OA for precedent. docs/referee-2/ was NOT read.
Written 2026-10-24 14:22Z-14:40Z by date -u. Every verdict is labelled (Opus 5.5, D15).
Notation as in the packet: Ξ_k honest valuation of σ_k (against σ̄_k), W_k the (σ_k, τ_k)-play values, θ_k = Ξ_k(o), w_k = W_k(o), R_k, F_k,
π_v, (h), joint λ-phase. "λ_k(v)" is the cycle node of Ξ_k(v).

## Verdict
| item | verdict (Opus 5.5, D15) |
|---|---|
| (1) Lemma G (a)-(c) | SIGNED |
| (2) Lemma Wo | SIGNED |
| (3) Lemma RM | SIGNED WITH GAPS: RM-1 (the "i.e." needs the route order defined free of the terminal; one line, given in §3) |
| (4) Lemma RE and Corollary RE | SIGNED WITH GAPS, and (NC) IS NOT NEEDED: RE-1 (step 2 has a false sentence and an avoidable hypothesis; replaced by a two-line argument that covers every case, §4.2), RE-2 (step 3 has a false justifying sentence; conclusion right by (V1), §4.3). With RE-1's argument, Lemma RE holds as stated WITHOUT (NC), and G26-1 can be closed |
| (5) Lemma PIECE | SIGNED WITH GAPS: P-1 (the count |R| − 1 is not R17 verbatim: 𝓡 has |R| + |K| vertices; the referee's contraction 𝓡* gives |R| − 1, §5.3), P-2 (the Consequence (READING) omits "inside one joint λ-phase") |
No step is WRONG in a way that breaks a statement. Two sentences in RE's proof are false as written (RE-1, RE-2); the statements survive.

## 1. Lemma G (a)-(c): SIGNED (Opus 5.5, D15)
- (a) v ∈ F_k: the σ_k-path from v never reaches o, so it meets only forced Odd vertices, at which σ̄_k and τ_k agree. Same play, same value.
  Checked.
- (b) v ∈ R_k. I checked the step "o's continuation avoids π_v" in full: if the honest play from o met u ∈ π_v, then from u it follows σ_k and
  forced Odd edges (no Odd choice before o) back to o, so o would lie on the cycle of its own honest play, against (h). The same argument for
  the W-play. So π_v followed by o's play is a simple path to c, and no u ∈ π_v is its own cycle node; iterated (V1) gives Ξ_k(v) = π_v ⊕ θ_k
  and W_k(v) = π_v ⊕ w_k. Note: the argument shows more, which PIECE and RE use: o's honest play and o's W-play avoid ALL of R_k \ {o}.
- (c) P(π_y ⊕ T) = A_y ∪ P(T) with A_y ∩ P(T) = ∅ (by (b): P(T) lies on o's play), so (A_y ∪ P(T)) Δ (A_z ∪ P(T)) = A_y Δ A_z, and the length
  difference is |π_y| − |π_z|; the cycle node c is common (h). Each of the three order keys is the same for T = θ_k and T = w_k, equality
  included. Checked.

## 2. Lemma Wo: SIGNED (Opus 5.5, D15)
b = τ(o) (the same at k and k+1). (h) at j excludes b = o and gives b ∈ F_j; Lemma G (a) gives W_j(b) = Ξ_j(b); o ≠ λ of its W-play, so (V1)
gives w_j = o ⊕ Ξ_j(b); R15 (a) at b, then (V2) with both paths avoiding o (b ∈ F_j at both j). Every step checked. Remarks (no gap): the
lemma uses no λ-phase and no N5 property beyond R15 (a); τ fixed is used only for b being the same vertex at k and k+1.

## 3. Lemma RM: SIGNED WITH GAPS (Opus 5.5, D15)
The displayed claim π_x^{k+1} ⊕ θ ⊵ π_x^k ⊕ θ is Lemma G (b) at k and at k+1 plus R15 (a) at x: correct.
- RM-1 (wording). The "i.e." identifies this with the route order of Lemma G (c), which G (c) defines only for two routes AT ONE STATE (terminal
  θ_k or w_k). Here the routes are at two states. The identification holds with this definition: route π ⊴ route π' iff (c, A_π, |π|) ⊴
  (c, A_π', |π'|), i.e. the comparison against the terminal (c, ∅, 0). Then π ⊕ T ⊴ π' ⊕ T for EVERY terminal T with cycle node c whose path set
  is disjoint from A_π ∪ A_π' (the proof of G (c) verbatim). θ qualifies at both states by (h) at k and at k+1. One line; CLOSED by this text.
- Remarks: the joint λ-phase and τ constant are not used (c is fixed by θ constant).

## 4. Lemma RE: SIGNED WITH GAPS, (NC) not needed (Opus 5.5, D15)
### 4.1 Steps 1, 4, 5: checked
Step 1: if no vertex of π_x^L switched, the (L+1)-path from x is π_x^L and reaches o; o is not on π_x^L and the other Odd vertices are forced.
So a first switched y exists, y is Even and y ∈ R_L. Step 4: R15 (a), E − L times. Step 5: Lemma G (b) at L and E+1 (needs (h) only there),
then θ_{E+1} = θ_L. Correct.

### 4.2 Step 2 (strict gain at y): RE-1, and a proof without (NC)
Two problems in the packet's step 2:
- The chain inserts y ⊕ Ξ_L(z), which needs Ξ_L(z)'s path to avoid y. The caveat claims: "if z's L-path passed y, then z ∈ R_L and y's new play
  would cycle back through y, which is case (i)". The first half is right (o's play avoids R_L \ {o}, §1 (b)), the second is NOT: vertices on z's
  L-path between z and y may switch at L → L+1 too (y is the first switched vertex on π_x^L, not on z's path), and then y's new play need not
  return to y. DATA: this situation (z's honest L-path passes y, y NOT on its new honest cycle) occurs at 1,852 switches in my probe (§6), 18 of them
  on the pinned instances (fts_best16: 5). None of them was in RE's exact setting (y ∈ R_L inside a joint λ-phase with τ fixed and (h) at L),
  but the sentence is false as an implication and the proof as written does not cover that case.
- Case (i) ∧ (ii) is excluded by hypothesis (NC), but it does not need to be.
Replacement (covers every case at once, no (NC)). Let z := σ_{L+1}(y) ≠ σ_L(y).
1. λ_L(y) = c ≠ y (packet, first bullet: y ∈ R_L and (h)), and λ_{L+1}(y) = λ_L(y) = c (joint λ-phase). So y is its own cycle node at
   neither state.
2. (V1) at L and at L+1: Ξ_L(y) = y ⊕ Ξ_L(σ_L(y)) and Ξ_{L+1}(y) = y ⊕ Ξ_{L+1}(z), and BOTH paths (σ_L(y)'s at L, z's at L+1) avoid y.
   (V1) holds also when y lies on its own cycle with top c ≠ y: the path from y's successor to c ends at the first visit to c, before the cycle
   returns to y. So case (i) is included.
3. The gate: z ∈ Iσ_L(y) (S4a arena = {σ_L(y)} ∪ Iσ_L(y); S4c switches inside Iσ), so Ξ_L(z) ▷ Ξ_L(σ_L(y)). R15 (a) at z: Ξ_{L+1}(z) ⊵ Ξ_L(z).
   Transitivity: Ξ_{L+1}(z) ▷ Ξ_L(σ_L(y)). (No prefix is taken here, so Ξ_L(z)'s path never needs to avoid y.)
4. Strict (V2) applied once, to a = Ξ_L(σ_L(y)) ◁ b = Ξ_{L+1}(z), whose paths both avoid y (item 2): y ⊕ b ▷ y ⊕ a, i.e.
   Ξ_{L+1}(y) ▷ Ξ_L(y). □
In the (i) ∧ (ii) case this reads: Ξ_{L+1}(z) = (c, ∅, ℓ' − 1) ▷ Ξ_L(σ_L(y)) = (c, ∅, ℓ_L − 1), so ℓ' ≠ ℓ_L in the direction favoured by c's
parity, and Ξ_{L+1}(y) ▷ Ξ_L(y) strictly. The packet's "may equal Ξ_L(y) if the lengths agree" cannot happen: the lengths are forced apart by
the gate and R15 (a).
In general form (what was proved): AT ANY N5 TRANSITION, every Even y whose σ changes and which is its own cycle node neither before nor after
gains strictly. No class, (h), phase or τ hypothesis is needed for this form; RE uses the phase only to get λ_{L+1}(y) ≠ y. This is the
classical "switched non-cycle-node vertex strictly improves" fact, and it is consistent with R15's side finding (strictness fails only at
cycle nodes).
DATA (§6): 17,473 such switches, 0 non-strict; the (NC) case (λ constant, y on its new honest cycle, empty path set at L) 494 times, all strict.
Negative control: switched y that ARE their own cycle node at L or L+1: 57 of 446 non-strict, so the probe distinguishes.
So: (NC) IS NOT NEEDED. Lemma RE holds under (h) at L and E+1 in one joint λ-phase with τ constant; G26-1's residue (NC) is closed by this
argument (pending the second referee).

### 4.3 Step 3 (strict gain at x): RE-2
The packet's last sentence ("The prefix avoids y's new play: otherwise x's new play would pass a prefix vertex twice") is not a valid reason: a
play may pass a vertex twice (it is a lasso), and y's new play CAN pass a prefix vertex u (then u, y lie on the new cycle with top c). The
conclusion holds anyway by the argument of §4.2: for each prefix vertex u_i (i < j, u_j = y), u_i ∈ R_L gives λ_L(u_i) = c ≠ u_i, the phase gives
λ_{L+1}(u_i) = c ≠ u_i, (V1) at both states gives Ξ_s(u_i) = u_i ⊕ Ξ_s(u_{i+1}) with both paths avoiding u_i (σ(u_i) is unchanged), and strict
(V2) carries Ξ_{L+1}(u_{i+1}) ▷ Ξ_L(u_{i+1}) to u_i. Induction from y back to x. CLOSED by this text.

### 4.4 Corollary RE: checked
θ is non-decreasing (R15 (a) at o), so θ_{E+1} ≠ θ_L iff a θ-change lies in (L, E+1]; x's intervals (L, E+1] are disjoint (the next leave is
≥ E+1); so x's non-ROUTE re-entries ≤ #θ-changes, and the sum over < n vertices gives the display. Hypotheses as stated ((h) at every leave and
re-entry). With §4.2 the clause "(NC) holds at every leave" can be deleted.

## 5. Lemma PIECE: SIGNED WITH GAPS (Opus 5.5, D15)
### 5.1 Steps 1-4: checked
- Closure: R constant across the stretch forces every switch of x ∈ R \ {o} to stay in R and of x ∈ F to stay in F (a switch of x ∈ R into F
  would put x in F_{k+1} = F). Forced Odd vertices of F have their successor in F; o's successor b ∈ F by (h). Correct.
- 𝓡's terminal: plays through o have value π ⊕ val(K) = π ⊕ w_{k_0} = π ⊕ w (π ⊆ R, K ⊆ F disjoint). W_k|R = 𝓡-values of σ_k|R by Lemma G (b) and
  w_k = w. Correct.
- Gates: for x, z ∈ R the comparison of z with σ(x) ∈ R is Lemma G (c) at state k; for F, Lemma G (a). Correct.
- Steps: τ is constant and there is no S4c, so every transition has Iσ_k ≠ ∅ and σ_{k+1} is S4a's arena optimum (if Iσ_k = ∅, the transition
  would have to change τ or fall back). For an 𝓡-arena strategy ρ, the extension by σ_{k+1} on F lies in the S4a arena; plays from R either
  cycle inside R (same in both games) or reach o and continue along σ_{k+1}'s play from b ⊆ F, with value π ⊕ w_{k+1} = π ⊕ w = the 𝓡-value. (F1)
  for the S4a arena then gives W_{k+1}|R ⊵ ρ's 𝓡-values, and σ_{k+1}|R is in the arena, so it is a pointwise optimum of 𝓡's arena. Same for 𝓕.
  R17's argument uses only that each step is A pointwise arena optimum (R17 (d), and Lemma P's proof uses only (F1)), and a step with
  σ_{k+1}|R = σ_k|R is admissible in that proof. Correct.

### 5.2 Step 5: the phase structure: checked
𝓕's cycle nodes are Ξ's on F (Ξ = W on F), constant in the joint λ-phase: one 𝓕-phase. In 𝓡, every R vertex reaches o at every state of the
stretch: one phase. A value change on R (of Ξ or W) is a change of (A_v, |π_v|), i.e. of the 𝓡-value; on F of the 𝓕-value. Correct.

### 5.3 P-1: the count |R| − 1 is not R17 verbatim
R17 Theorem PH bounds value-changing steps of a phase by N − 1, N the number of vertices of the one-player game. 𝓡 has the |R| + |K| vertices
R ∪ K, so the verbatim bound is |R| + |K| − 1, not |R| − 1, and the packet's "(|R| − 1) + (|F| − 1) ≤ n − 2" does not follow as written (the
verbatim total is ≤ |R| + |K| + |F| − 2 ≤ 2n − 3, still linear).
Repair (the referee's; this closes P-1). Let 𝓡* be the one-player game on R alone in which o has a self-loop and o's priority is replaced by c's
(c ∉ R, so injectivity holds). For a play reaching o, map (c, A_π ∪ P(w), |π| + ℓ(w)) in 𝓡 to (o*, A_π, |π|) in 𝓡*; plays cycling inside R map to
themselves. Two o-reaching values compare the same way in both games (same cycle-node key, symmetric difference A_π Δ A_π', length difference
|π| − |π'|, the parity of c); an o-reaching value and an internal cycle compare the same way (cycle-node keys of c and o* are equal). So the map
is an order isomorphism on every value an 𝓡-arena strategy gives to R, the improving sets coincide, arena optima correspond, and σ_k|R runs
switch-best on 𝓡*, which has |R| vertices: at most |R| − 1 value-changing steps in its single phase (R17 Theorem PH). With 𝓕's |F| − 1 the
packet's (|R| − 1) + (|F| − 1) = n − 2 holds. DATA (§6): the split bounds (R-changes ≤ |R| − 1 and F-changes ≤ |F| − 1, separately) hold at
480 in-piece transitions, and BOTH are attained with slack 0 in the random samples, so neither can be lowered.

### 5.4 P-2: the Consequence (READING)
"In a stretch with τ, θ, w constant and (h), each fallback-free run between crossings is a piece" omits "inside one joint λ-phase", which the
lemma assumes and step 5 uses (𝓕 can change phase while θ and w stay constant). With that clause added, the count (n − 2)·(X + F + 1) + X + F ≤
(n − 1)·(X + F + 1) is right. A READING, not signed as a result.

## 6. Data (DATA, not proof)
### 6.1 The packet's checks (lane tools unmodified; experiments/new/box25/ at the pin; sha1 wocheck 4cdd0306…, piececheck e4d7508e…,
reentry 570d745d…, common 4c1dc30b…)
| instance (n) | wocheck pairs / W_o_DECREASE | piececheck max piece (≤ n − 2) / violations | reentry classes (OTHER) |
|---|---|---|---|
| fts_best16 (16) | 27 / 0 | 6 / 0 | ROUTE 2, THETA 2 (0) |
| theta_tp32 (32) | 42 / 0 | 10 / 0 | THETA 4 (0) |
| returns_rt48 (48) | 79 / 0 | 6 / 0 | ROUTE 21, THETA 21 (0) |
| returns_ph64 (64) | 104 / 0 | 9 / 0 | ROUTE 30, THETA 23 (0) |
| tr20_s4 (20) | 17 / 0 | 1 / 0 | ROUTE 3 (0) |
| i1h_fts_best16 (11) | 6 / 0 | 1 / 0 | ROUTE 2 (0) |
| rtt24 (24) | 13 / 0 | 10 / 0 | none |
| thetare_n (11) | 6 / 0 | none / 0 | ROUTE 1, THETA 1 (0) |
| fbh_drop9 (9, its .start) | 2 / 0 | none / 0 | none (1 leave) |
No (h)-failure at any re-entry (no "_noh" counter). Random samples (fresh seeds): wocheck 3,000 games seed 141 (821 pairs) and 3,000 seed 142
--randstart (1,196 pairs): 0 decreases. piececheck 3,000 seed 903 and 3,000 seed 904 --randstart: 0 violations (max piece 2). reentry 3,000 seed
901 and 3,000 seed 902 --randstart: 302 and 435 leaves but NO re-entry at all, so random re-entry samples of this generator are VACUOUS for RE;
the evidence for RE's classes is the pinned instances only (THETA re-entries exist, so the θ-alternative is needed, as the packet says).
### 6.2 Referee's probe docs/referee/scratch/re_probe.py (n5x.step read-only; the pinned instances above + random 𝒞^1O 4,000 seed 2611, 4,000
seed 2612 --randstart, n 4-14; random two-player games 4,000 seed 2613, 4,000 seed 2614 --randstart, n 3-12)
- SW (§4.2 general form): 17,473 switches of non-cycle-node Even vertices, 0 non-strict. Of these, the (NC) case 494 (all strict), the caveat
  case of §4.2 1,852 (all strict). Restricted to RE's exact setting, both cases had 0 occurrences.
- RE3 (step 3 conclusion at every leave inside a joint λ-phase with τ fixed and (h) at L): 512 leaves, 0 non-strict.
- PSPLIT (§5.3): 480 in-piece transitions, 0 violations of either split bound, slack 0 attained for R and for F.
- Negative control: 1,500 random games, switched y that are their own cycle node at L or L+1: 57 of 446 non-strict.

## 7. Gaps (joint list for §C)
| id | item | kind | status |
|---|---|---|---|
| RM-1 | RM's "i.e.": route order across two states | wording | CLOSED here (§3) |
| RE-1 | RE step 2: false caveat sentence; (NC) unnecessary | proof step | CLOSED here by §4.2 (two-line replacement); (NC) and G26-1's residue can be dropped |
| RE-2 | RE step 3: false justifying sentence | proof step | CLOSED here (§4.3) |
| P-1 | PIECE count |R| − 1 vs R17's N − 1 on R ∪ K | proof step | CLOSED here by 𝓡* (§5.3); verbatim bound 2n − 3 otherwise |
| P-2 | PIECE Consequence omits the joint λ-phase | wording (READING) | open for L-NEW, one clause |
Not covered (the packet says so, §6 of it): non-(h) states, CYC, XING, FB-1O. G-N5-TIME stays OPEN. Nothing here is a running-time bound or a
TARGET.md claim; TARGET.md diff: these are lemmas about the candidate N5 on 𝒞^1O (a subclass solvable in polynomial time by other means), not
statements of TARGET.md §2.
