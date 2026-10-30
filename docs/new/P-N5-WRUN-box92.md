# P-N5-WRUN (packet, box 92): the within-W-run reduction chain. Headline (a composition of landed RESULTS R86 SW-RETURN with R15 (d)): every W-run F has |F| ≤ m_E + Σ_c d_E(c)·ΞCH_F(c), so polynomial W-runs ⇔ polynomially many Ξ-changes per vertex per W-run (XI-CH-POLY); with it, ten named residuals are proved EQUIVALENT forms of one open statement, and BIP-REL-1, NO-DEV and LEVEL-RED are one-way
L-NEW successor 39 (Opus 5.5), D14 / D18, Lead reading L40. Lead 2026-10-30 (brief to successor 39, after 15:58Z): «(B) MAIN BOX 92: freeze
P-N5-WRUN, the within-W-run reduction chain, as a packet for the referees, following your predecessor's outline. … Bind every symbol (strict
symbol test). State exactly which claims are equivalences ("⇔ polynomial W-runs") and which are one-way implications. Mark every CONJECTURE
(BIP-REL-1, INT-LIN, XI-CH-POLY, …) as not to sign.» FROZEN 2026-10-30 (this commit; sha1 reported to the Lead). Written 16:06Z-16:09Z (date -u).
Sources (working notes, unrefereed; THIS packet governs where they differ; none is cited as a proof): docs/new/N5-WAIT-box84.md,
N5-FREE-box85.md, N5-RSTAR-box86.md, N5-ARV-box87.md, N5-ONEP-box88.md, N5-BIP-box89.md, N5-REL-box90.md (L-NEW successor 38, l-new
246f1687 … 83021322); outline notes/L-NEW.md (successor 38 FINAL, l-new 5027c17c). Other lanes, quoted verbatim in §2 with their SHAs.
Status: REDUCTIONS and EQUIVALENCES only. No residual is bounded here. G-N5-TIME stays OPEN. Not M3, not a step-4 pass, not a TARGET.md
claim. Object: N5 only (SPEC S1-S5). Nothing is claimed for N5-LZC, N5-SF or any other variant.

## 0. What to sign
| § | item | origin | label |
| --- | --- | --- | --- |
| 3 | Theorem XI-RUN and Corollary WRUN-EQ (the equivalence table, §3.3) | L-NEW, new in this packet (composition of landed lemmas) | PROVED (to sign) |
| 4 | Lemma WAIT-CYCLE′, Corollaries DEAD-CYCLE and CHARGE, Lemma E0-BOUND, Theorem TRIPLE-RED | L-NEW box 84 | PROVED (to sign) |
| 5 | Lemma RET-ΞRISE (landed R86 SW-RETURN's chain in return form; covers L-SI's RETURN-CHARGE), Theorem FREE-RED | L-NEW box 85 | PROVED (to sign; short, see §5.1) |
| 6 | Lemma GAP-DEV, Lemma ΞCH-PCH, Theorem RSTAR-PCH | L-NEW box 86 | PROVED (to sign) |
| 7 | Lemmas LEX-SIGN, PREFIX-MON, Theorem LEVEL-RED | L-NEW box 87 | PROVED (to sign) |
| 8 | Definition BIP(ρ, τ), Lemma BIP-MON, Lemma NO-DEV (CORRECTED here, §8.3) | L-NEW box 88 | PROVED (to sign) |
| 9 | Theorem BIP-RED under premise [SUB] | L-NEW box 89 | PROVED (to sign) as an implication from [SUB] |
| 9.1 | [SUB] (FW-R* on every sub-interval of a W-run) | REFEREE-2 successor 22, one referee's check | to sign by the referee who has not checked it; if signed, BIP-RED is unconditional |
| 10 | Lemma REL2-WRISE (under (A1), (A2)) | L-NEW box 90 | PROVED (to sign); used by no reduction |
| 11 | Corollary INT-XCH⁰ (L-SI's INT-XCH with RX_I = 0) | L-NEW, new (XI-RUN on a W-constant interval) | PROVED (to sign) |
| 2 | ARENA-MAX (L-RED), INTERVAL-SI / TIGHT-VALUE / FL-INT, RETURN-CHARGE / INT-XCH (L-SI) | other lanes, quoted | premises as stated by their lanes; to sign only if the Lead routes them (see §2) |
| 12 | CONJECTURES | — | NOT to sign |
| 13 | DATA, DEAD, READING | — | NOT to sign |

## 1. Setting and landed premises (quoted from docs/RESULTS.md)
- N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md; FIX 1-4 as in RESULTS); any parity game, V = {0, …, n − 1}, n := |V|, n_E := the number of
  Even vertices, m_E := the number of edges leaving Even vertices, d_E(c) := the number of Even vertices with an edge to c. A run is the
  sequence of states (σ_t, τ_t) from any start pair; a TRANSITION is t → t + 1 (states t, t + 1). v is SWITCHED at t if σ_{t+1}(v) ≠ σ_t(v);
  then σ_{t+1}(v) is ADOPTED (v ENTERS σ_{t+1}(v)) and v LEAVES σ_t(v).
- Ξ_t := Ξ_{σ_t} (SPEC S1: the [S1-val] valuation of the (σ_t, σ̄_t)-plays, σ̄_t Odd's pointwise-optimal counterstrategy to σ_t); a value is
  x = (c, P, ℓ) (cycle node λ(x) = c, path set P(x) = P, length ℓ(x) = ℓ ∈ [0, n − 1]); λ_Ξ the cycle-node map of Ξ_t. ⊴, ◁, ⊵, ▷: the SPEC
  S1 order (better for Even) and its strict and reverse forms. Iσ_t := Even's improving edges (SPEC S2: (y, z) with Ξ_t(z) ▷ Ξ_t(σ_t y)).
- W_t := the [S1-val] valuation of the (σ_t, τ_t)-plays; λ_W its cycle-node map; val(ρ, τ) the [S1-val] valuation of the (ρ, τ)-plays for any
  positional Even ρ and Odd τ. H_t := S4a's arena at t (Even v keeps {σ_t(v)} ∪ Iσ_t(v), Odd follows τ_t).
- [R57] standing SPEC premise (RESULTS R57, as quoted in RESULTS R91 / R93): «1E-N3: S1's procedure realises the pointwise optimum; for S4a,
  σ_new is the pointwise optimum of the one-player arena H_t». Every item below that uses S4a's step uses this premise, as R88-R93 do.
- [R15] RESULTS R15 (a): «Lemma A: for any non-empty unambiguous set I of improvements of σ (VJ00 §4.4), Ωσ ⊴ Ω_{Switch_I(σ)}». (b):
  «Lemma B: if moreover Ω_{Switch_I(σ)} = Ωσ, then every (v, w) ∈ I is a length-only switch at a cycle node». (d): «N5: every iteration applies
  Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ (on G) and/or with ∅ ≠ I ⊆ Iτ to Odd's τ (on G^d), and changes at least one of them … at most
  4n(n−1) consecutive N5 iterations leave both Ωσ and Ωτ unchanged». Hence Ξ_{t+1} ⊵ Ξ_t pointwise at every transition (MON).
- [R89] RESULTS R89: «a τ-stretch := a maximal run of consecutive states with τ constant; a W-run := a maximal run of consecutive states of
  one τ-stretch none of whose transitions is an S4c fallback or changes λ_W»; «(Lemma SUCC-MON) Ξ_t(σ_t(y)) is non-decreasing in t for
  every Even y»; «(Lemma LATE-RISE) (y, z) ∉ Iσ_t, (y, z) ∈ Iσ_u, t < u imply Ξ_u(z) ▷ Ξ_t(z)»; «(Lemma GP*-RUN) RESULTS R88's Lemma GP*
  and Corollary FW-R* hold on every W-run (σ̄ and λ_Ξ need not be constant there), and (Corollary R*-RISE) in a W-run F the late
  adoptions of each Even edge (y, z) are at most the transitions of F at which Ξ(z) changes». For a W-run F = [a, b], |F| := b − a.
- [R88] RESULTS R88: BLOCKED edge at state q := «W-better than σ's choice at r_i but not a VJ00-improving edge of Ξ», i.e. W_q(z) ▷
  W_q(σ_q y) and (y, z) ∉ Iσ_q; «(Corollary FW-R*) F has at most (n−1)(R*_T+1) W-changing transitions, R*_T := the transitions of F at
  which some Even vertex adopts an edge blocked at an earlier state of F». A LATE ADOPTION is such an adoption. Below R*_F := R*_T read on
  the W-run F (by [R89] GP*-RUN).
- [R86] RESULTS R86 (a), Lemma SW-RETURN, verbatim: «For every run of states R of an N5 run, every Even v and every vertex c: ENT_R(v, c)
  ≤ 1 + RISE_R(c).» with «ENT_R(v, c) the transitions of R at which v's strategy enters c, SW_R(v) := Σ_c ENT_R(v, c) the switches of v,
  RISE_R(c) the transitions of R at which Ξ(c) changes»; REFEREE's cell: «No phase, no λ, no τ used: it holds on ANY stretch of
  consecutive states, fallbacks included.»
- [R91] RESULTS R91, Lemmas XW and W-MON, W-SUCC: «Ξ_t ⊴ W_t pointwise, W does not fall at an S4a step (read with τ_t)»; «W_t(σ_t(v)) is
  non-decreasing on an interval [p, q] of a piece on which v is not its own W-cycle node at any state of [p + 1, q]».
- [R93] RESULTS R93 Fact LEX (P-N5-WCH §2.1): «For a value x = (c, P, ℓ) put CS(x) := (rew(c); s_{n−1}, …, s_0; ℓ̂), where s_r := 0 if the
  vertex u_r of rank r is not in P, s_r := +1 if u_r ∈ P and Ω(u_r) is even, s_r := −1 if u_r ∈ P and Ω(u_r) is odd, and ℓ̂ := ℓ if Ω(c)
  is odd, −ℓ if Ω(c) is even. Then x ◁ y iff CS(x) < CS(y) lexicographically.» RESULTS R93 Lemma NEW-BOUND: «|F| ≤ m_E + Σ_e d_E(e)·WCH_F(e)
  + TIE_F», TIE_F «the pairs (v, t), t → t + 1 a transition of F and v switched at t with W_{t+1}(v) = W_t(v)».
- Fact STEP-SW (from [R15] (d), used throughout). Every transition of a W-run F switches at least one Even vertex. Proof: it is not an S4c
  fallback (W-run), τ_{t+1} = τ_t (one τ-stretch), and every N5 iteration changes σ or τ ([R15] (d)). □ Hence |F| ≤ Σ_v SW_F(v), and every
  transition of F is an S4a step with σ_{t+1}(v) ∈ H_t(v) for every Even v ([R57]).
- Fact EXT (elementary, [S1-val] / [S1-ord]). ext(y, x) := (λ(x), P(x) ∪ {y if p′(y) > p′(λ(x))}, ℓ(x) + 1) is strictly order-preserving and
  order-reflecting: either both arguments gain y or neither (equal cycle nodes) or the comparison is decided by rew(λ) (different cycle
  nodes); the symmetric difference of path sets and the length difference are unchanged. For a vertex v that is not its own cycle node
  under a valuation Ω of a positional pair, Ω(v) = ext(v, Ω(succ)) for its successor succ on the play.

## 2. Other lanes' statements (VERBATIM, with SHAs; their lanes' labels kept)
### 2.1 ARENA-MAX (L-RED successor 33, R140, l-red 47000632, docs/red/R140-friedmann-port.md l. 42-46; identical at trunk)
> - Lemma ARENA-MAX. Let H_t be the arena of S4a at state t: Even v restricted to {σ_t(v)} ∪ Iσ_t(v), Odd fixed to τ_t. Then for every
>   vertex v and every Even strategy ρ of H_t:
>   W_(t+1)(v) ⊵ val(ρ, τ_t)(v), with W_(t+1) := val(σ_(t+1), τ_t).
>   - Proof. σ_(t+1) is Even's pointwise optimal strategy in the one-player game H_t (SPEC S4a: Odd's optimal counterstrategy on the dual of
>     H_t, i.e. VJ00's simultaneous optimum). □
- L-NEW note (not a new claim): ARENA-MAX is the S4a half of the standing premise [R57] read pointwise («σ_new is the pointwise optimum of
  the one-player arena H_t»). Used here only by §10 (REL2-WRISE) and the READING of §9.
### 2.2 INTERVAL-SI, TIGHT-VALUE, FL-INT (L-SI successor 33, l-si a0d6f79b, docs/si/N5-GATE-box51b.md §1, l. 22-47; identical at trunk)
> ## 1. Theorem INTERVAL-SI (PROVED, lane): a W-constant interval is strategy improvement on the W-tight subgame
> - Definition. For a valuation W = val(ρ, τ) (some Even strategy ρ, [S1-val] in G_τ) and a vertex v (either player):
>   OPT_W(v) := {e ∈ succ(v) : v ⊕ W(e) = W(v)} if v is not its own W-cycle node, and {e : W(e) has cycle node v and empty path set}
>   otherwise. G_W := the game in which Even's edges are restricted to OPT_W (Odd keeps all its edges).
> - Lemma TIGHT-VALUE. Every Even strategy σ with σ(v) ∈ OPT_W(v) for all Even v has val(σ, τ) = W.
>   - Proof. τ(o) ∈ OPT_W(o) for Odd o, because W is the valuation of the (ρ, τ)-plays ((V1); for an own cycle node o, τ(o) lies on o's
>     cycle and o is its most relevant vertex). Follow the (σ, τ)-play from x. At a vertex y that is not its own W-cycle node, the step
>     keeps λ_W and lowers the length of W by 1. A vertex with W-length 0 is its own W-cycle node. So within n steps the play reaches a
>     vertex c with λ_W(c) = c. From c it follows non-cycle-node steps (λ_W stays c) until the next own cycle node c′; then λ_W(c′) = c′
>     and λ_W(c′) = c, so c′ = c. The play therefore closes a cycle Γ through c.
>   - Backward induction along Γ with ⊕ gives that the path set of W(σ(c)) consists of the vertices of Γ ∖ {c} more relevant than c. That
>     set is empty, so c is the most relevant vertex of Γ: val(σ, τ)(c) = (c, ∅, 0) = W(c).
>   - The path from x to c is simple (lengths strictly fall), and backward induction with ⊕ gives val(σ, τ)(x) = W(x). □
> - Theorem INTERVAL-SI. Let I = [p, q] be a W-constant interval of a W-run F, W := W_p = … = W_q, G_I := G_W. Then:
>   - (i) σ_k is a strategy of G_I for every k ∈ I, by (V1) for W = val(σ_k, τ).
>   - (ii) Ξ_k is also the [S1] valuation of σ_k in G_I: Odd's edges are the same, and σ_k is fixed.
>   - (iii) every transition k → k + 1 of I switches a non-empty set of Even edges, each in Iσ_k ∩ G_I, i.e. improving for σ_k in G_I.
>     Every transition of a W-run moves σ (box 50b §1). A switched v takes σ_{k+1}(v) ∈ S4a's arena {σ_k(v)} ∪ Iσ_k(v) (RESULTS R91's
>     premise), different from σ_k(v), and in OPT_W(v) by (i) at k + 1.
>   - (iv) every Even strategy of G_I has τ-valuation W (TIGHT-VALUE). So inside I, the S4a choice among the edges of G_I is a pure
>     tie-break of SPEC S1's procedure.
>   - So the transitions of I form a run of Vöge–Jurdziński strategy improvement for Even on the fixed game G_I, valuation Ξ, with some
>     non-empty improving set switched at each step. □
> - Corollary FL-INT (PROVED, lane). FL_F = Σ_I |I| over the W-constant intervals I of F. Their number is WCH_F + 1 ≤ (n − 1)(R*_F + 1) + 1
>   (R92 FW-R*). So FL_F ≤ ((n − 1)(R*_F + 1) + 1)·max_I |I|, and FL-POLY ⇐ R*-POLY ∧ [P-INT], where [P-INT] := «every W-constant interval
>   of every run has ≤ p(n) transitions». [P-INT] is about N5's tie-break only.
- [P-INT] is L-SI's symbol: «every W-constant interval of every run has ≤ p(n) transitions». Used here by §3.3 row E7 and §11.
### 2.3 RETURN-CHARGE, INT-XCH (L-SI successor 33, l-si a0d6f79b, docs/si/N5-GATE-box51b.md §10.3, l. 276-294; identical at trunk)
> ### 10.3 Lemma RETURN-CHARGE (PROVED, lane): the exchange argument
> - Statement. In a W-run, let Even v leave d at k1 (σ_{k1}(v) = d ≠ σ_{k1+1}(v) = e1) and return to d at k2 > k1 (σ_{k2}(v) = e2 ≠ d =
>   σ_{k2+1}(v)). Assume λ_Ξ is constant on [k1, k2 + 1] and v is not its own Ξ-cycle node there. Then Ξ_{k2}(d) ▷ Ξ_{k1}(d).
> - Proof.
>   - S2 / the arena: e1 ∈ Iσ_{k1}(v), so Ξ_{k1}(e1) ▷ Ξ_{k1}(d). Likewise d ∈ Iσ_{k2}(v), so Ξ_{k2}(d) ▷ Ξ_{k2}(e2).
>   - Ξ(v) = v ⊕ Ξ(σ(v)) at every state of [k1, k2 + 1] (v not its own Ξ-cycle node). With λ_Ξ fixed, v ⊕ · adds the same bit and length
>     to values of one cycle node, so it preserves and reflects ⊴.
>   - Ξ is pointwise non-decreasing (R15 (a), (d)). So Ξ_{k2}(e2) ⊵ Ξ_{k1+1}(e1) ⊵ Ξ_{k1}(e1), by reflection through v ⊕ ·, using
>     Ξ_{k2}(v) ⊵ Ξ_{k1+1}(v).
>   - Chain: Ξ_{k2}(d) ▷ Ξ_{k2}(e2) ⊵ Ξ_{k1}(e1) ▷ Ξ_{k1}(d). □
> - Corollary INT-XCH (PROVED, lane). For a W-constant interval I, let XCH_I(d) be the transitions of I at which Ξ(d) changes, and RX_I the
>   returns outside the hypothesis.
>   - The windows (k1, k2] of successive returns of one v to one d are disjoint. A switch of v that is not a return adopts an edge v has
>     not held in I (≤ |OPT(v)| − 1 of them).
>   - Hence SW_I(v) ≤ |OPT(v)| − 1 + Σ_{d ∈ OPT(v)} XCH_I(d) + RX_I(v), and
>     |I| ≤ Σ_v SW_I(v) ≤ m_E + Σ_d d_E(d)·XCH_I(d) + RX_I.
>   - So [P-INT] ⇐ «XI-CH-POLY inside W-constant intervals» ∧ RX polynomial. With FL-INT and R139: FL-POLY ⇐ R*-POLY ∧ XI-CH-POLY ∧ RX-POLY.
>     FL stops being an independent residual. It is the in-interval case of the per-vertex Ξ-change count that L-LIT T52 and L-NEW
>     already target.
- DEDUPE (L-NEW): RETURN-CHARGE's conclusion Ξ_{k2}(d) ▷ Ξ_{k1}(d) is RET-ΞRISE's (§5.1), which needs neither «λ_Ξ is constant on
  [k1, k2 + 1]» nor «v is not its own Ξ-cycle node there»; both are the return form of landed [R86] SW-RETURN. So RX_I = 0 always (§11).
### 2.4 [SUB] (REFEREE-2 successor 22, l-referee-2 a11c2868, docs/referee-2/SUB-check.md l. 5-11; one referee's check, not a landing)
> ## Verdict: TRUE (Opus 5.5, D15)
> For every W-run F = [a, b] and every sub-interval F′ = [a′, b′] with a ≤ a′ ≤ b′ ≤ b (consecutive states of F), WCH_{F′} ≤ (n − 1)(R*_T(F′) + 1).
> - WCH_{F′} := the transitions t → t + 1 with a′ ≤ t < b′ and W_{t+1} ≠ W_t.
> - R*_T(F′) := the transitions τ → τ + 1 of F′ at which some Even y adopts an edge (y, z) that was BLOCKED (R88 §3) at some state
>   t ∈ [a′, τ).
> - R88's definitions are read with [a′, b′] in place of [a, b]. No added hypothesis is needed.
> - The bound with R*_T(F′) implies the bound with R*_T counted on all of F: every late adoption relative to F′ is late relative to F.

## 3. Theorem XI-RUN and Corollary WRUN-EQ (PROVED, L-NEW; a composition of [R86] SW-RETURN, [R15] (d) and Fact STEP-SW)
### 3.1 Definitions (per W-run F; every count is over the transitions t → t + 1 with t, t + 1 ∈ F unless said otherwise)
- ΞCH_F(c) := the transitions of F at which Ξ(c) changes (= [R86] RISE_F(c)); WCH_F(c) likewise for W(c); WCH_F := the transitions of F at
  which W changes at some vertex; FL_F := the transitions of F at which W changes at no vertex ([R89]'s FL with σ_{t+1} ≠ σ_t, automatic by
  STEP-SW). PCH_F(c) := the transitions of F at which P(Ξ(c)) changes and λ(Ξ(c)) does not. P*_F := max_c PCH_F(c).
- For a per-W-run quantity Q_F (a number for each W-run F of each N5 run on each game from each start pair; per-vertex or per-edge
  quantities are maximised over vertices or edges), «Q-POLY» := there is a polynomial p with Q_F ≤ p(n) for all of them.
  WRUN-POLY := |F|-POLY. XI-CH-POLY := (max_c ΞCH_F(c))-POLY.
### 3.2 Theorem XI-RUN
- Statement. For every W-run F, and more generally for every stretch R of consecutive states of a W-run (R ⊆ F, |R| its transitions):
  |R| ≤ Σ_{v Even} SW_R(v) ≤ m_E + Σ_c d_E(c)·RISE_R(c). For R = F: |F| ≤ m_E + Σ_c d_E(c)·ΞCH_F(c) ≤ m_E·(1 + max_c ΞCH_F(c)).
- Proof. Each transition of R switches some Even vertex (Fact STEP-SW), so |R| ≤ Σ_v SW_R(v) = Σ_v Σ_c ENT_R(v, c). ENT_R(v, c) = 0 unless
  (v, c) is an Even edge, and ENT_R(v, c) ≤ 1 + RISE_R(c) by [R86] SW-RETURN (any stretch). Summing over the m_E Even edges,
  Σ_{(v, c)} (1 + RISE_R(c)) = m_E + Σ_c d_E(c)·RISE_R(c). Finally Σ_c d_E(c) = m_E. □
### 3.3 Corollary WRUN-EQ: what is EQUIVALENT to polynomial W-runs, and what is one-way
Each row is PROVED here from the cited items (⇒ / ⇐ as marked); «trivially» means the quantity is at most |F|, or at most n_E·|F| or
m_E·|F|, since it counts transitions of F, pairs (vertex, transition of F) or (edge, transition) incidences.
| row | statement | ⇐ (sufficiency) | ⇒ (necessity) | kind |
| --- | --- | --- | --- | --- |
| E1 | WRUN-POLY ⇔ XI-CH-POLY | XI-RUN (§3.2) | ΞCH_F(c) ≤ |F| | EQUIVALENCE |
| E2 | XI-CH-POLY ⇔ P*-POLY | ΞCH-PCH (§6.2): ΞCH_F(c) ≤ n(n + 1 + PCH_F(c)) | PCH_F(c) ≤ ΞCH_F(c) | EQUIVALENCE |
| E3 | for each fixed k ≥ 1: XI-CH-POLY ⇔ DEEP_k-POLY | LEVEL-RED (§7.3) with E2 | DEEP_{k,F}(v) ≤ PCH_F(v) | EQUIVALENCE |
| E4 | WRUN-POLY ⇔ R*-POLY ∧ FL-POLY | [R88] FW-R* on F ([R89]): |F| = WCH_F + FL_F ≤ (n − 1)(R*_F + 1) + FL_F | R*_F, FL_F ≤ |F| | EQUIVALENCE |
| E5 | WRUN-POLY ⇔ ALT-POLY ∧ FREE-POLY | TRIPLE-RED (§4.4) | REG_F(X, g), FREE_F(X, g) ≤ RET_F(X, g) ≤ |F| | EQUIVALENCE |
| E6 | WRUN-POLY ⇔ R3-POLY ∧ TIE-POLY | [R93] NEW-BOUND | WCH_F(e) ≤ |F|, TIE_F ≤ n_E·|F| | EQUIVALENCE |
| E7 | WRUN-POLY ⇔ R*-POLY ∧ [P-INT] | FL-INT (§2.2; elementary: FL_F = Σ_I |I| over the WCH_F + 1 W-constant intervals, so a referee signing E7 signs it) with E4 | every W-constant interval I ⊆ F has |I| ≤ |F| | EQUIVALENCE |
| E8 | under [SUB]: WRUN-POLY ⇔ SB-POLY ∧ R°-POLY ∧ FL-POLY | BIP-RED (§9) | SB_F ≤ |F|, R°_Φ ≤ |Φ| ≤ |F| | EQUIVALENCE (⇐ needs [SUB]) |
| E9 | R*-POLY ⇐ XI-CH-POLY; FL-POLY ⇐ XI-CH-POLY; SB-POLY ⇐ XI-CH-POLY | E1 then R*_F, FL_F, SB_F ≤ |F|; directly also R*_F ≤ m_E·max_z ΞCH_F(z) (RSTAR-PCH) | — | ONE-WAY |
| E10 | BIP-REL-1 ∧ SB-POLY ∧ FL-POLY ⇒ WRUN-POLY (under [SUB]) | BIP-RED with R° ≤ m_E | — (BIP-REL-1 is not implied by WRUN-POLY as far as known) | ONE-WAY |
| E11 | [P-INT] ⇐ XI-CH-POLY read inside W-constant intervals | INT-XCH⁰ (§11) | — | ONE-WAY |
| E12 | (Ξ_t = W_t at every state of F) ⇒ |F| ≤ (n − 1) + 4n²(n − 1) | NO-DEV (§8.3, corrected) | — | ONE-WAY (special case) |
| E13 | WRUN-POLY ⇒ R3-POLY | WCH_F(e) ≤ |F| | — | ONE-WAY (the converse needs TIE-POLY, E6) |
- Reading of the table (PROVED by the rows): XI-CH-POLY, P*-POLY, DEEP_k-POLY (any fixed k), R*-POLY ∧ FL-POLY, ALT-POLY ∧ FREE-POLY,
  R3-POLY ∧ TIE-POLY, R*-POLY ∧ [P-INT] and (under [SUB]) SB-POLY ∧ R°-POLY ∧ FL-POLY are all the SAME open statement WRUN-POLY.
- WRUN-POLY does not by itself bound N5's runs: τ-changes, S4c fallbacks and λ_W-changes cut runs into W-runs ([R89] STRETCH-RED's Q and
  fb_S, RESULTS R90's B*, O*). Not claimed here.
- DATA (experiments/new/box92/xirun.py, xirun_sbcg.txt + xirun_alt.txt, box 83's corpus, 1132 runs, 1692 W-runs): XI-RUN 0 violations;
  STEP-SW 0 transitions without an Even switch; SW-RETURN per edge 0 violations; max |F| / (m_E + Σ_c d_E(c)·ΞCH_F(c)) = 0.273
  (thetaA_n6). Pins (check.sh "box 92"): pftheta34_n32 |F| 34, max ΞCH 34, bound 1010; fx_K8_m32 |F| 280, max ΞCH 137, bound 2005.
  Also latew_K16_m32 |F| 560, bound 4389; gate_K64_n581 |F| 71, max ΞCH 63, bound 2733.

## 4. Box 84: returns, blocks, Theorem TRIPLE-RED (PROVED, L-NEW successor 38; restated)
### 4.1 Definitions
- SELF-ROUTED BLOCK of (X, g) at state t: X Even, g ∈ succ(X), g ≠ σ_t(X), (X, g) ∉ Iσ_t, and the (σ_t, σ̄_t)-play from g reaches X with
  the vertices strictly before X pairwise distinct; π := those vertices (g first; π = ∅ iff g = X). If X lies on the cycle Z* of its own
  (σ_t, σ̄_t)-play, π is also required to avoid Z*. The ROUTE PATTERN is σ_t restricted to the Even vertices of π. c* := λ(Ξ_t(X)). The block
  is E0 if c* = X and every vertex of π has p′ below p′(X); otherwise REG. rew(c) := p′(c) if Ω(c) is even, −p′(c) if odd (SPEC S1); p′ as
  in SPEC S1 (p′(v) = 2·rank(v) + (Ω(v) mod 2)); «u is above c» means p′(u) > p′(c).
- RETURN. In a W-run F, a return of X to g is a transition t2 − 1 → t2 of F with σ_t2(X) = g ≠ σ_{t2−1}(X) where X held g at some earlier
  state of F; s → s + 1 (s ≥ a) is X's last leave of g before t2. RET_F(X, g) counts them. Class: REG if some state in [s + 1, t2 − 1] has a
  REG block of (X, g); else E0 if some state there has an E0 block of (X, g); else FREE. REG_F, E0_F, FREE_F count them.
  (So RET_F(X, g) = ENT_F(X, g) − 1 if σ_a(X) ≠ g and ENT_F(X, g) ≥ 1, and RET_F(X, g) = ENT_F(X, g) otherwise.)
### 4.2 Lemma WAIT-CYCLE′, Corollaries DEAD-CYCLE and CHARGE
- Statement. Let (X, g) have a REG block at t1 with route π and pattern Pat. Then at no state t > t1 of the run do σ_t(X) = g and
  σ_t|Even(π) = Pat hold together.
- Proof. Claim A: the simple cycle C := X → g → π → X has top vertex z (max p′ on π ∪ {X}) with rew(z) < rew(c*).
  - Case 1, X ∉ Z*. π ∪ {X} is disjoint from the play of σ_t1(X). Write Ξ_t1(σ_t1 X) = (c*, P′, ℓ′). Then Ξ_t1(g) = (c*, P′ ∪ A, ℓ′ + 1 + |π|),
    A := the vertices of π ∪ {X} above c*, disjoint from P′. If A ≠ ∅, its top m decides the comparison with Ξ_t1(σ_t1 X) ([R93] LEX); the
    block (Ξ_t1(g) ⊴ Ξ_t1(σ_t1 X)) forces Ω(m) odd; z = m and rew(m) = −p′(m) < rew(c*) (c* even: rew(c*) > 0; c* odd: p′(m) > p′(c*)).
    If A = ∅ the path sets are equal and Ξ_t1(g) is longer; if c* were odd that is better for Even, contradicting the block; so c* is
    even, every vertex of C is below c*, and rew(z) ≤ p′(z) < p′(c*) = rew(c*).
  - Case 2, X ∈ Z*, X ≠ c*. π avoids Z*, X's way to c* runs inside Z*, so Ξ_t1(σ_t1 X) = (c*, ∅, ℓ′) and Ξ_t1(g) = (c*, A, ℓ′ + 1 + |π|)
    with A := the vertices of π above c*. Case 1's two sub-cases apply verbatim (c* ∈ Z* ∖ {X} is not on C).
  - Case 3, X = c*, REG. Ξ_t1(σ_t1 X) = (X, ∅, |Z*| − 1) and Ξ_t1(g) = (X, A, |π|), A := the vertices of π above X, A ≠ ∅ (REG). Its top m
    is odd (else (X, g) would be improving), z = m, rew(m) < rew(X) as in Case 1.
  - Suppose t > t1, σ_t(X) = g, σ_t|Even(π) = Pat. Let ρ′ := σ̄_t1 on the Odd vertices of π and σ̄_t elsewhere. The (σ_t, ρ′)-play from X is C
    repeated, so val(σ_t, ρ′)(X) has cycle node z. σ̄_t is Odd's pointwise optimum against σ_t (SPEC S1), so Ξ_t(X) ⊴ val(σ_t, ρ′)(X) and
    rew(λ(Ξ_t(X))) ≤ rew(z) < rew(c*) = rew(λ(Ξ_t1(X))). The order compares rew(λ) first, so Ξ_t(X) ◁ Ξ_t1(X), contradicting MON. □
- Corollary DEAD-CYCLE. For any simple cycle C, Y ∈ C and state t1 with rew(top C) < rew(λ(Ξ_t1(Y))), at no state t ≥ t1 is every Even
  vertex of C pointing along C. Same proof (last bullet).
- Corollary CHARGE. If a return of X to g at t2 is REG with REG block at t1 ∈ [s + 1, t2 − 1] and route π, then some Even y ∈ π has
  σ_t2(y) ≠ σ_t1(y) (by WAIT-CYCLE′, as σ_t2(X) = g), so y switches at some transition of [t1, t2 − 1].
### 4.3 Lemma E0-BOUND
- Statement. For every Even edge (X, g) and every W-run F, E0_F(X, g) ≤ n.
- Proof. Let the E0 returns be at t2^1 < t2^2 < …, with E0 blocks at t1^i ∈ [s^i + 1, t2^i − 1]. At an E0 block the play from g is π then
  X, X = λ(Ξ(X)), π below X, so Ξ_{t1^i}(g) ∈ K := {(X, ∅, ℓ) : 0 ≤ ℓ ≤ n − 1}. At t2^i − 1, (X, g) ∈ Iσ (Fact STEP-SW: S4a takes only
  edges of H), so with [R89] SUCC-MON and the block: Ξ_{t2^i − 1}(g) ▷ Ξ_{t2^i − 1}(σ X) ⊵ Ξ_{t1^i}(σ_{t1^i} X) ⊵ Ξ_{t1^i}(g). So Ξ(g)
  changes at some transition of [t1^i, t2^i − 1]. These windows are disjoint (t1^{i+1} > s^{i+1} ≥ t2^i). K is an interval of the order
  (values between two members of K have equal rew(λ), hence cycle node X, and equal path-set coordinates, hence ∅: [R93] LEX), so by MON
  Ξ(g) stays in K on [t1^1, t1^last], and the strict changes of the first (last − 1) windows are distinct moves inside K, which has n
  elements: last − 1 ≤ n − 1. □
### 4.4 Theorem TRIPLE-RED (a REDUCTION)
- Statement. For every W-run F: |F| ≤ m_E + Σ_{(X, g)} RET_F(X, g) ≤ m_E(n + 1) + Σ_{(X, g)} REG_F(X, g) + Σ_{(X, g)} FREE_F(X, g).
  CONJECTURE ALT-POLY := (max_{(X, g)} REG_F(X, g))-POLY; CONJECTURE FREE-POLY := (max_{(X, g)} FREE_F(X, g))-POLY. Then
  ALT-POLY ∧ FREE-POLY ⇒ WRUN-POLY, and conversely (row E5).
- Proof. By STEP-SW every transition of F switches some Even X; each switch adopts an edge X has not held earlier in F (at most once per
  Even edge: ≤ m_E) or is a return. Each return has exactly one class; E0_F ≤ n per Even edge (§4.3). □

## 5. Box 85: Lemma RET-ΞRISE, Theorem FREE-RED (PROVED, L-NEW successor 38; restated)
### 5.1 Lemma RET-ΞRISE
- Statement. In every W-run F, for every Even edge (X, g): RET_F(X, g) ≤ ΞCH_F(g). Each return k → k + 1 with last leave s → s + 1 has
  Ξ_k(g) ▷ Ξ_s(g).
- Proof. At s, X moved from g to h ∈ Iσ_s(X) (Fact STEP-SW), so Ξ_s(h) ▷ Ξ_s(g). At k, (X, g) ∈ Iσ_k, so Ξ_k(g) ▷ Ξ_k(σ_k X)
  ⊵ Ξ_{s+1}(σ_{s+1} X) = Ξ_{s+1}(h) ⊵ Ξ_s(h) ▷ Ξ_s(g) ([R89] SUCC-MON; MON). So Ξ(g) changes at a transition of [s, k − 1]; the windows of
  successive returns of one edge are disjoint. □
- Status (DEDUPE). The chain is [R86] SW-RETURN's (landed: ENT_F(X, g) ≤ 1 + RISE_F(g)), started at the leave s instead of at an entry;
  this also covers σ_a(X) = g, where SW-RETURN alone gives only RET_F(X, g) ≤ 1 + ΞCH_F(g). §2.3's RETURN-CHARGE is its special case.
### 5.2 Theorem FREE-RED (a REDUCTION)
- Statement. For every W-run F and Even edge (X, g): FREE_F(X, g) ≤ RET_F(X, g) ≤ |F| ≤ (n − 1)(R*_F + 1) + FL_F.
- Proof. A return of X is a switch of X at one transition of F, one per transition. Every transition of F changes W or is counted in
  FL_F; at most (n − 1)(R*_F + 1) change W ([R88] FW-R* on F by [R89] GP*-RUN). □
- Note: since XI-RUN (§3), FREE-RED is subsumed by E4 / E1; it is kept because the Lead's outline lists it.

## 6. Box 86: Lemma GAP-DEV, Lemma ΞCH-PCH, Theorem RSTAR-PCH (PROVED, L-NEW successor 38; restated)
### 6.1 Lemma GAP-DEV
- Statement. If (y, z) is BLOCKED at a state q of a W-run (τ = τ_q), then Ξ_q(z) ◁ W_q(z), and the (σ_q, σ̄_q)-play from z contains an
  Odd vertex o with σ̄_q(o) ≠ τ(o).
- Proof. W_q(z) ▷ W_q(σ_q y) ⊵ Ξ_q(σ_q y) ⊵ Ξ_q(z): the first by BLOCKED, the second by [R91] XW, the third because (y, z) ∉ Iσ_q. If
  σ̄_q agreed with τ at every Odd vertex of the (σ_q, σ̄_q)-play from z, that play would be the (σ_q, τ)-play and Ξ_q(z) = W_q(z). □
### 6.2 Lemma ΞCH-PCH
- Statement. For every W-run F and vertex z: ΞCH_F(z) ≤ (n − 1) + PCH_F(z) + (n + PCH_F(z))(n − 1) ≤ n(n + 1 + PCH_F(z)).
- Proof. λ(Ξ(z)) changes at most n − 1 times in the whole run: by MON and [R93] LEX each change strictly raises rew(λ(Ξ(z))), rew is
  injective, and λ takes at most n values. Split F's transitions at those where (λ, P)(Ξ(z)) changes: at most (n − 1) + PCH_F(z) of them,
  so at most n + PCH_F(z) maximal blocks with (λ, P)(Ξ(z)) constant. Inside a block, a change of Ξ(z) changes only ℓ, which by MON moves
  strictly in one direction in [0, n − 1]: at most n − 1 changes per block. □
### 6.3 Theorem RSTAR-PCH (a REDUCTION; a composition of [R89] R*-RISE and §6.2)
- Statement. For every W-run F: R*_F ≤ Σ_{(y, z) Even edge} ΞCH_F(z) ≤ m_E·n·(n + 1 + P*_F).
- Proof. A transition counted in R*_F carries at least one late adoption, so R*_F ≤ Σ_{(y, z)} LATE_F(y, z) ≤ Σ_{(y, z)} ΞCH_F(z) ([R89]
  R*-RISE; LATE_F(y, z) the late adoptions of (y, z) in F). Apply §6.2. □

## 7. Box 87: Lemmas LEX-SIGN, PREFIX-MON, Theorem LEVEL-RED (PROVED, L-NEW successor 38; restated)
### 7.1 Lemma LEX-SIGN
- Statement. For values x, y with λ(x) = λ(y): P(x) ◁ P(y) in the path-set comparison of SPEC S1 iff the vector (s_{n−1}, …, s_0) of
  CS(x) is lexicographically below that of CS(y) ([R93] LEX). Proof: CS(x), CS(y) have equal first coordinates rew(λ); [R93] LEX. □
### 7.2 Lemma PREFIX-MON
- Definitions. The signed TERM LIST of a path set P: its elements in decreasing rank, each with sign + (even priority) or − (odd). Order
  single terms: (r, +) > (r′, +) iff r > r′; every (r, +) > NONE > every (r′, −); (r, −) < (r′, −) iff r > r′. pre_k(P) := the first k terms,
  padded with NONE, ordered lexicographically. For a change of P (P ≠ P′, same λ) with top differing rank r, its DEPTH is the number of
  terms of P (equivalently of P′) above r.
- Statement. While λ(Ξ_t(v)) is constant, pre_k(P(Ξ_t(v))) is non-decreasing in t, and strictly increases at every change of depth < k.
  It takes at most (2n + 1)^k values.
- Proof. Let P ◁ P′ (§7.1) with top differing rank r and d common terms above r; the pairs (s_r(P), s_r(P′)) are (0, +1), (−1, +1) or
  (−1, 0). If d ≥ k the prefixes are equal. Otherwise term d + 1 decides. Case s_r(P′) = +1: P′'s term is (r, +); P's is (r, −), a term of
  lower rank, or NONE, each below (r, +). Case s_r(P) = −1, s_r(P′) = 0: P's term is (r, −); P′'s is a term of lower rank or NONE, each
  above (r, −). MON. Term values: n ranks × 2 signs + NONE. □
### 7.3 Theorem LEVEL-RED (a REDUCTION)
- Definition. DEEP_{k,F}(v) := the transitions of F at which P(Ξ(v)) changes with λ(Ξ(v)) unchanged and the change has depth ≥ k.
  CONJECTURE DEEP_k-POLY := (max_v DEEP_{k,F}(v))-POLY.
- Statement. For every W-run F, vertex v and k ≥ 1: PCH_F(v) ≤ n·((2n + 1)^k − 1) + DEEP_{k,F}(v) ≤ n(2n + 1)^k + DEEP_{k,F}(v).
- Proof. λ(Ξ(v)) takes at most n values in F (§6.2), so at most n maximal blocks with λ(Ξ(v)) constant. In each, the changes of depth < k
  strictly raise pre_k (§7.2), at most (2n + 1)^k − 1 times. □

## 8. Box 88: BIP(ρ, τ), Lemma BIP-MON, Lemma NO-DEV (PROVED, L-NEW successor 38; NO-DEV corrected by successor 39)
### 8.1 Definition BIP(ρ, τ) and the identification
- For Odd strategies ρ, τ: BIP(ρ, τ) is the process on Even strategies σ_t with offers Iρ_t := {(y, z) : val(σ_t, ρ)(z) ▷ val(σ_t, ρ)(σ_t y)}
  and step σ_{t+1} := the pointwise-optimal Even strategy (against τ) of the one-player arena σ_t ∪ Iρ_t.
- A FROZEN STRETCH Φ of a W-run F is a maximal interval of states of F on which σ̄_t is constant, = ρ. On Φ, N5's step is BIP(ρ, τ)'s
  (SPEC S1-S2: Ξ_t = val(σ_t, ρ), Iσ_t = Iρ_t; [R57]).
### 8.2 Lemma BIP-MON
- Statement. Along BIP(ρ, τ), val(σ_t, ρ) and val(σ_t, τ) are pointwise non-decreasing.
- Proof. In the one-player game G_ρ (Odd restricted to ρ), Odd's optimal counterstrategy to any σ is ρ, so val(σ, ρ) is VJ00's Ωσ there and
  Iρ_t its improvement set; σ_{t+1} switches a subset of it, non-empty when σ_{t+1} ≠ σ_t: [R15] (a) in G_ρ. σ_{t+1} is the pointwise
  optimum against τ of an arena containing σ_t: val(σ_{t+1}, τ) ⊵ val(σ_t, τ) (the inequality of ARENA-MAX with ρ := σ_t). □
### 8.3 Lemma NO-DEV (CORRECTED)
- Statement. If Ξ_t = W_t at every state t of a W-run F, then R*_F = 0, WCH_F ≤ n − 1, every run of consecutive FL transitions of F has
  at most 4n(n − 1) transitions, and |F| ≤ (n − 1) + n·4n(n − 1).
- Proof. A blocked target would have Ξ ◁ W (GAP-DEV): none, so R*_F = 0, and WCH_F ≤ n − 1 ([R88] FW-R*). At an FL transition W is
  unchanged at every vertex, hence so is Ξ (= W at both states); τ is constant on F, so Odd's valuation Ωτ (a function of τ alone) is
  unchanged too; by [R15] (d) at most 4n(n − 1) consecutive transitions do this. The ≤ n − 1 W-changing transitions split F into ≤ n such
  runs: |F| ≤ (n − 1) + n·4n(n − 1). □
- CORRECTION (finding of successor 39). Box 88 §1 claimed FL_F = 0 and |F| ≤ n − 1 because «a switched vertex strictly improves its Ξ».
  That step is not justified as written: [R15] (a) is non-strict, the recursion Ξ(y) = ext(y, Ξ(σ y)) fails when the switched y is its
  own cycle node, and [R15] (b) leaves open exactly that case (length-only switches at a cycle node with Ω unchanged). I have neither a
  proof that it cannot occur in a W-run with Ξ = W nor an instance where it does. The corrected bound is still polynomial; only the constant changed.

## 9. Box 89: Theorem BIP-RED under [SUB] (PROVED, L-NEW successor 38)
- Definitions. In a W-run F: SB_F := the transitions of F at which σ̄ changes (at some Odd vertex); F has SB_F + 1 frozen stretches (§8.1).
  A STRICT RELEASE in a frozen stretch Φ is an adoption of (y, z) at a transition of Φ such that (y, z) is BLOCKED at some state of Φ
  before it (a Φ-late adoption, = §2.4's R*_T(Φ)). R°_Φ := the transitions of Φ carrying a strict release; R° := max_Φ R°_Φ over the frozen
  stretches of F.
- Premise [SUB] (§2.4): FW-R* holds on every sub-interval F′ of a W-run with R* counted inside F′: WCH_{F′} ≤ (n − 1)(R*_T(F′) + 1).
- Statement. Under [SUB], every W-run F has |F| ≤ SB_F + (SB_F + 1)·(n − 1)·(R° + 1) + FL_F.
- Proof. A transition of F either changes σ̄ (SB_F of them) or has both states in one frozen stretch Φ. In Φ, [SUB] gives at most
  (n − 1)(R°_Φ + 1) transitions changing W; the others are FL transitions, at most FL_F over all stretches. □
- With CONJECTURE BIP-REL-1 (§12) R° ≤ m_E (row E10).

## 10. Box 90: Lemma REL2-WRISE (PROVED, L-NEW successor 38, under (A1), (A2); used by no reduction)
- Setting. In a frozen stretch Φ (σ̄ ≡ ρ, τ fixed), (y, z) has a strict release at t1, y leaves z at s > t1 (σ_s(y) = z, σ_{s+1}(y) = h),
  and (y, z) is BLOCKED again at q2 > s, h2 := σ_q2(y). (A1) y is not its own W-cycle node at any state of [s + 1, q2]. (A2) with π_s :=
  σ_{s+1} changed at y to z, the (π_s, τ)-play from z does not pass y.
- Statement. W_q2(z) ▷ W_{s+1}(z), and Ξ_q2(z) ⊴ Ξ_q2(h2).
- Proof. (i) π_s is a strategy of H_s (z = σ_s(y) ∈ H_s(y); elsewhere π_s = σ_{s+1} ∈ H_s). ARENA-MAX: W_{s+1}(y) ⊵ val(π_s, τ)(y). By (A2),
  val(π_s, τ)(z) = W_{s+1}(z) and val(π_s, τ)(y) = ext(y, W_{s+1}(z)); by (A1), W_{s+1}(y) = ext(y, W_{s+1}(h)). Fact EXT reflects:
  W_{s+1}(h) ⊵ W_{s+1}(z). (ii) [R91] W-SUCC on [s + 1, q2] (F lies inside one piece: τ constant, no S4c; and (A1)): W_q2(h2) ⊵ W_{s+1}(h). (iii) BLOCKED at q2: W_q2(z) ▷ W_q2(h2) and
  (y, z) ∉ Iσ_q2, i.e. Ξ_q2(z) ⊴ Ξ_q2(h2). Chain (iii), (ii), (i). □

## 11. Corollary INT-XCH⁰ (PROVED, L-NEW; XI-RUN on a W-constant interval)
- Statement. For every W-constant interval I of a W-run F (§2.2), with XCH_I(d) the transitions of I at which Ξ(d) changes:
  |I| ≤ m_E + Σ_d d_E(d)·XCH_I(d). That is L-SI's INT-XCH with RX_I = 0, and it needs neither INTERVAL-SI nor RETURN-CHARGE's hypotheses.
- Proof. I is a stretch of consecutive states of F: §3.2 with R = I. □
- Hence [P-INT] ⇐ XI-CH-POLY read inside W-constant intervals (row E11), and L-SI's «FL-POLY ⇐ R*-POLY ∧ XI-CH-POLY ∧ RX-POLY» holds
  without the RX-POLY conjunct (and, by E1, without R*-POLY too).

## 12. CONJECTURES and open statements (NOT to sign; none is claimed)
- WRUN-POLY (= |F|-POLY) and its equivalent forms of §3.3: XI-CH-POLY, P*-POLY, DEEP_k-POLY (k fixed), R*-POLY ∧ FL-POLY,
  ALT-POLY ∧ FREE-POLY, R3-POLY ∧ TIE-POLY, R*-POLY ∧ [P-INT], SB-POLY ∧ R°-POLY ∧ FL-POLY. Separately open: R*-POLY, FL-POLY, ALT-POLY,
  FREE-POLY, R3-POLY (RESULTS-free statement in docs/new/N5-R3-box83.md), TIE-POLY, [P-INT], SB-POLY, R°-POLY.
- CONJECTURE BIP-REL-1: in every frozen stretch Φ of every W-run, each Even edge has at most one strict release (so R°_Φ ≤ m_E).
- CONJECTURE BIP-POLY: every BIP(ρ, τ) run (any game, any ρ, τ, any start) has at most p(n) steps.
- CONJECTURE INT-LIN (L-SI, l-si a0d6f79b §FINDINGS 8): |I| ≤ n − 1 for every W-constant interval I.
- CONJECTURES NT-1 / GAP-1 / IMM-1 (box 85 §4): at most one FREE return of each of these sub-classes per (F, X, g).
- CONJECTURE FLAT-SW (P-N5-FIXD §4) is not used here.

## 13. DATA, DEAD, READING (NOT to sign)
- DATA. Corpus = box 83's lists (experiments/new/box59/sbcg.lst, 719; experiments/si/root/logs/alt_all.lst, 413), 1132 runs, S3 starts.
  - XI-RUN: §3.3 (box92/xirun.py; 0 violations; max ratio 0.273). WAIT-CYCLE′: 0 violations in 434,925 REG blocks (box84/waits.py).
  - Returns REG 1,005 / E0 0 / FREE 5,260 (box84/retclass.py); FREE = LAT 4,911 / NT 231 / GAP 115 / IMM 3 (box85/freeclass.py).
  - GAP-DEV 0 violations in 116,086 blocked (edge, state) records (box86/rstar.py); ΞCH-PCH, RSTAR-PCH 0 violations (box86/pch.py).
  - PREFIX-MON 0 violations, k = 1, 2, 3 (box87/depth.py). BIP-REL-1 0 violations (box89/relpe.py STRICT=1). [SUB]: 57,726 sub-interval
    checks, 0 violations (REFEREE-2's sub_check.py, §2.4).
  - Largest values: R*_F 64 and ΞCH_F 63 (red/usplit/instances/gate_K64_n581.pg, sha1 a93c7c8b…); |F| 560, SB_F 513
    (red/rstar/instances/latew_K16_m32.pg, sha1 6d34c161…, l-red 5374e0a5); fx_K8_m32 (red/free/instances/fx_K8_m32.pg, sha1 e995709e…)
    |F| 280, ΞCH 137, all 836 FREE returns LAT; obs_K12_m24 (L-RED R139, l-red 9326f166, sha1 7df541fb…; not on trunk) |F| 324 > n − 1
    with SB_F = 1.
- DEAD (each with the instance that killed it):
  - DEV-CAP (R*_F ≤ distinct Odd deviation edges): red/usplit/instances/gate_K16_n197.pg (sha1 3eeddc86…), R*_F 16 > 5.
  - SHALLOW-k (every path-set change has depth < k, k constant): new/box54/out/switchbestexp_N, depth 3N + 3; counter_symsi_8 depth 42.
  - FLIP-c (each top-differing rank tops ≤ c changes per (F, v)): fx family (L-RED span/mkrw.py + free/obsx.py, BLK=2 OWNER=0 ABOVE=a), K + 1.
  - Non-strict BIP-REL-1 (blocks counted anywhere in F): si/root/instances/ueonce_n27.pg (sha1 c90d5ab8…), edge (10, 23) twice.
  - SB-LIN (SB_F ≤ n): red/so/instances/pftheta34_n32.pg (sha1 b291d7bb…), 34 > 32; latew_K16_m32, 513 > 482.
- READING. After E1 the whole within-W-run problem is ONE per-vertex count: how often Ξ(c) can change inside one W-run. The earlier
  residuals (R*, FL, REG / FREE returns, σ̄-flips, deep path-set changes) are its faces. The open core is the lexicographic counter in
  Ξ's path set (§7: depth ≥ k changes; [FFSS] arXiv 1007.2989 Prop. 5.2 / 6.3, opened by successor 38, shows that monotonicity in a
  lexicographic order alone gives no polynomial bound). Largest known: max ΞCH_F(c) = 137 at n 250 (0.55n); no super-linear family.

## 14. Symbols (all bound in docs/new/P-N5-WRUN-box92-line.txt)
n; n_E; m_E; d_E(c); N5; run; state; transition; switched / adopt / enter / leave; σ_t, τ_t, σ̄_t; Ξ_t; W_t; val(ρ, τ); value (c, P, ℓ);
λ, P, ℓ; λ_Ξ, λ_W; ⊴ ◁ ⊵ ▷; rank, p′, rew; Iσ_t; H_t; [R57]; τ-stretch; W-run F = [a, b]; |F|; stretch R, |R|; ENT_R, SW_R, RISE_R; ΞCH_F,
WCH_F(c), WCH_F, FL_F, TIE_F; PCH_F, P*_F; BLOCKED; late adoption; R*_F; Q-POLY; WRUN-POLY; XI-CH-POLY; P*-POLY; DEEP_k-POLY; R*-POLY;
FL-POLY; R3-POLY; TIE-POLY; ALT-POLY; FREE-POLY; SB-POLY; R°-POLY; [P-INT]; self-routed block, route π, pattern, c*, REG, E0, FREE; return,
RET_F, REG_F, E0_F, FREE_F; CS (R93 LEX); term list, pre_k, depth, DEEP_{k,F}; BIP(ρ, τ); frozen stretch Φ; SB_F; strict release; R°_Φ, R°;
[SUB]; ext; (A1), (A2); W-constant interval I; XCH_I; G_I, OPT_W (L-SI); LATE_F(y, z).
