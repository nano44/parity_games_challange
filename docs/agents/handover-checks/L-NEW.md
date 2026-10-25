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

## Successor 20 (session_018pjn8Y8JRES3YuFDUCAJgM), written 2026-10-25 18:01Z (date -u)
Predecessor: successor 19, session_011reTXakSJCcwLhC4i9ZpkB, parked at l-new 688c2d41 (handover). Trunk fetched again at 17:58Z,
right before writing (lesson of successor 18).

### 1. Branch, head, ahead/behind trunk
- Branch claude/l-new. Container stale at 5961101a: `git fetch origin claude/l-new` (5961101a..688c2d41), `git checkout -B
  claude/l-new origin/claude/l-new` → `git rev-parse HEAD origin/claude/l-new` both 688c2d41.
- Trunk origin/claude/vibrant-johnson-nxvvxo (NOW l.15) head 19d707b4 ("Lead: merge referee (RHO, PFZ-ext §C, LV2 §C); log",
  17:52:51Z). Before merging: `git rev-list --left-right --count HEAD...trunk` = **2 ahead / 151 behind**, merge-base ae05d83b
  (trunk merged l-new up to the FB-CAP route commit, not the handover commit 688c2d41).
- `git merge --no-ff` trunk (no conflicts, no rebase) → 9a86833d: 3 ahead / 0 behind; 4 ahead after this commit.

### 2. Open work and the next step of each
Nothing running (`ps aux`: no python / oink of mine). Oink NOT built (`tools/oink/build` absent): `scripts/setup_oink.sh` first.
- **P-N5-PFZ + ext** (sha1 3c617e06… / b3702b1b…, re-measured on trunk). In: REFEREE R-N5-PFZ 8595343 (main §C 4859e63, §C-ext
  ed8bc207 on trunk 19d707b4: PFZ-1 = G-PFX-1, repair proves (i)); REFEREE-2 R2-N5-PFZ 37e55fde (main, N-PFZ-1..3) + §X 78896bfc
  (G-PFX-1; signs (i′)). **Missing: REFEREE-2's §C on PFZ (vs R-N5-PFZ)**; origin/claude/referee-2 head 5f6d5405 (17:23Z) has none.
  Next: when the Lead relays it, write NEW docs/new/P-N5-PFZ-fixes-box39.md (does not exist; checked): repairs only, PFZ-1 repair in
  full (ℓ(θ) = |P(θ)| + |Q ∩ A_low| inside a P-epoch; θ_S ≤ ρ + (ρ+1)(|U|−3) ≤ (ρ+1)(|U|−2)), PFZ-N1..N3, N-PFZ-1..3, G-PFX-1.
- **P-N5-RHO** (sha1 cd5df65c…, pinned c8144551): REFEREE R-N5-RHO 59278313 ALL SIGNED (HN-POLY conditional as labelled; notes
  RHO-N1..N3). REFEREE-2 10 RHO not yet on origin/claude/referee-2 ("RHO next"). Next: NEW RHO fixes file after both reports + §Cs.
- **P-N5-NHN** (sha1 da7d09ec…, pinned 0bb175d): no report yet; referees after RHO. Next: NEW fixes file when relayed.
- **Research (D18) after GO**, the Lead's order (17:48Z): (1) FB-CAP proof (docs/new/N5-FBCAP-route-box40.md): route switches inside
  R̄ (κ-freeze on θ-runs, P-FREEZE with κ, F-FLAT analogue at Q fallbacks), Even vertices outside U, ¬H1 states, the c_θ-cycle
  exception via CN-LAST (R38 (f)); first read L-RED's FB-CAP data (l-red 1b00610, experiments/red/frz/; L-RED head now 847795fe).
  (2) Q-EPOCH and breaks in Q-runs (docs/new/N5-Q-box40.md §3-§4). (3) global f ↔ X loop (SCOPE-COUNT R38 (c), X-SN-PHASE R34 (f)).
- Not routed: G-N1-LB.

### 3. docs/GAPS.md rows I own (`git show trunk:docs/GAPS.md | grep -n L-NEW`)
- **G-N5-TIME** (l.11): major; "L-NEW (L-LIT T22; referees later)"; **open**. Latest update 17:41Z: R42 LANDED (P-N5-NEB); R41
  (P-N5-LV) 17:35Z. "Open: RW_S, θ_ph / ρ (lane P-N5-PFZ / RHO / NHN in review), Q states, scope runs per phase / X, S4a steps,
  phases." CONJECTURES (DATA): FB-CAP (L-RED), INTO (L-SI).
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
- **Trap**: `pkill -f <pattern>` inside a compound command matches the calling shell itself and kills it (exit 144); it bit
  successors 18 and 19 (19: after push.sh had finished, so the push state had to be re-checked).
- **Check**: kill by pid only, from a separate command: `pgrep -f` / `ps aux`, confirm each pid with `ps -p <pid>` is the python
  process, then `kill <pid>`; after any exit 144 re-run `git status` / `git log -1 origin/claude/l-new` before assuming anything.
  Also carried: stale container (fetch + rev-parse equality); fetch trunk right before any status text; push.sh output to a file,
  then `$?`; packets and cited fixes files frozen once sha1 reported (new text → new file); grep trunk docs for every new lemma
  name. New this session: `rev` on a 15 kB GAPS line hung at 99% CPU (killed by pid); slice long lines with python instead.

## Successor 21 (this session), written 2026-10-25 19:36Z (date -u)
Predecessor: successor 20, session_018pjn8Y8JRES3YuFDUCAJgM, parked at l-new a3efded7 (handover). Trunk fetched at 19:35Z, right
before writing.

### 1. Branch, head, ahead/behind trunk
- Branch claude/l-new. Container stale at 5961101a: `git fetch origin claude/l-new` (5961101a..a3efded7), `git checkout -B
  claude/l-new origin/claude/l-new` → `git rev-parse HEAD origin/claude/l-new` both a3efded7.
- Trunk origin/claude/vibrant-johnson-nxvvxo (NOW l.15) head 6d78b8f4 ("Lead: R45 draft (P-N5-RHO), held until R44 (PFZ); log",
  19:30:12Z). Before merging: `git rev-list --left-right --count HEAD...trunk` = **3 ahead / 10 behind**, merge-base b67831cd
  (trunk merged l-new up to the PFZ fixes draft, 2f4cad19; not cf20cdc2 (PFZ fixes file) nor a3efded7 (handover)).
- `git merge --no-ff` trunk (no conflicts, no rebase) → 27d35bc0: 4 ahead / 0 behind; 5 ahead after this commit.

### 2. Open work and the next step of each
Nothing running of mine. Oink NOT built (`tools/oink/build` absent): `scripts/setup_oink.sh` before any run.
- **P-N5-PFZ + ext**: both referees' reports and both §Cs are in (REFEREE-2 11 §C 212f88ec: identical, G-PFX-1 = PFZ-1, BRK-POLY′
  (i)-(iii) SIGNED with REFEREE's repair). Fixes file docs/new/P-N5-PFZ-fixes-box39.md (cf20cdc2, sha1 3f55bc88…) frozen. Lead
  drafts R44. Next for me: none unless CHECKER/Lead returns a defect (then a NEW file).
- **P-N5-RHO**: fixes file docs/new/P-N5-RHO-fixes-box40.md (cf02711c, sha1 cc4e8540…) frozen, merged on trunk; R45 draft held
  until R44 (trunk 6d78b8f4). Next: none unless returned.
- **P-N5-NHN** (pinned 0bb175d): no report on origin/claude/referee (head 008ad8ab = NEEDB) nor referee-2 (head fa71c133 = FBPOLY
  batch). Next: NEW fixes file when relayed; must carry NHN-N1 = RHO-N2 (τ(o) = o line cites R34 (e) with HN = H1).
- **P-N5-FBPOLY** (sha1 de244dcd…, pinned 42d8c3a9): REFEREE-2 11 batch in (fa71c133: 1,484 logs, 0 violations), report follows;
  REFEREE not yet. Next: NEW fixes file after both reports.
- **Research (D18) after GO**, Lead's order 19:01Z: (1) packet P-N5-NH (docs/new/P-N5-NH-box41.md, new): signable lemmas with proofs
  for the (NH′) reductions R22 / R24 / R26, marking (X) as covered via FX / FB-POLY + R30 (c) + R34 (e),(f), NFB-O via FB-POLY;
  sources P-N5-NH-box30.md + fixes, N5-NH-box28.md, N5-NH2-box29.md. (2) K (wakes per phase, R27 (XJ)) ≡ (E), (K_W) (R26): does the
  κ-freeze / FB-POLY structure bound K? Else the exact obstruction + instance (cf. K-chain, box33 kchain32.pg). Also open: FB-CAP for
  |U| ≥ 3 (lane conjecture; FB-POLY gives a poly bound regardless), κ-FREEZE-F.
- Not routed: G-N1-LB.

### 3. docs/GAPS.md rows I own (trunk 6d78b8f4, `grep -n L-NEW docs/GAPS.md`)
- **G-N5-TIME** (l.11): major; "L-NEW (L-LIT T22; referees later)"; **open**. Latest update 17:41Z (R42 landed); "Open: RW_S, θ_ph /
  ρ (lane P-N5-PFZ / RHO / NHN in review), Q states, scope runs per phase / X, S4a steps, phases." CONJECTURES (DATA): FB-CAP, INTO.
- **G-N1-LB** (l.10): minor; "L-NEW (optional; not routed)"; **open**.
- **G-N5-TERM** (l.16): major; "L-NEW (L-COMP checks runs)"; **closed** (RESULTS R15).

### 4. Three owner rulings that most constrain me (verbatim, trunk docs/DECISIONS.md), with DECISIONS-INDEX status
1. D18 (DECISIONS l.332-333; INDEX l.32 **active**; Lead reading L40, INDEX l.33 active):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
2. D14 (l.244-246; INDEX l.22 **active**; Lead reading L35, l.23 active):
   > D
   > You know it can also test prveiously not tested approaches, it can come up with it own as well
3. D16 (l.299-300; INDEX l.28 **active**; Lead reading L38, l.29 active):
   > Then keep working as I told you to

### 5. One trap, and the check that prevents it
- **Trap** (successor 20): push.sh started before `git commit`; verify ran on the uncommitted tree while the commit landed between
  verify and push, so what was verified was not exactly what was pushed.
- **Check**: `git status --porcelain` empty and `git log -1` = the intended commit BEFORE `scripts/push.sh > file 2>&1; echo $?`;
  after the push, `git rev-parse HEAD origin/claude/l-new` equal. Carried: stale container (fetch + rev-parse equality); fetch
  trunk right before status text; kill only by pid (pkill -f kills its own shell, exit 144); slice long GAPS lines with python
  (`rev` hung); $TMPDIR is empty (use the scratchpad); frozen packets / fixes files (new text → new file); grep RESULTS for the
  counted quantity before proving a new bound (X was already poly by R30 (c) + R34 (f)).

## Successor 22 (session per NOW roster, to be added by the Lead), written 2026-10-25 21:47Z (date -u)
Predecessor: successor 21, session_01YJHHx1t8hvqkDnKzMU2Lfa, parked at l-new 6a1b0e95 (box 43 brief in the resume point). Trunk
fetched at 21:46Z, right before writing.

### 1. Branch, head, ahead/behind trunk
- Branch claude/l-new. Container stale at 5961101a: `git fetch origin claude/l-new` (5961101a..6a1b0e95), `git checkout -B
  claude/l-new origin/claude/l-new` → `git rev-parse HEAD origin/claude/l-new` both 6a1b0e95.
- Trunk origin/claude/vibrant-johnson-nxvvxo head c4d18621 ("Lead: LAND RESULTS R47 (P-N5-PHI, checker 5bb11d61); GAPS update;
  NOW; log", 21:39:10Z). Before merging: `git rev-list --left-right --count HEAD...trunk` = **2 ahead / 55 behind**, merge-base
  669624b2 (my two unmerged commits: d9e3754b and 6a1b0e95, both notebook-only).
- `git merge --no-ff` trunk (no conflicts, no rebase) → a1c4370a: 3 ahead / 0 behind; 4 ahead after this commit.

### 2. Open work and the next step of each
Nothing running of mine. Oink NOT built (`tools/oink/build` absent): `scripts/setup_oink.sh` before any run.
- **Box 43 (Lead 21:22Z): N5 beyond 𝒞^1O**, not started; waits for "go". File docs/new/N5-MULTI-box43.md. Steps: (1) ledger of
  R17-R47 + FBPOLY, FX, KW, NH42: which hypothesis uses "o is the only Odd choice vertex"; verbatim / per-Odd-vertex index / fails;
  (2) first obstruction on 𝒞^2O (exhaustive small n, then climbs; seeds counter_*; lens = N5 phases), instance to the Lead at once;
  (3) one novel route (Lead's candidate: τ-change of each Odd choice vertex as a phase boundary of a product of 𝒞^1O runs).
- **P-N5-FBPOLY**: REFEREE-2 12's §C FBPOLY not on origin/claude/referee-2 (head 84d8c8c9, 20:30Z, handover notes).
  Next: when it lands, append a section to docs/new/P-N5-FBPOLY-fixes-box41.md (frozen above) or a new file, only if it adds anything.
- **P-N5-NH-box42** (pinned trunk 54ac72e6): REFEREE signed (a47f8540 per NOW); REFEREE-2 12 pending. Next: NEW fixes file
  docs/new/P-N5-NH-fixes-box43.md when both reports and §Cs are in.
- **P-N5-KW**: written by L-SI 10 (Lead 21:22Z); my N5-KW-box42 v3.2 stays the independent second-lane proof, not packeted. Next: none
  unless asked.
- Not routed: G-N1-LB.

### 3. docs/GAPS.md rows I own (trunk c4d18621, `grep -n L-NEW docs/GAPS.md`)
- **G-N5-TIME** (l.11): major; "L-NEW (L-LIT T22; referees later)"; **open**. Update 21:39Z: R47 landed (Lemma Φ every game,
  Corollary Φ-1O); "phases" closed on 𝒞^1O; open on 𝒞^1O: fallbacks per phase (FBPOLY), crossings (FX), T per phase given f (P-N5-KW,
  L-SI). "Beyond 𝒞^1O: OPEN (L-NEW box 43)."
- **G-N1-LB** (l.10): minor; "L-NEW (optional; not routed)"; **open**.
- **G-N5-TERM** (l.16): major; "L-NEW (L-COMP checks runs)"; **closed** (RESULTS R15).

### 4. Three owner rulings that most constrain me (verbatim, trunk docs/DECISIONS.md), with DECISIONS-INDEX status
1. D18 (DECISIONS l.332-333; INDEX l.32 **active**; Lead reading L40, INDEX l.33 active):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
2. D14 (l.244-246; INDEX l.22 **active**; Lead reading L35, l.23 active):
   > D
   > You know it can also test prveiously not tested approaches, it can come up with it own as well
3. D16 (l.299-300; INDEX l.28 **active**; Lead reading L38, l.29 active):
   > Then keep working as I told you to

### 5. One trap, and the check that prevents it
- **Trap** (successor 21, found by me at restart): the handover commit 6a1b0e95 inserted the new resume point by re-pasting the
  notebook, so lines 16-271 appeared twice (byte-identical at 304-559) followed by the SUPERSEDED resume point (NEXT = "wait for the
  K decision"). A successor reading the second "Resume point" heading would take the stale NEXT. Fixed in this commit: duplicate
  block and stale resume point removed (python check: the two slices equal before deletion); one "Resume point" heading remains.
- **Check**: after any notebook overwrite, `grep -c '^## Resume point' notes/L-NEW.md` = 1 and `git diff --stat` line counts
  match the intent. Carried: stale container (fetch + rev-parse equality); `git status --porcelain` empty before
  `scripts/push.sh > file 2>&1; echo $?`; `git rev-parse HEAD origin/claude/l-new` equal after; read notifications whenever the
  notice appears; scratchpad, not $TMPDIR; kill by pid only.
