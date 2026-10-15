# experiments/red: L-RED's adversary bench (report: docs/red/R1-MSF.md)
| file | what |
| --- | --- |
| vj.py | independent VJ valuation + MSF/LSF single switch, from Friedmann 1106.0778 section 3; brute-force validator; `vj.py msf game.pg [--start best|first|last|spec:v:w] [--trace]` |
| gens_red.py | adversarial families: `gated_bland N` (MSF takes 2^N - 1 iterations; n = 5N+2); `fhz_padded n` (S7 takes 8*2^n - 4n - 8 iterations on Theta(n^2) vertices, R5); `fhz_P n` (labelled encoding without pads, R6); `friedmann_Gn N` (1106.0778 Table 4 port, start printed as % start) and `padded*_Gn` (R3 pad schemes) |
| gate.py | generic gate relabelling of any sink game with designer labels per Even edge; demo: MSF and LSF both take 2^N - 1 on G_N with suitable labels |
| fhz.py | FHZ 1410.7530 G_{n,r,s,t} (weighted) + its sink-parity encoding + lockstep Random-Facet driver; `lockstep`, `lockstep3`, `relation`, `table`, `export` (report docs/red/R2-RAR.md) |
| xcheck_mi.py, trace_mi.py, search_pads.py | S7 (most-improved): fidelity check against vjfast and si.py; labelled trace with counts; random/hill-climb search over pad schemes (report docs/red/R3-S7.md) |
| zadeh_lb.py | Zadeh with PGSolver's lower-bound tie-break (switch_zadeh.ml port) on labelled zadehexp instances; `--tie lb|index|val`, `--trace` (bit state at every tie), `--rev` (pairs chosen in both orders); checks whether a fixed total order of the edges reproduces the run (R7) |
| zadeh_anyorder.py | exhaustive DFS over the tie decisions of Zadeh under ANY fixed total order (upper bound on every index order), `--prefer` follows a given run while allowed (R7) |
| zadeh_order_climb.py, zadeh_climb_fast.py | hill-climb over vertex numberings for S5 with the exp-game start (in-process vj.py / vjfast-scored, `--out` writes the best numbering) (R7) |
| dtl/dtl_search.py, dtl/dtl_flips.py, dtl/gens_dtl.py | DTL box (R8): hill-climb over small games for Oink DTL's tangle count or unsolved vertices; strategy-flip census over random games or random walks from a game; `chain n` family (n - 2 tangles in one search); `counter_dftl n`, `counter_odftl n` = van Dijk's generators from Oink's dftl branch (a028e62, d54dfad), transcribed |
| search_numbering.py, search_classnum.py | S5/S6: hill-climb over vertex permutations / class-structured numberings, scored by vjfast zadeh or cunningham (report docs/red/R4-S5S6.md) |
| antichain_check.py | downstream-first diagnostic (R3 3c): along a rule's run, how often the chosen vertex is upstream of another improving vertex; S7 never is (Lemma D) |
| df_fhz.py, df_lp.py, df_search.py, df_fast.py, pad_scheme.py, pad_fhz.py | Question DF (R5): exact longest downstream-first runs on FHZ's graph and on random small games; pad-feasibility LP; structured pad schemes and pad hill-climbs for S7 |
| correspond.py | MSF on gated_bland N == Bland's rule on DLMM's G_N, switch for switch |
| xcheck.py | validation of vj.py: brute force over Odd's counterstrategies, Zielonka, verify.py, and (with --lsi DIR) si.py |
| check.sh | self-check run by scripts/verify.sh (pins the counts and the instances) |
| instances/ | gated_bland_N6.pg, gated_bland_N8.pg (63 / 255 MSF iterations); claimF_len_cf1.pg, claimF_bit_cf2.pg (Claim F counterexamples, start sigma(2)=1); fhz_n3_r1s1t1.pg, fhz_n4_r1s1t1.pg, fhz_n5_r2s2t2.pg (R2 parity encodings of FHZ's graphs); fhz_padded_n4.pg, fhz_padded_n6.pg (R5: S7 takes 104 / 480 iterations) |
