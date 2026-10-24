# Handover check: L-RED successor 14 (Opus 5.5, D15/L37; LANE-RESTART step 3; written 2026-10-24 ~14:35Z by date -u)
Every answer is measured from the repository at the time of writing (commands named), not recalled. Predecessor: successor 13
(session_01GhyuHegkNZEo8bet84n56c), last push f9f0e7c7 (box 30, R58 §13). The previous answers in this file (successors 4-13,
appended) are replaced; they remain in history (`git show b28a0af3:docs/agents/handover-checks/L-RED.md`).

## 1. Branch, head, distance to trunk
- Branch `claude/l-red`. Container at start: local = origin/claude/l-red = 0d0b67a1 (stale; clean tree).
- `git fetch origin claude/vibrant-johnson-nxvvxo claude/l-red` (14:3xZ): origin/claude/l-red 0d0b67a1 -> f9f0e7c7;
  trunk origin/claude/vibrant-johnson-nxvvxo = 70f5f10a ("Lead: CYC-ELIM data point; XING restated").
- `git merge --ff-only origin/claude/l-red` -> f9f0e7c7; then `git merge --no-edit origin/claude/vibrant-johnson-nxvvxo`
  (normal merge, no conflicts) -> 4bf07701. `git merge-base --is-ancestor f9f0e7c7 HEAD` true.
- `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` -> 15 ahead, 0 behind before this file's
  commit (14 box-30 commits of the predecessor plus the merge commit); 16 ahead after it. `git merge-base` = 70f5f10a.

## 2. Open work and the next step of each
No process running in this container (`ps aux | grep -c python3` = the grep itself plus harness). Predecessor's notebook
notes/L-RED.md was last changed at 1578a1a0 (08:25Z, "PARKED, wake only on a new named target"); at my 14:33Z fetch it does not
yet cover box 30. Box 30 is recorded in docs/red/R58-n5-width.md §13 (f9f0e7c7). I re-fetch before the GO and fold the
predecessor's handover in when it lands.
- (A) Box 30 cont., Lead brief (context only, not started): port Mei's mixed-cycle family Ĝ_h (arXiv 2610.27386, Thm 4 p.20)
  to a parity game and run N5. Spec docs/lit/T31-mei-port.md (L-LIT) is NOT on trunk 70f5f10a yet (`ls docs/lit/T31*` empty).
  Next step after GO: read T31 and open the arXiv source myself; then the checklist: (1) Oink zlk + verify.py on the port;
  (2) Dantzig-SSI control, expect 2^h − 1 iterations; (3) N5 from both starts; (4) if N5 is short, redesign so N5's gate is a
  singleton.
- (B) R58 §13a: (ELIM-n) REFUTED (elimn_cex_n48.pg, sha1 d6062e86…, re-measured with sha1sum). Weaker (ELIM-cn)/(ELIM-poly)
  OPEN; window 49 at n 48 is linear. Next: only if the Lead routes it, climb for windows ≥ 2n.
- (C) R58 §13b-c: L-NEW box 26 lemmas RM and RE: 0 violations on 12 named instances and climbs; θ-changes per phase stuck at
  16 (n 24-64). Next: attack each new L-NEW lemma as it lands (L40 (2b)); target super-polynomial θ-changes in one joint
  λ-phase.
- (D) CHECKER questions on R56 §4 / DE30, if any (notebook NEEDS).

## 3. docs/GAPS.md rows I own
- G-NEST (major, owner "L-RED (attacks + proof attempts); L-ALG successor if any"), status **open** (docs/GAPS.md line 9).
  Paused with the DTL line by L40 (1).
- Rows L-RED attacks but does not own: GAP-A, GAP-C (L-ALG, open; DTL paused); G-N5-TIME (L-NEW, open) is the target my N5
  work attacks.

## 4. The three owner rulings that most constrain me (verbatim), with their DECISIONS-INDEX status
1. D18 (docs/DECISIONS.md line 333), index status **active**:
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics
   > and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and
   > proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
   (Lead reading L40, active: L-RED is the N5 adversary; labels PROVED / CONJECTURE / OPEN; DTL attack paused.)
2. D15 (docs/DECISIONS.md line 278), index status **active**:
   > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
   (Lead reading L37, active: Opus 5.5 lanes; the Lead decides allocation; reports are information.)
3. D1 launch brief, gauntlet (docs/decisions/D001-launch-brief.md lines 92-93), index status **active**:
   > Failing any step makes it a dead end, recorded with the exact obstruction or counterexample.
   and (line 99): "> - Dead ends are kept, with the obstruction and the instance that killed them."

## 5. One trap that bit this lane, and the check that now prevents it
- Trap (box 29, R58 §12e): my own classifier retcheck.py had a class ("θ at re-entry ▷ w at the leave") that cannot occur while
  w is constant (θ ⊴ w, Lemma S); the fall-through class absorbed everything, so R58 §12d (ii) reported "20 / 20 re-entries by
  route improvement", which was WRONG (THETA re-entries are common: rt48 21/21, ph64 30/23).
- Check: before any classifier result is stated, run it on a pinned instance where every class is known to occur, and use the
  other lane's classifier unmodified when attacking its lemma. Done now: `python3 experiments/new/box25/reentry.py
  experiments/new/box25/thetare_min.pg` -> {ROUTE: 1, THETA: 1, THETA_partial: 1, ...}: both classes reachable. Box 30 already
  followed it (elim.py, thetaelim.py, routemono.py, reentry.py all unmodified). Standing checks too: every instance passes Oink
  zlk + verify.py, and N5 counts agree between n5.py and L-COMP's n5b.py.
