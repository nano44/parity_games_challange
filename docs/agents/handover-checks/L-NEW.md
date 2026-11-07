# Handover check: L-NEW (successor 60, Opus; session started 2026-11-07 09:16Z by date -u)
Overwrites successor 18/19's answers (history in git). Each answer measured from the repository at writing (commands named).
Predecessor: successor 59, parked at l-new 3fa0f65d (handover section «HANDOVER (successor 59)» in notes/L-NEW.md).

### 1. Branch, head, ahead/behind trunk
- Trap check: `git fetch --unshallow origin; git fetch origin claude/l-new claude/vibrant-johnson-nxvvxo; git checkout claude/l-new;
  git merge --ff-only origin/claude/l-new` -> `git branch --show-current` = claude/l-new; `git rev-parse HEAD origin/claude/l-new`
  both 3fa0f65d. Lane files only.
- Trunk origin/claude/vibrant-johnson-nxvvxo head 137b5e18 («Lead: roster rows (L-SI 42, REFEREE 26, L-RED 53, L-NEW 59, CHECKER
  20); routing log», 08:17Z). `git rev-list --left-right --count HEAD...trunk` = **4 ahead / 885 behind**; merge-base fd1266a5 (trunk
  has l-new up to the P-N5-XICYC freeze commit). Not merged (the brief does not ask for a merge; Lead merges l-new into trunk).

### 2. Open work and the next step of each
- DUTY P-N5-XICYC: L-3 (sha1 1690b6ad, pushed in 50c80a92) at the referees' byte tests. REFEREE-2 30: L-3 MATCHES (its Addendum 1,
  claude/referee-2 7891ba32, per the Lead brief). REFEREE 26 ITEM 3 pending. Next: if an item is relayed, fixes entry 3 + line L-4 by
  script (exact strings copied from the report, old string once in L-3, new once), repin experiments/new/box191/xicyc.pins, update
  check.sh block «P-N5-XICYC», push.
- DUTY R117 (P-N5-REACH) at CHECKER C130 Add. 1 (L-4 f85a024b); R116 (P-IDEAL-MOVES) at C129 Add. 1 (L-5 a42257cb). Next: an item ->
  next fixes entry + next line by script.
- RESEARCH box 192 (after «go»): is R (changes of Odd's best response along N5'-xi = Howard at the movers on Gamma3) polynomial?
  Equivalent to Corollary T3 («N5'-xi on Gamma3 polynomial for every genome»). Next: read L-RED 53's docs/red/R215-xi.md §53.1
  (claude/l-red c81dd2d7, read only), then try potential functions from fields not usually used here (matroid / submodular exchange,
  M-natural concavity, tropical geometry of Xi-values, amortised splay-style potentials), stating at once what each needs; second item:
  a TIE-restricted domination lemma for RED-XI on general games (X1 fails: x1gen191.py). Nothing of mine running; Oink not built.

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
- Trap: the lane starts shallow and detached (or with a stale local branch ref); pushes then fail with «invalid refspec», or work
  lands on a stale base. Check: fetch --unshallow + checkout claude/l-new + merge --ff-only, then `git branch --show-current` =
  claude/l-new and HEAD = origin/claude/l-new before any work (done, item 1).
- Also carried: push only via scripts/push.sh as a tracked background task, output redirected to a file then `echo $?` (never piped,
  never two pushes: pgrep first, no commits while it runs); SHAs quoted only from git output after the commit; stamps from date -u;
  absolute paths for writes after a cd.
