# N5-WDEPTH (box 48): repeats charged to the late-adoption windows that enable them. Theorem REP-DEPTH: REP_F polynomial if the window depth is bounded; depth ≤ 2 in all data
L-SI successor 31 (Opus 5.5), D15 / D18, Lead reading L40. Lead 2026-10-30 02:00Z: «[P-REP] in its live shape: "each FIRST late adoption
re-enables ≤ p(n) repeats" … Define the "re-enable" charge exactly … try to prove the per-FIRST bound. A natural route: GP*-SUB on the
sub-interval after that FIRST adoption … Watch the chain: a repeat's parent may itself be a plain switch whose own cause is a FIRST adoption
further back. Either a lemma or the exact obstruction is a result.» Working note, unrefereed. G-N5-TIME OPEN. Labels as usual.
- Tool: experiments/si/odd/repchain.py (counters WIN0 / WINF / WINR, PERWIN, WINCH_V, MAXWD, SELF). Output odd/out/repchain_corpus.txt
  (re-run). Pinned in si/check.sh «box 45» (latew line extended) and «box 48».
- Setting and symbols: a W-run F (RESULTS R89); late adoption, BLOCKED (R88 / R89); FIRST / REPEAT, REP_F (P-N5-CUT §6). A LATE
  TRANSITION is a transition of F containing at least one late adoption.

## 1. Windows, and Lemma WIN (PROVED, lane; from GP*-SUB, box 46)
- The WINDOW of a late transition L is the set of transitions [L, L′) of F, L′ the next late transition (or the end of F). The INIT window
  is [a, L₁). Every transition of F lies in exactly one window.
- Lemma WIN. A window has at most n W-changing transitions (the INIT window at most n − 1).
- Proof. The transitions L + 1, …, L′ − 1 contain no late adoption of F. An adoption there of an edge blocked at a state ≥ L + 1 would be a
  late adoption of F. So the sub-interval [L + 1, L′] has R*_T = 0 read relative to itself, and GP*-SUB (box 46: FW-R* on every sub-interval)
  gives ≤ n − 1 W-changing transitions among L + 1, …, L′ − 1; the transition L adds at most 1. The INIT window is [a, L₁] with R*_T = 0. □

## 2. The charge and Theorem REP-DEPTH (PROVED, lane)
- The charge. Let ρ be a REPEAT of (y, z) at u₂ (previous late adoption of (y, z) at u₁; y's leave of z at k, u₁ < k < u₂). By LATE-SPLIT (ii)
  (P-N5-CUT §6), unless ρ is W-silent or y is its own cycle node on [k + 1, u₂ + 1], W(z) changes on [k + 1, u₂ + 1]. If it changes at some
  transition of [k + 1, u₂ − 1], let t*(ρ) be the last one; ρ is CHAINED and is charged to the window W(ρ) containing t*(ρ). Otherwise ρ is
  EXCEPTIONAL: W-silent, own-cycle, or SELF (the only change is at u₂ itself). X_F := the exceptional REPEATs of F.
- Depth. For a late transition L put lwd(L) := the largest depth of a chained REPEAT at L (0 if none). depth(ρ) := 1 + lwd(L(ρ)), L(ρ) the
  transition opening W(ρ) (lwd(INIT) := 0). L(ρ) ≤ t*(ρ) < u₂, so the recursion is well-founded. D_F := the largest depth.
- Counting. (i) A window W is charged at most n·m_E REPEATs: for a fixed edge (y, z) distinct REPEATs have disjoint intervals [k + 1, u₂]
  (consecutive adoptions), so distinct t*; at each W-changing transition t of W at most Σ_{z changed at t} d_E(z) ≤ m_E REPEATs have t* = t;
  W has ≤ n W-changing transitions (Lemma WIN). (ii) Windows with lwd = 0 number at most 1 + m_E + X_F: INIT, those opened by a transition
  whose late adoptions are FIRST (≤ m_E of them, P-N5-CUT §6 (i)) or exceptional REPEATs. (iii) Windows with lwd = d ≥ 1 number at most
  R_d := the chained REPEATs of depth d (each such window is opened by a transition containing one).
- Theorem REP-DEPTH. R₁ ≤ (1 + m_E + X_F)·n·m_E, R_{d+1} ≤ R_d·n·m_E, so
  REP_F ≤ X_F + (1 + m_E + X_F)·Σ_{d=1}^{D_F} (n·m_E)^d.
- Corollary. If D_F ≤ D for a constant D and X_F ≤ p(n), then REP_F = O(p(n)·(n m_E)^{D+1}); with P-N5-CUT's Theorem CUT-RED this gives
  [P-REP] and removes it from CUT-POLY's premises (replaced by [P-WD]: D_F ≤ D, and [P-X]: X_F ≤ p(n)).

## 3. DATA
| instance | n | REP | windows of t*: INIT / FIRST-only / REPEAT-opened | most REPEATs per window | D (max depth) | X (silent, own-cycle, SELF) | WIN violations |
| --- | --- | --- | --- | --- | --- | --- | --- |
| latew_K20_m32 (L-RED, .start) | 538 | 570 | 0 / 570 / 0 | 30 | 1 | 0 | 0 |
| so_th_n32 | 32 | 2 | 0 / 1 / 1 | 1 | 2 | 0 | 0 |
| corpus (719 games) | | 41 | 0 / 40 / 1 | 6 | 2 | 0 | 0 |
- The Lead's per-FIRST shape holds in data with room: one FIRST window re-enables at most 30 repeats at n = 538 (latew), far below n·m_E.
- The chain the Lead warned about occurs once: on so_th_n32 a REPEAT's enabling W-rise lies in a window opened by another REPEAT (depth 2).

## 4. CONJECTURE WD-BOUNDED and the obstruction (READING)
- CONJECTURE WD-BOUNDED: D_F ≤ 2 for every W-run (any constant would do). DATA: max 2; latew 1.
- The obstruction to proving it is the circle itself: a repeat-opened window has the same n·m_E capacity as a FIRST window (Lemma WIN), and
  nothing proved so far stops a repeat's wave from re-enabling another edge whose repeat opens the next window. A kill would be a family with
  growing D_F (repeats in a chain of windows, each enabled by the previous repeat's wave). That is a concrete target for L-RED.
- Composition: G-N5-TIME ⇐ (P-N5-CUT) [P-B] ∧ [P-SC] ∧ [P-ODD] ∧ [P-WD] ∧ [P-X], with [P-REP] now derived (Theorem REP-DEPTH).

## DONE / FINDINGS / NEEDS
- DONE: repchain.py window counters; corpus and latew; si/check.sh «box 45» extended, «box 48»; this note.
- FINDINGS: 1. PROVED (lane): Lemma WIN (≤ n W-changing transitions per window, from GP*-SUB). 2. PROVED (lane): Theorem REP-DEPTH,
  REP_F ≤ X_F + (1 + m_E + X_F)Σ_{d ≤ D_F}(n m_E)^d. 3. DATA: D ≤ 2, X = 0, ≤ 30 repeats per window (latew). 4. CONJECTURE WD-BOUNDED.
- NEEDS: none from the owner.
