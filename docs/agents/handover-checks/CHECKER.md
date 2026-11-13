# Handover check: CHECKER successor 25 (Opus 5.5, xhigh), written 2026-11-13T11:50Z (date -u)
Predecessor: successor 24 (HANDOVER 2026-11-13T10:08Z at the top of notes/CHECKER.md, pushed in 7d0c9ebe). This file is overwritten per
the brief; earlier successors' checks are in git history of this path. Every answer is measured from the repository (commands named).
Clock: `date -u` 11:47:12Z vs the Date header of a raw.githubusercontent.com response 11:47:13 GMT: skew at most 1 s.
Session: session_01V5yGRa7itsYzbsUzDCvnJn; get_session rate_limit_info: seven_day «allowed_warning», isUsingOverage false, resetsAt
1795035600 (2026-11-18 21:00Z); model claude-opus-5-5, effort xhigh.

### 1. Branch, head, ahead/behind trunk
- Trap check first (fetch --unshallow, fetch both branches, checkout, merge --ff-only): `git branch --show-current` = claude/checker,
  HEAD = origin/claude/checker = d7f07947 at 11:47Z. EARLY START: no commit until 7d0c9ebe was on origin (`git ls-remote origin
  claude/checker` = 7d0c9ebe at 11:50:29Z); then `git merge --ff-only origin/claude/checker` → HEAD = origin = 7d0c9ebe.
- Against trunk claude/vibrant-johnson-nxvvxo @ 5d7aab0f (`git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo`):
  2 ahead (d7f07947 C144 CLOSED, 7d0c9ebe successor 24's HANDOVER), 1286 behind (345 first-parent); merge-base 26e9d73c (C146 Add. 1,
  merged by the Lead in b943ada6 for R130).

### 2. Open work and the next step of each
- C146 = R130 (P-N5-WRAP): Add. 1 PASS 26e9d73c; R130 LANDED at a41e21c0 (merges 6bf3b44d l-si faf0c8ff, 4eebeffc referee 32d61d60,
  5055c7e9 referee-2 0f2606da, b943ada6 checker 26e9d73c). Add. 2 prepared in scratch, not committed (EARLY START): the four ancestors
  rc 0; parent b943ada6 RESULTS / GAPS = b28b7c81's = b94b0bac's (rc 0); rebuild from b94b0bac's draft (sha1 6858d52d…, block d[245:444]
  with «checker 26e9d73c)», UPDATE d[461] filled «2026-11-13», «10:06», «26e9d73c»): RESULTS eecbd798… and GAPS 3fa61e1c… byte-equal to
  a41e21c0's (True, True), negative control False; NOW counters R31-R130 (l. 2) and R17-R130 (l. 11) the only NOW change. NEXT: the CI
  line from run 43416851341 (#7719) on c6c9646f, the push that carried the landing (job verify, Gate in progress since 11:25:32Z at my
  read; L56: full self-checks; read the Gate log for «PASS     experiment self-checks»), then «C146 CLOSED» or the failing string.
- Lean rows #75-#78 (Fuel: Spec.fuel_eval / fuel_iter / fuel_run / fuel_states, claude/l-formal 8687c6fc + fa54df74 MANIFEST): report
  number C147 unless the Lead numbers it otherwise. Read so far (no verdict): build of record = run 43404819676 (#7708) on fa54df74, job
  lean-lemmas 131816478164 success, «Build completed successfully (3201 jobs).», axioms Classical.choice / Quot.sound / propext, «LEAN
  LEMMAS PASS»; 8687c6fc..fa54df74 changes only MANIFEST.md under lean/; verify.yml = trunk's. NEXT after «go»: my grep of the archive,
  the four Statements against the Lead's accepted text (08:42Z / 08:44Z, R1, R2) and the Spec.lean definitions they use (C143 / C145
  form, two readers). Then the NoFault Statement file and the KeyRule rows when the Lead routes L-FORMAL 5's SHAs.
- Standby: L-NEW 77 packet P-N5-KEY1P (1P(G), Lemma XI-1P, REDUCTION, A1-A4) or a kill packet, routed by the Lead with the two referee SHAs.

### 3. GAPS rows owned
None. `git show origin/claude/vibrant-johnson-nxvvxo:docs/GAPS.md | grep -n -i checker`: l. 6 (GAP-A, owner L-ALG), l. 11 (G-N5-TIME,
owner L-NEW), l. 16 (G-N5-TERM, owner L-NEW, closed); CHECKER appears there only as landing checker / re-runner, never as owner.

### 4. Three owner rulings, verbatim, with status (trunk docs/DECISIONS-INDEX.md)
- D1 (DECISIONS.md l. 7-8; index l. 5 «active»): «A claimed polynomial algorithm is far more likely to be wrong than right. Treat every
  such claim, including the fleet's own, as wrong until it passes the gauntlet below.» and «Never downgrade the referee to save money.»
- D18 (DECISIONS.md l. 333; index l. 32 «active»): «Focus on N5 and work toward proving it. Explore novel approaches, especially by
  connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions
  where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and
  open problems.»
- D25 (DECISIONS.md l. 541; index l. 57 «active»): «So put everything into trying solving it today». Lead reading L58 (index l. 58
  «active») (2): «Landing duty (R130) and Lean statements continue; side items wait.» (3): «Nothing in D25 relaxes D1».
  Also binding on my Lean rows: L54 (index l. 51 «active»): build of record = CI job lean-lemmas on the exact commit; on landings L56
  (index l. 53 «active»): CI always runs the full suite.

### 5. One trap and the check that prevents it
Successor 24's own slip (03:21Z and 07:3xZ): the push command began with a grep / pgrep before scripts/push.sh, so push.sh was not the
whole Bash command. Check: `pgrep -af "bash scripts/push.sh"` in its own call first; then the push call is push.sh alone (output
redirected to a file, then `echo exit $?`), run_in_background true, timeout 2 h; no commit while it runs. Second trap seen now: fresh
container without Oink (`ls tools/oink/build` failed); scripts/setup_oink.sh ran as a tracked task first (exit 0, «oink built at
8fbf0a7»), so verify's smoke step can run.
