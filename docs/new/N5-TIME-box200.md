# Box 200 (D18): a time charge for SPLIT-COUNT; the open core becomes the RETURN count of one Howard edge (L-NEW successor 67, Opus; written 2026-11-08 23:48Z by date -u)
Lead brief (successor 67, «go» 2026-11-08 23:22Z): «BOX 200: a TIME CHARGE for the recursion Dhi_y(b) = 1 + Σ_(z above y) c_z(b) … so that
the recursion does not multiply — e.g. charge each new high part at b to a distinct Howard step …»; Lead 23:22Z: «SPLIT-COUNT's sum is
loose by ~10× (DHIB26) … count only the high-part changes at b that are FOLLOWED by a y-top through (u, b) (the «used» changes) … state such
a refinement as a lemma if you can, and test it on DHIB26 / DHIB18 / MW32_2 / RWX_n95».
Labels: PROVED (lane, unrefereed) / CONJECTURE / DATA (unit, set, scope, counter) / DEAD / READING. Nothing here is a TARGET.md claim.
G-N5-TIME stays OPEN; N5′-xi stays a CANDIDATE (D1). Setting, notation, premises: the frozen packet P-N5-SPLIT (docs/new/P-N5-SPLIT.md,
l-new 399cda07, sha1 5bc1b1f3), on P-N5-CHAIN's facts only (R125 pending). L-SI 48 is generalising L-SI 47's Lemma SUPERSET (claude/l-si
de914535, box 90 §7) from the design side; this box does not use or duplicate it.
Tool: experiments/new/box200/self200.py (same engine as split199.py: gamma3.build with pads, n5v.step mode xi from S3, up to the first
fallback); record box200/self200.out; check200.sh -> check200.out, re-run by check.sh block «BOX 200 SELF».

## 0. Answer
- PROVED (lane): Lemma SELF. A y-top of v through the split pair (u, b) at step t IS a y-top of u at t, at a step where u itself SWITCHES
  INTO b (a Howard switch at a mover, a face flip at a gate), with Λ(u) = Λ(v) = w at t − 1 and t.
- PROVED (lane): Corollary TIME-CHARGE. c_y(v, I) ≤ Σ_((u,b) ∈ SPL_y(v,I)) S_y(u, b, w), where S_y(u, b, w) is a set of DISTINCT HOWARD
  STEPS: the steps at which u switches into b while Λ(u) = w and u's own change has top y. No recursion, so nothing multiplies. It refines
  SPLIT-COUNT (S_y(u, b, w) ≤ Dhi_y(b, J_b)) and it is exactly the Lead's «used changes» count, taken at the switching vertex.
- PROVED (lane): Σ_y S_y(u, b, w) ≤ R(u, b, w) := the number of switches of u into b while Λ(u) = w. Hence C ≤ 3M·R, R := max R(u, b, w).
  Lemma LEAP: between two such switches the abandoned successor a overtakes b, and b then overtakes a (REWIN without the letter).
- PROVED (lane, elementary) Corollary R-EQUIV: R ≤ T3 and T3 ≤ N(2M + 2) + M(2M + 3)·R. So T3 is polynomial iff R is. R is a classical
  quantity of Howard's policy iteration: how often ONE edge is re-chosen. The time charge is SHARP on data (§3): Σ S ≤ 8 where SPLIT-COUNT's
  sum is 45 (DHIB26_2804). But it lands on a target that is equivalent to G-N5-TIME on Γ3 by a two-line argument. It is a reduction, not
  progress toward a bound.
- D18 (§4, READING): the [VJ] order on Π is a total reward with weights ±2^rank. Hansen–Miltersen–Zwick's strongly polynomial bound for
  strategy iteration (arXiv 1008.0530) is what R needs, but it needs a CONSTANT discount. The lexicographic order corresponds to
  1/(1 − γ) of order 2^rank, so the transfer gives nothing. What a transfer would need is stated in §4.

## 1. Lemma SELF and Corollary TIME-CHARGE (PROVED, lane; premises: P-N5-SPLIT §2 (SPLIT, TRANSFER), P-N5-CHAIN F6, LOC-K2-3)
Notation: for a vertex u with ≥ 2 successors in HOW3 (a mover or a gate; LOC-K2-3: K2 never changes), a successor b, and a vertex w,
S_y(u, b, w) := {t : nx_(t−1)(u) ≠ nx_t(u) = b, Λ_(t−1)(u) = Λ_t(u) = w, and the change E_(t−1)(u) → E_t(u) has top y},
R(u, b, w) := |{t : nx_(t−1)(u) ≠ nx_t(u) = b, Λ_(t−1)(u) = Λ_t(u) = w}|.
**Lemma SELF.** Let t be a y-top of (v, I), Λ(v) = w on I, with split u and new successor b = nx_t(u) (P-N5-SPLIT §2). Then t ∈ S_y(u, b, w).
Proof.
- By SPLIT (i) nx_(t−1)(u) ≠ nx_t(u) = b, and by TRANSFER (iv) Λ_(t−1)(u) = Λ_t(u) = w and E_(t−1)(u) Δ E_t(u) = E_(t−1)(v) Δ E_t(v).
- So u's own change at t has the same symmetric difference, hence the same top y. That top enters E(u): y ∈ E_t(v) and y is not before u
  on v's play (the part before u is common to t − 1 and t, and y ∉ E_(t−1)(v)), so y ∈ E_t(u) ((PL)). ∎
**Corollary TIME-CHARGE.** c_y(v, I) ≤ Σ_((u,b) ∈ SPL_y(v,I)) |S_y(u, b, w)| ≤ 3M · max_(u,b) |S_y(u, b, w)|, and Σ_y |S_y(u, b, w)| ≤ R(u, b, w).
Proof. Each y-top of (v, I) is one step t. It lies in S_y(u, b, w) for its own pair (SELF), and distinct y-tops are distinct steps. So the
y-tops through (u, b) inject into S_y(u, b, w). Sum over SPL_y (≤ 3M, P-N5-SPLIT §4). For fixed (u, b, w) the sets S_y, over the letters y,
are disjoint (one top per change), and all lie in the switch steps counted by R(u, b, w). ∎
- Relation to the Lead's «used» changes: for the pair (u, b), the number of y-tops of v through it equals 1 + the number of «used» changes
  of E(b) ∩ U_y (the rises of PAIR-SPLIT (c′), one between consecutive same-pair y-tops). TIME-CHARGE bounds this count by
  |S_y(u, b, w)|. That is the same count at the switching vertex u itself, where it is a count of Howard steps.
- Relation to SPLIT-COUNT: applied at v := u, SPLIT-COUNT gives |S_y(u, b, w)| ≤ Dhi_y(b, J_b). So TIME-CHARGE ⇒ SPLIT-COUNT, and the gap
  is the «unused» high parts of b, i.e. those not followed by a switch of u into b with top y.
- Why it does not multiply: the bound is a sum over at most 3M pairs of a quantity that is not recursive. The recursion of SPLIT-COUNT
  (Dhi_y(b) = 1 + Σ_z c_z(b), each c_z(b) again a sum over b's pairs) is replaced by one count of steps at one vertex.
**Lemma LEAP (PROVED, lane; P-N5-SPLIT §3 (a)(b) with the letter removed).** Let t < t′ be consecutive switches of u into b (t, t′ ∈
R(u, b, w)), and a := nx_(t′−1)(u). Then Ω_(t′−1)(a) ▷ Ω_t(b) and Ω_(t′−1)(b) ▷ Ω_(t′−1)(a).
Proof. §3 (a)(b) of P-N5-SPLIT use only nx_t(u) = b ≠ nx_(t′−1)(u) and the switch at t′: mover, F1, STRICT, F3, F4′, F5, F6, CN2-3; gate,
LOC-GATE3, NO-TIE3, F1. ∎ The two successors leapfrog: every return to b needs a strict overtaking by a, then by b.
**Corollary R-EQUIV (PROVED, elementary).** R := max over (u, b, w) of R(u, b, w). Then C ≤ 3M·R, R ≤ T3, and
T3 ≤ N(2M + 2) + M(2M + 3)·R. So T3 is polynomial in N + M iff R is, iff C is (C-EQUIV).
Proof. The first is TIME-CHARGE. R ≤ T3: one switch per step at most. Each step t < T3 switches at least one mover (definition of T3).
A mover x's Λ changes at most 2M + 2 times (CYC: at most 2M + 3 values, each change to a larger reward). So the switches of x are those
at a step where Λ(x) changes (≤ 2M + 2) plus those counted in some R(x, b, w). x has one successor per option (its pads), so there are
M pairs (x, b) over all movers, and each has ≤ 2M + 3 values of w. ∎
- READING: R-EQUIV needs neither SPLIT nor TRANSFER. Only C ≤ 3M·R uses them. So the time charge relocates the open core from route
  vertices to one edge of one Howard mover. That is where policy-iteration lower bounds (exponentially many re-choices of one edge) live.
  Howard on Γ3(G) is therefore polynomial iff no edge is re-chosen super-polynomially often within one cycle-node interval.

## 2. Gate and mover returns, and what LEAP gives (PROVED / READING)
- With Λ(a) = Λ(b) = w at the comparison times (both on u's play, (PL)), LEAP's overtakings are decided by (LEX-Λ): by the e-part if
  the e-sets differ, otherwise below every e-vertex (β-part or length). A return at which u's e-set changes is counted in some S_y. The
  others («low returns») do not change E(u). They are bounded through QUIET3 only when no class changes elsewhere, which is not the case
  in general. Data: max R ≤ 8 on the frozen set outside MW (§3); low returns were not counted separately (not measured).
- What a polynomial bound on R needs (READING): an elimination statement. After some polynomial number of returns of u to b inside one
  Λ-interval of u, either u never returns to b, or Λ(u) changes. LEAP alone gives none: two lex-monotone sequences can overtake each
  other once per value change, i.e. Dhi-many times.

## 3. DATA (self200.py; set: the eight frozen instances below; scope: N5′-xi from S3 on Γ3, up to the first fallback, [E-LEV] holds)
Units: selffail (y-top of (v, I) not in S_y(u, b, w); must be 0, SELF); tcfail ((v, I, y) with c_y > Σ_(u,b) |S_y|; must be 0, TIME-CHARGE);
swfail ((u, b, w) with Σ_y |S_y| > R; must be 0); leapfail (consecutive switch couple violating LEAP; must be 0). Totals per instance.
Descriptive maxima: maxc = C (per (v, I, y)); maxused (per (v, I, y, (u, b)): the y-tops through one pair = 1 + used changes); maxS
(per (y, u, b, w)); maxsumS (per (v, I, y): Σ_(u,b) |S_y|); maxsw = R (per (u, b, w)); maxDhib, maxsumD (L-RED 62's Dhib, sumD on this
engine, Dhi over b's Λ-interval at the pair's first y-top). returns: total consecutive-switch couples (unit: (u, b, w, t, t′)).
| instance (sha1, first 8) | T3 | y-tops | returns | C | maxused | maxS | maxsumS | R | maxDhib | maxsumD | must-0 counters |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CX4_n21 (ef29debb) | 10 | 728 | 17 | 5 | 4 | 4 | 6 | 4 | 6 | 12 | 0 0 0 0 |
| C6G8_n54 (52067442) | 17 | 2,598 | 54 | 6 | 6 | 6 | 6 | 6 | 8 | 16 | 0 0 0 0 |
| RWX_n95 (da8b3a30) | 12 | 2,644 | 17 | 2 | 2 | 2 | 2 | 3 | 7 | 8 | 0 0 0 0 |
| DHIB18_2805 (9e8c2e3c) | 19 | 6,707 | 105 | 4 | 4 | 4 | 8 | 6 | 18 | 30 | 0 0 0 0 |
| DHIB26_2804 (2c49fd10) | 28 | 9,482 | 174 | 4 | 4 | 4 | 8 | 8 | 26 | 45 | 0 0 0 0 |
| FW16_2 (94df42b7) | 53 | 2,031 | 1 | 3 | 1 | 1 | 3 | 2 | 1 | 3 | 0 0 0 0 |
| WC16_2 (995e7132) | 4 | 513 | 0 | 1 | 1 | 1 | 1 | 1 | 2 | 2 | 0 0 0 0 |
| MW32_2 (445031d1) | 199 | 3,068 | 256 | 65 | 65 | 65 | 65 | 65 | 66 | 66 | 0 0 0 0 |
(must-0 counters in the order selffail, tcfail, swfail, leapfail.)
- Controls (CX4_n21): ctrl1 (S counted only for u = v, i.e. no TRANSFER) selffail 689, tcfail 420; ctrl2 (b := the OLD successor)
  selffail 728, tcfail 442; ctrl3 (R := 0) swfail 22; ctrl4 (LEAP direction reversed) leapfail 17. Each must-0 counter has a control that
  fires.
- Reading:
  - TIME-CHARGE is within a factor ≤ 2 of C on every row (maxsumS / C ≤ 2). SPLIT-COUNT's sum is 11× C on DHIB26: the climbed Dhi at
    route vertices are «unused» high parts.
  - R ≥ C on every row except CX4_n21 (C 5, R 4) and FW16_2 (C 3, R 2), where c_y spreads over several split pairs.
  - MW is tight everywhere: one edge re-chosen 2n + 1 times in one Λ-interval (R = 65 at n = 32), linear in N + M, with T3 = 6n + 7.
  - No instance has R above linear. These are short runs (T3 ≤ 199). They are not a bound.
- Instances: CX4_n21, C6G8_n54, RWX_n95, FW16_2, MW32_2 are the box199/inst copies. DHIB26_2804, DHIB18_2805 are copied from claude/l-red
  4b309716 experiments/red/r228/inst (sha1 = its SHA1SUMS). WC16_2 is copied from claude/l-si de914535 experiments/si/box90/inst (sha1 =
  its SHA1SUMS). All are frozen in box200/inst with SHA1SUMS.

## 4. D18: the lexicographic value as a total reward, and discounted strategy iteration (READING; source opened)
- Source opened: T. D. Hansen, P. B. Miltersen, U. Zwick, «Strategy iteration is strongly polynomial for 2-player turn-based stochastic
  games with a constant discount factor», arXiv 1008.0530 (abstract read 2026-11-08, before the 23:48Z date -u stamp of this file, via arxiv.org/abs/1008.0530). The abstract states:
  Howard's policy iteration on a discounted MDP terminates within O(m/(1 − γ)·log(n/(1 − γ))) iterations (an improvement of Ye's bound by a
  factor n), and the same bound holds for strategy iteration on 2-player turn-based stochastic games with discounted zero-sum rewards;
  strongly polynomial for constant γ. I have NOT opened the body: the mechanism («some action is eliminated for good after O(1/(1 − γ)·log)
  iterations» is my recollection, not checked) is not cited as a fact.
- Connection (READING, mine): [VJ]'s Π-comparison (most relevant vertex of the symmetric difference, better for Even iff even and in the
  larger set) equals comparing Σ_(z ∈ Π) (−1)^pr(z)·2^rank(z). So on one Λ-interval, Howard on Γ3 is Howard on a deterministic
  total-reward game with weights ±2^rank, ties broken by length. In that picture R(u, b, w) is the number of times one action is re-chosen.
  That is the quantity an action-elimination argument bounds.
- What transfers and what does not:
  - HMZ's bound depends on the rewards not at all, but on 1/(1 − γ). An undiscounted total reward is the limit γ → 1. Simulating the
    lexicographic order by a discount needs γ so close to 1 that the length tie-breaks and the 2^rank weights survive, i.e.
    1/(1 − γ) ≳ 2^(max rank) (my estimate, not proved). The bound then is exponential: nothing transfers.
  - What would transfer: an elimination lemma whose «discount» is replaced by the cycle-node structure. Inside one Λ-interval every play
    ends in the same cycle w, so the game is a reachability-to-w game with path weights. A candidate statement (CONJECTURE ELIM-Λ, stated
    only to be attacked): for every Λ-interval of a mover u and every successor b, R(u, b, w) ≤ p(N + M) for a fixed polynomial p. By
    R-EQUIV it is EQUIVALENT to G-N5-TIME on Γ3, so it is a restatement, not a new hypothesis. Its value is that it names the object that
    known strongly polynomial analyses bound. I give it no weight beyond that.
  - A real gain would be a potential in which each return to b costs a constant fraction of a polynomially bounded quantity (HMZ's
    «reduced cost» argument). Here values are lexicographic, so «fraction» has no meaning without a numerical embedding. That is the gap.
- Verdict of the D18 try: the connection is exact (R is HMZ's object), but the discount is what makes HMZ polynomial, and Γ3 has none.
  No result.

## 5. Status after box 200 (labels)
- PROVED (lane; P-N5-SPLIT + P-N5-CHAIN facts): SELF, TIME-CHARGE, LEAP, R-EQUIV. TIME-CHARGE answers the Lead's refinement: the «used»
  count at the pair is bounded by Howard steps at u, with no multiplication.
- Open core: R = max returns of one edge within one Λ-interval of its mover (or gate). Equivalent to T3 polynomial (R-EQUIV).
- Kill side (READING): a family with R super-polynomial must re-choose ONE edge super-polynomially often. MW does this linearly (one edge,
  2n + 1 times). Stacking MW races, «a race of races», is L-SI's open design step (box 90 §6: spacing doubles per level, so C ∝ T3).
- Not done: a lemma on low returns (§2); any elimination statement.
