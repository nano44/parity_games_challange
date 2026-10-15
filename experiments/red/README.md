# experiments/red: L-RED's adversary bench (report: docs/red/R1-MSF.md)
| file | what |
| --- | --- |
| vj.py | independent VJ valuation + MSF/LSF single switch, from Friedmann 1106.0778 section 3; brute-force validator; `vj.py msf game.pg [--start best|first|last|spec:v:w] [--trace]` |
| gens_red.py | adversarial families: `gated_bland N` (MSF takes 2^N - 1 iterations; n = 5N+2); `friedmann_Gn N` (1106.0778 Table 4 port, start printed as % start) and `padded*_Gn` (R3 pad schemes) |
| gate.py | generic gate relabelling of any sink game with designer labels per Even edge; demo: MSF and LSF both take 2^N - 1 on G_N with suitable labels |
| fhz.py | FHZ 1410.7530 G_{n,r,s,t} (weighted) + its sink-parity encoding + lockstep Random-Facet driver; `lockstep`, `lockstep3`, `relation`, `table`, `export` (report docs/red/R2-RAR.md) |
| xcheck_mi.py, trace_mi.py, search_pads.py | S7 (most-improved): fidelity check against vjfast and si.py; labelled trace with counts; random/hill-climb search over pad schemes (report docs/red/R3-S7.md) |
| correspond.py | MSF on gated_bland N == Bland's rule on DLMM's G_N, switch for switch |
| xcheck.py | validation of vj.py: brute force over Odd's counterstrategies, Zielonka, verify.py, and (with --lsi DIR) si.py |
| check.sh | self-check run by scripts/verify.sh (pins the counts and the instances) |
| instances/ | gated_bland_N6.pg, gated_bland_N8.pg (63 / 255 MSF iterations); claimF_len_cf1.pg, claimF_bit_cf2.pg (Claim F counterexamples, start sigma(2)=1); fhz_n3_r1s1t1.pg, fhz_n4_r1s1t1.pg, fhz_n5_r2s2t2.pg (R2 parity encodings of FHZ's graphs) |
