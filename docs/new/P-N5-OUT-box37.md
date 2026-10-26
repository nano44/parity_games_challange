# Referee packet P-N5-OUT: fallbacks at H1 ∧ ¬H2 states (SPLIT, EPOCH, F-FLAT, FREEZE-STEP, Theorem NO-ENTRY-A with its Corollary, and the case-B length-only lemma) (box 37)
L-NEW successor 17 (Opus 5.5, D15/D18, L37/L40), session_01ESR6bpU1r4ZjFsMExZtFpq. Written 2026-10-25 12:0xZ onward by date -u, at the
Lead's GO for box 38 (12:00Z, Lead's stamp). Frozen at this commit: corrections go in a fixes file, never here.
- Self-contained: definitions, statements, full proofs, the location and status of every dependency, the data, and the scripts.
- Source text: docs/new/N5-OUT-box37.md §1-§4, §9, §10 (sha1 45ef62a13426c024777e1acf719d3f998ef93c66, l-new 0b5ec987). The proofs
  are successor 16's. This successor checked them line by line against the cited statements and filled in steps the working text left
  implicit; each such step is marked "(filled in)". Where the packet and the source differ, the packet governs.
- Labels (D18/L40): PROVED (L-NEW succ. 16, unrefereed; re-checked by succ. 17), CONJECTURE, FALSE, OPEN, DATA.
- Scope: every statement is about the candidate N5, inside a phase, on 𝒞^1O. Nothing here is a running-time bound for N5, a TARGET.md
  claim or a step-4 pass. G-N5-TIME stays OPEN. θ-changes per phase are a PARAMETER here (θ_S, θ_ph); no bound on them is claimed.

## To sign, and what is not to sign
| § | statement | label | uses (P) | uses P-N5-SCOPE (in review) | uses P-N5-RL (in review) |
| --- | --- | --- | --- | --- | --- |
| §1 | Lemma SPLIT | PROVED | no | no | no |
| §2 | Corollary EPOCH (corrected form, see below) | PROVED | no | yes: FB-INT (§4 there) | no |
| §3 | Lemma F-FLAT | PROVED | no | KEY (§1 there) only, as for every item | no |
| §4 | Lemma FREEZE-STEP and Corollary TAIL | PROVED | no | KEY only | no |
| §5 | Theorem NO-ENTRY-A (τ(o) = o, case A) | PROVED | no | KEY only | no |
| §5 | Corollary NE-COUNT (case A, τ(o) = o; θ a parameter) | PROVED | no | yes: FB-INT via EPOCH | no |
| §6 | Lemma CASE-B-LEN (τ(o) = o, case B) and Remark W-SIDE | PROVED | no | KEY only | no |
- (P) (R18's one-player premise, VJ00 Lemma 5.8 "1 ⇒ 2") is used NOWHERE in this packet. Every one-player fact used is R17 (a) (F1)
  or R18 (d) Lemma S (a), both signed without (P), or R21 (c) FBL-N (i) / R23 (a) Step (K), which rest on them. So nothing is CONDITIONAL
  on (P), and L-SI's Lemma P1 (P-N5-P1, pinned, not landed) is not cited.
- P-N5-RL (docs/si/P-N5-RL-box10.md, sha1 0a3c70cb…): not used.
- §7 is NOT TO SIGN: CONJECTURES NO-ENTRY, NO-ENTRY-B and NO-ENTRY for τ(o) ≠ o; the DEAD END ROUTE-FROZEN (rfroz_cex_n16); the open
  residual core (θ-changes per HN stretch; HN stretches per phase for τ(o) ≠ o; OTHER states); a DATA observation. §8 is data.

### Superseded formulas (successor 16) and why
- N5-OUT §2 (EPOCH) and §6/§9 (its corollaries) state f_S ≤ n_E(2n − 1)(X_S + 1) and, over a τ(o) = o phase,
  "out-of-SN fallbacks ≤ (⌈T/2⌉ + 1)·n_E(2n − 1)(2(n − 1)(θ + 1) + 1)". The same formula is in the successor-16 resume point of
  notes/L-NEW.md. Both are SUPERSEDED by §2 and §5 here. The proofs had two holes:
  - (1) An evicting fallback IS a crossing (R changes at it), so it lies in no crossing-free run, and FB-INT does not count it. This is
    REFEREE-2's observation O-1 on P-N5-SCOPE §7.2 (draft docs/referee-2/R2-N5-SCOPE.md §8, referee-2 1f8a9109, relayed by the Lead
    12:00Z). Correct form: f_S ≤ n_E(2n − 1)(X_S + 1) + X_S (as in R28 (c) (iv)). DATA (§8): all 107 fallbacks with both ends in an HN
    stretch of the library are crossings; 0 are not.
  - (2) The fallback from the last state of a stretch to the next state of the phase (a drop out of H1) has only one end in the stretch,
    so f_S does not count it. It adds ≤ 1 per stretch (2 such transitions in the library).
- Neither hole changes the polynomial shape. Both change the constants.

## 0. Objects, notation and dependencies
- N5 is SPEC S1-S5 of docs/new/N5-ssi-global.md.
  - S4a is Even's arena step, S4b Odd's.
  - S4c is the fallback: if Iσ ≠ ∅, every Even v with an improving edge sets σ(v) to the w with (v, w) ∈ Iσ that maximises (Ξσ(w), w),
    ties to the larger index (τ unchanged); otherwise Odd does the same on Iτ.
  - S5 stops when Iσ = Iτ = ∅.
- Valuations x = (c, P, ℓ) and Even's order ⊴ / ◁ are VJ00's (SPEC S1). Priorities are injective; rank(u) is u's position in the
  relevance order; p′(u) := rank-based priority; reward(c) := p′(c) if Ω(c) is even, −p′(c) if Ω(c) is odd. The order compares:
  - first the cycle-node reward;
  - then P, by the injective signed weight Σ_{u∈P} ±2^rank(u) (+ for even u, − for odd u); this is lexicographic: the top vertex of
    P(x) Δ P(y) decides, in Even's favour on the side where it is even;
  - then the length: shorter is better for Even if Ω(c) is even, longer if Ω(c) is odd.
- lev(x, y), the level of first difference: +∞ if the cycle nodes differ; else rank(top of P(x) Δ P(y)) if the P differ; else −1 if
  only the lengths differ; else −∞ (x = y).
- Honest frame: Ξ_k := Ξ_{σ_k} (Even's valuation of σ_k against Odd's optimal counterstrategy σ̄_k); H_k is the (σ_k, σ̄_k)-graph;
  next_k(v) := σ_k(v) for Even v, σ̄_k(v) for Odd v; λ_k(v) := the cycle node of Ξ_k(v).
- 𝒞^1O: exactly one Odd vertex o has out-degree > 1; every other Odd vertex is forced. So τ is determined by τ(o), and H_k and the
  (σ_k, τ)-graph differ at most at o.
  - W_k := the valuation of the (σ_k, τ)-play in the one-player game G_τ; λ_W its cycle-node map.
  - θ := Ξ(o), w := W(o); c_θ := λ(o), c_w := λ_W(o).
- Sets (R19-R21 setting; P-N5-SCOPE §0): R_k := {v ≠ o : v's (σ_k, τ)-play reaches o}; R̄_k := R_k ∪ {o}; F_k := V ∖ R̄_k.
  For z ∈ R̄_k, the ROUTE π_z is the (σ_k, τ)-path from z to its first visit of o, o excluded (π_o = ∅).
- PHASE: a maximal run of consecutive states with λ_Ξ and τ constant. By Remark KEY (P-N5-SCOPE §1) it is a joint λ-phase, so results
  signed on joint λ-phases with τ constant apply. A transition of the phase has both ends in it ("in-phase"). c_θ is a phase constant.
- H1: o lies on no honest cycle. H2: o lies on no W-cycle. An HN STATE has H1 ∧ ¬H2. An HN STRETCH is a maximal run of consecutive HN
  states of one phase; its transitions are those with both ends in it.
- A CROSSING is an in-phase transition with R_{k+1} ≠ R_k. An ENTRY is a crossing with R_k ⊊ R_{k+1}; an EVICTION one with
  R̄_{k+1} ⊊ R̄_k. A crossing-free run is a maximal run of consecutive in-phase transitions none of which is a crossing.
- n_E := #Even vertices; K := n_E(2n − 1).
- Iσ_k: Even's improving (gate) edges at k: (y, z) ∈ E with Ξ_k(z) ▷ Ξ_k(σ_k y).

### Dependencies (statement used / where it lives / status)
| tag | statement used | location | status |
| --- | --- | --- | --- |
| (V1) | if λ(v) ≠ v, the value of v is v ⊕ (value of its successor on the play): add v to P if rank(v) > rank(cycle node), length + 1 | VJ00 BRICS RS-00-48 §4.2; R17 (a) | LANDED (R17) |
| R15 (a) | Ξ_k ⊴ Ξ_{k+1} pointwise at every transition, fallbacks included | RESULTS R15 (a) | LANDED |
| R15 (d) | σ_{k+1}(v) ∈ {σ_k(v)} ∪ Iσ_k(v); every iteration changes σ or τ | RESULTS R15 (d) | LANDED |
| F1 | the optimum of a one-player game dominates every strategy of that game pointwise | RESULTS R17 (a) | LANDED, no (P) |
| S (a) | Ξ_σ is the pointwise minimum of V_{σ,τ′} over Odd's strategies τ′ | RESULTS R18 (d) Lemma S (a) | LANDED, no (P) |
| G (a) | off R̄, Ξ = W | RESULTS R19 (a) Lemma G | LANDED |
| XW | Ξ_k ⊴ W_k pointwise | RESULTS R21 (a) | LANDED |
| FBL-N | at an S4c fallback with τ unchanged: (i) it is Even's and σ_k is a pointwise arena optimum in G_τ; (ii) every gate edge (x, z) with x ∈ F_k has x = λ_W(x) and λ_W(z) = x; (iii) if H2 fails, no gate edge goes from F_k to R_k | RESULTS R21 (c); proof docs/new/P-N5-X-box28.md §3 | LANDED |
| (K) | at an S4c fallback inside a phase, no arena edge (y, z) raises W at y | RESULTS R23 (a) (from FBL-N (i) and F1) | LANDED |
| ACT (i) | at a transition with τ unchanged, if R̄ gains a vertex, some switched Even s ∈ F_k with σ_{k+1}(s) ∈ R̄_k enters | RESULTS R23 (b) | LANDED |
| R-STICK | at an S4a transition of a phase, every v ∈ R_s whose W-cycle node differs from λ(v) stays in R_{s+1} | RESULTS R30 (c) | LANDED |
| H3H2 | H1 ∧ H3 ⇒ H2 (its proof: under H1, o's honest cycle avoids o and its vertices' plays avoid o) | RESULTS R30 (d) | LANDED |
| (F) | if x lies on the cycle of c's H_k-play and λ_k(c) = c, then Ξ_k(x) = (c, ∅, dist_k(x → c)) | RESULTS R34 (a) | LANDED |
| TOGGLE-COUNT | H1-toggles per phase ≤ T* := |U|(n + 1) + n − 1 ≤ n² + 2n − 1, U := λ^{-1}(c_θ) | RESULTS R34 (e) | LANDED |
| KEY | λ_U is a function of τ alone, so a (λ_Ξ, τ)-phase is a joint λ-phase | P-N5-SCOPE §1 (sha1 c3f5ed37…, pin trunk 8998ee6) | IN REVIEW: REFEREE SIGNED (docs/referee/R-N5-SCOPE.md fb6089bf); REFEREE-2 draft SIGN (referee-2 1f8a9109) |
| FB-INT | a crossing-free run of a phase has ≤ K S4c fallback transitions | P-N5-SCOPE §4 | IN REVIEW, as KEY |

- Item → dependencies:
  | item | depends on |
  | --- | --- |
  | §1 SPLIT | R-STICK, H3H2's proof, ACT (i), FBL-N (iii), KEY |
  | §2 EPOCH | SPLIT, FB-INT |
  | §3 F-FLAT | FBL-N (ii)-(iii), G (a), (F), (V1), S (a), R15 (a), KEY |
  | §4 FREEZE-STEP, TAIL | (V1), ACT (i), SPLIT, R15 (a), (d), KEY |
  | §5 NO-ENTRY-A | XW, FBL-N (iii), (K), ACT (i), (V1), R15 (a), (d), KEY |
  | §5 NE-COUNT | NO-ENTRY-A, F-FLAT, SPLIT, EPOCH (so FB-INT), TOGGLE-COUNT |
  | §6 CASE-B-LEN, W-SIDE | XW, (K), (V1), KEY |

## 1. Lemma SPLIT (PROVED, L-NEW succ. 16; 𝒞^1O)
Statement. Let k → k+1 be an in-phase transition with H1 ∧ ¬H2 at k.
- (a) If it is not a fallback, then R_k ⊆ R_{k+1}.
- (b) If it is an Even S4c fallback, then R̄_{k+1} ⊆ R̄_k.
So inside an HN stretch every crossing is an entry at an S4a step or an eviction at a fallback, and never both.
Proof.
- (filled in) The transition kinds. τ is constant in a phase, so an in-phase non-fallback transition is an S4a step, and an in-phase
  fallback is Even's (an Odd fallback changes τ and leaves the phase).
- (a) Let v ∈ R_k.
  - v's (σ_k, τ)-play reaches o and then follows o's W-play. Under ¬H2, o lies on its W-cycle C_W. Every vertex of C_W reaches o, so
    C_W ⊆ R̄_k, and v's W-cycle node is the top c_w of C_W, a vertex of R̄_k.
  - v's honest play agrees with its (σ_k, τ)-play up to o (on 𝒞^1O the two graphs differ only at o), and then follows o's honest play.
    Under H1 that play never returns to o, so λ(v) = λ(o) = c_θ.
  - Under H1, c_θ ∈ F_k (H3H2's proof, R30 (d): o's honest cycle avoids o, and so do its vertices' plays, which are the same in both
    graphs because they avoid o).
  - So v's W-cycle node c_w ∈ R̄_k differs from λ(v) = c_θ ∈ F_k, and R-STICK (R30 (c)) keeps v in R_{k+1}.
- (b) Suppose R̄ gains a vertex. By ACT (i) (R23 (b)), some switched Even s ∈ F_k has σ_{k+1}(s) ∈ R̄_k. S4c switches only gate edges,
  so (s, σ_{k+1}(s)) is a gate edge from F_k into R̄_k. FBL-N (iii) (R21 (c)) excludes a gate edge from F_k to R_k under ¬H2.
  - (filled in) The target o is excluded too. FBL-N (iii)'s proof: a gate edge (x, z) with x ∈ F_k has x = λ_W(z) (FBL-N (ii)). If
    z = o, then λ_W(o) ∈ C_W ⊆ R̄_k under ¬H2, so x ∈ R̄_k, a contradiction.
  So there is no such edge, a contradiction. □

## 2. Corollary EPOCH (PROVED, L-NEW succ. 16; corrected form by succ. 17; 𝒞^1O)
Statement. Let S be an HN stretch. A BREAK is an entry of S that is preceded in S by an eviction with no entry in between. Let B be the
number of breaks of S, X_S its number of crossings, and f_S its number of fallback transitions (transitions with both ends in S).
Then:
- X_S ≤ 2(n − 1)(B + 1);
- f_S ≤ K(X_S + 1) + X_S, where K = n_E(2n − 1).
Proof.
- Cut S just before each break. This gives B + 1 segments. Inside a segment no entry follows an eviction (such an entry would be a break,
  and breaks only start segments), so every entry precedes every eviction.
- Crossings of one segment.
  - Before its first eviction, R never shrinks: S4a steps do not shrink R (SPLIT (a)), and a fallback that changes R is an eviction
    (SPLIT (b)). Every entry makes R strictly larger, and R ⊆ V ∖ {o}, so there are ≤ n − 1 entries.
  - From its first eviction on there are no entries, and every eviction makes R̄ strictly smaller: ≤ n − 1 evictions.
  - So a segment has ≤ 2(n − 1) crossings, and X_S ≤ 2(n − 1)(B + 1).
- Fallbacks. A fallback of S is either a crossing (≤ X_S of them) or lies in a crossing-free run of S. The crossings cut S into
  ≤ X_S + 1 crossing-free runs. Each lies in one crossing-free run of the phase, and distinct ones in distinct runs of the phase (a
  crossing separates them). FB-INT (P-N5-SCOPE §4) gives ≤ K fallbacks in each. So f_S ≤ K(X_S + 1) + X_S. □
- (filled in) The successor-16 text had f_S ≤ K(X_S + 1), counting only the second kind. See "Superseded formulas" above.

## 3. Lemma F-FLAT (PROVED, L-NEW succ. 16; 𝒞^1O)
Statement. Let k → k+1 be an in-phase Even S4c fallback with H1 ∧ ¬H2 at k. Then Ξ_{k+1}(v) = Ξ_k(v) for every v ∈ F_k, and
θ_{k+1} = θ_k. Hence inside an HN stretch θ changes only at S4a steps.
Proof.
- Step 1: the switched vertices in F_k. Let x ∈ F_k be switched to z.
  - By FBL-N (ii), x = λ_W(x) and λ_W(z) = x. By FBL-N (iii) and §1 (b)'s filled-in step, z ∉ R̄_k, so z ∈ F_k.
  - On F_k, plays avoid o, so honest and (σ_k, τ)-plays coincide and W = Ξ (G (a), R19 (a)). Hence λ_k(x) = x and λ_k(z) = x.
  - By (F) (R34 (a)), Ξ_k(σ_k x) = (x, ∅, L_x − 1), where L_x is the length of x's cycle.
  - Let q be z's path to its first visit of x. No switched vertex lies on q before x: a switched x′ ∈ F_k is its own cycle node (as
    for x), so a play through x′ ends on x′'s cycle, and λ_k(z) = x would force x′ = x. Odd vertices on q are forced (q avoids o).
  - So at k+1, x's honest play is the cycle x → z → q → x, the same for every Odd strategy.
  - If some vertex of q were more relevant than x, the top of that cycle would be that vertex, and λ_{k+1}(x) ≠ x: the transition would
    leave the phase. So P(Ξ_k z) = ∅: the gate (x, z) has level −1.
- Step 2: v ∈ F_k.
  - Let c := λ_k(v), and let p be v's honest path to its first visit of c. p lies in F_k.
  - A switched vertex on p before c is its own cycle node (Step 1), so it would be v's cycle node c. So p has no switched vertex before c.
  - If c is not switched, its old cycle is intact (a switched x on it, x ≠ c, would have λ_k(x) = c ≠ x). If c is switched, the
    continuation is the cycle c → z_c → q → c of Step 1, topped by c, with P = ∅.
  - (filled in) Either way, under (σ_{k+1}, σ̄_k) the play from v has prefix p and cycle node c, and the path set above c is that of p:
    the switched cycle adds no vertex above c (Step 1), and the old cycle adds none either. The lengths agree: in the unswitched case
    the cycle is the same; in the switched case the value of v is p ⊕ (c, ∅, 0) in both, by (V1) along p. So
    V_{σ_{k+1}, σ̄_k}(v) = Ξ_k(v).
  - Lemma S (a) (R18 (d)) gives Ξ_{k+1}(v) ⊴ V_{σ_{k+1}, σ̄_k}(v) = Ξ_k(v). R15 (a) gives ⊵. So the two are equal.
- Step 3: θ.
  - Under H1, x0 := σ̄_k(o) has an honest play that never visits o, so x0 ∈ F_k.
  - Under (σ_{k+1}, σ̄_k), o's play is o → x0 followed by x0's play from Step 2, which never returns to o. So o is not a cycle node, and
    by (V1), V_{σ_{k+1}, σ̄_k}(o) = o ⊕ Ξ_k(x0) = θ_k.
  - Lemma S (a) and R15 (a) give θ_{k+1} = θ_k. □

## 4. Lemma FREEZE-STEP (PROVED, L-NEW succ. 16; 𝒞^1O) and Corollary TAIL
Statement. Let t → t+1 be an in-phase transition with H1 ∧ ¬H2 at t, H1 at t+1 and θ_{t+1} = θ_t. Suppose no gate (y, z) ∈ Iσ_t has
z ∈ R̄_t. Then:
- (i) R̄_{t+1} ⊆ R̄_t, and the route of every z ∈ R̄_{t+1} is the same at t and t+1;
- (ii) Ξ_{t+1}(z) = Ξ_t(z) for every z ∈ R̄_{t+1};
- (iii) no gate (y, z) ∈ Iσ_{t+1} has z ∈ R̄_{t+1}.
Proof.
- Route form under H1. For z ∈ R̄_k at an H1 state, z's honest play is π_z followed by o's honest play, which never returns to o. No
  vertex of π_z is the cycle node of its own play. So by (V1) along π_z, Ξ_k(z) = π_z ⊕ θ_k (⊕ iterated along π_z).
- (i), S4a case.
  - Every gate target lies in F_t (hypothesis). An entry needs a switched s ∈ F_t with σ_{t+1}(s) ∈ R̄_t (ACT (i)). By R15 (d) that
    target is σ_t(s) ∈ F_t or a gate target, also in F_t. So there is none, and R̄_{t+1} ⊆ R̄_t. With SPLIT (a), R_{t+1} = R_t.
  - A switched v ∈ R_t would have σ_{t+1}(v) a gate target, in F_t = F_{t+1}; then v ∉ R_{t+1} = R_t, a contradiction. So no vertex
    of R_t switches, and routes are unchanged.
- (i), fallback case. SPLIT (b) gives R̄_{t+1} ⊆ R̄_t. A switched vertex on the route at t+1 of some z ∈ R̄_{t+1} has its new successor
  among the gate targets, in F_t ⊆ F_{t+1}; but the next vertex of the route is in R̄_{t+1}. A contradiction, so routes are unchanged.
- (ii) The route form at t and at t+1 (H1 at both), with the same route and θ_{t+1} = θ_t.
- (iii) Suppose (y, z) ∈ Iσ_{t+1} with z ∈ R̄_{t+1}.
  - Then Ξ_t(z) = Ξ_{t+1}(z) ▷ Ξ_{t+1}(σ_{t+1} y) ⊵ Ξ_t(σ_{t+1} y) ⊵ Ξ_t(σ_t y), by (ii), R15 (a), and
    σ_{t+1}(y) ∈ {σ_t(y)} ∪ Iσ_t(y) (R15 (d)).
  - If z = σ_t(y), this reads Ξ_t(z) ▷ Ξ_t(z), impossible. Otherwise (y, z) ∈ Iσ_t with z ∈ R̄_t, against the hypothesis. □
- Corollary TAIL. If a state t of an HN stretch has no gate into R̄_t, then on the rest of the stretch up to the first θ-change nothing
  enters R, R̄ only shrinks (≤ n − 1 crossings), and Ξ is frozen on R̄. Proof: induction with FREEZE-STEP (an H1-toggle ends the
  stretch, and so does an H2-change). □
- Where the hypothesis holds: at a fallback state there is no gate from F into R̄ (FBL-N (iii)). Gates from R into R̄ can exist there;
  the fallback switches them, R-values rise, and new gates can follow. That is the dead end ROUTE-FROZEN (§7).

## 5. Theorem NO-ENTRY-A (PROVED, L-NEW succ. 16; 𝒞^1O, τ(o) = o, case A) and Corollary NE-COUNT
Setting.
- A phase with τ(o) = o. So w = (o, ∅, 0); o's W-play is the self-loop, so ¬H2 holds at every state, the HN states are exactly the H1
  states, and W(r) = π_r ⊕ w for r ∈ R̄.
- If the phase has an H1 state, c_θ ≠ o. XW gives θ ⊴ w, and the cycle nodes differ, so reward(c_θ) < reward(o).
- CASE A: rank(o) > rank(c_θ). Then Ω(o) is even: an odd o more relevant than c_θ would have reward(o) = −p′(o) < reward(c_θ).
  CASE B: rank(c_θ) > rank(o). Then Ω(c_θ) is odd: an even c_θ would have reward(c_θ) = p′(c_θ) > p′(o) ≥ reward(o).
- Write x ≡ y when lev(x, y) < rank(o): the same cycle node, and P(x), P(y) agree on vertices of rank ≥ rank(o).
- (filled in) Three facts about the order (from the lexicographic form in §0):
  - (T1) If lev(x, y) ≥ rank(o), x′ ≡ x and y′ ≡ y, then lev(x′, y′) = lev(x, y), and x′ ◁ y′ iff x ◁ y. (The cycle nodes and the parts
    of P at ranks ≥ rank(o) are the same, so the same top vertex, on the same side, decides.)
  - (T2) ≡-classes are intervals of ⊴: if x ⊴ y ⊴ x′ and x ≡ x′, then y ≡ x. (Otherwise lev(x, y) ≥ rank(o) and x ◁ y, so x′ ◁ y by
    (T1), against y ⊴ x′.)
  - (T3) For every vertex z, z ⊕ · respects ≡: z ⊕ (c, P, ℓ) = (c, P ∪ ({z} if rank(z) > rank(c)), ℓ + 1).
Separation fact SEP-o (case A). At an H1 state t:
- every z ∈ R̄_t has o ∈ P(Ξ_t z): Ξ_t(z) = π_z ⊕ θ_t (route form, §4), and o ∈ P(θ_t) because θ_t = o ⊕ Ξ_t(σ̄_t o) with o not a
  cycle node (H1) and rank(o) > rank(c_θ);
- every f ∈ F_t has o ∉ P(Ξ_t f), because its honest play avoids o.
So lev(Ξ_t z, Ξ_t f) ≥ rank(o) for such z and f; in particular Ξ_t(z) ≢ Ξ_t(f).
Invariant INV(t):
- (i) no gate (y, z) ∈ Iσ_t with y ∈ F_t and z ∈ R̄_t;
- (ii) every gate (v, z) ∈ Iσ_t with v ∈ R_t and z ∈ R̄_t has lev(Ξ_t(σ_t v), Ξ_t(z)) < rank(o).
Statement. Let S be an HN stretch of a τ(o) = o phase in case A, let a ∈ S be a state at which an Even fallback a → a+1 is taken, and
let θ be constant on a run of states [a, b] ⊆ S. Then INV(t) holds for every t ∈ [a, b]; no transition of [a, b] is an entry; R̄ only
shrinks on [a, b]; and Ξ_t(z) ≡ Ξ_a(z) for t ∈ [a, b] and z ∈ R̄_t.
Proof.
- BASE: INV(a).
  - (i) is FBL-N (iii) with §1 (b)'s filled-in step (target o).
  - (ii). Let (v, z) be an R → R̄ gate at a, and suppose ℓ := lev(Ξ_a(σ_a v), Ξ_a(z)) ≥ rank(o).
    - σ_a(v) ∈ R̄_a since v ∈ R_a. Both values are π ⊕ θ_a with cycle node c_θ. Routes lie in R, and θ's path set lies in {o} ∪ F, so
      P(Ξ_a z) Δ P(Ξ_a σ_a v) = (π_z Δ π_{σ_a v}) ∩ V_{>c_θ}. Its top u has rank ℓ, and u ≠ o since o is in neither route; so
      rank(u) > rank(o).
    - (filled in) The W-values W_a(z) = π_z ⊕ w and W_a(σ_a v) = π_{σ_a v} ⊕ w have cycle node o and path sets π ∩ V_{>o}. Their
      symmetric difference is (π_z Δ π_{σ_a v}) ∩ V_{>o}. It contains u, and an element of rank > rank(u) would lie above c_θ and in
      the honest difference. So its top is the same u, on the same side, and W_a(z) ▷ W_a(σ_a v), with the same verdict as Ξ.
    - Case 1: z's route avoids v. After the switch v → z, z's play is unchanged and v is not a cycle node, so W at v becomes
      v ⊕ W_a(z) ▷ v ⊕ W_a(σ_a v) = W_a(v) (v is in neither route, so v ⊕ adds the same vertex to both). The switch raises W at v.
    - Case 2: z's route passes v: π_z = q · v · π_{σ_a v}. Then the honest difference is (q ∪ {v}) ∩ V_{>c_θ}, all on z's side, so u is on
      z's side and Ω(u) is even (the gate is Even-improving). (filled in: the side is needed only here.) The switched play from v closes
      the cycle v → z → q → v, whose top is u (every vertex of q ∪ {v} above u would be above c_θ and in the difference). Its cycle node
      u has reward(u) = p′(u) > p′(o) = reward(o), and W_a(v) has cycle node o. So W at v rises.
    - Either way an arena edge (a gate is in the arena) raises W at v at the fallback a, against Step (K) (R23 (a)).
- STEP: INV(t) ⇒ INV(t+1) for t, t+1 ∈ [a, b].
  - Switched edges are gate edges (R15 (d)). By (i) none goes F_t → R̄_t, so ACT (i) gives no entry: R̄_{t+1} ⊆ R̄_t.
  - Value claim: Ξ_{t+1}(z) ≡ Ξ_t(z) for z ∈ R̄_{t+1}. Induction on z's route length d at t+1.
    - d = 0: z = o, Ξ_{t+1}(o) = θ = Ξ_t(o).
    - d ≥ 1: z′ := next_{t+1}(z) ∈ R̄_{t+1}, and Ξ_{t+1}(z) = z ⊕ Ξ_{t+1}(z′) by (V1) (H1 at t+1: z is not a cycle node).
      - z forced or not switched: next_t(z) = z′.
      - z switched: z ∈ R_{t+1} ⊆ R_t and z′ ∈ R̄_t, so (z, z′) was an R → R̄ gate at t, and Ξ_t(z′) ≡ Ξ_t(σ_t z) by (ii).
      In both cases (T3) and the induction hypothesis give Ξ_{t+1}(z) ≡ z ⊕ Ξ_t(next_t z) = Ξ_t(z) ((V1) at t).
  - (i) at t+1. Let y ∈ F_{t+1} be Even, z ∈ R̄_{t+1}, and suppose Ξ_{t+1}(z) ▷ Ξ_{t+1}(σ_{t+1} y).
    - σ_{t+1}(y) ∈ F_{t+1}, so SEP-o at t+1 gives lev ≥ rank(o), and (T1) with Ξ_t(z) ≡ Ξ_{t+1}(z) gives Ξ_t(z) ▷ Ξ_{t+1}(σ_{t+1} y).
    - Ξ_{t+1}(σ_{t+1} y) ⊵ Ξ_t(σ_{t+1} y) ⊵ Ξ_t(σ_t y) (R15 (a), (d)). So Ξ_t(z) ▷ Ξ_t(σ_t y). z = σ_t(y) is impossible, so
      (y, z) ∈ Iσ_t, and z ∈ R̄_t.
    - y ∈ F_t contradicts (i) at t.
    - y ∈ R_t (evicted at t → t+1): (y, z) is an R → R̄ gate at t, so Ξ_t(z) ≡ Ξ_t(σ_t y) by (ii). Then
      Ξ_t(σ_t y) ⊴ Ξ_{t+1}(σ_{t+1} y) ◁ Ξ_t(z), and (T2) gives Ξ_{t+1}(σ_{t+1} y) ≡ Ξ_t(z). But o ∉ P(Ξ_{t+1}(σ_{t+1} y)) (it is
      an F_{t+1}-value) and o ∈ P(Ξ_t z) (SEP-o at t): a contradiction.
  - (ii) at t+1. Let (v, z) be an R → R̄ gate at t+1 with lev ≥ rank(o).
    - v ∈ R_{t+1} ⊆ R_t, σ_{t+1}(v) ∈ R̄_{t+1}. By the value claim and, if v switched, (ii) at t:
      Ξ_{t+1}(σ_{t+1} v) ≡ Ξ_t(σ_{t+1} v) ≡ Ξ_t(σ_t v). Also Ξ_{t+1}(z) ≡ Ξ_t(z).
    - By (T1), Ξ_t(z) ▷ Ξ_t(σ_t v) at the same level ≥ rank(o). So z ≠ σ_t(v), and (v, z) is an R → R̄ gate at t with lev ≥ rank(o),
      against (ii) at t. □
- Corollary NE-COUNT (case A, τ(o) = o; θ a parameter).
  - (a) Every break of an HN stretch S of the phase has a θ-change at an S4a transition strictly after its eviction and no later than
    its entry. Breaks are separated by disjoint intervals, so B ≤ θ_S := #θ-changes at transitions of S.
  - (b) X_S ≤ 2(n − 1)(θ_S + 1) and f_S ≤ K(X_S + 1) + X_S.
  - (c) Over the phase: let N_HN be its number of HN stretches, θ_ph its number of θ-changes, T_ph its number of H1-toggles, and f_HN
    its number of in-phase fallback transitions k → k+1 with H1 ∧ ¬H2 at k (here: all its out-of-SN fallbacks). Then
    N_HN ≤ ⌊T_ph/2⌋ + 1 ≤ ⌊T*/2⌋ + 1, and
    f_HN ≤ (K + 1)·(2(n − 1)·θ_ph + (2n − 1)·N_HN),  X_HN ≤ 2(n − 1)(θ_ph + N_HN),
    where X_HN counts the crossings with both ends in HN stretches. θ_ph is OPEN (§7).
  Proof.
  - (a) Let the break's entry be k → k+1, and a → a+1 the first eviction after the previous entry of S (or after S's start). It is a
    fallback (SPLIT). If θ were constant on [a, k+1], NO-ENTRY-A with b := k+1 would exclude the entry. So θ_j ≠ θ_{j+1} for some
    a ≤ j ≤ k, and j ≠ a by F-FLAT. By F-FLAT, j → j+1 is an S4a step. The next break's eviction comes after this entry, so the intervals
    (a, k] of distinct breaks are disjoint.
  - (b) EPOCH with (a).
  - (c) In a τ(o) = o phase the HN stretches are the maximal H1-runs. With T_ph toggles there are T_ph + 1 maximal H1-constant runs,
    alternating, so ≤ ⌊T_ph/2⌋ + 1 H1-runs; T_ph ≤ T* by TOGGLE-COUNT. An in-phase fallback from an HN state either has both ends in
    one stretch (counted in f_S) or is the last transition out of a stretch (≤ 1 per stretch). The θ_S are counted on disjoint sets of
    transitions, so Σ_S θ_S ≤ θ_ph. Hence f_HN ≤ Σ_S ((K + 1)X_S + K + 1) ≤ (K + 1) Σ_S (2(n − 1)(θ_S + 1) + 1), which is the bound;
    X_HN is the sum of (b)'s first bound. □
- What the theorem does not cover: case B (§6, §7) and τ(o) ≠ o (§7).

## 6. Lemma CASE-B-LEN (PROVED, L-NEW succ. 16; 𝒞^1O, τ(o) = o, case B) and Remark W-SIDE
Statement. In a τ(o) = o phase in case B (rank(c_θ) > rank(o), so Ω(c_θ) odd), let a be an HN state at which an Even fallback is taken.
Then every R → R̄ gate (v, z) at a is honest length-only: lev(Ξ_a(σ_a v), Ξ_a(z)) = −1, and z's route is longer than σ_a(v)'s.
Proof.
- Both values are π ⊕ θ_a with cycle node c_θ, and their P-difference is (π_z Δ π_{σ_a v}) ∩ V_{>c_θ} (the θ part is common).
- Suppose it is non-empty, with top u. Then rank(u) > rank(c_θ) > rank(o). The W-values have cycle node o and path sets π ∩ V_{>o}; any
  element of their difference above u would be above c_θ and in the honest difference, so the W-difference has the same top u on the same
  side. The two cases of §5 BASE then apply verbatim (Case 2: the difference q ∪ {v} lies on z's side, so Ω(u) is even, and the new
  cycle's node u has reward p′(u) > p′(o) ≥ reward(o)). So the switch raises W at v, against Step (K). Hence the P are equal and
  lev = −1.
- The gate is decided by length. c_θ is odd, so the longer value is better for Even: |π_z| + |θ_a| > |π_{σ_a v}| + |θ_a|. □
- Remark W-SIDE (PROVED, same setting; Case 1 of §5, z's route avoids v). Step (K) forbids v ⊕ W_a(z) ▷ W_a(v). The W-difference is
  (π_z Δ π_{σ_a v}) ∩ V_{>o}, all of rank in (rank(o), rank(c_θ)). So either its top is W-unfavourable to z, or it is empty and Ω(o) is
  even (the shorter W route is better; z's is longer). Both parities of o occur in case B: with c_θ odd, an odd o can still have
  reward(o) = −p′(o) > −p′(c_θ). In Case 2 (π_z = q · v · π_{σ_a v}, q ∪ {v} below c_θ), Step (K) forbids the closed cycle's node t := top
  of q ∪ {v} from having reward(t) > reward(o).
- Consequence (how a case-B entry would have to look; READING): after a case-B fallback, R-values rise only by length (at the fallback
  itself). A post-fallback entry from y ∈ F needs an edge y → z ∈ R̄ with P(Ξ(σ y)) = P(Ξ z) = (π_z ∩ V_{>c_θ}) ∪ P(θ) and an honest
  length of σ(y) strictly between z's lengths before and after the rise. SEP-o is not available: o is below c_θ, so o ∉ P(θ).

## 7. NOT TO SIGN
- CONJECTURE NO-ENTRY (DATA). Inside an HN stretch, after a fallback, no vertex enters R while θ is constant.
  - Case A with τ(o) = o is Theorem NO-ENTRY-A.
  - CONJECTURE NO-ENTRY-B: the case-B statement of §5 (τ(o) = o). Exact shape of a violation: §6 Consequence.
  - CONJECTURE NO-ENTRY for τ(o) ≠ o. Obstacle: the W threshold is c_w, which need not lie on θ's path, so SEP-o has no analogue yet.
  - DATA (successor 16, N5-OUT §6, §8, §9, §10): library 0 entries in 282 transitions after a fallback with θ constant (52 entries in
    205 S4a steps before the first fallback); inva.py 288 case-A and 33 case-B post-fallback states, 0 failures of (i), (ii) or the frozen
    values (so (ii) also held in case B); 11 / 11 library breaks θ-separated; climbs sepclimb / rfclimb MODE=ent / ent2 (seeds 3711-3714,
    3731-3733, 3741-3743): 0 violations; the case-B precondition (a length-only R → R̄ gate at a fallback) was never reached by a climb.
- DEAD END ROUTE-FROZEN (FALSE). Claim: "after a fallback with θ constant, Ξ on R is frozen inside an HN stretch".
  - Instance experiments/new/box37/instances/rfroz_cex_n16.pg, sha1 a9b40395ba9a351037f8dff612d50848540ddbc1; n 16, o = 11,
    succ(o) = {11, 12, 15}, τ(o) = o. Lead re-run OK 11:14Z. Re-run by successor 17 (12:0xZ): n5.py n5 15 iterations / 5 fallbacks;
    check_sol2.py "zielonka(oink zlk) OK strategies verified"; one Odd choice vertex asserted.
  - Phase states 4-13 are H1 ∧ ¬H2, θ = (6, 36880, 3) constant. The fallback at 4 → 5 evicts 10; R-values then rise at the S4a steps
    5 → 6 (σ(9): 13 → 7), 6 → 7 (σ(2): 1 → 9), 7 → 8 (σ(13): 0 → 2) and at later fallbacks: 8 transitions with an R-rise, 0 entries.
  - Exact obstruction: S4a takes R → R̄ gates that are W-improving, and fallbacks take any R → R̄ gate, so routes inside R keep improving
    after a fallback, and FREEZE-STEP's hypothesis (no gate into R̄) fails at the next state. It is case A: the rises are at levels 8-11,
    below rank(o) = 12, as INV (ii) requires.
- OPEN, the residual core.
  - (1) θ-changes per HN stretch (θ_S, θ_ph above). All are at S4a steps (F-FLAT). F1° (R22 (a)) bounds them by n − 2 per
    crossing-free interval, which is circular in X. A bound independent of X is the poly form of PF-THETA (CONJECTURE; its linear form is
    FALSE, L-RED pftheta_cex_n32) moved to HN stretches.
  - (2) For τ(o) ≠ o, HN stretches per phase. They start after toggles or after (h)-ends, and (h)-runs ≤ 1 + T + f (R34 (g)) is circular
    in f.
  - (3) OTHER states (H1 ∧ H2 ∧ ¬H3): 2 fallbacks in the library; untouched.
- DATA observation (successor 17, §8): every fallback with both ends in an HN stretch of the library is a crossing (107 / 107). So the
  "K per crossing-free run" term of EPOCH was never used in data, and the "+ X_S" term carries all of it. No claim.

## 8. Data and scripts (DATA, not proof)
- Every script asserts exactly one Odd vertex of out-degree > 1, and skips and counts non-𝒞^1O files of a list.
- Library: experiments/new/box37/lib37.txt (429 paths, 270 in 𝒞^1O) and rfroz_cex_n16.pg.
- Successor 16 (experiments/new/box37; logs in data/): epoch.py (SPLIT, breaks; 113 library HN stretches + 1,331 random, seed 3702,
  0 failures of SPLIT), hnstat (F-FLAT: 100 library θ-changes in HN stretches, 0 at fallbacks), rfrozen.py (ROUTE-FROZEN / NO-ENTRY
  classes), inva.py (INV (i), (ii), frozen values; data/inva_lib.txt), gadget.py (case-B one-vertex attack: b5_o11, b5_os_n12, b5_os_n14,
  wdrop_canon, 0 violations), sepclimb.py / rfclimb.py (climbs; logs in experiments/new/out/box37, gitignored).
- Successor 17: experiments/new/box38/fbsplit.py (per HN stretch: crossings, evictions, entries, crossing / non-crossing / exit
  fallbacks, max fallbacks per crossing-free run, breaks and θ-separation; checks SPLIT, EPOCH's corrected bounds, (a) of NE-COUNT on
  case-A τ(o) = o stretches, N_HN ≤ ⌊T_ph/2⌋ + 1, and (c)'s f_HN bound on case-A τ(o) = o phases).
  - data/fbsplit_lib.txt (library + rfroz_cex_n16, 8 s): 115 HN stretches; fallbacks with both ends in a stretch: 107 crossings,
    0 non-crossing; 2 exit fallbacks; max fallbacks per crossing-free run of a stretch 0; breaks 8 (case A, τ(o) = o) + 3 (case B),
    all θ-separated; 25 case-A and 12 case-B τ(o) = o phases; max f_S 12 (wd16_s2, n 16, X_S 12, all 12 crossings); max X_S 31
    (post31_n48, 11 θ-changes, 0 breaks); max f_HN per phase 12 (case A, wd16_s2, θ_ph 0) and 6 (case B, b5_os_n14). 0 failures.
  - data/fbsplit_rand.txt (20,000 random 𝒞^1O games, n 4-14, seed 3801): 872 HN stretches, no fallback in any, max X_S 1; 0 failures.
  - wd16_s2 re-run by successor 17: n5.py n5 19 iterations / 14 fallbacks; check_sol2.py "zielonka(oink zlk) OK strategies verified".
- Reproduce: `python3 experiments/new/box38/fbsplit.py $(cat experiments/new/box37/lib37.txt) experiments/new/box37/instances/rfroz_cex_n16.pg`
  and `python3 experiments/new/box38/fbsplit.py --rand 20000 4 14 3801` (Oink built by scripts/setup_oink.sh is needed only for
  check_sol2.py).
