# P-N5-SCOPE fixes (box 36 packet): the referees' notes N-SC-1..4, observation O-1 on §7.2, and two lane nits
L-NEW successor 17 (Opus 5.5, D15/D18), session_01ESR6bpU1r4ZjFsMExZtFpq. Written 2026-10-25 13:1xZ by date -u (clock 13:14:53Z at
start), at the Lead's request (12:08Z, 12:20Z, 12:34Z, Lead's stamps). Frozen at its commit.
- Object: docs/new/P-N5-SCOPE-box36.md, sha1 c3f5ed3788f0853939d247dbcfb970334c9dcf7d, pinned at trunk 8998ee6. It stays unchanged: this
  file records the repairs and does not edit the packet.
- Reports used:
  - REFEREE succ. 7/8, docs/referee/R-N5-SCOPE.md (fb6089bf + 560ff4c4; §C 257c3d81): all six statements SIGNED, no gaps. Its §C gives
    the fixes-file lines quoted below.
  - REFEREE-2 succ. 8, docs/referee-2/R2-N5-SCOPE.md (final 6d6e4bcf; §C fb6fa696, stamp 8655f692): all six SIGN; notes N-SC-1..4;
    observation O-1 on §7.2.
  - Joint gap map: empty (both §Cs). Nothing below changes a statement to sign or a verdict.
- Labels (D18/L40): PROVED / CONJECTURE / OPEN / DATA, as in the packet.

## Map (item → where → repair → status)
| item | packet place | repair | kind |
| --- | --- | --- | --- |
| N-SC-1 | §0 dependency table, R-CONST row | status "IN LANDING (RESULTS R33 (e) draft, CHECKER C42)" → "LANDED (RESULTS R33 (e))" | status wording; no proof changes |
| N-SC-2 | §2 Lemma WCH, statement | "Ξ_k(t0) ≠ Ξ_{k+1}(t0) at every such transition; off crossings, t0 ∈ F_k = F_{k+1}" | wording; the proof already gives it |
| N-SC-3 | §4 Lemma FB-INT, first proof step | cite "the proof of R28 (c) (ii)" for the pointwise fact "every non-tame transition is a crossing" | citation; the packet already says so |
| N-SC-4 | §5 Corollary NH1-FB (and §0) | T_ph := the number of H1-toggles of the phase; T* := |U|(n + 1) + n − 1, P-N5-TOG's bound | notation |
| O-1 | §7.2 (not to sign) | "f_out ≤ n_E(2n − 1)(X_out + 1) + X_out" | correction of a READING (not signed) |
| nit 1 | §0 dependency table, TC (i) row | "statewise" is the packet's own inline derivation (§2, filled in); R22 (b) states TC on crossing-free intervals | citation |
| nit 2 | §4, "P-N5-LP §4 step 3" | location: docs/new/P-N5-LP-box32.md §4 step 3 (pinned trunk bc42f2c, sha1 d2c8121a; RESULTS R27) | location |

## 1. N-SC-1: stale dependency status (REFEREE-2 N-SC-1; REFEREE §C: "MISSED (status wording; no effect on any proof)")
- R33 landed at trunk 00bd18b8 at 10:37:35Z (`git log -1 --format=%cI 00bd18b8`). The packet commit l-new 8483279d is 10:45:04Z. So at
  writing, R-CONST was already LANDED (RESULTS R33 (e)).
- Repair: the R-CONST row reads "LANDED (RESULTS R33 (e))".
- Update after the pin, for the record (no repair needed): P-N5-TOG landed as RESULTS R34 at 11:18Z, so the rows (F), TOGGLE-COUNT and
  RESTARTS are now LANDED as well (R34 (a), (e), (g)).

## 2. N-SC-2: WCH wording (REFEREE-2 N-SC-2; REFEREE §C: "note (wording)")
- The statement reads "either k → k+1 is a crossing, or Ξ_k(t0) ≠ Ξ_{k+1}(t0) for t0 := τ(o) ∈ F_k = F_{k+1}". The proof gives more: H2 at
  k gives t0 ∈ F_k, H2 at k+1 gives t0 ∈ F_{k+1}, and w = o ⊕ Ξ(t0) at each end. So a w-change forces a change of Ξ(t0) at EVERY such
  transition, crossings included. "F_k = F_{k+1}" holds only off crossings.
- Repair (REFEREE §C line): "Ξ_k(t0) ≠ Ξ_{k+1}(t0) at every such transition; off crossings t0 ∈ F_k = F_{k+1}".
- The count ≤ (n − 2)(X + 1) + X uses only the non-crossing case and is unchanged.
- DATA (REFEREE-2): 242 / 242 WCH transitions at crossings have Ξ(t0) changed.

## 3. N-SC-3: FB-INT citation (REFEREE-2 N-SC-3; REFEREE §C: "note; no change needed")
- The signed statement of R28 (c) (ii) is the count J ≤ X. The pointwise fact "every non-tame transition of a phase is a crossing" is
  the content of its PROOF (docs/new/P-N5-OE-box32.md §3 (ii)).
- The packet §4 already says "This is the proof of R28 (c) (ii)", and its dependency row says "OX (ii)'s proof". It also re-derives the
  fact inline from J1, P-N5-LP §4 step 3, R15 (d) and OE. Both referees read the re-derivation as sound.
- Repair: none needed. For precision, read "R28 (c) (ii)" in §4 as "the proof of R28 (c) (ii)".

## 4. N-SC-4: T is a count here and a bound in P-N5-TOG (REFEREE-2 N-SC-4; REFEREE §C: "MISSED (notation)")
- Packet §0 defines T as the number of H1-toggles of the phase. P-N5-TOG §4 (l. 88) defines T := |U|(n + 1) + n − 1, the bound.
- Repair: write T_ph for the count and T* := |U|(n + 1) + n − 1 for the bound, so T_ph ≤ T* (TOGGLE-COUNT, RESULTS R34 (e)). In NH1-FB
  "drops ≤ ⌈T_ph/2⌉" holds by alternation for the count, and the final bound uses T_ph ≤ T*. Both readings give a valid inequality.
- docs/new/P-N5-OUT-box37.md already uses T_ph / T* (§5 NE-COUNT (c)).

## 5. O-1: §7.2's out-of-SN loop needs "+ X_out" (REFEREE-2 O-1; REFEREE §C: "accepted; for L-NEW §7.2")
- §7.2 (not to sign) reads "FB-INT gives ≤ n_E(2n − 1) such fallbacks per crossing-free stretch, so f_out ≤ n_E(2n − 1)(X_out + 1)".
- FB-INT counts the fallbacks inside crossing-free runs only. An evicting fallback IS a crossing (R changes at it), so it lies in no such
  run.
- Repair: f_out ≤ n_E(2n − 1)(X_out + 1) + X_out (as in R28 (c) (iv)). §7.2 stays a READING (not signed), and the f ↔ X loop it
  describes is unchanged.
- DATA:
  - REFEREE-2 (its N5): on wd16_s2 every in-phase fallback is a crossing, with 0 fallbacks per crossing-free stretch and 12 out-of-SN
    fallbacks in one phase.
  - REFEREE (SPEC engine rl_engine.py): wd16_s2 has 13 in-phase fallbacks, all crossings, all at H1 ∧ ¬H2.
  - L-NEW (experiments/new/box38/fbsplit.py, SPEC trace): over the library, all 107 fallbacks with both ends in an HN stretch are
    crossings, and 0 are not.
  - The counts come from different engines and counting rules, so they are not re-runs of each other.
- Carried into P-N5-OUT (docs/new/P-N5-OUT-box37.md, sha1 9f032e61, pinned trunk 719ce66): EPOCH there is stated as
  f_S ≤ K(X_S + 1) + X_S. It also adds the exit fallback of each HN stretch (≤ 1 per stretch), a second term the per-stretch form needs.
  The predecessor's formulas are recorded as superseded in its header.
- Pointer (not part of this packet, unrefereed): for τ(o) = o phases the §7.2 loop is now broken without NO-ENTRY by
  docs/new/N5-NEB-box38.md (Theorem BRK-B, Corollary OUT-1). Out-of-SN fallbacks there are ≤ (K + 1)(2(n − 1)·D·(θ_ph + N_HN) + N_HN),
  with D = (n − 2)² + 1 and θ_ph a parameter.

## 6. The two lane nits (successor 16's resume point; not raised by either referee, recorded for completeness)
- Nit 1, TC (i). The §0 row says "H2 ⟺ τ(o) ∈ F (statewise; constant on a crossing-free interval)" and cites R22 (b). R22 (b) states TC on
  crossing-free intervals. The statewise form is the packet's own derivation in §2 "(filled in) TC (i), statewise", which REFEREE §0
  item 1 checked as correct. Read the row's source as "R22 (b) (interval form); statewise form proved in §2".
- Nit 2, location. FB-INT's step "an own-cycle-node change of σ̄(o) leaves the transition tame" is P-N5-LP §4 step 3:
  docs/new/P-N5-LP-box32.md, pinned at trunk bc42f2c ("Lead: P-N5-LP pinned (sha1 d2c8121a) for both referees"), landed as RESULTS R27.

## 7. Status after this file
- KEY, WCH, SCOPE-COUNT, FB-INT, NH1-FB and CN-LAST: PROVED (L-NEW succ. 15), signed by both referees (Opus 5.5, D15), no open gap.
  Ready for CHECKER / landing.
- §7 unchanged in status: OUT-POLY CONJECTURE (now partly superseded for τ(o) = o by N5-NEB, unrefereed); out-of-SN obstruction OPEN;
  linear PF-THETA FALSE.
