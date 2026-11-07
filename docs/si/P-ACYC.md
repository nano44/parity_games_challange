# Packet P-ACYC (box 81): on Ξ-acyclic genomes Odd never leaves the β-face, so Howard and N5′-xi's mover phase take at most N steps
L-SI successor 43 (Opus 5.5), D18 / D14 / D1; Lead brief 2026-11-07 22:35Z («Freeze a short packet P-ACYC»). Written 2026-11-07 from
22:33Z (date -u: see the commits). Source note: docs/si/box81-bridge.md §3 (history only). This packet carries every proof in full and
is checked against this text only. Labels: PROVED (L-SI 43, unrefereed) / PROVED-CONDITIONAL (on named landed premises) / DATA /
READING (not to sign). Not a TARGET.md claim; not M3; not a gauntlet step; G-N5-TIME stays OPEN.

Scope (one sentence). On every Ξ-acyclic genome, which is the whole domain of the tower route (R104, R117), Odd's optimal
counterstrategy takes the β-face at every gate. So IDEAL-CYC Howard has C = R = 0 and at most N steps, and (conditionally on R118's
REACH3-CYC, whose premises R117 signs for acyclic Ξ-graphs) N5′-xi's first fallback on Γ3(G) from S3 comes at iteration ≤ N + 1. N5
with SPEC's S4a tie rule, by contrast, realises R104's L(G) on the same games from the same start (R117). Hence a super-polynomial
tower family would bear on N5 only, and N5′-xi lower bounds need Ξ-cyclic genomes.

## To sign, and what is not to sign
| § | statement | label | premises |
| --- | --- | --- | --- |
| §2 | Lemma BETA-ACYC (on Γ(G) and on Γ3(G)) | PROVED | R104 definitions of the genome, Ξ-graph, Γ(G), its start; R117 definition of Γ3(G); R118 [VJ] order and σ̄ |
| §2 | Lemma LAMBDA-CONST | PROVED | the same, and BETA-ACYC |
| §3 | Theorem ACYC-LIN | PROVED | BETA-ACYC, LAMBDA-CONST, R118 (a) definitions, R118 (d) BR-SEG |
| §4 | Corollary ACYC-XI | PROVED-CONDITIONAL on R118 (k) REACH3-CYC with (l) Corollary T3 | BETA-ACYC, LAMBDA-CONST on Γ3 |
| §5-§6 | first-fallback definition, scope, DATA, TARGET diff | definitions / DATA / READING (not to sign) | |

## 0. Premises (quoted; every quote is checked verbatim by experiments/si/box81/quotes81.py against trunk docs/RESULTS.md and docs/new/N5-ssi-global.md)
- R104 (definitions only; no theorem of R104 is used):
  - genome: «an IDEAL genome G has N movers x with levels lev(x), M := Σ deg(x) options (x, k), each with a W-target of level lev(x) − 1
    (none at level 0), a Ξ-target xt(x, k), a mover or the exit X, a distinct β-rank with a parity, a distinct gate index, and a start»;
  - Ξ-graph: «the Ξ-graph has an edge x → xt(x, k) for every option with a mover as Ξ-target»;
  - game: «the game Γ(G) on n = N + 3M + 6 vertices (Even movers of priority 0; Odd gates of priority 1 with a W-face e and a Ξ-face β; β
    of priority 6 + 2·rank + parity with edges to the Ξ-target and to u, or to u alone; e of even priority above every β with one edge to
    the W-target or to the top even self-loop c_W; an unused even self-loop of priority 2; c_W's priority top is the least even number at
    least 2 above every other priority so far; a closed core u = K0 (Even, top + 2) → {K1, K3}, K1 (Even, 5) → {K0, K1}, K2 (Odd, 3) →
    {K1, K2}, K3 (Even, top + 3) → {K1, K2}»;
  - start: «with start σ = the genome start at movers, β → its Ξ-target (u when the target is X), K0 → K3, K1 → K1, K3 → K2, τ = e at
    every gate and K2 → K2».
- R117 (definition only): «the game Γ3(G) obtained from Γ(G) by 4M + 4 single-successor Even pads of priority ≤ 2 (pA on K0 → K3, s on
  K1's loop, q on K1 → K0, r on K2 → K1, pe_g and pβ_g on both faces of every gate g, pb_g on every β_g → u, and m_(x,k) on every mover
  edge x → (x, k) with priority 2 for the genome start and 0 otherwise, appended after Γ(G)'s vertices; n = N + 7M + 10)».
- R118:
  - values: «VJ00 §4.2 / Friedmann arXiv 1106.0778 §3 for the order ⊴ on values (Λ, Π, k)»; «σ̄ is Odd's optimal counterstrategy, chosen
    by a fixed deterministic rule»;
  - (a) IDEAL-CYC(G): «The game is Γ(G) with every Even vertex that is not a mover frozen at its start successor. Odd is unrestricted
    (gates and K2).»; Howard step: «every mover x goes to a successor of ⊴-largest Ω_t value, and keeps σ_t(x) if σ_t(x) is such a
    successor»; «T_CYC := the number of steps to the first state where no mover has a strictly better successor»; labels «C if Λ_t(v) ≠
    Λ_(t+1)(v) for some vertex v;», «else R if σ̄_t(v) ≠ σ̄_(t+1)(v) for some Odd vertex v;», else p;
  - (d) BR-SEG: «If Λ and σ̄ are constant on the states a, a+1, …, a+j+1 and the step a+j → a+j+1 changes σ, then j ≤ N − 1. Hence every
    maximal run of consecutive p-steps has at most N steps.»;
  - (j) N5′-xi is «an N5′-xi run (box 190's S4a tie rule by Ξσ)»;
  - (k) REACH3-CYC: «The N5′-xi run of Γ3(G) from S3 has the following form:» states 0, …, T3 standard, the mover parts a Howard run on
    Γ3(G); «T3 is the first state at which no mover has a strictly better successor in Γ3;»; «transition T3 + 1 is an S4c fallback.»; its
    premises [REACH-L], «which RESULTS R117 (P-N5-REACH) signs in its entry (S3-START, PAD, K3, TAU3 for every genome; ESC3, W3 for
    IDEAL-ACYC) and states in its line only for acyclic Ξ-graphs (S3-START, PAD)», plus Lemma K2-r and [1E-N3] as listed there;
  - (l) Corollary T3: «§4 applies on Γ3 (movers priority 0, pads never cycle nodes by PAD (b), non-mover Even vertices frozen in standard
    states, Odd = gates and K2)», so «T3 ≤ C + R + (C + R + 1)·N, with C ≤ n3·(2M + 2) and n3 = N + 7M + 10;» and «the first fallback of
    N5′-xi on Γ3(G) comes at iteration T3 + 1.»;
  - scope: «no bound on R is claimed (OPEN), so nothing about N5′-xi's or N5's running time follows».
- SPEC (RESULTS R15's object: «N5 "SSI-GLOBAL" as specified in docs/new/N5-ssi-global.md»): «S4 Iteration (one iteration = one pass with
  Iσ ∪ Iτ ≠ ∅; both steps computed from the SAME (σ, τ), applied together):» and «c. FALLBACK, if σ_new = σ and τ_new = τ: if Iσ ≠ ∅, for
  every Even v with an improving edge set σ_new(v) = the w with (v, w) ∈ Iσ maximising (Ξσ(w), w) (best valuation, ties: larger index);
  otherwise do the same for Odd on Iτ with G^d's valuations. Count it.»
- Not used: every theorem of R104 and R117; R118 (b), (c), (e)-(j) except the definitions quoted; every lane note.

## 1. Definitions and facts read off §0
- Ξ-ACYCLIC: the Ξ-graph has no directed cycle.
- FROZEN FRAME. H is Γ(G) or Γ3(G). σ is an Even strategy of H that agrees with the stated start at every Even vertex other than the
  movers. On Γ3 that start is transported through the pads: each pad has one successor; K0 → pA → K3, K1 → s → K1, K3 → K2,
  β_g → its Ξ-target or pb_g → u.
  - On Γ(G) this is IDEAL-CYC's frozen part (R118 (a)). On Γ3(G) it is the standard states' non-mover part (R118 (l): «non-mover Even
    vertices frozen in standard states»).
  - Odd (the gates and K2) is free.
- Notation. Ω_τ(v) is the value of the (σ, τ)-play from v. σ̄ is an optimal counterstrategy: Ω_σ̄(v) ⊴ Ω_τ(v) for every Odd strategy τ and
  every v (R118 [VJ]: the order of VJ00 §4.2, Friedmann §3). Relevance is by priority. A larger reward for Even means an even cycle node
  of higher priority, or an odd one of lower priority. Among sets, the most relevant vertex of the symmetric difference decides: if it is
  even, the set containing it is better for Even.
- Facts from §0 (the K-core is the same on Γ and Γ3 up to pads):
  - [RANK] The e-vertices have even priorities above every β. Only c_W (top, even), K0 (top + 2, even) and K3 (top + 3, odd) lie above
    them. K1 (5) and K2 (3) are odd and below every β (6 + 2·rank + parity ≥ 6). Gates (1), movers (0), the unused loop (2) and all pads
    (≤ 2) lie below K2.
  - [CORE] In the frozen frame the only edge into {K0, K1, K2, K3} from outside is into u = K0: β → u, or β → pb_g → u on Γ3. Inside,
    K0 → K3 → K2 (via pA on Γ3); K2 chooses K1 (via r on Γ3) or its own loop; K1 loops (via s on Γ3).
  - [cX] The unused loop has no in-edge.
- FIRST FALLBACK (definition). Iteration k (k ≥ 1) of a run is the k-th pass of SPEC S4, the transition from state k − 1 to state k. It
  is a FALLBACK iff S4c applies in it: σ_new = σ and τ_new = τ after S4a and S4b. The FIRST FALLBACK is the least such k.
  - For N5′-xi (S4a's tie rule by Ξσ, R118 (j)), R118 (k) and (l) place it at k = T3 + 1.

## 2. Lemma BETA-ACYC and Lemma LAMBDA-CONST (PROVED)
**Lemma BETA-ACYC.** Let G be Ξ-acyclic, H ∈ {Γ(G), Γ3(G)}, σ an Even strategy in the frozen frame, and σ̄ any optimal counterstrategy
to σ. Then σ̄ chooses the β-face at every gate g: β_g on Γ(G), pβ_g on Γ3(G). Under (σ, σ̄), no play from a vertex other than an
e-vertex (or a pad pe_g) contains an e-vertex.
Proof.
- Let τ′ := σ̄ changed to the β-face at every gate (σ̄(K2) kept).
- (1) The play from a gate g under (σ, τ′):
  - it runs g → (pβ_g →) β_g → x′ := xt(g) → (m-pad →) the gate of σ(x′) → its β-face → … ;
  - each passage from a β to a mover follows an edge of the Ξ-graph, so the movers on the play are distinct, because the Ξ-graph is
    acyclic;
  - so the play reaches a β whose Ξ-target is X, then u, and by [CORE] runs K0 → K3 → K2 → σ̄(K2) and ends in the K1 loop or the K2
    loop.
  - Its cycle node is w* := K1 if σ̄(K2) leads to K1, else K2. Its prefix contains K0 and K3 (both above w*), no e-vertex, and not c_W.
- (2) Suppose σ̄(g) is the e-face, and let π be the (σ, σ̄)-play from g with cycle node w. Which cycles can π end in?
  - c_W's loop.
  - The K1 or K2 loop.
  - A cycle through movers, gates, β's, e's and pads. (The unused loop is never entered, [cX].)
- (3) A cycle with no e-vertex and no K-vertex alternates mover → gate → β → mover, with single-successor pads in between. It uses one
  Ξ-edge per β, so it would be a cycle of the Ξ-graph: impossible.
- (4) A cycle through an e-vertex has an e-vertex or c_W as its most relevant vertex, which is even. The same holds if w = c_W.
  - An even cycle node beats the odd w* [RANK]. So Ω_σ̄(g) ▷ Ω_τ′(g), against optimality.
- (5) So w ∈ {K1, K2}. By [CORE], π enters the core at u and runs K0 → K3 → K2 → σ̄(K2), so w = w*.
  - Both plays contain K0 and K3; neither contains c_W (it occurs only as a cycle node); pads and gates are below w*, so they are in
    neither Π.
  - π contains e_g, which is above w*. The τ′-play contains no e-vertex.
  - So by [RANK] the most relevant vertex of the symmetric difference of the two Π-sets is an e-vertex of π, which is even. Hence
    Ω_σ̄(g) ▷ Ω_τ′(g), against optimality.
- So σ̄ takes the β-face at every gate, and every play from a non-e vertex is as in (1). It never passes an e-face, so it contains no
  e-vertex. ∎

**Lemma LAMBDA-CONST.** Under the hypotheses of BETA-ACYC, Λ(v) does not depend on σ. It is:
- c_W for c_W and for the e-vertices of level-0 options (and their pe pads);
- the unused loop for itself;
- w* for every other vertex.

w* does not depend on σ.
Proof.
- An e-vertex of a level-ℓ option with ℓ ≥ 1 goes to a mover, whose play is as in (1). Every other non-K vertex is as in (1) too. The
  K-vertices reach w* inside the core.
- w*: the two plays from K2 lie inside the closed core, which does not depend on σ. So Odd's optimal choice at K2 does not depend on σ.
  Under a fixed deterministic rule it is the same in every state. ∎

## 3. Theorem ACYC-LIN (PROVED)
For every Ξ-acyclic genome G and every start mover state, the Howard run of IDEAL-CYC(G) has C = 0 and R = 0, and T_CYC ≤ N.
Proof.
- No step changes a cycle node (LAMBDA-CONST), so C = 0.
- At every state σ̄ takes the β-face at every gate (BETA-ACYC), and at K2 the same choice (LAMBDA-CONST's proof). So σ̄ never changes
  and R = 0.
- So every step is a p-step and the whole run is one maximal p-run. By R118 (d) BR-SEG it has at most N steps: T_CYC ≤ N. ∎
- The bound is attained: T_CYC = N on some genomes of §6's set A (max T/N = 1.0).

## 4. Corollary ACYC-XI (PROVED-CONDITIONAL on R118 (k) REACH3-CYC and (l) Corollary T3)
For every Ξ-acyclic genome G, the first fallback of N5′-xi on Γ3(G) from S3 comes at iteration T3 + 1 ≤ N + 1. The mover phase
(states 0, …, T3) has at most N iterations.
Proof.
- By (k), states 0, …, T3 are standard and the mover parts are a Howard run on Γ3(G). So every state is in the frozen frame on Γ3(G).
- BETA-ACYC and LAMBDA-CONST hold there (§2, H = Γ3(G)). So the C and R of that run, the counts in (l)'s bound, are 0.
- (l) gives T3 ≤ C + R + (C + R + 1)·N = N, and the first fallback at iteration T3 + 1. ∎
- The condition. (k) is PROVED-CONDITIONAL on [REACH-L]. Its lemmas are signed in R117's entry: S3-START, PAD, K3, TAU3 for every
  genome; ESC3, W3 for IDEAL-ACYC, which is this case. Lemma K2-r and [1E-N3] are as listed in (k).
- Not claimed:
  - the number of iterations after the first fallback (DATA: 2 more on every genome of §6, but no bound);
  - the correctness of the output (SPEC S5, R15).

## 5. What this says about N5 (S4a) and N5′-xi (READING, not to sign)
- N5 with SPEC's S4a tie rule: on Ξ-acyclic genomes from S3 on Γ3(G), its FL run has length exactly L(G) (R117: «the N5 run of Γ3(G)
  FROM S3 has states 0, …, L(G) equal to the transported REALIZE states of the IDEAL run»).
- N5′-xi: on the same games from the same start, its mover phase has at most N iterations (§4).
- The two algorithms differ only in S4a's tie rule (R118 (j)). Under §2 Odd's choice is frozen, so the tower quantity L(G) measures
  N5's root-first-key tie rule only.
- A family of towers with L super-polynomial in N + M would therefore bear on N5 (R117's Corollary REAL-IDEAL-S3), not on N5′-xi.
- For N5′-xi to be slow, R must grow (R118 (l)'s equivalence), and R = 0 on every Ξ-acyclic genome. So a candidate counter for
  N5′-xi must have a Ξ-cycle.

## 6. DATA, clause by clause (not to sign)
Tools: experiments/si/box81/ (lemma81.py on IDEAL-CYC; pacyc81.py on Γ3 with the real N5′-xi; quotes81.py for §0). Runners are byte
copies of claude/l-new 9cdb7209 (ref/, pins ref.sha1). Frozen outputs in out/. All are re-run and diffed by box81/check81.sh, which
experiments/si/check.sh runs.
- Sets:
  - A: 300 Ξ-acyclic random genomes, generator lemma81.agen (the rand191 shape: d 1-6, w 1-3, degree 2-3; Ξ-targets only to earlier
    movers in a random order, or X), seed 7.
  - B: the four tower genomes H5_d20_F62, H6_d24_F126, SL41_d28, L6Z_KILL238_d28 (inst/, pins inst.sha1).
  - CONTROL: five Ξ-cyclic genomes rd2_d3, rd2_d4, rd3_d3, rf_d4, RS2.
  - Scope: the stored start (IDEAL-CYC) or S3 (Γ3).
- BETA-ACYC:
  - Unit: (state, gate) pairs with σ̄ off the β-face, and pairs where the β-face is not strictly ⊴-better for Odd.
  - IDEAL-CYC (lemma81.py), on states of the Howard run: A 0 and 0 (768 states); B 0 and 0 (44 states).
  - Γ3 (pacyc81.py), on states 0, …, T3 of N5′-xi, σ̄ off the β-face (pβ_g) only: A 0 (768 states); B 0 (44 states).
  - CONTROL: 121 (both models; 59 states).
- LAMBDA-CONST:
  - Unit: steps with a cycle-node change (C).
  - A 0, B 0 (both models); CONTROL 15.
- ACYC-LIN:
  - Unit: runs with T_CYC > N; steps with an R label.
  - A 0, 0; B 0, 0. Max T_CYC/N 1.0 on A, 0.25 on B. CONTROL: 4 of 5 runs have T_CYC > N, R 25.
- ACYC-XI:
  - Unit: genomes whose first fallback k1 has k1 − 1 > N; genomes with no fallback; states 0, …, k1 − 1 that are non-standard.
  - A 0, 0, 0; B 0, 0, 0. On B, k1 = 10, 13, 11, 10 for N = 40, 48, 56, 56.
  - The Γ3 mover phase equals the IDEAL-CYC Howard run state for state on all 12 instances of docs/si/box81-bridge.md §2 (real81.py).
- First-fallback definition, scope, §5: no separate DATA.
- §0 quotes: 28 of 28 verbatim (quotes81.py).
- Cross-check of the model: an implementation sharing no code with the runners (xchk81.py: own Γ(G), own Odd policy iteration, own
  Howard) gives identical games, states, values and labels on 10 of 10 instances, including H5, H6 and L6Z_KILL238.

## 7. Diff against TARGET.md (not to sign)
- TARGET.md §2 asks for an algorithm that is polynomial on EVERY parity game and outputs (W_E, W_O).
- Every statement here is about the step sequence of Howard on IDEAL-CYC(G) or of N5′-xi's mover phase on Γ3(G), for the restricted
  class of Ξ-acyclic genome games. TARGET.md §4: «Polynomial only on a restricted class … » does not count as M4.
- No statement bounds N5′-xi's total iterations (the part after the first fallback is not bounded), its bit cost (§3), or its output.
- None is an M3 or M4 claim or a gauntlet step (§5). G-N5-TIME stays OPEN; N5′-xi stays a CANDIDATE (D1).
