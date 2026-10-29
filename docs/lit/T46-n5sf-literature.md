# T46: N5-SF in the literature: the closest known rules, their lower bounds, and the constructions that make the opponent's best reply change (SBC)
L-LIT successor 3 (Opus 5.5), D18. Lead's message 15:19Z: «identify N5-SF in the literature. "Even's one-player optimum within the
improving arena, against Odd's best reply to the CURRENT σ, simultaneously with the mirror for Odd". Is it a known rule? ... Which
exponential lower bounds are known for the closest match, with theorem numbers? Above all, which constructions make the OPPONENT's best
reply change often (SBC)?» Written 2026-10-29 from 15:20Z (date -u). Working note, unrefereed. Not a TARGET.md claim; CONJECTURE SF-POLY
(L-NEW, docs/new/N5-SF-box54.md) stays OPEN. Labels: SOURCE (opened; notebook "Sources opened") / PROVED (L-LIT, unrefereed) / DATA /
READING / NOT OPENED. N5-SF = claude/l-new 057a08eb experiments/new/box54/n5sf.py (sha1 1ea3bdc7), MODE=x; SBC as in its §1 (σ-changes at
which σ̄ changes). Tool: docs/lit/T46-backedge-sbc.py (read-only on n5sf.py and si.py).

## Summary
- No opened source defines N5-SF's rule. The closest published things, each differing in one stated point (§1):
  (a) Schewe's SWITCH-BEST / Friedmann's I^glo: the same arena, but the choice is evaluated with the NEW counterstrategy (G|σ′,τ′),
      N5-SF's with the OLD one (G|σ′,τ). Friedmann's thesis names exactly this difference as the place where his gadget lives (§1 (a)).
  (b) PGSolver's never-registered "strategy improvement by counterstrategy" (strimprbyco, since the 2013 initial commit): improving
      arena, choice from a valuation against Odd's current best reply, but PER VERTEX and with Even best-responding over ALL edges (§1 (b)).
  (c) Fearnley's non-oblivious (snare-based) SI: N5-SF's stale frame makes every profitable back edge look like a closed winning cycle,
      so N5-SF acts like FixSnare inside one step (READING, §1 (c)); this is the mechanism Fearnley shows defeats Friedmann's families.
- Lower bounds: for (a) Friedmann LMCS Thm 8.4 / thesis Thm 4.50 (switch-best, H_n), which does NOT transfer (T45, L-NEW: linear on
  H_n); for (b) none known; for (c) Friedmann, "A superpolynomial lower bound for strategy iteration based on snare memorization",
  Discrete Applied Mathematics 161(10-11) 1317-1337 (2013), DOI 10.1016/j.dam.2013.02.007: NOT OPENED (publisher only; not on arXiv);
  its game family IS available as PGSolver's generator friedmannsubexp («Friedmann's Subexponential Lower Bound for snare-based rules»),
  not yet ported in this repo (experiments/hard-families/pgsolver-binary-diff.md l.14).
- SBC sources (§2): (i) Fearnley Prop. 14: switching a profitable back edge forces the opponent's best reply onto an escape (an SBC
  event); DATA: on switchbestexp N = 2..5 and H3, EVERY N5-SF step with an Even back-edge switch changed σ̄ (3/3, 7/7, 14/14, 23/23, 6/6);
  (ii) the remaining SBC steps have no back-edge switch and their share grows with N (1, 4, 12, 26 of 4, 11, 26, 49). Friedmann's simple
  cycle (thesis §4.3) is the gadget for (i); the snare-memorization family is the published construction that defeats a rule which
  closes snares eagerly — the natural kill target for SF-POLY.

## 1. Candidates, one by one
### (a) Schewe's optimal improvement = SWITCH-BEST = I^glo (and its relation to N5-SF)
- SOURCE. Friedmann PhD thesis (LMU 2011, edoc 13294, sha256 68748f53…), §4.2 Table 4.2 (printed p.94): SWITCH-BEST [Sch08] «Apply the best
  possible combination of switches», conjectured/proved lower bound 2^Ω(n) (Friedmann); §4.6.2 (p.139-140): «it holds for every non-empty
  applicable subset of improving switches I that Ξσ[I] ⊴ Ξσ*»; Thm 4.45 ([Sch08], polynomial computation); Thm 4.50 (printed p.149): SWITCH-BEST
  needs ≥ 2^n steps on H_n. LMCS version: arXiv 1106.0778 v2 §4, Thm 8.4 (T44 §1).
- The point of difference, in the source's own words (thesis §4.3, printed p.101): «Consider a strategy σ, an improved strategy σ′, and
  the corresponding optimal counterstrategies τ and τ′ ... if we consider G|σ′,τ, i.e. the game conforming to the improved strategy σ′ and
  the old counterstrategy τ, it might be the case that we encounter intermediate cycles. Such intermediate cycles need to have dominating
  cycle nodes that give a better reward to player 0, as player 1 denies staying in these cycles with τ′». And: «The main gadget that is used
  to enforce exponentially many iterations in every lower bound construction, exploits intermediate cycles, and is called the simple cycle
  gadget» (Fig. 4.4, p.102).
- PROVED (L-LIT, unrefereed; from the definitions). I^glo maximises Ξσ′ = val(σ′, τ′) over the arena (τ′ = σ̄(σ′)); N5-SF maximises
  val(σ′, τ) with τ = σ̄(σ) fixed. Since τ′ is Odd's optimal reply, val(σ′, τ′) ⊴ val(σ′, τ) for every σ′, with equality iff τ is still an
  optimal reply to σ′ at every vertex's valuation. So N5-SF's objective is an upper bound ("optimistic") of I^glo's, exact where σ′ creates
  no intermediate cycle that τ would stay in. T45 gave the first state where the two choices differ (dlm1 n = 2, state 0).
- READING. N5-SF is SWITCH-BEST evaluated in the frame Friedmann's gadget exploits: it sees the intermediate cycles as wins. That is why
  H_n (built to make I^glo postpone closing cycles) does not slow it.

### (b) PGSolver's "strategy improvement by counterstrategy" (strimprbyco)
- SOURCE. github.com/tcsprojects/pgsolver @ d3cd624 (git clone, read only): src/lib/solvers/stratimpralgs/switch_locally_best.ml,
  function improvement_policy_by_counterstrategy (l.21-45): «let tau = winning_strategies game node_compare (Array.make n (-1)) valu in let
  valutau = evaluate_player1_strategy game node_compare tau in ...» then at each Even vertex i: among successors j with valu(j) ⪰
  valu(σ(i)) (improving or equal), take the maximum by valutau; switch only if strictly improving in valu; if nothing switches, fall back to
  improvement_policy_optimize_all_locally (switch-all). winning_strategies (stratimpralgs.ml l.136-145): Odd's locally best decision under
  valu at Odd vertices whose cycle node is Odd's, −1 elsewhere. evaluate_player1_strategy: the valuation of that Odd strategy on the dual
  game, i.e. with Even best-responding. Registration is commented out (switch_internal.ml l.490-494, «"strimprbyco" "sibc" "use strategy
  improvement by counterstrategy"»); git log -S: present since f2ea8b0 (2013-06-07, initial commit).
- Difference from N5-SF: per-vertex choice (no one-player optimum over the arena), Even's evaluation unrestricted (best reply over all
  edges, not over the arena), Odd's strategy only on Odd's region. Same idea: improving arena + choice against Odd's current best reply.
  No lower bound or analysis known; it is dead code.

### (c) Fearnley's non-oblivious (snare-based) strategy improvement
- SOURCE. Fearnley, "Non-oblivious strategy improvement", arXiv 1003.2976 v1 (LPAR-16, 2010), pdf sha256 7ac44213b8d8d633…: Def. 2 (Max
  snare (W, χ): χ winning on G↾W), Def. 3 (escapes), Theorem 4 (a winning τ uses an escape from every snare), Def. 10 (strategy tree T_σ =
  T_{σ,br(σ)}; (v, u) profitable is a BACK edge iff u ∈ Subtree_σ(v)), Def. 11 (critical set), Prop. 12 («The strategy σ[v ↦ u] is winning for
  every vertex in G↾C»), Prop. 14 («There is some edge (x, y) in Esc(Critical_σ(v, u)) such that br(σ[v ↦ u])(x) = y»), Prop. 15, Alg. 1
  FixSnare, Prop. 16 (≤ |W| iterations), §8.2 (p.12-13): on Friedmann's families «the policies Augment(All) and Augment(Optimal) would close
  the cycle again after a single iteration ... both of our policies terminate in polynomial time on Friedmann's examples».
- READING (not proved). Against the stale σ̄(σ) (= br(σ)), Prop. 12 says σ[v ↦ u] wins the critical set: in N5-SF's frame a profitable back
  edge in the arena closes an Even-winning cycle, the best possible valuation, so N5-SF's one-player optimum takes such edges (or another
  win on that set). Prop. 14 then forces br to change: an SBC event. So N5-SF behaves like a snare-eager rule that re-closes a snare as soon
  as its back edge is improving again — the behaviour Fearnley shows makes Friedmann's families polynomial. DATA consistent with this:
  L-NEW's linear counts on H_n and DLM (N5-SF-box54.md §5); §2 below.
- Lower bound for snare-based rules: Friedmann, DAM 161 (2013) 1317-1337, DOI 10.1016/j.dam.2013.02.007 (title and pages from Crossref
  metadata; NOT OPENED: publisher only, no arXiv copy; theorem numbers unknown). Canavoi-Grädel-Rabinovich arXiv 1210.2459 v1 abstract
  (opened, T14) lists «switch-all (also with Fearnley's snare memorisation)» among rules with Friedmann-type super-polynomial bounds.
  The family: PGSolver src/lib/generators/policyiter/generators/friedmannsubexp.ml (90 lines, ident "friedmannsubexp"; also
  fearnleysubexp.ml, «Subexponential Lower Bound for Fearnley's rule», 86 lines). Neither is ported (pgsolver-binary-diff.md l.14).

### (d) Others checked, not matching
- STV symmetric SI (arXiv 1501.06484, T40 §1): Even switches only to σ^c_τ edges (best reply to Odd's CURRENT strategy τ), not a one-
  player optimum against σ̄(σ). With τ := σ̄(σ) its candidate set would be Iσ ∩ σ^c_{σ̄(σ)}, i.e. single edges of N5-SF's unrestricted
  target; N5-SF takes the arena optimum instead. DLM's bounds (T44 §2) need τ to be a separate, slowly moving strategy, so they do not apply.
- Naive alternation / Pollatschek-Avi-Itzhak / Hoffman-Karp with unrestricted best replies (T40 §2): N5-SF's step is Even's best reply to
  σ̄(σ) CUT to the improving arena; without the cut this is the naive scheme that cycles. The cut (Ξ arena) is what keeps it monotone.
- Björklund-Vorobyov (DAM 155 (2007), T12 sources): single/multiple local switches with the counter-player's optimal response;
  no one-player optimum step. Not a match.

## 2. Which constructions make the opponent's best reply change often (SBC)
- Mechanism 1 — closing a snare (Fearnley Prop. 14; Friedmann's simple cycle, thesis §4.3 p.102-104: «If player 0 decides to use the edge
  (d1, e1), i.e. to move into the cycle, then player 1 will use as counterstrategy the escape edge (e1, h1) ... if player 0 decides to use an
  edge going out of the cycle, it might be the case that player 1 decides to use the edge (e1, d1)»). Every close and every re-open of a
  simple cycle flips Odd's choice at e1. Friedmann's counters (G_n, H_n, switchbestexp) open and close cycle i about 2^(n−i) times under
  their target rule; under N5-SF they are closed early (READING (c)), so this mechanism alone gives SBC ≈ number of cycle (re)openings,
  which the counter structure no longer drives.
- DATA (T46-backedge-sbc.py over n5sf.py trace(); switchbestexp = experiments/hard-families/pgsolver_port.py switchbestexp N, sha1 N = 2..5:
  b3d5bc29, e1cd8f13, 57b27b74, 84913ba8; H3 = f7bdd38a, F start c552ac0d):
  | game | n | N5-SF iterations | SBC | steps with an Even back-edge switch | of which σ̄ changed | SBC steps with no back-edge switch |
  | --- | --- | --- | --- | --- | --- | --- |
  | switchbestexp N = 2 | 60 | 58 | 4 | 3 | 3 | 1 |
  | switchbestexp N = 3 | 85 | 135 | 11 | 7 | 7 | 4 |
  | switchbestexp N = 4 | 110 | 258 | 26 | 14 | 14 | 12 |
  | switchbestexp N = 5 | 135 | 364 | 49 | 23 (25 switches) | 23 | 26 |
  | H3, F start | 63 | 64 | 8 | 6 | 6 | 2 |
  Iterations and SBC match L-NEW's switchbestexp table (58, 135, 258, 364; 4, 11, 26, 49). On H3 I count 64 iterations with trace(); L-NEW's
  §5 formula 7n + 49 gives 70 at n = 3: Lead to reconcile (different n? different count?), not mine to edit.
  So: every back-edge step is an SBC step (Prop. 14 seen in data, 53/53), and the non-back-edge SBC steps are the growing part.
- Mechanism 2 — escape SELECTION changes (READING, from the data): Odd's best reply also changes when Even's cross-edge switches change
  WHICH escape is best (Friedmann's lanes and selector nodes; DLM Observation 8: «As long as σ(a_j) = a_{j+1}, we have σ̄(d_j) = d_1», i.e.
  Odd's reply at d_j reads Even's choice at a_j). These are the 1, 4, 12, 26 steps above. A construction for SF-POLY's kill has to drive
  this mechanism (or snare re-openings) exponentially often while N5-SF's optimistic step cannot pre-empt it.
- Published construction aimed at exactly the eager-snare behaviour: Friedmann DAM 2013 (NOT OPENED) / PGSolver friedmannsubexp. Its title
  says super-polynomial ("subexponential" in PGSolver's description) — not exponential.

## 3. For the adversary (READING; priorities)
1. Port PGSolver friedmannsubexp.ml and fearnleysubexp.ml (d3cd624) with the pgsolver_port.py conventions, check them against the OCaml
   binary if one can be built, and run N5-SF on them from PGSolver's start (initial_strategy_by_best_reward) and from the generator's
   intended start. This is the one published family built against a rule that closes snares eagerly. (L-COMP owns ports; L-LIT can
   transcribe if asked.)
2. Target Mechanism 2: make σ̄ change through escape selection (DLM-style coupling, σ̄(d_j) reading σ(a_j)) rather than through snare
   closing, because N5-SF neutralises snare re-closing (every back-edge step is an SBC step only once per closure).
3. Open the DAM 2013 paper if the owner provides access (NOT OPENED here: the publisher fetch was refused in this session).

## DONE / FINDINGS / NEEDS
- DONE: this note; T46-backedge-sbc.py; opened Fearnley 1003.2976 v1, Friedmann thesis §4.2-4.3, 4.6.2 (re-opened), PGSolver d3cd624
  stratimpralgs sources and generator list. DAM 2013: Crossref metadata only.
- FINDINGS:
  - No published rule equals N5-SF. Closest: I^glo evaluated with the OLD counterstrategy (thesis p.101's «intermediate cycles»); PGSolver's
    dead strimprbyco (per-vertex cousin); Fearnley's snare-based SI (behavioural match, READING).
  - PROVED (unrefereed): N5-SF's step objective is an upper bound on I^glo's (optimistic), equal unless an intermediate cycle forms.
  - SBC: every N5-SF back-edge switch changed σ̄ (53/53, Fearnley Prop. 14); the growing part of SBC on switchbestexp is non-back-edge.
  - Kill target: Friedmann's snare-memorization family (DAM 2013; PGSolver friedmannsubexp), unported, paper not opened.
- NEEDS: none from the owner (optional: access to DOI 10.1016/j.dam.2013.02.007).
