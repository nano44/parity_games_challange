#!/bin/bash
# Box 191 growth climbs (resumable: each climb restarts from its best genome OUT.json). Run from experiments/new/box191.
for spec in "1 6" "1 9" "1 12" "0 10"; do set -- $spec
  ONEP=$1 nohup python3 climb191.py T $2 2 2 4$2 20000 out/g${1}_d$2 >> out/g${1}_d$2.log 2>&1 &
done
wait
