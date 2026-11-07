#!/bin/bash
# one-off (L-COMP box 28, 07:1xZ): q2pieces.sh's parent shell was stopped (to edit the script) while drup checked q2_c0s0p0; drup
# (pid in $1) kept running, writing to log/q2/q2_c0s0p0.chk.tmp. Wait for it, finish the record as q2pieces.sh would (wall time from
# the proof file's mtime = when Glucose finished and drup started; drup's exit code is not available to a non-parent), then start
# q2pieces.sh (which skips c0s0p0 if its .chk holds «s VERIFIED», and regenerates it otherwise).
cd "$(dirname "$0")"; n=q2_c0s0p0; R=log/q2/$n; P=/home/user/pf/q2
while kill -0 $1 2>/dev/null; do sleep 20; done
t0=$(stat -c %Y $P/$n.proof); echo "drup exit (not available: parent stopped) wall $(( $(date +%s) - t0 )) s (from the proof mtime)" >> $R.chk.tmp; mv $R.chk.tmp $R.chk
rm -f "$P/$n.proof" "$P/$n.proof.cnf"
echo "$(date -u +%FT%TZ) $n (-2,-8,-14,-20,-26,-32,-38,-44): $(grep -o 'glucose4 [A-Z]* [0-9.]* s\|sha1 [0-9a-f]*\|bytes [0-9]*' $R.gen | tr '\n' ' ') $(grep -h '^s ' $R.chk)" >> log/q2/summary.txt
PDIR=$P setsid nohup ./q2pieces.sh < /dev/null > log/q2pieces.run 2>&1 &
echo $! > cubes/.pid_q2
