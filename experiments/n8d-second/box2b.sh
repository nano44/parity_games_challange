#!/usr/bin/env bash
# Box 2b (Lead 08:34Z): R2 seeds 1-5 under four start/tie settings, kl2fast. Output experiments/n8d-second/results-2b/.
#   first   = tau_1 first successor (file order), as frozen
#   last    = tau_1 last successor (= edges reversed in file order; checked identical on switchbestexp 8)
#   rand    = tau_1 drawn per Odd node by random.Random(7) (its own generator, independent of R2's seed)
#   relabel = node ids reversed (variants.py relabel): every smallest-id tie-break flips; tau_1 = first successor (same arcs)
set -u
cd "$(dirname "$0")/../.."
B=experiments/n8d-second/bench.py; V=experiments/n8d-second/variants.py; R=experiments/n8d-second/results-2b
mkdir -p "$R" experiments/n8d-second/out/r1k experiments/n8d-second/out/r1k-relabel
HF="python3 experiments/hard-families/pgsolver_port.py"
for f in $(ls experiments/n8d-second/out/rand10k/*.pg | sort | head -1000); do
  ln -sf "$(realpath "$f")" experiments/n8d-second/out/r1k/
  python3 $V relabel "$f" experiments/n8d-second/out/r1k-relabel/$(basename "$f")
done
J=${JOBS:-4}
run() {  # name fam sizes tau1 genprefix
  python3 $B family "$2" --gen "$5$HF $2 {N}" --sizes $3 --seeds 1 2 3 4 5 --no-r1 --jobs $J --timeout 7200 --impl kl2fast \
    --tau1 "$4" --out "$R/$2.$1.csv" > "$R/$2.$1.log" 2>&1; echo "$2 $1 exit $? $(tail -1 "$R/$2.$1.log")"; }
for fam in "switchallexp:8 12 16 20 24 28" "switchbestexp:10 14 18 22 26 30"; do
  f=${fam%%:*}; s=${fam#*:}
  run first "$f" "$s" first ""
  run last "$f" "$s" last ""
  run rand "$f" "$s" rand7 ""
  run relabel "$f" "$s" first "python3 $V relabel -- "
done
for st in first:first:r1k last:last:r1k rand:rand7:r1k relabel:first:r1k-relabel; do
  IFS=: read name t d <<< "$st"
  python3 $B corpus experiments/n8d-second/out/$d --seeds 1 2 3 4 5 --no-r1 --jobs $J --timeout 600 --impl kl2fast --tau1 "$t" \
    --out "$R/rand1k.$name.csv" > "$R/rand1k.$name.log" 2>&1; echo "rand1k $name exit $? $(tail -1 "$R/rand1k.$name.log")"
done
echo "box2b done"
