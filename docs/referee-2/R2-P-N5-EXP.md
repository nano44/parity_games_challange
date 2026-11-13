# R2-P-N5-EXP: SECOND REVIEW of P-N5-EXP — the kill packet for candidate N5's gauntlet step 4 (Theorem EXP-IDEAL: L(G_k) = 2^k − 2 on 9k − 16 movers; Corollary EXP-N5: N5 from S3 makes at least 2^k − 1 iterations on Γ3(G_k), 135k − 230 vertices)
REFEREE-2 successor 41 (model as in the Lead's roster), 2026-11-13T14:16:52Z (date -u). Independent second referee (D1).
- Object (frozen; read at this commit only): claude/l-red-b 350d84eb6602003172d0d3dd67e0ef2d0c72d2f8, docs/red-b/P-N5-EXP.md, sha1
  c0449b17193f19619f33b366096762dfde27d542, 569 lines, 57,511 B; generator experiments/red-b/gk.py, sha1
  5222f555f9572e5c92119a2bc1e16d02008a96c5 (192 lines, read in full); docs/red-b/B6b-construction.md, sha1
  960ddf06fb3fc1306895c92af68f59b483da7b39 (history; NOT read: the packet [Q docs/red-b/P-N5-EXP.md@350d84eb] «To sign: §2 (Theorem
  EXP-IDEAL, Corollary EXP-N5), §4 (Lemma MEMBER), §5 (MOVE-2, K1-K4, V0-V4, WIRE), §6 (RESPONSE LEMMA, STABLE)» carries every proof).
  The lane's fixes file (a later commit) was NOT read before this report.
- Independence: docs/referee/ and notes/REFEREE.md were NOT read on this object (REFEREE 35 is first referee). No lane tool was
  imported by my checkers; the lane's engines appear only as an extra comparison (§3.4), named there.
- Owner rulings in force: [Q docs/DECISIONS.md@5d7aab0f] «A claimed polynomial algorithm is far more likely to be wrong than right.
  Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.» (D1; it applies both ways: a claimed
  KILL of the fleet's candidate is refereed like a claimed proof.) Lead reading L43 (docs/DECISIONS-INDEX.md): a «DEAD» of an
  asymptotic statement needs a refereed proof or an instance beyond an explicit bound.
- What this is: a referee report. A signature here is one of the two that CLAUDE.md's first hard rule asks for; the result is
  refereed-only (no Lean). Not a TARGET.md claim: nothing here is M3 or M4; the target statement stays open.

## 0. Verdict
| statement (packet §) | verdict | items |
| --- | --- | --- |
| Theorem EXP-IDEAL (a) = Lemma MEMBER (§4) | **SIGN** | M-1 (the rank clause of rule R needs its tie-break in the text) |
| Lemma MOVE-2 (§5) | **SIGN** | — |
| V0, V1, V2, V3, V4 (§5) | **SIGN** | — |
| K1, K2, K3, K4, WIRE (§5) | **SIGN** | — |
| RESPONSE LEMMA (§6) | **SIGN the statement**; its proof has gap G-1, closed in §2.4 of this report by the PREFIX form | G-1, W-1 |
| STABLE (§6) | **SIGN** | — |
| Theorem EXP-IDEAL (b), (c) (§7) | **SIGN** (through the RESPONSE LEMMA with G-1 closed) | G-1 |
| Corollary EXP-N5 (§2, §7) | **SIGN as PROVED-CONDITIONAL on RESULTS R117, Theorem REACH3, as landed** (refereed-only, with R117's standing premises); the sizes n = 135k − 230 and m = 176k − 300 SIGN outright | W-2 |
| «Dead end» paragraph (§2) | follows from the Corollary, so it carries the same condition; the wording must say so | W-2 |
| §8 (where the start and the orders are used) | checked against the proofs of K1-K4 and V1-V4: every order listed is used where §8 says. The sentence «Nothing else … is free» was tested only as far as §3.1 goes (gate renumbering, the rank tie-break) | — |
| §9 DATA | reproduced on my own code, §3 (same numbers at every point I ran) | D-1 |
| §10 | NOT run as written (the lane's script and archives); CHECKER's exact-commit re-run covers it | — |
| §11 | READING, not signed | — |

No error was found in the mathematics. No counter-instance, no failing counter. The two listed items change no number.

## 1. Items
- **G-1 (gap in the proof of the RESPONSE LEMMA; closed here; the statement is right).** Case (ii) applies the lemma to unit j + 1
  before the hypothesis (H2) of that application is known: [Q docs/red-b/P-N5-EXP.md@350d84eb] «provided its input stays (1, 1), which
  we check along the way» (l. 229). The input of unit j + 1 is (C_j, E_j). E_j depends on EY_j (V1), EY_j on the options of the
  observers y_j, ȳ_j (V2), the observers' moves on the key order D_j (K4), and D_j on the option of E(j + 1) (K2), a mover of unit
  j + 1 whose moves are the CONCLUSION of the application. So the lemma, as stated with (H2) on the whole window, cannot be used as a
  black box inside its own induction step. What the packet's step-by-step text proves, and what the induction needs, is the PREFIX
  form of §2.4 (hypothesis and conclusion both cut at a step τ_0), by an induction on τ_0 inside the downward induction on j. The
  stated lemma is the case τ_0 = the last step. Fix for the lane: state the prefix form as the induction hypothesis (text in §2.4).
- **M-1 (rule R, rank clause; harmless for the run).** §3 defines [Q docs/red-b/P-N5-EXP.md@350d84eb] «br of the β of (x, o) := the
  rank, among all options, of the pair (−depth(x), local δ of (x, o)), a wire counting as depth 2k + 5» and Lemma MEMBER says
  [Q docs/red-b/P-N5-EXP.md@350d84eb] «gate and br are ranks of injective keys». The br key is NOT injective for k ≥ 4: every wv_j
  has the pairs (−(2k + 5), 1), (−(2k + 5), 0) and every wu_j the pairs (−(2k + 5), 3), (−(2k + 5), 2), so 4k − 14 options share a
  key with an earlier one (2, 6, 10, … for k = 4, 5, 6, …; 0 at k = 3). gk.py breaks the ties by β-id (its line
  `order = sorted(rawrk, key=lambda b: (rawrk[b], b))`), and with that tie-break my generator reproduces the lane's files exactly.
  The run does not depend on the tie-break (§2.1, c6; tested with the opposite tie-break, counter tiebreak 0). Fix: add «ties broken
  by β-id» to §3 and to c6.
- **W-1 (wording).** §6 never says that «step t» is the IDEAL step s_(t−1) → s_t; (H1), (H2) and the proof use exactly that reading.
- **W-2 (status label of the kill).** The Dead-end paragraph says [Q docs/red-b/P-N5-EXP.md@350d84eb] «The claim "N5 (SPEC S1-S5,
  default start S3) runs in polynomial time" is FALSE.» That sentence is Corollary EXP-N5, which is proved THROUGH R117's Theorem
  REACH3. R117 is a landed, refereed-only result with standing premises (RESULTS R117, header: 1E-N3 = R57 (b); R24 (a) and (b) with
  R103's bridge B; R36 (c); R15 (d) for termination). So the sentence is PROVED-CONDITIONAL on R117 as landed, like every line that
  cites R117; the RESULTS line should carry «refereed-only, through R117» and not a bare «FALSE». See §4.
- **D-1 (defect of the frozen file).** §9.7 is the unfilled placeholder `QUOTESUMMARY` (l. 530). My own quote check is in §3.6.
- **O-1 (my own tool, not the packet).** My Γ3 builder (r2end.build, successor 34) numbers the β-vertices in GATE order. R104's packet
  says [Q docs/red/P-N5-REALIZE.md@5d7aab0f] «β_g: indices N + M, … (options in (x, k) order)». On G_k the two orders differ (on level 0 the gate order is (v_0, 1), (u_0, 0), (v_0, 0),
  (u_0, 1); e_j's gates are below u_j's although e_j is a later mover), so my game is the lane's .pg file with the β block permuted: an isomorphic game
  (β priorities are distinct; no vertex has two β successors, so no successor list changes its order). r2pg.py renumbers the block as
  R104 says: then my game EQUALS the lane's instance file index by index for k = 3..11, and N5 on that numbering makes the same run
  (§3.5). The lane's files are right; my earlier reports that used r2end.build compared games through name maps, never index by
  index, so their numbers stand, but the builder's header should say this (notebook).

## 2. Re-derivation (paper; every line of §4-§7 was redone, not read)
Notation as in the packet. E_j, EY_j, EY′_j are value orders under s (1 = the second mover of the pair is ahead); C_j, D_j, Z_j key
orders; a mover is value-enabled / key-enabled as in MOVE-2.
### 2.1 Lemma MEMBER, against R104's definition (P-N5-REALIZE §2 at trunk 5d7aab0f, l. 52-60, opened; the packet quotes it in full)
c1 levels 0..k all used, two options each: from the table (level k holds y_(k−2), ȳ_(k−2), y′_(k−2), ȳ′_(k−2) for k ≥ 4 and the top
observers; for k = 3 the level-3 movers are y_1, ȳ_1, y_2, ȳ_2). c2 GRADED: every row's W-targets are one level down (the row of
y_(k−1), ȳ_(k−1) at level k points to u_(k−1), v_(k−1); E(k − 1) = u_(k−1) is on level k − 1 = (k − 2) + 1 as the row of y_(k−2)
needs). R104's clause is per option, so a wire with one W-target twice is allowed. c3: by the table. c4: β-id 2i + o. c5: the numbers
100·lev + ε are distinct (inside a level the ε's of different movers are disjoint: 0/1, 2/3, 4/5, 6/7, 8/9, 10..13, 14..17 and, on
level k, 20..23 for the top observers; level 0 has 2/5 and 3/1), so their ranks are a bijection onto 0..M − 1. c6: see M-1; with
the tie-break br is a bijection; all parities 0. Why the tie-break cannot matter: a wire is no option's Ξ-target, so a wire's β lies
on the X-chain of that wire's own two options only; B_s(w, 0) Δ B_s(w, 1) is the two β's of w, and option 0 has the larger δ under
every tie-break; a wire's β's are below every other β (depth 2k + 5 is last) and occur in no other symmetric difference. c7: the
start column. c8: every Ξ-edge lowers the Ξ-depth by exactly one (u_j, v_j: 2j → 2j − 1; y_j, ȳ_j: 2j − 1 → 2j − 2, with u_0, v_0
at depth 0; y′_j, ȳ′_j: 2j → 2j − 1; e_j: 2j + 1 → 2j). Count: 2 + 2(k − 1) + (k − 3) + (k − 2) + (k − 3) + 2(k − 1) + 2(k − 3)
= 9k − 16. The RAW gate numbers 100·lev + ε are not onto 0..M − 1 and fail c5; the rule's text ranks them, and the ranked files are
the members. **(a) holds.**
### 2.2 MOVE-2 and the static facts
- MOVE-2 is R104's step read for a mover with two options: s′(x) is the key-least element of A_s(x); with A_s(x) = {o} nothing
  moves; with A_s(x) = {o, o′} the mover moves iff key(x, o′) < key(x, o), keys taken along the W-chains under s′ on the lower
  levels. Two facts make the later induction causal and I checked both on the table: (K-loc) no observer is a W-target, so a key
  depends only on the options of pairs, e's and wires of lower levels; (V-loc) values are read under the OLD state s.
- V0 (how every value comparison is decided). Ranks are depth-major: a β of SMALLER Ξ-depth outranks every β of larger depth, and
  every Ξ-edge lowers the depth by one, so along an X-chain the ranks INCREASE. All parities are 0. Hence for two chains: if they
  continue through different movers (of the same Ξ-depth, as in every use below), the top β of the symmetric difference lies in the
  tails (the two tails differ at least in the own β's of the two targets, which are of smaller depth than the heads), and the order
  of the chains is the order of the targets' values; if they continue through the same mover (or both end at X), the difference is the two head β's and the larger δ wins.
- V1 (E_j := [v_j ahead of u_j]). u_j's Ξ-targets are ȳ_j / y_j and v_j's are y_j / ȳ_j. Split pair (different options): the same
  observer follows, heads decide, δ(v_j, ·) ∈ {3, 2} > δ(u_j, ·) ∈ {1, 0}: E_j = 1. Aligned pair (both on o): different observers
  follow, so E_j is the order of the observers: at o = 0, v_j → y_j and u_j → ȳ_j, E_j = [EY_j = 0]; at o = 1, E_j = [EY_j = 1]:
  E_j = [EY_j = s(v_j)]. Level 0: E_0 = s(v_0) while u_0 is on 0 (δ 3 > 2 > 1).
- V2 (EY_j := [ȳ_j ahead of y_j]). y_j → u_(j−1) / v_(j−1), ȳ_j → v_(j−1) / u_(j−1). Different options: the same target, heads
  decide, and the forward one is ahead (δ: (ȳ_j, 1) = 2 > (y_j, 0) = 1; (y_j, 1) = 3 > (ȳ_j, 0) = 0): EY_j = s(ȳ_j). Same option o:
  different targets, EY_j is the order of u_(j−1), v_(j−1): EY_j = [o ≠ E_(j−1)].
- V3 (EY′_j): the same with y′_j → ȳ_j / y_j, ȳ′_j → y_j / ȳ_j and δ 7 > 6 > 5 > 4: different options: EY′_j = s(ȳ′_j); same
  option o: EY′_j = [1 − o ≠ EY_j].
- V4: for one mover the two options have different targets (except wires, u_0, v_0), so the better option is the one whose target is
  ahead: v_j at o is value-enabled iff EY_j = 1 − o; u_j iff EY_j = o; e_j iff EY′_j = o; y_j at back iff E_(j−1) = 1, at forward
  iff E_(j−1) = 0; ȳ_j the opposite; y′_j at back iff EY_j = 0, at forward iff EY_j = 1; ȳ′_j the opposite; v_0 at 0 (δ 3 > 1) and
  never at 1; u_0 at 0 never (δ 2 > 0); a wire at 0 never.
- K1 (C_j := [v_j key-ahead of u_j]). Aligned: the same W-target, own gates decide, ε(u_j, o) < ε(v_j, o): C_j = 0. Split: the
  W-targets are u_(j−1) and v_(j−1); the keys differ before the own gate; C_j = [s(v_j) = C_(j−1)]. C_0 = s(v_0) (ε(v_0, 1) = 1 <
  ε(u_0, 0) = 2 < ε(v_0, 0) = 3).
- K2, K3 (wires on 0, WIRE): μ(wv_j) = μ(v_j) ++ gate(wv_j, 0). E(j + 1) on 1 has W-target v_j, own gates decide and
  ε(E(j + 1), 1) ≤ 3 < 6: ahead; on 0 its W-target is u_j: ahead iff C_j = 0. So D_j = [s(E(j + 1)) = 1 or C_j = 0]; likewise
  Z_j = [s(E(j + 1)) = 0 or C_j = 1] with ε(E(j + 1), 0) ≤ 2 < 8. E(j + 1) and the two wires are on level j + 1, so inside one
  level, where the gate order is the ε order.
- K4: u_j, v_j, e_j at o are key-enabled iff o ≠ C_(j−1)(s′) (options 0 / 1 lead to u_(j−1) / v_(j−1)); an observer of Y_j
  (j ≤ k − 2) at back iff D_j(s′) = 1, at forward iff D_j(s′) = 0; of Y′_j with Z_j; a top observer at back iff C_(k−1)(s′) = 1.
- WIRE: a wire and u_0 start on the option that is both value-better and key-less, so they never move; v_0 moves in step 1
  (enabled both ways) and never again (on 1 it is not value-enabled).
Each of V1-V4 and K1-K4 was also tested as a FORMULA against the model at every state with the wires and u_0 on 0 for k = 3 and
k = 4 (§3.3): 0 differences on 66,048 states. They are local (each involves one unit and its two neighbours), so k = 4, where every
kind of unit occurs (bottom, middle with e and Y′, top), exercises every case of the paper argument.
### 2.3 The window arithmetic
P_(k−1) = 3, P_j = 2P_(j+1) + 1 = 2^(k+1−j) − 1. Case (ii): t_1 = t + P_(j+1) − 1, t_2 = t_1 + P_(j+1), t_2 + 1 = t + 2P_(j+1) =
t + P_j − 1. For j = 1, a = 0, t = 1 the last step is t_2 = 1 + P_1 − 2 = 2^k − 2. Responses: unit 1 once, unit j + 1 twice per
response of unit j, so 2^(j−1) for unit j; every mover of unit j moves once per response; total 1 + 4·1 + 7·(2^(k−2) − 2) +
4·2^(k−2) = 11·2^(k−2) − 9 (13 at k = 3).
### 2.4 The RESPONSE LEMMA in the form the induction needs (closes G-1)
PREFIX FORM. Let j, a, c, t, F, B, F′, B′ be as in the packet, last := t + P_j − 1 (t + P_1 − 2 for j = 1), and assume (H1). Let
t ≤ τ_0 ≤ last and assume (H2[τ_0]): for every τ with t ≤ τ ≤ τ_0 the step from s_(τ−1) leaves C_(j−1) = c on the levels below j
(i.e. C_(j−1)(s_τ) = c), and E_(j−1)(s_τ) = c for every τ with t ≤ τ ≤ τ_0 − 1. Then the run reaches s_(τ_0), and in each step
τ ∈ [t, τ_0] the movers of the units j, …, k − 1 that move are exactly those the packet lists for step τ.
Proof scheme (the packet's own steps, in an order that is well-founded). Downward induction on j; for fixed j, induction on τ_0.
In step τ_0: (1) the level-j movers u_j, v_j, e_j: value-enabled by V4 from s_(τ_0−1) (known by the induction on τ_0; the E_(j−1)
it needs is a at τ_0 = t by (H1) and c later by (H2[τ_0])), key-enabled by K4 from C_(j−1)(s_(τ_0)) = c. (2) So C_j(s_(τ_0)) is
known (K1), and E_j(s_τ) is known for τ ≤ τ_0 − 1 (V1, V2 on complete earlier states): these are the hypothesis (H2[τ_0]) of the
response of unit j + 1 that is in progress. (3) The prefix form for j + 1 (induction on j) gives every move of the units above j in
step τ_0, in particular s_(τ_0)(E(j + 1)); in step t_2 + 1, after the second response, STABLE gives «no move» above j. (4) The observers of unit j
(level j + 2): value-enabled by V4 from s_(τ_0−1), key-enabled by K4 from D_j, Z_j under s_(τ_0), which by K2, K3 are functions of
s_(τ_0)(E(j + 1)) and C_j(s_(τ_0)), both known from (1) and (3). No step uses anything not yet determined: (K-loc) and (V-loc).
With this order I re-checked every step of case (i) (steps t, t + 1, t + 2) and of case (ii) (steps t, t + 1, the quiet stretch to
t_1 − 1, t_1, t_1 + 1, the quiet stretch to t_2 − 1, t_2, t_2 + 1), for a = 0 and a = 1, for j = 1, for 2 ≤ j ≤ k − 2 and for
j = k − 2 (where E(j + 1) = u_(k−1) and the unit above is the top unit): each move and each non-move the packet lists follows.
### 2.5 STABLE and §7
STABLE (in a unit at rest a with input (a, a) no mover is both value-enabled and key-enabled) is V4 and K4 at a rest state: only
v_j is value-enabled (EY_j = 1 − a), and it is key-disabled (s(v_j) = a = C_(j−1)). (b): at
t = 1 (H1) holds by the start column; (H2) for unit 1 is unconditional, since v_0 moves in step 1 and never again and u_0 never
(WIRE), so (C_0, E_0) = (1, 1) from s_1 on: for j = 1 the stated lemma applies as it stands. The last state has REST_1(1), REST_i(0);
v_1 at 1 is value-enabled (EY_1 = 0) and not key-enabled (C_0 = 1), so the stop is «stuck». (c): §2.3.
### 2.6 Corollary EXP-N5
REACH3's only hypothesis on G (RESULTS R117 at trunk 5d7aab0f, l. 13362, opened): [Q R117] «for every G with an ACYCLIC Ξ-graph»,
G a genome in R104's sense; G_k is one by (a). Its conclusion [Q R117] «the run makes at least L(G) + 1 iterations» gives 2^k − 1.
n = N + 7M + 10 = 135k − 230. m = 9M + M_X + 14 with M_X = M − (4k − 6) = 14k − 26 options whose Ξ-target is a mover: 176k − 300.
Both counted on my own builder for k = 3..14 (§3.5). Cost sentence: TARGET.md §3 is a word RAM; an iteration is at least one step.

## 3. DATA on my own code (files in docs/referee-2/R2-P-N5-EXP/; every counter below is «must 0» unless marked INFO)
Tools: r2exp.py (generator written from §3's TABLE, one row list and one resolver; the model is my r2unit217.M1P, which Addendum 3
of R2-key-preread showed equal to R104's IDEAL model; ideal_states = R104's words); r2pg.py (instance files, sizes, N5 on R104's
numbering); r2qexp.py (quotes); ../R2-key/r2kill217.py (N5 itself on Γ3 with three solvers; this commit adds Oink to it). Nothing of
the lane is imported by any of them.
### 3.1 The rule, rebuilt (exp_main.out)
| counter | unit | set | value |
| --- | --- | --- | --- |
| size | k | k = 3..14 | 0 (N = 9k − 16, M = 2N, k + 1 levels) |
| lanediff | file | the lane's 12 files data/b6b/G/G_k.json and 12 raw files, compared as dictionaries with my G_k | 0 of 24 |
| leadsha | k | sha1 of json.dumps of my RAW-gate G_k against the Lead's four sha1s (k = 3, 4, 8, 10) | 0 of 4 |
| member_c1..c8 | clause × k | R104's eight clauses on my G_k, k = 3..14 | 0 |
| depth | option | a Ξ-target's Ξ-depth is not smaller than its source's | 0 |
| rawdiff | k | the run under gates 100·lev + ε ≠ the run under ranked gates | 0 |
| tiebreak | k | the run with the br ties broken by DECREASING β-id ≠ the run (M-1) | 0 |
INFO: tied br keys per k = 0, 2, 6, 10, …, 42 (= 4k − 14 for k ≥ 4).
### 3.2 The run (exp_main.out k = 3..14; exp_big.out k = 15, 16)
| counter | unit | value |
| --- | --- | --- |
| tfail | k: T ≠ 2^k − 2 | 0 (T = 6, 14, 30, …, 16,382; 32,766; 65,534) |
| stopfail | k: the last state has only singleton availability sets | 0 (the stop is «stuck») |
| swfail | mover: its number of option changes ≠ (c) | 0 (max 2^(k−2): 2, 4, …, 16,384) |
| totfail | k: total ≠ 11·2^(k−2) − 9 | 0 (13, 35, 79, …, 45,047; 90,103; 180,215) |
| idfail | k ≤ 12: the run ≠ R104's IDEAL run state by state (ideal_states) | 0 |
### 3.3 The lemmas as predicates (exp_exh.out, exp_main.out, exp_big.out)
| counter | unit | set | value |
| --- | --- | --- | --- |
| v1, v2, v3, k1, k2, k3 | (state, j): the formula ≠ the model's own value / key comparison | EVERY state with wires and u_0 on 0: 2^9 at k = 3, 2^16 at k = 4 (66,048 states); and for k = 3..16 the run's states (all for T ≤ 600, else the first 400 and last 200) plus 200 random states each | 0 |
| v4, k4 | (state, mover): the enabling predicate ≠ the model's A_s / key comparison | the same sets | 0 |
| move2 | (step, mover): moved ≠ (value-enabled under s and key-enabled in the step) | the first 600 steps of every run | 0 |
| resp | step: the set of (mover, new option) ≠ the RESPONSE LEMMA's schedule, generated recursively from (j, a, t) = (1, 0, 1) | EVERY step of every run, k = 3..16 (131,036 steps in all) | 0 |
| rest | response: (H1) fails at its start, or REST_j(c) / REST_i(0) fails at its end | 16,177 responses for k ≤ 14 (all for k ≤ 13; the first and last 4,000 of 8,191 at k = 14); the first and last 4,000 for k = 15, 16 | 0 |
| inp | (response, τ): the input of unit j is not (c, c) | the first 65 steps of each such response's window | 0 |
### 3.4 N5 itself from S3 on Γ3(G_k), to termination (kill_k3.out … kill_k11.out)
Own engine r2end (SPEC S1-S5 with FIX 1-4; successor 34's, the engine of my R117 review). F = the iteration of the first fallback.
| k | n | T | F | iterations | red | zl | zh | oink-zlk | oink-tl | lane | secs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 175 | 6 | 7 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0.6 |
| 4 | 310 | 14 | 15 | 17 | 0 | 0 | 0 | 0 | 0 | 0 | 0.3 |
| 5 | 445 | 30 | 31 | 33 | 0 | 0 | 0 | 0 | 0 | 0 | 1.2 |
| 6 | 580 | 62 | 63 | 65 | 0 | 0 | 0 | 0 | 0 | 0 | 3.5 |
| 7 | 715 | 126 | 127 | 129 | 0 | 0 | 0 | 0 | 0 | 0 | 10.5 |
| 8 | 850 | 254 | 255 | 257 | 0 | 0 | 0 | 0 | 0 | 0 | 30.3 |
| 9 | 985 | 510 | 511 | 513 | 0 | 0 | 0 | 0 | 0 | 0 | 81.2 |
| 10 | 1,120 | 1,022 | 1,023 | 1,025 | 0 | 0 | 0 | 0 | 0 | 0 | 212.7 |
| 11 | 1,255 | 2,046 | 2,047 | 2,049 | 0 | 0 | 0 | 0 | 0 | 0 | 540.0 |
red = [the mover parts of N5's states before the first fallback ≠ the key run, or F ≠ T + 1]; zl = [N5's output ≠ my own Zielonka
(R2-TA1/r2lib)]; zh = [≠ the harness Zielonka]; oink-zlk, oink-tl = [≠ Oink 8fbf0a7, solvers zlk and tl, each with Oink's own
verification]: a third and fourth independent solver; lane = [the lane's n5v (mode spec, from n5x.start_pair) on L-NEW's
gamma3.build differs in the number of states before its fallback, the mover states, the iteration count (it also makes 2^k + 1) or
the regions]. |W_E| = n − 1 on every game. So on k = 3..11: the first fallback is transition 2^k − 1 (as REACH3 says: L(G) + 1),
N5 makes 2^k + 1 iterations, and its answer is right. Control (kill_ctrl.out): one vertex of the reference regions flipped fires zl
and both Oink counters.
### 3.5 The instance files and the sizes (size.out, pg.out, pg_ctrl.out)
sizediff = [n ≠ 135k − 230] + [m ≠ 176k − 300] on my builder: 0 for k = 3..14. pgdiff = [my game, β block renumbered as R104's
l. 86 says, ≠ the lane's data/b6b/pg/G_k_g3.pg index by index (priority, owner, successor set)]: 0 for k = 3..11 (9 files; their
sha1s equal the packet's §9.4 column, e.g. G_3_g3.pg fca7a52c49e095d297458c2264664b846c442f8b). pgraw (INFO) = 0 of 9: without the
renumbering my game is not the file (item O-1). n5diff = [N5 on the renumbered game differs from N5 on my numbering in F, the
iteration count or the mover states, or F ≠ 2^k − 1, or iterations ≠ 2^k + 1]: 0 for k = 3..9; zdiff (its output against my own
Zielonka on the renumbered game): 0. Oink zlk on the lane's nine files: exit 0, |W_E| = n − 1 on each. Control: pgdiff fires on 9 of
9 files, sizediff on 12 of 12.
### 3.6 Quotes (quote.out, quote_ctrl.out)
Own checker, the packet's convention (every top-level guillemet quote after a Q-tag, up to the next tag or blank line), sources by
`git show 5d7aab0f:<path>`: 27 tagged quotes, 27 found verbatim (18 R104P, 5 R117 — all five inside the entry «### R117» —, 2 TARGET,
1 CLAUDE, 1 GAPS); control (one letter of each quote changed): 27 missing. Four untagged quotes of ≥ 25 characters: three are found
in R104P (two are repeats of a tagged quote inside MOVE-2; one, §9.2's «implemented as r178/fastcyc.simulate and r187/ideal.traj»,
is a verbatim R104P quote without a tag), one («different options at depth d*») is the packet's own words.
### 3.7 Fits with residuals and explicit bounds (fit.out, bounds.out) — DATA about the members, not statements
12 points, k = 3..14, size N + M = 33..330. Closed forms T = 2^k − 2 and max sw = 2^(k−2): residual 0 at every point.
log2 T = 1.5419 + 0.03797·(N + M), R² 0.99949, residuals within ±0.21; log2 max sw = −0.2222 + 0.03704·(N + M), R² 1.00000,
residuals 0.000 (max sw = 2^((N + M − 6)/27) exactly). Power laws: log2 T = −16.7652 + 3.4822·log2(N + M), R² 0.9209, residuals
+1.785 … −1.119 … +1.632 (U-shaped: the local exponent grows); log2 max sw = −17.9054 + 3.3725·log2(N + M), R² 0.9085, the same
shape. These equal the packet's §9.5 fit lines. Explicit bounds, exact integers, with «the bound then holds for the next 1,000 k»:
2^k − 1 > n² first at k = 23 (n = 2,875), > n³ at k = 37, > n⁴ at k = 51; against (n + m)^c: k = 26, 41, 57. As the packet says.
### 3.8 Controls (exp_ctrl.out and the three above)
start (ȳ_1's start flipped), eps (ε of u_1 and v_1 exchanged), rank (δ of y_1's options exchanged): tfail, swfail, totfail, resp,
rest fire (eps also k1-k4; rank also v1-v4; leadsha too, since the raw genome changes with them); sched (schedule shifted by one step): resp; form (V2 negated): v1-v4; mv2 (MOVE-2
without its key half): move2; stuck: stopfail; mem2, mem4, mem5 (the RAW gates), mem6, mem8: the one clause each; start with
--lane: lanediff. 13 controls, each fires its target.
Not done: §10's commands as written; the lane's ablation rows (§9.6) and the «seq» / Howard contrast rows (§9.5) were not re-run;
the B6b history file was not read; N5 at k ≥ 12 was not run (about 25 minutes per engine at k = 12).

## 4. Unconditional, conditional, measured — and what a RESULTS «DEAD» needs (the Lead's question, 13:10Z)
- UNCONDITIONAL (mathematics about R104's DEFINITIONS, no theorem used): Theorem EXP-IDEAL (a), (b), (c) with its lemmas. After
  both referees' signatures it is a refereed-only result with the gaps G-1 (closed) and M-1 listed.
- PROVED-CONDITIONAL on RESULTS R117 as landed: Corollary EXP-N5's iteration bound, and with it the Dead-end paragraph («FALSE»,
  «cannot pass gauntlet step 4», «G-N5-TIME is answered NO»). R117 is itself refereed-only and carries standing premises (its
  header: 1E-N3 = R57 (b) in its two forms; R24 (a) Lemma R and R24 (b)'s choice rule with R103's bridge B and (R1) ruling; R36 (c)
  Lemma P1 on the dual game; R15 (d) for termination only). G_k meets REACH3's hypothesis on G (a genome with an acyclic Ξ-graph);
  nothing else about G_k is needed.
- MEASURED (DATA): N5's own counts at k ≤ 11 (n ≤ 1,255; 2,049 iterations at most), on my engine, the lane's n5v, and (the
  packet's) L-COMP's n5b. They confirm REACH3's prediction at every k tried, and they confirm that N5's ANSWER is right there. They
  are far below every explicit polynomial bound (2^k − 1 < n² until k = 23, where a run would take 8.4 million iterations on 2,875
  vertices): no measured instance «beyond an explicit bound» exists or is in reach of these engines. The kill rests on the proof.
- For a RESULTS line «DEAD» under L43 («a refereed proof»): (1) both referees' signatures on Theorem EXP-IDEAL; (2) the Corollary
  cited as «through R117 Theorem REACH3, refereed-only, with R117's standing premises»; (3) the fixes file with G-1's prefix form,
  M-1's tie-break, D-1; (4) CHECKER's exact-commit re-run of §10 and its statement diff. What the line may say: N5 (SPEC S1-S5, S4a
  root-first key rule, fallback S4c) from its default start S3 is not polynomial; G-N5-TIME answered NO for that start. What it may
  not say: anything about other start pairs, other tie rules (N5′-xi), other candidates, or the target — the packet's «Not claimed»
  paragraph is exact and I checked nothing beyond it.

## 5. TARGET diff
The packet claims no M3 / M4 statement and proves no bound for any algorithm. Its only contact with TARGET.md: the quoted §2
statement (verbatim, marked as staying open), gauntlet step 4 [Q TARGET.md@5d7aab0f] «4. Written correctness and running-time proofs,
double-refereed with every gap listed.» (verbatim), and the cost sentence (TARGET §3: word RAM; an iteration is at least one step:
correct, and it needs no bit-cost argument because it is a LOWER bound on steps). The lower bound is in the number of iterations
against n and n + m with d not fixed: the right measure for TARGET §2 (p(n + m)); Γ3(G_k) has 2M + O(1) distinct priorities
(52 at k = 3, 448 at k = 14 on my builder), so no parameter is being held small. No statement of the packet goes beyond TARGET.md.

## 6. Reproduction (from the repository root; inputs by git, nothing edited outside docs/referee-2/)
- `git archive 350d84eb6602003172d0d3dd67e0ef2d0c72d2f8 docs/red-b experiments/red-b | tar -x -C DIR` (the lane's files, read only),
  LANE := DIR/experiments/red-b/data/b6b.
- `python3 -B docs/referee-2/R2-P-N5-EXP/r2exp.py --lane LANE/G --dump GK 3 4 5 6 7 8 9 10 11 12 13 14` → exp_main.out (about 40 s);
  `… r2exp.py 15 16` → exp_big.out (about 4 minutes); `… r2exp.py --exh 3 4` → exp_exh.out; `… r2exp.py --ctrl NAME 3 4 5 6` for
  the twelve names of §3.8 → exp_ctrl.out; `… r2exp.py --bounds` → bounds.out.
- `python3 -B docs/referee-2/R2-key/r2kill217.py --lane ROOT --oink zlk,tl GK/r2_G_k.json` → kill_k<k>.out (ROOT = a `git archive
  a143d406 experiments/si/si.py experiments/harness experiments/new` checkout; Oink from scripts/setup_oink.sh);
  `… r2kill217.py --nog3 GK/r2_G_3.json … GK/r2_G_14.json` → fit.out; `… --ctrl --oink zlk,tl GK/r2_G_4.json` → kill_ctrl.out.
- `python3 -B docs/referee-2/R2-P-N5-EXP/r2pg.py LANE/pg GK --n5max 9 3 … 11` → pg.out; `… --n5max 0 3 … 14` → size.out; `… --ctrl
  3 … 14` → pg_ctrl.out.
- `python3 -B docs/referee-2/R2-P-N5-EXP/r2qexp.py DIR/docs/red-b/P-N5-EXP.md 5d7aab0f R104P=docs/red/P-N5-REALIZE.md
  R117=docs/RESULTS.md TARGET=TARGET.md CLAUDE=CLAUDE.md GAPS=docs/GAPS.md` → quote.out (with --ctrl → quote_ctrl.out).

DONE: second review of P-N5-EXP at 350d84eb: every statement to sign re-derived; own generator, model checks, N5 runs with four
solvers, instance files, quotes (this file and docs/referee-2/R2-P-N5-EXP/).
FINDINGS: no error; SIGN Theorem EXP-IDEAL (a)-(c) and its lemmas with G-1 (proof gap, closed by the prefix form) and M-1 (rank
tie-break) listed; SIGN Corollary EXP-N5 as proved-conditional on R117 as landed (W-2); D-1 placeholder in §9.7; O-1 in my own
builder (isomorphic numbering of the β block; the lane's files are the right ones).
NEEDS: Lead: route G-1, M-1, W-1, W-2, D-1 to L-RED-B's fixes file; CHECKER: the exact-commit re-run.
