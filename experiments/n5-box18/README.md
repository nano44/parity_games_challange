# Box 18: carries (T32 E6), LIP (E1), HAM-MONO and NEST-FACE (E7) (L-COMP successor 7)
Lead brief 2026-10-29 10:23Z (D18). Source: L-LIT T32, docs/lit/T32-n5-frontier-crossfield.md on claude/l-lit a06dc24a (read only),
entries E1, E6, E7. Every number is DATA except where labelled PROVED. Engine: n5b SPEC via experiments/n5-box17/box17.py. Its state
sequences, σ̄ and REL segments equal L-SI's engine on every instance checked in box 17. Phases use the key (λ_Ξ, τ) of RESULTS R38 (a).
nm.py --key r104 uses L-RED gatep.py's key (τ, λ_Ξ, λ_Ξτ), and gives the same numbers on pl130_n40 and l121reader_n41.

## Tools
| file | what |
| --- | --- |
| nm.py | per (vertex v, phase P): PCH (P-changes of P(Ξ v)), NM (carries = non-MATCHED P-changes, T32 §E6 definition), the same on fixed-top changes (top of A = top of B, both nonempty), RESET (fixed-top change removing an element, L-RED R104) and RESET_STALL (a reset followed by an in-phase fallback) |
| matchtest.py | nm.matched against L-LIT's brute-force match() from docs/lit/T32-match-check.py (its definitions exec'd, its own loop not run) on every ordered pair of subsets of K ranks, every parity pattern |
| inv.py | LIP (three readings), HAM-MONO (strict, weak; all ranks / even ranks / odd ranks), NEST-FACE (ii) |
| agg.py | aggregates the logs in results/ |

## Cross-checks (done first)
- matchtest.py: K = 5, 31,744 pairs, 0 disagreements. K = 6, 258,048 pairs (all 64 parity patterns, not only T32's 40 random ones),
  0 disagreements. Of the 129,024 improving pairs at K = 6, 50,756 are carries.
- nm.py vs L-RED gatep.py (best phase, summed over gates): pl130_n40 PCH 157 / RESET 133 / RESET_STALL 8, and l121reader_n41 187 / 157 / 0.
  Both identical to gatep.py's output. l121reader_n41 vertex 40 has 71 P-changes in phase [1, 122], as T32 says.
- Pins re-checked: n5.py states = n5b states, regions = Oink zlk @ 8fbf0a7, verify.py OK for ladderd0_k12_n48 (sha1 c654bf9e…),
  pl130_n40 (895f1128…) and l121reader_n41 (084da8cd…).

## (a) NM per (vertex, phase): DATA
| corpus | instances | max PCH | max NM | max NM/n | max carries at a fixed top | max NM at a gate |
| --- | --- | --- | --- | --- | --- | --- |
| alt_all (si/root/logs/alt_all.lst), S3 | 413 | 60 | 31 (rise_thin51_n40) | 0.775 (rise_thin51_n40) | 29 | 31 |
| alt_all, pinned starts | 413 | 67 (nep92_n40) | 62 (gate_K64_n581, 0.11n) | 0.90 (ret22_n40: 36 of 48) | 37 (best_qpc_nep90_n40_s62, n 80) | 62 |
| lib41 (new/box41/lib41.txt, n ≤ 48: 349 games), S3 | 349 | 37 | 18 (b6_xw_n48) | 0.469 (b6_xw_n32) | 16 | 14 |
| climb corpora (si/grun/out, si/lwp/out, si/lay|lwp|grun/instances; .start where present) | 90 | 23 | 6 | 0.20 | 5 | 6 |
| pl130_n40 (own start) | 1 | 62 (vertex 1) | 47 (vertex 1) | **1.175** | 42 | 47 |
| l121reader_n41 (own start) | 1 | 71 (vertex 40) | 42 (vertex 40) | 1.02 | 36 | 42 |
- The splits the Lead asked for:
  - l121reader_n41, vertex 40, phase [1, 122]: of 71 P-changes, 29 are MATCHED and 42 are carries. Of the 65 fixed-top changes, 29 are
    MATCHED and 36 are carries.
  - pl130_n40, phase [1, 131], summed over the gates: of 157 P-changes, 41 are MATCHED and 116 are carries. Of R104's 133 RESETs, 39 are
    MATCHED and 94 are carries. All 8 RESET_STALLs are carries. Vertex 1 alone: 62 P-changes, 47 carries, 55 resets (41 carries).
- READING: carries are not rare. They are about 60-75 % of the P-changes on the long-phase pins. The largest NM per (vertex, phase)
  is 1.18n (pl130_n40), so an "NM ≤ c·n" CONJECTURE would need c ≥ 1.18 on present data. E4's bound then gives SEG = poly(n)
  (≈ n³·NM) only if NM is O(n). NM = O(n) is OPEN. Nothing here bounds it.

## (b) Invariants: DEAD / DATA / PROVED
| statement | verdict | killing instance (first found) and failure |
| --- | --- | --- |
| LIP (all three readings: w = jW, w = jH, either) | DEAD | ladderd0_k12_n48 (own start; T32's test case), segment [0, 13]. Vertex 14 ∈ E_b switches 15 → 35 → 36 → … → 46: 12 switches, the first 2 already by t = 2. jW(14) = 1 switches once (at 11 → 12), and jH(14) = ⊥ (its honest b-play enters the cycle (13, 17) ⊆ T at once). So SW(14) = 2 > SW(w) + 1 already at t = 2, and 12 > 2 at b. Also seglast_kill_n29 (LIP-H only), and 48-69 library instances per corpus |
| HAM-MONO strict | DEAD | every corpus. First in alt_all S3: gci3_n24, phase [3, 15], vertex 8, P-change at 14: \|P Δ P_i\| goes 6 → 5 |
| HAM-MONO weak (non-decreasing) | DEAD | same instance and change. 157 alt_all S3 instances fail |
| HAM-MONO weak on even ranks only | DEAD | gci3_n24 (same change: even part 2 → 1). 145 alt_all S3 instances fail |
| HAM-MONO weak on odd ranks only | DEAD | lend107_n32 S3, phase [2, 25], vertex 0, change at 6: odd part 5 → 4. Also the l121reader / long121 / pl130 pins |
| NEST-FACE (ii): k_t := top of P_{t+1} Δ P_i never decreases | DATA: 0 failures on all corpora and pins (125,954 P-changes in the inv logs). PROVED (L-COMP, elementary, unrefereed), see below |
| NEST-FACE (i) ("Ξ-best among the path sets realizable at t+1 that agree with P_i above k") | NOT RUN | T32 does not define "realizable at t+1" (by which strategies, in which arena). Needs a READING from L-LIT or the Lead |

NEST-FACE (ii) is a consequence of monotonicity. PROVED (L-COMP, elementary, unrefereed). Assume, as R84 states for a phase, that
every P-change t → t+1 of P(Ξ v) in a phase is a strict improvement in S1's path-set order. That order compares two sets at the top
rank of their symmetric difference: the set holding it wins iff that rank is even. Suppose k_{t'} < k_t at the next P-change
t' → t'+1. Then P_{t+1} and P_{t'+1} both agree with P_i above k_t, and they differ at k_t: P_{t+1} differs from P_i there and P_{t'+1}
does not. So k_t is the top of P_{t+1} Δ P_{t'+1}, and P_{t'+1} holds P_i's choice there. P_{t+1} beats P_i at k_t, so P_{t+1} beats
P_{t'+1}. This contradicts the chain P_{t+1} = P_{t'} < P_{t'+1} (P is constant between consecutive P-changes). □
So (ii) holds whenever the P-sequence is monotone. It says only that the sequence is lexicographically increasing (a binary counter
also satisfies it). It bounds nothing by itself. The bound in T32's Lemma 5 analogue needs (i).

## DONE / FINDINGS / NEEDS
- DONE: tools nm.py, matchtest.py, inv.py, agg.py; logs results/*.log (instance lists results/lib41_n48.lst, results/climb.lst).
- FINDINGS: (1) matching rule = L-LIT brute force (K 6, all parity patterns, 0 disagreements). (2) NM ≤ 1.18n on every instance run
  (max pl130_n40, 47 at n 40); carries are 60-75 % of the P-changes on the long pins; all 8 of R104's RESET_STALLs on pl130_n40 are
  carries. (3) LIP is DEAD (ladderd0_k12_n48 [0, 13], vertex 14). (4) HAM-MONO is DEAD in every form tested (strict, weak, even-only,
  odd-only). (5) NEST-FACE (ii) holds everywhere and is a theorem given R84's monotonicity, so it carries no information. NEST-FACE (i)
  is untestable until "realizable" is defined.
- NEEDS: Lead / L-LIT: a definition of "realizable at t+1" for NEST-FACE (i), if it is wanted.
