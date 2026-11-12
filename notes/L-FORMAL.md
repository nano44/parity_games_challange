# L-FORMAL notebook (Lean formalization lane; branch claude/l-formal; files: lean/, this notebook)

## Resume point
- 2026-11-12T11:57Z (date -u): ALL FIVE STATEMENTS ARE PROVED IN LEAN (lean/lemmas, `lake build` «Build completed successfully (3147 jobs)», 0
  warnings; no sorry / admit / axiom by grep; `lake env lean Axioms.lean`: every theorem ⊆ [propext, Classical.choice, Quot.sound]).
  They are proved as sent to the Lead at 11:44Z (commit 9dde1527); the Lead's statement-diff verdict is still OPEN, so nothing here is
  a result yet (CLAUDE.md: every theorem statement is diffed before it lands). If the diff changes a statement, re-prove that statement.
- Theorems (file: name : statement):
  - PGLemmas/LamGap.lean: `lam_gap_sharp : LamGapSharpStatement V`.
  - PGLemmas/Corollaries.lean: `lam_gap_oneplayer : LamGapOnePlayerStatement V`, `brseg : BrSegStatement V`, `brsegG : BrSegGStatement V`,
    and `brsegG_noH0` (BR-SEG-G (a) with H0 weakened to «every step changes σ at some Even vertex»: the checked proof uses nothing else
    of H0).
  - PGLemmas/OneCross.lean: `one_cross (α) [Preorder α] (F) : OneCrossStatement α F`; `one_cross_vj` (α = node valuations).
  - PGLemmas/Counting.lean (statements in PGLemmas/Statements2.lean, PROPOSED, not yet sent for diff when written): `two_cross`
    (box 100 §2 TWO-CROSS (i), (ii), any preorder), `lam_count` (a ⊴-non-falling sequence of node valuations changes its cycle node
    at most n − 1 times: the Λ part of DEPTH-COUNT3, the per-vertex count behind R118 (i)(b)), `howard_run` (box 101 §3 L1-POLY,
    abstract: T ≤ n(n − 1) + (n(n − 1) + 1)·|Ch| for a Howard run with only Ch moving, given (M)); helper `steps_le_of_breaks`.
  - 2026-11-12T12:36Z: PREMISE (M) IS PROVED IN LEAN FOR ONE-PLAYER GAMES (statements in PGLemmas/Statements3.lean, PROPOSED, need the Lead's diff):
    PGLemmas/Mono.lean `val_mono : ValMonoStatement V` (if every vertex keeps its successor or moves to one of strictly larger value
    under s, then val_s ⊴ val_s′ pointwise: VJ00 Lemma 5.7 / RESULTS R15 (a) when the opponent has no choice); PGLemmas/OnePlayer.lean
    `lam_gap_oneplayer_noM` (LAM-GAP SHARP, one-player, NO premise) and `howard_run_oneplayer` (Howard with VJ valuations on a
    one-player game: T ≤ n(n − 1) + (n(n − 1) + 1)·|Ch|, NO premise). Proof route (Weights.lean + Mono.lean): path sets → integer
    weights wt(M) = Σ ±2^pr (`setLt_iff_wt_lt`; `Nat.geomSum_lt` gives the dominance of the top vertex); keys (wt, signed length)
    compare lexicographically (`Val.le_iff_lex`); `edge_key` (one s′-edge inside a Λ-class) and `telescope` (a walk); `rew_cycle` (a
    cycle of s′ has non-negative weight, so its top beats the old Λ or is it; uses `Function.minimalPeriod` for distinct cycle
    vertices); `prefix_key` (induction on the new prefix length).
  - 2026-11-12T12:44Z: also PROVED (statements PROPOSED, need the Lead's diff): PGLemmas/DepthCount.lean `depth_count : DepthCountStatement V`
    (DEPTH-COUNT3's count of changes of depth in [0, c] with R234's fix D1: ≤ n(S_c(n) − 1) + n(n − 1)S′_c(n) for a non-falling
    sequence of values with lengths < n), `plen_lt_card` (plen < n), `depth_count_val`; PGLemmas/TCyc.lean `tcyc : TCycStatement V`
    (R118 (f) T-CYC and (i)(b), (c) without the genome: T ≤ C + R + (C + R + 1)·|Mov| and C ≤ n(n − 1), given F1).
    Proof notes: `topk pr (c+1) Π` = box 100's P_t; a set change of depth ≤ c raises wt(topk) strictly (`topk_setLt`), deeper ones
    keep topk (`topk_eq`); t ↦ (Λ_t, topk_t) is injective on such steps and misses the heaviest set; length-only steps: t ↦
    (Λ_t, Π_t, len_t or len_t − 1) is injective into n × S′_c × (n − 1).
  - 2026-11-12T12:54Z: TWO-PLAYER F1 = RESULTS R15 (a) LEMMA A IS PROVED IN LEAN (statements in PGLemmas/Statements6.lean, PROPOSED, need the
    Lead's diff): PGLemmas/TwoPlayer.lean `f1 : F1Statement V`: τ an optimal counterstrategy against σ (`OptCounter`: Friedmann §3's
    definition, pointwise ⊴-minimum over Odd's strategies), σ′ arising from σ by improvements ⇒ Ω_σ(v) ⊴ val(σ′, τ′)(v) for EVERY Odd
    strategy τ′, in particular Ω_σ ⊴ Ω_σ′. Also `brseg_opt`, `tcyc_opt` (BR-SEG and T-CYC with «σ̄_t optimal» instead of F1) and
    PGLemmas/OptExists.lean `optCounter_exists` (an optimal counterstrategy exists when every Odd vertex has a successor).
    Route: Mono.lean was refactored around `UnderProgAt pr s u w` (the three under-progress conditions on one edge) and
    `val_le_of_underProg` (VJ00 Lemma 5.5); `underProgAt_of_le` (Ξ(s u) ⊴ Ξ(w) suffices); Dual.lean `val_mono_dual` via the shift
    pr ↦ pr + 1 (`val_shift`: same values; `Val.lt_shift`: reversed order); `underProgAt_of_opt` (if switching u to w does not lower
    the value of u, the edge u → w is under-progressive: else dual (M) makes the value of u unchanged, and (P1) + strict F4′, or the
    empty path set after a cycle node, contradict); `optCounter_exists` by a pointwise-minimal valuation among finitely many strategies.
  - 2026-11-12T13:09Z: DATA (unit: vertex value / pair of values / (Odd strategy, vertex); set: random games n ≤ 8, 3 random Even strategies
    each; tool lean/lemmas/check/crosscheck.py, a Python transcription of Defs.lean, NOT the Lean code): seed 1, 2,000 games: values
    29,823 valdiff 0; pairs 171,723 orddiff 0; optchecks 127,356 optfail 0. Seed 2, 2,000 games: values 30,141 valdiff 0; pairs
    175,539 orddiff 0; optchecks 122,214 optfail 0. Control CTRL=1 (plen read one too long), seed 1, 300 games: valdiff 4,464 of
    4,464 (fires). Reading: the definitions as written denote si.py's valuation and order, and si.py's σ̄ is an `OptCounter`.
  - lean/lemmas/INDEX.md: the table lane text ↔ Lean statement ↔ Lean theorem ↔ remaining premise.
  - 2026-11-12T13:22Z: fresh `git clone --depth 1 --branch claude/l-formal` of origin (HEAD 4b376da457ddb2aed895c56f101c5a86d233f766), then
    in lean/lemmas `lake exe cache get` (exit 0), `lake build` (exit 0, «Build completed successfully (3149 jobs)», 0 warnings),
    `lake env lean Axioms.lean` (exit 0, 13 theorems, axioms ⊆ the allowed three), grep sorry / admit / axiom: nothing. 101 s in all.
  - PGLemmas/Example.lean: `Example.window_example` (4 vertices, Ch = {1}, a window 0..1: the hypotheses hold together and b − a = |Ch|).
  - PGLemmas/VJ00.lean: `vj00Le_iff` (VJ00 §4.2's order as printed = `Val.le` on play values), `val_proper` (every val is a play value).
- How the SHARP proof goes in Lean (LamGap.lean), for whoever edits it:
  - `SPath pr edge Ch ℓ v S x c` (inductive): a simple path v → … → ℓ with vertex set S, value x = value(P), c = choice vertices before ℓ.
    `SPath.count_eq`: c + [ℓ ∈ Ch] = |Ch ∩ S|, so c ≤ |Ch| and c + 1 ≤ |Ch| when ℓ ∈ Ch.
  - `ext_le_val`: inside ONE state σ, x ⊴ val(σ v) with top(x) ≠ v ∉ set(x) gives ext(v, x) ⊴ val(v) (cycle-node case by rewards, other
    case by (P1) + F4′). This one lemma serves both the fixed-vertex and the choice-vertex case of (L).
  - `lower_bound` = (L): induction on k, inside it induction on the SPath derivation; the choice-vertex case uses Howard at a + k − 1,
    then (M), then `ext_le_val` at time a + k (never ext of an old value: box 101's point).
  - `play_spath` = (U): induction on plen; `val_le_of_play` = (L) + (U) with the two count bounds.
  - `lam_gap_sharp`: Ch.card = m + 1 (else nothing moves); x ∈ Ch switches at a + m + 1; u = old successor is strictly below w = new
    one at a + m + 1; x a top → `hback` (values of u, w equal at a + m and a + m + 1) contradicts Howard at a + m; x not a top →
    `hconst` (all values equal at a + m + 1 and a + m + 2) and strict F4′ give val(x) ◁ val(x).
- Next: (1) apply the Lead's diff verdict on all statements (Statements.lean sent 11:44Z; Statements2.lean sent 12:26Z; Statements3-6
  and OptCounterExistsStatement to send); (2) whatever the Lead routes next (L-NEW 72's Lemma LEVEL if it survives). Not formalized
  and needing R104 / R117's genome definitions: WINDOW, SCC-RED, CAP, REACH3. Not formalized, generic: R15 (b), (c) (the φ potential and
  strictness), VJ00's Ω_σ as a minimum over plays (the Lean `OptCounter` is Friedmann's positional form).
- Layout rule: no lean/lakefile.* at lean/ root (Lead 11:31Z: «keep lean/lakefile.* absent at lean/ root»).
- Toolchain in a fresh container: commands in lean/lemmas/README.md (elan, `lake exe cache get`, `lake build`); tested on a fresh copy.

## Queue
0. (own initiative, proposed to the Lead) TWO-CROSS, Λ-count, Howard run bound, (M) one-player, premise-free one-player LAM-GAP and
   Howard bound, DEPTH-COUNT3 with fix D1, T-CYC without the genome: all PROVED in Lean; every statement needs the Lead's diff.
   Two-player F1 = R15 (a) and the existence of optimal counterstrategies: PROVED in Lean; statements need the Lead's diff.
   Not done: WINDOW, SCC-RED, CAP (they need R104 / R117's genome definitions).
1. LAM-GAP, SHARP form, with BR-SEG and BR-SEG-G as corollaries: PROVED in Lean as sent; waits for the Lead's statement diff.
2. ONE-CROSS: PROVED in Lean as sent (abstract over a preorder, plus the VJ instance); waits for the Lead's statement diff.
3. Possible later (Lead 11:31Z, not yet): L-NEW 72's CANDIDATE Lemma LEVEL, if it survives L-RED.

## Sources opened
- [VJ00] Vöge, Jurdziński, «A Discrete Strategy Improvement Algorithm for Solving Parity Games», BRICS RS-00-48 (Dec 2000),
  https://www.brics.dk/RS/00/48/BRICS-RS-00-48.pdf, pdf sha256 485a12de432a2a8c88640b0718bd2042d855fa86d6a82092a0d538fd41ba9e65 (the
  sha256 RESULTS R15 names). Opened 2026-11-12, read by pdftotext:
  - §2.2 (cycle-domination games): V = {1, …, n} ordered by ≤ (the relevance order), partitions (R+, R−) and (M⊕, M⊖); a play ends at
    its first repeated vertex; λ(P) = the ≤-largest vertex of the play's cycle.
  - §4.1 (play values): Prefix(P) = the vertices before λ(P); π(P) = Prefix(P) ∩ V_{>λ(P)}; #(P) = |Prefix(P)|; Θ(P) = (λ(P), π(P), #(P));
    (1) PlayValues ⊆ {(v, (B, k)) : B ⊆ V_{>v}}.
  - §4.2 (the order): Reward(v) = −v on R−, v on R+; v ⪯ w iff Reward(v) ≤ Reward(w); B ≺ C iff MaxDiff(B, C) ∈ (B∖C) ∩ R− or
    ∈ (C∖B) ∩ R+; ⪯_ℓ compares B ∩ V_{>ℓ}; (B, k) ⊴_ℓ (B′, k′) iff B ≺_ℓ B′, or B =_ℓ B′ and (ℓ ∈ R− and k ≤ k′, or ℓ ∈ R+ and
    k′ ≤ k); (ℓ, (B, k)) ⊴ (ℓ′, (B′, k′)) iff ℓ ≺ ℓ′, or ℓ = ℓ′ and (B, k) ⊴_ℓ (B′, k′). «(1) guarantees that ⊴ is a linear order
    on PlayValues. It is a linear pre-order on V × ℘(V) × N.»
  - §4.4 (improvement, Switch_I, eq. (2)); §5.1 (4)-(10) (path values as shortest paths; (8) Π_σ(ℓ) = (∅, 0)); Lemma 5.7 (σ ⊑ Improve(σ)),
    read only as far as R15 (a) cites it. Not re-derived by me: (M) / F1 enters the Lean statements as a hypothesis.
- [Fr] Friedmann, «An Exponential Lower Bound for the Latest Deterministic Strategy Iteration Algorithms», arXiv 1106.0778 (LMCS 7
  (3:19) 2011), https://arxiv.org/pdf/1106.0778, pdf sha256 46c96f44775aa2b07cad20912cb325b177e38c94cb2e40297df66b6047679611. Opened
  2026-11-12, read by pdftotext:
  - §2: «W.l.o.g. we assume Ω to be injective».
  - §3: rew(v) := Ω(v) if Ω(v) ≡₂ 0, −Ω(v) otherwise; relevance v < u :⟺ Ω(v) < Ω(u); reward ordering v ≺ u :⟺ rew(v) < rew(u);
    the play π = v₁ … v_k (w₁ … w_l)^ω with v₁ = v, vᵢ ≠ w₁ (1 ≤ i ≤ k), Ω(w₁) > Ω(w_j) (1 < j ≤ l); node valuation
    ϑ := (w₁, {vᵢ > w₁ | 1 ≤ i ≤ k}, k); M ≺ N :⟺ M △ N ≠ ∅ and max_<(M △ N) ∈ ((N ∩ V⊕) ∪ (M ∩ V⊖)); (u, M, e) ≺ (v, N, f) :⟺
    (u ≺ v) or (u = v and M ≺ N) or (u = v and M = N and e < f and u ∈ V⊖) or (u = v and M = N and e > f and u ∈ V⊕). Lemma 3.1,
    Theorem 3.2 ([VJ00]) read as statements only.
  - The Lean definitions (PGLemmas/Defs.lean) encode THIS form, line by line, as RESULTS R118's premise line says («in Friedmann arXiv
    1106.0778 §3's form (si.py)»). On play values (path component ⊆ V_{>cycle node}, VJ00 (1)) it is VJ00 §4.2's order: the filter
    ∩ V_{>ℓ} does nothing there. That equivalence is now a Lean lemma: PGLemmas/VJ00.lean `vj00Le_iff` with `val_proper`.
- Fleet texts read as inputs (not sources): claude/l-si 23d39400 docs/si/box101-lamgap.md §2; claude/l-red 0148d73f
  docs/red/R234-lamgap.md §0, §2, §3; claude/l-red docs/red/R231-onecross.md §2; trunk docs/RESULTS.md R118 (l. 13607 ff.), R17
  (l. 730 ff.), R15 (l. 624 ff.); docs/new/P-N5-XICYC.md §1-§5 and P-N5-XICYC-fixes.md l. 30-60 (F4′, STRICT-G, PATH-G).

## Dead ends
- None yet. (One trap met, not a dead end: inside `namespace PG` a theorem named `Val.lt_irrefl` shadows Mathlib's `lt_irrefl` in its
  own body, and `Val.lt_trichotomy` even failed with «fail to show termination»; the root lemmas are written `_root_.lt_irrefl`, …)

## Things only I know
- Proxy: github.com HTML pages and codeload.github.com return 403; git reads of public repositories, GitHub release assets,
  releases.lean-lang.org, cache.mathlib.org, arxiv.org and www.brics.dk returned 200.
- Mathlib v4.35.0 «is designed for use with the module system»: a plain (non-module) file importing it gets one Lake warning per
  import. lean/lemmas/lakefile.toml sets `allowNonModules = true` on the library, which removes the warning (Lake's own opt-out).
- The gate takes about 41 minutes in this container (experiments/si/check.sh about 20 of them): batch commits, one push at a time.
- Design choices in Defs.lean worth knowing: (1) a state is ONE map s : V → V (a positional pair read as one successor map), so the
  one-player lemma and the two-player corollaries share one valuation; (2) `lam` is chosen by Classical.choose among the cycle's
  vertices of largest priority, unique once `pr` is injective (a hypothesis of every statement, not of the definitions); (3) the
  statements are `def … : Prop`, and each theorem will have exactly that type, so the diffed text cannot drift from the proved one.
