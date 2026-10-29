# P-N5-SDPRIME (box 25): two-frame settling. On a σ̄-constant stretch of one phase whose end-state cycles (W and honest, separately) persist, the run settles along the end state's plays within |Even ∖ (T_W ∪ T_H)| ≤ n − 1 transitions (STATIC-DEPTH′, extending RESULTS R77 (c)); a σ̄-constant piece has ≤ (CF + 1)·n − 1 transitions, CF its cycle appearances (EPOCH)
L-SI successor 21 (Opus 5.5; D18, Lead reading L40). Packet for the referees, FROZEN at its push; the sha1 goes to the Lead; repairs go in a NEW
file docs/si/P-N5-SDPRIME-fixes-box25.md. Lead 2026-10-29 03:28Z: «File: docs/si/P-N5-SDPRIME-box25.md. To sign: Theorem STATIC-DEPTH′ (with
(H3′), (H4′), GEN_W) and Corollary EPOCH.» Working note with data: docs/si/N5-PIECE-box25.md (l-si 6bb0ec34). Labels (D18 / L40): PROVED (lane,
unrefereed) / CONJECTURE / OPEN / DATA.
SCOPE (D1): structural lemmas about N5 inside one phase. Not a TARGET.md claim, not an algorithm claim, no running-time bound; G-N5-TIME stays
OPEN. NOTHING HERE DEPENDS ON AN UNLANDED PACKET: the premises are LANDED RESULTS entries and the SPEC text, quoted below.
Quotes: every [Q path@commit:lines] «…» is verbatim from the tagged source, checked by experiments/si/rund/quotecheck.py (pinned in
experiments/si/check.sh with a shifted-line control that must fail).

## 0. What to sign, and what not
| § | statement | label |
| --- | --- | --- |
| §2 | Theorem STATIC-DEPTH′ (N5, every game; hypotheses (H1′), (H2), (H3′), (H4′), GEN_W) | PROVED (to sign) |
| §2 | Remark: STATIC-DEPTH′ contains RESULTS R77 (c) | PROVED (to sign) |
| §3 | Corollary EPOCH (with (H4′) and GEN_W at every epoch end) | PROVED (to sign) |
| §4 | data, CONJECTURE PIECE, CONJECTURE STATIC-DEPTH′-TIE | DATA / CONJECTURE (NOT to sign) |

## 1. Setting and premises (all LANDED)
- SPEC docs/new/N5-ssi-global.md. Valuations: [Q docs/new/N5-ssi-global.md@55e0bcbda:28-29] «valuation of v under (σ, σ̄): (c, P, ℓ), c = the
  most relevant (max p') vertex of the cycle the play from v ends in, P = set of vertices on the play before reaching c with p' > p'(c), ℓ =
  number of steps to reach c.» A valuation is a function of the play. The order: [Q docs/new/N5-ssi-global.md@55e0bcbda:30-31] «order (better
  for Even): compare reward of c (p'(c) if even, −p'(c) if odd); then P by the signed weight Σ_{u∈P} (+2^rank(u) if Ω(u) even else
  −2^rank(u)); then ℓ» — p′ is injective and the signed weights of distinct sets differ, so the order is TOTAL on valuations.
  Improving edges: [Q docs/new/N5-ssi-global.md@55e0bcbda:47] «Iσ = {(v, w) : owner(v) = Even, w ≠ σ(v), Ξσ(w) strictly better than
  Ξσ(σ(v))}».
- S4a: [Q docs/new/N5-ssi-global.md@55e0bcbda:51] «A(v) = {σ(v)} ∪ {w : (v, w) ∈ Iσ} for Even v» and [Q docs/new/N5-ssi-global.md@55e0bcbda:53]
  «(Even's one-player optimum against τ among "keep or take an improving edge".)». S4c: [Q docs/new/N5-ssi-global.md@55e0bcbda:56] «FALLBACK,
  if σ_new = σ and τ_new = τ».
- Pointwise optimality of S4a's step over the strategies using arena edges: RESULTS R18 (d) Lemma S (a), [Q docs/RESULTS.md@55e0bcbda:804] «U_τ
  the pointwise maximum of V_{σ',τ} over Even's σ'», applied to S4a's arena game (the standing premise P2 as listed in RESULTS R69:
  [Q docs/RESULTS.md@55e0bcbda:3596] «P2: S4a's step is Even's optimum in its arena»).
- (SW), as listed among RESULTS R72's landed premises: [Q docs/RESULTS.md@55e0bcbda:3768-3769] «(SW): every Even switch of N5 is to an edge … of Iσ».
- RESULTS R77 (c)'s signed proof steps: [Q docs/RESULTS.md@55e0bcbda:4204-4205] «(W-MONO) W_{t+1} ⊵ W_t (P2), (Ξ-SUCC) Ξ_t(σ_t v)
  non-decreasing ((M2κ), (SW))», on in-phase S4a transitions (R77's (H1); neither step uses (H2)-(H4)). GEN_W as in R77 (c):
  [Q docs/RESULTS.md@55e0bcbda:4202] «GEN_W (for every v, different W-plays from v to the same cycle have different W-valuations)».
- RESULTS R80 (a): [Q docs/RESULTS.md@55e0bcbda:4433] «(a) (C1) EVERY-SWITCH (§2): at every transition t → t+1 of a phase, σ_{t+1} ≠ σ_t.»
- Notation. Ξ_t(v): the valuation of v's honest play (σ_t at Even vertices, σ̄_t at Odd vertices); W_t(v): that of v's (σ_t, τ)-play. A
  W-cycle (honest cycle) at t: a cycle of the successor map v ↦ σ_t(v) / τ(v) (v ↦ σ_t(v) / σ̄_t(v)), as a vertex sequence up to rotation. A
  vertex on a cycle of a successor map has that cycle as its play. For v not on its play's cycle, val(v) = v ⊕ val(next v) (S1).

## 2. Theorem STATIC-DEPTH′ (PROVED, lane)
Hypotheses on states [a, b] of one phase:
- (H1′) every transition t → t + 1, a ≤ t < b, is an S4a step (no fallback); τ and λ are constant on [a, b]. (λ_W need not be constant.)
- (H2) σ̄_t = σ̄_a for t ∈ [a, b].
- (H3′) every W-cycle at b is a W-cycle at every t ∈ [a, b], and every honest cycle at b is an honest cycle at every t ∈ [a, b]. T_W / T_H :=
  the vertices of the W-cycles / honest cycles at b; T := T_W ∪ T_H. (The two frames' cycles may differ, and other cycles may come and go.)
- Depths: dW(v) := 0 for v ∈ T_W; dH(v) := 0 for v ∈ T_H; Odd v: dW(v) := dW(τ v) (v ∉ T_W), dH(v) := dH(σ̄ v) (v ∉ T_H); Even v ∈ T_H ∖ T_W:
  dW(v) := dW(σ_b v); Even v ∈ T_W ∖ T_H: dH(v) := dH(σ_b v); Even v ∉ T: dW(v) := dH(v) := d(v) := 1 + max(dW(y), dH(y)), y := σ_b(v).
- (H4′) this recursion is well founded. Equivalently: the graph J_b on the Even vertices outside T, with an edge v → v′ when v′ is the first
  Even vertex outside T after v on v's W-play at b or on v's honest play at b, is acyclic. (A cycle of the recursion that meets no Even
  vertex outside T would be a cycle of one frame's successor map at b outside that frame's end-state cycles, which does not exist.)
- GEN_W.
Claim. Every v has its W-play at b at every t ∈ [a + dW(v), b] and its honest play at b at every t ∈ [a + dH(v), b]. Hence σ_t = σ_b on
[a + max d, b], and b − a ≤ max d ≤ |Even ∖ T| ≤ n − 1, the max over Even v ∉ T (0 if there is none).
Proof. "v W-settled from s": v's W-play at every t ∈ [s, b] is its W-play at b; "H-settled" likewise with honest plays. Induction along the
well-founded recursion.
1. v ∈ T_W lies on a W-cycle Z at b; Z is a W-cycle at every t (H3′), so v's W-play at every t is Z from v: W-settled from a. Likewise
   v ∈ T_H is H-settled from a. An Even v ∈ T has σ_t(v) = its successor on that cycle = σ_b(v) for every t ∈ [a, b].
2. Odd v ∉ T_W. Its (σ_t, τ)-successor is τ(v) at every t. If τ(v) is W-settled from s, then for t ∈ [s, b] τ(v)'s W-play is its W-play at b,
   which does not contain v (v ∉ T_W, so v's W-play at b is v followed by τ(v)'s, simple up to a cycle not through v); so v's W-play at t is
   v followed by it, its W-play at b: v is W-settled from a + dW(τ v). Odd v ∉ T_H: the same with σ̄(v), constant by (H2), and honest plays.
3. Even v ∈ T_H ∖ T_W: σ_t(v) = σ_b(v) =: y for all t (item 1), and item 2's argument with y gives W-settled from a + dW(y). Even v ∈ T_W ∖ T_H:
   H-settled from a + dH(y) the same way.
4. Even v ∉ T, y := σ_b(v), y W-settled from a + dW(y) and H-settled from a + dH(y); s := a + max(dW(y), dH(y)).
   (A) For t ∈ [s, b], y ∈ {σ_t v} ∪ Iσ_t(v). Otherwise σ_t(v) ≠ y and, the order being total, Ξ_t(y) ⊴ Ξ_t(σ_t v). As σ_b(v) = y, v switches
       to y at some t′ → t′ + 1 with t ≤ t′ < b. By (SW), Ξ_{t′}(y) ▷ Ξ_{t′}(σ_{t′} v) ⊵ Ξ_t(σ_t v) ⊵ Ξ_t(y) = Ξ_{t′}(y) (Ξ-SUCC; y H-settled and a
       valuation is a function of the play). Contradiction.
   (B) For t ∈ [s, b − 1] let s′ := σ_{t+1} with v's choice set to y. By (A) and S4a, s′ uses arena edges of state t. y's W-play under σ_{t+1} is
       its W-play at b (W-settled, t + 1 ≥ s), which does not contain v (v ∉ T_W); so it is also y's play under s′, and W_{s′}(v) = v ⊕ W_b(y) =
       W_b(v). Pointwise optimality (§1) gives W_{t+1}(v) ⊵ W_b(v); W-MONO from t + 1 to b gives W_{t+1}(v) ⊴ W_b(v). So W_{t+1}(v) = W_b(v).
   (C) The cycle node c of W_b(v) lies on a W-cycle Z at b; Z is a W-cycle at t + 1 (H3′), so c's W-play at t + 1 is Z. W_{t+1}(v) has cycle
       node c, so v's W-play at t + 1 reaches c and then follows Z: it ends in the same cycle as v's W-play at b. By GEN_W the two plays are
       equal. So σ_{t+1}(v) = y, and v's honest play at t + 1 is v followed by y's honest play at t + 1, which is y's honest play at b (y
       H-settled) and avoids v (v ∉ T_H): v's honest play at b. v is W- and H-settled from s + 1 = a + d(v).
5. Length. For t ≥ a + max d, every Even v ∉ T has σ_t(v) = σ_b(v) (the first step of its settled W-play) and every Even v ∈ T has it by
   item 1: σ_t = σ_b. If b > a + max d, the transition a + max d → a + max d + 1 of the phase leaves σ unchanged, against R80 (a) EVERY-SWITCH.
   So b − a ≤ max d. A J_b-path visits distinct Even vertices outside T (H4′) and d(v) is the number of vertices of a longest J_b-path from v,
   so max d ≤ |Even ∖ T| ≤ n − 1 (T ≠ ∅: every play ends in a cycle). □
Remark (contains R77 (c)). Under R77's (H1)-(H4): (H1) gives (H1′); (H3) gives (H3′) with T_W = T_H = the common cycle vertices; a J_b-edge
v → v′ then follows σ_b at Even vertices and τ or σ̄ at Odd ones through vertices outside T, i.e. it is a path of R77's H_b, so a J_b cycle
would be an H_b cycle and (H4) gives (H4′); and d(v) ≤ R77's d*(v) (both count the Even non-cycle vertices of a path, J_b's paths being H_b's).
So R77 (c)'s bound follows from STATIC-DEPTH′. What is new: the W- and honest cycles may differ, cycles other than the end state's may come
and go, and λ_W may change.

## 3. Corollary EPOCH (PROVED, lane; a REDUCTION)
- A PIECE: a maximal stretch [a, b] of states of a fallback-free run of one phase on which σ̄ is constant (so (H1′), (H2) hold on it).
- Epochs: b_k := b; a_k := the least state of [a, b_k] such that every W-cycle (honest cycle) of state b_k is a W-cycle (honest cycle) at every
  state of [a_k, b_k]; then b_{k−1} := a_k − 1, and so on down to a. This cuts [a, b] into epochs [a_1, b_1], …, [a_k, b_k] (an epoch may be one
  state), each satisfying (H1′), (H2), (H3′) with end state b_i, by construction.
- CF := the transitions t → t + 1 of [a, b] at which a cycle appears: some W-cycle (honest cycle) of state t + 1 is not a W-cycle (honest cycle)
  of state t.
Claim. If (H4′) and GEN_W hold at every epoch end b_i, then |[a, b]| = b − a = Σ_i (b_i − a_i) + (k − 1) ≤ k(n − 1) + k − 1, and k − 1 ≤ CF; so
b − a ≤ (CF + 1)·n − 1.
Proof. Theorem STATIC-DEPTH′ on each epoch gives b_i − a_i ≤ n − 1. For i ≥ 2, a_i > a and the minimality of a_i give a cycle Z of state b_i
that is a cycle of its frame at every state of [a_i, b_i] but not at a_i − 1; so Z is a cycle at a_i and not at a_i − 1: it appears at the
transition a_i − 1 → a_i. These k − 1 transitions are distinct. □
- So CONJECTURE PIECE (b − a ≤ n − 1 for every piece) reduces to the pieces with CF ≥ 1; nothing here bounds CF.

## 4. NOT to sign: data and conjectures (details in docs/si/N5-PIECE-box25.md)
- DATA (experiments/si/piece/sdprime.py; one engine, n5x): STATIC-DEPTH′'s hypotheses hold on 844 of 872 alt_all pieces (R77's: 708), 914 /
  943 lib41, 940 / 1,080 random 𝒞^kO; 0 violations of the per-vertex settling, of b − a ≤ max d, of b − a ≤ n − 1; the MUT=1 control (d − 1)
  fails 912 / 74 times. EPOCH (piece/epochs.py): ≤ 6 epochs and CF ≤ 5 per piece, 0 violations.
- CONJECTURE PIECE (unconditional): every piece has ≤ n − 1 transitions. OPEN. Pieces outside STATIC-DEPTH′ are short in data (≤ 0.43(n − 1) in
  alt_all); a climb found none above 0.71(n − 1).
- CONJECTURE STATIC-DEPTH′-TIE: STATIC-DEPTH′ without GEN_W. 22 pieces with a GEN_W failure in the data, conclusion intact.
