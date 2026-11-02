# R194 The (a′) lap recipe (L-NEW box 137 §6) against the realised IDEAL runs: in every REALIZE game the carry already IS a gating event; each transition is its own epoch (GCH = FL − 1 on all 8 realised pins), so «make the carry a gating event, then nest laps» is the IDEAL-ACYC question again and adds no new lever (L-RED successor 46)
Started 2026-11-02 18:10Z (queue item (a′); Lead 18:06Z «go on to the (a′) lap recipe»; date -u). Labels: DATA, READING, OPEN.
Sources read: L-NEW box 137 (claude/l-new 5c93eaf8, docs/new/N5-REL-box137.md §0, §1, §4, §6), box132/anchor.py (epoch / GCH
definition). Premise for the realised side: RESULTS R104 (an acyclic IDEAL genome realised by the REALIZE gadgets is one real N5 FL run,
state for state). Not a TARGET.md claim. G-N5-TIME OPEN. No kill, no family.

## 0. Answer
- Box 137 §6 asks for a lap gadget whose carry is a GATING event (a change of σ̄, of Ξ on ODIFF, or of Ξ on the W-cycle nodes), so
  that FL runs contain many epochs (GCH growing), then nested laps. On realised IDEAL games this is already the case at EVERY transition
  (DATA, r194/gch.py = box132/anchor.py's epoch / GCH count as a function):

| pin (realised IDEAL-ACYC genome) | n | FL | GCH | epochs | MOVMAX |
| --- | --- | --- | --- | --- | --- |
| stab_d4_n126 (R187) | 126 | 32 | 31 | 32 | 10 |
| stab_g24_n246 (R187) | 246 | 64 | 63 | 64 | 10 |
| g4_L12_n62 (R188) | 62 | 12 | 11 | 12 | 4 |
| lag2c_d4_n62 (R189) | 62 | 9 | 8 | 9 | 3 |
| nest3_D3_p6_n84 (R191) | 84 | 6 | 5 | 6 | 3 |
| u_d8_D3_n214 (R191) | 214 | 24 | 23 | 24 | 6 |
| rk_D3_k3_d8_n214 (R192) | 214 | 20 | 19 | 20 | 6 |
| (box 137) ret2_n37, cwmov2_n57 | 37 / 57 | 7 / 5 + 1 | 0 / 1 + 0 | 1 / 2 + 1 | 6 / 4 |
  anchor.py itself on stab_d4_n126: EPOCHS 32, GCH 31, XIB 31 (every boundary is a Ξ change on ODIFF), VIOL 0, BOUNDVIOL 0.
- READING (why): in the REALIZE game the ODIFF set is the set of gates (σ̄ takes the β-face, τ the W-face), and Ξ at a gate (x, k) is
  β(x, k) followed by the current value of its Ξ-target. Every IDEAL step moves some mover y to a strictly better face, so Ξ(y) rises
  strictly (R178 (ii): Ξ is monotone). Every gate whose β-play reaches y then changes. So a transition is a gating event as soon as a
  mover with a Ξ-in-edge moves; in all 8 pins that is every transition. (Not proved here against the frozen packet's lemma statements:
  READING + DATA.)
- Consequence. On realised games GCH = FL − 1, so «GCH super-polynomial» ⟺ «FL super-polynomial» ⟺ (R104) a super-polynomial
  IDEAL-ACYC run ⟺ (box 144 CHAIN-BACK) U super-polynomial. The lap recipe's two ingredients are, in IDEAL terms:
  - the lap (chooser with k options moving k times, each join a Ξ-release, box 137 DOUBLE-PULL) = a degree-k mover whose moves are
    Ξ-helped; R191 ROT-CAP caps the unhelped ones at k − 2 per window;
  - the carry (root-side key drop that resets the joiners) = a lower-level key flip (R191 KEY-ALT).
  Nesting «laps of x = moves of a» is then a doubling of helps along a Ξ-chain, which is exactly what U-climbs and NEST(d) test (R189
  NEST-DEAD at degree 2, R191 NEST-DEAD-3 at degree 3: dead; U linear at d ≤ 12 in every climb so far).
- So (a′) gives no new route beyond the IDEAL-ACYC search: the open object is still U (box 144). Native (non-realised) games such as
  ret2_n37 have long epochs (GCH 0, 7 transitions); there the lap repeats inside one epoch, bounded by box 137 KCH-GCH (a).

## 1. Files
experiments/red/r194/gch.py (per FL run: FL, GCH, epochs, MOVMAX; the box132/anchor.py definitions as a function). check.sh block «R194».
