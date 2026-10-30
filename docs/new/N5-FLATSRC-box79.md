# N5-FLATSRC (box 79): every flat transition carries a FLAT EVEN SWITCH (12882 / 12882, CONJECTURE FLAT-SW), so phase length reduces to Even's per-vertex flat decisions (≤ 14 per (vertex, phase) in data)
L-NEW successor 36 (Opus 5.5), D14 / D18, Lead reading L40. Lead 08:41Z (read 08:48Z, after box 78 RET-WCH was pushed): «BOX 78: GO on
FLAT-SRC. Measure the inheritance sources of dead-branch climbs first, then attempt the charge. Compare with L-RED's wall … TWO-SOURCE /
PREFIX / GAP-IN-PREFIX … Then park with a FINAL resume point.» Numbered 79. Written 08:49Z-08:54Z (date -u). Working note, unrefereed, not
a TARGET.md claim. G-N5-TIME OPEN.
- Tool box79/flatsrc.py; run.sh gives flatsrc_*.txt (1132 runs × N5 and N5-LZC).

## 1. A sharper count than box 77's Σ FLAT
- PHASE-RED's proof (box 77 §2) charges each Ξ-changing transition without a K-rise to ONE flat event. So it needs only:
  - FLATTR_P := the Ξ-changing transitions of P with no DEPTH rise;
  - CH_P ≤ n(n + 2) + FLATTR_P.
- Σ_v FLAT_P(v) counts (vertex, transition) pairs, i.e. breadth. FLATTR counts transitions.

## 2. DATA: the source of every flat transition is an Even switch
| engine | K-rise transitions | FLATTR | FLATTR containing a flat Even switch (FSW) | Ξ-flat | max FLATTR per phase | max flat switches per (x, phase) |
| --- | --- | --- | --- | --- | --- | --- |
| N5 | 9615 | 6503 | 6503 | 65 | 91 (returns_ph64, n 64) | 14 (red/n5inj returns_rt64, n 64) |
| N5-LZC | 9454 | 6379 | 6379 | 51 | 91 | 14 |
- FSW: some switched Even vertex x has Ξ_{k+1}(x) ≠ Ξ_k(x). That change is necessarily flat, since the transition has no DEPTH rise.
- On box 77's instances:
  | instance | FLATTR | max flat switches per (x, phase) | for comparison |
  | --- | --- | --- | --- |
  | nep92_n40 | 73 | 8 | FLAT(v) = 66 |
  | snap_n80_s62 | 77 | 8 | |
  | returns_ph64 | 91 | 10 | |
- So the 66 dead-branch climbs of one vertex are inherited, while the decisions behind them are spread: ≤ 14 flat switches per vertex.

## 3. CONJECTURE FLAT-SW, and the composition (PROVED, lane, given FLAT-SW)
- CONJECTURE FLAT-SW (OPEN; 12882 / 12882 in data). Every Ξ-changing transition without a DEPTH rise contains a switched Even vertex whose
  own Ξ value changes.
  - Why no proof here: the box 72 inheritance chain (TXC-SRC) can also end at an Odd σ̄-change (SBAR), or at a cycle node. FLAT-SW says
    such ends never occur alone in a flat transition. That needs an argument about σ̄ as Odd's optimum on G_{σ_{k+1}}: if every switched
    x keeps Ξ(x), then Ξ_k might still satisfy the optimality equations of G_{σ_{k+1}}. That would make Ξ_{k+1} = Ξ_k, against Ξ changing
    somewhere. Not completed (cycle cases).
- Corollary PHASE-RED′ (PROVED, lane, given FLAT-SW). For every phase P:
  |P| ≤ (4n(n − 1) + 1)·(n(n + 2) + Σ_x FLATSW_P(x) + 1),
  with FLATSW_P(x) the switches of Even x in P whose Ξ(x)-change is flat. Charge each flat transition to one flat switch; distinct
  transitions give distinct (x, transition) pairs. Then apply box 77 PHASE-RED.
- FLATSW_P(x) ≤ SW_P(x), x's switches in P: a per-vertex DECISION count. Inside each W-run piece of P (P is cut into W-runs by its
  fallbacks and λ_W-changes), RET-WCH (box 78) bounds x's switches by deg x + Σ_{e ∈ succ x} (WCH_F(e) + TL_F(x, e)).
- READING vs L-RED's wall (l-red 1c8d8667 notes/L-RED.md "Successor 32 PARK"):
  - Quoted: «Every Even switch y: z -> a needs W(a) to overtake W(z) by a switch on a's private prefix (TWO-SOURCE / PREFIX)».
  - That is the same charge direction as RET-WCH: an Even decision is paid by a W-change of its target.
  - FLAT-SW + PHASE-RED′ + RET-WCH therefore put phase length on the same per-vertex W-change count, [P-WCHτ], that L-RED's PREFIX
    points to. They do not break the wall: [P-WCHτ] is open, and PREFIX's private-prefix switches are its mechanism.

## DONE / FINDINGS / NEEDS
- DONE: box79/flatsrc.py, run.sh, flatsrc_*.txt; this note; check.sh "box 79" (pins nep92_n40).
- FINDINGS:
  1. DATA: every flat transition (12882 / 12882, both engines) contains a flat Even switch. Flat switches are ≤ 14 per (vertex, phase),
     against 66 inherited dead-branch climbs at one vertex.
  2. CONJECTURE FLAT-SW (OPEN, data 0 exceptions). Given it, PROVED (lane) PHASE-RED′:
     |P| ≤ (4n(n − 1) + 1)(n(n + 2) + Σ_x FLATSW_P(x) + 1).
  3. READING: with RET-WCH, phase length rests on Even's per-vertex decisions and hence on [P-WCHτ], the same quantity behind L-RED's
     PREFIX wall. A unification, not a bound.
- NEEDS: none from the owner. PARKED (FINAL resume point updated in notes/L-NEW.md).
