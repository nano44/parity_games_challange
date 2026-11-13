#!/usr/bin/env bash
# L-SI box 90: extract the pinned engines (pins.txt) into a temp dir and run mult90 (both engines) + ra227 + pair198 on the given genomes.
set -u
cd "$(dirname "$0")"
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p "$T/lred" "$T/lnew"
git -C "$(git rev-parse --show-toplevel)" archive ea985380 experiments/red | tar -x -C "$T/lred" || exit 3
git -C "$(git rev-parse --show-toplevel)" archive fcba92fc experiments/new experiments/si/si.py experiments/harness | tar -x -C "$T/lnew" || exit 3
export OWN_DIR="$T/lred/experiments/red/r221" ROOT="$T/lnew"
python3 -I mult90.py own "$@"
python3 -I mult90.py g3 "$@"
for f in "$@"; do python3 -I "$T/lred/experiments/red/r227/ra227.py" "$f" | tail -1; python3 -I "$T/lnew/experiments/new/box198/pair198.py" "$f" | sed -n 1p; done
