# T37: the known exponential families for strategy improvement / policy iteration, classified as carries or as cycle changes, and how they sequence their carries (L-LIT, 2026-10-29)

Asked by the Lead at 11:34Z (date -u), for L-RED 26: «the exact target is now one count: carries of one vertex's path set inside one joint
λ-run (COMPOSE-RUN)».

Owner ruling D18:
> Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and
> computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed
> without asking me questions. Clearly distinguish proven results from conjectures and open problems.

Labels: PROVED (source); READING; CONJECTURE; OPEN. No runs. Nothing here bounds N5.

**The classification test.**
- CARRY-TYPE: the family counts inside one fixed cycle. Every play reaches the same sink / absorbing state, so the cycle component of
  every valuation (the gain) is constant, and the counter lives in path components / biases. In N5 terms the whole count sits inside
  one λ-run (R47 does not bound it). This is the N5-relevant kind.
- CYCLE-TYPE: the count advances through new cycles with better values (gains, cycle means). Blocked in N5: a parity valuation's
  cycle component has ≤ n values ([F] §5 p.8), and RESULTS R47 Lemma Φ bounds the λ-runs by 2n(n − 1) + 1.
- TIMING-TYPE (discounted only): equal-mean cycles separated by discount timing. No N5 analogue (N5's order is undiscounted and
  lexicographic).

## 0. Answer in short
- **Every known exponential family for strategy improvement on parity games, and every exponential policy-iteration family for MDPs
  with an absorbing sink, is CARRY-TYPE.** They are 1-sink / sink games by design. [F] §5 p.8: "Every approach trying to construct a
  game family of polynomial size that requires super-polynomially many iterations ... needs to focus on the second component of game
  valuations". So the target count NM* is exactly where the literature puts its counters.
- **The only CYCLE-TYPE families are for deterministic MDPs.** These are Zhong-Ye's exponential average-reward family and Hansen-Zwick /
  Asadi-Chatterjee-de Raaij's quadratic ones (T35). Deterministic MDPs have no sink trick: a counter there must create cycles. They do
  not transfer to N5 (R47).
- **All carry-type families sequence their carries with the same three ingredients (§2).** (1) A hidden-profit gate per bit; (2) a
  delay supply that makes the least unset bit close first; (3) a one-step reset triggered by setting a bit.
- **What survives in N5 is the τ-side of ingredient (1), and only inside a λ-run (§3).** The hiding must come from Odd's CURRENT
  strategy τ lagging, because S4a chooses against τ (T34 §3). The σ̄-hiding is void.
  - COMPOSE-RUN counts per λ-run, and a λ-run may contain τ-changes. So a τ-sequenced counter is within the target.
  - P-N5-MPGS (B) GATE-SHUT says a Friedmann-type gate that S4b has shut never reopens while (H1)-(H3) hold. A counter must therefore
    reopen its gates by violating (H1), (H2) or (H3). §3 gives the three ways, with the instance where each was observed or is
    possible.

## 1. The families

| family (source opened; sha256 in notes/L-LIT.md) | rule | setting | type | count, theorem |
| --- | --- | --- | --- | --- |
| Friedmann G_n ([F] = arXiv 1106.0778 v2) | locally optimizing (switch-all / switch-best-per-vertex) | 1-sink parity game ([F] §5, Lemma 6.7 p.17: "x is the 1-sink ... the cycle component ... equals x") | CARRY | ≥ 2^n, Thm 6.14 |
| Friedmann H_n ([F] §8) | globally optimizing (Schewe's switch-best) | 1-sink (Lemma 8.3) | CARRY | ≥ 2^n, Thm 8.4 (p.33) |
| Fearnley (arXiv 1003.3418 v1) | greedy (Howard) PI | MDP, total reward with an absorbing sink c_{n+1}; average reward with gain 0 everywhere ("G^π(s) = 0 for every policy", p.12) | CARRY (bias) | ≥ 2^n, Thm 17 (total), Thm 18 (average) p.12 |
| Disser-Friedmann-Hopp, Zadeh (arXiv 1911.01074 v2) | Zadeh's least-entered (history) | sink games (§2.1 p.4, Definition of a Sink Game: "Ω(v) > Ω(t) for all v ∈ V \ {t}") / weak-unichain MDP / LP | CARRY | exponential, Thm 6.18 (p.31) |
| Avis-Friedmann, Cunningham (arXiv 1305.3944 v1) | round-robin (least recently considered) | sink parity game (p.10 "Sink Existence ... Sink Seeking") / MDP / AUSO | CARRY | exponential, Thm 4 (p.15), Thm 6 |
| Friedmann-Hansen-Zwick, Random-Facet / Random-Edge (errata arXiv 1410.7871 v1) | randomized | sink games | CARRY | the parity Random-Facet bound is "flawed" (errata p.1-3); Random-Facet* and Random-Edge stand (T13) |
| van Dijk-Loho-Maat, symmetric SI (arXiv 2309.02223 v1) | symmetric SI, any improvement rule | sink parity games (Def. 2, p.4: sink ⊤ with "p(⊤) < p(v) for all nodes") | CARRY | Thm 1 (p.2), Thm 13 (p.14); N5 runs them in 1-13 iterations (SPEC, docs/new/N5-ssi-global.md "First test") |
| Disser-Loho-Maat-Mosis, ranking-based rules (arXiv 2512.16684 v2) | index-/ranking-based, memory o(log m) | sink parity games / MDPs | CARRY | superpolynomial, Thm 4.3 (p.13); Thm 5.1, 5.3 |
| Mei, Dantzig SSI on turn-based deterministic games (arXiv 2610.27386 v1; T31) | Dantzig single switch + exact best reply | discounted G_h; mean-payoff Ĝ_h, where only the terminal self-loop is a cycle of completed profiles (T31 l.73) | CARRY (Ĝ_h; T31: "one joint λ-phase") | 2^h − 1, Thm 1, Thm 4 |
| Zhong-Ye average-reward (arXiv 2609.40147 v2) | Howard PI | deterministic MDP, strongly connected | CYCLE ("encoded cycles have strictly increasing mean rewards", eq. (6.8)) | exp(Ω(N)), Thm 6.1 (p.23) |
| Zhong-Ye discounted (same) | Howard PI | deterministic discounted MDP | TIMING ("cycles with the same mean reward have strictly increasing discounted values", p.33) | exp(Ω(N)), Thm 2.1; exp(Ω(N^{1/4})), Thm 2.2 |
| Hansen-Zwick; Asadi-Chatterjee-de Raaij (T35) | Howard PI | deterministic MDP, mean payoff | CYCLE (n cycles found in order) | Ω(n²) only |

**Not opened here** (opened in earlier tasks, cited only for the row): Hollanders et al. 1407.4293 / 1410.7583 (discounted Fearnley-type,
T-earlier), Melekopoglou-Condon (T30 §7, through Fearnley's thesis), Friedmann's thesis.

## 2. How the carry-type families sequence their carries (PROVED in each source; the common pattern is READING)
**Where the carry sits.** [F] §6.5, Lemma 6.11-6.12 (p.21-22): at the bit state b, Ξ(r) = {r} ∪ ⋃{U_j | b_j = 1}, U_j = {g_j, f_j, e_j,
h_j, k_j}. The selectors k_i point to the next set bit (σ(k_i) = min{j > i | b_j = 1}).
- So the path set of the root r (and of every lower selector) LISTS the set bits in ascending order.
- An increment adds U_{μb} (μb the least unset bit) and removes U_j for all j < μb: a carry exactly in the sense of P-N5-MPGS (A), at a
  fixed cycle node x.
- Fearnley's π^B (p.9) is the same: "r_i should use the action (c_i, r_j) where j ∈ B is the smallest bit that is both larger than
  i and a member of B".

**The three ingredients, with each source's implementation.**
1. **A hidden-profit gate per bit.** Setting bit i is an improving switch whose value, in the RULE's metric, is far below its real
   value. So the rule prefers something else until the right moment.
   - [F] §6.1 (p.9-10). Simple cycle d_i ⇄ e_i with Odd e_i. While open, τ_σ(e_i) = d_i (Lemma 6.1 (3)), so "by moving to d_i, the
     player 1 node hides the fact that there is a highly profitable node on the other side". Closing forces Odd out to h_i.
   - [F] §8.2 (I^glo). Stubborn cycles that need three edges, "so that cycles are not closed within one iteration".
   - Fearnley (p.6, Prop. 4). A probabilistic action a_i whose "appeal ... is at most Val^π(b_i) + 1" while unchosen, though g_i's
     value is much larger.
   - Mei (T31 Lemma 2). Each pivot creates a 2-cycle a_i → s → a_i that the exact best reply cancels.
   - DLM (p.3). "The optimal counterstrategy to a bad strategy can also be a bad strategy itself", so the opponent's counterstrategy
     distracts.
2. **A delay supply ordered by bit index.** Every unset bit has a fresh, slightly better alternative in each iteration, and lower
   bits run out first.
   - [F] §6.2 deceleration lane (Lemmas 6.3-6.4: "new best-valued node in each iteration"). §6.4: "lower cycle gates have less edges to
     the deceleration lane. This construction ensures that lower open cycle gates will close before higher open cycle gates".
   - Fearnley §4.2 (p.6): "policy iteration can only switch the state b_i to a_i after every state b_j with j < i has been switched";
     b_i sees lane states up to d_{2i}.
   - DFH Zadeh (§3, p.6): two cycle centers per level, "only one of the cycle centers is interpreted as encoding the bit ... alternating
     and balanced usage of both cycle centers of any level as required by Zadeh's pivot rule". The occurrence records play the role of
     the lane.
   - Avis-Friedmann: the round-robin order.
3. **A one-step reset caused by the set.**
   - [F] Lemma 6.11 (phase 3 → 4). After bit μb closes, the reset root s gets a better value than the default root r: "r ≺_σ a_* ≺_σ
     h_{*<μb} ≺_σ s ≺_σ h_{*≥μb}".
     - Lemma 6.2 (4) then opens every lower closed cycle ("closed cycles with index i < μb open").
     - The lane resets (Lemma 6.4 (1)).
     - The selectors move to the new next set bit.
   - Lemma 6.12 returns to phase 1 of the incremented counter. Fearnley's Propositions 13-16 (p.10-11) are the same four steps.
- **In one paragraph for L-RED.** A bit is a cycle gadget whose closing pays off only through the opponent's forced exit. While the
  bit is unset, the opponent's reply hides that pay-off: the switch looks no better than the lane's next node. A lane, with more lane
  edges for higher bits, gives every unset bit a new marginally better option each iteration, so the least unset bit is the first
  whose options run out. Its cycle closes, the exit pay-off appears, and the selector chain (each selector points to the next set
  bit) carries it into the counted path set. The new set bit lifts the reset root above the exits of all lower bits, which reopens
  their cycles and resets the lane in one step. The counted vertex's path set (the root's, listing the set bits in ascending order)
  has made a carry. Each increment is one carry plus O(lane length) matched changes.

## 3. What survives in N5, and the three ways around GATE-SHUT (READING; for L-RED)
- **Ingredient (1) under N5.**
  - S4a chooses against τ (T34 §3; n5b.py l. 234-241). A gate's profit is hidden from S4a only if τ's play through the gate is low,
    i.e. Odd's CURRENT strategy sits inside the open cycle. σ̄ sitting there does not suffice.
  - The σ̄ channel still decides membership in Iσ (T34 §3, [F] Lemma 6.1 (2) vs (3)).
  - So the hidden-profit gate must be a τ-gate: τ(e) = d (inside) while the bit is unset, then τ(e) = h (exit) when it should pay.
    That move is an S4b step, a τ-change, so a new phase. But COMPOSE-RUN counts per λ-run, and a λ-run may contain any number of
    τ-changes. A τ-sequenced counter is within the target.
- **GATE-SHUT (P-N5-MPGS (B), under review).** Once τ(e) = h with (H1)-(H3), d never enters Iτ(e): the gate cannot reopen. A counter
  needs each lower bit's gate to reopen at every carry above it, so at the reopening one hypothesis must fail.
  - **(H1) fails**: the gate's route vertices rank at or below the cycle node c_h of h's τ-play, so they do not enter P and Odd decides
    by length.
    - This is the only mechanism observed. All 247 h → d1 reopenings on H_n random starts are of this kind (T34-gateshut-check.py; rand4,
      n = 3: c_h = e2, a closed Even-won cycle above gate 1).
    - Inside one λ-run, c_h is fixed per vertex. So the gate must sit below its exit play's cycle node for the whole λ-run, i.e. the
      exit play must end in a high cycle. That cycle is NOT the global sink. This contradicts [F]'s 1-sink layout and needs a game with
      several cycle nodes held fixed.
  - **(H2) fails**: the exit play from h passes back through the gate (π or e). Then the deviation in GATE-SHUT's proof changes h's
    play, and the comparison is open. A self-referential gate: the exit route re-enters the cycle region.
  - **(H3) fails**: the gate's top vertex (on route + e) has ODD priority.
    - Then closing the cycle is Odd-won, so Odd prefers d when Even's best reply closes it. The reopening is "free".
    - Cost (T34 (R2)): the bit's pay-off can no longer come from forcing Odd out of an Even-won cycle. And if Even ever closes the
      cycle under τ(e) = d, the cycle node changes (λ-change, the end of the λ-run).
- **Data point already in the repo.** runquad has I_τ = ∅ at every state (R106 §Summary). Its pivots' W-sinks are gated by W-routes
  through Odd vertices whose τ is fixed (τ(C_i) = MP_i → w_{i−1}). That is a τ-gate that never moves.
  - L-RED 26's plan ("W-gates that reopen through τ changes") is the natural next step.
  - By the above, each reopening must be an (H1)-, (H2)- or (H3)-failure. (H1) inside one λ-run needs a high fixed cycle node above the
    gate. That is the cheapest to test with T34-gateshut-check.py's hypothesis logic on L-RED's own instances.
- **CONJECTURE (OPEN; the proof-side mirror of the above).** In a λ-run, a vertex's carries are at most poly(n) × (the number of
  reopenings of gates on its play that violate (H1), (H2) or (H3)).
  - It would turn NM* into a count of hypothesis failures.
  - Not proved, and no data yet. L-SI's anatomy (N5-CHG-box28 §10: one carry per pivot step) is consistent with it on runquad, where
    there are no reopenings and NM = K comes from the pivot clock instead.

## DONE / FINDINGS / NEEDS
- DONE: this note; 9 sources opened (sha256 in the notebook).
- FINDINGS:
  1. Every exponential SI/PI family for parity games and absorbing-sink MDPs ([F] G_n, H_n; Fearnley; Zadeh DFH; Cunningham AF;
     Random-Edge / Facet*; DLM symmetric; DLMM ranking-based; Mei Ĝ_h) is CARRY-type (1-sink). Only deterministic-MDP families (Zhong-Ye
     Thm 6.1; Hansen-Zwick / ACR) are CYCLE-type, which R47 blocks for N5. Zhong-Ye's discounted families are TIMING-type.
  2. All carry-type families sequence carries by (1) hidden-profit gates, (2) a lane ordered by bit index, (3) a one-step reset. The
     carry sits in the root's ascending selector path set ([F] Lemma 6.11-6.12; Fearnley p.9).
  3. In N5 only a τ-gate can hide profit, which is allowed inside a λ-run (COMPOSE-RUN's unit). GATE-SHUT forces every reopening to
     violate (H1), (H2) or (H3). The observed reopenings are all (H1); (H3) costs a λ-change if the cycle ever closes.
- NEEDS (Lead to route; nothing for the owner): L-RED 26 to classify each gate reopening in its τ-gate designs by which of (H1)-(H3)
  fails (the hypothesis tests are in docs/lit/T34-gateshut-check.py).
