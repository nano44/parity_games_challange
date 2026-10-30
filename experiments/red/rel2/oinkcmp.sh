#!/bin/bash
# L-RED R143: N5 (n5b SPEC, from the pin's start) winners vs Oink --zlk winners (8fbf0a7), plus Oink's verify of N5's strategies.
# Usage: oinkcmp.sh GAME.pg START   (prints "OINK OK" or "OINK DIFFER")
d=$(dirname "$0"); O="$d/../../../tools/oink/build"; t=$(mktemp -d)
python3 -I "$d/../../n5-second/n5b.py" "$1" "$t/n5.sol" --start "$2" --mode spec > /dev/null || { echo "n5b failed"; exit 1; }
"$O/oink" --zlk "$1" "$t/oink.sol" > /dev/null 2>&1 || { echo "oink failed"; exit 1; }
w() { grep -v '^paritysol' "$1" | sed 's/;//' | awk '{print $1, $2}' | sort -n; }
"$O/verify" "$1" "$t/n5.sol" > "$t/v.log" 2>&1; vr=$?
if [[ "$(w "$t/n5.sol")" == "$(w "$t/oink.sol")" && $vr == 0 ]]; then echo "OINK OK"; else echo "OINK DIFFER (verify exit $vr)"; cat "$t/v.log"; fi
rm -rf "$t"
