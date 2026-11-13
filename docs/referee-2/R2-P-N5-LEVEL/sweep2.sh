#!/bin/bash
# second sweep: every reference b on corpus (--ball), random genomes (own generator r2end.gen), own mutants (r2split.mutate); controls.
export R2DIR=/home/user/parity_games_challange/docs/referee-2 PYTHONDONTWRITEBYTECODE=1
job() { cfg="$1"; tag="$2"; shift 2; d="out/$cfg"; mkdir -p "$d"; o="$d/$tag.out"
  [ -s "$o" ] && grep -q '^TOTAL' "$o" && return 0
  timeout 6000 python3 r2lv.py "$@" > "$o.tmp" 2>&1; echo "exit $?" >> "$o.tmp"; mv "$o.tmp" "$o"; }
export -f job
{
for s in 3911 3912 3913 3914 3915 3916 3917 3918; do echo "gen_any $s --gen 250 $s any"; done
for s in 3921 3922 3923 3924; do echo "gen_self $s --gen 250 $s self"; done
for s in 3931 3932; do echo "gen_acyc $s --gen 250 $s acyc"; done
for s in 3941 3942 3943 3944; do echo "gen_any_tierand $s --tie rand --eorder lev --gen 250 $s any"; done
for b in BLKX26_n48 CFI3_n48 CW4_n K1F21_n48 K1L10_n48 K1L7_n48 MWR4_2 RINT_n48; do echo "mut $b --mut 100 3951 ../records/$b.json"; echo "mut_minlev $b --tie min --eorder lev --mut 100 3952 ../records/$b.json"; done
for c in fronthigh snonfvs yfront k5t edom hval htie p6out; do echo "ctrl_$c ctrl --ctrl $c ../records/DEAD_SEG2P_d4_N8.json ../records/DEAD_SEG2P_d7_N14.json ../records/DEAD_SEG2P_d9_N18.json ../records/CFI3_n48.json ../records/MWR4_2.json ../records/RINT_n48.json ../records/K1L10_n48.json ../corpus/WC8_2.json"; done
for f in $(ls -S -r ../corpus/*.json ../records/*.json); do echo "ball_max_gate $(basename $f .json) --ball $f"; done
} | xargs -P ${P:-3} -L 1 bash -c 'job $0 "$@"'
