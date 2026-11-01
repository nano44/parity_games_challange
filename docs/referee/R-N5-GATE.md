# R-N5-GATE: REFEREE report on packet P-N5-GATE (L-NEW box 120): SETTLE-MON, BRACKET-MON, SETTLE-RED / BRACKET-RED, CONSISTENT-RED, the explicit DEAD
Referee: REFEREE (successor 21), Opus 5.5 (D15). Lead brief 2026-11-01 00:34Z (read 00:33Z by date -u). REFEREE-2 reviews independently.
- Object and pin: docs/new/P-N5-GATE-box120.md at claude/l-new 516717da. `git show 516717da:<path> | sha1sum` =
  ac88915dfb07fc8b5644db99762671eee8ef7312 (135 lines). The line docs/new/P-N5-GATE-line.txt has sha1
  245ce9feac30a6462ec31edca2c724e1409d9f06. Both equal the Lead's figures.
- Independence: I opened no docs/referee-2/ file for this packet.
- Scope (D1): REDUCTIONS and EQUIVALENCES, and one DEAD at an explicit bound. No count is bounded. G-N5-TIME stays OPEN. Not a TARGET.md
  claim.
- Every verdict below is labelled (Opus 5.5, D15).

## Verdicts
| § | item | verdict |
| --- | --- | --- |
| 1 | premises, incl. THE KEY CHECK: R18 (d) Lemma S (a)-(b) «on every game» | CHECKED, holds on every game (§1) |
| 2 | Corollary SETTLE-MON | SIGNED |
| 3 | Corollary BRACKET-MON | SIGNED |
| 4 | SETTLE-RED, BRACKET-RED (equivalences) | SIGNED |
| 5 | Lemma CONSISTENT-RED and its Corollary | SIGNED |
| 6 | DEAD at the explicit bound n − 1 | CONFIRMED on both instances by my own engine (lend107_n32 107 > 31; fbg_K12_m6_m24 403 > 289) |
| 7-8 | DATA, READING | not to sign |
| — | RESULTS line (245ce9fe) | MATCHES the signed items. Precision items only (§8) |

## 1. Premises
- R18 (d) Lemma S (a)-(b), and whether it uses any 𝒞^1O hypothesis. It does not.
  - RESULTS R18 (l. 778-835) lands Lemma S inside the 𝒞^1O packet, but its statement (l. 803-807) carries no class hypothesis: «(a) L_σ is
    the pointwise minimum of V_{σ,τ'} over Odd's strategies τ' and U_τ the pointwise maximum of V_{σ',τ} over Even's σ' (VJ00 (11) on G
    and on G^d); (b) L_{σ_k} ⊴ V_{σ_k,τ_k} ⊴ U_{τ_k}, with L non-decreasing and U non-increasing along the run.»
  - Its signed proof is docs/referee/R-N5-1OA.md l. 136-142 (my predecessor's).
    - (a) is VJ00 (11) on G, and on G^d read through Lemma R. The «⊵» halves of (4)/(6) are derived in R17 (a) (gap S1, closed).
    - (b) is immediate from (a) plus R15 (a) applied to every N5 step, which is Switch_I with ∅ ≠ I ⊆ Iσ (resp. Iτ on G^d) by R15 (d)
      (gap S2, closed).
  - VJ00 (11), Lemma R (proved from SPEC S1 alone, R-N5-1OA l. 47), R15 (a) and R15 (d) are all game-general. Nothing in the argument
    refers to the single Odd choice vertex o, to X or to o-acyclicity.
  - So [SQZ] holds on every game, including the HI half, which uses R15 (d)'s Odd clause (τ moves only by Switch_I with I ⊆ Iτ on G^d).
  - My control confirms it mechanically (§7: SQZ 0 violations).
  - Precision: the landed R18 entry names its setting «𝒞^1O» in its Setting line. A line using Lemma S «on every game» should say why,
    as this line does («used on every game»). CHECKER may want the citation «(proof: VJ00 (11), Lemma R, R15 (a), (d); no 𝒞^1O
    hypothesis)».
- R17 (b)-(d) (RESULTS l. 1-17 of R17). (d) reads «switch-best on one-player games makes fewer than (n² − n + 1)(n + m) steps … the bound
  holds for every pointwise-optimal choice». Switch-best is «ρ_{k+1} = an optimal strategy of the arena H_k in which every vertex x may
  use {ρ_k(x)} ∪ I_k(x) (VJ00 improving edges, §4.4 eq. (2))». «Any start» is R18 (c)'s reading, as cited ✓.
- R57 1E-N3; R93 (a) (CS, linear) ✓; R99 SANDWICH (signed by me in R-N5-STAIR §3) ✓.
- SPEC S4 with FIX 3: the arenas and the fallback rule as used ✓.

## 2-4. SETTLE-MON, BRACKET-MON, SETTLE-RED / BRACKET-RED
- SETTLE-MON ✓: a ⊴ LO_j ⊴ W_j ⊴ HI_j ⊴ a, and ⊴ is linear.
- BRACKET-MON ✓.
  - a ≤ a′ ≤ b′ ≤ b, where a′ ≤ b′ is the sandwich at k + 1.
  - SANDWICH on (a, a′, b) gives lcp(a, b) ≤ lcp(a′, b). SANDWICH on (a′, b′, b) gives lcp(a′, b) ≤ lcp(a′, b′).
  - Each lcp lies in [0, n + 2].
- REDs ✓. SET grows at r ≤ n transitions, leaving ≤ r + 1 windows of ≤ SG transitions each, so K ≤ (r + 1)SG + r ≤ (n + 1)(SG + 1). The
  same holds for B with ≤ n(n + 2) rises. The correction of box 117's «(n + 1)·SG» is right.

## 5. CONSISTENT-RED
- On a consistent transition with τ fixed, σ changes: if S4a changed nothing, then with τ_(k+1) = τ_k the transition would be an S4c
  fallback, which is excluded ✓.
- S4a's arena equals R17's switch-best arena on G_τ: {σ_k(y)} ∪ Iσ_k(y) = {σ_k(y)} ∪ IW_k(y). IW_k is VJ00's improving set of σ_k in G_τ,
  because the VJ00 valuation of σ_k in the one-player game G_τ is W_k.
- [1E-N3] makes σ_(k+1) a pointwise optimum of that arena. So the window is a prefix of a switch-best run on G_τ from σ_(k0), under some
  pointwise-optimal choice at each step. R17 (d) (every choice, any start) gives k1 − k0 < B ✓.
- The Corollary ✓: ≤ INC + 1 consistent windows of ≤ B − 1 transitions each, plus the INC inconsistent ones. The equivalence with INC
  holds because INC ≤ the length.

## 6. DEAD (explicit bound)
- The killed statement has the explicit bound n − 1 (R17 (c)'s), so it is allowed in a line under L43.
- lend107_n32 (sha1 ab4c9811…, start 9df4ea2c…; both from the frozen worktree): my engine gives K = 112, one τ-stretch of 109 transitions,
  and a largest λ_W-phase with 107 W-changing transitions. 107 > 31 ✓. This equals the packet.
- fbg_K12_m6_m24 (2f035ca0…, with the repaired start 9f03f81f…; n 290; gate_logs/pin_fbgK12.txt):
  - K = 404, one τ-stretch of 403 transitions, and 403 W-changing transitions in one λ_W-phase. 403 > 289 ✓.
  - INC = 395. This equals the packet's §7 «395 / 403».
  - The run has VIOLATIONS 0 for SQZ, SET, BR and CR.

## 7. Controls (own engine; docs/referee/scratch/gate_probe.py, `python3 -I`, rl_engine, CS from stair_probe.py; no lane code)
- Definitions in the control:
  - LO = Ξ_k (S1); HI = the dual valuation of τ_k (rl_engine's Ut, read as a G-triple per Lemma R; G^d keeps G's rank order);
    W = val(σ_k, τ_k).
- Checks:
  - SQZ (sandwich and both monotone halves), SET (SETTLE-MON), BR (BRACKET-MON per vertex), RED (both bounds);
  - CR (the Corollary's bound per τ-stretch, with INC computed from Is and IW);
  - MAXPH (§6's count).
- MUT controls on lend107_n32 (both bite):
  - MUT 1 (HI := W): SET_V 30, BR_V 73, SQZM_V 239.
  - MUT 2 (BR compared with LO_(k+1) instead of HI): BR_V 3,394.
- Corpus: 719 distinct games, MAXN 100 (656 analysed, 63 skipped), start file when present (gate_logs/sum.txt).
  - K 11,289 iterations, SQZ 529,356 checks, 619 τ-stretches (9,379 transitions, INC 7,083), SG ≤ 120, BG ≤ 98.
  - VIOLATIONS 0 for SQZ, SET, BR, RED and CR.
  - 71 runs exceed the §6 bound n − 1 (the lane's 118 is on its 1,132-line list). Examples: lend47_n32 49 > 31, nep92_n40 95 > 39,
    b6_xl_n48 94 > 47.
- Lane check.sh blocks «box 116»-«box 118» were not re-run by me. The two DEAD instances were re-run on my own engine, which is
  independent of n5b / n5x.

## 8. RESULTS line (245ce9fe): strict symbol test
- Binder: «for every N5 run on every game, every vertex v, every transition k → k + 1 and all states k0 < k1» ✓.
  - j is bound in SETTLE-MON.
  - y and z are bound in IW_k.
  - k is rebound locally in CONSISTENT-RED's «for k0 ≤ k ≤ k1» (harmless).
- All defined: n, m, K, values, Iσ_k, LO_k, HI_k, W_k, SET_k, lcp, CS (R93 (a)), B_k, SG, BG, G_τ, IW_k, τ-stretch, consistent, INC,
  λ_W-phase, B.
- Precision (not required):
  - P-1. Notation clash: B := (n² − n + 1)(n + m) and B_k := Σ_v lcp(…); «BG := … at none of which … B rises» means B_k. Write «B_k rises»
    (or rename one of them).
  - P-2. In CONSISTENT-RED, «τ_k = τ» binds τ as the common value. «τ := τ_(k0)» would be explicit.
  - P-3. The DEAD clause names its instances without path or sha1. Add experiments/new/box116/inst/fbg_K12_m6_m24.pg (2f035ca0…) with
    fbg_K12_m6_m24_fixed.start (9f03f81f…), and experiments/n5-epoch/instances/lend107_n32 (ab4c9811…, start 9df4ea2c…).
  - P-4. The Lemma S premise: see §1's precision.
- L41 tail («R17 (F1) and R18 (d) Lemma S (a) rest on derivations written by REFEREE and REFEREE-2 (R17 (a))») ✓.
- L43: the only DEAD is at an explicit bound with both counts ✓.
- TARGET.md diff: scope words ✓, no algorithm claim.
- Verdict: MATCHES the signed items (precision P-1..P-4 optional).

## DONE / FINDINGS / NEEDS
- DONE: this report; gate_probe.py; gate_logs/.
- FINDINGS:
  1. Every item to sign is SIGNED, with no gap.
  2. R18 (d) Lemma S (a)-(b) uses no 𝒞^1O hypothesis. Its proof is VJ00 (11) on G and G^d, Lemma R and R15 (a)/(d), all game-general.
  3. The DEAD is confirmed on lend107_n32 by my engine.
  4. The line MATCHES; precision P-1..P-4.
- NEEDS: Lead: precision items to L-NEW 44 if wanted.
