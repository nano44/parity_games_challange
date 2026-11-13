# Handover check: L-NEW (successor 76; session session_01V5yGRXFkFRGsbtdAPyKqXN; started 2026-11-13 ~06:06Z, written 2026-11-13T06:07Z by date -u)
Overwrites successor 75's answers (history in git). Each answer measured from the repository at writing (commands named).
Predecessor: successor 75, parked at l-new f8a042ab (section «HANDOVER (successor 75, PARKING 2026-11-13 04:57Z …)» at the top of notes/L-NEW.md).
Clock: `date -u` 06:06:23Z against the `date:` header of raw.githubusercontent.com (06:06:23 GMT) in the same command: skew 0 s (< 1 s).

### 1. Branch, head, ahead/behind trunk
- Trap check, as briefed: `git fetch --unshallow origin; git fetch origin claude/l-new claude/vibrant-johnson-nxvvxo;
  git checkout claude/l-new; git merge --ff-only origin/claude/l-new`. The container came up on claude/l-new but 16 commits BEHIND
  origin/claude/l-new (fast-forwarded to f8a042ab); `git rev-parse --is-shallow-repository` = false.
  `git branch --show-current` = claude/l-new; `git rev-parse HEAD origin/claude/l-new` both f8a042abf1cf4dea19b74d8765029f3120255df5.
- Trunk origin/claude/vibrant-johnson-nxvvxo head at my fetch (06:06Z): 65e02855 («Lead: R129 third fill (CHECKER C144 R-E1 …)»,
  committed 2026-11-13T05:37:20Z). `git rev-list --left-right --count trunk...HEAD` = 481 / 24: **24 ahead / 481 behind**;
  merge-base 621e6b77 (unchanged since successors 73-75). Not merged by me (the brief does not ask for a merge).
- RESULTS on trunk 65e02855: `### R128` present (P-N5-GATE, CHECKER C142 a9233137); `### R129` NOT yet present (third fill in flight).

### 2. Open work and the next step of each
- Item 1, BOX 216 VALUE SIDE (approved by the Lead 04:58Z; proposal and terms in notes/L-NEW.md HANDOVER of successor 75):
  V1 first: per-lemma rule-free reading of the landed value-side lemmas (R121 E-MON; R125 E-MON3, CHAIN-DECOMP3; R127 SPLIT, TRANSFER,
  REWIN, REWIN-HI, SPLIT-COUNT; R128 GATE-RACE, TRIGGER, GATE-LOW-NULL, NP-SHAPE, E-FACE-PAYS, WAIT-QUIET, SAME-SUFFIX, STEP-BOUND,
  PARALLEL, PAIR-EXPEL, EXPEL-COUNT, A*-EQUIV), each with its deciding proof line quoted by script; verdict per lemma: uses Howard's tie
  rule, or only «each moved mover improves strictly» + F1-F6 + static lemmas. Output: the list that holds for ANY improving run of
  standard states, hence for N5's key run via [IMP3]. Then V2 XFLIP (moves(x) ≤ 1 + XF_x for degree-2 movers, from F2; proof, must-0
  counter xflip, a firing control «swap the gates' Ξ values»), then V3 JOINT-POLY labelled as a reformulation equivalent to O1′ at
  degree ≤ 2 up to a factor N (DATA: KF, XF, JF per mover). Next step: statement first (docs/new/N5-VALUESIDE-box216.md), reading
  the proofs in the landed packets. Not a bound; G-N5-TIME stays OPEN; not M3 or M4.
- Item 2, duty P-N5-LEVEL / R129 (C144): if CHECKER routes an item to L-NEW: fixes entry 2 + L-3 by script (box211 mkl2 pattern, asserting
  L-2 sha1 d18125ed); never edit the frozen packet, L-1 or L-2. At writing nothing is routed to L-NEW (Lead's third fill 65e02855
  carries C144's R-E1/R-E2 strings itself).
- Boxes 209, 210, 212, 213 (KEY-TAU CANDIDATE), 215 (KEYSIDE-ALL CONDITIONAL on KEY-TAU (i)): under attack (L-RED 69, R241);
  answers are append-only addenda. Box 214: dead end of its proposal (block lifting), recorded.
- Running at writing: only `scripts/setup_oink.sh` (tools/oink absent; tracked task). No research job started; none before «go».

### 3. docs/GAPS.md rows I own (`git show trunk:docs/GAPS.md | grep -n L-NEW`, trunk 65e02855)
- G-N5-TIME (l.11): major; owner «L-NEW (L-LIT T22; referees later)»; status **open** (last UPDATE in the row: 2026-11-13 04:22Z,
  R128 landed). Box 216 does not close it.
- G-N1-LB (l.10): minor; owner «L-NEW (optional; not routed)»; status **open**.
- G-N5-TERM (l.16): major; owner «L-NEW (L-COMP checks runs)»; status **closed** (RESULTS R15).

### 4. Three owner rulings (verbatim; status from docs/DECISIONS-INDEX.md on trunk 65e02855)
1. D18 (INDEX l.32, **active**; text docs/DECISIONS.md l.333): «Focus on N5 and work toward proving it. Explore novel approaches,
   especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable
   assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from
   conjectures and open problems.»
2. D14 (INDEX l.22, **active**; text docs/DECISIONS.md l.246): «You know it can also test prveiously not tested approaches, it can come
   up with it own as well»
3. D1 (INDEX l.5, **active**; excerpt, docs/decisions/D001-launch-brief.md l.25-26): «A claimed polynomial algorithm is far more likely
   to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.»
- Also in force: D21 (INDEX l.46, **active**) with Lead readings L51 (l.48: maximum effort until 2026-11-14 10:05Z), L52 (l.49), L53
  (l.50: Fable 5.2 weekly limit reached, resets 2026-11-18 21:00Z; successors on Opus 5.5 high). L55 (l.51) on verify's self-check skip;
  L56 (per the brief, docs/DECISIONS.md) — the skip applies only to docs/agents/-only changes, so my pushes run verify in full.

### 5. One trap, and the check that prevents it
- Trap (this lane, many starts; this start: 16 commits behind): the container starts shallow, stale or detached; a commit there forks
  history and the push fails («invalid refspec» on a detached HEAD) or is rejected as non-fast-forward.
- Check: fetch --unshallow + fetch the branches by name, checkout + merge --ff-only, then `git branch --show-current` and
  `git rev-parse HEAD origin/claude/l-new` must agree before any edit (done: claude/l-new, both f8a042ab, not shallow). Before my own
  push: re-fetch and ff-only again; on a non-fast-forward refusal, merge origin/claude/l-new with --no-ff (never rebase, never force).
- Also kept (box 216 relevant): a lemma read on a wider class than its proof covers (one-player read as two-player; Howard-only facts
  read as rule-free: R212's K5how, platexit fire under other rules). V1's check: quote each proof's deciding line by script and run
  each rule-free claim's counter under a non-Howard rule as a firing control. Reversing the gate order is NOT a control (use a random
  permutation). Never edit check.sh while verify runs; one push at a time (`pgrep -f "bash scripts/push.sh"` first); SHAs only from git
  output in a later step; times from `date -u`; no model name in commits.
