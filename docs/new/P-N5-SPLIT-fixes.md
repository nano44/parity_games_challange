# P-N5-SPLIT fixes (append-only; the packet docs/new/P-N5-SPLIT.md is frozen at l-new 399cda07, sha1 5bc1b1f390ed81683fe5c93008c7ea0b338fe735)

## Fixes entry 1 (L-NEW successor 67; written 2026-11-09 00:44Z by date -u; source: L-RED 62's packet-level read, claude/l-red f3903cb8 docs/red/R228-box91.md (B), relayed by the Lead 2026-11-09 00:25Z; I have not opened f3903cb8: it was not on origin when I fetched)
Scope: DATA only (§9.1). No statement, proof, premise or DEAD row of the packet changes.
- (n1) TAKEN. §9.1's clause «max c_y ≤ 6 outside MW (C6G8_n54 6), MW 2n + 1 (65 on MW32_2)» is restated with its set:
  - «On the 28 frozen instances of experiments/new/box199/inst (split199.out): max c_y ≤ 6 outside the MW family (C6G8_n54: 6); MW(n) has
    max c_y = 2n + 1 (65 on MW32_2).»
  - It is NOT a corpus statement. L-RED 62's cap-scaling climb (ORDER=CT, mutants of L-SI's MW(n), claude/l-red 6080533a / 4b06129e /
    0657d38f) reaches C 12 at N + M ≤ 200 and C 26 at N + M ≤ 400 (relayed by the Lead; not re-run by me; instances not frozen by me). These
    are on MW's line (C ≈ 2n + 1 at N + M ≈ 29n + 29): linear in N + M.
  - No PROVED statement used the clause. SPLIT-COUNT's tightness remark (MW and FW) is unchanged.
- (n2) NO CHANGE. §9.1 already says that playfail, kindfail, trfail and wlamfail test definitions and have no firing control; L-RED's
  split228 reproduces them on its own engine. Taken as stated.
- Lines: none (this entry changes no signable text).

## Fixes entry 2 (L-NEW successor 69; Lead 22:55Z 2026-11-11: «write P-N5-SPLIT fixes entry 2 (append-only) answering every item, plus line L-1 by script»; written 2026-11-11T22:55Z by date -u)
- Reports answered (read only, not edited):
  - REFEREE 30, docs/referee/R-P-N5-SPLIT.md at claude/referee ca091557: every row SIGN (§3, §4 and ASC-WIT (c) «SIGN WITH SP-1»),
    CONDITIONAL on R125; no GAP; SP-1, SP-2 (REQUIRED), SP-3 (optional); line requirements LS-1..LS-8.
  - REFEREE-2 36, docs/referee-2/R2-P-N5-SPLIT.md at claude/referee-2 991296c9 (final) + c708c968 (Addendum 1): every row SIGN,
    CONDITIONAL on R125; no GAP; W-1 (= SP-1, found independently) closed; line requirements R-1..R-5, R-6 (= SP-2), N-1 (= SP-3), N-2.
- No statement, proof, label, premise of a signed row, or DATA number changes. Where this entry and the packet differ, this entry governs.
  Every item is ACCEPTED.

### SP-1 (REFEREE) = W-1 (REFEREE-2): the reason in §1 (LEX-Λ). ACCEPTED (L41 standard, as P-N5-CHAIN's W-1 and P-N5-QUIET's R-G).
- §1 (LEX-Λ) gives as its reason a sentence that is false over all vertices (plays from pA or K3 pass K3, not K0; REFEREE-2's witness p = K3,
  z = K0). It is the sentence P-N5-CHAIN's fixes entry 3 records as false. Every use of (LEX-Λ) in the packet compares values of NON-core
  vertices: §3 (c) and PAIR-SPLIT (c′) (a, b: successors of a mover or a gate, i.e. pads), RW-SHAPE (ii) (the same a, b), ASC-WIT (c)
  (pe_(g1), pβ_(g1)). For non-core vertices the only edge into the eight-vertex core {K0, pA, K3, K1, s, r, K2, q} is pb_g → K0, so K0, K3
  lie on both plays (node K1) or on neither: P-N5-CHAIN's W-1 repair (fixes entry 3, R-W). So every signed proof stands.
- Governing reading of §1 (LEX-Λ): «(LEX-Λ) is applied only to non-core vertices (pads), where P-N5-CHAIN's W-1 repair holds.» The
  sentence «a play passes K0 iff it passes K3 iff its cycle node is in the closed core» is withdrawn; L-1 does not contain it (asserted).
- Credit: referee-originated: REFEREE-2 R2-P-N5-SPLIT W-1; also REFEREE R-P-N5-SPLIT SP-1 (found independently). REFEREE-2's
  strengthening (the conclusion «the larger value has the lex-larger e-set» holds for all pairs) is recorded, not used.

### SP-2 (REFEREE, REQUIRED) = R-6 (REFEREE-2): citation form. ACCEPTED.
- R125's line (L-4 a69c8aa9, L-5 473344b1) does not contain F2, (Core), (E-DOM), [G3], [DEF], (R) or (P); the packet calls them «P-N5-CHAIN
  facts». L-1 cites them as follows:
  - [DEF] = RESULTS R104's definitions of the genome and of Γ(G); [G3] = RESULTS R117's definition of Γ3(G); [OPT] = RESULTS R118 (b) +
    RESULTS R21 (a) (σ̄_t optimal at every vertex at once);
  - (R), (P), (E-DOM), (Core) (in its W-1-repaired reading: the only edge into the eight-vertex core from outside is pb_g → K0), F2 and CYC:
    P-N5-CHAIN's frozen text (l-new 93531b03, sha1 6e613ba7, §2 and §4);
  - the facts in P-N5-CHAIN's «To sign» rows (F1, F3, F4′, F5, F6, DOM, STRICT, CN2-3, LOC-GATE3, LOC-K2-3, B-ONLY3, NO-TIE3, T-QUIET3 with
    L3, E-MON3, CHAIN-DECOMP3, REACH3-ALL, HOW3): as RESULTS R125 (P-N5-CHAIN).

### SP-3 (REFEREE, optional) = N-1 (REFEREE-2). ACCEPTED as wording; governs §1 (PL).
- (PL) reads: «E_s(v) is the disjoint union of the e-letters of Π_s(v) strictly before u on P_s(v) and E_s(u)». It coincides with the frozen
  wording whenever E_s(v) ≠ ∅ (then w ≠ c_W and B-ONLY3 puts w below every e-vertex), and every use has E ≠ ∅.

### N-2 (REFEREE-2, optional). ACCEPTED; governs the «To sign» premise column.
- §2's row adds [DEF]; §7's row adds (E-DOM), (Core) (repaired reading), [DEF]. These were used in the proofs as written; no new premise.

### split.pins row count (REFEREE §4). NOTED.
- §11 says «58 rows»; experiments/new/box199/split.pins has 59 since fixes entry 1 (that entry's file was added). After this entry it has
  61 rows (this file re-pinned; line L-1 and its generator mkl1_199.py added). check.sh «P-N5-SPLIT» counts rows from the file.

### Line requirements, and how L-1 meets them
- LS-1 = R-2 + R-3: every statement «CONDITIONAL on RESULTS R125 (P-N5-CHAIN)»; labels as the «To sign» table; ASC-WIT and ASC-ROOT, and
  no other row, «under HYPOTHESIS [E-LEV]»; DEAD D1-D7 with their instances (sha1 prefixes) and counters.
- LS-2 = R-1: the governing (LEX-Λ) sentence above, with the credit string; the false sentence absent (asserted by the generator).
- LS-3 = R-6: the citation form above.
- LS-4 = R-4: the run named «HOW3(G), i.e. N5′-xi from S3 on Γ3(G) until its first fallback»; nothing for N5, nothing outside Γ3(G).
- LS-5 = R-5: DATA units as §9.1 (split199.py): spfail in its lower-bound form; rh2fail over all same-pair couples t < t′; playfail,
  kindfail, trfail and wlamfail named as definition checks without a firing control; the max c_y clause with its set, the 28 frozen
  instances (fixes entry 1 (n1)); «Large zero counts are DATA, not evidence» kept.
- LS-6 = R-4: RE-EQUIV, ALT-EQUIV, C-EQUIV stated as equivalences; SPLIT-COUNT as a reduction «C polynomial ⇐ max over y, b, J of
  Dhi_y(b, J) polynomial»; no polynomial claim; the open core named; «G-N5-TIME stays OPEN».
- LS-7: TARGET tail in the landed R123 / R124 form (asserted verbatim in RESULTS at trunk 8ba1b23b by the generator).
- LS-8: source note: packet sha1 5bc1b1f3 frozen at l-new 399cda07 with fixes entries 1-2; L-NEW successors 65-67 and 69; attack record
  L-RED 60-62.

## Line L-1 (L-NEW successor 69; first RESULTS line for P-N5-SPLIT; written 2026-11-11 by date -u)
- docs/new/P-N5-SPLIT-line-L1.txt, one paragraph, no «|»; generator experiments/new/box199/mkl1_199.py, run from the repo root with
  `git show 8ba1b23b:docs/RESULTS.md` saved to a file as its argument. It asserts the frozen packet's sha1, the governing (LEX-Λ) sentence
  verbatim in this file, the absence of the withdrawn sentence, R124's landed TARGET tail verbatim in RESULTS, one line, no «|», «(» = «)».

## Fixes entry 3 (L-NEW successor 71; Lead ruling R-D7a 07:12Z 2026-11-12, L43; written 2026-11-12T07:14Z by date -u)
- Source: R127 first fill (the Lead's helper, trunk 07139249) found one L43 item in L-1 (sha1 634b2fdf…). D7 bundled three claims: (i) «fan-in
  1 of RA», an explicit bound, killed by 3 and 4 (clean); (ii) «RA-LOG» (O(log(N + M)) depth, no explicit constant) and (iii) «bounded
  multiplicity» (RA-MULT(K)), stated as DEAD without numbers or source commits. Under L43 (docs/DECISIONS.md, Lead reading L43: «A lane DEAD
  of an ASYMPTOTIC statement (one with an unspecified constant …) does not enter a RESULTS line as «DEAD»: it enters as DATA with its
  numbers and source commit, or not at all»), (ii) and (iii) leave D7 and enter the DATA clause with numbers and sources. ACCEPTED as ruled.
- Ruling R-D7a (Lead, line-only), applied verbatim: in L-1, replace exactly once
  «D7 fan-in 1 of RA and RA-LOG / bounded multiplicity as game properties (NK6_cl21, 408b9988, fan-in 3; DSALT9_n416, fan-in 4; FW16_2,
  94df42b7, linear RA depth; MW32_2, 445031d1, multiplicity n, L-SI DATA cited)»
  with
  «D7 fan-in 1 of RA as a game property (NK6_cl21, 408b9988, fan-in 3; DSALT9_n416, da3308b5, fan-in 4; unit: max over (v, I, y) of the
  number of letters of RA(y), box198/pair198.out maxRA)»
  and in the DATA clause, right after «max split pairs 5 (FW6_4, FW8_4);», insert
  « RA depth (longest RA chain) 4 / 8 / 12 / 16 on FW4/8/12/16_2 (REFEREE-2 36 R2-P-N5-SPLIT, claude/referee-2 4948ce5d, own engine; L-SI
  47 box 90, claude/l-si 4ded1e8d) and the per-pair multiplicity n on MW(n) (L-SI 47 box 90, claude/l-si 2d0344d3, not re-run by the lane
  or a referee), DATA only;»
- Ids and numbers verified by git before the build (Lead: «If any id or number is wrong, STOP»; none was):
  - DSALT9_n416: experiments/new/box199/inst/SHA1SUMS «da3308b524e2b00861a880e8f9bfdc2cd652555f  DSALT9_n416.json».
  - 4948ce5d (on origin/claude/referee-2 and trunk): «REFEREE-2 36: R2-P-N5-SPLIT boxes 4-5 (DEAD D1-D7 and DATA replay on own engine …»;
    docs/referee-2/R2-P-N5-SPLIT.md there: «The longest RA chain (counting y) on FW4/8/12/16_2 is 4 / 8 / 12 / 16: linear in the family
    parameter.» and «The multiplicity m(y, z) = n on MW is L-SI's census. I did not compute it».
  - 4ded1e8d (origin/claude/l-si): «L-SI box 90: FW staircase family (P = F_(d+2) - 1, RA depth d, …»; docs/si/box90-ra.md there, header
    «(L-SI successor 47; …)», table rows FW4_2 / FW8_2 / FW12_2 / FW16_2 with RA depth 4 / 8 / 12 / 16.
  - 2d0344d3 (origin/claude/l-si): «L-SI box 90 milestone 2: MW family (m(y, z) = n, …»; docs/si/box90-ra.md there: «Family MW(n): m(y, z)
    = n», MW32_2 row maxm 32.
  - box198/pair198.out maxRA: pair198.py computes, per (v, I, y), the number of distinct re-arming letters of y (rs = RA(y)) and takes the
    maximum (pair198.out: NK6_cl21 maxRA 3, DSALT9_n416 maxRA 4) = the ruling's unit.
- Line L-2: docs/new/P-N5-SPLIT-line-L2.txt = L-1 + R-D7a, built by experiments/new/box199/mkl2_199.py (from the repo root; asserts the frozen
  packet's sha1 5bc1b1f3, L-1's sha1 634b2fdf, each old string exactly once, one line, no «|», balanced parentheses, «RA-LOG» and «MW32_2,
  445031d1» absent, each new source id once): sha1 d8888d0b090339b80b4ce9b636a23461b476bf3f, 9,521 B.
- Re-pinned: split.pins adds L-2 and mkl2_199.py and re-pins this file (63 rows); check.sh «P-N5-SPLIT» also asserts that L-2 is pinned.
- Lead's second ask (the three maxima clauses and the DATA rule), PROPOSED, NOT APPLIED (L-2 carries R-D7a only):
  - «max c_y ≤ 6 outside the MW family (C6G8_n54: 6) and MW(n) has max c_y = 2n + 1 (65 on MW32_2)»: its set is named («on the 28 frozen
    instances»), its unit is not. Proposed string, inserted after «max c_y»: « (unit: y-tops of one (v, I, y), max over (v, I, y);
    split199.out maxc)».
  - «max split pairs 5 (FW6_4, FW8_4)»: unit missing. Proposed: «max split pairs (unit: distinct split pairs (u, b) of the y-tops of one
    (v, I, y), max over (v, I, y); split199.out maxSPL) 5 (FW6_4, FW8_4)».
  - «every run is short (T3 ≤ 199)»: unit missing. Proposed: «every run is short (T3 ≤ 199; unit: states of the HOW3 run, max over the 28
    frozen instances, split199.out T3; 199 on MW32_2)».
  - Also noticed, not applied: L-1's source note reads «with fixes entries 1-2»; after this entry it could read «with fixes entries 1-3»
    (the QN precedent, mkl2_qn.py, left its source note unchanged).
