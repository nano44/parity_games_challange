# R2-N5-Z: second-referee check of packet P-N5-Z (L-SI box 5: crossings of N5 reduce to reversals of R). REFEREE-2 (successor 4), 2026-10-24 20:42Z (date -u)
Signature: (Opus 5.5, D15). Packet P-N5-Z (Lead 20:3xZ), pinned at trunk claude/vibrant-johnson-nxvvxo fba7177 (an ancestor of my merged tree).
Object: docs/si/P-N5-Z-box5.md, sha1 a027638f06d18143ed0779290b24f8e5decb8249 (219 lines; checked at the pin; L-SI successor 2, l-si 57dbb8b).
Convention as the packet: R excludes o, R̄ = R ∪ {o}; F and the crossing transitions are those of R19-R21.
Independence: I have not read docs/referee/R-N5-Z.md. I did not run the lane's experiments/si/xing scripts; its instances are inputs only.
Tools (docs/referee-2/R2-N5-Z/, own code on my R2-N5-RE/re_check.py definitions and own N5 with random tie-breaks; "spec" = n5.py's state
sequence): z_check.py, dbg_k.py, run_all.sh, logs/.

## Verdicts (Opus 5.5, D15)
| statement | verdict | gaps / notes |
| --- | --- | --- |
| (1) §7 Lemma LV′ | SIGN | N-Z-1: "a maximal run of consecutive equal pure signs" must mean ADJACENT in the sequence of crossing transitions, with a '±' transition breaking the run. Read "ignoring '±'", as the definition of Z does when it compares with "the previous pure-sign crossing transition", the monotonicity step is false: '±' transitions can lower \|R\| inside the run. Under the adjacent reading, #runs ≤ 1 + #'±' + #sign changes = Z + 1, and the proof is right |
| (2) §9 Corollary Z | SIGN | R21 (g) is used inside its signed hypotheses: one phase (joint λ-phase, τ fixed), X = #crossing transitions, the same set under either convention for R; O as in R21. The arithmetic: 12n⁴(1 + X + O) with X ≤ n(Z + 1) gives O(n⁵(1 + Z + O)) |
| (3) §4 Lemma NOFE (strong form) | SIGN | — |
| (4) §2 ACT | SIGN | — |
| (4) §3 LOOP and Corollary | SIGN | — |
| (4) §5 NOFL-E and Corollary | SIGN | — |
| (4) §6 GAP | SIGN | the left inequality and Step (K) need no H1/H3; (h) is used only for the π′-form |
| (4) §8 WM and Corollary | SIGN | — |
| (4) §1 Step (K) | SIGN | — |
| data note | — | N-Z-2: s_rt32_final (experiments/si/orlens/instances, cited in §10 for (U*-DROP) and in box 4's tables) is NOT in 𝒞^1O. It has two Odd vertices with a choice (14 and 28). The packet's lemmas, and Lemma G behind them, do not apply to it. (U*-DROP)'s refutation stands on the other four instances; the lane should drop s_rt32_final from 𝒞^1O data, or label it |
Context: (Z) = (X) up to a factor n is a REDUCTION. (Z), the carries (C) per phase, and G-N5-TIME stay OPEN. Lemma Φ, used in §9's READING,
is UNREFEREED, as the packet says.

## 1. Step (K), ACT, LOOP
- Step (K) ✓. At a fallback inside a phase, σ_k is a pointwise optimum of the S4a arena (FBL-N (i)). σ_k[y → z] is an arena strategy, so
  (F1) gives W_k(y) ⊵ its value at y.
- ACT (i) ✓. The membership propagation along kept edges ((F0)) is right. For forced Odd vertices and for o this needs τ fixed, which is
  assumed. The segment endpoints give M(s_1) = F and M(σ_{k+1}(s_j)) = R̄, so some s_i switches from F to R̄. It lies on a play that
  reaches o, so s_i ∈ R_{k+1}.
- ACT (ii) ✓. If no s_i switches R̄ → F, the whole new play lies in R̄_k \ {o} = R_k, including its cycle. A cycle of old edges inside R_k
  is impossible, so the cycle contains a switched vertex.
- LOOP ✓.
  - c = λ_Ξ(o) ∉ R_k under H1, and λ_Ξ = c on R_k.
  - A new o-free cycle C ⊆ R_k has top t with λ_Ξ,k+1(t) = t: the honest play from t follows C, since there is no Odd choice on C. But
    λ_Ξ,k(t) = c ≠ t, so the phase is broken.
- DATA: ACT (i) 9,174 and (ii) 7,951 transitions, 0 failures. The cycle alternative of (ii) occurs 2,146 times, but never at a
  transition with H1 inside a phase (LOOP: 2,689 checks, 0 failures).

## 2. NOFE (strong form), NOFL-E, GAP, WM
- NOFE ✓.
  - Suppose y is not on o's W-play. Then z's W-play avoids y (z = o, or z's route followed by o's W-play), so σ_k[y → z] gives y the
    value y ⊕ W_k(z).
  - Case A: (VAL) and (F-pre). Their side conditions hold: σ_k y's path avoids y, and neither cycle node is y.
  - Case B: y is its own W-cycle node, and W_k(z)'s cycle node (o's W-cycle, without y) differs from y. So the strict improvement is
    decided by the cycle node.
  - Step (K) then gives the contradiction. The "or on a (σ_k, τ)-cycle" escape of box 4 is indeed not needed.
  - DATA: 21 switched F_k → R̄_k edges at fallbacks in phases; all 21 tails on o's W-play, and all 21 are W-cycle nodes (consistent
    with the READING remark).
- NOFL-E ✓. With Ξ = W and H2, y ∈ R_k is on no W-cycle and z's W-play avoids y. Step (K).
  - DATA: 0 R_k → F_k switches at fallbacks from Ξ = W states with H2. The Corollary (no leave from Ξ = W with H1 ∧ H2): 113 checks,
    0 failures.
- GAP ✓. The left inequality is the gate. The right one by contradiction, as in NOFL-E, using only H2 and Lemma G (a) at z ∈ F. The
  π′-form uses Lemma G (b) under (h).
  - DATA: 1,950 switched R_k → F_k edges at fallbacks with (h), 0 violations of either inequality or of the π′-form.
- WM ✓. R18 (d) Lemma S (c) applies to S4a steps (G-1OA-6: not to S4c steps, which WM excludes). σ_k is in the arena with valuation W_k.
  If Iσ_k = ∅ inside a phase, S4a returns σ_k and W is unchanged.
  - DATA: 15,717 non-fallback transitions in phases, 0 decreases.
  - Corollary: 963 of the 1,153 fallbacks in phases lower W somewhere; no non-fallback does.

## 3. LV′ and Corollary Z
- LV′. Under the adjacent reading (N-Z-1), each run is a maximal block of adjacent crossing transitions with one pure sign, so |R| is
  strictly monotone inside it, and it has ≤ n − 1 transitions (|R| ∈ {0, …, n − 1}).
  - A new run starts only after a '±' transition or at a pure sign change. So #runs ≤ 1 + #'±' + #(sign changes) = Z + 1, and
    X ≤ (n − 1)(Z + 1) + Z. Z ≤ X is immediate. ✓
  - The literal reading fails as a proof step: "+, ±, +, ±, …" with each '±' lowering |R| forms one "run ignoring ±" whose length is
    unbounded by |R|. In my data no such run exceeded n − 1 (max 23, at n ≥ 24), so it is a wording point, not a counterexample.
  - DATA: 35,072 phases, max X 70, max Z 22, 335 '±' transitions; X ≤ (n − 1)(Z + 1) + Z in every phase.
- Corollary Z ✓.
  - R21 (g) needs only "one phase". X is the same set under the packet's R and R21's.
  - DATA: the R21 (g) bound held in every phase. It is far from tight.

## 4. Data (DATA; logs/totals.txt)
- Sources:
  - random o-cyclic 𝒞^1O: own seeds 131 (n 6-14) and 132 (n 6-16), 5,000 runs each; SPEC seed 133, 3,000 runs;
  - named instances (SPEC from the S3 start or their .start, plus 20 own runs each): experiments/si/xing/instances (nofe_cyc_n8 with its
    .start, zcl_*), experiments/si/orlens/instances (15 of 16; s_rt32_final skipped as not 𝒞^1O), box28 and box29 instances,
    fbref_cex_n32, returns_rt48, fts_best16.
- Totals: 13,756 runs, 38,186 transitions; 0 violations of any packet statement.
- One false alarm, recorded.
  - My first run took s_rt32_final as 𝒞^1O (my inst mode picked the first Odd choice vertex), and Step (K) "failed" 14 times under SPEC.
  - dbg_k.py shows the cause: my honest valuation (minimum over o's exits only) differs from si.py's at vertex 28, which is the second
    Odd choice vertex.
  - The checker now refuses non-𝒞^1O games. The false alarm is the origin of N-Z-2.

## 5. Gap list
| id | where | status |
| --- | --- | --- |
| N-Z-1 | LV′: "consecutive" must mean adjacent among crossing transitions ('±' breaks runs) | wording; with it the proof is right |
| N-Z-2 | s_rt32_final is not 𝒞^1O (Odd choices at 14 and 28) | data note for the lane (§10, box 4 tables) |
