#!/usr/bin/env bash
# Fast self-check of box 16 (run by scripts/verify.sh via experiments/*/check.sh): hn.py regenerates the pinned H_3 and H_5 (sha1,
# Fact 8.1 asserted inside hn.py), I^glo from ι on H_3 takes 107 steps (= 16*2^3 - 21, [F] Theorem 8.4: >= 2^3), and n5b SPEC from
# S3 on H_5 takes 34 iterations (= 6*5 + 4), 0 fallbacks.
set -e
cd "$(dirname "$0")"
T="$(mktemp -d)"; trap 'rm -rf "$T"' EXIT
python3 hn.py 3 --out "$T/h3.pg"; python3 hn.py 5 --out "$T/h5.pg"
[ "$(sha1sum < "$T/h3.pg" | cut -d' ' -f1)" = "$(sha1sum < instances/H3.pg | cut -d' ' -f1)" ] || { echo "friedmann-hn check FAILED: H3 sha1"; exit 1; }
[ "$(sha1sum < "$T/h5.pg" | cut -d' ' -f1)" = "$(sha1sum < instances/H5.pg | cut -d' ' -f1)" ] || { echo "friedmann-hn check FAILED: H5 sha1"; exit 1; }
python3 iglo.py 3 | grep -q "I^glo steps 107 " || { echo "friedmann-hn check FAILED: I^glo H3"; exit 1; }
python3 ../n5-second/n5b.py "$T/h5.pg" --mode spec | grep -q "^n5b iterations 34 fallbacks 0 " || { echo "friedmann-hn check FAILED: n5b H5 S3"; exit 1; }
echo "friedmann-hn check OK"
