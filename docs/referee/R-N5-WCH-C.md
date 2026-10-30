# R-N5-WCH-C: §C cross-map for P-N5-WCH (REFEREE 19 vs REFEREE-2 22)
Referee: REFEREE (successor 19), Opus 5.5 (D15). Lead brief 2026-10-30 10:32Z; written 10:32Z-10:36Z by date -u. Every verdict "(Opus 5.5, D15)".
- My report: docs/referee/R-N5-WCH.md at claude/referee d71d6e55, pushed BEFORE I opened REFEREE-2's.
- REFEREE-2's report: docs/referee-2/R2-N5-WCH.md at claude/referee-2 24f32388 (sha1 185416fe…, 207 lines), opened 10:32Z after the Lead's word.
- Fixes and corrected line W1: not yet pushed. The word-diff goes in a later section.

## 1. Joint gap map
| item | REFEREE 19 | REFEREE-2 22 | joint |
| --- | --- | --- | --- |
| Fact REW, LEX, COMMON PREFIX | SIGNED | SIGNED | SIGNED by both |
| Lemma TIE | SIGNED (WCH-N2 wording) | SIGNED (N-1 wording) | SIGNED by both |
| NEW-BOUND, RET-WCH | SIGNED | SIGNED | SIGNED by both |
| RUN-WCH, REP-WCH (without FW-R*′) | SIGNED | SIGNED (N-3) | SIGNED by both |
| SIL-Z, SC-GXC (landed R90 / R91 premises only) | SIGNED | SIGNED | SIGNED by both |
| GXC-CLOSE, GXC-SPLIT, LEVEL-MON, DROP-PAID, FBO-R56, FBO-SPLIT, ZF-SPLIT | SIGNED | SIGNED | SIGNED by both |
| WCH-RED, WCH-ONE | SIGNED | SIGNED | SIGNED by both |
| §7.1-7.4 N5-LZC | SIGNED (variant) | SIGNED (variant) | SIGNED by both |
| §7.5 LZ-NOSIL (implication) | SIGNED | SIGNED | SIGNED by both |
| ASSUMPTION OPT-ONLY | CHECKED TRUE (§7: R90's proofs use σ_new only via OPT-OFF (i)) | CHECKED TRUE (§2.7: the same reading of P-N5-CUT §2-§4) | see §2 |
| line 9ac6fdba | MATCHES, no free symbol | MATCHES, no REQUIRED fix, precisions L-1..L-4 | MATCHES |
The verdicts are identical and the gap map is EMPTY: neither referee lists a gap, and nothing is false.
- Data: two engines on overlapping corpora. Mine: 722 runs, n ≤ 80, given and S3 starts. REFEREE-2's: 1,131 runs, all sizes.
  - Both have 0 violations.
  - Both have 0 class-S re-entries in N5-LZC.
  - Both have NC = NT = 0.
  - Both reproduce the lane's tog6b pins.
  - The absolute counts differ only by run set: class S is 42 for me and 84 for REFEREE-2, which runs both starts on all games.

## 2. OPT-ONLY: joint finding or one referee's strengthening?
JOINT FINDING, signed by both. Each referee independently read the landed proofs of R90's object (P-N5-CUT §2-§4). Each found:
- Fact B, OPT-OFF (ii), W-MON′, W-SUCC and W-RETURN-G use S4a's σ_new only through OPT-OFF (i), i.e. pointwise optimality in H_t against τ_t;
- no step uses the S1 procedure or its tie-break.
LZ-OPT supplies (i) for σ′, so OPT-ONLY holds, and LZ-NOSIL holds for N5-LZC without the assumption.

The two reports agree on the substance and differ only on presentation:
- REFEREE-2 recommends that the line keep the label, discharged by the reports.
- I wrote that the label "can be discharged".

Joint position: the line may keep «under ASSUMPTION OPT-ONLY …». The RESULTS entry should record that both referees checked OPT-ONLY and found
it TRUE for N5-LZC, a referee finding about a VARIANT. It transfers nothing to N5.

## 3. Notes map
| mine | REFEREE-2 | content |
| --- | --- | --- |
| WCH-N1 | N-2 | four SPEC line tags one line low (text verbatim) |
| WCH-N2 | N-1 | TIE (a2)/(a3), RET-WCH (ii)/(iii): read as "v reached after / before π's cycle node" (wording; the GAP-type configuration is covered by (a3)/(iii)) |
| WCH-N3 | N-4 | OPT-ONLY true (§2) |
| WCH-N4 | — | mine only: NC, NT never exhibited (REFEREE-2's data also has NC = NT = 0) |
| (§3-4 watch item) | N-3 | REP-WCH needs no FW-R*′ |
| — | N-5 | REFEREE-2 only: the lane's symtest.py cannot see clause-scope slips (like L-1); agreed |
| §10 precision (k in NZ_P) | L-1 | the same point; precision |
| — | L-2 | REFEREE-2 only: w is never declared a function ℕ → ℕ in the line; agreed, precision |
| — | L-3 | REFEREE-2 only: σ′ is defined by reference to Lemma TIE's two forms; agreed, precision (the reference is to a clause of the same line) |
| — | L-4 | REFEREE-2 only: R84 (a) Fact DELTA is used by the packet but not in the line's premise list. Agreed, and I MISSED it. Precision: add «R84 (a)» to the premises, as R90 / R91's lines do through their objects |
Joint position on the line: MATCHES, no REQUIRED fix. Precisions for W1: L-1 (bind k inside NZ_P's clause), L-2 (declare w : ℕ → ℕ), L-3
(optional), L-4 (cite R84 (a)). I will word-diff W1 against 9ac6fdba and re-run my strict symbol test when the Lead sends the SHA.

## DONE / FINDINGS / NEEDS
- DONE: this §C.
- FINDINGS: verdicts identical; gap map EMPTY; every item SIGNED by both; OPT-ONLY TRUE is a JOINT finding, checked independently by both and
  transferring nothing to N5; L-4 (R84 (a) not cited) was missed by me.
- NEEDS: Lead: the W1 line and fixes SHA for a word-diff.
