# R200-R204 Exact CNF engine for IDEAL-ACYC ladders (xcnf); d 5 maximum run ≥ 15 (pinned); NEST(3) at d 6 still UNKNOWN; level-1 slot filling exact at d 4 (C_1 = 8) (L-RED successor 49)
Started 2026-11-04 00:18Z (Lead brief BOX R200, date -u); later targets R202 (07:00Z), R203 (11:49Z), R204 (12:46Z) and R201 (queued)
came from the Lead. Labels: EXACT (CaDiCaL / z3 / brute force, machine-checked, not Lean), DATA, UNKNOWN. Model: IDEAL-ACYC (RESULTS
R104), degree 2, 2-wide W-ladder in the R197 convention (option k of a level-l ≥ 1 mover W-points to mover 2(l − 1) + k; level 0 keyed by
gates). This is not a TARGET.md claim. G-N5-TIME stays OPEN. No family.

## 0. Answers
- R200 (NEST(3), k 3, two ladder levels above, d 6): UNKNOWN.
  - Gate choices covered: all three W-feasible full-F choices (r199/allgates.py: k3/ag_0 with L 24; k3p2/ag_0 and k3p2/ag_4 with L 16).
  - Monolithic CaDiCaL runs: no answer in 92 min each before a container restart killed them.
  - EXACT partial results:
    - For k3p2/ag_0, the first 10 steps are realisable (SAT 262 s) and the first 14 steps are realisable (SAT 623 s; replays under
      r187/ideal.py match). Any obstruction therefore lives in steps 15-16.
    - The 15-step prefix is UNKNOWN (7200 s).
  - Prefix CEGAR (pcegar.py: exact; P = the 10-step prefix model, no-goods = deletion-minimised UNSAT cores of the full model):
    - k3/ag_0: 46 no-goods, cores of 3-7 literals out of 52.
    - k3p2/ag_0: 44 no-goods.
    - k3p2/ag_4: 2 no-goods.
    - None has converged.
  - Successor 48's d 6 hunt proposals are now exactly refutable: 5 of them were refuted in 0-389 s each (propck.py).
- R202 (exact maximum run T*(d) on the 2-wide degree-2 ladder):
  - Reproduced: T*(2) = 4 (T ≥ 5 UNSAT 0.1 s) and T*(3) = 8 (T ≥ 9 UNSAT 13.5 s), each with a SAT witness at the maximum.
  - NEW: T*(5) ≥ 15. T ≥ 15 is SAT (2092 s). Witness r202/max_d5_L15: L 15 opt, F [2, 2, 3, 3, 3], level-0 steps t7 / t8, split (seg1, mid, tail) [6, 0, 7] (replayed).
    - Pinned as max_d5_L15_n96 (sha1 .pg 5a4c6dba…, .start 9e8bb59b…): PIN OK (startck, Oink 8fbf0a7 --zlk + verify, --tl + verify,
      xeng); lemck 0 violations; check.sh block «R202».
  - T ≥ 16 and T ≥ 17: UNKNOWN (CaDiCaL 6 h each). T ≥ 16 with Kissat is running.
  - T ≥ 16 with the L 15 witness's Ξ-graph fixed: UNSAT 18 s. This is inexact (a hint only).
  - Maxima so far: 4, 8, 13, ≥ 15. Neither of L-NEW's fits (linear 5d − 7 → 18, quadratic → 19) is decided.
- R203 (slot filling, C_l = number of steps moving some mover of level ≤ l), d 4, horizon 13 = T*(4) (R197), hence EXACT:
  - With C_0 = 2: C_1 ≥ 4 / 6 / 7 / 8 all SAT (19 / 20 / 61 / 134 s). So max C_1 = 8, the LEVEL-PRODUCT ceiling (2 + 1)(2 + 1) − 1.
    Witness r203/d4_C1_8: L 10, C [2, 8, 10, 10].
  - With C_1 = 8: C_2 ≥ 11 SAT (4690 s). Witness r203/d4_C1_8_C2_11: L 11, C [2, 8, 11, 11], lemck 0. C_2 ≥ 12 is running.
  - The extremal runs do NOT fill level 1. C_l replayed: max_d4_L13 [2, 7, 9, 13]; dd_d5_F14 [2, 4, 9, 14, 14];
    max_d5_L15 [2, 3, 8, 13, 15].
- R204 (segment sums: seg1 / mid / tail = nonempty steps before / between / after the level-0 steps), d 4, horizon 13, C_0 = 2:
  - seg1 + tail ≥ 10: SAT, split [5, 0, 5].
  - seg1 ≥ 8: SAT, split [8, 0, 0]. This agrees with LIFT (max seg1 = T*(3) = 8).
  - seg1 ≥ 5 ∧ tail ≥ 5: SAT.
  - seg1 + tail ≥ 12 and min ≥ 6: UNSAT. Both are trivial: T = seg1 + mid + tail + 2 ≤ 13.
  - seg1 + tail ≥ 11: running.
  - d 5, seg1 + tail ≥ 14 at horizon 20: running. A SAT would beat T*(4) = 13 inside two segments. An UNSAT would cover only runs of
    ≤ 20 steps.
- R201 (queued; groundwork only, DATA): a W-side hill climb over L-NEW's fixed Ξ-ladders (box 153, LP 22 / 52 / 114) with a free start
  reaches L 4 / 7 / 9 for K 3 / 4 / 5, below 2n = 12 / 16 / 20. From ladlp's own start, which is the antipode of the sink, every W side
  tried gives L 1. Nothing exact.

## 1. The engine (experiments/red/r200/xcnf.py)
- What it encodes. The r199/xbmc.py model, constraint for constraint, compiled by hand to CNF (Tseitin with constant folding) and solved
  with CaDiCaL 1.9.5 (pysat; Kissat 4.0.4 optional):
  - one-hot Ξ-targets, ordered by an acyclic tournament;
  - a strict total order on the faces, and parities;
  - chain membership IN[t, u, f];
  - comparison bits c[t, x] with the exact «top face of the symmetric difference» rule, in both directions;
  - the C-ELEMENT requirements (R199 §1) for prescribed movers, and the C-element rule for free movers, with keys from the R198 K3
    recursion;
  - the LEM clauses (reach, R189 RE-REVERSAL, Corollary LAG).
- Options:
  - PMD: Corollary PMDIFF, immediate from R104 (the symmetric difference consists of x's two faces and the current faces of the movers
    on exactly one chain).
  - CUBEVARS: resumable cubes.
  - HINT / XTHINT: SAT-finding only.
  - CMIN, SEG: cardinalities.
  - TMIN: «step t nonempty».
  - SYMB (all-free ladders): σ_l swaps the two level-l movers and relabels the options of level l + 1. The σ_l are exact symmetries,
    they commute, and σ_l touches only levels l and l + 1. Fixing levels bottom-up therefore gives the valid break s_0(u_l) ≥ s_0(v_l).
- SAT models are decoded to genomes and replayed under r187/ideal.py, the reference simulator. Every SAT claim above is a replayed
  witness.
- Validation (logs in r200/logs/):
  - Known answers: k 2 d 4 UNSAT 3.2 s; k 2 d 5 SAT 78 s (replay L 12, main prefix matches); k 3 d 5 UNSAT 13.2 s (L 24) and 17.2 s
    (L 16). z3 took 4.9 / 4194 / 246 / 69 s.
  - bf.py, independent of both encodings (all acyclic Ξ-targets, N 4, then GREEDY): 85/85 agree, including 8 UNSAT, with LEM on and off.
  - agree.py vs r199/xisat.py: 88/90. The two non-agreements are xisat UNKNOWN (z3 600-900 s) against xcnf UNSAT, which also holds
    without LEM.
  - Two decode bugs were found and fixed before any result was stated:
    - negative literals were read as false;
    - level-0 gates were not decoded.
  - Inputs with an empty step are invalid prescribed runs (every IDEAL run ends there). agree.py filters them.

## 2. Files
- experiments/red/r200/:
  - xcnf.py; xmax.py (R202-R204 driver);
  - pcegar.py, propck.py, runcubes.sh;
  - agree.py, bf.py;
  - logs/ (validation logs and the k 2 d 5 genome).
  - out/ is gitignored (run logs; relaunch lines are in notes/L-RED.md).
- experiments/red/r202/: max_d5_L15.json, instances/ (pin and pins.sha1).
- experiments/red/r203/: d4_C1_7, d4_C1_8, d4_C1_8_C2_11 (+ logs).
- experiments/red/r201/: wclimb.py, inputs/ (ladlp_3/4/5; 3 and 4 regenerated with L-NEW's ladlp.py, seed 1: LP 22 / 52).

## 3. OPEN
- R200: k 3 d 6 (steps 15-16 of the L 16 target; pcegar continues).
- R202: T*(5) ∈ [15, 3·13 + 2]. Upper end from LEVEL-PRODUCT / SEG-CAP (L-NEW box 158; not opened by me).
- R203: max C_2 given C_1 = 8 at d 4.
- R204 at d 5.
