# Handover check: L-NEW (successor 75; session session_01V5yGRWimvjsi2nZhjaevtK; started 2026-11-13 ~03:03Z, written 2026-11-13T03:04Z by date -u)
Overwrites successor 74's answers (history in git). Each answer measured from the repository at writing (commands named).
Predecessor: successor 74, parked at l-new 565b6d28 (section «HANDOVER (successor 74, …)» at the top of notes/L-NEW.md).
Clock: `date -u` 03:03:52Z against the `date:` header of raw.githubusercontent.com (03:03:52 GMT) in the same command: skew 0 s (< 1 s).

### 1. Branch, head, ahead/behind trunk
- Trap check, as briefed: `git fetch --unshallow origin; git fetch origin claude/l-new claude/vibrant-johnson-nxvvxo;
  git checkout claude/l-new; git merge --ff-only origin/claude/l-new`. The container came up on claude/l-new but 9 commits BEHIND
  origin/claude/l-new (fast-forwarded to 565b6d28); `git rev-parse --is-shallow-repository` = false after the unshallow.
  `git branch --show-current` = claude/l-new; `git rev-parse HEAD origin/claude/l-new` both 565b6d285e50b25d37865074241f5354b7c242f0.
- Trunk origin/claude/vibrant-johnson-nxvvxo head at my fetch (03:04Z): e8b6abf0 («Lead: log 00:27Z-00:54Z (P-N5-LEVEL L-2 two-referee
  MATCH; …)», committed 2026-11-13T00:55:02Z). `git rev-list --left-right --count trunk...HEAD` = 385 / 17: **17 ahead / 385 behind**;
  merge-base 621e6b77 (unchanged since successors 73 and 74). Not merged by me (the brief does not ask for a merge).

### 2. Open work and the next step of each
- Item 0, notebook corrections credited «Lead 02:43Z» (first commit after «go»): (1) P-N5-LEVEL L-2 (366a38ab; line sha1 d18125ed,
  re-measured by sha1sum now; packet 7c956df4, L-1 28565b3c unchanged) MATCHES at both referees (REFEREE 34 §8, claude/referee
  98cdc7aa + 28b95151; REFEREE-2 39 Addendum 2, 5bba2b8e); R129 drafted by the Lead (docs/agents/R129-draft.md is NOT on trunk e8b6abf0
  at my fetch: `git show trunk:docs/agents/R129-draft.md` fails) and goes to CHECKER as C144; nothing owed by L-NEW. (2) «N-L1» CLOSED
  (Lead's labelling error; no change to L-2 or the fixes file; CHECKER flag G-NL1).
- Item 1, BOX 213 KEY-WINDOW (approved): first deliverable = the τ-arena form of RF-B: (P1)-(P5′) restated with Odd fixed at τ (SPEC S4a
  optimises against N5's τ, pe at every gate, not σ̄), with a proof, or a precise statement of what fails with instances. Until then
  RF-D stays CONDITIONAL with that named gap. Inputs to weigh, each cited as what it is: L-COMP BOX 46 (6ac85200; «window-used», odd Ξ
  self-loops inert on towers), L-RED-B 3 FLAT-IDX / L-RED R240 (only the ≤ |E(H)| H-move bound «hbound» is numbering-free; credit
  L-RED-B if made a lemma), L-RED R239 (2cc894f2: RF-A/B/C survive), L-FORMAL 4 Lean definitions of S1-S5, REFEREE-2 40's pre-read.
  Next step: read SPEC S4a and arena213.py + its frozen output (successor 74: τ constant before the first fallback, N5 moves each mover
  to a Ξσ-best gate except 187 of 6,107 moves on 12 genomes), then write the box 213 STATEMENT (statement, kill criteria, DATA plan
  with must-0 counters and firing controls, what is NOT claimed) and send it to the Lead before any long run.
  Sources: Post-Ye arXiv:1208.5083 v2 opened (Thm 3.7, 4.8; discounted γ < 1, single-switch Dantzig, not policy iteration);
  Hansen-Kaplan-Zwick full text NOT opened (abstract only): not citable until opened.
- Item 2, P-N5-LEVEL / R129: if CHECKER C144 routes an item back: fixes entry 2 + L-3 by script (box211 mkl2 pattern, asserting L-2's
  sha1 d18125ed); never edit the frozen packet, L-1 or L-2.
- Boxes 209, 210, 212: CANDIDATES under attack; answers are append-only addenda.
- Running at writing: nothing. `scripts/setup_oink.sh` ran first (tools/oink was absent; built at 8fbf0a7, exit 0).
  `pgrep -af "push.sh|verify.sh|check.sh|python"` = none before it. No research job started.

### 3. docs/GAPS.md rows I own (`git show trunk:docs/GAPS.md | grep -n L-NEW`, trunk e8b6abf0)
- G-N5-TIME (l.11): major; owner «L-NEW (L-LIT T22; referees later)»; status **open** (last UPDATE in the row: 2026-11-12 13:58Z,
  R127 landed). Neither P-N5-LEVEL, box 212 nor box 213 closes it.
- G-N1-LB (l.10): minor; owner «L-NEW (optional; not routed)»; status **open**.
- G-N5-TERM (l.16): major; owner «L-NEW (L-COMP checks runs)»; status **closed** (RESULTS R15).

### 4. Three owner rulings (verbatim; status from docs/DECISIONS-INDEX.md on trunk e8b6abf0)
1. D18 (INDEX l.32, **active**; text docs/DECISIONS.md l.333): «Focus on N5 and work toward proving it. Explore novel approaches,
   especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable
   assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from
   conjectures and open problems.»
2. D14 (INDEX l.22, **active**; text docs/DECISIONS.md l.246): «You know it can also test prveiously not tested approaches, it can come
   up with it own as well»
3. D1 (INDEX l.5, **active**; excerpt, docs/decisions/D001-launch-brief.md): «A claimed polynomial algorithm is far more likely
   to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.»
- Also in force: D21 (INDEX l.46, **active**) with Lead readings L51 (l.48: maximum effort until 2026-11-14 10:05Z), L52 (l.49) and
  L53 (l.50, now on trunk: Fable 5.2 weekly limit reached, resets 2026-11-18 21:00Z; successors on Opus 5.5 high). If my turn fails on
  a limit I resume from notes/L-NEW.md when woken.

### 5. One trap, and the check that prevents it
- Trap (this lane, many starts; this start: 9 commits behind): the container starts shallow, stale or detached; a commit there forks
  history and the push fails («invalid refspec» on a detached HEAD) or is rejected as non-fast-forward.
- Check: fetch --unshallow + fetch the branches by name, checkout + merge --ff-only, then `git branch --show-current` and
  `git rev-parse HEAD origin/claude/l-new` must agree before any edit (done: claude/l-new, both 565b6d28, not shallow). Before my own
  push: re-fetch and ff-only again (successor 74 may still push a notebook correction); on a non-fast-forward refusal, merge
  origin/claude/l-new with --no-ff (never rebase, never force) and re-push.
- Also kept: the box 213 trap my predecessor found: «N5's step = Howard on a subset» is FALSE (187 of 6,107 moves on 12 genomes go to a
  non-Ξσ-best gate): every identification is checked by a counter on the frozen + tower set before it is written as a statement; never
  edit a script while a job uses it; a push runs ~40-70 min of verify during which nothing is committed (`pgrep -f "bash scripts/push.sh"`
  first; never two pushes); no model name in commits; SHAs only from git output in a later step; times from `date -u`.
