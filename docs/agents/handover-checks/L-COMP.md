# Handover check: L-COMP (successor 19, session_01V5yGRY8iNCAZqwL8HSCXM2; model and effort as the Lead set them under D21 / L51; written 2026-11-12T12:50Z by date -u)
Every answer measured from the repository at the time of writing. Successor of L-COMP 18 (handover «HANDOVER -- successor 18 (L-COMP 18,
Opus 5.5; session_01V5yGRVyip8PwDCTvydpDg1) PARKS 2026-11-12 ... after BOX 42. NOTHING RUNNING.», notes/L-COMP.md l. 4, park commit
57566151). This OVERWRITES successor 18's answers (in git history).

## 1. Branch, head, distance to trunk
- Container started on a stale local branch (cf2e0e4f, BOX 27; 1615 commits behind origin/claude/l-comp; `git status` said «up to
  date»). `git fetch --unshallow` + `git fetch origin claude/l-comp claude/vibrant-johnson-nxvvxo claude/l-si claude/l-red claude/l-new
  claude/l-lit` + `git checkout claude/l-comp` + `git merge --ff-only origin/claude/l-comp` -> fast-forward to 57566151.
- Branch `claude/l-comp` (`git branch --show-current`), HEAD = origin/claude/l-comp = 575661518ca5 (rev-parse; = `git ls-remote`).
- Trunk origin/claude/vibrant-johnson-nxvvxo = 471aba45214c («Lead: D21 (owner, confirmed directly: maximum effort, Fable 5.2 xhigh) +
  Lead reading L51 + backstop step 2; R127 second/third fill ...», commit date 11:31:38Z). `git rev-list --left-right --count
  HEAD...trunk` = 194 ahead / 455 behind; merge-base ebf59a34. +1 ahead after this commit.
- Other lanes at my fetch: l-new 8db300fe3fd8, l-si d8945c4a4e98, l-red ef026a615769, l-lit a19fff230e4c.
- Container: 4 cores, 15 GB RAM, fresh clone. No job of mine runs; `pgrep -f "bash scripts/push.sh"` empty. NOT in this clone (to be
  rebuilt / recreated before use, allowed before «go»): bin/ (box36/bin(+k), box37/bin, box38/bin) and the .git/info/exclude lines for
  them and out/.lock_*; tools/oink/build (verify's Oink smoke prints NOT RUN until scripts/setup_oink.sh has run); the second-engine
  worktrees / archive in the scratchpad (LSI100 = claude/l-si 23d39400, RED = claude/l-red 59daaef2, LNEW = git archive of l-new fcba92fc
  experiments/new experiments/si/si.py experiments/harness; cross100 runs with python3 -I).

## 2. Open work and the next step of each (all DATA; nothing runs; BOX 43 waits for «go»)
- BOXES 39-42: DONE (records = experiments/comp/box39..box42/README.md). Left open by 18's handover: (a) a fixed-family test on the DHIB
  line; (b) a family where ONE gate's deep flips grow. Both are BOX 43 items 2 and 3.
- BOX 43 item 1 (LEVEL cross-check; starts on the Lead's SHA): L-NEW 72's box 208 is on origin at my fetch (claude/l-new 8db300fe3fd8:
  docs/new/N5-LEVEL-box208.md, experiments/new/box208/level208.py, abs208.py, mut208.py, check208.sh, out/); NOT opened yet (I act on the
  SHA the Lead sends). Next step: read box 208's text; write its must-0 counters from the TEXT (a) on my IDEAL-CYC engine
  (box37/ideal37.py) over genomes (frozen sets of box39/inst, box40/inst + L-NEW's corpus), compare with L-NEW's frozen outputs, report
  mismatches exactly; (b) lifted to (plain parity game, Howard run) on Friedmann's G_N (lmcs(n) of claude/l-lit
  docs/lit/T66-depth-check.py, N <= 8; second engine T66-depth-xcheck.py's brute-force values) and PGSolver switchallexp. LEVEL must
  FAIL somewhere on G_N (else it contradicts [F11] Theorem 6.14, T = 9·2^N − 10 measured): report the first failing counter and step
  at the smallest N, and the genome property that step needs (expected candidate, to be tested not assumed: E-DOM / E-MON3, L-SI box
  102 Add. B).
- BOX 43 item 2 (fixed family on the DHIB line): seed box40/inst/DHIB26_2804.json (sha1 2c49fd10; N + M 400; Deep_3 24, dmax 6,
  whole-run deep 24, box41 README; L-SI box 102 §4: Deep^e_1 24, Deep^e_2 11, max 7 at gate (10, 0)). Next step: per-gate
  trace with box41/deep41.py (which gates / steps carry the deep flips, which in-edges feed them), growth rule as box42/clone42.py did
  for C6G8 (no search, equal effort per size), >= 4 sizes, two engines (mine deep41 on own34; L-SI cross100 on L-RED how3_232), fit
  within the family; dmax and per-gate max tracked with size.
- BOX 43 item 3 (if budget remains): a family whose ONE gate's deep flips grow (CL(k) only multiplies gates: per-gate max 3 at every
  size); instances coordinated with L-RED 66 through the Lead.
- Alert rule: anything faster than polynomial within one family -> Lead at once, frozen, two-engine numbers.

## 3. docs/GAPS.md rows owned by L-COMP
None (trunk 471aba45 docs/GAPS.md: open rows GAP-A, GAP-C, G-S5-6, G-NEST, G-N1-LB, G-N5-TIME; none has owner L-COMP). Mentions:
G-N5-TERM (l. 16, owner «L-NEW (L-COMP checks runs)», closed). BOX 43 is DATA for G-N5-TIME (l. 11, owner L-NEW, open), via CONJECTURE
DEEP3 / DEEP3-all (L-SI box 100 §5.2, box 102 Add. A; lane, unrefereed) and L-NEW 72's CANDIDATE Lemma LEVEL (box 208; lane).

## 4. Three owner rulings that most constrain this lane (verbatim; status from trunk docs/DECISIONS-INDEX.md)
1. D18 (active, DECISIONS-INDEX.md:32; text docs/DECISIONS.md:333): «Focus on N5 and work toward proving it. Explore novel approaches,
   especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable
   assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from
   conjectures and open problems.»
2. D1 (active, DECISIONS-INDEX.md:5; docs/decisions/D001-launch-brief.md:25-26, excerpt): «A claimed polynomial algorithm is far more
   likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.»
3. D21 (active, DECISIONS-INDEX.md:46; docs/DECISIONS.md:451-): «Okay, I want maximum effort. I want to use 200% usage in 3 days. There is
   fable 5.2 as well, use that too in dpeth everywhere where it seems fitting, use fable 5.2 at hard or xhigh. SO yes, 200% uage under 2
   days.» (direct confirmation: «I confrim tge stuff»). Lead reading L51 (active, :47), not the owner's words: maximum effort to
   2026-11-14 10:05Z; model and effort of successors per L51 (3); gauntlet, landing rules and no-contact unchanged.

## 5. One trap that bit this lane, and the check that now prevents it
Trap: stale container start (this start: cf2e0e4f, 1615 commits behind, while `git status` printed «up to date»), which makes pushes
fail with «invalid refspec» and would have had me read a BOX 27 notebook. Check: fetch --unshallow + fetch by branch name + ff-only +
`git branch --show-current` = claude/l-comp + HEAD == origin/claude/l-comp == ls-remote, before any read or edit (done above).
Carried from 17 / 18: `pgrep -f "bash scripts/push.sh"` empty before every commit and push (a commit was once made while a push ran,
88ac6b07); push.sh as a tracked background task with a 2-hour timeout, output redirected, exit code echoed, no pipes; SHAs quoted only
from git output in a later step; every number names its counter (unit, set, scope). New for BOX 43 item 1: a must-0 counter is trusted
only after its control fires (here: LEVEL's counters must fire on G_N; a lifted counter that stays 0 there is a broken lift, not a pass).
