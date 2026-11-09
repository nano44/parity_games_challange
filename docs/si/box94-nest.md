# Box 94: NESTED MW / doubler counters — do ch(D), gate flips, C, T3 multiply across levels? (L-SI successor 49; Lead 04:57Z 2026-11-09)
Written 2026-11-09 (date -u in the commit). Labels: PROVED (lane, unrefereed) / CONJECTURE / DATA (unit, set, scope, counter) / DEAD /
READING. Nothing here is a TARGET.md claim. G-N5-TIME stays OPEN. N5′-xi stays a CANDIDATE (D1). No counterexample candidate.
Brief (Lead 04:57Z): by E-FACE-PAYS (box 93) a gate flips super-linearly only if its e-face continuation D changes super-linearly; build a
NESTED design (an MW / MWR hub whose gate continuation is the hub of a second MW-type counter, 2-3 levels) and measure whether ch(D), gate
flips, C, T3 MULTIPLY or only ADD; say which lemma forces the addition.
Tools: experiments/si/box94/ (gennest94.py: H copies of box 90's MW(n, 2) with link / order / clock options and DOUBLER levels; lev94.py:
per-level change census; run94.sh; check94.sh, wired). Engines (two on every number): own = L-RED R221 own.py (claude/l-red 4b309716);
g3 = L-NEW's Γ3 N5′-xi from S3 (claude/l-new fcba92fc); counters mult91 (T3, C) and np93 (gate flips) of boxes 91 / 93.

## 0. Answer
- They ADD (or copy). Nothing MULTIPLIES. On every nested genome built (6 families × H = 2, 3 × n = 4, 8 frozen, plus a 126-point
  own-engine sweep), C and the max gate flips equal those of ONE MW(n) (C = 2n + 1, max flips 4n + 2), and T3 equals one MW(n)'s
  (6n + 7) when the levels run on simultaneous clocks, or the SUM of the levels' run lengths when they run one after another (NSQ: T3 103 / 271 at H = 2 / 3, N + M 505 / 1369,
  T3 / (N + M) ≤ 0.21: still linear). Both
  engines IDENTICAL on every frozen row.
- Where the factor 2 lives, and why it does not compound:
  - MW's race gate Q does double: ch(g_Q) = flips(g_Q) = 2·ch(v) = 2·ch(D) (v = D's successor). DATA: it is an exact ONE-STEP ECHO,
    S(g_Q) = S(v) ∪ (S(v) + 1) (S(x) := the steps at which x's value changes), on both engines, on level 1 of every family and on every
    level of NP (simultaneous clocks); not on NSQ's later levels (ch(v_2) 13, ch(g_Q2) 22, flips 18), which are still additive.
  - An echo composes by UNION of step sets, not by multiplication: ch(x) = |S(x)| ≤ T3 for every vertex (Lemma STEP-BOUND, §1, trivial),
    so value-change counts can multiply across levels only if T3 does. S ∪ (S + 1) ∪ … ∪ (S + h) has at most (h + 1)·|S| elements.
  - A level that READS the lower hub instead of running its own letters only COPIES it: **Lemma SAME-SUFFIX (PROVED, lane; §1)**: if
    both faces of a gate (or all options of an Even mover) end in the same vertex's play behind prefixes that stay constant inside one
    Λ-interval, the choice there never changes. The DOUBLER levels (v_j → R_(j−1)) are exactly that case: their gate never flips and every
    level-j vertex changes value exactly when R_(j−1) does (DATA: S(R_j) = S(R_(j−1)), flips(g_Qj) = 0).
  - A level that keeps its OWN letters and gets a link to the lower level runs in parallel on its own clock: the link option is either
    never chosen (own letters more relevant) or makes the upper level die (REV order: the lower letters dominate, the upper race never
    starts). Either way the counts are max (simultaneous) or sum (sequential), never product.
- Which lemma forces addition: per design, (i) SAME-SUFFIX (doubler / follower levels: copy); (ii) STEP-BOUND + the echo (one gate's
  doubling is a time shift, so stacking adds one step set per level); (iii) GATE-RACE's min (box 91 §3) with
  E-FACE-PAYS: in ND (level j's Highs read R_(j−1)) v_2 changes 17 = 9 own + 8 imported at n = 4 (33 = 17 + 16 at n = 8): the imports
  ADD to the continuation's changes, and the race gate Q_2 still changes 18 (34) times, its own count, because its β-face R_2 does not
  import them (flips ≤ 2·min(ch_pe, ch_pb) + 1). For the
  parallel designs no lemma is needed: they are two independent runs (DATA).
- What a multiplying design would need (READING, not built): a level that, between two consecutive changes of the lower hub, runs a full
  re-arming sub-run of its OWN gates; by E-FACE-PAYS each of those re-locks needs a change of its own continuation, and by SAME-SUFFIX
  those changes cannot all come from the lower hub through common suffixes. That is the open core again (c_y at the continuations).

## 1. Lemmas
**Lemma STEP-BOUND (PROVED, trivial).** For every vertex x, ch(x) = |S(x)| ≤ T3, and S(x) ⊆ {t : some vertex of x's play at t − 1 changes
successor at t}. (A value is a function of the play; the play changes only if a successor on it changes.) ∎
- Consequence: «ch multiplies across levels while T3 stays linear» is impossible; multiplication of ch needs multiplication of T3.

**Lemma SAME-SUFFIX (PROVED, lane; premises [VJ] valuation, LOC-GATE3, NO-TIE3 for gates; Howard's greedy switch for Even movers).**
Let W be a window of steps inside one Λ-interval of a vertex o, y a vertex, and for each successor f of o a path P_f from f to y, all
constant on W, such that at every t ∈ W the play of each f is P_f followed by y's play at t, and y's play at t avoids every P_f. Then
the order of the successors' values is the same at every t ∈ W; so if o is Odd, σ̄_t(o) is constant on W, and if o is Even, σ_t(o) is
constant on W from its second step on.
Proof. Fix f, f′. Both plays end in the same cycle (y's), so Λ is equal; [VJ] compares the sets of vertices more relevant than Λ on the
two plays by the most relevant vertex of their symmetric difference, which lies in P_f Δ P_f′ (y's play is common and disjoint from
both prefixes): constant on W. If the two sets are equal, [VJ] compares lengths, |P_f| − |P_f′| constant. So the comparison is constant.
Odd plays the ◁-least face, unique by NO-TIE3; Even's Howard switch at t picks a ▷-best option for the values at t − 1: constant from
the window's second step. ∎
- Use: the DOUBLER gadget (gennest94 DBL): v_j → R_(j−1), hv_j → v_j, gate Q_j with W-target hv_j and Ξ-target R_j, R_j: race → Q_j
  and → v_j (and / or → R_(j−1)). When R_j is off the race, both faces of Q_j end in R_(j−1)'s play behind fixed prefixes: Q_j is
  constant; R_j's options all end in R_(j−1)'s play: R_j is constant. Level j copies level j − 1 (S(R_j) = S(R_(j−1))).
- Scope: SAME-SUFFIX needs a common suffix AND one Λ-interval. MW's own race gate escapes it because Q's β-face R has options into the
  Highs and qz whose plays do not share v's suffix; that independence is what produces the echo.

## 2. DATA (two engines; unit: genome / level; set: inst/ (SHA1SUMS); scope: own to the end, cap 3000; g3 to the first fallback, cap
## 20000; T3 = Howard steps; C per (v, I, y), per-tuple maximum; flips per gate, maximum; ch per vertex, whole run)
Families (gennest94.py; n = 4, 8; H = 2, 3): NP (LINK=u: level j's race mover u_j gets an option to qz_(j−1); levels on simultaneous
clocks), NV (REV=1, LINK=v: lower letters more relevant, v_j → R_(j−1)), ND (LINK=D: level j's Highs' W-target = R_(j−1)), NDV / NDB
(DOUBLER levels, R_j → v_j / both), NSQ (LINK=u, SCALE 3, OFFJ 24: level j's clock 3× slower and later, so levels run one after another).
| instance | N + M | T3 | C | max gate flips | per level j: ch(v_j) / ch(g_Qj) / flips(g_Qj) / echo |
| --- | --- | --- | --- | --- | --- |
| ND2_4 | 288 | 31 | 9 | 18 | L1 9 / 18 / 18 / 1; L2 17 / 18 / 18 / 0 |
| ND2_8 | 520 | 55 | 17 | 34 | L1 17 / 34 / 34 / 1; L2 33 / 34 / 34 / 0 |
| ND3_4 | 431 | 31 | 9 | 18 | L1 9 / 18 / 18 / 1; L2 17 / 18 / 18 / 0; L3 17 / 18 / 18 / 0 |
| ND3_8 | 779 | 55 | 17 | 34 | L1 17 / 34 / 34 / 1; L2 33 / 34 / 34 / 0; L3 33 / 34 / 34 / 0 |
| NDB2_4 | 155 | 31 | 9 | 18 | L1 9 / 18 / 18 / 1; L2 18 / 18 / 0 / 0 |
| NDB2_8 | 271 | 55 | 17 | 34 | L1 17 / 34 / 34 / 1; L2 34 / 34 / 0 / 0 |
| NDB3_4 | 165 | 31 | 9 | 18 | L1 9 / 18 / 18 / 1; L2 18 / 18 / 0 / 0; L3 18 / 18 / 0 / 0 |
| NDB3_8 | 281 | 55 | 17 | 34 | L1 17 / 34 / 34 / 1; L2 34 / 34 / 0 / 0; L3 34 / 34 / 0 / 0 |
| NDV2_4 | 154 | 31 | 9 | 18 | L1 9 / 18 / 18 / 1; L2 18 / 18 / 0 / 0 |
| NDV2_8 | 270 | 55 | 17 | 34 | L1 17 / 34 / 34 / 1; L2 34 / 34 / 0 / 0 |
| NDV3_4 | 163 | 31 | 9 | 18 | L1 9 / 18 / 18 / 1; L2 18 / 18 / 0 / 0; L3 18 / 18 / 0 / 0 |
| NDV3_8 | 279 | 55 | 17 | 34 | L1 17 / 34 / 34 / 1; L2 34 / 34 / 0 / 0; L3 34 / 34 / 0 / 0 |
| NP2_4 | 289 | 31 | 9 | 18 | L1 9 / 18 / 18 / 1; L2 9 / 18 / 18 / 1 |
| NP2_8 | 521 | 55 | 17 | 34 | L1 17 / 34 / 34 / 1; L2 17 / 34 / 34 / 1 |
| NP3_4 | 433 | 31 | 9 | 18 | L1 9 / 18 / 18 / 1; L2 9 / 18 / 18 / 1; L3 9 / 18 / 18 / 1 |
| NP3_8 | 781 | 55 | 17 | 34 | L1 17 / 34 / 34 / 1; L2 17 / 34 / 34 / 1; L3 17 / 34 / 34 / 1 |
| NSQ2_4 | 505 | 103 | 9 | 18 | L1 9 / 18 / 18 / 1; L2 13 / 22 / 18 / 0 |
| NSQ3_4 | 1369 | 271 | 9 | 18 | L1 9 / 18 / 18 / 1; L2 13 / 22 / 18 / 0; L3 17 / 26 / 18 / 0 |
| NV2_4 | 289 | 31 | 9 | 18 | L1 9 / 18 / 18 / 1; L2 18 / 18 / 2 / 0 |
| NV2_8 | 521 | 55 | 17 | 34 | L1 17 / 34 / 34 / 1; L2 34 / 34 / 2 / 0 |
| NV3_4 | 433 | 31 | 9 | 18 | L1 9 / 18 / 18 / 1; L2 18 / 18 / 2 / 0; L3 18 / 18 / 2 / 0 |
| NV3_8 | 781 | 55 | 17 | 34 | L1 17 / 34 / 34 / 1; L2 34 / 34 / 2 / 0; L3 34 / 34 / 2 / 0 |
| (MW4_2 / MW8_2, one level, box 91) | 145 / 261 | 31 / 55 | 9 / 17 | 18 / 34 | L1 9 / 18 / 18 / 1; 17 / 34 / 34 / 1 |
- Every column above is IDENTICAL on the two engines (out/mult94_*.out, np94_*.out, lev94_*.out; own and g3).
- Sweep (own engine only; H = 2, n = 4; LINK ∈ {u, R, D, Dz, zR, v, vQ} × REV ∈ {0, 1} × SCALE ∈ {1, 2, 3} × OFFJ ∈ {0, 12, 24}; 126
  genomes; out/sweep94_own.out): C max 9 (= MW(4)'s 9), max gate flips max 18 (= 18), T3 31-103 (T3 > 31 only with SCALE > 1 and OFFJ > 0: the levels run one after another)
- H = 1 reproduces box 91's MW8_2 byte for byte (check94).

## 3. What this closes and what it does not
- DEAD (DATA): nesting MW-type counters by a link edge, by replacing the High's continuation with the lower hub, or by follower
  (doubler) levels, at H = 2, 3: no product growth in ch, gate flips, C or T3.
- PROVED: SAME-SUFFIX (followers copy), STEP-BOUND (ch ≤ T3).
- NOT proved: that no nesting multiplies. A design with a self-clocked re-arming sub-run per lower change is not excluded; it needs
  continuations that change independently of the lower hub (E-FACE-PAYS + SAME-SUFFIX), which is the core. No instance to send.
