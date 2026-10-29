# P-N5-COMPOSE fixes (box 28): repairs only, after both reports on P-N5-COMPOSE-box28 (all items SIGNED by both; no mathematical gap)
L-SI successor 25 (Opus 5.5; D18, Lead reading L40), at the Lead's request (13:08Z). Object: the frozen packet docs/si/P-N5-COMPOSE-box28.md,
sha1 e1b977aa9cf1583d5e0c442a8f87d024230b6524 (l-si 3ca0932d), UNCHANGED (sha1 pinned in experiments/si/check.sh). This file changes NO signed
statement and NO proof step; every F-item below is APPENDED text that is read together with the packet, or «no change, because …».
Reports: REFEREE (successor 18) docs/referee/R-N5-COMPOSE.md (claude/referee 4896bc2e; notes §8: COMP-E1, COMP-N1..N6); REFEREE-2 (successor
20) docs/referee-2/R2-N5-COMPOSE.md (claude/referee-2 4b8afa95; notes §4: N-C1..N-C5; joint gap map §C, C.4 joint list, read at ee549524). REFEREE's §C (claude/referee
c6011b70): «JOINT GAP MAP: EMPTY. ONE E-ITEM: COMP-E1»; it classes N-C2 / N-C3 (its C3 / C4) as optional, REFEREE-2 as E; appended text is given
for both either way, so the class difference changes nothing here. This file is a lane
record, not refereed text.

## Joint list (REFEREE-2 §C C.4) and where each item is repaired
| item | class (§C C.3) | F-item |
| --- | --- | --- |
| COMP-E1 = D1 | E | F1 (definition line) |
| N-C2 = D2 | E | F2 |
| N-C3 = D3 | E | F3 |
| COMP-N1 = D4 | opt | F4 |
| COMP-N2 = D5 | opt | F5 |
| COMP-N3 = D6 | opt | F6 |
| COMP-N4 = D7, N-C4 | opt / record | F7 |
| N-C1 = D8 | opt | F8 |
| COMP-N5, N-C5 = D10 | record | F9 |
| COMP-N6 = D9 | record | F10 |

## F1 (COMP-E1; §C D1, C.2). |𝒫| is the number of transitions
- Note, verbatim (REFEREE §8): «COMP-E1 (E-item, §1): define |𝒫| := #{t : t, t + 1 ∈ 𝒫} (transitions). Under "states" the phase part of Theorem
  COMPOSE is false.»
- Appended text (definition line, to be read at the end of §1's «Symbols.» item): «For a stretch R of consecutive states (a phase, a λ-run,
  a λ^U-run, a whole run), |R| := #{t : t, t + 1 ∈ R}, the number of TRANSITIONS inside R (one less than its number of states). In
  particular |𝒫| in Theorem COMPOSE and «transitions (iterations)» in Corollary COMPOSE-RUN count transitions.»
- Why this is what the packet proves: Theorem COMPOSE's proof bounds the transitions of 𝒫 («every transition of 𝒫 changes σ, i.e. contains an
  Even switch»), and chg/compose.py's L = j − i is the transition count (both checkers computed it so: REFEREE «compose.py's L = j − i»,
  REFEREE-2 «b − a»).

## F2 (N-C2; §C D2). LEN-MONO and Theorem COMPOSE hold on any stretch with λ (λ^U) constant
- Note, verbatim (REFEREE-2 §4): «N-C2 (LEN-MONO / COMPOSE scope). The proofs need only "λ constant on R", not maximality. Theorem COMPOSE's
  phase statement applies LEN-MONO to a phase, which is a sub-stretch of a λ-run. Say "any stretch with λ (λ^U) constant" in LEN-MONO and
  Theorem COMPOSE. One word.»
- Appended text (§3 and §4): «In Lemma LEN-MONO and in Theorem COMPOSE's first statement, "every λ-run R" is to be read as "every stretch R of
  consecutive states on which λ is constant" (dually λ^U); a λ-run and a phase are such stretches. The proofs use only that λ is constant on
  R (§3: "On R the cycle node of Ξ_t(c) is a fixed vertex c₀ (λ constant)"), never maximality. Theorem COMPOSE's phase statement is the first
  statement applied to the stretch 𝒫, with RISE_𝒫, PCH_𝒫 counted inside 𝒫.»
- Why it matters (REFEREE-2 §C D2): applying the λ-run bound to the enclosing λ-run gives PCH_R, not PCH_𝒫; the phase statement as written
  uses the stretch form. REFEREE §4 applies it the same way.

## F3 (N-C3; §C D3). Odd side: MATCHED / CARRY / NM^U with G^d's parities
- Note, verbatim (REFEREE-2 §4): «N-C3 (§6, Odd side). For λ^U-runs on G^d, MATCHED / CARRY / NM^U are read with G^d's parities (Ω + 1, same
  ranks). "NM* over both players" should say so. The bound holds because MATCH-Φ is parity-agnostic. My check reads them that way: NM_O, 0
  violations.»
- Appended text (§6, after «(over both players)»): «On Odd's side (λ^U-runs of U on G^d), P-changes, MATCHED, CARRY and the carry count NM^U
  are read on G^d, i.e. with G^d's parities (Ω + 1; the ranks are those of G). NM* in the Corollary is max(NM*_Even, NM*^U).»
- chg/compose.py MODE=run already computes the Odd side on G^d (Ed = Engine(dual(g))), so the packet's §7 data are of this reading.

## F4 (COMP-N1; §C D4, opt). P*^U in the title
- Note, verbatim (REFEREE §8): «COMP-N1: the title defines P* but its formula also uses P*^U.»
- Appended text: «In the title, P*^U is the largest number of P-changes of one vertex's dual valuation U (Odd's valuation of τ on G^d) inside
  one λ^U-run, as defined in §1 ("P*^U likewise over λ^U-runs").»

## F5 (COMP-N2; §C D5, opt). RISE counts changes, which are rises
- Note, verbatim (REFEREE §8): «COMP-N2: SW-RETURN's RISE_R(c) counts CHANGES of Ξ(c); by F-MON they are rises. Say so where RISE is defined (the
  name suggests it, the definition says ≠).»
- Appended text (§1, at RISE_R's definition): «RISE_R(c) counts the transitions of R at which Ξ(c) CHANGES; by (F-MON) every such change is a
  strict rise (Ξ_{t+1}(c) ▷ Ξ_t(c)), which is why it is called RISE. RISE^U likewise with U on G^d.»

## F6 (COMP-N3; §C D6, opt). The set I in (F-MON)
- Note, verbatim (REFEREE §8): «COMP-N3: F-MON's "I is unambiguous: σ_{t+1} is a strategy" — say that I := {(v, σ_{t+1}(v)) : σ_{t+1}(v) ≠ σ_t(v)}
  ⊆ Iσ_t by F-SW (the link from S4a's arena to R15 (d)'s "Switch_I with I ⊆ Iσ" is [STEP] itself; one clause).»
- Appended text (§1, (F-MON)): «Here I := {(v, σ_{t+1}(v)) : σ_{t+1}(v) ≠ σ_t(v)}, and I ⊆ Iσ_t by (F-SW); σ_{t+1} = Switch_I(σ_t), the form in
  which [MON] (R15 (a)) is stated.»

## F7 (COMP-N4 and N-C4; §C D7). Status of [MΦ] on λ-runs
- Notes, verbatim. REFEREE §8: «COMP-N4 (§6 note): the λ-run reading of [MΦ] is now confirmed by the first referee twice (R-N5-MPGS §1b, here
  §6); it can be stated as a remark of the landed MPGS entry rather than an assumption.» REFEREE-2 §4: «N-C4 (§6 status). [MΦ] is signed by
  REFEREE-2 (record: R2-N5-MPGS.md, successor 19). REFEREE's MPGS report is not yet out (name count 0 at 11:54Z). So §6 stays an
  implication until [MΦ] lands, as the packet labels it.»
- Update (REFEREE §C C5): «[MΦ] is now SIGNED by both referees with an empty joint map (R-N5-MPGS §C 8da7b717, R2-N5-MPGS 0c4524f0); §6 can land
  as "COMPOSE-RUN with [MΦ] (R85-or-whichever entry) gives …", the λ-run transfer as a referees' remark.»
- No change to the frozen packet, because §6 is signed as an implication by both referees. Appended text (§6): «[MΦ] is signed by both
  referees (R-N5-MPGS §C 8da7b717, R2-N5-MPGS 0c4524f0); its λ-run reading is confirmed by both (REFEREE §6 and R-N5-MPGS §1b; REFEREE-2 §2.5
  and R2-N5-MPGS-C). When P-N5-MPGS lands, §6's premise is that entry plus this referees' remark, and §6's conclusion holds with it.» The
  ordering of the two RESULTS entries is the Lead's / CHECKER's.

## F8 (N-C1; §C D8, opt). The [MΦ] quote
- Note, verbatim (REFEREE-2 §4): «N-C1 (quote form). [MΦ]'s quote joins MPGS l. 97 and 98 with "…" and drops "**". The lane's checker accepts
  it; my strict one does not. The content is faithful. This is the recurring "… over a line break" theme; quote the two lines separately.»
- No change to the frozen packet (its quote passes the lane's checker and is content-faithful, both referees). Lane practice from this
  packet on: a quote spanning two source lines is given as two separate quotes, with markup kept.

## F9 (COMP-N5, N-C5; §C D10). Slack figures (DATA)
- Notes, verbatim. REFEREE §8: «COMP-N5 (slack, DATA): Σ SW / Σ(1 + RISE) = 0.10 overall on the library, 0.28 on random games; the factor n of
  LEN-MONO and MΦ's n²/2 are the loose links, as §7's READING says.» REFEREE-2 §4: «N-C5 (READING §7 "L/S1 ≤ 1, S1/S2 ≤ 0.75 per phase"). My max
  S1/S2 is 0.8 on lib41 λ^U-runs (Odd side on λ^U-runs, not phases). That is not the packet's quantity, so there is no conflict. Noted because
  the packet's 0.75 is a per-phase Even figure.»
- No change, because §7 is DATA (not signed) and the three figures are different statistics (overall ratio; per-phase Even maximum; per
  λ^U-run Odd maximum), as §C D10 says. Recorded: the per-λ^U-run Odd maximum of S1/S2 is 0.8 (REFEREE-2, lib41).

## F10 (COMP-N6; §C D9). F-MON on Odd's side
- Note, verbatim (REFEREE §8): «COMP-N6 (premise): F-MON on the Odd side is [MON] applied to G^d, as in R47's Lemma Φ (b) citation chain
  (PHI-N1 = N-PHI-2); no new premise.»
- No change, because the packet's (F-MON) already says «Dually» for Odd on G^d, and both referees read it as [MON] on G^d with no new premise.

## DONE / FINDINGS / NEEDS
- DONE: F1-F10 (appended text for COMP-E1, N-C2, N-C3 (E) and COMP-N1, COMP-N2, COMP-N3 (opt); «no change, because …» for COMP-N4/N-C4, N-C1,
  COMP-N5/N-C5, COMP-N6). Packet sha1 e1b977aa… unchanged.
- FINDINGS: no signed statement changes; COMP-E1's definition (|R| = transitions) is what the proof and both checkers use.
- NEEDS: none from the owner.

## Appended by successor 26 (2026-10-29T13:34Z by date -u (13:34:15); Lead brief 13:15Z): F11-F14, quote pins, quote check
F1-F10 above are unchanged. The items below cover what F1-F10 left without an F-item: the definition line in the Lead's form, REFEREE's
re-worded §C C5 (claude/referee 1680010b, after F7 quoted c6011b70), REFEREE §C C11 = REFEREE-2 §C D11, and REFEREE-2 §C D12.

## F11 (COMP-E1, report §1 wording; Lead 13:15Z). The definition line
- Note, verbatim (REFEREE §1): «COMP-E1 (E-item). |𝒫| (§4) is used but never defined. It must be the number of TRANSITIONS t → t + 1 with t, t + 1 ∈ 𝒫 (compose.py's L = j − i).»
- Appended text (definition line; same content as F1, in the form the Lead asked for): «|𝒫| := number of transitions t → t + 1 with t, t + 1 ∈ 𝒫.»
  Read as the number of states, the phase part is FALSE (REFEREE §1: a one-state phase gives 1 ≤ 0).
- Lead ruling on the class difference (Lead 13:43Z by date -u, verbatim): «REFEREE-2's D2 (N-C2: "any stretch with λ (λ^U) constant")
  and D3 (N-C3: Odd side read on G^d) are REQUIRED appended items, the conservative reading.» So F2 and F3 are REQUIRED items (class E);
  they stay as written.

## F12 (REFEREE §C C5, re-worded at 1680010b)
- Note, verbatim (REFEREE §C C5 at 1680010b): «UPDATED: [MΦ] is now SIGNED by both referees with an empty joint map (R-N5-MPGS §C 8da7b717, R2-N5-MPGS 0c4524f0); §6 can land as "COMPOSE-RUN with [MΦ] (citing the landed MPGS entry) gives …", the λ-run transfer as a referees' remark.»
- No change, because F7's appended text names no RESULTS entry; it already says «When P-N5-MPGS lands, §6's premise is that entry plus this
  referees' remark». F7's «Update» quote is the c6011b70 wording («R85-or-whichever entry»); the current wording is the one above.

## F13 (REFEREE §C C11 = REFEREE-2 §C D11). Is the λ-constant restriction of LEN-MONO needed?
- Notes, verbatim. REFEREE §C C11: «OPEN in data, not a finding (the proof uses it; LEN-MONO across a λ-change compares different cycle nodes)».
  REFEREE-2 §C D11: «Complementary. REFEREE shows the phase restriction is needed; neither shows the λ restriction of LEN-MONO is needed».
- No change, because the packet states and proves LEN-MONO only on stretches with λ constant (F2), which is all that Theorem COMPOSE uses.
  Recorded as OPEN (data): LEN-MONO across a λ-change (X_LENfull) did not bite in REFEREE-2's control; no proof and no counterexample.

## F14 (REFEREE-2 §C D12). Data scale
- Note, verbatim (REFEREE-2 §C D12): «REFEREE: 10,778 runs (763 library + 15 pins + 6,000 + 4,000 random), Odd-side λ^U NM data new.»
- No change, because §7 is DATA. Recorded: REFEREE's §C says «mine 6,778 runs»; the two figures differ by REFEREE's 4,000 MPHI runs (its
  report table: 763 + 15 + 6,000 runs for the COMPOSE control, plus 4,000 runs of the MPHI control). Lane reading; no conflict.

## Quote pins (every verbatim note above, with its source lines)
Check: `python3 -I docs/si/P-N5-COMPOSE-fixes-quotecheck.py` from the repository root. Each pinned quote must (a) equal, whitespace
collapsed, a substring of lines a..b of the source at the commit, and (b) occur, whitespace collapsed, in this file above this section.
- [Q docs/referee/R-N5-COMPOSE.md@4896bc2e:116-116] «COMP-E1 (E-item, §1): define |𝒫| := #{t : t, t + 1 ∈ 𝒫} (transitions). Under "states" the phase part of Theorem COMPOSE is false.»
- [Q docs/referee-2/R2-N5-COMPOSE.md@4b8afa95:168-169] «N-C2 (LEN-MONO / COMPOSE scope). The proofs need only "λ constant on R", not maximality. Theorem COMPOSE's phase statement applies LEN-MONO to a phase, which is a sub-stretch of a λ-run. Say "any stretch with λ (λ^U) constant" in LEN-MONO and Theorem COMPOSE. One word.»
- [Q docs/referee-2/R2-N5-COMPOSE.md@4b8afa95:170-171] «N-C3 (§6, Odd side). For λ^U-runs on G^d, MATCHED / CARRY / NM^U are read with G^d's parities (Ω + 1, same ranks). "NM* over both players" should say so. The bound holds because MATCH-Φ is parity-agnostic. My check reads them that way: NM_O, 0 violations.»
- [Q docs/referee/R-N5-COMPOSE.md@4896bc2e:117-117] «COMP-N1: the title defines P* but its formula also uses P*^U.»
- [Q docs/referee/R-N5-COMPOSE.md@4896bc2e:118-118] «COMP-N2: SW-RETURN's RISE_R(c) counts CHANGES of Ξ(c); by F-MON they are rises. Say so where RISE is defined (the name suggests it, the definition says ≠).»
- [Q docs/referee/R-N5-COMPOSE.md@4896bc2e:119-120] «COMP-N3: F-MON's "I is unambiguous: σ_{t+1} is a strategy" — say that I := {(v, σ_{t+1}(v)) : σ_{t+1}(v) ≠ σ_t(v)} ⊆ Iσ_t by F-SW (the link from S4a's arena to R15 (d)'s "Switch_I with I ⊆ Iσ" is [STEP] itself; one clause).»
- [Q docs/referee/R-N5-COMPOSE.md@4896bc2e:121-122] «COMP-N4 (§6 note): the λ-run reading of [MΦ] is now confirmed by the first referee twice (R-N5-MPGS §1b, here §6); it can be stated as a remark of the landed MPGS entry rather than an assumption.»
- [Q docs/referee-2/R2-N5-COMPOSE.md@4b8afa95:172-173] «N-C4 (§6 status). [MΦ] is signed by REFEREE-2 (record: R2-N5-MPGS.md, successor 19). REFEREE's MPGS report is not yet out (name count 0 at 11:54Z). So §6 stays an implication until [MΦ] lands, as the packet labels it.»
- [Q docs/referee/R-N5-COMPOSE.md@c6011b70:151-151] «[MΦ] is now SIGNED by both referees with an empty joint map (R-N5-MPGS §C 8da7b717, R2-N5-MPGS 0c4524f0); §6 can land as "COMPOSE-RUN with [MΦ] (R85-or-whichever entry) gives …", the λ-run transfer as a referees' remark.»
- [Q docs/referee-2/R2-N5-COMPOSE.md@4b8afa95:166-167] «N-C1 (quote form). [MΦ]'s quote joins MPGS l. 97 and 98 with "…" and drops "**". The lane's checker accepts it; my strict one does not. The content is faithful. This is the recurring "… over a line break" theme; quote the two lines separately.»
- [Q docs/referee/R-N5-COMPOSE.md@4896bc2e:123-124] «COMP-N5 (slack, DATA): Σ SW / Σ(1 + RISE) = 0.10 overall on the library, 0.28 on random games; the factor n of LEN-MONO and MΦ's n²/2 are the loose links, as §7's READING says.»
- [Q docs/referee-2/R2-N5-COMPOSE.md@4b8afa95:174-175] «N-C5 (READING §7 "L/S1 ≤ 1, S1/S2 ≤ 0.75 per phase"). My max S1/S2 is 0.8 on lib41 λ^U-runs (Odd side on λ^U-runs, not phases). That is not the packet's quantity, so there is no conflict. Noted because the packet's 0.75 is a per-phase Even figure.»
- [Q docs/referee/R-N5-COMPOSE.md@4896bc2e:125-125] «COMP-N6 (premise): F-MON on the Odd side is [MON] applied to G^d, as in R47's Lemma Φ (b) citation chain (PHI-N1 = N-PHI-2); no new premise.»
- [Q docs/referee/R-N5-COMPOSE.md@4896bc2e:31-31] «COMP-E1 (E-item). |𝒫| (§4) is used but never defined. It must be the number of TRANSITIONS t → t + 1 with t, t + 1 ∈ 𝒫 (compose.py's L = j − i).»
- [Q docs/referee/R-N5-COMPOSE.md@1680010b:151-151] «UPDATED: [MΦ] is now SIGNED by both referees with an empty joint map (R-N5-MPGS §C 8da7b717, R2-N5-MPGS 0c4524f0); §6 can land as "COMPOSE-RUN with [MΦ] (citing the landed MPGS entry) gives …", the λ-run transfer as a referees' remark.»
- [Q docs/referee/R-N5-COMPOSE.md@1680010b:157-157] «OPEN in data, not a finding (the proof uses it; LEN-MONO across a λ-change compares different cycle nodes)»
- [Q docs/referee-2/R2-N5-COMPOSE.md@ee549524:225-225] «Complementary. REFEREE shows the phase restriction is needed; neither shows the λ restriction of LEN-MONO is needed»
- [Q docs/referee-2/R2-N5-COMPOSE.md@ee549524:226-226] «REFEREE: 10,778 runs (763 library + 15 pins + 6,000 + 4,000 random), Odd-side λ^U NM data new.»
- [Q docs/referee/R-N5-COMPOSE.md@1680010b:141-141] «mine 6,778 runs»

## DONE / FINDINGS / NEEDS (successor 26)
- DONE: F11-F14 appended; 19 quote pins; docs/si/P-N5-COMPOSE-fixes-quotecheck.py (quotes=19 bad=0; a mutated quote gives bad=1, check.sh).
  F1-F10 and the frozen packet (sha1 e1b977aa…) unchanged.
- FINDINGS: every verbatim note in F1-F10 is a literal substring of the referee report at its commit; F7's C5 quote is the pre-1680010b
  wording (F12). No signed statement changes.
- NEEDS: none from the owner.
