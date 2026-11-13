#!/usr/bin/env bash
# Box 218 DATA (deterministic: fixed seeds and iteration counts; about 6 minutes). Run from experiments/new/box218: bash run218.sh
# Resumable: a finished output (last line DONE) is skipped. Records go to out/rec (one best genome per run, overwritten per class/d/seed).
set -uo pipefail
job() { local f="out/$1"; shift; if [ -f "$f" ] && [ "$(tail -1 "$f")" = "DONE" ]; then return 0; fi; "$@" > "$f.tmp" 2>&1 && echo DONE >> "$f.tmp" && mv "$f.tmp" "$f"; }
one() { local env="$1" d="$2" s="$3" it="$4"; echo "class [$env] d $d seed $s iters $it: $(env $env python3 lad218.py climb $d $s $it out/rec | tail -1)"; }
export -f one
job xcheck218.out bash -c 'python3 lad218.py xcheck 1 300 5; LAD218_LEVR=0 python3 lad218.py xcheck 2 300 6; LAD218_TPL=down python3 lad218.py xcheck 3 200 5; python3 lad218.py show inst/up_k2_d4.json inst/up_k3_d6.json'
job climb218_templates.out bash -c 'for c in LAD218_PURE=1 LAD218_TPL=mirror LAD218_TPL=mirror1 LAD218_TPL=mid LAD218_TPL=up2 LAD218_TPL=down "LAD218_TPL=down LAD218_LEVR=0"; do for d in 4 6; do for s in 1 2; do one "$c" $d $s 150000; done; done; done'
job climb218_upward.out bash -c 'for c in LAD218_LEVR=1 LAD218_LEVR=0 "LAD218_NEAR=1 LAD218_LEVR=1"; do for d in 4 6; do for s in 1 2 3; do one "$c" $d $s 250000; done; done; done; for s in 1 2; do one LAD218_LEVR=0 8 $s 600000; done'
job climb218_seeded.out bash -c 'for s in 1 2 3; do one "LAD218_SEED=inst/up_k2_d4.json" 6 $s 250000; done; for s in 11 12; do one "LAD218_SEED=inst/up_k3_d6.json LAD218_STALL=20000" 8 $s 600000; done'
