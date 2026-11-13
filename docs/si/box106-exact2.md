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

## 2a. Kill search for KEY2-5 with the audited evaluator (DATA; a SEARCH, not an enumeration; no new statement)
- runclimb106.sh (finished 2026-11-12T23:36Z by date -u): mg106.py climb, 40 chunks (seeds 1-40) × 10 restarts × 5,000 hill-climb steps
  (ladder105.py's moves: Ξ-target, gate swap, carrier-rank swap, parity flip, start flip) on 𝓛*_2, score = L* of the abstract run
  (= key105's run, §2 xrun); out/climb106.out (40 lines, first and last inserted by script):
  «MG106 climb seed 1 restarts 10 steps 5000: best L* 5 | per restart [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]»
  «MG106 climb seed 40 restarts 10 steps 5000: best L* 5 | per restart [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]»
- Over the 400 restarts the final L* is 5 in 373 and 4 in 27; none is above 5. Each chunk's best genome (best/climb106_<seed>.json) was
  replayed on N5 from S3 by box 105's val105.py (out/climbval106.out): 40 of 40 lines «L* 5 (search: 5) Xi-graph cyclic | s3fail 0 keyfail
  0 endfail 0 wrong 0 keymono 0 valmono 0», i.e. N5 makes 8 iterations with its only fallback at 6 on each.
- So CONJECTURE KEY2-5 survives this kill search (about 2·10^6 evaluated genomes, against 1.2·10^5 in box 105's free d = 2 search): DATA only. The exact
  answer needs §3's certificate; the next query is «L* ≥ 6».

## 3. Plan and status (OPEN)
- 3.1 mg106.py: the mover-game evaluator; audit against key105.py (SPEC's engine on Γ3*) on random 𝓛*_2 genomes: counter mgfail (unit
  (genome, state, option): the mover-game value's comparison with the current option's differs from SPEC's availability bit); must be
  0 on every audited genome, with a control (one carrier's parity flipped in the evaluator only) that fires.
- 3.2 cnf106.py (DESIGN, not written; successor 53 → 54): the query «some G* ∈ 𝓛*_2 has L* ≥ m + 1» as ONE CNF (no outside
  enumeration, so one UNSAT proof), built on Claim MG:
  - Free data: XT[q][t] one-hot, q the 8 options, t ∈ {0, 1, 2, 3, X}; GO[i][j] a strict total order on the 4 level-0 gates (pairwise
    bits + transitivity); S0[x] the start; ORD[c][c′] a strict total order on the 16 carriers (120 pairwise bits + 3·C(16,3) transitivity
    clauses), PAR[c] their parities. cW sits above and K1 below every carrier (constants), K0, K3 above cW.
  - Availability, run-independent: AV[σ][x] for the 16 states σ and 4 movers (64 variables). The run: states R[j] (4 bits, j = 0..m + 1),
    R[0] = S0; R[j + 1] = the KEY step of §1 (level 0 by GO, level 1 by the NEW level-0 gates) with availability AV[R[j]] (a 16-way mux
    per bit); R[j + 1] ≠ R[j] for j ≤ m. (Run-independence of AV is what keeps the CNF small: values depend on the state only.)
  - Values, per state σ (fixed in the encoding, so the e-edges and the active gates are constants): Odd's optimal positional strategy as
    witness bits RHO[σ][u] at the 8 gates u (4 active, 4 inactive); the successor of node z under RHO is a one-hot over {0, 1, 2, 3, cW, K}
    (e-face: constant; β-face: XT of z's active option). A play = the walk from a start gate in this functional graph, unrolled for at
    most 5 node visits (4 movers + start), with one-hot position variables; from it per carrier c: ONPATH, ONCYC, NODE (c on the cycle
    and above every other cycle carrier by ORD), INP (on the path before the node's first visit and above the node), and the terminal
    flags. Lengths: 2 + 5·(steps) per §2's edge counts, as a one-hot over the ≤ 6 possible values.
  - Comparison CMP(p, q) («p ▷ q» in SPEC S1's order) of two plays: reward of the nodes (ORD, PAR; cW / K1 constants), else the top of
    the symmetric difference of INP (a «top» variable per carrier: in exactly one set and no higher carrier in exactly one set; its
    parity and side decide), else the lengths by the node's parity.
  - Constraints per σ: 16 plays (each gate under RHO, and each gate with its OTHER face first and RHO after); local optimality of RHO at
    all 8 gates (no face strictly better for Odd: «not CMP(own, other) reversed»), which characterises Odd's pointwise optimum in a
    one-player game (RESULTS R36 (c) Lemma P1); AV[σ][x] ⇔ CMP(play from x's inactive gate, play from x's active gate).
  - Expected size: 16 states × (16 plays × ~6·5 position vars + 16 × ~5 per-carrier vars) ≈ 30k variables, ≲ 10^6 clauses: within
    CaDiCaL's range (R112's CNF was of this order).
- 3.3 Audit (R112's standard): every satisfying assignment is decoded into a genome and replayed on N5 (key105.validate); random
  assignments of the free data are pushed through both the CNF (unit propagation to a full assignment) and key105.py, and the predicted
  availability bits compared (counter cnffail); a mutation control.
- 3.4 Certificate: CaDiCaL 1.9.5 (as R112; available here through python-sat 1.9.dev15's bindings, version to be printed) with DRAT output
  for «≥ m + 1», checked by a RUP checker (the referees' docs/referee/scratch/ref_rup.c, read-only, or drat-trim), and regenerated.
- Status: §0, §1, §2 done (3.1 = mg106.py, audited); §2a kill search done (KEY2-5 survives); 3.2 designed, not written; 3.3-3.4 not started. (Successor 54: 3.2 written as §3a, which supersedes the design above where they differ; 3.3 = §3b.)

## 3a. The encoding as written: cnf106.py (L-SI successor 54; Lead 2026-11-13 01:27Z «go» conditions: encoding and audit in this file BEFORE any solve)
- One CNF, cnf106.build(LEN), for «some G* ∈ 𝓛*_2 has L*(G*) ≥ LEN»; build(None) is the same CNF without the length constraint (the audit
  uses it). No outside enumeration. Variables and constraints, in the order the encoder writes them:
  - Free data (the genome): XT[q][t] one-hot (q = 2x + k, t ∈ {mover 0-3, X}); GO: a strict total order of the four level-0 gates (6
    pairwise bits, transitivity on all ordered triples); ORD: a strict total order of the 16 carriers (β_q = q, e_q = 8 + q; 120 pairwise
    bits, transitivity on all 3,360 ordered triples); PAR[c] (1 = odd); the start R[0]. Constants: cW above every carrier and even, K1 (5)
    below every carrier and odd (K0, K3 above cW never decide a comparison: they are in the P-set of every K1-play and only K1-plays have
    node K1).
  - Per state σ (all 16; the run picks them by a mux): RHO[σ][u], Odd's face at the ACTIVE gate of mover u (0 = e-face, 1 = β-face).
    SUCC[σ][u][·] one-hot over {0, 1, 2, 3, cW, K}: e-face → cW at level 0, → mover σ(u) at level 1 (option k W-points to mover k); β-face
    → XT of the active option (X → K). POS[σ][z][i][·], i = 0..4: the walk from mover z in this functional graph (forward implication
    plus at-most-one; cW and K absorb). CYC[σ][u] (u returns to itself within 4 steps), VIS[σ][z][u] (u among positions 0-3).
  - The value of a walk from mover z (= the play from z's active gate, mg106.play_value with the start's return closing the cycle):
    node = the ORD-largest active carrier of a visited cyclic mover, or cW / K1 at a terminal; P = the carriers of visited non-cyclic
    movers above the node (all of them at K1, none at cW); LEN = the first position of the node's mover (of the terminal), 0..4. Lengths in
    Γ3*'s edges are 5·LEN + 2 (carrier node), 5·LEN − 2 (cW), 5·LEN + 4 (K1): strictly increasing in LEN for a fixed node type, and LEN is
    compared only at equal nodes. A «prepended» value (gate → carrier c → target t, then t's walk): node and P of t's walk (cW: ∅; K1: ∅),
    plus c when c is above that node (always at K1), LEN + 1 (LEN 1 at a terminal target).
  - GT(a, b) («a ▷ b», SPEC S1's order as mg106.key): RW (rewards of the nodes: an even node's reward is its priority, an odd one's the
    negative; RG[n][n′] derived from PAR and ORD) or [same node and (top of P_a Δ P_b in P_a and even, or in P_b and odd) or (P_a = P_b
    and LEN smaller at an even node / larger at an odd node)]. The top of the symmetric difference is a TOP[c] variable per carrier
    (TOP → in exactly one set, TOP → no higher carrier in exactly one set, some TOP unless the sets are equal).
  - Odd's optimum (local optimality of RHO at the four active gates): for the face f ≠ RHO[σ][u], the prepended value of u's active gate
    with face f (carrier f, its target, then the walks under RHO) is NOT ◁ the value under RHO, i.e. ¬GT(value under RHO, value via f).
  - Availability: AV[σ][x] ⇔ GT(e-face play of x's inactive gate, value of x's active gate) ∧ GT(β-face play of the inactive gate, the
    same). An inactive gate lies on no play under RHO, so Odd's optimum there is the smaller of its two faces' plays, and «min ▷ v» is
    «both ▷ v».
  - The KEY run (mg106.abstract_run, §1's rule): R[j] (4 bits), j = 0..LEN; AVR[j][x] = AV[R[j]][x] by a 16-way selector; level 0:
    x moves iff AVR[j][x] and the other option's gate is lower in GO; PREF = 1 iff gate(0, R[j+1](0)) is not below gate(1, R[j+1](1));
    level 1: R[j+1](x) = PREF if AVR[j][x], else R[j](x). Length constraint: R[j+1] ≠ R[j] for j = 0, …, LEN − 1 (by KEY-MONO*, a run whose
    first LEN steps all change the state has L* ≥ LEN; conversely a run with L* ≥ LEN satisfies it).
  - Size: LEN = 6: 72,015 variables, 394,221 clauses (cnf106.py dimacs).
- **Lemma ENC (PROVED, lane; premises Claim MG (§2, lane, audited), RESULTS R36 (c) Lemma P1 for ONE-player games, applied to Odd's
  one-player game M_s through the duality [DUAL] of RESULTS R104 (a), and SPEC S1's order).** For fixed free data, the models of
  build(None) restricted to AV and R are exactly one: AV[σ][x] is the availability bit of Claim MG and R[0..LEN] are the first LEN + 1
  states of KEY(G*) (repeated after it stops). Hence build(LEN) is satisfiable iff some G* ∈ 𝓛*_2 has L*(G*) ≥ LEN.
  Proof. Fix the free data and σ. Given RHO, SUCC, POS, CYC, VIS and every value variable are functions of RHO (each is defined by an
  equivalence, or by forward implication plus at-most-one in a functional graph). The walk value is the VJ value of the play from the
  active gate in M_s (cycle closed at the first repeated mover, node the most relevant carrier on the cycle, P the more relevant ones
  before it, lengths as above), i.e. mg106.play_value; GT is mg106.key's order (reward, then the signed sum Σ ±2^rank over P, which is
  decided by the top of the symmetric difference since 2^rank dominates all lower powers, then the length by the node's parity).
  The local-optimality clauses say: no improving edge for Odd at an active gate, comparing the two pads' successor values under RHO
  (Lemma M of R36 (b): prefixing by the gate and the pads is strictly monotone, so comparing the plays through the faces is comparing the
  successors). M_s with the inactive gates removed is a one-player game for Odd (the movers' edges are fixed by σ). By P1 in its dual form
  ([DUAL]: Odd's optimum in G is Even's in the dual game, with ⊴ reversed), an Odd strategy with no improving edge is pointwise optimal,
  and Odd's optimal strategy has no improving edge; so models exist, and every model's walk values are THE optimal values of Claim MG
  (pointwise optima are unique as values). The inactive gate's value is the minimum of its two faces under the optimal play, so AV is
  Claim MG's bit. R follows by the run clauses, which are mg106.abstract_run's rule (box 106 §1; xrun audited against key105 in §2). ∎
- What the lemma does NOT say: nothing about N5 except through Claim MG and box 105's KEY-MODEL (both lane, unrefereed); the SAT side is
  certified independently of both by replaying a decoded genome on N5 (val105.py).

## 3b. Audit of the encoding (§3.3; DATA; aud106.py; out/aud106.out; run106.sh audit)
- aud106.py fixes a genome's free data by assumptions in build(None) (python-sat 1.9.dev15 solver «cadical195», incremental) and
  compares with mg106.py (the audited evaluator of §2). Counters (all must be 0): avfail (unit (genome, state, mover): the model's AV bit
  differs from mg106's), avfree (same unit, --full only: the opposite AV bit is also satisfiable, i.e. the CNF does not determine it:
  Lemma ENC's uniqueness), runfail (unit genomes: R[0..6] differs from mg106.abstract_run's first 7 states, padded with the last), unsat
  (unit genomes: no model). Sets: random genomes of ladder105's generator (seeds 1065 with --full, 1066), and the 40 climbed genomes of
  §2a (best/climb106_*.json, every one with L* = 5: the long runs) with --full. Controls (encoder mutations, env CTRL; each must fire):
  CTRL 1 availability ignores Odd's β-face at the inactive gate; CTRL 2 the length rule's parity reversed; CTRL 3 the node's parity reversed
  in the reward (this one makes Odd's local optimality unsatisfiable: it fires as «unsat», a weaker control, kept for the record).
- Output (out/aud106.out, six lines, inserted by script; run106.sh audit, 2 min 2 s, one core):
  «AUD106 seed 1065 genomes 300 full: (genome, state, mover) units 19200 avfail 0 avfree 0 runfail 0 unsat 0 | max L* 3»
  «AUD106 seed 1066 genomes 2000: (genome, state, mover) units 128000 avfail 0 avfree - runfail 0 unsat 0 | max L* 3»
  «AUD106 seed json genomes 40 full: (genome, state, mover) units 2560 avfail 0 avfree 0 runfail 0 unsat 0 | max L* 5»
  «AUD106 seed 1067 genomes 100 CTRL 1: (genome, state, mover) units 6400 avfail 2816 avfree - runfail 64 unsat 0 | max L* 2 | first (0, (0, 0, 0, 0), 1)»
  «AUD106 seed 1067 genomes 100 CTRL 2: (genome, state, mover) units 5056 avfail 1511 avfree - runfail 34 unsat 21 | max L* 3 | first (0, (0, 0, 0, 0), 0)»
  «AUD106 seed 1067 genomes 100 CTRL 3: (genome, state, mover) units 64 avfail 32 avfree - runfail 1 unsat 99 | max L* 1 | first (27, (0, 0, 0, 0), 1)»
- Reading: on 2,300 random genomes and the 40 climbed genomes with L* = 5, the CNF's availability bits (151,360 (genome, state, mover)
  units) and its runs (2,340 genomes, the longest of length 5) equal mg106's; on the 340 genomes of the --full sets every bit is
  determined (avfree 0 on 21,760 units), as Lemma ENC says. The three mutations fire (CTRL 1: avfail 2,816, runfail 64; CTRL 2: avfail
  1,511, runfail 34; CTRL 3: unsat 99 of 100). With §2's audit of mg106 against SPEC's engine (mgfail 0) this is the chain CNF = mg106 =
  key105 (SPEC on Γ3*); every SAT answer is in addition replayed on N5 itself (§3c).

## 3c. Controls of the certificate pipeline (Lead 2026-11-13 01:27Z; DATA; run106.sh controls; out/solve106.out)
- Pipeline (run106.sh, solve106.py): the CNF is written as DIMACS (sha1 printed; dump/*.cnf git-ignored, cnf106.py regenerates it) and
  solved by Glucose 4 through python-sat 1.9.dev15 with DRUP output. UNSAT: the proof is checked by TWO independent forward RUP checkers,
  L-COMP's drup.c (claude/l-comp 07cec8399, sha1 2d4b8eab…, the checker of RESULTS R112; read-only copy experiments/si/box71/ref) and
  REFEREE's ref_rup.c (claude/referee 2005aee7, sha1 707c484d…; deletions ignored), both compiled from source by the runner; then the CNF
  and the proof are REGENERATED from scratch in a temp dir and compared byte for byte; the proof is kept gzipped (dump/TAG.drup.gz).
  SAT: the model is decoded into a genome (best/TAG.json) and replayed by mg106.abstract_run (its L*) and by box 105's val105.py on N5
  itself from S3 (s3fail, keyfail, endfail, wrong, keymono, valmono).
- Note: python-sat 1.9.dev15's «cadical153» returned proofs that end without a refutation on g6 and c9 (49,802 lemmas all RUP, «s NOT
  VERIFIED: no refutation reached» at both checkers): not used for certificates; Glucose 4 is (as R112).
- Controls (as the Lead set them): «L* ≥ 5» on the whole class must be SAT with a replayed witness; «L* ≥ 5» on the climbed genome
  best/climb106_1.json (L* = 5, §2a) SAT and «L* ≥ 6» on it UNSAT with a checked proof; «L* ≥ 9» on the whole class UNSAT with a checked
  proof (the adversarial maximum is 8, §1). Output (out/solve106.out, inserted by script):
  «SOLVE106 c5 L* >= 5: SAT | vars 71972 clauses 393931 | cnf sha1 cc358fe65da5dea8a28e9ce2da4e1b88a744b6cf | solver glucose4 (python-sat 1.9.dev15) | 5.0 s | decoded L* (mg106) 5 | model run = mg106 run prefix True»
  «N5REPLAY106 c5: VAL105 c5.json mode free d 2: |V| 70 L* 5 (search: 5) Xi-graph cyclic | s3fail 0 keyfail 0 endfail 0 wrong 0 keymono 0 valmono 0»
  «SOLVE106 g5 L* >= 5 genome climb106_1.json: SAT | vars 71972 clauses 394117 | cnf sha1 6992411c0859a2ed4cb7c4c64095255b5f40109a | solver glucose4 (python-sat 1.9.dev15) | 0.2 s | decoded L* (mg106) 5 | model run = mg106 run prefix True»
  «N5REPLAY106 g5: VAL105 g5.json mode free d 2: |V| 70 L* 5 (search: 5) Xi-graph cyclic | s3fail 0 keyfail 0 endfail 0 wrong 0 keymono 0 valmono 0»
  «SOLVE106 g6 L* >= 6 genome climb106_1.json: UNSAT | vars 72015 clauses 394407 | cnf sha1 9a3074d764b601a4081b985b4af6793182df5814 | solver glucose4 (python-sat 1.9.dev15) | 0.2 s | proof lines 119364 sha1 cd65e1ffc9a852a907bd565c214f902a7d3a25ff»
  «CHECK106 g6 drup: s VERIFIED (89 lemmas RUP-checked)»
  «CHECK106 g6 ref_rup: s VERIFIED (89 lemmas RUP-checked, deletions ignored)»
  «REGEN106 g6 cnf equal yes proof equal yes»
  «PROOF106 g6 dump/g6.drup.gz bytes 512790 sha1 740a2fa61ffbb908a95d4cdf8e229bcae823f5b0»
  «SOLVE106 c9 L* >= 9: UNSAT | vars 72144 clauses 395091 | cnf sha1 321498e6e67047b7a99a54caa8f1066d55c21618 | solver glucose4 (python-sat 1.9.dev15) | 0.1 s | proof lines 2107 sha1 5e9c0b589760b6de5864bb49b3bc7aff9f5390cf»
  «CHECK106 c9 drup: s VERIFIED (730 lemmas RUP-checked)»
  «CHECK106 c9 ref_rup: s VERIFIED (730 lemmas RUP-checked, deletions ignored)»
  «REGEN106 c9 cnf equal yes proof equal yes»
  «PROOF106 c9 dump/c9.drup.gz bytes 14110 sha1 990187767a33a76f6ae1db99404eb18969bcd415»
- Reading: the pipeline finds a known witness (c5, decoded and replayed on N5 with L* = 5, all six counters 0), recovers the fixed
  genome's L* exactly (g5 SAT, g6 UNSAT with a proof both checkers verify), and refutes «L* ≥ 9» with a checked proof (a sanity bound,
  below the layer-1 maximum + 1). Both proofs regenerate byte-identically.
