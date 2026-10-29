#!/usr/bin/env bash
# Fast self-check of box 21 (run by scripts/verify.sh via experiments/*/check.sh): hard-families/pgsolver_port.py regenerates every pinned
# friedmannsubexp / fearnleysubexp instance (N = 1..8) byte for byte (sha1), and n5b SPEC from S3 takes 19 iterations, 0 fallbacks, on
# friedmannsubexp_4 and 14 iterations, 0 fallbacks, on fearnleysubexp_4 (results/run21_S3.log).
set -e
cd "$(dirname "$0")"
for g in friedmannsubexp fearnleysubexp; do for N in 1 2 3 4 5 6 7 8; do
  [ "$(python3 ../hard-families/pgsolver_port.py $g $N | sha1sum | cut -d' ' -f1)" = "$(sha1sum < instances/${g}_$N.pg | cut -d' ' -f1)" ] || { echo "n5-box21 check FAILED: $g $N sha1"; exit 1; }
done; done
python3 ../n5-second/n5b.py instances/friedmannsubexp_4.pg --mode spec | grep -q "^n5b iterations 19 fallbacks 0 " || { echo "n5-box21 check FAILED: n5b friedmannsubexp_4"; exit 1; }
python3 ../n5-second/n5b.py instances/fearnleysubexp_4.pg --mode spec | grep -q "^n5b iterations 14 fallbacks 0 " || { echo "n5-box21 check FAILED: n5b fearnleysubexp_4"; exit 1; }
echo "n5-box21 check OK"
