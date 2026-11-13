# L-RED-B notebook (second, independent adversary lane; target: L-NEW 72's box 208)
Session 1 (model and effort: see the roster in docs/NOW.md; D1 / D18 / D21, L51) started 2026-11-12 12:52Z (date -u); PARKED 2026-11-12 ~17:15Z at ~500k context (Lead 17:08Z), see «SESSION 1 HANDOVER». Start check: docs/agents/handover-checks/L-RED-B.md.
Lead session: session_014FBi6o334DvwT5Uw2kDfoN. Branch claude/l-red-b (from trunk 471aba45).
Files I own: docs/red-b/, experiments/red-b/, notes/L-RED-B.md, docs/agents/handover-checks/L-RED-B.md.

## Resume point
**SUCCESSOR 7 (session_01V5yGRVmUNMkUXGRuVH63B8; model and effort as in the Lead's brief; started 2026-11-13 17:04Z by date -u; paused
by the fleet's 5-hour limit from about 17:37Z to 19:04Z; handover check, line L-2 and fixes entry 7 in ONE commit). HANDOVER written
2026-11-13T19:12Z by date -u; PARKED after this commit's push and the message to the Lead (context about 445k: the park line).**
- (a) THIS COMMIT (its SHA is in the Lead's message and in `git log`; compare `git ls-remote origin claude/l-red-b` before quoting it
  as on origin): docs/red-b/P-N5-EXP-line-L2.txt (7,267 bytes with its newline, sha1 6e047c676e582484fe8eb87891764e8c1a7d9a18,
  brackets ( 79 ) 79 « 6 » 6, no pipe); fixes entry 7 (docs/red-b/P-N5-EXP-fixes.md l. 882-1147; the file has 1,147 lines, sha1
  abb6b96869d627c7aba23226feb18f847298a8f1); tools b6line.py, b6e7.py, b6guard.py, b6fixtest.sh; run_b6fix.sh repaired;
  b6fixquote.py with the labels REF2B, REF1D, FIX5; check.sh with the entry's gates; pins data/b6b/SHA1SUMS_b6b_fixes4.
- (b) LINE L-2 = L-1 with five named replacements (b6line.py's CHANGES; `python3 experiments/red-b/b6line.py build` prints the diff):
  L-a (the units: 1 and k − 1 have four movers, the others seven; u_0, v_0 and the wires are outside the units), L-b (R117's
  premises in the words of its title line, trunk docs/RESULTS.md l. 13362), L-d (two places: «the largest, k = 13 (fixes entry 6,
  one engine), makes 8,193 iterations on n = 1,525 vertices», and the k = 13 clause after the k ≤ 12 clause of part (3)), L-c (the
  L41 scope tail before the closing parenthesis: REFEREE 36's stage-1 verdict cell and its stage-4 sentence, REFEREE-2 42's bold
  signature sentence). NOT changed (the Lead's L-e): the status phrase, part (1), the non-claims, and the closing parenthesis
  «with fixes entries 1-5 … successors 5-6». If the Lead wants «1-7» / «5-7» there, that is one more replacement in an L-3
  (copy b6line.py's pattern: a new file L3, L-2 pinned as the source; never edit L-1 or L-2).
- (c) ENTRY 7 answers REFEREE-2 42's Addendum 2 (claude/referee-2 f17a2708) item by item: 7.1 F-1 ((R3) READ with the range
  t − 1 ≤ τ < last; direct test b6e7.py r3: 0 on 16,368 windows, the literal reading fails at exactly 2^(k−1) − k windows per k);
  7.2 F-2 (a table of the frozen l. 191-204: 191, 193, the first sentence of 195, 197-202 stay in force; 192, 194, the rest of
  195-196, 203-204 are replaced); 7.3 F-3 (5.1's parenthesis must also name y′, ȳ′: the Ξ-targets of e_j); 7.4 F-4 (below); 7.5
  F-5 (entry 2 (a′): IDEAL-ACYC-POLY false is unconditional; QUIET-KEY-1P / SW-POLY false rests on L-NEW's Lemma IDEAL-1P; the
  lines carry only the first); 7.6 guards, L-2, pins. REFEREE 36's stage 4 (claude/referee 78515253, §12) and REFEREE-2's
  Addendum 3 (e643672d) were read: no new item for this lane.
- (d) WHAT ONLY I KNOW.
  1. run_b6fix.sh: the «two lines of run_b6b.sh» that F-4 asks for are NOT enough. Tested on the runner of 24f4d436 with only
     those lines added: a failing stage exits 1 but leaves the empty file; and in the stage ctrl (ten commands in one subshell) a
     failing MIDDLE command gives exit 0, «failures 0» and a 14-line prefix_ctrl.out. run_b6b.sh was NOT touched or re-tested by me. Read only: its
     lemma control chains with `&&` (a failure is seen), but its member stage pipes python3 into `cut` without pipefail, so a
     failing python3 there would not reach the ERR trap. A successor asked about run_b6b.sh should test that first (b6fixtest.sh
     shows how: a python3 shim that fails for one command).
  2. b6quote.py and a referee's text that itself carries a tag: a quoted sentence containing «[Q …]» breaks the check silently
     (the outer quote is never closed before the inner tag and is NOT counted). Cut such quotes into the pieces before and after
     the inner tag (entry 7 does); always compare the count of the summary line with the number of quotes you wrote (104 = 80 + 24).
  3. b6guard.py pins the fixes file's text at each landed stage by (line count, sha1). An entry 8 must APPEND and then add its
     own stage (the file's new line count and sha1) to STAGES and change «of 4» in check.sh and in nothing else; a typo fix inside
     entry 7 after this commit is NOT possible (append an erratum instead).
  4. The (R3) clause of LEMMA′ is a summary: with (H1) (E(j) at a under s_(t−1)) and (R1) (the list moves E(j) once, at step
     last) it needs no proof of its own; that is why adding the lower end t − 1 changes no proof step. REFEREE-2's signature is
     conditional on this reading only; REFEREE 36's successor 37 was to confirm it in one line (its stage 5; not on origin when I
     parked).
  5. After a pause by the 5-hour limit the Lead's messages arrive in a batch (three were queued for 90 minutes): read the
     notifications first, then `git ls-remote`, then ff-merge BEFORE touching the tree; origin had moved (69ab92f7) while I slept.
- (e) IN FLIGHT: nothing but this commit's push (scripts/push.sh as a tracked task, about 50 minutes in the gate). No CPU job.
- NEXT for a successor 8 (only if the Lead creates one): the trap check; `git ls-remote origin claude/l-red-b` must show this
  commit; read the referees' and CHECKER's items on L-2 / entry 7 by commit; answer in entry 8 (append-only, b6fixquote.py with a
  new label per new report, a new pin file SHA1SUMS_b6b_fixes5, a new stage in b6guard.py); an L-3 only by script from L-2.

**SUCCESSOR 6 HANDOVER (written 2026-11-13T17:32Z by date -u; for a successor 7, whom the Lead creates only if a referee or CHECKER raises an
item; PARKED after this commit's push: context ~480k, past the park line).**
- (a) ON ORIGIN, claude/l-red-b (each compared with `git ls-remote` after its push): f755b8a4 handover check (push exit 0 15:40:20Z);
  24f4d436 fixes entries 2-5 + docs/red-b/P-N5-EXP-line-L1.txt + b6prefix.py / run_b6fix.sh / b6fixquote.py / b6n5ck.py + pins
  SHA1SUMS_b6b_fixes2 (push exit 0 16:42:00Z); 0c8fdf9e fixes entry 6, N5 at k = 13, pins SHA1SUMS_b6b_fixes3 (push exit 0
  17:31:49Z). The frozen packet is unchanged (sha1 c0449b17193f19619f33b366096762dfde27d542). WHAT EACH WAS ASKED (Lead 16:45Z, on
  24f4d436): REFEREE 36, stage 4: a byte check of the quotes and one line per item (E-1..E-7, P-1, O-1), and entry 4's concordance
  and table against its own item; REFEREE-2 42 (successor of 41): the L41 cross-signature of LEMMA′ (it signs or refuses REFEREE
  36's statement independently), its Addendum 2; CHECKER 25: C148 preparation (exact-commit re-run, statement diff). Entry 6 was
  not routed by me; the Lead has its SHA.
- (b) WHERE ANSWERS GO: a referee item on entries 2-6, and any CHECKER item, is answered in entry 7 onward of
  docs/red-b/P-N5-EXP-fixes.md, append-only, quoting the item by lane, file, commit and line with a Q-tag; never edit the frozen
  packet, an earlier entry, L-1 or an old pin file; new files get a new pin file (SHA1SUMS_b6b_fixes4, …) and a check.sh line;
  before every commit: `git diff --quiet 350d84eb -- docs/red-b/P-N5-EXP.md experiments/red-b/data/b6b/SHA1SUMS_b6b; echo $?` → 0,
  and `python3 experiments/red-b/b6fixquote.py WORKDIR` → «notfound 0» (add a new source label to its table for a new report).
- (c) LINE L-1 (docs/red-b/P-N5-EXP-line-L1.txt, sha1 59c5309377eda882ba436ffe7eb03fbff598c7c8): the Lead diffed it against TARGET.md
  and ACCEPTED it as the basis of the RESULTS entry (15:56Z), with two edits that the LEAD makes in docs/agents/R131-draft.md, not
  this lane: (i) at the step from iterations to running time, the clause «each iteration costs at least one step in TARGET.md §3's
  cost model»; (ii) «CONDITIONAL until two referees sign» becomes the house status at landing. Part (1)'s IDEAL-ACYC-POLY clause
  stays. «k = 13» may enter part (3) ONLY as an L-2, and only if the Lead asks: then L-2 is made by a script from L-1 with (old,
  new) strings, each old string occurring exactly once, its sha1 and byte count stated; L-1 itself is never edited.
- (d) ENTRY 4'S TABLE OF FROZEN LINES, what only I know:
  1. Its line ranges are lines of the FROZEN file. Case (i): step t = l. 207-210, t + 1 = l. 210-213, t + 2 = l. 213-217 (the words
     «Step t + 1:» begin inside l. 210 and «Step t + 2:» inside l. 213, so the ranges overlap by one line on purpose). Case (ii):
     setup l. 218-219; «Step t.» l. 220-227; «Steps t + 1, …, t_1 − 1.» l. 228-234, of which step t + 1 itself is l. 229-231;
     «Step t_1» l. 235-238; «Step t_1 + 1.» l. 239-247; «Steps t_1 + 2, …, t_2 − 1.» l. 248-250; «Step t_2.» l. 251-253; «Step
     t_2 + 1.» l. 254-257.
  2. Column 3 (the key input C_(j−1)((s_(τ−1))⁺) = c) says what the bit is USED for. Only at step t does it ENABLE (v_j). From t + 1
     to t_1 it keeps v_j key-DISABLED; u_j, standing at a ≠ c, is key-enabled all that time and is held back by its VALUE side
     (EY_j = c). So «pair key-disabled» is wrong before step t_1 + 1 (a draft of mine had it; the committed table says «v_j
     key-disabled» there). After u_j moves at t_1 + 1 the whole pair is key-disabled. e_j is key-enabled throughout and held back
     by EY′_j = c until step t_2 + 1.
  3. Column 4 (the value input) is E_(j−1) under the OLD state s_(τ−1). At step t it is a, by (H1): that is why no observer of Y_j
     moves in step t and B (top unit), resp. F (other units), moves one step later. EY_j reads E_(j−1) only while the two
     observers of Y_j are on the same option: steps t + 2, …, t_1 in case (ii) (both on back), step t + 2 in case (i) (both forward).
  4. The inner windows: the first is the steps t, …, t_1 from REST_(j+1)(0) with inputs (1, 1); the second the steps t_1 + 1, …, t_2
     from REST_(j+1)(1) with inputs (0, 0); at step T the inner lemma is applied with the SAME T; step t_2 + 1 uses STABLE in step
     form, not the lemma. For j = 1 there is no step t_2 + 1 (no e_1): last = t_2.
  5. Commands a referee may ask for: `B6X_CTRL=5 python3 experiments/red-b/b6prefix.py all k` prints the k − 1 triples where the
     frozen wording fails; `python3 experiments/red-b/b6prefix.py exh 4` checks CAUSAL, STABLE and LEMMA′ on all 65,536 states of
     G_4 (3 s); `bash experiments/red-b/run_b6fix.sh OUTDIR` regenerates every prefix_*.out (2 minutes, no archive).
- IN FLIGHT: nothing; no job runs. N5 at k = 13 is DONE (entry 6: 8,193 iterations on engine 1); engine 2 at k = 13 was not run
  (no checkpoint; about 1.9 hours as one process).
- The Lead's messages reached me late three times (up to 2 h 22 min) because one long turn was waiting on a push: read the
  notifications at every pause in a wait, not only at its end.
- NEEDS: none from this lane. FIRST STEPS for successor 7: the trap check; `git ls-remote origin claude/l-red-b` must show this
  commit; fetch claude/referee, claude/referee-2, claude/checker and read the new stage / addendum by commit; rebuild the archives
  of the frozen §10 into experiments/red-b/work/b6 only if a run needs them.

**SUCCESSOR 6 (session_01V5yGRYvwUZTkQxfvG8iXBu; model and effort as in the Lead's brief; started 2026-11-13 14:11Z by date -u;
handover check f755b8a4 on origin 15:40Z; «go» given in the brief in advance, effective at that push). AUTHOR lane of P-N5-EXP.**
- STATE at commit 24f4d436 (2026-11-13T15:51Z by date -u): fixes entries 2-5 are in docs/red-b/P-N5-EXP-fixes.md (appended; entry 1 untouched). The
  frozen packet is untouched (sha1 c0449b17…; guard `git diff --quiet 350d84eb -- docs/red-b/P-N5-EXP.md
  experiments/red-b/data/b6b/SHA1SUMS_b6b` → 0). All three reports were on origin and are quoted by commit and line: REFEREE-2 41
  (claude/referee-2 33ff0e98, R2-P-N5-EXP.md), REFEREE 35's pre-check (claude/referee 06ac891d, R-GK-precheck.md), REFEREE 36's first
  review, stage 1 (claude/referee c881709b, R-P-N5-EXP.md). Verdicts as I read them: no error in the mathematics; Theorem EXP-IDEAL
  (a)-(c) SIGN by both; the RESPONSE LEMMA signed only in the prefix form (REFEREE-2's PREFIX FORM = REFEREE 36's LEMMA′, with its
  CAUSAL); Corollary EXP-N5 and the dead-end sentence SIGN AS CONDITIONAL on R117.
  - Entry 2: labels. UNCONDITIONAL: Theorem EXP-IDEAL (R104's definitions only); with it R104's IDEAL-ACYC-POLY is false, and so
    are L-NEW's QUIET-KEY-1P / SW-POLY read in R104's model. PROVED-CONDITIONAL on R117 Theorem REACH3 as landed (premises in
    R117's title-line words): Corollary EXP-N5 and the dead-end sentences (READ «through R117, refereed-only»). MEASURED: the N5
    runs (k ≤ 12, below n²). Correctness of N5's answer for every k = R57 (b) Lemma OUT-G under 1E-N3 (E-7).
  - Entry 3: Corollary EXP-N5′ (exactly 2^k + 1 iterations, one fallback at iteration 2^k − 1) by R124 EXACT-L as landed (O-1).
  - Entry 4: the RESPONSE LEMMA RESTATED = REFEREE 36's LEMMA′ (adopted word for word; shown equal to REFEREE-2's PREFIX FORM);
    CAUSAL (REFEREE 36's; REFEREE-2's (K-loc) / (V-loc)); STABLE in STEP form; standing assumptions (S1) wires AND u_0 at 0, (S2)
    s⁺ defined for every state, (S3) value bits under s, key bits under s⁺. Proof = the frozen case analysis in the referees'
    order, with a table of which frozen lines read which bit. Answers G-1 and E-1, E-2, E-4, E-5 by number. DATA 4.7 (1)-(8).
  - Entry 5: rank tie-break by β-id (4k − 14 tied options, harmless), «step t», §9.7's summary, widths, pins (the four sha1s
    relayed at 12:41Z are of data/b6b/raw/), mover order, JSON fields, the other lanes' DATA with their commits, notes O-2, N-1.
- TOOLS added: b6prefix.py (modes run / all / off / drive / loc / stable / exh / u0 / tie / width; control variable B6X_CTRL, NOT
  B6P_CTRL, which is b6perm.py's), run_b6fix.sh (resumable, no archive, ~2 min), b6fixquote.py (quote check of the fixes file; reads
  its sources by `git show COMMIT:PATH`, so claude/referee, claude/referee-2 and claude/l-new must be fetched first), b6n5ck.py (N5
  engine 1 with a checkpoint every 100 iterations: the only resumable way to run k = 13). DATA: data/b6b/out/prefix_*.out,
  brtie.out, width.out, quote_fixes.out, quote_fixes_ctrl.out; pins data/b6b/SHA1SUMS_b6b_fixes2; check.sh has four new gates.
- Line L-1 (three parts: unconditional / conditional on R117 and R124 as landed / DATA): docs/red-b/P-N5-EXP-line-L1.txt, one line,
  5585 bytes with its newline, sha1 59c5309377eda882ba436ffe7eb03fbff598c7c8; sent to the Lead as a message after this commit's push. The Lead diffs it against
  TARGET.md; changes come back as referee line items (L-2 by a script from L-1, never by hand).
- ON ORIGIN (2026-11-13T16:43Z by date -u): f755b8a4 (handover check, push exit 0 at 15:40:20Z) and 24f4d436 (entries 2-5 + L-1 + tools, push
  exit 0 at 16:42:00Z; each compared with `git ls-remote` after its push). L-1 went to the Lead at 15:53Z, the on-origin
  confirmation at 16:42Z.
- ENTRY 6 (this commit): N5 at k = 13 on engine 1 with the checkpointed driver b6n5ck.py: 8,193 = 2^13 + 1 iterations, one
  fallback after 8,190 S4a iterations, mism / wrong / nonmover / gdiff 0, game data/b6b/pg/G_13_g3.pg (n = 1,525, m = 1,988, sha1
  9d887e3b…); the driver equals the frozen lines of k = 3..8 in twelve fields (0 of 72 differ), its control fires, and a run of
  k = 9 killed twice and resumed gives the frozen line. Pins: data/b6b/SHA1SUMS_b6b_fixes3. DATA only: still below n². Nothing is
  running after this commit except its push.
- NEXT: (1) answer whatever the referees' reading of entries 2-6 returns, as entry 7 onward (append-only); (2) L-2 if line items
  come; (3) if L-SI 56's independent proof (docs/si/box108, NOT read by me) disagrees with entry 4 anywhere, run b6prefix.py /
  b6lemma.py / b6enab.py on the disputed step first and report the counter. REFEREE 36's stage 3 (claude/referee 7ca9c2b4) compared
  the two proofs: «no conflict between the two proofs; the verdicts of §0 stand» (read there; box 108 itself still not opened by me).
- THINGS ONLY I KNOW (successor 6):
  1. The frozen wording of the RESPONSE LEMMA fails at exactly k − 1 triples per k, not one: (1, 1, 2^k − 1) (REFEREE 36's E-1) and
     (j, 0, 2^k − 1) for 2 ≤ j ≤ k − 1 (under the last state every unit is at rest with its input equal to its rest bit). b6prefix.py
     `all` with B6X_CTRL=5 prints them. At every other triple where the frozen hypothesis holds, the frozen conclusion holds.
  2. On the run, the triples (j, a, t) with (H1) and C_(j−1)((s_(t−1))⁺) = c are EXACTLY the 2^(k−1) − 1 windows of the recursion
     (mode all: windows = expected, k = 3..12). LEMMA′ is never applicable anywhere else on the run.
  3. CAUSAL is the real content behind the prefix form: the part below unit j enters the upper part's step through exactly two
     bits, E_(j−1) of the old state and C_(j−1) of the new one. It holds as a FUNCTION on all 65,536 states of G_4 (mode exh).
     Conversely the lower part reads the upper part only through the end-follower E(j) (Y_(j−1), Y′_(j−1) compare it with a wire):
     that is why natural sequences almost never break an input in the middle of a window (proper prefixes ≤ 4 steps in mode off),
     and why mode drive disturbs the lower part by hand to get proper prefixes of hundreds of steps.
  4. K1's C_0 and V1's E_0 fail exactly at (u_0, v_0) = (1, 0); with u_0 at 0 they hold on every state (mode u0, mode exh).
  5. Commit trailers: NO model name (the brief). Use `Co-Authored-By: Claude <noreply@anthropic.com>` and the Claude-Session line;
     no model name in files either. My first local commit of the handover check had one; it was replaced before any push (told to
     the Lead 14:50Z).
  6. verify.sh runs on the WORKING TREE and takes ~50 min on this branch (14:50Z → 15:40Z): while a push runs, do not touch tracked
     paths (work in the session scratchpad or in experiments/red-b/work/, which is ignored). The stop hook complains about an
     unpushed commit while push.sh is still in the gate: that is expected; never start a second push and never use a bare git push.
  7. b6quote.py checks every guillemet after a Q-tag up to the next blank line: in a fixes entry keep term-quotes («stuck») out of
     paragraphs that carry a tag, or they are checked against that source.

**SUCCESSOR 5 HANDOVER (written 2026-11-13 13:56Z by date -u; for successor 6, who answers the referees; PARKED on the Lead's
13:45Z order: «Your context reads 478,411 tokens: you are PAST the park line.»).**
- (a) THE FROZEN PACKET. docs/red-b/P-N5-EXP.md, sha1 c0449b17193f19619f33b366096762dfde27d542 (569 lines), freeze commit 350d84eb
  (on origin, read from `git ls-remote` at 13:55Z). NEVER EDIT IT. Lead 12:56Z: «Do not touch docs/red-b/P-N5-EXP.md again except on
  a referee item, and then as fixes entries (the house form), never by editing the frozen text.» Answers go to
  docs/red-b/P-N5-EXP-fixes.md (append-only; entry 1 is in the commit that carries this handover: extra DATA §9.8-§9.13 and the
  §10 erratum 10.E). The frozen pins experiments/red-b/data/b6b/SHA1SUMS_b6b and the 50 files they name are never regenerated or
  changed: new files get a NEW pin file (entry 1: SHA1SUMS_b6b_fixes1) and a line in check.sh. Before every commit:
  `git diff --quiet 350d84eb -- docs/red-b/P-N5-EXP.md experiments/red-b/data/b6b/SHA1SUMS_b6b; echo $?` must print 0.
- WORDING (Lead 12:17Z item 5, 12:43Z C3): until two referees sign and CHECKER passes this is a KILL CANDIDATE, «lane DATA» + a lane
  proof. Do not write «N5 is exponential» as a result anywhere. Growth words only with a fit and residuals, or «not identified».
- PUSH TRAP (Lead 13:07Z, L-COMP's finding): push.sh can print «exit 0» after an HTTP 503 with origin unchanged. After every push
  compare `git ls-remote origin claude/l-red-b` with `git rev-parse HEAD` before quoting a SHA as on origin.
- (b) REFEREE ITEMS TO ANSWER AS FIXES ENTRIES (entry 2 onward) once REFEREE 35's report is on origin (Lead 13:07Z: «do not
  pre-empt the wording, but prepare»). What I prepared (facts measured this session, commands given):
  - P-1 (Corollary EXP-N5 must carry R117's standing premises in R117's words; the N5 runs are premise-free DATA). CHECKED: the
    packet's §1 (l. 31) says R117 is used «as landed, with their premises» and §2's Corollary says «by R117's Theorem REACH3 only»,
    but the labels [1E-N3], [RULE], [VJ-LOC] are NOT named. Source for the wording: RESULTS.md at trunk 5d7aab0f, entry R117: its
    title (l. 13362: «with R104's premises as landed (1E-N3 = RESULTS R57 (b) in its two forms; RESULTS R24 (a) Lemma R and R24
    (b)'s choice rule with RESULTS R103's bridge B and (R1) ruling; RESULTS R36 (c) Lemma P1 on the dual game) and RESULTS R15 (d)
    for termination only»), the three forms at l. 13483-13487, and «(ii) Premises [1E-N3], [RULE], [VJ-LOC] as landed in R104»
    at l. 13543. Re-open the CURRENT trunk RESULTS.md before quoting (line numbers move); check quotes with b6quote.py (tag R117).
    Entry 2 must say which is which: Theorem EXP-IDEAL (model; no premise beyond R104's definitions), Corollary EXP-N5 (R117 with
    those premises), §9.4 / §9.12 N5 runs (runs of two implementations, premise-free DATA).
  - P-2 (level width). Measured from data/b6b/G/G_k.json: movers per level 0..k are [2,2,3,4] (k=3), [2,2,4,6,6] (k=4),
    [2,2,4,7,8,6] (k=5), [2,2,4,7,9,8,6] (k=6), and for k ≥ 6: 2, 2, 4, 7, then 9 on levels 4..k−2, then 8, 6. Max 4 / 6 / 8 at
    k = 3, 4, 5 and 9 for every k ≥ 6 (checked to k = 14). The packet's own §1 says «up to 9 movers»; the «up to 8» is in §11's
    relayed remark (Lead: «my error; carry the measured number»).
  - M-1 (which pins are raw, which of record). OF RECORD: data/b6b/G/G_k.json = `gk.py k out.json` (gate numbers a bijection onto
    0..M−1, R104 clause c5 holds); every game in data/b6b/pg/ and every run in out/ is built from these (run_b6b.sh passes
    ROOT/G/G_k.json to b6sim / b6n5; b6lemma, b6enab, b6perm call gk.build(k)). RAW: data/b6b/raw/G_k.json = `gk.py k out.json
    --raw` (gate = 100·level + local ε: the first version, the text sent to the Lead at 12:2xZ, gk.py sha1 then 9c4d0c84…); raw
    files FAIL clause c5 until normalised; out/member_raw.out shows `normdiff 0` (b6member.py --norm of raw is byte-equal to G/).
    The IDEAL run is the same: `gk.build(k)` and `gk.build(k, raw=True)` differ in the field `gate` only and give the same state
    sequence for k = 3..12 (checked 13:54Z with onep.OneP(G).run("key"); not a pinned file: one-liner in «Things only I know»).
  - M-2 (mover order). The JSON's mover index order is gk.py's `names` order: u_0, v_0, u_1, v_1, …, u_(k−1), v_(k−1), then
    e_2..e_(k−2), wv_1..wv_(k−2), wu_2..wu_(k−2), then y_1, ȳ_1, …, y_(k−1), ȳ_(k−1), then y′_2, ȳ′_2, …, y′_(k−2), ȳ′_(k−2). It is
    NOT level-sorted. The games use the file's order as is: gamma3.build(G, eg195.PADS) and my eng3.build3 take movers in index
    order and options in the order (mover index, option index); β index of option (x, o) is 2x + o (opts[x][o][2]). I did not run
    mover renumberings myself (REFEREE 35's PERM run did: Lead 13:07Z).
  - M-3 (JSON fields). Keys: N, lev (list), deg (the SCALAR 2), opts (opts[x][o] = [W-target mover index or −1, Ξ-target mover
    index or −1 for X, β index]), gate (gate[x][o]), br (β ranks, a permutation of 0..M−1), bp (β parities, all 0), start. There
    are no fields «pi» or «cyc». Say so in an entry on §10.
  - Lead 12:56Z item 3 (later, in a fixes entry): §9's two commits «seen on origin at 12:49Z» are to be replaced by the lanes' own:
    L-COMP's BOX 48 in c4c75222, L-RED's R245 in 706d1ecc (SHAs AS RELAYED by the Lead; I have not fetched them: read them from
    `git ls-remote origin claude/l-comp claude/l-red` / `git log` before writing them).
  - Lead 12:56Z item 5 (one-command reproduction from a clean checkout): DONE with a finding, see fixes entry 1 §10.E: at 350d84eb
    run_b6b.sh needs an ABSOLUTE ROOT and exited 0 on failed stages; fixed in this commit. Clean clone,
    relative ROOT, fixed runner: `gen 10` < 1 s, `n5 10` 406 s for G_3..G_10 (G_3 0.1 s, G_10 248 s), lines equal to the frozen ones
    but for `badstrat 0` and the timings, .pg files byte-equal (data/b6b/out/n5_clean.out).
- (b′) ADDENDUM (Lead 14:00Z, read after the first handover commit 06d399c2 was made; written 14:06Z by date -u). Fixes entries to
  PREPARE and to write only when the referees' reports ask for them (never into the frozen file):
  - Entry 2 (P-1): R117's standing premises [1E-N3], [RULE], [VJ-LOC] in R117's words on Corollary EXP-N5; «the N5 runs at k ≤ 12
    named as premise-free DATA» (Lead). Material in (b) P-1 above.
  - Entry 3 (suggested by L-NEW 77, relayed by the Lead): landed RESULTS R124, Corollary EXACT-L. OPENED by me at trunk 6eaf4604
    (docs/RESULTS.md l. 15371, the entry's title line; the file's sha1 eecbd798b81ad431d1b753f5a7f92f3c63e56da1 is the same as at
    5d7aab0f, so my archive RESULTS.trunk.md already held it and I had not read it). Verbatim there: «N5 (SPEC S1-S5 with its FIX
    1-4 tie-breaks) from S3 on Γ3(G) makes exactly L(G) + 3 iterations» and «N5's iteration count is polynomial in n iff L(G) is
    polynomial in N + M», stated as «(Corollary EXACT-L, PROVED for G ∈ IDEAL-ACYC» with «premise RESULTS R117 (f); it uses SPEC's
    S1 tie-breaks, through REACH3's [RULE] choice», all «under the standing SPEC premise 1E-N3». With Theorem EXP-IDEAL this gives
    EXACTLY 2^k − 2 + 3 = 2^k + 1 iterations on Γ3(G_k), the number both engines measure for k = 3..12. Successor 6 states it as
    Corollary EXP-N5′ with R124's premises quoted (check them with b6quote.py, new tag R124), IF the referees agree (Lead).
    THIS CORRECTS item (d) 8 below, which I wrote before reading R124.
  - A firing control from the first referee's lane (THEIR data, claude/referee 06ac891d as relayed by the Lead, pushing at 14:00Z;
    not opened by me): with the e-indices in reversed gate order the run is 6 iterations for every k = 3..6, so the long run rests
    on S4a's root-first key order. Cite it as theirs, after reading it on origin; it agrees with my §9.10 (a broken listed
    comparison can drop T to 3) and §9.13.
  - P-2 (width 9 for k ≥ 6), M-1, M-2, M-3: as in (b) above.
- (c) N5 AT k = 12: COMPLETE (not to be resumed). Line in data/b6b/out/n5_k12.out (4097 = 2^12 + 1 iterations on both engines, all
  must-0 counters 0; 622 s + 944 s), game data/b6b/pg/G_12_g3.pg sha1 abca6452…, fixes entry 1 §9.12. If k = 13 is ever asked:
  `bash experiments/red-b/run_b6b.sh R n5 13` is resumable per GENOME only (a single k is one process); by the ratio 2.5-2.6 per k
  it needs about 27 + 41 min, which is longer than the usual container life (~40 min): run the two engines as separate tracked
  jobs or do not promise it. L-COMP ran k = 12 on its own builder too (Lead 13:07Z; its DATA, not mine).
- (d) WHAT ONLY I KNOW ABOUT THE PROOF (packet §5-§7).
  1. THE HARDEST STEP is the reading of one IDEAL step that MOVE-2 fixes: a mover x on level ℓ moves iff it is value-enabled under
     the OLD state s (|A_s(x)| = 2) AND key-enabled with the NEW state s′ on the levels below ℓ, read at x's CURRENT option. Every
     «in the same step» of the RESPONSE LEMMA rests on it: v_j moves in the very step in which the pair below changes C_(j−1);
     B moves at step t_1, the step in which E(j+1) moves to 1 (B is one level above E(j+1), so its key sees the new option);
     F′ moves with u_j at t_1 + 1. Every one-step DELAY comes from values being read under the old state (B one step after v_j in
     the top unit; u_j one step after B). A referee who reads the mover's own option from the new state gets kenab ≠ 0 at every
     move: my first b6enab.py did exactly that (fixes entry 1 §9.8 note 1). Answer with §9.3's sched counter and §9.8.
  2. The count: P_(k−1) = 3; a response of unit j ≤ k−2 is [first response of unit j+1: steps t..t_1, P_(j+1) steps, begun in the
     SAME step as v_j] + [second: steps t_1+1..t_2, P_(j+1) steps] + [e_j at t_2+1], so P_j = 2·P_(j+1) + 1 = 2^(k+1−j) − 1. Level
     1 has no e_1, no Y′_1: its response ends at t_2, so L = 1 + P_1 − 2 = 2·P_2 = 2^k − 2 (not 2^k − 1). k = 3 has units 1, 2 only
     (E(2) = u_2, one wire wv_1). These off-by-ones are where I made my own slips while writing; b6lemma.py's tlen / rest
     counters test them on the real run.
  3. V1's «aligned» case is USED by the proof (step t_1 + 1: E_j = [EY_j = c] = 0) but along the run it only ever evaluates to 0,
     which is why a control that drops it is inert (§9.8 note 2). If a referee asks whether the case is dead text: it is needed for
     the lemma's statement that the input of unit j+1 is (0, 0); the DATA cannot distinguish it from the constant 0.
  4. The stop is «stuck», not «opt»: under the last state v_1 is value-enabled and key-disabled (§7 (b)). R117's REACH3 covers a
     «stuck» stop (REFEREE 35's pre-check read it so, Lead 13:07Z); L(G) counts steps either way.
  5. §8's list of ε comparisons is SUFFICIENT, never claimed minimal: about 40% of single violations still give 2^k − 2 (§9.10).
     Never write «necessary».
  6. The static facts need exactly: β ranks Ξ-depth-major, all β parities even (values then compare root-first like keys), wires
     never a Ξ-target (V0), and the wire ε's above the ε's of E(j+1)'s options (K2 / K3). Ablations (§9.6): odd parities (upar)
     T = 2, rank order broken T = 1, no end-follower T = 2k + 2, no wu wire T = 6; WITHOUT the wv wires the run is still 2^k − 2 at
     N = 8k − 14 (DATA only; the proof's K2 uses wv; no proof for that variant: keep it outside the theorem, Lead 12:56Z item 4).
  7. In box 217's vocabulary k(G_k) = 1 (no mover above level 0 switches |K| − 1 times): the brief's target «k(G_k) = k» was NOT met
     in that sense; the kill is by run length and switch counts against N + M (Lead 12:08Z accepted that measure). Say so if asked.
  8. N5's exact count on the DATA is 2^k + 1 = L + 3 iterations (k = 3..12); the frozen Corollary claims only ≥ 2^k − 1 (REACH3's
     «at least L(G) + 1»). CORRECTED 14:06Z: the exact count IS proved elsewhere, by landed R124's Corollary EXACT-L (see (b′));
     the frozen packet does not use R124. Upgrade only through a fixes entry that quotes R124's premises (entry 3 in (b′)).
  9. Other tie rules (§9.13, DATA): xi and idx stop after 7 iterations on Γ3(G_4), Γ3(G_6), Γ3(G_8); seq takes 65 / 154 / 235.
     The family attacks N5's S4a key order and nothing else; no claim about any other rule.
- TOOLS ADDED IN THIS COMMIT: b6enab.py, b6perm.py, b6reach.py (needs the lnew archive), b6n5.py (now with the `badstrat` column
  and control B6N5_CTRL=3; the frozen §9.4 lines were made by the 350d84eb version), run_b6b.sh (absolute ROOT; exit 1 on a failed
  stage command), check.sh (b6enab 6, b6perm 5 with their controls, the fixes1 pins).
- WORK DIR. experiments/red-b/work/b6/ (ignored) held the archives lnew/ (a143d406), lred/ (aa4f7680), trunk/ (5d7aab0f) and
  RESULTS.trunk.md / GAPS.trunk.md; it may be gone in a fresh container: rebuild with the packet's §10 commands (they work from the
  repository root; use an absolute ROOT for run_b6b.sh at 350d84eb). work/b6/tools/ is a STALE copy: the committed tools are the
  record. work/b6/final/ holds helper scripts with absolute paths: never commit them.
- WHO ELSE (as relayed by the Lead, not opened by me): REFEREE 35 (pre-check done from the rule's text, own stack, k ≤ 15 model,
  k ≤ 9 N5; «NO hypothesis of R117's proofs is violated by G_k»; not a signature) and REFEREE-2 41 referee the packet; L-SI 56
  writes an independent proof from the rule alone and does not read mine until its own is committed («If the two proofs disagree
  anywhere, both lanes hear from me at once»); L-COMP 22 (C port to k = 20; n5b on its own builder) and L-RED 70 (R245 «SURVIVES»)
  rebuilt the family. L-RED's R243 / R245 may be read now (my verdict is written).
- NEXT for successor 6: (1) handover check as the Lead's brief says; (2) wait for REFEREE 35's and REFEREE-2 41's reports on
  origin, then answer item by item in fixes entries (2, 3, …), each saying whether a statement, proof or hypothesis changes;
  (3) if L-SI's proof disagrees with §6 anywhere, run b6lemma.py / b6enab.py on the disputed step first and report the counter.

**SUCCESSOR 5 (Fable 5.2, xhigh, session_01V5yGRXFf3kFNfkycCHTnLT; started 2026-11-13 11:29Z by date -u; handover check 4cbabe14;
«go» from the Lead 12:17Z; EARLY START under D25 while 1fbd6d0d was still pushing).**
- B6 attempt 2 (KILL attempt on QUIET-KEY-1P by construction) SUCCEEDED as a CANDIDATE. Packet docs/red-b/P-N5-EXP.md (statement,
  rule R, proofs, DATA; name fixed by the Lead), lane report docs/red-b/B6b-construction.md (verdict, record, how it was found,
  dead ends). Theorem EXP-IDEAL (PROVED lane, UNREFEREED): the rule G_k gives a genome of R104's class, Ξ-acyclic, N = 9k − 16,
  M = 2N, k + 1 levels, every degree 2, with L(G_k) = 2^k − 2 and every mover of unit j switching 2^(j−1) times. Corollary EXP-N5
  (by landed R117 REACH3): N5 from S3 on Γ3(G_k) (n = 135k − 230, m = 176k − 300) makes at least 2^k − 1 iterations, so the claim
  «N5 runs in polynomial time» is FALSE and G-N5-TIME is answered NO (wording fixed by the Lead 12:43Z C3).
- DATA (data/b6b/, pinned in data/b6b/SHA1SUMS_b6b): membership 0 violations on G_3..G_14 with 8 firing controls; three model
  simulators (mine, L-NEW's one217, L-RED's r187/ideal.traj) state by state to k = 14; the proof's own schedule equal to the real
  run step by step to k = 14 (b6lemma.py, counters kfact / vfact / sched / tlen / rest / swk all 0, 2 controls fire); N5 itself on
  two engines (n5v spec, n5b spec) with two Γ3 builders (gamma3.build and my eng3) to k = 11: 2^k + 1 iterations, first fallback at
  2^k − 1, wrong 0 against Zielonka, 3 controls fire; fits with residual 0 against the closed forms; ablations.
- Status under D1: a KILL CANDIDATE, «lane DATA on the model» + a lane proof, until both referees sign and CHECKER passes (Lead
  12:17Z item 5, 12:43Z). REFEREE 35 and REFEREE-2 41 were waiting at this writing; L-COMP 22, L-RED 70 (R245: SURVIVES) and the
  Lead rebuilt the family independently from my generator text (their DATA, cited in the packet §9, not opened by me).
- Tools (experiments/red-b/, none needs another lane's archive except b6sim.py and b6n5.py): gk.py (the rule; --raw for the first
  version's gate numbering), onep.py (own IDEAL / 1P simulator), b6member.py (R104's clauses, --norm, --quote, 8 controls),
  b6sim.py (three simulators), b6lemma.py (the proof's direct test), b6n5.py (N5 on Γ3: n5v + n5b + Zielonka + own builder),
  b6fit.py, b6size.py (sizes and the first k beyond n^c), b6quote.py (verbatim quote check), gkvar.py (ablations), bilad.py (the
  dead-end family), run_b6b.sh (resumable runner; archives per packet §10 into work/b6/, which is ignored and does not survive a
  fresh container).
- NEXT: answer the referees on §4-§7 of the packet (press points in its §11); if asked, N5 at k = 12 (about 25 + 40 min, resumable:
  run_b6b.sh R n5 12) and a proof for the leaner «nowv» variant (8 movers per level, T unchanged on DATA). L-RED's R243 / R245 may
  now be read (the verdict is written).

**SUCCESSOR 4 HANDOVER (written 2026-11-13 ~09:25Z by date -u; for successor 5).**
- B5 DONE (docs/red-b/B5-second-fb.md §1-§7): ONE-FB FALSE (dead end, NULL fallback instance data/b5/null2_s5101_i313_n3.pg sha1
  8be02077) → ONE-FB′ (k ≤ 2 on every gscan104 Wg; UNREFEREED; Lead: not routed to a referee). Records on origin: 8854d85d (correction),
  4065efc0 (tools), 18dd585f (wrap-up; push started ~09:11Z — CHECK `git ls-remote origin claude/l-red-b` before quoting it).
- B6 (QUIET-KEY-1P / O1, Lead 09:08Z; owner relayed «So put everything into trying solving it today»): attempt 1 written in
  docs/red-b/B6-quietkey-1p.md §1-§4. Three classical embeddings fail for clean reasons: Disser-Loho-Maat-Mosis arXiv 2512.16684v2
  Lemma 4.4 G_n (N5 linear on it, data/b6/b6gn.out), its Thm 4.3 (single-switch class), and Zhong-Ye arXiv 2609.40147v2 (cycles). Lemma
  ACYC-GREEDY (proved, lane): value-greedy rules are optimal after h steps on acyclic one-player games. DATA data/b6/b6acyc.out (0 viol;
  the control fires for n ≥ 40), b6simul (SIMUL-BLAND climbs: no long runs from random local search).
- Box 217 LANDED (Lead 09:53Z): claude/l-new a32a588d, docs/new/N5-QUIETKEY-box217.md + experiments/new/box217/one217.py (rules key /
  howard / seq). Lead's target for B6 attempt 2: ENUMERATION DEPTH k = 8 (box 217 A6; towers stop at k = 7 = HIT7) by a designed carry
  chain / Gray code, or a TIMING reason why k = 8 is impossible (L-NEW's A7′: counting alone cannot cap it). Read box 217 §1, §5 and
  docs/lower/P-TOWER-FUEL.md (PULSE / GAP) first; L-LOWER L16 runs SAT screens on the same target (do not duplicate).
- Next ideas: a designed doubling on the per-level pair automaton (𝓛^R_d with Ξ-targets as «fuel», see HIT7's format: opts[x][k] =
  [W-target, Ξ-target, gate]; values flow on the Ξ-DAG, keys on the W-ladder); do NOT duplicate L-LOWER's SAT search (claude/l-lower
  L16 P16 screens); read docs/lower/P-TOWER-FUEL.md first.
- One-player N5 climbs (B5 §6, b5one.py): I ≈ 0.9 n on cyclic one-player games, n ≤ 64 (d3: n48 45, n64 43; d5: n6..n32 7, 9, 14, 18,
  29, 32); runner run_b5d.sh was stopped at n48_d5 (resumable).
- Sources opened this session: arXiv 1106.0778v2 (PDF sha1 a63a9293; Thm 3.2, p. 5-6), 2512.16684v2 (8629b38e; Lemma 4.4, Thm 1.1,
  4.3, §2), 2609.40147v2 (72974eb2; Thm 2.1, 6.1, §2 figure text). PDFs in the session scratchpad only (not committed).
- Traps this session: (1) my own lemma was false: always run the direct test before telling the Lead it is proved; (2) a message time
  stamp typed by hand was wrong (09:20Z vs 09:11Z): take every stamp from date -u; (3) three CPU jobs at once happened for a minute (I
  killed one): count verify as a CPU job.

**SUCCESSOR 4 (Opus 5.5, session_01V5yGRZixRCf3PLfDhttq7S; started 2026-11-13 06:14Z by date -u; handover check 28823167 on origin;
«go» from the Lead 06:56Z on B5 plan (1)-(3)).**
- B5 (SECOND FALLBACK): report docs/red-b/B5-second-fb.md; tools b5lemma.py (direct test, counters + controls CTRL=1/2/3, FREE, MIRROR),
  b5climb.py (climbs outside W: FREE Odd faces; objectives p1 / k / its), run_b5.sh (lemma | climbs; resumable; outputs work/b5/).
- FINDING: Lemma ONE-FB («k = 1 on every Wg», draft 2afb3f11) is FALSE (my test, 07:10Z; Lead told 07:16Z): NULL second fallback at the
  last iteration, 15/1,500 (high) and 12/1,500 (low) random Wg. Corrected ONE-FB′: k ∈ {1, 2}; a second fallback only switches NULL
  edges (v the cycle node of both values), leaves Ξ unchanged, ends the run. Proof step (v.2) rewritten without [F11] Thm 3.2.
- Lead 06:56Z: ONE-FB not routed to a referee (lane lemma, UNREFEREED, premise 1E-N3); climbs outside W aim at P1 / I, not k; growth words
  only with fits; Lead wants «the B5 record SHA».
- Archives rebuilt in experiments/red-b/work/b3 (fresh container had none). Old (uncorrected-counter) lemma outputs in work/b5_old/.
- B5 WRAPPED UP 09:2xZ at the Lead's re-target (owner, via Lead 09:08Z: «So put everything into trying solving it today»): §1-§7 of
  docs/red-b/B5-second-fb.md; NO CANDIDATE KILL; ONE-FB DEAD END -> ONE-FB′; climbs outside W partial (P1 ≤ 33), 51 bests verified on n5b;
  one-player N5 climbs I ≈ 0.91 n + 3.3 on n ≤ 32 (DATA). Origin before this commit: 4065efc0 (8854d85d = correction record).
- NEXT = B6 (Lead 09:08Z): second independent kill attempt on QUIET-KEY-1P (O1): N5's key rule on L-NEW's one-player model 1P(G)
  (claude/l-new box 217, one217.py; e-index keys per L-RED R241). NOT on origin at 09:15Z (searched every remote branch): ask the Lead.
  Method: cross-domain (D18): key rule as a pivot rule on a deterministic one-player lexicographic shortest-path problem; embed a known
  exponential construction (Friedmann [F11] counters, Melekopoglou-Condon, Klee-Minty-type cubes for lexicographic rules); cite only
  opened sources; test on one217.py and n5v. b5one.py already runs N5 from S3 on one-player games (no key model).

**SUCCESSOR 3 HANDOVER (written 2026-11-13 ~04:45Z by date -u; park after the B4 report's push and the final message).**
- B2 (box 209): DONE, verdict NO KILL (docs/red-b/B2-box209.md, 7247a639). B3 (GUIDE-RULE): DONE, NO KILL (docs/red-b/B3-guide.md,
  9bce72fa + §3a R240 / amended FLAT-IDX d4e16fc1 + Addendum A d889e559, eb28fde5, 4b8f650a, cb98decb). FLAT-IDX routed by the Lead to
  L-NEW box 213 as «L-RED-B reading, not proved» (L41); R240 (L-RED 68): DEPENDS ON NUMBERING; numbering-free form = WRAP Remark (3).
- B4 (POST-FALLBACK, docs/red-b/B4-postfb.md): statement + DATA (a) on origin (eb28fde5). B4 (b) climbs DONE (work/b4c_*.out; P1 best
  per n: switchallexp 19, 14, 15, 20, 24; LMCS 10, 14, 16, 18, 19; H_n 12, 18, ≥30, 33; k = 1 always, 0 wrong). IN FLIGHT at this
  writing: b4phase on the climb bests (work/b4phase_climbs_spec.out, both engines) and run_b4own.sh (own guides at larger n: H_n 6, 7;
  switchallexp, LMCS 7..10) testing the 5-point fits. Next: B4 §6 with those, data/b4 pins, push, message the Lead (B4(b) results).
- Lead's wording rules (01:33Z, 03:56Z): growth words only with a fit (model, coefficients, residuals, n range), else «growth not
  identified»; a k-parameter fit to few points is DATA, not a formula; budgets per row; claims labelled «L-RED-B reading, not proved».
- Archives for B3/B4 in experiments/red-b/work/b3/ (ignored, survives restarts): lnew (claude/l-new 069c888b), lred (claude/l-red
  2d290a15), lsi (claude/l-si 2051a0ee), llit (claude/l-lit 5c53efbd), lcomp (claude/l-comp aa863db5), trunk (7fa6aff4 n5b,
  hard-families, harness); rebuild commands in docs/red-b/B3-guide.md §6.
- Push hygiene: verify takes ~45 min; container restarts every 25-60 min have killed 2 pushes (re-run push.sh as a tracked task; check
  `git ls-remote origin claude/l-red-b` before telling the Lead anything is on origin). Tracked tasks die at 2 h: every runner here is
  resumable (skip-if-done; climbs keep a state file in work/).

**SUCCESSOR 3 (Opus 5.5, session_01V5yGRXHoHifjbeqR3Lntn5; started 2026-11-12 20:00Z by date -u). «go» from the Lead 20:06Z, effective
at the push of d19af5df (exit 0, 20:47:58Z).** Successor 2's 8d5d8388 is lost (not on origin); its tools are rebuilt from scratch.
- B2 (box 209) DONE (verdict NO KILL; every statement SURVIVES; E-DOM's use VALID; notes N-1 (P2) citation, N-2 tie-rule
  dependence of T3, N-3 n_E3 wording): docs/red-b/B2-box209.md, evidence data/b2/ (pinned). Tools: eng3.py, xcheck3.py, lev3.py,
  sweep3.py, n5xi3.py, climb3.py, edomctl.py, run_b2.sh; gate checks in check.sh. Not run: exhaustive (1,6), (2,5); (3,4) partial 8.8M.
- B3 (GUIDE-RULE on N5): report docs/red-b/B3-guide.md, data/b3/ (pinned). NO CANDIDATE KILL; growth not identified (fits stated);
  claim FLAT-IDX (L-RED-B reading, not proved; proof sketch §3; direct test 0 on 4,020 N5 runs, control N5'-xi fires). Still running
  at the commit: run_b3b.sh (1,500-step H_n climbs n = 3, 4): report them in an addendum. Lead's three requirements (01:33Z): fits or
  «not identified», FLAT-IDX labelled + lemma + test, budget per row: all in the report.
  Archives in experiments/red-b/work/b3/ (ignored; rebuild per gclimb.py / B3-guide.md §6).
- B3 after B2: n5v spec mode + L-SI box104 guide tools (2051a0ee) via git archive; SPEC = docs/new/N5-ssi-global.md «## SPEC» l. 23-62.

### (session 1 resume point, kept as history)
**SESSION 1 HANDOVER (written 2026-11-12 17:07Z by date -u; PARKED after this commit's push and the final message to the Lead).**
- BOX 208 IS CLOSED FOR THIS LANE. Final verdict (report docs/red-b/B1-box208.md §0; sent to the Lead): no kill. Lemma LEVEL, Theorem
  WIN, Corollary R-INT, Theorems R-HEIGHT, K1-TCYC, FVS-TCYC, ALL-TCYC and §10 ABS SURVIVE the proof read and my engine; Lemma PLATEAU
  SURVIVES with write-up gap G-1 in (P6) step (ii) (repair: F3 at the gate + ext(g, ·) injective by CN2 + NO-TIE; K2 by LOC-K2); notes
  N-1, N-2. The Lead relayed G-1 to L-NEW 72 and is freezing box 208 + Addenda A, B as packet P-N5-LEVEL (Lead 14:14Z).
- All planned runs are DONE and committed in experiments/red-b/data/ (pinned in data/SHA1SUMS; check.sh verifies the pins): engine
  validation, 78 frozen genomes (all refs, three tie rules), WIN counters, ABS, every tie-breaking branch, controls, exhaustive
  (1,1) … (1,6) = 42,352,796 genomes, 5.9M random genomes, 1,200 mutants, 26 climbs. Every must-0 counter is 0; every control fires.
- No CPU job is running. No push is running when this is read unless `pgrep -f "bash scripts/push.sh"` says so (the push of this commit
  was started as a tracked task; if the session died first, re-run `bash scripts/push.sh` as a tracked task with a 2-hour timeout:
  the gate takes about 70 minutes).
- NEXT OBJECT FOR THE SUCCESSOR (Lead 14:45Z and 17:08Z): BOX 209, claude/l-new 3f8960998427db1f67daab4d7fdab210344643cc,
  docs/new/N5-LEVEL3-box209.md (sha1 94356803…, measure it), the Γ3 form: on HOW3(G) on Γ3(G) (N5′-xi from S3 up to its first fallback),
  LEVEL3 (Φ takes ≤ P3 = 2M(N + 4M) values), PLATEAU3 (a plateau and the final tail each ≤ n_E3 = N + 6M + 9 steps), T3-ALL (T3 ≤
  P3(n_E3 + 1) + n_E3), N5XI-G3 (exactly T3 + 3 iterations of N5′-xi). Premises named by the Lead: R117, R104, R125, R15 (a), R121 E-DOM,
  R118 (i), R124. Also WRAP's (W4) (the Lead's 17:08Z message names it; I have not seen it: ask the Lead for its SHA).
  I HAVE NOT OPENED BOX 209. Nothing below is a finding about it.
  - Stance: assume it is false; own Γ3 / HOW3 engine (NOT the lane's gamma3.py); independent of L-RED 66, REFEREE, L-COMP on box 209.
  - The Lead's pressure points for box 209: pads pA, s, q, r, pe_g, pβ_g, pb_g and the mover pads m_(x,k) (priority 2 for the genome
    start, 0 otherwise); K2 / LOC-K2-3; CORE-ABOVE in place of E-DOM; REACH3-ALL / [STD3]; the fallback; the author's own list (§8 of the
    box): (K2′) / (K0′) at the pads pb_g, (L2′) at pe_g, (P4) case (3) and the reading (D1′), BR-SEG-G on H, PLATEAU3 (ii), the tie-rule
    step of N5XI-G3. Lead: «L-SI 52 reports that on F_n (E-DOM dropped) N5′-xi is exponential. So E-DOM must be used somewhere in box
    209; find exactly where, and check that the use is valid.»
  - What carries over from box 208 (my reading; check each on Γ3): the whole argument rests on «Odd's choice at a gate is a function of
    the two face classes» ((K2) + LOC-GATE + NO-TIE; at equal classes the e-face, by (D1): e_g's only in-edge is from g). On Γ3 the
    in-edge of e_g is from the pad pe_g, exact VJ ties exist (R118's DATA: IDEAL-CYC and Γ3 runs diverge at ties), and N5′-xi has its
    own tie rule (SPEC's choice, then the larger index), so NO-TIE3 and the tie step are the first places to press.
  - How to start fast: eng.py builds Γ(G) from a genome dict (same JSON format as the fleet's frozen genomes); a Γ3 builder = that plus
    the 4M + 4 pads of R117 (read docs/new/P-N5-REACH.md §3 for indices and priorities; I did not). lev.py's counters work on any
    history of states {sig, sbar, val, lam, pim, kk} once `kind`, `succ`, `owner` are set for the pads; win.py, press.py, ties.py,
    sweep.py, climb2.py, gen.py (random shapes, exhaustive enumerator with part / parts), mut.py are reusable as they are.
- Rules that cost me time: a push takes ~70 minutes in the gate; never commit while it runs; the repository's root .gitignore ignores
  experiments/*/out/ (use data/); a session stop hook complains about uncommitted files, so long jobs should write into work/
  (ignored) and be moved to data/ just before the commit; messages from the Lead can arrive more than an hour late (read them with
  the notifications tool as soon as a notice appears).

## Queue
1. (successor) Start check per CLAUDE.md / the Lead's brief; measure box 209's sha1; read it and its premises (R117, R124, R125).
2. (successor) Own Γ3 / HOW3 engine + brute-force check + T3 comparison with the box's outputs (as data), then counters and attacks.
3. (successor) Verdict per lemma to the Lead; park at ~450k.

## Sources opened
- claude/l-new a143d4060d75f8463fe098b6ce18eef3febcd14b docs/new/N5-QUIETKEY-box217.md (all 236 lines) and
  experiments/new/box217/one217.py (all): read 2026-11-13 (successor 5). Trunk 5d7aab0f docs/red/P-N5-REALIZE.md §2 (R104's
  definitions of the genome, IDEAL-ACYC, the values, the IDEAL step, L(G)) and docs/RESULTS.md l. 13362 (R117: REACH3,
  REAL-IDEAL-S3), title lines of R113, R120: read 2026-11-13. claude/l-comp experiments/comp/box29 tower genomes (DBL4, H5, H6,
  RECF4, HIT7): read as data. Not read: L-RED's R243 / R245, L-COMP's box 47 code, any arXiv / DOI source this session.
- trunk docs/RESULTS.md R104 (l. 9864), R118 (l. 13607): read 2026-11-12 (title lines; definitions of the genome, Γ(G), IDEAL-CYC).
- docs/new/P-N5-XICYC.md §1-§5 and docs/new/P-N5-XICYC-fixes.md entries 1-3 (R118's packet: IDEAL-CYC, Howard step, F1-F6, DOM, STRICT,
  PATH, BR-SEG, BR-SEG-G with its repaired proof STRICT-G / PATH-G): read 2026-11-12.
- docs/red/P-N5-REALIZE.md §1-§3.3 (R104's packet: genome, Γ(G) vertex by vertex, priorities, start): read 2026-11-12.
- claude/l-new 8db300fe docs/new/N5-LEVEL-box208.md, all 502 lines: read 2026-11-12.
- claude/l-formal 9dde1527 lean/lemmas/PGLemmas/Statements.lean and Defs.lean (BrSegGStatement, BrSegStatement, LamGapSharpStatement,
  HowardAt, Val.lt): read 2026-11-12. trunk docs/RESULTS.md R117, R123, R126 title lines: read 2026-11-12. claude/l-new 8db300fe
  docs/new/N5-RLOCAL-box207.md l. 48-49 (λ(W)): read. L-LIT T69 (cited by the Lead for the pressure points): NOT read.
- No external source (arXiv / DOI) opened yet. VJ00 and Friedmann arXiv 1106.0778 are cited by R118 as premise [VJ]; I use the order
  as R118's packet states it and have not opened the papers myself.

## Dead ends
- (successor 5, B6 attempt 2) Anti-aligned 2-wide ladders (Ξ-target one level up, depth-major ranks): T ≤ 6 on 20,000 random
  depth-6 instances (data/b6b/bilad_d6.out); obstruction: between two decisions of a lower pair the levels above return to the
  same state, so no value order above can alternate (docs/red-b/B6b-construction.md §3, dead ends 1-3; ablations §9.6 of
  docs/red-b/P-N5-EXP.md: without the wu wires T = 6, without end-followers T = 2k + 2, follower parallel T = 2, ranks reversed T = 1).
- None yet (no statement of box 208 killed; attacks tried and why each fails: docs/red-b/B1-box208.md §5).

## Things only I know
- (successor 5, 13:54Z) Raw and of-record genomes give the same model run: `cd experiments/red-b && python3 -c "import gk, onep;
  [print(k, [tuple(x) for x in onep.OneP(gk.build(k)[0]).run('key')] == [tuple(x) for x in onep.OneP(gk.build(k, raw=True)[0]).run('key')])
  for k in range(3, 13)]"` printed True for k = 3..12 (and the two genomes differ in the field `gate` only).
- (successor 5) run_b6b.sh trap: at 350d84eb a RELATIVE ROOT fails in the gen stage (cd before the write) and the runner still exits 0;
  fixed in the handover commit (absolute ROOT; exit 1 on a failed stage command). Always read the last line («failures 0»).
- (successor 5) The IDEAL model is a boolean asynchronous network: with β-ranks ordered by Ξ-depth and all parities even, a value
  is compared root-first exactly as a key is, and every degree-2 mover is a two-input latch (P-N5-EXP Lemma MOVE-2). That is what
  made the construction possible; it is also the quickest way to read any genome's run.
- (successor 5) experiments/red-b/work/ does NOT survive a fresh container: the archives (lnew, lred, trunk) must be rebuilt per
  docs/red-b/P-N5-EXP.md §10 before any run that needs another lane's tools; gk.py, onep.py, b6lemma.py, b6member.py, gkvar.py,
  bilad.py, b6fit.py, b6size.py, b6quote.py need no archive.
- (successor 3) bash reads a running script incrementally: editing run_b3.sh while `run_b3.sh fam` ran made that runner go on into
  the newly added fam2 jobs. Never edit a runner that is running; add a new file instead.
- (successor 3) Container restarts (one at ~00:15Z on 11-13) kill tracked tasks and the push; experiments/red-b/work/ SURVIVES (it is
  inside the repo checkout), /tmp scratchpad files did too. Every runner here is resumable (skip-if-done; climbs keep a state file).
- (successor 3) gverify.py: n5v (spec) and n5b (L-COMP, --mode spec, own best-reward start) agree on the guided wrappers tried.
- My engine's e-priority order is P-N5-REALIZE §3.1's (by (lev(owner), gate index)). The optional genome key "eorder" (mine, tests only)
  replaces it by an arbitrary order; box 208 says [E-LEV] is not used, and 30,000 such genomes gave 0 violations.
- Exhaustive tiers with M = N are vacuous for LEVEL (every mover has one option, T = 0). The first non-trivial tiers are M ≥ N + 2.
- The root .gitignore ignores experiments/*/out/: my outputs live in experiments/red-b/data/ (first commit fbb6a062 went out without
  them for that reason; the next commit adds data/).
- A gen.py bug I made and fixed before any output used it: the loop variable `part` shadowed the chunk parameter (chunks came out
  empty after the first group). The outputs data/exh_* of set D were produced by the unchunked code (checked: counts equal the formula).
- Howard ties (several best gates, current one not best) are rare on the frozen genomes (2 in 78 runs) and common on small random
  genomes; the tie rule is a parameter of eng.howard_run ("keep-low", "high", "rand").
- The Python engine does about 6,000-7,000 tiny genomes per second with all reference states; (N, M) = (2,5) has 294,865,920 genomes
  and is not run exhaustively.
