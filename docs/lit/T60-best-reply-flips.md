# T60: how often can the opponent's best reply change while one player improves? Symmetric SI, best-response counts in two-player and stochastic games, and monotone comparative statics (Topkis / Milgrom-Shannon) against SB_F
L-LIT successor T59 (Opus 5.5), D18. Lead's brief 2026-10-30 18:54Z (T60). The residual inside a W-run is L-SI's HEAD-RED (P-N5-SETTLE,
l-si docs/si/P-N5-SETTLE-line.txt, under review): per-vertex counts SB_F(o) of σ̄-flips, CN_F of W-cycle-node switches and HXU_F of
head Ξ-changes. FLIP-EV is DEAD (l-si 051eb196, flipev_n20). Written 2026-10-30 18:55Z-19:20Z (date -u). Working note, unrefereed, not a
TARGET.md claim. G-N5-TIME stays OPEN; no count is bounded here.
Labels as in T59. Notation as in P-N5-SETTLE §1: F a W-run (τ fixed, λ_W fixed, no S4c fallback); Ξ_k, σ̄_k (S1's Odd counterstrategy to
σ_k); SB_F(o) := the transitions of F at which σ̄(o) changes; U_k = L-RED R143's upward heads. Tool: docs/lit/T60-sc-check.py.

## Summary
- (a) Symmetric SI (Schewe-Trivedi-Varghese 1501.06484, ICALP 2015) does not bound the opponent's counterstrategy changes.
  - Its only argument against Friedmann's trap is informal and specific to G_n (p.9: Min's OWN strategy locks the j most significant
    simple cycles «after 2j improvement steps»; «We have not formalised these arguments on other instances»).
  - The follow-up van Dijk-Loho-Maat 2309.02223 Thm 1 (p.2) makes symmetric SI exponential «independently of the improvement rule».
    The mechanism is that «the optimal counterstrategy to a bad strategy can also be a bad strategy itself» (p.3). Following
    counterstrategies does not make them settle.
- (b) No opened source bounds the opponent's best-response changes on their own. They are bounded either through the total iteration
  count, or by charging each change to an ORDER CHANGE among a few distinguished values.
  - Through the total count: HMZ Lemma 6.4 p.11 eliminates only player-1 actions, «We may assume, therefore, that a ∈ A₁», via
    (c^{π*})_{A₂} ≤ 0, Lemma 3.7.
  - Through order changes: Auger-Badin de Montjoye-Strozecki 2102.04922, proof of Thm 29, pp.16-17, and Gimbert-Horn's f-strategies
    (LMCS 5(2:9)).
    - «when the random order changes, the value of some random vertex increases by at least q^−r», giving ≤ r·q^r such steps.
    - f-strategies are determined by the order, so there are ≤ r! iterations.
  - The order-change template is the literature form of HEAD-RED. For N5 it needs (i) σ̄ determined by Ξ's order on the heads U
    (R143's downward dependence (A) is the start), and (ii) a quantum or no-repeat for head orders. (ii) is XI-CH-POLY again (ordinal
    values), or a no-repeat lemma that is OPEN.
  - Rule-free statements are impossible. Under switch-all, Friedmann LMCS Lemma 6.1 p.10 makes τ_σ(e_i) mirror bit i of a 2^n counter
    in one cycle-node phase, so Ξ rises monotonically while σ̄(e_1) flips 2^Θ(n) times. Any bound on SB_F must use S4a, not only Ξ's
    monotonicity.
- (c) Monotone comparative statics gives SB_F(o) ≤ deg(o) − 1, but only under SINGLE CROSSING.
  - Hypothesis (Milgrom-Shannon / Topkis, as stated in Etessami-Papadimitriou-Rubinstein-Yannakakis 1909.03210 §5.1 p.22): f(w, t) :=
    −Ξ_t(w) is single crossing in (w, t) for some linear order of succ(o), with a monotone tie selection.
  - N5 does NOT meet it. DATA: on latew_K16_m32 one Odd vertex of out-degree 2 flips σ̄ 32 times in one W-run, and its two successors
    reverse their Ξ-order 32 times (16 at K = 8). On switchbestexp_6 a degree-2 vertex reverses 3 times.
  - So no order of the successors has single crossing in time: the Topkis route per vertex is DEAD (corpus §4.3).
  - What survives is the elementary Lemma PAIR-CROSS (§4.2): SB_F(o) ≤ (strict pair reversals among succ(o)) + (tie re-orders). That
    turns SB_F into a count of how often two successors' Ξ leapfrog, the same quantity as FLIP-EV step 1 and HEAD-RED.
- The bridge that is still open is the Gimbert-Horn / Auger "best reply = function of an order of few values" template. It would make
  W-runs FPT in max |U_k|. The missing lemmas are ORDER-DET and NO-REPEAT (§3.3).

## 1. Sources (opened 2026-10-30, scratchpad t60/A and t59/A; sha256 prefixes in notes/L-LIT.md)
- [STV] Schewe-Trivedi-Varghese, arXiv 1501.06484 v1 (ICALP 2015). Alg. 2 p.2 (naive symmetric SI; «suggested by Condon [5] where it
  was shown that a repeated application of this update can lead to cycles»). Alg. 3 p.2. Alg. 5 p.6. Lemma 3.1 p.6, Thm 3.4-3.5. §4 pp.8-9
  on Friedmann's G_n.
- [vDLM] van Dijk-Loho-Maat, arXiv 2309.02223 v1. Thm 1 p.2; «Technical overview» p.3; the 2j-th iteration argument and the
  self-similar recursion pp.11-12; Thm 13 p.15; Discussion p.15.
- [DDS] Dell'Erba-Dumas-Schewe, arXiv 2404.04124 (LMCS 22(1) 2026). Abstract (objective improvement, symmetric). No best-response count.
- [F11] Friedmann arXiv 1106.0778 v2. Lemma 6.1 p.10 («(1) If cycle i is closed, we have τσ(ei) = hi. … (3) If cycle i is open and
  σ(di) ≺σ hi, we have τσ(ei) = di»); p.10 «by moving to di, the player 1 node hides …»; Thm 6.14.
- [HMZ] arXiv 1008.0530 v1. Lemma 3.7 p.6 (optimality: (c^π)_{A₁} ≥ 0, (c^π)_{A₂} ≤ 0). The algorithm p.9 («τ^k = τ₂(σ^k)»). Lemma 6.4
  and its proof p.11.
- [ABS] Auger-Badin de Montjoye-Strozecki, arXiv 2102.04922 (MFCS 2021). Prop. 7, BR(σ) p.4. Thm 29 and its proof pp.16-17. §5.1 p.17
  (Gimbert-Horn's algorithm as an instance; f-strategies; «bounded by r!»). §5 p.17 (Hoffman-Karp as an instance of GSIA).
- [GH] Gimbert-Horn, «Solving simple stochastic games with few random vertices», arXiv 0712.1765 (LMCS 5(2:9) 2009). Opened (title page);
  its content is used only as [ABS] §5.1 restates it.
- [EPRY] Etessami-Papadimitriou-Rubinstein-Yannakakis, arXiv 1909.03210 (ITCS 2020). §5.1 p.22: definitions C1-C3, increasing
  differences, single crossing; «the best response correspondence βi(s−i) … both functions sup βi(·) and inf βi(·) are monotone
  functions [56]». §6: Condon's SSGs reduce to Tarski (the monotone object is the value vector).
- NOT OPENED: Topkis 1978 (Oper. Res.) and Milgrom-Shannon 1994 (Econometrica 62(1); JSTOR paywall). Their theorem is used only as
  [EPRY] §5.1 states it. Also not opened: Hoffman-Karp 1966; Condon 1993; Björklund-Vorobyov DAM 2007; Quah-Strulovici 2009
  (interval dominance order).

## 2. (a) Symmetric strategy improvement
- [STV] Alg. 3 / Alg. 5: σ is updated only by profitable switches that agree with στ^c, the counterstrategy to τ, and symmetrically for τ.
  Correctness and termination: Lemma 3.1, Thm 3.4-3.5. No iteration bound.
- On G_n (§4 pp.8-9, informal): «Player Min will move to the right in the j most significant positions after 2j improvement steps».
  - This is a TOP-DOWN LOCKING of the opponent's OWN strategy τ, not a statement about the counterstrategy τσ^c. Under single-sided SI,
    τσ^c mirrors Max's bits («the optimal counter strategy by Player Min is to move to the right in simple cycles where Player Max is
    moving to the right, and to move left in all other simple cycles», p.9).
  - «We have not formalised these arguments on other instances» (p.9).
- [vDLM] Thm 1: exponential for symmetric SI «independently of the improvement rule», for parity, mean-payoff and discounted games.
  Thm 13: also for the generalization that compares valuations directly.
  - Mechanism (p.3): «the optimal counterstrategy to a bad strategy can also be a bad strategy itself».
  - pp.11-12: the instance G_j is solved by solving G_(j−1), making the crucial switches, and solving G_(j−1) again. READING: the
    counterstrategies on G_(j−1)'s nodes run through their whole sequence twice, so per-vertex counterstrategy changes double with j.
- Does N5's W-run meet [STV]'s hypothesis? No. Inside a W-run τ is FIXED (R89). The STV-type locking of τ is a statement across W-runs
  (N5's S4b τ-steps), not about SB_F.
  - N5 is not symmetric SI. S4a takes Even's arena optimum against τ, and Iσ uses Ξ (σ̄).
  - The repo's data: N5 runs [vDLM]'s instances in 1-13 iterations (T37 §1, SPEC "First test").
- Bound for SB_F: none.

## 3. (b) Counting the opponent's best-response changes
### 3.1 Through the total count ([HMZ])
- Player 2 best-responds every iteration (τ^k = τ₂(σ^k), p.9). Its reduced costs satisfy (c^π)_{A₂} ≤ 0 (Lemma 3.7).
- Lemma 6.4 eliminates an action of the profile π^k, and the sign argument puts it in A₁ («We may assume, therefore, that a ∈ A₁»).
- So player 2's best-response changes are bounded only by the total iteration count, (m + 1)(1 + log_{1/γ} n²/(1 − γ)) (Thm 6.5).
- For N5 this gives only SB_F(o) ≤ |F|, which HEAD-RED already uses.

### 3.2 Rule-free statements are impossible ([F11] Lemma 6.1)
- Let σ improve by switch-all on Friedmann's G_n, one cycle-node phase (T53). Lemma 6.1 (1)-(3) makes Odd's best reply at e_i equal to
  h_i iff bit i is set (closed, or open with h_i ≺ σ(d_i)).
- Bit 1 changes 2^Θ(n) times while Ξ rises monotonically (Thm 6.14). So σ̄(e_1) changes 2^Θ(n) times. PROVED (source) + elementary.
- Consequence: "Ξ non-decreasing" alone gives no polynomial bound on per-vertex best-reply flips. A bound on SB_F has to use S4a, as
  R140 does to kill G_n.

### 3.3 Through order changes of a few values ([ABS] Thm 29; [GH] via [ABS] §5.1)
- [ABS] p.17: «We assume that the order of the values (in G) of the random vertices is the same for σ and σ′. Then, knowing this order and
  σ′, it is easy to compute τ(σ′) a best response».
  - «when the random order changes, the value of some random vertex increases by at least q^−r, hence there are at most rq^r such steps».
- [GH] (as restated in [ABS] §5.1): an f-strategy is an optimal strategy for a total order f of the random vertices and sinks. The
  algorithm produces an improving sequence of f-strategies, so it makes at most r! iterations.
- So best-response changes are charged to ORDER CHANGES among r distinguished values. These are counted either by a value quantum
  (q^−r) or by no-repeat of orders (r!). That is FPT in r.
- N5 analogue (READING): the distinguished set is the upward heads U_k (R143, P-N5-SETTLE).
  - R143 (A) «Ξ_k(y) is a function of σ_k on the Even vertices of layers ≤ d, of σ̄_k, and of Ξ_k on U_k» is the analogue of
    «knowing this order and σ′».
  - Missing lemma ORDER-DET (OPEN): inside a W-run, between CN switches, σ̄_k is determined by σ_k and the ⊴-ORDER (not the values) of
    Ξ_k on U_k.
  - Missing lemma NO-REPEAT (OPEN): the sequence of head orders visited in F never repeats a (σ-pattern, order) pair. In [GH] this follows
    from strict improvement because the order alone fixes the strategy.
  - With both, SB_F would be ≤ the number of distinct orders, i.e. FPT in max_k |U_k|.
  - Without NO-REPEAT, the quantum route needs a lower bound on each order-changing rise of Ξ. Ξ is ordinal with exponentially many
    values per vertex, so the [ABS] quantum gives only an exponential bound: XI-CH-POLY again.
- This is the template HEAD-RED instantiates. The literature adds nothing beyond FPT-in-|U| unless NO-REPEAT holds. A suggested test for
  L-SI (not run here): max_k |U_k| and the number of distinct head orders per W-run on latew / fx.

## 4. (c) Monotone comparative statics (Topkis / Milgrom-Shannon) and the σ̄-flips
### 4.1 The hypothesis, exactly ([EPRY] §5.1 p.22)
- Odd at o chooses w ∈ succ(o) to maximize f(w, t) := −Ξ_t(w), along the chain t ∈ F (Ξ_t non-decreasing, R15).
- Single crossing in (w, t) for a linear order ≤_o of succ(o): for w′ >_o w and t′ > t, f(w′, t) ≥ f(w, t) ⇒ f(w′, t′) ≥ f(w, t′), and
  strict ⇒ strict.
- Then the sup (inf) best reply is monotone in t ([EPRY], citing Topkis / Milgrom-Shannon). So σ̄(o) changes ≤ deg(o) − 1 times in F,
  if S1's tie selection is the sup (or inf) selection.
- Increasing differences in the full value vector (f(w, x) = −x_w, x ∈ the lattice of value vectors) fails for every order of succ(o) as
  soon as two coordinates can rise independently. So time-single-crossing along the actual run is the only usable form.

### 4.2 Lemma PAIR-CROSS (PROVED, L-LIT, elementary)
- Let rev_F(w1, w2) be the number of reversals of the strict Ξ-order of w1, w2 along F (ties skipped). Then
  SB_F(o) ≤ Σ_{w1, w2 ∈ succ(o)} rev_F(w1, w2) + TIE_F(o).
  TIE_F(o) counts the flips t1 → t2 at k → k + 1 with Ξ_(k+1)(t1) = Ξ_(k+1)(t2), or with Ξ_k(t1) = Ξ_k(t2) and no strict reversal of
  (t1, t2) at k.
- Proof. A flip t1 → t2 with neither tie has Ξ_k(t1) ◁ Ξ_k(t2) (t1 was the strict argmin) and Ξ_(k+1)(t2) ◁ Ξ_(k+1)(t1), so the strict
  order of (t1, t2) reverses at k. □
- If every pair reverses at most once and the reversal arcs are acyclic (a single-crossing order exists), then SB_F(o) ≤ C(deg, 2) +
  TIE_F(o). With a monotone tie selection, Topkis gives deg − 1.
- L-SI's FLIP-EV analysis (box 52 §3, steps 1-3) is the tie part. Its GAP is an ENT flip at a tie, so TIE_F is exactly where FLIP-EV
  died.

### 4.3 DATA (docs/lit/T60-sc-check.py; W-runs as T58/T59)
| instance | n | max |F| | SB (max σ̄-flips of one Odd vertex) / its out-degree | PF (max reversals of one successor pair) | (run, o) with SB > 0: SC1 (some pair reverses > 1) / CYC / SCOK | OVER |
| --- | --- | --- | --- | --- | --- | --- |
| latew_K8_m32 (R2-N5-CUT inst) | 370 | 280 | 16 / 2 | 16 | 31 / 0 / 32 | 0 |
| latew_K16_m32 (red/rstar pin) | 482 | 560 | 32 / 2 | 32 | 31 / 0 / 64 | 0 |
| switchbestexp_6 | 160 | 44 | 3 / 2 | 3 | 5 / 0 / 1 | 0 |
| fx_K4_m16, fx_K8_m16 | 130, 186 | 76, 152 | 1 / 2 | 1 | 0 / 0 / 16, 32 | 0 |
| flipev_n20 (l-si 051eb196) | 20 | 1 | 1 / 3 | 1 | 0 / 0 / 2 | 0 |

- On latew the per-vertex σ̄-flips are 2K, linear in n (n = 14K + 258). The pair at that vertex reverses 2K times. No order of a degree-2
  vertex's successors is single-crossing there.
  - DEAD (route): "SB_F(o) ≤ deg(o) − 1 by Topkis / Milgrom-Shannon single crossing in time". Killed by latew_K16_m32 (SB 32 at
    out-degree 2, PF 32) and switchbestexp_6 (PF 3).
  - Also dead: any Davenport-Schinzel bound on the sequence σ̄_t(o) at a degree-2 vertex (the sequence alternates a b a b … 2K times;
    T52's DS route was already DEAD on the Even side, R137).
- Where single crossing holds (SCOK), OVER = 0 on these instances: S1's tie selection did not add flips beyond deg − 1 there.
- Corpus: §4.4 (gate_K64_n581: SB 62 at out-degree 2, PF 61).

### 4.4 Corpus
- Scope: the same 892 games as T59 §4.4 (each with its .start if present), 30 s timeout each. Run 2026-10-30 19:12Z-19:17Z (date -u),
  output scratchpad t59/c60b.out.
  - 877 finished; 14 timed out (rc 124); 1 failed (dlmm_ML_L6, unparsable .start).
  - The timeouts include latew_K16_m32, which was run separately above (61 s).
- Totals: 663 games have a W-run of length ≥ 1; 404 have a σ̄-flip; 8,717 flips.
  - Over the (run, Odd o) pairs with SB > 0: SC1 1,677 (some successor pair reverses more than once), CYC 0, SCOK 1,811.
  - 259 games have a pair reversing more than once.
- Largest SB:
  - gate_K64_n581: 62 at out-degree 2, PF 61 (the corpus maximum L-SI box 52 reports);
  - pp_K48_n449: 49 at out-degree 3, PF 49;
  - pft35_n48: 35 at out-degree 25, PF 5;
  - pftheta34_n32: 34 at out-degree 19, PF 6.
- OVER (SB > deg − 1 although a single-crossing order exists) occurs 3 times: nep13_n24 (6 at degree 6), nep22f_n64 (2 at degree 2),
  run34_n40 (7 at degree 4). These are tie-selection flips, i.e. PAIR-CROSS's TIE term. nep13_n24 is L-SI's own-cycle-node instance.
- Reading:
  - Single crossing fails at about half of the flipping vertices.
  - At the high-SB degree-2/3 vertices (gate, pp, latew) one successor pair simply leapfrogs SB times.
  - At high-degree vertices (pft*), SB is spread over many pairs with ≤ 7 reversals each.
  - A per-vertex bound has to bound leapfrogging (Ξ-changes of the two successors, i.e. HEAD-RED's HXU), not exploit an order.

## 5. Table (the brief's per-source questions)
| source (opened) | exact hypothesis | does N5's (σ_t, σ̄_t) inside a W-run meet it? | missing lemma | bound it would give for SB_F |
| --- | --- | --- | --- | --- |
| [STV] Alg. 3/5, §4 p.9 | both players switch only along the other's counterstrategy; G_n analysis informal | no: τ fixed in a W-run; N5's S4a is an arena optimum, not symmetric | a formal top-down locking lemma, and it would concern τ across W-runs | none |
| [vDLM] Thm 1, 13 | symmetric SI, any rule | n/a; shows that following counterstrategies does not settle them (recursion doubles them) | – | none (lower bound for SSI) |
| [F11] Lemma 6.1, Thm 6.14 | switch-all, Ξ monotone, one cycle-node phase | no (S4a kills G_n, R140), but it shows monotone Ξ alone is not enough | a bound must use S4a | 2^Θ(n) flips of σ̄(e_1) under switch-all |
| [HMZ] Lemma 3.7, 6.4 | 2TBSG, Howard vs best response, fixed γ | no discount | – | SB ≤ total iterations only |
| [ABS] Thm 29; [GH] (via [ABS] §5.1) | best response is a function of the ORDER of r random-vertex values; each order change raises a value by ≥ q^−r; or orders never repeat | partly: R143 (A) gives downward dependence on Ξ|U | ORDER-DET and NO-REPEAT (OPEN); a quantum is XI-CH-POLY | ≤ number of distinct head orders, FPT in max |U_k| (if both lemmas hold) |
| [EPRY] §5.1 (Topkis; Milgrom-Shannon NOT OPENED) | single crossing of −Ξ_t(w) in (w, t) for an order of succ(o), monotone tie selection | NO: latew_K16_m32 (PF 32 at out-degree 2), switchbestexp_6 (PF 3) | none salvageable; PAIR-CROSS reduces SB to pair reversals + ties | deg(o) − 1 if met; DEAD as a route |
| [EPRY] §6 | Condon SSG value = Tarski fixed point of a monotone operator | the monotone object is Ξ (values), not σ̄ | – | none |

## DONE / FINDINGS / NEEDS
- DONE: this note; docs/lit/T60-sc-check.py; notes/L-LIT.md.
- FINDINGS:
  1. No opened source bounds the opponent's best-response changes on their own. [HMZ] bounds them through the total count only (it
     eliminates player-1 actions only, Lemma 6.4 p.11). [ABS] / [GH] charge them to order changes among r distinguished values (r·q^r,
     or r! by no-repeat). Symmetric SI ([STV]) has only an informal G_n argument, and [vDLM] makes it exponential for every rule.
  2. Rule-free bounds are impossible: under switch-all, [F11] Lemma 6.1 makes σ̄(e_1) flip 2^Θ(n) times while Ξ rises monotonically. A
     bound on SB_F must use S4a.
  3. Topkis / Milgrom-Shannon single crossing would give SB_F(o) ≤ deg(o) − 1, but N5 fails it. On latew_K16_m32 a degree-2 Odd vertex
     flips 32 times and its successor pair reverses 32 times (2K; linear in n). DEAD as a route. PROVED (L-LIT): PAIR-CROSS, SB_F(o) ≤
     pair reversals + tie re-orders.
  4. OPEN bridge: the [GH] / [ABS] f-strategy template (best reply = function of an order of few values) would give FPT in max |U_k| with
     ORDER-DET + NO-REPEAT.
- NEEDS: none from the owner (optional: Milgrom-Shannon 1994, Topkis 1978, Hoffman-Karp 1966, Condon 1993 via library).
