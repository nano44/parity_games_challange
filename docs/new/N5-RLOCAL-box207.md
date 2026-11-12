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
