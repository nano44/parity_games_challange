# R101: FB-LIN route (1), the fallback analogue of runfam (one Odd gate whose options are corridor ends). No kill: single-vertex fallback waves never revisit a vertex (R1 = 0 on 1,128 games and every climb); the corridor-gate design dies on the R100 inequality pair; new data max f 38 = 0.79n (fb38_n48, pinned)
L-RED successor 24 (Opus 5.5; D14/D15/D18; Lead 2026-10-29 02:37Z: "NEXT box: route (1) ... Success means f > n in one phase, or a family
with f/n growing ... record the obstruction if it dies. Bound the box at about 90 min."). Written 2026-10-29 from 03:20Z (date -u).
Labels: DATA / READING / OPEN. Builds on R100 (docs/red/R100-fblin-waves.md) and L-SI's docs/si/N5-RUNLIN-box24.md §1, §4, §7 (l-si).

## 1. DATA: reuse measures, and the survey
fbphase.reuse (experiments/red/fb/fbphase.py) per phase, the maximum over phases:
- RF = in-phase fallbacks that re-switch an Even vertex already switched by an earlier in-phase fallback of the phase.
- R1 = the same restricted to SINGLE-switch fallbacks (a fallback that switches exactly one vertex, the wave step of R100 §1), counting only
  earlier single-switch fallbacks.
A kill by repeated waves (R100 §0: f > n needs vertex reuse across configurations) shows up as R1 = Θ(n).
| set | games | max f | max RF | max R1 |
| --- | --- | --- | --- | --- |
| experiments/red (all .pg, own start or S3; r1survey.py) | 348 | 37 (rise_fb38_n48) | 19 (n3/out/ph7/best_7, f 23) | 0 |
| experiments/si, new, n5-exhaustive, n5-second, weak-sep, attr, alg (all .pg) | 780 | 37 (si/coarse/instances/box9/cl9_rep_b, n 48) | 17 (new/box49/out/fbclimb_rise_s21, f 37) | 1 (new/esc/instances/cond_stuck_symsi3_YE, n 32, f 3) |
- RF > 0 comes from switch-all fallbacks that move many vertices at once (early in a phase) followed by a wave over some of them
  (§2's l121rf_s72: fallbacks of 22 and 15 switches at iterations 5 and 13, then a 13-step wave re-switching 7, 8, 20, …). That reuse is
  bounded by the number of switch-all fallbacks; it is not a second wave.
- long121_n40: f 8, RF 7, R1 0 (its carries are multi-switch fallbacks: Isz 3-8).

## 2. DATA: climbs with reuse fitness (fbclimb.py --reuse, own start; 25-45 min each)
| seed | n | fitness | best (f, reuse) | shape |
| --- | --- | --- | --- | --- |
| long121_n40 ×3 | 40 | 1000 f + 300 R(≥2 switches) | f 16-21, R 30 | 20+-vertex switch-all fallbacks, then one wave |
| pl130_n40 | 40 | same | f 12, R 28 | same |
| long121_n40 ×3 | 40 | 1000 f + 1000 RF | f 12-18, RF 11-14 | two switch-all fallbacks, then one wave over their vertices |
| rise_fb38_n48 (S3) | 48 | 100 f + 1000 R1 | f 38, R1 0 | one wave; NEW DATA MAX f 38 = 0.79n (§3) |
| farrise25_n32 (S3) | 32 | same | f 25, R1 0 | unchanged |
| long121_n40 | 40 | same | f 19, R1 0 | one wave |
| lvl1 + 14 spare (R100 §2) | 51 | same | f 31, R1 0 | one wave |
No climb ever produced R1 > 0.

## 3. DATA: pin fb38_n48 (data max, not a kill)
experiments/red/fb/instances/fb38_n48.pg (sha1 bc5858a24505851a9117b8e0e43cbda9f7f4a033), full start fb38_n48.start (sha1
e72ba8b3be4dff258c02c435f3bd21d03615ea74, written by sel/fullstart2.py; every entry an existing edge; τ0 = S3). Climbed from rise_fb38_n48.
- fbphase.py: f = 38 in the phase from state 3 (66 iterations); 38 / 48 = 0.79n (previous max 37 = 0.77n). FB-LIN holds (38 ≤ 48).
- ul/vrun.sh: n5.py 66 iterations, 39 fallbacks; n5b.py --mode spec 66 iterations, 39 fallbacks (the same start file, n5b validates
  it); check_sol2 "zielonka(oink zlk) OK strategies verified" for both solutions.
- Shape: one detachment wave (R100 §1), R1 = 0.

## 4. READING: why the corridor-gate design does not give repeated fallback waves (design obstruction, not a theorem)
Design (the fallback analogue of runfam). Gate o (Odd), τ(o) = T (W high), options A and B used as the two wave sources; chain c_i → {o,
c_{i−1}}, c_1 → {o, A, B}. Waves alternate: when σ̄(o) = B (B below A) the chain detaches from o toward A; when B rises above A, σ̄(o)
flips to A, Ξ(o) = {o} ∪ Ξ(A) exceeds the detached values {c_{i−1} … c_1} ∪ Ξ(A) (o even, chain odd) and S4a re-attaches every c_i to o;
then c_1 → B starts the next wave. Good points: the lock that killed R100 (O-B) is automatic here (B, the lower option, is below the
current source A until it rises), and the gate flip IS the configuration change.
- It fails on B's rise. Wave j changes only the chain, so B's rise must read it (R100 §3). The attached chain routes through o → σ̄(o) = B,
  so a reader r on B's branch reading c_m sees its own branch: safety during wave j needs the cycle {c_m, o, B, r} odd-topped. The re-attach
  needs o even (or below the chain). The release of B to a high value H_B (B Odd → {r, H_B}) needs r even above H_B. And the next wave needs
  {B} ∪ H_B > {o} ∪ Ξ(A). Whichever of o, B, r tops the cycle, one of the three fails (o odd: no re-attach; B odd: H_B needs an even above B,
  hence r even above B, and r tops; r odd: r's route is below Ξ(A), no release above it).
- The literal runfam variant (B := c_m, the corridor end itself, no reader): with τ optimal (the TAUSTAR regime of every long run, L-SI §3),
  τ(o) = T requires Even's optimal value of o's corridor option to beat T. Even's escape from c_m runs down the detached chain to the source
  A, so value(A) > W(o), but the wave needs W(A) < W(o). The level-1 template escapes this only because its source has an edge back to the
  gate (s1 → q1), and that edge is what closes the gate at the wave end (R100 §1). Run check (dsl, m = 8, o odd 199 with options T1, c_m,
  A; TAUSTAR): τ*(o) = c_m, no gap, the chain re-points in ONE S4a step, f = 0.
- So route (1) inherits R100's obstruction. What runfam has and this lacks: its waves are S4a waves, which need no gap (W and Ξ agree), so
  its gate needs no escape. A fallback wave needs a gap at the current route for its whole length, and every gap so far closes exactly when
  its escape (the wave itself) is realised.

## 5. OPEN
- CONJECTURE R1-ZERO (DATA only, stated for the attack): in every phase, no single-switch in-phase fallback re-switches a vertex that an
  earlier single-switch in-phase fallback of the same phase switched. Max R1 is 1 on 1,128 games (one instance, f 3) and 0 in every climb.
  Not proposed as a lemma; it would mean long single-vertex waves never repeat inside a phase, which is the shape R100 §3 says is blocked.
- A kill would have to use multi-switch fallbacks repeatedly (long121's carries: RF 7 of f 8) with Θ(n) of them per phase. The climbs
  push that direction to f ≈ 0.5n at most (RF 11-14).

## DONE / FINDINGS / NEEDS
- DONE: R101 (this file); fbphase.reuse (RF, R1), r1survey.py, fbclimb --reuse / --owntau; pin fb38_n48 (n5 = n5b 66 / 39, Oink OK);
  check.sh pins its f.
- FINDINGS:
  - Route (1) (corridor gate) dies on the R100 §3 inequality pair; the literal runfam variant has no gap under an optimal τ.
  - Single-switch fallback waves never revisit a vertex in a phase: R1 = 0 on 1,127 of 1,128 games and in every climb (max 1).
  - New data max f 38 = 0.79n (fb38_n48), one wave. FB-LIN unkilled.
- NEEDS: none from the owner.
