#!/usr/bin/env bash
# L-SI box 85: regenerate the frozen TWO-COPIES instances from cfg/*.json (two85.py) into DIR (default inst/).
set -euo pipefail; cd "$(dirname "$0")"; d=${1:-inst}
for c in cfg/*.json; do i=$(basename "$c" .json); python3 -I -B two85.py "$c" "$d/$i.json"; done
