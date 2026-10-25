# P-N5-NHN fixes (box 40 packet, filed in box 42): the referees' notes, written out
L-NEW successor 21 (Opus 5.5, D15/D18, L37/L40), session_01YJHHx1t8hvqkDnKzMU2Lfa. Written 2026-10-25 20:59Z by date -u, at the Lead's
request of 20:49Z (Lead's stamp): "GO for two fixes files ... repairs only; do not change any signed statement." Frozen once its sha1 is reported.
- Object: packet docs/new/P-N5-NHN-box40.md, sha1 da7d09ec6cb27ee8f7d94b857bc13fb2946aff1a (pinned trunk 0bb175d). The packet is NOT
  edited; this file is its correction layer, a record of the reports, not refereed text.
- Sources:
  - REFEREE: docs/referee/R-N5-NHN.md (referee 9bb3f79; §C 41b93026): all SIGNED, no gaps (§7 SIGNED with its stated conditions); notes
    NHN-N1 (citation), NHN-N2 (wording), NHN-N3 (data).
  - REFEREE-2: docs/referee-2/R2-N5-NHN.md (referee-2 04b5c1fd; §C a41f2c13): all SIGN; §7 HN-POLY-ALL SIGN CONDITIONAL as labelled;
    notes N-NHN-1 (citation), N-NHN-2 (statuses); its §C accepts NHN-N2.
  - Neither report has a gap, a NOT SIGNED item or a counterexample.
- Scope unchanged: lemmas about the candidate N5 on 𝒞^1O. Not a running-time bound, not a TARGET.md claim, not a step-4 pass.
  G-N5-TIME stays OPEN. The packet's §8 OPEN item (fallbacks at H1 ∧ H2 ∧ ¬H3 states in phases with no HN state) stays OPEN here.

## One line per note (source, kind, repair text)
| note | source | kind | repair text |
| --- | --- | --- | --- |
| NHN-N1 = N-NHN-1 = RHO-N2 | REFEREE §5, §7 (and R-N5-RHO RHO-N2); REFEREE-2 §5, §7; identical in both §Cs | citation, no gap | Wherever the packet cites "RESULTS R39 (f) (c)" for τ(o) = o (§0 table l. 55 "NE-COUNT (c)", §5 Remarks l. 122, §7 l. 134), read: "RESULTS R34 (e), with HN = H1 when τ(o) = o (or §5 (b)'s own argument with no EV2 end)". Reason: R39 (f) is headed "Corollary NE-COUNT (τ(o) = o, case A; θ a parameter)", so (c) is landed for case A only. The bound holds in case B too: τ(o) = o makes o's W-play its loop, so ¬H2 holds at every state and HN = H1; H1 runs alternate with ¬H1 runs, so N_HN ≤ ⌊T_ph/2⌋ + 1 (R34 (e), no case hypothesis). Data: REFEREE 30 τ(o) = o library phases with HN states (case A 17, case B 13); REFEREE-2 1,252 case-A and 1,885 case-B phases. |
| NHN-N2 | REFEREE §6; accepted by REFEREE-2 §C | wording | In §6's Consequence (l. 130), replace "(there H3 fails at every H2 state, and every ¬H2 state is ¬H1)" by "(in a phase that contains a Q state (H1 ∧ H2 ∧ ¬H3), H3 fails at every H2 state, by H3-CONST (RESULTS R33 (a)), and every ¬H2 state is ¬H1)". Reason: a phase with no HN state may still have H3 at every H2 state (then it has no Q state); "there" must mean "in a phase containing a Q state". |
| N-NHN-2 | REFEREE-2 §7, §8; REFEREE §C row (its verdict row lists the conditions with their status at its writing) | statuses | Read §0's "in review" / "REFEREE-2 10 to review" (l. 28-33, l. 58-59) as of trunk 4f94b452: P-N5-PFZ and P-N5-PFZ-ext are LANDED as RESULTS R44, P-N5-RHO as RESULTS R45 (both signed by both referees). BRK-POLY′ (i) as stated is now signed unconditionally with the PFZ-1 repair (R2-N5-PFZ §C, C.2; REFEREE-2 C.5, ea5cc217). §7 needs only (i′) and (ii), so HN-POLY-ALL's conditions are all met by landed results. |
| NHN-N3 | REFEREE §8 | data | T0-PIN and NHN-BOUND (a)'s late branch rest on their proofs (checked line by line, REFEREE §4, §5). The §5 bound is far from approached: max N_HN 4 against ⌈T/2⌉ + 2\|U\| − 3 in the hundreds. |

## Labels after this layer
- Every statement of P-N5-NHN is PROVED (L-NEW succ. 19 / 20; REFEREE, REFEREE-2). §7 HN-POLY-ALL's conditions (PFZ, PFZ-ext (i′)/(ii),
  RHO) are landed as R44 and R45, so HN-POLY-ALL holds with no open condition, given the citation repair NHN-N1.
