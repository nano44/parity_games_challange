#!/usr/bin/env bash
# L-SI box 83 LADDER-R (docs/si/box83-ladder.md) self-check: pins --strict (frozen instances); the builder regenerates them byte-equal;
# the DSL reproduces L-RED's RS2 genome (box81/inst/RS2.json); meas83 / lock83 (Lemma LOCK-UP, Corollary LADDER-2) / census81 / anal82 /
# real81 (N5'-xi and N5 on Gamma3) / xchk81 re-run on the frozen instances and diffed with out/; the 48-genome sweep re-run and diffed.
set -euo pipefail
cd "$(dirname "$0")"
sha1sum -c --quiet --strict pins.sha1
t=$(mktemp -d); mkdir -p "$t/inst"
python3 -I -B rs2port83.py 4 3 "$t/rs2.json"; cmp -s "$t/rs2.json" ../box81/inst/RS2.json
I="LR2_none LR2_exitup LR2_chainup LR3_exitup LR3_chainup LR6_exitup"
sed "s#inst/#$t/inst/#g; s#cd \"\$(dirname \"\$0\")\"#cd \"$(pwd)\"#" mkinst83.sh > "$t/mk.sh"; bash "$t/mk.sh"
for i in $I; do
  cmp -s "$t/inst/$i.json" inst/$i.json; cmp -s "$t/inst/$i.names.json" inst/$i.names.json
  python3 -I -B meas83.py inst/$i.json ../box81 -v > "$t/m"; diff -q "$t/m" out/meas_$i.out
  python3 -I -B ../box81/census81.py inst/$i.json > "$t/c"; diff -q "$t/c" out/census_$i.out
  python3 -I -B ../box82/anal82.py inst/$i.json ../box81 > "$t/a"; diff -q "$t/a" out/anal_$i.out
  python3 -I -B ../box81/xchk81.py inst/$i.json > "$t/x"; diff -q "$t/x" out/xchk_$i.out
  grep -q "game SAME states SAME .* valuediffs 0 hist SAME .* labels SAME" out/xchk_$i.out
done
for i in LR2_none LR2_exitup LR2_chainup LR3_exitup LR3_chainup; do
  python3 -I -B ../box81/real81.py inst/$i.json > "$t/r"; diff -q "$t/r" out/real_$i.out
done
python3 -I -B lock83.py ../box81 $(for i in $I; do echo inst/$i.json; done) > "$t/l"; diff -q "$t/l" out/lock83_inst.out
bash sweep83.sh "$t/sw" > "$t/s"; diff -q "$t/s" out/sweep83.out
rm -rf "$t"
echo "box 83 checks: PASS"
