# N5-RTC (box 32): CONJECTURE R*-TC by an injection — Lemma LATE-BASIN PROVED (lane); R*-TC DEAD outside the same-pair core (kt6_n58); in the same-pair core the naive injection is injective on all data (CONJECTURE R*-TC(SP))
L-SI successor 28 (Opus 5.5; D18, Lead reading L40). Lead's brief 2026-10-29 17:23Z, STEP 1b: «CONJECTURE R*-TC (R*_T ≤ TC), via the
injection of a non-basin-changing late adoption of (y, w), blocked at t, into y's entry or w's exit; the collisions are the open point. Then TC
itself: multi-gate, per-transition TRAP-LIN. How each would compose toward NM*/NM*^U (R86 COMPOSE) or W-SPLIT is the question that matters for
G-N5-TIME. Say it for every result.» Working note, unrefereed, not frozen. Not a TARGET.md claim; no running-time bound; G-N5-TIME stays OPEN.
Labels (D18 / L40): PROVED (lane) / CONJECTURE / OPEN / DATA / DEAD. Counts are TRANSITIONS. Setting and symbols: docs/si/N5-SPC-box31.md §0
and §6 (frozen W-phase F = [a, b], ρ_k = σ_k, W_k = val(ρ_k, τ), Ξ_k = val(ρ_k, σ̄), Iσ_k, D, U_k, S_{d,k}, G3*, BLOCKED, late adoption*,
R*_T, TC); docs/si/N5-TORD-box30.md §11 (GATE-FORM, SAME-NODE); packet docs/si/P-N5-GP-box31.md (Lemma XW, GP*, FW-R*). Tool:
experiments/si/core/inj.py; outputs core/out/inj_*.txt.

## Summary
| § | item | label |
| --- | --- | --- |
| §1 | Lemma LATE-BASIN: a blocked edge (y, w) at t has w ∉ U_t; if w's gate d at t is same-pair with G3* at t, then y ∉ S_{d,t}; hence a late adoption* of (y, w) at a transition s that changes no basin is preceded by a basin change of y or of w at some transition in [t, s) | PROVED (lane) |
| §2 | CONJECTURE R*-TC in every frozen W-phase | DEAD (red/fbx/instances/kt6_n58: R*_T = 5, TC = 0; 15 non-same-pair phases with R*_T > TC) |
| §2 | same-pair core: a matching of late* transitions into basin-changing transitions of size R*_T exists in all 255 phases with R*_T > 0; the naive map has multiplicity 1 everywhere; all 8 non-basin-changing late* transitions are charged to the transition just before (gap 1) | DATA |
| §3 | CONJECTURE R*-TC(SP): R*_T ≤ TC in every same-pair frozen W-phase; sharper CONJECTURE INJ1: the map s ↦ (s if s changes a basin, else s − 1) is an injection into the basin-changing transitions | CONJECTURE |
| §4 | composition: R*-TC(SP) + FW-R* ⇒ WCH ≤ (n − 1)(TC + 1) per same-pair frozen W-phase; feeds W-SPLIT's L* only, not R86 COMPOSE's NM* / NM*^U; the frontier is TC (multi-gate TRAP-LIN) | READING |

## 1. PROVED (lane): Lemma LATE-BASIN
Lemma LATE-BASIN. Let F = [a, b] be a frozen W-phase (any game, any D), y Even, and (y, w) BLOCKED at state t ∈ [a, b), i.e. W_t(w) ▷
W_t(ρ_t(y)) and (y, w) ∉ Iσ_t.
(i) w ∉ U_t: w's (ρ_t, τ)-play meets D, at a first gate d =: g_t(w).
(ii) If d = g_t(w) is same-pair (λ_Ξ(d) = λ_W(d)) and satisfies G3* at t, then y ∉ S_{d,t}.
(iii) If y adopts w at a transition s → s + 1 with t < s < b (ρ_{s+1}(y) = w ≠ ρ_s(y)) and no vertex changes its basin at s → s + 1
(first gate or membership of U), and the hypothesis of (ii) holds, then y or w changes its basin at some transition q → q + 1 with t ≤ q < s.
Proof. (i) (y, w) ∉ Iσ_t and w ≠ ρ_t(y) (W_t(w) ▷ W_t(ρ_t y) excludes w = ρ_t y) give, by [S2] (Iσ = the edges to a strictly Ξ-better
successor) and totality of the order, Ξ_t(w) ⊴ Ξ_t(ρ_t(y)). Lemma XW (packet §2): Ξ_t(ρ_t(y)) ⊴ W_t(ρ_t(y)). So Ξ_t(w) ⊴ W_t(ρ_t y) ◁ W_t(w),
Ξ_t(w) ≠ W_t(w). By XW's second part, Ξ_t(w) = W_t(w) whenever w's (ρ_t, τ)-play avoids D. So it meets D.
(ii) Suppose y ∈ S_{d,t}. y is Even, so y ∉ D and y's play passes ρ_t(y) before reaching d: ρ_t(y) ∈ S_{d,t}; and w ∈ S_{d,t} by (i). By
GATE-FORM (box 30 §11, under G3* at t for d) Ξ_t(v) = pre_t(v) ⊕ Ξ_t(d) and W_t(v) = pre_t(v) ⊕ W_t(d) for v ∈ {w, ρ_t(y)}, where Ξ_t(d)
and W_t(d) have the same cycle node (same pair). Two values p ⊕ A, q ⊕ A with a common tail A compare as their prefixes, independently of
A (the symmetric difference of the P-sets lies in the prefixes, the length difference is the prefix length difference; packet §3a, GP+ case,
which uses exactly this). Hence W_t(w) ▷ W_t(ρ_t y) ⟺ Ξ_t(w) ▷ Ξ_t(ρ_t y), and the latter would put (y, w) in Iσ_t: contradiction.
(iii) No basin changes at s → s + 1, so every vertex has the same basin at s and at s + 1. At s + 1, y's play is y, w, then w's play (if it
returns to y it closes a cycle through y and w, and both plays run around the same cycle after w; y ∉ D): so y and w have the same basin at
s + 1, hence at s. If neither y nor w changed its basin at any transition q → q + 1 with t ≤ q < s, then at t both were in the basin of w at
t, S_{d,t} with d = g_t(w): y ∈ S_{d,t}, contradicting (ii). □
- Remarks. (1) (i) holds in every frozen W-phase: blocked edges point INTO basins, never into U (the arena refuses only pessimistic heads).
  (2) (ii) is the reason the 8 non-basin-changing late* transitions of the box-31 data all have tail-disjoint gates. (3) Without (ii)'s
  hypothesis (iii) fails: §2's instance (gate not same-pair, U = ∅, no basin changes at all).
- Composition: LATE-BASIN is the domain lemma of the injection; it gives a charge target for every non-basin-changing late* transition, but
  not injectivity. By itself it gives nothing for W-SPLIT or NM*.

## 2. DATA (core/inj.py, the three corpora of box 31: alt_all pinned starts (START=1), lib41_n48, experiments/si (START=1))
inj.py, per frozen W-phase with D ≠ ∅: candidates of a late* transition s are {s} if s changes a basin, else the basin-changing transitions
q ∈ [t, s) at which y or w changes basin, t := the LAST state < s at which the adopted edge was blocked (union over the late* adoptions of s).
It counts Lemma LATE-BASIN violations (empty candidate set with (ii)'s hypothesis at t), computes a maximum bipartite matching (an injection
into basin-changing transitions exists iff its size is R*_T), and the multiplicity of the naive map s ↦ the latest candidate. Control:
MUT=lastonly (candidates {s} only, the per-transition form) must fail on a phase with a non-basin-changing late* transition.
| corpus | same-pair phases with R*_T > 0 | Σ R*_T / Σ TC | non-BC late* | matching fails | naive multiplicity > 1 | non-same-pair phases with R*_T > 0 | of these R*_T > TC |
| --- | --- | --- | --- | --- | --- | --- | --- |
| alt_all | 120 | 192 / 540 | 6 | 0 | 0 | 15 | 7 |
| lib41 | 87 | 104 / 424 | 0 | 0 | 0 | 9 | 8 |
| experiments/si | 48 | 52 / 146 | 2 | 0 | 0 | 5 | 0 |
- LEMMA_VIOL = 0 everywhere. Every empty candidate set (21, all non-same-pair) is outside (ii)'s hypothesis.
- Same-pair core: an injection exists in all 255 phases; the naive map is already injective (multiplicity 1). All 8 non-basin-changing late*
  transitions (lend47_n32 s = 8; usplit_n14, usplit_n23, usplit_rd_n24, usplit_rd_s3_n27 (twice: red/usplit and si/rund), usplit_s3_n16;
  si/lay/out/s_ka) have the adopted edge blocked at s − 1 and their only candidate is q = s − 1 (gap 1; core/out/inj_show_alt.txt).
- The mechanism is the same in all 8 (checked state by state): at s − 1 → s the head w itself switches and leaves its basin (to U in 5
  cases: usplit_n14, usplit_n23, usplit_s3_n16, lend47_n32, s_ka; to y's basin in 3: usplit_rd_n24, usplit_rd_s3_n27 (both copies)), y's
  basin does not change, and at s → s + 1 y follows w. So the charge is always «w's exit», never «y's entry».
- DEAD: CONJECTURE R*-TC «in every frozen W-phase» (stated in N5-SPC-box31 §6). Instance experiments/red/fbx/instances/kt6_n58.pg (sha1
  41d4f7cbe8644ac77bac9e2fd03a17ed4b2c7915), S3 default start written out as experiments/si/core/instances/kt6_n58_S3.start (sha1
  3ec0dab4b7769651de02ae86effec0318cfe7056); n5b identical (root/n5bcmp.py: 38 iterations, 2 fallbacks, identical state sequences: True).
  Frozen W-phase [5, 20], n 58, D = {18}, λ_Ξ(18) = 18 ≠ λ_W(18) = 0 (c₁ ≠ c₂), U = ∅ (all 58 vertices in S_18): R*_T = 5, TC = 0, WCH = 13
  (FW-R* holds: 13 ≤ 57·6). Obstruction: with c₁ ≠ c₂ the basin union is constant (TRAP-FIX, box 30), so TC = 0 is forced, while edges
  inside S_18 are compared by the two frames with different tails (no prefix comparison), so blocked edges inside the one basin are adopted
  later without any basin change. Largest non-same-pair R*_T − TC: 5 (kt6_n58); lib41: u1t_cex_n32 R*_T = 2, TC = 0.
- Not killing: for |D| = 1 and c₁ ≠ c₂, FW-D1 (box 30 TORD, W> case: ≤ s² trapped switches) already bounds WCH polynomially; R*-TC was never
  needed there.

## 3. CONJECTURE R*-TC(SP) and INJ1
- CONJECTURE R*-TC(SP): every same-pair frozen W-phase has R*_T ≤ TC. DATA: §2 (255 phases, 0 failures; also box 31 §6).
- CONJECTURE INJ1 (sharper, same-pair core): every non-basin-changing late* transition s has a basin change of y or w at s − 1 → s, and
  s − 1 → s is not itself a late* transition; so s ↦ (s if s changes a basin, else s − 1) is injective into the basin-changing transitions.
  DATA: all 8 cases, gap 1, each charged to w's own switch out of its basin at s − 1; never a collision.
- Where a proof stands. LATE-BASIN gives a basin change of y or w in [t, s). The open point (the Lead's «collisions») splits in two:
  (C1) the gap: the last blocked state t may be < s − 1 (the edge is unblocked and unchosen at s − 1); then the charge q may lie further back,
  and several late* transitions of one vertex could reach one q. (C2) the self-collision: q may itself be a late* transition, charged to
  itself. Neither occurs in the data; neither is excluded by a proof. A per-vertex bound would close (C1) for a polynomial (not linear)
  version: OPEN.
- Composition: R*-TC(SP) with FW-R* gives WCH ≤ (n − 1)(TC + 1) for every same-pair frozen W-phase, any number of gates. For |D| = 1, TD,
  c₁ = c₂ this is already known (box 30 TORD (i) + EPOCH-U, Corollary SEG's first inequality); the new content would be |D| ≥ 2 same-pair
  phases and non-TD same-pair gates (data: covered, §2). It reduces FW-BF in the core to TC, not to anything smaller.

## 4. READING: what these results feed, and what they do not (the G-N5-TIME question)
- W-SPLIT (box 29 §2): |𝒫| ≤ (FB + 1)(n(n − 1) + 1) + SBCH′ + (FB + 1 + n(n − 1)(FB + 1) + SBCH′)·L* per phase 𝒫, L* = the longest frozen
  W-phase. FW-R* (+ R*-TC(SP)) bounds the W-CHANGING transitions of a frozen W-phase, so it enters L* only, and only together with FW-LEN
  (W-silent transitions; none in the same-pair data, box 31 §1) and a bound on TC. So: L* ≤ poly would follow from R*-TC(SP) + a polynomial
  TC per frozen W-phase + FW-LEN + the non-same-pair cases (FW-D1 for |D| = 1; G1 ∧ G2 ∧ G3 by FW-DG; the mixed gate classes OPEN).
- The other factors of W-SPLIT are not touched: FB (fallbacks per phase; FB-LIN) and SBCH′ (λ_W-keeping σ̄-changes) are other lanes' open
  quantities.
- R86 COMPOSE (NM* / NM*^U): those count PHASES (τ- and λ-changes) along the run, and R*-TC / FW-R* live strictly inside one frozen W-phase
  (τ, σ̄, λ constant). They give nothing for NM* or NM*^U. So even a full proof of R*-TC(SP) and TRAP-LIN leaves the number of phases (and
  hence G-N5-TIME) open.
- TC itself (the next item, multi-gate per-transition TRAP-LIN): box 30 data stand (TC ≤ 0.868(n − 1) in kill climbs, entries per vertex
  ≤ 2, long runs are monotone waves); Corollary SEG reduces |D| = 1 TD c₁ = c₂ to the number of reversals of S. No new result here: OPEN.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/si/core/inj.py; core/out/inj_{alt_start,lib41,sicorpus}.txt, inj_show_alt.txt; core/instances/kt6_n58_S3.start;
  check.sh «box 32» block (lend47_n32 matching + LATE-BASIN, MUT=lastonly control fails, kt6_n58 R*_T 5 > TC 0); and check.sh: the two old
  «; ! grep» negations (lines 427, 440; ineffective under set -e) rewritten as «if grep …; then exit 1; fi» (both still pass).
- FINDINGS: (1) PROVED (lane): Lemma LATE-BASIN. (2) DEAD: R*-TC in general (kt6_n58, c₁ ≠ c₂, R*_T 5, TC 0). (3) DATA: in the same-pair core
  the naive injection is injective, gap 1. (4) CONJECTURE R*-TC(SP), INJ1. (5) READING: feeds W-SPLIT's L* only; nothing for NM*/NM*^U.
- NEEDS: none from the owner.

## Addendum (Lead 17:31Z: «For each result, also state the instance that would kill it if one turns up»; written 2026-10-29T17:4xZ by date -u, see commit)
| result | label | what would kill it | where it would show |
| --- | --- | --- | --- |
| Lemma LATE-BASIN (i) | PROVED (lane) | a blocked edge (y, w) at t with w ∈ U_t (w's (ρ_t, τ)-play avoids D) | that would also refute Lemma XW (packet §2), already signed |
| Lemma LATE-BASIN (ii)-(iii) | PROVED (lane) | a frozen W-phase with a late* adoption at a non-basin-changing s, w's gate at t same-pair and G3* at t, and neither y nor w changing basin in [t, s) | inj.py LEMMA_VIOL > 0 |
| general R*-TC | DEAD | (killed: kt6_n58) | — |
| CONJECTURE R*-TC(SP) | CONJECTURE | a same-pair frozen W-phase with R*_T > TC | inj.py SP_RT>TC > 0 (and SP_MATCH_FAIL > 0) |
| CONJECTURE INJ1 | CONJECTURE | a same-pair non-basin-changing late* transition s whose adopted edge was last blocked before s − 1 or with no basin change of y or w at s − 1 (gap > 1), or with s − 1 itself a late* transition (C2) | inj.py SHOW=1: «gap» ≠ 1, or SP naive_mult > 1 |
| READING (composition) | READING | — (not a claim) | — |
- The «w's exit» pattern (§2) is DATA, not a claim; a same-pair non-basin-changing late* transition charged to y's entry would end it.
- Fixes-file footer (Lead 17:35Z note): in docs/si/P-N5-GP-fixes-box31.md I edited the existing DONE / FINDINGS / NEEDS footer when adding
  G12 (2d0ada80) instead of appending a new one. Noted; later fixes items append a new footer and leave the old one in place.
