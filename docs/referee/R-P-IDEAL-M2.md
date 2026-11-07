# R-P-IDEAL-M2: REFEREE report on P-IDEAL-M2 (L-NEW successor 51, box 156)
REFEREE successor 23 (Opus 5.5, D15), 2026-11-04T07:29Z by date -u. Independent: I did not read docs/referee-2/.
- Object: claude/l-new 6bcfa0de, an ancestor of origin/claude/l-new. I re-measured both files:
  - docs/new/P-IDEAL-M2.md: sha1 bc47b06c4b8d90ceb28939c966083e0c057a442b, 171 lines;
  - docs/new/P-IDEAL-M2-line-L1.txt: sha1 0160d1e3ffa832536454a74c559b20280b87f53e, 1 line, no «|».

## 0. Verdicts
| § | statement | verdict | notes |
| --- | --- | --- | --- |
| §1 | Lemma MULTI-CHARGE | SIGN | |
| §1 | Corollary M2-EQ | SIGN | |
| §1 | Corollary SINGLE-SHORT | SIGN | |
| §2 | Lemma TRIGGER (a)-(c) | SIGN WITH GAP M2-G1 | (b) cites LOCAL's line summary; it needs R105's LOCAL (a) |
| §3 | Lemma XIFLIP | SIGN | |
| §3 | Corollary MIN-FLIP | SIGN WITH GAP M2-G1 | the XF bound needs R105's LOCAL (b) |
| §4 | DEAD LIN-156 (T part), instance max_d4_L13 | SIGN | recomputed with my own simulator: T 13 > 12 |
| §5 | machine check, exclusions, TARGET diff | not to sign; w105 re-run MATCHES; diff agreed | |
| line | L-1 | NOT YET | REQUIRED M2-L1 (a DATA overclaim) |
- Labels.
  - PROVED (lane + REFEREE): MULTI-CHARGE, M2-EQ, SINGLE-SHORT, XIFLIP. TRIGGER and MIN-FLIP become PROVED once M2-G1 is fixed.
  - DEAD (instance): LIN-156's T part. 13 exceeds the explicit bound 12, so L43 is met.
  - Nothing is bounded polynomially. G-N5-TIME OPEN.

## 1. Premise route (R105 quotes against landed RESULTS)
- R105 is on trunk (e951db48, «### R105 [refereed-only]»). I grepped every quote the packet attributes to R105, as a literal string in
  that heading line. ALL FOUND verbatim:
  - XI-NEW: «for t ≥ 2 every least-level mover h of step t moves to an option w ∉ A_(s_(t−2))(h)»;
  - RISE: «that option's value rose strictly at step t − 1, and some strict Ξ-descendant of h on its chain under s_(t−2) moved at
    step t − 1»;
  - CHAIN-BACK: «T ≤ N (1 + U) with U the number of unchained steps t ∈ [2, T]»;
  - ENC: «the Ξ-order of β-sets is the order of the integers Σ ±2^rank»;
  - LOCAL: «an option's value depends only on the states on its chain» and «a key only on the states below its level»;
  - KEYFLIP: «moves(x) ≤ 1 + KF_x with KF_x the number of steps at which KP(x) changes»; and «KP_s(x) the key-preferred option under
    the keys of s».
- Other premises: R104's definition only (§0 restates it, and it agrees with R104 / R105 §0). No docs/lit and no docs/sources. R106
  is listed as not used, and that is correct.
- M2-G1 (citation gap, closable).
  - The landed LINE form of LOCAL, «an option's value depends only on the states on its chain», counts the option's OWN mover as on
    its chain (the chain starts at (x, k)).
  - TRIGGER (b) needs «values of (z, o), (z, o′) unchanged from s_(t−2) to s_(t−1) when no mover y ≠ z on their chains moved». But z
    itself can be in Mv_(t−1), as in case 2 of (a)'s proof.
  - Likewise, MIN-FLIP's «XF_x ≤ #(steps moving a strict Ξ-descendant)» needs the values of x's options unchanged when x itself moves.
  - The needed forms are R105's LOCAL (a) («If two states s, s′ agree on every mover of the chain of (x, k) under s other than x …»)
    and LOCAL (b) («agree on every strict Ξ-descendant of x ⇒ Ξ_s(x, k) = Ξ_(s′)(x, k) for every k»), from the landed packet
    docs/new/P-IDEAL-RED.md §1.
  - Fix: quote these two forms in place of the line summary. The mathematics is unaffected, and both forms are in the landed entry's
    signed packet.

## 2. Proof checks
- MULTI-CHARGE: SIGN.
  - XI-NEW + RISE give Z_t ≠ ∅.
  - If |Mv_(t−1)| = 1, then Mv_(t−1) = {h_(t−1)}, and Z_t ⊆ Mv_(t−1) forces Z_t = {h_(t−1)} on the chain under s_(t−2): chained.
  - So an unchained t has |Mv_(t−1)| ≥ 2, with t − 1 ∈ [1, T − 1], injective. CHAIN-BACK then gives T ≤ N(1 + M₂).
- M2-EQ: SIGN. M₂ counts a subset of [1, T − 1]. (⇒) M₂ ≤ T; (⇐) T ≤ N(1 + p).
- SINGLE-SHORT: SIGN. M₂ = 0 gives T ≤ N.
- TRIGGER: SIGN WITH GAP M2-G1.
  - (a): with no flip, the Ξ-preference for o′ and the key-preference for o′ both already held for step t − 1.
    - Case s_(t−2)(z) = o: step t − 1 would pick o′.
    - Case s_(t−2)(z) = o′: the move o′ → o at t − 1 needs Ξ(o) ▷ Ξ(o′) at s_(t−2), against strictness.
    - Correct. At degree 2, s_(t−2)(z) ∈ {o, o′}.
  - (b): correct given LOCAL (a) (M2-G1). Acyclicity makes every later chain mover a strict Ξ-descendant.
  - (c): correct by the key half of the LOCAL quote.
  - Its «Does NOT claim» parenthetical («it is one: (c) gives a second mover …») is a true one-line consequence of (c).
- XIFLIP: SIGN.
  - Consecutive moves a < b go o → o′ → o. σ differs at s_(a−1) and s_(b−1) (strict, total order), so some j ∈ [a, b − 1] flips.
  - The ranges are disjoint.
- MIN-FLIP: SIGN WITH GAP M2-G1.
  - The KEYFLIP quote is exact.
  - The XF bound needs LOCAL (b) (M2-G1).
  - The KF bound: KP_s(x) reads keys of x, which read levels < lev(x). Correct.
- DEAD LIN-156: SIGN.
  - The conjecture's text at 4047aacf (docs/new/N5-M2-box156.md l. 34-35): «for every IDEAL-ACYC genome of degree ≤ 2 with N movers
    and every start, T ≤ ⌊3N/2⌋ and M₂ ≤ N + 1». It EQUALS the packet's quote.
  - Instance file: experiments/new/box156/ext/max_d4_L13.json at 6bcfa0de, sha1 f0735b61…. It equals L-RED's
    experiments/red/r197/lag/max_d4_L13.json (same sha1) and the packet's inline copy, field by field.
  - My own checks:
    - acyclic (DFS); W-targets exactly one level down; ranks and gates distinct; degree 2 everywhere.
    - My β-SET simulator (written from R104's text; scratch/xinew_probe.py) gives T = 13 > ⌊3·8/2⌋ = 12.
    - |Mv| = 1, 1, 2, 1, 1, 2, 3, 2, 1, 1, 2, 1, 1, so M₂ = 5.
    - XI-NEW, all-option monotonicity and RISE: 0 violations on this run.

## 3. Machine checks
- w105 at 6bcfa0de, all six commands of the block verbatim, in a detached worktree (2 s). Every output line equals check.sh's expected
  string:
  - MCHARGE 54 runs: VIOL 0; 34,934 runs: VIOL 0, single_maxT_over_N 1.0;
  - TRIG 54 runs: NEITHER 0, WNOLOW 0, XNODESC 0, XIFLIP 0;
  - TRIG 3,981 runs: zeros;
  - NEG=3: NEITHER 141;
  - val.py: T 13, M2 5, U 4.
  - MATCHES.
  - The pins (packet bc47b06c, L-1 0160d1e3) equal my re-measurement.
- Observation (DATA strength). trig.py's 3,981 random runs contain only 298 moves, with WT 0 and WREL 0. So TRIGGER (c) and the
  W-branch of (a) are exercised only by the 54 corpus runs (WT 333).
- Own check: docs/referee/scratch/m2_probe.py, on my β-set simulator; random degree-≤-2 genomes, BIG=1; log
  xinew_logs/m2_probe.txt.
  - 4,000 runs (seeds 1, 2), 4,176 steps, 530 unchained steps, 751 multi-mover steps, 135 W-triggered moves.
  - MULTI-CHARGE 0, TRIGGER (a) 0, (c) 0, XIFLIP 0 violations.
  - Control MUT=1 (keys of the old state), seed 3: MULTI-CHARGE 39, TRIGGER (a) 425. The checks bite.

## 4. Diff against TARGET.md
- No statement mentions a parity game, a winning region, an algorithm's running time or a cost model (TARGET §1-§3). Each is about the
  step sequence of R104's IDEAL model.
- The DEAD item refutes a lane conjecture about that model only.
- Agreed with packet §5: not M4, not M3, not a gauntlet step. G-N5-TIME OPEN.

## 5. Line L-1, word by word against the packet
- MATCHES:
  - scope and premises (R104 definition; R105 items by name; acyclic; any width);
  - definitions of T, Mv_t, U and M₂;
  - the any-degree group: MULTI-CHARGE, M2-EQ, SINGLE-SHORT;
  - the degree-≤-2 group: TRIGGER, XIFLIP, MIN-FLIP;
  - DEAD with its instance and sha1;
  - the tail (REDUCTION / EQUIVALENCE, nothing bounded, LIN-2 not claimed, exclusions, OPEN, not M3 / step 4 / TARGET).
- REQUIRED M2-L1 (DATA overclaim).
  - «on 34,934 / 3,981 all-start random runs»: by packet §5, the 34,934 MULTI-CHARGE runs are «every start of each genome with N ≤ 8,
    the genome start of the others». They are not all-start runs. Only the 3,981 trig.py runs are all-start.
  - New: «on 34,934 random runs (every start for N ≤ 8, the genome start otherwise; mcharge.py) and 3,981 all-start degree-≤-2
    random runs (trig.py)».
  - Precedent: C108 E-1, «A DATA label does not cure an overclaim».
- OPTIONAL:
  - M2-L2 (TRIGGER): «caused by» → «and then … moved» (the lemma states existence, not causation); and «on one of their chains» →
    «… under s_(t−2)» (the packet's form; the unanchored form is also true).
  - M2-L3: name N and M («N movers, M options») at first use.
  - M2-L4 (DEAD): add the explicit bound «T 13 > ⌊3·8/2⌋ = 12» and «from its stored start».
- VERDICT: line L-1 NOT YET. It matches once M2-L1 is applied. M2-G1 is a packet citation fix (fixes file), not a line change: the line
  cites «R105's … LOCAL», which includes LOCAL (a)/(b).

## DONE / FINDINGS / NEEDS
- DONE:
  - this report;
  - w105 re-run at 6bcfa0de: MATCHES;
  - every R105 quote is verbatim;
  - the DEAD instance is recomputed independently (T 13 > 12);
  - own m2_probe.py: 0 violations, and the control bites.
- FINDINGS:
  - 5 SIGN (MULTI-CHARGE, M2-EQ, SINGLE-SHORT, XIFLIP, DEAD LIN-156).
  - 2 SIGN WITH GAP M2-G1 (TRIGGER, MIN-FLIP): a LOCAL citation that is too coarse, closable.
  - Line L-1 NOT YET (M2-L1, DATA overclaim).
  - trig.py's random runs exercise no W-triggers.
- NEEDS: Lead: route M2-G1 (fixes entry) and M2-L1 (optionally M2-L2 to L4) to L-NEW 51. I will do a §C when they are frozen.

## §C (2026-11-04T08:52Z by date -u, successor 23; Opus 5.5, D15): fixes entries 1-2 and line L-2
- Object: claude/l-new 4d244698, an ancestor of origin/claude/l-new. I re-measured every file:
  - docs/new/P-IDEAL-M2-fixes.md: sha1 66fd6173…, 50 lines;
  - docs/new/P-IDEAL-M2-line-L2.txt: sha1 c890f268…, 1 line, no «|»;
  - packet: unchanged, bc47b06c, 171 lines;
  - line L-1: unchanged, 0160d1e3.
- Entry 1 (M2-G1): CLOSED.
  - The quoted forms are in the landed R105 body, item «(b) Lemma LOCAL» (docs/RESULTS.md at trunk 651fb144, l. 10214-10217).
    - They are verbatim, modulo a line break inside the first quote, which is why a single-line grep misses it.
    - «(b) the same for every k when s, s′ agree on every strict Ξ-descendant of x» is verbatim RESULTS text. (RESULTS paraphrases the
      packet's (b) there, unquoted. The paraphrase is sufficient: equal values for every k.)
  - TRIGGER (b) replacement: LOCAL (a) is applied with s = s_(t−2), s′ = s_(t−1), x = z, for k ∈ {o, o′}. Its hypothesis excludes z
    itself, so the conclusion holds whether or not z moved. Correct.
  - MIN-FLIP XF replacement: LOCAL (b) is applied with s = s_(j−1), s′ = s_j. Correct.
  - The premise route is still landed RESULTS only.
  - TRIGGER and MIN-FLIP are now SIGNED, without gap. All 7 statements are SIGNED.
- Entry 2 against my own word diff L-1 → L-2 (split on blanks): 15 hunks, equal to entry 2's 15 items, and nothing else differs.
  - M2-L1 is MET: «34,934 random runs (every start for N ≤ 8, the genome start otherwise; …mcharge.py) and … 3,981 all-start
    degree-≤-2 random runs (…trig.py)». This is packet §5 exactly.
  - M2-L2 is MET: TRIGGER now says «and then some … under s_(t−2) moves at step t − 1» / «and then some mover of lower level moves at
    step t». This is (b)/(c) as existence statements.
  - M2-L3 is MET: N and M are named.
  - M2-L4 is MET: «from its stored start T 13 > ⌊3·8/2⌋ = 12».
  - REFEREE-2's MIN-FLIP binders: moves(x) and KF_x (R105 KEYFLIP's) are now bound. Correct.
  - REFEREE-2 P-1: U's definition carries «as a mover other than h_t». This is packet §0 verbatim in substance, and it is needed.
- VERDICT: line L-2 MATCHES. All 7 statements SIGNED with entry 1.

### Answer to the Lead (08:53Z): R105's landed line against the signed P-IDEAL-RED
- R105's heading text, without the label, is word for word the P-IDEAL-RED line L-2 (l-new ffeb9736, sha1 65ba7ca7) plus the
  CHECKER tail. I checked this with a word diff.
- So R105-E1 (CHAINED defined without «as a mover other than h_t») is a defect of L-2 that I MATCHED in R-P-IDEAL-RED §C addendum 1.
  It is MY MISS.
  - Packet §4 defines CHAINED with «(as a mover other than h_t)».
  - Without it, a step with h_(t−1) = h_t is chained, because h_t lies first on its own chain, and CHAIN-BACK (i) «π(h_t) <
    π(h_(t−1))» is false for it.
  - Lesson: when matching a line, check every DEFINITION in it against the packet's §0, not only the claims.
- Other places where R105's line is coarser than the packet (I re-read every definition):
  - R105-E2 (precision, recommended for the same erratum). TOP-MONO: «RANK_t := 1 + #(unstable movers above y_t before the step)».
    «above» is not anchored. The packet's RANK_t counts x ∈ S(s_(t−1)) with π(x) > π(y_t), and «above» could be read as «of higher
    level». Fix: «… with π above π(y_t) …».
  - R105-N1 (no erratum needed; it is now known and handled). LOCAL's line summary «an option's value depends only on the states on its
    chain» is true but coarser than LOCAL (a)/(b). Citing packets must use the body forms, as P-IDEAL-M2 entry 1 now does.
  - R105-N2 (no erratum needed). INTERVAL-RESTRICT's «step a + j» leaves «a» unnamed (my optional note in R-P-IDEAL-RED §C add. 1).
    It is unambiguous in context: a is the index of the interval's first state.
  - Everything else matches the packet's definitions: h_t, y_t, c_s, KP_s, A_s, ε, U (with t ∈ [2, T]), the TOP_k padding, R := 0,
    U*, and the degree split.
