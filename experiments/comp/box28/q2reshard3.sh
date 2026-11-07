#!/bin/bash
# L-COMP 11 (one-shot): wait until q2_c0s1p0 has a final .chk, then stop both 2-shard workers (pid files + children), delete their
# in-flight proof/tmp files (those pieces are regenerated from scratch by the new owner) and start the 3-shard workers via relaunch_all.sh.
cd "$(dirname "$0")"
until [ -f log/q2/q2_c0s1p0.chk ]; do sleep 5; done
for f in cubes/.pid_q2 cubes/.pid_q2b; do P=$(cat $f); C=$(pgrep -P $P); G=$(for c in $C; do pgrep -P $c; done); kill $P $C $G 2>/dev/null; done
sleep 5; for f in cubes/.pid_q2 cubes/.pid_q2b; do while kill -0 $(cat $f) 2>/dev/null; do sleep 1; done; done
for t in log/q2/*.chk.tmp; do [ -f "$t" ] && rm -f "$t"; done
for g in /home/user/pf/q2/q2_*.proof /home/user/pf/q2/q2_*.proof.cnf; do [ -f "$g" ] && rm -f "$g"; done
echo "$(date -u +%FT%TZ) q2reshard3: 2-shard workers stopped after c0s1p0; 3 shards started" >> log/q2/reshard.txt
./relaunch_all.sh >> log/q2/reshard.txt 2>&1
