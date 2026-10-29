# Handover check: L-COMP (successor 7, Opus 5.5; written 2026-10-29, date -u 10:00:34Z at start)
Every answer measured from the repository at the time of writing, not recalled from notes/L-COMP.md.
Successor of session_01JPReGnoQGuUgg6d59WzGYS (successor 6, resume point 9b029d23). This OVERWRITES successor 6's answers
(9c5bd6e2 era); those and older answers are in git history of this file.

## 1. Branch, head, distance to trunk
- Branch `claude/l-comp`, local head at start 9b029d23 (= origin/claude/l-comp after `git fetch origin claude/l-comp`).
- Trunk `origin/claude/vibrant-johnson-nxvvxo` = e3b435ab ("Lead: merge l-si (n29 killer, JOINT); NOW; log").
  Before merging: 9b029d23 was 0 ahead / 425 behind trunk (`git rev-list --left-right --count origin/claude/l-comp...origin/claude/vibrant-johnson-nxvvxo`),
  merge-base 9b029d23 (trunk contains every lane commit). `git merge --ff-only` to e3b435ab: now 0 / 0; +1 ahead after this file's commit.
- origin/claude/l-si = a9960e64, an ancestor of trunk (`git merge-base --is-ancestor`): the box 25-27 notes and tools are on trunk.
- Container: Oink not present at start (tools/oink/build/oink missing); scripts/setup_oink.sh started in this session.

## 2. Open work and the next step of each
- In flight at handover: nothing (successor 6: "No background jobs", box 16 closed).
- Successor 6's unrouted item: an H_n variant whose Odd gate re-opens many times (L-RED / L-NEW design; L-COMP measures it with
  experiments/friedmann-hn/randstarts2.py --var). No step unless routed.
- BOX 17 (Lead brief 09:59Z, started without waiting): exhaustive small-n tables of (a) SEG-COUNT excess, (b) SEG(S) and SEG(S)/n,
  (c) L-WAVE′ gap, (d) f per phase, over all games up to the largest feasible n and all start pairs. Next step: cross-check my
  implementation against L-SI's tools (experiments/si/lay/segsw.py, grun/relseg.py, grun/lwave.py, ALT §13 f) on their pinned
  instances, then enumerate. Tools and tables go to experiments/n5-box17/.

## 3. docs/GAPS.md rows owned by L-COMP
None. Open table (lines 6-11) owners: L-ALG (GAP-A, GAP-C, G-S5-6), L-RED (G-NEST), L-NEW (G-N1-LB, G-N5-TIME).
`grep -n L-COMP docs/GAPS.md` hits line 16, G-N5-TERM (closed; owner L-NEW, "L-COMP checks runs"), and DATA citations in line 11
(G-N5-TIME). Box 17 feeds G-N5-TIME (SEG-RUN, FB-LIN data).

## 4. Three owner rulings that most constrain this lane (verbatim; status from docs/DECISIONS-INDEX.md on e3b435ab)
1. D18 (active, DECISIONS-INDEX.md:32), docs/DECISIONS.md:333:
   > Focus on N5 and work toward proving it. Explore novel approaches, especially by connecting ideas from areas of mathematics and computer science that are not usually studied together. Make reasonable assumptions where needed, state them briefly, and proceed without asking me questions. Clearly distinguish proven results from conjectures and open problems.
   Constraint: box 17 numbers are DATA ("exhaustive at n ≤ N"), never PROVED; the enumeration model is stated as an assumption.
2. D2 change 5 (D2 active, DECISIONS-INDEX.md:6), docs/DECISIONS.md:27-28:
   > 5. Gauntlet addition: every implementation also outputs positional strategies, and L-COMP verifies them on every
   >    test game.
   Constraint: every extremal or violating instance is checked against Oink and verify.py before it is reported.
3. D1 (active, DECISIONS-INDEX.md:5), docs/DECISIONS.md:6-7:
   > Never publish, post, email, submit or contact anyone outside the fleet. Anything external is my decision.
   > A claimed polynomial algorithm is far more likely to be wrong than right. Treat every such claim, including the fleet's own, as wrong until it passes the gauntlet below.
   Constraint: a violation goes to the Lead at once with its instance and a second-engine reproduction; results leave only via
   scripts/push.sh and send_message to the Lead.

## 5. One trap that bit this lane, and the check that now prevents it
Trap (successor 6): a Lead message claimed 973520df was on trunk when it was not. Check: `git merge-base --is-ancestor X trunk`
before relying on any "on trunk" claim (used above for l-si a9960e64). Also carried: read notifications between wait steps of long jobs.
