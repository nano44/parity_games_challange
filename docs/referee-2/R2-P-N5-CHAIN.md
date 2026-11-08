# R2-P-N5-CHAIN: second-referee report on packet P-N5-CHAIN (L-NEW successor 64, box 196)
REFEREE-2 successor 35 (Opus 5.5, D1). Written 2026-11-08 by date -u (times in the commit). Independent: docs/referee/R-P-N5-CHAIN.md
(REFEREE 29) NOT read before this report is committed. L-RED 58's R223-reach, R223-q2 and R224-chain are context only. I did not read
them. I used only what the packet quotes from them, and I diffed the one copied L-RED file (ctrl196.py / .out) against its source.
Disclosure: the packet says that REFEREE 29's draft notes CH-1..CH-5 are answered in its text, and the fixes file names CH-4. I read
those sentences only as part of the object.
Second disclosure (Lead 10:54Z sent line L-2): fixes entry 1 at 8b67d40e quotes REFEREE 29's verdicts in outline. It says every
statement is SIGN, no GAP is in any proof, and L-1 is NOT YET on CL-1 only (= my R-3). I read that entry after my findings W-1 and
R-1..R-4 were already committed in my notebook's resume point (claude/referee-2 52d51575, committed before that reading; «R-1 wfail counts steps; R-2 Tfail tests
Q-form not Σ-form; R-3 ties has no control; R-4 k2fail one conjunct»). Nothing below was changed after that reading, except the L-2 row of the table and the L-2
section.

## Object (claude/l-new, FROZEN at 93531b03)
- Packet docs/new/P-N5-CHAIN.md at 93531b0368ef938b7ffcd44eb0743796810ea35d: sha1 6e613ba762b6ecf67247ef6d8674b4c960013039, 38,551 B
  (= the brief), re-hashed on a git archive.
- Line L-1 at 71b754245637d10f230727816b102e25f9b6275d: docs/new/P-N5-CHAIN-line-L1.txt, sha1 bd152dd9c71ea47dbc7fa6655a9a18a87908781a,
  8,124 B (= the brief). 93531b03 is an ancestor of 71b75424. Between the two commits only the fixes file, the line, chain.pins (3 rows
  added), mkl1_196.py and notes/L-NEW.md change. The packet is unchanged.
  - The lane's generator mkl1_196.py, run on a git archive of 71b75424 with trunk a1decf9a0's RESULTS as its argument, exits 0 and
    rebuilds L-1 byte-equal (bd152dd9…, 8,124 B).
- Pins: experiments/new/box196/chain.pins, 51 rows. On a git archive of 71b75424, the sed of the check.sh «P-N5-CHAIN» block gives
  `sha1sum -c --quiet` exit 0. All 51 rows match.
- The copied control file experiments/new/box196/ctrl196.out is byte-equal to L-RED's experiments/red/r224/out/ctrl224.txt at
  e7937985 (sha1 18647b3c…). ctrl196.py differs from ctrl224.py only in a 2-line credit header and the default of W196 (its root path).

## Verdicts (Opus 5.5, D1)
| statement | verdict | note |
| --- | --- | --- |
| Lemma ESC3-ALL | SIGN | every genome |
| Lemma W3-ALL | SIGN | every genome; (ii) holds for every pad m_(x,k), not only those in A(x) |
| Theorem REACH3-ALL | SIGN | removes R118 (k)'s condition; the fallback is at T3 + 1 with T3 in HOW3's own sense (my t3def counter) |
| Facts F1, F3, F4′, F5, F6, DOM, STRICT (and F2, CYC as used) | SIGN | on HOW3(G) |
| Lemma CN2-3 | SIGN | |
| Lemma LOC-GATE3 | SIGN | all seven cases redone |
| Lemma LOC-K2-3 | SIGN | |
| Lemma B-ONLY3 | SIGN | |
| Corollary NO-TIE3 | SIGN | one step made explicit (pe_g lies on pβ_g's prefix) |
| Theorem QUIET3 | SIGN | W-1: one sentence of (F-cls3) is false as written over all vertices; I closed it, and every use holds |
| Corollary T-QUIET3 | SIGN | (W-1 as for QUIET3) |
| Lemma E-MON3 | SIGN | W-1: the stated reason for «both or neither contain K0, K3» is wrong; the claim holds per vertex |
| Lemma CHAIN-DECOMP3 | SIGN | |
| Corollary HUB-ASC-G3 | SIGN as PROVED-CONDITIONAL | on P-N5-ASC §4 (unlanded; R121 when landed); the CS(M) axioms are supplied by E-MON3, CHAIN-DECOMP3, F1, F2 |
| Lemma UP-JUMP3 | SIGN | under HYPOTHESIS [E-LEV] |
| Corollary UP-B3 | SIGN | under HYPOTHESIS [E-LEV] |
| Theorem CHAIN3 | SIGN as PROVED-CONDITIONAL | under HYPOTHESIS [E-LEV]; on P-N5-END (ENDGAME-3) and P-N5-ASC §4, both unlanded |
| DEAD RUN-TRANSFER | SIGN (dead) | RT_n1 re-run on my own code: T3 = 1, T_CYC = 2, options 1 and 2 exactly tied at state 0 |
| Line L-1 | NOT YET | four REQUIRED changes, all in DATA clauses (R-1..R-4); N-1, N-2 optional |
| Line L-2 (e481d260, = L-1 + CL-1) | NOT YET | CL-1 meets R-3; R-1, R-2, R-4 still REQUIRED (old strings once each in L-2) |

No statement is REFUSED. W-1 is a defect in the proof text, and I closed it here (§ W-1). No gap is left open in any signed proof. All
four required changes are to the line's DATA clauses. The lane tool's counters and units are weaker than, or different from, what the
clauses say (the DATA rule).

## Premises (own scripts R2-P-N5-CHAIN/r2q.py, out r2q.out; r2qattr.py, out r2qattr.out)
- Every «…» of the packet (whole text) and of L-1: 36 quotes, looked up by `git show`, whitespace collapsed. The sources are trunk
  3906d411 (docs/RESULTS.md, docs/new/N5-ssi-global.md, P-N5-XICYC.md, P-N5-REACH.md, P-N5-XICYC-fixes.md, docs/DECISIONS.md), P-N5-END
  at 131b4c1c and P-N5-ASC at 93531b03.
  - 29 are found verbatim. The 7 misses are not premises. The Lead's freeze words (a message) and five self-labels (counter, block and
    route names: «nohoward», «pβ at every gate, r at K2», «T3 equals the IDEAL-CYC count …», «BOX 196 CHAIN», «P-N5-CHAIN») account for
    6. The last is «Polynomial only on a restricted class». It is TARGET.md §4 line 31, found by hand at trunk 3906d411 (TARGET.md is
    not in the script's list).
- Attribution to RESULTS entries (r2qattr.out): [R117-SIGN], [K2r] and both R118 (k) quotes are in R118. [TERM] «Lemma A …» is in R15
  (and in R118's premise text). «(Odd's best reply σ̄_k is pointwise optimal in G_{σ_k})» is in R21. The [1E-N3] form «used in two forms:
  …» is in R104 (and R118). [DEF] is in R104. [G3] and «S3's start pair …» are in R117. Every premise attributed to R104, R117, R118, R15
  or R21 is in that landed entry.
- Landed status: R117 and R118 are landed [refereed-only]. No ### R121 entry exists at trunk 3906d411. So P-N5-ASC §4 and P-N5-END are
  unlanded lane packets, and the packet labels both as conditions (CHAIN3 and HUB-ASC-G3 rows).
- [END] (ENDGAME-3's words) is verbatim in P-N5-END at 131b4c1c, the packet I signed in R2-P-N5-END.md. [ASC]'s constants F′_0, F′_B
  match P-N5-ASC §5 (l. 151-153) verbatim.
- SPEC S2 / S4a / S4c (N5-ssi-global.md l. 47-57) read for REACH3-ALL. Ξσ is the valuation under σ̄ (= HOW3's Ω_t). S4c fires iff
  σ_new = σ and τ_new = τ. FIX 3: τ is unchanged in an Even fallback.

## Re-derivation (every step redone by hand)
- ESC3-ALL. (K0, K1) ∈ Iσ is K3 (b). At β_g with xt(g) a mover: A(β_g) ⊆ {xt(g), pb_g}. Every H-play from xt(g) takes pe at every gate
  (τ), so it meets no β and reaches c_W's loop after finitely many level descents. Every H-play from pb_g enters K0 and ends at node K1 or
  K2, both odd (A(K0) = {pA, K1} by K3 (b)). So xt(g) is strictly better and TIE(β_g) = {xt(g)}. β_g is on no H-cycle: its only
  in-edge is from pβ_g, which no gate enters in H. K0: K3 (d). The rest have one successor. Correct.
- W3-ALL. (i) x → m → g → pe → e → (W-target, a mover of level ℓ − 1 | c_W) gives length 5ℓ + 5 by induction, with Π = ∅ (all less
  relevant than c_W). β → xt adds one step. (ii) Every H-play from a pad m_(x,k) (any k: the pad has one successor, so W* is defined
  for all of them) has that shape whatever the lower movers choose. (iii) follows. Correct.
- REACH3-ALL. Induction on standard states with S3-START, TAU3 (Iτ = ∅), ESC3-ALL (σ_new = σ off the movers, for SPEC's optimum and for
  [N5XI]: TIE = {σ(v)} at β_g and K0) and W3-ALL (TIE(x) = A(x) at movers, so [N5XI] takes the Ξσ-best element of A(x)). A(x) holds
  every strictly better successor, so this is a ⊴-best successor, and σ(x) is kept when nothing is strictly better (A(x) = {σ(x)}). Some
  mover changes, so S4c does not fire. At T3, σ_new = σ and τ_new = τ, with Iσ ∋ (K0, K1), so S4c fires at iteration T3 + 1. Correct.
- F1 ([TERM]; the Howard switch set is non-empty and unambiguous, one switch per mover), F3, F4′ (equal Λ: v added to both or neither,
  symmetric difference unchanged, both k + 1; different Λ: decided by Λ), F5, F6 (a cycle through a mover passes a gate then e or β, Ω
  ≥ 6). DOM and STRICT chain F3/F6 at t + 1, F1 and F4′ (x in no Π by CN2-3), then F5. CYC: 2M + 3 nodes (e's, β's, c_W, K1, K2). Correct.
- CN2-3. (P) gives a cycle vertex of priority ≥ 3 on every cycle but c_X's loop. Movers, gates and pads (≤ 2) rank below it, so they
  are never the node and never in Π. Correct.
- LOC-GATE3. I redid Cases 1, 2-i-a, 2-i-b, 2-ii-a, 2-ii-b and 2-ii-c.
  - In 2-i-a, the most relevant element of Rel(P) is the most relevant vertex of C, since g ranks low.
  - In 2-ii-a, it beats every vertex of Q, because Λ is Q's most relevant vertex.
  - In 2-ii-c, Λ lies on Q strictly between g and q, so the path from q to Λ passes g and a, and k(b) > k(a).
  - q ∈ arc puts Λ = q in 2-ii-b. Correct.
- LOC-K2-3. Rewards: node K2 (priority 3) has −3, and node K1 (priority 5) has −5 (in rank units). Odd takes r. With node K1 odd, the
  longer prefix is better for Even: (K1, ∅, 1) ◁ (K1, ∅, 2). Correct.
- B-ONLY3. Under τ_β no gate enters pe, so for the non-excluded v the τ_β-play meets no e-vertex after its start and never reaches c_W.
  Its node is below every e by (E-DOM), with a smaller reward. [OPT] gives Ω_t(v) ⊴ that value, and rewards come first. Λ_t(v) cannot
  be an e-vertex or c_W (rewards above every e), nor K0 or K3 (never nodes). By (E-DOM) it is less relevant than every e. Correct.
- NO-TIE3. One step is implicit, and I make it explicit. e_g ∈ Π(pβ_g) puts e_g on pβ_g's PREFIX. So pe_g (its only in-neighbour) is on
  the prefix too. pe_g is not on the cycle: if it were, e_g would be on the cycle and more relevant than the node. So k(pβ_g) > k(pe_g).
  Correct.
- QUIET3, (Q1)-(Q6). I redid the B-class induction.
  - The boundary values of C = (w, S) are y in (w, S ∖ {e}) (constant after a_(s−1) by induction), the core exit (K1, ∅, ·) (constant),
    or w itself. If some C-play's cycle has node w, then Λ(w) = w on the whole window.
  - At most M flips: the e-face is constant, the β-face only rises, and LOC-GATE3 + NO-TIE3 allow a single β → e flip.
  - Bellman-Ford, using DOM at x and F3 at m, g, the face pad and the face. The face β is in no Π of either compared value: on z's play
    it would close a cycle through β, and the path is simple. It reaches opt(x) within N steps.
  - After c + N no C-value changes, so no flip, so each sub-window starts within N + 1 steps of the previous one.
  - (Q6) STRICT, then (Q3), gives at most N(n3 − 1) further steps. L3 is exactly (M + 1)(2M + 1)(N + 1) + N(n3 − 1). Correct, given W-1's
    repair of (F-cls3).
- T-QUIET3. Q + (Q + 1)L3 = (Q + 1)(L3 + 1) − 1. Q ≤ Σ_v (D^tot_E(v) − 1) needs only the per-vertex interval property (W-1). Correct.
- E-MON3, CHAIN-DECOMP3. Correct (E-MON3 with W-1's per-vertex reason).
- HUB-ASC-G3. P-N5-ASC §2's CS(M) needs three things.
  - Forests next_t on the active items: CHAIN-DECOMP3, with next(f) the first element of seq_t(y_f), an active item.
  - Lex-nondecreasing chains per item over its active interval: E-MON3. The interval comes from F1 + F2.
  - A hub with a lex-nondecreasing value: seq_t(v), by E-MON3 at fixed Λ.
  §5's refinement (M² + 3M + 1 levels) and §4 then apply as the packet says. F′_B(M_w) ≤ F′_B(M) (F′ is nondecreasing in M), and with
  ≤ 2M + 3 nodes (CYC) D^tot_E(v) ≤ (2M + 3)·F′_B(M). Correct, CONDITIONAL on §4.
- UP-JUMP3. ℓ ≥ 1. The play goes from a to the W-target of level ℓ − 1. [E-LEV]'s contrapositive gives lev(x′) ≥ ℓ for b = e_(x′,k′).
  Only Ξ-steps from β can raise the level (e-steps lower it by 1, pads keep it, pb enters the closed core). The first step to level ≥ ℓ
  goes strictly up from the mover the β was entered from: an option counted by U(G). Correct.
- UP-B3. The segments are disjoint pieces of the simple prefix, so each ascent uses its own upward β. Correct.
- CHAIN3. REACH3-ALL (F = T3 + 1) + ENDGAME-3 (F + 2 iterations) + T-QUIET3 + UP-B3 / HUB-ASC-G3. The arithmetic of the displayed bound
  is exact. F′_B is nondecreasing in B (F′_1(0) = F′_0(0) = 1), so U(G) ≤ B gives the polynomial claim. Correct, CONDITIONAL as labelled.
- DEAD RUN-TRANSFER. On my engine (r2rt.out), at state 0 options 1 and 2 have equal values (Λ β_(0,0), Π ∅, k 8), both strictly above
  option 0 (k 3; the node is odd, so the longer prefix is better).
  - N5′-xi on Γ3: T3 = 1 (r2chain.py, pinned.out).
  - My IDEAL-CYC on Γ(G) (R2-P-N5-QUIET/r2quiet.py, Howard, keep then the largest vertex id): T = 2. On Γ3 the same rule gives T = 1.
  So T_CYC is not one number across tie rules, and the route is dead as stated.

## W-1 (proof text; closed here; no change to any statement or to the line)
- (Core) says «a play passes K0 iff it passes K3». This is false for plays starting at pA or K3 (they pass K3, not K0).
- (F-cls3) says «each class is a convex set of values». This is false over ALL vertices.
  - Witness (R2-P-N5-CHAIN/r2nonconv.py, out r2nonconv.out), at one S3 state:
    x_1 (Λ K1, Π {β, K0, K3}, class (K1, ∅)) ◁ e_(3,1) (Λ K1, Π {β, e_(3,1), K0, K3}, class (K1, {e})) ◁ K1 (Λ K1, Π ∅, class (K1, ∅)).
  - The reason: K3 ∈ Π decides before E does, and the core vertices K1, s, r, K2 have node K1 without K0 or K3 in Π.
  - My replay counts such states as «nonconv» on every set (record).
- E-MON3's reason («both plays have node w, so both or neither contain them») is not a valid inference either.
- Repair:
  - Every vertex outside {K0, pA, K3, K1, s, r, K2, q} reaches the core only through some pb → K0, so its plays with node K1 or K2 contain
    both K0 and K3, and its plays with any other node contain neither.
  - The eight core vertices have constant values on every state (the core is frozen and σ̄(K2) = r by LOC-K2-3).
  - So on one vertex's trajectory, and between two non-core vertices, the order is reward, then E, then the rest.
  - Every use in the packet is of that kind: (Q1) compares pe_g with pβ_g, (Q2) compares a mover with its pads, and the per-vertex
    interval property gives Q ≤ Σ(D − 1). E-MON3 compares one vertex at t and t + 1.
  - My counter civ (a class of one vertex occupied in two separate intervals) is 0 on every set.
- Suggested for the fixes file (wording only, optional): restrict (F-cls3)'s convexity sentence and E-MON3's reason to non-core
  vertices, and say that core vertices are constant.

## DATA replay on my own engine (R2-P-N5-CHAIN/r2chain.py on R2-P-N5-END/r2end.py; driver sweep.sh; outputs in R2-P-N5-CHAIN/)
- Engine: REFEREE-2's own r2end.py. That is my predecessor's Γ3 builder with R117's pad index order, SPEC S1, S3 (FIX 1), and N5′-xi's
  S4a (TIE rule, then SPEC's choice, then the larger index). No lane, L-RED, REFEREE or L-SI code is imported. e-priorities are in
  (lev, gate) order, so [E-LEV] holds on every instance (the same scope as the lane's).
- Counters: one per statement, from the packet's text. Notably:
  - k2 tests BOTH conjuncts of LOC-K2-3.
  - TQfail tests T-QUIET3's Σ-form directly.
  - t3def tests T3's HOW3 definition: no mover has a strictly better successor exactly at the last pre-fallback state.
  - civ is the per-vertex class-interval property.
  - bound tests CHAIN3's displayed bound, with F′ saturated at 10^40.
  - dom, strict and f1 test DOM, STRICT and F1. cdec tests CHAIN-DECOMP3.
- Sets:
  - Pinned: every *.json in box189/corpus, box191-box196/inst and box196/inst_si85 at the archive, which is the lane's 58 pinned genomes
    plus L-SI's 11. That gives 69 runs. One file, DEAD_SEGT_n20.json, is not a genome and is skipped, as the lane's tool does.
  - Own random genomes: 3,000 «any» (Ξ-targets anywhere, incl. self and upward; seed 3501), 1,500 «self» (seed 3502) and 1,500
    «acyc» (seed 3503).
  - 6,069 runs in all.
- Results (pinned.out, gen_any.out, gen_self.out, gen_acyc.out): every fail counter is 0 on every set. That covers t3def, nonstd, nohow,
  nonmov, fbidx, tot3, emptytie, cnlow, loc, tie, k2 (both conjuncts), bonly, f1, dom, strict, emon, cdec, upfail, wfail, Tfail,
  TQfail (Σ-form), civ and bound.
  - Pinned maxima: T3 129 (LEAP_k64), longest quiet window 32, max ascents 4, U(G) up to 217. These equal the lane's maxima, from a
    different engine.
  - Random sets: max T3 9, max window 5, max ascents 3.
  - RT_n1: T3 1, 4 iterations, F 2.
  - Record: nonconv (W-1) > 0 on every set (948 states pinned, 3,018 any, 1,356 self, 2,903 acyc). F-cls3's convexity over all
    vertices fails routinely, while civ (per vertex) is 0.
- Controls (every counter fires; ctrl0.out, ctrlX.out on 200 «any» seed 3504; ctrl0_pinned.out, ctrlX_pinned.out on the 69 pinned):
  - ctrl0 (L3 := 0, U(G) := −1): upfail 69,503, wfail 55, Tfail 47, TQfail 1 (pinned: 1,482,910 / 385 / 59 / 14).
  - ctrlX (each condition inverted or tightened; see r2chain.py's doc) fires every other counter on both sets. On the random set:
    t3def 200, nonstd 584, nohow 2,882, nonmov 39,666, fbidx 200, tot3 200, cnlow 30,717, loc 3,562, tie 4,946, k2 584, bonly 5,472,
    f1 22,053, dom 4,835, strict 963, emon 2,015, cdec 19,767, upfail 69,503, TQfail 175, civ 10,116, bound 175.

## DATA rule on L-1, clause by clause (lane tool qt3_196.py and check196.sh at the archive of 93531b03, read line by line)
- Unit, set and scope: the runs, the 8 families × 500 × 2 seeds and the 58 pinned genomes are as stated. I re-summed data/sweep196.out:
  74 xi lines with ctrl 0, 8,058 runs.
  - Every fail counter is 0. Max T3 129, max W 32, max ascents 4.
  - tdiff 101 = 100 random + RT_n1, and seqdiff 1,014 = 1,013 + RT_n1. These match «tdiff … 100 of the 8,000 runs» (and the packet's
    seqdiff 1,013).
  - The spec lines read nohoward 599 (rand, 200) and 911 (dense, 200), as stated. ctrl1 / ctrl2 / ctrl3 in check196.out read wfail 32,
    Tfail 22, upfail 26,477, locfail 3,320, bonly 2,269, as stated.
- nonstd: σ off the movers = S3's start and τ = τ0. With S3-START, «standard» means exactly this. OK.
- nohoward: the next σ(x) is not a key-maximal successor, or it leaves a maximal σ(x). OK. (No lane counter tests that the loop stops
  where T3's definition says: N-2.)
- cnlow, locfail, bonly, upfail, emon, crossflip: each condition matches its clause and unit. OK.
- **ties (NO-TIE3) has NO firing control.** check196.sh's ctrl1/2/3 cover wfail, Tfail, upfail, locfail and bonly. Spec mode covers
  nohoward. L-RED's ctrl196 covers «the five box-196 counters that have none (nonstd, cnlow, k2fail, crossflip, emon)» (its own header).
  ties is in none of these. So the clause «controls fire (every fail counter has one)» is false: R-3. (My own tie counter has a firing
  control, ctrlX.)
- **k2fail (LOC-K2-3) counts states with σ̄(K2) ≠ r only.** The lemma's second conjunct, Ω_t(r) ◁ Ω_t(K2), is not counted. This is the
  P-N5-QUIET D-2 pattern again: R-4. (My k2 counts both conjuncts: 0.)
- **wfail (QUIET3) counts STEPS, not windows.** `cur += 1 … if cur > L3: c["wfail"] += 1` adds 1 for every quiet step past the L3-th of
  its window. In ctrl1 (L3 := 0) the reported «wfail 32» is 32 quiet steps over 50 runs, whose longest window is 3. So the clause's unit
  «(unit: quiet windows)» is wrong for the control count it is read with: R-1. (The 0 is unit-independent.)
- **Tfail (T-QUIET3) tests T3 > Q + (Q + 1)·L3, Q the loud steps.** The line states T-QUIET3 only in the Σ-form T3 ≤ (1 + Σ_v (D^tot_E(v)
  − 1))·(L3 + 1). That form also needs Q ≤ Σ_v (D^tot_E(v) − 1), which no lane counter tests (sumDE and Q are recorded only as maxima).
  So the clause names a weaker counter than its statement: R-2. (My TQfail tests the Σ-form directly: 0.)
- «check196.sh … spec on 100 runs and 5 pinned genomes»: the 5 pinned genomes run in xi mode (check196.sh l. 8), not spec. The wording
  can be read either way: N-1.
- Independent L-RED results are cited, not re-run, as the line says. The copy ctrl196.out = ctrl224.txt, as shown above.

## Line L-1: NOT YET (four REQUIRED changes; exact strings; each old string occurs exactly once in L-1, checked by script)
- R-1 (REQUIRED). old «QUIET3: wfail 0 (unit: quiet windows)» → new «QUIET3: wfail 0 (unit: quiet steps past the L3-th step of their
  window)».
- R-2 (REQUIRED). old «T-QUIET3: Tfail 0 (unit: runs)» → new «T-QUIET3: Tfail 0 (unit: runs with T3 > Q + (Q + 1)·L3, Q the number of
  loud steps; the Σ_v form is not counted)».
- R-3 (REQUIRED). old «controls fire (every fail counter has one):» → new «controls fire (every fail counter except ties has one):».
- R-4 (REQUIRED). old «LOC-K2-3: k2fail 0 (unit: states)» → new «LOC-K2-3: k2fail 0 (unit: states with σ̄_t(K2) ≠ r; the conjunct
  Ω_t(r) ◁ Ω_t(K2) is not counted)».
- A tool fix in place of R-2, R-3 or R-4 is equally acceptable: a ties control, a k2fail on both conjuncts, a Σ-form counter. In that case
  the clause stays and the tool and its output are re-pinned. R-1 can also be met by counting windows.
- N-1 (optional). old «spec on 100 runs and 5 pinned genomes, check196.out)» → new «spec on 100 runs, and 5 pinned genomes in xi mode,
  check196.out)».
- N-2 (optional). Add a counter of T3's definition: no mover has a strictly better successor exactly at the last pre-fallback state. My
  t3def is 0 on every set.
- Everything else in L-1 matches the packet:
  - statements and labels (PROVED / CONDITIONAL / HYPOTHESIS / DEAD), premises, scope, limits;
  - the TARGET.md §2 / §4 clause;
  - the restatement of LOC-GATE3, CN2-3 («priority ≥ 3») and W3-ALL («every option»).

## Line L-2 (claude/l-new 8b67d40e; byte test R2-P-N5-CHAIN/bt_l2.py, out bt_l2.out)
- docs/new/P-N5-CHAIN-line-L2.txt: sha1 e481d260884807424c545bd3f3cdd7fbfb25f05c, 8,248 B, one line, 160 «(» = 160 «)», no «|».
  71b75424 is an ancestor of 8b67d40e.
- Diff against L-1: ONE changed region, the control clause, and everything outside it is byte-equal. Old «has one): … in 50 runs; …
  bonly 2,269; spec mode». New «except ties, NO-TIE3's counter, which has none): … upfail 26,477; … bonly 2,269 (each control on 50
  runs, family rand, seed 1963, check196.out); spec mode, seed 1963 (data/sweep196.out),». This is CL-1 as fixes entry 1 and
  mkl2_196.py state it.
- The lane's mkl2_196.py, on a git archive of 8b67d40e, rebuilds L-2 byte-equal. box196/chain.pins: 53/53 match there.
- Meaning: CL-1 meets my R-3. Its form is different and better (it names the control and spec sets). The sets it names are right: the
  three ctrl rows in check196.out are on rand, seed 1963, 50 runs, and the two spec rows in sweep196.out are on seed 1963.
- Still open against L-2, each old string exactly once in L-2 (bt_l2.out): R-1 (wfail unit), R-2 (Tfail's Q-form), R-4 (k2fail's one
  conjunct), with the exact strings of «Line L-1» above. N-1 and N-2 stay optional. L-3 := L-2 + R-1 + R-2 + R-4 (or the equivalent
  tool fixes) would MATCH from my side.

## TARGET.md diff
- TARGET.md §2 (M4) asks for one algorithm, polynomial on every parity game, at bit cost (§3). §4 l. 31: «Polynomial only on a
  restricted class (bounded d, treewidth, Strahler/register number, ...)» is not M4.
- CHAIN3 bounds the ITERATIONS of N5′-xi on {Γ3(G) : U(G) ≤ B} under [E-LEV]. It is conditional on two unlanded packets. Per-iteration
  cost at bit cost is not addressed.
- So it is not M4 and not a step-4 pass. G-N5-TIME stays OPEN and N5′-xi stays a CANDIDATE (D1). The packet (§11) and the line say
  exactly this. No statement of the packet is stated as a TARGET.md claim.

## Machine checks (all on git archives; outputs in R2-P-N5-CHAIN/)
- sha1 / sizes: as in Object.
- chain.pins: 51/51.
- mkl1_196.py rebuilds L-1 byte-equal.
- ctrl196.out = ctrl224.txt.
- r2q.out, r2qattr.out: premises.
- My sweep: totals above.
- Not re-run: the lane's check196.sh. It imports lane code, and its record sweep196.out was re-summed instead. L-RED's R223 / R224 runs:
  context.

## Statement of independence
My verdicts rest on my own derivations above and on my own engine. I did not read docs/referee/R-P-N5-CHAIN.md or L-RED 58's reports.
