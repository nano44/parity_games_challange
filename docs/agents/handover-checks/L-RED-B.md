# Handover check: L-RED-B successor 8 (second adversary lane; target today: candidate RF; model and effort as in the Lead's brief and roster; D1 / D22 / D27 / D28, reading L61; written 2026-11-14T15:20Z by date -u)
Every answer is measured from the repository (commands named), not recalled. Predecessor: successor 7
(session_01V5yGRVmUNMkUXGRuVH63B8), handover in notes/L-RED-B.md («SUCCESSOR 7», items (a)-(a⁗)), last commit
91d30d95a3875950b5290b8fc63f1e2c3ad05238 (line L-6, fixes entry 11). This session: session_01V5yGRYdyWTwtt6n2dRhXMs (parent
session_014FBi6o334DvwT5Uw2kDfoN), started by the Lead's brief of 2026-11-14 14:07Z.
EARLY START record (the brief's NO-COMMIT clause, changed by the Lead at 14:24Z from abde9163 to 91d30d95): `git ls-remote origin
refs/heads/claude/l-red-b` printed 10dfedb6574c9291011a5a7fbbdff261fe312d91 at 14:07Z, 14:14Z, 14:59Z and 15:13Z, and
91d30d95a3875950b5290b8fc63f1e2c3ad05238 at 15:17Z; then `git fetch`, `git merge --ff-only origin/claude/l-red-b`. Nothing was
committed before that; all work of 14:07Z-15:17Z lived in UNTRACKED files under experiments/red-b/b7/ and in the ignored
experiments/red-b/work/b7/. Clock skew was not measured against an outside clock this session (every stamp is date -u of this
container).

## 1. Branch, head, distance to trunk
- `git branch --show-current` -> claude/l-red-b. Before this session's commit: `git rev-parse HEAD origin/claude/l-red-b` -> both
  91d30d95a3875950b5290b8fc63f1e2c3ad05238.
- Trunk: `git rev-parse origin/claude/vibrant-johnson-nxvvxo` -> 15171faa822983e7c6118bb3c4be25b47469a387 (fetched 15:17Z).
  `git rev-list --left-right --count origin/claude/vibrant-johnson-nxvvxo...HEAD` -> 201 48: 48 ahead, 201 behind; merge-base
  471aba45 (`git merge-base`). Trunk is not merged into this branch; other lanes' files are read with `git show`.
- Read-only refs fetched today: claude/l-si 8c062914 (box 108), claude/l-comp dc6d831f, claude/l-red 19aad190, claude/l-lit
  (docs/lit/T66-depth-check.py at 5c53efbd: its transcription of Friedmann's Table 4, used only to compare with mine).
- Files I own: docs/red-b/, experiments/red-b/, notes/L-RED-B.md, this file.

## 2. Open work and the next step of each
- P-N5-EXP (this lane's kill of N5): FROZEN packet docs/red-b/P-N5-EXP.md (sha1 c0449b17193f19619f33b366096762dfde27d542,
  measured 15:19Z), fixes file 1,443 lines (sha1 214967a1…), line of record L-6 (sha1 1e0ff12d…). The brief: its landing as
  RESULTS R131 «is NOT your work: anything on the packet, the fixes file or the line goes to you only if I send it». Next step:
  none unless the Lead sends an item; then append-only (entry 12, an L-7 by script, pin file fixes9, a ninth guard stage: the
  predecessor's NEXT NUMBERS, to be re-read in its (a⁗) before use).
- B7 (today's target, brief 14:07Z, corrected 14:28Z and 14:52Z): KILL RF (L-SI 57's ROOT-FIRST rule inside classical one-sided
  Vöge-Jurdziński strategy improvement) by a rule-built family. State at this commit: own engine experiments/red-b/b7/si7.py with
  its self-tests (Howard = 9·2^n − 10 on Friedmann's G_n, n ≤ 6; valuation against the definition by brute force; Oink zlk / tl /
  verify), a C++ port rf7.cpp equal to it on 1,648 runs, and a KILL CANDIDATE: family K^s_n (rfc2.py, `build(n, skip=True)`),
  |V| = 3n² + 3n + 1, on which RF makes exactly 7·2^(n−1) − 2n − 3 iterations for every n measured (n = 1..13 at this writing;
  n = 14..17 running). Reported to the Lead 15:14Z as DATA on one engine. Report: docs/red-b/B7-RF.md.
  Next steps: (i) the schedule of the run in closed form and its step-by-step test against the real run (the lane's method for
  G_k); (ii) the proof of the doubling recurrence; (iii) an instance beyond an explicit polynomial (by the law the first n with
  iterations > |V|² is 19: 1,834,967 > 1,301,881; needs a checkpointed run); (iv) answers to the independent rebuilds the Lead
  routes.
- Nothing else is open. No job of a predecessor runs (`ps` at 15:20Z shows only this session's runks.py and runks_cpp.sh with its rf7).

## 3. docs/GAPS.md rows this lane owns
- Owned: none. Trunk 15171faa docs/GAPS.md: `git show origin/claude/vibrant-johnson-nxvvxo:docs/GAPS.md | grep -n L-RED-B` -> one
  line (11, row G-N5-TIME, owner «L-NEW (L-LIT T22; referees later)», status open): its text cites this lane, the owner column
  does not name it. No row for the candidate RF exists yet (grep «RF» in the same file matches only that line 11, in the label NO-RF-OLD of its text).

## 4. Owner rulings, verbatim (trunk 15171faa docs/DECISIONS.md; status from docs/DECISIONS-INDEX.md at the same commit)
- D1 (index line 5, status **active**):
  > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
  The same standard binds a kill: K^s_n is a KILL CANDIDATE (DATA + a lane mechanism) until two referees sign or an instance
  passes an explicit bound (reading L43, index line 36, active).
- D27 (index line 62, status **active**):
  > SO we have to look for a new algorithm no? Do we have any promising lead or can convert our learning into a new promising algorithm?
- D28 (index line 63, status **active**):
  > I reset everything, you have until 11PM to use a full 100% usage
- Also binding: D22 (index line 47, active): owner (verbatim) «yes» to the L-RED-B lane. Lead reading L61 (index line 64, active):
  today is a design day; L-RED and L-RED-B are the adversaries of the design lanes' candidates.

## 5. One trap that bit this lane, and the check that prevents it
- Trap (successors 2-7, and the reason for today's NO-COMMIT clause): a commit made, or a SHA quoted, before the previous push is
  on origin; verify runs on the WORKING TREE for about 50 minutes, so a tracked file touched during a push is verified in a state
  nobody committed. Check: `git ls-remote origin refs/heads/claude/l-red-b` before the first commit after an EARLY START and
  after every push (push.sh can print exit 0 after an HTTP 503); pushes are tracked background tasks with the output redirected
  and `echo exit $?`; never a second push, never a commit while one runs; during a push only untracked or ignored paths are
  written (experiments/red-b/work/, the scratchpad).
- Trap found by this session at 14:13Z (new): a module of mine named selftest.py was shadowed by experiments/harness/selftest.py
  once the harness directory was put on sys.path: `import selftest` ran the HARNESS's self-test and my cross-check silently used
  nothing of mine. Check: every B7 module has a lane-specific name (si7, st7, gens7, rfc2, cmp7, xoink) and every cross-check
  prints its own tag («B7 …») in the summary line that check.sh matches, so a foreign module cannot pass for it.
