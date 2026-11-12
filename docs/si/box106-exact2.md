# Box 106 (D18; O2 of box 104 at depth 2, exact): the largest L* of N5's key rule on the free depth-2 ladder — statement, proven bounds 5 ≤ L*_max(2) ≤ 8, the exact adversarial layer, and the reduction to a 4-node one-player game
L-SI successor 53 (Opus 5.5), D18 / D1 / D21; Lead 2026-11-12 22:03Z: «Next box, approved: box 106, the exact d = 2 maximum of KEY on the
free ladder by an order / SAT encoding in R112's style, with a proof certificate. Keep R112's machine-trust standard: an audited encoding
plus RUP-checked refutations, regenerated. Requirements: statement first; the kill and dead-end criteria as in box 105; the answer is a
number with its certificate: SAT model replayed on N5, or a DRUP-checked UNSAT for «> m».» Written 2026-11-12 (date -u in the commit).
Labels: PROVED (L-SI lane, unrefereed) / CONJECTURE / DATA (counter, unit, set, scope) / DEAD / OPEN / READING.
**SCOPE LINE: nothing here is a TARGET.md claim, M3 or M4, or a gauntlet step. G-N5-TIME stays OPEN. Every statement is about KEY(G*)
(box 105 §1) on the free depth-2 ladder genomes below, and about N5 on Γ3*(G*) only through box 105's Lemma KEY-MODEL (lane, unrefereed)
or through a replay on N5.** At fixed depth O2 already holds (box 105, DEPTH-BOUND*: L* ≤ Π_ℓ (1 + w_ℓ(Δ − 1)) − 1); the number asked
here is not about polynomiality. It measures how far VALUE-induced availability can follow the adversarial ceiling, whose growth 3^d − 1
is the pattern a kill family for O2 would have to approach on unboundedly many levels.

## 0. Statement first
- The class 𝓛*_2 (box 105 ladder105.py's shape, d = 2): movers 0, 1 on level 0 and 2, 3 on level 1; every mover has options k ∈ {0, 1};
  option k of a level-1 mover W-points to mover k; level-0 options W-point to nothing (their e goes to c_W). Free data: the Ξ-target of
  each of the 8 options (a mover 0-3 or X; Ξ-cycles and Ξ-self-loops allowed), the 8 gate indices (distinct), the start, and π, an
  injective map of the 16 carriers (8 β, 8 e) into the integers ≥ 6 of either parity (box 104 §4's free genome). Γ3*(G*) as there.
- **Question Q106.** L*_max(2) := max { L*(G*) : G* ∈ 𝓛*_2 }, L* the number of steps of KEY(G*) (box 105 §1); by KEY-MODEL N5 from S3 on
  Γ3*(G*) makes exactly L* + 3 iterations.
- **Known now.**
  - (LB, DATA with a replayed instance) L*_max(2) ≥ 5: box 105's best/ladder_free_d2.json (claude/l-si d7747b99, out/val105.out: «L* 5»,
    N5 replay with s3fail, keyfail, endfail, wrong, keymono, valmono 0, i.e. N5 from S3 makes 8 iterations with its only fallback at 6).
  - (UB, PROVED lane) L*_max(2) ≤ 8: box 105's DEPTH-BOUND* with w_0 = w_1 = 2, Δ = 2: (1 + 2)(1 + 2) − 1 = 8.
  - (UB is the adversarial maximum, exact, §1) With availability chosen freely at every state, the KEY rule's longest run on this shape
    is exactly 8 over all gate orders and starts; 1,488 runs have length ≥ 6.
- **The answer this box must produce.** A number m with: (i) a genome G* ∈ 𝓛*_2 with L*(G*) = m, replayed on N5 from S3 (m + 3 iterations,
  one fallback, regions = harness Zielonka, S3 standard): a certificate independent of KEY-MODEL; and (ii) for m < 8, a refutation of
  «some G* ∈ 𝓛*_2 has L* ≥ m + 1»: a CNF whose encoding is audited (§3.3) and a DRUP / RUP-checked UNSAT proof, regenerated from the
  encoder by a second run, as RESULTS R112 did for T^R(3). (ii) is a statement about KEY(G*); it is a statement about N5 through
  KEY-MODEL only, and must say so.
- **CONJECTURE KEY2-5 (lane; DATA only: box 105's 40 restarts × 3,000 steps found 5 and never more, both priority modes).** L*_max(2) = 5.
- Kill criterion for KEY2-5: one G* ∈ 𝓛*_2 with L* ≥ 6 whose N5 replay from S3 gives L* + 3 iterations with one fallback and correct
  regions (key105.validate's six counters 0). Dead-end criteria for this box's METHOD (recorded with the instance that kills it): the
  encoder's availability bits differ from key105.py's (computed by SPEC's own engine on Γ3*) on any audited genome (§3.3); or the
  mover-game reduction of §2 fails on any genome (counter mgfail ≠ 0); then the encoding is not used and the failure is written down.

## 1. Layer 1 (exact, PROVED by exhaustive enumeration; tool experiments/si/box106/skel106.py)
- Keys on 𝓛*_2 (box 105 §1): level 0, key(x, k) = gate(x, k); level 1, key(x, k) = (gate(k, s′(k)), gate(x, k)) with s′ the NEW level-0
  choices. The first entries of a level-1 mover's two options are gates of the two DIFFERENT level-0 movers, so they always differ: only
  the order of the four level-0 gates matters (24 orders), and movers 2 and 3 rank their options the same way. No state repeats along a
  run (KEY-MONO*: every step strictly decreases the key of a mover that moves and no key increases, while keys are functions of the state).
- skel106.py enumerates, for every one of the 24 orders and 16 starts, EVERY run of non-trivial steps under freely chosen availability
  (at each state each mover has {current} or {0, 1}), with the availability each step NEEDS per mover: «A» (it moves: the other option
  must be available), «N» (it stays although the other option is key-less: the other option must NOT be available), «-» (free).
  Output (out/skel106.out): «SKEL106 max length over 24 gate orders x 16 starts: 8 | paths by length 0:384 1:1560 2:3144 3:3888 4:3376
  5:2216 6:1072 7:352 8:64 | lines written (length >= 6) 1488»; the 1,488 runs of length ≥ 6 with their needs are in out/skel106_ge6.txt.
- So Q106 is: which of these 1,488 need-patterns can VALUES realise. A pattern is realised by G* iff at every visited state s_j and every
  mover x with need A the other option is strictly ▷-better than the current one under V_(s_j), and with need N it is not.

## 2. The reduction: V_s on 𝓛*_2 is the value of a one-player game on four nodes (Claim MG: PROVED, lane; audited, mgfail 0)
- The MOVER GAME M_s. Nodes: the movers 0-3; terminals cW and K. Node z has two edges, both chosen by Odd (the faces of z's ACTIVE gate
  g_(z,s(z))): its e-edge, labelled with the carrier e_(z,s(z)), to the mover wt(z, s(z)) (to cW if lev(z) = 0); and its β-edge,
  labelled with β_(z,s(z)), to the mover xt(z, s(z)) (to K if xt = X). For an option (x, k) to be valued, its gate g_(x,k) is the start
  node, with the same two edges for (x, k) (if k = s(x) it is x's active gate). Lengths are counted in Γ3*'s edges: from a gate, 3 edges
  to the next mover through pe → e or pβ → β, or to c_W through pe → e (level 0), or 9 edges to K1 through pβ → β → pb → K0 → pA → K3 →
  K2 → r → K1; from a mover, 2 edges to its active gate (pad, gate); a carrier sits 2 edges after its gate.
- **Claim MG (PROVED, lane).** In the standard state of s (σ_s at movers and β's, τ0, K-config κ0), for every option (x, k): V_s(x, k) =
  pad ⊕ (Odd's minimum, over its face choices at g_(x,k) and at the four active gates, of the VJ value of the resulting play of M_s),
  where a play ending in cW has node c_W and P = ∅, a play ending in K has node K1 and P = {its carriers} ∪ {K0, K3}, and a play that
  closes a cycle of movers has as node the most relevant carrier on the cycle and as P the carriers before it that are more relevant.
  Proof. Under σ_s every Even vertex has one successor on these plays: a mover goes to its pad and gate, a β to xt (or pb), K0 → pA,
  K1 → s, K3 → K2. So a play from m_(x,k) is fixed by Odd's choices: the face at g_(x,k), the face at every active gate it meets (no
  other gate is reachable: from a mover the play enters its active gate), and K2's. K2's choice matters only after the play has
  entered the core, where the loop gives node K2 and r gives node K1, more relevant and odd, hence smaller for Even: the minimum takes r
  (this is K2-r, which uses the core only). Every vertex of such a play other than the carriers, c_W, K0, K1, K3 has Ω ≤ 3 and is
  neither a cycle node nor in a P-set (box 104 §4, PAD under (R*)). So the play's value is the M_s play's value as described, with the
  stated lengths, plus the pad. Odd's σ̄ is a pointwise optimum ([1E-N3] P1), so at every start it attains the minimum over all Odd
  strategies, i.e. over the face choices above. The availability bit «V_s(x, k′) ▷ V_s(x, s(x))» is the same comparison without the pad. ∎
- DATA (mg106.py; out/mg106.out; the evaluator takes the minimum by brute force over the 2^5 face choices; SPEC's side is si.Engine on
  Γ3*(G*) in the standard state, as key105.py): counter mgfail (unit (genome, state, mover): the two availability bits differ), every
  one of the 16 states of each random genome of ladder105.py's generator:
  «MG106 rand seed 1062 genomes 300: (genome, state, mover) units 19200 mgfail 0»
  «MG106 rand seed 1064 genomes 300: (genome, state, mover) units 19200 mgfail 0»
  «MG106 rand seed 1061 genomes 20 CTRL 1: (genome, state, mover) units 1280 mgfail 281 | first (2, (0, 0, 1, 0), 0)»
  «MG106 xrun seed 1063 genomes 1000: runfail 0 | max L* 3»
  (CTRL 1 = the evaluator flips every e-carrier's parity: fires.) xrun: the abstract KEY run equals key105.py's run state for state
  (counter runfail, unit genomes). So availability on 𝓛*_2 is a finite function of (s, xt, the carriers' order and parities), exactly
  as §3's encoding needs; and the abstract run (about 2 ms per genome) can search far more than box 105's engine-based climb.

## 3. Plan and status (OPEN)
- 3.1 mg106.py: the mover-game evaluator; audit against key105.py (SPEC's engine on Γ3*) on random 𝓛*_2 genomes: counter mgfail (unit
  (genome, state, option): the mover-game value's comparison with the current option's differs from SPEC's availability bit); must be
  0 on every audited genome, with a control (one carrier's parity flipped in the evaluator only) that fires.
- 3.2 cnf106.py: the query «some G* ∈ 𝓛*_2 has L* ≥ m + 1» as CNF: one-hot Ξ-targets; a strict total order on the 16 carriers (pairwise
  bits + transitivity); parity bits; the 24 gate orders and 16 starts enumerated OUTSIDE the CNF (as skeleton families from §1) or
  encoded; per visited state Odd's strategy bits in M_s with local-optimality clauses; the needs A / N as value comparisons.
- 3.3 Audit (R112's standard): every satisfying assignment is decoded into a genome and replayed on N5 (key105.validate); random
  assignments of the free data are pushed through both the CNF (unit propagation to a full assignment) and key105.py, and the predicted
  availability bits compared (counter cnffail); a mutation control.
- 3.4 Certificate: CaDiCaL 1.9.5 (as R112; available here through python-sat 1.9.dev15's bindings, version to be printed) with DRAT output
  for «≥ m + 1», checked by a RUP checker (the referees' docs/referee/scratch/ref_rup.c, read-only, or drat-trim), and regenerated.
- Status at this commit: §0, §1, §2 done (3.1 = mg106.py, audited); a kill search with the abstract evaluator is running
  (runclimb106.sh: 40 × 10 restarts × 5,000 steps, best genomes replayed on N5; outputs land in the next commit); 3.2-3.4 not started.
