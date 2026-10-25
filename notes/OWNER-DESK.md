# OWNER-DESK notebook
Overwrite the top sections; append to "Sources opened" and "Dead ends".

## Resume point
2026-10-22 ~07:10Z. D4-D15 recorded. No owner questions open. Standing D15/L37: never ask the owner option, model,
allocation or reassessment questions; raise only TARGET changes, external acts, paid overage, restart after stop, >5 sessions.
Reports (milestones, step-2 survivors, incorrect runs, super-poly families, step-4 claims, weekly checkpoint) are information only.

## Queue
1. On each owner reply: log verbatim in docs/owner-desk/LOG.md, relay verbatim to the Lead (session_014FBi6o334DvwT5Uw2kDfoN).
2. Answer progress questions from the repository (git fetch origin; lane branches, notebooks), citing file and SHA.
3. Mark questions closed when the Lead reports a D-number.

## Sources opened
| source | used for | opened on | note |
| --- | --- | --- | --- |
| fleet files only (TARGET.md, docs/NOW.md, DECISIONS, GAPS, RESULTS at d580fcd; l-lower 9ece275 docs/lower/L1-report.md §4) | status reply | 2026-10-15 | no external sources; the desk cites fleet files, not literature |
| Huth-Kuo-Piterman, Imperial DTR 2015/4 (9 Aug 2015), www.doc.ic.ac.uk/research/technicalreports/2015/DTR15-4.pdf (owner upload, same sha256) | Q5: §5 Fig. 7 (psolB), Thm 4 p.12 (psolC ⊇ psolB), §7-8; full-text search for psolB completeness | 2026-10-15 | pre-publication text of LNCS 9560 chapter; Springer version still unopened |

## Dead ends
(none)

## Things only I know
- For DTL status questions, the crux is docs/alg/GAP-A-M.md §12 on l-alg: polynomial bound needs (H1)-(H4), none proved; APP(k) (§10)
  shows proved facts allow 2^Theta(n) searches. L-RED tries to realise APP; L-ALG tests a potential for (H2b). (Lead, 2026-10-16 10:36Z.)
- The owner also answers questions in the Lead session (Q9, Q11): re-sync QUESTIONS.md from docs/NOW.md "Owner questions open".
- 2026-10-22 07:1xZ: pushed 79abccc2 with scripts/verify.sh FAILED (my regex dropped "## Resume point"; I piped verify through
  `tail -1`, so `&&` did not gate the push). Fixed in the next commit. Lesson: never pipe verify before `&&`; use
  `scripts/verify.sh >/dev/null && git push`.
- 2026-10-22T07:12Z Lead correction: push ONLY with scripts/push.sh, output redirected to a file, then print $? (never a pipe,
  never verify.sh && git push). Timestamps: take them from date -u in the same command that writes them.
