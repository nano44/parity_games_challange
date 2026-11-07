# Packet P-N5-REACH (box 189): N5 from its default start S3 never reaches R104's IDEAL run on Γ(G) (NO-REACH), but on the S3-padded game Γ3(G) of size N + 7M + 10 the N5 run FROM S3 contains R104's FL run of length exactly L(G) (REACH3); so a polynomial iteration bound for N5 as specified implies IDEAL-ACYC-POLY (Corollary REAL-IDEAL-S3, a reduction only)
L-NEW successor 58 (Opus 5.5), D1 / D14 / D18; Lead 2026-11-07 02:28Z: «freeze P-N5-REACH for both referees», contents «NO-REACH;
S3-START; PAD; the lemma-by-lemma transfer of P-N5-REALIZE …; Theorem REACH3; Corollary REAL-IDEAL-S3; DEAD SUBDIV with its n = 3
instance». Written 2026-11-07 from 02:30Z (date -u: see the commit). FROZEN at push: later text goes into docs/new/P-N5-REACH-fixes.md
(append-only). Source (history only): docs/new/N5-REACH-box189.md (f55dac37). This packet carries every proof in full and is checked
against this text only. Labels: PROVED (L-NEW 58, unrefereed) / DEAD (instance, machine-checked) / DATA / CONJECTURE / READING (not to
sign). NOT a TARGET.md claim; does NOT decide G-N5-TIME; NOT M3; not a step-4 pass. It bounds nothing and asserts nothing about whether
long IDEAL-ACYC runs exist.

## To sign, and what is not to sign
| § | statement | label | hypotheses |
| --- | --- | --- | --- |
| §2 | Theorem NO-REACH (a)-(c); (d) | PROVED | (a)-(c): every genome G, Γ(G) of R104; (d): G ∈ IDEAL-ACYC |
| §3 | the game Γ3(G) (definition) and its size | definition + count | every genome |
| §4 | Lemma S3-START | PROVED | every genome |
| §5 | Lemma PAD (a)-(c) | PROVED | every genome |
| §6 | Lemmas K3, PLAY3, SBAR3, TAU3, ESC3, W3, KEY3 (the transfer of P-N5-REALIZE §3) | PROVED | G ∈ IDEAL-ACYC (K3, TAU3: every genome) |
| §7 | Theorem REACH3 | PROVED | G ∈ IDEAL-ACYC |
| §8 | Corollary REAL-IDEAL-S3 (a), (b) | PROVED (reduction / necessity only) | |
| §9 | DEAD SUBDIV (instances A, B) | DEAD | |
| §10-§13 | DATA, conjectures, context, machine checks, TARGET diff, limits | DATA / CONJECTURE / READING (not to sign) | |

## 1. Premises (LANDED only; quoted verbatim, trunk claude/vibrant-johnson-nxvvxo 6ca995ed, docs/RESULTS.md line numbers)
- [DEF] RESULTS R104 (l. 9864), its definitions only (the IDEAL model, L(G), the Ξ-graph, Γ(G), its start, the FL run). Quoted:
  «an IDEAL genome G has N movers x with levels lev(x), M := Σ deg(x) options (x, k), each with a W-target of level lev(x) − 1 (none at
  level 0), a Ξ-target xt(x, k), a mover or the exit X, a distinct β-rank with a parity, a distinct gate index, and a start; under a state
  s the Ξ-value of option (x, k) is the set of β's on its chain (x, k), (xt, s(xt)), … up to the first Ξ-target X, compared by the β of
  largest rank in the symmetric difference: the option whose set contains that β is the better one if its parity is even and the worse
  one if odd; an IDEAL step moves every mover to the lexicographically least key (gate indices of the chain of W-targets under the new
  state, lowest level first) among its current option and the options with a strictly better Ξ-value, and the run stops when nothing is
  available or nothing changes, L(G) := its number of steps; the Ξ-graph has an edge x → xt(x, k) for every option with a mover as
  Ξ-target»; «the game Γ(G) on n = N + 3M + 6 vertices (Even movers of priority 0; Odd gates of priority 1 with a W-face e and a Ξ-face
  β; β of priority 6 + 2·rank + parity with edges to the Ξ-target and to u, or to u alone; e of even priority above every β with one edge
  to the W-target or to the top even self-loop c_W; an unused even self-loop of priority 2; c_W's priority top is the least even number at
  least 2 above every other priority so far; a closed core u = K0 (Even, top + 2) → {K1, K3}, K1 (Even, 5) → {K0, K1}, K2 (Odd, 3) →
  {K1, K2}, K3 (Even, top + 3) → {K1, K2}; vertex indices: movers, gates in gate-index order, β-vertices, e-vertices in the order of their
  gates' gate indices, the unused loop, c_W, K0 to K3 (packet §3.1), on which the root-first key comparison depends) with start σ = the
  genome start at movers, β → its Ξ-target (u when the target is X), K0 → K3, K1 → K1, K3 → K2, τ = e at every gate and K2 → K2»;
  «one FL run (a maximal set of consecutive non-fallback transitions that keep τ, change σ and keep that valuation everywhere)», «that
  valuation» being «the valuation of the (σ, τ)-play». Where the line leaves a detail to «packet §3.1» (the text of record, R104 l. 9878-9879
  «The packet read with its fixes is the text of» «record.»), this packet uses that detail: β-vertices in option order; Ω(e) := eb + 2i
  with eb the least even number above every Ω(β) and i the position of the gate in the order (lev(owner), gate index). The proofs below
  use of Ω(e) only that it is even and lies strictly between every Ω(β) and top. No THEOREM of R104 is used.
- [SPEC] SPEC S1-S5 with FIX 1-4 (docs/new/N5-ssi-global.md, «## SPEC (EXACT …)», l. 24 ff., trunk sha1 66fde9ef…), the N5 of RESULTS
  R57 and R104 (R104 l. 9864 «N5 (SPEC S1-S5 …)»). Used verbatim: S2 (l. 47) «Iσ = {(v, w) : owner(v) = Even, w ≠ σ(v), Ξσ(w) strictly
  better than Ξσ(σ(v))}; Iτ the same on G^d for τ.»; S3 (l. 48-49) «Start (unless a start pair is given): Even v: σ(v) = the successor w
  maximising (r(w), w if r(w) even else −w), r(w) = Ω(w) if» «even else −Ω(w) (PGSolver best-reward); Odd v: the same rule on G^d (r
  computed from Ω + 1).»; FIX 1 (l. 81-83) «highest even priority, else lowest odd priority; equal priorities: largest index if even,
  smallest if odd. Odd's v (the rule on G^d), in» «G's terms: highest ODD Ω(w), else lowest EVEN Ω(w); equal priorities: largest index
  if Ω(w) odd, smallest if even.»; S4a (l. 51) «A(v) = {σ(v)} ∪ {w : (v, w) ∈ Iσ} for Even v. Arena H: Even v keeps only edges to A(v);
  Odd v keeps only the edge» «to τ(v).», «Else σ_new = σ.» (l. 53); S4b (l. 54-55) the same for τ, «Else τ_new = τ.»; S4c (l. 56-57)
  «FALLBACK, if σ_new = σ and τ_new = τ: if Iσ ≠ ∅, for every Even v with an improving edge set σ_new(v) = the w with (v, w) ∈ Iσ»
  «maximising (Ξσ(w), w) …; otherwise do the same for Odd on Iτ»; S1 (l. 26-46): values (c, P, ℓ), the order, «Odd's side: everything
  on the DUAL game G^d (owner swapped, Ω + 1); τ is an "Even" strategy of G^d; Ξτ, τ̄ (= Even's optimal» «counterstrategy to τ, as a
  G^d-Odd strategy), Iτ computed there.»
- [1E-N3] R104's premise as landed (R104 l. 9975-9978): «under the standing SPEC premise of RESULTS R57 (1E-N3: «that S1's procedure
  realises an optimal σ̄ is VJ00 §6 plus SPEC conformance», RESULTS R57 (b), read on every valid input of S1's procedure (Lead reading
  L45, RESULTS R102), used in two forms: S1's σ̄, and τ̄ on the dual game, are pointwise optima; and S4a's σ_new, S1's output on the dual
  of the one-player arena in which Even y keeps {σ(y)} ∪ Iσ(y) and Odd follows τ, is a pointwise optimum of that arena, before S4c)»;
  R57 (b) (l. 2915-2916): «that S1's procedure realises an optimal σ̄ is VJ00 §6» «plus SPEC conformance, and the code's match to SPEC is
  DATA (R15 G-N5T-1) (1E-N3 = N-1E-1).» Forms P1 (σ̄, τ̄ pointwise optima) and P2 (S4a's σ_new a pointwise optimum of H).
- [RULE] R104's premise as landed (R104 l. 9989-9992): «with RESULTS R24 (a) Lemma R and R24 (b)'s choice rule (TB proof steps 1, 3-5;
  fixes §2.3) with RESULTS R103's bridge B, whose proof uses no 𝒞^1O hypothesis (Lead reading L46 and its amendment), applied at every
  Even vertex that is not its own W′-cycle node, non-movers included (RESULTS R103's (R1) ruling)». Form used (R104's form, its l.
  10004-10005 «σ_j(x) is the κ_j-least element of» «TIE_j(x)», read as «σ_new(x) (= σ_j(x) at a» «non-fallback transition)»): at a
  transition with Iσ ≠ ∅, for every Even x that is not its own W′-cycle node (W′ := the value of S4a's pointwise optimum of H), σ_new(x)
  is the κ-least element of TIE(x) := the options y of x in H with W′(x) = x ⊕ W′(y) that are not corners (x does not occur on y's play
  before its cycle node); κ(y) := the vertex sequence of the (σ_new, τ) play path from the W′-cycle node c of x to y, c excluded,
  compared lexicographically by index (root-first key).
- [VJ-LOC] R104's premise as landed (R104 l. 10011-10012): «local optimality in a one-player game (RESULTS R36 (c) Lemma P1, applied on
  the dual game to Odd's one-player game against a fixed σ; VJ00's two-player Lemma 5.8 is not used)»; R36 (c) (l. 1730-1731): «if σ is a
  positional Even strategy of a one-player game H with no improving edge (no Even edge (x, y) with V_σ(y) ▷ V_σ(σ(x))), then V_σ(v) ⊵
  V_{σ′}(v) for every positional Even strategy σ′ and every vertex v»; setting (l. 1723-1724): «A ONE-PLAYER game» «is a game in which
  every non-Even vertex has one successor».
- [TERM] RESULTS R15 (d) (l. 640-642): «N5: every iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ (on G) and/or with ∅ ≠ I ⊆ Iτ
  to Odd's τ (on G^d), and» «changes at least one of them …» «Hence no (σ, τ) state repeats and N5 terminates». Used only for the
  finiteness of L(G) in §7. R15 (a) is not used (NO-REACH needs only S4a/S4c's text).
- Nothing else is used. P-N5-REALIZE (claude/l-red docs/red/P-N5-REALIZE.md, sha1 067f06b6…, fixes entries 1-3) is the SOURCE of the
  proof pattern of §6; every step of §6 is proved here.

## 0. Notation and two facts (PROVED, from [SPEC] S1, S2 only)
- p'(v) := 2·rank(v) + (Ω(v) mod 2), rank by (Ω(v), v) (SPEC S1). A value is (c, P, ℓ); ⊳ = «better for Even»: reward of c (p'(c) if
  Ω(c) even, −p'(c) if odd), then P by its most relevant element of the symmetric difference and its parity, then ℓ (c odd: longer
  is better for Even; c even: shorter). v ⊕ (c, P, ℓ) := (c, P ∪ {v : p'(v) > p'(c)}, ℓ + 1), the value of v when v steps to a vertex of
  value (c, P, ℓ) and v is not on the cycle. Ξσ: σ with Odd's optimal σ̄ (SPEC S1). φ_(σ,ρ): the play value of a strategy pair.
- Fact DUAL. G^d has the same ranks (Ω + 1 keeps the order and the index ties) and the same P-membership; rewards map by x ↦ −x − 1;
  signed weights change sign; the length rule swaps with the parity of c. So G^d's order is the reverse of Γ's: Iτ(v) = {w ≠ τ(v) :
  Ξτ(w) ◁ Ξτ(τ(v))} in Γ's order, and τ̄ (Even's reply on G^d's Odd side) MAXIMISES Γ's order at every vertex ([1E-N3] P1).
- Fact X (IDEAL-ACYC). For two options k ≠ k' of one mover x and any state s, B_s(x, k) ≠ B_s(x, k'), where B_s(x, k) is the set of
  β-ids on the X-chain of (x, k) under s. Proof: after its first option, the chain of (x, k') visits only movers reachable from x by ≥ 1
  Ξ-edge, so (acyclic) never x, never the option (x, k), never its β-id b(x, k) (β-ids are a bijection on options); b(x, k) ∈ B_s(x, k).
  Hence, by [DEF]'s comparison, the order of two options' Ξ-values is decided by the β of largest rank in the symmetric difference.

## 2. Theorem NO-REACH (PROVED)
Let G be ANY genome and Γ(G) as in [DEF]; let (σ_j, τ_j), j = 0, 1, …, be the N5 run of Γ(G) from S3. Then for every j:
- (a) σ_j(K0) = K1 and σ_j(K1) = K0;
- (b) Ξσ_j(K0) = (K0, ∅, 0); no state (σ_j, τ_j) is a standard state of R104 (one with σ(K0) = K3, σ(K1) = K1); in particular no
  state of the run is a state of R104's REALIZE run for any mover state s;
- (c) K0 and K1 have no improving edge at any state: Iσ_j contains no edge out of K0 or K1.
- (d) If G ∈ IDEAL-ACYC: for every j and every vertex v ∉ {K2, K3, c_X}, the cycle node of Ξσ_j(v) ranks above every β-vertex, hence
  no β-vertex lies in the P-set of Ξσ_j(v).
Proof.
- j = 0 (S3, FIX 1). K0's successors are K1 (Ω 5) and K3 (Ω top + 3; top is even): both odd, the lowest is K1. K1's successors are K0
  (Ω top + 2, even) and K1 (Ω 5, odd): the even one, K0. So (a) holds at j = 0.
- Step. Suppose (a) at j. Both K0, K1 are Even, so the play from K0 is K0 → K1 → K0 → … whatever Odd does; the cycle {K0, K1} has the
  larger p' at K0: Ξσ_j(K0) = (K0, ∅, 0), Ξσ_j(K1) = K1 ⊕ Ξσ_j(K0) = (K0, ∅, 1) (rank(K1) < rank(K0)). (c): K1's other successor is K1
  itself: Ξσ_j(K1) = (K0, ∅, 1) vs Ξσ_j(σ_j(K1)) = Ξσ_j(K0) = (K0, ∅, 0): same c and P, c even, the shorter is better: not improving.
  K0's other successor is K3, with σ_j(K3) ∈ {K1, K2}. If σ_j(K3) = K1, Ξσ_j(K3) = (K0, {K3}, 2), and the symmetric difference with
  Ξσ_j(K1) = (K0, ∅, 1) is {K3}, odd Ω: K3 is worse: not improving. If σ_j(K3) = K2: Odd at K2 may keep its self-loop, a play of
  value (K2, {K3}, 1) from K3 with reward −p'(K2) < 0; σ̄_j is a pointwise optimum for Odd ([1E-N3] P1), so Ξσ_j(K3) ⊴ that value, reward
  < 0 < p'(K0): not improving. So no edge out of K0 or K1 is in Iσ_j. By SPEC S4a, σ_new(v) ∈ A(v) = {σ(v)} ∪ Iσ(v) («Else σ_new = σ»);
  S4c changes only vertices «with an improving edge» in Iσ (or, if Iσ = ∅, only τ). So σ_(j+1)(K0) = K1, σ_(j+1)(K1) = K0. This
  proves (a) and (c) by induction, and the value in (b); the rest of (b) is (a).
- (d) Under σ_j the only edge into K from outside is β → u = K0 ([DEF]: K is closed; β's edges are «to the Ξ-target and to u, or to u
  alone»), and by (a) K0 → K1 → K0 is fixed, so K2, K3 are reached from outside K by no σ_j-play; from v ∉ K the cycle reached inside K
  is {K0, K1} with node K0. A cycle outside K is a loop of c_W or c_X or uses an e-vertex: without e-vertices it would use only edges
  mover → gate, gate → β, β → mover, i.e. it would be a cycle of the Ξ-graph (an edge x → xt(x, k)), excluded by acyclicity. Its node is
  then an e-vertex or a vertex above it (Ω(e) > every Ω(β)). So the cycle node of Ξσ_j(v), v ∉ {K2, K3, c_X}, is K0, c_W or an e-vertex,
  each ranked above every β (Ω(β) < Ω(e) < top < top + 2); P-sets hold only vertices ranked above the cycle node. ∎
- Not claimed: anything about τ_j beyond what SPEC does; the iteration count (DATA §10: 1 iteration on every genome tried).

## 3. The S3-padded game Γ3(G) (definition) and its size
A PAD on an edge a → b is a new Even vertex p with the single edge p → b, the edge a → b being replaced by a → p. Γ3(G) is Γ(G) ([DEF],
with its vertex indices, priorities and owners unchanged) with these pads, appended after Γ's vertices in the order pA, s, q, r, pe
(gate-index order), pβ (gate-index order), pb (option order), m (gate-index order):
- core: pA (Ω 0) on K0 → K3; s (Ω 0) on the self-loop of K1 (K1 → s → K1); q (Ω 1) on K1 → K0; r (Ω 0) on K2 → K1;
- gates: pe_g (Ω 1) on g → e_g, and pβ_g (Ω 0) on g → β_g;
- escapes: pb_g (Ω 1) on β_g → u (for every gate g, also when xt(g) = X);
- movers: m_(x,k) on x → g_(x,k), with Ω 2 if k = start(x) and Ω 0 otherwise.
top, the priority of c_W, is computed as in [DEF] and is unchanged (every pad has Ω ≤ 2). Count: 4 + 2M + M + M = 4M + 4 pads, so
n3 = N + 3M + 6 + 4M + 4 = N + 7M + 10; each pad adds one vertex and one edge; the largest priority is that of Γ(G). The input size of
Γ3(G) is polynomial in N + M at bit cost (TARGET.md §3).
Transport. Every pad has one successor, so the positional strategies of the two players in Γ and in Γ3 correspond one to one (a choice
a → b of Γ is a → p(a, b) in Γ3 when that edge is padded, a → b otherwise), and plays correspond with pads inserted. The STANDARD STATE
of Γ3 for a mover state s is the transport of R104's start with the genome start replaced by s: σ(x) = m_(x,s(x)); σ(β_g) = xt(g) if
xt(g) is a mover, pb_g otherwise; σ(K0) = pA, σ(K1) = s, σ(K3) = K2; τ(g) = pe_g at every gate, τ(K2) = K2; forced choices elsewhere.

## 4. Lemma S3-START (PROVED; every genome)
S3's start pair on Γ3(G) is the standard state of Γ3 for the genome start s_0.
Proof, by [SPEC] S3 / FIX 1 at every vertex with two or more successors. Mover x: its successors are its pads m_(x,k), all even; the
highest is the unique Ω-2 pad, that of start(x). β_g with xt(g) a mover: xt(g) (Ω 0, even) and pb_g (Ω 1, odd): the even one, xt(g).
K0: K1 (Ω 5, odd) and pA (Ω 0, even): pA. K1: q (Ω 1, odd) and s (Ω 0, even): s. K3: K1 (Ω 5) and K2 (Ω 3), both odd: the lowest,
K2. Odd gate g: pe_g (Ω 1, odd) and pβ_g (Ω 0, even): the highest odd, pe_g. Odd K2: r (Ω 0, even) and K2 (Ω 3, odd): K2. ∎

## 5. Lemma PAD (PROVED; every genome)
(a) Every cycle of Γ3 other than the self-loop of c_X contains a vertex of Ω ≥ 3. (b) Hence, for every pair of positional strategies and
every vertex v ≠ c_X, the cycle node c of v's play has Ω(c) ≥ 3 > Ω(p) for every pad p: no pad is a cycle node and no pad is in a P-set.
(c) Hence the value in Γ3 of a vertex v of Γ under transported strategies is (c, P, ℓ + π), where (c, P, ℓ) is the value in Γ and π
is the number of pads on the play before c; for a pad p, value(p) = p ⊕ value(its successor), with the same c and P. Two values compare
as in Γ when their pairs (c, P) differ; only when (c, P) agree do the padded lengths decide.
Proof. (a) A pad's successor is a vertex of Γ, so every cycle contains a vertex of Γ. Every cycle inside K ∪ {pA, s, q, r} contains K0,
K1 or K3 (the successors of those pads; K2's only cycle without them is its own loop, Ω 3), all with Ω ≥ 3. A cycle through a mover
passes a gate; a gate's successors are pe_g → e_g and pβ_g → β_g, with Ω(e_g), Ω(β_g) ≥ 6; a cycle made only of movers, gates and pads
does not exist (a gate is left only towards e or β); c_W's loop has Ω top; c_X has no in-edge other than its loop. (b) Ranks order by Ω
first, so rank(p) < rank(c); P holds only vertices with p' > p'(c). (c) Follows from (b): inserting pads changes neither c nor P. ∎

## 6. The lemmas on Γ3 (PROVED): the transfer of P-N5-REALIZE §3 (Lemmas K, PLAY, SBAR, TAU, ESC, W, KEY)
Fix a mover state s and the standard state (σ, τ) of Γ3 for s (§3). Transfer key for the referees: each lemma below is the packet's
lemma on Γ3; «REWARD», «P-SET» or «LENGTH» names what decides each comparison, and «INDEX» marks where vertex indices decide. By PAD (c),
comparisons decided by REWARD or P-SET are those of Γ; the LENGTH and INDEX spots are re-proved with the padded lengths and indices.
Rank facts (from [DEF] and §3): pads, movers, gates, c_X < K2 (Ω 3) < K1 (Ω 5) < every β < every e < c_W < K0 < K3.

### 6.1 Lemma K3 (the core; every genome). Let ρ_K(K2) := r.
- (a) Under σ and ρ_K: K1 ↦ (K1, ∅, 0); s ↦ (K1, ∅, 1); r ↦ (K1, ∅, 1); K2 ↦ (K1, ∅, 2); K3 ↦ (K1, {K3}, 3); pA ↦ (K1, {K3}, 4);
  K0 ↦ (K1, {K0, K3}, 5); q ↦ (K1, {K0, K3}, 6). (Plays: K1 → s → K1, cycle node K1; K3 → K2 → r → K1; K0 → pA → K3 → …; P collects
  K3 and K0, the only vertices above K1 on these plays.)
- (b) Iσ ∩ (edges out of K0, K1, K3) = {(K0, K1)}. K0: K1 (K1, ∅, 0) vs pA (K1, {K3}, 4): P-SET, difference {K3} odd, K1 better:
  improving. K1: q (K1, {K0, K3}, 6) vs s (K1, ∅, 1): P-SET, top of the difference K3, odd, q worse: not improving. K3: K1 (K1, ∅, 0) vs
  σ(K3) = K2 (K1, ∅, 2): LENGTH, c = K1 odd, the longer is better for Even, so K2 is better: not improving (in Γ: 0 vs 1, the same
  direction). These values hold once SBAR3 gives σ̄(K2) = r.
- (c) Iτ ∩ {edges out of K2} = ∅. τ(K2) = K2: Ξτ(K2) = (K2, ∅, 0), reward −p'(K2) < 0. From r, Even may play r → K1 → q → K0 → K1 …,
  a cycle with node K0 (Ω top + 2, the largest on {K1, q, K0}); τ̄ maximises Γ's order (Fact DUAL), so Ξτ(r) has reward ≥ p'(K0) > 0:
  REWARD, r is worse for Odd. (Uses no acyclicity.)
- (d) In S4a's arena H: by (b), K0 keeps {pA, K1}, K1 keeps {s}, K3 keeps {K2}, and Odd's K2 follows τ: K2 → K2. The H-plays from K0
  are K0 → K1 → s → K1 … (node K1, odd) and K0 → pA → K3 → K2 → K2 … (node K2, odd): REWARD, −p'(K2) > −p'(K1), so pA is strictly
  better; K0 lies on no cycle of H, so every pointwise optimum of H chooses pA at K0 (value(K0) = K0 ⊕ value(choice), and ⊕ by a vertex
  outside P keeps the order); K1, K3 have one option in H. So every pointwise optimum of H agrees with σ on K0, K1, K3; and every play of
  H from u = K0 ends in an odd cycle (node K1 or K2).

### 6.2 Lemma PLAY3 (play shapes; IDEAL-ACYC). Let ρ := pβ_g at every gate g and r at K2; φ := φ_(σ,ρ).
- (a) The play from β_g follows the X-chain of g: β_g → xt(g) → m → g' → pβ_(g') → β_(g') → … until the first option with xt = X,
  then pb → K0 → pA → K3 → K2 → r → K1 → s → K1 …; it repeats no mover (acyclic) and meets no e-vertex, c_W or c_X. So φ(β_g) = (K1,
  B(g) ∪ {K0, K3}, ·) with B(g) := {β_h : h on the X-chain of g under s}; φ(pβ_g) and φ(g) have the same c and P.
- (b) lev = 0: pe_g → e_g → c_W: φ(e_g) = (c_W, ∅, 1), φ(pe_g) = (c_W, ∅, 2).
- (c) lev ≥ 1: pe_g → e_g → wt(g) → m → g' → pβ_(g') → β_(g') → (a): φ(pe_g) = (K1, {e_g} ∪ B(g') ∪ {K0, K3}, ·); e_g occurs once.
Proof: read off the edges; P by the rank facts (β, e, K0, K3 above K1; pads, movers, gates, K2 below). ∎

### 6.3 Lemma SBAR3 (Odd's best reply is the β-face; IDEAL-ACYC). σ̄ = ρ, hence Ξσ = φ.
- (i) No Odd-improving switch for ρ w.r.t. φ. Gate, lev ≥ 1: φ(pe_g) vs φ(pβ_g): same node K1; the P-sets differ by e_g and by
  β-vertices (K0, K3 in both); e_g is even and outranks every β: P-SET, pe_g is better for Even, so worse for Odd. Gate, lev = 0: node
  c_W (even) vs K1 (odd): REWARD, Odd prefers pβ_g. K2: the switch from r to K2's loop gives K2 the value φ(K2) = (K1, ∅, 2) (by (a) of
  K3 the current play K2 → r → K1) versus φ(r) = (K1, ∅, 1): LENGTH, c = K1 odd, the longer φ(K2) is better for Even, so the loop is
  worse for Odd (in Γ: 1 vs 0, the same direction).
- (ii) By [VJ-LOC] (R36 (c) P1 on G^d, where Γ with Even fixed to σ is one-player for G^d's Even = Odd; by Fact DUAL «no improving
  edge» there is (i), and P1's conclusion is: ρ is Odd's pointwise optimum against σ) and [1E-N3] P1 (σ̄ is a pointwise optimum),
  φ = φ_(σ,σ̄) = Ξσ at every vertex.
- (iii) σ̄ = ρ. Suppose σ̄(g) = pe_g at a gate g. If g lies on the cycle of its own (σ, σ̄)-play, that cycle passes e_g and avoids K,
  c_W, c_X (closed, resp. loops); its most relevant vertex is an e-vertex (e outranks movers, gates, pads, β): an EVEN node, while φ(g)
  has the odd node K1: contradiction with (ii). Otherwise φ_(σ,σ̄)(g) = g ⊕ (pe_g ⊕ φ(e_g)) differs from φ(g) = g ⊕ φ(pβ_g): by the node
  (lev 0) or by e_g in P (lev ≥ 1): contradiction. Suppose σ̄(K2) = K2: K2's play is its loop, node K2 ≠ K1: contradiction. ∎

### 6.4 Lemma TAU3 (τ stays; every genome). In the standard state, Iτ = ∅, so S4b leaves τ unchanged.
Odd vertices are the gates and K2 (K2: K3 (c)). Gate g with τ(g) = pe_g: under τ every gate takes its e-face, so every play from pe_g,
whatever Even does (movers choose pads → gates; e → W-target or c_W), ends in the loop of c_W: Ξτ(pe_g) has reward p'(c_W). From pβ_g,
Even may play β_g → pb_g → K0 → K1 → q → K0 …, node K0 (Ω top + 2, above c_W); τ̄ maximises (Fact DUAL), so Ξτ(pβ_g) has reward ≥
p'(K0) > p'(c_W): REWARD, pβ_g is worse for Odd: (g, pβ_g) ∉ Iτ. ∎

### 6.5 Lemma ESC3 (S4a keeps σ off the movers; IDEAL-ACYC). In the standard state, Iσ ∋ (K0, K1) (so Iσ ≠ ∅), and every pointwise
optimum of S4a's arena H agrees with σ at every Even vertex that is not a mover.
β_g with xt(g) a mover: its options in H are within {xt(g), pb_g}. In H Odd follows τ (pe at gates), so every H-play from xt(g) is mover
→ pad → gate → pe → e → … → c_W, node c_W (even); every H-play from pb_g → u ends in an odd cycle (K3 (d)): REWARD, xt(g) is strictly
better; β_g is on no cycle of H; so a pointwise optimum chooses xt(g). Core: K3 (d). Pads, e, c_X, c_W, β_g with xt = X: one successor. ∎

### 6.6 Lemma W3 (W graded and constant; the arena optimum; IDEAL-ACYC). In every standard state, and for every s:
- (i) W, the value of the (σ, τ)-play: from a mover x of level ℓ the play is x → m → g → pe_g → e_g → (level ℓ − 1) → … → c_W, five
  steps per level, through vertices below c_W; so W(x) = (c_W, ∅, 5ℓ + 5), W(m_(x,k)) = (c_W, ∅, 5ℓ + 4) for the pad on the play,
  W(g) = (c_W, ∅, 5ℓ + 3), W(pe_g) = (c_W, ∅, 5ℓ + 2), W(e_g) = (c_W, ∅, 5ℓ + 1); W(β_g) = (c_W, ∅, 5·lev(xt(g)) + 6) when xt(g) is a
  mover; on β_g with xt = X, pβ, pb, K ∪ {pA, s, q, r}, c_X, c_W the play never meets a mover, so W there does not depend on s. Every
  vertex's W depends on lev only, not on s or on the chosen option: W is the SAME in every standard state. (LENGTH values, re-counted.)
- (ii) In H every play from a gate of a level-ℓ mover follows τ (pe), and every option of a mover in H is a pad m_(x,k) leading to its
  gate, so it ends at c_W after exactly the steps of (i) and meets nothing above c_W: W*(m_(x,k)) = (c_W, ∅, 5ℓ + 4) for EVERY option
  m_(x,k) in H, W*(x) = (c_W, ∅, 5ℓ + 5), W′ := W*.
- (iii) For every mover x: x's W′-cycle node is c_W ≠ x; every option y ∈ R(x) := {σ(x)} ∪ Iσ(x) satisfies W′(x) = x ⊕ W′(y); none is
  a corner (y's play visits only levels < lev(x) before c_W). So TIE(x) = R(x). ∎

### 6.7 Lemma KEY3 (availability and keys are the IDEAL ones; IDEAL-ACYC). In the standard state for s, for every mover x:
- (a) R(x) = {m_(x,k) : k ∈ A_s(x)}, A_s(x) := {s(x)} ∪ {k : (x, k) strictly Ξ-better than (x, s(x)) under s} ([DEF]). By SBAR3 and
  PLAY3 (a), Ξσ(m_(x,k)) = (K1, B_s(x, k) ∪ {K0, K3}, ·). Two options of x: same node, K0, K3 cancel, B-sets differ (Fact X): P-SET,
  decided by the β of largest rank in the symmetric difference and its parity; Ω(β) = 6 + 2·rank + parity, so rank order of β-vertices
  is the β-rank order and Ω-parity is the β-parity: exactly [DEF]'s comparison. So (x, m_(x,k)) ∈ Iσ ⟺ k ≠ s(x) and (x, k) is
  Ξ-better under s.
- (b) INDEX. For y, y' ∈ R(x) and any Even σ' that agrees with the standard σ for s' on the movers of level < lev(x) (any s'), the
  root-first keys κ(y), κ(y') under (σ', τ) compare as the IDEAL keys of (x, k), (x, k') under s'. Proof: the play from y = m_ℓ (an
  option of x, level ℓ = lev(x)) is m_ℓ → g_ℓ → pe_ℓ → e_ℓ → x_(ℓ−1) → m_(ℓ−1) → g_(ℓ−1) → … → x_0 → m_0 → g_0 → pe_0 → e_0 → c_W, with
  g_i := the gate of the pad m_i and x_(i−1) := wt(g_i). Read from c_W (root first, c_W excluded): e_0, pe_0, g_0, m_0, x_0, e_1, pe_1,
  g_1, m_1, x_1, …, e_ℓ, pe_ℓ, g_ℓ, m_ℓ: length 5ℓ + 4 for every option of x. Block i (e_i, pe_i, g_i, m_i, x_i) is determined by g_i
  (a gate determines its pad, its owner and its faces). So if g_j = g'_j for j < i and g_i ≠ g'_i, the sequences agree before block i
  and first differ at e_(g_i) vs e_(g'_i). e-indices follow gate indices ([DEF]; unchanged in Γ3): κ(y) < κ(y') ⟺ (gate(g_0), …,
  gate(g_ℓ)) < (gate(g'_0), …, gate(g'_ℓ)) lexicographically, which is [DEF]'s key comparison under s'. (In Γ the block is e, g, x; the
  pad indices never decide because pe_i, m_i are determined by g_i.) ∎

## 7. Theorem REACH3 (PROVED, on [DEF], [SPEC], [1E-N3], [RULE], [VJ-LOC], [TERM])
Let G ∈ IDEAL-ACYC with IDEAL run s_0 → s_1 → … → s_L, L = L(G). Then the N5 run of Γ3(G) FROM S3 has states 0, …, L equal to the
standard states of Γ3 for s_0, …, s_L; transitions 1, …, L are FL transitions; transition L + 1 is a fallback. So, if L ≥ 1, [0, L] is
one FL run of length exactly L(G), the movers' choices are the IDEAL ones state for state, and the run makes at least L(G) + 1
iterations; if L = 0, transition 1 is a fallback and there is no FL run.
Proof, by induction on j: state j is the standard state for s_j. j = 0: Lemma S3-START.
- Step j < L (s_(j+1) ≠ s_j). τ: Iτ = ∅ (TAU3), so τ_new = τ. σ: Iσ ≠ ∅ (ESC3), so S4a computes σ_new, a pointwise optimum of H
  ([1E-N3] P2); σ_new = σ off the movers (ESC3). Movers, by induction on the level ℓ = 0, 1, …: x is not its own W′-cycle node and
  TIE(x) = R(x) (W3 (iii)), so by [RULE] σ_new(x) is the κ-least element of R(x), with κ read under (σ_new, τ). By KEY3 (a), R(x) =
  {m_(x,k) : k ∈ A_(s_j)(x)}; by the induction on ℓ, σ_new agrees with the standard σ for s_(j+1) below level ℓ, so by KEY3 (b) the κ
  order on R(x) is the IDEAL key order under s_(j+1), whose least element in A_(s_j)(x) is s_(j+1)(x) ([DEF]). So σ_new(x) = m_(x,
  s_(j+1)(x)). Hence (σ_new, τ_new) is the standard state for s_(j+1) ≠ (σ, τ): S4c does not fire; τ is kept, σ changes, and W is kept
  (W3 (i)): transition j + 1 is FL.
- Step L. The IDEAL run stops: either A_(s_L)(x) = {s_L(x)} at every x (then R(x) = {σ(x)} by KEY3 (a)), or the IDEAL choice is s_L
  itself; either way the argument above gives σ_new = σ, τ_new = τ, while Iσ ∋ (K0, K1): S4c fires, transition L + 1 is a fallback.
- Maximality: no transition precedes state 0 and transition L + 1 is a fallback. Finiteness of L(G): the induction realises every
  IDEAL step that exists as an N5 transition from S3, and N5 terminates ([TERM]); the induction does not assume finiteness. ∎

## 8. Corollary REAL-IDEAL-S3 (PROVED; a REDUCTION / NECESSITY statement only)
Let FL-S3-POLY mean: there is a nondecreasing polynomial p such that, on every parity game on n vertices, every FL run of the N5 run FROM
S3 has length ≤ p(n). Let IDEAL-ACYC-POLY mean: there is a polynomial q with L(G) ≤ q(N + M) for every G ∈ IDEAL-ACYC.
- (a) FL-S3-POLY ⇒ IDEAL-ACYC-POLY, with L(G) ≤ p(N + 7M + 10). In particular a polynomial bound p(n) on the NUMBER OF ITERATIONS of N5
  from S3 (the iteration bound of G-N5-TIME) gives L(G) + 1 ≤ p(N + 7M + 10). Proof: REACH3 on Γ3(G), n = N + 7M + 10 (§3).
- (b) Conversely, if (G_i) ⊆ IDEAL-ACYC has L(G_i) super-polynomial in N_i + M_i, then on the games Γ3(G_i) (n_i = N_i + 7M_i + 10
  vertices, polynomial input size, §3) N5 FROM ITS DEFAULT START S3 makes at least L(G_i) + 1 iterations: super-polynomially many in n_i.
- Not claimed: that such a family exists or does not exist; IDEAL-ACYC-POLY ⇒ FL-S3-POLY; anything for Ξ-cyclic genomes. This packet
  says nothing about how long IDEAL-ACYC runs are.

## 9. DEAD SUBDIV (DEAD; instances machine-checked)
Statement killed: «for every game G and every start pair (σ0, τ0), the game G^pad := G with every priority + 4 and EVERY edge (a, b)
subdivided by an Even pad p(a, b) (indices n, n + 1, … in (a, b) order; Ω(p) = 2 if a is Even and b = σ0(a), 1 if a is Odd and
b = τ0(a), 0 otherwise) has an N5 run from S3 that equals, state for state and transition for transition (fallbacks included), the
transported N5 run of G from (σ0, τ0).» (S3's start on G^pad IS the transported (σ0, τ0) by FIX 1, as on Γ3; the run is not.)
- Instance A: n = 3, Ω (3, 3, 1), owners (Odd, Even, Odd), successors 0 → {1}, 1 → {0, 1, 2}, 2 → {0}; σ0(1) = 1; τ0(0) = 1, τ0(2) = 0.
  G from (σ0, τ0): 1 iteration, 1 fallback. G^pad (n = 8) from S3: 1 iteration, 0 fallbacks. The projected state sequences are equal;
  transition 1 is a fallback in G and not in G^pad.
- Instance B: n = 5, Ω (3, 2, 4, 0, 0), owners (Odd, Odd, Even, Odd, Even), successors 0 → {1, 3, 4}, 1 → {2, 3}, 2 → {3, 4},
  3 → {0, 2, 3}, 4 → {1, 4}; σ0(2) = 4, σ0(4) = 1; τ0(0) = 4, τ0(1) = 2, τ0(3) = 2. G: 2 iterations; G^pad (n = 17): 3 iterations.
- Obstruction (READING, from the traces; not to sign): SPEC FIX 2 (l. 84-87) fixes the choice of a cycle node that belongs to the optimiser
  by a DFS that scans successors in index order and stops at the first successor equal to v. In instance A, vertex 1 of S4a's arena is
  such a node: in G its self-loop is found at depth 1; in G^pad the loop is behind the pad p(1, 1), the DFS has already pushed p(1, 2)
  and returns to 1 through 2 → 0 → 1 first, so 1's choice is p(1, 2). Γ3 does not meet this case in REACH3: no mover is its own
  W′-cycle node (W3 (iii)), and K1, whose loop passes the pad s, has the single option s in H (K3 (d)).

## 10. DATA (not to sign; each clause with its counter, unit, set and scope; output experiments/new/box189/reachcheck.out)
Sets: C14 = the 14 genomes experiments/new/box189/corpus/*.json (4 L-RED r187 A_* genomes, 10 L-LOWER l3/kill genomes order-preserving
normalised by box189/norm.py); R440 = gen(Random(seed)), seed = 1, …, 440 (box189/reachcheck.py gen: d ≤ 4 levels, ≤ 3 movers per
level, degrees 2-3). All in IDEAL-ACYC (asserted). Engine: experiments/new/box21/n5x.py (SPEC S1-S5).
- NO-REACH (a), (b) on data. Counter «C14+R440 NO-REACH runs 454 states 908: standard 0, core-not-(K0->K1,K1->K0) 0,
  cycle-node(K0)!=K0 0»: unit = states of the S3 runs on Γ(G); set = all 908 states of the 454 runs; scope = §2 (a), (b).
- NO-REACH (d) on data. Same line, «(state, vertex) pairs 42880: beta-in-P-or-low-cycle-node 0»: unit = (state, vertex) pairs with
  v ∉ {K2, K3, c_X}; set = every such pair of the 908 states; scope = §2 (d) for Ξσ.
- Iteration count of N5 from S3 on Γ(G) (no statement; DATA only): «iterations histogram {1: 454}» (unit = runs; set = C14 + R440).
- S3-START on data. «C14+R440 S3-START genomes 454: S3 != stated start 0»: unit = genomes; set = C14 + R440; scope = §4.
- PAD (b) on data. «C14+R440 PAD (state, vertex, world) triples 693030: pad-in-P-or-cycle-node-Om<3 0»: unit = (state of the Γ3 S3 run,
  vertex ≠ c_X, world ∈ {Ξσ, Ξτ}); set = every such triple; scope = §5 (b) for the strategy pairs that occur (§5 states all pairs).
- REACH3 on data. «C14+R440 REACH3 genomes 454 (states 0..L checked 1225): failures 0»: unit = genomes (a failure = some state j ≤ L
  not standard for s_j, some transition 1..L not FL, or transition L + 1 not a fallback); set = C14 + R440; scope = §7. C14 alone: 14
  genomes, 391 states, 0 failures; per genome (L, iterations, fallbacks) in the 14 «C14 …» lines, e.g. REC_d10_tower_mu30 L 35, n 310,
  38 iterations, 1 fallback; RECT_d11_T59 L 59, n 340, 62 iterations, 1 fallback. R440 alone has L ≤ 3: a weak test of REACH3.
- W3 (i) on data. «C14+R440 W3 (state, mover) pairs 11642: W(x) != (c_W, empty, 5 lev + 5) 0»: unit = (standard state j ≤ L, mover);
  scope = §6.6 (i) at movers.
- L(G) cross-check: the 10 L-LOWER genomes' L in the «C14» lines (13, 24, 59, 33, 35, 44, 48, 17, 25, 31) equal the T column of
  claude/l-lower experiments/lower/l3/kill/README.md (12216a37) for the same files: 10/10 (unit = genomes).
- Two engines and Oink (box189/xcheck.sh, output box189/xcheck.out): for the 28 games (Γ3 «_g3» and Γ «_g0» of C14), L-COMP's
  experiments/n5-second/n5b.py --mode spec from its default start: iterations and fallbacks equal n5x's on 28/28 (Γ3: L + 3 and 1; Γ:
  1 and 0); experiments/new/check_sol2.py (Oink 8fbf0a7 --zlk + harness/verify.py) on n5b's solutions: 28/28 «zielonka(oink zlk) OK
  strategies verified» (unit = games).
- SUBDIV instances: «SUBDIV-DEAD instance A n 3: … iterations 1 fallbacks 1; G^pad (n 8) from S3: iterations 1 fallbacks 0; S3 start =
  transported (s0, t0) True; projected state sequences equal True» and «instance B n 5: … iterations 2 …; G^pad (n 17) …: iterations 3»:
  scope = §9.
- No separate DATA: §0 Fact DUAL, Fact X; §2 (c) (it is a step of (a)'s proof; its effect is counted by «core-not-…»); §3 size
  (count); §5 (a), (c); §6 K3 (a)-(d), PLAY3, SBAR3, TAU3, ESC3, W3 (ii)-(iii), KEY3 (a)-(b) (their conjunction is counted by the REACH3
  counter, not separately); §8 (a), (b) (reduction, no data).

## 11. CONJECTURES (not to sign; data only) and context (not to sign)
- CONJECTURE BLIND: for G ∈ IDEAL-ACYC the whole N5 run from S3 on Γ(G) does not depend on (br, bp). Counter «R440 BLIND … genomes 440:
  S3 run changed by redrawing (br, bp) 0» (unit = genomes; redraw = a shuffle of br and fresh bp from the same Random(seed)).
  NO-REACH (d) proves the Ξσ part only.
- CONJECTURE SUBDIV-APPROX: |T(G^pad from S3) − T(G from (σ0, τ0))| ≤ 2 on every game. Counter «SUBDIV-APPROX … games 550: … histogram
  {-1: 8, 0: 506, 1: 35, 2: 1}» (unit = games: subdiv.rgame, Random(7) 400 games n ≤ 10 and Random(8) 150 games n ≤ 16).
- Context (READING): L-LOWER successor 3's REC_d10_tower (claude/l-lower 4d747490) is CANDIDATE data for long IDEAL-ACYC runs; whether
  towers extend (S(h)) is open in L-LOWER 3, L-SI 41 and L-RED 52. Nothing in §2-§9 depends on it.

## 12. Machine checks, pins, cross-check commands
- experiments/new/check.sh block «P-N5-REACH» (run by scripts/verify.sh): `python3 -I box189/reachcheck.py --approx | diff -
  box189/reachcheck.out` must be empty (~15 s), plus the sha1 pins of this packet, its line L-1, reachcheck.py, gamma3.py, subdiv.py,
  reachcheck.out and the 14 corpus genomes. (The earlier block «BOX 189 REACH» stays.)
- Pinned instances: box189/inst/REC_d10_tower_mu30_g3.pg (sha1 c6058ce5…), RECT_d11_T59_g3.pg (0825f9d1…) with their .start files and
  the Γ games _g0.pg; regenerated byte-identically by box189/writepg.py in the «BOX 189 REACH» block.
- Builder check (not in check.sh; needs an L-RED tree): `python3 experiments/new/box189/gamma3.py GENOME <tree with experiments/red/r187>`
  prints «SELFTEST gamma3.build(G, {}) == stab.build(G, 0, kgad, esc): game and start identical» (3 genomes run, f55dac37).
- Oink and second engine (not in check.sh: needs scripts/setup_oink.sh): from the repo root, `bash experiments/new/box189/xcheck.sh >
  out.txt`; each line: «name sha1 | n5b iterations I fallbacks F evals E | zielonka(oink zlk) OK strategies verified». Single game:
  `python3 experiments/n5-second/n5b.py X.pg X.sol --mode spec; python3 experiments/new/check_sol2.py X.pg X.sol 300`.

## 13. TARGET.md diff and honest limits
- TARGET.md: not a TARGET.md claim; does not decide G-N5-TIME (open); not M3; not a step-4 pass; no algorithm is claimed. «every parity
  game on n vertices» in §8 is TARGET.md §1's class («V finite», «every vertex has at least one successor (self-loops allowed), and pr :
  V → {0, 1, ..., n}»): Γ(G), Γ3(G) and the SUBDIV games are such games (every vertex of Γ3 has a successor; its priorities are those of
  Γ(G), at most top + 3 ≤ 4M + 9 by R104's packet §5 count, below n3 = N + 7M + 10); «polynomial» is in n at bit cost (TARGET.md §3).
- Limits: (i) a reduction only; it bounds nothing. (ii) Premises [1E-N3], [RULE], [VJ-LOC] as landed in R104 (the correctness of S1's
  procedure stays SPEC's requirement; code conformance is DATA, R57 (b)). (iii) Ξ-cyclic genomes are not covered. (iv) Γ3 is one padding;
  other paddings are not studied. (v) NO-REACH speaks of Γ(G) only; it does not say that N5 from S3 is fast on any class.
