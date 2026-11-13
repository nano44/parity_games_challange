#!/usr/bin/env bash
# L-SI box 92 check (~30 s): if the pinned commit is present, gate92 on the own engine for WC4_2 / MW8_2 / C6G8_n54 / RWX_n95 equals the
# recorded rows of out/own92.out, and the control row on C6G8_n54 equals out/ctrl92.out.
set -u
cd "$(dirname "$0")"
fail=0
TOP=$(git rev-parse --show-toplevel)
if git cat-file -e 4b309716^{commit} 2>/dev/null; then
  T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
  git -C "$TOP" archive 4b309716 experiments/red/r221 | tar -x -C "$T" || exit 3
  export OWN_DIR="$T/experiments/red/r221"; I=../box91/inst
  got=$(python3 -I gate92.py own $I/WC4_2.json $I/MW8_2.json $I/C6G8_n54.json $I/RWX_n95.json | grep -v '^engine')
  want=$(grep -E '^own (WC4_2|MW8_2|C6G8_n54|RWX_n95)\.json' out/own92.out)
  [ "$got" = "$want" ] || { echo "BOX92 FAIL own rows"; echo "$got"; fail=1; }
  ga=$(python3 -I astar92.py own $I/FW8_2.json $I/MW8_2.json $I/C6G8_n54.json | grep -v '^engine')
  [ "$ga" = "$(grep -E '^own (FW8_2|MW8_2|C6G8_n54)\.json' out/astar92_own.out)" ] || { echo "BOX92 FAIL astar rows"; echo "$ga"; fail=1; }
  g=$(CTRL=low python3 -I gate92.py own $I/C6G8_n54.json | grep -v '^engine' | sed 's/^own/ctrl=low own/')
  [ "$g" = "$(grep -E '^ctrl=low own C6G8_n54\.json' out/ctrl92.out)" ] || { echo "BOX92 FAIL control"; fail=1; }
else
  echo "BOX92 NOT RUN engine rows (pinned commit 4b309716 absent)"
fi
[ $fail = 0 ] && echo "BOX92 OK" || exit 1
