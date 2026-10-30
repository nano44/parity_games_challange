# R2-N5-SRC-C: §C, joint gap map for P-N5-SRC (REFEREE-2 successor 24, Opus 5.5, D15)
- Inputs:
  - mine: docs/referee-2/R2-N5-SRC.md, claude/referee-2 e8c1b62d, pushed before I opened REFEREE's report;
  - REFEREE's: docs/referee/R-N5-SRC.md, claude/referee 81f6b89c, 125 lines, opened after my push (Lead 22:56Z).
- Packet: l-red 0521fb82, sha1 3caae56e. Line 3101a0c0.

## C.1 Item by item
| § | item | REFEREE | REFEREE-2 | joint |
| --- | --- | --- | --- | --- |
| 1 | (R1), (R2), definitions | CHECKED | checked | ✓ |
| 2 | PLAY-CAUSE^S | SIGNED | SIGNED | SIGNED by both |
| 3 | (S_j)/(X_j), C1-C7 | SIGNED, G-SRC-1 closed (four-sub-case split) | SIGNED, G-SRC-1 closed (Lemma ONE-STEP) | SIGNED by both; G-SRC-1 found independently by both, closed (C.2) |
| 4 | TAIL (T0), (T1) | SIGNED | SIGNED | SIGNED by both |
| 5 | SRC-SETTLE, SRC-COUNT, EQUIVALENCE | SIGNED | SIGNED | SIGNED by both |
| 6-7 | F1, F2, DATA | not signed | not signed | — |

## C.2 G-SRC-1: my verdict on REFEREE's four-sub-case argument (R-N5-SRC §3)
- Same gap, found independently. REFEREE's statement of it matches mine:
  - «Its play from y is y, then b's (σ_k, τ)-path» fails when y ≠ c lies on c's σ_k-cycle;
  - Case 2b has the same pattern with ρ′ = σ_(k+1)[y ↦ a] and «y on c's σ_(k+1)-cycle».
- The sub-cases checked.
  - (i) y is not on the cycle: the ρ-play ends in c's unchanged cycle, as written. ✓
  - (ii) y is on the cycle and P := P(W_k(b)) = ∅.
    - The new cycle consists of c's arc from c to y and b's path to c. Every vertex of the arc is less relevant than c, which is the
      top of c's cycle, and no vertex of b's path is more relevant than c, since P = ∅. So the top is c, and
      val(ρ, τ)(y) = y ⊕ W_k(b). ✓
  - (iii) m := the most relevant vertex of P, m even.
    - m is the top of the new cycle: it is above c and above every arc vertex.
    - reward(m) = p′(m) > p′(c) ≥ reward(c), so val(ρ, τ)(y) ▷ W_k(y). That contradicts ARENA-MAX at k − 1 → k (ρ ∈ H_(k−1)). ✓
  - (iv) m odd.
    - W_k(y) = (c, ∅, ℓ_y), because y's σ_k-path is c's arc from y to c.
    - y ⊕ W_k(b) has path set P. y is not added, since y is below c. The top of the symmetric difference is the odd m, so
      y ⊕ W_k(b) ◁ W_k(y). ✓
    - REFEREE's extra remark is also right: in Case 2, y ⊕ W_k(b) = W_(k+1)(y) ⊵ W_k(y) by W-MON, so (iv) is excluded there.
  - Case 2b by symmetry (σ_(k+1), a, ARENA-MAX at k → k + 1): ✓, with the same four cases at state k + 1.
- One unstated step, a precision and not a gap: «the new cycle» needs b's path to be disjoint from c's arc from c to y.
  - It is: if b's path entered that arc, it would reach y before c, against «b's path avoids y».
  - My ONE-STEP (β) states this step.
- Equivalence with ONE-STEP. (ii) is my z* = c; (iii) is my z* even; (iv) is my z* odd. REFEREE's split by P = ∅ or by the parity of
  max P equals my split by the top z*, because z* = c iff P = ∅, and otherwise z* = max P.
- **Verdict on REFEREE's G-SRC-1 closing argument: SIGNED (Opus 5.5, D15).** No gap. No FALSE step.
- DATA reconciles.
  - REFEREE's CYC counts Case-2 switches with y on c's cycle: 3, all of type (ii).
  - My OS_newtop counts every z ∈ H_t(y), not only switches: 4, all on ret22_n40 at non-chosen z, type (iv).
  - Both find (iii) = 0. The two counters count different populations, so this is not a disagreement.
- Status under L41 once REFEREE's explicit verdict on my ONE-STEP arrives (the Lead asked for it at 22:56Z):
  - G-SRC-1 is closed by two independent repairs, each signed by the other referee;
  - joint gap map: EMPTY after closure; G-SRC-1 is recorded as found and CLOSED.
  - Until that verdict, it stands: REFEREE's repair signed by both; mine signed by me.

## C.3 Line (3101a0c0): union of both reports
| item | REFEREE | REFEREE-2 | joint |
| --- | --- | --- | --- |
| \|F\| undefined | SRC-L1 REQUIRED | SRC-L1 REQUIRED | REQUIRED |
| t free in «H_t» (R57 gloss) | SRC-L2 REQUIRED | SRC-L2 REQUIRED (also «σ_new») | REQUIRED |
| cite the G-SRC-1 repair in the RUN-SETTLE proof note | SRC-L3 precision | SRC-L3 REQUIRED | Lead decides. My reason for REQUIRED: the note says «signed» of an induction whose written Case 2 / 2b step is false on reachable states (ret22_n40). The rule «gaps listed» asks the line to point at the repair. Either repair, or both, can be cited |
| «n := \|V\|», V unnamed | SRC-L3 precision | — | precision; TARGET.md l. 8 binds n = \|V\| fleet-wide, so optional |
| «not events» → «not source events» | — | N-1 precision | precision |
- Same for SETTLE: both reports say G-SRC-1 sits in [SET] §5. SETTLE line L-4 should carry the same citation, which the Lead has already
  planned. A [SET] fixes entry should record the split (REFEREE's NEEDS).

## C.4 Corrections and differences
- Longest source block: REFEREE 63 (MAXN 100, so it skips n > 100); mine 67 (gate_K64_n581, n 581) = the lane's. A run-set difference.
- Correction (my side): my predecessor's SETTLE report (§2.5) and §C missed G-SRC-1. Both referees missed it in SETTLE (REFEREE's
  FINDING 2 says the same).

## Verdict (Opus 5.5, D15)
- Every SRC item to sign is SIGNED by both referees.
- G-SRC-1 was found by both and is CLOSED. I SIGN REFEREE's four-sub-case argument. REFEREE's verdict on my ONE-STEP is pending.
- Line: SRC-L1 and SRC-L2 are REQUIRED by both. SRC-L3 is REQUIRED by me and precision by REFEREE: the Lead decides.
