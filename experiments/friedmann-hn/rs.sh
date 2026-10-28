#!/bin/bash
# randstarts.py over rs_jobs.txt (N R SEED GSTEP; env JOBS = job file), P in parallel; logs results/rs_H<N>.log
cd "$(dirname "$0")"; mkdir -p results
xargs -P "${P:-4}" -L 1 sh -c 'python3 randstarts.py "$@" > results/rs_H$1.log 2>&1 || echo "EXIT $?" >> results/rs_H$1.log' _ < "${JOBS:-rs_jobs.txt}"
