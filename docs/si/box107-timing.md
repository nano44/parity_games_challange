# Box 107 (D18; item 0 of the Lead's 2026-11-13 brief): the TIMING structure of full key enumeration on L-NEW's one-player model 1P(G) — ABANDON, ONE-AHEAD, the odometer order, CAUSE; what the Ξ side owes; exact tiny data (PROVED lane lemmas + DATA; QUIET-KEY-1P stays OPEN; not a bound; not M3, not M4)
L-SI successor 55 (session_01V5yGRXxumMiQqqDcnP9eDr), D1 / D18 / D21. Lead brief 2026-11-13 (item 0, quoted): «the TIMING structure of
full enumeration on L-NEW's 1P(G)»; «(a) Prove or refute ABANDON»; «(b) What must the Ξ side deliver per level under Ξ-acyclicity?»;
«(c) Goal, either one: a lemma «k full levels need at least f(k) movers (or levels, or relay switches)» … or the explicit rule of a
family». Lead 10:51Z («GO»), quoted: «Box 107 (a) as written, each lemma with its hypothesis exact (which need «full», which only
«enumerating», which need the ladder). Add the must-0 counters … as a committed check with its firing control, on all five towers.»
Labels: PROVED (L-SI lane, unrefereed) / DATA (counter, unit, set, scope) / DEAD (with numbers; lane, per L43 not a RESULTS claim) / OPEN.
**SCOPE LINE: nothing here is a TARGET.md claim, M3 or M4, or a gauntlet step. G-N5-TIME stays OPEN. Every statement is about the
model 1P(G) of docs/new/N5-QUIETKEY-box217.md §1 (claude/l-new a143d4060), i.e. about N5 only through L-NEW's REDUCTION there
(lane, conditional). No lower or upper bound on N5 is claimed.**
D1 (owner, verbatim): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the
fleet's own, as wrong until it passes the gauntlet below.»
History: the statement of §2-§4 was sent to the Lead at 10:52Z, after scratch runs of the counters on two towers (H5, RECF4) and
before the committed tools existed; the tools of §7 re-measure everything from scratch. Tools: experiments/si/box107 (run107.sh,
check107.sh; «box 107» in experiments/si/check.sh).

## 0. What stands after this box
- (a) ABANDON is TRUE in the strict «before the step» form, at any shape and degree (§2): a W-target of a full mover never changes
  its key in a step that the mover starts on it. The weaker hypothesis «μ enumerates» gives ENUM-ABANDON and ONE-AHEAD. On a 2-per-level
  ladder these give the Lead's odometer as a forced partial order of events, with the exact simultaneity rule (§3).
- (b) Every move of a second mover S_j below the top capped level is decided by the Ξ side alone (FROZEN, §4), must carry the bit
  «both level-(j + 1) movers have left S_j», and has a Ξ-cause one step earlier (CAUSE). No lower bound on movers follows from these
  (§4 names the exact step that is missing); the question «one shared chain or one relay per level» stays OPEN.
- (c) Neither outcome reached. DATA: no 3-level ladder has a full level-2 mover (SAT, exact horizon, uncertified; §7); two natural
  «self-dual» LEVEL-RANKED classes are DEAD as sources of long runs (level-ranked bi-ladders: exact maxima 2, 3, 6, 8, 11 for
  d = 2..6; pair networks on a W-chain: no k = 3 with up to 6 pairs; §6). «Level-ranked» (β ranks increasing with the W-level) is a
  real restriction: with free ranks the bi-ladder wiring has T_key 7 at d = 4 (the Lead's instance, ctrl/lead_bil4.json, replayed),
  so NO negative statement about a level-ranked class transfers to ladders in general. One structured class is ALIVE: level-ranked
  UPWARD ladders (every Ξ-target on a higher W-level; §6) have k = 2 at d = 4 and k = 3 at d = 6 (models replayed on one217.OneP), and no k = 3 at d = 5 within 12 steps:
  k = d/2 at the two sizes measured. Whether k = 4 exists at d = 8 is the next query; it decides whether this is a family.

## 1. Setting and notation
1P(G) as in box 217 §1 ([Q box 217] «KEY rule (KEY-TAU (i), box 213): s′ is computed level by level from level 0: s′(x) := the
k ∈ A_s(x) with the least key_s′(x, k) := key_s′(wt, s′(wt)) ++ (ε(x, k))»), any number of movers per level, any degree. Run
s_0, s_1, …, s_T; step t is s_t → s_(t+1); x switches at step t if s_(t+1)(x) ≠ s_t(x). μ_t(x) := key_(s_t)(x, s_t(x)); K(x) := the
set of keys of x; K_k(x) := {κ ++ ε(x, k) : κ ∈ K(wt(x, k))} (K_k(x) := {(ε(x, k))} at level 0), so K(x) is the disjoint union of the
K_k(x) (the ε are distinct). sw(x) := the number of switches of x. x is FULL if sw(x) = |K(x)| − 1; x ENUMERATES if μ(x) takes every
value of K(x) during the run. Used from box 217 (lane): A1 MONO-1P ([Q box 217] «μ_(t+1)(x) ≤ μ_t(x) and V_(t+1)(x) ≥ V_t(x) for
every x, t; both strict when x switches at t») and A4 HEREDITY (if μ(x) enumerates then μ(wt(x, k)) enumerates for every option k;
its proof uses only that μ(x) enumerates). Two facts of the rule itself: (R1) s_t(x) ∈ A_t(x); (R2) the argmin is over the keys of
the NEW lower-level state. Ξ-acyclicity is not used in §2-§3.

## 2. ABANDON, ENUM-ABANDON, ONE-AHEAD (any shape, any degree)
**Lemma FULL-ORDER (PROVED lane; hypothesis: x full).** μ(x) runs through all of K(x) in decreasing order; it changes exactly at the
switches of x, each time to the immediate predecessor in K(x). Proof. μ(x) ∈ K(x) is non-increasing and strictly decreases at each of
the |K(x)| − 1 switches (A1), so it takes |K(x)| distinct values: all of K(x), each once, in decreasing order, and it cannot change
at a step without a switch (that would be a |K(x)|-th change). ∎
**Lemma ABANDON (PROVED lane; hypothesis: x full; parallel options allowed).** If a mover w changes its key at step t
(μ_(t+1)(w) ≠ μ_t(w)), then s_t(x) is not an option into w. Proof. Let s_t(x) = k with wt(x, k) = w and μ_t(w) = κ, μ_(t+1)(w) = κ′ <
κ. If x keeps k, μ_(t+1)(x) = κ′ ++ ε(x, k) ≠ μ_t(x) without a switch, against FULL-ORDER. If x switches to k′ ≠ k: by (R1), (R2)
μ_(t+1)(x) = min over A_t(x) ≤ κ′ ++ ε(x, k), with equality excluded (distinct last entries), so μ_(t+1)(x) < κ′ ++ ε(x, k) < κ ++
ε(x, k) = μ_t(x): the key κ′ ++ ε(x, k) ∈ K(x) lies strictly between two consecutive values of μ(x) and is never taken (μ is monotone),
against FULL-ORDER. ∎ So a reader never LEAVES in the step in which its target moves; it may ARRIVE in that step (lag 0: (R2)).
**Lemma ENUM-ABANDON (PROVED lane; hypothesis: x enumerates).** If w changes its key κ → κ′ at step t and s_t(x) = k is into w, then
s_(t+1)(x) = k and κ′ ++ ε(x, k) is the immediate predecessor of κ ++ ε(x, k) in K(x). Proof. As above μ_(t+1)(x) ≤ κ′ ++ ε(x, k) <
μ_t(x); an enumerating monotone μ(x) skips no key, so μ_(t+1)(x) is the predecessor of μ_t(x) and no key of K(x) lies strictly
between them; κ′ ++ ε(x, k) ∈ K(x) lies in [μ_(t+1)(x), μ_t(x)), so it equals μ_(t+1)(x), and the last entry gives s_(t+1)(x) = k. ∎
**Lemma ONE-AHEAD (PROVED lane; hypothesis: x enumerates).** For every time t and option k of x with W-target w: if
Λ := {λ ∈ K_k(x) : λ ≤ μ_t(x)} is non-empty then μ_t(w) ++ ε(x, k) ≥ max Λ. (No W-target is ever more than one of its keys past
the point where x reads.) Proof. λ* := max Λ is taken by μ(x) at some t′, and t′ ≥ t because μ(x) is non-increasing and λ* ≤ μ_t(x);
at t′, s_(t′)(x) = k and μ_(t′)(w) ++ ε(x, k) = λ*; μ(w) is non-increasing, so μ_t(w) ≥ μ_(t′)(w). ∎
**What survives without «enumerates» (the half-rate regime; PROVED lane, but empty of timing).** For any mover x let U(x) ⊆ K(x) be
the set of values μ(x) takes. ONE-AHEAD's proof gives the same inequality with K_k(x) replaced by U(x) ∩ K_k(x) (VISIT-AHEAD): a
target is never past the next key that x will actually read through it. For sw(x) = |K(x)|/2 − 1 (levels 5, 6 of H5: 31 switches)
this constrains nothing by itself, because the hypothesis does not say WHICH half of K(x) is read: a target may change its key
under x (x then skips keys without switching). On a ladder the only landed constraint in that regime is R113's count ([Q R113]
«(MOVES) on 𝓛^R_d, KF_x = F(l − 1) and moves(x) ≤ 1 + F(l − 1) for every mover x of level l ≥ 1»): the pair below flips at least
sw(x) − 1 times. A timing statement for sw ≈ |K|^c, c < 1, is the OPEN remainder (Lead 10:41Z: SW-POLY is the proof-side target).

## 3. Ladders: one bit per level, and the odometer as a forced order
Ladder: two movers a_l, b_l per level, every mover of level l + 1 with exactly two options, option 0 into a_l and option 1 into b_l
(this is 𝓛^R_d of RESULTS R110 in 1P's notation).
**OMEGA (landed, restated).** ω_l(s) := the level-l mover with the smaller key under s. ω_0 is read off the ε-order of the four
level-0 options; for l ≥ 1, ω_l = σ_l(o) (a fixed bit of the ε's) if both level-l movers hold option o, and otherwise the one
that points at ω_(l−1). A mover of level l + 1 switches at step t iff its other option is strictly Ξ-better under s_t and points at
ω_l(s_(t+1)). This is RESULTS R113 (ALIGN) and R120 (MOVE) in the IDEAL model: [Q R113] «(ALIGN) on 𝓛^R_d, for 1 ≤ l ≤ d − 1 and every
state s of a run, both movers 2l and 2l + 1 have KP_s = c_l(s), each of them that moves at step t moves to option c_l(s_t)»;
[Q R120] «(MOVE) a mover x of level l ≥ 1 moves at step t iff its other option is strictly better under s_(t−1) and c_l(s_t) ≠
s_(t−1)(x), and then moves to c_l(s_t)» (c_l = ω_(l−1); their steps are numbered one higher). On Ξ-acyclic R104 genomes the IDEAL run
is 1P's key run with gate-index keys (box 105 §1, lane); with e-index keys (R241) the same proof applies to 1P as it stands,
because it uses only the lexicographic order of keys with distinct last entries. So on a ladder the key side is a Boolean network.
**ODOMETER (PROVED lane; hypothesis: a ladder whose levels 0, …, h − 1 are CAPPED, i.e. both movers full; this is the towers' regime).**
Let M_j := K(a_j) ⊔ K(b_j) in decreasing order (2^(j+2) positions; a level-(j + 1) mover has one key per position). For j ≤ h − 2:
 (1) M_j alternates between its two owners, and the same owner is first in every pair: there is a FIRST mover F_j and a SECOND mover
     S_j, with K(F_j) and K(S_j) interleaved F, S, F, S, … (for j ≥ 1 this says σ-suffixes agree: ε(F_j, o) > ε(S_j, o) for o = 0, 1).
     Proof: a full reader x of level j + 1 switches at every change of μ(x) (FULL-ORDER) and has one option per owner, so
     consecutive positions have different owners. ∎
 (2) Each of the two readers of level j + 1 reads every position of M_j, in order, one position per switch.
 (3) (order) Write E(z, p) for the step at which the level-(j + 1) reader z arrives at position p, and W(p) for the step at which
     the owner of position p arrives at that key. Then W(p) ≤ E(z, p) («≤»: the same step is allowed), E(z, p) < E(z, p + 1), and
     E(z, p + 1) < W(p + 2) for both readers z («<»: a strictly later step; ABANDON applied to the owner of p and p + 2).
 Hence Pass(j, i) = «F_j → i; both readers read it; S_j → i; both readers read it», nested over the levels: the Lead's odometer
 reading («Pass(j, target) = a_j → target; Pass(j+1, a_j); b_j → target; Pass(j+1, b_j)») is correct as a partial order, with the
 simultaneity rule: a reader may move in the step of its writer (whole carry chains in one step), a writer never moves in a step
 that a full reader starts on it. The landed forms of (1)-(3) in the IDEAL model are R120's DOUBLE-EQ and PULSE-NEST: [Q R120]
 «(DOUBLE-EQ) if level j is doubling then no step moves both members of pair j, the pair flips exactly at the steps moving a member,
 each member moves exactly once in every j-window, and if F(j − 1) ≥ 1 the first mover is the same member in every j-window»;
 [Q R120] «(PULSE-NEST) if levels j, …, j + k are doubling then PULSE ≥ k + 1 on every j-window». New here: the statements at any
 shape and degree (§2), the hypothesis «one full reader» instead of «doubling level» (ABANDON needs only x full), ONE-AHEAD, and
 the «arrive but never leave» rule.
**One full top mover only (PROVED lane; hypothesis: x full at level J of a ladder).** Then (1) holds for j = J − 1 with the single
reader x, every W-descendant of x enumerates (A4), ONE-AHEAD and ENUM-ABANDON hold at every W-descendant, and for j < J − 1 each
enumerating reader of level j + 1 reads all of M_j in order (possibly without switching where consecutive positions have one owner).

## 4. (b) What the Ξ side owes (STATEMENT; PROVED lane where marked)
Throughout: a ladder with levels 0..h − 1 capped, F_j / S_j as in §3; «KC» = the key condition of OMEGA, «ΞC» = «the other option
is strictly Ξ-better»; a mover switches at step t iff KC (read on s_(t+1) below it) and ΞC (read on s_t).
**CAUSE (PROVED lane; any 1P(G)).** If x switches at step t ≥ 1, then a strict Ξ-descendant of x switched at step t − 1, or a mover
of lower level on a W-path below one of x's options switches at step t. Proof. Suppose no lower-level mover on those W-paths
switches at step t and no Ξ-descendant switched at t − 1. Then the option values of x at s_t equal those at s_(t−1) (they are
functions of the Ξ-descendants' options) and the keys of x's options at step t equal those at step t − 1. If x did not switch at
t − 1 it faced the same A and the same keys and stays again. If x switched at t − 1 (to k), then k was strictly better than the old
option at s_(t−1), hence also at s_t, so the old option is not in A_t(x); any other k′ ∈ A_t(x) is strictly better than k at s_t,
hence at s_(t−1), hence was in A_(t−1)(x) with a larger key than k at step t − 1, and the keys are unchanged: x stays. ∎
**FROZEN (PROVED lane; 1 ≤ j ≤ h − 2).** Let S_j move to position i of M_(j−1) at step t, and let t_F < t be the step at which F_j
moved to position i. Then no level-(j − 1) mover changes its key at any step u with t_F < u ≤ t, KC(S_j) holds at every step
u ∈ [t_F, t], ΞC(S_j) is false on s_u for t_F ≤ u < t and true on s_t. Proof. The owner w of position i arrived at a step ≤ t_F and
cannot move again before both readers F_j, S_j are past i (§3 (3)); the other level-(j − 1) mover is the owner of position i − 1,
which S_j points at until step t (ABANDON). So ω_(j−1) is constant = w on s_(t_F+1), …, s_(t+1), which is KC(S_j); S_j does not
switch at the steps u < t, so ΞC fails there. ∎ For j = 0 the key condition is the fixed ε-order and the same conclusion holds.
**Corollary Ξ-LAST (PROVED lane).** Every move of S_j, j ≤ h − 2 (2^(j+1) − 1 moves per run), happens at a step fixed by the Ξ
side alone: by CAUSE a strict Ξ-descendant of S_j, on the Ξ-path of the option S_j moves to, switched at step t − 1. And by ABANDON
at step t neither level-(j + 1) mover points at S_j: with READ_j(s) := «both movers of level j + 1 point at F_j», ΞC(S_j) ⟹ READ_j
on every state of a frozen interval. Since ΞC(S_j) is a function of the options of the strict Ξ-descendants D(S_j) of S_j:
**SEPARATION (PROVED lane).** If two states s_u, s_(u′) of frozen intervals of S_j agree on D(S_j) and on S_j's own option, and S_j
switches at u, then READ_j(s_(u′)). So the run projected to D(S_j) separates the move states of S_j from every frozen state in which
a level-(j + 1) mover still points at S_j: D(S_j) contains the level-(j + 1) movers themselves or movers whose options record them.
**The signals, as a list.** (i) to S_j, j ≤ h − 2: one Ξ-change per position, at the step before the move, true only after READ_j;
by PULSE-NEST at least h − j steps after F_j's move. (ii) to F_j: KC(F_j) turns true when the owner of the next position arrives;
F_j needs ΞC at or after that step, and (ABANDON) not while a level-(j + 1) mover still points at F_j; between two consecutive moves
its Ξ-order must flip once, at any step of the window (DATA §7: on the towers F_j is key-last on most moves, i.e. its ΞC is already
true when the key arrives). (iii) FLIP-SUPPLY (PROVED lane, counting only): between two consecutive switches of any mover x some
strict Ξ-descendant switches (degree 2: the Ξ-order of the two options must flip), so Σ_(y ∈ D(x)) sw(y) ≥ sw(x) − 1 and, by
induction along a topological order of D(x), sw(x) ≤ 2^|D(x)|: a full level-(h − 1) mover has at least h strict Ξ-descendants.
**Where a lower bound stops (OPEN, the exact step).** SEPARATION says WHAT D(S_j) must record, CAUSE says WHEN; neither says that
the record for S_j cannot be shared with the record for S_(j+1). Lead reading 10:51Z (quoted): «is the signal to S_j computable from
the signal to S_(j+1) plus O(1) movers … or does each level need its own relay whose supply is not shared». What can be said:
 - Logically it IS shareable: «all of Pass(j + 1, ·) is complete» = «Pass(j + 2, ·) is complete» ∧ «S_(j+1) is not behind F_(j+1)»; a
   token that each S_m either takes (if it is behind, KC) or passes down. In the relaxation where ΞC(x) may be ANY Boolean function
   of the options of D(x) (FUNCTIONAL model), this needs no relay at all with the W-level order as Ξ-order.
 - What the relaxation drops is MONO-1P on the Ξ side: V(y) never decreases, so «y's option» cannot be read as a level, only as a
   leapfrog of two rising values. Each S_j alternates its two options, so the SAME event (pass complete) must raise the value of
   option 0's Ξ-path above option 1's in one window and the reverse in the next. Every instance known (five towers; §7) pays for
   this with movers that switch at S_j's own rate (HIT7: about six movers of rate ≈ 2^(j+1) per level j ≤ 4, DATA).
 - A proof of a super-linear f(k) would have to show that these rate-2^(j+1) movers cannot serve two levels; a family would have to
   give their wiring as a rule. Neither is done here.

## 5. The Boolean-network form (for encoders; exact)
Ladder with d levels, movers (l, i), i ∈ {a, b}; state c(l, i) ∈ {0, 1} (option o points W at (l − 1, o), o = 0 for a).
Parameters: an order of the four level-0 options by ε; bits σ_l(o) ∈ {a, b} for l ≥ 1, o ∈ {0, 1} (the mover with the smaller ε on
option o); for each option q = (l, i, o) a Ξ-target xt(q) (a mover or the exit; Ξ-graph acyclic), a rank ρ(q) (a bijection onto
{0..4d − 1}) and a sign; the start c_0. Derived, for a state c: ω_0(c) := the level-0 mover whose current option has the smaller ε;
ω_l(c) := σ_l(o) if c(l, a) = c(l, b) = o, else the i with c(l, i) = ω_(l−1)(c) (as an option index). P_c(l, i, o) := {(l, i, o)} ∪ the
options on the Ξ-chain from xt(l, i, o) under c. BET_c(l, i) := the option of largest rank in P_c(l, i, 0) Δ P_c(l, i, 1) lies in
P_c(l, i, 1) and has sign +, or lies in P_c(l, i, 0) and has sign − (hops never decide: the two sets differ). Step c → c′, level by
level from 0: mover (l, i) with o := c(l, i) switches iff [BET_c(l, i) ≠ o, i.e. the other option is better] and [l = 0: ε(l, i, 1 − o)
< ε(l, i, o); l ≥ 1: ω_(l−1)(c′) = 1 − o]. experiments/si/box107/syn107.py is this network as a CNF with all parameters free
(value side: sets of options and a free total order of ranks); every model is decoded to L-NEW's genome JSON and must replay on
their one217.OneP (replay107.py: equal states) before it is cited.

## 6. Dead ends of this box (lane; DATA with numbers, not asymptotic claims; L43)
- **LEVEL-RANKED BI-LADDER.** B_d: the ladder in which every mover of level l has its two Ξ-targets on the two movers of level l + 1
  (top level to the exit) AND the β ranks increase with the level, so that both sides are one bit per level (the exact self-dual form of the rule up
  to the one-step delay). Longest run, exact by SAT over all parameters and starts (uncertified): 2, 3, 6, 8, 11 for d = 2, …, 6
  (bil107.py; §7). Obstruction: with both Ξ-targets one level up, the Ξ-order of a mover is the bit «which of the two movers above
  is higher», which is decided by the first level at which their Ξ-paths merge, so no mover reads further than its merge level.
  CORRECTION (Lead 11:47Z, with an instance): the same WIRING with FREE β ranks has T_key 7 at d = 4 (ctrl/lead_bil4.json, replayed
  on one217.OneP: switches 1, 1, 1, 2, 1, 2, 1, 1; the Lead reports 15 at d = 6, not re-measured here). So «6» and «11» are maxima
  of the level-ranked class only; the dead end is «level-ranked bi-ladders», not «bi-ladders».
- **PAIR NETWORKS on a W-chain.** Pairs with a W-parent pair and a Ξ-parent pair (any acyclic choice), both options of a mover into
  the two members of ONE Ξ-parent pair: no k = 3 (no full level-2 mover) with P = 3, 4, 5, 6 pairs on a W-chain (SAT, horizons 22,
  30, 20, 20; uncertified); the general ladder has k = 3 at d = 5 (Lead scratch, N = 10). So the two options of a mover must be able
  to read movers of DIFFERENT pairs / levels. With a free W-forest the longest run is 1, 2, 4, 6 for P = 1, …, 4 and ≥ 10 for P = 5.

- **LEVEL-RANKED UPWARD LADDERS (not dead; DATA).** The ladders in which every Ξ-target lies on a strictly higher W-level (or is the exit) and
  the β ranks increase with the W-level: «low reads high by value, high reads low by key», the orientation §4 arrives at. The
  Ξ-graph is acyclic by construction and an option comparison is decided at the highest level where the two Ξ-paths differ
  (up107.py; a much smaller CNF than syn107.py). Longest run, exact (uncertified): 3, 5, 7 for d = 2, 3, 4. Full movers: k = 2 at
  d = 4 (out/up_k2_d4.json) and k = 3 at d = 6 (out/up_k3_d6.json: N = 12, T_key = 8, switches 1, 1, 3, 3, 7, 1, 3, 3, 3, 2, 1, 1; both
  replayed on one217.OneP with equal states); no k = 3 at d = 5 within T = 12. Counting gives k ≤ (d + 1)/2 in this class for one full
  mover (a level-(k − 1) mover has at most 2^(d − k + 1) Ξ-paths, A2), so the two measured sizes sit within one level of the counting
  bound. This is two data points, not a family: no rule is read off yet. The negative lines of this class («d 5 T 12 full:4
  UNSAT», the longest runs) are statements about level-ranked upward ladders only. Scratch attempts toward k = 4 (not in the output
  files; commands in notes/L-SI.md): `up107.py 8 18 full:6` no answer in 55 min (timeout 3,300 s); lifting the k = 3 model by a new bottom and top
  level (`--lift`): UNSAT at T = 18, 22; inserting two middle levels (`--lift … --mid 3`, with levels 2 / 2, 5 freed): no answer / UNSAT
  in 250 s; the «perfect» structure (`cap:h --upperbil h --dualcap h`: lower half key-capped, upper half a pure ladder of
  value-capped movers) is SAT at h = 2 (d = 4) and UNSAT at h = 3 (d = 6, T ≤ 24, 2 s).

## 7. DATA (experiments/si/box107/out; every SAT answer is a SEARCH answer of cadical195 via python-sat 1.9.dev15, UNCERTIFIED)
Counters and units. abandon107.out: one line per tower (set: the five tower genomes of claude/l-new a143d4060
experiments/new/box212/inst; scope: movers of level ≤ 7; «skipped» = movers above): bad_i (unit: full mover), viol_ii (unit: (full
mover, option, step) with the target's key changing while the mover starts the step on it), census of the key changes of W-targets
of full movers (away / arrive / leave), viol_iii (unit: the same for enumerating movers, with the predecessor test), viol_iv (unit:
(enumerating mover, option, time) of ONE-AHEAD; checks_iv = units tested), ctrl (the same test as viol_ii on NON-full movers: fires).
All must-0 counters are 0 on the five towers; «leave» is 0 (ABANDON) and «arrive» is frequent (carry chains). SAT lines: «len» = a
run of at least T steps exists; «full:x» = mover x (= 2·level + member) switches 2^(level+1) − 1 times within T steps. Exact horizons:
a 2-level ladder run has at most 8 steps and a 3-level one at most 22 (R113 T-BOUND), so «d 2 … len» is exact from T = 5 on (longest
run of a 2-level ladder: 4) and «d 3 T 22 full:4 UNSAT» is exact: NO 3-LEVEL LADDER HAS k = 3. d = 4 (N = 8): the query at T = 12 gave
no answer in 23 minutes and was stopped (not in the files); the Lead's anneal has k = 3 at d = 5 (N = 10), so the least d for k = 3
on ladders is 4 or 5 (OPEN). check107.sh re-derives the fast lines and compares the rest with the files.
ENCODER CONTROL (ctrl107.out; Lead 11:47Z: «feed it a known instance's parameters as unit clauses and require SAT with the same
run»): with every parameter of the Lead's instance fixed by unit clauses, syn107.py answers «len 7» SAT and «len 8» UNSAT, and
one217.OneP gives T_key = 7 on it: on this instance the general encoder neither loses nor invents a step. up107.py / bil107.py /
pn107.py have no such control beyond the replay of their SAT models; their UNSAT lines rest on the encoders as written.
Relation to landed text (Lead 12:10Z relays REFEREE-2 41 and L-NEW 77: 1P(G) with gate-index ε is R104's IDEAL model, so every
landed IDEAL lemma holds in 1P(G); not re-verified in this box): OMEGA restates R113 ALIGN + R120 MOVE; ODOMETER (1)-(3) on doubling
levels restates R120 DOUBLE-EQ / PULSE-NEST; FLIP-SUPPLY is the counting behind R113 PATH-RISE / box 217 A2. Not found in the landed
entries read (R113, R120): ABANDON at any shape and degree with the «arrive, never leave» rule, ENUM-ABANDON, ONE-AHEAD, CAUSE,
FROZEN / SEPARATION. R105 KEYFLIP and R111 PAIR-KF were NOT opened in this box (to do before any packet).
<!-- DATA107 begin -->
```
--- out/abandon107.out
DBL4_d20_F30.json N 40 T 30 lmax 7 skipped 24 full 0 [] enum 0 bad_i 0 viol_ii 0 census away 0 arrive 0 leave 0 viol_iii 0 viol_iv 0 checks_iv 0 ctrl 97
RECF4_d20_F60.json N 40 T 67 lmax 7 skipped 24 full 8 [0.0 0.1 1.2 1.3 2.4 2.5 3.6 3.7] enum 8 bad_i 0 viol_ii 0 census away 23 arrive 21 leave 0 viol_iii 0 viol_iv 0 checks_iv 756 ctrl 187
H5_d20_F62.json N 40 T 136 lmax 7 skipped 24 full 10 [0.0 0.1 1.2 1.3 2.4 2.5 3.6 3.7 4.8 4.9] enum 10 bad_i 0 viol_ii 0 census away 54 arrive 50 leave 0 viol_iii 0 viol_iv 0 checks_iv 2085 ctrl 214
H6_d24_F126.json N 48 T 209 lmax 7 skipped 32 full 12 [0.0 0.1 1.2 1.3 2.4 2.5 3.6 3.7 4.8 4.9 5.10 5.11] enum 12 bad_i 0 viol_ii 0 census away 162 arrive 66 leave 0 viol_iii 0 viol_iv 0 checks_iv 4036 ctrl 250
HIT7_d28_F254.json N 56 T 299 lmax 7 skipped 40 full 14 [0.0 0.1 1.2 1.3 2.4 2.5 3.6 3.7 4.8 4.9 5.10 5.11 6.12 6.13] enum 14 bad_i 0 viol_ii 0 census away 318 arrive 162 leave 0 viol_iii 0 viol_iv 0 checks_iv 6974 ctrl 222
TOTAL bad_i 0 viol_ii 0 viol_iii 0 viol_iv 0
--- out/replay107.out
out/k2_d2.json N 4 T_key 3 replay_equals_model 1 sw [1, 1, 3, 1] full [0, 1, 2]
--- out/ctrl107.out
ctrl/lead_bil4.json N 8 T_key 7 replay_equals_model 1 sw [1, 1, 1, 2, 1, 2, 1, 1] full [0, 1]
SYN107 d 4 T 7 goal len extra [] FIXED ctrl/lead_bil4.json solver cadical195 answer SAT
SYN107 d 4 T 8 goal len extra [] FIXED ctrl/lead_bil4.json solver cadical195 answer UNSAT
--- out/syn107.out
SYN107 d 2 T 6 goal full:2 extra [] solver cadical195 answer SAT
SYN107 d 2 T 3 goal len extra [] solver cadical195 answer SAT
SYN107 d 2 T 4 goal len extra [] solver cadical195 answer SAT
SYN107 d 2 T 5 goal len extra [] solver cadical195 answer UNSAT
SYN107 d 2 T 6 goal len extra [] solver cadical195 answer UNSAT
SYN107 d 2 T 7 goal len extra [] solver cadical195 answer UNSAT
SYN107 d 2 T 8 goal len extra [] solver cadical195 answer UNSAT
SYN107 d 3 T 22 goal full:4 extra [] solver cadical195 answer UNSAT
--- out/bil107.out
BIL107 d 2 T 2 full None vars 58 clauses 186 answer SAT
BIL107 d 2 T 3 full None vars 78 clauses 271 answer UNSAT
BIL107 d 3 T 3 full None vars 128 clauses 457 answer SAT
BIL107 d 3 T 4 full None vars 162 clauses 604 answer UNSAT
BIL107 d 4 T 6 full None vars 322 clauses 1270 answer SAT
BIL107 d 4 T 7 full None vars 370 clauses 1479 answer UNSAT
BIL107 d 5 T 8 full None vars 538 clauses 2184 answer SAT
BIL107 d 5 T 9 full None vars 600 clauses 2455 answer UNSAT
BIL107 d 6 T 11 full None vars 886 clauses 3679 answer SAT
BIL107 d 6 T 12 full None vars 962 clauses 4012 answer UNSAT
--- out/up107.out
UP107 d 2 T 3 goal len maxjump None fuelonly None vars 175 clauses 677 answer SAT
UP107 d 2 T 4 goal len maxjump None fuelonly None vars 218 clauses 880 answer UNSAT
UP107 d 3 T 5 goal len maxjump None fuelonly None vars 690 clauses 3097 answer SAT
UP107 d 3 T 6 goal len maxjump None fuelonly None vars 812 clauses 3690 answer UNSAT
UP107 d 4 T 7 goal len maxjump None fuelonly None vars 2019 clauses 9347 answer SAT
UP107 d 4 T 8 goal len maxjump None fuelonly None vars 2290 clauses 10648 answer UNSAT
UP107 d 4 T 7 goal full:2 maxjump None fuelonly None vars 2043 clauses 9388 answer SAT
UP107 d 5 T 12 goal full:4 maxjump None fuelonly None vars 6410 clauses 29612 answer UNSAT
UP107 d 6 T 14 goal full:4 maxjump None fuelonly None vars 12578 clauses 57604 answer SAT
--- out/replay107_up.out
out/up_k2_d4.json N 8 T_key 3 replay_equals_model 1 sw [1, 1, 3, 1, 2, 2, 1, 1] full [0, 1, 2]
out/up_k3_d6.json N 12 T_key 8 replay_equals_model 1 sw [1, 1, 3, 3, 7, 1, 3, 3, 3, 2, 1, 1] full [0, 1, 2, 3, 4]
--- out/pn107.out
PN107 P 1 T 1 chain 0 full None vars 24 clauses 49 answer SAT
PN107 P 1 T 2 chain 0 full None vars 32 clauses 80 answer UNSAT
PN107 P 2 T 2 chain 0 full None vars 109 clauses 401 answer SAT
PN107 P 2 T 3 chain 0 full None vars 140 clauses 580 answer UNSAT
PN107 P 3 T 4 chain 0 full None vars 267 clauses 1228 answer SAT
PN107 P 3 T 5 chain 0 full None vars 314 clauses 1513 answer UNSAT
PN107 P 4 T 6 chain 0 full None vars 494 clauses 2544 answer SAT
PN107 P 4 T 7 chain 0 full None vars 557 clauses 2941 answer UNSAT
PN107 P 5 T 10 chain 0 full None vars 948 clauses 5425 answer SAT
PN107 P 3 T 22 chain 1 full [(2, 0)] vars 1320 clauses 6004 answer UNSAT
PN107 P 4 T 30 chain 1 full [(2, 0)] vars 2322 clauses 11056 answer UNSAT
PN107 P 5 T 20 chain 1 full [(2, 0)] vars 1910 clauses 9379 answer UNSAT
PN107 P 6 T 20 chain 1 full [(2, 0)] vars 2272 clauses 11526 answer UNSAT
```
<!-- DATA107 end -->

## 8. Open, and next
- OPEN: QUIET-KEY-1P / SW-POLY; the sharing question of §4; a timing statement in the half-rate regime (§2).
- Next (this lane): upward ladders at k = 4 (d = 7, 8) and k = 5 (d = 10); if they exist, read the wiring rule off capped models
  and test it on one217.OneP at k = 6, 8; if k = 4 fails at d = 8, that failure is the first piece of an f(k).
