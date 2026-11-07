#!/bin/bash
# L-COMP 11 one-shot: stop the running shard 2 of 3 at a piece boundary (after its current piece's .chk is final) and start q2chain2.sh.
cd "$(dirname "$0")"; P=$(cat cubes/.pid_q2c); n=$(grep -c . log/q2/summary.txt)
while [ "$(grep -c "q2_c0s1p6 " log/q2/summary.txt)" = 0 ]; do sleep 5; done
kill -STOP $P; C=$(pgrep -P $P); G=$(for c in $C; do pgrep -P $c; done)
PF=$(for x in $C $G; do ps -o args= -p $x; done | grep -o "/home/user/pf/q2/q2_c[0-9s]*p[0-9q]*\.proof" | head -1)
kill $C $G 2>/dev/null; kill $P; kill -CONT $P; while kill -0 $P 2>/dev/null; do sleep 1; done
[ -n "$PF" ] && rm -f "$PF" "$PF.cnf" && echo "removed in-flight $PF" >> log/q2/reshard.txt
for t in log/q2/*.chk.tmp; do [ -f "$t" ] && rm -f "$t"; done
ls /home/user/pf/q2/ > log/q2/stop2_pf.txt
echo "$(date -u +%FT%TZ) q2stop2: shard 2/3 stopped after c0s1p6; deferred to q2chain2.sh (after shard 0/3)" >> log/q2/reshard.txt
setsid nohup ./q2chain2.sh < /dev/null > log/q2shard2.run 2>&1 & echo $! > cubes/.pid_q2c
