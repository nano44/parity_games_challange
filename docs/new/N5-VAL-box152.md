# Box 152 N5-VAL (IN PROGRESS): value-semantics clauses against NEST(3) with 2 levels above (d 6); Lemma PREMERGE / PMDIFF and Lemma STABLE-PATH (PROVED, lane; 0 violations on simulated runs); k = 3, E = 2 still open
L-NEW successor 50, 2026-11-03 (date -u: see the commit). Lead brief BOX 152: can MONO / EXACT-ENERGY / KEYFLIP plus the wake-order
clauses forbid NEST(3) with E = 2 levels above (d 6)? Labels: PROVED (lane), EXACT (z3 on a sound relaxation), DATA, OPEN. Model:
P-IDEAL-RED §0, degree 2, 2-wide ladder. Not a TARGET.md claim. This file is a WORKING checkpoint; the box report follows.

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
- + PMDIFF + STABLE-PATH: k 2 E 2 SAT (sanity), k 3 E 1 UNSAT; k 3 E 2 running at this checkpoint.
- CEGAR (value nogoods on top of PMDIFF): ~350 s per iteration at k 3, E 2; stopped, not conclusive.
