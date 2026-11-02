# P-N5-REALIZE: every IDEAL genome with an ACYCLIC Ξ-graph runs, state for state, as ONE real N5 FL run of the STAB+K+ESC game of size N + 3M + 6 (Theorem REALIZE); so FL-POLY from every start pair ⇒ IDEAL-ACYC-POLY, and a super-polynomial IDEAL-ACYC family is a real N5 family from a given start pair (Corollary REAL-IDEAL) — a REDUCTION / NECESSITY packet for the referees (L-RED successor 45)
Frozen 2026-11-02 (date -u: see the commit), L-RED successor 45 (Opus 5.5), D1/D18. For REFEREE and REFEREE-2 (Lead brief 2026-11-02 02:38Z:
«freeze packet P-N5-REALIZE for the two referees … your predecessor's Theorem REALIZE (R187 §1) and Corollary REAL-IDEAL»).
- Status: a REDUCTION / NECESSITY statement. It bounds NOTHING. G-N5-TIME stays OPEN. Not M3, not a step-4 pass, not a TARGET.md claim.
- Source notes (history only; this packet restates everything it uses and governs where they differ): docs/red/R187-ladder.md §1
  (l-red 436fe6e9; proof by successor 44), docs/red/R178-ideal.md §1 (the IDEAL model, l-red e03b15a6), docs/red/R188-xicounter.md.
- To sign: §3 Lemmas K, PLAY, SBAR, TAU, ESC, W, KEY; §4 Theorem REALIZE; §5 Corollary REAL-IDEAL. To check: §6 (scope), §7 (DATA
  reproduction). Not to sign: §7 numbers as statements (DATA), §8 (honest limits, READING).
- Line: docs/red/P-N5-REALIZE-line.txt (one line, no heading marker). Fixes after the freeze: docs/red/P-N5-REALIZE-fixes.md
  (append-only); line revisions as P-N5-REALIZE-line-L1.txt, … This file and the line file are never edited (sha1 pinned in
  experiments/red/check.sh).

## 1. Setting and premises
- N5 = SPEC S1-S5 (docs/new/N5-ssi-global.md, «SPEC (EXACT)») on a parity game Γ = (V, E, Ω, owner), n := |V|, run from a GIVEN start
  pair (σ_0, τ_0) (SPEC: «Optional start pair»). A run is the sequence of states (σ_j, τ_j); transition j is (σ_(j−1), τ_(j−1)) →
  (σ_j, τ_j); it is a FALLBACK if S4c fired at it.
- Valuations, as in SPEC S1. p'(v) := 2·rank(v) + (Ω(v) mod 2), rank by (Ω(v), v). A value is (c, P, ℓ): c the most relevant (max p')
  vertex of the cycle the play ends in, P the set of play vertices before c with p' > p'(c), ℓ the number of steps to c. Order «better
  for Even» (written ⊳; ⊴, ◁ as usual): reward of c first (p'(c) if Ω(c) even, −p'(c) if odd), then P by the signed weight
  Σ_(u∈P) ±2^rank(u) (+ for even Ω(u)), i.e. by the most relevant vertex of the symmetric difference and its parity, then ℓ (c odd:
  longer is better for Even; c even: shorter). For a vertex v not on the cycle of its own play, value(v) = v ⊕ value(next vertex), where
  v ⊕ (c, P, ℓ) := (c, P ∪ {v : p'(v) > p'(c)}, ℓ + 1); for fixed c and v ∉ P this map is injective and strictly order-preserving.
- Ξ_j := Ξσ_j (σ_j with Odd's OPTIMAL counterstrategy σ̄_j, minimising the order at every vertex at once, SPEC S1). Ξτ_j, τ̄_j: the same
  for τ_j on G^d (owner swapped, Ω + 1). Iσ, Iτ: SPEC S2. W_j := the value of the (σ_j, τ_j)-play.
- Fact DUAL (used in Lemma TAU; one line). The order of G^d is the REVERSE of the order of Γ: ranks agree (SPEC A3), P-membership agrees
  (p' > p'(c) ⟺ rank > rank(c)), rewards map by x ↦ −x − 1 (Ω(c) even: 2r ↦ −(2r + 1); odd: −(2r + 1) ↦ 2r), signed weights change
  sign, and the length rule swaps with the parity of c. So Iτ(v) = {w ≠ τ(v) : Ξτ(w) ◁ Ξτ(τ(v))} (strictly better for Odd in Γ's order),
  and τ̄ maximises Γ's order at every vertex.
- FL run (as in RESULTS R103): a maximal set of consecutive transitions j = a + 1, …, b, each of which is not a fallback, keeps τ
  (τ_j = τ_(j−1)), changes σ (σ_j ≠ σ_(j−1)) and keeps W (W_j = W_(j−1) at every vertex). Its length is b − a.
- Premises (named; nothing else is used):
  - [SPEC] S1-S5 as written, with FIX 2-4 and Q1-Q4 of the same file.
  - [1E-N3] The standing SPEC premise (RESULTS R57; R102 S4B-OPT under Lead reading L45): at a non-fallback transition j, σ_j is a
    POINTWISE OPTIMUM of the one-player arena H_(j−1) in which Even y keeps R_j(y) := {σ_(j−1)(y)} ∪ Iσ_(j−1)(y) and Odd follows τ_(j−1);
    W*_j := its value.
  - [VJ-LOC] VJ00 local optimality: BRICS RS-00-48 Lemma 5.8 «1 ⇒ 2» (no improving switch ⇒ optimal), the direction that HOLDS (RESULTS
    R15 side finding; L-LIT docs/lit/T21-VJ00-check.md (c) «Unaffected»). Applied on G^d to the one-player game Γ_σ (Even's choices
    fixed to σ), where Odd is the only player, so the opponent's counterstrategy is trivial and the lemma's valuation of an Odd strategy
    ρ is the play value φ_(σ,ρ). Use: if no Odd v has w ∈ succ(v) with φ_(σ,ρ)(w) ◁ φ_(σ,ρ)(ρ(v)), then φ_(σ,ρ) = Ξσ at every vertex.
  - [RULE] (Lead reading L46 with its 17:35Z amendment; REFEREE CF-1 472f0dcd, REFEREE-2 d96d2f9e). Citing line, verbatim as in
    RESULTS R103: «RESULTS R24 (a) Lemma R and R24 (b)'s choice rule (TB proof steps 1, 3-5; fixes §2.3) with bridge B, whose proof uses
    no 𝒞^1O hypothesis». Form used: at a non-fallback transition j, for every Even x that is not its own W′-cycle node (W′ := W*_j),
    σ_j(x) is the κ_j-least element of TIE_j(x) := the options of x in H_(j−1) that are FULLY W′-optimal (W′(x) = x ⊕ W′(y)), an option
    being a corner (outside the rule) when x occurs on its play BEFORE that play's cycle node; for an even W′-cycle node c of x,
    κ_j(y) := the root-first key of y, i.e. the vertex sequence of the σ_j / τ_(j−1) play path from c to y, c excluded, compared
    lexicographically by index. Non-movers are covered ((R1) ruled «covered», RESULTS R103).
    Bridge B (RESULTS R103, landed: «every Even h ∉ CN has σ_(j−1)(h) and σ_j(h) fully optimal in that arena») is the bridge CF-1 asks
    the citing packet to have. Here its CONCLUSION is proved directly, for EVERY arena option, by Lemma W (iii) below, at transitions
    that are not yet known to be FL; so this packet uses Lemma W (iii), not bridge B's FL hypothesis.

## 2. The IDEAL model (R178 §1) and the IDEAL-ACYC class
- A GENOME G consists of:
  - movers x = 0, …, N − 1, each with a level lev(x) ∈ {0, …, d − 1} and options k = 0, …, deg(x) − 1; M := Σ_x deg(x);
  - per option (x, k): a W-target wt(x, k), which is a mover of level lev(x) − 1 if lev(x) ≥ 1 and «none» if lev(x) = 0 (GRADED);
    a Ξ-target xt(x, k) ∈ {movers} ∪ {X}; a β-id b(x, k) (a bijection onto 0..M − 1);
  - a gate index gate(x, k), a bijection of the options onto 0..M − 1;
  - per β-id b: a rank br(b) (a bijection onto 0..M − 1) and a parity bp(b) ∈ {0, 1};
  - a start s_0 (an option per mover).
- The Ξ-GRAPH of G: the digraph on movers with an edge x → xt(x, k) for every option with xt(x, k) ≠ X. G is in IDEAL-ACYC iff its
  Ξ-graph is ACYCLIC (self-loops count as cycles).
- Values under a state s (an option per mover). The X-CHAIN of a face (x, k) is the sequence of options (x, k) = (x_0, k_0),
  (x_1, k_1), … with x_(i+1) := xt(x_i, k_i) and k_(i+1) := s(x_(i+1)), ending at the first option whose Ξ-target is X (finite for
  IDEAL-ACYC). B_s(x, k) := the set of β-ids of the chain. In R178 §1 / fastcyc this is the one-player VJ value in G_X (gates on their
  Ξ-faces) with β-priorities 4 + 2·br + bp above an even sink T of priority 2: (T, B_s(x, k), length). Order: (x, k) ▷_s (x, k') iff
  that value is strictly better for Even (r178/fastcyc.py values()).
- Fact X (used in Lemma KEY). For IDEAL-ACYC and two options k ≠ k' of ONE mover x, B_s(x, k) ≠ B_s(x, k'): after its first option
  (x, k'), the chain of (x, k') visits only movers reachable from x by ≥ 1 Ξ-edge, so it never returns to x (acyclic) and never
  contains b(x, k); and vice versa. Hence
  (x, k) ▷_s (x, k') iff the β-id of LARGEST rank in B_s(x, k) Δ B_s(x, k') has parity 0 and lies in B_s(x, k), or has parity 1 and lies
  in B_s(x, k'). Lengths never decide.
- IDEAL step from s. Availability A_s(x) := {s(x)} ∪ {k : (x, k) ▷_s (x, s(x))}.
  - If |A_s(x)| = 1 for every x, the run STOPS («opt»).
  - Otherwise s' is defined level by level, lev = 0, 1, …: key(x, k) := (gate(x, k)) if lev(x) = 0, and key_(s')(wt(x, k), s'(wt(x, k)))
    followed by gate(x, k) otherwise (a tuple of length lev(x) + 1); s'(x) := the k ∈ A_s(x) with the lexicographically least key. Keys of
    one mover's options have equal length and distinct last entries, so s'(x) is unique. If s' = s, the run STOPS («stuck»).
  - Otherwise s → s' is one IDEAL step. L(G) := the number of IDEAL steps from s_0 (finite: it is an FL run of a real N5 run by
    Theorem REALIZE, and N5 terminates, RESULTS R15).
  - This is R178 §1's step (S4a with σ̄ := Ξ-face and τ := W-face fixed by fiat; TB lex-min key = RESULTS R24 (b) at an even cycle node),
    implemented as r178/fastcyc.simulate and r187/ideal.traj (the same rule; ideal.traj also returns the states).

## 3. The construction and the lemmas
### 3.1 The game Γ(G) (experiments/red/r187/stab.py, build(G, 0, kgad=True, esc=True))
Vertices and indices (n = N + 3M + 6):
- movers x: index x, Even, Ω 0, edges to its gates;
- gates g = (x, k): index N + gate(x, k), Odd, Ω 1, edges {e_g, β_g};
- β_g: indices N + M, … (options in (x, k) order), Even, Ω(β_g) := 6 + 2·br(b(g)) + bp(b(g)); edges {xt(g), u} if xt(g) is a mover
  (ESC), {u} if xt(g) = X. bmax := the largest Ω(β);
- e_g: indices N + 2M, … allocated in GATE-INDEX order, Even, Ω(e_g) := eb + 2·i, eb := the least even number > bmax, i := the position
  of g in the order by (lev(owner), gate index) (so every Ω(e) is EVEN and above every Ω(β)); single edge to wt(g), or to c_W if lev = 0;
- c_X: index N + 3M, Even, Ω 2, self-loop (isolated, unused); c_W: index N + 3M + 1, Even, Ω top := the least even number ≥ 2 + max
  Ω so far, self-loop;
- the core K = (K0, K1, K2, K3) = (u, …), indices N + 3M + 2, …, N + 3M + 5: K0 Even Ω top + 2, edges {K1, K3}; K1 Even Ω 5, edges
  {K0, K1}; K2 Odd Ω 3, edges {K1, K2}; K3 Even Ω top + 3, edges {K1, K2}. K is CLOSED (no edge leaves K). u := K0.
Rank facts used below: movers, gates, c_X, K2 < K1 < every β < every e < c_W < K0 < K3 (by Ω: 0, 1, 2, 3 < 5 < 6.. ≤ bmax < eb.. < top <
top + 2 < top + 3). Odd vertices: the gates and K2 only.
Start (σ_0, τ_0): σ_0(x) := (x, s_0(x)); σ_0(β_g) := xt(g) if a mover, u otherwise; σ_0(K0) := K3, σ_0(K1) := K1, σ_0(K3) := K2; single
edges elsewhere. τ_0(g) := e_g at every gate; τ_0(K2) := K2.
A STANDARD STATE for a mover state s is the pair (σ^s, τ_0) with σ^s := σ_0 except σ^s(x) := (x, s(x)) at movers. So (σ_0, τ_0) is
standard for s_0. Fix a standard state (σ, τ) = (σ^s, τ_0) for Lemmas K-KEY.

### 3.2 Lemma K (the stuck core; PROVED, lane)
In every standard state, with ρ_K(K2) := K1:
- (a) Ξσ on K: K1 ↦ (K1, ∅, 0); K2 ↦ (K1, ∅, 1); K3 ↦ (K1, {K3}, 2); K0 ↦ (K1, {K0, K3}, 3); σ̄(K2) = K1 (Lemma SBAR).
- (b) Iσ ∩ K = {(K0, K1)}.
- (c) Iτ ∩ K = ∅ and, in the τ-world, Ξτ(K1) has a cycle node of reward ≥ reward(K0).
- (d) In S4a's arena H, every play from u ends in an ODD cycle (node K1 or K2), and the pointwise optimum keeps σ on K.
Proof.
- (a) Under σ (K0 → K3, K1 → K1, K3 → K2) and K2 → K1 the plays are K1 (self-loop), K2 → K1, K3 → K2 → K1, K0 → K3 → K2 → K1; the cycle
  node is K1 (Ω 5); P collects the vertices of rank > rank(K1) before K1: K3 and K0, not K2. (σ̄(K2) = K1 is part of Lemma SBAR.)
- (b) K0: Ξσ(K1) = (K1, ∅, 0) vs Ξσ(σ(K0)) = Ξσ(K3) = (K1, {K3}, 2): the symmetric difference is {K3}, Ω odd, so Ξσ(K1) ⊳ Ξσ(K3):
  improving. K1: Ξσ(K0) = (K1, {K0, K3}, 3) vs Ξσ(K1): top of the difference is K3 (odd), so Ξσ(K0) ◁ Ξσ(K1): not improving. K3:
  Ξσ(K1) vs Ξσ(K2) = (K1, ∅, 1): same c and P; c = K1 is odd, so the longer K2 is better for Even: not improving.
- (c) τ(K2) = K2 is a self-loop, so Ξτ(K2) = (K2, ∅, 0), reward −p'(K2) < 0. From K1 Even can play K1 → K0 → K1, a cycle with node K0
  (Ω top + 2, even); τ̄ maximises Γ's order (Fact DUAL), so Ξτ(K1) has reward ≥ p'(K0) > 0. Hence Ξτ(K1) ⊳ Ξτ(K2): (K2, K1) ∉ Iτ.
- (d) By (b), H keeps K0 → {K3, K1}, K1 → {K1}, K3 → {K2}, and K2 → K2 (τ). The plays from K0 are K0 → K1 → K1 (cycle node K1, Ω 5)
  and K0 → K3 → K2 → K2 (node K2, Ω 3), both odd; reward −p'(K2) > −p'(K1), so K3 is strictly better at K0. K1, K3 have one option.
  K0 is not on a cycle of H, so a pointwise optimum (value v ⊕ value(choice)) must choose K3. ∎

### 3.3 Lemma PLAY (play shapes; PROVED, lane)
Let ρ be the Odd strategy «β_g at every gate, K1 at K2», and φ := φ_(σ,ρ). For a face g = (x, k) let B(g) := {β_h : h on the X-chain of
g under s} (§2). Then:
- (a) the (σ, ρ)-play from β_g follows the X-chain of g: β_g → xt(g) → σ(xt(g)) → β_(…) → … until the first option with xt = X, then u;
  it reaches u (the Ξ-graph is acyclic, so the chain is finite and repeats no mover) and continues K0 → K3 → K2 → K1; no e-vertex, no
  c_W and no c_X occurs on it. So φ(β_g) = (K1, B(g) ∪ {K0, K3}, ℓ_g) for some length ℓ_g, and φ(g) = g ⊕ φ(β_g) = (K1, B(g) ∪ {K0,
  K3}, ℓ_g + 1) (Ω(g) = 1 < 5);
- (b) for lev(x) = 0: the play from e_g is e_g → c_W, φ(e_g) = (c_W, ∅, 1);
- (c) for lev(x) ≥ 1: the play from e_g is e_g → wt(g) → σ(wt(g)) =: g' → β_(g') → (a); e_g occurs once (ρ never takes an e-face),
  so φ(e_g) = (K1, {e_g} ∪ B(g') ∪ {K0, K3}, ℓ_(g') + 3).
Proof. Each claim reads the play off the edges: Even vertices follow σ (standard), Odd vertices follow ρ; acyclicity of the Ξ-graph
makes the chain of (a) finite; K is closed; P is computed with the rank facts of §3.1 (movers, gates, K2 below K1; β, e, K0, K3
above). ∎

### 3.4 Lemma SBAR (Odd's best reply is the β-face, by strict local preference; PROVED, lane)
In every standard state, σ̄ = ρ: σ̄(g) = β_g at every gate g and σ̄(K2) = K1. Hence Ξσ = φ.
Proof.
- (i) No Odd-improving switch for ρ w.r.t. φ.
  - Gate g, lev ≥ 1: by Lemma PLAY, φ(e_g) and φ(β_g) have the same cycle node K1, and the symmetric difference of their P-sets
    contains e_g and otherwise only β-vertices (K0, K3 lie in both). e_g outranks every β and has even Ω, so φ(e_g) ⊳ φ(β_g):
    switching to e_g is strictly WORSE for Odd.
  - Gate g, lev = 0: φ(e_g) has the even cycle node c_W, φ(β_g) the odd node K1; Odd strictly prefers the odd reward.
  - K2: φ(K2) = (K1, ∅, 1) ⊳ φ(K1) = (K1, ∅, 0) (odd node, longer is better for Even): switching to K2 is strictly worse for Odd.
- (ii) By [VJ-LOC], φ = Ξσ at every vertex.
- (iii) SPEC's σ̄ is optimal, so φ_(σ,σ̄) = Ξσ = φ. Suppose σ̄(g) = e_g at a gate g.
  - If g lies on the cycle of its own (σ, σ̄)-play, that cycle passes e_g and avoids K, c_W and c_X (closed, and g ∉ them), so its most
    relevant vertex is an e-vertex (e outranks movers, gates and β): an EVEN cycle node, while φ(g) has the odd node K1. Contradiction.
  - Otherwise φ_(σ,σ̄)(g) = g ⊕ φ_(σ,σ̄)(e_g) = g ⊕ φ(e_g), which differs from φ(g) = g ⊕ φ(β_g): for lev = 0 by the cycle node, for
    lev ≥ 1 by the P-set (it contains e_g; g ⊕ adds nothing to P). Contradiction.
  - Suppose σ̄(K2) = K2: then K2's play is its self-loop and φ_(σ,σ̄)(K2) has cycle node K2 ≠ K1. Contradiction.
  - The gates and K2 are all Odd vertices, so σ̄ = ρ. ∎

### 3.5 Lemma TAU (τ stays; PROVED, lane)
In every standard state, Iτ = ∅. So S4b leaves τ unchanged (τ_new = τ).
Proof. Odd vertices are the gates and K2 (K2: Lemma K (c)). At a gate g with τ(g) = e_g:
- Ξτ(e_g): under τ every gate leads to its e-face, movers lead to gates, e to a lower mover or c_W. So EVERY play from e_g, whatever Even
  does, ends in the cycle c_W: Ξτ(e_g) has reward p'(c_W).
- Ξτ(β_g): Even may play β_g → u → K1 → K0 → K1 …, a cycle with node K0 (Ω top + 2, even, rank above c_W). τ̄ maximises Γ's order
  (Fact DUAL), so Ξτ(β_g) has reward ≥ p'(K0) > p'(c_W).
- So Ξτ(β_g) ⊳ Ξτ(e_g): β_g is strictly worse for Odd, (g, β_g) ∉ Iτ (Fact DUAL). ∎
- Remark (why ESC). Without the edge β_g → u, Ξτ(β_g) would also end at c_W and the comparison would fall to P and length, where Odd
  prefers the longer play to the even c_W: τ then breaks at upward Ξ-targets (R187 «Things only I know», notebook).

### 3.6 Lemma ESC (S4a keeps σ off the movers; PROVED, lane)
In every standard state: Iσ ≠ ∅ (it contains (K0, K1)), and every pointwise optimum of S4a's arena H has σ_new(β_g) = σ(β_g) at every β,
σ_new = σ on K, and σ_new = σ on e, c_X, c_W (single edges).
Proof.
- Iσ ∋ (K0, K1): Lemma K (b).
- β_g with xt(g) = X: one edge. β_g with xt(g) a mover: R(β_g) ⊆ {xt(g), u}. In H (Odd follows τ, so every gate leads to its e-face),
  every play from xt(g) runs mover → gate → e → … → c_W: value with the EVEN cycle node c_W. Every play from u ends in an ODD cycle
  (Lemma K (d)). So xt(g) is strictly better; β_g is on no cycle of H; a pointwise optimum (value(β_g) = β_g ⊕ value(choice)) chooses
  xt(g).
- K: Lemma K (d). ∎

### 3.7 Lemma W (W graded and constant; the arena optimum; PROVED, lane)
In every standard state (σ^s, τ_0), and for every s:
- (i) W at movers: W(x) = (c_W, ∅, 3·lev(x) + 3); at gates (c_W, ∅, 3·lev + 2); at e (c_W, ∅, 3·lev + 1); at β_g with a mover target
  (c_W, ∅, 3·lev(xt(g)) + 4); at β_g with target X, on K, c_X, c_W: values that do not depend on s. Hence W is the SAME for every
  standard state.
- (ii) In S4a's arena H: every play from a gate or mover of level ℓ ends at c_W after exactly the steps of (i), and no vertex outranking
  c_W is on it. So W*(y) = (c_W, ∅, 3ℓ + 2) for every gate y of a level-ℓ mover and W*(x) = (c_W, ∅, 3ℓ + 3).
- (iii) For every mover x: x's W′-cycle node is c_W (even, ≠ x); every option y ∈ R(x) is FULLY W′-optimal (W*(x) = x ⊕ W*(y)); none is
  a corner (y's play visits only vertices of level < lev(x) before c_W). So TIE(x) = R(x).
Proof. (i)-(ii): the (σ, τ_0)-play (resp. any H-play) from a mover of level ℓ is x → gate → e → (mover of level ℓ − 1) → … → c_W, three
steps per level, through movers (Ω 0), gates (Ω 1) and e-vertices, all below c_W; β-vertices are not reached (τ_0 takes e at every
gate). β_g → xt(g) then follows (i). The rest is closed or fixed. (iii) follows from (ii); levels drop strictly along W-plays. ∎

### 3.8 Lemma KEY (availability and keys are the IDEAL ones; PROVED, lane)
In every standard state (σ^s, τ_0), for every mover x:
- (a) R(x) = {σ(x)} ∪ Iσ(x) is the set of gates (x, k) with k ∈ A_s(x).
- (b) For y, y' ∈ R(x) and any Even strategy σ' that agrees with σ^(s') on movers of level < lev(x) (any s'), the root-first keys
  κ(y), κ(y') under (σ', τ_0) compare as the IDEAL keys key_(s')(x, k), key_(s')(x, k').
Proof.
- (a) By Lemma SBAR and PLAY (a), Ξσ((x, k)) = (K1, B_s(x, k) ∪ {K0, K3}, ℓ + 1). For two options of x the cycle nodes agree, K0, K3
  cancel, and B_s(x, k) ≠ B_s(x, k') (Fact X), so the comparison is decided by the β of largest rank in the symmetric difference and its
  parity: rank order of β = br order and parity = bp in BOTH Γ(G) (Ω = 6 + 2br + bp) and the IDEAL model (4 + 2br + bp). So
  Ξσ((x, k)) ⊳ Ξσ((x, s(x))) ⟺ (x, k) ▷_s (x, s(x)).
- (b) The play from a gate y = g_ℓ of a level-ℓ mover under (σ', τ_0) is g_ℓ, e_(g_ℓ), m_(ℓ−1), g_(ℓ−1), e_(g_(ℓ−1)), …, m_0, g_0, e_(g_0),
  c_W with g_i := σ'(m_i) and m_(i−1) := wt(g_i). Read from c_W (root first, c_W excluded): e_(g_0), g_0, m_0, e_(g_1), g_1, m_1, …,
  m_(ℓ−1), e_(g_ℓ), g_ℓ; length 3ℓ + 2 for every option of x. For y, y': if g_0 = g'_0, …, g_(i−1) = g'_(i−1) then also m_0 = m'_0, …
  (a gate determines its owner); so the first difference is at e_(g_i) vs e_(g'_i), and e-indices follow gate indices: κ(y) < κ(y') ⟺
  (gate(g_0), …, gate(g_ℓ)) < (gate(g'_0), …, gate(g'_ℓ)) lexicographically, which is key_(s')(y) vs key_(s')(y'). ∎

## 4. Theorem REALIZE (PROVED, lane, on [SPEC], [1E-N3], [VJ-LOC], [RULE])
Let G ∈ IDEAL-ACYC with IDEAL run s_0 → s_1 → … → s_L (L = L(G)) and Γ(G) with start (σ_0, τ_0) (§3.1). Then the N5 run of Γ(G) from
(σ_0, τ_0) has states (σ^(s_j), τ_0) for j = 0, …, L; transitions 1, …, L are FL transitions; transition L + 1 is a fallback. So
[0, L] is ONE FL run of length exactly L(G), and the real movers' choices equal the IDEAL ones state for state.
Proof, by induction on j: state j is the standard state (σ^(s_j), τ_0) (true for j = 0).
- Step j < L (s_(j+1) ≠ s_j). S4 is computed from (σ^(s_j), τ_0).
  - τ: Iτ = ∅ (Lemma TAU), so τ_new = τ_0.
  - σ: Iσ ≠ ∅ (Lemma ESC), so S4a computes σ_new, a pointwise optimum of H ([1E-N3]); off the movers σ_new = σ (Lemma ESC).
  - Movers, by induction on the level ℓ = 0, 1, …: x is not its own W′-cycle node and TIE(x) = R(x) (Lemma W (iii)), so by [RULE]
    σ_new(x) is the κ-least gate of R(x), with κ read under (σ_new, τ_0). By Lemma KEY (a) R(x) = the gates of A_(s_j)(x); by the
    induction on ℓ, σ_new agrees with σ^(s_(j+1)) below level ℓ, so by Lemma KEY (b) the κ order on R(x) is the IDEAL key order under
    s_(j+1). So σ_new(x) = (x, s_(j+1)(x)).
  - So (σ_new, τ_new) = (σ^(s_(j+1)), τ_0) ≠ (σ, τ): no fallback (S4c fires only when σ_new = σ and τ_new = τ); τ kept; σ changed; W
    kept (Lemma W (i)). Transition j + 1 is FL, and state j + 1 is standard.
- Step L (the IDEAL run stops). If «opt», R(x) = {σ(x)} at every mover (Lemma KEY (a)); if «stuck», the IDEAL choice is s_L itself.
  Either way the argument above gives σ_new = σ^(s_L) = σ and τ_new = τ; with Iσ ≠ ∅ S4c fires: transition L + 1 is a fallback.
- Maximality: no transition precedes state 0 and transition L + 1 is a fallback, so [0, L] is a maximal FL run. ∎

## 5. Corollary REAL-IDEAL (PROVED, lane, on the same premises)
- Size: Γ(G) has n = N + 3M + 6 vertices and at most M (movers) + 2M (gates) + 2M (β) + M (e) + 2 + 8 = 6M + 10 edges; every
  Ω ≤ 4M + 9 (bmax ≤ 2M + 5, eb ≤ 2M + 6, max Ω(e) ≤ 4M + 4, top ≤ 4M + 6). Polynomial in N + M at bit cost (TARGET.md §3).
- (a) NECESSITY. Let FL-POLY mean: there is a polynomial p such that for every game Γ on n vertices and EVERY start pair, every FL run of
  N5 has length ≤ p(n) (p nondecreasing, w.l.o.g.). Let IDEAL-ACYC-POLY mean: there is a polynomial q such that L(G) ≤ q(N + M) for every G ∈ IDEAL-ACYC. Then
  FL-POLY ⇒ IDEAL-ACYC-POLY, with q(t) := p(3t + 6): by Theorem REALIZE, L(G) is the length of an FL run of Γ(G) from (σ_0, τ_0).
- (b) TRANSFER. If (G_i) ⊆ IDEAL-ACYC has L(G_i) super-polynomial in N_i + M_i, then (Γ(G_i), (σ_0, τ_0)_i) is a family of real games
  of size n_i = N_i + 3M_i + 6 whose N5 runs FROM THOSE START PAIRS contain one FL run of length L(G_i), hence ≥ L(G_i) iterations:
  super-polynomial in n_i.
- Not claimed: the converse (IDEAL-ACYC-POLY ⇒ FL-POLY); anything about the S3 default start; anything for Ξ-cyclic genomes. ∎

## 6. Scope: acyclic Ξ-graphs only
- Every use of acyclicity: Lemma PLAY (a) (chains finite, end at u, never through e), Fact X (two options' β-sets differ, so lengths never
  decide), and through them SBAR, KEY.
- Ξ-CYCLES ARE NOT COVERED. With a Ξ-cycle, Odd's reply can genuinely differ from the β-face (R167's self-referential gate: x's Ξ-face
  returns through x's own gate). DATA (this session, r187/t2.py CLASS=full, ESC on, random fastcyc genomes of any Ξ-graph): seed 187 d 3:
  14 / 30 equal (16 mismatches); seed 188 d 4: 20 mismatches of 30. R187 §1 (successor 44): σ̄ ≠ Ξ-face from the first state in the
  mismatches inspected (t3.py). No acyclic genome has ever mismatched (§7).
- Also outside: genomes that are not graded (W-targets not exactly one level down), pads > 0 (stab.py allows them; not used here), and
  any start other than (σ_0, τ_0).

## 7. DATA (labelled DATA; reproduction, not proof). Commands run in experiments/red, 2026-11-02, this commit.
- r189/lemck.py: per state j of the REAL run (n5x.step = SPEC S1-S5), checks SBAR (σ̄ = β at every gate, K2 → K1), TAU (Iτ = ∅), ESC
  ((K0, K1) ∈ Iσ; σ kept on β and K at j < L), W (W_j = W_0), AV (Iσ at movers = IDEAL availability), KEY (σ_(j+1)(x) = the least gate
  of R(x) in the root-first key read off the REAL game, independent of ideal.py; and the mover state = IDEAL's), FB (1..L not fallbacks
  and change σ; L + 1 a fallback). Counts are violations.

| input | L | SBAR | TAU | ESC | W | AV | KEY | FB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| the 7 R178 champions (big_d3/d4/d6/d8_k3_W3, grow_top_N15, grow_top_N24, grow_bottom_N24) | 17 / 32 / 42 / 54 / 39 / 64 / 48 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| R188 x3_L8, g4_L12 | 8 / 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 60 random ACYC (--rand 20 3 451, 20 4 187, 20 5 452; downgen.randacyc) | 0-2 each (sums 19 / 24 / 20) | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 60 perturbed champions (--perturb 60 189: 1-6 fastcyc mutations, kept only if acyclic) | 1-64 (sum 1011) | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
- r187/realck.py (successor 44's end-to-end check: FAITHFUL = IDEAL length, mover states equal): the 7 champions IDEAL 17 / 32 / 42 /
  54 / 39 / 64 / 48, all «stuck», FAITHFUL equal, EQUAL True; --rand 20 3 451 / 20 4 187 / 20 5 452: 20 / 20 equal each.
- Pins (built by r187/stab.py from the genome named, byte-identical to a fresh build; each passes r187/pinck.sh: startck (validated
  start pair, D-ODD-1 strict), Oink 8fbf0a7 --zlk + verify (regions = N5's), --tl + verify, xeng (n5b and n5.py: identical states)):

| pin | genome | n | L_FL | sha1 .pg | sha1 .start |
| --- | --- | --- | --- | --- | --- |
| r187/instances/stab_d4_n126 | r178/out/big_d4_k3_W3.json | 126 | 32 | 06f81991e8140f0cd851b2ff107776dfc92bcfcb | 337b01154e2119ccd344d323410a201fae398e58 |
| r187/instances/stab_g24_n246 | r178/out/grow_top_N24.json | 246 | 64 | 55295dd859fc632196e23127dd2d3dc8426d4607 | 3cd50ed19ebfce8735a8d32ba29983ddfd41dbb9 |
| r188/instances/x3_L8_n48 | r188/instances/x3_L8.json | 48 | 8 | 158ca15db07ff2080239bf4fc35af14c814e5336 | f07be77086026f975a7d245a48441f550b6a8e08 |
| r188/instances/g4_L12_n62 | r188/instances/g4_L12.json | 62 | 12 | 658f4e23ca3c6bb7daccf790007c2ba856abb848 | 9f3e1f92f8998c49cd06864d3595f28a208f4d55 |
- check.sh block «P-N5-REALIZE» runs the champion rows, the R188 rows, --rand 20 4 187, --perturb 60 189, the frozen sha1s, and the pins.
- What the data says about L (DATA, R178 / R187 / R188, not part of the statement): every IDEAL-ACYC run found is LINEAR in N
  (L / n ≈ 0.2-0.26 on the champions); exact z3 maxima on the 2-wide ladder 4 (d 2), 8 (d 3, relaxation L 9 UNSAT).

## 8. Honest limits (READING)
- It bounds NOTHING. It does not say IDEAL-ACYC runs are long (all data: linear) or short (CONJECTURE IDEAL-LIN, R178, open).
- It is a REDUCTION / NECESSITY statement: a proof of FL-POLY must in particular bound L on IDEAL-ACYC, where σ̄ and τ are FIXED BY FACT
  (gadgets), so σ̄-optimality and τ-stability give no further leverage there (R187 §3, §5).
- (b) gives a real family only FROM THE GIVEN START PAIR (σ_0, τ_0); whether N5's default start S3 reaches such a state is not
  addressed. A kill of G-N5-TIME in its S3 form would need that separately.
- It covers acyclic Ξ-graphs only (§6). The IDEAL model with Ξ-cycles (fastcyc CLASS=full) is not realised by these gadgets.
- It uses the standing premise [1E-N3] and the L46 citation form of [RULE], exactly as RESULTS R103 does; [VJ-LOC] is the direction of
  VJ00 Lemma 5.8 that holds. No Lean.
- Lemma W (iii) gives bridge B's conclusion (old and new option fully W′-optimal) directly, for every arena option and without bridge B's
  FL hypothesis; bridge B (RESULTS R103) is cited as CF-1 asks but is not needed in the proof.
