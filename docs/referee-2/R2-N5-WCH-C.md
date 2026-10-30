# R2-N5-WCH-C: §C cross-map of the two referee reports on P-N5-WCH (REFEREE-2 successor 22, Opus 5.5, D15)
Reports mapped:
- mine: docs/referee-2/R2-N5-WCH.md (claude/referee-2 24f32388), pushed before any docs/referee/ file for this packet was opened;
- REFEREE successor 19's: docs/referee/R-N5-WCH.md (claude/referee d71d6e55), opened after the Lead's word at 10:32Z.
Object: P-N5-WCH-box79.md @ l-new 2ad78f51 (sha1 31caa72e…) and the line 9ac6fdba…, the same in both reports.

## C.1 Verdicts side by side
| item | REFEREE 19 | REFEREE-2 22 | joint |
| --- | --- | --- | --- |
| Fact REW, LEX, COMMON PREFIX | SIGNED | SIGNED | agree |
| Lemma TIE (a), (b) | SIGNED (+ WCH-N2) | SIGNED (+ N-1) | agree; same wording note |
| NEW-BOUND | SIGNED | SIGNED | agree |
| RET-WCH | SIGNED (+ WCH-N2) | SIGNED (+ N-1) | agree; both checked the tie-leave and cycle-node cases |
| RUN-WCH, REP-WCH | SIGNED; no FW-R*′ | SIGNED; no FW-R*′ (N-3) | agree |
| SIL-Z, SC-GXC | SIGNED; landed R90 / R91 only | SIGNED; landed only | agree |
| GXC-CLOSE, GXC-SPLIT | SIGNED | SIGNED | agree |
| LEVEL-MON, DROP-PAID | SIGNED | SIGNED | agree |
| FBO-R56, FBO-SPLIT, ZF-SPLIT | SIGNED | SIGNED | agree |
| WCH-RED, WCH-ONE | SIGNED | SIGNED | agree |
| N5-LZC §7.1-§7.4 | SIGNED (VARIANT) | SIGNED (VARIANT) | agree |
| LZ-NOSIL; OPT-ONLY | SIGNED; OPT-ONLY TRUE (WCH-N3) | SIGNED; OPT-ONLY TRUE (§2.7, N-4) | agree (C.3) |
| OPT-ONLY in the N5 part | not used | not used | agree |
| line 9ac6fdba | MATCHES; no free symbol | MATCHES; precisions L-1..L-4 | agree on MATCHES; precisions C.4 |

## C.2 Joint gap map
- Proof gaps: NONE in either report. Joint gap map: EMPTY.
- Required fixes: NONE in either report.

## C.3 OPT-ONLY as a joint finding
- Both referees checked ASSUMPTION OPT-ONLY independently against R90's object (P-N5-CUT §1-§3), and both find it TRUE, for the same reason:
  - Fact B uses only [S4a]-[S4c] (S4d) and R15 (d), read on σ′; σ′ switches only along improving edges;
  - OPT-OFF (ii), W-MON′, W-SUCC and W-RETURN-G use S4a's σ_new only through OPT-OFF (i) (pointwise optimality in H_t against τ_t), which
    LZ-OPT supplies for σ′;
  - no step uses S1's tie-break or the identity σ_new = S1's output.
- Joint status (Opus 5.5, D15): OPT-ONLY is DOUBLE-REFEREED TRUE, and LZ-NOSIL holds for N5-LZC without the assumption. This is a referee
  finding about a landed proof, not a new landed lemma.
- Two ways to carry it:
  - (a) keep the line as frozen, with LZ-NOSIL «under ASSUMPTION OPT-ONLY», and record in the RESULTS entry's body that both referees
    checked OPT-ONLY true;
  - (b) drop the assumption from the line. That STRENGTHENS the landed statement, so it needs a word-diff and both referees' sign-off on the
    new line (W1).
- My recommendation is (a) unless the lane wants (b), because (a) changes nothing that was signed. Either way, nothing in N5 (§2-§6) depends
  on it.

## C.4 Notes mapping
| REFEREE 19 | REFEREE-2 22 | joint reading |
| --- | --- | --- |
| WCH-N1 (four SPEC tags one line low; add a quote check to «box 79») | N-2 (same four tags) | same; REFEREE's extra suggestion (a pinned quote check) accepted |
| WCH-N2 (case split «after / before the cycle node»; it is P-N5-GAP's G-GAP-1 configuration) | N-1 (same reading, same cases in TIE and RET-WCH) | same; REFEREE's link to G-GAP-1 (R91) is right and worth recording: the same configuration has now been mis-split twice |
| WCH-N3 (OPT-ONLY true) | N-4 / §2.7 | same (C.3) |
| WCH-N4 (NC_R = NT_R = 0 on its corpus; SIL-Z (b)'s exclusion and the NT term never exercised) | — (my data also has NC 0, NT 0 on 1,131 runs, but I did not record it as a note) | I MISSED it as a note; accepted: those premises are used by the proofs, not exhibited by data |
| §10 precision: k in NZ_P bound only through ZF_P's gloss | L-1 | same |
| — (lists w(n), [P-WCHτ](w) as bound) | L-2 (w never declared a function ℕ → ℕ) | precision only; REFEREE reads «[P-WCHτ](w)» as the binder, which is acceptable; the packet §1 declares w : ℕ → ℕ, the line does not |
| — | L-3 (N5-LZC's σ′ in the line by reference to Lemma TIE's two forms) | precision only; REFEREE accepts the in-line reference |
| — | L-4 (Fact DELTA, R84 (a), used and not listed) | precision only |
| — (symtest.py agrees) | N-5 (symtest.py cannot see clause scope; L-1 shows it) | consistent: both found L-1 by hand; the tool did not |
| REP-WCH needs no FW-R*′ (§4) | N-3 | same |
| MUT 1-4 bite, MUT 5 never | controls X_TIE_noeq, X_LM_s4a bite | consistent; REFEREE's MUT 3 = my X_LM_s4a |

## C.5 Data on two engines
- Pins: both reproduce tog6b_n32 exactly. N5: returns 4, paid 3, TT 1, TIE 2. N5-LZC: returns 3, paid 3, TIE 0.
- Corpus counts differ by run set, not by definition:
  - REFEREE: 719 distinct games, n ≤ 80, given start and S3, 722 runs: returns 2,656, TT 44, class S 42.
  - mine: 1,131 runs with the lane's convention (alt_all's 319 start-less lines from S3; one invalid start skipped): returns 6,246, TT 88,
    class S 84.
  - Both find 0 violations, NC = NT = 0, every class-S re-entry a GXC event, N5-LZC with TIE = TT = 0 and no class-S re-entry, and LZ-OPT
    exact at every S4a computation.
- My TT 88 and TIE 397 equal the lane's §8.4 exactly.

## DONE / FINDINGS / NEEDS
- DONE: this §C.
- FINDINGS:
  1. Joint gap map EMPTY; no required fix; every item of §2-§7 SIGNED by both.
  2. OPT-ONLY: double-refereed TRUE; LZ-NOSIL holds outright. Recommend carrying it as a recorded finding (C.3 (a)); dropping the assumption
     from the line is a strengthening that needs a word-diff.
  3. Notes agree: WCH-N1 = N-2, WCH-N2 = N-1 (the G-GAP-1 configuration again), WCH-N3 = N-4. I missed WCH-N4 as a note.
  4. Precisions: L-1 is joint; L-2..L-4 are mine only.
- NEEDS: Lead: send the corrected line W1 for the word-diff; your choice between C.3 (a) and (b).
