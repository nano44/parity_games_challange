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

## 5. TC (Lead 18:04Z: «go on TC with your untried idea: bound one vertex's exit-entry rounds by its strict Ξ rises across a round, plus a count of distinct prefix classes ... If TC stalls ... write a precise statement of what the bound needs (the missing lemma, with a kill instance if one is visible) and park»). Written 2026-10-29T18:1xZ by date -u, see commit
Setting: a frozen W-phase F = [a, b] with D = {o}, λ_Ξ(o) = λ_W(o) = c (c₁ = c₂) and TD at every state (τ(o), σ̄(o) ∉ S_k). S_k := the
vertices whose (ρ_k, τ)-play meets o. For x ∈ S_k (GATE-FORM, box 30 §11): W_k(x) = pre_k(x) ⊕ α2_k and Ξ_k(x) = pre_k(x) ⊕ α1_k, with
α2_k := W_k(o), α1_k := Ξ_k(o) and pre_k(x) the ρ_k-path from x up to o (excluding o; the same in both frames because σ̄ = τ off D).
p ⊕ A := (c, P_A ∪ hp, ℓ_A + |p|), hp := the vertices of p more relevant than c. The PREFIX ORDER compares (weight(hp), ±|p|) with c's
length polarity. Fact CMP: if hp, hq are disjoint from P_A and P_B, then p ⊕ A vs q ⊕ A is ordered as p vs q, and p ⊕ A vs p ⊕ B is ordered as
A vs B. Reason: the signed weight is additive over disjoint sets, and the key is lexicographic (reward(c), weight, ±length). A ROUND of x is
an exit at q1 → q1 + 1 (x ∈ S_{q1} ∖ S_{q1+1}) followed by the next entry at q2 → q2 + 1 (q1 < q2, x ∈ S_{q2+1} ∖ S_{q2}).

### 5.1 PROVED (lane): Lemma ROUND
Lemma ROUND. Let (q1, q2) be a round of x, p1 := pre_{q1}(x), p2 := pre_{q2+1}(x). Then at least one of the following holds:
(B) GATE CROSSING: α1_{q2+1} ▷ α2_{q1}.
(M) TAIL CAPTURE: hp2 meets P(α2_{q1}), i.e. some vertex more relevant than c lies on x's new prefix and on the gate's W-tail play at q1.
(A) PREFIX CLIMB: p2 ⊵ p1 in the prefix order.
Proof. W-MON: W_{q2}(x) ⊵ W_{q1}(x) = p1 ⊕ α2_{q1}. x ∈ U_{q2}, so Ξ_{q2}(x) = W_{q2}(x) by XW. Ξ is monotone along N5's steps:
Ξ_{q2+1} ⊵ Ξ_{q2} pointwise. This is VJ00's improvement theorem for switches to improving edges, the premise used in box 30's PMON and
SIL-EXIT proofs. Hence p2 ⊕ α1_{q2+1} = Ξ_{q2+1}(x) ⊵ p1 ⊕ α2_{q1}. hp1 is disjoint from P(α2_{q1}), and hp2 from P(α1_{q2+1}), because each
play is simple. Suppose neither (B) nor (M) holds. Then α1_{q2+1} ⊴ α2_{q1}, and hp2 is disjoint from both tails. By CMP:
p2 ⊕ α2_{q1} ⊵ p2 ⊕ α1_{q2+1} ⊵ p1 ⊕ α2_{q1}. Both sides now carry the common tail α2_{q1}, so CMP gives p2 ⊵ p1. □
- Kill: a round that is none of A, B, M. That would refute W-MON, XW or Ξ-monotonicity; core/rounds.py would count it as ORD_V or as a
  class outside {A, B, M, L}.

### 5.2 DATA (core/rounds.py; the three corpora; outputs core/out/rounds_*.txt)
| corpus | \|D\| = 1, c₁ = c₂ phases (TD) | rounds | class A / B / M / L | strict prefix increases (PREINC) | prefix decreases (PREDEC) | max rounds per vertex | max entries per vertex |
| --- | --- | --- | --- | --- | --- | --- | --- |
| alt_all | 445 (435) | 60 | 60 / 0 / 0 / 0 | 564 | 0 | 2 (x31_re24) | 2 |
| lib41 | 519 (512) | 63 | 63 / 0 / 0 / 0 | 686 | 0 | 2 (x31_re24) | 2 |
| experiments/si | 279 (271) | 3 | 3 / 0 / 0 / 0 | 703 | 0 | 1 | 1 |
- Every round is a STRICT prefix climb: class A with the top of the symmetric difference inside the prefixes, and the new side strictly above
  (ORD_V = 0). No gate crossing or tail capture ever decides a round. Gate crossings occur, at most 2 per phase (si/lwp/out/xa), but never
  inside a round.
- PREDEC = 0 everywhere: over ALL states at which x ∈ S (within stays, across epoch boundaries and across rounds) the prefix of x never
  decreases. Control: MUT=rev (flag increases instead) fires on x31_re24 (PREDEC 34). So the check has teeth.
- Strict prefix increases per vertex per phase: at most 11 (new/box25/instances/rtt16, n 16, 11 transitions). In total per phase: at most
  2.83(n − 1) (new/box25/instances/rttf48, n 48, 10 transitions).

### 5.3 What the bound needs (precise), and the reduction it would give
- CONJECTURE PRE-MON. In a |D| = 1, c₁ = c₂, TD frozen W-phase, pre_k(x) is non-decreasing in the prefix order over all k with x ∈ S_k.
  - Proved pieces: inside an epoch, PMON (box 30). Across a round, Lemma ROUND gives case A unless B or M.
  - Missing:
    - (i) a stay of x across a basin change of other vertices, while α1 and α2 move. The tails are U values; they rise, and they can absorb
      prefix vertices.
    - (ii) excluding B and M as the deciding case of a round.
    - (iii) strictness at a round.
  - DATA: 0 decreases in 1,243 phases.
  - Kill: a phase with PREDEC > 0, or a round of class B or M (rounds.py).
- CONJECTURE PRE-P (the missing lemma). In such a phase every vertex's prefix strictly increases at most n − 1 times.
  - DATA: at most 11 at n 16.
  - Kill: a vertex with more than n − 1 strict prefix increases (rounds.py «preinc/vertex»).
  - The SUMMED form, at most n − 1 increases per phase over all vertices, is false on the data: rttf48 has 2.83(n − 1).
- Reduction. PROVED (lane) as an implication; the inputs are the two conjectures.
  - From PRE-MON with strictness: each round of x is a strict prefix increase, so rounds(x) ≤ preinc(x).
  - Every entry of x except possibly the first ends a round, and every exit except possibly the last starts one. So TC ≤ Σ_x (entries(x) +
    exits(x)) ≤ Σ_x (2·preinc(x) + 2).
  - With PRE-P this gives TC ≤ 2n². Corollary SEG's first inequality (WCH ≤ (TC + 1)(n − 1), proved) then gives WCH ≤ (2n² + 1)(n − 1)
    per frozen W-phase: a polynomial FW-BF for |D| = 1, c₁ = c₂, TD.
  - X2 (entries ≤ 2) would need preinc at rounds ≤ 1. That is false on the data: x31_re24 has 2 rounds per vertex with 3 stays (in, out,
    in, out, in). X2 itself still holds there (2 entries).
- Why this stalls here. PRE-P is a Lemma P in the prefix frame (paths into o through S) ACROSS epochs. Inside S no edge is ever blocked
  (GP+ case: the prefix comparison makes Ξ and W agree there). Still, the paths available into o change as vertices enter and leave S. A
  Bellman-Ford argument across epochs meets the same F1/F2 walls as box 30 §9. Bounding PI = Σ preinc through W-changes is circular:
  PI ≤ n·WCH, and WCH ≤ (n − 1)(TC + 1).
- Composition (the G-N5-TIME question): the same as §4. PRE-MON + PRE-P would bound TC, hence L*, for |D| = 1 TD c₁ = c₂ frozen W-phases
  only. That feeds W-SPLIT. Nothing here reaches NM* / NM*^U, FB or SBCH′. Multi-gate TC would need the per-gate version, with the gates'
  basins interacting through U.

## DONE / FINDINGS / NEEDS (box 32, after §5)
- DONE: §5; experiments/si/core/rounds.py (MUT=rev control); core/out/rounds_*.txt; check.sh «box 32 §5» block.
- FINDINGS:
  - (1) PROVED (lane): Lemma ROUND (A / B / M dichotomy).
  - (2) DATA: every round is a strict prefix climb; prefixes never decrease (1,243 phases, control bites).
  - (3) CONJECTURES PRE-MON and PRE-P, with the reduction TC ≤ Σ (2·preinc + 2) ≤ 2n² ⇒ WCH = O(n³) for |D| = 1, c₁ = c₂, TD.
  - (4) DEAD on data: the summed form «PI ≤ n − 1» (rttf48, 2.83(n − 1)), and «rounds per vertex ≤ 1» (x31_re24).
  - (5) TC is parked at PRE-P, a prefix-frame Lemma P across epochs.
- NEEDS: none from the owner.

## 6. The bounded attempt «prefix improvements above g» (Lead 18:18Z: «a per-vertex bound on prefix improvements above g = top of P(α1) Δ P(α2) that does NOT go through W-changes, e.g. a count of distinct (prefix class, g) pairs that can only rise in a fixed order. One bounded attempt»). Written 2026-10-29T18:3xZ by date -u, see commit
### 6.1 PROVED (lane): Lemma ROUND-G (where a round's climb must sit)
Setting and notation of §5. Let (q1, q2) be a round of x with neither (B) nor (M). Assume also (M′): hp1 is disjoint from P(α1_{q2+1}).
(M′ is the reverse capture: an above-c vertex of x's old prefix lies on the gate's Ξ-tail at q2 + 1.) Let g′ := the top of P(α1_{q2+1}) Δ
P(α2_{q1}). Then either P(α1_{q2+1}) = P(α2_{q1}), i.e. the tails differ at most in length, or hp1 ≠ hp2 and the top of hp1 Δ hp2 is more
relevant than g′.
Proof. ROUND's chain gives p2 ⊕ α1′ ⊵ p1 ⊕ α2, with α1′ := α1_{q2+1} ⊴ α2 := α2_{q1}. Suppose P(α1′) ≠ P(α2). Then weight(P(α1′)) <
weight(P(α2)): a weight tie forces equal sets (RESULTS R84 (a) Fact DELTA). The signed-weight comparison of two sets is decided at the top of
their symmetric difference, so g′ lies in P(α2) ∖ P(α1′) if g′ is even, and in P(α1′) ∖ P(α2) if odd. Not (M) and not (M′), and each play is
simple, so the four sets hp1, hp2, P(α1′), P(α2) meet only as hp_i ∩ P(α_i) = ∅ and between the two tails. The symmetric difference of
hp2 ∪ P(α1′) and hp1 ∪ P(α2) is therefore (hp1 Δ hp2) ∪ (P(α1′) Δ P(α2)). If its top were g′, the comparison would be decided at g′ for the
α2 side, and p2 ⊕ α1′ ◁ p1 ⊕ α2: a contradiction. So the top lies in hp1 Δ hp2 and is above g′. □
- DATA (core/rounds.py, ROUNDG_V = 0): of the 126 rounds, 54 are high climbs (top of hp1 Δ hp2 above g′) and 72 have equal tail masks
  (the gate's gap is a length gap only).
- Kill: a round with no (B), (M) or (M′), unequal tail masks, and the prefix difference's top below g′ (rounds.py ROUNDG_V > 0); it would
  refute XW, W-MON or Ξ-monotonicity.

### 6.2 The (prefix class, g) count: where it fails
- Idea tested: the climbs that pay rounds are high (above g′), and the ranks above g′ form a fixed set. If the tops of a vertex's climbs
  never repeated, a vertex would have at most n climbs and hence at most n rounds, with no W-changes used.
- DEAD for all prefix climbs (not only the round-paying ones). Instance experiments/new/box25/instances/rtt16.pg (sha1
  1775c8b0e0f16e4393a945299eacac4098778d08), S3 start, phase [0, 11], gate o = 13. Vertex 8 climbs 11 times. Every climb's top is an ADDED
  even vertex, and the top ranks repeat (5 repeats for vertex 8, 7 in the phase; TOPREP). This is a binary-counter pattern: a lower even
  vertex is re-added after a higher climb dropped it. Here g = rank 15 lies above every prefix vertex, so none of these climbs is high, and
  vertex 8 never makes a round. The counter mechanism lives below g.
- Does not apply at all to equal-tail gates. Instance experiments/red/xing/instances/x31_re24.pg (sha1
  49eaf50e960923f70ec6df2671561dd89e38882a), phase [1, 5]: P(α1) = P(α2) (α1 = (∅, 2), α2 = (∅, 1)). There every one of the 33 rounds is paid
  by an arbitrary prefix climb (round_tails_equal = 33), 2 rounds per vertex. «Above g» is vacuous there, so a (prefix class, g) count can
  give nothing for this family.
- What remains true on the data: the HIGH climbs of one vertex never repeat a top (HC_toprep = 0). This is thin evidence: at most 2 rounds
  per vertex in all corpora.

### 6.3 The precise missing lemma (parking point)
- CONJECTURE PRE-HC (unequal tail masks). In a |D| = 1, c₁ = c₂, TD frozen W-phase, the rounds of x not decided by (B), (M) or (M′) have
  pairwise distinct climb tops. Then x has at most n such rounds, by ROUND-G, without W-changes.
  - Kill: a vertex with two rounds whose climbs share their top (rounds.py HC_toprep > 0).
  - Even with PRE-HC, the remaining rounds stay open: equal-tail rounds (x31 family) and rounds decided by (B), (M) or (M′). Those need
    PRE-P (§5.3) or a gate-crossing count.
- Combined parking point for TC (|D| = 1, c₁ = c₂, TD): PRE-MON + PRE-P (§5.3) ⇒ TC ≤ 2n² ⇒ WCH = O(n³). The «above g» lever handles only
  rounds through unequal tails, and only under PRE-HC. The length-gap gates (x31_re24) and the in-stay counter pattern (rtt16) are the two
  instances any proof must handle.
- Composition: unchanged from §4 and §5.3 (W-SPLIT's L* for this class only; nothing for NM*/NM*^U).

## DONE / FINDINGS / NEEDS (box 32, after §6)
- DONE: §6; rounds.py (ROUNDG_V, HC_toprep, TOPREP counters); core/out/rounds_*.txt re-run; check.sh «box 32 §6» pins.
- FINDINGS:
  - (1) PROVED (lane): Lemma ROUND-G (a round through unequal tails needs a prefix climb above g′).
  - (2) DEAD: distinct climb tops per vertex for all prefix climbs (rtt16: 11 climbs, counter-like repeats below g).
  - (3) The «above g» lever is vacuous for length-gap gates (x31_re24: 33 rounds with equal tail masks).
  - (4) CONJECTURE PRE-HC (thin data).
  - (5) TC parked at PRE-MON + PRE-P.
- NEEDS: none from the owner.
