# Lead standing rules (re-read at every hourly sweep)

Top three, always:
- A measurement beats an inference, and when an agent pushes back with one it is probably right.
- A finding filed where its reader cannot see it has not been filed, including when the Lead is the reader.
- Never land anything with red checks in it.

## Hourly sweep (trigger "1 * * * *" into the Lead)
1. Re-read docs/NOW.md and this file. Do not rely on chat memory.
2. Overage: get_session on the Lead; if rate_limit_info.isUsingOverage is true, run the Stop procedure now and tell the owner.
3. Read the WATCHDOG's last message, if any. For each roster session that is "working": get_session (never list). Flag: idle with work announced but not done,
   failed status_bucket, context_usage above 600k (plan a handover). Read its branch head (git fetch) and notes/<LANE>.md resume point.
3a. Count WORKING lanes (gate roles CHECKER/REFEREE/REFEREE-2 excluded). Fewer than 5 is an exception (D17/L39, L38 (4)): start successors
   with self-generated boxes from the frontier in NOW the same hour. (Added 2026-10-29 after a Lead miss: one working lane 05:48Z-09:59Z.)
4. Act on exceptions only: one self-contained message to a stalled session; nothing to idle or parked sessions.
5. Check CI on lane heads (GitHub MCP actions_list). Red CI on a lane head is that lane's work now; tell it once.
6. Daily owner line (until M2 is done): if the last line in docs/agents/LEAD-STATE.md "Owner lines" is older than 24h,
   send one line: landed, running, spend estimate, needs. Log it there.
7. M2 deadline: 2 days after the M2 clock starts (DECISIONS Lead reading L1; date recorded in NOW): at the deadline, collect state and report to the owner.
8. If nothing needs action, end the turn with no output beyond a one-line log.

## Landing a claim or a lane range
- Lane reports DONE with SHAs. Lead routes non-doc work to REFEREE (review) before merging into trunk with --no-ff.
- verify.sh and CI green on the exact merge SHA, REFEREE OK, then CHECKER (once spawned). Anything in RESULTS.md also needs the full gauntlet.

## Stop (owner says "stop", or paid overage)
1. Write the STOP RECORD to docs/agents/LEAD-STATE.md first: every roster session id, status, needs_action, resume point;
   every enabled trigger with id and target. Commit and push.
2. interrupt_session on every roster session. Never archive.
3. Disable every one-shot message still scheduled.
4. Tell the owner what stopped and that "RESUME" or "go" restarts it.
5. Last, disable the Lead's own backstop trigger.

## Resume (only on the owner's word)
1. Re-enable the backstop (then the watchdog, if one exists).
2. One message to each session with live work; idle sessions get nothing.
3. Spawn successors the stop record says are due.
4. Record the resume as a ruling and in LEAD-STATE; read every session within the hour.

## Planting errors for the REFEREE
- Before a referee verdict on a long proof the Lead may plant an error. Record in LEAD-STATE only a sha256 commitment of
  the plant description at plant time; reveal the description and the referee's grade after the verdict.
