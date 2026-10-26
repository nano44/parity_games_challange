# P-N5-FBC fixes (box 47 packet): the referees' notes, written out (no gap)
L-NEW successor 28 (Opus 5.5, D14 / D18, L40), for the parked author (successor 26). Written 2026-10-26 15:16Z onward by date -u, on the Lead's GO
of 15:16Z (Lead's stamp): "Queue item 1, now: docs/new/P-N5-FBC-fixes-box47.md." and "Repairs only, no signed statement changes." FROZEN at
push; its sha1 is reported to the Lead.
- Object: packet docs/new/P-N5-FBC-box47.md, sha1 32d3776cf4090fb15c1d0cb4c8b4f59276f64e21 (l-new freeze 1f8d6d7d; re-measured with `git show
  1f8d6d7d:… | sha1sum` and on this tree). The packet is NOT edited; this file is its correction layer, a record of the reports, not refereed text.
- Sources. Each referee file is read at the commit that holds its §C (trunk 10b5b144 was still landing them at 15:16Z). Line numbers are of
  these files at these commits:
  - REFEREE: docs/referee/R-N5-FBC.md at claude/referee d08011be (report 0addfc5f, §C d08011be; successor 15).
  - REFEREE-2: docs/referee-2/R2-N5-FBC.md at claude/referee-2 bde1ea77 (report aab45be6, pushed with the trunk merge 64ee8e9c; §C bde1ea77;
    successor 17).
  - The packet at l-new 1f8d6d7d; P-N5-HON-box46.md and docs/RESULTS.md at trunk 10b5b144; P-N5-EPC-box48.md at l-new 81ab0b72 (its freeze).
  Every quote below, set in curly double quotes, was checked by script against those revisions (whitespace normalised, then substring test; §6).
- Nothing here changes a signed statement.

## 1. Verdicts (both referees, Opus 5.5, D15)
- REFEREE (R-N5-FBC.md l. 20-33): FB-RISE_C, SAT_C (both parts), Theorem FB-C, Corollaries (a), (b), (c) SIGNED; (d) “SIGNED (the inequality; the
  comparison sentences after it are READINGS, note FBC-N4)” (l. 29); the header's comparison with EPOCH “CONFIRMED for n ≥ 2” (l. 30); l. 32:
  “No gap. Notes FBC-N1..N4.”
- REFEREE-2 (R2-N5-FBC.md l. 18-31, §5 l. 129-132): every statement SIGN, l. 30: “No gap. Notes N-FBC-1..6 (§3).”; l. 129-130: “SIGN, on every game,
  under the standing SPEC premise 1E-N3 (in form P1, through (MON)) and P-N5-HONFF's question Q-A”.
- Joint: REFEREE §C l. 145: “Verdicts identical. Joint gap map: EMPTY (neither referee found a gap).”; REFEREE-2 §C l. 161: “No disagreement on
  any signed item. Joint gap map: EMPTY.”
- Scope, both: FB-C bounds f per phase by the number of distinct configurations at fallback sources, itself not bounded on general games; no
  running-time bound; G-N5-TIME stays OPEN (REFEREE l. 32-33, REFEREE-2 l. 15-16).

## 2. Notes matched across the two reports (both §Cs; the Lead's matching of 15:16Z agrees)
| REFEREE | REFEREE-2 | kind | §C relation |
| --- | --- | --- | --- |
| FBC-N1 | N-FBC-3 | definitions imported (repair, §3) | same note; FBC-N1 the wider form (REFEREE-2 §C l. 141: ACCEPT) |
| FBC-N2 | — | citation (repair, §3) | REFEREE-2 §C l. 142: ACCEPT |
| — | N-FBC-1 | one sentence missing in FB-C's count (repair, §3) | REFEREE §C l. 154: ACCEPTED |
| — | N-FBC-2 | where the C-state hypothesis is used (remark, §3) | REFEREE §C l. 155: ACCEPTED, complementary to REFEREE §1 |
| header n = 1 remark (§3) | N-FBC-4 | the header's "weaker" at n = 1 (repair, §3) | same; REFEREE-2 accepts REFEREE's sharper line (f = 0) |
| FBC-N4 | N-FBC-5 | "incomparable" with R56 (reading, §3) | same substance; REFEREE-2 accepts FBC-N4's wording |
| FBC-N3 | N-FBC-6 | strengthening (NOT a repair; §4) | REFEREE-2 checked FBC-N3's proof; it supersedes N-FBC-5 and N-FBC-6 |
Union of notes to the lane, REFEREE-2 §C l. 161-162: “FBC-N1..N4, N-FBC-1, N-FBC-2, N-FBC-4 (N-FBC-3 ⊆ FBC-N1; N-FBC-5, N-FBC-6 superseded by
FBC-N3 as above)”.

## 3. Repairs (wording and citation; no statement changes)
- R1 = FBC-N1 = N-FBC-3 (imported definitions). Packet §0 l. 39: “As P-N5-HONFF §0 (state k, σ̄_k, Ξ_k, λ, phase P, in-phase, value(r)).” REFEREE
  l. 126-127: “D_k (used in (c), §3) and EPOCH / N_ep (used in (a), (d)) are defined in P-N5-HON §0 (l. 44, landed R68) and RESULTS R60 / R61 / R63,
  not in P-N5-HONFF §0. Name them.” REFEREE-2 l. 93: “Add D to the imported list.” Read §0's first sentence as: as P-N5-HONFF §0 (state k, σ̄_k,
  Ξ_k, λ, phase P, in-phase, value(r)); and from P-N5-HON §0 (RESULTS R68), “D_k := {q ∈ Q : σ̄_k(q) ≠ τ(q)}” (P-N5-HON l. 44); and from RESULTS
  R60's setting line, “An EPOCH: a maximal run E of consecutive states of a phase on which σ̄_t|Q is constant” and “N_ep := the epochs of the
  phase” (RESULTS l. 3065-3068). REFEREE-2 l. 93-95 checked that this D_k is the one that makes (c) true.
- R2 = FBC-N2 (citation). Packet l. 32-33: “RESULTS R15 (d)'s "at most 4n(n−1) consecutive N5 iterations leave both Ωσ and Ωτ unchanged" (Ωσ read
  as S1's Ξ, as every per-phase packet does).” REFEREE l. 128-129: “SAT_C (2) applies R15 (d) to Ξ; the bridge is R57 (a) (VJ) under 1E-N3 (as in
  R60's premises, ACCEL-N2). Cite it instead of "read as … as every per-phase packet does".” REFEREE-2 §C l. 142: “ACCEPT FBC-N2 (citation note)”.
  Read the parenthetical as: (Ωσ = Ξ by RESULTS R57 (a), premise (VJ), under the standing premise 1E-N3, as in R60's premise list). R57 (a) reads
  “Premise (VJ), on every game: for every positional σ and every positional Odd strategy τ′, Ξσ(v) ⊴ V_{σ,τ′}(v) at every v” (RESULTS l. 2907).
  The same bridge is in REFEREE-2's premise column for (MON), l. 21: “(MON) = R15 (a), (d) via (VJ) under P1”.
- R3 = N-FBC-1 (FB-C's count). Packet l. 71: “with values in {0, …, n − 2} there are at most n − 1 of them.” REFEREE-2 l. 86-88: “The unsaturated
  count "with values in {0, …, n − 2} there are at most n − 1 of them" needs LEV_C ≥ 0 at every state of P. It holds (0-edge paths exist only at
  cycle nodes of λ, where Ξ = (x, ∅, 0) throughout the phase), but the packet does not say it.” REFEREE l. 39: “LEV_C(k) ≥ 0 at every state (j = 0:
  x = u a cycle node of λ, Ξ_k(u) = (u, ∅, 0))”; §C l. 154: “ACCEPTED (I checked the fact but did not flag that the packet omits it)”. Add to §0,
  after LEV_C's definition: LEV_C(k) ≥ 0 at every state of P (the only 0-edge paths are x = u, a cycle node of λ, and Ξ_k(u) = (u, ∅, 0) throughout
  the phase), so unsaturated values lie in {0, …, n − 2}.
- R4 = N-FBC-2 (remark; no change needed). REFEREE-2 l. 89-90: “FB-RISE_C's Even case uses only LEV_C's definition at t, S4c, Case A, (MON),
  (V1), (V2): it holds at ANY source state, not only a C-state.” REFEREE l. 49: “The Odd case does not use the fallback at all: it holds at EVERY
  C-state”. REFEREE §C l. 155: “the two remarks are complementary (Odd case: any C-state, no fallback; Even case: any state, the fallback)”. So the
  configuration frame is paid for exactly in the Odd case; the signed statement is unchanged.
- R5 = REFEREE's n = 1 line = N-FBC-4 (the header's "weaker"). Packet l. 13: “Its Corollary (a) in the N_ep form, and Corollary (d), are WEAKER
  than EPOCH (c)”. REFEREE l. 99-100: “At n = 1 the only vertex has a self-loop only, Iσ = ∅, f = 0, and both forms are trivial.” REFEREE-2 l. 96:
  “True for n ≥ 2, false at n = 1 (vacuously). Either say "for n ≥ 2" or ignore; it changes nothing signed.” REFEREE-2 §C l. 140: “ACCEPT
  REFEREE's sharper n = 1 line”. Read the header (l. 13) and the CORRECTION paragraph (l. 92) as "WEAKER than EPOCH (c) for n ≥ 2; at n = 1,
  f = 0 and both forms hold trivially".
- R6 = FBC-N4 = N-FBC-5 (reading; "incomparable"). Packet l. 10: “It is INCOMPARABLE with RESULTS R56”; l. 89: “The two are incomparable in
  general.” REFEREE l. 132: “(d)'s "incomparable in general" with R56 is witnessed in one direction only (§3); the header's "INCOMPARABLE"
  likewise.” REFEREE-2 l. 82-83: “R56 (f) (f ≤ 1 + (n − 1)(2 + ρ)) and FB-C are incomparable as FORMULAS (different quantities, neither factor
  dominates)”; §C l. 144: “ACCEPT FBC-N4's wording ("witnessed in one direction only")”. Read both sentences as: incomparable as formulas; in
  data R56's number was the smaller one in every phase both referees checked, and no known phase witnesses the other direction (it needs ρ of
  order 4n·|𝒞_f(P)|; REFEREE l. 95-96). A READING, as REFEREE l. 29 labels it; nothing signed changes.

## 4. FBC-N3 is not a repair: it is P-N5-EPC §3 (refereed there)
- FBC-N3 (REFEREE §2, l. 67-84) proves “Per phase P and configuration C, at most one in-phase fallback has a saturated C-state source.” and so
  f ≤ n·|𝒞_f(P)|, by SAT_C (2), R15 (b) (through R57 (a)) and R38 (f) CN-LAST. REFEREE-2 §C l. 147-152 checked it line by line: “CORRECT. So
  f ≤ n·\|𝒞_f(P)\|.” and l. 159-160: “FBC-N3 is a referee strengthening, not a statement of the packet: for the lane to take up as a new
  statement, then to be refereed as one.”
- The lane has taken it up: packet P-N5-EPC-box48 (frozen, sha1 9f48ded742d7f44bbf82ae8ec9e0e88c46457700, l-new 81ab0b72, pinned on trunk) §3,
  “Corollary SAT-FB1. For every phase P and configuration C, at most one in-phase fallback of P has a saturated C-state as its source.” and
  “Theorem FB-C′. In every phase P of N5 on every game, f ≤ n·|𝒞_f(P)|.” EPC proves SAT-FB1 by its own route (Lemma SAT-FB, flat fallback ⇒ Iσ = ∅
  next) and cites FBC-N3 as a referee note, not a premise. EPC is with both referees now. So FB-C's signed bound (4n² − 3n) stands as signed;
  the n·|𝒞_f| form is EPC's, and lands only with EPC.
- Consequences already recorded by the referees: N-FBC-6 (“SAT_C's 4n(n − 1) + 1 term is untested”, REFEREE-2 l. 101-102) is explained, not a
  thin spot (§C l. 155: “"≤ 1 saturated per configuration" is a theorem, which is why the control could not bite”); N-FBC-5's data sign
  reverses under FB-C′ (§C l. 156: “n·\|𝒞_f\| ≤ n·N_ep < 1 + n·N_ep”). The packet's §5 second OPEN item is answered by FBC-N3 / EPC §3.

## 5. Context (not part of the fixes)
- Both referees reproduce the packet's figures: REFEREE l. 120-121 (fr39_q4_n48: “39 in-phase fallbacks in one phase, 7 configurations at
  fallback sources, max 24 unsaturated per configuration, 0 saturated: the packet's row exactly.”), REFEREE-2 l. 117-118 (farrise25_n32,
  “unsaturated sources of one configuration 25”). Both τ-frame controls bite (REFEREE 79, REFEREE-2 14,399; REFEREE §C l. 158-159).
- Independence: REFEREE l. 6-7 and REFEREE-2 l. 6-9 (REFEREE-2 saw file NAMES only at its push turn and opened nothing; its text was final).

## 6. Quote check (script; run from the repository root)
`python3 experiments/new/box48/quotecheck2.py docs/new/P-N5-FBC-fixes-box47.md d08011be:docs/referee/R-N5-FBC.md
bde1ea77:docs/referee-2/R2-N5-FBC.md 1f8d6d7d:docs/new/P-N5-FBC-box47.md 10b5b144:docs/new/P-N5-HON-box46.md 10b5b144:docs/RESULTS.md
81ab0b72:docs/new/P-N5-EPC-box48.md` prints, for every quote, the revision, file and line(s) where it occurs, and exits
1 if any quote occurs in none (the Lead's GO in the header is a message, set in straight quotes, so it is not checked). Output: experiments/new/box48/out/quotecheck_fbc_fixes.txt.
