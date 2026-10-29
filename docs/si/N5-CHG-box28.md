# N5-CHG (box 28): the SEG-COUNT charging ((a), INTER-JOINT, DL-RUN DEAD; SEG-COUNT DEAD by L-RED R105); REL-segment LENGTH without (H4′_rel)
L-SI successor 24 (Opus 5.5; D18, Lead reading L40). Lead's brief 2026-10-29 10:06Z, STEP 1: «the SEG-COUNT charging proof (note §6):
charge each deadlock step of a REL segment to a JOINT final step (Corollary JOINT), and prove the two missing pieces: (a) no early
finalization, (b) injectivity (distinct deadlock steps charged to distinct H-sinks). Use psidrop_kill_n70 and the ladder family ... as test
cases for every lemma you state. If a lemma fails on one of them, record it DEAD with that instance and say what the proof needs instead.»
Working note, unrefereed, not frozen. Not a TARGET.md claim. Nothing here bounds N5's running time; G-N5-TIME stays OPEN.
Labels (D18 / L40): PROVED (lane) / CONJECTURE / OPEN / DATA / READING / DEAD. Counts are TRANSITIONS. Tools: experiments/si/chg/
(suffix.py, dlock.py, cclimb.py, ijcheck.py); outputs chg/*.txt, chg/out/; pins chg/instances/.

## Summary
| § | item | label |
| --- | --- | --- |
| §1 | SEG-COUNT ⇔ (deadlock steps) ≤ (surplus = Σ_t (finalizers at t − 1)); SUFFIX-COUNT (the same on every suffix [t, b]) | definitions; DATA |
| §2 | Lemma FREEZE (non-growth step: sink sets unchanged); Lemma DEADLOCK (structure of a deadlock step: zig-zag cycle of unready W-sinks and non-W H-sinks); Corollary BND (L(v) ≤ max(fW(jW v) − 1, fH(jH v))) | PROVED (lane) |
| §3 | (a) in its general form (EARLY: a non-W H-sink never finalizes before s_h) | DEAD: lay/instances/wgrow_kill_n90 |
| §3 | INTER-JOINT (a non-W H-sink that makes an intermediate switch finalizes exactly at s_h) | DEAD: chg/instances/interjoint_kill_n70 (n5b-reproduced) |
| §3 | DL-JOINT ((a) at deadlock steps: some H-sink finalizes at s_h) | CONJECTURE; DATA 15/15 |
| §4 | (b) injectivity | OPEN; what a proof needs |
| §5 | DL-HSW, DL-NEXT, GROW-PERSIST | DEAD (instances) |
| §5 | CONJECTURE DL-RUN (a deadlock step is the first transition of its run), DL-FIRST, NEWFINAL | DEAD: L-RED's segcount_kill_n20 (R105), segfam_k3_n29, segfam_k8_n79 |
| §6 | After SEG-COUNT died (L-RED R105, Lead 10:30Z): the LENGTH of a REL segment. PROVED (lane): b − a = FIN + DL, GR ≤ min(FIN, settle events ≤ 2\|E_b\|), Lemma NEW-EDGE. Conditional bounds: DL-SEP or DL-NOCONSEC ⇒ b − a ≤ 2·FIN ≤ 2\|E_b\|; FROZEN-COUNT ⇒ b − a ≤ 2\|E_b\|² + 3\|E_b\| | PROVED (lane); CONJECTURE; DATA |
| §6 | DL-SEP, DL-NOCONSEC, FROZEN-COUNT, DL-SOMEH, ZIG and the routes (L2), (L3) | DEAD: chg/instances/dlsep_kill_n70 (8 deadlocks in one segment, n5b-reproduced) |
| §7 | the length reduces to MAXV (switches of one vertex in one segment); Lemma SW-RETURN | READING; PROVED (lane) |
| §6 | LENE (b − a ≤ \|E_b\|) and LEN2 (b − a ≤ 2·SW + 1) | DEAD: L-RED R106 runquad_K8_m30_n192 (one REL segment of 263 transitions, \|E_b\| = 49, SW = 47) |
| §8 | Lemma SW-RISE (a switch strictly raises the switcher's own Ξ off its honest cycle); SW-RUN per fallback-free run (Lead: SW-PER-VERTEX) | PROVED (lane); CONJECTURE, DATA ≤ 0.667n |

## 0. Setting
As N5-LAY-box27 §0-§1 (sets S^W_t, S^H_t, U^W_t, U^H_t ⊆ E_b, maps jW, jH, W-/H-sinks, readiness, y_v = σ_b(v)) on a maximal
REL-admissible segment [a, b] of a fallback-free run, GEN_W assumed, no (H4′_rel). L(v) := the last t ∈ [a, b) with σ_t(v) ≠ σ_{t+1}(v)
(v SWITCHES in [a, b]); F_t := {v : L(v) = t}; t is a FINAL step if F_t ≠ ∅, a DEADLOCK step otherwise. fW(v) (fH(v)) := the least
t ∈ [a, b] with v ∈ S^W_t (S^H_t); fW(⊥) = fH(⊥) := a. GROWTH step: W-GROW(t) or H-GROW(t) (box 27 §1), i.e. some v ∈ E_b has
fW(v) = t + 1 or fH(v) = t + 1. s_h := fW(jW h) − 1 for an H-sink h that is not a W-sink (the JOINT step of box 27 Corollary JOINT).

## 1. Reformulation (definitions; DATA)
- b − a = #(final steps) + #(deadlock steps) and #(switching Even vertices) = Σ_t |F_t| = #(final steps) + SURPLUS, SURPLUS := Σ_t (|F_t| − 1)
  over final steps. So CONJECTURE SEG-COUNT ⇔ #(deadlock steps) ≤ SURPLUS: the charging must map deadlock steps injectively into
  surplus finalizations (a finalizer at a step with ≥ 2 finalizers, at most |F_s| − 1 charges at step s).
- SUFFIX-COUNT: slack(t) := #{v : L(v) ≥ t} − (b − t) ≥ 0 for every t ∈ [a, b). It is SEG-COUNT for the REL-admissible (not maximal)
  segment [t, b]; a backward induction would need slack(t + 1) ≥ 1 at every deadlock step t. DATA (chg/suffix.py, SUFFIX PASS): alt_all
  default starts (907 segments), alt_all pinned starts (1,249), lib41 (978), the five box-27 kill pins, the ladders ladderd0_k12/k24/k48
  (pinned starts), the 48 box-27 climb instances (lay/out, 72 segments, 13 deadlock steps): 0 failures (chg/suffix_*.txt).

## 2. PROVED (lane)
- Lemma FREEZE. If t ∈ [a, b) is not a growth step, then U^W_{t+1} = U^W_t, U^H_{t+1} = U^H_t, and the W-sinks and H-sinks at t + 1 are
  those at t. Proof. S^W, S^H are monotone in t (box 26 §5); no growth means equality on E_b; sinks are defined from U^W, U^H and the
  fixed maps jW, jH (box 27 §1). □
- Lemma DEADLOCK. Let t be a deadlock step. Then (i) t is not a growth step (so FREEZE applies); (ii) W-sinks exist and none is
  arena-ready; (iii) H-sinks exist, none is a W-sink, none switches at t to its target; (iv) every W-sink w has jH(w) ∈ U^H_t; (v) the map
  Z: w ↦ the W-sink at the end of the jW-chain (inside U^W_t) of the H-sink at the end of the jH-chain (inside U^H_t) of w is defined on
  all W-sinks, so it has a cycle: W-sinks w_1, …, w_k and H-sinks h_1, …, h_k with w_i ⇝_H h_i ⇝_W w_{i+1} (indices mod k) (box 27 §5's
  zig-zag, now proved to close at every deadlock step).
  Proof. (i) By Theorem SINK-STEP (box 27 §2) a growth step has a sink switching to its target for the last time: a final step. (ii) The
  transition changes σ (τ is constant on the run and there is no fallback), at some v ∈ E_b (box 27 §6: switchers lie in E_b ∪ T and
  vertices of T do not switch, (F1)); v ∈ U^W_t, and the jW-walk from v inside U^W_t has no repeats, so it ends at a W-sink. An arena-ready
  W-sink switches at t to its target for the last time (SINK-STEP). (iii) H-sinks exist as in (ii) with jH. An H-sink is arena-ready (box 27
  Corollary SINK-OFF), so an H-sink that is a W-sink is a ready W-sink, excluded by (ii); an H-sink switching at t to its target does so
  for the last time (SINK-STEP). (iv) If jH(w) ∉ U^H_t then y_w ∈ S^H_t (Lemma CHAIN) and w is ready (Lemma READY), against (ii).
  (v) By (iv) the jH-walk from w stays a while in U^H_t and ends at an H-sink h (no repeats); by (iii) jW(h) ∈ U^W_t, so the jW-walk from h
  ends at a W-sink. Z maps a finite set to itself. □
- Corollary BND. For every v ∈ E_b that switches in [a, b]: L(v) ≤ max(fW(jW v) − 1, fH(jH v)); and fW(v) = max(L(v) + 1, fW(jW v)),
  fH(v) = max(L(v) + 1, fH(jH v)) (L(v) + 1 := a if v does not switch).
  Proof. The b-W-play from y_v reaches jW(v) (or T_W) through Odd vertices (τ constant) and Even vertices of T (constant, (F1)); the honest
  one through Odd vertices of RO_b (σ̄ constant on [a, b], REL) and vertices of T. So v ∈ S^W_t ⇔ σ_s(v) = y_v for all s ∈ [t, b] and
  jW(v) ∈ S^W_t, which is the recursion (H: the same). Bound: put s := max(fW(jW v) − 1, fH(jH v)) ≥ a; if s ≥ b there is nothing to
  prove. Else y_v ∈ S^H_s (CHAIN), so v is arena-ready at s (READY), and y_v ∈ S^W_{s+1}; Lemma W-STICK′ (box 27 §6) gives
  σ_{s+1}(v) = y_v and σ = y_v on [s + 1, b], so L(v) ≤ s. □
  DATA: BND 0 failures on every corpus of §1; the bound is attained (MUT=1, the bound lowered by one: BND fails on seglast_kill_n29 and on
  ladderd0_k12_n48, 14 vertices, among them the ladder's H-sink 14: L = 11 = fW(jW 14) − 1).
- READING. BND alone does not bound b − a: it is a max-plus recursion along the two forests jW, jH with "+1" only on H-steps into W-sinks
  (on Lemma DEADLOCK's cycle: L(w_i) ≤ 1 + max L over w_i's H-chain, L(h_i) ≤ max L over h_i's W-chain), and it allows any number of
  transitions in which only intermediate switches happen. A proof of SEG-COUNT must use why a transition happens at all (an arena change).

## 3. (a) no early finalization: DEAD in the general form and in the INTER-JOINT form; CONJECTURE DL-JOINT
- EARLY (general (a)): «an H-sink h that is not a W-sink finalizes at s_h» is DEAD: lay/instances/wgrow_kill_n90 (box 27 pin, n5b-identical),
  segment [0, 3]: H-sinks 34, 47, 61 at t = 0 switch at 0 to their targets (last switch) while their W-chain settles only at 3 (s_h = 2);
  also 55 at t = 1. Box-27 climb instances: 28 such (H-sink, step) pairs (chg/suffix_climb27.txt); alt_all pinned starts: 1
  (red/n3/instances/n3cov_lean, [19, 21], h = 23). It holds on psidrop_kill_n70 and on the ladders k12/k24/k48 (chg/suffix.py, EARLY PASS).
  Those early H-sinks went straight to their target. Corollary JOINT (box 27) needs h still off target at s_h; this is not automatic.
- INTER-JOINT («an H-sink, not a W-sink, that makes an INTERMEDIATE switch (σ_{t+1}(h) ∉ {σ_t(h), σ_b(h)}) finalizes exactly at s_h»)
  was the repair suggested by the ladder: ladderd0_k12/k24/k48: 11/23/47 intermediate switches of H-sink 14, which finalizes at s_h = 11
  (23, 47) jointly with 1; psidrop_kill_n70: vacuous (vertex 1's intermediate switch at 2 is not by an H-sink); 35 events in the box-27
  climb instances, alt_all pinned starts 81: 0 failures. It is DEAD: lemma climb chg/cclimb.py OBJ=IE (kill = INTEREARLY_V; shaping 3 ×
  intermediate H-sink switches + early H-sinks) from ladderd0_k12_n48, step 2,971: chg/instances/interjoint_kill_n70.pg (n 70, sha1
  79a7c76a…; .start 9b313151…). REL segment [1, 7] = the whole fallback-free run (τ changes 0 → 1). H-sink 10: σ = 32, 21, 36, 24, 24, 28, 28
  on [1, 7], target 28, jW(10) = 0, whose W-play settles only at 7 (s_h = 6), yet 10 switches to 28 at 5 (L = 5): intermediate switches at
  1, 2, 3, then an early final switch. About 25 H-sinks (all with target 28, jW = 0) do the same. n5x and n5b (L-COMP, SPEC mode) give
  identical state sequences (root/n5bcmp.py); chg/ijcheck.py recomputes from n5b ALONE the run, the REL segment and its maximality, h's
  sink status, L(h) = 5 < s_h = 6, observed GEN_W (0 failures). SEG-COUNT holds there (6 transitions, slack ≥ 1).
- What the proof needs instead (READING): the intermediate switch does not keep an H-sink off target; an H-sink can move to its target as
  soon as the target's W-value beats the current option, before the W-chain is final. No early finalization can only come from the
  DEADLOCK condition itself. CONJECTURE DL-JOINT: at every deadlock step some H-sink h has L(h) = s_h. DATA: 15/15 deadlock steps
  (chg/dlock_climb27.txt, chg/dlock_sicorpus.txt: NOEARLY PASS); in all of them exactly one H-sink switches, and it is one of the
  DL-JOINT witnesses, the end of the H-chain of an unready W-sink (ZIG PASS).

## 4. (b) injectivity: OPEN
- With ≤ 1 deadlock step per segment in every instance found (15/15), (b) cannot be tested on data: the bipartite check (chg/dlock.py MATCH:
  deadlock t → s_h for a DL-JOINT witness h at t, capacity |F_s| − 1) passes trivially. A proof must exclude the design of box 27 §6 READING
  (t1 deadlock, h → c1; t1 + 1: w1 final alone; t1 + 2 deadlock, h → c2; t1 + 3: w2 and h final). Lemma FREEZE shows the two deadlocks of
  that design lie in different non-growth runs (t1 + 1 is a W-growth step), so a proof cannot argue inside one frozen sink structure.
- READING (why the design is not excluded by the lemmas we have): BND, JOINT and the sink lemmas are all compatible with it; what would
  exclude it is a statement about WHEN an option c2 can enter h's arena (Ξ(c2) rising through w1's final switch), i.e. about the honest
  frame between two growth steps. §5's DL-RUN would exclude it outright (t1 + 2 is not a run start).

## 5. Other candidates (DEAD) and CONJECTURE DL-RUN
- DEAD (chg/dlock.py on the box-27 climb corpus; not needed by the charging): DL-HSW («only H-sinks switch at a deadlock step»):
  lay/out/c_sk.pg [5, 14] t = 5 (1, 41, 48, 127, 131 switch, only 1 is an H-sink), also d29a, d29c, ll29. DL-NEXT («t + 1 is a W-growth step»):
  lay/out/d29a.pg [4, 20] t = 4 (also d29c, d29d, p29). Candidate DL-SOMEH («some H-sink switches at a deadlock step»): 15/15.
- DEAD: GROW-PERSIST («after the first growth step of a segment every step grows», suggested by the pattern D F* G* of all 13 deadlock
  segments): lemma climb OBJ=GP from psidrop_kill_n70, step 5: chg/instances/growpers_kill_n73.pg (n 73, sha1 ff73bab1…; .start
  b496c9b9…), segment [2, 5] with pattern G F G (t = 3: vertex 1 finalizes, no sink settles); n5b state sequence identical.
- CONJECTURE DL-RUN: every deadlock step t of a REL segment is the first transition r0 of its fallback-free run (so t = a = r0).
  DATA: all 15 deadlock steps (box-27 climb instances, all experiments/si instances, alt_all both start sets, lib41) are at r0, i.e.
  right after τ changed (d29a-d, m_sk, p29, s_hg, sgkill1, ll29), λ_Ξ changed (c_sk2, d_sk, ll29) or a fallback (c_sk); all 15 segments
  start at their run start. CONJECTURE DL-FIRST («a deadlock step is the first step a of its segment») is implied and has the same data.
- Consequence (PROVED (lane), conditional): DL-FIRST ⇒ b − a ≤ #(switching Even vertices in [a, b]) + 1 ≤ |E_b| + 1 ≤ n on every maximal
  REL-admissible segment, without (H4′_rel) (one deadlock step at most, every other step final). DL-FIRST + DL-JOINT ⇒ SEG-COUNT
  (the one deadlock step is charged to the JOINT step s_h of its witness; injectivity is trivial).
- READING (why run starts): for t > r0, σ_t is the S4a optimum against the SAME τ over the arena of state t − 1, so W_t is pointwise
  arena-optimal; at r0, σ_{r0} was optimal against the old τ (or came from a fallback). Every deadlock found sits where this W-optimality
  of the current strategy against the current τ is missing. A proof of DL-RUN would use exactly that; it is the next proof target.
- UPDATE 10:39Z: DL-RUN and DL-FIRST are DEAD (DEAD.md box 28): L-RED's hand-built segcount_kill_n20 (claude/l-red 22d7c6ab,
  docs/red/R105-segcount-kill.md; copies in chg/instances/red/, sha1 2783f64d… / 97ba6b29…) has deadlocks at t = 0 and t = 2 of its run
  [0, 4] (r0 = 0); segfam_k3_n29: t = 0, 2, 4; segfam_k8_n79: t = 0, 2, …, 14 (chg/dlock.py DLRUN FAIL, DLFIRST FAIL; n5x = n5b,
  root/n5bcmp.py). The same instances kill CONJECTURE SEG-COUNT (R105, EXC = K − 1) and the candidate NEWFINAL («at t > r0 some switch to
  an arena edge outside A(t − 1) is final»; held on 240 late transitions of the climb corpus and ~12,000 library ones). The READING above
  (W-optimality against the same τ after r0) does not prevent deadlocks: in the family each deadlock after r0 is a NEW arena edge (C_i enters
  h's arena through w_{i−1}'s final switch).

## 6. The LENGTH of a REL segment without (H4′_rel) (Lead's redirect 10:30Z)
Notation per segment: FIN final steps, DL deadlock steps, GR growth steps, SW switching Even vertices (= Σ_t |F_t| ≥ FIN), a FROZEN RUN :=
a maximal run of consecutive non-growth steps (sinks constant on it, Lemma FREEZE).
- PROVED (lane), counting. (i) b − a = FIN + DL. (ii) GR ≤ FIN (Theorem SINK-STEP: a growth step is a final step). (iii) GR ≤ (settle
  events) ≤ |U^W_a ∩ E_b| + |U^H_a ∩ E_b| ≤ 2|E_b| (a growth step settles some v in one frame, each v settles at most once per frame).
  (iv) the frozen runs number ≤ GR + 1 and b − a = GR + Σ (frozen-run lengths).
- Lemma NEW-EDGE (PROVED, lane). If t − 1 and t lie in one fallback-free run and σ_{t+1}(v) ∈ A(t − 1, v) for every Even v, then
  W_{t+1} = W_t (a W-FLAT transition). Proof. σ_{t+1} then uses only arena edges of state t − 1, and σ_t is pointwise W-optimal over such
  strategies (S4a against the same τ): W_t ⊵ W_{t+1}; W-MONO gives ⊴. □ So every non-W-flat transition after r0 switches some vertex to
  an edge outside the arena of the previous state. DATA: W-flat late transitions 21 (alt_all), 39 (lib41), 0 (climbs, family); NEW-EDGE
  0 failures (chg/dlock.py NEWEDGE PASS). It does not say the new-edge switch is final (NEWFINAL is DEAD).
- Conditional length bounds (PROVED, lane, from (i)-(iv)):
  (L2) CONJECTURE DL-SEP («two deadlock steps of one REL segment are separated by a growth step», i.e. ≤ 1 deadlock per frozen run) ⇒
       DL ≤ GR (the last step b − 1 is a growth step: its switchers settle at b in both frames; so after the last deadlock there is one
       more growth step) ⇒ b − a ≤ FIN + GR ≤ 2·FIN ≤ 2·SW ≤ 2|E_b| ≤ 2n − 2. The same follows from the weaker CONJECTURE DL-NOCONSEC
       («no two consecutive deadlock steps»): then t ↦ t + 1 maps deadlock steps injectively to final steps (b − 1 is final), DL ≤ FIN.
  (L3) CONJECTURE FROZEN-COUNT («a frozen run is no longer than the number of Even vertices switching in it», SEG-COUNT inside one frozen
       sink structure) ⇒ b − a ≤ GR + (GR + 1)|E_b| ≤ 2|E_b|² + 3|E_b| = O(n²).
  Either gives a polynomial per-segment length without (H4′_rel), hence with Corollary REL-SPLIT's cutting |S| ≤ SEG·(2n − 1) resp.
  SEG·O(n²) per fallback-free run (GEN_W kept; SEG still needs CONJECTURE SEG-RUN).
- DATA (chg/lenstat.py, chg/dlock.py; chg/lenstat_*.txt, chg/dlock_*.txt): L-RED's family mkk.py K = 2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24
  (generated from claude/l-red 22d7c6ab; chg/lenstat_redfam.txt): b − a = 2K, FIN = GR = DL = K, SW = K + 1, |E_b| = 2K + 1, frozen runs all
  of length 1 (pattern D G D G … D G): DL-SEP, DL-NOCONSEC, FROZEN-COUNT hold, (L2) is tight (b − a = 2·FIN). Library (alt_all both
  start sets, lib41: 3,134 segments, no deadlock), all experiments/si instances (702 segments, 15 deadlocks), box-27 climbs (72 segments,
  13 deadlocks, frozen runs up to 6 steps, ≤ 2 switches of one vertex inside a frozen run): DL-SEP, DL-NOCONSEC, FROZEN-COUNT, DL-SOMEH,
  DL-JOINT, BND 0 failures. LENE (b − a ≤ |E_b|) holds everywhere, tight on the family (2K = |E_b| − 1).
- READING (what a proof of DL-NOCONSEC needs, and why it may fail): after a deadlock at t (an H-sink h moves to a W-better, honest-improving
  non-target c1), the next step is final in every instance because h's honest rise makes the W-sink at the end of its H-chain ready, or a
  vertex of that H-chain takes its final successor (d29a: a snake of σ-final, non-settling switches up a W-sink's H-chain, one per step).
  A two-stage H-chain (y_w ⇝ u ⇝ h with u a non-sink that must also make an intermediate switch) would give two consecutive deadlocks; I see
  no lemma that forbids it, so DL-NOCONSEC is plausibly killable by L-RED's gadget method; FROZEN-COUNT would survive that design
  (2 steps, 2 switchers).
- UPDATE 10:46Z: DL-SEP, DL-NOCONSEC, FROZEN-COUNT (and DL-SOMEH, ZIG) are DEAD, and with them the routes (L2), (L3) (DEAD.md box 28):
  lemma climb chg/cclimb.py OBJ=GP (kill = DL-SEP / DL-NOCONSEC / FROZEN-COUNT failure; shaping deadlocks, non-growth steps, frozen-run
  excess) from L-RED's segfam_k3_n29, ~10,000 steps: chg/instances/dlsep_kill_n70.pg (sha1 e500ea47…; .start f5569821…). The run [0, 12]
  is one maximal REL segment; 12 transitions with pattern F D D D F D D D D D G G (FIN 4, DL 8), ONE frozen run [0, 10) with 9 switching
  Even vertices, then 11 vertices finalize at t = 10. Deadlocks 5, 6, 7: a SNAKE of intermediate switches of non-sinks, each to the
  previous switcher (4: 31 → 10; 15: 23 → 4; 35: 23 → 15); then 20: 14 → 16, 44: 14 → 20 (44 returns to 20, which it left at 3). Every
  deadlock reproduced from n5b alone (lay/relcheck.py), n5x = n5b. Later climb states (chg/out/gp3_k3*.pg: [1, 13], FIN 2, DL 10) push the
  same way. Still holding there: b − a ≤ SW (12 ≤ 26), LEN2, LENE (12 ≤ |E_b| = 41), BND, DL-JOINT.

## 7. What is left (READING; OPEN)
- After SEG-COUNT (L-RED R105) and dlsep_kill_n70, nothing ties deadlock steps to settling, to the sink structure or to growth: inside
  one frozen sink structure an honest snake of intermediate switches can run, and an H-sink can climb a ladder of intermediate options.
  The only per-step currency that is never empty is a SWITCH: b − a ≤ TOT := Σ_v (switches of v in [a, b]) ≤ SW · MAXV. So a polynomial
  REL-segment length without (H4′_rel) follows from a polynomial bound on MAXV, the switches of ONE Even vertex inside one REL segment.
  DATA: MAXV ≤ 48 at n 156 (ladderd0_k48, its H-sink), K + 1 at n 10K − 1 (L-RED's family, its H-sink), 4 (dlsep_kill_n70).
- Lemma SW-RETURN (PROVED, lane; the argument of box 27 Lemma H-STICK): if v leaves a successor c at s1 and switches back to c at s2 > s1
  in [a, b], then Ξ_{s2}(c) ▷ Ξ_{s1}(c). Proof: (SW) at s2 and s1, Ξ-SUCC and R15 (a): Ξ_{s2}(c) ▷ Ξ_{s2}(σ_{s2} v) ⊵ Ξ_{s1+1}(σ_{s1+1} v)
  ⊵ Ξ_{s1}(σ_{s1+1} v) ▷ Ξ_{s1}(c). □ So switches of v are bounded by out-degree × (1 + the number of honest-value rises of v's successors
  between its visits); dlsep_kill_n70's vertex 44 returns to 20 after Ξ(20) rose through 20's own switch at 8. This is a recursion, not a
  bound; it is the next proof target, together with L-RED's attempt to exceed n − 1.

## 8. Per-vertex switches per fallback-free run (Lead 10:48Z: CONJECTURE SW-PER-VERTEX, after L-RED R106)
- DEAD (DEAD.md box 28): LENE («b − a ≤ |E_b|») and LEN2 («b − a ≤ 2·SW + 1»), and with them every per-segment LINEAR length bound in
  |E_b| or SW: L-RED's runquad_K8_m30_n192 (claude/l-red 86f24219, R106; copy chg/instances/red/, sha1 ebaa6ac5… / 4ba9f860…): one
  fallback-free run [0, 263] = one maximal REL segment, |E_b| = 49, SW = 47, FIN = 45, DL = 218, TOT = 481 switches (chg/lenstat.py).
  BND and FROZEN-COUNT still hold there (frozen runs of length 1 and 9). The run length is Θ(n²) on L-RED's family mkr.py (L ≈ n²/144).
- Lemma SW-RISE (PROVED, lane). Let t → t + 1 be a transition of a fallback-free run and v an Even vertex with σ_{t+1}(v) = w ≠ σ_t(v) = u
  such that v is on the cycle of neither its honest play at t nor at t + 1. Then Ξ_{t+1}(v) ▷ Ξ_t(v).
  Proof. v's honest plays at t and t + 1 are v·(u's play) and v·(w's play), and these avoid v. RESULTS R15 (a) (Lemma A, VJ00 Lemma 5.7)
  gives Ξ_{t+1}(w) ⊵ Ξ_t(w); (SW) gives Ξ_t(w) ▷ Ξ_t(u). Prepending v to a play that avoids v is strictly order-preserving under S1's order
  (the cycle node is unchanged; v enters both P-sets or neither, so the largest rank of the symmetric difference is unchanged (RESULTS R84
  Fact DELTA); both lengths grow by 1). So Ξ_{t+1}(v) = v ⊕ Ξ_{t+1}(w) ⊵ v ⊕ Ξ_t(w) ▷ v ⊕ Ξ_t(u) = Ξ_t(v). □
  DATA (chg/pervert.py, all switches of all fallback-free runs): the only switches with Ξ_{t+1}(v) = Ξ_t(v) are at v's OWN cycle node
  (R15 (b)'s length-only switches): FLATCN = 7 (alt_all), 8 (alt_all pinned starts), 19 (lib41), 6 (experiments/si instances); SWRISE_V
  = 0 (no other flat switch) on every corpus, the runquad family (mkr.py (K, m) = (3, 4) … (12, 4), (6, 40)) and dlsep_kill_n70.
- Corollary. SW(v) ≤ RISE(v) + (own-cycle-node switches of v) in every fallback-free run: switches are bounded by the rises of the
  switcher's OWN honest value (with Lemma SW-RETURN, also by its successors' rises). It is a reduction, not a bound: RISE(v) ≤ n is FALSE
  (RISEN: grun/out/gc1 etc., 34 rises in a run of 35 at n 31; alt_all pinned red/so/instances/so_th_n32: 33 > 32): a vertex downstream of
  everything rises at almost every step. The usable count is the number of DISTINCT successor values Ξ_t(σ_t v) at v's switch times
  (strictly increasing by (SW) and Ξ-SUCC), which is SW(v) + 1 itself; its P-part is L-LIT's MATCH-Φ count (docs/lit/T33-match-phi.md,
  trunk): matched P-changes raise the potential Φ (range O(n²)), carries (NM) are the open part.
- CONJECTURE SW-PER-VERTEX = the fleet's CONJECTURE SW-RUN (every Even vertex switches O(n) times per fallback-free run; Θ(n²) runs would
  then be tight against runquad). DATA (chg/pervert.py, chg/pervert_*.txt): max SW(v)/n = 0.667 (experiments/si/root/out/swr_sc24_s8, n 21:
  vertex 0 switches 14 times in a 14-step run, cycling 9 → 12 → 4 four times: each re-entry after the successor's Ξ rose, Lemma SW-RETURN),
  0.583 (lib41 sc24), 0.308 (ladder k48), (2K − 1)/n ≤ 0.142 on the runquad family; SW(v) ≤ n: 0 failures (PERV PASS) on every corpus.
  (Per PHASE it is false: SW-LIN DEAD, swlin_kill_n26, fallbacks re-arm; N5-ALT §10.)

## DONE / FINDINGS / NEEDS
- DONE: this note; tools chg/suffix.py (SUFFIX-COUNT, BND with MUT, EARLY, INTER-JOINT), chg/dlock.py (deadlock anatomy and candidates),
  chg/cclimb.py (lemma climbs OBJ=IE, GP), chg/ijcheck.py (n5b-only check of an INTER-JOINT failure); pins chg/instances/
  (interjoint_kill_n70, growpers_kill_n73, dlsep_kill_n70; copies of L-RED's R105 pins in chg/instances/red/); chg/lenstat.py (length
  statistics), chg/revisit.py, chg/pervert.py (per-vertex switches); data chg/*.txt; climb logs chg/climbs_box28.txt; DEAD.md "box 28"; check.sh "box 28" (5 blocks).
- FINDINGS: (1) PROVED (lane): FREEZE, DEADLOCK (the zig-zag cycle closes at every deadlock step), BND, NEW-EDGE, the counting (i)-(iv)
  of §6. (2) DEAD: general (a) (wgrow_kill_n90), INTER-JOINT (interjoint_kill_n70), DL-HSW, DL-NEXT, GROW-PERSIST (growpers_kill_n73),
  DL-RUN, DL-FIRST, NEWFINAL (L-RED's segcount_kill_n20 / segfam_k3_n29 / segfam_k8_n79). SEG-COUNT itself: DEAD by L-RED R105 ((b) fails
  exactly as §4 predicted). (3) The length routes (L2) (DL-SEP / DL-NOCONSEC ⇒ b − a ≤ 2·FIN) and (L3) (FROZEN-COUNT ⇒ O(n²)) are DEAD
  (dlsep_kill_n70: 8 deadlocks, 6 consecutive, in one segment); LENE (b − a ≤ |E_b|) and b − a ≤ SW still hold in all data except L-RED's
  family (b − a = 2K > SW = K + 1). (4) What is left: a per-vertex switch bound (§7, §8); Lemmas SW-RETURN, SW-RISE PROVED (lane); LENE, LEN2 DEAD (runquad,
  L-RED R106); SW-RUN DATA ≤ 0.667n.
- NEEDS: none from the owner.
