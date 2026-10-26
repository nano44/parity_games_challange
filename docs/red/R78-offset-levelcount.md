# R78: CONJECTURE LEVEL-COUNT (count form) is FALSE (lcount_n23); OFFSET-ONCE's refutation reproduced on an independent engine; mkalt's √n family reproduced (L-SI successor 12's docs/si/N5-RUND-box17.md; L-RED successor 19, box 45f; Lead 06:56Z, 07:20Z, 07:43Z, date -u)
Targets: L-SI's lane note docs/si/N5-RUND-box17.md (l-si d61b3cf0 → ac80b594): CONJECTURE OFFSET-ONCE (§6), CONJECTURE LEVEL-COUNT
(§12), Lemma RULER (§12, PROVED). Labels per L40. Every game. Nothing here bounds N5. CR-D, FRZ-U_H3, TWIN-GAP and RULER are untouched.

## 0. Result
- **KILL: CONJECTURE LEVEL-COUNT, count form ("|OC(v)| ≤ |RL(v)|" inside one stretch_D segment of a run with (h3_D)), is FALSE.**
  - Instance: experiments/red/h3/instances/lcount_n23.pg, sha1 f86125a08f0e3b0caf3d825cb48e6dcdc0ee3b04, n 23, Odd choice vertices 4, 6
    and 14 (𝒞^3O).
  - Start files: lcount_n23.start (n5.py / L-SI format) and lcount_n23.start.json (sha1 c25786c5).
  - Run: `python3 experiments/new/n5.py n5 lcount_n23.pg out.sol --start "<SIGMA0 line>" "<TAU0 line>"` gives 5 iterations and
    0 fallbacks. `check_sol2.py` gives "zielonka(oink zlk) OK strategies verified".
  - Failing step: states 0..3 lie in one phase, are fallback-free, have (h3_D) at every state, and form one stretch_D (D = {4, 6, 14};
    R_D and the three gates' (Ξ, W) values are constant). Vertex v = 1 keeps cycle node 17 throughout.
    | transition | path sets of v (vertex ids; rank = id for 14 → 21, 18 → 18, 10 → 19) | rising score, level | Δ(1) after |
    | --- | --- | --- | --- |
    | 0 → 1 | W: {18} → ∅ (18 odd, prio 37) | s^W, 18 | 0 → 2^18 |
    | 1 → 2 | Ξ: {18} → ∅ | s^Ξ, 18 | → 0 |
    | 2 → 3 | Ξ: ∅ → {14, 18}; W: ∅ → {10, 14} | both, 21 | → 2^19 + 2^18 |
    So OC(1) = 3 and RL(1) = {18, 21}: |OC| = 3 > |RL| = 2.
  - Mechanism. Level 18 is used once by each score: first W drops the odd vertex 18, then Ξ does. RULER constrains one score at a time,
    so it is respected; the count form needs one level per offset change across both scores. This is the "a, a, b" pattern L-SI's §12
    suggested attacking, realised by the two scores reaching the same improvement at different times, rather than by mkalt-style
    alternation of sides.
  - Independent confirmation, three tools:
    - my h3_19.py: LEVELCOUNT and LEVELPAY;
    - L-SI's lvl.py --one (l-si ac80b594): "VIOLATION ('LC', …, 0, 3, 1, 3, [18, 21])", "LVL FAIL";
    - L-SI's gap.py --one: the same offset sequence [0, 262144, 0, 786432] for vertex 1, states 0-3.
    Two engines agree (mine, via o1_19.trace, and L-SI's n5x step), and n5.py reproduces the iteration count.
  - How found: climbfr19.py (ANALYSER=h3) on (offset changes − rise levels) per vertex per stretch_D, seeded from L-SI's offret_n23 with
    its start. Seed 172 found it; seed 171 found a sibling at n 23 (v = 12, 16, 20, levels [20, 21]; not pinned).
- OFFSET-ONCE (already refuted by L-SI, offret_n23): my engine reproduces L-SI's return on offret_n23 (v = 22: 131204 → 264200 → 131204,
  states 0-3). My own OFFSET-ONCE climbs (from frz40 and off_s22_n24) also found returns on this engine. Smallest pinned:
  offret_l19_n24.pg (sha1 17b41245fb87e8e2638912ea78112a3751321cd8; zlk OK, strategies verified). I do not claim it was found first.
- mkalt family (L-SI): reproduced on my engine. K − 1 in-stretch offset changes of one vertex at n = Θ(K²): 3, 7, 11, 15, 19 at n 62, 134,
  238, 374, 542 (K = 4..20), i.e. about 0.8·√n. mkalt2 (shared lines) collapses to 1 change at every K, as L-SI found. LEVEL-COUNT holds on
  the whole family (slack −1): every change is paid at a fresh h_j.

## 1. Checks and data (h3_19.py, sha1 at this commit; experiments/red/h3/)
- New in h3_19:
  - OFFSET-ONCE: per stretch_D, per vertex, the offset sequence. Returns are counted, not flagged: the conjecture is dead.
  - LEVEL-COUNT: per stretch_D, per vertex,
    - |OC| vs |RL|, with RL the top ranks of P_k Δ P_{k+1} at transitions where s^W or s^Ξ rises (LEVELCOUNT);
    - the pay form (LEVELPAY): no two offset changes paid at one level, where the paying score is s^W for d > 0 and s^Ξ for d < 0
      (TWIN-GAP (i)).
- Library (625 files, S3 + 3 starts, seed 17): 17,803 stretch_D segments, 7 in-stretch offset changes, at most 1 per vertex, 0 LEVEL-COUNT
  violations. As L-SI found, natural data never has two offset changes of one vertex in one stretch_D. The kill needs a constructed seed
  plus a climb.
- Calibration: frz3_n24 has 8 offset changes per vertex in the run and 0 inside a stretch_D (L-SI's §7 table); frz40 has 6 in-stretch
  changes, at most 1 per vertex.

## 2. Two other items closed in this box
- R77 §6 pending item: exh19 re-run with the corrected counter (≥ n + 1 states): 132,054 games, 7,188,422 all-start-pair runs at n 4-7,
  0 non-vacuous FRZ runs, 0 FAIL, best gap 0 (frzgap0_n4 again).
- Resume-list climbs, 40 min each, 0 FAIL:
  - FB-CAP within one phase (fcap3, |U| ≥ 3, f ≥ 2) from fbcap_eq_u4_n11: best 0, i.e. R71's equality, never exceeded (3.08 M
    evaluations);
  - β-fallbacks per scope run (betaclimb19 from beta2_n11): best 2, never 3 (2.52 M evaluations).

## 3. READING for the next attack (growth: offset changes per vertex per stretch_D beyond √n)
- In mkalt, a delayed arrival needs a chain of NEWLY switched edges. Once a line is wired toward a deep anchor, a better value at the deep
  end propagates through the existing pointers in the same transition. That is mkalt2's collapse, and also R76 §9's two-wave collapse.
  Distinct arrival times 1..K then cost Σ fresh lengths = Θ(K²), so K = O(√n) for constructions built from fresh delay lines.
- To beat √n, line vertices must re-switch between arrivals, which needs a trigger that changes a line vertex's best successor without a
  new line. R76 §9's additivity obstruction forbids triggers that read the chain end they feed. A trigger from the OTHER score
  (lcount_n23 shows W and Ξ reaching the same improvement at different times) is not covered by that obstruction. It is the natural
  next construction.
