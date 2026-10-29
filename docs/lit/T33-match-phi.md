# T33: Lemma MATCH-Φ, self-contained; and the ARV counter transfer question (L-LIT, 2026-10-29)

Asked by the Lead at 10:23Z (date -u), after T32 (docs/lit/T32-n5-frontier-crossfield.md §5-§6), under owner ruling D18:
> Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and
> computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed
> without asking me questions. Clearly distinguish proven results from conjectures and open problems.

- **Labels.** PROVED (L-LIT, unrefereed): proved here, elementary, no referee yet. PROVED (source): a theorem of an opened source.
  CONJECTURE / OPEN / READING as in D18 / L40. Nothing here bounds N5's running time; G-N5-TIME stays OPEN.
- **Not a frozen packet.** This note may still change.
- **Check script.** docs/lit/T33-match-phi-check.py, sha1 6853179bf10bdf1c3d9cae61c939b1054aa4b70c, run as
  `python3 -I docs/lit/T33-match-phi-check.py`. Output at this commit:
  - Part A: "improving pairs 80640 | matched with phi rise < 1: 0 | carries: 32534".
  - Part B: k = 1..8 "strict-rise=True fixed-top=True", carries(NM) = 0, 0, 1, 3, 7, 15, 31, 63 for 1, 3, 7, …, 255 P-changes.

## 1. Lemma MATCH-Φ

### 1.1 Symbols (from SPEC S1, docs/new/N5-ssi-global.md, and RESULTS R84)
- G = (V, E, Ω, owner), V = {0, …, n − 1}. rank(u) := the position of u in V sorted by (Ω(u), u) (SPEC S1); ranks are distinct.
  A rank r is EVEN or ODD as Ω of the vertex of rank r (R84 F5; not the parity of the number r).
- Ξ_t(v) = (c, P, ℓ): v's S1 valuation at state t, under (σ_t, σ̄_t), σ̄_t Odd's optimal counterstrategy (S1).
  - c: the most relevant vertex of the cycle the play from v ends in.
  - P = P(Ξ_t v): the vertices on the play before c with p′ > p′(c), read as a set of ranks.
  - ℓ: the number of steps to reach c.
- Signed weight (S1): weight(A) := Σ_{r ∈ A} s(r)·2^r, s(r) = +1 for even r and −1 for odd r. S1 orders valuations by the reward of c,
  then weight(P), then ℓ.
- Fact DELTA (R84 (a), signed by both referees; also SPEC Q1). For sets A ≠ B of ranks, weight(B) > weight(A) iff d := the largest rank
  of A Δ B is even and d ∈ B ∖ A, or d is odd and d ∈ A ∖ B.
- Phase (R84's setting; RESULTS R38 (a) KEY): a maximal run of states with λ (Ξ's cycle-node map) and τ constant.
- Fix a vertex v and a phase 𝒫; c := λ(v), constant on 𝒫. P_t := P(Ξ_t v) ⊆ R_c := {rank(u) : rank(u) > rank(c)}.
  K := |R_c| ≤ n − 1; r_1 < … < r_K the elements of R_c.
  - P-change of v in 𝒫: a transition t → t + 1 of 𝒫 with P_t ≠ P_{t+1}.
  - PCH_𝒫(v): the number of P-changes of v in 𝒫.
- From R84's proof of TOP-SHAPE ((MON) = RESULTS R15 (a), (d); c fixed; (INJ)): at every P-change of v in 𝒫,
  weight(P_{t+1}) > weight(P_t).
- New here.
  - pos(r_k) := k.
  - w(r) := +pos(r) for even r, −pos(r) for odd r.
  - Φ(A) := Σ_{r ∈ A} w(r) for A ⊆ R_c.

### 1.2 Definition (MATCHED, CARRY)
A P-change A := P_t → B := P_{t+1} is **MATCHED** if there is a matching M ⊆ (A ∖ B) × (B ∖ A) (each rank in at most one pair) such that:
- (M1) w(i) > w(o) for every pair (o, i) ∈ M;
- (M2) every incoming rank i ∈ B ∖ A not covered by M is even;
- (M3) every outgoing rank o ∈ A ∖ B not covered by M is odd.

Otherwise it is a **CARRY**. NM_𝒫(v) := the number of carries of v in 𝒫. Deciding MATCHED is a bipartite matching problem
(covering the even outgoing and the odd incoming ranks), polynomial per P-change.

### 1.3 Fact 1 (PROVED, L-LIT, unrefereed): MATCHED means "decomposes into individually improving moves"
For distinct ranks o, i: w(i) > w(o) iff weight({i}) > weight({o}), i.e. iff the one-for-one exchange o → i improves on its own.
Adding an even rank, or removing an odd rank, improves on its own.

Proof. By Fact DELTA on the pair {o} vs {i}, d = max(o, i).
- If i > o, the exchange improves iff i is even.
  - i even: w(i) = pos(i) > pos(o) ≥ |w(o)| ≥ w(o).
  - i odd: w(i) = −pos(i) < −pos(o) ≤ w(o).
- If o > i, the exchange improves iff o is odd.
  - o odd: w(o) = −pos(o) < −pos(i) ≤ w(i).
  - o even: w(o) = pos(o) > pos(i) ≥ w(i).
- Adding an even rank: Fact DELTA with d = that rank ∈ B ∖ A.
- Removing an odd rank: d = that rank ∈ A ∖ B. □

### 1.4 Lemma MATCH-Φ (PROVED, L-LIT, unrefereed)
At every MATCHED P-change A → B, Φ(B) − Φ(A) ≥ 1.

Proof. Φ(B) − Φ(A) = Σ_{i ∈ B∖A} w(i) − Σ_{o ∈ A∖B} w(o), which regroups as:
- Σ_{(o,i) ∈ M} (w(i) − w(o)): each term is a positive integer by (M1);
- Σ_{i ∈ B∖A uncovered} pos(i): each term ≥ 1, as i is even by (M2);
- Σ_{o ∈ A∖B uncovered} pos(o): each term ≥ 1, since o is odd by (M3), so −w(o) = pos(o).

A ≠ B, so at least one term is present. □

### 1.5 Corollary (PROVED, L-LIT, unrefereed)
For every vertex v and phase 𝒫:
PCH_𝒫(v) ≤ (K(K+1)/2)·(NM_𝒫(v) + 1) + NM_𝒫(v) ≤ (n²/2)·(NM_𝒫(v) + 1) + NM_𝒫(v).

Proof.
- Φ takes values in [−Σ_{odd r} pos(r), Σ_{even r} pos(r)], an interval of width W ≤ Σ_k k = K(K+1)/2.
- A carry changes Φ by at most W in absolute value. Each MATCHED change raises Φ by ≥ 1 (Lemma).
- So the MATCHED changes number at most W·(NM + 1): the total rise is at most W plus the total drop, and the drop is ≤ W·NM.
- Adding the NM carries gives the bound. □

### 1.6 What it uses, and its limits
- **Uses.** Only distinct ranks and the definition of MATCHED. The Lemma does not use (MON). (MON), Fact DELTA and R84 enter only
  through Fact 1's reading that a MATCHED change is an improvement decomposed into improvements.
- **Transfer.** This is Ackermann-Röglin-Vöcking's Lemma 4 / Theorem 3 mechanism (ECCC TR06-067 p.5: rank-replace the delays; a move
  decomposed into non-worsening 1-1 exchanges lowers the rank potential), transferred to signed path sets (T32 §5).
- **Limits.**
  - (i) A REDUCTION, not a bound: NM may be exponential (§2).
  - (ii) It counts P-changes, not ℓ-changes. GRUN §5 (L-SI, PROVED lane) gives XR ≤ PCH + (PCH + 1)(n − 1) for Ξ-changes.
  - (iii) Unrefereed.
  - (iv) The bound is per vertex and per phase. It does not need a fixed top.
- **Self-check.** Part A of the script: every ordered pair (A, B) of subsets of K = 6 ranks with weight(B) > weight(A), for 40
  random parity patterns; 0 MATCHED pairs with Φ rise < 1.

## 2. The ARV transfer question
**Question (Lead).** ARV (TR06-067) build an EXPONENTIAL 1-2-exchange counter for best response. Does N5's structure admit the same
counter for the carries NM of one vertex under a fixed top, or does some hypothesis block it?

**Answer in one line.**
- None of the N5 facts named blocks it. (MON), λ and τ constant on the phase, Fact DELTA and TOP-SHAPE are all satisfied by an
  ascending binary counter of path sets with exponentially many carries (§2.2).
- What does not transfer is ARV's PROOF. Lemma 10 needs a free choice of which player moves, one at a time ("there exists a best
  response sequence"), and N5's step is fixed and simultaneous (§2.1).
- So the question is not settled either way. Reading the question's dichotomy strictly, this is the "not blocked" branch, and §2.3
  sketches a gadget. Being honest about it: the sketch reduces to the problem L-RED has worked on since box 13, a super-polynomial
  N5 run. NM = poly(n) stays OPEN, not a conjecture backed by a blocking fact.

### 2.1 What ARV's counter needs (PROVED, source: ECCC TR06-067, opened 2026-10-29, sha256 d13b2032…)
- **(A1) a 1-2 exchange, Def. 8 (p.7).** For three resources a, b, c and every k there are delays with:
  - d(a) < d(b) + d(c) ⇒ every optimal set contains a and not b, c;
  - d(a) > d(b) + d(c) ⇒ every optimal set contains b and c and not a.
  - Lemma 9 (p.8): every inclusion-free non-matroid strategy space has it.
- **(A2) gadgets with three main configurations, Lemma 10 (p.8-9).** "Every gadget has three main configurations, namely a 0-state, a
  1-state and a reset state." Two moves:
  - "If a gadget G_i is in state 0 and no gadget G_j with j > i is in its reset state, then there exists a best response sequence
    such that gadget G_i first changes to its reset state and after that to state 1" (p.9).
  - "If a gadget G_i is in state 1 and at least one gadget G_j with j > i is in its reset state, then there exists a best response
    sequence in which gadget G_i changes its state to 0" (p.9).
- **(A3) a free schedule: one player at a time, in an order the constructor chooses.**
  - p.10: "allowing the tree players to play their best responses one after another".
  - p.11: "Altogether this shows that the aforementioned sequence of strategy changes which results in counting from 0 to 2^n − 1 is
    a best response sequence."
  - Lemma 10 is an existence statement over sequences. The stronger "every best response sequence is exponential" in ARV comes only
    from tight PLS reductions (p.3; p.11 for 2-threshold games), not from the counter.
- **(A4) coupling through loads.** A player's delay depends on the other players' choices (the bit player returns to r_1^i because the
  load of r_1^i changed, p.10-11); the potential (Rosenthal's) falls but takes exponentially many values (delays α^{k_i}).

### 2.2 The N5 facts against (A1)-(A4): none of the listed facts blocks a counter
- **(A1) is satisfied, in a stronger form.** Fact DELTA: a single rank d outweighs every set of lower ranks (2^d > Σ_{r<d} 2^r). The
  1-k exchange {higher even} versus {several lower even} is exactly ARV's 1-2 exchange, for every k.
- **(A2) and (A4) are compatible with (MON), the fixed λ, τ and TOP-SHAPE.** Part B of the script checks the ascending binary counter
  at the level of path sets:
  - Bits: k even ranks b_1 < … < b_k, plus a fixed even top T.
  - The count x is the path set {T} ∪ {b_i : bit i of x set}.
  - Every successive pair rises strictly in weight (as (MON) requires inside a phase), and the top stays T (TOP-SHAPE holds trivially).
  - NM = 2^{k−2} − 1 carries for k ≥ 2 (k = 8: 63 of 255 P-changes). A carry at bit j ≥ 3 is {T, b_1, …, b_{j−1}} → {T, b_j}.
    Only one outgoing even rank can be matched (to b_j); the others are even and uncovered, so (M3) fails.
- **Realizable by plays.**
  - Graph: v → b_1 or a lane; each b_i → b_{i+1} or a lane; the lanes and the stretch from b_k reach T and then the cycle node c.
  - Lane vertices get p′ < p′(c), so they are not in P (S1: P counts only vertices with p′ > p′(c)).
  - Every set {T} ∪ S is then v's path set for some strategy. This is static realizability only.
- **Recount without copies (READING).** A recount after a carry needs no copies of the low bits if the play from v visits bits in
  ASCENDING rank order (low bits first, then higher set bits, then T). Then each low bit's own valuation is {b_i} ∪ (set bits above
  b_i) ∪ {T}, and it RISES at every carry above it. So (MON) holds at every vertex, not only at v.
  - Had the play visited bits in DESCENDING order, a recount would need fresh copies of the lower counter. The reason: a bit vertex's
    suffix value, once raised by the first count, cannot fall back.
  - The ascending layout is the shape of Friedmann's sink-game counters. There the lowest-level vertex's path set lists the set bits.
- **(A3) is the only hypothesis N5 fails, and it is a hypothesis of ARV's proof, not a fact that excludes counters.**
  - N5's step is deterministic and simultaneous. S4a moves ALL Even vertices to Even's one-player optimum against τ in the arena H
    (keep σ(v) or an improving edge of Iσ_t); S4b does the same for Odd; S4c is the fallback (SPEC S4).
  - ARV's per-bit sequence (0,0) → (0,1) → (1,1) → (1,0) needs the reset player to move BEFORE the bit player, with the tree players
    following one at a time. A joint arena optimum either does all of these in one step or skips the intermediate configuration.
- **Verdict (READING).** Not blocked by any N5 fact; ARV's counter does not transfer as a proof. The open part is sequencing under
  N5's rule. This matches T20's barrier table:
  - N5 is outside switch-all (Friedmann 1106.0778 Thm 6.14) and outside Schewe's switch-best (Thm 8.4): switch-best optimizes against
    Odd's OPTIMAL reply σ̄, N5 against Odd's CURRENT τ.
  - Those are the deterministic, simultaneous-step counters closest to N5.

### 2.3 Gadget sketch for L-RED (a lower-bound route for NM, hence for one phase; CONJECTURE that it can be made to work)
This is not a construction. It lists what a counter for one vertex's carries must do under N5's rule, in ARV's terms, mapped onto
SPEC S1-S4.
1. **Fixed frame for one phase.** One cycle node c (a sink-like Odd-won or Even-won cycle) reached by every play. τ must stay constant
   on the phase, so Odd's choices that matter must not be improvable in G^d during the count (Iτ = ∅, or Odd's improving edges
   irrelevant to the plays from v). Otherwise S4b changes τ and ends the phase.
2. **Bits (ARV's bit player → an Even choice).** For i = 1..k, an Even vertex x_i with two edges: "set" (into b_i, an even vertex of
   rank above c) and "lane" (a vertex with p′ < p′(c)). The plays visit bits in ascending order (§2.2).
   - The counted vertex v: v → x_1, and x_i's lane and b_i both lead on to x_{i+1}; x_k leads to T, then c.
   - Then P(v) = {T} ∪ {b_i : x_i set}.
3. **The carry (ARV's 1-2 exchange).** Setting bit j while resetting bits < j must be ONE improving move in the sense of the arena.
   - Δ = {b_j} in, {b_1, …, b_{j−1}} out.
   - Fact DELTA makes it improving for v whatever the lower bits are, so S4a takes it as soon as the edge x_j → b_j is in Iσ_t.
4. **Sequencing (ARV's reset player; the part (A3) gets for free and N5 does not).** The edge x_j → b_j must become improving (enter
   Iσ_t) only when bits 1..j−1 are all set. Otherwise S4a's joint optimum sets several bits at once and the count collapses.
   - ARV use a reset player and load thresholds; N5 has only valuations.
   - Candidate mechanism: make Ξ(b_j) depend on Odd's best reply σ̄ (the arena uses Iσ, which is computed against σ̄), through an
     Odd vertex o_j next to b_j. o_j's best reply σ̄(o_j) escapes to a low vertex unless all lower bits are set. τ(o_j) is fixed on the
     phase, while σ̄(o_j) is free.
   - This is the τ versus σ̄ gap that T20 records (docs/lit/T20-N5-barriers.md l. 27: switch-best "evaluated against the
     opponent's CURRENT strategy instead of its optimal counterstrategy"), the one structural lever N5 has that switch-best does not.
5. **Reset of the lower bits (ARV's "G_i changes its state to 0").** After the carry, x_1..x_{j−1} must switch back from set to lane
   AND must be improving to set again one at a time.
   - In the ascending layout, the lane of x_i must become strictly better than its set edge once b_j is on the play (b_i's suffix
     now ends in a play through b_j). That requires x_i's set edge and lane edge to lead to different suffixes, so that the carry
     changes their order.
   - This is the step Friedmann's games solve with cycles that Odd leaves. Here it must happen without any cycle node changing (λ is
     fixed in the phase).
6. **Kill criterion for L-RED.** A family with PCH_𝒫(v) ≥ 2^{Ω(k)} for one vertex in one phase of N5 (SPEC mode, two engines), at
   n = O(k^c). Through T32 E4 that is also a super-polynomial N5 run.
   - Expected obstacle (READING): steps 4 and 5 together. The joint arena optimum tends to set every bit whose edge is improving in
     the same step. The fleet's kill searches (L-RED boxes 13 onward; L-SI box 27) have not produced a vertex with exponentially many
     P-changes in one phase.
   - Current data: 71 P-changes in one phase at n = 41 (R84 honest limits).

### 2.4 Status of NM = poly(n)
OPEN. No blocking fact found: the facts the Lead listed are all satisfied by the ascending counter (§2.2, Part B). A proof that NM is
polynomial must therefore use N5's step rule (S4a's joint optimum against τ in the improving arena), in particular how an edge enters
Iσ_t, and not only monotonicity and the order. One-line target, labelled as such:
- CONJECTURE NM-SEQ (OPEN; no data yet; the measurement is routed to L-COMP 7): in one phase, a carry of v at bit j (an incoming even
  rank above ≥ 2 outgoing even ranks) is preceded by a P-change of v that set the outgoing ranks, and S4a never needs more than
  poly(n) such set-then-carry pairs per vertex, because an edge whose target's value is already maximal in its block cannot re-enter
  the arena. This is stated to be measured, not believed. If L-COMP's NM data are small (≤ c·n), NM-SEQ is the lemma to try. If L-RED
  finds a counter, NM-SEQ is dead.

## DONE / FINDINGS / NEEDS
- DONE:
  - docs/lit/T33-match-phi.md (this note);
  - docs/lit/T33-match-phi-check.py (sha1 6853179b…; Part A brute force, Part B counter);
  - notebook rows.
- FINDINGS:
  1. Lemma MATCH-Φ written self-contained from SPEC S1 and R84, with Fact 1 (MATCHED = decomposes into individually improving 1-1
     moves). PROVED (L-LIT, unrefereed). PCH ≤ (n²/2)(NM + 1) + NM per vertex per phase.
  2. ARV transfer: (A1) is satisfied, in a stronger form (Fact DELTA). (A2) and (A4) are compatible with (MON), the fixed λ and τ,
     and TOP-SHAPE: the ascending counter has NM = 2^{k−2} − 1 at fixed top (Part B). Only (A3), ARV's free one-player-at-a-time
     schedule, fails for N5. Not blocked; ARV's proof does not transfer.
  3. A counter for N5 must solve sequencing and reset under S4a's joint optimum against τ (§2.3 steps 4-5). The τ-versus-σ̄ gap is
     the one lever not present in switch-best.
- NEEDS (for the Lead to route; nothing for the owner):
  - (a) L-RED, if the Lead wants a lower-bound attempt: §2.3 as a gadget brief.
  - (b) L-COMP 7's NM measurement (routed) decides between NM-SEQ (proof side) and §2.3 (kill side).
  - (c) A referee read of §1 when (b) is in.
