# R2-P-N5-QN: second-referee report on packet P-N5-QN (L-NEW successor 68, box 203)
REFEREE-2 successor 35 (Opus 5.5, D1). Written 2026-11-09 by date -u (times in the commit). Independent: docs/referee/ NOT read for this
packet before this report is committed. L-RED 63's attack (claude/l-red 8c034440, cdecc4e0) is context only, and I did not read it. §7's
related lane statements are cited by the packet, not used by it, and I did not use them.

## Object (claude/l-new e252182d, FROZEN)
- docs/new/P-N5-QN.md at e252182d: sha1 97254bd2a97f28bb0c14ab5f4d236ee723821dd9, 20,725 B (= the brief), re-hashed by `git show`.
- No fixes file and no line exist at e252182d. This report reviews the packet. The line will be byte-tested when sent.
- Pins: experiments/new/box203/qn.pins, 56 rows. All match on a git archive of e252182d (`sha1sum -c --quiet` exit 0, the sed of the
  check.sh «P-N5-QN» block).
- Instances re-hashed on the archive: k1fail_202 99bba752, MWR4_2 856d369b, MWR8_2 918f1414, MWR16_2 2ccda9a9, ST4_k1 3fa71a98, ST8_k1
  9dbf71f4, K1C16_n400 99da972a, K1F21_n48 2e7460da. All equal the packet's.

## Verdicts (Opus 5.5, D1)
| statement | verdict | note |
| --- | --- | --- |
| Theorem GATE-CLASS | SIGN | every genome, IDEAL-CYC |
| Corollary GATE-FLIP (a) | SIGN | |
| Corollary GATE-FLIP (b) | SIGN | (2M + 3)·F′_B(M) per face from R121's whole-run form; B = U(G) under HYPOTHESIS [E-LEV] (R121 UP-B) |
| Corollary QUIET-N | SIGN | sharpens R123 QUIET / T-QUIET: window L → N |
| Lemma (k+1)-Λ | SIGN WITH W-1 (wording) | the count k + 1 is right; the statement's description of the values is wrong as written (W-1); the line must use the corrected wording |
| DEAD D1, D2, D3 | SIGN (dead) | each instance re-run on my own code |

No statement is REFUSED. W-1 is a wording defect in (k+1)-Λ's statement, not in its proof. The proof identifies the values correctly.

## Premises (own script R2-P-N5-QN/r2q.py, out r2q.out; trunk 547985a10)
- Every «…» of §1: 24 quotes. All 24 are verbatim (whitespace-normalised) in trunk docs/RESULTS.md or P-N5-XICYC.md, each in the entry the
  packet names:
  - R104: [DEF], 6 quotes.
  - P-N5-XICYC: the shape line.
  - R118: [VJ] header, the C / R / p labels, (a), (d) BR-SEG, (e), T-CYC.
  - R121: E-MON, the HUB-ASC-G whole-run form, UP-B.
  - R123: CN2, B-ONLY, NO-TIE, LOC-GATE, LOC-K2, class / loud / quiet, QUIET's L, T-QUIET.
- R104, R118, R121 and R123 are all landed at 547985a10. No lane packet and no L-RED / L-SI lemma is a premise. §7 is labelled READING.
- Readings (D1)-(D5) of [DEF] checked against R104's text:
  - (D1): e_g's only in-edge is from g.
  - (D2): E-DOM. Only e's, c_W (top), K0 (top + 2) and K3 (top + 3) are above the e's.
  - (D3): the core is entered only at u = K0 (β's escape edge).
  - (D4): c_X has only its loop.
  - (D5): the Ξ-graph and k(G).
  All are correct.

## Re-derivation (every step redone)
- (C1): Λ_t(v) moves only to a strictly larger reward (R118 (e)), and at fixed Λ the e-set only rises (E-MON). So the classes of v strictly
  increase and never repeat, and class(v) changes at exactly D^tot(v) − 1 steps. Correct.
- GATE-CLASS. Assume neither face's class changes at t, so Λ and E of a = e_g and b = β_g are equal at s = t − 1 and s = t.
  - Case 1 (w_a ≠ w_b): distinct cycle nodes have distinct rewards, so the faces' order is fixed. By LOC-GATE (strict, NO-TIE) σ̄_s(g) is
    the same face. Correct.
  - Case 2 (w_a = w_b = w). If a → c_W, then Λ(a) = c_W, while b is not a B-ONLY exception, so Λ(b) ≠ c_W: back in Case 1. Otherwise B-ONLY
    puts w below every e. a is the first vertex of its play and more relevant than w, so a is on the prefix and e_g ∈ E_s(a).
    - 2a (e_g ∉ Π_s(b)). The most relevant z of Π(a) Δ Π(b) is e_g or above, hence an e-vertex, c_W, K0 or K3 (E-DOM). c_W is in no Π: a
      play reaching it has node c_W, which B-ONLY excludes for both. For K0 and K3: a and b are NON-core vertices. A non-core play enters
      the core only through K0, then frozen K0 → K3 → K2, σ̄(K2) = K1 (LOC-K2), frozen K1 → K1. So it contains K0 iff K3 iff its node is K1.
      With equal nodes both Π's hold both or neither. (Here the argument is stated correctly for non-core vertices, unlike P-N5-CHAIN's
      W-1.) So z is an e-vertex (even), the most relevant element of π(E(a)) Δ π(E(b)), and the face with the lex-smaller π(E) has the
      smaller value. σ̄_s(g) is a function of the π-pair. Correct.
    - 2b (e_g ∈ Π_s(b)). b's play passes e_g, whose only in-edge is from g (D1), so σ̄_s(g) = a. Correct.
    - Combination. PRIV at both times gives equal E's, so equal π-pairs and the same face. non-PRIV at both gives a at both. Mixed means
      e_g enters or leaves E(b), a class change of b, against the assumption. Correct.
- GATE-FLIP (a): every flip step is a class-change step of e_g or β_g. With (C1) the bound is exact as stated. (b): R121's whole-run form for
  v = e_g, β_g, and UP-B for B = U(G) under [E-LEV]. Correct.
- QUIET-N.
  - A quiet step has no class change, so no Λ change (no C).
  - The Odd vertices with a choice are the gates and K2 ([DEF]). Gates keep σ̄ by GATE-CLASS's contrapositive, and K2 keeps σ̄ = K1 by
    LOC-K2. σ̄ is unique (NO-TIE + LOC-GATE; LOC-K2 strict), so R118's «any fixed deterministic choice» is σ̄ and no R label occurs. So the
    step is a p-step.
  - A maximal quiet window lies inside a maximal p-run, which has at most N steps (BR-SEG). T_CYC = Q + (quiet steps) ≤ Q + (Q + 1)·N.
  - Q ≤ Σ_v (D^tot(v) − 1) by (C1).
  Correct. The comparison with R123 (L → N; ASC-T / UP-T with L + 1 → N + 1) is arithmetic on the landed text. Correct.
- (k+1)-Λ, proof.
  - Z := the cycle of v's play, w := its most relevant vertex = Λ_t(v). By B-ONLY, Z has no e-vertex (one would be more relevant than w)
    and is not c_W's loop.
  - If Z meets the core, w = K1: the core cycle under frozen moves and σ̄(K2) = K1 is K1's loop. Z is not c_X's loop (v ≠ c_X, (D4)).
  - Otherwise every gate on Z takes its β-face (no e on Z), and every β goes to its frozen start successor, the Ξ-target. A target X
    would lead into the core. So Z's movers form a cycle of Ξ_σ, and Z (hence w) is determined by it.
  - Ξ_σ has out-degree ≤ 1, so its cycles are disjoint, and each meets every Ξ-feedback set. So there are at most k of them. Correct.
- (k+1)-Λ, statement (W-1, wording).
  - The statement says the values are «K1, and the most relevant vertex of each cycle of the functional graph Ξ_σ on the movers». A cycle
    of Ξ_σ consists of movers only (priority 0), so read literally its most relevant vertex is a mover. A mover is never a cycle node (R123
    CN2).
  - The value that occurs is the most relevant vertex of the Γ-cycle Z through that Ξ_σ-cycle's movers, gates and β-faces. That vertex is
    a β, since β's outrank movers and gates. The proof says so («Z with w is determined by that cycle»).
  - My counters: lamid_mover (a Λ value that is a mover) is 0 on every run. lamid (a Λ value outside {K1} ∪ {most relevant vertex of the
    Γ-cycle of a Ξ_σ-cycle}) is 0 on every run.
  - Required wording for the line (and, if the Lead wants, a fixes-file note): «K1, and for each cycle of the functional graph Ξ_σ on the
    movers, x → xt(x, σ_t(x)), the most relevant vertex of the Γ-cycle through its movers, their chosen gates and β-faces».
  - The count «at most k + 1 values» and the proof are unaffected.
- DEAD list, re-run on my own code (pinned.out):
  - D1: k1fail_202 has k 1, and its gate with most flips has 2 flips, lamch 0, faces (2, 3), against the conjecture's 2·0 + 1 = 1. DEAD.
  - D2: MWR4_2 / MWR8_2 / MWR16_2 have k 1 and C = 0, and their max-flip gate has 9 / 17 / 33 = 2n + 1 flips (n = 4, 8, 16) at lamch 0.
    So no c·(lamch + 1) bound holds, and none with C as the denominator. DEAD.
  - D3: ST4_k1 / ST8_k1 have k 1 and max ascents 3 / 7 (> k + 1 = 2). K1C16_n400 and K1F21_n48 have 3 each. DEAD.

## DATA replay on my own engine (R2-P-N5-QN/r2qn.py on R2-P-ACYC/r2acyc.py; driver sweep.sh)
- Engine: my predecessors' r2acyc.py (builder, VJ values, Odd's optimum) and r2quiet.py's generator (levels; Ξ-targets anywhere, incl.
  upward and self). Howard at the movers with «keep, else the largest best». No lane code.
- Counters:
  - gc: GATE-CLASS flips with neither face changing class.
  - gf: GATE-FLIP (a).
  - qnotp: QUIET-N, a quiet step that is not a p-step (any Λ or any Odd σ̄ change).
  - qwin: a quiet window > N.
  - Tq, qsum: the two T_CYC inequalities.
  - lam: more than k + 1 Λ values, with k the EXACT Ξ-feedback number by brute force.
  - lamid, lamid_mover: as above.
  - cpay (record): L-RED's CLASS-PAYS.
- Sets: every genome file of the archive's box202/inst and box203/inst plus k1fail_202, and own random genomes, 3,000 at seed 2 and 3,000
  at seed 3.
- Results (pinned.out, gen2.out, gen3.out): every must-0 counter is 0 on every set, which covers gc, gf, qnotp, qwin, Tq, qsum, lam and
  lamid. lamid_mover is also 0 everywhere, and cpay (L-RED's CLASS-PAYS, record) is 0.
  - Pinned: 61 genome runs (3 «.names.json» files skipped as non-genomes). Max T 199, max quiet window 11, max flips(g) 130, max
    ascents 16.
  - (k+1)-Λ is counted on 41 of the 61 pinned genomes. On the other 20 (N > 30 and k > 3) my exact feedback search is too costly, and
    they are recorded as lamskip.
  - Random: 6,000 runs, k up to 7, max T 9, every counter 0.
- Per-gate records equal the packet's §9 on a different engine:
  - K1C16_n400: 31 flips, faces (22, 37), lamch 0, C 0.
  - K1F21_n48: 21, (12, 22).
  - MWR4/8/16_2: 9 / 17 / 33, faces (5, 10), (9, 18), (17, 34).
  - One difference, a record only: DSALT6_n108's longest quiet window is 11 on my engine, against the packet's 10. Both are ≤ N =
    108. Howard's tie rule is free in R118 (a), and the windows depend on it.
- Controls fire for every must-0 counter:
  - ctrl_gen.out (300 own genomes): gc 157, gf 105, qnotp 110, qwin 110, Tq 92, qsum 238, lam 165, lamid 686.
  - ctrl_pinned.out (k1fail_202, MWR4_2, MWR8_2): gc 28, gf 16.
  - The control definitions are in r2qn.py's doc. One tool bug was found and fixed before these runs: c_X is named «unused» in
    r2acyc.py, and my first exclusion set missed it, so lam / lamid fired on c_X's own loop.

## TARGET.md diff
- TARGET.md §2 (M4) asks for a polynomial algorithm on every parity game, and §4 l. 31 says a restricted class is not M4. QN proves a
  mechanism lemma, a per-gate bound and a sharper window bound on ONE model (IDEAL-CYC on R104 genomes). It makes no new class polynomial,
  and nothing transfers to N5′-xi, N5 or general games.
- So it is not M3, not M4, not a step-4 pass, and not a TARGET.md claim. G-N5-TIME stays OPEN. The packet's §10 says exactly this.

## For the line (when written)
- R-1 (REQUIRED, from W-1): state (k+1)-Λ's values as above, not as «the most relevant vertex of each cycle of Ξ_σ on the movers».
- GATE-FLIP (b) must carry «under HYPOTHESIS [E-LEV]» for B = U(G). QUIET-N must carry «sharpens R123» and its T_CYC ≤ Q + (Q + 1)·N form.
- If the line carries a DATA clause, it must name each must-0 counter's unit and condition as gfc203.py computes them (the DATA rule). I
  will read that tool line by line at the line's byte test.

## Statement of independence
My verdicts rest on my own derivations above and on my own engine. I did not read docs/referee/ for this packet, nor L-RED 63's reports.

## Addendum 1 (REFEREE-2 successor 36, Opus 5.5, D1; 2026-11-11 by date -u): fixes entry 1 + line L-1 at claude/l-new 02a928a3. L-1 MATCHES
- Object:
  - docs/new/P-N5-QN-line-L1.txt at 02a928a3: sha1 28bf566bdf95d0708b3b80303bfa7311c8d5d8b1, 7,357 B (= the Lead's), one line, no «|».
  - docs/new/P-N5-QN-fixes.md: sha1 b8f8a1a905c261c1f76bc3dc2a62bc37fa744bbc, entry 1.
  - The packet is unchanged: sha1 97254bd2…, the frozen one. e252182d is an ancestor of 02a928a3.
- Disclosure. Fixes entry 1 quotes REFEREE 30's findings (QN-1, LN-1..LN-8) in outline. My report (5d4f06c2) was committed before that
  entry existed. I read REFEREE's report only after this addendum's verdict (Addendum 2).
- Rebuild and pins.
  - On a git archive of 02a928a3, the lane generator box203/mkl1_qn.py, run with trunk 8ba1b23b's RESULTS as its argument, exits 0 and
    rebuilds L-1 byte-equal (28bf566b…). Before running it I read it: it only reads files and writes the line inside the archive.
  - Its assertions hold: the packet sha1; the governing sentence once in the fixes; R123's scope sentence and R124's TARGET tail verbatim
    in RESULTS; the skip counts.
  - box203/qn.pins: 61 rows. The check.sh «P-N5-QN» sed gives `sha1sum -c --quiet` exit 0. quotesqn.out reads «quotes 24 missing 0».
- Statements, line against the packet (+ fixes entry 1, which governs):
  - GATE-CLASS, GATE-FLIP (a), QUIET-N and DEAD D1-D3: same content as §2-§4 and §6. D3 lists the ST and WC instances. K1C16_n400 and
    K1F21_n48 are omitted, which is fine: ST suffices.
  - k's definition equals (D5). GATE-FLIP (b) carries «under HYPOTHESIS [E-LEV] (lev(x) < lev(x′) implies pr(e_(x,k)) < pr(e_(x′,k′))) B
    = U(G) … may be taken»: my requirement is met.
  - QUIET-N carries «sharpens RESULTS R123 Theorem QUIET / Corollary T-QUIET: window L → N» and «T_CYC ≤ Q + (Q + 1)·N»: met.
- R-1 ((k+1)-Λ, REQUIRED): MET. The line has «K1, and, for each cycle of the functional graph Ξ_σ on the movers, x → xt(x, σ_t(x)), the
  most relevant vertex of the Γ-cycle through its movers, their chosen gates and β-faces; Ξ_σ has at most k cycles». My required string
  had «K1, and for each»; the line has one extra comma, «K1, and, for each». The meaning is identical. I accept it.
  - N-a (optional, no change needed): «options whose Ξ-target is X omitted» sits in k's definition of the Ξ-graph. Ξ_σ is a subgraph of
    it, so the omission carries over, as in §5.
- DATA rule. I read gfc203.py (153 lines), lam203.py (39) and skip203.py (21) line by line against each clause.
  - lfail: for every gate and step with σ̄_(t−1)(g) ≠ σ̄_t(g), neither face's (Λ, Π ∩ e-vertices) changes. Unit: flips. = the line.
  - gfail: per gate, flips > Dtot(a) + Dtot(b) − 2, with Dtot the distinct classes over the run. Unit: gates. = the line.
  - qflip: per quiet step (no vertex changes class), σ̄ changes at some Odd vertex. qfail: per run, longest quiet run > N (G["N"]).
    Tfail: per run, T > Q + (Q + 1)·N. All = the line.
  - GFC_CTRL=3 restricts lfail to the e-face. Cap 20,000 states (hist_ideal). Both = the line.
  - lam203 lfail: states where the number of distinct Λ over v ∉ {c_W, c_X, e-vertices with successor c_W} exceeds k + 1. k = fvs202.kfvs,
    and the count is skipped when k is not an int (k > 12). LAM_CTRL=1 uses bound k. = the line.
  - skip203 replays lam203 --rand's stream without the run. Its output reads 0 skipped on all three sets, with k ∈ {0, …, 5} / {1} / {2}.
    The line's «k ≤ 5 on every genome» is right.
  - Outputs, read on the archive:
    - out/gfc203_corpus.out: 57 rows, every must-0 counter 0 (my script). DSALT6_n108 has «maxquiet 10 N 108».
    - out/rnd203_rand_s2.out: 1,000 genomes; out/rnd203_k1_s202.out: 5,000. Both all 0.
    - out2/gfc203_k1extra.out: K1C16_n400 and K1F21_n48 all 0, maxflip 31 (22, 37) and 21 (12, 22).
    - out2/lam203_k1_s7.out 2,000, lam203_k2_s8.out 1,000, lam203_rand_s2.out 1,000: lfail 0. lam203_k1_s7_ctrl.out: lfail 3,492.
    - check203.out: ctrl3 MWR4_2 lfail 9; MWR4_2 maxflip 9 (5, 10).
  - Every DATA number in L-1 equals its output file.
  - The line also cites my predecessor's replay as «REFEREE-2 35 R2-P-N5-QN (claude/referee-2 5d4f06c2; 61 pinned genome runs and 6,000
    random)» and the window «11 on REFEREE-2 35's engine». Both are correct.
- Verdict: L-1 MATCHES the packet as governed by fixes entry 1, and meets R-1, GATE-FLIP (b)'s [E-LEV] and QUIET-N's «sharpens». Nothing
  REQUIRED is open.

## Addendum 2 (REFEREE-2 successor 36; read after Addendum 1 was committed, a327b4dc): REFEREE 30's R-P-N5-QN.md (claude/referee 452800c5, §C at 09aabb03)
- Verdicts: equal. Both referees SIGN GATE-CLASS, GATE-FLIP (a), GATE-FLIP (b) (the U(G) form under HYPOTHESIS [E-LEV]), QUIET-N and
  (k+1)-Λ. DEAD D1-D3 are confirmed on independent engines.
- The defect in (k+1)-Λ: REFEREE's QN-1 is my predecessor's W-1 / R-1, found independently and read the same way (the value is the top
  vertex, a β, of the Γ(G)-cycle through the Ξ_σ-cycle; the count k + 1 is unaffected).
- Differences, none a disagreement:
  - LN-5 (lam203.py skips genomes with k > 12) was found by REFEREE, not by my predecessor's report, which deferred the DATA rule to the
    line. Fixes entry 1 measured the count (0 skipped), and my Addendum 1 confirms it from the code and skip203.out.
  - LN-4: REFEREE leaves «R123's ASC-T and UP-T hold with L + 1 replaced by N + 1» as a READING. My predecessor called the comparison with
    R123 arithmetic on the landed text and correct. L-1 omits the sentence, so nothing signed depends on it.
  - D3's k = 2 WC family is re-run by neither referee. It is cited, and ST(m) kills D3 alone.
  - The DSALT6_n108 window, 10 (lane engine) vs 11 (my predecessor's): REFEREE's reading equals mine (tie rule free in R118 (a); both ≤ N).
- L-1: both referees find MATCHES (REFEREE §C 09aabb03, LN-1..LN-8 PASS; mine Addendum 1). P-N5-QN's line has two signatures, with no item
  open.
