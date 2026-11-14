# Packet P-N5-CHAIN (box 196): N5′-xi from S3 on Γ3(G) is a Howard run until its first fallback for EVERY genome; the counting lemmas hold on that Γ3 run; under [E-LEV] its iteration count is polynomial for bounded U(G)
L-NEW successor 64 (Opus 5.5), D1 / D14 / D18. Lead 2026-11-08 08:27Z: «FREEZE BOX 196 as packet P-N5-CHAIN … statements REACH3-ALL (with
ESC3-ALL, W3-ALL), the Γ3 forms, CHAIN3; premises by landed R-id or by packet …, [E-LEV] a HYPOTHESIS; DEAD RUN-TRANSFER RT_n1». FROZEN at
push. Later text goes to docs/new/P-N5-CHAIN-fixes.md, append-only. Source, history only: docs/new/N5-CHAIN-box196.md (box 196 with
Addendum 1). This packet carries every proof in full, except the game-free abstract core CS(M) of P-N5-ASC §4, cited as a packet.
REFEREE 29's draft notes CH-1..CH-5 (relayed by the Lead 08:35Z) are answered in this text before the freeze. Attacked by L-RED 58: R223-reach (claude/l-red 71133de5, ESC3 / W3 / R118 (k) on Ξ-cyclic genomes: SURVIVES) and R224-chain (claude/l-red
e7937985, every box-196 statement: SURVIVES; controls for five counters, copied here with credit). Credit: the chain map is L-RED 58's
(docs/red/R223-q2.md §4, claude/l-red 77b8946b); the F1 / STRICT re-citation is from R223-reach §3; the ENDGAME-3 conjecture and family
generator are L-RED 56's (via P-N5-END).
Labels: PROVED (L-NEW 64, unrefereed) / DEAD / DATA / READING (not to sign).
This packet is NOT a TARGET.md claim, NOT M3 and NOT M4. It does not decide G-N5-TIME.

## Scope (explicit)
- Games: Γ3(G) of RESULTS R117 for a genome G of RESULTS R104 (every genome, Ξ-cycles and Ξ self-loops allowed). Algorithm: N5′-xi (RESULTS
  R118's [N5XI]) from SPEC's default start S3. Counted: iterations (SPEC S4). Model: HOW3(G) (§2), the Howard run on Γ3(G).
- What it implies: (i) REACH3-ALL: R118 (k)'s REACH3-CYC holds for every genome (its premises ESC3 and W3 are proved here for every
  genome); (ii) the counting lemmas of P-N5-QUIET and the game form of P-N5-ASC hold on the Γ3 run itself (no comparison with the run on
  Γ(G)); (iii) Theorem CHAIN3: under HYPOTHESIS [E-LEV] and CONDITIONAL on the unlanded packets P-N5-END and P-N5-ASC §4, N5′-xi from S3 on Γ3(G) makes at most (1 + n3·((2M + 3)·F′_(U(G))(M) − 1))·(L3 + 1)
  + 3 iterations; for U(G) ≤ B, B fixed, a polynomial in N + M.
- What it does NOT imply: anything about N5 (SPEC's S4a; its pre-fallback run on Ξ-cyclic genomes is not a Howard run, §9 DATA); anything
  for genomes with U(G) unbounded (the quantity Σ_v D^tot_E(v), equivalently P-N5-ASC with unboundedly many ascents, stays OPEN); anything
  without [E-LEV]; anything on games other than Γ3(G); anything about general parity games. The bound is loose and its degree in M grows
  like 5·2^B (from P-N5-ASC's F′, not re-checked here); measured runs are short (max T3 129, LEAP_k64), so L3's tightness is untested.

## To sign
| § | statement | label | hypotheses |
| --- | --- | --- | --- |
| §3 | Lemmas ESC3-ALL, W3-ALL; Theorem REACH3-ALL | PROVED | every genome |
| §4 | Facts F1, F3, F4′, F5, F6, DOM, STRICT on HOW3(G) | PROVED | every genome |
| §5 | Lemmas CN2-3, LOC-GATE3, LOC-K2-3, B-ONLY3; Corollary NO-TIE3 | PROVED | every genome |
| §6 | Theorem QUIET3; Corollary T-QUIET3 | PROVED | every genome |
| §7 | Lemmas E-MON3, CHAIN-DECOMP3 | PROVED | every genome |
| §7 | Corollary HUB-ASC-G3 | PROVED, CONDITIONAL on the unlanded packet P-N5-ASC §4 (R121) | every genome |
| §7 | Lemma UP-JUMP3; Corollary UP-B3 | PROVED | under HYPOTHESIS [E-LEV] |
| §8 | Theorem CHAIN3 | PROVED, CONDITIONAL on the unlanded packets P-N5-END (ENDGAME-3) and P-N5-ASC §4 (R121) | under HYPOTHESIS [E-LEV] |
| §8 | DEAD RUN-TRANSFER | DEAD | instance RT_n1 |
| §9-§11 | DATA, machine checks, TARGET diff | DATA / READING (not to sign) | |
Every row is under the standing SPEC premise 1E-N3 (RESULTS R57 (b)), as in RESULTS R104 / R117.

## 1. Premises (quoted by script: experiments/new/box196/quotes_chain.py, output quotes_chain.out; trunk sources by git show, lane packets
by sha1)
- [DEF] RESULTS R104, definitions only: «Even movers of priority 0; Odd gates of priority 1 with a W-face e and a Ξ-face β»; options
  «each with a W-target of level lev(x) − 1 (none at level 0)»; «β of priority 6 + 2·rank + parity with edges to the Ξ-target and to u,
  or to u alone»; «e of even priority above every β with one edge to the W-target or to the top even self-loop c_W»; «an unused even
  self-loop of priority 2; c_W's priority top is the least even number at least 2 above every other priority so far»; «a closed core
  u = K0 (Even, top + 2) → {K1, K3}, K1 (Even, 5) → {K0, K1}, K2 (Odd, 3) → {K1, K2}, K3 (Even, top + 3) → {K1, K2}».
- [G3] RESULTS R117: Γ3 «obtained from Γ(G) by 4M + 4 single-successor Even pads of priority ≤ 2 (pA on K0 → K3, s on K1's loop, q on
  K1 → K0, r on K2 → K1, pe_g and pβ_g on both faces of every gate g, pb_g on every β_g → u, and m_(x,k) on every mover edge x → (x, k)
  with priority 2 for the genome start and 0 otherwise, appended after Γ(G)'s vertices; n = N + 7M + 10)». The standard state
  (P-N5-REACH §3, the packet R117 lands): «σ(x) = m_(x,s(x)); σ(β_g) = xt(g) if xt(g) is a mover, pb_g otherwise; σ(K0) = pA, σ(K1) = s,
  σ(K3) = K2; τ(g) = pe_g at every gate, τ(K2) = K2; forced choices elsewhere.»
- [R117-SIGN] RESULTS R118 (k)'s text: «RESULTS R117's entry signs S3-START, PAD, K3 and TAU3 for every genome and ESC3, W3 for acyclic
  Ξ-graphs». Used: S3-START («S3's start pair on Γ3(G) is the standard state of Γ3 for the genome start s_0.»), PAD (a) («every cycle
  contains a vertex of Γ»; P-N5-REACH §5 (a)'s proof, quoted in §2 (P)), K3 (b)-(d), TAU3 («In the standard state, Iτ = ∅, so S4b leaves
  τ unchanged.»).
- [K2r] RESULTS R118: «with σ̄(K2) = r proved for every genome in P-N5-XICYC's fixes».
- [R3C] RESULTS R118 (k): «N5′-xi from S3 on Γ3(G) visits only standard states and makes Howard steps at the movers until its first
  fallback, at iteration T3 + 1» («Theorem REACH3-CYC, CONDITIONAL on P-N5-REACH's S3-START, PAD, K3, TAU3, ESC3, W3 for every genome»).
  §3 removes the condition. Its proof is P-N5-XICYC §7 (frozen, sha1 149e2414), re-run in §3 with ESC3-ALL, W3-ALL.
- [N5XI] RESULTS R118 / P-N5-XICYC l. 45-47: «SPEC S1-S5 with ONE change in S4a. At every Even v with |A(v)| ≥ 2 that is not its own
  H-cycle node, σ_new(v) := the Ξσ-best element of TIE(v) := {w ∈ A(v) : W*(v) = v ⊕ W*(w)}.»
- [TERM] RESULTS R15 (a): «Lemma A: for any non-empty unambiguous set I of improvements of σ (VJ00 §4.4), Ωσ ⊴ Ω_{Switch_I(σ)}.»
- [VJ] the value (Λ, Π, k) and its order ⊴, as in R118's premise (VJ00 §4.2 / Friedmann arXiv 1106.0778 §3; P-N5-XICYC l. 31-33): «first
  the reward of Λ (an even priority p gives +p, an odd one −p, with priorities made injective by rank); then Π, decided by the most
  relevant vertex of the symmetric difference, which is better for Even iff it is even and in the larger set; then k, where a longer
  prefix is worse for Even if Λ is even and better if Λ is odd». ext(v, (Λ, Π, k)) := (Λ, Π ∪ {v if v is more relevant than Λ}, k + 1).
- [OPT] σ̄_t is optimal at every vertex at once against σ_t: RESULTS R118's σ̄ as used in R118 (b) (P-N5-XICYC §3 l. 75: «σ̄_t is
  optimal at every vertex at once ([VJ])») and RESULTS R21 (a) («(Odd's best reply σ̄_k is pointwise optimal in G_{σ_k})»). In SPEC runs
  the same fact is [1E-N3] = RESULTS R57 (b) as landed in R104 (used only where a SPEC procedure's output is meant, i.e. §3's S4a arena and
  REACH3-ALL; for HOW3's σ̄_t, a defined object, R57 (b) is NOT used, as in P-N5-QUIET's line L-2, QT-L1) («used in two forms: S1's σ̄, and τ̄ on the dual game, are pointwise
  optima; and S4a's σ_new … is a pointwise optimum of that arena, before S4c»), the standing SPEC premise.
- [END] P-N5-END (lane packet, docs/new/P-N5-END.md frozen at l-new 131b4c1c, sha1 5cae845b; REFEREE 29 SIGN all, END-T3 as
  PROVED-CONDITIONAL; L-RED 58 R223 SURVIVES): Theorem ENDGAME-3, «For every genome G, N5′-xi from S3 on Γ3(G) has exactly one fallback, at
  an iteration F ≥ 1, and makes exactly F + 2 iterations».
- [ASC] P-N5-ASC (lane packet, docs/new/P-N5-ASC.md with fixes entries 1-5; RESULTS R121 when landed): §4's abstract core, Theorem
  HUB-ASC(B) and Lemma SKELETON on the chain system CS(M) (game-free), and the constants F′_0(M) := 1 + M(M + 1)/2, F′_B(M) := (M² + 3M + 1)
  (1 + M·F′_(B−1)(M)²) of §5. Only §4 (game-free) is used as a premise; §3, §5, §6's game lemmas are re-proved on Γ3 in §7.
- [QUIET] P-N5-QUIET (lane packet, docs/new/P-N5-QUIET.md with fixes entries 1-2): its proofs are the templates of §5-§6, re-proved here on
  Γ3; no statement of it is used as a premise.
- HYPOTHESIS [E-LEV] (only §7 UP-JUMP3, UP-B3 and §8 CHAIN3): lev(x) < lev(x′) implies pr(e_(x,k)) < pr(e_(x′,k′)). Γ3 keeps Γ's
  priorities ([G3]); box 189's gamma3.py builds e-priorities in the order (lev, gate), which satisfies it (R104 (vi) leaves the exact
  e-priorities to its packet; P-N5-QUIET fixes entry 2 QT-L3: a hypothesis).
- Not used: PLAY3, SBAR3, KEY3, Fact X (the acyclic-only lemmas of P-N5-REACH), R118 (b)'s F1 / STRICT (re-derived in §4), any statement of
  P-N5-QUIET, any L-RED lemma.

## 2. The model HOW3(G) and facts used
- HOW3(G): Γ3(G) with every non-mover Even vertex frozen at the standard state's choice ([G3]); Odd unrestricted at the gates and K2; a
  state is the frozen part plus a choice at every mover; Ω_t := the [VJ] value against σ̄_t ([OPT]); a HOWARD step: every mover x goes to a
  successor of ⊴-largest Ω_t value and keeps σ_t(x) if it is such a successor (ties among best successors by any rule); T3 := the first
  state at which no mover has a strictly better successor. n3 := N + 7M + 10.
- (R) Rank order, by Ω first: pads, movers, gates, c_X (Ω ≤ 2) < K2 (3) < K1 (5) < every β (≥ 6) < every e < c_W (top) < K0 (top + 2)
  < K3 (top + 3) ([DEF], [G3]; ranks order by Ω, then index).
- (P) PAD (a), proof as in P-N5-REACH §5 (a): a pad's successor is a vertex of Γ, so every cycle contains a vertex of Γ; every cycle inside
  the core contains K0, K1 or K3, except K2's loop (Ω 3); a cycle through a mover passes a gate, then pe_g → e_g or pβ_g → β_g with Ω ≥ 6;
  c_W's loop has Ω top; c_X has no in-edge but its loop. So every cycle other than c_X's loop has a vertex of Ω ≥ 3.
- (E-DOM) Every vertex more relevant than some e-vertex is an e-vertex, c_W, K0 or K3 ((R)).
- (Core) In standard states and in HOW3: K0 → pA → K3 → K2 and K1 → s → K1 are frozen; Odd chooses at K2 between r (→ K1) and its loop.
  K3's only in-edge is from pA, pA's only from K0; K0's in-edges are from q (q's only in-edge is from K1, which plays s) and from the
  pb's. So a play passes K0 iff it passes K3, iff it enters the core through some pb_g; K0 and K3 lie on no cycle.

## 3. ESC3 and W3 for every genome; REACH3-ALL (PROVED)
Setting: any genome; a mover state s; the standard state (σ, τ) for s; S4a's arena H (Even v keeps A(v) = {σ(v)} ∪ Iσ(v), Odd follows τ);
W* := the values of S4a's pointwise optimum in H ([1E-N3]); ⊕ := ext. Used: [DEF] (W-targets have level lev − 1; level-0 e's go to c_W),
[G3], K3 and TAU3 ([R117-SIGN]), [1E-N3]. The Ξ-targets enter only through the β-vertices, and no proof below follows a β → xt edge
except W3-ALL (i)'s single β step, after which levels strictly decrease.
**Lemma ESC3-ALL.** In every standard state: Iσ ∋ (K0, K1), so Iσ ≠ ∅; every pointwise optimum of H agrees with σ at every Even vertex
that is not a mover; TIE(β_g) = {xt(g)} for every β_g with xt(g) a mover, and TIE(K0) = {pA}.
Proof.
- (K0, K1) ∈ Iσ: K3 (b) (every genome).
- β_g with xt(g) a mover: A(β_g) ⊆ {xt(g), pb_g} ([DEF] edges) and σ(β_g) = xt(g) ∈ A(β_g). In H, Odd plays τ: pe at every gate, K2 → K2.
  An H-play from xt(g) is a mover, a pad m in A(·), its gate, pe, e, then (level ≥ 1) a mover one level lower, …: it never leaves a gate
  by pβ, so it meets no β, and after at most lev(xt(g)) + 1 e-steps it enters c_W's loop: node c_W, even, reward p′(c_W) > 0. An H-play
  from pb_g enters K0 and stays in the core, ending in an odd cycle (node K1 or K2; K3 (d)). REWARD: every H-value via xt(g) beats every
  H-value via pb_g. β_g is on no H-cycle: its only in-edge is from pβ_g, whose only in-edge is from a gate, which plays pe in H. So the
  pointwise optimum picks xt(g), W*(β_g) = β_g ⊕ W*(xt(g)), and β_g ⊕ W*(pb_g) has another node: TIE(β_g) = {xt(g)}.
- Core: K3 (d) (every genome): every pointwise optimum keeps pA at K0; K0 is on no H-cycle and the two H-values from K0 have different
  nodes (K2 via pA, K1 via K1), so TIE(K0) = {pA}.
- Pads, e, c_X, c_W, β_g with xt = X: one successor in H. ∎
**Lemma W3-ALL.** In every standard state, for every s:
- (i) W := the value of the (σ, τ)-play: W(x) = (c_W, ∅, 5ℓ + 5) for a mover x of level ℓ; W(m) = (c_W, ∅, 5ℓ + 4) for the pad of its
  chosen option, W(g) = (c_W, ∅, 5ℓ + 3), W(pe_g) = (c_W, ∅, 5ℓ + 2), W(e_g) = (c_W, ∅, 5ℓ + 1); W(β_g) = (c_W, ∅, 5·lev(xt(g)) + 6) when
  xt(g) is a mover.
- (ii) In H: W*(m_(x,k)) = (c_W, ∅, 5ℓ + 4) for EVERY m_(x,k) ∈ A(x), and W*(x) = (c_W, ∅, 5ℓ + 5).
- (iii) No mover x is its own H-cycle node, and TIE(x) = A(x).
Proof. (i) Under τ every gate takes pe: x → m → g → pe_g → e_g → (ℓ ≥ 1: the W-target, a mover of level ℓ − 1; ℓ = 0: c_W). By
induction on ℓ the play reaches c_W after 5ℓ + 5 steps through movers, pads, gates and e's, all less relevant than c_W ((R)): P = ∅.
β_g → xt(g) adds one step. (ii) In H every play from a gate follows τ (pe), and every option of a mover in H is a pad to its gate; so every
H-play from m_(x,k) has the shape of (i) with some choices at lower movers: node c_W, P = ∅, length 5ℓ + 4, whatever the choices.
(iii) Every H-play from x descends in level to c_W, so x lies on no H-cycle; x ⊕ W*(y) = (c_W, ∅, 5ℓ + 5) = W*(x) for every y ∈ A(x). ∎
**Step check of the landed text.** experiments/new/box196/quotes196.py (record; `git show` of trunk docs/new/P-N5-REACH.md §6.5-§6.6,
verbatim, 16 steps; output quotes196.out) flags every step containing Ξ, xt(, X-chain, PLAY3, SBAR3, KEY3, Fact X, acycl, ACYC, «β_g →»,
«→ β». Flagged: ESC3.2 and W3.2 (the IDEAL-ACYC labels only); ESC3.3 (xt(g) named as β_g's successor, an edge of [DEF]); ESC3.4 (the
H-play from xt(g) takes pe at every gate, so no Ξ-edge); W3.5 (one β → xt step, then a W-descent). No step cites PLAY3, SBAR3, KEY3, Fact X.
L-RED 58 checked the same steps by hand (R224-chain §1: OK) and found no Ξ-cyclic counterexample (R223-reach: SURVIVES).
**Theorem REACH3-ALL.** For every genome G, the N5′-xi run from S3 on Γ3(G) visits only standard states and its mover parts form a run of
HOW3(G) (tie rule: Ξσ-best, then SPEC's choice, then the larger index) until its first fallback, at iteration T3 + 1.
Proof. Induction on j: state j is standard. j = 0: S3-START. Step j < T3 (some mover has a strictly better successor):
- τ: TAU3 gives Iτ = ∅ in every standard state, so τ_new = τ (S4b does nothing; S4c acts on Iτ only if Iσ = ∅, and Iσ ≠ ∅ by ESC3-ALL).
- Off the movers: σ_new = σ by ESC3-ALL, for SPEC's pointwise optimum and for [N5XI]'s rule (TIE = {σ(v)} at β_g and K0; one successor
  elsewhere).
- Movers: where |A(x)| = 1, σ_new(x) = σ(x) is forced. Where |A(x)| ≥ 2, x is not its own H-cycle node and TIE(x) = A(x) (W3-ALL (iii)),
  so [N5XI] picks the Ξσ-best element of A(x); A(x) contains every successor strictly better than σ(x), so this is a ⊴-best successor:
  a Howard step (and A(x) = {σ(x)} when nothing is strictly better).
- Some mover changes, so σ_new ≠ σ and S4c does not fire; state j + 1 is standard.
Step T3: A(x) = {σ(x)} at every mover, so σ_new = σ, τ_new = τ, while Iσ ∋ (K0, K1): S4c fires at iteration T3 + 1. ∎
Remark (N5). For SPEC's S4a the same induction gives standard states, but SPEC picks in TIE(x) = A(x) by its root-first key, not by Ξσ:
not a Howard step in general. §9 DATA: «nohoward» fires in spec mode. Nothing here is claimed for N5's pre-fallback run on Ξ-cyclic G.

## 4. Facts on HOW3(G) (PROVED; R118 (b) not used, after L-RED 58 R223-reach §3)
- F1. Ω_t ⊴ Ω_(t+1) pointwise. A Howard step switches exactly the movers whose new successor is strictly better, one switch per vertex: a
  non-empty unambiguous set of improvements (VJ00 §4.4); [TERM]. (R15's object is SPEC with its injective ranks, which covers Γ3's repeated
  pad priorities.)
- F3. If Λ_t(v) ≠ v then Ω_t(v) = ext(v, Ω_t(nx_t(v))), nx_t(v) := σ_t(v) for Even v, σ̄_t(v) for Odd v; and Ω_t(w) = (w, ∅, 0) when
  Λ_t(w) = w. Proof: by [OPT] the play from v under (σ_t, σ̄_t) is v followed by the play from nx_t(v); v is on the prefix or on the cycle
  below Λ. ([VJ], game-free.)
- F4′. If v ∉ Π(A) ∪ Π(B), then A ⊴ B ⇒ ext(v, A) ⊴ ext(v, B) and A ◁ B ⇒ ext(v, A) ◁ ext(v, B). Proof: equal Λ: v is added to both Π or
  to neither, the symmetric difference is unchanged, both lengths grow by 1; different Λ: decided by Λ, which ext keeps. ([VJ].)
- F5. σ_(t+1)(x) is ⊴-best among x's successors under Ω_t, and Ω_t(σ_(t+1)(x)) ▷ Ω_t(σ_t(x)) when they differ (definition of HOW3).
- F6. No mover is the cycle node of its own play ((P): a cycle through a mover has a vertex of Ω ≥ 6; movers have Ω 0). Every non-mover
  Even vertex has one successor in HOW3.
- DOM. For every mover x, step t and successor y of x: Ω_(t+1)(x) ⊵ ext(x, Ω_t(y)). Proof: F3, F6 at t + 1 give Ω_(t+1)(x) =
  ext(x, Ω_(t+1)(σ_(t+1)(x))); by F1 and F4′ (x ∉ any Π, CN2-3) this is ⊵ ext(x, Ω_t(σ_(t+1)(x))), which by F5 and F4′ is ⊵ ext(x, Ω_t(y)). ∎
- STRICT. If σ_(t+1)(x) ≠ σ_t(x), then Ω_(t+1)(x) ▷ Ω_t(x). Proof: DOM gives ⊵ ext(x, Ω_t(σ_(t+1)(x))); F5 and F4′ (strict) give ▷
  ext(x, Ω_t(σ_t(x))) = Ω_t(x) by F3 and F6. ∎
- F2. If Ω(v) ⊴ Ω′(v) and Λ ≠ Λ′, the reward of Λ′ is strictly larger; distinct vertices have distinct rewards ([VJ]).
- CYC. Λ_t(v) takes values among at most 2M + 3 vertices: the M e's, the M β's, c_W, K1, K2 (pads, movers, gates: CN2-3; K0, K3: (Core);
  c_X only for c_X itself), and by F1 and F2 it changes only to a vertex of strictly larger reward.

## 5. Lemmas on HOW3(G) (PROVED)
**Lemma CN2-3.** For every positional pair of Γ3(G) and every vertex v ≠ c_X, the cycle node of v's play has Ω ≥ 3; no mover, gate or pad
is ever a cycle node or in a set Π.
Proof. (P): the cycle of v's play (v ≠ c_X; c_X has no in-edge but its loop, so no other play reaches it) has a vertex of Ω ≥ 3, and its
node is its most relevant vertex. Movers (0), gates (1) and pads (≤ 2) rank below every vertex of Ω ≥ 3 ((R)), so they are never a cycle
node and never more relevant than one, hence never in Π ([VJ]: Π holds only vertices more relevant than the node). ∎
**Lemma LOC-GATE3.** Let t be a state, g a gate, a := σ̄_t(g) ∈ {pe_g, pβ_g}, b the other face, Ω := Ω_t. If Ω(a) ≠ Ω(b), then Ω(a) ◁ Ω(b).
Proof (P-N5-QUIET §3's proof; on Γ3 the faces are pads). Suppose Ω(b) ◁ Ω(a). Let τ := σ̄_t with g switched to b. By [OPT], Ω(g) ⊴
val_τ(g), the value of g's play under (σ_t, τ). We show val_τ(g) ◁ Ω(g), a contradiction. Ω(g) = ext(g, Ω(a)) (F3; g is not a cycle node,
CN2-3).
- Case 1: b's play under (σ_t, σ̄_t) does not visit g. Then g's play under τ is g followed by b's play: val_τ(g) = ext(g, Ω(b)); g ∉
  Π(Ω(a)) ∪ Π(Ω(b)) (CN2-3), so F4′ gives ext(g, Ω(b)) ◁ ext(g, Ω(a)) = Ω(g).
- Case 2: b's play visits g: b = z_1, …, z_m, g, … with z_i distinct and ≠ g, P := {z_1, …, z_m}; after g it follows a, so b, g, a end in
  the same cycle, Λ := its node. Under τ, g's play is the cycle C = {g} ∪ P, whose node c is its most relevant vertex, c ∈ P (CN2-3).
  - 2-i: a's play does not visit g (so it meets no z_i). Π(b) = Π(a) ∪ Rel(P), Rel(P) := the elements of P more relevant than Λ;
    k(b) = k(a) + m + 1.
    - 2-i-a, Rel(P) ≠ ∅: its most relevant element r is c; Ω(b) ◁ Ω(a) with equal Λ is decided by Rel(P), so r is odd; r is more
      relevant than Λ, so reward(c) = −p′(c) < reward(Λ): val_τ(g) ◁ Ω(g).
    - 2-i-b, Rel(P) = ∅: Π(b) = Π(a), k(b) > k(a), and Ω(b) ◁ Ω(a) means Λ is even; every vertex of C is less relevant than Λ, so
      reward(c) < p′(Λ): val_τ(g) ◁ Ω(g).
  - 2-ii: a's play visits g. Then g is on the σ̄-cycle Q = (g, a = w_1, …, w_l, g), Λ ∈ Q ∖ {g}, Π(a) = ∅, k(a) = dist_Q(a, Λ),
    Ω(g) = (Λ, ∅, k(a) + 1). b's play first meets Q at q; P0 := the part of P before q; Π(b) = Rel(P0), k(b) = |P0| + dist_Q(q, Λ), and
    C = {g} ∪ P0 ∪ arc, arc := Q's vertices from q up to g.
    - 2-ii-a, Rel(P0) ≠ ∅: as 2-i-a.
    - 2-ii-b, Rel(P0) = ∅, Λ ∈ arc: c = Λ and val_τ(g) = (Λ, ∅, k(b) + 1) against Ω(g) = (Λ, ∅, k(a) + 1): the comparison of Ω(b) with
      Ω(a): val_τ(g) ◁ Ω(g).
    - 2-ii-c, Rel(P0) = ∅, Λ ∉ arc: the path from q to Λ passes g and a, so k(b) > k(a), Π(b) = Π(a) = ∅; Ω(b) ◁ Ω(a) means Λ is even;
      every vertex of C is less relevant than Λ: val_τ(g) ◁ Ω(g). ∎
**Lemma LOC-K2-3.** At every state σ̄_t(K2) = r and Ω_t(r) = (K1, ∅, 1) ◁ Ω_t(K2) = (K1, ∅, 2).
Proof. K1 → s → K1 is frozen: Ω(K1) = (K1, ∅, 0), Ω(s) = Ω(r) = (K1, ∅, 1). K2's loop gives node K2, reward −p′(K2) > −p′(K1) (K2 is less
relevant than K1, both odd); [OPT] takes the smaller: σ̄(K2) = r (also [K2r]), Ω(K2) = (K1, ∅, 2) (F3), and with node K1 odd the longer
prefix is better for Even. ∎
**Lemma B-ONLY3.** At every state t and every vertex v other than c_W, the e-vertices whose successor is c_W, and the pads pe_g of those
e-vertices, Λ_t(v) is less relevant than every e-vertex.
Proof (P-N5-QUIET fixes entry 1's B-ONLY, credit L-RED R221 §3, on Γ3). τ_β := «pβ at every gate, r at K2». e_g's only in-edge is from
pe_g, and pe_g's only from g; under (σ_t, τ_β) no gate enters pe_g. So the play from v meets an e-vertex only at its start (v = e_g or
v = pe_g) and reaches c_W only through a level-0 e. For the v of the statement its cycle holds no e-vertex and not c_W, and not K0, K3
((Core)): by (E-DOM) its node is less relevant than every e-vertex, with a smaller reward (every e is even, [DEF]). By [OPT], Ω_t(v) ⊴ v's
value under (σ_t, τ_β); rewards come first ([VJ]), so reward(Λ_t(v)) is below every e-vertex's reward, hence Λ_t(v) is not an e-vertex,
not c_W, not K0, K3 (never cycle nodes), and so less relevant than every e-vertex. ∎
**Corollary NO-TIE3.** At every state and gate g, Ω_t(pe_g) ≠ Ω_t(pβ_g).
Proof. If e_g → c_W: Λ(pe_g) = c_W while Λ(pβ_g) ≠ c_W (B-ONLY3). Otherwise Λ(pe_g) is less relevant than e_g (B-ONLY3), so e_g ∈
Π(pe_g); equality needs e_g ∈ Π(pβ_g), i.e. pβ_g's play passes g, pe_g, e_g and then e_g's play, so k(pβ_g) > k(pe_g). ∎
So LOC-GATE3 decides every gate at every state: σ̄_t(g) is the face of strictly ⊴-smaller value.

## 6. QUIET on Γ3 (PROVED)
Definitions. class_t(v) := (Λ_t(v), E_t(v)), E_t(v) := the e-vertices of Π_t(v). A step t → t+1 is LOUD if some vertex changes class,
else QUIET; Q := the number of loud steps; a quiet window is a maximal interval of states whose steps are all quiet. D^tot_E(v) := the
number of distinct classes of v over the run. A class (w, S) is a B-class if w is less relevant than every e-vertex, else an E-class.
- (F-cls3) The order compares reward(Λ), then E (the top layer of Π: only e-vertices, c_W, K0, K3 are more relevant than an e-vertex
  (E-DOM); c_W is never in Π; K0 and K3 are both or neither on a play (Core)), then the rest. So each class is a convex set of values, each
  vertex is in each class during one interval of states (F1), distinct classes compare the same way at all times, and Q ≤ Σ_v (D^tot_E(v)
  − 1).
- (F-E3) An E-class has w an e-vertex or c_W (E-DOM; K0, K3 are never cycle nodes, (Core)).
**Theorem QUIET3.** Every quiet window of HOW3(G) has at most L3 := (M + 1)(2M + 1)(N + 1) + N(n3 − 1) steps.
**Corollary T-QUIET3.** T3 ≤ Q + (Q + 1)·L3 ≤ (1 + Σ_v (D^tot_E(v) − 1))·(L3 + 1), the sum over the n3 vertices of Γ3(G).
Proof of QUIET3. Fix a quiet window [a, b]; every vertex keeps its class on [a, b].
- (Q1) If a gate's faces pe_g, pβ_g are in different classes, their order is fixed on [a, b] (F-cls3), so σ̄_t(g) is constant (LOC-GATE3).
- (Q2) For a mover x and a step in [a, b], ext at x, at its pad m and at the gate changes neither Λ nor E (CN2-3), so x's chosen option's
  value lies in class(x); and at a state t < b no option of x has a value in a class above class(x) (by DOM x's value at t + 1 would lie in
  that class).
- (Q3) E-class vertices: if class(v) = (w, S) is an E-class, Π_t(v) = S on [a, b] (only e-vertices, c_W, K0, K3 are more relevant than w;
  c_W is never in Π; K0, K3 lie only on plays with node K1 or K2, (Core)). So Ω_t(v) = (w, S, k_t); by F1 k_t is monotone with values in
  {0, …, n3 − 1}: at most n3 − 1 changes.
- (Q4) B-class structure. Let C = (w, S) be a B-class.
  - pβ_g → β_g → z, z = xt(g) or pb_g (frozen): class(pβ_g) = class(β_g) = class(z) (β_g ∉ Π(z): if z's play met β_g it would close a
    cycle through β_g, which lies below its node; pβ_g ∉ Π by CN2-3).
  - pe_g → e_g → y: if e_g is in C then e_g ∈ S and y is in the B-class (w, S ∖ {e_g}) (every e is more relevant than w).
  - G_C := the movers of class C with their options whose gate's chosen face is in C. A C-mover's play is a simple G_C-path until a
    boundary point: an e-face into a class (w, S ∖ {e}); the exit β → pb → K0 → pA → K3 → K2 → r → K1 → s → K1, constant (core frozen,
    σ̄(K2) = r by LOC-K2-3); or w itself, Ω(w) = (w, ∅, 0).
- (Q5) B-class stabilisation. For s = 0, …, M let a_s := a + (s + 1)(2M + 1)(N + 1). Claim: every vertex of a B-class (w, S) with |S| = s
  is constant on [min(a_s, b), b].
  - Assume it for s − 1. Fix C = (w, S), |S| = s. After a_(s−1) (after a if s = 0) every boundary value of C is constant.
  - A gate with both faces in C has its e-face of constant value ext(pe, ext(e, Ω(y))) after a_(s−1), while its β-face's value only rises
    (F1). By LOC-GATE3 and NO-TIE3 it flips at most once after a_(s−1). Gates with faces in different classes do not flip (Q1). So after
    a_(s−1) G_C and its chosen faces change at most M ≤ 2M times: at most 2M + 1 sub-windows.
  - In a sub-window from c with G_C fixed, opt(x) := the ⊴-largest value of a simple G_C-path from x to a boundary point (constant). Upper
    bound: Ω_t(x) ⊴ opt(x) (Q4). Lower bound (Bellman-Ford): Ω_(c+h)(x) ⊵ the value of every such path with at most h movers, by induction
    on h with DOM at x, F3 at the pad, the gate, the face pad and the face, F1 and F4′ (x, m, the gate and the pads are in no Π by CN2-3;
    the face is in neither Π, by (Q4)'s argument and simplicity). Simple G_C-paths have at most N movers, so Ω_t(x) = opt(x) for t ≥ c + N,
    and every C-vertex is then constant (non-movers by F3).
  - A sub-window ends only at a flip, which needs a β-face change, i.e. a C-value change. So each sub-window after the first starts within
    N + 1 steps of the previous one, and C is constant from a_(s−1) + (2M + 1)(N + 1) = a_s on. ∎ (claim)
- (Q6) |S| ≤ M, so every B-class vertex is constant from a_M on. Each step changes σ at some mover, whose value strictly rises (STRICT);
  after a_M that mover is in an E-class, and by (Q3) E-class movers change at most N(n3 − 1) times in all. So b − a ≤ L3. ∎
Proof of T-QUIET3. Steps are loud or quiet; quiet steps form at most Q + 1 windows of at most L3 steps each; (F-cls3). ∎

## 7. P-N5-ASC's game form on Γ3 (PROVED)
seq_t(v) := the e-vertices of Π_t(v) in play order; E_t(v) their set; an ascent of seq_t(v) is a step to a more relevant element; sets of
e-vertices are compared lexicographically by their most relevant differing element; D_E,I(v) := the number of distinct E_t(v) on an
interval I with Λ_t(v) = w fixed; M_w := the number of e-vertices more relevant than w; U(G) := the number of options (x, k) whose Ξ-target
is a mover of level > lev(x).
**Lemma E-MON3.** If Λ_t(v) = Λ_(t+1)(v) then E_t(v) ≤ E_(t+1)(v).
Proof. F1: Ω_t(v) ⊴ Ω_(t+1)(v). With equal node w, [VJ] decides by z, the most relevant vertex of Π_t(v) Δ Π_(t+1)(v) (if any): z is in
the later set if even, in the earlier if odd. c_W is never in Π; K0, K3 are both or neither on each play, and both plays have node w, so
both or neither contain them ((Core)); pads are in no Π (CN2-3). So if an e-vertex lies in the symmetric difference, z is an e-vertex
(E-DOM), even, in Π_(t+1)(v): E_t(v) < E_(t+1)(v). Otherwise the e-sets are equal. ∎
**Lemma CHAIN-DECOMP3.** If seq_t(v) = (f, …), then f's successor y_f is a mover, Λ_t(y_f) = Λ_t(v) and E_t(v) = {f} ∪ E_t(y_f).
Proof. f ∈ Π_t(v) is more relevant than w := Λ_t(v), so f is on the prefix (cycle vertices other than w are less relevant than w). f is
Even with one successor ([DEF]; Γ3 adds no pad on e → W-target), so the play from f is f then the play from y_f (F3). y_f ≠ c_W, else the
node would be c_W, more relevant than f. So y_f is the W-target mover; its play is a suffix of v's, Λ_t(y_f) = w, and no e-vertex of
Π_t(v) precedes f. ∎
**Corollary HUB-ASC-G3.** For every vertex v (movers, gates, pads, K-vertices, all of Γ3) and every interval I of states of HOW3(G) with
Λ_t(v) = w on I: if seq_t(v) has at most B ascents for every t ∈ I, then D_E,I(v) ≤ F′_B(M_w); over the whole run, D^tot_E(v) ≤
(2M + 3)·F′_B(M).
Proof (P-N5-ASC §5's proof, with E-MON3, CHAIN-DECOMP3, F1, F2, CYC on Γ3). Items := the e-vertices more relevant than w, in relevance
order; item x is active at t iff Λ_t(x) = w, and its active times form an interval (F1, F2). At each t ∈ I, next_t on the active items is
one forest (CHAIN-DECOMP3), each active item's chain is E_t(x) in the order seq_t(x), and by E-MON3 each chain is lex-nondecreasing over its
active times; the hub's value is seq_t(v). Refining by the times where the active set changes gives at most M² + 3M + 1 levels; inside
one, the active items form a run of CS(M_w), and [ASC] §4 (HUB-ASC(B), SKELETON) applies word for word. Whole run: Λ_t(v) takes at most
2M + 3 values (CYC), and classes are (Λ, E) pairs. ∎
**Lemma UP-JUMP3 (under [E-LEV]).** Let a, b be consecutive in seq_t(v) with b more relevant than a, a = e_(x,k), ℓ := lev(x). Then the
play from a to b passes a β-vertex whose Ξ-target is a mover of level > the level of the mover it was entered from.
Proof. ℓ ≥ 1 (at level 0 a's successor is c_W and the node would be c_W, more relevant than a ∈ Π). The play continues at the W-target, a
mover of level ℓ − 1. b = e_(x′,k′) for a mover x′ on the play; by [E-LEV], lev(x′) ≥ ℓ. Between a and b the play leaves each mover through
its pad, its gate and a face pad to its e-face (then to a mover one level lower) or its β-face; a β-face goes to pb → K0 (then the play
stays in the closed core and never reaches b) or to its Ξ-target mover. Pads change no level. So the first step after the W-target that
reaches a level ≥ ℓ is a Ξ-step that goes strictly up. ∎
**Corollary UP-B3 (under [E-LEV]).** For EVERY vertex v of Γ3 (pads and K-vertices included: UP-JUMP3 is a statement about plays) and every
state, seq_t(v) has at most U(G) ascents: the segments between consecutive elements of seq_t(v) are disjoint parts of the play's prefix,
each ascent's segment holds a β-vertex with an upward Ξ-edge (UP-JUMP3), and each β-vertex has one Ξ-edge. Hence D^tot_E(v) ≤
(2M + 3)·F′_(U(G))(M) (HUB-ASC-G3). ∎

## 8. Theorem CHAIN3 and DEAD RUN-TRANSFER
**Theorem CHAIN3 (PROVED, under HYPOTHESIS [E-LEV], CONDITIONAL on the unlanded packets P-N5-END (ENDGAME-3, [END]) and P-N5-ASC §4
(the abstract core and F′, [ASC]; RESULTS R121 when landed); P-N5-QUIET is not a premise).** Under HYPOTHESIS [E-LEV], if ENDGAME-3 and
P-N5-ASC §4 hold (both lane packets, unlanded), then for every genome G, N5′-xi from S3 on Γ3(G) makes at most
  T3 + 3 ≤ (1 + n3·((2M + 3)·F′_(U(G))(M) − 1))·(L3 + 1) + 3
iterations, n3 = N + 7M + 10, L3 = (M + 1)(2M + 1)(N + 1) + N(n3 − 1). For U(G) ≤ B, B fixed, this is a polynomial in N + M; Γ3(G)'s size
is polynomial in N + M at bit cost (R117: n3 vertices, n3 + O(M) edges, priorities below top + 4 = O(M)).
Proof. REACH3-ALL: the run up to its first fallback is a HOW3(G) run of length T3 and the first fallback is iteration F = T3 + 1.
ENDGAME-3 ([END]): exactly F + 2 = T3 + 3 iterations. T-QUIET3: T3 ≤ (1 + Σ_v (D^tot_E(v) − 1))(L3 + 1) over the n3 vertices; UP-B3 with
HUB-ASC-G3 gives D^tot_E(v) ≤ (2M + 3)·F′_(U(G))(M) for every v. ∎ (L-RED 58 R224-chain §4: the formula follows exactly.)
- READING (not to sign): F′_B has degree 5·2^B − 3 in M ([ASC] §4; not re-checked here), so the bound is polynomial only for bounded B and
  very loose; this bounds iterations, and the per-iteration cost at bit cost is a separate gauntlet step-4 item.
**DEAD RUN-TRANSFER.** The route «T3 equals the IDEAL-CYC count T_CYC on Γ(G), so P-N5-QUIET's bound transfers» is DEAD. Instance RT_n1
(experiments/new/box196/inst/RT_n1.json, sha1 829f3c97f8c1eadf4f57933ab40c398ad62e8f66; N 1, one mover of level 0 with three options, all
Ξ self-loops, start option 0): N5′-xi from S3 on Γ3 has T3 = 1 (state 0 → option 2), box 191's idealcyc on Γ(G) has T_CYC = 2 (0 → 1 → 2).
Obstruction: at state 0 options 1 and 2 are EXACTLY tied in both games, and the tie rules differ (idealcyc: keep, then larger vertex
index; N5′-xi: Ξσ-best, then SPEC's root-first key, then larger index). R118 (a) allows any tie rule, so T_CYC is not one number. Counters
on RT_n1: tdiff 1, seqdiff 1 (check196.out). L-RED R221 §7 found the same divergence (11 of 2,150 genomes); REFEREE-2 33 (7 of 2,000).

## 9. DATA (not to sign; tools in experiments/new/box196/; check196.sh run by check.sh)
Unit: runs of N5′-xi (default) or N5 (Q196_MODE spec) from S3 on Γ3(G) (box189 gamma3.build, all pads; box190 n5v.step), observed on states
0, …, T3. Scope: Γ3(G) as built by gamma3.py (pinned), e-priorities by (lev, gate), so [E-LEV] holds on every instance. Tool qt3_196.py;
families box195 eg195.gen (rand, esc, noesc, deep, dense, lvl0, late, acyc; L-RED R221 §11's generator, transcribed there with credit).
- Record sweep, data/sweep196.out (one tool version): 8,000 runs (8 families × 500 × seeds 1961, 1962) and 58 pinned genomes
  (box189/corpus, box191-box195/inst, RT_n1): REACH3-ALL: nonstd 0 (unit: states), nohoward 0 (unit: (state, mover) pairs); CN2-3: cnlow 0
  (unit: (state, vertex) pairs); LOC-GATE3: locfail 0, NO-TIE3: ties 0 (unit: (state, gate) pairs); B-ONLY3: bonly 0 (unit: (state, vertex)
  pairs); LOC-K2-3: k2fail 0 (unit: states); QUIET3: wfail 0 (unit: quiet windows), crossflip 0 (unit: σ̄ flips); T-QUIET3: Tfail 0 (unit:
  runs); E-MON3: emon 0 (unit: (step, vertex) pairs); UP-B3: upfail 0 (unit: (state, vertex) pairs with more than U(G) ascents), max ascents
  4. Longest quiet window 32 (RS2_L32M6); max T3 129 (LEAP_k64).
- Controls in sweep196.out and check196.out (each fail counter of §5-§7 has a firing control: Tfail, T-QUIET3's counter, fires in ctrl1):
  ctrl1 (L3 := 0, U(G) := −1) wfail 32, Tfail 22, upfail 26,477 (50 runs); ctrl2 (order
  reversed) locfail 3,320; ctrl3 (no excluded vertex in B-ONLY3) bonly 2,269. Spec mode (N5): nohoward 599 (rand, 200 runs) and 911 (dense,
  200 runs): N5's pre-fallback run is not Howard on Ξ-cyclic genomes (§3 Remark); every other counter 0 there.
- Controls for nonstd, cnlow, k2fail, crossflip, emon: L-RED 58's fault injection into qt3_196.check() (experiments/red/r224/ctrl224.py
  at claude/l-red e7937985, COPIED with credit as experiments/new/box196/ctrl196.py, output ctrl196.out, identical to L-RED's
  out/ctrl224.txt): 75 of 75 (genome, counter) controls fire (clean 0, injected > 0) on L-SI's 11 box-85 genomes (copied to
  box196/inst_si85/, L-SI's sha1 in SHA1SUMS) and 4 corpus genomes. Faults edit the counters' view of values, not the game.
- Record (RUN-TRANSFER): tdiff (runs with T3 ≠ T_CYC) 100 of the 8,000 xi runs, seqdiff 1,013; spec mode tdiff 138 / 200 (rand), 146 / 200
  (dense).
- Independent (cited, not re-run): L-RED 58 R223-reach (own Γ3 builder, own valuation): ESC3, W3, Howard, start counters 0 on 43,816
  exhaustive N ≤ 2 Ξ-cyclic genomes and 7,000 random N 3-6; R224-chain §3 (own code): QUIET3 / T-QUIET3 on 6,000 Γ3 runs, wov 0, tq 0.
- Limits: every run is short (max T3 129); L3 is in the thousands to millions on these instances, so these data test only that nothing
  exceeds it, not its tightness.

## 10. Machine checks
- check.sh block «BOX 196 CHAIN»: re-runs check196.sh (8 families × 100, seed 1964; the three controls; spec on 100 runs; RT_n1, LEAP_k64,
  RS2_L32M6, rd3_d4, cyc_d8), diffs check196.out, requires 0 in every fail counter outside «ctrl» / «spec» lines and the controls to fire.
- check.sh block «P-N5-CHAIN»: sha1 of this packet and of every tool, instance and output it cites, against experiments/new/box196/chain.pins.
- §1's quotes: experiments/new/box196/quotes_chain.py (record; needs git objects), output quotes_chain.out. §3's step check:
  quotes196.py, output quotes196.out.

## 11. TARGET.md diff and limits
- TARGET.md §2 (M4) asks for an algorithm polynomial on EVERY parity game; §4: «Polynomial only on a restricted class» is not M4. CHAIN3 is
  a polynomial iteration bound for one algorithm (N5′-xi) on one restricted family ({Γ3(G) : U(G) ≤ B}, under [E-LEV]), conditional on
  unlanded packets (P-N5-END, P-N5-ASC). Not M3, not M4, not a step-4 pass. G-N5-TIME stays OPEN; N5′-xi stays a CANDIDATE (D1).
- Limits: nothing for N5; nothing for U(G) unbounded; nothing without [E-LEV]; nothing outside Γ3(G).
