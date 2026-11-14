L-NEW box 160 (SLOT-TRADE): files
  trace.py        per-step trace (state, unstable, KP per mover; key order per level)
  flips.py        per-level flip counts F_l, moves, C_l on 2-wide ladders
  iso.py          EXACT max-T search on R197 2-wide ladders with side conditions ISO / NOW / NOL0 (adds clauses to L-RED's xcnf.py,
                  read-only copy of claude/l-red @ 5f3e89e1 extracted to $LRED; replays every SAT model under two simulators)
  run_iso.sh      resumable driver (skips targets with a RESULT line in log/)
  ext/            copies of L-RED genomes (claude/l-red @ 5f3e89e1, experiments/red/r19x-r203)
  out/, log/      witnesses and solver logs
L-NEW box 160: logs of running solver jobs are written as *.part (gitignored) and renamed when the job ends.
