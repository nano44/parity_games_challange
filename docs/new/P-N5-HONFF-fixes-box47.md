# P-N5-HONFF fixes (box 47 packet): the referees' notes, written out (no gap)
L-NEW successor 27 (Opus 5.5, D14 / D18, L40), for the parked author (successor 26). Written 2026-10-26 13:34Z onward by date -u, on the Lead's word of
13:29Z (Lead's stamp): "Side task (3) is due now: the P-N5-HONFF fixes file. Both reports and both §Cs are in. FILE:
docs/new/P-N5-HONFF-fixes-box47.md, repairs only. Packet 98101d1f is FROZEN." FROZEN at push; its sha1 is reported to the Lead.
- Object: packet docs/new/P-N5-HONFF-box47.md, sha1 98101d1fe723a570f3c79085b929a456ebb7dff5 (l-new 2fca63b8; re-measured with `git show
  2fca63b8:… | sha1sum` and on this tree). The packet is NOT edited; this file is its correction layer, a record of the reports, not refereed text.
- Sources. The Lead names trunk ea6ad574; that commit was not fetchable at 13:3xZ (trunk head 16b330d9 has the reports but not the §Cs), so each
  file is read at the commit that holds its §C. The line numbers below are of these files at these commits:
  - REFEREE: docs/referee/R-N5-HONFF.md at claude/referee e7db1ab4 (report cce5ea5e, §C e7db1ab4; successor 14).
  - REFEREE-2: docs/referee-2/R2-N5-HONFF.md at claude/referee-2 11e3cfb1 (report 05e7663c, independence addendum 1306c31e, §C 11e3cfb1;
    successor 16). The Lead notes that REFEREE-2's run-total correction of 13:11Z is in a message only, not in its file; it is not used here.
  - The packet at l-new 2fca63b8.
  Every quote below, set in curly double quotes, was checked by script against those three revisions (whitespace normalised, then substring
  test; §5).
- Nothing here changes a signed statement.

## 1. Verdicts (both referees, Opus 5.5, D15)
- REFEREE (R-N5-HONFF.md l. 19-27): FB-RISE (a), (b), Theorem HON-FF, Corollary HON-0-FF (a)-(c) and REC-1-FF (a) SIGNED; REC-1-FF (c), (d)
  “SIGNED as IMPLICATIONS from (Στ) (at R65's audit strength they hold; signed as stated)” (l. 24); Q-A “YES (§1 below)” (l. 25); l. 27: “No gap.
  Notes HONFF-N1..N3.”
- REFEREE-2 (R2-N5-HONFF.md l. 88-90): “FB-RISE (a), (b), Theorem HON-FF, Corollary HON-0-FF (a)-(c), Corollary REC-1-FF (a): SIGN, on every game,
  under the standing SPEC premise 1E-N3 (P1 for FB-RISE; P1 and P2 for HON-FF through HON step 1). REC-1-FF (c), (d): SIGN as IMPLICATIONS from
  (Στ).” l. 21: “SIGN as IMPLICATIONS from (Στ) (which holds at R65's audit strength)”; l. 24: “No gap. Notes N-HONFF-1..4 (§3).”
- The packet's comparison with REC-0 (RESULTS R66): REFEREE l. 57: “(f + 1)(n + 1) + 4n(n − 1) + 1 − (4n² − 3n) = f(n + 1) + 2 ✓ (re-computed).”;
  REFEREE-2 l. 52: “REC-0 comparison: (f + 1)(n + 1) + 4n(n − 1) + 1 − (4n² − 3n) = f(n + 1) + 2. CORRECT.”
- Q-A: YES from both, with the same four-item list. REFEREE l. 39: “Case A (box 10 §2 l. 32-38) uses: (1) Ω(z) ⪯ Ω(ρ(x))”, then (2) the LEV bound,
  (3) (V1) for the single honest play, (4) (V2) (l. 39-43); l. 42-43: “A1's last link "⪯ Ω_{k+1}(x) by (F2)" is not part of the inequality value(r) ⪯
  Ω(x) and is replaced here by (MON).”; l. 43: “One-player-ness is used nowhere in Case A”. REFEREE-2 l. 30-31: “All four are facts about the VALUE OF
  A PLAY of a positional strategy pair: the one-player hypothesis of R17 is not used.”; l. 32-33: “No optimality premise (P1 or P2) is needed for
  Case A itself.” Both §Cs record the lists as identical: REFEREE l. 89 (“same (identical item list)”), REFEREE-2 l. 107 (its Q-A row: “YES: play-value facts only, no optimality premise”, relation “same”).
  So the packet's question is answered as asked: Case A holds with Ω := Ξ_t, ρ := σ_t, S2's Iσ_t, using only play-value facts, with A1's (F2)
  link replaced by (MON).
- Joint gap map EMPTY: REFEREE §C l. 92: “No disagreement; both: no gap.”, l. 106: “EMPTY.”; REFEREE-2 §C l. 115: “No disagreement. Joint gap map:
  EMPTY.”

## 2. Notes (wording and citation; no statement changes)
- HONFF-N1 (REFEREE; = REFEREE-2 §1 (b); ACCEPTED by REFEREE-2). Packet l. 67: “SAT0's Odd case at h (with N-HON-1's wording) gives W_h(x) ⪰
  value(r).” REFEREE l. 72-73: “what is used is the Odd-case step of SAT0's proof, which is per vertex and hypothesis-free. Say "the Odd-case
  argument of SAT0's proof".” REFEREE-2 l. 44: “SAT0's Odd case does not use SAT0's hypothesis "no W-improving edge" (that is for Even vertices).”
  and §C l. 108: “same; ACCEPT HONFF-N1's wording”. Read the packet's l. 67 (and the premise line l. 29, “Lemma SAT0's Odd case with REFEREE-2's
  wording N-HON-1”) as: the Odd-case argument of SAT0's proof (per vertex; SAT0's hypothesis is not used), with N-HON-1's wording.
- HONFF-N2 (REFEREE; ACCEPTED by REFEREE-2 as a note, §C l. 109: “ACCEPT (note)”). Packet l. 44: “So LEV(k) ≤ LEV_odd(k).” REFEREE l. 74-75: “note
  that LEV(k) ≤ LEV_odd(k) makes (a)'s bound min(LEV(t) + 1, LEV_odd(t), n − 1) ≥ LEV(t), so (a) contains (MON)'s "no fall" as a special case
  (consistent, not an error).” A remark; no change.
- HONFF-N3 (REFEREE; quote line cites). REFEREE l. 76: “the cited line numbers are the lines where each quote begins or ends within the cited
  ranges; all found.” REFEREE-2 l. 23: “all VERBATIM (my own substring check against the six named files at l-new 0238b1cb)”. No change.
- N-HONFF-1 (REFEREE-2; ACCEPTED by REFEREE). Packet l. 30: “RESULTS R21 (a) XW and R23 (g) WM enter only through HON step 1 (fallback-free
  gaps).” REFEREE-2 l. 61-62: “XW does NOT enter HON-FF at all (in P-N5-HON, XW is used only in HON-FB (iv), which HON-FF does not cite).” and
  l. 62-63: “suggest "WM (and Lemma S (c)) enter only through HON step 1; XW is not used".” REFEREE §C l. 97: “ACCEPTED (checked: HON-FF cites
  HON steps 0-3, SAT0's Odd case, HON-0, REC-1; none uses XW)”. Read the packet's l. 30 as: RESULTS R23 (g) WM (and Lemma S (c)) enter only
  through HON step 1 (fallback-free gaps); XW is not used. The premise list was over-complete, not wrong.
- N-HONFF-2 (REFEREE-2; ACCEPTED by REFEREE). REFEREE-2 l. 64-65: “FB-RISE (a), (b) need P1 only (through (MON)); P2 enters HON-FF only through
  HON step 1 on fallback-free gaps.” REFEREE §C l. 98: “REFEREE-2 only as a note; ACCEPTED”. So the landing line should name the standing premise
  1E-N3 in its two forms: P1 for FB-RISE; P1 and P2 for HON-FF (through HON step 1). This is how REFEREE-2 signs (§1 above).
- N-HONFF-3 (REFEREE-2; data; the same in REFEREE's §3). The decisive data are thin: REFEREE-2 l. 66: “Exact LEV reached 5 of the 6 known gaps
  with an inside fallback”; l. 68-69: “j7_n32 stays over budget even at 1.5·10⁸ paths per phase (UNK).” REFEREE §C l. 104: “both find j7_n32 over
  budget”. The packet's own row for j10_n24, j7_n32, j8_n32 (packet l. 102, “j10_n24, j7_n32, j8_n32, S3, budget 3·10⁷”) checks 4 fallbacks; no
  engine has an exact LEV on j7_n32's inside gap. No statement depends on data.
- N-HONFF-4 (REFEREE-2; data; the same in REFEREE's §3). REFEREE-2 l. 70: “Dropping the LEV_odd term ("LEV(t + 1) ≥ min(LEV(t) + 1, n − 1)")
  fails 152 times on lib41 (one start)”; REFEREE l. 67-68: “The control without the Odd term fails exactly where the packet says (inside
  fallbacks), always with LEV_odd(t) binding”. The Odd term of FB-RISE (a) is needed, as the packet's CTRL_T column shows.

## 3. The independence addendum (REFEREE-2, accepted by REFEREE)
- REFEREE-2's addendum (R2-N5-HONFF.md l. 92-99): l. 93: “The independence count at the push was 1, not 0”; its commit message's "0" is wrong
  and its header's “1 at 13:06Z” is right (l. 94-95); l. 97-98: “I did not open the file. My report text, verdicts and notes were final at the push
  and are unchanged.” No history was rewritten.
- REFEREE §C l. 80-82 accepts it: “I accept the record; it does not affect either report.”
- So both reports are independent in the fleet's sense: neither opened the other's file before its own report was pushed.

## 4. Context (not part of the fixes)
- RESULTS R68 (P-N5-HON) has landed (docs/RESULTS.md, "### R68"). HON-FF strengthens its Lemma HON / HON′ / HON-0 / REC-1 (a) by removing f
  (and f_in) from the W-honest count; it does not edit R68.
- FB-RISE is used by the lane's unrefereed working docs N5-FB-box47.md (FB-RISE_C, Theorem FB-C; packet P-N5-FBC-box47, frozen, sha1 32d3776c…,
  in the referee queue) and N5-NCONF-box48.md (Lemma RET-FB). Both rest on Q-A, now answered YES by both referees.

## 5. Quote check (script; run from the repository root)
`python3 experiments/new/box48/quotecheck2.py docs/new/P-N5-HONFF-fixes-box47.md e7db1ab4:docs/referee/R-N5-HONFF.md
11e3cfb1:docs/referee-2/R2-N5-HONFF.md 2fca63b8:docs/new/P-N5-HONFF-box47.md` prints, for every quote, the revision, file and line(s) where it
occurs, and exits 1 if any quote occurs in none. Output: experiments/new/box48/out/quotecheck_honff_fixes.txt; result at the freeze in its
last line (`quotes N missing 0`).
