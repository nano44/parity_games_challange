#!/usr/bin/env bash
# DTL tangle counts at the largest sizes reachable (raw, 600 s per game); appends to out/dtl_growth.log
O=../../tools/oink/build; HF=../hard-families
run() { local name=$1 N=$2 f=$3; local n=$(grep -c ";" $f); local t0=$(date +%s); local w=$(timeout 600 $O/oink --dtl -v --no-single --no-wcwc $f 2>&1 | grep -oE "[0-9]+ tangles|solution verified" | tr '\n' ' '); echo "$name N=$N n=$((n-1)) dtl: ${w:-TIMEOUT} ($(( $(date +%s) - t0 ))s)"; }
for N in 40 48 64; do $O/tc $N > /tmp/g.pg; run tc $N /tmp/g.pg; done
for N in 64 100; do $O/counter_symsi $N > /tmp/g.pg; run counter_symsi $N /tmp/g.pg; done
for N in 64 100; do $O/counter_rr $N > /tmp/g.pg; run counter_rr $N /tmp/g.pg; done
for N in 64 100; do $O/counter_dp $N > /tmp/g.pg; run counter_dp $N /tmp/g.pg; done
for N in 64 100; do $O/counter_m $N > /tmp/g.pg; run counter_m $N /tmp/g.pg; done
for N in 64 100; do $O/counter_core $N > /tmp/g.pg; run counter_core $N /tmp/g.pg; done
for N in 40 48; do $O/counter_rob $N > /tmp/g.pg; run counter_rob $N /tmp/g.pg; done
for N in 64 100; do $O/counter_ortl $N > /tmp/g.pg; run counter_ortl $N /tmp/g.pg; done
for N in 256 512; do $O/counter_qpt $N > /tmp/g.pg; run counter_qpt $N /tmp/g.pg; done
for N in 64 100; do python3 $HF/pgsolver_port.py recursiveladder $N > /tmp/g.pg; run recursiveladder $N /tmp/g.pg; done
for N in 64 128; do python3 $HF/pgsolver_port.py switchallexp $N > /tmp/g.pg; run switchallexp $N /tmp/g.pg; done
for N in 64 128; do python3 $HF/pgsolver_port.py switchbestexp $N > /tmp/g.pg; run switchbestexp $N /tmp/g.pg; done
for s in 10 11 12; do python3 -c "import sys; sys.path.insert(0,'.'); sys.path.insert(0,'../harness'); import strfam, pg; pg.write(strfam.S($s), '/tmp/g.pg')"; run strfam $s /tmp/g.pg; done
