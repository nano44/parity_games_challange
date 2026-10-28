# P-N5-OFFMONO fixes (the box 49 unit: OFFMONO + add1 + add2 + add3; repairs only)
L-NEW successor 30 (Opus 5.5; D14, D18, L40). Written 2026-10-28 from 21:30Z (date -u), on the Lead's word of 21:27Z (message to L-NEW):
"TASK 1, the OFFMONO unit fixes file. … Repairs only: no signed statement changes, every changed sentence quoted from a referee, quotes checked
by script and pinned in experiments/new/check.sh." FROZEN at push; its sha1 is reported to the Lead.
- Objects, all FROZEN and not edited (sha1 re-measured on this tree at the successor 30 handover check):
  - docs/new/P-N5-OFFMONO-box49.md ("OFFMONO"), sha1 d9705ac6cede9849d68bf9b8d0fc5c54ab6fc3c4, l-new freeze 1f816370, author successor 28;
  - docs/new/P-N5-OFFMONO-add-box49.md ("add1"), sha1 5911aba8fc4e968187523c27b4f48cdc55433b3f, freeze b2a78eb1, successor 29;
  - docs/new/P-N5-OFFMONO-add2-box49.md ("add2"), sha1 f2d123ef6ebbb71408dc25b503b78edc085cbf9a, freeze 6ef3dd25, successor 29;
  - docs/new/P-N5-OFFMONO-add3-box49.md ("add3"), sha1 b7cd0ff103ead10054c8f42f787369710f7feb40, freeze 8b7e2e6e, successor 29.
  I write these repairs as the authors' successor.
- Repairs only. This file adds no lemma and changes no signed statement. Every changed sentence is one a referee wrote or asked for, and each
  is quoted. Where a note asks for nothing to change, the item says so.
- Sources. Each referee file is read at the commit that holds its unit §C; line numbers are of the files at these commits:
  - REFEREE: docs/referee/R-N5-OFFMONO.md (report 04a563d3, successor 15) and -add.md (c2a97189, successor 15), -add2.md (d6e07396 / stamp
    ff99f1f5) and -add3.md (907e21b9 / d1a22e18) (successor 16); the unit §C at the end of R-N5-OFFMONO.md, and the pointers in the three
    addendum reports, at claude/referee 96b2cd9a. All four files are quoted at 96b2cd9a.
  - REFEREE-2: docs/referee-2/R2-N5-OFFMONO.md, report 4e9a6372, §C at claude/referee-2 c040084a; quoted at c040084a.
  - The four packets at their freeze commits above.
  - At the time of writing, 96b2cd9a and c040084a are on the referee branches, not yet on trunk (`git branch -r --contains`).
- Quotes. Every «…» below is verbatim. Its tag [Q path@commit:lines] gives the source. experiments/new/box49/quotecheck3.py (L-SI's
  experiments/si/rund/quotecheck.py format, copied) checks each one against `git show commit:path` at those lines (whitespace normalised; "…"
  inside a quote separates parts, each of which must occur, in order). `python3 -I experiments/new/box49/quotecheck3.py
  docs/new/P-N5-OFFMONO-fixes-box49.md` prints QUOTES PASS; pinned in experiments/new/check.sh with its quote count and a shifted-line control
  that must fail.

## Verdicts (joint)
- REFEREE §C: [Q docs/referee/R-N5-OFFMONO.md@96b2cd9a:102] «Verdicts identical on every item. Joint gap map: EMPTY.»
- REFEREE-2 §C: [Q docs/referee-2/R2-N5-OFFMONO.md@c040084a:238] «Identical on every to-sign item: SIGN, no gap, in all four files.» and
  [Q docs/referee-2/R2-N5-OFFMONO.md@c040084a:239] «JOINT GAP MAP: EMPTY.»
- So every to-sign item of the unit is SIGNED by both referees with no gap:
  - OFFMONO: §1 Lemma OFFSET-MONO; §2 Corollary CHAIN-SUM; §2 Corollary CHAIN-COUNT (a REDUCTION to EXIT_x, CYC_c and D).
  - add1: §0 (CYC-ID), (CYC-SHAPE) (REFEREE SIGNED, REFEREE-2 CORRECT); §1 Remark Z-CONST; §2 Corollary CHAIN-COUNT′; §3 Lemma ZCH-COUNT and its
    Corollary (a REDUCTION in TIE_c, ODDC_c).
  - add2: §0 (A-F); §1 Lemma FT-COUNT; §2 Remark FT-CONST; §3 Corollary CHAIN-COUNT″; §4 Lemma PF-CHOICE and Corollary TIE-CHARGE (code-level,
    against si.py e688b963).
  - add3: §1 Lemma OFFSET-MONO⁺; §2 Corollary CHAIN-COUNT‴ (a REDUCTION to EXIT_x and D, both OPEN).
  - Not reviewed, as the packets asked: OFFMONO §3-§5, add1 §4-§7, add2 §5-§7, add3 §3-§4 (READING / DATA / OPEN).
- Scope, both referees: [Q docs/referee-2/R2-N5-OFFMONO.md@c040084a:20-21] «the unit reduces the per-phase, per-class count of κ-changes to EXIT_x
  (exit changes) and D (offset values on a piece). Both are OPEN. Nothing here bounds N5's running time.» G-N5-TIME stays OPEN.
- Notes to the lane: REFEREE OFFMONO-N1..N4, OFFADD-N1..N2, ADD2-N1..N4, ADD3-N1..N3; REFEREE-2 N-OFF-1..9. F1-F14 take them one at a time;
  the table says where each one goes.
  | note(s) | item | kind |
  | --- | --- | --- |
  | N-OFF-1 | F1 | premise wording, all four packets |
  | OFFMONO-N3 | F2 | premise wording (P1), OFFMONO and add3 |
  | OFFMONO-N4, OFFADD-N2, ADD2-N4 (= N-OFF-7's conjecture side, N-OFF-9's subject; ADD3-N3) | F3 | bookkeeping: PROVED by add3 |
  | ADD3-N1 | F4 | one clause, add3 §1 |
  | OFFADD-N1, N-OFF-2, N-OFF-6 | F5 | Remark (i) of add1; add3 §3 READING; D ≥ 1 |
  | N-OFF-3 | F6 | wording, add2 §2 |
  | N-OFF-5 | F7 | wording, add1 §3 |
  | ADD2-N2 | F8 | citation, add2 §4 |
  | ADD2-N1 | F9 | sharper count (remark; the signed bound is unchanged) |
  | N-OFF-4 | F10 | no change |
  | OFFMONO-N1 | F11 | DATA definition, OFFMONO §4 |
  | ADD3-N2, N-OFF-7 | F12 | DATA record: L1 and L2a exercised |
  | OFFMONO-N2, N-OFF-8, ADD2-N3 | F13 | DATA / method, no change |
  | N-OFF-9 | F14 | independence record, no change |

## F1. N-OFF-1: λ_Ξ is constant on a phase by definition; R38 (a) KEY is about λ_U (premise wording; all four packets)
- Packet text: [Q docs/new/P-N5-OFFMONO-box49.md@1f816370:28] «RESULTS R38 (a) KEY (λ is constant on a phase).»;
  [Q docs/new/P-N5-OFFMONO-add-box49.md@b2a78eb1:28] «RESULTS R38 (a) Remark KEY (λ is constant on a phase; docs/RESULTS.md l. 1825).»;
  [Q docs/new/P-N5-OFFMONO-add2-box49.md@6ef3dd25:27] «RESULTS R38 (a) Remark KEY (λ constant on a phase; docs/RESULTS.md l. 1825).»;
  [Q docs/new/P-N5-OFFMONO-add3-box49.md@8b7e2e6e:23] «RESULTS R38 (a) Remark KEY (λ constant on a phase; l. 1825).»
  In the text: OFFMONO §0 [Q docs/new/P-N5-OFFMONO-box49.md@1f816370:37] «A phase P of N5 (τ and λ constant; RESULTS R38 (a))», add1 §1
  [Q docs/new/P-N5-OFFMONO-add-box49.md@b2a78eb1:57-58] «(c is the cycle node at both, by R38 (a);» and add3 §1
  [Q docs/new/P-N5-OFFMONO-add3-box49.md@8b7e2e6e:38] «y2 ∈ U_c (λ constant, R38 (a))».
- REFEREE-2: [Q docs/referee-2/R2-N5-OFFMONO.md@c040084a:196-198] «"RESULTS R38 (a) KEY (λ is constant on a phase)" cites KEY for the constancy of λ_Ξ.
  KEY's quoted sentence is about λ_U (Odd's valuation map): "λ_U is a function of τ alone". λ_Ξ is constant on a phase by the definition of a
  (λ_Ξ, τ)-phase; KEY's second clause is what makes these the joint phases. No effect on any proof.»
- REFEREE's §C: [Q docs/referee/R-N5-OFFMONO.md@96b2cd9a:113] «ACCEPTED (I read KEY's text: its quoted clause is λ_U's; the (λ_Ξ, τ)-phase fixes λ_Ξ by
  definition)»
- Repaired premise line (all four packets): "A phase is a (λ_Ξ, τ)-phase: λ_Ξ and τ are constant on it by definition. RESULTS R38 (a) Remark
  KEY (docs/RESULTS.md l. 1825: λ_U is a function of τ alone) is what makes these the joint λ-phases." In the three places in the text, read
  "λ constant" / "by R38 (a)" as "λ_Ξ constant on the phase (by its definition)". No proof step changes.

## F2. OFFMONO-N3: name P1 in the premise list (citation; OFFMONO and add3)
- Packet text: [Q docs/new/P-N5-OFFMONO-box49.md@1f816370:26-27] «standing premise 1E-N3 (RESULTS R57).» (the same words in add3:
  [Q docs/new/P-N5-OFFMONO-add3-box49.md@8b7e2e6e:22] «S1's order; standing premise 1E-N3 (RESULTS R57).»), used in Case L as
  [Q docs/new/P-N5-OFFMONO-box49.md@1f816370:74] «with Ξ_t = L_{σ_t} (S1's counterstrategy is optimal: standing premise 1E-N3)».
- REFEREE: [Q docs/referee/R-N5-OFFMONO.md@96b2cd9a:77-78] «Step 2's Case L uses Lemma S (a) through the standing premise 1E-N3 (S1's counterstrategy is
  Odd's pointwise optimum, form P1); the packet says so in the proof; the premise list could name P1 as P-N5-FLIP §1 does.»
- REFEREE-2 (its §0 premise column): [Q docs/referee-2/R2-N5-OFFMONO.md@c040084a:27] «Lemma S (a) (R18 (d), every game by R57 (a), standing premise
  1E-N3)»; the §C row matching it: [Q docs/referee/R-N5-OFFMONO.md@96b2cd9a:106] «OFFMONO-N3 (Case L uses Lemma S (a) through 1E-N3) | its §0 premise
  column (Lemma S (a), standing premise 1E-N3) | same».
- P1 as P-N5-FLIP §1 names it: [Q docs/si/P-N5-FLIP-box18.md@7ea3d8cf:27] «P1: σ̄_k is Odd's pointwise-optimal strategy in the one-player game
  G_{σ_k}.»
- Repaired premise line (OFFMONO and add3): "standing premise 1E-N3 in its form P1 (P-N5-FLIP §1: S1's σ̄ is Odd's pointwise optimum in G_σ;
  RESULTS R57), used by Case L (OFFMONO §1) and Cases L1, L2 (add3 §1) through Lemma S (a)." add1 and add2 do not use Lemma S (a); their
  premise lines are unchanged.

## F3. OFFMONO-N4, OFFADD-N2, ADD2-N4: PROVED by add3 (bookkeeping; ADD3-N3)
- The open items as written: OFFMONO-N4 [Q docs/referee/R-N5-OFFMONO.md@96b2cd9a:80] «a CONJECTURE that the hypothesis can be dropped would be the
  natural next item; it is not proved here»; OFFADD-N2 [Q docs/referee/R-N5-OFFMONO-add.md@96b2cd9a:58-59] «OFFSET-MONO for q on an honest cycle at t:
  0 failures in 4,006 + 1,371 checks (OFFMONO-N4 and §1 above). If proved, CHAIN-COUNT holds with no CYC term at all.»; ADD2-N4
  [Q docs/referee/R-N5-OFFMONO-add2.md@96b2cd9a:110-111] «ZC″_c is needed by the proof, but not shown necessary in data (0 offset falls at 1,054 cut checks;
  no-cut control silent). Whether some game needs it is OPEN, as for add1's ZC_c.»
- REFEREE (add3 report): [Q docs/referee/R-N5-OFFMONO-add3.md@96b2cd9a:74-75] «With OFFSET-MONO⁺ signed, my predecessor's OFFADD-N2 (CONJECTURE
  candidate) and OFFMONO-N4 are answered. They should be marked "PROVED by P-N5-OFFMONO-add3" in the joint notes, not left as open conjectures.»
- REFEREE's §C: [Q docs/referee/R-N5-OFFMONO.md@96b2cd9a:107] «ANSWERED by add3's OFFSET-MONO⁺ (signed by both); mark both "PROVED by add3" (ADD3-N3)»
- REFEREE-2's §C: [Q docs/referee-2/R2-N5-OFFMONO.md@c040084a:246] «PROVED by add3's OFFSET-MONO⁺, which both of us sign (= ADD3-N3)» and, for
  ADD2-N4, [Q docs/referee-2/R2-N5-OFFMONO.md@c040084a:251] «the necessity question is CLOSED by OFFSET-MONO⁺: no level's offset ever falls, so no game
  needs any cycle cut» and [Q docs/referee-2/R2-N5-OFFMONO.md@c040084a:285] «OFFMONO-N4, OFFADD-N2 and ADD2-N4 are closed by OFFSET-MONO⁺.»
- Recorded: OFFMONO-N4, OFFADD-N2 and ADD2-N4 are PROVED by P-N5-OFFMONO-add3 (Lemma OFFSET-MONO⁺, signed by both referees). The cycle cuts of
  CHAIN-COUNT, CHAIN-COUNT′ and CHAIN-COUNT″ are proof devices: OFFSET-MONO⁺ removes the need for them (the counts are F5's matter).
  OFFMONO §1's hypothesis "q on no honest cycle at t" stays in OFFMONO's statement, which is signed as written; OFFSET-MONO⁺ is the
  statement without it.

## F4. ADD3-N1: say y2 ≠ q (one clause; add3 §1)
- Packet text: [Q docs/new/P-N5-OFFMONO-add3-box49.md@8b7e2e6e:38-39] «y2's honest play at t ends in c's honest cycle Z_t(c), which contains q. So that
  play meets q, either before c (Case L1) or after reaching c (Case L2).»
- REFEREE: [Q docs/referee/R-N5-OFFMONO-add3.md@96b2cd9a:71] «Say y2 ≠ q (a self-loop at q would make q its own cycle node at t + 1, against λ
  constant). Both cases need it.»
- REFEREE-2's §C: [Q docs/referee-2/R2-N5-OFFMONO.md@c040084a:252] «correct: a self-loop at q would make q its own cycle node at t + 1. REFEREE 15 had it
  in OFFMONO §1; I checked it but did not write it»
- Repaired: before "So that play meets q", add "y2 ≠ q: a self-loop at q would make q its own cycle node at t + 1, against λ_Ξ constant on the
  phase (F1)." (OFFMONO §1 already had it, as REFEREE 15 checked: [Q docs/referee/R-N5-OFFMONO.md@96b2cd9a:30] «y2 ≠ q (a self-loop at q would make
  q its own cycle node, λ(q) = c ≠ q) ✓».)

## F5. OFFADD-N1, N-OFF-2 (refined), N-OFF-6: which earlier counts follow from which (add1 Remark (i); add3 §3 READING)
- Packet text, add1 §2 Remark (i): [Q docs/new/P-N5-OFFMONO-add-box49.md@b2a78eb1:78-79] «(i) ZC_c ⊆ CYC_c, so CHAIN-COUNT′ implies P-N5-OFFMONO's
  CHAIN-COUNT, with x-pieces′ at least as long as x-pieces; the hypothesis "≤ D values on every piece" is then asked on longer pieces.»
- Packet text, add3 §3 (READING, unsigned): [Q docs/new/P-N5-OFFMONO-add3-box49.md@8b7e2e6e:67] «all follow from CHAIN-COUNT‴ (their cut sets only add
  pieces and a non-negative term).»
- REFEREE, OFFADD-N1: [Q docs/referee/R-N5-OFFMONO-add.md@96b2cd9a:54] «"CHAIN-COUNT′ implies P-N5-OFFMONO's CHAIN-COUNT" holds through the SUM form»
  … [Q docs/referee/R-N5-OFFMONO-add.md@96b2cd9a:56-57] «The STATED form alone does not, since its D is asked on the longer pieces′; the packet says so
  ("the hypothesis … is then asked on longer pieces"), and one line naming the sum form would close it.»
- REFEREE-2, N-OFF-2: [Q docs/referee-2/R2-N5-OFFMONO.md@c040084a:200-201] «is true of the ROUTE (‴ needs only EXIT_x and D), not of the NUMBERS.» and
  [Q docs/referee-2/R2-N5-OFFMONO.md@c040084a:205-206] «Suggested wording: "are no longer needed", not "follow from".»
- REFEREE's §C (withdrawing its add3 report's wording): [Q docs/referee/R-N5-OFFMONO.md@96b2cd9a:117] «ACCEPTED; I withdraw my wording.» and
  [Q docs/referee/R-N5-OFFMONO.md@96b2cd9a:117] «Suggested wording: "are no longer needed" (add3 §3 is a READING, unsigned)».
- REFEREE-2's §C, the joint reading (N-OFF-2 refined by OFFADD-N1): [Q docs/referee-2/R2-N5-OFFMONO.md@c040084a:260] «The stated / D forms of
  CHAIN-COUNT, CHAIN-COUNT′ and CHAIN-COUNT″ DO follow from CHAIN-COUNT‴'s SUM form.» and [Q docs/referee-2/R2-N5-OFFMONO.md@c040084a:264] «The cut SUM
  forms (CHAIN-COUNT′ and CHAIN-COUNT″ state one) do NOT follow.» and [Q docs/referee-2/R2-N5-OFFMONO.md@c040084a:267-268] «Joint reading: add3 §3's "follow
  from" is right for the stated / D forms, through ‴'s sum form, and not for the cut sum forms. The route (count reduced to EXIT_x and D) is
  unaffected.»
- REFEREE-2, N-OFF-6: [Q docs/referee-2/R2-N5-OFFMONO.md@c040084a:213-214] «The D form also needs D ≥ 1, which every non-empty piece gives. All four sum
  forms are the sharper statements»
- Repaired add1 Remark (i): "(i) ZC_c ⊆ CYC_c. Through the SUM form, CHAIN-COUNT′ implies P-N5-OFFMONO's CHAIN-COUNT: under CHAIN-COUNT's
  hypothesis an x-piece′ is a union of x-pieces glued at CYC ∖ ZC transitions, so Σ_{π′}(v_x(π′) − 1) ≤ (D − 1)(#x-pieces) + |CYC_c ∖ ZC_c|
  (OFFADD-N1). The stated form alone does not, since its D is asked on the longer pieces′."
- Repaired add3 §3, first bullet (READING): "The CUTS are no longer needed: P-N5-OFFMONO's CHAIN-COUNT (cut CYC_c), add1's CHAIN-COUNT′ (cut ZC_c)
  and add2's CHAIN-COUNT″ (cut ZC″_c) stand on their own proofs; the route of all of them (the count reduced to EXIT_x and D) is CHAIN-COUNT‴'s.
  As numbers, their stated / D forms follow from CHAIN-COUNT‴'s sum form; the cut SUM forms of CHAIN-COUNT′ and CHAIN-COUNT″ do not (a cut sum
  bound is below ‴'s in 10 / 12 of 27,395 (q, J) pairs in REFEREE-2's data)." REFEREE-2's example: [Q docs/referee-2/R2-N5-OFFMONO.md@c040084a:265]
  «e.g. tcS8_N9, J = 19..21: 39 against 55.»
- N-OFF-6: in every D form, D ≥ 1 is implicit (a piece has at least one state, so v_x(π) ≥ 1); the sum forms are the sharper statements. No
  statement changes.

## F6. N-OFF-3: FT-CONST's offset clause is for x ∈ Q (wording; add2 §2)
- Packet text: [Q docs/new/P-N5-OFFMONO-add2-box49.md@6ef3dd25:53-54] «and for every x ∈ Z_t(c), x ≠ c, and p := par_{t+1}(x): off_{t+1}(x; p) = off_t(x;
  p).»
- REFEREE-2: [Q docs/referee-2/R2-N5-OFFMONO.md@c040084a:207-208] «but par is defined only for q ∈ Q ∩ U. Read "x ∈ Z_t(c) ∩ Q". It is used only so (Step
  A″).»
- REFEREE's §C: [Q docs/referee/R-N5-OFFMONO.md@96b2cd9a:114] «ACCEPTED (OFFMONO §0 defines par for Q only; Step A″ uses only x ∈ Q)»
- Repaired: "and for every x ∈ Z_t(c) ∩ Q, x ≠ c, and p := par_{t+1}(x): off_{t+1}(x; p) = off_t(x; p)." (κ(x) is unchanged for every x ∈ Z_t(c),
  x ≠ c, by the proof's first part; only the offset clause needs par.)

## F7. N-OFF-5: CEVEN / ODDC by the OWNER of c (wording; add1 §3)
- Packet text: [Q docs/new/P-N5-OFFMONO-add-box49.md@b2a78eb1:87] «CEVEN if N = ∅ and c is Even; ODDC if N = ∅ and c is Odd.»
- REFEREE-2: [Q docs/referee-2/R2-N5-OFFMONO.md@c040084a:211-212] «means the OWNER of c: ODDC needs c ∈ Q, and CEVEN's ψ argument needs c to switch by
  (SW). Ω(c)'s parity plays no role there.»
- REFEREE's §C: [Q docs/referee/R-N5-OFFMONO.md@96b2cd9a:116] «N-OFF-5 (CEVEN / ODDC by the OWNER of c) | ACCEPTED»
- Repaired: "CEVEN if N = ∅ and c is owned by Even; ODDC if N = ∅ and c is owned by Odd (the owner, not the parity Ω(c))."

## F8. ADD2-N2: TIE-CHARGE's Even step takes x′ ∈ U_c from (Aκ) (citation; add2 §4)
- Packet text: [Q docs/new/P-N5-OFFMONO-add2-box49.md@6ef3dd25:103-104] «An Even z ∈ A_t that switches has κ_{t+1}(z) ≻ κ_t(z) (add1 §3, the Even case: (SW),
  (M1κ), (Aκ), (M2κ)), an F-touching change»
- REFEREE: [Q docs/referee/R-N5-OFFMONO-add2.md@96b2cd9a:106-107] «The Even step cites add1 §3, whose "x′ ∈ U_c" came from x′ ∈ Z_{t+1}(c). For z ∈ A_t,
  take x′ ∈ U_c from (Aκ) at t + 1 instead. One clause.»
- REFEREE-2 makes the same step: [Q docs/referee-2/R2-N5-OFFMONO.md@c040084a:124] «(the add1 step; next_{t+1}(z) ∈ U_c by (Aκ))»
- Repaired: "An Even z ∈ A_t that switches to x′ := σ_{t+1}(z) has κ_{t+1}(z) ≻ κ_t(z) (add1 §3's Even case: (SW), (M1κ), (Aκ), (M2κ), with
  x′ ∈ U_c taken from (Aκ) at t + 1, since z ∈ U_c ∖ {c}), an F-touching change".

## F9. ADD2-N1: FT-COUNT's per-vertex count is ≤ n (a sharper remark; the signed bound is unchanged)
- Packet text: [Q docs/new/P-N5-OFFMONO-add2-box49.md@6ef3dd25:49] «Hence z takes at most 2|F| = 2(n − 1) charges»
- REFEREE: [Q docs/referee/R-N5-OFFMONO-add2.md@96b2cd9a:36-38] «F is exactly the set of κ-values with first component 0 (for z ≠ c), a contiguous block of
  the lexicographic order, so a monotone κ(z) enters F at most once, moves inside it at most |F| − 1 times and leaves it at most once: ≤ n
  F-touching changes per z.»
- REFEREE-2's §C: [Q docs/referee-2/R2-N5-OFFMONO.md@c040084a:248] «CORRECT. F = the κ-values with first component 0 (z ≠ c)»
- Added after FT-COUNT's proof, as a remark: "Sharper (REFEREE, ADD2-N1): z takes at most n charges, so |FT_c| ≤ n(|U_c| − 1). Not needed; the
  signed bound 2(n − 1)(|U_c| − 1) stands." Data: REFEREE's [Q docs/referee/R-N5-OFFMONO-add2.md@96b2cd9a:38] «Data: at most 7 per vertex per phase
  (§5).»

## F10. N-OFF-4: the minimum in κ-Y-FORM_D (no change)
- Packet text: [Q docs/new/P-N5-OFFMONO-box49.md@1f816370:48] «the minimum is attained at σ̄_t(q) (Odd's choice; RESULTS R56 (d) with (Aκ)).»
- REFEREE-2: [Q docs/referee-2/R2-N5-OFFMONO.md@c040084a:209-210] «R56 (d) alone states the equality of values only; the packet says "with (Aκ)", so this is
  fine.» REFEREE's §C: ACCEPTED. Nothing to change.

## F11. OFFMONO-N1: the "parent changed" column of OFFMONO §4 (DATA definition; not signed)
- Packet text: OFFMONO §4's table, [Q docs/new/P-N5-OFFMONO-box49.md@1f816370:130] «| nep90_n40 (start ../si/rund) | 455 | 0 | 28 |».
- REFEREE: [Q docs/referee/R-N5-OFFMONO.md@96b2cd9a:72-73] «At the lane's three start files my count of checks with par_t(q) ≠ par_{t+1}(q) is 53 / 60 / 48 (nep90 /
  nep76 / long121) against the packet's 28 / 42 / 26» … [Q docs/referee/R-N5-OFFMONO.md@96b2cd9a:74] «the lane should state its definition of "parent
  changed"».
- REFEREE-2's §C: [Q docs/referee-2/R2-N5-OFFMONO.md@c040084a:243] «CONFIRMED independently. My logs/named.txt gives exactly 455 / 390 / 363 checks, 53 / 60
  / 48 parent changes and Case L 2 on long121, with par as in §0».
- The lane's definition, from the code that made the column: [Q experiments/new/box48/offmono2.py@1f816370:56] «if p != c and qs and A["vs"][q][0] ==
  c:» and [Q experiments/new/box48/offmono2.py@1f816370:58] «if (pt[0] if pt else c) != p: inc("parent_changed_checks")».
- Stated: the packet's "parent changed at t → t+1" counts the checks with p := par_{t+1}(q) ≠ c (q has a Q-vertex on its (t+1)-play before c)
  and par_t(q) ≠ p. It leaves out the checks where the new parent is c and the old one is not. Under §0's definition (par_t(q) ≠ par_{t+1}(q),
  either side may be c) both referees count 53 / 60 / 48 on nep90 / nep76 / long121. The check counts (455 / 390 / 363) and Case L agree. DATA
  only; no statement depends on the column.

## F12. ADD3-N2 corrected by N-OFF-7: Case L2a is exercised twice, L1 once in each referee's data (DATA record; add3 §4)
- Packet text: [Q docs/new/P-N5-OFFMONO-add3-box49.md@8b7e2e6e:78-79] «Case L1 never occurs in these data; Case L2 does (473 checks).»
- REFEREE (add3 report): [Q docs/referee/R-N5-OFFMONO-add3.md@96b2cd9a:72-73] «The strict sub-case L2a never occurs in my data; L1 occurs once. The landing
  text should carry "rests on proof alone" for L2a.»
- REFEREE-2: [Q docs/referee-2/R2-N5-OFFMONO.md@c040084a:253] «L2a occurs, and holds strictly, in 2 random games I saved. It is very thin (2 in about
  17,900 on-cycle checks), not vacuous» and its instances [Q docs/referee-2/R2-N5-OFFMONO.md@c040084a:275] «r1814_6302_0.pg (sha1 9c575fc9), t = 1, c = 0,
  q = 4, y1 = 8, y2 = p = 3» and [Q docs/referee-2/R2-N5-OFFMONO.md@c040084a:276] «r1813_619_1.pg (sha1 fd6d95a4), t = 0, c = 7, q = 3, y1 = 5, y2 = p =
  1».
- REFEREE's §C: [Q docs/referee/R-N5-OFFMONO.md@96b2cd9a:119] «CORRECTED: L2a is exercised, twice, in REFEREE-2's data only; L1 once in each referee's
  data (mine: harm_n12_seed412); the landing text can say "L2a exercised twice"»
- Recorded (add3 §4, DATA): Case L1 is exercised once in each referee's data (REFEREE: harm_n12_seed412, sha1 5282c3f1; REFEREE-2: once in its
  lib41 runs), never in the lane's. Case L2a (P(Ξ_t y2) ≠ ∅, the strict sub-case) is exercised twice, in REFEREE-2's saved instances
  docs/referee-2/R2-N5-OFFMONO/l2a/ (r1814_6302_0.pg, r1813_619_1.pg), and holds strictly there; never in the lane's or REFEREE's data. The
  landing text says "L2a exercised twice", not "rests on proof alone". L2b carries the bulk (473 lane checks; 4,498 + 855 + 4,036 REFEREE;
  4,048 REFEREE-2).

## F13. OFFMONO-N2, N-OFF-8, ADD2-N3: data and method notes (no change)
- OFFMONO-N2: [Q docs/referee/R-N5-OFFMONO.md@96b2cd9a:75-76] «On the lane instances D is large (max D 69 on nep90's phase, against at most 72 κ-changes
  of one vertex), so CHAIN-COUNT is weak exactly where R61's product is». The packet's §3 says the route needs EXIT_x and D, both OPEN; nothing
  to change.
- N-OFF-8: [Q docs/referee-2/R2-N5-OFFMONO.md@c040084a:218] «TIE 14 and ODDC 29 transitions in all. FT-COUNT's factor 2 is never needed (CTL_ft1 = 0). Max
  EXIT per level 6.» Data; F9 is the proof side of the factor 2.
- ADD2-N3: [Q docs/referee/R-N5-OFFMONO-add2.md@96b2cd9a:109] «si.py was not used as a checker; my engine (rl_engine) agrees with it at every state
  compared.» Method; nothing to change.

## F14. N-OFF-9: independence exposure (record; no change)
- [Q docs/referee-2/R2-N5-OFFMONO.md@c040084a:219-220] «add3 quotes REFEREE 15's OFFADD-N2 and its counts. I could not avoid reading those two quotes; my
  OFFSET-MONO⁺ check was written from add3 §1's proof, with my own Case L1/L2 split.» For later packets: a packet sent to both referees quotes
  no referee report; it cites the note by name and commit only.

## What this file does not do
- It bounds nothing new. The unit's route still needs EXIT_x per phase and the offset value count D; both OPEN. ODDC_c stays unbounded
  (add2 §4's remark). G-N5-TIME stays OPEN. Not a TARGET.md claim.
