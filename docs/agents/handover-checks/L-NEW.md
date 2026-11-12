# Handover check: L-NEW (successor 74; session session_01V5yGRYHKYSjsfxFEDcsyEP started 2026-11-12 ~19:58Z, written 2026-11-12T19:59Z by date -u)
Overwrites successor 73's answers (history in git). Each answer measured from the repository at writing (commands named).
Predecessor: successor 73, parked at l-new 069c888b (section «HANDOVER (successor 73, …)» at the top of notes/L-NEW.md).
Clock: `date -u` 19:58:47-48Z against the `date:` header of raw.githubusercontent.com (19:58:48 GMT) in the same command: skew <= 1 s.

### 1. Branch, head, ahead/behind trunk
- Trap check, as briefed: `git fetch --unshallow origin; git fetch origin claude/l-new claude/vibrant-johnson-nxvvxo;
  git checkout claude/l-new; git merge --ff-only origin/claude/l-new`. The container came up on claude/l-new but 3 commits BEHIND
  origin/claude/l-new (fast-forwarded to 069c888b); `git rev-parse --is-shallow-repository` = false after the unshallow.
  `git branch --show-current` = claude/l-new; `git rev-parse HEAD origin/claude/l-new` both 069c888b6d0ab6bc124e32424f50f4372da0a4a1.
- Trunk origin/claude/vibrant-johnson-nxvvxo head at my fetch (19:58Z): 7fa6aff4 («Lead: CI job lean-lemmas (separate from the
  gate) …», committed 2026-11-12T17:10:52Z). `git rev-list --left-right --count trunk...HEAD` = 379 / 11: **11 ahead / 379 behind**;
  merge-base 621e6b77 (unchanged since successor 73's check). Not merged by me (the brief does not ask for a merge).

### 2. Open work and the next step of each
- DUTY 1, P-N5-LEVEL (frozen at 1e6df499; docs/new/P-N5-LEVEL.md sha1 7c956df443cfddbf23bfbaa18a26a98369b176ec; proposed line
  docs/new/P-N5-LEVEL-line-L1.txt sha1 28565b3c60fe8167f4b660c83fa27c00cd7b4fe9; both re-measured by sha1sum now): under review by
  REFEREE 34 (first) and REFEREE-2 39 (second). Nothing routed to me yet; docs/new/P-N5-LEVEL-fixes.md does not exist. Next step on
  the first routed item: fixes entry 1 (creates the file, append-only) + line L-2 by script (experiments/new/box211/mkl2_211.py on
  the pattern of mkl1_211.py, asserting L-1's sha1 28565b3c and the packet's 7c956df4), both added to box211/level.pins and the
  check.sh block «P-N5-LEVEL»; never edit the frozen packet or L-1. Also: box 209's pre-read notes N-1..N-3 (claude/referee
  90703a81, R-box209-preread.md) go into a box 209 Addendum B (append-only) when there is room.
- BOX 212 RF-LEVEL (approved by the Lead 18:32Z with changes (a)-(c)): RF-A (any improving rule obeying (K1)-(K4), (L1)-(L3), (L5)
  makes at most P = 2M(N + 2M) non-stall steps per reference state), RF-B (a plateau is a closed one-player frozen window), RF-C,
  RF-D (Γ3 form: reduces O1′ to the key rule on one-player frozen windows); kill criteria (i)-(iii); not a bound for N5; G-N5-TIME
  OPEN. Next step (change (a)): a dated per-lemma reading of whether R125's static lemmas (CN2-3, B-ONLY3, NO-TIE3, LOC-GATE3,
  LOC-K2-3) hold at every STANDARD state or only along HOW3; then the pluggable-rule counter on rv208's builder (DATA plan (a), (b)).
  Cite the Lean status as it stands on origin (claude/l-formal 6ed90b71 / e14f5508: Howard form, «the rule enters only at the
  stalls; the non-stall count is rule-free»), and W-FLAT (box 104, claude/l-si 26704e01) as the source of «not proposed».
- Boxes 209 and 210: still CANDIDATES under attack; answers are append-only addenda.
- Running at writing: only `scripts/setup_oink.sh` (tools/oink absent in this container; the gate's Oink smoke needs it).
  `pgrep -af "push.sh|verify.sh|check.sh"` = none before this push. No research job started.

### 3. docs/GAPS.md rows I own (`git show trunk:docs/GAPS.md | grep -n L-NEW`, trunk 7fa6aff4)
- G-N5-TIME (l.11): major; owner «L-NEW (L-LIT T22; referees later)»; status **open** (last UPDATE in the row: 2026-11-12 13:58Z,
  R127 landed). P-N5-LEVEL (IDEAL-CYC on Γ(G) only) does not close it; BOX 212 does not either.
- G-N1-LB (l.10): minor; owner «L-NEW (optional; not routed)»; status **open**.
- G-N5-TERM (l.16): major; owner «L-NEW (L-COMP checks runs)»; status **closed** (RESULTS R15).

### 4. Three owner rulings (verbatim; status from docs/DECISIONS-INDEX.md on trunk 7fa6aff4)
1. D18 (INDEX l.32, **active**; text docs/DECISIONS.md l.333): «Focus on N5 and work toward proving it. Explore novel approaches,
   especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable
   assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from
   conjectures and open problems.»
2. D14 (INDEX l.22, **active**; text docs/DECISIONS.md l.246): «You know it can also test prveiously not tested approaches, it can come
   up with it own as well»
3. D1 (INDEX l.5, **active**; excerpt, docs/decisions/D001-launch-brief.md l.25-26): «A claimed polynomial algorithm is far more likely
   to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.»
- Also in force: D21 (INDEX l.46, **active**) with Lead reading L51 (INDEX l.47: maximum effort until 2026-11-14 10:05Z) and L52
  (l.48). L53 (this session runs on Opus because the Fable weekly limit is reached, resets 2026-11-18 21:00Z) is in my brief but NOT
  yet in trunk's INDEX at 7fa6aff4 (last row L52, l.48). If my turn fails on a limit I resume from notes/L-NEW.md when woken.

### 5. One trap, and the check that prevents it
- Trap (this lane, many starts; this start in its mild form: 3 commits behind): the container starts shallow, stale or detached;
  a commit there forks history and the push fails («invalid refspec» on a detached HEAD) or is rejected as non-fast-forward.
- Check: fetch --unshallow + fetch the branches by name, checkout + merge --ff-only, then `git branch --show-current` and
  `git rev-parse HEAD origin/claude/l-new` must agree before any edit (done: claude/l-new, both 069c888b, not shallow).
- Also kept: never edit a script or tool while a job that uses it runs; numbers in a doc come from a summary script after the outputs
  are final; a push runs ~40-70 min of verify, during which nothing is committed (`pgrep -f "bash scripts/push.sh"` first; never two
  pushes); no model name in commits, headers or docs (trailer = this session's Claude-Session line only); SHAs quoted only from git
  output, in a step after the commit; times from `date -u`; a RESULTS line must not contain «|».
