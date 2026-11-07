#!/bin/bash
# R173: adversarial random sweep for Lemma PORTAL: genportal.py N SEED with a random valid start, then portalck.py (one line per seed).
cd "$(dirname "$0")/../.."
N=$1; A=$2; B=$3; d=red/r173/rnd
for s in $(seq $A $B); do python3 red/r173/genportal.py $N $s $d/q.$N.$s.pg $d/q.$N.$s.start
  timeout 300 python3 -I red/r173/portalck.py $d/q.$N.$s.pg $d/q.$N.$s.start 2>&1 | tail -1 | sed "s/^/seed $s /"
  rm -f $d/q.$N.$s.pg $d/q.$N.$s.start; done
