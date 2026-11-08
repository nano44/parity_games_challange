# Box 196 «CLOSE THE Γ3 CHAIN» (L-NEW successor 64, Opus 5.5; D1 / D14 / D18)
Written 2026-11-08 06:59Z (date -u). Labels: PROVED (landed R-id) / PROVED (lane, packet) / PROVED (lane, box 196; unrefereed) /
PROVED-CONDITIONAL / CONJECTURE / DATA / DEAD / READING (not a claim). Nothing here is a TARGET.md claim. G-N5-TIME stays OPEN.

Target statement (Lead brief): «under [E-LEV], for genomes with bounded U(G), N5′-xi from S3 on Γ3(G) makes polynomially many
iterations».

Verdict. (a) The chain has exactly two links that were OPEN: ESC3 / W3 for Ξ-cyclic genomes (premises of REACH3-CYC), and the bound on
T3 itself (T-QUIET is proved on Γ(G), and the Γ3 run differs from the Γ run: DEAD route RUN-TRANSFER, §6). (b) Both close by
re-proving on Γ3 directly, with no run comparison: §2 (ESC3-ALL, W3-ALL, hence REACH3-CYC for every genome) and §3-§4 (QUIET3,
T-QUIET3, E-MON3, CHAIN-DECOMP3, UP-JUMP3, UP-B3, HUB-ASC-G3 on the Γ3 Howard model). §5 Theorem CHAIN3: under [E-LEV], N5′-xi from S3
on Γ3(G) makes at most (1 + n3·((2M + 3)·F′_(U(G))(M) − 1))·(L3 + 1) + 3 iterations, L3 := (M + 1)(2M + 1)(N + 1) + N(n3 − 1),
n3 = N + 7M + 10: polynomial in N + M for U(G) ≤ B, B fixed (degree in M grows like 5·2^B). PROVED (lane, box 196), on premises of
which two packets (P-N5-ASC = R121 to land, P-N5-QUIET) and one lane packet (P-N5-END) are not landed. What it does NOT give: §7.

## 1. The chain (a): from landed RESULTS and lane lemmas to the target
Model names. Γ3(G): RESULTS R117. N5′-xi: RESULTS R118's [N5XI]. HOW3(G) := the Howard model on Γ3(G): every non-mover Even vertex frozen
at the standard state's choice (P-N5-REACH §3: σ(β_g) = xt(g) if xt(g) is a mover, else pb_g; σ(K0) = pA, σ(K1) = s, σ(K3) = K2; pads
forced), Odd unrestricted (gates, K2), Howard steps at the movers (R118 (a)'s definition, any tie rule), from S3's mover choice.

| # | link | status | where |
| --- | --- | --- | --- |
| C1 | S3-START, PAD (a)-(c), K3, TAU3 for every genome | PROVED (landed) | R117 (signs them for every genome, per R118 (k)'s text: «RESULTS R117's entry signs S3-START, PAD, K3 and TAU3 for every genome»); σ̄(K2) = r for every genome: R118 (P-N5-XICYC fixes) |
| C2 | ESC3, W3 for Ξ-cyclic genomes | was OPEN (R117 signs them for acyclic Ξ-graphs only; P-N5-XICYC §7 reads them for every genome, R118 signs REACH3-CYC CONDITIONAL on them) | now PROVED (lane, box 196 §2: ESC3-ALL, W3-ALL) |
| C3 | REACH3-CYC: N5′-xi from S3 on Γ3(G) visits only standard states, makes Howard steps at the movers (a run of HOW3(G)), first fallback at T3 + 1 | PROVED-CONDITIONAL (landed R118 (k)) on C1 + C2 | with C2: PROVED (lane, box 196 §2, Theorem REACH3-ALL) |
| C4 | F1, F3, F4′, DOM, STRICT on HOW3(G) | PROVED (landed R118 (l): «§4's proofs apply to the Howard run on Γ3», with R118 (b)-(c)) | re-checked in §3 (F6 on Γ3 = PAD (a)) |
| C5 | ENDGAME-3: one fallback at F, total F + 2 | PROVED (lane, P-N5-END, frozen 131b4c1c; L-RED 57 R222 SURVIVE; REFEREE 29 reviewing) | |
| C6 | END-T3: N5′-xi = T3 + 3 | PROVED-CONDITIONAL (lane, P-N5-END) on C3 | with C3 (box 196): PROVED (lane) |
| C7 | T3 ≤ (1 + Σ_v (D^tot_E(v) − 1))(L3 + 1) on HOW3(G) | was OPEN (P-N5-QUIET proves it on IDEAL-CYC = Γ(G) only; QT-L4) | now PROVED (lane, box 196 §3: CN2-3, LOC-GATE3, LOC-K2-3, QUIET3, T-QUIET3); route via T3 = T_CYC is DEAD (§6) |
| C8 | D^tot_E(v) ≤ (2M + 3)·F′_B(M) when every seq_t(v) has ≤ B ascents, on HOW3(G) | P-N5-ASC (R121, to land) proves it on IDEAL-CYC | PROVED (lane, box 196 §4: E-MON3, CHAIN-DECOMP3, HUB-ASC-G3; the abstract core CS(M) of P-N5-ASC §4 is game-free and used as is) |
| C9 | under [E-LEV], every seq_t(v) has ≤ U(G) ascents on HOW3(G) | P-N5-ASC UP-B on IDEAL-CYC | PROVED (lane, box 196 §4: UP-JUMP3, UP-B3) |
| C10 | [E-LEV] for the order Γ3 inherits from Γ(G) | HYPOTHESIS, or R104 (vi)'s packet §3.1 (docs/red/P-N5-REALIZE.md l. 88) by Lead reading 23:54Z (referees decide) | gamma3.py builds it (e-priorities by (lev, gate)) |
| C11 | Theorem CHAIN3 (target) | PROVED (lane, box 196) on C1-C10 | §5 |

Weakest links now: C5 / C7 / C8 / C9 are lane proofs (unrefereed; C8 and C7's Γ(G) versions are at the referees as P-N5-ASC and
P-N5-QUIET); C10 is a hypothesis unless the referees accept the Lead reading.

Independent map of the same chain: L-RED 58, docs/red/R223-q2.md §4 at claude/l-red 77b8946b (opened): its four links are C3 (its
link 1, «LINK OPEN for Ξ-cyclic genomes»), C7-C9 (its link 2, «READING, not proved»: QUIET / T-QUIET / P-QUIET on Γ3 with L recomputed
from n3 = N + 7M + 10), the run identity Γ3 = IDEAL-CYC (its link 3, «false as an identity of runs», 11 of 2,150 genomes; our §6) and
ENDGAME-3 (its link 4 = C5). This box writes links 1 and 2 out as proofs; credit L-RED 58 for the map. L-RED's item 5 (an adversarial
hunt for a Ξ-cyclic genome where ESC3 / W3 / R118 (k) fail on Γ3) runs in parallel and attacks §2.

## 2. ESC3 and W3 for every genome; REACH3-CYC without condition (PROVED, lane, box 196)
Setting: G any genome (Ξ-cycles and Ξ self-loops allowed); a mover state s; the standard state (σ, τ) of Γ3 for s (P-N5-REACH §3).
Used: [DEF] (R104) and Γ3's pads (R117); W-targets have level lev − 1 and level-0 e's go to c_W ([DEF]); TAU3, K3 (every genome, C1);
[1E-N3] (R57 (b) as landed in R104). The Ξ-targets enter only through the β-vertices, and the proofs below never follow a β → xt edge
except in W3 (i)'s one β step, which is followed by a W-descent. So no statement depends on the Ξ-graph.

**Lemma ESC3-ALL.** In every standard state: Iσ ∋ (K0, K1) (so Iσ ≠ ∅), and every pointwise optimum of S4a's arena H agrees with σ at
every Even vertex that is not a mover; moreover TIE(β_g) = {xt(g)} for every β_g with xt(g) a mover, and TIE(K0) = {pA} (so N5′-xi's
rule agrees with SPEC at these vertices).
Proof.
- (K0, K1) ∈ Iσ: K3 (b) (every genome).
- β_g with xt(g) a mover: A(β_g) ⊆ {xt(g), pb_g}, and σ(β_g) = xt(g) ∈ A(β_g). In H, Odd follows τ = pe at every gate (and K2 → K2).
  Every H-play from xt(g) is: a mover, one of its options in H (a pad m), the pad's gate, pe, e, then (level ≥ 1) a mover one level
  lower, …; the level drops by one at every e-step and nothing else is possible (the only Odd choices are τ's), so after at most
  lev(xt(g)) + 1 e-steps it reaches c_W's loop: node c_W, even, reward p′(c_W) > 0. Every H-play from pb_g → K0 stays in the core and
  ends in an odd cycle (node K1 or K2; K3 (d)). REWARD: W*-values via xt(g) beat those via pb_g. β_g is on no H-cycle (its only in-edge
  is from pβ_g, whose only in-edge is from a gate, which plays pe in H). So W*(β_g) = β_g ⊕ W*(xt(g)) ≠ β_g ⊕ W*(pb_g): every pointwise
  optimum picks xt(g), and TIE(β_g) = {xt(g)}.
- Core: K3 (d) (every genome): every pointwise optimum keeps pA at K0, and TIE(K0) = {pA} since K0 is on no H-cycle and the two H-values
  differ in their node (K2 vs K1).
- Pads, e, c_X, c_W, β_g with xt = X: one successor in H. ∎

**Lemma W3-ALL.** In every standard state, for every s:
- (i) W := the value of the (σ, τ)-play: W(x) = (c_W, ∅, 5ℓ + 5) for a mover x of level ℓ; W(m) = (c_W, ∅, 5ℓ + 4) for the pad of its
  chosen option, W(g) = (c_W, ∅, 5ℓ + 3), W(pe_g) = (c_W, ∅, 5ℓ + 2), W(e_g) = (c_W, ∅, 5ℓ + 1); W(β_g) = (c_W, ∅, 5·lev(xt(g)) + 6)
  when xt(g) is a mover.
- (ii) In H: W*(m_(x,k)) = (c_W, ∅, 5ℓ + 4) for EVERY option m_(x,k) ∈ A(x), and W*(x) = (c_W, ∅, 5ℓ + 5).
- (iii) Every mover x is not its own H-cycle node, and TIE(x) = A(x) = {σ(x)} ∪ Iσ(x).
Proof. (i) Under τ every gate takes pe. From a mover x of level ℓ: x → m → g → pe_g → e_g → (ℓ ≥ 1: the W-target, a mover of level
ℓ − 1; ℓ = 0: c_W). By induction on ℓ the play reaches c_W after 5ℓ + 5 steps through movers, pads, gates and e's, all less relevant than
c_W, so P = ∅. β_g → xt(g) adds one step. (ii) In H every play from a gate follows τ (pe), and every option of a mover in H is a pad to
its gate; so every H-play from m_(x,k) is the play of (i) for some choices at lower movers, and all have the same length 5ℓ + 4 and node
c_W, P = ∅ (lengths do not depend on the choices). (iii) x lies on no H-cycle (every H-play from x ends at c_W after descending levels),
and x ⊕ W*(y) = (c_W, ∅, 5ℓ + 5) = W*(x) for every y ∈ A(x). ∎

**Step check of the landed text (Lead 06:17Z: «quote their landed text by script and show each step uses no Ξ-edge»).** Tool
experiments/new/box196/quotes196.py (record; `git show` of trunk c8f42538f docs/new/P-N5-REACH.md §6.5-§6.6, verbatim, split into 16
steps; output quotes196.out; flags every step containing Ξ, xt(, X-chain, PLAY3, SBAR3, KEY3, Fact X, acycl, ACYC, «β_g →», «→ β»).
Every step not listed has no flag. The flagged steps, read by hand:
- ESC3.2 and W3.2 «IDEAL-ACYC).»: the labels only (the scope R117 signs), not a proof step.
- ESC3.3 «β_g with xt(g) a mover: its options in H are within {xt(g), pb_g}.»: xt(g) is named as β_g's successor (an edge of [DEF]); no
  property of the Ξ-graph is used.
- ESC3.4 «every H-play from xt(g) is mover → pad → gate → pe → e → … → c_W»: from xt(g) the H-play leaves every gate by pe (τ in H), so it
  never takes a β-face, hence no Ξ-edge; «β_g is on no cycle of H» needs only that β_g's one in-edge comes from pβ_g, entered only from a
  gate playing pe in H.
- W3.5 «W(β_g) = (c_W, ∅, 5·lev(xt(g)) + 6) when xt(g) is a mover»: one β → xt step, then the (σ, τ)-play of a mover, which by W3.4 takes
  pe at every gate (W-descent): one Ξ-edge, used once, whose target's level is all that matters; no cycle can form (levels then strictly
  decrease to c_W).
- No step cites PLAY3, SBAR3, KEY3 or Fact X (the acyclic-only lemmas). The three RESULTS labels are quoted by the same tool (OK × 3:
  R117 (e) «[IDEAL-ACYC; K3 and TAU3 every genome]»; R118 (k)'s «RESULTS R117's entry signs … ESC3, W3 for acyclic Ξ-graphs»; «P-N5-XICYC
  §7 reads ESC3's and W3's proofs for every genome»).

**Theorem REACH3-ALL (= R118 (k)'s REACH3-CYC without its condition).** For every genome G, the N5′-xi run from S3 on Γ3(G) visits only
standard states and makes Howard steps at the movers (a run of HOW3(G), tie rule: Ξσ-best, then SPEC's choice, then the larger index)
until its first fallback, at iteration T3 + 1, T3 := the first state at which no mover has a strictly better successor.
Proof. R118 (k)'s proof (P-N5-XICYC §7, quoted in §1's C3) with ESC3-ALL and W3-ALL in place of ESC3 and W3: state 0 is standard
(S3-START); in a standard state with some mover improvable, τ_new = τ (TAU3), σ_new = σ off the movers (ESC3-ALL, also for N5′-xi's rule),
and at a mover x N5′-xi takes the Ξσ-best element of TIE(x) = A(x) ∋ every strictly better successor (W3-ALL (iii)): a Howard step, and
some mover changes, so S4c does not fire and the next state is standard. At T3, A(x) = {σ(x)} at every mover, so σ_new = σ, τ_new = τ,
and Iσ ∋ (K0, K1): S4c fires. ∎
Remark. For N5 (SPEC's S4a) the same proof gives standard states but NOT Howard steps on Ξ-cyclic genomes: SPEC picks in TIE(x) by its
root-first key, not by Ξσ. DATA (§8): «nohoward» fires in spec mode. Nothing here is claimed for N5's pre-fallback run on Ξ-cyclic G.

## 3. QUIET on Γ3 directly (PROVED, lane, box 196)
Everything is on HOW3(G); Ω_t := Ξ_(σ_t) on Γ3 against Odd's optimal counterstrategy σ̄_t; class_t(v) := (Λ_t(v), E_t(v)), E_t(v) the
e-vertices of Π_t(v); Q, quiet windows, D^tot_E(v), B-class / E-class as in P-N5-QUIET §4. n3 = N + 7M + 10.
Facts on HOW3(G): F1, F3, F4′, DOM, STRICT (C4: R118 (l) applies P-N5-XICYC §3-§4 to the Howard run on Γ3; F6 there is PAD (a): every
cycle through a mover passes a gate and then a face pad and a face of Ω ≥ 6). [OPT]: σ̄_t is a pointwise optimum (R57 (b) / R21 (a),
as P-N5-QUIET §1).
**Lemma CN2-3.** For every positional pair of Γ3(G) and every vertex v ≠ c_X, the cycle node of v's play has Ω ≥ 3; no mover, gate or pad
is ever a cycle node or in a set Π.
Proof. PAD (a) (R117, every genome): every cycle contains a vertex of Ω ≥ 3, except c_X's loop (Ω 2), and c_X has no in-edge but its
loop. Movers (0), gates (1) and pads (≤ 2) rank below every vertex of Ω ≥ 3 (ranks order by Ω first), so they are never the most
relevant vertex of a cycle and never more relevant than a cycle node. ∎
**Lemma LOC-GATE3.** At every state t of HOW3(G) and gate g, with a := σ̄_t(g) ∈ {pe_g, pβ_g} and b the other face: Ω_t(a) ≠ Ω_t(b)
implies Ω_t(a) ◁ Ω_t(b).
Proof. P-N5-QUIET §3's proof word for word: it uses only [OPT], F3 and F4′ at g, «g is not a cycle node and in no Π» (CN2-3), and the
case analysis of the cycle C = {g} ∪ P closed by switching g, whose node is the most relevant vertex of C (it lies in P by CN2-3, so the
face pad, never a cycle node, changes nothing). ∎
**Lemma LOC-K2-3.** At every state σ̄_t(K2) = r, Ω_t(r) = (K1, ∅, 1) ◁ Ω_t(K2) = (K1, ∅, 2).
Proof. K1 → s → K1 is frozen (σ(K1) = s), so Ω(K1) = (K1, ∅, 0), Ω(s) = Ω(r) = (K1, ∅, 1). K2's loop gives node K2, reward −p′(K2) >
−p′(K1); [OPT] picks the smaller: r. Then Ω(K2) = (K1, ∅, 2), and with node K1 odd the longer is better for Even. ∎
**Lemma B-ONLY3 (P-N5-QUIET fixes entry 1, credit L-RED R221 §3, re-read on Γ3).** At every state t and every vertex v other than c_W,
the e-vertices whose successor is c_W, and the pads pe_g in front of them, Λ_t(v) is less relevant than every e-vertex.
Proof. τ_β := «pβ at every gate, r at K2». Under (σ_t, τ_β) no gate enters pe_g, and e_g's only in-edge is from pe_g, whose only in-edge
is from g: so a play from v (not one of the excluded vertices) meets no e-vertex except possibly at its start segment pe_g → e_g, and
reaches c_W only through a level-0 e. Its cycle contains no e-vertex and not c_W; not K0, K3 (F-E3); so its node is less relevant than
every e-vertex (E-DOM), with a smaller reward (every e is even). [OPT]: reward(Λ_t(v)) ≤ that reward. ∎
**Corollary NO-TIE3.** At every state and gate g, Ω_t(pe_g) ≠ Ω_t(pβ_g). Proof: as NO-TIE (P-N5-QUIET fixes entry 1) with pe_g, pβ_g in
place of e_g, β_g: if e_g → c_W the nodes differ (c_W vs B-ONLY3); else e_g ∈ Π(pe_g), and equality needs e_g ∈ Π(pβ_g), i.e. pβ_g's play
passes g, pe_g, e_g and then e_g's play, so k(pβ_g) > k(pe_g). ∎ So LOC-GATE3 decides every gate at every state, and (Q5)'s flips are
at most one per gate per sub-window chain (the tie step of P-N5-QUIET's G-1 never occurs).

**Facts (F-cls3), (F-E3).** As P-N5-QUIET §4: the order compares reward(Λ), then E (the top layer of Π below K0, K3), then the rest. Here:
every vertex more relevant than an e-vertex is an e-vertex, c_W, K0 or K3 (E-DOM, pads have Ω ≤ 2); c_W is never in Π (its only edge is
its loop); K0 → pA → K3 → K2 are frozen and the only edge into K3 is from pA, into pA from K0, into K0 from q (never on a play: K1 → s is
frozen) and from the pb's; so a play passes K0 iff it passes K3 iff its node is K1 or K2, and K0, K3 are never cycle nodes. Each class is
convex, and Q ≤ Σ_v (D^tot_E(v) − 1).
**Theorem QUIET3.** Every quiet window of HOW3(G) has at most L3 := (M + 1)(2M + 1)(N + 1) + N(n3 − 1) steps.
**Corollary T-QUIET3.** T3 ≤ (1 + Σ_v (D^tot_E(v) − 1))·(L3 + 1), the sum over the n3 vertices of Γ3(G).
Proof of QUIET3: P-N5-QUIET §4 (Q1)-(Q6) with these replacements, each checked:
- (Q1): LOC-GATE3 for the faces pe_g, pβ_g.
- (Q2): ext at x, at its pad m and at the gate changes neither Λ nor E (CN2-3).
- (Q3): k_t ∈ {0, …, n3 − 1}.
- (Q4): pβ_g → β_g → z (z = xt(g) or pb_g, frozen): class(pβ_g) = class(β_g) = class(z) (β_g ∉ Π(z): if z's play met β_g it would
  close a cycle through β_g, below its node). pe_g → e_g → y: e_g ∈ S and y in the B-class (w, S ∖ {e_g}). Boundary points: an e-face into
  a class (w, S ∖ {e}); the exit β → pb → K0 → pA → K3 → K2 → r → K1 → s → …, constant (core frozen, LOC-K2-3); or w itself.
- (Q5): the gate's e-face value is ext(pe, ext(e, Ω(y))), constant after a_(s−1); the β-face only rises (F1); LOC-GATE3 bounds the flips
  by two; Bellman-Ford along simple G_C-paths (≤ N movers; F3 at the pad, the gate, the face pad and the face, none in Π by CN2-3 and
  (Q4)); sub-windows as there.
- (Q6): STRICT; E-class movers change at most N(n3 − 1) times (Q3).
T-QUIET3: as T-QUIET. ∎

**Which lemmas carry over verbatim, which needed a re-proof (Lead 06:17Z (ii)).**
| lemma (Γ version) | Γ3 version | how |
| --- | --- | --- |
| F1, F3, F4′, DOM, STRICT (R118 (b)-(c)) | same | verbatim; R118 (l) applies them to the Howard run on Γ3; F6 on Γ3 = PAD (a) |
| CN2 | CN2-3 | RE-PROVED: pads (Ω ≤ 2) added to «never cycle node, never in Π»; c_X excepted (no in-edge but its loop) |
| LOC-GATE | LOC-GATE3 | verbatim (uses only [OPT], F3, F4′ and CN2's conclusion; faces are pe_g, pβ_g) |
| LOC-K2 | LOC-K2-3 | RE-PROVED: K1 → s → K1, σ̄(K2) = r (not K1), values shifted by the pads |
| B-ONLY, NO-TIE | B-ONLY3, NO-TIE3 | RE-PROVED: τ_β uses pβ and r; pe_g joins the excluded vertices; lengths via the pads |
| QUIET, T-QUIET | QUIET3, T-QUIET3 | re-read with the five listed substitutions (Q1)-(Q6); n → n3; boundary exit through pb, K0, pA, K3, K2, r, K1, s |
| E-MON | E-MON3 | re-read: K0 → pA → K3 is the frozen path (both or neither on a play) |
| CHAIN-DECOMP | CHAIN-DECOMP3 | verbatim (e_g → W-target is unpadded) |
| HUB-ASC-G (+ CS(M) §4) | HUB-ASC-G3 | verbatim; the 2M + 3 possible cycle nodes re-counted on HOW3 |
| UP-JUMP, UP-B | UP-JUMP3, UP-B3 | re-read: pads change no level; β → pb → K0 enters the closed core |

## 4. P-N5-ASC's game form on Γ3 (PROVED, lane, box 196)
seq_t(v), E_t(v), ascents, U(G), F′_B, CS(M) as in P-N5-ASC (R121 when landed).
- **E-MON3.** If Λ_t(v) = Λ_(t+1)(v) then E_t(v) ≤ E_(t+1)(v). Proof: P-N5-ASC §3 with (F-E3)'s facts: c_W, K0, K3 never in the symmetric
  difference (K0 and K3 both or neither, by (F-E3)); pads never in Π (CN2-3); so a top differing element, if it is in E, is an even
  e-vertex in the later set. ∎
- **CHAIN-DECOMP3.** If seq_t(v) = (f, …), f's successor y_f is a mover with Λ_t(y_f) = Λ_t(v) and E_t(v) = {f} ∪ E_t(y_f). Proof:
  P-N5-ASC §3 word for word (e_g has one edge, to its W-target or c_W; Γ3 adds no pad there). ∎
- **HUB-ASC-G3.** On every interval I with Λ_t(v) = w: D_E,I(v) ≤ F′_B(M_w) if every seq_t(v) has ≤ B ascents; whole run: Λ_t(v) takes
  ≤ 2M + 3 values (possible cycle nodes on HOW3: the M e's, the M β's, c_W, K1, K2; R118 (e)'s reason, C4), so D^tot_E(v) ≤
  (2M + 3)·F′_B(M). Proof: P-N5-ASC §5 (items, forests by CHAIN-DECOMP3, lex-monotone by E-MON3, §4's abstract core unchanged). ∎
- **UP-JUMP3 (under [E-LEV]).** An ascent a → b of seq_t(v) needs, between a and b on the play, a β-vertex whose Ξ-target is a mover of
  strictly higher level than the mover it was entered from. Proof: P-N5-ASC §6: levels change only at e-steps (down by one; pe and the
  W-edge) and at Ξ-steps (β → xt); a β → pb step enters the closed core and never reaches b; pads change no level. ∎
- **UP-B3 (under [E-LEV]).** Every seq_t(v) has at most U(G) ascents, so D^tot_E(v) ≤ (2M + 3)·F′_(U(G))(M). ∎

## 5. Theorem CHAIN3 (PROVED, lane, box 196; on the premises of §1)
Under [E-LEV], for every genome G, N5′-xi from S3 on Γ3(G) makes at most
  T3 + 3 ≤ (1 + n3·((2M + 3)·F′_(U(G))(M) − 1))·(L3 + 1) + 3
iterations (n3 = N + 7M + 10, L3 = (M + 1)(2M + 1)(N + 1) + N(n3 − 1), F′ of P-N5-ASC §5). For U(G) ≤ B, B fixed, this is a polynomial
in N + M of degree O(5·2^B) in M; as Γ3(G)'s size is polynomial in N + M at bit cost (R117 §3), the iteration count is polynomial in the
input size of Γ3(G). Each iteration is polynomial at bit cost (SPEC S1-S4 are one-player VJ evaluations; R117 / SPEC).
Proof. REACH3-ALL (§2): the run up to its first fallback is a run of HOW3(G) of length T3, and the first fallback is at T3 + 1;
ENDGAME-3 (P-N5-END): total = (T3 + 1) + 2. T-QUIET3 (§3) with UP-B3 / HUB-ASC-G3 (§4) bounds T3. ∎
Premises not landed: P-N5-END (ENDGAME-3; REFEREE 29), P-N5-ASC (R121; §4 uses its abstract core and its proofs' structure), P-N5-QUIET
(§3 uses its proofs' structure); [E-LEV] (C10).

## 6. DEAD: RUN-TRANSFER (T3 = T_CYC, or equal mover sequences)
The route «T3 equals the IDEAL-CYC count T_CYC on Γ(G), so P-N5-QUIET's bound transfers» is DEAD: the Γ3 run and the Γ run differ.
Instance: RT_n1 (box196/inst/RT_n1.json, sha1 829f3c97…; N 1, one mover of level 0 with three options, all Ξ self-loops, start option
0; eg195.gen «noesc» seed 2, 5th genome): N5′-xi from S3 on Γ3 has T3 = 1 (state 0 → option 2, then no mover improves), box191
idealcyc on Γ(G) has T_CYC = 2 (0 → 1 → 2). Obstruction: at state 0 options 1 and 2 are EXACTLY tied in both games (Γ: key (−19, 0, 4)
for both; Γ3: (−51, 0, 8) for both), and the tie rules differ (idealcyc: keep, then larger vertex index; N5′-xi: Ξσ-best, then SPEC's
root-first key, then larger index). R118 (a) allows any tie rule, so T_CYC is not one number; QUIET3 holds for every tie rule. DATA: tdiff / seqdiff in §8. §3 avoids the transfer.

## 7. What CHAIN3 gives and does NOT give (against TARGET.md)
- Gives: a polynomial bound on N5′-xi's iteration count on ONE restricted family of games, {Γ3(G) : G a genome with U(G) ≤ B} under
  [E-LEV], from S3. Ξ-cycles are allowed (new beyond R117 / R118's acyclic results).
- Does NOT give: anything for N5 (SPEC S4a; its pre-fallback run is not Howard on Ξ-cyclic genomes, §2 Remark); anything for genomes with
  U(G) unbounded (the open core Σ_v D^tot_E(v), equivalently P-N5-ASC with unboundedly many ascents, stays OPEN; L-SI / L-RED counters
  use unbounded-ascent doubling hubs); anything on games other than Γ3(G); anything on general parity games. N5′-xi stays a CANDIDATE
  (D1). TARGET.md §2 (M4) asks for an algorithm polynomial on EVERY parity game; §4: a bound on a restricted class is not M4. Not M3, not
  M4, not a step-4 pass. G-N5-TIME stays OPEN.

## 8. DATA (tool experiments/new/box196/qt3_196.py, run by check196.sh; output check196.out; record runs data/)
Unit: runs of N5′-xi (default) or N5 (Q196_MODE spec) from S3 on Γ3(G) (box189 gamma3.build, all pads; box190 n5v.step), observed on
states 0, …, T3 (up to the first fallback). Scope: Γ3(G) as built by gamma3.py (pinned), whose e-priorities are ordered by (lev, gate),
so [E-LEV] holds on every instance. Families: box195 eg195.gen (rand, esc, noesc, deep, dense, lvl0, late, acyc; L-RED R221 §11's
generator, transcribed there with credit). Record sweep: data/sweep196.out (8 families × 500 × seeds 1961, 1962 = 8,000 runs, plus
controls, spec runs and every pinned genome of box189/corpus, box191-box195/inst and RT_n1: 58 genomes).
- REACH3-ALL: nonstd 0 (unit: states), nohoward 0 (unit: (state, mover) pairs) on the 8,000 runs and the 58 genomes.
- CN2-3: cnlow 0 (unit: (state, vertex) pairs). LOC-GATE3: locfail 0, NO-TIE3: ties 0 (unit: (state, gate) pairs). B-ONLY3: bonly 0
  (unit: (state, vertex) pairs). LOC-K2-3: k2fail 0 (unit: states).
- QUIET3: wfail 0 (unit: quiet windows), crossflip 0 (unit: σ̄ flips); longest quiet window W ≤ 32 (RS2_L32M6, N 77); T-QUIET3: Tfail 0
  (unit: runs). E-MON3: emon 0 (unit: (step, vertex) pairs). UP-B3: upfail 0 (unit: (state, vertex) pairs; ascents > U(G)); max ascents
  4 (deep, seed 1962).
- Controls (fire): ctrl1 (L3 := 0, U(G) := −1): wfail 32, Tfail 22, upfail 26,477 in 50 runs; ctrl2 (order reversed): locfail 3,320;
  ctrl3 (no excluded vertex in B-ONLY3): bonly 2,269. Spec mode (N5): nohoward 599 (rand, 200 runs) and 911 (dense, 200 runs): N5's
  pre-fallback run is NOT Howard on Ξ-cyclic genomes (§2 Remark); every other counter 0 there.
- No control: nonstd, cnlow, k2fail, crossflip, emon (counters that the proofs predict 0 and no simple perturbation of this tool makes
  fire without changing the game; stated, not hidden).
- Record (RUN-TRANSFER, §6): tdiff (runs with T3 ≠ T_CYC) 100 of 8,000 xi runs, seqdiff 1,013; spec mode tdiff 138 / 200 (rand) and
  146 / 200 (dense). Large pinned instances: LEAP_k64 T3 = 129, RS2_L32M6 T3 = 41, rd2_d10 T3 = 26, all far below the bound.
- check196.sh (re-run by check.sh, block «BOX 196 CHAIN»): 8 families × 100 (seed 1964), the three controls, spec on 100 runs, and five
  pinned genomes (RT_n1, LEAP_k64, RS2_L32M6, rd3_d4, cyc_d8); output check196.out.

## 9. D18 note (READING, not a claim)
The direct route did not stall, so no outside tool was needed for (b): the decisive move was to stop comparing two runs (the «tie
transfer») and to prove the counting lemmas on the run that is actually executed. The order-theoretic content is P-N5-QUIET's: classes
are convex blocks of a total preorder that every vertex climbs monotonically (F1), so a run is a walk in a product of chains with
bounded-length plateaus (QUIET3); the open core is the HEIGHT of that product along the run (Σ_v D^tot_E(v)), which [E-LEV] + bounded
U(G) controls through P-N5-ASC's chain systems.

## Addendum 1 (L-NEW successor 64, 07:12Z by date -u): L-RED 58 R223 item 5, and F1 / DOM / STRICT on the Γ3 run without R118 (b)
- L-RED 58, docs/red/R223-reach.md at claude/l-red 71133de5 (opened): «Verdict: SURVIVES (no Ξ-cyclic counterexample)» for ESC3, W3 and
  R118 (k) with N5′-xi from S3 (its counters, cited, not re-run: 43,816 exhaustive N ≤ 2 Ξ-cyclic genomes, 5,000 random N 3-4 and 2,000
  N 5-6, every fail counter 0; its control MODE=spec fires; its own Γ3 builder equals box189's gamma3 on all N ≤ 2 genomes). Its reading
  agrees with §2: ESC3's and W3's proofs follow pe-plays and W-edges only. Its §3 transfer checklist for QUIET on Γ3 is the table at the
  end of §3 here; one item differs and is taken below.
- F1, DOM and STRICT on HOW3(G), proved without R118 (b) (R223-reach §3: «F1 and STRICT: from R15 (a) and «movers are never cycle
  nodes» (PAD (b)), instead of R118 (b)»). Replaces C4's citation of R118 (l) for these three facts; the rest of C4 (F3, F4′) is [VJ]'s
  value definition with [OPT], game-free.
  - F1. A Howard step switches exactly the movers whose new successor is strictly better (ties keep the current one), one switch per
    vertex: a non-empty unambiguous set I of improvements of σ_t (VJ00 §4.4). RESULTS R15 (a) («for any non-empty unambiguous set I of
    improvements of σ (VJ00 §4.4), Ωσ ⊴ Ω_{Switch_I(σ)}») gives Ω_t ⊴ Ω_(t+1) pointwise. R15's Object is SPEC on any game with SPEC's
    injective ranks, so Γ3's repeated pad priorities are covered (R223-end §1).
  - F6 on Γ3: no mover is the cycle node of its own play (CN2-3: movers have Ω 0, every cycle through a mover passes a gate, a face pad
    and a face of Ω ≥ 6). So F3 applies at every mover: Ω_t(x) = ext(x, Ω_t(σ_t(x))).
  - F5 (Howard on Γ3): σ_(t+1)(x) is ⊴-best among x's successors under Ω_t, and strictly better than σ_t(x) when it differs (REACH3-ALL:
    N5′-xi takes the Ξσ-best element of A(x) ∋ every strictly better successor; ties keep σ_t(x) since A(x) = {σ_t(x)} when nothing is
    strictly better).
  - DOM and STRICT: P-N5-XICYC §4's two-line proofs from F1, F3, F4, F5, F6, with these Γ3 versions; nothing else is used.
- Lead 07:04Z / R223-reach §3's other «re-prove» items, each already in §2-§4: the frozen core and the β-successors in (F-E) ((F-E3),
  standard states by REACH3-ALL); LOC-K2 (LOC-K2-3); Q4 (R117 K3 + the standard-state invariant = REACH3-ALL / ESC3-ALL); L with n3 in
  Q3 / Q6 (QUIET3). No statement of §1-§5 changes.
