# N5-EXIT (box 22): exit changes per phase, EXIT_x. Odd's value pushes only go down the routing forest, and that part is self-limiting. What drives the rest is Even re-routing and leapfrogs between incomparable branches
L-SI successor 18 (Opus 5.5; D18, Lead reading L40). Lead's GO 17:19Z, queue item 1: «EXIT_x per phase, classified by cause in the R72 / R69 /
GCX frame». Working note, unrefereed; not frozen. Not a TARGET.md claim. Nothing here bounds N5's running time; G-N5-TIME stays OPEN.
Labels (D18 / L40): PROVED (lane, unrefereed) / CONJECTURE / OPEN / DATA / READING / DEAD.
Tools: experiments/si/root/exitx.py (all counters below; MUT controls), climbexit.py. Logs: experiments/si/root/logs/exitx_*.txt.

## Summary
| § | item | label |
| --- | --- | --- |
| §1 | Lemma MONO-REF: off(z; m) = κ(z) − κ(m) never falls at a transition after which m is on z's honest play | PROVED, conditional on P-N5-OFFMONO §1 (in review) |
| §2 | Lemma PUSH: an Odd switch y1 → y2 with y1's class exit path fixed needs a strict rise of off(p1; m) for EVERY class terminal m on y2's new play (p1 = the old exit), unless a tie at t + 1 | PROVED, same condition |
| §2 | Corollary NO-UP: Odd never moves by such a switch into the subtree of its old exit (new exit routes through the old one), except at a tie at both ends | PROVED, same condition |
| §3 | Lemma EXIT-RHO: off honest cycles, every exit change of x is a ρ event at x or follows a tie at t | PROVED (landed premises + a proof step of OFFMONO, restated) |
| §4 | Lemma DEPTH: transitions whose exit changes are all DOWN (towards c in the routing forest) number ≤ (k² − k)(1 + the other exit-change transitions) | PROVED (elementary) |
| §4 | Corollary EXIT-RED: exit-change transitions ≤ (k² − k + 1)(1 + RR_c + DJ_c + TIE2_c + CYC′_c) | PROVED; VACUOUS in data (RR_c ≈ phase length) |
| §5 | data: 10 long instances, lib41, 4,000 random games; every check 0 violations; controls bite | DATA |
| §6 | what is left: Even's exit-changing re-routings and DISJ leapfrogs; growth at fixed k is linear (L-RED's mkpp, mkgate) | READING + DATA |
| §7 | open items | OPEN |

## 0. Setting (every game; as P-N5-OFFMONO-box49 §0, frozen, sha1 d9705ac6, not edited)
A phase P of N5 (τ, λ constant; RESULTS R38 (a)), a cycle node c, U := U_c, Q := the Odd vertices of out-degree ≥ 2, Q_c := (Q ∩ U) ∖ {c},
T := Q_c ∪ {c}, k := |Q_c|. κ, κwt_c, s_c, next_t as in RESULTS R56's setting line. Facts used (RESULTS R56 (a), (d); stated in P-N5-FBPOLY-box41
§0.3): (Aκ) for z ∈ U ∖ {c}, next_t(z) ∈ U and κ_t(z) = κwt_c(z) + κ_t(next_t z); (A0κ) κ_t(c) = (0, 0); (M1κ) for valuations with cycle node c,
x ⊴ x′ ⇔ κ(x) ≤ κ(x′); (M2κ) κ_t(z) ⪯ κ_{t+1}(z) for z ∈ U at in-phase transitions; κ-Y-FORM_D (R56 (d)); (SW) every Even switch of N5 is to an edge
of Iσ (as listed in R72's landed premises).
- The honest s-play of z ∈ U is simple before c (P-N5-OFFMONO §1, via (Aκ) iterated). chain_s(z) := the T-vertices on z's honest s-play
  strictly after z, in order (it ends with c). For x ∈ Q_c, par_s(x) := the first vertex of chain_s(x) (P-N5-OFFMONO's routing vertex: the
  first vertex of Q ∖ {x} on the play before c, else c). The ROUTING FOREST F_s: x → par_s(x), rooted at c. Its ancestor relation is acyclic,
  because chains are T-vertices of simple plays.
- off_s(z; m) := κ_s(z) − κ_s(m) ∈ ℤ² (lexicographic order, compatible with addition).
- For y ∈ succ(x) ∩ U: its CLASS EXIT PATH and EXIT at s as in RESULTS R69 (the part of y's honest s-play strictly before the first vertex of
  Q_c ∪ {c}, and that vertex). An EXIT CHANGE at x at t → t+1: par_t(x) ≠ par_{t+1}(x); EXIT_x := their number in the phase (P-N5-OFFMONO §2).
  With p1 := par_t(x), p2 := par_{t+1}(x), an exit change is UP if p1 lies on p2's honest (t+1)-play (p1 = c included), DOWN if not UP and p2 lies
  on p1's honest t-play (p2 = c included), DISJ otherwise. CYC: x on its honest cycle at t or t + 1.

## 1. Lemma MONO-REF (PROVED, lane; conditional on P-N5-OFFMONO §1 Lemma OFFSET-MONO, unrefereed)
Statement. Let t → t+1 be an in-phase transition of P, z ∈ U ∖ {c}, and m ∈ T a vertex of z's honest (t+1)-play, m ≠ z. Suppose every vertex of
Q_c on that play from z (included) up to m (excluded) is on no honest cycle at t. Then off_{t+1}(z; m) ⪰ off_t(z; m).
Proof. Let x_1, …, x_h = m be the vertices of chain_{t+1}(z) up to m. For i < h, par_{t+1}(x_i) = x_{i+1} (x_i's (t+1)-play is a suffix of z's).
Telescoping: off_s(z; m) = off_s(z; x_1) + Σ_{i<h} off_s(x_i; x_{i+1}) for s = t, t + 1 (each side is a difference of κ-values at s).
- Each term i < h is ⪰ 0 at t → t+1 by OFFSET-MONO at x_i with p := par_{t+1}(x_i) (x_i ∈ Q_c, x_i ≠ c, on no honest cycle at t).
- The first term. If z ∈ Q_c, it is OFFSET-MONO at z (p := x_1 = par_{t+1}(z)). Otherwise z ∉ T, and the part of z's (t+1)-play from z to x_1
  contains no vertex of Q (it lies in U, and its vertices before x_1 are not in T). OFFSET-MONO's Step 1 applies verbatim. Odd vertices
  outside Q have one successor. An Even vertex keeps its successor, or switches along Iσ_t ((SW)) to a successor in U, which is κ_t-larger by (M1κ).
  Backward induction from x_1 gives off_{t+1}(z; x_1) ⪰ off_t(z; x_1). Step 1 does not use where z's t-play went.
A sum of ⪰ 0 terms is ⪰ 0. □
- Remarks. (i) m = c gives (M2κ) back (κ(c) = (0, 0)). (ii) No hypothesis on z's t-play or on par_t: m need not have been on z's play at t.
  (iii) DATA (§5): 0 violations in 400,807 checks (every z ∈ U_c, every m on its (t+1)-play), control MRMUT=1 (m off the play) bites.

## 2. Lemma PUSH and Corollary NO-UP (PROVED, lane; conditional as §1)
Fact CL (a proof step of P-N5-OFFMONO §1, Step 2, Case L, from landed premises RESULTS R18 (d) Lemma S (a), R57 (a), SPEC S1, 1E-N3;
restated): let x ∈ Q_c be on no honest cycle at s, y′ ∈ succ(x) ∩ U with y′'s honest s-play passing x. Then κ_s(y′) = κwt_c(Z) + κ_s(σ̄_s x)
with κwt_c(Z) ≻ (0, 0), Z the cycle x → (y′'s play up to x). In particular κ_s(σ̄_s x) ≺ κ_s(y′).
Consequently (BEST): for x ∈ Q_c on no honest cycle at s and every y′ ∈ succ(x) ∩ U, κ_s(σ̄_s x) ⪯ κ_s(y′). If y′'s s-play avoids x, this is
κ-Y-FORM_D (y′ ∈ Y^x_s); otherwise it is Fact CL, strictly.
Statement (PUSH). Let t → t+1 be in-phase, x ∈ Q_c on no honest cycle at t and at t + 1, y1 := σ̄_t(x) ≠ y2 := σ̄_{t+1}(x), and suppose y1's
class exit path π1 and exit p1 (= par_t(x)) are the same at t and t + 1. Let m ∈ T lie on y2's honest (t+1)-play, with every Q_c-vertex of that
play before m on no honest cycle at t. Then off_{t+1}(p1; m) ⪰ off_t(p1; m), strictly unless κ_{t+1}(y1) = κ_{t+1}(y2).
Proof. By (Aκ) along π1 (the same path at t and t + 1): κ_s(y1) = κwt_c(π1) + κ_s(p1), s = t, t + 1. Then
  κwt_c(π1) + off_t(p1; m) = off_t(y1; m) ⪯ off_t(y2; m)        (BEST at t)
                           ⪯ off_{t+1}(y2; m)                 (MONO-REF at y2; if m = y2, both sides are 0)
                           ⪯ off_{t+1}(y1; m)                 (BEST at t + 1, with σ̄_{t+1}(x) = y2)
                           = κwt_c(π1) + off_{t+1}(p1; m).
The last "⪯" is strict unless κ_{t+1}(y2) = κ_{t+1}(y1). □
- Corollary P1UP (m = c): κ(p1) rises strictly at t → t+1, unless κ_{t+1}(y1) = κ_{t+1}(y2). (The exit-level form of RESULTS R72's CHOSEN.)
- Corollary NO-UP (m = p1): if p1 lies on y2's honest (t+1)-play (the new exit p2 routes through the old one, or y2's path meets p1 first),
  then all four "⪯" above are equalities: κ_t(y1) = κ_t(y2) and κ_{t+1}(y1) = κ_{t+1}(y2), a tie at both ends; and Fact CL's case does not
  occur at t. So by value pushes, Odd moves only DOWN (towards c in the routing forest) or DISJ, never UP. An UP exit change with σ̄(x)
  changed needs y1's class exit path or exit to change (an Even switch on it), a both-ends tie, or a Q_c-vertex on an honest cycle (CYC).
  With σ̄(x) unchanged, an exit change always needs an Even switch on y1's class exit path.
- Corollary PAIR (alternation of two fixed options). Let I be a run of in-phase transitions on which x stays off honest cycles, options y_A,
  y_B ∈ succ(x) ∩ U keep their class exit paths and exits A, B, and some m ∈ T lies on the honest plays of y_A and y_B at every state of I
  (m = c always qualifies), with the no-cycle hypothesis of PUSH. Then every switch of x from y_A to y_B on I comes with a strict rise of
  off(A; m), and every switch from y_B to y_A with a strict rise of off(B; m), ties at t + 1 excepted. So x switches between them at most
  1 + 2·min(R_A, R_B) times on I, where R_A is the number of strict rises of off(A; m) on I. If moreover A lies on y_B's play throughout
  (nested), there is at most one switch, from y_A to y_B, ties excepted (NO-UP). Proof: PUSH at each switch (m on the new option's play);
  switches between the two alternate. □
- DATA (§5): PUSH, checked at every m ∈ T on y2's (t+1)-play: 982 checks, 0 violations. The control PUSHMUT=1 (the rise demanded of p2
  instead of p1) bites on all 8 long instances with pushes (16 of 16 on nep90 ... 95 of 96 on pp_K48; logs/exitx_pushmut8.txt). NO-UP's hypothesis set never occurs (0 UP value pushes in all data, including ties). This agrees with the
  corollary, but it means the check is vacuous.

## 3. Lemma EXIT-RHO (PROVED, lane; landed premises plus Fact CL)
Statement. Let x ∈ Q_c be on no honest cycle at t and at t + 1, with par_t(x) ≠ par_{t+1}(x). Then κ_{t+1}(x) ≻ κ_t(x) (a ρ event at x), or
σ̄_t(x) ≠ σ̄_{t+1}(x) and κ_t(σ̄_t x) = κ_t(σ̄_{t+1} x) (a tie at t).
Proof. Case σ̄_t(x) = σ̄_{t+1}(x) = y1. The exits differ, so y1's honest play changes before p1 = par_t(x). Let w be the first vertex of y1's
class exit path at t whose successor changes. w is not Odd: Odd vertices outside Q have one successor, and the path holds no Q_c-vertex. So w is
Even, and by (SW) and (M1κ), κ_t(x′) ≻ κ_t(σ_t w) for x′ := σ_{t+1}(w). Hence κ_{t+1}(w) = κwt_c(w) + κ_{t+1}(x′) ⪰ κwt_c(w) + κ_t(x′) ≻ κ_t(w),
by (Aκ) and (M2κ). Backwards along the unchanged prefix from w to y1, (Aκ) at both times carries the strict rise to y1, then to x
(κ(x) = κwt_c(x) + κ(y1) at both times).
Case σ̄ changes, y1 → y2. κ_{t+1}(x) = κwt_c(x) + κ_{t+1}(y2) ⪰ κwt_c(x) + κ_t(y2) ⪰ κwt_c(x) + κ_t(y1) = κ_t(x), by (M2κ) and BEST at t.
Equality forces κ_t(y2) = κ_t(y1). □
- So EXIT_x ≤ ρ_x + TIE_x + CYC_x. Combined with P-N5-OFFMONO's CHAIN-COUNT (ρ_x ≤ |CYC_c| + Σ_{x′} D(EXIT_{x′} + |CYC_c| + 1), where the sum
  includes x′ = x), this is self-referential with coefficient D ≥ 1. The two lemmas do not close on each other (READING; §6).
- DATA: 0 violations; the tie alternative occurs (rho_tie = 3 on lib41, 2 and 3 on the random batches), so the check is not vacuous.

## 4. Lemma DEPTH and Corollary EXIT-RED (PROVED, elementary; no premise beyond §0's definitions)
Statement (DEPTH). Call an exit-change transition t → t+1 ALL-DOWN if every x ∈ Q_c with par_t(x) ≠ par_{t+1}(x) has par_{t+1}(x) on par_t(x)'s
honest t-play (p2 a strict F_t-ancestor of p1). Let N_dn be the number of ALL-DOWN transitions of the phase in class c, and N_ot the number of
the other exit-change transitions. Then N_dn ≤ (k² − k)(1 + N_ot).
Proof. Let anc_s(x) := the set of vertices of chain_s(x), and Φ_s := Σ_{x ∈ Q_c} |anc_s(x)|. Since anc_s(x) ⊆ T ∖ {x}, k ≤ Φ_s ≤ k². Φ changes
only at exit-change transitions. At an ALL-DOWN transition, par_{t+1}(x) ∈ anc_t(x) for every x (unchanged, or a strict ancestor of
par_t(x)). By induction along F_{t+1} from the root, anc_{t+1}(x) = {par_{t+1}(x)} ∪ anc_{t+1}(par_{t+1}(x)) ⊆ anc_t(x). For a mover, p1 ∉
anc_{t+1}(x) ⊆ {p2} ∪ anc_t(p2), because p2 ∈ anc_t(p1) and the ancestor relation of F_t is acyclic. So Φ drops by at least 1. At any other
transition it rises by at most k² − k. Summing over the phase: N_dn ≤ (Φ_first − Φ_last) + (k² − k)·N_ot ≤ (k² − k)(1 + N_ot). □
- Corollary EXIT-RED (PROVED). A non-ALL-DOWN exit-change transition carries an exit change at some x that is UP, DISJ or CYC. By §2 an
  UP one is (Even switch on σ̄_t(x)'s class exit path) or (both-ends tie) or (CYC′: a Q_c-vertex on an honest cycle at t or t + 1).
  Hence, with RR_c := transitions at which an Even vertex on the class exit path of σ̄_t(x) switches, for some x ∈ Q_c; DJ_c := transitions with a
  DISJ exit change; TIE2_c := transitions with a both-ends tie switch; CYC′_c := transitions with some x ∈ Q_c on an honest cycle at t or t + 1:
  N_ex := N_dn + N_ot ≤ (k² − k + 1)(1 + RR_c + DJ_c + TIE2_c + CYC′_c), and EXIT_x ≤ N_ex for every x.
- VACUOUS in data: RR_c is about the phase length (nep90 89 of 91, nep76 75 of 78, the n = 80 climb 91 of 100). Even switches on chosen class
  exit paths happen at almost every transition. Most of them keep the exit (same-exit offset rises, OFFSET-MONO's monotone part). EXIT-RED is
  recorded as a correct statement with no counting value. The finer reading in §6 replaces RR_c by the exit-changing re-routings.
- DATA: DEPTH 0 violations (Φ strictly drops at every ALL-DOWN transition); N_dn / N_ot ≤ 0.81 on every instance, far below k² − k.

## 5. DATA (experiments/si/root/exitx.py; logs root/logs/exitx_long10.txt, exitx_lib41_n34_rs2.txt, exitx_rand3000_s41.txt, exitx_rand1000_k6_s42.txt)
Checks (each must be 0): RT_V (an exit change with σ̄(x) fixed and no Even switch on its old class exit path), CHV_V (a pure-value exit change
with none of P1UP / VIAB / TIE), MR_V (MONO-REF), PUSH_V, NOUP_V, RHO_V (EXIT-RHO), DEPTH_V, RED_V (EXIT-RED). Controls: MRMUT=1 (m off the
play) and PUSHMUT=1 (the rise demanded of p2) bite.
| instance (start) | n | k | len | ΣEXIT | max EXIT_x | RT / CHV / CHR / CYC | NEX | Even switches (max per vertex) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| nep90_n40 (rund/instances/nep90_n40.start) | 40 | 5 | 91 | 53 | 18 | 19 / 13 / 21 / 0 | 3 | 202 (12) |
| nep76_n40 | 40 | 5 | 78 | 60 | 21 | 13 / 17 / 30 / 0 | 4 | 188 (12) |
| long121_n40 | 40 | 3 | 121 | 48 | 22 | 26 / 11 / 11 / 0 | 3 | 246 (12) |
| L-NEW's climbs (new/box48/out/qpcclimb/scale): best_qpc_nep90_s61 / nep76_s63 | 64 | 25 | 97 / 86 | 207 / 200 | 32 / 16 | 52/94/61/0, 30/86/84/0 | 4 | 217 (13 / 12) |
| snap_n80_s62 | 80 | 36 | 100 | 274 | 25 | 94 / 111 / 69 / 0 | 6 | 235 (11) |
| L-RED's pp_K12_n161 / pp_K48_n449 | 161 / 449 | 6 | 19 / 55 | 25 / 97 | 13 / 49 | 0 / 12 / 13 / 0, 0 / 48 / 49 / 0 | 3 | 125 (7) / 413 (25) |
| L-RED's gate_K16_n197 / gate_K64_n581 | 197 / 581 | 5 | 23 / 71 | 14 / 62 | 14 / 62 | 1/0/13/0, 1/0/61/0 | 4 | 158 (9) / 542 (33) |
- Logs: exitx_long10.txt (these ten, MR=1, -v), exitx_pushmut8.txt (controls), exitx_lib41_n34_rs2.txt, exitx_rand3000_s41.txt, exitx_rand1000_k6_s42.txt.
- ΣEXIT on nep90 / nep76 / long121 = 53 / 60 / 48 equals L-NEW's PARCHG (N5-KPOLY §2; reset.py, independent code).
- Directions. Odd value pushes (CHV): nep90 13 DOWN / 0 DISJ / 0 UP; nep76 15 / 2 / 0; n80 climb 58 / 53 / 0; pp_K48 0 / 48 / 0. Even-driven
  Odd moves (RT + CHR): UP 28 / 30 / 109 / 1, DOWN 12 / 11 / 44 / 0. Every exit change with σ̄ changed and y1's path fixed was pushed by a strict
  rise of κ(p1) (P1UP 100 %). Root of each push, following old exits down: an offset rise at a fixed parent (OFF) 12 / 13 / 76 of 13 / 17 / 111,
  chains of depth ≤ 2.
- Ping-pong. Returns to an exit used earlier in the phase: RET 45 of 53 (nep90), 206 of 274 (n80). Distinct exits per x ≤ 6. A trace on nep90
  (x = 1, 20 exit changes, exits 0 ↔ 11, where 0 routes through 11): x moves DOWN 0 → 11 by a value push each time off(0; 11) rises (CHV), and is
  pulled back UP by an Even switch on its chosen option's path (CHR / RT). That is nested ping-pong with 0 DISJ moves. pp_K48 is the
  opposite: every Odd and Even exit move is DISJ (the two leapfrogging risers).
- Per-exit offsets across pieces (CONJECTURE candidate PER-EXIT-MONO, off(x; p) never lower when x returns to p): DEAD as a candidate. It
  drops at 6 / 5 / 4 / 8 / 7 / 10 returns on the six nep-type instances (of 45-206 returns). Instance: nep90_n40 at its start (exitx.py
  counter PEM_drop_ret = 6).
- lib41 (n ≤ 34, S3 + 2 random starts, 715 phases): ΣEXIT 120, max EXIT_x 3; MONO-REF 224,811 checks, PUSH 98; all 0. Random 𝒞^kO (3,000 games, n 8-20;
  1,000 games with k = 6, n 14-30): phases ≤ 3 transitions, all checks 0 (thin).

## 6. READING: what is left, and growth at fixed k
- The exit-change count splits by direction. Odd's value pushes go DOWN or DISJ (NO-UP). DOWN-only stretches are paid by the depth potential
  Φ (DEPTH, factor ≤ k² − k). What feeds Φ back up is UP moves, and those are Even-driven (an Even switch that changes the exit of x's chosen
  option), ties, or cycles. So EXIT_x is controlled by two quantities. (a) EXIT-CHANGING Even re-routings of chosen options. These are Even's
  own exit moves; the same NO-UP argument shows nested choices are one-way for Even too, but in the other direction (towards deeper exits),
  as long as the abandoned successor's path is fixed. (b) DISJ leapfrogs between incomparable branches. PAIR bounds each leapfrog pair by
  the min of the two branches' rise counts. Both are Even-side counts. R69's ROOT already says every ρ event needs an Even switch on an
  exit path; this note says which Even switches can sustain exit changes: those that change an exit.
- No closure. EXIT-RHO puts EXIT_x inside ρ_x, and CHAIN-COUNT puts ρ_x inside Σ D·EXIT, with x's own term. A bound has to come from the
  Even side, i.e. from per-vertex Even switch counts in a phase. DATA: ≤ 12-13 per Even vertex on the nep-type instances (n 40-80), 25 / 33 on
  L-RED's pp_K48 / gate_K64.
- Growth at fixed k (DATA; L-RED's families, generated by experiments/red/usplit/mkpp.py, mkgate.py). pp: k = 6, max EXIT_x = K + 1 (13 at
  n = 161, 49 at n = 449). gate: k = 5, max EXIT_x = K − 2 (14 at n = 197, 62 at n = 581). Linear in n at fixed k, so no bound in k alone exists.
  Every rise in these families is driven by fresh content (a line per rise). No super-linear growth at fixed k is known to me. My climbs from
  random 𝒞^kO games (climbexit.py, n = 12, k = 2) found phases of length ≤ 3; that seed is too poor to say anything.
- Cross-field reading (no cited result is used). Inside one phase the honest frame is a deterministic two-player reach-c game with
  lexicographic weights. Even moves along improving edges and Odd best-responds. The two players' one-way rules on nested choices (Odd
  shallower, Even deeper) are the discrete analogue of "a dominated action stays dominated", the elimination step behind
  strongly-polynomial strategy-iteration bounds for discounted games. There, discounting makes the gap grow geometrically. Here nothing makes
  the leapfrog gap grow, and that is the missing ingredient. Sources not opened; READING only.

## 7. OPEN
- (1) EXIT-changing Even re-routings per phase, and DISJ leapfrogs per phase (§6). A bound on either in n and k is open.
- (2) A super-linear (in n) EXIT_x family at fixed k, or an argument that each leapfrog consumes fresh content (as in mkpp / mkgate).
- (3) NO-UP's tie case: a tie at both ends with a σ̄ change. It never occurred; N5's Odd tie rule would decide it.

## 8. The Even side (Lead 17:47Z): is an exit-changing Even re-routing self-limiting? It reduces to the classic count (written 18:01Z by date -u)
Script experiments/si/root/evenside.py (per-class C-intervals and C-cuts exactly as gcx.py; logs root/logs/evenside_long8.txt,
evenside_lib41_n34_rs2.txt).
- Lemma E-ONEWAY (PROVED, lane; conditional as §1). Even's nested switches are one-way, mirroring NO-UP. Let Even w ∈ U ∖ {c} switch a → b at
  t → t+1. Let e1 ∈ T be the exit of a, with a's class exit path π_a and exit e1 unchanged on [t, t′], and let e1 lie on w's honest play at
  every state of [t + 1, t′] (Q_c-vertices on it before e1 off honest cycles). Then w does not switch back to a at t′ → t′ + 1.
  Proof. Put h := κwt_c(w) + κwt_c(π_a) and g_s := off_s(w; e1). By (SW) and (M1κ), κ_t(b) ≻ κ_t(a). By MONO-REF at b (e1 on b's (t+1)-play),
  g_{t+1} = κwt_c(w) + off_{t+1}(b; e1) ⪰ κwt_c(w) + off_t(b; e1) ≻ κwt_c(w) + off_t(a; e1) = h. MONO-REF at w on each later transition keeps
  g ⪰ g_{t+1} ≻ h up to t′. A switch back at t′ needs κ_{t′}(a) ≻ κ_{t′}(σ_{t′} w), i.e. h = κwt_c(w) + off_{t′}(a; e1) ≻ g_{t′}. Contradiction. □
  DATA (evenside.py): 777 windows checked (129 on the eight long instances, 648 on lib41 with S3 + 2), 0 returns. Control E1MUT=1 (window
  conditions dropped): returns appear (10, 16, 7, 7, 22, 11 on six of the eight long instances), so the check is not vacuous.
  Unlike Odd's, Even's statement is about returns, not single moves. Even's choice is an improvement, not a best response, so a single
  shallower move is allowed (data: Even DOWN moves 26 / 38 / 64 / 41 on nep90 / nep76 / long121 / n80).
- What does limit Even. Inside a PURE C-interval (every gate D-direct; A non-increasing; D, offsets constant), the packet's reading
  (P-N5-GCX §5) makes S4a on U_c the abstract model's step. N5-ABSCYC-box22's Theorem ABS-DEPTH then says (under GEN) that U_c has no Even
  switch at index ≥ (|A_a| − 1) + |U_c| of the interval. By R69's ROOT that also means no ρ event and no exit change there. READING:
  conditional on the lift lemma (L1) and GEN.
  DATA: 0 such late switches (PURELATE = 0) in every pure interval. Largest index of an Even switch inside a C-interval, measured from the
  interval's start: pure 28 on lib41 and ≤ 5 on the eight long instances; impure 52 on pp_K48 (|U_c| = 449) and ≤ 3 on the others. In no
  interval, pure or impure, is an Even switch at index ≥ |U_c| − 4 (largest index − |U_c| = −4, on lib41). (An earlier draft of this paragraph
  quoted indices 96 / 52 / 67. They came from a bug in evenside.py's first version, which measured from the phase start instead of the
  run start. Fixed before this push; the logs are from the fixed code.)
- So Even's re-routing is self-limiting between C-cuts, and the count moves to the C-cuts K(S). The cuts are mostly Odd: a σ̄ change at a gate
  changes D (DCH) or a D-direct offset (OSB). DATA, cuts by kind (AG / DCH / OSB / DDSET / OVAL):
  | sample | transitions at cuts / inside | AG | DCH | OSB | DDSET | OVAL | exit-change transitions at cuts / inside |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | nep90_n40 | 74 / 10 | 15 | 19 | 38 | 2 | 0 | 31 / 2 |
  | nep76_n40 | 63 / 9 | 9 | 20 | 24 | 10 | 0 | 40 / 0 |
  | long121_n40 | 53 / 60 | 17 | 4 | 13 | 11 | 8 | 23 / 8 |
  | snap_n80_s62 | 77 / 16 | 34 | 22 | 10 | 7 | 4 | 63 / 3 |
  | pp_K48_n449 (impure) | 2 / 53 | 2 | 0 | 0 | 0 | 0 | 1 / 48 |
  | lib41 (n ≤ 34, S3 + 2) | 1,605 / 4,322 | 304 | 169 | 942 | 14 | 176 | 35 / 17 |
- Obstruction, named ALTERNATION (READING, plainly). After every Odd change at a gate, Even settles within about 2n steps (ABS-DEPTH; lift
  pending). But every Odd change at a gate is itself a C-cut that restarts Even, and every Odd change needs Even activity at the same
  transition (R69 ROOT; §2 PUSH). So the combined count is the number of Odd best-response changes at gates during Even's improvement.
  That is the classic policy-iteration quantity: how often the best response moves while the improver improves. No potential in this note
  breaks the cycle. DEPTH (§4) pays only for Odd's DOWN pushes; what feeds them is Even's exit changes on chosen options and DISJ leapfrogs,
  and both occur only in the windows that the cuts open.
  Instances: nep90_n40 (74 of 84 transitions are cuts, 57 of them Odd gate changes; 31 of 33 exit-change transitions at cuts); pp_K48_n449
  (the impure regime: 95 σ̄ changes at non-direct gates and 48 exit changes inside one C-interval).
- Consequence for the queue: the impure regime (gap (iv)) and the cut count are where the problem sits. L-RED's GCI-LEN (every global
  C-interval has length ≤ n − 1) is the pure-and-impure length statement. My ABS-DEPTH reading gives < 2n for pure intervals only.

## 9. OPEN ALTERNATION, stated precisely (Lead 18:08Z; written 18:26Z by date -u)
- Definitions. S is a λ_W-constant fallback-free run inside one phase, c a class, and C-intervals and cuts are per class as in P-N5-GCX §1
  (gcx.py / evenside.py).
  - ALT_c(S) := the transitions t → t+1 of S at which σ̄ changes at a gate of class c (u ∈ D_t ∪ D_{t+1}, u ∈ U_c), and either D ∩ U_c changes
    (DCH) or a D-direct offset changes (OSB).
  - K(S) = AG + DCH + OSB + DDSET + OVAL, summed over the cut kinds.
- OPEN ALTERNATION. Is ALT_c(S) bounded by a polynomial in n (and k = |Q_c|), uniformly over games and runs?
- Why it is the target.
  - Even's work between cuts is bounded: N5-GCILEN-box22 STATIC-DEPTH on σ̄-constant stretches; < 2n inside pure C-intervals by the
    ABS-DEPTH reading; data: no C-interval anywhere has an Even switch at index ≥ |U_c| − 4.
  - Exit changes sit at cuts (nep90: 31 of 33 exit-change transitions).
  - P-N5-GCX's UL-RED bounds U events and coarse W changes in K(S).
  - So on this route a bound on K(S), whose Odd part is ALT, bounds the run length. The other cut kinds: AG (A grows, G_c of P-N5-GCX)
    and the value cuts DDSET / OVAL.
- DATA (evenside.py; logs/evenside_long8.txt, evenside_lib41_n34_rs2.txt):
  | sample | ALT = DCH + OSB | all cuts K | transitions | max K in one run |
  | --- | --- | --- | --- | --- |
  | nep90_n40 | 57 | 74 | 84 | 12 |
  | nep76_n40 | 44 | 63 | 72 | 13 |
  | long121_n40 | 17 | 53 | 113 | 10 |
  | snap_n80_s62 | 32 | 77 | 93 | 14 |
  | lib41 (n ≤ 34, S3 + 2) | 1,111 | 1,605 | 5,927 | 19 |
  On the long instances ALT is about half to two thirds of the transitions. No family is known with ALT super-linear in n.
- Close known results (READING; sources opened: notes/L-SI.md "Sources opened"; ABSTRACTS ONLY, no theorem number checked; L-LIT
  should open the full texts before anything is cited):
  - arXiv 1106.0778, O. Friedmann, "An Exponential Lower Bound for the Latest Deterministic Strategy Iteration Algorithms". Its abstract
    reports exponential lower bounds for the variant that «computes the globally optimal improvement in each step», on parity, mean payoff,
    discounted and simple stochastic games.
    - S4a's step is a globally optimal improvement inside an arena: Even's W-optimum over the Ξ-improving edges, against a fixed τ.
    - So exponential ALTERNATION is not excluded by anything general. What is open is whether such a family fits inside ONE N5 phase
      (τ and λ_W constant; arena by Ξ, choice by W).
  - arXiv 1008.0530, T. D. Hansen, P. B. Miltersen, U. Zwick, "Strategy iteration is strongly polynomial for 2-player turn-based
    stochastic games with a constant discount factor". Its abstract gives O(m/(1−γ)·log(n/(1−γ))) iterations.
    - N5's lexicographic valuations are the γ → 1 regime, where that bound says nothing.
    - E-ONEWAY / NO-UP are elimination statements of the kind such proofs use ("an action, once left, is not retaken"), but without a
      contraction that makes the gap grow.
