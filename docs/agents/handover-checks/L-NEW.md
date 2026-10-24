# Handover check: L-NEW (successor 10, Opus 5.5 per owner D15 / Lead reading L37; written 2026-10-24 15:53Z by date -u)
This file replaces the previous answers (Lead brief 15:52Z). Successors 1-9's answers are in git history before this commit. Each
answer was measured from the repository when written (the commands are named), not recalled. Predecessor: successor 9,
session_01EnPXboLL7nw4CKpAwqSDkm, parked after box 27 (notes/L-NEW.md resume point 15:40Z, af823a23).

### 1. Branch, head, ahead/behind trunk
- Branch claude/l-new. I ran `git fetch origin claude/l-new claude/vibrant-johnson-nxvvxo`. The container was STALE: local was
  5961101a and origin/claude/l-new was af823a23.
- `git rev-list --left-right --count origin/claude/l-new...origin/claude/vibrant-johnson-nxvvxo` gave 0 ahead, 11 behind trunk
  36297e16. Trunk already contains af823a23 (Lead merge "Merge claude/l-new (af823a2)").
- So `git merge` of trunk was a fast-forward, with no merge commit, and HEAD = 36297e16.
- `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` gives 0 / 0. `git merge-base --is-ancestor`
  holds for both af823a23 and 36297e16.
- After this file's commit the branch is 1 ahead (this commit) and 0 behind.

### 2. Open work and the next step of each
Nothing of mine is running. tools/oink/build and experiments/new/out/ are absent from this container. Run scripts/setup_oink.sh
before any Oink-verified run.
- **Box 28** (after GO only). The Lead's brief, given "for context": first (NH), then (CYC'). Its base is the box-27 reduction
  (docs/new/N5-xing-box27.md §4, §6, §8; READING, assumes (h)): N5 on o-cyclic 𝒞^1O is polynomial if both of these are poly(n)
  per joint λ-phase:
  - θ- and w-changes per phase (CYC');
  - non-(h) transitions per phase (NH).
  The throttled stretches are covered by C / FBL / FBF / XA / CR / PIECE, and the unthrottled runs by UT.
  - (NH), next step: count the non-(h) transitions per joint λ-phase with experiments/new/box25/phaseprofile.py.
    - Inputs: the pinned long-phase instances (fts_best16, tp32, rt48, ph64, sc32, elim24_p52), then random climbs.
    - Notebook data: all of these give 0 inside long phases. So (NH) may be a boundary effect at phase starts.
    - Known fallbacks off (h): box-25 W-drops (wdrop_cyc.pg n 4, sha1 d2684b7b…; wd16_s2), where τ(o) closes a cycle at o.
    - Then: try to prove that a non-(h) state can occur only at a phase start or a τ-change, or reduce such states to (h).
    - Label the outcome PROVED / CONJECTURE / OPEN (L40).
  - (CYC'), next step: the designer's angle on θ-changes against a fixed w (box 27 §8b, the u*-levels; §8c, a recursion below u*
    after the coarse freeze).
    - Seed: sc32 (experiments/new/box25/instances/sc32.pg, sha1 c3859ab5…). It has 43 θ-changes in one phase and no w-change.
    - Lemma UD: u* descends only when θ changes AT u*.
    - Use L-SI's Lemma VIS (docs/si/N5-OR-lens-box2.md): visible INR events are ≤ d per run.
    - Any bound I believe goes to the Lead at once, labelled READING (D1).
- **P-N5-XA** (docs/new/P-N5-XA-box27.md, pinned at trunk b70aa59, sha1 832d0da2…, re-measured, `git diff b70aa59 HEAD` on it is
  empty). REFEREE and REFEREE-2 successors 4 are reviewing it. Next step: answer their gaps in a NEW dated file, never in the
  packet.
- **P-N5-RE / R19** (docs/new/P-N5-RE-box26.md, pinned 52c7261, sha1 8dba4576…, empty diff). Both referees have signed. The Lead
  is landing it as R19 (docs/agents/R19-draft.md, CHECKER C28 Addendum 1 pending). Nothing for me unless C28 asks. The repairs are in
  N5-xing-box27.md §9.
- Others, relayed through the Lead: L-RED 14 is on (CYC') with sc32 as seed, and L-SI box 2 is on (CYC-u*).
- Not routed: (FO*), (BR*) ∧ (SEG-LEN*), (ALT), G-N1-LB.

### 3. docs/GAPS.md rows I own (`grep -n "L-NEW" docs/GAPS.md` at 36297e16)
- **G-N5-TIME**: major; owner "L-NEW (L-LIT T22; referees later)"; status **open**.
  - R18 is landed: o-acyclic 𝒞^1O, conditional on (P).
  - Still open: o-cyclic 𝒞^1O, which reduces to (CYC') + (NH) (READING); ≥ 2 Odd choice vertices; the general case.
- **G-N1-LB**: minor; owner "L-NEW (optional; not routed)"; status **open**.
- **G-N5-TERM**: major; owner "L-NEW (L-COMP checks runs)"; status **closed** (RESULTS R15).

### 4. The three owner rulings that most constrain me (verbatim), with their index status
1. D18 (docs/DECISIONS.md#d18, l.333; DECISIONS-INDEX row D18 "active"; Lead reading L40 "active", L-NEW = designer):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
2. D1 (docs/decisions/D001-launch-brief.md; DECISIONS-INDEX row D1 "active"):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   For me this means a bound I believe is a READING until it is refereed, and L-RED attacks it (designer and falsifier differ).
3. D15 (docs/DECISIONS.md#d15, l.278; DECISIONS-INDEX row D15 "active"; L37 "active"):
   > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
   This means no option questions to the owner. I decide inside the brief and report.

### 5. One trap, and the check that prevents it
- **Trap** (box 26, notebook "TRAPS THAT BIT ME"): I measured crossing counts on UNTHROTTLED stretches (θ = w). Those are already
  bounded (UT / Lemma PT + R17), and they inflated the (XING) data. Box 27 §0 corrected it: xc16 / xc24 / xcf20 / tr20_s4 have 0
  throttled crossings.
- **Check**: experiments/new/box25/crossings.py counts throttled stretches by default (`--all` must be given explicitly). For box
  28 I measure every (NH) / (CYC') quantity per joint λ-phase with phaseprofile.py, which reports throttled and non-(h) transitions
  separately. I also state which regime and class each count covers before I use it.
- **Also carried**:
  - Stale container: caught again here (5961101a vs af823a23). Check: fetch, then `git rev-parse` / is-ancestor first.
  - The pinned packets: check with an empty `git diff <pin> HEAD` before any push.
  - ReadNotifications at each milestone.
  - push.sh output goes to a file, then `$?`.
  - Header times come only from date -u.
