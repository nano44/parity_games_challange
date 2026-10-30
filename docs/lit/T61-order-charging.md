# T61: the Gimbert-Horn / Auger-Badin de Montjoye-Strozecki order-charging template, step by step, mapped to N5's heads (support for L-NEW 40, box 97: ORDER-DET / NO-REPEAT)
L-LIT successor T59 (Opus 5.5), D18. Lead's brief 2026-10-30 20:01Z (T61). Written 2026-10-30 20:02Z-20:40Z (date -u). Working note,
unrefereed, not a TARGET.md claim. G-N5-TIME stays OPEN. Inputs: T60 §3.3 (l-lit 2b120701); L-SI P-N5-SETTLE (RUN-SETTLE, HEAD-RED;
l-si docs/si/P-N5-SETTLE-line.txt); L-RED R143 (upward heads U_k, events, downward dependence (A); quoted in P-N5-SETTLE §2).
Labels as in T59/T60. Tool: docs/lit/T61-heads-check.py.

## Summary
- Both sources were OPENED. Gimbert-Horn's original is arXiv 0712.1765 (LMCS 5(2:9) 2009), so nothing here is labelled SECONDARY.
- The template has six steps (§2):
  - (S0) the game class;
  - (S1) the distinguished values;
  - (S2) the improving player's step is a function of their ORDER;
  - (S3) the opponent's best reply is a function of the order;
  - (S4) so a best-reply change forces an order change;
  - (S5) closing argument, either (a) NO-REPEAT (orders never recur, ≤ (r+k)!) or (b) a VALUE QUANTUM (each order change raises a
    value by ≥ q^−r, ≤ (r+k)q^r).
- Mapping to N5 (table in §2.7):
  - (S0) transfers with r = 0: a parity game is deterministic, so the distinguished set must be the ABS «A-sinks», i.e. the heads U_k.
  - (S1) needs lemma U-FIX: ABS fixes the arc set A for the whole run, but U_k moves (gate_K64_n581: |U| alternates 4 ↔ 5).
  - (S2) FAILS as stated, because VJ transit is not reward-free. A route's value is P ⊕ Ξ(u), so the head ORDER does not determine Odd's
    or Even's choice. Hand example in §3.
    - The correct datum is the ORDERED-ULTRAMETRIC TYPE of Ξ on U: the order plus, for each pair, the level where the two values first
      differ.
    - Needs lemma TYPE-DET (σ, σ̄ on the transit region are functions of (U, type) after a RUN-SETTLE window). DATA is consistent with
      its Odd half: ORDREP = TYPREP = 0 on 6 runs, with a caveat.
  - (S3)-(S4) transfer given TYPE-DET. They reproduce HEAD-RED: a σ̄-change forces a type change, i.e. a head Ξ-change or a U-change.
    Nothing new.
  - (S5a) NO-REPEAT FAILS, because Even's σ is not a function of the head type. In GH it is: the f-strategy is the improving player's
    whole strategy.
    - DATA: gate_K64_n581 has 5 distinct head orders, 60 returns to an earlier order and 64 σ̄-changing transitions; 34 types and
      31 returns. DEAD as a count.
  - (S5b) FAILS: no polynomial quantum, because Ξ has 2^Θ(n) values per vertex. The quantum form is XI-CH-POLY / HXU itself.
  - The FPT parameter is not small either: max |U_k| = 64 on latew_K8_m32 (n 370), growing with K.
- Pointer for L-NEW 40 (box 97):
  - ORDER-DET as "order only" is false in principle (§3). Replace it by TYPE-DET.
  - NO-REPEAT is false on gate_K64_n581 (§4) for both orders and types.
  - The template can only re-derive HEAD-RED. A bound needs a charge for RETURNS of the head type, which the literature does not
    supply.

## 1. Sources (opened 2026-10-30; scratchpad t60/A; sha256 in notes/L-LIT.md)
- [GH] Gimbert-Horn, «Solving simple stochastic games with few random vertices», arXiv 0712.1765 = LMCS 5(2:9) 2009, pp.1-17 (6245096f…).
  Opened at:
  - p.5 (permutation strategies; «the only meaningful events in a play are the visits to random vertices. Between two visits the players
    only strive to impose which random vertex will be visited next»);
  - §2.1 Def. 2.1 p.6 (deterministic attractor); §2.1-2.2 pp.6-7 (f-regions W_f[i], f-strategies σ_f, τ_f; properties (2.1)-(2.4));
  - Prop. 2.2 p.7;
  - Def. 3.2 (self-consistent: ϕ_f(f_1) ≤ … ≤ ϕ_f(f_k)), Def. 3.3 (live) p.8; Thm 3.1, Thm 3.4 (k! by enumeration), Lemma 3.7;
  - §4.1 p.13 (the naive improvement oscillates; «the naïve algorithm terminates … in the special case of one-player games [Hor08]»);
  - §4.2 + Algorithm 2 p.13-14; Thm 4.1 p.14 («at most |V_R|! improvement steps»);
  - Lemma 4.2; Lemma 4.4 + proof pp.15-16 (val_σf ≤ val_σg; (4.3) val_σf(g_1) ≤ … ≤ val_σf(g_k)).
- [ABS] Auger-Badin de Montjoye-Strozecki, arXiv 2102.04922 (MFCS 2021) (c992c3f4…). Opened at:
  - Prop. 7 p.4 (positional best responses);
  - Def. 10 p.6 (G[A, f], A-sinks, G[A, σ] with f(e) = v_σ(y));
  - Lemma 11, 12 pp.6-7 (absorbing sets and values agree);
  - Lemma 14 (optimal in G[A, σ] ⇒ optimal in G); Prop. 18 (σ′ ≻ σ in G[A, σ] ⇒ σ′ > σ in G); Prop. 21 p.10;
  - Thm 22 p.12 (GSIA correct);
  - Thm 23 p.13 (denominators ≤ q^r, matrix tree theorem, tight); Thm 26 + Def. 27 + Lemma 28 pp.15-16 (≤ n·q^r);
  - Thm 29 + proof pp.16-17 («when the random order changes, the value of some random vertex increases by at least q^−r»);
  - §5.1 p.17 (GHA as an instance); Thm 30 + proof p.18 (Opt-GSIA: «σ′ is consequently an f-strategy in G[A, σ], where f is the
    ordering on V_R ∪ V_A … induced by the value vector … Hence, the order f must be distinct at each step … at most (r + k)!
    iterations … the value in G of at least one vertex in V_R ∪ V_A must improve, by at least q^−r … (r + k)q^r»).

## 2. The template, step by step, and its N5 image
### 2.1 (S0) Game class and hypotheses
- [GH]/[ABS]: simple stochastic games, with Max, Min and random vertices. [ABS] allows rational probabilities p/q (q-SSG) and sinks with
  rational values; [GH] has two sinks ⊗ (0) and ⊚ (1).
- Reachability objective. Positional optimal strategies ([GH] Thm 1.1; [ABS] Prop. 7).
- [GH] assumes «normalised» games (no value-0 trap except ⊗; Prop. 4.3). [ABS] removes the stopping assumption.
- The parameter is r = |V_R|, plus in [ABS] Thm 30 the number k of fixed arcs out of Max/Min vertices.
- N5: a deterministic parity game with VJ valuations, so r = 0. Every distinguished value must come from fixed arcs ([ABS]'s V_A).
  TRANSFERS only in this form: the heads U_k play the A-sinks.

### 2.2 (S1) The distinguished values
- [GH]: the values of the r random vertices, ordered by a permutation f, with ⊗ lowest and ⊚ highest (p.6).
- [ABS] Thm 30: the values on V_R ∪ V_A.
  - V_A are the A-sinks: every fixed arc (x, y) ∈ A is redirected to a sink of value v_σ(y), frozen at the start of the step (Def. 10).
  - Hypothesis used: «the set A of fixed arcs is the same at each step» (p.18).
- N5: Ξ_k on U_k. R143 (A) is the analogue of "values enter only through the sinks": «Ξ_k(y) is a function of σ_k on the Even vertices
  of layers ≤ d, of σ̄_k, and of Ξ_k on U_k».
- NEEDS LEMMA U-FIX, or a charge for U-changes. U_k is not fixed: it is defined from σ̄_k and C, and it moves inside a W-run.
  - DATA: gate_K64_n581, where |U_k| alternates 4 ↔ 5 (the head 572 enters and leaves).
  - A U-change is already a HEAD-RED event (it needs a σ̄-change).

### 2.3 (S2) The improving player's step is a function of the order
- [GH] §2.1-2.2: given f, the f-strategies are nested deterministic attractors (Max) and trap strategies (Min).
  - They are «expressed in terms of deterministic games as they do not depend on what happens once a random vertex is reached» (Prop. 2.2
    proof, p.7).
  - Between random vertices the payoff is reward-free reachability: only WHICH distinguished vertex is reached first matters.
- [ABS] Thm 30 proof: the optimal σ′ of G[A, σ] is an f-strategy for the order induced by its own value vector.
- N5: FAILS as stated, because VJ transit carries a reward.
  - A route from x to head u with path set P has value P ⊕ Ξ(u). Two routes compare by the most relevant vertex of the symmetric
    difference of P₁ ∪ P(Ξ(u₁)) and P₂ ∪ P(Ξ(u₂)) (same cycle node).
  - So the comparison depends on the order of Ξ(u₁), Ξ(u₂), AND on the level where they differ relative to the levels in P₁, P₂.
  - Example in §3.
- Replacement datum: TYP_k, the ORDERED-ULTRAMETRIC TYPE of Ξ_k on U_k. It is the weak order plus, for every pair, the cycle node if they
  differ, else the top rank of the symmetric difference of the path sets, else "length". This is exactly the information a VJ comparison
  of two prefixed routes reads.
- NEEDS LEMMA TYPE-DET (OPEN): after an event-free RUN-SETTLE window (≤ n − 1 transitions, P-N5-SETTLE), σ and σ̄ on the transit region
  are functions of (U_k, TYP_k), together with τ and the game.
  - This is the [GH] f-strategy statement with "order" replaced by "type".
  - DATA for the Odd half (§4): ORDREP = TYPREP = 0 on every measured run.
  - Caveat: U_k is built from σ̄_k's targets, so part of σ̄ is encoded in U_k by definition. This is weak evidence.

### 2.4 (S3) The opponent's best reply from the order
- [ABS] p.17: «knowing this order and σ′, it is easy to compute τ(σ′) a best response to σ′ in O(r log(r) + n) time».
- [GH] Lemma 4.4: Min's g-strategy in G[σ_f] is optimal for g sorted by val_σf ((4.3)).
- N5: TRANSFERS given TYPE-DET's Odd half, with weak orders. L-SI's FLIP-EV gap is a tie re-order, so ties must be part of the type
  (they are: TYP records equal values).

### 2.5 (S4) Best-reply change ⇒ order change
- [ABS] Thm 29 proof (contrapositive of S3): when the order is unchanged, the best reply is recomputed from the order. A change of best
  reply that is not explained by the order triggers the LP case, «In that case, the order of the random vertices has changed».
- N5: TRANSFERS given TYPE-DET. A σ̄-change forces a change of (U, TYP), i.e. a Ξ-change at a head, or a U-change (itself a σ̄-change at
  a deviating Odd vertex).
  - This is HEAD-RED's event (i)/(iii) (P-N5-SETTLE). The template re-derives HEAD-RED and adds nothing beyond it.

### 2.6 (S5) The closing argument
- (S5a) NO-REPEAT.
  - [GH] Thm 4.1 / Lemma 4.4 and [ABS] Thm 30: successive improving strategies strictly increase ([ABS] Prop. 18; [GH] Lemma 4.4).
  - Each is a function of the order (S2, for the IMPROVING player), so orders never recur: ≤ (r + k)! (k! for [GH] Thm 3.4/4.1).
  - N5: FAILS.
    - The improving player is Even. σ_k is NOT a function of the head type: S4a's optimum depends on the arena H_k, i.e. on Iσ_k and so
      on Ξ_k everywhere. And σ moves in the transit region between head events.
    - Ξ strictly improves, so σ_k never repeats, but (U, TYP) can.
    - DATA: gate_K64_n581 has 5 distinct head orders and 60 returns (34 types, 31 returns) in a 71-transition W-run with 64 σ̄-changing
      transitions. Also gate_K16_n197 (12 / 7 returns) and pp_K12_n161 (9 order returns).
    - DEAD as stated: "NO-REPEAT of head orders / types in a W-run" is false on gate_K64_n581.
- (S5b) VALUE QUANTUM.
  - [ABS] Thm 23: under (σ, τ) every value is s_x/t with t ≤ q^r (matrix tree theorem). An order change raises some distinguished value
    by ≥ q^−r, and values lie in [0, 1], so ≤ (r + k)·q^r (Thm 29, 30).
  - N5: FAILS. Ξ is ordinal with 2^Θ(n) distinct values per vertex. In T56's ISO embedding these are integers in a range of size 2^n,
    so the quantum is 1 and the count 2^n.
  - A polynomial quantum statement IS XI-CH-POLY (per-head Ξ-changes, HXU_F).

### 2.7 Table (the brief's mapping)
| step | [GH] / [ABS] (opened) | N5 object | status |
| --- | --- | --- | --- |
| S0 class | SSG, reachability, r random vertices (+ k fixed arcs, [ABS] Thm 30) | deterministic parity game, r = 0; fixed arcs = arcs into heads | transfers (as A-sinks only) |
| S1 values | values on V_R ∪ V_A, A FIXED over the run ([ABS] p.18) | Ξ_k on U_k; R143 (A) | needs lemma U-FIX (U moves: gate_K64_n581) |
| S2 step = f(order) | f-strategies = deterministic attractors / traps, reward-free transit ([GH] §2, Prop. 2.2) | σ, σ̄ on transit after a RUN-SETTLE window | fails for the pure order (VJ transit rewards, §3); needs lemma TYPE-DET (ordered-ultrametric type) |
| S3 BR = f(order) | [ABS] p.17; [GH] Lemma 4.4 (4.3) | σ̄_k from (U_k, TYP_k) | transfers given TYPE-DET (Odd half); DATA consistent (weak) |
| S4 BR change ⇒ order change | [ABS] Thm 29 proof | σ̄-change ⇒ head Ξ-change or U-change | transfers = HEAD-RED (nothing new) |
| S5a no-repeat | strict improvement + step = f(order) ⇒ ≤ (r+k)! ([GH] Thm 4.1, [ABS] Thm 30) | (U, TYP) along F | FAILS: σ is not f(type); DEAD on gate_K64_n581 (5 orders, 60 returns) |
| S5b quantum | denominators ≤ q^r ([ABS] Thm 23) ⇒ ≤ (r+k)q^r | Ξ-changes at heads | FAILS: 2^Θ(n) values; = XI-CH-POLY / HXU |
| parameter | r (+ k) small | max |U_k| | 64 on latew_K8_m32 (n 370); grows with K |

## 3. Why the pure order cannot determine a VJ route choice (elementary example, not an N5 run)
- Same cycle node; priorities as ranks, with even ranks good for Even.
- An Odd vertex o chooses between route 1, with prefix P₁ = {10} (even) into head u₁, and route 2, with empty prefix into head u₂.
- State A: Ξ(u₁) = {8}, Ξ(u₂) = {9}. Then Ξ(u₁) ◁ Ξ(u₂): top of {8} △ {9} is 9, even, in u₂.
  - Route 1 = {10, 8}, route 2 = {9}. The top of the symmetric difference is 10, even, in route 1. Route 1 is better for Even, so Odd
    takes route 2.
- State B: Ξ(u₂) rises to {12} (12 even; {12} ▷ {9}). Ξ(u₁) is unchanged, so the ORDER Ξ(u₁) ◁ Ξ(u₂) is unchanged.
  - Route 1 = {10, 8}, route 2 = {12}. The top is 12, in route 2, so route 2 is better for Even and Odd takes route 1.
- So σ̄(o) changed with the head order and the prefixes fixed. What changed is the LEVEL at which Ξ(u₁) and Ξ(u₂) differ: 9 → 12,
  crossing the prefix level 10. TYP records exactly this; the order does not.
- In [GH] transit is reward-free (P₁ = P₂ = ∅ in effect), so this cannot happen there.

## 4. DATA (docs/lit/T61-heads-check.py; W-runs as T58/T59)
| instance | n | max |F| | UMAX | NORD | NTYP | SBT (σ̄-changing transitions) | ORDREP / TYPREP | ORDRET / TYPRET (returns) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| gate_K64_n581 (red/usplit) | 581 | 71 | 6 | 5 | 34 | 64 | 0 / 0 | 60 / 31 |
| gate_K16_n197 (red/usplit) | 197 | 23 | 6 | 5 | 10 | 16 | 0 / 0 | 12 / 7 |
| pp_K12_n161 | 161 | 19 | 7 | 6 | 15 | 14 | 0 / 0 | 9 / 0 |
| latew_K8_m32 (R2-N5-CUT inst) | 370 | 280 | 64 | 265 | 265 | 257 | 0 / 0 | 0 / 0 |
| fx_K8_m16 (T58 regeneration) | 186 | 152 | 33 | 17 | 17 | 1 | 0 / 0 | 0 / 0 |
| switchbestexp_6 | 160 | 44 | 6 | 3 | 3 | 3 | 0 / 0 | 1 / 1 |

- Two regimes kill the template:
  - On gate / pp the head set is small (≤ 7) but orders RETURN (60 returns at K = 64; the count grows with K). That kills NO-REPEAT.
  - On latew the head set is LARGE (64) and orders do not repeat (265 distinct orders in 280 states). There the FPT parameter is
    useless.
- ORDREP = TYPREP = 0 everywhere: σ̄ was the same at every recurrence of an order. This is consistent with TYPE-DET's Odd half (and
  even with the pure order), but U_k is defined from σ̄_k's targets, so it is weak evidence.
- Not run on the whole corpus (the template is already dead on the pinned instances above). The script is in the repo for L-NEW 40.

## DONE / FINDINGS / NEEDS
- DONE: this note; docs/lit/T61-heads-check.py; notes/L-LIT.md.
- FINDINGS:
  1. [GH] (original, LMCS 5(2:9)) and [ABS] (Thm 23, 26, 29, 30) share one template: distinguished values (random vertices + A-sinks),
     strategies as functions of their ORDER (reward-free transit), best-reply change ⇒ order change, closed by no-repeat ((r+k)!) or a
     value quantum ((r+k)q^r).
  2. For N5: S0, S3 and S4 transfer, and S4 reproduces HEAD-RED. S1 needs U-FIX. S2 fails for the pure order because VJ transit carries
     path sets (§3); it needs TYPE-DET (ordered-ultrametric type).
  3. Both closings fail. NO-REPEAT is DEAD on gate_K64_n581 (5 orders, 60 returns, 64 σ̄-changes), because Even's σ is not a function of
     the head type. The quantum is XI-CH-POLY. The parameter max |U_k| reaches 64 on latew_K8_m32.
  4. Pointer for L-NEW 40: replace ORDER-DET by TYPE-DET. NO-REPEAT must be replaced by a charge for type RETURNS; the literature
     supplies none.
- NEEDS: none from the owner.
