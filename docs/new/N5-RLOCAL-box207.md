# Box 207 (D18): the feedback vertex R at k = 1 — a split of DEEP-k1, two dead race-flip charges, and the window outside R122 (L-NEW successor 71, Opus)
Written 2026-11-12 (date -u in the commit). Brief (Lead 05:45Z «go»): «RESEARCH (D18): DEEP-k1 via your predecessor's race-flip-at-R charge
… Aim for a lane lemma with its premises, or an exact obstruction with its instance.» Lead 06:29Z approved the plan, with three asks:
«(1) State exactly what R-LOCAL reduces DEEP-k1 to … A reduction that only renames the question must be labelled as one. (2) For (Q2):
R122 ACYC-LIN is landed, so quote it by script. Say exactly which of its premises the window model … meets and which it does not … (3)
Freeze CFI_s1 (sha1) and every DEAD-charge instance».
Labels: PROVED (lane, unrefereed) / CONJECTURE / DATA (unit, set, scope, counter) / DEAD / READING. Nothing here is a TARGET.md claim.
G-N5-TIME stays OPEN. N5′-xi stays a CANDIDATE (D1). Setting: IDEAL-CYC(G) (RESULTS R118 (a)); class_t(v) = (Λ_t(v), E_t(v)) and D^tot(v)
as in P-N5-QN §1 / R123; «loud» as in R123. A FEEDBACK VERTEX R of a genome with Ξ-feedback number k = 1 is a mover whose removal makes
the Ξ-graph acyclic (box202 fvs202). Tool: experiments/new/box207/rlocal207.py (definitions of every counter in its header); outputs
box207/out/; quotes207.py; check207.sh («BOX 207 RLOCAL» in experiments/new/check.sh).

## 0. Answer
- **The race-flip charge, in the two forms I could state, is DEAD** (§3): (D1) «each deep loud step (loud depth > 1) changes class(R)»
  dies on K1L10_n48 (5 of its 10 deep loud steps, for both of its feedback vertices); (D2) EFLIP-R «every step at which a gate flips to its
  e-face changes class(R)» dies on B400_r32 step 43 (two gates off R's play flip to e because their β-play newly reaches R).
- **Lemma R-LOCAL (PROVED, lane; elementary).** For every genome and every vertex R (any k): cut the run into the maximal R-WINDOWS
  (intervals of constant class(R)); there are exactly D^tot(R) of them, and with λ_max := the most loud steps in one window,
  D^tot(R) − 1 ≤ T_CYC and λ_max ≤ T_CYC, and T_CYC ≤ Q + (Q + 1)·L with Q ≤ D^tot(R)·λ_max (L of R123 QUIET).
- **What it reduces DEEP-k1 to (ask 1) — a SPLIT, labelled as such, not a reduction to an easier question:** on any family of k = 1
  genomes, with R a feedback vertex, T_CYC (equivalently Q_(>c), LOUD-SPLIT; equivalently D_mov, Theorem EQ) is polynomial iff BOTH
  (Q1) D^tot(R) is polynomial and (Q2) λ_max is polynomial. (Q1) is the single-vertex case of Theorem EQ's D_mov at R, so DEEP-k1 ⇒ (Q1);
  (Q1) alone is STRICTLY WEAKER than DEEP-k1 in this sense: no bound T_CYC ≤ f(N + M)·g(D^tot(R)) with f fixed independent of the run
  structure follows from (Q1) — the converse needs (Q2), and CWR(n) has D^tot(R) = 3 at n = 4, 8, 16 while T_CYC = 28 / 52 / 100 (§4).
  Whether (Q1) ⇒ DEEP-k1 in the polynomial sense is OPEN (it is equivalent to «(Q1) ⇒ (Q2)»; no k = 1 family with super-polynomial T is
  known either way). Neither half is known to be easier than DEEP-k1; R-LOCAL relocates the question, it does not shrink it.
- **(Q2) is NOT covered by R122 (ask 2).** R122's Lemma BETA-ACYC / Theorem ACYC-LIN need «a genome G whose Ξ-graph is acyclic»; the window
  model fails exactly that hypothesis (the Ξ-graph still has its cycles through R; R stays a mover and may switch inside a window; read as a
  terminal, R carries a class (K1, ε) with ε ≠ ∅, which no R104 genome vertex X has). The conclusions fail inside a window: on CFI3_n48,
  window t = 4 … 18 (class(R) = (K1, {e_(33,0)}) throughout), gate (32, 0) flips to its e-face at t = 6 with neither face's play reaching R,
  and the window holds 8 R-labelled steps (ACYC-LIN: R = 0). So (Q2) is a CONJECTURE (R-INT), not a lemma (§5).
- DATA (§4): on every k = 1 record family, windows are short and constant in n (MWR(n), CW(n): λ_max 8, every vertex ≤ 2 class changes
  per window), and all the length sits in D^tot(R) (≈ T); on CWR(n) the opposite (D^tot(R) = 3, λ_max ≈ T); climbs at N 48 push λ_max to 22
  (RINT_n48, T 24, D^tot(R) 2). 1,000 random k = 1 genomes: λ_max ≤ 3.
- Frozen (ask 3): experiments/new/box207/inst/CFI3_n48.json (sha1 d55b20b8f00d0e4e08c606879c8c6ec44283e114; = the Lead's «CFI_s1»),
  inst/RINT_n48.json (sha1 35b48913a615d4c88f0eb69afc38e42ecb0ab0b0); DEAD-charge instances, already frozen: experiments/new/box206/inst/
  K1L10_n48.json (sha1 303545c072e7b8d90d6acaf1c3ee8160caeebdbf), experiments/new/box204/inst/B400_r32_a13d9661.json (sha1
  a13d9661f77652c62006f77daa64c5603258fe42); CWR: box206/inst/CWRR4_n / CWRR8_n / CWRR16_n.json (sha1 6970f1b9… / c11bc1c2… / 4cd707c7…).

## 1. Lemma R-LOCAL (PROVED, lane)
Premises (quoted by script: quotes207.py, out/quotes207.out, trunk docs/RESULTS.md at b3d7294c):
- [Q] RESULTS R118 (a) (setting; l. 13677-13678): «The game is Γ(G) with every Even vertex that is not a mover frozen at its start
  successor. Odd is unrestricted (gates and K2).»
- [Q] RESULTS R121 E-MON (l. 14480): «If Λ_t(v) = Λ_(t+1)(v), then E_t(v) ≤ E_(t+1)(v).»
- [Q] RESULTS R121's per-vertex form of R118 (e) (l. 14531): «Λ_t(v) takes at most 2M + 3 values, in increasing reward»
- [Q] RESULTS R123 Theorem QUIET (l. 15076): «every maximal window of quiet steps has at most L := (M + 1)(2M + 1)(N + 1) + N(n − 1) steps,
  n = N + 3M + 6»
Statement. For every genome G, every vertex R of Γ(G), the R-windows W_1, …, W_D (maximal intervals of states with constant class(R);
the step that changes class(R) is counted in the window it ends) and λ(W) := the number of loud steps whose step ends inside W:
(i) D = D^tot(R); (ii) D^tot(R) − 1 ≤ T_CYC and max_W λ(W) ≤ T_CYC; (iii) Q = Σ_W λ(W) ≤ D^tot(R)·max_W λ(W) and T_CYC ≤ Q + (Q + 1)·L.
Proof. (i) Λ_t(R) only moves to strictly larger reward (premise (e)), so each value of Λ(R) is taken on one interval; on it E(R) only rises
(E-MON) in a total order; so class(R) never returns to a value it left, and its values are taken on D^tot(R) disjoint consecutive
intervals: the windows. (ii) class(R) changes D^tot(R) − 1 times, each at a distinct step; λ(W) counts distinct steps. (iii) The windows
partition the steps 1 … T_CYC, so the loud steps are partitioned too: Q = Σ λ(W). The steps of the run are the Q loud steps and at most
Q + 1 maximal quiet windows, each of at most L steps (QUIET). ∎
- With P-N5-QN's Corollary QUIET-N (R126 when it lands) L may be replaced by N. Nothing here uses k = 1; the content at k = 1 is the
  choice of R (§0).
- Corollary (the split). On any family of genomes and any choice of one vertex R per genome: T_CYC is polynomial in N + M iff D^tot(R)
  and max_W λ(W) both are. (⇐ by (iii); ⇒ by (ii).) With LOUD-SPLIT (box 206, premise list as corrected in Addendum E) and Theorem EQ
  (box 204), the same holds for Q_(>c) and for D_mov.

## 2. Why R (READING)
At k = 1 every Ξ-cycle passes R, and by (k+1)-Λ (P-N5-QN §5) the cycle nodes are K1 and the top of the one cycle of Ξ_σ (through R). The
brief's charge («each deep loud step to a race flip at R») asks whether R's class height controls the run. §3 kills the two pointwise
forms; §4 shows on which side of the split each known family puts its length.

## 3. DEAD (with instances; rlocal207.py counters, out/rlocal207_records.out, scope: every vertex of Γ(G); per genome the feedback vertex
## with the smallest (cint, loudint))
- (D1) «Every loud step of loud depth > 1 is a step at which class(R) changes» (the race-flip charge, naive). Counter deepnoR (unit: loud
  steps of loud depth > 1 at which class(R) does not change). DEAD: K1L10_n48 deepnoR 5 (of Q_(>1) = 10, box 206 Addendum B), for each of
  its two feedback vertices (R = 28 and R = 46: the same steps 27-31; rlocal207 reports R = 28); also K1L7_n48 3, BLKX26_n48 2. The 5 on K1L10 are its end
  steps 27-31, p-steps (box 206 B1), after R's class has settled.
- (D2) EFLIP-R «every step with no Λ change at which some gate flips to its e-face changes class(R)» (the sharper form: in MWR(n) every
  flip to an e-face puts the gate on R's play and changes class(R); flips back to β do not). Counter efail (unit: such steps without a
  class(R) change). DEAD: B400_r32 (L-COMP 15; box204/inst/B400_r32_a13d9661.json), feedback vertex 83, step 43: gates (62, 1) and (86, 0)
  flip to their e-faces; at t − 1 neither face's play reaches R, at t their β-faces' plays do (a mover switched into R's basin after
  R's class changed at step 42); neither gate is on R's play (out/eflip207_B400.out). Also CFI3_n48 efail 5, RINT_n48 2, 1,000 random k = 1
  genomes (seed 712) efail 10.
- (D3, a DATA remark of mine withdrawn before writing) «class(R) never changes at a p-step of R118»: 0 on every record row, but 23 on the
  1,000 random k = 1 genomes (counter pR, out/rlocal207_rand_k1_s712.out). Not claimed.

## 4. DATA (rlocal207.py; must-0 counters rrep, ifail, qfail = 0 on every row; control RL_CTRL=1 on MWR4_2: rrep 8, ifail 1, qfail 1, fires)
Unit and scope: DR = D^tot(R) (states → classes of R); cint = max over windows and over every vertex of Γ(G) of its class changes in
the window; λ_max = max loud steps in one window; flipint = max flips of one gate in one window; Rint = max R118 R-steps in one window.
| genome (k = 1) | T | R | DR | cint | λ_max | flipint | Rint | deepnoR | efail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MWR4_2 / MWR8_2 / MWR16_2 | 30 / 54 / 102 | 47 / 83 / 155 | 10 / 18 / 34 | 2 | 8 | 2 | 2 | 0 | 0 |
| CW4_n / CW8_n / CW16_n | 30 / 59 / 114 | 47 / 83 / 155 | 12 / 38 / 92 | 2 | 8 | 2 | 2 | 0 | 0 |
| CWRR4_n / CWRR8_n / CWRR16_n | 28 / 52 / 100 | 47 / 83 / 155 | 3 / 3 / 3 | 2 | 19 / 43 / 91 | 1 | 1 | 0 | 0 |
| K1F21_n48 / K1F34_n84 | 31 / 52 | 28 / 83 | 22 / 35 | 2 | 6 | 1 / 2 | 1 / 2 | 0 | 0 |
| K1L7_n48 / K1L10_n48 | 37 / 31 | 28 | 19 / 15 | 2 | 8 / 7 | 2 | 2 / 3 | 3 / 5 | 0 |
| BLKX23_n48 / BLKX26_n48 | 28 / 33 | 28 | 23 / 21 | 2 | 2 | 2 | 2 | 0 / 2 | 0 |
| B400_r32 (three levels) | 49 | 83 | 34 | 3 | 4 | 2 | 2 | 0 | 1 |
| CFI3_n48 (climb, §4.1) | 24 | 29 | 3 | 4 | 11 | 3 | 9 | 0 | 5 |
| RINT_n48 (climb, §4.1) | 24 | 29 | 2 | 7 | 22 | 3 | 2 | 0 | 2 |
- 1,000 random k = 1 genomes (box202 k1srch202.mk, seed 712; out/rlocal207_rand_k1_s712.out): max DR 5, cint 2, λ_max 3, flipint 2,
  Rint 2 (T ≤ 6); TOTALS deepnoR 0, efail 10, pR 23, rrep 0, ifail 0, qfail 0.
- READING: two regimes. On MWR(n) and CW(n) every window is short (λ_max 8, fixed in n) and T grows with D^tot(R) (≈ T / 3 … T / 1.2):
  (Q1) carries the length. On CWR(n) R's class freezes after 3 values and the whole run (a linear lane) is one window: (Q2) carries it.
  Both are linear. Nothing super-polynomial on either side.
### 4.1 Climbs (scratch climbers over box203 aclimb203's mutations with AC_FREE=1, k kept = 1; logs out/climb207_*.log)
- Score (flipint, Rint, T), seed 1, from K1F21_n48, 4,000 iterations: final (3, 9, 24) = CFI3_n48 (frozen; the Lead's «CFI_s1»).
- Score (λ_max, cint, T), seed 2, from CFI3_n48, 4,000 iterations: final (22, 7, 24) = RINT_n48 (frozen); still rising at the end
  (19 at 3,046, 22 at 3,965). N 48 only: one size, nothing about growth.
- The mechanism in CFI3_n48's long window (out/window207_CFI3.out, out/window207_CFI3_class.out; trace206.py): class(R) = (K1, {e_(33,0)})
  for t = 4 … 18; a clock lane (movers 16, 15, …, 9 switch X → next, one per step) hooks onto mover 33, whose gate lies on R's play; the
  level-1 gates (32, 0), (46, 0), (31, 0), (30, 0) flip e then b as the lane passes, with neither face's play reaching R; R itself switches at
  t = 15, 16 without a class change.

## 5. (Q2) against RESULTS R122 (ask 2)
- [Q] R122 Lemma BETA-ACYC (l. 14744): «for every genome G whose Ξ-graph is acyclic, on Γ(G) or Γ3(G), and every Even strategy that agrees
  with the stated start off the movers (transported through the pads on Γ3), every optimal counterstrategy of Odd takes the β-face at every
  gate, and no play from a non-e vertex contains an e-vertex»
- [Q] R122 Theorem ACYC-LIN (l. 14744): «the Howard run of IDEAL-CYC(G) from any mover state has C = 0, R = 0 and T_CYC ≤ N»
- [Q] R122's premise list (l. 14744): «R104's definitions of the genome, the Ξ-graph, Γ(G) and its start only»
- The window model: the states of one R-window W of an IDEAL-CYC run of a k = 1 genome G, read as «Ξ-graph minus R, plus one terminal R of
  fixed class».
  - MET: «every Even strategy that agrees with the stated start off the movers» (IDEAL-CYC freezes every non-mover Even vertex at the start,
    R118 (a)); «from any mover state» (the window starts at some state of the run).
  - NOT MET: «a genome G whose Ξ-graph is acyclic». G's Ξ-graph has its cycles through R, and the window does not remove them: R is still a
    mover whose successor may change inside W (CFI3_n48: R switches at t = 15, 16, inside W = [4, 18]); class(R) is constant, its value is not.
    Read as a terminal, R is not an R104 genome vertex either: the only terminal R104 offers a Ξ-chain is X (β → u = K0 → K3 → K2 → K1,
    class (K1, ∅)), while R's window class is (K1, ε) with ε ≠ ∅ in every long window seen (CFI3: ε = {e_(33,0)}), and on CWR(n) (Λ(R),
    ·) = (β_(R,0), ·), an even cycle top.
  - The conclusions fail inside the window: CFI3_n48 W = [4, 18]: gate (32, 0) takes its e-face at t = 6 (BETA-ACYC: «takes the β-face at
    every gate»), neither face's play reaching R (out/window207_CFI3.out: eR [0, 0], bR [0, 0]); W holds 8 R-labelled steps (ACYC-LIN: R = 0).
- So (Q2) is not R122 in disguise. CONJECTURE R-INT (open): at k = 1, λ_max (the most loud steps inside one window of constant class(R)) is
  polynomial in N + M. DATA §4: 8 on MWR(n), CW(n) (constant in n), linear on CWR(n), 22 at N 48 by a climb. Status: a conjecture of the
  same kind as DEEP-k1 (R-LOCAL: DEEP-k1 ⟺ (Q1) ∧ R-INT).
- One sub-case that might be provable (READING, not tried to the end): windows with class(R) = (K1, ∅), where a play reaching R ends like
  a play reaching X as far as classes go. On the sets of §4 such windows hold 0 flips (scratch count: CFI3 3 steps, K1L10 1 step); they
  are short and rare, so a lemma there would not touch the long windows.

## 6. Status and next step
- PROVED (lane, unrefereed): R-LOCAL and its split corollary (elementary; premises R118 (a), R121 E-MON, R121's per-vertex R118 (e),
  R123 QUIET).
- DEAD: the race-flip charge in forms D1 (K1L10_n48) and D2 = EFLIP-R (B400_r32, step 43).
- CONJECTURE R-INT (Q2), and (Q1) «D^tot(R) polynomial at k = 1» (open; implied by DEEP-k1). DEEP-k1 ⟺ (Q1) ∧ R-INT (by R-LOCAL).
- Next (proposal): (Q2) is the k = 0 problem plus one terminal of fixed class that may be Even-favourable. A lemma for windows would need
  BETA-ACYC's induction with that terminal: Odd takes the e-face at g only if the β-side reaches R with a class that beats the e-side
  (FACE-TARGET), so the e-faces taken in a window are «paid» by R's fixed ε. The first test: does every e-face taken inside a window sit on a
  gate whose β-play reaches R or whose W-target's play contains an e-face so paid (a «paid chain» invariant)? CFI3's lane is the instance
  to check it on.

## Addendum A (L-NEW successor 71; Lemma PAID: at k = 1 every e-face Odd takes is anchored at R; written 2026-11-12 by date -u)
Lead 06:29Z approved box 207's plan; this addendum follows §6's «paid chain» test, which held, and gives its proof. Tool:
experiments/new/box207/paid207.py (counters defined in its header); outputs out/paid207_*.out; quotes by quotes207.py (all «[Q]» lines of
this file, trunk b3d7294c).
### A1. Statement
- Setting: G a genome with Ξ-feedback number 1, R a FEEDBACK VERTEX (a mover on every cycle of the Ξ-graph), t a state of IDEAL-CYC(G),
  plays under (σ_t, σ̄_t). A gate g is DIRECT at t if R lies on the play of e_g or on the play of β_g. For a gate g with σ̄_t(g) = e_g that
  is not DIRECT, next_t(g) := the gate of the first e-vertex on the play of β_g.
- **Lemma PAID (PROVED, lane).** At every state t and every gate g with σ̄_t(g) = e_g: if g is not DIRECT, then (i) Λ_t(e_g) = Λ_t(β_g) =
  K1; (ii) the play of β_g contains an e-vertex, so next_t(g) =: h exists, and σ̄_t(h) = e_h; (iii) E_t(e_g) <lex E_t(e_h). Hence the chain
  g, next_t(g), next_t(next_t(g)), … consists of gates at their e-faces with strictly rising E_t(e_·), and ends, after at most M − 1 steps,
  at a DIRECT gate.
- Premises: [DEF] = RESULTS R104's definitions of the genome and of Γ(G), read as (D1)-(D3) of P-N5-QN §1 (frozen l-new e252182d): (D1) the
  only in-edge of e_g is from g; (D2) E-DOM: every vertex more relevant than an e-vertex is an e-vertex, c_W, K0 or K3; (D3) the core is
  entered from outside only at u = K0; R118 (a) (IDEAL-CYC; frozen starts); R118 (h) LEVEL0; R123 B-ONLY, LOC-GATE, LOC-K2; [VJ] (the order ⊴,
  R118's premise, as read in P-N5-QN §1).
- [Q] R104 (l. 9864): «e of even priority above every β with one edge to the W-target or to the top even self-loop c_W»; and R104's start
  (l. 9864): «β → its Ξ-target (u when the target is X), K0 → K3, K1 → K1, K3 → K2»
- [Q] R118 (h) (l. 13607): «σ̄ takes the β-face at every level-0 gate in every state»
- [Q] R123 B-ONLY (l. 15076): «at every state t and every vertex v other than c_W and the e-vertices whose successor is c_W, Λ_t(v) is less
  relevant than every e-vertex»
- [Q] R123 LOC-GATE (l. 15076): «at every state t and gate g, Odd's optimal counterstrategy σ̄_t chooses the face of strictly ⊴-smaller value»
- [Q] R123 LOC-K2 (l. 15176): «At every state σ̄_t(K2) = K1 and Ω_t(K1) ◁ Ω_t(K2).»
### A2. Proof
Step 0 (cycles). Every cycle of a play is K1's self-loop, c_W's self-loop, or passes R. (a) No cycle contains an e-vertex f: its successor
on the cycle would be f's W-target m (a mover; if f's successor is c_W, the play stays in c_W's loop and f is not on a cycle), and m's
cycle node would be at least as relevant as f, against B-ONLY (m is not an exception). (b) In the core the strategies are K0 → K3 → K2 → K1
→ K1 (R104's start, frozen by R118 (a); σ̄(K2) = K1 by LOC-K2), so its only cycle is K1's loop, and by (D3) a play leaves no core vertex
for a non-core one. (c) Any other cycle consists of movers, gates and β's only: mover x → σ_t(x) = a gate (x, k) → β_(x,k) (not e, by (a))
→ its frozen successor, the Ξ-target xt(x, k) (a mover; a β to u enters the core). So it is a cycle x → xt(x, k) → … → x of the Ξ-graph,
and passes R.
Step 1 (i). Let σ̄_t(g) = e_g, g not DIRECT. By Step 0 each face's play ends in K1's or c_W's loop. c_W's only in-edges are from e-vertices of
level-0 options ([DEF]), and a play from a non-e vertex reaches such an e_f only through f (D1), where σ̄ takes β (LEVEL0). So β_g's play
never reaches c_W. If g were a level-0 gate, LEVEL0 would give σ̄_t(g) = β_g; so wt(g) is a mover, e_g's play continues from a non-e vertex
and never reaches c_W either. Hence Λ_t(e_g) = Λ_t(β_g) = K1.
Step 2 (core letters). Both plays end at K1, which they reach only through K0 → K3 → K2 (D3, Step 0 (b)); K0 and K3 are more relevant than K1,
so K0, K3 lie in Π_t(e_g) and in Π_t(β_g). c_W lies in neither.
Step 3 ((ii), (iii)). LOC-GATE: Ω_t(e_g) ◁ Ω_t(β_g). Both have cycle node K1, so [VJ] compares Π: with z the most relevant vertex of
Π_t(e_g) Δ Π_t(β_g), the side containing z is the larger iff z is even. e_g ∈ Π_t(e_g) (the first vertex; e above every β and K1).
- Case A, e_g ∉ Π_t(β_g). The Π's differ at e_g, so z = e_g or z is more relevant than e_g; by E-DOM and Step 2, z is an e-vertex, hence the
  most relevant element of E_t(e_g) Δ E_t(β_g), and even. Ω_t(e_g) ◁ Ω_t(β_g) puts z on β_g's side: E_t(e_g) <lex E_t(β_g).
- Case B, e_g ∈ Π_t(β_g). β_g's play passes e_g, so it passes g (D1) and continues as g's play. If the first e-vertex on β_g's play were e_g
  itself, the segment from β_g to g would hold only movers, gates and β's: a Ξ-path xt(g) → … → x, which with the edge x → xt(g) of option
  g closes a cycle of the Ξ-graph without R (R is not on β_g's play): impossible. So an e-vertex f precedes e_g on β_g's play; the play of
  e_g is a suffix of it (both plays simple up to K1), so E_t(β_g) ⊇ E_t(e_g) ∪ {f} with f ∉ E_t(e_g); the difference lies in E_t(β_g)
  only, so its most relevant element does: E_t(e_g) <lex E_t(β_g).
In both cases E_t(β_g) ≠ ∅: (ii). Let f be the first e-vertex on β_g's play and h its gate (D1): h precedes f, σ̄_t(h) = f = e_h, the part
of the play before h has no e-vertex, and from h on the play is h · (e_h's play), with the same cycle node K1; h is a gate, of priority 1,
not in Π. So E_t(β_g) = E_t(e_h), and (iii) follows from Cases A / B.
Step 4 (chain). Along g_0 = g, g_(i+1) = next_t(g_i) (while g_i is not DIRECT), E_t(e_(g_i)) strictly rises in a total order, so the g_i are
distinct; there are M gates, so a DIRECT gate is reached after at most M − 1 steps. ∎
- Remarks. (1) Nothing but Step 0 uses k = 1: for any k, with R replaced by a feedback vertex set F of the Ξ-graph and DIRECT meaning
  «a face's play meets F», the same proof gives the same chain. (2) For a Ξ-acyclic genome take F = ∅: no gate is DIRECT, so no chain ends,
  so no gate is at its e-face at any state: R122 BETA-ACYC's first clause on Γ(G) (consistency, not new; it uses LEVEL0, which R122 does not).
### A3. DATA (paid207.py; unit (state, gate at its e-face); scope every gate; R = the first feedback vertex in index order)
- Must-0 counters nonext (A1 (ii) fails), notK1 ((i)), notE (next(g) not at its e-face), lexfail ((iii)), nochain (chain does not end at a
  DIRECT gate): 0 on every row.
  | set | e-gate cases | DIRECT | longest chain |
  | --- | --- | --- | --- |
  | MWR4_2, MWR8_2, CW8_n, CWRR8_n, K1F21_n48, K1F34_n84 | 109, 301, 284, 22, 93, 278 | all | 0 |
  | K1L7_n48, K1L10_n48, BLKX23_n48, BLKX26_n48 | 142, 129, 89, 113 | 73, 44, 57, 75 | 1, 2, 1, 1 |
  | B400_r32, CFI3_n48, RINT_n48 | 293, 48, 98 | 292, 36, 64 | 1, 1, 1 |
  | 1,000 random k = 1 genomes (box202 k1srch202.mk, seed 714) | 3,512 | 3,444 | 1 |
  (out/paid207_records.out, out/paid207_rand_k1_s714.out.)
- Control PAID_CTRL=1 (R replaced by the next mover that is not a feedback vertex; out/paid207_ctrl.out): MWR4_2 lexfail 31, nochain 109;
  CFI3_n48 lexfail 21, nochain 48 (fires).
### A4. What PAID gives, and what it does not (READING)
- It is the k = 1 form of BETA-ACYC: Odd's e-faces exist only because of R, each one either meeting R directly or resting, through a rising
  chain, on one that does. On MWR(n), CW(n), CWR(n), K1F21 and K1F34 every e-face taken is DIRECT; chains (length ≤ 2) appear on the climbed
  genomes.
- It bounds nothing yet: a DIRECT gate's choice still depends on its faces' classes, which change with the movers. For (Q2) (R-INT) the use
  would be inside a window: there R's class is fixed, so a DIRECT gate whose two face plays both pass R compares the parts BEFORE R only
  (the common suffix's E(R) cancels). Next step (proposal): split the e-gates of a window by «both faces through R» / «one face through R»
  / chained, and test whether flips inside a window happen only at the last two kinds (CFI3's window flips are at gates with neither face
  through R at t = 6, so those are chained or β-side-through-R cases: to be checked).

## Addendum B (L-NEW successor 71; Lead 07:58Z: «Label it CANDIDATE until the proof is written in full with its premises quoted by script. Give the exact statement of [VJ] with E-DOM that you use and its landed source. Name the strict-lex-cycle step's premise.»; written 2026-11-12 by date -u)
- LABEL (governs Addendum A where they differ): Lemma PAID is a **CANDIDATE** (the Lead's rule). Addendum A2 writes the proof in full; with
  this addendum every premise it uses is quoted by script from landed RESULTS (quotes207.py, all «[Q]» lines of this file) or named with
  its landed source. I propose PROVED (lane, unrefereed) on the Lead's check; until then CANDIDATE.
- [VJ], the exact statement used (only its first two clauses; the length clause never decides in A2): for values Ω = (Λ, Π, k) and
  Ω′ = (Λ′, Π′, k′) of two vertices at one state: (VJ-1) if Λ ≠ Λ′, Ω ◁ Ω′ iff reward(Λ) < reward(Λ′); (VJ-2) if Λ = Λ′ and Π ≠ Π′, let z be
  the most relevant vertex of Π Δ Π′; then Ω ◁ Ω′ iff (z ∈ Π′ and z is even) or (z ∈ Π and z is odd). «Most relevant» refers to the
  relevance order, a linear order on the vertices (higher priority more relevant; on Γ(G) every e-vertex has its own priority). Landed
  source: RESULTS R118's premise list (l. 13607 at trunk 07139249), quoted:
- [Q] «VJ00 §4.2 / Friedmann arXiv 1106.0778 §3 for the order ⊴ on values (Λ, Π, k)»
  (the same order is R126's [VJ], landed at trunk 07139249). A2 uses VJ-2 once, in Step 3, at Λ = Λ′ = K1.
- E-DOM, the exact statement used: every vertex more relevant than some e-vertex is an e-vertex, c_W, K0 or K3. Landed source: RESULTS
  R121's record (l. 14481 at trunk 07139249), quoted:
- [Q] «Every vertex more relevant than some e-vertex is an e-vertex, c_W, K0 or K3, by [DEF]»
  A2 Step 3 uses it to conclude that z, being e_g or more relevant than e_g, is an e-vertex once c_W (in neither Π) and K0, K3 (in both Π's,
  Step 2) are excluded.
- The order on e-sets used in (iii) and Step 4: R121's lexicographic order, quoted:
- [Q] «sets of e-vertices compared lexicographically by their most relevant differing element»
- Premise of the strict-lex-cycle step (A2 Step 4): this order is a STRICT TOTAL ORDER on the subsets of the e-vertices. Reason: the
  relevance order is linear (VJ-2's premise above), so two distinct sets have a unique most relevant differing element, which lies in
  exactly one of them; then «S < S′ iff that element lies in S′» is irreflexive, total on distinct sets and transitive (the standard
  lexicographic order on 0/1 vectors indexed by a linear order). So a sequence E_t(e_(g_0)) < E_t(e_(g_1)) < … has pairwise distinct terms,
  the chain's gates are pairwise distinct, and it has at most M terms. No other premise enters Step 4.
- Quote check rerun: quotes207.py at trunk 07139249 (out/quotes207.out).
