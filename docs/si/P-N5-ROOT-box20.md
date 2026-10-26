# P-N5-ROOT-box20: S4a steps are Bellman-Ford rounds off the disagreement region, path weights freeze on it while it does not grow, and a D-direct Odd vertex then moves ≤ deg − 1 times (BF-F_D, FREEZE-A, ROOT-PIECE, DL-SPLIT)
Packet for both referees. Author: L-SI successor 16 (Opus 5.5; D18, L40). Source: lane note docs/si/N5-ROOT-box20.md §2-§4, §7.2 (not
frozen; this packet is). Written at the Lead's request of 14:25Z (Lead's stamp: "at your box end or handover, freeze packet P-N5-ROOT-box20:
BF-F_D, FREEZE-A, ROOT-PIECE, plus the G_c result"). Stamp of the freeze: the commit (date -u).
Scope (D1): lemmas inside one phase of N5 on EVERY game. ROOT-PIECE is a REDUCTION: it bounds path-weight changes of an Odd vertex by
(f + G_c + 1)·poly(n), and G_c (the A-gains) is NOT bounded here. Nothing here bounds N5's running time, ρ, N_ep or f. Not a TARGET.md claim.
G-N5-TIME stays OPEN.
Quotes: every «…» is verbatim from the tagged source; [Q path@commit:lines] is checked by
`python3 -I experiments/si/rund/quotecheck.py docs/si/P-N5-ROOT-box20.md` (QUOTES PASS; whitespace normalised; "…" separates parts).
Pinned in experiments/si/check.sh.

## 0. What to sign
- §2 Lemma BF-F_D; §3 Theorem FREEZE-A (a)-(c) and its length remark (R-LEN); §4 Corollary ROOT-PIECE; §5 Lemma DL-SPLIT (CONDITIONAL on
  Corollary RELAY-CHAIN of packet P-N5-CHOSEN-box19, in review, in case (i) only).
- Not to sign: §6 (the map of FRZ-U's single-gate steps, READING; the DATA; what is open).

## 1. Setting, premises and cited text
- N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md, FIX 1-4) with the standing premise 1E-N3, as in RESULTS R55-R69. A PHASE: a maximal run of
  states with λ_Ξ and τ constant (RESULTS R38 (a) KEY). Every in-phase transition is an S4a step (σ_{t+1} is Even's optimum of the arena H_t
  against τ: every Even v keeps σ_t(v) and its edges in Iσ_t, every Odd v keeps τ(v)) or an Even S4c fallback.
- Disagreement set and region, as landed: [Q docs/RESULTS.md@a7c141b8:2786-2787] «D_k := {Odd u : σ̄_k(u) ≠ τ_k(u)}; u(v) := the first vertex
  of D_k on v's (σ_k, τ_k)-play (v included), if any; R_D := {v : u(v) exists}, F_D := V ∖ R_D». W_k(v) is the value of the (σ_k, τ_k)-play
  from v.
- Classes and κ, as landed: [Q docs/RESULTS.md@a7c141b8:2839-2841] «for c ∈ C the honest class U_c := λ^{-1}(c). κ_t(z) := (signed weight of
  P(Ξ_t z), s_c·ℓ(Ξ_t z)) for z ∈ U_c, s_c := +1 if Ω(c) is odd, −1 if even; κwt_c(v) := (wt_c(v), s_c), wt_c(v) := sgn(v)·2^rank(v) if
  rank(v) > rank(c), else 0.» Write wt := wt_c, M_t(z) := wt(P(Ξ_t z)) (the first component of κ_t(z)), and for any valuation x with cycle
  node c, Mx := wt(P(x)); MW_t(z) := wt(P(W_t z)) when W_t(z) has cycle node c. For a vertex set Z, wt(Z) := Σ_{v ∈ Z} wt(v).
- New notation. U := U_c (constant on the phase). A_t := F_D(t) ∩ U. G[A]: the graph on A in which every Even v ∈ A ∖ {c} keeps its edges into
  A, every Odd v ∈ A ∖ {c} keeps the edge to τ(v) if τ(v) ∈ A, and c is a sink. MoptA(z) := max{wt(p ∖ {c}) : p a simple path of G[A] from z
  to c} (−∞ if none). An A-GAIN of class c: an in-phase S4a transition t → t+1 with A_{t+1} ⊄ A_t; G_c := their number in the phase.
  f := the in-phase fallbacks of the phase.
- Facts per honest class, LANDED as [Q docs/RESULTS.md@a7c141b8:2851] «(a) Facts (Aκ), (A0κ), (M1κ), (M2κ), (INJ), (SP′) per honest class»,
  stated in the source packet as [Q docs/new/P-N5-FBRED-box44.md@3732ab55:49-50] «(Aκ): for z ∈ U_c ∖ {c}: λ_t(z) = c ≠ z, so (V1) gives
  Ξ_t(z) = z ⊕ Ξ_t(next_t z) with cycle node c; next_t(z) ∈ U_c, and κ_t(z) = κwt_c(z) + κ_t(next_t z)». Used here in the forms:
  - (Aκ) for z ∈ U ∖ {c}: next_t(z) ∈ U and M_t(z) = wt(z) + M_t(next_t z) (next_t := σ_t at Even, σ̄_t at Odd vertices).
  - (A0κ) M_t(c) = 0 (Ξ_t(c) = (c, ∅, 0)).
  - (M1κ) for valuations x, x′ with cycle node c: x ⊴ x′ ⇔ (Mx, s_c·ℓ(x)) ≤ (Mx′, s_c·ℓ(x′)) lexicographically. This is a fact about
    valuations (VJ00's order with a common cycle node), so it is applied to W-values as well.
  - (M2κ) M_{t+1}(z) ≥ M_t(z) at every in-phase transition (Ξ_t ⊴ Ξ_{t+1}, then (M1κ)).
- Cited landed lemmas:
  - (F1) [Q docs/RESULTS.md@a7c141b8:738-739] «(F1)/(F2) (the optimum of a one-player game dominates every strategy of that game pointwise»,
    applied to S4a's arena H_t in G_τ; game-general by [Q docs/RESULTS.md@a7c141b8:2792-2794] «R17 (a)-(c), R18 (c) flat case, R18 (d) Lemma S
    (c) in its landed "⇒" form, R21 (a) XW, R21 (c) FBL-N (i), each signed under a 𝒞^1O setting line, whose proofs both referees read and
    CONFIRM use no one-Odd step (R17 and R18's flat case are one-player statements, applied to G_τ, its arenas and 𝓕, which are one-player on
    every game; XW is VJ00 (11) on G_σ)». (V1) is R17 (a) as well.
  - XW [Q docs/RESULTS.md@a7c141b8:933] «(a) Lemma XW: Ξ_k ⊴ W_k pointwise at every state», game-general by the quote above.
  - G_D (a) [Q docs/RESULTS.md@a7c141b8:2798] «(a) Lemma G_D (a) (no hypothesis): for every state k and every v ∈ F_D, Ξ_k(v) = W_k(v).»
  - κ-Y-FORM_D [Q docs/RESULTS.md@a7c141b8:2858-2859] «(d) κ-Y-FORM_D (per q ∈ Q ∩ U_c, q ≠ c, at a state t where q lies on no honest cycle):
    κ_t(q) = κwt_c(q) + min over y ∈ Y^q_t of κ_t(y), with Y^q_t := {y ∈ succ(q) ∩ U_c : y's honest play at t avoids q}».
  - Rewards are injective (SPEC S1), and values with different cycle nodes are ordered by the rewards of their cycle nodes first.
- A positional play is a lasso; a vertex on its cycle is visited before the first repetition. So the honest play of z ∈ U ∖ {c} up to its
  first visit of c is a simple path (used in §3 (b); stated directly, not via (SP′)).

## 2. Lemma BF-F_D
Statement. Let t → t+1 be an in-phase S4a transition, c a cycle node of the phase, U := U_c, and v ∈ U Even, v ≠ c, with v ∈ F_D(t) ∩ F_D(t+1).
Then for every successor x ∈ U of v: M_{t+1}(v) ≥ wt(v) + M_t(x).
Proof.
- Case 1: M_t(x) ≤ M_t(σ_t v). By (Aκ), M_t(v) = wt(v) + M_t(σ_t v) ≥ wt(v) + M_t(x); by (M2κ), M_{t+1}(v) ≥ M_t(v).
- Case 2: M_t(x) > M_t(σ_t v). σ_t(v) = next_t(v) ∈ U by (Aκ), so Ξ_t(x) and Ξ_t(σ_t v) have cycle node c, and (M1κ) gives Ξ_t(x) ▷ Ξ_t(σ_t v).
  So (v, x) ∈ Iσ_t and σ″ := σ_t[v ↦ x] is a strategy of the arena H_t. By (F1), W_{t+1} ⊵ W_{σ″} pointwise, W_{σ″} the value of the
  (σ″, τ)-play. v ∈ F_D(t+1), so by G_D (a) W_{t+1}(v) = Ξ_{t+1}(v), whose cycle node is λ_{t+1}(v) = c.
  - (i) x's (σ_t, τ)-play avoids v. It is also x's (σ″, τ)-play, and v's (σ″, τ)-play is v followed by it; v is not on its cycle, so (V1)
    gives W_{σ″}(v) = v ⊕ W_t(x).
    - XW: W_t(x) ⊵ Ξ_t(x), which has cycle node c. If W_t(x) had a cycle node u ≠ c, then reward(u) > reward(c); W_{σ″}(v) would have cycle
      node u, and W_{t+1}(v) ⊵ W_{σ″}(v) would give reward(λ(W_{t+1} v)) ≥ reward(u) > reward(c), against λ(W_{t+1} v) = c. So W_t(x) has
      cycle node c, and (M1κ) gives MW_t(x) ≥ M_t(x).
    - v ∉ P(W_t x) (that set lies on x's play). So W_{σ″}(v) has cycle node c and path weight wt(v) + MW_t(x), and (M1κ) on W_{t+1}(v) ⊵
      W_{σ″}(v) gives M_{t+1}(v) = MW_{t+1}(v) ≥ wt(v) + MW_t(x) ≥ wt(v) + M_t(x).
  - (ii) x's (σ_t, τ)-play passes v. Write it q · v · (v's (σ_t, τ)-play), q the part before the first visit of v (q = ∅ if x = v).
    - v ∈ F_D(t): v's (σ_t, τ)-play is its honest play (σ̄_t = τ off D_t), and W_t(v) = Ξ_t(v) (G_D (a)), with cycle node c. So x's (σ_t,
      τ)-play ends on c's cycle. Its path weight is the sum of wt over its distinct vertices: a vertex of nonzero wt has rank > rank(c) and is
      not on the cycle, whose top is c. Its vertex set is q ∪ (v's play), and a vertex of q that also lies on v's play lies on v's cycle and
      has wt 0. So MW_t(x) = wt(q) + M_t(v) = wt(q) + wt(v) + M_t(σ_t v), by (Aκ).
    - XW: Ξ_t(x) ⊴ W_t(x), both with cycle node c, so M_t(x) ≤ MW_t(x) by (M1κ). With Case 2, wt(q ∪ {v}) > 0.
    - v's (σ″, τ)-play is the cycle Z := v → x → q → v (every vertex other than v keeps its edge). wt(Z) > 0, so the vertex u* of largest
      rank among Z's vertices of rank > rank(c) is even (it dominates the signed sum), and every other vertex of Z is below it: u* is the top
      of Z. u* even with rank(u*) > rank(c) gives reward(u*) > reward(c).
    - (F1): W_{t+1}(v) ⊵ W_{σ″}(v), whose cycle node is u*, so reward(λ(W_{t+1} v)) ≥ reward(u*) > reward(c), against λ(W_{t+1} v) = c. So
      (ii) does not occur. □
- No hypothesis on the number of disagreement vertices, (h_D), (h3_D), H1 / H2 or the class is used. (i) does not use v ∈ F_D(t); (ii) does.
- On 𝒞^1O at H1 ∧ ¬H2 states (F_D = F) this is RESULTS R45 (d) BF-F; there the sub-case "x reaches o" is excluded by ¬H2, here it is
  absorbed by XW in (i).

## 3. Theorem FREEZE-A
Statement. Let c be a cycle node of a phase, U := U_c, A_t := F_D(t) ∩ U, and [s, e] states of the phase such that every transition t → t+1
with s ≤ t < e is an S4a step and A_{t+1} ⊆ A_t. Let L := max(|A_s| − 1, 0).
- (a) For t ∈ [s, e], z ∈ A_t and every simple path p of G[A_t] from z to c with ≤ t − s edges: M_t(z) ≥ wt(p ∖ {c}).
- (b) For t ∈ [s, e] and z ∈ A_t: M_t(z) ≤ MoptA_t(z). Hence for s + L ≤ t ≤ t′ ≤ e and z ∈ A_{t′}: M_{t′}(z) = M_t(z) = MoptA_t(z).
- (c) Let q ∈ U be Odd, and V_q := {wt(q) + M_{s+L}(y) : y ∈ succ(q) ∩ A_{s+L}} (≤ deg(q) values). At every state t ∈ [s + L, e] with
  σ̄_t(q) ∈ A_t, M_t(q) ∈ V_q. Hence at most deg(q) − 1 transitions t → t+1 with s + L ≤ t < e, σ̄_t(q) ∈ A_t and σ̄_{t+1}(q) ∈ A_{t+1} change
  M(q).
Proof.
- (a) Induction on t − s. If p has no edge, z = c and M_t(c) = 0 (A0κ). Step t → t+1: z ∈ A_{t+1}, z ≠ c, p = z · p′, p′ from x with ≤ t − s
  edges. G[A_{t+1}] is a subgraph of G[A_t] (A_{t+1} ⊆ A_t; Even edges into A_{t+1} are edges into A_t; Odd vertices keep their τ-edge, τ
  constant on the phase), so p′ is a simple path of G[A_t] and, by induction, M_t(x) ≥ wt(p′ ∖ {c}); also wt(p ∖ {c}) = wt(z) + wt(p′ ∖ {c}).
  - z Even: z ∈ A_{t+1} ⊆ A_t, so z ∈ F_D(t) ∩ F_D(t+1); BF-F_D gives M_{t+1}(z) ≥ wt(z) + M_t(x).
  - z Odd: z ∈ F_D(t+1), so z ∉ D_{t+1}, σ̄_{t+1}(z) = τ(z) = x and next_{t+1}(z) = x. (Aκ) at t + 1 and (M2κ): M_{t+1}(z) = wt(z) +
    M_{t+1}(x) ≥ wt(z) + M_t(x).
- (b) Let z ∈ A_t, z ≠ c. z's (σ_t, τ)-play avoids D_t and σ̄_t = τ at its Odd vertices, so it is z's honest play. Each vertex y on it has a
  suffix of it as its play, so y ∈ F_D(t), and λ(y) = c, so y ∈ U: the play stays in A_t. Up to its first visit of c it is a simple path (§1,
  last item) whose Even vertices use σ_t-edges into A_t and whose Odd vertices use τ-edges: a simple path of G[A_t]. By (Aκ), (A0κ) iterated,
  M_t(z) = wt(that path ∖ {c}) ≤ MoptA_t(z). For z = c both sides are 0.
  - Simple paths of G[A_t] have ≤ |A_t| − 1 ≤ L edges. So for t ≥ s + L, (a) gives M_t(z) ≥ MoptA_t(z), hence M_t = MoptA_t on A_t.
  - For s + L ≤ t ≤ t′ and z ∈ A_{t′} ⊆ A_t: M_{t′}(z) = MoptA_{t′}(z) ≤ MoptA_t(z) = M_t(z) ≤ M_{t′}(z) (fewer paths; (M2κ)).
- (c) Let t ∈ [s + L, e] with y* := σ̄_t(q) ∈ A_t.
  - If q ∉ D_t: q's honest play is q followed by y*'s, which avoids D_t, so q ∈ A_t ⊆ A_{s+L}, and M_t(q) = M_{s+L}(q) by (b). As
    q ∈ A_{s+L}, q ∉ D_{s+L}, so next_{s+L}(q) = τ(q), which lies on q's play and so in A_{s+L}; (Aκ): M_{s+L}(q) = wt(q) + M_{s+L}(τ q) ∈ V_q.
  - If q ∈ D_t: q's honest play continues in A_t and avoids D_t ∋ q, so q lies on no honest cycle; q ≠ c (c lies on y*'s play, so c ∉ D_t).
    By κ-Y-FORM_D, κ_t(q) = κwt_c(q) + min over y ∈ Y^q_t of κ_t(y), and by (Aκ) the minimum is attained at y*. Every y ∈ succ(q) ∩ A_t lies
    in Y^q_t (its honest play avoids D_t ∋ q). κ compares M first, so M_t(y*) ≤ M_t(y) for those y, y* among them: M_t(q) = wt(q) + M_t(y*),
    and M_t(y*) = M_{s+L}(y*) by (b) (y* ∈ A_t ⊆ A_{s+L}). So M_t(q) ∈ V_q.
  - M(q) is non-decreasing on the phase (M2κ). Over the states of (c) it takes ≤ deg(q) values in non-decreasing order, so it changes at ≤
    deg(q) − 1 of the counted transitions. □
- (R-LEN) On [s + L, e], Ξ on A_t changes only in its length (P fixed by (b) and (INJ) — signed weight is injective on sets of ranks above
  rank(c) — cycle node c), monotonically (Ξ non-decreasing), with lengths in [1, |U| − 1]. So the Ξ-changes of q at the transitions counted
  in (c) are at most deg(q)·(|U| − 1) − 1.
- On 𝒞^1O at H1 ∧ ¬H2 HN runs this is RESULTS R45 (e) FREEZE-F with A = F ∩ U and q = o (there A is non-increasing by R39 (a) SPLIT). It
  differs from RESULTS R55 (b) F1°_D (Ξ-changes on F_D ≤ |F_D| − 1 per D-crossing-free interval): A may shrink, and (c) covers q ∈ D.

## 4. Corollary ROOT-PIECE
Statement. In a phase with f in-phase fallbacks, for a cycle node c, U := U_c, G_c the A-gains of class c, and an Odd q ∈ U, let ρ^P_q(A) be
the number of transitions t → t+1 of the phase with σ̄_t(q) ∈ A_t, σ̄_{t+1}(q) ∈ A_{t+1} and M_t(q) ≠ M_{t+1}(q). Then
ρ^P_q(A) ≤ (f + G_c + 1)·(|U| + deg(q) − 2) + f + G_c, and the Ξ-changes of q at such transitions are ≤ (f + G_c + 1)·(|U| − 1)(deg(q) + 1) +
f + G_c.
Proof. Cut the phase at its fallback transitions and its A-gains (≤ f + G_c transitions, counted once each). The rest lies in ≤ f + G_c + 1
pieces satisfying FREEZE-A's hypothesis. In a piece, ≤ L ≤ |U| − 1 transitions lie before s + L, and ≤ deg(q) − 1 counted ones after it
(FREEZE-A (c)); with (R-LEN), ≤ (|U| − 1) + deg(q)(|U| − 1) − 1 Ξ-changes. □

## 5. Lemma DL-SPLIT (the A-gains by cause)
Statement. Let t → t+1 be an in-phase S4a A-gain of class c. Then (A) some entering vertex z ∈ A_{t+1} ∖ A_t has its first D_t-vertex u not in
D_{t+1} (a D-LEAVE at u: σ̄_{t+1}(u) = τ(u) ≠ σ̄_t(u)), or (B) z is unsplit at t (λ_{W,t}(z) = λ_t(z) = c) and leaves R_D by an Even switch.
In case (A), if the change of σ̄(u) is CLEAN in the sense of RESULTS R61 (e) ALT (u on no honest cycle at t and t + 1, and y2 := σ̄_{t+1}(u)
has an honest play at t that avoids u), with y1 := σ̄_t(u) and e1 := y1's exit (the first vertex of Q_c ∪ {c} on y1's honest play at t), one
of the following holds:
- (i) e1 ≠ c and Ξ(e1) changes at t → t+1: the transition carries a ROUTE, CYC or TOG event of class c (CONDITIONAL on P-N5-CHOSEN's
  Corollary RELAY-CHAIN, applied from e1's event);
- (ii) u has a ROUTE event at t → t+1 (some class exit path or exit of u differs at t and t + 1);
- (iii) e1 ≠ c and e1's honest play at t + 1 passes u (a TOG step at e1, as in Lemma CHOSEN), or κ_t(y2) = κ_t(y1) (a TIE).
Proof.
- Split. z ∈ A_{t+1} ∖ A_t: z ∈ R_D(t), with first D_t-vertex u. If u ∉ D_{t+1}, (A). Otherwise u ∈ D_t ∩ D_{t+1}, and z ∉ R_D(t+1). If z were
  split at t, RESULTS R63 (a) R-STICK_D (every split v ∈ R_D(s) lies in R_D(s+1) at an in-phase S4a transition) would put z in R_D(t+1). So z is
  unsplit at t, and since τ and σ̄(u) are unchanged on its old route up to u, some Even vertex of that route switched: (B).
- Case (A), none of (i), (ii), and not a TOG step at e1: the class exit paths and exits of u's options are the same at t and t + 1, and e1 has no
  event. y1's honest play at t + 1 is its (unchanged) exit path, which avoids u (it avoids u at t, as u is on no honest cycle at t and y1 =
  σ̄_t(u)), followed by e1's play, which avoids u (no TOG; for e1 = c, c's cycle avoids u as u is on no honest cycle at t + 1). So y1 ∈ Y^u_{t+1}.
  By additivity (P-N5-FLIP §1, signed as a proof step) κ_{t+1}(y1) = κwt_c(path) + κ_{t+1}(e1) = κ_t(y1) (κ(c) is constant on the phase).
  - κ-Y-FORM_D at t + 1 (u on no honest cycle), minimum attained at y2: κ_{t+1}(y2) ≤ κ_{t+1}(y1) = κ_t(y1).
  - κ is non-decreasing on the phase: κ_t(y2) ≤ κ_{t+1}(y2) ≤ κ_t(y1).
  - y2 ∈ Y^u_t (clean), so κ-Y-FORM_D at t (minimum attained at y1) gives κ_t(y1) ≤ κ_t(y2). Hence κ_t(y2) = κ_t(y1): a TIE, (iii). □
- Consequence: G_c ≤ #(B-gains) + #(S4a transitions carrying a ROUTE / CYC / TOG event of class c, or a tie or a non-clean change at a
  D-leaving vertex). This is a
  decomposition, not a bound: ROUTE events are ρ events again (READING, §6).

## 6. Not to sign: the map, the data, what is open (READING / DATA / OPEN)
- READING (note §1). In R50 FRZ-U's Claim P^c the step that uses D = {o} essentially is Fact B (Ξ- and W-orders agree) across two gates: Case B
  compares z and σ_k(x), which can have different first D-vertices. A0 / A port by G_D (b); (MON), B2 / B3 need only W(gate) constant.
- DATA (experiments/si/root/; note §5, §7): BF-F_D 1,195,562 checks on lib41 (S3 + 4), 36,738 on lib2o, 7,827 / 8,701 on nep90 / nep76, 0
  failures. FREEZE-A (a) 444,719 checks on lib41, 0 failures; 347 pieces past the freeze index, 0 failures of (b), (c); controls bite (freeze
  from s: 1,581; one more edge: 410). nep90 phase@4: ρ_r = 72 for r = 0, 22 cuts = 7 fallbacks + 15 D-leave A-gains, ≤ 7 root Ξ-changes per
  piece; nep76: 15 cuts, ≤ 9 per piece. A-gains on lib41 (KMIN 1, S3 + 4): 9,085 entering vertices, 8,802 by a D-leave, 283 by an Even
  switch, 0 split. D-leaves (KMIN 2): every leave without a ROUTE at u was a COPY, so case (iii) never occurred; on nep90 15 of 20 S4a leaves are by a relay whose chosen option and τ-option
  both exit at c ("two interleaving direct roots").
- OPEN: G_c (DL-SPLIT is self-referential with ROOT-PIECE: ρ ≤ (f + G_c + 1)·B and G_c ≤ B-gains + ROUTE / CYC / TOG transitions); the relays'
  own ROUTE events (their chosen exit lies in D, so (c) does not apply); f on general games.
