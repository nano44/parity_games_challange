#!/usr/bin/env bash
# L-SI box 84 HUB PAIR (docs/si/box84-hubpair.md) self-check: pins; builder regenerates the frozen instances byte-equal; meas83 /
# census81 / anal82 / lock83 re-run on all, real81 / xchk81 on HP2-HP4, diffed with out/.
set -euo pipefail
cd "$(dirname "$0")"
sha1sum -c --quiet --strict pins.sha1
cmp -s gen83.py ../box83/gen83.py   # byte copy of the box 83 DSL
t=$(mktemp -d); mkdir -p "$t/inst"
sed "s#inst/#$t/inst/#g; s#cd \"\$(dirname \"\$0\")\"#cd \"$(pwd)\"#" mkinst84.sh > "$t/mk.sh"; bash "$t/mk.sh"
for i in HP2_mup HP3_mup HP3_mup0 HP4_mup HP5_mup; do
  cmp -s "$t/inst/$i.json" inst/$i.json; cmp -s "$t/inst/$i.names.json" inst/$i.names.json
  python3 -I -B ../box83/meas83.py inst/$i.json ../box81 -v > "$t/m"; diff -q "$t/m" out/meas_$i.out
  python3 -I -B ../box81/census81.py inst/$i.json > "$t/c"; diff -q "$t/c" out/census_$i.out
  python3 -I -B ../box82/anal82.py inst/$i.json ../box81 > "$t/a"; diff -q "$t/a" out/anal_$i.out
  python3 -I -B ../box83/lock83.py ../box81 inst/$i.json > "$t/l"; diff -q "$t/l" out/lock_$i.out
done
for i in HP2_mup HP3_mup HP4_mup; do
  python3 -I -B ../box81/real81.py inst/$i.json > "$t/r"; diff -q "$t/r" out/real_$i.out
  python3 -I -B ../box81/xchk81.py inst/$i.json > "$t/x"; diff -q "$t/x" out/xchk_$i.out
  grep -q "game SAME states SAME .* valuediffs 0 hist SAME .* labels SAME" out/xchk_$i.out
done
rm -rf "$t"
echo "box 84 checks: PASS"
