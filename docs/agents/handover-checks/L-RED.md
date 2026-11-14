# Handover check: L-RED successor 72 (D1/D27/D28; LANE-RESTART step 3; written 2026-11-14T19:10Z by date -u)
Every answer is measured from the repository (commands named), not recalled. Predecessor: successor 71 (session_01V5yGRVyq25BY6qxdGPF1dD;
its handover is notes/L-RED.md «HANDOVER (successor 71 -> 72)», l. 3691; line 1 points to it; its last commit is f0ad3cca). This session
started 2026-11-14 15:12Z on the Lead's early-start brief (15:11Z) with a no-commit clause; the clause was lifted by the Lead's 15:32Z message
(read 19:05Z: the fleet's five-hour limit stopped this session at about 15:55Z, reset 18:30Z, Lead reading L52). Nothing was committed or
pushed before this file.

## 1. Branch, head, distance to trunk
- Trap check run first: `git fetch origin claude/l-red; git merge --ff-only origin/claude/l-red` -> the local branch was at 821d63e33
  (R247, one commit behind); fast-forwarded to f0ad3cca4.
- `git rev-parse HEAD` -> f0ad3cca4e3085b6973a91b1aaeba78be340662c; `git ls-remote origin refs/heads/claude/l-red` -> the same (19:05Z).
- Trunk claude/vibrant-johnson-nxvvxo = 37009aba5e898d4a9c54fa9af22d28c4a4a50e3c (committed 2026-11-14T15:39:46Z; ls-remote equal).
  `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` -> 226 1413, i.e. 226 ahead / 1413 behind;
  merge-base c2d1e88ee. Trunk is not merged in; truth docs are read with `git show origin/claude/vibrant-johnson-nxvvxo:<file>`.
- Lead session id in trunk docs/NOW.md (roster): session_014FBi6o334DvwT5Uw2kDfoN (equal to the brief's).
- Other heads by ls-remote (19:08Z): claude/l-red-b 18509d949, claude/l-si c236bca94, claude/l-new b4a9ae47b.

## 2. Open work and the next step of each
- Nothing running at this write (`pgrep -af "push.sh|verify.sh|climb|python"`: none; 4 CPUs, 15 GB). Oink built in this container
  15:14Z (`scripts/setup_oink.sh`, exit 0, «oink built at 8fbf0a7»).
- Successor 71's R246 (71894473), R247 (821d63e3) and R247 §8 (f0ad3cca: RC_n, RF n² + 3n − 2) are DONE and on origin.
- Done by this session in scratch (not committed; reported to the Lead 15:26Z): own engine rf248.py (one-sided VJ improvement, pluggable
  rule, own valuation by Odd-side improvement; Howard on Friedmann's G_n = 9·2^n − 10 at n = 1..7; RF on G_n = 5, 9, …, 27 at n = 1..8,
  0 Odd ties); a rebuild of RC_n from 71's description that gives n² + 3n − 2 at n = 2..12, 16, 20 once the side door hh_i is even and
  above e_i. The work on RC_n's open step is STOPPED by the Lead's 15:47Z message (RF is dead in DATA on K^s_n, two builds).
- QUEUE (the Lead's 15:47Z and 19:05Z messages), in order:
  (1) this handover check (commit by explicit path, scripts/push.sh as a tracked background task, ls-remote compared after it);
  (2) K^s_n (L-RED-B 8's kill family for RF) rebuilt from the rule text on rf248.py: the counts as ONE message (expected 2, 7, 19, 45,
      99, 209, 431, 877, 1771 = 7·2^(n−1) − 2n − 3 at n = 1..9), at most 15 minutes;
  (3) NEW TARGET: lane A's candidate N13 «SEESAW» (L-NEW 78; exact pseudocode to be relayed word for word by the Lead). Until it
      arrives: open arXiv 2110.04533v1 §3 (source into the notebook), build the frame (weights (−1)^pr(v)·(n+1)^pr(v) on the edges
      leaving v, modified weights under a potential, the sign partition, the attractor) and plain GKK; self-test rows: tc_1..9 =
      4, 19, 52, 139, 388, 1123, 3316, 9883, 29572 iterations, counter_symsi_1..12 = 11, 28, 52, 94, 172, 322, 616, 1198, 2356, 4666,
      9280, 18502. Then two kills to look for: (i) long runs (climbs scored by jumps AND by the bit length of the potentials and the
      Dijkstra work; exhaustive small maxima; a designed tower); (ii) non-termination or a wrong region. Every finding with its
      instance file, sha1, counter and unit; winners against Oink zlk and `--tl`.
- Deliverable file names: docs/red/R248-*.md, tools experiments/red/r248/.

## 3. docs/GAPS.md rows I own (trunk 37009aba5)
- G-NEST (major, «L-RED (attacks + proof attempts); L-ALG successor if any», open; l. 9).
- L-RED attacks: GAP-A (blocker, open; l. 6), GAP-C (blocker, open; l. 7), G-STR (major, closed; l. 22), G-DOM (major, closed; l. 23).
- Today's candidates (RF, N13) have no GAPS row on trunk at 37009aba5 (`grep -n "N13\|G-RF"`: no hit); G-N5-TIME (major, owner L-NEW,
  open at l. 11) is the row the dead N5 work was under; trunk's docs/RESULTS.md still ends at R130 (no «### R131» heading).

## 4. Three owner rulings (verbatim; status from trunk docs/DECISIONS-INDEX.md at 37009aba5)
- D1 «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own,
  as wrong until it passes the gauntlet below.» (active, index l. 5; text at trunk docs/DECISIONS.md l. 7 and
  docs/decisions/D001-launch-brief.md l. 25).
- D27 (2026-11-14) «SO we have to look for a new algorithm no? Do we have any promising lead or can convert our learning into a new
  promising algorithm?» (active, index l. 62; text at docs/DECISIONS.md l. 583).
- D28 (2026-11-14) «I reset everything, you have until 11PM to use a full 100% usage» (active, index l. 63; text at docs/DECISIONS.md
  l. 586). Lead reading L61 (index l. 64, not the owner's words): «N5 is dead; no promising lead (estimate stated); today = land R131 +
  a design day (L-NEW, L-SI design; L-COMP battery; L-RED, L-RED-B adversaries; L-LOWER barrier), successors of existing lanes only,
  Fable 5.2 xhigh, D1's standard unchanged».

## 5. One trap that bit this lane, and the check
- Lead messages read late (successor 69; and this session: three messages of 15:19Z-15:47Z were first read at 19:05Z after the limit
  pause, while I worked on a target that had been withdrawn at 15:47Z). Check: ReadNotifications at every wait, before every push and
  after every resume, before any other work.
- Stale local branch at start (this session: one commit behind while `git status` said up to date). Check: fetch + ff-only, then
  HEAD == origin/claude/l-red == ls-remote before any commit (equal at f0ad3cca).
- A rebuilt family that matches a count at one n only (my first RC_n rebuild gave 8 at n = 2 and 13, not 16, at n = 3). Check: a
  rebuild is «reproduced» only on the whole reference row, and a difference is reported with its first step in the trace.
- Totals and SHAs typed before they were computed (successors 68-70). Check: totals pasted from script output in the same step, SHAs
  copied from git output, stamps from date -u. Never a commit while push.sh runs (pgrep before every commit); never pipe verify.sh or
  push.sh; no model names in commits.
