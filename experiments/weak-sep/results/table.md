# w(n,d) and s(n,d): exact values (SAT, verified by the independent checker)

Cell = w / s. '-' = not computed. '?' = strongness of the witness not analysed (slow family). '*' after w: the minimal weak separator found is not strong (its transition
graph has a reachable odd cycle). Universal-tree row: least leaves of an (n, d/2)-universal tree for even d
(CFGO Prop. 6.10/6.11 recursions f = g where they agree; brute force in wsep/utrees.py where run); equals s^E by
CFGO Thm 4.1 + Lemma 6.8. Conventions: E = edge-labelled multigraphs (CDFJLP/CFGO), S = at most one label per
ordered pair, V = vertex-labelled (TARGET.md). Columns: d = largest letter of the alphabet {1..d}.

## Convention E

| n \ d | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 / 1 | 1 / 1 | 1 / 1 | 1 / 1 | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| 2 | 2 / 2 | 2 / 2 | 3 / 3 | 3 / 3 | 3* / 4 | 3* / 4 | - / - | 4* / 5 | - / - | - / - | 4* / - |
| 3 | 3 / 3 | 3 / 3 | 5 / 5 | 5 / 5 | 7 / 7 | 7 / 7 | - / - | - / - | - / - | - / - | - / - |
| 4 | 4 / 4 | 4 / 4 | 8 / 8 | 8 / 8 | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| 5 | 5? / 5 | 5? / 5 | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |

## Convention S

| n \ d | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | - / - | 1 / 1 | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| 2 | 2 / 2 | 2 / 2 | 3 / 3 | 3 / 3 | 3? / 4 | 3? / 4 | - / - | - / - | - / - | - / - | - / - |
| 3 | 3 / 3 | 3 / 3 | 5 / 5 | 5 / 5 | 7? / 7 | 7? / 7 | - / - | - / - | - / - | - / - | - / - |
| 4 | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| 5 | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |

## Convention V

| n \ d | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 / 1 | 1 / 1 | 1 / 1 | 1 / 1 | - / - | - / - | - / - | - / - | - / - | - / - | - / - |
| 2 | 2 / 2 | 2 / 2 | 3 / 3 | 3* / 3 | 3* / 4 | 3* / 4 | 4* / - | 4* / 5 | 4? / - | 4? / - | 4? / - |
| 3 | 3 / 3 | 3 / 3 | 5* / 5 | 5 / 5 | 6* / 7 | 6* / 7 | - / - | 7* / - | - / - | 8? / - | - / - |
| 4 | 4 / 4 | 4 / 4 | 7 / 7 | 7 / 7 | - / 10 | - / 10 | - / - | - / - | - / - | - / - | - / - |
| 5 | 5? / - | 5? / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - | - / - |

## Universal trees (n, h = d/2), least leaves: g(n,h) <= value <= f(n,h) (CFGO Props 6.11 / 6.10)

| n \ d | 2 | 4 | 6 | 8 | 10 | 12 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | 2 | 3 | 4 | 5 | 6 | 7 |
| 3 | 3 | 5 | 7 | 9 | 11 | 13 |
| 4 | 4 | 8 | 13 | 19 | 26 | 34 |
| 5 | 5 | [10,11] | [16,19] | [23,29] | [31,41] | [40,55] |

