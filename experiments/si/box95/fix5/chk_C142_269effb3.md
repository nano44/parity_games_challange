# C142: landing check of RESULTS R128 (P-N5-GATE, L-SI 48-50), first fill (CHECKER successor 23, Opus 5.5, D1 / D18 / D20)
Lead message 17:06Z (its stamp). Object on origin at my fetch 17:05Z. Report 2026-11-12 17:12Z by date -u. Every number below was
measured by me from git objects or from a full `git archive`. Nothing is taken from the draft, the lane or the referees unless it says
«cited».

## 1. Object
| item | where | measured |
| --- | --- | --- |
| draft | docs/agents/R128-draft.md @ trunk 68c8d293 (RESULTS/GAPS equal f9520557's, `git diff --quiet` rc 0) | sha1 70db12a9e83b623a8aa6438494bffb4db029424e, 524 lines |
| title | d[248] | = «### R128 [refereed-only] » + L-4 + «, CHECKER PASS (docs/checker/C142.md, checker PENDING)» (True) |
| entry block | d[248:445] | 197 lines, 0 "\|", 0 empty lines, d[445] blank |
| GAPS UPDATE | d[462] | sha1 90d1e0ca964af3edc672aea76fa69fef1d799be9 (unfilled, no newline), 12,601 B; = my build on L-4 (§4) |
| line L-4 | docs/si/P-N5-GATE-line-L4.txt @ claude/l-si 676b6a1c | sha1 6bfde78ef050b47f43527875256c65a205869e77, 12,562 B; = my rebuild from L-3 (§4) |
| packet / fixes | docs/si/P-N5-GATE.md frozen 4066f579 (sha1 f3a584e6… at 676b6a1c); fixes entries 1-4 (entry 4: 676b6a1c, l. 248-) | §3.2, §3.4 read |
| referees | REFEREE §K (49d34123, an ancestor of 68c8d293): «**Line L-4 MATCHES** (L-3 + exactly LT-1, GL-1..GL-3 and the entry count).» (l. 411); REFEREE-2 Add. 3 (93413fc6, an ancestor): «Verdict: L-4 (676b6a1c, sha1 6bfde78e) MATCHES.» (l. 569) | at those lines |

## 2. Verdict: **FAIL**: three line items (E-1, E-2, E-3) and one entry-text item (E-4)
The mathematics, tools, the box checks, the UPDATE procedure (G-U) and the placement PASS.

**E-1 (L43): the GL-3 DATA rows for RA-MULT and the RA path count carry family formulas and no source commit.** L-4 reads «re-arm
multiplicity m = n with C = 2n + 1 on MW8_2, MW32_2 (refutes a constant multiplicity only below 32), the RA path count P = F_(d+2) − 1 with
C = 3 on FW8_2, FW16_2,».
- L43 (DECISIONS l. 371) says an asymptotic DEAD enters «as DATA with its numbers and source commit, or not at all».
- Here the numbers are given as formulas (m = n, P = F_(d+2) − 1), not as numbers, and these two rows have no source commit. The MWR row
  has one: «L-RED 63, claude/l-red 406ef2fd».
- The numbers are L-SI 47's box 90, not box 91's. Box 91's outputs carry C only (own91.out header: no m, no P).
- My reads at 676b6a1c of box90/out/mw90.out (committed by 2d0344d3): maxm 8 / 32 on MW8_2 / MW32_2, both engines.
- My reads of fw90.out (committed by 4ded1e8d): maxP 54 / 2583 on FW8_2 / FW16_2 (= F_10 − 1, F_18 − 1), both engines.
- C: 17 / 65 (MW) and 3 / 3 (FW) in own91.out and g391.out.
- Neither referee re-counted m or P. REFEREE-2 Add. 4: «Still cited, not re-run: the re-arm multiplicity m = n, the RA path count P =
  F_(d+2) − 1» (l. 584-585 at f2793d9a).
- Fix R-E1 (§4): numbers on the named instances, plus the source.

**E-2 (L43, «A DATA label does not cure an overclaim»): the growth clause states asymptotic growth from finite data and names no
instance and no source.** L-4 reads «growth: C, A*_all and the largest gate flip count are linear in n on every family measured (MW(n):
C = 2n + 1, flips 4n + 2; MWR(n): flips 2n + 1 = 2·ch_D + 1 with lamch 0, which makes E-FACE-PAYS (d) tight)».
- «Linear in n» is an asymptotic statement, and it is measured at n = 8, 32 (MW) and n = 4, 8, 16 (MWR) only. REFEREE 31 §J said the same:
  «as DATA they are acceptable only as numbers on the named instances» (fbc4d865 l. 394-395).
- A*_all has no lane counter in the cited DATA. Box 91's «maxa» is 9 / 33 on MW8_2 / MW32_2 and 0 on FW16_2. It cannot be A*_all,
  because the line's own A*-EQUIV gives C ≤ A*_all, and 65 > 33. REFEREE-2 Add. 4 measured «A*_all 66» on MW32_2 and «A*_all 16» on
  FW16_2 with its own engine. So the line asserts A*_all growth without a lane number.
- My reads at 676b6a1c:
  - box91 own91.out and g391.out (rows equal): C 17 / 65, maxflip 34 / 130 on MW8_2 / MW32_2.
  - box93 mwr93_own.out and mwr93_g3.out (rows equal): mx_flips 9 / 17 / 33, mx_ch_D 4 / 8 / 16, mx_ch_pe 4 / 8 / 16, mx_lam_pe =
    mx_lam_pb = 0 on MWR4/8/16_2.
- Fix R-E2 (§4): numbers on the named instances, both engines, with their output files. A*_all is dropped from the DATA (L43: «or not
  at all»).

**E-3 (C135 E-4, undefined symbols): sub-labels used but not defined in the line.** L-4 cites «E-FACE-PAYS (b)» (3 times), «(c)» (in «(b),
(c) and WAIT-QUIET») and «E-FACE-PAYS (d)». It also cites GATE-LOW-NULL's «(a)'s order equivalence» and «(b′) no separate lane DATA».
Neither statement in L-4 marks its parts. The packet does mark them: §3.2 (a), (b), (b′) and §3.4 (a)-(d), at 676b6a1c l. 76-82 and
105-112. No landed RESULTS line defines these sub-labels: «GATE-LOW-NULL» and «E-FACE-PAYS» occur only in R126, as lane names. A RESULTS
reader cannot tell which clause (d) is.
- Fix R-E3 (§4): insert the packet's markers into the two statements. The words do not change. The markers follow the packet: (a) the
  order equivalence; (b) the flip / π-change; (b′) the equal-Λ rise; for E-FACE-PAYS (a) relocks / unlocks; (b) the p_e ⟺ D step
  equivalence; (c) the unlock bound with the proviso; (d) the flip bound.

**E-4 (entry text, not the line; G-6): «TRIGGER» name clash.** «(TRIGGER)» is a landed name of R107 (RESULTS l. 10593). Honest limits
(vii) names only the P-N5-GATE clash. Add, as R127's (viii) did for «Lemma SPLIT»: «TRIGGER» is also R107's; this entry's is «RESULTS R128
Corollary TRIGGER». No referee re-sign is needed for this item.

## 3. Rulings on the Lead's flags
- **G-MERGE.** I checked the merge without writing a ref. `git merge-tree --write-tree 68c8d293 676b6a1c`: rc 0, no conflict, tree
  2a01e035. From that tree's full archive, experiments/si box 90-96 checks ran with the repository's git objects available
  (GIT_DIR/GIT_WORK_TREE set, so the pinned engines 4b309716 / fcba92fc / ea985380 are present), 17:09:53Z-17:11:06Z: «BOX90 OK» …
  «BOX94 OK», box 95 «P-N5-GATE fix1-fix4 checks: PASS», «BOX96 checks: PASS», each rc 0, and no «NOT RUN» line. Without git (a bare
  archive) boxes 90-94 and 96 print «NOT RUN engine rows (pinned commit … absent)» and still exit 0, so the box 95 file checks are the
  only part that runs there. Negative control: one byte appended to L-4 in a copy of the merged tree gives «BOX95 FAIL fix4», rc 1.
  Merging l-si at 676b6a1c, not the later heads, is the Lead's call. No objection. At the second fill, merge the L-5 commit instead.
- **G-6 (names).** «P-N5-GATE» (R101's packet name too): no line change. R-ids and paths disambiguate, and Honest limits (vii) says so.
  «TRIGGER»: E-4.
- **G-U (UPDATE).** I confirm both deviations.
  - (i) The «, and » connector between PAIR-EXPEL and EXPEL-COUNT is kept, with the label moved behind its clause. This is landed R122's
    pattern: «… T_CYC ≤ N (Theorem ACYC-LIN); and …», GAPS l. 11.
  - (ii) The drop is L-4's own form, «; G-N5-TIME stays OPEN; not a step-4 pass, not a TARGET.md claim», and «not M3» stays in «not M4 and
    not M3».
  - My builder (c142/mkL5.py: R118's procedure with both deviations) gives 90d1e0ca… on L-4, equal to d[462]. On SPLIT's L-3, with the
    old drop, it gives R127's landed 5bd83938.
- **G-L43.** (i) → E-1. (ii) → E-2. (iii) The construction rows stay DEAD: clean, as the Lead ruled at 03:00Z. (iv) WC8_2 is not
  pinned in the four inst dirs: the clause names WC4_2, WC16_2 only, so no action.
- **G-4** (four P-N5-CHAIN frozen items: F2, CYC, (E-DOM), (Core) at 93531b03, sha1 6e613ba7): C141 G-4's case, no action.
- **G-7** (five L41 credits in the premise parenthesis, the EXPEL-COUNT and A*-EQUIV statements, and the scope tail): credited in the
  line, so no action (C141 G-7).
- **G-9 (DATA)**: every must-0 counter clause, cited, is no action. The growth clause and the GL-3 rows are E-2 and E-1.
- **G-1** (source note «L-SI successors 48-50»): no action. **G-L** («PROVED» once, in A*-EQUIV's label «PROVED-CONDITIONAL»): no action.
  **G-S** clean. **G-LT1** MET: R127 = P-N5-SPLIT landed at f9520557, CI #7513 success (C141).

## 4. Line L-5 and its UPDATE (strings; apply to L-4 in this order, each old string exactly once, checked)
- R-E1: «re-arm multiplicity m = n with C = 2n + 1 on MW8_2, MW32_2 (refutes a constant multiplicity only below 32), the RA path count
  P = F_(d+2) − 1 with C = 3 on FW8_2, FW16_2,» → «re-arm multiplicity m 8 / 32 with C 17 / 65 on MW8_2 / MW32_2 (refutes a constant
  multiplicity only below 32), the RA path count P 54 / 2583 (= F_(d+2) − 1 at d = 8, 16) with C 3 on FW8_2 / FW16_2 (m and P: L-SI 47
  box 90, claude/l-si 2d0344d3 and 4ded1e8d, box90/out/mw90.out maxm and fw90.out maxP, both engines),»
- R-E2: «growth: C, A*_all and the largest gate flip count are linear in n on every family measured (MW(n): C = 2n + 1, flips 4n + 2;
  MWR(n): flips 2n + 1 = 2·ch_D + 1 with lamch 0, which makes E-FACE-PAYS (d) tight)» → «growth, as numbers on the named instances only
  (both engines; box91/out/own91.out and g391.out C and maxflip, box93/out/mwr93_own.out and mwr93_g3.out mx_flips and mx_ch_D): C 17 /
  65 and the largest per-gate flip count 34 / 130 on MW8_2 / MW32_2, and per-gate flips 9 / 17 / 33 = 2·ch_D + 1 (ch_D 4 / 8 / 16) with
  lamch 0 on MWR4_2, MWR8_2, MWR16_2, where E-FACE-PAYS (d) holds with equality»
- R-E3 (seven insertions):
  - «(Lemma GATE-LOW-NULL) at a LAM ∧ PRIV step» → «(Lemma GATE-LOW-NULL) (a) at a LAM ∧ PRIV step»;
  - «(and they differ), so a flip at t» → «(and they differ), so (b) a flip at t»;
  - «changes π(E(p_e)) or π(E(p_b)) at t, and if Λ(p_e) = Λ(p_b)» → «changes π(E(p_e)) or π(E(p_b)) at t, and (b′) if Λ(p_e) = Λ(p_b)»;
  - «(Corollary E-FACE-PAYS) relocks(o) ≤ ch_(p_e),» → «(Corollary E-FACE-PAYS) (a) relocks(o) ≤ ch_(p_e),»;
  - «UP hypothesis, at every t with e_o ∉» → «UP hypothesis, (b) at every t with e_o ∉»;
  - «that of D does, so if D's play avoids e_o at every state of the run then» → «that of D does, so (c) if D's play avoids e_o at every
    state of the run then»;
  - «unchanged), and flips(o) ≤ 2·min(ch_(p_e), ch_(p_b)) + 1» → «unchanged), and (d) flips(o) ≤ 2·min(ch_(p_e), ch_(p_b)) + 1».
- Whitespace: the strings are single-line, with one space wherever this file wraps a line inside a string.
- **L-5** sha1 **7ebcf7355be9838473f05a7defe913940b6fd723**, 12,923 B: one line with its newline, 238 «(» = 238 «)», 0 "|" (c142/L5.txt).
- **UPDATE-5** (my builder on L-5, both G-U deviations, no reading): sha1 **f7edaed8b32cdad441bbe22c6111dd792fa96f59** (unfilled, no
  newline), 12,962 B, one each of <DATE>, <HH:MM>, <checker>, 0 "|", 238 «(» = 238 «)».
- E-3 changes statement text (markers only), so both referees re-sign the statements. E-1 and E-2 change the DATA. The lane writes L-5
  by script with a fixes entry 5, both referees byte-test it, the Lead refills the draft (adding E-4), then C142 Add. 1.

## 5. Checks run (scratch c142/)
- L-4 rebuild (c142/mkL4.py) from L-3 (b60495b2…, asserted):
  - LT-1's two strings as quoted in fixes entry 4 F4-1;
  - GL-1..GL-3 parsed by my script from REFEREE 31 §J (fbc4d865, `git show`), each old string once;
  - «fixes entries 1-3» → «1-4».
  Result 6bfde78e…, 12,562 B = L-4 (True).
- The box 90-96 checks on the merged tree, as in §3 G-MERGE, with the negative control.
- DATA reads for E-1 and E-2: box90 mw90.out and fw90.out, box91 own91.out and g391.out, box93 mwr93_own.out and mwr93_g3.out at
  676b6a1c (§2). F_10 = 55 and F_18 = 2584.
- Landing simulation of this fill's block on 68c8d293: R128 16127-16323, Erratum E-1 16325, 16,967 lines, 1,477 "|" unchanged; GAPS l.
  11: UPDATE after R127's, 76 "|". This equals the Lead's simulation, and the block will change at the second fill.
- Referee MATCH lines found at REFEREE l. 411 (49d34123) and REFEREE-2 l. 569 (93413fc6), both ancestors of 68c8d293.
- Deferred to Add. 1: the entry block's quote sweep. The block is refilled on L-5.

## 6. Verdict and next
- **FAIL**. E-1, E-2 and E-3 are line items: L-5 = 7ebcf735…, UPDATE-5 = f7edaed8…. E-4 is entry text. Then: the lane's fixes entry 5
  and L-5 by script; both referees byte-test L-5 and re-sign (E-3 touches two statements' wording by markers only); the Lead's second
  fill on L-5; C142 Add. 1.
