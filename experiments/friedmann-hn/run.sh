#!/bin/bash
# run box16.py over jobs.txt lines (N START [--mode M]), P in parallel; one log line per job in results/box16.log
cd "$(dirname "$0")"; mkdir -p results; : > results/box16.log
P=${P:-4}
xargs -P "$P" -L 1 sh -c 'python3 box16.py "$@" >> results/box16.log 2>&1 || echo "EXIT $? $*" >> results/box16.log' _ < jobs.txt
echo ALLDONE >> results/box16.log
