# R-N5-SRC-C: REFEREE §C on P-N5-SRC: cross-map against REFEREE-2 24 (R2-N5-SRC, claude/referee-2 e8c1b62d), joint gap map
Referee: REFEREE (successor 20), Opus 5.5 (D15).
- The Lead gave the §C word at 22:56Z (read 23:13Z by date -u).
- My report R-N5-SRC.md (81f6b89c) was written and pushed before I opened R2-N5-SRC.md. I opened it for the ONE-STEP check (R-N5-SETTLE
  Addendum 1, 8951ef7c) and for this §C.

## 1. Cross-map
| item | REFEREE (R-N5-SRC) | REFEREE-2 (R2-N5-SRC) | joint reading |
| --- | --- | --- | --- |
| (R1), (R2), definitions | checked | checked | agree |
| PLAY-CAUSE^S | SIGNED | SIGNED | agree. Both: it needs no σ̄ / CN condition, since D_k ∪ D_(k+1) ∪ C ⊆ S_k |
| (S_j)/(X_j), C1-C7 | SIGNED, G-SRC-1 closed by my four-way split (§3) | SIGNED, G-SRC-1 closed by Lemma ONE-STEP (§3.2) | the SAME gap, found independently, closed by the same argument (top of the new cycle: c / even / odd). ONE-STEP is the proof of record (Lead reading L41); I signed it in R-N5-SETTLE Addendum 1 |
| Lemma TAIL | SIGNED | SIGNED | agree (both: the LEX branch by induction on L, IDX immediate) |
| SRC-SETTLE, SRC-COUNT, EQUIVALENCE | SIGNED | SIGNED | agree. Both note that the line's «maximal run» narrows the packet's «every source block» |
| line SRC-L1 (|F|) | REQUIRED | REQUIRED | same |
| line SRC-L2 (H_t) | REQUIRED | REQUIRED, and also σ_new as a non-line symbol | same; I take REFEREE-2's exact text «σ_(k+1) … H_k» |
| line: proof note cites the SETTLE induction | SRC-L3 precision (cite G-SRC-1) | SRC-L3 REQUIRED (cite ONE-STEP) | I agree it is REQUIRED: the cited induction is signed only through ONE-STEP. Upgraded |
| line: «are not events» wording | not raised | N-1 (precision) | agree |
| DATA | n ≤ 100: 0 violations; CYC 3 actual Case-2 switches with y on c's cycle, all with top c | full corpus + 20,000 random runs: 0 violations; OS 852,572 checks, 4 «new top» configurations (ret22_n40 + start), none at an actual switch | consistent. My count is over actual Case-2 steps; REFEREE-2's OS is over all eligible z. Neither shows a wrong actual step |

## 2. Joint gap map
- Packet items to sign: no open gap. G-SRC-1 (inherited from [SET]) is CLOSED by ONE-STEP, which is signed by both referees (REFEREE-2 as
  author, mine in R-N5-SETTLE Addendum 1). Nothing FALSE.
- Line, REQUIRED: SRC-L1 (|F|), SRC-L2 (H_k / σ_(k+1) in the R57 gloss), SRC-L3 (cite ONE-STEP in the proof note, referee-originated, L41).
- Line, precision: name V; REFEREE-2's N-1 («not source events»).

## DONE / FINDINGS / NEEDS
- DONE: this §C.
- FINDINGS: SRC is signed by both referees; G-SRC-1 is one gap found by both and closed by ONE-STEP; the line needs SRC-L1, L2, L3.
- NEEDS: Lead: SRC L-2 with SRC-L1..L3, for successor 21 to word-diff.
