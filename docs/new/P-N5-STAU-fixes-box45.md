# P-N5-STAU fixes (box 45 packet): the referees' joint gap STAU-1, their notes, and the audit-list completions, written out
L-NEW successor 25 (Opus 5.5, D14 / D18, L40), for the parked author (successor 24). Written 2026-10-26 09:12Z onward by date -u, on the Lead's
word of 09:02Z (Lead's stamp): "write the referee-notes collection for P-N5-STAU … It contains repairs only and no signed statement changes."
FROZEN at push; its sha1 is reported to the Lead.
- Object: packet docs/new/P-N5-STAU-box45.md, sha1 7446d9a9e198ffa5073e0d43823d753b6aa46b3b (l-new 010bfdae). The packet is NOT edited; this file
  is its correction layer, a record of the reports, not refereed text.
- Sources (read on trunk fd50b8f0, which contains 94910ed3; line numbers below are of these files at fd50b8f0):
  - REFEREE: docs/referee/R-N5-STAU.md (report referee 48674360, successor 13; §C referee 3a999280).
  - REFEREE-2: docs/referee-2/R2-N5-STAU.md (report referee-2 8e42c473, successor 15; §C referee-2 fbbe66a4).
- Verdicts (both, Opus 5.5, D15): Lemma Στ-STEP (a)-(d) SIGNED; the Corollary's transfer clause SIGNED without gap; the Corollary's sentences
  1-2 SIGNED WITH GAP STAU-1 (wording), closed by the repair below; §2 audit CHECKED, question (1) YES (with the completions of §3 below),
  question (2) NO. Nothing here changes a signed statement; the transfer clause, §2, premise (Στ) and P-N5-EPR's EP-1 are unaffected.

## 1. STAU-1, the joint gap: the Corollary's sentences 1-2 (wording)
Packet text (P-N5-STAU-box45.md l. 71-72): "The in-phase transitions of N5 and of N5^τ are exactly Σ-transitions from τ-stable states. They
differ only in WHEN a phase ends: at a τ-stable state where S1's procedure on H′ returns a value-equal τ′ ≠ τ, N5 leaves the phase and N5^τ does
not."
- (i) Sentence 1, "exactly": the in-phase transitions are a SUBSET of the τ-keeping Σ-transitions, not all of them. A Σ-transition from a
  τ-stable state can change λ_Ξ and leave the phase.
  - REFEREE, R-N5-STAU.md l. 51-53: "In-phase also needs λ unchanged: a Σ-transition from a τ-stable state can change λ_Ξ and end the phase
    (my data: 25,997 state visits, on N5 and N5^τ runs of the 𝒞^1O sample, whose N5^τ transition keeps τ and changes λ_Ξ). For N5 the converse
    direction fails too: at a τ-stable state SPEC's S4b can return a value-equal τ′ ≠ τ (the packet's own point)."
  - REFEREE-2, R2-N5-STAU.md l. 144 (N-STAU-1): "holds as an inclusion only: a Σ-transition from a τ-stable state may change λ_Ξ and leave
    the phase (witness instances/nonex_min.pg; 3,514 such transitions on the 503 files)."
  - Witness: REFEREE-2's instances/nonex_min.pg (n 4, sha1 cd2c60f7…, with nonex_min.start), reproduced by REFEREE (R-N5-STAU.md l. 148-149):
    "τ-stable, Iσ = {(1,3)}, Iτ = {(0,0)}, τ value-optimal; N5^τ takes Σ, keeps τ, and λ_Ξ goes [1,1,1,3] → [0,3,0,3] ✓."
- (ii) Sentence 2, "differ only … at a τ-stable state": FALSE as written. N5 and N5^τ also differ at states with Iσ = ∅ (not τ-stable) where τ is
  value-optimal in H′: SPEC's S4b moves τ, while N5^τ keeps τ in S4b^τ and Odd's S4c fallback then fires.
  - REFEREE, R-N5-STAU.md l. 54-57: "they also differ at states with Iσ = ∅ (not τ-stable), where τ is value-optimal in H′ and SPEC's S4b returns
    τ′ ≠ τ. N5 goes to (σ, τ′); N5^τ keeps τ in S4b^τ, so Odd's S4c fallback fires and switches every Iτ vertex to its best dual target. Both
    leave the phase, to DIFFERENT states, so the runs differ after that point."
  - Witness (REFEREE, l. 58-61): scratch/stau_inputs/is0_c1o264.pg (sha1 b0006099716e5c57932c0ce7f334ae3750ff9188; n 12, 𝒞^1O, o = 5): "From the
    canonical start (best-reward): Iσ = ∅, Iτ = {(5,1), (5,10), (5,11)}, τ(5) = 9 value-optimal in H′; SPEC's S4b returns τ(5) = 11 (N5), N5^τ
    falls back to τ(5) = 10." Reproduced by REFEREE-2 (R2-N5-STAU.md l. 167-170) on its own engine.
  - Precision (REFEREE-2, l. 188-189, optional): "in (ii) the two successor states may still coincide (my counts above)."
- The repair: REFEREE's two one-line texts, verbatim (R-N5-STAU.md l. 63-66). REFEREE-2 checked them and judged them correct and the list
  complete (R2-N5-STAU.md l. 181-189). Sentences 1-2 of the Corollary are to be READ as:
  - "The τ-keeping transitions of N5^τ are exactly the Σ-transitions from τ-stable states; N5's are those among them at which SPEC's S4b
    returns τ; the in-phase ones are the τ-keeping ones with λ unchanged."
  - "N5 and N5^τ make different transitions only (i) at a τ-stable state where SPEC's S4b returns a value-equal τ′ ≠ τ (N5 leaves the phase,
    N5^τ need not), and (ii) at a state with Iσ = ∅ where SPEC's S4b returns a value-equal τ′ ≠ τ (both leave the phase, N5^τ by Odd's fallback)."
- Effect (REFEREE, l. 67-68): "none on (a)-(d), on the transfer clause, on §2, or on P-N5-EPR: (Στ) concerns phases of N5^τ runs, case (ii) is a
  phase-ending transition in both runs, and every τ-change of N5^τ is still an improving switch ((d))." REFEREE-2 agrees (l. 179-180): "The
  transfer clause stays signed without gap: it uses only the inclusion "in-phase ⇒ Σ-transition from a τ-stable state", and case (ii) is a
  phase-ending transition in both runs. (Στ) and §2 are unaffected."
- Gap or note (the referees' grades, recorded; both close with the repair). The two §Cs crossed on sentence 1:
  - REFEREE §C.2 (l. 176-178): sentence 1 is a NOTE ("Read as "are Σ-transitions from τ-stable states" (an inclusion) it is true, and the transfer
    clause uses only the inclusion. I withdraw part (i) of STAU-1 as a gap and accept REFEREE-2's N-STAU-1 classification."); sentence 2 stays
    a minor GAP, STAU-1 ("it is a mathematical claim under the label PROVED, and it is FALSE as written").
  - REFEREE-2 §C.2 (l. 177-180): both sentences are a GAP ("Both sentences are part of the statement to sign, and both are false as written. That
    is a gap of the "wording" kind with a one-line repair, not a note. … I withdraw "note" for N-STAU-1 and sign the Corollary's sentences 1-2
    WITH GAP STAU-1, as REFEREE does."); REFEREE-2's joint map (l. 219-220) lists STAU-1 (i) and (ii), both "closed by REFEREE's repair text".
  - So: sentence 2 is a gap for both; sentence 1 is a gap for REFEREE-2 and a note for REFEREE (after their §Cs). With the repair above, both
    are closed under either grade.

## 2. Notes (neither referee calls these gaps; no statement changes)
- N-STAU-2 (REFEREE-2, l. 145; accepted by REFEREE, §C.1 l. 160 "ACCEPTED (citation)"): in §1 (b), (c) for N5, "SPEC's S4b output τ is
  value-optimal" rests on the standing premise 1E-N3 as well as Lemma S (a): "Lemma S (a) says that valuation is the pointwise minimum; 1E-N3
  says τ attains it. Cite both (the packet lists 1E-N3 as a standing premise, so nothing changes)." Read the packet's "(… optimal by Lemma S (a))"
  (l. 63) as "by Lemma S (a) and 1E-N3".
- N-STAU-3 = STAU-N1 (both; R2 l. 146, R l. 47-48 and 139): §1 (d) should name R15 (a) too. REFEREE: "R15 (a) (Ξ non-decreasing; Lemma A per
  switch) transfers by the same property; the table's R22 row cites "R15 (a), (d)" and rests on this." REFEREE-2: "the chain uses it for N5^τ
  through Lemma S (b) (U_τ non-increasing) and wherever Ξ non-decreasing is cited." Read §1 (d)'s last sentence as covering R15 (a), (c), (d).
- N-STAU-4 (REFEREE-2, l. 147; accepted by REFEREE, §C.1 l. 164 "ACCEPTED (definition)"): §3's TIEKEEP "counts S4b^τ's choice (step level,
  L-COMP's count); at Iσ = ∅ the Odd fallback then moves τ, so the transition does not keep τ. Say which count the table uses." The packet's
  §3 definition (l. 139-140, "the iterations where N5^τ keeps τ although SPEC's S4b would move it") is the STEP-level count: it counts S4b^τ's
  output, including the Iσ = ∅ states of STAU-1 (ii), where the transition then moves τ by Odd's fallback. (Lane reading of the definition,
  from the packet's own words; REFEREE-2's l. 131-133 records the step / transition difference on L-COMP's pinned instances.)
- STAU-N3 (REFEREE, l. 141-142; accepted by REFEREE-2, §C.4 l. 207): "§0's "PHASE: maximal run with (λ_Ξ, τ) constant" is the joint λ-phase of R38
  (a) KEY; worth citing, since R19-R25 were signed under the key (λ_Ξ, λ_U, τ) (P-N5-SN-box33 l. 35) and λ_U is constant when τ is." Read §0's
  phase definition with the citation RESULTS R38 (a) Remark KEY.

## 3. Audit-list completions (§2.1 of the packet; both referees answer question (1) YES, the answers are unaffected)
- (a) The four entry-named files not in the packet's 66 (STAU-N2; REFEREE l. 81-86, REFEREE-2 l. 56-61, same four, §C.3 l. 192-193). None
  carries a proof step of the chain:
  - docs/new/N5-ssi-global.md (the SPEC; a premise);
  - docs/lit/T21-VJ00-check.md (R15's literature side finding; R15's proof is G-N5-TERM-reading);
  - docs/new/N5-brchanges-box11.md (R17 "Honest limits" only: three false invariants);
  - docs/red/R58-n5-width.md §9 (RESULTS R18 (a) Proposition X; REFEREE-2 l. 59-61: "It is not used by any proof in the chain … I read §9
    anyway: a locality argument on X (no path to o); no use of S4b's output. Completion, no effect.").
- (b) The referee-written proof steps on the chain (REFEREE-2 §2.1 (ii), l. 62-73; found by REFEREE-2 only, accepted by REFEREE, §C.1 l. 167 and
  checked by search, l. 150-153): signed closures inside chain items that RESULTS entries and fixes files cite; they are not in the 66 files.
  - (ii-a) X-1 / Lemma TF: R-N5-X §3.2 "X-1 closure" and R2-N5-X §3.2 "Lemma TF" (RESULTS R21 (i); docs/agents/R19-note-X1.md). Kinds HYP, DEF.
  - (ii-b) CAP-1: R-N5-FB §4.2 CAP-1 closure, R2-N5-FB §5.2 and §C.3, R-N5-OE §2.2 (RESULTS R25 CAP-1; used by R27 TH, R28 OE, R30 OR / ABS-L).
    Kinds DEF, FIX.
  - (ii-c) TB-1: R-N5-U1 §3.2 TB-1 and R2-N5-U1 §3.2 G-TB-1 (RESULTS R24 TB). S4a's arena optimum only.
  - (ii-d) N-U1-3: R-N5-U1 §C.3 and R2-N5-U1 §C.4, the N-U1-3 closure (RESULTS R24 WC). Kind FIX.
  REFEREE-2 (l. 73): "None uses S4b's output." REFEREE (l. 153): "No use of S4b's output ✓." Neither referee found any of them using S4b's output.
- (c) Table rows the packet's §2.3 lacks (REFEREE-2 §2.3, l. 104-112; accepted by REFEREE, §C.1 l. 168 "ACCEPTED, all FIX / R15 kind"), all
  "holds for N5^τ: yes":
  - R17 Lemma P / Theorem PH applied to τ-fixed segments as runs of N5 on the one-player game G_τ (P-N5-X l. 72, 129 (R21); P-N5-NH l. 49 (R22);
    N5-C-box8 l. 193-203 EQ-STRETCH (R27 object); N5-xing-box27 l. 229-237 (UT)). Kind FIX: "Each needs only that the segment's transitions are
    S4a arena optima and Even switch-alls with τ fixed (and, for EQ-STRETCH, Ξ = W so the gates are G_τ's)."
  - R18 (d) Lemma S (b) (U_τ non-increasing along the run; N5-time-box21 l. 70-71; cited by P-N5-RE l. 23). Kind R15 (with R15 (a); N-STAU-3).
  - R15 (a) wherever cited (e.g. P-N5-NH l. 25, N5-L-box32 l. 57, N5-C-box8 l. 235). Kind R15.

## 4. REFEREE-2's point of detail: N5-1Oacyc-box24 IS on the chain (the packet is right to list it)
- REFEREE (R-N5-STAU.md l. 87-88) called it over-inclusion: "The packet also lists files that are not on the signed chain (N5-1Oacyc-box24 =
  R18 (c); …); harmless over-inclusion."
- REFEREE-2 §C.3 (R2-N5-STAU.md l. 197-201) disagrees: "R18 (c)'s flat-case analysis (box 24 §3 Step 2 case (b), B1/B2) is cited as a proof step
  in the chain: P-N5-X l. 23, 65-66, 83, 94, 100 (R21), P-N5-XA l. 28 and its fixes l. 35 (R20), P-N5-NH l. 27 (R22), P-N5-X-fixes l. 33. So box
  24 is on the chain and the packet is right to list it (its rows R18 box24 l. 99-103, 119-122 are then needed too; both hold)."
- Recorded as REFEREE-2's finding; it does not change either audit answer. Both agree that docs/si/N5-KW-box15.md and docs/new/N5-KW-box42.md
  are not-signed lane proofs (RESULTS R50 "Not signed"), listed harmlessly.

## 5. What this file does not do
- It does not edit the frozen packet, sign anything, or change the status of (Στ) or of P-N5-EPR's EP-1; that is for the Lead and CHECKER.
- No new data. The witnesses (nonex_min.pg, is0_c1o264.pg) are the referees' files, cited in place.
