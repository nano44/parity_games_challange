#!/bin/bash
# REFEREE s34: re-run of my lane's box208_replay.py (s32; statements of box 208 = the packet's, see R-P-N5-LEVEL §6) on new seeds,
# the packet's frozen genomes (l-new 1e6df499 archive) and new mutants of the two longest-plateau bases.
cd "$(dirname "$0")/.."
for fam in rand deep wide acyc selfl; do python3 box208_replay.py gen $fam 3410 2000 > box208_logs/s34_gen_${fam}_3410.out 2>&1; echo "$fam exit $?"; done
python3 box208_replay.py files $(python3 -c "import json,glob;print(' '.join(f for f in sorted(glob.glob('/tmp/claude-0/-home-user-parity-games-challange/38720001-cd5c-50d8-a854-c66607f94371/scratchpad/pl/experiments/new/box20[2-7]/inst/*.json'))+sorted(glob.glob('/tmp/claude-0/-home-user-parity-games-challange/38720001-cd5c-50d8-a854-c66607f94371/scratchpad/pl/experiments/new/box191/inst/DEAD_SEG2P_d*.json')) if isinstance(json.load(open(f)),dict) and 'opts' in json.load(open(f))))") > box208_logs/s34_files_frozen.out 2>&1; echo "files exit $?"
python3 box208_replay.py mut 3420 300 6 /tmp/claude-0/-home-user-parity-games-challange/38720001-cd5c-50d8-a854-c66607f94371/scratchpad/pl/experiments/new/box203/inst/MWR4_2.json /tmp/claude-0/-home-user-parity-games-challange/38720001-cd5c-50d8-a854-c66607f94371/scratchpad/pl/experiments/new/box206/inst/CW4_n.json > box208_logs/s34_mut_3420.out 2>&1; echo "mut exit $?"
