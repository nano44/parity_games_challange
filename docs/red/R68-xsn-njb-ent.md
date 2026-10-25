# R68: X_SN growth, J-SEG, REL, NJB and ENT (L-RED successor 15, box 38; GO 2026-10-25 05:18Z, date -u)
Targets (Lead 05:18Z, 05:28Z, 06:39Z, 07:10Z):
- (1) X growth in the SN regime (c_w = c_θ) with fallbacks.
- (2) J-SEG: J ≤ (d_o − 1)(f + 1) per phase (my CONJECTURE, R67).
- (3) REL growth per phase.
- (4) L-SI succ. 4's CONJECTURE NJB (docs/si/N5-C-box9.md §3).
- (5) L-SI's Lemma NO-RF-OLD and CONJECTURE ENT (same file §8, with the ENT-SHAPE steer of §12).
𝒞^1O only: one Odd vertex with out-degree > 1, asserted in every checker. Referees were not contacted. Labels per L40. G-N5-TIME stays
OPEN.

## 0. Result
NO KILL. 0 failures of NJB, FLAT-ALL (iii), NO-RF-OLD, ENT and J-SEG, and of every R30 lemma re-checked by sox2.
- X_SN grows linearly in n per fallback-free run: at most 0.83n in the climbs. Over a phase it adds up across runs: 91 at n 48 with f 9.
- **The NJB / ENT mechanism never starts.** On 257 files and all climbs, there is NO rise of COARSE_L(θ) between an in-scope fallback
  and the next in-scope fallback of the same scope run. Every rise comes after the last fallback of its scope run (as in L-SI's data).

## 1. Tools (experiments/red/so/; each written from the source text)
- sox2.py, extended:
  - REL: exit releases per phase at non-fallback transitions (P-N5-SN §6).
  - RELe: releases of exits that entered R at an ε-transition.
  - Level-M blocks of consecutive in-scope fallbacks, M ≥ 0 (L-SI §3).
  - NJB: no COARSE_M change at a non-fallback transition strictly inside a block.
  - FLATALL: no COARSE_M change at f_1 … f_{N−1}.
  - Per block: releases at block fallbacks, and re-entries of those exits inside the block.
  - maxpre: crossings inside the c_w = c_θ prefix of one fallback-free run.
- sox3.py (new): NO-RF-OLD and ENT exactly as in §8, for every scope run, every fallback k0 (L = M_{k0}), and the next fallback k.
  - t* = the last state ≤ k with r > L on [k0+1, t*].
  - A rise is an S4a step j ∈ (k0, t*) with a COARSE_L(θ) change.
  - NORF: no gate y ∈ R_j ∩ R_t → z ∈ F_t at any t ∈ [j+1, t*].
  - ENT: if t* = k and M_k ≥ 0, no gate at k from y ∈ R_k ∖ R_j into F_k.
  - Also: rfb0 (rises before a next fallback, any r), rfb, and gap = t* − k.
  - On L-SI's seeds cl9_norf_a / _b (sha1 33580f22 / a90ad304, read from claude/l-si), sox3 reproduces L-SI's numbers: 3 rises;
    windows of 21, 15 and 23 states with r > L, i.e. 44 distinct states; 0 fallbacks after a rise.
- soclimb2.py modes xsnf, jbf, rel, njb, xrun; soclimb3.py (ENT).
  - ENT fitness: failures, then windows reaching a fallback, then a rise before any next fallback, then gap, then window length.
  - The rise-before-fallback key came after the first two climbs had stalled on window length alone.

## 2. X_SN growth (DATA)
| instance | sha1 | n | f | X | X_SN | max X_SN in one fallback-free run |
| --- | --- | --- | --- | --- | --- | --- |
| xsnf42_n48.pg | f1216810e369a6dcd92f6a70ccfb68de2d41d79c | 48 | 1 | 42 | 42 | 42 |
| xsnf52_n64.pg | 090ddfd10069e15cc6afcf6b2445b8f1ea2d901c | 64 | 1 | 52 | 52 | 52 |
| xsn91_n48.pg | 276fab41f7ddfed37cdc0a37f31b69baae044386 | 48 | 9 | 100 | 91 | 23 |
| xsn43_n48.pg (R67) | b9d41e3cb78c33ebdaa538fc2310978118cd8480 | 48 | 0 | 43 | 43 | 43 |
- Climbs with f ≥ 1 (xsnf): X_SN = 13 / 27 / 42 / 52 at n = 16 / 32 / 48 / 64, about 0.8n, linear. All stop at f = 1.
- The climb seeded from b6_xl_n48 (f 9) raised X_SN from 75 to 91 at n 48. Per-run X_SN there: 19, 23, 10, 9, 2, 7, 1, 7, 0, 14.
- CONJECTURE (L-RED, data): (XSN-RUN) at most n − 1 crossings inside the c_w = c_θ prefix of one fallback-free run. With SN-PREFIX
  (≤ n − 1 after the prefix) this would give X ≤ 2(n − 1)(f + 1) + f per phase: X is linear in f + 1, and the open core of X is f.
  - xrun climbs on per-run prefix crossings − (n − 1), at n 12 and n 20: §6.

## 3. J-SEG (DATA)
- No library phase with f ≥ 1 and J ≥ 1 comes within less than 1 of the bound. The closest are fbv32_inr2 and two box25 files (d_o 2,
  J 1, f 1).
- jbf climbs from fbv32_inr2 and j10_n24 (45 min each) stayed at J − (d_o − 1)(f + 1) = −1.
- With R67 (f = 0, three cases at equality), J-SEG has 0 violations. It is still a data conjecture.

## 4. REL (DATA)
- REL per phase reaches 12 on so_th_n32 and 44 in a climb at n 32 (rel32, about 9 iterations).
- Those releases are exits moving in and out of R with no ε-transition at all. Releases of exits that had been absorbed at an
  ε-transition (RELe) are 0 in the library and 1 on my R67 counterexamples.
- So raw REL is large but cheap: ABS-COUNT charges ε to releases only through RELe-type events, which stay rare.

## 5. NJB (DATA)
- Library (241 files): 0 NJB and 0 FLATALL failures. Max block 25 fallbacks (ccl_w48_n48); max releases at block fallbacks 12;
  re-entries of released exits inside a block 3 (zcl_fb2_n32).
- njb climbs (re-entries of block-released exits inside a block, about 50 min each):

| instance | sha1 | n | it / fb | block fallbacks | releases at block fallbacks | re-entries inside the block | NJB |
| --- | --- | --- | --- | --- | --- | --- | --- |
| njb_reabs54_n32.pg | c3cfcbf1004d4fb0e3f6f67dd8f3936adacd77ed | 32 | 40 / 22 | 21 | 77 | 54 | 0 failures |
| njb_reabs65_n48.pg | 3388d0be141a4c3ad1cca779861288d8e0dbbe09 | 48 | 70 / 29 | 26 | 95 | 65 | 0 failures |

- Released exits do come back into R inside blocks, many times. They come back through Even switches with no COARSE_M change and no
  ε-transition (ε = 0 on njb_reabs65). This is the case NJB allows; an absorption ABOVE M never appeared.

## 6. NO-RF-OLD and ENT (DATA)
- Library and all my instances (257 files): 6 rises with an r > L window, 8 post-rise states, 0 failures.
  - rfb0 = 0: no file has a COARSE_L(θ) rise between an in-scope fallback and the next in-scope fallback of its scope run.
- ENT climbs: 0 failures; rfb0 stayed 0 throughout.
  - From cl9_norf_a and cl9_norf_b: the window stayed at 21-24 states, ending at the end of the scope run.
  - From njb_reabs54_n32 and njb_reabs65_n48 (many fallbacks).
  - From so_k2_n32.
  - So step (ii) → (v) of the Lead's ENT-SHAPE target (a rise followed by any later fallback in the same scope run) was never reached.
- CONJECTURE (L-RED, data): (RISE-LAST) inside a scope run, no COARSE_L(θ) rise (L = the level of an in-scope fallback k0) happens
  before the next in-scope fallback after k0. RISE-LAST makes NJB's dirty intervals and ENT's setting empty, so it implies both.

## 7. Labels
- DATA, 0 failures:
  - NJB, ENT (L-SI CONJECTURES);
  - NO-RF-OLD, FLAT-ALL (iii) (L-SI, PROVED in lane);
  - J-SEG (L-RED CONJECTURE);
  - R30's lemmas.
- CONJECTURE (L-RED): XSN-RUN; RISE-LAST.
- OPEN: X per phase (reduced by XSN-RUN + SN-PREFIX to f, if XSN-RUN holds), K, G-N5-TIME.
