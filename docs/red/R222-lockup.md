# R222 item 2: adversary vs L-SI box 83 (Lemma LOCK-UP, Corollary LADDER-2) (L-RED successor 57)
Lead target 01:54Z 2026-11-08 (GO 01:56Z). Target: claude/l-si 2a44b7d6, docs/si/box83-ladder.md §2 (Lemma LOCK-UP, Corollary LADDER-2)
and §0 / §4 (the DEAD verdict on LADDER-R and the list of ways out). Referee files not read.
Labels: SURVIVES / BROKEN (frozen instance + sha1) / GAP / DATA (unit, set, scope, counter) / PROVED (lane, unrefereed) / READING.
Nothing here is a TARGET.md claim. G-N5-TIME stays OPEN. N5′-xi stays a CANDIDATE (D1).
Tools: experiments/red/r222/ (own.py = R217's independent IDEAL-CYC run, copied from r221; lock222.py, sweep222.py, priv222.py).
Independence: every run and every counter is L-RED code. L-SI code is used only as a GENERATOR: sweep222.py imports
ladder83.build from a read-only worktree of claude/l-si 2a44b7d6 ($WTSI83), so the swept genomes are exactly the box 83 class.
lock83.py, meas83.py and L-SI's runners are not run and not imported.

## 0. Verdicts
| statement (box 83) | verdict | evidence |
| --- | --- | --- |
| Lemma LOCK-UP (§2) | SURVIVES | proof audited step by step (§1); 0 violations in 3,006 runs, including starts and β ranks the proof does not use (§2) |
| Corollary LADDER-2 (§2) | SURVIVES | max 2 SET adoptions / 1 reset per bit per Λ-interval in all 3,006 runs (§2) |
| «each bit moves at most 3 times per Λ-interval» (§2 Consequence) | SLIP in wording, harmless | true for the bit's VALUE (SET status). False for σ(B_l): B_6 of LR6_exitup changes option 18 times (§2) |
| LADDER-R is DEAD as a counter (§0) | SURVIVES | follows from LADDER-2 plus R118 (e) |
| «(c) the hub pair is the only open way out» (§0, §4 READING) | SHARPENED | Lemma PRIV-FLIP (§3, PROVED lane): the hub pair is also polynomial under [E-LEV] with bounded U(G), UNLESS a play from the bit's own options returns to the bit |
| L-SI 44 CONJECTURE (box84 §4): PRIV-FLIP's bound without PRIV | PROVED (lane) | Lemma FLIP (§4): same bound, no PRIV, no β-parity; DATA 0 violations incl. L-SI's CY gadgets and adversarial climbs |

No hypothesis is used without being stated. I checked these candidates; each one is either stated or not needed:
- E-MON's premise: P-N5-ASC §3 states it for ANY vertex with a constant cycle node. LOCK-UP assumes constant cycle nodes on I.
- «e above every β»: [DEF], also in own.py (e-priority = eb + 2i with eb > every β).
- K0 / K3 on both plays or on neither: E-MON's proof.
- Howard picks the BEST option: not needed. Every step of the proof works for any rule that moves a mover only to a strictly better
  option.
- [E-LEV]: stated in §1's format line and used only in the Corollary.
- The start strategy and the β ranks: not used. Tested in §2 anyway.

## 1. Proof audit (Lemma LOCK-UP, l-si 2a44b7d6 §2)
- (P) persistence. E_s(X) ≥ E_t(X) needs Λ(X) constant on [t, s]. That is a hypothesis («every vertex keeps its cycle node on I»).
  E-MON (P-N5-ASC §3) needs nothing else. OK.
- (i) Odd takes e at g_S. Taking β would make B's cycle B g_S β_S, with cycle node β_S. But Λ_s(B) = Λ_t(B) = Λ(u) ∈ {K1, K2}, and
  β_S is not K1 or K2. OK.
- (ii) S is strictly best.
  - e_S is private to S: its only in-edge is from g_S, whose only in-edge is from B, and none of the plays involved passes B.
  - Odd minimises at g_o, so only β-faces matter for the upper bound.
  - Both cases (X: z = e_S; Z / u: z on the S side) are decided by e-vertices. Every vertex more relevant than an e is c_W, K0 or K3,
    and those agree. OK.
- (iii) A_s ⊆ A_(s+1).
  - The argument does not use σ(B) = S. It needs only top(E_s(X)) above e_S and Y's structure: dead gates and acyclicity.
  - So A is monotone on I as soon as top(E(X)) lies above e_S. The Corollary's «leave once» step uses this, implicitly and correctly:
    once B_l leaves SET, it sits on an option reaching X, and that option keeps reaching X.
- Corollary.
  - X = B_(l+1). Its play passes only gates of level ≥ l + 1 (checked against ladder83.build: UP / lane gates of B_(l+1) are dead,
    and F_(l+1) and the a, b, d lanes of level l + 1 have dead gates).
  - X_l's e_x uses e-key (8, l), below SET_l's (9, l), so Z = {X_l} passes only e's below e_SET_l.
  - With UPE = 1, UP_l's e-face reaches X with e_UP added. Odd takes β there, as the Remark says.
  - Count: one adoption while E(X) = ∅, at most one leave, then a re-adoption that LOCK-UP locks. OK.

## 2. DATA (lock222.py, sweep222.py; outputs experiments/red/r222/out/)
Counters, per bit B_l and per Λ-interval (a maximal run of states on which every cycle node is constant), from own.py's run:
- adopt = #(σ_(t−1)(B_l) ≠ SET, σ_t(B_l) = SET); reset = the reverse; moves = #(σ_(t−1)(B_l) ≠ σ_t(B_l)).
- LOCK-UP check, in my own reading:
  - HYP(t): σ_t(B_l) = SET, Odd takes e at g_SET, SET's W-target reaches X e-free, and top(E_t(X)) is above e_SET.
  - violation: HYP(t) holds, and some later state s of the same interval has σ_s(B_l) ≠ SET or W-target not reaching X e-free.
- Frozen instances (experiments/red/r222/inst/, copies of claude/l-si 2a44b7d6:experiments/si/box83/inst/; sha1 via `git show
  2a44b7d6:<path> | sha1sum`, all six equal to L-SI's table, list in inst/SHA1SUMS). out/lock_inst.txt:

| instance | T (own.py) | C | HYP states | violations | max adopt | max reset | max moves |
| --- | --- | --- | --- | --- | --- | --- | --- |
| LR2_none | 6 | 0 | 1 | 0 | 1 | 0 | 6 |
| LR2_exitup | 8 | 0 | 1 | 0 | 2 | 1 | 6 |
| LR2_chainup | 9 | 0 | 1 | 0 | 2 | 1 | 6 |
| LR3_exitup | 11 | 0 | 7 | 0 | 2 | 1 | 9 |
| LR3_chainup | 12 | 0 | 7 | 0 | 2 | 1 | 9 |
| LR6_exitup | 20 | 0 | 61 | 0 | 2 | 1 | 18 |

T and C equal L-SI's table in all six (independent run).
- Sweep. Unit: one own.py run.
  - Set: 3,000 ladder83 genomes (sweep222.py, seeds 1-5 × 600). h 2-5, lanes L_l 1-6, F-lengths M_l 1-4, FL ∈ {none, exitup, chainup},
    UPE ∈ {0, 1}, N ≤ 99.
  - Modes:
    - stored: ladder83's start.
    - rstart: a uniformly random start strategy.
    - rbeta: a random permutation of the β ranks (parities bp kept), plus a random start.
    - rev: EORD = rev, the level-reversed e-order. This violates [E-LEV], so it is a boundary probe outside the Corollary.
  - Scope: IDEAL-CYC, own.py.
  - Result: violations 0. Max adopt 2 and max reset 1 in every mode. Seeds 1-4 (2,400 runs): stored 426, rstart 834, rbeta 774, rev
    366. HYP held in ≥ 1 state in 2,034 of them.
  - rev also stays ≤ 1 adoption (READING of why: under rev, top(E(X)) never lies above e_SET_l, so SET_l is never left).
- The «moves» counter (seed 5, 600 runs, out/sweep_5.txt): max moves per bit per Λ-interval reaches 8 (stored).
  - On LR6_exitup it reaches 18: B_6 walks UP, lane15, lane0, lane1, …, lane15, SET, one delay-lane option per iteration.
  - So §2's «each bit moves at most 3 times per Λ-interval» holds for the bit's value (σ(B_l) = SET or not), and not for σ(B_l).
  - LADDER-R's DEAD verdict concerns bit values, so it is unaffected. Any iteration bound built on «3 moves per bit» must count the
    lane walks separately: they are linear in the lane lengths here.

## 3. Lemma PRIV-FLIP (PROVED, lane, unrefereed; new): a polynomial bound on SET flips beyond the LADDER class
Setting:
- Runs of IDEAL-CYC(G) for any genome G: Howard at the movers (best option, ties keep the current one), Odd's optimal counterstrategy,
  [VJ] values.
- B is a mover, and S = (w, Ξ-target B, even β_S) is a SET-type option of B. w is the successor of e_S.
- I is an interval of states on which every cycle node is constant, with Λ(B) = λ ∈ {K1, K2}.
- D_E,I(v) is the number of distinct e-sets of v on I, as in P-N5-ASC §2.

Hypothesis PRIV: at every state of I, neither the play from w nor the play from any gate g_o (o ≠ S) of B passes B.

Claim: the number of consecutive state pairs in I at which [σ(B) = S] changes is at most 1 + (D_E,I(w) − 1) + Σ_(o ≠ S) (D_E,I(g_o) − 1).

Proof.
- Facts.
  - By PRIV, e_S lies on no play from w or from any g_o. Its only in-edge is from g_S, whose only in-edge is from B.
  - Every vertex more relevant than an e-vertex is an e-vertex, c_W, K0 or K3, and two plays with the same cycle node agree on K0
    and K3 ([DEF], E-MON's proof). So two plays with cycle node λ and different e-sets are ordered by their e-sets in lex order.
  - λ ∈ {K1, K2} has priority 5 or 3. So β_S (priority ≥ 6) is in Π, and g_S (1) and B (0) are not.
  - Let P_t := [Λ_t(w) = λ and {e_S} ∪ E_t(w) >lex E_t(g_o) for every o ≠ S with Λ_t(g_o) = λ].
- (a) If σ_t(B) = S, then Odd takes e at g_S.
  - Otherwise B's cycle would be B g_S β_S, and Λ(B) = β_S ≠ λ.
  - So Ω_t(g_S) is the e-face value: cycle node λ (so Λ_t(w) = λ), e-set {e_S} ∪ E_t(w). By PRIV, w's play does not depend on σ(B).
- (b) If σ_t(B) = S and P_t holds, S is the unique best option, so σ_(t+1)(B) = S.
  - By (a), Ω_t(g_S) has cycle node λ and e-set {e_S} ∪ E_t(w).
  - Options with cycle node λ have different e-sets (e_S is private), so they are strictly worse.
  - Options with another cycle node are worse. Otherwise Howard would move B there, and Λ(B) would change at t + 1. Pairs that leave I
    are not counted.
- (c) If σ_t(B) ≠ S and P_t fails, S is not the best option, so σ_(t+1)(B) ≠ S.
  - If Λ_t(w) ≠ λ: taking S would change Λ(B). Same argument as in (b).
  - Otherwise some o″ with cycle node λ has E_t(g_o″) >lex {e_S} ∪ E_t(w). Odd minimises at g_S, so
    Ω_t(g_S) ⊴ Ω_t(e-face) ◁ Ω_t(g_o″).
- (d) So [σ(B) = S] can switch on only at a state where P holds, and switch off only at a state where P fails. Between two consecutive
  changes of P_t, it changes at most once.
- (e) P_t can change only where E(w) or some E(g_o) changes. The sets of options with cycle node λ are constant on I.
  - By E-MON (each of these vertices has a constant cycle node on I), each e-set moves only upward in lex order. So v's e-set changes
    at most D_E,I(v) − 1 times.
  - Sum (d) and (e). ∎

Remarks:
- P_t is ONE-SIDED in time. When P_t holds and B is on some o, Odd takes β at g_S, so Ω_t(g_S) = o's value plus β_S, which is strictly
  above o. B may still move to a better o″ first and adopt S one step later. (d) covers this lag.
- Nothing is assumed about B's other gates, about levels, or about which higher movers the plays reach (X, X′, …).

**Corollary PRIV-POLY (PROVED, lane; from PRIV-FLIP and P-N5-ASC §5-§6).**
- If every seq_t(v) for v ∈ {w} ∪ {g_o} has at most B ascents on I, then the number of SET flips of B on I is at most
  1 + deg(B)·(F′_B(M) − 1) (Corollary HUB-ASC-G).
- Under [E-LEV], take B = U(G) (Corollary UP-B). Over the whole run, with ≤ 2M + 3 cycle-node values per vertex and C ≤ n(2M + 2)
  (R118 (e)), every SET-type bit whose plays satisfy PRIV flips at most (C + 1)(1 + deg(B)·F′_U(G)(M)) times. That is polynomial when
  U(G) = O(1).

Consequence for L-SI's next design (READING; it answers box 83 §4 before the candidate exists):
- The hub pair routes B_l's alternatives to X and SET_l's continuation to X′ ≠ X. Both are higher movers. As long as no play from them
  comes back through B_l, PRIV holds, and PRIV-POLY bounds B_l's flips polynomially for bounded U(G).
- So, under [E-LEV], an exponential SET counter on the bits needs one of:
  - (a) Λ changes. These are polynomially many (R118 (e)).
  - (b) unbounded U(G): the open region of P-N5-ASC.
  - (c′) a play from the bit's own options that returns to the bit (PRIV fails): a Ξ-cycle through B_l longer than its SET self-loop.
- (c′) is the CYC-type gate of R222 item 1, so items 1 and 2 meet there.

DATA for PRIV-FLIP (priv222.py; unit: (B, SET-type S, Λ-interval with Λ(B) ∈ {K1, K2}); counter: flips vs the bound):
- Set A: 8,000 random Ξ-cyclic genomes (R221 brute221.rgen; seeds 2-5 × 2,000; d 1-4, width 1-4, degree 2-3). 3,628 units, 2,617
  with PRIV. Violations 0, max flips under PRIV 2.
- Set B: L-RED's 58 readable frozen instances in experiments/red/r21*/inst/ and r22*/inst/. Violations 0, max flips under PRIV 5 (the
  t1_* hubs of R218); out/priv_inst.txt. 16 files there are not genomes and were skipped (KeyError 'N').
- The bound is far from tight on this data. The data only shows that the inequality held. The proof is §3.

## 4. Lemma FLIP: PRIV-FLIP's bound WITHOUT PRIV (Lead 04:00Z: L-SI 44's CONJECTURE, claude/l-si 83d49640 docs/si/box84-hubpair.md §4)
Target: L-SI's CONJECTURE «[PRIV-FLIP's] bound holds for every SET-type option when Λ(B) ∈ {K1, K2}». L-SI's evidence was 4 CYC gadgets
and 4 climbs; L-SI called it weak. L-SI's Lemma LIVE-BREAK (same note) is the obstacle a counterexample would have to get around.

Verdict: PROVED (lane, unrefereed). There is no counterexample to freeze. PRIV was never needed, and neither is β_S's parity. The
proof below replaces §3's.

**Lemma FLIP (PROVED, lane; premises: F1 / E-MON, Odd's optimal response, Howard best switch with ties kept, [DEF]).**
Setting:
- Runs of IDEAL-CYC(G) for any genome G. B is a mover. S is a SET-type option of B: Ξ-target B itself, any β-parity. Its gate is g_S, its
  e-vertex e_S, its β-vertex b_S (single edge b_S → B), and w is the successor of e_S.
- I is an interval of states on which Λ(B) = λ ∈ {K1, K2}, and Λ(w) and Λ(g_o) are constant for every option o ≠ S.
- No condition on where any play goes: plays from w or from the g_o may pass B.

Claim: #{t : t, t + 1 ∈ I, [σ_t(B) = S] ≠ [σ_(t+1)(B) = S]} ≤ 1 + (D_E,I(w) − 1) + Σ_(o ≠ S) (D_E,I(g_o) − 1).

Define P_t := [Λ(w) = λ, and for every o ≠ S: reward(Λ(g_o)) < reward(λ), or (Λ(g_o) = λ and {e_S} ∪ E_t(w) >lex E_t(g_o))].
On I the cycle nodes in P are constant, so P_t can change only where E(w) or some E(g_o) changes.

Proof.
- (1) If σ_t(B) = S, then Odd takes e at g_S, w's play does not pass B, Λ(w) = λ, and Ω_t(g_S) has cycle node λ and e-set
  {e_S} ∪ E_t(w).
  - Odd taking β would make B's play the cycle B g_S b_S, with node b_S (priority ≥ 6). But b_S ≠ λ.
  - So B's play is B g_S e_S followed by w's play.
  - If w's play passed B, B's play would be a cycle through e_S. Its node would be at least as relevant as e_S, so it could not be K1
    or K2.
  - Hence Λ(w) = Λ(B) = λ, and e_S, which is more relevant than λ, lies in Π. g_S (priority 1) does not.
- (2) If σ_t(B) ≠ S, then no play passes g_S: its only in-edge is from B. So e_S ∉ E_t(v) for every vertex v ≠ e_S.
- (3) Comparisons. Take two values with cycle node λ and different e-sets. The most relevant vertex of their Π-difference is an
  e-vertex: every vertex more relevant than an e is c_W, K0 or K3; c_W is never in a Π; K0 and K3 lie on both plays or on neither
  (E-MON's proof, P-N5-ASC §3). So such values are ordered by their e-sets in lex order.
- (4) on → off forces ¬P_t.
  - Let σ_t(B) = S and P_t hold. By (1), Ω_t(g_S) has node λ and e-set {e_S} ∪ E_t(w).
  - Every o ≠ S has either a node of lower reward (strictly worse), or node λ and a lex-smaller e-set (strictly worse, by (3)).
  - So S is the unique best option, and Howard keeps it: σ_(t+1)(B) = S.
- (5) off → on forces P_t. Let σ_t(B) ≠ S and σ_(t+1)(B) = S, with t, t + 1 ∈ I, and suppose ¬P_t.
  - (i) Λ(w) ≠ λ. At t + 1, (1) gives Λ_(t+1)(w) = λ, against the constancy of Λ(w) on I.
  - (ii) Some o has reward(Λ(g_o)) > reward(λ). e_S's play is e_S followed by w's play; it cannot return to e_S, by (2). So the e-face
    of g_S has node Λ(w) = λ. Odd minimises at g_S, so Ω_t(g_S) ⊴ (e-face) ◁ Ω_t(g_o), and Howard does not choose S.
  - (iii) Some o has Λ(g_o) = λ and E_t(g_o) ≥lex {e_S} ∪ E_t(w). By (2), e_S ∉ E_t(g_o), so the two sets differ and «>» holds.
    The e-face has node λ and e-set {e_S} ∪ E_t(w): w's play may pass B here, but it never passes e_S, by (2). By (3),
    Ω_t(g_S) ⊴ (e-face) ◁ Ω_t(g_o), and Howard does not choose S.
- (6) By (4) and (5), the status [σ(B) = S] switches on only at a state where P holds, and off only at a state where P fails. So
  between two consecutive changes of P_t it changes at most once.
  - P_t changes only where E(w) or some E(g_o) changes.
  - By E-MON (each of these vertices has a constant cycle node on I), each of those e-sets moves only upward in lex order, so it
    changes at most D_E,I(v) − 1 times. ∎

Where PRIV was hiding in §3, and why it is not needed:
- §3 used PRIV to make e_S private, and to make the values of w and g_o independent of σ(B).
  - Privacy comes for free. When B is on S, (1) shows w's play cannot return to B. When B is off S, (2) shows nothing passes g_S.
  - Independence is not needed. P_t is defined from the ACTUAL e-sets at t, whatever σ(B) does to them, and E-MON still makes each of
    them monotone.
- When g_o's play does return to B, a flip of B changes E(g_o) as well. That change is charged to D_E,I(g_o), and HUB-ASC-G bounds
  D_E,I(g_o) for every vertex.
- L-SI's LIVE-BREAK is consistent with this. A returning route of B's CURRENT option is broken by Odd, so it enters only as a hidden
  value, which is exactly the role of E_t(g_o) in P_t.

**Corollary FLIP-POLY (PROVED, lane).**
- If every seq_t(v) for v ∈ {w} ∪ {g_o} has at most B ascents, the flips of [σ(B) = S] on such an I number at most
  1 + deg(B)·(F′_B(M) − 1) (HUB-ASC-G).
- By R118 (e), each of the deg(B) + 1 vertices B, w and g_o (o ≠ S) changes its cycle node at most 2M + 2 times, so the run splits
  into at most (deg(B) + 1)(2M + 2) + 1 such intervals, plus one flip per boundary.
- Under [E-LEV], B ≤ U(G) (UP-B). So, on the part of the run where Λ(B) ∈ {K1, K2}, every SET-type option of every mover flips
  polynomially often in N + M when U(G) = O(1).
- No PRIV, no LADDER structure and no [OPT] are needed. B-ONLY / [OPT] are needed only to drop «Λ(B) ∈ {K1, K2}»: by B-ONLY, Λ(B) is
  then a β, K1, K2 or c_X, and (1) needs λ ≠ b_S. That extension is not claimed here.

Consequence (READING):
- Under [E-LEV] with U(G) = O(1), no mover's SET option can be an exponential counter bit within polynomially many Λ-intervals, whatever
  routes return to the bit.
- An exponential SET counter on IDEAL-CYC therefore needs unbounded U(G), the open region of P-N5-ASC. This closes branch (c′) of §3's
  consequence: the returning play no longer helps.
- It says nothing about non-SET options or about P-steps: switches decided by β's when e-sets are equal.

DATA (priv222.py now also checks non-PRIV units: violnp = units with flips > bound, npslack = min(bound − flips); climb222.py):
- L-SI's gadgets, frozen copies in experiments/red/r222/inst/ (sha1 in inst/SHA1SUMS, from `git show 83d49640:<path> | sha1sum`):
  - CY2_lr, CY2_hp, CY3_hp, CY4_hp: violnp 0, npslack 5 / 5 / 7 / 13, max non-PRIV flips 3.
  - climb_s11-s14: violnp 0, npslack 0-1.
- Structured «ret» family (priv222.rgen_ret: every mover has a SET option, the other Ξ-targets point down or sideways so routes climb
  back): 500 genomes, 167 non-PRIV units, violnp 0. These rarely flip.
- Adversarial climbs (climb222.py, seeds 21-24, 3,000 iterations each; score = (−min slack over non-PRIV units, max non-PRIV flips, T);
  out/climb222_2*.txt, best genomes out/climb222_best_*.json): violnp 0 in all four. Best min slack 1 / 1 / 0 / 1: seed 23 attains the bound on
  a non-PRIV unit. Max non-PRIV flips 1. As L-SI found, random cyclic genomes rarely flip, so this DATA is weak; the proof carries the result.

## 5. Not done (named)
- N5′-xi on Γ3 for the box 83 instances, with my own tools or Oink n5v / n5b: NOT RUN.
  - Oink is not built in this container, and the R221 worktrees are gone.
  - L-SI's table reports 1 fallback and T + 3 iterations, consistent with CONJECTURE ENDGAME-3.
  - With the counter DEAD at IDEAL-CYC level, this check cannot change the verdict. It is queued for the hub-pair candidate, where it
    matters.
- No referee has seen PRIV-FLIP.

## 6. Sources opened
- claude/l-si 83d49640 docs/si/box84-hubpair.md §2b, §4 (LIVE-BREAK, the CONJECTURE, CY gadgets).
- claude/l-si 2a44b7d6: docs/si/box83-ladder.md (all), experiments/si/box83/ladder83.py (class definition; e / β keys).
- claude/l-new 95dc76d7: docs/new/P-N5-ASC.md §1-§3 (E-MON, CHAIN-DECOMP, [DEF] priority facts), §5 (HUB-ASC-G), §6 (UP-JUMP, UP-B,
  NOUP).
- claude/l-red: docs/red/R221-quiet.md §10-§11; experiments/red/r221q/brute221.py (rgen); experiments/red/r221/own.py.
