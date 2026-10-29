# R2-N5-SF-C: REFEREE-2 §C (joint gap map) for packet P-N5-SF (l-new 95a7a581, sha1 dbc2345f…)
Written by REFEREE-2 successor 20, Opus 5.5 (D15, L37), 2026-10-29 from 16:31Z (date -u), on the Lead's word (16:31Z).

**Inputs.**
- REFEREE: docs/referee/R-N5-SF.md at claude/referee 500b51d7 (REFEREE successor 18). First opened 16:31Z, after my report was pushed
  (3ae22a6d, 16:09Z).
- REFEREE-2: docs/referee-2/R2-N5-SF.md (3ae22a6d).
- L-NEW's fixes file docs/new/P-N5-SF-fixes-box55.md at l-new 122c2f68 (sha1 b4534e02…), items F1-F6. F7-F13 are not yet out, and C.4 will
  be extended when the Lead sends their SHA.

## C.1 Verdict map, row by row
| § | item | REFEREE | REFEREE-2 | joint |
| --- | --- | --- | --- | --- |
| §0 | definitions | CHECKED | SIGNED | agreed |
| §2 | Lemma SF-TERM | SIGNED | SIGNED | SIGNED by both |
| §2 | Lemma DECOUPLE | SIGNED | SIGNED | SIGNED by both |
| §3 | Lemma ONE-PLAYER (a), (b) | SIGNED, S1-conformance premise named (SF-N1) | SIGNED, the same premise (N-SF-1); τ-mirror via Ω + 2 (N-SF-2) | SIGNED by both |
| §3 | SF-RED (a) | SIGNED; the S4c step's flatness read from R17's proof (SF-N2) | SIGNED (read from R17 (e)'s text; see C.2) | SIGNED by both, with the citation of C.2 |
| §3 | SF-RED (b) | SIGNED | SIGNED | SIGNED by both |
| §3 | SF-RED (c) | SIGNED | SIGNED | SIGNED by both |
| — | proposed RESULTS line | MATCHES; optional clause "(and SPEC S1 conformance, as R57 (b))" | MATCHES | MATCHES, per both. I support the optional clause: it names the premise F1 now states |
| — | pinned checks | reproduced exactly | reproduced exactly | identical figures |

**Joint gap map: EMPTY.** No gap, nothing FALSE. Every to-sign item is SIGNED by both referees.

## C.2 Where the reports differ, and the E-item
- **SF-N2 (REFEREE), E-item (a citation).**
  - SF-RED (a)'s second clause, "at most n − 1 transitions change Ξ", needs the S4c step on G_σ̄ to change no valuation.
  - My report took this from R17 (e)'s text ("fires only in the value-flat situation").
  - That text says the SITUATION is value-flat, not that the switch changes nothing. The step itself is shown flat in R17's source,
    docs/new/N5-phase-bound-box10.md §3, Theorem PH proof l. 69-73: "it switches only vertices x that are their own cycle nodes … no
    valuation changes". I opened it at 16:3xZ.
  - REFEREE is right, and I missed the distinction.
  - Fix: cite the source line beside R17 (e). The first clause (b − a ≤ n + m) and (b), (c) do not depend on it.
  - Data, both referees: every in-stretch S4c step is Ξ-flat and last (REFEREE: 353 steps; mine: within SEG/FBLAST, 0 violations).
- **SF-N3 (REFEREE), E-item (a quote).** SF-TERM (i) cites SPEC S4a "Else σ_new = σ" (l. 53), which is outside the [S4a] quote. I relied on the
  same line without flagging the quote. Agreed: add it to the quote.
- **SF-N4 (REFEREE) = my §2.3 wording**, opt. "The same arena H" means the same graph with the same ids and increasing-index lists. My report
  says "the same graph with the same lists". Agreed; one clause.
- **SF-N5 (REFEREE) vs N-SF-4 (REFEREE-2)**, record only. The partial start file n3cov_lean.start was handled three ways:
  - REFEREE rejected it and ran S3 only;
  - I filled it from S3, the lane's convention, and reproduced the lane's ROW figures exactly;
  - with first-successor fill the figures differ.

  F4 now states the convention. Consistent.
- **SF-N6 (REFEREE) vs N-SF-5 (REFEREE-2)**, record only. REFEREE: no stretch exceeds n − 1 (its MUT 2 does not bite). Mine: re-measured for
  this §C (X_SEGn1 counter added to sf_check.py, logs re-run): 0 stretches longer than n − 1 on lib41, alt_all, fam and hard. Max stretch
  69 / 59 / 56 / 52 on games with larger n. So neither data set shows that the m term in (a) is needed. Agreed: the bound is loose in data.
- **SF-N7 (REFEREE) = my §2.5**, record only. The LAM argument is self-contained from R15 (a) and injective rewards (R47 is about N5 runs).
- **SF-N1 = N-SF-1**, both (E, done by F1). Standing S1-conformance premise. Data: REFEREE CONF 695,462 checks; mine OPa 45,163; 0 mismatches
  in both.
- **REFEREE-2 only:**
  - N-SF-2 (τ-mirror via Ω + 2): E, done by F2.
  - N-SF-3 (prefix of a λ-phase): E, done by F3. REFEREE's §4 says "the phase starts at a, since the G_σ̄ run starts there". That is the same
    point, made from the other end.
  - N-SF-6 (reading of "iff"): opt, done by F6.
- Data scale for the landing entry:
  - REFEREE: 4,482 runs (random, library n ≤ 48, families n ≤ 200), CONF 695,462, ONEP 15,614.
  - REFEREE-2: 14,220 runs and 34,162 iterations (random n 4-30, lib41, alt_all, fam, hard), OP 45,163, my N5-SF reproducing the lane's
    ROW figures.
  - 0 violations in both.
- Controls: REFEREE MUT 1 (N5's own S4a in place of S4a′) bites. My X_ORBN5 is the same contrast on the run level (2,787 runs where N5's
  σ-sequence differs).

## C.3 Check of L-NEW's fixes F1-F6 (l-new 122c2f68)
| item | answers | content check | clarification or widening? |
| --- | --- | --- | --- |
| F1 | N-SF-1 (also SF-N1) | Names S1 conformance (G-N5T-1) as a standing premise of ONE-PLAYER (a). Correct | CLARIFICATION. It names a premise the proof already used; no statement changes. Recommend that F1 also cover REFEREE's SF-N1 wording for Remark 2 (it says SF-RED uses nothing about σ̄ "beyond its being a function of σ") |
| F2 | N-SF-2 | Ω + 2 keeps ranks, parities and lists, so S1's output on H′ equals N5's S4a output on G^d_τ̄. Correct; matches my OPb check | CLARIFICATION (it supplies the mirror's one line; no statement changes) |
| F3 | N-SF-3 | "a PREFIX of a λ-phase"; R17 (c) bounds the whole phase. Correct | CLARIFICATION (proof wording; the bound is unchanged) |
| F4 | N-SF-4 | Partial start files are filled from S3 by n5x.start_pair, which affects the ROW figures; theorems are per run. Correct; matches my reproduction | CLARIFICATION (DATA convention only) |
| F5 | N-SF-5 | Remark 1 not visible in data; adds the lane's own max 101 on switchbestexp_16 (n 410, n + m 1,380) | CLARIFICATION (DATA). The 101 figure is the lane's and NOT re-run by me. Not signed |
| F6 | N-SF-6 | "iff" over all runs of the class; also per fixed start rule, because (b), (c) are per run. Correct: both directions are per-run inequalities | CLARIFICATION. The per-start-rule form is a direct reading of the signed per-run inequalities, not a new claim |

None of F1-F6 widens a statement. F1-F6 are ACCEPTED.

## C.4 Joint list for L-NEW (fixes F7-F13, pending)
1. E: SF-N2: cite R17's source (N5-phase-bound-box10.md §3, Theorem PH proof l. 69-73) for the flatness of the S4c step in SF-RED (a)'s
   second clause.
2. E: SF-N3: put SPEC S4a's "Else σ_new = σ" (l. 53) into the [S4a] quote.
3. E (done by F1): extend F1's premise wording to Remark 2 (SF-N1).
4. opt: SF-N4 (same ids, same increasing-index lists), SF-N7 (LAM self-contained), the RESULTS clause "(and SPEC S1 conformance, as
   R57 (b))".
5. record: SF-N5, SF-N6 (consistent with F4, F5).

When the Lead sends F7-F13's SHA, I check them against this list and append the result here as C.5.

## C.5 F7-F13 (l-new e9daffde, fixes file sha1 d937c8a9…; checked 17:1xZ by date -u)
- The packet is unchanged: `git diff 95a7a581 e9daffde -- docs/new/P-N5-SF-box55.md` is empty (sha1 dbc2345f).
- The 6 new quotes are 6/6 verbatim by my strict qcheck (R2-N5-CORE/qcheck.py at e9daffde).

| item | answers | content check | clarification or widening? |
| --- | --- | --- | --- |
| F7 | SF-N1, C.4 item 3 | Names both standing premises of ONE-PLAYER (a): G-N5T-1, and R57 (b)'s "S1's procedure realises an optimal σ̄" (quoted at l. 2915-2916, verbatim). It replaces Remark 2's "nothing about σ̄ beyond its being a function of σ". Not the G-N5T-3 premise. Correct | CLARIFICATION. It names premises already used. Remark 2 was not signed, and F7 makes it more accurate, not wider |
| F8 | SF-N2 (E) | Cites box10 §3 Theorem PH proof l. 69-72 verbatim ("it switches only vertices x that are their own cycle nodes …", "no valuation changes …"). An S4c step switches each such own-cycle-node x to an Ω-best improving successor (the Remark after Theorem PH), so it is a step of that kind | CLARIFICATION (citation). **E-item SF-N2 DISCHARGED** |
| F9 | SF-N3 (E) | The full S4a quote l. 51-53, ending "Else σ_new = σ.", verbatim | CLARIFICATION (quote). **E-item SF-N3 DISCHARGED** |
| F10 | SF-N4 | "The same arena H" = same ids, owners, priorities and increasing-index lists (S1 l. 44, verbatim). Correct | CLARIFICATION |
| F11 | SF-N5 | n3cov_lean.start's SIGMA0 47:18 is on an Odd vertex and has no effect: S1 reads σ only at Even vertices. The two referees' runs differ as starts, not as a disagreement. Consistent with my reproduction (S3 fill + listed entries) | CLARIFICATION (DATA) |
| F12 | SF-N6 | Stretches stay below n − 1 in all data (lane: max 101 at n = 410). A sharper "n − 1" would be a new claim for both referees, and F12 does not make it | CLARIFICATION (DATA). It explicitly does NOT widen |
| F13 | SF-N7 | The LAM argument is self-contained (R15 (a), S1's order, injective p′). R47 is deliberately not cited | CLARIFICATION |

- None of F7-F13 widens a statement. **F7-F13 ACCEPTED.**
- All REFEREE-2 E-items of this §C are discharged: SF-N2 (F8), SF-N3 (F9), and F1 extended to Remark 2 (F7).
- With F1-F13, the P-N5-SF joint gap map stays EMPTY and has no open E-item.

## C.6 DONE / FINDINGS / NEEDS
- DONE: this §C. sf_check.py gained the X_SEGn1 control; logs lib41, alt_all, fam and hard re-run, all RESULT PASS.
- FINDINGS:
  - The joint gap map is EMPTY, and every item is SIGNED by both referees.
  - E-items: SF-N2 (citation; my report missed it) and SF-N3 (quote). F1-F6 are all clarifications and are accepted.
  - Neither data set shows a stretch longer than n − 1.
- NEEDS: (C.5 done) none. I recommend the optional RESULTS clause "(and SPEC S1 conformance, as R57 (b))", which F7 supports.
