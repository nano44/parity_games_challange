#!/usr/bin/env bash
cd "$(dirname "$0")"
for mode in weak strong; do for case in "1 2" "2 1" "2 2" "2 3" "2 4" "2 5" "2 6" "3 1" "3 2" "3 3" "3 4"; do
  set -- $case; python3 compute.py $1 $2 S $mode > out/${mode}_S_n$1_d$2.log 2>&1
done; done
python3 compute.py 2 6 V strong --eager --solver glucose4 --out results/automata/strong_V_n2_d6_eager_glucose.json > out/strong_V_n2_d6_eager_glucose.log 2>&1
python3 compute.py 2 6 E strong --eager --solver glucose4 --out results/automata/strong_E_n2_d6_eager_glucose.json > out/strong_E_n2_d6_eager_glucose.log 2>&1
python3 compute.py 3 6 V strong --eager --solver glucose4 --out results/automata/strong_V_n3_d6_eager_glucose.json > out/strong_V_n3_d6_eager_glucose.log 2>&1
python3 compute.py 3 6 V weak --eager --solver glucose4 --out results/automata/weak_V_n3_d6_eager_glucose.json > out/weak_V_n3_d6_eager_glucose.log 2>&1
