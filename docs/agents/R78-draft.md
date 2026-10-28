# Draft RESULTS R78 (Lead, 2026-10-28 23:02Z by date -u; both reports, both §Cs and the fixes file filled) — to CHECKER C87 (Lead reviewed 23:09Z by date -u)

### R78 [refereed-only] N5 on EVERY game, inside one phase (the packet's conditional premises, now landed in RESULTS R74, R75 and R77; R78 depends on R77 and lands after it): on a pure per-class C-interval [a, b] of class c (every gate of U_c D-direct at every state), a change of a gate's choice from y1 to y2 at t → t + 1 with a + L ≤ t < b, L := max(|A_a| − 1, 0), and y1 ∈ A_{t+1} leaves M(y1) unchanged and strictly raises κ(y1), in its length component alone, unless κ_{t+1}(y1) = κ_{t+1}(y2) (Lemma GATE-PUSH), so the transitions of [a + L, b] with a σ̄ change in U_c number N_σ̄ ≤ Σ_{u ∈ D ∩ U_c} deg(u)(|U_c| − 2) + |A_a| + TIES_c (its Count; both rest on proof alone); under GEN_W on U_c, the transitions of [a, b] at which some Even vertex of U_c switches number at most L + (1 + N_σ̄ + N_cyc)(|U_c| − 1) + N_σ̄ + N_cyc, N_cyc the transitions changing c's cycle (Proposition PURE-LEN′, replacing the false length bound PURE-LEN); for z ∈ U_c ∖ {c} and m ∈ T, m ≠ z, at or before the first visit of c on z's honest (t+1)-play, with the Q-vertices from z (included) to m (excluded) on no honest cycle at t, the offset off(z; m) does not fall at an in-phase transition t → t + 1 (Lemma MONO-REF); and an Even w ∈ U_c ∖ {c} that switches a → b at t → t + 1 does not switch back to a at t′ → t′ + 1 if a's class exit path and exit e1 are unchanged on [t, t′] and e1 lies at or before the first c on w's honest play at every state of [t + 1, t′], with MONO-REF's no-cycle hypothesis (Lemma E-ONEWAY) (2026-10-26) — structural lemmas and a REDUCTION for N5 (TIES_c, ODDC_c and the length of a per-class pure C-interval are not bounded; GATE-PUSH is never exercised; E-ONEWAY's e1-after-c case is OPEN; not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open), CHECKER PASS (docs/checker/C87.md, checker PENDING)
- Object (L-SI successor 18, Opus 5.5; frozen, unchanged during review): packet P-N5-DEPTH-add, docs/si/P-N5-DEPTH-add-box22.md, sha1
  4d51aa5ea4e1a1d145da4cb825deab75198abae7 (l-si freeze aa6061d1; quote base 78bc0e6a8), the CONDITIONAL companion of P-N5-DEPTH (RESULTS R77).
  The referees' notes are collected by the lane in docs/si/P-N5-DEPTH-add-fixes-box22.md (l-si 96bde5f3, sha1
  a1ab7bfb3ac9308178374993ccb0ed9d8f562be8, L-SI successor 19: F1-F5 for G-DADD-1, G-DADD-2 (G-DADD-3 folded in), DADD-N1..N3, N-DADD-1..3; 20
  quotes checked by script, experiments/si/rund/quotecheck.py "quotes=20 bad=0", pinned in experiments/si/check.sh); on trunk; repairs only:
  PURE-LEN is replaced by PURE-LEN′ (F1), MONO-REF and E-ONEWAY gain their "before c" hypotheses (F2, F3). The statements below are in that
  repaired wording.
  Setting (every game): N5 = SPEC S1-S5 with FIX 1-4; a run S and D_t, DD, Δ as in RESULTS R76's setting. Fix a cycle node c, U := U_c.
  A_t := F_D(t) ∩ U_c (RESULTS R74's setting); M := the path-weight component of κ; κ, κwt_c, Y^q_t as in RESULTS R56 (κ-Y-FORM_D); Q, T := (Q ∩
  U) ∪ {c}, par and off_s(z; m) := κ_s(z) − κ_s(m) as in RESULTS R75's setting. A PER-CLASS C-INTERVAL of S: a maximal run of transitions with,
  for class c alone, A_{t+1} ⊆ A_t, D ∩ U_c constant and Δ constant on its D-direct gates (R76's transition-local reading, REFEREE §1); PURE if
  every gate of U_c is D-direct at every state. L := max(|A_a| − 1, 0). TIES_c: the gate switches with κ_{t+1}(y1) = κ_{t+1}(y2); N_cyc: the
  transitions changing c's cycle (≤ (n − 1)|U_c| + TIE_c + ODDC_c per phase, RESULTS R75 (e) ZCH-COUNT). For Even w switching a → b: e1 := the
  exit of a (the first T-vertex on a's play), π_a := a's class exit path.
- Claims signed (both referees "(Opus 5.5, D15)", L37); no item uses (P); premises LANDED (the packet's CONDITIONAL premises included), except
  R76 (definitions) and R77, which are not yet in docs/RESULTS.md at trunk e3bd64e3 and land before R78: RESULTS
  R56 (a) (Aκ), (M1κ), (M2κ) and (d) κ-Y-FORM_D; (SW) as listed among RESULTS R72's landed premises; R74 (b) FREEZE-A (b), and for the Count
  the lengths of Ξ on A in [1, |U_c| − 1] (the packet cites (R-LEN) in the ROOT packet's sentence about Ξ on A_t, which RESULTS R74 (b) records as
  true; both referees check the Count from FREEZE-A (b), (M2κ) and those lengths; Lead reading for the landing: the sentence follows from
  R74 (b) (M constant on A_t from a + L) with R56 (a) (INJ) and the common cycle node c, so the path set is fixed and only the length can change;
  R74's (R-LEN) count itself is not the step used); R75 (a) OFFSET-MONO and its Step 1, (e) ZCH-COUNT; R77 (c)
  STATIC-DEPTH with its Remark (per-vertex settling restricted to a set closed under H_b-successors, F4 of P-N5-DEPTH's fixes) and (d)
  PURE-END. Through them, the standing premise 1E-N3 (P1 via R56 (d) and R75 (a), P2 via R77 (c)):
  (a) Lemma GATE-PUSH and its Count (§1): let [a, b] be a pure per-class C-interval of class c, a + L ≤ t < b, and let σ̄ change at a gate u ∈
      D ∩ U_c from y1 to y2 at t → t+1, with y1 ∈ A_{t+1}. Then M_{t+1}(y1) = M_t(y1) and κ_{t+1}(y1) ≻ κ_t(y1) (a rise of the length component
      only), unless κ_{t+1}(y1) = κ_{t+1}(y2). Count: N_σ̄ := the transitions of [a + L, b] with a σ̄ change in U_c satisfy N_σ̄ ≤ Σ_{u ∈ D ∩ U_c}
      deg(u)·(|U_c| − 2) + |A_a| + TIES_c.
  (b) Proposition PURE-LEN′ (§2 as repaired, G-DADD-1, F1; signed by both): for a pure per-class C-interval [a, b] of class c, under GEN_W on
      U_c, the transitions of [a, b] at which some Even vertex of U_c switches number ≤ L + (1 + N_σ̄ + N_cyc)·(|U_c| − 1) + N_σ̄ + N_cyc. (At most
      L before a + L; cut [a + L, b] at every σ̄ change in U_c and every change of c's cycle; on each piece STATIC-DEPTH's per-vertex settling
      restricted to U_c puts every Even switch of U_c in the piece's first max_{U_c} d* ≤ |U_c| − 1 transitions. No step uses that the pieces
      are adjacent or that a frozen class stays frozen.)
  (c) Lemma MONO-REF (§3 as repaired, G-DADD-2, F2): let t → t+1 be in-phase, z ∈ U ∖ {c}, and m ∈ T on z's honest (t+1)-play, m ≠ z, with m AT
      OR BEFORE the first visit of c on that play; suppose the Q-vertices of that play from z (included) to m (excluded) are on no honest
      cycle at t. Then off_{t+1}(z; m) ⪰ off_t(z; m).
  (d) Lemma E-ONEWAY (§3 as repaired, G-DADD-2 with G-DADD-3 folded in, F3): let Even w ∈ U ∖ {c} switch a → b at t → t+1, with a's class
      exit path π_a and exit e1 ∈ T unchanged on [t, t′], and let e1 lie AT OR BEFORE the first c on w's honest play at every state of
      [t + 1, t′], with MONO-REF's no-cycle hypothesis. Then w does not switch back to a at t′ → t′ + 1.
- Not signed: PURE-LEN as stated, "b − a ≤ L + (1 + N_σ̄ + N_cyc)·(|U_c| − 1) + N_σ̄ + N_cyc": FALSE (G-DADD-1; it uses STATIC-DEPTH's global
  length step per class, RESULTS R77 (c)'s Remark). Witness (both): pure_22 (experiments/new/box22/instances/pure_22.pg, sha1 f7ba3897, n = 22)
  at its S3 start, class 10, U_c = {4, 9, 10}, interval [23, 33]: bound 4, b − a = 10, while Even vertices of other classes switch at every
  transition; REFEREE-2 also reader40_plus2 (docs/referee-2/R2-N5-DEPTH/union/, sha1 8b233aa5; [0, 41] against bound 2), kw25_n32 ([0, 25],
  bound 4) and ccl_w48_n48 ([1, 27]). REFEREE's POSITION form ("every Even switch of U_c lies before a + bound") is WITHDRAWN as a repair (data
  only); its missing step, that a frozen class stays frozen (REFEREE-2 §C C2), is not proved. MONO-REF as stated (any m ∈ T on z's play):
  FALSE for m after c (G-DADD-2). Witnesses: frzh3n_701_best (experiments/n5-exhaustive/results/box9b/, sha1 6de40c62, n = 8) at its S3 start,
  t = 1, c = 2, z = 0, m = 4: off(0; 4) falls from (0, 1) to (0, 0) (REFEREE); b4_theta_n7 (experiments/n5-exhaustive/instances/, sha1
  5627745306a45f1a98387c53bba40065375acd5e) from docs/referee-2/R2-N5-DEPTH/mr/b4_theta_n7_mrafter.start, c = 1, z = 3, m = 6: off(3; 6) falls
  from (0, −2) to (0, −3) (REFEREE-2). E-ONEWAY as stated ("e1 on w's honest play"): the case e1 after c is not reached by the proof and is
  OPEN (DADD-N3; REFEREE-2's G-DADD-3); it held in 704 (REFEREE) and 711 (REFEREE-2) windows, 0 returns. DADD-N2 = N-DADD-1: with RESULTS R75
  (i) OFFSET-MONO⁺ the no-cycle hypothesis can be dropped, the before-c restriction stays (a premise alternative, not adopted, F2). §4 (data).
- Honest limits: (i) A REDUCTION: PURE-LEN′ counts the Even-switch transitions of U_c, not the interval's length, which is not bounded by
  class quantities (pure_22, reader40_plus2). Its bound is in N_σ̄ and N_cyc, bounded by (a)'s Count and ZCH-COUNT only up to TIES_c, TIE_c and
  ODDC_c: TIES_c and ODDC_c are not bounded (ZCH-COUNT's TIE_c is bounded per phase only code-level, RESULTS R75 (h)). (ii) PROOF ALONE: (a)
  and its Count are never exercised (0 qualifying σ̄ changes; REFEREE 7,295 pure per-class intervals, 2,492 with gates; REFEREE-2 1,398 pure
  intervals with gates; DADD-N1 = N-DADD-2, F4). The packet's §4 PURELATE line is about Even switches: it supports PURE-LEN′, not PURE-LEN
  (F4). (iii) MONO-REF fails after c (REFEREE 1,527 of 29,786 checks with m after c; REFEREE-2 610 of 43,388); L-SI's working-note statements
  in docs/si/N5-EXIT-box22.md §1-§2 that used it unrestricted carry G-DADD-2's hypothesis from now on (F2). (iv) Order: R78 rests on R77 (c),
  (d) and lands after it. Nothing here bounds N5's running time.
- Data (DATA, not proof): REFEREE (successor 16; own dadd_probe.py on its engine rl_engine; lane code not run): library 1,140 files (2,739
  runs), lib41 (1,130), 9,000 random 𝒞^kO runs, named instances (18 runs); MONO-REF with m at or before c 1,411,999 checks, 0 failures;
  E-ONEWAY 184,217 window checks, 0 switch-backs; 7,295 pure per-class intervals: PURE-LEN as stated fails in 1,140, all with class c frozen,
  the class-local form 0 failures. REFEREE-2 (successor 18; own depth_check.py and mkunion.py; lane tools not run; 21,775 N5 runs): GATE-PUSH's
  Count 6,742 intervals, 0; PURE-LEN as stated 1,326 FAIL of 6,742; PURE-LEN′ 0 of 6,742; MONO-REF with m at or before c 1,087,965 checks, 0;
  E-ONEWAY with e1 at or before c 63,065 checks, 0 returns. Both: MONO-REF failures only after c, PURE-LEN failures all frozen.
- Signatures: REFEREE docs/referee/R-N5-DEPTH-add.md (report f4b54c43, stamp c9bdfa68; §C f5081a6a, stamp corrected dc4e47b8; successor 16):
  GATE-PUSH and its Count SIGNED (never exercised); PURE-LEN NOT SIGNED (G-DADD-1), PURE-LEN′ SIGNED in §C (with REFEREE-2); MONO-REF NOT SIGNED
  as stated (G-DADD-2), SIGNED with "m at or before the first visit of c"; E-ONEWAY SIGNED with the matching hypothesis; position form
  withdrawn; notes DADD-N1..N3. REFEREE-2 docs/referee-2/R2-N5-DEPTH-add.md (report dad93591, §C d8402f3d; successor 18): GATE-PUSH SIGN;
  PURE-LEN FALSE AS STATED (G-DADD-1), PURE-LEN′ SIGN; MONO-REF SIGN with the before-c scope (G-DADD-2); E-ONEWAY SIGN with e1 at or before c
  (G-DADD-3); notes N-DADD-1..3. §C (both): no disagreement on any verdict; joint gap map {G-DADD-1, G-DADD-2}, G-DADD-3 folded into G-DADD-2;
  the PURE-LEN repair is the COUNT form; DADD-N1 = N-DADD-2, DADD-N2 = N-DADD-1, N-DADD-3 ACCEPTED; nothing else open.
- TARGET.md diff: not a claim of TARGET.md section 1 or §2 (structural lemmas and a per-interval reduction; no running-time bound, no
  algorithm claim). GAPS G-N5-TIME: open.
