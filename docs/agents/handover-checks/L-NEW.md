# Handover check: L-NEW (successor 78; started 2026-11-14 13:44Z, written 2026-11-14T13:45Z by date -u)
Overwrites successor 77's answers (history in git). Each answer measured from the repository at writing (commands named).
Predecessor: successor 77, parked at l-new 0c18fbba (section «HANDOVER (successor 77, PARKING; written 2026-11-13 14:05Z by date -u …)»
at the top of notes/L-NEW.md). Brief: Lead message of 2026-11-14 13:42Z (DESIGN DAY, design lane A; «go» given in advance).

### 1. Branch, head, ahead/behind trunk
- Trap check, as briefed: `git fetch origin claude/l-new` then `git rev-parse HEAD origin/claude/l-new`: both
  0c18fbba48264c379c7d1d7d91e6c65fb8f6b816; `git status`: on claude/l-new, clean; `git rev-parse --is-shallow-repository` = false.
  This container was NOT stale (0 behind).
- Trunk origin/claude/vibrant-johnson-nxvvxo at my fetch (13:44Z): aeb90ac199aff97b7189666965d7fd7d7119cf29 («Lead: log 17:31Z-19:03Z …»,
  committed 2026-11-13T19:04:18Z). `git rev-list --left-right --count trunk...HEAD` = 538 / 23: **23 ahead / 538 behind**;
  `git merge-base` = 366a38ab. Not merged by me (the brief does not ask for a merge).
- RESULTS on that trunk: `grep -c '^### R'` = 130; R130 present, R131 NOT yet (the brief says its landing is in its last steps).

### 2. Open work and the next step of each
- Item 1 (TODAY, the brief): design ONE new candidate deterministic algorithm, N12 (next free number: N11 = N5-HT, dead, box 23), outside
  the N5 scheme or changing it at the root; docs/new/N12-proposal.md within 60-90 min (exact pseudocode; polynomial on BOTH kill
  families Γ3(G_k) and W(G_n, ι) / W(switchallexp_n) by argument or measurement; first barrier statement; my own best guess of what
  kills it; PROVED / DATA / CONJECTURE labels). Next step: read the kill families' generators (claude/l-red-b experiments/red-b/gk.py
  and data/b6b/pg/; claude/l-si experiments/si/box104/inst), choose the candidate within the first hour, write the proposal.
- Item 2: one implementation with regions AND positional strategies, 10,000 random games against Zielonka / Oink, growth tables on the
  kill families and the M1 hard families (experiments/new/n12/). Item 3: message to the Lead naming the candidate ready for attack.
- If N12 dies on my own tests: dead end recorded with the exact instance, next idea the same hour.
- Standing, NOT to be touched without the Lead's word (predecessor's NEEDS 1-2): P-N5-KEY1P is frozen (docs/new/P-N5-KEY1P.md, sha1
  f7191623…); its post-kill fixes entry waits for P-N5-EXP to land as R131 (draft: docs/new/P-N5-KEY1P-after-EXP-draft.md).
- Earlier candidates of this lane and what killed each (docs/new/README.md, c-lane-synthesis.md, N11-proposal.md): N1 DISC-ANNEAL
  (deep-trap switchallexp, one phase = Howard from the best-reward start), N2 PRIO-ANNEAL (padded switchallexp), N3 BLACKWELL-PATH (one
  degenerate breakpoint = a parity solve), N4 tropical simplex (proposed, never run), N5 SSI-GLOBAL (dead by P-N5-EXP: 2^k + 1
  iterations on Γ3(G_k), RIPPLE), N6 IPM-LCP and N7 entropic homotopy (κ / 1/(1−γ) exponential for parity; no answer on counter_ortl
  N = 3), N8a Koh-Loho tree SI with a global pivot (L_k: 3·n^(k+1) pivots), N8d (delay lanes HLg_k), N9a SA+ of ACYC (circ(n,1,2):
  level ⌈n/3⌉), N9b LP-guided peeling (STUCK, n = 5), N10a-c escape cuts (two-player gaps; τ cannot be guessed from the LP), N11 N5-HT
  (replays switch-all on switchallexp / switchbestexp), N5′-xi (R130, W(G_n, ι)), N5-SF (DE35).
- Running at writing: `scripts/setup_oink.sh` (tools/oink absent in this container; tracked background task). Nothing else.

### 3. docs/GAPS.md rows I own (`git show trunk:docs/GAPS.md | grep -n L-NEW`, trunk aeb90ac1)
- G-N5-TIME (l.11): major; owner «L-NEW (L-LIT T22; referees later)»; status **open** on this trunk (the kill packet's landing as R131
  will settle it as false for N5 as specified; not mine to edit).
- G-N1-LB (l.10): minor; owner «L-NEW (optional; not routed)»; status **open**.
- G-N5-TERM (l.16): major; owner «L-NEW (L-COMP checks runs)»; status **closed** (RESULTS R15).

### 4. Three owner rulings (verbatim; status from docs/DECISIONS-INDEX.md on trunk aeb90ac1)
1. D14 (INDEX l.22, **active**; text docs/DECISIONS.md l.246): «You know it can also test prveiously not tested approaches, it can come
   up with it own as well».
2. D18 (INDEX l.32, **active**; text docs/DECISIONS.md l.333): «Focus on N5 and work toward proving it. Explore novel approaches,
   especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable
   assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from
   conjectures and open problems.»
3. D1 (INDEX l.5, **active**; docs/decisions/D001-launch-brief.md l.25-26): «A claimed polynomial algorithm is far more likely to be
   wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.»
- NOT measured on trunk (absent from DECISIONS-INDEX.md at aeb90ac1, whose last owner row is D26; quoted here from the Lead's brief of
  13:42Z, which says they are in its push): D27 (2026-11-14) «SO we have to look for a new algorithm no? Do we have any promising lead
  or can convert our learning into a new promising algorithm?»; D28 «I reset everything, you have until 11PM to use a full 100% usage»;
  Lead reading L61 (today is a DESIGN DAY; this lane is design lane A). To re-check against DECISIONS.md once the Lead's push shows.

### 5. One trap, and the check that prevents it
- Trap (this lane, twice in its record): a candidate is declared «surviving» on families where its own implementation silently differs
  from its pseudocode, or a «kill» comes from an unfaithful engine (CLAUDE.md Traps, last line; N1's wrong stop test in box 1).
  Check for N12: the proposal's pseudocode is frozen with a sha1 BEFORE the growth tables are produced; every reported run is verified
  (regions against Oink / Zielonka AND both positional strategies by an independent one-player check); every counter that must be 0
  has a firing control.
- Push trap kept from successors 71-77: push only with scripts/push.sh as a tracked background task, output redirected to a file, then
  `echo exit $?`; never a pipe; `pgrep -f "bash scripts/push.sh"` before any push (never two); no commit while a push runs; compare
  `git ls-remote origin claude/l-new` with my SHA afterwards; on non-fast-forward: `git merge --no-ff origin/claude/l-new`, never rebase.
- Stamp trap: timestamps only from `date -u` output of the same command; SHAs only from git output.
