# Box 70 N5-FRAME: the SAT frame ABS-m + IM is a relaxation of the IDEAL ladders; at m = 3 it gives T_0(3) ≤ 8, T_1(3) = 10 exactly, and SUM_1(3) = 17 = 2T^R(3) + 1 (tight)
L-SI successor 39, 2026-11-05 (date -u: see the commit). Lead brief BOX 70 (17:47Z): ABS-3 + IM as an exact search frame (keys by
BIT-CHAIN, C_z arbitrary subject to LOCAL + IM over acyclic ISO Ξ-graphs):
- (1) max T_0 at m = 3;
- (2) max T_1 and max T_0 + T_1, stating whether the frame is a relaxation;
- (3) SAT if enumeration is too big; runs resumable.

Labels:
- PROVED (lane): proved here or in boxes 64-69, not refereed.
- EXACT-SAT: CaDiCaL 1.5.3 via python-sat; no proof certificate is checked; logs in experiments/si/box70/log/.
- DATA, CONJECTURE, READING.

Not a TARGET.md claim. No polynomial bound. FLIP-ADD and G-N5-TIME stay OPEN.

## 0. Answer
- **The frame is a relaxation (PROVED, lane).** Map each ISO R197 ladder of the external-flip model E_m to the frame as follows.
  - Its Ξ-graph on the 2m upper movers: acyclic by R104's IDEAL-ACYC hypothesis; ISO, so no Ξ-target at level 0.
  - Its improvement table C_z(s), the strictly better option, with no ties: distinct β ranks make the two option sets differ.
  - Its key bits c_l(k) = [g(A_l, k) < g(B_l, k)].
  - The table is LOCAL (RESULTS R105 LOCAL) and IM (box 69 Lemma IM, from R105 ENC). It does not depend on s_z itself, since z is not
    on its own chains by acyclicity.
  - The step rule is the BIT-CHAIN form of R104's (box 64, checked on every state).
  - So every E_m run of the genome is a frame run of the same length. An UNSAT answer in the frame is an upper bound for every
    ENC genome.
  - SAT models are frame systems, not necessarily genomes. Lower bounds come from real witnesses.
- **Validation at m = 2:** the frame reproduces the exact enumeration values.
  - T_0 = 4 (≥ 5 UNSAT); T_1 = 5 (≥ 6 UNSAT); T_0 + T_1 = 9 ((4, 5) SAT, (4, 6) UNSAT).
  - Without IM, T_1 = 7 (≥ 8 UNSAT), which is box 69's ABS-2 value.
  - check70.sh re-runs these 8 queries (~10 s).
- **m = 3 results** (EXACT-SAT, per log):
  | query | answer | time |
  | --- | --- | --- |
  | T_0 ≥ 8 | SAT | 52 s |
  | T_0 ≥ 9 | UNSAT | 693 s |
  | T_1 ≥ 10 | SAT | 770 s |
  | T_1 ≥ 11 | UNSAT | 1,282 s |
  | T_1 ≥ 12 | UNSAT | 1,284 s |
  | T_0 ≥ 8 and T_1 ≥ 9 (same system) | SAT | 262 s |
  | T_0 ≥ 8 and T_1 ≥ 10 | UNSAT | 724 s |
  | T_0 ≥ 7 and T_1 ≥ 11 | UNSAT | 1,251 s |
- **Consequences for the real model** (upper bounds from the frame, lower bounds from real ENC witnesses replayed with two simulators
  in boxes 64-68):
  - (1) **T_0(3) ≤ 8.** IM + LOCAL + BIT-CHAIN + triangularity already force the flip-free bound at m = 3.
    - With L-NEW's NOL0 d = 4 witness (exact 8, box 160): T_0(3) = 8. This is a third, structural route to it.
    - It is the E-model quantity T_0(3): the ISO class with level 0 frozen, i.e. L-NEW's NOL0 at d = 4. It is NOT T^R(3) of the
      3-level ladder; there level 0 moves and need not be ISO.
    - The relation is T_0(n) ≤ T^R(n + 1) (box 68), plus equality T_0 = T^R at n ≤ 3 by data.
    - So this is not a route to the «T^R(3) ≤ 8» premise unless that premise is the NOL0 / E-model one. Lead to check.
  - (2) **T_1(3) = 10 EXACTLY.** The frame gives ≤ 10 (T_1 ≥ 11 UNSAT); L-NEW's kf1_d4_t10 gives 10.
    - New: before this only T_1(3) ≥ 10 was known, with L-NEW's «≥ 11» run unresolved.
    - Hence the one-flip excess T_1(m) − T^R(m) = 1, 1, 2 for m = 1, 2, 3, all EXACT.
  - (3) **SUM_1 at m = 3 holds and is TIGHT.** max_G (T_0(G) + T_1(G)) = 17 = 2T^R(3) + 1.
    - Upper bound: (8, 10) and (7, 11) are UNSAT, and T_0 ≤ 8, T_1 ≤ 10 cover every split of 18.
    - Lower bound: box 66 pin f_m3_p4_s1 (T_0 8, T_1 9, replayed with L-NEW Gen).
    - SUM_1 is now EXACT at m = 1, 2, 3 (5, 9, 17).
- **READING.**
  - IM (box 69) is a sufficient mechanism at m = 3 as well. The frame without the realisability of rank sums, but with
    additivity-induced monotonicity, already gives the exact one-flip maximum.
  - So the right object for a proof of SUM_1 / FLIP-ADD at larger m is «triangular LOCAL + IM tables with BIT-CHAIN keys», a purely
    combinatorial class.
  - CONJECTURE SUM_1(m) (lane; EXACT for m ≤ 3): T_0(G) + T_1(G) ≤ 2T^R(m) + 1.
  - CONJECTURE (FLIP-ADD at k = 1, data): T_1(m) − T^R(m) = 1, 1, 2, ≥ 1 for m = 1..4; not refuted.

## 1. The frame (experiments/si/box70/frame.py)
- Variables:
  - x(o, t): option o = 2z + k of upper mover z has Ξ-target t, a mover ≠ z or X; exactly one per option.
  - R: a transitive irreflexive reach relation containing every Ξ-edge, which makes the graph acyclic.
  - on(z, k, s, y): y lies on the chain of (z, k) under s. Defined exactly: on ↔ x(2z + k, y) ∨ ⋁_w (on(z, k, s, w) ∧ x(2w + s_w, y)),
    which has a unique solution on a DAG.
  - C(z, s): z's better option at s. Constraints:
    - independent of s_z;
    - LOCAL: no change when a mover off both chains is toggled;
    - IM: the three clauses of box 69 Lemma IM, for every unhappy chain mover y.
  - c(l, k): key bits, levels 1..m−1.
  - Runs S[t][z] with external bit B and a monotone flip sequence F (at most one flip). The step is computed level by level by
    BIT-CHAIN; every step must move a mover.
- Modes:
  - t0 (a T-step flip-free run);
  - t1 (a T-step run with ≤ 1 flip);
  - sum (both runs on the same system).
  - NOIM=1 drops IM (control).
- run.sh: resumable driver; a finished log is skipped; logs are written as *.part (gitignored) until the solver ends.

## 2. Files
- experiments/si/box70/{frame.py, run.sh, check70.sh}.
- log/3_*.log: the eight m = 3 answers above, with their models where SAT.
- Environment: python-sat and scipy pip-installed in this container (notes/L-SI.md); check70.sh skips without python-sat.
