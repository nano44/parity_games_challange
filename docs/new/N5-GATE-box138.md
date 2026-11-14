# Box 138 N5-GATE: no polynomial gate potential is needed inside acyclic stretches, and none exists for what is left; σ̄ changes are not a separate currency (Theorem CASC-M‴); odxi_n37's 5 gate changes are paid by cascade height; the c-world SI is neither a known easy nor a known hard case
L-NEW successor 47, 2026-11-01 (date -u: see the commit). Lead GO 22:06Z (box 138: attack GCH with gate potentials). Labels: PROVED (lane),
CONJECTURE, READING, DATA, DEAD, OPEN. G-N5-TIME stays OPEN. Not a TARGET.md claim.
Premises and notation: P-N5-ANCHOR (f009a9a1) §1-§2; box 134 CYC-MONO; box 135 Lemma MERGE (with its persistence step) and Theorem
CASC-M; L-RED R184 Lemma SELF-FREE (b) (claude/l-red 2799b309); box 137 (docs/new/N5-REL-box137.md: CEIL on [PW], SAT-MONO, C-WORLD,
DEFICIT, KCH-GCH). One more premise, [OPT-ODD]: at every state s, σ̄_s(o) is a ⊴-minimal successor of o in o ⊕ Ξ_s(·) (VJ00 §5.1,
shortest-path characterisation, equations (6)-(10); opened, notes/L-NEW.md «Sources opened»), read off a play that does not pass o.

## 0. Answer
- The lexicographic potential (|SAT|, BAND values) does not work as stated:
  - SAT is never spent (0 saturation events in every corpus FL run, box 137).
  - The BAND values have exponential range.
- The poly-range monotone quantities that exist are |SAT| (≤ n events per run, SAT-MONO) and the cycle-node vector
  CYC_s := (rew-rank of the cycle node of Ξ_s(v))_v. CYC is non-decreasing coordinatewise and changes ≤ n(n − 1) times per run (CYC-MONO).
  - Every gating change that changes a cycle node strictly raises (|SAT|, CYC). Those are ≤ n(n − 1) + n per run.
  - The remaining gating changes are of two kinds: same-cycle-node Ξ changes at gates (box 134's FVCH) and σ̄ changes. NO poly-range
    potential raised by them was found, and none is needed inside acyclic stretches:
    - FVCH-type changes are not stretch boundaries at all; CASC-M / CASC-M″ pay them by cascade height.
    - σ̄ changes need not be boundaries either (Theorem CASC-M‴, §2, PROVED lane under (NT), (NC)): σ̄_s is a function of σ_s, so
      an Odd vertex adds no delay to the cascade.
- odxi_n37's 5 changes at gate 33 (box 133) are charged to the cascade:
  - its whole FL run (8 transitions) is ONE stretch, D″-acyclic and D‴-acyclic, Even-height 9;
  - each change of Ξ(33) keeps the cycle node (20) and is a MERGE-order change caused by a move on a pre-merge segment (vertex 2's
    side, box 135 §0);
  - by CASC-M, those moves are part of the ≤ 9-step settling. No gate potential is involved.
- Corollary (PROVED lane): FL run ≤ n_E · (1 + n(n − 1) + CNMOV), provided every S-stretch (cut only at cycle-node changes and W-cycle-node
  moves) has acyclic D‴ and (NT), (NC) hold. This drops SBCH from box 135's bound n_E (1 + SBCH + n(n − 1) + CNMOV).
- What is left of «GCH» is exactly: (1) cyclic dependency digraphs inside stretches, and (2) CNMOV.
  - D‴-cycles observed are Even–Odd 2-cycles x ↔ o (cwmov2_n57; one climb mutant). Box 136's refinement (z-world + DOM) removes them on
    cwmov2_n57 for D″. Combining that refinement with the Odd edges is OPEN.
- c-world (§3, READING with opened sources): with σ̄ fixed, the c-world FL face is one-player strategy improvement on a static-weight
  total-cost game under [RULE] (κ-least among improving tight options, all vertices at once). Fearnley's polynomial bound covers only
  the greedy all-switches rule, so it does not apply. Single-switch one-player SI is exponential (CDAG_n, box 130). The two-player
  exponential lower bounds (Friedmann) are for other rules. So the c-world is neither a known polynomial case nor a known hard case.
  Inside D‴-acyclic stretches it settles in ≤ n_E steps anyway.
- DATA (813 distinct pairs + pins): §4. σ̄ changes are frequent and harmless in the climbs: up to 125 inside one FL run of 4 transitions
  (sbmany_n57), SBMAX 4, 89 returns of σ̄ to an earlier choice. No climb lengthened an FL run by σ̄ changes.

## 1. The poly-range part (PROVED, lane)
- Lemma GATE-LEX. On an FL run, Φ_s := (|SAT_s|, CYC_s) is non-decreasing (lexicographically and coordinatewise). It changes ≤ n + n(n − 1)
  times. Every state s at which the cycle node of Ξ changes at some vertex raises Φ strictly.
  - Proof. SAT-MONO (box 137). CYC: by VJ, Ξ_(s−1)(v) ⊴ Ξ_s(v), and values compare by the reward of the cycle node first, so the reward
    is non-decreasing. A change is strict, and there are ≤ n − 1 strict steps per vertex (CYC-MONO). ∎
- Consequence: gating changes that change a cycle node (at an ODIFF vertex or at a W-cycle node) number ≤ n(n − 1) per run. The other
  gating changes keep every cycle node, and Φ does not see them.
- READING. A poly-range potential for same-cycle-node Ξ changes would have to rank path sets rel_w(·) below a fixed ceiling, and the
  weights are ±2^rank. No such ranking with polynomially many values is known to the lane. The route taken instead is §2: do not count
  these changes, but show that a cascade absorbs them.

## 2. Theorem CASC-M‴ (PROVED, lane, under (NT) and (NC))
- S-STRETCH: a maximal set of consecutive transitions of an FL run whose states have the same cycle node of Ξ at every vertex, and at which
  no W-cycle node moves. σ̄ may change inside, unlike box 135's stretches.
- D‴ (union over the states s of the S-stretch):
  - box 135's D′ edges without self-edges (R184 SELF-FREE (b)). Even x ∉ CN → every Even v ≠ x on the pre-merge segments Y′, Z′ of
    every pair y, z ∈ T_x ∪ {σ_s(x)} with equal Ξ_s-cycle node, and → the Even vertices on the W-key paths of x's options;
  - x → every Odd vertex on those segments;
  - for every Odd o reached this way: o → every vertex ≠ o on the pre-merge segments of every pair of successors of o with equal
    Ξ_s-cycle node.
- Hypotheses:
  - (NT) at every such o and state s, the ⊴-minimal successor of o in [OPT-ODD] is unique;
  - (NC) no vertex lies on the Ξ_s-play of one of its own successors before that play's cycle node (no corner).
- Even-height h(u) := the largest number of Even vertices on a D‴-path starting at u (u included). H := max over Even x ∉ CN.
- Claim: if D‴ is acyclic, no Even vertex moves after the S-stretch's H-th transition, so the S-stretch has ≤ H ≤ n_E transitions.
- Proof. Let a be the first state. By induction along D‴ (acyclic) we show P(u): σ_s(u) (Even u) or σ̄_s(u) (Odd u) is constant for
  s ≥ a + h(u) (Odd: h counts only the Even vertices below u).
  - Segments persist. Suppose every vertex that lies on a segment of a pair (p, q) at some state is constant from state t on. Then the
    plays from p and q run through the same segments to the same merge point m at every s ≥ t. Follow each play vertex by vertex: every
    vertex before m is constant. After m the common path cannot re-enter the segments before w (MERGE persistence: the cycle node is
    fixed). By MERGE, the order of p and q is then constant from t. Pairs with different cycle nodes compare by the (constant) cycle nodes.
  - Odd step. Let all D‴-successors of o be constant from t. Then o's preference order over its successors is constant from t. By
    [OPT-ODD], (NT) and (NC), σ̄_s(o) is that order's unique minimum, so it is constant from t. There is no delay, because σ̄_s is
    computed from σ_s at the same state.
  - Even step. Let all D‴-successors of x ∉ CN be constant from t. At a transition j with j − 1 ≥ t:
    - the orders on T_x ∪ {σ_(j−1)(x)} used by R_j(x) are constant (segment persistence; Odd vertices on the segments are
      successors);
    - the κ_j-keys are constant (W-key edges);
    - bridge B and [RULE] (with (R1)) give σ_j(x) = f_x(σ_(j−1)(x)) with a fixed f_x, which is idempotent as in the packet's §4.
    So x is constant from t + 1.
  - Base: a vertex all of whose successors are Odd (with only Odd vertices below them) is constant from a (Odd) or a + 1 (Even).
    Induction gives P(x) at a + h(x). ∎
- Corollary FL-CASC‴. If every S-stretch of an FL run has acyclic D‴, and (NT), (NC) hold, then FL run ≤ n_E (1 + CYCCH + CNMOV) ≤ n_E
  (1 + n(n − 1) + CNMOV).
  - Proof: S-stretches are cut only by cycle-node changes (≤ n(n − 1), CYC-MONO) and W-cycle-node moves. ∎
- Relation to box 135/136: SBCH (σ̄-change boundaries) disappears. The price is a larger digraph: Odd edges are added, while
  box 136's z-world and DOM refinements are not (yet) applied.
- OPEN: D⁗ := D‴ with box 136's z-world / DOM cuts. The observed D‴-cycles are 2-cycles x ↔ o in which o lies on x's option segment and
  x lies on an option play of o. This is the Odd analogue of self-feeding, which box 136's C-STATIC-Ξ handles for Even x in x's own
  z-world.

## 3. The c-world as a known problem (READING; sources opened in notes/L-NEW.md «Sources opened»)
- By box 137 DEFICIT, in the c-world Ξ(y) = W(y) minus the first gate's deficit, and Even's improving moves are exactly the deficit-
  decreasing tight switches. With σ̄ fixed this is one-player strategy improvement (minimiser) on a total-cost game with static integer
  edge costs:
  - an Odd deviation from τ(A) to s costs wt(W(τ(A)).rel) − wt(W(s).rel), and lengths likewise;
  - the minimiser's arena is the layered tight DAG plus the fixed Odd jumps;
  - the switching rule is [RULE]: every switchable vertex switches at once, to the κ-least improving option.
- Known polynomial cases do not cover this rule:
  - Fearnley (arXiv 1705.02313 v1, §4 «One-player strategy improvement», Lemma 3): O(|V||E|) for the ALL-SWITCHES greedy one-player rule
    only, citing Cochet-Terrasson-Gaubert; adaptive subsets and non-greedy choices are not covered.
  - VJ00 Prop. 7.4 (one-player parity games, O(n³) improvement steps) is stated without proof (RS-00-48 p. 36).
- Known hard cases:
  - single-switch one-player SI is exponential (CDAG_n, box 130: 2^n − n − 1);
  - Howard's rule on deterministic mean-payoff MDPs has «best known upper bound exponential» (Asadi-Chatterjee-de Raaij, arXiv
    2506.12254, abstract);
  - two-player strategy iteration (Odd best-responding, which is the c-world with σ̄ = BR(σ)) is exponential for VJ-type rules (Friedmann,
    arXiv 1106.0778, LMCS 7(3:19)). Hansen-Miltersen-Zwick (arXiv 1008.0530) is strongly polynomial only for a constant discount factor,
    and «exponential for non-discounted» games.
  - None of these lower bounds is for [RULE] on a layered tight arena with W constant.
- So: no reduction either way. The structural facts that matter are CASC-M / CASC-M‴ (acyclic dependency ⇒ ≤ n_E settling), not the
  game class.

## 4. DATA
Tools (experiments/new/box138/): dmerge3.py (S-stretches, D‴, Even-height, CASCVIOL, TIES for (NT), SBIN, SHOWCYC=1); rel.py (box 137's
checker plus σ̄-change counters SBCH / SBTOTAU / SBFROMTAU / SBOTHER / SBRET / SBMAX); climb138.py (MODE=sb: score 10^6 SBMAX + 10^3 SBRET
+ SBCH); runcorp.sh; pincheck.sh.

| set | S-stretches | FL in them | D‴ acyclic / cyclic | CASC-M‴ viol. | max Even-height | σ̄ changes inside | (NT) ties |
| --- | --- | --- | --- | --- | --- | --- | --- |
| corpus, 813 distinct pairs (E-1) | 10 | 29 | 10 / 0 | 0 | 18 | 1 | 0 |
| odxi_n37 (box 133) | 1 | 8 | 1 / 0 | 0 | 9 | 0 | 0 |
| u23sw64_n32 | 1 | 8 | 1 / 0 | 0 | 9 | 0 | 0 |
| odxi_many_n32 (R179) | 3 | 8 | 1 / 2 | 0 | 8 | 0 | 0 |
| cwmov2_n57 (box 137 pin) | 2 | 6 | 1 / 1 (6 ↔ 11) | 0 | 7 | 1 | 0 |
| sbmany_n57 (this box, pin) | 1 | 3 | 1 / 0 | 0 | 9 | 95 | 0 |
- The corpus S-stretches coincide with box 135's stretches (same 10 / 29; CNMOV 13 cut out).
- odxi_many_n32's two cyclic S-stretches are box 135's cyclic stretches (without self-edges: R184's 2-cycles of movers). They are acyclic
  under box 136's D″ (z-world + DOM), which this tool does not apply (§2 OPEN).
- Climbs MODE=sb (4 cores, stopped by hand once FL had stopped growing; no timing claim): seed 5 from cwmov2_n57: SBCH 75, SBMAX 2, FL 2;
  seed 6 from cnmov_k8_n57: SBCH 125, SBRET 89, SBMAX 4, FL 4; seed 7 from odxi_n37: no improvement; seed 8 from cw11_n24: SBCH 38,
  SBMAX 2, FL 2. No lemma check fired (LEMMAVIOL 0). Logs: box138/out/s5-s8.log. One mutant (seed 5, cyclic 20 ↔ 27) has (NT) TIES 1, in
  its cyclic stretch.
- Pin sbmany_n57.pg (sha1 8db15610e0a8…, start sbmany_n57_default.start 017aee8398d4…). Default start written out by start_pair,
  strict start check. Oink 8fbf0a7 --zlk and --tl verified, regions agree (pinwin), n5b identical state by state. FL run of 4: 125 σ̄
  changes (55 to τ, 55 from τ, 15 other), 4 epochs (GCH 3, all σ̄), one S-stretch of 3 transitions, D‴-acyclic, Even-height 9.
  box138/pincheck.txt; check.sh «box 138 GATE».

## 5. Status
- PROVED (lane): GATE-LEX (§1); Theorem CASC-M‴ and Corollary FL-CASC‴ under (NT), (NC) (§2).
- READING: §1 (no poly ranking of path sets known), §3 (c-world: no reduction to a known easy or hard case; sources opened).
- OPEN: D⁗ (z-world / DOM cuts together with Odd edges); CNMOV.
- DATA: §4. CONJECTURE: none new.
- G-N5-TIME: OPEN. Residual of the FL face: cyclic D⁗ (if any) and CNMOV.
