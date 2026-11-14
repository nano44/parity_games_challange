#!/usr/bin/env bash
# L-SI box 93 check (~20 s): inst sha1s; genk93 WT=D reproduces box 91's MW8_2 and WT=u / prev the frozen probes; if the pinned commit is
# present, np93 on the own engine for WC4_2 / MW8_2 / C6G8_n54 / k1fail_202 equals the recorded rows of out/own93.out and the control
# rows equal out/ctrl93.out; the K6 towers rebuild byte-equal from k6/cfg; recorded K6 lemma outputs show no violation.
set -u
cd "$(dirname "$0")"
fail=0
(cd inst && sha1sum -c --quiet --strict SHA1SUMS) || { echo "BOX93 FAIL inst sha1"; fail=1; }
(cd k6/inst && sha1sum -c --quiet --strict ../SHA1SUMS) || { echo "BOX93 FAIL k6 sha1"; fail=1; }
python3 -I genk93.py 8 2>/dev/null | cmp -s - ../box91/inst/MW8_2.json || { echo "BOX93 FAIL genk93 WT=D"; fail=1; }
WT=u python3 -I genk93.py 16 2>/dev/null | cmp -s - inst/Ku_16.json || { echo "BOX93 FAIL genk93 WT=u"; fail=1; }
WT=prev python3 -I genk93.py 8 2>/dev/null | cmp -s - inst/Kprev_8.json || { echo "BOX93 FAIL genk93 WT=prev"; fail=1; }
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
for c in k6/cfg/*.json; do python3 -I -B ../box86/lag86.py "$c" "$T/$(basename "$c")"; cmp -s "$T/$(basename "$c")" "k6/inst/$(basename "$c")" || { echo "BOX93 FAIL k6 rebuild $c"; fail=1; }; done
grep -qE "exU [1-9]|exE [1-9]" k6/out/flipu85.out && { echo "BOX93 FAIL flipu"; fail=1; }
grep -qv "mispredictions 0 " k6/out/lb84.out && { echo "BOX93 FAIL lb84"; fail=1; }
grep -qv "POOL-ALT violations 0" k6/out/pool85.out && { echo "BOX93 FAIL pool85"; fail=1; }
grep -qE "maxex_priv [1-9]|maxex_nopriv [1-9]" k6/out/priv84.out && { echo "BOX93 FAIL priv84"; fail=1; }
grep -qv "latch-violations 0$" k6/out/latch86.out && { echo "BOX93 FAIL latch86"; fail=1; }
TOP=$(git rev-parse --show-toplevel)
if git cat-file -e 4b309716^{commit} 2>/dev/null; then
  git -C "$TOP" archive 4b309716 experiments/red/r221 | tar -x -C "$T" || exit 3
  export OWN_DIR="$T/experiments/red/r221"; I=../box91/inst
  got=$(python3 -I np93.py own $I/WC4_2.json $I/MW8_2.json $I/C6G8_n54.json inst/k1fail_202.json | grep -v '^engine')
  [ "$got" = "$(grep -E '^own (WC4_2|MW8_2|C6G8_n54|k1fail_202)\.json' out/own93.out)" ] || { echo "BOX93 FAIL own rows"; echo "$got"; fail=1; }
  g=$(for c in swap tight; do CTRL=$c python3 -I np93.py own $I/MW8_2.json $I/C6G8_n54.json | sed "s/^own/ctrl=$c own/"; done)
  [ "$g" = "$(cat out/ctrl93.out)" ] || { echo "BOX93 FAIL control"; fail=1; }
else
  echo "BOX93 NOT RUN engine rows (pinned commit 4b309716 absent)"
fi
[ $fail = 0 ] && echo "BOX93 OK" || exit 1
