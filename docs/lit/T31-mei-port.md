# T31: construction spec, Mei's G_h / Ĝ_h ported to a parity game (L-LIT, 2026-10-24)

Asked by the Lead at 14:23Z (date -u), for L-RED, who builds in parallel.
- **Scope.** No runs, no contact.
- **Source.** S. Mei, "Simple strategy-iteration with Dantzig's rule is not strongly polynomial on turn-based deterministic games",
  arXiv 2610.27386 v1 (19 Oct 2026), PDF sha256 5b3265d3eb1c5b8a… Pages = PDF pages. p.5 was rendered as an image to read the
  parameters in eq. (3).
- **Labels.**
  - **PROVED-S**: proved here as a sketch by L-LIT, unrefereed, from Mei's lemmas and SPEC S1.
  - **CONJECTURE**: needs a run or a proof.
- **N5.** docs/new/N5-ssi-global.md SPEC S1-S5.

## (i) Mei's games exactly
**Discounted G_h (§3.1, p.5; Table 1).** h ≥ 2.
- **States:** a_i, b_i for 1 ≤ i ≤ h+1; p_i, q_i for 1 ≤ i ≤ h. n = 4h + 2, m = 8h + 2.
- **Owners:** Player 1 (minimises cost) owns a_1..a_{h+1}. Player 2 (maximises) owns all other states.

| state | owner | actions → successor : cost |
| --- | --- | --- |
| a_i (i ≤ h) | P1 | → p_i : 0; → q_i : 0 |
| p_i | P2 | → a_{i+1} : W_i/γ; → a_i : −K_i/γ |
| q_i | P2 | → b_{i+1} : W_i/γ; → a_i : −K_i/γ |
| b_i (i ≤ h) | P2 | → a_{i+1} : 0; → b_{i+1} : 0 |
| a_{h+1} | P1 | → a_{h+1} (self-loop) : 0 |
| b_{h+1} | P2 | → a_{h+1} : −R |

- **Parameters, eq. (3) (p.5):** R = 1; W_i = γ·4^(i−h−1); K_i = γ·2^(2−i−2h); δ = 1/(100·8^(h−2)); γ = 1 − δ.
- **Consequences used, eqs (5)-(7) (p.6):**
  - 8/9 < β ≤ η < 1 with β = γ², η = γ; K_i ≤ 2W_i;
  - W_{i+1} ≥ 4W_i; K_i ≥ 2K_{i+1};
  - R ≥ 4W_h; 3(1−β)R < K_h; 4(η−β)R < W_1.

**Start strategy, eq. (4) (p.6):** σ_0(a_i) = (a_i, p_i) for every i ≤ h; σ_0(a_{h+1}) = self-loop. Player 2 starts at its optimal counter
strategy τ_0 = π²(σ_0) (Algorithm 1, line 1, p.4).

**Two scales (p.5, p.11).**
- **W_i**, on the forward actions, fix the order of state values: they set the sign of ∆_i = v_{a_i} − v_{b_i}.
- **K_i**, on the return actions, fix Dantzig's pivot: the most negative reduced cost is −K_i − (1−β)v_{a_i}, at the smallest level
  with ∆_i > 0.

**Mean-payoff Ĝ_h (§5.1, p.20).**
- Same graph and owners.
- Costs W_i on the forward actions, −K_i on the return actions, −R on b_{h+1} → a_{h+1}, all others 0.
- eq. (35): R = 1, W_i = 4^(i−h−1), K_i = 2^(2−i−2h).
- Algorithm 2 (p.18): Dantzig on (gain, bias) lexicographically; Player 2 lexicographically maximises (gain, bias).
- Thm 4 (p.20): exactly 2^h − 1 iterations from (4).
- **Use Ĝ_h for the parity port.** VJ valuations are undiscounted, and in Ĝ_h every cycle except the self-loop at a_{h+1} has negative
  mean, so all values are finite path sums to a_{h+1}.

## (ii) The iteration pattern Mei proves (§3.2-3.3, p.6-11)
- **Lemma 2 (p.6), cancellation.** For every σ, the best reply takes the FORWARD action at the selected auxiliary state:
  - π(p_i) = (p_i, a_{i+1}) if σ(a_i) = p_i;
  - π(q_i) = (q_i, b_{i+1}) otherwise.
  - Reason: returning would close the cycle a_i → s → a_i, of value −K_i/(1−β) < −3R, which is bad for the maximiser.
- **Lemma 4 (p.8), sign rule.**
  - sgn ∆_i = sgn ∆_{i+1} if σ(a_i) = p_i, and −sgn ∆_{i+1} otherwise;
  - |∆_i| > 3W_i/4;
  - ∆_{h+1} = R > 0 (eq. (8)).
- **Lemma 5 (p.8-9), return at the unselected auxiliary state.** At the unselected s ∈ {p_i, q_i}, Player 2 returns to a_i iff
  ∆_i > 0. The best reply is unique.
- **Lemma 6 (p.9), reduced costs.**
  - r(a_i, s) = −K_i − (1−β)v_{a_i} if ∆_i > 0, and β|∆_{i+1}| if ∆_i < 0.
  - The unique Dantzig pivot is at i = min{j : ∆_j > 0} (eq. (14)).
- **Lemma 7 (p.10), the counter.** C_k := Σ_{j: ∆_j^{π_k} > 0} 2^(j−1) = 2^h − 1 − k.
  - Base: σ_0 has all ∆_j > 0.
  - Step: pivot at the lowest positive level i. It flips ∆_i to negative and, by the sign rule, makes every ∆_j, j < i (all negative
    before), positive.
- **Theorem 1 (p.11):** exactly 2^h − 1 iterations; a unique pivot and a unique best reply at every step.
- **Pattern (p.11).**
  - Pivot k has source level 1 + ν₂(k). Level i pivots 2^(h−i) times, alternating its two actions.
  - Each pivot (a_i, s) CREATES the 2-cycle a_i → s → a_i, because the old best reply had (s, a_i). The new best reply CANCELS it
    (Lemmas 2, 5).
  - Every completed profile has only the terminal self-loop as a cycle.
  - h = 2 example (Table 2, p.12): pivots (a1,q1), (a2,q2), (a1,p1). The initially selected (a1,p1) re-enters at pivot 3.

## (iii) Parity encoding (for Ĝ_h; Player 1 = Even, Player 2 = Odd)
Even maximises its VJ value, so Even value = −cost. Odd's best reply σ̄ (S1) = Mei's π²(σ). Costs sit on edges and VJ priorities on
vertices, so split every costed edge with a fresh vertex of out-degree 1 (owner irrelevant; say Odd).

**Vertices (n = 8h + 3).**
- Mei's 4h + 2 states with Mei's owners. Priorities:
  - a_{h+1}: 1 (odd), with a self-loop: the sink, Odd-won, the only cycle node of every completed profile;
  - every other Mei state (a_i, p_i, q_i, b_i for i ≤ h, and b_{h+1}): priority 0, so they are less relevant than a_{h+1} and never
    enter P.
- Cost vertices (forced, one edge each), replacing the costed edges:
  - w^p_i on p_i → w^p_i → a_{i+1}, and w^q_i on q_i → w^q_i → b_{i+1}: cost W_i > 0, bad for Even, so ODD priority;
  - k^p_i on p_i → k^p_i → a_i, and k^q_i on q_i → k^q_i → a_i: cost −K_i, good for Even, so EVEN priority;
  - r on b_{h+1} → r → a_{h+1}: cost −R, so EVEN priority.

**Priorities (h ≥ 2; d = 8h + 2):**

| vertex | priority |
| --- | --- |
| a_{h+1} | 1 |
| w^p_1, w^q_1 | 3, 5 |
| k^q_i, k^p_i (i = 1..h) | 6 + 4(h − i), 8 + 4(h − i) (so k^p_1 = 4h + 4 is the top K, k^q_h = 6 the bottom) |
| w^p_i, w^q_i (i = 2..h) | 4h + 4i − 3, 4h + 4i − 1 |
| r | 8h + 2 |
| all other vertices | 0 |

Rank order (S1, by (Ω, v)), from most relevant down:
    r > W-level h > … > W-level 2 > k_1 > … > k_h > W-level 1 > a_{h+1} > priority-0 vertices.

**Preservation claims.** "Higher levels decide" is used throughout. For every profile with only the sink cycle, P(a_{i+1}) and
P(b_{i+1}) differ, and their top differing vertex has rank ≥ min(rank w^p_{i+1}, rank w^q_{i+1}) (or is r at level h + 1). This
follows from the recursion below, by induction from level h + 1.

| Mei | parity port | status |
| --- | --- | --- |
| VJ order = path-sum order on these plays | every play from a level state is simple and ends at a_{h+1}. P = the set of cost vertices on it (all more relevant than a_{h+1}). Signed weights Σ ±2^rank of distinct ranks compare by the top differing rank | PROVED-S (S1; injective ranks) |
| Lemma 2 (best reply never keeps the created 2-cycle) | the cycle a_i → s → k^s_i → a_i has top k^s_i (even), so it is Even-won. The alternative play reaches the Odd-won sink. Odd prefers the odd cycle node. Holds for ANY magnitudes | PROVED-S |
| Lemma 4 (sign rule; ∆ in Even-value terms is −∆_Mei) | v_{a_i} = w^σ_i ⊕ v_{next}, b_i takes Odd's choice. If higher levels agree to the extent that b_i follows a_{i+1}, then P(a_i) Δ P(b_i) = {w^σ_i} (bad for Even, so ∆_Mei > 0). Otherwise the top difference is at level ≥ i + 1, so sgn is inherited (σ = p) or flipped (σ = q). Base: P(b_{h+1}) = {r}, so ∆_{h+1} > 0 | PROVED-S (needs only the W-layering: level i+1 above level i, r on top) |
| Lemma 5 (return at the unselected s iff ∆_i > 0, i.e. iff Mei's condition on ∆_{i+1} and σ(a_i)) | return = {k^s_i} ∪ P(a_i); forward = {w^s_i} ∪ P(next(s)). The top difference is at level ≥ i + 1 (above k^s_i, because every k lies below W-level 2), so the decision is Mei's | PROVED-S (needs rank k_i < W-level i+1: satisfied, since all k are below W-level 2) |
| Lemma 6 (gate = {(a_i, s) : ∆_i > 0}; Dantzig pivot = smallest such i) | honest improving: Ξ(s) = {k^s_i} ∪ Ξ(σ(a_i)) when s returns. Its gain over σ(a_i) is exactly the even vertex k^s_i; otherwise s goes forward and is worse. The lexicographically largest gain is the highest-ranked k^s_i, i.e. the smallest i | PROVED-S (k ranks decreasing in i) |
| Lemma 7 / Thm 4 (2^h − 1 iterations, one joint λ-phase) | for "Dantzig-SSI on VJ" (one switch, lexicographically largest honest gain, Odd = exact σ̄), the counter identity follows from the four rows above. Only the sink is ever a completed cycle, so the whole run is one λ-phase of Even's honest valuation | PROVED-S, to be confirmed by L-RED's run (a Dantzig-SSI control on si.py or similar) |
| two-scale separation | W-layering (by level, increasing in i) fixes values. k-layering (decreasing in i, all below W-level 2) fixes the pivot. The two never interact, because k-vertices lie only on unselected auxiliary plays, which no level state's play visits | PROVED-S |

Remarks:
- Mei's actual magnitudes (K_1 = 2W_1, W_1 = K_2) are not reproduced and need not be. The only K/W relations the four lemmas use are
  rank k_i < W-level i+1, plus "k has even priority".
- Placing W on a_i instead of on the forward edges would force k_i above w_i (for Lemma 2) and break the pivot order. Do not do
  that.

**For (ELIM-n) (READING).**
- Under Dantzig-SSI on the port, level i's two edges alternate 2^(h−i) times, so no edge is retired until the last pivots.
- That is a non-eliminating run of length 2^h − O(h) inside one phase: an (ELIM-n) counterexample for Dantzig-SSI (PROVED-S via the
  row above).
- The question is only whether N5 follows (iv).

## (iv) Where N5 deviates from Dantzig-SSI
**N5 (S4).** From the same (σ_k, τ_k), simultaneously:
- **Even:** the gate I_σ = honest-improving edges against σ̄_k (= Mei's τ_k). The arena A = {σ(v)} ∪ gate. σ_new = Even's optimum in A
  against N5's OWN Odd strategy τ_k.
- **Odd:** the symmetric step on the dual against σ_k. τ_new = Odd's arena optimum.
- **Fallback** (S4c) if neither changes.

**First possible difference: iteration k = 0, the very first, for every h ≥ 2.**
- At σ_0 = (4), all ∆_j > 0 (Lemma 7 base), so the gate contains (a_j, q_j) for EVERY j = 1..h (Lemma 6 row). Dantzig takes only
  (a_1, q_1).
- With the faithful start pair (σ_0, τ_0 = σ̄_0): τ_0 returns at every q_j (Lemma 5 row).
  - Against τ_0, switching a_j → q_j closes the Even-won cycle a_j → q_j → k^q_j → a_j. So Even's arena optimum switches ALL h
    levels at once (each gives a better cycle node than the sink).
  - Odd's simultaneous step leaves every q_j forward: against Even's best reply to τ_0, entering those cycles is Even's best, so
    Odd's improving edges are (q_j, w^q_j).
- CONJECTURE: after iteration 1, σ_1 = all q, and τ_1(q_j) = forward. N5 thereby does h of Dantzig's create/cancel pairs in one
  iteration (create by Even, cancel by Odd, simultaneously).
- CONJECTURE: N5 then finishes in O(h) iterations on the plain port. The multi-switch arena behaves like switch-all on a binary
  counter, which this construction does not delay; there is no deceleration lane.
- **Second difference (structural).** N5's selection is against its own τ_k, not σ̄_k. Whenever τ_k lags σ̄_k (Odd's step has not yet
  cancelled), Even's selection counts the created cycle as real. This is the trust mode of box 25 §5 on a mixed cycle through an
  Odd choice vertex. Here every p_i, q_i is an Odd choice vertex, so the port is NOT in 𝒞^1O; it has 2h Odd choice vertices.

**What L-RED needs to run.**
1. The port as above. Check by Oink zlk + verify.py that a_{h+1}'s Odd sink wins everywhere: every level state is Odd-won, since
   Odd can always reach the sink.
2. A Dantzig-SSI control on VJ valuations (single switch, top-ranked honest gain, Odd = σ̄). Expected 2^h − 1 iterations in one
   phase (the PROVED-S row).
3. N5 from (a) the start pair (σ_0 = (4), τ_0 = σ̄_0) and (b) the canonical S3 start. Measure iterations, the longest
   non-eliminating run (elim.py) and the phases.
4. If N5 is short (CONJECTURE (iv)), the port must be modified so that N5's gate is a SINGLETON. Candidate: Fearnley-type
   deceleration lanes on the levels j > lowest positive one, making their gate edges non-improving until level i resolves. That is
   a new construction, not Mei's.

No running-time claim is made (D1). G-N5-TIME stays OPEN.
