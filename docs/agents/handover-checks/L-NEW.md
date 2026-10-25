# Handover check: L-NEW (successor 18, Opus 5.5 per owner D15 / Lead reading L37; written 2026-10-25 14:1xZ by date -u)
This file replaces the previous answers (successor 14 here; successors 15-17 wrote theirs into notes/L-NEW.md; all in git history).
Each answer was measured from the repository when written (commands named), not recalled. Predecessor: successor 17,
session_01ESR6bpU1r4ZjFsMExZtFpq, parked at l-new dd3f780b (box 38 end + P-N5-OUT fixes file). Clock: `date -u` read 14:17:56Z.

### 1. Branch, head, ahead/behind trunk
- Branch claude/l-new. STALE container again: local HEAD 5961101a (successor 6), "behind 'origin/claude/l-new' by 1496 commits".
  `git fetch origin claude/l-new` (5961101a..dd3f780b); `git reset --hard origin/claude/l-new` (brief step 1; working tree clean) →
  HEAD dd3f780b.
- Trunk = origin/claude/vibrant-johnson-nxvvxo (docs/NOW.md l.15). After `git fetch origin claude/vibrant-johnson-nxvvxo`:
  `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` = **1 ahead / 167 behind** trunk e6899305 ("Lead:
  hourly sweep 14:04Z; merge checker (C45/C46 closed)"); merge-base 1500bdbd (trunk has merged up to successor 17's handover, not
  the fixes-file commit dd3f780b).
- `git merge --no-ff origin/claude/vibrant-johnson-nxvvxo` (no conflicts, no rebase) → merge commit 22fc9ccb: 2 ahead / 0 behind;
  after this file's commit 3 ahead / 0 behind until the Lead's next trunk commit.

### 2. Open work and the next step of each
Nothing of mine is running (`ps aux | grep python`: none). Oink is NOT built here (`ls tools/oink/build`: no such directory): the
first research step after GO is `scripts/setup_oink.sh`.
- **P-N5-OUT** (docs/new/P-N5-OUT-box37.md, `sha1sum` 9f032e61…, pinned trunk 719ce66): REFEREE succ. 8 signed all (R-N5-OUT
  fa08687; notes OUT-R1, OUT-N1); REFEREE-2 succ. 9 signed all (R2-N5-OUT dfcaae67, merged trunk da5bac3a; notes N-OUT-1..4).
  Fixes file docs/new/P-N5-OUT-fixes-box37.md exists (dd3f780b, `sha1sum` 640a5db2…), not yet on trunk; once its sha1 is reported it
  is frozen. Next: any item from the referees' §Cs goes in a NEW docs/new/P-N5-OUT-fixes2-box37.md (does not exist).
- **P-N5-NEB** (docs/new/P-N5-NEB-box38.md, `sha1sum` ba15e51f…, commit 8ca35711): not yet pinned; GAPS row 11 lists it "queued".
  Next: when relayed, referee items go in a NEW docs/new/P-N5-NEB-fixes-box38.md, including the three known items from the resume
  point: CONJECTURE BAND (rises form) FALSE on tauw_A_cex_n24; OUT-R1's remark (Step (K) at a only) applies to NEB §3/§4; NEB §0
  table status of P-N5-OUT is now "signed by both", not "IN REVIEW".
- **P-N5-SCOPE**: fixes file P-N5-SCOPE-fixes-box36.md (sha1 e2550755…) cited, frozen; landing as R36 per the resume point
  — but `grep "^### R3" docs/RESULTS.md`: R36 = P-N5-P1, R37 = P-N5-RL; P-N5-SCOPE has NOT landed yet (not in RESULTS), so the resume point's "R36" is stale.
- **Research (D18) after GO**, in the resume point's order: (1) RW_S, R̄-rises after c_w ≠ o evictions at any level (BAND is false);
  route improvements in R with θ fixed. (2) θ_ph / θ_S, the residual core (PF-THETA polynomial form; the linear form is FALSE,
  pftheta_cex_n32). (3) HN stretches per phase for τ(o) ≠ o. (4) OTHER states. Tools in experiments/new/box37 and box38.
- Not routed: G-N1-LB; OB_R, OB (CONJECTURES).

### 3. docs/GAPS.md rows I own (`git show origin/claude/vibrant-johnson-nxvvxo:docs/GAPS.md | grep -n L-NEW`)
- **G-N5-TIME** (l.11): major; owner "L-NEW (L-LIT T22; referees later)"; status **open**. Latest update 14:01Z: R37 LANDED
  (P-N5-RL + fixes; CHECKER C46). "Open: NJB = ENT, REL(S), the level −1 and out-of-scope fallbacks. In review: P-N5-OUT, P-N5-ENT;
  queued: P-N5-NEB, P-N5-LV." (13:52Z: R36 = P-N5-P1, discharges (P) for one-player games only.)
- **G-N1-LB** (l.10): minor; owner "L-NEW (optional; not routed)"; status **open**.
- **G-N5-TERM** (l.16): major; owner "L-NEW (L-COMP checks runs)"; status **closed** (RESULTS R15).

### 4. The three owner rulings that most constrain me (verbatim, docs/DECISIONS.md on trunk), with their index status
1. D18 (l.332-333; DECISIONS-INDEX l.32 **active**; Lead reading L40, L-NEW = designer):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
2. D14 (l.244-246; DECISIONS-INDEX l.22 **active**; Lead reading L35):
   > D
   > You know it can also test prveiously not tested approaches, it can come up with it own as well
3. D16 (l.299-300; DECISIONS-INDEX l.28 **active**; Lead reading L38):
   > Then keep working as I told you to

### 5. One trap, and the check that prevents it
- **Trap**: the stale container, now worse than ever: local claude/l-new at 5961101a (box 17), 1496 commits behind origin. Without a
  fetch, `git status` reports "up to date" and boxes 18-38, every packet, fixes file and instance would be invisible.
- **Check**: `git fetch origin claude/l-new` and `git rev-parse HEAD origin/claude/l-new` equal before any work; packets checked by
  `sha1sum` against the notebook / NOW; fetch and merge (never rebase) before every push (a parked predecessor has pushed during a
  handover before: a670161b).
- **Also carried**: frozen packets and cited fixes files get new text only in a new file; stamps only from date -u (container clock
  has run slow vs the Lead's stamps); push.sh output to a file, then `$?`; ReadNotifications after every push (successor 17 missed
  three Lead messages); `pkill -f` inside a compound command kills the shell itself (run it alone, or kill by pid); in box-37 tools,
  skip non-𝒞^1O library files; experiments/new/out/ is gitignored, experiments/new/boxNN/out/ is not.
