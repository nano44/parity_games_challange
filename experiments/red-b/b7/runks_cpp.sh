#!/usr/bin/env bash
# B7: RF (C++ engine rf7) on K^s_n for n = $2..$3; resumable (skips an n whose line exists). Output OUT/ks_cpp.out.
# Usage: runks_cpp.sh RF7BIN NMIN NMAX OUTDIR
set -u
BIN="$1"; OUT="$4"; HERE="$(cd "$(dirname "$0")" && pwd)"; mkdir -p "$OUT/inst"
for n in $(seq "$2" "$3"); do
  grep -q "^B7 Ks-cpp n $n " "$OUT/ks_cpp.out" 2>/dev/null && continue
  python3 "$HERE/rfc2.py" "$n" --skip --pgonly --pg "$OUT/inst/Ks_$n.pg" "$OUT/inst/Ks_$n.start" || exit 1
  t0=$(date +%s)
  line=$("$BIN" rf "$OUT/inst/Ks_$n.pg" "$OUT/inst/Ks_$n.start") || exit 1
  t1=$(date +%s)
  law=$(python3 -c "print(7*2**($n-1)-2*$n-3)")
  sha=$(sha1sum "$OUT/inst/Ks_$n.pg" | cut -c1-40)
  echo "B7 Ks-cpp n $n law $law | $line | pg sha1 $sha secs $((t1-t0))" >> "$OUT/ks_cpp.out"
done
