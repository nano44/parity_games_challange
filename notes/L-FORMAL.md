# L-FORMAL notebook (Lean formalization lane; branch claude/l-formal; files: lean/, this notebook)

## Resume point
- 2026-11-12T13:54Z (date -u): HANDOVER STATE. Everything proved so far is «Lean-checked (lane)»: the Lead ACCEPTED every statement (rulings 11:49Z,
  12:29Z, 13:13Z, quoted in lean/lemmas/README.md «Status and reading rules»); they become RESULTS only through CHECKER + the Lead's CI
  job for lean/lemmas (he owns .github/ and will name the job). lean/lemmas/INDEX.md is the table of statements and theorems.
- OPEN TARGET (Lead 13:13Z): «NEXT TARGET: box 208's ABSTRACT core … 1. State in Lean the abstract LEVEL potential theorem (§10's
  form). Send the statements for a diff first, as before. 2. If it goes well, state PLATEAU in the abstract one-player form it reduces
  to. Your BR-SEG-G / LAM-GAP theorems should do most of the work. Defining the genome and IDEAL-CYC in Lean comes later and only if §10
  goes through.» Source: claude/l-new 8db300fe docs/new/N5-LEVEL-box208.md (§10 l. 373-400; §3 Lemma LEVEL l. 120-181; §4 l. 183-197;
  Addendum A PLATEAU l. 402-500, NOT yet read by me).
  - DONE for step 1: PGLemmas/AbsStatement.lean = definitions (`SPGame`, `SPGame.edge`, `SPGame.PathW`, `SPGame.d : ℕ∞`,
    `SPGame.HowardAt`, `SPGame.NoZeroCycle`) and `AbsStatement` (a `def … : Prop`). It builds. NOT PROVED. Sent to the Lead for the
    statement diff; his verdict is open. My three deviations from §10's wording: (i) hypothesis `G.tgt ∉ G.Max` (§10 does not say who
    owns the target; with a Max target Bellman's equation fails there); (ii) weights in ℕ, d in ℕ∞; (iii) clause (2) is stated for
    EVERY step t < T (§10: «every step before the last one»); under my encoding every step of the run changes the state, and then the
    last step raises a front value too (argument below).
  - ALREADY PROVED towards it (PGLemmas/Abs.lean, builds): (B1) `SPGame.d_le_of_path`, `path_of_d_eq`, `d_tgt`, `d_le_edge`,
    `exists_edge_eq`, `d_max`; (K1′) `SPGame.d_le_step`. Still to do: (K5′), (A), (F), (L3), (L4), (L1), (C) below.
    ℕ∞ hints that worked: split on `G.d s v = ⊤`, else `obtain ⟨k, hk⟩ := ENat.ne_top_iff_exists.mp h` (hk : ↑k = d); `gcongr`
    for `↑w + a ≤ ↑w + b`; `push_cast; rfl` for `↑w + ↑k = ↑(w + k)`; `zero_le` takes no explicit argument; `dif_pos` / `dif_neg`
    are deprecated names (`dite_eq_left` / `dite_eq_right`), like `if_pos` / `if_neg` (`ite_eq_left` / `ite_eq_right`).
  - PROOF PLAN for `AbsStatement` (mine, from §10 and §3; write d_t := G.d (s t), reference state T):
    (B1) Bellman facts from the `Nat.find` definition: d_s(tgt) = 0; for every edge (v, u) of the s-graph d_s(v) ≤ w(v, u) + d_s(u)
    (cons a path); for v ≠ tgt with d_s(v) < ∞ some edge has equality (invert the least path: `cases` on `PathW`); so for a Max z
    (z ≠ tgt by hypothesis, s z ∈ E z) d_s(z) = w(z, s z) + d_s(s z).
    (K1′) d_t ≤ d_(t+1) pointwise: induction on a `PathW (s (t+1))` path, using at a Min vertex the Bellman inequality in the old graph
    and at a Max vertex Howard's «best» clause plus (B1). (K5′) d_(t+1)(z) ≥ w(z, y) + d_t(y) for every y ∈ E z, z Max.
    (A) every t < T lags somewhere: the step changes s at a Max z; «keeps» fails, so some y ∈ E z has w + d_t(y) > d_t(z); by (K5′)
    d_(t+1)(z) > d_t(z), and d_T ≥ d_(t+1). (So there is no value-flat step at all in this model.)
    (F) LAG_t := {v | d_t v ≠ d_T v} (then d_t v < d_T v, so d_t v is finite); m_t := the least lagging value; FRONT_t := the lagging
    vertices of value m_t. A front vertex of Min's has a best edge of weight 0 into the front (a non-lagging end would pin it by
    Bellman at T). A front vertex z of Max's whose edge s_t z lags has that edge of weight 0 into the front.
    (L3) so some Max z ∈ FRONT_t has s_t z not lagging (else the front maps into itself along weight-0 edges: pigeonhole on iterates
    gives `Relation.TransGen` v v, against `NoZeroCycle`), and m_t = w(z, s_t z) + d_T(s_t z): one value per Max edge.
    (L4) no stall: if every front vertex kept its value, map Max z ↦ s_T z (by (K5′) at y = s_T z: w + d_t(y) ≤ d_(t+1)(z) = m <
    d_T(z) = w + d_T(y), so y lags, w = 0, y ∈ FRONT) and Min o ↦ its best edge: again a weight-0 cycle. So some front vertex rises:
    clause (2).
    (L1) LAG only shrinks, m never falls, at equal m the front only shrinks: Φ_t = (m_t, −|FRONT_t|) rises strictly at every step.
    (C) t ↦ (m_t, |FRONT_t|) is injective on t < T into {w(z, y) + d_T(y) : z Max, y ∈ E z} × {1..n}: T ≤ (#Max edges)·n. Clause (1).
    Lean advice: do the order facts on ℕ∞ with `WithTop` case splits (lagging values are finite, `ENat.coe_toNat`); reuse the
    pigeonhole from Defs.lean `exists_cycleNode` (`Finite.exists_ne_map_eq_of_infinite`) and the injective-map counting from
    DepthCount.lean (`Finset.card_le_card_of_injOn` into a product). Expect 400-600 lines.
  - Step 2 (PLATEAU, abstract one-player form): read Addendum A first; the Lead expects `lam_gap_sharp` / `brsegG_noH0'` to carry it.
- Committed together with this notebook (2026-11-12T14:30Z, after push.sh of 91a29b88 ended with exit 0): README.md, INDEX.md
  (Lead's wording rulings applied), PGLemmas/Statements7.lean + NoH0.lean (`BrSegGNoH0Statement`, `brsegG_noH0'`),
  PGLemmas/AbsStatement.lean, PGLemmas/Abs.lean, PGLemmas.lean, Axioms.lean, this notebook.
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
00. OPEN: prove `AbsStatement` (box 208 §10) after the Lead's diff; then PLATEAU's abstract one-player form (Lead 13:13Z).
0. (accepted by the Lead 12:29Z / 13:13Z) TWO-CROSS, Λ-count, Howard run bound, (M) one-player, premise-free one-player LAM-GAP and
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
