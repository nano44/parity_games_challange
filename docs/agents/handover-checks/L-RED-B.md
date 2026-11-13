# Handover check: L-RED-B successor 5 (second adversary lane; Fable 5.2, effort xhigh, per the brief; D1 / D18 / D21 / D22 / D24 / D25; written 2026-11-13T12:13Z by date -u)
Every answer is measured from the repository at the time above (commands named), not recalled. Predecessor: successor 4
(session_01V5yGRZixRCf3PLfDhttq7S), handover 1fbd6d0d (notes/L-RED-B.md «SUCCESSOR 4 HANDOVER»). This session:
session_01V5yGRXFf3kFNfkycCHTnLT (get_session: model claude-fable-5-2, effort_level xhigh, parent session_014FBi6o334DvwT5Uw2kDfoN).
Trap check on entry (11:29Z): `git branch --show-current` -> claude/l-red-b; the local branch was at 9e8796cc, behind origin;
`git merge --ff-only origin/claude/l-red-b` -> 18dd585fe76e5c574f1f1fa7976bd6918053785f = origin at that time. The clone is not shallow
(fetch --unshallow was a no-op). Clock skew against the Date header of a raw.githubusercontent.com response: 0 s (local «Fri Nov 13
11:29:53 UTC 2026», header «Fri, 13 Nov 2026 11:29:53 GMT»).
EARLY START (Lead's brief): `git ls-remote origin claude/l-red-b` printed 18dd585f at 11:29Z, 11:38Z and 11:53Z and
1fbd6d0d2abb2c6cf9f832ffd118b5c3317a2f82 at 12:11Z; then `git merge --ff-only origin/claude/l-red-b` -> HEAD = origin = 1fbd6d0d.
Nothing was committed before that. rate_limit_info (get_session on this session, 12:12Z): isUsingOverage false, rateLimitType
seven_day, status allowed_warning, resetsAt 1795035600.

## 1. Branch, head, distance to trunk
- `git branch --show-current` -> claude/l-red-b. `git rev-parse HEAD origin/claude/l-red-b` -> both 1fbd6d0d2abb2c6cf9f832ffd118b5c3317a2f82.
- Trunk: `git rev-parse origin/claude/vibrant-johnson-nxvvxo` -> 5d7aab0f19f664034567c3bf4f41bcf9e1684d20 (fetched 11:29Z).
  `git rev-list --left-right --count HEAD...5d7aab0f` -> 35 ahead, 191 behind; merge-base 471aba45214c9b4009332ef1d498dd5dbc42f3cb.
  I do not merge trunk; other lanes' files are read with `git show <ref>:<path>` / git archive into experiments/red-b/work/ (ignored).
- Read-only refs fetched 11:3xZ: claude/l-new a143d4060d75f8463fe098b6ce18eef3febcd14b (box 217), claude/l-comp 6bfd4966, claude/l-lower
  b6887eff, claude/l-si ff28a3fc, claude/l-red aa4f7680 (fetched, NOT opened: R243 is not read before my own B6 attempt 2 verdict).
- Files I own: docs/red-b/, experiments/red-b/, notes/L-RED-B.md, this file.

## 2. Open work and the next step of each
- B1-B5: DONE on origin (B1 no kill; B2-B4 NO KILL; B5: ONE-FB false, ONE-FB′ k ≤ 2 on W-wrappers, 18dd585f). Nothing owed.
- B6 attempt 1 (docs/red-b/B6-quietkey-1p.md §1-§4, 1fbd6d0d): three classical exponential constructions do not embed; Lemma ACYC-GREEDY
  (lane, unrefereed). Nothing owed.
- B6 attempt 2 (this session's WORK, after «go»): a KILL attempt on QUIET-KEY-1P by CONSTRUCTION: a family G_k of Ξ-acyclic genomes by
  a rule with T_key ≥ 2^k at N + M = poly(k), or the exact step where every such rule fails, as a lemma or a smallest instance.
  State at this writing (done during the EARLY START wait, as the brief allows: reading, paper work, second-scale runs; no commit):
  - Read: box 217 (docs/new/N5-QUIETKEY-box217.md and one217.py at a143d406, all of both), trunk docs/RESULTS.md R113 and R120 title
    lines (ALIGN, MOVE, DOUBLE-EQ, PULSE-NEST), the five tower genomes of claude/l-comp experiments/comp/box29 (structure printed).
  - Two uncommitted tools, kept in experiments/red-b/work/b6/tools/ (ignored) until «go»: onep.py (own implementation of 1P(G) from
    box 217 §6.1; second-scale run: T_key = 30, 136, 209, 67, 299 and Howard 9, 9, 12, 9, 8 on DBL4, H5, H6, RECF4, HIT7, equal to
    one217.py's numbers on the same five files; k(G) = 0, 5, 6, 4, 7) and bilad.py (a generator of «anti-aligned» ladders; 20,000
    random ones at d = 6 gave T ≤ 6: DATA, no claim).
  - Paper work (NOT run, NOT a result): a candidate rule with O(1) movers per level (a block pair, an «end-follower», two wires and two
    observer pairs per level; keys read through wires, values root-first). Next step: build G_3 … G_10 from the rule, run them on
    onep.py and one217.py, then on N5 itself (n5v spec on Γ3) against Zielonka with must-0 counters and a firing control. A genome
    with k ≥ 8, or a rule whose first three members grow, goes to the Lead before anything else. If the rule fails: the exact failing
    step, as a lemma or the smallest instance.
- `pgrep -af "push.sh|verify.sh"` -> nothing running before this file's push; `git status --short` -> clean before this file.

## 3. docs/GAPS.md rows
- Owned: none. Trunk 5d7aab0f docs/GAPS.md open table rows (file lines 6-11): GAP-A, GAP-C, G-S5-6, G-NEST, G-N1-LB, G-N5-TIME;
  `grep -c L-RED-B` on it -> 1 (line 11, row G-N5-TIME: its text cites L-RED-B's B1 report twice; not an owner column).
- Worked against: G-N5-TIME (line 11; owner «L-NEW (L-LIT T22; referees later)», status open): N5's polynomial iteration bound, today
  through box 217's QUIET-KEY-1P / SW-POLY (L58).

## 4. Owner rulings, verbatim (trunk 5d7aab0f docs/DECISIONS.md; status from docs/DECISIONS-INDEX.md at the same commit)
- D1 (DECISIONS.md line 7; index line 5, status **active**):
  > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
- D18 (DECISIONS.md line 333; index line 32, status **active**):
  > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
- D25 (DECISIONS.md line 541; index line 57, status **active**): «So put everything into trying solving it today»
- Also binding: D22 (line 487-491; index line 47, active): owner (verbatim) «yes» to the L-RED-B lane; D21 (index line 46, active;
  Lead readings L51, L58: maximum effort until 2026-11-14 10:05Z); D23 (line 527; index line 54, active) «I reset the fable weekly
  limit, please conitnue on high effort, we already used a day, w still have 160% of usage left until tomorrow night»; D24 (line 538;
  index line 56, active) «do xhigh». L56 (index line 53, active): the self-check skip applies only when every changed path is under
  docs/agents/; my other pushes run in full. L58 (index line 58, active): the fleet works on box 217 today, either answer taken; D1's
  standard of proof unchanged.

## 5. One trap that bit this lane, and the check that prevents it
- Trap (successor 4's own words in the handover): «my own lemma was false: always run the direct test before telling the Lead it is
  proved» (ONE-FB, draft 2afb3f11, killed by its own test). It applies to this session at once: the candidate rule of §2 exists on paper
  only. Check: no construction or lemma goes to the Lead as more than «paper, not run» before (a) my simulator and one217.py agree on
  it, (b) N5 itself (n5v spec on Γ3) reproduces the step counts at the sizes where that is feasible, with Zielonka agreement and a
  firing control, and (c) growth is stated only with a fit and residuals or as «not identified».
- Second trap (successors 2-4): a SHA quoted before it is on origin (8d5d8388 lost; 1fbd6d0d needed a re-run push). Check: `git
  ls-remote origin claude/l-red-b` must print the SHA before it is quoted as on origin; pushes are tracked tasks (2-hour timeout, output
  redirected, exit code echoed, `pgrep -f "bash scripts/push.sh"` first); never a commit while a push runs.
