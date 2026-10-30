# P-N5-SETTLE (packet, box 52): inside every W-run F of N5, every stretch with no σ̄-change, no switch at a W-cycle node and no Ξ-change at an upward head has ≤ n − 1 transitions (Theorem RUN-SETTLE), so |F| ≤ n(E_F + 1) − 1 and polynomial W-runs ⇔ polynomial per-vertex σ̄-changes, W-cycle-node switches and head Ξ-changes (Theorem HEAD-RED). Plus Corollary T-XCH, a one-line composition of landed R86 (a) and R15 (d)
L-SI successor 34 (Opus 5.5), D18. Lead 2026-10-30 18:14Z: «FREEZE a small packet P-N5-SETTLE for the referees … Theorem RUN-SETTLE,
Theorem HEAD-RED and Claim RG′, quoting L-RED R143's Lemma SETTLE verbatim (l-red 717f407a) with your proof's dependence on it explicit.
Also RETURN-CHARGE′-O / SEG-XCH-O / Corollary T-XCH, if it is cheap to include. Use L-NEW's packet format …». FROZEN 2026-10-30 (this
commit; the sha1 is reported to the Lead). Written 18:15Z-18:4xZ (date -u).
- Source: docs/si/N5-HEADS-box52.md (working note, l-si 71d1d0ac). Where the two differ, THIS packet governs.
- Status: REDUCTIONS and one EQUIVALENCE. No residual is bounded here. G-N5-TIME stays OPEN. This is not M3, not a step-4 pass, and not a
  TARGET.md claim.
- Object: N5 only (SPEC S1-S5).

## 0. What to sign
| § | item | origin | label |
| --- | --- | --- | --- |
| 3 | Claim RG′ (L-SI box 51b §10.1 Claim RG, at every S4a step of a W-run) | L-SI, new | PROVED (to sign) |
| 4 | Lemma PLAY-CAUSE; facts W-MON, PATH | L-SI, new (PLAY-CAUSE restates R143 (A)'s play argument) | PROVED (to sign) |
| 5 | Theorem RUN-SETTLE; Corollary RUN-COUNT | L-SI, new | PROVED (to sign) |
| 6 | Theorem HEAD-RED | L-SI, new | EQUIVALENCE (to sign) |
| 7 | Corollary T-XCH (landed R86 (a) SW-RETURN, both sides, composed with R15 (d)) | landed + one-line composition | EQUIVALENCE; only the one-line composition is new (to sign, trivial) |
| 2 | R140 ARENA-MAX (L-RED); T54 LEX-BFS / IDX-MONO (L-LIT); R143 events and SETTLE (L-RED) | other lanes, quoted | premises as their lanes state them. LEX-BFS / IDX-MONO are used ONLY in Case 2a of §5; to sign as used there |
| 8 | CONJECTURES (FLIP-EV, HX-POLY, CN-POLY, XCN-POLY) | — | NOT to sign |
| 9 | DATA, DEAD, READING | — | NOT to sign |

## 1. Setting and landed premises
- N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md; FIX 1-4 as in RESULTS), on any parity game.
  - V = {0, …, n − 1}, n := |V|. n_O := the number of Odd vertices.
  - m_E (m_O) := the number of edges leaving Even (Odd) vertices. d_E(d) (d_O(d)) := the number of Even (Odd) vertices with an edge to d.
- Priorities are injective after SPEC's re-ranking: p′(v) = 2·rank(v) + parity (si.py header).
  - reward(v) := p′(v) if v is even, −p′(v) if v is odd.
  - v is MORE RELEVANT than w iff p′(v) > p′(w).
- A run is the sequence of states (σ_k, τ_k), and a TRANSITION is k → k + 1. Even y SWITCHES at k if σ_(k+1)(y) ≠ σ_k(y).
- Values x = (c, P, ℓ):
  - cycle node λ(x) = c, path set P (the vertices of the path to c that are more relevant than c), length ℓ.
  - ⊴ / ◁ / ⊵ / ▷: the SPEC S1 order, better for Even. First reward(c). Then, for one c, P by its most relevant vertex of the
    symmetric difference (better for Even iff that vertex is even). Then ℓ: for one c and P, a longer ℓ is better iff c is odd.
  - For a vertex y ≠ c, y ⊕ (c, P, ℓ) := (c, P ∪ ({y} if y is more relevant than c), ℓ + 1).
  - On values with one cycle node c, y ⊕ · preserves and reflects ⊴ and ◁.
- Valuations:
  - Ξ_k := the [S1-val] valuation of the (σ_k, σ̄_k)-plays, σ̄_k := SPEC S1's Odd counterstrategy to σ_k;
  - W_k := the valuation of the (σ_k, τ_k)-plays;
  - val(ρ, τ) := the valuation of the (ρ, τ)-plays;
  - ℓ_k(x) := the length of W_k(x), i.e. the length of the (σ_k, τ_k)-path from x to its cycle node λ_W(x);
  - Iσ_k := {(y, z) : Ξ_k(z) ▷ Ξ_k(σ_k(y))} (SPEC S2);
  - H_k := S4a's arena at k: Even v keeps {σ_k(v)} ∪ Iσ_k(v), Odd follows τ_k;
  - W_k-TIGHT edge (y, z) at Even y with λ_W(y) ≠ y: y ⊕ W_k(z) = W_k(y).
- W-run, RESULTS R89 verbatim: «a τ-stretch := a maximal run of consecutive states with τ constant; a W-run := a maximal run of
  consecutive states of one τ-stretch none of whose transitions is an S4c fallback or changes λ_W».
  - In a W-run F, τ_k =: τ and C := {v : λ_W(v) = v} are fixed.
  - Every transition of F switches some Even vertex: with τ fixed and no S4c fallback, S4a changed σ (SPEC S4).
  - Odd vertices in W-plays follow τ; D_k := {Odd o : σ̄_k(o) ≠ τ(o)}.
- [R57], standing SPEC premise (RESULTS R57, as quoted in RESULTS R91 / R93): «1E-N3: S1's procedure realises the pointwise optimum; for
  S4a, σ_new is the pointwise optimum of the one-player arena H_t». §3 and §5 use it, as R88-R93 do.
- [R15], RESULTS R15 (a), (d), signed:
  - «(a) Lemma A: for any non-empty unambiguous set I of improvements of σ (VJ00 §4.4), Ωσ ⊴ Ω_{Switch_I(σ)}»;
  - «(d) N5: every iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ (on G) and/or with ∅ ≠ I ⊆ Iτ to Odd's τ (on G^d), and changes at
    least one of them».
  - Hence Ξ_(k+1) ⊵ Ξ_k pointwise at every transition.

## 2. Other lanes' lemmas, quoted verbatim (not re-signed here unless the Lead routes them)
- L-RED R140 §2 (docs/red/R140-friedmann-port.md, on claude/l-red), Lemma ARENA-MAX:
  «Let H_t be the arena of S4a at state t: Even v restricted to {σ_t(v)} ∪ Iσ_t(v), Odd fixed to τ_t. Then for every vertex v and every
  Even strategy ρ of H_t: W_(t+1)(v) ⊵ val(ρ, τ_t)(v), with W_(t+1) := val(σ_(t+1), τ_t). Proof. σ_(t+1) is Even's pointwise optimal
  strategy in the one-player game H_t (SPEC S4a: Odd's optimal counterstrategy on the dual of H_t, i.e. VJ00's simultaneous optimum). □»
  (= [R57] for S4a.)
- L-LIT T54 §4.1-§4.2 (docs/lit/T54-stalling.md, l-lit 96cfda95), «PROVED, L-LIT, elementary, modulo Claim RG»:
  - IDX-MONO: «If Even v ≠ c := λ_W(v) and Ω(c) is odd, then σ_{k+1}(v) = the smallest-index W-tight edge of {σ_k(v)} ∪ Iσ_k(v).»
  - Key: «key_σ(x) := (x_{ℓ−1}, …, x_1, x_0), where x = x_0 → x_1 → … → x_ℓ = c is the (σ, τ) path … Keys are compared
    lexicographically.»
  - LEX-BFS: «If Ω(c) is even and v ≠ c is Even, then σ_{k+1}(v) = argmin over the W-tight arena edges y of key_{σ_{k+1}}(y).»
  - Proofs (T54 §4.1-§4.2, quoted): «The recursion «for y in hs[x]: if d > best» over the sorted remaining successors returns the first
    maximum. By Claim RG these are the tight arena edges, all of maximal length.» / «BFS layer j+1 is built by scanning layer j in queue
    order and appending undiscovered predecessors in increasing index. By induction on j, queue order within a layer is lexicographic
    order of keys … A vertex is discovered from the first queued tight successor, i.e. the lex-least one (Claim RG).»
  - T54 states these inside a W-constant interval, where W_k = W_(k+1). This packet uses them at an arbitrary transition k → k + 1 of a
    W-run, with «W-tight» meaning W_(k+1)-tight and the keys read on (σ_(k+1), τ)-paths. Their proofs are about one S4a evaluation and use
    only Claim RG, which §3 supplies in that form (RG′). That reading is part of what §5 asks to be signed.
- L-RED R143 (docs/red/R143-settle.md §0-§1, l-red 717f407a), verbatim:
  - «UPWARD HEADS: U_k := {σ̄_k(g) : g Odd, σ̄_k(g) ≠ τ(g)} ∪ {the Ξ-successor of c (σ_k(c), or σ̄_k(c) if c is Odd) : c ∈ C}.»
  - «EVENT: a transition k → k + 1 of I at which (i) σ̄ changes, or (ii) σ changes at some Even c ∈ C (a CN switch), or (iii) Ξ changes at
    some vertex of U_k ∪ U_(k+1). E_I := the number of events. A WINDOW is a maximal run of states of I with no event between
    consecutive ones.»
  - Lemma SETTLE: «|I| ≤ (D + 1)(E_I + 1) − 1 … (A) Downward dependence. For a state k of I and a vertex y with layer(y) = d, Ξ_k(y) is a
    function of σ_k on the Even vertices of layers ≤ d, of σ̄_k, and of Ξ_k on U_k. … (B) Settling. In a window starting at state k0, an
    Even x ∉ C of layer d switches at a transition k → k + 1 only if k ≤ k0 + d − 1. … (C) Count. … So a window has at most D :=
    max{layer(v) : v switches in I} transitions, and |I| ≤ E_I + (E_I + 1)·D = (D + 1)(E_I + 1) − 1. □»
    - There I is a W-constant interval and layer(v) the length of the fixed W(v).
- DEPENDENCE OF THIS PACKET ON R143, exactly:
  - (a) §5 uses R143's DEFINITIONS of U_k and EVENT, read over a whole W-run F in place of I. E_F and «window» are defined the same way
    on F.
  - (b) Lemma PLAY-CAUSE (§4) restates the play argument of R143 (A) and re-proves it on a W-run, where W is not fixed; no layer is used.
  - (c) SETTLE (B) and (C) are NOT used.
  - RUN-SETTLE's front ℓ_(k+1) is (B)'s «layer» made time-dependent. On a W-constant interval, RUN-SETTLE gives |I| ≤ n(E_I + 1) − 1,
    which is weaker than SETTLE's (D + 1)(E_I + 1) − 1. SETTLE stays the sharper statement there, and this packet does not replace it.

## 3. Claim RG′ (PROVED, to sign; L-SI box 51b §10.1 with W := W_(k+1) at ANY S4a step of a W-run)
- Setting. Any transition k → k + 1 of a W-run.
  - S4a evaluates the dual of H_k with dual-Even fixed to τ (si.py Engine.evaluate). So the round of cycle node c is a one-player problem
    for (original) Even on the alive vertices R reaching c.
  - The deletions (si.py l. 133-149) process each u ∈ R with rank(u) > rank(c), in decreasing rank:
    - u bad for original Even (dual par 0): M := reach(c avoiding u); every q ∉ M gets bit u; u's and every M-vertex's edges are
      restricted to M;
    - u good for original Even: M := reach(u avoiding c); every q ∈ M gets bit u; the edges of M ∖ {u} are restricted to M.
  - By [R57] the computed values (c, path[x], dist[x]) are W_(k+1).
- Statement. In c's round, the remaining edges (x, y), x ≠ c, with dist(y) = dist(x) − 1 are exactly the W_(k+1)-tight arena edges of x
  whose W_(k+1)-cycle node is c.
- (A) Every remaining edge (x, y), x ≠ c, has path[x] = path[y] ∪ ({x} if rank(x) > rank(c)).
  - Invariant per processed u: membership of bit u agrees on every remaining edge, except on edges leaving u itself.
  - Bad u: an edge x → y with y ∈ M and x ∉ M ∪ {u} would put x in M. Good u: an edge x → y with y ∈ M, x ∉ M and x ≠ c would put x in M.
    So remaining edges cross M only out of u.
  - Every processed u carries its own bit: a bad u ∉ M gets it, a good u ∈ M gets it. Hence the exception at u is exactly «{x} if
    rank(x) > rank(c)».
  - Later deletions only remove edges.
- (B) Every W_(k+1)-tight arena edge (x, y) with λ_W(x) = c survives.
  - y has cycle node c (tightness), so y ∈ R is alive in c's round.
  - A deleted edge is non-tight:
    - bad u, deleted q → y with q ∈ M, y ∉ M: y has bit u and q lacks it;
    - bad u, deleted u → y with y ∉ M: every path from y to c passes through u, so ℓ(y) > ℓ(u) and the edge is not length-tight;
    - good u, deleted q → y with q ∈ M ∖ {u}, y ∉ M: q has bit u and y lacks it.
- (A) with dist(y) = dist(x) − 1 is exactly x ⊕ W_(k+1)(y) = W_(k+1)(x); (B) is the converse. □
- Difference from §10.1 (word-diff for the referees): «A W-flat transition» → «Any transition»; «W_{k+1} = W» → «W_(k+1)». No step of the
  proof uses W_(k+1) = W_k.

## 4. Lemma PLAY-CAUSE and two facts (PROVED, to sign)
- Fix a W-run F with τ and C. A transition k → k + 1 of F is EVENT-FREE if it is not an EVENT (§2).
- Lemma PLAY-CAUSE. If k → k + 1 is event-free and Ξ_(k+1)(x) ≠ Ξ_k(x), then some Even y with λ_W(y) ≠ y switches at k and lies on x's
  (σ_(k+1), τ)-path to λ_W(x). In particular ℓ_(k+1)(x) ≥ ℓ_(k+1)(y).
  - Proof. Let x = y_0, y_1, … be the (σ_(k+1), σ̄_(k+1))-play, and i the least index with y_i ∈ D_(k+1) ∪ C.
    - i exists: before D_(k+1), Odd vertices follow τ, so y_0 … is the (σ_(k+1), τ)-play, which reaches λ_W(x) ∈ C.
    - y_(i+1) ∈ U_(k+1): σ̄_(k+1)(y_i) if y_i ∈ D_(k+1), the Ξ-successor of y_i if y_i ∈ C.
    - Every value on a play is (cycle node w of its eventual cycle, the vertices of the path to the first occurrence of w that are more
      relevant than w, the length of that path). The eventual cycle of x's play is that of y_(i+1)'s play, and w is read off
      Ξ(y_(i+1)). If w = y_j for some j ≤ i, the path is y_0 … y_j. Otherwise it is y_0 … y_i followed by the path of Ξ(y_(i+1)).
    - So Ξ_(k+1)(x) is determined by the sequence y_0 … y_i and the value Ξ_(k+1)(y_(i+1)).
    - Suppose no Even y_t, t ≤ i, switches at k. If y_i ∈ C is Even it does not switch, by no event (ii).
    - σ̄_k = σ̄_(k+1) and D_k = D_(k+1) (no event (i)). So the (σ_k, σ̄_k)-play from x is y_0 … y_(i+1) …, with the same first index i.
    - Ξ_k(y_(i+1)) = Ξ_(k+1)(y_(i+1)) (no event (iii); y_(i+1) ∈ U_(k+1)). Hence Ξ_k(x) = Ξ_(k+1)(x).
    - So some Even y_t, t < i, switches. It is not in C, and it lies on x's (σ_(k+1), τ)-path before λ_W(x), so
      ℓ_(k+1)(x) = t + ℓ_(k+1)(y_t). □
- (W-MON) In a W-run, W_(k+1) ⊵ W_k pointwise: ARENA-MAX with ρ = σ_k, a strategy of H_k.
- (PATH) If no Even vertex on the (σ_(k+1), τ)-path from b to c = λ_W(b) switches at k, then b's (σ_k, τ)-path is that same path. Hence
  W_k(b) = W_(k+1)(b) and ℓ_k(b) = ℓ_(k+1)(b). (W(b) = (c, the relevant vertices of the path, its length); c ∈ C at both states.)

## 5. Theorem RUN-SETTLE and Corollary RUN-COUNT (PROVED, to sign; uses [R57], [R15] (a), ARENA-MAX, Claim RG′, and LEX-BFS / IDX-MONO in Case 2a only)
- Statement.
  - Let F be a W-run, and let the transitions k0, k0 + 1, …, k1 − 1 of F all be event-free. For k0 ≤ k < k1 put j := k − k0.
  - (S_j) Every Even y that switches at k has ℓ_(k+1)(y) ≥ j + 1.
  - (X_j) Every vertex x with Ξ_(k+1)(x) ≠ Ξ_k(x) has ℓ_(k+1)(x) ≥ j + 1.
  - Consequently k1 − k0 ≤ max_x ℓ(x) ≤ n − 1.
- Corollary RUN-COUNT. For every W-run F with E_F event transitions, |F| ≤ E_F + (E_F + 1)(n − 1) = n(E_F + 1) − 1.
  - Proof: the event-free transitions form at most E_F + 1 maximal blocks, each with ≤ n − 1 transitions.
- Proof of the theorem. S_j ⇒ X_j by PLAY-CAUSE. We prove S_j by induction on j.
- j = 0. A switched y is not in C (no event (ii)), so ℓ_(k+1)(y) ≥ 1.
- j ≥ 1, assuming S_(j−1), hence X_(j−1).
  - Suppose S_j fails at k = k0 + j. Among the switched Even y with ℓ_(k+1)(y) ≤ j, choose one with the least L := ℓ_(k+1)(y).
  - Put a := σ_k(y), b := σ_(k+1)(y), c := λ_W(y) ∈ C. Then ℓ_(k+1)(b) = L − 1.
  - (MIN) No Even u with ℓ_(k+1)(u) < L switches at k. Such a u would be a violator with smaller ℓ, since L ≤ j.
  - Every vertex on b's (σ_(k+1), τ)-path has ℓ_(k+1) ≤ L − 1. So by (MIN) and (PATH): W_k(b) = W_(k+1)(b), ℓ_k(b) = L − 1, and b's
    (σ_k, τ)-path is its (σ_(k+1), τ)-path. That path avoids y, because y → b → … → c is simple.
  - Case 1: b ∉ H_(k−1)(y). (k − 1 ≥ k0, so k − 1 → k is a transition of the block.)
    - b ∈ H_k(y) and b ≠ a, so Ξ_k(b) ▷ Ξ_k(a).
    - Ξ_k(a) ⊵ Ξ_(k−1)(a) by [R15]. Also Ξ_(k−1)(a) ⊵ Ξ_(k−1)(σ_(k−1)(y)): equal if a = σ_(k−1)(y); otherwise a ∈ Iσ_(k−1)(y), because
      σ_k(y) ∈ H_(k−1)(y).
    - If Ξ_k(b) = Ξ_(k−1)(b), then Ξ_(k−1)(b) ▷ Ξ_(k−1)(σ_(k−1)(y)), so b ∈ H_(k−1)(y): a contradiction. So Ξ(b) changes at k − 1 → k.
    - X_(j−1) gives ℓ_k(b) ≥ j > L − 1 = ℓ_k(b). Contradiction.
  - Case 2: b ∈ H_(k−1)(y).
    - ρ := σ_k with y ↦ b is a strategy of H_(k−1). Its play from y is y, then b's (σ_k, τ)-path, which avoids y.
    - ARENA-MAX at k − 1 → k: W_k(y) ⊵ y ⊕ W_k(b) = y ⊕ W_(k+1)(b) = W_(k+1)(y) ⊵ W_k(y) (W-MON).
    - So W_(k+1)(y) = W_k(y) = y ⊕ W_k(a) = y ⊕ W_k(b) (y ⊕ · reflects ⊴). Both a and b are W_k-tight at y.
    - Case 2a: a is W_(k+1)-tight at y.
      - Then ℓ_(k+1)(a) = L − 1. By (MIN) and (PATH) the (σ_(k+1), τ)-paths of a and of b are their (σ_k, τ)-paths, so
        key_(σ_k) = key_(σ_(k+1)) on a and on b.
      - a ∈ H_k(y) (as σ_k(y)), and b ∈ H_(k−1)(y) ∩ H_k(y).
      - Ω(c) even: LEX-BFS at k − 1 → k (a chosen, b W_k-tight in H_(k−1)(y)) gives key(a) < key(b). LEX-BFS at k → k + 1 gives
        key(b) < key(a). (Keys of distinct vertices differ in their last coordinate.)
      - Ω(c) odd: IDX-MONO gives index(a) < index(b) and index(b) < index(a).
      - Contradiction either way. y ∉ C, so the CN branch does not arise.
    - Case 2b: a is not W_(k+1)-tight, and a's (σ_(k+1), τ)-path avoids y.
      - ρ′ := σ_(k+1) with y ↦ a is in H_k, and its play from y is y, then a's (σ_(k+1), τ)-path.
      - ARENA-MAX at k → k + 1: y ⊕ W_(k+1)(a) ⊴ W_(k+1)(y) = y ⊕ W_k(a) ⊴ y ⊕ W_(k+1)(a). The last step is W-MON, and ⊕ is monotone on
        values with cycle node c.
      - So a is tight. Contradiction.
    - Case 2c: a is not W_(k+1)-tight, and a's (σ_(k+1), τ)-path contains y.
      - a's (σ_k, τ)-path is y's minus y, so it avoids y. Let u be the first vertex on it that switches at k. u exists, u ∉ C, u ≠ y.
      - a's (σ_(k+1), τ)-path follows a's (σ_k, τ)-path to u, then u's (σ_(k+1), τ)-path, which therefore reaches y.
      - Let P := u's (σ_(k+1), τ)-path from u up to y, y excluded. Let Q := y's (σ_k, τ)-path from y up to u, u excluded (Q = y, a, …).
      - Z := P ∪ Q is a simple cycle. Q ∖ {y} and P are consecutive segments of a's simple (σ_(k+1), τ)-path, and y ∉ P. c ∉ Z, since
        every vertex of P and Q precedes c on a path to c.
      - Values, all with cycle node c: W_(k+1)(u) = P ⊕ W_(k+1)(y); W_(k+1)(y) = W_k(y) (Case 2); W_k(y) = Q ⊕ W_k(u).
      - Disjointness: P avoids y's (σ_(k+1), τ)-path, whose path set is that of W_k(y), which is Q's relevant vertices ⊔ S_k(u), the path
        set of W_k(u). Hence W_(k+1)(u) = (c, S_k(u) ⊔ R, ℓ_k(u) + |Z|), with R := {z ∈ Z : z more relevant than c}.
      - W-MON: W_(k+1)(u) ⊵ W_k(u). By the order of §1 this means: R ≠ ∅ and its most relevant vertex is even; or R = ∅ and c is odd
        (|Z| ≥ 2).
      - ρ′ := σ_(k+1) with y ↦ a is in H_k. Its play from y runs y, a, …, u, P, y, closing Z. Its cycle node z* is the most relevant
        vertex of Z, so reward(z*) > reward(c):
        - if R ≠ ∅: z* = max R, even, with p′(z*) > p′(c) ≥ |reward(c)|;
        - if R = ∅ and c is odd: reward(c) = −p′(c) < −p′(z*) ≤ reward(z*).
      - So val(ρ′, τ)(y) ▷ W_(k+1)(y), contrary to ARENA-MAX at k → k + 1. Contradiction.
  - Cases 1, 2a, 2b and 2c exhaust the possibilities, so S_j holds.
- The bound. If k1 > k0, the transition k1 − 1 switches some Even y (§1). S_(k1−k0−1) gives ℓ_(k1)(y) ≥ k1 − k0, and ℓ ≤ n − 1 since
  the path to the cycle node is simple. □

## 6. Theorem HEAD-RED (EQUIVALENCE, to sign)
- Per W-run F, define:
  - SB_F(o) := the transitions of F at which σ̄(o) changes;
  - CN_F(c) := the transitions of F at which Even c ∈ C switches;
  - HXU_F(u) := the transitions k → k + 1 of F with u ∈ U_k ∪ U_(k+1) and Ξ_(k+1)(u) ≠ Ξ_k(u).
- Statement.
  - (⇐) E_F ≤ Σ_(Odd o) SB_F(o) + Σ_(c ∈ C) CN_F(c) + Σ_u HXU_F(u). Hence, by RUN-COUNT,
    |F| ≤ n·(1 + n·max_o SB_F(o) + n·max_c CN_F(c) + n·max_u HXU_F(u)) − 1.
  - (⇒) Each of SB_F(o), CN_F(c), HXU_F(u) is ≤ |F|.
  - So, for any family of games: every W-run has polynomially many transitions ⇔ max SB_F, max CN_F and max HXU_F are polynomial over
    all W-runs.
- Proof. An event transition has an event of kind (i), (ii) or (iii), and each kind is counted at least once on the right. □
- Comparison (READING, not to sign). XI-RUN (P-N5-WRUN §3) needs Ξ-changes at EVERY vertex. Here only upward heads are counted, plus
  σ̄-changes and W-cycle-node switches.

## 7. Corollary T-XCH (EQUIVALENCE; landed RESULTS R86 (a) + R15 (d); only the composition is new)
- What the Lead asked for here (RETURN-CHARGE′-O, the Odd side of L-SI's SEG-XCH) is ALREADY LANDED. RESULTS R86 (a), verbatim: «Lemma
  SW-RETURN (§2): "For every run of states R of an N5 run, every Even v and every vertex c: ENT_R(v, c) ≤ 1 + RISE_R(c). Dually for Odd v
  with U."». REFEREE's cell there: «it holds on ANY stretch of consecutive states, fallbacks included».
  - L-SI's RETURN-CHARGE′ (box 51b §11) and its Odd mirror are this lemma in return form. Nothing in them is new against R86.
- Corollary T-XCH. Let a run have T iterations; RISE(c) / RISE^U(c) := the transitions of the whole run changing Ξ(c) / U(c);
  XE := max_c RISE(c), XO := max_c RISE^U(c). Then:
  - T ≤ Σ_v SW(v) (R15 (d): every iteration changes σ or τ);
  - Σ_v SW(v) = Σ_(edges (v, c)) ENT(v, c) ≤ Σ_(edges) (1 + RISE(c)) (R86 (a), both sides, R = the whole run);
  - hence T ≤ m_E(1 + XE) + m_O(1 + XO).
  - Conversely XE, XO ≤ T. So T is polynomial ⇔ XE and XO are polynomial: an EQUIVALENCE and a reformulation of G-N5-TIME, not a
    bound.
  - R86's own Corollary COMPOSE-RUN is the same chain run per λ-run with LEN-MONO. T-XCH is its whole-run, RISE form.

## 8. CONJECTURES (NOT to sign)
- FLIP-EV: every σ̄(o)-change at k → k + 1 of a W-run that moves o out of D or within D (old target ≠ τ(o)) happens at a transition with an
  event (iii), whenever o is not its own Ξ-cycle node at k or at k + 1. With it, a proved corollary of the note (FLIP-RED) gives
  E_F ≤ (n_O + 1)E⁽ⁱⁱⁱ⁾_F + n_O + CN_F + 2·XCN_F. That corollary is not in this packet.
- HX-POLY (max HXU_F polynomial), CN-POLY, XCN-POLY (σ̄-changes at own Ξ-cycle nodes): open.

## 9. DATA, DEAD, READING (NOT to sign; pins in experiments/si/check.sh «box 52», tools experiments/si/heads52/ at l-si 71d1d0ac)
- Corpus: box 50b's lists (719 + 413 runs) plus latew_K16_m32 and fx_K8_m32, 1,134 runs.
  - bffront.py: 36,834 in-block Ξ-changes, 0 with ℓ_(k+1)(x) ≤ j. The bound is attained (gci2_n12 with start); MUT=1 control BADW 2.
  - swcase.py, switches at j ≥ 1: Case 1 13,998; «WR» (b's W changes, excluded by (MIN)) 186; Case 2a 13; Case 2b 0; Case 2c 0;
    violations 0.
  - rwin.py: the longest event-free block is 44 at n 48 (red/xing/instances/x32_rand48.pg).
- DEAD (N5-HEADS §1.6): the same front measured by the distance along the Ξ-play to D ∪ C (red/ul/instances/ladderd0_k12_n48 + start,
  11 violations). That is why the front is W-length.
- Second engine: red/seg/xeng.py (n5b SPEC) gives state sequences identical to n5x on the four instances in heads52/inst/. The corpus
  tools use n5x only.

## Proposed RESULTS line
- docs/si/P-N5-SETTLE-line.txt (sha1 reported with this packet).
