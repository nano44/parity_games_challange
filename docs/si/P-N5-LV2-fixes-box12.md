# P-N5-LV2 fixes (box 12 packet; repairs only)
L-SI successor 8 (Opus 5.5; D14, D15, D18, L37, L40). Written 2026-10-25 17:58Z (date -u), at the Lead's request (17:35Z, 17:55Z; Lead's stamps).
- Object: docs/si/P-N5-LV2-box12.md, sha1 3b23a41f… (L-SI successor 7; pinned trunk 283bcb6). FROZEN, not edited.
- Repairs only. This file adds no new statement and no new proof.
- Sources, all on trunk (19d707b4); file sha1s by `git show <commit>:<path> | sha1sum`:
  - REFEREE: docs/referee/R-N5-LV2.md, report at referee b454ca3 (file sha1 916629f8…; successor 9), Addendum at referee 46a8030 (file sha1
    3c351912…; 16:29Z), §C at referee ed8bc207 (file sha1 103e8c85…; successor 10);
  - REFEREE-2 successor 10: docs/referee-2/R2-N5-LV2.md, report at referee-2 a551deb (file sha1 5d66ad3f…). Its §C is not needed: the
    Lead relayed REFEREE's §C as closing the comparison (17:55Z).
- Items: LV2-N1, LV2-N2 (REFEREE); N-LV2-1, N-LV2-2, N-LV2-3 (REFEREE-2); the REFEREE Addendum; the §C's new data (beta2_n11).
- REFEREE's §C: identical verdicts, joint gap map EMPTY; N-LV2-1 accepted as a fixes-file line; N-LV2-2 and LV2-N1 compatible.

## 0. Joint verdicts
- SIGN, by both referees (Opus 5.5, D15): §1 STALE-GATE; §2 EV-G; §3 ENT-X_{−1}; §4 LV-PL′; §5 SAND; §6 FLAT-ALL_{−1}^{none};
  §7 LV-NONE; §8 SCOPE-FB (CONDITIONAL on (C-ENT), (C-LV), (C-PKT), as stated).
- §9 data and §10: not signed (as briefed). No gap in either report.

## 1. Statuses (LV2-N2; N-LV2-1)
- P-N5-LV is signed by both referees and has LANDED as RESULTS R41 (trunk d0cc0ab; CHECKER C50). Its CN-LAST condition is discharged by R38 (f). So the
  conditions "P-N5-LV §1-§4" in §3, §4, §6, §7 are signed results; (C-LV) holds.
- P-N5-ENT is RESULTS R40 (landed, CHECKER C49), unconditional given R36. So (C-ENT) holds.
- §0 / §2: EV-G's premise FREE-FREEZE is R37 (c), CONDITIONAL on (P); (P) is RESULTS R36. Name R36 next to R37 (c). The "none" in the
  condition column holds given R36 (landed).

## 2. §3 ENT-X_{−1}, step (c): the P-set identity (LV2-N1; N-LV2-2)
- Before "ρ ∩ P(Ξ_k q) = ∅ (the play is simple before its cycle)" and (P2) along ρ, cite CYC-EV (at L = −1, proved in (e)): q lies on
  the pre-c path of z's play (LV2-N1).
- Read "Ξ_k(z) = ρ ⊕ Ξ_k(q)" as the P-set identity P(Ξ_k z) ∩ H = (ρ ∩ H) ⊔ P(Ξ_k q) (N-LV2-2). This holds even when q lies on c's
  cycle (cycle vertices other than c rank below c); only the P-sets are used. The same wording is in the signed EV (R37 (f)).

## 3. §9 DATA (REFEREE Addendum; N-LV2-3)
- §9's "the level −1 block and the none part are empty in all data" is no longer true. Read:
  - none part (THR, r = −1, in scope): 351,417 (REFEREE climbs), 237,033 (REFEREE-2 climbs), 131,558 (L-SI succ. 8 climb 1301);
    FLAT-ALL_{−1}^{none} and SAND held at all of them (REFEREE: 351,417 / 1,000,826 checks).
  - level −1 block (M = −1, r ≥ 0): 645 fallbacks in REFEREE-2's climbs, the first in any data (no witness saved).
  - Up to both reports, no scope run had two of either.
- REFEREE's §C (new data after both reports): L-RED 16's experiments/red/so/instances/beta2_n11.pg (sha1 bdea2a23) has ONE scope run with
  TWO in-scope THR fallbacks with r = −1, both with M = −1, from the canonical start. It is confirmed on REFEREE's engine, on L-RED's,
  and on L-SI scopefb.py (Lead re-run).
  - FLAT-ALL_{−1}^{none} (i)-(iv) held at both, with 0 failures of SAND, EV-G, STALE-GATE.
  - So LV-NONE's counting step (N = 2 ≤ n·n_E + 1) is exercised. ENT-X_{−1} and LV-PL′'s block (r ≥ 0) still have no saved witness.
- The candidate CONJECTURE (REFEREE-2 N-LV2-3; L-SI NONE-LAST, docs/si/N5-RISE-box13.md §4), "an in-scope THR fallback with M = −1 is the
  last fallback of its scope run", is FALSE on beta2_n11 (docs/si/DEAD.md, box 13). It was never part of the packet.
