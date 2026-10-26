# P-N5-EPC fixes (box 48 packet): the referees' notes, written out (no gap)
L-NEW successor 29 (Opus 5.5, D14 / D18, L40), for the parked author (successor 27). Written 2026-10-26 from 17:57Z by date -u, on the Lead's word of
17:39Z (Lead's stamp): "Switch now to the EPC fixes file, docs/new/P-N5-EPC-fixes-box48.md." and "Repairs only; quotes checked by script."
FROZEN at push; its sha1 is reported to the Lead.
- Object: packet docs/new/P-N5-EPC-box48.md, sha1 9f48ded742d7f44bbf82ae8ec9e0e88c46457700 (l-new freeze 81ab0b72; re-measured on this tree at
  successor 29's handover check). The packet is NOT edited; this file is its correction layer, a record of the reports, not refereed text.
- Sources. Each referee file is read at the commit that holds its §C. Line numbers are of these files at these commits:
  - REFEREE: docs/referee/R-N5-EPC.md at claude/referee cd4795f8 (report a52feb43, data addendum 58fd9535, §C cd4795f8; successor 15).
  - REFEREE-2: docs/referee-2/R2-N5-EPC.md at claude/referee-2 c4975512 (report 62b72f6e, §C c4975512; successor 17).
  - The packet at l-new 81ab0b72.
  Every quote below, set in curly double quotes, was checked by script against those revisions (whitespace normalised, then substring test; §6).
- Nothing here changes a signed statement.

## 1. Verdicts (both referees, Opus 5.5, D15)
- REFEREE (R-N5-EPC.md l. 21-37): every item of §1-§3 and the §5 remark SIGNED; §4 EP-ASM “SIGNED as an assembly; its second term SIGNED AS AN
  IMPLICATION from (Στ)” (l. 33); §5's DEAD guess “CONFIRMED DEAD” (l. 35); FB-C′ “EPC's own proof stands WITHOUT my FBC-N3 route” (l. 31); l. 37:
  “No gap. Notes EPC-N1..N4.”
- REFEREE-2 (R2-N5-EPC.md l. 18-32, §5 l. 130-134): every item SIGN, EP-ASM's second term as an implication; l. 32: “No gap. Notes N-EPC-1..6
  (§3).”; l. 131-132: “SIGN, on every game, under the standing SPEC premise 1E-N3 (P1) and Q-A”.
- Joint: REFEREE §C l. 146: “Verdicts identical. Joint gap map: EMPTY.”; REFEREE-2 §C l. 154: “No disagreement. Joint gap map: EMPTY.”
- Scope, both: EP-C and EP-ASM are reductions to quantities not bounded here; FB-C′ bounds f by n·|𝒞_f(P)|, not bounded on general games; no
  running-time bound; G-N5-TIME stays OPEN (REFEREE l. 37-38, REFEREE-2 l. 15-16).

## 2. Notes matched across the two reports (both §Cs; the Lead's word of 17:39Z: "Match them per the §Cs")
| REFEREE | REFEREE-2 | kind | §C relation |
| --- | --- | --- | --- |
| EPC-N1 | (its N-FBC-1 on P-N5-FBC) | unstated fact LEV_C ≥ 0 (repair R1) | REFEREE-2 §C l. 144: ACCEPT |
| EPC-N2 | — | wording of RET-FB's induction (repair R2) | REFEREE-2 §C l. 145: ACCEPT (wording note) |
| EPC-N3 | N-EPC-6 | EP-ASM's statement line should name its open terms (repair R3); N-EPC-6 is the data behind it | REFEREE-2 §C l. 146: ACCEPT, compatible |
| — | N-EPC-1 | pin wording (repair R4) | REFEREE §C l. 155: ACCEPTED |
| — | N-EPC-2 | definition of D_C (repair R5) | REFEREE §C l. 156: ACCEPTED |
| — | N-EPC-3 | citation not needed (repair R6) | REFEREE §C l. 157: ACCEPTED |
| — (REFEREE §2 checks it without a note) | N-EPC-4 | RET-FB's Even step is frame-free (remark, §4) | REFEREE §C l. 154: ACCEPTED |
| EPC-N4 | N-EPC-5 | VIS (a) untested; SAT-1 open; SAT-FB1 does not give it (remark, §4) | same finding; REFEREE-2 §C l. 147: ACCEPT EPC-N4's wording |
Union of notes to the lane, REFEREE-2 §C l. 154: “Notes to the lane (union): EPC-N1..N4, N-EPC-1..6.”

## 3. Repairs (wording, definitions and citations; no statement changes)
- R1 = EPC-N1 (FB-C′'s count). Packet l. 109-110: “consecutive unsaturated ones have strictly rising LEV_C in {0, …, n − 2}: at most n − 1.”
  REFEREE l. 124-125: “"values in {0, …, n − 2}" needs LEV_C ≥ 0 at every state, true (0-edge paths sit at cycle nodes of λ) and unstated here
  too.” Add to §0, after LEV_C's definition (as in P-N5-FBC-fixes-box47 R3): LEV_C(k) ≥ 0 at every state of P (the only 0-edge paths are x = u, a
  cycle node of λ, and Ξ_k(u) = (u, ∅, 0) throughout the phase), so unsaturated values lie in {0, …, n − 2}. The same fact is used in VIS (b)
  (packet l. 87-88: “from a value in {0, …, n − 2}”); REFEREE-2 lists it among VIS's premises (l. 23: “LEV_C monotone and ≥ 0”).
- R2 = EPC-N2 (RET-FB's induction). REFEREE l. 126-127: “The induction is on |r| at the fixed C-state s, and only the Odd branch calls it; one
  sentence would say so (the Even branch bounds Ξ_s directly through t + 1 and (MON)).” Add after the packet's “by induction on |r|” (l. 70): the
  induction is at the fixed C-state s over all start vertices; only the Odd branch uses the induction hypothesis; the Even branch bounds Ξ_{t+1}(y)
  through the fallback and carries it to s by (MON). REFEREE §2 (l. 54-55) checked that this makes the induction well-founded.
- R3 = EPC-N3 (EP-ASM is a reduction; with N-EPC-6). REFEREE l. 128-129: “EP-ASM is a reduction: say in its statement line that X_dir, X_big,
  NCONF_{≥2}, R⁰_{≥2} are unbounded here”. Read Corollary EP-ASM (packet l. 127-128) as ending: “the second term as an implication from (Στ)”, followed by:
  X_dir, X_big, NCONF_{≥2}(P) and R⁰_{≥2}(P) are not bounded here, so EP-ASM is a reduction of N_ep to these four quantities (plus premise (Στ) and
  R51 (a)'s polynomial T*_Q for the second term); it bounds N_ep on no class by itself (REFEREE §4 l. 92-93). REFEREE-2's N-EPC-6 (l. 105-107) is
  the data side: “Of the 1,340 returns classified exactly, 611 are kind (b) (a fallback in between, so LEV_C rises) and 729 are R⁰
  (fallback-free).”
- R4 = N-EPC-1 (pin wording). Packet l. 8: “Pinned at trunk f4562054 (merged into l-new before the freeze); every quote is checked there (§7).”
  REFEREE-2 l. 90-92: “The packet's header says "Pinned at trunk f4562054", which is the revision of its quotes; the Lead's "pinned 9f48ded7" is
  the packet file's sha1, and the frozen file is at l-new 81ab0b72 (on trunk).” Read l. 8 as: quotes checked at trunk f4562054; the packet file
  is frozen at l-new 81ab0b72 with sha1 9f48ded742d7f44bbf82ae8ec9e0e88c46457700 (the Lead's pin).
- R5 = N-EPC-2 (D_C). Packet l. 42-43 defines “D_E := {q ∈ Q : σ̄_E(q) ≠ τ(q)}” and uses |D_C| in “NCONF_{≥2}(P) := those with |D_C| ≥ 2”.
  REFEREE-2 l. 93-94: “D_C := {q ∈ Q : C(q) ≠ τ(q)} (the same set, since D_E is a function of the epoch's configuration). One line.” Add that line
  to §0: for a configuration C, D_C := {q ∈ Q : C(q) ≠ τ(q)}; D_E = D_C for every epoch E of configuration C (τ is constant on P).
- R6 = N-EPC-3 (citation). Packet l. 103-104: “exactly as in HON-FB (iv)'s proof (P-N5-HON, RESULTS R68 (c))”. REFEREE-2 l. 96-97: “The step
  itself uses only Iσ = ∅ and the SPEC, so citing S4a / S4b / S4c / S5 directly (as the proof text already does) is enough; the citation is
  correct but not needed.” Read SAT-FB's last step as resting on S4a, S4b, S4c, S5 and FIX 3 (packet §7's quotes), with the reference to HON-FB
  (iv) a cross-reference, not a premise; R68 stays in the premise list for §4's definitions only. REFEREE §3 (l. 66-70) reads the step from
  the SPEC directly too.

## 4. Remarks (no change needed)
- N-EPC-4 (RET-FB's Even step is frame-free). REFEREE-2 l. 98-100: “The relaxation of the Even vertices at a fallback holds in every frame H_C at
  once”; its EVEN check “passed 7,126 times”. The packet says it (l. 77-78: “Its relaxation of the Even vertices is frame-free, so it acts in
  every H_C at once”). REFEREE §C l. 154: ACCEPTED. Nothing to change.
- EPC-N4 = N-EPC-5 (thin spots). REFEREE l. 130-131: “SAT-FB1 bounds saturated FALLBACKS, not saturated epochs, so it does not give SAT-1.”
  REFEREE-2 l. 101-102: “VIS's kind (a) (returns after saturation) NEVER occurs in my data (0 of 1,340 returns), so its 2n(n − 1) term is untested,
  consistent with the packet's CONJECTURE SAT-1.” REFEREE's data agree (§C l. 159: “Both find no kind-(a) return anywhere.”). CONJECTURE SAT-1
  stays OPEN (packet §6); VIS (a)'s term stays as signed. REFEREE-2's control "VIS without R⁰_C" does not bite (l. 102-103); reported, not a
  defect.

## 5. DATA (not a repair): non-flat saturated fallbacks on the two referees' instance lists
- REFEREE sees non-flat saturated fallbacks in its library: R-N5-EPC.md §6 table, “236 (5 / 3)” at n ≤ 20 and “178 (11 / 7)” at n ≤ 34 (saturated
  fallbacks (non-flat / not last)), and on rho3_253_n32 at L-RED's start “51 (51 / 44)”.
- REFEREE-2 sees them only on its named instances: R2-N5-EPC.md §4 table, named set “25 (25 / 23)”; its lib41 row “43 (0 / 0)” and its 𝒞^1O row
  “51 (0 / 0)”.
- REFEREE §C explains the difference by the instance lists (l. 160-162): “REFEREE-2's library shows no non-flat saturated fallback (0 of 43), mine
  shows 5 of 236 (n ≤ 20) and 11 of 178 (n ≤ 34): different instance lists (mine includes experiments/new/esc and docs/referee/ instances such as
  cond_stuck_symsi3_YE, where REFEREE-2 also finds them).” The packet's own §5 DATA (l. 140-141) is of the same kind: “12 of 68 saturated
  fallbacks non-flat, 8 not last”. SAT-FB's disjunction holds at every one of them in all three sources (REFEREE: 0 SATFB failures; REFEREE-2:
  “SAT-FB and SAT-FB1 (713 saturated fallbacks)”, 0 violations). DATA only; no statement depends on it.
- Reproductions, both referees: long121 37 / 14, nep90 90 / 48, nep76 76 / 40 (REFEREE §C l. 159: “Both reproduce long121 37 / 14, nep90 90 / 48,
  nep76 76 / 40.”).
- Independence: REFEREE l. 8-10 and REFEREE-2 l. 6-10 (REFEREE-2 saw file NAMES only, opened nothing, before its report was fixed).

## 6. Quote check (script; run from the repository root)
`python3 experiments/new/box48/quotecheck2.py docs/new/P-N5-EPC-fixes-box48.md cd4795f8:docs/referee/R-N5-EPC.md
c4975512:docs/referee-2/R2-N5-EPC.md 81ab0b72:docs/new/P-N5-EPC-box48.md` prints, for every quote, the revision, file and line(s) where it
occurs, and exits 1 if any quote occurs in none (the Lead's words in the header and §2 are a message, set in straight quotes, so they are not
checked). Output: experiments/new/box48/out/quotecheck_epc_fixes.txt.
