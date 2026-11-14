#!/usr/bin/env bash
# L-SI box 91 check (~1 min): (1) frozen instances match inst/SHA1SUMS; (2) if the pinned commits are present, the own engine on
# WC4_2 / MW8_2 / C6G8_n54 / RWX_n95 equals the recorded rows of out/own91.out, and the four controls on MW8_2 equal out/ctrl91.out.
set -u
cd "$(dirname "$0")"
fail=0
(cd inst && sha1sum -c --quiet SHA1SUMS) || { echo "BOX91 FAIL sha1"; fail=1; }
TOP=$(git rev-parse --show-toplevel)
if git cat-file -e 4b309716^{commit} 2>/dev/null; then
  T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
  git -C "$TOP" archive 4b309716 experiments/red/r221 | tar -x -C "$T" || exit 3
  export OWN_DIR="$T/experiments/red/r221"
  got=$(python3 -I mult91.py own inst/WC4_2.json inst/MW8_2.json inst/C6G8_n54.json inst/RWX_n95.json | grep -v '^engine')
  want=$(grep -E '^own (WC4_2|MW8_2|C6G8_n54|RWX_n95)\.json' out/own91.out)
  [ "$got" = "$want" ] || { echo "BOX91 FAIL own rows"; echo "$got"; fail=1; }
  for c in a0 pre gr uz; do
    g=$(CTRL=$c python3 -I mult91.py own inst/MW8_2.json | grep -v '^engine' | sed "s/^own/ctrl=$c own/")
    w=$(grep -E "^ctrl=$c own MW8_2\.json" out/ctrl91.out)
    [ "$g" = "$w" ] || { echo "BOX91 FAIL control $c"; fail=1; }
  done
else
  echo "BOX91 NOT RUN engine rows (pinned commit 4b309716 absent)"
fi
[ $fail = 0 ] && echo "BOX91 OK" || exit 1
