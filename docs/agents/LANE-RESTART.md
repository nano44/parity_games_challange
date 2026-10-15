# Lane restart procedure
Replace a session at about 600k context, at a natural pause.
1. Old session overwrites notes/<LANE>.md with DONE, IN FLIGHT, NEEDS, "Things only I know"; pushes; reports the SHA; then parks.
2. Lead: create_session on the lane branch, outcome_branch = that branch, clone_depth 3000, with the lane brief.
3. New session answers the five questions into docs/agents/handover-checks/<LANE>.md, pushes, stops.
4. Lead re-measures each answer against the repo; a miss is written into the files before "go".
5. Record a row below, update the NOW roster.

Five questions:
1. Your branch, its head SHA, and how many commits ahead of and behind trunk (claude/vibrant-johnson-nxvvxo).
2. Your open work and the next step of each.
3. The docs/GAPS.md rows you own, with status.
4. The three owner rulings that most constrain you, verbatim, with their status in docs/DECISIONS-INDEX.md.
5. One trap that bit this lane before, and the check that now prevents it.

| date | lane | old session | new session | score (of 5) | misses fixed |
| --- | --- | --- | --- | --- | --- |
| 2026-10-15 | L-LOWER | session_01U5n8mgXxgyGzvuUzxHbiKx | session_0153E4mCB2wqi65xdfpxozfK | 5 | none (answers re-measured: 29/18 vs trunk, merge-base fe676d9, no GAPS rows, core 100 games) |
| 2026-10-15 | L-ALG | session_01WN44zjFXZSqaL5SwsoDn7d | session_012cQPWcEm23KMdMQSvWrULr | 5 | none (re-measured: merge-base 1017502, 0 ahead; 107 behind at its fetch, 112 now after Lead commits; no GAPS rows; T-ALG1 unrouted is correct: deferred by Lead) |
