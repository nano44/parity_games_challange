# N5 on o-cyclic 𝒞^1O, box 30 (b): case U1 of (OB_R)
L-NEW successor 10 (Opus 5.5, D15/D18). Written 2026-10-24 19:45Z onward (date -u). Labels: PROVED (L-NEW), READING, CONJECTURE,
OPEN, DATA.
- Notation: P-N5-NH-box30.md (pinned once the box ends; never edited).
- U1 piece: a (θ, w)-piece J of a crossing-free interval where both frames are in route form and c_w = λ_W(o) is strictly more
  relevant than c_θ = λ_Ξ(o).
- Scope: lemmas about the candidate N5. G-N5-TIME stays OPEN.

## 1. What holds in a U1 piece
- PROVED (L-NEW; P-N5-NH P3′ step 1, with κ_w := route vertices above c_w): κ_w(π_v) is constant for all v ∈ R from the |R|-th
  transition of J on.
  - The only change against P3′ is fact (R3) with the roles swapped. If κ_w(ρ) ≠ κ_w(ρ'), the top t of the difference is above c_w,
    hence above c_θ, and every other vertex of A_θ(ρ) Δ A_θ(ρ') lies in the κ_w-difference or between c_θ and c_w (V_mid).
  - So t tops both differences, and both frames decide the same way. Everything else in step 1 is unchanged.
- Consequence: before the freeze, J has ≤ |R| transitions. Every R-only change there is within the (OB_R) budget.
- After the freeze, the W order on routes is length only (direction: the parity of c_w). The honest order is: V_mid set (top of the
  difference, by parity), then length (parity of c_θ).
- READING: after the freeze, an R-only Ξ-change at a transition is one of two kinds.
  - (L) The W-length of some R-vertex changes. If there is no fallback in J, W is non-decreasing (Lemma W). So each R-vertex's
    W-length moves monotonically in [1, n − 1], and there are ≤ (n − 2)|R| transitions of kind (L).
  - (T) W is unchanged everywhere, and some R-vertex switches to a W-tied successor with a strictly better V_mid set. Such W-flat
    steps exist (WF0 is FALSE, wf0_cex_n16).
- So (OB_R) in U1 needs:
  - (a) "no fallback inside J" (CONJECTURE NFB-O), or a bound on fallbacks; and
  - (b) a bound on kind-(T) transitions.
  For (b), with the lengths frozen, the tied switches form an improvement process in the "W-tight" DAG (edges to successors of the
  same W-length). A vertex's honest value is then lexicographic over V_mid, which in general allows up to 2^|V_mid| increases. No
  polynomial argument is known. This is the exact residual obstruction.

## 2. DATA (u1vertex.py; route-form U1 pieces; after the κ_w-freeze)
| instance | n | U1 piece (|R|) | post-freeze R-changes (total / max per vertex) | kind (T) transitions | W decreases on R |
| --- | --- | --- | --- | --- | --- |
| u1_n32 (box 29 climb best, sha1 f9577ca9…) | 32 | 0..12 (27) | 13 / 2 | 3 | 0 |
| wf0_cex_n16 (sha1 1de2ff5b…) | 16 | 13..17 (7) and 20..21 (8) | 1 / 1 in each | 1 in each | 0 |
| b5_os_n16 / n20 / n24 (L-COMP 1993d744) | 16-24 | largest pieces with |R| 8 / 11 / 16 | 0 / 0 (all R-only changes are pre-freeze) | 0 | 0 |
- Readings:
  - On L-COMP's family, (OB_R) follows from the PROVED freeze alone: every R-only change is pre-freeze, so ≤ |R|.
  - Kind-(T) cascades seen are at most 2 changes per vertex. No fallback occurs in any U1 piece seen.
- CONJECTURE (U1-T): after the κ_w-freeze, each R-vertex has ≤ 2 Ξ-changes per value of its W-length. DATA as above. With (a), it
  would give ≤ |R| + (n − 2)|R| + 2(n − 1)|R| R-only changes per U1 piece. That is polynomial, but not the (OB_R) constant |R|.

## 3. Attack specification (for L-RED, as routed by the Lead)
- Target: a U1 piece in which one R-vertex makes many kind-(T) changes, i.e. many V_mid improvements at a fixed W-length.
- Mechanism to look for: a W-tight DAG (equal-length alternatives) where improvements at lower layers re-open honest-improving tied
  edges at higher layers, while Engine.evaluate's tie-break (the first maximal successor in DFS / BFS order, experiments/si/si.py
  evaluate) keeps picking non-best ties.
- A k-layer version with 2^k changes at the top would refute (OB_R) and (U1-T), and would be a superpolynomial count of N5 transitions
  inside one phase if the lengths stay frozen.
- Seeds: u1_n32.pg (13 post-freeze changes, 3 W-flat), wf0_cex_n16.pg.
- Fitness tools: experiments/new/box29/u1climb.py; experiments/new/box29/u1vertex.py (per-vertex counts).
