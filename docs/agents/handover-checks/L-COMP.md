# Handover check: L-COMP (successor 3, Opus 5.5; written 2026-10-24T17:44Z by date -u)
Every answer measured from the repository at the time of writing, not recalled from notes/L-COMP.md.
Successor of session_01TpuThMoeBcLB2T5KKeJpAa (parked after box 4; handover 298d2dc6 "L-COMP box 4 done ... handover notes; park").
The previous answers (2026-10-23) are in git history of this file.

## 1. Branch, head, distance to trunk
- Branch `claude/l-comp`; local head at start = origin/claude/l-comp = 298d2dc6 (working tree clean; 298d2dc6 is an ancestor: checked).
- Trunk `origin/claude/vibrant-johnson-nxvvxo` fetched: d1326c4b ("Lead: NOW roster (L-SI successor 2)", 2026-10-24 17:35Z).
- Before merging: `git rev-list --left-right --count HEAD...origin/claude/vibrant-johnson-nxvvxo` = 4 ahead (box 4 commits ee440b10,
  2629ccae, eba6a9ae, 298d2dc6), 70 behind; merge-base 079fd1e7.
- Merged trunk with a merge commit (no rebase): 7f1331cc. After it: 5 ahead, 0 behind (6 ahead after this file's commit).
- Container: Oink not built (tools/oink/build absent), no python jobs running, no timed wakes.

## 2. Open work and the next step of each
- In flight: nothing (predecessor stopped every run at 17:35Z; partial JSONs are in experiments/n5-exhaustive/results/).
- Box 5 (routed in this brief, waits for "go"): X (crossing transitions, R changes) and O (OTHER-touching transitions: (h) fails and
  Xi != W) per joint lambda-phase. Next step after go: build Oink (scripts/setup_oink.sh); read experiments/new/box28/fbre.py,
  eqcheck.py and experiments/new/box25/phaseprofile.py; add X and O to box4.measure; cross-check counts against L-NEW's tools on
  sc32, theta_tp32, fts_best16, fbref_cex_n32 (experiments/red/xing/instances/) before any table.
- n 5 canonical subset (box 3/4): partial, no resume support. Next step: add --slices to box4.py exh and run the 160 (o, parity)
  slices on 3 cores (part (b) of box 5).
- sat-hard (L-STRUCT T3 support), counter_qpt growth class: parked/low priority, no step unless routed.

## 3. docs/GAPS.md rows owned by L-COMP
None. `git show origin/claude/vibrant-johnson-nxvvxo:docs/GAPS.md | grep -n -i l-comp` returns one row, G-N5-TERM (closed; owner L-NEW,
"L-COMP checks runs"), closed 2026-10-19 by RESULTS R15. Box 5 feeds G-N5-TIME (owner L-NEW, open): its box-28 §5c note names (X)
and (NH') as OPEN, with DATA "X <= n on named instances; climb X = 37 > n = 32".

## 4. Three owner rulings that most constrain this lane (verbatim; status from docs/DECISIONS-INDEX.md on d1326c4b)
1. D18 (active), docs/DECISIONS.md:333:
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
   Constraint (with Lead reading L40 (2)c, (4)): my box is exhaustive small-n tables for N5; every line I report is labelled
   DATA (exact for the enumerated class) / CONJECTURE / OPEN, never PROVED; no questions to the owner.
2. D16 (active), docs/DECISIONS.md:300:
   > Then keep working as I told you to
   Constraint (Lead reading L38): no idle lane; when a run is going I prepare the next step, and the box ends with a queue.
3. D1 (active), docs/DECISIONS.md:6 (launch brief docs/decisions/D001-launch-brief.md:96):
   > Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision.
   Constraint: results go only to the repo via scripts/push.sh and to the Lead via send_message. Also from D1 (DECISIONS.md:7):
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   so any instance with X > n or super-linear X/O at small n goes to the Lead at once, checked first (check_instance.py: n5b, Oink zlk, verify.py).

## 5. One trap that bit this lane, and the check that now prevents it
Trap: two phase conventions. Box 4 found that exh.py's maxph keys a phase by joint lambda only (box21 phases.py), while box4.py keys
it by (lambda_sigma, lambda_tau, tau(o)) (box25 phaseprofile.py); on n 4 all starts they gave max phase lengths 4 vs 3. A per-phase
maximum (X, O) under the wrong key would be a different number with the same name.
Check now: box 5 uses phaseprofile.py's key only (the brief names it), the table header names the key, and before any table the
X and O counts must equal L-NEW's fbre.py / eqcheck.py counts on the four pinned instances (sc32, theta_tp32, fts_best16,
fbref_cex_n32; sha1 checked against 901674dc...). A mismatch is traced to a definition before any table is written.
Second check carried over: a stale container (this one was 70 behind trunk) is caught by fetch + is-ancestor + merge before work.
