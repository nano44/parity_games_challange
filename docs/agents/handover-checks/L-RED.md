# Handover check: L-RED successor 71 (D1/D27/D28; LANE-RESTART step 3; written 2026-11-14T13:50Z by date -u)
Every answer is measured from the repository (commands named), not recalled. Predecessor: successor 70 (stopped by a usage limit at about
13:20Z on 2026-11-13, per the Lead's brief; its handover is notes/L-RED.md «HANDOVER (successor 70 -> 71)», l. 3633; its last commit is
c7ed9b8b). This session: session_01V5yGRVyq25BY6qxdGPF1dD. Brief: Lead, 2026-11-14 13:44Z («go» in advance).

## 1. Branch, head, distance to trunk
- Trap check run first: `git fetch origin claude/l-red; git merge --ff-only origin/claude/l-red` -> the local branch was at acd1a2fdb
  (successor 53's park), 208 commits behind, although `git status` said «up to date» before the fetch; fast-forwarded.
- `git rev-parse HEAD origin/claude/l-red` -> both c7ed9b8b6af43c4ae94a5fa15571193bc923eedc; `git ls-remote origin claude/l-red` -> the same.
- Trunk claude/vibrant-johnson-nxvvxo = aeb90ac199aff97b7189666965d7fd7d7119cf29 (committed 2026-11-13T19:04:18Z; ls-remote equal).
  `git rev-list --left-right --count origin/claude/vibrant-johnson-nxvvxo...HEAD` -> 1409 222, i.e. 222 ahead / 1409 behind;
  merge-base c2d1e88ee. Trunk is not merged in; truth docs are read with `git show origin/claude/vibrant-johnson-nxvvxo:<file>`.
- Lead session id in trunk docs/NOW.md l. 15: session_014FBi6o334DvwT5Uw2kDfoN (equal to the brief's).
- Other heads by ls-remote (13:46Z): claude/l-red-b 10dfedb6, claude/l-si 8c062914, claude/l-new 0c18fbba, claude/l-comp dc6d831f.
- Clock: `date -u` 13:46:23Z against the Date header of a raw.githubusercontent.com response 13:46:23 GMT: skew 0 s.

## 2. Open work and the next step of each
- Nothing running at start (`pgrep -af "push.sh|verify.sh|climb|python"`: none; 4 CPUs, 15 GB). Oink was not built in this container;
  `scripts/setup_oink.sh` run 13:47Z as a tracked background task: exit 0, «oink built at 8fbf0a7» (winner checks, verify smoke step).
- Successor 70's R244 (306d74f6) and R245 (706d1ecc, c7ed9b8b) are DONE and on origin. Its «FIRST for successor 71» items (re-read of
  R104 / R117 proofs against wires; attack on the proof of L(G_k) = 2^k − 2) are overtaken by the brief: packet P-N5-EXP (claude/l-red-b,
  frozen 350d84eb, line L-3 at 10dfedb6) is signed by both referees and is landing as RESULTS R131 (trunk aeb90ac1 has no such heading
  yet: `git show trunk:docs/RESULTS.md | grep -n "^### R13[01]"` -> R130 only).
- NEW TARGET (brief): question SCHEME-TIE against the scheme SPEC S1-S5 (FIX 1-4, from S3) for every S4a tie rule. Deliverable
  docs/red/R246-scheme-tie.md. Next steps, in order:
  (1) tie census of the N5 run on Γ3(G_k) (unit: «S4a ties met», per iteration, per k), on own engine n5s237 (SPEC-exact) with a second
      engine (L-NEW's n5v) before any count is reported as DATA; commit, tell the Lead (within about 60 minutes of «go»);
  (2) T1: can each tie be removed (ranks / priorities / a gadget per tie) while the root-first-key run stays exponential;
  (3) T2: compositions of G_k and the wrapper W against the hybrids h1 (alternate), h2 (run both, stop with the first), h3 (Ξσ-best, then
      root-first key); or (4) a counter showing tie-free runs are short. Labels PROVED / DATA / CONJECTURE; winners against Oink zlk / --tl.
- When a design lane names a candidate (commit from the Lead): switch to it (exhaustive small search, climbs, compositions of kill families).
- ON HOLD (older): DEEP3 climbs (bests frozen in experiments/red/r234/inst); 2-wide seeded lifts k 3 -> 4 (dropped by successor 70).

## 3. docs/GAPS.md rows I own (trunk aeb90ac1)
- G-NEST (major, «L-RED (attacks + proof attempts); L-ALG successor if any», open; l. 9).
- L-RED attacks: GAP-A (blocker, open; l. 6), GAP-C (blocker, open; l. 7), G-STR (major, closed; l. 22), G-DOM (major, closed; l. 23).
- Today's work is against G-N5-TIME (major, owner «L-NEW (L-LIT T22; referees later)», open at aeb90ac1; l. 11); the R131 landing that
  closes it negatively for N5 is the Lead's and not yet on trunk.

## 4. Three owner rulings (verbatim; status from trunk docs/DECISIONS-INDEX.md at aeb90ac1)
- D1 «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own,
  as wrong until it passes the gauntlet below.» (active, index l. 5; text at trunk docs/DECISIONS.md l. 7 and docs/decisions/D001-launch-brief.md l. 25)
- D27 (2026-11-14) «SO we have to look for a new algorithm no? Do we have any promising lead or can convert our learning into a new
  promising algorithm?» and D28 «I reset everything, you have until 11PM to use a full 100% usage»: quoted as the brief gives them;
  NOT yet in trunk's DECISIONS-INDEX.md or DECISIONS.md at aeb90ac1 (`grep -n "D27\|D28\|new algorithm\|I reset everything"`: no hit;
  the index ends at D26 / L60). Lead reading L61 (design day; not the owner's words) is likewise from the brief only.
- D18 «Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics
  and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and
  proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.» (still «active» in the
  index, l. 32; its N5 focus is overtaken by the kill and D27 once those are recorded; its labelling rule stands).

## 5. One trap that bit this lane, and the check
- Stale local branch at start (this session: 208 behind while `git status` said up to date). Check: fetch + ff-only, then
  HEAD == origin/claude/l-red == ls-remote before any work (equal at c7ed9b8b).
- An engine whose «spec» mode is not SPEC's tie rule (successor 67 / 68: n5x236 «spec» ≠ SPEC; N5 on F_n differs). Today's target IS the
  tie rule, so: every tie count comes from n5s237 (written from the SPEC text, state-by-state equal to n5v on 8,900 games) and is repeated
  on a second engine; a census counter gets a firing control (the wrapper family, where every option is tied) before it is trusted.
- Totals and SHAs typed before they were computed (successors 68-70). Check: totals pasted from script output in the same step, SHAs copied
  from git output, stamps from date -u. Never «&»; never a commit while push.sh runs (pgrep before every commit); no model names in commits.
- Lead messages read late (successor 69). Check: ReadNotifications at every wait and before every push.
