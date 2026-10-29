# P-N5-FRAME (packet, box 65): Odd-side freeze and fixed-τ stretch reductions for N5 on every game
L-NEW successor 35 (Opus 5.5), D14 / D18, Lead reading L40. Lead 2026-10-29 20:22Z: «freeze the packet: GP*-RUN, STRETCH-RED, ODD-FREEZE,
ENT-FREEZE, FRAME-τ, COMPOSE-FREEZE, plus (a) if closed». (a) is closed (SUCC-MON, LATE-RISE, R*-RISE). Sources: docs/new/N5-FREEZE-box63.md
§1, N5-DW-box62.md §5.2, N5-STRETCH-box64.md §1.6-§1.8, §3, §5.4 (working notes; THIS packet governs where they differ).
Status: DRAFT, NOT FROZEN (RESULTS line sent to the Lead first, 2026-10-29 ~20:28Z). REDUCTION only. Nothing here bounds N5's iteration count; G-N5-TIME stays OPEN. Not a TARGET.md claim, not M3, not a step-4 pass.
Quote base: SPEC docs/new/N5-ssi-global.md and docs/RESULTS.md at l-new 9905dac3 (SPEC lines 28-57 unchanged since 2a435f8f4, R88's base).

## 0. What to sign
| § | item | label |
| --- | --- | --- |
| 2.1 | Lemma FRAME-τ | PROVED (to sign) |
| 2.2 | Lemma DUAL-ORDER (the triple order on G^d is the reverse of G's) | PROVED (to sign; restated from box 21 §2.1 Lemma R) |
| 2.3 | Lemma ODD-FREEZE | PROVED (to sign) |
| 2.4 | Lemma ENT-FREEZE | PROVED (to sign) |
| 2.5 | Corollary COMPOSE-FREEZE | PROVED (to sign) |
| 3.1 | Lemma SUCC-MON | PROVED (to sign) |
| 3.2 | Lemma LATE-RISE | PROVED (to sign) |
| 3.3 | Lemma GP*-RUN (R88's GP* and FW-R* on W-runs) | PROVED (to sign; a widening of a landed result, its own item) |
| 3.4 | Corollary R*-RISE | PROVED (to sign) |
| 3.5 | Theorem STRETCH-RED | PROVED (to sign) |
| 4 | READING, DATA | NOT to sign |

## 1. Setting and premises
- N5 = SPEC S1-S5 (FIX 1-4 as in RESULTS); any parity game G = (V, E, Ω, owner), n = |V|, m_E (m_O) = number of edges leaving Even (Odd)
  vertices. A run is the sequence of states (σ_t, τ_t); a TRANSITION is t → t + 1.
- [S1-val] [Q SPEC:28-29] «valuation of v under (σ, σ̄): (c, P, ℓ), c = the most relevant (max p') vertex of the cycle the play from v ends
  in, P = set of vertices on the play before reaching c with p' > p'(c), ℓ = number of steps to reach c.» The same definition is applied
  to any pair of positional strategies, one per player; "the (α, β)-play from v" is the unique play from v under α and β.
- [S1-ord] [Q SPEC:30-31] «order (better for Even): compare reward of c (p'(c) if even, −p'(c) if odd); then P by the signed weight
  Σ_{u∈P} (+2^rank(u) if Ω(u) even else −2^rank(u)); then ℓ: if c is odd, longer is better for Even; if c even, shorter is better.»
  ⊴ / ◁ (◁ strict) denote it, ⊵ / ▷ the reverse. Distinct triples are distinct in the order (RESULTS R84 (a) Fact DELTA, as in R88 §1).
- [S1-Xi] [Q SPEC:32] «Ξσ = valuation of every vertex under σ and Odd's OPTIMAL counterstrategy σ̄ (minimising this order at every
  vertex at once).» Ξ_t := Ξ_{σ_t}, σ̄_t its counterstrategy, λ_t (= λ_Ξ) its cycle-node map.
- [S1-dual] [Q SPEC:45-46] «Odd's side: everything on the DUAL game G^d (owner swapped, Ω + 1); τ is an "Even" strategy of G^d; Ξτ, τ̄
  (= Even's optimal counterstrategy to τ, as a G^d-Odd strategy), Iτ computed there.» U_t := Ξτ_t (on G^d), τ̄_t its counterstrategy,
  λ^U_t its cycle-node map (as in RESULTS R86 / R47).
- [S2] [Q SPEC:47] «Improving edges: Iσ = {(v, w) : owner(v) = Even, w ≠ σ(v), Ξσ(w) strictly better than Ξσ(σ(v))}; Iτ the same on
  G^d for τ.»
- [S4a] [Q SPEC:51-53] «a. If Iσ ≠ ∅: A(v) = {σ(v)} ∪ {w : (v, w) ∈ Iσ} for Even v. Arena H: Even v keeps only edges to A(v); Odd v keeps
  only the edge to τ(v). σ_new = Odd's optimal counterstrategy (S1 procedure) in the dual of H to the dual-Even strategy τ, read as an
  Even strategy of G. (Even's one-player optimum against τ among "keep or take an improving edge".) Else σ_new = σ.»
- [S4b] [Q SPEC:54-55] «b. If Iτ ≠ ∅: A(v) = {τ(v)} ∪ {w : (v, w) ∈ Iτ} for Odd v. Arena H': Odd v keeps only edges to A(v); Even v only
  the edge to σ(v). τ_new = Odd's optimal counterstrategy (S1 procedure on H', not dual) to σ. Else τ_new = τ.»
- [S4c] [Q SPEC:56-57] «c. FALLBACK, if σ_new = σ and τ_new = τ: if Iσ ≠ ∅, for every Even v with an improving edge set σ_new(v) = the w
  with (v, w) ∈ Iσ maximising (Ξσ(w), w) (best valuation, ties: larger index); otherwise do the same for Odd on Iτ with G^d's
  valuations. Count it.»
- [R15] RESULTS R15 (a) (Lemma A: Ωσ ⊴ Ω_{Switch_I(σ)} for a non-empty unambiguous set I of improvements), (c) (no strategy repeats in a
  VJ00 run with any non-empty selection rule), (d) («every iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ (on G) and/or with
  ∅ ≠ I ⊆ Iτ to Odd's τ (on G^d) … Iσ depends on σ alone»). The same on G^d for τ (R15 (d) states it for both).
- [R17-F1] RESULTS R17 (a) (F1): «the optimum of a one-player game dominates every strategy of that game pointwise».
- [R47a] RESULTS R47 Lemma Φ: along a run each vertex's cycle node in Ξ only rises in reward (and in U only falls), so at most n(n − 1)
  transitions change λ and at most n(n − 1) change λ^U (as cited in R86 Corollary COMPOSE-RUN).
- [R86] RESULTS R86: for a stretch R, ENT_R(v, c) = the transitions of R at which v's strategy enters c (switches to c); RISE_R(c),
  PCH_R(c); Lemma SW-RETURN (ENT_R(v, c) ≤ 1 + RISE_R(c) on every stretch, dually for Odd v with U on G^d); Lemma LEN-MONO (RISE_R(c) ≤
  PCH_R(c) + (PCH_R(c) + 1)(n − 1) on every λ-run, dually on λ^U-runs); λ-run, λ^U-run as defined there.
- [R85c] RESULTS R85 (c) (docs/RESULTS.md l. 5108-5109 at trunk c9045f86 = l-new c9045f86): [Q] «(c) Added statement (A), Corollary (A2):
  "PCH_𝒫(v) ≤ (K(K+1)/2)(NM_𝒫(v) + 1) + NM_𝒫(v) per vertex per phase, every game"». K = the ranks above rank(λ(v)), NM_𝒫(v) = v's carries
  (R86 (e)'s gloss, l. 5350-5351). This is the PER-VERTEX form.
- [R86e] RESULTS R86 (e) (l. 5345-5357): Corollary COMPOSE-NM, an implication whose premise «[MΦ] holds with "phase" replaced by "λ-run"
  (resp. "λ^U-run" on G^d)» both referees sign as HOLDING («MΦ's proof reads verbatim with c fixed»; REFEREE-2: «MATCH-Φ's proof holds
  for every parity pattern»), with NM^U read with G^d's parities (F3). Used here in the per-vertex form of [R85c] on one λ^U-run R:
  PCH^U_R(e) ≤ (n²/2)(NM^U_R(e) + 1) + NM^U_R(e) (K ≤ n − 1 gives K(K + 1)/2 ≤ n²/2, as R86 (e) notes).
- [R88] RESULTS R88 and its object docs/si/P-N5-GP-box31.md (sha1 cd4866df…): W_t := the valuation [S1-val] of the (σ_t, τ_t)-plays, λ_W
  its cycle-node map, G_τ := G with Odd fixed to τ; Lemma W-MON (§2), Lemma GP* (§3, with BLOCKED at t: W_t(z) ▷ W_t(σ_t x) and (x, z) ∉
  Iσ_t), Corollary FW-R* (§4, LATE ADOPTION, R*_T, WCH).
- [R56] RESULTS R56 Theorem FB-RED: «in-phase fallbacks per phase are at most 1 + (n − 1)(2 + ρ), ρ := the Ξ-changes at Odd choice vertices
  in the phase»; phase = RESULTS R38 (a) (a maximal run of states with (λ_Ξ, τ) constant); its fallbacks are Even S4c fallbacks.
- New definitions.
  - τ-STRETCH: a maximal run of consecutive states with τ_t constant.
  - W-RUN: a maximal run of consecutive states of one τ-stretch such that no transition t → t + 1 inside it is an S4c fallback or
    changes λ_W. (σ̄_t and λ_Ξ may change inside a W-run.)
  - For an Odd o, e ∈ succ(o), e ≠ τ_t(o), state t: (o, e) is PROTECTED AT t if ODD-FREEZE's hypotheses (H1′), (H2), (H3) hold at t.
  - PCH^U_R(e): the transitions of the λ^U-run R at which the path set of U(e) changes (R86's PCH on G^d).

## 2. The Odd side
### 2.1 Lemma FRAME-τ
(i) In [S4a]'s arena H, every Odd vertex v keeps only the edge to τ(v). (ii) At every transition, τ_{t+1}(o) ∈ {τ_t(o)} ∪ Iτ_t(o) for every
Odd o. (iii) No value of τ repeats along a run. (iv) Iτ_t depends on τ_t alone.
Proof. (i) is [S4a] verbatim. (ii) If S4b fires, τ_new(o) is chosen in H′, where o keeps only edges to {τ(o)} ∪ Iτ(o); if not, τ_new = τ;
S4c's Odd branch picks w with (o, w) ∈ Iτ; S4c's Even branch leaves τ. (iii) Each change of τ is Switch_I on G^d with ∅ ≠ I ⊆ Iτ (R15 (d)),
and no strategy repeats in such a sequence (R15 (c) on G^d, any non-empty selection rule; the τ-changing transitions form one). (iv) Iτ is
defined from Ξτ on G^d ([S2], [S1-dual]), which depends on τ alone; R15 (d) states the mirror «Iσ depends on σ alone». □
### 2.2 Lemma DUAL-ORDER
For any two plays π, π′ of G, their [S1-val] triples (c, P, ℓ) are the same in G and G^d (relevance = rank, the same in both games), and π
is strictly better for Even than π′ in G's [S1-ord] iff π is strictly worse for the G^d-Even player (Odd) than π′ in G^d's [S1-ord].
Proof (box 21 §2.1 Lemma R, restated). Ranks are positions in V sorted by (Ω(v), v); Ω + 1 preserves that order, so rank, relevance and
the triples (c, P, ℓ) agree in G and G^d. Each component of [S1-ord] reverses:
- cycle nodes c ≠ c′: if both have even Ω in G, G prefers the more relevant one, and in G^d both are odd, so G^d's Even player prefers the
  less relevant one; both odd in G: the mirror; mixed: G's Even prefers the G-even one, G^d's Even the G^d-even one, i.e. the other;
- path sets: each term's sign is the parity of Ω(u), which flips, so the signed weight in G^d is the negative of G's;
- length: "longer is better iff c is odd" flips with the parity of c.
So "strictly better for Even in G" ⇔ "strictly better for Odd (the G^d-Odd player) in G^d" ⇔ "strictly worse for the G^d-Even player". □
### 2.3 Lemma ODD-FREEZE
Setting: a state (σ, τ) of the run; τ̄ := τ̄(τ) [S1-dual]; o Odd, e ∈ succ(o), e ≠ τ(o). For an Even strategy α let P_e(α) be the
(τ, α)-play from e up to and INCLUDING its first visit of o (if any).
Hypotheses:
- (H1′) there is a positional Even strategy σ_e with σ_e(x) = τ̄(x) for every Even x ∉ P_e(σ_e), such that the (τ, σ_e)-play from e visits o
  before it repeats a vertex; write P_e := P_e(σ_e) (a simple path ending at o);
- (H2) the (τ, τ̄)-play from τ(o) has no vertex in P_e;
- (H3) the most relevant vertex x of P_e has even Ω, and x is more relevant than the cycle node w of the (τ, τ̄)-play from τ(o).
(With σ_e = τ̄, (H1′) is box 63's (H1).) Correspondence with box 63 (N5-FREEZE-box63.md §1): (H1′), (H2), (H3) here are box 63's H1′,
H2, H3 for "that play", made exact in two places: σ_e is POSITIONAL and the play is the (τ, σ_e)-play; P_e INCLUDES o (box 63's "cut at
the first visit of o"), so (H2) also says the play from τ(o) avoids o. Claim: (o, e) ∉ Iτ.
Proof.
- The (τ, σ_e)-play from e is P_e followed by the (τ, σ_e)-play from τ(o) (Odd o follows τ). The (τ, τ̄)-play from τ(o) never enters P_e
  (H2), and σ_e = τ̄ outside P_e, so by induction along that play the (τ, σ_e)-play from τ(o) is the same play: call it π_o, cycle node w,
  path set P_o, length ℓ_o. It is disjoint from P_e, so w ∉ P_e.
- So the (τ, σ_e)-play from e has cycle node w, path set P_o ∪ {y ∈ P_e : y more relevant than w}, length |P_e| + ℓ_o. The two path sets
  differ exactly in {y ∈ P_e : y more relevant than w}, whose most relevant element is x (by (H3), x ∈ P_e is more relevant than w, and it is
  the most relevant vertex of P_e). x has even Ω, so its signed-weight term +2^rank(x) dominates (all other differing terms have smaller
  rank). Hence, in G's order [S1-ord], the (τ, σ_e)-play from e is strictly better for Even than π_o.
- τ̄ minimises the order at every vertex at once for the G^d-Odd player [S1-dual], i.e. (DUAL-ORDER) it maximises G's order for Even among
  plays (τ, α) from e. So U(e) (the (τ, τ̄)-play from e) is at least as good for Even as the (τ, σ_e)-play, hence strictly better for Even
  than U(τ(o)) = π_o.
- By DUAL-ORDER, U(e) is strictly WORSE for the G^d-Even player than U(τ(o)). [S2] on G^d puts (o, e) into Iτ only if U(e) is strictly
  better for the G^d-Even player than U(τ(o)). So (o, e) ∉ Iτ. □
### 2.4 Lemma ENT-FREEZE
If (o, e) is protected at t (and τ_t(o) ≠ e), then τ_{t+1}(o) ≠ e.
Proof. ODD-FREEZE gives (o, e) ∉ Iτ_t; FRAME-τ (ii) gives τ_{t+1}(o) ∈ {τ_t(o)} ∪ Iτ_t(o); e is neither. □
### 2.5 Corollary COMPOSE-FREEZE
Let R be a λ^U-run (R86). Call (o, e) UNPROTECTED IN R if at some state t of R with t + 1 ∈ R and τ_t(o) ≠ e, (o, e) is not protected at t;
UNP_R := the set of such Odd edges. Then
(a) ENT_R(o, e) = 0 for every Odd edge (o, e) ∉ UNP_R;
(b) ENT_R(o, e) ≤ 1 + RISE^U_R(e) ≤ n·(PCH^U_R(e) + 1) for (o, e) ∈ UNP_R;
(c) the Odd switches in R (Σ over Odd o of the transitions of R at which τ(o) changes) are at most Σ_{(o, e) ∈ UNP_R} n·(PCH^U_R(e) + 1);
(d) the τ-changing transitions of the whole run are at most n(n − 1) + (n(n − 1) + 1)·max_R Σ_{(o, e) ∈ UNP_R} n·(PCH^U_R(e) + 1).
(e) with [R85c] / [R86e] per vertex on λ^U-runs: PCH^U_R(e) ≤ (n²/2)(NM^U_R(e) + 1) + NM^U_R(e), so (b)-(d) hold with PCH^U_R(e)
    replaced by that bound, i.e. in terms of the carries NM^U_R(e) of the targets of unprotected Odd edges only.
Proof. (a) An entry of e by o at t → t + 1 needs τ_t(o) ≠ e = τ_{t+1}(o); if (o, e) ∉ UNP_R then (o, e) is protected at t, and ENT-FREEZE
excludes it. (e) is [R85c] read on R as [R86e] signs it. (b) R86 SW-RETURN (dual), then LEN-MONO (dual) on the λ^U-run R: 1 + PCH + (PCH + 1)(n − 1) ≤ n(PCH + 1). (c) Every Odd switch
of o in R enters some e, so the switches are Σ_e ENT_R(o, e); apply (a), (b). (d) At most n(n − 1) transitions change λ^U ([R47a]); every
other τ-changing transition lies inside one of at most n(n − 1) + 1 λ^U-runs and contains at least one Odd switch. □

## 3. The Even side inside a τ-stretch
### 3.1 Lemma SUCC-MON
For every Even y, Ξ_t(σ_t(y)) is non-decreasing (⊴) in t along every run.
Proof. At each transition σ_{t+1}(y) ∈ {σ_t(y)} ∪ Iσ_t(y): [S4a]'s arena allows only these; S4c's Even branch picks from Iσ; otherwise σ is
unchanged. Ξ_{t+1} ⊵ Ξ_t pointwise: either σ_{t+1} = σ_t, or σ_{t+1} = Switch_I(σ_t) with ∅ ≠ I ⊆ Iσ_t (R15 (d)) and R15 (a). If σ_{t+1}(y) =
σ_t(y), Ξ_{t+1}(σ_{t+1} y) ⊵ Ξ_t(σ_t y). Otherwise Ξ_{t+1}(σ_{t+1} y) ⊵ Ξ_t(σ_{t+1} y) ▷ Ξ_t(σ_t y) ([S2]). □
### 3.2 Lemma LATE-RISE
If (y, z) ∉ Iσ_t and (y, z) ∈ Iσ_u with t < u, then Ξ_u(z) ▷ Ξ_t(z).
Proof. Ξ_u(z) ▷ Ξ_u(σ_u y) ([S2] at u) ⊵ Ξ_t(σ_t y) (SUCC-MON) ⊵ Ξ_t(z) (if z = σ_t(y) trivially; else (y, z) ∉ Iσ_t and [S2] at t). □
### 3.3 Lemma GP*-RUN
On every W-run F = [a, b], R88's Lemma GP* and Corollary FW-R* hold verbatim, with F in place of the frozen W-phase: for every k ∈ [a, b],
W_k(r_0) ⊵ value(r) for every path r unblocked at state k (R88 §3's definition, "blocked at t" read at state t of F); and F has at most
(n − 1)(R*_T + 1) W-changing transitions, R*_T := the transitions of F containing a late adoption (R88 §4's definition, read on F).
Proof. Line by line, the R88 proofs use only the following properties of F, all of which a W-run has:
- W-MON (§2): «τ_{t+1} = τ_t = τ», «not a fallback», [S4a], [R17-F1] on H_t. Its "inside a phase" (λ_Ξ constant) is never used in the
  proof: the transition changes σ (R15 (d)) and σ_new is [S4a]'s one-player optimum of H_t, which contains σ_t.
- GP* (§3): the base case and Case B1′ (ii), B2a, B2b(i), (iii) use «λ_W constant on F»; Case A uses «not blocked at state k» with Iσ_k of
  that state; Case B uses ρ̂ ∈ H_k and W-MON. No step uses σ̄, D or λ_Ξ.
- FW-R* (§4): GP*, W-MON, «λ_W(x) constant on F, so u is a cycle node of state a», and [S4a] (ρ_{t+1}(y_i) ∈ {ρ_t(y_i)} ∪ Iσ_t(y_i)).
- σ̄, D, U_t, S_{d,t}, λ_Ξ appear only in R88's §3a (Corollaries GP, GP+), which this lemma does not restate. □
### 3.4 Corollary R*-RISE
In every W-run F, the late adoptions of a fixed Even edge (y, z) (transitions of F at which σ(y) becomes z after (y, z) was blocked at an
earlier state of F) number at most RISE_F(z), the transitions of F at which Ξ(z) changes. Hence R*_T ≤ Σ_z d_E(z)·RISE_F(z), d_E(z) the
number of Even predecessors of z.
Proof. Let u_1 < u_2 < … be the late adoptions of (y, z) in F. Put t_1 := a state of F before u_1 at which (y, z) was blocked (so (y, z) ∉
Iσ_{t_1}). For i ≥ 2 put t_i := u_{i−1} + 1: σ_{t_i}(y) = z, so (y, z) ∉ Iσ_{t_i} ([S2]: w ≠ σ(v)), and t_i < u_i because σ_{u_i}(y) ≠ z.
(Adoption u_i is the transition u_i → u_i + 1.) Each adoption is from Iσ_{u_i} ([S4a]; F has no fallback). LATE-RISE gives Ξ_{u_i}(z) ▷
Ξ_{t_i}(z), so some transition t → t + 1 with t_i ≤ t < u_i changes Ξ(z). The index intervals [t_i, u_i) are disjoint (t_i > u_{i−1}) and lie
in F (t_1 ≥ a). □
### 3.5 Theorem STRETCH-RED
Let S be a τ-stretch. Let fb_S := the S4c fallbacks inside S; R*_S := the largest R*_T of a W-run of S; FL_S := the transitions of S with
σ_{t+1} ≠ σ_t and W_{t+1} = W_t; ρ_S := the largest R56 ρ of a phase meeting S. Let |S| := the transitions inside S (all change σ:
τ is constant and every transition changes σ or τ, R15 (d)). Then
  |S| ≤ Q + (Q + 1)·((n − 1)(R*_S + 1) + FL_S),  Q ≤ fb_S + n(n − 1)(fb_S + 1),  fb_S ≤ n(n − 1) + (n(n − 1) + 1)·(1 + (n − 1)(2 + ρ_S)).
Proof.
- Q := the transitions of S that are a fallback or change λ_W; removing them leaves the W-runs of S, at most Q + 1 of them.
- λ_W: inside a fallback-free piece of S, W_{t+1} ⊵ W_t pointwise (R88 W-MON as in GP*-RUN), the cycle node is the first key component
  and rewards are injective, so each vertex's W-cycle node changes at most n − 1 times per piece: at most n(n − 1) λ_W-changing
  transitions per piece, and there are fb_S + 1 pieces.
- Each W-run: at most (n − 1)(R*_S + 1) W-changing transitions (GP*-RUN) plus its W-flat ones (≤ FL_S in total).
- fb_S: τ is constant on S, so the phases meeting S are separated by λ_Ξ-changes: at most n(n − 1) + 1 phases ([R47a]); each has at most
  1 + (n − 1)(2 + ρ) in-phase fallbacks ([R56]); a fallback transition that changes λ_Ξ is not in-phase, and there are at most n(n − 1)
  λ_Ξ-changing transitions. □
- Consequence (to sign as stated): with R*-RISE and [R86] LEN-MONO, R*_S is bounded by a polynomial in n, m_E and the largest
  PCH_R(z) over λ-runs R meeting S. (R*_T ≤ Σ_z d_E(z)·RISE_F(z); a W-run meets at most n(n − 1) + 1 λ-runs ([R47a]), RISE on each is
  ≤ n(PCH + 1), and each λ-change is one transition.)

## 4. READING and DATA (NOT to sign)
- READING: combined with box 21 Theorem B (N5 ≤ (C_τ + 1)(F_E + 1), lane), STRETCH-RED bounds N5 through ρ, P*, FL and C_τ; R86 COMPOSE-RUN
  with COMPOSE-FREEZE bounds it through P* and P^U on UNP alone. So the second route needs strictly fewer premises; FRAME-STRETCH_P is not an
  independent half (N5-STRETCH-box64.md §5.5).
- DATA (experiments/new/box64/, 719 games box59/sbcg.lst, S3 start; mkr and dual families with their start files):
  ODD-FREEZE 35,780 hypothesis hits / 0 violations (box59/freeze2_all.txt); FW-R* on W-runs 0 violations (wrun_all.txt); late adoptions
  1141, each with a Ξ-rise of z (late_all.txt); in-stretch fallbacks 607, 603 lowering W (wdrop_all.txt); FRAME-STRETCH (n + m) DEAD on mkr
  (mk_16_100: 1648 > 1225, N5-STRETCH-box64.md §1.5); ρ = (2K − 1)² on mkr.
- Pinned checks: experiments/new/check.sh blocks "box 63", "box 64".

## DONE / FINDINGS / NEEDS
- DONE: this packet (box 65), from l-new 9905dac3.
- FINDINGS: ten items to sign (§0), all reductions or structural lemmas; no iteration bound.
- NEEDS: none from the owner.
