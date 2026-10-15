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

### Gadget-chain family search for MSF (famsearch.py: hill-climb over G-vertex gadget templates chained k times plus a sink; score = iterations at k = K; then the best template swept over k)
| search | iterations for k = 2..11 | growth |
|---|---|---|
| G=4, K=7, ascending relevance | 29, 66, 117, 186, 273, 382, 513, 670, 853, 1066 | second differences 14..30: between k^2 and k^3 |
| G=5, K=6, ascending | 24, 71, 143, 245, 379, 545, 743, 973, 1235 (k ≤ 10) | second difference constant 32: quadratic |
| G=4, K=7, seeded with the DLMM Bland level | 18, 47, 90, 149, 224, 315, 422, 545, 684, 839 | second difference constant 16: quadratic |
| G=4, K=7, descending relevance | 26, 53, 83, 116, 152, 191, 233, 278, 326, 377 | second difference 3..6: quadratic |

No search found super-polynomial growth in k (n = Gk + 1).

### PGSolver cunninghamexp (gens.py port; "Binary-Case Exponential Lower Bound for Cunningham's rule"; n = 9N + 1)
| N | cunningham-lb (PGSolver's lower-bound edge ordering, switch_cunningham.ml:104-148) | cunningham (index order, S6) | zadeh (S5) | msf | lsf | switch-all |
|---|---|---|---|---|---|---|
| 2 | 7 | 3 | 3 | 3 | 3 | 4 |
| 4 | 121 | 9 | 9 | 9 | 9 | 4 |
| 6 | 799 | 15 | 15 | 15 | 15 | 4 |
| 8 | 4309 | 21 | 21 | 21 | 21 | 4 |
| 10 | 21451 | 27 | 27 | 27 | 27 | 4 |

Best-reward start. The family blows up Cunningham's rule under the ordering it was built for (×2.2 per N) and is linear under the
index order: the lower-bound ordering is not lexicographic in any vertex numbering (edges of e0 sit at positions 1 and 16 of 22
for N = 3), so the index-order rule is not killed by relabelling this instance. Zadeh with the index tie-break is linear here.

### Random-Facet* (fixed random permutation; the variant whose lower bound stands) on the randomfacetsubexp port (vjfast rfstar, best-reward start, 8 seeds)
| N | n | switches (8 seeds) |
|---|---|---|
| 3 | 68 | 76 84 69 68 100 70 86 69 |
| 5 | 207 | 417 614 608 646 608 531 622 460 |
| 7 | 289 | 1369 593 1568 1005 1210 942 1828 1101 |
| 8 | 330 | 904 995 1101 1117 875 1434 1525 1453 |

At these sizes Random-Facet* and Random-Action-Removal behave alike on the family (the published 2^Ω~(√m) bound for
Random-Facet* is for the paper's initial strategy and is invisible at N ≤ 8); the family does not discriminate between
the two variants at reachable sizes.

### S5 Zadeh+index and S6 Cunningham+index: searches (Python engine)
Adversarial hill-climb maxima (n = 4..10; 100 restarts x 2000 steps or 700 s per n):
| rule | n=4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|
| zadeh | 7 | 16 | 28 | 43 | 63 | 71 | 100 |
| cunningham | 8 | 16 | 29 | 49 | 58 | 69 | 84 |

Gadget-chain family search (G = 4, K = 7; best template swept over k = 2..11):
| rule | iterations k = 2..11 | growth |
|---|---|---|
| zadeh | 16, 61, 148, 275, 442, 649, 896, 1183, 1510, 1877 | second differences 40: quadratic |
| cunningham | 7, 27, 72, 142, 237, 357, 502, 672, 867, 1087 | second differences 25..30: quadratic |

No super-polynomial growth found for either (the searches are weak evidence; see S5.md / S6.md: "not covered, not defended").

### C++ engine validation (xcheck_fast.py): 1,500 random games, n ≤ 16: valuations identical to si.py on 4,500 (game, strategy)
pairs; iteration counts identical for switch-all, msf, lsf, zadeh, cunningham; regions = py-zlk with verified strategies for
all rules incl. rar and random-edge. XCHECK-FAST PASS.

### S7 most-improved (vjfast; invariant tie-break, index last resort never used on these)
| family | iterations |
|---|---|
| gated_bland N = 4..12 | 1, 1, 1, 1, 1 |
| dlmm_bland N = 4..12 | 3, 5, 7, 9, 11 |
| dlmm_ML L = 4..12 (sigma_0) | 4, 6, 8, 10, 12 |
| zadehexp N = 4..12 | 27, 43, 59, 75, 91 |
| cunninghamexp N = 4..12 | 9, 15, 21, 27, 33 |
| switchallexp N = 2, 4, 6, 8 | 34, 90, 202, 354 |
| switchbestexp N = 2, 4, 6, 8 | 76, 142, 210, 278 |
| gated_zadehexp N = 2..6 | 6, 13, 16, 21, 24 |
| gated_switchallexp N = 2..6 | 31, 30, 39, 48, 57 |
| gated_switchbestexp N = 2..6 | 80, 203, 314, 658, 974 |
Adversarial maxima n = 5..10: 9, 14, 21, 26, 29, 38. Gadget chains (G = 4): quadratic (see S7.md).

### L-RED's fhz_padded (FHZ one-player Random-Facet counter + linear pads; claude/l-red ffa4e15), vjfast, best-reward start
| n | V | most-improved (S7) | lsf | zadeh (S5) | cunningham (S6) | msf | switch-all | rar (5 seeds) |
|---|---|---|---|---|---|---|---|---|
| 2 | 64 | 16 | 16 | 16 | 16 | 8 | 6 | 10 8 8 8 14 |
| 3 | 112 | 44 | 44 | 36 | 32 | 12 | 9 | 14 12 18 18 12 |
| 4 | 171 | 104 | 104 | 64 | 48 | 16 | 12 | 24 32 22 26 38 |
| 5 | 241 | 228 | 228 | 100 | 64 | 20 | 15 | 58 26 42 28 68 |
| 6 | 322 | 480 | 480 | 144 | 80 | 24 | 18 | 48 52 40 42 74 |
| 7 | 414 | 988 | 988 | 196 | 96 | 28 | 21 | 64 86 64 32 72 |
S7 and LSF: i(n) = 2 i(n-1) + 4n (exponential; L-RED's numbers reproduced exactly). Zadeh+index: 4n²; Cunningham+index: 16n.
