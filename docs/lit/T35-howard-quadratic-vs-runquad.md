# T35: Hansen-Zwick's quadratic Howard bound and its successors, against L-RED's runquad and CONJECTURE SW-PER-VERTEX (L-LIT, 2026-10-29)

Asked by the Lead at 10:54Z (date -u). Owner ruling D18:
> Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and
> computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed
> without asking me questions. Clearly distinguish proven results from conjectures and open problems.

**Labels.**
- PROVED (source): a theorem of an opened source.
- READING: L-LIT interpretation.
- CONJECTURE / OPEN: as in D18 / L40.

Nothing here bounds N5. G-N5-TIME stays OPEN.

**N5 objects.**
- runquad: docs/red/R106-quadratic-run.md on claude/l-red (read only; R106 pending). A fallback-free in-phase run of 264 iterations at
  n = 192 that is one REL segment; (H4′_rel) fails; family L = 4K² + 3K − 1 at n = 24K + 6 (with m = 4K).
- CONJECTURE SW-PER-VERTEX (L-SI, docs/NOW.md roster): O(n) switches per Even vertex per run, hence O(n²) per run.

## Sources opened (sha256 in notes/L-LIT.md)

| key | source | read |
| --- | --- | --- |
| [HZ] | Hansen, Zwick, "Lower bounds for Howard's algorithm for finding minimum mean-cost cycles", ISAAC 2010, LNCS 6506 pp. 415-426 | the AUTHORS' TALK SLIDES only, dated 16 Dec 2010 (pdfs.semanticscholar.org/8eaf/45e9…pdf, sha256 1ff1ee80…), pp. 6-19 |
| [ACR] | Asadi, Chatterjee, de Raaij, "Lower bound on Howard policy iteration for deterministic Markov decision processes", arXiv 2506.12254 v1 (UAI 2025) | §1-§4: Table 1, Conjecture 3.1, Theorem 3.2 (p.4), policy families and sequence (1), Lemma 4.1 (p.5), intuition paragraph |
| [ZY] | Zhong, Ye, "Policy iteration is not strongly polynomial for deterministic Markov decision processes: the price of algorithmic anarchy", arXiv 2609.40147 v2 (13 Oct 2026; re-opened, = T30's file) | abstract, §1 + Table 1, §6.1 (construction), Lemma 6.2 (p.26), Theorem 6.1 (p.23), Theorem 7.2 and its proof (p.33-34), §8 |
| [GGK] | Goenka, Gupta, Khyalia, Agarwal, Wajid, Kalyanakrishnan, "Upper bounds for all and max-gain policy iteration algorithms on deterministic MDPs", arXiv 2211.15602 v2 | abstract, §4: Definitions 13-18, Lemmas 7-8, Theorems 4-5, Corollaries 1-2 |
| [MK] | Mukherjee, Kalyanakrishnan, "Howard's policy iteration is subexponential for deterministic MDPs with rewards of fixed bit-size and arbitrary discount factor", arXiv 2505.00795 v1 | abstract, §1.1, Theorem 1.2 |
| [F] | Friedmann, arXiv 1106.0778 v2 (re-opened for T34) | §5 p.8 |

**Not opened.**
- [HZ]'s paper text (the Springer PDF came back empty; no author copy at www.cs.tau.ac.il/~zwick/papers/).
- Hansen's thesis (Aarhus 2012; Conjecture 6.1.1 is cited through [ACR] and [ZY]).
- Madani's 2n − O(1) bound (personal communication, cited in [HZ] slides p.13).
- Christ-Yannakakis.
- Every statement attributed to [HZ] below is from the authors' slides or from [ACR] / [ZY]'s descriptions, and is labelled so.

## 0. Answers
1. **Is [HZ]'s Ω(n²) construction structurally the same as runquad?**
   - Same skeleton, different level.
     - [HZ] / [ACR]: a DECELERATION LANE advances one vertex per iteration. A higher-level event resets all of it in one iteration.
       Total = (number of events) × (lane length) ≈ n².
     - runquad: a reactor chain advances one reactor per iteration (the "wave"). A rise of the other pivot flips the whole chain
       back in one step. Total = (number of pivot rises) × (chain length).
   - The difference that matters for N5.
     - In [HZ] / [ACR] the reset event is a NEW BETTER CYCLE (a gain change). In N5 terms that is a λ-change, i.e. a new phase.
     - In runquad the reset is a P-change of pivot h′ INSIDE one phase (λ and τ constant, R106 §2).
     - So runquad is the bias-level (in-phase) analogue of [HZ]'s gain-level mechanism.
   - That is exactly what one-player Howard cannot do. [ZY] Theorem 7.2's proof (p.34): "every N consecutive updates create a new
     cycle". Bias-only stretches of Howard on deterministic average-reward MDPs are shorter than N.
   - runquad shows that N5's in-phase stretch is not bounded like that. It is a two-frame effect: (H4′_rel) fails, while the
     one-player statement is the analogue of R82 / R83's STATIC-DEPTH.
2. **Nesting beyond n².**
   - [HZ] slides p.19 conjectured "at most the number of edges" ([ACR] Conjecture 3.1 = Hansen 2012 Conjecture 6.1.1).
   - [ZY] Theorem 6.1 REFUTES it: Howard needs exp(Ω(N)) iterations on deterministic average-reward MDPs with ≤ 4 actions per state.
   - [ZY]'s nesting is a binary counter on CYCLE MEANS. Every count step forms a new cycle with strictly larger mean reward ([ZY]
     eq. (6.8), Lemma 6.2: Howard "produces a policy containing the cycle C_n after 3n − 1 iterations").
   - That mechanism is BLOCKED for N5, as a fact: a parity valuation's cycle component takes at most n values ([F] §5 p.8: "there are
     only linearly many different values for the first and third component"), and RESULTS R47 Lemma Φ bounds the joint λ-runs by
     2n(n − 1) + 1 on every game (R106 §5).
   - So an N5 nesting beyond n² must happen at the bias level (path sets), i.e. through the P-change carries of T33 / P-N5-MPGS (A).
     No published construction does that. [ZY]'s small-reward exponential examples (Theorems 2.2-2.3) are DISCOUNTED and also count
     by cycles.
3. **An upper-bound argument for SW-PER-VERTEX?**
   - None transfers directly. The closest is [ZY] Theorem 7.2's two-part proof:
     - (i) the bias-level depth argument (one-player STATIC-DEPTH);
     - (ii) a potential, the sum of gains, that rises by ≥ 1/N at each cycle creation and has range N·2^b.
   - (ii) needs small integer rewards. N5's order is lexicographic with weights 2^rank, i.e. unrestricted rewards, where [ZY] proves
     Howard exponential.
   - The polynomial-range potential N5 does have is P-N5-MPGS (A)'s Φ (range ≤ n²/2, quantum 1). It rises only at matched
     P-changes.
   - §4 states the composite as a CONJECTURE.
   - [GGK] and [MK] give exponential and subexponential bounds respectively. [GGK]'s per-class elimination lemmas are of the
     "an edge is used at most once per class" kind and do not bound per-vertex switches polynomially.
   - DATA: runquad itself has O(n) switches per reactor (two per pivot round, K rounds, n = 24K + 6). It is consistent with
     SW-PER-VERTEX and tight in the sense L-SI states.

## 1. [HZ] and [ACR]: the quadratic constructions (PROVED, source)
- **[HZ] slides.**
  - p.14 "Theorem (Hansen and Zwick (2010)) For any integer n, there exists a weighted directed graph with n vertices on which
    Howard's algorithm performs Ω(n²) iterations."
  - Main idea: "Use cycles of very large cost to make Howard's algorithm favor going through many edges (recall that when computing
    potentials the value was subtracted at every step)."
  - p.15-16 "Delaying discovery of cheap cycles", "Getting alternating behaviour".
  - p.17: edge costs n^k, and one edge −n^N with N = n² + n (exponential weights).
  - p.18: the sequence was found by an LP-based search for long policy sequences.
  - p.19 Conjecture: Howard's iterations ≤ number of edges.
- **[ACR], as a description of [HZ]** (p.2; Table 1).
  - [HZ] give "DMDPs with 2n vertices, m edges, and edge weights of O(n^{n²}), on which the algorithm requires m − n + 1
    iterations".
  - "Howard's policy iteration goes through Θ(n²) 'good' cycles and due to the structure of the graph only ever finds a slightly
    better cycle. Each cycle weight is determined by a 'key' edge with largest weight."
- **[ACR] Theorem 3.2 (p.4).** "There exists a DMDP with 2n vertices, (3n² + n)/2 edges, and size of O(n² log n) on which Howard's
  algorithm performs (n² + 7n − 6)/2 iterations to find an optimal policy."
  - Policy sequence (1): π_1 → σ_{1,1} → … → τ_1 → π_2 → … → σ_{n,n−1}.
  - Lemma 4.1 (p.5) proves each step.
  - Intuition (p.5): "The n highest mean-payoff cycles in the graph are the self-loops of t_1 through t_n ... the algorithm 'finds'
    those cycles one after another, taking roughly i iterations to find the cycle at t_i after finding the cycle at t_{i−1}. This
    happens because whenever the next-best cycle is found, all 'progress' the algorithm made so far in the rest of the graph is
    lost."
  - "the vertices keep adding an edge of weight (n + 1)² to the path of their run by including more of the b-vertices (the
    'deceleration lane')".
  - "in the next iteration, all vertices in the deceleration lane ... choose their edge directly to the now-best cycle at t_{i+1}.
    Thus, all 'progress' in the deceleration lane is lost."
- **Per-vertex switches in [ACR] (READING, from the policy families).** Each lane vertex b_k switches a bounded number of times per
  cycle discovery, and there are n discoveries. So switches per vertex are O(n) and the total is Θ(n²): the same profile as
  runquad's reactors.

## 2. runquad against [ACR] (READING)

| feature | [ACR] / [HZ] (Howard, one player, mean payoff) | runquad (N5, R106) |
| --- | --- | --- |
| slow progress | lane: one b-vertex added per iteration ("roughly i iterations") | wave: one reactor b → a per step, m steps |
| global reset | new better cycle t_{i+1} found → all lane vertices jump to it in one iteration | h′ rises → all reactors a → b in one step |
| what the reset event is | a gain change (new cycle) | a P-change of pivot h′ (λ, τ constant; one phase, one REL segment) |
| number of events | n cycles, found in order | K pivot rises, alternating h, h′ |
| total | Θ(n²) | 4K² + 3K − 1 at n = 24K + 6 (≈ n²/144) |
| switches per vertex | O(n) | reactors: 2 per round, O(K) = O(n) |
| what bounds events | number of cycles ≤ ... ([ZY] shows cycles can be exponential for Howard) | pivot rises = Ξ-rises of h, h′ through distinct options (R106 §1: "a pivot climbs through distinct options") |

- **Same.** Lane / wave × reset events, with a one-step global reset caused by a better option at a higher level.
- **Different, and the point for N5.**
  - [ACR]'s resets are gain events, which in N5 would be λ-changes. Those are polynomially bounded on every game (R47 Lemma Φ).
  - runquad's resets are bias events inside one phase. So runquad is not an instance of the published mechanism transported to
    N5. It is its in-phase analogue, which one-player Howard does not have ([ZY] Thm 7.2 proof).

## 3. Beyond n²: what the literature says (PROVED, source)
- **[ZY] Theorem 6.1 (p.23).** "There is a family of deterministic average-reward MDPs with N states and at most four actions per
  state, on which Howard's policy iteration performs at least exp(Ω(N)) iterations from a specified initial policy before any state
  attains its optimal gain."
  - p.23: "It also refutes the conjecture that Howard's policy iteration terminates within M iterations ... (Hansen, 2012,
    Conjecture 6.1.1; Asadi et al., 2025, Conjecture 3.1)."
- **The mechanism ([ZY] §6.1-6.2, p.24-26).**
  - Encoded cycles C_n with means (eq. (6.8)) n/(6d 2^{d+1}), "strictly increasing mean rewards, with consecutive differences
    2^{−d−1}/(6d)".
  - "policy iteration copy[ies] the current encoding b from S_1 to S_2 ... uses the rewards along paths through S_2 to determine which
    bits must flip to form the cycle encoding b+ in S_1".
  - Lemma 6.2: "produces a policy containing the cycle C_n after 3n − 1 iterations".
  - The counter lives in the GAIN (cycle mean). Rewards have O(N) bits ([ZY] p.2).
- **[ZY] Theorem 2.1-2.3 (discounted).** exp(Ω(N)), and exp(Ω(N^{1/4})) even with O(log N)-bit rewards.
  - p.33: "In the discounted construction of Section 4.2, cycles with the same mean reward have strictly increasing discounted values
    along the counting sequence. The positive increments depend on reward timing and tend to zero as γ → 1".
- **[ZY] Theorem 7.1.** Dantzig's coordinated single switch is strongly polynomial on deterministic average-reward MDPs,
  O(N³M² log²(2N)) (T30 §4).
  - §8: "decentralized and simultaneous selfish improvements based on the same policy values can be exponentially slower than
    Dantzig's coordinated single-state updates".
- **[MK] Theorem 1.2.** Howard on DMDPs (discounted, any γ) visits at most nk·u·exp(u) policies, u = O(√(nb log(nb)) + b), b the
  reward bit-size. The method is a threshold discount γ_Q bounded via polynomial roots, plus Ye/Scherrer's γ-dependent bound.
- **[GGK] Corollaries 1-2.** O(n³kα(k)^n) for any PI with arbitrary action selection, and a smaller exponential base for max-gain,
  on DMDPs. Both count path-cycles; Lemmas 7-8 eliminate edges within an equivalence class.
- **Transfer to N5 (READING).**
  - The exponential nesting in [ZY] Theorem 6.1 counts through cycle means. N5's cycle component has ≤ n values ([F] §5 p.8) and λ
    changes are polynomially bounded (R47 Lemma Φ). So that route is closed for N5.
  - [ZY]'s discounted constructions count through "reward timing" of cycles with equal means. That is a discount-specific effect;
    parity valuations have no discount (Friedmann's §9 reduction gives γ near 1, but N5's order is the lexicographic limit).
  - What remains is bias-level counting: path sets under a fixed top, the carries NM (T33 §2.2; P-N5-MPGS (A)). No published
    construction counts there for a two-player symmetric rule. Friedmann's sink-game counters do, but via the hiding that N5 voids
    (T34).

## 4. SW-PER-VERTEX: what an upper-bound argument would look like (READING; CONJECTURE)
- **[ZY] Theorem 7.2's proof (p.33-34), the closest template.**
  - (a) "every N consecutive updates create a new cycle". This is a backward induction over the distance to the end-state cycles:
    "Every state reaches a cycle under π_N within N − 1 transitions, so P_{N−1}(s) = P_N(s)". It is the one-player analogue of R82
    STATIC-DEPTH′.
  - (b) A potential Σ_s J(s) that rises by ≥ 1/N at each cycle creation (eq. (7.12)) and is < N·2^b. Hence O(N³2^b).
- **N5 analogue.**
  - (a) is R82 / R83, which need (H4′_rel). runquad shows the bias stretch is Θ(n²) without it. So (a) must be replaced by a count
    of segment cuts, which is SEG-RUN.
  - (b) needs a polynomial-range potential with a fixed quantum at each cut. Parity's lexicographic order has none in general (Fact
    DELTA: one rank outweighs all lower ones). P-N5-MPGS (A)'s Φ is one, with range ≤ n²/2 and quantum 1, but only at MATCHED
    P-changes.
- **CONJECTURE CUT-Φ (OPEN; stated so that it can be measured).** At every REL cut of a run (a σ̄-change on RO_b or a cycle appearance,
  R83), Σ_{v ∈ V} Φ(P(Ξ v)) rises by ≥ 1 unless some vertex makes a carry at that transition.
  - With P-N5-MPGS (A) per vertex this would give SEG(S) ≤ n·(n²/2)·(NM_max + 1) + (carry transitions). That is poly(n) iff
    carries are.
  - It would bound SEG, not per-vertex switches. SW-PER-VERTEX would then still need switches per vertex per segment = O(1)
    amortized, which LAY §6 shows false per segment (one vertex switches 48 times in one segment).
- **SW-PER-VERTEX itself.**
  - For Howard, per-state switch counts are as hard as iteration counts: exp(Ω(N)) iterations ([ZY] Thm 6.1) force some state to
    switch exp(Ω(N))/N times.
  - For Dantzig's coordinated rule ([ZY] Thm 7.1, Post-Ye) they are polynomial, but only via elimination arguments that need one
    switch per iteration.
  - N5's step is a coordinated arena OPTIMUM (S4a), many switches per step. It sits between the two. No source bounds per-vertex
    switches for such a rule.
  - OPEN. DATA consistent with it: runquad's reactors (O(K) switches each), [ACR]'s lane vertices (O(n) each).

## 5. Not done
- [HZ]'s paper text not opened (Springer empty response; no author copy found). All [HZ] statements above come from the authors'
  slides or [ACR] / [ZY].
- No N5 runs.

## DONE / FINDINGS / NEEDS
- DONE: this note; notebook rows for [HZ] slides, [ACR], [ZY] (re-opened), [GGK], [MK].
- FINDINGS:
  1. runquad = [HZ] / [ACR]'s lane-times-reset skeleton moved from the gain level (new cycle, i.e. a new N5 phase) to the bias
     level (a pivot P-change inside one phase). One-player Howard provably cannot do that ([ZY] Thm 7.2 proof: N updates without a
     new cycle terminate the bias stretch). runquad's in-phase Θ(n²) is a two-frame effect.
  2. Beyond n²: [ZY] Thm 6.1 (2026) refutes Hansen-Zwick's "≤ m iterations" conjecture with an exp(Ω(N)) counter on cycle means. That
     route is blocked for N5: ≤ n cycle-node values ([F] §5) and R47 Lemma Φ. Any N5 nesting must count path sets, i.e. carries.
  3. No published upper-bound argument maps to SW-PER-VERTEX. [ZY] Thm 7.2's template (depth + small-quantum potential) fails on
     parity's exponential weights. Its N5 surrogate is CONJECTURE CUT-Φ (with P-N5-MPGS (A)'s Φ), which bounds SEG, not per-vertex
     switches.
- NEEDS (Lead to route; nothing for the owner):
  - (a) L-COMP or L-SI: measure CUT-Φ (Σ_v Φ rise at REL cuts, carries at those transitions) on the library and on
    runquad_K8_m30_n192.
  - (b) L-RED's deeper-nesting attempt (R106 §5 "OPEN, next") should aim at path-set carries, not cycles. [ZY]'s cycle-mean counter
    cannot be transported.
