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

## Addendum 1 (REFEREE-2 successor 41; 2026-11-13T14:39:51Z by date -u): three points from the Lead's 13:58Z message, which reached me at 14:19Z, after the report was committed (33ff0e98)
The verdict of §0 is unchanged. Nothing below was needed for it.
### A1.1 The exact count (R124, Corollary EXACT-L): should a fixes entry add it, and under which premises?
Source opened: docs/RESULTS.md at trunk 6eaf4604, l. 15371, entry R124 [refereed-only]. Its Corollary EXACT-L, for G ∈ IDEAL-ACYC:
[Q R124] «makes exactly L(G) + 3 iterations», with the entry's own premise label [Q R124] «premise RESULTS R117 (f)» and the remark
that it uses SPEC's S1 tie-breaks through REACH3's [RULE] choice; and Theorem ENDGAME-3-N5 of the same entry: exactly one fallback,
at an iteration F, and exactly F + 2 iterations.
- With Theorem EXP-IDEAL (a), (b) this gives: N5 from S3 on Γ3(G_k) makes EXACTLY 2^k + 1 iterations, with exactly one fallback, at
  iteration 2^k − 1. My measured counts (§3.4) are exactly these at every k = 3..11 (F = 2^k − 1, iterations = 2^k + 1 = F + 2), on
  my engine and on the lane's n5v; the count 4,097 at k = 12 relayed by the Lead (two lanes; not run by me) is 2^12 + 1.
- Recommendation: YES, add it, as a SEPARATE labelled sentence («Corollary EXP-N5, exact form»), and keep the present lower bound
  as it is. Reasons: (1) the lower bound ≥ 2^k − 1 needs R117 (f) only, and the kill should rest on the fewest premises; (2) the
  exact form turns §9.4's DATA into a test of an exact prediction (equality at every measured point, not only «≥»); (3) EXACT-L's
  second sentence [Q R124] «N5's iteration count is polynomial in n iff L(G) is polynomial in N + M» is the precise form of the
  dead-end line on {Γ3(G) : G ∈ IDEAL-ACYC}.
- Premises to print with it: RESULTS R124 Corollary EXACT-L and Theorem ENDGAME-3-N5 (refereed-only), whose premise is R117 (f)
  with R117's standing premises; N5 = SPEC S1-S5 with FIX 1-4 (EXACT-L is stated for these tie-breaks; R124 records that with another
  pointwise-optimal S4a choice the identity can fail); G_k ∈ IDEAL-ACYC by Lemma MEMBER; L(G_k) = 2^k − 2 by Theorem EXP-IDEAL (b).
  Status of the exact form: PROVED-CONDITIONAL on R124 and R117 as landed; no new premise beyond those two entries.
### A1.2 The reproduction erratum (run_b6b.sh needs an absolute root; with a relative root the gen stage fails and the runner prints «done», exit 0)
I did not run §10 (said in §0 and §3.8), so I neither met nor can confirm the erratum. Judgement on what it touches: it is a defect of
the reproduction SCRIPT, of the kind CLAUDE.md warns about for pipes (a failure hidden behind exit 0); it touches no statement and
no proof. The pinned DATA of §9.1-§9.5 does not rest on that script for this report: I reproduced those numbers with my own
generator, model, builder and engines (§3). For the fixes entry I would ask for two things, not one: the absolute root in §10, AND
a runner that exits non-zero when a stage fails; CHECKER's exact-commit re-run should include one deliberately failing stage.
### A1.3 Handover
The Lead (14:19Z): the items of §1 go to L-RED-B 6 as fixes entries; successor 42 does the fixes-file check, the agreement note with
the first referee, and a comparison of the packet's proof with L-SI 56's independent proof (box 108); P-N5-KEY1P's full review is
DEFERRED (not cancelled). The handover at the top of notes/REFEREE-2.md says so from this commit on.
Correction to the header: the first referee on this object is REFEREE 36 (the Lead, 13:58Z); REFEREE 35 wrote the pre-check. Neither
was read by me.
DONE: Addendum 1 (exact count through R124; the reproduction erratum; handover).
FINDINGS: the exact form (2^k + 1 iterations, one fallback at 2^k − 1) equals every measured count; add it as a separate sentence
under R124 + R117; the erratum is a script defect only.
NEEDS: Lead: none.
## Addendum 2 (REFEREE-2 successor 42; 2026-11-13T17:01:47Z by date -u): FIXES-FILE CHECK of P-N5-EXP-fixes.md entries 1-5, and the L41 cross-signature of LEMMA′, CAUSAL and STABLE in step form
Asked by the Lead (brief of 15:55Z, item 1): (a) entries 2-5 against this lane's items G-1, M-1, W-1, W-2, D-1 and Addendum 1;
(b) the L41 cross-check: sign or refuse LEMMA′ as stated in entry 4, independently; (c) the frozen guard.
- Object: claude/l-red-b 24f4d436a0fea1f62ae736f20f78ff9e84333a90 (on origin at 16:42:16Z, `git ls-remote`),
  docs/red-b/P-N5-EXP-fixes.md, sha1 9dc9179fb08063cd59de25c5d3e16b0f8c693fbd, 829 lines, 78,975 B; entries 2-5 are its lines
  126-829. Read in full, entry 1 included. Line L-1 (docs/red-b/P-N5-EXP-line-L1.txt, sha1
  59c5309377eda882ba436ffe7eb03fbff598c7c8, 5,585 B): read, §A2.7.
- Independence: docs/referee/R-P-N5-EXP.md and docs/referee/R-GK-precheck.md were NOT opened before this addendum was committed.
  What I know of the first referee's report is what entries 2-5 quote from it (22 tagged quotes; 5 of the pre-check). Whether those
  quotes are verbatim (4.0 says «word for word») is checked in Addendum 3, after this commit (§A2.6). The derivation of §A2.3 and
  the first version of my checker (my lane's PREFIX form, STABLE in step form, a causality statement, the frozen wording as a
  control) were done, and their results sent to the Lead at 16:27Z, before 24f4d436 was on origin.

### A2.0 Verdict
| entry | this lane's items | verdict |
| --- | --- | --- |
| 1 (extra DATA, pointer correction, §10 erratum) | Addendum 1 A1.2 | **closed** for the runner A1.2 named: run_b6b.sh at 24f4d436 takes a relative root and exits 1 when a stage fails (tests T1-T3, §A2.5). No statement, proof or hypothesis changes. New item F-4 (the NEW runner) |
| 2 (unconditional / conditional / measured) | W-2, §4 | **closed**: (b) and (c) carry «PROVED-CONDITIONAL on RESULTS R117's Theorem REACH3 AS LANDED [refereed-only]» with R117's standing premises quoted from its title line; the dead-end sentences are to be read through R117's Theorem REACH3, and the NO is for N5 from S3 only. Note F-5 |
| 3 (Corollary EXP-N5′) | Addendum 1 A1.1 | **closed**: the exact count is a SEPARATE labelled corollary under R124 EXACT-L (premise R117 (f), SPEC's FIX 1-4 tie-breaks); the frozen lower bound through R117 alone is kept |
| 4 (LEMMA′, CAUSAL, STABLE in step form) | G-1 (and W-1 in (S2)) | G-1 **closed**. L41: **I SIGN** 4.1 (S1)-(S4), 4.2, 4.3, 4.4 and the proofs 4.2, 4.3, 4.5, 4.6 as printed, with the reading F-1; the concordance claim «PREFIX FORM = LEMMA′ at τ_0 = T» is **correct** (§A2.4). Wording F-1, F-2 |
| 5 (wording and records) | M-1, W-1, D-1 | **closed** (5.1, 5.2, 5.3); wording F-3. 5.4-5.9 answer other referees' items: read; where they quote this lane's report the quotes are verbatim; nothing in them contradicts it |
| frozen guard | — | **holds**: the packet's sha1 is c0449b17193f19619f33b366096762dfde27d542 at 350d84eb and at 24f4d436; the fixes file at 06d399c2 (entry 1; sha1 4c692ab2…, 12,551 B) is a byte prefix of the file at 24f4d436 (`cmp -n 12551`) |

**P-N5-EXP: SIGNED with fixes entries 1-5.** The signature is §0's, with one correction (§A2.1): the statement of the RESPONSE
LEMMA that I sign is entry 4's 4.4 (LEMMA′), not the frozen l. 192-204; STABLE is signed in 4.2's step form. Every other row of §0
stands as written. Items F-1 to F-5 are wording and tooling; none of them is a condition of the signature except the reading F-1.

### A2.1 Self-correction: §0's row «RESPONSE LEMMA (§6): SIGN the statement»
That row was wrong about the STATEMENT. As frozen, (H2) is quantified over the τ [Q FROZEN l. 194] «that the run reaches»; under
the last state s_L, L = 2^k − 2, every unit is at rest with its input equal to its rest bit, so at t = 2^k − 1 (H1) holds for
(j, a) = (1, 1) and for (j, 0), 2 ≤ j ≤ k − 1, no τ of the window is reached, (H2) is vacuous, and the conclusion (the run
reaches the window's last state) is false. My lane's §2.4 wrote the PREFIX form, whose key clause («the step from s_(τ−1) leaves C_(j−1) = c») fails at
those triples, but it did not notice that the frozen statement itself fails there and said [Q REF2 l. 44-45] «The stated lemma is
the case τ_0 = the last step». The first referee found it (entry 4 quotes its E-1). My own control confirms it (§A2.5): the frozen
wording fails at exactly k − 1 triples per k, all at t = 2^k − 1, and nowhere else (frozen_noncorner 0: never when s_t is
reached). What this changes: the statement of record (now 4.4). What it does not change: any number, any step of §7 (the lemma is
used at the windows of the recursion, t ≤ 2^k − 2 with s_t reached, where the frozen form and LEMMA′ say the same), any other
verdict of §0, and G-1 (a gap of the PROOF, which 4.5 closes).

### A2.2 Entries 2, 3, 5 against this lane's items
- **W-2 and §4 → entry 2: closed.** (a) UNCONDITIONAL is my §4's first bullet. (b) quotes R117's own parenthesis of premises and
  the entry's [1E-N3], [RULE], [VJ-LOC], [TERM] (7 quotes, all inside the entry «### R117» of trunk 5d7aab0f, §A2.6); REACH3's
  only hypothesis on G is the acyclic Ξ-graph. (c) attaches the condition to the two dead-end sentences and restricts the NO:
  [Q FIX l. 213] «G-N5-TIME is answered NO for N5 from S3». (d) MEASURED: the arithmetic re-done (4,097 iterations at k = 12 on
  n = 1,390, n + m = 3,202, n² = 1,932,100; 2^k + 1 > n from k = 11, > n + m at k = 12; 2^23 − 1 = 8,388,607 > 2,875² first at
  k = 23). (e) the correctness sentence is RESULTS R57 (b) Lemma OUT-G for every k (2 quotes found in the entry «### R57») and
  DATA for k ≤ 12: right, and it is the answer to an item I did not raise.
  **F-5 (label inside (a′); no change asked).** (a′) has two sentences of different standing. That IDEAL-ACYC-POLY is false follows
  from Theorem EXP-IDEAL (b) alone (L(G_k) = 2^k − 2 against N + M = 27k − 48): unconditional. That QUIET-KEY-1P and SW-POLY of
  P-N5-KEY1P are false needs that lane packet's Lemma IDEAL-1P to identify T_key and sw with the IDEAL model's quantities; the
  entry says so ([Q FIX l. 187-188] «when T_key and sw are read in R104's IDEAL model, as that packet's Lemma IDEAL-1P reads
  them»). P-N5-KEY1P is a lane packet whose second review is deferred (my pre-read, R2-key-preread Addendum 3 item B-7, found no
  gap in that identification, and a pre-read is not a signature). A RESULTS line may carry the first sentence as unconditional
  and not the second; line L-1 does exactly that.
- **Addendum 1 A1.1 → entry 3: closed.** Corollary EXP-N5′: EXACTLY L(G_k) + 3 = 2^k + 1 iterations, one fallback, at iteration
  2^k − 1; labelled PROVED-CONDITIONAL on R124's Corollary EXACT-L as landed, with R124's premise words quoted (R117 (f); SPEC's S1
  tie-breaks through REACH3's [RULE]; «with another pointwise-optimal S4a choice the identity can fail»; 1E-N3; iterations counted
  as in SPEC S4): the premises my A1.1 listed. F = L(G_k) + 1 follows from the two quoted clauses (L + 3 iterations; F + 2
  iterations). G_k ∈ IDEAL-ACYC needs R104's self-loop clause, and the entry cites MEMBER c8 for it. The frozen Corollary EXP-N5
  stays as the lower bound through R117 alone. R124's title line opened at trunk 38f4a6a0, l. 15371 (8 quotes found, §A2.6).
- **M-1 → 5.1: closed.** br is now the rank of the TRIPLE (−depth, δ, β-id), the smaller β-id first, in §3's clause and in MEMBER
  c6: the text I asked for, and what gk.py and my generator do. The count is right (2(k − 3) + 2(k − 4) = 4k − 14 for k ≥ 4, none
  at k = 3). The lane's brtie.out (reverse tie order, same run, k = 3..14) agrees with my counter tiebreak.
  **F-3 (wording).** The reason given, [Q FIX l. 670] «(table: every Ξ-target is a u, v, y, ȳ or X)», omits y′_j and ȳ′_j, the
  Ξ-targets of e_j. The claim it supports, that no Ξ-edge ends at a wire, is true by the table.
- **W-1 → 5.2 and 4.1 (S2): closed.** [Q FIX l. 340] ««Step τ» is the passage s_(τ−1) → s_τ = (s_(τ−1))⁺.»
- **D-1 → 5.3: closed.** The placeholder's text is the summary of data/b6b/out/quote.out, pasted. Checked: that file's sha1 at
  24f4d436 is b20118000a5456610e9303b0e140a4bc53501a6f and its first five and last lines are the pasted ones; the sha1s of R104P,
  RESULTS, TARGET and GAPS equal `git show 5d7aab0f:PATH | sha1sum`; the fifth, CLAUDE.md 1e990915…, is the lane branch's own
  CLAUDE.md (the same at 350d84eb and 24f4d436; trunk's is 30e54151…), as the packet's label «CLAUDE = CLAUDE.md» says, and the
  quoted sentence is in both.
- **Addendum 1 A1.2 → entry 1, 10.E: closed** for run_b6b.sh (it was already there when A1.2 was written; successor 41 had not
  read the fixes file). Tested at 24f4d436 in a scratch copy: T1 relative root, stage gen: exit 0, files written; T2 stage n5
  without archives: «failures 1», exit 1; T3 a python3 that exits 3: exit 1.
  **F-4 (tooling; the same defect in the NEW runner).** experiments/red-b/run_b6fix.sh, added by 24f4d436 as the runner of 4.7,
  5.1 and 5.4's DATA, has no failure count: with the same failing python3 it prints «run_b6fix exh done», exits 0 and leaves an
  EMPTY prefix_exh.out (T4). run_b6b.sh got `trap 'fail=1' ERR` and `exit $fail` in entry 1; the new runner did not. No DATA is
  affected: I re-ran `run_b6fix.sh OUT every` in the scratch copy (exit 0, about 2 minutes) and all eleven output files are
  byte-equal to the pinned ones (prefix_run, prefix_all, prefix_off, prefix_drive, prefix_loc, prefix_stable, prefix_exh,
  prefix_u0, brtie, width, prefix_ctrl), and the lane's check.sh tests content (four b6prefix lines and `sha1sum -c
  SHA1SUMS_b6b_fixes2`), not an exit code. Ask: the two lines of run_b6b.sh in run_b6fix.sh; CHECKER should compare the files,
  not trust the runner's exit code.
- 5.4-5.9 (not this lane's items), what I could check cheaply: 5.4's widths equal my generator's for k = 3..14 (width_mine.out);
  5.5's four genome sha1s and four raw sha1s equal `git show 24f4d436:… | sha1sum`, and the raw ones are the Lead's four values in
  my r2exp.py; 5.6's mover order is my generator's row order; 5.8's line on this lane is what §3 says. 5.7, 5.9 and the other
  lanes' numbers in 5.8: read, not checked.

### A2.3 Entry 4, re-derived (the L41 cross-check)
What I sign and how it was checked. Everything below was derived from the packet's table (§3) and R104's step; notation of 4.1.
- **4.1.** (S1): C_0(s) = E_0(s) = s(v_0) needs u_0 at 0 (ε(u_0, 0) = 2 between ε(v_0, 1) = 1 and ε(v_0, 0) = 3; δ(u_0, 0) = 2
  between 1 and 3); a wire at 0 and u_0 at 0 are value-worse and key-larger on their other option, so s⁺ keeps both. (S2): Φ is
  total and the run stops at s iff s⁺ = s. (S3): in a step the value bits are read under s (A_s) and the key bits under s⁺ (keys
  with s′ below): this is R104's definition, and it is the whole content of G-1. Correct.
- **The unit as a transducer (my own derivation, before reading the entry).** For the movers of unit j in a step s → s⁺, with
  e := E_(j−1)(s), γ := C_(j−1)(s⁺), σ := s⁺(E(j + 1)): EY_j(s) = s(ȳ_j) if s(y_j) ≠ s(ȳ_j), else [s(y_j) ≠ e]; EY′_j(s) = s(ȳ′_j)
  if s(y′_j) ≠ s(ȳ′_j), else [1 − s(y′_j) ≠ EY_j(s)]; v_j at o moves iff EY_j(s) = 1 − o and o ≠ γ; u_j iff EY_j(s) = o and o ≠ γ;
  e_j iff EY′_j(s) = o and o ≠ γ; then C_j(s⁺) = [s⁺(v_j) = γ] if the pair is split under s⁺, else 0; D_j(s⁺) = [σ = 1 or
  C_j(s⁺) = 0], Z_j(s⁺) = [σ = 0 or C_j(s⁺) = 1]; y_j moves from back iff e = 1 and D_j(s⁺) = 1, from forward iff e = 0 and
  D_j(s⁺) = 0; ȳ_j the same with e negated; y′_j from back iff EY_j(s) = 0 and Z_j(s⁺) = 1, from forward iff EY_j(s) = 1 and
  Z_j(s⁺) = 0; ȳ′_j the same with EY_j negated (top unit: C_(k−1)(s⁺) in place of D). The unit reads the part below it through
  e and γ only, and the part above through σ only; σ is fixed by the units above from (C_j(s⁺), E_j(s)), and E_j(s) = 1 if split
  under s, else [EY_j(s) = s(v_j)].
- **4.3 CAUSAL: correct.** It is the statement above: (L1) is the three rules for u_j, v_j, e_j; (L2) is «(C_j(s⁺), E_j(s)) is
  a function of s⁺ on the pair, γ, s on the pair and EY_j(s)»; (L3) is the four observer rules with σ from CAUSAL for j + 1. The
  order (pair and e, then the units above, then the observers) is the level order of R104's step, and it is well-founded because
  no observer is a W-target. Downward induction on j, nothing to prove above k − 1. No gap.
- **4.2 STABLE: correct.** At REST_i(b) with e = b and γ = b: u_i, v_i, e_i stand at b = γ (no move by the key half); EY_i(s) =
  1 − b and Y_i = (b, 1 − b) with e = b makes both observers of Y_i value-disabled; EY_i(s) = 1 − b makes both observers of Y′_i
  value-disabled. «Hence»: the pair is aligned, so C_i(s⁺) = 0 and E_i(s) = [1 − b = b] = 0. «Consequently»: these two bits are
  the hypothesis for unit i + 1 at rest 0; induction upwards. Both uses (step t_2 + 1 inside 4.5; the stop in 4.6) are of this
  form. The frozen one-state wording was false (under s_0 unit 1 is at rest 0 with input (0, 0) and v_1 moves in step 1).
- **4.4 LEMMA′: correct, with the reading F-1.** I traced a response in the transducer with γ_τ := C_(j−1)((s_(τ−1))⁺) and
  e_τ := E_(j−1)(s_(τ−1)): step t needs γ_t = c and e_t = a (from (H1)): only v_j moves (u_j, e_j value-disabled: EY_j = EY′_j =
  c; no observer of Y_j value-enabled with e = a; none of Y′_j with EY_j = c). Steps t + 1, …, last need γ_τ = c and e_τ = c:
  t + 1: F to back (case (i): B to forward); the quiet stretch (Y_j on (0, 0), EY_j = [0 ≠ e] = c, D_j = 0, Z_j = 1); t_1: B to
  forward as σ becomes 1; t_1 + 1: u_j to c (EY_j = a from Y_j = (c, 1 − c)), then C_j = 0, Z_j = 0, F′ to back; the second
  quiet stretch (D_j = 1, Z_j = 0, EY′_j = c); t_2: B′ to forward as σ becomes 0; t_2 + 1: e_j to c; case (i): t + 2: u_j to c
  and F to back. So the moves of step τ are fixed by γ_τ and e_τ alone, which is exactly (H2′_T): C at τ = t..T and E at s_t, …,
  s_(T−1). The guards «if the run reaches» make the hypothesis well-formed without weakening the lemma: (R2) at T − 1 makes every
  guard of (H2′_T) true. The non-vacuity at a stop (Remark 1) is right: (H1) has C_(j−1)(s_(t−1)) = a and (H2′_T), T ≥ t, has
  C_(j−1)((s_(t−1))⁺) = c ≠ a, so (s_(t−1))⁺ ≠ s_(t−1). Remark 2 is right (E_(j−1)(s_last) is read by step last + 1 only).
  **F-1 (reading; inherited from the frozen l. 203).** (R3) says [Q FIX l. 384-385] «s_τ(E(j)) = a for τ < last» with no lower
  end. Read: for t − 1 ≤ τ < last. Without the lower end it is false (before the first response of unit j ≥ 2 ends, E(j) is at
  0, which is not a when a = 1). The proof uses and proves the window reading (4.5 (3): σ before t_1, resp. t_2). I sign with it.
  **F-2 (wording).** 4.0 says the frozen statement l. 192-204 is REPLACED by 4.4, and 4.4 then refers to [Q FIX l. 384] «the
  packet's list (i) / (ii)» and [Q FIX l. 384] «the lemma's F, B, F′, B′, t_1, t_2», which are frozen l. 195 and l. 197-202 (and P_j, l. 191).
  So those lines stay as definitions; what is replaced is the frame (H2) and the conclusion's first and last sentences.
- **4.5 the proof: correct, no gap left.** Outer induction downwards on j, inner on T. At step T: (1) u_j, v_j, e_j from
  s_(T−1) and γ_T; (2) (C_j((s_(T−1))⁺), E_j(s_(T−1))), which is the inner hypothesis up to T for unit j + 1 — at the first step
  of an inner window E_j(s_(T−1)) belongs to the inner (H1), whose other parts come from our (H1) (first window: REST_(j+1)(0),
  (C_j, E_j)(s_(t−1)) = (0, 0)) or from (R3) of the first inner window (second window: REST_(j+1)(1), and (C_j, E_j)(s_(t_1)) =
  (1, 1) because the pair is split with v_j at c = γ_(t_1)); (3) LEMMA′ for j + 1 at the same T gives σ; (4) the observers. The
  inner hypotheses hold as 4.5 says: first window, the pair split with v_j at c = γ_τ (C_j = 1) and E_j = 1 under a split state,
  u_j held back by EY_j = c, which needs e = c in the quiet stretch; second window, the pair aligned (C_j = 0) and E_j = [a = c]
  = 0 because Y_j = (c, 1 − c) from s_(t_1) on. Step t_2 + 1 above j: STABLE in step form with (R3) of the second inner window.
  (R2): the windows {t}, [t, t_1], [t_1 + 1, t_2], {t_2 + 1} cover [t, last] and each step has a listed mover. The table at the
  end of 4.5 (which of the two input bits each frozen sentence reads) agrees with my trace row by row: the key input is c at
  every step of the window; the value input is a at step t and c after it. This closes G-1: (3) at step T uses the inner
  hypothesis up to T only, which rests on (1) at steps ≤ T and on states up to s_(T−1).
- **4.6: correct.** j = 1, a = 0, t = 1: s⁺(v_0) = 1 for every state (v_0 at 0 is value- and key-enabled, at 1 it is not), so
  γ_τ = 1 for every τ ≥ 1 and E_0(s_τ) = 1 for τ ≥ 1; (H1) under s_0 by the start column. (R1)-(R3) at T = last = 2^k − 2, then
  STABLE with WIRE: s⁺ = s. L(G_k) = 2^k − 2; the stop is «stuck» (A_s(v_1) has two elements).
Signature (L41: the statements 4.3 and 4.4 are referee-originated, REFEREE 36's; this is the independent second signature):
**REFEREE-2 signs 4.1 (S1)-(S4), 4.2 STABLE, 4.3 CAUSAL, 4.4 LEMMA′ with their proofs (4.2, 4.3, 4.5) and 4.6, as printed in
docs/red-b/P-N5-EXP-fixes.md at claude/l-red-b 24f4d436 (sha1 9dc9179f…), (R3)'s range read as t − 1 ≤ τ < last (F-1).**

### A2.4 The concordance claim «PREFIX FORM = LEMMA′ at τ_0 = T»: correct
Read on the sequence s_0, (s_0)⁺, … of (S2), my §2.4 hypothesis at the cut τ_0 is (H2′_T) at T = τ_0 without the guards, and
its conclusion is (R1) ∧ (R2). LEMMA′ ⇒ PREFIX: an unguarded hypothesis implies the guarded one. PREFIX ⇒ LEMMA′ for T ≥ t: by
induction on T the run reaches s_(T−1) ((R2) at T − 1), so every guard of (H2′_T) is true and the hypotheses coincide. What
LEMMA′ has in addition is not new content: T = t − 1 is empty, and (R3) is the list read at T = last from the (H1) state (E(j)
moves once, at step last; the movers of unit j end at REST_j(c); the units above have made two responses, 0 → 1 → 0). LEMMA′ is
the better-formed text ((S2) says what «the step from s_(τ−1)» is at a stop; my «i.e. C_(j−1)(s_τ) = c» presupposed s_τ), so
4.4 is the statement of record and §2.4 is the same lemma. Machine side: at every (H1) triple and every T ≥ t the two
hypotheses have the same truth value and, where they hold, the two conclusions agree (conc_u1, conc_u2 = 0, §A2.5).

### A2.5 DATA on my own code (docs/referee-2/R2-P-N5-EXP/r2lem.py → lem_main.out, lem_u1big.out, lem_drive.out, lem_ctrl.out; every counter «must 0» unless marked)
r2exp.py lineage: my generator and my lane's model; Φ = s ↦ s⁺ is total; C_j, E_j are read off the model's own key and value
comparison; the list is written from the frozen (i), (ii); every clause is evaluated as printed, the guards of (H2′_T) included.
| counter | unit | set | value |
| --- | --- | --- | --- |
| lp_u1 | (triple, T): (H2′_T) true and (R1) or (R2) false | U1 = the run, k = 3..12: 163,840 triples (j, a, t), t ≤ 2^k; 8,109 with (H1) under a reached s_(t−1); 85,937 (triple, T) with a true hypothesis; 4,082 full windows (= Σ (2^(k−1) − 1)) | 0 |
| r3_u1 | window: (R3) false at T = last (range as in F-1) | 4,082 | 0 |
| pre_u1 | (triple, τ_0): my PREFIX form fails | 77,828 cuts with a true hypothesis | 0 |
| conc_u1 | (triple, T ≥ t): PREFIX at τ_0 = T and LEMMA′ at T differ in hypothesis or in conclusion | every T of the 8,109 triples | 0 |
| lp_u2, r3_u2, pre_u2, conc_u2 | the same | U2 = EVERY state with (H1) taken as s_(t−1), t = 1, k = 3..8: 121,368 states (41,368 exhaustive: all of k = 3, 4 and every unit with at most 2^14 lower parts; 80,000 sampled), 30,286 with (H1); inputs end: 6,440 full, 11,464 truncated (4,372 by C, 7,092 by E; longest 6 steps), 12,382 at once; 145,405 (triple, T) | 0 |
| drive | step: both input bits as (H2′) asks and U_j moves otherwise than the list | U3 = driven inputs (the part below U_j disturbed by hand inside a window of the run; not a run of G_k), k = 3..10: 16,000 windows, 3,667 full, 12,333 proper (longest 823 steps), 88,953 steps | 0 |
| causal | state: its triple (s on U_j, E_(j−1)(s), C_(j−1)(s⁺)) was seen with another s⁺ on U_j | every state of k = 3 and k = 4 (512; 65,536: CAUSAL as a function, 576 and 73,792 classes), 16,000 states each for k = 5..8; 228,381 repeated triples | 0 |
| standing | state: s⁺ has a wire or u_0 off 0, or C_0(s) ≠ s(v_0), or E_0(s) ≠ s(v_0) | the same 130,048 states | 0 |
| stab_u1, stab_u2 | (step, unit, b): STABLE's hypothesis true and a mover of the unit moves | 8,164 cases on U1, 510,405 on U2's trajectories | 0 |
| stab_hence, stab_cons | the «hence» clause; the «consequently» clause (420,141 cases with the units above at rest 0) | the same | 0 |
| lp_corner | triple where the frozen wording fails and (H2′_T) holds for some T ≥ t (Remark 1) | the 65 triples below | 0 |
| frozen_noncorner | the frozen wording fails although s_t is reached | U1 and U2 | 0 |
| tfail | k: the run does not stop at exactly 2^k − 2 | k = 3..12 | 0 |
FIRING CONTROL (the Lead's): the RESPONSE LEMMA exactly as frozen fails at (j, a, t) = (1, 1, 2^k − 1) for every k = 3..12
(frozen_at_111 = 10 of 10), and in all at 65 = Σ (k − 1) triples of U1: (1, 1, 2^k − 1) and (j, 0, 2^k − 1), 2 ≤ j ≤ k − 1; its
hypothesis holds at 4,147 triples, so it holds with its conclusion at 4,082, the windows. On U2 it fails at 148 start states, all
fixed points. Other controls (lem_ctrl.out, k = 3..5; each fires its targets): sched (the list shifted by one step: pre, lp,
drive), noE (the hypotheses without their E half: pre_u2, lp_u2 — the E half is needed), noC (without their C half: pre, lp, and
also conc and lp_corner — without the key clause the guards matter), late (the conclusion demanded one step beyond the cut:
pre_u2, lp_u2, drive — the cut is tight), stab (STABLE without C_(i−1)(s⁺) = b), causalE, causalC (CAUSAL's triple without one
input bit), unit (U_(j+1) with the inputs of unit j).
Agreement with the lane's independent tool (its DATA, 4.7 (2), (8); not an input of mine): my exhaustive numbers at k = 3 and
k = 4 are its numbers (7 / 839 (H1) triples whose key input is not c; 8 / 560 full and 3 / 667 proper windows; 30 / 2,428 steps;
576 / 73,792 CAUSAL classes), and its control 5 fails at the same triples as mine.
Runner tests (r2runner.sh → runner.out): T1-T5 and the «every» comparison of §A2.2.

### A2.6 Quotes (r2qfix.py → qfix_pre.out, qfix_pre_ctrl.out)
Entries 2-5 hold 75 tagged quotes (the lane's count too). Checked now, each against its source at the commit the entry names, by
`git show`: 48 quotes — FROZEN 9, REF2 (this report at 33ff0e98) 18, R117 7, R124 8, R57 2 (each restricted to that entry of
RESULTS at trunk 5d7aab0f), R104P 1, KEY1P 2 (claude/l-new 44775605), LNEW 1 (claude/l-new aa29064d): 48 found, 0 missing;
control (one letter of each quote changed): 48 missing. DEFERRED to Addendum 3: the 22 quotes of REF1 and the 5 of PRE, whose
sources are docs/referee/ files I had not opened. So «4.3 and 4.4 ADOPT REFEREE 36's two statements word for word» is not yet
checked by me; what I signed is the text printed in entry 4.

### A2.7 Line L-1 (read; a MATCHES check was not asked)
Every clause that comes from this lane's review agrees with it: part (1) unconditional on R104's definitions, with LEMMA′,
CAUSAL and STABLE in step form named; part (2) Corollary EXP-N5 PROVED-CONDITIONAL on R117's Theorem REACH3 as landed, the
dead-end clause «through R117» and «NO for N5 from S3», and EXP-N5′ as a separate sentence under R124 EXACT-L; part (3) says the
dead end rests on the proof and not on the DATA; the numbers (9k − 16, 18k − 32, 27k − 48, 135k − 230, 176k − 300, 311k − 530,
11·2^(k−2) − 9, 16,368 windows, k − 1 triples, the first k beyond n^c) are right; this lane's row is what §3 says. Three notes
for the Lead: (L-a) the gloss «per unit j a block pair u_j, v_j, an end-follower e_j, two wires wv_j, wu_j and two observer
pairs Y_j, Y′_j» describes the middle units 2 ≤ j ≤ k − 2 only (unit 1 has no e_1, wu_1, Y′_1; unit k − 1 has no e, wire or
Y′), and §6's UNIT j does not contain the wires, which the same line then counts separately («u_0 and the wires never»);
(L-b) R117's premises are paraphrased (R117's title line also has «in its two forms», «Lemma R», «and (R1) ruling», «Lemma P1 on
the dual game»): quote the parenthesis; (L-c) L41 asks for a scope tail naming the referee-originated statements (CAUSAL and
LEMMA′, REFEREE 36) with both signatures quoted; the second one is the bold sentence of §A2.3.

### A2.8 Reproduction (from the repository root)
- `git show 24f4d436a0fea1f62ae736f20f78ff9e84333a90:docs/red-b/P-N5-EXP-fixes.md > FIX` (sha1 9dc9179f…); frozen guard:
  `git show 24f4d436:docs/red-b/P-N5-EXP.md | sha1sum`; `git show 06d399c2:docs/red-b/P-N5-EXP-fixes.md > E1; cmp -n 12551 E1 FIX`.
- `python3 -B docs/referee-2/R2-P-N5-EXP/r2lem.py 3 4 5 6 7 8` → lem_main.out (about 1 minute); `… r2lem.py --u1only 9 10 11 12` →
  lem_u1big.out; `… r2lem.py --u3only 9 10` → lem_drive.out; `… r2lem.py --ctrl NAME 3 4 5` for sched, noE, noC, late, stab,
  causalE, causalC, unit → lem_ctrl.out (the TOTAL and FIRED lines).
- `python3 -B docs/referee-2/R2-P-N5-EXP/r2qfix.py FIX --from 126 --defer REF1,PRE FROZEN=350d84eb:docs/red-b/P-N5-EXP.md
  REF2=33ff0e98:docs/referee-2/R2-P-N5-EXP.md R117=5d7aab0f:docs/RESULTS.md#R117 R124=5d7aab0f:docs/RESULTS.md#R124
  R57=5d7aab0f:docs/RESULTS.md#R57 R104P=5d7aab0f:docs/red/P-N5-REALIZE.md KEY1P=44775605:docs/new/P-N5-KEY1P.md
  LNEW=aa29064d:docs/new/P-N5-KEY1P-after-EXP-draft.md` → qfix_pre.out (with --ctrl → qfix_pre_ctrl.out).
- `bash docs/referee-2/R2-P-N5-EXP/r2runner.sh WORKDIR every` (WORKDIR a new directory outside the tree) → runner.out.
Not done: entry 1's DATA subsections 9.8-9.13 and the lane's N5 runs were not re-run (DATA, not to sign; CHECKER's re-run);
the other lanes' numbers cited in 5.8 were not opened.

DONE: fixes-file check of entries 1-5 (item by item), the L41 cross-check of entry 4 (re-derivation, own checker with a firing
control), the concordance claim, the frozen guard.
FINDINGS: every item of this lane is closed (G-1, M-1, W-1, W-2, D-1, A1.1, A1.2); I sign LEMMA′, CAUSAL and STABLE in step form
as printed (reading F-1); «PREFIX FORM = LEMMA′ at τ_0 = T» is correct; the frozen wording fails only at the k − 1 stop triples,
and my §0 was wrong to sign that wording (§A2.1); F-2, F-3 wording; F-4 the new runner run_b6fix.sh exits 0 on a failing stage
(no DATA affected: eleven files byte-equal on re-run); F-5 a label inside (a′). P-N5-EXP: SIGNED with fixes entries 1-5.
NEEDS: Lead: L41's scope tail in the line (L-c), and F-1's range if the line or a later entry restates (R3); L-RED-B: F-4.

## Addendum 3 (REFEREE-2 successor 42; 2026-11-13T17:26:55Z by date -u): AGREEMENT NOTE with the first referee's report, and the 27 deferred quotes
Asked by the Lead (brief of 15:55Z, item 2). Written after Addendum 2 was committed (f17a2708, 17:02:13Z) and its SHA sent to the
Lead (17:03Z); only then were the first referee's files opened.
- Read: docs/referee/R-P-N5-EXP.md at claude/referee 7ca9c2b4596eb5185976aca9303696287a6e52e6 (496 lines, sha1 1dde3812…; stage 1 =
  its first 397 lines = the file at c881709b, sha1 c662d157…, byte for byte; stage 2 §10 at ea09ae2e; stage 3 §11), in full.
  REFEREE 36 is the first referee; REFEREE 35's pre-check (docs/referee/R-GK-precheck.md at 06ac891d) was opened only by the quote
  checker. Not opened: docs/referee/scratch/ (its tools and logs) and its review of P-N5-KEY1P.
- Timeline of independence: this lane's review 33ff0e98 (14:16:52Z) and Addendum 1 (14:39:51Z); REFEREE 36's stage 1 is stamped
  14:56Z and says REFEREE-2's reports were not read before it; neither report cites the other.

### A3.1 The deferred quotes (r2qfix.py → qfix_all.out, qfix_all_ctrl.out)
All 75 tagged quotes of entries 2-5 are verbatim in their sources at the commits the entries name: the 48 of §A2.6 and now REF1
22 of 22 (c881709b) and PRE 5 of 5 (06ac891d); control: 75 missing. In particular entry 4's standing paragraph, CAUSAL, LEMMA′
and STABLE's step form are REFEREE 36's l. 200-202, 203-204, 219-225 and 257-261 word for word. So the text I signed in §A2.3 IS
the referee-originated text, and L41's two signatures are on the same statements: its author's ([Q REF1 l. 17] «NOT SIGNED AS
WRITTEN; SIGNED in the form LEMMA′ of §5.3 below») and mine (§A2.3, the bold sentence).

### A3.2 Verdicts, statement by statement
| statement | REFEREE 36 (§0) | REFEREE-2 (§0 with Addendum 2) | same? |
| --- | --- | --- | --- |
| Lemma MEMBER = (a) | SIGN with E-3 | SIGN with M-1 | yes; E-3 = M-1 |
| MOVE-2 | SIGN | SIGN | yes |
| V0-V4, K1-K4 | SIGN with E-4 | SIGN; 4.1 (S1) signed in Addendum 2 | yes after the fixes; E-4 was not an item of mine |
| WIRE | SIGN | SIGN | yes |
| RESPONSE LEMMA | NOT signed as written (E-1, E-2); signed as LEMMA′ | 33ff0e98: «SIGN the statement», gap G-1; corrected in §A2.1: the statement signed is 4.4 | yes after §A2.1; E-2 = G-1; E-1 was missed by this lane |
| STABLE | SIGN with E-5 | SIGN; step form signed in Addendum 2 | yes after the fixes; E-5 was not an item of mine |
| Theorem EXP-IDEAL (b), (c) | SIGN through LEMMA′ | SIGN through the lemma with G-1 closed | yes |
| Corollary EXP-N5 | SIGN AS CONDITIONAL on R117's premises as landed (P-1) | SIGN as PROVED-CONDITIONAL on R117 Theorem REACH3 as landed (W-2); n, m signed outright | yes; P-1 = W-2 |
| Dead-end paragraph | conditional, P-1 and E-7 | conditional, W-2 | yes; E-7 was not an item of mine |
| §8 | CHECKED, correct (O-2) | checked against the proofs; «Nothing else» tested only for the gate renumbering and the rank tie | yes; its test is the stronger one (1,200 random orders) |
| §9 DATA, quotes | reproduced on own tools; 27 of 27 quotes; E-6 | reproduced on own tools; 27 of 27; D-1 | yes; E-6 = D-1 |
No verdict differs after the fixes, and no number differs anywhere: L(G_k) for k = 3..14, the switch counts and 11·2^(k−2) − 9,
n = 135k − 230, m = 176k − 300, the first k beyond n^c and (n + m)^c (23, 37, 51; 26, 41, 57), the tie counts 0, 2, 6, …, 42,
2^k + 1 iterations with the fallback at 2^k − 1, the 27 quotes and the same four untagged ones.

### A3.3 Items, by number
| REFEREE 36 | this lane | relation |
| --- | --- | --- |
| E-2 (the induction applies the lemma for j + 1 before its (H2) is known; prefix form needed) | G-1 | the SAME gap, found independently, with the same repair (LEMMA′ / PREFIX FORM; §A2.4: one lemma) and the same explanation (the inner hypothesis is produced step by step by the outer unit) |
| E-1 ((H2) vacuous after the stop; false at (1, 1, 2^k − 1), and at s_L for every j ≥ 2 with a = 0) | — (missed); §A2.1 | THEIRS ONLY. This lane signed the frozen statement. Confirmed now by my own control: exactly its k − 1 triples per k, k = 3..12, and nowhere where s_t is reached |
| E-3 (rank key not injective on wire options, k ≥ 4; tie by β-id; run independent of the tie order) | M-1 | the same finding, the same counts (2, 6, 10, …), the same test (reverse tie order: same run) |
| E-4 (standing assumption needs u_0 at 0) | — | THEIRS ONLY as an item. This lane's §2.2 wrote «while u_0 is on 0» and tested only states with u_0 at 0, so it used the right assumption without saying that the packet's sentence lacks it. Confirmed (counter standing 0; its counters with u_0 free fire) |
| E-5 (STABLE read under one state is false; key bit under s⁺) | — | THEIRS ONLY as an item. This lane's §2.5 read the key bit of the step silently. Confirmed (4.2 signed; control stab: 9,165 failures without C_(i−1)(s⁺) = b) |
| E-6 (§9.7 placeholder) | D-1 | the same |
| E-7 («CORRECT on these games»: DATA for k ≤ 11, R57 (b) for every k) | — | THEIRS ONLY. This lane's §4 called the answers MEASURED and did not ask the packet's sentence to name R57 (b). Entry 2 (e) is right |
| P-1 (R117's premises in the Corollary and the dead-end sentence) | W-2 | the same |
| O-1 (optional: R124 EXACT-L for the exact count) | Addendum 1 A1.1 | the same premises listed; it says optional, this lane recommended it as a separate sentence; entry 3 is that sentence |
| O-2 (only δ(v_j, o) > δ(u_j, 1 − o) is read) | — | THEIRS ONLY (a note); consistent with V1's split case, which is all §2.2 uses |
| N-1 («DEFINITIONS ONLY» is right; the order is R104's Fact X sentence) | — | THEIRS ONLY (a note); the same point from another side is S-1 of my box 108 review |
| — | W-1 («step t» never defined) | MINE ONLY; its 5.1 states the reading; closed by 4.1 (S2) |
| — | O-1 (my Γ3 builder numbers the β block in gate order) | MINE ONLY, about my own tool; its counter PG (games identical vertex by vertex) is the same check from its side |
| 10.E: not reproduced | A1.2 tested (T1-T3); F-4 | MINE ONLY: the new runner run_b6fix.sh exits 0 on a failing stage |
| LEMMA′ (R3) as printed | F-1 | MINE ONLY: «for τ < last» needs the lower end t − 1; its own test (econ) is on the invocation window, so the reading is the one it tested |
| — | F-2, F-3, F-5 | MINE ONLY, on entries 2-5, which are later than its three stages |

### A3.4 Where the two reviews differ in what was tested (no conflict; each covers what the other does not)
- LEMMA′. REFEREE 36 tests an ABSTRACT unit machine built from the bit formulas of §5: under a held input for every unit and both
  a (abs, k ≤ 9), and one unit against a contract of the unit above with ARBITRARY delays (unit, stage 2), which is the induction
  step for every k at the level of the formulas; the formulas are tied to R104's definition by its static counters and by
  causal. I test the DEFINITIONS themselves (the model's own value and key comparisons, never a formula) on the real run (k ≤ 12),
  on every state satisfying (H1) (k ≤ 8; 11,464 truncated inputs), on driven inputs (proper prefixes up to 823 steps), and CAUSAL
  as a function on all states of k = 3, 4. Neither is the proof; the proof is 4.5, which both referees checked line by line.
- N5 itself. REFEREE 36: its lane's builder and engine on its own genome, k ≤ 9 (successor 35: k ≤ 12), games identical to the
  lane's files, firing controls for every run-level counter, R117's lemmas on perturbed games, positional strategies with its
  own verifier (stage 2). This lane: own builder and engine, k ≤ 11, the answer against four solvers (two Zielonka, Oink zlk and
  tl). Different engines and builders, the same counts.
- §8. REFEREE 36 draws 1,200 random gate and rank orders satisfying §8's list (same run) and breaks each constraint; I did not.
- Box 108. REFEREE 36 (stage 3) compared it with the packet and says [Q REF1H l. 465] «its STEP table (32 transition classes)
  was not checked row by row»; my R2-box108.md checks every row. Its dictionary (H_i = P_i; S0 → S6 = the response from rest 0)
  and its remark that the stop has exactly v_1, …, v_(k−1) unstable are also what I found (my counter stop).

### A3.5 What remains open between the two reviews
Nothing that touches a statement. For the Lead's line: F-1 (the range of (R3), a wording of the referee-originated statement
that its author can confirm in one line) and L-c (L41's scope tail). For L-RED-B: F-4. For this lane: the second review of
P-N5-KEY1P stays deferred; REFEREE 36 has a first review of it on origin (claude/referee a85626aa, by its commit subject; not
opened), so entry 2 (a′)'s second sentence (F-5) has one referee behind its Lemma IDEAL-1P and not yet two.

DONE: agreement note; the 27 deferred quotes (75 of 75 verbatim).
FINDINGS: the two reviews agree on every verdict and every number after the fixes; the same gap (E-2 = G-1) and the same rank
tie (E-3 = M-1), placeholder (E-6 = D-1) and condition (P-1 = W-2) were found independently; E-1, E-4, E-5, E-7 are REFEREE 36's
alone (E-1 was a miss of this lane, corrected in §A2.1; E-4 and E-5 were right readings this lane used without flagging the
text); W-1, F-1 to F-5 are this lane's alone. LEMMA′ and CAUSAL in entry 4 are REFEREE 36's text word for word: L41 is met.
NEEDS: Lead: none beyond §A3.5.
