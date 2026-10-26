# Referee packet P-N5-FBPOLY: in a phase of N5 on 𝒞^1O, the in-phase Even S4c fallbacks number at most 1 + (|U| − 2)(deg_U(o) + |U|), with no hypothesis on H1, H2, H3, τ(o), c_w, θ or N_HN (κ-FB-ROUND, κ-HAT-FREEZE, κ-PFZ, κ-Y-FORM, EXIT-SWITCH, FREEZE-EXIT, CN-ONLY, THETA-AFTER, Theorem FB-POLY) (box 41)
L-NEW successor 20 (Opus 5.5, D15/D18, L37/L40), session_018pjn8Y8JRES3YuFDUCAJgM. Written 2026-10-25 18:4xZ-18:5xZ by date -u, at the
Lead's request of 18:37Z (Lead's stamp): "Freeze docs/new/P-N5-FBPOLY-box41.md as a new, self-contained packet."
Frozen at this commit: corrections go in a fixes file, never here.
- Source: docs/new/N5-FBPOLY-box41.md (working doc, l-new d65e43af, sha1 7a7087f7…). This packet restates and proves everything it
  asks to be signed. Where the packet and the source differ, the packet governs. Differences (none changes a statement): (i) the facts
  of P-N5-PFZ §1 and P-N5-RHO §0-§2 used here are restated in κ form WITH proofs (§0, §1); (ii) Y-FORM (b) and the length range of θ at
  ¬H1 states are proved here (§0 (YB)); (iii) FB-POLY (c) is stated in the graph G_U of P-N5-PFZ §0.
- Labels (D18/L40): PROVED (L-NEW succ. 20, unrefereed), OPEN, CONJECTURE, DATA.
- Scope. Every statement is about the candidate N5 (SPEC S1-S5, docs/new/N5-ssi-global.md) on 𝒞^1O (exactly one Odd vertex o of
  out-degree > 1), inside one phase. Nothing here is a running-time bound for N5, a TARGET.md claim or a step-4 pass. G-N5-TIME stays
  OPEN: crossings outside SN prefixes and OUT stretches, OTHER-touching transitions, θ-changes before the freeze, S4a steps and the
  number of phases are not bounded here.

## To sign, and what is not to sign
| § | statement | label |
| --- | --- | --- |
| §1 | Lemma κ-FB-ROUND (one fallback is one Bellman-Ford round for κ on U) | PROVED |
| §1 | Lemma κ-HAT-FREEZE (a)-(c) (κ frozen on F ∩ U after |U| − 2 fallbacks of a phase) | PROVED |
| §1 | Lemma κ-PFZ (paths to o: lower bound after j fallbacks of a θ-run) | PROVED |
| §1 | Lemma κ-Y-FORM (κ(o) = κwt(o) + min over Y at H1 states) | PROVED |
| §2 | Lemma EXIT-SWITCH (some switched vertex of U ∖ T has a target whose play meets a terminal first) | PROVED |
| §3 | Lemma FREEZE-EXIT (late fallbacks switch no vertex of U ∖ T) | PROVED |
| §4 | Lemma CN-ONLY (a fallback switching no vertex of U ∖ T is a CN-LAST fallback; ≤ 1 per phase) | PROVED |
| §5 | Lemma THETA-AFTER (≤ deg_U(o) + |U| − 2 θ-changes after g_{|U|−2}) | PROVED |
| §6 | Theorem FB-POLY (a)-(d) | PROVED |
- §7 is NOT TO SIGN: L-RED's CONJECTURE FB-CAP (f ≤ max(1, |U| − 2)) stays OPEN for |U| ≥ 3 (FB-POLY (b) proves it for |U| = 2); the
  two named routes (FB-CAP-1), (FB-CAP-2) are OPEN. §8 is data.
- (P) (R18's one-player premise) is used nowhere. Nothing uses H1, H2, H3, τ(o), c_w or N_HN as a hypothesis; Lemma THETA-AFTER splits
  on H1 / ¬H1 at each state and covers both.

## 0. Objects, notation, facts
### 0.1 Objects (as in P-N5-PFZ §0 and P-N5-RHO §0 = RESULTS R39's setting)
- N5's step (SPEC S4): S4a is Even's arena step (σ_{k+1} = Even's arena optimum against τ); S4b Odd's; S4c, the FALLBACK, applies when
  σ_new = σ and τ_new = τ: if Iσ_k ≠ ∅, every Even v with a gate sets σ_{k+1}(v) := the w with (v, w) ∈ Iσ_k maximising (Ξ_k(w), w)
  (ties to the larger index), and τ and every other vertex are unchanged (FIX 3). Gates: Iσ_k := {(y, z) : y Even, z ≠ σ_k(y),
  Ξ_k(z) ▷ Ξ_k(σ_k y)} (S2).
- Valuations x = (c, P, ℓ) and Even's order ⊴ (S1): first reward(c) = ±p′(c) (p′ injective, so the reward is injective on vertices), then
  the signed weight Σ_{u∈P} sgn(u)·2^rank(u) of P (sgn(u) = +1 for Ω(u) even, −1 for odd), then ℓ (longer is better for Even iff Ω(c)
  is odd). P(x) consists of vertices of p′ > p′(c) on the play before c; a cycle node's own value is (c, ∅, 0).
- Honest frame Ξ_k := Ξ_{σ_k} (against Odd's optimal counterstrategy σ̄_k); λ_k(v) := the cycle node of Ξ_k(v); next_k(v) := σ_k(v)
  for Even v, σ̄_k(v) for Odd v; the HONEST PLAY at k from v follows next_k. W_k := the valuation of the (σ_k, τ)-play.
- θ := Ξ(o), c_θ := λ(o). R_k := {v ≠ o : v's (σ_k, τ)-play reaches o}; R̄_k := R_k ∪ {o}; F_k := V ∖ R̄_k. H1: o lies on no honest
  cycle.
- PHASE: a maximal run of consecutive states with λ_Ξ and τ constant (= a joint λ-phase, RESULTS R38 (a)). An IN-PHASE transition has
  both ends in the phase; then λ_{k+1} = λ_k and τ_{k+1} = τ_k, so it is an S4a step or an Even S4c fallback (an Odd fallback changes τ).
  A θ-RUN is a maximal run of consecutive states of one phase with θ constant.
- U := λ^{-1}(c_θ) (constant on the phase; o, c_θ ∈ U); Û := U ∖ {o}; T := {o, c_θ} (the TERMINALS); deg_U(o) := |succ(o) ∩ U|.
- wt(v) := sgn(v)·2^rank(v) if rank(v) > rank(c_θ), else 0; s_θ := +1 if Ω(c_θ) is odd, −1 if even. For z ∈ U:
  κ_t(z) := (M_t(z), s_θ·ℓ(Ξ_t z)) with M_t(z) := the signed weight of P(Ξ_t z), ordered lexicographically; κwt(v) := (wt(v), s_θ);
  κwt(A) := Σ_{v∈A} κwt(v) componentwise.
- G_Û: the graph on Û in which every Even v ∈ Û ∖ {c_θ} keeps its edges into Û, every Odd v ∈ Û ∖ {c_θ} keeps its forced edge if it lies
  in Û, and c_θ is a sink. G_U^o (new): the graph on U ∖ {c_θ} in which every Even v keeps its edges into U ∖ {c_θ}, every Odd v ≠ o
  keeps its forced edge if it lies in U ∖ {c_θ}, and o is a sink. G_U (P-N5-PFZ §0): the graph on U with Even edges into U, forced Odd
  edges into U at Odd v ∉ T, and o, c_θ sinks. κoptÛ(z) := max{κwt(p ∖ {c_θ}) : p a simple path of G_Û from z to c_θ}.
- g_1 < g_2 < … : the in-phase Even S4c fallbacks of the phase (transitions g_j → g_j + 1). "t > g_j" is about states; t > g_0 means
  every state. For a θ-run Θ: f^Θ_1 < f^Θ_2 < … its in-phase Even fallbacks k → k+1 with k ∈ Θ. At a fallback k → k+1: S_k := the set of
  Even vertices that switch (= the gate sources, since S4c switches every Even vertex with a gate), x*_v := σ_{k+1}(v) for v ∈ S_k, and
  S_U := S_k ∩ (U ∖ T).

### 0.2 Dependencies (statement used / where / status)
| tag | statement used | location | status |
| --- | --- | --- | --- |
| (V1) | if λ(v) ≠ v, Ξ(v) = v ⊕ Ξ(next v): v is added to P iff p′(v) > p′(cycle node), length + 1, same cycle node | VJ00 BRICS RS-00-48 §4.2; RESULTS R17 (a) | LANDED |
| R15 (a) | Ξ_k ⊴ Ξ_{k+1} pointwise at every transition, fallbacks included | RESULTS R15 (a) | LANDED |
| Lemma S (a) | Ξ_σ is the pointwise minimum of V_{σ,τ′} over Odd's strategies τ′ (VJ00 (11) on G) | RESULTS R18 (d) (second source: XW, RESULTS R21 (a)) | LANDED (R18 signed with gaps S1, S2, G-1OA-6) |
| G (a) | off R, Ξ = W | RESULTS R19 (a) | LANDED |
| FBL-N (ii) | at an S4c fallback with τ unchanged, every gate (x, z) with x ∈ F_k has x = λ_W(x) and λ_W(z) = x | RESULTS R21 (c) | LANDED |
| KEY | a (λ_Ξ, τ)-phase is a joint λ-phase | RESULTS R38 (a) | LANDED (names the setting) |
| CN-LAST | if at an S4c fallback with Iσ_k ≠ ∅ every gate (y, z) has λ_k(y) = y and lev(Ξ_k(σ_k y), Ξ_k(z)) = −1 (same cycle node, same P, different length), then Ξ_{k+1} = Ξ_k, Iσ_{k+1} = ∅ and k + 1 is the last state of its phase | RESULTS R38 (f) (every game) | LANDED |
| setting | phases, R, F, H1, routes on 𝒞^1O | RESULTS R39 | LANDED |
| (A), (A0), (M1′), (M2′), FB-ROUND, HAT-FREEZE | M forms | P-N5-PFZ §1 (pinned 283bcb67); P-N5-RHO §0, §2 (pinned c8144551) | signed by both referees, in landing (PFZ: R-N5-PFZ 8595343, R2-N5-PFZ 37e55fd; RHO: R-N5-RHO 59278313, R2-N5-RHO 269ae45a); restated below in κ form WITH proofs, so this packet does not rest on them |
| Y-FORM | (a) at H1, M form; (b) P(θ) = ∅ at ¬H1 | P-N5-RHO §1 | as above; κ form of (a) and (b) proved below |
- Item → dependencies:
  | item | depends on |
  | --- | --- |
  | §0.3 facts | (V1), R15 (a), S1 |
  | §1 κ-FB-ROUND | (Aκ), (M1κ), (M2κ), S4c |
  | §1 κ-HAT-FREEZE | κ-FB-ROUND, (Aκ), (M2κ), (HP), (SP′) |
  | §1 κ-PFZ | κ-FB-ROUND, (Aκ), (M2κ) |
  | §1 κ-Y-FORM | (Aκ), (M1κ), (HP), Lemma S (a), G (a) |
  | §2 EXIT-SWITCH | (Aκ), (SP′), S4c, in-phase λ |
  | §3 FREEZE-EXIT | EXIT-SWITCH, κ-HAT-FREEZE (a), κ-PFZ, (Aκ), (M1κ) |
  | §4 CN-ONLY | FBL-N (ii), G (a), (HP), (Aκ), (A0κ), (M1κ), (M2κ), (YB), (INJ), S1, S4c, CN-LAST |
  | §5 THETA-AFTER | κ-Y-FORM, κ-HAT-FREEZE (c), (YB), (M2κ), (INJ) |
  | §6 FB-POLY | §2-§5 |

### 0.3 Facts (each with its proof)
- (Aκ) For every state t and z ∈ U ∖ {c_θ}: next_t(z) ∈ U and κ_t(z) = κwt(z) + κ_t(next_t z). Proof: λ_t(z) = c_θ ≠ z, so (V1) gives
  Ξ_t(z) = z ⊕ Ξ_t(next_t z) with cycle node c_θ; so next_t(z) ∈ U. ⊕ adds z to P iff rank(z) > rank(c_θ) (p′ and rank order agree) and
  adds 1 to ℓ. No double count: if z ∈ P(Ξ_t next_t z), z lies on its own play's cycle, whose top is c_θ, so rank(z) < rank(c_θ), wt(z) = 0
  and z is in neither P. □
- (A0κ) κ_t(c_θ) = (0, 0) (cycle node value (c_θ, ∅, 0)); and M_t(next_t c_θ) = 0: next_t(c_θ) lies on c_θ's own cycle (λ_t(c_θ) = c_θ,
  so c_θ is on its honest cycle), whose top is c_θ, so P(Ξ_t next_t c_θ) = ∅.
- (M1κ) For valuations x, x′ with cycle node c_θ: x ⊴ x′ ⇔ κ(x) ≤ κ(x′), where κ(x) := (signed weight of P(x), s_θ·ℓ(x)). Proof: S1's
  order with equal rewards. In particular, for y, z ∈ U at states t, t′ of one phase: Ξ_t(y) ⊴ Ξ_{t′}(z) ⇔ κ_t(y) ≤ κ_{t′}(z).
- (M2κ) For z ∈ U and every in-phase transition t → t+1: κ_t(z) ≤ κ_{t+1}(z). Proof: R15 (a) and (M1κ) (λ_{t+1}(z) = λ_t(z) = c_θ).
- (INJ) The signed weight is injective on vertex sets (distinct powers of 2). So M_t(z) = 0 ⇔ P(Ξ_t z) = ∅, and θ (cycle node c_θ on
  the phase) is determined by κ_t(o).
- (HP) On 𝒞^1O the honest play and the (σ_t, τ)-play from any vertex agree until their first visit of o (they use the same edge at
  every vertex other than o: σ_t at Even vertices, the forced edge at Odd vertices ≠ o). Hence: (i) if the honest play from v never
  visits o, v ∈ F_t; (ii) if it visits o, λ_t(v) = λ_t(o) = c_θ (from o on it is o's honest play), so v ∈ U.
- (SP′) For z ∈ U ∖ {c_θ}: the honest play at t from z stays in U and visits c_θ, and its prefix up to its first visit of T is a simple
  path. Proof: it stays in U by (Aκ) (applied at each vertex of U ∖ {c_θ} it meets). It ends in a cycle whose cycle node is c_θ, so the
  cycle contains c_θ. A play is a lasso: its vertices are pairwise distinct up to the first repetition, which occurs only after the whole
  cycle has been traversed once, hence after the visit of c_θ ∈ T. □
- (YB) At a ¬H1 state t: P(θ_t) = ∅; and if o ≠ c_θ, 1 ≤ ℓ(θ_t) ≤ |U| − 1. Proof: o lies on its honest cycle, whose cycle node λ_t(o) =
  c_θ is the top of that cycle; P(θ_t) consists of vertices of o's honest path before c_θ of rank > rank(c_θ); they lie on the cycle, so
  there are none (the same fact as RESULTS R34 (a) (F)). If o ≠ c_θ, ℓ(θ_t) is the length of o's honest path to c_θ, a simple path in
  U ((SP′)) with ≥ 1 edge, so ≤ |U| − 1. □

## 1. The κ-freeze lemmas (PROVED)
### Lemma κ-FB-ROUND
Statement. At an in-phase Even fallback k → k+1, for every Even v ∈ U ∖ {c_θ} and every successor x ∈ U of v:
κ_{k+1}(v) ≥ κwt(v) + κ_k(x).
Proof.
- If Ξ_k(x) ⊴ Ξ_k(σ_k v): κ_k(x) ≤ κ_k(σ_k v) by (M1κ) (both in U), so κwt(v) + κ_k(x) ≤ κwt(v) + κ_k(σ_k v) = κ_k(v) ≤ κ_{k+1}(v)
  ((Aκ), (M2κ)).
- Otherwise (v, x) ∈ Iσ_k, so S4c sets σ_{k+1}(v) = x* with Ξ_k(x*) ⊵ Ξ_k(x). λ_{k+1}(v) = c_θ ≠ v, so (Aκ) at k+1 gives x* ∈ U and
  κ_{k+1}(v) = κwt(v) + κ_{k+1}(x*) ≥ κwt(v) + κ_k(x*) ≥ κwt(v) + κ_k(x) ((M2κ); (M1κ)). □

### Lemma κ-HAT-FREEZE
Statement. In a phase:
- (a) For every j ≥ 0, every state t > g_j, every z ∈ Û and every simple path p of G_Û from z to c_θ with ≤ j edges: κ_t(z) ≥ κwt(p ∖ {c_θ}).
- (b) For every state t and z ∈ F_t ∩ U: κoptÛ(z) is defined and κ_t(z) ≤ κoptÛ(z).
- (c) If |U| ≥ 2: κ_t(y) = κoptÛ(y) for every state t > g_{|U|−2} and every y ∈ F_t ∩ U.
Proof.
- (a) Induction on j. j = 0: p has no edge, z = c_θ, κ_t(c_θ) = (0, 0) = κwt(∅). Step j − 1 → j: p = z·p′, z ≠ c_θ, p′ a simple path of
  G_Û from x with ≤ j − 1 edges.
  - z Odd: x is z's forced successor, so x = next_t(z); (Aκ) and the hypothesis at t (t > g_j > g_{j−1}): κ_t(z) = κwt(z) + κ_t(x) ≥
    κwt(z) + κwt(p′ ∖ {c_θ}).
  - z Even: k := g_j < t. The hypothesis at k (k > g_{j−1}; every state if j = 1) gives κ_k(x) ≥ κwt(p′ ∖ {c_θ}). κ-FB-ROUND at k gives
    κ_{k+1}(z) ≥ κwt(z) + κ_k(x), and (M2κ) from k+1 to t gives κ_t(z) ≥ κ_{k+1}(z).
- (b) If z = c_θ both sides are (0, 0). Otherwise z ∈ F_t, so z's honest play avoids o ((HP): it agrees with the (σ_t, τ)-play, which
  avoids o); its prefix q up to c_θ is a simple path in U ((SP′)), hence in Û; at Even vertices it uses σ_t-edges into Û, at Odd vertices
  forced edges into Û; so q is a simple path of G_Û, and (Aκ) along q gives κ_t(z) = κwt(q ∖ {c_θ}) ≤ κoptÛ(z).
- (c) Simple paths of G_Û have ≤ |Û| − 1 = |U| − 2 edges; (a) with j = |U| − 2 gives "≥", (b) gives "≤". □

### Lemma κ-PFZ
Statement. Let o ≠ c_θ and let Θ be a θ-run of the phase. For every j ≥ 0, every t ∈ Θ with t > f^Θ_j (every t ∈ Θ if j = 0), every
z ∈ U ∖ {c_θ} and every simple path p of G_U^o from z to o with ≤ j edges: κ_t(z) ≥ κwt(p ∖ {o}) + κ_t(o). (κ_t(o) = κ(θ_Θ), constant
on Θ.)
Proof. Induction on j. j = 0: z = o. Step j − 1 → j: p = z·p′, z ≠ o, p′ a simple path of G_U^o from x with ≤ j − 1 edges.
- z Odd (z ≠ o): x = next_t(z) (forced); (Aκ) at t and the hypothesis at t.
- z Even: k := f^Θ_j < t, with k ∈ Θ and k > f^Θ_{j−1}. Hypothesis at k: κ_k(x) ≥ κwt(p′ ∖ {o}) + κ(θ_Θ). κ-FB-ROUND at k (z ∈ U ∖ {c_θ},
  x ∈ U): κ_{k+1}(z) ≥ κwt(z) + κ_k(x). k + 1 ≤ t and Θ is a run of consecutive states, so k + 1 ∈ Θ; (M2κ) from k+1 to t. □

### Lemma κ-Y-FORM
Statement. At an H1 state t: σ̄_t(o) ∈ Y_t := succ(o) ∩ U ∩ F_t and κ_t(o) = κwt(o) + min_{y∈Y_t} κ_t(y).
Proof.
- Under H1, o is not on its honest cycle, so λ_t(o) = c_θ ≠ o, and (Aκ) gives σ̄_t(o) ∈ U and κ_t(o) = κwt(o) + κ_t(σ̄_t o). The honest
  play of σ̄_t(o) is the rest of o's honest play, which never returns to o (H1); by (HP) (i) σ̄_t(o) ∈ F_t. So σ̄_t(o) ∈ Y_t and
  κ_t(o) ≥ κwt(o) + min_{y∈Y_t} κ_t(y).
- For y ∈ Y_t, let τ′ be Odd's strategy with τ′(o) = y (every other Odd vertex is forced). y ∈ F_t, so y's (σ_t, τ′)-play avoids o and
  equals its (σ_t, τ)-play: V_{σ_t,τ′}(y) = W_t(y) = Ξ_t(y) (G (a)), with cycle node c_θ. o's (σ_t, τ′)-play is o · (y's play), which
  does not return to o, so V_{σ_t,τ′}(o) = o ⊕ Ξ_t(y), and κ(o ⊕ Ξ_t y) = κwt(o) + κ_t(y) (o ∉ P(Ξ_t y) since y's play avoids o; length
  + 1). Lemma S (a) gives Ξ_t(o) ⊴ o ⊕ Ξ_t(y); both have cycle node c_θ, so (M1κ) gives κ_t(o) ≤ κwt(o) + κ_t(y). □

## 2. Lemma EXIT-SWITCH (PROVED)
Statement. Let k → k+1 be an in-phase Even fallback with S_U ≠ ∅. Then some u ∈ S_U has the property: the honest play at k from x*_u
visits a vertex of T before it visits u. For such u, let e ∈ T be the first vertex of T on that play and p_u := u · (that play up to e).
Then p_u is a simple path from u to e; it is a path of G_Û if e = c_θ and of G_U^o if e = o; and κ_k(x*_u) = κwt(p_u ∖ {u, e}) + κ_k(e).
Proof.
- For w ∈ S_U: λ_{k+1}(w) = λ_k(w) = c_θ ≠ w, so (Aκ) at k+1 gives x*_w = next_{k+1}(w) ∈ U. For w ∈ U ∖ T with w ∉ S_k:
  next_{k+1}(w) = next_k(w) (Even: σ unchanged by S4c; Odd w ≠ o: the forced edge).
- Suppose, for a contradiction, that for every u ∈ S_U the honest play at k from x*_u visits u before any vertex of T. Fix v ∈ S_U. By
  (SP′) at k+1 (λ_{k+1}(v) = c_θ), the honest play at k+1 from v visits c_θ ∈ T. We show it never visits T. The k+1-play stays in U
  ((Aκ) at k+1), so the only switched vertices it can meet are in S_U or in T. It starts at v ∈ S_U. Whenever it stands at some u ∈ S_U,
  it moves to x*_u; the k-play from x*_u visits u before T, so its first vertex in S_U ∪ T lies in S_U; up to that vertex, every vertex
  visited is in U ∖ (S_U ∪ T), where the k+1-play and the k-play take the same step (first bullet). So the k+1-play follows the k-play from
  x*_u up to a vertex u′ ∈ S_U, visiting no terminal in between, and the argument repeats at u′. Hence the k+1-play from v never visits
  T: a contradiction.
- For u as in the statement: the k-play from x*_u up to its first vertex of T is a simple path ((SP′) if x*_u ∉ T; the single vertex e
  if x*_u ∈ T) that avoids u, so p_u is simple. Its first edge is u → x*_u (u Even, x*_u ∈ U); its other edges are σ_k-edges at Even
  vertices and forced edges at Odd vertices ≠ o, all inside U ((Aκ)); before e it avoids T. So p_u is a path of G_Û (if e = c_θ: it
  avoids o) or of G_U^o (if e = o: it avoids c_θ). (Aκ) along the play from x*_u to e gives κ_k(x*_u) = κwt(p_u ∖ {u, e}) + κ_k(e). □

## 3. Lemma FREEZE-EXIT (PROVED)
Statement. Let o ≠ c_θ, and let k = g_j be an in-phase Even fallback that is the i-th fallback of its θ-run Θ (k = f^Θ_i). If
j ≥ |U| − 1 and i ≥ |U| − 1, then S_U = ∅.
Proof. Suppose S_U ≠ ∅; take u, e and p_u from EXIT-SWITCH. p_u lies in G_Û or G_U^o, each with |U| − 1 vertices, so it has ≤ |U| − 2
edges. u switches through a gate: Ξ_k(x*_u) ▷ Ξ_k(σ_k u), both with cycle node c_θ (x*_u, σ_k(u) ∈ U), so κ_k(x*_u) > κ_k(σ_k u) (M1κ).
- e = c_θ: k > g_{|U|−2} (j ≥ |U| − 1), so κ-HAT-FREEZE (a) with p_u gives κ_k(u) ≥ κwt(p_u ∖ {c_θ}) = κwt(u) + κwt(p_u ∖ {u, c_θ}) =
  κwt(u) + κ_k(x*_u) (EXIT-SWITCH, κ_k(c_θ) = (0, 0)).
- e = o: k ∈ Θ and k > f^Θ_{|U|−2} (i ≥ |U| − 1), so κ-PFZ with p_u gives κ_k(u) ≥ κwt(p_u ∖ {o}) + κ_k(o) = κwt(u) + κ_k(x*_u).
In both cases (Aκ) at u gives κ_k(σ_k u) = κ_k(u) − κwt(u) ≥ κ_k(x*_u), a contradiction. □

## 4. Lemma CN-ONLY (PROVED)
Statement. Let k → k+1 be an in-phase Even fallback with S_U = ∅. Then every gate (y, z) ∈ Iσ_k has λ_k(y) = y and
lev(Ξ_k(σ_k y), Ξ_k(z)) = −1. Hence (CN-LAST) k + 1 is the last state of its phase, and a phase has at most one such fallback.
Proof.
- (1) Every switched y is a cycle node of Ξ_k. y ∈ U ∖ T is excluded (S_U = ∅); o is Odd; c_θ is a cycle node. If y ∉ U, y's honest play
  never visits o ((HP) (ii)), so y ∈ F_k ((HP) (i)); FBL-N (ii) gives y = λ_W(y), and λ_W(y) = λ_k(y) by G (a). The gate sources are
  exactly the switched vertices (S4c).
- (2) For a switched y: λ_{k+1}(y) = λ_k(y) = y, so y lies on its own honest cycle at k+1; x*_y = next_{k+1}(y) lies on that cycle, so
  λ_k(x*_y) = λ_{k+1}(x*_y) = y. Claim: P(Ξ_k σ_k y) = ∅ and P(Ξ_k x*_y) = ∅.
  - σ_k(y) lies on y's honest cycle at k, whose top is y; its play to y meets only vertices of p′ < p′(y): P(Ξ_k σ_k y) = ∅.
  - y ≠ c_θ. Every vertex of λ_k^{-1}(y) has an honest play avoiding o ((HP) (ii)), so lies in F_k ∖ U. The k-play from x*_y stays in
    λ_k^{-1}(y) and reaches y. Its vertices other than y are not cycle nodes, so they have no gate (FBL-N (ii) with G (a), as in (1)) and do
    not switch; its Odd vertices are not o (o ∈ U), so they are forced. So the k+1-play from x*_y is the same path, y's honest cycle at
    k+1 is y · (that path), and y is its top: every vertex of the path has p′ < p′(y), and P(Ξ_k x*_y) = ∅.
  - y = c_θ, and the k-play from x*_y meets c_θ before o. Its vertices before c_θ are in U ∖ T, not switched (S_U = ∅), Even or forced
    Odd: the k+1-play is the same path, c_θ's honest cycle at k+1 is c_θ · (that path), and as above P(Ξ_k x*_y) = ∅.
  - y = c_θ, and the k-play from x*_y meets o first (possibly x*_y = o), along a path π from x*_y to o (o excluded). π is unchanged at
    k+1 (same reason), so the k+1-play from c_θ is c_θ · π · o · …, and it returns to c_θ (c_θ is on its own honest cycle at k+1). So o
    and π lie on c_θ's honest cycle at k+1: ¬H1 holds at k+1, P(θ_{k+1}) = ∅, i.e. M_{k+1}(o) = 0 ((YB)), and every vertex of π has
    rank < rank(c_θ), wt = 0. (Aκ) along π and (M2κ) at o: M_k(x*_y) = M_k(o) ≤ M_{k+1}(o) = 0. The gate Ξ_k(x*_y) ▷ Ξ_k(σ_k c_θ), with
    M_k(σ_k c_θ) = 0 ((A0κ)) and (M1κ), gives M_k(x*_y) ≥ 0. So M_k(x*_y) = 0 and P(Ξ_k x*_y) = ∅ (INJ).
- (3) Every gate (y, z): Ξ_k(σ_k y) ◁ Ξ_k(z) ⊴ Ξ_k(x*_y), since x*_y maximises (Ξ_k(w), w) over the gate targets of y. By (2) the two
  ends are (y, ∅, ℓ_0) and (y, ∅, ℓ*). S1 compares the reward first and the reward is injective, so Ξ_k(z) has cycle node y; then the
  signed weight of P(Ξ_k z) lies between 0 and 0, so P(Ξ_k z) = ∅ (INJ). So Ξ_k(z) and Ξ_k(σ_k y) have the same cycle node and the same P
  and differ (strictly ordered), hence only in length: lev = −1. With (1), CN-LAST's hypothesis holds (Iσ_k ≠ ∅: y switches), so
  k + 1 is the last state of the phase. A second such fallback k′ → k′+1 in the phase would have k′ + 1 ≤ k, i.e. k′ + 1 not last. □

## 5. Lemma THETA-AFTER (PROVED)
Statement. Let o ≠ c_θ. If the phase has at least |U| − 2 in-phase Even fallbacks, then at most deg_U(o) + |U| − 2 of its transitions
t → t+1 with t > g_{|U|−2} change θ; hence at most deg_U(o) + |U| − 1 θ-runs of the phase contain a state t > g_{|U|−2}.
Proof. θ has cycle node c_θ on the phase, so θ_t is determined by κ_t(o) (INJ), and κ_t(o) is non-decreasing along the phase (M2κ).
For a state t > g_{|U|−2}:
- H1 at t: κ-Y-FORM gives κ_t(o) = κwt(o) + min_{y∈Y_t} κ_t(y), and κ-HAT-FREEZE (c) gives κ_t(y) = κoptÛ(y) for y ∈ Y_t ⊆ F_t ∩ U. So
  κ_t(o) ∈ V_H := {κwt(o) + κoptÛ(y) : y ∈ succ(o) ∩ U, κoptÛ(y) defined}, and |V_H| ≤ deg_U(o).
- ¬H1 at t: (YB) gives κ_t(o) ∈ V_N := {(0, s_θ·ℓ) : 1 ≤ ℓ ≤ |U| − 1}, |V_N| = |U| − 1.
So on the states t > g_{|U|−2}, κ(o) is a non-decreasing sequence with values in V_H ∪ V_N; it changes at most deg_U(o) + |U| − 2
times, and each θ-change is a κ(o)-change. The θ-runs meeting these states are separated by these changes. □
- Remark. This is the κ form of RHO-TAIL (P-N5-RHO §3), which counts only P(θ)-changes because HAT-FREEZE freezes only M; κ-HAT-FREEZE
  also freezes lengths, which bounds all θ-changes after the freeze.

## 6. Theorem FB-POLY (PROVED)
Statement. Let f be the number of in-phase Even S4c fallbacks of a phase of N5 on 𝒞^1O.
- (a) If o ≠ c_θ: f ≤ 1 + (|U| − 2)·(deg_U(o) + |U|) ≤ 1 + (n − 2)(2n − 1).
- (b) If |U| = 2: f ≤ 1.
- (c) If o = c_θ: f ≤ |U|.
- (d) At most one of the fallbacks has S_U = ∅, and that one (if any) is followed by the last state of the phase.
Proof.
- (d) is CN-ONLY.
- (a) Split the fallbacks g_j. Those with S_U = ∅: at most 1 (d). Those with S_U ≠ ∅ and j ≤ |U| − 2: at most |U| − 2. Those with
  S_U ≠ ∅ and j ≥ |U| − 1: by FREEZE-EXIT each is among the first |U| − 2 fallbacks of its θ-run, and its θ-run contains the state
  g_j > g_{|U|−2}; by THETA-AFTER (its hypothesis holds: there are ≥ |U| − 1 fallbacks) at most deg_U(o) + |U| − 1 θ-runs qualify, each
  contributing ≤ |U| − 2. Total ≤ 1 + (|U| − 2) + (|U| − 2)(deg_U(o) + |U| − 1) = 1 + (|U| − 2)(deg_U(o) + |U|). With deg_U(o) ≤ n − 1 and
  |U| ≤ n: ≤ 1 + (n − 2)(2n − 1).
- (b) U = {o, c_θ}, so U ∖ T = ∅ and S_U = ∅ at every fallback; (d).
- (c) o = c_θ: T = {o}, θ = (o, ∅, 0) at every state, so the phase is one θ-run. EXIT-SWITCH holds verbatim with T = {o} (its proof uses
  only that the k+1-play from a switched vertex visits a terminal), and p_u is a simple path of G_U (o = c_θ its only sink) with
  ≤ |U| − 1 edges. κ-PFZ holds verbatim in G_U for z ∈ U ∖ {o} (κ(θ) = (0, 0); FB-ROUND's v ranges over U ∖ {c_θ} = U ∖ {o}). So at the
  i-th fallback with i ≥ |U| (> f_{|U|−1}), FREEZE-EXIT's argument (case e = o) gives S_U = ∅. Hence ≤ |U| − 1 fallbacks with S_U ≠ ∅,
  plus ≤ 1 by (d). □
- Remarks (READING, not to sign).
  - An Odd fallback changes τ and ends the phase (SPEC S4c, FIX 3), so f counts all fallbacks inside a phase.
  - Known per-phase fallback bounds were polynomial only GIVEN other counts: FB-INT (RESULTS R38 (d), per crossing-free run), NH1-FB
    (R38 (e), ¬H1 fallbacks, given T), EPOCH (R39 (b), given breaks / crossings), PL-S″ (R40) and LV-PL (R41) (given REL(S)), OUT-1 (R42,
    given θ_ph, N_HN). FB-POLY needs none of them.
  - FB-POLY bounds no crossing, S4a step or phase count. With X-SN-PHASE (RESULTS R34 (f): X_SN ≤ 13(d_o + 1)n³(f + 1 + T) + T) it makes
    X_SN per phase polynomial; the lane's working doc docs/new/N5-XOUT-box41.md (not part of this packet) treats crossings in OUT
    stretches.

## 7. Not to sign: FB-CAP and the obstruction (OPEN)
- CONJECTURE FB-CAP (L-RED successor 17, docs/red/R71-freeze-regime-into.md): f ≤ max(1, |U| − 2) in every phase. PROVED here only for
  |U| ≤ 2 (FB-POLY (b); |U| = 1 means o = c_θ = U, where (c) gives f ≤ 1). OPEN for |U| ≥ 3.
- Obstruction. The proof gets |U| − 2 Bellman-Ford rounds for paths to c_θ once per phase (κ-HAT-FREEZE), but the rounds for paths to o
  are counted per θ-run (κ-PFZ uses κ(o) at the relaxing state; after θ rises, a route relaxed against the old κ(o) can be below its
  new optimum). THETA-AFTER bounds these restarts by deg_U(o) + |U| − 2, each costing ≤ |U| − 2 rounds. FB-CAP would follow from either:
  - (FB-CAP-1) after g_{|U|−2}, no fallback has a switched u with e = o (EXIT-SWITCH), or
  - (FB-CAP-2) a θ-change after g_{|U|−2} keeps every route relaxation valid.
  Both OPEN. No instance against either is known: the regime where they matter is never reached in data (§8).
- OPEN (not needed): EXIT-SWITCH's excluded branch (every switched vertex's target play returns to it first) is impossible as a whole;
  whether it can occur for SOME switched vertex is open. It never occurs in data (0 of 1,544 switched vertices of U ∖ T, §8).

## 8. Data (DATA; which hypotheses occur — lesson N-ENT-2)
Script experiments/new/box41/fbpoly.py (l-new d65e43af; trace = experiments/new/box38/neb_run.py trace, SPEC S3 or a given start).
Checks at every in-phase Even fallback: CN-ONLY (every switched vertex a cycle node; every gate lev −1; k + 1 the last state of the
phase); EXIT-SWITCH (some switched vertex of U ∖ T not of kind "loop") and the kind of each switched vertex of U ∖ T (loop / ct / o);
FREEZE-EXIT's halves (kind ct only at g_j with j ≤ |U| − 2; kind o only at the first |U| − 2 fallbacks of the θ-run); THETA-AFTER; the
FB-POLY bound; κ-HAT-FREEZE (a) (KH) and κ-PFZ (KP) directly against exact best κ-paths with ≤ j edges (3 ≤ |U| ≤ 12).
- (L) experiments/new/box41/lib41.txt (412 files = the P-N5-RHO §8 (L) list; 253 𝒞^1O, 159 skipped), canonical start.
- (R) `python3 experiments/new/box41/fbpoly.py --rand 4000 6 20 4101 3` (random o-cyclic 𝒞^1O, n 6-20, canonical start + 3 random Even
  start strategies per game; 433 games rejected by the generator).
- 0 failures of every check on (L) and (R).
  | set | runs | phases | fallbacks | S_U = ∅ (all followed by the phase's last state) | S_U ≠ ∅ | switched U ∖ T: ct / o / loop | KH | KP | max f per phase (|U|) |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | (L) | 253 | 990 | 660 | 21 | 639 | 1,509 / 28 / 0 | 531 | 395 | 33 (48; experiments/si/xing/instances/ccl_w48_n48.pg) |
  | (R) | 13,364 | 33,017 | 615 | 610 | 5 | 7 / 0 / 0 | 731 | 629 | 2 (17) |
- Honest caveats (for the referees to weigh):
  - The hypotheses of FREEZE-EXIT and THETA-AFTER (a fallback g_j with j ≥ |U| − 1 at |U| ≥ 3) NEVER occur in (L) or (R), as in L-RED's
    R71 §2 (library, 1.54 M random canonical runs, 4.46 M random start-pair runs, n = 3 and partial n = 4 exhaustive) and P-N5-RHO §8.
    So these two lemmas, and FB-POLY (a) beyond FB-CAP, are untested by data. Only the lemmas they rest on (KH, KP, EXIT-SWITCH, CN-ONLY)
    are tested where their hypotheses hold.
  - KH / KP are checked only for 3 ≤ |U| ≤ 12 (exact DFS).
  - FB-CAP's excess (f − max(1, |U| − 2)) is ≤ 0 everywhere; it reaches 0 only at |U| ≤ 3.
