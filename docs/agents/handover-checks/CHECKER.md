# Handover check: CHECKER (successor 4, Opus 5.5 per owner D15 / Lead reading L37; written 2026-10-24 15:22Z by date -u)
First file for this lane (none before). Every answer is measured from the repository at writing time (commands named), not recalled.
Predecessor: successor 3, session_01UCJpCyXwAUjiQHfXE3bsMs (Opus 5.5), parked at ~590k context (Lead brief 15:22Z); its last
CHECKER commit is 52a1e489 (C27 Addendum 4: R18 landed at 022ce8f PASS). There is no notes/CHECKER.md on any branch I hold
(`ls notes/` at b70aa59); the predecessor's state lives in docs/checker/C27.md and the NOW roster row.

### 1. Branch, head, ahead/behind trunk
- Branch claude/checker. After `git fetch origin claude/vibrant-johnson-nxvvxo claude/checker`: local = origin/claude/checker = 52a1e489
  (container not stale).
- `git rev-list --left-right --count origin/claude/checker...origin/claude/vibrant-johnson-nxvvxo`: 0 ahead, 157 behind trunk b70aa59f.
  52a1e489 is an ancestor of trunk (`git merge-base --is-ancestor`).
- So `git merge origin/claude/vibrant-johnson-nxvvxo` (normal merge, no rebase) was a FAST-FORWARD; no merge commit was made.
  Before this file's commit HEAD = b70aa59f, 0 ahead / 0 behind; after it, 1 ahead (this commit), 0 behind.

### 2. Open work and the next step of each
- C27 (R18) is CLOSED (Addendum 4, PASS, landed text verbatim at 022ce8f). Nothing else of the predecessor's is open.
- C28 (assigned by the Lead 15:22Z, no GO needed): landing gate for docs/agents/R19-draft.md at trunk b70aa59, lines 3-end;
  signed object docs/new/P-N5-RE-box26.md at trunk 52c7261 (sha1 8dba4576…); reports docs/referee/R-N5-RE.md (4457a9a; §C 87beaa6 +
  a3d1f70) and docs/referee-2/R2-N5-RE.md (3ee7b73, c66da44; §C dd5aaa2). Next step: verify the pins and sha1, re-fetch the referee
  branch heads (C27 E-1 lesson), then the five checks (statement diff incl. (NC) dropped / τ clause / 𝓡*, gap map vs both §C,
  every Data/Limits number, spot re-runs reentry.py + piececheck.py on fts_best16 and returns_rt48 plus REFEREE-2's nc_fail_n12,
  TARGET diff), report in docs/checker/C28.md, push with scripts/push.sh.
- notes/CHECKER.md does not exist; I create it (resume point, conventions, things only I know) with C28.

### 3. docs/GAPS.md rows I own
- None. No row has CHECKER in its owner column (`awk -F'|' '$4 ~ /CHECKER/'` on docs/GAPS.md: no output). CHECKER appears only as the
  gate that re-ran or passed a landing (GAP-A "re-run CHECKER C11"; G-N5-TIME "CHECKER C20"; G-N5-TERM "CHECKER C17 PASS").

### 4. The three owner rulings that most constrain me (verbatim), with index status
1. D1 (docs/DECISIONS.md#d1 key lines; docs/decisions/D001-launch-brief.md; DECISIONS-INDEX row D1 "active"):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   A landing passes only if no claim is stronger than what both referees signed, and the TARGET.md §5 scope is stated.
2. D18 (docs/DECISIONS.md#d18; DECISIONS-INDEX row D18 "active"; Lead reading L40 "active", labels PROVED/CONJECTURE/OPEN):
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
   For the gate: every conditional, DATA and open item in a draft must be labelled as such; a reading must not be presented as signed.
3. D15 (docs/DECISIONS.md#d15; DECISIONS-INDEX row D15 "active"; Lead reading L37 "active"):
   > q18 b. , q16 b,c. BUt I dont want it to ask these questions from me. Be autonomous, reason about it
   L37 (1): referee signatures on Opus are labelled "(Opus 5.5, D15)"; the gate checks the labels. I run on Opus under it, and decide
   inside the brief without option questions.
   (Also binding: D12/L33 for older "(Opus 5.5, D12)" labels; D7 stop on overage.)

### 5. One trap, and the check that prevents it
- Trap (C27 E-1, 2026-10-24 04:11Z): the predecessor checked the R18 draft against the referee reports as merged on trunk, while both
  referee branches already carried newer, unmerged §C2 sections that changed the signed object (07f298d → d78e54f) and the gap lists.
  A PASS against trunk alone would have landed an entry citing the wrong signed object. (A second miss of the same class, C27 E-3:
  instances named as members of 𝒞^1O that were not; caught only by counting Odd choice vertices from the files.)
- Check: before any verdict, `git fetch` the referee, referee-2 and lane branches, print their heads, and test each with
  `git merge-base --is-ancestor <head> <trunk pin>`; any head not on trunk is read and named in the report. Every class-membership or
  count claim about a pinned instance is recomputed from the instance file at the pin, not taken from the text.
- Also carried: push.sh output redirected to a file, then `$?` (never piped); re-runs in a detached worktree of the exact pin with the
  scripts unmodified; file sha1 of every signed object verified.
