# N5-ODDXI (box 126, last box of successor 44): Ξ-changes at Odd vertices are inherited down the play from Even switches; the Odd minimum adds no structure, and the count relocates again
- L-NEW successor 44 (Opus 5.5), D14 / D18. Lead GO 2026-11-01 05:32Z: «GO for (a) as your LAST box, BOX 126: the per-Odd-vertex Ξ-change
  count against out-degree and n. … check whether its depth or fan-out has any structure that the Odd min gives and the Even max does not
  (e.g. the minimiser changes only when the current minimiser rises). Use nep92_n40 as the extreme test. If it relocates again, say so in
  one line and stop.»
- Tool: experiments/new/box126/oddxi.py. Log: box126/oddxi.txt.
  - Instances: nep92_n40 (+ start) and L-RED's fbA_K8 / fbg_K12 / cp_K4 (repaired starts), plus b5_os_n40.
  - All are pinned in boxes 116b / 113 / 121 / 125 (Oink verified, n5b identical).
  - No corpus run was made in this box.

## 0. Answer (one line)
- It relocates again. Every Ξ-change at an Odd vertex v is a Ξ-change of v's current minimiser σ̄(v) at the same transition, and the chain
  of such changes runs down v's play to an Even vertex switched at that transition. So ΞCH(v) ≤ #{k : v's play at k meets an Even switch of
  k}. This is PLAY-CONTAIN's count, and the Odd minimum contributes nothing beyond it.

## 1. DATA (box126/oddxi.txt)
| instance | n | K | Ξ-changes at Odd vertices | with the minimiser rising | σ̄-moves | old minimiser rose | chain ends at an Even switch | longest chain | top Odd vertex: deg, ΞCH, successors used |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| nep92_n40 | 40 | 98 | 357 | 357 | 170 | 170 | 357 | 20 | 0: 16, 76, 15 |
| fbA_K8_m8_m8 | 192 | 88 | 2,433 | 2,433 | 144 | 144 | 2,433 | 9 | 124: 1, 40, 1 |
| fbg_K12_m6_m24 | 290 | 404 | 4,170 | 4,170 | 170 | 170 | 4,170 | 53 | 185: 2, 62, 2 |
| cp_K4 | 192 | 44 | 329 | 329 | 16 | 16 | 329 | 4 | 22: 2, 8, 2 |
| b5_os_n40 | 40 | 81 | 18 | 18 | 1 | 1 | 18 | 12 | see log |

- The out-degree does not govern the count. On fbA_K8 an Odd vertex of out-degree 1 has 40 Ξ-changes. nep92_n40's vertex 0 (out-degree 16)
  has 76, with 15 of its 16 successors used as minimiser.
- No FLAT σ̄-moves occur on these instances. No chain enters through a play's cycle (END cyc 0).

## 2. What is provable, and what is not claimed
- MIN-RISE, the form the Lead suggested: «at Odd v, if σ̄(v) moves at k and the move is not a tie, the old minimiser's Ξ changed at k».
  - Argument (READING, not signed as a lane proof): all Ξ-values are non-decreasing (RESULTS R18 (d) Lemma S (b)). If w0 := σ̄_k(v) kept
    its value, then every other successor's candidate value at v could only rise. So w0 stays a minimiser, and a move away from it is a tie.
  - The step «v's candidate value through w is v ⊕ Ξ(w)» needs w's optimal play to avoid v. When it does not (v on the cycle), the
    candidate is a cycle value and the step needs care.
  - I state MIN-RISE as DATA (100% on the five instances) with this proof sketch. It is not PROVED here.
- Even when MIN-RISE holds, it charges each Ξ(v)-change to a Ξ-change of ONE successor (the current minimiser) at the same transition.
  Following the charge down the play ends at an Even switch (box 121 PLAY-CONTAIN). That gives no bound per vertex: it is the same count as
  «transitions at which v's play is touched by an Even switch». No new structure appears.

## DONE / FINDINGS / NEEDS
- DONE: this note; experiments/new/box126/{oddxi.py, oddxi.txt}; check.sh block «box 126».
- FINDINGS:
  - Relocates again: per-Odd-vertex Ξ-changes = Ξ-changes of the current minimiser = PLAY-CONTAIN's count.
  - MIN-RISE holds on all data (7,307 / 7,307 events, 501 / 501 σ̄-moves); proof only sketched.
  - The out-degree is irrelevant (an out-degree-1 vertex has 40 changes).
- NEEDS: none from this box; the lane parks (Lead 05:32Z).
