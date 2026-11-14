# Packet P-N5-XICYC (box 191): N5′-xi on Ξ-cyclic genomes is Howard strategy improvement; it is polynomially bounded except for the number R of changes of Odd's best response (BR-SEG, CYC-COUNT, ONEP-POLY), plus a reduction for general games (RED-XI)
L-NEW successor 59 (Opus 5.5), D1 / D14 / D18. Lead 2026-11-07 05:51Z, decision 3, quoted: «Referee packet P-N5-XICYC: after the proof of (iii), or once you are close to ~500k context, whichever comes first. Include REALIZE-CYC only if (iii) is proved; otherwise include BR-SEG, CYC-COUNT, ONEP-POLY, RED-XI and the DEAD items.»
Status of (iii): proved in lane as REACH3-CYC (§7). It is CONDITIONAL on P-N5-REACH's lemmas, which have not landed.
Written 2026-11-07 from 06:40Z (date -u; see the commit). FROZEN at push. Later text goes to docs/new/P-N5-XICYC-fixes.md, which is append-only.
Source, history only: docs/new/N5-XICYC-box191.md (f09f67ec + addendum d6472691). This packet carries every proof in full.
Labels: PROVED (L-NEW 59, unrefereed) / PROVED-CONDITIONAL (on a named premise that has not landed) / DEAD (instance, machine-checked) / DATA / READING (not to sign).
This packet is NOT a TARGET.md claim. It does NOT decide G-N5-TIME. It is NOT M3 and not a step-4 pass. N5′-xi stays a CANDIDATE.
The packet bounds iterations only in terms of R. It does not bound R.

## To sign, and what is not to sign
| § | statement | label | hypotheses |
| --- | --- | --- | --- |
| §2 | definitions: IDEAL-CYC(G); Howard step; step labels C / R / p | definitions | every genome G |
| §3 | Facts F1-F6 | F1, F2 from premises; F3-F6 PROVED | as stated |
| §4 | Lemmas DOM, STRICT, PATH; Theorem BR-SEG; Lemma CYC-COUNT; Theorem T-CYC; Corollary ONEP-POLY; Lemma LEVEL0 | PROVED | every genome |
| §5 | Theorem BR-SEG-G (Howard on any game) | PROVED | hypothesis H0 |
| §6 | Lemma DECOMP-G; Theorem RED-XI | PROVED (reduction only) | X0, X1 |
| §7 | Theorem REACH3-CYC; Corollary T3 | PROVED-CONDITIONAL on [REACH-L] | every genome |
| §8 | DEAD SEG-2P; DEAD ODD-FIXED | DEAD | instances pinned |
| §9-§12 | data, machine checks, TARGET diff, limits | DATA / READING (not to sign) | |

## 1. Premises
Landed premises are from trunk claude/vibrant-johnson-nxvvxo f7fcfccd, docs/RESULTS.md, with line numbers. Sources are named.
- [R15a] RESULTS R15 (a) (l. 631), «Lemma A: for any non-empty unambiguous set I of improvements of σ (VJ00 §4.4), Ωσ ⊴ Ω_{Switch_I(σ)}.»
  Here Ωσ is VJ00's value of σ against Odd's optimal counterstrategy (BRICS RS-00-48, as in R15).
- [R15d] RESULTS R15 (d) (l. 640), «every iteration applies Switch_I with ∅ ≠ I ⊆ Iσ to Even's σ (on G) and/or with ∅ ≠ I ⊆ Iτ to Odd's
  τ (on G^d), and changes at least one of them …; Iσ depends on σ alone (Ωσ is against ⊖'s optimal reply, not against τ).»
- [VJ] VJ00 §4.2 (as used in R15), and Friedmann arXiv 1106.0778 §3, which is the form implemented in experiments/si/si.py.
  - A value is (Λ, Π, k): the cycle node Λ (the most relevant vertex of the play's cycle), the set Π of vertices on the play before Λ
    that are more relevant than Λ, and the length k of that prefix.
  - Comparison order: first the reward of Λ (an even priority p gives +p, an odd one −p, with priorities made injective by rank); then
    Π, decided by the most relevant vertex of the symmetric difference, which is better for Even iff it is even and in the larger set;
    then k, where a longer prefix is worse for Even if Λ is even and better if Λ is odd.
  - Write ⊴ for this order. For Odd vertices Ω uses an optimal counterstrategy σ̄_σ, which is positional and optimal at every vertex at
    once (VJ00 §5).
- [DEF] RESULTS R104 (l. 9864), definitions only: the IDEAL genome (N movers, levels, M options, W-target of level lev − 1 (none at
  level 0), Ξ-target xt(x, k) (a mover or X), distinct β-rank with parity, distinct gate index, start), the Ξ-graph, and the game Γ(G)
  with its start (quoted in P-N5-REACH §1). Γ(G) is defined for EVERY genome. R104's theorem needs acyclicity; its definitions do not.
  - Used shape: movers (Even, priority 0) → gates (Odd, priority 1) → {e-face e_g, β-face β_g}.
  - β_g (Even, priority 6 + 2·rank + parity) → {xt(g), u}, or → {u} when xt = X.
  - e_g (even priority above every β) → W-target, or → c_W at level 0.
  - c_W: top even self-loop. c_X: priority-2 self-loop with no other in-edge.
  - Core: K0 (top + 2) → {K1, K3}; K1 (5) → {K0, K1}; K2 (Odd, 3) → {K1, K2}; K3 (top + 3) → {K1, K2}.
  - Start: σ = genome start at the movers, β → xt (or u), K0 → K3, K1 → K1, K3 → K2.
- [N5XI] N5′-xi (box 190, docs/new/N5-DETOWER-box190.md §2.1, experiments/new/box190/n5v.py mode «xi»): SPEC S1-S5 with ONE change in
  S4a. At every Even v with |A(v)| ≥ 2 that is not its own H-cycle node, σ_new(v) := the Ξσ-best element of TIE(v) := {w ∈ A(v) :
  W*(v) = v ⊕ W*(w)}. Ties go by SPEC's choice, then the larger index. Here A(v) = {σ(v)} ∪ Iσ(v).
- [REACH-L] NOT LANDED. P-N5-REACH (docs/new/P-N5-REACH.md, frozen sha1 b7bd6937, with fixes and line L-3 adfbb3b8; at CHECKER C130 as
  R117): its §3 definition of Γ3(G) and of the standard state, and its Lemmas S3-START (§4), PAD (§5), K3 (§6.1), TAU3 (§6.4), ESC3
  (§6.5) and W3 (§6.6). Used ONLY in §7, which is therefore PROVED-CONDITIONAL.

## 2. Definitions
- IDEAL-CYC(G), for any genome G (Ξ-cycles allowed):
  - The game is Γ(G) with every Even vertex that is not a mover frozen at its start successor. Odd is unrestricted (gates and K2).
  - A state σ_t is the start off the movers plus a choice at every mover; Ω_t := Ω_(σ_t), the [VJ] value against Odd's optimal
    counterstrategy.
  - σ̄_t is the optimal counterstrategy chosen by a fixed deterministic rule (any rule; experiments use si.py's).
- A HOWARD step σ_t → σ_(t+1): every mover x goes to a successor of ⊴-largest Ω_t value, and keeps σ_t(x) if σ_t(x) is such a
  successor. The run stops at the first σ_T where no mover has a strictly better successor. T_CYC(G) := T. Ties among best successors
  may be broken by any rule.
- Labels of step t → t+1:
  - C if Λ_t(v) ≠ Λ_(t+1)(v) for some vertex v;
  - else R if σ̄_t(v) ≠ σ̄_(t+1)(v) for some Odd vertex v;
  - else p.
  C, R, P count the steps of each kind, so T = C + R + P.
- n := N + 3M + 6, the vertex count of Γ(G). n_E := the number of Even vertices.

## 3. Facts
- F1 (from [R15a]): Ω_t ⊴ Ω_(t+1) pointwise, for every step t. A Howard step switches exactly at the movers where the new successor is
  strictly better, so I is non-empty and unambiguous (one switch per vertex).
- F2 (from [VJ]): if Ω(v) ⊴ Ω′(v) and Λ ≠ Λ′, then the reward of Λ′ is strictly larger. Distinct vertices have distinct rewards.
- F3 (from [VJ], plays of a positional pair): let v be a vertex with Λ_t(v) ≠ v. Then Ω_t(v) = ext(v, Ω_t(nx_t(v))), where nx_t(v) is
  σ_t(v) for an Even v and σ̄_t(v) for an Odd v, and ext(v, (Λ, Π, k)) := (Λ, Π ∪ {v if v is more relevant than Λ}, k + 1).
  Also Ω_t(w) = (w, ∅, 0) when Λ_t(w) = w.
  Proof: σ̄_t is optimal at every vertex at once ([VJ]), so the play from v under (σ_t, σ̄_t) is v followed by the play from nx_t(v).
  Since v is not the cycle node, v lies on the prefix, or on the cycle below Λ. ∎
- F4: ext(v, ·) is ⊴-monotone and strictly monotone.
  Proof. Equal Λ: v is added to both Π or to neither, so the symmetric difference is unchanged, and both lengths grow by 1. Different
  Λ: the order is decided by Λ, which ext keeps. ∎
- F5 (Howard): σ_(t+1)(x) is ⊴-best among x's successors under Ω_t. If σ_(t+1)(x) ≠ σ_t(x), then Ω_t(σ_(t+1)(x)) ▷ Ω_t(σ_t(x)).
- F6: no mover is ever the cycle node of its own play. Movers have priority 0, every cycle of Γ(G) passes a vertex of priority ≥ 3
  (P-N5-REACH PAD (a) argued on Γ: a cycle through a mover passes a gate, and a gate leads only to e or β, of priority ≥ 6), and Λ is
  the most relevant vertex of the cycle. Every non-mover Even vertex has one successor in IDEAL-CYC. ∎

## 4. Bounds in IDEAL-CYC (PROVED)
- Lemma DOM. For every mover x, step t and successor y of x: Ω_(t+1)(x) ⊵ ext(x, Ω_t(y)).
  Proof. F3 and F6 at t+1 give Ω_(t+1)(x) = ext(x, Ω_(t+1)(σ_(t+1)(x))). By F1 and F4 this is ⊵ ext(x, Ω_t(σ_(t+1)(x))), which by F5
  and F4 is ⊵ ext(x, Ω_t(y)). ∎
- Lemma STRICT. If σ_(t+1)(x) ≠ σ_t(x), then Ω_(t+1)(x) ▷ Ω_t(x).
  Proof. By DOM, Ω_(t+1)(x) ⊵ ext(x, Ω_t(σ_(t+1)(x))). By F5 and F4 (strict) that is ▷ ext(x, Ω_t(σ_t(x))), which equals Ω_t(x) by F3
  and F6 at t. ∎
- Lemma PATH. Assume Λ_t = Λ_a and σ̄_t = σ̄_a for all t ∈ [a, b]. Let π: z_0 → z_1 → … → z_L = w be a simple path in the graph
  E_a, which has every mover edge, the frozen edge of every other Even vertex, and the σ̄_a-edge of every Odd vertex. Assume
  Λ_a(z_i) = w for every i and Λ_a(w) = w. Let μ(π) be the number of movers among z_0, …, z_(L−1), and set
  val(π) := ext(z_0, ext(z_1, …, ext(z_(L−1), (w, ∅, 0)) …)). Then Ω_t(z_0) ⊵ val(π) for every t ∈ [a, b] with t − a ≥ μ(π).
  Proof by induction on L.
  - L = 0: Λ_t(w) = w, so Ω_t(w) = (w, ∅, 0) by F3.
  - L ≥ 1, z_0 a mover: the tail has μ − 1 movers and t − 1 ∈ [a, b] with (t − 1) − a ≥ μ − 1. By induction Ω_(t−1)(z_1) ⊵ val(tail).
    DOM (with y = z_1) and F4 give Ω_t(z_0) ⊵ ext(z_0, Ω_(t−1)(z_1)) ⊵ ext(z_0, val(tail)) = val(π).
  - L ≥ 1, z_0 not a mover: Λ_t(z_0) = w ≠ z_0, and nx_t(z_0) = z_1 (a frozen edge, or σ̄_t(z_0) = σ̄_a(z_0)). F3 gives
    Ω_t(z_0) = ext(z_0, Ω_t(z_1)). The tail has the same μ, so induction and F4 finish. ∎
- Theorem BR-SEG. If Λ and σ̄ are constant on the states a, a+1, …, a+j+1 and the step a+j → a+j+1 changes σ, then j ≤ N − 1. Hence
  every maximal run of consecutive p-steps has at most N steps.
  Proof.
  - Let x be a mover with σ_(a+j+1)(x) ≠ σ_(a+j)(x). STRICT gives Ω_(a+j+1)(x) ▷ Ω_(a+j)(x).
  - Let w := Λ_(a+j+1)(x) = Λ_a(x), and let π be the play from x under (σ_(a+j+1), σ̄_a) up to its first visit of w.
  - π is simple. Every vertex on it has Λ_(a+j+1) = w, because the vertices of one play share its cycle node, and so Λ_a = w. Its
    edges lie in E_a: mover edges, frozen edges, and σ̄_(a+j+1) = σ̄_a edges. μ(π) ≤ N.
  - F3 along π gives Ω_(a+j+1)(x) = val(π).
  - If j ≥ N, PATH at t = a + j gives Ω_(a+j)(x) ⊵ val(π) = Ω_(a+j+1)(x), contradicting STRICT.
  - A run of r consecutive p-steps a → … → a + r has constant (Λ, σ̄) on its r + 1 states and every step changes σ. So r ≤ N. ∎
- Lemma CYC-COUNT. C ≤ n·(2M + 2).
  Proof.
  - By F1 and F2, each vertex's Λ changes only to a vertex of strictly larger reward.
  - The possible cycle nodes are among the β's, the e's, c_W, K1 and K2: at most 2M + 3. c_X is its own cycle node and never changes.
    K0 and K3 lie on no cycle, since K1 is frozen to its loop and K0 → K3 → K2.
  - So each vertex changes Λ at most 2M + 2 times, and each C-step changes at least one. ∎
- Theorem T-CYC. T_CYC ≤ C + R + (C + R + 1)·N ≤ (C + R + 1)(N + 1).
  Proof: the C- and R-steps split the run into at most C + R + 1 maximal p-runs, each of at most N steps (BR-SEG). ∎
- Corollary ONEP-POLY. In the variant where every gate keeps only its β-face (Odd has no choice at gates), R = 0, so
  T ≤ n(2M + 2) + (n(2M + 2) + 1)·N.
  Proof: the only Odd choice left is at K2. Its options' values come from the closed core {K0, …, K3}, which is independent of σ, so the
  deterministic rule picks the same σ̄(K2) every time. Apply T-CYC; F6 and every other fact hold unchanged. ∎
- Lemma LEVEL0. In every state σ̄_t takes the β-face at every gate of a level-0 mover. Hence R-flips happen only at gates of level ≥ 1,
  and on a genome with one level R = 0.
  Proof.
  - c_W's in-edges are its loop and the e-faces e_g of level-0 gates. Its priority top is the largest even priority on any cycle (K0,
    of priority top + 2, is on no cycle). So a value with Λ = c_W is the ⊴-largest kind, i.e. the worst for Odd.
  - If σ̄_t(g) = e_g at a level-0 gate g, then Λ_t(g) = c_W. Let σ̄′ be σ̄_t with every level-0 gate switched to its β-face. Then no
    play reaches c_W, so the play from g under (σ_t, σ̄′) has Λ ≠ c_W: strictly better for Odd.
  - That contradicts the optimality of σ̄_t at g ([VJ]). ∎

## 5. Theorem BR-SEG-G (Howard VJ strategy improvement on ANY game; PROVED)
Setting:
- G is any parity game on n vertices, with n_E Even vertices. Run Howard from any σ_0: every Even v goes to a ⊴-best successor under
  Ω_t and keeps σ_t(v) when it is one.
- Labels C / R / p are as in §2.
- H0: every step t → t+1 switches some Even x with Λ_t(x) ≠ x and Λ_(t+1)(x) ≠ x.

Claims:
- (a) every maximal run of p-steps has at most n_E steps;
- (b) C ≤ n(n − 1);
- (c) T ≤ C + R + (C + R + 1)·n_E.

Proof.
- §4's proofs, with «mover» read as «Even vertex» and no frozen vertices.
- DOM is used only at Even z_0 with Λ_t(z_0) = w ≠ z_0 inside PATH, so F3 applies there. STRICT is used only at the switched x, which
  H0 provides.
- (b): each vertex has at most n − 1 possible later cycle nodes (F1, F2). ∎

## 6. Reduction for general games (PROVED; a reduction only)
- Lemma DECOMP-G. Take any N5-type run in which each iteration's σ-change is Switch_I with I ⊆ Iσ ([R15d] form). Let S be the set of
  iterations that change σ, and Q_τ the number of iterations that keep σ. Then #iterations = |S| + Q_τ. Ωσ depends on σ alone
  ([R15d]), so the σ's at the iterations of S, in order, form a strategy-improvement run. ∎
- Theorem RED-XI. Consider an N5′-xi run on a game G. Assume:
  - (X1) at every iteration of S, σ_new is a Howard step of σ (every Even vertex goes to a ⊴-best successor, or keeps σ if σ is one);
  - (X0) H0 holds for these steps.

  Then #iterations ≤ (n_E + 1)·(n(n − 1) + R_σ + 1) + Q_τ, where R_σ is the number of S-steps at which σ̄ changes and C is not
  charged. So: «N5′-xi makes polynomially many iterations on every game where X0 and X1 hold» ⇐ X := «R_σ and Q_τ are polynomial in n
  on those games».
  Proof: DECOMP-G and BR-SEG-G (c) applied to the Howard run formed by S. ∎
- READING (not to sign): X1 is exactly where the W-ties enter. N5′-xi's step is the Ξσ-best element of TIE(v), so X1 means «TIE(v)
  contains a ⊴-best successor» (TIE-FULL). §7 shows TIE-FULL on Γ3. On general random games it often fails (§9).

## 7. REACH3-CYC (PROVED-CONDITIONAL on [REACH-L])
Theorem REACH3-CYC. Let G be any genome (Ξ-cycles allowed). The N5′-xi run of Γ3(G) from S3 has the following form:
- its states 0, …, T3 are standard states (P-N5-REACH §3: τ = the start, σ = the start off the movers);
- the mover parts form a Howard run on Γ3(G), with every non-mover Even vertex frozen and ties broken by SPEC's choice, then the larger
  index;
- T3 is the first state at which no mover has a strictly better successor in Γ3;
- transition T3 + 1 is an S4c fallback.

Proof. Induction on j: state j is standard. j = 0 is S3-START (every genome). Step j < T3:
- τ: TAU3 (every genome) gives Iτ = ∅ in every standard state, so τ_new = τ.
- Off the movers: Iσ ∋ (K0, K1) in every standard state (K3, every genome). Consider ESC3, labelled IDEAL-ACYC in [REACH-L]. Its proof
  follows only plays of S4a's arena H, where Odd plays τ = pe at every gate:
  - an H-play from xt(g) is mover → pad → gate → pe → e → … down the W-levels → c_W;
  - an H-play from pb_g ends in the core's odd cycle (K3 (d)).

  Neither play takes a β-face, so the Ξ-graph is never used and the proof holds verbatim for every genome. Hence every pointwise optimum
  of H keeps σ off the movers, and the TIE sets at β_g and K0 are the singletons {xt(g)} and {pA}. N5′-xi's rule therefore agrees with
  SPEC there.
- Movers: W3 (i)-(iii), labelled IDEAL-ACYC. Its plays are (σ, τ)-plays and H-plays with τ = pe; W(β_g) takes one β step and then a
  W-descent. So it holds verbatim for every genome: x is not its own W′-cycle node and TIE(x) = R(x) = {σ(x)} ∪ Iσ(x). N5′-xi takes the
  Ξσ-best element of R(x). R(x) contains every successor strictly better than σ(x), so this is a ⊴-best successor: a Howard step.
- S4c does not fire while some mover changes.

Step T3: R(x) = {σ(x)} at every mover, so σ_new = σ and τ_new = τ, while Iσ ∋ (K0, K1). S4c fires.

Not used: KEY3, PLAY3, SBAR3, Fact X (the acyclic-only lemmas). The referee check needed: ESC3 and W3 contain no hidden use of
Ξ-acyclicity. ∎

Corollary T3 (PROVED-CONDITIONAL). §4's proofs apply to the Howard run on Γ3 (movers have priority 0, pads are never cycle nodes by
PAD (b), non-mover Even vertices are frozen in standard states, and the Odd vertices are the gates and K2). So:
- T3 ≤ C + R + (C + R + 1)·N, with C ≤ n3·(2M + 2) and n3 = N + 7M + 10;
- LEVEL0 holds on Γ3 as well;
- the first fallback of N5′-xi on Γ3(G) comes at iteration T3 + 1.

Hence «N5′-xi's FL run on Γ3(G) is polynomial in N + M for every genome» ⇔ «R is polynomial along these Howard runs». The direction ⇐ is
the Corollary; ⇒ holds because R ≤ T3.

## 8. DEAD (instances pinned, machine-checked)
- DEAD SEG-2P: «in IDEAL-CYC, every run of consecutive steps keeping all Λ has at most N steps» (that is, BR-SEG without fixing σ̄).

  | instance | N | longest Λ-keeping run | labels |
  | --- | --- | --- | --- |
  | experiments/new/box191/inst/DEAD_SEG2P_d4_N8.json | 8 | 9 steps (8 p, then 1 R) | ppppppppRC |
  | inst/DEAD_SEG2P_d7_N14.json | 14 | 15 steps | CCCCpRRRRppRRRpRppp |
  | inst/DEAD_SEG2P_d9_N18.json | 18 | 21 steps | pppRppRppRppRRRpppppp, C = 0 |

  Obstruction: R-steps inside the run, as BR-SEG requires.
- DEAD ODD-FIXED: «σ̄ is constant on every run of Λ-keeping steps». The same instances contain R-steps.

## 9. DATA (not to sign; experiments/new/box191/, frozen check191.out)
- Γ3 against IDEAL-CYC (eq191.py), mover sequences:
  - 22/22 exact: 8 L-RED R215 Ξ-cyclic genomes (inst/cyc*.json, byte copies of claude/l-red b14066e1) and 14 P-N5-REACH corpus genomes;
    xi = T + 3.
  - rand191.py: 297/300 exact (seed 1) and 974/1,000 exact (seed 2). Every divergence starts at an exact VJ tie, consistent with PAD (c).
- REACH3-CYC (howard3_191.py): 1,000 random genomes, 2,167 mover-phase transitions; 0 non-standard states, 0 non-Howard steps, 0 bad
  stops.
- BR-SEG / CYC-COUNT: seg1p191.py, 2,000 genomes, 0 violations (one- and two-player); subrun191.py, 1,000 genomes, every p-run ≤ N.
- BR-SEG-G on Friedmann's switch-all family (pgsolver_port.py switchallexp, Howard), from si.py's best-reward start:

  | N | T | C | R | longest p-run | n_E |
  | --- | --- | --- | --- | --- | --- |
  | 2 | 30 | 0 | 4 | 9 | 23 |
  | 3 | 70 | 0 | 10 | 11 | 32 |
  | 4 | 150 | 0 | 24 | 13 | 41 |
  | 5 | 310 | 0 | 54 | 15 | 50 |
  | 6 | 630 | 0 | 116 | 17 | 59 |
  | 7 | 1243 | 0 | 241 | 19 | 68 |

  2,000 random games at n 12 all satisfy BR-SEG-G (a).
- X1 on general games (x1gen191.py): Howard-faithful σ-steps 401/517 (n 12) and 333/570 (n 24).
- Growth (weak hill-climbs): T_CYC ≤ 33 at N 20; R ≤ 9 in every climb best.

## 10. Machine checks and pins
- experiments/new/check.sh block «BOX 191 XI-CYCLIC» runs experiments/new/box191/check191.sh (~1 min) and diffs it against the frozen
  check191.out.
- Pins: experiments/new/box191/xicyc.pins (sha1 of this packet, line L-1, the tools, check191.out and the instances). The check.sh
  block «P-N5-XICYC» runs sha1sum -c on it.

## 11. TARGET.md diff (READING)
TARGET.md asks for a polynomial-time algorithm (gauntlet §5). This packet proves no time bound for N5′-xi or N5. It proves:
- an iteration bound for Howard runs in terms of R;
- a conditional realisation on Γ3;
- a reduction.

No statement here is a TARGET.md theorem. G-N5-TIME stays OPEN.

## 12. Limits
- R is not bounded anywhere. Whether R is polynomial on IDEAL-CYC / Γ3 is OPEN; L-RED 53 is attacking it.
- §7 is conditional on [REACH-L] (not landed) and on the ESC3 / W3 re-reading.
- BR-SEG-G needs H0. The DOM step is the VJ analogue of a folklore domination lemma: Hansen-Miltersen-Zwick arXiv 1008.0530 Lemma 5.3 /
  5.4 and §5, which calls the MDP case «well-known» and cites Meister-Holzbaur 1986, NOT opened here.
- BR-SEG, CYC-COUNT and ONEP-POLY were not found in the sources opened (L-NEW notebook, «Sources opened», successor 59). This is not a
  novelty claim.
- RED-XI: X1 fails often on general games, so RED-XI says nothing about general games without TIE-FULL.
