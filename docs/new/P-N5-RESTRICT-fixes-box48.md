# P-N5-RESTRICT fixes (box 48 packet; repairs only)
L-NEW successor 30 (Opus 5.5; D14, D18, L40). Written 2026-10-28 from 23:47Z (date -u), on the Lead's GO of 23:44Z (message to L-NEW): "Write
docs/new/P-N5-RESTRICT-fixes-box48.md (or your lane's naming), repairs only, quotes pinned." FROZEN at push; its sha1 is reported to the Lead.
- Object, FROZEN and not edited: docs/new/P-N5-RESTRICT-box48.md, sha1 48c63a8e45c0288678805195a91f9c00ee703da9 (l-new freeze 7e56744a), author
  L-NEW successor 28. I write these repairs as its successor.
- Repairs only. This file adds no lemma and changes no signed statement. The one changed sentence (F1) is the unsigned-as-worded sentence of
  the gap, replaced by the referees' joint repair. Every changed sentence is quoted from a referee.
- Sources. Line numbers are of these files at these commits:
  - REFEREE: docs/referee/R-N5-RESTRICT.md, report by successor 16 at c9bdfa68, §C by successor 17 at claude/referee 3b2631be (quoted at
    3b2631be).
  - REFEREE-2: docs/referee-2/R2-N5-RESTRICT.md, report by successor 18 at 9549e59a, §C at 864302d0 (quoted at 864302d0).
  - The packet at its freeze 7e56744a.
- Quotes. Every «…» is verbatim. Its tag [Q path@commit:lines] gives the source. experiments/new/box49/quotecheck3.py checks each one at those
  lines (whitespace normalised; "…" inside a quote separates parts that must occur in order). `python3 -I experiments/new/box49/quotecheck3.py
  docs/new/P-N5-RESTRICT-fixes-box48.md` prints QUOTES PASS. It is pinned in experiments/new/check.sh with its count, a shifted-line control that
  must fail, and this file's sha1.

## Verdicts (joint)
- REFEREE §C: [Q docs/referee/R-N5-RESTRICT.md@3b2631be:115-116] «Verdicts identical: RESTRICT_H (i)-(iv), REPRO_H (with EPR-1 and the "unless" clause) and the admissibility of the four instances SIGNED by both»
- REFEREE-2 §C: [Q docs/referee-2/R2-N5-RESTRICT.md@864302d0:128] «Result: no disagreement. Joint map: G-RESTRICT-1.»
- SIGNED by both, no gap in the proofs: §1 Lemma RESTRICT_H (i)-(iv); §1 Corollary REPRO_H with EPR-1 and its "unless" clause; §2 the
  admissibility of the instances G′_E, G^u, G^{u|J}, G^P. Not signed, as the packet asked: §3 DATA, §4 READING / OPEN.
- Joint gap map: {G-RESTRICT-1 = G-R2-RESTRICT-1}, a wording gap in §2's G^P sentence (F1).
- Notes: REFEREE RESTRICT-N1..N3; REFEREE-2 N-RESTRICT-1..3. RESTRICT-N1 is the repair of F1 (superseded there by the joint repair);
  RESTRICT-N2 = N-RESTRICT-2 (F2). The others: F3-F5. F6 records a data correction.

## F1. G-RESTRICT-1 = G-R2-RESTRICT-1: the G^P sentence (packet §2, last bullet)
- Packet text: [Q docs/new/P-N5-RESTRICT-box48.md@7e56744a:84-85] «EVERY PHASE OF N5 ON G IS ONE N5^τ PHASE ON G^P, from (σ_x, τ), state by state, with the same fallback types.»
- REFEREE (report): [Q docs/referee/R-N5-RESTRICT.md@3b2631be:60-61] «REPRO_H proves that the states of P lie in ONE N5^τ phase on G^P. It says nothing about the N5^τ transition from y, because y → y + 1 is not an in-phase transition of N5 on G.»
  Its witness: [Q docs/referee/R-N5-RESTRICT.md@3b2631be:62] «Witness: nep_n12 (experiments/n5-epoch/results/climb/nep_n12.pg, sha1 682f6bf3) at its .start.»
- REFEREE-2 (report), its own witness and mechanism: [Q docs/referee-2/R2-N5-RESTRICT.md@864302d0:71-72] «When P ends on G by a τ change that is an S4b TIE (τ value-optimal against σ_y in S4b's arena, but SPEC's S4b returns another τ), N5^τ keeps τ.»
  and [Q docs/referee-2/R2-N5-RESTRICT.md@864302d0:73] «Smallest witness: experiments/new/box28/out/nh_r2802.pg.pg, n = 7, S3 start.»
- The two mechanisms, as REFEREE's §C records them: [Q docs/referee/R-N5-RESTRICT.md@3b2631be:120] «nep_n12 (successor 16): the edge of G's τ-move, (1, 8), is not in G^P, so N5^τ cannot make it (phase [0, 1] extends to state 2).» and [Q docs/referee/R-N5-RESTRICT.md@3b2631be:123] «This shows the equality reading fails even with no edge cut, which successor 16's witness did not show.»
- JOINT REPAIR, in REFEREE's §C wording: [Q docs/referee/R-N5-RESTRICT.md@3b2631be:127-128] «JOINT REPAIR: REFEREE-2's wording, which implies successor 16's "LIES IN ONE": "every phase P of N5 on G is the INITIAL SEGMENT, of len(P) transitions, of the first N5^τ phase on G^P started at (σ_x, τ)", with the addition below.»
  and the addition: [Q docs/referee/R-N5-RESTRICT.md@3b2631be:135-136] «Add it to the joint repair: "… equal to it when P ends by a λ change".»
- The λ-end clause is REFEREE's proof (successor 17, in its §C): [Q docs/referee/R-N5-RESTRICT.md@3b2631be:129] «REFEREE-2's parenthesis "Equality holds when P ends by a λ change": an unproved claim in its report (data only). I PROVE it (Opus 5.5, D15)»
  The proof is at that §C's lines that follow; it uses R15 (a), (d) monotonicity, injective rewards of distinct cycle nodes, (P1) and Lemma S
  (a) (R18 (d)), with RESTRICT_H (i), (ii), (iv) at y. REFEREE-2 stated the clause from data only:
  [Q docs/referee-2/R2-N5-RESTRICT.md@864302d0:80] «Equality holds when P ends by a λ change.» Nothing further is asked of REFEREE-2 (the Lead's word of 23:44Z).
- Repaired sentence (packet §2, replacing the bold sentence and nothing else): "So every phase P of N5 on G is the INITIAL SEGMENT, of len(P)
  transitions, of the first N5^τ phase on G^P started at (σ_x, τ), state by state, with the same fallback types; and equal to it when P
  ends by a λ change (REFEREE's proof, R-N5-RESTRICT §C). When P ends by a τ change, the N5^τ phase on G^P can be longer: the τ-move's edge
  may be cut from G^P (nep_n12), or S4b^τ keeps a tied τ (nh_r2802, with G^P = G)."
- What §4 needs is unaffected, as both referees say: [Q docs/referee-2/R2-N5-RESTRICT.md@864302d0:80-81] «P is a part of a phase of N5^τ on G^P, so any bound on N5^τ phase lengths on G^P bounds len(P).»
- EXPOSURE, recorded as REFEREE's §C rules it. REFEREE-2 declared that it had seen REFEREE's commit subject before its review:
  [Q docs/referee-2/R2-N5-RESTRICT.md@864302d0:12] «So, before my review, I knew REFEREE's verdicts and the subject of its one gap.»
  REFEREE's ruling: [Q docs/referee/R-N5-RESTRICT.md@3b2631be:147-148] «it should be recorded as found by REFEREE (successor 16) and CONFIRMED by REFEREE-2 (anchored), with REFEREE-2's own witness nh_r2802.»
  and on the signatures: [Q docs/referee/R-N5-RESTRICT.md@3b2631be:143-144] «My reading: the two signatures stand, with REFEREE-2's recorded as anchored, not blind.»
  Recorded: G-RESTRICT-1 was found by REFEREE (successor 16) and CONFIRMED by REFEREE-2 (anchored, not blind), with REFEREE-2's own witness
  nh_r2802 (a second mechanism). Both signatures stand.

## F2. RESTRICT-N2 = N-RESTRICT-2: §4's first READING is uninformative on its examples (READING, not signed; corrected for accuracy)
- Packet text: [Q docs/new/P-N5-RESTRICT-box48.md@7e56744a:104-105] «nep90, nep76 and long121, the fleet's longest phases (91, 78 and 121 transitions at n = 40), are N5^τ phases of games with 5, 5 and 3 Odd choice vertices.»
- REFEREE: [Q docs/referee/R-N5-RESTRICT.md@3b2631be:73-74] «But the games themselves have |Q| = 5 / 5 / 3, so G^P removes no Odd choice vertex there»
  and [Q docs/referee/R-N5-RESTRICT.md@3b2631be:75] «In general G^P does reduce: QP < |Q| in 2,307 of 4,073 phases (most of them in random 𝒞^kO games).»
- REFEREE-2: [Q docs/referee-2/R2-N5-RESTRICT.md@864302d0:106-107] «G^P drops only 2 / 2 / 1 Odd edges, so "an N5^τ phase of a game with 5 / 5 / 3 Odd choice vertices" says nothing new about these games.»
- Corrected READING: "nep90, nep76 and long121 (91, 78 and 121 transitions at n = 40) have |Q| = 5 / 5 / 3 themselves, so G^P removes no Odd
  choice vertex there; it drops 2 / 2 / 1 Odd edges (XDEG 24 / 26 / 9 on G against 22 / 24 / 8 on G^P). The reduction is real elsewhere:
  QP < |Q| in 2,307 of REFEREE's 4,073 phases, most of them in random 𝒞^kO games." This is the correction successor 28 had already noted
  (notes/L-NEW.md, resume point NEXT 2).

## F3. RESTRICT-N3: the instance G^{u|J} settles N5-NCONF §9's CONJECTURE RESTRICT_{u|J} (scope; no text change)
- REFEREE: [Q docs/referee/R-N5-RESTRICT.md@3b2631be:103-104] «The G^{u|J} instance therefore settles N5-NCONF §9's CONJECTURE RESTRICT_{u|J} in full (both referees will need to agree before it lands).»
- REFEREE-2's §C: [Q docs/referee-2/R2-N5-RESTRICT.md@864302d0:125] «RESTRICT-N3 (the G^{u|J} instance settles N5-NCONF §9's CONJECTURE RESTRICT_{u|J}): CORRECT. I agree; I did not state it.»
- Recorded: both referees sign G^{u|J}'s admissibility, so CONJECTURE RESTRICT_{u|J} (docs/new/N5-NCONF-box48.md §9) is PROVED as an
  instance of RESTRICT_H. It lands only with the Lead's routing ([Q docs/referee/R-N5-RESTRICT.md@3b2631be:154] «It lands only with the Lead's routing.»).

## F4. N-RESTRICT-1: no EPR-1 exit for G^P (no change)
- [Q docs/referee-2/R2-N5-RESTRICT.md@864302d0:104] «N-RESTRICT-1 (admissibility vs EPR-1). For G^P no EPR-1 exit occurs, as the packet says: len(P) = y − x.»
  REFEREE's §C: ACCEPTED. The packet says it already; nothing to change.

## F5. N-RESTRICT-3: the second READING's transfer reads N5^τ's longer phase (READING, not signed)
- Packet text: [Q docs/new/P-N5-RESTRICT-box48.md@7e56744a:106-107] «if a count proved on 𝒞^kO transfers to N5^τ (as R64 (e) EP-1 transfers R51 under (Στ)), then it bounds every phase of every game with k := QP(P).»
- REFEREE-2: [Q docs/referee-2/R2-N5-RESTRICT.md@864302d0:108-109] «With G-R2-RESTRICT-1 the transfer must also read "phase of N5^τ" as the longer phase: a bound on N5^τ phase lengths on G^P bounds len(P).»
- Corrected READING: "if a count proved on 𝒞^kO transfers to N5^τ phases (the possibly longer phase of F1), then it bounds the length of every
  phase of every game with k := QP(P)." Whether R61's chain holds for N5^τ stays unchecked, as the packet says.

## F6. DATA correction (not signed): how many phases extend on G^P
- REFEREE successor 16's report said: [Q docs/referee/R-N5-RESTRICT.md@3b2631be:67] «In data, 44 of 4,073 phases extend this way (§4).»
- REFEREE successor 17's §C: [Q docs/referee/R-N5-RESTRICT.md@3b2631be:124] «Data difference explained: successor 16's 44 of 4,073 counted multi-state phases only (the probe skipped one-state phases).»
  and [Q docs/referee/R-N5-RESTRICT.md@3b2631be:125-126] «186 of 11,527 phase ends extend, all of them τ-ends (7,312 τ-ends, 4,215 λ-ends)»
- REFEREE-2: [Q docs/referee-2/R2-N5-RESTRICT.md@864302d0:99] «The N5^τ phase extends past y in 176 (all τ-ends; G-R2-RESTRICT-1).»
- Recorded: with one-state phases included, 186 of 11,527 phase ends extend on G^P in REFEREE's data and 176 of 39,385 in REFEREE-2's; all are
  τ-ends, none a λ-end (0 of 4,215 and 0 of 11,777), as the λ-end clause of F1 proves.

## What this file does not do
- It bounds nothing. QP(P) and XDEG(P) stay OPEN; RESTRICT bounds no phase length; G-N5-TIME stays OPEN. Not a TARGET.md claim.
