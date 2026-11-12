# L-COMP notebook
Overwrite the top sections; append to "Sources opened" and "Dead ends".

## HANDOVER -- successor 19 (L-COMP 19; session_01V5yGRY8iNCAZqwL8HSCXM2) PARKS 2026-11-12 (date -u in the park commit) after BOX 43. NOTHING RUNNING.
- «go» for BOX 43: Lead 13:17Z (handover check 3f8d27af accepted). Record: experiments/comp/box43/README.md (all DATA). Pushes: item 1
  at 90874f76; items 2-3 + this handover in the park commit.
- Item 1 (box 208, claude/l-new 8db300fe, on MY engine ideal37): (a) L-NEW's 16 LEVEL counters + 6 plateau counters on my history: 0 on
  25 records + 53 corpus (lines identical to its frozen files) + 57 of my frozen genomes; MY 23 counters (lev43.py, from the text): 0 on
  137 frozen runs, 3,300 random, 1,350 mutants; controls fire. (c) T_CYC / ALL-TCYC bound <= 5.6e-04 everywhere (constants untested).
  (b) lift to Howard on G_N / switchallexp: first failure (K5) at N = 2, state 5 (g2, f2), z = f2 odd above the escape h1: the failing
  step is (K2) COARSE, the property E-DOM; on G_N Phi takes only (N + 1)^2 − 1 values, the exponential is in the plateaus
  (9·2^(N−2) − 2): Lemma PLATEAU is what G_N defeats. Two engines (n5b / si.py) agree on every value.
- Item 2 (DHIB line): trace = repeater gate (10, 0) (7 deep flips, a staircase nest of top e-vertices), cascade gates (76..83, 1), hub
  18. Clone families D18(k), D10(k), D80(k) (clone42's rule on DHIB26_2804): Deep_3 = 24 + 17k / 24 + 9k / 24 + k exactly, N + M up to
  1,168; per-gate max 7, dmaxInt 6, T3 28 constant; two engines agree on 13/13 points. Linear; nothing faster.
- Item 3 (one gate): tail43.py, TAIL_h(G) = sink Ξ-targets retargeted to a chain of one-option movers with even Ξ self-loops (Odd must
  escape through each): the run is unchanged (7 genomes: T3, sigma, Odd's choices equal) and every Λ-quiet K1-flip gets depth + h or
  more, so Deep_3(TAIL_2(G)) = QF_K1(G) (all Λ-quiet internal flips after t0) exactly on the 7. TMWR(n) = TAIL_2(MWR(n)): ONE gate with
  2n + 1 deep flips (n 4-48, N + M 153-1429; BOTH engines on all 13 tail instances: per-gate max 2n + 1, whole-run deep 3n + 1,
  dmax 5; own34 needs ~35 min at N + M 1,429). READING sent to the Lead: the
  depth cut-off of DEEP3 does no work on a tail-closed class; DEEP3 is as strong as «quiet internal flips polynomial».
- Open (not started): (a) a depth notion TAIL cannot inflate (e.g. depth among the e-vertices not common to both faces) and its count
  on the frozen sets; (b) the per-gate quiet-flip maximum beyond linear (BOX 36/37 found linear only); (c) L-NEW's --hist form of
  plat208.py, if published: re-run run43a.sh (my wrapper plathist43.py calls its function unchanged).
- Things only I know: second-engine trees are ARCHIVES in the scratchpad (lost on a new container): eng/lsi100 (l-si 23d39400
  experiments/si experiments/harness), eng/red (l-red 59daaef2 experiments/red experiments/harness experiments/hard-families
  experiments/n5-second), eng/lnew (l-new fcba92fc experiments/new experiments/si/si.py experiments/harness), eng/lnew208 (l-new 8db300fe,
  same paths + n5-second, hard-families, docs/new/N5-LEVEL-box208.md), eng/llit (l-lit a19fff23 docs/lit/T66-*.py experiments/si/si.py
  experiments/harness experiments/hard-families); rebuild each with `git archive <sha> <paths> | tar -x -C <dir>` (no worktrees needed).
  cross100: RED=eng/red LNEW=eng/lnew CMAX=3 python3 -I eng/lsi100/experiments/si/box100/cross100.py inst <abs path> (how3_232 needs
  ~8 min at N + M 1,170 with 800 gates). own34 / deep41: ~20 s at N + M 400, ~3 min at 1,100. A push takes ~25 min (verify runs every
  lane's check.sh): batch commits. T66's G_N table has a priority collision (g_n = a_1 = 4n + 4); lev43.lmcs indexes vertices by sorted
  name like L-LIT's. Genome movers need NOT be ordered by level (MWR is not). bin/ (fast36/37/38) and Oink were never rebuilt this
  session (not needed). Do not rewrite a bash script while a job runs it.
- Slips (disclosed to the Lead): first local handover-check commit carried a model name (never pushed; redone with reset --soft; Lead
  13:17Z: acceptable); one job started with a bare «&» (killed within a minute, restarted as a tracked task).

## HANDOVER -- successor 18 (L-COMP 18, Opus 5.5; session_01V5yGRVyip8PwDCTvydpDg1) PARKS 2026-11-12 (date -u in the park commit) after BOX 42. NOTHING RUNNING.
- Boxes done this session (records = the READMEs; all DATA): BOX 39 (box39: Q_(>c) counter = L-NEW/L-RED; Q_(>1) climbs 10 @303, 18 @612;
  fit NOT identified), BOX 40 (box40: box 99 SCC census = L-SI 26/26; ties G1 small; SCC-LIN climbs max 0.8), BOX 41 (box41: DEEP3
  counter = box 100 26/26, DEEP3 proper 38; Deep_3 climbs 2 / 10; size-floor SCC-LIN 0.427), BOX 42 (box42: fixed family CL(k) on the
  C6G8 line: Deep_3 = 10 + 4k exactly linear, per-gate max 3, dmax 5, T3 14 constant at N + M 285-1202, two engines agree).
- Open (not started): (a) a fixed-family test on the DHIB line (DHIB26_2804, Deep_3 24, dmax 6 — the deepest known); (b) a family where
  ONE gate's deep flips grow (CL(k) grows only the number of gates; per-gate max stays 3) — that is L-RED 66's one-gate target.
- Things only I know: second engines need worktrees/archives in the scratchpad (lost on a new container): L-NEW depth206 = worktree
  claude/l-new (env LNEW, box39); L-SI scc99 = worktree claude/l-si f65e0fb9 (LSI) + git archive l-new fcba92fc experiments/new
  experiments/si/si.py experiments/harness (LSIROOT / LNEW); L-SI cross100 = worktree claude/l-si 23d39400 (LSI100) + worktree claude/l-red
  59daaef2 (RED) + that archive (LNEW), run with python3 -I. depth206 caps loud depth at «L8». gen36.levvecs enumerates 2^(N−1) (OOM ~N 30).
  bin/ dirs (box36/bin(+k), box37/bin, box38/bin) and out/.lock_* need .git/info/exclude lines in a fresh clone. own34 costs ~10 s per run
  at N + M 300; ties40 needs ulimit and its caps. Slips: none known beyond those listed in earlier handovers.

## RESUME POINT -- successor 18, 2026-11-12 ~11:xxZ by date -u. BOX 41 DONE (Lead 10:23Z); NOTHING RUNNING.
- BOX 41 record: experiments/comp/box41/README.md (all DATA). Item 1: deep41 = L-SI box 100 cross100 on 26/26; DEEP3 proper (internal,
  after t0) = 38, MW's deep all external. Item 2: Deep_3 climbs: 2 (N + M 160), 10 (285, from C6G8 grown); 11/11 bests agree with
  cross100. Item 3: size-floor (C_max >= 40) SCC-LIN: 0.427 (68 movers). Item 4: envelope exponent 2.45 +- 0.46 across 5 families:
  NOT identified; next = one family at 3+ sizes.
- Things only I know: cross100 needs env RED (worktree l-red 59daaef2) and LNEW (archive l-new fcba92fc) and runs with python -I.

## RESUME POINT -- successor 18, 2026-11-12 ~09:3xZ by date -u. BOX 40 DONE (Lead 08:42Z); NOTHING RUNNING.
- BOX 40 record: experiments/comp/box40/README.md (all DATA). Item 1: scc40 (box 99 loc/M_C census on own34) = L-SI inst99.out on 26/26,
  control = L-RED's (10/14). Item 2: ties on 2/26 frozen, 0/600 random k = 1, 90/400 of L-RED's replayed set; Hmax > n5v T3 on 7/400
  (by <= 3, all k > 1); HM <= −1 on every path. Item 3: SCC-LIN climbs (bands 150, 300): best loc/M_C 0.8 (C98 core), MWR -> 0.5 by
  fragmenting C_max; 29/29 bests agree with scc99; no alert.
- Things only I know: gen36.levvecs(N) enumerates 2^(N−1) vectors (OOM at N ~ 30): draw levels by fair bits instead. own34 at N + M 290:
  ~8-12 s per run. scc99 needs ROOT = git archive of l-new fcba92fc (see box40 README). ties40 caps: SCAP/PRODCAP/PCAP env.

## RESUME POINT -- successor 18 (L-COMP 18, Opus 5.5; session_01V5yGRVyip8PwDCTvydpDg1), 2026-11-12 ~07:5xZ by date -u. BOX 39 DONE; NOTHING RUNNING.
- BOX 39 record: experiments/comp/box39/README.md (all DATA). Item 1: depth39 (Q, Q_(>c), loud-depth histogram on ideal37, from box 206
  text) = L-NEW / L-RED on 27 genomes, 0 mismatches (CW32 T 225, D_mov 202, Q_(>1) 29). Item 2: Q_(>1) band maxima 10 (N + M 303) and
  18 (612), both CW(n) + a few deep steps; 12/12 bests agree with L-NEW depth206 (capped at L8). Q_(>2) at 300: no gain (9).
  Item 3: envelope exponent 0.49 +- 0.11 (4 sizes) but NOT identified (unequal effort, CW-dominated); nothing above linear.
- Things only I know: depth206 lumps loud depths >= 8 into «L8» (its l. 72): compare capped. band39.sh needs env LNEW (worktree of
  claude/l-new, used 8d6c363b); CW(n) at any n: L-RED r229/genmw229.py WTGT=R n + r231/carry231.py (worktree of claude/l-red). bin/
  rebuilt this session (box36/bin(+k), box37/bin, box38/bin; exclude lines re-added). ideal37 at N + M 600: ~20 s per run.

## HANDOVER -- successor 17 (L-COMP 17, Opus 5.5) PARKS 2026-11-12 (date -u in the park commit) after BOX 38. NOTHING RUNNING.
- BOX 38 record: experiments/comp/box38/README.md (all DATA). Lead 02:43Z: «When both are done, write the BOX 38 record and park».
  Item 2 (U(G) axis, for L-SI 50 BOX 98; reported to the Lead 02:42Z, logged at 61d04877): U(G) per P-N5-ASC §6 l. 179 = R121 (g);
  Ttot = T3 + 3 and F = 1 on 376/376 two-engine runs (mine full38 + L-NEW n5v); max T3 flat in U: exhaustive N + M <= 8 (118M
  genomes), sampled N + M 12-48, structured ladders to N + M 486 (U = 0 keeps >= 96% of T3; gen37: 6n + 7 -> 6n + 4), U-constrained
  T3 climbs: band 150: 33 / 32 / 34 (U <= 0 / <= 2 / none), band 290: 60 / 60 / 60. CHAIN3's bound at U = 0 alone is 10^13-10^18.
  Item 1 (band [580, 620], Lead budget 2 streams x 1 x 200): D_mov 83 / 82 at N + M 582 (ideal37 = fast37 on 7/7 bests); on BOX 37's
  linear envelope (predicts 84.4). Nothing above linear.
  Preempt (Lead 04:03Z): BLKX23_n48 reproduced exactly on ideal37 (88ac6b07).
- Things only I know: bin/ dirs (box36/bin/k, box37/bin, box38/bin) and out/.lock_* are in .git/info/exclude (re-add in a fresh
  clone); lnew38.py needs env LNEW = a worktree of claude/l-new (git worktree add --detach <dir> origin/claude/l-new; used 1478886e).
  Tasks die at 2 h and on container restarts (~every 1-2 h here): every BOX 38 job resumes by re-running its command (sweep38 per
  block, samp38 .ck, ladders per .out, climb38 OUT.state, band38.sh has a flock). samp38's composition sampler: rejection for the
  first five pairs, stars-and-bars after (the rejection sampler hangs at N = M = 8).
- Slips (disclosed to the Lead): one commit made while a push ran (88ac6b07; push.sh pushed only the verified SHA); one message
  timestamp written without date -u (04:12Z for 04:04Z).
- Open (not started): larger U-constrained T3 climbs (bands > 300) if L-SI 50 asks; item 1 beyond one band (Lead: single point only).

## HANDOVER -- successor 16 (L-COMP 16, Opus 5.5) PARKS 2026-11-11 (date -u in the park commit) after BOX 37. NOTHING RUNNING.
- BOX 37 record: experiments/comp/box37/README.md (item 1 gen37 family; (2) mover class height). All DATA; nothing above linear.
  Item 1: record gate = MWR's Q, not qz; gen37(n) = MWR(n) + 2 br moves, exactly linear on fast36 + own36 (n 2-23).
  (2): D_mov (box 204) on MY IDEAL-CYC engine ideal37 = L-NEW's on 41 genomes (0 mismatches); fast37 proxy; climbs C500s1, C700s1,
  C500s2 (score D_mov/(N + M), k = 1): 76 frozen bests, 38 sizes 244-493, p 0.944 +- 0.027, slope 0.139, max ratio 0.160.
- Things only I know: the container survived the 11-09 -> 11-11 stall (bin/ intact); background tasks die at 2 h -- climb37 resumes from
  OUT.state (restart, step, current genome). fast37 needs bin/ (build line in fast37.py); .git/info/exclude needs box36/bin/ and
  box37/bin/ in a fresh clone. ideal37 costs 16 s per genome at N + M 493, ~270 s for own36 at 696.
- Open (not started): a climb whose score does not divide by size (e.g. D_mov at a fixed N + M band) to reach N + M > 500.

## RESUME POINT -- successor 16 (L-COMP 16, Opus 5.5), 2026-11-09 08:55Z by date -u (GO Lead 08:25Z: BOX 37 items 1-3)
- BOX 37 item 1 DONE (experiments/comp/box37, README = the record). All DATA, scope N5'-xi from S3 on Gamma3 to the first fallback, [E-LEV].
  - Record gate (82, 0) of the C300 bests = MWR8_2's Q (race letter y), NOT qz (Lead question): Q 0 flips in MWR8_2; qz stays 17 along
    the chain while Q climbs 20 -> 34. The family is MWR plus INERT decoration: ablation leaves a core of N + M 261 (MWR8_2's size).
  - gen37(n) = MWR(n) + 2 br moves ((R, qz-option) and (a_m, 0) raised to just above (a_1, 1)). fast36 n 2-23 and own36 13 sizes agree;
    exact: Qf = maxflip = 4n + 2, C = 2n + 1, T3 = 6n + 7, N + M = 29n + 29, lamch 0, k 1. LINEAR (22 distinct sizes, zero residual).
  - Byte-for-byte reproduction of the bests: not possible (inert edits); gen37(8) reproduces their counters at 261 < 289/297. B400 r34
    is a variant core (qz bp/extra option + a37 exit removed instead of R's raise; same counts).
- Item 2 (penalised climb) NOT RUN: item 1 succeeded, so its condition («if the family is not extractable») does not hold.
- Item 3: no point above linear (nothing to send).
- Things only I know: fast36.py's width list stops at W 48 (n <= 3072 game vertices); meas37.one96 uses bin/k/fast36_w96 (build:
  gcc -O2 -DW=96 -o bin/k/fast36_w96 fast36.c). own36 at n 23 takes 270 s. bin/ needs a .git/info/exclude line in a fresh clone.

## HANDOVER -- successor 15 (L-COMP 15, Opus 5.5) PARKS 2026-11-09 (date -u in the park commit) after BOX 36 (Lead 05:18Z / 06:04Z: climb, fit, park)
### Where things are (all DATA; scope: N5'-xi from S3 on Gamma3 up to the first fallback, [E-LEV]; unit genome unless stated)
- Tools in experiments/comp/box36 (README = this section):
  own36.py (per-gate census on own34; own34.run keeps sigs/taus; FACE = (ch_pe, lam_pe, ch_pB, lam_pB); kfvs brute force);
  fast36.c (C port of own34 + census + C counter + face counters; build: gcc -O2 -DW=<1|8|16|48> -o bin/<dir>/fast36_w<w> fast36.c,
  bin/ is NOT committed (.git/info/exclude): bin = flips-only build used by the sweeps, bin/next = + C counter, bin/k = + faces; all
  three are the same source at successive edits, the final source builds all of them); fast36.py (glue: one(), run_block());
  gen36.py (box 33/35 genome space, any N), sweep36.py (exhaustive, resumable per block; ALLK=1 for C), table36.py, ctable36.py,
  val36.py / blockcmp36.py / cval36.py (validation), climb36.py (k = 1 climb), fit36.py (3-point fit).
- VALIDATION: fast36 vs own36 / asc197 / k1srch202 / fvs202 on 4,500 genomes (A 2,000, B1 2,000, B2 500): 0 mismatches; control
  FAST36_CTRL=1 fires 72/100; block stats = Python on 57,024 genomes; C counter 0 mismatches vs own34 on 1,075 (71 frontier, MWR).
- (b) MWR4/8/16_2 third engine: = L-RED R229 on every column (out/mwr_own36.out).
- (c) EXHAUSTIVE k >= 1, N + M <= 8 (N1M1-5, N2M2-4, N3M3-4, N4M4; out/table36_part{1,2}.jsonl, argmax out/argmax + SHA1SUMS):
  max flips/(lamch+1) = 1 wherever a gate flips (0 at N = 1 and N = M); K1-FLIP(2) violations 0; maxflip 2 (N2M4, lamch >= 1).
- Item 3 EXACT C (ALLK, every genome): (1,4) 0, (1,5) 0 [73.7M], (2,3) 1, (3,3) 0 (= BOX 35), (3,4) 1 [56.6M] (out/csweep). C >= 2
  below N + M 33 stays OPEN outside these sets ((2,4) has none by BOX 33's exhaustive A <= 2, since C >= 2 needs A >= 3; (2,5) not run, Lead no-go).
- CLIMB (k = 1, score (max_g flips/(lamch+1), C, T3); L-SI box 93 (d) bound checked on every eval: LSIFAIL 0):
  A200 (cap 200, 8 restarts x 3000, stopped by me for the 2-job limit): 16 at N + M 200 (BEST_A200_r16_C8_9b06186f).
  C300 (cap 300, 4 x 800): 34 at 289 (BEST_C300_r34_C17_30d4ea76). B400 (cap 400, 6 x 800): 34 at 297 (BEST_B400_r34_C17_1694d52f).
  r32 (275, a13d9661, routed by the Lead to L-RED 63 / L-NEW 68) and both r34: fast36 = own36 = L-NEW gflip202 (out/climb/gflip202_*.out).
  All bests: gate flips with lamch 0, flips ~ 2C, L-SI bound flips <= 2 min ch_f + 1 tight or near-tight.
  FIT (fit36.py, out/climb/fit36.out): MWR exactly linear (2n + 1, p 1.06); climb points p 1.97 +- 0.12 from 3 points of which two
  are at the same size and the cap-400 climb never used its room: NOT identified. Reading: the climb reaches MWR(16)'s per-gate count
  (34 vs 33) at N + M ~290 instead of 493; growth law OPEN.
- B400 final (6 restarts, 4,121 evals): only restarts 1 and 2 left 17 (to 34 and 32); 4 of 6 stayed at MWR8_2's 17. C300 restart 0
  climbed 17 -> 20 -> 24 -> 28 -> 32 -> 34 while N + M rose 263 -> 281 -> 281 -> 281 -> 286 -> 289 (+2 C per accepted edit at near-constant
  size). NOTHING RUNS at park.
### Things only I know (successor 15)
- fast36 speed: ~10-20 us per small genome; MWR4_2 0.09 s, MWR8_2 1.5 s (n 1,333; W 48 build): the cap-400 climb is eval-bound.
- Monitors on tail -F of the climb logs delivered nothing here; poll the logs at wake-ups instead.
- Not checked: whether gate (82, 0) of the r32/r34 bests descends from MWR8_2's qz (62) (ADD-mover shifts indices); open.
- verify.sh takes ~20 min while two heavy jobs run; never commit during a push (hook nags; ignore until the push ends).

## HANDOVER -- successor 14 (L-COMP 14, Opus 5.5) PARKS 2026-11-09 03:29Z by date -u (Lead 02:14Z: BOX 35 last before park). NOTHING RUNNING.
### Where things are (all DATA; scope of every number: N5'-xi from S3 on Gamma3 up to the first fallback, unit = genome unless stated)
- Engines: own34.py (experiments/comp/box34) = MY independent engine (Gamma3 from R104 + P-N5-REACH §3 text; n5b SPEC + [N5XI] tie rule;
  counters T3, maxalt (fixed), C, maxm, maxP, RA depth, fan-in/out). Second engines: L-NEW asc197 @ b61c2029 (BOX 33 counter) and @ f98e93ee
  (fixed maxalt) via ref34.py/cmp34.py (compare T3 + maxalt + game build); for C: L-NEW pair198.py @ fcba92fc. maxm has NO second counter.
  Worktrees are local in the scratchpad: recreate with `git fetch origin claude/l-new; git worktree add --detach <dir> <sha>`.
- BOX 33/34 item 1: N2M4 [E-LEV] and --noelev both COMPLETE: 14,929,920 genomes, A_max 2 on 30,432, T3_max 2 (identical). Full BOX 33 table
  two-engine (own34 agrees on all argmax files + 2,000 random per (N, M)).
- Item 2: N3 sample 20,000 per M 3..7 (seeds 3433-3437; out/n3_*): A_max 2 (M >= 5), T3_max 5 (M 7).
- Item 3: own34 vs asc197: 0 mismatches on ~228,000 random runs, 6 argmax, 64 pinned (58 live, 6 hfam towers vs L-NEW's recorded values).
- (c) FW family (L-SI 47, 7 files): own34 = L-SI's table on every column (third engine).
- (b) climb34 N 3-4, M 8-10: best C 1 (no repeated top) everywhere.
- (b') INVERSE FRONTIER (shrink34 greedy deletion; best34.py): upper bounds min N + M for C >= 2..12: 33, 45, 50, 63, 75, 105, 112, 122, 164,
  172, 176; maxm 2/3/4: 50/106/121. 13 frontier genomes two-engine (asc197 T3 + maxalt; pair198 maxC). out/frontier/SHA1SUMS.
- BOX 35 (2) EXACT «C >= 2 below N + M 33» (exact35.py), scope of the «none found»:
  (i) all genomes of (N, M) in {(1,1..4), (2,2..4)} (BOX 33 exhaustive A_max <= 2; C >= 2 implies A >= 3); (ii) all 73,728 genomes of
  (3, 3): C 0; (iii) every genome within <= 3 deletions (exact35 nbr moves) of the frontier genomes C2_NM33 x2, NM35, NM37 x2, NM38, and
  <= 2 deletions of NM40 (depth 3 stopped: ~10^6 genomes): no genome with C >= 2 and N + M < 33 (hits only at 35, 36).
  NOT covered: any other genome with N + M <= 32 (e.g. (1,5), (3,4), (2,5) exhaustive are 10^7-10^9 genomes). So C >= 2 below 33 is OPEN.
- BOX 35 (BOX 32 replay, Lead 02:54Z): rfix, W1 test, OSC decodes realize (box32/val/replay35.txt): no correction.
- BOX 35 (1) (L-LOWER 12 SAT replay + N5 end to end): NOT started (no model routed before park). Tools: box32/mutcheck.py (fenc + sim6 +
  replay30 + enc32 checker; fenc binary: gcc -O2 -o box32/bin/fenc box31/l-lower/l9/fenc.c), box29 pipeline for Gamma3 end to end.
### Things only I know (successor 14)
- cmp34 compares T3 + maxalt only; asc197 > 10 min on hfam towers; own34 ~0.5 s at N + M 100, minutes at n ~ 5,000.
- Deletion neighbourhoods explode with mover count of mover-deletion choices (NM40: 21k at depth 2).
- I once launched a push with «&» (killed before it pushed; disclosed). Always run push.sh as a tracked background task.

## RESUME POINT -- successor 14 (superseded by the handover above)
- Engines (scratchpad worktrees, local): lnew = claude/l-new b61c2029 (BOX 33 engine), lnewfix = f98e93ee (fixed maxalt), lnew198 = fcba92fc
  (pair198.py, L-NEW's maxC). Recreate: `git fetch origin claude/l-new; git worktree add --detach <dir> <sha>`.
- DONE (all pushed by 8db05457 / ce85a7cc / this push): item 1 N2M4 elev + noelev complete (14,929,920; A 2 on 30,432, T3 2; equal);
  item 2 N3 sample (20,000 per M 3-7); item 3 own34.py = my engine, 0 mismatches vs asc197 (both commits) on ~228,000 random runs, 6 argmax,
  76 pinned (6 towers vs record); (c) FW 7/7 rows = L-SI 47; (a) 64 pinned; (b) climb N 3-4 M 8-10: C 1 everywhere.
- (b') FRONTIER (Lead 23:34Z; shrink34.py greedy deletion, frontier34.sh chains, best34.py table; out/frontier/ + SHA1SUMS; logs in
  out/frontier/log): min N + M (upper bounds) C2 33, C3 45, C4 50, C5 63, C6 75, C7 105, C8 112, C9 122, C10 164, C11 172, C12 176;
  maxm 2 50, 3 106, 4 121. Final 13 genomes: asc197 (T3, maxalt) + pair198 (maxC) = own34 (out/frontier_final_2eng.txt). maxm: own34 only.
- BOX 32 SAT replay (Lead 02:54Z, L-LOWER 12: enc32 --freerank lacks transitivity among options sharing an insertion slot): rfix,
  W1 test (enc32 --freerank, affected) and OSC K4 T10 decodes re-replayed (experiments/comp/box32/val/replay35.txt): all realize their
  targets (fenc + sim6 + replay30 + enc32 --fix all; OSC by clampcheck). No artefact, NO CORRECTION to BOX 32's SAT lines.
- Things only I know: asc197 > 10 min on hfam towers (H6C-H8C); own34 ~0.5 s per N + M 100 genome, minutes on n ~ 5,000. cmp34 compares
  T3 + maxalt only; for C use pair198 (ROOT=<lnew198> python3 -I .../box198/pair198.py G.json). Never launch push with «&» (slip 23:1xZ).

## HANDOVER -- successor 13 (L-COMP 13, Opus 5.5) PARKS 2026-11-08 16:03Z by date -u (Lead 14:39Z park OK; NOTHING RUNNING)
### BOX 33 (Lead 14:16Z): exact small-size maxima of A (ALT-EQUIV) and T3 -- tool experiments/comp/box33/enum33.py
- ENGINE = L-NEW's asc197.run (claude/l-new b61c2029: gamma3.build box 189, n5v.step mode xi box 190, S3 start; T3 = iterations up to the
  first fallback, as asc197 counts). NOT an independent engine. The cross-check with my own N5'-xi engine (n5b/n5v mode xi) is OPEN.
- Genome space = eg195.gen schema, ALL genomes of (N, M), no symmetry reduction (levels, option split >= 1 per mover, xt in {-1} + movers,
  gate perm, br perm, bp, start). --noelev = Gamma3 e-priorities by gate only (patch verified: e-priority order flips on a test genome).
- A = 0 below says ONLY that at these tiny sizes no tops sequence has two alternating letters; it says nothing about larger N, M.
- Results (unit = genome; set = all genomes of (N, M) unless marked; scope = N5'-xi from S3 on Gamma3 up to the first fallback):
  | N, M | genomes | A_max [E-LEV] | T3_max [E-LEV] | A_max no E-LEV | T3_max no E-LEV |
  | --- | --- | --- | --- | --- | --- |
  | 1, 1 | 4 | 0 | 0 | 0 | 0 |
  | 1, 2 | 128 | 0 | 1 | 0 | 1 |
  | 1, 3 | 6,912 | 0 | 2 | 0 | 2 |
  | 1, 4 | 589,824 | 0 | 3 | 0 | 3 |
  | 2, 2 | 288 | 0 | 0 | 0 | 0 |
  | 2, 3 | 62,208 | 0 | 1 | 0 | 1 |
  | 2, 4 | 10.35M of ~14.9M (PARTIAL: shard 0 5,260,000, shard 1 5,090,000) | 2 (30,432 genomes with A = 2) | 2 | not run | not run |
  Argmax files (out/): ARGMAX_T3_N1M4.json 58b46be4, ARGMAX_T3_N2M3.json 0d459ac3, ARGMAX_A_N2M4_s0.json d0a2b91a, ARGMAX_A_N2M4_s1.json
  2f94da6b (both A = 2: lev (0,1), mover 0 one exit option, mover 1 three options with xt -1/1).
- RESUME (successor): `git worktree add --detach <dir> b61c2029` (any checkout of claude/l-new at b61c2029), then in experiments/comp/box33:
    LNEW=<dir> timeout 5100 nice python3 enum33.py 2 4 0/2 out/N2M4_s0.txt     (resumes from out/N2M4_s0.txt.ck, committed)
    LNEW=<dir> timeout 5100 nice python3 enum33.py 2 4 1/2 out/N2M4_s1.txt     (from out/N2M4_s1.txt.ck)
  each shard needs ~25-30 more min; then the same two lines with --noelev and new OUT names; then N = 3 by sample:
    LNEW=<dir> nice python3 enum33.py 3 <M> 0/1 out/N3M<M>_sample.txt --sample <S> --seed <R>   (state S, R as the scope).
  The .ck files are gitignored (out/*.ck) except the committed N2M4 ones: add new ones with `git add -f` before parking.
- Other work for the successor: the independent-engine cross-check of asc197's T3/maxalt on a sample (Lead 14:16Z).
### BOX 32 (exact CNF method) -- see RESUME POINT below; all jobs stopped; every verdict reported to the Lead.

## RESUME POINT -- successor 13 (L-COMP 13, Opus 5.5), updated 2026-11-08 10:29Z by date -u (GO 08:12Z; BOX 32)
### BOX 32 = exact CNF method for «a d 32 genome whose run realizes core8_HIT7 exactly» (experiments/comp/box32/, README in this section)
- Encoder enc32.py (own code from R104 rules; REALIZES = core rows equal at t 0..T, a change at every t < T, fixed point at T).
  Free: rank order (tournament, or --lazy/--lazy2 CEGAR, or --thresh 7-bit), signs, helper gate bits, helper starts, helper states.
  Fixed: wiring (W0) except --freeopts (one owner, acyclic candidates) / gadget.py cand lists; core gates; core start.
  Options: --fix ranks[,signs,gates,starts|all], --freerank (unary insertion of chosen options into the fixed order), --only X
  (keep only these core movers' constraints = sub-problem), --prefix N (rows 0..N, no fixed point), --relax (helpers free per step;
  sound relaxation), SKIPCORE env (diagnostics). Clauses stream into the solver (sink); --cnf writes DIMACS.
- Validation (val/): checker mode accepts HIT7 on its own 7-level target; 54 mutants, 0 mismatches fenc / sim6 / enc32 (30 rejected,
  24 realize), replay30 T/F equal (mutcheck_hit7*.out). Ranks-fixed free solve on HIT7 SAT 61 s, decode replays exactly (rfix_hit7*).
  W1 test (26,27 rewired + insertion ranks) SAT, decode realizes (w1test_hit7_dec.txt).
- FINDING: free ranks out of reach: HIT7 known-SAT not solved in 38 min (full), 30 min (lazy), 7 min/round (lazy2), 30 min (thresh).
- R-tier verdicts (all DRUP VERIFIED with Glucose proof + box27 drup.c; CNF/proofs in /home/user/pf32, local only):
  (i) seed W0-R UNSAT (885 lemmas), earliest prefix t 5, needs movers 11-15; (ii) C4 W0-R UNSAT (top-level), prefix t 3;
  (iii) F6 on C4 (only 13's constraints, f6 rewired over {-1, 2, 42, 49} only, insertion ranks) UNSAT (711 lemmas), prefix t 11.
- RUNNING at 10:3xZ: F6 W1 on C5 final (l-lower bb6a95bd, _solved b0997bc7; f6 cand 59) = w1/F6_C5f.out (no answer at 30 min).
- NEXT: gadget.py (c) on the seed base ALONE (OOM when run with another 40M build): fresh helpers 56-63 rewired, inputs pairs 0-5 movers
  2,3,4,5,7,8,9,10,11, f6 extras 11,18,19; SAT -> clampcheck.py (independent clamped replay) + Lead at once (goes to L-LOWER 10).
  Then (a): wider insertion ranks for the F6 test. MEMORY: one ~40M-clause job at a time (7 GB RSS each; 15 GB box).
- Lead rulings this box: 08:12Z go + W0 first, DRUP every UNSAT, ≤ 2 heavy jobs ≤ 90 min; 08:44Z plan OK, read l-lower directly;
  09:28Z R tiers OK, thresh retry OK; 09:49Z (c) first, (a) second, SAT in (c) to L-LOWER via Lead; 09:50Z C5-final W1-f6-R first.
### METHOD FINDING (DATA, timings; CaDiCaL 1.9.5 via pysat, 4 cores, one job each)
| instance | free parameters | clauses | verdict / time |
| --- | --- | --- | --- |
| HIT7 d 28 checker (all fixed) | none | 14.0M | SAT, build 22 s + solve < 1 s |
| HIT7 d 28 ranks fixed | signs, gates, starts, helper states | 14.9M | SAT 61 s (decode replays) |
| HIT7 d 28 ranks free, full order | + ranks | 25.3M | no answer 38 min |
| HIT7 d 28 ranks free, lazy / lazy2 / thresh | + ranks | 5.4M / - / 21.1M | no answer 30 min / 7 min per round / 30 min |
| seed d 32 W0-R | signs, gates, starts, states | 21.6M | UNSAT 19 s (drup 885 lemmas) |
| C4 / C10 W0-R | same | 39.3M / 23.2M | UNSAT 0 s (top-level) |
| F6 on C4 (f6 rewired over 3, insertion ranks) | + 2 options | 37.9M | UNSAT 5 s (drup 711 lemmas) |
| F6 on C5 final (f6 over 59) | + 2 options | 42.5M | no answer 58 min |
| gadget (c) seed (8 movers, insertion ranks 18 options) | | 47.4M | no answer 36 min |
| OSC K 4 T0 10 (free wiring + free ranks, 32 options) | all | 0.82M | SAT 408 s (clamp replay OK) |
| OSC K 8 T0 20 (40 options) | all | 3.19M | no answer 89 min |
Reading: fixed-rank questions decide in seconds (UNSATs often by unit propagation); free ranks (tournament) or wide insertion ranks
make CaDiCaL stall already at a few million clauses. Use exact SAT for fixed-rank / narrow-insertion checks; free ranks only at tiny size.
### Things only I know (successor 13)
- In C4 every mover but 2, 42, 49 reaches 13; in C5 final pairs 0-5 read helpers 56-63 (only 2, 5, 7 admissible gadget inputs).
- /usr/bin/time is not installed; dimproof.py (box27) streams Glucose's proof file; drup.c on 280 MB proofs takes ~35 s.
- A background Bash call that times out at 600 s is auto-stopped after 30 min: launch long jobs with run_in_background from the start.


## HANDOVER -- successor 12 (L-COMP 12, Opus 5.5) PARKS 2026-11-08 07:1xZ by date -u (Lead 05:59Z park order; ~450k context)
### STATE AT PARK: ALL JOBS STOPPED (L7br, L7cr, freezer31, commit_loop, diskguard, monitors). Nothing runs. Everything is DATA.
### HEADLINE: box 31 (eight capped levels, cap F(7) = 510, d 32) -- NO HIT; every scoring order plateaued (table below).
Counters: unit = one rclimb31 run of 2e7 proposals (~15 min); set = the lane; scope = rclimb31 LJ=7 at d 32, from HIT7 + 4 TOP-ADD
(out/seed_HIT7_d32.txt sha1 ad9a39d4: npaths 8, n1 218, sv 105, T 299, F(7) 190). npaths = npaths into pair 7 (L7a/L7b: from q6 =
roles(6)[1]; others: LJNPMAX max over 12, 13); n1 = length-1 7-windows; sv = slack violations j 4+5 at H 8; caps 7 in every file.
| lane | settings (all: LJ 7, LJGATE 190, LJGUARD 20:17,34:22, FIX 20,34, NMIN 2) | ~units | final frozen best (box31/out/) | npaths | n1 | sv | T |
| L7a | FB 0, NMAX 4, anneal .15, RC order | 14 | L7_FRZ_K7099283200044_L7a.txt e7b254bb | 7 | 168 | - | 445 |
| L7b | FB 0, NMAX 4, anneal .15, RC order | 14 | L7_FRZ_PREROOM_L7b.txt 5168b927 | 6 | 174 | - | 466 |
| L7d | FB 12 (FB 12 + LJSLACK 8 + LJNPMAX from 04:2xZ) | 13 | L7_FRZ_K70929298210041_L7d.txt 92c1f661 | 7 | 179 | 70 | 410 |
| L7c -> L7cr | FB 8 + LJSLACK 8 + LJNPMAX + LJORDER room (from 04:57Z) | 10+10 | L7_FRZ_FINAL_L7cr.txt 7562f645 | 7 | 190 | 92 | 423 |
| L7br | seed, FB 0, NMAX 8, anneal .5, LJSLACK 8 + LJNPMAX + room | 8 | L7_FRZ_FINAL_L7br.txt 741afe4c | 7 | 192 | 79 | 434 |
Bests over all lanes: npaths 6 (L7b, first 02:29:49Z), n1 168 (L7a), sv 70 (L7d), T 466 (L7b), F(7) 206 (L7br). Cap needs T >= 510,
n1 = 0, sv = 0 (L-LOWER 9). Reading (mine): random 1-8-edit proposals cannot re-time pairs 0-5 without breaking a lower cap.
### OTHER RESULTS (DATA)
- Item 2: L-RED n5v (spec) on HIT7's Γ3 (box29/hit7/HIT7_d28_F254_g3.pg sha1 8a360485): 302 iterations, 1 fallback = n5b's 302 = L + 3;
  regions == Oink zlk (--verify OK) == n5b; harness verify.py OK (box31/n5v/check_n5v.out). COMPLETE.
- Phase 2 (fix q6 = 12's options to level 9): one edit 4/4 break level 0 (12 is upstream of movers 0-3); two edits + short climbs
  (12 runs, 2e6 proposals): caps <= 2; LJNOREAD reaches nr = 0 in 6/6 but no caps (phase2_test.out, phase2b_sum.out). NEGATIVE.
- Counters: slack j 4/5/6 on the seed = 15/90/217 = L-LOWER slack.py; 217 (slack j 6) != 218 (n1_7) are different counters.
- fenc (L-LOWER 9, box31/l-lower/l9/fenc.c) = sim6 = replay30 on every genome checked; never use l5/fev.c at d >= 32 (overflow).
### RELAUNCH (only if the Lead asks; all lines exist in box31/relaunch31.sh, ended lanes commented)
1. New container: scripts/setup_oink.sh; .git/info/exclude lines as in the resume point below; box31/bin is rebuilt by relaunch31.sh
   (fenc: gcc -O2 -o box31/bin/fenc box31/l-lower/l9/fenc.c).
2. Resume points: out/L7br.unit = 9, out/L7cr.unit = 11 (logged at park; .unit files are local: re-write them in a new container).
3. Exact lane lines (from experiments/comp/box31, RCLIMB=$PWD/bin/rclimb31, via relaunch31.sh's upa):
   ENVX="LANEANNEAL=0.5 LJ=7 LJGATE=190 LJGUARD=20:17,34:22 FIX=20,34 NMIN=2 NMAX=8 FROZENBELOW=0 LJSLACK=8 LJNPMAX=1 LJORDER=room" upa L7br L7br out/seed_HIT7_d32.txt 550000 6 5 7
   ENVX="LANEANNEAL=0.15 LJ=7 LJGATE=190 LJGUARD=20:17,34:22 FIX=20,34 NMIN=2 NMAX=4 FROZENBELOW=8 LJSLACK=8 LJNPMAX=1 LJORDER=room" upa L7cr L7cr out/L7_FRZ_PREROOM_L7c.txt 540000 6 5 7
   (lane31.sh starts from out/<lane>_best.txt when it exists, else from the seed file.) Then upf (freezer31), box28/commit_loop via
   box28/relaunch_all.sh (it also runs relaunch31.sh; idempotent).
4. Code: rclimb31.c sha1 dcbb3b44 (options LJ, LJGATE, LJGUARD, LJSLACK, LJSLACKJ, LJNPMAX, LJNOREAD, LJORDER=room); references ref_lj.py
   310c4f91 / check_lj.py 83aca26c / check_nr.py 4d83108b; all checks 0 mismatches (check_lj_J7*.out, check_nr.out).
### NEXT (my proposal; the Lead decides): no more blind climbing at level 7; support L-LOWER 9's by-hand level-8 design with replays
(sim6 + fenc + replay30) and the N5 end-to-end check (box29 pipeline; n5b + n5v + Oink) on any candidate.

## RESUME POINT -- successor 12 (L-COMP 12, Opus 5.5), updated 2026-11-08 03:4xZ by date -u (GO 02:14Z) -- HANDOVER-READY
### RELAUNCH (container restarts every ~40 min; a new container needs steps 1-3)
1. New container only: scripts/setup_oink.sh (verify.sh needs Oink). Re-add to .git/info/exclude (local only; else commit_loop commits
   binaries): experiments/comp/box28/{frup,cubes/,log/*.out,log/*.run}; experiments/comp/box30/{bin/,out/.pid_*,out/*.unit,out/*_u[0-9]*.txt,
   out/*_u[0-9]*.run,out/.zseen}; experiments/comp/box31/{bin/,out/.pid_*,out/*.unit,out/*_u[0-9]*.txt,out/*_u[0-9]*.run,out/*.nohup,mut_check*/}.
2. Lanes L7a-d: if out/<lane>_u<k>.txt of the unit in flight exists and scores above out/<lane>_best.txt, copy it to _best (as at 02:25Z:
   partial unit best kept; log a line «INTERRUPTED by container restart» in out/<lane>.log). Write out/<lane>.unit = last unit in
   out/<lane>.log + 1 (box31/out/, local files).
3. experiments/comp/box28/relaunch_all.sh (idempotent): diskguard, commit_loop, box30/relaunch30.sh (all lines stopped), box31/relaunch31.sh
   (L7a-d + freezer31; builds bin/rclimb31 if missing; fenc for checks: gcc -O2 -o box31/bin/fenc box31/l-lower/l9/fenc.c). Verify each
   PID file names a live process (ps -o args= -p $(cat out/.pid_X)); a just-killed process can still answer kill -0 for a moment.
4. Re-arm the monitor (FROZEN npaths < 6, HITS, dead lanes, commit_loop «push exit»).
### LANES (box31/README.md; rclimb31.c 46c1746c; ref ref_lj.py 53b22e78; checks check_lj*.out, check_nr.out: 0 mismatches)
- Common C = LANEANNEAL 0.15 LJ 7 LJGATE 190 LJGUARD 20:17,34:22 FIX 20,34 NMIN 2 NMAX 4; lane31.sh args 6 5 7; seed out/seed_HIT7_d32.txt.
  L7a FB 0 (500000+), L7b FB 0 (510000+): baseline, unchanged. L7c (now L7cr, below), L7d: relaunch31.sh ALREADY has the Lead-approved switch (02:53Z, 03:43Z):
  L7c = FB 8 + LJSLACK 8 + LJNPMAX 1, L7d = FB 12 + LJSLACK 8 + LJNPMAX 1; it takes effect at their next (re)start (score scale changes;
  freezer31 keeps a per-lane max).
  APPLIED 04:2xZ (no container restart since 02:25Z; L7c/L7d had not improved since 03:24Z/03:11Z; Lead 02:46Z: timing my call, never
  interrupt an improving lane): L7c stopped at unit 9, L7d at unit 8 (partial bests kept if higher; logged), relaunched; env confirmed.
- 04:57Z (Lead 04:57Z, ROOM lane): L7c ENDED; its best frozen as out/L7_FRZ_PREROOM_L7c.txt (sha1 75514342). NEW LANE L7cr = from that
  file, seeds 540000+, C + FROZENBELOW 8 + LJSLACK 8 + LJNPMAX 1 + LJORDER room: order (caps, g, -sv, -n1, -npaths, T, F(7)) = caps*1e18 +
  g*1e17 - sv*1e14 - n1*1e11 - np*1e9 + T*1e4 + F (gate kept right after caps). rclimb31.c sha1 dcbb3b44 (ref_lj.py 310c4f91, check_lj.py
  83aca26c): check_lj_J7_room.out = L7c best + 40 mutants + 34 L7 frozen files, 75 genomes, 0 mismatches; without LJORDER bit-identical.
  New lane name because the room scale differs: lane best and freezer per-lane max stay consistent. Monitor/relaunch use L7cr, not L7c.
- Score options in rclimb31 (all off = the launched score, bit-identical): LJSLACK=H (slack j 4,5 term), LJNOREAD=t:x.. (readers of t),
  LJNPMAX=1 (npaths = max over movers 12, 13, role-free; Lead 03:43Z, because q6 can switch to 13).
- Phase 2 (fix q6's options to level 9): one-edit test (phase2_test.out) and two-edit + short-climb test (b) (phase2b_sum.out): NEGATIVE,
  caps <= 2. Lead 03:43Z: (a) no phase-2 lane for now.
- Next report to the Lead: frozen best with npaths < 6, n1 well down, or T >= 510; a HIT; or ~05:00Z. A HIT -> Lead at once (genome, sha1,
  F, T, rclimb31 + replay30 + sim6 + fenc), then Γ3 end to end (box29 pipeline: replay30 JSON -> l-new norm.py -> writepg.py; n5b run29.py,
  n5v box31/n5v/check_n5v.py, Oink check29.py).
### DONE (DATA): seed re-measured; n5v on HIT7 Γ3 = 302 = n5b, = Oink; slack counts 15/90/217 = L-LOWER slack.py; commit_loop pattern
  '^(/usr/bin/env )?(/bin/|/usr/bin/)?(bash )?(\./)?scripts/push\.sh' (live test below); pushes 12dd20ff, 7c7d104e, beb1deec.
### Things only I know (successor 12)
- fenc (L-LOWER 9) is the exact d <= 64 engine; l5/fev.c overflows at d >= 32 (Lead 02:46Z): never use fev at d 32.
- slack j 6 (217 on the seed) != n1_7 (218): two counters. lj_npaths before LJNPMAX follows q6 = roles(6)[1], which can be 13 or none.
- Movers 0-3 read 12 (upstream(12) ∋ 0..3) in every L7 genome so far: any edit of 12's options breaks level 0.
- commit_loop (box28) RESTARTED 02:2xZ with pattern pgrep -f '^(/usr/bin/env )?(/bin/|/usr/bin/)?(bash )?(\./)?scripts/push\.sh' (Lead 02:20Z),
  footer = my session, box31 added. LIVE TEST (02:2xZ, during my push of 39c09dbf): ps showed 13019 «bash scripts/push.sh» and my tool
  wrapper 13018 «/bin/bash -c ...; scripts/push.sh > log»; old anchored «^bash scripts/push.sh» -> 13019; unanchored «scripts/push.sh» ->
  13018 13019 (wrapper too: the loop would stall); new pattern -> 13019 only. grep -E on strings: matches «bash scripts/push.sh», «bash
  ./scripts/push.sh», «./scripts/push.sh», «/bin/bash ./scripts/push.sh»; no match for the wrapper and for «bash -c until ! pgrep -f bash
  scripts/push.sh». Hand commits: only when that pgrep is empty and commit_loop is asleep (it sleeps 600 s after each round).

## HANDOVER -- successor 11 (L-COMP 11, Opus 5.5) PARKS 2026-11-08 00:5xZ by date -u (~500k context; Lead 00:46Z item 4)
### HEADLINE (DATA, a CANDIDATE tower, not a result): first 7-capped tower in the fleet
- box30/out/L6_HIT7_F254_d28.txt, sha1 6a3b274d3af4d0d8f057f82c8f2919c84b7dd446: d 28, T 299, F(0..6) = 2, 6, 14, 30, 62, 126, 254
  (F 2 6 14 30 62 126 254 190 95 64 48 32 24 33 33 65 32 16 8 4 3 4 3 3 1 0 0 1); npaths(q5, pair 6) 0, n1 0; vs SL41 only core change
  10:0 55 -> 17. Lane D_l6u seed 415003 (L6W score, gate 248, from L6_FRZ_F248). Replays: rclimb30, replay30, sim6 (caps 7), guard_l6
  noreturn ok -- record box30/out/L6_HIT7_F254_d28.replays.txt. Path of bests: 238 (REC238) -> 240 ... 248 (n1 3) -> 250 (n1 2) -> 254.
- End to end (box29/README.md section HIT7): Γ3 .pg sha1 8a360485 (n 850); my n5b SPEC: 302 iterations = L + 3 (L = T = 299), one
  fallback at transition 300, one FL run [0, 299]; Oink zlk --verify OK, regions equal, verify.py OK. n5v (L-RED) NOT run on it.
### STATE AT PARK: ALL JOBS STOPPED (climbs, freezer, commit_loop, diskguard). Nothing runs. Query 2 and xval_d3 are COMPLETE.
### NEXT (Lead 00:46Z item 3, for the successor): 8 capped levels (cap F(7) = 510) at d 32 -- plan, NOT started
1. Seed: L6_HIT7_F254_d28.txt + 4 TOP-ADD (box30/l-lower/lift.py IN 4 OUT; earlier D_d32 seeds were made the same way) -> d 32 (rclimb30
   is 192-bit: no overflow at d 32). Re-measure the lifted seed with rclimb30 + replay30 (+ sim6) before climbing: F(0..6) must stay exact.
2. Score: GUARD levels 0-6 exact, then the n1-style term at level 7 = number of length-1 7-windows (windows of level 7 cut at the flips of
   o(6), as guard_l6.windows(S, O, 7)), then F(7). rclimb30's L6W code is hard-wired to level 6 (O[t][5] cuts, F[6], gate on F[6],
   q5/roles(5), npaths to {12, 13}, FIX 20,34): generalise it to a level J (env L6J=7: cuts at o(J-1), F[J], roles(J-1) movers 2J-2, 2J-1,
   npaths to {2J, 2J+1}) and CHECK the C score against a Python reference (guard_l6.windows(S, O, 7), sim6) on the seed + 20 mutants first.
3. RC-free constraint at level 7: npaths(q6, pair 7) = 0, q6 = the SECOND mover of pair 6 (roles(D, S, O, 6); on HIT7 roles(6) = (13, 12),
   so q6 = 12). Path analogue (my definition, to confirm with the Lead): q5's working path was 10:0 -> 17 (a level-8 mover) -> 22; for
   level 7 keep the HIT7 path FIXED (FIX 20,34) and do NOT fix a new one at first; record which level->=9 mover q6's options reach.
4. Two seed streams per setting, 4 lanes on 4 cores; freezer.sh + watcher as for L6 (HIT = F(0..7) = 2..510). Report settings + code sha1
   to the Lead before launch.
### Relaunch of what existed (if ever needed): box28/relaunch_all.sh -> box30/relaunch30.sh. Every L6 lane line in relaunch30.sh was STOPPED
at park; un-comment only what the Lead asks for. Lane resume points: out/<lane>.log (last unit + 1).

## RESUME POINT -- successor 11 (L-COMP 11, Opus 5.5), updated 2026-11-07 23:3xZ by date -u (handover-ready; GO was 11:02Z)
### RELAUNCH (after a restart or in a new container)
1. New container only: scripts/setup_oink.sh (verify.sh needs Oink); re-add local excludes to .git/info/exclude:
   experiments/comp/box28/frup, box28/cubes/, box28/log/*.out, box28/log/*.run, box30/bin/, box30/out/.pid_*, box30/out/*.unit,
   box30/out/*_u[0-9]*.txt, box30/out/*_u[0-9]*.run, box30/out/.zseen (all under experiments/comp/), else commit_loop commits binaries.
   Write each live lane's out/<lane>.unit = (last unit in out/<lane>.log) + 1 (.unit files are local only).
2. experiments/comp/box28/relaunch_all.sh (idempotent: diskguard, commit_loop, then box30/relaunch30.sh = the climb lanes + freezer).
   Query 2 and xval lines are commented DONE. Kill jobs by PID files only (box30/out/.pid_<lane>, box28/cubes/.pid_<name>); never edit a
   running bash script (sed -i makes a new inode: the running copy keeps the old text; restart it to take effect).
### LIVE (4 climbs on 4 cores, Lead 23:36Z) -- rclimb30.c sha1 9808cd9b (CORRECTED by L-COMP 12, Lead 02:14Z: f7c31685 was the previous version; 9808cd9b adds L6W24) (env L6SCORE/L6W/L6GATE/FIX/FROZENBELOW/FROZENSET/NMIN/NMAX/...)
- Score L6W = (caps, [F(6) >= gate], -npaths(q5, pair 6), -n1, F(6)); n1 = length-1 6-windows (guard_l6.windows); = Python reference
  (L-LOWER guard_l6.py 18e85589 + sim6.py 6953306e at claude/l-lower bca48384; copies only in a scratchpad -- git show them again).
  Guard: options 20 (10:0) -> 17 and 34 (17:0) -> 22 fixed (FIX 20,34). Edits on movers >= 12. HIT = F(0..6) = 2,6,...,254.
- D_l6w (from REC238, gate 238, seeds 400000+), D_l6v (from L6_FRZ_F240, gate 240, 410000+), D_l6u / D_l6u2 (from L6_FRZ_F248, gate 248,
  415000+ / 420000+). freezer.sh copies every new constrained best to out/L6_FRZ_F<F6>_<lane>.txt (+ sha1 line in out/FROZEN.txt).
- Constrained bests (caps 6, npaths 0; DATA, sim6 + guard_l6 + replay30 agree): 238 REC238 (file L6Z_KILL238_d28, n1 8) -> 240/242/244
  (n1 4) -> 246 (n1 3) -> 248 L6_FRZ_F248_D_l6v.txt sha1 ba061180 (n1 3, windows at steps 44, 79, 114; 248 = 254 - 2 n1 exactly).
- Stopped lanes (resume points in out/<lane>.log): B_d32, D_d28, D_d28b, D_l6, D_l6g, D_l6h, D_l6z, D_l6w2.
### DONE this session (all DATA/CERT; details in the Lead messages and the files)
- Query 2 (L-SI frame «T_2(3) >= 13») CERTIFIED: 84-cube complete split (1,024-pattern check), all Glucose UNSAT + drup.c VERIFIED;
  table box28/log/lsi_q2_cert.txt. ONE checker only (frup not run; proofs deleted) -- state this with every mention (Lead 23:36Z).
- xval_d3: frup = drup = P-TR3 on 16/16 cubes (box28/README.md section xval_d3).
- RC-PLATEAU: stays a CONJECTURE (implication; Lead 21:19Z). REC230/REC238 (files L6Z_KILL230/238_d28) refute only «RC-free 6-capped
  genomes stay <= 222». Constrained climb reached 248 (above).
### Things only I know (successor 11)
- A climb's out/<lane>_best.txt changes only at unit END; read live progress in out/<lane>_u<k>.txt; frozen copies are L6*_d28 / L6_FRZ_*.
- push.sh now takes ~30-45 min (trunk merged 006d9071): commit_loop rounds ~45-55 min apart. Hand-commit urgent files by explicit path
  only when pgrep -f "bash scripts/push.sh" is empty (commit_loop sleeps 600 s right after its push).
- MY BUG 17:40Z: q2stop2.sh glob-deleted log/q2/*.chk.tmp of OTHER workers (c0s1p2/p4 drup results lost; re-run). Never glob-delete in a
  shared work dir; delete only files named by the stopped process.
- `setsid nohup X &; echo $!` may record setsid's short-lived parent: re-read with pgrep -f "^/bin/bash ./X".

## FINAL (successor 9, 2026-11-07 05:2xZ by date -u): query 2 handed to L-COMP 10 (finer split); proofs in this scratchpad are not reachable from other sessions.
- At hand-off: query 2 CERTIFIED cubes 1, 2, 3, 5, 6, 7 and sub-cube c4s1 (log/q2_cert/); open: c0s0..c0s3, c4s0, c4s2, c4s3 (restarts every
  ~40 min on 11-07 killed every multi-hour drup check). Lead 05:18Z: park for good; no relaunch. All my jobs stopped.

## HANDOVER -- successor 9 PARKS (session_01V5yGRVtZknivpYHCjzoA9y, ~580k context), 2026-11-07 01:1xZ by date -u
### DONE (all pushed; records in the repo)
- P-TR3 (T^R(3) <= 8, = 8): packet experiments/comp/box27/P-TR3.md (frozen d03d8370, sha1 cab32c0e, 125 l.), fixes entries 1-2
  (P-TR3-fixes.md sha1 38b97e59, 86 l.), lines L-1 / L-2 (11cd9acc) / L-3 (d87bb3f0, = C123 expected). Both referees SIGNED (REFEREE
  24 5a5b94cf, REFEREE-2 28 60e24158); L-3 with the Lead / CHECKER C123. 16/16 d 3 cubes CERTIFIED (log/R_d3_L9_cert.txt).
- L-SI frame query 1 (box 70, m 3 t1 T 11 = «T_1(3) >= 11»): CERTIFIED (log/lsi_q1_cert.txt; Glucose 2.39 GB, drup 6,531,220 lemmas).
- Box 27 tables: T^R(2) = 4 (C exhaustive), T_k(1), T_k(2) k <= 12 + unlimited, SUM_1 m 1, 2 = 5, 9 (README.md).
### IN FLIGHT: L-SI frame query 2 (box 71, m 3 tk T 13 K 2 = «T_2(3) >= 13»; DIMACS sha1 f3d4b6ad = lsi/dump/*.cnf.gz)
- Complete split: cubes c = 0..7 on vars (2, 8, 14) (frame.py x(o, X), o = 0, 1, 2; bit i of c set -> +var). CERTIFIED: 1, 2, 3, 5, 6, 7
  (records log/q2_cert/q2_c<c>.gen|.chk). Cubes 0 and 4: their monolithic checks were killed by restart #7 (21:58Z 11-06); each is
  split again on vars (20, 26) (sub s: bit 0 -> +20, bit 1 -> +26): sub-cubes q2_c0s0..3, q2_c4s0..3. CERTIFIED: c4s1.
  At 01:04Z running (this container only): drup on c4s0 (72% of 3.08 GB), c0s1 (67% of 3.23 GB), c0s0 (32% of 5.76 GB), c4s2 (33% of
  1.97 GB); queued c0s2, c0s3, c4s3 (Glucose not started). Records of every sub-cube so far: log/q2_cert/.
- The proofs and cube CNFs live in THIS session's scratchpad (/tmp/claude-0/.../scratchpad/lsi/): a NEW session does not see them.
  Successor: for every sub-cube without «s VERIFIED» in log/q2_cert/, regenerate and check (Glucose is deterministic):
    cd experiments/comp/box27; mkdir -p W; zcat lsi/dump/m3_tk_T13_T20_K2_NOIM0.cnf.gz > W/m3_tk_T13_T20_K2_NOIM0.cnf  (sha1 f3d4b6ad)
    gcc -O2 -o drup drup.c
    PDIR=$PWD/W C=0 BASE=-2,-8,-14 PAR=2 setsid nohup ./subcubes0.sh >> log/lsicubes.out 2>&1 &
    PDIR=$PWD/W C=4 BASE=-2,-8,14  PAR=2 setsid nohup ./subcubes0.sh >> log/lsicubes.out 2>&1 &
  (W/ must be gitignored: proofs are 1-6 GB.) Each sub-cube: Glucose 0.5-3 h, drup ~1 GB/h. If a sub-cube proof is > ~4 GB, split it
  again on the next vars (e.g. 32, 38 = x(5, X), x(6, X)) the same way. When all 8 sub-cubes are VERIFIED: query 2 is CERTIFIED;
  collect the table (cube, cube literals, cube-formula sha1, Glucose s, proof sha1 + bytes, lemmas, drup s) into log/lsi_q2_cert.txt
  and report to the Lead.
- Paused / stopped by the Lead: T_1(3) <= 10 on my encoding (acube T1_m3_L11, paused 09:35Z 11-06), d 4 T>=13/14 and T_inf(3)>=18
  (stopped 04:09Z 11-06: my plain encoding closes no d 4 cube in 20 min); d 3 free-W / padded d 2 (lowest).
### Things only I know (successor 9)
- pysat get_proof() loads the whole proof into memory (10.5 GB RSS for a 9 GB proof -> killed). dimproof.py streams solver.prfile.
- pysat Solver.interrupt() does not stop cadical195 here: acube.py uses subprocess + timeout.
- drat-trim fetch / build is refused by the classifier («Code from External»): drup.c (own, audited by both referees) / drup2.c.
- Container restarts: 7 in ~36 h, at normal resource levels (log/resources.txt, local only); a harness-tracked background wait
  loop helps keep the container but does not prevent restarts. Background waits die at 2 h: re-arm.
- drup prints nothing until the end: progress = file position of fd 4 (awk '{print $2}' /proc/<pid>/fdinfo/4) vs proof size.
- rm with a $VAR target is refused by a safety check: use "${P:?}/..." or literal paths.

## STATUS 2026-11-06 01:4xZ (successor 9): P-TR3 FROZEN at d03d8370 (P-TR3.md sha1 cab32c0e, 125 lines; line L-1 221c81eb, 1 line);
16/16 d 3 cubes CERTIFIED (Glucose 4 DRUP + own drup.c; log/R_d3_L9_cert.txt). Sent to the Lead for the two referees.
- Restarts: 6 on 11-05 (~14:05, ~15:45-16:53, ~17:0x, 18:49, ~19:08, ~23:3x). Resource log (log/resources.txt, local) normal every
  time; a tracked background task helps (no restart for 4 h) but does not prevent them. After a restart: experiments/comp/box27/
  relaunch.sh; INT=60 setsid nohup ./mon.sh <abs>/log/resources.txt; keep one harness-tracked wait loop alive.
- Running: R_d4_L13, R_d4_L14 (d 4), INF_m3_L18 (T_inf(3) >= 18), acube.py summaries. Queue after them: optional T_1(3) <= 10
  re-derivation (L-SI box 70 has it EXACT; Lead 19:24Z); #5 d 3 free-W / padded d 2 lowest. #2, #3, #7 STOPPED (Lead 19:24Z).
- Things only I know: pysat Solver.interrupt() does not stop cadical195 here: use subprocess + timeout (acube.py). drat-trim fetch is
  refused (classifier). drup.c IGNDEL mode reaches the refutation one lemma earlier than the default mode.

## HANDOVER -- successor 10 (L-COMP 10, Opus 5.5) PARKED 2026-11-07 10:3xZ by date -u (~545k context; Lead 10:27Z order)
### STATE AT PARK (all jobs STOPPED; everything below is in committed files; relaunch: experiments/comp/box28/relaunch_all.sh)
- relaunch_all.sh (box28) starts: diskguard, xval_d3 (niced), q2pieces.sh (query 2), commit_loop, and box30/relaunch30.sh (lanes B_d32,
  D_d32; A and C are commented out as STOPPED). The cnf2 d 4 drivers (ISO_L13, R4_L14) are commented out (stopped 07:05Z / 05:32Z).
- BOX 30 lanes (state files experiments/comp/box30/out/<lane>.unit, <lane>_best.txt, <lane>.log; seed = base + unit):
  B_d32: units 0-5 done (seeds 310000-310005), next unit 6 = seed 310006; best out/B_d32_best.txt: F 2 6 14 30 62 126 190 127 95 …, T 257.
  D_d32 (SLACKH=7 score since 10:3xZ): no unit finished yet; next = unit 0 = seed 340000 from out/seed_D_d32.txt (G7_best_d28 + 4 TOP-ADD:
  30 level-5 violations, F(6) 222, T 270). Its earlier F(6)-score lane (seeds 330000-…) is out/D_d32_fsix*.
  A_d28 (300000-300005, flat F(6) 160) and C_d23 (320000-320009 top-trunc; 320100-320132 from H6 minus level 21, penalty 6) STOPPED.
  S(h) DATA: out/remlevel_profiles.txt. No HIT.
- Query 2 (records experiments/comp/box28/log/q2/): q2_c0s0p0 CERTIFIED (cube -2,-8,-14,-20,-26,-32,-38,-44; cube CNF sha1 32da2e76; Glucose
  UNSAT 2,969.6 s; proof sha1 78c37e99, 3,921,344,874 bytes; drup.c VERIFIED 8,849,652 lemmas, ~15,472 s). NEXT piece: c0s0p1q0 (c0s0 pieces
  p1-p7, each split x4 on vars 50, 56: parts q0-q3), then c0s1, c4s0, c4s2, c0s2, c0s3, c4s3 in 8 pieces each on vars 32, 38, 44
  (q2pieces.sh does exactly this; it skips any piece whose .chk holds «s VERIFIED»). Proof dir /home/user/pf/q2 (outside git; a new
  container must re-unzip the DIMACS: q2pieces.sh does it and checks sha1 f3d4b6ad).
- xval_d3: 10/16 P-TR3 cubes done (0, 1, 2, 5, 6, 9, 10, 13, 14, 15: log/xval_d3/c<c>.done), each frup VERIFIED = drup VERIFIED with
  DIMACS + proof sha1 = the P-TR3 table (log/xval_d3.txt, 11 lines: one cube logged twice across the 05:00Z restart); next cube 3.
### DONE (all pushed by commit_loop or by hand; all DATA unless labelled)
- BOX 28 (T^R(4)): NOT certified, not even EXACT-SAT. cnf.py roots > 4 h without verdict; frup.c (own forward RUP checker, = drup.c on
  124 d 2 cases + the P-TR3 cubes so far; same speed) kept as a second checker; PAIR-SWAP symmetry (README "Symmetry", lane proof +
  pairswap.py 0 mismatches) -> 8 roots; cnf2.py (new encoder, chains by one equivalence per (mover, option) along pi; 3.2x smaller;
  regression: T^R(3) = 8 re-derived (SAT 8, UNSAT 9 on 16/16 cubes), 1,096 pinned runs 0 failures, mutants caught) -- NOT audited;
  ISO witness ISO_1_d4_t12 (T 12) pinned; d 4 cnf2 cubes: R4_L14 1 UNSAT / 512, ISO_L13 2 UNSAT + 8 timeouts (25 min) -> STOPPED 07:05Z
  (Lead 05:32Z rule: does not fit 10 h). Per-cube DATA: experiments/comp/box28/log/cnf2_d4_status.txt.
- BOX 29 DONE: N5 (n5b SPEC, S3) on Γ3 of H5/H6/RECF4/DBL4: one FL run = L(G) = 136/209/67/30, one fallback at L(G)+1, iterations
  L(G)+3 (= L-RED n5v); Oink zlk --verify + harness verify.py OK; valuations <= 280 bits; N5'-xi (L-NEW n5bxi) 12/12/12/15.
### IN FLIGHT (restart: experiments/comp/box28/relaunch_all.sh; it also runs box30/relaunch30.sh)
- BOX 30 tower climbs (rclimb30 = L-LOWER rclimb.c with 192-bit values): B_d32 (seeds 310000+, F(6) 190), D_d32 (since 10:3xZ: seeds
  340000+, from L-LOWER 4 G7_best_d28 + 4 TOP-ADD, score GUARD 5 then −1000·(level-5 violations of L-LOWER 5's slack.py, ported as
  SLACKH=7; port = slack.py on 3 genomes) + F(6); start: 30 violations, F(6) 222), C_d23 stops 10:35Z (stopC.sh). HIT = out/HITS.txt: report to the Lead at once with the genome
  file, sha1, F vector, T, and replay30.py (own sim) output.
- Query 2 (q2pieces.sh, records box28/log/q2/): c0s0p0 drup finishing (whole, 3.92 GB proof), then the finaliser q2fin_c0s0p0.sh starts
  q2pieces.sh: c0s0 p1-p7 x 4 parts on vars 50, 56, then c0s1, c4s0, c4s2, c0s2, c0s3, c4s3 in 8 pieces on 32, 38, 44. A c0s0 piece ≈ 50 min
  Glucose + ~4 h drup: query 2 is many hours away.
- xval_d3 (niced): frup vs drup on the 16 P-TR3 cubes, 9/16 agree; log box28/log/xval_d3.txt (local until done, then commit).
- commit_loop.sh (box28): every 10 min commits all box 28-30 files + this notebook and pushes synchronously; live lane files are
  skip-worktree between rounds.
### NEEDS: none from the owner. Lead decides BOX 30's continuation after the next units.
### Things only I know (successor 10)
- pgrep -f / pkill -f match ANY command line containing the pattern, including waiting bash -c jobs and runners: it lost a queued chain
  (04:3xZ) and DEADLOCKED queued commit jobs (07:2xZ). Kill by PID files; anchor patterns ("^bash scripts/push.sh").
- Never edit a running bash script (bash reads it as it runs): stop it by PID, edit, relaunch; after kill, wait for the PID to vanish
  before relaunch_all.sh (its up() checks kill -0 on the old PID).
- rclimb.c (L-LOWER) overflows __int128 at d 32 (ranks to 127): use rclimb30.c. pinck.py runs its CLI on import (exec its text before
  'if sys.argv[1] == "files"'). A d 4 Glucose proof grows ~7.6 GB/h; drup slows as the DB grows (c0s0p0: 3.9 GB in ~4 h).

## Successor 10 handover check (L-COMP successor 10, Opus 5.5), 2026-11-07 01:1xZ by date -u
- Stale-clone check: clone was shallow; fetch --unshallow + merge --ff-only ("Already up to date"); HEAD = origin/claude/l-comp =
  ls-remote = cf2e0e4f. The brief's handover commit ae9e7069 is NOT in the remote (git cat-file: not a valid object at 01:0xZ); L-COMP 9
  has a push running (Lead 01:07Z), so I read successor 9's STATUS / resume / box27 README / P-TR3.md at cf2e0e4f instead.
1. Branch claude/l-comp, head cf2e0e4f. Against trunk claude/vibrant-johnson-nxvvxo: 4 ahead, 982 behind; merge-base 9c70c980.
2. Open work: (i) query 2 sub-cube checks = L-COMP 9's, NOT mine (Lead collects them; I do not touch log/q2_cert/). (ii) BOX 28 (mine):
   T^R(4) certified. Next steps: witness read-back (DONE: max_d4_L13 pinned, SAT at 13, UNSAT at 14), sample cube times for T >= 14,
   feasibility report to the Lead by ~03:00Z, then the cube run with Glucose 4 proofs + drup.c.
3. GAPS rows owned: none open. The only row naming L-COMP is G-N5-TERM ("L-NEW (L-COMP checks runs)"), closed. G-N5-TIME (open)
   is L-NEW's; box 28 feeds it with DATA / CERT only.
4. Rulings (status from trunk docs/DECISIONS-INDEX.md): D1 (active): «A claimed polynomial algorithm is far more likely to be wrong
   than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.» D18 (active): «Focus on
   N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer
   science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without
   asking me questions. Clearly distinguish proven results from conjectures and open problems.» D20 (active): «We have reset the
   weekly usage, so we can again work faster no?»
5. Trap: a proof loaded into memory (pysat get_proof(), 10.5 GB RSS on query 2 cube 0, killed) and proofs of ~1-2 GB filling disk.
   Check: dimproof.py streams the proof file; each proof is deleted only after "s VERIFIED", sha1 + size recorded; df before each wave.
   Also the shared branch: git fetch + merge origin/claude/l-comp before every commit (L-COMP 9 still commits q2 records).

## Resume point -- successor 9, BOX 27 (running), updated 2026-11-05 10:5xZ by date -u
- Everything: experiments/comp/box27/README.md. DONE: T^R(2) = 4 (C + CNF), T^R(3) = 8 (CNF cubes), T_k(1), T_k(2) k <= 12 + unlimited.
- CONTAINER RESTART 2026-11-05 ~14:05Z killed every solve (no cube had finished). Since 14:3xZ all searches run under acube.py
  (adaptive cubes: 20-min cap per cube, split on the next option's Xi-target on timeout; state cubes2/TAG/<id>.res|.split).
- IN FLIGHT. After ANY restart run: experiments/comp/box27/relaunch.sh  (idempotent: skips running tags and finished cubes)
  R_d4_L13 (d 4 witness), R_d4_L14 (d 4 T >= 14), F_d3_L9 (d 3 free W, T >= 9), P22_d2_L5 (d 2, W free, 2+2 padding, T >= 5).
  Progress: python3 acube.py TAG d L summary. Logs log/acube_TAG.out (local exclude while running).
- QUEUE (Lead 14:13Z / 15:02Z / 15:45Z, in order): (1) P-TR3 packet + RUP certificates (proofs.sh); (2) T_1(3) >= 11 (acube
  T1_m3_L11, FREE0=1 KF=1; reproduce L-NEW T_1(3) >= 10 = T1_m3_L10); (3) SUM_1 at m 3: a+b >= 18, splits a = 0..8 (RUN2=a, L=b),
  pruned by (2); controls a+b = 17 SAT; (4) frontier max post s.t. pre >= p, m 3, pre 3..6; (5) d 4 T >= 13 / 14; d 3 free-W and
  padded d 2 lowest; (6) INF-2: T_inf(3) >= 18 (KF unlimited, d 4); (7) L-SI box 67 tau-cells «T_0(G) <= 5 and T_1(G) >= 11»
  (answered by (2) if UNSAT) and «T_0(G) >= 6 and T_1(G) >= 10».
- NEXT: padded d 3 (W=free P=1,1,0 and P=1,1,1) T >= 9 cubes; padded d 2 P=2,2 rerun without the 3000 s timeout if it timed out.

## Successor 9 handover check (session_01V5yGRVtZknivpYHCjzoA9y, Opus 5.5), 2026-11-05 09:5xZ by date -u
- Stale-clone check: ls-remote claude/l-comp = 3ae78ea86869 = local HEAD after fetch + merge --ff-only ("Already up to date").
1. Branch claude/l-comp, head 3ae78ea8 (box 26). Against trunk claude/vibrant-johnson-nxvvxo @ b738337b: 0 ahead, 705 behind;
   merge-base = 3ae78ea8 (the Lead merged everything of successor 8).
2. Open work: none inherited (successor 8 parked with no jobs). New: BOX 27 (Lead brief 2026-11-05): (a) independent exact T^R(d), d 2-4,
   own engine + own CNF (next step: own simulator + brute force d 2-3); (b) T_k(1), T_k(2) for k <= 12 (FREE0 external flips) and the
   padded class T*(d) at d 3, 4 (is T* > T^R?).
3. GAPS rows owned: none open. The only row naming L-COMP is G-N5-TERM ("L-NEW (L-COMP checks runs)"), status closed.
4. Rulings: D17 (active): «We have so much still of our weekly usage cap, like we are not on track to make the most of it».
   D18 (active): «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of
   mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them
   briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.»
   D20 (2026-11-05, quoted from the Lead brief; not yet in trunk docs/DECISIONS-INDEX.md at b738337b): «We have reset the weekly usage,
   so we can again work faster no?»
5. Trap: pgrep -f / pkill -f with a pattern in your own command line matches your own shell (bit successors 7 and 8). Check now: wait on
   output files / line counts, never on process names; and Lead messages arrive late: ReadNotifications between long waits.

## Resume point -- PARKED: successor 8 (session_01V5yGRWL1xbdLiUMMLuy7vR, Opus 5.5), 2026-10-31 06:4xZ by date -u. Lead 04:38Z: box 26 last, then park.
- Boxes this session: 23-26, one directory and README each (experiments/n5-box23 .. n5-box26). Every push via scripts/push.sh, VERIFY PASS.
### DONE (all DATA unless labelled; tables and sha1s in the READMEs)
- BOX 23 (R*_F, FL_F per W-run): rstar.py (own, n5b) = xirise.py on 1,132/1,132; exhaustive C(4) all 268M start pairs R*_F <= 1, FL_F <= 1;
  climbs R*_F ~0.7-1.0n (42 at n 60); latew R*_F = K·m exactly (7 sizes, n 186-778), an independent reproduction of L-RED R138.
  PROVED (trivial): R*_F, FL_F <= |F|, so R*-POLY and FL-POLY together = W-run length POLY; incl = strict. 15 pins.
- BOX 24 (|F| at small n; root map): max |F| = n - 1 exhaustive n <= 4; climbs n 5-7 only n - 1; first |F| > n - 1 at n 8 (F8_n8), n 9
  (F10_n9, one late adoption); casc.py (own Even root map) = retcause.py 599/599; RETURN node with 35 > n children (kr35_n30, no clones),
  PXR 5 at deg 2 (pxr5_n32). C(4) root-map pass PARTIAL (parts 0-3, stopped by the Lead).
- BOX 25 (INS): ins.py (own) = treestab.py 1,132/1,132; tie_n32 and u23sw64 reproduced; climbs max INS 9 (ins9_n48), INS = |I| - 1.
- BOX 26 (XICH): xich.py (own) = xirise 'xich' 1,132/1,132; R139's observer family reproduced (max XICH = K·m + K + 1, up to n 448: 821);
  climbs max XICH 31 at n 48 (xich31_n48); every extreme has max XICH ~ |F|.
### IN FLIGHT: nothing. No background jobs.
### NEEDS: none from the owner. Open (not routed): a super-quadratic W-run (nest the observer funnel / latew pivot cycles), L-RED's side.
### Things only I know (successor 8)
- Lead messages can arrive hours late (21:49Z and 22:17Z arrived at 00:13Z): call ReadNotifications between long waits.
- red/n3/instances/n3cov_lean.start is invalid (R99): overlay start files on S3 dropping invalid entries (n5-box23/rstar.overlay).
- pkill -f / pgrep -f with a pattern in your own command line kills or matches your own shell. A whole `cd X && ... &` chain is
  backgrounded, cd included.
- Climbs on rare quantities (return-node children, INS, XICH) need a gradient: (quantity, secondary, #returns or |F|); seed from the
  corpus or construction maxima. Seeded climbs beat fresh ones by 2-3x at n 32-48.
- L-NEW cause_*.txt / L-SI tree_*.txt are xargs -P 4 outputs with interleaved lines: parse the last record on a line.
- pin23.py writes its instance copies into n5-box23/instances: delete them after pinning another box's witness.
- Running another lane's tool from its branch: git archive its experiments/new/box21, new/n5.py, harness, si into /tmp, run with -I.
- Generators: LATE=1 red/span/mkrw.py K m (latew); OWNER=0 ABOVE=a red/mix/obs2.py on mkrw K m (R139 observer).

## Resume point -- PARKED: successor 7 (session_01V5yGRZrRdwiCSQqHfS2zGE, Opus 5.5), 2026-10-29 19:2xZ by date -u. Lead 17:49Z: box 22 last, then park; no successor for now.
- Handover check 76a57b40 (successor 7's answers in docs/agents/handover-checks/L-COMP.md). Boxes this session: 17-22, all under experiments/n5-box17..22/
  (one README per box: definitions, cross-checks, every table, every pinned sha1). Every push via scripts/push.sh, verify PASS each time.
### DONE (all DATA unless labelled)
- BOX 17 (exhaustive small-n tables of L-SI's quantities): box17.py = my implementation on n5b of REL cutting / SEG-COUNT EXC / SEG(S) /
  L-WAVE' gap / f per phase / DL-RUN deadlocks; xcheck.py = field-by-field equality with L-SI's own tools (seglast.segs, segsw, relseg,
  lwave PMODE=1, chg/dlock.py) on all L-SI/L-RED pins + 4,000 random games: 0 mismatches. Model C(n) (all owners, parity patterns, successor
  sets; ids in rank order; privar.py: priorities matter only by rank+parity). EXHAUSTIVE n <= 4 with ALL start pairs (C(4): 12,960,000 games,
  268,435,456 pairs), L(3) all rank orders; random n 5-8. 0 violations; max EXC 0, SEG 3, L-WAVE' gap 3 = n - 1 (tight on 384 trajectories),
  f 1, no deadlock step at all (least n with DL-RUN in [5, 20]; segcount_kill_n20 is 1-minimal under vertex/edge deletion, dlshrink.py).
- BOX 18 (T32): nm.py carries (= T32 and T33 brute force on all K=6 pairs, all parities; = L-RED gatep.py counts). NM <= 1.18n (pl130_n40);
  LIP DEAD (ladderd0_k12_n48 [0,13] v 14); HAM-MONO DEAD in all forms; NEST-FACE (ii) PROVED (mine, unrefereed) from R84 monotonicity.
- BOX 19: CUT-Φ DEAD (b4_n5_other_0, n 5: cycle-appearance cut with no path-set change; wk1_n32 σ̄-type).
- BOX 20: N5-SF SBC tables (sf20.py on L-NEW's n5sf.py verbatim copy, n5-box20/lnew_box54 @ l-new 56a42d4f): n <= 3 exhaustive, C(4) every
  16th game, random n 5-8: 0 cycle/region/opt violations, max SBC/n 1.17.
- BOX 21: PGSolver friedmannsubexp / fearnleysubexp ported (hard-families/pgsolver_port.py); byte-identical to L-LIT's T47 generator on 36
  (family, N) pairs N 1..12 (+ friedmann N 13..20); NOT diffed vs the PGSolver binary (build refused by the permission classifier).
  N5 linear (friedmann 4N+3 S3 / 4N+13 lastedge, N <= 16); N5-SF SBC ~ 0.08n on friedmannsubexp N <= 20 (DSB = SBC + 1, no cycle-centre
  counter). check.sh gate n5-box21/check.sh.
- BOX 22: fcN (L-RED R115) rebuilt from my own switchbestexp port (fc3/6/10 sha1 = L-RED's); sfb.py = N5-SF on n5b (= n5sf.py on fc3-6, fc8
  and 1,000 random games). N = 3..16, S3: L-RED's iteration counts reproduced exactly; SBC_σ = N² for N <= 14, then 227 (N²+2) at 15 and
  257 (N²+1) at 16; SBC_τ = N. N5 itself on fcN is linear (41..129, ≈ 6.3N + 22, 0 fallbacks).
### IN FLIGHT: nothing. No background jobs. Parked on the Lead's 17:49Z order (no successor for now).
### NEEDS: none from the owner. Open (not routed): a PGSolver binary diff of friedmannsubexp/fearnleysubexp if an OCaml build is ever allowed.
### Things only I know (successor 7)
- An experiments/n5-box17/enum.py name shadowed stdlib `enum` (any `import re` broke): never name a module after a stdlib module (renamed exh17.py).
- pgrep -f in an until-loop matches its own command line (bit me again 10:3xZ): wait on files/line counts, not process names.
- run_parts.sh N P: resumable parts (skips existing JSON); merge.py merges; parts' .log files are in .git/info/exclude locally only.
- n5x (L-SI/L-NEW engine) is ~2x faster than n5b for N5-SF; sf20.py caches each state's step per game, so all-start tables cost ~ #states.
- Building PGSolver (ocaml/dune) is refused by the auto-mode classifier ("Code from External"); apt install of ocaml was allowed.
- Oink must be rebuilt per container (scripts/setup_oink.sh, ~5 min); verify.sh needs it.
- L-SI's rows() uses n5x; its "fb" is the flag of the transition LEAVING a state; runs() splits at k with fb; phases need j > i.

## Resume point -- PARKED: successor 6 (session_01JPReGnoQGuUgg6d59WzGYS), 2026-10-28 22:1xZ by date -u. Lead 22:06Z: BOX 16 CLOSED, park.
- Last pushes: aeff7b04 (box 16 §4/§5), eabb3018 (XR-LIN repro), d9197efe, 973520df. Both 973520df and aeff7b04 merged by the Lead.
- No background jobs. Oink was built in this container (gitignored; rebuild with scripts/setup_oink.sh).
- Open (not routed): an H_n variant whose Odd gate must re-open many times (Odd's S4b as a counter). That is L-RED / L-NEW design work;
  a future L-COMP successor measures it with experiments/friedmann-hn/randstarts2.py --var (add the variant to hn_var.VARS).
- Trap this session: a Lead message claimed 973520df was on trunk when it was not. Check with `git merge-base --is-ancestor`
  before relying on such a claim.

### Box 16 history (successor 6), 2026-10-26 by date -u
Handover check 9c5bd6e2 (Lead: 5/5). GO 19:18Z. Everything: experiments/friedmann-hn/README.md.
### DONE (DATA)
- hn.py: H_n from [F] §8.4 Table 7 (arXiv 1106.0778, sha256 46c96f44...); Fact 8.1 asserted; mode fig (gate priorities 8i-5.., Fig. 8-10;
  Table 7 as printed collides with the lane: not injective) and mode table. M1's switchbestexp is NOT H_n (25N+10 vertices).
- iglo.py: I^glo (PGSolver switch_globally_best port) from ι: 16*2^n - 21 steps (n 1..6), Lemma 8.3 holds: H_n faithful.
- box16.py on n 3..8, 10, 12, 16 (F = (ι, σ̄(ι)) = Fs3, S3, G<k> mid-counter): 45 runs OK (n5 = n5b = L-SI rows; Oink zlk; verify), 0
  violations. N5 LINEAR: S3 it 6n+4, longest 5n+1 exact; F it 8.06n+9.4, longest 7.06n+3.4. Shape: n tau changes (e_i -> h_i, one gate
  per iteration, empty phases), then one final phase (lane walk + ~1 sigma-bar flip per gate, ALT ~ n+2). f = 0, lambda_Xi const.
### DONE after RESTART (2026-10-28)
- XR-LIN reproduction (eabb3018): experiments/xr-lin, n5b only: Xi(o) changes 86 > 2n = 82 on l121reader_n41, run on 0..39 = long121_n40.
- §4 randstarts2.py (XR, ALT, TF per run): 1,612 H_n runs, 0 FAIL, all linear; τ re-flips at a gate at most twice.
- §5 hn_var.py dual / ex: linear in n; gate flips ≤ 2 / ≤ 1; dual phases = it + 1; ex F phases 3n + 3.
### IN FLIGHT: nothing.
### Things only I know (successor 6)
- exh.py imports L-NEW's experiments/new/box25 'common'; L-SI's gcx needs experiments/si/root 'common': box16.py pops sys.modules['common'].
- n5b.read_start with no TAU0 line leaves tau all -1 (truthy list, S3 not used): always write both lines.
- [F]'s start σ̄(ι) equals S3's τ on H_n (same start sha1).

## Resume point -- HANDOVER of successor 5 (session_017XFY64b42Hkc6fmeUEzwek, Opus 5.5), parked 2026-10-26 ~19:0xZ at ~515k context
Boxes this session: handover check 1a8a4628; box 12 epoch census cf441de1; HON-FF add-on 15bcfa06; box 13 growth law + rho_q table 73e72e55;
box 14 NCONF 6f782d57 + EP-ASM dda29260; box 15 UL_G / GCI-LEN (this push). Everything: experiments/n5-epoch/README.md (one section per box,
every command, every sha1). No background jobs. NEEDS: next box from the Lead (successor 6).
### DONE (all DATA; 0 violations of any landed or lane statement tested)
- census.py (EP0/ALT/NEP/XEP/SPLIT/EPOCH/MONO), honff.py (HON-FF; IMM/IMM' dead confirmed), rhotab.py (= L-SI relay.py exactly), nconf.py
  (= L-NEW nep90 exactly), epc.py (EP-ASM in the Lead's form), ulg.py (UL_G, GCI-LEN; = L-RED on b6_xs_n24).
- Records pinned in experiments/n5-epoch/instances/ (pin.py: n5.py = n5b states, Oink zlk, verify.py): nep94_n48 (N_ep 94, NCONF_{>=2} 93),
  nep92_n40 (92), lend107_n32 (|D| 3 epoch len 107 = 3.34 n), lend82_n32, ret14_n48 / ret14_n64 (R0_{>=2} 14), ffin12_n32 (12 fallbacks in one
  honest gap), gci2_n12 / gci3_n24 (gated global C-intervals n - 3 / n - 4).
- Growth law: not separable (fresh climbs b <= 0.5; seeded b ~1.2-1.3 seed-dominated; fixed k = 5 all b <= 0); only the |D| >= 2 epoch
  length still rises with budget at n 32 (58, 63, 62, 82, 107/95 for 240 ... 7,680 s).
### Open items for successor 6
- L-SI's FREEZE-G per-gate reset count (Lead 15:04Z (5); docs/si/N5-ROOT-box20.md §9): NOT RUN.
- Longer lend doubling at n 32 (15,000 s+), several seeds (seed variance is large: 107 vs 95).
### Things only I know (successor 5)
- TRAP that bit me: Lead messages queue while a long tool loop runs; four arrived during box 14 and I read them only at its end (C-ONCE and
  UL_C were already dead by then). Check: call ReadNotifications between every wait step of a long box, not only at the end.
- Engine: n5b.N5(g, mode="spec").run(..., trace=, fbtrace=); census.state_info gives Xi, sbar, lam, lamW, W, D, RD, H per state.
- honff.lev(g, SG, Xi, lam, oddmap, budget): LEV in G_tau (oddmap = tau) or H_C (oddmap = sigma-bar); optimistic-completion prune verified by
  levcheck.py (0 mismatches vs brute force).
- climb.py fitnesses nep, lend2, nconf2, ret02, gdl, ulg; --fixk keeps |Q|; seeds padded with Even self-loops; replay any best with
  census.py FILE.pg:FILE.start. Wall-clock budgets: steps fall with n (n 64 seeded ~1-2k steps); always report steps.
- runjobs.sh JOBFILE (env P parallelism) runs climb job lists; fit.py DIR fits END lines.
- Stop-hook: untracked climb logs trigger "uncommitted changes"; wait in-turn (10-min steps) or commit partial logs.
- epc.py's "runs" in box-14 outputs mixed game and fallback-free runs (fixed to ff_runs later).


## Resume point (successor 5, session_017XFY64b42Hkc6fmeUEzwek, Opus 5.5) -- box 12 (epoch census) DONE 2026-10-26
Handover check 1a8a4628 (Lead: 5/5). Box 12 GO 07:57Z. Code + tables: experiments/n5-epoch/ (README.md has every command and number).
### DONE
- census.py (n5b SPEC engine, own definitions pinned to RESULTS R60/R61/R63/R64): N_ep, ρ, ALT classes, |D_E|, len(E), X_SN^pre; falsification
  tests EP0/ALT/NEP/XEP/SPLIT/EPOCH/MONO/D-EPOCH with mutation controls. 0 violations on named (60 runs), lib41 (1,236), random C^kO (100,000),
  exhaustive C^2O n 4 all starts (3,538,944), C^2O n 5 every 10th (10.8M).
- Climbs (climbs.sh): N_ep 76 at n 40 (nep76_n40, seeded rise_thin51), 56 at n 32; |D| >= 2 epoch len 55 at n 32 (lend55_n32, |D| 4), 47 (|D| 2).
  All pinned with pin.py (n5.py = n5b states, Oink zlk, verify.py).
### Box 12 add-on HON-FF DONE (15bcfa06). Box 13 DONE (growth law; rho_q table): see experiments/n5-epoch/README.md "Box 13".
- Scaling climbs: fresh exponents <= 0.5, seeded ~1.2-1.3 (seed-dominated; steps fall with n); budget doubling at n 32: lend still rising (82).
- rhotab.py = L-SI relay.py counts exactly on lib41; N_ep records have acyclic star relay graphs (root q = 0 ROUTE-only).
### Box 14 (NCONF add-on 6f782d57; EP-ASM box GO 15:04Z) DONE: README "Box 14" (both sections). Item (5) FREEZE-G NOT RUN.
### IN FLIGHT: nothing (no background jobs). NEEDS: next box from the Lead. HANDOVER: this session parks at ~480k (Lead: handover ~600k).
### Things only I know (successor 5, box 13-14)
- climb.py fitnesses: nep, lend2, nconf2, ret02, gdl; --fixk keeps |Q|; seeds padded with Even self-loops. runjobs.sh JOBS (env P = parallelism).
- Wall-clock budgets: steps per climb fall with n (n 64 seeded ~1,000-2,000 steps); compare steps before reading a trend.
- fit.py parses END lines of *.log in a dir; family = <fit>_<fresh|seed|seed90|k5>_n<N>_r<R>.
- epc.py's "runs" counter in b14 outputs mixed game runs and fallback-free runs (fixed to ff_runs afterwards; ff runs = phases + f).
- honff.lev(g, SG, Xi, lam, oddmap): oddmap = tau gives LEV in G_tau, = sigma-bar gives LEV_C in H_C.
- rhotab.py reproduces L-SI relay.py exactly with --lsi-starts 4 --nmax 48 --kmin 1 (random.Random(path) starts).
### Things only I know (successor 5)
- n5b.run has an fbtrace hook (fallback flag per transition), no effect on the run.
- lib41.txt contains games up to n 492 (not n <= 64).
- climb.py mutates the start pair too; replay with census.py FILE.pg:FILE.start (the .start is SIGMA0/TAU0).
- check_instance.py's analyse assumes C^1O; use experiments/n5-epoch/pin.py for k >= 2.
- Background watchers using `until ... ; do sleep` hit the 10-min foreground limit; run them with run_in_background.


## Resume point (successor 4, session_01AiLCefKYn3CkbJsYJtY5aR, Opus 5.5) -- HANDOVER after box 11 (2026-10-26 07:3xZ by date -u)
Handover check cd3b5ff7 (5/5). Boxes run: 7 completion, 8, 9, 9b, 10, 11 + N5 step-2 diff. Last push: see git log (box 11 1d2f29d7 + this).
### DONE (all pushed on claude/l-comp; every number is DATA unless labelled)
- Box 7 complete (4633d132): box7.py + box7w.py on the whole n 5 subset (68,764,800 runs), 0 violations; J <= 1, Z <= 1, K = 0, S_o <= 1.
- Box 8 complete (758d02ef): box8.py = REFEREE-2 oe/cls/sn/h1_check (start pair) + REFEREE probes (canonical) on n 4 / n 4 all starts /
  n 5 subset: 0 violations; max J 1, K 0, X <= 3, X_SN <= 2, REL <= 3; VACUOUS: CLS1/FBL/CLU, WK, ABS-L.
- N5 gauntlet step 2 closed (45def408, a47b3fa3): experiments/n5-second/seqdiff.py; n5b SPEC = n5.py state by state on 22,810 runs +
  box 43/44 frontier 459 runs.
- Box 9 (52e326aa..589dc66c): climb9.py; WK non-vacuous (9,020 checks pass; wk1_n32, wk2_n32); CLS1 small-n climbs n 6-12 vacuous;
  ABS-L climbs: 0 theta-changes above L.
- Box 9b (86193e62..589dc66c): gdnc_check.py (G_D-NC b'/c1'/c2', C2-H3, FRZ-U_H3), frz_climb.py; FRZ instances frz1/frz3_n24 test FRZ-U_H3
  as proved, frz2_n24 only the stronger 1-based form (author: 0-based); not-(NC) case of FRZ-U_H3 VACUOUS (tau changes after 80% of
  not-(NC) states).
- Box 10 (95f35638, 16c960b5): instances/notnc/ (8 pinned (h3_D) and not-(NC) in-phase states); n5tau.py + tau_check.py: N5^tau on 26,573
  runs, 0 violations of R48 (i), R50 (h), R51 (a) via REFEREE-2 fbpoly_check / kw_check unmodified; N5^tau != SPEC on 497 runs.
- Box 11 (c4fef4b0, 1d2f29d7): citeclosure.py: RESULTS closure of R48, R50 = L-NEW's §9.2 list exactly; rund_check.py: OFFSET (a)-(c),
  TWIN-GAP (i)-(iii) 0 violations on 322,065 runs, TWIN-GAP (ii) vacuous.
### IN FLIGHT: nothing (no background jobs). NEEDS: none open from the Lead; next box to be routed.
### Things only I know (successor 4)
- Runners live in the scratchpad (lost with the container); every command is in the README sections / script headers.
- gdnc_check.state_info is the shared state machinery for gdnc_check, frz_climb, rund_check (D_k, u(v), pi_v, NC, h3, M_D, h_D).
- REFEREE-2 checkers expect FULL strategy lists with the non-own entries CONSTANT along a run (out_check compares whole tau lists);
  tau_check.full() fills them with succ(v)[0]. My first version used one combined list and produced 3 fake "fallback changes tau" FAILs.
- .start formats differ by lane: SIGMA0/TAU0 v:w (mine, L-NEW), bare v:w pairs (L-SI si/instances), 'sigma [list]' / 'tau [list]'
  (L-NEW box45). seqdiff.readstart handles the first two.
- L-NEW's DIV is measured on the restricted game G'_E of an epoch, not on G: div_n8 diverges only on its G'_E (results/tau/divE_n8.pg).
- citeclosure.py: lane report numbers collide with RESULTS numbers (L-RED R73, docs/red/R72-, OUT-R1, NEB-R1, P-N5-NH (R1)); filters
  are in TOK / LANE; R1/R2 hits left are DATA/SIG-only labels.
- climb best files are overwritten on equal fitness; the logged seed is the last STRICT improvement: replay with score(g, seed) may not
  reproduce; search many random starts on the best instead (done for frz3/frz4).
- Never `pkill -f` (killed my own shell twice); kill by pid. scripts/push.sh can take 10+ min under full CPU load.

## Resume point (successor 3, box 7, 2026-10-25 by date -u) -- HANDOVER
### DONE box 7 (Lead GO 23:2xZ; amended 00:28Z: (c) via L-RED u23x.py; 00:33Z: NO-WAKE false, table K and S_o instead)
- box7.py (R23 WM/LV', R24 CASC/TB/U1, R25 FB/MONO, J): n 4 canonical, n 4 all starts, n 5 quarters 1-2: 0 violations, max J 1.
- box7w.py (K, S_o, rise causes, u23x P-N5-U23, E, K_W): n 4 canonical, all starts, n 5 quarter 1: 0 violations; max K 0, S_o 2, E 1, K_W 2.
- README "Box 7" (rows Q234ROW / W5ROW to fill).
### IN FLIGHT (resumable; rerun the same command, finished tasks are reused from results/box7/<tag>.tasks/, gitignored)
- At park (04:3xZ): box7.py exh 5 --no-forced --even-maxdeg 2 --o-deg 2 --cyclic-only --every 4 --offset 2 (then --offset 3)
  --jobs 4 --out results/box7, ~2 h each, running unattended in this container (scratchpad run7x.sh). A successor reruns the same
  commands; finished tasks are reused from results/box7/<tag>.tasks/ if the container survives, else they restart from zero.
- Not started: box7w on n 5 quarters 2-4 (same command with box7w.py and --offset 1/2/3).
### Things only I know (box 7)
- nowake.py / mblock.rows_w and u23x.rows_x hard-code start_pair(..., None); box7w rebinds the module-level name start_pair.
- u23x.rows_x caps runs at 400 states (fine for n <= 5).
- A container restart loses the .tasks caches only if the directory is lost; they are gitignored, so a new container restarts the
  n 5 quarters from zero.

## Resume point (successor 3, box 6 end, 2026-10-24 23:0xZ by date -u)
### DONE box 6 (Lead GO 20:0xZ)
- box6.py: exhaustive checks of P-N5-NH (c7981ee) F1°, TC (i)-(iv) and CONJECTURE (OB_R) per crossing-free interval; --every/--offset
  sampling, resume. 0 violations on n 4 canonical, n 4 all starts and the WHOLE n 5 subset (4 quarters = 68,764,800 runs, 100,587,132
  intervals, 3,432 OTHER blocks); F1° and (OB_R) attained (slack 0), never exceeded. n 4 canonical: (OB_R) vacuous.
- X chains: one-wave ~0.8-0.9n; wave chain from L-RED x32_waves32; long climbs at n 32: X 67 / 75 / 77 at 360 / 1,500 / 2,400 s
  (b6_xl2_n32, 2.41n); n 40: 79, n 48: 84. X rises with budget at fixed n: maxima are lower bounds. README "Box 6".
### IN FLIGHT: nothing. Queue: longer X climbs (budget is the limit); a k-digit wave design is L-RED's target, not mine.

## Resume point (successor 3, session_01BmytANWGKiHZhXK9QC2rB2, Opus 5.5; box 5 = X / O per joint lambda-phase; 2026-10-24 by date -u)
Handover check 0ef77018 (5/5, Lead GO 17:5xZ). Box 5 started 17:52Z.

### DONE (pushed on claude/l-comp)
- box4.py: X (crossing transitions), O (OTHER-touching), Xmn (X - n), Xplen/Oplen; --slices + resume (OUT/TAG.tasks/<i>.json);
  --no-reentry. xo_validate.py: equal to L-NEW box28 xcount.py on 33 instances (4 pinned ones included). shrink.py --prop X/O/canonX/
  canonO --thr T. climb5.py (X/O hill climb, optional SEED.pg padded to n). xo_split.py (box 29 split per crossing-free interval).
- Tables: n 4 canonical (X 2, O 1), n 4 all starts (X 3, O 2), random n 6-16 (X <= 4, O <= 3), climbs n 6-16, seeded O chain
  n 10-40 (b5_o11, b5_os_n12..n40: O = phase length, 11 .. 77, O/n peaks 2.14 at n 28). README "Box 5".
- Reported to the Lead at once: O > n (18:27Z), O/n rising (19:00Z), O split (19:13Z: F1° and (OB_R) hold; growth = F-changes).

### IN FLIGHT
- n 5 canonical subset: DONE 19:56Z (68,764,800 games, all 160 slices; results/box5/box4_n5_ed2_od2_nf_cyc.json).

### Things only I know (box 5)
- L-NEW's |R| (reach_o) excludes o; thtrace.Rset (mine, xo_split) includes o. X is the same either way; for (OB_R) compare with
  |R| without o.
- box29 scripts live on claude/l-new only; run them from a git-archive copy with PYTHONPATH=experiments/new:experiments/si:
  experiments/harness and symlinks box25/box28 next to box29 (python -I breaks their sibling imports).
- Climbs are very seed-dependent (O at n 10: 11 once, 6 twice at 300 s); seeding from the previous best is what made the O chain.
- Every O-chain phase is pattern 23 throughout, tau constant: the long phases are Even-only improvement runs at fixed tau.

## Previous resume point (successor 2, kept for its "Things only I know"; LANE-RESTART step 1; successor 2 parks after box 4, 2026-10-24 ~17:40Z by date -u)
Session session_01TpuThMoeBcLB2T5KKeJpAa (Opus 5.5), boxes this session: N8d step 2 + switchbestexp + box 2b (2026-10-23),
box 3 and box 4 (2026-10-24). Lead asked to park at ~587k context after box 4.

### DONE (all pushed on claude/l-comp; merged by the Lead up to box 3)
- N8d-R2 second implementation: experiments/n8d-second/ (kl2.py frozen c0dc7a21; kl2fast.py C port reproduces it on every row);
  R1/R2 equal to L-NEW per instance; switchbestexp R2 to N 30 ~ n^2; box 2b: tau_1 / tie-break settings do not change growth.
- Box 3: experiments/n5-exhaustive/ (exh.py, rnd.py, shrink.py, check_instance.py, README.md): theta-driven re-entries exist
  (thetaA_n6, thetaA_canon_n8, ...); exact small-n tables n <= 4 (+ n 5 subset partial); T28 (b) false; SEG-1O, ELIM-n, H-E hold.
- Box 4: box4.py (CYC' = theta+w changes, NH = non-(h) transitions, phaseprofile.py convention, every phase; reentry.py classes);
  tables n 4 canonical, n 4 all starts subset, n 5 subset partial, random streams; nh_n8 (smallest found: non-(h) throughout a
  4-iteration phase, o on the play cycle, start pair). README "Box 4" section.

### IN FLIGHT
- Nothing (all background runs stopped 17:35Z; partial JSONs copied to experiments/n5-exhaustive/results/; box 4 written up in
  experiments/n5-exhaustive/README.md "Box 4").

### NEEDS / next for a successor (box 5, Lead 17:1xZ)
- Add X (crossing transitions: R changes) and O (transitions touching an OTHER state: (h) fails and Xi != W) per phase to
  box4.measure (a few lines: R via thtrace.Rset per state, O via rows[k][3] and Xi[o] != W[o]) and re-run the small-n tables
  (n 4 canonical ~10 min on 3 cores, n 4 all-starts subset ~35 min).
- Finish the n 5 canonical subset (exh.py / box4.py exh 5 --no-forced --even-maxdeg 2 --o-deg 2 --cyclic-only; 160 (o, parity)
  slices, ~2-3 min per slice per core with box4's reentry pass); there is no resume: rerun from scratch, or add a --slices option.

### Things only I know
- exh.py's canonical subset (ids in priority order, distinct priorities) is the only symmetry reduction; L-SI's Engine ranks by
  (priority, id), so it is Engine-equivalent up to relabelling, but N5 id tie-breaks could differ on relabelled copies.
- "max_*" excess columns in exh.py start at 0, so 0 means "<= 0"; rnd.py tracks true maxima (negative values are real).
- box4 phases are keyed by (lambda_sigma, lambda_tau, tau(o)) (phaseprofile); exh.py's maxph uses joint lambda without tau(o)
  (phases.py). The two give different phase lengths (n 4 all starts: 4 vs 3).
- reentry.py re-runs N5 itself (n5x.step); box4 calls it only for runs with >= 2 iterations.
- check_instance.py is the gate for any reported instance (n5.run counts, n5b SPEC full state sequence, Oink zlk, verify.py).
- n5b.py has a trace hook (run(..., trace=list)) added 2026-10-24; behaviour unchanged.
- Monitors that grep THETA lines from random streams at n >= 8 flood; filter by n.
- kl2fast.py builds out/lfp.so with gcc on first import; out/ is gitignored.

## Queue (for the successor, after the running cells)
0. sat-hard state (from the 2026-10-14 resume point): CEGAR-only s^V(5,5) k=10 and TARGET n=5 strong k=8 UNSAT; CNFs lost
   with the container; regenerate with `diag.py 5 5 V strong --klo 10` / `diag.py 5 7 V strong --min-letter 2 --klo 8`.
   Next k: w^V(5,5) k=10, s^V(5,5) k=11, TARGET n=5 k=9 (1-2 h per k per core; cube.py on 4 cores). Needs cadical (apt).
1. Report the four n=5 cells with evidence; LRAT for out/w_n4_d6_k8.cnf (w^E(4,6) >= 9; solve ~1000 s, proof large).
2. Remaining (Lead's order): (4,5) V weak/strong, (5,6) V, E cells (4,5)/(4,6)/(5,4) k >= 9 (cube.py for 4 cores).
3. Low: w(2,d) for d >= 14 (E): k=4 UNSAT (CEGAR only) for d=14,16,20,24; row2.py computes the row (slow).

## How to run the bench on a new claim
Wrap the claimed algorithm as a command that reads a PGSolver .pg file (max-parity, owner 0 = Even, priorities any
naturals) and writes a 'paritysol' solution with a positional strategy for every vertex owned by its winner (see
experiments/harness/README.md; avh.py is a worked example, register it in experiments/harness/solvers.py). Then:
(1) `python3 experiments/harness/compare.py DIR --solver NEW='CMD {in} {out}' --stop-first` on a seeded corpus
(`gen.py corpus DIR 10000 SEED --nmax 200`), an rngame corpus (`rngame_corpus.sh`), exhaustive tiny games
(`exhaustive.py`, or `iter_games` in-process for Python code) and experiments/harness/bench/hkp_*.pg; compare.py
reports MISMATCH (regions differ from Zielonka) or BADSTRAT (strategy not closed/winning per verify.py).
(2) every hard family: add the solver to experiments/hard-families/run_all.sh (or `sweep.py FAMILY --gen ... -s NEW`)
for agreement plus runtime growth tables/plots. (3) On the first failure: `experiments/m2/shrink.py` (adapt the
solver import) to a minimal game, save the .pg, push, message the Lead with SHA, game, expected and actual result.

## Open items
- counter_qpt growth class: qpt lifts jump x15 at N = 8 and x31 at N = 16, ~N^3..N^4 in between, timeout at N = 32;
  run N = 29..40 with a long timeout (sweep.py counter_qpt --timeout 600) to see the N = 32 jump.
- PGSolver binary diff: DONE 2026-10-15 (pgsolver-binary-diff.md), all identical.
- counter_dtl is listed in Oink's README (8fbf0a7) but has no source upstream (no src/tools/counter_dtl.cpp, not in
  CMakeLists); not swept.
- avh strategy construction S1/S2 is not always winning (experiments/m2/counterexamples/strat_s2_12v.pg); moot since
  M2 is closed.

## M2 pseudocode
Source: arXiv 2511.03752v1, R. van der Heijden, "Attractors Is All You Need: Parity Games In Polynomial Time"
(submitted 2025-11-04). Opened 2026-10-14 as the LaTeX e-print (sha256 of e-print 4dc6c4b9...ee2e4; main.tex
9840db37...3f8b). Line numbers "tex:N" refer to that main.tex; the paper has no numbered equations. Theorem
numbering follows the paper's counter: Lemma 1 (tex:290), Theorem 2 (tex:322), Lemma 3 (tex:341), Lemma 4 (tex:397),
Theorem 5 (tex:404), Lemma 6 (tex:413), Theorem 7 (tex:421), Theorem 8 (tex:428); Algorithm 1 (tex:370-395).

### Conventions of the paper
- MIN-parity: "Even wins the play iff min{inf(pi)} is even" (Sec. 2, tex:274). TARGET.md is max-parity.
  Implementation maps a max-parity game with priorities 0..P to min-parity by rho'(v) = M - rho(v), M = P rounded up
  to even: order reversed, parity kept, so winning regions and strategies are unchanged. (Mine, not the paper's.)
- player(d) = Even if d even else Odd; par(d) = d mod 2 (tex:301). In A(G,d) the symbol O ("circle") is the player
  of d, O-bar the other (Theorem 2, tex:323: "priority d of player O, A(G,d) is an O-dominion").
- Attr as defined tex:280-286 (standard attractor, computed in the current game G).
- Subgame G \ U (tex:278).

### Pre-routine: self-loops (tex:297, Remark tex:335)
The paper assumes no self-loops and says they "can be removed as a pre-routine [friedmann_solving_2009]"
(doi:10.1007/978-3-642-04761-9_15, NOT opened: awaiting source). Reading used (from PGSolver d3cd624, Friedmann's
code: transformations.ml:15-24 remove_useless_self_cycles_inplace, specialsolve.ml:20-28 find_useful_self_cycles,
univsolve.ml:698-760 their use):
P1. For every v with (v,v) in E, rho(v) of parity NOT the owner's, and |E(v)| > 1: delete edge (v,v).
P2. For p in {Even, Odd}: S_p = {v : (v,v) in E, and (owner(v) = p and par(rho(v)) = p, or E(v) = {v} and par(rho(v)) = p)};
    X_p = p-Attr(G, S_p); W_p += X_p; strategy: v in S_p owned by p plays v->v, attractor strategy on X_p \ S_p;
    G = G \ X_p (Even first, then Odd on the remaining game, recomputing S_Odd there).
    (The "E(v) = {v}, wrong parity" case is my addition: PGSolver leaves such a self-loop in place.)
After P1-P2 no vertex of G has a self-loop (every remaining self-loop vertex was in S_Even or S_Odd or lost its loop).

### Definitions (Sec. 3, tex:301-318), for the current game G and a priority d, O = player(d)
D1. U_d(G) = { v : rho(v) <= d and par(rho(v)) = par(d) }                                     (tex:303)
D2. A*_d(G) = union over k in 0..d with par(k) != par(d) of { v in O-Attr(G, U_{k-1}(G)) : rho(v) = k }   (tex:304)
    (U_{-1} = empty set.)
D3. A'_d(G, A) = O-bar-Attr(G, { v in A \ (A*_d(G) u U_d(G)) : rho(v) < d })                 (tex:309)
D4. U^0 = U_d(G);  A^0 = O-Attr(G, U^0)                                                        (tex:314-315)
    U^{k+1} = U^k \ O-bar-Attr(G, (V \ A^k) u A'_d(G, A^k));  A^{k+1} = O-Attr(G, U^{k+1})     (tex:316-317)
    A(G,d) = intersection over k of A^k                                                         (tex:312)
    Computed by iterating until U^{k+1} = U^k (then every later A^k equals A^k).

### Algorithm 1 (tex:370-395), run on the game left after P1-P2
 1 n = |V|, m = |E|                                         (tex:374)
 2 D = ordered list of priorities (unused afterwards)        (tex:375)
 3 W_E, W_O = {}, {}                                         (tex:376)
 4 while V != {}:                                            (tex:377)
 5   dhat = max priority of G                                (tex:378)
 6   O = Even if dhat even else Odd                          (tex:379; the tex writes "d", read as dhat)
 7   dbar = max priority of O-bar in G                       (tex:380)
 8   compute A(G, dbar)  [an O-bar dominion by Theorem 2]    (tex:382)
 9   W_{O-bar} += A(G, dbar);  G = G \ A(G, dbar)            (tex:383-384)
10   if A(G, dbar) != {}: continue                           (tex:385-387)
11   compute A(G, dhat);  W_O += A(G, dhat);  G = G \ A(G, dhat)   (tex:389-391)
12 return (W_E, W_O)                                         (tex:393)
Implementation guard (mine): if in one iteration both A(G,dbar) and A(G,dhat) are empty and V != {}, stop and report
STUCK (Lemma 4, tex:397-402, says this cannot happen).

### Strategies (not in the paper; my construction, required by D2 change 5)
For a removed set A = A(G,d) = O-Attr(G, U) with U = U^k at the fixpoint:
S1. v in A \ U owned by O: the attractor strategy (a successor in the previous attractor layer).
S2. v in U owned by O: a successor in U if there is one; else a successor in A \ A'_d(G, A) (the case analysis
    in Theorem 2's proof, tex:328-330); else any successor in A (flagged in the log; the proof says it cannot occur).
Pieces are removed as O-attractors, so the remaining game is an O-trap and the per-piece strategies compose.
A failed strategy check therefore does not by itself refute the paper; a region mismatch does.

### Ambiguities (reading chosen; alternatives)
AM1 Parity convention: min-parity as written (tex:274). Alternative: the author meant max-parity (Algorithm 1 starts
    from the MAX priority, which in min-parity is the least significant one). Implementing max-parity instead would be
    a different algorithm; I implement min-parity as written and could add the max-parity variant as a probe.
AM2 Line 6 says "if d is even"; read d = dhat.
AM3 Line 7 when O-bar has no priority in G: reading A(G, dbar) = {} (skip to line 11). Alternative: undefined.
AM4 Self-loop pre-routine: see P1-P2 (cited source not opened; PGSolver's code used; forced wrong-parity self-loop
    vertex handled by me).
AM5 A(G,d) = intersection of the A^k (tex:312): since U^k decreases and Attr is monotone, A^k decreases; computed at
    the fixpoint of U. Alternative readings give the same set.
AM6 All attractors inside D2, D3, D4 are computed in the current G (whole remaining game), not inside A or U.
    Alternative: D3's attractor restricted to A. Chosen: G, as the formulas write "Attr(G, .)".
AM7 D3 uses strict rho(v) < d and excludes A* and U_d (as written).
AM8 Text references "line 12" for continue and "lines 8-10, 14-16" (tex:369, 408), numbering that counts the blank
    \[\] lines; my line numbers above are my own.
AM9 Lemma 3's proof sets D_{dbar} = D cap U_{dtilde} (tex:345), probably a typo for U_{dbreve}; no effect on the algorithm.

## Things only I know
- PGSolver (tcsprojects/pgsolver d3cd624) builds with apt OCaml 4.14 + dune 3.14 after two local edits
  ((lang dune 3.18)->3.14, drop maintenance_intent) in a dune workspace with tcslib 6778419,
  ocaml-sat-solvers 0264291, c-cube/ocaml-minisat aeb7776 (cloned under experiments/hard-families/out/pgsolver,
  gitignored; a fresh session must re-clone). Running the built binaries was refused by the permission classifier
  on 2026-10-14 ("code from external"); on 2026-10-15 (L15 attempt) it ran. Build also needs apt libextlib-ocaml-dev,
  libnum-ocaml-dev. switchall/switchbest: `pgsolver.exe -global policyiter -x "-sa"|"-sb" -dgo -dsd -dlo -dsg -v 3`.
- The ported SI (pgsolver_si.py) runs the bare strategy-improvement loop; PGSolver wraps it in universal_solve
  (preprocessing, SCC decomposition), so counts may differ from PGSolver's own. Details that matter for fidelity:
  TreeSet.choose = min_elt, folds ascending, del_edge is a no-op on deleted nodes, iter_by iterates a snapshot.
- switchbestexp.ml's description string repeats the switch-all text (line 79); its target is switchbest.
- Oink rngame is seeded from std::random_device: not reproducible; keep the files, not the parameters.
- Oink mspm (8fbf0a7) is unsound: logic error at mspm.cpp:486 on 4 rngame games, and on one game a wrong answer
  that Oink's own verifier rejects ("loser can escape"). Instances: experiments/harness/regressions/mspm_*.pg.
  Exclude mspm from any "all solvers agree" claim.
- Oink preprocessing (single-parity, winner-controlled cycles) solves counter_qpt and the PGSolver families
  outright; use the oink-<s>-raw registry entries to make the solver see the game.
- Oink's work counters are solver-specific (iterations, promotions, lifts, major iterations); compare across sizes
  of one solver, never across solvers. Iteration counts are deterministic with -w 1; wall times are noisy.
- py-zlk is slow on exponential families (Python recursion); sweep.py skips a solver after its first timeout.
- Background watchers: `pgrep -f NAME` inside a loop matches its own command line; use a pid file instead. (Bit again
  2026-10-15 20:10Z: an `until ! pgrep -f "sweep.py X"` watcher never ended; wait on a log line instead.)
- gen.py uses its own splitmix64 so games are identical across Python versions; selftest pins the corpus hash.
- sat-hard: graphs.family/family_V/family_S are my own generators (progress-measure trees; every graph brute-force
  checked); counts equal L-STRUCT's maximal families. Families are not reduced to maximal graphs: n=5 V families are
  ~30k-60k graphs, so each CEGAR round's check is slow-ish.
- Unary (thermometer) ranks + CEGAR are the best encoding found; binary ranks ~8x slower, pure lasso CEGAR does not
  converge, clique bounds are always 1 (shared tail -> same limsup parity), annealing / state merging fail.
- Never `pkill -f PATTERN` where PATTERN occurs in the current shell's own command line: it kills the shell (exit 144).
  List pids with `ps -eo pid,args | grep ...` first, then kill by pid.

- N8d (2026-10-23): kl2.py needs about n*d/2 Tarjan runs per pivot (Phi_p for every even p); switchbestexp N = 14 (n = 360)
  takes ~400 s per R2 run, N = 16 ~2x that. The naive-lifting oracle (--check) is exponential in d: use only n <= 16, d <= 6.
- N8d: the R2 draw `random.Random(seed).choice(sorted candidates)` reproduces L-NEW's sequence exactly, so R2 seeds are
  comparable per instance across the two codes.
- famF/G/H/L: the added nodes are isolated Even self-loops with top priorities; pivot counts are constant in k by construction
  (R1 and every R2 seed), so these families test only correctness, not growth. counter_core N and counter_dp 2N give identical
  counts for every rule and seed.

- kl2fast.py: speed came from keeping labels in C buffers across pivots and doing the admissible scan in C; a C LFP alone with
  Python label conversion was only 5x. pypy3 (apt, 7.3.15) gives only 1.7x on kl2.py. The C .so builds into out/ (gitignored) on
  first import; gcc must exist.
- run_families.sh line "echo ... tail -1 $R/$f.kl2.log" prints a tail error with IMPL=kl2fast (cosmetic; exit codes are right).

- Box 3: exh.py's analyse() reruns Engine evaluations per state (Xi_sigma, Xi_tau, W, R, trust set, route lengths); ~0.2 ms per
  trivial game, ~2-3 ms per run with >= 2 iterations. Full n 5 (7e9 games) is out of reach in Python; the canonical subset (ids in
  priority order) is the only symmetry reduction used. Max fields initialised at 0 mean "<= 0" for excess columns.
- Monitors on THETA lines flood when random streams at n >= 8 hit often; filter by n in the grep.

## Sources opened
| source (arXiv id / DOI) | result used (theorem / section) | opened on | note |
| --- | --- | --- | --- |
| github.com/trolando/oink @ 8fbf0a7 | solver list (README), generators src/tools/*.cpp, solution format src/game.cpp:459 | 2026-10-14 | code, not a paper |
| arXiv 1405.0386v2 (LaTeX e-print, Huth-Kuo-Piterman) | Figs. 4(a), 4(b), 6 tikz source (archiv.tex:815-855, 1164-1194); conventions archiv.tex:225, 342-343 | 2026-10-14 | bench witnesses |
| arXiv 2511.03752v1 (LaTeX e-print) | Sec. 2-3, Algorithm 1, Thm 2, Lemmas 3-4 (see M2 pseudocode) | 2026-10-14 | M2 subject |
| github.com/tcsprojects/pgsolver @ d3cd624 | generators recursiveladder.ml, policyiter/generators/*.ml; paritygame.ml conventions | 2026-10-14 | code, not a paper; papers awaiting source |
| arXiv 2108.13338v5 (LaTeX e-print, sha256 7189eb2f...5c816c; abs page lists v1 2021-08-30 .. v5 2025-06-15) | §2 (prelim.tex: ordered/universal trees, labels, feasibility, violated/tight/loose, Tighten, lift, Prop. 2.6 lattice fixed points); §3 (strategy-iteration.tex: Algorithm 1, admissible arcs, Thm 3.1 correctness, base nodes, Thm 3.3 MinBottleneckCycles); §4 (label-setting.tex: Algorithm 2 Dijkstra, Lemma 4.1, Thm 4.2, Cor. 4.3; §4.1 Algorithm 3 LabelSetting, Thm 4.4, Rem. 4.5) | 2026-10-23 | N8d second implementation; theorem numbers are my count in source order, the .tex uses labels (thm:correctness, thm:dijkstra, cor:dijkstra, thm:label-setting) |
| arXiv 1106.0778 (pdf sha256 46c96f44775aa2b07cad20912cb325b177e38c94cb2e40297df66b6047679611 = L-NEW's), O. Friedmann, LMCS 7(3:19) 2011 | §2 (Ω injective, l.132 of pdftotext), §3, §4 (I^glo), §5 (1-sink), §8.1 Table 5 / Fig. 7 / Lemma 8.1, §8.2 Fig. 8, §8.3 Table 6 / Fig. 9 / Lemma 8.2, §8.4 Table 7 / Fact 8.1 / start ι_{H_n} / Fig. 10 / Lemma 8.3, §8.5 Theorem 8.4, Fig. 11 | 2026-10-26 | box 16 H_n. Table 7 gate priorities collide with the lane (d2_n = t1 = 8n+3 etc.); Fig. 10/8/9 use 8i-5..8i+2: hn.py mode fig. Text says lane length 6n-3, Table 7 has i <= 6n-2 (= m of §8.1): 6n-2 used |

| github.com/tcsprojects/pgsolver @ d3cd624 | src/lib/generators/policyiter/generators/friedmannsubexp.ml (90 lines), fearnleysubexp.ml (86 lines), stratimprgenerators.ml SymbolicParityGame | 2026-10-29 | code, not a paper; box 21 ports |
| fleet docs (successor 8, 2026-10-30/31) | RESULTS R88 / R89 / R95 (W-run, BLOCKED, R*_T, FL, GP*-RUN, XI-CH); l-new 893b9346 N5-FREE-box85 §3; l-new 2311683e N5-CASC-box100 §1-2 + N5-QRET-box99 §2.1 + N5-RET-box98; l-si 481bc6c2 N5-SBF-box53 §7; L-RED R99, R128, R138, R139, R148-R150, R152 | 2026-10-30/31 | internal lane notes, not papers; every definition used is quoted in the box READMEs 23-26 |

## Dead ends
- 2026-10-30 (box 23): "R*_F = O(n) per W-run" (any reading of box 85's R*-POLY as linear) DEAD on L-RED's latew_K20_m32 (sha1
  063d173c…; LATE=1 red/span/mkrw.py 20 32): one W-run, R*_F 640 > n = 538 (rstar.py on n5b = xirise.py; first shown by L-RED R138, l-red 5374e0a5, so mine is an independent reproduction). Exact on 7 sizes: R*_F = K·m,
  |F| = K(m + 3), n = 14K + 8m + 2, so Θ(n²) balanced. Not a kill of R*-POLY.
- 2026-10-30 (box 23, method): hill climbs on R*_F saturate near n (best 42 at n 60), far below the construction; climb fits are not growth laws.
- 2026-10-18 (method note): watcher loops counting 'done' lines never end when a run crashes before printing 'done'; count
  log lines or processes instead (three stale watchers hit their time limits this box, no data affected).
- 2026-10-15 (not a dead end of an idea; a method note): a C5-literal reimplementation cannot reproduce Oink's
  tangle counts: four orders (step-0 std::sort, in-edge order, stored tangle order, Pearce SCC order) change counts.
  Use dtl_py.py --order oink for exact counts; stdsort.py emulates libstdc++ introsort incl. heap fallback.
- 2026-10-14 sat-hard (L-STRUCT task): pairwise-inconsistent-word clique bound (always 1: u.y and v.y share the tail's
  limsup parity); simulated annealing (stuck at 16 violations, (3,6) k=7); pure lasso CEGAR (no convergence at (2,6) k=2);
  binary ranks (~8x slower UNSAT); merging strong separators (fails to recover the known (2,6) weak separator).
- 2026-10-14 (M2 closed BROKEN by the Lead 18:36Z; REFEREE's independent counterexample breaks readings (a)-(d)): arXiv 2511.03752v1 Algorithm 1 as read in
  "M2 pseudocode" is incorrect. Obstruction: Theorem 2 (A(G,d) is a player(d)-dominion) fails; A'_d only removes
  vertices the opponent can force into lower-priority parts, but player(d) (here Odd) can dodge A' on a
  cycle that never returns to U^k, and that cycle can be won by the opponent. Instance: experiments/m2/counterexamples/ce1_4v.pg
  (4 vertices, all Odd's; Even wins all; the algorithm gives all to Odd via A(G,1) = V). Trace in that folder's README.
- 2026-10-29 (box 18): CONJECTURE LIP (T32 E1 (b), all three readings) DEAD. Obstruction: a vertex can switch many times while its jW / jH
  successor is fixed or ⊥. Instance: red/ul/instances/ladderd0_k12_n48 (+ .start), REL segment [0, 13], vertex 14 switches 12 times,
  jW(14) = 1 switches once, jH(14) = ⊥.
- 2026-10-29 (box 18): HAM-MONO (T32 E7; strict, weak, even-only, odd-only) DEAD. Obstruction: path sets move back toward the phase start.
  Instances: gci3_n24 S3 (phase [3, 15], v 8, |PΔP_i| 6 → 5) and lend107_n32 S3 (odd part 5 → 4).
- 2026-10-29 (box 19): CONJECTURE CUT-Φ (T35 §4) DEAD. Obstruction: a REL cut can change no path set at all (cycle appearance or σ̄ change
  with ℓ-only effect). Instance: n5-exhaustive/instances/b4_n5_other_0.pg (n 5, S3), cut 0 → 1.
- 2026-11-08 (box 31, L-COMP 12): PHASE-2 hand edit at level 7 (re-target q6 = 12's options to a level-9 trigger) DEAD as a one- or
  two-edit repair. Obstruction: 12 is upstream of movers 0-3 (they read 12's value), so any re-target of 12 breaks level 0 (F(0) = 0).
  Instance: box31/out/L7_FRZ_K7099382600043_L7b.txt (sha1 0e71e029), edits 24 -> 18/19, 25 -> 18/19 (box31/phase2_test.out); two
  edits + 2e6-proposal climbs reach caps <= 2 (box31/phase2b_sum.out).
