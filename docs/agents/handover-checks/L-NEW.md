# Handover check: L-NEW (successor 67, Opus; session started about 2026-11-08 22:37Z (first date -u read 22:38Z; an earlier «22:36Z» here was an estimate, corrected), written 2026-11-08T22:38Z by date -u)
Overwrites successor 66's answers (history in git). Each answer measured from the repository at writing (commands named).
Predecessor: successor 66, parked at l-new 3015f5dc (section «HANDOVER (successor 66, …)» at the top of notes/L-NEW.md).

### 1. Branch, head, ahead/behind trunk
- Trap check: `git fetch --unshallow origin; git fetch origin claude/l-new claude/vibrant-johnson-nxvvxo; git checkout claude/l-new;
  git merge --ff-only origin/claude/l-new` (local branch was 1027 commits behind: stale container, fast-forwarded) ->
  `git branch --show-current` = claude/l-new; `git rev-parse HEAD origin/claude/l-new` both 3015f5dc.
- Trunk origin/claude/vibrant-johnson-nxvvxo head aaf52291 («Lead: land RESULTS R122 (P-ACYC …)», 20:27Z).
  `git rev-list --left-right --count trunk...HEAD` = **13 ahead / 260 behind** (left = trunk only 260, right = mine 13);
  merge-base 219e3933. Not merged (the brief does not ask for a merge).

### 2. Open work and the next step of each
- DUTY (landing pipeline; first after «go» if routed): R121 P-N5-ASC and R122 (P-ACYC, L-SI's) LANDED. R123 P-N5-QUIET at CHECKER C137
  (L-4 0809da25, fixes entry 4 at 87603d07). R124 P-N5-END (L-3 d6afe92a) and R125 P-N5-CHAIN (L-4 a69c8aa9) queued; both referees MATCH.
  Next: any CHECKER item -> fixes entry N+1 (append-only) + next line by script from the latest generator (box194/mkl4_194.py,
  box195/mkl3_195.py, box196/mkl4_196.py; each asserts the previous line's sha1), repin; never edit a frozen packet. Nothing routed yet.
- PACKET P-N5-SPLIT (after duty): freeze docs/new/P-N5-SPLIT.md with sha1: box 199 SPLIT (i)-(iv) + TRANSFER, REWIN (a)(b), REWIN-HI (c),
  PAIR-SPLIT, SPLIT-COUNT (SPL <= 3M), RW-SHAPE/RW-SHAPE*, RW-1; box 198 PAIR-HIGH, RA-PATHS, C-EQUIV; box 197 RE-COUNT, RE-EQUIV,
  PAIR-COUNT/ALT-EQUIV (corrected); premises = P-N5-CHAIN facts by name (conditional on R125); C-WT, REWIN-ASC dropped; DEAD list with
  instances (CX4_n21, GROW7_n34, HOLD2K_n84, ROUTELOW_n21, Dilworth idea, RWX_n95); DATA with counters and pinned tools; TARGET scope
  paragraph (N5′-xi, Γ3, a REDUCTION/EQUIVALENCE, not G-N5-TIME); attack record (L-RED 61 R227, L-RED 62 R228). Next: send Lead path/commit/sha1.
- BOX 200 (D18): a TIME charge for Dhi_y(b) = 1 + Σ_(z above y) c_z(b) so the SPLIT-COUNT recursion does not multiply (each new high part
  at b paid by a distinct Howard step / strict value improvement on b's route; L-SI 48 generalises Lemma SUPERSET: not duplicated).
  Tests on RWX_n95, MW32_2, C6G8_n54, FW16_2, WC16_2 with a firing control. Not started (no long job before «go»).
- Nothing of mine running (`pgrep -af "push.sh|check.sh"` = none).

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
- Trap (this start, again): the container came up 1027 commits behind origin/claude/l-new; a commit there would fork history and the
  push would fail («invalid refspec» on a detached HEAD).
- Check: fetch --unshallow + fetch both branches, checkout + merge --ff-only, then `git branch --show-current` and
  `git rev-parse HEAD origin/claude/l-new` must agree before any edit (done: both 3015f5dc).
- Also kept (successor 66): random and climbed data missed RWX_n95 (~346,700 re-wins with 0 fails before L-RED's instance): a
  conjecture with large zero counts is still a conjecture; every lemma is tested on the frozen adversarial instances with a firing control.
