# Handover check: REFEREE

## successor 35 (2026-11-13T12:42Z by date -u; predecessor successor 34, HANDOVER NOTE in notes/REFEREE.md at 92d1cfdb)
Measured from the repository at the time of writing, not recalled. The model label is left out of repository files (the Lead's brief:
no model name in commits); the Lead's brief names it.

### 1. Branch, head, distance to trunk
- Trap check: `git fetch --unshallow` (repository not shallow: `git rev-parse --is-shallow-repository` = false) + fetch of claude/referee
  and trunk. The local branch was claude/referee but 39 commits behind origin (stale container); `git merge --ff-only
  origin/claude/referee` fast-forwarded it. Then `git branch --show-current` = claude/referee and HEAD = origin/claude/referee =
  92d1cfdbaa0d72b468a28de1516720654c0cd250.
- At 92d1cfdb: 1 ahead / 144 behind trunk claude/vibrant-johnson-nxvvxo 5d7aab0f19f664034567c3bf4f41bcf9e1684d20 (merge-base 32d61d60).
- Merged trunk with a normal merge (`git merge -m …` with this session's Claude-Session trailer; no rebase): head ebb891e5415f6eed74154b9e9a68dbccc3bd0890,
  `git rev-list --left-right --count trunk...HEAD` = «0 2» (behind, ahead) before this file's commit.
- Clock: local `date -u` Fri, 13 Nov 2026 12:41:26 GMT against «date: Fri, 13 Nov 2026 12:41:26 GMT» of a raw.githubusercontent.com
  response in the same command: skew 0 s (to the second).
- No push running (`pgrep -af "bash scripts/push.sh"`: nothing).
- rate_limit_info (get_session on this session, 12:41Z): isUsingOverage false, rateLimitType seven_day, status allowed_warning,
  resetsAt 1795035600; session_context.model and last_served_model as the Lead's brief names them, effort_level xhigh.

### 2. Open work and next step of each (after «go», in the Lead's order)
- 1. PRE-CHECK of the kill candidate G_k (not a signature). Inputs measured on this tree (trunk merged): docs/red/P-N5-REALIZE.md
  (R104's packet) sha1 067f06b6c67969adf346621b4a92b253491ab2b9, 278 lines, 28,204 B; docs/new/P-N5-REACH.md (R117's packet) sha1
  b7bd693744fdec2aa993f2133c22cbe724933ff0, 345 lines, 39,253 B; this lane's earlier reports docs/referee/R-N5-REALIZE.md and
  docs/referee/R-P-N5-REACH.md (predecessors' work, to be disclosed as prior work of this lane). The rule's text: NOT in hand yet (the
  Lead sends it in the first message after this start). Next, in this order: (a) rebuild G_3..G_12 with my own code from the rule's
  text only; (b) membership in R104's class, clause by clause against docs/red/P-N5-REALIZE.md §2; (c) L(G_k) on an IDEAL simulator
  written from R104's words (expected by the lane's DATA: 2^k − 2; mine is a re-measurement, not a copy); (d) read R117's proofs of
  Theorem REACH3 and Corollary REAL-IDEAL-S3 line by line for a hypothesis G_k violates (wires = two options of a mover with one
  W-target and both Ξ-targets the exit; level-0 movers on the exit; all parities even; up to 8 movers on a level). Not reading
  claude/l-red-b or docs/referee-2/ on G_k before my own rebuild. While this file's push is in verify: paper work and second-scale
  runs on (d) and on the simulator only (the Lead's exception on D25); no long job, no commit.
- 2. FIRST REVIEW of packet P-N5-EXP (Theorem EXP-IDEAL, Corollary EXP-N5, Lemma MEMBER, DATA) when the Lead sends the freeze SHA
  (claude/l-red-b; not frozen at this writing). Next: statement diffed against TARGET.md and R117's wording; Lemma MEMBER; the
  induction (RESPONSE LEMMA, P_(k−1) = 3, P_j = 2P_(j+1) + 1) step by step, writing for each inductive step which states the cited
  fact was proved for; DATA re-run on my own engine with named must-0 counters and a firing control; verdict per item, gaps listed.
  L43: «DEAD» needs the growth proved for all k or an instance beyond an explicit bound; fits are DATA.
- 3. FIRST REVIEW of packet P-N5-KEY1P (claude/l-new 44775605 per the brief; docs/new/P-N5-KEY1P.md sha1 f7191623… per the brief).
  MEASURED: `git cat-file -t 44775605` fails after `git fetch origin claude/l-new` (origin/claude/l-new = c7e85713, whose tree has
  no docs/new/P-N5-KEY1P.md): the freeze commit is not on origin at this writing (push presumably in verify). Next: re-fetch at
  the start of item 3 and measure the sha1 before reading.
- Any CHECKER item on R128 / R129 / R130 this lane signed: nothing in hand.

### 3. docs/GAPS.md rows relevant to me (trunk 5d7aab0f)
- REFEREE owns no row. The row the N5 packets feed: G-N5-TIME (line 11; severity major; owner «L-NEW (L-LIT T22; referees later)»; status
  open).

### 4. Three owner rulings that most constrain me (verbatim, docs/DECISIONS.md at trunk 5d7aab0f), with DECISIONS-INDEX status
1. D1 (index: active; DECISIONS.md lines 7-8):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never downgrade the referee to save money.
   (For today's item: the same standard applies to a kill as to a bound; Lead reading L43, index: active, says a «DEAD» of an
   asymptotic statement needs a refereed proof or an instance beyond an explicit bound. L43 is a Lead reading, not owner words.)
2. D18 (index: active; DECISIONS.md line 333):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
3. D25 (index: active; DECISIONS.md line 541; owner, direct message to the Lead, 2026-11-13):
   > So put everything into trying solving it today
   (with D24, index: active, DECISIONS.md line 538: «do xhigh»; D23, index: active, line 527: «I reset the fable weekly limit, please
   conitnue on high effort, we already used a day, w still have 160% of usage left until tomorrow night»; D21, index: active, line
   449. Lead readings L51, L52, L56, L57, L58 are in the index; not owner words.)

### 5. One trap that bit this lane, and the check that prevents it
- Trap (s27-s35): stale local branch (39 behind at this start). Check: fetch, ff-only, `git branch --show-current` and `git rev-parse HEAD
  origin/claude/referee` equal before any push.sh (done above).
- Trap (s34): a SHA sent to the Lead in the same tool batch as the commit (a nonexistent 4e2fd393). Check: send_message is never in
  the batch of a git commit; the SHA is read from git output in a step after the commit.
- Trap (s34): a container restart killed push.sh and origin stayed behind. Check after any restart: `git rev-parse HEAD
  origin/claude/referee` and `git ls-remote`; re-push at once; tell the Lead.
- Trap (s32, G-P6), the one that matters most for item 2: an induction run past the interval its lemma was proved on. Check: for each
  inductive step of the RESPONSE LEMMA, write down which states the cited fact was proved for and whether the step's state is
  among them.
- Trap (CLAUDE.md, «Traps»): a «counterexample» from an unfaithful implementation is not a counterexample. Check for item 1: my IDEAL
  simulator is written from R104's packet text and first run on instances whose L is known from landed text before it is run on G_k;
  the engine for N5 on Γ3(G_k) is checked against Zielonka's winners on every run.
