# R6: S5 (Zadeh + index tie-break) and S6 (Cunningham + index order) on the FHZ counter encoding (L-RED, 2026-10-15)

Lead's ask (14:08Z): can a numbering of P_{n,1,1,1} (R5's family without pads; pads do not affect these rules) give Zadeh
or Cunningham an exponential run? The numbering is the adversary's. Tools: experiments/red/search_numbering.py (hill-climb
over all vertex permutations, vjfast zadeh / cunningham), search_classnum.py (class-structured numberings that define a
family: rank per label class, direction per class), gens_red.py fhz_P (labelled encoding).

## Verdict: HELD for both; the counter's order is not reachable by an index-fair rule on this family
| numbering | Zadeh, n = 2..6 | Cunningham, n = 2..6 |
| --- | --- | --- |
| identity (fhz.py export order) | 16, 36, 64, 100, 144 (= 4n^2) | 16, 32, 48, 64, 80 (= 16(n-1)) |
| best permutation found (n = 2, 3, 4; 1800 steps) | 22, 44, 76 | 23, 46, 72 |
| best class-structured scheme (fitted at n = 3) | 20, 42, 72, 110, 156 (second difference 8) | 20, 39, 64, 95, 132 (second difference 6) |
| vertices and edges ordered by first switch in the S7 kill run | 16, 36, 64, 100, 144 | 8, 12, 16, 20, 24 |
Every scheme that defines a family is quadratic; free permutations at fixed n gain a factor below 1.3.

## Why (Lead reading)
The S7 kill (R5) rests on one fact of the FHZ counter: while the lower levels count up, the next higher bit edge (b_{i+1}
-> w_{i+2}) is already improving but off the lower switches' plays, so a downstream-first rule may ignore it, and pads make
S7 prefer the lower levels. Zadeh and Cunningham cannot ignore it:
- Cunningham: between two consecutive switches of the same edge the pointer makes a full round of the cyclic order, and on
  that round it switches every improving edge it passes (the first one after the last switch, then the next, ...). The
  level-1 edges switch 2^{n-1} times; each of those rounds passes the improving higher bit edge and switches it. So the
  higher bit is set before the lower counter finishes, whatever the order; the run degenerates to O(n^2) (observed 4n and
  16(n-1)).
- Zadeh: the least-entered improving edge is taken; once the level-1 edges have been entered more often than the higher
  bit edge, the higher bit edge (entered O(1) times, improving) is preferred whenever it is improving; the index tie-break
  only decides among equal counts, and the counter needs the lower edge to win with a higher count. Observed 4n^2.
Both failures are the same one as in R3 section 3c, now from the other side: the counter has an improving higher bit
during the lower count (that is what makes it a counter), downstream-first rules may leave it alone, index-fair rules
may not. An exponential family for S5 or S6 therefore needs a counter in which the higher bit becomes improving only when
the lower bits have finished, i.e. the opposite dependence (higher bit enabled by the lower bits), which in a one-player
DAG is impossible together with resets (the dependence would have to run both ways, R5 section "Why"), and which in
two-player games is Friedmann's gate mechanism with its own order problems (R3). Not found in this box.

## DONE / FINDINGS / NEEDS
- DONE: the table above (vjfast), the labelled encoding (gens_red.py fhz_P), the first-switch-order experiment.
- FINDINGS: S5, S6 held on the FHZ encoding; the structural reason (index-fair rules must take the improving higher bit)
  is the complement of the S7 kill.
- NEEDS: none.
