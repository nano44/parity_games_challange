# R-N5-CUT-C: §C cross-map for P-N5-CUT (REFEREE 19 vs REFEREE-2 21), K0 line check, K1 signature, K2-K11 review
Referee: REFEREE (successor 19), Opus 5.5 (D15). Lead brief 2026-10-30 02:00Z; written 02:03Z-02:08Z by date -u. Every verdict "(Opus 5.5, D15)".
- My report: docs/referee/R-N5-CUT.md at claude/referee ff5a6f81 (+ §10b line check 8a7818a0), pushed BEFORE I opened any docs/referee-2/ file.
- REFEREE-2's report: docs/referee-2/R2-N5-CUT.md at claude/referee-2 335814dc (sha1 ace5e691…, 303 lines; §8 = its line check), opened 02:02Z
  after the Lead's word. docs/referee-2/R2-N5-GAP.md NOT opened (my GAP report cd1c29d6 was pushed first anyway; I keep it closed until the GAP §C word).
- Fixes: docs/si/P-N5-CUT-fixes-box43.md at l-si cc84e54c, `git show cc84e54c:<path> | sha1sum` = ff9946215da949f49057fc939292b3e668e646cb (= the
  Lead's figure). The packet object is unchanged (d6519d3d).

## 1. Joint gap map and items signed by both
| item | REFEREE 19 | REFEREE-2 21 | joint |
| --- | --- | --- | --- |
| OPT-OFF (i), (ii) | SIGNED (premise CUT-N1) | SIGNED (premise N-CUT-2) | SIGNED by both |
| W-MON′, W-SUCC | SIGNED | SIGNED | SIGNED by both |
| W-RETURN-G | SIGNED | SIGNED | SIGNED by both |
| CUT-CHARGE + Remark | SIGNED | SIGNED | SIGNED by both |
| FRESH-SPLIT + ENT bound | SIGNED | SIGNED | SIGNED by both |
| LATE-SPLIT (i)-(iii), Consequence, R*-REP | SIGNED | SIGNED | SIGNED by both |
| WV-R | SIGNED | SIGNED | SIGNED by both |
| Theorem CUT-RED | SIGNED | SIGNED | SIGNED by both |
| Corollary CUT-POLY | SIGNED as an implication | SIGNED as an implication | SIGNED by both |
| §8 notes, §9 | READING / DATA, not signed | same | — |
Verdicts identical. Gap map EMPTY (neither referee lists a gap; nothing FALSE). No disagreement on any proof step.
- Proof-level agreements worth recording: both re-derived OPT-OFF (ii) in three cases with the same split (R2 §2.1 = my §2); both found the
  first-bullet wording "σ′v's play avoids v" not literal when v lies on its cycle below c (my CUT-N2, R2's N-CUT-3); both check the FR boundary
  index a − 1 ∈ [s, j − 1] and disjointness across re-entries. R2 adds that the leave k in LATE-SPLIT (ii) is UNIQUE in (u₁, u₂) (every
  adoption of z after u₁ would itself be late); I said "any leave works". Both true; compatible.
- Data: two independent engines (mine rl_engine, REFEREE-2's dual_check.Runner on si.py) reproduce the lane's §9 counts EXACTLY on the 719
  sbcg games with the S3 start (F 557, FR 6,031, C 4, P 5,035, S 42; LATE 313; late 1,141 = 1,100 + 41; max REP_F 6). Both: 0 W-silent and 0
  own-cycle REPEATs; the off-cycle premise of LATE-SPLIT (ii) is never exhibited (my MUT 3, R2's census). R2 also confirms R128 on latew_K20_m32
  (REP* 570 > n 538); I did not run latew (n 538 > my MAXN).
- Notes map (mine ↔ REFEREE-2's): CUT-N1 = N-CUT-2; CUT-N2 = N-CUT-3; CUT-N3 = N-CUT-5; CUT-N4 = N-CUT-9; CUT-N5 ≈ N-CUT-6 (R2: name m_E ≤ n²;
  I: the order estimate); CUT-N6 = N-CUT-10; CUT-N7 ↔ R2 §4.2 reproduction. REFEREE-2 only: N-CUT-1 (cite R89 as LANDED; I cited the landed R89
  but did not flag the packet's "draft" wording), N-CUT-4 (§0's §6 row omits own-cycle; I MISSED it), N-CUT-7 (frame τ_{j−1} also at j; my §1
  states it, not as a note), N-CUT-8 (FRESH-SPLIT's LATE is R88-blocked, a late adoption only inside one W-run). Mine only: MUT 5 (the new-τ
  frame breaks W-MON′, 22 hits), OPT-OFF's necessity datum also at t = 0 → 1 on tog6b. None is an E-item on the packet.
- Line (00:56Z proposal): both rejected it for the same two reasons (SC* underdefined: my CUT-E1 = R2's REQUIRED SC*; "iff" beyond CUT-POLY:
  my CUT-E2 = R2's; both supplied the same converse) and the same missing symbols (T, m_E; R2 also REQUIRED the R86 / R88 / R89 citations,
  which I listed as CITE).

## 2. K0 (the corrected line), word by word against my §10b table
| §10b row | K0 text | status |
| --- | --- | --- |
| N5 (SPEC S1-S5) | «N5 on EVERY game, under the standing SPEC premise of RESULTS R57 …» | ✓ in substance; precision: "N5 (SPEC S1-S5)" as R89's line (K0-P1, optional) |
| every run | «T is the number of transitions (iterations) of the run»; the maxima are "inside one λ-run" / "one W-run" of it | ✓ |
| T | defined | ✓ (missing symbol 1 of 4: FIXED) |
| n | «n = |V|» | ✓ |
| m_E | «the number of edges leaving Even vertices» | ✓ (missing symbol 2 of 4: FIXED) |
| K | «K := n(n−1) + (n(n−1)+1)(n−1)(m_E + REP* + 1)» | ✓ = §8 |
| formula | «T ≤ 2n(n−1) + (n(n−1)+1)·(m_E·[1 + 2B* + (B*+1)·K] + SC* + O*)» | ✓ = §8 (1 + B* + B*) |
| λ-run, λ^U-run | «as in RESULTS R86» | ✓ (CITE done) |
| W-run | «as in RESULTS R89» | ✓ |
| late adoption | «as in RESULTS R88 / R89» | ✓ |
| B* | «transitions inside one λ-run that are Even S4c fallbacks or change τ» | ✓ = §8 |
| REP* | «REPEAT late adoptions (a second or later late adoption of the same Even edge) inside one W-run» | ✓ = §6 / §8 |
| re-entry, W (inside SC*) | «re-entries of Even edges in R of class S (W-silent) or C (own-cycle) of P-N5-CUT §4 (W read against τ_{j−1}, smallest anchor)» | ✓ by citation of the packet's §4, which defines leave / re-entry, anchor, the classes and W^τ (missing symbols 3, 4 of 4: FIXED by citation) |
| SC* (CUT-E1) | «the largest number, over λ-runs R, of [those] re-entries» | ✓ = max_R Σ_{(v, c)} (#S + #C). CUT-E1 DISCHARGED: the frame τ_{j−1} and the smallest anchor are named, and §4 (not §6) is the cited source |
| O* | «τ-changing transitions inside one λ^U-run» | ✓ |
| "iff" (CUT-E2) | «T is polynomial if and only if B*, REP*, SC* and O* are (Corollary CUT-POLY and its converse, fixes K1)» | ✓ CUT-E2 DISCHARGED, given K1 (signed in §3) |
| via-clause | «LATE-SPLIT (first late adoptions ≤ m_E per W-run, R*_T ≤ m_E + REP_F)» | ✓ in content; REP_F and R*_T are not defined in the line (REP_F = the REPEATs of one W-run F, R*_T as in R88). Precision K0-P2 (optional): "R*_T (RESULTS R88) ≤ m_E + REP_F, REP_F the REPEATs in F" |
| standing premise | «under the standing SPEC premise of RESULTS R57 (S1's procedure realises the optimal counterstrategy)» | ✓ (CUT-N1 at line level; K2 adds R17 (a) (F1) + R57 (a) in the fixes) |
| scope | «a REDUCTION (none … bounded here; CONJECTURE REP-LIN is DEAD (L-RED R128, latew_K20_m32); not M3, not a step-4 pass, not a TARGET.md claim; G-N5-TIME stays open)» | ✓ |
| other premises (R15 (d), R17 (a), R47 (a)) | not named in the line | optional (K0-P3): R89's line also names its landed premises only through its objects; not required |
Symbols in K0 I listed and found: every one (N5, T, n, m_E, K, B*, REP*, SC*, O*, λ-run, λ^U-run, W-run, late adoption, Even S4c fallback,
τ-changing transition, re-entry, class S / C, W, τ_{j−1}, anchor, R*_T, REP_F). Only R*_T and REP_F, inside the "via" parenthetical, are not
defined in the line itself (K0-P2). Verdict (Opus 5.5, D15): K0 MATCHES Theorem CUT-RED, Corollary CUT-POLY and K1, and claims nothing
more. CUT-E1 and CUT-E2 are discharged; the four missing symbols are supplied. K0-P1..P3 are optional precisions, not blockers.

## 3. K1 (converse of CUT-POLY), as written
SIGNED (Opus 5.5, D15). B* and O* count transitions of the run: ≤ T. A late adoption is the switch of one Even vertex at one transition of a
W-run, so REP* ≤ (late adoptions in one W-run) ≤ |V_E|·T ≤ n·T. A re-entry of an Even edge is the switch of one Even vertex at one transition,
so SC* ≤ |V_E|·T ≤ n·T. Hence T ≤ q(n) on every run gives all four ≤ n·q(n). (= my CUT-E2 text and REFEREE-2's §8 converse.)

## 4. K2-K11: clarifications only?
| item | content | widening? |
| --- | --- | --- |
| K2 | standing premise: R17 (a) (F1) on A + R57 (a) (VJ), under R57 / R51 (d)'s 1E-N3; G-N5T-1 for DATA only | no (names a premise; answers CUT-N1 / N-CUT-2) |
| K3 | cite RESULTS R89 (landed) for "R89 draft" | no |
| K4 | OPT-OFF (ii) first bullet and Case 3: the triple identity, injective rewards, Fact DELTA | no (answers CUT-N2 / N-CUT-3; matches both derivations) |
| K5 | §0's §6 row read with the body's form (W-rise, W-silent or own-cycle) | no (restores the signed body; N-CUT-4) |
| K6 | [P-REP] note: REP-LIN DEAD (R128; also L-SI box 46 data), [P-REP] open | no (a READING; the added box-46 citation is DATA, not signed) |
| K7 | m_E ≤ n²; the order estimate | no |
| K8 | every W*, incl. W*_j, in the frame τ_{j−1} | no (the packet's definitions already say so) |
| K9 | FRESH-SPLIT's LATE is R88-BLOCKED at j − 2; a late adoption in R89's sense only if j − 2, j − 1, j lie in one W-run | no: it claims less than nothing new ("only if" is a necessary condition, not asserted to hold) |
| K10 | rename §6's SIL_F / CYC_F to SIL^REP_F / CYC^REP_F | no (notation; §8 uses only §4's) |
| K11 | data notes; new CONJECTURE REP-WPAID (every REPEAT W-paid) "not used anywhere" | no: a labelled CONJECTURE, used by no signed item; the corpus list in K11 is REFEREE-2's and mine (DATA) |
Verdict: K2-K11 are clarifications / readings; none widens a signed statement. K1 is the only new signed statement; K0 the only line.

## DONE / FINDINGS / NEEDS
- DONE: this §C (R-N5-CUT-C.md).
- FINDINGS: verdicts identical with REFEREE-2, gap map empty, every PROVED item signed by both; K0 MATCHES (CUT-E1, CUT-E2 discharged, 4
  symbols supplied; optional precisions K0-P1..P3); K1 SIGNED as written; K2-K11 clarifications only. I missed N-CUT-4 (§0's row); recorded.
- NEEDS: Lead: K0 is ready for CHECKER as far as I am concerned (optionally with K0-P2: define REP_F / cite R88 for R*_T in the parenthetical).

- K12 check (Lead 02:41Z; l-si fd1cb0bc docs/si/P-N5-CUT-fixes-box43.md sha1 95584f7e3e7c928e1aadf1ea684ebb9d764e3927 re-measured; my own word diff of the K0 and K12 lines, whitespace-normalised, written 02:42Z by date -u): K12 = K0 + P1-P3 exactly; MATCHES (Opus 5.5, D15).
