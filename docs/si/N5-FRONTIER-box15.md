# N5 beyond 𝒞^1O (box 15): which link of the P-N5-KW chain fails first with two Odd choice vertices, and a coarse freeze that survives
L-SI successor 10 (Opus 5.5; D18, L40), session_01PBqfsNWMhTPn7yNJ8C18HP. Lane note (not a packet), at the Lead's invitation of 00:51Z, item (3).
Independent of L-NEW 22's docs/new/N5-MULTI-box43.md (read-only; its notation D_k, R_D, F_D, u(v), (h_D), (h3_D), M_D, G_D (a)-(c) is used
and cited, not re-proved). Labels: PROVED (L-SI 10, unrefereed) / CONJECTURE / OPEN / READING. Not a TARGET.md claim.

## 1. The question, for the chain that closed 𝒞^1O
P-N5-KW (R50) used, in order:
- W-ONCE (every game);
- Facts A0 / A / B: one route terminal o, with Ξ = π ⊕ θ and W = π ⊕ w on R;
- FRZ-U;
- LEN;
- PAR / H-PATH / KIND-MONO / CASC-B / CW-INT (the c_w ≻ c_θ case);
- Theorem RUN.
Which link fails first on a game with ≥ 2 Odd choice vertices, and what survives?

## 2. What survives (PROVED unless marked)
- W-ONCE and W-ONCE′: every game (R50 (a)). Inside a phase, a W-changing S4a step follows a Ξ-changing step or a fallback.
- PAR_D (PROVED, every game; from R21 (a) XW, which L-NEW 22's ledger rates as true on every game, READING).
  - At a state with u ∈ D_k and λ_W(u) ≻ λ_Ξ(u), λ_W(u) is even.
  - Proof: R50's PAR at u. Ξ(u) ⊴ W(u), the cycle nodes differ, and the rewards are injective.
- Lemma CR-D (PROVED; R20 (d) CR with its hypotheses isolated). Let S be a run of consecutive S4a transitions inside one phase of N5 on ANY
  game, and L ≥ −1 a level such that at every state of S:
  - (i) COARSE_L(Ξ(v)) = COARSE_L(W(v)) for every v ∈ V;
  - (ii) the W cycle-node map v ↦ λ_W(v) is constant on S.
  Then COARSE_L(W) (= COARSE_L(Ξ)) is constant on S from its (n − 1)-th state on.
  Proof. R20 (d)'s Lemma P^c / CR (P-N5-XA §5 with the fixes of P-N5-XA-fixes-box28) uses exactly:
  - Lemma C, which is (i);
  - (Cstrict) and (Cmono), which follow from (i), WM (R23 (g), every game) and (C1);
  - "W's cycle-node map is constant on S", which is (ii);
  - (F1) in G_τ (R17);
  - its base case Ω(u) = (u, ∅, 0) at cycle nodes.
  Its fallback case is vacuous on a run of S4a steps (N-XA-1). R20's remark covers COARSE without lengths. None of these uses 𝒞^1O or a
  throttled stretch beyond (i) and (ii). □
- Corollary CR-D′ (PROVED, given L-NEW 22's G_D (c2), PROVED unrefereed). If (h_D) and (h3_D) hold at every state of S and
  L ≥ max_S M_D, then (i) and (ii) hold, so COARSE_L freezes after n − 1 transitions of S.
  - (i) is G_D (c2).
  - (ii): on F_D, λ_W = λ_Ξ (G_D (a)), constant in the phase. On R_D, λ_W(v) = λ_W(u(v)) = λ_Ξ(u(v)) by (h3_D), and that equals λ_Ξ(v) by
    G_D (b). So λ_W = λ_Ξ everywhere, constant in the phase. □
  - This is L-NEW 22's CONJECTURE "the coarse R20 machinery … holds with u* replaced by M_D" (§4.4, last line), for the CR part, with
    (h_D), (h3_D) as hypotheses. It needs neither D_k nor R_D constant.

## 3. Which link fails first: LEN (Fact A's fine part)
- FRZ-U itself survives in coarse form (CR-D′, with threshold max M_D instead of m*).
- What fails is the step after it.
  - On 𝒞^1O, every R-route ends at the same terminal o. So after the freeze, Ξ(v) and W(v) differ between routes only by the routes'
    lengths (LEN). That was the whole fine order (R19 (a) Lemma G (c): one terminal ⇒ the two frames order routes the same way).
  - With two Odd choice vertices, routes to DIFFERENT terminals u ≠ u′ ∈ D_k compare π_y ⊕ Ξ(u) with π_z ⊕ Ξ(u′), and π_y ⊕ W(u) with
    π_z ⊕ W(u′). Below max M_D these two comparisons can disagree. This is L-NEW's Δ-RT.
- So the first failing link of the KW chain is LEN (equivalently Fact A below the coarse threshold). Everything after it (KIND-MONO,
  CW-INT, E-SEG, RUN) is stated in terms of LEN's lengths and fails by inheritance (L-NEW's "FI").
- Exact obstruction (READING, a shape; no instance built): a W-flat S4a step at which an Even y switches from a route to u to a W-tied
  route to u′. It is Ξ-improving because Ξ(u′) beats Ξ(u) below M_D while W(u′) ties W(u). After the switch, y's Ξ-value has moved
  below the frozen coarse level, with no length bookkeeping.
  - On 𝒞^1O such a step is impossible (u = u′ = o).
  - On the frontier, the number of such terminal-changing switches per run is the new quantity.

## 4. What could replace LEN (CONJECTURE / OPEN)
- Terminal classes. For a fixed terminal u, the routes ending at u satisfy G_D (c1): both frames order them the same way. Inside a class,
  LEN-type monotonicity holds after the coarse freeze.
- CONJECTURE TC-SWITCH: inside one run of a phase with (h_D), (h3_D), the transitions at which some vertex changes its terminal u(v)
  number ≤ poly(n). Heuristic: a terminal change at y moves Ξ(y) strictly up (SG) at a level ≤ M_D. The pair (terminal value Ξ(u),
  route length) then acts like R26's "kind" with |D_k| kinds instead of 2. KIND-MONO used ONE bit (c_w ∈ π_v) above which everything was
  frozen. Here the analogue is the top of Ξ(u) Δ Ξ(u′), which differs per pair of terminals, so a per-vertex monotone order on terminals
  is NOT immediate. OPEN.
- What would close it: a total preorder ≼_D on D_k (fixed on the run) such that a W-flat terminal change always moves up in ≼_D. Then
  each vertex changes terminal ≤ |D_k| − 1 times per run, and the KIND-MONO / CW-INT / E-SEG pattern would go through with |D_k| kinds.
  - Candidate: order u by (Ξ(u), W(u)) lexicographically. Untested.
- DATA to collect first (not run): count terminal changes per run on L-NEW 22's frontier instances (dch16_n44, tx2_n8, retf_n6) and on
  lib41's 135 frontier games.

## 5. Status
- PROVED (L-SI 10, unrefereed): PAR_D, Lemma CR-D, Corollary CR-D′ (given L-NEW 22's G_D (a)-(c2)).
- READING: LEN is the first failing link of the KW chain.
- CONJECTURE: TC-SWITCH. OPEN: Δ-RT and the frontier.
- Nothing here bounds N5 on any class beyond 𝒞^1O ∪ 𝒞^1E.
