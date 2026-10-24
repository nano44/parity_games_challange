# N5 through the operations-research lens: action elimination inside a joint λ-phase
L-SI successor 1 (Opus 5.5, D15), box 1. Lead GO 2026-10-24 13:27Z (owner D18). Started 13:30Z; first version 13:47Z (date -u).
Status: proof attempt on GAPS G-N5-TIME. Labels: PROVED (by whom), CONJECTURE (with data), OPEN, DATA, READING. Unrefereed.
No polynomial bound is claimed. G-N5-TIME stays OPEN.
Object: N5 = docs/new/N5-ssi-global.md SPEC S1-S5. My runs use experiments/si/orlens/ortrace.py. It repeats the loop of
experiments/new/n5.py and imports n5.py read-only for dual(). Every run asserts that the iteration and fallback counts equal
n5.run's.
Sources opened, with sha256 prefixes of the PDFs:
- HMZ: Hansen, Miltersen, Zwick, arXiv 1008.0530 v1 (f53a6b51…), Lemmas 3.7, 4.2, 4.8, 5.1, 5.3-5.5, 6.1-6.4, Theorem 6.5, §7.
- Scherrer, arXiv 1306.0386 v4 (391b6481…), Theorems 1-7, Lemmas 4-5, Assumption 1, §2 remark on the 1/(1−γ) factor.
- Post and Ye, arXiv 1208.5083 v2 (c51876eb…), abstract, Lemmas 3.4-3.5.
- Ye 2011 (Math. Oper. Res. 36(4), DOI 10.1287/moor.1110.0516) was NOT opened. Its theorem is used only as Scherrer's
  Theorem 1 quotes it.

## 0. Result in one paragraph
- **The correspondence is exact (§1).**
  - action = an Even edge (x, z). For Odd's best reply σ̄: an Odd edge (y, e), e.g. an exit of o.
  - "Eliminated forever inside a joint λ-phase" = never again in σ_k (resp. σ̄_k) for the rest of the phase.
  - potential = the gap level g_k(v), the ultrametric level of the first difference between Ξ_k(v) and the phase target T(v).
    T is the honest valuation at the phase's last state.
  - reduced cost / slack of an action = s(x, z), the level of the first difference between x ⊕ T(z) and T(x).
- **Ingredient 1 of Ye/HMZ transfers to VJ valuations, PROVED (§2).** "A used action certifies its slack, so once the gap is
  below the slack the action is gone for the rest of the phase" (HMZ Lemmas 6.1-6.2):
  - Lemmas U, E1-E5;
  - for Even edges, and for Odd's best reply at exits;
  - for EVERY strategy-improvement rule with monotone honest valuations, so in particular for N5.
- **Ingredient 2, the contraction (HMZ Lemma 4.8 / 5.5), has no analogue (§3).**
  - PROVED (Lemma D): classical switch-all SI satisfies "Howard dominates value iteration" in VJ valuations (HMZ Lemma 5.3).
  - Switch-all is nevertheless exponential inside ONE λ-phase on Friedmann's switchallexp.
  - So lexicographic value iteration is itself exponentially slow there. DATA: from Ξ_0 it gets stuck at a spurious (c, P)
    fixed point.
  - The "lexicographic discount" contracts nothing. It is the γ → 1 limit, where Scherrer says the 1/(1−γ) factor cannot be
    removed for Howard's PI.
  - Bellman-Ford truncation (a horizon of k edges) is the right "combinatorial discount" for ONE player. That is exactly
    RESULTS R17's Lemma P (§3.3).
  - N5 does not even satisfy Howard ≥ VI. The exact failing step is a trust-routed vertex (i4_hand, states 0-2, vertex z = 9;
    §3.4).
- **What N5 does instead (§4).**
  - HMZ's specific mechanism, "the max-slack action is gone within L steps", FAILS on returns_rt48: a max-slack edge of σ_k
    persists 77 transitions in a 78-transition phase.
  - Yet N5 eliminates SOME action almost every transition. On every instance named in the brief, plus L-RED's and L-NEW's
    pinned ones, the longest run of non-eliminating transitions inside a phase is at most 17, at n up to 64.
  - The switch-all control on switchallexp shows this run doubling with N (24, 62, 140, 298).
- **CONJECTURE (ELIM-n) (§5): every n consecutive transitions of a joint λ-phase contain an eliminating one.**
  - With Lemma Φ it implies N5 < (2n(n−1)+1)·n·(m_E + 1) iterations, which is G-N5-TIME. This implication is PROVED (§5).
  - (ELIM-n) is not proved. I have no route to it. It is a reformulation, but one with a structural test that separates N5 from
    switch-all.
- **For the brief's (CYC) target, a narrower CONJECTURE (CYC-ELIM) (§4.3), the Post-Ye Lemma 3.6 shape.**
  - Every non-eliminating window contains ≤ d θ-changes (d = o's out-degree). The data give at most 3.
  - PROVED: (CYC-ELIM) implies θ-changes ≤ (d+1)(m+1) per phase, i.e. (CYC).
  - On 𝒞^1O, Lemma G supplies L-LIT's LP(t) family; N5 prices with LP(θ) and selects with LP(w) (§3.3b).
- **The gap-level potential itself gives no (CYC) or (TRUST) bound.**
  - θ-changes are almost all FLAT in gap level: theta_thc24 has 16 θ-changes in one phase, only 2 of which lower g(o).
  - So no level potential counts them (§4.3).

## 1. The exact correspondence

| Ye / HMZ (discounted MDP / 2TBSG) | N5 inside one joint λ-phase Φ = states a..b |
| --- | --- |
| state i | vertex v |
| action a ∈ A_i | Even edge (x, z). For Odd's best reply: Odd edge (y, e), e.g. an exit e of o on 𝒞^1O |
| strategy σ^k, best response τ2(σ^k) | σ_k; σ̄_k = Odd's optimal counter-strategy to σ_k (S1). Not τ_k: Ξ_k is the honest valuation, as in HMZ |
| value v^{π_k} (monotone, Lemma 5.2) | Ξ_k := Ξ_{σ_k}, ⊴-monotone (RESULTS R15 (a)) |
| optimal value v* | phase target T := Ξ_b, the honest valuation at the phase's last state (the global optimum has other cycle nodes in earlier phases) |
| reduced cost (c^{π*})_a ≥ 0 | slack level s(x, z) := lev(T(x), x ⊕ T(z)), for actions with x ⊕ T(z) ⊴ T(x) |
| ‖v^π − v*‖ | gap level g_k(v) := lev(T(v), Ξ_k(v)) |
| contraction ‖v^{k} − v*‖∞ ≤ γ^k ‖v^0 − v*‖∞ (Lemma 5.5) | none; see §3. One-player substitute: R17 Lemma P (horizon k after k steps) |
| "action eliminated": a ∉ σ^ℓ for ℓ > k + L (Lemma 6.4) | (x, z) ∉ σ_ℓ for ℓ > k in Φ |

Definitions.
- Valuations are (c, P, ℓ) as in S1. ⊴ is Even's S1 order.
- x ⊕ (c, P, ℓ) := (c, P ∪ ({x} if rank(x) > rank(c)), ℓ + 1). This is the prefix of R17 §1.
- λ_k(v) is the cycle node of Ξ_k(v). It is constant in v's entry over Φ, and T has the same cycle nodes.
- lev(a, b) is the level of the first difference:
  - −1 if a = b;
  - 0 if c and P agree and ℓ differs;
  - 1 + r if c agrees and r is the top rank of P_a Δ P_b;
  - n + 1 if the cycle nodes differ.
  The levels are ordered as integers.

## 2. PROVED: the elimination half (L-SI successor 1; elementary; uses only R15 (a) and S1)
Facts used:
- (F-mono) Ξ_k ⊴ Ξ_{k+1} pointwise (R15 (a)). Hence Ξ_k ⊴ T on Φ.
- (F-bell) If λ_k(v) ≠ v, then Ξ_k(v) = v ⊕ Ξ_k(succ), where succ = σ_k(v) for Even v and σ̄_k(v) for Odd v.
  - The play from v continues at succ.
  - If v lies on the final cycle, the play from succ reaches the cycle node before it returns to v.
- (F-pre) If a ⊴ b and a, b have the same cycle node, then x ⊕ a ⊴ x ⊕ b and lev(x ⊕ a, x ⊕ b) = lev(a, b).
  - x is added to both path sets or to neither, and both lengths grow by 1.
  - This is R17 (V2).

**Lemma U (ultrametric).**
(i) lev(a, c) ≤ max(lev(a, b), lev(b, c)).
(ii) If a ⊴ b ⊴ c, then lev(a, b) ≤ lev(a, c) and lev(b, c) ≤ lev(a, c).
Proof of (i): if both levels on the right are ≤ n, then a, b, c share the cycle node, and top(P_a Δ P_c) ≤
max(top(P_a Δ P_b), top(P_b Δ P_c)). If both are ≤ 0, the path sets are equal.
Proof of (ii): if lev(a, c) = n + 1 there is nothing to prove. Otherwise c(a) = c(c), and rew(c(a)) ≤ rew(c(b)) ≤ rew(c(c)) with
rew injective, so c(b) is the same node. Let r0 := top(P_a Δ P_c) (−∞ if equal), and suppose r := top(P_b Δ P_c) > r0.
- a and c agree at every rank ≥ r.
- So top(P_b Δ P_a) = r as well, with the same membership pattern.
- S1's rule at the top differing rank depends only on which side contains r and on r's parity. So b ▷ a and b ▷ c, or b ◁ a and
  b ◁ c. Either contradicts a ⊴ b ⊴ c.
- The same argument covers lev(a, b), and lengths when P_a = P_c (then P_b = P_a). □

**Lemma E1 (gap monotone).** For k ≤ k' in Φ: g_{k'}(v) ≤ g_k(v).
Proof: Ξ_k ⊴ Ξ_{k'} ⊴ T (F-mono), then U (ii). □

**Lemma E2 (a used action certifies its slack; HMZ Lemma 6.1).** Let k ∈ Φ, x Even with λ(x) ≠ x, z = σ_k(x), and suppose
x ⊕ T(z) ⊴ T(x). Then g_k(x) ≥ s(x, z).
Proof:
- Ξ_k(x) = x ⊕ Ξ_k(z) (F-bell).
- Ξ_k(z) ⊴ T(z), and both have cycle node λ(z) = λ(x). So by F-pre, Ξ_k(x) ⊴ x ⊕ T(z) ⊴ T(x).
- U (ii) with b = x ⊕ T(z) gives lev(T(x), x ⊕ T(z)) ≤ lev(T(x), Ξ_k(x)). □

**Corollary E3 (elimination for the rest of the phase).** If g_k(x) < s(x, z), then σ_ℓ(x) ≠ z for every ℓ ≥ k in Φ (E1 + E2). □

**Lemma E4 (Odd's best reply; exits).** Let y be Odd with λ(y) ≠ y, e = σ̄_k(y), and suppose T(y) ⊴ y ⊕ T(e). Then
g_k(e) ≥ s̄(y, e) := lev(y ⊕ T(e), T(y)). So once g_k(e) < s̄(y, e), σ̄ never again uses e at y in Φ.
Proof:
- y ⊕ Ξ_k(e) = Ξ_k(y) ⊴ T(y) ⊴ y ⊕ T(e).
- U (ii) gives lev(T(y), y ⊕ T(e)) ≤ lev(y ⊕ Ξ_k(e), y ⊕ T(e)).
- By F-pre the right-hand side is g_k(e). □
On 𝒞^1O with y = o this restricts σ̄-laps (box 25 §4): σ̄(o) can return to an exit e only while g(e) ≥ s̄(o, e).

**Lemma E5 (gap ≤ largest slack on the play; HMZ Lemma 6.2 shape).** Extend s(x, z) := lev(T(x), x ⊕ T(z)) to all edges.
- Hypothesis: at every Odd y on the (σ_k, σ̄_k)-play from v before λ(v), T(y) ⊴ y ⊕ T(σ̄_k(y)).
- Claim: g_k(v) ≤ max of s(x, σ_k(x)) over the Even x on that play.
Proof, backwards along the play:
- At the cycle node c, Ξ_k(c) = T(c) = (c, ∅, 0), so g = −1.
- Even x: g(x) ≤ max(s(x, z), g(z)), by U (i) and F-pre.
- Odd y: g(y) ≤ g(σ̄_k(y)), by U (ii) as in E4. □
With E2: max_v g_k(v) lies between the largest slack of σ_k's used non-negative-slack edges and the largest level s over all
of σ_k's used edges on plays. HMZ's equality is recovered when no used edge has negative slack.

**Theorem E6 (level counting; rule-independent).** Inside Φ, at most n(n+1) transitions change some g_k(v).
Proof: in Φ, g takes values in {−1, …, n}, and each value can only fall (E1). □
- This holds for every rule with (F-mono), including exponential ones.
- So the whole difficulty lies in FLAT transitions: values change only strictly below every vertex's gap level.
- DATA (gaps.py): flat transitions dominate the long phases. returns_ph64: 91 of 103 transitions are flat. fts_g43: 91 of 120.

DATA check of U and E1-E4 (gaps.py counts every violation): 0 violations on all 29 runs where gaps.py ran: every N5 instance of §4.2, plus i3hn, cyc4, lap_n6, oneodd_c16 and two climb bests.

## 3. The contraction half has no lexicographic analogue
### 3.1 PROVED (L-SI): switch-all satisfies "Howard ≥ value iteration" (HMZ Lemma 5.3) in VJ valuations
Bellman operator on valuation vectors:
- T(V)(x) = max_z x ⊕ V(z) for Even x;
- T(V)(x) = min_z x ⊕ V(z) for Odd x;
- a vertex that is its own cycle node in V keeps V(x).
T is monotone (F-pre, and a different cycle node is not affected by the prefix).

**Lemma D.** Let σ_{k+1} be the switch-all successor of σ_k: each x with an improving edge takes the Ξ_k-best successor.
Suppose the transition k → k+1 stays in one λ-phase and x is not a cycle node. Then Ξ_{k+1}(x) ⊵ T(Ξ_k)(x).
Proof:
- Even x: σ_{k+1}(x) = z*, the ⊴-best successor, or x keeps σ_k(x), which is then already best. Since the transition stays in
  the phase, z* has x's cycle node.
  So Ξ_{k+1}(x) = x ⊕ Ξ_{k+1}(z*) ⊵ x ⊕ Ξ_k(z*) = T(Ξ_k)(x), by F-bell, F-mono and F-pre. The prefix x ⊕ · preserves ⊴, so
  x ⊕ Ξ_k(z*) is the maximum.
- Odd y: T(Ξ_k)(y) ⊴ y ⊕ Ξ_k(σ̄_k(y)) = Ξ_k(y) ⊴ Ξ_{k+1}(y), by F-bell and F-mono.
  This half holds for every rule. Only the Even half uses switch-all. □
(vi.py checks the inequality wherever T(Ξ_k)(x) keeps x's cycle node. By the proof this covers every Even x and is harmless for
Odd x.)

**Corollary D1.** Along a switch-all run in which every honest valuation Ξ_k has the same single cycle node s at every vertex,
Lemma D holds at every v ≠ s, and Ξ_k ⊵ T^k(Ξ_0) for all k. T is monotone, and T^k(Ξ_0) keeps cycle node s everywhere.
DATA: this holds on switchallexp N 3, 4, 5, where every state's cycle nodes are {0}.
- On switchallexp, switch-all runs exponentially long. DATA here: 70, 150, 310, 630, 1243 iterations for N = 3..7 (doubling),
  all in ONE λ-phase. This is consistent with Friedmann 1106.0778 Thm 6.14 (≥ 2^n on G_n from ι_{G_n}), as opened by my
  predecessor (notes/L-SI.md).
- So T^k(Ξ_0) ◁ T somewhere for every k below that count. Lexicographic value iteration needs exponentially many rounds:
  HMZ Lemma 4.8 / 5.5 has no analogue.
- DATA (vi.py), stronger: value iteration from Ξ_0 reaches a (c, P) fixed point of T below the optimum and stays there. Only the
  lengths keep moving.
  - switchallexp N 3 (n 49): stationary from round 11, 45 vertices wrong after 300 rounds.
  - N 5 (n 77): stationary from round 15, 73 wrong.
  So the lexicographic Bellman equation has spurious fixed points. That is the γ → 1 symptom: there is no discount to make the
  fixed point unique.
- Reading: no "combinatorial discount" built from VJ valuations can play the role of γ for TWO players. The obstacle is not N5's;
  it is Lemma 4.8.
  - HMZ §7 states Friedmann's exponential bound for SI when γ is part of the input.
  - Scherrer §2 states that the 1/(1−γ) factor cannot be removed for Howard's PI.
  - Both agree with this.

### 3.2 Discounting explicitly does not help
Making γ explicit (parity → mean-payoff → discounted, with 1 − γ inverse-exponential in the priorities) turns HMZ Theorem 6.5's
O((m/(1−γ)) log(n/(1−γ))) into an exponential bound. READING. The reduction's exact constants were not opened, so this line is
not used anywhere.

### 3.3 What does transfer: one player, horizon = combinatorial discount
- Scherrer Thm 6/7 and Post-Ye remove γ for ONE player through transient time (τ_t ≤ 1 for deterministic MDPs) and through
  cycle-creation epochs (Post-Ye Lemmas 3.4, 3.5).
- The parity analogue is RESULTS R17: one-player, in-phase N5 is Bellman-Ford. Lemma P says that after k steps every vertex
  dominates every simple path of ≤ k edges. That is Howard ≥ VI with a horizon that closes after n − 1 rounds.
- Two players break both halves:
  - Friedmann's sink games have every honest play reach the sink (τ_t ≤ n), yet switch-all is exponential (Corollary D1).
  - So Scherrer's transient-time bound does not extend to 2TBSG with best responses.

### 3.3b The Post-Ye reading (L-LIT T28 rank 2, relayed by the Lead 13:42Z)
- Post-Ye prove "Either the algorithm finishes or a new cycle is created after O(n²m log n) iterations" (Lemma 3.4). They also
  prove that O(n log n) new cycles force an action out (Lemma 3.6, as L-LIT quotes it). Both are for ONE LP and highest-gain
  pivots, deterministic MDPs, any discount.
- L-LIT's first step asks for a parametrised LP(t) whose improving set at t = θ is N5's gate. On 𝒞^1O under (h), box 21's
  Lemma G already gives it:
  - LP(t) := the one-player game G^t, in which o is a terminal of value t. Under Jurdziński's reduction it is a deterministic
    MDP.
  - The honest gate is LP(θ)'s improving set, and the selection is LP(w)'s optimum over that set (box 25 §5 (1)).
- In OR terms, an N5 stretch is a pricing / selection split with STALE prices:
  - columns are priced by LP(θ);
  - the restricted master is solved to optimality in LP(w), with w ⊵ θ.
- Post-Ye's Lemma 3.4 analogue for a single LP is R17. Two-LP pricing breaks it at exactly two places, the two exception
  types of Lemma G (d):
  - withheld entering edges (d1);
  - refused leaving edges at trust-routed vertices (d2 in the gate, rejected by LP(w)), as in §3.4.
- Post-Ye's Lemma 3.6 analogue is (CYC-ELIM) in §4.3: DATA, not proved.
- Akian-Gaubert (arXiv 1310.4953, Thm 5; L-LIT's γ-free hook) was NOT opened by me and is not used here.

### 3.4 N5 does not satisfy Howard ≥ VI; the exact failing step (DATA, vi.py)
Lemma D's inequality, checked at every in-phase transition:

| run | checks | violations |
| --- | --- | --- |
| switch-all, switchallexp N 3 | 3,360 | 0 |
| switch-all, switchallexp N 4 | 9,300 | 0 |
| switch-all, switchallexp N 5 | 23,560 | 0 |
| N5, fts_best16 | 390 | 51 |
| N5, i3hn | 24 | 4 |
| N5, thetare_min | 56 | 1 |

The smallest clean case is box 22's hand-built deadlock, i4_hand (n 12, with start file):
- Vertex z = 9 has σ_k(z) = o = 3 at states 0, 1, 2.
- Ξ_k(z) = (s, P = {ranks 11, 3, 2, 1}, 4), key (0, −2054, −4).
- T(Ξ_k)(z) = z ⊕ Ξ_k(y) through y = 8 has key (0, −508, −2), which is strictly better.
- Ξ_{k+1}(z) = Ξ_k(z), because N5's selection keeps z on o: against τ, π_z ⊕ w beats z → y.
- This is box 22 §1.4's trust mode, seen as a failure of HMZ Lemma 5.3. N5 is not even as fast as value iteration, and value
  iteration is itself slow (§3.1).

## 4. What N5 does instead: elimination without contraction (DATA)
### 4.1 HMZ's mechanism ("the max-slack action of σ_k is gone within L steps") is not what happens
hmzL.py measures, for each state k of a phase, L_k = min over edges a of σ_k of (last use of a in the phase) − k (HMZ Lemma
6.4's L). It also measures the same with a restricted to σ_k's max-slack edges (HMZ's argmax c^{π*}).

| run | n | phase | L_max, any edge | L_max, max-slack edges |
| --- | --- | --- | --- | --- |
| N5, fts_best16 | 16 | 26 | 8 | 10 |
| N5, fts_best24 | 24 | 42 | 18 | 27 |
| N5, fts_g29 (start file) | 29 | 65 | 13 | 22 |
| N5, theta_thc24 | 24 | 17 | 0 | 8 |
| N5, returns_rt48 | 48 | 78 | 29 | 77 |
| N5, thetare_min | 15 | 4 | 0 | 1 |
| switch-all, switchallexp N 3 / 4 / 5 | 49 / 63 / 77 | 70 / 150 / 310 | 14 / 34 / 74 | 16 / 36 / 76 |

- On returns_rt48 some state's max-slack edges survive 77 of the phase's 78 transitions.
- Consistently, the largest gap level stays constant for almost the whole phase. gaps.py's "gmaxrun" is 77 of 78 (rt48) and 102
  of 103 (ph64).
- So E3 (gap below slack) is not what drives N5's eliminations.

### 4.2 N5 eliminates SOME action almost every transition
elim.py calls a transition ELIMINATING if some Even vertex leaves an edge at it and that edge is never used again in the phase.
For each run's longest joint λ-phase:

| instance (dir) | n | iterations | phase transitions | eliminating | longest non-eliminating run | Even edges used |
| --- | --- | --- | --- | --- | --- | --- |
| fts_best16 (new/box21) | 16 | 28 | 26 | 19 | 5 | 34 |
| fts_ph16 + start (new/box21) | 16 | 22 | 22 | 16 | 2 | 31 |
| fts_best24 (new/box21) | 24 | 43 | 42 | 31 | 3 | 58 |
| fts_g29 + start (new/box21) | 29 | 66 | 65 | 39 | 7 | 71 |
| fts_g43 + start (new/box21) | 43 | 121 | 120 | 51 | 10 | 110 |
| oneodd_c24 (new/box21) | 24 | 44 | 14 | 14 | 0 | 39 |
| i4_hand + start (new/box22) | 12 | 5 | 5 | 5 | 0 | 16 |
| thetare_min (new/box25, l-new 0d6a93c, sha1 753f5c04…) | 15 | 7 | 4 | 4 | 0 | 19 |
| thetare_n (new/box25, sha1 64698459…) | 11 | 7 | 4 | 4 | 0 | 15 |
| returns_rt32 (red/n5inj) | 32 | 57 | 53 | 31 | 17 | 61 |
| returns_rt48 (red/n5inj) | 48 | 80 | 78 | 42 | 11 | 95 |
| returns_rt64 (red/n5inj) | 64 | 90 | 88 | 47 | 12 | 112 |
| returns_ph64 (red/n5inj) | 64 | 105 | 103 | 49 | 15 | 115 |
| theta_thf16 / theta_thc24 / theta_tp40 (red/n5inj) | 16 / 24 / 40 | 20 / 29 / 41 | 18 / 17 / 20 | 13 / 17 / 20 | 3 / 0 / 0 | 28 / 40 / 57 |
| frz24 / frz40 + start (red/n5inj) | 24 / 40 | 39 / 90 | 10 / 35 | 10 / 18 | 0 / 7 | 33 / 63 |
| block_bk32, phase2_pk48, wide_h16 (red/n5inj) | 36 / 48 / 32 | 49 / 72 / 44 | 21 / 49 / 22 | 21 / 29 / 15 | 0 / 8 / 2 | 57 / 77 / 31 |
| tr20_s4, wd16_s2 (new/box25/instances) | 20 / 16 | 17 / 19 | 17 / 12 | 17 / 12 | 0 / 0 | 37 / 26 |
| CONTROL switch-all, switchallexp N 4 / 5 / 6 / 7 | 63 / 77 / 91 / 105 | 150 / 310 / 630 / 1243 | same (one phase) | 47 / 60 / 73 / 86 | 24 / 62 / 140 / 298 | 116 / 144 / 172 / 200 |

- Every N5 phase is at most about twice the number of Even edges it uses, and the non-eliminating runs stay below n.
- Under switch-all the eliminating transitions grow linearly in N (bounded by the edges), and the non-eliminating runs double.
- Returns do happen: an abandoned edge can come back. returns.py: on fts_g43, 71 returns are to T-tight edges and 67 to edges
  with positive slack. So "abandoned ⇒ eliminated" is FALSE. The phase stays short only because other edges are eliminated in
  between.
- Climb (climb.py: fitness = the longest non-eliminating run in one phase; one Odd choice vertex, o-cyclic allowed; mutations
  and generator are L-NEW's box25/box21 code, read-only): see §6.

### 4.3 The brief's targets: θ-changes (CYC) and trust events (TRUST)
theta.py: for the phase with the most θ-changes, the count, how many of them lower g(o), and how often σ̄(o) changes exit.

| instance | n | phase | θ-changes | of which g(o) drops | σ̄(o) changes |
| --- | --- | --- | --- | --- | --- |
| fts_best16 | 16 | 26 | 8 | 3 | 8 |
| theta_thf16 | 16 | 18 | 13 | 4 | 10 |
| theta_thc24 | 24 | 17 | 16 | 2 | 9 |
| theta_tp40 | 40 | 17 | 16 | 2 | 9 |
| returns_rt48 / returns_ph64 | 48 / 64 | 78 / 103 | 3 / 3 | 1 / 1 | 1 / 1 |
| thetare_min | 15 | 4 | 2 | 1 | 1 |

- θ-changes are mostly flat in gap level. E1-E6 count at most n + 1 of them per phase. The rest happen below g(o)'s level, where
  no slack argument reaches.
- E4 shows that σ̄(o) revisits only exits whose gap is at least their Odd-slack. It gives no count.
- So the gap-level potential gives no bound on (CYC) or (TRUST).
- Trust events were not measured separately. L-NEW's trustcount.py covers them (box 25 §6).

**θ-changes against eliminations, the Post-Ye Lemma 3.6 shape (DATA, thetaelim.py).**
L-LIT T28 rank 2 (iii)(b) asks whether every O(n log n) θ-changes retire a gate edge for the rest of the phase. Measured: the
largest number of θ-changes inside one window of consecutive non-eliminating transitions (σ- or τ-eliminations).

| instance | n | θ-changes in the phase | max θ-changes in a non-eliminating window |
| --- | --- | --- | --- |
| fts_best16 | 16 | 8 | 1 |
| theta_thf16 | 16 | 13 | 3 |
| theta_thc24 / theta_tp40 | 24 / 40 | 16 / 16 | 0 / 0 |
| returns_rt48 / returns_ph64 | 48 / 64 | 3 / 3 | 0 / 0 |
| oneodd_c24, thetare_min, thetare_n, lap_n6, tr20_s4 | 24, 15, 11, 6, 20 | 1, 2, 2, 2, 0 | 0 |

**CONJECTURE (CYC-ELIM).** On 𝒞^1O, every window of consecutive non-eliminating transitions inside a joint λ-phase contains at
most d θ-changes, where d is o's out-degree. The data give at most 3, with d = 5 on theta_thf16.
- PROVED (elementary): (CYC-ELIM) implies θ-changes ≤ (d + 1)·(m + 1) per joint λ-phase, which is (CYC) of box 24 §4.
  - At most m eliminating transitions per phase, each changing θ at most once.
  - At most d θ-changes between consecutive eliminating transitions.
- Mechanism of the 3-θ-change window (theta_thf16, states 2-5):
  - σ̄(o) walks the exits 15 → 1 → 4 → 2, then walks them again 2 → 4 → 1 → 15 → 1 → 4 → 2 at states 8-15.
  - The ring vertices repeat the same switches on the second lap; e.g. 15 takes 5 → 14 at state 3 and again at state 13.
  - So the first lap is non-eliminating and the last lap retires the edges.
- The constant was first stated as 3 (14:04Z message). d is the honest scale: a window can hold one lap of the ring, and a ring
  is at most o's exits.
- Kill design for L-RED (READING): one ring lapped ≥ 3 times with identical switches and no retirement elsewhere. The middle lap's
  window then holds about d θ-changes, and more laps give more. Box 25 §4's lap counts (fts_best16: 4 σ̄-returns, two full laps)
  are the nearest data.
- (CYC-ELIM) is weaker than (ELIM-n). It is aimed at the brief's target. Climb: §6.

### 4.4 Why N5's windows end, and two refinements that fail or do not separate (DATA)
**Mechanism of the long windows** (elim.py traces):
- returns_rt32, window 17 (states 3-19):
  - Chain reversal at states 8-16: a chain of nine vertices, 17 → 5, 9 → 17, 22 → 9, …, 0 → 25. One vertex switches per
    iteration, and each switch points at the vertex that switched before it.
  - At states 45-55 the same chain sweeps back: each vertex returns to its old edge (17: 9 → 5 → 9).
  - The first sweep is non-eliminating because the second one undoes it.
  - The window starts after a fallback (state 7) and ends after another fallback (state 19). Its elimination comes at state 20.
- returns_rt48: hub vertex 46 (successors 18, 37, 40) switches 14 times in the phase, cycling over all three edges. Eliminations
  are sparse in the first half of the phase (7 in 40 transitions) and dense at its end.
- So a kill of (ELIM-n) needs one lane swept back and forth ≥ 3 times, or a hub cycled, while nothing else retires an edge.
  READING: this is a target for L-RED.

**Refinement 1: "every return is paid by a gap drop" is FALSE** (retpay.py).
A return of x to z (x leaves z at k and uses it again at j) need not see g(z) or g(x) drop in [k, j].

| run | returns | paid by a drop of g(z) or g(x) |
| --- | --- | --- |
| N5, returns_rt48 | 83 | 10 |
| N5, fts_g29 | 57 | 32 |
| N5, fts_best16 | 11 | 10 |
| switch-all, switchallexp N 3 | 377 | 146 |

The unpaid returns all sit at the top level (g = n). The top-ranked vertex's membership in the path sets differs from T for
almost the whole phase, so g is blind below it.

**Refinement 2: recursive gap depth** (depth.py).
- Definition. Split a phase at its non-flat transitions. Re-target each maximal flat run at its own last state, and recurse. D is
  the recursion depth.
- PROVED (elementary, from E6, which holds for any in-phase target Ξ_b): a phase with depth D has < (n(n+1)+1)^D
  value-changing transitions.
  - At every level there are ≤ n(n+1) non-flat transitions, so ≤ n(n+1)+1 flat runs.
  - Every interval with a value change has a non-flat transition against its own end: its last value change.
  - Value-flat transitions (Ξ unchanged) are not counted.
- DATA, N5: depth ≤ 3 on all 22 named and pinned instances run.
  - n ≤ 64: returns_ph64 3, returns_rt64 3, fts_g43 3, returns_rt48 3, frz40 3, phase2_pk48 3, fts_g29 3.
  - Every other instance has depth 1-2.
- DATA, switch-all on switchallexp N 3 / 4 / 5 / 6: depth 4 / 5 / 5 / 6.
- READING: depth grows roughly like log(phase length) under BOTH rules (switch-all: 70 → 4, 630 → 6; N5: 26 → 2, 103 → 3).
  So "depth ≤ c" separates the rules only weakly on this data, and it is not stated as a conjecture. It is the closest
  lexicographic analogue of HMZ's "number of scales" log_{1/γ}(n²/(1−γ)): each recursion level is one scale, and the
  contraction that would bound the levels is what §3 shows to be missing.

### 4.5 Lead checks of 14:23Z (pieces.py; trunk 4332f9f texts: docs/new/N5-reentry-box26.md §7.2, docs/new/P-N5-RE-box26.md §5, docs/lit/T30-elimination.md)
**Check 1: does Lemma PIECE give an eliminating transition within ≤ n − 2 steps?**
- A piece (P-N5-RE §5) is a maximal run of transitions in one joint λ-phase with:
  - τ, θ, w constant;
  - (h) at every state;
  - no S4c fallback;
  - R constant.
- **In the PIECE sense: PROVED (L-SI), but vacuous.** If a piece's last transition switches any edge (a value-changing transition
  does), that edge is absent from the piece's last state. So every piece with a value change contains a piece-eliminating
  transition, and PIECE bounds a piece by n − 2 value-changing transitions. Neither fact says anything about the rest of the
  phase.
- **In the PHASE sense (this file's definition): FALSE.** Pieces with value changes and NO phase-eliminating transition, i.e. every
  edge abandoned inside the piece is used again later in the phase:
  - fts_best16: piece = transition 7 → 8. Vertex 3 leaves edge (3, 7) for 13 and re-adopts (3, 7) at state 11, inside the same
    joint λ-phase (states 2-28). No fallback at 7.
  - theta_tp32 (red/n5inj): piece states 9-19, 10 value-changing transitions, none phase-eliminating.
  - returns_rt48: 4 of 14 pieces. returns_ph64: 4 of 16 pieces.
  - 0 violations of the piece-sense statement on 22 runs.
- Windows span several pieces and crossings: returns_rt48 has a non-eliminating window of 11 while its longest piece is 6;
  returns_ph64 has 15 against 9.
- So "(ELIM-n) ⇐ (XING) + (CYC) + (FB-1O)" does NOT follow from PIECE: a crossing can re-adopt an edge abandoned in an earlier
  piece. The implication is OPEN.
- (XING) + (CYC) + (FB-1O) + (d) bound the phase directly by L-NEW's §7.4 reduction, which does not need (ELIM-n).

**Check 2: L-LIT T30's (ELIM-CANCEL).**
- Tagged event (pieces.py): at transition k → k+1, all of the following hold:
  - some Even x switches to z';
  - the play from o under (σ_{k+1}, σ̄_k) returns to o through x, i.e. a mixed cycle closed by the Even switch;
  - σ̄(o) changes.
- HIT if the closing edge (x, z') is never re-adopted after it is first abandoned in the phase, or if o's old exit σ̄_k(o) is
  never used by σ̄ again in the phase.
- DATA: 28 cancellations on 22 one-Odd-choice runs, 28 hits, and BOTH parts hit every time.
  - fts_best16 4, theta_thf16 4, theta_tp32 6, thclimb_n16 8;
  - returns_rt48 1, returns_ph64 1, thetare_min 1, thetare_n 1, oneodd_c24 1, thclimb_n12 1;
  - 0 on the other 12 runs.
- CONJECTURE (ELIM-CANCEL) is not contradicted. The sample is small. Cancellations are rare outside the θ-lap instances.

**(CYC-ELIM) is tight on theta_tp32.** Its non-eliminating window holds 5 θ-changes, and o's out-degree is d = 5. On theta_tp40,
d = 4 and the window holds 0.

## 5. The open statement, and what it would give
**CONJECTURE (ELIM-n).** In every joint λ-phase of an N5 run, among any n consecutive transitions at least one is eliminating:
some vertex leaves an edge of σ (Even) or τ (Odd) that it does not use again in that phase.
- Counting τ as well matters only on games where Odd moves inside phases. The σ-only and σ-or-τ windows (elim.py columns
  noelimrun and noelimrun_st) are equal on every instance checked except wide_h16 (two Odd choice vertices), where they are
  2 and 0.
- DATA: §4.2 (max 17 at n 32, 15 at n 64) and §6.
- Not stated for fallback-free phases only. Fallbacks are included in every count above.

**Proposition (PROVED, L-SI; elementary).** (ELIM-n) implies that N5 makes < (2n(n−1)+1)·n·(m_E + 1) iterations, where m_E is the
number of Even edges.
Here m_E is replaced by m, the number of edges, when τ-eliminations are counted.
Proof:
- In one phase, the eliminating transitions are at most m (resp. m_E), because each one retires a distinct (phase, edge) pair.
- Between consecutive eliminating transitions there are at most n − 1 others. So a phase has ≤ n·(m_E + 1) − 1 transitions.
- Lemma Φ (box 21 §2.3) gives at most 2n(n−1)+1 joint λ-phases. □
So (ELIM-n) implies G-N5-TIME (gauntlet step 4, running time). It does NOT imply correctness, which is R15.

**Why this is not just "N5 is polynomial" restated (READING).**
- It is a local, checkable statement: one window of n transitions in one phase.
- It separates N5 from switch-all on Friedmann's family (§4.2 control).
- The natural proof would be an N5-specific replacement for HMZ Lemma 6.4. The candidate fact: N5's selection is a full
  one-player OPTIMUM against τ over the gate, so a vertex that keeps oscillating must pay with a retirement elsewhere.
- I have no argument for that. The obstacles are exactly the failures in §4.1 (the retired edge is not the max-slack one) and the
  returns in §4.2 (abandoned ≠ retired). (ELIM-n) is OPEN.

## 6. Climbs (DATA; climb.py; canonical start; one Odd choice vertex, o-cyclic allowed; L-NEW's generator and mutations, read-only)
**ELIM climbs.** First round, 13:39Z, with σ-ONLY eliminations (the definition sent to the Lead at 13:51Z):

| n | seed | best (window, phase) |
| --- | --- | --- |
| 12 | 1 | (5, 7) |
| 16 | 2 | (7, 9) |
| 20 | 3 | (5, 11) |
| 24 | 4 | (9, 12) |

- These bests exploit transitions at which only τ moves. On elimclimb_n24 and elimclimb_n16 the σ-or-τ window is 0.
- This is why §5 counts τ-edges. The 13:51Z climb figures are withdrawn.

Second round, 13:59Z, σ-or-τ eliminations, 1,800 s each:
- n 20, seed 21: (0, 11), with no non-eliminating window at all.
- n 24, seed 22: **(12, 52)**.
  - instances/elim24_p52.pg (n 24, m 80, sha1 51f0c964…, from out/elimst_n24_s22.pg).
  - n5.py n5: 59 iterations, 4 fallbacks, matching ortrace and gaps.py's assert. Oink zlk OK, strategies verified (check_sol2.py, Oink 8fbf0a7 built in this
    container). Lane phase counts are transitions; the Lead's phases.py may differ by 1.
  - Its longest joint λ-phase has 52 transitions. That is 2.2n, above the 1.6n envelope of N5-STANDDOWN's table for o-cyclic
    𝒞^1O (returns_ph64 104 at n 64).
  - Its window is 12 ≤ n, so (ELIM-n) holds.
  - 23 eliminating transitions; 46 edges used.
  - θ-changes in the window ≤ 1 (o's out-degree d = 8; CYC-ELIM holds).
  - Recursive depth 2; 6 pieces, longest 13; 1 cancellation (a hit).
  - Note for L-RED and L-NEW: a phase of 52 at n 24 from a 30-minute climb, at a fitness that did not ask for long phases.

**θ-window climbs** (fitness = θ-changes in a non-eliminating window, then θ-changes in that phase), 1,800 s each:
- n 12, seed 11: (4, 12), with d = 7. instances/thclimb_n12_s11.pg; Oink zlk OK, strategies verified.
- n 16, seed 12: (4, 16), with d = 10. instances/thclimb_n16_s12.pg; Oink zlk OK, strategies verified.
- Both stay ≤ d, so (CYC-ELIM) holds.

## 7. Files (experiments/si/orlens/; read-only use of experiments/new/n5.py, experiments/si/si.py, new/box21, new/box25)
- ortrace.py: N5 loop with states (asserts equality with n5.run), plus switch-all control mode; Lex (lev, ⊕).
- gaps.py: E1-E4 checks, flat transitions, gap-max runs, returns.
- batch.py: gaps.py over a list.
- elim.py: eliminating transitions.
- hmzL.py: HMZ Lemma 6.4's L.
- returns.py: tight / slack returns.
- theta.py: θ-changes and g(o).
- stretchret.py: returns inside (θ, w, τ, λ)-stretches.
- vi.py: Lemma D check and value iteration.
- climb.py: §6.
- instances/ (tracked): elim24_p52.pg, thclimb_n12_s11.pg, thclimb_n16_s12.pg.
- pieces.py (§4.5), thetaelim.py (§4.3), depth.py (§4.4), retpay.py (§4.4), sweep.py (random games).
- out/: thetare_min.pg and thetare_n.pg (copied from l-new 0d6a93c, sha1 above), and the switchallexp_N4..7 instances from
  experiments/hard-families/pgsolver_port.py. The out/ files are not tracked except where named.
- Reproduce (from experiments/): `python3 si/orlens/elim.py new/box21/instances/fts_best16.pg`;
  `python3 si/orlens/vi.py --switchall si/instances/switchallexp_N3.pg`;
  `python3 si/orlens/batch.py red/n5inj/instances/returns_rt48.pg`.
