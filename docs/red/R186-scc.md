# R186 The mover 2-cycle as an SCC charge: it closes through KEY-CHARGE, which charges every move, in an SCC or not, to key changes below it; it does not close to a polynomial, because KEY-CHARGE multiplies per W-level (DEPTH). A ring of gate-sink movers is linear by GATE-SINK. DATA: no D″-cycle in the R183 ring/feedback gadget families (L-RED successor 43)
Written 2026-11-01 ~20:2xZ (date -u), after the Lead's GO of 20:07Z: «R185 = the mover 2-cycle as an SCC charge … If it closes,
D″-cycles are paid by KCH … Otherwise build the longest mutual-feeding chain». That GO crossed my R185 report (D″-cycles / CN-UP,
docs/red/R185-dprime.md), so this note is numbered R186. Labels: PROVED (lane), DATA, READING. G-N5-TIME stays OPEN. No kill.

## 0. Answer
- The charge closes, but only to KEY-CHARGE's bound, and that bound is exponential in W-depth.
- PROVED (lane), a direct consequence of R183 Lemma OVT-KEY. In any stretch (D″-SCC or not):
  - every move of an Even x ∉ CN belongs to a key-stretch of x;
  - per key-stretch, x moves ≤ |T_x| − 1 times.
  - So the moves of a D″-SCC C in an FL run are ≤ Σ_(x ∈ C) (|T_x| − 1)(1 + KCH_x).
  - Hence FL ≤ Σ_(x ∉ CN) (|T_x| − 1)(1 + KCH_x) + CNONLY, whatever D″ looks like.
  - D″-cycles therefore need no separate potential: they are paid by KCH, as asked.
- What does not close: KCH_x counts moves strictly below x in W-level (B_x). The recursion is μ_ℓ ≤ (Δ − 1)(1 + n·μ_(ℓ−1)), which gives
  R183's DEPTH bound n(Δn)^(ℓ*−1).
  - Polynomiality needs one more fact: a key change below x re-releases x only O(1) times, independent of depth.
  - The SCC structure gives no handle on that. The SCC edges are Ξ-segment edges, whereas KCH runs along W-key edges.
- Ring of movers reading each other through gates (the requested build):
  - If each gate's W-face goes to the W-cycle node (the odxi_n37 / chain.py shape), then B_x = ∅ for every ring mover. By GATE-SINK,
    each moves ≤ |T_x| − 1 times per FL run, so the ring contributes ≤ Σ (|T_x| − 1) moves per run: linear, whatever its D″ structure.
  - A ring that needs a D″-cycle to matter must give its movers W-depth: gates whose W-faces read lower choice vertices. That is
    R178's graded two-face shape, and its naive realisation collapses (R183 §2: 0 FL runs).
- DATA: the R183 gadget families (chains, rings and feedback with free targets; k 4-32, n 45-129) have NO D″-cyclic stretch
  (dcyc.py DM2=1):

| instance | n | stretches | D″-cyclic | longest stretch | max height | own-segment hits |
| --- | --- | --- | --- | --- | --- | --- |
| s2_k4 | 45 | 4 | 0 | 3 | 11 | 24 |
| s2_k8 | 57 | 6 | 0 | 2 | 11 | 26 |
| s2_k16 | 81 | 5 | 0 | 2 | 11 | 24 |
| s2_k32 | 129 | 6 | 0 | 2 | 12 | 26 |
| s_k16 | 81 | 7 | 0 | 1 | 10 | 28 |
- The only D″-cycles known are R185's (dcyc3_n48, d2cyc4_n72). They are inert and temporally split.

## 1. For the proof side (READING)
- The FL face is: FL ≤ Σ_(x ∉ CN) (|T_x| − 1)(1 + KCH_x) + CNONLY.
  - CNONLY is controlled per FL run by R185 Lemma CN-UP: between two consecutive shortcuts, a cycle node c makes ≤ |T_c| − 1 up
    moves. The number of shortcuts is open (0 alternations in the data).
  - The open quantity is KCH, i.e. moves on W-key paths below x.
- R177's LADDERBF shows that with adversarial availability KCH does multiply per level (2(2^(d+1) − d − 2)). So the missing statement
  is a Ξ-side «release once per key change».
  - It needs σ̄-optimality or τ-stability: in the IDEAL model, where both are fixed by fiat, the question is exactly IDEAL-LIN.
