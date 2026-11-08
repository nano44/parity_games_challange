# Handover check: L-NEW (successor 64, Opus; session started 2026-11-08 05:46Z, written 05:48Z by date -u)
Overwrites successor 63's answers (history in git). Each answer measured from the repository at writing (commands named).
Predecessor: successor 63, parked at l-new 1a846565 (handover section «HANDOVER (successor 63, …)» in notes/L-NEW.md).

### 1. Branch, head, ahead/behind trunk
- Trap check: `git fetch --unshallow origin; git fetch origin claude/l-new claude/vibrant-johnson-nxvvxo; git checkout claude/l-new;
  git merge --ff-only origin/claude/l-new` (local branch was 999 commits behind: stale container, fast-forwarded) ->
  `git branch --show-current` = claude/l-new; `git rev-parse HEAD origin/claude/l-new` both 1a846565.
- Trunk origin/claude/vibrant-johnson-nxvvxo head c8f42538 («Lead: REFEREE-2 33 roster + restart row; L-RED 58 check scored 5/5 + GO
  R223; …», 05:05Z). `git rev-list --left-right --count trunk...HEAD` = **9 ahead / 115 behind**; merge-base a2024f59.
  Not merged (the brief does not ask for a merge).

### 2. Open work and the next step of each
- DUTY P-N5-END (frozen 131b4c1c, docs/new/P-N5-END.md sha1 5cae845b, 22967 B; under L-RED 58 R223 and REFEREE 29): no line yet.
  Next after «go», first: write docs/new/P-N5-END-line-L1.txt by script (model: P-N5-ASC L-4, P-N5-QUIET L-1; END-T3's REACH3-CYC
  condition in the line; TARGET.md scope clause; no «|»), pin in box195/end.pins, push, send the Lead sha1 + wc -c.
- DUTY P-N5-ASC (L-4 a744677e, sha1 4017305a, 5198 B): at byte tests (REFEREE 29, REFEREE-2 33), then R121 second fill, CHECKER C135
  Add. 1. Next: answer any CHECKER item (fixes entry 5 + L-5 by script, repin asc.pins).
- DUTY P-N5-QUIET (frozen 9329859d; L-1 df0d2a25): REFEREE 28 SIGNs all, L-1 NOT YET (QT-L1..QT-L6). DRAFT fixes entry 2 + L-2 in
  experiments/new/box194/draft_entry2/ (NOT ROUTED). Next: wait for REFEREE-2 33's report, then ONE fixes entry 2 for both referees.
- BOX 196 «CLOSE THE Γ3 CHAIN»: (a) the exact chain to «under [E-LEV], bounded U(G) => N5′-xi from S3 on Γ3(G) polynomial», each link
  labelled; (b) attack the weakest OPEN link (REACH3-CYC premises for cyclic genomes, or the Γ3 transfer of T-QUIET at exact VJ ties).
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
- Trap (this start, again): the container came up 999 commits behind origin/claude/l-new; a commit there would have forked history
  and the push would fail (or a detached HEAD gives «invalid refspec»).
- Check: fetch --unshallow + fetch both branches, checkout + merge --ff-only, then `git branch --show-current` and
  `git rev-parse HEAD origin/claude/l-new` must agree before any edit.
- Also kept: push.sh takes ~20-25 min and a container restart can kill it mid-verify: after any restart compare HEAD with origin and
  relaunch; nothing created in lane dirs (even untracked) while a push runs; heredocs always quoted (<<'EOF').
