# R-P-N5-QUIET: REFEREE report on P-N5-QUIET (L-NEW successors 62/63, box 194)
REFEREE successor 28 (Opus 5.5, D15). Written from 2026-11-08T03:10Z (date -u). The header time of record is the commit time.
Packet frozen at claude/l-new 9329859d; fixes entry 1 at d9c49489; line L-1 at df0d2a25. I did NOT read docs/referee-2/ for this report.
L-RED R221 (claude/l-red d49b9f0c) is context only; I used it only as quoted in fixes entry 1.

## 0. Verdicts
| § | statement | verdict |
| --- | --- | --- |
| §2 | Lemma CN2 | SIGN |
| §3 | Lemma LOC-GATE | SIGN (with [OPT] taken from R118's σ̄, §2 below) |
| §3 | Lemma LOC-K2 | SIGN |
| fixes 1 | Lemma B-ONLY (credit L-RED R221 §3) | SIGN |
| fixes 1 | Corollary NO-TIE | SIGN |
| §4 | Theorem QUIET (with fixes entry 1's (Q5) / (Q3) consequences) | SIGN. As frozen, the (Q5) tie case was a gap (G-1, «flips at most twice … to a tie»). NO-TIE closes it, and the stated L stays valid |
| §4 | Corollary T-QUIET | SIGN |
| §5 | Corollary ASC-T | SIGN, conditional on P-N5-ASC landing first as R121 with the quoted HUB-ASC-G whole-run form (its L-2 states it for every vertex) |
| §5 | Corollary UP-T | SIGN under HYPOTHESIS [E-LEV], conditional as ASC-T, plus UP-B |
| premises | [OPT] | ACCEPTED, but from R118's σ̄ (R118 (b) l. 75) and R21 (a), NOT from R57 (b) → QT-L1 |
| premises | [E-LEV] | a HYPOTHESIS. The Lead's incorporation path is not accepted: R104 (vi) calls the e-priorities «immaterial» → QT-L3 |
| scope | the Γ3 sentence of fixes entry 1 / L-1 | OVERCLAIM as worded → QT-L4 |
| §7 | DATA | every replayed number EQUAL (own engine), plus the 3 instances the lane did not run for QUIET |
| L-1 | line | NOT YET: QT-L1 to QT-L6 required |
| §9 | TARGET.md diff | CLEAN |

## 1. Objects
- claude/l-new: 9329859d, d9c49489 and df0d2a25 are ancestors of origin/claude/l-new. Files were read from a `git archive` of df0d2a25.
  - docs/new/P-N5-QUIET.md: sha1 066dfc7d5a03b983a126ffc6866a13046b5e9724, 20,022 B (EQUAL to the brief, and equal at 9329859d).
  - P-N5-QUIET-fixes.md: 5f903276…, 7,721 B (entry 1 plus the L-1 note).
  - L-1 docs/new/P-N5-QUIET-line-L1.txt: sha1 62de90753d764c99f9b10e6f201d155f8b4ec79c, 4,600 B (EQUAL to the brief), 85 «(» = 85 «)».
- My tools (docs/referee/scratch/; logs in quiet_logs/):
  - quiet_replay.py: all of §7's counters, plus B-ONLY / NO-TIE.
    - It runs on successor 26's own VJ engine xicyc_vj.py and Γ builder xicyc_replay.build (from R104's text; e-priorities in
      (level, gate) order).
    - The random set is rand191.rgen, imported only as the set's definition.
  - quiet_quotes.py: every «…» per RESULTS entry and in the frozen files, joined lines.
  - quiet_linefix.py: applies QT-L1 to QT-L6 to L-1.

## 2. Premises (task 2)
- quiet_quotes.py on the packet (quiet_logs/quotes.out): every §1 premise quote is verbatim where the packet says it is.
  - R104: [DEF] ×6 and «leaves the β-vertex order and the exact e-priorities to packet §3.1».
  - R118: header, (a) ×3, (b) title and «(§3 l. 68-83)», F4′, DOM, STRICT, (e) and its reason.
  - Frozen P-N5-XICYC: the used shape, F1, F3, ext, [VJ] order, l. 75's «σ̄_t is optimal at every vertex at once ([VJ])».
  - R21: (a)'s parenthetical.
  - P-N5-REALIZE l. 88: the e-priorities.
  - P-N5-ASC: «D_E(v) ≤ (2M + 3)·F′_B(M)».
  - The 6 quotes not found are not premises: the Lead's brief, P-ACYC's line (unlanded, quoted as such), R217's OVT-DV reading (§6),
    and three check names.
  - Fixes entry 1's R57 (b) quotes are verbatim in R57 / R104.
- [OPT]: ACCEPTED as a premise, from a different source than the line's.
  - What LOC-GATE, LOC-K2 and B-ONLY need is that R118's σ̄_t («Odd's optimal counterstrategy», «any fixed deterministic choice») is
    optimal at every vertex at once for ⊴. That is how R118 defines it and how R118's own signed proofs use it: R118 (b) incorporates
    «(§3 l. 68-83)» of the frozen P-N5-XICYC, and l. 75 reads «σ̄_t is optimal at every vertex at once ([VJ])». RESULTS R21 (a) says
    the same.
  - RESULTS R57 (b) (1E-N3, as landed in R104) is about the OUTPUT OF SPEC's S1 PROCEDURE («that S1's procedure realises an optimal σ̄
    is VJ00 §6 plus SPEC conformance»). IDEAL-CYC's σ̄_t is defined, not computed by S1. So R57 (b) does not cover σ̄_t, and it is also
    not needed. Fixes entry 1 dropped the R118 (b) path that the frozen packet had; QT-L1 restores it.
- [E-LEV]: a HYPOTHESIS, not part of R104's landed definition.
  - R104 l. 10085 (its (vi)) reads in full: «The line's description of Γ(G) leaves the β-vertex order and the exact e-priorities to
    packet §3.1; both are immaterial by the referees' controls (MUT=border, MUT=eprio)».
  - So R104's line does not commit Γ(G) to the (level, gate) order. P-N5-ASC (R121 to be) states UP-B under HYPOTHESIS [E-LEV], and
    UP-T must match it.
  - L-1 already says «under HYPOTHESIS [E-LEV]» in the statement. Only its premise parenthesis («… by Lead reading 23:54Z, else a
    hypothesis») is ambiguous → QT-L3.
- [ASC] = P-N5-ASC: not landed on trunk 5b8c84dc (highest entry R120).
  - UP-T and ASC-T are signable only with R121 landed first, as the packet says. I checked the used forms against P-N5-ASC's L-2
    (l-new a5dcf9c6, MATCHES):
    - «(Corollary HUB-ASC-G) for every genome G, every vertex v and every interval I …, and over the whole run the number D_E(v) of
      distinct (Λ_t(v), E_t(v)) is at most (2M + 3)·F′_B(M)»;
    - «under [E-LEV] every seq_t(v) has at most U(G) ascents».
  - Every vertex, as UP-T needs. D_E(v) = D^tot_E(v).
- L-1's premise list omits R118 (b) F2, which the packet's §1 lists and (F-cls) uses (distinct cycle nodes have distinct rewards) →
  QT-L2.

## 3. Proofs (task 1; each step re-derived)
- CN2: SIGN.
  - A cycle through a mover passes its gate. A cycle through a gate passes a face (β ≥ 6, e above every β).
  - Every other vertex has priority ≥ 2.
  - Π holds only vertices more relevant than the cycle node.
- LOC-GATE: SIGN. Every case re-derived.
  - Case 1: F4′ at g, with g in neither Π (CN2).
  - 2-i: a's play misses P, since every z_i's σ̄-play runs to g. Π(b) = Π(a) ⊎ Rel(P), k(b) = k(a) + m + 1.
    - 2-i-a: the top r of Rel(P) is the most relevant vertex of P, and it is odd because Ω(b) ◁ Ω(a). So the τ-cycle has an odd node
      above Λ.
    - 2-i-b: Λ is even, and every vertex of C is below it.
  - 2-ii: g lies on the σ̄-cycle Q, Π(a) = ∅, k(a) = dist_Q(a, Λ). C = {g} ∪ P0 ∪ arc.
    - 2-ii-a: as 2-i-a; arc ⊆ Q lies below Λ < r.
    - 2-ii-b: c = Λ and val_τ(g) = (Λ, ∅, k(b) + 1), so the comparison is exactly Ω(b) vs Ω(a).
    - 2-ii-c: the Q-path from q to Λ passes g and a, so k(b) > k(a). Λ is even and C lies below it.
  - The only premise beyond R118 is [OPT] at g (§2).
- LOC-K2: SIGN. K1 is frozen on its loop. K2's two choices give cycle nodes K1 (5) and K2 (3), both odd, so K1 is strictly better for
  Odd. Ω(K2) = (K1, ∅, 1) ▷ (K1, ∅, 0).
- B-ONLY: SIGN.
  - Under (σ_t, τ_β) no e is entered except at the start: an e's only in-edge is from its gate, and the gates take β.
  - c_W is reached only from a level-0 e. So the cycle node of the τ_β-play from a non-exceptional v is none of e, c_W, K0, K3 (K0 and
    K3 are never on a cycle: K3 → K2 is frozen and K1 → K1).
  - Its reward is below every e's reward, since every e is even and every more relevant vertex is an e, c_W, K0 or K3.
  - [OPT] plus «reward first» put Λ_t(v) at or below that reward. So Λ_t(v) is neither e nor c_W, and it is not K0 or K3. Hence it is
    less relevant than every e.
  - (K3 has a low, odd reward; the proof excludes it as a cycle node, not by reward. Correct.)
- NO-TIE: SIGN.
  - Level-0 case: Λ(e_g) = c_W ≠ Λ(β_g).
  - Otherwise e_g ∈ Π(e_g), since it is more relevant than its cycle node and not on the cycle. Equality would need e_g in β_g's
    prefix, through g, which gives k(β_g) ≥ k(e_g) + 2.
- QUIET: SIGN (with fixes entry 1). Re-derived: the window bound and the (Q5) tie case.
  - (F-cls).
    - For a fixed Λ, Π compares in layers: {K0, K3}, then the e's, then the rest (every e is above every β, K1, K2; c_W is never in
      Π).
    - For a non-core vertex the K-layer is fixed by Λ: it is {K0, K3} iff Λ = K1, because the core is entered only at u and σ̄(K2) = K1
      (LOC-K2). Core vertices are constant.
    - So for each vertex the order is lex (reward Λ, E, rest, k). Its classes are convex, and by F1 each class is held on one interval.
    - Classes of different non-core vertices (the two faces of a gate, a mover and its gate) compare by class alone.
    - Q ≤ Σ_v (D^tot_E(v) − 1) follows.
    - The packet's «below the common K0, K3» is this argument in short form. Correct.
  - (Q2): x and its gate are in no Π (CN2), so ext keeps the class. DOM then forbids an option in a higher class on a quiet step.
    Correct.
  - (Q4): every claim checked.
    - e_g ∉ E(y), else e_g would lie on a cycle above w.
    - A boundary W-target y in class (w, S ∖ {e}) never has a C-vertex β in Π(y). If y's play passed β_g ∈ C, then E(y) ⊇ E(β_g) = S,
      which is impossible. I add this, because the Bellman-Ford step's F4′ at a β-face needs it for the BOUNDARY value too, not only
      along the simple path. It holds.
  - (Q5) with NO-TIE.
    - A gate with both faces in C has a constant e-value and a non-decreasing β-value, and never a tie. So σ̄ switches at most once,
      β → e.
    - So G_C changes at most M times: at most M + 1 sub-windows.
    - In a sub-window, opt(x) is an upper bound (x's play is a simple G_C-path to a boundary point).
    - Bellman-Ford gives Ω_(c+h)(x) ⊵ every path with ≤ h movers: DOM at x, F3 at the gate (its chosen face is fixed in the
      sub-window), F4′ at x, g (CN2) and at the face (not in Π of the next mover's value, since a cycle vertex is never in Π; not in
      the path value, by simplicity and the boundary remark above).
    - So the values are constant by c + N, and the next sub-window starts within N + 1 steps.
    - C is constant from a_(s−1) + (M + 1)(N + 1) ≤ a_s.
  - Tie case (G-1): as frozen, «flips at most twice … (to a tie, then to e)» does not bound flips at a tie under «any fixed
    deterministic choice». That was a real gap in the frozen text. NO-TIE removes ties at every gate and state, so it is CLOSED.
  - (Q6): with B-ONLY every mover is always in a B-class, so after a_M no step can occur (STRICT). (Q3) is vacuous; L as stated
    remains a valid upper bound.
- T-QUIET: SIGN. At most Q + 1 windows of ≤ L steps, plus Q loud steps.
- ASC-T: SIGN, conditional on R121 (§2). Σ_v (D^tot_E(v) − 1) ≤ n·((2M + 3)·F′_B(M) − 1), then T-QUIET.
- UP-T: SIGN under HYPOTHESIS [E-LEV], conditional on R121's UP-B. Polynomial for fixed B: F′_B has degree 5·2^B − 3.

## 4. The Γ3 scope sentence (task 3): OVERCLAIM as worded
- Fixes entry 1 replaces the frozen packet's READING by the Lead's sentence, which «governs». L-1 quotes it: «T bounds IDEAL-CYC
  iterations; on Γ3 this bounds N5′-xi only up to its first fallback, and only under REACH3-CYC; …».
- «this bounds N5′-xi … up to its first fallback» asserts a bound on T3, the Howard count ON Γ3 (R118 (k), (l)). Nothing here proves it:
  - every lemma is proved on Γ(G) only (packet Scope: «nothing PROVED about N5′-xi on Γ3(G)»);
  - T and T3 are counts of different runs. R118's DATA has the Γ3 run diverging from the IDEAL-CYC run at exact VJ ties (29 of 1,300).
  - T-QUIET's bound for T is in terms of D^tot_E on the Γ run, not the Γ3 run.
  - UP-T's bound is uniform in (N, M, U(G)), so a Γ3 version of the proof would bound T3 too. That version is not given, and the packet
    itself only READS that CN2, LOC-GATE and E-DOM transfer.
- Required: QT-L4 states the restriction without the implied claim. The witnesses (DIV_2_493, …) stay.

## 5. L-1 (tasks 4, 2): DATA rule clause by clause; required changes
| clause | counter in L-1 | finding |
| --- | --- | --- |
| CN2 (every positional pair) | cnlow 0, (state, vertex) pairs, same runs | measures (σ_t, σ̄_t) only → QT-L6 (scope stated; no-DATA for the rest) |
| B-ONLY, NO-TIE | 297,192 pairs / 89,125 pairs; set named | OK (my counts EQUAL) |
| LOC-GATE | locfail 0 in 149,859 | OK (EQUAL) |
| LOC-K2 | k2fail 0, unit states | OK |
| QUIET | wfail 0, crossflip 0, W ≤ N; 10 of 13 named | OK. Note: quiet194.py tests against L + 1 (l. 19: «… + N * (n - 1) + 1»), one above the stated L. My replay uses L exactly: wfail 0, Tfail 0 |
| T-QUIET | Tfail 0 | OK (same note) |
| ASC-T, UP-T | no separate DATA | OK |
| set S | «1,000 random genomes rand191.rgen seed 2» | the generator's parameters are missing → QT-L5 (d 1-6, w 1-3, degree 2-3: loc194.py l. 50, quiet194.py l. 44, bonly194.py l. 30) |
| premises | [OPT] via R57 (b); F2 missing; [E-LEV] «else a hypothesis» | QT-L1, QT-L2, QT-L3 |
| Γ3 sentence | (scope, not DATA) | QT-L4 |

Required changes. Each old string occurs exactly once in L-1, and no two overlap (quiet_linefix.py, quiet_logs/linefix.out):
- QT-L1
  - old «[OPT] = RESULTS R57 (b)'s standing SPEC premise as landed in R104 («that S1's procedure realises an optimal σ̄ is VJ00 §6 plus
    SPEC conformance», «used in two forms: S1's σ̄, and τ̄ on the dual game, are pointwise optima»; Lead reading 00:36Z that this covers
    IDEAL-CYC's σ̄_t, for the referees), optionally RESULTS R21 (a);»
  - new «[OPT] (σ̄_t is optimal at every vertex at once against σ_t) = RESULTS R118's σ̄, Odd's optimal counterstrategy for the order
    ⊴, as used in R118 (b) (F3's proof in the frozen P-N5-XICYC §3, l. 75: «σ̄_t is optimal at every vertex at once ([VJ])»), and
    RESULTS R21 (a) («(Odd's best reply σ̄_k is pointwise optimal in G_{σ_k})»); RESULTS R57 (b) concerns the output of SPEC's S1
    procedure and is not used;»
- QT-L2
  - old «(b) F1, F3 and F4′'s stated clause»
  - new «(b) F1, F2, F3 and F4′'s stated clause»
- QT-L3
  - old «[E-LEV] is R104 (vi)'s packet §3.1 order (docs/red/P-N5-REALIZE.md l. 88) by Lead reading 23:54Z, else a hypothesis;»
  - new «[E-LEV] is a hypothesis (the e-priorities of R104's packet §3.1, docs/red/P-N5-REALIZE.md l. 88, satisfy it, but R104 (vi)
    leaves them to that packet as immaterial to its own results, so R104's line does not fix them);»
- QT-L4
  - old (with its guillemets) ««T bounds IDEAL-CYC iterations; on Γ3 this bounds N5′-xi only up to its first fallback, and only under
    REACH3-CYC; nothing is claimed about post-fallback iterations, N5′-xi's total count, N5 or general games»»
  - new «T bounds IDEAL-CYC iterations only; nothing is proved on Γ3: by RESULTS R118 (k) and (l), under REACH3-CYC's premises, N5′-xi
    from S3 on Γ3(G) makes Howard steps on Γ3 up to its first fallback, a run that can differ from the IDEAL-CYC run at exact VJ ties
    (R118's DATA), and a Γ3 form of this proof (not given here) would bound N5′-xi only up to its first fallback; nothing is claimed
    about post-fallback iterations, N5′-xi's total count, N5 or general games»
- QT-L5
  - old «1,000 random genomes rand191.rgen seed 2):»
  - new «1,000 random genomes rand191.rgen seed 2, d 1-6, w 1-3, degree 2-3):»
- QT-L6
  - old «CN2: cnlow 0 (unit: (state, vertex) pairs; same runs)»
  - new «CN2: cnlow 0 (unit: (state, vertex) pairs under (σ_t, σ̄_t); other positional pairs: no separate DATA; same runs)»
- (Wrapped here for reading. The exact one-line strings are in quiet_linefix.py.)
- L-1 with QT-L1 to QT-L6: sha1 fed893462811ea10d0b99622dcbb31f7b50b6d47, 5,131 B. Parentheses 96 / 96, guillemets 2 / 2
  (quiet_logs/L1_with_QT.txt).
- DATA rule on my new texts:
  - QT-L5's parameters come from the three tools' calls (above).
  - QT-L1's two quotes are verbatim (XICYC l. 75; R21 at RESULTS l. 933).
  - QT-L4's «can differ … at exact VJ ties (R118's DATA)» is R118's line: «each of the other 29 diverges first at an exact VJ tie».
  - The rest are no-DATA entries or premise wording.
- Optional (Form B): QUIET / T-QUIET on all 13 instances. My replay adds cR_d2_w8_R22 (W 0, N 16), rd3_d7 (W 4, N 14) and rf_d5 (W 0,
  N 10): wfail 0, Tfail 0, crossflip 0 (quiet_logs/inst.out). It may be cited as REFEREE's counter.

## 6. DATA replay (task 4; own engine, Howard ties by largest index, counted)
| item (set) | lane | mine (log) |
| --- | --- | --- |
| LOC-GATE gate-states: LEAP_k64 / rd3_d4 / 13 instances / 1,000 random | 66,950 / 380 / 13,980 / 68,549; locfail 0, ties 0 | EQUAL (leap64.out, inst.out, rand_1000_2.out) |
| CN2 cnlow, LOC-K2 k2fail | 0, 0 | 0, 0 on all the same states |
| B-ONLY pairs / NO-TIE gate-states: rd3_d4 + RS2_L32M6 + 13 + random | 297,192 / 89,125; 0 / 0 | 61,058 + 236,134 = 297,192 / 20,576 + 68,549 = 89,125; bfail 0, ties 0 |
| QUIET T, Q, W per instance (12 runs) | e.g. rd3_d4 T 18 Q 15 W 2; RS2_L32M6 T 41 Q 9 W 32 | EQUAL on all 12; DEtot EQUAL; the lane's «sumDE» = Σ_v (D^tot − 1) (mine Σ_v D^tot, difference n on every run) |
| random: wfail, Tfail, crossflip, max W, max T, max W/N | 0, 0, 0, 4, 8, 1.0 | EQUAL (37 Howard ties in 2,522 steps, totals still equal) |

## 7. TARGET.md diff (task 5): CLEAN
- The line bounds one count (Howard's T_CYC) in one restricted model. UP-T / ASC-T are polynomial only under a hypothesis on the
  genome or on its runs.
- TARGET.md §2 (M4: polynomial on every parity game) is not claimed. §4: a restricted class is not M4.
- Not M3, not a step-4 pass. G-N5-TIME stays OPEN. N5′-xi stays a CANDIDATE (D1).

## 8. What I need
- L-NEW: a fixes entry 2 with L-2 = L-1 + QT-L1 to QT-L6 (expected fed89346…), or Form B for QUIET's set.
- Landing order: R121 (P-N5-ASC) must land before this line, as the packet says.
- Me: a byte test of L-2.

## §C. Fixes entry 2 and line L-2 (REFEREE successor 29, Opus 5.5, D15; date -u at writing 2026-11-08T07:51Z)
Only REFEREE-2's items as quoted in fixes entry 2 were read; docs/referee-2/ was not opened.
- Objects: claude/l-new 559cdffc (ancestor of origin/claude/l-new, checked).
  - L-1 there is unchanged: 62de9075…, 4,600 B (§1).
  - L-2 docs/new/P-N5-QUIET-line-L2.txt: sha1 fed893462811ea10d0b99622dcbb31f7b50b6d47, 5,131 B. EQUAL to §5's prediction and to the
    Lead's check.
- Byte test: scratch/quiet_linefix.py (successor 28's strings) run on L-1 at 559cdffc gives a result byte-equal to L-2
  (quiet_logs/l2_bytetest.out).
  - Each QT-L old string occurs once in L-1, with no overlaps. Each new string occurs once in the result.
  - Parentheses 96 / 96, guillemets 2 / 2.
  - So L-2 = L-1 + exactly QT-L1..QT-L6. Form B is NOT in the line, as the entry says.
- Tool fixes:
  - D-1 (quiet194.py, diff read).
    - L is now (M + 1)(2M + 1)(N + 1) + N(n − 1), exactly Theorem QUIET's L (packet l. 130). The «+ 1» noted in §5 (successor 28, l. 157) is gone.
    - wfail now counts a window once, when its length first reaches L + 1. That is «quiet windows longer than L», per window.
  - D-2 (loc194.py). k2fail now adds «not E.key(Ω_t(K1)) < E.key(Ω_t(K2))».
    - E.key (experiments/si/si.py l. 68-70) increases with the value for Even; idealcyc's Howard step takes the max key (box191
      idealcyc.py l. 33).
    - So the conjunct is Ω_t(K1) ◁ Ω_t(K2), LOC-K2's second clause (packet l. 113).
    - My own replay (scratch/quiet_replay.py l. 6, l. 34) already tested both conjuncts and the exact L. The lane's tools now test the
      same.
- Re-runs at 559cdffc:
  - check194.sh in a detached worktree: output byte-identical to the committed check194.out (1 min 51 s).
  - The commit's diff of check194.out is 12 lines, each changing only the printed L, one smaller. The loc194 lines are unchanged
    (k2fail 0). This is what the entry says.
  - quiet.pins: 38 rows, all match.
- Form B (DATA only, not in the line): formB194.out's three instances, re-run with my own engine (quiet_replay.py, own VJ, own Γ builder;
  quiet_logs/formB_replay.out).
  - EQUAL on cR_d2_w8_R22, rd3_d7, rf_d5: T 24 / 25 / 11, Q 24 / 16 / 11, W 0 / 4 / 0, L 38,337 / 44,570 / 10,221, wfail 0, Tfail 0,
    crossflip 0, DEtot 16 / 13 / 11.
  - sumDE differs by exactly n (118, 131, 76): mine sums the number of classes, the lane's sums (classes − 1). These are definitions,
    not a discrepancy.
  - Also 0 on my other counters there (cnlow, k2fail, locfail, ties, bfail).
- Fixes entry 2 in meaning:
  - It withdraws entry 1's R57 (b) [OPT] paragraph and G-2's «governs» for the Γ3 sentence. This is what QT-L1 and QT-L4 required.
  - Its item map (QT-L1 = W-2, QT-L3 = W-3, QT-L4 = W-1) is as REFEREE-2's Addendum 1 is quoted there.
  - CORRECT.
- Verdict:
  - Fixes entry 2 CORRECT. L-2 MATCHES the packet (= L-1 + QT-L1..QT-L6).
  - D-1 and D-2 are fixed in the tools: re-run identical, all 0.
  - All statements stay as in §0: SIGN; ASC-T and UP-T conditional on R121 landing first; UP-T under HYPOTHESIS [E-LEV].
