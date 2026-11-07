#!/bin/bash
# one-off (Lead 09:32Z): stop lane C_d23 at 10:35Z (one more hour), by its pid file; mark it STOPPED in relaunch30.sh and its log.
cd "$(dirname "$0")"; until [ $(date -u +%H%M) -ge 1035 ]; do sleep 30; done
p=$(cat out/.pid_C_d23); kill $p; sleep 2; c=$(ps -eo pid,args | awk '/rclimb30 out\/(C_d23_best|seed_d23_rm21)\.txt/ && !/awk/ {print $1}'); [ -n "$c" ] && kill $c
sed -i 's|^up C_d23 |# STOPPED 10:35Z (Lead 09:32Z): up C_d23 |' relaunch30.sh
echo "$(date -u +%FT%TZ) C_d23 STOPPED (Lead 09:32Z: one more hour, then stop; S(h) DATA = out/remlevel_profiles.txt)" >> out/C_d23.log
