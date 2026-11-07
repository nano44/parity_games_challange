# R2-N5-GATE: REFEREE-2 report on P-N5-GATE (box 120): SETTLE-MON, BRACKET-MON, SETTLE-RED / BRACKET-RED, CONSISTENT-RED, DEAD §6
Referee: REFEREE-2 successor 25 (session_01V5yGRaPp26T6iMUpCRmXsW), Opus 5.5 (D15). Written 2026-11-01 (date -u; see the commit).
Independence: written without opening docs/referee/ for this packet.

## 0. Object
- docs/new/P-N5-GATE-box120.md at claude/l-new 516717da: sha1 ac88915dfb07fc8b5644db99762671eee8ef7312, 135 lines. Re-hashed: match.
- Line: docs/new/P-N5-GATE-line.txt, sha1 245ce9feac30a6462ec31edca2c724e1409d9f06. Re-hashed: match.
- Premises opened:
  - RESULTS R17 (b)-(e), R18 (c)/(d), R15 (a)/(d), R57, R93, R99 (Lemma SANDWICH), all on trunk.
  - docs/new/N5-time-box21.md §2.1-§2.2: the proof text of Lemma R and Lemma S.
  - SPEC docs/new/N5-ssi-global.md S4 a-d and FIX 3.
  - My predecessors' R2-N5-1OA.md: the Lemma S signature and gaps S1, S2, G-1OA-6.

## 1. Claims table
| § | claim | verdict |
| --- | --- | --- |
| §2 | Corollary SETTLE-MON | **SIGNED** |
| §3 | Corollary BRACKET-MON (B_k non-decreasing in [0, n(n + 2)], ≤ n(n + 2) rises) | **SIGNED** |
| §4 | SETTLE-RED, BRACKET-RED (K ≤ (n + 1)(SG + 1), K ≤ (n(n + 2) + 1)(BG + 1), SG, BG ≤ K; the equivalences) | **SIGNED** |
| §5 | Lemma CONSISTENT-RED and its Corollary ((INC + 1)(B − 1) + INC) | **SIGNED** |
| §6 | DEAD «every λ_W-phase of a τ-stretch has ≤ n − 1 W-changing transitions» | **SIGNED** (instance check). fbg_K12 is exact (403 > 289). lend107 has **106** > 31 under the packet's own phase definition, not 107 (GATE-L1) |

No gap in the mathematics.

## 2. The Lead's key premise question: does R18 (d) Lemma S need 𝒞^1O?
- **No.** I re-read box 21 §2.2 (trunk docs/new/N5-time-box21.md). It is the text R18 (d) signs.
  - (a) The lower half, L_σ = min_τ′ V_(σ,τ′), is VJ00 (11) on G.
  - (a) The upper half, U_τ = max_σ′ V_(σ′,τ), is (11) on G^d read through Lemma R. Lemma R (§2.1) is proved «from S1 alone» for any game.
  - (b) The monotone halves are R15 (a) on G and on G^d. They need R15 (d), every N5 step is Switch_I of improvements; this was gap S2,
    closed as a citation.
- Nothing in (a)-(b) mentions o, X, out-degrees, or o-acyclicity. In R18 those enter only in Proposition X and Lemmas 1-3 of (c).
  - R18 (d)'s own wording has no class restriction: «Lemma S (box 21 §2.2) (a)-(b): (a) … (VJ00 (11) on G and on G^d); (b) L_(σ_k) ⊴ V ⊴
    U_(τ_k), with L non-decreasing and U non-increasing along the run».
- The two moves the HI half needs hold on every game under SPEC S4 b/c with FIX 3:
  - τ_(k+1)(o) ∈ {τ_k(o)} ∪ Iτ_k(o) at S4b (also RESULTS R89 FRAME-τ).
  - S4c's Odd branch picks from Iτ, only when Iσ = ∅.
  - σ moves only along Iσ (S4a's arena; S4c's Even branch).
- Both halves were checked empirically on every state of the corpus. [SQZ], all three inequalities: 1,679,311 vertex-state checks, 0
  violations (§4). A wrong dual encoding would fail the sandwich at once.
- Formal status (NEEDS): R18's heading scopes the R-line to o-acyclic 𝒞^1O, while item (d) itself is stated and proved class-free.
  - Citing «R18 (d) … used on every game» is therefore correct as mathematics.
  - Whether a CHECKER accepts a class-free item of a subclass R-line as a premise «on every game» is a Lead reading (cf. L42).
  - I recommend the line say so explicitly, e.g. «R18 (d) (Lemma R and Lemma S (a)-(b), whose proof (box 21 §2.1-§2.2) uses no 𝒞^1O
    hypothesis)».
  - Also add R15 (d) to [SQZ]'s citation, as the packet's parenthesis «τ moves only along Iτ» already says (P-1 = R18's S2).

## 3. Review notes
- SETTLE-MON:
  - a ⊴ LO_j ⊴ W_j ⊴ HI_j ⊴ a by induction on the monotone halves and the sandwich at j. LEX (antisymmetry of a linear order) gives
    equality.
  - Both SET_k ⊆ SET_(k+1) and the frozen values follow. ✓
- BRACKET-MON:
  - a ≤ a′ ≤ b′ ≤ b lexicographically. CS is order-preserving and injective (R93 (a)) and the length n + 2 is fixed.
  - SANDWICH twice gives lcp(a, b) ≤ lcp(a′, b) ≤ lcp(a′, b′).
  - SANDWICH (R99) is the standard identity lcp(x, z) = min(lcp(x, y), lcp(y, z)) for x ≤ y ≤ z, and it is landed.
  - The range and the «≤ n(n + 2) rises» count are right. ✓
  - SETTLE-MON is in fact the case lcp = n + 2 of BRACKET-MON (CS injective).
- SETTLE-RED / BRACKET-RED:
  - SET is strictly growing at r ≤ n − |SET_0| ≤ n transitions. There are r + 1 windows of ≤ SG transitions each.
  - K ≤ (r + 1)SG + r ≤ (n + 1)(SG + 1).
  - Similarly with ≤ n(n + 2) rises of B.
  - The converse is trivial (SG, BG ≤ K). The equivalence is per run, so «over any family» means over any family of runs. ✓
  - The §4 erratum (box 117's «(n + 1)·SG» → «(n + 1)(SG + 1)») is right: K = SG + 1 with r = 1 is possible.
- CONSISTENT-RED:
  - (i) A consistent transition changes σ. If σ_new = σ_k and τ_new = τ_k, S4c fires (SPEC S4 c), which makes it a fallback.
    - Since τ_(k+1) = τ_k, τ_new = τ_k, so σ_new ≠ σ_k.
    - Not a fallback, so σ_(k+1) = σ_new.
  - (ii) S4a's arena with Iσ_k = IW_k is exactly R17's switch-best arena on G_τ: G_τ's improving set is IW_k, Odd has out-degree 1.
    - [1E-N3] makes σ_(k+1) a pointwise optimum of it.
    - So each step is one switch-best step from the current strategy, and the window is a prefix of some switch-best run from σ_(k0).
  - (iii) R17 (d) bounds every such run by < B, from any start (R18 (c)'s reading), for every pointwise-optimal choice. A prefix of
    k1 − k0 strategy-changing steps therefore has k1 − k0 < B.
  - R17's setting assumes injective priorities. SPEC S1's rank relevance gives that, as in R17 (e).
  - The Corollary's count is right: ≤ INC + 1 windows of ≤ B − 1 transitions each, plus INC.
  - Remark (R18 (c) Lemma 3 as a special case): consistent with R18's text. Not to sign.
- DEAD §6: the statement is the per-in-phase-step count of R17 (c), transferred, at the explicit bound n − 1. It is an instance kill at an
  explicit bound, not an asymptotic DEAD, so it may enter the line (L43 form).

## 4. Re-runs with my own code
- Tool: docs/referee-2/R2-N5-GATE/gate_check.py.
  - It runs on my N5 loop (DC.Runner / Engine / dual) with validated starts. LO, HI and W come from my engine; HI is the dual valuation read
    as a G-triple.
  - The lane's box117 / box118 scripts are not imported.
  - Checks: SQZ, SET, BRK, RED, CONS (consistent ⇒ σ changes; window < B), OPT (OPT-OFF form at consistent steps), CORL.
- Corpus: L-SI box 53's 1,132 runs, the same three lists as my R2-N5-ROOT114 run (sbcg runs=1; alt_all with-start runs=0; start-less runs=1).
  - Logs: logs/sbcg.txt, alst.txt, alns.txt; totals in logs/corpus_totals.txt. RESULT PASS, 0 violations, in all three.

| quantity (packet §7, DATA) | packet | mine |
| --- | --- | --- |
| [SQZ], SETTLE-MON, BRACKET-MON violations | 0 | 0 (1,679,311 SQZ vertex-state checks) |
| INC / climb steps | 12,433 / 17,841 | 12,433 / 17,841 |
| runs with INC 0 | 575 | 575 |
| SG / n, BG / n maxima | ≤ 3.41, ≤ 2.91 | 3.375, 2.875 (both within) |
| runs exceeding n − 1 in one λ_W-phase | 118 | 116 (see GATE-L1: in-phase transitions only) |

- CONS / OPT: 0 violations. OPT has 347,234 checks at consistent transitions; consistent windows are all < B.
- DEAD instances (logs/pins.txt; files at l-new 516717da):
  - fbg_K12_m6_m24.pg (sha1 2f035ca0a999…) with fbg_K12_m6_m24_fixed.start (9f03f81fae59…):
    - n 290, K 404, fallbacks 0, one τ-stretch of 403 transitions, and λ_W constant on it.
    - 403 W-changing in-phase transitions > 289. INC 395 (packet 395 / 403). **Exact.**
  - lend107_n32.pg (ab4c9811b311…) with lend107_n32.start (9df4ea2ceafe…): n 32, K 112, 10 fallbacks. The τ-stretch is transitions 1-109,
    with λ_W changing at transitions 1 and 108 (logs/lend107_phases.txt, tool phases.py).
    - So the phase's in-phase transitions are 2-107: **106** W-changing, all > 31.
    - The lane's box118/gate.py assigns a transition to the phase of its FIRST state (`lam` from W0 only), which also counts the closing
      transition 108. That gives 107.
    - The packet's definition («consecutive transitions at whose states λ_W is constant») gives 106.
    - The DEAD stands either way.
- Oink 8fbf0a7 `--zlk -v` on both instances (logs/oink_pins.txt; tool R2-N5-ROOT114/oink_pins.py): «verified», and the regions equal N5's
  final regions.

## 5. Gap map and line items
| id | where | kind | status |
| --- | --- | --- | --- |
| GATE-L1 | line DEAD clause (and packet §6 instance 2) | **REQUIRED**: «lend107_n32, 107 > 31» → «106 > 31» under the line's own λ_W-phase definition. Alternatively, redefine the phase by first states (then fbg is unchanged and lend107 is 107) | open (line) |
| P-1 | packet §1 [SQZ] / line R18 (d) | cite R15 (d) with R15 (a) for the monotone halves (R18's S2) | optional |
| P-2 | line R18 (d) | state that Lemma S (a)-(b)'s proof uses no 𝒞^1O hypothesis (§2) | recommended; formal status is a Lead reading |
| P-3 | line CONSISTENT-RED | «τ_k = τ for k0 ≤ k ≤ k1» uses k as a local index while the binder already has «every transition k → k + 1». Write «τ_j = τ for k0 ≤ j ≤ k1» and «every transition j → j + 1 with k0 ≤ j < k1» | optional precision |
| N-1 | packet §7 DATA | «118 runs exceed» is 116 under the in-phase definition (same cause as GATE-L1). Not to sign | note |

## 6. Line diff against TARGET.md's scope words
- «N5 on EVERY game», n := |V|, m := |E|, as in TARGET §1. No algorithm claim, no polynomial bound proved, no unit-cost arithmetic.
- The tail reads «REDUCTIONS and EQUIVALENCES (no count is bounded here; the sandwich is R18 (d)'s, not claimed here; … DEAD …; G-N5-TIME
  stays OPEN; not M3, not a step-4 pass, not a TARGET.md claim)». This is consistent with TARGET §2 and §4.
- Asymptotic words: none. The DEAD is at the explicit bound n − 1 with both counts (L43).
- L41: no proof in this packet is referee-originated.
  - The tail clause «the premises R17 (F1) and R18 (d) Lemma S (a) rest on derivations written by REFEREE and REFEREE-2 (R17 (a))» is
    accurate. R17 (a) records two referee derivations of (F1), one of them REFEREE-2's via VJ00 (11) plus the ⊵ halves of (4)/(6).
  - Lemma S (a) is (11) on G and G^d with those halves (gap S1).
- Binder pass: v, k, k0, k1, j bound; y, z bound in IW_k; τ as in P-3. SET, B_k, SG, BG, IW_k, INC, τ-stretch, λ_W-phase and B are
  defined. No free symbol.
- Verdict on the line: **REQUIRED** (GATE-L1). Then a word-diff of the revision.

## DONE / FINDINGS / NEEDS
- DONE: this report; docs/referee-2/R2-N5-GATE/{gate_check.py, phases.py}; logs/ (corpus, pins, Oink, lend107 phases).
- FINDINGS:
  - SETTLE-MON, BRACKET-MON, SETTLE-RED / BRACKET-RED, CONSISTENT-RED with its Corollary, and the §6 DEAD are all SIGNED (Opus 5.5, D15).
    There is no gap.
  - R18 (d) Lemma S (a)-(b) needs no 𝒞^1O hypothesis: its proof is VJ00 (11) on G and G^d, Lemma R, and R15 (a)+(d).
  - Line GATE-L1 is REQUIRED: lend107's count is 106, not 107, by the line's phase definition. The lane's gate.py counts each phase's
    closing transition.
  - The corpus DATA is reproduced: INC 12,433 / 17,841 and 575 runs with INC 0 exact; 116 vs 118 exceeding runs, same cause.
- NEEDS: Lead:
  - route GATE-L1 (and optional P-1 to P-3) to L-NEW;
  - a reading on citing a class-free item of the subclass R-line R18 «on every game» (P-2).
