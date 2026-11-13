#!/bin/bash
# REFEREE-2 40: one process per (rule, genome file) / per (rule, random set); resumable (skips outputs with a TOTAL line); run from r2b212/
export R2DIR=/home/user/parity_games_challange/docs/referee-2 PYTHONDONTWRITEBYTECODE=1
job() { cfg="$1"; tag="$2"; shift 2; d="out/$cfg"; mkdir -p "$d"; o="$d/$tag.out"
  [ -s "$o" ] && grep -q '^TOTAL' "$o" && return 0
  timeout ${TO:-1500} python3 r2rf.py "$@" > "$o.tmp" 2>&1; echo "exit $?" >> "$o.tmp"; mv "$o.tmp" "$o"; }
export -f job
{
for r in howard allleast oneleast onebest onerand subrand allrand; do
  for f in $(ls -S -r inst/*.json); do echo "fz_$r $(basename $f .json) --rule $r --seed 4011 $f"; done
done
for r in howard allleast oneleast onebest onerand subrand allrand; do
  for s in 4021 4022 4023; do echo "rnd_$r any_$s --rule $r --seed $s --gen 100 $s any"; done
  echo "rnd_$r self_4024 --rule $r --seed 4024 --gen 100 4024 self"
  for b in BLKX26 CFI3 CW4_n K1F21 K1L10 K1L7 MWR4_2 RINT; do
    f=$(ls inst/$b*.json 2>/dev/null | head -1); [ -n "$f" ] && echo "mut_$r ${b}_4031 --rule $r --seed 4031 --mut 25 4031 $f"; done
done
for f in $(ls -S -r inst/*.json | head -20); do
  echo "ctl_worsen $(basename $f .json) --rule worsen $f"
  for c in k5t nsp0 tailshift rfc hval; do echo "ctl_$c $(basename $f .json) --rule oneleast --rctrl $c $f"; done
done
} | xargs -P ${P:-2} -L 1 bash -c 'job $0 "$@"'
