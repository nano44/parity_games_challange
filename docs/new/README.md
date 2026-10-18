# L-NEW: (c) design lane (D14, Lead reading L35). One line per approach.
| id | approach | status |
| --- | --- | --- |
| N0-S5 | Zadeh least-entered rule, index tie-break (L-SI S5), under adversarial renumbering | not killed (fast test, S5S6-renum.md); sweep still running |
| N0-S6 | Cunningham round-robin, index order (L-SI S6), under adversarial renumbering | not killed (fast test, S5S6-renum.md); sweep still running |
| N1 | DISC-ANNEAL: discount 1-2^-j annealing, warm-started switch-all (N1-disc-anneal.md) | implemented; UNDER TEST (not killed so far; switchallexp quadratic vs plain doubling; no claim) |
| N2 | PRIO-ANNEAL: top-down priority coarsening, warm-started SI (N2-prio-anneal.md) | proposed |
| N3 | BLACKWELL-PATH: exact discount homotopy (N3-blackwell-path.md) | proposed |
| X1 | SCALE-VI: bit-scaled energy value iteration, warm-started from 2x the coarser measure | screened out before code (argument, no instance): Odd-region flips cost a climb to the top value ~ n*W_k per phase, i.e. small-progress-measure behaviour |
