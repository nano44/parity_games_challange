# R2-P-IDEAL-M2: second-referee report on packet P-IDEAL-M2 (L-NEW successor 51, box 156)
REFEREE-2 successor 27 (Opus 5.5, D12/D19). Written 2026-11-04 07:32Z (date -u). Independent: docs/referee/ not read before this push.

## Object
- claude/l-new 6bcfa0de. docs/new/P-IDEAL-M2.md sha1 bc47b06c4b8d90ceb28939c966083e0c057a442b, 171 lines (re-hashed: match).
  docs/new/P-IDEAL-M2-line-L1.txt sha1 0160d1e3ffa832536454a74c559b20280b87f53e, 1 line (re-hashed: match).
- DEAD instance: experiments/new/box156/ext/max_d4_L13.json at 6bcfa0de sha1 f0735b61312bdbfe1bb553496d7e9ee38681dcee = claude/l-red
  46588929:experiments/red/r197/lag/max_d4_L13.json (same sha1; byte-identical copy).

## Verdicts
| § | statement | verdict |
| --- | --- | --- |
| §1 | Lemma MULTI-CHARGE (U ≤ M₂, T ≤ N (1 + M₂); any degree) | **SIGN** (Opus 5.5, D12) |
| §1 | Corollary M2-EQ | **SIGN** (Opus 5.5, D12) |
| §1 | Corollary SINGLE-SHORT | **SIGN** (Opus 5.5, D12) |
| §2 | Lemma TRIGGER (a)-(c), degree ≤ 2 | **SIGN** (Opus 5.5, D12) |
| §3 | Lemma XIFLIP, degree ≤ 2 | **SIGN** (Opus 5.5, D12) |
| §3 | Corollary MIN-FLIP, degree ≤ 2 | **SIGN** (Opus 5.5, D12) |
| §4 | DEAD LIN-156 (T part) by max_d4_L13 | **SIGN** (Opus 5.5, D12): recomputed T 13 > ⌊3·8/2⌋ = 12 with my own simulator |
| line | L-1 | **REQUIRED** M2-L1, M2-L2 (exact word changes below); optional P-1 to P-3 |
No gap in any proof. Gaps list: EMPTY.

## Premise route (only landed RESULTS; nothing from docs/lit)
- R104 (docs/RESULTS.md l. 9864): only the definition of the IDEAL model. Packet §0 checked against R104's text: N movers, levels,
  M := Σ deg(x) options, W-target one level down (none at level 0), Ξ-target a mover or X, distinct β-rank with parity, distinct gate index,
  start; Ξ-value = set of β on the chain up to the first Ξ-target X; comparison by the β of largest rank in the symmetric difference,
  even = better; step: least key «gate indices of the chain of W-targets under the new state, lowest level first» among the current option
  and the strictly better ones; stop «when nothing is available or nothing changes». §0 states the same model (key = W-chain gates
  root-first, then the own gate; keys read s_t below lev(x) only). MATCH. No R104 theorem is used anywhere.
- R105 (docs/RESULTS.md l. 10155), each quote grepped verbatim in the landed statement:
  - XI-NEW «for t ≥ 2 every least-level mover h of step t moves to an option w ∉ A_(s_(t−2))(h)»: verbatim.
  - RISE «that option's value rose strictly at step t − 1, and some strict Ξ-descendant of h on its chain under s_(t−2) moved at step
    t − 1»: verbatim.
  - CHAIN-BACK «T ≤ N (1 + U) with U the number of unchained steps t ∈ [2, T]»: verbatim.
  - ENC «the Ξ-order of β-sets is the order of the integers Σ ±2^rank»: verbatim (prefix). (Only asymmetry of ▷ is used; that also
    follows from the definition directly.)
  - LOCAL «an option's value depends only on the states on its chain», «a key only on the states below its level»: verbatim.
  - KEYFLIP «moves(x) ≤ 1 + KF_x with KF_x the number of steps at which KP(x) changes»: verbatim; degree ≤ 2 hypothesis respected.
  - Not used: MONO, U-EQ, DECREMENT, EXACT-ENERGY, TOP-MONO, RANK-BOUND, INTERVAL-*, RECURSION, R106, docs/lit. Confirmed by reading every
    proof step.
- Definition of CHAINED: the packet adds «(as a mover other than h_t)». The landed R105 statement reads «h_(t−1) lies on the chain under
  s_(t−2) of the option h_t takes» without it; the governing P-IDEAL-RED packet (docs/new/P-IDEAL-RED.md l. 118-119) has it, and
  CHAIN-BACK (i) π(h_t) < π(h_(t−1)) needs it. Either reading is safe here: the literal reading makes fewer steps unchained, so U_lit ≤
  U_packet ≤ M₂ and MULTI-CHARGE's per-step claim holds for the smaller set too. h_(t−1) = h_t occurs (DATA: 54 times on the box-150
  random runs, 1,286+1,050+910 on my degree-3/4 climbs, 0 at degree 2 in my runs). Optional P-1.

## Proof check, step by step
### MULTI-CHARGE (hyp.: IDEAL-ACYC, any degree, any width)
1. t ∈ [2, T], h = h_t least-level mover of step t, w = s_t(h_t): XI-NEW + RISE apply (t ≥ 2). ✓
2. RISE gives a strict Ξ-descendant z ≠ h_t on the chain of (h_t, w) under s_(t−2) with z ∈ Mv_(t−1): Z_t ≠ ∅. ✓
3. Mv_(t−1) = {h_(t−1)} ⇒ Z_t = {h_(t−1)} ⇒ h_(t−1) on that chain, ≠ h_t ⇒ chained (packet definition = R105 packet definition). ✓
4. Contrapositive; t ↦ t − 1 injective into [1, T − 1] with |Mv_(t−1)| ≥ 2 ⇒ U ≤ M₂. ✓ CHAIN-BACK ⇒ T ≤ N (1 + U) ≤ N (1 + M₂). ✓
### M2-EQ, SINGLE-SHORT
- M₂ counts a subset of [1, T − 1]: M₂ ≤ max(T − 1, 0). (⇒) M₂ ≤ T; (⇐) T ≤ N (1 + p(N + M)), a polynomial in N + M. ✓
- SINGLE-SHORT: hypothesis is exactly M₂ = 0; then T ≤ N. ✓ (T = 0 trivially.)
### TRIGGER (hyp.: degree ≤ 2)
- deg(z) = 2 since a degree-1 mover never moves (A is a singleton). ✓ Keys of the two options of z are distinct (own gate distinct, same
  length), so «<» is a strict total order on them. ✓
- (a) Case s_(t−2)(z) = o: A_(s_(t−2))(z) = {o, o′}, step t − 1 picks the key-least under s_(t−1), = o′, contradicting s_(t−1)(z) = o. ✓
  Case s_(t−2)(z) = o′: z moved o′ → o at t − 1, needs Ξ(z, o) ▷ Ξ(z, o′) under s_(t−2), contradicting the unflipped Ξ(z, o′) ▷ Ξ(z, o)
  by asymmetry. ✓ Step t − 1 exists since t ≥ 2. ✓
- (b) LOCAL: if no mover y ≠ z of the two chains under s_(t−2) is in Mv_(t−1), both chains and values are the same under s_(t−1). ✓ The
  first changed mover on an s_(t−2) chain is also on the s_(t−1) chain (identical prefix), so (b) holds for chains under either state. ✓
  Chain movers after z are reached by Ξ-edges: strict descendants. ✓
- (c) LOCAL (keys read levels < lev(z) only). ✓ Negative remark «(c) gives a second mover of lower level in Mv_t, so |Mv_t| ≥ 2»: true
  (the lower-level mover is ≠ z); my counter VIOL_TRIG_note 0.
### XIFLIP, MIN-FLIP (hyp.: degree ≤ 2)
- Consecutive moves a < b alternate o → o′ → o (two options, no move in between). At a: Ξ_(s_(a−1))(x, o′) ▷ Ξ_(s_(a−1))(x, o); at b the
  reverse under s_(b−1). σ differs at s_(a−1), s_(b−1) ⇒ a flip at some j ∈ [a, b − 1] ⊆ [1, T]; disjoint intervals. ✓
- MIN-FLIP: XIFLIP + KEYFLIP. XF bound: values of x's options read only strict descendants (LOCAL + acyclicity). KF bound: keys read only
  levels < lev(x) (LOCAL). ✓ Negative remarks (no bound on XF, KF) are statements of non-claim: correct.
### DEAD LIN-156
- Conjecture text checked at l-new 4047aacf docs/new/N5-M2-box156.md l. 34-35: «for every IDEAL-ACYC genome of degree ≤ 2 with N movers and
  every start, T ≤ ⌊3N/2⌋ and M₂ ≤ N + 1.» Packet §4 quotes it verbatim.
- Instance checks (own code): Ξ-graph acyclic and xorder a topological order; β indices 0-15 each used once; ranks distinct; gates
  distinct; W-targets exactly one level down (none at level 0); every mover degree 2.
- My simulator (below), written from R104's text with β-SETS (no ENC), keys under the NEW state, level by level:
  «N 8 T 13 M2 5 U 4 Mv [1, 1, 2, 1, 1, 2, 3, 2, 1, 1, 2, 1, 1]» = packet §4 exactly. 13 > 12: the T part of LIN-156 is FALSE. ✓
  M₂ = 5 ≤ N + 1 = 9: the packet's remark that the M₂ part is not killed is correct.
- Control NEG=1 (keys under the OLD state): T 7, Mv [3, 3, 1, 1, 1, 1, 1], VIOL_MULTI 1, VIOL_TRIG_a 1: the result depends on the R104 rule.

## Machine checks (own tool docs/referee-2/R2-P-IDEAL-M2/m2_check.py; lane code not imported)
- Lane block re-run at 6bcfa0de (worktree, experiments/new, «P-IDEAL-M2» block of check.sh incl. pin105), 07:30Z: both lines PASS, exit 0.
- My simulator on the same inputs reproduces the lane's totals exactly:
  - 54 corpus runs: steps 468, U 222, M₂ 300; degree-2 moves at t ≥ 2: 919, XiT 707, WT 333 (= lane TRIG line). 0 violations.
  - box150/out/rand, every start for N ≤ 8 (ALLN=8): runs 34,934, steps 38,676, U 2,148, M₂ 5,188 (= lane MCHARGE line). 0 violations.
  - the 93 degree-≤-2 random genomes, every start (all N ≤ 10): runs 3,981, moves 298, XiT 298, WT 0 (= lane TRIG line). 0 violations.
- Beyond the lane: hill-climbs (mutating ranks, parities, gates, start) from the 54 corpus genomes: 32,400 runs (max T 26), WT 130,319
  events; from 60 random ladder genomes of degree 3-4: 72,000 runs. Random genomes: 6 batches plain + 6 ladder (102,770 runs). Counters
  checked per run: MULTI-CHARGE per step, U ≤ M₂, T ≤ N(1 + M₂), CHAIN-BACK, M2-EQ, SINGLE-SHORT (M₂ = 0), TRIGGER (a), (b) and its
  descendant clause, (c) and its |Mv_t| ≥ 2 remark, XIFLIP, KEYFLIP, XF ≤ #descendant-moving steps, KF ≤ #lower-level-moving steps.
  All 0 violations. Note: the lane's random DATA has WT 0, so TRIGGER (c) is exercised only by the corpus (333) and my climbs.
- DATA precision: the lane's «single_runs 6114 … T / N ≤ 1.0» counts runs with every step 1..T single-mover, a subset of SINGLE-SHORT's
  hypothesis (steps 1..T − 1); my M₂ = 0 counter covers the full hypothesis (0 violations). Not a line issue.

## TARGET.md diff
- TARGET §2 (M4): a deterministic algorithm solving every parity game within p(n + m) steps. No statement of the packet mentions a parity
  game, an algorithm or running time; all are about IDEAL-model step sequences (R104's definition). No M4 / M3 claim, no gauntlet step.
  The packet's §5 diff is correct. G-N5-TIME stays OPEN.

## Line L-1: clause by clause
- Premises, model, acyclic, any width, T, Mv_t, U «of R105», M₂ with range t ∈ [1, T − 1]: MATCH §0.
- MULTI-CHARGE, M2-EQ, SINGLE-SHORT: MATCH §1 (ranges bound: «unchained step t ≥ 2», «steps 1, …, T − 1»).
- TRIGGER: MATCH §2 (a)-(c) in substance (P-2, P-3 optional). XIFLIP: MATCH; XF_x defined in the line.
- MIN-FLIP: MATCH except binders (M2-L1).
- DEAD: MATCH §4 (N 8, degree 2, T 13, sha1). L43: the killed statement is universal and finite (not asymptotic); the instance numbers are
  in the line. OK.
- Scope tail: MATCH §1-§5 «Does NOT claim» lines and §5 excluded list.
- DATA tail: M2-L2.
### REQUIRED
- M2-L1 (binders). KF_x and moves(x) are not defined in the line (R105's line defines KF_x; this line only bounds it). Replace
  «(MIN-FLIP) moves(x) ≤ 1 + min(KF_x, XF_x), with XF_x» by
  «(MIN-FLIP) moves(x) ≤ 1 + min(KF_x, XF_x), with moves(x) the number of steps moving x, KF_x R105's number of steps at which KP(x)
  changes (KEYFLIP), XF_x».
- M2-L2 (DATA). «on 34,934 / 3,981 all-start random runs» is not exact: the 34,934 runs use every start only for the 192 genomes with
  N ≤ 8 and the genome start for the other 8 (packet §5; I counted 8 genomes with N 9-10). Replace by
  «on 34,934 random runs (every start for N ≤ 8) and 3,981 all-start degree-≤-2 random runs».
### Optional
- P-1: «U the number of unchained steps of R105» → «… of R105 (h_(t−1) on the chain as a mover other than h_t)» (the landed R105 statement
  omits the parenthesis that its packet has; harmless here, see Premise route).
- P-2: TRIGGER «on one of their chains» → «on one of their chains under s_(t−2)».
- P-3: TRIGGER «caused by» (twice) → «and then … moves» wording: the packet proves existence of such a mover, not causation.

## Signatures
All seven statements: SIGN (Opus 5.5, D12), REFEREE-2 successor 27, 2026-11-04 07:32Z (date -u). Gaps: none. Line L-1: REQUIRED M2-L1, M2-L2.
