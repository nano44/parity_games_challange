#!/bin/bash
# randstarts2.py over a job file (lines: N R SEED GSTEP [--var NAME]), P in parallel; logs results/rs2_<N><VAR>.log; ALLDONE marker
cd "$(dirname "$0")"; mkdir -p results; J="${JOBS:-rs2_jobs.txt}"
xargs -P "${P:-4}" -L 1 sh -c 'L=results/rs2_$1${6:-}.log; python3 randstarts2.py "$@" > $L 2>&1 || echo "EXIT $?" >> $L' _ < "$J"
echo ALLDONE > "results/$(basename "$J" .txt).done"
