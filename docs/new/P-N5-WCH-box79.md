# P-N5-WCH (packet, box 79): Even returns, tie switches and gap levels are paid by per-vertex W-changes; REP*, the W-run length and GAP-RED's per-phase count share one premise [P-WCHτ]
L-NEW successor 37 (Opus 5.5), D14 / D18, Lead reading L40. Lead 2026-10-30 (after 08:52Z): «TASK 1, PACKET: freeze ONE packet, P-N5-WCH,
for both referees … Scope: the items above that compose into a clean REDUCTION … trim anything that does not compose. Mark ASSUMPTION
OPT-ONLY wherever it is used … Keep N5 and N5-LZC statements separate. Every symbol must be bound in the line file … Cite only landed
RESULTS or the packet's own sections.» FROZEN 2026-10-30 (this commit; sha1 reported to the Lead).
Sources (working notes, unrefereed; THIS packet governs where they differ; none is cited as a proof): docs/new/N5-SC-box70.md §2-§3,
N5-LZ-box72.md §2-§5, N5-FBO-box73.md §3, N5-SBQ-box76.md §2, N5-RETWCH-box78.md §1-§2.
Status: REDUCTION only. No count named below as a residual is bounded here. G-N5-TIME stays OPEN. Not M3, not a step-4 pass, not a
TARGET.md claim. Quote base: l-new aefb71a3 (= trunk merge; SPEC docs/new/N5-ssi-global.md lines 24-57 unchanged since 7039eb524).
Two objects, kept apart: N5 (SPEC S1-S5, §1-§6) and the labelled VARIANT N5-LZC (§7). Nothing in §7 transfers to N5, and nothing proved
for N5 in §2-§6 is claimed for N5-LZC unless §7 proves it.

## 0. What to sign
| § | item | object | label |
| --- | --- | --- | --- |
| 2.1 | Fact REW (R1, R2) and Fact LEX (the [S1-ord] coordinate sequence) | game-general | PROVED (to sign) |
| 3 | Lemma TIE (an S4a switch without a W-rise keeps the old successor W-consistent) | N5 (any pointwise optimum of H_t) | PROVED (to sign) |
| 4.1 | Lemma NEW-BOUND (W-run length ≤ m_E + returns) | N5 | PROVED (to sign) |
| 4.2 | Theorem RET-WCH (a return of v to e is paid by a W(e)-change or by a W-flat leave) | N5 | PROVED (to sign) |
| 4.3 | Corollary RUN-WCH and Corollary REP-WCH | N5 | PROVED (to sign) |
| 5.1 | Lemma SIL-Z and Corollary SC-GXC | N5 | PROVED (to sign) |
| 5.2 | Lemma GXC-CLOSE and Theorem GXC-SPLIT | N5 | PROVED (to sign) |
| 5.3 | Lemma LEVEL-MON and Corollary DROP-PAID | N5 | PROVED (to sign) |
| 5.4 | Corollary FBO-R56, Corollary FBO-SPLIT, Corollary ZF-SPLIT | N5 | PROVED (to sign) |
| 6 | Theorem WCH-RED (the composition) and Corollary WCH-ONE (under premise [P-WCHτ]) | N5 | PROVED (to sign), a REDUCTION |
| 7.1-7.4 | N5-LZC: definition, Lemma LZ-OPT, Lemma W-MON_LZ, Theorem LZ-STRICT, Corollary RUN-WCH_LZ / REP-WCH_LZ | N5-LZC (VARIANT) | PROVED (to sign) |
| 7.5 | Corollary LZ-NOSIL | N5-LZC (VARIANT) | PROVED under ASSUMPTION OPT-ONLY (to sign: the implication; referees asked to check OPT-ONLY) |
| 8 | trimmed items, DATA, READING, symbol table | — | NOT to sign |

## 1. Setting, premises, definitions
- N5 = SPEC S1-S5 (FIX 1-4 as in RESULTS); any parity game G = (V, E, Ω, owner), V = {0, …, n − 1}, n = |V|. m_E := the number of edges
  leaving Even vertices (as in RESULTS R90); n_E := the number of Even vertices; d_E(e) := |{v Even : (v, e) ∈ E}| for a vertex e, so
  Σ_e d_E(e) = m_E. A run is the sequence of states (σ_t, τ_t); a TRANSITION is t → t + 1; "v is switched at t" means σ_{t+1}(v) ≠ σ_t(v).
- [S1-rank] [Q SPEC:26] «injective priorities: rank(v) = position of v in V sorted by (Ω(v), v); p'(v) = 2·rank(v) + (Ω(v) mod 2).» "x is
  more relevant than y" means p'(x) > p'(y). rew(x) := p'(x) if Ω(x) is even, −p'(x) if Ω(x) is odd ([S1-ord]'s "reward").
- [S1-val] [Q SPEC:27-28] «valuation of v under (σ, σ̄): (c, P, ℓ), c = the most relevant (max p') vertex of the cycle the play from v ends
  in, P = set of vertices on the play before reaching c with p' > p'(c), ℓ = number of steps to reach c.» For a value x = (c, P, ℓ):
  λ(x) := c (its CYCLE NODE), P(x) := P, ℓ(x) := ℓ. (P(x), a path set, is never the phase P: a phase is always written P without an argument.) "v is its own cycle node" (for a valuation Ω) means λ(Ω(v)) = v.
- [S1-ord] [Q SPEC:29-30] «order (better for Even): compare reward of c (p'(c) if even, −p'(c) if odd); then P by the signed weight
  Σ_{u∈P} (+2^rank(u) if Ω(u) even else −2^rank(u)); then ℓ: if c is odd, longer is better for Even; if c even, shorter is better.»
  ⊴ / ◁ (strict), ⊵ / ▷ the reverse. Distinct triples are distinct in the order (RESULTS R84 (a) Fact DELTA, as in R88-R91).
- [S1-Xi] [Q SPEC:31] «Ξσ = valuation of every vertex under σ and Odd's OPTIMAL counterstrategy σ̄ (minimising this order at every vertex at
  once).» Ξ_t := Ξ_{σ_t}; λ_Ξ := the cycle-node map v ↦ λ(Ξ_t(v)).
- [S2] [Q SPEC:47] «Improving edges: Iσ = {(v, w) : owner(v) = Even, w ≠ σ(v), Ξσ(w) strictly better than Ξσ(σ(v))}; Iτ the same on G^d for τ.»
- [S4a] [Q SPEC:51-53] «a. If Iσ ≠ ∅: A(v) = {σ(v)} ∪ {w : (v, w) ∈ Iσ} for Even v. Arena H: Even v keeps only edges to A(v); Odd v keeps only
  the edge to τ(v). σ_new = Odd's optimal counterstrategy (S1 procedure) in the dual of H to the dual-Even strategy τ, read as an Even
  strategy of G. (Even's one-player optimum against τ among "keep or take an improving edge".) Else σ_new = σ.»
- [S4c] [Q SPEC:56-57] «c. FALLBACK, if σ_new = σ and τ_new = τ: if Iσ ≠ ∅, for every Even v with an improving edge set σ_new(v) = the w
  with (v, w) ∈ Iσ maximising (Ξσ(w), w) (best valuation, ties: larger index); otherwise do the same for Odd on Iτ with G^d's valuations.»
- Standing premise (as RESULTS R90 and R91; a disclosure, not a widening): the standing SPEC premise of RESULTS R57 (1E-N3: S1's procedure
  realises the pointwise optimum); for S4a, σ_new is the POINTWISE OPTIMUM of the one-player arena H_t (RESULTS R90 (a) (i), OPT-OFF (i)).
- [R15] RESULTS R15 (a) «Lemma A: for any non-empty unambiguous set I of improvements of σ (VJ00 §4.4), Ωσ ⊴ Ω_{Switch_I(σ)}»; (d) «N5: every
  iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ (on G) and/or with ∅ ≠ I ⊆ Iτ to Odd's τ (on G^d), and changes at least one of
  them». Hence Ξ_{t+1} ⊵ Ξ_t pointwise at every transition.
- [F1] RESULTS R17 (a): «the optimum of a one-player game dominates every strategy of that game pointwise».
- [V1], [V2], [⊕] (as quoted in RESULTS R91's packet §1 and R88's object §1): «Prefix: x ⊕ (c, P, ℓ) := (c, P ∪ {x if x more relevant than c},
  ℓ + 1); this is the value of a play that steps from x to a vertex of value (c, P, ℓ) whose path to c avoids x.» «(V1) if x is not its own
  cycle node then Ω_ρ(x) = x ⊕ Ω_ρ(ρ(x)) and the ρ-path from ρ(x) to λ(x) avoids x. (V2) PREFIX MONOTONICITY: if a ⪯ b are values whose
  paths both avoid x (or whose cycle nodes differ), then x ⊕ a ⪯ x ⊕ b, and strictly if a ≺ b.» Below, x ⊕ y is always the formal
  operation on triples; [V1] / [V2] are invoked only where their hypotheses are checked. They hold for every pair of positional strategies,
  so for Ξ (pair σ, σ̄) and for W (pair σ, τ).
- Symbols of RESULTS R90 (landed; P-N5-CUT §1, quoted in R90's entry): W^τ_t := the [S1-val] valuation of the (σ_t, τ)-plays (G_τ: Odd
  fixed to τ); W_t := W^{τ_t}_t; λ_W := its cycle-node map; H_t := σ_t ∪ Iσ_t (S4a's arena at t, Odd following τ_t); an S4a STEP: «a
  transition with Iσ_t ≠ ∅, not an S4c fallback, σ_{t+1} = [S4a]'s σ_new ≠ σ_t (τ_{t+1} may differ)»; a BOUNDARY: «an Even S4c fallback or
  a τ-changing transition»; Fact B: «every transition is an S4a step with τ kept, or a boundary»; a τ*-PIECE: «a maximal run of states
  with τ_t = τ* and every inside transition an S4a step»; B_R := the boundaries inside a λ-run R; LEAVE, RE-ENTRY, ANCHOR and the classes
  F, FR, C, P, S of R90 (e) (CUT-CHARGE); SIL_R := Σ over Even edges of SIL_R(v, c) = #S (R90 (e)). λ-run: RESULTS R86 (a maximal run of
  states with λ_Ξ constant).
- RESULTS R89: a τ-STRETCH «:= a maximal run of consecutive states with τ constant»; a W-RUN «:= a maximal run of consecutive states of one
  τ-stretch none of whose transitions is an S4c fallback or changes λ_W». For a W-run F: |F| := its transitions (t, t + 1 ∈ F); τ_F := its τ.
- RESULTS R88 (f) / R90 (g): a LATE ADOPTION in a W-run F is a transition of F at which some Even vertex adopts an edge blocked at an earlier
  state of F (R88); «in a W-run F, a late adoption of (y, z) is FIRST if it is the first in F, REPEAT otherwise, REP_F := the REPEATs in F»
  (R90 (g)); REP* := max_F REP_F (R90).
- RESULTS R91 (P-N5-GAP): PHASE (RESULTS R38 (a)): a maximal run of consecutive states with (λ_Ξ, τ) constant; IN-PHASE transition: both
  states in one phase («An in-phase transition has τ_{t+1} = τ_t, hence changes σ (R15 (d)), hence is either an S4a step … or an Even S4c
  fallback», R91 packet §1); τ-FIXED EVEN FALLBACK: an S4c transition with Iσ ≠ ∅; GAP SET Z_t := {v : Ξ_t(v) ≠ W_t(v)};
  WCH^S4a_P(v) := the in-phase S4a transitions of P changing W(v); f_P := the in-phase (Even S4c) fallbacks of P; ZF_P := its in-phase
  fallbacks with Z_{k+1} = Z_k (Z-FLAT fallbacks). Landed lemmas used: R91 (a) XW «Ξ_t(v) ⊴ W_t(v) for every v and t»; (b) W-MON «If
  t → t + 1 is an S4a step, then W^{τ_t}_{t+1} ⊵ W^{τ_t}_t pointwise»; (c) FB-W «If k → k + 1 is a τ-fixed Even fallback, then W_{k+1} ⊴ W_k
  pointwise»; (h) GAP-MON «If k → k + 1 is a τ-fixed Even fallback, then Z_{k+1} ⊆ Z_k, and every v ∉ Z_k has Ξ_{k+1}(v) = Ξ_k(v) and
  W_{k+1}(v) = W_k(v)»; (i) SW-IN «Let k → k + 1 be a τ-fixed Even fallback, and v an Even vertex with σ_{k+1}(v) ≠ σ_k(v) that is its own
  Ξ-cycle node neither at k nor at k + 1. Then Ξ_{k+1}(v) ▷ Ξ_k(v); hence v ∈ Z_k»; (k) REOPEN-W «Let k → k + 1 be an in-phase S4a
  transition. If v ∉ Z_k and v ∈ Z_{k+1}, then W_{k+1}(v) ▷ W_k(v)»; (m) Theorem GAP-RED «f_P ≤ |Z_a| + RO_P + ZF_P ≤ n + Σ_v
  WCH^S4a_P(v) + ZF_P» (a := P's first state).
- Landed lemmas of RESULTS R90 used in §5.1 (quoted from R90's entry): (a) (ii) OPT-OFF «At an S4a step t → t + 1, put τ* := τ_t … for every
  Even v that is off-cycle for τ* at t + 1 and every (v, y) ∈ H_t: W^{τ*}_{t+1}(y) ⊴ W^{τ*}_{t+1}(σ_{t+1} v)»; (b) W-MON′ «At an S4a step
  t → t + 1 with τ* := τ_t: W^{τ*}_{t+1} ⊵ W^{τ*}_t pointwise»; (c) W-SUCC «Let [q, p] be states of one τ*-piece, v Even and off-cycle for
  τ* at every state of [q + 1, p]. Then W^{τ*}_t(σ_t v) is non-decreasing on [q, p]»; (d) W-RETURN-G «Let R be a λ-run, (v, c) an Even
  edge, s → s + 1 a leave of c and j − 1 → j the next re-entry, and suppose j − 1 → j is an S4a step. Put τ* := τ_{j−1}, [a, b] the
  τ*-piece containing j − 1, W* := W^{τ*}. An ANCHOR is a state q with max(s, a) ≤ q − 1 ≤ j − 2 and (v, c) ∈ H_{q−1}. If an anchor q
  exists, v is off-cycle for τ* at every state of [q, j], and W*_t(c) is the same for all t ∈ [q, j], then W*_j(σ_{j−1} v) = W*_j(c).»
- RESULTS R56 (Theorem FB-RED): «in-phase fallbacks per phase are at most 1 + (n − 1)(2 + ρ), ρ := the Ξ-changes at Odd choice vertices in
  the phase». ρ_P := that ρ for the phase P.
- Packet definitions (all for N5).
  - TIE EVENT: a pair (v, t), t → t + 1 an S4a step with τ_{t+1} = τ_t, v Even switched at t, and W_{t+1}(v) = W_t(v). For a run stretch X
    (a W-run, a phase): TIE_X := the TIE events with t, t + 1 ∈ X; TIE_X(v) those at v. TIE* := max over W-runs F of TIE_F.
  - For a W-run F, Even v and successor e: a RETURN of v to e at u: u → u + 1 a transition of F, σ_{u+1}(v) = e ≠ σ_u(v), and σ_r(v) = e
    for some state r ∈ F, r ≤ u. Its LEAVE: the largest k < u with σ_k(v) = e ≠ σ_{k+1}(v) (it exists and k ≥ r ≥ first state of F, since
    σ_r(v) = e ≠ σ_u(v)). RET_F(v, e) := the returns of v to e in F. WCH_F(e) := the transitions s → s + 1 of F with W_{s+1}(e) ≠ W_s(e).
    TT_F(v, e) := the transitions k of F at which v leaves e (σ_k(v) = e ≠ σ_{k+1}(v)) with W_{k+1}(v) = W_k(v).
  - GXC EVENT (box 70): a pair (v, t) with v Even switched at t, τ_{t+1} = τ_t, λ_Ξ the same at t and t + 1, v ∈ Z_t, Ξ_{t+1}(v) ▷ Ξ_t(v),
    and W_{t+1}(v) ⊴ W_t(v). Both states then lie in one phase. GXC_P (GXC_R) := the GXC events with t, t + 1 in the phase P (λ-run R).
  - CL_P := the GXC events (v, t) of P at in-phase fallbacks with v ∉ Z_{t+1}; FBO_P := those with v ∈ Z_{t+1}.
  - NC_R := the class-S re-entries j − 1 → j of λ-run R at which the re-entering v is its own Ξ-cycle node at j − 1 or at j; NT_R := the
    class-S re-entries of R with τ_j ≠ τ_{j−1}.
  - GAP LEVEL: for v ∈ Z_t, LEV_t(v) ∈ {1, …, n + 2} := the position of the first coordinate at which CS(Ξ_t(v)) and CS(W_t(v)) differ
    (CS from Fact LEX; position 1 = the cycle coordinate).
  - DROP_P(v) := the transitions k → k + 1 of the phase P that are not S4a steps changing W(v), with v ∈ Z_k ∩ Z_{k+1} and
    LEV_{k+1}(v) > LEV_k(v).
  - FBOS_P := the FBO events (v, t) of P with LEV_{t+1}(v) = LEV_t(v).
  - NZ_P := the Z-flat in-phase fallbacks of P all of whose switched Even vertices are their own Ξ-cycle node at k or at k + 1 (box 70);
    ZFS_P := the other Z-flat in-phase fallbacks k → k + 1 of P at which every switched Even v that is its own Ξ-cycle node neither at k
    nor at k + 1 has LEV_{k+1}(v) = LEV_k(v).
  - WCH_S(e), for a τ-stretch S: the S4a steps t → t + 1 with t, t + 1 ∈ S and W_{t+1}(e) ≠ W_t(e).
  - PREMISE [P-WCHτ](w), for a function w : ℕ → ℕ: on every game with n vertices, in every N5 run, every τ-stretch S and vertex e have
    WCH_S(e) ≤ w(n). (A premise; not proved here. TASK 2's target.)

## 2. Facts
### 2.1 Fact REW and Fact LEX (game-general)
- REW. rew is injective (p′ is). (R1) If u is even (Ω) and more relevant than x, then rew(u) > rew(x). (R2) If x is odd, every u less relevant
  than x has rew(u) > rew(x). Proof: (R1) rew(u) = p′(u) > p′(x) ≥ rew(x). (R2) rew(x) = −p′(x) < −p′(u) ≤ rew(u). □
- LEX. For a value x = (c, P, ℓ) put CS(x) := (rew(c); s_{n−1}, …, s_0; ℓ̂), where s_r := 0 if the vertex u_r of rank r is not in P,
  s_r := +1 if u_r ∈ P and Ω(u_r) is even, s_r := −1 if u_r ∈ P and Ω(u_r) is odd, and ℓ̂ := ℓ if Ω(c) is odd, −ℓ if Ω(c) is even. Then
  x ◁ y iff CS(x) < CS(y) lexicographically. Proof: equal first coordinates mean equal c (REW). For equal c, the signed weights are
  Σ_r s_r 2^r; at the top rank R where the s differ, |s_R − s′_R| = 1 (u_R has one parity) and |Σ_{r<R} (s_r − s′_r) 2^r| ≤ 2^R − 1, so
  the top differing s decides; that is lexicographic. For equal (c, P), ℓ̂ orders ℓ as [S1-ord] does. □
  Consequence (COMMON PREFIX): if x ⊴ z ⊴ y and CS(x), CS(y) agree on their first L coordinates, so does CS(z) with both.
  CS has n + 2 coordinates, so LEV takes values in {1, …, n + 2}.

## 3. Lemma TIE (N5; any pointwise optimum)
Setting. t → t + 1 an S4a step; τ := τ_t; H := H_t; W := W^τ_t = W_t; σ⁺ any POINTWISE-OPTIMAL Even strategy of H against τ (for N5,
σ⁺ = σ_{t+1}, by the standing premise); W′ := val(σ⁺, τ). Let v be Even with d := σ_t(v) ≠ σ⁺(v) and W′(v) = W(v). Then:
- (a) if v is not its own W′-cycle node: v ⊕ W′(d) = W′(v), and d's σ⁺-path to its cycle node avoids v;
- (b) if v is its own W′-cycle node: W′(d) has cycle node v and empty path set.
By [F1], W′ ⊵ val_ρ pointwise for every Even strategy ρ of H; σ_t is one, so W′ ⊵ W. ρ := σ⁺[v ↦ d] is a strategy of H (d ∈ A(v)).
Two values with the same cycle node compare by the most relevant vertex of the symmetric difference of their path sets (Fact LEX): the set
that holds it is better iff that vertex is even.
Proof of (a). If v were its own W-cycle node, W(v) = (v, ∅, 0) = W′(v), against (a)'s hypothesis. So by [V1], W(v) = v ⊕ W(d) and d's
σ_t-path avoids v. Let c* be the common cycle node of W(v) = W′(v), hence of W(d). Let π be d's σ⁺-play.
- (a1) π never visits v. Under ρ, v's play is v·π, so val_ρ(v) = v ⊕ W′(d); [F1]: v ⊕ W′(d) ⊴ W′(v) = W(v) = v ⊕ W(d). [V2] with
  W(d) ⊴ W′(d) (both paths avoid v) gives v ⊕ W(d) ⊴ v ⊕ W′(d). So they are equal, and π's path avoids v.
- (a2) v lies on π's cycle. Then v's σ⁺-play is that cycle: its node is c*, P(W′(v)) = ∅, v is less relevant than c*. π's path to c*
  avoids v, so [V2] gives W(v) = v ⊕ W(d) ⊴ v ⊕ W′(d) = (c*, P(W′(d)), ·).
  - If P(W′(d)) = ∅: under ρ, v's play is the cycle v·(π's path)·(c*'s cycle back to v), with top c*; val_ρ(v) = v ⊕ W′(d) ⊴ W′(v) by
    [F1]; equality follows, and π's path to c* avoids v.
  - Otherwise let u be the top of P(W′(d)); it is more relevant than c* and tops ρ's cycle through v. [F1] gives rew(u) < rew(c*), so u
    is odd (R1). Then v ⊕ W′(d) = (c*, P(W′(d)), ·) ◁ (c*, ∅, ·) = W′(v) = W(v), against W(v) ⊴ v ⊕ W′(d).
- (a3) v lies on π's path part: d = x_0, …, x_q = v, q ≥ 1. Then c* ∉ X := {x_0, …, x_q} and W′(d) = (c*, R ∪ P(W′(v)), q + ℓ(W′(v))),
  R := {x_i : i < q, x_i more relevant than c*}; P(W′(v)) = P(W(v)) = P(W(d)) ∪ {v if more relevant than c*}. Let u be the most relevant
  vertex of X. Under ρ, v's play is the cycle X with top u ≠ c*; [F1] gives rew(u) < rew(c*).
  - u more relevant than c*: then u is odd (R1). If u ∉ P(W(d)), the elements of P(W′(d)) not in P(W(d)) have top u, odd, and none is
    missing, so W′(d) ◁ W(d), against [F1]. If u ∈ P(W(d)), then u ≠ v (d's σ_t-path avoids v) and u ∈ P(W′(v)), so u lies on v's σ⁺-path
    to c*; but u = x_i with i < q, so u's σ⁺-play passes v: u and v lie on one σ⁺-cycle, the cycle of v's play, whose most relevant vertex
    is c*, against u more relevant than c*.
  - u less relevant than c*: then R = ∅ and v is less relevant than c*, so W′(d) = (c*, P(W(d)), ℓ(W(d)) + q + 1). If c* is odd, R2 gives
    rew(u) > rew(c*), against [F1]. If c* is even, W′(d) has W(d)'s path set and is longer, so W′(d) ◁ W(d), against [F1].
  So (a3) does not occur. □
Proof of (b). W(v) = W′(v) = (v, ∅, 0), so d lies on v's σ_t-cycle and W(d) = (v, ∅, ·). If π never visits v, val_ρ(v) = v ⊕ W′(d) has
cycle node λ(W′(d)) ≠ v; [F1] gives rew(λ(W′(d))) < rew(v), so W′(d) ◁ W(d), against [F1]. Otherwise π reaches v and stays on v's
σ⁺-cycle, so λ(W′(d)) = v. If P(W′(d)) ≠ ∅, its top u is more relevant than v, and even, since W′(d) ⊵ W(d) = (v, ∅, ·); ρ's cycle
d … v d has top u, so by R1 val_ρ(v) ▷ W′(v), against [F1]. So P(W′(d)) = ∅. □

## 4. W-runs: returns and their payers (N5)
### 4.1 Lemma NEW-BOUND
For every W-run F: |F| ≤ m_E + Σ_{(v, e) ∈ E, v Even} RET_F(v, e).
Proof. Every transition of F is an S4a step with τ kept (no S4c, τ constant; R90 Fact B), so it switches some Even vertex. Call a switch
of v to e at u NEW if σ_r(v) ≠ e for every state r ∈ F with r ≤ u; otherwise it is a return. For each Even edge (v, e) at most one switch
is new (after it, v has held e), and none if e = σ_{a}(v), a := F's first state; so the transitions holding a new switch number at most
m_E. Every other transition holds a return; charge it to one; distinct transitions give distinct (v, transition) pairs. □

### 4.2 Theorem RET-WCH
For every W-run F, Even v and successor e: RET_F(v, e) ≤ WCH_F(e) + TT_F(v, e). More precisely, every return u of v to e whose leave k has
W_{k+1}(v) ≠ W_k(v) has a transition s ∈ [k, u] at which W(e) changes; the others are charged to their leave k, a TT_F(v, e) transition.
Premises: [F1] (S4a's σ_{t+1} is a pointwise optimum of H_t; σ_t and σ_{k+1}[v ↦ e] are strategies of H_t, H_k), [V1], [V2], W-MON (R91 (b))
and λ_W constant on F. Write W := W^{τ_F}, so W_t = W^{τ_F}_t on F.
Proof. Fix a return u with leave k, and suppose W_{k+1}(v) ≠ W_k(v). λ_W is constant on F, so v is its own W-cycle node at every state of F
or at none. If it is, W_t(v) = (v, ∅, 0) at every state of F, against W_{k+1}(v) ≠ W_k(v). So v is never its own W-cycle node on F; let
c := λ(W_t(v)), the same for all t ∈ F.
- Step 1 (tie-leave). Suppose v ⊕ W_{k+1}(e) = W_{k+1}(v). Since σ_k(v) = e, [V1] gives W_k(v) = v ⊕ W_k(e). If W_{k+1}(e) = W_k(e), then
  W_{k+1}(v) = W_k(v), against the assumption. So W(e) changes at s = k.
- Step 2 (otherwise). Now v ⊕ W_{k+1}(e) ≠ W_{k+1}(v). Suppose, for contradiction, that W(e) is the same at every state of [k + 1, u + 1].
  Let π be e's σ_{k+1}-play and ρ := σ_{k+1}[v ↦ e] ∈ H_k (e = σ_k(v)). By [F1] in H_k, val_ρ ⊴ W_{k+1} pointwise.
  - (i) π never visits v. Then val_ρ(v) = v ⊕ W_{k+1}(e) ⊴ W_{k+1}(v), and ≠, so v ⊕ W_{k+1}(e) ◁ W_{k+1}(v).
  - (ii) v lies on π's cycle. Then that cycle's node is c, P(W_{k+1}(v)) = ∅, and v is less relevant than c. If P(W_{k+1}(e)) = ∅, ρ
    closes a cycle with top c and val_ρ(v) = v ⊕ W_{k+1}(e); then ⊴ and ≠ give ◁. Otherwise the top u′ of P(W_{k+1}(e)) is more relevant
    than c and tops ρ's cycle through v; [F1] and R1 force u′ odd; so v ⊕ W_{k+1}(e) = (c, P(W_{k+1}(e)), ·) ◁ (c, ∅, ·) = W_{k+1}(v).
  - (iii) v lies on π's path part: e = x_0, …, x_q = v, q ≥ 1. Then W_{k+1}(e) = (c, R ∪ P(W_{k+1}(v)), ℓ(W_{k+1}(v)) + q), R the x_i
    (i < q) more relevant than c. At u + 1, v is not its own W-cycle node and σ_{u+1}(v) = e, so [V1] gives W_{u+1}(v) = v ⊕ W_{u+1}(e) =
    v ⊕ W_{k+1}(e). If v were more relevant than c, then v ∈ P(W_{k+1}(e)) = P(W_{u+1}(e)), so v lies on e's σ_{u+1}-path before c while
    σ_{u+1}(v) = e: e's σ_{u+1}-play returns to e before reaching c, so its cycle contains v, more relevant than c, against
    λ(W_{u+1}(e)) = c. So v is less relevant than c, and W_{u+1}(v) = (c, R ∪ P(W_{k+1}(v)), ℓ(W_{k+1}(v)) + q + 1). Let u* be the most
    relevant vertex of {x_0, …, x_q}; ρ's v-play is that cycle, with top u*.
    - u* more relevant than c: u* ≠ v, u* ∈ R, and u* is odd ([F1], R1). If u* ∉ P(W_{k+1}(v)), the elements of P(W_{u+1}(v)) not in
      P(W_{k+1}(v)) have top u*, odd, and none is missing, so W_{u+1}(v) ◁ W_{k+1}(v), against W-MON on the S4a steps of [k + 1, u]. If
      u* ∈ P(W_{k+1}(v)), then u* lies on v's σ_{k+1}-path and v on u*'s, so they share a σ_{k+1}-cycle, whose top is c (v's play), against
      u* more relevant than c.
    - u* less relevant than c: R = ∅, so W_{u+1}(v) has W_{k+1}(v)'s path set and is one plus q steps longer. If Ω(c) is even that is ◁,
      against W-MON. If Ω(c) is odd, R2 gives rew(u*) > rew(c), so val_ρ(v) ▷ W_{k+1}(v), against [F1].
    So (iii) does not occur.
  - From (i) / (ii): W_{u+1}(v) = v ⊕ W_{u+1}(e) ([V1]) = v ⊕ W_{k+1}(e) ◁ W_{k+1}(v) ⊴ W_{u+1}(v) (W-MON on each S4a step of [k + 1, u],
    τ fixed): a contradiction. So W(e) changes at some s ∈ [k + 1, u].
- Distinctness. For consecutive returns u₁ < u₂ of (v, e), v holds e at u₁ + 1, so the leave k₂ of u₂ satisfies k₂ ≥ u₁ + 1. The intervals
  [k, u] of distinct returns are disjoint, so the W(e)-changes chosen above are distinct; returns charged to TT use distinct leaves. □

### 4.3 Corollary RUN-WCH and Corollary REP-WCH
For every W-run F:
- (RUN-WCH) |F| ≤ m_E + Σ_e d_E(e)·WCH_F(e) + TIE_F;
- (REP-WCH) REP_F ≤ Σ_e d_E(e)·WCH_F(e) + TIE_F; hence REP* ≤ max_F Σ_e d_E(e)·WCH_F(e) + TIE*.
Proof. Σ_e TT_F(v, e) ≤ TIE_F(v): a TT transition k of (v, e) is a switch of v at an S4a step of F (τ kept) with W(v) unchanged, i.e. a TIE
event (v, k); at one k, v leaves exactly one e. Sum RET-WCH over the Even edges (v, e) and use NEW-BOUND. For REP: a REPEAT late adoption of
(y, z) at u₂ follows an earlier late adoption of (y, z) at u₁ < u₂ in F (R90 (g)), so σ_{u₁+1}(y) = z with u₁ + 1 ∈ F, u₁ + 1 ≤ u₂, and
σ_{u₂}(y) ≠ z (it adopts z): a return of y to z at u₂. Distinct REPEATs are distinct (vertex, transition) pairs, so REP_F ≤ Σ_{(v, e)}
RET_F(v, e). □

## 5. Phases and λ-runs: tie switches, gap closings and gap levels (N5)
### 5.1 Lemma SIL-Z and Corollary SC-GXC
Lemma SIL-Z. Let j − 1 → j be a class-S re-entry of v into c in the λ-run R (R90 (e)), q its smallest anchor, τ* := τ_{j−1}, W* := W^{τ*},
d := σ_{j−1}(v). Then:
- (a) W*_{j−1}(d) = W*_j(d) = W*_j(c) = W*_{j−1}(c), and W*_j(v) = W*_{j−1}(v);
- (b) if v is not its own Ξ-cycle node at j − 1: d ∈ Z_{j−1} and v ∈ Z_{j−1};
- (c) if v is its own Ξ-cycle node neither at j − 1 nor at j: Ξ_j(v) ▷ Ξ_{j−1}(v).
Proof. Class S: j − 1 → j is not an Even S4c fallback, and it changes σ(v), so it is an S4a step (R90 Fact B); an anchor exists; v is
off-cycle for τ* at every state of [q, j] (not class C); W*_t(c) is the same for all t ∈ [q, j] (not class P). Let [a, b] be the τ*-piece
containing j − 1; then a ≤ q − 1 and [q − 1, j − 1] ⊆ [a, b].
- (a) W*_q(c) ⊴ W*_q(σ_q v) (R90 (a) (ii) at the S4a step q − 1 → q: (v, c) ∈ H_{q−1}, v off-cycle at q) ⊴ W*_{j−1}(σ_{j−1} v) (R90 (c)
  W-SUCC on [q, j − 1]) = W*_{j−1}(d) ⊴ W*_j(d) (R90 (b) W-MON′ at j − 1 → j) = W*_j(c) (R90 (d) W-RETURN-G) = W*_q(c) (W*(c) constant on
  [q, j]). The ends are equal, so every link is an equality; and W*_{j−1}(c) = W*_q(c). By [V1] at j − 1 and j (v off-cycle for τ*,
  σ_{j−1}(v) = d, σ_j(v) = c): W*_{j−1}(v) = v ⊕ W*_{j−1}(d) = v ⊕ W*_j(c) = W*_j(v).
- (b) W_{j−1} = W*_{j−1} (τ_{j−1} = τ*). (v, c) ∈ Iσ_{j−1} ([S4a]: c = σ_j(v) ∈ A(v) ∖ {d}), so Ξ_{j−1}(c) ▷ Ξ_{j−1}(d) ([S2]). By XW,
  Ξ_{j−1}(c) ⊴ W*_{j−1}(c) = W*_{j−1}(d). So Ξ_{j−1}(d) ◁ W*_{j−1}(d): d ∈ Z_{j−1}. For v: Ξ_{j−1}(v) = v ⊕ Ξ_{j−1}(d) and W*_{j−1}(v) =
  v ⊕ W*_{j−1}(d), both paths avoid v ([V1]); [V2] strict gives Ξ_{j−1}(v) ◁ W*_{j−1}(v): v ∈ Z_{j−1}.
- (c) Ξ_j(c) ⊵ Ξ_{j−1}(c) ([R15]) ▷ Ξ_{j−1}(d) ([S2]); both values' paths avoid v ([V1] at j for c, at j − 1 for d); [V2]: Ξ_j(v) =
  v ⊕ Ξ_j(c) ▷ v ⊕ Ξ_{j−1}(d) = Ξ_{j−1}(v). □
Corollary SC-GXC. For every λ-run R: SIL_R ≤ GXC_R + NC_R + NT_R, and GXC_R ≤ Σ_{phases P ⊆ R} GXC_P, with at most B_R + 1 phases inside R.
Proof. A class-S re-entry j − 1 → j of v counted neither in NC_R nor in NT_R has τ_j = τ_{j−1} (so W*_j = W_j), λ_Ξ the same at j − 1
and j (both in R), v switched, v ∈ Z_{j−1} (SIL-Z (b)), Ξ_j(v) ▷ Ξ_{j−1}(v) (SIL-Z (c)) and W_j(v) = W_{j−1}(v) (SIL-Z (a)): the GXC event
(v, j − 1). A transition switches v to one target, so distinct re-entries give distinct events. A GXC event of R has τ and λ_Ξ the same at
both states, so both lie in one phase, and a phase meeting R lies inside R (λ_Ξ constant on it). Inside R, consecutive states with equal τ
lie in one phase, so R's phases are cut only by τ-changing transitions, which are boundaries: at most B_R + 1 phases. □

### 5.2 Lemma GXC-CLOSE and Theorem GXC-SPLIT
Lemma GXC-CLOSE. For every phase P with first state a: CL_P ≤ |Z_a| + Σ_x WCH^S4a_P(x).
Proof. Each CL event (v, t) is an EXIT of v from Z (v ∈ Z_t, v ∉ Z_{t+1}) at an in-phase transition; distinct events are distinct (vertex,
transition) exits. For each vertex x, the exits of x in P are at most [x ∈ Z_a] plus the in-phase ENTRIES of x (x ∉ Z_t, x ∈ Z_{t+1}). An
in-phase transition is an S4a step or a τ-fixed Even fallback (R91 §1). There are no entries at the latter (GAP-MON, R91 (h)). An entry of
x at an in-phase S4a transition has W_{t+1}(x) ▷ W_t(x) (REOPEN-W, R91 (k)), a WCH^S4a_P(x) transition. □
Theorem GXC-SPLIT. For every phase P: GXC_P ≤ TIE_P + CL_P + FBO_P ≤ TIE_P + |Z_a| + Σ_x WCH^S4a_P(x) + FBO_P.
Proof. A GXC event (v, t) of P sits at an in-phase transition. If it is an S4a step: W-MON (R91 (b), τ kept) gives W_{t+1}(v) ⊵ W_t(v),
and the GXC condition W_{t+1}(v) ⊴ W_t(v) makes them equal: a TIE event (v, t) of P. Otherwise it is an in-phase fallback, and v ∉ Z_{t+1}
(CL_P) or v ∈ Z_{t+1} (FBO_P). Then GXC-CLOSE. □

### 5.3 Lemma LEVEL-MON and Corollary DROP-PAID
Lemma LEVEL-MON. Let P be a phase, v a vertex, t < t′ states of P with v ∈ Z_t ∩ Z_{t′}, and suppose no transition s → s + 1 with
t ≤ s < t′ is an S4a step changing W(v). Then LEV_{t′}(v) ≥ LEV_t(v).
Proof. Ξ_t(v) ⊴ Ξ_{t′}(v) ([R15]). Each transition of [t, t′] is in-phase: an S4a step not changing W(v), or a τ-fixed Even fallback, at
which W does not rise (FB-W, R91 (c)); so W_{t′}(v) ⊴ W_t(v). With XW: Ξ_t(v) ⊴ Ξ_{t′}(v) ⊴ W_{t′}(v) ⊴ W_t(v). CS(Ξ_t(v)) and CS(W_t(v))
agree on their first LEV_t(v) − 1 coordinates, so (COMMON PREFIX, Fact LEX) do CS(Ξ_{t′}(v)) and CS(W_{t′}(v)). □
Corollary DROP-PAID. For every phase P and vertex v: DROP_P(v) ≤ (n + 1)(1 + WCH^S4a_P(v)).
Proof. The WCH^S4a_P(v) transitions cut the states of P into at most 1 + WCH^S4a_P(v) SEGMENTS (maximal runs of consecutive states of P
with no such transition between them). A DROP transition k → k + 1 is not one of them, so k, k + 1 lie in one segment. On a segment, LEV(v)
read at the states where v ∈ Z is non-decreasing (LEVEL-MON) with values in {1, …, n + 2} (Fact LEX), and each DROP transition of the
segment is a strict increase between two consecutive such states: at most n + 1 per segment. □

### 5.4 Corollaries FBO-R56, FBO-SPLIT, ZF-SPLIT
- FBO-R56. FBO_P ≤ n_E·f_P ≤ n_E·(1 + (n − 1)(2 + ρ_P)). Proof: an FBO event is a (switched Even vertex, in-phase fallback) pair; then R56. □
- FBO-SPLIT. FBO_P ≤ Σ_v DROP_P(v) + FBOS_P. Proof: an FBO event (v, t) has v ∈ Z_t ∩ Z_{t+1} at a fallback (not an S4a step); LEVEL-MON
  (t′ = t + 1) gives LEV_{t+1}(v) ≥ LEV_t(v); if >, t is a DROP_P(v) transition, and (v, t) ↦ t is injective for fixed v; if =, FBOS_P. □
- ZF-SPLIT. ZF_P ≤ NZ_P + Σ_v DROP_P(v) + ZFS_P. Proof: let k → k + 1 be a Z-flat in-phase fallback counted neither in NZ_P nor in ZFS_P.
  Then some switched Even v is its own Ξ-cycle node neither at k nor at k + 1 and has LEV_{k+1}(v) ≠ LEV_k(v). SW-IN (R91 (i)) gives
  v ∈ Z_k, and Z_{k+1} = Z_k gives v ∈ Z_{k+1}; LEVEL-MON gives LEV_{k+1}(v) > LEV_k(v): k is a DROP_P(v) transition. Distinct fallbacks
  are distinct transitions. □

## 6. Theorem WCH-RED (the composition; a REDUCTION) and Corollary WCH-ONE
Theorem WCH-RED (N5, every game, under the standing premise of §1). For every W-run F, phase P (first state a) and λ-run R:
- (W) |F| ≤ m_E + Σ_e d_E(e)·WCH_F(e) + TIE_F and REP_F ≤ Σ_e d_E(e)·WCH_F(e) + TIE_F (§4.3), so REP* ≤ max_F Σ_e d_E(e)·WCH_F(e) + TIE*;
- (G) f_P ≤ n + Σ_v WCH^S4a_P(v) + ZF_P (R91 GAP-RED) and ZF_P ≤ NZ_P + (n + 1)·Σ_v (1 + WCH^S4a_P(v)) + ZFS_P (§5.3, §5.4);
- (X) GXC_P ≤ TIE_P + |Z_a| + Σ_v WCH^S4a_P(v) + FBO_P (§5.2), with FBO_P ≤ n_E(1 + (n − 1)(2 + ρ_P)) and
  FBO_P ≤ (n + 1)·Σ_v (1 + WCH^S4a_P(v)) + FBOS_P (§5.4);
- (S) SIL_R ≤ (B_R + 1)·max_{P ⊆ R} GXC_P + NC_R + NT_R (§5.1).
Corollary WCH-ONE. A W-run lies in one τ-stretch and holds only S4a steps (R90 Fact B), so WCH_F(e) ≤ WCH_S(e) for the τ-stretch S ⊇ F; a
phase lies in one τ-stretch S, so WCH^S4a_P(v) ≤ WCH_S(v). Hence under [P-WCHτ](w), with w := w(n):
- REP* ≤ m_E·w + TIE*, and |F| ≤ m_E·(1 + w) + TIE_F for every W-run F;
- f_P ≤ n(1 + w) + ZF_P and ZF_P ≤ NZ_P + n(n + 1)(1 + w) + ZFS_P for every phase P;
- GXC_P ≤ TIE_P + n(1 + w) + FBO_P and FBO_P ≤ n(n + 1)(1 + w) + FBOS_P.
So, for N5, [P-WCHτ] with w polynomial reduces RESULTS R90's REP* to TIE*, and RESULTS R91's FB-LIN count f_P to NZ_P + ZFS_P; the
S-part of R90's SC* is reduced by (S) and (X) to TIE_P, FBO_P (or ρ_P), NC_R, NT_R and B_R. None of TIE*, NZ, ZFS, FBOS, NC, NT, ρ_P, B*
is bounded here, and [P-WCHτ] is not proved. □

## 7. The VARIANT N5-LZC (labelled; separate object; nothing here transfers to N5)
### 7.1 Definition
N5-LZC is N5 except in S4a. Let σ* be [S4a]'s σ_new (the S1 procedure's optimum of H_t), W* := val(σ*, τ_t). Define σ′ on Even vertices:
- if ℓ(W*(v)) ≥ 1 and v ⊕ W*(σ_t v) = W*(v), then σ′(v) := σ_t(v);
- if W*(v) = (v, ∅, 0), and W*(σ_t v) has cycle node v and empty path set, then σ′(v) := σ_t(v);
- otherwise σ′(v) := σ*(v).
σ_new := σ′ (if Iσ_t = ∅, σ_new := σ_t as in [S4a]). S4b, S4c (evaluated on σ′: «if σ_new = σ and τ_new = τ»), S4d and S5 are unchanged.
For N5-LZC runs, the §1 definitions (W_t, H_t, S4a step, W-run, late adoption, REP_F, TIE event, WCH_F, RET_F, TT_F) are read verbatim on
N5-LZC's states. An S4a step of N5-LZC: a transition with Iσ_t ≠ ∅, not an S4c fallback, σ_{t+1} = σ′ ≠ σ_t.
Premise: the standing SPEC premise for σ* (R57 1E-N3: σ* is the pointwise optimum of H_t).
### 7.2 Lemma LZ-OPT
val(σ′, τ_t) = W*. Hence σ′ is a pointwise optimum of H_t (σ′ ∈ H_t since σ′(v) ∈ {σ_t(v), σ*(v)} ⊆ A(v)).
Proof. Every step of σ′ (and of τ_t at Odd vertices) is W*-CONSISTENT: x ⊕ W*(next) = W*(x) when ℓ(W*(x)) ≥ 1 (for σ*'s and τ_t's steps
this is [V1] for the pair (σ*, τ_t); for kept steps it is the rule), and W*(next) = (x, ∅, ·) when W*(x) = (x, ∅, 0) (for σ*'s and τ_t's
steps: x tops its own (σ*, τ_t)-cycle, whose other vertices are less relevant, so its successor's value is (x, ∅, ·); for kept steps it is
the rule). A consistent step lowers ℓ by exactly 1 and keeps the cycle node, so from any x the (σ′, τ_t)-play reaches c := λ(W*(x)) in
ℓ(W*(x)) steps without repeating a vertex (the only vertex of value (c, ·, 0) is c). From c the next value is (c, ∅, ·) and consistency
gives P(y) = P(y′) ∪ {y if more relevant than c} along the way, so every vertex until c recurs has empty path set and is less relevant than
c: the play from c is a cycle with top c. Along x's path the path set accumulates exactly P(W*(x)). So val(σ′, τ_t)(x) = W*(x). □
### 7.3 Lemma W-MON_LZ and Theorem LZ-STRICT
- W-MON_LZ. At an S4a step t → t + 1 of N5-LZC, W^{τ_t}_{t+1} ⊵ W^{τ_t}_t pointwise. Proof: σ_{t+1} = σ′ is a pointwise optimum of H_t
  (LZ-OPT) and σ_t is a strategy of H_t; [F1]. □
- LZ-STRICT. At an S4a step t → t + 1 of N5-LZC, every switched Even v has W^{τ_t}_{t+1}(v) ▷ W^{τ_t}_t(v). Proof: W-MON_LZ gives ⊵.
  Suppose equality. σ⁺ := σ′ is a pointwise optimum of H_t with W′ = W* (LZ-OPT), so Lemma TIE (§3; its proof uses only that σ⁺ is a
  pointwise optimum of H_t) applies with d = σ_t(v): (a) or (b) holds for W* — exactly the keep-rule's condition. So σ′(v) = σ_t(v), and
  v is not switched. □
- Hence in N5-LZC: TIE_X ≡ 0 and TT_F ≡ 0 (every switch at an S4a step strictly raises W(v), read with τ_t).
### 7.4 Corollary RUN-WCH_LZ and REP-WCH_LZ (no OPT-ONLY)
For every W-run F of N5-LZC: |F| ≤ m_E + Σ_e d_E(e)·WCH_F(e) ≤ m_E·(1 + max_e WCH_F(e)), and REP_F ≤ Σ_e d_E(e)·WCH_F(e).
Proof. §4.1-§4.3 read on N5-LZC: every W-run transition switches some Even vertex (if σ′ = σ_t and τ is kept, S4c fires, which W-runs
exclude); RET-WCH's premises are [F1] in H_k for σ_{k+1} = σ′ (LZ-OPT), [V1], [V2], W-MON_LZ and λ_W constant on F; REP's step uses
only R90 (g)'s definitions. TT_F ≡ 0 and TIE_F ≡ 0 (§7.3). No fleet lemma is transferred: every premise is re-proved for N5-LZC here. □
### 7.5 Corollary LZ-NOSIL (under ASSUMPTION OPT-ONLY)
- ASSUMPTION OPT-ONLY. RESULTS R90 Fact B and (a) (ii), (b), (c) and (d) hold verbatim for N5-LZC runs (Fact B and (b) are also immediate
  from §7.1 and W-MON_LZ). (Their landed proofs, as R90's standing-premise
  disclosure states, use S4a's σ_new as «the pointwise optimum of the one-player arena», which σ′ is by LZ-OPT; that no proof step uses the
  S1 procedure's own tie-break is NOT checked line by line here. Referees: please check.)
- Statement. Under OPT-ONLY, N5-LZC has no class-S re-entry (R90 (e) classes read on N5-LZC).
- Proof. SIL-Z (a) (§5.1) uses only R90 Fact B, (a) (ii), (b), (c), (d) and [V1]; under OPT-ONLY it holds for N5-LZC and gives
  W^{τ*}_j(v) = W^{τ*}_{j−1}(v), τ* = τ_{j−1}, at every class-S re-entry j − 1 → j, an S4a step switching v. LZ-STRICT (read with τ_{j−1},
  whether or not τ changes at j − 1 → j) excludes that. □
- Not claimed: anything about class C, phases, GXC, ZF, fallbacks or T for N5-LZC; LZ-NOSIL is the only §5-type statement made for it.

## 8. NOT to sign
### 8.1 Trimmed from the predecessor's list (Lead's scope rule: they do not compose into this reduction)
- TXC-SRC / TXC-RHO (box 72 §6): they bound tied Ξ-climbs per W-run by TIE + ρ_F + CYC. REP is reached here through returns (§4.3)
  directly, and ρ per W-run is not a landed count; nothing in §6 uses them.
- FIX-DEPTH / FIXD-MON and Theorem PHASE-RED (box 77): a separate reduction of phase length to dead-branch climbs ΣFLAT, premise FLAT, not
  [P-WCHτ]. Proposed as its own packet if the Lead wants it.
- LZ-RUN (box 74): |F| ≤ (n − 1)(R*_T + 1) for N5-LZC needs OPT-ONLY for R89 (h); §7.4 gives a W-run bound for N5-LZC without OPT-ONLY,
  in the packet's own premise.
- N5-LZC output correctness (box 73 §4): true and short, but not part of the reduction. GXC-CLOSE / FBO for N5-LZC: not claimed (they would
  need R91's fallback lemmas for N5-LZC).
- Changes against the working notes (this packet governs): RET-WCH's tie-leave term TL (box 78) is replaced by TT (leaves with W(v)
  unchanged), via Step 1; so the N5 residual is TIE, the same object as GXC's S4a part. DOWN-PAID (box 73) is generalised to DROP-PAID
  (every non-W(v)-changing transition, not only FBO events). ZF-SPLIT is new composition bookkeeping (from SW-IN, LEVEL-MON, DROP-PAID).
### 8.2 DATA (experiments/new/box79/wchpk.py; corpus = box59/sbcg.lst (719) + alt_all (413), N5 and N5-LZC; wchpk_*.txt)
- Table in §8.4 (run 2026-10-30 09:00Z-09:02Z by date -u; summary by experiments/new/box79/sumpk.py).
- Earlier, as in the working notes: RET-WCH (TL form) 12365 returns, 0 unpaid (box 78); TIE (a) in 359 / 359 off-cycle S4a GXC events
  (box 72); LEVEL-MON: no UP in 1132 + 1132 runs (box 73); GXC-CLOSE 0 violations (box 72); SIL-Z / SC-GXC: every S re-entry is a GXC event
  (box 70); N5-LZC S = 0 in 1132 runs (box 72, the DATA behind LZ-NOSIL).
### 8.3 READING
- Every residual of §6 for N5 except NZ, ZFS, FBOS, NC, NT is a TIE count or a per-vertex W-change count; N5-LZC removes TIE outright.
  The one shared premise is [P-WCHτ]: per-vertex S4a W-changes per τ-stretch.
### 8.4 DATA table (from wchpk_*.txt at freeze)
| engine | games | W-runs | returns | paid by a W(e)-change in [k, u] | TT (leave with W(v) unchanged) | UNPAID | per-(F, v, e) violations of RET-WCH | RUN-WCH violations | TIE events in W-runs | max returns per (F, edge) | max |F| / RUN-WCH bound |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| N5 | 1132 | 1692 | 6265 | 6177 | 88 | 0 | 0 | 0 | 397 | 17 | 0.30 |
| N5-LZC | 1132 | 1658 | 6100 | 6100 | 0 | 0 | 0 | 0 | 0 | 17 | 0.30 |
- The return totals equal box 78's (6265 / 6100). TIE = 0 and TT = 0 on N5-LZC everywhere (LZ-STRICT). Pins: tog6b_n32 (red/so) N5 returns 4,
  paid-W 3, TT 1, TIE 2; N5-LZC returns 3, paid-W 3, TIE 0.
### 8.5 Strict symbol test of the line file (experiments/new/box79/symtest.py; run at freeze; output experiments/new/box79/symtest.out)
- Method: every token of docs/new/P-N5-WCH-box79-line.txt that holds a Greek letter, ℓ, a math operator, a subscript / superscript / prime /
  star / brace, or is an all-caps, mixed-case or single-letter identifier is extracted (item labels (a)-(m) of cited RESULTS entries and
  possessive 's removed). Each must be listed in the test's BIND table, and its binding phrase must occur verbatim in the line (in-line
  binding: either a definition in the line or the line's citation of the landed RESULTS item that defines it). An unlisted token, or a
  listed token whose phrase is absent, FAILS. Words (Lemma, Theorem, …, =, :=) are listed as words.
- Result: 182 symbols, 0 failures, SYMTEST PASS (pinned in experiments/new/check.sh, "box 79").
| symbol | uses | status | binding (verbatim phrase in the line) |
| --- | --- | --- | --- |
| 1E-N3 | 1 | OK | in: 1E-N3: S1's procedure realises the pointwise optimum |
| < | 1 | OK | in: t < t′ |
| > | 1 | OK | in: > |
| ASSUMPTION | 1 | OK | in: ASSUMPTION OPT-ONLY |
| B | 1 | OK | in: R90 Fact B |
| B_R | 3 | OK | in: B_R (the boundaries inside the λ-run R) |
| Corollaries | 3 | OK | word:  |
| Corollary | 3 | OK | word:  |
| DROP-PAID | 1 | OK | in: Corollaries DROP-PAID |
| DROP_P | 3 | OK | in: number at most (n + 1)(1 + WCH^S4a_P(v)) (DROP_P(v)) |
| EVERY | 1 | OK | in: on EVERY game |
| Even | 14 | OK | in: Even vertices |
| F | 9 | OK | in: for a W-run F, \|F\| |
| F1 | 1 | OK | in: R17 (a) (F1) |
| FBO | 1 | OK | in: FBO_P the GXC events of P at in-phase fallbacks |
| FBO-R56 | 1 | OK | in: FBO-R56 |
| FBO-SPLIT | 1 | OK | in: FBO-SPLIT |
| FBOS_P | 4 | OK | in: FBOS_P the FBO events of P with LEV_{t+1}(v) = LEV_t(v) |
| FBO_P | 6 | OK | in: FBO_P the GXC events of P at in-phase fallbacks with v ∈ Z_{t+1} |
| Fact | 1 | OK | in: R90 Fact B |
| G-N5-TIME | 1 | OK | in: G-N5-TIME stays open |
| GXC | 3 | OK | in: a GXC event is a pair (v, t) |
| GXC-CLOSE | 1 | OK | in: (Lemma GXC-CLOSE |
| GXC-SPLIT | 1 | OK | in: Theorem GXC-SPLIT) |
| GXC_P | 3 | OK | in: GXC_X the GXC events with t, t + 1 in X |
| GXC_R | 1 | OK | in: GXC_X the GXC events with t, t + 1 in X |
| GXC_X | 1 | OK | in: GXC_X the GXC events with t, t + 1 in X |
| H_t | 3 | OK | in: H_t := S4a's arena at t |
| Iσ_t | 2 | OK | in: Iσ_t the improving edges of σ_t (SPEC S2) |
| LEV | 1 | OK | in: with LEV_t(v), for v ∈ Z_t |
| LEVEL-MON | 1 | OK | in: (Lemma LEVEL-MON |
| LEV_k | 1 | OK | in: LEV_{k+1}(v) > LEV_k(v) |
| LEV_t | 3 | OK | in: with LEV_t(v), for v ∈ Z_t, the position of the first coordinate at which Ξ_t(v) and W |
| LEV_{k+1} | 1 | OK | in: LEV_{k+1}(v) > LEV_k(v) |
| LEV_{t+1} | 1 | OK | in: LEV_{t+1}(v) = LEV_t(v) |
| LEV_{t′} | 1 | OK | in: LEV_{t′}(v) ≥ LEV_t(v) for states t < t′ of a phase P |
| LZ-NOSIL | 1 | OK | in: (Corollary LZ-NOSIL, under ASSUMPTION OPT-ONLY |
| LZ-OPT | 1 | OK | in: (Lemma LZ-OPT |
| LZ-STRICT | 1 | OK | in: Theorem LZ-STRICT |
| Lemma | 7 | OK | word:  |
| M3 | 1 | OK | in: not M3 |
| N5 | 3 | OK | in: N5 on EVERY game (SPEC S1-S5 |
| N5-LZC | 4 | OK | in: for the labelled VARIANT N5-LZC (N5 with S4a's output σ* replaced by σ′ |
| NC_R | 4 | OK | in: NC_R (NT_R) the class-S re-entries j − 1 → j of R |
| NEW-BOUND | 1 | OK | in: (Lemma NEW-BOUND |
| NT_R | 4 | OK | in: NC_R (NT_R) the class-S re-entries j − 1 → j of R |
| NZ_P | 4 | OK | in: NZ_P the Z-flat in-phase fallbacks of P all of whose switched Even vertices |
| OPT-ONLY | 1 | OK | in: ASSUMPTION OPT-ONLY that RESULTS R90 Fact B and (a) (ii), (b), (c), (d) hold verbatim  |
| Odd | 1 | OK | in: Odd follows τ_t |
| P | 13 | OK | in: of the phase P |
| Q | 4 | OK | in: path set Q, |
| R | 4 | OK | in: the λ-run R |
| R15 | 1 | OK | in: R15 (a), (d) |
| R17 | 1 | OK | in: R17 (a) (F1) |
| R38 | 1 | OK | in: RESULTS R38 (a) |
| R56 | 2 | OK | in: R56 |
| R57 | 1 | OK | in: RESULTS R57 |
| R86 | 2 | OK | in: R86 |
| R88 | 2 | OK | in: R88 (f) |
| R89 | 2 | OK | in: R89 |
| R90 | 4 | OK | in: R90 (a)-(e), (g) |
| R91 | 2 | OK | in: R91 (a)-(c), (h), (i), (k), (m) |
| REDUCTION | 1 | OK | in: a REDUCTION |
| REP* | 2 | OK | in: REP* := max_F REP_F |
| REP-WCH | 1 | OK | in: Corollaries RUN-WCH and REP-WCH |
| REP-WCH_LZ | 1 | OK | in: Corollaries RUN-WCH_LZ, REP-WCH_LZ) |
| REPEATs | 1 | OK | in: REPEATs, REP_F and REP* |
| REP_F | 4 | OK | in: REP_F and REP* := max_F REP_F |
| RESULTS | 10 | OK | in: RESULTS R57 |
| RET-WCH | 1 | OK | in: (Theorem RET-WCH) |
| RUN-WCH | 1 | OK | in: Corollaries RUN-WCH and REP-WCH |
| RUN-WCH_LZ | 1 | OK | in: Corollaries RUN-WCH_LZ, REP-WCH_LZ) |
| S | 2 | OK | in: every τ-stretch S |
| S1 | 4 | OK | in: SPEC S1 |
| S1-S5 | 1 | OK | in: SPEC S1-S5 |
| S2 | 1 | OK | in: (SPEC S2) |
| S4a | 11 | OK | in: SPEC S1-S5 |
| S4c | 1 | OK | in: SPEC S1-S5 |
| SC-GXC | 1 | OK | in: Corollary SC-GXC) |
| SIL-Z | 1 | OK | in: (Lemma SIL-Z |
| SIL_R | 2 | OK | in: class-S re-entries and SIL_R as in RESULTS R90 (e) |
| SPEC | 6 | OK | in: SPEC S1-S5 |
| TARGET.md | 1 | OK | in: not a TARGET.md claim |
| TIE | 2 | OK | in: (Lemma TIE) at an S4a step |
| TIE* | 3 | OK | in: TIE* := max_F TIE_F |
| TIE_F | 6 | OK | in: TIE_F the pairs (v, t), t → t + 1 a transition of F and v switched at t with W_{t+1}(v |
| TIE_P | 3 | OK | in: TIE_P the pairs (v, t) with t → t + 1 an in-phase S4a transition of P |
| TT_F | 3 | OK | in: TT_F(v, e) the transitions k → k + 1 of F at which v leaves e |
| Theorem | 4 | OK | word:  |
| VARIANT | 1 | OK | in: labelled VARIANT |
| W | 6 | OK | in: W(v) := W_t(v) at the state in question |
| W* | 2 | OK | in: W*, the [S1-val] valuation of the (σ*, τ_t)-plays |
| W-run | 5 | OK | in: a W-run and, for a W-run F |
| WCH-ONE | 1 | OK | in: Corollary WCH-ONE) |
| WCH-RED | 1 | OK | in: (Theorem WCH-RED |
| WCH^S4a_P | 3 | OK | in: f_P, ZF_P and WCH^S4a_P(v) as in RESULTS R91 |
| WCH_F | 6 | OK | in: WCH_F(e) the transitions of F at which W(e) changes |
| W_k | 1 | OK | in: with W_{k+1}(v) = W_k(v) |
| W_t | 9 | OK | in: W_t := the [S1-val] valuation of the (σ_t, τ_t)-plays |
| W_{k+1} | 1 | OK | in: with W_{k+1}(v) = W_k(v) |
| W_{t+1} | 3 | OK | in: W_{t+1}(v) = W_t(v) |
| W′ | 6 | OK | in: W′ the [S1-val] valuation of the (σ⁺, τ_t)-plays |
| W′-cycle | 1 | OK | in: for a valuation Ω (Ξ_t, W_t, or W′ below) |
| X | 1 | OK | in: with t, t + 1 in X |
| Z-flat | 2 | OK | in: those k → k + 1 with Z_{k+1} = Z_k |
| ZF-SPLIT | 1 | OK | in: ZF-SPLIT) |
| ZFS_P | 4 | OK | in: ZFS_P the other Z-flat in-phase fallbacks of P |
| ZF_P | 4 | OK | in: f_P, ZF_P and WCH^S4a_P(v) as in RESULTS R91 |
| Z_k | 2 | OK | in: those k → k + 1 with Z_{k+1} = Z_k |
| Z_t | 4 | OK | in: Z_t := {v : Ξ_t(v) ≠ W_t(v)} the gap set |
| Z_{k+1} | 2 | OK | in: those k → k + 1 with Z_{k+1} = Z_k |
| Z_{t+1} | 1 | OK | in: with v ∈ Z_{t+1} |
| Z_{t′} | 1 | OK | in: v ∈ Z_t ∩ Z_{t′} |
| [P-WCHτ] | 2 | OK | in: (premise [P-WCHτ](w), not proved here) |
| [S1-val] | 3 | OK | in: SPEC S1 |
| a | 17 | OK | in: with first state a |
| c | 5 | OK | in: cycle node c, |
| class-S | 3 | OK | in: class-S re-entries and SIL_R as in RESULTS R90 (e) |
| d | 1 | OK | in: d := σ_t(v) |
| d_E | 5 | OK | in: d_E(e) the number of Even vertices with an edge to the vertex e |
| e | 10 | OK | in: for every Even v and successor e |
| f_P | 2 | OK | in: f_P, ZF_P and WCH^S4a_P(v) as in RESULTS R91 |
| j | 4 | OK | in: re-entries j − 1 → j of R |
| k | 8 | OK | in: those k → k + 1 |
| m_E | 5 | OK | in: m_E the number of edges leaving Even vertices |
| max_F | 2 | OK | in: REP* := max_F REP_F |
| max_P | 1 | OK | in: max_P GXC_P + NC_R + NT_R (P over the phases inside R) |
| n | 18 | OK | in: n the number of vertices of the game |
| n_E | 2 | OK | in: n_E the number of its Even vertices |
| r | 2 | OK | in: for each rank r from n − 1 down to 0 |
| t | 23 | OK | in: a transition is written t → t + 1 |
| t′ | 1 | OK | in: for states t < t′ of a phase P |
| u | 2 | OK | in: transitions u → u + 1 of F |
| v | 72 | OK | in: v is switched at t |
| w | 8 | OK | in: at most w(n) S4a steps inside S changing W(e) |
| x | 3 | OK | in: x ⊕ (c, Q, ℓ) := |
| \|F\| | 4 | OK | in: \|F\| (its transitions) |
| \|Z_a\| | 1 | OK | in: every phase P with first state a |
| · | 6 | OK | in: d_E(e)·WCH_F(e) |
| Ξ-cycle | 3 | OK | in: v is its own Ω-cycle node if the cycle node of Ω(v) is v |
| Ξ_t | 5 | OK | in: Ξ_t := Ξ_{σ_t} (SPEC S1) |
| Ξ_{t+1} | 1 | OK | in: Ξ_{t+1}(v) ▷ Ξ_t(v) |
| Ξ_{σ_t} | 1 | OK | in: Ξ_t := Ξ_{σ_t} (SPEC S1) |
| Σ_e | 4 | OK | in: Σ_e d_E(e)·WCH_F(e) |
| Σ_v | 3 | OK | in: Σ_v WCH^S4a_P(v) |
| Ω | 2 | OK | in: for a valuation Ω |
| Ω-cycle | 1 | OK | in: v is its own Ω-cycle node if the cycle node of Ω(v) is v |
| λ-run | 3 | OK | in: a λ-run as in RESULTS R86 |
| λ_W | 1 | OK | in: λ_W its cycle-node map |
| λ_Ξ | 2 | OK | in: λ_Ξ its cycle-node map |
| ρ | 1 | OK | in: RESULTS R56's ρ |
| ρ_P | 3 | OK | in: ρ_P := RESULTS R56's ρ of the phase P |
| σ* | 3 | OK | in: S4a's output σ* |
| σ_k | 1 | OK | in: (σ_k(v) = e ≠ σ_{k+1}(v)) |
| σ_new | 1 | OK | in: σ_new is the pointwise optimum of the one-player arena H_t |
| σ_t | 7 | OK | in: the sequence of states (σ_t, τ_t) |
| σ_u | 1 | OK | in: σ_{u+1}(v) = e ≠ σ_u(v) |
| σ_{k+1} | 1 | OK | in: (σ_k(v) = e ≠ σ_{k+1}(v)) |
| σ_{t+1} | 1 | OK | in: v is switched at t if σ_{t+1}(v) ≠ σ_t(v) |
| σ_{u+1} | 1 | OK | in: σ_{u+1}(v) = e ≠ σ_u(v) |
| σ′ | 2 | OK | in: replaced by σ′, which keeps σ_t(v) |
| σ⁺ | 3 | OK | in: for any pointwise-optimal Even strategy σ⁺ of H_t |
| τ-stretch | 3 | OK | in: a τ-stretch, a W-run and, for a W-run F, \|F\| (its transitions) as in RESULTS R89 |
| τ_j | 1 | OK | in: τ_j ≠ τ_{j−1} |
| τ_t | 8 | OK | in: the sequence of states (σ_t, τ_t) |
| τ_{j−1} | 1 | OK | in: τ_j ≠ τ_{j−1} |
| τ_{t+1} | 1 | OK | in: τ_{t+1} = τ_t |
| ℓ | 4 | OK | in: length ℓ) |
| → | 9 | OK | in: a transition is written t → t + 1 |
| ∈ | 5 | OK | in: ∈ |
| − | 4 | OK | in: − |
| −1 | 1 | OK | in: +1, −1 or 0 |
| ∩ | 2 | OK | in: Z_t ∩ Z_{t′} |
| ∪ | 2 | OK | in: Q ∪ {x if |
| ≠ | 6 | OK | in: ≠ |
| ≤ | 16 | OK | in: ≤ |
| ≥ | 1 | OK | in: ≥ |
| ⊕ | 2 | OK | in: the prefix operation x ⊕ (c, Q, ℓ) := (c, Q ∪ {x if x is more relevant than c}, ℓ + 1) |
| ⊴ | 2 | OK | in: ⊴, ◁, ⊵, ▷ the SPEC S1 order |
| ⊵ | 1 | OK | in: ⊴, ◁, ⊵, ▷ the SPEC S1 order |
| ▷ | 2 | OK | in: ⊴, ◁, ⊵, ▷ the SPEC S1 order |
| ◁ | 1 | OK | in: ⊴, ◁, ⊵, ▷ the SPEC S1 order |
