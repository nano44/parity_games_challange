# Box 132 N5-ANCHOR: FL runs settle level by level between Ξ-changes at ODIFF vertices and W-cycle nodes
L-NEW successor 46, 2026-11-01 11:4x-11:5xZ (date -u). Lead brief 11:37Z (STEP 1, box 132). Code: experiments/new/box132/ (anchor.py,
dcyc2.py, runcorp.sh, rundcyc2.sh, a_corpus.txt, d2_corpus.txt, pincheck.sh, pincheck.txt, two default starts). check.sh block
«box 132 ANCHOR». Labels: PROVED (lane), CONJECTURE, READING, DATA, DEAD, OPEN.

## 0. Answer
- (b) done in the asked form, CONDITIONAL on [RULE] (below; on every game a READING, signed only on 𝒞^1O as RESULTS R24 (a)+(b)).
  Theorem FL-ANCHOR (§2): in one FL run, between two changes of the gating data
  G_j := (σ̄_j, Ξ_j on ODIFF_j, Ξ_j on the W-cycle nodes),
  the run has at most CAP := (ℓ* − 1) + Σ_c (|T_c| − 1) ≤ n + m transitions. So
  FL run ≤ CAP · (1 + GCH), GCH = the number of gating changes inside the run.
  In a TWO-FIX window (σ̄ fixed), GCH ≤ Σ_{v ∈ ODIFF ∪ CN} XCH_run(v), and over the window
  FL ≤ CAP · (1 + WCH + Σ_{v ∈ ODIFF ∪ CN} XCH(v)).
  This moves FL onto Ξ-changes at a FIXED small vertex set (the ODIFF Odd vertices and the W-cycle nodes), like the rest of the frontier.
- Between gating changes the dynamics is CASC exactly (R24 (c), lifted): a non-cycle-node Even vertex of level ℓ moves only in the
  first ℓ − 1 transitions of the epoch, and then never again. The CDAG-type blow-up (box 130) can therefore come only from gating
  changes. Consequence for L-RED R177: an exponential FL run needs exponentially many Ξ-changes at ODIFF vertices or W-cycle nodes
  while W stays constant (READING, from the theorem).
- (a) DATA: with the W-cycle source added (dcyc2.py), 13 of the 16 cyclic-D runs have an anchor-carried edge (ODIFF- or W-cycle-carried)
  in every nontrivial SCC. 6 of these are rescued by the W-cycle source alone (kt6_n58, cw11_n24 ×4, u23sw64_n32). The other 3 (tog6a_n32,
  tog6b_n32, u2flat_n32) close only through a W-cycle node's own edges.
  - PROVED (lane) Lemma PREFIX (§2): every upward D-edge out of a non-cycle-node vertex is anchor-carried. DATA: UPNOANCH 0.
  - So every D-cycle uses an anchor-carried edge or an edge out of a cycle node. FL-ANCHOR is the right form of «the charge»: it charges
    epochs, not D-cycles.
- DATA (813 distinct pairs, Erratum E-1): 20 FL runs, 42 FL transitions (τ-stretch level; box 130's 37 counted TWO-FIX windows),
  23 epochs, 0 violations of every predicted item.
  - Gating changes inside FL runs: 3, all Ξ-changes at a W-cycle node (cw11_n24).
  - 0 at ODIFF vertices, 0 σ̄-changes.
  - The longest run (u23sw64_n32, 8) is ONE epoch: 8 ≤ ℓ* − 1 = 9.
- NEEDS (Lead): FL-ANCHOR on every game rests on [RULE] = Lemma R + the choice form of Lemma TB. Both are signed on 𝒞^1O only (R24 (a),
  (b)). Lifting them to every game per L44 would make FL-ANCHOR unconditional on its own premise list.

## 1. Setting and premises
- FL run: consecutive non-fallback transitions j − 1 → j of one τ-stretch with σ_j ≠ σ_(j−1) and W_j = W_(j−1) everywhere, on states
  a..b. Standing premise: 1E-N3 / RESULTS R102 (S4B-OPT) with R57 (σ_j is a pointwise optimum of the arena H_(j−1), where Even x keeps
  R_j(x) := {σ_(j−1)(x)} ∪ {y : Ξ_(j−1)(y) ▷ Ξ_(j−1)(σ_(j−1)(x))} and Odd follows τ).
- W is constant on the run, so these are constant too:
  - the level ℓ(v) := length component of W(v);
  - the set CN of W-cycle nodes (ℓ = 0);
  - for x ∉ CN, T_x := {y ∈ succ(x) : x·W(y) = W(x)}, all of level ℓ(x) − 1;
  - for c ∈ CN, T_c := {y ∈ succ(c) : W(y) has cycle node c}.
- FL-TIGHT (box 130): σ_j(x) ∈ T_x at every state of the run. TIE_j(x) := R_j(x) ∩ T_x is the set of W-optimal arena options.
- Gating data G_j := (σ̄_j on the Odd vertices, Ξ_j on ODIFF_j := {o Odd : σ̄_j(o) ≠ τ(o)}, Ξ_j on CN). An EPOCH is a maximal set of
  consecutive transitions j − 1 → j of the run whose gating states j − 1 carry the same G.
- [RULE] (READING on every game: box 131 §1, DATA 666 / 666 and 8 / 8; SIGNED on 𝒞^1O as RESULTS R24 (a) Lemma R + (b) Lemma TB): for
  every Even x ∉ CN, σ_j(x) is the κ_j-least element of TIE_j(x). Here κ_j(y) is the BFS key K_j(y) (the c-side σ_j/τ path from x's
  cycle node c to y) if c is even, and the index of y if c is odd.
  - K_j(y) depends only on σ_j at Even vertices of level < ℓ(y) + 1 on that path, and on τ.
  - No rule is assumed at cycle nodes. Their choice in the code is a DFS (si.py «v itself»), and §2 (iii) does not need it.

## 2. PROVED (lane)
- Lemma PREFIX. For a state j of the run and y ∉ CN, follow the W_j-play from y until its first vertex A ∈ ODIFF_j ∪ CN. It exists:
  the play reaches the cycle node within ℓ(y) steps.
  - The Ξ_j-play from y has the same prefix up to A. On non-ODIFF Odd vertices σ̄_j = τ, and Even vertices follow σ_j in both plays.
  - Every vertex of the prefix other than y has level < ℓ(y): along a W-play the level drops by 1 per step.
  - Ξ_j(y) = F(p_0 … p_(k−1), Ξ_j(A)): a function of the vertex sequence of the prefix and of the value at A.
  - Proof of the last point: let w be the cycle node in Ξ_j(A). The play from y has the same final cycle, so the same cycle node w.
    - If w is in the prefix, Ξ_j(y) is read off the prefix up to w.
    - Otherwise the path from y to w is the prefix followed by A's path to w. Its relevant-vertex set and length are the prefix's
      contribution plus those recorded in Ξ_j(A). ∎
  - Corollary (D-edges): every D-edge v → u with ℓ(u) ≥ ℓ(v) and v ∉ CN is anchor-carried, i.e. the Ξ-play passes ODIFF or the W-cycle
    node before u.
- Theorem FL-ANCHOR (under the §1 premises and [RULE]). Take an epoch whose first gating state is s0 and last state is s1, and let
  ℓ* := the largest level of an Even vertex ∉ CN.
  - (i) For every ℓ ≥ 1, σ_j restricted to the Even vertices ∉ CN of level ≤ ℓ is constant for j ∈ [s0 + ℓ − 1, s1].
  - (ii) Hence a vertex x ∉ CN moves only at transitions j with j − s0 ≤ ℓ(x) − 1, and always to an option of level ℓ(x) − 1. (On 𝒞^1O
    this is R24 (c) CASC's «level ℓ switches only at run steps ≤ ℓ − 2», 0-based.)
  - (iii) For j ∈ [s0 + ℓ*, s1], only cycle nodes move. Each move of c strictly raises ξ(σ(c)) in a fixed map ξ on T_c, so c makes
    ≤ |T_c| − 1 such moves.
  - (iv) The epoch has ≤ CAP = (ℓ* − 1) + Σ_{c ∈ CN Even} (|T_c| − 1) transitions, and the run has ≤ CAP · (1 + GCH).
  - Proof of (i), by induction on ℓ.
    - ℓ = 1: T_x ⊆ {y : ℓ(y) = 0, cycle node c} = {c}, so σ_j(x) = c at every state.
    - ℓ ≥ 2: take j ∈ [s0 + ℓ − 1, s1]. For y ∈ T_x ∪ {σ_(j−1)(x)}, of level ℓ − 1, Lemma PREFIX writes Ξ_(j−1)(y) through σ_(j−1) at
      levels ≤ ℓ − 1 and Ξ_(j−1) at an anchor. The first is constant by induction, since j − 1 ≥ s0 + ℓ − 2. The second is constant
      because j − 1 ∈ [s0, s1 − 1] and the gating data is fixed, and ODIFF_(j−1) is fixed with σ̄.
    - κ_j on level ℓ − 1 depends on σ_j at levels ≤ ℓ − 1, also constant.
    - So σ_j(x) = f_x(σ_(j−1)(x)), where f_x(z) := κ-least element of ({z} ∪ {y : ξ(y) ▷ ξ(z)}) ∩ T_x, with fixed ξ and κ.
    - f_x is idempotent. Let z' = f_x(z) ≠ z. Then ξ(z') ▷ ξ(z), so the set for z' is contained in the set for z, and it contains z'.
      Since z' is κ-least in the larger set, f_x(z') = z'. κ is injective (last key coordinate, or index).
    - Hence σ_j(x) is constant from j = s0 + ℓ − 1 on. ∎
  - Proof of (iii). For j − 1 ≥ s0 + ℓ* − 1, every y ∈ T_c has Ξ_(j−1)(y) = ξ(y), constant: by Lemma PREFIX (y ∉ CN), or ξ(c) = Ξ(c)
    is gating data when y = c.
    - A move of c at j picks σ_j(c) ∈ R_j(c) \ {σ_(j−1)(c)}, so ξ(σ_j(c)) ▷ ξ(σ_(j−1)(c)).
    - σ_j(c) ∈ T_c, because W(c) is unchanged.
    - A strictly increasing sequence in the finite set ξ(T_c) has ≤ |T_c| − 1 steps. Every FL transition moves someone, and after
      s0 + ℓ* − 1 only cycle nodes can move. ∎
  - (iv) adds (i)–(iii). The epochs number ≤ 1 + GCH. ∎
- Corollary (window form). In a TWO-FIX window σ̄ is fixed, so GCH ≤ Σ_{v ∈ ODIFF ∪ CN} XCH(v). FL runs are separated by W-changing
  transitions, so FL_window ≤ CAP (1 + WCH + Σ_{v ∈ ODIFF ∪ CN} XCH(v)).
- Not used, and not needed: any rule at cycle nodes, Ξ ⊴ W, or one-player structure beyond R_j.

## 3. What this does and does not give
- Does: FL-POLY ⇐ «per W-constant run, Ξ changes polynomially often at ODIFF vertices and W-cycle nodes» (under [RULE]). This is a
  sharper target than XI-CH-POLY over all Even vertices (box 92 XI-RUN, which already bounds the whole W-run by Σ d_E XICH). Here only
  |ODIFF| + |CN| vertices carry the cost, and the in-between dynamics is bounded by n + m.
- Does not: bound XCH at those vertices. Ξ is monotone at every vertex over the window (VJ monotonicity), but the number of distinct
  values is exponential in general.
  - OPEN (DATA: 0 in the 20 corpus FL runs): can Ξ change at an ODIFF vertex inside one FL run at all?
  - The only gating changes seen are Ξ-changes at a W-cycle node that moved itself (cw11_n24: 3 changes, CMXICH 11 / 13 cycle-node
    moves).
- Exact obstruction to an unconditional polynomial FL (READING): an FL run longer than CAP · k needs ≥ k gating changes. A CDAG_n
  embedding (R177) must make Ξ at ODIFF vertices or W-cycle nodes change about 2^n / (n + m) times while W is constant everywhere.
  No such instance is known; the smallest candidate to test is R177's own output.

## 4. DATA (813 distinct pairs; a_corpus.txt, d2_corpus.txt; 0 script errors)
| quantity | value |
| --- | --- |
| FL runs / transitions / epochs | 20 / 42 / 23 |
| level-timing violations (ii) / mover not to level ℓ − 1 | 0 / 0 |
| epochs longer than CAP / runs longer than CAP (1 + GCH) | 0 / 0 |
| gating changes: Ξ at ODIFF / σ̄ / Ξ at W-cycle node only | 0 / 0 / 3 (cw11_n24) |
| cycle-node moves / with Ξ(c) change / after ℓ* − 1 (item iii tested) | 13 / 11 / 0 (item (iii) not exercised by data) |
| longest run, longest epoch | 8, 8 (u23sw64_n32, CAP slack 1 on (ii)'s ℓ* − 1) |
| cyclic-D runs: every SCC ODIFF-carried / anchor-carried / neither | 7 / 13 / 3 (tog6a, tog6b, u2flat: closed by a cycle node's edges) |
| upward D-edges out of non-cycle-node vertices not anchor-carried | 0 |
- Pins (pincheck.txt): u23sw64_n32 (sha1 18b46837d2f0…, default start c69511c1064f… written out) and cw11_n24 (5c6dcf2d9668…, start
  8200da23563c…). Oink 8fbf0a7 --zlk and --tl verified, regions agree, n5b identical state by state (16 / 17 iterations). Starts
  validated (D-ODD-1, strict start_pair).

## 5. Next (Lead decides)
- Referees: lift R24 (a) Lemma R + the choice form of (b) to every game (L44). Then FL-ANCHOR has only R102 / R57 + FL-TIGHT as
  premises.
- L-RED R177: the theorem says where the cost must sit. An exponential FL run needs exponentially many Ξ-changes at ODIFF vertices or
  W-cycle nodes inside one W-constant run. A useful first test: a single FL run with ≥ 1 Ξ-change at an ODIFF vertex (none in the corpus).
- L-NEW: try to bound Ξ-changes at ODIFF vertices inside an FL run. Ξ(o) = o·Ξ(σ̄(o)), so a change needs an FL mover on o's Ξ-play; FL
  movers are value-dirty: their current option's Ξ is strictly below W (since Ξ ⊴ W pointwise and the released
  option is W-tied; a one-line remark, not used in §2).
