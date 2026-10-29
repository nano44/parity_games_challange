# N5-SF close-out (box 62): what stays true and useful after dwN
L-NEW successor 34 (Opus 5.5), D14 / D18. Written 2026-10-29 ~19:02Z (date -u). Lead 18:50Z: N5-SF recorded as a DEAD END
(docs/red/R116-sf-exponential.md, L-RED 29; reproduced by REFEREE-2, the Lead, and my own rebuild, N5-DW-box62.md).
- Dead end: N5-SF makes 19·2^N − 18 iterations on dwN. The exact obstruction is Lemma LATENCY at every set (N5-DW §2). Instance dw_8
  (n 217): 4846 iterations.

## True and reusable (labels as recorded by the Lead)
| item | where | label | use as a tool |
| --- | --- | --- | --- |
| SF-TERM, DECOUPLE | P-N5-SF-box55.md §2 | PROVED, signed by both referees | the τ-free orbit of a one-sided map; any variant whose arena opponent is a function of the mover's strategy |
| ONE-PLAYER, SF-RED (a)-(c) | P-N5-SF §3 | PROVED, signed | reducing a one-sided run to R17's λ-phases on G_σ̄: stretch ≤ n + m |
| SF-RED-R | N5-FC-box59.md §6.2 | PROVED (lane), under ASSUMPTION LOC (DATA-checked on 716 games) | dropping unreachable Odd vertices from any best-reply count |
| SF-RED-G | N5-PV-box60.md §3.2 | PROVED (lane), no LOC | segment decomposition: any run whose step equals N5's step on some fixed one-player game is cut into ≤ 1 + SBC_G pieces of < (n + m + 1)(n² − n + 1) steps |
| Lemma COUNT | N5-FC §1.1 | PROVED (lane) | counting unary / record counters |
| Lemma LATENCY | N5-FC §1.3 | PROVED (lane) | the hop-count race; the mechanism of fcN (records only) and dwN (every set) |
| Lemma DEPTH-COUNT, Theorem DEPTH-BOUND | N5-DEPTH-box61.md §1 | PROVED (lane) | any monotone-valuation run: ≤ n²(n + 1)^K transitions of depth ≤ K |
| Lemma FRAME-τ | N5-DW §5.2 | PROVED (lane) | N5's Even frame changes only by Odd's own improvements |
| Theorem EXIT (under NT), Lemma STALE | N5-SBC2-box56, N5-CARRY-box57 | PROVED (lane) | as stated there |

## Dead (instances)
- SF-POLY, SBC-QP, I-CUBIC, SBCG-QUAD, PV_G: dwN (dw_8, sha1 64f954f37903).
- PV, PV-PLAY: fcobs_3, fcobsP_3.
- FLIP-REC°: so_sorl_n32.
- Value-prefix potentials: switchbestexp_8.
- CARRY-CUT (box 57): moot, since F is exponential anyway.

## Still OPEN and relevant to N5 (G-N5-TIME)
- CONJECTURE FRAME-STRETCH (N5-DW §5.2; 0 / 719).
- CONJECTURE LOOP (N5-PV §4).
- Whether two coupled counters, each clocking the other's frame, can make N5 exponential.
