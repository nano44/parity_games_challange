# Handover check: L-NEW (successor 61, Opus; session started 2026-11-07 18:57Z by date -u)
Overwrites successor 60's answers (history in git). Each answer measured from the repository at writing (commands named).
Predecessor: successor 60, parked at l-new 589c9fba (handover section «HANDOVER (successor 60, …)» in notes/L-NEW.md).

### 1. Branch, head, ahead/behind trunk
- Trap check: `git fetch --unshallow origin; git fetch origin claude/l-new claude/vibrant-johnson-nxvvxo; git checkout claude/l-new;
  git merge --ff-only origin/claude/l-new` (local branch was 975 commits behind: stale container, fast-forwarded) ->
  `git branch --show-current` = claude/l-new; `git rev-parse HEAD origin/claude/l-new` both 589c9fba.
- Trunk origin/claude/vibrant-johnson-nxvvxo head 762c2184 («Lead: roster L-LOWER 7, L-RED 55; restart rows; log», 18:20Z).
  `git rev-list --left-right --count HEAD...trunk` = **5 ahead / 55 behind**; merge-base 478d0bd9 (= the R118 landing commit).
  Not merged (the brief does not ask for a merge).
- CI on the lane head (GitHub MCP actions_list, branch claude/l-new): run 6803 on 589c9fba IN PROGRESS (started 18:52Z);
  run 6798 on 57cae1c0 IN PROGRESS (started 18:23Z); last completed: 6786 on d2295934 SUCCESS, 6772 on 89a033ef SUCCESS.

### 2. Open work and the next step of each
- DUTIES: none open. R116, R117 (REACH3) and R118 (XICYC) are LANDED (trunk docs/RESULTS.md l. 13362 R117, l. 13607 R118);
  stay ready for any CHECKER / referee item on them (an item -> next fixes entry + next line by script).
- RESEARCH box 193 (after «go»), the PROOF side of the open core: R polynomial <=> R_mov polynomial (R-SPLIT, [LOC]) <= D(v)
  polynomial (OVT-DV) <= CONJECTURE IN-BOUND + polynomial height of REALISABLE e-set walks on one vertex's plays («no 3-bit counter
  under E-DOM in any architecture»). Next: read docs/new/N5-RPOT-box192.md and docs/red/R217-ovt.md (claude/l-red, read only);
  check each lane lemma used (E-DOM-ALL-d, E-DOM-CHOICE, LEAK-ARCH, CHAIN-SHIELD, HIDE-BUSY; my MERGE, EQ-FLIP, A10 e-part
  monotone) on pinned instances; then try to prove «lane re-arms <= poly» by generalising LEAK-ARCH / CHAIN-SHIELD without H1-H2
  (classify how a lane's exits come to beat its chain again, from R104's model + E-DOM + MERGE only), and IN-BOUND. If the proof
  fails: the escaping architecture as an instance, to L-RED via the Lead. Nothing of mine running; Oink not built.

### 3. docs/GAPS.md rows I own (`git show trunk:docs/GAPS.md | grep -n L-NEW`)
- G-N5-TIME (l.11): major; owner «L-NEW (L-LIT T22; referees later)»; status **open**.
- G-N1-LB (l.10): minor; owner «L-NEW (optional; not routed)»; status **open**.
- G-N5-TERM (l.16): major; owner «L-NEW (L-COMP checks runs)»; status **closed** (RESULTS R15).

### 4. Three owner rulings (verbatim; status from docs/DECISIONS-INDEX.md on trunk)
1. D18 (INDEX l.32, **active**): «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas
   from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed,
   state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.»
2. D14 (INDEX l.22, **active**): «You know it can also test prveiously not tested approaches, it can come up with it own as well»
3. D1 (INDEX l.5, **active**; excerpt): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such
   claim, including the fleet's own, as wrong until it passes the gauntlet below.»

### 5. One trap, and the check that prevents it
- Trap (successor 60): ABSOLUTE PATH: a tool copied from scratch kept ROOT=/home/user/...; it passed in the container and failed
  in CI for six runs (6692-6715). Check: `grep -rn '/home/user' experiments/new/` before every commit, and run a relocated copy of a
  new tool with the repo path hidden.
- Also caught again this time: stale container (local claude/l-new 975 behind); fetch + ff-only + HEAD = origin check (item 1).
- Carried: push only via scripts/push.sh as a tracked background task, output redirected to a file then `echo $?` (never piped,
  never two pushes: pgrep first, no commits or lane-file edits while it runs); SHAs quoted only from git output; stamps from date -u.
