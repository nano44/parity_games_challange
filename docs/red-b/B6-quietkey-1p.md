# B6: QUIET-KEY-1P (O1), second independent kill attempt by the cross-domain route (L-RED-B successor 4) — first attempt: three classical exponential constructions do not embed, and why
Written 2026-11-13 (date -u in the commit). Brief (Lead 09:08Z, relaying the owner «So put everything into trying solving it today»):
«move to B6, the second independent kill attempt on QUIET-KEY-1P (O1): N5's key rule on L-NEW's one-player model 1P(G) (claude/l-new
box 217; e-index keys per L-RED R241). Method, different from L-RED 69's hand construction: cross-domain, per D18. Treat the key rule as
a pivot rule on a deterministic one-player problem, a lexicographic shortest-path / reachability structure. Look for an embedding of a
KNOWN exponential construction for a related rule … Open and cite only sources you actually read … Then test the embedding on one217.py
and n5v. A super-polynomial family, or a clean reason why such embeddings fail for this rule, comes to me at once.»
D18 (owner, verbatim): «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of
mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly,
and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.»
LABELS: PROVED (lane, unrefereed) / DATA / READING. O1 and G-N5-TIME stay OPEN. No kill is claimed.
ASSUMPTION (stated per D18): box 217 and one217.py are NOT on any origin branch (09:12Z: every remote branch searched). Until they
are, «the key rule on a one-player model» is read as the IDEAL model of RESULTS R104 on Ξ-acyclic genomes and its 2-wide-ladder class
𝓛^R_d (R110, R113, as quoted in docs/lower/P-TOWER-FUEL.md §1 at claude/l-lower 4285c9a5), which box 216 §1.4 names as QUIET-KEY's
sub-window model («a one-player lexicographic path game … box 212 RF-D's "generalised O1"»). Tests on one217.py are owed.

## 1. The model read as a pivot rule (READING, from the landed definitions quoted in P-TOWER-FUEL §1)
- States: one option per mover; movers sit on levels of an acyclic Ξ-graph whose plays end at the exit X. In 𝓛^R_d there are 2 movers
  per level, each with 2 options, option k of a level-l mover leading to mover 2(l − 1) + k. A strategy is a vertex of the cube
  {0, 1}^(2d).
- Values (R105 ENC): «the value of option (x, k) is ε(x, k) plus the current value of its Ξ-target», ε(x, k) = ±2^rank, distinct ranks.
  So a mover's value is an ADDITIVE path weight. Comparisons are lexicographic by top rank, as in a lexicographic shortest path.
- The rule (R104 IDEAL; R113 ALIGN): A-sets (current + strictly better) under the old state; then, level by level lowest first, each
  mover takes the key-least option of its A-set under the new state, keys read root first. ALIGN: on 𝓛^R_d both movers of level l prefer
  the same option c_l(s), the key-smaller member of the pair below; a mover moves only to c_l, and only when that option is strictly
  better (P-TOWER-FUEL Lemma 0). So it is a SIMULTANEOUS, PER-STATE, INDEX-type rule: every state with an improving action switches, but
  the action it takes is fixed by a key order that is independent of the values, not by the size of the improvement.
- The two orders: the improving set comes from the VALUE order (additive, lexicographic by rank); the choice comes from the KEY order
  (root-first lexicographic by e-index). A long run needs the two to disagree for a long time: each move raises the mover's value
  (PATH-RISE) and lowers its key (KEY-TAU (ii), R241).

## 2. Lemma ACYC-GREEDY (L-RED-B, PROVED here, unrefereed): value-greedy rules are fast on acyclic one-player games
Setting. A one-player parity game in which every cycle is the self-loop of one sink c, and every vertex reaches c. Let h be the largest
number of edges of a path to c, and Ξσ the SPEC S1 valuation of σ (the optimal counterstrategy is trivial). A run σ_0, σ_1, … is
VALUE-GREEDY if, at every step and every vertex v, Ξσ_(t+1)(v) ⊵ max over successors w of (v prefixed to Ξσ_t(w)).
**Claim.** Every value-greedy run reaches an optimal σ by step h. In particular this holds for Howard's switch-best rule, and for
N5's S4a whenever the arena values are the true values (the S4a arena contains Howard's choice: a best successor is current or strictly
improving).
Proof. With node c fixed, Ξ is an additive path weight (R105 ENC for the path set; the length term at the lowest significance, with sign
by the parity of c). Let opt(v) be the optimum and ht(v) the largest number of edges from v to c. Induction on k: after step k every v
with ht(v) ≤ k has Ξσ_k(v) = opt(v). For k = 0 this holds at c. Step k ≥ 1: let w* be an optimal successor of v, so ht(w*) ≤ k − 1, and
Ξσ_(k−1)(w*) = opt(w*). Then Ξσ_k(v) ⊵ v prefixed to Ξσ_(k−1)(w*) = opt(v) ⊵ Ξσ_k(v). ∎
DATA (experiments/red-b/b6acyc.py, data/b6/b6acyc.out): random one-player games with a single sink loop (vertex v > 0 points to lower
indices only; 25 % Odd pass-through vertices), N5 n5v spec and xi from S3. Must-0: viol (I > h), wrong (regions vs harness Zielonka).
seed 11, 1,000 games, n ≤ 12, out-degree ≤ 3: viol 0 / 0, wrong 0, max I 2, max h 8. seed 12, 500 games, n ≤ 40, out-degree ≤ 6:
viol 0 / 0, wrong 0, max I 4, max h 15. seed 13, 200 games, n ≤ 80, out-degree ≤ 8: viol 0 / 0, wrong 0, max I 5, max h 20. CONTROL
(must fire): single-switch Bland from the same start is not value-greedy. Its step count exceeds h on 0 of 1,000 (n ≤ 12: the control
does not fire there), 85 of 500 and 116 of 200 games. So the control fires on the two larger strata.
Consequence for embeddings. On the acyclic one-player model, an exponential run must come from rules whose choice is not value-greedy.
N5's key rule is not, because on Γ3 the S4a arena values are flat (W3-ALL, quoted in R241 §1: «every option of a level-ℓ mover has
arena value (c_W, ∅, 5ℓ + 4) … and TIE(x) = A(x)»), so the key decides. Every construction that defeats a greedy rule only through
cycles (§3 (c)) is out.

## 3. Three known exponential constructions and why they do not embed (sources opened; DATA where run)
- (a) Bland's rule as a single-switch counter: Disser, Loho, Maat, Mosis, «Lower bounds for ranking-based pivot rules», arXiv
  2512.16684v2 (PDF sha1 8629b38e63b8eac6e0ec231a3c02cfd59664d0e7), Lemma 4.4 and Fig. 4.1: on the sink parity game G_n «Strategy
  improvement with Bland's rule takes 2^n − 1 iterations». Built exactly as the proof of Lemma 4.4 lists it (experiments/red-b/
  b6gn.py) and run with N5 (n5v spec and xi, from S3 and from the paper's σ0). DATA (data/b6/b6gn.out, n = 1..32, |V| ≤ 66): I = n − 1
  from S3, n from σ0, both modes, k = 0, wrong 0 on all 40 runs. Why: the doubling in Lemma 4.4 needs ONE switch per iteration («Bland's
  rule prefers the edges from a1, it switches (a1, b2) first»); a rule that switches every improvable state at once performs the
  counter's lower bits in parallel. The paper's own scope: its rules apply «a single switch in each iteration» (§2, «we only consider a
  version of this algorithm that applies a single switch in each iteration»). Theorem 4.3 there covers only such rules.
- (b) The same paper's Theorem 1.1 / 4.3 (superpolynomial for every «ℓ-index-based» rule with o(m / log m) memory states): its rules
  choose ONE improving edge from the ranks of the improving edges. N5's key rule switches at every mover with an A-set and ranks
  options by whole root-first PATH keys, which depend on the current choices below, not only on the improving edge's own rank. It is
  outside the class as defined (READING; Definition 3.1 / 4.x were read only as far as the theorem statements quoted here).
- (c) Howard's rule on deterministic MDPs: Zhong, Ye, «Policy Iteration Is Not Strongly Polynomial for Deterministic Markov Decision
  Processes: The Price of Algorithmic Anarchy», arXiv 2609.40147v2 (PDF sha1 72974eb240042b53930e073fee2e97cfa9c04167), Theorem 2.1
  («There is a family of deterministic discounted MDPs with N states and at most two actions» on which Howard's policy iteration takes
  exp(Ω(N)) iterations) and Theorem 6.1 (average reward; «The instances have strongly connected transition» graphs). The counter value
  is stored in CYCLES («The selected paths form a cycle from s0 through s1, …, sd and back to s0», Iteration 3 «form the new cycle»). On
  an acyclic one-player model Howard is value-greedy and ends within h steps (§2), so this mechanism has nothing to act on.
So the three classical routes fail for clean reasons. (a), (b): single switches. (c): cycles plus a greedy rule. What remains is a
SIMULTANEOUS per-state index rule on an acyclic additive DP. That is exactly R113's PAIR-DOUBLE regime, F(l) ≤ 2F(l − 1) + 2, met with
equality up to l = 6 by HIT7 (NOW M4 row: «HIT7 F(6) = 254 at d 28»). I found no published lower bound for that class in what I opened.
The arXiv queries tried (09:14Z): «policy iteration» + «acyclic»; «Bland» + «policy iteration»; «strategy improvement» + «index» +
«lower bound»; «shortest path» + «policy iteration» + «exponential». Only (a)'s paper and arXiv 2309.14034 (single switches, not
opened) matched.

## 3a. Probe of the remaining class: SIMUL-BLAND on acyclic one-player games (DATA; experiments/red-b/b6simul.py, data/b6/b6simul_wave1.out)
SIMUL-BLAND: every Even vertex with an improving edge (SPEC S2) switches at once to its LOWEST-INDEX improving successor. It is the
simplest simultaneous per-state index rule, not N5. Hill climb of its step count from S3 over acyclic one-player games (all vertices
Even, out-degree ≤ 3, one sink loop), 5,000 candidates per n. Best steps at n = 8, 12, 16, 24, 32: 5, 6, 11, 7, 11, each with h = 7,
8, 13, 11, 12 and N5 (spec) I = 4, 6, 9, 3, 6 on the same game; wrong 0. Random local search does not find runs above h. Long runs of a
simultaneous index rule need DESIGNED structure. The natural one has two vertices per level whose values leapfrog (each level's
option values must overtake each other F(l − 1) + 1 times, and values only rise), and that is the pair structure of 𝓛^R_d. This is
where HIT7 lives and where L-LOWER's SAT search works. READING: I see no cross-domain shortcut past it in the sources opened.

## 4. Not claimed; next
- Not claimed: anything about box 217's 1P(G) or one217.py (not on origin); any bound for the key rule.
- Box 217 landed at 09:53Z (Lead): claude/l-new a32a588dfe92ae581d2be9928d89b7afaf44a5a5, docs/new/N5-QUIETKEY-box217.md (1P(G) §1,
  A1-A6 §5) and experiments/new/box217/one217.py. Its A6 names the exact open step: the ENUMERATION DEPTH k(G) (the largest k with a
  level-(k − 1) mover switching |K| − 1 times); QUIET-KEY-1P ⟺ k(G) = O(log N) (conjecture ENUM-LOG); towers reach k = 7 (HIT7, d = 28).
  The Lead's target for this lane: k = 8 by a designed carry chain, or a timing reason why 8 is impossible. §1-§3a here are consistent
  with box 217's model (keys by e-index ε, values additive along the Ξ-DAG, KEY rule level by level). The §3 embeddings were not re-run
  on one217.py (owed: G_n has no genome form; ACYC-GREEDY is box 217's HOWARD control, which A2-type bounds already cover).
- Next (B6 attempt 2, for the successor): a constructive, cross-domain doubling for simultaneous index rules on 2-state-per-stage acyclic DPs (a
  Gray-code / carry-chain design on the per-level automaton of §1), tested on n5v and, when available, one217.py.
