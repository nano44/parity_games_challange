#!/bin/bash
# one process per (config, genome file); TOTAL line per output; run from tool/
export R2DIR=/home/user/parity_games_challange/docs/referee-2 PYTHONDONTWRITEBYTECODE=1
job() { cfg="$1"; f="$2"; shift 2; d="out/$cfg"; mkdir -p "$d"; o="$d/$(basename $f .json).out"
  [ -s "$o" ] && grep -q '^TOTAL' "$o" && return 0
  timeout 5400 python3 r2lv.py "$@" "$f" > "$o.tmp" 2>&1; echo "exit $?" >> "$o.tmp"; mv "$o.tmp" "$o"; }
export -f job
{
for f in ../records/*.json; do echo "rec_max_gate $f --tie max --eorder gate"; echo "rec_min_lev $f --tie min --eorder lev"; done
for f in $(ls -S -r ../corpus/*.json); do echo "cor_max_gate $f --tie max --eorder gate"; done
for f in $(ls -S -r ../corpus/*.json); do echo "cor_min_lev $f --tie min --eorder lev"; done
} | xargs -P ${P:-3} -L 1 bash -c 'job $0 "$@"'
