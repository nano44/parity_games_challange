# w(n,d) and s(n,d): exact values (SAT, verified by the independent checker)

Cell = w / s. '-' = not computed. '*' after w: the minimal weak separator found is not strong (its transition
graph has a reachable odd cycle). Universal-tree row: least leaves of an (n, d/2)-universal tree for even d
(CFGO Prop. 6.10/6.11 recursions f = g where they agree; brute force in wsep/utrees.py where run); equals s^E by
CFGO Thm 4.1 + Lemma 6.8. Conventions: E = edge-labelled multigraphs (CDFJLP/CFGO), S = at most one label per
ordered pair, V = vertex-labelled (TARGET.md). Columns: d = largest letter of the alphabet {1..d}.

## Convention E

| n \ d | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 / 1 | 1 / 1 | 1 / 1 | 1 / 1 | - / - | - / - |
| 2 | 2 / 2 | 2 / 2 | 3 / 3 | 3 / 3 | 3* / 4 | 3* / 4 |
| 3 | 3 / 3 | 3 / 3 | 5 / 5 | 5 / 5 | 7 / 7 | 7 / 7 |
| 4 | 4 / 4 | 4 / 4 | 8 / 8 | 8 / 8 | - / - | - / - |
| 5 | 5 / 5 | 5 / 5 | - / - | - / - | - / - | - / - |

## Convention S

| n \ d | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | - / - | 1 / 1 | - / - | - / - | - / - | - / - |
| 2 | 2 / 2 | 2 / 2 | 3 / 3 | 3 / 3 | 3* / 4 | 3* / 4 |
| 3 | 3 / 3 | 3 / 3 | 5 / 5 | 5 / 5 | 7 / - | - / - |
| 4 | - / - | - / - | - / - | - / - | - / - | - / - |
| 5 | - / - | - / - | - / - | - / - | - / - | - / - |

## Convention V

| n \ d | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 / 1 | 1 / 1 | 1 / 1 | 1 / 1 | - / - | - / - |
| 2 | 2 / 2 | 2 / 2 | 3 / 3 | 3* / 3 | 3* / 4 | 3* / 4 |
| 3 | 3 / 3 | 3 / 3 | 5* / 5 | 5 / 5 | 6* / 7 | 6* / 7 |
| 4 | 4 / 4 | 4 / 4 | 7 / 7 | 7 / 7 | - / - | - / - |
| 5 | - / - | - / - | - / - | - / - | - / - | - / - |

## Universal trees (n, h = d/2), least leaves: g(n,h) <= value <= f(n,h) (CFGO Props 6.11 / 6.10)

| n \ d | 2 | 4 | 6 |
| --- | --- | --- | --- |
| 1 | 1 | 1 | 1 |
| 2 | 2 | 3 | 4 |
| 3 | 3 | 5 | 7 |
| 4 | 4 | 8 | 13 |
| 5 | 5 | [10,11] | [16,19] |

