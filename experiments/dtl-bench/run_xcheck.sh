#!/usr/bin/env bash
# Second-implementation cross-check (dtl_py.py vs Oink pinned dtl/idtl): every corpus of the step-2 bench.
set -uo pipefail
cd "$(dirname "$0")"
J="${J:-4}"
[ -n "${SKIP_EXH:-}" ] || for np in "1 1" "2 2" "3 3"; do set -- $np
  python3 xcheck.py exhaustive $1 $2 --csv results/xcheck_exhaustive_n$1_P$2.csv --jobs $J --order oink | tail -6; done
python3 xcheck.py files out/g10k --csv results/xcheck_g10k.csv --jobs $J --order oink | tail -6
python3 xcheck.py files out/rn --csv results/xcheck_rngame.csv --jobs $J --order oink | tail -6
python3 xcheck.py files out/small50k --csv results/xcheck_small50k.csv --jobs $J --order oink | tail -6
python3 xcheck.py files $(cat out/xcheck_fam_list.txt) --csv results/xcheck_families.csv --jobs $J --order oink --timeout 900 | tail -8
# C5-literal choices (CH1 stable, CH2 ascending ins, CH3 pop order): regions/strategies must agree, counts may differ.
python3 xcheck.py files out/rn --csv results/xcheck_rngame_orderstable.csv --jobs $J --order stable | tail -6
python3 xcheck.py files out/small50k --csv results/xcheck_small50k_orderstable.csv --jobs $J --order stable | tail -6
