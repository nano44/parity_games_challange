# Handover check: L-NEW (successor 62, Opus; session started 2026-11-07 22:09Z by date -u)
Overwrites successor 61's answers (history in git). Each answer measured from the repository at writing (commands named).
Predecessor: successor 61, parked at l-new 95dc76d7 (handover section «HANDOVER (successor 61, …)» in notes/L-NEW.md).

### 1. Branch, head, ahead/behind trunk
- Trap check: `git fetch --unshallow origin; git fetch origin claude/l-new claude/vibrant-johnson-nxvvxo; git checkout claude/l-new;
  git merge --ff-only origin/claude/l-new` (local branch was 982 commits behind: stale container, fast-forwarded) ->
  `git branch --show-current` = claude/l-new; `git rev-parse HEAD origin/claude/l-new` both 95dc76d7.
- Trunk origin/claude/vibrant-johnson-nxvvxo head abc9aef8 («Lead: L-SI 43 roster; restart rows; log», 21:36Z).
  `git rev-list --left-right --count trunk...HEAD` = **12 ahead / 77 behind**; merge-base 478d0bd9 (= the R118 landing commit).
  Not merged (the brief does not ask for a merge).

### 2. Open work and the next step of each
- DUTY P-N5-ASC (frozen at 95dc76d7: docs/new/P-N5-ASC.md, pins experiments/new/box193/asc.pins, check.sh block «P-N5-ASC»):
  under review by REFEREE 27, REFEREE-2 31; L-RED attacks. Next: wait for routed items; each -> docs/new/P-N5-ASC-fixes.md
  (append-only) + a line file by script, repin asc.pins, update the check.sh block. Never edit the frozen packet.
- M = 8, A = 1 (dp193b): the old run's checkpoint is lost (stopped 97.5%, f_1(8) >= 106 per the Lead). Next after «go»: build
  dp193b in the scratchpad, rerun `dp193b 8 1 <ckpt outside repo>` as tracked 2-h tasks, resuming; report exact f_1(8) vs the cubic's 128.
- BOX 194 (D_E to R): (a) remove [LOC] from OVT-DV or prove IN-BOUND (abstract CS model first); (b) remove [E-LEV] via R104 / R117
  Γ3 encoding, or an e-order where UP-B fails, with instance; (c) D18 angle: wqo / Higman-Kruskal / tableau structure for
  ω(1)-ascent hubs. Next: read docs/new/N5-ASC-box193.md Add. 2-4, box 192 Add. 9 (IN-BOUND), L-RED R217 §2 (OVT-DV [LOC]).
- Nothing of mine running.

### 3. docs/GAPS.md rows I own (`git show trunk:docs/GAPS.md | grep -n L-NEW`)
- G-N5-TIME (l.11): major; owner «L-NEW (L-LIT T22; referees later)»; status **open**.
- G-N1-LB (l.10): minor; owner «L-NEW (optional; not routed)»; status **open**.
- G-N5-TERM (l.16): major; owner «L-NEW (L-COMP checks runs)»; status **closed** (RESULTS R15).

### 4. Three owner rulings (verbatim; status from docs/DECISIONS-INDEX.md)
1. D18 (INDEX l.32, **active**): «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas
   from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed,
   state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.»
2. D14 (INDEX l.22, **active**): «You know it can also test prveiously not tested approaches, it can come up with it own as well»
3. D1 (INDEX l.5, **active**; excerpt): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such
   claim, including the fleet's own, as wrong until it passes the gauntlet below.»

### 5. One trap, and the check that prevents it
- Trap (successor 61): a long job (dp193b M = 8, A = 1) kept its checkpoint in scratch inside the old container and ran as a
  detached job; the container was reclaimed at 97.5% and both the checkpoint and the value were lost.
- Check now: long jobs run only as tracked background tasks (2-h timeout), resumable, with the checkpoint outside the repo tree;
  the partial value is written into the notebook / reported at each turn, so a restart loses at most one checkpoint interval.
- Also kept: start push.sh from the repo root, after `pgrep -f "bash scripts/push.sh"`; no files created in lane dirs while it runs.
