# Box 152 N5-VAL (CLOSED): value-semantics clauses against NEST(3) with 2 levels above (d 6); Lemma PREMERGE / PMDIFF and Lemma STABLE-PATH (PROVED, lane; 0 violations on simulated runs); k = 3, E = 2 UNKNOWN (5400 s); E_min table under value semantics
L-NEW successor 50, 2026-11-03 (date -u: see the commit). Lead brief BOX 152: can MONO / EXACT-ENERGY / KEYFLIP plus the wake-order
clauses forbid NEST(3) with E = 2 levels above (d 6)? Labels: PROVED (lane), EXACT (z3 on a sound relaxation), DATA, OPEN. Model:
P-IDEAL-RED §0, degree 2, 2-wide ladder. Not a TARGET.md claim. CLOSED by the Lead 00:09Z (2026-11-04).

## 1. Lemmas (PROVED, lane)
- Notation: for a mover x and a state s, its two face chains under s; their first common mover m (if any); the PRE-MERGE parts are the
  options of each chain before m (whole chains if they never meet). The movers on exactly one chain are exactly the pre-merge movers.
- Lemma PREMERGE. C_s(x) (the strictly better face) is the sign of Σ_(pre-merge part of face 1) ε − Σ_(pre-merge part of face 0) ε.
  Proof: P-IDEAL-RED ENC; both chains continue identically from m, so the common suffix cancels. ∎
- Corollary PMDIFF. For ANY two states a, c: C_a(x) ≠ C_c(x) ⇒ some mover on exactly one of x's face chains at a has a different
  option at c. Proof: otherwise both pre-merge parts are the same option sequences at c, still ending at m (or at X), and PREMERGE
  gives the same sign. ∎ (Wake-order CBIT is the weak case c = a + 1 with «moved, anywhere on the chains».)
- Lemma STABLE-PATH. Let C_a(x) = b, with pre-merge parts P (face b) and Q (face 1 − b) at a, merging at m. If at state c every
  Q-mover keeps its option, and every P-mover keeps its option or is stable at c (its current face is its better one), then
  C_c(x) = b. Proof: Q unchanged gives face_c(x, 1 − b) = ΣQ + cv_c(m) (or ΣQ alone if no merge). Along P, backwards from m, each
  mover y_i either sits on the path option or is stable, so cv_c(y_i) ≥ ε(y_i, k_i) + (path value below), by induction
  face_c(x, b) ≥ ΣP + cv_c(m). ΣP > ΣQ by PREMERGE at a. ∎
- DATA: experiments/new/box152/lemcheck.py: 0 violations of PMDIFF and STABLE-PATH on all ordered state pairs of 50 corpus runs
  (92,308 pairs, incl. the R198 / R199 d 5 pins nd2_d5_F12, dd_d5_F14, c4x_d5_F12, tri_d5_L12) and of 1,936 all-start random runs
  (20,804 pairs); premises apply in 32,586 / 37,303 and 14,872 / 15,855 pairs.

## 2. Runs so far (box151/xwake_anti.py, XT=1 per-option Ξ-targets, ANTI=1, build.py gates)
- Wake-order witnesses for k 3, E 2 are value-INFEASIBLE once their own Ξ-targets are fixed (box152/cegar.py lincheck: strict linear
  inequalities over the option weights, a relaxation of ±2^rank). Cores: mostly 2-cores of PREMERGE type; one worked 3-core is a
  STABLE-PATH instance (mover 6 leaves the shared suffix of mover 7's faces for its better option).
- + PMDIFF: k 2 E 1 UNSAT, k 2 E 2 SAT (sanity: nd2 exists), k 3 E 1 UNSAT, k 3 E 2 SAT (130 s).
- + PMDIFF + STABLE-PATH: k 2 E 2 SAT (sanity, 1.9 s), k 3 E 1 UNSAT (10.2 s), k 3 E 2 UNKNOWN (z3 timeout 5400 s). Prefixes of
  NEST(3) at E 2: first 12 steps SAT (5.4 s); first 16 steps: no answer at the close (running, timeout 3400 s).
- CEGAR (value nogoods on top of PMDIFF): ~350 s per iteration at k 3, E 2; stopped after 1 iteration, not conclusive.
- Seed for L-RED (Lead routing): box152/hints/wo_pmdiff_k3_E2.json = the latest wake-order + PMDIFF witness at k 3, E 2 (states,
  KP, per-option Ξ-targets, reach). With ITS OWN Ξ-targets it is value-infeasible (valcheck FIXXT: REL UNSAT, 3-core
  {(0, 8): 1, (1, 7): 0, (2, 8): 0}); as a schedule (Ξ-targets free) it is not decided (free-target REL check timed out). So it is a
  schedule seed, not a witness. hints/nest_k3.json = the genk target; hints/wo_stabpath_k3prefix12_E2.json = the 12-step prefix
  witness under all clauses.

## 3. E_min under value semantics (least number of ladder levels above NEST(k) for which a run can exist)
| k | E_min | evidence |
| --- | --- | --- |
| 2 | 2 | E 1 UNSAT (wake order + antisymmetry, gate-fixed; L-RED allgates: all gates); E 2 realised exactly (nd2_d5_F12, R199) |
| 3 | ≥ 2 | E 1 UNSAT (all gates, L-RED allgates; also wake order + PMDIFF here); E 2 UNKNOWN under PMDIFF + STABLE-PATH (5400 s) |
| 4 | ≥ 2 | E 1 UNSAT gate-free (box 151); E 2 gate-free SAT in wake order, not run with value clauses |
| 5 | ≥ 3 | E 2 UNSAT gate-free (box 151, wake order) |
- READING (the Lead's framing, 23:03Z): a polynomial bound needs nesting depth k = O(log d), i.e. E_min(k) growing exponentially
  (at least super-linearly) in k. Any linear bound E_min(k) ≥ k / c still allows about 2^(d c/(c+1)) carries. The table (k ≤ 5)
  can only point at a trend; it shows lower bounds 2, 2, 2, 3, consistent with ⌈k/2⌉, and no super-linear growth. Nothing here is a
  polynomial bound; IDEAL-ACYC-POLY and G-N5-TIME stay OPEN.

## 4. Status
- PROVED (lane): PREMERGE, PMDIFF, STABLE-PATH (and SDIFF, the weaker «any reached mover differs» form).
- EXACT (z3, sound relaxations): the UNSAT rows above.
- UNKNOWN: NEST(3) at E 2 (d 6). L-RED 49's exact engine is the next decider; seeds in box152/hints/.
- Tools: box152/lemcheck.py (lemma check on simulated runs), valcheck.py (value check of a witness, REL/EXACT, fixed or free Ξ-targets,
  cores), cegar.py (CEGAR with sound value nogoods; PREMERGE nogoods minimal), classify.py (core types); box151/xwake_anti.py modes
  XT, SDIFF, PMDIFF, STABPATH, VAL, NOGOODS.
