# Handover check: L-NEW (successor 73; session started 2026-11-12 ~17:09Z, written 2026-11-12T17:12Z by date -u)
Overwrites successor 72's answers (history in git). Each answer measured from the repository at writing (commands named).
Predecessor: successor 72, parked at l-new 311bbf81 (section «HANDOVER (successor 72, …)» at the top of notes/L-NEW.md).
Clock: `date -u` 17:10:21-22Z against the `date:` header of raw.githubusercontent.com (17:10:22 GMT): skew <= 1 s. Responses from
github.com itself came through the proxy without a Date header (HTTP 400 on a HEAD request, no header on the git endpoint), so the
comparison is against GitHub's raw host, said plainly.

### 1. Branch, head, ahead/behind trunk
- Trap check, as briefed: `git fetch --unshallow origin; git fetch origin claude/l-new claude/vibrant-johnson-nxvvxo;
  git checkout claude/l-new; git merge --ff-only origin/claude/l-new`. The container came up ON claude/l-new, up to date, but SHALLOW
  (`git rev-parse --is-shallow-repository` = true before, false after the unshallow). `git branch --show-current` = claude/l-new;
  `git rev-parse HEAD origin/claude/l-new` both 311bbf81 (311bbf81faa525eda9c09ad15d0b0d170a2c25e9).
- Trunk origin/claude/vibrant-johnson-nxvvxo head at my fetch (17:12Z): 68c8d293 («Lead: R128 first fill (P-N5-GATE over L-4 6bfde78e
  …)», committed 2026-11-12T15:06:33Z). `git rev-list --left-right --count trunk...HEAD` = 377 / 8: **8 ahead / 377 behind**;
  merge-base 621e6b77 (the Lead merged l-new 621e6b77 for the R127 landing). Not merged by me (the brief does not ask for a merge).

### 2. Open work and the next step of each
- BOX 211 (after «go»): FREEZE PACKET P-N5-LEVEL = box 208 body + Addenda A, B as ONE packet (PR-6 resolved by the Lead: one packet;
  box 209 NOT included), file docs/new/P-N5-LEVEL.md, packet form of the frozen P-N5-SPLIT (399cda07). Next step: write it from
  docs/new/N5-LEVEL-box208.md with (i) title and scope exactly as briefed (Howard ALL-SWITCH, Even = maximiser improves, switch-best
  with keep-if-best ties, VJ values, on IDEAL-CYC(G) for every R104 genome; single-switch rules not covered; fails on Friedmann's G_N
  at (K5), as DATA from L-COMP BOX 43; not N5, not N5′-xi off Γ3, not M4; G-N5-TIME stays OPEN); (ii) premises by landed R-id only,
  each quoted BY SCRIPT at a pinned trunk commit (R104 with readings (D1), (D3), (D4); R118 (a), (b) F1, (c) DOM, (e)'s reason,
  (i) BR-SEG-G with H0; R121 E-MON, E-DOM; R123 CN2, B-ONLY, NO-TIE, LOC-GATE, LOC-K2, [OPT]; R126 QUIET-N), no lane lemma as a
  premise; (iii) REFEREE 32's PR-1..PR-5 each applied and located; (iv) L41 names for every referee- or adversary-originated step
  (G-P6's repair: REFEREE 32; G-1: L-RED-B; SHARP: L-RED 66, only if proved inside the packet); (v) L43: finite-instance asymptotics
  as DATA with its counter; (vi) every genome-only step named ((K2) / (K3 (b), (d)) from B-ONLY + E-DOM; QUIET-N in WIN (iii) and
  (P4); (K5) from DOM); (vii) ALL-TCYC's constant exactly as Addendum A states it; (viii) the statement diffed against TARGET.md
  §2 / §4 inside the packet. Then: freeze commit, push, send the Lead the freeze SHA and the file's sha1.
- BOX 212 (while REFEREE 33, then REFEREE-2, read): own design (D14) on the open links for N5 from L-SI 52's box 104 map: O1 (tower
  on R104 genomes), O2 (the key rule on free-priority genomes), O3 (R90's B*, REP*, SC*, O* off the Γ3 shape). Next step: read box
  104 on claude/l-si, then PROPOSE one box to the Lead (statement, DATA plan, kill criterion) before starting it.
- Standing duty, P-N5-SPLIT = R127: LANDED on trunk (f9520557 «Lead: land R127 (P-N5-SPLIT) after CHECKER C141 PASS (850e9765)»).
  Open only if a C141 Add. 1 / R127 item is routed: fixes entry 5 (append-only) + line L-4 by script; never edit the frozen packet.
- Standing: findings by L-RED / L-RED-B / L-COMP / L-SI / referees on boxes 208-210 are answered as APPEND-ONLY addenda (boxes 209,
  210 are still under attack per the Lead's log; they are not part of BOX 211).
- Reading still owed before «go» (reading only, no long job): box 208 body + Addenda A, B; box 209 + Add. A; box 210 + Add. A;
  P-N5-SPLIT (form); claude/referee R-box208-preread.md §9; claude/l-red R235-box208.md; claude/l-red-b (G-1); claude/l-comp
  experiments/comp/box43/README.md; claude/l-formal lean/lemmas/README.md + INDEX (f74d38a4).
- Running at writing: only `scripts/setup_oink.sh` (tools/oink was absent in this container; the gate's Oink step and two other
  lanes' check.sh files use it). `pgrep -af "push.sh|verify.sh|check.sh"` = none before this push. No research job started.

### 3. docs/GAPS.md rows I own (`git show trunk:docs/GAPS.md | grep -n L-NEW`, trunk 68c8d293)
- G-N5-TIME (l.11): major; owner «L-NEW (L-LIT T22; referees later)»; status **open** (last UPDATE in the row: 2026-11-12 13:58Z,
  R127 landed). Box 208 / the packet does not close it (IDEAL-CYC on Γ(G) only).
- G-N1-LB (l.10): minor; owner «L-NEW (optional; not routed)»; status **open**.
- G-N5-TERM (l.16): major; owner «L-NEW (L-COMP checks runs)»; status **closed** (RESULTS R15).

### 4. Three owner rulings (verbatim; status from docs/DECISIONS-INDEX.md on trunk 68c8d293)
1. D18 (INDEX l.32, **active**; text docs/DECISIONS.md l.333): «Focus on N5 and work toward proving it. Explore novel approaches,
   especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable
   assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from
   conjectures and open problems.»
2. D14 (INDEX l.22, **active**; text docs/DECISIONS.md l.246): «You know it can also test prveiously not tested approaches, it can come
   up with it own as well»
3. D1 (INDEX l.5, **active**; excerpt, docs/decisions/D001-launch-brief.md l.25-26): «A claimed polynomial algorithm is far more likely
   to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.»
- Also in force, D21 (INDEX l.46, **active**; text docs/DECISIONS.md l.452, relayed by OWNER-DESK): «Okay, I want maximum effort. I
  want to use 200% usage in 3 days. There is fable 5.2 as well, use that too in dpeth everywhere where it seems fitting, use fable 5.2
  at hard or xhigh. SO yes, 200% uage under 2 days.» Lead reading L51 (INDEX l.47, active): maximum effort until 2026-11-14 10:05Z.
  If my turn fails on a usage limit I resume from notes/L-NEW.md when woken.

### 5. One trap, and the check that prevents it
- Trap (this lane, many starts; this start in its mild form): the container starts shallow and sometimes detached or far behind
  origin/claude/l-new; a commit there forks history and the push fails («invalid refspec» on a detached HEAD).
- Check: fetch --unshallow + fetch the branches by name, checkout + merge --ff-only, then `git branch --show-current` and
  `git rev-parse HEAD origin/claude/l-new` must agree before any edit (done: claude/l-new, both 311bbf81, not shallow).
- Also kept from successor 72: never edit a script or tool while a job that uses it runs; numbers in a doc come from a summary script
  after the outputs are final; a push runs ~40-60 min of verify, during which nothing is committed and no lane file is created
  (`pgrep -f "bash scripts/push.sh"` first; never two pushes); no model name in commits, headers or docs (trailer = the
  Claude-Session line of THIS session only); SHAs quoted only from git output, in a step after the commit; times from `date -u`.
