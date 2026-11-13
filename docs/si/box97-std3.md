# Box 97: [STD3] for every genome up to the first fallback (independent re-derivation of P-N5-CHAIN §3 REACH3-ALL)
L-SI successor 50 (Opus 5.5), D18 / D14 / D1; Lead 2026-11-09 10:48Z and 2026-11-11 21:10Z (BOX 97: «Prove [STD3] for Ξ-cyclic G up to
the first fallback … Name every premise by R-id. If it does not hold, give the exact failing configuration.»). Labels: PROVED (L-SI lane,
unrefereed) / DATA (unit, set, scope, counter) / READING. Not a TARGET.md claim; not M3 or M4; not a gauntlet step; G-N5-TIME stays OPEN.

## 0. Answer
- [STD3] HOLDS for every genome (Ξ-cyclic included) up to the first fallback: N5′-xi's states 0, …, T3 on Γ3(G) from S3 are standard,
  its mover steps are Howard steps, and its first fallback is iteration T3 + 1. This is NOT new: it is L-NEW's Theorem REACH3-ALL
  (P-N5-CHAIN §3, frozen claude/l-new 93531b03, landing as R125; first referee SIGN per docs/NOW.md (REFEREE 29), second referee
  in progress). What box 97 adds: an independent step-by-step check of that proof from landed premises only (§2), the exact list of
  what is landed and what is not (§1), and run-level DATA on two sets (§3). No gap found; no failing configuration exists before the
  first fallback; after it, [STD3] fails (L-RED 64, MWR4_2), as P-N5-BONLY3 §3 already states.
- What is still not landed: (i) R117's LINE states S3-START and PAD for acyclic Ξ-graphs only, although its ENTRY signs them for every
  genome; (ii) ESC3 and W3 for Ξ-cyclic G are P-N5-CHAIN's ESC3-ALL and W3-ALL (pending R125). So until R125 lands, [STD3] for Ξ-cyclic
  G is PROVED at lane level (this box, and L-NEW's packet with one referee's signature), not a landed premise.

## 1. Premises (each by R-id)
- [DEF] RESULTS R104's definitions of the genome, Γ(G) and its start (as quoted in P-N5-BONLY3 §1); [DEF3] RESULTS R117's definition
  of Γ3(G) (pads as quoted there; mover pads m_(x,k) of priority 2 for the start option and 0 otherwise).
- [SPEC] SPEC S2 (strict improving edges), S4a (A(v) = {σ(v)} ∪ Iσ(v); arena H: Even keeps A(v), Odd follows τ), S4b, S4c
  (docs/new/N5-ssi-global.md, RESULTS R15's object), with N5′-xi's change [N5XI] in S4a (RESULTS R118: «an N5′-xi run (box 190's S4a tie
  rule by Ξσ)»; P-N5-XICYC l. 45-47 as P-N5-CHAIN §1 quotes it: σ_new(v) := the Ξσ-best element of TIE(v) := {w ∈ A(v) : W*(v) = v ⊕ W*(w)}
  at every Even v with |A(v)| ≥ 2 that is not its own H-cycle node).
- [1E-N3] RESULTS R57 (b) as landed in R104: S1's σ̄ and S4a's arena optimum are pointwise optima.
- From RESULTS R117's ENTRY (P-N5-REACH, signed for every genome; R118's own text: «RESULTS R117's entry signs S3-START, PAD, K3 and TAU3
  for every genome and ESC3, W3 for acyclic Ξ-graphs»): S3-START (S3's start pair is the standard state for the genome start), PAD (no pad
  is a cycle node or in a P-set), K3 (a)-(d) (the core: (b) Iσ ∩ edges out of K0, K1, K3 = {(K0, K1)}; (d) in H every pointwise
  optimum keeps pA at K0, and K1, K3 have one option), TAU3 (Iτ = ∅ in every standard state).
- RESULTS R118 Lemma K2-r (σ̄(K2) = r on Γ3 for every genome), which K3 (b)'s values need (P-N5-REACH's K3 (b) otherwise cites SBAR3,
  which is IDEAL-ACYC; R118: «with σ̄(K2) = r proved for every genome in P-N5-XICYC's fixes»).
- Not used: any IDEAL-ACYC lemma (PLAY3, SBAR3, KEY3, Fact X, ESC3 / W3 as signed in R117), any Ξ-acyclicity, any L-RED lane lemma.

## 2. The proof, step by step (re-derived; credit L-NEW P-N5-CHAIN §3; my check marks where each step's premise comes from)
Fix a genome G (any Ξ-graph) and a STANDARD state (σ, τ) of Γ3(G) for a mover state s: σ = s at the movers (through their pads), the
transported start elsewhere (K0 → pA, K1 → s, K3 → K2, β_g → xt(g) if a mover, else pb_g); τ = pe_g at every gate, K2 → K2.
- (L1) In the arena H every H-play from a mover descends to c_W. In H Odd follows τ (pe at every gate). A mover's options are pads to its
  gates; a gate goes pe → e; e goes to its W-target, a mover one level lower ([DEF]), or to c_W at level 0. So an H-play from a mover of
  level ℓ passes 5 vertices per level (mover, m, g, pe, e) and ends in c_W's loop, meeting no β. Its value is (c_W, ∅, 5ℓ + 5): c_W is the
  most relevant vertex on the play ([DEF], top priority), so the P-set is empty. The same holds for every choice inside A(·). [DEF], [DEF3], [SPEC] S4a.
- (L2) W3-ALL: every H-value of a pad m_(x,k) ∈ A(x) is (c_W, ∅, 5ℓ + 4), whatever the lower choices (L1). So x ⊕ W*(y) = W*(x) for
  every y ∈ A(x): TIE(x) = A(x). x is on no H-cycle (levels strictly decrease), so x is not its own H-cycle node. [1E-N3] for W*.
- (L3) ESC3-ALL at β_g, xt(g) a mover: A(β_g) ⊆ {xt(g), pb_g} ([DEF] edges) and σ(β_g) = xt(g) ∈ A(β_g). The H-play via xt(g) ends at
  c_W (L1), node c_W, even, positive reward. The H-play via pb_g enters K0 = u; there K3 (d) keeps K0's choices in H to {pA, K1}, both
  ending in an odd cycle (node K1 or K2): negative reward. β_g is on no H-cycle: its only in-edge is from pβ_g, whose only in-edge is from
  its gate, which plays pe in H. So every pointwise optimum picks xt(g), and β_g ⊕ W*(pb_g) has another cycle node: TIE(β_g) = {xt(g)}.
  At K0: K3 (b) gives A(K0) = {pA, K1}, and K3 (d) gives TIE(K0) = {pA} (two different odd nodes, K2 via pA better). K1, K3: one option in H
  (K3 (b), which needs K2-r). Pads, e, c's, β_g with xt = X: one successor. [DEF], K3 (b), (d), R118 K2-r, [1E-N3].
- (L4) Iσ ≠ ∅ in every standard state: (K0, K1) ∈ Iσ (K3 (b)). Iτ = ∅ (TAU3), so S4b changes nothing and S4c can act only through Iσ.
- (L5) Induction (REACH3-ALL). State 0 is standard (S3-START). If state j < T3 is standard: τ_new = τ (L4); off the movers σ_new = σ
  ((L3): [N5XI] picks in TIE, which is {σ(v)} at β_g and K0, and every other non-mover has one option in H); at a mover x with |A(x)| ≥ 2,
  TIE(x) = A(x) and x is not its own H-cycle node (L2), so σ_new(x) is the Ξσ-best element of A(x) = {σ(x)} ∪ Iσ(x): a ⊴-best successor
  (A(x) holds every successor strictly better than σ(x)), i.e. a Howard step; where nothing is strictly better A(x) = {σ(x)}. Since j < T3
  some mover has a strictly better successor, σ_new ≠ σ, S4c does not fire, and state j + 1 is standard. At j = T3: A(x) = {σ(x)} at every
  mover, σ_new = σ, τ_new = τ, Iσ ∋ (K0, K1): S4c fires at iteration T3 + 1. ∎
- Where acyclicity could have entered and does not: (L1) never takes a β → xt edge (Odd plays pe in H); (L3) takes ONE β → xt edge and
  then descends by (L1). No step follows a Ξ-cycle. This matches P-N5-CHAIN's own step check (quotes196.py) and L-RED 58's R224-chain §1.
- σ̄_t: [STD3]'s second half (σ̄_t pointwise optimal against σ_t) is [1E-N3], S1's output.
- After the first fallback the induction stops: S4c changes K0 (and then K1), so states T3 + 2, … are not standard. L-RED 64 (claude/l-red
  328a6fe2, MWR4_2 sha1 856d369b…, states 32-33) shows B-ONLY3's conclusion failing there; box 97's control CTRL=post sees the
  non-standard states (§3).

## 3. DATA (experiments/si/box97: std97.py, run97.sh; engine L-NEW gamma3 / n5v / n5x / eg195 at claude/l-new fcba92fc)
- Counters (must be 0): nstd (unit state j ≤ T3: σ off the movers or τ not standard); s0 (unit genome: state 0 not standard,
  S3-START); nfb (unit genome: no fallback before the cap 20000); nhow (unit transition j → j + 1, j < T3: a mover moves to a successor
  that is not ⊴-best for state j's values, Howard).
- Results: nstd = s0 = nfb = nhow = 0 on box 91's 11 and box 93's 8 frozen instances (19 genomes, all Ξ-cyclic; 883 states, the same
  state counts as box 96's g3 runs; out/inst97.out) and on 600 random genomes (rand191.rgen, seed 9701; 542 Ξ-cyclic; 1,969 states;
  out/rand97.out).
- Control CTRL=post (the run continues 3 iterations past the first fallback, outside [STD3]): nstd = 3 on MWR4_2 (states 31-33 after T3 = 30, i.e. the fallback's target and two more) and 3 on C6G8_n54 (out/ctrl97.out): the counter
  fires outside the frame, as L-RED 64 found.
- L-RED 64's census (claude/l-red 328a6fe2, R230): «early non-std 0» on 1,900 random Ξ-cyclic and 24 pinned genomes (its commit line;
  quoted, not re-run).

## 4. Consequences (READING)
- P-N5-BONLY3 §3's HYPOTHESIS [STD3] is PROVED at lane level here and in P-N5-CHAIN §3 (one referee's signature so far); it becomes a
  landed premise when R125 lands. Nothing in the frozen P-N5-BONLY3 or P-N5-GATE changes; a fixes entry citing R125 by id can follow then.
- R118 (k)'s CONDITIONAL is then removed for every genome up to the first fallback (REACH3-ALL is exactly R118 (k)'s statement with the
  [REACH-L] items proved for every genome). Nothing is claimed after the first fallback, and nothing about R (σ̄-changes) or T3's size.

## 5. Sources opened (this box)
- claude/l-new 93531b03 docs/new/P-N5-CHAIN.md §1-§3; trunk docs/new/P-N5-REACH.md §4 (S3-START), §5 (PAD), §6.1 (K3), §6.4 (TAU3),
  §6.5-§6.6 (ESC3, W3 as signed); trunk docs/RESULTS.md R117, R118 ((k), K2-r); trunk docs/NOW.md (referee roster lines); claude/l-red
  328a6fe2 (R230 commit and outputs).
