# Handover check: L-COMP (successor 5, Opus 5.5; written 2026-10-26T07:45Z by date -u)
Every answer measured from the repository at the time of writing, not recalled from notes/L-COMP.md.
Successor of session_01AiLCefKYn3CkbJsYJtY5aR (successor 4, handover 0f200c63). This OVERWRITES successor 4's answers (cd3b5ff7);
those and older answers are in git history of this file.

## 1. Branch, head, distance to trunk
- Branch `claude/l-comp`. Local head at start was 298d2dc6 (stale container again); `git fetch origin claude/l-comp
  claude/vibrant-johnson-nxvvxo` moved origin/claude/l-comp 298d2dc6..0f200c63; 0f200c63 is an ancestor of it (is-ancestor OK);
  working tree clean, so fast-forwarded to 0f200c63.
- Trunk `origin/claude/vibrant-johnson-nxvvxo` = 71c4e31a ("Lead: land R64 (EPR, C73 7b326f11) after R61, R63; GAPS/NOW; log").
  Before merging: origin/claude/l-comp was 4 ahead / 27 behind trunk (`git rev-list --left-right --count`).
  Merged trunk with a merge commit (no rebase): 11ba4e5c. Now `HEAD...origin/claude/vibrant-johnson-nxvvxo` = 5 ahead / 0 behind
  (4 lane commits + the merge); merge-base 71c4e31a. +1 ahead after this file's commit.
- Container: Oink not built (tools/oink/build absent); no python jobs (`pgrep -a python` empty); no timed wakes.

## 2. Open work and the next step of each
- In flight: nothing (successor 4's notebook: "IN FLIGHT: nothing (no background jobs)"; boxes 7-11 pushed, last 1d2f29d7).
- BOX 12 (Lead brief, waits for "go"): epoch census for N5 (D18). (a) N_ep, ρ = Σ_q ρ_q and the ALT residuals tie_q, nc_q, cyc_q per
  phase; (b) per epoch |D_E|, len(E), X_SN^pre(E), len distribution by |D_E| ∈ {0, 1, ≥2}, EP-0 (len ≤ n + m when D_E = ∅) as a
  falsification test; (c) budgeted climbs on N_ep/n and on max len(E) over |D_E| ≥ 2 epochs vs n, pinned with sha1s.
  Next step after GO: read RESULTS R60 (l.3058), R61 (l.3103), R63 (l.3156), R64 (l.3206) and docs/new/N5-NEP*.md (NOT on trunk
  71c4e31a: `ls docs/new | grep -i nep` finds only N5-oneplayer-box7.md; locate it on origin/claude/l-new), pin each definition
  (epoch, D_E, len, X_SN^pre, ρ_q, tie/nc/cyc) with its line, then extend my n5 / n5tau / gdnc_check.state_info machinery;
  build Oink (scripts/setup_oink.sh) for the check_instance gate.
- Parked/low (no step unless routed): sat-hard cells; counter_qpt growth class.

## 3. docs/GAPS.md rows owned by L-COMP
None. `grep -n -i l-comp docs/GAPS.md` on 71c4e31a hits only line 16, G-N5-TERM (closed; owner L-NEW, "L-COMP checks runs").
Box 12 feeds G-N5-TIME (line 11; owner L-NEW, open): its note now reads "epochs are bounded by ρ plus ties, non-clean and cycle-node
changes (ALT); ... EP-0 ... EP-k ... EP-1 ... epochs OPEN; general games OPEN".

## 4. Three owner rulings that most constrain this lane (verbatim; status from docs/DECISIONS-INDEX.md on 71c4e31a)
1. D18 (active), docs/DECISIONS.md:333:
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
   Constraint (L40 (2)c): exhaustive / census tables for N5; every number labelled DATA, never PROVED by me; no owner questions.
2. D2 change 5 (D2 active), docs/DECISIONS.md:27-28:
   > 5. Gauntlet addition: every implementation also outputs positional strategies, and L-COMP verifies them on every
   >    test game.
   Constraint: every pinned instance passes check_instance.py (n5b SPEC, Oink zlk or --tl, verify.py strategies) before it is reported.
3. D1 (active), docs/DECISIONS.md:6-7:
   > Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision.
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   Constraint: EP-0 and every landed epoch statement are run as falsification tests; a violation goes to the Lead at once with the
   instance, after check_instance; results leave only via scripts/push.sh and send_message to the Lead.

## 5. One trap that bit this lane, and the check that now prevents it
Trap: checker/format mismatch producing fake violations. In box 10 (successor 4, notebook "Things only I know") REFEREE-2's checkers
expected FULL strategy lists with non-own entries constant along a run; a combined list produced 3 fake "fallback changes τ" FAILs.
Check now: before reporting any violation, (i) re-run the instance through check_instance.py (n5b SPEC state sequence = n5.py),
(ii) confirm the checker's input convention on a pinned instance where the property holds (and a mutation where it must fail),
(iii) only then message the Lead. Carried over: stale container (fetch + is-ancestor before work, done above).
