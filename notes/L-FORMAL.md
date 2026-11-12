# L-FORMAL notebook (Lean formalization lane; branch claude/l-formal; files: lean/, this notebook)

## Resume point
- 2026-11-12T11:41Z (date -u): «go» received 11:31Z (Lead rulings: pin Lean v4.35.0 + Mathlib v4.35.0 approved; SHARP text = claude/l-red
  0148d73f docs/red/R234-lamgap.md; one core theorem with BR-SEG and BR-SEG-G as corollaries; statements diffed before any proof).
- State: lean/lemmas/ holds DEFINITIONS (PGLemmas/Defs.lean) and STATEMENTS as propositions (PGLemmas/Statements.lean); both build
  (`lake build`: «Build completed successfully»); no proof of any statement exists yet. Sent to the Lead for the statement diff.
- Next, after the Lead's diff verdict: prove, in this order,
  1. order facts for `Val.lt` / `Val.le` under an injective `pr` (irreflexive, transitive, total; `ext` strictly monotone off Π = F4′);
  2. play facts from the definition of `val`: Λ(s v) = Λ(v); Λ(v) = v ⇒ val v = (v, ∅, 0); Λ(v) ≠ v ⇒ val v = ext(v, val(s v)) and
     v is not on the play prefix of s v;
  3. claim (L) of box 101 §2 over an inductive «simple path with value and choice count» predicate; (U) = the play prefix is such a path;
  4. LamGapSharpStatement by the plan below; then the one-player wording, BrSegStatement, BrSegGStatement as corollaries; OneCross.
- Proof plan for SHARP in Lean (mine, from box 101 §2 + R234 §3, slightly shorter than both): put t* := a + |Ch| and suppose t* + 1 ≤ b.
  Some x ∈ Ch switches at t* (the step changes the state, and only Ch moves). With u := s_(t*)(x), w := s_(t*+1)(x): val_(t*)(u) ◁
  val_(t*)(w) (Howard: x did not keep, so u was not best, and w is best).
  - x not a top: (L) at k = |Ch| and (M) make every value equal at t* and t* + 1 (the play prefix at t* + 1 is a simple path). Then
    val_(t*)(x) = ext(x, val_(t*)(u)) ◁ ext(x, val_(t*)(w)) = ext(x, val_(t*+1)(w)) = val_(t*+1)(x) = val_(t*)(x): contradiction. This
    replaces box 101's three (E) cases by F4′ in its strict form.
  - x a top: Λ(u) = Λ(w) = x, so the play prefixes of u and w at t* have at most |Ch| − 1 choice vertices before x; (L) at k = |Ch| − 1
    and (M) give val_(t*−1) = val_(t*) at u and w; Howard at t* − 1 made u best, so val_(t*)(w) ⊴ val_(t*)(u): contradiction (R234 §3).
- Layout rule: no lean/lakefile.* at lean/ root (Lead 11:31Z: «keep lean/lakefile.* absent at lean/ root»).
- Toolchain in a fresh container: commands in lean/lemmas/README.md (elan, `lake exe cache get`, `lake build`).

## Queue
1. LAM-GAP, SHARP form, with BR-SEG and BR-SEG-G as corollaries (statements written; proofs after the diff).
2. ONE-CROSS (statement written, abstract over a preorder; proof after the diff).
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
    ∩ V_{>ℓ} does nothing there. That equivalence is a READING, not yet a Lean lemma.
- Fleet texts read as inputs (not sources): claude/l-si 23d39400 docs/si/box101-lamgap.md §2; claude/l-red 0148d73f
  docs/red/R234-lamgap.md §0, §2, §3; claude/l-red docs/red/R231-onecross.md §2; trunk docs/RESULTS.md R118 (l. 13607 ff.), R17
  (l. 730 ff.), R15 (l. 624 ff.); docs/new/P-N5-XICYC.md §1-§5 and P-N5-XICYC-fixes.md l. 30-60 (F4′, STRICT-G, PATH-G).

## Dead ends
- None yet.

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
