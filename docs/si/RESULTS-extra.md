## Hand-recorded runs (appended by report.py; L-SI)

### DLMM M_L sink-game port (gens.py dlmm_ML, start sigma_0 of Lemma 5.4; n = 3L + 4)
| L | lsf | steepest | msf | msfa | most-improved | switch-all | rar (mean of 10) |
|---|---|---|---|---|---|---|---|
| 2 | 4 | 4 | 4 | 4 | 2 | 2 | 3.0 |
| 3 | 11 | 11 | 7 | 7 | 3 | 2 | 4.8 |
| 4 | 26 | 26 | 10 | 10 | 4 | 2 | 5.8 |
| 5 | 57 | 57 | 13 | 13 | 5 | 2 | 8.2 |
| 6 | 120 | 120 | 16 | 16 | 6 | 2 | 9.0 |
| 7 | 247 | 247 | 19 | 19 | 7 | 2 | 14.4 |
| 8 | 502 | 502 | 22 | 22 | 8 | 2 | 13.0 |
| 9 | 1013 | 1013 | 25 | - | - | 2 | - |
| 10 | 2036 | 2036 | 28 | - | - | 2 | - |

lsf = steepest = 2^(L+1) - (L+2) (exponential); msf = 3L - 2.

### DLMM Bland counter G_n (gens.py dlmm_bland; start sigma_0 = "first"; n = 2n_levels + 2)
| levels | lsf | msf | steepest | switch-all | rar (mean of 10) |
|---|---|---|---|---|---|
| 4 | 15 | 1 | 1 | 4 | 4.0 |
| 8 | 255 | 1 | 1 | 8 | 6.8 |
| 12 | 4095 | 1 | 1 | 12 | 12.2 |

### Cross-lane (Lead 11:21Z): L-ALG's block-structured games, claude/l-alg a5164a4, experiments/alg/instances/zp_ga_K*.pg
| instance | n | msf | msfa | lsf | steepest | switch-all |
|---|---|---|---|---|---|---|
| zp_ga_K6_n24_calls129 | 24 | 3 | 3 | 3 | 3 | 2 |
| zp_ga_K8_n32_calls247 | 32 | 2 | 2 | 4 | 2 | 3 |
| zp_ga_K10_n40_calls659 | 40 | 7 | 7 | 12 | 7 | 4 |
| zp_ga_K12_n48_calls1943 | 48 | 12 | 12 | 13 | 11 | 4 |

Trivial for every SI rule (the games are built to blow up a Zielonka+psolC hybrid, not SI).
