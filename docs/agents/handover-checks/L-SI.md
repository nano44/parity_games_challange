# Handover check: L-SI (successor 7, written 2026-10-25T13:58Z by date -u; LANE-RESTART step 3; Opus 5.5, D18/L40)
Every answer below was measured in this container; the commands are given. Predecessor: successor 6, session_01WZRciyMqz1LNWwdFoeq2AP.
Its handover is dbef1de6, notes/L-SI.md "## HANDOVER (successor 6, box 11)".

## 1. Branch, head, distance to trunk
- Branch `claude/l-si`. Commands: `git fetch origin claude/l-si`, then `git checkout -B claude/l-si origin/claude/l-si` → head dbef1de6.
  - This container's local branch was already up to date with origin, unlike successors 4-6. The fetch moved origin 0d48da26 → dbef1de6.
- Trunk = claude/vibrant-johnson-nxvvxo at 601df6ed ("Lead: R36 LANDED (P-N5-P1, CHECKER C45 3667fb1c); GAPS; P-N5-LV pinned; NOW, log").
  - Before the merge: `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` = 1 ahead / 55 behind;
    merge-base b7f18feb.
  - `git merge --no-ff origin/claude/vibrant-johnson-nxvvxo` (merge commit "L-SI succ. 7: merge trunk 601df6e") → 2 ahead / 0 behind.
  - My first push of this file (2e1a7c29) was rejected: successor 6 had pushed 84974fea at 13:55Z (P-N5-LV addendum).
    `git merge --no-ff origin/claude/l-si` brought it in (no rebase). The pushed head SHA is in the message to the Lead.

## 2. Open work and the next step of each (nothing running; fresh container)
The frozen files and their sha1s are re-measured with sha1sum.
- P-N5-ENT (docs/si/P-N5-ENT-box11.md, 4fd22be7):
  - REFEREE succ. 8 report docs/referee/R-N5-ENT.md is on trunk. It signs §1-§3 (FZ, BF, RB, WALK, CYC-EV, TEV-FB). It signs §4-§5
    (ENT-X, NJB-A, D1, PL-S″) CONDITIONAL ON (P). There are no gaps and §6 is not signed.
  - R2-N5-ENT: not on trunk or on origin/claude/referee-2. REFEREE-2 succ. 9 is WORKING on it (NOW roster).
  - Since R36 has LANDED (Lemma P1 = (P) for one-player games), the (P) condition should lift once ENT lands. READING, to be confirmed by
    the referees/CHECKER.
  - Next step: any items go to a NEW file docs/si/P-N5-ENT-fixes-box11.md (does not exist).
- P-N5-LV (docs/si/P-N5-LV-box11.md, d0d797f0): pinned on trunk and queued after NEB (NOW). No R-N5-LV / R2-N5-LV yet.
  - Addendum docs/si/P-N5-LV-addendum-box11.md (a15a8871; successor 6, 84974fea; answers Lead 13:51Z) is not yet on trunk.
    - It points to the (β) bound already in the packet (PL_{−1} / LV-PL cover (β)-fallbacks with r ≥ 0).
    - It marks the NL= straddle material NOT TO SIGN.
  - Lead: please pin the addendum with the packet.
  - Next step: items go to a NEW file docs/si/P-N5-LV-fixes-box11.md.
- Level −1 (successor 6 NEXT 2), OPEN:
  - (a) THR fallbacks with u* = none (r = −1; NL at L = −1 is not available).
  - (b) A length-based ENT-SHAPE, to drop REL(S) from LV-PL ≤ n·n_E·(d_o + REL(S)).
  - (c) Or exclude a (β)-fallback, giving "THR ⇒ M ≥ 0" in scope (P-N5-LV §1/§5).
  - First step: (c) via the N5-LV §3 kill shape, checked against experiments/si/tev/lvm1.py. DATA so far: 1,032 in-scope THR, all M ≥ 0.
- NL= (straddle; N5-STR/STR2) CONJECTURE: off the critical path (Lead agreed). Only if cheap; it buys a factor 2.
- Not started from older successors: two-player VJ00 Lemma 5.8 (R15's G-N5T-3), the remaining half of (P).

## 3. docs/GAPS.md rows I own
- None. L-SI owns no GAPS row.
- The row I work under is G-N5-TIME: major, owner L-NEW, status open.
  - Last update 13:52Z: R36 [refereed-only] LANDED (P-N5-P1 + fixes, addendum §3; CHECKER C45). This discharges R18's premise (P) for
    one-player games only and "Adds no running-time bound. Open as before."
  - "Open as before" (11:51Z update): "NJB = ENT (CONJECTURE; lane reductions EV/EV+/TEV-RED in review as P-N5-RL), REL(S), level −1
    fallbacks, out-of-scope fallbacks (P-N5-SCOPE in review; lane NO-ENTRY-A), θ-changes per HN stretch."
- G-N5-TERM: closed (R15).

## 4. The three owner rulings that constrain me most (verbatim from docs/DECISIONS.md; status from docs/DECISIONS-INDEX.md)
- D18 (index: active): "Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas
  of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them
  briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems."
  - Lead reading L40 (active): L-SI is the OR/MDP lens on N5.
- D1 (index: active; full text docs/decisions/D001-launch-brief.md). Key lines:
  - "A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own,
    as wrong until it passes the gauntlet below."
  - "Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision."
- D16 (index: active): "Then keep working as I told you to"

## 5. One trap that bit this lane before, and the check that prevents it
- Trap: editing a packet or fixes file after its sha1 had already gone to the Lead. Several Lead messages crossed with successor 6's
  files, and referees pin by sha1 (R-N5-ENT checks `git show 765e893:docs/si/P-N5-ENT-box11.md | sha1sum` = 4fd22be7).
- Check: before touching any docs/si/P-* or *-fixes-* file, `sha1sum` it and grep notes/L-SI.md and docs/NOW.md for that sha1. If the
  sha1 is listed, the file is FROZEN and new text goes in a NEW file.
  - Today's frozen list: ENT 4fd22be7, LV d0d797f0, N5-LV 407c5520, N5-LV2 94ac2469, N5-TEV 58a0b3cf, STR c7b9c671, STR2 b6ed9476,
    RL-fixes ac027458, RL-fixes2 b3e3cd93, P1-fixes 83ef83b0, RL-P1-addendum 5c29d93d, LV-addendum a15a8871.
  - This bit me in this very check: my push crossed with successor 6's 13:55Z addendum. Fetch before pushing, and merge, never rebase.
- Still live from successors 5-6:
  - Never `pkill -f <pattern>` from a shell whose own command line contains it (exit 144).
  - `git log -- <path>` takes more than 120 s here.
  - Never `git add -A`; add files by name.
