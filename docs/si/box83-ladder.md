# Box 83: LADDER-R built and measured (h = 2..6); the obstruction is Lemma LOCK-UP (L-SI successor 44)
Lead GO BOX 83 (01:17Z 2026-11-08). Design: docs/si/box82-cyctower.md §5 (constraints K1-K6, design §5.2, test §5.3). Written 2026-11-08T01:28Z (date -u).
Labels: PROVED (lane, unrefereed) / PROVED-CONDITIONAL (named premise) / CONJECTURE / DATA (unit, set, scope, counter) / DEAD (instance).
Nothing here is a TARGET.md claim. G-N5-TIME stays OPEN. N5′-xi stays a CANDIDATE (D1).
Tools: experiments/si/box83/ (gen83.py DSL, ladder83.py builder, meas83.py, lock83.py, trace83.py, sweep83.sh, check83.sh; wired
in experiments/si/check.sh). Runners: the pinned box81 copies (idealcyc, gamma3, n5v) via census81 / real81, anal82, and xchk81, the independent implementation.

## 0. Answer
- Built: LADDER-R at h = 2 in three forms (§1). Every form has one gate pair per level ≥ 1 with UP β-faces to the level-(l + 1) mover,
  the carry as the hub play's own upward Ξ-edge, no access options (K5), and RS2-style delay lanes exiting to the level-(l + 1) mover.
- §5.3 test at h = 2 (DATA, §3):
  - Literal form: FAILS. The run is 00 → 01 → 11 with no reset. RF = [0, 1, 1], hub e-set height 3.
  - With a continuation lane F_l on SET_l's W-side: a full 2-bit cycle 00 → 01 → 11 → 10 → 11. Bit 1 resets one step after the carry
    (Howard's lag), then re-sets. Hub e-set height 4 (∅ < {e1} < {e2} < {e1, e2}). No premature reset.
  - But RF(1) = 3 = 2·RF(2) + 1, so the criterion RF(1) ≥ 2·RF(2) + 2 FAILS by one.
- h = 3..6 (§3): NO DOUBLING. The carry into bit 3 resets bit 2 but never bit 1 (111 → 101 → 111; 100 is skipped). For h = 3, 4, 5, 6:
  RF(l) ≤ 3 at every level, and R = 7 at every h (continuation forms; R = 3 for the literal form).
- DEAD (as a counter; frozen instances §1). Exact obstruction: K6 in an access-free form, Lemma LOCK-UP (§2, PROVED-CONDITIONAL on
  E-MON only, for the persistence clause).
  - Once a bit is on SET, its continuation reaches the next bit's mover X e-free, and E(X) ≠ ∅, the bit never leaves SET for the rest
    of the Λ-interval.
  - Corollary LADDER-2: in the whole LADDER-R class, every bit adopts SET at most twice and resets at most once per Λ-interval.
- The exits do see the carry before the chain, as K6 asked. But they never un-see it: E(X) is lex non-decreasing (E-MON), so it stays
  nonempty, and the lane cannot re-arm.
- Re-arming a bit therefore needs one of three things:
  - (a) a Λ change (a C-step; R118 (e) bounds C);
  - (b) an alternative of the bit reaching an e above e_SET that is not on X's play: an access route, which K5 / LEAK-ARCH forbid;
  - (c) the bit's alternatives and its continuation routed to DIFFERENT higher movers X ≠ X′. That is the R218 §4 hub pair (RUNG-ALT),
    the only open way out.
- Measured as the Lead asked (DATA, §3):
  - R, C, RF per level, hub e-set height, U(G), and ascents (up to 5 at h = 6, harmless as R221 §2 said).
  - Σ_v D^tot_E(v) (definition in §3), from 155 (LR2_none) to 2,203 (LR6_exitup), i.e. linear in n.
  - N5′-xi on Γ3: T + 3 iterations, 1 fallback, mover phase = Howard (consistent with L-RED 56's CONJECTURE ENDGAME-3).

## 1. The builds (ladder83.py; frozen in experiments/si/box83/inst/, sha1 in pins.sha1)
Format: RESULTS R104's IDEAL genome (W-targets exactly one level down, none at level 0; e above every β; [E-LEV] e-order by
(level, gate)). Bits B_1..B_h, B_l at level l; T := B_(h+1) is a top mover of level h + 1 that escapes.
- B_l's options:
  - UP_l: β → B_(l+1); its e-face goes to a dummy, so Odd never takes it.
  - lane_(l,j): β → helper a_(l,j); dead e-face.
  - SET_l: W-target w_l, Ξ-target B_l itself, even β. Start = UP.
- Dummies D_l (level l): an even self-cycle of top β. An e-face into D_l is never taken by Odd.
- Delay lanes (RS2 style, R217 §11): helper a_(l,j) has an even β rising in j and leads to lane mover b_(l,j). b_(l,j) has EXIT (odd β → B_(l+1))
  or CHAIN (odd β → b_(l,j−1); b_(l,0) → bonus d_l with a top even β). All at level 0, so every gate there is dead.
- Hub H (level 0): β → B_1.
- SET_l's continuation (FL mode):
  - none (the literal §5.2): w_l (level l − 1) has one option, β → B_(l+1). The carry is the hub's own upward Ξ-edge.
  - exitup: w_l = f_(l,0) of a lane F_l of M_l movers at level l − 1. Each f has EXIT (β → B_(l+1)) or CHAIN (β → f_(l,i+1);
    the last → bonus c_l → u). Dead e-faces.
  - chainup (RS2's F0): each f has EXIT (β → X_l, a forced-escape SET-type mover of level l whose e_x lies below e_l) or CHAIN
    (β → f_(l,i+1); the last → B_(l+1)).
- Variant UPE=1 (sweep only): UP_l's e-face goes to a level-(l − 1) mover y_l with β → B_(l+1), so Odd has a real choice at UP_l.

| instance | args (h; L; FL; M) | sha1 (genome .json) |
| --- | --- | --- |
| LR2_none | 2; 1,4; none | df3ffc3c9488aac5551d0c9f50da4fa5d1ea2879 |
| LR2_exitup | 2; 1,4; exitup; 2,2 | aa9ae7a5149a707c49098bca177626dbaea5abe3 |
| LR2_chainup | 2; 1,4; chainup; 2,2 | 7f7d80dffaa5387abd19375040a962080d5f5deb |
| LR3_exitup | 3; 1,4,7; exitup; 2,2,2 | 8868cdea2d2d830cfa4150cdab8c4ffb5184df75 |
| LR3_chainup | 3; 1,4,7; chainup; 2,2,2 | ad76dc14bae953c3b633b9084e43f2a0667014fa |
| LR6_exitup | 6; 1,4,7,10,13,16; exitup; 2×6 | 15b96ca3bc6972c85957d6a4ec1b7ae77826aff7 |
(sha1 of the working-tree files at the commit that adds them; re-take with `git show <that commit>:path | sha1sum`.)
DSL check: gen83 reproduces L-RED's RS2 genome byte for byte (rs2port83.py 4 3 = box81/inst/RS2.json; in check83.sh).

## 2. Lemma LOCK-UP and Corollary LADDER-2
Setting: IDEAL-CYC(G) Howard (RESULTS R118's model; Odd plays an optimal counterstrategy; Howard moves a mover only to a strictly better
option, ties kept). E_s(v) = the set of e-vertices of the play from v at state s. u = K0. Values are compared as in VJ: reward of the cycle
node first, then the most relevant vertex z of the symmetric difference of the path sets.
Definitions.
- A gate is DEAD if every play from its e-vertex ends in an even cycle node, while the play from its β-face ends at Λ(u), which is odd.
  So Odd takes β there. Examples: e → c_W at level 0, and e → a dummy D.
- Fix a mover B, an option S = (W-target w, Ξ-target B, even β_S) of B, and a mover X ≠ B.
- Y is a finite set of movers, not containing B or X, with w ∈ Y. Y is X-CLOSED if every option of every y ∈ Y has a dead gate and
  a Ξ-target in Y ∪ {X} ∪ Z ∪ {u}, and the Ξ-graph restricted to Y is acyclic.
- Z (low sinks) is a set of movers whose plays, at every state considered, end at Λ(u) and pass only e-vertices less relevant than e_S.
- A_s := {y ∈ Y : the play from y at s reaches X before any e-vertex}.

**Lemma LOCK-UP (PROVED, lane; the persistence clause (P) uses E-MON, P-N5-ASC §3 @ claude/l-new 95dc76d7, PROVED lane, survived
L-RED R220).**
Hypotheses:
- Y is X-closed.
- Every option of B other than S has its Ξ-target in Y ∪ {X} ∪ Z ∪ {u}.
- I is an interval of states on which every vertex keeps its cycle node.
- On I: Λ(X) = Λ(u), and X's play passes neither B nor a mover of Y.
- At t ∈ I: σ_t(B) = S, Odd takes e at S's gate g_S, w ∈ A_t, and the most relevant element of E_t(X) is more relevant than e_S
  (so E_t(X) ≠ ∅).
Claim: for every s ∈ I with s ≥ t, σ_s(B) = S and w ∈ A_s.
Proof. (P) First, E-MON gives E_s(X) ≥ E_t(X) in lex order (= numeric order of the 0/1 words, R221 NO-REFLECT). So top(E_s(X)) is at
least as relevant as top(E_t(X)), and hence more relevant than e_S, for all s ≥ t in I. Now induct on s.
- (i) Odd takes e at g_S at s.
  - At t, B's play is B g_S e_S w … X …, so Λ_t(B) = Λ_t(X) = Λ(u).
  - If σ_s(B) = S and Odd took β at g_S, B's play would be the cycle B g_S β_S B, with cycle node β_S. But β_S ≠ Λ(u), and Λ(B) is
    constant on I. Contradiction.
- (ii) Values of B's options at s, given σ_s(B) = S and w ∈ A_s.
  - The play from g_S has cycle node Λ(u) and e-set {e_S} ∪ E_s(X). The route from w to X passes no e. Also e_S ∉ E_s(X): e_S's only
    in-edge is from g_S, whose only in-edge is from B, and X's play does not pass B.
  - Take any other option o. Odd minimises, so Ω_s(g_o) ⊴ ext(g_o, Ω_s(β_o)).
  - The play from β_o enters Y ∪ {X} ∪ Z ∪ {u}. Inside Y it passes only β's, dead gates (β-face) and Y-movers, and it leaves Y because
    Y is acyclic. So either it reaches X before any e, with e-set E_s(X), or it reaches Z or u, with only e's less relevant than e_S.
    In both cases its cycle node is Λ(u).
  - With equal cycle nodes, K0 and K3 lie on both plays or on neither (E-MON's proof, P-N5-ASC §3). Every other vertex more relevant
    than an e is c_W, which is never on such a play. So z is the most relevant e of the symmetric difference.
    - Case X: the symmetric difference of the e-parts is {e_S}, so z = e_S.
    - Case Z / u: the S-side contains e_S and top(E_s(X)), both more relevant than every e on the other side, so z lies on the S-side.
  - z is even, so S ▷ o strictly. Howard keeps S: σ_(s+1)(B) = S.
- (iii) A_s ⊆ A_(s+1).
  - Let y ∈ A_s. Its current option leads e-free into A_s ∪ {X}, so its value has cycle node Λ(u) and e-set E_s(X).
  - Any option of y whose Ξ-target is in (Y \ A_s) ∪ Z ∪ {u} has a play ending at Z or u with only e's less relevant than e_S. A play
    from Y \ A_s cannot reach X: it passes no e inside Y, so reaching X would put it in A_s. Its e-set is therefore lex below E_s(X),
    because top(E_s(X)) is more relevant than all of those e's. So such an option is strictly worse.
  - Hence σ_(s+1)(y) has its Ξ-target in A_s ∪ {X}. Following the plays at s + 1 from y, every mover met is in A_s and moves into
    A_s ∪ {X}. Y is acyclic and every gate there is dead, so the play reaches X before any e. So y ∈ A_(s+1).
  - With w ∈ A_t this gives w ∈ A_s for all s ≥ t in I. ∎
- Remarks:
  - Nothing is assumed about the gates of B's other options; only their β-faces enter the proof. That covers UPE = 1.
  - Ties between equal X-routes (decided by β's) are allowed. They keep the route inside A_s ∪ {X}.

**Corollary LADDER-2 (PROVED, lane, from LOCK-UP).** In every genome of the ladder83 class (any h, lane lengths L, F-lengths M, FL ∈
{none, exitup, chainup}, UPE ∈ {0, 1}), let I be a maximal interval with every cycle node constant and Λ(u) = Λ(B_(l+1)) on I.
Then each bit B_l adopts SET_l at most twice in I and leaves it at most once.
Proof.
- Take X = B_(l+1) (T for l = h). Y = the lane movers of level l (a, b, d), plus F_l and its bonus c_l (or w_l for FL = none).
  Z = {X_l} for chainup. In each case Y is X-closed and B_l's other options (UP, lane_j) have their Ξ-targets in Y ∪ {X}.
- Every e on X's play has level ≥ l + 1: SET, X-type and UP gates of bits ≥ l + 1 only. So it is more relevant than e_SET_l
  ([E-LEV]). Hence E(X) ≠ ∅ implies the top-element hypothesis.
- While E(X) = ∅, every option of B_l other than SET_l has an e-set of e's less relevant than e_SET_l (Y, Z, u). So once SET_l is
  adopted, it is strictly best until E(X) ≠ ∅: at most one adoption, no reset.
- Once E(X) ≠ ∅ (it stays nonempty in I, by E-MON):
  - If B_l is on SET_l with w ∈ A, LOCK-UP locks it. (i) of the proof gives Odd's e at g_S, since Λ is constant on I.
  - Otherwise SET_l's continuation ends at Z or u with low e's. Some option reaching X is then strictly better, so B_l leaves SET_l
    (at most once), to an option reaching X. That is the only kind of option with an e above e_SET_l.
  - A later re-adoption needs SET_l ▷ the current option, whose e-set contains top(E(X)). So at the deciding state SET_l's
    continuation reaches X e-free: w ∈ A. By (iii), w ∈ A at the adoption state too, and LOCK-UP locks it.
- So: at most two adoptions, at most one reset. ∎
- Consequence: under LADDER-R, each bit moves at most 3 times per Λ-interval. Λ changes are C-steps; R118 (e) gives C ≤ n(2M + 2).
  So the counter cannot double, at any h: DEAD as an exponential counter. The SET-gate flips (R) are not bounded by the corollary;
  R is DATA in §3.

## 3. DATA (meas83.py, census81.py, anal82.py, real81.py, xchk81.py, lock83.py; outputs in experiments/si/box83/out/)
Unit: one run per frozen instance (Howard on IDEAL-CYC from the stored start). Set: the 6 instances of §1. Scope: box81/ref idealcyc
runner; xchk81 is the independent re-implementation. Counters:
- RF(l) = R-steps with a σ̄ change at a level-l gate (anal82's definition, reproduced).
- hubH = max over Λ(H)-intervals of the number of distinct e-sets of H.
- D^tot_E(v) := 1 + #steps with E_t(v) ≠ E_(t−1)(v), summed over all n vertices of Γ(G) (SumD).
- bits = B_l's play passes its own SET e.
- premature reset = a set bit clears while no higher bit changed at that step or the step before.

| instance | N | n | T | R | C | RF (levels 0..h) | bits (B_h..B_1) | hubH | SumD | U | max asc | N5′-xi on Γ3 (iters / fallbacks / T3) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LR2_none | 21 | 126 | 6 | 2 | 0 | 0 1 1 | 00 → 01 → 11 | 3 | 155 | 10 | 1 | 9 / 1 / 6 |
| LR2_exitup | 25 | 154 | 8 | 4 | 0 | 0 3 1 | 00 → 01 → 11 → 10 → 11 | 4 | 194 | 12 | 1 | 11 / 1 / 8 |
| LR2_chainup | 27 | 162 | 9 | 4 | 0 | 0 3 1 | 00 → 01 → 11 → 10 → 11 | 4 | 200 | 14 | 1 | 12 / 1 / 9 |
| LR3_exitup | 45 | 285 | 11 | 7 | 0 | 0 3 3 1 | 000 → 001 → 011 → 010 → 011 → 111 → 101 → 111 | 6 | 433 | 22 | 2 | 14 / 1 / 11 |
| LR3_chainup | 48 | 297 | 12 | 7 | 0 | 0 3 3 1 | 000 → 001 → 011 → 010 → 011 → 111 → 101 → 111 | 6 | 437 | 25 | 2 | 15 / 1 / 12 |
| LR6_exitup | 141 | 930 | 20 | 7 | 0 | 0 3 3 3 3 3 1 | 000001 → 011111 → 010000 → 011111 → 111111 → 101111 → 111111 | 6 | 2,203 | 70 | 5 | 23 / 1 / 20 |
- Premature resets: 0 in every run.
- N5′-xi mover phase = Howard (moverphase_eq_howard 1, full_eq_howard 1) in all 6. N5 (spec) from S3: 4 iterations.
- xchk81: game, states, values and labels SAME in all 6.
- census81 checks: UP-B OK, HUB-ASC-G fail 0, OVT-DV fail 0, R-SPLIT OK.
- The h = 2 §5.3 criterion: hubH ≥ 4 holds and there is no premature reset, but RF(1) = 3 < 2·RF(2) + 2 = 4. It fails.
- Lane lengths do not matter. h = 2 with L ∈ {1,4; 2,6; 4,8} and M ∈ {2,2; 3,3} gives RF [0, 3, 1] every time. h = 3 with
  L ∈ {1,3,6; 2,5,10; 1,6,12}, M ∈ {2; 4} gives RF [0, 3, 3, 1] and R 6-7 (scratch runs; the commands are ladder83.py + meas83.py).
- Lemma check (lock83.py):
  - Unit: (bit, state) with HYP (σ = SET, continuation reaches X e-free, E(X) ≠ ∅); claim = HYP at every later state of the Λ-interval.
  - Set: the 6 frozen instances plus a 48-genome sweep (sweep83.sh, seed 83: h 2-5 × FL 3 modes × UPE 0/1 × 2 random (L, M);
    T ≤ 15). Scope: idealcyc.
  - LOCK-UP violations 0. HYP holds in ≥ 1 state of every run. Max adoptions per bit per Λ-interval 2, max resets 1 (LADDER-2 tight).
    Files out/lock83_inst.out, out/sweep83.out.

## 4. What this says about the design route (READING)
- §5.2's «a carry at level l + 1 changes the Ξ-target that the level-l bits' β-faces lead to» cannot happen while all of B_l's routes
  lead into the same mover B_(l+1). The carry is then seen identically by SET_l's continuation and by every alternative. Once the
  continuation has caught up, SET_l carries an extra e on top.
- What remains, by LOCK-UP's hypotheses:
  - (c) B_l's alternatives and SET_l's continuation lead to different movers X ≠ X′ whose e-sets overtake each other at every carry.
    This is R218 §4's hub pair, and R221 RUNG-ALT's re-adoption needs exactly that: an alternative gate with about 2^(h−l) values.
  - (a) Λ changes, which are polynomially many.
- So the next design question is a pair of hubs per level in carry order, not a ladder. I have no construction. This is OPEN, not a
  claim.
- What would refute LOCK-UP's reach: a LADDER-class genome (all of a bit's routes into one X) whose bit adopts SET 3 times inside one
  Λ-interval. L-RED may attack with the frozen instances and sweep83.sh.

## 5. Sources opened (this box)
- claude/l-red docs/red/R217-ovt.md l. 270-360 (§11 LEAK-ARCH, §12 HIDE-BUSY, CHAIN-SHIELD, RS3); experiments/red/r217/rs2.py, gdsl.py.
- claude/l-red docs/red/R221-ladder.md §1-§9 (NO-REFLECT, ASC-LOG, RUNG-ALT, RHO-SET, RHO-E); R221-quiet.md §0; R219-xi.md §0.
- claude/l-new docs/new/N5-ASC-box193.md §3 (CS(M, A), ASC-EXP); docs/new/P-N5-ASC.md §3 Lemma E-MON (l. 66-78) @ 95dc76d7.
- RESULTS R104 (trunk docs/RESULTS.md l. 9864: genome format, W-target one level down), R105 (l. 10155).
