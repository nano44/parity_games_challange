# R90: P-N5-EPC's open terms on the long instances, and a LINEAR family for R⁰_{≥2} at fixed k with NCONF_{≥2} constant and f = 0 (mkpp, mkgate); exact by SAT_C (2) (L-RED successor 21, box 57; Lead 14:47Z; written 14:53Z, date -u)
Target: L-NEW 27's Corollary EP-ASM (docs/new/P-N5-EPC-box48.md, l-new, sha1 9f48ded7, frozen):
N_ep ≤ (4n² − 3n) + N_1-term + NCONF_{≥2}·(2n² − n) + R⁰_{≥2}. Labels per L40: DATA, READING; one elementary PROVED remark (§1). Not a
TARGET.md claim. G-N5-TIME stays open. No kill (nothing here contradicts EP-ASM; it measures its open terms).

## 0. Result
- **R⁰_{≥2} grows linearly on an explicit family with k fixed, NCONF_{≥2} fixed and no fallback**: on mkpp (R83) and mkgate (R84),
  every return is a fallback-free return to a multi-gate configuration, and each one is in R⁰ exactly (§1):

| instance (experiments/red/usplit/instances/) | sha1 (.pg) | n | |Q| | phase T | f | N_ep | NCONF | NCONF_{≥2} | R⁰_{≥2} (exact) | REV |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pp_K12_n161 | 8808ba5dcf51… | 161 | 6 | 19 | 0 | 15 | 5 | 4 | 10 | 10 |
| pp_K48_n449 | a161569d654c… | 449 | 6 | 55 | 0 | 51 | 5 | 4 | 46 | 46 |
| gate_K16_n197 | 3eeddc86ae0b… | 197 | 5 | 23 | 0 | 17 | 4 | 2 | 13 | 13 |
| gate_K64_n581 | a93c7c8be2c3… | 581 | 5 | 71 | 0 | 65 | 4 | 2 | 61 | 61 |
  R⁰_{≥2} = K − 2 on mkpp and K − 3 on mkgate (n = 8K + 65 and 8K + 69): linear, while NCONF_{≥2} stays 4 / 2. So on 𝒞^kO the term
  NCONF_{≥2}·(2n² − n) is not the only multi-gate cost: R⁰_{≥2} alone reaches Θ(n), and any bound for it must allow that.
- Cross-check: L-NEW's experiments/new/box48/nconf.py (run read-only from a detached worktree of origin/claude/l-new, removed afterwards)
  gives EPQ 51 / 65, NCONF 5 / 4, REV 46 / 61, RET_NOFB 46 / 61, f 0 on pp_K48 / gate_K64: equal to mine.
- On the long instances of R88 / R89 the multi-gate returns are few: R⁰_{≥2} = 3 (long121), 2 (long90_k2), 1 (core41, comp54), 0 (run34,
  run49). long121: N_ep 37, NCONF 14, NCONF_{≥2} 12, N_ep^{≥2} 35 (L-NEW §6 reports 37 / 14 / 12 / 35 / R⁰ 3: equal).
- Climbs (phclimb.py FIT=E, fitness = fallback-free returns to |D_C| ≥ 2 configurations in a phase) after ~4 min: 16 at n 40 (from long121,
  phase of 50 epochs), 12 at n 80 (comp54), 8 at n 24 (ffin4); still running; final numbers in an addendum.

## 1. Exactness of the count (PROVED, elementary, from P-N5-EPC's own Lemma SAT_C (2))
R⁰_C counts the returns (i, i + 1) of C with no in-phase fallback source in [s_i, s_{i+1}) AND LEV_C(s_i) ≤ n − 2. epc.py counts the
fallback-free returns (an upper bound) and, as R0_2_certain, those with Ξ_{s_i} ≠ Ξ_{s_{i+1}}. The latter are in R⁰: if LEV_C(s_i) = n − 1,
SAT_C (2) (s_i < s_{i+1} both C-states of P) makes Ξ constant on s_i, …, s_{i+1}. On all eight instances above every fallback-free
multi-gate return has Ξ_{s_i} ≠ Ξ_{s_{i+1}}, so the counts are exact.

## 2. Mechanism and READING
- mkpp: two leapfrogging risers; Odd's best reply at the relay pair q1, q2 flips direction at every rise (R83), so σ̄|Q alternates between
  two configurations with |D| ≥ 2, K times in one fallback-free phase. mkgate: the gate u enters and leaves D at every leapfrog (R84): in
  ROOT-PIECE's terms, the D-leave / D-re-enter cycle, K times.
- Each return there costs one fresh content level C_j (R82 / R83 RULER: a level is reused only after a higher rise). So R⁰_{≥2} = Θ(n)
  is the same linear barrier as ρ_q in R83; it does not get past "fresh content per event".
- R⁰_{≥2} ≤ N_ep ≤ T + 1 per phase, so a super-polynomial R⁰_{≥2} is again a super-polynomial phase; with f = 0 it is a single
  fallback-free run (R89's target). So the three open lines (fallback-free runs, R⁰_{≥2}, the D-leave cycle G_c) are one problem here:
  a fallback-free run in which the multi-gate configuration returns super-polynomially often.
- On the long121 family the opposite holds: many configurations (NCONF_{≥2} = 12), few fallback-free returns (3), length from fallbacks.
  The two known mechanisms are complementary: mkpp/mkgate (fresh content, no fallbacks, few configurations, many returns) and long121
  (fallback ping-pong, many configurations, few returns). A super-polynomial phase on 𝒞^kO would need returns without fresh content.

## 3. Tools
experiments/red/n3/epc.py (N_ep, NCONF, NCONF_{≥2}, fallback-free returns, exact R⁰_{≥2} lower count via SAT_C (2), REV); phclimb.py FIT=E.
