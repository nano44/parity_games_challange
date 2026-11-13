# Packet P-N5-WRAP: every parity game H inside a W-flat wrapper W(H, s0) — N5′-xi from S3 on W(H, s0) is Howard's rule on H plus exactly 3 iterations (Lemma WRAP); with Claim NT and Friedmann's Theorem 6.14, N5′-xi needs 2^Ω(n) iterations on parity games with O(n²) vertices (Statement XI-EXP, CONDITIONAL on this packet) — a DEAD-END packet for the candidate N5′-xi; N5 itself is not hit
L-SI successor 53 (Opus 5.5), D18 / D1 / D21; Lead brief 2026-11-12 (DUTY 3: «the dead-end packet P-N5-WRAP (WRAP + F_n + Friedmann
[F11] Theorem 6.14; conditional statement XI-EXP «N5′-xi needs 2^Ω(n) iterations on a game with O(n²) vertices»), with the K3 / E1-E4
proofs on W in full (W-4)»). Written 2026-11-12T20:58:18Z (date -u). Sources (history only, NOT part of what is signed): docs/si/box104-map.md §3,
§5, §6 and its Addenda A-C (L-SI successors 52, 53); REFEREE successor 33's pre-read R-WRAP-preread (claude/referee e44ce56b, 90703a81),
which found no gap in WRAP and originated Claim NT. This packet carries every proof in full, on W, and is checked against this text only.
Labels: PROVED (L-SI lane, unrefereed) / PROVED, REFEREE-originated (L41: written here by the lane, to be checked by the other referee) /
CONDITIONAL / DATA / READING (not to sign) / DEAD (only after two signatures, L43). Every «…» introduced by [Q] is printed into this file
by experiments/si/pwrap/qwrap.py from its source at a pinned commit (out/qwrap.out: 30 items, 0 FAIL); nothing of it is retyped.
**SCOPE LINE: N5 (SPEC) is not affected; G-N5-TIME stays OPEN. Not a TARGET.md claim; not M3 or M4; not a gauntlet step. This is a
DEAD-END packet for N5′-xi (RESULTS R118's [N5XI]) as an M4 candidate; for N5 it proves only that these wrappers are easy (WRAP (v),
Remark 3). XI-EXP stays CONDITIONAL in this text until two referees sign.**
D1 (owner, verbatim): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the
fleet's own, as wrong until it passes the gauntlet below.» The same care applies to a kill: CLAUDE.md, «A "counterexample" from an
unfaithful implementation is not a counterexample: the referee checks pseudocode against the paper first.»

Scope (one sentence). For EVERY parity game H and every positional Even strategy s0 of H, the game W(H, s0) (n + 7·m_E + 6·m_O + n_O + 9
vertices) makes N5′-xi from SPEC's default start S3 run, at H's Even vertices, a Howard (switch-best, Vöge-Jurdziński values) run of H
from s0 and stop exactly 3 iterations after it; on [F11]'s G_n with its initial strategy no tie ever occurs (Claim NT), so that run is
the I^loc run of [F11] Theorem 6.14, and N5′-xi inherits Friedmann's lower bound.

## To sign, and what is not to sign
| § | statement | label | premises (§1) |
| --- | --- | --- | --- |
| §2 | Definition of W(H, s0) with its vertex order; size count; rank facts (R_W); standard state | DEFINITION / PROVED (count, rank facts) | [SPEC] S1 |
| §2.4 | Fact (H) (the forced arena pick, N5 and N5′-xi) | PROVED | [SPEC] S4a, [N5XI], [1E-N3] |
| §4.1 | Lemma PAD-W (W1) | PROVED | §2 |
| §4.2 | Lemma S3-W (W2) = WRAP (i) | PROVED | [SPEC] S3 / FIX 1 |
| §4.3 | Lemma K3-W (a)-(d) with Lemma K2-r-W (the core, on W, for every σ with K-config κ0) | PROVED | [SPEC] S1, S2, [1E-N3], [DUAL], (H) |
| §4.4 | Lemma ODD-W (W4) (a)-(d) (Odd's reply; values = H's values stretched by 6) | PROVED | [SPEC] S1, S2, [1E-N3], PAD-W |
| §4.5 | Lemma TAU-W (W5) = WRAP (ii) (also Lemma E0-W) | PROVED | [SPEC] S4b, S4c, FIX 3, [DUAL], K3-W (c) |
| §4.6 | Lemma ESC-W (W6) (W-flat arena) | PROVED | K3-W, (H), PAD-W |
| §4.7 | Lemma REACH-W (W7) = WRAP (iii) and the first half of (v) | PROVED | ODD-W, TAU-W, ESC-W, [N5XI], [R15c] |
| §4.8 | Lemmas E1-W, E2-W, E3-W, E4-W (a), (b); Theorem ENDGAME-W = WRAP (iv) and the second half of (v) | PROVED | K3-W, TAU-W, (H), [1E-N3], [SPEC] S4c / S5 / FIX 3, [R15d] |
| §5 | Remarks 1, 2 (READING); Remark 3 (N5 on W(H, s0): F ≤ m_E − \|V_E\| + 1) | Remark 3 PROVED under [RULE] | [RULE], ESC-W, REACH-W |
| §6 | Claim NT (no tie on a 1-sink game); Corollary NT-RUN | Claim NT: REFEREE 33's claim and proof (L41), rendered here by L-SI 53; NT-RUN PROVED (lane), CONDITIONAL on §4 | [F11] §3-§5, Lemma 5.1, Lemma 6.7; [R15a]; REACH-W |
| §7 | Statement XI-EXP (2^Ω(n) on O(n²) vertices) | CONDITIONAL on §4 and §6 being signed; [F11] Theorem 6.14 cited as published | §4, §6, [F11] |
| §8-§12 | dead-end record (draft), DATA, independent DATA, what is not here, TARGET diff, machine checks | DATA / READING (not to sign) | |

## 1. Premises (named exactly; [Q] = copied by qwrap.py from trunk claude/vibrant-johnson-nxvvxo 7fa6aff4)
- [SPEC] (docs/new/N5-ssi-global.md, «SPEC (EXACT …)», the SPEC that RESULTS R15, R57, R104, R117, R118, R124 run):
  - [Q] «injective priorities: rank(v) = position of v in V sorted by (Ω(v), v); p'(v) = 2·rank(v) + (Ω(v) mod 2).»
  - [Q] «valuation of v under (σ, σ̄): (c, P, ℓ), c = the most relevant (max p') vertex of the cycle the play from v ends in, P = set
    of vertices on the play before reaching c with p' > p'(c), ℓ = number of steps to reach c.»
  - [Q] «order (better for Even): compare reward of c (p'(c) if even, −p'(c) if odd); then P by the signed weight Σ_{u∈P} (+2^rank(u)
    if Ω(u) even else −2^rank(u)); then ℓ: if c is odd, longer is better for Even; if c even, shorter is better.»
  - [Q] «Ξσ = valuation of every vertex under σ and Odd's OPTIMAL counterstrategy σ̄ (minimising this order at every vertex at once).»
  - [Q] «Odd's side: everything on the DUAL game G^d (owner swapped, Ω + 1); τ is an "Even" strategy of G^d; Ξτ, τ̄ (= Even's optimal
    counterstrategy to τ, as a G^d-Odd strategy), Iτ computed there.»
  - [Q] «S2 Improving edges: Iσ = {(v, w) : owner(v) = Even, w ≠ σ(v), Ξσ(w) strictly better than Ξσ(σ(v))}; Iτ the same on G^d for
    τ.»
  - [Q] «S4 Iteration (one iteration = one pass with Iσ ∪ Iτ ≠ ∅; both steps computed from the SAME (σ, τ), applied together):»
  - [Q] «a. If Iσ ≠ ∅: A(v) = {σ(v)} ∪ {w : (v, w) ∈ Iσ} for Even v. Arena H: Even v keeps only edges to A(v); Odd v keeps only the
    edge to τ(v). σ_new = Odd's optimal counterstrategy (S1 procedure) in the dual of H to the dual-Even strategy τ, read as an Even
    strategy of G. (Even's one-player optimum against τ among "keep or take an improving edge".) Else σ_new = σ.»
  - [Q] «b. If Iτ ≠ ∅: A(v) = {τ(v)} ∪ {w : (v, w) ∈ Iτ} for Odd v. Arena H': Odd v keeps only edges to A(v); Even v only the edge to
    σ(v). τ_new = Odd's optimal counterstrategy (S1 procedure on H', not dual) to σ. Else τ_new = τ.»
  - [Q] «c. FALLBACK, if σ_new = σ and τ_new = τ: if Iσ ≠ ∅, for every Even v with an improving edge set σ_new(v) = the w with (v, w)
    ∈ Iσ maximising (Ξσ(w), w) (best valuation, ties: larger index); otherwise do the same for Odd on Iτ with G^d's valuations. Count
    it.»
  - [Q] «S5 Stop when Iσ = Iτ = ∅.»
  - [Q] «FIX 1 (S3, A2). Even's v: σ0(v) = argmax over successors w of (r(w), w if r(w) even else −w), r(w) = Ω(w) if Ω(w) even else
    −Ω(w): highest even priority, else lowest odd priority; equal priorities: largest index if even, smallest if odd. Odd's v (the
    rule on G^d), in G's terms: highest ODD Ω(w), else lowest EVEN Ω(w); equal priorities: largest index if Ω(w) odd, smallest if
    even.»
  - [Q] «FIX 3 (S4c, A7). In a fallback iteration with Iσ ≠ ∅ only σ changes (τ_new = τ); n5.py l. 61-62. Odd falls back only if Iσ =
    ∅.»
  The signed-weight comparison of P is the comparison by the most relevant vertex of the symmetric difference (2^rank dominates the
  sum of all lower powers): the set containing that vertex is better for Even iff its Ω is even.
- [N5XI] N5′-xi (RESULTS R118, its frozen packet docs/new/P-N5-XICYC.md l. 45-47): [Q] «SPEC S1-S5 with ONE change in S4a. At every
  Even v with |A(v)| ≥ 2 that is not its own H-cycle node, σ_new(v) := the Ξσ-best element of TIE(v) := {w ∈ A(v) : W*(v) = v ⊕
  W*(w)}. Ties go by SPEC's choice, then the larger index. Here A(v) = {σ(v)} ∪ Iσ(v).» (W* = the values of S4a's arena optimum
  in the arena H of S4a; to avoid a clash with the input game H of this packet, S4a's arena is called «the arena» below.)
- [1E-N3] RESULTS R57 (b) as landed in R104: [Q] «used in two forms: S1's σ̄, and τ̄ on the dual game, are pointwise optima; and S4a's
  σ_new, S1's output on the dual of the one-player arena in which Even y keeps {σ(y)} ∪ Iσ(y) and Odd follows τ, is a pointwise
  optimum of that arena, before S4c)» Called P1 (σ̄ and τ̄ pointwise optima) and P2 (S4a's σ_new a pointwise
  optimum of the arena) below.
- [DUAL] RESULTS R104 (a), Fact DUAL (both referees «SIGNED»): [Q] ««The order of G^d is the REVERSE of the order of Γ»; «So Iτ(v) =
  {w ≠ τ(v) : Ξτ(w) ◁ Ξτ(τ(v))} (strictly better for Odd in Γ's order),» «and τ̄ maximises Γ's order at every vertex.»»
- [R15a], [R15c], [R15d] RESULTS R15:
  - [Q] «(a) Lemma A: for any non-empty unambiguous set I of improvements of σ (VJ00 §4.4), Ωσ ⊴ Ω_{Switch_I(σ)}.»
  - [Q] «(c) Theorem: with φ(σ) = Σ_{v ∈ M⊕, Λσ(v) = v} ε(v)·k_σ(σ(v)) (ε = +1 on R−, −1 on R+) and σ ≺ σ⁺ iff Ωσ ◁ Ωσ⁺ or (Ωσ = Ωσ⁺
    and φ(σ) < φ(σ⁺)), ≺ is a strict partial order on strategies and every non-empty switch of improvements goes strictly up in ≺.
    Consequence: no strategy repeats in any VJ00 strategy-improvement run with any non-empty selection rule; φ is an integer with |φ|
    ≤ n(n−1).»
  - [Q] «(d) N5: every iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ (on G) and/or with ∅ ≠ I ⊆ Iτ to Odd's τ (on G^d), and
    changes at least one of them (S4a/S4b, or the S4c fallback, a switch-all); Iσ depends on σ alone (Ωσ is against ⊖'s optimal reply,
    not against τ). Hence no (σ, τ) state repeats and N5 terminates within h(≺_G) + h(≺_{G^d}) iterations; at most 4n(n−1) consecutive
    N5 iterations leave both Ωσ and Ωτ unchanged (two potentials φ, φ^d).»
- [RULE] (Remark 3 only) RESULTS R104's premise clause: [Q] «with RESULTS R24 (a) Lemma R and R24 (b)'s choice rule (TB proof steps 1,
  3-5; fixes §2.3) with RESULTS R103's bridge B, whose proof uses no 𝒞^1O hypothesis (Lead reading L46 and its amendment), applied at
  every Even vertex that is not its own W′-cycle node, non-movers included (RESULTS R103's (R1) ruling)»
- [F11] O. Friedmann, «An Exponential Lower Bound for the Latest Deterministic Strategy Iteration Algorithms», Logical Methods in
  Computer Science 7 (3:19), 2011; arXiv 1106.0778v2, 618,145 B, pdf sha256 46c96f44775aa2b07cad20912cb325b177e38c94cb2e40297df66b6047679611
  (opened by this lane and, independently, by REFEREE 33; p. 5 and p. 8 read as rendered pages, §2-§6.6 as pdftotext). Used: §2 («W.l.o.g.
  we assume Ω to be injective», p. 3); §3 (node valuation ϑ_(σ,τ,v) = (w_1, {v_i > w_1 | 1 ≤ i ≤ k}, k), the total order ⪯ on node
  valuations, the optimal counterstrategy τσ, Ξσ : v ↦ ϑ_(σ,τσ,v), Ξ ◁ Ξ′ iff Ξ(v) ⪯ Ξ′(v) for all v and Ξ ≠ Ξ′, the improvement arena
  and improvement policies, p. 4-6); §4 (the locally optimizing policy: «The locally optimizing policy I^loc_G selects a most profitable
  strategy decision in every point with respect to the current valuation. More formally, it holds for every strategy σ, every player 0
  node v and every w ∈ vE that w ⪯σ I^loc_G(σ)(v).», p. 6); §5 (1-sink games: Sink Existence and Sink Seeking, with ⊴ in Sink Seeking
  on the rendered page; the remark «the path-length component equals the cardinality of the path component, because all nodes except
  the sink node are more relevant than the cycle node itself»; Lemma 5.1, p. 8); §6.2 (G_n: Table 4, Figure 4, Fact 6.1 «10 · n + 4
  nodes, 1.5 · n2 + 20.5 · n + 5 edges», ι_(G_n)); Lemma 6.7 (p. 17: «(1) The game Gn is completely won by player 1.» «(2) x is the
  1-sink of Gn and the cycle component of ΞιGn (w) equals x for all w.»); Theorem 6.14 (p. 23): «Let n > 0. The Strategy Improvement
  Algorithm with the I loc -policy requires at least 2n improvement steps on Gn starting with ιGn .» (pdftotext prints superscripts
  flat: «2n» is 2^n.)
- Not used: any lemma of P-N5-REACH, P-N5-CHAIN, P-N5-END, R117, R118, R124, R125 (their proofs about Γ3(G) were the templates of §4;
  every step is re-proved here on W); FREE-REACH and F_n (box 104 §4, not in this packet: §11); [F11]'s Lemmas 6.2-6.13.

## 2. Definitions
### 2.1 The wrapper W(H, s0)
Let H = (V, V_E, V_O, E, pr) be any parity game (TARGET.md §1: every vertex has a successor), V = {0, …, n − 1} with its indices, m_E
(m_O) the number of edges leaving Even (Odd) vertices, n_O := |V_O|, and s0 a positional Even strategy of H. W := W(H, s0) consists of:
- the vertices of H with their owners and indices, and Ω(v) := pr(v) + 6;
- for every edge (v, w), v ∈ V_E: a pad m_(v,w) (Ω 2 if w = s0(v), else 0), an Odd GATE g_(v,w) (Ω 1), pads pe_(v,w) (Ω 1) and
  pβ_(v,w) (Ω 0), with the edges v → m → g, g → pe → c_W, g → pβ → b_(v,w);
- for every edge (o, w), o ∈ V_O: pads x1, x2, x3 (Ω 0) with the edges o → x1 → x2 → x3 → b_(o,w);
- for every edge (a, w) of H: a VALVE b_(a,w) (Even, Ω 0) and pads y_(a,w) (Ω 2), pb_(a,w) (Ω 1), with the edges b → y → w, b → pb → K0;
- for every o ∈ V_O: a pad pe_o (Ω 1) with the edges o → pe_o → c_W;
- c_W (Even, a self-loop, Ω top := the least even number ≥ max_(v ∈ V) Ω(v) + 2); the CORE: K0 (Even, top + 2) → {K1, pA}, pA → K3,
  K1 (Even, 5) → {q, s}, s → K1, q → K0, K2 (Odd, 3) → {r, K2}, r → K1, K3 (Even, top + 3) → {K1, K2}; pA, s, r have Ω 0, q has Ω 1.
- Every pad is an Even vertex with exactly one successor. No other edges. (H's edges are a set; v's successors are its pads.)
- VERTEX ORDER (indices of the new vertices; REFEREE 33's note W-2): after V, in this order: c_W, K0, K1, K2, K3, pA, s, q, r; then for
  v = 0, 1, …, n − 1 and, for each v, its successors w in the order of H's successor list as given: if v ∈ V_E the seven vertices pb,
  y, b, pβ, pe, g, m of the edge (v, w), in this order; if v ∈ V_O the six vertices pb, y, b, x3, x2, x1 of the edge (v, w), and after
  v's last edge the pad pe_v. (This is wrap104.py's order, the order of every frozen instance; L-COMP 20 rebuilt the 11 frozen W files
  byte-identically in it, claude/l-comp aa863db5.) No statement of §4 or §6 depends on this order; N5's COUNTS do (§5 Remark 3, §9).
- Count: n vertices of H; 7 per Even edge (m, g, pe, pβ, b, y, pb); 6 per Odd edge (x1, x2, x3, b, y, pb); 1 per Odd vertex (pe_o); 9
  (c_W, K0, K1, K2, K3, pA, s, q, r): |W| = n + 7·m_E + 6·m_O + n_O + 9, and W has O(n + m_E + m_O) edges and priorities ≤ top + 3 =
  O(max pr + 1): polynomial in |H| at bit cost (TARGET.md §3). Every vertex has a successor, so W is a parity game.
- Paths. An edge (a, w) of H becomes a path of exactly 6 edges from a to w through 5 new vertices of Ω ≤ 2: a → m → g → pβ → b → y → w
  (a ∈ V_E) or a → x1 → x2 → x3 → b → y → w (a ∈ V_O).
### 2.2 Rank facts (R_W) (from [SPEC] S1's rank by (Ω, index))
Pads, gates, valves (Ω ≤ 2) < K2 (3) < K1 (5) < every vertex of H (Ω ≥ 6) < c_W (top) < K0 (top + 2) < K3 (top + 3). The vertices of
H are ordered among themselves as in H (pr ↦ pr + 6 keeps the order, the parity and the index ties). K0 is the most relevant EVEN vertex
of W, so a value with cycle node K0 has the largest reward of all values; c_W is the most relevant even vertex outside the core, so a
value with node c_W has a larger reward than every value whose node is a vertex of H, K1 or K2; K1's reward −p'(K1) is below K2's.
Notation: a value is (c, P, ℓ); ▷ = strictly better for Even, ⊵ = better or equal. v ⊕ (c, P, ℓ) := (c, P ∪ ({v} if v is more relevant
than c), ℓ + 1): the value of v when v steps to a vertex of value (c, P, ℓ) and v is not on that play's cycle. If v is less relevant
than c, v ⊕ · is strictly order-preserving and injective (it adds 1 to the length on both sides); if two values have different cycle
nodes, v ⊕ · keeps their order (rewards decide).
### 2.3 Standard states; the H-part; Howard's rule on H
- The STANDARD STATE of a positional Even strategy s of H is the state (σ, τ0) of W with σ(v) = m_(v,s(v)) at v ∈ V_E, σ(b) = y at every
  valve, σ(K0) = pA, σ(K1) = s, σ(K3) = K2 (the K-config κ0 := (pA, s, K2)); τ0(g) = pe at every gate, τ0(o) = pe_o at every o ∈ V_O,
  τ0(K2) = K2. Its H-PART is s. K-configs (σ(K0), σ(K1), σ(K3)): κ0 = (pA, s, K2), κ1 = (K1, s, K2), κ2 = (K1, q, K2), κ3 = (K1, q, K1).
- Ω^H_s(v) := SPEC S1's value of v in H under s and Odd's pointwise-optimal counterstrategy ([1E-N3] on H). A HOWARD STEP of H at s moves
  every v ∈ V_E to a ⊴-best successor (by Ω^H_s) and keeps s(v) when s(v) is one; ties among best successors by a rule R. A HOWARD RUN
  from s0 is s0, s1, … with s_(t+1) a Howard step at s_t; T is the first t at which no v ∈ V_E has a successor strictly better than s_t(v).
  WRAP's run uses R = «the Ξσ-best pad by N5′-xi's rule: SPEC's choice, then the larger index» (§4.7).
### 2.4 Fact (H) (PROVED, from [SPEC] S4a, [N5XI], [1E-N3] P2)
Let v be an Even vertex of W with |A(v)| ≥ 2 that is not its own cycle node in the arena optimum W*. If exactly one w0 ∈ A(v) has
v ⊕ W*(w0) = W*(v), then σ_new(v) = w0 in N5 and in N5′-xi. Proof. N5: σ_new is a pointwise optimum of the arena (P2), so v's arena value
under σ_new is W*(v) = v ⊕ W*(σ_new(v)) (v is not its own cycle node, and the arena values under σ_new are W*), so σ_new(v) ∈ TIE(v) =
{w0}. N5′-xi: σ_new(v) ∈ TIE(v) = {w0} by [N5XI]. Where |A(v)| = 1 the choice is forced in both. ∎

## 3. Lemma WRAP (the statement)
**Lemma WRAP (PROVED, lane; premises [SPEC], [N5XI], [1E-N3], [DUAL], [R15c], [R15d]).** For every parity game H and every positional
Even strategy s0 of H:
- (i) S3's pair on W(H, s0) is the standard state of s0.
- (ii) At every state of the N5′-xi run and of the N5 run from S3: τ = τ0 and Iτ = ∅.
- (iii) The N5′-xi run from S3 visits only standard states until its first fallback; their H-parts form a Howard run of H from s0 with
  the tie rule of §2.3; the first fallback is at iteration T + 1, T the length of that Howard run.
- (iv) The N5′-xi run has exactly one fallback and exactly T + 3 iterations.
- (v) The N5 run from S3 has exactly one fallback, at an iteration F ≥ 1, and exactly F + 2 iterations; before F its states are standard
  and each v ∈ V_E picks, by SPEC's rule, inside A(v) = {its current pad} ∪ {the pads of its successors strictly ⊴_H-better than s(v)}.

## 4. Proof, on W
### 4.1 Lemma PAD-W (W1). Every cycle of W is c_W's loop, lies in the core, or contains a vertex of H; every cycle other than c_W's loop contains a vertex of Ω ≥ 3. So for every pair of positional strategies, no pad, gate or valve is a cycle node, and none is in a P-set.
Proof. The core {K0, K1, K2, K3, pA, s, q, r} has no edge leaving it, and c_W's only successor is c_W. Let C be a cycle that contains
neither c_W nor a core vertex nor a vertex of H. Its vertices are new vertices outside the core; along every edge among them the vertex
type strictly advances in the order m < g < pβ < x1 < x2 < x3 < b < y (pe, pe_o and pb lead to c_W or K0 only, y leads into V): no
cycle. So C contains c_W (then C is c_W's loop), a core vertex (then C lies in the core, which is closed), or a vertex of H (Ω ≥ 6).
The core's simple cycles are K1 → s → K1, K1 → q → K0 → K1, K0 → pA → K3 → K1 → q → K0, K0 → pA → K3 → K2 → r → K1 → q → K0
and K2's loop: each contains K0, K1 or K3, or is K2's loop (Ω 3). A cycle node is the most relevant vertex of its
cycle, so it has Ω ≥ 3; a P-set holds only vertices more relevant than its cycle node; pads, gates and valves have Ω ≤ 2. ∎
### 4.2 Lemma S3-W (W2) = WRAP (i)
By [SPEC] S3 / FIX 1 at every vertex with two or more successors (all others are forced). v ∈ V_E: its successors are its pads
m_(v,w), all of even Ω; the highest even one is the unique Ω-2 pad, m_(v,s0(v)). A valve: y (Ω 2, even) and pb (Ω 1, odd): y. K0: K1
(Ω 5, odd) and pA (Ω 0, even): pA. K1: q (Ω 1, odd) and s (Ω 0, even): s. K3: K1 (Ω 5) and K2 (Ω 3), both odd: the lowest odd, K2.
A gate (Odd): pe (Ω 1, odd) and pβ (Ω 0, even): the highest odd, pe. o ∈ V_O (Odd): its pads x1 (Ω 0, even) and pe_o (Ω 1, odd): the
highest odd, pe_o (the only odd one). K2 (Odd): r (Ω 0, even) and K2 (Ω 3, odd): K2. This is the standard state of s0. ∎
### 4.3 Lemma K3-W (the core) with Lemma K2-r-W. Let σ be any Even strategy of W with K-config κ0, and τ = τ0.
- (K2-r-W) σ̄(K2) = r in every pointwise optimum. Odd's two options at K2: the loop (cycle node K2) and r → K1 → s → K1 … (cycle node K1,
  as σ(K1) = s). Both odd; K1 is more relevant, so −p'(K1) < −p'(K2): the value via r is strictly smaller, and σ̄ minimises at every
  vertex (P1). The core is closed, so this holds whatever σ is outside the core.
- (a) Values in the core (P by (R_W): K0, K3 are the only core vertices above K1): K1 ↦ (K1, ∅, 0); s ↦ (K1, ∅, 1); r ↦ (K1, ∅, 1);
  K2 ↦ (K1, ∅, 2); K3 ↦ (K1, {K3}, 3); pA ↦ (K1, {K3}, 4); K0 ↦ (K1, {K0, K3}, 5); q ↦ (K1, {K0, K3}, 6). (Plays: K1 → s → K1; K3 → K2
  → r → K1; K0 → pA → K3 → K2 → r → K1; q → K0 → ….)
- (b) Iσ ∩ (edges out of K0, K1, K3) = {(K0, K1)}. K0: K1 (K1, ∅, 0) against σ(K0) = pA (K1, {K3}, 4): same node, the difference {K3}
  is odd and lies in pA's set, so K1 is strictly better: improving. K1: q (K1, {K0, K3}, 6) against s (K1, ∅, 1): the top of the
  difference is K3, odd, in q's set: q worse: not improving. K3: K1 (K1, ∅, 0) against K2 (K1, ∅, 2): same node and set; the node K1 is
  odd, so the longer is better for Even: K2 better: not improving.
- (c) Iτ ∩ {edges out of K2} = ∅ (τ(K2) = K2). From r, Even may play r → K1 → q → K0 → K1 …, a cycle whose most relevant vertex is K0
  (even, the largest reward of all); by [DUAL] τ̄ maximises Γ's (here W's) order at every vertex, so the τ-value of r has reward ≥ p'(K0)
  > 0 > −p'(K2), the reward of the loop's value: r is worse for Odd; Iτ(K2) = ∅ by [DUAL]'s form of Iτ. (Uses only the core.)
- (d) In S4a's arena: by (b), A(K0) = {pA, K1}, A(K1) = {s}, A(K3) = {K2}; Odd's K2 follows τ0: K2 → K2. The arena plays from K0 are
  K0 → K1 → s → K1 … (node K1) and K0 → pA → K3 → K2 → K2 … (node K2); −p'(K2) > −p'(K1), so pA is strictly better. K0 lies on no arena
  cycle: the only edge into K0 inside the core is q → K0, and q ∉ A(K1); the core is closed, so no arena play leaves it and returns.
  Hence W*(K0) = K0 ⊕ W*(pA), K0 ⊕ W*(K1) ≠ W*(K0) (different nodes), and by (H) σ_new(K0) = pA in N5 and N5′-xi; K1, K3 are forced.
  Every arena play from K0 ends in an odd cycle (node K1 or K2). ∎
### 4.4 Lemma ODD-W (W4). Let (σ, τ0) be the standard state of s. Then (a) σ̄(g) = pβ at every gate and σ̄(o) ≠ pe_o at every o ∈ V_O; (b) for v ∈ V, Ξσ(v) = (c, P, 6ℓ) where (c, P, ℓ) = Ω^H_s(v); (c) Ξσ(m_(v,w)) = (c, P, 6ℓ + 5) where (c, P, ℓ) = Ω^H_s(w); (d) for v ∈ V_E: (v, m_(v,w)) ∈ Iσ iff Ω^H_s(w) ▷ Ω^H_s(s(v)), and Ξσ orders the pads of v as Ω^H_s orders its successors (equal H-values give equal pad values).
Proof. Call an Odd strategy of W pe-FREE if it plays pβ at every gate and some x1_(o,w) at every o ∈ V_O (it exists: every o has a
successor in H). (Correction C-1 of box 104, REFEREE note W-1:) under σ, a pe-free play that starts at a vertex of H, a gate, a valve,
or a pad m, pβ, x_i or y runs along the 6-edge paths from vertex of H to vertex of H forever: a vertex of H goes to its pad m (Even, σ)
or to x1 (Odd); m → g → pβ → b; x1 → x2 → x3 → b; a valve b → y (σ) → w ∈ V; so it never meets pe, pe_o, pb, c_W or the core, and by
PAD-W its cycle node is a vertex of H, of rank below c_W. A play that takes a pe at a gate or a pe_o ends in c_W's loop.
- (a) Let u be a gate or a vertex of V_O. If σ̄(u) were pe (pe_u), Ξσ(u) would have the node c_W; a pe-free Odd strategy gives u a value
  whose node is a vertex of H, of strictly smaller reward than c_W's ((R_W)); so Ξσ(u) would not be the minimum at u, against P1.
- (b) The pe-free Odd strategies, restricted to V_O, correspond one to one to the positional Odd strategies ρ of H (o ↦ w iff the
  strategy plays x1_(o,w)). Under σ and a pe-free strategy with ρ, the play from v ∈ V is the (s, ρ)-play of H with every edge replaced
  by its 6-edge path: if H's play from v reaches its cycle node c after ℓ steps, W's play reaches c after 6ℓ steps; its cycle consists of
  H's cycle vertices and inner path vertices, so its most relevant vertex is c (inner vertices have Ω ≤ 2); its P-set is H's (inner
  vertices are less relevant than c). So its value is (c, P, 6ℓ) for the H-value (c, P, ℓ). The map (c, P, ℓ) ↦ (c, P, 6ℓ) is strictly
  order-preserving and injective for [SPEC] S1's order: rewards and P-comparisons are H's (ranks and parities of V are H's), and
  lengths are multiplied by 6. By (a) σ̄ is pe-free; it minimises at every vertex over all Odd strategies (P1), in particular over the
  pe-free ones; so its ρ̄ minimises the H-value at every vertex of H: ρ̄ is a pointwise-optimal counterstrategy of s in H, and Ξσ(v) =
  (c, P, 6ℓ) with (c, P, ℓ) = Ω^H_s(v) (the pointwise minimum is unique as a value).
- (c) Under (σ, σ̄) the play from m_(v,w) is m → g → pβ (a) → b → y (σ) → w and then w's play: five more steps, no new P-element (all five
  have Ω ≤ 2 < Ω(c)): (c, P, 6ℓ + 5).
- (d) [SPEC] S2 compares Ξσ at the successors of v, which are its pads; σ(v) = m_(v,s(v)); (c, P, ℓ) ↦ (c, P, 6ℓ + 5) is strictly
  order-preserving and injective. ∎
### 4.5 Lemma TAU-W (W5) = WRAP (ii) = Lemma E0-W. At every state of the N5′-xi run and of the N5 run from S3, τ = τ0 and Iτ = ∅.
Proof. Iτ is computed on G^d from τ alone ([SPEC] S1, «Iτ computed there»): it is the same at every state with τ = τ0. Under τ0 every
gate plays pe and every o ∈ V_O plays pe_o, both of which lead to c_W's loop, so their τ-values have node c_W whatever Even does. The
alternative of a gate g is pβ_g → b; of o ∈ V_O, a pad x1 → x2 → x3 → b. From the valve b Even may play b → pb → K0 → K1 → q → K0 …, a
cycle with node K0; by [DUAL] τ̄ maximises at every vertex, so these alternatives have τ-values of reward ≥ p'(K0) > p'(c_W): worse for
Odd, not in Iτ ([DUAL]'s form Iτ(v) = {w ≠ τ(v) : Ξτ(w) ◁ Ξτ(τ(v))}). K2: K3-W (c) (which uses the core only). The Odd vertices of W are
the gates, V_O and K2; so Iτ = ∅ whenever τ = τ0. By S4-S5: S4b changes τ only if Iτ ≠ ∅; S4c changes τ only if Iσ = ∅ and then along
Iτ (FIX 3); if Iσ = Iτ = ∅ the run stops (S5). τ = τ0 at S3 (S3-W), so by induction τ = τ0 and Iτ = ∅ at every state, for N5 and
N5′-xi (S4b, S4c are the same in both). ∎
### 4.6 Lemma ESC-W (W6). In the standard state of any s: Iσ ∋ (K0, K1) (K3-W (b), with K2-r-W); and in S4a's arena (Even keeps A(·), Odd follows τ0):
- every option of v ∈ V_E is a pad m whose arena play is m → g → pe → c_W (τ0), so W*(m) = (c_W, ∅, 3) for EVERY m ∈ A(v) (m, g, pe are
  less relevant than c_W); W*(v) = (c_W, ∅, 4); v is on no arena cycle and its arena cycle node is c_W ≠ v; TIE(v) = A(v).
- a valve b has A(b) ⊆ {y, pb} with y = σ(b). Via y → w: if w ∈ V_E every option of w is a pad whose arena play goes g → pe → c_W; if
  w ∈ V_O, τ0(w) = pe_w → c_W: node c_W. Via pb → K0: an odd cycle (K3-W (d)). c_W is even, so y is strictly better (REWARD). b is on no
  arena cycle (its arena plays end in c_W's loop or in the core, neither of which contains b). So TIE(b) = {y} when pb ∈ A(b), and by
  (H) σ_new(b) = y; when A(b) = {y} it is forced.
- the core: K3-W (d): σ_new(K0) = pA, K1 and K3 forced. Every other Even vertex (the pads, c_W) has one successor.
So σ_new = σ off V_E, in N5 and in N5′-xi. ∎
### 4.7 Lemma REACH-W (W7) = WRAP (iii) and the first half of (v)
Let s0, s1, … be the Howard run of H from s0 with the tie rule of §2.3, and T its length. T exists: each Howard step at t < T switches
every moving Even vertex to one strictly better successor, so s_(t+1) = Switch_I(s_t) for a non-empty unambiguous set I of improvements
of s_t in H; by [R15c] no strategy of H repeats along the run, and H has finitely many strategies.
Claim: for j = 0, …, T, the N5′-xi state j is the standard state of s_j, and iterations 1, …, T are not fallbacks. j = 0: S3-W. Let
j < T and state j standard for s_j. τ_new = τ (TAU-W). Iσ ∋ (K0, K1) (ESC-W), so S4a applies; off V_E, σ_new = σ (ESC-W). At v ∈ V_E
with |A(v)| ≥ 2: v is not its own arena cycle node and TIE(v) = A(v) (ESC-W), so N5′-xi takes the Ξσ-best element of A(v) (ties: SPEC's
choice, then the larger index). A(v) = {m_(v,s_j(v))} ∪ {pads of the successors strictly ⊴_H-better than s_j(v)} (ODD-W (d)), so A(v)
contains the pads of all ⊴_H-best successors of v, and by ODD-W (d) its Ξσ-best elements are exactly those pads: v moves to the pad of
a ⊴_H-best successor. Where A(v) = {σ(v)}, s_j(v) is itself a ⊴_H-best successor and v stays. So σ_new is the standard state of a
Howard step s_(j+1) of s_j under the tie rule of §2.3. As j < T some v moves, σ_new ≠ σ, S4c does not apply, and state j + 1 is standard.
At j = T no v ∈ V_E has a strictly better successor, so A(v) = {σ(v)} for all v ∈ V_E (ODD-W (d)); σ_new = σ (ESC-W) and τ_new = τ
(TAU-W), so iteration T + 1 is a fallback, with Iσ ∋ (K0, K1) ≠ ∅ (an Even fallback). This is (iii).
For N5 the same induction holds with SPEC's S4a pick: P2 makes σ_new a pointwise optimum of the arena, so σ_new(v) ∈ TIE(v) = A(v) at
v ∈ V_E (ESC-W) and σ_new = σ off V_E: as long as σ_new ≠ σ the new state is the standard state of the strategy s′ of H with
m_(v,s′(v)) = σ_new(v), and s′(v) ∈ {s(v)} ∪ {successors strictly ⊴_H-better than s(v)}; the first iteration with σ_new = σ is the first
fallback F (τ_new = τ by TAU-W). This is the first half of (v). ∎
### 4.8 The endgame on W: Lemmas E1-W to E4-W and Theorem ENDGAME-W
In this section σ is arbitrary at V_E and at the valves; only the K-config and τ = τ0 (TAU-W) are fixed.
- **E1-W.** In every state with K-config κ0: (a) Iσ ∩ (edges out of K0, K1, K3) = {(K0, K1)}; (b) every S4a σ_new (N5 or N5′-xi) has
  K-config κ0. Proof: K3-W (a)-(d), whose proofs use the core only (the core is closed). Corollary: the K-config changes only at a
  fallback; in every state before the first fallback it is κ0 and Iσ ≠ ∅.
- **E2-W.** If iteration F is the first fallback, its input state has K-config κ0 and τ0, it is an Even fallback, and its result has
  K-config κ1 and τ0. Proof: E1-W's corollary and TAU-W; Iσ ≠ ∅ (E1-W (a)), so S4c switches every Even vertex with an improving edge to
  its best improving edge and keeps τ (FIX 3); in the core only K0 has one, (K0, K1). (Vertices of V_E and valves may switch too.) ∎
- **E3-W.** From every state with K-config κ1 and τ0, the next iteration is an S4a iteration, not a fallback, whose result has K-config κ2.
  Proof. Odd at K2: r → K1 → s → K1 … (node K1) against the loop (node K2): σ̄(K2) = r (P1, as in K2-r-W). Values: K1 (K1, ∅, 0); s
  (K1, ∅, 1); K0 (K1, {K0}, 1) (K0 → K1); q (K1, {K0}, 2); r (K1, ∅, 1); K2 (K1, ∅, 2); K3 (K1, {K3}, 3); pA (K1, {K3}, 4). Iσ in the core:
  K1: q (K1, {K0}, 2) against s (K1, ∅, 1): the difference {K0} is even and in q's set: (K1, q) ∈ Iσ. K0: pA (K1, {K3}, 4) against K1
  (K1, ∅, 0): K3 odd in pA's set: not improving. K3: K1 (K1, ∅, 0) against K2 (K1, ∅, 2), node odd: not improving. So Iσ ≠ ∅: S4a. Arena:
  A(K0) = {K1}, A(K1) = {s, q}, A(K3) = {K2}, K2 → K2. Via q: K1 → q → K0 → K1, a cycle whose most relevant vertex is K0: W*(K1) =
  (K0, ∅, 2) and K1 is not its own arena cycle node; W*(q) = (K0, ∅, 1), so K1 ⊕ W*(q) = W*(K1); via s: W*(s) = (K0, ∅, 3) (s → K1 → q →
  K0), K1 ⊕ W*(s) = (K0, ∅, 4) ≠ W*(K1). By (H) σ_new(K1) = q; K0, K3 are forced. σ_new ≠ σ, so S4c does not apply: K-config κ2. ∎
- **E4-W (a).** From every state with K-config κ2 and τ0, the next iteration is an S4a iteration, not a fallback, whose result σ* has
  K-config κ3 and σ*(b) = pb at every valve.
  Proof. Odd at K2: r → K1 → q → K0 → K1 … (node K0, the largest reward) against the loop (node K2): σ̄(K2) = K2. Core values: K0 (K0, ∅,
  0); q (K0, ∅, 1); K1 (K0, ∅, 2); s (K0, ∅, 3); K2 (K2, ∅, 0); K3 (K2, {K3}, 1); pA (K2, {K3}, 2); pb (K0, ∅, 1) at every valve's pb. Iσ in
  the core: K3: K1 (node K0) against K2 (node K2): REWARD, (K3, K1) ∈ Iσ. K0: pA (node K2) against K1 (node K0): not. K1: s (K0, ∅, 3)
  against q (K0, ∅, 1), node K0 even, the shorter is better: not. Valves: let b = b_(a,w). By P1, Ξσ(w) ⊴ the value of w's play under σ
  and the Odd strategy «pe at every gate, pe_o at every o ∈ V_O, K2 → K2»; that play goes w → σ(w) (a pad m) → g → pe → c_W if w ∈ V_E,
  and w → pe_w → c_W if w ∈ V_O: node c_W. So the node of Ξσ(w) has reward ≤ p'(c_W) < p'(K0), and Ξσ(y) = y ⊕ Ξσ(w) has the same node
  (y has Ω 2, PAD-W). Hence Ξσ(y) ◁ Ξσ(pb): (b, pb) ∈ Iσ where σ(b) = y, and (b, y) ∉ Iσ where σ(b) = pb. Arena (Odd: τ0): A(K0) = {K1},
  A(K1) = {q}: every arena play from K0 is K0 → K1 → q → K0 …, node K0. A valve has A(b) = {y, pb} or {pb}: via pb node K0; via y → w the
  arena play ends in c_W's loop as in ESC-W (w ∈ V_E: a pad, its gate, pe; w ∈ V_O: pe_w), node c_W; b is on no arena cycle; so TIE(b) =
  {pb} and (H) gives σ_new(b) = pb (forced when A(b) = {pb}). K3: A(K3) = {K2, K1}; via K2: the loop K2 (τ0), node K2; via K1: node K0;
  K3 is on no arena cycle (its only in-edge is from pA, whose only in-edge is from K0, and A(K0) = {K1}); (H): σ_new(K3) = K1. σ_new(K3)
  ≠ σ(K3), so no fallback. K0, K1 forced: K-config κ3. ∎
- **E4-W (b).** At σ* (K-config κ3, σ*(b) = pb at every valve, any σ* at V_E): Iσ* = ∅; with TAU-W the run stops (S5).
  Proof. Odd's reply: from a gate g, pe gives (c_W, ∅, 2); pβ gives pβ → b → pb (σ*) → K0 → K1 → q → K0 …, node K0, a larger reward. From
  o ∈ V_O, pe_o gives (c_W, ∅, 2) (o is less relevant than c_W); every x1 gives x1 → x2 → x3 → b → pb → K0 …, node K0. At K2 the loop
  (node K2) is below r (node K0). So by P1, σ̄* plays pe at every gate, pe_o at every o ∈ V_O and the loop at K2. Even vertices: v ∈ V_E:
  every option is a pad m → g with Ξσ*(m) = (c_W, ∅, 3): all equal, none strictly better: no improving edge. Valve b: Ξσ*(pb) = (K0, ∅, 1);
  Ξσ*(y) = y ⊕ Ξσ*(w) with node c_W (w ∈ V_E: its pad, gate, pe; w ∈ V_O: pe_w): (b, y) ∉ Iσ*. Core: K0: pA → K3 → K1 → q → K0: (K0, {K3},
  4) against K1 (K0, ∅, 2): K3 odd: not. K1: s (K0, ∅, 3) against q (K0, ∅, 1): not. K3: K2 (K2, ∅, 0) against K1 (K0, ∅, 2): not. The
  pads and c_W have one successor. So Iσ* = ∅; Iτ = ∅ by TAU-W; the run stops. ∎
- **Theorem ENDGAME-W (PROVED).** The N5′-xi run and the N5 run from S3 on W(H, s0) each have exactly one fallback, at an iteration F ≥ 1,
  and exactly F + 2 iterations; iterations 1, …, F − 1 are S4a iterations with K-config κ0 and τ0.
  Proof. A first fallback F exists: for N5′-xi at T + 1 (REACH-W); for N5 because the run terminates ([R15d]) and cannot stop while the
  K-config is κ0 (Iσ ∋ (K0, K1), E1-W), which changes only at a fallback (E1-W's corollary). E2-W: after F, κ1. E3-W: iteration F + 1 is
  not a fallback and gives κ2. E4-W (a): iteration F + 2 is not a fallback and gives σ*; E4-W (b): the run stops. ∎
- Proof of WRAP (iv) and the second half of (v): ENDGAME-W with F = T + 1 for N5′-xi (REACH-W): T + 3 iterations. ∎

## 5. Remarks
- Remark 1 (READING). WRAP uses no property of H: any owners, priorities (equal ones included), degrees, self-loops.
- Remark 2 (READING; DATA rem2 0 at REFEREE 33). Even wins W(H, s0) from every vertex but K2: the valves reach the core, which Even wins
  with K0 → K1 → q → K0. The wrapper tests the run, not the winner.
- **Remark 3 (PROVED under [RULE]; REFEREE 33: «correct given [RULE]», counted rem3 0).** For N5, by ESC-W every option m of v ∈ V_E has
  the 3-step arena play m → g → pe → c_W at every standard state, so its root-first key is the index sequence of (pe, g, m), the same at
  every state; by [RULE] SPEC picks the key-least option of TIE(v) = A(v), so before its first fallback each v ∈ V_E only moves to a
  pad of strictly smaller key: at most deg(v) − 1 moves per v, at most m_E − |V_E| in all; every non-fallback iteration before F moves
  some v ∈ V_E (σ_new = σ off V_E). So F ≤ m_E − |V_E| + 1 and N5 makes at most m_E − |V_E| + 3 iterations on W(H, s0). The count
  depends on the index order of §2.1 (§9: 6 in this order on W(G^L_n, ι), 3 and 4 in two other orders); the bound does not.

## 6. Claim NT and Corollary NT-RUN (Claim NT and its proof originate with REFEREE successor 33, R-WRAP-preread §3.2; L41; the written rendering below is L-SI 53's)
- REFEREE 33's text, quoted (it signs nothing; the lane writes the proof below; REFEREE-2 checks it independently):
  - [Q] «(T-2) **Claim NT (no tie on a 1-sink game; mine).** Let G with ι be a 1-sink game in [F11] §5's sense, with sink x, and σ a
    player-0 strategy with Ξ_ι ⊴ Ξ_σ. Then Ξ_σ(u) ≠ Ξ_σ(u′) for all nodes u ≠ u′. Proof. By Sink Seeking (p. 8) every Ξ_σ(u) has cycle
    component x; every other node is more relevant than x (Sink Existence), so the cycle is x's loop and the path component of Ξ_σ(u)
    is the set of ALL nodes of the play from u before x, u itself included (the paper's own remark, p. 8: «the path-length component
    equals the cardinality of the path component»). Ξ_σ(x) = (x, ∅, 0) differs from every other value. If u, u′ ≠ x had equal values,
    u′ would lie on u's play and u on u′'s play; plays are positional, so u's play would return to u before reaching x: a cycle
    without x, against Sink Seeking. ∎»
  - [Q] «(T-3) G_n with ι_(G_n) is a 1-sink game: [F11] Lemma 6.7 with Lemma 5.1 (p. 17, p. 8). I re-read both proofs. 6.7 (1): under
    τ(e_i) = h_i the edges of Table 4 allow no cycle but x's loop (s → f_j or x; r → g_j or x; f, e, h, k, g only move to k, x or a g
    of higher index; t, a, c, d only reach s, r, e or lower t's); 6.7 (2) and 5.1 as written. Neither uses the six priorities that
    differ between Table 4 and Figure 4.»
  - [Q] «(T-4) Every strategy σ of an improvement run from ι has Ξ_ι ⊴ Ξ_σ ([F11] Theorem 3.2; in the fleet, landed R15 (a)). By Claim
    NT no two successors of a node tie at any state of the run, so the property of §3.1 determines I^loc(σ) uniquely there: every
    policy with the property, WRAP's included, produces the same run from ι_(G_n), which is therefore the run Theorem 6.14 speaks of.
    No reading of the proofs of Lemmas 6.2-6.13 is needed (Addendum A's route), and the lane's tie rule is never invoked on G_n.»
  - [Q] «Status. Claim NT and (T-4) are referee-originated: under L41 they count only when the lane has written them and the other
    referee has checked them independently. I would sign them.»
- **Claim NT (REFEREE 33's claim and proof, L41; this rendering of the proof by L-SI successor 53; to be checked by REFEREE-2).** Let G be a parity game with injective Ω and initial strategy ι such
  that (G, ι) is a 1-sink game with sink x ([F11] §5). For every player-0 strategy σ with Ξ_ι ⊴ Ξσ and all nodes u ≠ u′: Ξσ(u) ≠
  Ξσ(u′). Hence at such a σ every player-0 node has exactly one ⪯σ-best successor.
  Proof. Fix τ := τσ. For every node u, Ξσ(u) is the valuation of the (σ, τ)-play from u, a positional play u = v_1, …, v_k followed by
  a cycle, the v_i pairwise distinct and not on the cycle. By Sink Seeking the cycle component (the most relevant node of the cycle) is
  x; every node other than x is more relevant than x (Sink Existence), so the cycle is x's loop alone and the path component of Ξσ(u)
  is {v_1, …, v_k}, every node before x ([F11] p. 8: «the path-length component equals the cardinality of the path component»). So
  Ξσ(x) = (x, ∅, 0), and for u ≠ x the path component contains u: Ξσ(x) ≠ Ξσ(u). Let u ≠ u′, both ≠ x, with Ξσ(u) = Ξσ(u′). Then u′ is
  in the path component of Ξσ(u): u′ = v_j for some j ≥ 2. Since σ and τ are positional, the play from u′ is the suffix v_j, …, v_k, x,
  x, … of u's play, which does not contain v_1 = u (the v_i are pairwise distinct and u ≠ x). So u is not in the path component of
  Ξσ(u′) = Ξσ(u), which contains u: a contradiction. The order ⪯ on node valuations is total ([F11] p. 4-5), so the pairwise distinct
  valuations of a node's successors have exactly one maximum. ∎
- **Corollary NT-RUN (CONDITIONAL on Lemma WRAP being signed; premises [F11] Lemma 5.1, Lemma 6.7, [R15a], Claim NT).** For n ≥ 1 let
  G^L_n be [F11]'s G_n with Figure 4's injective priorities (READING F-1, §7) and W^L_n := W(G^L_n, ι). The H-parts s_0 = ι, …, s_T of the
  N5′-xi run on W^L_n (WRAP (iii)) are the run of the strategy improvement algorithm on G^L_n from ι with ANY policy that has [F11] §4's
  defining property of I^loc; so T is the number of improvement steps of Theorem 6.14.
  Proof. (G^L_n, ι) is a 1-sink game: [F11] Lemma 6.7 with Lemma 5.1; their proofs use the graph, the owners and Ω(x) = 1, not the six
  priority formulas in which Table 4 and Figure 4 differ (REFEREE 33 (T-3) re-read them). Each step s_t → s_(t+1) moves every moving Even
  vertex to a strictly better successor (REACH-W), so s_(t+1) = Switch_I(s_t) for a non-empty unambiguous set of improvements, and [R15a]
  gives Ξ_(s_t) ⊴ Ξ_(s_(t+1)) pointwise; by transitivity Ξ_ι ⊴ Ξ_(s_t) for every t, the hypothesis of Sink Seeking and of Claim NT.
  [SPEC] S1's values and order on G^L_n are [F11] §3's node valuations and order (injective Ω, so SPEC's rank by (Ω, index) is Ω's
  order; the start vertex counts in the path set and the length is the number of steps to the cycle node in both; REFEREE 33 §3.1). By
  Claim NT every Even node v has a unique best successor b_t(v) at s_t; a Howard step sets s_(t+1)(v) = b_t(v) at every v (a node with no
  strictly better successor already sits on its unique best one), and b_t(v) is the only value that a policy with the property «w ⪯σ
  I(σ)(v) for every w ∈ vE» can take at v. So s_(t+1) = I(s_t) for every such policy I, and the run stops at the first non-improvable
  s_T, as the algorithm does. N5′-xi's tie rule is never invoked on these runs. ∎

## 7. [F11] Theorem 6.14 as cited, and Statement XI-EXP (CONDITIONAL)
- What «as published» carries (REFEREE 33, quoted):
  - [Q] «F-1 (the game; READING, stated by the box, confirmed here). Table 4 (p. 15) prints d_i 4i + 1, e_i 4i + 2, g_i 4i + 4, k_i 8n
    + 4i + 7, f_i 8n + 4i + 9, h_i 8n + 4i + 10. Then Ω(g_n) = Ω(a_1) = 4n + 4, against p. 3's injectivity, and the highest priority
    is 12n + 10, against Fact 6.1's «12·n + 8 as highest priority» on the same page. Figure 4 (p. 16, G_3) shows d 3, 7, 11; e 4, 8,
    12; g 6, 10, 14; k 33, 37, 41; f 35, 39, 43; h 36, 40, 44, i.e. each of the six formulas minus 2; Figure 3 / Table 3 (p. 13, «p′_1
    = 3 and p_1 = 33») agree with Figure 4. So the game of Theorem 6.14 is the Figure-4 game on the reading that Table 4 carries a
    misprint; XI-EXP must keep saying so (it does, §5.1 and §6).»
  - [Q] «F-2 (the count). The paper proves its phase lemmas under a stated restriction (p. 17-18): «we will assume that b is different
    from 0_n and that the two highest bits in b are zero and remain zero, i.e. we will only use the first n − 2 bits for counting.
    Note however, that every bit works as intended in the counter.» Lemma 6.13 gives k ≥ 4 steps per increment. So the bound 2^n is
    the theorem «as published»; what the written lemmas give line by line is of the order 4·2^(n−2) minus a constant. XI-EXP's «2^n +
    3» inherits exactly this. For «not polynomial» any 2^Ω(n) suffices. DATA: T = 9·2^n − 10 for n = 1, …, 10 (my run), above 2^n.»
  - [Q] «F-3 (wording). XI-EXP is exact: at least 2^n + 3 iterations on 10.5n² + 152.5n + 48 vertices. In the number of vertices this
    is 2^Ω(√|W|): super-polynomial. §0 item 3's «exponential wherever Howard's is» should read «in n» or «super-polynomial» here.»
- **STATEMENT XI-EXP (CONDITIONAL on Lemma WRAP (§3-§4) and Claim NT (§6) being signed by two referees; with [F11] Theorem 6.14 as a
  cited published theorem, on the READING F-1).** For every n ≥ 1, N5′-xi (RESULTS R118's [N5XI]) from SPEC's default start S3 makes
  exactly T_n + 3 iterations on W^L_n = W(G^L_n, ι), where T_n is the number of improvement steps of the I^loc-policy on G^L_n from ι
  (Corollary NT-RUN, WRAP (iv)), and T_n ≥ 2^n by Theorem 6.14. W^L_n has |W^L_n| = 10.5n² + 152.5n + 48 vertices (n_H = 10n + 4, m_E =
  1.5n² + 14.5n + 4, m_O = 6n + 1, n_O = 5n + 1 in §2.1's count; 211, 395, 600, 826, 1,073, 1,341, 1,630, 1,940 at n = 1, …, 8). **In
  short: N5′-xi needs 2^Ω(n) iterations on a game with O(n²) vertices, so 2^Ω(√|V|)** (|V| the number of vertices of W^L_n):
  super-polynomially many in the number of vertices; «exponential» is in n only (F-3). By F-2, «2^n» is the theorem as stated; the paper's written phase lemmas, proved for
  counter states b ≠ 0_n whose two top bits stay zero, give a count of order 4·2^(n−2) minus a constant line by line; both are 2^Ω(n).
- Consequence, if signed: N5′-xi does not make polynomially many iterations on every parity game; it fails gauntlet step 4 (TARGET.md
  §5) and is not an M4 candidate (Lead rulings 14:36Z (c), 15:19Z, as recorded in box 104 §0). It says nothing against N5 (WRAP (v),
  Remark 3) and nothing about RESULTS R118-R125 or boxes 208 / 209, whose scope is R104's genome games Γ3(G); W^L_n is not a Γ3(G).
- More generally (READING, from WRAP alone): on W(H, s0), N5′-xi's iteration count is Howard's on H (with §2.3's tie rule) plus 3, on a
  game with n + 7·m_E + 6·m_O + n_O + 9 vertices; any family on which Howard's rule is super-polynomial (with every tie rule, or with no
  tie events) transfers.

## 8. DEAD row (draft for the Lead; CLAUDE.md: «Record every dead end with the exact obstruction and the instance that killed it»; L43: «DEAD» only after two signatures, until then CONDITIONAL)
| candidate | claim killed | status | exact obstruction | killing family and frozen instances | source |
| --- | --- | --- | --- | --- | --- |
| N5′-xi (RESULTS R118's [N5XI]: SPEC S1-S5 with box 190's S4a tie rule, the Ξσ-best element of TIE(v)), from SPEC's default start S3 | «N5′-xi makes polynomially many iterations on every parity game» (gauntlet step 4; M4 candidacy) | DEAD-CONDITIONAL: on Lemma WRAP (§3-§4) and Claim NT (§6) being signed by two referees; [F11] Theorem 6.14 cited as published (READING F-1) | W-FLAT: on W(H, s0) Odd's τ never moves (TAU-W) and S4a's arena ties every option of every Even vertex of H (ESC-W: TIE(v) = A(v), every option reaches c_W in 3 steps), so the two-sided step is inert and the Ξσ-best pick inside the tie is Howard's switch-best on H (REACH-W): N5′-xi = Howard on H + 3 iterations (ENDGAME-W). On [F11]'s G_n no tie occurs (Claim NT), so the run is the I^loc run and Theorem 6.14's 2^n steps transfer: 2^Ω(n) iterations on O(n²) vertices, 2^Ω(√\|V\|) | (proof route) W(G_n, ι) = W^L_n: WL_1 … WL_4 (211, 395, 600, 826 vertices; 11, 29, 65, 137 iterations); (DATA routes, same counts T + 3) W(switchallexp_n) = W_2 … W_8 (567 … 2,073 vertices; 33 … 2,489 iterations) and F_n = Γ3*(comp(switchallexp_n), π_n) = F_2 … F_8 (708 … 2,562 vertices; 33, 73, 153, 313, 633, 1,246, 2,489 iterations; its proof route FREE-REACH is NOT in this packet, §11); all in experiments/si/box104/inst at claude/l-si 26704e01, sha1 below | this packet; box 104 §3-§6, Addenda A, C |
- Frozen instance sha1s (experiments/si/box104/inst/SHA1SUMS, checked by checkW.sh): WL_1 b5ee1e18…, WL_2 eb745856…, WL_3 c490812c…,
  WL_4 4114df5e…; W_2 5af12aca…, W_3 5f597572…, W_4 45364079…, W_5 7098bc1b…, W_6 9ee230ec…, W_7 a3ba5233…, W_8 b419a59d…; F_2 438fa60b…,
  F_3 e998a5e1…, F_4 6940487a…, F_5 56c5de50…, F_6 7fbbd92d…, F_7 ca80d502…, F_8 c1d6e9bd…. Generators: wrap104.py `pglmcs fig4 n OUT.pg`
  (W^L_n), `pg n OUT.pg` (W_n); free104.py (F_n).
- Exact counts: T_n + 3 with T_n = 9·2^n − 10 on W^L_n, measured for n ≤ 8 (this lane, L-COMP 20, REFEREE 33) and T_n on G_n alone for
  n ≤ 10 (REFEREE 33); T(switchallexp_n) + 3 on W_n and F_n for n ≤ 8 (this lane, L-COMP 20, L-RED 66 on F_n).
- Not killed by this row: N5 (SPEC) (Remark 3: at most m_E − |V_E| + 3 iterations on every W(H, s0) under [RULE]; 3 to 7 measured
  on these instances); G-N5-TIME stays OPEN.

## 9. DATA (not to sign; each clause with its counter, unit, set and scope; tools experiments/si/box104/, outputs out/)
- Scope of every row: one run from SPEC's S3 on the named game; «iterations» as SPEC S4 counts them. N5 rows are for §2.1's vertex order.
- WRAP's six must-0 counters (wrap104.py; definitions in box 104 §3 DATA): s3fail (games), nonstd (states before the first fallback),
  nohoward ((step, Even vertex of H) pairs: the new successor is not ⊴-best by H's own valuation, computed by si.Engine on H, or a best
  current one was left), fbwrong (games: first fallback ≠ T + 1), endwrong (games: fallbacks ≠ 1 or iterations ≠ T + 3; for N5 ≠ F + 2),
  wrong (games: regions of W ≠ harness Zielonka on W). All 0 on: 3,000 random games H (seed 1043, 2 ≤ n ≤ 12) and 1,000 (seed 1044,
  n ≤ 24) for N5′-xi; 3,000 (seed 1043) for N5 (out/wrap_rand.out); the frozen 300 (rand300.json; out/wrap_json.out, 0 rows differing);
  W(G^L_n, ι) n = 1, …, 6 both priority versions (out/wrap_lmcs_xi.out, wrap_lmcs_spec.out), n = 7, 8 Figure 4 (out/wrap_long.out);
  W(switchallexp_n) n = 2, …, 8 (out/wrap_fried_xi.out, wrap_long.out). Controls: CTRL=1 (best := worst) nohoward 405; CTRL=2 (T shifted)
  fbwrong 100, endwrong 100 (out/wrap_ctrl.out). Two implementations of N5′-xi (n5v.py, n5bxi.py) AGREE+CORRECT on 7 wrapped games
  (out/wrap_xck.out) and on W(G^L_5, ι), W(switchallexp_5) (out/wrap_long.out); that is agreement of two implementations of the same rule.
- Iterations of N5′-xi on W^L_n, n = 1, …, 8: 11, 29, 65, 137, 281, 569, 1,145, 2,297 = T_n + 3, T_n = 8, 26, 62, 134, 278, 566, 1,142,
  2,294 = 9·2^n − 10; tie events on Howard's run of G^L_n: 0 (n ≤ 8). N5 on WL_1, …, WL_4 (this order): 6 iterations, F = 4.
- REFEREE 33's measured note on the vertex order, quoted: [Q] «W-2 (required): the Definition says only «the new vertices are indexed
  after V». Statements (i)-(v) hold for every index order of the new vertices (no step uses one; my PERM = 1 sets, §5). The NUMBERS
  for N5 do depend on it: on W^L_n in my order N5 makes 3 iterations (F = 1) for n = 1, …, 6; on the lane's frozen WL_1, …, WL_4
  (wrap104.py's order; same vertex and edge counts and the same 2-step signature multisets as mine, scratch/wrap_cmp.py) my engine
  gives 6 iterations (F = 4), the lane's column «N5 (spec) on W^L_n: 6». Both agree with (v) and Remark 3 (the key is an index
  sequence). The box should fix the order in the Definition, or say that its N5 columns are for wrap104.py's order. N5′-xi's counts
  are the same in both orders on these games, as (iii) and Claim NT say; on a game H with exact ties (iii)'s Howard run can depend on
  the order through «SPEC's choice, then the larger index».»

## 10. Independent DATA (cited from their own commits; not to sign)
- REFEREE successor 33 (claude/referee e44ce56b; Addendum 1 at 90703a81): [Q] «No FALSE statement found; no instance against any step.
  Own replay (§5): 18 must-be-0 counters (the box's six and twelve of mine), all 0 on every set; every counter has a firing control;
  my engine reproduces the lane's N5′-xi iteration counts on Friedmann's game from my own transcription of the PDF and on the lane's
  frozen instances.» 18 must-be-0 counters, 0 on 523,721 runs
  (random families, every game on 1-3 vertices with priorities 0-2, Friedmann's G_n from its own transcription), nine controls, every
  counter fires under one; the n = 8 row: [Q] «So on my wrapper of my transcription of G_8 the iteration count is above the number of
  vertices, as in the lane's Addendum A.1 row (2,297 iterations on 1,940 vertices), with one fallback and all 18 counters 0.»
- L-COMP successor 20, BOX 44 (claude/l-comp aa863db5, experiments/comp/box44/README.md): own builder, VJ evaluator, Howard run, N5′-xi
  engine and counters written from box 104's text; the 11 frozen W files byte-identical to its build in §2.1's order; nine must-0
  counters 0 on the 300 random games, W_n (n = 2, …, 8) and W(G_n, ι) (n = 1, …, 8); no tie rule acts on any family row; on random
  games every count difference between vertex orders or tie clauses is a tie of Howard's rule. N5 on W(G_n, ι): 4 iterations in its own
  order, 6 in §2.1's order.
- L-RED successor 66, R236 (claude/l-red 0037d948, docs/red/R236-fn.md: F_n CONFIRMED on its own engine n5x236, 33 … 2,489 iterations
  = Howard T + 3) and R237 (1) (claude/l-red 5eca1c32: WRAP's six counters 0 on n5x236 on the 300 random games, W(G_n, ι) n ≤ 4 both
  priority versions, W(switchallexp_2, _3); 14 random rows T ± 1, all ties of H; control nohoward 660). Its independence wording: «up
  to SPEC's cycle-node and S4b tie rules».

## 11. Not in this packet
- FREE-REACH and F_n (box 104 §4-§5: the same fact in R104's genome shape with free carrier priorities; REFEREE 33's PW-4: «the Lead's
  call»): not needed for XI-EXP; available as a second packet if the Lead wants it. L-RED R236 and L-COMP 20 replayed F_n (§10).
- Anything about N5 beyond Remark 3; O1-O3 of box 104 §8; boxes 208 / 209; GUIDE-RULE, GLO-1P (box 104 Addenda A, B).

## 12. Against TARGET.md (READING, not to sign)
- TARGET.md §2 asks for one algorithm and one polynomial for EVERY parity game. XI-EXP, if signed, exhibits a family of parity games
  (in TARGET.md §1's sense, polynomial size at bit cost) on which the candidate N5′-xi takes super-polynomially many iterations: a dead
  end for N5′-xi under CLAUDE.md's rule, recorded with its obstruction and instance family (§8). No algorithm is claimed, no bound is
  claimed, M3 / M4 untouched, G-N5-TIME (about N5) stays OPEN.
- Honest limits: the lower bound rests on a published theorem read on a misprint reading (F-1) and stated in its published form (F-2);
  the lane's tools were written by the lane (two engines are two implementations of one rule); the independent replays are DATA.

## 13. Machine checks and pins
- experiments/si/pwrap/qwrap.py src (out/qwrap.out: 30 items OK, each with its sha1) and doc (every item stands in this file);
  experiments/si/pwrap/checkW.sh (~1 s, no engine): the quotes, the instance sha1s of experiments/si/box104/inst, the DATA lines of §9
  re-read from experiments/si/box104/out/, this file's sha1 against out/P-N5-WRAP.sha1 once frozen. Wired into experiments/si/check.sh.
- Re-run (minutes to hours): `bash experiments/si/box104/runw104.sh` (needs env LNEW, LRED, LLIT archives: box 104 §0's tool line).
- Pins: trunk 7fa6aff4 (premises), claude/referee e44ce56b / 90703a81 (REFEREE 33), claude/l-comp aa863db5, claude/l-red 0037d948 /
  5eca1c32, claude/l-si 26704e01 (box 104 freeze and inst/), [F11] pdf sha256 46c96f44….

