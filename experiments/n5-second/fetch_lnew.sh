#!/usr/bin/env bash
# Build out/root: L-NEW's generators and CSVs from claude/l-new (WITHOUT experiments/new/n5.py, which this lane must not
# read) + this repo's experiments/hard-families, experiments/harness, tools -> a root where L-NEW's `gen` commands run.
# Usage: fetch_lnew.sh [REV]   (default origin/claude/l-new)
set -euo pipefail
cd "$(dirname "$0")"; R="$(git rev-parse --show-toplevel)"; REV="${1:-origin/claude/l-new}"
rm -rf out/root; mkdir -p out/root/experiments
git -C "$R" archive "$REV" experiments/new | tar -x -C out/root --exclude=experiments/new/n5.py
[ ! -e out/root/experiments/new/n5.py ] || { echo "n5.py must not be extracted"; exit 1; }
cp -r "$R/experiments/hard-families" "$R/experiments/harness" out/root/experiments/; rm -rf out/root/experiments/hard-families/out
ln -sfn "$R/tools" out/root/tools
git -C "$R" rev-parse "$REV" > out/root/LNEW_REV; echo "out/root from $REV $(cat out/root/LNEW_REV)"
