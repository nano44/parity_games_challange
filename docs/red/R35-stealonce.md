# R35: (STOLEN-PERM), (STAYS-MET), (NO-REFIRE at σ) and (STEAL-ONCE*) are FALSE on A_DTL under the stable order datum; the run is complete (L-RED box 8, 19:20Z by date -u; produced on Opus 5.5)
Status: DATA, unrefereed. Targets: L-ALG's chain (STOLEN-PERM) ⇒ (STAYS-MET) ⇒ (NO-REFIRE at σ) ⇒ (STEAL-ONCE*)
(docs/alg/GAP-A-M.md §23a-§23c, l-alg 9b621aa2). (STEAL-ONCE*) is a conjunct of the signed refinement
(FALL) ⇐ (STEAL-ONCE*) ∧ (FIRED-R) (RESULTS R10, R11). Lead box-8 plan item (1).

## Instance
experiments/red/carry/instances/stealonce_viol_n76.pg (n = 76, sha1 32c2da0b6ff0ad87b3f7d725e351356bd8e14172).
It is stealer_viol_n76 (R34, sha1 714ecc0f) with two edges changed:
- vertex 3 (Odd-owned, priority 2): edge 3→31 replaced by 3→64;
- vertex 20 (Even-owned, priority 41): edge 20→31 added.
How it was found: a hand edit (3→64, so that the stealing vertex 3 depends on vertex 64 of region 66; file r64) raised the
graded near-miss of root/permgap.py from 4 to 8. Then a scan of every one-edge change at vertices 3, 20, 25 and 64 of r64
found 20→31 (hit 14 in permgap) and 20→33 (hit 1).

## Evidence (re-run on the pinned file)
- L-ALG experiments/alg/dtl_rootmono.py UNMODIFIED (l-alg 9b621aa2), RM_EXCL=1 RM_PREF=1 RM_DV=0:
  - DTL_ORDER=stable:
    - "STOLEN-PERM (the stealing vertices stay in the prefix): FAILS" 7, holds 12;
    - "NO-REFIRE after a relevant steal: REFIRES later | prefix later unmeets t" 7, "never refires | stays met" 12;
    - "RELEVANT STEALS per (context, round, top, tangle): max 2";
    - no INCOMPLETE line.
  - DTL_ORDER=oink: STOLEN-PERM holds 1; NO-REFIRE "never refires | stays met" 1; RELEVANT STEALS max 1; no INCOMPLETE.
- L-ALG experiments/alg/dtl_stealtrace.py UNMODIFIED, RM_EXCL=1 RM_PREF=1 RM_LIGHT=1 RM_DV=0:
  - stable: "STEAL-ONCE* VIOLATION ... phase 1 ctx |R| 76 step (round 4, top 18) tangle 7: 2 relevant steals";
    STAYS-MET FAILS 7 / holds 12; NO-REFIRE FAILS 7 / holds 12; STEALER-MONO FAILS 7 / holds 12;
  - oink: everything holds (1 relevant steal).
- Pinned Oink 8fbf0a7 `--dtl --no-single --no-wcwc --no-loops -v`: 1 dominion, 50 tangles, 7 iterations, "solution verified
  (33 strategies)". Pinned in experiments/red/check.sh (dtl_flipflop n=76 tangles=50 dominions=1 iterations=7).
- Second hit (not pinned; same shape): r64 + 20→33 (sha1 011284ed), stable: STOLEN-PERM FAILS 1, NO-REFIRE REFIRES 1,
  RELEVANT STEALS max 1; pinned Oink verified (44 tangles, 7 iterations).

## Mechanism (stable order, phase 1, depth-0 context |R| = 76; file ids; root/steptrace.py)
Step σ = (round 4, top 18). Tangle 7 = {3, 7, 15}.
1. Search 2: region 18 fires tangle 7 (region {3, 7, 15, 16, 17, 18, 25, 61}).
2. Search 3: region 66 (higher) fires tangle 9 and holds 64. Vertex 3 (owned by the searching player) joins region 66 via its
   edge 3→64. Tangle 7 is met but not contained by P(σ⁺): a relevant steal, W = {3}.
3. Search 4: a new top 68 (above 66) fires tangle 6 and takes most of region 66, but not 64. Tangle 9 is relevantly stolen at
   step (4, 66), so region 66 shrinks to {65, 66}. Now 64 lies in no region above 18, so 3 has no edge into P(σ) and leaves it:
   (STOLEN-PERM) fails. Tangle 7 is no longer met at σ (STAYS-MET fails) and fires again at σ (NO-REFIRE fails).
4. Search 6: region 66 fires a new tangle 34 and is {3, 55, 63, 64, 65, 66}. Vertex 3 enters P(σ) again, so tangle 7 is relevantly
   stolen a second time at the same (context, round, top, tangle): (STEAL-ONCE*) fails with 2.
This is L-ALG's case A one level up (GAP-A-M §23c): the stealing vertex depends, through an edge, on a vertex of a region whose
fired tangle is later relevantly stolen by a higher new top. It is not DE19's upward migration: 64 does not move up.

## Reading (L-RED)
- Under the binding Lead reading L22/L26 the frozen DTL statement covers every order datum, so a failure under the stable
  datum refutes (STOLEN-PERM), (STAYS-MET), (NO-REFIRE at σ) and (STEAL-ONCE*) as statements about A_DTL. The Oink datum
  holds on this instance.
- The §23b implications are not refuted: every premise fails here together with its conclusion.
- Not claimed: anything about (FALL), (FIRED-R), (CTX⁺) or GAP-A itself. The counts are 2 steals per triple and 7 refires,
  so no super-polynomial family. The run is complete and verified.
