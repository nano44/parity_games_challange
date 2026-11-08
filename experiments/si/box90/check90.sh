#!/usr/bin/env bash
# L-SI box 90 check (~3-6 min): (1) gen90 regenerates every frozen instance byte for byte; (2) fibseq's abstract table equals out/fibseq.out;
# (3) if the pinned engine commits are present, both engines on FW4_2 / FW8_2 / FW6_3 equal the recorded rows of out/fw90.out.
set -u
cd "$(dirname "$0")"
fail=0
for f in inst/FW*_*.json; do
  case "$f" in *.names.json) continue;; esac
  b=$(basename "$f" .json); d=${b#FW}; k=${d#*_}; d=${d%_*}
  if ! cmp -s <(python3 -I gen90.py "$d" "$k" 2>/dev/null) "$f"; then echo "BOX90 FAIL regen $f"; fail=1; fi
done
cmp -s <(python3 -I fibseq.py 16) out/fibseq.out || { echo "BOX90 FAIL fibseq"; fail=1; }
if git cat-file -e ea985380^{commit} 2>/dev/null && git cat-file -e fcba92fc^{commit} 2>/dev/null; then
  got=$(./run90.sh inst/FW4_2.json inst/FW8_2.json inst/FW6_3.json 2>&1 | grep -E "^(own|g3) FW")
  want=$(grep -E "^(own|g3) FW(4_2|8_2|6_3)\.json" out/fw90.out)
  [ "$got" = "$want" ] || { echo "BOX90 FAIL engines"; echo "$got"; fail=1; }
else
  echo "BOX90 NOT RUN engine rows (pinned commits ea985380 / fcba92fc absent)"
fi
[ $fail = 0 ] && echo "BOX90 OK" || exit 1
