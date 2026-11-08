# R-P-N5-ASC: REFEREE report on P-N5-ASC (L-NEW successor 61, box 193)
REFEREE successor 27 (Opus 5.5, D15). Written from 2026-11-07T22:25Z (date -u); the header time of record is the commit time.
Packet frozen at claude/l-new 95dc76d7. I did NOT read docs/referee-2/ for this report.

## 0. Verdicts
| § | statement | verdict |
| --- | --- | --- |
| §1 | premises [DEF] R104, [XICYC] R118 (a), (b) F1-F3, (e) | all LANDED; every quote verbatim (script); F1-F3 are quoted from the frozen P-N5-XICYC packet, which R118 (b) incorporates by line range: correct as the packet says |
| §3 | Lemma E-MON (with its E-DOM derivation from R104's priorities) | SIGN |
| §3 | Lemma CHAIN-DECOMP | SIGN |
| §4 | Lemma SKELETON | SIGN |
| §4 | Theorem HUB-ASC(B) (B = 0: DESC-POLY), degree 5·2^B − 3 | SIGN |
| §5 | Corollary HUB-ASC-G and the whole-run corollary | SIGN (optional AS-1: the B = 0 case of F′ is DESC-POLY on the whole interval, not «word for word» per level) |
| §6 | Lemma UP-JUMP, Corollary UP-B, Corollary NOUP, each under [E-LEV] | SIGN; AS-2 (required, text): §1 and the «To sign» table name [E-LEV] for UP-JUMP and UP-B only, but NOUP needs it too (its own heading and §9 say so) |
| scope | «It bounds the e-set height D_E,I(v) … and NOT R and NOT any running time …» | CORRECT; no other text contradicts it (one wording item AS-3 for a future line) |
| §7 | DATA | every replayed number EQUAL (own code); DATA-rule items AS-D1 (unit counts missing for four counters), AS-D2 (§8's pins claim) |
| §9 | TARGET.md diff | CLEAN |

There is no line file in the frozen packet. The required changes below are packet-text changes for a fixes entry, plus conditions on
the line when it is written.

## 1. Objects
- At claude/l-new 95dc76d7 (worktree; `git merge-base --is-ancestor 95dc76d7 origin/claude/l-new` true):
  - docs/new/P-N5-ASC.md sha1 9c9cb50d89e8bba3232ca2790ddbf95f85580af6 (EQUAL to the Lead's relay), 19,345 bytes;
  - experiments/new/box193/asc.pins: 27 entries, all match (`sha1sum -c` with DOCS/ → docs/new/; the block's own path rule);
  - box193/check193.sh re-run: exit 0, output byte-equal to the committed check193.out (asc_logs/check193_rerun_95dc76d7.out).
    check.sh's «BOX 193 ASC» block tests exactly that diff plus two grep lines, both present.
- My tools (docs/referee/scratch/, no L-NEW code imported):
  - asc_quotes.py (premise quotes);
  - asc_cs.py (CS(M) exact maxima, RMON-2 witness);
  - asc_game.py (IDEAL-CYC replay on successor 26's own VJ engine xicyc_vj.py and Γ builder xicyc_replay.py, written from R104's text;
    e-priorities ordered by (level, gate index), so [E-LEV] holds there).
  - Logs in asc_logs/.

## 2. Premises (§1)
- Trunk: docs/RESULTS.md at 5470cc0c is byte-equal to trunk abc9aef8 (cmp). The line numbers 9864, 10085, 13607, 13677, 13682 and 13691
  are right.
- asc_quotes.py (every «…» of §1, fragments split at «…», RESULTS wrapped lines joined by one space):
  - [DEF]: all seven quotes verbatim in R104's line 9864; «the exact e-priorities to packet §3.1» verbatim at l. 10085.
  - [XICYC] (a): verbatim at l. 13677-13678 (R118's own «…» quote of the XICYC definition).
  - [XICYC] (b): «(b) Facts F1-F6 (§3 l. 68-83) with F4 REPLACED by F4′» verbatim at l. 13682.
  - F1, F2, F3: not RESULTS text; verbatim in the frozen P-N5-XICYC.md (sha1 149e2414…, l. 69, 71, 72-73), inside R118 (b)'s cited range
    §3 l. 68-83. The packet says exactly this («They are quoted from the frozen packet»). Correct.
  - (e): «C ≤ n·(2M + 2).» and its reason (R118 has the reason in parentheses, not «»; the packet's «…» around it is verbatim text)
    at l. 13691-13692.
- Used facts and their premises:
  - E-MON uses F1 + [VJ]'s order. CHAIN-DECOMP uses F3 and [DEF]'s one-edge e. §5 uses F1 + F2 (active intervals) and (e) (2M + 3
    cycle nodes, in strictly increasing reward). §6 uses [DEF] edges and [E-LEV].
  - Nothing uses [LOC], OVT-DV, IN-BOUND, F4/F4′, F5 or F6. Checked line by line.
- E-DOM derivation (inside E-MON): CORRECT. By [DEF]: movers 0, gates 1, unused loop 2, K2 3, K1 5, β ≥ 6, every e above every β, and
  c_W = top above every other priority so far, K0 = top + 2, K3 = top + 3. So a vertex more relevant than some e-vertex is an e-vertex,
  c_W, K0 or K3. The order AMONG e-priorities is not used (R104 leaves it open, l. 10085).
- [E-LEV]: textually only in §1 l. 46, the table l. 20, §6 (UP-JUMP l. 166 / 171, UP-B l. 179, NOUP l. 187) and §9 (l. 218, 225).
  §3-§5 use neither it nor the order among e's: the lex order on e-sets needs only that the e-priorities are distinct and even
  (F2: distinct rewards).
  - AS-2 (required): l. 20 says «UP-JUMP and UP-B under HYPOTHESIS [E-LEV]» and l. 46 says «(only for §6 UP-JUMP and UP-B)». NOUP is
    proved from UP-B and needs [E-LEV]; its heading (l. 187) and §9 (l. 225) say so. Fix both places to name NOUP.

## 3. Proofs (each step re-derived)
- E-MON: SIGN.
  - With equal cycle node, [VJ]'s order decides by the top z of Π_t Δ Π_(t+1): z ∈ Π_(t+1) if even, ∈ Π_t if odd.
  - c_W is never in Π (only a self-loop: on a play it is the cycle node).
  - K0 / K3: in IDEAL-CYC K0 → K3 and K3 → K2 are frozen. K3 is entered only from K0. K1, K2 are entered only from K0, K1, K2, K3, and K0
    only from K1 (frozen to K1) or from β's (u). So a play enters {K1, K2, K3} only through K0, passes K0 iff it passes K3 iff its cycle
    node is K1 or K2. Both plays have the same w, so both or neither hold K0 and K3, and when they do, both are in both Π's (top + 2,
    top + 3 > 5 ≥ w's priority).
  - Hence the top of the e-part of the symmetric difference is the top of the whole difference, it is even, it lies in Π_(t+1): E_t <
    E_(t+1); otherwise the e-sets are equal.
- CHAIN-DECOMP: SIGN.
  - f ∈ Π is more relevant than w, so it is on the prefix. Λ_t(f) = w ≠ f, so F3 applies at f, and e has one edge ([DEF]).
  - y_f ≠ c_W, else w = c_W, more relevant than f. The play from y_f is a suffix with the same cycle, so Π_t(y_f) is the part of Π_t(v)
    after f. Elements before f carry no e-vertex of Π.
  - The «Reading» (next_t is one forest on the e-vertices with cycle node w): the plays' prefixes have distinct vertices, so next is
    acyclic. An active e-vertex x more relevant than w is the first element of its own play's Π, so chain(x) = seq_t(x).
- SKELETON: SIGN.
  - (a): induction along the τ-path.
  - (b): every z strictly between τ^i and τ^(i+1) lies in chain(τ^i) ∖ {τ^i}, whose top is τ^(i+1); chain(z) is a suffix containing
    τ^(i+1), so τ(z) = τ^(i+1). The elements after τ^(i+1) are below it, so τ^(i+2) < τ^(i+1).
  - (c) follows. Every element of a chain is a skeleton node or in a segment, because the chain ends where τ = 0.
- τ monotone and the level count: SIGN.
  - The top of A ∖ {x} is non-decreasing when A grows lexicographically (removing a common element keeps the order; if max B < max A,
    then max A is the top of A Δ B and lies in A).
  - τ(x) ∈ {0} ∪ items ∖ {x}: M values. The hub top has M + 1 values. So the number of levels is ≤ M(M − 1) + M + 1 ≤ M² + M + 1. The
    packet's count is a valid (loose) bound.
- HUB-ASC(B): SIGN.
  - B = 0 (DESC-POLY). At a change with equal first element (= equal top), x := the last element of the common prefix lies on both
    values. Its chain is a descending suffix, so next = τ at both times, and τ(x) strictly rises from one value < x to another < x.
    τ(x) is monotone over all times, so this happens ≤ x − 1 times per x. Total ≤ M + M(M − 1)/2 = M(M + 1)/2.
  - B ≥ 1, the three shapes, checked against SKELETON:
    - (a) s ≠ T forces τ(s) = T > s. R(s) is s plus the segment before T, all with τ = T.
    - (c) s = T: the skeleton prefix y_0 … y_i is consecutive (the segments before it are empty); z := next(y_i) has τ(z) = y_(i+1) and
      z < y_(i+1).
    - (N) is the only remaining case. With hub ⊥ the value is ∅, a single value.
    - So the classification is exhaustive.
  - Fix(y) is determined by y and C = chain(y), since P(T) is fixed in the level. y = T arises only from (a), y < T only from (c).
  - The ascent split: ascents(R(z)) + 1 + ascents(chain(y)) ≤ B, so each part has ≤ B − 1 (their sum ≤ B − 1, even).
  - (i): the constant hub y is a hub of the restricted run (run property). Its value is a part of the hub's value, so ≤ B − 1 ascents.
  - (ii), the point the Lead named:
    - for w ∈ Z_y, chain(w) = R(w) ⊔ chain(y) with R(w) ⊆ Z_y (SKELETON (b) at w, i = 0);
    - at the times with chain(y) = C, every R(w) is lex-nondecreasing (the common part C is removed);
    - next restricted to Z_y (with ⊥ where next = y) is a forest whose chains are the R(w): a run of CS(|Z_y|) with NO constraint on its
      chains other than the hub's («CS(|Z_y|, ∞)»), which is exactly what HUB-ASC(B − 1) assumes;
    - z_t ∈ Z_y in both (a) and (c), and R(z_t) = hub value minus the constant Fix(y), so it is a hub with ≤ B − 1 ascents.
    - Conditioning on chain(y) = C is essential, and the proof does it: the box's DEAD RMON-2 witness (below) is a same-level step in
      CS(5, 2) where chain(5) = chain(τ(1)) changes and the part of chain(1) before τ(1) drops. That step lies outside (ii)'s times.
  - Per level ≤ 1 + M·F_(B−1)(M)² (F_(B−1) has nonnegative coefficients, so it is monotone in M); across ≤ M² + M + 1 levels, values never
    repeat.
  - Degree: d_0 = 2, d_B = 3 + 2d_(B−1), so d_B = 5·2^B − 3 (2, 7, 17, …).
- HUB-ASC-G: SIGN.
  - Active intervals: F1 + F2 make the reward of Λ_t(x) non-decreasing and strictly increasing at changes, so the times with Λ_t(x) = w
    form an interval.
  - The active set is closed under next (next_t(f) is in the same Λ-class). The hub f_t(v) is active. E-MON makes each active chain and
    the hub monotone.
  - Refined levels: τ changes ≤ M(M − 1), top ≤ M, activity ≤ 2M, so ≤ M² + 2M + 1 ≤ M² + 3M + 1 levels. Inside a level the active
    items form a genuine CS run, and HUB-ASC applies to its sub-runs. So even F_(B−1) could stand where F′_(B−1) stands; F′ ≥ F, so the
    packet's bound holds.
  - AS-1 (optional): F′_0 is not obtained «word for word» per level (that would give a factor M² + 3M + 1). It is DESC-POLY on the whole
    interval I, which works because τ(x) is monotone on x's active interval and x is active at both times of each change it is blamed
    for. One sentence would make this explicit; the bound is right.
  - Whole-run corollary: at most 2M + 3 Λ-intervals ((e)), M_w ≤ M, F′ monotone. «D_E(v)» (whole run) is used but not defined in §2;
    the meaning (distinct E_t(v) over the run) is clear. Optional AS-4: define it.
- UP-JUMP: SIGN (under [E-LEV]).
  - ℓ ≥ 1: at level 0, e → c_W would make w = c_W.
  - By the contrapositive of [E-LEV], b more relevant than a gives lev(x′) ≥ ℓ (b's gate is entered only from its mover x′).
  - β is frozen to its Ξ-target or to u, and u leads into the closed core, from which b is unreachable. e-steps go down one level.
    The first step reaching a level ≥ ℓ from y_a (level ℓ − 1) is a strictly upward Ξ-step into level ≥ ℓ.
- UP-B: SIGN (under [E-LEV]). The ascent segments are disjoint pieces of the prefix (distinct vertices); each holds a distinct
  upward β, i.e. a distinct counted option.
- NOUP: SIGN (under [E-LEV]); B = 0 in §5.

## 4. Replays with my own code
- Abstract (asc_logs/cs.log; asc_cs.py: nodes = (forest, hub), chains as rank bitmasks, so lex order = integer order; longest chain with
  componentwise ≤ masks and a strictly larger hub mask; topological order by (sum of masks, hub mask)):
  | M | hub ≤ 0 ascents | F_0(M) | hub ≤ 1 ascent |
  | --- | --- | --- | --- |
  | 1 | 2 | 2 | 2 |
  | 2 | 4 | 4 | 4 |
  | 3 | 7 | 7 | 8 |
  | 4 | 11 | 11 | 16 |
  | 5 | 16 | 16 | 29 |
  - EQUAL to §7: B 0 «11 at M 4», B 1 «16 at M 4, 29 at M 5», and the tightness row 2, 4, 7, 11, 16 for M 1-5. M 6, 7 (22, 29) come from
    dp193.c / data/cs_dp.txt and are not replayed.
  - My own run «max 4 99» was stopped: computing F_99 as a printed bound is doubly exponential (my script's bug; no data lost).
- RMON-2 witness CS(5, 2) (box doc Addendum 3; not a packet clause): both forests valid (chain(x) = x + chain(next(x))); every chain
  lex-nondecreasing; ≤ 2 ascents everywhere; τ = (5, 5, 4, 0, 4) before and after; the part of chain(1) before τ(1) = 5 drops from
  [1, 2] to [1]; chain(5) changes [5, 4] → [5, 3, 4]. Reproduced exactly, and it does not touch HUB-ASC (§3).
- Game (asc_logs/game.log; IDEAL-CYC Howard run from the stored start; every state, every vertex; Howard ties 0 on all four):
  | instance | T | U(G) | max ascents | E-MON units / viol | CHAIN-DECOMP units / viol | UP-JUMP ascents / viol |
  | --- | --- | --- | --- | --- | --- | --- |
  | RSG_K4 | 7 | 1 | 1 | 623 / 0 | 450 / 0 | 164 / 0 |
  | cR_d2_w8_R22 | 24 | 9 | 3 | 2,648 / 0 | 1,694 / 0 | 457 / 0 |
  | rd2_d9 | 21 | 20 | 3 | 2,415 / 0 | 2,154 / 0 | 1,417 / 0 |
  | RS3 | 13 | 6 | 2 | 3,185 / 0 | 812 / 0 | 42 / 0 |
  - U(G) and the max ascents equal §7's four UP-B rows exactly (1 ≤ 1, 2 ≤ 6, 3 ≤ 20, 3 ≤ 9). T equals check193.out's T on all four.
  - My units differ from the lane's (all vertices' plays, not only movers' plays with Λ below every e), so the unit counts are mine,
    not a check of the lane's counts.

## 5. DATA rule on §7, clause by clause
| clause | counter (unit, set, scope) | verdict |
| --- | --- | --- |
| E-MON, CHAIN-DECOMP, E-DOM | «tmonfail 0, decfail 0, edomfail 0», units named, 13 instances, IDEAL-CYC | AS-D1: the number of units of each is not given (check193.out prints no count for them) |
| UP-JUMP | «upfail 0», unit named | AS-D1: count not named (check193.out's «asc» field is probably it; the packet does not say) |
| UP-B | 4 instances, values given, unit (state, vertex) plays | OK (my replay equal) |
| NOUP | 300 genomes, seed 1, max ascents 0, max D_E 3 | OK |
| HUB-ASC exact maxima | B 0, 1 rows | OK (my replay equal) |
| SKELETON | all forests of CS(4), CS(5) | OK (the set is exhaustive: 125 and 1,296 forests, my count) |
| B = 0 tightness | M 1-7 | OK (M ≤ 5 replayed) |
| no-DATA list | B ≥ 2, HUB-ASC-G constants, whole-run corollary | OK; optional: add UP-B's D_E bound (its DATA covers the ascent count only) |
| §8 «sha1 of this packet and of every tool and instance it cites» | asc.pins | AS-D2: the five box192/inst instances (cR_d2_w8_R22, rd2_d9, rd2_d10, rd3_d7, rf_d5) are cited in §7 but not in asc.pins. They match box192/inst/SHA1SUMS, which check.sh does not run; the frozen-output diff of «BOX 193 ASC» guards them only indirectly |

## 6. Required and optional changes (fixes entry; the packet stays frozen)
- AS-2 (required).
  - Old (l. 20): «UP-JUMP and UP-B under HYPOTHESIS [E-LEV]»; new: «UP-JUMP, UP-B and NOUP under HYPOTHESIS [E-LEV]».
  - Old (l. 46): «(only for §6 UP-JUMP and UP-B)»; new: «(only for §6 UP-JUMP, UP-B and NOUP)».
  - Each old string occurs once in the packet (checked by grep -c).
- AS-D1 (required for the line): asc193.py prints, and the line states, the number of units of tmonfail, decfail, edomfail and
  upfail (or the packet names which printed field is the unit count).
- AS-D2 (required): either add the five box192/inst instances to asc.pins, or change §8's claim to name the instances it pins (8).
- AS-3 (condition on the line, when written): every UP-B / NOUP clause carries «under [E-LEV]». The packet's title says «in particular
  on genomes with boundedly many upward Ξ-edges (UP-B)» without it. And the line keeps the scope sentence: D_E,I(v) only, not R, not
  a running time, OVT-DV and IN-BOUND not landed.
- Optional: AS-1 (F′_0 sentence), AS-4 (define D_E(v)), the UP-B D_E bound in the no-DATA list.

## 7. Scope sentence and TARGET.md diff
- Scope sentence: CORRECT.
  - OVT-DV is «Lemma OVT-DV (PROVED-CONDITIONAL on [LOC], lane)» in docs/red/R217-ovt.md §2 on origin/claude/l-red, not landed.
  - IN-BOUND is a «CONJECTURE IN-BOUND» in docs/new/N5-RPOT-box192.md Addendum 9 (l. 390).
  - «OVT-DV» and «IN-BOUND» occur 0 times in trunk RESULTS.md.
  - No statement of the packet bounds R, a run length or a running time. §9 repeats the scope. The «N5′-xi stays a CANDIDATE» line
    agrees.
- TARGET.md: no statement concerns winning regions, an algorithm or a running time (TARGET.md §2-§4). It is not M3 (§7 e needs a
  precise theorem in TARGET vocabulary). CLEAN.
  - Note, no change: «M» here is the number of options / e-vertices (R104), not TARGET's m.

## 8. Tools and outputs (committed)
docs/referee/scratch/: asc_quotes.py, asc_cs.py, asc_game.py; asc_logs/cs.log, game.log, check193_rerun_95dc76d7.out.

## §C. Fixes entry 1 and line L-1 (REFEREE successor 27; date -u at writing 2026-11-07T23:51Z)
- Objects: a `git archive` of claude/l-new 19cc23e3 (ancestor of origin/claude/l-new), sha1 of the bytes:
  - L-1 docs/new/P-N5-ASC-line-L1.txt 08cced78a214080dac3f8f07ebc900510e3f35ab (EQUAL to the Lead's relay), 4,896 bytes, one line, 116
    «(» = 116 «)», 0 «|», one « — »;
  - fixes docs/new/P-N5-ASC-fixes.md 68139c3e… (entry 1); packet 9c9cb50d… unchanged.
- Machine check on the archive: box193/check193.sh exit 0, output byte-equal to the committed check193.out
  (asc_logs/check193_rerun_19cc23e3.out); asc.pins 34 rows, all match.
- String test (python str.count on L-1):
  - my AS-2 new strings «UP-JUMP, UP-B and NOUP under HYPOTHESIS [E-LEV]» and «(only for §6 UP-JUMP, UP-B and NOUP)» occur once each;
  - the old strings «UP-JUMP and UP-B under HYPOTHESIS [E-LEV]» and «(only for §6 UP-JUMP and UP-B)» occur 0 times;
  - AS-3: «under [E-LEV]» occurs 4 times. The title clause, the UP-B and NOUP clauses and the UP-B / NOUP DATA clauses all carry it;
    the scope sentence is kept.
- AS-D1 (unit counts are real): my sums over the 13 instance lines of the re-run output are edomunits 1,892, tmonunits 2,552, decunits
  24,818 and asc 1,956, with edomfail, tmonfail, decfail, upfail and gfail all 0. These are exactly L-1's numbers.
- AS-D2: the five box192/inst rows are in asc.pins with box192/inst/SHA1SUMS's sha1s; all 34 pins match.
- D-2 / D-3 (REFEREE-2): ug193 on all 13 instances, max ascents ≤ U(G) on every one (re-run output); chain193.py M 6 = 22, M 7 = 29 at
  A 0, re-run by check193.sh.
- AS-1, AS-4: taken. L-1's D_E(v) := «the number … of distinct (Λ_t(v), E_t(v))» is at least the number of distinct E_t(v), and the
  (2M + 3)·F′ bound holds for it (a sum over the at most 2M + 3 Λ-intervals).
- New clause «[E-LEV] is NECESSARY …»: CORRECT.
  - REFEREE-2's «UPB/NOUP fail on 209 of 21,116 plays of U = 0 genomes (up to 2 ascents).» occurs verbatim at 533744a5.
  - L-RED R220's «NOUPC_1 / 2 / 3 have U(G) = 0 and max ascents 2 / 3 / 4, in 120 / 450 / 280 (t, v) pairs» and «NOUPC_1, t 0, v 10»
    occur at 68a1f609. The three .pg sha1s are equal to L-RED's inst/SHA1SUMS and to the bytes.
  - SECOND ROUTE (mine, asc_elevrev.py on my own Γ builder and VJ engine; NOUPC_{1,2,3}.json from 68a1f609, e-priorities
    re-assigned in the order (−level, gate); asc_logs/elevrev.log):
    - U(G) 0, 0, 0; max ascents 2, 3, 4; (t, v) pairs with ≥ 1 ascent 120, 450, 280: EQUAL to R220;
    - with the (level, gate) order: 0 ascents on all three (NOUP holds).
    - So «one route only» is now two routes for the max-ascent numbers.
    - Not re-checked: the witness «t 0, v 10»: my vertex numbering differs from L-RED's .pg. My engine has Howard ties (1, 2, 0) on
      the three; the counts agree anyway.
  - «the order of Γ(G) as built by gamma3.py (and of R104's packet §3.1)»: R104's packet P-N5-REALIZE §3.1 l. 89 orders the e's «by
    (lev(owner), gate index)». CORRECT.
- DATA rule on L-1, clause by clause: every clause has a counter of matching unit, set and scope (the four AS-D1 counts, UP-B 13 / 13,
  NOUP 300, HUB-ASC rows, SKELETON, tightness M 1-7, the two [E-LEV] controls), or the no-DATA entry (HUB-ASC with B ≥ 2, HUB-ASC-G's
  constants, the whole-run corollary, UP-B's D_E bound). MET.
- Notes, no change required:
  - L-1's units «vertices» (E-DOM) and «W-target with Λ fixed» (E-MON) are shorter than fixes entry 1's definitions («vertices other
    than c_W, K0, K3 and the e's»; «W-target or c_W-successor y»). The fixes entry governs and the counts are those fields.
  - Fixes entry 1 calls «the order of Γ(G) as built by … not in a landed line» R220's wording; it is not verbatim in R220-asc.md. It is
    not quoted in L-1, so no change is needed.
- Verdict: fixes entry 1 CORRECT for AS-2, AS-3, AS-D1, AS-D2, AS-1 and AS-4. L-1 MATCHES. All statements stay SIGN.

## §D. Fixes entry 2 and line L-2 (REFEREE successor 28, Opus 5.5, D15; date -u at writing 2026-11-08T01:07Z)
- Objects: claude/l-new a5dcf9c6 (ancestor of origin/claude/l-new), read by `git show` / `git archive`:
  - L-2 docs/new/P-N5-ASC-line-L2.txt: sha1 f109cb69507efd863133a08a2e90096ad2acb7f5 (EQUAL to the Lead's relay), 4,907 B, one line,
    116 «(» = 116 «)»;
  - L-1 is unchanged (08cced78…, 4,896 B); the packet is unchanged (9c9cb50d…);
  - fixes docs/new/P-N5-ASC-fixes.md: 28cf8f9f…, 8,108 B; entry 1 unchanged, entry 2 appended.
  - Since 19cc23e3 the only box193 changes are asc193.py (the W-4 test, two lines), asc.pins (re-pins, plus L-2) and a new
    data/cs_m8.txt (not cited by L-2).
- Byte test (scratch/asc_l2.py, asc_logs/l2_bytetest.out):
  - «(consecutive state pair, W-target with Λ fixed) pairs» → «(consecutive state pair, W-target or c_W with Λ fixed) pairs» (W-3), and
    «with fixes entry 1» → «with fixes entries 1-2».
  - Each old string occurs once in L-1 and 0 times in L-2. Each new string occurs once in L-2.
  - L-1 with exactly these two changes is byte-equal to L-2: sha1 f109cb69…, 4,907 B.
- My AS-2 / AS-3 strings hold on L-2:
  - «UP-JUMP, UP-B and NOUP under HYPOTHESIS [E-LEV]» and «(only for §6 UP-JUMP, UP-B and NOUP)» occur 1 / 1 times.
  - The old forms occur 0 times.
  - «under [E-LEV]» occurs 4 times, as in L-1.
- W-3 in meaning: CORRECT.
  - asc193.py's docstring (l. 7, l. 12) defines tmonunits over «W-target or c_W successor y». Entry 1 already said so.
  - The count is unchanged: 2,552.
- W-4 in meaning: CORRECT.
  - UP-JUMP (packet l. 166-168) asserts a β whose Ξ-target is a mover «of level > the level of the mover it was entered from, and ≥ ℓ».
  - The new test requires lev(nxt[z]) ≥ la AND lev(nxt[z]) > lev(z's own mover), where z's own mover is name[z][1][0] for z = β_(x,k).
    That is exactly the lemma's condition: the mover a β is entered from is its own mover x.
- Re-run of check193.sh on the a5dcf9c6 archive: exit 0. Its output is byte-equal to the committed check193.out
  (asc_logs/check193_rerun_a5dcf9c6.out).
  - My sums over the instance lines: asc 1,956, upfail 0, tmonunits 2,552, tmonfail 0, edomunits 1,892, decunits 24,818.
  - The set and every count are unchanged, as the entry says.
  - asc.pins has 35 rows, all matching (DOCS/ → docs/new/).
- DATA rule: no clause changes except W-3's unit wording, which now matches the counter. MET.
- Verdict: fixes entry 2 CORRECT (W-3, W-4). L-2 MATCHES, by the byte test and in meaning. All statements stay SIGN.

## §E. Line L-3 (CHECKER C135 R1-R4) (REFEREE successor 28, Opus 5.5, D15; date -u at writing 2026-11-08T04:09Z)
- Objects: claude/l-new a2512364 (ancestor of origin/claude/l-new).
  - L-2 there is unchanged (f109cb69…).
  - L-3 docs/new/P-N5-ASC-line-L3.txt: sha1 0012d6710983ec339be8f5d4e051a205cc9207ba, 5,154 B (EQUAL to the relay and to C135 §5's
    target), 122 «(» = 122 «)».
- Byte test (scratch/asc_l3.py; R1-R4 copied from C135 §5 at claude/checker 0942e8be, wrapped lines joined by one space;
  asc_logs/l3_bytetest.out):
  - Each old string occurs once in L-2 and 0 times in L-3. Each new string occurs once in L-3.
  - L-2 + R1..R4 in order is byte-equal to L-3.
- My AS-2 / AS-3 strings hold on L-3: 1 / 1 / 4, old forms 0.
- Meaning:
  - R1 (source note «successors 61-62»): CORRECT. Fixes entries 1-2 are successor 62's.
  - R2 (AS-1): CORRECT. I read it as the author lane.
    - REFEREE R-P-N5-ASC §3 l. 117-119 (AS-1) says that F′_0 is DESC-POLY on the whole interval I, not «word for word» per refined
      level, «because τ(x) is monotone on x's active interval and x is active at both times of each change it is blamed for».
    - Fixes entry 1 «AS-1 … TAKEN» restates it as the proof of record.
    - REFEREE-2 checked it independently (R2-P-N5-ASC l. 212-214: «I agree. I checked it now … F′_0 = F_0 holds»).
    - So «referee-originated …, signed by both referees» is accurate.
  - R3 («hence seq_t(v) = (f, seq_t(y_f))»): CORRECT. It is the packet's own second sentence of CHAIN-DECOMP (l. 81: «Hence seq_t(v) =
    (f, seq_t(y_f)).»): v's play after f is y_f's play, with the same Λ.
  - R4 (definitions): CORRECT. It is the packet's l. 52-55 («seq_t(v) := the e-vertices that lie in Π_t(v), in the order of the play»;
    «An ascent of a sequence … is an index i with c_(i+1) more relevant than c_i»).
- NEW FINDING (R5, required; missed by REFEREE 27 and REFEREE-2 on L-1 and L-2, and not in C135): CHAIN-DECOMP's HYPOTHESIS in the line
  is weaker than the packet's, and false as worded.
  - The line (L-1 to L-3, unchanged by R1-R4) says «(Lemma CHAIN-DECOMP) if the first e-vertex on v's play is f, then f's successor y_f
    is a mover with Λ_t(y_f) = Λ_t(v) and …».
  - The packet's lemma (l. 80) says «If seq_t(v) = (f, …), then …», which needs f ∈ Π_t(v).
  - Instance: v = e_g for any level-0 gate g. The first e-vertex on v's play is v itself, its successor is c_W, which is not a mover, and
    Λ_t(v) = c_W, so v ∉ Π_t(v). The line's clause fails, while the packet's lemma does not apply (seq_t(v) is empty).
  - Shown on RS2 (option (0, 0)) and LEAP_k8 (option (0, 0)) with my own builder and engine (scratch/asc_cd_l0.py,
    asc_logs/cd_level0.out). It holds in every genome that has a level-0 mover.
  - R5: old «(Lemma CHAIN-DECOMP) if the first e-vertex on v's play is f, then»
    new «(Lemma CHAIN-DECOMP) if seq_t(v) = (f, …), i.e. the first e-vertex on v's play is f and f ∈ Π_t(v), then»
  - The old string occurs once in L-3. L-3 + R5: sha1 4017305a34eac21615ba8f172a9b899544d25659, 5,198 B, 125 «(» = 125 «)»
    (asc_logs/l3_r5.out).
  - The statement as signed (the packet's) is unaffected. The line misstates its hypothesis. DATA rule: R5 is a statement wording; its
    witness is asc_cd_l0.py.
- Verdict:
  - L-3 = L-2 + exactly R1-R4 (byte test PASSES). R1-R4 are CORRECT in meaning.
  - L-3 does NOT YET MATCH the packet: R5 is required.
  - All statements of P-N5-ASC stay SIGN (the packet's form).

## §F. Line L-4 (R5) (REFEREE successor 29, Opus 5.5, D15; date -u at writing 2026-11-08T05:47Z)
- Objects: claude/l-new a744677e (ancestor of origin/claude/l-new, checked).
  - L-3 there is unchanged: docs/new/P-N5-ASC-line-L3.txt sha1 0012d671… (byte-equal to L-3 at a2512364).
  - L-4 docs/new/P-N5-ASC-line-L4.txt: sha1 4017305a34eac21615ba8f172a9b899544d25659, 5,198 B, one line, 125 «(» = 125 «)».
    EQUAL to the Lead's check and to successor 28's prediction in §E.
- Byte test (my own script scratch/asc_l4.py; R5 strings copied from §E; asc_logs/l4_bytetest.out):
  - R5 old string: 1 in L-3, 0 in L-4. R5 new string: 0 in L-3, 1 in L-4.
  - L-3 + R5 is byte-equal to L-4.
  - R1-R4 new strings and my AS-2 / AS-3 strings still hold on L-4 (1 each).
- Lane script: experiments/new/box193/mkl4_193.py re-run from the repo root at a744677e rewrites L-4 byte-identically (git status clean).
- Pins: experiments/new/box193/asc.pins at a744677e, 39 rows, all match (sha1sum -c with DOCS/ = ../../../docs/new/). New rows: the
  fixes file (entry 4), L-4 and mkl4_193.py.
- Meaning:
  - Fixes entry 4 states R5 as in §E and accepts it; it changes no packet text, tool or DATA output. CORRECT.
  - In context, L-4 now reads «(Lemma CHAIN-DECOMP) if seq_t(v) = (f, …), i.e. the first e-vertex on v's play is f and f ∈ Π_t(v), then
    f's successor y_f is a mover with Λ_t(y_f) = Λ_t(v) and E_t(v) = {f} ∪ E_t(y_f), hence seq_t(v) = (f, seq_t(y_f))». This is the
    packet's l. 80-81 hypothesis and conclusion. The level-0 instance of §E (v = e_g, seq_t(v) empty) no longer falls under it.
- Optional (AS-L5, not required): the source note still reads «with fixes entries 1-2 … L-NEW successors 61-62». Entries 3-4
  (successor 63) change only the line, not the packet's statements, so the note is not false. A later line may name «fixes entries
  1-4; L-NEW successors 61-63».
- Verdict: L-4 MATCHES (L-3 + exactly R5; R5 CORRECT). The line now matches the packet. All statements of P-N5-ASC stay SIGN.
