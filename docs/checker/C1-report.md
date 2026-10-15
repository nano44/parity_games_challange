# C1: landing-gate check of RESULTS R1 (L4) and R2 (T-A1) (CHECKER, 2026-10-15)

Scope: what landed on trunk against what was signed, and re-runs of every listed computation on the exact signed commits.
No mathematical judgement (two referees did that). Trunk checked: claude/vibrant-johnson-nxvvxo at 631d4a5 (docs/RESULTS.md
as of cdf7ecc). Worktrees: detached, clean (`git status --porcelain` empty before and after every run) at l-struct 50dc28b,
l-attr 57a1515, referee d1e065b, referee-2 d76c9e1 and 2eb1a2d. Python 3, python-sat 1.9.dev15; Oink built at 8fbf0a7 by
scripts/setup_oink.sh (not used by any re-run below: all scripts are pure Python). Every script run with `python3 -I`.

## Verdicts
| item | R1 (L4) | R2 (T-A1) |
| --- | --- | --- |
| 1. Blob identity | PASS | PASS |
| 2. Statement diff | FAIL (minor, Lead-side wording: D1-1 quantifier range, D1-2 hypotheses; rest notes) | PASS with notes (D2-1..D2-4) |
| 3. Vocabulary | FAIL (V1-1: "class (i)-(iii)" and "TARGET alphabet" defined in files not on trunk and not cited) | PASS with notes (V2-1..V2-3) |
| 4. Re-runs on exact commits | PASS (3/3) | PASS (9/9) |
| 5. Gap list | PASS | FAIL (G2-1: HKP Thm 5(1) black box missing; G2-2: G11 closure differs between the referees) |
| **Overall** | **FAIL until RESULTS is edited** (no new referee work needed) | **FAIL until RESULTS is edited and the first referee answers G2-2** |

Nothing found contradicts the signed mathematics; every computation re-ran with identical output. The failures are
wording/reference defects in docs/RESULTS.md and one referee-level inconsistency to be resolved by the first referee.

## 1. Blob identity (`git hash-object <trunk file>` vs `git rev-parse <sha>:<path>`)
| file | signed commit | trunk blob | signed blob | |
| --- | --- | --- | --- | --- |
| docs/struct/L4-proof.md | l-struct 50dc28b | 5f75ea9 | 5f75ea9 | MATCH |
| docs/struct/S1-statement.md | l-struct 50dc28b | 768a730 | 768a730 | MATCH |
| docs/attr/TA1-proof.md | l-attr 57a1515 | f58968f | f58968f | MATCH |
| docs/attr/A1-results.md | l-attr 57a1515 | c0d62df | c0d62df | MATCH |
| docs/referee/2026-10-14-L4-proof-check.md | referee 9bf5301 (= referee head) | 613579f | 613579f | MATCH |
| docs/referee-2/R2-L4.md | referee-2 d76c9e1 | 36d8e00 | 36d8e00 | MATCH |
| docs/referee/2026-10-14-TA1-proof-check.md | referee d1e065b | fa62116 | fa62116 | MATCH |
| docs/referee-2/R2-TA1.md | referee-2 2eb1a2d | f996cd6 | f996cd6 | MATCH |
TA1-proof.md blob f58968f is the blob both T-A1 signatures name. Note: l-struct has moved past 50dc28b (head 729c965); the
only later change to L4-proof.md (f465acd) rewrites the Status paragraph (3 lines, no statement or proof text). Trunk
correctly carries the signed 50dc28b version. l-attr head is 57a1515 itself.

## 2. Statement diff
### R1 (L4). Signed texts: first referee "Lemma L4.1, Lemma L4.2, Theorem L4, Corollaries L4.3 and L4.4 ... hold as stated"
at 50dc28b (gaps G1-G6); REFEREE-2 §7: the Lead's 23:48Z wording, quoted there. RESULTS R1 against those:
- D1-1 (quantifier range; FAIL). RESULTS: "max over even d' ≤ n". Signed (file §1 and R2-L4 §1): "d' even, 2 ≤ d' ≤ n". The
  lower bound is missing; at d' = 0 the term ⌊n/d'⌋ is undefined. Fix: "max over even d' with 2 ≤ d' ≤ n".
- D1-2 (hypotheses / labelling). RESULTS: "Lemma L4.1 (a)-(b) for infinite words (s^E(k,d) ≤ s^V(kd,d), likewise w; ...)".
  In the file, (a)-(b) are the path and cycle facts; the inequalities are the statement of L4.1, proved via (c)-(d) and
  stated "for all k ≥ 1 and d ≥ 2". RESULTS attaches the inequalities to "(a)-(b)" and drops k ≥ 1, d ≥ 2. Both referees
  signed the inequalities (first referee: L4.1 OK; REFEREE-2 verdict table: L4.1 OK, (c)-(d) re-derived as part of Theorem
  L4), so the substance is signed; the wording is not the signed one. Fix: "Lemma L4.1 (k ≥ 1, d ≥ 2): s^E(k,d) ≤ s^V(kd,d)
  and w^E(k,d) ≤ w^V(kd,d); its parts (a)-(b) for infinite words".
- D1-3 (note). Theorem L4 "for n ≥ 2": matches REFEREE-2's signed wording; the signed FILE still says "for all n ≥ 1"
  (REFEREE-2 F1-F3 were not applied to L4-proof.md at 50dc28b). The landed claim is narrower than the file, as REFEREE-2
  intended; the first referee signed the file's "as stated", which covers n ≥ 2. Not a defect; recorded.
- D1-4 (note). Corollary L4.3: matches REFEREE-2's wording (C(a0+b0, a0) for n ≥ 64; S(n) = n^{Ω(lg n)}). The file's last
  closed form (√n/(2 lg n))^{⌊½ lg n⌋−2} is not in RESULTS (correctly: it exceeds 1 only from n = 257, R2-L4 F2).
- D1-5 (note). Corollary L4.4: matches REFEREE-2's theorem-part wording; literature sentence excluded in both. The first
  referee signed L4.4 including the literature sentence ("CDFJLP §3.3's remark, cited"); RESULTS excludes it. Narrower; fine.
- Lemma L4.2, signature SHAs (9bf5301, d76c9e1), "Status: supporting lemma (L7)": match.

### R2 (T-A1). Signed texts: first referee signature block (referee d1e065b); REFEREE-2 §8 (Lead's 23:51Z wording).
- Theorem T-A1: matches ("for every finite parity game G (TARGET §1)"; the file says "every parity game G" with TARGET §1
  vocabulary, which makes G finite). OK.
- T-A1' with converse false, witnesses HKP Fig. 4(a) and `0 0 1 0,1; 1 2 0 0`: matches the first referee's block word for
  word; REFEREE-2 signs "with 'the converse fails'". The file names only Fig. 4(a); the n = 2 game is in A1-results.md §n=2
  row and R2-TA1.md F5. OK.
- Corollaries 1-2 "as stated in the file", Remark 3, Remark 4 excluded: match both signatures.
- D2-1 (note). "arXiv 1405.0386": the file and both referees use v2 (1405.0386v2). Add "v2".
- D2-2 (note). RESULTS' gloss of Corollary 1 omits the file's qualifier "Büchi ... up to an order- and parity-preserving
  recolouring"; covered by "as stated in the file".
- D2-3 (note, excluded part). RESULTS: "Remark 4 (PA ⊊ PA* ⊊ PA**, data only)". The file: PA* ⊆ PA** re-derived by both
  referees; only PA ⊆ PA* is data only; strictness by named instances. Suggest "(PA ⊊ PA* ⊊ PA**; PA ⊆ PA* data only)".
- D2-4 (note). Remark 3 gloss "holds for every stable colour order" vs the first referee's "for HKP's stable sequences":
  same notion (HKP Thm 6). OK.

## 3. Vocabulary (TARGET v1.0 conventions: max-parity, vertex priorities, pr : V → {0..n})
### R1
- s^X, w^X, strong/weak separator, conventions E/S/V, Σ_d = {1..d}, EvenCycles, LimsupEven: S1-statement.md D1-D5 (on trunk,
  cited). Max-parity: S1 §1 and D2 (cycle even iff largest label even). Vertex priorities: convention V (D1). OK.
- S(n) = s^V(n,n): defined inline in RESULTS; also S3 D6 (not on trunk). OK.
- V1-1 (FAIL). "algorithm of class (i)-(iii)" is defined in S2-lower-bound-statement.md §1 (l-struct 50dc28b) and S3 D6;
  "the TARGET alphabet" is a referee term (R2-L4 §1, §7) whose meaning is S3 D6 ("letters = TARGET priorities, 0 removed by S1
  Lemma 2(b-V)") or S2 §1 (shift to {2..n+2}). Neither S2 nor S3 is on trunk or cited by RESULTS R1. Fix: cite
  docs/struct/S2-lower-bound-statement.md §1 and S3-statement.md D6 at l-struct 50dc28b (or copy them to trunk), and say
  "TARGET alphabet = priorities {0..n} with 0 removed by S1 Lemma 2(b-V), i.e. Σ_n".
- V1-2 (convention note). Letter d. In S1 (§1, "d here is the largest letter, NOT TARGET's d = |pr(V)|") and in all of R1,
  d and d' are the largest letter, while TARGET §1 uses d = |pr(V)|. RESULTS R1 uses d, d' without the warning. Add it.
- V1-3 (convention note). TARGET priorities {0..n} vs separator alphabet {1..n}: bridged by S1 Lemma 2(b-V) (needs n ≥ 2;
  n = 1 checked directly), which RESULTS does not mention; REFEREE-2 notes L4.4's theorem part does not need it (s^E ≥ s^V,
  L4.2). Consistent with the n ≥ 2 restriction. No min-parity anywhere in R1.
### R2
- PA**(G), (p,d)-peelable, recurrent set, MAttr, trap, "solves completely" (HKP Def. 8): TA1-proof.md §1 (on trunk), in
  TARGET's max-parity with vertex priorities. OK.
- psolB, psolQ: HKP Fig. 3 / Fig. 5, which work in MIN-parity colours; TA1-proof.md header restates every HKP notion in
  max-parity (colour = M − priority, "colour ≥ c" ↔ "priority ≤ d"); both referees' code translates the same way
  (ta1check.py, R2 validate.py "pr = M - c with M even"). Convention handled; no mismatch in the landed text.
- V2-1 (note). "HKP's Büchi ... class": HKP's min-parity colours {0,1}; the file's Corollary 1 gives the max-parity form
  (two consecutive priorities, even on top) up to recolouring. RESULTS defers to the file. OK.
- V2-2 (note). "deterministic games" (HKP Lemma 5) and "SCC-constant" are HKP's notions, named but not defined in TA1-proof.md.
  Suggest one line each (deterministic: every vertex has exactly one successor, as read by ta1check.py's class test).
- V2-3 (note). The witness `0 0 1 0,1; 1 2 0 0` is in the fleet's "id priority owner successors" game format (owner 1 = Odd;
  R2-TA1.md F5 spells it out). Priorities {0, 2} ⊆ {0..2}: within TARGET. Suggest naming the format once.

## 4. Re-runs on the exact commits (outputs in the CHECKER scratchpad; summaries below)
### R1
| run | commit | result |
| --- | --- | --- |
| experiments/weak-sep/l4_bound.py | l-struct 50dc28b | PASS: 36/3, 816/28, 52360/680, 11716640/46376, 25761160440576/6547258432 (d' = 16, 32, 64, 256, 1024); "closed form <= optimised bound for all n <= 5000: ok"; equals the values quoted in L4-proof.md §4 |
| docs/referee-2/R2-L4/l4_numeric.py | referee-2 d76c9e1 | PASS: output byte-identical to committed results_numeric.txt ("chain violations for 64 <= n <= 20000: none"; last form > 1 from n = 257), 16 s |
| docs/referee-2/R2-L4/l41_bruteforce.py | referee-2 d76c9e1 | PASS: byte-identical to results_bruteforce.txt ("4396 graphs, 0 failures"), 7 s |
### R2
| run | commit | result |
| --- | --- | --- |
| experiments/attr/check.sh | l-attr 57a1515 | PASS: "validate --quick: PASS", 5 instance outcomes and 5 PA*/PA** checks as asserted, "n=2: all 240 canonical games solved by psolQ" |
| experiments/attr/validate.py (full) | l-attr 57a1515 | PASS: 18 ok, 0 FAIL, "VALIDATE PASS" |
| experiments/attr/exhaustive.py 3 --all-strahler | l-attr 57a1515 | PASS: 41,440 games; out/summary_n3.txt identical to committed results/summary_n3.txt except the time line |
| experiments/attr/peeling.py --pa2 3 | l-attr 57a1515 | PASS: identical to committed results/pa2_n3.txt; "PA** => psolQ solves: HOLDS; PA** => psolB solves: HOLDS; psolB solves => PA**: HOLDS; psolQ solves => PA**: FAILS (3016)"; buchi/scc/det => PA**: HOLDS |
| docs/referee/scratch/ta1check.py (full) | referee d1e065b | PASS: n = 1, 2, 3 exhaustive (4, 324, 175,616 games) and random n = 4, 5: 0 problems on every line; counts equal the first referee's §5 table (168,080 / 175,376 / 168,080 at n = 3; 27,608 / 29,881 at n = 4; ...); Fig. 4(a) as expected |
| docs/referee-2/R2-TA1/validate.py | referee-2 2eb1a2d | PASS: 24 ok, "validate.py: ALL OK" |
| docs/referee-2/R2-TA1/search.py exhaustive 1, 2, 3 | referee-2 2eb1a2d | PASS: identical (time stamps aside) to committed results/exh_n1..3.txt; n = 3: 175,616 games, T-A1 both directions HOLD, T-A1' HOLDS, routed iff FAILS (7,296), order independence HOLDS |
| docs/referee-2/R2-TA1/compare_lane.py <57a1515 experiments> 3 0 0 | referee-2 2eb1a2d vs l-attr 57a1515 | PASS: "175616 games: psolB residual differs on 0, psolQ on 0, PA** on 0"; identical to results/compare_lane_n3_exh.txt |
| docs/referee-2/R2-TA1/hkp_thm4_strategy.py (side finding in RESULTS) | referee-2 2eb1a2d | reproduces: minimal-rank strategy loses (v u v u ..., min Inf colour 1), witness strategy wins |
Not re-run (outside the bounded scope): the lane's 27.3M n = 4 enumeration (about 30 min on 3 workers; README gives
deterministic sha256 for out/fail_n4.jsonl, re-runnable on request), random n = 4, 5, 6 searches beyond ta1check.py's.

## 5. Gap lists
### R1: PASS
RESULTS: "Gaps (union, see R2-L4.md §7): CDFJLP Thm 5.1 ... black box (G-L4-1); first referee G1-G6". R2-L4.md §7 lists the
union G1/G-L4-2, G2, G3/G-L4-1, G4/G-L4-3, G5, G6 and "nothing Lean-checked"; this covers every gap in both reports
(first referee G1-G6; REFEREE-2 G-L4-1..3). By reference: complete. (docs/GAPS.md row G1 now records G-L4-1 too.)
### R2: FAIL
RESULTS: "G1-G9 closed; G10 open ...; G11 (HKP Thm 4) closed at referee level by re-derivation"; side finding on Thm 4.
- G1-G11 statuses match REFEREE-2 §8 and the first referee's table. OK.
- G2-1 (missing). The first referee's "Gaps (steps not machine-checked)" lists items not in RESULTS, directly or by
  reference: HKP Thm 5(1) used as a black box for Corollary 2's O(|V|^2 |E|) bound; DJT §2 (trap definition) not opened by
  the first referee; Invariant I, L1, O, the "only if" induction and Lemma 0 are prose re-derivations, machine-checked only
  in extension on the searched games; nothing Lean-checked. (HKP Thm 2 is covered by G9.) Fix: add "HKP Thm 5(1) black box
  (Cor. 2); prose-only steps as listed in the first referee's 'Gaps' section" or reference that section and R2-TA1.md §8.
- G2-2 (inconsistency between the two signatures; not a CHECKER judgement on the mathematics). Both referees close G11, but
  by different arguments. The first referee's table (d1e065b) re-derives HKP Thm 4 with "the rank-(d,i) strategy" from HKP's
  text (tex:1067-1125). REFEREE-2 (2eb1a2d, later) shows that HKP's strategy as written (minimal-rank successor, tex:1085-1088)
  is unsound (instance re-run above) and closes G11 only with the witness-successor repair. The first referee's sentence "each
  step goes to X ... or to a smaller rank" is true of the witness choice, not of the minimal-rank choice in that instance; the
  first referee does not say which choice is meant. RESULTS' "closed at referee level by re-derivation" therefore rests on
  REFEREE-2 alone for the repaired strategy. T-A1' uses Thm 4 (F1'). Needed: the first referee confirms that their G11
  derivation uses a witness successor (or adopts REFEREE-2's repair), in writing, on the referee branch.
- Note: TA1-proof.md at 57a1515 still says G11 "Open until re-derived" and G10 "Open until a second signature"; the closure
  status lives in the referee reports, which RESULTS cites. Not a defect.

## Fix list for the Lead (RESULTS.md only, plus one referee answer)
1. R1: "max over even d' with 2 ≤ d' ≤ n" (D1-1).
2. R1: L4.1 wording with k ≥ 1, d ≥ 2, inequalities as the lemma, (a)-(b) as its parts (D1-2).
3. R1: cite S2 §1 and S3 D6 at l-struct 50dc28b (or land them) for "class (i)-(iii)" and "TARGET alphabet"; add the
   "d = largest letter, not TARGET's |pr(V)|" note (V1-1, V1-2).
4. R2: add the missing gaps (G2-1); "arXiv 1405.0386v2" (D2-1); optionally D2-3, V2-2, V2-3.
5. R2: first referee's written answer on G11 (G2-2).
After 1-5, CHECKER re-checks the RESULTS text only (the blobs, re-runs and signatures above stay valid while the signed
commits and trunk files are unchanged).

## C1-recheck (CHECKER, 2026-10-15 ~00:10Z): RESULTS.md text at trunk 4b9cb6e
Scope as asked: the RESULTS text, the blobs of the newly copied files, and the first referee's G11 answer. The signed
commits are unchanged, so the re-runs of section 4 stay valid and were not repeated.

### Blob identity (git rev-parse 4b9cb6e:<path> vs <signed sha>:<path>)
| file | signed | trunk blob | |
| --- | --- | --- | --- |
| docs/struct/S2-lower-bound-statement.md (new) | l-struct 50dc28b | 3347517 | MATCH |
| docs/struct/S3-statement.md (new) | l-struct 50dc28b | f4f4705 | MATCH |
| L4-proof.md, S1-statement.md | l-struct 50dc28b | 5f75ea9, 768a730 | MATCH (unchanged) |
| TA1-proof.md, A1-results.md | l-attr 57a1515 | f58968f, c0d62df | MATCH (unchanged) |
| docs/referee/2026-10-14-TA1-proof-check.md | referee 5ff8edb | 04246ee | MATCH |
| R2-L4.md, R2-TA1.md, L4 first-referee report | d76c9e1, 2eb1a2d, 9bf5301 | unchanged | MATCH |
| docs/checker/C1-report.md | checker e8a2a8d | ba342a6 | MATCH |
The first referee's 5ff8edb change is append-only (`git diff d1e065b 5ff8edb`: 28 insertions, 0 deletions). The
signature block and gap table signed at d1e065b are untouched.

### R1 (L4): fix items
- D1-1: "max over even d' with 2 ≤ d' ≤ n": FIXED, matches L4-proof.md §1 and R2-L4 §1.
- D1-2: "Lemma L4.1, for k ≥ 1 and d ≥ 2, on infinite words: s^E(k,d) ≤ s^V(kd,d) and w^E(k,d) ≤ w^V(kd,d)": FIXED.
  It matches the file's hypotheses. "On infinite words" is the signed restriction of (a)-(b).
- V1-1: S2 §1 (class (i)-(iii)) and S3 D6 (S(n), letters = TARGET priorities with 0 removed) are cited and landed
  (blobs above): FIXED. I checked that S2 §1 lines 42-45 define the class (i)-(iii) and S3 D6 defines S(n) and the letter set.
- V1-2: the convention note ("d is the largest letter of Σ_d = {1..d}, not TARGET's d = |pr(V)|") is added: FIXED.
- Notes (non-blocking):
  - (n1) The phrase "TARGET alphabet" is used in S3 in two senses: Σ_n after removing 0 (line 33, D6) and {2..n+2} after
    the +2 shift (line 56 table). RESULTS points to D6. Per R2-L4 §1/§7, L4.4's theorem part holds for either encoding, so
    the ambiguity does not change the claim.
  - (n2) S2 §1's class (i)-(iii) sits inside the statement of target T1, which is refuted (dead end DE2). The class
    definition does not depend on T1; a reader should not take the citation as reviving T1.
- Other R1 text: unchanged from the first check and matching.
**R1 overall: PASS.**

### R2 (T-A1): fix items
- D2-1: "arXiv 1405.0386v2": FIXED.
- D2-3: Remark 4 is now "inclusions among the predicates PA, PA*, PA**; data only, not signed", still excluded: FIXED
  (neutral wording; nothing excluded is claimed).
- G2-1: "Corollary 2 uses HKP Thm 5(1) as a black box (first referee's list); all steps are prose, nothing machine-checked
  beyond the data searches": FIXED.
  - Residual note (non-blocking): the first referee's line "DJT §2 (trap definition) not opened by me" is not in RESULTS.
  - Why non-blocking: it discloses which source a referee did not open for a definition. TA1-proof.md §1 states that
    definition in full and both referees checked it. It is not a gap in any step of the proof.
  - The Lead may add it for completeness.
- G2-2: the first referee answered (b) in writing at referee 5ff8edb.
  - They agree that HKP's minimal-rank strategy as written is unsound, and reproduced REFEREE-2's instance with their own code.
  - They state that their G11 sentence was the witness step, named imprecisely.
  - They re-derive Thm 4 with the witness successor, close G11 on that basis, and reconfirm the 57a1515 signature.
  - RESULTS now says G11 is closed "ONLY with REFEREE-2's witness-successor repair ... (both referees: REFEREE answer (b),
    referee 5ff8edb ...)". This matches both reports. RESOLVED.
  - I record the referee's answer as given; I do not judge its mathematics.
- Note (non-blocking): the R2 "Referees" bullet still cites the first referee's signature at d1e065b. The reconfirmation is
  at 5ff8edb, which the Gaps bullet cites. Both SHAs are correct for what they name.
- The R2 heading still reads "CHECKER re-check pending". The Lead should update it to this re-check.
**R2 overall: PASS.**

### Re-check verdict
| entry | 1 blobs | 2 statement | 3 vocabulary | 4 re-runs | 5 gaps | overall |
| --- | --- | --- | --- | --- | --- | --- |
| R1 (L4) | PASS | PASS | PASS | PASS (section 4) | PASS | **PASS** |
| R2 (T-A1) | PASS | PASS | PASS | PASS (section 4) | PASS | **PASS** |
Validity:
- Both verdicts hold for trunk 4b9cb6e's RESULTS text and the signed commits l-struct 50dc28b, l-attr 57a1515, referee
  9bf5301 / 5ff8edb and referee-2 d76c9e1 / 2eb1a2d.
- Any later change to one of those files or to the RESULTS entries needs a new CHECKER pass.
