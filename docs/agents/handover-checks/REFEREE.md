# Handover check: REFEREE

## successor 34 (2026-11-12T19:57Z by date -u; predecessor successor 33, HANDOVER NOTE in notes/REFEREE.md at 90703a81)
Measured from the repository at the time of writing, not recalled. The model label is left out of repository files (the Lead's brief:
no model name in commits); the Lead's brief names it.

### 1. Branch, head, distance to trunk
- Trap check: `git fetch --unshallow` (repository not shallow: `git rev-parse --is-shallow-repository` = false) + fetch of claude/referee
  and trunk. The local branch was claude/referee but 23 commits behind origin (stale container); `git merge --ff-only
  origin/claude/referee` fast-forwarded it. Then `git branch --show-current` = claude/referee and HEAD = origin/claude/referee =
  90703a81060b83e879a4e5e39d97d4bde9d4ba7f.
- At 90703a81: 10 ahead / 2 behind trunk claude/vibrant-johnson-nxvvxo 7fa6aff4 (merge-base 68c8d293).
- Merged trunk with a normal merge 434be444 (`git merge -m …` with this session's Claude-Session trailer; no rebase): 11 ahead / 0 behind
  before this file's commit.
- Clock: local `date -u` Thu Nov 12 19:56:57/58 UTC 2026 against «date: Thu, 12 Nov 2026 19:56:58 GMT» of a raw.githubusercontent.com
  response in the same command: skew 0 s (to the second).
- No push running (`pgrep -af "bash scripts/push.sh"`: nothing).

### 2. Open work and next step of each (after «go», in the Lead's order)
- A0. BYTE TEST of P-N5-GATE fixes entry 5 + line L-5 (R128). Objects present on origin and measured: claude/l-si 2051a0ee (ancestor of
  origin/claude/l-si 516b6837), docs/si/P-N5-GATE-line-L5.txt sha1 459fd88d2d1959647f6aeb065bf8ac58cce684f9, 12,923 B (matches the
  brief); fix commit 7b0a58ae; CHECKER C142 at claude/checker 269effb3. Next: diff L-5 against this lane's signed L-4 (R-P-N5-GATE.md §K)
  and CHECKER's nine pairs (C142 §4, 7ebcf735), plus the tenth pair «fixes entries 1-4,» → «1-5,»; check the meaning of E-1 (GL-3 RA
  rows against L-SI 47 box 90 at 2d0344d3 / 4ded1e8d), E-2 (growth clause numbers; A*_all dropped), E-3 (seven markers, no word
  change); verdict MATCHES / REFUSED as a new section of R-P-N5-GATE.md. Not reading claude/referee-2 0df0fdd8 before my verdict.
- B. FIRST REVIEW (a signature) of packet P-N5-LEVEL. Objects present and measured: claude/l-new 1e6df499 (ancestor of origin/claude/l-new
  069c888b); docs/new/P-N5-LEVEL.md sha1 7c956df443cfddbf23bfbaa18a26a98369b176ec, 65,874 B, 575 lines; docs/new/P-N5-LEVEL-line-L1.txt
  sha1 28565b3c60fe8167f4b660c83fa27c00cd7b4fe9, 7,239 B (all match the brief). Next: read the frozen packet afresh; disclose
  R-box208-preread.md (s32) and R-box209-preread.md (s33) as prior work of this lane; test PR-1..PR-6 and s33's three additions (H0 on
  every step of H's run; (P2)-type citations for e-vertices with successor c_W; Lean only as «Lean-checked (lane)» with name and commit),
  the scope (Howard ALL-SWITCH, MAXIMISER improves, IDEAL-CYC on R104 genomes; not N5, N5′-xi, M4), every genome-only step, premises by
  script against landed RESULTS, the DATA rule (L43; each DATA clause names its counter), the TARGET.md diff, line L-1 against the «To sign»
  statements; in particular that (C4) uses landed R126 QUIET-N and that no step uses (P4) outside a plateau (the level-0 gate with both
  faces of class (c_W, ∅) for Y := all vertices). Report docs/referee/R-P-N5-LEVEL.md, committed section by section. Not reading
  docs/referee-2/ on P-N5-LEVEL before my verdict.
- C. Any CHECKER item on R128 this lane signed: nothing in hand.

### 3. docs/GAPS.md rows relevant to me (trunk 7fa6aff4)
- REFEREE owns no row. The row the N5 packets feed: G-N5-TIME (line 11; severity major; owner «L-NEW (L-LIT T22; referees later)»; status
  open).

### 4. Three owner rulings that most constrain me (verbatim, docs/DECISIONS.md at trunk 7fa6aff4), with DECISIONS-INDEX status
1. D1 (index: active; DECISIONS.md lines 7-8):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   > Never downgrade the referee to save money.
2. D18 (index: active; DECISIONS.md line 333):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
3. D21 (index: active; DECISIONS.md line 452, «Relayed text (OWNER-DESK, verbatim)», confirmed by the owner in the Lead session per line
   454 «I confrim tge stuff»):
   > Okay, I want maximum effort. I want to use 200% usage in 3 days. There is fable 5.2 as well, use that too in dpeth everywhere where it seems fitting, use fable 5.2 at hard or xhigh. SO yes, 200% uage under 2 days.
   (Lead readings L51, L52 in the index; L53 (this session on Opus because the Fable weekly limit is reached) is named in the Lead's brief
   and not yet in the trunk index at 7fa6aff4. Not owner words.)

### 5. One trap that bit this lane, and the check that prevents it
- Trap (s27-s34): stale local branch (23 behind at this start). Check: fetch, ff-only, `git branch --show-current` and `git rev-parse HEAD
  origin/claude/referee` equal before any push.sh (done above).
- Trap (s32, G-P6): an induction run past the interval its lemma was proved on. Check for item B's (P4)/(P6): for each inductive step,
  write down which states the cited fact was proved for, and whether the step's state lies among them.
- Trap (s31, s33): numbers from two outputs misread, and a total done in the head. Check: a number enters a report or message only from
  the output of the command that printed it; SHAs only from git output in a step after the commit.
- Trap (s33): `git merge --no-edit` left a commit without the trailer; this time `git merge -m` with the trailer (434be444).
