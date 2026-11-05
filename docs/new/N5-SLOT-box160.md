# Box 160 N5-SLOT-TRADE (interim): the level-0 step acts on the levels above through two channels, the W-keys (b_0) and the Ξ-values; exact maxima per channel at d = 3, 4 show the W-channel alone almost reaches T*(d), and the exact single-channel trade seg1 + tail ≤ T*(d − 1) of d = 3 fails at d = 4 (excess 1)
L-NEW successor 52, 2026-11-05 (date -u: see the commit). Lead brief BOX 160 (SLOT-TRADE, proof side; obstruction in the W-gate).
Labels: PROVED (lane), EXACT (CaDiCaL via pysat, replayed under two simulators; machine-checked, not Lean), DATA, DEAD, CONJECTURE,
READING. Model: RESULTS R104's definition; notation of P-IDEAL-SLOT §0 (RESULTS R109). Not a TARGET.md claim. No polynomial bound.
SLOT-TRADE, IDEAL-ACYC-POLY and G-N5-TIME stay OPEN.

## 0. Answer
- Scope of every EXACT number below: 𝓛^R_d = the 2-wide degree-2 ladders in L-RED's R197 convention (option k of a level-l ≥ 1 mover
  W-points to mover 2(l − 1) + k; no degree-1 padding), all Ξ-data, gates and starts; T^R(d) := max T over 𝓛^R_d. L-RED (R197, R202):
  T^R(2), T^R(3), T^R(4) = 4, 8, 13 (exact), T^R(5) ≥ 15. P-IDEAL-SLOT's T*(d) is over the wider 𝓛_d (any W-targets, padding allowed);
  T^R(d) ≤ T*(d). Whether T^R = T* is not known (FINDING F-1: the brief's «T*(d) = 4, 8, 13» are T^R values).
- Two channels. A level-0 step acts on the movers of level ≥ 1 in exactly two ways:
  - W-channel: it may flip b_0 := [key of level-0 mover 0 < key of level-0 mover 1]. On 𝓛^R_d both level-1 movers prefer the option
    whose W-target has the smaller key, so a flip of b_0 flips the preferred option of both level-1 movers (§1, Lemma W-ONLY).
  - Ξ-channel: it changes the Ξ-values of every option whose chain passes the level-0 mover that moved.
  - ISO (genome property): no option has a level-0 mover as its Ξ-target, so only the W-channel acts. NOW (run property): b_0 is the
    same at every state, so only the Ξ-channel acts.
- EXACT (box160/iso.py; every SAT model replayed under L-RED's r187/ideal.py and under the box 150 simulator, same states):
  | class (𝓛^R_d, all Ξ-data, gates, starts) | d = 2 | d = 3 | d = 4 |
  | --- | --- | --- | --- |
  | all (L-RED R197 / R202: T^R(d)) | 4 | 8 (reproduced here) | 13 |
  | ISO: W-channel only | 4 | 7 | ≥ 12 (12 SAT; 13 running) |
  | NOW: Ξ-channel only (b_0 constant on the run) | - | 6 | ≥ 10 (11 running) |
  | NOL0: no level-0 step | - | 4 = T^R(2) | 8 = T^R(3) (T ≥ 9 UNSAT 143 s) |
  | only level-0 mover 0 may move (FRZ=1) | - | 6 | (queued) |
  | ISO, only level-0 mover 0 may move | - | 5 | (queued) |
  | NOW, only level-0 mover 0 may move | - | 5 | (queued) |
  | max seg1 + tail: all | - | 6 (seg1 3, tail 3) | ≥ 10 (L-RED R204) |
  | max seg1 + tail: ISO | - | 4 = T^R(2) | ≥ 9 (≥ 10: UNKNOWN, stopped after ~90 min) |
  | max seg1 + tail: NOW | - | 4 = T^R(2) | UNKNOWN (≥ 9 stopped after ~90 min) |
  - Exact maxima are «T ≥ m SAT and T ≥ m + 1 UNSAT» (TMIN form, as L-RED's xmax.py). seg1 + tail rows: horizon T^R(d) (exact
    because every run of 𝓛^R_d has at most T^R(d) steps). The d = 3 (seg1, tail) frontier of all three classes is in §2
    (grid: box160/log/grid_d3_seg1_tail.txt, SEG="1:a,t:b" TMIN=0 at horizon 8).
  - External flips (FREE0, ISO): T_k(m) = max number of steps above level 0 of an m-level 𝓛^R ladder whose level-0 key bit an outside
    agent flips at most k times (each counted step moves a mover of level ≥ 1; SAT models replayed with the schedule forced):
    | k | 0 | 1 | 2 | 3 | 4 | 8 |
    | --- | --- | --- | --- | --- | --- | --- |
    | T_k(1) | 2 | 3 | 3 | 3 | 3 | (k 6: 3) |
    | T_k(2) | 4 | 5 | 7 | 8 | 8 | ≥ 9 (10 running) |
    | T_k(3) | ≥ 8 | ≥ 9 (10 running) | ≥ 12 (ISO witness) | | | |
- READING (what the table says about SLOT-TRADE):
  - The W-channel alone gets almost all the growth: at d = 4, ISO runs reach ≥ 12 of T^R(4) = 13 (at d = 3: 7 of 8). The Lead's pointer
    is right: the trade-off to be proved lives in the W-gate. The Ξ-coupling of level 0 is not needed for most of T^R(d) − T^R(d − 1).
  - The W-channel is a clean sub-problem (§1, Lemma W-ONLY): an ISO run is a run of the frozen (d − 1)-level genome H in which an outside
    agent flips the level-0 key bit of H at most twice. SLOT-TRADE restricted to ISO is: T_2(d − 1) ≤ T^R(d − 1) + O(d), where T_k(m) :=
    max number of steps of an m-level 𝓛^R-ladder whose bottom key bit is flipped by an outside agent at most k times (FREE0 mode).
  - Each external flip adds little, not a fresh budget: T_k(1) = 2, 3, 3, 3 (k = 0, 1, 2, ≥ 3; PROVED (lane) for every k, §1) and
    T_k(2) = 4, 5, 7, 8, 8 for k = 0..4 (EXACT), ≥ 9 at k = 8 (so it does NOT saturate at 8; it grows slowly). A fresh (m)-budget per
    flip would give ≈ (k + 1)·T^R(m).
  - The single-channel trade «seg1 + tail ≤ T^R(d − 1)» is EXACT at d = 3 for both channels, and DEAD at d = 4 for ISO: instance
    box160/out/iso_d4_st9.json (ISO, T 11, level-0 steps t7, t8, seg1 6, tail 3: seg1 + tail = 9 > T^R(3) = 8).
  - The ISO extremal runs replay: in ISO_1_d4_t12 the frozen remainder R_q is 4, 3, 2, 1, 0 over seg1 (H stuck at t4), the W-pulse
    (b_0 flips at t5 and back at t8) lifts it to 5, and the tail repeats seg1's move pattern on levels 1-3 (box160/rq.py). So in the
    W-channel the reset is a «pulse» that re-arms a stuck (d − 1)-run, and the second run is a copy, not a fresh maximum.
  - DATA (relaxation, not tight): if the two level-0 movers are an adversary (each changes once at any time, Ξ-coupling kept: FREE0
    ONCE0), d = 3 reaches ≥ 9 steps above level 0 > T^R(3) = 8 (box160/out/ext_d3_9.json). So a proof that treats level 0 as an
    arbitrary once-moving agent cannot give T^R(3); level 0's own step rule (it moves only when Ξ-unhappy and off its gate choice) matters.
- CONJECTURE FLIP-ADD (lane; the W-channel form of SLOT-TRADE): T_2(m) ≤ T^R(m) + O(m). With Lemma W-ONLY it gives SLOT-TRADE on ISO
  genomes. DATA: T_2(1) − T^R(1) = 1, T_2(2) − T^R(2) = 3 (EXACT); d = 4 values in §2.
- No proof of SLOT-TRADE, FLIP-ADD or any polynomial bound. G-N5-TIME stays OPEN.

## 1. PROVED (lane)
- Lemma W-ONLY (𝓛^R_d, d ≥ 2, ISO). For a level-0 configuration q let H_q be the genome with every level-0 mover frozen at its option
  in q (P-IDEAL-SLOT §1 notation). If b_0(q) = b_0(q′), then H_q and H_(q′) take the same step from every state.
  - Proof. (i) A-sets: under ISO no chain of an option of a level-≥ 1 mover passes a level-0 mover, so all Ξ-values, hence all A-sets of
    level-≥ 1 movers, are the same in H_q and H_(q′). Level-0 movers are frozen in both. (ii) Keys: a level-1 mover's option k has
    W-target the level-0 mover k, so its key is (gate of mover k's option in q, own gate). The two options of a level-1 mover compare as
    the two level-0 keys do, that is by b_0(q). The current options of the two level-1 movers compare by b_0(q) if they point to
    different level-0 movers, and by their own gates if they point to the same one. Every key comparison at level ≥ 2 is decided by
    comparisons at the level below (lexicographic order on W-chains), so by induction on the level every comparison at level ≥ 1 is a
    function of b_0(q) and of the states of levels ≥ 1. (iii) Same A-sets and same comparisons give the same step rule at every
    level-≥ 1 mover (P-IDEAL-SLOT §0). ∎
  - Consequence. On an ISO run, a level-0 step that does not flip b_0 is invisible above level 0. So the run above level 0 is the run of
    one frozen genome H (d − 1 levels after SHIFT) whose level-0 key bit is flipped from outside at most twice (each of the two level-0
    movers moves at most once, SEG-ONCE). Hence (ISO): T ≤ T_2(d − 1) + #{level-0 steps that move no other mover} ≤ T_2(d − 1) + 2.
  - Does NOT claim: anything without ISO; anything about b_0 itself (it is a function of the level-0 options and the four level-0 gates).
- Lemma NOW-ONCE (𝓛^R_d). If b_0(s_t) is the same for all t ∈ [a − 1, b], every level-1 mover moves at most once in [a, b].
  - Proof. As SEG-ONCE (P-IDEAL-SLOT §2): if x moves at t1 < t2 in [a, b] and not in between, then s_(t1)(x) = KP_(s_(t1))(x) and
    s_(t2)(x) = KP_(s_(t2))(x) ≠ s_(t1)(x). By (ii) above (no ISO needed for keys) KP of a level-1 mover is the option index b_0 decides,
    the same at s_(t1) and s_(t2). Contradiction. ∎
  - Consequence: on a NOW run, the four movers of levels 0 and 1 move at most once each.
- Lemma FLIP-1 (one level, any k). An ISO genome of 𝓛^R_2 whose level-0 key bit is flipped from outside any number of times makes at most
  3 steps above level 0, so T_k(1) ≤ 3 for every k; T_0(1) = 2.
  - Proof. Let u, v be the two level-1 movers. By ISO every Ξ-target of their options lies in {X, u, v}, and by acyclicity u and v do
    not both have an option pointing to the other. Say no option of v points to u, so both options of v point to X.
    - v: its two Ξ-values never change, so the strictly better option is fixed. v moves only out of the worse option and onto the better
      one (a degree-2 mover that moves takes the other option, which lies in its A-set, so it is strictly better). After that move its
      A-set is a singleton forever. So v moves at most once.
    - u: its two Ξ-values depend only on v's option, so its strictly better option changes at most once. If u moves at t1 < t2, it takes
      the better option under s_(t1−1) at t1 and the better option under s_(t2−1) at t2, and these differ. So u moves at most twice.
    - The outside flips do not touch any Ξ-value (ISO). Every counted step moves u or v, so there are at most 3. ∎
  - EXACT check: iso.py FREE0 KF = 0, 1, 2, 6 at d = 2: max 2, 3, 3, 3.
  - Does NOT claim: anything for two or more levels.

## 2. Table rows still running at the push
- d = 3 (seg1, tail) frontier (rows seg1 ≥ a, columns tail ≥ b, S = SAT, U = UNSAT, horizon 8):
  - all: a = 0: tail ≤ 4; a = 1, 2, 3: tail ≤ 3; a = 4: tail ≤ 1. Max seg1 + tail 6 at (3, 3).
  - ISO: the maximal SAT corners are (0, 3), (2, 2), (3, 1), (4, 0). Max seg1 + tail 4.
  - NOW: (0, 4), (1, 3), (2, 2), (3, 1), (4, 0). Max seg1 + tail 4.
- Running or queued at the push (box160/queue.txt; logs in box160/log/; results go into the next push):
  - ISO d 4 T ≥ 13; NOW d 4 T ≥ 11; ISO d 4 seg1 + tail ≥ 10; NOW d 4 seg1 + tail ≥ 9;
  - T_1(3), T_2(3) (run_kf.sh 4 …); ISO / NOW with one level-0 mover at d 4; NOL0 d 4; T_8(2); the adversarial-level-0 relaxation
    (FREE0 ONCE0) at d 3, T ≥ 10.

## 3. Files
- experiments/new/box160/: iso.py (driver), xcnf_free0.py (copy of L-RED's r200/xcnf.py @ 5f3e89e1 with one added line: FREE0),
  run_iso.sh / run_kf.sh / run_env.sh / queue.sh (resumable), trace.py, flips.py, jumpkind.py, rq.py, ext/ (L-RED genomes),
  out/ (witnesses), log/ (solver logs). Engine provenance: claude/l-red 5f3e89e1 experiments/red/{r178,r187,r199,r200} (read-only).
- Other DATA (not to sign): per-level flip counts (flips.py): F_l − F_(l−1) reaches 8 (dd_d5_F14), so no «each level adds O(1) flips»
  shortcut. Jumps by kind (jumpkind.py, 137 level-0 steps): jumps up to 16 with a b_0 flip (dc_d12) and up to 10 without (uc_d10), so
  neither channel has a per-step jump bound.

