# Referee packet P-N5-NH-box42: OTHER-touching transitions per phase are polynomial in X, NFB-O, (E) and (K_W) (Theorem NH), the signable form of the (NH′) reductions of RESULTS R22, R24, R26 (box 42)
L-NEW successor 21 (Opus 5.5, D15/D18, L37/L40), session_01YJHHx1t8hvqkDnKzMU2Lfa. Written 2026-10-25 19:51Z-19:59Z by date -u, at the
Lead's request of 19:48Z (Lead's stamp): "P-N5-NH (docs/new/P-N5-NH-box42.md, new, frozen, self-contained). Turn three readings into
signable lemmas with full proofs". Frozen at this commit: corrections go in a fixes file, never here.
- Name. This packet is P-N5-NH-box42. It is a different object from the box-30 packet P-N5-NH (docs/new/P-N5-NH-box30.md, RESULTS
  R22), whose signed lemmas F1°, TC and P3′ it uses.
- What it replaces. Three READINGs, checked by both referees but not signed:
  - RESULTS R22 "Reduction" (P-N5-NH-box30 §4 with its fixes §5, §6): transitions per phase ≤ poly(n)·(1 + X + Σ_I (ROI(I) + WC(I))).
  - RESULTS R24 "Reduction" (P-N5-U1-box31 §6): (NH′) reduces to (X), NFB-O and the U2/U3 re-routings.
  - RESULTS R26 "Reading" (P-N5-U23-box31 §3 with fixes §6, R-1): (NH′) reduces to (X), NFB-O, (E) and (K_W).
  Theorem NH (§4) states all three as one explicit inequality and proves it. It covers every OTHER state of a phase, by clause pattern,
  with no case left to a reading.
- Labels (D18/L40): PROVED (L-NEW succ. 21, unrefereed), READING (not to sign), OPEN, DATA.
- Scope. Every statement is about the candidate N5 (SPEC S1-S5, docs/new/N5-ssi-global.md) on 𝒞^1O (exactly one Odd vertex o of
  out-degree > 1), inside one phase. Theorem NH is a REDUCTION: it bounds OTHER-touching transitions, and with RESULTS R21 Theorem X
  all transitions of a phase, by polynomials in four per-phase counts. Two of them, (E) and (K_W), are OPEN. Nothing here is a
  running-time bound for N5, a TARGET.md claim or a step-4 pass. G-N5-TIME stays OPEN.

## To sign, and what is not to sign
| § | statement | label |
| --- | --- | --- |
| §1 | Lemma SW (on a stretch, Ξ and W on R are functions of the routes; a change on R needs a switch on R) | PROVED |
| §2 | Lemma ST (OTHER status is constant on every stretch; on I it is constant unless ¬H1 ∧ ¬H2) | PROVED |
| §2 | Lemma CL (every OTHER stretch is exactly one of P3′, U1, U2, U3, U23; c_θ ≠ c_w on route-form OTHER stretches) | PROVED |
| §3 | Lemma STR-COUNT (θ- and w-changes per crossing-free interval; number of stretches) | PROVED |
| §3 | Lemma NR (Ξ-changes on R per OTHER stretch, by class) | PROVED |
| §4 | Theorem NH (a) assembled bound, (b) O ≤ 11n⁷(1 + X + f^O) + 8n³(K_W + E), (c) T ≤ 156n¹¹(1 + X + f^O) + 104n⁷(K_W + E) | PROVED |
- §5 is NOT TO SIGN: the status of the four inputs (X, NFB-O covered by packets in review or by landed results given X; (E), (K_W)
  OPEN) and the READING that follows. §6 (map to R22 / R24 / R26) is a READING. §7 is DATA.
- No hypothesis on H1, H2, H3, τ(o), c_w or θ is made anywhere; §2 splits on the four clause patterns of (H1, H2) and covers each.
  (P) (R18's one-player premise) is not used.

## 0. Objects and dependencies
### 0.1 Objects (as in RESULTS R21, R22, R24, R26)
- N5 and its SPEC: docs/new/N5-ssi-global.md. Valuations x = (c, P, ℓ) (VJ00, BRICS RS-00-48): cycle node, path set (the vertices more
  relevant than c on the play before its first visit of c), length. ⊵ is Even's order. Relevance is the injective priority order of
  SPEC S1 (Engine rank): distinct vertices are never equally relevant.
- (V1): if v is not its own cycle node in a play, val(v) = v ⊕ val(next(v)).
- Ξ_k := Ω_{σ_k}: Even's honest valuation of σ_k, against Odd's best reply σ̄_k in G_{σ_k}. W_k: the valuation of the (σ_k, τ)-play
  (Odd fixed to τ). θ := Ξ(o), w := W(o). λ_Ξ, λ_W: the cycle-node maps. c_θ := λ_Ξ(o), c_w := λ_W(o) (the cycle-node component of
  w).
- On 𝒞^1O every Odd vertex u ≠ o has one successor, so σ̄_k(u) = τ(u) for u ≠ o.
- PHASE: a maximal run of states with λ_Ξ and τ constant; it is the joint λ-phase of R21 (RESULTS R38 (a) KEY). A transition of the
  phase has both ends in it. Inside a phase every transition is an S4a step or an Even S4c fallback (τ is constant; SPEC S4c, FIX 3).
- R_k: the vertices whose (σ_k, τ)-play reaches o, with o ∈ R_k (the R22 convention); F_k := V ∖ R_k. F is closed under σ and τ,
  and o ∉ F. A CROSSING is a transition with R_{k+1} ≠ R_k. X := #crossings of the phase.
- A CROSSING-FREE INTERVAL I is a maximal run of states of the phase with R constant; on I write R, F. There are ≤ X + 1 of them.
- A STRETCH is a maximal run of states of the phase with R, θ and w constant (RESULTS R26). Every stretch lies in one interval.
- For v ∈ R, π_v is v's σ-ROUTE: the vertices of v's (σ, τ)-path before its first visit of o. π_v ⊆ R ∖ {o}, and it contains no
  Odd vertex with a choice.
- H1: the honest play from o does not return to o. H2: the W-play from o does not return to o. H3: c_θ = c_w. (h) := H1 ∧ H2 ∧ H3.
- State types (R21): EQ (Ξ = W at every vertex), THR ((h) and Ξ ≠ W), OTHER ((h) fails and Ξ ≠ W). A transition is OTHER-TOUCHING if
  one of its ends is OTHER. O := #OTHER-touching transitions of the phase.
- Route form (R22 (c)): the honest frame is in route form if H1 or c_θ = o; the W frame if H2 or c_w = o. Classes of a state:
  P3′ (both frames in route form, c_θ strictly more relevant than c_w), U1 (both in route form, c_w strictly more relevant than c_θ),
  U2 (¬H1, c_θ ≠ o, W frame in route form), U3 (¬H2, c_w ≠ o, honest frame in route form), U23 (¬H1, ¬H2, c_θ ≠ o, c_w ≠ o).
- Per-phase counts used as inputs:
  - f^O: the fallback transitions of the phase whose start state is OTHER (NFB-O counts these). f_S, f^O_I: the same inside a stretch S
    or an interval I. A fallback transition of an OTHER stretch starts at an OTHER state, so Σ_S f_S ≤ f^O.
  - K_W: the sum, over the OTHER stretches of class U2, U3 or U23, of their non-fallback transitions with a W-change at some vertex of
    R (RESULTS R26's K_W, per stretch, summed).
  - E: the sum, over the OTHER stretches of class U3 or U23, of their transitions containing an EVENT (RESULTS R26 (c): a switch of an
    Even R-vertex that changes its kind, or a switch of c_w).
- D := 4n(n − 1) + 1. n ≥ 2 throughout (o has two successors).

### 0.2 Signed results used (RESULTS line numbers on trunk 6d78b8f4)
| tag | statement used | where | status |
| --- | --- | --- | --- |
| MONO | Ξ_{k+1} ⊵ Ξ_k | R15 (a) | LANDED |
| R15d | ≤ 4n(n − 1) consecutive iterations leave both Ω_σ and Ω_τ unchanged | R15 (d) | LANDED |
| G(a) | off R, Ξ = W (no (h) needed) | R19 (a) | LANDED |
| X-1 | under H1 at the start of a transition with R constant, a θ-change changes W (= Ξ) at a vertex of F | R21 (i) (REFEREE X-1 = REFEREE-2 Lemma TF; R22 fixes §3, N-NH-1) | LANDED |
| THM-X | a phase has ≤ (3n²(1 + X + O) + X + O + 1)·D transitions | R21 (g) Theorem X | LANDED |
| F1° | on I, Ξ changes at some vertex of F at ≤ max(0, \|F\| − 1) transitions (OTHER states included) | R22 (a) | LANDED |
| TC | (i) H1 ⟺ c_θ ∈ F, H2 ⟺ τ(o) ∈ F, both constant on I; (ii) under H2, c_w = λ_Ξ(τ(o)), and I is all OTHER or has no OTHER state; (iii) under H1 ∧ ¬H2 every state of I is OTHER; (iv) under ¬H1 ∧ ¬H2, a state of I is EQ iff θ = w | R22 (b) | LANDED |
| P3′ | on a piece with c_θ strictly more relevant than c_w, ≤ (n + 1)\|R\| transitions with a Ξ-change at some vertex of R | R22 (c) | LANDED |
| U1 | a U1 piece with f fallbacks has ≤ \|R\| + f + K + (K + f + 1)(\|R\| − 2) transitions changing Ξ, W or σ on R, K ≤ (f + 1)(\|R\| − 1)(\|R\| − 2) | R24 (d) | LANDED |
| WC | under ¬H2 on I: w-changes ≤ (f^O_I + 1)(\|R\|² − 1) + f^O_I (only fallbacks at OTHER states count, N-U1-3, both §C) | R24 (e) | LANDED |
| U2C | a U2 stretch with f fallbacks and K_W non-fallback W-changes on R has ≤ f + K_W + (K_W + f + 1)(\|R\| − 2) transitions changing Ξ, W or σ on R | R26 (b) | LANDED |
| U3C | a U3 or U23 stretch with f, K_W, E has ≤ f + K_W + E + (K_W + f + E + 1)(2\|R\| − 4) R-changing transitions | R26 (d) | LANDED |
"Piece" (R22 (c)): a maximal run of an interval with both frames in route form and θ, w constant. By Lemma CL (b) below a route-form
stretch is a piece and a piece is a route-form stretch, so P3′ and U1 apply to route-form stretches.

## 1. Lemma SW (PROVED): on a stretch, Ξ and W on R are functions of the routes
Statement. Let S be a stretch and k ∈ S.
- (a) For v ∈ R, Ξ_k(v) is determined by π_v and θ, and W_k(v) is determined by π_v and w.
- (b) Hence, if a transition k → k+1 of S changes Ξ or W at some vertex of R, some Even vertex of R switches at k (σ_{k+1}(y) ≠ σ_k(y)).
Proof.
1. The honest play from v ∈ R. Along π_v every Odd vertex is forced (o ∉ π_v), and σ̄ = τ off o. So the honest play from v is π_v,
   then o, then o's honest play. Likewise the W-play from v is π_v, then o, then o's W-play.
2. Honest frame, H1. o's honest play enters F (TC (i): c_θ ∈ F) and never returns to o, so it is disjoint from π_v ⊆ R and no vertex
   of π_v is its own honest cycle node. Iterating (V1) along π_v gives Ξ(v) = π_v ⊕ θ.
3. Honest frame, ¬H1. o lies on its honest cycle C_Ξ; every vertex of C_Ξ reaches o along it, so C_Ξ ⊆ R, and its most relevant
   vertex is c_θ. So v's play ends in C_Ξ and λ_Ξ(v) = c_θ. Two cases:
   - c_θ ∈ π_v: the play prefix up to the first visit of c_θ is a prefix of π_v, so Ξ(v) is determined by π_v.
   - c_θ ∉ π_v: the prefix is π_v followed by o's honest path to c_θ. That path lies on C_Ξ, so none of its vertices before c_θ is more
     relevant than c_θ, and θ = (c_θ, ∅, d) with d its length. Hence Ξ(v) = (c_θ, A(π_v), |π_v| + d), where A(π_v) is the set of
     vertices of π_v more relevant than c_θ: a function of π_v and θ.
4. W frame: steps 2-3 with W, w, c_w, H2 and the W-cycle C_W in place of Ξ, θ, c_θ, H1 and C_Ξ (under H2 o's W-play enters F, since
   τ(o) ∈ F by TC (i); under ¬H2, C_W ⊆ R with top c_w). This proves (a).
5. (b): inside S, θ and w are constant. π_v depends only on σ restricted to the Even vertices of R (τ is constant in a phase, the Odd
   vertices of π_v are forced, and a route from R stays in R). If no Even vertex of R switches at k, every π_v (v ∈ R) is the same at
   k and k+1, and by (a) so are Ξ and W on R. □
- Use. Lemma SW makes the counts of R22 (c), R24 (d), R26 (b), (d) comparable: each of them counts at least every transition of its
  stretch with a Ξ-change on R, whether "changing Ξ, W or σ on R" or "R-changing" (a switch on R) is read. It is the step "a change of
  Ξ or W on R needs a switch on R" of the U1 and U2 proofs (P-N5-U1 §4 step 4, P-N5-U23 §1 Corollary), written once for every class.

## 2. Lemmas ST and CL (PROVED): OTHER stretches and their classes
### Lemma ST
Statement. Let I be a crossing-free interval.
- (a) If H1 ∧ H2, H1 ∧ ¬H2 or ¬H1 ∧ H2 holds on I, either every state of I is OTHER or none is.
- (b) If ¬H1 ∧ ¬H2 holds on I, a state of I is OTHER iff θ ≠ w. So OTHER status is constant on every stretch of I.
- (c) In every case OTHER status is constant on every stretch.
Proof. H1 and H2 are constant on I (TC (i)).
- H1 ∧ H2: TC (ii).
- H1 ∧ ¬H2: TC (iii), every state OTHER.
- ¬H1 ∧ H2: c_θ ∈ R (TC (i)). Under H2, o's W-play goes to τ(o) ∈ F and stays in F (F is closed under σ and τ), so c_w ∈ F. Hence
  c_θ ≠ c_w: H3 fails, (h) fails, and θ ≠ w (different cycle nodes), so Ξ ≠ W. Every state of I is OTHER.
- ¬H1 ∧ ¬H2: (h) fails at every state, so a state is OTHER iff it is not EQ, iff θ ≠ w (TC (iv)). θ and w are constant on a stretch.
- (c) follows from (a) and (b). □
### Lemma CL
Statement. Let S be an OTHER stretch.
- (a) H1, H2, c_θ, c_w and the route form of each frame are constant on S, so S has a class.
- (b) If both frames are in route form on S, then c_θ ≠ c_w; so S is a P3′ piece or a U1 piece. A route-form stretch is a piece in
  the sense of R22 (c), and conversely.
- (c) Otherwise S is a U2, U3 or U23 stretch, in the sense of R26.
Proof.
- (a) H1, H2: TC (i). c_θ = λ_Ξ(o) is constant in the phase. c_w is the cycle-node component of w, constant on S. The route form of
  each frame is a function of these.
- (b) By the clause pattern on S:
  - H1 ∧ H2: S is OTHER, so (h) fails by Lemma ST; H1 and H2 hold, so H3 fails: c_θ ≠ c_w.
  - H1 ∧ ¬H2: the W frame is in route form only if c_w = o; c_θ ∈ F (TC (i)), so c_θ ≠ o = c_w.
  - ¬H1 ∧ H2: c_θ ∈ R, c_w ∈ F (proof of Lemma ST).
  - ¬H1 ∧ ¬H2: both frames in route form means c_θ = o and c_w = o. o is then the cycle node of its own honest and W-cycles, so
    θ = (o, ∅, 0) = w, and the state is EQ (TC (iv)), not OTHER. So this case does not occur.
  Relevance is injective (SPEC S1), so c_θ ≠ c_w means one of them is strictly more relevant: class P3′ or U1.
  Piece: on S, R, θ, w are constant and both frames are in route form. A run of I strictly containing S changes θ or w, so S is
  maximal among runs with both frames in route form and θ, w constant. Conversely a piece has R, θ, w constant and is maximal with
  that property inside I, because the route form cannot change while θ and w are constant (part (a)). (This is also the fixes-file
  line P-N5-NH-fixes-box30 §4, L-NEW's one-line reading, now proved.)
- (c) Not both in route form:
  - honest not in route form (¬H1 and c_θ ≠ o), W in route form: U2;
  - W not in route form (¬H2 and c_w ≠ o), honest in route form: U3;
  - neither: ¬H1, ¬H2, c_θ ≠ o, c_w ≠ o: U23.
  These are R26's definitions, and S is a stretch in R26's sense (same definition). □

## 3. Lemmas STR-COUNT and NR (PROVED)
### Lemma STR-COUNT
Statement. Let I be a crossing-free interval, Θ_I and WC_I its transitions at which θ, respectively w, changes, and f^O_I its fallback
transitions with an OTHER start state.
- (a) Θ_I ≤ n − 1. Under H1 every θ-change of I is a transition with a Ξ-change at some vertex of F.
- (b) Under H2 every w-change of I is a transition with a Ξ-change at some vertex of F, so WC_I ≤ n − 1. Under ¬H2,
  WC_I ≤ (f^O_I + 1)(|R|² − 1) + f^O_I.
- (c) I has at most 1 + Θ_I + WC_I ≤ n − 1 + (f^O_I + 1)n² stretches.
- (d) Summed over the phase: N := Σ_I (1 + Θ_I + WC_I) ≤ n²(2X + 2 + f^O).
Proof.
- (a) H1: X-1 (R21 (i)) at each θ-change of I (H1 holds at its start, R is constant), and Ξ = W on F (G(a)); so Θ_I ≤ max(0, |F| − 1)
  by F1°. ¬H1: o lies on C_Ξ ⊆ R with top c_θ (Lemma SW step 3), so θ = (c_θ, ∅, d) with d ∈ [0, |R| − 1] the length of o's
  honest path to c_θ along C_Ξ. c_θ is fixed in the phase and the path set is ∅, so θ ⊵-compares by d alone, in the direction fixed
  by c_θ's parity. θ is ⊵-non-decreasing (MONO), so d moves strictly in one direction at each θ-change: Θ_I ≤ |R| − 1. (RESULTS R26
  READING, R-1 = N-U23-2, proved here.) In both cases Θ_I ≤ n − 1.
- (b) H2: τ(o) ∈ F (TC (i)), and o's W-play o → τ(o) → … stays in F, so o is not its own W-cycle node and (V1) gives
  w = o ⊕ W(τ(o)) = o ⊕ Ξ(τ(o)) (G(a)). A w-change is a change of Ξ(τ(o)), τ(o) ∈ F: WC_I ≤ max(0, |F| − 1) ≤ n − 1 by F1°. (This is
  R19 (b) with H2 only, N-X-2.) ¬H2: WC (R24 (e) with N-U1-3).
- (c) A new stretch of I starts only at a transition changing θ or w. With (a), (b): 1 + Θ_I + WC_I ≤ 1 + (n − 1) + max(n − 1,
  (f^O_I + 1)n² − 1) ≤ n − 1 + (f^O_I + 1)n², since (f + 1)(|R|² − 1) + f = (f + 1)|R|² − 1 and n − 1 ≤ n² − 1.
- (d) There are ≤ X + 1 intervals and Σ_I f^O_I ≤ f^O; n − 1 + (f^O_I + 1)n² ≤ (f^O_I + 2)n². □
### Lemma NR
Statement. Let S be an OTHER stretch in the interval I, f_S its fallback transitions, K_S its non-fallback transitions with a W-change on
R, E_S its transitions containing an event (K_S, E_S are counted only for the classes where they are defined: K_S for U2, U3, U23; E_S
for U3, U23; otherwise read 0). Let N_R(S) be the number of transitions of S with a Ξ-change at some vertex of R, r := |R| ≤ n. Then
- P3′: N_R(S) ≤ (n + 1)r ≤ n³;
- U1: N_R(S) ≤ r + f_S + K + (K + f_S + 1)(r − 2) with K ≤ (f_S + 1)(r − 1)(r − 2); ≤ (f_S + 1)n³;
- U2: N_R(S) ≤ f_S + K_S + (K_S + f_S + 1)(r − 2) ≤ n(K_S + f_S + 1);
- U3, U23: N_R(S) ≤ f_S + K_S + E_S + (K_S + f_S + E_S + 1)(2r − 4) ≤ 2n(K_S + f_S + E_S + 1);
- in every class: N_R(S) ≤ n³(1 + f_S) + 2n(K_S + E_S).
Proof.
- Lemma CL gives the class, and for P3′, U1 that S is a piece. Each bound is the signed one (P3′, U1, U2C, U3C), applied to S; each of
  them counts at least every transition of S with a Ξ-change on R (P3′ counts exactly these; the others count every transition that
  changes Ξ, W or σ on R, and by Lemma SW (b) a Ξ-change on R comes with a switch on R).
- Arithmetic (n ≥ 2, 1 ≤ r ≤ n):
  - P3′: (n + 1)n ≤ n³ iff n + 1 ≤ n².
  - U1: with A := K + f_S + 1, the bound is r + A − 1 + A(r − 2) = (A + 1)(r − 1). For r ≤ 2, K = 0 and (A + 1)(r − 1) ≤ f_S + 2 ≤
    (f_S + 1)n³. For r ≥ 3, A + 1 ≤ (f_S + 1)((r − 1)(r − 2) + 2), so the bound is ≤ (f_S + 1)(r − 1)((r − 1)(r − 2) + 2), which
    increases in r and at r = n equals (f_S + 1)(n³ − 4n² + 7n − 4) ≤ (f_S + 1)n³ (4n² − 7n + 4 > 0).
  - U2: with A := K_S + f_S + 1 the bound is A(r − 1) − 1 ≤ nA.
  - U3, U23: with A := K_S + f_S + E_S + 1 the bound is A(2r − 3) − 1 ≤ 2nA.
  - Last line: n³ ≥ 2n ≥ n for n ≥ 2, so each class bound is ≤ n³(1 + f_S) + 2n(K_S + E_S). □

## 4. Theorem NH (PROVED)
Statement. In one phase of N5 on 𝒞^1O, with X, f^O, K_W, E, O as in §0, N as in Lemma STR-COUNT (d) and D = 4n(n − 1) + 1:
- (a) O ≤ X + N + D·(n(X + 1) + (n³ + 1)N + n³f^O + 2n(K_W + E)), and N ≤ n²(2X + 2 + f^O);
- (b) O ≤ 11n⁷(1 + X + f^O) + 8n³(K_W + E);
- (c) the phase has T ≤ 156n¹¹(1 + X + f^O) + 104n⁷(K_W + E) transitions.
So (NH′) (O polynomial per phase, RESULTS R21 limit (ii)) follows from (X), NFB-O, (E) and (K_W), each read as "this count is
polynomial in n per phase".
Proof.
1. Split the OTHER-touching transitions k → k+1 of the phase into three kinds:
   - crossings: at most X;
   - non-crossings with θ_{k+1} ≠ θ_k or w_{k+1} ≠ w_k: both ends lie in one interval I, and the transition is in Θ_I ∪ WC_I; at most
     Σ_I (Θ_I + WC_I) ≤ N;
   - the rest: both ends lie in one stretch S, and S is OTHER (an end is OTHER, and OTHER status is constant on S, Lemma ST (c)).
2. Transitions of one OTHER stretch S. Let N_Ξ(S) be the transitions of S at which Ξ changes at some vertex. The other transitions of
   S form at most N_Ξ(S) + 1 maximal runs of consecutive transitions with Ξ unchanged everywhere; τ is constant in the phase, so Ω_τ is
   unchanged along them too, and each run has ≤ 4n(n − 1) transitions (R15d; Ξ_k = Ω_{σ_k}). So S has ≤ N_Ξ(S) + 4n(n − 1)(N_Ξ(S) + 1)
   ≤ D(N_Ξ(S) + 1) transitions.
3. N_Ξ(S) ≤ N_F(S) + N_R(S), where N_F(S) counts the transitions of S with a Ξ-change at some vertex of F.
   - Σ over the stretches of I of N_F(S) ≤ max(0, |F| − 1) ≤ n − 1 (F1°; stretches of I are disjoint runs of I). Over the phase:
     ≤ n(X + 1).
   - The number of OTHER stretches is ≤ the number of stretches ≤ N (Lemma STR-COUNT (c), (d)).
   - Σ_S N_R(S) ≤ Σ_S (n³(1 + f_S) + 2n(K_S + E_S)) ≤ n³(N + f^O) + 2n(K_W + E) (Lemma NR; Σ_S f_S ≤ f^O; Σ_S K_S = K_W and
     Σ_S E_S = E by definition).
4. Sum: O ≤ X + N + D·Σ_S (N_F(S) + N_R(S) + 1) ≤ X + N + D·(n(X + 1) + N + n³(N + f^O) + 2n(K_W + E)). This is (a), with N's bound
   from Lemma STR-COUNT (d).
5. (b). Put Q := 1 + X + f^O. Then X ≤ Q, N ≤ 2n²Q, n(X + 1) ≤ nQ, n³f^O ≤ n³Q, and D ≤ 4n². So
   O ≤ Q·(1 + 2n² + 4n²(n + 2n²(n³ + 1) + n³)) + 4n²·2n(K_W + E) = Q·(1 + 2n² + 4n³ + 8n⁴ + 4n⁵ + 8n⁷) + 8n³(K_W + E).
   For n ≥ 2, 1 + 2n² + 4n³ + 8n⁴ + 4n⁵ ≤ (1/128 + 2/32 + 4/16 + 8/8 + 4/4)n⁷ < 3n⁷, so O ≤ 11n⁷Q + 8n³(K_W + E).
6. (c). THM-X: T ≤ (3n²(1 + X + O) + X + O + 1)·D = (3n² + 1)(1 + X + O)·D ≤ 13n⁴(1 + X + O), since (3n² + 1)·4n² = 12n⁴ + 4n² ≤
   13n⁴ for n ≥ 2. And 1 + X + O ≤ Q + 11n⁷Q + 8n³(K_W + E) ≤ 12n⁷Q + 8n³(K_W + E). So T ≤ 156n¹¹Q + 104n⁷(K_W + E). □
Remarks (READING, not to sign).
- The exponents are loose; the theorem's content is that nothing but X, f^O, K_W and E is left. In particular U1 and P3′ pieces, the
  θ- and w-changes in every clause pattern, the OTHER-block boundaries (R22 fixes §5, NH-1 = N-NH-3) and the value-preserving runs are
  all bounded here.
- The theorem does not use wakes (R27's K) or J. It is a second route to a per-phase transition bound, next to R27 Corollary XJ
  (T = O(m·n⁷(1 + X) + m·n⁵·K)); R27's Reading reduces K in U2 / U3 / U23 stretches to the same (E) and (K_W).
- If f^O is replaced by f (all in-phase fallbacks), the theorem still holds (f^O ≤ f), and WC is then used in its unsharpened form.

## 5. The four inputs (NOT TO SIGN: status as of trunk 6d78b8f4)
| input | what must be polynomial per phase | status |
| --- | --- | --- |
| (X) | crossings X | IN REVIEW: P-N5-FX (docs/si/P-N5-FX-box14.md, sha1 aa227b0b…) Corollary FX (b): X ≤ n(F* + 13(d_o + 1)n³(F* + 1 + T₀) + T₀) + n − 1 = O(n⁷), F* := 1 + (n − 2)(2n − 1), T₀ := n² + 2n − 1; it rests on R30 (c) R-STICK and R34 (f) X-SN-PHASE (LANDED) and on FB-POLY (IN REVIEW) |
| NFB-O | fallbacks at OTHER states f^O | IN REVIEW: P-N5-FBPOLY (docs/new/P-N5-FBPOLY-box41.md, sha1 de244dcd…) Theorem FB-POLY: f^O ≤ f ≤ F* ≤ 2n². Also LANDED GIVEN X: R27 (h) XJ, f ≤ n_E(2n − 1)(S_o + 1) + S_o with S_o ≤ d_o(2n + (n + 1)X) |
| (E) | events in U3 / U23 OTHER stretches, E | OPEN |
| (K_W) | non-fallback W-changes on R in U2 / U3 / U23 OTHER stretches, K_W | OPEN |
- READING. If P-N5-FBPOLY and P-N5-FX are signed, Theorem NH (c) reads T = O(n¹⁸ + n⁷(K_W + E)) per phase; with P-N5-PHI (sha1
  35e79ec1…, IN REVIEW: ≤ n(n − 1) + d_o phases) N5 on 𝒞^1O would be polynomial if (E) and (K_W) hold. That is the whole open core of
  G-N5-TIME on 𝒞^1O along this route.
- DATA (§7): on the 412-file library (253 runs with one Odd choice vertex) the per-phase maxima are E 15, K_W 25, f^O 12, O 77,
  X 100. f^O > 0 in data: the box-30 CONJECTURE NFB-O "no fallback at an OTHER state" fails there; only its counting form is used here.
  None of this is evidence of a polynomial bound on E or K_W.

## 6. Map to the three readings (READING, not to sign)
| reading | its terms | here |
| --- | --- | --- |
| R22 Reduction (P-N5-NH-box30 §4, fixes §5, §6) | ROI(I) (R-only value-changing transitions in OTHER blocks), WC(I) under ¬H1 ∧ ¬H2, boundary transitions B(I) ≤ 2(1 + WC(I)) | ROI(I) ≤ Σ_S N_R(S) + Σ (θ, w)-changes (Lemma NR, STR-COUNT); boundaries are θ- or w-changes (Theorem NH step 1; at ¬H1 ∧ ¬H2 they change θ or w by Lemma ST (b); in the other patterns there are none inside I, Lemma ST (a)); WC in every pattern (STR-COUNT (b)) |
| R24 Reduction (P-N5-U1 §6) | (X), NFB-O, U2/U3 re-routings; pieces per interval | U1 and P3′ by Lemma NR; pieces = route-form stretches (Lemma CL (b)), counted by STR-COUNT (c); the re-routings are (E) and (K_W) (R26) |
| R26 Reading (P-N5-U23 §3, fixes §6) | (X), NFB-O, (E), (K_W); ¬H1 θ-count R-1 | Theorem NH (a)-(c); R-1 is STR-COUNT (a) |

## 7. DATA (experiments/new/box42/nhcheck.py; one Odd choice vertex asserted, files without one skipped)
- The script recomputes, per phase: intervals, stretches, OTHER status, the class, N_R, K_S, E_S, f_S, Θ_I, WC_I, f^O_I, and checks
  Lemma SW (b), Lemma ST (c), Lemma CL (b) (no OTHER route-form stretch with c_θ = c_w), STR-COUNT (a)-(d), Lemma NR (signed bound and
  crude bound per class), F1°, the R15d run bound per OTHER stretch, and Theorem NH (a), (b), (c).
- Commands (repo root): `python3 experiments/new/box42/nhcheck.py --list experiments/new/box41/lib41.txt` and
  `python3 experiments/new/box42/nhcheck.py --rand 3000 6 16 4202 --randstart` (python 3, no other input; Oink not used: the checks are on
  N5's own run, experiments/new/box25 and box28 engines).
- Library (412 files of lib41.txt; 253 runs with exactly one Odd choice vertex, 159 skipped): 990 phases, 101 with O > 0, ΣO = 833;
  OTHER stretches by class P3′ 131, U1 353, U2 66, U3 104, U23 51. Per-phase maxima: O 77, X 100, T 112, f^O 12, K_W 25, E 15; max N_R
  per stretch P3′ 9, U1 12, U2 25, U3 14, U23 8. Violations of every check listed above: 0.
- Random o-cyclic 𝒞^1O, n 6-16, random start pairs (seed 4202, 3,000 drawn, 2,633 runs): 7,042 phases, 20 with O > 0, ΣO = 21; max
  K_W 2, E 0, f^O 1. Violations: 0. Random runs barely reach OTHER states; the library carries the data.
- The data test the proof's steps, not tightness: every bound of Theorem NH is far from the observed counts.
