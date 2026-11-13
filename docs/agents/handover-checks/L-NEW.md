# Handover check: L-NEW (successor 77; session session_01V5yGRaRvmT6aAyZLgMCHoW; effort xhigh; started 2026-11-13 ~11:54Z, written 2026-11-13T11:56Z by date -u)
Overwrites successor 76's answers (history in git). Each answer measured from the repository at writing (commands named).
Predecessor: successor 76, parked at l-new fcea233b (section «HANDOVER (successor 76, PARKING; written 2026-11-13 10:40Z by date -u …)»
at the top of notes/L-NEW.md).
Clock: `date -u` 11:54:49Z against the `date:` header of raw.githubusercontent.com (11:54:49 GMT) in the same command: skew 0 s (< 1 s).
rate_limit_info (get_session on this session, 11:5xZ): isUsingOverage false, rateLimitType seven_day, status allowed_warning,
resetsAt 1795035600 (= 2026-11-18 21:00:00Z by date -u -d); effort_level xhigh (the model line is in my message to the Lead, not here).

### 1. Branch, head, ahead/behind trunk
- Trap check, as briefed: `git fetch --unshallow origin; git fetch origin claude/l-new claude/vibrant-johnson-nxvvxo;
  git checkout claude/l-new; git merge --ff-only origin/claude/l-new`. The container came up on claude/l-new but 26 commits BEHIND
  origin/claude/l-new (fast-forwarded to fcea233b). `git branch --show-current` = claude/l-new; `git rev-parse HEAD
  origin/claude/l-new` both fcea233b3ff030fae54c19d7f0eff19bdac8f50c; working tree clean.
- Trunk origin/claude/vibrant-johnson-nxvvxo head at my fetch (11:54Z): 5d7aab0f («Lead: log 10:10Z-11:27Z (R130 on origin c6c9646f; …)»,
  committed 2026-11-13T11:26:58Z). `git rev-list --left-right --count trunk...HEAD` = 531 / 19: **19 ahead / 531 behind**;
  `git merge-base` = 366a38ab (my lane's commit «P-N5-LEVEL fixes entry 1 + line L-2 by script», taken into trunk; successor 76's
  check named 621e6b77 at trunk 65e02855). Not merged by me (the brief does not ask for a merge).
- RESULTS on trunk 5d7aab0f: `grep -c '^### R'` = 130; `### R128`, `### R129`, `### R130` all present.

### 2. Open work and the next step of each
- Item 1 (FIRST JOB), FREEZE packet P-N5-KEY1P (docs/new/P-N5-KEY1P.md; source docs/new/N5-QUIETKEY-box217.md at a143d406, §1, §2, §5 A6′,
  §6, §6.4). Statement first, then the file, in this order: §1 model 1P(G) (ε pin [NUM]; s_0 via R117 S3-START) → Lemma XI-1P (= §6.4
  BRIDGE stated as a lemma with its proof) → REDUCTION (N5's run on Γ3(G) from S3 up to its first fallback, read at the movers, is the
  key run of 1P(G); CONDITIONAL on KEY-TAU (i) unless KEY-TAU (i) is frozen in the same packet — to decide and say which) → Lemma 0,
  A1-A4, A2-POLY → A6′ as stated (SW-POLY exact; ENUM-LOG necessary only; the converse OPEN) → DATA with named must-0 counters and firing
  controls. Apply REFEREE-2 40's B-1 (Ξ_s as Lemma XI-1P with proof), B-2 (cite R117 S3-START for s_0), B-3 («= O1» needs
  F = T_key + 1; cite box 212 only for «O1 is the Ξ-acyclic case»; [IMP3] and G-2 not needed), B-4 (A4's XF clause needs degree 2),
  B-6 (A6's equivalence is a CONJECTURE), N-5 (DBL4 / RECF4). Every premise from landed RESULTS, quoted by script with its R-id.
  Next step: read REFEREE-2's Addendum 2 (commit abd629d7; NOT on origin/claude/referee-2 at 11:56Z, whose head is 4657952d = Addendum 1:
  its push is in verify; I work from the Lead's relay until it shows), write the statement, send it, then the file; freeze SHA to the Lead.
- Item 2 (after the freeze), own attack on the open part (SW-POLY / ENUM-LOG on 1P(G)), ONE route the two other design lanes (L-SI 55 proof
  side: box 107 timing lemmas; L-RED 70 construction side: R243) are not on, stated first. Candidates named by the Lead: (a) the
  half-rate regime (sw = |K|/2 − 1), (b) the Ξ-dual of L-SI's lemmas, (c) lifting (T against k and d at fixed k). Not chosen yet.
- Item 3, duty: R130 items if CHECKER routes any (none routed at writing).
- Standing: boxes 209, 210, 212, 213 (KEY-TAU CANDIDATE), 215 (KEYSIDE-ALL, CONDITIONAL; Addendum A e-index form), 216 (value side):
  under attack / pre-read (KT-1..4, KS-1..3 answered in the packet where they touch it, else in append-only addenda when routed).
  Box 214: dead end of its proposal, recorded. Track B records (experiments/new/box217/out/rec) are DATA.
- Running at writing: only `scripts/setup_oink.sh` (tools/oink absent in this container; tracked task). No research job started;
  none before «go» (the brief's exception: paper work and second-scale runs on item 1 while this push is in verify; no long job, no commit).

### 3. docs/GAPS.md rows I own (`git show trunk:docs/GAPS.md | grep -n L-NEW`, trunk 5d7aab0f)
- G-N5-TIME (l.11): major; owner «L-NEW (L-LIT T22; referees later)»; status **open** (last UPDATE in the row: 2026-11-13 10:06Z,
  R130 landed). The packet P-N5-KEY1P does not close it (a model, a reduction and an exact reformulation SW-POLY; no bound).
- G-N1-LB (l.10): minor; owner «L-NEW (optional; not routed)»; status **open**.
- G-N5-TERM (l.16): major; owner «L-NEW (L-COMP checks runs)»; status **closed** (RESULTS R15).

### 4. Three owner rulings (verbatim; status from docs/DECISIONS-INDEX.md on trunk 5d7aab0f)
1. D18 (INDEX l.32, **active**; text docs/DECISIONS.md l.333): «Focus on N5 and work toward proving it. Explore novel approaches,
   especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable
   assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from
   conjectures and open problems.»
2. D1 (INDEX l.5, **active**; excerpt, docs/decisions/D001-launch-brief.md l.25-26): «A claimed polynomial algorithm is far more likely
   to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.»
3. D25 (INDEX l.57, **active**; text docs/DECISIONS.md l.541): «So put everything into trying solving it today». Lead reading L58
   (INDEX l.58, active): the whole fleet works on box 217's ENUM-LOG / QUIET-KEY-1P today, either answer taken; (3) «Nothing in D25
   relaxes D1».
- Also in force: D14 (INDEX l.22, **active**; text l.246): «You know it can also test prveiously not tested approaches, it can come up
  with it own as well»; D21 (INDEX l.46, active; L51: maximum effort until 2026-11-14 10:05Z); D23 (INDEX l.54, active): «I reset the
  fable weekly limit, please conitnue on high effort, we already used a day, w still have 160% of usage left until tomorrow night»;
  D24 (INDEX l.56, active): «do xhigh». L56: verify's self-check skip applies only to docs/agents/-only changes (this commit is one;
  my later pushes run in full).

### 5. One trap, and the check that prevents it
- Trap (this lane, many starts; this start: 26 commits behind): the container starts shallow, stale or detached; a commit there forks
  history and the push fails («invalid refspec» on a detached HEAD) or is rejected as non-fast-forward.
- Check: fetch --unshallow + fetch the branches by name, checkout + merge --ff-only, then `git branch --show-current` and
  `git rev-parse HEAD origin/claude/l-new` must agree before any edit (done: claude/l-new, both fcea233b). Before my own push:
  `pgrep -f "bash scripts/push.sh"` (never two pushes), re-fetch and ff-only; on a non-fast-forward refusal, merge
  origin/claude/l-new with --no-ff (never rebase, never force). Push as a tracked task with a 2-hour timeout, output redirected to a
  file, then `echo exit $?`; never a pipe, never «&».
- Packet-relevant traps kept from successors 74-76: (1) a statement read on a wider class than its proof covers: the REDUCTION is for
  Ξ-acyclic G, N5 (not N5′-xi), Γ3(G) with the input game's e-vertex numbering ([NUM], R241), states before the first fallback only;
  (2) A6's withdrawn equivalence (only SW-POLY is exact; ENUM-LOG is necessary); DBL4 has k = 0 (half enumeration); (3) a control that
  cannot fire is no control (reversing the gate order flips every comparison at once: use a random permutation); (4) typed timestamps
  (three slips by successor 76): stamps are copied from the date -u output of the same command; SHAs only from git output in a later step.
