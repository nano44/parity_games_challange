#!/usr/bin/env bash
# L-SI box 106 §3.3-§3.4 runner (resumable: a job whose output line is already in its out/ file is skipped). Builds box 105's environment
# (LNEW, LRED as runclimb106.sh). Steps: audit | controls | query (see docs/si/box106-exact2.md §3b, §3c). Proofs go to dump/ (gitignored
# size rule: a DRUP proof is gzipped and kept in git only if <= 50 MB gzipped; its sha1 is printed either way). Checkers: drup.c (L-COMP,
# read-only copy ../box71/ref/drup.c) and REFEREE's ref_rup.c (claude/referee, read with git show; compiled in a temp dir).
set -u
cd "$(dirname "$0")"
export PYTHONDONTWRITEBYTECODE=1
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p out best dump "$T/red" "$T/new"
TOP=${TOP:-$(git rev-parse --show-toplevel)}; SI=${SI:-$TOP/experiments/si}
git -C "$TOP" archive 8c01d40e experiments/red/r217 | tar -x -C "$T/red" || exit 3
git -C "$TOP" archive fcba92fc experiments/new experiments/si/si.py experiments/harness experiments/hard-families experiments/n5-second | tar -x -C "$T/new" || exit 3
export LNEW="$T/new" LRED="$T/red" BOX104="${BOX104:-$SI/box104}"
step=${1:-audit}
job() {  # job OUTFILE PATTERN COMMAND...: run unless PATTERN is already a line of OUTFILE
  local f=$1 pat=$2; shift 2; touch "$f"; grep -q -- "$pat" "$f" && { echo "skip: $pat"; return 0; }
  "$@" >> "$f" || exit 1
}
if [ "$step" = audit ]; then
  job out/aud106.out "^AUD106 seed 1065 genomes 300 full:" python3 -I aud106.py 1065 300 --full
  job out/aud106.out "^AUD106 seed 1066 genomes 2000:" python3 -I aud106.py 1066 2000
  job out/aud106.out "^AUD106 seed json genomes 40 full:" python3 -I aud106.py json --full $(ls best/climb106_*.json | sort -V)
  for c in 1 2 3; do job out/aud106.out "^AUD106 seed 1067 genomes 100 CTRL $c:" env CTRL=$c python3 -I aud106.py 1067 100; done
fi
if [ "$step" = controls ]; then
  job out/solve106.out "^SOLVE106 c5 " python3 -I solve106.py 5 c5
  job out/solve106.out "^SOLVE106 g5 " python3 -I solve106.py 5 g5 --genome best/climb106_1.json
  job out/solve106.out "^SOLVE106 g6 " python3 -I solve106.py 6 g6 --genome best/climb106_1.json
  job out/solve106.out "^SOLVE106 c9 " python3 -I solve106.py 9 c9
fi
if [ "$step" = query ]; then
  job out/solve106.out "^SOLVE106 q6 " python3 -I solve106.py 6 q6
fi
echo DONE "$step"
