# P-N5-CHOSEN fixes (box 19 packet; repairs only)
L-SI successor 16 (Opus 5.5; D15, D18, L37, L40). Written at the Lead's request of 15:08Z and 15:22Z (Lead's stamps), after both §Cs. Stamp:
the commit (date -u).
- Object: docs/si/P-N5-CHOSEN-box19.md, sha1 764cfbb331a1aaefa819a01d64ee6b7cfbbd7316 (l-si b7189738). FROZEN, not edited.
- Repairs only. This file adds no lemma and changes no signed statement. Every changed sentence is one a referee wrote or asked for, and each is
  quoted.
- Sources (file sha1 by `git show <commit>:<path> | sha1sum`; all on trunk 539b4192):
  - REFEREE successor 15, docs/referee/R-N5-CHOSEN.md: report at referee b3473114 (file sha1 a4f973d9…), n ≤ 40 data added at e49bf11a, §C at
    d08011be (dc0a3298…).
  - REFEREE-2 successor 17, docs/referee-2/R2-N5-CHOSEN.md: report at referee-2 aab45be6 (7f4fd3ed…), §C at bde1ea77 (9f07abde…).
- Quotes. Every «…» below is verbatim. Its tag [Q path@commit:lines] gives the source, and experiments/si/rund/quotecheck.py checks each one
  against `git show commit:path` at those lines (whitespace normalised; "…" inside a quote separates parts, and each part must occur).
  `python3 -I experiments/si/rund/quotecheck.py docs/si/P-N5-CHOSEN-fixes-box19.md` prints QUOTES PASS (pinned in experiments/si/check.sh).

## Verdicts (joint)
- REFEREE §C: [Q docs/referee/R-N5-CHOSEN.md@d08011be:143] «Verdicts identical up to the discharged condition. Joint gap map: EMPTY.»
- REFEREE-2 §C: [Q docs/referee-2/R2-N5-CHOSEN.md@bde1ea77:176-178] «No disagreement. Joint gap map: EMPTY. Notes to the lane (union): CHOSEN-N1 =
  N-CHOSEN-4, CHOSEN-N2, CHOSEN-N3 + N-CHOSEN-3, CHOSEN-N4, CHOSEN-N5 = N-CHOSEN-6, N-CHOSEN-1, N-CHOSEN-2, N-CHOSEN-7. N-CHOSEN-5 (premise
  status) is closed by R69's landing. My verdicts are unchanged except that TV-END's condition is lifted.»
- TV-END: [Q docs/referee/R-N5-CHOSEN.md@d08011be:141] «SIGNED: the condition is discharged, R69 (c) landed at trunk a7c141b8».
- Consequence (a): [Q docs/referee/R-N5-CHOSEN.md@d08011be:139] «SIGNED; the parenthetical is a READING».
- So §2 Lemma CHOSEN, §3 Corollary RELAY-CHAIN and its consequences (a) (without its parenthetical) and (b), and §4 Lemma TV-END are SIGNED by
  both, with no gap. §5 was not reviewed, as the packet asked.

## F1. CHOSEN-N1 = N-CHOSEN-4: the identity at t (wording; §2, first proof bullet)
- Packet text: [Q docs/si/P-N5-CHOSEN-box19.md@b7189738:56-57] «By R56 (d) at t (and its "≥" half, i.e. σ̄_t attains the minimum, P1): κ_t(q) =
  κwt_c(q) + κ_t(y*).»
- REFEREE: [Q docs/referee/R-N5-CHOSEN.md@b3473114:118-119] «κ_t(q) = κwt_c(q) + κ_t(y*) is the play decomposition (no half of R56 (d)
  needed); the step that needs optimality is R56 (d)'s "≤" half at t + 1 (Lemma S (a), every game). Relabel the parenthetical.»
- REFEREE-2: [Q docs/referee-2/R2-N5-CHOSEN.md@aab45be6:109-110] «κ_t(q) = κwt_c(q) + κ_t(y*) is one-step additivity (Aκ), not R56 (d) with P1;
  R56 (d) is needed only for the "⪯" step at t + 1.»
- Repaired bullet: "y* ∈ U_c, and y*'s play at t avoids q, so y* ∈ Y^q_t. Since σ̄_t(q) = y* and q is on no honest cycle at t, one-step
  additivity (Aκ) (the play decomposition) gives κ_t(q) = κwt_c(q) + κ_t(y*). R56 (d) (its "≤" half, Lemma S (a)) is used only at t + 1."
  The proof's later step "R56 (d) at t + 1" is unchanged.

## F2. N-CHOSEN-2: add e ≠ q to CHOSEN's statement (wording; §2 statement)
- Packet text: [Q docs/si/P-N5-CHOSEN-box19.md@b7189738:54] «Statement. e ≠ c, and either κ_t(e) ≠ κ_{t+1}(e)».
- REFEREE-2: [Q docs/referee-2/R2-N5-CHOSEN.md@aab45be6:104-106] «CHOSEN concludes "e ≠ c", but RELAY-CHAIN needs e ∈ Q_c ∖ {q}. e ≠ q follows from
  the same hypothesis (e = q means y*'s play returns to q, so q is on an honest cycle at t), and the chain's "e_{i+1} ∈ Q_c ∖ {e_i}" silently
  uses it. Add "and e ≠ q" to CHOSEN's statement.»
- REFEREE-2 §C (matched row; REFEREE had derived it in its own §2): [Q docs/referee-2/R2-N5-CHOSEN.md@bde1ea77:171] «e ≠ q to be stated in CHOSEN | derived in its §2 ("Also e ≠ q"), no note | N-CHOSEN-2».
- Repaired statement: "e ≠ c and e ≠ q, and either κ_t(e) ≠ κ_{t+1}(e) (e has a ρ event at t → t+1), or e's honest play at t + 1 passes
  through q (TOG)." Proof of e ≠ q as REFEREE-2 wrote it.

## F3. CHOSEN-N2: consequence (a)'s parenthetical is a READING, not signed
- Packet text: [Q docs/si/P-N5-CHOSEN-box19.md@b7189738:79-80] «(This is the stronger, per-event form of ROOT-C's consequence, which only asks for
  a changed class exit path or exit.)»
- REFEREE: [Q docs/referee/R-N5-CHOSEN.md@b3473114:120-122] «is not an implication (CYC and TOG ends name no changed class exit path); (a) is
  P-N5-FLIP's CONJECTURE ROOT-C (strong form) proved up to the TOG alternative. Reword; I sign (a) without the parenthetical.»
- Repair: the parenthetical is withdrawn from the signed text. READING (not signed), in REFEREE's words: (a) is P-N5-FLIP's CONJECTURE ROOT-C
  (strong form) proved up to the TOG alternative.

## F4. CHOSEN-N3 + N-CHOSEN-3: consequence (b)'s counting sentence (compatible wordings, both adopted)
- Packet text: [Q docs/si/P-N5-CHOSEN-box19.md@b7189738:81-83] «Here ROUTE_c, CYC_c are the ROUTE, CYC events in the class, and TOG_c the RELAY
  events ending in a TOG step. Each RELAY event is mapped to the end of its sequence, at the same transition, and at most |Q_c| events map to
  one end.»
- REFEREE: [Q docs/referee/R-N5-CHOSEN.md@b3473114:123] «TOG_c counts RELAY events, not chain ends, so Σ_q ρ_q ≤ |Q_c|(ROUTE_c + CYC_c) + TOG_c;
  the stated bound holds a fortiori.»
- REFEREE-2: [Q docs/referee-2/R2-N5-CHOSEN.md@aab45be6:107-108] «The map must cover ROUTE and CYC events too (each is its own end); as written only
  the RELAY events are mapped, while the left side counts all events. One sentence, no change to the inequality.»
- Repaired sentence: "Each ROUTE or CYC event is its own end; each RELAY event is mapped to the end of its sequence, at the same transition, and
  at most |Q_c| events map to one end. Since TOG_c counts RELAY events ending in a TOG step, also Σ_q ρ_q ≤ |Q_c|(ROUTE_c + CYC_c) + TOG_c; the
  stated bound holds a fortiori." The signed inequality is unchanged.

## F5. CHOSEN-N4: notation in TV-END (ii)
- Packet text: [Q docs/si/P-N5-CHOSEN-box19.md@b7189738:99] «By additivity and κ_t(e) = κ_Θ(e)».
- REFEREE: [Q docs/referee/R-N5-CHOSEN.md@b3473114:124] «κ_Θ(e) for e = c means κ(c) = (0, 0); say so.»
- Repair (as written): "for e = c, κ_Θ(c) := κ(c) = (0, 0), constant on the phase."

## F6. CHOSEN-N5 = N-CHOSEN-6: the §5 DATA sentence (DATA; not signed text)
- Packet text: [Q docs/si/P-N5-CHOSEN-box19.md@b7189738:120] «CHOSEN / RELAY-CHAIN: 0 violations, TOG never occurs.»
- Joint wording: [Q docs/referee/R-N5-CHOSEN.md@d08011be:148] «joint wording: "no RELAY chain ends in a TOG step; the TOG alternative is never the
  only one" (in both referees' data)».
- REFEREE-2: [Q docs/referee-2/R2-N5-CHOSEN.md@aab45be6:114-115] «TOG as CHOSEN's second alternative DOES occur: 241 RELAY events in my runs have q
  on the chosen exit's honest play at t + 1».
- Repaired DATA sentence: "CHOSEN / RELAY-CHAIN: 0 violations; no RELAY chain ends in a TOG step; the TOG alternative is never the only one
  (TOG cases occur, always together with a ρ event at e: REFEREE 130, REFEREE-2 241)." Also, per the second half of N-CHOSEN-6 and REFEREE's
  matched row, the packet's "TV-END is THIN" is an artefact of its R56 (g) trigger: [Q docs/referee/R-N5-CHOSEN.md@d08011be:149] «same: the
  packet's "THIN" is an artefact of its R56 (g) trigger». My script tvend.py tests the fallback-count trigger only (note §27.3); the referees
  tested (H) directly.

## F7. Notes taken as written (no change to the packet's text)
- N-CHOSEN-1 (quotes): [Q docs/referee-2/R2-N5-CHOSEN.md@aab45be6:101-103] «9 tagged quotes, all verbatim at the tagged commits and lines (own
  script).» (the note goes on: one guillemet quote in the packet's §1 has no tag of its own). Accepted: in this fixes file every quote carries its own tag.
- N-CHOSEN-5 (premise status of TV-END): closed by R69's landing (REFEREE-2 §C, quoted under Verdicts).
- N-CHOSEN-7 (SELF-FREE cross-check: 0 RELAY events on 503 𝒞^1O files): data, confirms P-N5-FLIP's signed Corollary SELF-FREE; no change.
