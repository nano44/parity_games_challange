# P-N5-ENT fixes (box 11 packet; repairs only)
L-SI successor 7 (Opus 5.5; D14, D15, D18, L37, L40). Written 2026-10-25 ~15:15Z (date -u), at the Lead's request (14:33Z, 14:46Z, 15:04Z;
Lead's stamps).
- Object: docs/si/P-N5-ENT-box11.md, sha1 4fd22be79f7050a7f466288c76eea8bfe2f669d0 (L-SI successor 6). FROZEN, not edited.
- Repairs only. This file adds no new statement and no new proof.
- Sources, all on trunk:
  - REFEREE successor 8: docs/referee/R-N5-ENT.md, report at referee 55a3f6f and §C at referee d6b8aef9;
  - REFEREE-2 successor 9: docs/referee-2/R2-N5-ENT.md, report at referee-2 b7df84b8 and §C at referee-2 f33884e6.
- One file covers both reports and both §Cs (Lead 14:46Z). No fixes2 file is needed.

## 0. Joint verdicts (as both §Cs record them; quoted in substance)
- SIGN, no (P), by both referees (Opus 5.5, D15):
  - §1 Lemma FZ, Lemma BF; §2 Lemma RB, Corollary WALK (a)-(c); §3 Lemma CYC-EV, Proposition TEV-FB;
  - and (REFEREE-2) the §0 facts (Σ1)-(Σ6), which REFEREE checked in its §1.
- SIGN CONDITIONAL ON (P), by both: §4 Theorem ENT-X; §5 Corollaries NJB-A, D1, PL-S″.
- §6: not signed (it was marked NOT TO SIGN).
- No gap in either report; the joint gap map is empty.

## 1. Status line (the condition (P), and the related landings)
- RESULTS R36 (P-N5-P1, Lemma P1) has LANDED. It is the premise (P).
- RESULTS R37 (P-N5-RL) has LANDED. It records EV, EV+ and TEV-RED′ as unconditional given R36.
- CYC-EV lands with P-N5-ENT, not under R37, per the Lead ruling of 12:58Z (R37's object paragraph).
- R36 lift: YES (REFEREE §C, referee d6b8aef9).
  - ENT-X, NJB-A, D1 and PL-S″ use (P) only through EV+ ⇐ FREE-FREEZE ⇐ BL (c), i.e. (P) on the one-player game G_τ[F_k].
  - R36 (d) states P1 exactly for G[X], G_τ and G_τ[F_k].
  - So, with R36 and R37 landed, all four are PROVED without condition.
- REFEREE-2's §C agrees: both reports note that with P1 landed §4-§5 become unconditional.
- Labels after this line:
  - §1-§3 PROVED (no (P));
  - §4-§5 PROVED (via R36).
  - No running-time bound is added: G-N5-TIME stays OPEN (packet §6: the straddling interval of NJB; level −1 fallbacks; out-of-scope
    fallbacks).

## 2. N-ENT-1 (REFEREE-2 §7; REFEREE §1-§2; ACCEPTED in both §Cs): CYC-EV and TEV-FB need only M_k ≤ L
- Add to §3, after the setting line "M_k = L is NOT assumed: (Σ4) suffices":
  - "Lemma CYC-EV and Proposition TEV-FB need only (Σ) and a rise. M_k = L is not used. Their proofs use M_k ≤ L ((Σ4), CLS2) only
    inside Lemma RB."
  - "So this CYC-EV has the conclusion of the CYC-EV in docs/si/P-N5-RL-fixes-box10.md (signed in the R-N5-RL / R2-N5-RL addenda) under a
    WEAKER hypothesis, and implies it."
  - "RB is the step that needs k to be a fallback state, through (Σ4) (REFEREE §1)."
- For the RESULTS entry (REFEREE-2's request): say that the two signed CYC-EV statements are one result, the ENT form being the more
  general one, so that they are not read as different results.

## 3. N-ENT-2 (REFEREE-2 §7; ACCEPTED in both §Cs): "vacuous" applies only to CYC-EV, TEV-FB and ENT-X
- Replace in §7 ("Thin spots"):
  - "No (Σ)-pair in any data has a rise. So CYC-EV, TEV-FB, ENT-X and its corollaries have vacuous hypotheses everywhere, and they rest on
    the proofs."
  - with: "No (Σ)-pair in any data has a rise. So CYC-EV, TEV-FB and ENT-X have vacuous hypotheses in data and rest on their proofs. The
    corollaries' hypotheses do occur:
    - NJB-A's hypothesis (a block interval with r > M throughout) occurs 698 / 601 / 701 times (REFEREE-2, own / random / spec library)
      and at 654 (Σ)-pairs (REFEREE), every interval clean;
    - D1's and PL-S″'s objects (blocks) occur 287 / 273 / 290 times (REFEREE-2).
    Only the dirty case, i.e. the ENT setting, is unreached."
- REFEREE's §4 thin spot repeated the packet's wording. REFEREE corrected it in §C ("vacuous only for CYC-EV, TEV-FB and ENT-X").

## 4. N-ENT-3 (REFEREE-2 §0 note; ACCEPTED in both §Cs): §0's status of P-N5-RL is stale
- Replace in §0, "IN REVIEW, used: P-N5-RL …", the lines "REFEREE-2's report is pending (its items go to P-N5-RL-fixes2-box10.md)" and the
  status of EV / EV+ with:
  - "P-N5-RL has LANDED as RESULTS R37 (CHECKER C46). Sources: REFEREE R-N5-RL; REFEREE-2 R2-N5-RL 30dc5f54, §C 88571b03, Addendum A
    db9d66a8; fixes files ac027458 and b3e3cd93, and the addendum 5c29d93d."
  - "R37 (f) signs EV and EV+, unconditional given R36."
- Likewise, §0's "(P) … discharged by P-N5-P1 … unrefereed" now reads "discharged by RESULTS R36 (Lemma P1; CHECKER C45)".

## 5. Other referee lines, recorded (no change to the packet's text)
- REFEREE §3: "There is no circularity: TEV-FB does not use EV+ or any (P) item." REFEREE-2 §5 makes the same point ("(P) enters only
  through EV+. §1-§3 are unconditional").
- REFEREE §1-§3, disclosure: §1-§3 had been seen before as the RL fixes source (R-N5-RL Addendum A2, d104aac2). The packet's §1-§2 differ
  from that text only in rewording (diffed); TEV-FB, §4 and §5 were checked for the first time. REFEREE-2 re-checked the ENT text on its
  own and diffed the two CYC-EV statements (N-ENT-1).
- REFEREE §2: TEV-FB is TEV at the fallback state k. L-RED's tevlast_cex_n40 (a failure at an S4a state) is consistent with it: its gate
  (15, 21) of level 33 > L at t = 7 is exactly what (Σ4) forbids at k.
- DATA, both referees, independent engines (DATA, not proof):
  - tev_cex_n40 counts agree exactly: 15 (Σ)-pairs, FZ 414, BF 19, RB 16, WALK 19.
  - The packet's single "RB / BF" column counts RB checks.
  - REFEREE-2 only (DATA; it suggests an unconditional route to "(Σ) + rise is empty", not claimed here):
    - every rise after a fallback with r > L (62 library, 26,665 climb) is followed by NO further fallback of its scope run;
    - the run ends by r ≤ L 38 times, by stop 13, by phase end 6, by H2 failing 5 (Lead relay 14:33Z).

