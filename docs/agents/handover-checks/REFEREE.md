# Handover check: REFEREE

## successor 36 (2026-11-13T14:44Z by date -u; predecessor successor 35, HANDOVER NOTE in notes/REFEREE.md at 06ac891d)
Measured from the repository at the time of writing, not recalled. The model label is left out of repository files (the Lead's brief:
no model name in commits); the Lead's brief names it.

### 1. Branch, head, distance to trunk
- Trap check at the start (13:59Z): the local branch was claude/referee at 890daf41, 185 commits behind origin (stale container);
  `git fetch --unshallow` (not shallow), fetch of claude/referee and trunk, `git merge --ff-only origin/claude/referee` to
  ef22a8d11c541d4fc0d76a8720afb23d03574e34, origin's head at that time.
- EARLY START clause kept: no commit and no push before 06ac891d was on origin. A watcher on `git ls-remote origin claude/referee`
  reported the move at 14:42:42Z; then `git merge --ff-only`: `git branch --show-current` = claude/referee and HEAD =
  origin/claude/referee = 06ac891df6f6212bac74259863da3105e7fe4341 (the commit that carries successor 35's HANDOVER NOTE and
  docs/referee/R-GK-precheck.md; both read).
- At 06ac891d: `git rev-list --left-right --count trunk...HEAD` = «1 4» (behind, ahead) against trunk claude/vibrant-johnson-nxvvxo
  6eaf460475effc5f27d6d2a02d3d80ffe7f0714f, merge-base 5d7aab0f. Trunk is NOT merged in this commit, so that this push changes
  docs/agents/ only (Lead reading L56); a normal merge of trunk goes with the first report push.
- Clock: local `date -u` Fri Nov 13 13:59:49 UTC 2026 against «date: Fri, 13 Nov 2026 13:59:49 GMT» of a raw.githubusercontent.com
  response in the same command: skew 0 s (to the second).
- No push running (`pgrep -af "bash scripts/push.sh"`: nothing). Working tree clean before this file (`git status --short`: 0 lines).
- rate_limit_info (get_session on this session, 14:23Z): isUsingOverage false, rateLimitType seven_day, status allowed_warning,
  resetsAt 1795035600; session_context.model and last_served_model as the Lead's brief names them, effort_level xhigh.

### 2. Open work and next step of each (the Lead's WORK order; «go» is given in advance, effective when this file's push exits 0)
- 1. FIRST REVIEW of packet P-N5-EXP (claude/l-red-b 350d84eb; docs/red-b/P-N5-EXP.md sha1 c0449b17193f19619f33b366096762dfde27d542,
  569 lines, measured; gk.py 5222f555…, B6b-construction.md 960ddf06…, measured). State: the packet is read in full; every
  statement re-derived on paper; own tools written during the wait, in the session scratchpad, NOT in the repository yet (own
  transcription of the §3 table, own IDEAL step from P-N5-REALIZE §2, tests of MEMBER, K1-K4, V0-V4, MOVE-2, WIRE on run states, random
  states and all states at k = 3, 4, an abstract unit machine, the RESPONSE LEMMA's schedule with (H1), (H2) at every invocation,
  §8's orders, quotes); preliminary verdicts and items E-1..E-7 sent to the Lead at 14:23Z (not a signature). Next, after «go»: (a)
  copy the tools to docs/referee/scratch/, regenerate every log from there; (b) the N5 side on this lane's engine (successor 35's
  gk_gamma3.py / gk_reach.py / rl_engine.py), with new firing controls for its not-controlled list (TAU, AV, W, WIN and the others
  named in the HANDOVER NOTE); (c) commit docs/referee/R-P-N5-EXP.md in stages; (d) only then read L-SI's box 108 and compare; (e)
  the lane's fixes entries when they are on origin.
- 2. FIRST REVIEW of packet P-N5-KEY1P (claude/l-new 44775605; docs/new/P-N5-KEY1P.md sha1 f7191623e9ee212fa127c7e4a224f7ab9d689156,
  321 lines, measured). State: read on paper during the wait; own checker of IDEAL-1P, Lemma 0, A1-A4, ENUM-NEC written (scratchpad).
  Next, after item 1's report is committed: the N5 side of RED-1P on this lane's engine, then docs/referee/R-P-N5-KEY1P.md.
- CHECKER items on R128 / R129 / R130: nothing in hand.

### 3. docs/GAPS.md rows relevant to me (trunk 6eaf4604)
- REFEREE owns no row. The row the two packets feed: G-N5-TIME (line 11; severity major; owner «L-NEW (L-LIT T22; referees later)»; status
  open). P-N5-EXP's dead-end paragraph would answer it; changing the row is the Lead's, after both signatures and CHECKER.

### 4. Three owner rulings that most constrain me (verbatim, docs/DECISIONS.md at trunk 6eaf4604), with DECISIONS-INDEX status
1. D1 (index: active; DECISIONS.md lines 7-8):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never downgrade the referee to save money.
   (The Lead's brief applies the same standard to a kill. Lead reading L43, index: active: «DEAD» needs a refereed proof or an
   instance beyond an explicit bound. L43 is a Lead reading, not owner words.)
2. D18 (index: active; DECISIONS.md line 333):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
3. D25 (index: active; DECISIONS.md line 541; owner, direct message to the Lead, 2026-11-13):
   > So put everything into trying solving it today
   (with D24, index: active, line 538: «do xhigh». D26 is quoted in the Lead's brief to me, «I hit my usage limit while you were
   working, but it has reset now. Please continue from where you left off.»; it is not in docs/DECISIONS.md at trunk 6eaf4604 by
   my grep, so I cite it from the brief only.)

### 5. One trap that bit this lane, and the check that prevents it
- Trap (s27-s36): stale local branch (185 behind at this start). Check: fetch, ff-only, `git branch --show-current` and `git rev-parse HEAD
  origin/claude/referee` equal before any commit or push.sh (done twice: at the start and after 06ac891d landed).
- Trap (EARLY START): a commit made before the predecessor's push lands forks the branch. Check: nothing was written inside the
  repository until `git ls-remote` showed 06ac891d; every tool and draft of the wait is in the session scratchpad.
- Trap (s34): a SHA sent in the same tool batch as its commit. Check: send_message is never in the batch of a git commit.
- Trap (s34, s35): a restart or an HTTP 503 leaves origin behind although push.sh printed exit 0. Check after every push: `git ls-remote
  origin claude/referee` against the SHA.
- Trap (s32 G-P6; named by successor 35 for this packet): an induction run past the interval its lemma was proved on. It is in
  P-N5-EXP: the RESPONSE LEMMA is applied to unit j + 1 before its (H2) is known on its whole interval (my item E-2), and (H2) is
  vacuous after the stop (E-1). Check that found it: for each inductive step, write which states the cited fact was proved for.
