# P-N5-CUT (box 43): N5's iteration count reduced to boundaries, repeat late adoptions, silent / own-cycle re-entries and Odd switches (W-RETURN-G, CUT-CHARGE, FRESH-SPLIT, WV-R, LATE-SPLIT, Theorem CUT-RED)
L-SI successor 31 (Opus 5.5; D15 / D18, Lead reading L40). Packet for the two referees, FROZEN at its push; the sha1 goes to the Lead;
repairs go in a NEW file docs/si/P-N5-CUT-fixes-box43.md, never into this file. Lead 2026-10-30 00:23Z / 00:34Z: «Freeze packet P-N5-CUT
for the two referees … FRESH-SPLIT and its ENT bound (box 40), WV-R (box 41), and LATE-SPLIT plus R* ≤ m_E + REP (box 42) … the exact
conditional ([C1]-[C3], [P-*]) ⇒ G-N5-TIME, written as a REDUCTION in the style of R89's STRETCH-RED: every symbol defined, every hypothesis
carried; the definitions of "late adoption" and "W-run" quoted from the frozen tool … pinned checks.» Working notes with data:
docs/si/N5-CUT-box40.md, N5-WVP-box41.md, N5-LATE-box42.md. Labels (D18 / L40): PROVED (lane, unrefereed) / DATA / READING.
SCOPE (D1): a REDUCTION of N5's iteration count on every game to four counts that are NOT bounded here. Not a TARGET.md claim, not an
algorithm claim, no running-time bound; G-N5-TIME stays OPEN. Every [Q path@commit:lines] «…» is verbatim, checked by
experiments/si/rund/quotecheck.py (pinned in experiments/si/check.sh «box 43» with the shifted-line control that must fail).
L-NEW's box 66 lemmas (LATE-W, LATE-PIECE, l-new 78e1fd24) overlap §6 (i)-(ii); they are cited as lane input only and used nowhere.

## 0. What to sign, and what not
| § | statement | label |
| --- | --- | --- |
| §2 | Lemma OPT-OFF (S4a's σ_new is successor-optimal at every off-cycle Even vertex, in the frame of the old τ), Lemma W-MON′, Lemma W-SUCC | PROVED (to sign) |
| §3 | Lemma W-RETURN-G (anchored re-entries are W-paid or W-silent) | PROVED (to sign) |
| §4 | Corollary CUT-CHARGE (ENT ≤ 1 + FC + WCH* + SIL + CYC; FC ≤ B_R) | PROVED (to sign) |
| §5 | Lemma FRESH-SPLIT and its ENT bound | PROVED (to sign separately; not used by §8) |
| §6 | Lemma LATE-SPLIT (FIRST ≤ m_E per W-run; a REPEAT needs a W-rise of z or is W-silent) and Corollary R*-REP (R*_T ≤ m_E + REP_F) | PROVED (to sign) |
| §7 | Lemma WV-R (W-changes of one vertex per guided stretch) | PROVED (to sign) |
| §8 | Theorem CUT-RED (the reduction) and Corollary CUT-POLY (the conditional) | PROVED (to sign) |
| §9 | readings, data, pinned checks | READING / DATA (NOT to sign) |

## 1. Setting, symbols, premises
- N5 = SPEC S1-S5 of docs/new/N5-ssi-global.md (FIX 1-4 as in RESULTS); any parity game G = (V, E, Ω, owner), n = |V|, m_E (m_O) = the
  number of edges leaving Even (Odd) vertices. A run is the sequence of states (σ_t, τ_t); a TRANSITION is t → t + 1; T = the number of
  transitions of the run.
- [S1-val] [Q docs/new/N5-ssi-global.md@7039eb524:28-29] «valuation of v under (σ, σ̄): (c, P, ℓ), c = the most relevant (max p') vertex
  of the cycle the play from v ends in, P = set of vertices on the play before reaching c with p' > p'(c), ℓ = number of steps to reach c.»
  The same definition is applied to any pair of positional strategies, one per player.
- [S1-ord] [Q docs/new/N5-ssi-global.md@7039eb524:30-31] «order (better for Even): compare reward of c (p'(c) if even, −p'(c) if odd); then P
  by the signed weight Σ_{u∈P} (+2^rank(u) if Ω(u) even else −2^rank(u)); then ℓ: if c is odd, longer is better for Even; if c even, shorter
  is better.» ⊴ / ◁ (strict), ⊵ / ▷ the reverse. Distinct triples are distinct in the order (RESULTS R84 (a) Fact DELTA).
- [S1-Xi] [Q docs/new/N5-ssi-global.md@7039eb524:32] «Ξσ = valuation of every vertex under σ and Odd's OPTIMAL counterstrategy σ̄ (minimising
  this order at every vertex at once).» Ξ_t := Ξσ_t; λ_t := its cycle-node map.
- [S1-dual] [Q docs/new/N5-ssi-global.md@7039eb524:45-46] «Odd's side: everything on the DUAL game G^d (owner swapped, Ω + 1); τ is an "Even"
  strategy of G^d; Ξτ, τ̄ (= Even's optimal counterstrategy to τ, as a G^d-Odd strategy), Iτ computed there.» λ^U_t := the cycle-node map of
  Ξτ_t on G^d (RESULTS R86 / R47).
- [S2] [Q docs/new/N5-ssi-global.md@7039eb524:47] «Improving edges: Iσ = {(v, w) : owner(v) = Even, w ≠ σ(v), Ξσ(w) strictly better than
  Ξσ(σ(v))}; Iτ the same on G^d for τ.»
- [S4a] [Q docs/new/N5-ssi-global.md@7039eb524:51-53] «a. If Iσ ≠ ∅: A(v) = {σ(v)} ∪ {w : (v, w) ∈ Iσ} for Even v. Arena H: Even v keeps only
  edges to A(v); Odd v keeps only the edge to τ(v). σ_new = Odd's optimal counterstrategy (S1 procedure) in the dual of H to the dual-Even
  strategy τ, read as an Even strategy of G. (Even's one-player optimum against τ among "keep or take an improving edge".) Else σ_new = σ.»
- [S4b] [Q docs/new/N5-ssi-global.md@7039eb524:54-55] «b. If Iτ ≠ ∅: A(v) = {τ(v)} ∪ {w : (v, w) ∈ Iτ} for Odd v. Arena H': Odd v keeps only
  edges to A(v); Even v only the edge to σ(v). τ_new = Odd's optimal counterstrategy (S1 procedure on H', not dual) to σ. Else τ_new = τ.»
- [S4c] [Q docs/new/N5-ssi-global.md@7039eb524:56-57] «c. FALLBACK, if σ_new = σ and τ_new = τ: if Iσ ≠ ∅, for every Even v with an improving
  edge set σ_new(v) = the w with (v, w) ∈ Iσ maximising (Ξσ(w), w) (best valuation, ties: larger index); otherwise do the same for Odd on Iτ
  with G^d's valuations. Count it.»
- [R15d] RESULTS R15 (d): every iteration applies Switch_I (∅ ≠ I ⊆ Iσ) to σ and/or Switch_I (∅ ≠ I ⊆ Iτ) to τ. So every transition changes
  σ or τ.
- [R47a] RESULTS R47 Lemma Φ: at most n(n − 1) transitions of a run change λ and at most n(n − 1) change λ^U.
- [R86] RESULTS R86: λ-run (maximal run of states with λ constant), λ^U-run; ENT_R(v, c) := the transitions t → t + 1 of R (t, t + 1 ∈ R)
  at which σ(v) becomes c; SW_R(v) := Σ_c ENT_R(v, c) (the switches of v in R).
- [DO] R89 draft (P-N5-FRAME, docs/new/P-N5-FRAME-box65.md @ l-new 938d8796, sha1 ce8c4803…; both referees SIGNED; RESULTS entry drafted as
  docs/agents/R89-draft.md, at CHECKER C99): Lemma DUAL-ORDER (§2.2): the [S1-val] triples are the same in G and G^d, and a play is strictly
  better for Even in G iff it is strictly worse for the G^d-Even player in G^d.
- [GPR] R89 draft, Lemma GP*-RUN (§3.3) and the W-run definition (§1). [Q docs/new/P-N5-FRAME-box65.md@938d87967:70-71] «W-RUN: a maximal run
  of consecutive states of one τ-stretch such that no transition t → t + 1 inside it is an S4c fallback or changes λ_W. (σ̄_t and λ_Ξ may
  change inside a W-run.)» [Q docs/new/P-N5-FRAME-box65.md@938d87967:145-146] «and F has at most (n − 1)(R*_T + 1) W-changing transitions,
  R*_T := the transitions of F containing a late adoption» (the late adoption of R88 §4: σ(y) becomes z at a transition of F after (y, z)
  was BLOCKED at an earlier state of F; BLOCKED at t: W_t(z) ▷ W_t(σ_t y) and (y, z) ∉ Iσ_t; R89 §1, R88 §3).
- [SR-λ] R89 draft, STRETCH-RED's proof, λ_W item: [Q docs/new/P-N5-FRAME-box65.md@938d87967:170-172] «λ_W: inside a fallback-free piece of S,
  W_{t+1} ⊵ W_t pointwise (R88 W-MON as in GP*-RUN), the cycle node is the first key component … transitions per piece, and there are fb_S + 1
  pieces.» Used for: at most n(n − 1) λ_W-changing transitions in a fallback-free piece of a τ-stretch.
- The tools' definitions (experiments/new/box64/late.py, L-NEW, copied with a FIRST / REPEAT split as experiments/si/odd/laterep.py):
  [Q experiments/new/box64/late.py@9905dac36:2-3] «late adoptions in W-runs (box 64 §1.8; fallback-free, tau and lambda_W constant) of plain N5,
  S3 start … For each adoption at transition u of an edge (y, z) that was blocked at an earlier state t of the W-run» and
  [Q experiments/new/box64/late.py@9905dac36:21-22] «bl = {(v, x) for v in range(n) if g.owner[v] == 0 for x in g.succ[v] … if x != s[v] and
  Ew.key(w[x]) > Ew.key(w[s[v]]) and (v, x) not in Is}».
- Symbols of this packet.
  - W^τ_t := the [S1-val] valuation of the (σ_t, τ)-plays (G_τ := G with every Odd vertex fixed to τ), compared by [S1-ord]. W_t := W^{τ_t}_t;
    λ_W its cycle-node map. CN^τ_t(v) := the cycle node of W^τ_t(v); v is OFF-CYCLE (for τ, at t) if CN^τ_t(v) ≠ v.
  - H_t := σ_t ∪ Iσ_t ([S4a]'s Even arena; the edges (v, σ_t v) and (v, w) ∈ Iσ_t).
  - An S4a STEP: a transition with Iσ_t ≠ ∅ that is not an S4c fallback and has σ_{t+1} = [S4a]'s σ_new ≠ σ_t (τ_{t+1} may differ).
  - BOUNDARY: a transition that is an Even S4c fallback or changes τ. Fact B (from [S4a]-[S4c], [R15d]): every transition is an S4a step with
    τ_{t+1} = τ_t, or a boundary, or an S4a step with τ_{t+1} ≠ τ_t (also a boundary). [An S4c transition with Iσ ≠ ∅ is Even (changes σ, keeps
    τ); with Iσ = ∅ it is Odd (changes τ). A non-fallback transition with σ_{t+1} = σ_t changes τ by [R15d].]
  - A τ*-PIECE: a maximal run of states [a, b] with τ_t = τ* on it and every transition inside it an S4a step. A GUIDED STRETCH: the same
    thing, read as a stretch (box 37's setting).
  - For a λ-run R and an Even edge (v, c): a LEAVE s → s + 1 (σ_s v = c ≠ σ_{s+1} v), its next RE-ENTRY j − 1 → j (the next transition of R
    with σ_j v = c; s + 1 ≤ j − 1), the OUT-WINDOW [s + 1, j − 1]; span(v, c) := from v's first leave of c in R to its last re-entry into c
    in R (box 38). B_R := the boundaries inside R.

## 2. One-player facts at S4a steps (PROVED)
### Lemma OPT-OFF
At an S4a step t → t + 1, put τ* := τ_t, A := G_{τ*} restricted to H_t (Even keeps H_t's edges, Odd follows τ*), σ′ := σ_{t+1}. Then
(i) σ′ is POINTWISE OPTIMAL for Even in A: W^{τ*}(σ′)(x) ⊵ W^{τ*}(σ″)(x) for every x and every Even strategy σ″ inside H_t; (ii) for every
Even v that is off-cycle for τ* at t + 1 and every (v, y) ∈ H_t: W^{τ*}_{t+1}(y) ⊴ W^{τ*}_{t+1}(σ_{t+1} v).
Proof. (i) [S4a]: σ′ is Odd's optimal counterstrategy in the dual of H to τ*, i.e. it MINIMISES the dual order at every vertex at once
([S1-Xi] applied in the dual); by [DO] the dual order of plays is the reverse of G's, so σ′ maximises G's order at every vertex among
Even strategies in A. (ii) Write W := W^{τ*}(σ′), c := CN(v) ≠ v, and σ″ := σ′ with v → y.
- Since v ≠ c, W(v) = ext(v, W(σ′ v)): the play from v is v followed by σ′ v's play, which avoids v. ext(v, ·) keeps the cycle node,
  adds v to P in both or neither (v's rank against c), and adds 1 to ℓ; between valuations with the same cycle node whose plays avoid v, it
  preserves and reflects ⊴ (and differing cycle nodes are compared by reward, which ext keeps).
- Case 1: v is not on y's σ′-play. σ″'s play from v is v then y's σ′-play: W″(v) = ext(v, W(y)). (i) gives W″(v) ⊴ W(v), reflection
  gives W(y) ⊴ W(σ′ v).
- Case 2: v is on y's path to y's cycle node. Then y's play continues as v's: W(y) = (c, D ⊔ P(σ′ v), ℓ + L), D := the vertices of the
  segment y … v above c, L ≥ 1. σ″ closes the cycle C = v → y → … → v. If D ≠ ∅ with an even top, that top is C's top (rank > c) and W″(v)
  has a better reward than W(v), against (i). So D = ∅ or D's top is odd. D's top odd: W(y) ◁ W(σ′ v). D = ∅, c even: W(y) is longer,
  ◁. D = ∅, c odd: C's top t has rank < c, reward(t) > reward(c), against (i).
- Case 3: v is on y's cycle after c. Then CN(y) = c and P(σ′ v) = ∅ (σ′ v runs along the cycle to c). σ″ closes C = v → y → … → c → … → v.
  If P(y) = ∅, C's top is c and W″(v) = ext(v, W(y)): as in Case 1. Otherwise C's top is t = top of P(y), rank > c; t even gives W″(v)
  better than W(v), against (i); so t is odd and W(y) ◁ W(σ′ v).
- Exhaustive: v on y's play lies on y's path to its cycle node or on its cycle. □
- The off-cycle premise is necessary: red/so/instances/tog6b_n32.pg, vertex 13 = its own cycle node, t = 2 → 3 (box 37 §2; DATA).
### Lemma W-MON′
At an S4a step t → t + 1 with τ* := τ_t: W^{τ*}_{t+1} ⊵ W^{τ*}_t pointwise. Proof: σ_t ⊆ H_t is an Even strategy inside H_t; apply OPT-OFF (i). □
(R88's W-MON is the case τ_{t+1} = τ_t; here τ_{t+1} may differ, the frame is τ_t.)
### Lemma W-SUCC
Let [q, p] be states of one τ*-piece, v Even and off-cycle for τ* at every state of [q + 1, p]. Then W^{τ*}_t(σ_t v) is non-decreasing on
[q, p]. Proof: at t → t + 1, if σ_{t+1} v = σ_t v, W-MON′; else W^{τ*}_{t+1}(σ_{t+1} v) ⊵ W^{τ*}_{t+1}(σ_t v) (OPT-OFF (ii), (v, σ_t v) ∈ H_t)
⊵ W^{τ*}_t(σ_t v) (W-MON′). □

## 3. Lemma W-RETURN-G (PROVED)
Let R be a λ-run, (v, c) an Even edge, s → s + 1 a leave of c and j − 1 → j the next re-entry, and suppose j − 1 → j is an S4a step. Put
τ* := τ_{j−1}, [a, b] the τ*-piece containing j − 1, W* := W^{τ*}. An ANCHOR is a state q with max(s, a) ≤ q − 1 ≤ j − 2 and
(v, c) ∈ H_{q−1}. If an anchor q exists, v is off-cycle for τ* at every state of [q, j], and W*_t(c) is the same for all t ∈ [q, j], then
W*_j(σ_{j−1} v) = W*_j(c).
Proof. q − 1, …, j − 1 lie in [a, b], so q − 1 → q, …, j − 1 → j are S4a steps in the frame τ* (τ_{j} may differ; §2 uses only τ_t).
W*_q(c) ⊴ W*_q(σ_q v) (OPT-OFF (ii) at q − 1 → q) ⊴ W*_{j−1}(σ_{j−1} v) (W-SUCC on [q, j − 1]) ⊴ W*_j(σ_{j−1} v) (W-MON′) ⊴ W*_j(σ_j v) =
W*_j(c) (OPT-OFF (ii) at j − 1 → j with (v, σ_{j−1} v) ∈ H_{j−1}). The ends are equal, so every link is an equality. □
(q = s + 1 with τ constant on [s, j] is box 37's W-RETURN: the leave's own state s is an anchor, σ_s v = c.)

## 4. Corollary CUT-CHARGE (PROVED)
Classes. Every re-entry j − 1 → j of v into c in R is exactly one of: F — j − 1 → j is an Even S4c fallback; FR (FRESH) — an S4a step with
no anchor; C — an anchor exists, q := the smallest, and v is its own cycle node for τ* at some state of [q, j]; P — otherwise, and W*(c)
changes on [q, j]; S — the rest (silent: W*_j(σ_{j−1} v) = W*_j(c) by §3). (j − 1 → j changes σ(v), so by Fact B it is an S4a step or an Even
fallback.) Put FC_R(v, c) := #F + #FR, SIL_R(v, c) := #S, CYC_R(v, c) := #C, and WCH*_R(v, c) := the transitions t → t + 1 inside span(v, c)
with W^{τ_t}_{t+1}(c) ≠ W^{τ_t}_t(c). Then
  ENT_R(v, c) ≤ 1 + FC_R(v, c) + WCH*_R(v, c) + SIL_R(v, c) + CYC_R(v, c),  and  FC_R(v, c) ≤ B_R.
Proof. The first entry of (v, c) in R counts 1; every later entry is a re-entry after a leave. Consecutive re-entries own the disjoint
windows [s + 1, j]. A P re-entry has, inside its window, a transition t → t + 1 (q ≤ t ≤ j − 1, t ∈ [a, b]) with W*_{t+1}(c) ≠ W*_t(c) and
τ_t = τ*: one transition of WCH*, distinct for distinct re-entries. FC: an F re-entry is itself a boundary inside its window's last
transition. An FR re-entry has a > s (otherwise q − 1 = s is an anchor: σ_s v = c, so (v, c) ∈ H_s, and s ≤ j − 2), so a − 1 → a is a
boundary (it ends a τ*-piece: Fact B) inside [s, j − 1]. Windows are disjoint, so distinct F / FR re-entries use distinct boundaries of R. □
Remark (proved in the same way): a second re-entry of the same pair inside one τ*-piece has its own leave s′ ≥ a as an anchor, so #FR ≤ 1
per τ*-piece and pair.

## 5. Lemma FRESH-SPLIT and its ENT bound (PROVED; refinement, not used by §8)
Let j − 1 → j be an FR re-entry, [a, b] ∋ j − 1 its τ*-piece, W* := W^{τ*}. Exactly one of: (WC) W*(c) changes on [a, j]; (G0) W*(c) is
constant on [a, j], W*_j(c) ▷ W*_j(σ_{j−1} v) and j − 1 = a; (CY) as (G0) with j − 1 > a and v its own τ*-cycle node at j − 1 or j;
(LATE) as (CY) with v off-cycle at j − 1 and j; (SAME) W*(c) constant on [a, j] and not W*_j(c) ▷ W*_j(σ_{j−1} v). In case (LATE),
(v, c) is BLOCKED at j − 2 for τ* (W*_{j−2}(c) ▷ W*_{j−2}(σ_{j−2} v), (v, c) ∉ Iσ_{j−2}).
Proof. The five cases partition. (LATE): (v, c) ∉ H_{j−2} (no anchor, j − 2 ≥ a ≥ s + 1 > s), so (v, c) ∉ Iσ_{j−2}; and W*_{j−2}(c) = W*_j(c) ▷
W*_j(σ_{j−1} v) ⊵ W*_{j−1}(σ_{j−1} v) (W-MON′) ⊵ W*_{j−1}(σ_{j−2} v) (OPT-OFF (ii) at j − 2 → j − 1, (v, σ_{j−2} v) ∈ H_{j−2}, v off-cycle at
j − 1) ⊵ W*_{j−2}(σ_{j−2} v) (W-MON′). □
ENT bound: ENT_R(v, c) ≤ 1 + BA + WCH*_R(v, c) + LATE + SIL + CYC + CY, with BA := #F + #G0 + #SAME and LATE := #(LATE) (the (WC) re-entries
join the P ones in WCH*, windows disjoint). BA + LATE + CY ≤ FC ≤ B_R by §4.

## 6. Lemma LATE-SPLIT and Corollary R*-REP (PROVED)
Setting: a W-run F ([GPR]); late adoption and BLOCKED as in [GPR] / the tool quotes. A late adoption of (y, z) in F is FIRST if it is
the first late adoption of (y, z) in F, REPEAT otherwise; REP_F := the REPEAT late adoptions in F.
(i) #FIRST in F ≤ m_E. (ii) Let u₁ < u₂ be consecutive late adoptions of (y, z) in F (transitions u₁ → u₁ + 1, u₂ → u₂ + 1). Then y leaves z
at a transition k → k + 1 with u₁ < k < u₂, and, if y is off-cycle (for F's τ) at every state of [k + 1, u₂ + 1], either W(z) changes on
[k + 1, u₂ + 1] or the adoption is W-SILENT: W_{u₂+1}(σ_{u₂} y) = W_{u₂+1}(z). (iii) If moreover (y, z) is blocked at some state t with
k < t ≤ u₂, then W_t(z) ▷ W_{k+1}(z) (a strict rise before t).
Proof. (i) one per Even edge. F has no fallback and τ constant, so its transitions are S4a steps with τ_{t+1} = τ_t ([GPR]'s W-run, Fact
B), and W = W^τ on F. (ii) σ_{u₁+1}(y) = z ≠ σ_{u₂}(y) (u₂ adopts z), so y leaves z at some k with u₁ < k < u₂. Chain: W_{k+1}(z) ⊴ W_{k+1}(σ_{k+1} y)
(OPT-OFF (ii) at k → k + 1, (y, z) ∈ σ_k ⊆ H_k) ⊴ W_{u₂}(σ_{u₂} y) (W-SUCC) ⊴ W_{u₂+1}(σ_{u₂} y) (W-MON′) ⊴ W_{u₂+1}(z) (OPT-OFF (ii) at u₂ → u₂ + 1,
(y, σ_{u₂} y) ∈ H_{u₂}). If W(z) is constant on [k + 1, u₂ + 1], the ends agree and every link is an equality: W-silent. (iii) W_{k+1}(z) ⊴
W_{k+1}(σ_{k+1} y) ⊴ W_t(σ_t y) (W-SUCC on [k + 1, t]) ◁ W_t(z) (blocked at t). □
Remark. The late-adoption definition ([GPR], the tool's `last` set) needs only SOME earlier blocked state of F, possibly before u₁; so (iii)'s
hypothesis is not automatic, and (ii) is the general form (box 37's W-RETURN inside F). DATA: no W-silent REPEAT occurs (§9).
Consequence: #REPEAT_F(y, z) ≤ WCH_F(z) + SIL_F(y, z) + CYC_F(y, z), SIL_F / CYC_F := the W-silent REPEATs of (y, z) / those with y its own cycle node somewhere on [k + 1, u₂ + 1] (the intervals [k + 1, u₂ + 1] of consecutive adoptions are disjoint).
Corollary R*-REP. R*_T(F) ≤ #late adoptions in F ≤ m_E + REP_F. (R*_T counts transitions containing a late adoption.) □

## 7. Lemma WV-R (PROVED)
Let Q be a guided stretch (a τ*-piece read on its own), Λ_Q := its transitions that change λ_W, R*_Q := the largest R*_T(F) over the W-runs
F inside Q, REP*_Q := the largest REP_F. For every vertex w, WCH_Q(w) := the transitions of Q at which W(w) changes satisfy
  WCH_Q(w) ≤ Λ_Q + (Λ_Q + 1)·(n − 1)(R*_Q + 1) ≤ Λ_Q + (Λ_Q + 1)·(n − 1)(m_E + REP*_Q + 1),   Λ_Q ≤ n(n − 1).
Proof. Q has no fallback and τ constant, so the W-runs inside Q are the pieces of Q between its λ_W-changing transitions: at most Λ_Q + 1.
Each has at most (n − 1)(R*_T + 1) W-changing transitions ([GPR]); the Λ_Q cut transitions add at most Λ_Q. Λ_Q ≤ n(n − 1) by [SR-λ] (Q is
a fallback-free piece of a τ-stretch). The second form is §6. □

## 8. Theorem CUT-RED and Corollary CUT-POLY (PROVED)
Definitions (all maxima over the λ-runs R, λ^U-runs R′ and guided stretches Q of the run):
- B* := max_R B_R (boundaries inside a λ-run: Even fallbacks and τ-changing transitions).
- REP* := max_F REP_F over all W-runs F of the run.
- SC* := max_R Σ_{(v, c)} (SIL_R(v, c) + CYC_R(v, c)) over Even edges.
- O* := max_{R′} the transitions t → t + 1 of R′ (t, t + 1 ∈ R′) at which τ changes.
- K(n, m_E, r) := n(n − 1) + (n(n − 1) + 1)(n − 1)(m_E + r + 1) (§7's per-stretch bound).
Theorem CUT-RED. Every N5 run on every game has
  T ≤ 2n(n − 1) + (n(n − 1) + 1)·( m_E·[1 + B* + B* + (B* + 1)·K(n, m_E, REP*)] + SC* + O* ).
Proof.
- (Bookkeeping, as in R86 Corollary COMPOSE-RUN.) At most 2n(n − 1) transitions change λ or λ^U ([R47a]). Every other transition lies inside
  one λ-run R and one λ^U-run R′ and changes σ or τ ([R15d]); if σ, it is counted in Σ_v SW_R(v) ≥ 1; if τ, it is one of R′'s τ-changing
  transitions. There are at most n(n − 1) + 1 λ-runs and as many λ^U-runs. So T ≤ 2n(n − 1) + (n(n − 1) + 1)(E* + O*), E* := max_R Σ_v SW_R(v).
- Σ_v SW_R(v) = Σ_{(v, c) Even edge} ENT_R(v, c); a term with ENT_R(v, c) = 0 contributes 0; at most m_E terms remain. By §4, each is
  ≤ 1 + B_R + WCH*_R(v, c) + SIL + CYC.
- WCH*_R(v, c) ≤ B_R + (B_R + 1)·K. Each counted transition t → t + 1 lies in span(v, c) ⊆ R and is either a boundary (≤ B_R) or an S4a step
  with τ_{t+1} = τ_t, i.e. a transition inside a guided stretch Q at which W(c) changes (W^{τ_t} = W on Q). The guided stretches meeting R are
  separated inside R by boundaries (Fact B): at most B_R + 1 of them, each contributing at most WCH_Q(c) ≤ K(n, m_E, REP*) (§7).
- Summing: E* ≤ m_E·[1 + B* + B* + (B* + 1)K] + SC*. □
Corollary CUT-POLY (the conditional). If, for some polynomial p, every run on every game has [P-B] B* ≤ p(n), [P-REP] REP* ≤ p(n),
[P-SC] SC* ≤ p(n) and [P-ODD] O* ≤ p(n), then T ≤ q(n) for a polynomial q (about n² · m_E · p · n³ m_E p): G-N5-TIME's iteration half. □
Notes on the premises (what implies them; READING, not signed):
- [P-B] ⇐ (Even fallbacks per phase ≤ p₁(n), e.g. via RESULTS R56's ρ or FB-LIN) ∧ (τ-changing transitions per λ-run ≤ p₂(n)), since a
  λ-run's phases are separated by its τ-changes and its Even fallbacks are in-phase.
- [P-ODD] is the Odd half; R89 COMPOSE-FREEZE (d) bounds the τ-changing transitions of the whole run through P^U on unprotected targets.
- [P-REP]: CONJECTURE REP-LIN (REP_F ≤ n). [P-SC]: open; SIL and CYC are rare in data.
- Compared with R89 STRETCH-RED: R* is replaced by m_E + REP (§6), and FL_S (W-flat σ-changes) by SIL + CYC (re-entries only).

## 9. READING and DATA (NOT to sign); pinned checks
- DATA (719 games of experiments/si/odd/sbcg.lst, S3 start; outputs in experiments/si/odd/out/):
  - cuts.py: 11,669 re-entries; old-τ frame (FR=1, §3 as stated): F 557, FR 6,031, C 4, P 5,035, S 42; W-RETURN-G failures 0; FC ≤ 4 per
    pair per λ-run (0.125n), B per span ≤ 25 (0.52n).
  - cutsx.py (§5): of the 6,031 FR: WC 3,925, G0 1,787, LATE 313, CY 1, SAME 5; LATE-claim failures 0.
  - laterep.py (§6): 1,141 late adoptions, FIRST 1,100, REPEAT 41; REPEATs without a W-rise of z since the leave (off-cycle; i.e. W-silent) 0; most REPEATs in one game 6.
  - hntop_N (N = 2..8; frozen.py --wrun, L-NEW): one guided stretch, 4N λ_W-cuts, max R* = 0; W-changes Θ(N²) come from λ_W (§7 with R* = 0).
  - L-RED's spanobs_K12_m48 and carryobs_K12_m48 (R123): 1,077 and 1,609 re-entries, all class P; FC 0.
- Pinned (experiments/si/check.sh «box 40», «box 42», «box 43»): cuts.py on rise_thin51_n40 (classes) and on fc_3 (FR=1), the controls
  MUT=nofresh (anchor across a cut: fires 16) and MUT=off1 (empty anchor: fires 92); cuts.py on spanobs / carryobs; cutsx.py on rise_thin51
  (FR split); laterep.py on so_th_n32 and rise_thin51 (FIRST / REPEAT); frozen.py --wrun on hntop_n3 (R* 0); this file's quotes
  (quotecheck.py, and --mut must fail).

## DONE / FINDINGS / NEEDS
- DONE: this packet, frozen at its push (boxes 40-42 restated; §2 includes the proofs of OPT-OFF, W-MON′, W-SUCC).
- FINDINGS: Theorem CUT-RED: T ≤ 2n(n − 1) + (n(n − 1) + 1)(m_E[1 + 2B* + (B* + 1)K(n, m_E, REP*)] + SC* + O*); polynomial iff the four
  counts B*, REP*, SC*, O* are (Corollary CUT-POLY, an implication).
- NEEDS: none from the owner.
