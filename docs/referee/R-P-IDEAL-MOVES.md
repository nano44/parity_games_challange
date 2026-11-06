# R-P-IDEAL-MOVES: REFEREE report on P-IDEAL-MOVES (L-NEW successor 57, box 187)
REFEREE successor 24 (Opus 5.5, D15), 2026-11-06 (date -u in the commit). Independent: docs/referee-2/ was not opened on this packet.
- Object: claude/l-new d86adc86 (an ancestor of origin), detached worktree. Re-measured:
  - packet 5ce2947d…, 202 lines; L-1 819c5815…, 4,313 bytes;
  - movescheck.py 8153717b…; movescheck.out 48740209…;
  - instances pass_d3_D3 8bca9764…, pass_d4_D4 3bf6a4a4…, pass_d5_D5 16be2e59…, m4_z4_r7 7c158e2f….
- Premises checked on trunk b876c884.

## 0. Verdicts
| § | statement | verdict |
| --- | --- | --- |
| §1 | REDUCE-XI; Corollary MOVES-EQUIV | SIGN |
| §2 | AND-GATE (a), (b), (c) | SIGN |
| §3 | WINDOW-DOUBLE (a), (b) (incl. BURST-2) | SIGN |
| §4 | SEG-WINDOW (a)-(e) | SIGN |
| §5 | DEAD-SEG (c ≤ 4); DEAD-LEV | SIGN (instances recomputed with my own simulator) |
| §6 | DATA / exclusions / TARGET diff | not to sign; check.sh block PASS; DATA rule applied (§3) |
| line | L-1 | MATCHES; optional MV-L1 |

## 1. Premises and proofs
- Premise quotes are FOUND verbatim on b876c884:
  - R105 ENC, LOCAL, MONO, XI-NEW, RISE («at any degree»);
  - R110's 𝓛^R_d;
  - R113 ALIGN, F0 and the notation quotes (KP_s, c_l, γ_l, F(l)).
  E-2 does not bear.
- REDUCE-XI: SIGN.
  - XI-NEW / RISE give, for the least-level mover h of step t ≥ 2, a strict Ξ-descendant y moving at t − 1. The last edge of a path to
    y makes y a Ξ-target, so y ∈ Z.
  - t ↦ t − 1 is injective.
- MOVES-EQUIV: SIGN. Each level-0 mover moves at most once (F0), and Z ∩ level ≥ 1 has ≤ 2d − 2 movers. This gives
  3 + (2d − 2)μ(d), and with μ ≤ 2d it gives 4d² − 4d + 3.
- AND-GATE: SIGN.
  - (a): the degree-2 A-set is {s} or both options, and the step takes the key-least option under s_t.
  - (b): s_t(x) = π_(s_(t−1))(x) = KP_(s_t)(x) at both consecutive moves; the windows are disjoint.
  - (c): v(x, a) is non-decreasing (ENC + MONO), so the strict chain holds.
- WINDOW-DOUBLE: SIGN.
  - (a): ALIGN's order formula, and c_j changes only at flips of the pair below.
  - (b): the PAIR-DOUBLE potential argument on a window, with Φ(a) ≤ 2. BURST-2 is the F_W(j − 1) = 0 case.
- SEG-WINDOW: SIGN.
  - (a): consecutive moves at t − 1 and t give a KP change at t (AND-GATE (b)), and by ALIGN that is a flip of (u, w).
  - (b): the pass-through descent ends at a moving pair, at level 0 at the latest, since level-0 keys are their own gates.
  - (c): (a) + WINDOW-DOUBLE (b), and F0 at l = 1.
  - (d): (a) + BURST-2.
  - (e): AND-GATE (a)-(c) with LOCAL. The chain's movers after x are not x (acyclic).

## 2. Independent checks (my simulator t3r_sim.py; no lane code)
- DEAD-SEG:
  - pass_d3_D3, start 110100: in 𝓛^R_3, T 4, mover 5 (level 2, ∈ Z) moves at 1, 2, 3; segment D 3, LM 0.
  - pass_d4_D4, start 01010111: T 4, mover 7 (level 3, ∈ Z) moves at 1-4; D 4, LM 0.
  - pass_d5_D5, start 0101010110: T 5, mover 9 (level 4, ∈ Z) moves at 1-5; D 5, LM 0.
  - So «D ≤ 2·LM + c» fails for c ≤ 4. All EQUAL to §5 and movescheck.out.
- DEAD-LEV: m4_z4_r7, stored start 10111010: in 𝓛^R_4, T 8, mover 4 (level 2, ∈ Z) moves at 1, 2, 3, 5, 6, 7, 8. That is 7 > 6.
  EQUAL.
- check.sh block «P-IDEAL-MOVES» at d86adc86: PASS (pins; movescheck.out regenerated identically).

## 3. DATA rule (every signed clause of L-1 has a counter or a no-DATA entry; counters read in movescheck.py)
| clause of L-1 | counter / entry | verdict |
| --- | --- | --- |
| REDUCE-XI: step t − 1 moves a member of Z; T ≤ 1 + Σ moves(z) | RX (l. 40: both) | MATCH |
| MOVES-EQUIV | «no separate DATA» | MATCH |
| AND-GATE: moves iff s ≠ π = KP | AGA (l. 51) | MATCH |
| AND-GATE: moves(x) ≤ 1 + min(KF_x, PF_x) | not counted; follows by arithmetic from AGB on every consecutive pair (disjoint windows, each with a π and a KP change) | MATCH by arithmetic (optional MV-L1) |
| AND-GATE: v(x, b) rises when π changes to b | AGC (l. 54) | MATCH |
| WINDOW-DOUBLE: pass-through clause | «no separate DATA» | MATCH |
| WINDOW-DOUBLE: F_W(j) ≤ 2 + 2F_W(j − 1) | WPD (l. 86), 1,288,162 pairs | MATCH |
| WINDOW-DOUBLE: BURST-2 | SWD (l. 80) | MATCH |
| SEG-WINDOW: flips at every step (a) | SWA | MATCH |
| SEG-WINDOW: a mover of level < l at every step (b) | SWB (also D ≤ 1 + LS + PT) | MATCH |
| SEG-WINDOW: D bound (c) | SWC | MATCH |
| SEG-WINDOW: 3-step clause (d) | «no separate DATA» | MATCH |
| SEG-WINDOW: a chain mover other than x moves (e) | SWE (l. 70-72; g.play lists the movers AFTER x, so the check is not vacuous) | MATCH |
| DEAD items | «DEAD-SEG …», «DEAD-LEV …» lines | MATCH |
- Optional MV-L1: the line's «AND-GATE 0 on … every pair of consecutive moves» covers moves ≤ 1 + min(KF, PF) only by arithmetic.
  Either say «(the min bound by arithmetic)», or leave it (C125 G-9 (iii) precedent: a bound that follows by arithmetic from counted
  checks is a note).

## 4. TARGET diff, line L-1
- TARGET: every statement is inside R104's IDEAL model; MOVES-EQUIV is an equivalence, not a bound. Not M3, not M4, not a gauntlet step.
  G-N5-TIME OPEN. Agreed.
- L-1:
  - Shape: one line, 68 «(» / 68 «)», depth never negative, 0 «|», one « — », «2026» once.
  - Definitions diffed against §0: T, Mv_t, moves (E2c), Z, KP_s, KF_x, π_s, PF_x, v_s, F_W(j), T^R(d), μ(d), metronome segment, LM
    all MATCH. The pair l − 2 is (2l − 4, 2l − 3); correct.
  - Claims MATCH their signed forms.
  - The source note names the packet; all proofs are in it.
- Verdict: L-1 MATCHES.

## DONE / FINDINGS / NEEDS
- DONE: premise byte tests; every proof re-derived; DEAD instances recomputed; check.sh block; DATA rule clause by clause; L-1.
- FINDINGS: every item SIGNED; L-1 MATCHES; optional MV-L1.
- NEEDS: none.
