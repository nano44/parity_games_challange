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

# Handover check: L-NEW (successor 19, Opus 5.5 per D15 / L37; session started 2026-10-25 15:45:30Z by date -u)
New section; successor 18's answers above stay as history. Each answer measured from the repository at writing (commands named).
Predecessor: successor 18, session_01BhkSHzG2cPM2Rdbj5Y2NJV, parked at l-new 79c706da (handover). Clock: `date -u` 15:46:30Z.

### 1. Branch, head, ahead/behind trunk
- Branch claude/l-new. Container fresh this time at 5961101a (stale view): `git fetch origin claude/l-new` (5961101a..79c706da),
  `git checkout -B claude/l-new origin/claude/l-new` → `git rev-parse HEAD origin/claude/l-new` both 79c706da.
- Trunk origin/claude/vibrant-johnson-nxvvxo (NOW l.15) head 23544b8a ("Lead: R40 draft rev. (C49 E-1, N-1, N-2); log", 15:40:17Z).
  Before merging: `git rev-list --left-right --count HEAD...trunk` = **1 ahead / 74 behind**, merge-base 1b6239fb (trunk merged
  l-new up to the PFZ-ext commit, not the handover commit 79c706da).
- `git merge --no-ff` trunk (no conflicts, no rebase) → edcc2b17: 2 ahead / 0 behind; 3 ahead after this commit, until the Lead's next.

### 2. Open work and the next step of each
Nothing running (`ps aux | grep python`: none of mine). Oink NOT built (`tools/oink/build` absent): `scripts/setup_oink.sh` first
if a step needs it.
- **P-N5-PFZ** (docs/new/P-N5-PFZ-box39.md, sha1 3c617e06… re-measured) PINNED at trunk 283bcb67 (15:29Z); **P-N5-PFZ-ext**
  (docs/new/P-N5-PFZ-ext-box39.md, sha1 b3702b1b… re-measured) PINNED at trunk c61ecc4e (15:35Z), one review unit with PFZ.
  REFEREE 9 queue (NOW l.37): NEB → PFZ → LV → LV2. Next: referee items, when relayed, go in a NEW docs/new/P-N5-PFZ-fixes-box39.md.
- **P-N5-NEB** (sha1 ba15e51f…, pinned 314d220): REFEREE-2 signed (c547d6e; N-NEB-1..3); REFEREE 9 reviewing now (NOW l.37).
  Next: when relayed, write NEW docs/new/P-N5-NEB-fixes-box38.md (does not exist; checked) with BAND FALSE (tauw_A_cex_n24),
  OUT-R1 = N-NEB-1, N-NEB-2 (optional), N-NEB-3 (stale rows: R39 has landed, 15:09Z), and the §0 status rows.
- **P-N5-OUT**: LANDED as RESULTS R39 (C48 closed). Nothing open.
- **Research (D18) after GO**, resume-point order: (1) offer P-N5-RHO (docs/new/N5-RHO-box39.md §1-§4) as a frozen packet, asking
  the Lead first; (2) N_HN for τ(o) ≠ o: is N_HN ≤ H1-toggles (R34) + H2-changes (WCH, R38) + 1 polynomial? if yes HN-POLY for every
  τ(o); (3) climbs against FREEZE-F (c) / RHO-TAIL; (4) post-freeze regime of P-FREEZE beyond |U| = 1 in data (for the referees);
  (5) W-TIE (OPEN); (6) SN / OTHER states with the Bellman-Ford lens. Tools experiments/new/box39 (climb outputs were gitignored: lost).
- Not routed: G-N1-LB.

### 3. docs/GAPS.md rows I own (`git show trunk:docs/GAPS.md | grep -n L-NEW`)
- **G-N5-TIME** (l.11): major; "L-NEW (L-LIT T22; referees later)"; **open**. Latest update 15:09Z: R39 LANDED (P-N5-OUT). "Open:
  θ_ph, HN stretches for τ(o) ≠ o, OTHER states, NJB = ENT (P-N5-ENT converged, landing next), REL(S), level −1. Lane (unrefereed):
  P-FREEZE / BRK-POLY (L-NEW 18), STALE-GATE / LV-PL′ (L-SI 7)." (R40 = P-N5-ENT is a draft at CHECKER C49, not landed.)
- **G-N1-LB** (l.10): minor; "L-NEW (optional; not routed)"; **open**.
- **G-N5-TERM** (l.16): major; "L-NEW (L-COMP checks runs)"; **closed** (RESULTS R15).

### 4. Three owner rulings that most constrain me (verbatim, trunk docs/DECISIONS.md), with DECISIONS-INDEX status
1. D18 (DECISIONS l.332-333; INDEX l.32 **active**; Lead reading L40):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
2. D14 (l.244-246; INDEX l.22 **active**; Lead reading L35):
   > D
   > You know it can also test prveiously not tested approaches, it can come up with it own as well
3. D16 (l.299-300; INDEX l.28 **active**; Lead reading L38):
   > Then keep working as I told you to

### 5. One trap, and the check that prevents it
- **Trap**: a status answer written from a trunk view that is minutes old (successor 18 lost a point for it: the OUT fixes file and
  the NEB pin were on trunk already). Here the same: PFZ / PFZ-ext were pinned at 15:29Z / 15:35Z, after the predecessor's handover
  text ("pin pending"), and R39 had landed.
- **Check**: `git fetch origin claude/vibrant-johnson-nxvvxo` right before writing any status, then `git log --since` on trunk for
  Lead commits and sha1sum of each packet named. Also carried: stale container (fetch + rev-parse equality); `pkill -f` inside a
  compound command kills the shell (kill by pid from a separate command; re-grep edits after exit 144); grep trunk docs for every new
  lemma name before use (BF / FBF clashes); ReadNotifications after every push; push.sh output to a file, then `$?`.
