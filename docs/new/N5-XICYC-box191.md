# Box 191 XI-CYCLIC: N5′-xi beyond REALIZE (L-NEW successor 59, Opus 5.5)
Written 2026-11-07 from 05:10Z (date -u at commit). Lead brief (BOX 191, D14 / D18 / D1, 12 h). D1 applies in full: N5′-xi stays a
CANDIDATE, wrong until it passes the TARGET.md §5 gauntlet. Labels: PROVED (lane, unrefereed) / CONJECTURE (data) / DEAD (instance) /
DATA / READING. G-N5-TIME stays OPEN. Nothing here is a TARGET.md claim.
Premises: RESULTS R15 (a) Lemma A (VJ00 Lemma 5.7: a non-empty unambiguous switch of improvements gives Ωσ ⊴ Ω_Switch pointwise) and
R15 (b) (length-only switches); VJ00 §4.2 (the order ⊴ on play values: the cycle node's reward first, then the path set, then the
length; source opened in the fleet, R15 cites it with sha256 485a12de…); R104's definition of Γ(G) (gamma3.build(G, {})); box 190's
N5′-xi definition (n5v.py) and P-N5-REACH's Γ3 (frozen packet, at the referees, NOT landed: used for DATA and for sketches only).
Tools: experiments/new/box191/ (check191.sh, frozen output check191.out; check.sh block «BOX 191 XI-CYCLIC»).

## 0. Answer
- (a) On Γ3(G) for EVERY genome (Ξ-cycles allowed), N5′-xi from S3 runs a MOVER PHASE of T steps, then exactly 3 core / fallback
  iterations. In the mover phase only movers change. There are no β escapes, τ is unchanged, and σ is unchanged off the movers. Each
  mover step is a HOWARD step: every mover goes to its VJ-best successor (HOWARD-EQ). The model is therefore IDEAL-CYC(G) := Howard
  (switch-best) strategy improvement at the movers of R104's Γ(G), with every other Even vertex frozen at R104's start and Odd best
  responding (§1).
  - REALIZE-CYC: CONJECTURE, with DATA and a partial proof.
  - Data: 22/22 state for state (8 L-RED Ξ-cyclic climb bests and 14 corpus genomes), with xi = T_CYC + 3.
  - Random genomes: 1,271 of 1,300 match exactly. All 29 others first diverge at an exact VJ tie, where xi breaks the tie by SPEC's
    key and the model keeps the current option.
  - SPEC N5 on the same 8 Ξ-cyclic instances also runs a mover phase, then 3 iterations. Its mover step is the root-first key rule
    inside TIE = A, not Howard.
- (b) Bounds in IDEAL-CYC (PROVED, lane, §2). Classify each step t → t+1:
  - C: some vertex's VJ cycle node Λ changes;
  - R: Λ is kept and Odd's optimal counterstrategy σ̄ changes at some vertex;
  - p: neither.

  Then:
  - CYC-COUNT: C ≤ n·(2M + 2), with n = N + 3M + 6.
  - BR-SEG: every maximal run of p-steps has ≤ N steps. Hence T_CYC ≤ C + R + (C + R + 1)·N.
  - ONEP-POLY: in the ONE-PLAYER model (gates forced to their β-face), R = 0, so T ≤ N·(n(2M+2) + 1) + n(2M+2): polynomial.
  - The acyclic IDEAL-XI bound T ≤ H ≤ N is the special case C = R = 0.

  So everything in N5′-xi's run on Γ3 is polynomially bounded except R, the number of steps at which Odd's best response changes.
  - DEAD: «path segments (Λ fixed) ≤ N» in the TWO-player model, by 3 instances (9 steps at N 8, 15 at N 14, 21 at N 18). The excess
    always sits at R-steps.
  - DEAD: ODD-FIXED («σ̄ constant on path segments») by the same instances.
  - Growth DATA (weak climbs): T_CYC ≤ 33 at N 20 (two-player) and 31 at N 24 (one-player), i.e. T ≲ 1.7 N. No super-linear sign.
  - The structure to hand to L-RED 53: GROWTH ⇔ MANY σ̄-CHANGES. On Γ the only Odd choices that move are the gate faces (β vs e).
    Friedmann's switch-all family shows that this is exactly where Howard's exponential runs live. On it (Howard, si.py engine, N 2-7)
    C = 0 always, R = 4, 10, 24, 54, 116, 241, T = 30, …, 1243, and the longest p-run is ≤ 19 ≤ nE.
  - Gadget hint: an Even-won Ξ-cycle closed by the movers, which Odd leaves through an e-face at one of its gates (§3).
- (c) Bridge, a REDUCTION (PROVED, lane, §4), not a claim. The IDEAL argument uses three properties of Γ:
  - (U1) TIE-FULL: the S4a arena's tie set contains a Ξσ-best successor at every Even vertex. Then N5′-xi's σ-step is a Howard step.
  - (U2) Odd's best response does not change (R = 0).
  - (U3) No cycle-node changes (C = 0: every play ends at the exit).

  For a general game, RED-XI states: if (X0) and (X1) hold along a run, then

  #iterations ≤ (n_E + 1)·(n(n−1) + R_σ + 1) + Q_τ.

  So «N5′-xi polynomial on the class where X0, X1 hold ⇐ X := R_σ and Q_τ polynomial». (X1) = U1 holds on Γ3 (HOWARD-EQ) but fails
  on general games: only 401/517 (n 12) and 333/570 (n 24) σ-steps of random games are Howard-faithful.

## 1. (a) N5 / N5′-xi on Ξ-cyclic Γ3(G): the mover phase and IDEAL-CYC
### 1.1 Data (experiments/new/box191/trace191.py, howard191.py, eq191.py, rand191.py)
- trace191.py prints, per state of a run on Γ3(G): the mover options, the β escapes (σ(β) = pb instead of the Ξ-target), the gates
  with τ on the β-face, the Even vertices changed off movers / β's, and the cycles of the chain graph x → xt(x, s(x)).
  - On L-RED R215's cyc_d6 (n 190, xi 22): states 0-19 change movers only, while the chain graph has cycles at every state; states
    20-21 change the core; state 22 is the fallback with every escape.
  - Odd's optimal counterstrategy σ̄ uses e-faces at some gates whenever chain cycles exist: up to 10 gates on cyc2_d7. In the acyclic
    corpus it never does (0 on all 14 genomes).
- HOWARD-EQ (DATA, howard191.py): at every mover-phase transition, σ_new at every mover = the Ξσ-best successor over ALL successors
  (ties: keep the current one), and σ_new = σ elsewhere: 22/22 genomes, every transition.
- REALIZE-CYC (DATA, eq191.py): the Γ3 mover sequence = idealcyc.run(G) state for state, and xi = T_CYC + 3, on 22/22 genomes.
  Random (rand191.py eq, d 1-5, width 1-3, degree 2-3, Ξ-target X with prob. 0.2):
  - seed 1: 297/300 exact;
  - seed 2: 974/1,000 exact;
  - every one of the 29 divergences starts at an exact VJ tie: the two choices have equal VJ keys in IDEAL-CYC's game.
- SPEC N5 on the 8 Ξ-cyclic instances: a mover phase (4-8 steps), then 3 iterations (1 fallback). Chain cycles are present at 4-9
  of its states.

### 1.2 The model (idealcyc.py)
IDEAL-CYC(G), for any genome G:
- The game is R104's Γ(G). Every Even vertex that is not a mover is frozen at R104's stated start (β → its Ξ-target, or u; core
  K0 → K3, K1 → K1, K3 → K2). Odd is free (gates: e-face or β-face; K2).
- A step moves every mover to a successor of ⊴-largest VJ value Ωσ (Howard / switch-best; ties: keep the current one, then the larger
  index). The run stops when no mover has a strictly better successor.
- This model replaces R104's key rule by Howard's rule and drops Ξ-acyclicity. On acyclic genomes it is IDEAL-XI (box 190; Fact X
  makes the best option unique).

### 1.3 Partial proof of REALIZE-CYC (READING / sketch; not PROVED)
- (i) TIE(x) = A_s(x) at every mover in any state of the phase where τ = the e-faces (τ0 under the pads). Reason: S4a's arena H keeps
  Odd on τ, so a play of H from a gate goes e → W-target. The W-graph is level-decreasing, so H never reaches a β-face. The proof of
  P-N5-REACH W3 (iii) / KEY3 (a) for «every option of a mover ties in H» uses only the W-faces, the e-priorities and the pads, never
  the Ξ-graph. So it transfers verbatim to Ξ-cyclic G (to be re-checked line by line by a referee).
- (ii) Given (i), N5′-xi's tie rule picks the Ξσ-best element of A_s(x). That is the Ξσ-best successor overall, since A_s(x) holds
  every strictly better one. This is HOWARD-EQ.
- (iii) NOT PROVED for Ξ-cyclic G: «τ stays e at every gate (S4b finds no Odd-improving switch), no β escape becomes improving, and the
  core is untouched until the stop». In the acyclic case these are P-N5-REACH's TAU3 / ESC3 / K3 lemmas, and their proofs use Ξ-chains
  ending at X. DATA: they hold on all 22 + 1,300 runs (they are part of the phase definition, and the phase covered the whole IDEAL-CYC
  run every time).
- So REALIZE-CYC = (i) + (ii) PROVED-sketch + (iii) CONJECTURE. Exact match also needs the tie rule: SPEC's key at exact VJ ties.

## 2. (b) Bounding IDEAL-CYC (PROVED, lane)
Notation: Ω_t = VJ00 value of σ_t against the optimal counterstrategy σ̄_t, where σ̄ is any fixed deterministic choice of an optimal
counterstrategy (si.py Engine); Ω_t(v) = (Λ_t(v), Π_t(v), k_t(v)), with ext(v, (w, P, k)) := (w, P ∪ {v if v ≻ w}, k + 1). Facts:
- (F1) Ω_t ⊴ Ω_(t+1) pointwise (R15 (a): a Howard step is Switch_I with I = the switches made, a non-empty unambiguous set of
  improvements).
- (F2) ⊴ compares the reward of Λ first, and distinct vertices have distinct rewards (VJ00 §4.2).
- (F3) If Λ_t(v) ≠ v, then Ω_t(v) = ext(v, Ω_t(next)), with next = σ_t(v) for Even v and σ̄_t(v) for Odd v; also Ω_t(w) = (w, ∅, 0)
  when Λ_t(w) = w.
- (F4) ext(v, ·) is ⊴-monotone and strictly monotone. With equal Λ, adding v to both sets leaves the symmetric difference unchanged,
  and both lengths grow by 1.
- (F5) Howard: σ_(t+1)(x) is a ⊴-best successor under Ω_t, and σ_(t+1)(x) ≠ σ_t(x) only if it is strictly better.
- (F6) In Γ(G) every mover has priority 0, so it is never the cycle node of its own play (every cycle passes a β or an e of positive
  priority). Every non-mover Even vertex has one successor in IDEAL-CYC.

DOM. For every mover x, every t and every successor y of x: Ω_(t+1)(x) ⊵ ext(x, Ω_t(y)).
Proof: Ω_(t+1)(x) = ext(x, Ω_(t+1)(σ_(t+1)(x))) by F3 and F6. This is ⊵ ext(x, Ω_t(σ_(t+1)(x))) by F1 and F4, which is ⊵ ext(x, Ω_t(y))
by F5 and F4. ∎

STRICT. If σ_(t+1)(x) ≠ σ_t(x), then Ω_(t+1)(x) ▷ Ω_t(x).
Proof: by DOM, Ω_(t+1)(x) ⊵ ext(x, Ω_t(σ_(t+1)(x))). By F5 and F4 that is ▷ ext(x, Ω_t(σ_t(x))), which equals Ω_t(x) by F3 and F6. ∎

PATH. Let (Λ_t, σ̄_t) be constant on the states a..b. Let π: z_0 → … → z_L = w be a simple path in the graph whose Odd vertices keep
only their σ̄_a-edge and whose frozen Even vertices keep their one edge, with Λ_a(z_i) = w for all i and Λ_a(w) = w. Let μ(π) be the
number of movers among z_0..z_(L−1), and val(π) := ext(z_0, ext(z_1, … ext(z_(L−1), (w, ∅, 0)))). Then Ω_t(z_0) ⊵ val(π) for every
t ∈ [a, b] with t − a ≥ μ(π).
Proof by induction on L.
- L = 0: Ω_t(w) = (w, ∅, 0), since Λ_t(w) = Λ_a(w) = w (F3).
- z_0 a mover: by induction Ω_(t−1)(z_1) ⊵ val(tail), since t − 1 − a ≥ μ − 1. DOM and F4 then give
  Ω_t(z_0) ⊵ ext(z_0, Ω_(t−1)(z_1)) ⊵ val(π).
- z_0 not a mover: Λ_t(z_0) = w ≠ z_0, so F3 gives Ω_t(z_0) = ext(z_0, Ω_t(z_1)), because the edge is frozen or σ̄_t(z_0) = σ̄_a(z_0).
  Induction at the same t with μ unchanged, plus F4, finishes. ∎

BR-SEG. If (Λ, σ̄) is constant on the states a, …, a+j+1 and step a+j → a+j+1 changes σ, then j ≤ N − 1. So every maximal run of
p-steps has ≤ N steps.
Proof:
- Let x be a mover that switches. By STRICT, Ω_(a+j+1)(x) ▷ Ω_(a+j)(x).
- Let π be the prefix of x's play under (σ_(a+j+1), σ̄_(a+j+1) = σ̄_a) up to its first visit of w := Λ_(a+j+1)(x) = Λ_a(x).
- π is simple, and every vertex on it has Λ_a = w, since vertices on one play share its cycle node and Λ is constant. Its Odd edges
  are σ̄_a-edges. Iterating F3 gives Ω_(a+j+1)(x) = val(π), and μ(π) ≤ N.
- If j ≥ N, PATH at t = a + j gives Ω_(a+j)(x) ⊵ val(π) = Ω_(a+j+1)(x): a contradiction. ∎

CYC-COUNT. By F1 and F2, Λ_t(v) can only change to a vertex of strictly larger reward. In IDEAL-CYC the possible cycle nodes are the
β's, the e's, c_W and the core's K1 / K2, so there are ≤ 2M + 3 of them. Hence C ≤ n·(2M + 2), with n = N + 3M + 6. ∎

THEOREM (T_CYC). T_CYC ≤ C + R + (C + R + 1)·N, since the C- and R-steps split the run into ≤ C + R + 1 maximal p-runs. ∎
- ONEP-POLY: if every gate is forced to its β-face, the only Odd choice left is K2. Its options' values depend on the core only, so
  R = 0 and T ≤ n(2M+2) + (n(2M+2) + 1)·N. ∎
- Acyclic sanity check: on G ∈ IDEAL-ACYC Odd always takes the β-face (R104's strict local preference) and every play ends at the
  exit, so C = R = 0 and T ≤ N. This is box 190's IDEAL-XI bound T ≤ H, up to H ≤ N.
- READING: the Bellman-Ford / «policy iteration dominates value iteration» pattern, carried over to VJ values. Its standard MDP form
  was NOT opened here: no citation, the proof above is self-contained.

General form (PROVED, lane, same proof). Howard VJ strategy improvement on ANY game, from any start: if every step switches some Even
vertex that is not its own cycle node at t and at t+1 (H0), then T ≤ C + R + (C + R + 1)·n_E with C ≤ n(n − 1).
DATA (brseg_gen191.py):
- 2,000 random games, n 12: the longest p-run is ≤ n_E in all of them; no H0 event.
- Friedmann's switch-all family (pgsolver_port.py switchallexp, Howard's exponential family):

  | N | T | C | R | longest p-run | n_E |
  | --- | --- | --- | --- | --- | --- |
  | 2 | 30 | 0 | 4 | 9 | 23 |
  | 3 | 70 | 0 | 10 | 11 | 32 |
  | 4 | 150 | 0 | 24 | 13 | 41 |
  | 5 | 310 | 0 | 54 | 15 | 50 |
  | 6 | 630 | 0 | 116 | 17 | 59 |
  | 7 | 1243 | 0 | 241 | 19 | 68 |

  READING: Howard's exponential runs there are runs of exponentially many Odd best-response changes. Nothing else grows.

### 2.1 Data
- seg1p191.py, 2,000 random genomes (seed 11), one- and two-player: longest Λ-free run ≤ N and C ≤ N·M in all of them.
- One-player climbs reach the BR-SEG bound exactly: r1_d5 has a 10-step run at N 10 (the bound is tight).
- DEAD SEG-2P («Λ-free runs ≤ N in the TWO-player model»), by three instances:

  | instance | N | longest Λ-free run | labels |
  | --- | --- | --- | --- |
  | inst/DEAD_SEG2P_d4_N8.json | 8 | 9 | ppppppppRC |
  | inst/DEAD_SEG2P_d7_N14.json | 14 | 15 | CCCCpRRRRppRRRpRppp |
  | inst/DEAD_SEG2P_d9_N18.json | 18 | 21 | pppRppRppRppRRRpppppp (C = 0) |

  Every excess run contains R-steps, as BR-SEG requires.
- DEAD ODD-FIXED: the same instances.
- Growth (climb191.py, hill-climb on T, 2-wide degree-2 ladders with Ξ-cycles, ≤ 20,000 mutations):

  | model | best T_CYC |
  | --- | --- |
  | two-player | 9 at N 6, 16 at N 10, 21 at N 14, 33 at N 20 |
  | one-player | 13 at N 10, 19 at N 12, 22 at N 18, 31 at N 24 |

  On Γ3, N5′-xi = T_CYC + 3, by REALIZE-CYC data. L-RED R215 reached xi 25 at N 16 (T_CYC 22). R stayed ≤ 9 in every climb best.
  READING: this climber is weak (box 190 caveat), so the data shows no super-linear growth but bounds nothing.

## 3. Hand-off to L-RED 53 (via the Lead): what must grow
- By the Theorem, a super-polynomial N5′-xi run on Γ3(G) needs super-polynomially many R-steps: steps where Odd's best response
  changes a gate face (β ↔ e) while no cycle node changes. Conditional on REALIZE-CYC (iii).
- In Γ, Odd takes an e-face (e has an even priority above every β, then goes to the W-target one level down) only when the β-face
  continuation is worse for Odd. That means an Even-won Ξ-cycle, or a path set carrying a large even e.
- Suggested gadget: Friedmann's «simple cycle» pattern transported into Γ. Even's movers close an Ξ-cycle whose top β is even; Odd
  leaves it through an e-face at one of its gates; the escape value through the W-chain encodes the «bit».
- What the gadget must survive:
  - the mover / gate / β / e shape;
  - e-priorities ordered by (level, gate);
  - W-targets exactly one level down;
  - REALIZE-CYC (iii): τ must stay e and no β escape may become improving. Check with eq191.py; a run that leaves the mover phase
    early is not an IDEAL-CYC run.
- Tools: idealcyc.py (fast model), subrun191.py (C / R / p labels), climb191.py (scores T, run, C; a score on R is a one-line change).

## 4. (c) Bridge to general games (REDUCTION, PROVED, lane)
- What the IDEAL argument uses: (U1) TIE-FULL, (U2) R = 0, (U3) C = 0. Ξ-cycles break U3 only through CYC-COUNT, which is polynomial
  anyway. They break U2, and U2 is the whole difficulty.
- DECOMP-G. For any N5′ (σ_new ∈ A(v) everywhere, so R15 (d) applies) on any game: #iterations = |S| + Q_τ, where S is the set of
  σ-changing iterations and Q_τ the number of iterations that keep σ (they change τ). R15 (d): every iteration changes σ or τ.
- RED-XI. Suppose that in a run of N5′-xi on G:
  - (X1) every iteration in S is a Howard step of σ (every Even vertex with a strictly better successor moves to a ⊴-best one, every
    other Even vertex keeps σ);
  - (X0) every iteration in S switches some Even vertex that is not its own cycle node before and after.

  Then the σ's at S form a Howard run (τ-only iterations do not change σ, and Ωσ does not depend on τ: R15 (d)), and the general
  BR-SEG gives |S| ≤ (n_E + 1)(n(n − 1) + R_σ + 1), with R_σ the number of S-iterations at which σ̄ changes. Hence
  #iterations ≤ (n_E + 1)(n(n − 1) + R_σ + 1) + Q_τ.
  So: N5′-xi is polynomial on every game where X0 and X1 hold ⇐ X := «R_σ and Q_τ are polynomial in n there». ∎
- On Γ3(G):
  - X1 holds in the mover phase (HOWARD-EQ: PROVED-sketch (i)+(ii));
  - X0 holds (F6);
  - Q_τ = 3 (DATA, REALIZE-CYC (iii));
  - so X reduces to «R polynomial in N + M on IDEAL-CYC».
- On general games X1 fails often (x1gen191.py): 401/517 σ-steps Howard-faithful at n 12 (395/500 games fully faithful), 333/570 at
  n 24 (116/300). Then N5′-xi's σ-step is a TIE-restricted best step, and DOM fails at the vertices where the best successor is outside
  TIE.
  - READING: a general proof along these lines needs either TIE-FULL, or a domination lemma for TIE-restricted steps (open).

## 5. Status and limits
- PROVED (lane, unrefereed): DOM, STRICT, PATH, BR-SEG, CYC-COUNT, Theorem T_CYC, ONEP-POLY (on IDEAL-CYC), the general BR-SEG form
  (Howard, H0), DECOMP-G, RED-XI.
- PROVED-sketch: HOWARD-EQ parts (i)+(ii).
- CONJECTURE (data): REALIZE-CYC (iii).
- DEAD (instances in inst/): SEG-2P; ODD-FIXED.
- OPEN:
  - is R polynomial on IDEAL-CYC? A yes would kill the tower route for N5′-xi on all genomes; a no would be L-RED's target.
  - X on general games. G-N5-TIME OPEN; N5′-xi stays a CANDIDATE.
- Literature (READING, source opened in this box): Asadi, Chatterjee, de Raaij, «Lower Bound on Howard Policy Iteration for
  Deterministic Markov Decision Processes», arXiv 2506.12254 (UAI 2025).
  - §1 and abstract: for Howard on mean-payoff DMDPs «the best known upper bound is exponential».
  - Thm 3.1: (n² + 7n − 6)/2 iterations on 2n vertices.
  - §3 / §6: Hansen's conjecture (iterations ≤ #edges) is open.
  - ONEP-POLY is for VJ discrete valuations, not for mean-payoff Howard, so it does not touch that open problem. Whether ONEP-POLY or
    the general BR-SEG is already in the literature is a question for L-LIT (not checked).
- Files (experiments/new/box191/):

  | file | role |
  | --- | --- |
  | trace191.py | traces a run on Γ3 |
  | howard191.py | HOWARD-EQ check |
  | idealcyc.py | the model; ONEP=1 for the one-player variant |
  | eq191.py | REALIZE-CYC check |
  | rand191.py | random genomes |
  | segs191.py, oddfix191.py, seg1p191.py, subrun191.py | step decompositions |
  | brseg_gen191.py | general games and families |
  | x1gen191.py | X1 on general games |
  | climb191.py, runclimbs.sh | resumable climbs; outputs in out/ |
  | inst/ | 8 L-RED Ξ-cyclic genomes (byte copies from claude/l-red b14066e1, experiments/red/r215/out/), 3 DEAD SEG-2P genomes, switchallexp N 2-5 (SHA1SUMS) |
