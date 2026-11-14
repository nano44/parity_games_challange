#!/usr/bin/env bash
# L-SI box 94: nested MW genomes (gennest94.py) -> inst/ (+ names, SHA1SUMS); mult91 (T, C), np93 (gate flips), lev94 (per-level change
# census) on both engines (pins as box91/pins.txt); own-only sweep over LINK x REV x SCALE x OFFJ at H = 2, n = 4. Output: out/*.out
set -u
cd "$(dirname "$0")"
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
mkdir -p "$T/lred" "$T/lnew" out inst
TOP=$(git rev-parse --show-toplevel)
git -C "$TOP" archive 4b309716 experiments/red/r221 | tar -x -C "$T/lred" || exit 3
git -C "$TOP" archive fcba92fc experiments/new experiments/si/si.py experiments/harness | tar -x -C "$T/lnew" || exit 3
export OWN_DIR="$T/lred/experiments/red/r221" ROOT="$T/lnew"
mk() { local nm=$1; shift; env "$@" python3 -I gennest94.py $H $n > inst/$nm.json 2> inst/$nm.names.json; }
for H in 2 3; do for n in 4 8; do
  mk NP${H}_$n LINK=u; mk NV${H}_$n LINK=v REV=1; mk ND${H}_$n LINK=D; mk NDV${H}_$n DBL=v; mk NDB${H}_$n DBL=b
done; done
H=2; n=4; mk NSQ2_4 LINK=u SCALE=3 OFFJ=24; H=3; mk NSQ3_4 LINK=u SCALE=3 OFFJ=24
(cd inst && sha1sum *.json > SHA1SUMS)
L=$(ls inst/*.json | grep -v names)
for e in own g3; do
  python3 -I ../box91/mult91.py $e $L > out/mult94_$e.out || exit 1
  python3 -I ../box93/np93.py $e $L > out/np94_$e.out || exit 1
  for f in $L; do python3 -I lev94.py $e $f ${f%.json}.names.json || exit 1; done > out/lev94_$e.out
done
{ for lk in u R D Dz zR v vQ; do for rev in "" 1; do for sc in 1 2 3; do for oj in 0 12 24; do
  REV=$rev LINK=$lk SCALE=$sc OFFJ=$oj python3 -I gennest94.py 2 4 > "$T/sw.json" 2>/dev/null
  a=$(python3 -I ../box91/mult91.py own "$T/sw.json" | tail -1 | awk '{print $3,$4,$5}')
  b=$(python3 -I ../box93/np93.py own "$T/sw.json" | tail -1 | awk '{print $5,$20,$21}')
  echo "LINK=$lk REV=${rev:-0} SCALE=$sc OFFJ=$oj | N+M T C: $a | flips maxgate ch_pe: $b"
done; done; done; done; } > out/sweep94_own.out || exit 1
echo DONE
