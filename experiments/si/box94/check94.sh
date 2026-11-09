#!/usr/bin/env bash
# L-SI box 94 check (~15 s): gennest94 H = 1 reproduces box 91's MW8_2; the frozen instances regenerate byte-equal (inst/SHA1SUMS);
# if the pinned commit is present, mult91 / np93 / lev94 on the own engine for NP2_4, NDV2_4, ND2_4 equal the recorded rows.
set -u
cd "$(dirname "$0")"
fail=0
python3 -I gennest94.py 1 8 2>/dev/null | cmp -s - ../box91/inst/MW8_2.json || { echo "BOX94 FAIL H=1"; fail=1; }
(cd inst && sha1sum -c --quiet --strict SHA1SUMS) || { echo "BOX94 FAIL inst sha1"; fail=1; }
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
g() { local nm=$1 H=$2 n=$3; shift 3; env "$@" python3 -I gennest94.py $H $n > "$T/$nm.json" 2>/dev/null; cmp -s "$T/$nm.json" inst/$nm.json || { echo "BOX94 FAIL regen $nm"; fail=1; }; }
g NP3_8 3 8 LINK=u; g NV2_4 2 4 LINK=v REV=1; g ND3_4 3 4 LINK=D; g NDV3_8 3 8 DBL=v; g NDB2_4 2 4 DBL=b; g NSQ3_4 3 4 LINK=u SCALE=3 OFFJ=24
TOP=$(git rev-parse --show-toplevel)
if git cat-file -e 4b309716^{commit} 2>/dev/null; then
  git -C "$TOP" archive 4b309716 experiments/red/r221 | tar -x -C "$T" || exit 3
  export OWN_DIR="$T/experiments/red/r221"; L="inst/ND2_4.json inst/NDV2_4.json inst/NP2_4.json"
  a=$(python3 -I ../box91/mult91.py own $L | grep -v '^engine'); [ "$a" = "$(grep -E '^own (NP2_4|NDV2_4|ND2_4)\.json' out/mult94_own.out)" ] || { echo "BOX94 FAIL mult rows"; fail=1; }
  b=$(python3 -I ../box93/np93.py own $L | grep -v '^engine'); [ "$b" = "$(grep -E '^own (NP2_4|NDV2_4|ND2_4)\.json' out/np94_own.out)" ] || { echo "BOX94 FAIL np rows"; fail=1; }
  c=$(for f in $L; do python3 -I lev94.py own $f ${f%.json}.names.json; done); [ "$c" = "$(grep -E '^own (ND2_4|NDV2_4|NP2_4)\.json' out/lev94_own.out)" ] || { echo "BOX94 FAIL lev rows"; fail=1; }
else
  echo "BOX94 NOT RUN engine rows (pinned commit 4b309716 absent)"
fi
[ $fail = 0 ] && echo "BOX94 OK" || exit 1
