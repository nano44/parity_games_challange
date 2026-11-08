# L11: OSC-ROOM on small exact cases (BOX L11, L-LOWER successor 11; GO from the Lead 12:38Z 2026-11-08)
Labels: PROVED (lane, unrefereed) / CONJECTURE / DATA / DEAD / READING. Every DATA clause names its counter (unit, set, scope).
Model and notation as L7 §0, L8 §0, L9, L10 (R104 IDEAL rules; simulator l6/sim6.py; pair j = movers 2j, 2j + 1; c_j = o(j − 1);
q_j = 2j, f_j = 2j + 1 in the targets built here). closure(x) = movers reachable from x by the wiring (either option).
Nothing here is a result in the sense of CLAUDE.md; G-N5-TIME stays OPEN. Not a TARGET.md claim (§9).

## 0. Question, instances, tools (experiments/lower/l11/)
- Box question (Lead): can ONE shared helper cascade serve every capped level, or does each level need its own oscillator
  (L10 §3c CONJECTURE OSC-ROOM; per-level ⇒ d(h + 1) ≥ d(h) + d(h − c), T polynomial in d)? Decide on h = 3, 4 exactly.
- ttarget.py: the TIGHT h-capped core target from a capped (h − 1)-genome = the small-h version of l10/build.core8 (minimal
  stretch of pairs 0..h − 2 under P-TOWER-FUEL Lemmas 2, 3 at h, then pair h − 1 added: f at the first step of every (h − 1)-window,
  q at the second). «Tight» = T = F(h − 1) = 2^(h+1) − 2: o(h − 1) changes at every step.
- tsat.py: hsat.py's exact encoding (l8; free wiring, ranks, signs, starts, helper trajectories) for ANY clamped core target. The
  helper gates are SAT variables, so one instance covers all gate cases. Sharing modes: `disj` = no helper is a client of two core
  levels (client(j, y): a mover of pair j reaches helper y by a path whose inner movers are helpers); `shared:J1,J2`; `noread`.
  Env PREFIX=T0 cuts the target to rows 0..T0. Validated: HS2_d3's own core (T 6): d 2 UNSAT (DRUP VERIFIED, 252 lemmas),
  d 3 SAT, decoded genome replayed by sim6 (core = target).
- annk.c (l10/ann.c, helper-gate mutation generalised), mkstart.py, viol.py (per-(step, mover) violations), req.py (required
  preferences and trigger candidates), topstarve.py (TOP-ONLY change points), clients.py (helper sharing in a realized tower),
  slackvar.py, schedtarget.py.
- Instances (sha1): TT3_HS2 7db3f03d (from HS2_d3 8ddebddc), TT3_HIT7 792a6d52 (from HIT7 6a3b274d), TT4_HIT7 4452f39b,
  TT3_REC10 7b7ed360, TT4_REC10 74930dea, TT5_REC10 e0430d29 (from rec/REC_d10_tower_mu30.txt eea2b203 = text copy of
  l3/kill/REC_d10_tower_mu30.json cc94dc9c; sim6: d 10, T 35, F 2 6 14 30 23 …, 4 caps); RC3_REC10 0d6ec3f3 (REC10's own pairs 0-2
  core run, not tight, realized by REC10 at d 10); SC3_a110 5d0728ff (l7/sched.py, T 16); out/sv/TT3_HS2_s<k> (row k doubled).

## 1. Exact small cases (DATA; unit = SAT instance; scope = the clamped core target named, helpers free as in tsat.py)
| target | h | T | d | result | solver, time |
| --- | --- | --- | --- | --- | --- |
| T2_HS2self (tight) | 2 | 6 | 2 | UNSAT, DRUP VERIFIED | Glucose4 0 s |
| T2_HS2self | 2 | 6 | 3 | SAT, replay exact | Glucose4 0 s |
| T2_HS2self, mode disj | 2 | 6 | 3 | SAT, replay exact (each level owns its helpers) | Glucose4 1 s |
| TT3_HS2 (tight) | 3 | 14 | 4 | UNSAT, DRUP VERIFIED (§1a) | Glucose4 45 s |
| TT3_HIT7 (tight) | 3 | 14 | 4 | UNSAT, DRUP VERIFIED (§1a) | Glucose4 44 s |
| TT3_HS2, PREFIX 7 | 3 | 7 | 4 | UNSAT (solver result; proof not kept) | Glucose4 307 s |
| TT3_HS2_s0 .. s13 (one slack step each) | 3 | 15 | 4 | UNSAT, all 14 (solver results; proofs not kept) | Glucose4 36-54 s each |
| TT3_HS2, TT3_HIT7 | 3 | 14 | 5 | TIMEOUT | Glucose4 3,600 s each |
| TT3_HS2 | 3 | 14 | 5, 6 | no answer (stopped by the 2-h task limit, ~7,000 s) | CaDiCaL 1.9.5 |
| TT3_HS2, PREFIX 7 | 3 | 7 | 5 | TIMEOUT | Glucose4 800 s |
| T2_HS2a11self (HS2a11_d4's own core; realized at d 4) | 2 | 8 | 3 / 4 | UNSAT 4 s / TIMEOUT 600 s | Glucose4 |
- Reading. h = 3 needs d ≥ 5 on both tight targets (as on the sequential targets, L9 e198d0b6), and one slack step does not change
  that at d = 4. The discriminating depth d = 5 is out of reach: the solver stalls already on the SAT side at ~25k variables
  (T2_HS2a11self at d 4 is SAT — HS2a11_d4 realizes it — but no model in 600 s). So whole-instance exact SAT cannot decide
  OSC-ROOM at h = 3 (and a fortiori h = 4: TT4 at d ≥ 7) with this encoding inside the 2-hour limit.
### 1a. DRUP checks (l8/sat/drup.c, default mode; proofs from Glucose4)
- TT3_HS2 at d 4: CNF sha1 bceb3e86c406361aeac106b2f0a91b6abcdb35df (97,449 clauses), proof cfcce3378f7f80f15b6df307ec5bbd5faf419711:
  «s VERIFIED (251384 lemmas RUP-checked)», 215,031 deletion lines applied.
- TT3_HIT7 at d 4: CNF sha1 3f18a265b34d85f5bd830dae7905804ca9842db6 (98,632 clauses), proof 5bf4837915e9faea6dd8d37a736bde321f27cf73:
  «s VERIFIED (257409 lemmas RUP-checked)», 211,096 deletion lines applied.
- drup.c prints VERIFIED only when the input plus the lemmas is refuted by unit propagation at the end (l. 97-98); both proofs end
  with the empty clause. Scope of both UNSATs: the clamped tight target named, at d = 4 (one helper pair), every wiring, rank order,
  sign, helper gate, helper start and helper trajectory allowed by tsat.py's encoding (= hsat.py's, validated in §0).
  The CNFs are rebuilt exactly by `python3 tsat.py out/TT3_HS2.txt 4 none g4 900 OUTPREFIX` (resp. TT3_HIT7; the build is deterministic); the proofs (~300 MB) are
  not committed.

## 2. The annealer is no test at small h (DEAD as a method; DATA; unit = run; scope = annk.c from the empty genome, T 1.0)
- annk reaches 0 on T2_HS2self at d 3 (87k iterations), but on h = 3 it stalls everywhere: TT3_HS2 best 4 (d 5, 6, 8, 10; 18-28 M
  iterations each), TT3_HIT7 best 4 (d 8), SC3_a110 best 4, SC3_a111 best 7 (d 6), and RC3_REC10 best 12 / 13 at d 6 / 10, although
  REC10 itself realizes RC3_REC10 at d 10 (viol.py scores REC10 at 0 on it, and HS2_d3 at 0 on T2_HS2self: the scorer is right).
  So a stall of this search is no evidence of infeasibility at small h. The stalls on TT3_HS2 always included step 7, mover 5
  (f2), the step where pair 0 and f1 move together with f2 (viol.py).

## 3. Where the loop comes from: TOP-ONLY change points (PROVED parts + DATA)
- Rule (PROVED, lane; R104 / R105: pref_x is a function of the states of closure(x)). If x's required preference differs at two
  free pre-states a < b, some mover of closure(x) changes at a step in (a, b]. Call the point TOP-ONLY if, in the core, only
  movers of the top pair h − 1 change in (a, b]: then closure(x) holds a top-pair mover or a helper that changes there.
- Lemma TOP-LOOP on TT3_HS2 and TT3_HIT7 (PROVED, lane; req.py tables). q2's requirement changes from pre-state 0 to 1 and only f2
  changes at step 1 in the core; f2's requirement changes from 0 to 2 and only q2 changes in steps 1-2. If neither has a helper
  changing there in its closure, f2 ∈ closure(q2) and q2 ∈ closure(f2), a cycle. So every realization (any d) has a helper in
  closure(q2) ∪ closure(f2) that changes at step 1 or 2. In TT3_HS2, every lower mover 0-3 also has a TOP-ONLY point (mover 0
  at step 10, 1 at 6, 2 at 4, 8, 12, 3 at 2: only q2 changes there), so pairs 0-1 must read q2 or a helper changing at those
  steps, and q2 / f2 must then be fuelled without reading those readers: the L10 loop (§2e-§3d) at h = 3. ∎
- DATA (topstarve.py; unit = change point of a lower-pair mover (pairs 0..h − 2), i.e. two consecutive free pre-states with
  different required preference; set = all of them; scope = the stored run / the target):
  | run or target | h | T | slack steps (o(h − 1) unchanged) | change points | TOP-ONLY |
  | --- | --- | --- | --- | --- | --- |
  | HS2_d3 (realized) | 2 | 6 | 0 | 2 | 2 (100%) |
  | REC_d10_tower (realized) | 4 | 35 | 5 | 22 | 9 (41%) |
  | H5_d20 (realized) | 5 | 136 | 74 | 52 | 3 (6%) |
  | H6_d24 (realized) | 6 | 209 | 83 | 114 | 29 (25%) |
  | HIT7 (realized) | 7 | 299 | 45 | 240 | 87 (36%) |
  | TT3_HS2 / TT3_HIT7 (tight) | 3 | 14 | 0 | 8 / 8 | 6 (75%) / 5 (62%) |
  | TT4_HIT7 / TT4_REC10 (tight) | 4 | 31 / 30 | 1 / 0 | 22 / 22 | 13 (59%) / 8 (36%) |
  | TT5_REC10 (tight) | 5 | 62 | 0 | 52 | 32 (62%) |
  | core8_HIT7 (L10's level-8 target, tight) | 8 | 510 | 0 | 494 | 262 (53%) |
- No realized tower with h ≥ 3 is tight (slack steps 5 / 74 / 83 / 45); only h = 2 (HS2_d3) is. L10's level-8 target is tight
  because the MINIMAL stretch met Lemma 3's bound exactly (T′ = 510 = F(7)); its 262 TOP-ONLY points are L10's retrigger bill (261
  + the step-3 hold). In a tight target every step at which o(h − 2) holds has only q_(h−1) changing in the core, so a lower mover
  that holds and then moves there needs q_(h−1) or a helper changing at exactly that step. READING: this is the root of the
  recursion L10 §3d observed (cut at level j ⇒ the same loop at j − 1): the cut needs a helper clock that does not read the level
  being cut, and in a tight target there is no core step without the top pair to time it.

## 4. Sharing in the realized towers (DATA; clients.py; unit = moving helper; set = the helpers that move in the stored run;
scope = helper-only wiring paths from the core, as tsat.py's `disj`)
| tower | d | caps | moving helpers | by number of client levels (k: count) | private helpers per level 0..h−1 |
| --- | --- | --- | --- | --- | --- |
| HS2_d3 | 3 | 2 | 1 | 2: 1 | 0 0 |
| HS2a11_d4 | 4 | 2 | 3 | 2: 3 | 0 0 |
| REC_d10_tower | 10 | 4 | 12 | 0: 3, 1: 5, 2: 3, 3: 1 | 1 0 4 0 |
| H5_d20 | 20 | 5 | 27 | 0: 4, 1: 7, 2: 9, 3: 1, 4: 6 | 0 0 4 2 1 |
| H6_d24 | 24 | 6 | 34 | 0: 9, 1: 12, 2: 3, 3: 8, 4: 1, 5: 1 | 0 1 1 3 7 0 |
| HIT7 | 28 | 7 | 36 | 0: 6, 1: 6, 2: 4, 3: 2, 4: 10, 5: 1, 6: 1, 7: 6 | 2 1 0 0 0 3 0 |
- In HIT7, 6 moving helpers are read by ALL 7 capped levels and 10 by 4 levels; no level owns more than 3 private helpers. Every
  realized tower uses one shared helper system; none has a per-level oscillator. At h = 2, per-level ownership is also POSSIBLE at
  the least d (T2_HS2self, mode disj, SAT at d 3, §1): neither form is forced there.
- Caveat: «client» counts helper-only paths; a level can also use another level's helpers through the core movers it reads.

## 5. Verdict on OSC-ROOM, and what it implies for the tower route
- OSC-ROOM is SHARPENED, not decided. Exact small-case SAT does not reach the question (§1: h = 3 needs d ≥ 5, and d = 5 is out
  of reach; h = 4 more so). Not PROVED, not DEAD.
- What is established. (i) PROVED (lane): TOP-LOOP on the tight h = 3 targets: the top pair cannot be fuelled by the core alone,
  and the lower pairs' TOP-ONLY points tie them to the top pair or to helper clocks (§3). (ii) DATA: every realized tower
  (h = 2, 4, 5, 6, 7) uses ONE shared helper system (§4), with d = 3, 10, 20, 24, 28 (upper bounds for S(h) at h = 4..7; exact
  S(2) = 3); (iii) DATA: no realized tower with h ≥ 3 is tight, while L10's level-8 target is; tight targets have 53-75% TOP-ONLY
  change points against 6-41% in the realized towers with h ≥ 4.
- CONJECTURE OSC-ROOM′ (replaces OSC-ROOM's per-level reading). The recursion of L10 §3d (each cut re-creates the loop one level
  down) is a property of the TIGHT re-timing T′ = F(h − 1), where every idle step of pairs 0..h − 2 has only q_(h−1) moving. With
  slack (T′ > F(h − 1)), lower pairs can be retriggered at the slack steps, and one shared helper cascade can serve all levels as
  in H5-HIT7. Support: §3 and §4 (DATA, READING); no exact test separates tight from slack at d ≤ 4 (§1). Refuted by: a slack
  level-8 target whose exact searches show the same level-by-level recursion.
- Implication for the tower route against N5. Nothing measured here supports super-linear d: the per-level («Fibonacci») form of
  OSC-ROOM has no instance among the realized towers, and its only evidence (L10 C4-C11) was gathered on a tight target that no
  realized tower with h ≥ 3 resembles. The linear DATA d(h) = 20, 24, 28 (h = 5, 6, 7) stands, with one shared cascade. So the
  route stays open with d linear as the working CONJECTURE (towers extend ⇒ N5 needs time exponential in d on them); it is NOT
  shown. Next step for level 8: a NON-minimal re-timing of HIT7's pairs 0-6 (T′ > 510), with slack steps where the TOP-ONLY points
  of core8 sit (e.g. the 127 q6 and 63 q5 retriggers of L10 §1a), and the C10-style search rerun on it.
- What this does NOT say: that slack targets are realizable at h = 8; that d stays linear for all h; anything about N5's default
  start (S3).

## 6. Addendum (BOX L12, 17:2xZ): OSC-ROOM′ DEAD for re-timings
- docs/lower/L12-slack.md §1 (Lemma BILL-FLOOR, PROVED, lane): every re-timing of HIT7's pairs 0-6 for level 8 pays a retrigger
  bill of ≥ 262, and the least-bill one is core8 itself (sha1 c6e19673). Slack (T′ > 510) cannot lower the bill. So §5's
  OSC-ROOM′ and its «next step» are DEAD as stated. The §3-§4 DATA stand; the revised reading is CONJECTURE OSC-ROOM″ (L12 §3).

## 9. Diff against TARGET.md
No statement mentions a parity game, a winning region, an algorithm's running time or a complexity class. All are about the IDEAL
model's step sequence (R104's definition) on 𝓛^R_d and its F-profile. Not M3, not a step-4 pass, not a TARGET.md claim.
