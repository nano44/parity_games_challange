#!/bin/bash
# L-RED R187 pin checks: startck, Oink --zlk + verify vs N5 (rel2/oinkcmp.sh), Oink --tl + verify, xeng (two engines, same states).
# Usage: pinck.sh G.pg G.start   (prints one line; exit 1 on any failure)
d=$(dirname "$0"); R="$d/.."; O="$R/../../tools/oink/build"; t=$(mktemp -d)
python3 -I "$R/startck/startck.py" "$1" "$2" > /dev/null || { echo "STARTCK FAIL"; exit 1; }
a=$(bash "$R/rel2/oinkcmp.sh" "$1" "$2"); [[ "$a" == "OINK OK" ]] || { echo "ZLK: $a"; exit 1; }
"$O/oink" --tl "$1" "$t/tl.sol" > /dev/null 2>&1 || { echo "TL oink failed"; exit 1; }
"$O/verify" "$1" "$t/tl.sol" > /dev/null 2>&1 || { echo "TL verify failed"; exit 1; }
x=$(python3 -I "$R/seg/xeng.py" "$1" "$2" | tail -1); [[ "$x" == "state sequences identical: True" ]] || { echo "XENG: $x"; exit 1; }
rm -rf "$t"; echo "PIN OK $(basename "$1") (startck, zlk+verify, tl+verify, xeng)"
